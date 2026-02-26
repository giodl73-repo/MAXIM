# Gene Expression and RNA-seq

## The Big Picture

```
FROM DNA TO EXPRESSION MEASUREMENT
=====================================

  CENTRAL DOGMA (the measurement context):

  DNA ──transcription──► pre-mRNA ──splicing──► mRNA ──translation──► Protein

  RNA-SEQ MEASURES: Which mRNAs are present, and in what quantity
  at a specific moment, in a specific tissue/cell population.

  KEY DIFFERENCE FROM GENOMICS:
  ┌────────────────────────────────────────────────────────────────┐
  │ GENOMICS (DNA-seq)                                              │
  │   Same in every cell of the body                               │
  │   Stable over time (mostly)                                    │
  │   Answer: "What could this organism make?"                     │
  │                                                                 │
  │ TRANSCRIPTOMICS (RNA-seq)                                       │
  │   Different in liver vs. brain vs. immune cells                │
  │   Changes with development, disease, drug treatment             │
  │   Answer: "What is this cell currently making, and how much?"  │
  └────────────────────────────────────────────────────────────────┘

  RNA-SEQ PIPELINE:
  ┌────────────────────────────────────────────────────────────────┐
  │  Biological sample                                              │
  │       │ RNA extraction + quality check (RIN score)             │
  │       ▼                                                         │
  │  Total RNA or poly(A)-selected mRNA                            │
  │       │ Library preparation (fragmentation, cDNA, adapters)    │
  │       ▼                                                         │
  │  FASTQ files (paired-end 2×150 bp typical)                     │
  │       │ Quality control (FastQC, trimming)                     │
  │       ▼                                                         │
  │  Alignment (STAR, HISAT2) or pseudo-alignment (kallisto, salmon)│
  │       │                                                         │
  │       ▼                                                         │
  │  Read counts per gene/transcript                                │
  │       │ Normalization (TPM, FPKM, TMM, VST)                    │
  │       ▼                                                         │
  │  Differential expression (DESeq2, edgeR, limma)                │
  │       │                                                         │
  │       ▼                                                         │
  │  Gene lists + pathway analysis (GSEA, g:Profiler)              │
  └────────────────────────────────────────────────────────────────┘
```

---

## Library Preparation

```
  RNASEQ LIBRARY PREPARATION CHOICES
  ====================================

  POLY(A) SELECTION:
  ─ Captures mRNAs with poly(A) tail (most coding genes)
  ─ Removes rRNA (>90% of total RNA) efficiently
  ─ Misses non-polyadenylated RNAs (some IncRNAs, histone mRNAs)
  ─ Standard choice for bulk mRNA profiling

  RIBOSOMAL DEPLETION (RiboZero):
  ─ Removes rRNA but keeps all other RNA types
  ─ Better for: degraded samples, prokaryotes (no poly-A)
  ─ Also captures long non-coding RNAs, circular RNAs

  STRAND-SPECIFICITY:
  Most modern libraries are stranded (dUTP method):
  ─ Preserves which strand (sense/antisense) was transcribed
  ─ Critical for antisense transcripts and overlapping genes
  ─ dUTP: second strand marked with dU → degraded → original strand preserved

  TOTAL RNA vs. TARGETED:
  Total mRNA-seq: ~20,000 genes quantified per sample
  Targeted (amplicon): 100–2,000 genes, cheaper, less noise
  CITE-seq: RNA + protein surface markers simultaneously (single-cell)
```

---

## Alignment: Two Paradigms

### 1. Splice-Aware Alignment (STAR, HISAT2)

```
  SPLICE-AWARE ALIGNMENT
  =======================

  CHALLENGE: mRNA has introns removed. A 100-bp read spanning
  an exon junction won't align continuously to genomic DNA.

  Example:
  Genome:  EXON1──────INTRON──────EXON2
  mRNA:    EXON1──EXON2    (intron spliced out)
  Read:    ───────────────────────────
           half in EXON1, half in EXON2 → must split-align

  STAR (Spliced Transcripts Alignment to a Reference):
  ─ Two-pass alignment: discover splice junctions in pass 1,
    use them to improve alignment in pass 2
  ─ Very fast (uses suffix array index)
  ─ Default for most bulk RNA-seq workflows
  ─ Outputs: BAM file (standard alignment), junction files

  HISAT2:
  ─ Graph-based alignment using known SNPs/splice sites
  ─ Lower memory than STAR
  ─ Integrates population variation into alignment

  OUTPUT: BAM file
  ─ Same format as DNA-seq BAM
  ─ Key difference: Reads have N cigar operations (intron skips)
  ─ Example: 50M10000N50M = 50 bp match, 10 kb intron, 50 bp match
```

