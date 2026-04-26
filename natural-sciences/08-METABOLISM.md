# 08-METABOLISM — Cellular Metabolism

> Glycolysis → TCA → oxidative phosphorylation → ~30 ATP per glucose.
> Gluconeogenesis, β-oxidation, pentose phosphate pathway, and the
> regulatory logic that integrates all of them.

---

## The Big Picture — Metabolic Map

```
FUEL INPUTS
  Glucose ──────────────────────────────────────────┐
  Fatty acids ─────────────────────────────────┐    │
  Amino acids ────────────────────────────┐    │    │
  Glycerol ───────────────────────────┐   │    │    │
                                      │   │    │    │
                                      ▼   ▼    ▼    ▼
                              GLYCOLYSIS (cytoplasm)
                              Glucose → 2 Pyruvate
                              Net: 2 ATP, 2 NADH

                                          ▼
                              PYRUVATE DEHYDROGENASE (matrix)
                              2 Pyruvate → 2 Acetyl-CoA
                              Yield: 2 NADH, 2 CO₂

                 Fatty acids (β-oxidation) ─→ Acetyl-CoA ←─ Amino acids (ketogenic)
                                                   │
                                                   ▼
                                        TCA CYCLE (matrix)
                                        2 × (3 NADH + 1 FADH₂ + 1 GTP)
                                        Release: 4 CO₂

                                                   │
                                                   ▼
                              OXIDATIVE PHOSPHORYLATION (inner membrane)
                              NADH, FADH₂ → proton gradient → ATP synthase
                              Yield: ~26–28 ATP

                                         TOTAL: ~30–32 ATP/glucose
```

---

## Glycolysis (10 Steps, Cytoplasm)

```
INVESTMENT PHASE (steps 1–5): consume 2 ATP
  1.  Glucose + ATP → Glucose-6-phosphate (G6P) + ADP
      Enzyme: Hexokinase (or glucokinase in liver)
      Irreversible. Traps glucose in cell. Key regulation point.

  2.  G6P ⇌ Fructose-6-phosphate (F6P)
      Enzyme: Phosphoglucose isomerase

  3.  F6P + ATP → Fructose-1,6-bisphosphate (FBP) + ADP
      Enzyme: Phosphofructokinase-1 (PFK-1)
      *** THE KEY REGULATORY STEP ***
      Inhibited by: ATP (energy sufficient), citrate (TCA running)
      Activated by: AMP, ADP (energy needed), fructose-2,6-bisphosphate

  4.  FBP → DHAP + Glyceraldehyde-3-phosphate (G3P)
      Enzyme: Aldolase

  5.  DHAP ⇌ G3P
      Enzyme: Triose phosphate isomerase (TPI — near-perfect catalyst)
      — BOTH molecules continue as G3P (×2 for all subsequent steps) —

PAYOFF PHASE (steps 6–10): produce 4 ATP, 2 NADH
  6.  G3P + Pᵢ + NAD⁺ → 1,3-BPG + NADH + H⁺
      Enzyme: G3P dehydrogenase

  7.  1,3-BPG + ADP → 3-phosphoglycerate (3-PG) + ATP
      Enzyme: Phosphoglycerate kinase  (substrate-level phosphorylation)

  8.  3-PG ⇌ 2-phosphoglycerate (2-PG)
      Enzyme: Phosphoglycerate mutase

  9.  2-PG ⇌ Phosphoenolpyruvate (PEP) + H₂O
      Enzyme: Enolase

  10. PEP + ADP → Pyruvate + ATP
      Enzyme: Pyruvate kinase  (substrate-level phosphorylation, irreversible)
      Inhibited by: ATP, alanine; Activated by: fructose-1,6-bisphosphate

NET per glucose:
  −2 ATP (investment) + 4 ATP (payoff) = +2 ATP
  +2 NADH (cytoplasmic)
  +2 Pyruvate
```

---

## Pyruvate Fate

```
Aerobic conditions:
  Pyruvate → mitochondrial matrix → Pyruvate Dehydrogenase Complex (PDC)
  Pyruvate + CoA + NAD⁺ → Acetyl-CoA + CO₂ + NADH
  × 2 per glucose: 2 Acetyl-CoA, 2 CO₂, 2 NADH

Anaerobic (animals, yeast under O₂ deprivation):
  Pyruvate + NADH → Lactate + NAD⁺   (lactate dehydrogenase)
  Purpose: regenerate NAD⁺ so glycolysis can continue
  (NADH from step 6 must be reoxidized — O₂ not available)

Yeast fermentation:
  Pyruvate → Acetaldehyde + CO₂   (pyruvate decarboxylase)
  Acetaldehyde + NADH → Ethanol + NAD⁺  (alcohol dehydrogenase)
```

