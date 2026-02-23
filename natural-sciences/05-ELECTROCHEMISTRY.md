# 05-ELECTROCHEMISTRY — Electrochemistry

> Redox reactions, electrochemical cells, Nernst equation, batteries, electrolysis,
> Pourbaix diagrams, and corrosion. The field where chemistry and electricity are
> literally the same thing.

---

## The Core Idea

```
Oxidation:   loss of electrons    (OIL — Oxidation Is Loss)
Reduction:   gain of electrons    (RIG — Reduction Is Gain)

In solution these processes are coupled:
  Zn(s) + Cu²⁺(aq) → Zn²⁺(aq) + Cu(s)   (electrons flow from Zn to Cu²⁺)

If you SEPARATE oxidation from reduction → electrons travel through a wire
→ CURRENT → do electrical work.

That separation is an electrochemical cell.
```

---

## Oxidation States

Rules (in order of priority):
1. Free element: OS = 0
2. Monatomic ion: OS = charge
3. H = +1 (except metal hydrides: H = −1)
4. O = −2 (except peroxides O₂²⁻: O = −1; OF₂: O = +2)
5. F = −1 always
6. Group 1 = +1, Group 2 = +2 in compounds
7. Sum of OS = charge of species (0 for neutral)

```
Assign OS in Cr₂O₇²⁻:
  2(OS_Cr) + 7(−2) = −2
  2(OS_Cr) = 12
  OS_Cr = +6   (dichromate — very oxidizing)

In Cr³⁺: OS = +3. Reduction: Cr⁶⁺ → Cr³⁺ (gains 3 e⁻ per Cr, 6 total for Cr₂O₇²⁻)
```

### Balancing Redox Equations — Half-Reaction Method

```
Unbalanced: MnO₄⁻ + Fe²⁺ → Mn²⁺ + Fe³⁺  (acidic solution)

STEP 1: Write half-reactions
  Oxidation:   Fe²⁺ → Fe³⁺ + e⁻
  Reduction:   MnO₄⁻ → Mn²⁺

STEP 2: Balance O with H₂O, H with H⁺, charge with e⁻
  Reduction:   MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O

STEP 3: Multiply to equalize electrons
  Oxidation × 5:   5Fe²⁺ → 5Fe³⁺ + 5e⁻
  Reduction × 1:   MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O

STEP 4: Add:
  MnO₄⁻ + 5Fe²⁺ + 8H⁺ → Mn²⁺ + 5Fe³⁺ + 4H₂O  ✓

For basic solution: add OH⁻ to neutralize H⁺ → form H₂O
```

---

## Electrochemical Cells

### Galvanic Cell (Voltaic) — Spontaneous, Produces Work

```
ZINC-COPPER DANIELL CELL:

  │ Zn(s) │ Zn²⁺(aq) ║ Cu²⁺(aq) │ Cu(s) │
    anode               salt         cathode
    (oxidation)         bridge       (reduction)

Anode:    Zn(s) → Zn²⁺(aq) + 2e⁻       E° = +0.76 V (oxidation)
Cathode:  Cu²⁺(aq) + 2e⁻ → Cu(s)        E° = +0.34 V (reduction)

E°cell = E°cathode − E°anode = 0.34 − (−0.76) = +1.10 V

Cell notation:
  anode | anode solution ║ cathode solution | cathode
  Zn(s) | Zn²⁺(1M) ║ Cu²⁺(1M) | Cu(s)

Salt bridge: maintains charge neutrality (ions flow to balance charge buildup)
  Without it: anode solution accumulates Zn²⁺ (+charge) → repels more Zn²⁺ → stops
```

### Electrolytic Cell — Non-Spontaneous, Requires Work

```
EXTERNAL POWER SOURCE drives non-spontaneous reaction
E_applied > E°cell (must overcome the cell potential)

Applications: electroplating, Hall-Héroult process (Al from Al₂O₃),
              chlor-alkali process (NaOH + Cl₂ from NaCl), water splitting

Faraday's laws:
  Mass deposited = (M/nF) · I · t
  M = molar mass,  n = electrons,  F = 96485 C/mol,  I = current (A),  t = time (s)

Example: Cu electroplating for 1 hour at 2 A
  mol e⁻ = (2 A × 3600 s) / 96485 C/mol = 0.0746 mol
  Cu²⁺ + 2e⁻ → Cu:  mol Cu = 0.0746/2 = 0.0373 mol
  mass Cu = 0.0373 × 63.5 g/mol = 2.37 g
```

