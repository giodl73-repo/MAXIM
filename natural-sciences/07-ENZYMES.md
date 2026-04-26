# 07-ENZYMES — Enzyme Kinetics & Catalysis

> Michaelis-Menten derivation, inhibition types, allostery, covalent modification.
> How biology achieves 10⁶–10¹⁷-fold rate enhancements while remaining
> precisely regulated.

---

## Landscape

```
┌────────────────────────────────────────────────────────────────────┐
│                        ENZYMOLOGY                                  │
│                                                                      │
│  CATALYSIS FUNDAMENTALS                                            │
│  ─────────────────────────                                         │
│  Lower ΔG‡ (both ΔH‡ and ΔS‡)     Rate enhancement 10⁶–10¹⁷      │
│  Proximity / orientation            Does NOT change K or ΔG_rxn    │
│  Electrostatic TS stabilization     EC number classification       │
│          │                                                           │
│          ▼                                                           │
│  MICHAELIS-MENTEN KINETICS                                         │
│  ──────────────────────────                                        │
│  E + S ⇌ ES → E + P               v₀ = Vmax[S]/(Km + [S])          │
│  kcat (turnover), Km (half-sat)    kcat/Km = catalytic efficiency  │
│  Lineweaver-Burk linearization                                     │
│          │                                                           │
│     ┌────┴──────────────────────────┐                              │
│     ▼                               ▼                               │
│  INHIBITION                      ALLOSTERIC REGULATION             │
│  ──────────                      ───────────────────                │
│  Competitive (↑Km, Vmax same)    Hill equation (n > 1 = sigmoidal) │
│  Uncompetitive (both ↓, parallel) MWC T⇌R model                   │
│  Noncompetitive (↓Vmax, Km same)  Hemoglobin / Bohr effect         │
│          │                                                           │
│          ▼                                                           │
│  COVALENT REGULATION                                                │
│  ─────────────────────                                              │
│  Phosphorylation (kinase/phosphatase)   Irreversible: proteolytic  │
│  Cascade amplification (10⁸ glucose/min) activation (zymogens)    │
│  Acetylation, ubiquitination, glycosylation                        │
└────────────────────────────────────────────────────────────────────┘
```

---

## Enzyme as Catalyst — The Core Idea

```
Without enzyme:    A → [TS‡_uncatalyzed] → B    rate = k_uncat
With enzyme:       A → [ES‡] → B               rate = k_cat >> k_uncat

Enzyme does NOT:
  × change ΔG of reaction (substrate and product energies unchanged)
  × change equilibrium constant K
  × get consumed

Enzyme DOES:
  ✓ lower activation energy ΔG‡ (provides alternative pathway)
  ✓ lower both ΔH‡ AND ΔS‡ (pre-organizes reactants)
  ✓ achieve rate enhancement 10⁶–10¹⁷ over uncatalyzed

Strategies:
  Proximity + orientation  →  reduce −ΔS‡ (entropy cost of bringing reactants together)
  Electrostatic stabilization of TS  →  reduce ΔH‡
  Covalent intermediates  →  split TS into two lower barriers
  Metal ion catalysis  →  Lewis acid, redox, geometric templating
  General acid/base  →  His, Asp, Glu, Cys as proton donors/acceptors
```

---

## Michaelis-Menten Kinetics

### The Model

```
E + S ⇌ ES → E + P
    k₁  k₋₁   k₂(= kcat)

Assumptions:
  1. [S] >> [E]total  (substrate in large excess)
  2. Steady state: d[ES]/dt ≈ 0  (ES forms and breaks down at equal rates)
  3. Measure initial rate v₀ (before significant P accumulates, reverse negligible)
```

### Derivation

```
d[ES]/dt = k₁[E][S] − k₋₁[ES] − kcat[ES] = 0

[E]free = [E]total − [ES]

k₁([E]total − [ES])[S] = (k₋₁ + kcat)[ES]

Define:  Km = (k₋₁ + kcat) / k₁   (Michaelis constant, units: M)

[ES] = [E]total[S] / (Km + [S])

v₀ = kcat[ES] = kcat[E]total[S] / (Km + [S])

Define:  Vmax = kcat[E]total

────────────────────────────────────────────────────────
         Vmax · [S]
v₀  =  ─────────────    MICHAELIS-MENTEN EQUATION
          Km + [S]
────────────────────────────────────────────────────────
```

### Physical Meaning of Parameters

