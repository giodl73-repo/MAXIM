# Phylogenetics and Molecular Clocks

## The Big Picture

Phylogenetics reconstructs the evolutionary history of organisms by inferring the
tree of relationships (phylogeny) from molecular or morphological data.

```
┌──────────────────────────────────────────────────────────────────┐
│                   PHYLOGENETICS WORKFLOW                          │
│                                                                    │
│  DATA                ALIGNMENT            TREE INFERENCE         │
│  ────                ─────────            ──────────────         │
│  DNA sequences  →  Multiple sequence  →  Parsimony              │
│  Protein seqs      alignment (MSA)       Maximum likelihood     │
│  Morphology        ClustalW/MUSCLE       Bayesian MCMC          │
│  SNP arrays        MAFFT                                         │
│                                                                    │
│  TREE INTERPRETATION        MOLECULAR CLOCK                      │
│  ──────────────────         ────────────────                    │
│  Topology: who is           Strict: rate constant               │
│    related to whom          Relaxed: rate varies                 │
│  Branch lengths:            Calibrated against fossils          │
│    amount of change         Output: divergence times            │
│  Bootstrap/PP:                                                    │
│    statistical support                                           │
└──────────────────────────────────────────────────────────────────┘
```

---

## Reading a Phylogenetic Tree

```
  Internal nodes = common ancestors
  Tips (leaves) = sampled taxa (species, individuals, sequences)
  Branch lengths = amount of evolution (substitutions per site, or time)
  Root = deepest common ancestor

  Example rooted tree:

         ┌──── Human
       ┌─┤
       │ └──── Chimpanzee     } Clade A
  ─────┤
       │   ┌── Gorilla
       └───┤             } Clade B
           └── Orangutan

  Clade: monophyletic group = ancestor + ALL descendants
         (Human + Chimpanzee + Gorilla + Orangutan = clade)
  (Human + Chimpanzee) = clade A
  (Human + Gorilla) = NOT a clade (polyphyletic w.r.t. topology above)

  KEY RULE: the *branching order* is what matters, not left-right placement.
  Rotating branches around a node does NOT change relationships.
```

---

## Methods of Phylogenetic Inference

### 1. Maximum Parsimony

Find the tree that requires the fewest character state changes to explain the data.

```
  Parsimony score = total number of changes on the tree
  Search: exhaustive (small datasets), heuristic branch-swapping (large)

  Pros: conceptually simple, no model required
  Cons: inconsistent under some models (Felsenstein zone):
        - Long branch attraction: two long branches incorrectly grouped
          due to convergent accumulation of same nucleotide by chance
        - Fails when substitution model deviates strongly from parsimony assumptions
```

### 2. Distance Methods (UPGMA, Neighbor-Joining)

Convert sequences to pairwise distance matrix, then build tree by clustering.

```
  UPGMA: assumes constant rate (molecular clock) — often violated
  Neighbor-Joining (NJ): star decomposition, fast, no clock assumption
                          Good for exploratory analysis, large datasets

  Pros: fast (NJ scales well)
  Cons: throws away information by reducing to pairwise distances
        NJ can be inconsistent with some models
```

### 3. Maximum Likelihood (ML)

Find the tree T and parameters θ that maximize P(data | T, θ).

```
  L(T, θ) = P(D | T, θ) = ∏ P(site_i | T, θ)   [sites independent]

  Model θ: substitution model (GTR+Γ), branch lengths

  Tools: RAxML, IQ-TREE (fast ML, auto model selection)
         IQ-TREE2 is current standard for ML phylogenetics

  Bootstrap: resample sites, rerun ML, count fraction of replicates
             recovering each node. Bootstrap support ≥ 70 = reasonable,
             ≥ 95 = strong (standard thresholds)

  Pros: statistically principled, consistent under correct model
  Cons: computationally intensive; sensitive to model misspecification
```

### 4. Bayesian MCMC

Compute posterior distribution P(T, θ | data) using Bayes' theorem and MCMC.

