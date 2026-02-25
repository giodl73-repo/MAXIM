# Epigenomics

## The Big Picture

```
EPIGENOMICS: THE CHEMICAL LAYER ABOVE THE SEQUENCE
====================================================

  DNA SEQUENCE:     A T C G A T C G A T C G ...  (same in every cell)
  EPIGENOME:        m   m     m       m           (methylation marks)
                    ↑ acetyl ↑ methyl ↑           (histone modifications)
                    [  open  ][closed][  open  ]  (chromatin state)

  KEY PRINCIPLE: Same DNA sequence — different epigenetic state →
                 different gene expression → different cell identity.

  LIVER CELL vs. NEURON:
  ─ Identical DNA sequence
  ─ Different methylation patterns at thousands of genes
  ─ Different chromatin accessibility at enhancers
  ─ → ~3,000 different genes expressed (liver-specific vs. neural-specific)

  EPIGENETIC MECHANISMS:
  ┌────────────────────────────────────────────────────────────────┐
  │                                                                 │
  │  DNA METHYLATION         5-methylcytosine (5mC) at CpG sites  │
  │  ───────────────         Repressive in gene body/promoters     │
  │                          Measured by: bisulfite-seq, RRBS      │
  │                          Inherited through cell division        │
  │                                                                 │
  │  HISTONE MODIFICATIONS   Chemical tags on histone tails         │
  │  ──────────────────────  Acetylation (active), methylation      │
  │                          (active or repressive, context-dep)    │
  │                          Measured by: ChIP-seq                  │
  │                                                                 │
  │  CHROMATIN ACCESSIBILITY Nucleosome positioning/remodeling      │
  │  ──────────────────────  Open = transcription factor access     │
  │                          Measured by: ATAC-seq, DNase-seq       │
  │                                                                 │
  │  3D GENOME ORGANIZATION  Topologically Associating Domains      │
  │  ─────────────────────── (TADs), enhancer-promoter loops        │
  │                          Measured by: Hi-C, ChIA-PET            │
  └────────────────────────────────────────────────────────────────┘
```

---

## DNA Methylation

### Chemistry and Function

```
  DNA METHYLATION CHEMISTRY
  ==========================

  5-methylcytosine (5mC):
  Cytosine + methyl group donated by DNMT (DNA methyltransferase)
  at position 5 of the cytosine ring.

  CpG SITES: The dominant methylation context in mammals
  C─G dinucleotide (CpG = Cytosine-phosphate-Guanine)
  5% of cytosines are methylated; ~70–80% of all CpG sites methylated

  CpG ISLANDS:
  Regions with higher CpG density than expected
  Typically at gene promoters (~60% of human gene promoters)
  Usually UNMETHYLATED → gene can be expressed
  Methylation at CpG island → gene silenced

  FUNCTIONAL ROLES:
  ┌──────────────────────────────────────────────────────────┐
  │ Gene silencing: Methylated promoter CpGs recruit         │
  │   MBD proteins → chromatin compaction → no transcription │
  │                                                           │
  │ X-chromosome inactivation: One X chromosome fully        │
  │   methylated in females → transcriptionally silent       │
  │                                                           │
  │ Genomic imprinting: Parental-origin-specific methylation │
  │   e.g., IGF2 expressed only from paternal allele          │
  │                                                           │
  │ Transposon silencing: Repeat elements methylated to       │
  │   prevent transposition                                   │
  │                                                           │
  │ Cancer: CpG island hypermethylation silences tumor        │
  │   suppressor genes (e.g., CDKN2A in many cancers)        │
  └──────────────────────────────────────────────────────────┘

  DNMT ENZYMES:
  DNMT3A/3B: De novo methyltransferases (establish new methylation)
  DNMT1: Maintenance methyltransferase (copies marks to daughter strand)
  TET1/2/3: Demethylases (oxidize 5mC → 5hmC → demethylation)
```

### Bisulfite Sequencing

