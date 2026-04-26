# 04 — Geotechnical Engineering

## Soil Mechanics, Foundations, Slopes, Earth Pressure

```
THE GEOTECHNICAL PROBLEM

 SURFACE LOADS
      ↓
┌─────────────────────────────────────────────────────────┐
│  SOIL/ROCK MASS                                         │
│  • 3-phase medium: solid grains + water + air           │
│  • Behavior driven by effective stress σ' = σ − u       │
│  • Strength: τ_f = c + σ' tan φ  (Mohr-Coulomb)         │
│                                                         │
│  Key issues:                                            │
│  Bearing capacity: can the foundation resist load?      │
│  Settlement: how much does it compress? how fast?       │
│  Slope stability: will the slope slide?                 │
│  Earth pressure: how hard does soil push on wall?       │
└─────────────────────────────────────────────────────────┘
```

---

## Soil Composition and Phase Relationships

### The Three-Phase System

```
       ┌─────┐
       │  A  │  Air (volume V_a)
       │─────│
       │  W  │  Water (volume V_w, mass M_w)
       │─────│
       │  S  │  Solids (volume V_s, mass M_s)
       └─────┘

Total volume: V = V_s + V_v   where V_v = V_a + V_w (void volume)
Total mass:   M = M_s + M_w   (air mass neglected)
```

**Phase relationships:**
```
Void ratio:        e = V_v/V_s    (ranges 0.3–1.5 for soils)
Porosity:          n = V_v/V = e/(1+e)
Degree of saturation: S_r = V_w/V_v  (0 = dry, 1 = fully saturated)
Water content:     w = M_w/M_s    (decimal or %)

Dry unit weight:   γ_d = G_s γ_w / (1+e)
Saturated:         γ_sat = (G_s + e) γ_w / (1+e)
Submerged:         γ' = γ_sat − γ_w   (buoyant unit weight)

where G_s = specific gravity of solids ≈ 2.65–2.72 for most minerals
      γ_w = 9.81 kN/m³ (unit weight of water)
```

---

## Soil Classification

### Grain Size Boundaries (ASTM/USCS)

```
Gravel: > 4.75 mm
Sand:   0.075–4.75 mm
Silt:   0.002–0.075 mm  (not visible to naked eye)
Clay:   < 0.002 mm (colloidal, platelet shape, surface chemistry important)
```

### Atterberg Limits (Fine-Grained Soils)

```
Liquid Limit (LL): water content where soil transitions from plastic to liquid
Plastic Limit (PL): water content where soil transitions from brittle to plastic
Plasticity Index: PI = LL − PL   (range of plastic behavior)
Liquidity Index:  LI = (w − PL)/PI   (0=plastic limit, 1=liquid limit, >1=liquid)
```

### USCS Classification

```
GW, GP: Gravel (W=well-graded, P=poorly-graded)
GM, GC: Gravel with fines (M=silt, C=clay)
SW, SP: Sand (W=well-graded, P=poorly-graded)
SM, SC: Sand with fines
ML, CL: Low plasticity silt and clay (LL < 50%)
MH, CH: High plasticity silt and clay (LL > 50%)
OL, OH: Organic soils
PT:     Peat
```

**Engineering significance:**
- GW, SW: excellent foundations, high friction, low compressibility
- CH: problematic — high compressibility, high swell potential, low strength when wet
- PT: unsuitable for direct foundation support

---

## Permeability and Seepage

**Darcy's Law:**
```
q = k i A   (discharge flow rate [m³/s])
v = k i      (discharge velocity, not actual pore fluid velocity)

where:
  k = hydraulic conductivity [m/s]   (permeability)
  i = hydraulic gradient = Δh/L = (h₁−h₂)/L
  A = cross-sectional area

Typical k values:
  Clean gravel:     10⁻¹ to 10⁰ m/s
  Clean sand:       10⁻⁴ to 10⁻² m/s
  Silty sand:       10⁻⁷ to 10⁻³ m/s
  Silt:             10⁻⁹ to 10⁻⁵ m/s
  Clay:             10⁻¹¹ to 10⁻⁹ m/s
```

