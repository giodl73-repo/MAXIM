# Population Genetics: Hardy-Weinberg and Drift

## The Big Picture

Population genetics is the mathematical theory of how allele frequencies change over
time under the four evolutionary forces. It is the quantitative backbone of modern
evolutionary biology.

```
┌──────────────────────────────────────────────────────────────────┐
│               EVOLUTIONARY FORCES ON ALLELE FREQUENCY            │
│                                                                    │
│  FORCE           DIRECTION        SPEED        PREDICTABLE?      │
│  ─────           ─────────        ─────        ────────────      │
│  Selection       Toward fitness   Fast (large s)   Yes          │
│  Genetic drift   Random           Faster in        No (stoch.)  │
│                                   small N                        │
│  Mutation        Toward new       Very slow         Yes (μ)     │
│                  alleles          (~10⁻⁸/bp/gen)                │
│  Gene flow       Toward source    Depends on        Yes (Fst)   │
│                  population       migration rate                  │
│                                                                    │
│  NULL: HARDY-WEINBERG EQUILIBRIUM                                 │
│  ─────────────────────────────────                               │
│  No forces acting → allele frequencies constant, genotype       │
│  frequencies = p², 2pq, q² forever                               │
└──────────────────────────────────────────────────────────────────┘
```

---

## Hardy-Weinberg Equilibrium — Derivation

Hardy (mathematician) and Weinberg (physician) independently derived this in 1908.
It is a theorem, not an empirical observation.

### Setup
- Single autosomal locus, two alleles: A (frequency p) and a (frequency q)
- p + q = 1 by definition
- Infinite population (no drift)
- Random mating (no assortative mating)
- No selection (all genotypes equally fit)
- No mutation
- No migration

### Derivation
Random mating is equivalent to random sampling of gametes. Gamete pool:
frequency of A gametes = p, frequency of a gametes = q.

Probability of producing each diploid genotype by random combination:

```
  Gametes unite randomly:

        A (prob p)    a (prob q)
       ┌────────────┬────────────┐
  A    │  AA  p·p   │  Aa  p·q   │   (prob p)
       ├────────────┼────────────┤
  a    │  Aa  q·p   │  aa  q·q   │   (prob q)
       └────────────┴────────────┘

  f(AA) = p²
  f(Aa) = 2pq   (two ways to produce it: Ap×aq or ap×Aq)
  f(aa) = q²

  Check: p² + 2pq + q² = (p + q)² = 1² = 1  ✓
```

### One-generation property
If the population starts at ANY genotype frequencies (not H-W), after ONE generation
of random mating the population reaches H-W proportions and stays there.

### What H-W tells you
H-W is the null hypothesis. If observed genotype frequencies deviate from expected
p², 2pq, q², one of the five assumptions is violated. Which one is then the
scientific question.

```
  Observed excess of homozygotes:   inbreeding, population subdivision (Wahlund effect)
  Observed excess of heterozygotes: overdominant selection, or genotyping error
  Allele frequency differs by sex:  X-linked locus, sex-specific selection
```

---

## Genetic Drift — The Wright-Fisher Model

Drift is sampling error. In a finite population, the next generation is a random
sample from the current generation's gametes.

### The Model

N diploid individuals → 2N gene copies. Each individual in generation t+1 is formed
by drawing two gene copies from generation t's gamete pool (with replacement).

The number of A copies in generation t+1 given k A-copies in generation t follows
a binomial distribution:

```
  X_{t+1} | X_t ~ Binomial(2N, X_t / 2N)

  E[X_{t+1}]    = X_t               (no expected change — unbiased)
  Var(X_{t+1})  = 2N · p · (1-p)    (where p = X_t / 2N)

  In terms of allele frequency p:
  Var(Δp) = p(1-p) / (2N)
```

This is the key variance equation. Variance per generation scales as 1/(2N) — the
smaller the population, the more random the change.

### Fixation and Loss

Starting at frequency p, eventual outcomes are:
- Fixation (allele reaches frequency 1): probability = p
- Loss (allele reaches frequency 0): probability = 1 - p

