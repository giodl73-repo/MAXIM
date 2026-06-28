---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-graphics:overview
kind: guide
module: computer-graphics
section: computer-graphics
title: Computer Graphics - Overview
status: source-custody
source_custody: partial
current_path: computer-graphics/00-OVERVIEW.md
canonical_path: computer-graphics/00-OVERVIEW.md
backsource_ids: [proof-backfill:computer-graphics:00-overview, git-history:computer-graphics:00-overview]
concepts: [rendering pipeline, rasterization, ray tracing, scene graph, shading, display]
root_concepts: [computer graphics]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Computer Graphics — Overview

## The Big Picture: Scene to Pixels

Every rendered image is the answer to one question: *given a description of a 3D
world and a virtual camera, what color is each pixel?* Everything in this directory
is a stage in answering it.

```
+------------------------------------------------------------------------------+
|                       THE RENDERING PIPELINE (scene -> pixels)               |
|                                                                              |
|  SCENE            GEOMETRY          VISIBILITY        SHADING        DISPLAY |
|  -----            --------          ----------        -------        ------- |
|                                                                              |
| +---------+     +-----------+     +-----------+     +----------+   +-------+ |
| | meshes  | --> | transform | --> | which     | --> | what     |-->| frame | |
| | lights  |     | to clip   |     | surface   |     | color is |   | buffer| |
| | camera  |     | space     |     | is seen   |     | it?      |   | -> sRGB| |
| | materials|    | (M·V·P)   |     | per pixel?|     | (BRDF +  |   | -> mon | |
| +---------+     +-----------+     +-----------+     |  lights) |   +-------+ |
|     |                |                 |             +----------+      |     |
|  [07,08]          [01]            [02 raster]          [04]        [08,09]   |
|                                  [03 ray-trace]                              |
|                                                                              |
|  GPU executes transform + visibility + shading in parallel  [06]            |
|  Textures feed material data into shading                   [05]            |
+------------------------------------------------------------------------------+
```

**Read this left to right.** A scene (geometry, lights, camera, materials) is
transformed into the camera's coordinate frame, the visible surface at each pixel is
determined, that surface is shaded to produce a color, and the result is written to a
framebuffer and sent to a display. The bracketed numbers point to the guide that owns
each stage.

---

## The Two Grand Strategies

Visibility — *which surface is seen at each pixel* — is the fork in the road. There are
two opposite ways to answer it, and almost all of graphics descends from this choice.

```
            THE SAME QUESTION, TWO OPPOSITE LOOPS

  RASTERIZATION                          RAY TRACING
  -------------                          -----------
  "For each triangle,                    "For each pixel,
   which pixels does it cover?"           which surface does its ray hit?"

  for triangle in scene:                 for pixel in image:
      project to screen                      ray = camera -> pixel
      for pixel in bbox:                     hit = closest_intersection(ray, scene)
          if inside triangle:                color = shade(hit)
              if closer (z-buffer):
                  shade + write

  Object order (scatter)                 Image order (gather)
  Cheap, parallel, hardware-native       Expensive, but physically natural
  Hard to do shadows/reflections         Shadows/reflections/GI are trivial
  Dominates real-time (games, UI)        Dominates film, offline, RTX hybrids
```

The deep duality: rasterization iterates **over geometry** and asks "where does this go
on screen"; ray tracing iterates **over pixels** and asks "what does this pixel see." A
rasterizer *scatters* primitives onto the image; a ray tracer *gathers* radiance into
each pixel. Modern GPUs now do both — hardware ray tracing (RTX, 2018) bolts intersection
units onto a rasterizing pipeline so renderers can use each where it is strongest.

| Axis | Rasterization | Ray Tracing |
|------|---------------|-------------|
| Loop order | Per-primitive (object order) | Per-pixel (image order) |
| Visibility | Z-buffer depth test | Closest-hit search along ray |
| Cost model | O(triangles × covered pixels) | O(pixels × log(scene)) with BVH |
| Global effects | Faked (shadow maps, SSR, probes) | Native (recurse the ray) |
| Acceleration | Tiling, early-Z, hierarchical Z | BVH / kd-tree spatial structures |
| Home turf | Real-time, interactive | Film, photoreal, offline |
| Guide | `02-RASTERIZATION.md` | `03-RAY-TRACING.md` |

---

## Layer 1: The Scene — What We Render

Before anything moves, the world must be described. Four ingredients:

```
+-------------------------------------------------------------------+
|                          THE SCENE                                |
|                                                                   |
|  GEOMETRY            MATERIALS         LIGHTS         CAMERA      |
|  --------            ---------         ------         ------      |
|  triangle meshes     BRDF params       point          position    |
|  curves / NURBS      albedo            directional    orientation |
|  subdivision         roughness         area            FOV / lens |
|  point clouds        metalness         environment     near/far   |
|  volumes             normal/disp maps  (IBL/HDRI)      proj type  |
|                                                                   |
|  [07-GEOMETRY]       [04][05]          [04-LIGHTING]   [01-PROJ]  |
+-------------------------------------------------------------------+
```

- **Geometry** is overwhelmingly **triangle meshes** — a triangle is the simplest planar
  primitive, is always convex and flat, and has trivial interpolation. Higher-order
  surfaces (Bézier patches, NURBS, subdivision) exist for authoring but are usually
  *tessellated* into triangles before rendering. (`07-GEOMETRY-AND-MESHES.md`)
- **Materials** describe how a surface interacts with light — historically ad-hoc (Phong
  exponents), now physically based (a BRDF with albedo, roughness, metalness).
  (`04`, `05`)
- **Lights** range from idealized point/directional sources to area lights and full
  image-based environment lighting. (`04`)
- **Camera** is a virtual pinhole (plus optional lens effects), defining the projection
  from 3D to 2D. (`01`)

---

## Layer 2: Geometry — Getting Into the Camera's Frame

This is pure linear algebra, and the learner's home territory — but the one *non-obvious*
move is the use of **homogeneous coordinates** so that translation and (critically)
*perspective* become matrix operations.

```
  OBJECT          WORLD           CAMERA          CLIP            SCREEN
  SPACE           SPACE           SPACE           SPACE           SPACE
  (local)         (shared)        (eye at origin) (cube)          (pixels)

  vertex  --M-->  vertex  --V-->  vertex  --P-->  vertex  --/w--> vertex
          model           view            proj            persp
          matrix          matrix          matrix          divide

  MVP = P · V · M   (applied right-to-left to a column vector)
```

Each matrix is 4×4 and operates on a 4-vector `(x, y, z, w)`. Translation lives in the
4th column; perspective lives in the bottom row (it writes `-z` into `w`, and the later
divide by `w` is what makes far things small). The order of composition is *not*
commutative — `T·R` (rotate then translate) differs from `R·T` (translate then rotate).
Full treatment in `01-TRANSFORMS-AND-PROJECTION.md`.

---

## Layer 3: Visibility — What Is Seen

Once geometry is in clip/screen space, the renderer must resolve occlusion. The modern
answer is almost always the **z-buffer** (depth buffer): per pixel, keep the nearest
fragment's depth, reject anything farther.

```
  PAINTER'S ALGORITHM (obsolete)        Z-BUFFER (universal)
  ------------------------------        --------------------
  sort all polygons back-to-front       per pixel store nearest depth z
  draw far ones first, near ones over   for each fragment:
                                            if z < zbuffer[x,y]:
  FAILS on intersecting / cyclic            zbuffer[x,y] = z
  overlap (no valid sort exists)            color[x,y]  = shade()

  O(n log n) sort, order-dependent       O(1) per fragment, order-independent
```

The painter's algorithm — sort and overpaint — breaks on mutually overlapping or
interpenetrating geometry (a cyclic occlusion graph has no valid back-to-front order).
The z-buffer sidesteps sorting entirely by deciding occlusion *per pixel*, at the cost of
one depth value per pixel. It is order-independent for opaque geometry, which is exactly
why it won. Detail in `02-RASTERIZATION.md`; the ray-traced analogue (closest-hit search)
is in `03-RAY-TRACING.md`.

---

## Layer 4: Shading — What Color Is It

Given the visible surface point, its material, and the lights, compute the outgoing
radiance toward the camera. This is the physics-rich core of the field, and it is
governed by one equation.

```
  THE RENDERING EQUATION (Kajiya, 1986)

  Lo(x, wo) = Le(x, wo)  +  INTEGRAL over hemisphere of:
                              f_r(x, wi, wo) · Li(x, wi) · (n · wi) dwi

  outgoing  =  emitted   +  (for every incoming direction:
  radiance                    BRDF × incoming radiance × cosine)

  Lo  outgoing radiance toward the eye
  Le  light the surface emits itself
  f_r the BRDF: how this material redirects light from wi to wo
  Li  incoming radiance from direction wi
  n·wi  Lambert cosine: grazing light contributes less
```