**Seepage and flow nets:** Graphical technique — flow lines + equipotential lines form curvilinear squares. Used to find seepage quantity and pore pressures under dams/levees.

```
q = k h (N_f/N_d)
  N_f = number of flow tubes, N_d = number of equipotential drops, h = total head difference
```

**Piping:** When upward seepage force equals submerged weight → quicksand/piping failure.
```
Critical hydraulic gradient: i_cr = (G_s − 1)/(1+e) ≈ 1.0 for many soils
Factor of safety against piping: FS = i_cr / i_actual > 1.5–2.0
```

---

## Effective Stress (Terzaghi's Principle)

**The single most important concept in soil mechanics:**

```
σ' = σ − u

σ  = total stress (from overburden + applied loads)
u  = pore water pressure (hydrostatic: u = γ_w × h_w)
σ' = effective stress = stress carried by grain-to-grain contact

ALL shear strength and consolidation behavior governed by σ', not σ
```

**Why it matters:**
- Saturated clay: apply load → u increases immediately → σ' unchanged → no immediate strength gain
- Over time: drainage → u dissipates → σ' increases → strength increases
- Undrained strength S_u = c_u: appropriate for rapid loading (no drainage)
- Drained friction φ': appropriate for long-term (full drainage)

---

## Consolidation and Settlement

### Terzaghi's 1D Consolidation Theory

This is the 1D heat/diffusion equation with u (excess pore pressure) playing the role of temperature, and c_v as the thermal diffusivity. The solution is the standard Fourier series (separation of variables: sine modes in z, exponential decay in t), and T_v = c_v t / H_dr^2 is the Fourier number. The entire consolidation time-history follows from the same mathematics as transient heat conduction in a slab with fixed-temperature boundaries.

```
∂u/∂t = c_v ∂²u/∂z²   (diffusion equation for excess pore pressure)

c_v = k(1+e₀) / (a_v γ_w)   (coefficient of consolidation)
    = k / (m_v γ_w)            m_v = coefficient of volume compressibility

Time factor: T_v = c_v t / H_dr²
  H_dr = drainage path length (= H/2 for drainage top and bottom)

Degree of consolidation U:
  T_v = 0.010 → U = 11%
  T_v = 0.197 → U = 50%
  T_v = 0.848 → U = 90%
  T_v ≈ (π/4)U² for U < 60%   (approximate)
```

### Settlement Magnitude

```
Normally consolidated clay:
  S_c = Cc/(1+e₀) × H × log₁₀((σ'₀ + Δσ')/σ'₀)

Overconsolidated clay (σ'₀ + Δσ' < σ'_pc):
  S_c = Cs/(1+e₀) × H × log₁₀((σ'₀ + Δσ')/σ'₀)    [Cs << Cc]

Cc = compression index (slope of e-log σ' curve in normally consolidated range)
Cs = swelling index ≈ Cc/5 to Cc/10

Overconsolidation Ratio: OCR = σ'_pc / σ'₀  (OCR > 1: overconsolidated, stiffer)
```

**Stress distribution in soil (Boussinesq, point load Q on surface):**
```
Δσ_z = 3Q z³ / (2π r⁵)   where r = √(x²+y²+z²)

For spread footings: use Boussinesq chart or 2:1 stress spread approximation
  2:1 method: Δσ = Q / ((B+z)(L+z))  [rough but quick]
```

---

## Shear Strength

### Mohr-Coulomb Failure Criterion

```
τ_f = c' + σ' tan φ'    (drained, effective parameters)
τ_f = c_u              (undrained, S_u = undrained shear strength)

c' = effective cohesion intercept [kPa]  (0 for clean sand; 0–50 for clay)
φ' = effective friction angle [degrees]   (28–48° sand; 20–35° clay)
c_u = undrained cohesion [kPa]            (unconfined compression: q_u = 2 c_u)
```