```
Vmax:  maximum rate at saturating [S]; all enzyme is bound as ES
       Vmax = kcat · [E]total
       Units: M·s⁻¹ (or µM·min⁻¹, etc.)

kcat:  catalytic rate constant ("turnover number")
       = max number of substrate molecules converted per enzyme molecule per second
       Typical values: 1–10,000 s⁻¹
       Carbonic anhydrase: kcat = 10⁶ s⁻¹ (diffusion-limited)

Km:    [S] at which v₀ = Vmax/2
       Approximate measure of enzyme–substrate affinity
       Low Km → tight binding → enzyme saturates at low [S]
       High Km → weak binding → need high [S] for saturation
       NOT exactly Kd unless k₋₁ >> kcat (equilibrium assumption)

kcat/Km:  catalytic efficiency  (second-order rate constant for E + S → P)
          Units: M⁻¹s⁻¹
          Theoretical maximum: diffusion limit ~10⁸–10⁹ M⁻¹s⁻¹
          "Catalytically perfect" enzymes: kcat/Km ≈ 10⁸–10⁹ M⁻¹s⁻¹
          (acetylcholinesterase, catalase, triose phosphate isomerase)
```

### Michaelis-Menten Curve

```
v₀
│
Vmax ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
         /
Vmax/2 ─ ─ ─ ─ /
       /
      /
     /
────┼─────────────────────── [S]
    0    Km

At [S] = Km:    v₀ = Vmax/2
At [S] << Km:   v₀ ≈ (kcat/Km)[E]·[S]   (first order in [S])
At [S] >> Km:   v₀ ≈ Vmax               (zero order in [S], saturated)
```

---

## Lineweaver-Burk (Double Reciprocal) Plot

Linearizes Michaelis-Menten for graphical parameter extraction:

```
1/v₀ = (Km/Vmax)·(1/[S]) + 1/Vmax

Plot 1/v₀ vs 1/[S]:
  Slope     = Km/Vmax
  y-intercept = 1/Vmax   →  Vmax = 1/y-intercept
  x-intercept = −1/Km    →  Km = −1/x-intercept

Disadvantage: compresses high [S] data points, amplifies low [S] error
Better for modern work: nonlinear regression directly on v₀ vs [S]
Lineweaver-Burk still useful for: visualizing inhibition type
```

---

## Enzyme Inhibition

### Competitive Inhibition

Inhibitor (I) binds only to free enzyme (same site as S, or overlapping):

```
E + I ⇌ EI    (dead-end complex, no product)
Ki = [E][I]/[EI]  (inhibitor dissociation constant)

Effect on kinetics:
  Vmax:  UNCHANGED  (at infinite [S], I can be outcompeted)
  Km:    INCREASES  (apparent Km = Km(1 + [I]/Ki))
  Km_app = Km · α    where α = 1 + [I]/Ki > 1

Lineweaver-Burk:
  Lines intersect on y-axis (same Vmax, different slopes/x-intercepts)

Examples:
  Statins → HMG-CoA reductase (competitive with HMG-CoA)
  Methotrexate → dihydrofolate reductase (very tight competitive)
  Sulfanilamide → DHPS (competitive with p-aminobenzoate) — first antibiotic
```

### Uncompetitive Inhibition

Inhibitor binds only to ES complex (not free E):

```
ES + I ⇌ ESI    (dead-end ternary complex)
Ki' = [ES][I]/[ESI]

Effect:
  Vmax:  DECREASES  (Vmax_app = Vmax/α')  where α' = 1 + [I]/Ki'
  Km:    DECREASES  (Km_app = Km/α')      (paradoxically — more ES trapped)
  kcat/Km: UNCHANGED

Lineweaver-Burk: parallel lines (same slope, different intercepts)

More common in multi-substrate reactions. Rare for single-substrate.
```

### Noncompetitive Inhibition

Inhibitor binds both E and ES (at allosteric site, does not block substrate binding):

```
E + I ⇌ EI    (Ki)
ES + I ⇌ ESI  (Ki' = Ki, pure noncompetitive)

Effect:
  Vmax:  DECREASES  (Vmax_app = Vmax/α)
  Km:    UNCHANGED  (substrate still binds normally to E)
  kcat/Km: DECREASES

Lineweaver-Burk: lines intersect on x-axis (same Km, different Vmax)

Mixed inhibition: Ki ≠ Ki' → lines intersect left of y-axis, not on x-axis
```

### Summary Table

