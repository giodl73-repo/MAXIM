# Biological Thermodynamics — Free Energy, ATP, and Non-Equilibrium Life

## The Big Picture

```
┌──────────────────────────────────────────────────────────────────────────┐
│              BIOLOGICAL THERMODYNAMICS LANDSCAPE                         │
│                                                                            │
│  EQUILIBRIUM THERMO           NON-EQUILIBRIUM THERMO                     │
│  ──────────────────           ─────────────────────                      │
│  ΔG = ΔH - TΔS               Steady-state fluxes                         │
│  Keq = exp(-ΔG°/RT)          Driving force: chemical potential gradient  │
│  Boltzmann distribution       Onsager reciprocal relations                 │
│  Free energy minimization     NESS: non-equilibrium steady state           │
│                                                                            │
│  ATP HYDROLYSIS                                                            │
│  ─────────────                                                             │
│  ATP + H₂O → ADP + Pᵢ                                                    │
│  ΔG°' = -7.3 kcal/mol    (standard, pH 7, 25°C)                          │
│  ΔG_cell ≈ -12 kcal/mol  (in vivo, far from equilibrium)                 │
│                                                                            │
│  FREE ENERGY TRANSDUCTION CHAIN                                            │
│  ─────────────────────────────                                             │
│  Light / Food                                                              │
│      ↓  oxidative phosphorylation / photosynthesis                       │
│  Proton gradient (ΔμH⁺)                                                  │
│      ↓  ATP synthase                                                       │
│  ATP                                                                       │
│      ↓  hydrolysis by molecular machines                                   │
│  Mechanical work / ion pumping / biosynthesis                              │
│                                                                            │
│  ENERGY SCALE ANCHOR: k_BT = 0.6 kcal/mol at 310 K                       │
│  ATP hydrolysis ΔG_cell ≈ 20 k_BT — large premium over thermal noise     │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Section 1 — Gibbs Free Energy in Biology

### The Core Equation

At constant temperature and pressure (the relevant biological constraint):

```
  ΔG = ΔH - TΔS

  ΔG < 0  →  spontaneous (exergonic)
  ΔG > 0  →  non-spontaneous (endergonic), requires energy input
  ΔG = 0  →  equilibrium
```

For a reaction A ⇌ B with concentrations [A] and [B]:

```
  ΔG = ΔG° + RT ln([B]/[A])

  At equilibrium: ΔG = 0  →  ΔG° = -RT ln(Keq)
  Rearranging:    Keq = exp(-ΔG°/RT)
```

### Biochemical Standard State (ΔG°')

Biochemists use a modified standard state: pH 7.0, 25°C, all solutes at 1 M except
water and protons. Denoted ΔG°' to distinguish from physical chemistry convention.
This matters because ATP hydrolysis releases a proton — the pH dependence is baked in.

### Free Energy Composition

```
┌──────────────────────────────────────────────────────────┐
│                ΔG = ΔH - TΔS                             │
│                                                            │
│  ΔH contributions (enthalpy):                            │
│  ─────────────────────────────                           │
│  Covalent bond formation/breaking    ±50-500 kcal/mol    │
│  Hydrogen bonds                      ±1-5 kcal/mol       │
│  van der Waals contacts              ±0.1-1 kcal/mol     │
│  Electrostatic interactions          ±1-10 kcal/mol      │
│  Hydrophobic effect (ΔH small!)      ≈0 kcal/mol         │
│                                                            │
│  TΔS contributions (at 310 K):                           │
│  ─────────────────────────────                           │
│  Hydrophobic burial (water ordering) -TΔS ≈ -3 kcal/mol  │
│  Conformational restriction          -TΔS ≈ +2-10 kcal/mol│
│  Translational/rotational entropy    -TΔS ≈ +5-15 kcal/mol│
└──────────────────────────────────────────────────────────┘
```

**The hydrophobic effect** is entropy-dominated, not enthalpy-dominated. Water
molecules around nonpolar surfaces form ordered cages → large entropic cost. Burying
nonpolar surface releases those water molecules → entropy gain drives folding. At room
temperature, ΔH ≈ 0 for hydrophobic burial. At low temperature, the entropy advantage
disappears → cold denaturation is a real phenomenon.

---

## Section 2 — ATP as Energy Currency

### Why ATP?

ATP is not the most energy-rich molecule (GTP, CTP, PEP are comparable). ATP is the
universal energy currency because:

1. **Kinetic stability**: ATP does not hydrolyze rapidly without enzymes. Half-life in
   neutral water ≈ years. The cell controls when and where energy is released.
2. **Thermodynamic coupling**: ΔG_cell ≈ −12 kcal/mol is large enough to drive most
   biosynthetic reactions, ion pumping, and motor proteins.
3. **Three phosphates**: Two high-energy phosphoanhydride bonds (γ and β). Each
   hydrolysis releases ≈20 k_BT in vivo.
4. **Allosteric signaling**: ATP/ADP/AMP ratios are the cell's energy sensor — AMP
   kinase (AMPK) activates catabolic pathways when energy is low.

### ATP Hydrolysis: The Numbers

```
  Reaction:   ATP⁴⁻ + H₂O → ADP³⁻ + HPO₄²⁻ + H⁺

  Standard:   ΔG°' = -7.3 kcal/mol = -30.5 kJ/mol

  In vivo (typical cytoplasmic concentrations):
    [ATP] ≈ 5 mM
    [ADP] ≈ 0.5 mM
    [Pᵢ]  ≈ 5 mM

  ΔG = ΔG°' + RT ln([ADP][Pᵢ] / [ATP])
     = -7.3 + (0.6) × ln((0.5×10⁻³)(5×10⁻³) / (5×10⁻³))
     = -7.3 + (0.6) × ln(5×10⁻⁴)
     = -7.3 + (0.6) × (-7.6)
     = -7.3 - 4.6
     ≈ -11.9 kcal/mol  ≈ -50 kJ/mol

  In k_BT units at 310 K:  ΔG_cell ≈ -20 k_BT per ATP hydrolysis