### PDC — Three Enzymes, Five Cofactors

```
E1 (pyruvate decarboxylase):   cofactor TPP (thiamine pyrophosphate, vitamin B1)
E2 (dihydrolipoyl transacetylase): cofactor lipoic acid + CoA
E3 (dihydrolipoyl dehydrogenase):  cofactor FAD + NAD⁺

Regulation:
  Inhibited by: Acetyl-CoA (product), NADH (product), ATP
  Activated by: CoA, NAD⁺, ADP, pyruvate
  PDC kinase phosphorylates E1 → inactive
  PDC phosphatase dephosphorylates → active
```

---

## TCA Cycle (8 Steps, Mitochondrial Matrix)

Per turn of cycle (= 1 Acetyl-CoA = ½ glucose):

```
         Acetyl-CoA (2C)
              │
              + Oxaloacetate (4C)
              ↓ citrate synthase
         Citrate (6C)
              ↓ aconitase
         Isocitrate (6C)
              ↓ isocitrate dehydrogenase ← [NAD⁺→NADH + CO₂]  regulated by ADP/ATP
         α-Ketoglutarate (5C)
              ↓ α-ketoglutarate dehydrogenase ← [NAD⁺→NADH + CO₂]
         Succinyl-CoA (4C)
              ↓ succinyl-CoA synthetase ← [GDP+Pᵢ→GTP] substrate-level
         Succinate (4C)
              ↓ succinate dehydrogenase ← [FAD→FADH₂] (Complex II!)
         Fumarate (4C)
              ↓ fumarase
         Malate (4C)
              ↓ malate dehydrogenase ← [NAD⁺→NADH]
         Oxaloacetate (4C) ─── regenerated ─── cycle continues

Per turn (per Acetyl-CoA):
  3 NADH,  1 FADH₂,  1 GTP,  2 CO₂

Per glucose (× 2 turns):
  6 NADH,  2 FADH₂,  2 GTP
```

**TCA intermediates as biosynthetic precursors:**
```
α-Ketoglutarate → glutamate → other amino acids
Oxaloacetate → aspartate, glucose (gluconeogenesis)
Citrate → (exported to cytoplasm) → fatty acid synthesis
Succinyl-CoA → heme synthesis
```

---

## Oxidative Phosphorylation

The electron transport chain (ETC) in the inner mitochondrial membrane.
Electrons flow from NADH/FADH₂ through protein complexes to O₂, pumping
protons to create the electrochemical gradient that drives ATP synthesis.

### Oxidative Phosphorylation — Engineering Bridge

Mitchell's chemiosmotic hypothesis (Nobel 1978) describes a machine that any
engineer should find familiar. Strip away the biology and the structure is:

```
ELECTROCHEMICAL GRADIENT AS STORED ENERGY:

  Inner mitochondrial membrane ≈ capacitor / charged battery
  ┌─────────────────────────────────────────────────────┐
  │  Intermembrane space  (high H⁺ — positive terminal) │
  │  ~ +180 mV electrical potential across membrane     │
  │  ~ 1 pH unit ΔpH (0.06 V per pH unit contribution)  │
  │  Total proton-motive force: Δp ≈ 220 mV             │
  ╔═════════════════════════════════════════════════════╗
  ║  Inner mitochondrial membrane (insulator + machine) ║
  ╚═════════════════════════════════════════════════════╝
  │  Matrix  (low H⁺ — negative terminal)               │
  └─────────────────────────────────────────────────────┘

ETC (Complexes I–IV) = pumps building the gradient
  → like charging a battery or compressing a spring
  → NADH/FADH₂ are the "fuel" (oxidized to drive pumping)
  → O₂ is the terminal electron acceptor (the "drain")

ATP synthase (Complex V) = turbine / motor driven by the gradient
  → F₀ c-ring: 8–15 subunits; H⁺ flow drives mechanical rotation
  → F₁ head: α₃β₃γ; γ rotation drives conformational changes
     (binding change mechanism: O → L → T sites cycle, releasing ATP)
  → ~2.7 H⁺ per ATP; ~3 ATP per revolution of c-ring

PARALLEL TO ELECTROCHEMICAL CELLS (05-ELECTROCHEMISTRY.md):
  E°(NADH → O₂) = +1.14 V
  ΔG° = −nFE° = −2 × 96485 × 1.14 = −220 kJ/mol per 2e⁻ pair
  → enough free energy to synthesize ~2.5 ATP
  The ~2.5–3 ATP/NADH efficiency reflects this thermodynamic budget.

PARALLEL TO HYDRAULIC TURBINES:
  Proton gradient (Δp) = hydraulic head
  H⁺ flux through ATP synthase = water flow
  ATP = mechanical work output
  Uncouplers (DNP, FCCP) = bypass bypass — flow without doing work → heat
```

