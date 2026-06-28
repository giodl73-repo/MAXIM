---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-graphics:shading-and-lighting
kind: guide
module: computer-graphics
section: computer-graphics
title: Shading and Lighting
status: source-custody
source_custody: partial
current_path: computer-graphics/04-SHADING-AND-LIGHTING.md
canonical_path: computer-graphics/04-SHADING-AND-LIGHTING.md
backsource_ids: [proof-backfill:computer-graphics:04-shading, git-history:computer-graphics:04-shading]
concepts: [rendering equation, BRDF, energy conservation, phong, physically based rendering, global illumination]
root_concepts: [shading, lighting]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Shading and Lighting

## The Big Picture: One Equation, Many Approximations

Shading answers: *given a surface point, its material, and the lights, how much light
leaves toward the eye?* Every model in this guide is an approximation to a single integral
equation — the rendering equation. The history of shading is the history of approximating
it ever more faithfully.

```
+--------------------------------------------------------------------------------------+
|                THE RENDERING EQUATION AND ITS APPROXIMATIONS                         |
|                                                                                      |
|   Lo(x,wo) = Le(x,wo) + INTEGRAL_hemisphere f_r(x,wi,wo)·Li(x,wi)·(n·wi) dwi         |
|   (Kajiya 1986 -- the ground truth every renderer approximates)                      |
|                                                                                      |
|   crude <------------------- fidelity -------------------> physically correct        |
|                                                                                      |
|  +----------+   +-----------+   +-----------+   +-----------+   +-----------------+  |
|  | Lambert  |-> | Phong /   |-> | PBR BRDF  |-> | direct +  |-> | full GI: path   |  |
|  | (diffuse)|   | Blinn     |   | (Cook-    |   | image-    |   | tracing solves  |  |
|  |          |   | (1973-77) |   | Torrance) |   | based lit |   | the integral    |  |
|  +----------+   +-----------+   +-----------+   +-----------+   +-----------------+  |

|   [L1]           [L2]            [L3 BRDF]       [L4 IBL]        [L5 GI / 03]        |
+--------------------------------------------------------------------------------------+
```

Read left to right: increasing physical fidelity. Lambert and Phong are *guesses* tuned to
look plausible; PBR uses a real BRDF that conserves energy; global illumination actually
attempts the recursive integral. The equation itself is the spec.

---

## Layer 1: The Rendering Equation, Term by Term

```
   Lo(x, wo)  =  Le(x, wo)  +  INTEGRAL over hemisphere Ω of:
                                 f_r(x, wi, wo) · Li(x, wi) · (n · wi) dwi

   ┌──────────┬──────────────────────────────────────────────────────────┐
   │ Lo(x,wo) │ RADIANCE leaving point x toward viewing direction wo     │
   │ Le(x,wo) │ radiance the surface EMITS itself (0 unless it's a light)│
   │ f_r(...) │ the BRDF: fraction of light from wi redirected toward wo │
   │ Li(x,wi) │ radiance ARRIVING at x from incoming direction wi        │
   │ (n · wi) │ Lambert cosine: grazing light spreads over more area     │
   │ ∫ dwi    │ sum over EVERY incoming direction on the hemisphere      │
   └──────────┴──────────────────────────────────────────────────────────┘
```

The equation is **recursive**: `Li(x, wi)` is itself the `Lo` of *whatever surface lies in
direction `wi`*. That recursion is exactly what makes global illumination hard — to shade
one point you must, in principle, shade the whole scene. The cosine term `(n · wi)` is the
geometric fact that a beam striking at a grazing angle is spread thinly (this is also why
seasons exist — sunlight at high latitude hits at a shallow angle).

**Old world → new world.** The rendering equation is a **Fredholm integral equation of the
second kind** — the unknown `L` appears both outside and inside the integral. Solving it is
formally like solving a large linear system where the operator is "light transport." Path
tracing is just a Monte Carlo estimator of its Neumann-series solution (the sum over 0, 1,
2, … bounces) — the same series expansion you'd use for `(I − T)⁻¹`.

---

## Layer 2: Phong and Blinn-Phong — The Plausible Guess

Before physics, there was a tuned formula. Phong (1973) splits reflection into three
hand-chosen terms.

