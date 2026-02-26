# 12-SYSTEMS-SYNTHETIC — Systems & Synthetic Biology

> Gene regulatory networks, ODE/Boolean models, flux balance analysis,
> synthetic circuits, and the engineering of living systems.
> Where biology meets control theory, network science, and software design.

---

## The Systems Biology Shift

```
REDUCTIONIST VIEW:           SYSTEMS VIEW:
  Gene X → Protein X          Network of interactions
  Protein X → Function X       → Emergent behaviors
  Study one component          → Study dynamics, topology, robustness
  at a time

KEY INSIGHT: the same components can produce radically different behaviors
depending on network topology. A negative feedback loop, a positive feedback loop,
and a feedforward loop are three different computations performed on the same signal.

Tools imported from engineering:
  Control theory       → stability analysis, feedback, robustness
  Network science      → topology, hubs, modularity
  Information theory   → noise, channel capacity, mutual information
  Signal processing    → frequency response, filtering
  Software engineering → modularity, abstraction, composition (synthetic biology)
```

---

## Gene Regulatory Networks (GRNs)

### Network Representations

```
NODES: genes (or proteins) — state variable = expression level
EDGES: regulatory interactions
  → activation (→ or ─▶)
  ─| repression (─┤)
  ── protein–protein interaction

Example: toggle switch
         A ─┤ B
         B ─┤ A
  Mutual repression → bistable (two stable states: A-on/B-off or A-off/B-on)

Example: negative feedback oscillator
         A → B → C ─┤ A
  Delayed negative feedback → oscillation (circadian clock motif)
```

### Boolean Network Models — Automata Theory Bridge

Boolean gene regulatory networks are finite-state automata — the TCS connection
is direct and the computational complexity results transfer exactly:

```
BOOLEAN GENE NETWORK = SYNCHRONOUS FINITE STATE AUTOMATON

  States:        2^N possible states for N genes (each ON/OFF)
  Transitions:   deterministic update function F: {0,1}^N → {0,1}^N
  Attractors:    fixed points + limit cycles = stable cell states
                 (cell types = attractors; differentiation = transient toward basin)

KAUFFMAN NK MODEL = RANDOM BOOLEAN CIRCUIT ANALYSIS

  N genes, each regulated by K random inputs, random Boolean function
  Computational analog: random K-SAT / random circuit satisfiability

  Phase transitions (same as in random K-SAT):
  K < 2:  ordered phase → few attractors, large basins, robust
           like easy SAT regime — most initial conditions reach same attractor
  K = 2:  critical (self-organized criticality) — maximal complexity
           corresponds to phase transition in random 2-SAT (solvable in polytime)
  K > 2:  chaotic phase → 2^(N/2) attractors, exponential sensitivity
           like hard 3-SAT — small perturbation → different attractor

STATE-SPACE EXPLOSION:
  N = 20,000 genes: 2^20000 possible states — computationally intractable to enumerate
  Practical approach: identify attractors by random sampling of trajectories
  Equivalent to: SAT solving by local search (random restart hill climbing)

SAT CONNECTION:
  "Is gene X eventually always ON for all initial conditions?"
  = reachability / liveness property of the automaton
  = model checking problem (CTL/LTL model checking on Boolean circuit)
  = NP-hard in general (known from model checking complexity theory)

ATTRACTOR LANDSCAPE AS EPIGENETIC LANDSCAPE (Waddington 1957):
  Height = energy / instability
  Valleys = attractors (cell types)
  Ridges = unstable states / separatrices between basins
  Differentiation = gradient descent into valley
  Reprogramming (Yamanaka factors) = add energy to escape local minimum
  → same vocabulary as optimization on non-convex landscapes
```

### Boolean Network Models

Simplest abstraction: each gene is ON (1) or OFF (0).
Update rules: Boolean functions of input states.

```
Example: toggle switch
  A(t+1) = NOT B(t)
  B(t+1) = NOT A(t)

Initial state (1,0): A=1, B=0 → next: A=NOT(0)=1, B=NOT(1)=0 → stable fixed point
Initial state (0,1): A=0, B=1 → next: A=NOT(1)=0, B=NOT(0)=1 → stable fixed point
Initial state (1,1): A=1, B=1 → next: A=NOT(1)=0, B=NOT(1)=0 → → oscillates

Attractor: state space trajectory converges to fixed point, limit cycle, or (rarely) chaos

Kauffman NK model:
  N genes, each regulated by K random inputs
  K=2: near critical regime — balance between order and chaos
  Biological GRNs: K ≈ 2–3 on average
  Attractors ≈ cell types (Kauffman's hypothesis)
```