```
  P(T, θ | D) ∝ P(D | T, θ) × P(T, θ)
                ↑                ↑
                likelihood       prior

  MCMC samples trees and parameters proportional to posterior probability
  Output: distribution of trees, parameter values, credible intervals

  Tools: MrBayes (standard), BEAST (molecular clock + phylogeography)

  Key output: Posterior probability (PP) of each node
  PP = fraction of MCMC samples containing that node
  PP ≥ 0.95 = high support (more conservative threshold than bootstrap)

  Pros: full uncertainty quantification; can integrate over nuisance parameters;
        natural framework for hypothesis testing; incorporates priors
  Cons: computationally expensive; sensitive to priors; convergence assessment
        (need independent MCMC chains to agree)
```

---

## Phylogenetic Inference — Statistical Inference Bridge

Phylogenetic inference is a structured estimation problem. The statistical
machinery is identical to probabilistic graphical models and Bayesian inference:

```
MAXIMUM LIKELIHOOD PHYLOGENETICS:

  Goal: find tree T* = argmax P(sequences | T, θ)
        where θ = substitution model parameters (rate matrix Q, branch lengths)

  Likelihood computation: Felsenstein's pruning algorithm (1981)
    = dynamic programming on the tree (bottom-up message passing)
    Same structure as: belief propagation on a tree-structured graphical model
    Time complexity: O(n · L · k²) where n = taxa, L = sites, k = states (4)
    The tree's topology is the latent structure (discrete, combinatorial)

  Tree topology space: (2n-3)!! unrooted binary trees for n taxa
    n=10:  2,027,025 trees
    n=50:  3 × 10⁷⁴ trees (vastly larger than state spaces of most search problems)
  Search: heuristic (NNI, SPR, TBR branch swapping) — same as local search in
    combinatorial optimization. Exact solution (exhaustive search) intractable for n > 12.

BAYESIAN PHYLOGENETICS = POSTERIOR SAMPLING ON TREE SPACE:

  P(T, θ | data) ∝ P(data | T, θ) · P(T) · P(θ)

  Identical to any Bayesian model with a discrete latent variable
  Implemented via MCMC (MrBayes, BEAST, RevBayes):
    - Proposal moves: NNI/SPR topology moves + parameter updates
    - Metropolis-Hastings acceptance criterion (same as any MCMC)
    - Convergence: run multiple chains, check Rhat / ESS (same as Stan/PyMC)

  Output: posterior probability (PP) of each clade
    PP = fraction of MCMC samples containing the clade
    PP ≥ 0.95: high support (analogous to 95% credible interval)
    More conservative than bootstrap (because PP accounts for model uncertainty)

BOOTSTRAP = FREQUENTIST RESAMPLING:
  Resample sites (columns) of alignment with replacement → 100–1000 pseudoreplicates
  → run ML on each → frequency of clade across replicates = bootstrap support
  Conceptually: same as any bootstrap uncertainty estimate in frequentist inference
  BS ≥ 70% ≈ PP ≥ 0.95 (rough correspondence)

MODEL SELECTION:
  AIC = 2k − 2·ln(L̂): penalizes parameters
  BIC = k·ln(n) − 2·ln(L̂): stronger penalty
  Same as model selection in any regression context
  IQ-TREE's ModelFinder: tests all models → AIC/BIC rank
```

## Substitution Models

DNA evolves non-uniformly. Models account for:
- Unequal base frequencies (A+T ≠ G+C in many organisms)
- Rate variation between sites (active sites change slowly, loops change fast)
- Transition/transversion bias (transitions 2-10x more frequent)

```
  MODEL HIERARCHY (increasing complexity):
  ─────────────────────────────────────────
  JC69  → all rates equal, equal frequencies
  K80   → Ti ≠ Tv, equal frequencies
  F81   → all rates equal, unequal frequencies
  HKY85 → Ti ≠ Tv, unequal frequencies (most common simple model)
  GTR   → all 6 rate parameters free, unequal frequencies
        → 9 free parameters total

  +Γ:   rate variation across sites (gamma distribution, parameter α)
        α < 1: most sites slow, some very fast
        α > 1: rates more uniform
  +I:   proportion of invariable sites (impossible to change regardless of time)

  Model selection: AIC (Akaike Information Criterion) or BIC
  IQ-TREE does model selection automatically via ModelFinder
```

