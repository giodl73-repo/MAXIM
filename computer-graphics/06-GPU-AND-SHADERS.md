---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-graphics:gpu-and-shaders
kind: guide
module: computer-graphics
section: computer-graphics
title: GPU and Shaders
status: source-custody
source_custody: partial
current_path: computer-graphics/06-GPU-AND-SHADERS.md
canonical_path: computer-graphics/06-GPU-AND-SHADERS.md
backsource_ids: [proof-backfill:computer-graphics:06-gpu, git-history:computer-graphics:06-gpu]
concepts: [programmable pipeline, vertex shader, fragment shader, compute shader, SIMT, warp, GPU memory hierarchy]
root_concepts: [GPU, shaders]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# GPU and Shaders

## The Big Picture: A Throughput Machine Running Tiny Programs in Lockstep

A GPU renders by running small programs — **shaders** — across millions of vertices and
pixels simultaneously. Understanding graphics performance means understanding the GPU's
execution model (SIMT) and its memory hierarchy, both of which differ sharply from a CPU.

```
+--------------------------------------------------------------------------------------+
|                        THE PROGRAMMABLE GPU PIPELINE                                 |
|                                                                                      |
|  INPUT          VERTEX        [TESS]      [GEOM]      RASTER       FRAGMENT     OUT  |
|  ASSEMBLY       SHADER         opt.        opt.       (fixed)      SHADER      MERGE |
|                                                                                      |
|  vertices  --> per-vertex --> subdivide-> per-prim-> triangle--> per-pixel --> blend |
|  + indices      transform      patches     emit       coverage     shade      z-test |
|                 (PROG)        (PROG)      (PROG)      (FIXED)     (PROG)     (FIXED) |
|                                                                                      |
|  --------------------------- alongside ------------------------------------------    |
|  COMPUTE SHADER: general-purpose data-parallel kernels (no fixed pipeline)           |
|  -> physics, culling, post-processing, simulation, ML, hybrid RT (03)                |
+--------------------------------------------------------------------------------------+
```

Boxes marked **PROG** are programmable (you write the shader); **FIXED** are
fixed-function hardware (rasterizer, depth/blend). The pipeline evolved from entirely
fixed-function (1990s) to fully programmable; **compute shaders** then escaped the graphics
pipeline entirely, turning the GPU into a general data-parallel processor.

---

## Layer 1: The Programmable Stages

Each programmable stage is a kernel run independently across its data elements.

```
  VERTEX SHADER       runs once PER VERTEX
                      job: object-space vertex -> clip-space (apply MVP, 01)
                      outputs: clip position + interpolants (UV, normal, ...)

  TESSELLATION        runs on patches; subdivides into more triangles on the GPU
  (hull + domain)     -> displacement, adaptive detail, smooth surfaces (07)

  GEOMETRY SHADER     runs per primitive; can emit/discard primitives
                      -> rarely used now (slow); compute/mesh shaders replaced it

  RASTERIZER (fixed)  clip-space triangles -> covered fragments + interpolated attrs (02)

  FRAGMENT SHADER     runs once PER FRAGMENT (candidate pixel)
                      job: compute the output color (sample textures, evaluate BRDF, 04/05)
                      this is where the per-pixel cost lives -> the usual bottleneck

  OUTPUT MERGER (fixed) depth test, stencil, blend -> framebuffer (02)
```

```
  MESH SHADERS (2018+, modern alternative front-end):

    classic:  index buffer -> input assembly -> vertex shader -> ...
    mesh:     [TASK shader] -> [MESH shader emits "meshlets"] -> rasterizer

  Replaces the fixed vertex-fetch + geometry stages with two flexible compute-like
  stages -> better culling and scaling for huge geometry.
```

**Old world → new world.** A fragment shader is a **map** over a giant dataset: the same
kernel applied to every pixel, embarrassingly parallel, no cross-element dependencies — the
GPU equivalent of a data-parallel `map`/`SELECT`-projection over millions of rows. A
compute shader is the more general form, with explicit thread groups and shared memory —
closer to a hand-tuned parallel kernel than to a query.

---

## Layer 2: SIMT — The Execution Model

A GPU is not "thousands of independent cores." Threads are bundled into **warps** (NVIDIA,
32 threads) or **wavefronts** (AMD, 32/64) that execute **one instruction across all lanes
in lockstep**. This is **SIMT** — Single Instruction, Multiple Threads.