```
Inhibition type   Km_app        Vmax_app      LB plot intersection
─────────────────────────────────────────────────────────────────
Competitive       ↑ (× α)       unchanged     on y-axis
Uncompetitive     ↓ (÷ α')      ↓ (÷ α')      parallel lines
Noncompetitive    unchanged     ↓ (÷ α)       on x-axis
Mixed             changes       ↓             left of y-axis
```

---

## Allosteric Regulation

### The Problem with Michaelis-Menten for Allosteric Enzymes

Allosteric enzymes are multi-subunit. Substrate binding to one subunit
changes affinity in other subunits (cooperativity). They do NOT follow
simple hyperbolic Michaelis-Menten kinetics.

### Hill Equation

```
v₀ = Vmax · [S]^n / (K₀.₅ⁿ + [S]^n)

n = Hill coefficient (cooperativity)
  n = 1: no cooperativity (Michaelis-Menten)
  n > 1: positive cooperativity (O₂ binding to hemoglobin, n ≈ 2.8)
  n < 1: negative cooperativity (unusual)
K₀.₅ = [S] at v₀ = Vmax/2 (replaces Km for allosteric enzymes)

Sigmoidal v₀ vs [S] curve for n > 1:
  Shallow response at low [S] → steep "switch-like" response near K₀.₅
  → digital/switch-like behavior useful for metabolic control
```

### MWC (Monod-Wyman-Changeux) Model

```
Two states: T (tense, low affinity) ⇌ R (relaxed, high affinity)

Equilibrium: L₀ = [T]/[R]  (large → T dominates in absence of ligand)
Cooperative binding: first ligand shifts T→R, subsequent bindings increasingly likely

Activators: bind R → shift T→R → lower K₀.₅ (left shift)
Inhibitors: bind T → shift R→T → raise K₀.₅ (right shift)

Example: ATCase (aspartate transcarbamoylase)
  Activated by ATP (energy available → make pyrimidines)
  Inhibited by CTP (end product → feedback inhibition)
  Classic example of allosteric feedback in biosynthetic pathway
```

### Hemoglobin — The Model Allosteric Protein

```
O₂ binding: α₂β₂ tetramer, 4 heme groups
  T state (deoxy): low O₂ affinity, salt bridges between subunits
  R state (oxy):   high O₂ affinity, T→R triggered by first O₂ binding

Bohr effect: CO₂ and H⁺ stabilize T state → lower O₂ affinity
  At tissues: high CO₂, low pH → T state → releases O₂
  At lungs: low CO₂, high pH → R state → binds O₂
  Physiological logic: deliver O₂ where metabolism is active

2,3-BPG (2,3-bisphosphoglycerate): binds T state of hemoglobin
  → stabilizes T → right-shifts O₂ binding curve → facilitates O₂ release
  High altitude adaptation: 2,3-BPG increases → better O₂ delivery to tissues
  Fetal hemoglobin (γ subunits): lower 2,3-BPG affinity → higher O₂ affinity → extracts O₂ from maternal blood
```

---

## Covalent Modification and Regulation

### Phosphorylation

Most common reversible covalent modification:

```
Kinase: ATP + Enzyme−OH → Enzyme−OPO₃²⁻ + ADP   (add phosphate)
Phosphatase: Enzyme−OPO₃²⁻ + H₂O → Enzyme−OH + Pᵢ  (remove)

Targets: Ser, Thr (most common), Tyr (signal transduction)
Effect: can activate OR inactivate (depends on enzyme)

Example: glycogen phosphorylase
  Phosphorylated form (a): ACTIVE  → breaks down glycogen
  Dephosphorylated form (b): INACTIVE
  Triggered by glucagon/epinephrine → cAMP → PKA → phosphorylates phosphorylase

Phosphorylation cascade amplification:
  1 hormone → 1 GPCR → many Gα → many adenylyl cyclase → many cAMP
  → many PKA → many phosphorylase kinase → many phosphorylase → 10⁸ glucose/min
```

### Proteolytic Activation (Zymogens)

Enzymes synthesized as inactive precursors (zymogens), activated by cleavage:

```
Trypsinogen → trypsin (cleavage by enterokinase, then autocatalytic)
Chymotrypsinogen → chymotrypsin
Pepsinogen → pepsin (acid-activated in stomach)
Proinsulin → insulin (C-peptide cleaved in secretory granules)
Blood clotting cascade: all factors as zymogens → activated sequentially
Caspases: procaspases activated in apoptosis cascade

Why zymogens?
  Protects cells from premature enzymatic activity (pancreatic proteases)
  Allows irreversible activation as a signaling event
  Concentrates active enzyme at site of need
```