---

## Standard Reduction Potentials (E°)

Measured vs Standard Hydrogen Electrode (SHE): 2H⁺(1M) + 2e⁻ → H₂(1 atm), E° ≡ 0.000 V

```
Reduction half-reaction (25°C, 1M, 1 atm)          E° (V)
──────────────────────────────────────────────────────────────
F₂ + 2e⁻ → 2F⁻                                    +2.87  ← strongest oxidizer
MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O                 +1.51
Cr₂O₇²⁻ + 14H⁺ + 6e⁻ → 2Cr³⁺ + 7H₂O             +1.33
Cl₂ + 2e⁻ → 2Cl⁻                                  +1.36
O₂ + 4H⁺ + 4e⁻ → 2H₂O                             +1.23
Br₂ + 2e⁻ → 2Br⁻                                  +1.07
Ag⁺ + e⁻ → Ag                                      +0.80
Fe³⁺ + e⁻ → Fe²⁺                                   +0.77
Cu²⁺ + 2e⁻ → Cu                                    +0.34
2H⁺ + 2e⁻ → H₂                                    ±0.00  ← SHE reference
Pb²⁺ + 2e⁻ → Pb                                    −0.13
Ni²⁺ + 2e⁻ → Ni                                    −0.25
Fe²⁺ + 2e⁻ → Fe                                    −0.44
Zn²⁺ + 2e⁻ → Zn                                    −0.76
Al³⁺ + 3e⁻ → Al                                    −1.66
Mg²⁺ + 2e⁻ → Mg                                    −2.37
Na⁺ + e⁻ → Na                                      −2.71
Li⁺ + e⁻ → Li                                      −3.04  ← strongest reducer
```

**Using the table:**
- Higher E° = better oxidizing agent (easier to reduce)
- Lower E° = better reducing agent (easier to oxidize)
- Spontaneous cell: combine a half-reaction from high E° (cathode) with one from low E° (anode)
- E°cell = E°cathode − E°anode > 0 for spontaneous

---

## Nernst Equation

E° is at standard state (1 M, 1 atm, 298 K). Real conditions: use Nernst.

```
E = E° − (RT/nF) · ln Q

At 298 K:  RT/F = 0.02569 V,  RT ln(x) / F = 0.05916 log₁₀(x) / n

E = E° − (0.05916/n) · log Q

where Q = reaction quotient (same form as K)

At equilibrium: E = 0, Q = K
  0 = E° − (0.05916/n) · log K
  log K = nE° / 0.05916
  E° = (0.05916/n) · log K    →    larger E° → larger K
```

### Link to Gibbs Free Energy

```
ΔG = −nFE          (work done by cell)
ΔG° = −nFE°
ΔG = ΔG° + RT ln Q = −nFE° + RT ln Q = −nF(E° − RT ln Q / nF) = −nFE  ✓

At standard state:
  ΔG° = −nFE°
  K = e^(nFE°/RT) = 10^(nE°/0.05916)

Example: Zn/Cu cell  E° = 1.10 V, n = 2
  ΔG° = −2 × 96485 × 1.10 = −212,300 J/mol = −212.3 kJ/mol
  K = e^(2 × 96485 × 1.10 / 8.314 / 298) = e^85.6 = 10^37.2
  → Reaction essentially goes to completion
```

### Concentration Cells

Two identical half-cells at different concentrations.
E° = 0, but E ≠ 0 because Q ≠ 1.

```
Cell: Cu | Cu²⁺(0.001M) ║ Cu²⁺(1.0M) | Cu
Cathode: Cu²⁺(1.0M) + 2e⁻ → Cu
Anode:   Cu → Cu²⁺(0.001M) + 2e⁻
Q = [Cu²⁺]_anode / [Cu²⁺]_cathode = 0.001/1.0 = 0.001

E = 0 − (0.05916/2) · log(0.001) = 0.0886 V
```