### ODE Models

More quantitative: differential equations for continuous concentrations.

```
Gene X with activator A and repressor R:

  d[X]/dt = α · f([A], [R]) − δ · [X]

  α = synthesis rate,  δ = degradation rate
  f = regulatory function (often Hill-type):
    Activation:   f = [A]^n / (Kₐ^n + [A]^n)
    Repression:   f = Kᵣ^n / (Kᵣ^n + [R]^n)

  Steady state:  d[X]/dt = 0  →  [X]_ss = (α/δ) · f([A],[R])

For a two-gene toggle switch:
  d[u]/dt = α₁/(1 + v^β) − u
  d[v]/dt = α₂/(1 + u^γ) − v

  Phase plane analysis: nullclines (d[u]/dt = 0 and d[v]/dt = 0)
  Intersections = steady states; stability from Jacobian eigenvalues
  Three intersections (bistable): two stable + one unstable (saddle point)
```

### Network Motifs (Alon, 2007)

Recurring patterns significantly more common than in random networks:

```
NEGATIVE AUTOREGULATION (NAR):
  X ─┤ X
  Effect: speeds up response time, reduces steady-state noise
  ~40% of E. coli TFs autoregulate negatively

POSITIVE AUTOREGULATION (PAR):
  X → X
  Effect: bistability, slow response, memory
  Used for cell fate decisions (e.g., LuxR in quorum sensing)

FEEDFORWARD LOOP (FFL) — 8 types, most common: C1-FFL
  S → X → Z
  S → Z
  (S activates X; S AND X activate Z)
  Effect (C1-FFL): sign-sensitive delay, filters transient signals
  Coherent (all activate): delay on activation, no delay on deactivation
  Incoherent (X represses Z): pulse generator, fold-change detector

SINGLE INPUT MODULE (SIM):
  One master regulator → many target genes
  Genes activated sequentially (temporal program, e.g., flagella assembly)

DENSE OVERLAPPING REGULONS (DORs):
  Multiple regulators → shared target genes
  Integration of multiple signals (AND/OR logic)
```

---

## Flux Balance Analysis (FBA)

Quantitative modeling of metabolic networks at steady state.

### Setup

```
Stoichiometric matrix S (m × n):
  m = metabolites (rows),  n = reactions (columns)
  S_ij = stoichiometric coefficient of metabolite i in reaction j
         (positive = produced, negative = consumed)

Steady-state assumption:
  d[c]/dt = S · v = 0     (concentrations constant, fluxes v are unknowns)

Constraints:
  Reaction bounds: vₘᵢₙ ≤ vᵢ ≤ vₘₐₓ
    Irreversible: vₘᵢₙ = 0
    Exchange reactions: uptake/secretion bounds from measurements

Linear program:
  Maximize  c^T · v  (objective — usually biomass production or ATP yield)
  Subject to  S · v = 0  and  vₘᵢₙ ≤ v ≤ vₘₐₓ
```

### Applications

```
In silico gene knockouts:
  Set reaction v_i = 0 → reoptimize → does biomass decrease?
  Essential genes: knockouts that eliminate growth
  Synthetic lethality: two individually viable KOs that are lethal together

Metabolic engineering:
  Find reaction to overexpress/add to maximize product yield
  Constraint-based design: COBRA toolbox, COBRApy

Flux variability analysis (FVA):
  For each reaction: find min and max v_i consistent with optimal objective
  → determine which reactions are uniquely determined vs flexible

iJO1366 (E. coli): 1366 reactions, 1136 metabolites — largest validated GEM
Human metabolic reconstructions (RECON): tissue-specific models
```

---

## Noise in Gene Expression

### Sources of Noise

