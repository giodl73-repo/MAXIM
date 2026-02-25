# Molecular Evolution and Neutral Theory

## The Big Picture

Molecular evolution studies how DNA and protein sequences change over time.
The dominant paradigm — Kimura's neutral theory — holds that most molecular
evolution is selectively neutral, driven by drift rather than selection.

```
┌──────────────────────────────────────────────────────────────────┐
│              MOLECULAR EVOLUTION LANDSCAPE                        │
│                                                                    │
│  INPUT                  FORCES                OUTPUT              │
│  ─────                  ──────                ──────              │
│  Mutation               Purifying selection   Sequence divergence │
│  Recombination          Positive selection    Polymorphism level  │
│  Gene duplication       Neutral drift         Gene family size    │
│  Horizontal transfer    Codon usage bias      GC content          │
│                         Methylation           Substitution rate   │
│                                                                    │
│  KEY TOOL: dN/dS ratio (ω = Ka/Ks)                               │
│  ─────────────────────────────────                               │
│  ω < 1:  purifying selection (most genes)                        │
│  ω = 1:  neutral (pseudogenes, some introns)                     │
│  ω > 1:  positive selection (immune, reproductive genes)         │
│                                                                    │
│  MOLECULAR CLOCK: neutral substitution rate ≈ μ (mutation rate)  │
│  Calendar time → sequence divergence → divergence dates          │
└──────────────────────────────────────────────────────────────────┘
```

---

## Kimura's Neutral Theory (1968)

### The Core Claim

Most DNA polymorphisms and most evolutionary substitutions are selectively neutral
(or nearly so). They drift to fixation or loss without regard to fitness effects.

This was controversial in 1968 — the classical school expected most variation to
be maintained by balancing selection. The data from protein electrophoresis showed
far too much variation for selection to maintain.

### The Key Equation

Rate of neutral substitution per site per generation = μ (mutation rate per site).

Derivation:
```
  In a population of N diploid individuals (2N gene copies):
  - Rate of new mutations per gene per generation: μ (per site × number of sites)
  - Probability that a new neutral mutation fixes: 1/(2N)
  - Number of new neutral mutations per generation: 2N·μ (per site across all copies)
  - Rate of fixation: 2N·μ × 1/(2N) = μ

  Rate of neutral evolution = μ, independent of population size N
```

This is striking: the substitution rate does not depend on population size, only
on mutation rate. Compare to beneficial mutations: rate ∝ N·μ·s·(probability of
fixation given beneficial) — strongly population-size dependent.

---

## The Nearly Neutral Theory (Ohta)

Kimura assumed strictly neutral mutations. Ohta extended to "nearly neutral" —
mutations with |s| << 1/(N_e) that behave as if neutral in small populations
but are selected in large populations.

```
  Large N_e population:
    Even very small s effects are "seen" by selection
    Nearly deleterious mutations are purged efficiently
    Higher average fitness; cleaner genome

  Small N_e population:
    Nearly neutral mutations drift freely
    Slightly deleterious mutations accumulate
    Mutational meltdown in extreme cases
```

This predicts:
- Stronger purifying selection signature in large-population species (bacteria)
- More slightly deleterious variation in small-population species (humans)
- Effective genome size inversely related to N_e (Lynch's work: larger genomes in
  species with smaller N_e because introns / transposons not efficiently purged)

---

## Types of Substitution

```
  DNA level:
  ──────────
  Synonymous (silent):     codon change that doesn't alter amino acid
                           (UCU → UCC, both = serine)
  Nonsynonymous:           codon change that alters amino acid
                           Conservative: similar biochemical properties
                           Radical: different properties
  Nonsense:                creates stop codon
  Indel:                   insertion or deletion (frameshift if not mod 3)

  Transition vs. transversion:
  ────────────────────────────
  Transition:   purine → purine (A↔G) or pyrimidine → pyrimidine (C↔T)
                More common (transition/transversion ratio Ti/Tv ≈ 2)
  Transversion: purine → pyrimidine or vice versa
                Less common
```

---

## dN/dS Ratio — The Main Diagnostic

