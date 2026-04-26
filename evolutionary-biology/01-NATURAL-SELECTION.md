# Natural Selection: Mechanism and Evidence

## The Big Picture

Natural selection is the only known mechanism that systematically produces adaptation.
Every other evolutionary force (drift, mutation, gene flow) is directionless with
respect to function. Selection alone links environment to heritable change.

```
┌────────────────────────────────────────────────────────────────┐
│                  NATURAL SELECTION ENGINE                      │
│                                                                │
│  PREREQUISITES (all three required simultaneously):            │
│  ─────────────                                                 │
│  1. VARIATION         Individuals differ in some trait         │
│  2. HERITABILITY      Offspring resemble parents for that trait │
│  3. FITNESS EFFECT    Variants differ in survival/reproduction │
│                              │                                 │
│                              ▼                                 │
│           Allele frequencies change across generations         │
│                              │                                 │
│                              ▼                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  TYPES BY FITNESS LANDSCAPE SHAPE                        │  │
│  │                                                           │  │
│  │  Directional:   one extreme favored                      │  │
│  │  Stabilizing:   intermediate favored                     │  │
│  │  Disruptive:    both extremes favored                    │  │
│  │  Balancing:     multiple alleles maintained              │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘
```

---

## Darwin's Logic — Reconstructed

Darwin's argument in *On the Origin of Species* (1859) is a deductive syllogism:

```
Premise 1: More offspring are produced than can survive (Malthus)
Premise 2: Individuals vary in heritable traits
Premise 3: Some variants survive and reproduce better
─────────────────────────────────────────────────────
Conclusion: Those variants become more common over generations
```

What Darwin lacked: a mechanism for inheritance. Mendel's discrete particles (1865)
solved this, but the synthesis took until 1918 (Fisher).

---

## Fitness: Formal Definition

Fitness is not "strength" or "health." It is a precise quantity:

```
  Fitness W of genotype g = expected number of offspring in the next generation
                            (relative to other genotypes in the same population)
```

Absolute fitness: W
Relative fitness: w = W / W_max  (ranges 0 to 1)

Selection coefficient s: s = 1 - w  (deviation from maximum fitness)
Dominance coefficient h: controls heterozygote fitness

```
  Genotype    Fitness (general diploid model)
  ──────────  ──────────────────────────────
  AA          1
  Aa          1 - hs
  aa          1 - s

  h = 0:  A is fully dominant (aa selected against, Aa normal)
  h = 1:  A is fully recessive (only aa has full fitness)
  h = 0.5: additive (heterozygote intermediate)
  h > 1:  overdominance (heterozygote more fit than either homozygote)
```

**Overdominance** = mechanism for balancing selection (sickle cell / malaria is the
canonical example: HbS/HbA heterozygote is more fit than either homozygote in
malaria-endemic regions).

---

## The Selection Equation — Derivation

Start with genotype frequencies at Hardy-Weinberg equilibrium.
Let p = frequency of A, q = 1-p = frequency of a.

```
  Before selection:
    f(AA) = p²       f(Aa) = 2pq       f(aa) = q²

  After viability selection (multiply by fitness, normalize):
    f'(AA) = p²·W_AA / w̄
    f'(Aa) = 2pq·W_Aa / w̄
    f'(aa) = q²·W_aa / w̄

  Mean fitness: w̄ = p²·W_AA + 2pq·W_Aa + q²·W_aa

  New allele frequency of A:
    p' = [p²·W_AA + pq·W_Aa] / w̄

  Change per generation:
    Δp = p' - p = p·q·[p(W_AA - W_Aa) + q(W_Aa - W_aa)] / w̄
```

This is the fundamental equation of natural selection for a diploid locus.

### Special cases

**Additive (no dominance), W_AA = 1+2s, W_Aa = 1+s, W_aa = 1:**
```
  Δp ≈ spq    (for small s, p not at extremes)
```

**Rate of frequency change is maximum when p ≈ 0.5** — selection is fastest when
both alleles are at intermediate frequency. At extremes (p near 0 or 1), selection
is slow because the disadvantaged genotype is rare.

---

## Types of Selection — Visual