```

The cell maintains [ATP] >> [ADP] far from the equilibrium ratio. Keq for hydrolysis
≈ 10⁵ → equilibrium would have essentially no ATP. The cell dies when this ratio
collapses toward Keq (e.g., ischemia, cyanide poisoning, mitochondrial failure).

### Coupling Exergonic to Endergonic Reactions

```
  Example: glutamine synthesis

  Glutamate + NH₃ → Glutamine + H₂O    ΔG°' = +3.4 kcal/mol  (unfavorable)
  ATP + H₂O → ADP + Pᵢ                 ΔG°' = -7.3 kcal/mol

  Coupled total:
  Glutamate + NH₃ + ATP → Glutamine + ADP + Pᵢ
  ΔG°' = 3.4 + (-7.3) = -3.9 kcal/mol  ← spontaneous

  Mechanism: glutamine synthetase phosphorylates glutamate intermediate,
  never releasing it, so the two reactions are mechanistically coupled.
```

The coupling is mechanistic, not just arithmetic. The enzyme physically links the
reactions via a short-lived phosphorylated intermediate that never diffuses away.

### ATP Accounting in Aerobic Metabolism

```
  Aerobic oxidation of glucose:
  C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O    ΔG°' = -686 kcal/mol

  ┌─────────────────────────────────────────────────────┐
  │  Pathway                     │  ATP (approx.)       │
  │  ────────────────────────────│────────────────────  │
  │  Glycolysis (substrate-lvl)  │  2 ATP               │
  │  Pyruvate → Acetyl-CoA       │  ~5 ATP (via NADH)   │
  │  Krebs cycle (substrate-lvl) │  2 GTP ≈ 2 ATP       │
  │  Krebs NADH/FADH₂ → ETC     │  ~26 ATP              │
  │  ────────────────────────────│────────────────────  │
  │  Total                       │  ~30-32 ATP          │
  └─────────────────────────────────────────────────────┘

  Efficiency: 30 × 7.3 / 686 ≈ 32%
  Rest dissipated as heat → maintains body temperature
```

---

## Section 3 — Equilibrium Constants and Boltzmann Distribution

### Two-State Systems

For a two-state system (open/closed channel, folded/unfolded, bound/unbound):

```
  p_B / p_A = exp(-ΔG° / k_BT)   (Boltzmann relation)

  ΔG = 0:        p_B = p_A = 0.5    (equal populations)
  ΔG = +1 k_BT:  p_B / p_A = 0.37  (A favored ~3:1)
  ΔG = +2 k_BT:  p_B / p_A = 0.14  (A favored ~7:1)
  ΔG = +5 k_BT:  p_B / p_A = 0.007 (A favored ~150:1)
  ΔG = +10 k_BT: p_B / p_A = 5×10⁻⁵ (essentially never in B)
