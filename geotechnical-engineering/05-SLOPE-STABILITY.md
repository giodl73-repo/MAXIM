# Slope Stability: Limit Equilibrium, Bishop Method, Seismic Stability

## The Big Picture

Slopes fail when driving forces (gravity component along failure surface) exceed resisting forces (shear strength along the surface). Limit equilibrium methods find the ratio of available shear strength to mobilized shear stress — the factor of safety — along a trial failure surface. The minimum F over all possible surfaces determines stability.

```
+------------------------------------------------------------------+
|               SLOPE STABILITY — ANALYSIS HIERARCHY               |
+------------------------------------------------------------------+
|                                                                  |
|  CHARACTERIZE SLOPE AND GEOMETRY                                 |
|  Soil profile, shear strength parameters, water levels          |
|              |                                                    |
|              v                                                   |
|  SELECT ANALYSIS TYPE                                            |
|  +------------------+  +------------------+  +--------------+  |
|  |  INFINITE SLOPE  |  | CIRCULAR FAILURE |  | NON-CIRCULAR |  |
|  |  Shallow, long   |  | Homogeneous soil |  | Layered soils|  |
|  |  translational   |  | or weak layer    |  | Hard base    |  |
|  |  failures        |  |                  |  | Complex geo  |  |
|  +------------------+  +------------------+  +--------------+  |
|              |                   |                   |          |
|              v                   v                   v          |
|  Infinite slope     Bishop simplified    Janbu or Spencer        |
|  equation           (most common)        (complex geometry)      |
|              |                                                   |
|              v                                                   |
|  COMPUTE F = resisting moment / driving moment                  |
|  (or resisting forces / driving forces)                         |
|              |                                                   |
|              v                                                   |
|  Minimum F over all trial surfaces → governing failure mode     |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Types of Slope Failure

| Failure Type | Geometry | Typical Soils | Key Variables |
|-------------|---------|---------------|---------------|
| **Planar** | Failure on a single plane | Rock slopes, thin weak layer | Geometry, water pressure on plane |
| **Rotational (circular)** | Curved failure surface, mass rotates | Homogeneous clay or uniform fill | Su, c', φ', pore pressure |
| **Translational (block)** | Mass slides on nearly flat weak layer | Clay varves, bedding planes | Weak layer strength, water pressure |
| **Compound** | Part circular, part planar | Layered soils with weak horizons | Multiple strength parameters |
| **Debris flow** | Steep, saturated, rapid | Colluvium, volcanic deposits | High pore pressures, loose structure |
| **Progressive failure** | Strain-softening OC clay | Intact OC clay | Peak → residual reduction |

---

## Infinite Slope Analysis

For shallow, long landslides (depth H << length) on a slope angle β, the failure is approximately planar and parallel to the slope surface.

```
INFINITE SLOPE MODEL:

  Surface of slope → β angle
  ─────────────────────────────────────────
    ↗ β                          failure
  ─────────────────────────────────────────
  depth z                        plane
  ─────────────────────────────────────────

  Stresses on failure plane:
  Normal: σ'n = γ'z cos²β  (using buoyant γ' if below water table)
  Shear:  τ = γ'z sinβ cosβ
```

**Factor of Safety** (general, effective stress):

**F = c' / (γz sinβ cosβ) + (tanφ' / tanβ) × (1 - ru)**

where **ru = u / (γz)** = pore pressure ratio

When ru = 0 (dry slope): F = c'/(γz sinβ cosβ) + tanφ'/tanβ
For cohesionless slope, c' = 0: F = tanφ' / tanβ × (1 - ru)

At saturation (ru = 0.5 for water table at surface, γsat ≈ 2γw):
F = tanφ' / (2 × tanβ)

**Key insight**: A fully saturated cohesionless slope has half the factor of safety of a dry slope. This explains why many shallow landslides occur during or after heavy rainfall.

---

## Method of Slices — General Framework

For circular (or general) failure surfaces, the mass is divided into vertical slices. For each slice i:
- Width: b_i
- Height: h_i (to center of slice base)
- Slice weight: W_i = γ × b_i × h_i
- Angle of slice base to horizontal: α_i

Forces on each slice base:
- Normal: N_i (total) = N'_i + u_i × l_i
- Shear: T_i = τ_f × l_i (at limit equilibrium)

The factor of safety F = available shear / mobilized shear:
**T_i = (c' × l_i + N'_i × tanφ') / F**

The methods differ in how they handle interslice forces.

---

## Fellenius (Ordinary) Method

**Assume**: No interslice forces.

N'_i = W_i cos α_i - u_i × l_i

**F = Σ(c' × l_i + (W_i cos α_i - u_i × l_i) × tanφ') / Σ(W_i sin α_i)**

Advantage: Explicit solution, no iteration.
Disadvantage: **Significantly underestimates F** for shallow slip circles or high pore pressures. Errors of 10–15% are common. Not recommended for design.

---

## Bishop's Simplified Method

**Assume**: Interslice forces are horizontal (no interslice shear).

The resulting equation for F is implicit — must iterate:

**F = Σ[(c' × b + (W - u × b) tanφ') / mα] / Σ(W × sinα)**

where: **mα = cosα × (1 + tanα × tanφ' / F)**

**Iteration procedure**:
1. Assume F = 1.5 (initial guess)
2. Compute mα for each slice
3. Compute new F
4. Repeat until F converges (typically 3–5 iterations)

Bishop's is accurate to within ~1–2% of the exact solution for circular failure surfaces. It is the workhorse method for routine circular failure analysis.

---

## Janbu's Generalized Method

For non-circular failure surfaces (required when weak layers are not circular):

Janbu uses horizontal force equilibrium (not moment) and an interslice force correction factor f0:

**F = f0 × Σ[(c' × b + (W - u × b) tanφ') / (cosα + sinα × tanφ'/F)] / Σ(W tanα)**

f0 ≈ 1.0 to 1.1 (correction for interslice moment neglect; Janbu's chart).

Accurate for non-circular surfaces but requires more input and iteration.

---

## Spencer's Method (Rigorous)

Satisfies both force and moment equilibrium. Assumes interslice force at a constant angle θ to horizontal. Solve two unknowns (F and θ) simultaneously — requires numerical solution.

Most accurate method for general failure surfaces. Required by some codes for critical infrastructure.

---

## Stability Charts

For preliminary analysis, Taylor's chart (1937) and Bishop's chart give F directly from geometry and strength:

**Taylor's chart** (undrained, c only, φ = 0):
F = Ns × Su / (γ × H)
where Ns = stability number from chart (function of β and depth factor D = depth to hard base / slope height)

Typical Ns values:
- β = 90° (vertical cut): Ns = 3.83 (maximum height = 3.83Su/γ)
- β = 45°: Ns ≈ 5.5
- β = 30°: Ns ≈ 6+

---

## Seismic Slope Stability

### Pseudostatic Approach

Apply a horizontal seismic force = kh × W to each slice:

**F = Σ[(c' × b + (W cos α - u × b - kh × W × sin α) × tanφ') / mα_seismic] / Σ(W sin α + kh × W × cos α)**

kh = horizontal seismic coefficient = PGA/g × factor (typically 0.5–1.0 depending on code)

Limitation: pseudostatic gives F > 1 or < 1 but doesn't estimate deformation. Acceptable for simple cases; conservative.

### Newmark Sliding Block Method (1965)

When F(pseudostatic) < 1 during part of an earthquake, the slope deforms permanently. Newmark's method estimates permanent displacement:

1. Determine yield acceleration ay = g × (F-1) × components... → the acceleration at which F = 1.0
2. Integrate the acceleration time history segments exceeding ay
3. Result: permanent displacement estimate

```
NEWMARK SLIDING BLOCK CONCEPT:

  Ground acceleration history: ─────/\──/\/\──/\────
  Yield acceleration ay:       ─────────────────────  ← threshold

  When ground accel > ay: block slides (accumulates displacement)

  Double integration of (accel - ay) × dt² for exceedance periods
  = permanent displacement

  Rough correlation (Jibson 2007):
  log Dn = 0.215 + log[(1-ay/PGA)^2.341 × (ay/PGA)^-1.438]
  where PGA = peak ground acceleration, Dn in cm
```

---

## Common Failure Causes and Warning Signs

| Cause | Mechanism | Warning Signs |
|-------|-----------|--------------|
| Toe erosion | Removes passive resistance | Undercutting of slope base |
| Rainfall/saturation | ru increases → F decreases | Rapid pore pressure rise in piezometers |
| Seepage | Seepage forces, softening | Springs emerging from slope face |
| Surcharge | Increases driving moment | New construction, fill placement above slope |
| Excavation at toe | Reduces normal stress and passive resistance | Horizontal displacement indicators, tension cracks |
| Loss of suction | Capillary suction lost on saturation | Surface tension cracks, recent heavy rain |
| Creep / progressive failure | Strain softening from peak to residual | Slow inclinometer movement |

---

## Monitoring

| Instrument | Measures | Threshold Action |
|-----------|---------|-----------------|
| **Inclinometer** | Lateral displacement profile with depth | Rapid acceleration or localized deflection |
| **Piezometer (standpipe or VW)** | Pore pressure at specific depth | Pore pressure approaching design limit |
| **GPS/survey points** | Surface displacement | Velocity increase, especially after rain |
| **Crackmeters** | Tension crack opening | Increasing rate of opening |
| **Tiltmeters** | Rotation of slope or structure | Increasing tilt rate |

---

## Decision Cheat Sheet

| Situation | Method | Parameters |
|-----------|--------|-----------|
| Shallow rainfall-triggered landslide | Infinite slope | c', φ', ru (measure piezometer) |
| Cut slope in homogeneous clay | Bishop simplified | Su (undrained) or c', φ' (drained) |
| Embankment on soft clay | Bishop simplified | Su of foundation clay |
| Complex layered profile with weak seam | Janbu or Spencer | c', φ' for each layer |
| Earthquake stability | Pseudostatic (screening) + Newmark (deformation) | kh, ay vs. earthquake record |
| Preliminary estimate | Taylor or Bishop stability chart | Su, γ, H, β |

---

## Common Confusion Points

**F > 1 does not mean the slope is safe by much**: F = 1.05 is not acceptable design. Typical minimum requirements: F ≥ 1.5 for permanent slopes under static conditions; F ≥ 1.3 for temporary construction slopes; F ≥ 1.1 for seismic loading.

**Circular failure surface is not always critical**: The minimum-F surface is not necessarily circular. For layered profiles with a thin weak layer, the critical surface may be non-circular (composite). Use Janbu or Spencer for these cases.

**End-of-construction vs. long-term**: For embankments on soft clay, end-of-construction (undrained, Su) is typically critical. For cut slopes in OC clay, long-term (drained, c' = 0, φ'residual) is critical. Don't analyze only one condition.

**Ru is not equal to the water table position**: ru = u / (γz) — it depends on γz (total vertical stress), not just head. A water table at the surface in a slope with γ ≈ 2γw gives ru ≈ 0.5. ru is not 1.0 even with the water table at the surface.
