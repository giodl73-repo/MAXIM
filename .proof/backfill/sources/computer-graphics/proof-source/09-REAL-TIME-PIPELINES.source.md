---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "09-REAL-TIME-PIPELINES.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-graphics:real-time-pipelines
kind: guide
module: computer-graphics
section: computer-graphics
title: Real-Time Pipelines
status: source-custody
source_custody: partial
current_path: computer-graphics/09-REAL-TIME-PIPELINES.md
canonical_path: computer-graphics/09-REAL-TIME-PIPELINES.md
backsource_ids: [proof-backfill:computer-graphics:09-realtime, git-history:computer-graphics:09-realtime]
concepts: [forward rendering, deferred shading, shadow mapping, post-processing, modern graphics APIs, frame budget]
root_concepts: [real-time rendering]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Real-Time Pipelines

## The Big Picture: Architecting a Frame Under a Budget

A real-time renderer must produce a finished frame in milliseconds — about 16.6 ms at 60 Hz,
8.3 ms at 120 Hz. Everything in this guide is about *architecture*: how to organize the
passes (geometry, lighting, shadows, post) so the frame fits the budget. This is where the
mathematical machinery of the prior guides is assembled into a shipping system.

```
+--------------------------------------------------------------------------------------+
|                      A MODERN REAL-TIME FRAME (one ~16ms budget)                     |
|                                                                                      |
|  SHADOW         GEOMETRY        LIGHTING        TRANSPARENCY     POST-PROCESS    UI  |
|  PASSES         PASS            PASS                                                 |
|                                                                                      |
|  render depth-> rasterize    -> shade lit      -> blend OIT  -> tonemap, AA,  -> HUD |
|  from each      scene (fwd     pixels (fwd        / sorted       bloom, DoF,         |
|  light          or G-buffer    inline OR          alpha          motion blur,        |
|  (shadow maps)  for deferred)  deferred pass)                    color grade         |
|                                                                                      |
|   [L3 shadows]  [L1 fwd/def]   [L1 fwd/def]      [transp]       [L4 post]   [L4 UI]  |
|                                                                                      |
|   Driven over an EXPLICIT API (Vulkan/D3D12/Metal) with command buffers [L5]         |
+--------------------------------------------------------------------------------------+
```

The frame is a *graph of passes* writing and reading render targets. The big architectural
fork is **forward vs deferred** (how lighting relates to geometry); shadows are their own
pre-passes; post-processing is a chain of full-screen compute/fragment passes; and the whole
thing is choreographed over an explicit modern API.

---

## Layer 1: Forward vs Deferred Shading

The central architecture decision. *Forward* shades each object against all lights as it
rasterizes. *Deferred* first writes surface data to a **G-buffer**, then shades once per
pixel in a separate pass.

```
  FORWARD                                DEFERRED
  -------                                --------
  for each object:                       PASS 1 (geometry): rasterize scene ->
     for each light: shade               G-buffer (albedo, normal, depth, rough...)
  -> cost ~ objects x lights             PASS 2 (lighting): for each light, shade the
  -> overdraw shades hidden pixels          G-buffer pixels it touches
                                         -> cost ~ pixels x lights (geometry decoupled
                                            from lighting; no overdraw shading)

      [obj]-->shade(all lights)           [scene]-->[ G-BUFFER ]-->[ shade per pixel ]
                                                      normal|albedo
                                                      depth |rough
```

| | Forward | Deferred |
|---|---|---|
| Lighting cost | objects × lights | pixels × lights (no overdraw) |
| Many lights | Expensive | Cheap (its whole point) |
| Transparency | Natural | Hard (G-buffer holds one layer) → forward pass for transparents |
| MSAA | Works | Awkward/costly (subsample G-buffer) |
| Material variety | Easy (any shader) | Constrained (G-buffer is fixed format) |
| Memory bandwidth | Low | High (fat G-buffer read/write) |

```
  THE MODERN ANSWER: hybrids that keep deferred's many-lights win without its costs.

  TILED / CLUSTERED forward (Forward+):  split the screen into tiles (and depth
     slices = clusters); cull lights per tile; forward-shade against only the lights
     that touch each tile. -> many lights + easy transparency + MSAA + material variety.

  VISIBILITY BUFFER: store only triangle/instance IDs per pixel; fetch material and
     shade in a deferred-like pass -> tiny G-buffer, scales to huge geometry (Nanite).
```

**Old world → new world.** Deferred shading is *decoupling*: separate "what surface is here"
(geometry pass) from "how is it lit" (lighting pass), so lighting cost no longer multiplies
by geometry/overdraw — the same decoupling instinct as splitting a fat request into a cheap
index pass plus a focused fetch. Clustered forward then re-couples them but with a *spatial
cull* (per-tile light lists) so each pixel only pays for nearby lights.

