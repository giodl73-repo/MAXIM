<!-- @editor[diagram/P2]: Opening comparison table (thermo vs kinetics) is useful but not a landscape diagram — doesn't show how rate laws, Arrhenius, TST, mechanisms, and catalysis relate to each other as a system. Consider a visual map: experimental observables → rate law → mechanism → theory (collision, TST) → catalysis. -->
# 04-KINETICS — Chemical Kinetics

> Rate laws, integrated equations, Arrhenius, transition state theory, mechanisms,
> catalysis, and radical chain reactions. Thermodynamics tells you *if*;
> kinetics tells you *how fast* and *by what path*.

---

## The Central Question

```
THERMODYNAMICS                 KINETICS
──────────────────────────────────────────────────────────
ΔG < 0 ?                       k = ?  (rate constant)
Will reaction occur?           How fast will it occur?
Path-independent               Path-dependent
State functions (H, S, G)      Activation barrier (Ea, ΔG‡)
Equilibrium position           Mechanism, intermediates
Answer: yes/no/maybe           Answer: seconds, years, never

Both required for full picture.
Diamond → graphite: ΔG < 0 (thermodynamics says yes),
                    k ≈ 0 at 298 K (kinetics says never in practice).
```

---

## Rate Laws

### Empirical Rate Law

Rate = k · [A]^m · [B]^n · …

- **m, n**: reaction orders (integers or fractions — determined experimentally, not from stoichiometry)
- **k**: rate constant (units depend on overall order)
- **Overall order**: m + n + …

```
Units of k:
  Zero order:    mol·L⁻¹·s⁻¹
  First order:   s⁻¹
  Second order:  L·mol⁻¹·s⁻¹
  nth order:     L^(n-1)·mol^(1-n)·s⁻¹
```

**Critical point**: reaction orders are NOT determined by stoichiometric coefficients
unless the reaction is elementary. For A + 2B → C, rate could be k[A][B]², or k[A],
or k[A]²[B]⁰ — must be measured.

### The Method of Initial Rates

```
Experiment 1:  [A]₀ = 0.10 M,  [B]₀ = 0.10 M,  rate₁ = 1.5 × 10⁻³ M/s
Experiment 2:  [A]₀ = 0.20 M,  [B]₀ = 0.10 M,  rate₂ = 3.0 × 10⁻³ M/s
Experiment 3:  [A]₀ = 0.10 M,  [B]₀ = 0.20 M,  rate₃ = 1.5 × 10⁻³ M/s

Exps 1→2: double [A], rate doubles → m = 1  (first order in A)
Exps 1→3: double [B], rate unchanged → n = 0  (zero order in B)

rate = k[A]¹[B]⁰ = k[A]
k = rate / [A] = 1.5 × 10⁻³ / 0.10 = 0.015 s⁻¹
```

---

## Integrated Rate Laws

### Zero Order

```
Rate = k                d[A]/dt = −k

[A] = [A]₀ − kt        (linear in time)
Half-life: t₁/₂ = [A]₀ / 2k    (depends on initial concentration)

Diagnostic: plot [A] vs t → straight line
```

### First Order

```
Rate = k[A]             d[A]/dt = −k[A]

[A] = [A]₀ · e^(−kt)   (exponential decay)
ln[A] = ln[A]₀ − kt

Half-life: t₁/₂ = ln 2 / k = 0.693 / k    (INDEPENDENT of [A]₀)

Diagnostic: plot ln[A] vs t → straight line (slope = −k)

Examples:
  Radioactive decay (first order by definition)
  First-order drug elimination (pharmacokinetics)
  SN1 reactions (rate-limiting step: carbocation formation)
```

### Second Order (in one reactant)

```
Rate = k[A]²            d[A]/dt = −k[A]²

1/[A] = 1/[A]₀ + kt

Half-life: t₁/₂ = 1 / (k·[A]₀)    (depends on [A]₀)

Diagnostic: plot 1/[A] vs t → straight line (slope = k)
```

### Summary Table

