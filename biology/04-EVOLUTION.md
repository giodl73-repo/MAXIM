# 04 — Evolution

## Natural Selection, Population Genetics, Speciation, Phylogenetics, Evo-Devo

---

## Big Picture: Evolution's Four Forces

```
EVOLUTION: change in allele frequencies in a population over generations

FOUR EVOLUTIONARY FORCES:
  ┌─────────────────────────────────────────────────────────────┐
  │  1. Natural Selection: differential reproduction based on   │
  │     heritable variation in fitness                          │
  │     → Directional, Stabilizing, Disruptive                  │
  │                                                             │
  │  2. Genetic Drift: random changes in allele frequency       │
  │     → dominates in small populations                        │
  │     → founder effect, bottleneck effect                     │
  │                                                             │
  │  3. Mutation: source of new variation                       │
  │     → ~70 new mutations per human genome per generation     │
  │     → most neutral or deleterious; rare beneficial          │
  │                                                             │
  │  4. Gene Flow: migration of alleles between populations     │
  │     → homogenizes populations; can introduce new alleles    │
  └─────────────────────────────────────────────────────────────┘

MODERN SYNTHESIS (1930s-1940s):
  Darwinian selection + Mendelian genetics + population genetics
  Key figures: Fisher, Haldane, Wright (theoretical); Dobzhansky, Mayr, Simpson (empirical)
  Result: mathematical framework unifying natural history with genetics

LEVELS OF ANALYSIS (Tinbergen's 4 Questions):
  Proximate (mechanism):  What genes/proteins/physiology produces this trait?
  Development:            How does the trait develop during ontogeny?
  Function (adaptation):  What fitness benefit does this provide?
  Evolutionary history:   How did this trait evolve phylogenetically?
```

---

## Engineering Bridges

```
EVOLUTION ←→ CS AND SYSTEMS THEORY

Natural selection = A/B testing without a product manager
  Variation: random mutations generate feature variants
  Heritability: successful variants propagate to offspring (reproduction)
  Selection: differential survival/reproduction = user retention metric
  No goal function, no gradient, no foresight — only differential survival
  Key difference from ML: the "loss function" (fitness) changes as the environment changes

Genetic drift = stochastic noise in small populations
  Small N → allele frequency wanders by sampling variance p(1-p)/2N per generation
  Like gradient descent with very high learning rate + tiny batch size
  All alleles eventually fix or go extinct (absorbing boundaries at 0 and 1)
  In small populations, drift dominates selection when s << 1/2N_e

Hardy-Weinberg = the null model (the "control group")
  Assumptions: random mating, no selection, no drift, no mutation, no migration
  → p² + 2pq + q² = 1 in one generation from any starting allele frequencies
  Use: if a population deviates from HWE → something is happening (selection, inbreeding,
    genotyping error, population substructure)
  → Like testing a distributed system against a null hypothesis of "no interesting behavior"

Phylogenetic trees = version control history of life
  Branch = lineage (like a git branch)
  Node = common ancestor (like a merge point or a branch origin)
  Branch length = evolutionary divergence (like commit count or time since fork)
  Clade (monophyletic group) = all descendants of a common ancestor
    → like all code downstream of a given commit
  Horizontal gene transfer = cherry-pick across branches (common in prokaryotes)
    → makes the "tree of life" a DAG, not a tree, for bacteria

dN/dS (Ka/Ks) = selection signal in sequence data
  dS = synonymous substitution rate (neutral proxy; like comment changes)
  dN = nonsynonymous rate (amino acid changes; like logic changes)
  ω = dN/dS:
    ω < 1: purifying selection (functional constraint; most protein-coding genes)
    ω = 1: neutral (no constraint)
    ω > 1: positive selection (adaptive change; immune genes, rapidly evolving loci)
  → Detects which parts of a genome are under selection — without knowing what they do

Evo-devo insight: morphological change ≈ regulatory rewiring, not new proteins
  Hox genes: same gene family (Hox) in fly and vertebrate; conserved ~600 Myr
  Change body plan by altering *when/where* Hox genes are expressed
  → Like changing system behavior by modifying config/feature-flags, not rewriting code
  → Cis-regulatory evolution (enhancer changes) = configuration layer innovation
```

## Natural Selection

