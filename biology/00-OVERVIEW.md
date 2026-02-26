# Biology — Overview
<!-- @editor[diagram/P2]: Landscape diagram lists items linearly — rework as layered system view showing relationships between modules -->
<!-- @editor[bridge/P1]: Missing universal CS bridge upfront — Biology as Information Science should anchor the opening, not be buried at bottom -->

---

## Big Picture

```
BIOLOGY: the study of living systems — their structure, function, evolution,
         and molecular mechanisms

HIERARCHY OF ORGANIZATION:
  Atoms → Molecules → Macromolecules → Organelles → Cells
  → Tissues → Organs → Organisms → Populations → Ecosystems

CENTRAL DOGMA (Crick, 1958):
  DNA ──────────→ RNA ──────────→ Protein
    (transcription)    (translation)

  Information flows: DNA → RNA → Protein
  Reverse transcriptase: RNA → DNA (retroviruses — exception, not rule)
  No reverse translation: protein sequence never goes back to nucleic acid

UNIFYING THEORIES:
  1. Cell theory: all life is composed of cells (Schleiden, Schwann, Virchow 1838-1855)
  2. Evolution by natural selection (Darwin, Wallace 1858/1859)
  3. Molecular basis of heredity (Watson & Crick, Franklin 1953)
  4. Biochemical universality: same genetic code in all life (Nirenberg 1961)
```

---

## Why This Matters for an Engineer/AI Person

1. **Biotechnology revolution**: CRISPR, mRNA vaccines, protein folding (AlphaFold2), synthetic biology — all require understanding molecular biology at depth.

2. **AI for biology**: AlphaFold2 (2021, DeepMind) solved the protein folding problem. AlphaProteo designs novel proteins. Genomics uses ML to decode 3 billion base pairs. Biological data is now the largest scientific dataset.

3. **Biological computation is the benchmark.** The cell is a molecular computer running massively parallel biochemical programs on a 3.8 billion year evolutionary codebase. Understanding it sets the bar for what synthetic systems might achieve.

4. **Gene therapy and precision medicine.** CAR-T cells, mRNA therapeutics, gene editing — understanding the molecular layer is necessary for engineering biologically informed systems.

5. **Evolutionary algorithms and evolutionary game theory** both draw directly from population genetics and Darwinian selection.

---

## Field Map

```
BIOLOGY
│
├── Molecular Biology
│     DNA/RNA structure, central dogma, transcription/translation
│     Gene regulation, epigenetics, CRISPR
│     → Module 01-MOLECULAR-MACHINERY.md
│
├── Cell Biology
│     Cell organelles, membrane transport, cell signaling
│     Cell cycle, division, apoptosis
│     → Module 02-CELL-BIOLOGY.md
│
├── Genetics & Genomics
│     Mendelian genetics, chromosome theory, molecular genetics
│     Population genetics, genomics, epigenetics
│     → Module 03-GENETICS.md
│
├── Evolution
│     Natural selection, genetic drift, molecular evolution
│     Speciation, phylogenetics, evo-devo
│     → Module 04-EVOLUTION.md
│
├── Ecology
│     Population dynamics, species interactions, community ecology
│     Biogeochemical cycles, conservation biology
│     → Module 05-ECOLOGY.md
│
└── Physiology
      Organ systems, homeostasis, neural signaling
      Immune system, endocrinology, integration
      → Module 06-PHYSIOLOGY.md
```

---

## Module Map

| File | Topic | Status |
|------|-------|--------|
| `01-MOLECULAR-MACHINERY.md` | DNA, RNA, proteins — central dogma in molecular detail | ✅ Complete |
| `02-CELL-BIOLOGY.md` | Membrane, organelles, cell signaling, cell cycle | ✅ Complete |
| `03-GENETICS.md` | Mendelian → molecular genetics, genomics, epigenetics, CRISPR | ✅ Complete |
| `04-EVOLUTION.md` | Natural selection, population genetics, speciation, phylogenetics, evo-devo | ✅ Complete |
| `05-ECOLOGY.md` | Population dynamics, species interactions, community ecology | ✅ Complete |
| `06-PHYSIOLOGY.md` | Organ systems, homeostasis, neural signaling, immune, endocrine | ✅ Complete |

---

## Concept Map: Biology's Core Ideas