---

## Layer 2: The Frame Budget

```
  FRAME BUDGET (the hard constraint everything bends to):

     60 Hz  -> 16.6 ms / frame      120 Hz -> 8.3 ms      90 Hz (VR) -> 11.1 ms

     a frame is split across:  shadow passes + geometry + lighting + transparency
                               + post + UI + CPU submission, all overlapping GPU/CPU.

  CPU and GPU run PIPELINED: while the GPU renders frame N, the CPU prepares frame N+1.
     -> latency = ~2-3 frames; throughput = bounded by the slower of CPU/GPU per frame.

  "GPU-bound" vs "CPU-bound": profile to find which stage blows the budget;
     optimize that one. (Amdahl applies -- speeding up a non-bottleneck buys nothing.)
```

The budget is why every prior technique exists in the form it does: LOD (`07`) and mipmaps
(`05`) cut work to fit it; deferred/clustered shading fits many lights into it; MSAA over
SSAA (`05`) is the cheaper-AA-that-fits choice. Real-time graphics is constrained
optimization under a millisecond budget.

---

## Layer 3: Shadows

Shadows are *visibility from the light's point of view* — is the path from surface to light
blocked? The dominant real-time technique is the **shadow map**: render scene depth *from the
light*, then at shading time check whether each surface point is farther than the recorded
depth (occluded → in shadow).

```
  SHADOW MAPPING (two passes):

   PASS 1: render the scene depth FROM THE LIGHT -> shadow map (a depth texture)
   PASS 2: when shading point P, transform P into light space; compare its depth to
           the shadow map. farther than stored depth? -> in shadow.

      light                                  shade point P:
        \                                       project P to light space
         \  shadow map (depth from light)        depthP vs shadowmap[P.xy]
          \____________                          depthP >  stored -> SHADOWED
           |   |    |  |                          depthP <= stored -> LIT
        occluder  receiver

   ARTIFACTS + FIXES:
     "shadow acne" (self-shadowing)  -> depth BIAS / normal-offset / slope-scaled bias
     hard jagged edges (aliasing)    -> PCF (percentage-closer filtering: average
                                         several depth comparisons -> soft edge)
     coarse near, wasteful far       -> CASCADED shadow maps (CSM): several maps at
                                         different resolutions by distance (like LOD)
     contact-hardening soft shadows  -> PCSS / variance/moment shadow maps
```

The ray-traced alternative (`03`) is conceptually simpler — fire a shadow ray to the light,
test occlusion — and gives correct soft shadows from area lights without the bias/aliasing
fiddle, which is why ray-traced shadows are an increasingly common hybrid effect. Shadow maps
remain the workhorse because they piggyback on the rasterizer.

---

### Ambient Occlusion in Screen Space (SSAO)

The single most common "fake GI" effect deserves a closer look, because it shows the
screen-space pattern in miniature.

```
  SSAO: darken creases and contact points by sampling nearby DEPTH.

    at pixel P (with depth + normal from the G-buffer / depth buffer):
      sample N points in a hemisphere around P (oriented by the normal)
      for each sample: is its depth OCCLUDED by the depth buffer? (something nearer?)
      occlusion = fraction of samples blocked  ->  darken P by (1 - occlusion)

       open surface: few samples blocked -> bright
       inside a crease: many blocked      -> darkened (the contact-shadow look)

    HBAO / GTAO are refined variants (horizon-based / ground-truth) with better falloff.
```

SSAO approximates the *visibility* part of the ambient term (`04`) using only the depth
buffer already in hand — cheap, and it adds the contact shadows that flat ambient lacks. Its
screen-space nature is also its limit: it only knows about on-screen depth, so occlusion from
off-screen geometry is missed and it can darken incorrectly at screen edges. It is the
quintessential budget-fit approximation: a depth-buffer trick standing in for a hemisphere
integral.

## Layer 4: Post-Processing

After the lit scene is in an HDR buffer, a chain of **full-screen passes** (compute or
fragment) applies image-space effects before encoding for display (`08`).

```
  POST CHAIN (each pass reads the previous target, writes a new one):

   HDR scene -> | bloom |  bright-pass + blur, add back -> glow around highlights
             -> | SSAO  |  screen-space ambient occlusion -> contact darkening (fakes GI)
             -> | SSR   |  screen-space reflections -> cheap reflections from the depth+
                            color buffers (misses off-screen geometry)
             -> | motion blur | from per-pixel velocity (motion vectors)
             -> | depth of field | blur by circle-of-confusion from depth
             -> | TAA / upscale | temporal AA resolve; DLSS/FSR upscaling      [05]
             -> | tone map + color grade | HDR -> display range; LUT grade       [08]
             -> | encode sRGB / PQ |  for the display                            [08]

  SCREEN-SPACE methods are cheap because they reuse buffers already rendered (depth,
  normal, color, velocity) -- but they only "see" what's on screen (SSR/SSAO miss
  off-screen occluders/reflectors). That's the trade for fitting the frame budget.
```

