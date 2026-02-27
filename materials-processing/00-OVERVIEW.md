# Materials Processing — Landscape and Taxonomy

## The Big Picture

Materials processing is the set of methods that control material structure — from atomic-scale phase distribution to macroscopic grain flow — to achieve target mechanical, thermal, and surface properties. It bridges materials science (what atoms do) and manufacturing (what machines do).

```
MATERIALS PROCESSING MAP
──────────────────────────────────────────────────────────────────
RAW MATERIAL                PROCESSING                TARGET PROPERTY
─────────────────────────────────────────────────────────────────
                        ┌─────────────────────┐
                        │  THERMAL PROCESSING  │
                        │  (change microstructure)│
  Metal →               │  Heat treatment      │→  Hardness
  Powder →              │  Annealing           │→  Toughness
  Polymer →             │  Quenching/Tempering │→  Ductility
  Ceramic →             └─────────────────────┘→  Strength
                        ┌─────────────────────┐
                        │  MECHANICAL DEFORM.  │
                        │  (change grain flow) │→  Yield strength
                        │  Rolling, forging    │→  Fatigue life
                        │  Drawing, extrusion  │→  Surface hardness
                        └─────────────────────┘
                        ┌─────────────────────┐
                        │  SOLIDIFICATION      │
                        │  (control as-cast    │→  Porosity level
                        │   microstructure)    │→  Grain size
                        │  Casting metallurgy  │→  Composition
                        └─────────────────────┘
                        ┌─────────────────────┐
                        │  SURFACE TREATMENT   │
                        │  (modify surface     │→  Wear resistance
                        │   only, not bulk)    │→  Corrosion resist.
                        │  PVD, CVD, Nitriding │→  Fatigue life
                        └─────────────────────┘
                        ┌─────────────────────┐
                        │  POWDER PROCESSING   │
                        │  (from powder to     │→  Controlled pore
                        │   dense solid)       │→  Complex geometry
                        │  Pressing, Sintering │→  Near-net shape
                        └─────────────────────┘
```

---

## The Microstructure–Property Relationship

Every processing decision ultimately manipulates microstructure, which determines properties.

```
PROCESSING → MICROSTRUCTURE → PROPERTIES
──────────────────────────────────────────────────────────────────
Processing controls:
  Phase presence:     what phases are present (α, β, martensite)
  Phase fraction:     how much of each phase
  Grain size:         fine grains → higher strength, lower ductility
  Grain orientation:  texture → anisotropic properties
  Defects:            dislocations, vacancies, grain boundaries
  Composition:        local alloy chemistry (segregation)
  Second phases:      precipitates, carbides, inclusions

Microstructure determines:
  Yield strength:     resistance to plastic deformation onset
  UTS:                maximum stress before fracture
  Ductility:          elongation to fracture
  Hardness:           resistance to indentation
  Toughness:          energy to fracture (K_IC, Charpy)
  Fatigue strength:   cyclic stress endurance limit
  Creep resistance:   resistance to slow deformation at temperature
  Wear resistance:    surface hardness + toughness balance
  Corrosion resist.:  surface chemistry, passive layer stability
```

---

## The Phase Diagram as Process Map

```
IRON-CARBON PHASE DIAGRAM (simplified)
──────────────────────────────────────────────────────────────────
Temperature (°C)
1538 ─────── Liquid
1495 ─── δ-iron + Liquid
1400 ─────────────────────────────────────────── Liquid
         δ iron     │
1200 ─── γ (austenite) + Liquid
                    │  Eutectic point
1153 ─────────────────────────────────── γ + Liquid + Fe₃C
         γ (austenite, FCC)
  912 ─── α+γ ─────────────────────────── γ + Fe₃C (cementite)
                    │ Eutectoid (0.76% C)
  723 ─────────────────────────────────── α+Fe₃C (pearlite)
         α (ferrite, BCC) + Fe₃C (cementite)

0%C (pure iron)  0.76% C  1.2%  2%      4.3%  6.7%C
                 Eutectoid                Eutectic

Steels: < 2% C   Ductile iron: 2.5–4% C   Cast iron: > 2% C

HEAT TREATMENT is about controlling which phases form and when.
  Fast cool from austenite → martensite (hard, brittle)
  Slow cool → pearlite/ferrite (soft, ductile)
  Controlled cool → controlled hardness
```

---

## The Processing Triangle

```
MATERIALS PROCESSING DECISION TRIANGLE
──────────────────────────────────────────────────────────────────
                     PROPERTY
                   (what you need)
                       ▲
                      / \
                     /   \
                    /     \
                   /       \
          PROCESSING ─────── MICROSTRUCTURE
         (what you do)     (what forms)

Cannot specify any two corners without affecting the third.

Example: I need tensile strength of 1500 MPa in steel
  Microstructure: 95% martensite, tempered at 200°C
  Processing: quench and temper — austenitize at 850°C,
              oil quench, temper at 200°C for 1 hour

Example: I need a ductile steel (35% elongation)
  Microstructure: ferrite + pearlite, coarse grain
  Processing: full anneal — slow cool in furnace from ~900°C
```

---

## Materials Classes and Their Processing

