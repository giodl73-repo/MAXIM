# Heat Treatment: Annealing, Quenching, Tempering

## The Big Picture

Heat treatment is a parameterized procedure: inputs (temperature profile T(t), atmosphere, quench medium) deterministically produce a target microstructure. Each named process — normalize, full anneal, Q&T, carburize+quench+temper — is a specific parameterization. This maps directly to a build pipeline with configurable stages: the same "compile" step (austenitize) followed by different "link" parameters (quench vs. furnace cool) produces entirely different outputs. Pre-conditions (starting microstructure, prior cold work) and post-conditions (hardness, grain size, residual stress) define each procedure's contract.

Heat treatment is the application of controlled thermal cycles to solid metal to achieve target microstructure and properties. It is the primary tool for controlling hardness, strength, ductility, and toughness in steel and aluminum alloys. Every cycle involves three controllable parameters: temperature, time, and cooling rate.

```
HEAT TREATMENT TAXONOMY
──────────────────────────────────────────────────────────────────
┌─────────────────────────────────────────────────────────────────┐
│  FULL PROCESSING (through-thickness)                            │
│                                                                 │
│  Annealing family:       Hardening family:                      │
│    Full anneal             Austenitize + quench                 │
│    Process anneal          Martempering                         │
│    Spheroidize anneal      Austempering                         │
│    Stress relief           Temper (always follows quench)       │
│    Normalizing                                                  │
│                            Solution treat + age (Al, Ti, Ni)    │
├─────────────────────────────────────────────────────────────────┤
│  SURFACE (shallow depth, tough core maintained)                  │
│    Carburizing (diffusion of C into surface)                    │
│    Nitriding (diffusion of N into surface)                      │
│    Carbonitriding (C + N)                                        │
│    Induction hardening (localized austenitize + quench)         │
│    Flame hardening (torch + quench)                             │
│    Laser surface hardening                                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Annealing Processes

### Full Anneal

```
FULL ANNEAL
──────────────────────────────────────────────────────────────────
Purpose: Maximum softness, maximum ductility, relieve internal stress.
         Prepare for machining or forming.

Process:
  1. Heat to 30–50°C above A3 (for hypoeutectoid, ~900–950°C)
     or above A1 (for hypereutectoid, ~750–800°C)
  2. Soak until fully austenitic
  3. Furnace cool SLOWLY (typically 50°C/hour or less)
     → through A1 with slow cooling → coarse pearlite + ferrite

Result:
  Very soft: 150–200 HV for 0.4%C steel
  Coarse pearlite: lamellar spacing large → soft
  Maximum machinability
  Ductility: 25–30% elongation

Limitation:
  Very long cycle time (many hours for large parts)
  Costly furnace time
```

### Normalizing

```
NORMALIZING
──────────────────────────────────────────────────────────────────
Purpose: Refine grain size, uniform microstructure, moderate
         properties. Intermediate between full anneal and hardening.
         Most common "as-supplied" condition for structural steel.

Process:
  1. Heat to 30–50°C above A3 (~900–950°C)
  2. Soak (20 min per inch of cross-section)
  3. Air cool in still air (faster than full anneal, slower than quench)

Result:
  Fine pearlite + ferrite
  Harder than full anneal (~200–280 HV)
  Good machinability and toughness
  Grain refinement: removes cast structure, improves forgings

vs. Full anneal:
  Faster cycle
  Slightly harder / higher strength
  Better impact toughness than coarse pearlite from full anneal
```

### Stress Relief Anneal

```
STRESS RELIEF ANNEAL
──────────────────────────────────────────────────────────────────
Purpose: Reduce residual stresses from welding, machining,
         cold work, without changing hardness significantly.

Process:
  Steel: hold at 500–650°C (below A1) for 1–4 hours
         Must stay below A1 to avoid phase transformation
  Aluminum: 300–350°C for aluminum alloys
  Weldments: typically 600–650°C for 1 hour per inch of thickness

