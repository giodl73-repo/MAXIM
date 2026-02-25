# Phase Transformations and TTT/CCT Diagrams

## The Big Picture

Phase transformations in metals occur when the thermodynamic driving force (free energy difference between phases) exceeds the activation energy barrier. The rate at which transformations occur — controlled by temperature and time — determines the final microstructure and thus all mechanical properties.

```
TRANSFORMATION FUNDAMENTALS
──────────────────────────────────────────────────────────────────
            Austenite (γ, FCC, stable above A1)
            cooling
               │
               ▼
  ┌────────────┬────────────┬──────────────────┐
  │            │            │                  │
  Slow         Moderate     Fast               Very fast
  cool         cool         cool               quench
  │            │            │                  │
  ▼            ▼            ▼                  ▼
Pearlite +  Bainite +   Martensite +       Martensite
Ferrite     Ferrite     small amount        (pure)
(soft,      (intermediate) of retained     (hard,
 ductile)               austenite          brittle)

Hardness:   ~200 HV     ~400 HV           ~600–800 HV
```

---

## The Iron-Carbon System in Detail

### Key Temperatures (Equilibrium, 1 atm)

```
KEY TEMPERATURES (approximate for plain carbon steel)
──────────────────────────────────────────────────────────────────
1538°C  Melting point of pure iron
1495°C  Peritectic (δ-Fe + liquid → γ)
1153°C  Eutectic temperature (γ ↔ iron + cementite ledeburite)
 912°C  A3 — γ↔α+γ boundary (for hypoeutectoid steels, varies with %C)
 723°C  A1 — eutectoid temperature (pearlite ↔ austenite)
         Always 723°C for Fe-C binary (0.76 wt% C = eutectoid)
         Alloys shift: Ni, Mn lower A1; Cr, Mo, V, W raise A1
 200–    Martensite start (Ms) and finish (Mf) temperatures
 -100°C  Depend strongly on carbon and alloying content

AC1, AC3: temperatures on HEATING (higher than equilibrium, rate-dependent)
Ar1, Ar3: temperatures on COOLING (lower than equilibrium, rate-dependent)
Ac = chauffage (heating), Ar = refroidissement (cooling)
```

### The Eutectoid Reaction

```
PEARLITE FORMATION (eutectoid reaction)
──────────────────────────────────────────────────────────────────
At 723°C:   γ (0.76%C) ──slow cool──► α (0.02%C) + Fe₃C (6.67%C)
            austenite                   ferrite      cementite

Pearlite = lamellar structure of alternating α + Fe₃C plates
  Spacing (lamellar spacing) decreases with higher undercooling
  Finer pearlite = harder (more phase boundary area)

Coarse pearlite (small undercooling, high temperature):
  Forms just below 723°C (650–700°C range)
  Soft (~200 HV), ductile

Fine pearlite (larger undercooling):
  Forms at lower temperatures (500–650°C)
  Harder (~300 HV), less ductile

Upper bainite (350–550°C):
  Feathery ferrite laths with carbide between laths
  Mixed properties

Lower bainite (200–350°C):
  Acicular ferrite with fine carbide within laths
  Higher hardness than upper bainite, good toughness
```

### Martensite Formation

```
MARTENSITE: DIFFUSIONLESS TRANSFORMATION
──────────────────────────────────────────────────────────────────
At fast quench rate (below Ms temperature):
  Austenite cannot transform to equilibrium phases (pearlite/bainite)
  Carbon atoms "trapped" in BCC iron → BCT (body-centered tetragonal)
  No diffusion: carbon stays where it was
  Volume expansion (~4%) → compressive surface stress

Ms temperature (approximate): depends on %C and alloying
  Ms(°C) ≈ 539 − 423(%C) − 30.4(%Mn) − 17.7(%Ni) − 12.1(%Cr) − 7.5(%Mo)

  For 1080 steel (~0.8%C): Ms ≈ 539 − 423×0.8 = 201°C
  For 4340 steel (~0.4%C, ~1.7%Ni, ~0.8%Cr, ~0.25%Mo):
    Ms ≈ 539 − 170 − 52 − 14 − 2 ≈ 301°C

Martensite hardness: primarily controlled by %C
  ~0.2%C → ~300 HV
  ~0.4%C → ~500 HV
  ~0.6%C → ~650 HV
  ~0.8%C → ~750 HV (approaching maximum ~850 HV)
  Above ~0.6%C: excess retained austenite appears
```

---

## TTT Diagrams (Time-Temperature-Transformation)

### Isothermal TTT Diagram Structure

