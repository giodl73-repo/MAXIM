# 02 — Fluid Mechanics

## Flow Behavior, Navier-Stokes, Pipe & External Flow

```
FLUID MECHANICS HIERARCHY
          │
          ▼
┌─────────────────────────────────────────────────────────────┐
│                   FLUID STATICS                              │
│    p = p₀ + ρgh   (hydrostatics, buoyancy)                  │
├─────────────────────────────────────────────────────────────┤
│                  FLUID KINEMATICS                            │
│    streamlines, continuity, RTT, vorticity                  │
├─────────────────────────────────────────────────────────────┤
│                  FLUID DYNAMICS                              │
│    Euler equations (inviscid)                                │
│    Navier-Stokes (viscous)                                   │
│    Bernoulli (simplified)                                    │
├──────────────────────────┬──────────────────────────────────┤
│   INTERNAL FLOW          │   EXTERNAL FLOW                  │
│   pipe, duct, channel    │   airfoils, bluff bodies         │
│   laminar/turbulent      │   boundary layers, drag/lift     │
├──────────────────────────┴──────────────────────────────────┤
│   COMPRESSIBLE FLOW   (Ma > 0.3)                            │
│   isentropic nozzles, shocks, choked flow                   │
├─────────────────────────────────────────────────────────────┤
│   TURBOMACHINERY                                             │
│   pumps, compressors, turbines, fans                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Fluid Properties

| Property | Symbol | Units | Physical meaning |
|----------|--------|-------|-----------------|
| Density | ρ | kg/m³ | Mass per volume |
| Dynamic viscosity | μ | Pa·s | Resistance to shear |
| Kinematic viscosity | ν = μ/ρ | m²/s | Momentum diffusivity |
| Pressure | p | Pa | Normal force per area |
| Bulk modulus | B = −V(dp/dV) | Pa | Resistance to compression |
| Surface tension | σ | N/m | Energy per area at interface |

**Newton's law of viscosity:** τ = μ(du/dy)  [shear stress proportional to velocity gradient]
Newtonian fluids: μ constant. Non-Newtonian: shear-thinning (blood, paint), shear-thickening (cornstarch), Bingham plastic (toothpaste, yield stress).

**Water at 20°C:** ρ = 998 kg/m³, μ = 1.002×10⁻³ Pa·s, ν = 1.004×10⁻⁶ m²/s
**Air at 20°C, 1 atm:** ρ = 1.204 kg/m³, μ = 1.81×10⁻⁵ Pa·s, ν = 1.51×10⁻⁵ m²/s

---

## Fluid Statics

```
Pressure increases with depth:
  dp/dz = −ρg    →    p = p_atm + ρgz  (incompressible)

Hydrostatic force on a vertical flat surface:
  F = ρg ȳ A    (acts at pressure center, below centroid)

Buoyancy (Archimedes):
  F_b = ρ_fluid g V_submerged
  Floats if ρ_object < ρ_fluid (or displaced fluid weight > object weight)
```

**Pascal's principle:** Pressure applied to a confined fluid transmits undiminished throughout.
Hydraulic press: F₂/F₁ = A₂/A₁ (mechanical advantage from area ratio).

**Manometry:** U-tube manometer: Δp = ρgh. Differential manometer for pressure difference.

---

## Reynolds Transport Theorem (RTT)

Bridge between **Lagrangian** (follow the fluid particle) and **Eulerian** (fixed control volume) descriptions.

```
d/dt ∫_system η dm = ∂/∂t ∫_CV η ρ dV + ∮_CS η ρ (v·n̂) dA

where η = any intensive property (1 → mass, v → momentum, e → energy)
```

Applying RTT to mass → **continuity equation:**
```
∂ρ/∂t + ∇·(ρv) = 0    (general, compressible)
∇·v = 0                 (incompressible: ρ = const)
ṁ = ρ₁A₁v₁ = ρ₂A₂v₂   (steady, 1D channel flow)
```

---

## Navier-Stokes Equations

The governing equations for Newtonian, incompressible flow:

```
Continuity:
  ∇·v = 0

Momentum (vector equation — one per component):
  ρ(∂v/∂t + v·∇v) = −∇p + μ∇²v + ρg
                              ↑           ↑
                         viscous       body
                          term         force