```
  SIMT WARP (32 lanes, one program counter):

     instruction:  r2 = r0 * r1
     lane:   0    1    2    3   ...  31
     data:  d0   d1   d2   d3   ... d31     <- all multiplied SAME cycle

  One PC, 32 data items. Like SIMD, but each lane has its own registers and can
  be masked off -- so it PROGRAMS like scalar threads, EXECUTES like a vector.
```

### Branch Divergence — the SIMT tax

Because the whole warp shares one program counter, an `if` where lanes disagree must run
**both sides**, masking the inactive lanes each time. Divergence *serializes* the branches.

```
  if (cond) { A } else { B }   with cond differing within a warp:

    step 1: run A with lanes where cond==true  active, others MASKED (idle)
    step 2: run B with lanes where cond==false active, others MASKED (idle)
    -> warp pays for BOTH A and B. Worst case: 32x slowdown for fully divergent code.

  Coherent branch (all lanes agree) -> only the taken side runs -> free.
```

This is *the* GPU performance rule that surprises CPU programmers: data-dependent branching
inside a warp is expensive. Sort/bucket work so a warp's lanes take the same path; prefer
arithmetic (`select`/`mix`) over branches for short divergent sections.

### Latency Hiding by Oversubscription

A GPU has tiny caches relative to its arithmetic. It hides memory latency not by caching but
by keeping *many* warps resident and switching to a ready one whenever the current warp
stalls on a memory fetch.

```
  warp A issues a memory load (hundreds of cycles latency)
     -> scheduler instantly runs warp B, then C, then D ...
     -> by the time A's data arrives, A is rescheduled
  "Occupancy" = how many warps are resident. High occupancy -> latency fully hidden.
  Limited by registers/shared-memory per thread (more usage -> fewer resident warps).
```

| | CPU (latency-optimized) | GPU (throughput-optimized) |
|---|---|---|
| Cores | Few fat cores | Thousands of thin lanes |
| Model | MIMD (independent) | SIMT (warps in lockstep) |
| Branching | Cheap (predictors) | Divergence serializes a warp |
| Latency hiding | Big caches, OOO, prefetch | Massive warp oversubscription |
| Wins at | Control flow, serial work | Data-parallel arithmetic |
| Hurts at | Throughput per watt | Divergent/irregular control flow |

**Old world → new world.** SIMT is SIMD with per-lane masking and per-lane registers — wider
than CPU vector units and with hardware-managed divergence. Latency hiding by warp-switching
is hardware **hyperthreading taken to the extreme** (dozens of "threads" per scheduler rather
than two), trading cache for concurrency.

---

## Layer 3: The GPU Memory Hierarchy

Memory bandwidth and access pattern dominate GPU performance more than raw FLOPs.

```
  REGISTERS         per-thread, fastest, scarce (more regs/thread -> lower occupancy)
     |
  SHARED MEMORY     per thread-GROUP scratchpad, software-managed, ~L1 speed
  / L1              (key tool: stage data here for reuse across a group)
     |
  L2 CACHE          shared across the whole GPU
     |
  VRAM (GDDR/HBM)   huge, high BANDWIDTH but high LATENCY (hundreds of cycles)

  MEMORY COALESCING: when the 32 lanes of a warp read CONSECUTIVE addresses, the
  hardware merges them into a few wide transactions.
     coalesced:    lane i reads addr base + i      -> 1-2 transactions  (fast)
     scattered:    lane i reads random addr        -> up to 32 transactions (slow)
```

Coalescing is the memory analogue of branch coherence: keep the warp's *accesses* together,
just as you keep its *control flow* together. Texture units add a hardware path with built-in
filtering (`05`) and 2D-locality caching. **Shared memory** is the programmer's explicit lever
— stage a tile of data once, let the whole thread group reuse it, avoid re-reading VRAM. This
is exactly the blocking/tiling you'd do for cache on a CPU, but *manual* and *per-group*.

