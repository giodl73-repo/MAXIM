# Rivers and Floodplains — Channel Morphology, Manning Equation, Meandering, Sediment Transport

## The Big Picture

```
+===========================================================================+
|                   RIVER SYSTEM STRUCTURE                                  |
|         From headwater to delta — energy, sediment, and form              |
+===========================================================================+
|                                                                           |
|  HEADWATER REACHES                                                        |
|  Steep gradient, bedrock channels, waterfalls, gorges                    |
|  Energy: high; Sediment: supply-limited (export > supply)                 |
|  Erosion dominant; V-shaped valleys                                       |
|          │                                                                |
|          ▼ Increasing discharge, decreasing slope                        |
|  TRANSPORT REACHES                                                        |
|  Gravel-bed channels, alternating pool-riffle                            |
|  Energy: moderate; Sediment: transport-limited (in equilibrium)           |
|          │                                                                |
|          ▼                                                                |
|  LOWLAND REACHES                                                          |
|  Sand-bed channels, meanders, floodplains                                |
|  Energy: low; Sediment: deposition-dominant                               |
|  Wide flat floodplains, oxbow lakes, wetlands                            |
|          │                                                                |
|          ▼                                                                |
|  COASTAL/DELTA                                                            |
|  Distributary network, tidal influence, sediment deposition              |
+===========================================================================+
```

---

## Channel Geometry and Cross-Section

```
BASIC CHANNEL DIMENSIONS:
  Width W = channel top width (m) at bankfull stage
  Depth D = mean depth = Area/W (m) at bankfull stage
  Hydraulic radius R = A/P (m) ← P = wetted perimeter
  For wide channels: R ≈ D

  HYDRAULIC GEOMETRY RELATIONSHIPS (Leopold & Maddock, 1953):
  As discharge Q increases downstream:
    Width:    W = aQ^b     (b ≈ 0.5)
    Depth:    D = cQ^f     (f ≈ 0.4)
    Velocity: V = kQ^m     (m ≈ 0.1)
    Where b + f + m = 1.0 (continuity: Q = WDV)

  These power-law relationships hold with remarkable consistency worldwide.
  Local variability reflects geology (bedrock control), vegetation, discharge history.

BANKFULL DISCHARGE:
  Q_bf = discharge that fills channel to the top without spilling onto floodplain
  Approximately equal to: 1.5-year recurrence interval (on average)
  The "channel-forming discharge" — shapes the channel geometry over time
  Channel geometry ADJUSTS to bankfull Q through:
    Erosion of banks (widening) or deposition (narrowing)
    Scour of bed (deepening) or fill (raising)
```

---

## Manning Equation

```
MANNING'S EQUATION (1889) — steady uniform flow:
  Q = (1/n) × A × R^(2/3) × S^(1/2)

  Or in terms of velocity:
  V = (1/n) × R^(2/3) × S^(1/2)

  Q = discharge (m³/s)
  A = cross-sectional area (m²)
  R = hydraulic radius = A/P (m)
  S = channel slope (m/m) = energy grade line slope
  n = Manning's roughness coefficient (dimensionless)

  US customary units: V = (1.486/n) × R^(2/3) × S^(1/2)  [V in ft/s, R in ft]

  ROUGHNESS COEFFICIENT n — representative values:
    Smooth concrete/pipe:        n = 0.010–0.013
    Earth channel (good):        n = 0.020–0.025
    Natural stream (clean):      n = 0.025–0.035
    Natural stream (minor weeds): n = 0.030–0.040
    Natural stream (heavy weeds): n = 0.040–0.070
    Mountain stream (boulders):  n = 0.040–0.070
    Flood plain (heavy brush):   n = 0.070–0.160

  Manning's n INCREASES with:
    Larger grain size / rougher bed
    Vegetation (submerged or emergent)
    Channel irregularity, cross-section variability
    Obstructions

COMPOUND SECTION (floodplain):
  Main channel + floodplain carry flow separately at flood stage
  Calculate Q_main and Q_overbank separately (different n, geometry)
  Total Q = Q_main + Q_overbank
  Treating as single cross-section gives wrong answer (different velocities, n values)
```