**Biological relevance**: nerve action potential, pH gradients across membranes,
and mitochondrial proton-motive force are all concentration cell phenomena.

---

## Pourbaix Diagrams (E vs pH)

Shows the thermodynamically stable phase of an element as a function
of electrode potential (E) and pH. Essential for corrosion science.

```
IRON POURBAIX DIAGRAM (simplified):

  E (V)
+1.2 │  ─ ─ ─ ─ O₂/H₂O line ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
     │
+0.4 │         Fe³⁺ │  Fe₂O₃
     │               │
  0  │  ─ ─ ─ ─ H⁺/H₂ line ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
     │  Fe²⁺          │  Fe(OH)₂ / Fe₃O₄
−0.4 │                │
     │    Fe(s)        │
−0.8 └────────────────────────────────────
     0       4       8       12   pH

Regions:
  Below H₂/H₂O line:  H₂ evolution kinetically possible
  Above O₂/H₂O line:  O₂ evolution kinetically possible
  Fe²⁺/Fe³⁺ region:  corrosion (dissolution)
  Fe₂O₃/Fe₃O₄ region: passivation (protective oxide layer)
  Fe(s) region:        immunity (thermodynamically stable)

Corrosion control strategies:
  Cathodic protection: shift E below Fe stability → Fe(s) immune (sacrificial anode: Zn)
  Anodic passivation: shift E into oxide region (stainless steel: Cr₂O₃ film)
```

---

## Batteries

### Lead-Acid

```
Anode (−):   Pb(s) + SO₄²⁻ → PbSO₄(s) + 2e⁻         E° = −0.36 V
Cathode (+):  PbO₂(s) + 4H⁺ + SO₄²⁻ + 2e⁻ → PbSO₄ + 2H₂O   E° = +1.69 V

E°cell = 1.69 − (−0.36) = 2.05 V per cell (12 V battery = 6 cells)
Rechargeable: reverse current regenerates Pb and PbO₂
H₂SO₄ electrolyte: Peukert effect, gassing on overcharge (H₂ + O₂ evolution)
```

### Lithium-Ion

```
Anode (−):   LiₓC₆ → C₆ + xLi⁺ + xe⁻       (graphite intercalation)
Cathode (+):  Li₁₋ₓCoO₂ + xLi⁺ + xe⁻ → LiCoO₂

Nominal voltage: 3.6–4.2 V per cell
Energy density: 150–250 Wh/kg (vs lead-acid: ~30–50 Wh/kg)
Electrolyte: LiPF₆ in organic carbonate solvents (flammable — thermal runaway risk)
SEI layer: solid electrolyte interphase forms on first charge — limits capacity fade
```

### Fuel Cell

```
H₂/O₂ PEM fuel cell:
  Anode:   H₂ → 2H⁺ + 2e⁻                (Pt catalyst)
  Cathode: ½O₂ + 2H⁺ + 2e⁻ → H₂O        (Pt catalyst)
  Net:     H₂ + ½O₂ → H₂O                E° = 1.23 V

Theoretical efficiency: ΔG/ΔH = 83% at 25°C (vs ~40% for combustion engine)
Practical: ~50–60% (activation overpotential, ohmic losses)
Overpotential: extra voltage beyond E°_cell needed to drive reaction at useful rate
```

---

## Overpotential and Electrode Kinetics (Butler-Volmer)

The Nernst equation gives equilibrium potential. Overpotential (η) is the
additional potential needed for net current flow.

```
Butler-Volmer equation:
  j = j₀ [exp(αFη/RT) − exp(−(1−α)Fη/RT)]

j₀ = exchange current density (kinetics parameter — larger = faster)
α  = transfer coefficient (~0.5 for symmetric barriers)
η  = overpotential = E − E_eq

Tafel approximation (large |η|, one exponential dominates):
  |η| = (RT/αF) · ln(j/j₀)
  Plot |η| vs log|j| → Tafel slope = 2.303RT/αF ≈ 120 mV/decade (for α=0.5)

Why overpotential matters:
  Even with E°cell = 1.23 V (water splitting), practical cells need ~1.8 V
  because of overpotentials at both electrodes.
  Better catalyst → lower j₀⁻¹ → lower overpotential → higher efficiency.
```