```

This governs: ion channel open probability, protein conformational states, and
the fraction of receptors occupied by a ligand at given concentration.

### Binding Affinity and Free Energy

```
  Association: A + B ⇌ AB
  Kd = [A][B] / [AB]   (units: M)

  ΔG°_binding = RT ln(Kd)

  Kd = 1 nM   →  ΔG°_binding = -12 kcal/mol  (tight binding)
  Kd = 1 μM   →  ΔG°_binding = -8.2 kcal/mol (moderate)
  Kd = 1 mM   →  ΔG°_binding = -4.1 kcal/mol (weak)

  Rule: each 10× reduction in Kd = 1.36 kcal/mol ≈ 2.3 k_BT in ΔG
```

Getting from Kd = 1 μM to 1 nM requires only ~5.5 kcal/mol — roughly 2-3 hydrogen
bonds or well-packed hydrophobic contact. Achievable but not trivial in drug design.

---

## Section 4 — Non-Equilibrium Steady States (NESS)

### Why Life Is Not at Equilibrium

```
  EQUILIBRIUM:                      NON-EQUILIBRIUM STEADY STATE:

  Net flux = 0                      Net flux ≠ 0 (continuous cycling)
  Detailed balance holds            Detailed balance violated
  Boltzmann distribution            Non-Boltzmann stationary distribution
  No dissipation                    Constant entropy production
  Keq completely determines         Kinetic parameters + energy input
    populations                       determine populations
  Nothing happens                   Life
```

**Example: ATP/ADP cycle.** Keq for ATP hydrolysis ≈ 10⁵ → equilibrium [ATP]/[ADP]
≈ 10⁻⁵. Actual cell: [ATP]/[ADP] ≈ 10. The cell operates 10⁶× away from equilibrium.
Mitochondria continuously drive this ratio by pumping protons. ATP depletion kills
cells not because ATP is toxic when absent, but because hundreds of NESS processes
collapse toward useless equilibria.

### Chemical Potential and Driving Force

For species i, chemical potential:

```
  μᵢ = μᵢ° + RT ln(cᵢ)

  Net reaction flux is driven by:
  ΔG_reaction = Σᵢ νᵢ μᵢ   (νᵢ = stoichiometric coefficients)

  At equilibrium: ΔG_reaction = 0
  Away from equilibrium: |ΔG_reaction| drives net flux
```

For the Na⁺/K⁺-ATPase (pumps 3 Na⁺ out, 2 K⁺ in per ATP hydrolyzed):

```
  ΔG_pump = ΔG_Na(3 ions) + ΔG_K(2 ions) + ΔG_membrane + ΔG_ATP

  Electrochemical potential per ion: Δμᵢ = RT ln(cᵢ_in/cᵢ_out) + zᵢFΔΨ

  Na⁺ inside: [Na⁺]_in ≈ 12 mM, [Na⁺]_out ≈ 145 mM, ΔΨ ≈ -70 mV
  → pumping Na⁺ out costs: ~3.5 kcal/mol per ion × 3 = ~10.5 kcal/mol
  ATP provides: ~12 kcal/mol  → thermodynamically feasible
```

### Proton Motive Force

Mitchell's chemiosmotic hypothesis (Nobel 1978): the mitochondrial inner membrane
uses a proton gradient as the energy intermediate between electron transport and ATP.

```
  ΔμH⁺ = F·ΔΨ + RT·ln([H⁺]_out / [H⁺]_in)
         = F·ΔΨ - 2.303 RT·ΔpH

  Typical values:
    ΔΨ   ≈ -180 mV  (matrix negative)
    ΔpH  ≈ 0.5-1    (matrix more alkaline)
    ΔμH⁺ ≈ -200 meV per proton ≈ -4.6 kcal/mol per H⁺

  ATP synthase uses ~2.7 protons per ATP:
  Energy harvested: 2.7 × 4.6 ≈ 12.4 kcal/mol ≈ ΔG_ATP  (consistent)