### The Five Complexes

```
Complex I   NADH dehydrogenase (NADH → CoQ)
  NADH + H⁺ + CoQ → NAD⁺ + CoQH₂
  Pumps: 4 H⁺ per NADH (into intermembrane space)
  Contains: FMN + 8–9 Fe-S clusters

Complex II  Succinate dehydrogenase (FADH₂ → CoQ)
  Succinate + CoQ → Fumarate + CoQH₂
  Pumps: 0 H⁺  (no proton pumping — explains lower ATP yield from FADH₂)
  Note: same enzyme as TCA step 6

Complex III  CoQ-cytochrome c reductase (CoQ → cyt c)
  CoQH₂ + 2 cyt c(ox) → CoQ + 2 cyt c(red)
  Pumps: 4 H⁺ per 2e⁻ (Q cycle mechanism)
  Contains: cytochrome b, Rieske Fe-S, cytochrome c₁

Complex IV  Cytochrome c oxidase (cyt c → O₂)
  4 cyt c(red) + O₂ + 4H⁺ → 4 cyt c(ox) + 2H₂O
  Pumps: 4 H⁺ per 4e⁻ (per O₂ reduced)
  Contains: heme a, heme a₃, CuA, CuB

Complex V   ATP synthase
  F₀ subunit: proton channel in membrane (rotary motor, c-ring)
  F₁ subunit: catalytic head in matrix (α₃β₃γ, binding change mechanism)
  H⁺ flow drives c-ring rotation → γ rotation → conformational change → ATP
  ~8 H⁺/revolution (c-ring with 8 subunits), 3 ATP/revolution
  → ~2.7 H⁺/ATP

Mobile electron carriers:
  CoQ (ubiquinone): lipid-soluble, between I/II and III
  Cytochrome c: water-soluble, on outer face of inner membrane, between III and IV
```

### Proton-Motive Force (PMF)

```
Δp = Δψ − (2.303 RT/F) ΔpH     (Mitchell's chemiosmotic hypothesis, 1961)

Δψ ≈ −180 mV (membrane potential, negative inside)
ΔpH ≈ 0.5–1 units (matrix more alkaline)
Total Δp ≈ −200 to −220 mV

Free energy per H⁺: ΔG = F·Δp ≈ 20–21 kJ/mol
Per ATP (at 2.7 H⁺/ATP): ΔG ≈ 54–57 kJ/mol
ΔG of ATP hydrolysis in vivo: ~50–60 kJ/mol  ✓ (well-matched)
```

### ATP Yield Accounting

```
                    NADH      FADH₂      Substrate-level ATP
Glycolysis          2 (cytoplasm) —       2 ATP
PDC                 2          —          —
TCA (×2)            6          2          2 GTP

Mitochondrial NADH: ~2.5 ATP each  (10 NADH × 2.5 = 25 ATP)
FADH₂:             ~1.5 ATP each  (2 FADH₂ × 1.5 = 3 ATP)
Cytoplasmic NADH:  ~1.5 ATP each  (NADH shuttle into mitochondria costs 1 H⁺)
  (malate-aspartate shuttle: 2.5 ATP; glycerol-3-P shuttle: 1.5 ATP — tissue-dependent)

Subtotal from NADH/FADH₂: 25 + 3 + 3 = 31 ATP
Substrate-level:           2 (glycolysis) + 2 (TCA GTP) = 4
Total:                     ~30–32 ATP per glucose

Old textbook value of 36–38 ATP used rounded P/O ratios and ignored transport costs.
Modern mechanistic calculation: 29.85 (P/O = 2.5 for NADH, 1.5 for FADH₂).
```