```
  DIRECTIONAL SELECTION
  ─────────────────────
  Frequency
      │ Before: ────────/\────────
      │ After:           ────────/\──
      └──────────────────────────────→ Trait value
      Shifts the mean; reduces variance if sustained

  STABILIZING SELECTION
  ─────────────────────
  Frequency
      │ Before: ────/\────
      │ After:      /\\      (sharper peak)
      └────────────────────→ Trait value
      Maintains the mean; reduces variance
      Example: human birth weight (too small = premature, too large = difficult delivery)

  DISRUPTIVE SELECTION
  ────────────────────
  Frequency
      │ Before:    /\
      │ After:  /\    /\    (bimodal)
      └────────────────────→ Trait value
      Can drive speciation if coupled with assortative mating

  BALANCING SELECTION
  ───────────────────
  Multiple alleles maintained indefinitely
  Mechanisms: overdominance, frequency-dependent, spatiotemporally variable
```

---

## Selection vs. Drift — The 4Nes Rule

For a new mutation with selection coefficient s in a population of effective size N_e:

```
  4·N_e·s >> 1:  selection dominates — mutation behaves deterministically
  4·N_e·s ≈ 1:   selection and drift compete
  4·N_e·s << 1:  drift dominates — mutation behaves as if neutral
```

This is the most important criterion in population genetics. Large N_e means even
small s values are effectively selected. Small N_e (bottleneck, island population)
means moderately deleterious mutations can fix by drift.

Example: N_e ≈ 10,000 for humans (far smaller than census size due to historical
bottlenecks). So 4Nes = 1 at s = 0.000025 — selection is only "strong" for
mutations with >0.0025% fitness effect.

---

## Hard Sweeps vs. Soft Sweeps

```
  HARD SWEEP (classic selective sweep)
  ─────────────────────────────────────
  Single new mutation arises → beneficial → sweeps to fixation
  Signature: loss of diversity around the selected site
  Linkage disequilibrium haplotype "hitchhikes" to high frequency

  SOFT SWEEP
  ──────────
  Selection acts on:
  (a) Standing variation — allele already at some frequency when environment changes
  (b) Multiple independent origins of the same mutation
  Signature: diversity less depleted; multiple haplotypes at the selected locus
  Common in humans (most human adaptation appears to be soft sweeps)
  Example: lactase persistence — multiple independent mutations in regulatory region
           in cattle-herding populations on different continents
```

---

## Levels of Selection

Selection can act at multiple levels simultaneously:

```
  Genes          Selfish genetic elements, transposons, meiotic drive
  Individuals    Classic organismal selection
  Kin groups     Kin selection (Hamilton's rule: r·B > C)
  Populations    Group selection (species selection in macroevolution)
  Species        Species sorting in macroevolution
```

Hamilton's rule: an altruistic act evolves if r·B > C, where:
- r = coefficient of relatedness between actor and beneficiary
- B = fitness benefit to beneficiary
- C = fitness cost to actor

Kin selection is not an alternative to natural selection — it *is* natural selection
operating through inclusive fitness.

---

## Evidence for Natural Selection

### Direct observation
- **Biston betularia** (peppered moth): industrial melanism, documented in real time
- **Antibiotic resistance**: bacteria evolving resistance in clinical settings, years
- **Darwin's finches**: beak depth tracked drought cycles — Grant & Grant measured it
- **HIV within a patient**: rapid evolution of drug resistance, sequenced directly

### Molecular signatures
- **dN/dS ratio**: ratio of nonsynonymous to synonymous substitution rates
  - dN/dS < 1: purifying selection (most proteins)
  - dN/dS = 1: neutral
  - dN/dS > 1: positive selection (immune genes, virulence factors, sperm proteins)
- **Selective sweeps**: regions of reduced diversity flanking a recently fixed allele
- **Population differentiation**: FST outliers (alleles unusually differentiated
  across populations — local adaptation signals)

### Experimental
- **E. coli LTEE** (Lenski): 60,000+ generations, fitness increases roughly log-linear
  with time, with occasional large-effect mutations
- **Yeast fitness landscapes**: all combinations of N mutations measured; epistasis
  abundant

---

## Adaptation: What It Is and Isn't

An adaptation is a trait that:
1. Evolved by natural selection
2. Improves fitness in a specific environment
3. Is not currently maintained merely by chance

Criteria: comparative method (is the trait homologous or convergent?), experimental
manipulation (does removing/altering the trait reduce fitness?), molecular signatures.

**Exaptation**: a trait originally selected for one function co-opted for another.
Bird feathers: likely selected for insulation, co-opted for flight.