```
INFORMATION FLOW:
  Genome (genotype) ──→ Transcriptome ──→ Proteome ──→ Metabolome
                   transcription   translation    enzyme catalysis
          ↑
  Epigenome (histone modification, DNA methylation) ← environment

BIOLOGICAL SCALES:
  nm:    molecules (DNA 2nm, protein average ~5nm)
  μm:    organelles, bacteria (1-10 μm)
  mm:    cells (animal: ~10 μm, egg: 0.1mm, but visible range is huge)
  cm:    tissues, small organs
  m:     organisms

TIMESCALES:
  ns-μs:   molecular dynamics, protein folding fast phases
  ms-s:    enzyme catalysis, signaling cascades, action potential
  min-hr:  gene expression, cell signaling
  hr-day:  cell division (~24 hr for mammalian), circadian rhythms
  day-yr:  development, growth, lifespan
  yr-kyr:  population dynamics, ecological succession
  kyr-Myr: speciation, macroevolution
  Gyr:     origin of life, major evolutionary transitions

SELECTION LEVELS:
  Gene-level: selfish gene (Dawkins) — replicators drive evolution
  Organism-level: organism fitness = reproductive success (classic view)
  Kin selection: Hamilton's rule rb > c (altruism favored when benefit × relatedness > cost)
  Group selection: controversial; most apparent group-level effects explained by kin
```

---

## Key Numbers

```
Human genome:
  Base pairs:                ~3.2 × 10⁹ (3.2 Gbp, haploid)
  Protein-coding genes:      ~20,000 (only ~1.5% of genome!)
  Total genes (incl. RNA):   ~25,000-30,000
  Repetitive elements:       ~50% of genome (TEs, SINEs, LINEs)
  Gene regulatory elements:  ~8% (ENCODE estimate)
  Information content:       ~800 MB as compressed sequence

DNA:
  Diameter:                  2 nm
  Rise per base pair:        0.34 nm
  Persistence length:        ~50 nm (semirigid polymer — longer than this = flexible)
  Total length stretched:    ~2 m (in every single cell!)
  Nucleosome spacing:        ~200 bp = 1 nucleosome (~10 nm bead)
  Supercoiling ratio:        ~1 negative supercoil per 10 turns

Proteins:
  Average size:              400 amino acids
  Average mol. weight:       ~45 kDa
  Synthesis rate:            ~20 amino acids/second (ribosome)
  Folding time:              μs (small) to seconds (large/complex)
  Proteins in one cell:      ~3-4 billion molecules
  Human proteome:            ~20,000 proteins (but >100,000 protein isoforms)

Cell:
  Typical animal cell:       ~10-20 μm diameter, ~2000 μm³ volume
  Number of cells in body:   ~37 trillion (~30T human cells, ~38T microbiome)
  Cell division time:        24 hours (typical mammalian somatic)
  Neurons in brain:          ~86 billion (Azevedo et al. 2009)
  Synapses per neuron:       ~7,000 (hippocampal) to ~200,000 (Purkinje cells)

Evolution:
  E. coli generation time:   20 min (enables rapid evolution experiments)
  Human generation time:     25-30 years
  Primate-chimp divergence:  ~6-7 million years ago
  Homo sapiens:              ~300,000 years ago (Jebel Irhoud, Morocco)
  Mutation rate (human):     ~1.1 × 10⁻⁸ per site per generation
                             → ~70 new mutations per individual genome
```

---

## Historical Arc

```
1665: Hooke — cork cells under microscope; coins "cell"
1838: Schleiden, 1839: Schwann — cell theory (plant, animal)
1855: Virchow — omnis cellula e cellula (every cell from a cell)
1858: Darwin & Wallace — natural selection presented jointly (Linnean Society)
1859: Darwin — On the Origin of Species
1866: Mendel — laws of inheritance (pea experiments; ignored until 1900)
1869: Miescher — discovers nucleic acid (DNA) in white blood cell nuclei
1900: de Vries, Correns, Tschermak — rediscover Mendel's laws
1902: Boveri, Sutton — chromosome theory of heredity
1910: Morgan — Drosophila genetics; genes on chromosomes, sex linkage
1928: Griffith — transforming principle (some DNA-like substance transforms bacteria)
1944: Avery, MacLeod, McCarty — DNA is the transforming substance (genetic material)
1953: Watson & Crick, Franklin, Wilkins — DNA double helix structure
1958: Crick — Central Dogma, sequence hypothesis
1961: Jacob & Monod — lac operon: gene regulation
1961: Nirenberg & Matthaei — genetic code begins to be cracked
1973: Cohen, Boyer — recombinant DNA (first GMO, pSC101 + frog rDNA)
1977: Sanger — chain-termination DNA sequencing (dideoxy method)
1977: Woese — discovers Archaea (third domain of life) by rRNA
1983: Mullis — PCR (polymerase chain reaction, Nobel 1993)
1990: Human Genome Project begins ($3B, 15-year goal)
2001: Draft human genome published simultaneously by HGP + Celera (Craig Venter)
2003: Human Genome Project complete
2006: Fire, Mello — RNAi mechanism (Nobel 2006)
2006: Yamanaka — iPSCs (induced pluripotent stem cells — reprogramming, Nobel 2012)
2007-: Next-generation sequencing revolution (Illumina) — $1B → $100 → $200 per genome
2012: Doudna, Charpentier — CRISPR-Cas9 as programmable editor (Nobel 2020)
2016: Single-cell RNA-seq: every cell's transcriptome independently
2020: mRNA vaccines BNT162b2 + mRNA-1273 against SARS-CoV-2 → 95% efficacy
2021: AlphaFold2 — protein structure predicted from sequence (DeepMind, Nobel 2024)
2022: T2T Consortium — truly complete human genome (previously had gaps)
2023+: Foundation models for biology: ESM-2 (protein LLM), Evo (DNA LM), AlphaProteo
```