```
Order  Rate law    Integrated          Plot      t₁/₂
──────────────────────────────────────────────────────────────
0      k           [A] = [A]₀ − kt    [A] vs t  [A]₀/2k
1      k[A]        ln[A] = ln[A]₀−kt  ln[A] vs t  0.693/k
2      k[A]²       1/[A] = 1/[A]₀+kt  1/[A] vs t  1/(k[A]₀)
```

---

## Arrhenius Equation — Temperature Dependence

```
k = A · e^(−Ea/RT)

A  = pre-exponential (frequency) factor  — collision frequency × steric factor
Ea = activation energy (J/mol)
R  = 8.314 J/(mol·K)
T  = temperature (K)

Linearized:
  ln k = ln A − Ea/(RT)
  plot ln k vs 1/T → slope = −Ea/R,  intercept = ln A

Two-temperature form:
  ln(k₂/k₁) = −(Ea/R) · (1/T₂ − 1/T₁)

Rule of thumb: rate doubles per 10°C rise (for Ea ≈ 50 kJ/mol near 25°C)
```

```
REACTION COORDINATE DIAGRAM:

Energy
  │          ‡ (transition state)
  │         /│\
  │        / │ \
  │       /  │  \           Ea (forward)  = activation energy
  │      /   │   \          Ea (reverse)  = Ea − ΔH°rxn
  │─────/    │    \─────    ΔH°rxn = Ea(fwd) − Ea(rev)
  │  reactants     products
  │
  └──────────────────────── Reaction coordinate
```

---

## Collision Theory

Arrhenius factor A has physical content:

```
k = Z · p · e^(−Ea/RT)

Z = collision frequency = σ_AB · N_A · n_A · n_B · √(8k_BT / πμ)
    (from kinetic theory: σ_AB = collision cross-section, μ = reduced mass)

p = steric factor (0 < p ≤ 1)
    fraction of collisions with correct orientation
    e.g., p = 0.01 for reactions requiring precise alignment

Problem: collision theory predicts A poorly for complex molecules.
Better framework: transition state theory.
```

---

## Transition State Theory (Eyring Equation)

More rigorous: the transition state (‡) is treated as a quasi-equilibrium species.

```
k = (k_B · T / h) · K‡ · e^(−ΔG‡/RT)

Simplified Eyring equation:
  k = (k_B T / h) · exp(−ΔG‡/RT)
  k = (k_B T / h) · exp(ΔS‡/R) · exp(−ΔH‡/RT)

k_B = 1.38 × 10⁻²³ J/K,   h = 6.63 × 10⁻³⁴ J·s
k_BT/h at 298 K = 6.25 × 10¹² s⁻¹  (universal frequency factor)

Components:
  ΔH‡ ≈ Ea − RT  (activation enthalpy ≈ activation energy)
  ΔS‡ = activation entropy (negative for bimolecular: order decreases at TS)
  ΔG‡ = ΔH‡ − TΔS‡  (activation free energy)
```

**Why TST matters**: separates enthalpic barrier (bond breaking/forming geometry)
from entropic penalty (rigidity, orientation requirements at transition state).
Enzymes work largely by reducing both ΔH‡ and |ΔS‡| (pre-organizing substrate).

```
Activation parameters from Eyring plot:
  ln(k/T) vs 1/T → slope = −ΔH‡/R, intercept = ln(k_B/h) + ΔS‡/R
```

---

## Reaction Mechanisms

### Elementary Steps

An elementary step is one that occurs exactly as written (no intermediates).
For elementary steps ONLY: rate order = stoichiometric coefficient.

```
Unimolecular:   A → products        rate = k[A]          (first order)
Bimolecular:    A + B → products    rate = k[A][B]        (second order)
Termolecular:   A + B + C → ...     rate = k[A][B][C]     (rare, third order)
```

