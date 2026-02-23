# Mechanical Engineering — Landscape & Field Taxonomy

## The Big Picture

Mechanical engineering is the discipline of **energy, matter, and motion** — how energy converts
between forms, how fluids and solids behave under load, and how machines are designed to last.
It underlies every physical system: power plants, aircraft engines, automotive drivetrains, HVAC
systems, manufacturing equipment, and the thermal management of your server racks.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    MECHANICAL ENGINEERING STACK                          │
├─────────────────────────────────────────────────────────────────────────┤
│  ENERGY SCIENCE                                                          │
│  ┌────────────────────┐  ┌────────────────────┐                         │
│  │   THERMODYNAMICS   │  │   HEAT TRANSFER     │                         │
│  │  entropy, cycles,  │  │  conduction,        │                         │
│  │  exergy, combustion│  │  convection,        │                         │
│  └────────────────────┘  │  radiation, HX      │                         │
│                           └────────────────────┘                         │
├─────────────────────────────────────────────────────────────────────────┤
│  CONTINUUM MECHANICS                                                      │
│  ┌────────────────────┐  ┌────────────────────┐                         │
│  │  FLUID MECHANICS   │  │  SOLID MECHANICS   │                         │
│  │  Navier-Stokes,    │  │  stress/strain,    │                         │
│  │  pipe/external/    │  │  failure, fatigue, │                         │
│  │  compressible,     │  │  FEA               │                         │
│  │  turbomachinery    │  └────────────────────┘                         │
│  └────────────────────┘                                                  │
├─────────────────────────────────────────────────────────────────────────┤
│  DESIGN & MANUFACTURING                                                   │
│  ┌────────────────────┐  ┌────────────────────┐                         │
│  │  MACHINE DESIGN    │  │  MANUFACTURING     │                         │
│  │  gears, bearings,  │  │  machining, casting│                         │
│  │  shafts, springs,  │  │  forming, welding, │                         │
│  │  fasteners         │  │  AM, tolerances    │                         │
│  └────────────────────┘  └────────────────────┘                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Module Map

| Module | Core Topic | Key Equations | Real-World Anchor |
|--------|-----------|---------------|-------------------|
| `01-THERMODYNAMICS` | Energy conversion, cycles | dU=δQ−δW, η=1−Tc/Th | Steam turbines, gas turbines, refrigerators |
| `02-FLUID-MECHANICS` | Flow behavior | Navier-Stokes, Bernoulli | Pipe networks, aircraft, pumps |
| `03-HEAT-TRANSFER` | Heat flow modes | Fourier, Newton cooling, S-B | Heat exchangers, fins, GPU cooling |
| `04-MACHINE-DESIGN` | Stress, fatigue, elements | von Mises, Goodman, Hertz | Gears, shafts, bearings, bolts |
| `05-MANUFACTURING` | Making parts | Tolerances, GD&T | CNC machining, casting, AM |

---

## Governing Equations — The Short List

```
THERMODYNAMICS               FLUID MECHANICS               SOLID MECHANICS
─────────────────            ─────────────────             ─────────────────
First law:                   Continuity:                   Hooke's law:
  dU = δQ − δW                ∂ρ/∂t + ∇·(ρv) = 0           σ = Eε

Second law:                  Navier-Stokes:                Equilibrium:
  dS ≥ δQ/T                   ρ(∂v/∂t + v·∇v) =            ∇·σ + f = 0
                               −∇p + μ∇²v + ρg
Ideal gas:                                                 von Mises:
  pV = nRT                   Bernoulli:                      σ_vm = √(σ₁²+σ₂²-σ₁σ₂)
                               p + ½ρv² + ρgz = const
Carnot limit:
  η_max = 1 − Tc/Th          Reynolds number:
                               Re = ρvL/μ
```

---

## Dimensionless Numbers — The Universal Language

| Number | Formula | Meaning | Domain |
|--------|---------|---------|--------|
| Reynolds (Re) | ρvL/μ | Inertia/viscous | Fluid flow transition |
| Mach (Ma) | v/a | Flow/sound speed | Compressible flow |
| Nusselt (Nu) | hL/k | Conv/cond heat transfer | Forced convection |
| Prandtl (Pr) | c_p μ/k | Momentum/thermal diffusivity | Heat transfer |
| Grashof (Gr) | gβΔTL³/ν² | Buoyancy/viscous | Natural convection |
| Fourier (Fo) | αt/L² | Thermal diffusion time | Transient conduction |
| Strouhal (St) | fL/v | Oscillation frequency | Vortex shedding |
| Weber (We) | ρv²L/σ | Inertia/surface tension | Droplets, sprays |
| Damköhler (Da) | τ_flow/τ_rxn | Transport/reaction | Combustion, reactors |

---

## The Four Fundamental Laws of Thermodynamics

```
ZEROTH LAW: If A≡B and B≡C thermally, then A≡C → temperature as property

FIRST LAW:  Energy is conserved
            dU = δQ − δW       (closed system)
            ṁΔh + ΔKE + ΔPE = Q̇ − Ẇ   (steady-flow open system)

SECOND LAW: Entropy of isolated system ≥ 0
            dS_universe ≥ 0   (equality only for reversible)

THIRD LAW:  S → 0 as T → 0 K  (perfect crystal)
            → absolute entropy reference exists
```

---

## Continuum Hypothesis

All of ME rests on treating matter as a **continuous field**, not discrete atoms.
Valid when Knudsen number Kn = λ/L ≪ 1, where λ = mean free path.

- Air at STP: λ ≈ 68 nm → continuum valid down to ~1 μm features
- Micro/nano flows (MEMS): Kn > 0.01 → need slip conditions or DSMC
- Plasma: Debye length, not continuum → see physics/06-MHD.md

---

## Connections to Computing

| ME Concept | CS/Software Analog |
|-----------|-------------------|
| Finite Element Analysis (FEA) | Sparse linear system solve (Kx = F) |
| Computational Fluid Dynamics (CFD) | PDE discretization on mesh → same numerics as PDEs in 19-NUMERICAL-METHODS.md |
| Control systems (PID) | Feedback loops in software → see control-theory/ |
| Thermal management of data centers | HVAC + heat transfer: same equations |
| Manufacturing tolerances | Floating-point rounding analogies |
| Fatigue life prediction | Reliability models, survival analysis |
| Turbulence modeling | Chaos → same mathematics as chaotic ODEs |

---

## Decision Guide — Which Module?

```
WHAT'S YOUR QUESTION?
        │
        ├─ Energy conversion, efficiency, what's the maximum work?
        │   └─► 01-THERMODYNAMICS
        │
        ├─ How does fluid flow — pressures, velocities, pipe networks?
        │   └─► 02-FLUID-MECHANICS
        │
        ├─ How much heat moves and how fast?
        │   └─► 03-HEAT-TRANSFER
        │
        ├─ Will this part fail? How long will it last? What size shaft?
        │   └─► 04-MACHINE-DESIGN
        │
        └─ How is it made? Tolerances, processes, quality?
            └─► 05-MANUFACTURING
```