**Expected time to fixation**, given fixation occurs:
```
  E[T_fix] ≈ -4N · [(1-p)/(p)] · ln(1-p)    generations
```

For a new mutation: p = 1/(2N), so T_fix ≈ 4N generations.
In humans: N_e ≈ 10,000 → ~40,000 generations → ~1 million years.

**Effective population size N_e**
The size of an idealized Wright-Fisher population that would experience the same
amount of drift as the actual population. Always ≤ census size N.

```
  Source of N_e < N:
  ──────────────────
  Bottlenecks:          N_e ≈ 1 / Σ(1/N_t)   (harmonic mean)
  Unequal sex ratio:    N_e = 4·N_f·N_m / (N_f + N_m)
  Variance in reprod:   N_e ≈ 4N / (V_k + 2)  (V_k = variance in offspring number)
```

The harmonic mean is dominated by minimum values. One catastrophic bottleneck
(N_min = 10) massively reduces N_e even if the population recovers to millions.
This is why African populations have higher genetic diversity than non-African
populations: non-Africans descend from a small founding group (~50-100k years ago).

---

## Drift vs. Selection — Quantitative Border

For a mutation with selection coefficient s in population of effective size N_e:

```
  4·N_e·|s| >> 1:  selection dominates (deterministic)
  4·N_e·|s| ≈ 1:   transition zone (probabilistic, both matter)
  4·N_e·|s| << 1:  drift dominates (nearly neutral)
```

In humans (N_e ≈ 10,000): the boundary is |s| ≈ 0.000025.
In bacteria (N_e ≈ 10⁸): the boundary is |s| ≈ 2.5 × 10⁻¹⁰.

This is why bacteria are exquisitely tuned by selection (even tiny fitness differences
are effectively selected), while humans tolerate more slightly deleterious variation.

---

## Mutation-Selection Balance

Deleterious alleles enter the population by mutation and are removed by selection.
At equilibrium:

```
  q_eq ≈ √(μ/s)        for recessive lethal (h=0)
  q_eq ≈ μ/hs           for partially dominant (h > 0)
```

Most disease alleles are maintained at equilibrium between mutation input and
selection removal. For a fully recessive lethal (s=1, h=0) with μ ≈ 10⁻⁵:
q_eq ≈ √(10⁻⁵) ≈ 0.003 → about 1 in 30 people are carriers.
This matches observed cystic fibrosis carrier frequency (~1/25 in Northern Europeans).

---

## Population Structure

Real populations are not single random-mating units. They are subdivided.

### FST — The Key Statistic

```
  FST = (H_T - H_S) / H_T

  H_T = expected heterozygosity in total (pooled) population
  H_S = average expected heterozygosity within subpopulations

  FST = 0:   no differentiation — subpopulations are identical
  FST = 1:   complete differentiation — different alleles fixed in each
```

Interpretation: FST measures what fraction of total genetic diversity is between
subpopulations (as opposed to within).

Human FST values: ~0.12 across major continental populations. This means ~12% of
human genetic diversity is between continents — 88% is within populations. The
popular claim that "race explains little genetic variation" directly follows from
this number.

### Wright's Island Model

Migration rate m between subpopulations and drift balance at equilibrium:
```
  FST ≈ 1 / (1 + 4·N_e·m)
```

High gene flow → low FST. Small populations → high FST even with some migration.

### Isolation by Distance
FST increases with geographic distance (no discrete populations, just continuous
cline). Tested with Mantel test: correlation between genetic distance and
geographic distance matrices.

---

## Coalescent Theory

Rather than tracking allele frequencies forward in time, coalescent theory traces
genealogical lineages backward in time to their most recent common ancestor (MRCA).

```
  Present:   ● ● ● ● ● ● ● ● ● ●   (n gene copies in current population)
              \/ \/  |  \/ \/ \/
  Past:        ●  ●  ●   ●  ●       (lineages coalesce back in time)
                  \   \/   /
                   ●   ●
                    \ /
                     ●              (MRCA — most recent common ancestor)
```