```
  BISULFITE SEQUENCING: HOW METHYLATION IS MEASURED
  ===================================================

  CHEMISTRY: Bisulfite reagent converts unmethylated C → U (reads as T)
             Methylated C (5mC) is PROTECTED → stays as C

  Before bisulfite:
  ATCGACTGCATCG
  Methylated:  5mC at position 4

  After bisulfite conversion:
  ATTGATTGTATGG   (unmethylated C → T)
   ^   ^ ^         methylated C stays C ─────┘

  After PCR and sequencing:
  - Original Cs that were methylated → sequenced as C
  - Original Cs that were unmethylated → sequenced as T
  - Compare to reference: C = methylated, T = unmethylated

  METHODS:
  WGBS (Whole-Genome Bisulfite Sequencing):
    - Coverage of all ~28 million CpG sites in human genome
    - Expensive: need ~30x coverage × larger library (both strands)
    - Gold standard for methylome profiling

  RRBS (Reduced Representation Bisulfite Sequencing):
    - MspI digestion enriches CpG-dense regions
    - ~1–3 million CpG sites; much cheaper
    - Good for CpG islands and gene promoters

  EPIC Array (Illumina):
    - 935,000 CpG sites as beads on array
    - No sequencing needed: fluorescence readout
    - Cheap ($200/sample), medium coverage
    - Standard in large epigenome studies

  ONT DIRECT METHYLATION:
    - Nanopore electrical signal differs for 5mC vs C
    - Detect methylation directly from WGS run, no bisulfite
    - Also detects 5hmC, 6mA (not possible with bisulfite)
```

---

## Histone Modifications and ChIP-seq

### Histone Code

```
  HISTONE STRUCTURE AND MODIFICATIONS
  =====================================

  Nucleosome = 147 bp DNA wrapped around 8 histones (2× H2A,H2B,H3,H4)
  Histone tails protrude from nucleosome → modification targets

  KEY HISTONE MARKS AND THEIR MEANING:
  ┌─────────────────────────────────────────────────────────────────┐
  │ H3K4me3   Active promoters                                      │
  │ H3K4me1   Enhancers (poised and active)                         │
  │ H3K27ac   Active enhancers and promoters (acetylation)          │
  │ H3K36me3  Actively transcribed gene bodies                      │
  │ H3K27me3  Polycomb repression (developmental silencing)         │
  │ H3K9me3   Heterochromatin (constitutive silencing, repeats)     │
  │ H3K9ac    Active promoters (acetylation)                        │
  │                                                                  │
  │ Bivalent domains: H3K4me3 + H3K27me3 simultaneously            │
  │   Poised for expression in stem cells — resolves upon           │
  │   differentiation (one mark wins)                               │
  └─────────────────────────────────────────────────────────────────┘

  NOTATION: H3 = histone 3, K4 = lysine at position 4, me3 = trimethyl
```

### ChIP-seq Protocol

```
  CHIP-SEQ: CHROMATIN IMMUNOPRECIPITATION + SEQUENCING
  ======================================================

  GOAL: Find all genomic locations where protein X binds DNA

  PROTOCOL:
  ┌──────────────────────────────────────────────────────┐
  │ 1. CROSSLINK: Add formaldehyde to living cells       │
  │    Proteins covalently linked to nearby DNA          │
  │                                                       │
  │ 2. SHEAR: Sonicate cells to fragment chromatin       │
  │    Target: ~200 bp fragments                         │
  │                                                       │
  │ 3. IMMUNOPRECIPITATE: Add antibody against target    │
  │    (e.g., anti-H3K27ac; or anti-CTCF; or anti-RNA-Pol2)│
  │    Antibody binds protein → protein pulls down DNA   │
  │                                                       │
  │ 4. REVERSE CROSSLINK: Heat to release DNA from protein│
  │                                                       │
  │ 5. SEQUENCE: Standard Illumina library prep          │
  │    Single-end 50 bp is usually sufficient            │
  │                                                       │
  │ 6. PEAK CALLING: MACS2/3 identifies regions enriched │
  │    vs. input control (unimmunoprecipitated DNA)      │
  └──────────────────────────────────────────────────────┘

  PEAK TYPES:
  Narrow peaks: Transcription factors (sharp, ~200 bp)
  Broad peaks:  Histone modifications covering gene bodies (~5–100 kb)

  MACS2 STATISTICS:
  ─ Compare IP enrichment to input (Poisson background model)
  ─ q-value (FDR-controlled) < 0.05 → peak called
  ─ fold enrichment (IP/input) > 10 is typical high-confidence peak
```

