# Shear Strength: Mohr-Coulomb, Triaxial Tests, Critical State, Residual Strength

## The Big Picture

Soil fails in shear — not compression or tension. When you push soil to its limit (under a footing, inside a slope, behind a retaining wall), it mobilizes shearing resistance along a failure surface. Understanding what governs that resistance — and how it changes with drainage conditions and stress history — is the core of geotechnical strength analysis.

```
+------------------------------------------------------------------+
|               SHEAR STRENGTH — CONCEPTUAL MAP                   |
+------------------------------------------------------------------+
|                                                                  |
|  MOHR-COULOMB FAILURE CRITERION                                  |
|  τ_f = c' + σ'_n × tan(φ')     [effective stress parameters]   |
|  τ_f = cu (= Su)               [total stress for undrained]     |
|                                                                  |
|  KEY DISTINCTION:                                                |
|  DRAINED analysis: stresses change slowly; pore pressure        |
|  ≈ hydrostatic throughout loading; use c', φ'                   |
|                                                                  |
|  UNDRAINED analysis: stresses change faster than drainage;      |
|  excess pore pressure develops; use Su = cu (φ=0 analysis)      |
|                                                                  |
|  WHEN DOES EACH APPLY?                                           |
|  Sand: always drained (high k → pore pressure dissipates fast)  |
|  Soft clay: short-term = undrained; long-term = drained         |
|  Stiff clay: often drained controls (swells long-term)          |
|                                                                  |
+------------------------------------------------------------------+
```

---

## The Mohr-Coulomb Failure Criterion

### Effective Stress Form

**τ_f = c' + σ'_n × tan φ'**

where:
- τ_f = shear stress at failure (shear strength)
- c' = effective cohesion intercept (kPa)
- σ'_n = effective normal stress on failure plane
- φ' = effective friction angle

```
MOHR CIRCLE AND FAILURE ENVELOPE:

  τ
  |               Failure envelope
  |              /   τ = c' + σ'tanφ'
  |             /
  |            /   *
  |           / *     (σ'3, 0) ... (σ'1, 0) Mohr circle
  |          /*          ^
  |         *           failure if circle tangent to envelope
  |        /
  +──────────────────────── σ'
  0     c'/tanφ'

  Each Mohr circle = one test (different confining pressure)
  Failure envelope = best-fit line tangent to circles
  Slope = tanφ', intercept = c'
```

### The Friction Angle

φ' governs how shear strength increases with normal stress. It comes from:

1. **Mineral friction**: Quartz-quartz contact friction ≈ 26–30°
2. **Particle interlocking**: denser/rounder particles → lower effective φ'
3. **Dilation**: dense sands dilate (expand) during shear → extra resistance → φ'peak > φ'critical

For design, distinguish:
| Parameter | Meaning | Use |
|-----------|---------|-----|
| φ'peak | Strength at failure | Short-term, pre-failure calculations |
| φ'critical state (φ'cv) | Strength after large strain (dilation complete) | Post-failure, residual |
| φ'residual | Strength after very large strain (clay particles aligned) | Reactivated landslides |

### The Cohesion Intercept

c' for clean sands = 0. Sand has no cohesion.

c' for clays: true cohesion (cementation between particles) is rare. Most apparent c' from:
- Suction (negative pore pressure) in unsaturated soils
- Time-dependent structure (thixotropy, diagenesis)
- Testing artifacts (poor saturation, incorrect drainage)

For long-term stability: use c' = 0 for most clays (conservative but reasonable). The c' from fitting Mohr-Coulomb to a range of stresses is a statistical artifact of the nonlinear actual strength envelope.

---

## Laboratory Shear Tests

### Direct Shear Test

Simple and widely used:
- Soil sample in split box; horizontal shearing plane forced
- Normal load applied; shear force measured at displacement
- Advantage: simple, fast, disturbed or undisturbed samples
- Disadvantage: failure plane forced (not necessarily the weakest); drainage conditions poorly controlled

Output: τ vs. σ'_n at failure → plot several tests → Mohr-Coulomb line

### Triaxial Test

More controlled, better for clayey soils. Three test types:

```
TRIAXIAL TEST CONFIGURATIONS:

  +------------------+------------------+------------------+
  |    UU TEST        |    CU TEST        |    CD TEST       |
  |  (Unconsolidated  |  (Consolidated-   |  (Consolidated-  |
  |   Undrained)      |   Undrained)      |   Drained)       |
  +------------------+------------------+------------------+
  | Consolidation:    | Consolidate to    | Consolidate to   |
  | NOT consolidated  | in-situ stress    | target stress    |
  | before shear      | before shear      | before shear     |
  +------------------+------------------+------------------+
  | Drainage in shear:| Closed (no        | Open (slow shear |
  | Closed            | drainage)         | so Δu dissipates)|
  +------------------+------------------+------------------+
  | Pore pressure:    | Measured (so      | Controlled       |
  | Not measured      | effective stress  | (u = hydrostatic)|
  |                   | known)            |                  |
  +------------------+------------------+------------------+
  | Results:          | c', φ' in terms   | c', φ' in terms  |
  | Su = qu/2         | of effective      | of effective     |
  | (total stress,    | stress (reliable) | stress (most     |
  | φ = 0 analysis)   |                   | fundamental)     |
  +------------------+------------------+------------------+
  | Use for:          | Short-term +      | Long-term        |
  | Quick loading,    | long-term analysis| analysis, drained|
  | field vane check  |                   | slopes           |
  +------------------+------------------+------------------+
```

### Mohr Circle Construction (Triaxial)

Given UU test with σ3 = 100 kPa, failure at σ1 = 280 kPa:
- Center of Mohr circle: p = (280 + 100)/2 = 190 kPa
- Radius: q = (280 - 100)/2 = 90 kPa = Su

