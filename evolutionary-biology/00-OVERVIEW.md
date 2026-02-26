# Evolutionary Biology — Landscape and Taxonomy

## The Big Picture

Evolution is the unifying theory of all biology. Every module in this directory maps to
one axis of the full framework:

```
+------------------------------------------------------------------+
|                  EVOLUTIONARY BIOLOGY LANDSCAPE                   |
+------------------------------------------------------------------+
|                                                                    |
<!-- @editor[diagram/P2]: Diagram lists mechanism-pattern pairs but doesn't show how they interact or feed into each other — rework as layered system view showing forces acting on a population with arrows showing interactions (e.g., drift opposes selection at small N, mutation feeds variation to selection) -->
|  MECHANISM              PATTERN                  TIMESCALE        |
|  ─────────              ───────                  ─────────        |
|  Natural selection  →   Adaptation               Generations      |
|  Genetic drift      →   Allele frequency shift   Generations      |
|  Mutation           →   New variants             Per replication  |
|  Gene flow          →   Population mixing        Generations      |
|  Sexual selection   →   Mate-choice traits       Generations      |
|  Coevolution        →   Arms races               Coevolutionary   |
|                                                                    |
|  MICROEVOLUTION         EVO-DEVO                 MACROEVOLUTION   |
|  ───────────────         ────────                 ─────────────   |
|  Within populations     Developmental toolkit    Across species   |
|  Hardy-Weinberg         HOX genes                Phylogeny        |
|  Wright-Fisher model    Modularity               Fossil record    |
|  Fitness landscape      Deep homology            Mass extinction  |
+------------------------------------------------------------------+
```

---

## The Modern Synthesis and Its Extensions

Darwin (1859) gave us natural selection. The Modern Synthesis (1930s–1940s) fused
Darwinian selection with Mendelian genetics. Subsequent decades added layers:

```
1859  Darwin: Descent with modification; natural selection
1865  Mendel: Discrete inheritance (ignored for 35 years)
1908  Hardy-Weinberg equilibrium formalized
1918  Fisher: Mendelian genetics + continuous variation reconciled
1930  Fisher: The Genetical Theory of Natural Selection
1931  Wright: Genetic drift and effective population size
1932  Wright: Adaptive landscape metaphor
1937  Dobzhansky: Genetics and the Origin of Species
1942  Mayr: Allopatric speciation; biological species concept
1944  Simpson: Fossil record integration — Tempo and Mode in Evolution
        = THE MODERN SYNTHESIS
1953  Watson-Crick: DNA structure
1968  Kimura: Neutral theory — most molecular evolution is neutral
1972  Gould & Eldredge: Punctuated equilibrium
1977  King & Wilson: Regulatory change explains human/chimp divergence
1980s Evo-devo emerges: HOX genes, developmental constraints
1990s Molecular phylogenetics matures (PCR + sequencing scale)
2000s Genomics: Comparative genomics, GWAS, selection scans
2010s Ancient DNA revolution: Neanderthal admixture, Denisovans
2020s Extended Evolutionary Synthesis debate:
        epigenetic inheritance, niche construction, plasticity
```

---

## Field Taxonomy

```
┌─────────────────────────────────────────────────────────────────┐
│                    EVOLUTIONARY BIOLOGY                          │
├──────────────────┬──────────────────┬────────────────────────── ┤
│  POPULATION      │  MOLECULAR        │  COMPARATIVE / MACRO      │
│  GENETICS        │  EVOLUTION        │  EVOLUTION                │
│                  │                   │                           │
│  Hardy-Weinberg  │  Neutral theory   │  Systematics              │
│  Fitness         │  dN/dS ratio      │  Phylogenetics            │
│  Drift           │  Molecular clock  │  Macroevolution           │
│  Selection       │  Gene families    │  Biogeography             │
│  coefficients    │  Horizontal GT    │  Mass extinctions         │
├──────────────────┼──────────────────┼───────────────────────────┤
│  EVO-DEVO        │  BEHAVIORAL /     │  SPECIATION               │
│                  │  ECOLOGICAL       │                           │
│  HOX genes       │  Sexual selection │  Allopatric               │
│  Toolkit genes   │  Kin selection    │  Sympatric                │
│  Modularity      │  Life history     │  Hybrid zones             │
│  Heterochrony    │  Coevolution      │  Reproductive isolation   │
│  Deep homology   │  Arms races       │  Ring species             │
└──────────────────┴──────────────────┴───────────────────────────┘
```

---

## Core Mathematical Frameworks

### 1. Hardy-Weinberg Equilibrium
Null model for population genetics. Allele frequencies do not change unless a force
acts. Derived from Mendelian random mating:

```
  p + q = 1   (two alleles, frequencies p and q)
  Genotype frequencies: AA = p², Aa = 2pq, aa = q²
  Σ = p² + 2pq + q² = (p + q)² = 1  ✓
```

Forces that perturb equilibrium: selection, drift, mutation, gene flow, non-random
mating. H-W is the null; departures are what require explanation.

### 2. Wright-Fisher Model
Stochastic model of genetic drift. Population of diploid size N; allele frequency p;
next generation sampled binomially:

```
  Var(Δp) = p(1-p) / (2N)
  Expected time to fixation (starting at p): ≈ 4N generations
  Expected time to loss:                     ≈ 2ln(1/p)(1-p)·N/p generations
```

Small N = large drift = stochastic dominates over selection. Bridge: effective
population size N_e < N always (bottlenecks, unequal sex ratio, variance in
reproductive success).

### 3. Selection Equations
Change in allele frequency per generation under diploid selection:

```
  Δp = p·q·[p(w₁₁-w₁₂) + q(w₁₂-w₂₂)] / w̄
```

where w₁₁, w₁₂, w₂₂ = fitnesses of AA, Aa, aa; w̄ = mean fitness.
Fitness landscape: assigns a fitness value to every genotype.

### 4. Neutral Theory (Kimura 1968)
Rate of neutral molecular evolution = mutation rate μ (independent of N).
Most polymorphism is selectively neutral.
Selection detectable via dN/dS > 1 (positive selection), dN/dS << 1 (purifying).

### 5. Molecular Clock
Rate of neutral substitution roughly constant across lineages → distance between
sequences ∝ divergence time. Calibrated against fossil record.

### 6. Phylogenetic Inference
Maximum parsimony, maximum likelihood, Bayesian MCMC (MrBayes, BEAST).
Gene trees ≠ species trees: incomplete lineage sorting, horizontal transfer complicate
inference. Coalescent theory bridges gene trees to population history.

---

## The Fitness Landscape — Unifying Concept

Sewall Wright (1932) introduced the adaptive landscape. Every genotype maps to a
fitness value. Evolution = movement across this landscape:

```
  High fitness ↑
               │    * peak 1        * peak 2
               │   / \             /
               │  /   \           / \
               │ /     \—valley——/   \
               │/                     \
  Low  fitness └──────────────────────────→ Genotype space
```

Key observations:
- Natural selection = gradient ascent (hill climbing)
- Drift allows crossing fitness valleys (key for Wright's shifting balance)
- Epistasis = interactions between loci = rugged landscape (many local peaks)
- Convergent evolution = independent ascent to the same adaptive peak

**Bridge to ML**: Fitness landscape is structurally identical to a loss surface in
neural network optimization. Local optima, saddle points, gradient descent — same
mathematical structure. Genetic algorithms are literally evolution-inspired
optimization. The "curse of dimensionality" in both fields: high-dimensional fitness
landscapes are mostly saddle points, not local optima (same result as in deep learning
loss surfaces — Dauphin et al. 2014).

---

<!-- @editor[bridge/P2]: No explicit "old world -> new world" bridge section — this learner would benefit from a bridge mapping evolutionary biology concepts to optimization, signal processing, or control theory concepts they already own from CS/math background -->
## Connections to Other Reference Directories

| Evolutionary concept | Where else it appears |
|----------------------|----------------------|
| Population genetics | genomics/ — GWAS, selection scans |
| Molecular clock | genomics/ — ancient DNA, phylogenomics |
| Immune co-evolution | immunology/ — host-pathogen arms races |
| Viral evolution | virology/ (this batch) — quasispecies |
| HOX genes / development | developmental-biology/ (Batch 10) |
| Neutral theory | information-theory/ — sequence entropy |
| Fitness landscape | machine-learning-theory/ — loss surfaces |
| Phylogenetic statistics | probability-statistics/ — Bayesian inference |

---

## Module Map

| File | Core question |
|------|---------------|
| 01-NATURAL-SELECTION.md | How does selection work mechanically? |
| 02-POPULATION-GENETICS.md | How do allele frequencies change? |
| 03-MOLECULAR-EVOLUTION.md | How do sequences diverge over time? |
| 04-SPECIATION.md | How do species split? |
| 05-PHYLOGENETICS.md | How do we reconstruct evolutionary history? |
| 06-EVO-DEVO.md | How does development constrain evolution? |
| 07-SEXUAL-SELECTION.md | How does mate choice drive evolution? |
| 08-COEVOLUTION.md | How do interacting species shape each other? |
| 09-MACROEVOLUTION.md | What happens above the species level? |

---

## Decision Cheat Sheet

| Question | Relevant framework | Module |
|----------|-------------------|--------|
| Is this trait adaptive? | Natural selection, dN/dS | 01, 03 |
| How fast will a beneficial allele spread? | Selection coefficient, sweep | 01, 02 |
| Is drift or selection dominant? | 4Nes criterion | 02 |
| Are two populations diverging? | FST, isolation-by-distance | 02, 04 |
| When did two lineages split? | Molecular clock, coalescent | 03, 05 |
| What is the phylogeny? | ML/Bayesian tree inference | 05 |
| Why does this gene exist across phyla? | Deep homology, toolkit genes | 06 |
| Why do males have elaborate ornaments? | Sexual selection, handicap | 07 |
| Why do hosts have complex immune systems? | Red Queen, arms races | 08 |
| What caused a mass extinction? | Macroevolution, kill curves | 09 |

---

## Common Confusion Points

**Evolution is not goal-directed.** Selection acts on existing variation; it does not
create variation to order. No foresight, no optimization toward a predetermined
target — only differential reproduction among available variants.

**Fitness is relative, not absolute.** Fitness of genotype AA = survival and
reproduction *relative to other genotypes in the same environment*. An "unfit"
organism in one environment may be fit in another.

**Micro vs. macroevolution is a spectrum, not a divide.** Macroevolution is the
long-run accumulation of microevolutionary changes, plus the sorting effect of
species selection and extinction. There is no mechanism unique to macroevolution.

**Neutral does not mean non-functional.** A synonymous substitution is neutral with
respect to amino acid sequence but the codon may affect translation speed, mRNA
stability, etc. "Neutral" means no fitness effect on the trait being measured.

**Species concept ambiguity.** Biological species concept (reproductive isolation)
works for sexually reproducing organisms but fails for bacteria, asexual eukaryotes,
and plants where hybridization is common. ~26 competing species concepts exist; this
is not a crisis, it is a reflection that "species" is a human category imposed on a
continuum.