---

## Corrosion

```
Iron corrosion (rust formation in wet air):
  Anodic sites:   Fe → Fe²⁺ + 2e⁻
  Cathodic sites: O₂ + 2H₂O + 4e⁻ → 4OH⁻

Then:  Fe²⁺ + 2OH⁻ → Fe(OH)₂  →  oxidizes  →  Fe₂O₃·xH₂O (rust)

Galvanic corrosion: two dissimilar metals in contact in electrolyte
  More active metal (lower E°) becomes anode → corrodes preferentially

  Example: Fe/Cu couple in seawater → Fe corrodes, Cu protected
  Example: Mg bolts in Al frame → Mg sacrificed, Al protected

Prevention:
  Sacrificial anode: more active metal (Zn on steel hull, Mg on pipelines)
  Cathodic protection: impress negative current on structure
  Coatings: paint, powder coat, galvanizing (Zn on steel)
  Alloying: Cr in stainless steel → passive Cr₂O₃ film (requires >12% Cr)
  Inhibitors: chromate (toxic), organic inhibitors adsorb on surface
```

---

## Decision Cheat Sheet

| Question | Concept | Key equation |
|----------|---------|-------------|
| Will this redox reaction be spontaneous? | E°cell > 0 | E°cell = E°cathode − E°anode |
| What is ΔG for this cell reaction? | Free energy link | ΔG° = −nFE° |
| What is K for this equilibrium? | Nernst link | log K = nE°/0.05916 |
| How does voltage change with concentration? | Nernst | E = E° − (0.05916/n)·log Q |
| Which metal corrodes in galvanic pair? | More negative E° | Anode (oxidation) = more active metal |
| How to protect steel in seawater? | Cathodic protection | Attach Zn (Zn corrodes instead) |
| Why does stainless steel not rust? | Passivation | Cr₂O₃ film, Pourbaix passivation region |
| How much metal is plated by 10 A for 30 min? | Faraday's laws | m = MIt/nF |
| What determines battery voltage? | E°cell | Sum of half-cell potentials |
| Why does H₂ fuel cell need Pt? | Overpotential | Pt has high j₀ → low overpotential |

---

## Common Confusion Points

**E° signs depend on convention (reduction vs oxidation)**
Reduction potentials are the standard (IUPAC). The table lists reduction half-reactions.
To get E° for oxidation: flip the sign.
E°cell = E°cathode(reduction) − E°anode(reduction) = E°cathode + E°anode(oxidation)
Both formulations are correct — don't mix them.

**E°cell ≠ E°cell per cell for batteries**
A 12V lead-acid battery has six 2V cells in series. Total voltage = 6 × 2V.
E°cell is per electrochemical cell, not per device.

**SHE is a reference, not a real electrode**
Standard Hydrogen Electrode (2H⁺ + 2e⁻ → H₂, E° ≡ 0.000 V) is a theoretical
standard. Real reference electrodes: Ag/AgCl (E = +0.197 V vs SHE),
saturated calomel electrode (SCE, E = +0.241 V vs SHE).
All literature E° values must be compared on the same reference.

**Nernst concentrations are activities, not molarities**
Rigorously: Q uses activities (aᵢ = γᵢ[cᵢ/c°]). Activity coefficient γ ≠ 1 at high
concentrations. For dilute solutions, aᵢ ≈ [cᵢ]. For concentrated electrolytes
(batteries, seawater), use Debye-Hückel or Pitzer activity coefficients.

**Pourbaix diagrams are thermodynamic, not kinetic**
A region labeled "Fe₂O₃" means that phase is thermodynamically stable —
it may not form quickly. Passivation requires the oxide to form a protective film
(depends on kinetics, surface adhesion, porosity). Chromium passivates well;
iron oxide is porous and flakes (rust). Same thermodynamic diagram, different kinetics.