```

---

## Section 5 — Entropy in Biology

### The Hydrophobic Effect: Detailed Thermodynamics

The hydrophobic effect drives membrane assembly and protein folding. Its anomalous
temperature dependence is a diagnostic signature:

```
  Transfer of nonpolar solute from water to organic phase:

  At 25°C:   ΔH ≈ 0,   ΔS > 0   →  entropy-driven
  At 80°C:   ΔH < 0,   ΔS ≈ 0   →  enthalpy-driven (solvation changes)
  At  0°C:   ΔH > 0,   ΔS > 0   →  entropy still drives but ΔH works against
             → at very low T: cold denaturation

  Large positive ΔCp (heat capacity increase) upon nonpolar exposure:
    Signature in calorimetry: ΔCp = dΔH/dT > 0 for hydrophobic burial
```

Physical picture: water forms ordered clathrate-like cages around hydrophobic
solutes. These cages cost entropy (constrained water). Burying nonpolar surface
releases the cages → ΔS_water > 0. This dominates at physiological temperature.

### Conformational Entropy

```
  Flexible polypeptide: each residue has several rotamer states
  → 100-residue protein has ~3¹⁰⁰ conformations before folding

  Upon folding: ΔS_conf < 0  (unfavorable — backbone fixed)

  Folding ΔG breakdown (typical globular protein):
    ΔH_fold ≈ -100 to -200 kcal/mol  (H-bonds, van der Waals)
    TΔS_conf ≈ +50 to +150 kcal/mol   (backbone restriction, unfavorable)
    TΔS_water ≈ +50 to +100 kcal/mol  (hydrophobic burial, favorable)

    Net: ΔG_fold = -5 to -15 kcal/mol  (small difference of large numbers)
```

Protein stability is a narrow balance. ΔG_fold ≈ −10 kcal/mol means the folded
state is only marginally preferred (~1:5000 unfolded at any instant in dilute
solution). Chaperones and the crowded cellular environment shift this balance.

---

## Section 6 — Calorimetry: Direct Thermodynamic Measurement

### Isothermal Titration Calorimetry (ITC)

```
  ┌──────────────────────────────────────────────────────────┐
  │  ITC: ligand titrated into protein solution at const T   │
  │                                                          │
  │  Measures directly:  ΔH per injection (heat signal)      │
  │  From binding isotherm:  n (stoichiometry), Kd           │
  │  Calculates:         ΔG = -RT ln(Kd)                     │
  │                       TΔS = ΔH - ΔG                      │
  │                                                          │
  │  Complete thermodynamic profile in one experiment        │
  │  Gold standard for binding characterization              │
  │  Limitation: requires high protein concentration (μM-mM) │
  │    and large sample volumes (1-2 mg protein per run)     │
  └──────────────────────────────────────────────────────────┘
```

### Differential Scanning Calorimetry (DSC)

Measures Cp vs. temperature. Protein unfolding shows a large endothermic peak:

```
  At melting temperature Tm:  ΔG = 0  →  Tm = ΔH_fold / ΔS_fold

  From DSC:
    ΔH_unfold = area under peak
    ΔS_unfold = ΔH_unfold / Tm
    ΔCp from baseline difference → quantifies hydrophobic burial area
    van't Hoff ΔH from peak shape vs. calorimetric ΔH → cooperativity