```
DARWINIAN REQUIREMENTS (all three must hold):
  1. Variation: individuals differ in a trait
  2. Heritability: some variation is heritable (parent → offspring)
  3. Fitness consequences: variation affects survival/reproduction

  If all three hold → natural selection will occur (logically guaranteed)

MODES OF SELECTION:
  Directional: favors one extreme of phenotypic distribution
    → shifts population mean; reduces variance at extreme
    Example: antibiotic resistance, beak size during drought

  Stabilizing: favors intermediate phenotypes; both extremes selected against
    → reduces variance; maintains mean
    Example: human birth weight (~3.4 kg optimal), clutch size in birds

  Disruptive: favors both extremes over intermediate
    → increases variance; can lead to bimodal distribution → speciation?
    Example: seed size in Darwin's finches, disassortative mating

  Sexual selection: trait evolves because it improves mating success
    (can conflict with survival selection — peacock tail, frog calls)
    Intrasexual: competition between individuals of same sex (antlers)
    Intersexual: mate choice (female choice for honest signal)

FITNESS:
  Absolute fitness W: expected reproductive output of a genotype
  Relative fitness w: normalized to most fit genotype (w = W/W_max)
  Selection coefficient s: 1 − w (fitness deficit of less fit genotype)
  Heterozygote advantage (overdominance): w_Aa > w_AA and w_aa
    Classic: sickle cell/malaria — HbS/HbA heterozygote survives better

SELECTION ON QUANTITATIVE TRAITS:
  Response to selection (breeder's equation): R = h² · S
  R: response (change in population mean)
  h² (narrow-sense heritability): V_A / V_P  (additive genetic / phenotypic variance)
  S: selection differential (difference between selected parents and population mean)
  → This is the foundation of animal/plant breeding AND evolutionary quantitative genetics
```

---

## Population Genetics

```
HARDY-WEINBERG EQUILIBRIUM (HWE):
  In a diploid population with random mating, no selection, no mutation,
  no genetic drift, no gene flow:
  p² + 2pq + q² = 1   (genotype frequencies stable)
  p = frequency of allele A, q = frequency of allele a (p + q = 1)

  Genotype frequencies:
    AA: p²     Aa: 2pq     aa: q²

  Useful as null model: departures from HWE → selection, inbreeding, or genotyping error
  Common use: estimate carrier frequency from disease prevalence
    If aa phenotype = 1/10,000, then q = 1/100, carrier freq 2pq ≈ 1/50

SELECTION EQUATIONS (single locus):
  p' = p · w̄_A / w̄     (frequency of A after selection)
  w̄ = p²W_AA + 2pqW_Aa + q²W_aa  (mean fitness)

  Change in allele frequency: Δp = pq(w_A − w_a) / w̄
  When w_A > w_a: favorable allele increases each generation
  Rate depends on current frequency: slow when rare (q << 1), fast at intermediate freq

  Time to fix a favorable mutation (rough): T ≈ 2 ln(2N)/s  generations
  Example: s = 0.01 in N = 10,000 → ~2700 generations to go from 1/2N to near fixation

GENETIC DRIFT:
  Random sampling in finite populations → allele frequencies wander
  Expected change: 0 (unbiased)
  Variance of change: p(1-p)/2N per generation
  All alleles eventually fix or lost (at rate 1/2N per generation for neutral allele)

  Effective population size N_e:
    Often << census size due to variance in reproductive success, sex ratio, bottlenecks
    Human N_e ≈ 10,000-15,000 (despite 8 billion today — reflects pre-agriculture bottleneck)
    Very low diversity at most loci → most human polymorphism is neutral/weakly deleterious

  Bottleneck: N_e crashes briefly → alleles lost, diversity reduced
    → founder effect: colonizing population carries only subset of source population alleles
    Example: Ashkenazi Jewish disease alleles elevated by founder effects

COALESCENT THEORY:
  Traces ancestry of alleles backward in time until common ancestor (MRCA)
  Coalescence time: E[T_MRCA] = 4N_e generations for diploid
  Gene trees vs species trees: can differ due to incomplete lineage sorting (ILS)
  Application: molecular clock, Ne estimation, demographic inference from genomic data

NEUTRAL THEORY (Kimura, 1968):
  Most molecular variation is neutral or nearly neutral (not subject to selection)
  Fixation probability of neutral mutation: 1/2N (same as any allele)
  Substitution rate at neutral sites = mutation rate μ (independent of N)
  K = μ (per site per generation; remarkable result)
  Applications: calibrate molecular clocks, define null expectation for selection tests

SELECTION TESTS:
  dN/dS ratio (ω):
    dN: nonsynonymous substitution rate  (changes amino acid)
    dS: synonymous substitution rate     (silent — proxy for neutral rate)
    ω < 1: purifying selection (protein function conserved)
    ω = 1: neutral evolution
    ω > 1: positive/diversifying selection
  McDonald-Kreitman test: within-species vs between-species polymorphism
    Excess of nonsynonymous fixed differences → positive selection
  Tajima's D: use of allele frequency spectrum to detect recent selection
```