Mechanism:
  Temperature allows dislocation recovery and creep
  Residual stresses relax to material's yield stress at that temperature
  No phase transformation (below A1)
  Hardness change: minimal (slight softening)

Applications:
  Post-weld stress relief of heavy fabrications
  Dimensional stability: machined precision components
  Prevent stress corrosion cracking (SCC)
  Post-straightening of distorted parts
```

### Spheroidize Anneal

```
SPHEROIDIZE (SPHEROIDIZING) ANNEAL
──────────────────────────────────────────────────────────────────
Purpose: Convert lamellar pearlite (cementite plates) to
         spheroidal cementite particles → maximum softness
         for cold working operations (drawing, cold heading).

Process (typical for high-carbon steel):
  Option A: Hold just below A1 (700–720°C) for 8–24 hours
  Option B: Cycle above/below A1 repeatedly
  Option C: For heavily work-hardened steel, start above A1

Result:
  Spherical Fe₃C particles in ferrite matrix
  Softest possible microstructure for high-carbon steels
  Excellent cold formability
  ~150–180 HV for 1.0%C steel (vs ~280 HV spheroidized)

Applications:
  High-carbon steel wire before cold drawing
  Bearing steel (52100) before machining
  Required for any cold heading of high-carbon steel (bolts, screws)
```

---

## Quench Hardening

### Austenitizing and Quenching

```
QUENCH HARDENING PROCESS
──────────────────────────────────────────────────────────────────
1. AUSTENITIZE
   Heat steel into single-phase austenite region
   Temperature: 30–80°C above Ac3 (complete austenitization)
   Soak time: dependent on cross-section, typically 1 hour/inch
   Purpose: Dissolve carbides, homogenize carbon in austenite

2. QUENCH (rapid cooling)
   Transfer to quench medium immediately
   Cooling rate must exceed critical cooling rate → martensite

Quench media (fastest to slowest):
  Brine (10% NaCl in water):    fastest, most distortion/cracking risk
  Cold water:                   very fast
  Warm water (50–60°C):         fast, less cracking
  Polymer quench (PAG):         adjustable by concentration
  Oil (mineral quench oil):     moderate, good for alloy steels
  Forced air / gas quench:      slow, for high-hardenability alloys
  Still air:                    very slow, limited to very high Cr tools

Distortion and cracking risk:
  Faster quench → more martensite, more quench cracking risk
  Choose slowest quench that gives required microstructure
  4340: oil quench → fully martensitic (vs. 1080: requires water)

3. TEMPER IMMEDIATELY
   Martensite is brittle — must temper before cooling to room temp
   Especially critical for high-carbon, large cross-sections
```

### Quench Cracking Prevention

```
QUENCH CRACKING RISK FACTORS AND MITIGATION
──────────────────────────────────────────────────────────────────
Risk factors:
  High carbon (>0.5%C): martensite more brittle, more volume expansion
  Large cross-section: thermal gradients → differential transformation
  Sharp corners, holes: stress concentration during transformation
  Slow medium for high-hardenability steel: unnecessary gradient
  Delay before tempering: martensite sits unstable, crack propagates

Mitigation:
  Minimize sharp corners (r > 2mm preferred)
  Use slowest quench medium that achieves target hardness
  Temper within 30 minutes of quenching (sooner is better)
  Martempering: quench to just above Ms, equalize, then air cool
  Pre-heat complex shapes (reduces thermal gradient at quench entry)
  Choose alloy steel (oil quench) over plain carbon (water quench)
```

---

## Tempering

### Tempering Mechanisms

```
TEMPERING OF MARTENSITE
──────────────────────────────────────────────────────────────────
Martensite is metastable (supersaturated BCT structure).
Tempering allows controlled decomposition to stable state.

STAGE I TEMPERING (below ~250°C):
  Epsilon carbide (Fe₂.₄C) precipitates from martensite
  Carbon partially rejected from BCT → less tetragonal distortion
  Hardness drops slightly
  Brittleness reduced somewhat

STAGE II TEMPERING (~200–300°C):
  Retained austenite transforms to bainite/ferrite
  (Important in high-carbon steels with significant retained γ)