```

If van't Hoff ΔH ≠ calorimetric ΔH, the transition is not two-state (intermediate
states exist). This distinction between two-state and multistate unfolding is
invisible in most other techniques.

---

## Engineering and Physics Bridges

Biological thermodynamics is classical thermodynamics applied to a non-equilibrium machine. Every concept has a direct engineering analog.

```
  BIOLOGY                         CLASSICAL ENGINEERING PARALLEL
  ──────────────────────────────────────────────────────────────────────
  Free energy transduction        Heat engine efficiency (Carnot):
  (ATP coupling)                  ΔG_cell ≈ -12 kcal/mol per ATP is the
                                  "work available per fuel cycle." The
                                  mitochondrion is a proton-gradient engine
                                  with ~32% efficiency — comparable to a
                                  steam turbine.

  Proton motive force             Electrochemical potential in batteries:
  ΔμH⁺ = FΔΨ - 2.303RT·ΔpH      ΔΨ ≈ -180 mV is a ~200 meV stored EMF.
                                  ATP synthase is the "load" driven by this
                                  potential — exactly as a motor load is
                                  driven by voltage across a circuit.

  Membrane equivalent circuit     RC circuits in electrical engineering:
  C_m × dV/dt = -Σ G_ion(V-E_ion) Kirchhoff's current law applied to a
                                  capacitor (bilayer) in parallel with
                                  conductances (channels). The Nernst
                                  potential is a battery EMF for each ion.

  NESS (non-equilibrium steady    Open thermodynamic systems in chemical
  state): [ATP]/[ADP] ≈ 10⁶×Keq  engineering — a continuous flow reactor
                                  maintained far from equilibrium by
                                  continuous energy input (combustion fuel
                                  input → products out).

  ΔG°' vs ΔG in vivo              Standard state vs. operating point:
  (-7.3 vs -12 kcal/mol)          ΔG°' is the property at standard conditions;
                                  ΔG is the operating condition. A chemical
                                  engineer always uses operating conditions,
                                  not standard state, to evaluate feasibility.
  ──────────────────────────────────────────────────────────────────────
```

**Key insight**: life is not a closed system at equilibrium — it is an open chemical engine that continuously imports free energy (food, light) and exports entropy (heat, CO₂). Classical thermodynamics provides all the tools; the biological context adds the specific concentrations and coupling mechanisms.

---

## Decision Cheat Sheet

| Question | Concept | Formula / Value |
|----------|---------|-----------------|
| Is a reaction spontaneous? | Sign of ΔG | ΔG = ΔH - TΔS < 0 |
| What equilibrium ratio does ΔG give? | Boltzmann | p₂/p₁ = exp(-ΔΔG/k_BT) |
| How much energy does ATP provide in the cell? | In vivo ΔG | ~-12 kcal/mol = -20 k_BT |
| Why does a cell die when ATP runs out? | NESS collapse | [ATP]/[ADP] → Keq ≈ 10⁻⁵ |
| What drives protein folding thermodynamically? | Hydrophobic + H-bonds | ΔG_fold ≈ -5 to -15 kcal/mol |
| How is drug affinity related to free energy? | ΔG = RT ln(Kd) | Each 10× in Kd = 1.36 kcal/mol |
| What links electron transport to ATP synthesis? | Proton motive force | ΔμH⁺ = FΔΨ - 2.303RT·ΔpH |
| What makes hydrophobic burial favorable? | Water entropy gain | ΔH ≈ 0, ΔS_water > 0 at 25°C |
| How to measure both ΔH and Kd simultaneously? | ITC | Single titration experiment |

---

## Common Confusion Points

**ΔG° vs. ΔG.** The standard free energy ΔG° is a fixed number for a given reaction at
given T and pH. The actual free energy ΔG depends on current concentrations. ATP
hydrolysis has ΔG°' = −7.3 kcal/mol but ΔG_cell = −12 kcal/mol because [ATP] >> [ADP]
in the living cell. These are fundamentally different quantities. Using ΔG° to reason
about in vivo processes is a common error.

**Entropy is not disorder.** Entropy is the log of the number of microstates. The
hydrophobic effect increases water entropy (more microstates available to water
molecules freed from ordered cages) even though it drives formation of ordered
structures. The system's entropy = water + protein; water contribution dominates
at physiological temperature.

**Enthalpy-entropy compensation.** In protein-ligand binding, gains in enthalpy (new
H-bond) are often offset by entropy loss (ligand or protein restricted). Adding a
functional group that gains −2 kcal/mol ΔH typically loses +1.5 kcal/mol TΔS. Net
gain: −0.5 kcal/mol. This compensation is endemic and explains why drug optimization
is slow despite abundant structural data.

**Non-equilibrium ≠ violation of thermodynamics.** The second law says total entropy
(system + surroundings) increases. Cells decrease local entropy (build ordered
structures) by exporting more entropy to surroundings (heat + CO₂). The cell is a
conduit for entropy production, not a violation of physics.

**Marginal stability is a feature, not a flaw.** Proteins with ΔG_fold = −5 kcal/mol
seem barely stable. This is intentional: the protein must be flexible for function,
degradable by proteases, and capable of large conformational changes. Hyperthermostable
proteins from 120°C organisms are more stable but often less active at room temperature.
Evolution tunes stability to "just enough."