---

## ATAC-seq: Chromatin Accessibility

```
  ATAC-SEQ: ASSAY FOR TRANSPOSASE-ACCESSIBLE CHROMATIN
  ======================================================

  PRINCIPLE: Hyperactive Tn5 transposase cuts open (nucleosome-free)
             chromatin and inserts sequencing adapters simultaneously.
             Only accessible regions get cut and sequenced.

  Closed chromatin (nucleosome-wrapped): Tn5 BLOCKED → no cut
  Open chromatin (nucleosome-free): Tn5 CUTS → sequenced

  ┌─────────────────────────────────────────────────────────┐
  │  NUCLEOSOME-FREE REGION (NFR):                          │
  │  ──────────────────────────────                          │
  │  ...NNNNN[NFR: ~150 bp open]NNNNN...                    │
  │          ↑ TF binding here                              │
  │          ↑ Tn5 cuts here → short fragments             │
  │                                                          │
  │  NUCLEOSOME-OCCUPIED:                                   │
  │  ───────────────────────                                 │
  │  ...[NUC]...[NUC]...[NUC]...                            │
  │       ↑ 147 bp protected → longer fragments             │
  └─────────────────────────────────────────────────────────┘

  FRAGMENT SIZE DISTRIBUTION (ATAC-seq fingerprint):
  ~150 bp:  NFR fragments (nucleosome-free)
  ~300 bp:  Mono-nucleosomal fragments
  ~450 bp:  Di-nucleosomal fragments
  This nucleosomal ladder is diagnostic of successful ATAC-seq

  ADVANTAGES vs. ChIP-seq:
  ─ No antibody needed → works for ANY accessible region
  ─ Requires only ~50,000 cells (ChIP needs millions)
  ─ Works on frozen tissue, single cells (scATAC-seq)
  ─ Can infer TF occupancy by "footprinting" (protected ~20 bp under TF)

  PEAK CALLING: MACS2 with NFR-size fragments
  FOOTPRINTING: TOBIAS (reconstructs TF binding from nucleotide protection)
  scATAC-seq: ArchR, Signac (Seurat-based) for single-cell chromatin
```

---

## Hi-C: 3D Genome Organization

```
  HI-C: CAPTURING 3D CHROMATIN CONTACTS
  ========================================

  PRINCIPLE: Formaldehyde crosslinks DNA regions that are
             spatially close in the nucleus (even if far in sequence).
             Restriction digest + proximity ligation + sequencing
             reveals which genomic regions are near each other.

  PROTOCOL (simplified):
  1. Crosslink chromatin with formaldehyde
  2. Restrict digest (HindIII, MboI, or MNase)
  3. Fill ends, mark with biotin
  4. Proximity ligation (contact pairs are ligated together)
  5. Shear, pull down biotin-marked junctions
  6. Paired-end sequencing: each read pair = one chromatin contact

  OUTPUT: Contact matrix (N × N matrix of contact frequencies)
  Resolution: Depends on sequencing depth
    1 Mb resolution: ~100 million read pairs
    10 kb resolution: ~2–5 billion read pairs

  STRUCTURES REVEALED:
  ┌──────────────────────────────────────────────────────────────┐
  │ A/B COMPARTMENTS                                             │
  │   A compartment: active, gene-rich, open chromatin          │
  │   B compartment: inactive, gene-poor, compacted             │
  │   Correlation with H3K27ac/H3K9me3                          │
  │                                                              │
  │ TADs (Topologically Associating Domains)                    │
  │   ~200 kb – 1 Mb self-interacting domains                   │
  │   Boundary elements: CTCF + cohesin loop extrusion          │
  │   Disrupted TAD boundaries → ectopic enhancer contact       │
  │   → gene misexpression (linked to disease)                  │
  │                                                              │
  │ LOOPS                                                        │
  │   Enhancer–promoter contacts (10 kb – 1 Mb)                 │
  │   CTCF–CTCF convergent orientation forms insulating loops   │
  │   HiChIP/ChIA-PET: protein-centric loop identification       │
  └──────────────────────────────────────────────────────────────┘

  TAD BOUNDARY DISRUPTION IN CANCER:
  CTCF binding site deletion → TAD boundary lost
  → Oncogene now in contact range of strong enhancer
  → Oncogene overexpressed → cancer
  Example: MYC activation by 8q24 enhancer hijacking
```