STAGE III TEMPERING (250–400°C):
  Epsilon carbide → cementite (Fe₃C) replaces epsilon carbide
  Martensite → tempered martensite (ferrite + fine carbides)
  Major hardness reduction begins in this range
  Significant improvement in ductility and toughness

STAGE IV TEMPERING (above 400°C):
  Cementite coarsens and spheroidizes
  Major reduction in hardness (recovery of bulk ductility)
  Above 600°C: approaching normalized/annealed properties

TEMPERED MARTENSITE EMBRITTLEMENT (TME): 300–400°C
  Complex carbide precipitation at grain boundaries
  Impact toughness decreases (trough in Charpy vs. temp)
  Avoid tempering in this range when toughness critical
  Also called "350°C embrittlement"
```

### Tempering Temperature vs Properties

```
TEMPERING TEMPERATURE EFFECT (medium carbon steel, e.g., 4140)
──────────────────────────────────────────────────────────────────
Temp(°C)  Hardness(HRC)  UTS(MPa)  Elongation  Charpy(J)
────────  ─────────────  ────────  ──────────  ─────────
As-quenched  ~58         2000      <5%         <10
150           55          1900      5%          15
200           53          1800      6%          20
300           48          1600      8%          25     ← TME zone starts
400           43          1400      12%         35     ← TME trough
500           38          1200      16%         80
600           32          1050      20%         120
650           28           900      25%         150

Typical structural applications: 550–650°C temper (Q&T condition)
High-strength bolts: 400–500°C (compromise strength/toughness)
Springs: 350–450°C (high hardness needed)
Dies and tools: 150–250°C (maximum hardness with some temper)
```

---

## Case Hardening Processes

### Carburizing

```
GAS CARBURIZING
──────────────────────────────────────────────────────────────────
Purpose: Introduce carbon into surface layer (case) while
         maintaining low-carbon (tough) core.
Starting material: low-carbon steel (0.15–0.25% C)

Process:
  1. Heat to 850–950°C in carburizing atmosphere (CH₄ or propane)
     CH₄ → C(nascent) + 2H₂  at steel surface
  2. Carbon diffuses into steel surface
  3. Carbon profile: ~0.8% at surface → ~0.2% at case/core boundary
  4. Case depth (time/temperature controlled):
       ~0.5mm: 2 hours at 900°C
       ~1.0mm: 5–6 hours at 900°C
       ~2.0mm: 15–20 hours at 900°C
       Case depth ∝ √(D×t) with D(carbon in γ) increasing with T

  5. Direct quench (from carburizing temperature) or:
  6. Slow cool + reheat + quench (for better grain structure)
  7. Low temper (150–200°C) to reduce brittleness

Result:
  Surface: ~0.8%C, martensite after quench → 60–65 HRC
  Core: ~0.2%C, low-carbon martensite or pearlite → 35–45 HRC
  Compressive residual stress at surface → excellent fatigue resistance

Applications: Gears, cams, pins, bearing surfaces
```

### Nitriding

```
GAS NITRIDING
──────────────────────────────────────────────────────────────────
Purpose: Introduce nitrogen into surface for hard, wear-resistant
         case WITHOUT quenching. Very low distortion.

Process:
  1. Finish machine to final dimensions (no quench after nitriding)
  2. Heat to 500–550°C in ammonia (NH₃) atmosphere
     NH₃ → N(nascent) + H₂ at steel surface
  3. Nitrogen diffuses into steel, forms hard nitrides (AlN, CrN, Fe₄N)
  4. Very slow process: 15–100 hours for 0.3–0.6mm case depth
  5. No quench required → minimum distortion

Nitriding steels: must contain nitride-forming elements
  AISI 4140, 4340 (Cr, Mo nitrides)
  Nitralloy 135 (Al-bearing, strongest nitrided case)

Result:
  White layer: ~15–25 µm, very hard (~1000+ HV), brittle
    (Usually removed by post-grinding if fatigue is concern)
  Diffusion zone: ~0.3–0.6mm, 650–900 HV
  Compressive residual stress (excellent for fatigue)
  No distortion (process below tempering temperature of pre-treated core)
  Excellent corrosion resistance