Multiple UU tests with different σ3 all give same Su (horizontal line φ=0) for saturated NC clay.

---

## Undrained Shear Strength Su

For saturated saturated clay, undrained analysis uses:
**τ_f = Su = cu** (with φu = 0)

Su is not a unique material property — it depends on:
- Stress history (OCR): Su ≈ 0.11 + 0.0037 × PI (Skempton, NC)
- Su/σ'v increases with OCR
- Anisotropy (horizontal vs. vertical shearing)
- Test type (triaxial compression > triaxial extension > direct simple shear)
- Strain rate (higher rate → higher Su)

Field measurement of Su:
- **Field vane shear test (VST)**: drive cross-shaped vane, torque to failure
  Su = T / (K × D³) where K = π/2(1 + D/3H) for solid cylinder, T = torque, D = diameter
- **CPT**: Su ≈ (qt - σvo) / Nkt, where Nkt ≈ 12–20 (site-specific)
- **Pressuremeter**: direct measurement of Su from limit pressure

---

## Critical State Soil Mechanics

Roscoe and colleagues at Cambridge (1960s) developed critical state soil mechanics — a unified framework for understanding soil behavior.

### The Critical State

The **critical state** is the condition at which soil continues to deform at constant volume under constant stress. All soils, regardless of initial density or stress history, tend toward the critical state after sufficient shearing.

**Critical State Line (CSL)**: A unique line in e – log p' – q' space:
- In p'-q' space: q' = M × p' (slope M = 6sinφ'/(3-sinφ'))
- In e – log p' space: a line parallel to the VCL, offset by κ (where κ ≈ λ - κ)

```
CRITICAL STATE IN e - log p' SPACE:

  e (void ratio)
  |   VCL (virgin compression line)
  |  \
  |   \      CSL (critical state line, parallel to VCL)
  |    \    \
  |     \    \  Dense sample (low e) → DILATES toward CSL
  |      \    \
  |       \    \   Loose sample (high e) → CONTRACTS toward CSL
  |        \    \
  +──────────────── log p'

  DENSE SAND (left of CSL):
  Shear → volume increases (dilation) → negative Δu (undrained)
  → reaches CSL from below

  LOOSE SAND (right of CSL):
  Shear → volume decreases (contraction) → positive Δu (undrained)
  → reaches CSL from above (can liquefy if undrained)
```

### The Cam Clay Model

Cambridge developed the Cam Clay model — the first elastic-perfectly-plastic constitutive model for soil. Key:
- Yield surface: ellipse in p'-q' space
- Hardening: cap expands as void ratio decreases (preconsolidation pressure increases)
- Critical state on the ellipse at q/p' = M

Practical use: numerical models (FEM) for embankments, excavations, tunnels in soft clay. Software: PLAXIS, ABAQUS with Cam Clay.

---

## Residual Shear Strength

After very large displacements (meters), clay particles align parallel to the shear surface. The cohesion drops to zero and friction angle reaches a minimum:

**τ_r = σ'_n × tan φ'_r**

φ'_r is much lower than φ'peak:
- London clay: φ'r ≈ 10–12°, φ'peak ≈ 20°
- Montmorillonite-rich soils: φ'r can be as low as 5–8°

**Measured by**: ring shear test (unlimited displacement on fixed plane); or back-analysis of existing landslides.

**Critical for**:
- Reactivated landslides (failure surface already formed → use φ'r)
- Long-term stability of cut slopes in OC clays
- Dam foundations in clayey rock

---

## Stress-Dilatancy and Angle of Dilation

Dense soils dilate (expand) during shear. Rowe's stress-dilatancy theory relates peak friction angle to critical state friction angle plus a dilation component:

**φ'peak = φ'cv + ψ** (approximate)

where ψ = angle of dilation (rate of volume expansion vs. shear strain).

Dense sand: ψ ≈ 5–15°
Dense gravel: ψ can exceed 20°

For slope stability: do not use φ'peak if large strains expected. Progressive failure in OC clay can reduce mobilized φ' to residual.

---

## Decision Cheat Sheet

| Situation | Analysis | Strength Parameters |
|-----------|----------|---------------------|
| Sand, any loading rate | Drained (always) | c' = 0, φ' from direct shear or CPT correlation |
| Soft clay, rapid loading | Undrained (φ = 0) | Su from UU triaxial or field vane |
| Soft clay, long-term | Drained | c' ≈ 0, φ' from CU or CD triaxial |
| OC clay, cut slope long-term | Drained, may be residual | φ'r from ring shear or back-analysis |
| End-of-construction stability | Undrained for clay | Su = Su at in-situ OCR |
| Reactivated landslide | Residual strength | φ'r; c' = 0 |
| Earthquake loading | Undrained for saturated sand | Check liquefaction (cyclic resistance) |

---

## Common Confusion Points

**φ' and Su are not interchangeable**: φ' is an effective stress parameter used in drained analysis. Su is a total stress undrained strength. Don't use Su in a Mohr-Coulomb formula with effective stresses — the result is dimensionally correct but conceptually wrong.

**c' does not mean real cohesion**: For most soils, c' from Mohr-Coulomb fitting is a statistical parameter, not real cementation. For long-term stability in normally consolidated clays, c' = 0 is the appropriate conservative assumption.

**Peak strength is not always appropriate**: For plastic clays, strains can be large enough that strength has reduced from peak to critical state or residual. Progressive failure (strain-softening) in OC clay slopes can cause failures at average stresses well below peak.

**The UU test gives Su, not φ' and c'**: A series of UU tests on saturated clay should give a horizontal failure envelope (φu = 0). If it doesn't, the sample is not fully saturated (check B coefficient). Using UU tests to get "c" and "φ" is a common error.