### Other Covalent Modifications

| Modification | Residue | Function |
|-------------|---------|----------|
| Phosphorylation | Ser, Thr, Tyr | On/off switch, signaling |
| Acetylation | Lys (N-terminus) | Histone regulation, stability |
| Ubiquitination | Lys | Proteasomal degradation signal |
| Methylation | Lys, Arg | Histone code, epigenetics |
| Glycosylation | Asn (N-linked), Ser/Thr (O-linked) | Folding, recognition, stability |
| Myristoylation | N-terminal Gly | Membrane anchoring |
| SUMOylation | Lys | Nuclear localization, transcription |

---

## Enzyme Classes (EC Numbers)

```
EC 1  Oxidoreductases    Transfer electrons (oxidation/reduction)
      Examples: dehydrogenases, oxidases, peroxidases, reductases

EC 2  Transferases       Transfer chemical groups (except electrons)
      Examples: kinases (phosphate), transaminases (amino), methyltransferases

EC 3  Hydrolases         Bond cleavage using water
      Examples: proteases, lipases, phosphatases, nucleases, glycosidases

EC 4  Lyases             Bond cleavage WITHOUT water (addition or elimination)
      Examples: decarboxylases, dehydratases, synthases (non-ATP using)

EC 5  Isomerases         Intramolecular rearrangements
      Examples: racemases, epimerases, mutases, isomerases

EC 6  Ligases            Bond formation coupled to ATP hydrolysis
      Examples: synthetases, carboxylases, DNA ligase
      (Note: "synthase" ≠ "synthetase" — synthetase uses ATP)

EC 7  Translocases       Ion pumps, transport ATPases (added 2018)
      Examples: Na⁺/K⁺-ATPase, ABC transporters
```

---

## Decision Cheat Sheet

| Question | Concept | Key indicator |
|----------|---------|--------------|
| Does inhibitor change Vmax? | Inhibition type | Competitive: no; noncompetitive: yes |
| Does inhibitor change Km? | Inhibition type | Competitive: yes; noncompetitive: no |
| Lineweaver-Burk lines parallel — which inhibition? | Uncompetitive | Same slope = Km/Vmax unchanged |
| Why is kcat/Km the key efficiency metric? | Second-order kinetics | At low [S], v₀ = (kcat/Km)[E][S] |
| Sigmoidal v₀ vs [S] curve — what does it mean? | Cooperativity | n > 1 in Hill equation, allosteric enzyme |
| Why does 2,3-BPG decrease O₂ affinity? | Allosteric T-state stabilization | BPG binds T → shifts equilibrium → less R |
| What does a high Km mean? | Weak binding | Need high [S] to saturate; enzyme has low affinity |
| How does phosphorylation regulate enzymes? | Covalent modification | Adds −2 charge; changes conformation; on or off |
| What's the difference between synthase and synthetase? | EC nomenclature | Synthetase uses ATP; synthase does not |

---

## Common Confusion Points

**Km ≠ Kd (binding constant)**
Km = (k₋₁ + kcat)/k₁. It equals Kd only if kcat << k₋₁ (equilibrium assumption).
For efficient enzymes where kcat ≈ k₋₁, Km > Kd. Km is an operational parameter
(half-saturation concentration), not a thermodynamic binding affinity.

**Competitive inhibitor always outcompeted at infinite [S] — but infinite [S] is impractical**
In cells, [S] is rarely >> Km. At physiological concentrations, competitive inhibitors
are highly effective. Drugs that are competitive inhibitors work because cellular
substrate concentrations are finite and near Km.

**Vmax depends on [E]total — it is not an intrinsic enzyme property**
kcat (turnover number) is intrinsic. Vmax = kcat × [E]total. If you double enzyme
concentration, Vmax doubles. When comparing enzymes: compare kcat and kcat/Km,
not Vmax values measured at different enzyme concentrations.

**Allosteric enzymes violate Michaelis-Menten assumptions**
Michaelis-Menten assumes a single ES complex and independent binding sites.
Allosteric enzymes have multiple subunits with cooperative binding — they require
Hill or MWC models. Applying Michaelis-Menten to allosteric enzymes gives
apparent Km values that have no physical meaning.

**Noncompetitive inhibition is rare in simple one-substrate enzymes**
True noncompetitive inhibition (affects only Vmax) requires the inhibitor to bind
equally well to E and ES. This is unusual because binding ES usually affects the
active site. Most "noncompetitive" inhibitors in practice are mixed.
