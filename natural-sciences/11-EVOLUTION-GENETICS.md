# 11-EVOLUTION-GENETICS — Evolution & Genetics

> Mendelian inheritance to molecular population genetics to evo-devo.
> The mathematical framework behind natural selection, drift, and speciation —
> plus the molecular machinery that generates and constrains variation.

---

## The Conceptual Hierarchy

```
LEVELS OF ANALYSIS:
  Molecular genetics    — DNA sequence, mutation, repair, recombination
  Transmission genetics — Mendelian inheritance, linkage, mapping
  Population genetics   — allele frequencies, selection, drift, migration
  Evolutionary biology  — speciation, phylogenetics, macroevolution
  Evo-devo             — developmental constraints, gene regulatory networks

Each level has its own tools, but the thread is the same:
  Variation (mutations, recombination) + Inheritance (replication) +
  Differential reproduction (selection or drift) = Evolution
```

---

## Mendelian Genetics

### Mendel's Laws

```
Law of Segregation:
  Each diploid individual has two alleles per locus.
  These segregate equally into gametes (meiosis I separation).
  Probability of transmitting either allele: 50%.

Law of Independent Assortment:
  Alleles at different loci assort independently into gametes —
  IF loci are on different chromosomes (or far apart on same chromosome).
  Molecular basis: random orientation of homolog pairs at meiosis I.
  Violated by: linkage (loci on same chromosome, close together)

Dominance/Recessiveness:
  Dominant: expressed in heterozygote (Aa)
  Recessive: expressed only in homozygote (aa)
  Incomplete dominance: Aa intermediate phenotype
  Codominance: Aa expresses both (ABO blood type A + B → AB)
```

### Punnett Square and Probability

```
Monohybrid cross:  Aa × Aa
  Offspring: 1/4 AA : 2/4 Aa : 1/4 aa
  Phenotypic ratio (A dominant): 3:1

Dihybrid cross:  AaBb × AaBb
  Phenotypic ratio (independent assortment): 9:3:3:1

Test cross:  unknown dominant × homozygous recessive (aa or aabb)
  All offspring show genotype of unknown parent

Chi-square test for Mendelian ratios:
  χ² = Σ (observed − expected)² / expected
  df = number of classes − 1
  p < 0.05 → observed deviates significantly from expected ratio
```

### Extensions to Simple Dominance

```
Epistasis: one gene masks expression of another
  Labrador coat color: B locus (black/brown) + E locus (expression)
    ee: yellow regardless of B — E epistatic to B

Pleiotropy: one gene affects multiple phenotypes
  Example: FBN1 mutations → Marfan syndrome (tall, aortic aneurysm, lens dislocation)

Penetrance: fraction of individuals with genotype who show phenotype
  BRCA1 mutation: 65–72% lifetime breast cancer risk (not 100% — incomplete penetrance)

Expressivity: variable degree of phenotype expression among individuals with same genotype

Polygenic traits: controlled by many loci (height, IQ, BMI)
  Each locus contributes small additive effect
  Normal distribution of phenotype (central limit theorem applied to many loci)
  GWAS (genome-wide association studies) identify contributing loci
```

---

## Molecular Basis of Mutation

### Mutation Types

```
Point mutations:
  Transition:   purine → purine (A↔G) or pyrimidine → pyrimidine (C↔T)
                More common than transversions (base tautomers, deamination)
  Transversion: purine → pyrimidine or vice versa (A/G ↔ C/T)

Synonymous (silent):  codon change → same amino acid (third position wobble)
Nonsynonymous:        codon change → different amino acid
  Missense:    different amino acid (Glu→Val in HbS → sickle cell)
  Nonsense:    amino acid codon → stop codon → truncated protein

Indels (insertions/deletions):
  In coding sequence: frameshift if not multiple of 3
  Most common in homopolymer runs (polymerase slippage)

Copy number variants (CNVs): large duplications/deletions (kb–Mb)
Chromosomal rearrangements: inversions, translocations, fusions (BCR-ABL in CML)
```

### Common Mutagens and Mechanisms

```
Deamination:    C → U (read as T → C:G → T:A transition, most common spontaneous)
                5-methylcytosine → thymine (C:G → T:A at CpG sites — "hotspots")
Oxidation:      8-oxoguanine (pairs with A → G:C → T:A transversion)
Alkylation:     O⁶-methylguanine (misread as A → G:C → A:T transition)
UV radiation:   pyrimidine dimers (T-T, T-C cyclobutane) → XP if NER defective
Ionizing radiation: DSBs → NHEJ-mediated chromosomal rearrangements
Intercalating agents (ethidium, acridine): insert between bases → frameshift indels
```

### DNA Repair Pathways