**Typical φ' values:**
| Soil | φ' (degrees) |
|------|------------|
| Loose clean sand | 28–34 |
| Dense clean sand | 36–45 |
| Silty sand | 28–36 |
| Gravel | 35–45 |
| Normally consolidated clay | 20–30 |
| Overconsolidated clay | 25–35 |

### Field Tests

| Test | Measure | Best use |
|------|---------|---------|
| SPT (Standard Penetration) | N-value (blow count) | Sand: correlate to φ', density |
| CPT (Cone Penetration) | q_c, f_s continuously | Both sand + clay; profile |
| VST (Vane Shear) | S_u (undrained) | Soft clays |
| Pressuremeter | Elastic modulus, p_L | Rock and stiff soil |
| Plate load test | Modulus, bearing capacity | Direct but expensive |

---

## Shallow Foundation Bearing Capacity

**Terzaghi's bearing capacity equation (general shear failure):**
```
q_ult = c N_c + q N_q + ½ γ B N_γ

q = γ D_f  (overburden pressure at foundation level)
B = footing width
N_c, N_q, N_γ = bearing capacity factors (depend on φ')

φ' = 0°:   N_c = 5.14, N_q = 1, N_γ = 0  → q_ult = 5.14 c_u + γ D_f
φ' = 30°:  N_c ≈ 30, N_q ≈ 18, N_γ ≈ 15
φ' = 35°:  N_c ≈ 46, N_q ≈ 33, N_γ ≈ 37

Shape factors (Meyerhof/Hansen):
  Sc = 1 + 0.4(B/L)     for strip (B/L→0), square (B/L=1), circle (B/L=1)

Allowable bearing capacity: q_allow = q_ult / FS   (FS = 3 typical for buildings)
```

---

## Earth Pressure Theories

### Rankine Earth Pressure

For smooth wall (no wall friction), horizontal backfill:
```
Active pressure (wall moves away from soil):
  K_a = tan²(45° − φ'/2)    (coefficient of active earth pressure)
  σ_h = K_a σ'_v − 2c'√K_a

  At rest (no movement): K₀ = 1 − sin φ' (Jaky's formula)
  Passive (wall pushed into soil): K_p = tan²(45° + φ'/2)

  K_a < K_0 < K_p  always
  For φ'=30°: K_a=0.33, K₀=0.5, K_p=3.0
```

**Pressure distribution diagram:**
```
Active pressure on wall (granular, no cohesion, uniform backfill):
  Triangular: σ_h = K_a γ z   (increases linearly with depth)
  Resultant: P_a = ½ K_a γ H²  (acts at H/3 from base)
```

**Coulomb's method:** Considers wall friction; use for more accurate cases.

### Retaining Wall Design

```
Check sliding: ΣF_horizontal ≤ μ × N_vertical
  ΣP_a (active) must be resisted by base friction + passive
  FS_sliding ≥ 1.5

Check overturning about toe:
  ΣM_resisting / ΣM_overturning ≥ 1.5–2.0

Check bearing capacity:
  Eccentricity e = B/2 − ΣM/ΣV < B/6 (resultant in middle third → no tension)
  q_max = ΣV/B × (1 + 6e/B) < q_allow
```

---

## Slope Stability

**Factor of safety:** FS = available shear strength / required shear strength for equilibrium

### Swedish Circle Method (ϕ = 0 analysis — undrained)

```
FS = M_resisting / M_driving = (S_u × r × L_arc) / (W × d)

where:
  r = radius of failure circle
  L_arc = arc length
  W = weight of failure mass
  d = horizontal distance from center to centroid of W
```

### Bishop's Simplified Method (general)