Plasma nitriding (ion nitriding):
  Faster than gas, better control, lower temperatures possible
  Eliminates white layer more easily
```

### Induction Hardening

```
INDUCTION HARDENING
──────────────────────────────────────────────────────────────────
Purpose: Selectively harden specific areas (gear teeth, journal)
         without affecting entire part.

Process:
  1. Induction coil near part surface
  2. AC current (1 kHz–500 kHz) → induced eddy currents in part
  3. Resistive heating → surface austenitizes in seconds (no bulk heating)
  4. Water or polymer spray quench → martensite in surface only
  5. No temper required for some applications (self-tempering by heat flow)
     or low temper for toughness

Depth control by frequency:
  High frequency (100–500 kHz): shallow case (~0.5–1mm) → small parts
  Low frequency (3–10 kHz): deep case (~3–6mm) → large shafts, gears

Result:
  Hard surface: 58–65 HRC (same as through-hardening)
  Tough core: unchanged from original (normalized or Q&T)
  Compressive residual stress in surface: excellent fatigue
  Speed: seconds per part → high production rate
  Energy efficiency: heat only what needs hardening

Applications: Crankshaft journals, camshafts, gear teeth,
  transmission shafts — the standard for automotive drivetrain
```

---

## Heat Treatment of Non-Ferrous Alloys

### Aluminum Alloys (Precipitation Hardening)

```
ALUMINUM ALLOY HEAT TREATMENT (2024-T4/T6 example)
──────────────────────────────────────────────────────────────────
1. SOLUTION TREATMENT
   Heat to ~495°C (within single-phase solid solution region)
   Dissolve all Cu into Al matrix (single phase: α solid solution)
   Water quench: freeze Cu in solution (supersaturated)
   Do NOT overheat: incipient melting at grain boundaries (≥510°C)
   Do NOT under-heat: incomplete dissolution → weaker precipitation

2. AGING (PRECIPITATION)
   T4: natural age at room temperature (24h to peak)
     → GP zones → moderate strength, maximum formability
   T6: artificial age at 160–177°C for 8–12 hours
     → θ' (transition) precipitates → peak strength
   T73: artificial overaging (200°C+ longer time)
     → coarser precipitates → less strength, better SCC resistance
     Used where stress corrosion cracking is the failure mode

Temper designations:
  T3: SHT + cold work + natural age
  T4: SHT + natural age
  T6: SHT + artificial age (peak)
  T7: SHT + overaged (stabilized or SCC-resistant)
  T8: SHT + cold work + artificial age

2024-T4 vs 2024-T6:
  T4: UTS 440 MPa, 19% elong. → formable
  T6: UTS 476 MPa, 11% elong. → strongest
  For aircraft sheet formed then installed: T3 (intermediate)
```

### Titanium Alloys

```
TITANIUM ALLOY HEAT TREATMENT (Ti-6Al-4V)
──────────────────────────────────────────────────────────────────
Ti-6Al-4V (Grade 5): most common titanium alloy
  Alpha (α) phase: HCP, stable below beta transus
  Beta (β) phase: BCC, stable above beta transus (~995°C)
  Beta transus: ~995°C (temperature where all α transforms to β)

ANNEALED (mill annealed):
  Hold below beta transus (~700–850°C), air cool
  Result: α+β equiaxed structure
  UTS: ~950 MPa, 14% elongation
  Baseline structural condition

SOLUTION TREAT + AGE (STA) — maximum strength:
  1. Solution treat at ~900–950°C (in α+β region, just below beta transus)
  2. Rapid quench (water)
  3. Age at 480–540°C for 2–4 hours → fine α precipitates in β matrix
  UTS: ~1100–1150 MPa, 10% elongation
  Applications: high-strength aerospace structures

β-annealed:
  Heat above beta transus → all β → slow cool → Widmanstätten α laths
  Lower strength, better fatigue crack growth resistance, better creep
  Applications: rotating compressor blades (fatigue priority)