```
TTT DIAGRAM (0.8% C eutectoid steel)
──────────────────────────────────────────────────────────────────
T(°C)
800 ─ A3 ─────────────────────────────────────
        Austenite stable
723 ─ A1 ─────────────────────────────────────
650 ─         ╲  (nose)
              ┌────────────────────┐
600 ─      ╔══╝                    ╚═══════════
           ║  Pearlite                        ║
500 ─      ║  ─────────────────               ║ Bainite
           ╚═══════════════╗                  ║
400 ─                      ║Bainite start     ║
                           ║                  ║
300 ─ Ms ──────────────────║──────────────────╬──────
                           ║                  ║
200 ─ Mf ─                 ╚══════════════════╝
                            Transformation
100 ─                        complete
      │
      └──────────────────────────────────────────► log t(s)
      0.1s  1s   10s  100s  1000s  10000s

Reading: For isothermal hold at temperature T:
  Left curve = transformation start (1%)
  Right curve = transformation finish (99%)
  Below Ms: martensite forms on cooling (no time axis)
```

### Using TTT for Isothermal Heat Treatment

```
AUSTEMPERING (isothermal at bainite nose):
  Austenitize at 850°C
  Quench rapidly to 350°C (above Ms)
  Hold isothermally → bainite forms (30–60 min)
  Air cool to room temperature

Result: Bainite → tough, hard (400–500 HV), no quench cracks
        (no martensite → less distortion, no temper needed)
        Best for springs, gears, hand tools

MARTEMPERING (quench to just above Ms, then air cool):
  Austenitize at 850°C
  Quench to just above Ms (e.g., 220°C for 1080 steel)
  Equalize temperature throughout part
  Air cool through Ms → uniform martensite transformation

Result: Martensite with reduced thermal gradient → less distortion
        Must still temper to reduce brittleness
        Best for: dies, precision tools, large cross-sections
```

---

## CCT Diagrams (Continuous Cooling Transformation)

### CCT vs TTT

```
CCT DIAGRAM (Continuous Cooling)
──────────────────────────────────────────────────────────────────
Real heat treatment ≠ isothermal hold.
Parts are cooled continuously (water quench, oil quench, air cool).
CCT maps transformation under CONTINUOUS COOLING conditions.

CCT diagram features:
  Transformation curves shifted right + down vs TTT
  (more time, lower temperature needed for same transformation
   because cooling rate is passing through, not sitting at temp)

  Different cooling rates plotted as lines through the diagram:
  Line A (very fast: water quench): only martensite
  Line B (fast: oil quench): martensite + small bainite
  Line C (moderate: forced air): bainite + pearlite mix
  Line D (slow: furnace): ferrite + pearlite only

Critical cooling rate:
  Fastest cooling rate that misses the pearlite nose entirely
  → Fully martensitic structure
  Alloy steel (4340) has much slower critical cooling rate than
  plain carbon steel → can be quenched in oil (not water) → less distortion
```

### Hardenability and the Jominy Test

```
HARDENABILITY
──────────────────────────────────────────────────────────────────
Hardenability = ability of steel to harden to martensite through
  its cross-section (NOT maximum hardness achievable).

Controlled by: alloying elements that shift TTT nose to right
  (slow transformation → gives time for martensite to form)
  Mn, Cr, Mo, Ni, V all increase hardenability

Jominy End-Quench Test (ASTM A255):
  Standardized round bar, one end quenched with water
  Hardness measured at intervals from quenched end

  ┌─────────────────────────────────────────────┐
  │ Bar cross-section                           │
  │ ←─────── decreasing cooling rate ─────────►│
  │                                             │
  │ Hardness vs. distance from quenched end     │
  │                                             │
  │  H  ─────╲                                  │
  │  a         ╲                                │
  │  r          ╲─────────────────────────────  │
  │  d                                          │
  │       Distance from quenched end            │
  └─────────────────────────────────────────────┘

  Steep drop: low hardenability (plain carbon steel)
  Flat line:  high hardenability (alloy steel like 4340)
  → 4340 hardens fully even at 50mm from quench end
  → 1080 hardens only 5mm from quench end
```

---

## Transformation Mechanisms

### Nucleation and Growth

```
NUCLEATION THEORY IN PHASE TRANSFORMATIONS
──────────────────────────────────────────────────────────────────
ΔG_total = -ΔG_v × V + γ × A    (nucleus formation energy balance)
  ΔG_v = free energy per unit volume (driving force, decreases with T↓)
  γ = interfacial energy (always positive cost)
  V = volume, A = surface area

Critical radius r*:
  r* = 2γ / ΔG_v
  Nuclei smaller than r* dissolve back (no free energy benefit)
  Nuclei larger than r* grow spontaneously

Homogeneous nucleation (within perfect crystal):
  Very high ΔG* barrier
  Rarely occurs in practice (supercooling required)

Heterogeneous nucleation (at grain boundaries, inclusions, surfaces):
  Reduced surface energy at existing boundaries
  Lower ΔG* → nucleation at small undercooling
  Always dominates in real materials

Effect of temperature:
  Closer to A1: low ΔG_v (small driving force), slow nucleation
  Far below A1: high ΔG_v (fast nucleation), but slower diffusion
  Pearlite nose = maximum transformation rate (optimum T)
```

### Precipitation Hardening Mechanism

