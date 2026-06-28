---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-graphics:ray-tracing
kind: guide
module: computer-graphics
section: computer-graphics
title: Ray Tracing
status: source-custody
source_custody: partial
current_path: computer-graphics/03-RAY-TRACING.md
canonical_path: computer-graphics/03-RAY-TRACING.md
backsource_ids: [proof-backfill:computer-graphics:03-ray-tracing, git-history:computer-graphics:03-ray-tracing]
concepts: [ray-surface intersection, whitted ray tracing, path tracing, BVH, kd-tree, monte carlo]
root_concepts: [ray tracing]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Ray Tracing

## The Big Picture: Follow the Light Backwards

Ray tracing is the image-order strategy: for each pixel, shoot a ray from the eye into the
scene, find the nearest surface it hits, and ask what light leaves that surface toward the
eye. Reflections, refractions, and shadows fall out by *recursively shooting more rays*.

```
+--------------------------------------------------------------------------------------+
|                         THE RAY TRACING LOOP (per pixel)                             |
|                                                                                      |
|  CAMERA          TRAVERSE         INTERSECT        SHADE           RECURSE           |
|  RAY GEN         ACCEL STRUCT     PRIMITIVE        HIT POINT       (spawn rays)      |
|                                                                                      |
|  eye -> pixel -> descend BVH  -> ray vs triangle -> evaluate   -> shadow rays  -> +  |
|  build ray      skip empty/      (Moller-          BRDF + lights    reflection       |
|  (o, d)         far boxes         Trumbore)         at hit point     refraction      |
|                                                                      bounce ray      |
|                                                                                      |
|   [ray gen]     [BVH/kd  L3]      [intersect L2]    [shade L1+04]   [recurse L4]     |
+--------------------------------------------------------------------------------------+
```

The naming convention is "backward" ray tracing — rays travel *from* the eye *into* the
scene, the reverse of physical photons, because we only care about the light that actually
reaches the camera. The whole field is built on one geometric primitive (ray-surface
intersection) and one organizing principle (recursion).

---

## Layer 1: The Ray and Why We Go Backward

A ray is a parametric half-line.

```
   r(t) = o + t·d ,    t >= 0

      o : origin (the eye, or a surface point for secondary rays)
      d : direction (often normalized)
      t : distance along the ray; the smallest positive t that hits = nearest surface

         o •------------>------------> d
                   t increases
```

```
  FORWARD (physical)                    BACKWARD (what we compute)
  -----------------                     ---------------------------
  light source emits photons            eye casts rays into scene
  -> bounce around scene                -> find what each pixel sees
  -> a few land in the camera           -> follow only paths that matter
  WASTEFUL: most photons miss the eye   EFFICIENT: every ray is for a pixel

  By Helmholtz reciprocity, the light transport is symmetric, so tracing
  backward from the eye gives the same answer as forward from the light.
```

We trace backward because forward tracing wastes essentially all rays — the camera
aperture is tiny. Reciprocity guarantees the answer is identical.

---

## Layer 2: Ray-Surface Intersection

The inner kernel. Two canonical cases.

### Ray-Sphere (the textbook case)

```
  Sphere: |x - c|^2 = R^2.  Substitute x = o + t·d:

     |o + t·d - c|^2 = R^2
     (d·d) t^2 + 2 d·(o-c) t + (|o-c|^2 - R^2) = 0     <-- quadratic in t

  Discriminant D = b^2 - 4ac:
     D < 0   miss
     D = 0   tangent (grazing)
     D > 0   two hits; take the smaller positive t (front surface)
```

### Ray-Triangle (Möller–Trumbore, the one that matters)

Triangles dominate real scenes. Möller–Trumbore (1997) intersects a ray with a triangle
*and* returns barycentric coordinates in one pass, without precomputing the plane:

```
  Triangle V0,V1,V2.  Edges E1 = V1-V0,  E2 = V2-V0.

     P = d × E2          h
     det = E1 · P        (if |det| ~ 0, ray parallel to triangle -> miss)
     T = o - V0
     u = (T · P) / det           barycentric u; reject if u<0 or u>1
     Q = T × E1
     v = (d · Q) / det           barycentric v; reject if v<0 or u+v>1
     t = (E2 · Q) / det          hit distance; reject if t<=0

  Survives all tests -> ray hits triangle at distance t,
  barycentrics (1-u-v, u, v) for interpolating attributes.
```

The same barycentrics that the rasterizer derives from edge functions (`02`) emerge here
from the intersection algebra — the geometry is identical, only the loop order differs.

---

## Layer 3: Acceleration Structures — The Whole Game

Testing every ray against every triangle is `O(pixels × triangles)` — hopeless for
millions of each. The fix is a **spatial hierarchy** so a ray skips the vast majority of
primitives. This is the single most important idea in making ray tracing practical.

```
  BVH (Bounding Volume Hierarchy)        kd-TREE (spatial partition)
  -------------------------------        ---------------------------
  group OBJECTS into nested boxes        split SPACE by axis-aligned planes
  (AABBs); boxes may overlap             cells don't overlap; primitives may
                                         straddle planes (referenced twice)

       [root AABB]                              | split x
        /       \                          [left] | [right]
   [box A]     [box B]                       /         \
    / \         / \                      split y     split y
  tri tri    tri tri                      ...           ...

  ray descends, testing cheap box        ray walks cells front-to-back,
  hits; recurses only into boxes it      stops at first real hit
  pierces -> O(log n) expected

  BVH dominates today (easy to build/refit for animation, GPU-friendly).
  Both turn O(n) intersection into O(log n).
```

```
  WITHOUT acceleration:   ray tests ALL n triangles        -> O(n)
  WITH a BVH:             ray descends a tree of boxes      -> O(log n) expected

  This is the difference between minutes-per-frame and frames-per-second.
```

**Old world → new world.** A BVH is a spatial index — the same idea as a B-tree or
R-tree over geometry instead of keys. A ray query is a range/nearest search that prunes
whole subtrees by a cheap bounding-box rejection, exactly as a database index prunes by
key range before touching rows. Building a good BVH (SAH — the Surface Area Heuristic —
chooses splits that minimize expected traversal cost) is the spatial analogue of choosing
good index split points.

---

## Layer 4: Recursive Tracing — Whitted to Path Tracing

### Reflection and Refraction Directions

The secondary rays Whitted spawns need exact directions. Reflection is a mirror about the
normal; refraction bends by **Snell's law**.

```
  REFLECTION (perfect mirror):
     r = d - 2(d·n) n          (d incoming, n unit normal, r reflected)

  REFRACTION (Snell: n1 sin θi = n2 sin θt):
     let η = n1/n2,  c = -(d·n)
     k = 1 - η²(1 - c²)
     if k < 0:  TOTAL INTERNAL REFLECTION (no transmitted ray — e.g. underwater past
                the critical angle; the surface acts as a mirror)
     else:      t = η d + (η c - √k) n        (refracted direction)

           incoming d \   | n                glass (n2 > n1) bends the ray
                       \  |                   TOWARD the normal; exiting bends away.
            ────────────\─|──────── surface   Critical angle θc = asin(n2/n1) when n1>n2.
                          \|
                           \  refracted t (bent toward normal in denser medium)
```