### 2. Pseudo-Alignment / Lightweight Quantification (kallisto, salmon)

```
  PSEUDO-ALIGNMENT: QUANTIFY WITHOUT FULL ALIGNMENT
  ===================================================

  KEY INSIGHT: For gene/transcript quantification, you don't
  need to know exactly WHERE each read aligns — just WHICH
  transcript it came from.

  KALLISTO:
  ─ Builds De Bruijn index of transcript sequences
  ─ Maps k-mers from reads to transcripts (very fast)
  ─ EM algorithm: resolve multi-mapping reads probabilistically
  ─ Speed: 30x faster than STAR for quantification only
  ─ 500 million reads in ~10 minutes on laptop

  SALMON:
  ─ Similar to kallisto but corrects for:
    - GC bias (fragments with more GC are over-represented)
    - Positional bias (ends of transcripts under-sequenced)
    - Sequence-specific bias (adapter/primer effects)
  ─ Outputs transcript-level estimates
  ─ tximport in R propagates transcript uncertainty to gene level

  SALMON vs. STAR+featureCounts:
  Both give similar gene-level counts for well-annotated genomes.
  Salmon/kallisto: faster, handles multi-mapping better, transcript-aware.
  STAR: required if you need splice junction discovery or custom analyses.
```

---

## Count Normalization

```
  WHY RAW COUNTS ARE MISLEADING
  ==============================

  Raw count for Gene A = 1,000 reads in Sample 1
  Raw count for Gene A = 500 reads in Sample 2

  Is Gene A 2x higher in Sample 1?

  MAYBE NOT. Could be because:
  1. Sample 1 had more total RNA sequenced (library size effect)
  2. Gene A is longer → more fragments captured per molecule (length bias)
  3. Sample 2 had one very highly expressed gene consuming all reads

  NORMALIZATION METHODS:
  ┌───────────────────────────────────────────────────────────────────┐
  │ RPKM/FPKM (Reads/Fragments Per Kilobase per Million mapped reads)│
  │   Corrects for: library size + gene length                       │
  │   Problem: Not comparable across samples (sum ≠ same)            │
  │   Status: Deprecated for DGE; still used in some contexts        │
  │                                                                   │
  │ TPM (Transcripts Per Million)                                    │
  │   Corrects for: gene length first, then library size             │
  │   Sum per sample = 1,000,000 (comparable across samples)         │
  │   Status: Preferred for expression level reporting               │
  │                                                                   │
  │ TMM (edgeR) / DESeq2 size factors                                │
  │   Normalizes to housekeeping reference (no length correction)    │
  │   Designed specifically for DGE statistical testing              │
  │   Assumes: most genes are NOT differentially expressed           │
  │   Status: Required for DESeq2/edgeR statistical tests            │
  │                                                                   │
  │ VST / rlog (DESeq2)                                              │
  │   Variance-stabilizing transformation for PCA/visualization      │
  │   Makes variance independent of mean (heteroscedasticity fix)    │
  └───────────────────────────────────────────────────────────────────┘

  TPM FORMULA:
  RPK_i = count_i / (gene_length_i / 1000)  [reads per kilobase]
  TPM_i = RPK_i / (sum(RPK) / 10^6)          [scale to per million]
```

---

## Differential Expression Analysis

### DESeq2 Model