---

## Regime Theory and Channel Classification

```
CHANNEL CLASSIFICATION (Rosgen, 1996 — commonly used in US):

  STREAM TYPE:   A    B    C    D    DA   E    F    G
  Pattern:       steep gorge → moderately entrenched → alluvial meandering
  Entrenchment:  deeply entrenched (confined) → slightly entrenched (floodplain access)
  Width/Depth:   low (A,G) → high (D,C,E)
  Sinuosity:     1.0–1.2 (A,B) → 1.2–1.5 (C) → >1.5 (E)
  Gradient:      steep (A,G) → very gentle (E,DA)

  SINGLE-THREAD STABLE: B, C, E — channel in regime with floodplain
  BRAIDED (D): multiple channels, highly unstable, high bedload transport
  ANASTOMOSING (DA): multiple stable channels in low-energy wetland
  INCISING (G): vertical/lateral instability, deeply cut

LANE'S BALANCE (1955):
  Q_s × D_50 ∝ Q × S

  Q_s = sediment supply (load)
  D_50 = median grain size
  Q = water discharge
  S = channel slope

  If any factor changes, channel adjusts the others to restore balance.
  EXAMPLE:
    Dam upstream (↓Q_s, ↓Q): channel ERODES downstream (↓D_50 + ↓S) → incision
    Land use change (↑Q, same Q_s): channel erodes → ↑S, ↑D_50 → "channel evolution"

CHANNEL EVOLUTION MODEL (CEM):
  Stage I:  Pre-disturbance stable channel
  Stage II: Incision (degradation) — triggered by base-level lowering or discharge increase
  Stage III: Widening — bank failures, channel widening
  Stage IV: Aggradation (sediment refill) — wider but shallower
  Stage V:  Quasi-equilibrium — new stable state (different W, D than Stage I)
  Often takes 50–100 years to complete cycle
```

---

## River Meandering

```
MEANDER MECHANICS:

  SINUOSITY: S_i = channel length / valley length
  Straight: S_i = 1.0; Meandering: S_i > 1.5; Braided: multiple channels

  WHY RIVERS MEANDER:
    Not fully solved theoretically. Key contributions:
    1. Helical secondary flow in bends: centrifugal force pushes surface water
       to outer bank, bed material transported to inner bank (point bar)
    2. Perturbation amplification: slight irregularity → helical flow → erosion
       at outer bank → more pronounced bend → more helical flow → positive feedback
    3. Threshold: only rivers below a critical stream power meander
       (high energy → braiding, very low energy → straight or anastomosing)

  MEANDER WAVELENGTH:
    λ ≈ 10–14 × W (channel wavelength ≈ 10× channel width)
    This relationship is remarkably consistent across rivers spanning 5 orders of magnitude in size
    Same ratio holds for meanders in glaciers (subglacial channels) and tidal channels
    Suggests universal fluid-boundary interaction physics

  MEANDER MIGRATION:
    Outer bank: erosion (bank undercutting, mass failure)
    Inner bank: deposition (point bar — spiral flow moves sediment)
    Net: downstream migration + lateral expansion
    Rate: 1–100 m/yr depending on bank composition and discharge

OXBOW LAKE FORMATION:
  Meander amplifies → neck narrows → flood event cuts through neck → new straight channel
  Old meander loop isolated → oxbow lake (crescent-shaped)
  Oxbow eventually fills with sediment → marsh → dry land

BRAIDED RIVERS:
  High bedload transport, non-cohesive banks
  Multiple channels separated by bars
  Instability: channels shift continuously
  Typical: glacial outwash plains (Canterbury Plains, NZ), semi-arid rivers,
           rivers with high seasonal discharge variation
```

---

## Sediment Transport

### Sediment Characterization