```

---

## Furnace Types and Atmospheres

```
HEAT TREATMENT FURNACE TYPES
──────────────────────────────────────────────────────────────────
BOX/BATCH FURNACE:
  Chamber with heating elements, door load/unload
  Sizes: lab scale to room-size
  Atmosphere control possible
  Versatile for job shop, aerospace

CONTINUOUS (BELT/MESH BELT) FURNACE:
  Parts travel through on belt
  Multiple zones (heat up, soak, cool)
  High production rate, low per-piece cost
  Typical: brazing, annealing, sintering
  The continuous furnace is a pipeline processor: each zone is a
  transformation stage, parts are the data, throughput = production rate.
  Zone temperature profiles are the stage parameters. Same mental model
  as a staged processing pipeline where items flow through sequential
  stateless transformations.

VACUUM FURNACE:
  <10⁻³ torr atmosphere → no oxidation
  Critical for: titanium, high-alloy steels, brazing
  Partial pressure control (N₂, Ar gas)
  Excellent surface quality

ATMOSPHERE TYPES:
  Endothermic gas (RX gas): CO-H₂-N₂ mixture, slightly carburizing
    → Used for bright annealing, controlled carburizing
  Nitrogen + methanol: safer than endothermic, common
  Exothermic gas: oxidizing (for oxide annealing of copper)
  Pure nitrogen: inert, no oxidation, no carburizing
  Vacuum: best surface quality

ATMOSPHERE CONTROL:
  Carbon potential (aC): controls surface carbon during treatment
  Equilibrium with: CO₂ content, dew point, O₂ sensor
  Too high aC: case carburizes during anneal (unwanted)
  Too low aC: decarburization (surface loses carbon → soft)
```

---

## Decision Cheat Sheet

| I need to... | Heat treatment |
|--------------|---------------|
| Soften steel for machining | Full anneal (furnace cool) |
| Achieve maximum hardness | Quench (exceed critical cooling rate) → martensite |
| Reduce quench brittleness | Temper (temperature depends on required hardness) |
| Uniform, moderate properties on structural steel | Normalize (air cool from austenite) |
| Hard surface, tough core (gears, cams) | Carburize + quench + low temper |
| Very hard surface, no distortion | Nitride (after finishing machining) |
| Selective surface hardening (journals) | Induction harden |
| Relieve weld residual stress | Stress relief anneal (600–650°C, 1h/inch) |
| Aluminum maximum strength | Solution treat + artificial age (T6) |
| Titanium maximum strength | Solution treat + age (STA) |

---

## Common Confusion Points

**Tempering is not optional**: Quench-hardened parts must be tempered promptly. Martensite is under high internal stress and can crack if left untempered, especially under thermal cycling (workshop temperature changes) or mechanical handling. "Temper immediately" means within hours, preferably within 30 minutes.

**Normalizing is not annealing**: Normalizing uses air cooling; annealing uses furnace cooling. Normalizing gives a finer, harder, tougher microstructure. Annealing gives maximum softness. They are not interchangeable. Many engineers treat "normalize" as a synonym for "fully anneal" — they are not.

**Carburizing depth ≠ hardened depth**: Carburized case has high carbon to some depth. After quenching, the hardened zone is approximately the carburized zone. But effective case depth (defined as depth to some hardness, e.g., 50 HRC) is less than total case depth. Specify effective case depth in drawings, not total case depth.

**Aluminum "T" designations**: The temper code includes the processing history. T3 ≠ T4 ≠ T6 ≠ T73 even for the same alloy. Substituting T6 for T73 on a structural fitting in a corrosive environment can cause SCC failure. Always verify the correct temper for the application.

**Induction hardening frequency determines depth**: High frequency (kHz) = shallow case. Low frequency (Hz) = deep case. The skin depth δ = √(ρ/πfμ). Doubling frequency quarters skin depth. The coil and power supply must be matched to the required case depth — you cannot use a high-frequency induction heater for deep shaft hardening.