```
  DESEQ2: NEGATIVE BINOMIAL MODEL FOR COUNT DATA
  ================================================

  WHY NOT JUST T-TEST?
  ─ RNA-seq counts are integers (0, 1, 2...)
  ─ Highly variable: gene with mean 10 counts might range 0–100
  ─ Mean-variance relationship: variance grows with mean
  ─ Negative binomial distribution models this correctly

  DESEQ2 MODEL:
  count_ij ~ NegBinomial(mean = μ_ij, dispersion = α_i)

  μ_ij = s_j × q_ij        (size factor × expected fraction)

  log(q_ij) = β_i0 + β_i1 × treatment_j   (log-linear model)

  β_i1 = log fold change for gene i under treatment

  DISPERSION ESTIMATION (the secret sauce):
  ─ With only 3–5 replicates, per-gene dispersion estimates are noisy
  ─ DESeq2 uses "shrinkage": borrows information across all genes
  ─ Genes with similar mean expression share dispersion information
  ─ Result: stable estimates even with n=3 replicates per group

  SIGNIFICANCE:
  ─ Wald test (for simple contrasts) or LRT (for complex models)
  ─ P-value → BH-adjusted p-value (padj, FDR correction)
  ─ Standard threshold: padj < 0.05, |log2FC| > 1

  OUTPUT: DESeqDataSet with results():
  ┌─────────────────────────────────────────────────────────┐
  │ baseMean   Average normalized count across all samples   │
  │ log2FC     Log2(treatment/control)                       │
  │ lfcSE      Standard error of log2FC                     │
  │ stat       Wald test statistic                           │
  │ pvalue     Unadjusted p-value                           │
  │ padj       BH-adjusted p-value (FDR)                    │
  └─────────────────────────────────────────────────────────┘
```

### Volcano Plots and MA Plots

```
  STANDARD VISUALIZATION
  =======================

  VOLCANO PLOT:
  x-axis: log2(fold change)
  y-axis: -log10(adjusted p-value)

  Top-right: Significantly upregulated
  Top-left:  Significantly downregulated
  Bottom:    Not significant or small effect

                 10 │     *  *                 * * *
   -log10(padj)     │        *  * *       ** ****
                  5 │               ***  *** ***
                    │      ············ FC threshold
                  1 │─────────────────────────────
                    │   -3   -2   -1   0   1   2   3
                                   log2FC

  MA PLOT:
  x-axis: log2(mean expression) — the A (average)
  y-axis: log2(fold change) — the M (minus)
  Reveals: Low-count genes have noisy FC estimates (wide spread at left)
  DESeq2's lfcShrink() compresses low-count FC estimates toward zero
```

---

## Single-Cell RNA-seq Analysis

```
  SINGLE-CELL RNA-SEQ WORKFLOW (after 10x sequencing)
  =====================================================

  INPUT: Count matrix (genes × cells, ~20,000 × ~10,000)
         Very sparse: ~80–90% zeros

  STEP 1: QUALITY CONTROL
  ┌─────────────────────────────────────────────────────┐
  │ Filter low-quality cells:                           │
  │   - Too few genes detected (<200 → empty droplet)  │
  │   - Too many genes (>5,000 → doublets)             │
  │   - High mitochondrial % (>20% → dying cell)       │
  │ Filter unexpressed genes: keep genes in >3 cells    │
  └─────────────────────────────────────────────────────┘

  STEP 2: NORMALIZATION + LOG TRANSFORM
  ┌─────────────────────────────────────────────────────┐
  │ Normalize each cell to 10,000 total counts (CPM)   │
  │ Log1p transform: log(counts + 1)                   │
  │ Select highly variable genes (HVGs): top 2,000–3,000│
  └─────────────────────────────────────────────────────┘

  STEP 3: DIMENSIONALITY REDUCTION
  ┌─────────────────────────────────────────────────────┐
  │ PCA on HVGs (20,000 genes → 50 PCs)                │
  │ UMAP/t-SNE on top PCs (50 PCs → 2D visualization)  │
  │ UMAP preserves global structure; t-SNE = local only │
  └─────────────────────────────────────────────────────┘

  STEP 4: CLUSTERING
  ┌─────────────────────────────────────────────────────┐
  │ Build k-nearest neighbor graph in PC space          │
  │ Community detection (Leiden/Louvain algorithm)      │
  │ Result: clusters = putative cell types              │
  └─────────────────────────────────────────────────────┘

  STEP 5: ANNOTATION
  ┌─────────────────────────────────────────────────────┐
  │ Find marker genes per cluster (Wilcoxon or LR test) │
  │ Compare to known cell-type markers                  │
  │ T cells: CD3E, CD4, CD8A                           │
  │ B cells: CD19, CD79A, MS4A1                         │
  │ Macrophages: CD14, LYZ, FCGR3A                     │
  │ Assign cell type labels to clusters                 │
  └─────────────────────────────────────────────────────┘

  STEP 6: DOWNSTREAM ANALYSIS
  ┌─────────────────────────────────────────────────────┐
  │ Trajectory/pseudotime (RNA velocity, Monocle)        │
  │ Cell-cell communication (CellChat, NicheNet)         │
  │ Multi-sample DE (Pseudobulk → DESeq2)               │
  │ Doublet detection (Scrublet, DoubletFinder)          │
  └─────────────────────────────────────────────────────┘
```

