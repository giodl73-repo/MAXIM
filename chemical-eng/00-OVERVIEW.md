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

| ChE Concept | Software/Architecture Analogy |
|------------|-------------------------------|
| Batch reactor | MapReduce / batch processing: all data processed together, then output |
| CSTR (continuous stirred) | Perfectly mixed message queue: every item sees the same processing state |
| PFR (plug flow) | Streaming pipeline: each item processed in sequence, no mixing |
| Distillation (staged separation) | Staged sorting algorithm: each tray is a comparison/partition step |
| Reflux ratio | Re-examination passes: more passes = higher purity, lower throughput |
| PID control loop | Software rate limiter / autoscaler: P=proportional, I=cumulative, D=predictive |
| Integral windup in PID | Queue accumulation under sustained overload — same anti-windup logic |
| HAZOP guide words | Chaos engineering fault categories: NO=drop, MORE=overload, REVERSE=deadlock |
| Material balance (recycle) | Graph with feedback loops (same convergence challenges) |
| Process simulation (ASPEN) | ODE/algebraic system solving: same sparse Newton methods |
| Pinch analysis | Optimization under linear constraints |

---

## Decision Cheat Sheet

| Design question | Use this | Because |
|----------------|----------|---------|
| Reactor: liquid-phase, flexible, small batch | Batch reactor | Easy cleanup between products; handles variable demand |
| Reactor: continuous, well-mixed, liquid | CSTR | Simple control; good for autocatalytic or highly exothermic (heat removal easier) |
| Reactor: continuous, gas-phase, high conversion | PFR (tubular) | Higher conversion per volume for positive-order kinetics |
| Separation: components differ in boiling point | Distillation | Workhorse; α > 1.05 required; most mature technology |
| Separation: components form azeotrope | Extractive distillation or liquid-liquid extraction | Azeotrope breaks the volatility-based approach |
| Separation: heat-sensitive products (pharma, food) | Membrane or vacuum distillation | Avoids thermal degradation |
| Separation: dilute solute from large volume | Adsorption (PSA, TSA) or absorption | Efficient at low concentrations |
| Flowsheet documentation: early design | PFD (Process Flow Diagram) | Shows major equipment, streams, mass/energy balances |
| Flowsheet documentation: construction/ops | P&ID (Piping & Instrumentation Diagram) | Shows every valve, instrument, interlock — the construction blueprint |
| Control: fast process variable (flow) | PI controller (tight tuning) | Fast dynamics; D-action unnecessary |
| Control: slow process variable (composition) | Cascade: fast inner + slow outer loop | Compensates for analyzer delay |
| Safety review: systematic hazard identification | HAZOP with full team | Structured, auditable, covers all failure modes per guide word |

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

---

## Common Confusion Points

**Thermodynamic equilibrium ≠ kinetics.** Equilibrium (K_eq) tells you the maximum possible conversion at given T and P. Kinetics tells you how fast you get there. A catalyst changes the rate (kinetics) but never the equilibrium position. You cannot beat equilibrium by adding more catalyst — only by changing conditions (T, P) or removing products.

**Space time ≠ residence time.** Space time τ = V/v₀ uses the inlet volumetric flow. Mean residence time t̄ = V/v uses the actual volumetric flow at reactor conditions. They are equal only for constant-density systems (most liquids). For gas-phase reactions where moles change, τ ≠ t̄.

**HAZOP is not a checklist.** It is a structured, team-based, node-by-node deviation analysis. The guide words (NO, MORE, LESS, REVERSE...) are applied systematically to every process variable at every node. A pre-filled checklist misses the whole point: the value comes from the team discussion, not the form.

**Separation costs dominate.** In most chemical plants, 40-80% of capital and operating cost is in separations, not reactions. Choosing the right separation method (distillation vs extraction vs membrane) is often the most consequential design decision.

**Steady state ≠ equilibrium.** A CSTR at steady state has constant concentrations, but the reaction is continuously running — it is NOT at chemical equilibrium (except at complete conversion). Equilibrium is a thermodynamic concept; steady state is a mass-balance concept.