**Spandrel** (Gould & Lewontin 1979): architectural by-product of building one trait
that is not itself an adaptation. The chin is not an adaptation; it is a geometric
consequence of the lower jaw and face evolving independently.

This debate — how much of phenotype is adaptation vs. constraint/spandrel — is
central to the Extended Evolutionary Synthesis.

---

## Optimization and Signal Processing Bridge

Selection, heritability, and the drift threshold are optimization and signal
processing concepts with exact formal mappings:

```
SELECTION AS GRADIENT ASCENT:

  Fitness landscape W(genotype): maps genotype space → R (fitness value)
  Selection equation:  Δp = p·q·[p(w₁₁-w₁₂) + q(w₁₂-w₂₂)] / w̄

  This is gradient ascent on mean fitness w̄:
    Δw̄ ∝ (∂w̄/∂p) · Var(p) × selection_strength
  Fisher's Fundamental Theorem: rate of increase of mean fitness =
    additive genetic variance in fitness (exact analog of gradient magnitude)

  Epistasis = non-convexity: fitness interaction between loci →
    multiple local optima on the landscape →
    Wright's "problem of peaks": populations can get stuck at local optima
    Drift = stochastic perturbation to escape local optima (same role as
    momentum / noise in SGD escaping sharp minima)

BREEDER'S EQUATION AS SGD:

  R = h² · S

  R = response (parameter update Δθ)
  S = selection differential (gradient estimate from data)
  h² = narrow-sense heritability = fraction of variation that is "signal"
     = V_A / V_P = additive variance / total phenotypic variance
     ≈ effective learning rate × signal-to-noise ratio

  If h² = 0: no heritable variation → no response (like zero learning rate)
  If h² = 1: all variation is additive genetic → maximal response
  h² < 1:   noise (environmental variance V_E) reduces effective learning

4Nes AS SIGNAL-TO-NOISE RATIO:

  Effective selection: benefit = s (selection coefficient per generation)
  Drift noise: σ²(Δp) = p(1-p)/(2Ne) ≈ 1/(8Ne) at p = 0.5

  SNR analog: beneficial allele is "detectable" above drift noise when:
    s >> 1/(2Ne)  →  4Nes >> 1

  Below threshold (4Nes < 1): allele behaves as effectively neutral
    → fixed by drift with probability ~1/(2Ne) (same as neutral allele)
  Above threshold (4Nes >> 1): probability of fixation ≈ 2s
    → selection is the dominant force

  This is exactly the SNR threshold in detection theory:
    signal power s² vs. noise power σ² = 1/(2Ne)
    SNR = s / σ = s·√(2Ne) ∝ s·√Ne
```

## Decision Cheat Sheet

| Scenario | Framework | Key quantity |
|----------|-----------|-------------|
| Is selection strong enough to matter? | 4Nes criterion | s > 1/(4Ne) |
| How fast will a sweep complete? | Duration ≈ 2ln(2N)/s generations | s, N |
| Is heterozygote advantage maintaining polymorphism? | Overdominance | W_Aa > W_AA, W_aa |
| Is a gene under positive selection? | dN/dS > 1 | ω ratio |
| Why is diversity low near a gene? | Selective sweep or background selection | LD, haplotype |
| What maintains a rare allele? | Frequency-dependent or balancing | fitness at low freq |

---

## Common Confusion Points

**Selection does not produce variation.** Mutation and recombination produce variation.
Selection only changes frequencies of existing variants.

**Selection on quantitative traits is not the same as single-locus analysis.** For
traits controlled by many loci, use the breeder's equation: R = h²·S, where R is
response to selection, h² is heritability, S is selection differential. This is the
framework for plant and animal breeding — the foundation of modern agriculture.

**"Survival of the fittest" is misleading.** Reproduction, not just survival, is the
currency. A tree that lives 1000 years but produces no viable seeds has fitness zero.

**Neutral and adaptive evolution are not mutually exclusive.** Most of the genome
evolves neutrally; selected sites are embedded in a background of neutral change.
This is why comparative genomics works — functionally important regions stand out
against the neutral background.

**Background selection vs. selective sweeps.** Both reduce diversity around a
selected locus, but by different mechanisms. Selective sweeps drive a beneficial
allele to fixation (positive selection). Background selection purges diversity
near deleterious mutations (purifying selection). Both create similar genomic
signatures — distinguishing them requires detailed analysis.
