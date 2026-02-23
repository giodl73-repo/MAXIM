# Chemical Engineering — Landscape & Field Taxonomy

## The Big Picture

Chemical engineering is the discipline of **transforming raw materials into useful products at scale**.
The distinguishing word is *scale*: a chemist makes 1 gram in a lab; a chemical engineer makes
100,000 tons per year safely and economically. The field sits at the intersection of chemistry,
physics, mathematics, and economics.

```
RAW MATERIALS
      │
      ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  THERMODYNAMICS                                                          │
│  What is possible? Energy/equilibrium constraints, phase behavior        │
├─────────────────────────────────────────────────────────────────────────┤
│  TRANSPORT PHENOMENA (Bird-Stewart-Lightfoot)                            │
│  How fast? Momentum (flow), energy (heat), mass (diffusion) — unified   │
├─────────────────────────────────────────────────────────────────────────┤
│  REACTION ENGINEERING                                                    │
│  How does chemistry happen at scale? Kinetics, reactor design            │
├─────────────────────────────────────────────────────────────────────────┤
│  SEPARATIONS                                                             │
│  How do we get pure products? Distillation, absorption, membranes        │
├─────────────────────────────────────────────────────────────────────────┤
│  PROCESS DESIGN & SAFETY                                                 │
│  Integration: flowsheets, economics, control, HAZOP                     │
└─────────────────────────────────────────────────────────────────────────┘
        │
        ▼
   USEFUL PRODUCTS at scale: fuels, plastics, drugs, fertilizers, chips
```

---

## Module Map

| Module | Core Topic | Governing Equations | Example Systems |
|--------|-----------|--------------------|-----------------|
| `01-THERMO` | Phase equilibrium, EOS | Gibbs phase rule, VLE | Distillation, flash drums |
| `02-REACTION-ENGINEERING` | Kinetics, reactor design | CSTR/PFR design equations | Ammonia synthesis, polymerization |
| `03-TRANSPORT` | Momentum/heat/mass transfer | N-S, Fourier, Fick, analogies | Packed beds, heat exchangers |
| `04-SEPARATIONS` | Unit ops for separation | McCabe-Thiele, NTU/HTU | Distillation columns, membranes |
| `05-PROCESS-DESIGN` | Flowsheets, control, safety | Pinch, PID, HAZOP | Full plant design |

---

## The BSL Unification: Transport Phenomena

One of chemical engineering's distinctive contributions: recognizing that momentum, heat, and mass transfer are mathematically identical:

```
TRANSFER TYPE   DRIVING FORCE    TRANSPORT LAW        DIFFUSIVITY
──────────────────────────────────────────────────────────────────────
Momentum        Velocity grad.   Newton's law         ν = μ/ρ  [m²/s]
                τ = −μ dv/dy

Heat            Temp. gradient   Fourier's law        α = k/(ρcp) [m²/s]
                q = −k dT/dz

Mass            Conc. gradient   Fick's first law     D_AB [m²/s]
                J_A = −D_AB dC_A/dz
```

**The Reynolds analogy:** In turbulent flow, Nusselt, Sherwood, and friction factor correlate.
This lets you estimate heat transfer from mass transfer data (and vice versa) — powerful.

---

## Key Dimensionless Groups in ChE

| Number | Formula | Meaning |
|--------|---------|---------|
| Reynolds (Re) | ρvD/μ | Inertia/viscous |
| Prandtl (Pr) | c_p μ/k = ν/α | Momentum/thermal diffusivity |
| Schmidt (Sc) | ν/D_AB | Momentum/mass diffusivity |
| Nusselt (Nu) | hL/k | Convective/conductive heat |
| Sherwood (Sh) | k_c L/D_AB | Convective/diffusive mass |
| Lewis (Le) | α/D_AB = Sc/Pr | Thermal/mass diffusivity |
| Damköhler (Da) | τ_flow/τ_rxn | Residence time/reaction time |
| Thiele (φ) | L√(k/D_eff) | Reaction/diffusion in catalyst |

**Analogies:**
- Nu = f(Re, Pr) ↔ Sh = f(Re, Sc) (exactly parallel correlations)
- Chilton-Colburn: j_H = j_D = f/2 (turbulent pipe flow) → heat-mass-momentum

---

## Connection to Computing / Data Systems

| ChE Concept | Software/Data Analogy |
|------------|----------------------|
| Material balance (recycle) | Graph with feedback loops (same convergence challenges) |
| Process simulation (ASPEN) | ODE/algebraic system solving: same sparse Newton methods |
| Reactor design (PFR) | Integration of ODE: same as scipy.integrate.solve_ivp |
| CSTR steady state | Nonlinear algebraic equation: same as Newton-Raphson |
| Flash calculation (Rachford-Rice) | Root-finding problem: same bisection/Brent |
| Pinch analysis | Optimization under linear constraints |
| HAZOP | Systematic failure mode analysis (like FMEA) |
| Process control (PID) | See control-theory/ |

---

## Decision Guide

```
WHAT'S YOUR ChE QUESTION?
        │
        ├─ What phase/composition at equilibrium?
        │   └─► 01-THERMO (VLE, flash, EOS)
        │
        ├─ How fast is the reaction? What reactor type/size?
        │   └─► 02-REACTION-ENGINEERING
        │
        ├─ How does transport limit the process?
        │   └─► 03-TRANSPORT
        │
        ├─ How do we purify the product?
        │   └─► 04-SEPARATIONS
        │
        └─ How do we design/operate/control the whole plant safely?
            └─► 05-PROCESS-DESIGN
```