**Bridge to `computer-architecture/`.** The GPU is the extreme corner of the
latency-vs-throughput design space: trade caches, out-of-order execution, and branch
prediction (CPU's latency tools) for raw parallel ALUs and bandwidth, then hide latency with
concurrency. Same physics (memory wall, power), opposite optimization target.

---

### Derivatives and the Pixel Quad

A subtle but important detail: fragment shaders run in **2×2 pixel quads**, always, even at
triangle edges. This is what makes screen-space derivatives — and therefore automatic mip
selection — possible.

```
  GPUs shade pixels in 2x2 QUADS. Within a quad the hardware can take finite differences:

     ddx(v) = v(right pixel)  - v(this pixel)      (rate of change in screen x)
     ddy(v) = v(below pixel)  - v(this pixel)      (rate of change in screen y)

  -> the texture unit uses ddx/ddy of the UV to pick the mip LOD (05) for free.

  COST: a triangle covering 1 pixel still shades a full quad -> the other 3 lanes are
  "helper" pixels (computed for derivatives, then discarded). Thin slivers and dense
  micro-triangles waste up to 75% of shading on helpers — a key reason sub-pixel
  geometry is expensive and why LOD (07) and Nanite's pixel-sized clusters matter.
```

This quad execution is why the GPU can compute `ddx`/`ddy` of *any* shader value, not just
UVs — and why over-tessellated geometry (many triangles smaller than a quad) tanks
performance: every micro-triangle pays for 4 lanes to shade 1 useful pixel. The derivative
mechanism links straight back to mip selection (`05`) and the LOD argument (`07`).

## Layer 4: Compute Shaders — Off the Graphics Rails

A **compute shader** runs an arbitrary data-parallel kernel with no fixed pipeline — no
vertices, no rasterizer. You dispatch a grid of thread groups; each group has shared memory
and synchronization.

```
  DISPATCH a 3D grid of THREAD GROUPS; each group is a 3D block of threads:

     dispatch(groupsX, groupsY, groupsZ)
        each group: e.g. 8x8 threads, sharing scratchpad memory + a barrier()

  Used for:
     - post-processing (bloom, tone map, TAA resolve)   [08, 09]
     - GPU culling, particle systems, physics
     - building/refitting acceleration structures        [03]
     - GPGPU: linear algebra, FFTs, and ML inference/training

  This is the door through which GPUs became the substrate for deep learning
  (CUDA 2007) -- the same SIMT hardware, addressed as a general compute device.
```

The lineage runs straight from "shade a pixel" to "train a transformer": both are the same
SIMT arithmetic over huge arrays. Graphics shading languages (HLSL/GLSL/MSL) and GPGPU
languages (CUDA, compute shaders) compile to the same warp-executing hardware.

---

### Specialized Units: Texture, RT, and Tensor Cores

A modern GPU is not only general ALUs; it has fixed-function blocks the shader cores call out
to, each accelerating an operation that would be slow in software.

```
  TEXTURE UNITS   address calc + filtering (bilinear/trilinear/aniso) + 2D-locality
                  cache + format decode (BCn) — all in hardware (05). A texture fetch
                  is a single instruction that hides a lot of work.

  RT CORES        BVH traversal + ray-triangle/box intersection (03). The shader issues
                  a TraceRay; the RT core does the tree walk and hands back the hit.

  TENSOR CORES    small dense matrix-multiply-accumulate (e.g. 4x4) at very high rate.
                  Built for deep learning; in graphics they power DLSS and ML denoisers (09).
```

The trajectory is telling: the GPU keeps absorbing whatever operation is hot — filtering
(1990s), then general compute (2007), then ray intersection and matrix-multiply (2018). The
shader cores orchestrate; the fixed units do the heavy, regular work. This is why "the GPU"
is now equally the engine of rendering, ray tracing, *and* neural networks.

## Layer 5: Shading Languages and APIs

```
  SHADING LANGUAGES (what you write a shader in)
     HLSL   Direct3D (also DXR ray tracing); Microsoft
     GLSL   OpenGL / Vulkan (Vulkan via SPIR-V bytecode)
     MSL    Metal (Apple)
     WGSL   WebGPU (the browser's modern GPU language)
     -> all compile to a hardware-specific ISA (e.g. SPIR-V -> vendor microcode)

  GRAPHICS APIs (how the CPU drives the GPU)
     OLD (implicit):  OpenGL, Direct3D 11   -- driver manages state/sync for you
     NEW (explicit):  Vulkan, Direct3D 12, Metal, WebGPU
                      -- you manage command buffers, memory, synchronization,
                         pipeline state objects -> less driver overhead, more control
```

The shift from OpenGL/D3D11 to Vulkan/D3D12 mirrors a familiar trade: the old APIs are a
managed runtime (the driver hides synchronization and memory, like a GC); the new ones are
explicit and lower-level (you own memory and sync, like manual allocation) — more code, far
less per-draw CPU overhead, predictable multi-threaded submission. More in `09`.

---

## Worked Example: Why a Divergent Loop Tanks

A fragment shader computes a per-pixel iteration count (e.g. a Mandelbrot-style loop) that
varies by pixel:

```
  for (i = 0; i < iterations[pixel]; i++) { ... }    // iterations differs per lane

  A warp covers 32 neighboring pixels. Suppose in one warp:
     31 lanes finish at i = 10
      1 lane  needs  i = 200

  SIMT runs the loop until the LAST lane is done -> all 32 lanes step to i=200,
  with 31 lanes masked off (idle) for iterations 11..200.

  Useful work:    sum of per-lane iterations ~ 31*10 + 200 = 510 lane-iterations
  Work performed: 32 lanes * 200 steps      = 6400 lane-iterations
  Efficiency:     510 / 6400 ~ 8%      <- the warp ran at ~8% of peak.

  Fix: bin pixels by expected iteration count so each warp's lanes finish together,
       or cap/early-out coherently. Coherence, not raw FLOPs, set the speed.
```

This is the canonical GPU lesson: the bottleneck was **divergence**, not arithmetic. A CPU
would simply run each pixel's loop to its own length; the GPU pays for the worst lane in
each warp.

---

## Old World → New World Bridges

| You already know | Here it is |
|------------------|-----------|
| `map` over a large dataset | A fragment/compute shader kernel over pixels/elements |
| SIMD vector intrinsics | SIMT warps — wider, per-lane masking & registers |
| Hyperthreading (2 threads/core) | Warp oversubscription (dozens/scheduler) for latency hiding |
| Cache blocking / tiling | Shared-memory staging within a thread group |
| Coalesced vs random memory access | Memory coalescing across a warp's 32 lanes |
| Branch misprediction cost | Branch divergence cost (worse — serializes the warp) |
| Managed runtime vs manual memory | OpenGL/D3D11 vs Vulkan/D3D12 explicit APIs |
| Bytecode + JIT (CIL, JVM) | SPIR-V shader bytecode compiled to vendor ISA |

---

## Decision Cheat Sheet

| Situation | Choice |
|---|---|
| Transform geometry to clip space | Vertex shader |
| Per-pixel color / lighting | Fragment shader (usual bottleneck) |
| GPU subdivision / displacement | Tessellation (or mesh shaders) |
| General data-parallel work (post, physics, ML) | Compute shader |
| Avoid stalls | Maximize occupancy; coalesce memory; minimize divergence |
| Branch where lanes disagree a lot | Bucket/sort work, or use `select`/`mix` over `if` |
| Low CPU overhead, multi-thread submission | Explicit API (Vulkan / D3D12 / Metal) |
| Quick portable rendering, less control | Managed API (OpenGL / D3D11 / WebGPU-ish) |
| Reuse data across a thread group | Shared memory (manual tiling) |

---

## Common Confusion Points

### "A GPU has thousands of cores — so thousands of independent programs?"

No. Lanes are grouped into warps that share one program counter and execute in lockstep
(SIMT). It *programs* like many scalar threads but *executes* like a vector unit with
masking. Independent control flow within a warp is the expensive case — the model is closer
to "wide SIMD with per-lane masks" than to "many CPUs."

### "Why is my shader slow when it's not doing much math?"

Almost always memory or divergence, not arithmetic. Check: are warp accesses coalesced? Is
occupancy high enough to hide VRAM latency (or are registers/shared-memory per thread too
high)? Are lanes diverging on data-dependent branches? GPUs are bandwidth- and
coherence-bound far more often than FLOP-bound.

### "Geometry shader vs compute vs mesh shader — which front-end?"

Geometry shaders are largely deprecated (slow, serialization-prone). For GPU-driven geometry
today, use **compute** (culling, building draw lists) or **mesh shaders** (the modern
flexible front-end that replaces vertex-fetch + geometry). Reach for the geometry shader only
for legacy compatibility.

### "OpenGL vs Vulkan — is Vulkan just 'faster OpenGL'?"

Different abstraction levels. OpenGL/D3D11 let the driver manage state, memory, and
synchronization (convenient, but a CPU-side bottleneck and hard to multithread). Vulkan/D3D12
make all of that explicit — far more code, but much lower driver overhead and predictable
multi-threaded command submission. "Faster" only if you do the explicit management well;
otherwise it's just more error-prone.

### "Are graphics shaders and CUDA/ML kernels the same hardware?"

Yes — both compile to the same SIMT warp-executing cores. A fragment shader shading pixels
and a CUDA kernel multiplying matrices use the identical ALUs, schedulers, and memory
hierarchy. The compute-shader/CUDA door (2007) is exactly how GPUs became the substrate for
deep learning; graphics and ML are two workloads on one throughput machine.