---

## Gene Trees vs. Species Trees

A critical distinction that is frequently ignored:

```
  Species tree: the true evolutionary history of the species (reticulate
                for populations, but tree-like for species phylogeny)

  Gene tree: the genealogical history of a particular locus/gene

  These CAN DIFFER due to:
  ─────────────────────────
  1. Incomplete lineage sorting (ILS / deep coalescence)
  2. Horizontal gene transfer (HGT)
  3. Gene duplication + loss (paralog confused with ortholog)
  4. Hybridization / introgression

  ILS example:
  ────────────
  Speciation events A-B split and A-C split occurred in rapid succession.
  For some genes, the ancestral polymorphism was not resolved before the
  second split. Result: gene tree shows (A, C) as sister even when species
  tree has (A, B) as sister.

  This is not error — it is expected population-genetic behavior.
  In the human-chimp-gorilla trichotomy:
  - Many gene trees support (human, gorilla) as sister
  - Species tree: (human, chimp) sister
  - ILS explains this; the short branch between the splits was short in time
    relative to N_e
```

### ASTRAL and Coalescent Species Tree Methods

To infer species trees from sets of gene trees:

```
  ASTRAL: finds species tree that minimizes gene tree discordance
          (maximizes the number of quartet topologies shared with gene trees)
          Explicitly accounts for ILS under multi-species coalescent

  *BEAST: full Bayesian co-estimation of gene trees and species tree
          embedded in coalescent model
          Computationally expensive but statistically rigorous
```

---

## Molecular Clock — Implementation

### Calibration
The molecular clock must be calibrated against an independent time estimate.
Sources of calibration:
1. **Fossil record**: minimum age for a clade (earliest fossil → divergence occurred
   before that date, not at that date)
2. **Biogeography**: separation of continents (vicariance events) with known dates
   (e.g., separation of Atlantic and Pacific by Isthmus of Panama, 3.5 mya)
3. **Virus isolation dates**: for viral phylogenomics, known collection dates anchor
   the clock directly

### BEAST Workflow

```
  Input: Aligned sequences + calibration prior(s) + substitution model + clock model

  Outputs:
  - Dated phylogeny with credible intervals on divergence times
  - Rate variation across branches (relaxed clock)
  - Effective population size through time (Bayesian skyline plot)

  Key parameters:
  - Tree prior: Yule (pure birth), birth-death, coalescent
  - Clock prior: strict, uncorrelated relaxed lognormal (UCLN), random local clock
  - Calibration: log-normal prior on node age (mean = fossil date, σ = uncertainty)
```

---

## Phylogenetic Networks

The "tree of life" is not a tree for bacteria and archaea — it is a network
due to pervasive horizontal gene transfer (HGT). Network methods are now
essential for prokaryotic phylogenomics.

```
WHY NETWORKS, NOT TREES:

  Tree assumption: every nucleotide position shares the same evolutionary history
  Network reality: different positions have different histories (due to HGT,
                   hybridization, recombination, ILS)

  Signal in the data: "tree-like" signal from vertical descent
                    + "non-tree" signal from reticulate events
  Split decomposition: identifies both types of signal

PHYLOGENETIC NETWORK TYPES:

  1. IMPLICIT NETWORKS (data display):
     Split graph / NeighborNet:
       Identifies all splits (bipartitions) supported by the data
       Conflicting splits displayed as parallelograms
       → immediately visualizes "tree-like" vs. network-like signal
       Tool: SplitsTree4

  2. EXPLICIT NETWORKS (model reticulation events):
     HGT networks: model directed gene transfer edges (donor → recipient)
     Hybridization networks: model hybrid speciation (two parents → hybrid child)
     Tools: PhyloNet, HGT-Detection (via parsimony of gene tree incongruence)

  3. GENE TREE RECONCILIATION:
     Given species tree S and gene trees G₁...Gₙ:
     Count: duplications + losses + HGT events to explain G within S
     Parsimony: minimize total events (NP-hard in general)
     → same combinatorial optimization as string edit distance, but on trees

BACTERIA AND ARCHAEA:
  ~10–50% of any given bacterial genome has been acquired via HGT
  Core genome (shared by all strains): mostly vertical, somewhat tree-like
  Pan-genome (union of all genes in a species): includes accessory genome
    that flows horizontally between lineages
  "Tree of life" for bacteria: core genome phylogeny (ribosomal genes)
    provides a vertical backbone, but most functional diversity = horizontal

EUKARYOTES WITH NETWORK HISTORIES:
  Plants: allopolyploidy → hybrid species have two parents
    Bread wheat: hexaploid (AABBDD) from three ancestor genomes
    → its phylogeny is a network, not a tree
  Animals: rarer, but documented
    Darwin's finches: some interspecies hybridization
    Polar bear + brown bear: ancient admixture
    Neanderthal + H. sapiens: ~2% Neanderthal DNA in non-African humans
```