More accurate for c-phi soils. Considers vertical interslice forces only. Note the iteration structure: FS appears on both sides (m_alpha depends on FS), making this a fixed-point iteration FS_{k+1} = g(FS_k). The function g is monotone and contractive for physically reasonable parameters, so convergence is guaranteed and typically requires 3-5 iterations from any reasonable initial guess (FS_0 = 1.0 works fine).
```
FS = [Σ((c' b + (W − u b) tan φ') / m_α)] / Σ(W sin α)

m_α = cos α + sin α tan φ'/FS   (iterative!)

Divide slope into vertical slices:
  b = width, W = weight, u = pore pressure, α = base angle
```

**Seismic stability:** Add horizontal force k_h × W to each slice (pseudostatic).
Liquefaction reduces φ' dramatically — loose saturated sands can reach FS < 1.

---

## Deep Foundations (Piles)

```
Pile capacity: Q_ult = Q_tip + Q_skin

  Tip resistance: Q_tip = q_p A_p
    Sand: q_p = N_q σ'_v (Meyerhof)
    Clay: q_p = 9 c_u (undrained)

  Skin friction: Q_skin = ∫ f_s dA_perimeter
    Sand: f_s = β σ'_v (β = 0.2–0.4 for driven piles)
    Clay: f_s = α c_u  (α = 0.5–1.0, adhesion factor)

Design: Q_allow = Q_ult / FS,   FS = 2.5–3.0
```

**Pile group efficiency:** < 1 when piles close together (soil blocks form instead of individual piles).

---

## Liquefaction

**Criterion:** Factor of safety against liquefaction FS_L = CRR/CSR

```
Cyclic Stress Ratio (seismic demand):
  CSR = 0.65 (σ_v/σ'_v) (a_max/g) r_d
  a_max = peak ground acceleration, r_d = depth-dependent stress reduction

Cyclic Resistance Ratio (soil supply):
  CRR = f(N₁₆₀ from SPT, or q_c1N from CPT)
  N₁₆₀ = SPT N corrected to 60% energy efficiency and 100 kPa overburden

FS_L < 1.0: liquefaction expected
```

**Susceptibility:** Loose, saturated, uniformly graded sand with water table near surface.
1964 Niigata earthquake, 2010–2011 Christchurch earthquakes: large-scale liquefaction observed.

---

## Common Confusion Points

**Effective stress controls everything:** Total stress σ is easy to compute (just overburden). Pore pressure u must be measured or estimated. The difference σ' = σ − u is what governs strength and deformation. Applications of total load with no drainage → no immediate strength gain in saturated clay.

**Undrained vs drained parameters:** Use c_u and S_u for rapid loading of clay (embankment construction, earthquake). Use c' and φ' for long-term stability (after drainage). Clean sands drain so fast that undrained analysis rarely applies.

**Cohesion vs cohesiveness:** Pure sand has c' = 0 but has apparent cohesion when moist (surface tension). This disappears when saturated or dried. Don't rely on it for design.

**Settlement time:** Primary consolidation time scales as H_dr². A 1m thick clay layer under a building may consolidate in weeks. A 10m thick layer: 100× longer = years to decades. This is why preloading/surcharge + vertical drains work.

**Active vs passive vs at-rest:** Most retaining walls should be designed for active pressure (wall yields slightly away from soil — acceptable for most flexible walls). At-rest pressure (K₀) is for rigid non-yielding walls (basement walls, integral bridge abutments).

---

## Decision Cheat Sheet

| Task | Method | Notes |
|------|--------|-------|
| Bearing capacity (shallow) | Terzaghi equation | Adjust for shape/depth/inclination |
| Settlement (clay) | Terzaghi consolidation | Need compression index Cc |
| Shear strength (sand) | φ' from SPT/CPT | SPT N-value → φ' correlation |
| Shear strength (clay, rapid) | S_u (undrained) | Vane shear or UU triaxial |
| Earth pressure on wall | Rankine or Coulomb | Include water pressure separately! |
| Slope stability | Bishop's simplified | Iterate for FS |
| Liquefaction potential | CSR vs CRR | Needs seismic a_max and SPT data |
| Pile capacity | α or β method | Driven vs bored affects skin friction |