```
  dS = synonymous substitution rate per synonymous site
       (tracks the neutral molecular clock — just drift + mutation)

  dN = nonsynonymous substitution rate per nonsynonymous site
       (tracks amino acid change — affected by selection)

  ω = dN/dS

  Interpretation:
  ───────────────
  ω < 1:  purifying selection — most amino acid changes are deleterious
           Most proteins: ω ≈ 0.1-0.3
  ω = 1:  neutral — amino acid changes fix at same rate as silent changes
           Pseudogenes, relaxed constraint regions
  ω > 1:  positive selection — amino acid changes fix faster than silent changes
           Rapidly evolving genes: immune (MHC), venom, male reproductive, viral
```

### Caveat: site-specific selection
Many genes show ω > 1 at only a subset of sites (codons under positive selection
embedded in a gene mostly under purifying selection). Site-by-site analysis with
models like PAML M7/M8 is required to detect this.

### Application: Finding positively selected genes

```
  1. Align orthologous protein-coding sequences across species
  2. Compute dN and dS for each branch and each codon
  3. Sites with ω > 1 on certain branches: adaptive evolution
  4. Notable examples:
     - HIV envelope gp120: ω >> 1 (immune escape)
     - Primate MHC genes: ω > 1 at peptide-binding residues
     - Sperm-egg recognition proteins: among fastest-evolving in genome
     - Lysozyme: convergent positive selection in foregut fermenters
```

---

## Molecular Clock

### The Concept

If substitution rate r (substitutions per site per unit time) is constant across
lineages, then sequence divergence D between two taxa equals 2·r·t (where t =
divergence time, and the factor of 2 accounts for both branches accumulating changes).

```
  D = 2·r·t  →  t = D / (2·r)
```

Calibrate r using dated fossil evidence → date other splits without fossils.

### Strict vs. Relaxed Clocks

```
  STRICT CLOCK                      RELAXED CLOCK
  ────────────                      ─────────────
  r constant across all branches    r varies per branch
  First assumed by Zuckerkandl &    Implemented in BEAST (Bayesian
  Pauling (1965)                    Evolutionary Analysis by Sampling
  Falsified for many genes          Trees)
  Still useful for approximate      Uses Markov chain Monte Carlo
  dating                            integrates over rate uncertainty
```

### Substitution models (for phylogenetics)

DNA evolves with different rates for different types of substitution. Models
(Jukes-Cantor, HKY, GTR) correct for multiple substitutions at the same site
(saturation):

```
  JC69:   all substitutions equal rate, equal base frequencies
  K80:    transitions vs. transversions different rates
  HKY85:  unequal base frequencies + Ti/Tv ratio
  GTR:    general time-reversible (6 rate parameters + 4 base freqs)
  GTR+Γ:  GTR with gamma-distributed rate variation across sites
  GTR+Γ+I: also allows invariable sites

  Rule of thumb: GTR+Γ+I is the standard workhorse for molecular phylogenetics
```

---

## Gene Duplication and Gene Families

Gene duplication provides raw material for functional innovation without destroying
existing function.

```
  Duplication event
         │
         ├──────────────────────────────────────────────┐
         │                                               │
  Copy 1 (original function)                   Copy 2 (free to evolve)
         │                                               │
         │                                    ┌──────────┴──────────┐
         │                               Neofunctionalization   Pseudogenization
         │                               (new function)         (neutral evolution,
         │                                                        nonfunctional)
         │
  Subfunctionalization: both copies retain partial ancestral functions
  (division of labor between paralogs)
```

Examples:
- Vertebrate globin gene family: α and β subunits, fetal hemoglobin HbF, myoglobin
- Olfactory receptor genes: largest gene family in mammals (~400 in humans)
- HOX gene clusters: arose by duplication of ancestral Hox cluster (see 06-EVO-DEVO)

---

## Horizontal Gene Transfer (HGT)

In bacteria and archaea, HGT (gene transfer between non-parent-offspring lineages)
is pervasive. It complicates phylogenetics (the "tree of life" is actually a web).

```
  HGT mechanisms in bacteria:
  ───────────────────────────
  Transformation:  uptake of free DNA from environment
  Transduction:    phage carries DNA from one bacterium to another
  Conjugation:     direct cell-to-cell transfer via pili (plasmids)
  Integrons:       site-specific recombination, mobile gene cassettes

  Impact:
  ───────
  Antibiotic resistance genes spread horizontally across genera in years
  Metabolic pathway genes acquired wholesale
  Pathogenicity islands: blocks of virulence genes transferred as units
  ~10-50% of any given bacterial genome is HGT-acquired
```

