# Fluid Dynamics — Landscape and Taxonomy

## The Big Picture

Fluid dynamics describes the motion of liquids and gases. It is one of the oldest and richest fields of applied mathematics, and it contains some of the deepest unsolved problems in science — most famously, the Clay Millennium Prize for the Navier-Stokes existence and smoothness problem. Reynolds number is the single most important dimensionless parameter in the field: it separates laminar from turbulent flow, simple from complex behavior, analytically tractable from computationally intractable.

```
FLUID DYNAMICS — FULL LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  GOVERNING PRINCIPLE: Conservation laws + constitutive relations
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Conservation of mass:      ∂ρ/∂t + ∇·(ρ**v**) = 0                │
  │  Conservation of momentum:  ρ D**v**/Dt = −∇p + μ∇²**v** + ρ**g** │
  │  Conservation of energy:    ρ D(e)/Dt = −p∇·**v** + ∇·(k∇T) + Φ  │
  └──────────────────────────────────────────────────────────────────────┘

  FLOW REGIMES (by Reynolds number Re = ρUL/μ = UL/ν)
  ┌────────────────────────────────────────────────────────────────────┐
  │  Re << 1    Stokes flow (viscosity dominates, reversible)          │
  │  Re ~ 1     Transitional (viscosity and inertia comparable)        │
  │  Re ~ 10³   Laminar boundary layer; steady organized flow          │
  │  Re ~ 10⁵   Transition to turbulence in boundary layers            │
  │  Re >> 10⁶  Fully turbulent; Kolmogorov cascade; chaotic          │
  └────────────────────────────────────────────────────────────────────┘

  COMPRESSIBILITY (by Mach number M = U/c)
  ┌───────────────┬──────────────────────────────────────────────────┐
  │  M < 0.3      │ Incompressible (density changes < 5%)            │
  │  0.3 < M < 1  │ Subsonic compressible                           │
  │  M = 1        │ Transonic (shock formation)                      │
  │  M > 1        │ Supersonic; oblique shocks                       │
  │  M >> 1       │ Hypersonic; chemical dissociation, ionization     │
  └───────────────┴──────────────────────────────────────────────────┘

  VISCOSITY (ideal vs real)
  ┌───────────────┬──────────────────────────────────────────────────┐
  │  Inviscid     │ μ = 0; Euler equations; no boundary layers       │
  │               │ Holomorphic complex potential; exact solutions   │
  │  Newtonian    │ μ = const; Navier-Stokes; most common fluids     │
  │  Non-Newtonian│ μ = μ(strain rate); polymers, blood, paints      │
  └───────────────┴──────────────────────────────────────────────────┘
```

---

## The Ten Files at a Glance

```
FILE                      CORE CONTENT
─────────────────────────────────────────────────────────────────────────
00-OVERVIEW               This file — landscape, taxonomy, key parameters
01-CONTINUUM-MECHANICS    Strain, stress, material derivative, conservation laws
02-INVISCID-FLOW          Euler equations, Bernoulli, potential flow, circulation
03-VISCOUS-FLOW           Navier-Stokes, Stokes flow, pipe flow, exact solutions
04-BOUNDARY-LAYERS        Prandtl theory, Blasius, separation, transition
05-TURBULENCE             Reynolds averaging, Kolmogorov cascade, models, spectra
06-COMPRESSIBLE-FLOW      Shocks, expansion fans, normal/oblique shocks, de Laval
07-AERODYNAMICS           Airfoil theory, lift, drag, wing theory, Prandtl's LLT
08-HYDRODYNAMICS          Free surfaces, waves, hydraulics, geophysical flows
09-CFD                    Discretization, FVM, FEM, spectral; turbulence models
```

---

## The Most Important Parameters

### Reynolds Number (the master parameter)

    Re = ρUL/μ = UL/ν

where:
- ρ = density, U = characteristic velocity, L = characteristic length
- μ = dynamic viscosity, ν = kinematic viscosity = μ/ρ

Physical meaning: inertia forces / viscous forces.

```
Re VALUES FOR FAMILIAR FLOWS:
  Blood in capillary:        Re ~ 0.001   (Stokes flow, reversible)
  Swimming bacterium:        Re ~ 0.0001  (viscosity utterly dominates)
  Pipe flow (laminar):       Re < 2300
  Pipe flow (turbulent):     Re > 4000
  Aircraft wing (cruise):    Re ~ 10⁷    (thin turbulent boundary layer)
  Hurricane (200km diameter): Re ~ 10¹⁰
```

### Other Key Dimensionless Groups

| Number | Formula | Physical Meaning |
|--------|---------|-----------------|
| Re (Reynolds) | ρUL/μ | Inertia/viscosity |
| Ma (Mach) | U/c | Flow speed/sound speed |
| Fr (Froude) | U/√(gL) | Inertia/gravity (free surfaces) |
| Ro (Rossby) | U/(fL) | Inertia/Coriolis (geophysical) |
| We (Weber) | ρU²L/σ | Inertia/surface tension |
| Pr (Prandtl) | ν/κ | Momentum/thermal diffusivity |
| Pe (Péclet) | UL/κ | Advection/diffusion |
| Gr (Grashof) | gβΔTL³/ν² | Buoyancy-driven convection |

---

## The Navier-Stokes Equations — The Central Object

For incompressible Newtonian flow:

```
NAVIER-STOKES:
  ∂**v**/∂t + (**v**·∇)**v** = −(1/ρ)∇p + ν∇²**v** + **g**
  ∇·**v** = 0  (incompressibility)

  ──────────────────────────────────────────
  ∂**v**/∂t    = local acceleration (∂/∂t holding position fixed)
  (**v**·∇)**v** = convective acceleration (inertia: v carries itself)
  −(1/ρ)∇p    = pressure gradient force
  ν∇²**v**    = viscous diffusion (viscosity smooths velocity gradients)
  **g**        = body force (gravity, Coriolis, electromagnetic...)
  ──────────────────────────────────────────
  The hard term: (**v**·∇)**v** — nonlinear, couples all components
                 This is why turbulence is hard
```

The **Clay Millennium Problem**: Do smooth solutions to the incompressible 3D Navier-Stokes equations always exist for smooth initial data? Or can solutions develop singularities (blow up) in finite time? $1M prize. Unsolved as of 2026.

---

## Fluid Types and Constitutive Relations

```
FLUID TAXONOMY:
  Newtonian fluids:      τ = μ (∂u/∂y)    (shear stress ∝ shear rate)
  Examples: air, water, oils, most simple fluids

  Non-Newtonian fluids:  τ = μ(γ̇) · γ̇   (viscosity depends on strain rate)
  ─ Shear-thinning (pseudoplastic): μ↓ as γ̇↑   (ketchup, blood)
  ─ Shear-thickening (dilatant):   μ↑ as γ̇↑   (cornstarch/water)
  ─ Bingham plastic: needs yield stress τ₀ before flowing (toothpaste)
  ─ Viscoelastic: both viscous and elastic behavior (polymers)

  Gas vs Liquid:
  ─ Gas: compressible (ρ varies), low μ, Mach number matters
  ─ Liquid: nearly incompressible, higher μ, Mach ~ 0
```

---

## Field Connections

### Fluid Dynamics ↔ Mathematics

| Fluid Concept | Mathematical Tool |
|--------------|-----------------|
| Incompressible inviscid 2D | Complex analysis (holomorphic W(z)) |
| Navier-Stokes weak form | Functional analysis, Sobolev spaces |
| Turbulence statistics | Stochastic PDEs, Fourier analysis |
| Vortex dynamics | Geometric mechanics, symplectic structure |
| Shock waves | Hyperbolic conservation laws |
| Boundary layers | Asymptotic methods, matched asymptotics |

### Fluid Dynamics ↔ Engineering / Azure Analogy

A useful analogy from distributed systems engineering: fluid flow is like network traffic flow.

```
FLUID FLOWS       ↔      NETWORK/DATA FLOWS
────────────────────────────────────────────
Viscous resistance  ↔  Network latency / bandwidth limit
Reynolds number     ↔  Traffic load ratio
Laminar flow        ↔  Ordered, predictable packet flow
Turbulence          ↔  Chaotic, unpredictable congestion
Boundary layer      ↔  Rate-limiting near slow nodes
Shock wave          ↔  Sudden congestion collapse
Bernoulli           ↔  Bandwidth conservation (continuity)
```

This is informal but useful for intuition about Reynolds-number-like transitions in complex systems.

---

## Historical Perspective

| Era | Key Advance |
|----|------------|
| 1738 | Bernoulli: energy conservation in flows |
| 1757 | Euler: inviscid equations |
| 1822 | Navier: viscosity added to Euler equations |
| 1845 | Stokes: rigorous derivation of N-S |
| 1883 | Osborne Reynolds: turbulence criterion (Re), dye experiment |
| 1904 | Prandtl: boundary layer theory |
| 1941 | Kolmogorov: turbulence cascade and K41 scaling |
| 1963 | Lorenz: chaotic ODEs (related to convection) |
| 1965+ | CFD develops as numerical field (FVM, FEM) |
| 2000 | N-S Clay Millennium Problem posed |

---

## Decision Cheat Sheet

| Question | First step |
|---------|-----------|
| Is viscosity important? | Compute Re. If Re >> 1, boundary layers thin; bulk ≈ inviscid |
| Is compressibility important? | Compute Ma. If Ma < 0.3, treat as incompressible |
| Is the flow turbulent? | Re > 4000 (pipe), > 5×10⁵ (flat plate), > ~10⁵ (free shear) |
| Can I solve it analytically? | Inviscid (complex potential) or Stokes (Re<<1) or fully symmetric |
| Need to model it numerically? | Choose CFD: FVM for conservation, LES/DNS for turbulence |
| Gravity waves? Surface effects? | Froude number Fr = U/√(gL) |
| Rotating frame? | Rossby number Ro = U/(fL); small Ro → strong Coriolis |

---

## Common Confusion Points

**Velocity is a vector field, not a particle trajectory**: The Eulerian velocity field **v**(x,t) describes the velocity at each spatial point at time t. Particle trajectories (Lagrangian) are obtained by integrating dx/dt = **v**(x(t),t). These are different objects — streamlines (Eulerian) ≠ pathlines (Lagrangian) in unsteady flow.

**"Incompressible" ≠ constant density in all contexts**: Incompressibility means ∇·**v** = 0, which implies Dρ/Dt = 0 (density of each fluid parcel is constant). This does NOT mean the density field is uniform — a stratified fluid can be incompressible with varying ρ(x,y,z).

**Reynolds number depends on length scale**: Pipe flow and boundary layer flow have different transition Reynolds numbers because the relevant length scales differ. Re is always computed with the appropriate characteristic length for the problem.

**The Millennium Problem is about smooth solutions, not just existence**: The question is whether smooth initial data leads to smooth solutions for all future time. Weak solutions (distributional) exist — the open question is whether they remain classical (smooth).