```
INTRINSIC NOISE: stochastic fluctuations in the biochemical reactions of a gene
  Transcription: mRNA produced in bursts (Poisson not well-fit; negative binomial better)
  Translation: protein bursts from single mRNA molecules
  Noise ∝ 1/√N (shot noise — fewer molecules → more noise)

EXTRINSIC NOISE: cell-to-cell variation in shared components
  Differences in: RNAP levels, ribosome numbers, cell volume, cell age
  Correlated between genes sharing upstream regulators

Fano factor = Var(n) / Mean(n)
  Poisson: Fano = 1 (intrinsic noise reference)
  Super-Poisson (Fano > 1): bursty expression
  mRNA: median ~1–100 molecules; protein: ~100–100,000

Noise-function tradeoffs:
  Negative autoregulation: reduces intrinsic noise (faster return to steady state)
  Ultrasensitivity (Hill n>1): can sharpen noisy graded signal to binary output
  Mutual inhibition toggle: bistability can "store" binary decisions above noise floor
```

---

## Synthetic Biology Principles

### Design Hierarchy

```
Parts → Devices → Systems → Chassis

Parts:     promoters, RBS, coding sequences, terminators, operators
           Characterized by: strength, orthogonality, context-dependence

Devices:   logic gates, switches, oscillators, sensors
           Composed from parts with defined behavior

Systems:   full circuits with defined I/O specification
           Example: biosensor + logic gate + actuator (kill switch, reporter)

Chassis:   host organism (E. coli, S. cerevisiae, CHO cells, cell-free)
           Provides: transcription/translation machinery, metabolism, growth
```

### Key Design Principles

```
ORTHOGONALITY: synthetic circuit should not interact with native networks
  Orthogonal RNAP (T7 RNAP): only transcribes T7 promoters
  Orthogonal ribosomes: only translate specific mRNAs
  Synthetic TFs (ZF, TALE, dCas9): bind designed DNA sequences only

MODULARITY: devices should work predictably when combined
  Problem: genetic context effects (promoter/RBS spacer, terminator read-through)
  Solution: insulators, strong terminators, standardized part interfaces

ABSTRACTION: hide implementation details at each level
  BioBricks (iGEM): standard prefix/suffix → parts physically compatible
  BUT: composability is harder than software (parts have crosstalk)

CHARACTERIZATION: measure transfer functions (input → output)
  Hill-type response: g(u) = α(u/K)^n / (1 + (u/K)^n)
  Plot: input signal [u] vs output expression level
  Capture: max expression, threshold, cooperativity
```

---

## Landmark Synthetic Circuits

### Genetic Toggle Switch (Gardner et al., Nature 2000)

```
Promoter 1 → Repressor 2 → blocks Promoter 2
Promoter 2 → Repressor 1 → blocks Promoter 1

Two stable states (bistable):
  State 1: Rep2 ON, Rep1 OFF → fluorescence from reporter at Promoter 2
  State 2: Rep1 ON, Rep2 OFF → fluorescence from reporter at Promoter 1

Switch with inducer: transient IPTG or temperature shift → flip to other state
  → digital memory, cell fate latch

ODE model: Gardner's two-equation system
  du/dt = α₁/(1 + v^β) − u
  dv/dt = α₂/(1 + u^γ) − v
```

### Repressilator (Elowitz & Leibler, Nature 2000)

```
lacI ─┤ tetR ─┤ cl ─┤ lacI  (ring of 3 mutual repressors)

Each repressor inhibits the next → delayed negative feedback → oscillation
GFP reporter on one node → fluorescence oscillations (~150 min period in E. coli)

Key requirement: delay (degradation tags on repressors) + sufficient repression (n > 1)
Noisy in original: cell-to-cell variation ~50% in period
Improved repressilator (Potvin-Trottier 2016): synchronized, ultra-precise (~500 min, low noise)

Circuit analogy: ring oscillator (n odd-numbered NOT gates in ring)
```

### Boolean Logic Gates

```
NOT gate:   Input → repressor → repressed output (inverter)
AND gate:   Input A + Input B → both required for output
            Two activators required; or repress two inhibitors of output
OR gate:    Either input A OR B → output
            Two promoters driving same output
NAND, NOR: combinations

Genetic AND gate example:
  Input A → TF1 (VP16 activation domain)
  Input B → TF2 (DBD domain)
  Only TF1 + TF2 together → active chimeric TF → output gene
```

---

## Optogenetics