In eukaryotes, HGT is rarer but documented: bdelloid rotifers have acquired
hundreds of bacterial genes; some plant genes from bacteria; mitochondria and
chloroplasts themselves are ancient HGT events (endosymbiosis).

---

## Detecting Selection in Genomic Data

### Population-level tests (within-species polymorphism)

**Tajima's D**:
```
  D = (θ_π - θ_W) / sqrt(Var(θ_π - θ_W))

  θ_π = average pairwise differences (sensitive to intermediate-freq variants)
  θ_W = Watterson's estimate (sensitive to all variants equally)

  D < 0: excess of rare variants → recent positive selection (sweep) or
         population expansion
  D > 0: excess of intermediate-freq variants → balancing selection or
         population contraction
  D ≈ 0: consistent with neutral equilibrium
```

**McDonald-Kreitman test**: compare dN/dS within species (polymorphism) to between
species (divergence). Under neutrality, the ratio of nonsynonymous to synonymous
should be the same in both. Excess nonsynonymous divergence = positive selection;
excess nonsynonymous polymorphism = slightly deleterious.

**Extended Haplotype Homozygosity (EHH)**: measures how far a haplotype extends in
LD. Rapid sweep → long high-LD haplotype. Used in iHS, XP-EHH statistics for GWAS
selection scans.

---

## Ancient DNA — Molecular Evolution in Real Time

Ancient DNA (aDNA) from bones, teeth, permafrost specimens allows direct measurement
of evolutionary changes over historical time:

```
  Key insights from aDNA:
  ────────────────────────
  - European hunter-gatherers, early farmers, steppe pastoralists: three major
    ancestry components in modern Europeans, mixed 8,000-2,500 ya
  - Neanderthal admixture into non-Africans: 1-3% of genome
  - Denisovan admixture in Melanesians / Tibetans (EPAS1 high-altitude adaptation)
  - Yamnaya steppe expansion ~3000 BCE correlated with IE language spread
  - Lactase persistence LCT-13910*T allele rose from 0→90% in Europe in 5,000 years
    → selection coefficient s ≈ 0.02 (one of the strongest known in humans)
```

aDNA + selection scans = molecular evolution observed directly at human-relevant
time scales. This is the intersection of population genetics, molecular evolution,
and archaeology.

---

## Decision Cheat Sheet

| Question | Method | Threshold/Result |
|----------|--------|-----------------|
| Is a gene under positive selection? | dN/dS > 1 | ω > 1 |
| Is a gene under purifying selection? | dN/dS << 1 | ω typically 0.1-0.3 |
| When did two lineages diverge? | Molecular clock | t = D/(2r) |
| Is there recent selection at a locus? | Tajima's D, iHS, EHH | D << 0, long haplotype |
| Is there balancing selection? | Tajima's D, MK test | D >> 0, excess poly. |
| Did HGT occur? | Gene tree vs. species tree incongruence | Deep branch in wrong place |
| What substitution model? | AIC model comparison | GTR+Γ+I default |

---

## Common Confusion Points

**Neutral evolution is not "random" in the sense that anything can happen.** Drift is
random, but the mutation process is biased by chemistry (transitions more frequent
than transversions, CpG sites hypermutable). Neutral evolution follows regular
statistical patterns — this is why the molecular clock works.

**dN/dS > 1 on average does not mean every codon is under positive selection.**
Use codon-by-codon models (PAML). Most codons in any gene have ω << 1; a few
functional residues drive the signal.

**Molecular clocks are not perfect clocks.** Generation time, metabolic rate,
repair efficiency, and selection pressure all affect substitution rate. Relaxed
clock models accommodate this. Results are calibration-dependent; fossil ages
have uncertainty that propagates into divergence time estimates.

**Gene trees are not species trees.** Incomplete lineage sorting (deep coalescence)
means alleles from species A can be more similar to alleles in species B than to
other alleles in species A, even without HGT or hybridization. This is common when
speciation events are rapid (human-chimp-gorilla trichotomy: many gene trees support
human-gorilla grouping even though species tree has human-chimp).

**Pseudogenes evolve neutrally, not randomly.** A pseudogene that has lost its
function will accumulate synonymous and nonsynonymous substitutions at roughly
equal rates (ω ≈ 1). Comparing ω in a functional gene to a pseudogene controls
for structural constraints on the DNA itself.