Written out in x:
  ρ(∂u/∂t + u∂u/∂x + v∂u/∂y + w∂u/∂z)
    = −∂p/∂x + μ(∂²u/∂x² + ∂²u/∂y² + ∂²u/∂z²) + ρgₓ
```

The N-S equations are **nonlinear** (the v·∇v term). This nonlinearity is why turbulence is hard.
Exact analytical solutions exist only for simple geometries (Couette, Poiseuille, Stokes flow).
All else: approximations (boundary layer theory, potential flow) or CFD.
<!-- @editor[bridge/P2]: No bridge from N-S simplification hierarchy → PDE approximation strategies. This learner has numerical methods context; the connection from "nonlinear PDE with no closed form" → "boundary layer as singular perturbation" → "potential flow as inviscid limit" → "RANS as time-averaged closure" maps directly onto the approximation-hierarchy thinking they use for numerical methods. -->

**Euler equations** = N-S with μ=0 (inviscid). Applicable far from boundaries.

---

## Bernoulli Equation

Derived from Euler equations along a streamline (inviscid, steady, incompressible):
```
p + ½ρv² + ρgz = const  (along streamline)

Modified Bernoulli (with losses and work):
  p₁ + ½ρv₁² + ρgz₁ + ρgh_pump = p₂ + ½ρv₂² + ρgz₂ + ρgh_loss
```

Each term has units of pressure (Pa) or equivalently J/m³:
- p: static pressure (flow work)
- ½ρv²: dynamic pressure (kinetic energy)
- ρgz: hydrostatic pressure (potential energy)

**Pitot tube:** p_stagnation − p_static = ½ρv²  →  v = √(2Δp/ρ)
**Venturi meter:** continuity + Bernoulli → Q = A₂√(2Δp/(ρ(1−(A₂/A₁)²)))

---

## Dimensional Analysis — Buckingham Π Theorem

Physical laws must be dimensionally homogeneous. If a problem has n variables and k fundamental dimensions, there are n−k dimensionless Π groups.

**Key dimensionless groups:**
```
Reynolds:   Re = ρvL/μ = vL/ν     (inertia / viscous forces)
Mach:       Ma = v/a               (velocity / sound speed)
Froude:     Fr = v/√(gL)           (inertia / gravity) — open channel flows
Euler:      Eu = Δp/(ρv²)         (pressure / inertia)
Strouhal:   St = fL/v             (oscillation / mean flow)
Weber:      We = ρv²L/σ           (inertia / surface tension)
```

**Model testing:** Achieve geometric + dynamic similarity by matching all relevant Π groups.
Full-size ship → scale model in towing tank: match Froude number for wave resistance, Reynolds for friction drag (can't match both simultaneously → fundamental problem in ship testing).

---

## Internal Flow — Pipe and Duct

### Laminar vs Turbulent

```
Re = ρvD/μ (pipe, D = diameter)

Re < 2300:   Laminar (Hagen-Poiseuille)
2300–4000:   Transition (unstable)
Re > 4000:   Turbulent

Fully developed laminar pipe flow:
  u(r) = (R²−r²)/(4μ) × (−dp/dx)      ← parabolic profile
  V_avg = R²/(8μ) × (−dp/dx)           ← Hagen-Poiseuille
  Δp/L = 128μQ/(πD⁴)                   ← Q = flow rate
  f_Darcy = 64/Re                       ← friction factor (Fanning f = 16/Re)
```

### Moody Chart & Darcy-Weisbach

**Darcy-Weisbach equation** (head loss in pipe):
```
h_L = f × (L/D) × (v²/2g)

f = friction factor from Moody chart:
  Laminar:   f = 64/Re
  Turbulent: Colebrook equation (implicit):
    1/√f = −2.0 log(ε/(3.7D) + 2.51/(Re√f))
  Explicit approx (Swamee-Jain):
    f = 0.25/[log(ε/(3.7D) + 5.74/Re^0.9)]²