```
GRAIN SIZE CLASSIFICATION:
  Boulders: > 256 mm
  Cobbles:  64–256 mm
  Gravel:   2–64 mm (pebbles, coarse gravel)
  Sand:     0.0625–2 mm (fine, medium, coarse)
  Silt:     0.004–0.0625 mm
  Clay:     < 0.004 mm

  D_50 = median grain size
  D_84, D_90 = coarser percentiles (used for roughness, critical shear stress)
  Gradation coefficient σ_g = (D_84/D_16)^0.5 → 1.0 = uniform, >3 = poorly sorted

MODES OF TRANSPORT:
  Bedload: grains rolling/sliding/saltating along bed
    Dominant for gravel, coarse sand
    Difficult to measure (sampler intrudes on flow)

  Suspended load: fine sediment (silt, clay, fine sand) carried in water column
    Easier to measure (water samples, turbidity sensors)
    Typically 90%+ of total transport by mass in lowland rivers

  Wash load: very fine clay/silt that stays in suspension indefinitely
    Not related to bed composition
    Set by supply (erosion rate in watershed), not transport capacity
    Doesn't deposit except in low-velocity zones (reservoirs, floodplains)

RATING CURVE:
  Q_s = a Q^b  (sediment discharge vs. water discharge)
  b typically 1.5–2.5 (sediment transport is highly nonlinear in Q)
  → 10× flow increase → 30–300× sediment transport
  This is why floods do most of the geomorphic work
  (1% of time, 50% of total sediment transport in many rivers)
```

### Bedload Transport — Shields Criterion

```
SHIELDS CRITERION (critical shear stress for bedload initiation):

  τ* = τ / [(ρ_s - ρ_w) g D]    (dimensionless shear stress)
  τ = ρ_w g R S                 (bed shear stress)

  Motion begins when τ* > τ*_c ≈ 0.03–0.06 (varies with grain Reynolds number)

  PHYSICAL INTERPRETATION:
    τ = drag force per unit bed area (fluid pushing grains)
    (ρ_s - ρ_w) g D = submerged weight of grain per unit area
    Critical ratio: drag/weight exceeds threshold → grain moves

  PRACTICAL: critical flow depth for bedload motion
    D_c = τ*_c × (ρ_s - ρ_w) × D / (ρ_w × S)
    For D_50 = 50 mm gravel, S = 0.002:
    D_c ≈ 0.05 × 1.65 × 0.05 / (1000 × 0.002) ≈ 0.21 m
    → Need depth > 21 cm to move this gravel

BEDLOAD TRANSPORT EQUATIONS:
  Meyer-Peter Müller (1948):
    q_s = 8(τ* - 0.047)^1.5 × [(ρ_s - ρ_w)/ρ_w]^0.5 × D^1.5

  Engelund-Hansen:
    q_s = 0.05 V^2 × V / (g × (ρ_s/ρ_w - 1)² × D_50)

  All bedload formulas have ±100–200% uncertainty — field conditions dominate.
```

---

## Floodplains

```
FLOODPLAIN FORMATION:
  TWO MECHANISMS work together:
  1. Lateral accretion: point bar deposition as meander migrates
     → Epsilon cross-bedding: inclined layers recording lateral bar growth
  2. Vertical accretion: overbank deposition during flood events
     → Fine silt and clay layers settling from floodwater
     → Rates: 0.5–5 mm/yr in actively aggrading floodplains

FLOODPLAIN STRATIGRAPHY:
  ┌───────────────────────────────────┐  ← flood levee (coarsest overbank)
  │  Vertical accretion (fine)        │  ← overbank silt/clay
  ├───────────────────────────────────┤
  │  Point bar (fining-upward)        │  ← lateral accretion (coarse to fine)
  ├───────────────────────────────────┤
  │  Basal gravel lag                 │  ← scour lag (coarsest)
  └───────────────────────────────────┘
  This "fining-upward sequence" is a diagnostic signature of meandering river deposits
  Preserved in rock record → paleofluvial facies analysis

FLOODPLAIN INUNDATION:
  1% AEP (100-year) flood extent mapped by:
    FEMA NFIP (National Flood Insurance Program): regulatory standard
    Hydraulic model: HEC-RAS 1D or 2D (river flow + floodplain routing)
    Input: bathymetry/LiDAR DEM + Manning's n + flow boundary condition

  HEC-RAS 2D:
    Shallow water equations (St. Venant): full 2D momentum + continuity
    Grid cells 1–100 m resolution
    Solves ∂h/∂t + ∇·(hV) = 0 (continuity) + momentum (gravity + friction + inertia)
    Can incorporate buildings, levees, culverts as boundary conditions
```

