# Speciation: Mechanisms and Models

## The Big Picture

Speciation is the process by which one ancestral lineage splits into two or more
lineages that are reproductively isolated from each other. It is the origin of the
diversity of life.

```
┌──────────────────────────────────────────────────────────────────┐
│                    SPECIATION FRAMEWORK                           │
│                                                                    │
│  GEOGRAPHIC ARRANGEMENT          REPRODUCTIVE ISOLATION           │
│  ─────────────────────────       ──────────────────────          │
│  Allopatric: populations          Prezygotic:                    │
│    physically separated           - Ecological (habitat)        │
│    (mountain range, ocean)        - Temporal (season)           │
│                                   - Behavioral (mate choice)    │
│  Parapatric: adjacent zones       - Mechanical (morphology)     │
│    with limited contact           - Gametic (sperm-egg incomp.) │
│                                                                    │
│  Sympatric: same geographic       Postzygotic:                   │
│    area, diverging anyway         - Hybrid inviability          │
│                                   - Hybrid sterility (F1)       │
│  Peripatric: small peripheral     - Hybrid breakdown (F2)       │
│    population diverges            Dobzhansky-Muller model        │
└──────────────────────────────────────────────────────────────────┘
```

---

## Biological Species Concept

Mayr (1942): "Species are groups of actually or potentially interbreeding natural
populations which are reproductively isolated from other such groups."

This is the most widely used definition but has well-known failures:

| Situation | Problem with BSC |
|-----------|-----------------|
| Allopatric populations | "Potentially interbreeding" is untestable |
| Bacteria, asexuals | No interbreeding at all; the concept is inapplicable |
| Hybridizing plants | Many plant "species" hybridize freely |
| Fossil taxa | Cannot test reproductive isolation |
| Ring species | Endpoints cannot interbreed but connected by interbreeding intermediates |

Alternative concepts:
- **Phylogenetic species concept**: smallest clade diagnosable by shared derived characters
- **Ecological species concept**: lineage occupying a distinct adaptive zone
- **Cohesion species concept**: most inclusive population sharing mechanisms of
  cohesion (genetic exchangeability + ecological interchangeability)

The plurality of species concepts reflects the reality that "species" is a human
category imposed on a continuum of divergence.

---

## Allopatric Speciation

The dominant mode. Geographic barrier prevents gene flow; populations diverge
independently; secondary contact tests whether reproductive isolation has evolved.

```
  PROCESS:
  ─────────
  1. Ancestral population occupies continuous range
  2. Vicariance event: geographic barrier splits population
     (mountain uplift, sea level rise, continental drift, habitat change)
  3. Allopatric populations evolve independently
     - Genetic drift accumulates differences
     - Local adaptation drives divergence
     - Dobzhansky-Muller incompatibilities develop
  4. Secondary contact:
     - If RI complete: species coexist, character displacement
     - If RI partial: hybridization, hybrid zone
     - If RI minimal: populations merge (reticulation)

  EXAMPLES:
  ─────────
  Darwin's finches: multiple colonizations of Galápagos islands
  Hawaiian honeycreepers: single colonization → 50+ species
  Atlantic-Pacific sister species: Isthmus of Panama (3.5 mya)
  Eastern/Western US bird species: Pleistocene glacial refugia
```

### Peripatric Speciation

Variant of allopatric: a small peripheral isolate diverges from a large source
population. The founder effect + drift + local selection can drive rapid divergence.

Mayr's "genetic revolution" hypothesis: allele frequency changes in the founder
population alter epistatic interactions across the genome, potentially enabling
rapid phenotypic evolution.

---

## Dobzhansky-Muller Incompatibilities

The key mechanism by which reproductive isolation accumulates between allopatric
populations without requiring selection *for* isolation.

```
  Ancestral population:  genome contains alleles A (locus 1) and B (locus 2)
                         A and B interact — co-evolved

  Population splits:
    Population 1 evolves:   A → A*  (new derived allele at locus 1)
    Population 2 evolves:   B → B*  (new derived allele at locus 2)

    Within each population, the new allele is compatible with the other
    original allele (A* works fine with B; B* works fine with A).

    Hybrid: A* / B*  → never been together, may be incompatible
    → hybrid inviability or sterility

  Key insight: incompatibility arises by drift or local selection,
  NOT by direct selection for isolation
```

Snowball effect (Orr): the number of D-M incompatibilities grows faster than
linearly with divergence time, because each new derived allele can be incompatible
with ALL previously derived alleles in the other lineage. If k mutations have
occurred, possible incompatibilities scale as k(k-1)/2.

This predicts: reproductive isolation accumulates slowly at first, then accelerates.
Evidence: in Drosophila, older species pairs show faster-than-linear accumulation of
hybrid incompatibilities.

---

## Sympatric Speciation

Speciation within the same geographic area, without physical isolation. Controversial
because gene flow is expected to homogenize populations.

Requires: strong enough disruptive selection AND assortative mating (mate preference
correlated with the trait under selection) to overcome homogenizing gene flow.

```
  REQUIREMENTS FOR SYMPATRIC SPECIATION:
  ───────────────────────────────────────
  1. Disruptive selection: two ecological niches, both extremes favored
  2. Assortative mating: individuals prefer mates similar to themselves
  3. Sufficiently strong selection to overcome gene flow

  MODELS:
  ───────
  Ecological speciation: divergent natural selection drives RI
  Sexual conflict model: differential selection on males vs. females
  Parasite model: host shift drives ecological + reproductive isolation

  CLASSIC CASE: Apple maggot fly (Rhagoletis pomonella)
    - Originally on hawthorn
    - ~200 years ago: host shift to apple (introduced from Europe)
    - Flies now mate on their host fruit → assortative mating by host
    - Populations genetically differentiated and reproductively partially isolated
    - Ongoing sympatric divergence observable in real time
```