```
   PHONG model (per light):

     I = k_a·I_a  +  k_d·(n·l)·I_d  +  k_s·(r·v)^α·I_s
         ───────     ─────────────     ───────────────
         ambient      diffuse           specular
         (fake fill)  (Lambert)         (shiny highlight)

       l = direction to light    n = surface normal
       v = direction to viewer   r = reflection of l about n
       α = "shininess" exponent (bigger = tighter highlight)

   BLINN-PHONG (1977) replaces (r·v) with (n·h),
       h = normalize(l + v)   (the HALFWAY vector)
   -- cheaper, and a better match to measured highlights at grazing angles.
```

Phong is not physical: ambient is a flat fudge for missing global light, the specular
exponent has no physical meaning, and **nothing conserves energy** — crank `k_d`, `k_s`,
and `k_a` and a surface can emit more light than hits it. It looked good enough to rule
real-time graphics for 30 years, but its parameters don't transfer between lighting
conditions, which is exactly what PBR fixes.

### Where the Lambert Cosine Comes From

The `(n·l)` diffuse term is not arbitrary — it is **radiometry**. A beam of fixed
cross-sectional power striking a surface at angle `θ` from the normal spreads over an area
`1/cos θ` larger, so the *irradiance* (power per unit area) on the surface scales by
`cos θ = n·l`.

```
   light beam (fixed width)        same beam, grazing angle
        | | | |                       \ \ \ \
        | | | |                        \ \ \ \
   ─────┴─┴─┴─┴──── surface       ──────\─\─\─\──────── surface
        ↑ lands on width w               ↑ smeared over width w/cos θ
        full irradiance                  irradiance × cos θ  (diluted)
```

A **Lambertian** (ideal diffuse) surface scatters that received light equally in all
directions, so its outgoing radiance is `(ρ/π)·(n·l)·I` — the `cos` is geometry, the `1/π`
normalizes the BRDF so a white Lambertian surface (`ρ=1`) conserves energy exactly. This is
why every shading model, Phong included, carries the `n·l` factor: it is the cosine of the
rendering equation, not a fudge.

### Shading frequency: flat / Gouraud / Phong

```
  FLAT      one normal per triangle    -> faceted look, cheapest
  GOURAUD   shade at vertices,         -> smooth but misses highlights inside a triangle
            interpolate the COLOR
  PHONG     interpolate the NORMAL,    -> shade per pixel; correct highlights, costlier
            shade per PIXEL (fragment)
```

Note the naming overload: "Phong" is both a *reflection model* and a *shading frequency*
(per-pixel normal interpolation). Modern fragment shaders do Phong-frequency shading with
PBR reflection models.

---

## Layer 3: Physically Based Rendering (PBR) and BRDFs

A **BRDF** (Bidirectional Reflectance Distribution Function) `f_r(x, wi, wo)` is the
material's full answer: for light arriving from `wi`, what fraction leaves toward `wo`? A
*physically valid* BRDF obeys two hard constraints.

```
  THE TWO LAWS A REAL BRDF MUST OBEY:

  1. ENERGY CONSERVATION
     For any incoming direction, the total reflected over the hemisphere <= incoming.
        INTEGRAL_hemisphere f_r(wi,wo)·(n·wo) dwo  <=  1     (the rest is absorbed)
     A surface cannot reflect more light than it receives.

  2. HELMHOLTZ RECIPROCITY
     f_r(wi, wo) = f_r(wo, wi)     (swapping light and eye gives the same value)
     -- this is what lets us trace rays backward (03).
```

Phong violates #1; PBR is built around it. The modern standard is a **microfacet** model:
the surface is millions of tiny mirrors whose orientation distribution sets the roughness.

```
  COOK-TORRANCE microfacet specular BRDF:

                D(h) · F(wo,h) · G(wi,wo)
     f_spec  = ───────────────────────────
                  4 (n·wi)(n·wo)

     D : NORMAL DISTRIBUTION   how many microfacets point toward h (GGX/Trowbridge-Reitz)
                               -> controlled by ROUGHNESS
     F : FRESNEL               reflectance rises at grazing angles (Schlick approx)
                               -> everything is mirror-like at the edge
     G : GEOMETRY / SHADOWING  microfacets occlude/shadow each other at glancing angles

   Full BRDF = diffuse term + f_spec, weighted so the two never exceed incoming energy.
```

The **metalness/roughness** workflow that artists use maps onto this: *roughness* sets
`D`'s spread; *metalness* decides whether the diffuse term exists (metals have ~no diffuse;
their base color tints the Fresnel `F`) and sets `F0` (the head-on reflectance). Because the
parameters are physical, a PBR material looks correct under *any* lighting — the property
Phong lacked.