---

## Bridges from CS and Engineering

```
RIVER/FLOODPLAIN CONCEPT      CS / ENGINEERING EQUIVALENT
──────────────────────────────────────────────────────────────────────────────
Manning equation              Empirical transport law (Ohm's law for open channels)
  Q = (1/n) A R^{2/3} S^{1/2}  → Q ∝ conductance × driving force
  n (roughness)                 → resistance in a conduit; 1/n = conductance
  Hydraulic radius R            → "effective diameter" for non-circular pipes
  Manning ↔ Darcy-Weisbach      → same structure; different parameterization

Muskingum flood routing       Discrete-time IIR filter
  Q(t) = C0·I(t) + C1·I(t-1) + C2·Q(t-1)
  C0 + C1 + C2 = 1             → coefficients sum to 1 (bounded-input stable)
  K parameter (travel time)    → group delay through reach
  x parameter (0 to 0.5)       → damping: x=0 is maximally attenuating (level
                                   pool); x=0.5 is pure translation (wave passes
                                   through undistorted)
  Saint-Venant ↔ PDE routing   → moving from discrete filter to continuous PDE
                                   (Muskingum is the linearized finite-difference
                                   approximation)

Lane's balance                Constraint equilibrium / invariant
  Q_s × D₅₀ ∝ Q_w × S         → sediment supply × grain size ∝ water power × slope
  Disturb one term              → system adjusts others to restore balance
  Channelization doubles slope  → shear stress doubles → incision → re-meandering
  Equivalent to: coupled ODEs  → stability analysis around equilibrium point

Hydraulic geometry scaling    Power-law self-similarity
  W ~ Q^b, D ~ Q^f, V ~ Q^m   → log-log linear (same as Zipf, Moore's law)
  b + f + m = 1                → conservation constraint on exponents

River meandering              Emergent pattern from convective instability
  Secondary helical flow       → positive feedback loop: bend → erosion → deeper
                                   bend → stronger secondary flow → more erosion
  Meander cutoff               → cycle reset: abrupt discontinuity in channel path
  Chaos analogy                → sensitive to initial perturbation of channel

HEC-RAS 1D/2D routing        PDE solver (Saint-Venant equations)
  Continuity + momentum PDEs   → conservation laws discretized on channel mesh
  1D: centerline cross-sections → one spatial dimension, lateral homogeneity assumed
  2D: full 2D shallow water    → finite volume / finite element on triangulated mesh
  Timestep stability (CFL)     → Courant number constraint (same as any wave solver)
```

## Flood Routing

```
MUSKINGUM METHOD (hydrological routing):
  Route flood wave downstream through channel reach
  Q(t) = C_0 I(t) + C_1 I(t-1) + C_2 Q(t-1)

  I = inflow, Q = outflow
  C_0, C_1, C_2 = routing coefficients (function of K, x parameters)
  K = travel time through reach, x = weighting factor (0 = level pool, 0.5 = translating wave)

  Simple, efficient — widely used for ungauged reaches
  Limitation: doesn't account for backwater effects, cannot represent 2D flow

HYDRAULIC ROUTING (HEC-RAS):
  1D: solves Saint-Venant equations along channel centerline
    ∂A/∂t + ∂Q/∂x = 0                           (continuity)
    ∂Q/∂t + ∂(Q²/A)/∂x + gA(∂h/∂x + S_f) = 0  (momentum)
    where S_f = friction slope = n²Q²/(A²R^4/3) (Manning friction)

  Dynamic wave: full equation — includes inertia terms
  Diffusion wave: drop inertia — good for slowly varying flows
  Kinematic wave: drop both inertia and pressure — good for upland routing

  2D: HEC-RAS 2D, MIKE FLOOD, TUFLOW — full 2D shallow water equations
    Required for floodplains with complex flow paths, bridges, culverts
```

