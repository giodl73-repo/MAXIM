# Biology — Overview

---

## Big Picture

```
BIOLOGY: the study of living systems — their structure, function, evolution,
         and molecular mechanisms

HIERARCHY OF ORGANIZATION:
  Atoms → Molecules → Macromolecules → Organelles → Cells
  → Tissues → Organs → Organisms → Populations → Ecosystems

CENTRAL DOGMA:
  DNA ──→ RNA ──→ Protein
       (transcription)  (translation)

  Information flows: DNA → RNA → Protein
  NOT: protein → DNA (general rule; reverse transcriptase is exception)

UNIFYING THEORIES:
  1. Cell theory: all life is composed of cells
  2. Evolution by natural selection (Darwin, 1859)
  3. Molecular basis of heredity (Watson-Crick, 1953)
  4. Biochemical universality: same genetic code in all life
```

---

## Why This Matters for an Engineer/AI Person

1. **Biotechnology revolution:** CRISPR, mRNA vaccines, protein folding (AlphaFold2), synthetic biology — all require understanding molecular biology at depth.

2. **AI for biology:** AlphaFold2 (2021, DeepMind) solved the protein folding problem. AlphaProteo designs novel proteins. Genomics uses ML to decode 3 billion base pairs. Biological data is now the largest scientific dataset.

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
│
├── Cell Biology
│     Cell organelles, membrane transport, cell signaling
│     Cell cycle, division, apoptosis
│
├── Genetics & Genomics
│     Mendelian genetics, population genetics, GWAS
│     Sequencing (NGS, long-read), personal genomics
│
├── Evolution
│     Natural selection, genetic drift, speciation
│     Molecular evolution, phylogenetics, evo-devo
│
├── Systems Biology
│     Gene regulatory networks, metabolic networks
│     Synthetic biology, network motifs
│
└── Biotechnology
      CRISPR/Cas9, mRNA vaccines, protein engineering
      AlphaFold2, drug discovery, diagnostics
```

---

## Module Map

| File | Topic |
|------|-------|
| `01-MOLECULAR-MACHINERY.md` | DNA, RNA, proteins — central dogma in molecular detail |
| `02-CELL-BIOLOGY.md` | Membrane, organelles, cell signaling, cell cycle |
| `03-GENETICS-GENOMICS.md` | Mendelian genetics, population genetics, NGS, GWAS |
| `04-EVOLUTION-SYSTEMS.md` | Natural selection, genetic drift, molecular evolution, network motifs |
| `05-BIOTECHNOLOGY-BRIDGE.md` | CRISPR, mRNA vaccines, AlphaFold2, synthetic biology, ML in biology |

---

## Key Numbers

```
Human genome:
  Base pairs:    ~3.2 × 10⁹ (3.2 Gbp)
  Protein-coding genes: ~20,000 (only ~1.5% of genome!)
  Total genes (incl. RNA): ~25,000-30,000
  Repetitive elements: ~50% of genome
  Information content: ~800 MB as compressed sequence

DNA:
  Diameter: 2 nm
  Rise per base pair: 0.34 nm
  Persistence length: ~50 nm (semirigid polymer)
  Total length if stretched: ~2 m (in every cell!)
  Supercoiling: tightly wound around histones → nucleosomes → chromatin

Proteins:
  Average size: 400 amino acids
  Average molecular weight: ~45 kDa
  Synthesis rate: ~20 amino acids/second (ribosome)
  Folding time: microseconds (small) to seconds (large/complex)
  Proteins in human body: ~20,000 types × >10^13 cells = ~10^17 total

Cell:
  Typical animal cell volume: ~2,000 μm³ (~10 μm diameter)
  Number of proteins in one cell: ~3-4 billion molecules
  Cell division time: 24 hours (typical mammalian)
  Number of cells in human body: ~37 trillion
```

---

## Historical Arc

```
1858: Virchow — omnis cellula e cellula (cell theory complete)
1859: Darwin — Origin of Species (natural selection)
1866: Mendel — laws of inheritance (rediscovered 1900)
1869: Miescher — discovers nucleic acid (DNA)
1944: Avery, MacLeod, McCarty — DNA is genetic material (not protein)
1953: Watson & Crick — DNA double helix structure (with Franklin/Wilkins data)
1961: Nirenberg, Khorana — genetic code cracked (Nobel 1968)
1973: Cohen, Boyer — recombinant DNA (first GMO)
1977: Sanger — DNA sequencing method (first widely used)
1983: Mullis — PCR (polymerase chain reaction) (Nobel 1993)
1990: Human Genome Project begins
2001: Human genome draft published (~$3B)
2003: Human genome project complete
2005: Next-generation sequencing (NGS) democratizes genomics
2012: Doudna & Charpentier — CRISPR-Cas9 as programmable editor (Nobel 2020)
2016: Single-cell RNA sequencing (scRNA-seq) — every cell's transcriptome
2020: mRNA vaccines (BNT162b2, mRNA-1273) against SARS-CoV-2
2021: AlphaFold2 — protein folding solved (DeepMind, Nobel Chemistry 2024)
2022: Complete human genome finally sequenced (T2T project)
2023+: Foundation models for biology (ESM-2, Evo, AlphaProteo)
```