Post-processing is where many "global" effects are *faked* in image space (SSAO ≈ ambient
occlusion, SSR ≈ reflections) precisely because the true versions (`04`) don't fit the budget.
Each is a band-aid over the rendering equation, cheaper than solving it, with characteristic
artifacts (screen-edge cutoff) that mark the approximation.

---

### Frame Pacing, V-Sync, and Variable Refresh

Hitting the *average* budget isn't enough — *consistency* is what the eye perceives as
smoothness. How the finished frame meets the display matters as much as how fast it renders.

```
  V-SYNC OFF      present immediately -> TEARING (a frame swap mid-scan shows two frames'
                  halves stitched at the tear line)
  V-SYNC ON       wait for the display's vblank -> no tearing, but if you miss a refresh
                  you drop to the next one: 60 -> 30 -> 20 fps cliffs + input latency
  TRIPLE BUFFER   render ahead into a 3rd buffer -> hides small stalls, adds latency
  VRR (G-Sync /   the DISPLAY waits for the GPU: refresh rate tracks frame rate within a
  FreeSync /      range -> no tearing AND no 60->30 cliff. The modern answer.
  Adaptive Sync)

  FRAME PACING: 60 fps with one 33 ms hitch reads as a STUTTER even though the average
  is fine. Even frame times > high-but-jittery average. Profile the 99th percentile,
  not just the mean.
```

This is why shipping renderers chase *frame-time variance*, not just average FPS: a steady
16.6 ms is smoother than a jittery 12 ms with occasional 30 ms spikes. The whole budget
discipline (Layer 2) is ultimately about predictable pacing.

## Layer 5: Modern Explicit APIs

The CPU drives the GPU through a graphics API. The generation shift (mid-2010s) moved from
*implicit* drivers to *explicit* control.

```
  IMPLICIT (OpenGL, D3D11)            EXPLICIT (Vulkan, D3D12, Metal, WebGPU)
  ----------------------              ---------------------------------------
  driver tracks state, hazards,       YOU build command buffers, manage memory,
  memory, synchronization             insert barriers, own pipeline-state objects
  one thread submits draws            many threads record command buffers in parallel
  high per-draw CPU overhead          low overhead; predictable; explicit sync

      app -> GL calls -> [DRIVER       app threads -> record cmd buffers -> queue submit
                          guesses]                    -> GPU
```

```
  KEY EXPLICIT-API CONCEPTS:
     COMMAND BUFFER     pre-recorded list of GPU work (record on many threads, submit once)
     PIPELINE STATE OBJ all fixed-function + shader state baked into one immutable object
                        -> no costly mid-frame state changes; compile cost paid up front
     EXPLICIT BARRIERS  you declare resource transitions/dependencies (read-after-write etc.)
     DESCRIPTOR SETS    how shaders bind to resources (textures/buffers) in bulk
     SWAPCHAIN          the set of framebuffers presented to the display (double/triple buffer)
```

**Old world → new world.** The implicit→explicit shift is the managed-runtime→manual-control
trade applied to the GPU: OpenGL/D3D11 hide memory and synchronization (convenient, single-
threaded bottleneck) the way a garbage-collected runtime hides allocation; Vulkan/D3D12 hand
you the command buffers, memory, and barriers (more code, fewer surprises, parallel
submission) the way manual memory management does. WebGPU is the modern, safer middle ground
for the browser.

---

## Worked Example: Budgeting a 60 Hz Frame

A scene targets 60 Hz (16.6 ms) with deferred shading, cascaded shadows, and TAA. Rough GPU
time split, and what to do when it overruns:

```
  measured GPU times:
     shadow passes (4 cascades) .... 3.5 ms
     G-buffer (geometry) ........... 4.0 ms
     lighting (clustered) .......... 5.0 ms
     transparency + particles ...... 1.5 ms
     post (bloom, SSAO, TAA, tonemap) 3.5 ms
     ----------------------------------------
     total ......................... 17.5 ms   -> 0.9 ms OVER budget (would drop to ~57 fps)

  PROFILE says lighting is the largest term. Options, cheapest first:
     - tighten clustered light culling (fewer lights per cluster)         -> ~1 ms
     - drop a shadow cascade resolution at distance                       -> ~0.7 ms
     - lower G-buffer precision / fewer channels                          -> ~0.5 ms
     - DLSS/FSR: render at 67% resolution, upscale -> cuts lighting+post  -> several ms

  Pick ONE that closes the 0.9 ms gap (Amdahl: optimize the bottleneck, not the
  3.5 ms shadow pass that's already comfortable). Re-profile; budgets shift as you cut.
```