---

## Speciation

```
BIOLOGICAL SPECIES CONCEPT (Mayr, 1942):
  A species = group of actually or potentially interbreeding natural populations
  reproductively isolated from other such groups
  Problems: asexual species, hybridization, allopatric populations (can't test)
  Alternative concepts: phylogenetic, ecological, genotypic cluster

MODES OF SPECIATION:
  Allopatric (geographic isolation):
    Vicariance: physical barrier divides range → independent evolution → reproductive isolation
    Example: isthmus of Panama (3 Mya) → Atlantic and Pacific marine species diverged
    Most common mode for most taxa

  Peripatric (founder speciation):
    Small peripheral population becomes isolated → drift + selection → new species
    Mayr's model; explains why species on island periphery differ most

  Sympatric (no geographic separation):
    Divergence while ranges overlap; requires very strong disruptive selection or polyploidy
    Controversial for animals; clear in plants (polyploidy)

  Parapatric: adjacent populations with some gene flow but diverging

REPRODUCTIVE ISOLATION MECHANISMS:
  Prezygotic (prevent mating/fertilization):
    Habitat: use different microhabitats
    Temporal: breed at different times
    Behavioral: mate recognition signals differ (song, color, courtship)
    Mechanical: copulatory incompatibility
    Gametic: sperm-egg incompatibility

  Postzygotic (reduce hybrid fitness):
    Hybrid inviability: zygote dies in development
    Hybrid sterility: hybrid lives but is sterile (mule = horse × donkey)
    Hybrid breakdown: F₂ or backcross hybrids have reduced fitness

  Dobzhansky-Muller incompatibilities (DMI):
    Two populations independently fix different alleles that are incompatible
    aa/BB + AA/bb → F1 Aa/Bb (fine) → F2: some aaBB recombinants are inviable
    Explains why hybrid incompatibilities evolve even without selection against hybrids

POLYPLOIDY (important in plants):
  Autopolyploidy: chromosome duplication within species
  Allopolyploidy: hybridization + chromosome doubling → instant reproductive isolation
  ~70% of flowering plant species are polyploids or descended from polyploids
  Wheat: hexaploid (6n = 42); cotton: tetraploid
  Rare in animals but occurs (some fish, frogs, insects)

SPECIATION RATES:
  Molecular clock: rates of evolution calibrated by fossil record
  Rapid radiation: Cichlid fish (400+ species, African Great Lakes, 15,000 years)
    → ecological opportunity + sexual selection → explosive speciation
  Slow speciation: lineages with poor dispersal, stable ecology
  Average species duration: ~1-10 Myr in fossil record before extinction or cladogenesis
```

---

## Phylogenetics