---

## ENCODE and Reference Epigenomes

```
  ENCODE PROJECT (Encyclopedia of DNA Elements)
  ===============================================

  Goal: Annotate all functional elements in the human genome
  Scale: >22,000 experiments, >400 cell types
  Data types: ChIP-seq, ATAC-seq, RNA-seq, Hi-C, CAGE, RAMPAGE

  REGULATORY ELEMENT CLASSIFICATION:
  ─ Active promoters: H3K4me3 + H3K27ac + open ATAC
  ─ Active enhancers: H3K4me1 + H3K27ac + open ATAC
  ─ Poised enhancers: H3K4me1 + H3K27me3 (no H3K27ac)
  ─ CTCF sites: Loop anchors and TAD boundaries

  ROADMAP EPIGENOMICS:
  ─ 111 human cell types and tissues
  ─ 5-mark combination → 15 chromatin states per cell type
  ─ ChromHMM: HMM trained on 5 histone marks to call states
  ─ Enables cross-tissue comparison of regulatory activity
```

---

## Decision Cheat Sheet

| Goal | Method | Key Tool |
|------|--------|---------|
| Map DNA methylation genome-wide | WGBS | Bismark + DSS/MethylKit |
| Map CpG islands cheaply | EPIC Array | minfi (R package) |
| Find transcription factor binding | ChIP-seq | MACS2 + DiffBind |
| Find histone mark genome-wide | ChIP-seq | MACS2 (broad peaks) |
| Map open chromatin genome-wide | ATAC-seq | MACS2 + TOBIAS |
| Detect accessible chromatin per cell | scATAC-seq | ArchR or Signac |
| Map 3D chromatin interactions | Hi-C | Juicer, HiCExplorer |
| Find enhancer-promoter contacts | HiChIP/ChIA-PET | FitHiChIP |
| Profile multiple marks simultaneously | CUT&TAG or CUT&RUN | SEACR peak caller |
| Detect methylation without bisulfite | ONT direct sequencing | Modkit/DeepSignal |

---

## Common Confusion Points

**H3K4me3 vs. H3K4me1**: Both methylations on the same residue but with different numbers of methyl groups — and completely different biological meanings. Trimethylation (me3) marks active promoters. Monomethylation (me1) marks enhancers. The distinction is experimentally determined by the antibody specificity used in ChIP-seq.

**Active vs. poised enhancers**: H3K27ac marks active enhancers (actually looping to promoters). H3K4me1 without H3K27ac marks poised/primed enhancers (positioned but not currently active). During differentiation, poised enhancers gain H3K27ac when they become active.

**Bisulfite conversion efficiency**: If bisulfite conversion is incomplete, unmethylated Cs won't be converted to Ts and will be misclassified as methylated. Quality control checks Lambda spike-in (fully unmethylated control) to confirm >99.5% conversion efficiency.

**ATAC-seq mitochondrial DNA problem**: Mitochondria have no nucleosomes — their DNA is fully accessible. If cells contain many mitochondria, the Tn5 preferentially cuts mtDNA, resulting in most reads mapping to the mitochondrial genome (chrM). High mitochondrial read fraction (>40%) = failed ATAC-seq. Pre-filtering on intact nuclei is essential.

**TAD conservation vs. compartment dynamics**: TAD boundaries are largely conserved across cell types (defined by CTCF binding). A/B compartment assignments flip between cell types (a region in A in liver might be in B in brain). These are different levels of 3D organization responding to different regulatory signals.