```

**Relative roughness** ε/D: commercial steel ε=0.046 mm, cast iron ε=0.26 mm, drawn tubing ε=0.0015 mm.

**Minor losses:** h_m = K(v²/2g)  where K = loss coefficient for fittings (elbow: 0.3–1.5, valve: 0.1–10).

### Pipe Networks

Analogous to resistor networks:
- Series pipes: same flow rate, sum head losses: h_total = Σh_i
- Parallel pipes: same head loss, sum flow rates: Q_total = ΣQ_i
- Loop (Hardy-Cross method): iterative correction until flow continuity satisfied

**Analogy to electrical circuits:**
Δp ↔ Voltage, Q ↔ Current, Hydraulic resistance R = h/Q ↔ Electrical resistance

---

## External Flow — Boundary Layers & Drag

### Flat Plate Boundary Layer

```
Leading    Laminar       Transition    Turbulent
edge   →   BL            zone          BL
       →   δ(x) ~ x^0.5             δ(x) ~ x^0.8
       →   Re_x = ρv∞x/μ
       →   Transition at Re_x ≈ 5×10⁵

Blasius solution (laminar, exact):
  δ/x = 5/√Re_x           (BL thickness)
  C_f = 0.664/√Re_x       (local skin friction)
  C_D = 1.328/√Re_L       (drag coefficient, flat plate)
```

### Drag on Bluff Bodies

```
F_drag = C_D × ½ρv² × A_ref

C_D values (approximate):
  Sphere:              0.47
  Cylinder (2D):       1.2
  Streamlined body:    0.04
  Flat plate (⊥):      1.17
  Car (typical):       0.25–0.35
  Truck:               0.6–0.8

Drag crisis: C_D drops sharply at Re ≈ 5×10⁵ for sphere/cylinder
  (laminar → turbulent BL → delayed separation → smaller wake)
  Why golf balls have dimples: force turbulent BL → lower drag
```

**Lift:**
```
F_lift = C_L × ½ρv² × A_wing

Kutta-Joukowski theorem: L = ρv∞Γ  (lift per unit span = density × velocity × circulation)
Circulation Γ = ∮ v·dl  (line integral around airfoil)
```

---

## Compressible Flow (Ma > 0.3)

**Speed of sound:**
```
a = √(γRT/M) = √(γp/ρ)   (ideal gas)
Air at 20°C: a ≈ 343 m/s
```

**Mach number regimes:**
```
Ma < 0.3:   Incompressible (density variation < 5%)
0.3–0.8:    Subsonic compressible
0.8–1.2:    Transonic (shocks on airfoil)
1.2–5:      Supersonic
Ma > 5:     Hypersonic (real gas effects, dissociation)
```

**Isentropic relations** (stagnation = zero-velocity reference):
```
T₀/T = 1 + (γ-1)/2 × Ma²
p₀/p = (1 + (γ-1)/2 × Ma²)^(γ/(γ-1))
ρ₀/ρ = (1 + (γ-1)/2 × Ma²)^(1/(γ-1))
```

**Choked flow:** When Ma=1 at throat (nozzle minimum area), mass flow is maximum.
Cannot increase ṁ by lowering downstream pressure below critical.
Critical for rocket nozzles, flow measurement, and safety valves.

**Normal shock relations** (Ma₁ > 1 enters, Ma₂ < 1 exits):
```
Ma₂² = [(γ-1)Ma₁² + 2] / [2γMa₁² − (γ-1)]
p₂/p₁ = [2γMa₁² − (γ-1)] / (γ+1)
```
Total pressure drops across a shock (irreversible). Strong shocks: pressure ratio 10:1 or more.

---

## Turbomachinery

### Euler Turbomachinery Equation

```
Ẇ_shaft / ṁ = U₂Vθ₂ − U₁Vθ₁

where:
  U = blade speed = ωr
  Vθ = tangential component of absolute velocity
  Subscripts 1,2 = inlet, outlet

Pump: work input = U₂Vθ₂ − U₁Vθ₁  (fluid gains angular momentum)
Turbine: work output = U₁Vθ₁ − U₂Vθ₂  (fluid loses angular momentum)
```

### Pump Similarity Laws (Affinity Laws)

For geometrically similar pumps at same efficiency point:
```
Q ∝ ND³         (flow scales with speed × diameter³)
H ∝ N²D²        (head scales with speed² × diameter²)
P ∝ N³D⁵        (power scales with speed³ × diameter⁵)
```

**Specific speed** classifies pump type:
- Low N_s: centrifugal (radial), high head, low flow
- Medium N_s: mixed flow
- High N_s: axial (propeller), low head, high flow

---

## CFD — The Discretized Navier-Stokes

```
Method          Approach                    Typical use
──────────────────────────────────────────────────────────────
FVM (Finite     Integral conservation on    OpenFOAM, Fluent,
Volume)         cell faces                  Star-CCM+. Industry standard.