```
PHYLOGENETIC TREES:
  Nodes: common ancestors
  Branches: lineages; branch length often proportional to evolutionary change
  Leaves: taxa (operational taxonomic units)
  Clade (monophyletic group): ancestor + all descendants
  Paraphyletic: ancestor + some descendants (e.g., "reptiles" excluding birds)
  Polyphyletic: taxa from different ancestors (e.g., "warm-blooded animals" = birds + mammals)

HOMOLOGY VS ANALOGY:
  Homology: shared trait from common ancestor (bat wing + human arm = same bones)
  Analogy (convergence): similar function, independent evolution (bat wing + insect wing)
  Molecular phylogenetics relies on homologous sequences

TREE BUILDING METHODS:
  Distance (UPGMA, Neighbor-Joining):
    Pairwise distances → cluster; fast but assumes clock-like evolution
  Maximum Parsimony:
    Find tree requiring fewest evolutionary changes; NP-hard for many taxa
  Maximum Likelihood (ML):
    Find tree maximizing P(data | tree, model); computationally intensive; RAxML, IQ-TREE
  Bayesian:
    Posterior P(tree | data) via MCMC; MrBayes, BEAST; accounts for uncertainty

SUBSTITUTION MODELS:
  JC69 (Jukes-Cantor): all substitutions equal
  HKY85: transitions ≠ transversions; different base frequencies
  GTR+Γ+I: most parameter-rich; accounts for rate variation across sites
  Codon models: for protein-coding genes; detect dN/dS

MOLECULAR CLOCK:
  Constant substitution rate → divergence time from sequence divergence
  Strict clock: one rate for whole tree (often violated)
  Relaxed clock: rate varies among branches (BEAST)
  Calibration: fossil record dates → absolute time scale

KEY PHYLOGENETIC RESULTS:
  Three domains: Bacteria, Archaea, Eukarya (Woese, 1977-1990)
  Eukaryotes closer to Archaea than Bacteria (TACK, Asgard superphyla)
  Endosymbiotic origin: mitochondria from α-proteobacteria; chloroplasts from cyanobacteria
  Fungi more closely related to animals than to plants (opisthokont clade)
  Cetaceans (whales) nested within artiodactyls (closest relative: hippopotamus)
  Birds are dinosaurs (therapod clade includes all living birds)
```

---

## Evo-Devo (Evolutionary Developmental Biology)

```
CORE INSIGHT:
  Differences between species often arise from changes in gene expression patterns
  during development, not necessarily from new genes
  Many developmental toolkit genes are highly conserved across vast evolutionary distance

HOX GENES:
  Master regulators of body axis patterning (segment identity)
  Discovered in Drosophila (Lewis, McGinnis, Scott — Nobel 1995)
  Conservation: fly Hox genes can often substitute for mouse Hox genes
  Collinearity rule: order of genes on chromosome = order of expression along body axis
  Humans: 4 Hox clusters (HOXA-D), 39 genes total

PATTERNING TOOLKIT (examples):
  Pax6: eye development in both fly (compound) and vertebrate (camera) — different structures,
    same master gene → convergent evolution of eye types but same genetic switch
  Hedgehog/Sonic hedgehog: limb development, neural tube patterning (fly + vertebrate)
  Wnt: body axis polarity, stem cell maintenance (very ancient, present in cnidarians)
  Notch-Delta: cell fate specification, lateral inhibition (fly + vertebrate)
  Nanos/Bicoid: anterior-posterior axis in Drosophila (Nüsslein-Volhard + Wieschaus, Nobel 1995)

CIS-REGULATORY EVOLUTION:
  Regulatory changes → altered expression patterns → morphological change
  Without changing protein coding sequence
  Examples:
    Sticklebacks: loss of pelvic spine through Pitx1 enhancer deletion (multiple times)
    Human accelerated regions (HARs): sequences conserved in mammals but fast-evolving in humans
      HAR1: expressed in developing cortex; may contribute to human brain size
    Pharyngeal jaw in cichlids: same genes, altered expression patterns → novel jaw structures

DEVELOPMENTAL CONSTRAINTS AND PHYLOTYPIC STAGE:
  Von Baer (1828): vertebrate embryos more similar at early/mid development than at start or end
  Phylotypic stage: "hourglass model" — most constrained in pharyngula stage
  Developmental constraints: some morphological change is not achievable (would break development)
  Modularity: development organized in semi-independent modules → can change one without disrupting others

MAJOR EVOLUTIONARY TRANSITIONS:
  Eukaryotic cell (endosymbiosis ~2 Gya)
  Multicellularity (multiple independent origins; plants, animals, fungi; ~600-800 Mya)
  Sexual reproduction (origins unclear, Mya in algae)
  Land colonization (plants ~500 Mya, animals ~375 Mya)
  Vertebrate jaw (Silurian ~430 Mya; from pharyngeal arch remodeling)
  Amniotic egg (Carboniferous ~320 Mya — freed from water for reproduction)
  Flowering plants (Cretaceous ~130 Mya; co-evolution with pollinators)
  Human evolution: bipedalism (~7 Mya), stone tools (~3.3 Mya), fire use (~1 Mya), language
```