```
PRECIPITATION SEQUENCE (Al-Cu example, 2XXX series)
──────────────────────────────────────────────────────────────────
Solution treatment: hold at ~520°C → all Cu in solution (supersaturated)
Water quench: freeze Cu in solution (no time to precipitate)

  Metastable supersaturated solid solution (SSSS)
       │
       │  Natural aging (room temperature) or artificial aging
       ▼
  GP (Guinier-Preston) zones:
    Cu-enriched coherent platelets (1–2 nm)
    Cohere with Al lattice → elastic strain field → hardening
    Peak: GP zones form (~12-48 h at room temp, or hours at 100°C)
       │
       │  Overaging (higher temperature or longer time)
       ▼
  θ'' → θ' → θ (equilibrium CuAl₂):
    Becomes incoherent with lattice → strain fields diminish
    Hardness decreases (overaging)

  T6 temper = solution treat + peak age (130°C/24h for 2024)
  T4 temper = solution treat + natural age (room temp)
  T73 temper = overaged to improve corrosion resistance (sacrifices strength)
```

---

## Phase Diagram Reading for Processing

```
LEVER RULE: Phase fractions at two-phase equilibrium
──────────────────────────────────────────────────────────────────
For a two-phase region with phases α and β at composition C₀:

  Weight fraction of β = (C₀ - Cα) / (Cβ - Cα)
  Weight fraction of α = (Cβ - C₀) / (Cβ - Cα)

  [─────────────────────────────────────────────]
  Cα         C₀                              Cβ

  "Lever" balances at C₀:
  f_β × (C₀ - Cα) = f_α × (Cβ - C₀)

Example: 0.4%C steel at 800°C (α+γ region):
  Cα (ferrite) = 0.02%C
  Cγ (austenite) = 0.65%C
  f_γ = (0.4 - 0.02)/(0.65 - 0.02) = 0.38/0.63 = 60% austenite
  f_α = 40% ferrite
```

---

## Alloy Effects on Transformations

### Effect of Alloying Elements on Phase Boundaries

| Element | Effect on A1/A3 | Effect on TTT nose | Effect on Ms | Hardenability |
|---------|----------------|-------------------|-------------|---------------|
| Mn | Lowers A1, A3 | Shifts right | Lowers Ms | Increases |
| Ni | Lowers A1, A3 | Shifts right | Lowers Ms | Increases |
| Cr | Raises A1, A3 | Shifts right | Lowers Ms slightly | Increases strongly |
| Mo | Raises A1, A3 | Shifts right, split nose | Lowers Ms | Increases strongly |
| Si | Raises A1 | Accelerates ferrite | Raises Ms slightly | Moderate |
| V, W | Raise A1, A3 | Shift right | Lower Ms | Moderate |
| Co | Raises A3 | Shifts LEFT | Raises Ms | Decreases |
| Al | Raises A3 | Stabilizes ferrite | Raises Ms | Decreases |

---

## Decision Cheat Sheet

| I need to achieve... | TTT/CCT action |
|---------------------|---------------|
| Maximum hardness | Quench to martensite (exceed critical cooling rate) |
| Tough bainite, no quench cracks | Austempering (isothermal bainite) |
| Soft, machinable microstructure | Full anneal (slow furnace cool through A1) |
| Normalize (uniform, moderately soft) | Austenitize + still air cool |
| Predict if oil quench gives martensite | Check CCT diagram for critical cooling rate |
| Identify composition for deep hardening | Use Jominy data for alloy choice |
| Prevent retained austenite | Ensure Mf is above room temperature |
| Stabilize austenite for wear applications | Cold work, add Mn/Ni (austenitic SS, Hadfield steel) |

---

## Common Confusion Points

**TTT diagrams are isothermal; real parts cool continuously**: You cannot read a cooling curve directly off a TTT diagram. CCT diagrams are the correct tool for continuous cooling. However, TTT diagrams are better for understanding transformation mechanisms and can be used to interpret CCT diagrams conceptually.

**Martensite hardness ≠ alloy hardness**: The maximum hardness of martensite depends almost entirely on carbon content. High-alloy steels are not harder than high-carbon steels in the martensitic state. Alloying provides: deeper hardening (hardenability), better toughness after tempering, elevated-temperature properties — but not harder martensite.

**Retained austenite is normal above ~0.5%C**: When Mf falls below room temperature, some austenite survives quenching. For 0.8%C steel, Mf ≈ -60°C — so there is always ~5–15% retained austenite at room temperature. This is not a defect in most applications, but it can transform under stress (transformation-induced plasticity, TRIP) or during service in cryogenic applications.

**Precipitation hardening "aging" is diffusion-limited**: Unlike martensite formation (milliseconds), precipitation hardening takes hours to days. The aging time-temperature curve is parabolic — doubling temperature does not halve time; the Arrhenius relationship applies. Overaging (too long or too hot) reverses the hardening. Peak properties occur at a specific time-temperature combination.

**Phase diagrams are for equilibrium compositions**: At fast cooling rates, the actual phase boundaries shift (see Ac/Ar temperatures vs equilibrium A1/A3). Real processing always involves non-equilibrium conditions. Phase diagrams give the target; TTT/CCT diagrams give the kinetics of how you get there.