---

## Biology as Information Science

```
COMPUTATION ANALOGY:

  DNA sequence         ←→  source code (program)
  Epigenome            ←→  runtime configuration / feature flags
  Transcription        ←→  compilation (gene → mRNA)
  Translation          ←→  runtime execution (mRNA → protein)
  Protein folding      ←→  function binding / JIT compilation
  Signal transduction  ←→  interrupt handling / event-driven architecture
  Cell division        ←→  process fork / container spawn
  Apoptosis            ←→  graceful process termination
  Cancer               ←→  unchecked infinite loop / security exploit
  Evolution            ←→  genetic algorithm (mutation + selection + drift)
  Development          ←→  staged deployment from single seed state
  Immune system        ←→  adaptive security with memory (learned signatures)

KEY INSIGHT: Biology runs highly parallel, massively distributed computation
  in a chemical substrate with:
  - ~3.8 Gyr of evolutionary optimization (no engineer has this runway)
  - Fault tolerance via redundancy, checkpoints, error correction
  - Self-assembly from first principles
  - Energy efficiency: brain uses ~20W for 86 billion neurons
  - Evolution as online learning: no gradient, just selection pressure

LIMITS OF ANALOGY:
  - No separation of program and hardware (protein is both)
  - No clean read/write memory (context-dependent expression)
  - Evolution is blind (no foresight) — not an optimizer with a goal
  - Stochasticity is fundamental (gene expression has noise by design)
```

---

## Cross-Module Concept Links

```
MOLECULAR-MACHINERY (01) feeds into all other modules:
  → DNA replication / repair → GENETICS (03)
  → Transcription factors, chromatin → GENETICS (03)
  → Protein signaling domains → CELL-BIOLOGY (02)
  → Metabolic enzymes → implicit in all physiology

GENETICS (03) → EVOLUTION (04):
  Mutation → raw material for selection
  Recombination → new combinations
  Neutral variation → molecular evolution

EVOLUTION (04) → ECOLOGY (05):
  Adaptation → niche use efficiency
  Speciation → community structure
  Coevolution → mutualism, arms races

ECOLOGY (05) → PHYSIOLOGY (06):
  Environmental pressures → physiological adaptation
  Climate → endocrine regulation
  Dietary ecology → digestive physiology
```

---

## What's Covered Elsewhere in This Library

The `natural-sciences/` directory covers overlapping material from a chemistry-first perspective:

| Topic | biology/ | natural-sciences/ |
|-------|----------|-------------------|
| Molecular biology | 01-MOLECULAR-MACHINERY.md (deep) | 09-MOLECULAR-BIO.md |
| Cell biology | 02-CELL-BIOLOGY.md | 10-CELL-BIOLOGY.md |
| Evolution & genetics | 03-GENETICS.md + 04-EVOLUTION.md | 11-EVOLUTION-GENETICS.md |
| Ecology | 05-ECOLOGY.md | 18-ECOLOGY.md (more comprehensive) |
| Biochemistry pathways | — | 06-BIOMOLECULES, 07-ENZYMES, 08-METABOLISM |
| Plasma/physics of life | — | 15-16-PLASMA-*.md |

The biology/ modules go deeper on the biological narrative, evolution, and physiology.
The natural-sciences/ modules integrate chemistry ↔ biology connections.

<!-- @editor[structure/P1]: Missing Decision Cheat Sheet — needs "which module for what question" in "use X when Y" format -->
<!-- @editor[structure/P2]: Missing Common Confusion Points section -->