The **Fresnel** factor decides how much light reflects vs refracts at the interface, rising
to 100% at grazing angles — the reason a calm lake is transparent looking down but mirror-like
looking across it. Whitted weighted the two rays by fixed coefficients; physically correct
renderers use the Fresnel equations (or Schlick's approximation, `04`). Refraction indices:
vacuum 1.0, water 1.33, glass ~1.5, diamond 2.42 (its high index and small critical angle
cause the total-internal-reflection sparkle).

### Whitted Ray Tracing (1980) — Deterministic Recursion

Turner Whitted's insight: at a hit point, spawn a few *specific* secondary rays.

```
  trace(ray):
      hit = nearest_intersection(ray, scene)
      if no hit: return background
      color = local_shading(hit)                  # direct light (Phong-ish)
      for each light:
          shadow_ray = hit -> light
          if occluded(shadow_ray): skip this light's contribution   # SHADOWS
      if surface is reflective:
          color += k_r · trace(reflect(ray, normal))                # REFLECTION
      if surface is refractive:
          color += k_t · trace(refract(ray, normal, ior))           # REFRACTION
      return color

  Recursion depth is capped (e.g. 5-8 bounces) to terminate.
```

Whitted tracing gives crisp shadows, mirror reflections, and glass — effects that
rasterization can only *fake*. But it handles only perfect mirrors/glass and point lights;
it cannot do soft shadows, glossy reflection, or indirect diffuse bounce.

### Path Tracing (Kajiya 1986) — Monte Carlo Integration

To solve the full **rendering equation** (`04`), replace deterministic rays with *random*
sampling of the hemisphere of incoming directions, averaging many paths per pixel.

```
  THE INTEGRAL we must estimate (per hit point):
     Lo = Le + INTEGRAL_hemisphere  f_r · Li · cos(theta) dwi

  PATH TRACING estimates it by Monte Carlo:
     - at each bounce, sample ONE outgoing direction (importance-sampled by the BRDF)
     - follow that path; accumulate radiance; terminate via Russian roulette
     - average N independent paths per pixel

         pixel
           |  many random paths per pixel
       ----+----   each bounces stochastically through the scene
        \  |  /    until it hits a light or is killed
         \ | /
       [scene of bouncing light]

  Error falls as 1/sqrt(N)  ->  NOISE. Halving noise needs 4x the samples.
```

Path tracing is *unbiased*: average enough paths and it converges to the true solution,
including soft shadows, color bleeding, caustics, and global illumination — all from one
algorithm. The cost is **variance** (noise), which is why production renderers pair it with
importance sampling, multiple importance sampling (MIS), and — recently — neural denoisers.

| | Whitted (1980) | Path tracing (1986) |
|---|---|---|
| Secondary rays | Deterministic (mirror, refract, shadow) | Random hemisphere samples |
| Solves | A subset of effects | Full rendering equation |
| Soft shadows / GI | No | Yes |
| Error type | Bias (missing effects) | Variance (noise), unbiased |
| Convergence | One pass | `1/√N` — many samples |
| Use | Early ray tracers | Modern film & offline rendering |

---

## Layer 5: Hardware Ray Tracing and the Hybrid Present

Since 2018, GPUs (NVIDIA RTX, then AMD/Intel) include fixed-function **RT cores** that
accelerate BVH traversal and triangle intersection. APIs (DXR, Vulkan RT) expose a
*two-level* acceleration structure and a shader-table model.

```
  TWO-LEVEL ACCELERATION STRUCTURE (TLAS over BLAS):

     TLAS  (instances: transforms + references)
       |---- instance A --> BLAS_mesh1   (the actual triangle BVH)
       |---- instance B --> BLAS_mesh1   (reused, different transform)
       |---- instance C --> BLAS_mesh2

  BLAS = geometry, built once. TLAS = scene, refit/rebuilt per frame for animation.

  Shader stages: ray-gen -> traversal (HW) -> closest-hit / any-hit / miss shaders
```

Real-time renderers don't path-trace the whole frame. They **rasterize** primary
visibility (cheap, `02`) and ray trace *selected* effects — shadows, reflections, ambient
occlusion, GI — at one or a few samples per pixel, then *denoise* aggressively. This hybrid
is the current state of the art: rasterize what's cheap, trace what rasterization fakes
badly.

---

## Worked Example: Ray-Sphere Hit

Camera at `o=(0,0,0)`, ray direction `d=(0,0,-1)` (down −z, normalized). Sphere center
`c=(0,0,-5)`, radius `R=1`.

```
  oc = o - c = (0,0,5)
  a = d·d = 1
  b = 2(d·oc) = 2·(0·0 + 0·0 + (-1)·5) = -10
  c_term = oc·oc - R^2 = 25 - 1 = 24

  Discriminant D = b^2 - 4ac = 100 - 96 = 4  > 0  -> two hits
  t = (-b ± √D) / 2a = (10 ± 2)/2 = {4, 6}

  Nearest positive t = 4  ->  hit point = o + 4d = (0,0,-4)  (front of sphere)
  Normal at hit = (hit - c)/R = (0,0,1)  (points back toward camera)  ✓
```

The far root `t=6` is the back surface, correctly ignored. A shadow ray would now fire from
`(0,0,-4)` toward each light; a reflection ray would fire about the normal `(0,0,1)`.

---

## Old World → New World Bridges

| You already know | Here it is |
|------------------|-----------|
| B-tree / R-tree spatial index | BVH / kd-tree — prune subtrees by bounding box |
| Query planner choosing a good index | SAH (Surface Area Heuristic) choosing BVH splits |
| Recursion with a depth bound | Whitted tracing — bounce rays, capped depth |
| Monte Carlo integration / quadrature | Path tracing the hemisphere integral |
| Variance reduction in MC simulation | Importance sampling, MIS in path tracing |
| Two-level page table / handle table | TLAS over BLAS (instances over geometry) |
| Caching a denoised expensive estimate | Real-time RT: few samples + neural denoiser |

---

## Decision Cheat Sheet

| Situation | Choice |
|---|---|
| Photoreal film, offline, GI/caustics | Path tracing |
| Crisp mirror/glass, point lights (classic) | Whitted recursion |
| Real-time with some ray-traced effects | Hybrid: rasterize primary + RT shadows/reflections + denoise |
| Triangle intersection kernel | Möller–Trumbore (also yields barycentrics) |
| Speeding up "ray vs many triangles" | BVH (default today) or kd-tree |
| Animated scene acceleration | Refit/rebuild a BVH; TLAS per frame, BLAS reused |
| Killing path-tracer noise | More samples, importance sampling, MIS, denoiser |
| Terminating recursion fairly | Russian roulette (unbiased) |

---

## Common Confusion Points

### "Why trace rays *from* the eye, not from the light?"

Because the camera aperture is minuscule — forward-traced photons almost never reach it,
wasting nearly all work. Helmholtz reciprocity makes backward tracing give the identical
result far more efficiently. (Bidirectional and photon-mapping methods trace *both* ways to
capture effects like caustics that pure backward tracing samples poorly.)

### "Is ray tracing automatically more realistic than rasterization?"

Ray tracing makes *global* effects (shadows, reflections, GI) natural rather than faked —
but a single-bounce Whitted trace can look *less* realistic than a well-tuned rasterizer
with good shadow maps and probes. Realism comes from solving the rendering equation well
(`04`), which is path tracing's domain, not from ray casting per se.

### "Why is path tracing noisy and rasterization isn't?"

Path tracing estimates an integral by random sampling; finite samples leave variance, seen
as grain. Convergence is `1/√N` — brutally slow, hence denoisers. Rasterization computes a
deterministic (if approximate) result with no Monte Carlo step, so no noise — but also no
true global illumination without bolt-on tricks.

### "BVH vs kd-tree — which should I care about?"

BVH dominates modern (especially GPU/RTX) rendering: easy to build, cheap to *refit* for
animation, bounded memory, hardware-accelerated. kd-trees can give slightly faster
traversal for fully static scenes but are costlier to build and rebuild. Default to BVH.

### "Does hardware ray tracing replace rasterization?"

No — it augments it. Current GPUs rasterize the primary visibility pass and ray trace
selected effects, because full-frame path tracing at real-time rates is still out of reach
without heavy denoising. The pipeline is hybrid by design; the RT cores accelerate the
intersection/traversal kernels described in Layers 2–3.