FEM (Finite     Weak form, shape functions  COMSOL, LS-DYNA.
Element)        on elements                 Good for FSI (fluid-structure).

LBM (Lattice    Kinetic theory,             PowerFLOW. Fast for complex
Boltzmann)      stream-collide on lattice   geometry and moving boundaries.

DNS (Direct     Resolve all scales,         Research only. Needs Re^(9/4)
Numerical Sim)  Re < 10,000 feasible        grid points.

LES (Large Eddy Filter large scales,        Turbomachinery, combustion.
Simulation)     model sub-grid              10–100× more expensive than RANS.

RANS (Reynolds  Time-average + turbulence   Everyday CFD. k-ε, k-ω SST
Averaged N-S)   model (k-ε, k-ω, etc.)     models. 90% of industry work.
```

<!-- @editor[bridge/P2]: Turbulence closure problem is stated but the connection to underdetermined linear systems and regularization is missing. This learner immediately recognizes "more unknowns than equations" as an ill-posed system — a k-ε model is a regularization strategy, just as RANS itself is a model-order reduction from DNS. Framing it that way would give the engineering intuition for why different closure models give different results. -->
**Turbulence closure problem:** Time-averaging N-S introduces Reynolds stress tensor with 6 new unknowns but no new equations. Every turbulence model is a different closure assumption.

---

## Open Channel Flow

Flow with a free surface (rivers, canals, storm sewers).

**Manning equation** (empirical, turbulent):
```
Q = (1/n) A R_h^(2/3) S^(1/2)
where n = Manning roughness coefficient (0.012 concrete, 0.025 natural channel)
      R_h = hydraulic radius = A/P (area/wetted perimeter)
      S = channel slope
```

**Froude number:** Fr = v/√(gD_h)
- Fr < 1: subcritical (tranquil) — downstream control
- Fr > 1: supercritical (rapid) — upstream control
- Fr = 1: critical flow (maximum discharge for given energy)

**Hydraulic jump:** Supercritical → subcritical transition with large energy dissipation.
Used in spillways to protect downstream structures from erosion.

---

## Common Confusion Points

**Streamline vs pathline vs streakline:** In steady flow, all three coincide. In unsteady flow:
- Streamline: everywhere tangent to v at time t (instantaneous snapshot)
- Pathline: trajectory of a particular fluid particle over time
- Streakline: locus of all particles that passed a fixed point (smoke visualization)

**Bernoulli application gotchas:**
- Only along a streamline (unless irrotational flow → then everywhere in flow field)
- Not across streamlines in rotational flow
- Not applicable across shocks, or with significant viscous losses
- The "high velocity → low pressure" intuition is consequence, not cause of lift

**Laminar vs turbulent pressure drop:** Laminar: Δp ∝ Q¹ (linear). Turbulent: Δp ∝ Q^1.75–2 (much steeper). Doubling flow rate in turbulent pipe roughly quadruples pressure drop.

**Gauge vs absolute pressure:** p_abs = p_gauge + p_atm. N-S and Bernoulli use absolute pressure, but gauge pressure is often used for pipe flow calculations (consistent Δp).

**No-slip condition:** Fluid velocity at a solid wall equals wall velocity. Leads to velocity gradient → viscous stress → boundary layer. Without it: d'Alembert's paradox (zero drag for any streamlined body in inviscid flow).

---

## Decision Cheat Sheet

| Problem type | Approach | Key equation/tool |
|-------------|---------|-----------------|
| Static fluid forces | Hydrostatics | p = ρgh, F = ρgȳA |
| Pipe flow, pressure drop | Darcy-Weisbach | h_L = f(L/D)(v²/2g) |
| Turbulent friction factor | Moody chart | Colebrook equation |
| Incompressible flow balance | Bernoulli + continuity | p + ½ρv² + ρgz = C |
| Drag force on body | C_D correlation | F = C_D × ½ρv² × A |
| Compressible nozzle | Isentropic relations | p₀/p = f(Ma, γ) |
| Pump design/scaling | Affinity laws | Q∝ND³, H∝N²D² |
| Flow regime | Reynolds number | Re = ρvL/μ vs 2300/4000 |
| Open channel discharge | Manning equation | Q = (1/n)AR_h^(2/3)S^(1/2) |