---

## Gluconeogenesis

Synthesis of glucose from non-carbohydrate precursors. Occurs in liver (mainly), kidney.
Not simply reverse glycolysis — three irreversible glycolytic steps replaced.

```
Glycolysis step 1 (hexokinase): reversed by Glucose-6-phosphatase (liver ER)
Glycolysis step 3 (PFK-1):      reversed by Fructose-1,6-bisphosphatase
Glycolysis step 10 (pyruvate kinase): two steps to bypass:
  Pyruvate → OAA (pyruvate carboxylase, uses ATP + CO₂, requires biotin)
  OAA → PEP (PEPCK, uses GTP)

Precursors:
  Glucogenic amino acids (most AA) → pyruvate, OAA, α-KG, succinate, fumarate
  Lactate (Cori cycle: muscle → liver → glucose → muscle)
  Glycerol (from triglyceride breakdown) → DHAP
  Propionate (odd-chain fatty acid) → succinyl-CoA → OAA

Regulation (reciprocal with glycolysis):
  High glucagon/low insulin → activate gluconeogenesis
  F-2,6-BP low → FBPase-1 active (gluconeogenesis); PFK-1 inactive (glycolysis)
  Acetyl-CoA activates pyruvate carboxylase (feeds substrate into gluconeogenesis)
```

---

## β-Oxidation of Fatty Acids

```
Fatty acid activation: FA + CoA + ATP → Fatty acyl-CoA + AMP + PPᵢ  (cytoplasm)
Transport into matrix: carnitine shuttle (acyl-carnitine through inner membrane)

β-Oxidation (4 steps per cycle, matrix):
  1. Acyl-CoA dehydrogenase:    Acyl-CoA + FAD → Trans-Δ²-enoyl-CoA + FADH₂
  2. Enoyl-CoA hydratase:       + H₂O → 3-L-Hydroxyacyl-CoA
  3. 3-Hydroxyacyl-CoA dehydrogenase: + NAD⁺ → 3-Ketoacyl-CoA + NADH
  4. Thiolase:                  + CoA → Acyl-CoA (shortened by 2C) + Acetyl-CoA

Per cycle: 1 FADH₂ + 1 NADH + 1 Acetyl-CoA (enters TCA)

Palmitate (C16:0) example:
  7 cycles of β-oxidation → 8 Acetyl-CoA, 7 NADH, 7 FADH₂
  ATP: 8 × 10 (TCA/OxPhos per Acetyl-CoA) + 7 × 2.5 + 7 × 1.5 = 108 ATP
  Cost: 2 ATP (activation) → Net: 106 ATP per palmitate

Vs glucose (C16 equiv ≈ 2.3 glucose): ~72 ATP → fat gives ~50% more ATP/carbon
Fat: ~37 kJ/g stored energy vs carbohydrate/protein: ~17 kJ/g
```

---

## Pentose Phosphate Pathway (PPP)

Parallel to glycolysis; two phases:

```
OXIDATIVE PHASE (irreversible):
  G6P + 2 NADP⁺ + H₂O → Ribulose-5-P + 2 NADPH + CO₂
  Enzyme: G6P dehydrogenase (rate-limiting)
  Purpose: generate NADPH for reductive biosynthesis + antioxidant defense

NONOXIDATIVE PHASE (reversible):
  Ribulose-5-P → Ribose-5-P (for nucleotide synthesis)
  Or: interconvert C3-C7 sugars, feed back into glycolysis

Key outputs:
  NADPH: fatty acid synthesis, cholesterol synthesis, glutathione reduction,
         cytochrome P450, NADPH oxidase (immune)
  Ribose-5-P: nucleotide and nucleic acid biosynthesis

G6PD deficiency (X-linked, most common enzyme defect in humans):
  Red blood cells: no mitochondria → PPP is only NADPH source
  → oxidative stress → hemolysis → favism (broad beans contain oxidants)
  Protective against P. falciparum malaria → high frequency in malaria zones
```

---

## Metabolic Integration — Regulatory Logic