---

## River Restoration Principles

```
NATURAL CHANNEL DESIGN:
  Goal: restore channel to stable reference condition
  Method: match dimensions to regional hydraulic geometry curves
    → W, D, S, meander wavelength, radius of curvature
    → From reference reaches (similar Q, geology, vegetation)

  COMMON FAILURES:
    Over-engineered: hard revetments prevent natural adjustment
    Under-designed: channel too small → instant incision
    Ignoring sediment supply: restored channel will fill or incise
    Short reach fix: upstream/downstream problems propagate in

WOOD IN RIVERS:
  Large wood (logs) in streams:
    Creates pools (scour), stores sediment, provides habitat complexity
    Historical clearing of rivers → lost habitat structure
    Reintroduction: controversial (debris concerns downstream) but effective
  Beaver dams: similar hydraulics to wood jams
    Raise water table, store water, create wetlands
    "Beaver dam analogs" (BDAs) used in restoration

FLOODPLAIN RECONNECTION:
  Entrenched (incised) channels: water doesn't reach floodplain
  Fix: grade control structures (riffles) to arrest incision
       or strategic overbank spillways to reconnect flow
  Benefit: groundwater recharge, floodplain deposition, ecological function
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Manning equation purpose | Calculate steady uniform discharge given channel geometry, slope, roughness |
| What is bankfull discharge? | Discharge filling channel to top without overflowing; ~1.5-yr return interval; channel-forming Q |
| Why do rivers meander? | Secondary helical flow in bends → outer bank erosion + inner bar accretion → amplifying perturbation |
| What is Lane's balance? | Q_s × D ∝ Q × S; disturbing any factor causes channel adjustment to restore balance |
| What is bedload vs. suspended load? | Bedload: grains rolling on bed; suspended load: fine sediment carried in water column |
| Shields criterion? | Critical dimensionless shear stress τ* ≈ 0.047 for grain motion; drag/weight threshold |
| What is fluvial fining-upward sequence? | Point bar deposit: coarse gravel base → fining sand toward top; diagnostic meandering river deposit |
| What is Muskingum routing? | Simple hydrological method to route flood hydrograph downstream; weighted inflow-outflow formula |

---

## Common Confusion Points

**Manning's n is empirical, not physically derived**: n values come from matching observed flows to formula predictions for specific channel types. There's no rigorous theory predicting n from grain size and channel geometry alone (though Strickler's formula K_s ≈ D_90^(1/6) approximates for gravel beds). Always treat published n values as starting estimates requiring calibration.

**Bankfull discharge ≈ 1.5-year flood, not 2-year**: The 1.5-year return period (67% exceedance probability per year) is an AVERAGE for US streams. It ranges from 1-year to 5-year in different climatic regions. Semi-arid streams tend toward 2–5-year bankfull; humid streams 1–2-year. Don't assume 2-year = bankfull without checking regional calibration.

**River sinuosity responds to valley slope, not just discharge**: A river with slope 0.005 (valley) that meanders at sinuosity 2.0 has channel slope 0.0025. If you channelize it (straighten → sinuosity 1.0), the channel slope doubles. → shear stress doubles → erosion increases → river re-meananders to lower slope. Channelization creates a continuous cycle of erosion and remeandering unless maintained.

**Sediment transport equations have huge uncertainty**: Factor of 2–10 errors are common comparing different bedload transport equations applied to the same site. The physical complexity (grain shapes, hiding and exposure effects, bed armoring, sand-gravel transition) is poorly captured by analytical formulas. Always use multiple equations and field calibration.

**Floodplains are part of the river system, not just adjacent land**: The floodplain is where the river naturally stores water during floods, deposits sediment, and exchanges nutrients. A river without floodplain access (leveed) has higher and faster flood peaks, less habitat, and exports rather than stores sediment. Separating rivers from floodplains (for development) fundamentally changes river function.