Every shading model is an approximation to this integral. **Phong/Blinn-Phong** (1970s)
hard-codes a diffuse-plus-specular guess. **Physically based rendering (PBR)** uses a
proper BRDF that obeys **energy conservation** (a surface cannot reflect more light than
it receives) and reciprocity. **Global illumination** actually attempts the recursive
integral — light bouncing between surfaces — via path tracing, photon mapping, or
radiosity. Full development in `04-SHADING-AND-LIGHTING.md`.

---

### Radiometry: The Units Everything Is Measured In

Before shading, a word on what "brightness" actually means, since the rendering equation is
stated in these terms.

```
  RADIANT FLUX (power)      watts                  total light energy per second
  IRRADIANCE                W/m²                    flux arriving per unit area
  RADIANT INTENSITY         W/sr                    flux per unit solid angle (a point light)
  RADIANCE (L)              W/(m²·sr)               flux per area per solid angle — THE one

  RADIANCE is the quantity a renderer computes because it is what a sensor/pixel
  measures and it is INVARIANT along a ray in a vacuum (doesn't fall off with distance
  — the inverse-square law is about irradiance, not radiance). That invariance is why
  "the radiance leaving a surface toward the eye" is exactly "the pixel's value".
```

This is why the rendering equation's `Lo` and `Li` are *radiances*: radiance is conserved
along an unoccluded ray, so the value computed at a surface is the value that reaches the
camera. The inverse-square falloff of a point light (`04`) is an *irradiance* effect — the
same power spread over a growing sphere — not a property of radiance itself.

---

## Layer 5: The GPU — Where It Runs

All of the above runs, in real time, on a **GPU**: a massively parallel processor built
to run the same small program (a *shader*) across millions of vertices and pixels at once.

```
  CPU  (latency-optimized)            GPU  (throughput-optimized)
  -----------------------             ---------------------------
  few fat cores                       thousands of thin lanes
  deep caches, branch prediction      SIMT: 32-lane warps in lockstep
  MIMD (each core does its own thing) one instruction, many data
  good at: control flow, serial work  good at: data-parallel, arithmetic

       FIXED + PROGRAMMABLE PIPELINE
   vertices -> [VERTEX SHADER] -> primitive assembly -> [RASTERIZER]
            -> fragments -> [FRAGMENT SHADER] -> blend -> framebuffer
   (also: tessellation, geometry, and general-purpose COMPUTE shaders)
```

The bridge to `computer-architecture/`: a GPU is the extreme end of the throughput-vs-
latency tradeoff. It hides memory latency not with caches but with massive
*oversubscription* — when one warp stalls on memory, another runs. The SIMT model
(single instruction, multiple threads) means **branch divergence** within a warp is
expensive: lanes that take different paths serialize. Covered in `06-GPU-AND-SHADERS.md`.

---

## How the Field Got Here (a timeline)

The pipeline above is the accumulated answer to 60 years of the same question. The bridges
in each guide make more sense against this arc.

```
  1963  Sutherland's Sketchpad — interactive graphics, the first GUI/CAD
  1971  Gouraud shading (smooth vertex interpolation)
  1973-77 Phong / Blinn-Phong reflection — the tuned model that ruled real-time for decades
  1974  Z-buffer (Catmull) — per-pixel visibility, the algorithm that won
  1980  Whitted ray tracing — recursive reflection/refraction/shadows
  1986  Kajiya's rendering equation + path tracing — the physics, stated once and for all
  1992  OpenGL standardized (from SGI's IRIS GL)
  2001  Programmable shaders (GeForce 3 / DirectX 8) — the fixed pipeline opens up
  2007  CUDA — GPUs become general compute; the road to deep learning
  ~2012  PBR goes mainstream (Disney "principled" BRDF, UE4) — physics replaces fudges
  2016  Explicit APIs (Vulkan, D3D12) — the driver gets out of the way
  2018  Hardware ray tracing (RTX) + DLSS — rasterize + trace hybrids, neural upscaling
  2021  Nanite/Lumen (UE5) — virtualized geometry + real-time GI
```

Two long arcs run through this: **fixed → programmable → general-purpose** (the hardware), and
**plausible fudge → physically based** (the math). Every guide here sits somewhere on those two
arcs.

---

## Old World → New World Bridges