---

## Pathway Analysis

```
  GENE SET ENRICHMENT ANALYSIS (GSEA)
  =====================================

  PROBLEM: Differential expression gives a list of genes.
           What biological processes are affected?

  APPROACH 1: OVER-REPRESENTATION ANALYSIS (ORA)
  ─ Take top N differentially expressed genes
  ─ Test if any pathway is enriched: hypergeometric test
  ─ Limitation: arbitrary cutoff, ignores rank/effect size

  APPROACH 2: GSEA (Broad Institute)
  ─ Use ALL genes, ranked by test statistic or log2FC
  ─ Walk ranked list: each gene in pathway = step up (+1)
  ─ Gene not in pathway = step down (-1/n)
  ─ Enrichment score = maximum deviation from center
  ─ Permutation test: shuffle gene labels to get null distribution
  ─ NES (Normalized Enrichment Score) = comparable across pathways

  PATHWAY DATABASES:
  ┌──────────────────────────────────────────────────────┐
  │ MSigDB: Molecular Signatures Database (7.5 databases)│
  │   H: hallmark gene sets (50 curated)                 │
  │   C2: curated pathways (KEGG, Reactome, BioCarta)    │
  │   C5: Gene Ontology terms                            │
  │   C7: immunologic signatures                         │
  │                                                       │
  │ Reactome: human pathway hierarchy                    │
  │ KEGG: biochemical pathway maps                       │
  │ GO: Gene Ontology (MF/BP/CC)                         │
  └──────────────────────────────────────────────────────┘
```

---

## Decision Cheat Sheet

| Goal | Tool |
|------|------|
| Align RNA-seq to genome | STAR (most common) or HISAT2 |
| Quantify transcript abundance fast | kallisto or salmon (pseudo-alignment) |
| Differential expression (bulk) | DESeq2 (negative binomial, recommended) |
| Differential expression (large dataset) | edgeR (similar model, sometimes faster) |
| Report expression levels | TPM (normalized, cross-sample comparable) |
| Single-cell analysis | Seurat (R) or Scanpy/AnnData (Python) |
| Pathway enrichment | GSEA (ranked) or g:Profiler (ORA) |
| Visualize DE results | Volcano plot (effect + significance) |
| Correct for technical variation | DESeq2 design formula (batch as covariate) |
| Detect doublets in scRNA-seq | Scrublet or DoubletFinder |

---

## Common Confusion Points
<!-- @editor[bridge/P3]: Natural bridge opportunity -- DESeq2 negative binomial model and shrinkage estimation parallel Bayesian inference in signal processing / empirical Bayes in large-scale hypothesis testing, which the learner knows from statistics -->

**TPM vs. FPKM**: FPKM normalizes library size first, then gene length — the resulting values don't sum to a constant across samples. TPM normalizes length first, then library size — sums to 10^6 per sample. TPM is directly comparable across samples; FPKM is not. Use TPM for reporting.

**Why DESeq2 doesn't use TPM**: DESeq2 works on raw integer counts and does its own normalization internally (size factors). Feeding TPM into DESeq2 is wrong — it loses the count distribution properties the model depends on.

**Log fold change shrinkage**: Raw log2FC estimates for low-expression genes are extremely noisy (gene with 2 vs. 4 reads = log2FC of 1.0, but this is meaningless with counts that small). DESeq2's lfcShrink() applies an empirical Bayes prior that compresses unreliable fold changes toward zero. Always use lfcShrink for ranking genes or making figures.

**Single-cell pseudobulk vs. single-cell DE**: Naive per-cell DE tests (treating each cell as an independent observation) are statistically invalid — cells from the same patient are correlated. Pseudobulk approach: sum counts per patient per cell type, then use DESeq2 on the per-sample totals. This respects the biological replication unit.

**scRNA-seq sparsity**: Most genes read zero in most cells — this is expected, not missing data. It reflects the stochastic nature of gene expression (transcriptional bursting) plus the low sensitivity of droplet-based capture (~10–20% of mRNA molecules actually captured). Imputation methods exist but are controversial — many analyses use sparse data directly.