The Fresnel term in practice uses **Schlick's approximation** — cheap and accurate:

```
  F(θ) = F0 + (1 - F0)·(1 - cos θ)^5

     F0 = reflectance at normal incidence (head-on):
        dielectrics (plastic, skin, water): ~0.02–0.04  (so diffuse dominates)
        metals: 0.5–1.0, and COLORED (gold F0 ≈ (1.0, 0.78, 0.34))

     as θ -> 90° (grazing), (1 - cos θ)^5 -> 1, so F -> 1.0 for EVERYTHING.

  cos θ:   1.0 (head-on)            0.0 (grazing)
  F:       F0 (0.04 for plastic) -> 1.0 (full mirror at the edge)
```

This grazing-angle rise is the "Fresnel rim" — the bright edge on a backlit sphere, the
mirror sheen of a lake seen across its surface. Blinn-Phong has no such term, which is why
its materials look subtly flat at silhouettes.

| | Phong / Blinn-Phong | PBR (microfacet) |
|---|---|---|
| Basis | Tuned formula | Physics (microfacet + Fresnel) |
| Energy conservation | No | Yes (enforced) |
| Reciprocity | Approximate | Yes |
| Parameters | `k_a,k_d,k_s,α` (unitless fudges) | albedo, roughness, metalness (physical) |
| Transfers across lighting | No | Yes |
| Fresnel (grazing reflectance) | Missing | Built in |
| Era | 1973–~2010 | ~2012– (UE4, Disney "principled") |

---

## Layer 4: Lights and Image-Based Lighting

The `Li` term needs sources. Idealized lights are cheap; real environments are captured.

```
  LIGHT TYPES
  -----------
  POINT        radiates from a position; falls off as 1/d^2 (inverse square)
  DIRECTIONAL  parallel rays, no falloff (the sun) -- one direction for all points
  SPOT         point + angular cone + falloff
  AREA         emits from a surface -> SOFT shadows (penumbra), physically real
  ENVIRONMENT  the whole surrounding hemisphere as a light (IBL)

  IMAGE-BASED LIGHTING (IBL): use an HDR environment map (HDRI) as Li(wi).
     diffuse  -> precompute an irradiance map (cosine-convolved environment)
     specular -> precompute prefiltered mips per roughness + a BRDF LUT
                 ("split-sum" approximation, Karis/UE4 2013)
  This is how PBR materials get believable reflections of their surroundings.
```

The inverse-square falloff for point lights is just radiometry: a fixed power spread over a
sphere of area `4πd²`. Area lights produce **penumbrae** (soft shadow edges) because parts
of the light are occluded while others aren't — a point light, having zero area, gives
unrealistically hard shadows.

---

## Layer 5: Global Illumination — Closing the Recursion

**Direct lighting** evaluates only the light coming straight from sources. **Global
illumination (GI)** adds *indirect* light — bounces off other surfaces — which is the
recursive part of the rendering equation. It produces color bleeding, soft contact
shadows, and realistic ambient.

```
  DIRECT ONLY                          WITH GLOBAL ILLUMINATION
  -----------                          ------------------------
  surfaces lit only by sources         light bounces between surfaces
  shadows are pitch black              shadows filled by bounced light
  no color bleeding                    red wall tints nearby white floor pink

  Methods to approximate the indirect integral:
    PATH TRACING     Monte Carlo over all bounce paths (unbiased, noisy)   [03]
    PHOTON MAPPING   shoot photons from lights, gather at shading points (caustics)
    RADIOSITY        finite-element solve for diffuse interreflection (view-indep)
    PROBES / SH      precomputed light at points, interpolated (real-time)
    VOXEL/SCREEN-SPACE GI, RTXGI, DDGI  -- real-time approximations
```

```
  AMBIENT TERM EVOLUTION (how we faked the indirect integral over time):

   constant k_a   ->  ambient occlusion (AO)  ->  precomputed probes  ->  real-time GI
   (flat fudge)       (darken creases via       (irradiance volumes)     (ray-traced
                       local geometry)                                     indirect)
```

Real-time GI is an active frontier: ray-traced GI (one or few bounces, denoised) is now
shipping in games, finally connecting the real-time pipeline to the rendering equation that
offline path tracers have solved since 1986.

---

## Worked Example: Energy Conservation Check

A naive "diffuse + specular" material with a Lambertian albedo `ρ = 0.9` and an added
specular lobe that reflects another `0.3` of incoming light at the head-on direction.