---

## Molecular Evolution

```
NEUTRAL EVOLUTION DOMINATES:
  Most substitutions between species at neutral sites (synonymous, intergenic)
  Protein sequence diverges at rate proportional to fraction of neutral sites
  Functionally constrained proteins evolve slowly (histones, ribosomal proteins)
  Less constrained proteins evolve faster (fibrinopeptides, pseudogenes)

MOLECULAR PHYLOGENY OF LIFE:
  rRNA (small subunit) = primary phylogenetic marker (Woese)
    Universally present, functionally conserved, evolves slowly
    16S (prokaryote), 18S (eukaryote)
  Protein phylogenies: many markers → reduce phylogenetic noise
  Core genome phylogeny: genes present in all species (most reliable backbone)

HORIZONTAL GENE TRANSFER (HGT):
  Genes can move between non-related organisms (common in prokaryotes)
  Antibiotic resistance genes: spread by conjugation/transduction/transformation
  Archaea: HGT from bacteria is common
  Eukaryotes: HGT much rarer but occurs (e.g., plant genes in bdelloid rotifers)
  HGT complicates "tree of life" → "web of life" for prokaryotes

GENOME SIZE EVOLUTION:
  C-value paradox: genome size not correlated with organismal complexity
  Salamanders: >10× human genome; onion: 5× human
  Most variation due to transposable element (TE) accumulation/removal
  Humans: ~50% TEs; plants: up to 85% TEs
  Genome reduction in endosymbionts/parasites (Mycoplasma: 580 kb; free-living bacteria: 2-10 Mb)
```

---

## Decision Cheat Sheet

| Question | Concept | Key Formula/Rule |
|----------|---------|-----------------|
| Is this locus under selection? | dN/dS ratio (ω) | ω > 1: positive, < 1: purifying, = 1: neutral |
| Is population in HWE? | Hardy-Weinberg test | p² + 2pq + q² = 1; χ² test |
| How fast will allele spread? | Selection coefficient | T ≈ 2 ln(2N)/s generations to fixation |
| How important is drift vs selection? | N_e · s product | s >> 1/2N_e: selection wins; s << 1/2N_e: drift |
| How are species related? | Phylogenetic tree | Build with ML or Bayesian; model selection |
| What's the molecular clock rate? | Neutral theory | K = μ at neutral sites; calibrate with fossils |
| Why do hybrids fail? | DMI incompatibilities | Incompatible alleles at two loci |
| How does body plan change? | Evo-devo: Hox genes | Regulatory changes, cis-regulatory evolution |
| How do I estimate population history? | Coalescent / PSMC | E[T_MRCA] = 4N_e for diploid |
| Is this a real clade? | Monophyly + bootstrap | Clade = ancestor + ALL descendants |

---

## Common Confusion Points

**Natural selection is not goal-directed**: Evolution does not "try" to produce outcomes. Selection is a filter — heritable variation in fitness → differential reproduction → allele frequency change. No foresight, no purpose.

**Fitness is relative and context-dependent**: An allele that is beneficial in one environment can be neutral or deleterious in another. Sickle cell trait: beneficial in malaria regions, harmful without malaria. Fitness has no absolute meaning.

**Evolution doesn't always mean adaptation**: Most molecular evolution is neutral (genetic drift). Most new mutations are slightly deleterious. Adaptation (improvement) is real but not the dominant mechanism at the sequence level.

**Genetic drift is strongest in small populations**: For humans, N_e ≈ 10,000. Modern humans have low diversity relative to other great apes — consistent with past bottleneck. Population size changes dramatically affect evolutionary dynamics.

**Species concepts are imperfect**: The biological species concept (reproductive isolation) is practical for animals but fails for bacteria (HGT), plants (polyploidy + hybridization), and allopatric populations. Use context-appropriate concept.

**Pax6 / convergent evolution**: Pax6 is required for eye development in both flies and mice. This doesn't mean fly and mouse eyes evolved from a common eye ancestor (they didn't — they're convergent). It means the same master regulatory gene was co-opted for an analogous function.

**Heritability is a population statistic, not a gene characteristic**: h² of 0.8 for height doesn't mean "80% of your height is genes." It means 80% of the variation in height in that population is attributable to genetic differences. Change the environment (add famine), and h² changes.