```
Pathway              Damage type             Key proteins
──────────────────────────────────────────────────────────────────
Base excision (BER)  Oxidized/deaminated     Glycosylase, APE1, Pol β, XRCC1
  repair             single bases
Nucleotide excision  Bulky adducts, pyrim-   XPC, TFIIH, XPA, XPG, XPF-ERCC1
  (NER)              idine dimers (UV)
Mismatch repair (MMR) Replication errors,    MSH2/6, MLH1/PMS2, EXO1
                      mismatches
Homologous           DSBs (in S/G2)          ATM, BRCA1/2, RAD51, RAD52
  recombination (HR)
NHEJ                 DSBs (all phases)       Ku70/80, DNA-PKcs, XRCC4, LIG4
```

---

## Hardy-Weinberg Equilibrium

A null model: allele frequencies don't change in absence of evolutionary forces.

### Assumptions

```
1. Random mating (panmixia)
2. No selection (all genotypes equally fit)
3. No mutation
4. No genetic drift (infinite population)
5. No migration (closed population)
```

### The Law

```
For two alleles at a diploid locus:
  p = frequency of allele A₁
  q = frequency of allele A₂
  p + q = 1

Genotype frequencies at equilibrium:
  AA:  p²
  Aa:  2pq
  aa:  q²
  p² + 2pq + q² = 1  (binomial expansion of (p+q)²)

Achieved in ONE generation of random mating from any initial genotype frequencies.

Applications:
  1. Test for HWE: χ² test on observed vs expected genotype frequencies
     Deviation → non-random mating, selection, population structure
  2. Estimate carrier frequency from disease prevalence:
     Cystic fibrosis: q² = 1/2500 → q = 1/50 → 2pq ≈ 2/50 = 4% carrier frequency
  3. Forensic genetics: product rule assumes HWE + linkage equilibrium
```

---

## Population Genetics

### Natural Selection

```
Fitness (w): relative reproductive success
Selection coefficient (s): deviation from maximum fitness
  w_AA = 1,  w_Aa = 1,  w_aa = 1 − s   (selection against aa)

Change in allele frequency per generation:
  Δq ≈ −sq²(1−q) / (1 − sq²)   (weak selection approximation)

For dominant/recessive/additive models:
  Additive: w_AA = 1, w_Aa = 1−s/2, w_aa = 1−s → fastest allele frequency change
  Dominant: w_AA = w_Aa = 1, w_aa = 1−s → recessives protected in heterozygotes
  Overdominance (heterozygote advantage): maintains polymorphism
    Classic example: HbS/HbA heterozygote — malaria resistance + no sickle cell
    Stable equilibrium at p* = s_aa/(s_AA + s_aa)

Time to fixation/loss:
  Strongly selected: ~1/s generations (fast)
  Weakly selected: ~4Ne generations (slow — neutral theory relevant)
```

### Genetic Drift

```
Random sampling fluctuation in finite populations.
Change in allele frequency per generation: Var(Δp) = p(1−p)/(2Ne)

Ne = effective population size
  Diploid, equal sex ratio, constant size: Ne = N
  Unequal sex ratio: Ne = 4Nm·Nf/(Nm+Nf)
  Fluctuating population: Ne = 1/(1/N₁ + 1/N₂ + … + 1/Nt) × t (harmonic mean)

Key consequences:
  Fixation probability of neutral allele: 1/(2Ne)
  Fixation time of neutral allele: ~4Ne generations
  Loss of heterozygosity rate: ΔH/H = 1/(2Ne) per generation

Bottleneck effect: severe reduction in population → random loss of alleles →
  reduced diversity → founder effects in isolated populations
  Example: Amish founder effect (Ellis-van Creveld syndrome ~1% vs 0.007% general)

Founder effect: new population established by few individuals → genetic drift +
  subset of original alleles
```

### Wright-Fisher and Coalescent — Probability Theory Bridge

The Wright-Fisher model and coalescent theory are standard probability structures
in disguise. The TCS framing is direct:

```
WRIGHT-FISHER MODEL = DISCRETE-TIME STOCHASTIC PROCESS

  State space: allele count k ∈ {0, 1, ..., 2N}
  Transition: P(k → j) = C(2N,j) · (k/2N)^j · (1 − k/2N)^(2N−j)
              = Binomial(2N, k/2N)
  → Random walk on {0,...,2N} with absorbing barriers at 0 (loss) and 2N (fixation)
  → Var(Δp) = p(1-p)/2N: variance shrinks as N grows (drift weakens)
  → Drift dominates selection when s < 1/(2N) (signal buried in noise)

COALESCENT = TIME-REVERSAL OF WRIGHT-FISHER

  Instead of simulating forward (allele frequencies), ask backward:
  "When did any two sampled lineages last share a common ancestor?"

  For a sample of k lineages:
    Rate of any pair coalescing = C(k,2) / N_e per generation
    Expected wait time for first coalescence: 2N_e / C(k,2) generations

  PARALLEL TO COUPON COLLECTOR:
    Collecting k distinct items from N possible = expected N·H_k draws
    Coalescent: k lineages need to find common ancestors = O(N log k) generations

  PARALLEL TO RANDOM WALK / HITTING TIME:
    Allele frequency under neutral drift ≡ 1D random walk
    Fixation = hitting the boundary {0} or {2N}
    Expected hitting time from start p: ~4N_e generations (expected time to boundary)

MCMC CONNECTION:
  Bayesian phylogenetic inference (BEAST, MrBayes) uses MCMC to sample from
  P(tree, parameters | sequence data)
  The state space is tree topologies × branch lengths × model parameters
  Same Metropolis-Hastings framework as any posterior sampling problem —
  just with a combinatorial topology component in the state.
```

### The Wright-Fisher Model

```
Discrete generations. Each individual samples 2Ne alleles from previous generation.
P(k copies of A in generation t+1 | j copies in t) = Binomial(2N, j/2N)

Coalescent theory (Kingman, 1982): looking backward in time
  Two lineages coalesce (share common ancestor) at rate 1/(2Ne) per generation
  Expected coalescence time for k lineages: 2Ne/C(k,2) generations
  → Inference of Ne from sequence diversity
  → Foundation of most modern phylogeographic methods
```

### Molecular Evolution

```
Neutral theory (Kimura, 1968):
  Most molecular variation is selectively neutral (neither beneficial nor harmful)
  Evolutionary rate ∝ mutation rate for neutral sites
  Fixation: drift-driven (probability 1/2Ne for new neutral mutation)

Molecular clock: neutral sites evolve at constant rate per year (corrected for Ne)
  Used for phylogenetic dating

dN/dS ratio (= Ka/Ks = ω):
  dN = nonsynonymous substitution rate
  dS = synonymous substitution rate (neutral proxy)

  ω < 1: purifying selection (most functional proteins: ω ≈ 0.1–0.3)
  ω = 1: neutral evolution
  ω > 1: positive selection (some sites in immune genes, MHC, virus-host conflicts)

  McDonald-Kreitman test: compare polymorphism vs divergence at synonymous vs nonsynonymous
    Excess divergence at nonsynonymous → positive selection (adaptive evolution)
```

---

## Phylogenetics

### Tree Building Methods

```
Distance methods:
  Compute pairwise distances (Jukes-Cantor, Kimura 2-parameter for sequence evolution)
  UPGMA: assumes constant rate (molecular clock)
  Neighbor-joining (NJ): no clock assumption, fast, good for large datasets

Parsimony:
  Find tree requiring fewest changes to explain observed sequences
  Fast, intuitive, but sensitive to long-branch attraction artifacts

Maximum likelihood (ML):
  Find tree (topology + branch lengths) maximizing P(data | tree, model)
  Model of sequence evolution (GTR+Γ+I most common for DNA)
  RAxML, IQ-TREE: fast ML implementations

Bayesian (MCMC):
  Sample tree posterior P(tree | data) via MRBAYES, BEAST
  Incorporates model uncertainty, yields credible intervals
  BEAST: integrates divergence time estimation with fossil calibration

Bootstrap support: resample columns of alignment → repeat tree building → % support
```

### Key Concepts

```
Homology: same structure due to shared common ancestry
  Orthologues: homologs in different species (diverged by speciation)
  Paralogues: homologs in same organism (diverged by gene duplication)

Analogy (homoplasy): similar structure from convergent evolution, NOT common ancestry
  Bat wing, bird wing, pterosaur wing — analogy for flight; forelimb — homology

Clade (monophyletic group): common ancestor + all descendants
Paraphyletic: common ancestor + some but not all descendants (e.g., "reptiles" excludes birds)
Polyphyletic: members lack shared exclusive common ancestor
```

---

## Speciation

```
ALLOPATRIC (geographic isolation):
  Physical barrier separates populations → independent evolution
  → reproductive isolation accumulates → species barrier complete even if reunited
  Most common speciation mechanism (particularly for animals)

SYMPATRIC (same location):
  Differentiation without geographic barrier
  Mechanisms: polyploidy (most common in plants), host-race formation (insects),
  assortative mating, disruptive selection
  Controversial in animals; well-documented in plants (allopolyploidy)

REPRODUCTIVE ISOLATION MECHANISMS:
  Pre-zygotic:
    Habitat isolation: different microhabitats
    Temporal isolation: different breeding seasons
    Behavioral isolation: mate recognition (song, display, pheromones)
    Mechanical isolation: incompatible morphology
    Gametic isolation: sperm-egg incompatibility

  Post-zygotic:
    Hybrid inviability: hybrid dies before reproducing
    Hybrid sterility: hybrid survives but infertile (mule = horse × donkey)
    Hybrid breakdown: F1 fertile, F2 reduced fitness

Haldane's rule: in F1 hybrids, when only one sex is sterile/inviable, it's the
  heterogametic sex (XY in mammals, ZW in birds)
```