```
  Lambertian reflects fraction ρ = 0.9 of incoming (integrates to 0.9 over hemisphere).
  Add a specular lobe reflecting 0.3.

  Total reflected = 0.9 + 0.3 = 1.2  >  1.0    ->  VIOLATES energy conservation!
  This surface emits 120% of incoming light -- it would glow brighter each bounce
  and a GI solver would DIVERGE.

  PBR FIX: the specular and diffuse share an energy budget. With Fresnel F0 = 0.04
  (typical dielectric) reflecting ~4% specularly head-on, the diffuse is scaled by
  (1 - F):
      diffuse  <= (1 - 0.04)·ρ = 0.96·0.9 = 0.864
      specular  = 0.04 (head-on), rising toward 1.0 only at grazing angles
      total    <= 1.0   ✓   (and -> 1.0 at the grazing Fresnel edge, never above)
```

This is the concrete reason PBR replaced ad-hoc shading: get the energy budget wrong and
multi-bounce GI either darkens or explodes. Phong's free `k_d + k_s` is exactly the bug.

---

## Old World → New World Bridges

| You already know | Here it is |
|------------------|-----------|
| Fredholm integral equation of the 2nd kind | The rendering equation — unknown inside and outside the integral |
| Neumann series `(I−T)⁻¹ = Σ Tⁿ` | Light transport as a sum over bounce counts |
| Conservation laws as hard constraints | Energy conservation forces valid BRDFs |
| Reciprocity / symmetry of an operator | Helmholtz reciprocity `f_r(wi,wo)=f_r(wo,wi)` |
| Precomputed lookup tables | IBL irradiance maps, prefiltered specular, BRDF LUT |
| Importance sampling in Monte Carlo | Sampling the BRDF lobe in path tracing |
| Inverse-square field (gravity, Coulomb) | Point-light falloff `1/d²` |
| Replacing magic constants with units | Phong's fudges → PBR's physical parameters |

---

## Decision Cheat Sheet

| Situation | Choice |
|---|---|
| Believable materials under any lighting | PBR (microfacet, metalness/roughness) |
| Cheap legacy / stylized look | Blinn-Phong |
| Smooth surface highlights | Per-pixel (Phong-frequency) normal interpolation |
| Soft, realistic shadows | Area lights (penumbra) |
| Reflections of the environment | Image-based lighting (HDRI + split-sum) |
| Color bleeding / realistic ambient | Global illumination (path tracing / probes) |
| Real-time indirect light | Probes / SH / DDGI / ray-traced GI + denoise |
| Caustics (focused light through glass) | Photon mapping or bidirectional path tracing |
| Diagnosing materials that "glow" | Check energy conservation: diffuse+spec ≤ 1 |

---

## Common Confusion Points

### "Phong vs PBR — is PBR just 'better Phong'?"

No — it's a different basis. Phong is a tuned formula with no physical meaning to its
knobs; PBR derives reflection from microfacet physics and *enforces* energy conservation
and reciprocity. The practical payoff: PBR materials look correct under any lighting and
transfer between scenes; Phong materials must be re-tuned per scene.

### "What exactly is a BRDF returning?"

A *ratio of radiances*, with units of inverse steradians: outgoing radiance per unit
incoming irradiance, per direction pair. It is **not** a probability and not bounded by 1
pointwise (a sharp mirror's BRDF spikes high in one direction); the *integral* with the
cosine term is what must stay ≤ 1. That distinction trips people up constantly.

### "Why do metals look different in PBR?"

Metals have essentially no diffuse reflection — incoming light is either reflected
specularly or absorbed — and their *specular* reflection is tinted by the base color (gold
reflects yellow). Dielectrics (plastic, wood, skin) have a colorless ~4% specular plus a
colored diffuse. The "metalness" parameter is a switch between these two regimes, which is
why it's binary-ish in authoring.

### "Is the rendering equation actually solvable?"

Not in closed form for real scenes — it's an integral equation with the unknown on both
sides. We *estimate* it: path tracing converges to the true answer statistically
(unbiased); rasterization-era methods approximate it with biased shortcuts. "Solving
graphics" means approximating this one equation well enough for the budget.

### "Ambient light — is that real?"

The constant ambient term is a *fake* — a flat stand-in for the indirect light that real GI
would compute. It's the crudest possible approximation of the hemisphere integral (assume
constant `Li`). The whole arc from constant ambient → ambient occlusion → probes →
ray-traced GI is the field gradually replacing that fudge with the actual integral.