```
ENERGY CHARGE = ([ATP] + ½[ADP]) / ([ATP] + [ADP] + [AMP])
  Range: 0 (depleted) to 1 (fully charged)
  Normal cells: ~0.8–0.9
  High EC → inhibit catabolism, activate anabolism
  Low EC → activate catabolism, inhibit anabolism

KEY REGULATORY ENZYMES AND SIGNALS:

Enzyme           Activated by          Inhibited by
──────────────────────────────────────────────────────────────
Hexokinase       —                     G6P (product)
PFK-1            AMP, ADP, F-2,6-BP    ATP, citrate
Pyruvate kinase  F-1,6-BP              ATP, Ala
PDC              ADP, NAD⁺, CoA        ATP, NADH, Acetyl-CoA
Isocitrate DH    ADP, Ca²⁺             ATP, NADH
Citrate synthase —                     ATP, NADH, Succinyl-CoA
Pyruvate         Acetyl-CoA,           ADP
  carboxylase    ATP

HORMONAL CONTROL:
  Glucagon (liver):  ↑ cAMP → PKA → activate glycogenolysis, gluconeogenesis
                                    → inhibit glycolysis, glycogen synthesis
  Insulin (all tissues): ↑ PI3K/Akt → activate glucose uptake, glycolysis, lipogenesis
                                      → inhibit gluconeogenesis
  Epinephrine (muscle+liver): ↑ cAMP → same as glucagon + activates glycogenolysis
```

---

## Decision Cheat Sheet

| Question | Concept | Answer |
|----------|---------|--------|
| Where is glycolysis regulated? | PFK-1 | Main committed step; ATP inhibits, AMP activates |
| Why can't fatty acids make glucose? | Acetyl-CoA → OAA bypass | Acetyl-CoA enters TCA but both carbons lost as CO₂ |
| Why does FADH₂ yield less ATP than NADH? | Complex II | FADH₂ enters at Complex II (no proton pumping) |
| Why does the brain need glucose? | Fuel specificity | Can't use fatty acids (can't cross BBB); uses ketones during starvation |
| Why is lactate produced during sprinting? | Anaerobic → NAD⁺ limit | O₂ delivery insufficient; LDH regenerates NAD⁺ |
| What is the Cori cycle? | Lactate shuttle | Muscle lactate → liver → glucose → muscle |
| Why is gluconeogenesis not reverse glycolysis? | 3 irreversible steps | Need pyruvate carboxylase, PEPCK, G6Pase |
| What does NADPH do? | Reductive power | Biosynthesis + antioxidant (GSH reduction) |
| Why is fat better stored fuel than carbohydrate? | Carbon oxidation state | Fats more reduced → more electrons → more ATP |

---

## Common Confusion Points

**ATP yield "36 ATP" is outdated**
Old textbooks: 36–38 ATP (used integer P/O ratios of 3 and 2).
Modern mechanistic values: P/O = 2.5 (NADH), 1.5 (FADH₂) → ~30 ATP total.
Real cells: lower still (~25–28) due to proton leak, transport costs, variable efficiency.
The number is approximate and context-dependent — the mechanism matters.

**Fatty acids cannot make net glucose**
Acetyl-CoA (from β-oxidation) can enter TCA but loses both carbons as CO₂.
No net carbon enters the gluconeogenic pathway from even-chain fatty acids.
Exception: odd-chain fatty acids → propionyl-CoA → succinyl-CoA → OAA → glucose.
Glycerol from fat breakdown CAN make glucose (glycerol → DHAP).

**NADH and NADPH are not interchangeable**
NADH: catabolic carrier (glycolysis, TCA) → goes to ETC → ATP
NADPH: anabolic carrier (PPP) → goes to biosynthesis and antioxidant defense
The cell maintains separate pools at different redox potentials.
Transhydrogenase can interconvert them but at an energy cost.

**PDC is in the matrix, not cytoplasm**
Pyruvate must be transported into the mitochondrial matrix (MPC — mitochondrial
pyruvate carrier) before PDC acts. Inhibiting this transport is a regulatory point
and a target in cancer metabolism (Warburg effect exploits cytoplasmic pyruvate).

**Substrate-level phosphorylation ≠ oxidative phosphorylation**
Substrate-level: direct transfer of phosphate from metabolite to ADP (steps 7, 10 glycolysis; succinyl-CoA synthetase). No membrane, no gradient.
Oxidative phosphorylation: proton gradient drives ATP synthase. The dominant source.
Both produce ATP but by completely different mechanisms.