---

## Evo-Devo

```
KEY INSIGHT: major morphological differences between animal body plans often
arise from changes in WHEN, WHERE, and HOW MUCH developmental genes are
expressed — not from changes in the genes themselves.

Hox genes:
  Transcription factors that specify body axis identity (anterior-posterior)
  Conserved across all bilaterians (fly Antennapedia homologous to human HOXB6)
  Collinear: expressed in same order along chromosome as along A-P axis
  Loss-of-function: homeotic transformations (antenna → leg in Drosophila Antennapedia)
  Vertebrate: 4 Hox clusters (A-D) from ancestral single cluster (2 rounds WGD)

Pax6: master regulator of eye development
  Conserved: fly eyeless, mouse/human Pax6 — overexpression induces ectopic eyes
  "Deep homology": eye evolved once, diversified (compound, camera, pinhole)

Modularity:
  Development organized into semi-independent modules (limb, eye, segment)
  Allows independent evolution of parts without disrupting others
  Cis-regulatory modules (enhancers): combinatorial TF inputs → specific expression patterns

Heterochrony: change in timing/rate of developmental events
  Neoteny (paedomorphosis): retention of juvenile features into adulthood
    Example: axolotl retains larval form (never metamorphoses — neotenic salamander)
    Human hypothesis: neotenic features (large brain, flat face, playfulness) vs apes

Developmental constraints:
  Not all mutations are equally accessible — some require multiple simultaneous changes
  Explains: conservation of body plans despite molecular-level variation
  Vertebrate limb: 5-digit (pentadactyl) body plan highly conserved since Devonian
```

---

## Decision Cheat Sheet

| Question | Concept | Key tool |
|----------|---------|----------|
| Carrier frequency of recessive disease? | Hardy-Weinberg | q = √(disease freq); carrier = 2pq |
| Is locus under positive selection? | dN/dS | ω > 1 → positive selection |
| What maintains sickle cell allele? | Overdominance | Heterozygote advantage in malaria zones |
| Why do small populations lose diversity? | Genetic drift | Var(Δp) = p(1−p)/2Ne; fixation by chance |
| Why can't male mules reproduce? | Post-zygotic isolation | Hybrid sterility — Haldane's rule applies |
| Which tree-building method gives confidence intervals? | Bayesian | BEAST/MrBayes → posterior credible intervals |
| Why are Hox mutations homeotic (not lethal)? | Modularity | Regional specification genes — change identity, not viability |
| What does a bottleneck do to Ne? | Harmonic mean | Single generation of N=10 dominates Ne even if usually N=10,000 |
| Are synonymous mutations really neutral? | Nearly neutral | Codon usage affects translation speed, mRNA stability — not truly neutral |

---

## Common Confusion Points

**Natural selection ≠ "survival of the fittest"**
Fitness = reproductive success, not physical strength.
Selection favors alleles that increase the number of descendants, regardless of
how "fit" the organism appears. Peacock tails reduce survival but increase mating success
(sexual selection). "Fittest" survives in the sense of "leaves most offspring."

**Genetic drift is not selection — and it dominates for small Ne**
A beneficial mutation (s = 0.01) in a population of N = 100 has probability
~1/(2N) + s/(2) ≈ 2% of fixation — mostly drift-determined.
Drift dominates when s < 1/(2Ne). For human Ne ~10,000: drift dominant for |s| < 0.0001.
Most new mutations, even slightly beneficial ones, are lost by drift.

**Neutral theory ≠ "nothing is adaptive"**
Kimura argued most MOLECULAR variation is neutral — not most phenotypic variation.
The neutral theory is about substitution rates at the molecular level.
Morphological and behavioral evolution can still be largely adaptive.
These operate at different timescales and levels — not contradictory.

**Homology vs analogy is about history, not similarity**
Bat wing and bird wing are superficially similar (convergent function) but not homologous
(different developmental origin, different bones modified).
Bat forelimb and human arm are homologous despite different appearance.
Molecular homology: orthologues can have diverged sequences while retaining homology.

**Speciation is not goal-directed**
Populations don't "decide" to speciate. Isolation + independent mutation accumulation
+ natural selection → divergence. Reproductive isolation is an emergent outcome,
not the purpose. The process has no target or directionality.