Molecularity (# species in elementary step) ≠ overall order (from experiment).

### Rate-Determining Step (RDS)

The slowest step governs the overall rate.

```
Example: NO₂(g) + CO(g) → NO(g) + CO₂(g)  (observed: rate = k[NO₂]²)

Proposed mechanism:
  Step 1 (slow): NO₂ + NO₂ → NO₃ + NO         rate₁ = k₁[NO₂]²
  Step 2 (fast): NO₃ + CO → NO₂ + CO₂         rate₂ = k₂[NO₃][CO]

Overall rate = rate₁ = k₁[NO₂]²     ✓ matches experiment
NO₃ is a reactive intermediate (formed and consumed, not in net equation)
```

### Steady-State Approximation (SSA)

For reactive intermediates, assume d[intermediate]/dt ≈ 0:

```
Mechanism:
  A ⇌ B        (k₁ forward, k₋₁ reverse — fast)
     ↓ k₂
     C          (slow)

SSA on B:
  d[B]/dt = k₁[A] − k₋₁[B] − k₂[B] = 0
  [B]_ss = k₁[A] / (k₋₁ + k₂)

Overall rate = k₂[B]_ss = k₁k₂[A] / (k₋₁ + k₂)

Two limits:
  k₂ >> k₋₁:  rate = k₁[A]          (step 1 is RDS)
  k₂ << k₋₁:  rate = (k₁k₂/k₋₁)[A] (step 2 is RDS, pre-equilibrium applies)
```

### Pre-Equilibrium Approximation

When fast equilibrium precedes slow step:

```
A + B ⇌ C    (fast, K = k₁/k₋₁)
C → D        (slow, k₂)

K = [C]/([A][B])  →  [C] = K[A][B]
rate = k₂[C] = k₂K[A][B] = k_obs[A][B]

Michaelis-Menten enzyme kinetics is the biochemical analog:
  E + S ⇌ ES (fast) → E + P (slow)  → rate = Vmax[S]/(Km + [S])
  (see 07-ENZYMES.md for full treatment)
```

---

## Catalysis

A catalyst provides an alternative pathway with lower Ea.
It does NOT change ΔG, ΔH, or K — only kinetics.

```
Without catalyst:
  A → [TS‡] → B     Ea = 200 kJ/mol,  k = 10⁻¹⁰ s⁻¹

With catalyst:
  A → [TS‡_cat] → B  Ea = 80 kJ/mol,   k = 10³ s⁻¹

Rate ratio ~ 10¹³ — 13 orders of magnitude from 120 kJ/mol reduction in Ea
```

### Homogeneous Catalysis

Catalyst in same phase as reactants.

```
Acid catalysis: H⁺ protonates substrate → lowers Ea for bond breaking
  Example: ester hydrolysis in HCl(aq)

Transition metal complexes:
  Wilkinson's catalyst: RhCl(PPh₃)₃  →  olefin hydrogenation
  Mechanism: oxidative addition → migratory insertion → reductive elimination
```

### Heterogeneous Catalysis

Catalyst in different phase. Reactants adsorb on surface.

```
Langmuir-Hinshelwood mechanism (both reactants adsorb):
  A(g) ⇌ A(ads)
  B(g) ⇌ B(ads)
  A(ads) + B(ads) → products

Eley-Rideal mechanism (one reactant from gas phase):
  A(g) ⇌ A(ads)
  A(ads) + B(g) → products

Industrial examples:
  Haber-Bosch (N₂ + 3H₂ → 2NH₃): Fe catalyst, 400–500°C, 150–300 atm
  Fischer-Tropsch (CO + H₂ → hydrocarbons): Fe or Co catalyst
  Catalytic converter (CO + O₂, NOₓ reduction): Pt/Pd/Rh on CeO₂/Al₂O₃

Poisoning: CO blocks Pt surface (strong adsorption, no vacant sites)
Promoters: K₂O on Fe increases N₂ adsorption in Haber process
```

### Enzyme Catalysis (Preview)

```
Rate enhancement: 10⁶ – 10¹⁷ over uncatalyzed reaction
Mechanism: lowers ΔH‡ AND ΔS‡
  → Proximity/orientation effect (reduces −ΔS‡)
  → Electrostatic stabilization of TS
  → Covalent intermediates (serine proteases, coenzyme A)
  → Metal ion catalysis
Full treatment: 07-ENZYMES.md
```

---

## Chain Reactions

Radical chain mechanisms: initiation → propagation (repeated) → termination.

```
H₂ + Cl₂ → 2HCl   (chain reaction — quantum yield up to 10⁶)

INITIATION:
  Cl₂ + hν → 2 Cl•           (photochemical — or thermal)

PROPAGATION (repeats ~10⁶ times):
  Cl• + H₂ → HCl + H•
  H•  + Cl₂ → HCl + Cl•

TERMINATION:
  Cl• + Cl• → Cl₂    (wall or third-body recombination)
  H•  + Cl• → HCl
  H•  + H•  → H₂

Chain length = propagation steps per initiation event
Inhibitors terminate chains: ROOR peroxides, NO, antioxidants
```

**Atmospheric relevance**: ozone depletion is a chain reaction.
Cl• (from CFC photolysis) catalytically destroys O₃:
```
  Cl• + O₃ → ClO• + O₂
  ClO• + O → Cl• + O₂       (net: O₃ + O → 2O₂, Cl• regenerated)
  One Cl• destroys ~100,000 O₃ molecules
```

---

## Decision Cheat Sheet

| Question | Concept | Key tool |
|----------|---------|----------|
| What is the rate law? | Must measure — not from stoichiometry | Method of initial rates |
| Does rate double with temperature? | Arrhenius | Rule of thumb for Ea ≈ 50 kJ/mol |
| Why do enzymes work? | TST: lower ΔH‡ AND ΔS‡ | Eyring equation components |
| What's the overall rate law from mechanism? | Identify RDS | rate = rate of RDS (in terms of observables) |
| Why does pressure increase rate of gas reactions? | Collision frequency | Z ∝ concentration → rate ∝ [A][B] |
| Does catalyst change equilibrium? | No | K unchanged; Ea lowered for both directions equally |
| First-order diagnostic? | Plot | ln[A] vs t → straight line |
| Second-order diagnostic? | Plot | 1/[A] vs t → straight line |
| Why does radical inhibitor stop a chain? | Termination | Inhibitor scavenges chain-carrying radicals |

---

## Common Confusion Points

**Reaction order ≠ stoichiometric coefficient**
For A + 2B → C, the rate might be k[A][B]², or k[A], or k[A]⁰[B]².
Orders must be determined experimentally. The stoichiometry only tells you the
rate order if the step is elementary — and most balanced equations are not elementary.

**Ea and ΔH are not the same**
Ea = Arrhenius activation energy (empirical, from ln k vs 1/T slope).
ΔH‡ = activation enthalpy (from TST Eyring analysis).
They're related: ΔH‡ ≈ Ea − RT (differs by ~2.5 kJ/mol at 298 K — usually negligible).
ΔH of the reaction = Ea(fwd) − Ea(rev). All three are different numbers.

**Intermediates vs transition states**
Intermediate: real species in a local energy minimum — has finite lifetime,
can sometimes be isolated (e.g., carbocation, radical, enzyme-substrate complex).
Transition state: energy maximum — cannot be isolated, exists instantaneously.
Both appear on the reaction coordinate diagram, but they're fundamentally different.

**Half-life depends on order**
First-order: t₁/₂ = 0.693/k (constant, independent of concentration — radioactive decay)
Second-order: t₁/₂ = 1/(k[A]₀) (decreases as [A] falls)
Zero-order: t₁/₂ = [A]₀/2k (increases as [A] falls)
The textbook "half-life" instinct (constant) only applies to first-order.

**Catalyst lowers Ea for BOTH directions**
Since ΔG = ΔG_fwd − ΔG_rev is fixed, lowering ΔG‡_fwd by x lowers ΔG‡_rev by the same x.
The equilibrium constant K is unchanged. The reaction reaches the same equilibrium faster.