Rate of coalescence: two lineages coalesce at rate 1/(2N_e) per generation.
Expected time to coalescence for two lineages: E[T_MRCA] = 2N_e generations.

This is why all human mitochondrial DNA traces to "Mitochondrial Eve" ~150,000 ya
and all Y chromosomes to "Y-chromosomal Adam" ~250,000 ya — these are not actual
individuals from whom all humans descend, they are just the MRCA of those specific
lineages.

---

## Linkage Disequilibrium (LD)

LD measures statistical association between alleles at different loci:

```
  D = f(AB) - f(A)·f(B)

  At linkage equilibrium (LE): allele frequencies independent, D = 0
  At LD: alleles are more or less common together than expected from
          their individual frequencies

  D decays over generations:  D_t = D_0 · (1 - r)^t

  r = recombination fraction between loci (r = 0.5 for unlinked)
```

LD decays faster with more recombination and more generations. In humans, LD
blocks typically extend ~10–50 kb in outbred populations.

**GWAS connection**: GWAS exploits LD. If disease variant and a typed SNP are in
LD, the SNP shows association. The typed variant is usually not the causal variant —
it is a proxy. Fine-mapping uses the LD structure to localize the causal variant
within an LD block.

---

## Quantitative Genetics

Most medically and agronomically important traits are quantitative (polygenic):
height, body mass index, blood pressure, intelligence proxies.

### Breeder's Equation
```
  R = h² · S

  R = response to selection (change in mean after selection)
  h² = narrow-sense heritability = V_A / V_P
       V_A = additive genetic variance
       V_P = total phenotypic variance
  S  = selection differential (mean of selected vs. mean of population)
```

This equation underlies all of animal and plant breeding. Heritability is not fixed —
it depends on the population and environment. Height h² ≈ 0.8 in developed countries
(most phenotypic variation is genetic); h² ≈ 0.4 in malnourished populations
(environment explains more variation).

**Bridge to ML**: The breeder's equation is essentially stochastic gradient descent
on a quadratic fitness surface. The response R is the parameter update, h² is the
learning rate × signal-to-noise ratio, S is the gradient. Genomic prediction
(BLUP/ridge regression) is regularized linear regression predicting phenotype from
genotype — the same mathematics as L2-regularized regression in any ML framework.

---

## Decision Cheat Sheet

| Question | Tool | Formula/threshold |
|----------|------|-------------------|
| Are genotype freqs at equilibrium? | Chi-squared test on H-W | p² + 2pq + q² |
| How much drift per generation? | Var(Δp) = p(1-p)/(2N) | Scales 1/N |
| Is selection effective vs. drift? | 4Nes criterion | >> 1 for selection |
| How differentiated are populations? | FST | 0 = none, 1 = complete |
| How much migration? | Island model | FST ≈ 1/(1+4Nm) |
| What is coalescence time? | Coalescent | E[T] = 2Ne generations |
| Can we predict phenotype from SNPs? | Genomic BLUP | Ridge regression |

---

## Common Confusion Points

**H-W requires infinite population.** In real populations, even without selection, drift
causes frequencies to change. H-W is a mathematical null, not a physical reality.

**Heritability is not "how genetic" something is.** It measures the proportion of
phenotypic variance attributable to additive genetic variance in a specific population
in a specific environment. If everyone gets the same environment, h² approaches 1
for almost any trait — but that does not mean the trait is insensitive to environment.

**FST of 0.12 does not mean "race is biologically meaningless."** It means most
genetic variation is within populations. But the between-population variation that
does exist is real, structured, and medically relevant (pharmacogenomics, disease
risk). The statement "there is more variation within groups than between" is
arithmetically true but has been misapplied in both directions.

**Coalescent MRCA is not a demographic ancestor.** The mitochondrial MRCA is the
most recent woman from whom all current mitochondrial lineages descend. Contemporaries
of that woman also contributed autosomal DNA to modern humans — their mitochondrial
lineages just went extinct by chance (drift).

**Effective population size is not census size.** N_e for humans ≈ 10,000 at various
historical time points despite census sizes in the millions. The discrepancy reflects
past bottlenecks and the variance in reproductive success.