## Ancestral State Reconstruction

Given a tree and character states at the tips, infer states at internal nodes
(ancestors):

```
  Methods:
  ─────────
  Parsimony: minimize total changes (fast, biased under unequal rates)
  Maximum likelihood: P(data | model, tree) for each ancestral state
  Bayesian: posterior distribution over ancestral states

  Applications:
  - Inferring ancestral protein sequences (resurrect ancient proteins — "paleogenomics")
  - Mapping habitat transitions on tree (did flight evolve once or multiple times?)
  - Tracing migration routes (virus epidemiology)
  - Ancestral gene regulation (where did enhancers evolve?)
```

---

## Phylogenomics

The use of hundreds to thousands of genes (or whole genomes) for phylogenetic
inference:

```
  ADVANTAGES:
  ───────────
  - More data → better resolution of short branches
  - Can identify ILS-prone regions
  - Can detect horizontal transfer, admixture
  - Can build "supermatrices" (concatenation) or "coalescent-based" trees

  CHALLENGES:
  ───────────
  - Systematic error: model misspecification amplified across thousands of genes
  - Long branch attraction: still a problem with poor models
  - Gene tree heterogeneity: concatenation assumes all genes share one history
  - Computational: thousands of genes × complex models = expensive

  Modern approach: ASTRAL or SVDquartets for coalescent tree from many gene trees
                   + detect outlier genes (possible HGT, duplication errors)
```

---

## Decision Cheat Sheet

| Task | Method | Tool |
|------|--------|------|
| Quick exploratory tree | Neighbor-Joining | MEGA, FastTree |
| Best ML tree from DNA | ML with model selection | IQ-TREE2 |
| Dated phylogeny | Bayesian + molecular clock | BEAST2 |
| Species tree from gene trees | Coalescent species tree | ASTRAL |
| Ancient divergences, fossil calibration | BEAST relaxed clock | BEAST2 |
| Population-level genealogy | Coalescent | ARGweaver, RELATE |
| Ancestral state reconstruction | Bayesian ASR | BayesTraits, IQ-TREE |

---

## Common Confusion Points

**Rotating branches does NOT change tree topology.** Any node can be freely rotated.
A phylogenetic tree is an unordered tree — the left-right arrangement of taxa is
arbitrary. Two trees that look different can be identical topologically.

**Bootstrap support is not a probability.** It measures reproducibility (would the
same node be recovered in resampled datasets?), not the probability that the node
is correct. Bayesian posterior probabilities are closer to a probability of correctness
given the model and prior.

**Outgroup rooting can be misleading.** The outgroup needs to be related closely
enough to the ingroup to align well but distantly enough to root the tree. A distant
outgroup (long branch) can cause long-branch attraction artifacts.

**Molecular clocks are not constant.** Rate variation across lineages is the rule.
A strict clock for mammalian mtDNA is approximately valid; a strict clock across
insects, plants, and vertebrates is not. Always test clock-like behavior before
assuming it.

**ILS is not a nuisance — it is signal.** The distribution of gene tree topologies
in an ILS scenario contains information about ancestral population sizes and
speciation times. This is the foundation of coalescent-based species tree methods.