```
Light-controlled proteins engineered into cells:

CHANNELRHODOPSIN-2 (ChR2, blue light ~470 nm):
  Cation channel; opens on blue light → Na⁺/Ca²⁺ influx → depolarization → action potential
  Application: activate specific neurons in circuit

HALORHODOPSIN (NpHR, yellow light ~580 nm):
  Cl⁻ pump; hyperpolarizes cell → silences neurons

ARCH (archaerhodopsin, yellow light):
  H⁺ pump; outward current → silences neurons

LIGHT-ACTIVATED PROTEIN INTERACTIONS:
  LOV domains (blue light): dimerize or undimeize → fuse to TFs → light-controlled transcription
  CRY2/CIB1 (blue light): heterodimerize
  PhyB/PIF (red light): dimerize; far-red reverses
  Applications: light-controlled kinases, GTPases, gene expression, protein localization
```

---

## CRISPRi / CRISPRa

```
dCas9 (catalytically dead): binds target DNA guided by sgRNA but does NOT cut

CRISPRi (interference = repression):
  dCas9 alone: steric block of RNAP → modest repression
  dCas9-KRAB (KRAB repressor domain): recruits KAP1/HP1 → H3K9me3 → silencing
  ~100–1000× repression

CRISPRa (activation):
  dCas9-VP64: 4× VP16 activation domains → modest activation
  dCas9-VPR: VP64+p65+Rta → stronger activation
  SAM system: dCas9-VP64 + sgRNA with MS2 hairpins + MCP-VP64 → even stronger

APPLICATIONS:
  Genome-scale screening: CRISPRi/a library (all 20,000 genes) → phenotypic readout
  Gene circuits: CRISPRi repressors as modular parts (good orthogonality)
  Transcription factor replacement: CRISPRa to activate endogenous loci
```

---

## Decision Cheat Sheet

| Question | Concept | Answer |
|----------|---------|--------|
| Circuit produces two stable states | Bistability | Mutual repression (toggle switch) or positive feedback |
| Circuit produces oscillation | Limit cycle | Odd-numbered ring of repressors; delayed negative feedback |
| Filter out transient signal inputs | Network motif | Coherent FFL with AND logic |
| Model metabolic capability of organism | FBA | S·v = 0 LP; maximize biomass subject to exchange constraints |
| Gene shows bursty expression | Noise | Negative binomial distribution; single mRNA → protein burst |
| Control a single neuron in a circuit | Optogenetics | ChR2 (activate), Halorhodopsin/Arch (silence) |
| Repress gene without editing sequence | CRISPRi | dCas9-KRAB guided by sgRNA to promoter region |
| Activate silent endogenous gene | CRISPRa | dCas9-VPR/SAM guided to promoter |
| Test if gene is essential in metabolism | FBA KO | Set v=0, reoptimize; essential if biomass → 0 |

---

## Common Confusion Points

**Systems biology ≠ big data / omics alone**
Systems biology includes quantitative modeling, network analysis, and dynamical theory.
Collecting transcriptomic data is not systems biology — it becomes systems biology when
integrated with models that predict and test system-level behaviors. Data without models
is phenotype cataloging, not mechanistic understanding.

**Boolean models lose quantitative information but gain tractability**
A Boolean model can't capture graded responses, noise, or exact timing.
But it CAN identify attractors, determine which initial states lead to which cell fates,
and guide intuition about what ODE parameters are important.
Start Boolean, validate with ODE, calibrate with experiment — standard workflow.

**FBA is not a dynamic model**
FBA assumes steady state (d[c]/dt = 0). It tells you the optimal flux distribution
at one snapshot, not how the system gets there or how it responds to perturbations.
Dynamic FBA (dFBA) adds time course; resource allocation models add growth constraints.
Don't ask "how fast does the cell adapt?" of a static FBA model.

**Synthetic circuits don't behave like software modules**
Software modules have well-defined interfaces and no side effects if properly written.
Biological parts have genetic context effects (promoter–RBS spacing, read-through,
codon usage), metabolic burden (expression costs slow growth), and evolutionary
pressure (cells evolve to reduce circuit burden). Orthogonality is approximated,
not achieved. This is why synthetic biology is harder than writing code.

**Optogenetics changes cell behavior, not gene expression (usually)**
ChR2/Arch control electrical activity on timescales of milliseconds.
Light-activated TFs (CRY2-CIB1, LOV-TF fusions) control gene expression on minutes–hours.
These are different tools for different timescales — don't conflate them.