---

## Ring Species

A compelling demonstration that speciation is a continuum:

```
  Ring species example: Ensatina salamander in California

                    Northern California
                    (ancestral population)
                          /\
                         /  \
                        /    \
          West coast     │    │     East coast
          subspecies     │    │     subspecies
          chain          │    │     chain
          (interbreed    │    │     (interbreed
          with           │    │     with adjacent)
          adjacent)      │    │
                          \  /
                           \/
                    Southern California
                    (end-point populations)
                    DON'T interbreed with each other
                    → reproductively isolated
                    → by BSC: different species
                    But connected by interbreeding chain
                    → by BSC: same species
```

Ring species demonstrate that species boundaries are arbitrary cuts along a
continuum of divergence.

---

## Hybrid Zones

Where two partially differentiated populations meet and hybridize:

```
  TENSION ZONE MODEL:
  ───────────────────
  Hybrid zone maintained by balance between:
  - Selection against hybrids (endogenous selection)
  - Migration from flanking populations

  Hybrid zone width ∝ √(dispersal / selection)
  Narrow zones = strong selection against hybrids
  Wide zones = weak selection or high dispersal

  Two outcomes at secondary contact:
  (a) Reinforcement: selection strengthens prezygotic isolation
      (selecting against hybrids indirectly selects for assortative mating)
  (b) Fusion: gene flow overcomes divergence, populations merge

  Genetic consequence of hybrid zones:
  - "Genomic mosaic": neutral loci introgress freely, barrier loci resist
  - Barrier loci = genes involved in adaptation or incompatibility
  - Can identify "speciation genes" by which loci fail to introgress
```

---

## Speciation Genes

What genes actually cause reproductive isolation?

```
  KNOWN SPECIATION GENES / FACTORS:
  ──────────────────────────────────
  OdsH (Odysseus):    drives hybrid male sterility in Drosophila
                      rapidly evolving under positive selection
  Prdm9:              controls meiotic recombination hotspot positions;
                      hybrid males infertile when PRDM9 alleles mismatch
  Hmr, Lhr:           Drosophila hybrid lethality; encode chromatin proteins
  RBTN2 / speciation  Mimulus (monkeyflower): nuclear-cytoplasmic incompatibility
  genes in plants:    hybrid breakdown in F2
  EPAS1 (HIF-2α):     altitude adaptation in Tibetans (from Denisovan);
                      not speciation gene but shows how introgression blocks
                      between populations

  Pattern: speciation genes often encode:
  - Chromatin regulators
  - Meiotic machinery
  - Transcription factors
  - Nuclear-cytoplasmic interactions
  Why: these systems involve co-evolved molecular partners; mismatch = incompatibility
```

---

## Speciation Rate — Macroevolutionary Perspective

Why do some clades speciate faster than others?

```
  CORRELATES OF HIGH SPECIATION RATE:
  ────────────────────────────────────
  Island archipelago:       repeated colonization + isolation (Hawaii, Galápagos)
  Complex habitat:          mountain ranges create many allopatric isolates
  Sexual selection:         birds with elaborate plumage → larger genera
  Polyploidy in plants:     instant reproductive isolation by chromosome doubling
  Host shifting (insects):  specialization on different hosts → assortative mating
  Lake adaptive radiation:  African cichlids — >500 species in Lake Victoria alone
                             (<15,000 years old)
```

African cichlid radiation is the fastest known vertebrate speciation: hundreds of
species diverged since the last dry period emptied the lake. Driven by: sexual
selection on male coloration, trophic specialization, and shallow neutral genetic
divergence (many species more similar than human populations).

---

## Decision Cheat Sheet

| Situation | Expected speciation mode | Key signal |
|-----------|-------------------------|-----------|
| Island colonization | Allopatric / peripatric | Founder effects, rapid divergence |
| Mountain range barrier | Allopatric vicariance | Phylogeographic break |
| Host-plant shift (insects) | Sympatric / parapatric | Assortative mating on host |
| Polyploid plant | Instantaneous speciation | Chromosome number change |
| Hybridizing species at contact | Hybrid zone | Mosaic genome, barrier loci |
| Lake fish radiation | Ecological speciation | Trophic morphology divergence |

---

## Common Confusion Points

**Allopatric speciation doesn't require selection for isolation.** Drift and
incidental divergence are sufficient to accumulate D-M incompatibilities over
time. Selection accelerates this but is not required.

**Hybridization is not evidence against species status.** Many valid biological
species hybridize at low rates in contact zones. The question is whether the hybrid
zone is a stable equilibrium (maintained by selection) or a transient mixing event.

**Sympatric speciation is not the norm.** Despite the appeal of the model, well-
documented cases remain few. Rhagoletis is the strongest case. Most speciation in
animals appears to require some period of geographic isolation.

**Reproductive isolation is not binary.** It ranges from 0 to 1 and can be
decomposed into contributions from each pre- and post-zygotic barrier. Total RI =
1 - (product of all (1 - partial isolation) values). You can have two populations
that are 50% reproductively isolated — they are not clearly "species" or "not species."

**Polyploidy is the exception that proves the rule.** In plants, polyploidization
(genome duplication) can create reproductive isolation instantly: a tetraploid cannot
mate with its diploid parent (triploid offspring are sterile). This is the one
mechanism that truly bypasses the continuum of gradual divergence. It explains why
~70% of flowering plant species have ancient polyploid ancestry.