| Material Class | Primary Processing Methods | Key Properties Controlled |
|----------------|---------------------------|--------------------------|
| Carbon steel | Heat treatment, forging, rolling | Hardness, strength, toughness |
| Alloy steel (4140, 4340) | Heat treatment (Q&T), carburizing | High strength, wear resist. |
| Stainless steel | Annealing, cold work, solution treat | Corrosion + strength balance |
| Aluminum alloys | Solution treat + age hardening | Precipitation hardening |
| Titanium alloys | Alpha-beta processing, aging | STA → highest strength |
| Ni superalloys | STA, directional solidification | High-temp creep resistance |
| Polymers | Extrusion, molding, crosslinking | Stiffness, toughness, HDT |
| Ceramics | Sintering, HIP | Density, hardness, toughness |
| Composites | Cure cycle, fiber architecture | Stiffness/strength direction |

---

## Key Concepts

### Temperature–Time as the Fundamental Control Variable

```
THERMAL PROCESSING CONTROL
──────────────────────────────────────────────────────────────────
Heat treatment = controlled thermal cycle:
  Heating rate → affects residual stress, cracking risk
  Soak temperature → phase transformation, solubility
  Soak time → diffusion distance, homogeneity
  Cooling rate → determines which phases form
  Tempering → reduce brittleness of martensite

Rate of phase transformation depends on:
  Driving force (ΔG = departure from equilibrium)
  Diffusion rate (D = D₀ × exp(-Q/RT))
  Nucleation sites (grain boundaries, inclusions)

TTT and CCT diagrams map this:
  Time-Temperature-Transformation (isothermal hold)
  Continuous Cooling Transformation (constant cooling rate)
  Both show: start/finish curves for each transformation

A TTT diagram is a finite state machine. States: austenite (initial), pearlite,
bainite, martensite (terminal states). Transitions: triggered by (temperature,
time) pairs crossing transformation start/finish boundaries. Reading a TTT
diagram = reading a state transition map: given current state (austenite at T),
which states are reachable and at what holding time? The "nose" is the
fastest transition path. Temperature selects which transition is active.
```

### Diffusion and Its Implications

```
FICK'S FIRST LAW:
  J = -D × (dC/dx)    flux proportional to concentration gradient

FICK'S SECOND LAW:
  ∂C/∂t = D × ∂²C/∂x²  transient diffusion

ARRHENIUS TEMPERATURE DEPENDENCE:
  D = D₀ × exp(-Q/RT)
  Q = activation energy (J/mol)
  R = gas constant (8.314 J/mol·K)
  T = absolute temperature (Kelvin)

Implication: doubling soak temperature is NOT the same as
  doubling soak time. Temperature has exponential effect.

Example: Carburizing steel at 950°C vs 900°C
  Case depth ~ √(D × t)
  D(950°C)/D(900°C) ≈ exp(-Q/R × (1/1223 - 1/1173))
  ≈ 1.5× faster diffusion at 950°C
  → Get same case depth in 67% of the time
```

---

## Directory Guide

| File | Content |
|------|---------|
| 01-PHASE-TRANSFORMATIONS.md | TTT/CCT diagrams, Fe-C system, transformation mechanisms |
| 02-HEAT-TREATMENT.md | Annealing, normalizing, quenching, tempering, case hardening |
| 03-SOLIDIFICATION.md | Nucleation, grain growth, casting defects, segregation |
| 04-DEFORMATION.md | Plastic deformation, dislocations, work hardening, dynamic recovery |
| 05-FRACTURE-MECHANICS.md | Griffith criterion, K_IC, fatigue crack growth, Paris law |
| 06-SURFACE-TREATMENT.md | PVD, CVD, nitriding, carburizing, anodizing, thermal spray |
| 07-POWDER-PROCESSING.md | Powder metallurgy, HIP, MIM, SPS, sintering theory |
| 08-POLYMERS-PROCESSING.md | Extrusion, injection molding, thermosets, crystallinity |
| 09-CHARACTERIZATION.md | XRD, SEM/TEM, hardness testing, tensile test, Charpy |

---

## Decision Cheat Sheet

| I need... | Process |
|-----------|---------|
| Maximum hardness in steel | Quench (martensite) |
| Relieve residual stress without strength loss | Stress relief anneal |
| Soften steel for machining | Full anneal or spheroidize anneal |
| High surface hardness, tough core | Carburize + quench, or induction harden |
| Age-hardenable aluminum at maximum strength | Solution treat + age (T6 or T73 temper) |
| Titanium at maximum strength | Solution treat + age (STA) |
| Steel wire at high strength (springs) | Cold drawing (work hardening) |
| Reduce porosity in PM part | HIP (Hot Isostatic Pressing) |
| Near-net metal parts without tooling | Powder metallurgy or MIM |

---

## Common Confusion Points

**Phase diagram shows equilibrium; processing is non-equilibrium**: The iron-carbon phase diagram tells you what phases are stable at each temperature and composition. Actual processing occurs off-equilibrium — martensite forms because austenite is quenched too fast for equilibrium transformation. TTT/CCT diagrams map this non-equilibrium reality.

**Heat treatment of aluminum vs steel is fundamentally different**: Steel hardening is a quench-martensite mechanism (diffusionless transformation). Aluminum hardening is precipitation hardening (requires controlled aging — a diffusional process). Same vocabulary ("heat treatment," "temper," "T6") but completely different metallurgy.

**Processing history matters**: A part's current microstructure depends on ALL prior processing — casting, hot work, cold work, heat treatment, welding. Reversing one step often means redoing subsequent steps. Process sequencing is a constraint often violated by design changes.

**Surface treatment changes are not free**: Adding a PVD coating, carburizing case, or anodize layer changes part dimensions (typically 1–25 µm), surface roughness, and sometimes residual stress state. Final machining must precede or follow treatment depending on the process. Design tolerances must account for coating thickness.