This is the daily reality of real-time rendering: profile, find the bottleneck pass, cut it
to fit the millisecond budget, re-profile. The algorithms from the prior guides are the
*levers*; the budget is the *constraint*.

---

## Old World → New World Bridges

| You already know | Here it is |
|------------------|-----------|
| Decoupling concerns into stages | Deferred shading: geometry pass vs lighting pass |
| A pass/pipeline DAG of dependent stages | The frame graph (passes reading/writing targets) |
| CPU/GPU pipelining (producer/consumer) | Frame N+1 on CPU while GPU renders frame N |
| Amdahl's law / optimize the bottleneck | Profile the frame; cut the slowest pass only |
| Caching/reusing computed buffers | Screen-space effects reuse depth/normal/velocity |
| Managed runtime vs manual memory | Implicit (GL/D3D11) vs explicit (Vulkan/D3D12) APIs |
| Spatial culling / indexing | Tiled/clustered light culling per screen tile |
| LOD/mip band-limiting to fit budget (`05`,`07`) | Cascaded shadow maps: resolution by distance |

---

## Decision Cheat Sheet

| Situation | Choice |
|---|---|
| Many dynamic lights | Deferred or clustered/tiled forward |
| Heavy transparency, varied materials, MSAA | Forward (or clustered forward / Forward+) |
| Massive geometry, tiny G-buffer | Visibility buffer (Nanite-style) |
| Real-time shadows | Cascaded shadow maps + PCF (or ray-traced shadows) |
| Soft area-light shadows, correct | Ray-traced shadows (hybrid) |
| Cheap fake reflections/AO | SSR / SSAO (accept screen-edge artifacts) |
| Antialiasing in a deferred renderer | TAA (MSAA is awkward on a G-buffer) |
| Hit a higher resolution/framerate | DLSS / FSR upscaling |
| Low CPU overhead, multi-threaded submit | Explicit API (Vulkan / D3D12 / Metal) |
| Frame over budget | Profile → cut the bottleneck pass (Amdahl) |

---

## Common Confusion Points

### "Forward or deferred — which is 'better'?"

Neither universally. Deferred decouples lighting from geometry so it scales to many lights
without overdraw, but struggles with transparency, MSAA, and material variety, and burns
bandwidth on a fat G-buffer. Forward handles those naturally but pays objects×lights. Modern
engines mostly use **clustered/tiled forward** (Forward+) to get deferred's many-lights win
while keeping transparency, MSAA, and material flexibility.

### "Why are real-time shadows so fiddly compared to ray-traced ones?"

Shadow maps approximate visibility by sampling a depth texture from the light, so they
inherit *sampling* problems: acne (self-shadow from depth quantization, fixed with bias),
aliasing (jagged edges, softened with PCF), and resolution allocation (cascades). Ray-traced
shadows test occlusion directly along a ray — no depth-map sampling, correct soft shadows from
area lights — at the cost of ray-tracing the scene. The fiddliness is the price of
piggybacking shadows on the rasterizer.

### "SSR/SSAO are 'screen-space' — what's the catch?"

They reuse buffers already on screen (depth, color, normals), which is cheap, but they can
only account for what's *visible*. SSR can't reflect off-screen geometry; SSAO misses
occluders outside the frame. So reflections vanish at screen edges and ambient occlusion is
incomplete — characteristic artifacts of fitting global effects into the frame budget by
faking them in image space.

### "Does upscaling (DLSS/FSR) just blur the image?"

Modern temporal upscalers render at lower resolution but *reconstruct* detail by accumulating
jittered samples across frames (the TAA mechanism, `05`) plus, for DLSS, a neural network
trained on high-res references. Done well, the result rivals native resolution at a fraction
of the cost — the trade is occasional ghosting/artifacts on fast motion and disocclusion, the
same temporal-reuse caveats as TAA.

### "Is the frame graph just the pipeline from the overview?"

The hardware *pipeline* (`00`, `06`) is the per-draw vertex→fragment flow. The **frame graph**
is the higher-level orchestration: the DAG of *passes* (shadows, G-buffer, lighting, post)
and the render targets they read/write, which the engine uses to schedule work, place
barriers, and alias memory. One is how a single draw flows through the GPU; the other is how a
whole frame's passes are wired together.