| You already know | Graphics analogue |
|------------------|-------------------|
| A linear transform `Ax` | A vertex transform — but in *homogeneous* coords so translation is also a matrix |
| Change of basis | The view matrix: rebasing the world into the camera's frame |
| Depth-first traversal of a tree | Scene-graph traversal; BVH descent during ray tracing |
| A hash/spatial index for fast lookup | BVH / kd-tree: spatial acceleration so a ray skips most triangles |
| SIMD intrinsics on a CPU | SIMT warps on a GPU — wider, with hardware-managed divergence |
| MapReduce: map over a huge dataset | A fragment shader: the same kernel over every pixel |
| Nyquist sampling in DSP | Texture sampling and antialiasing — the *same* theorem (`signal-processing/`) |
| Numerical integration (quadrature) | Monte Carlo estimation of the rendering equation's hemisphere integral |
| sRGB / gamma in image files | Linear-light shading vs display-encoded output (`08`, `colors/`) |

---

## Decision Cheat Sheet

| I want to... | Look at |
|---|---|
| Understand 3D-to-2D math (matrices, projection) | `01-TRANSFORMS-AND-PROJECTION.md` |
| Know how triangles become pixels (z-buffer, interpolation) | `02-RASTERIZATION.md` |
| Render photorealistic reflections/shadows/GI | `03-RAY-TRACING.md` |
| Get materials physically right (BRDF, energy conservation) | `04-SHADING-AND-LIGHTING.md` |
| Stop textures from shimmering (mipmaps, filtering, AA) | `05-TEXTURING-AND-SAMPLING.md` |
| Write shaders / understand SIMT and GPU parallelism | `06-GPU-AND-SHADERS.md` |
| Represent meshes, curves, LOD | `07-GEOMETRY-AND-MESHES.md` |
| Get color/gamma/HDR/tone mapping correct | `08-COLOR-AND-PERCEPTION.md` |
| Architect a real-time renderer (deferred, shadows, post) | `09-REAL-TIME-PIPELINES.md` |
| Pick rasterization vs ray tracing | This file — the Two Grand Strategies table |

---

## Common Confusion Points

### "Is graphics rasterization OR ray tracing?"

Both, and increasingly *both at once*. Real-time historically meant rasterization; film
meant ray/path tracing. Since 2018, consumer GPUs ship hardware ray-intersection units,
so games rasterize the primary visibility pass and ray trace *selected* effects (shadows,
reflections, ambient occlusion). The question is no longer "which" but "which for this
effect, at this frame budget."

### "Why homogeneous coordinates? Aren't 3 numbers enough for a 3D point?"

Three numbers describe the point; the fourth (`w`) is what lets a single 4×4 matrix
express translation *and* perspective. A pure 3×3 linear map fixes the origin, so it can
rotate and scale but never translate. Lifting to 4D and treating points as `(x,y,z,1)`
makes translation a *shear* in the 4th dimension. Perspective then writes depth into `w`,
and the divide-by-`w` produces foreshortening. Full reasoning in `01`.

### "Rendering equation vs. ray tracing — same thing?"

No. The **rendering equation** (Kajiya 1986) is the *physics* — the integral equation
that any correct renderer must approximate. **Path tracing** is one *algorithm* for
approximating it (Monte Carlo sampling of light paths). Rasterization with shadow maps is
a *cruder* approximation of the same equation. The equation is the spec; renderers are
implementations.

### "Linear light vs. sRGB — why does it matter?"

Light is linear: two photons are twice one photon, and blending, filtering, and lighting
math are only correct in linear space. But displays and image files are *gamma-encoded*
(roughly sRGB) to match human perception and 8-bit precision. Doing math in the encoded
space — averaging two sRGB values, say — gives visibly wrong results (dark fringes on
edges, muddy blends). The fix: decode to linear, compute, re-encode for display. This bug
is everywhere; `08-COLOR-AND-PERCEPTION.md` and `colors/` cover it.

### "MSAA vs SSAA vs FXAA — all antialiasing?"

Yes, but at different costs. **SSAA** renders the whole image at higher resolution and
downsamples — correct but brutally expensive (shades every subsample). **MSAA** samples
*coverage* at multiple points per pixel but shades once per pixel per primitive — far
cheaper, targets only geometric edges. **FXAA/TAA** are screen-space *post-process*
filters — cheapest, but blur and (for TAA) use prior frames. The sampling-theory reason
they exist is in `05-TEXTURING-AND-SAMPLING.md`.
