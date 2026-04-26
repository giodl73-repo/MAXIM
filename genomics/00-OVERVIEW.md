# Genomics — Landscape Overview

## The Big Picture

```
GENOMICS LANDSCAPE
==================

  GENERATION 1 (1977–2003)       GENERATION 2 (2005–present)     GENERATION 3 (2011–present)
  ========================       ============================     ===========================
  Sanger Sequencing              Short-Read (Illumina)            Long-Read
  ~1 kb/read                     ~150 bp reads                    ONT: 10 kb–Mb-length reads
  Capillary electrophoresis      Bridge PCR amplification         PacBio: 15–25 kb HiFi reads
  Human Genome Project           HiSeq/NovaSeq platforms          Telomere-to-telomere assembly
  13 years, $2.7B                $1,000 genome achieved 2014      ~$200–400/genome (2024)
  (1990–2003)                    ~90 GB/day on NovaSeq X          Complete sequences now possible

                           DATA TYPES FROM SEQUENCING
                           ==========================

  WGS (whole-genome) ─────────── Full 3.2 Gb genome, all variants
  WES (whole-exome) ──────────── Just the ~1.5% that codes protein
  RNA-seq ─────────────────────── Which genes are expressed, how much
  ChIP-seq ────────────────────── Where proteins bind to chromatin
  ATAC-seq ────────────────────── Which chromatin regions are open
  Hi-C ────────────────────────── 3D genome organization
  scRNA-seq ───────────────────── Per-cell gene expression
  Spatial TX ──────────────────── Expression + tissue location

                         THE BIOINFORMATICS STACK (maps to software stack)
                         ==================================================

  ┌────────────────────────────────────────────────────────────────┐
  │  APPLICATIONS                                                  │
  │  Personalized medicine · GWAS · CRISPR target design           │
  │  Clinical reporting · Drug discovery · Cancer monitoring       │
  ├────────────────────────────────────────────────────────────────┤
  │  ANALYSIS TOOLS (like application frameworks)                   │
  │  GATK · DESeq2 · PLINK · Seurat · STAR · kallisto/salmon       │
  ├────────────────────────────────────────────────────────────────┤
  │  FILE FORMATS (data contracts — like .proto or OpenAPI spec)   │
  │  FASTQ → BAM/CRAM → VCF/GVCF → BED/GTF                         │
  ├────────────────────────────────────────────────────────────────┤
  │  WORKFLOW ENGINES (like MSBuild/ADF pipelines)                  │
  │  Snakemake · Nextflow · WDL/Cromwell · CWL                     │
  ├────────────────────────────────────────────────────────────────┤
  │  CLOUD COMPUTE (familiar territory)                            │
  │  Terra · DNAnexus · Azure Microsoft Genomics                   │
  │  AWS HealthOmics · Google Cloud Life Sciences                  │
  └────────────────────────────────────────────────────────────────┘
```

---

## Scale: Why This Is a Data Engineering Problem

```
  GENOMIC DATA SCALE
  ==================

  Human genome (haploid):     3.2 × 10⁹ base pairs
  Human genome (diploid):     6.4 × 10⁹ base pairs (two copies)
  Protein-coding sequence:    ~1.5% of genome (~50 Mb exome)
  Protein-coding genes:       ~20,000 genes
  Typical SNP density:        ~1 variant per 1,000 bp vs. reference
  Total variants per person:  ~3–4 million SNPs, ~500,000 indels

  DATA VOLUMES PER EXPERIMENT
  ============================

  30x WGS (standard):         ~90 GB raw FASTQ
  After alignment (BAM):      ~50 GB
  After compression (CRAM):   ~15 GB (reference-anchored)
  Final VCF:                  ~1 GB (called variants only)
  Compression ratio:          ~90:1 from raw to VCF

  POPULATION-SCALE PROJECTS
  ==========================

  UK Biobank:                 500,000 genomes
  All of Us (NIH):            1,000,000+ genomes planned
  gnomAD v4:                  730,947 exomes + 76,215 genomes
  Storage per project:        Petabyte class
  Compute:                    Millions of CPU-hours per analysis

  ANALOGY: This is like Azure Data Factory managing petabyte ETL.
  FASTQ = raw event logs. BAM = indexed structured store.
  VCF = aggregated fact table. Workflow = the ADF pipeline DAG.
```

---

## Genomics vs. Related Omics Fields

| Field | What It Measures | Snapshot Type | Key Tools |
|-------|-----------------|---------------|-----------|
| **Genomics** | DNA sequence and variants | Stable (same in all cells) | BWA, GATK, Illumina |
| **Transcriptomics** | RNA expression levels | Dynamic (varies by cell/time) | STAR, kallisto, DESeq2 |
| **Proteomics** | Protein abundance | Dynamic, post-translational | LC-MS/MS, MaxQuant |
| **Epigenomics** | DNA/histone modifications | Semi-stable, heritable | bisulfite-seq, ChIP-seq |
| **Metabolomics** | Small-molecule metabolites | Dynamic, systemic readout | NMR, mass spec |
| **Metagenomics** | All genomes in a sample | Community snapshot | Kraken2, MetaPhlAn, MetaSPAdes |
| **Single-cell** | Per-cell expression | Cell-type resolved | 10x Genomics, Seurat, Scanpy |

---

## Genomics Subdisciplines

```
  STRUCTURAL GENOMICS
  ─ Chromosome organization, centromeres, telomeres, repeats
  ─ Methods: Hi-C, optical mapping, long-read assembly
  ─ Goal: Complete reference genome (T2T project closed all gaps)

  FUNCTIONAL GENOMICS
  ─ Which DNA sequences do what — regulatory elements, enhancers
  ─ Methods: ENCODE, ATAC-seq, CRISPRi screens
  ─ Goal: Annotate non-coding genome function

  COMPARATIVE GENOMICS
  ─ Evolution by comparing genomes across species
  ─ Methods: LASTZ, MAFFT alignment; synteny analysis
  ─ Goal: Identify conserved functional elements

  POPULATION GENOMICS
  ─ Genetic variation across individuals and populations
  ─ Methods: GWAS, admixture, FST statistics
  ─ Goal: Link variants to traits and disease risk

  CLINICAL GENOMICS
  ─ Variant interpretation for diagnosis and treatment
  ─ Methods: ACMG classification guidelines, ClinVar, PharmGKB
  ─ Goal: Return actionable results to patients

  CANCER GENOMICS
  ─ Somatic mutations acquired during tumor development
  ─ Methods: Tumor-normal paired WGS/WES, ctDNA
  ─ Goal: Identify driver mutations, guide therapy
```

---

## The Central Dogma Connection

Genomics sits at the DNA layer. To understand why it matters, recall the central dogma (covered in natural-sciences/09-MOLECULAR-BIO.md):

```
  DNA ──transcription──► RNA ──translation──► Protein ──► Function

  Genomics studies:    ↑ this layer
  Transcriptomics:              ↑ this layer
  Proteomics:                            ↑ this layer

  Key insight: DNA is the instruction set. RNA is the executing program.
  Proteins are the running processes. Most disease variants alter DNA
  in ways that affect RNA production or protein function downstream.
```

---

## File Roadmap

| File | What It Covers |
|------|----------------|
| 01-SEQUENCING-TECH.md | How DNA gets read — Sanger → Illumina → nanopore generations |
| 02-GENOME-ASSEMBLY.md | Turning reads into genomes — graph algorithms, de Bruijn, phasing |
| 03-VARIANT-CALLING.md | Finding what differs — SNPs, indels, CNVs; GATK HaplotypeCaller |
| 04-GENE-EXPRESSION.md | RNA-seq: which genes active, in which cells, by how much |
| 05-EPIGENOMICS.md | Chemical layer above sequence — methylation, histone marks, ATAC |
| 06-GWAS.md | Association studies — connecting variants to traits in populations |
| 07-CRISPR.md | Genome editing — guide RNA as search string, Cas9 as editor |
| 08-BIOINFORMATICS-PIPELINE.md | Engineering layer — formats, workflows, cloud compute, databases |
| 09-PERSONALIZED-MEDICINE.md | Clinical applications — pharmacogenomics, cancer, rare disease |

---

## Decision Cheat Sheet

| I want to... | Approach |
|-------------|---------|
| Sequence the full genome | WGS, 30x coverage, Illumina short-read |
| Find protein-altering variants cheaply | WES, 100x coverage, ~$300 |
| Measure gene expression | RNA-seq (bulk) or scRNA-seq (per cell) |
| Type known common variants at scale | SNP array, ~$50 per sample |
| Get long contiguous sequences | PacBio HiFi or Oxford Nanopore |
| Profile chromatin accessibility | ATAC-seq |
| Map protein–DNA binding | ChIP-seq |
| Sequence a microbial community | Metagenomic shotgun sequencing |
| Find disease-associated variants in population | GWAS (need thousands of samples) |
| Edit the genome | CRISPR-Cas9 (→ 07-CRISPR.md) |
| Identify cancer driver mutations | Tumor-normal paired WGS/WES |
| Detect cancer from blood | Liquid biopsy / ctDNA sequencing |

---

## The Genomics Pipeline as a Data Engineering Problem

The genomics stack maps almost perfectly onto a modern data engineering pipeline — not as an analogy but as a structural identity.

```
GENOMICS PIPELINE ↔ DATA ENGINEERING STACK
──────────────────────────────────────────────────────────────────────────────
RAW DATA ACQUISITION:
  Sequencer output (FASTQ)          ↔  Raw event log (append-only stream)
  Base quality scores (Q30)         ↔  Event confidence / reliability metadata
  Paired-end reads                  ↔  Paired records in a message queue
  Multiplexed samples on flow cell  ↔  Multi-tenant data in shared ingestion

TRANSFORMATION PIPELINE:
  Alignment (BWA, STAR)             ↔  ETL: map raw logs → structured records
  SAM → BAM (sorted + indexed)      ↔  Columnar storage (Parquet/ORC + index)
  CRAM (reference-anchored compress)↔  Delta encoding / reference compression
  Mark duplicates (Picard)          ↔  Deduplication step in ETL
  Base quality recalibration (BQSR) ↔  Calibration pass to correct systematic bias

FORMAT CONTRACTS:
  FASTQ                             ↔  Raw log format (unstructured, high volume)
  BAM/CRAM                          ↔  Structured binary store (sorted, indexed)
  VCF                               ↔  Change log / diff against reference
  BED/GTF                           ↔  Region annotation (like partition metadata)
  BCF                               ↔  Binary-encoded VCF (like compressed Parquet)

ORCHESTRATION:
  Snakemake / Nextflow / WDL        ↔  MSBuild / ADF pipeline / Airflow DAG
  Scatter-gather in WDL             ↔  Fan-out parallelism in ADF
  cromwell on Terra                 ↔  Azure Batch + Data Factory

STORAGE:
  gnomAD variant database           ↔  Reference data lake (population-scale)
  dbSNP / ClinVar                   ↔  Lookup tables / dimension tables
  RefSeq / Ensembl annotation       ↔  Metadata catalog

QUERY / ANALYTICS:
  PLINK (GWAS linear regression)    ↔  Statistical modeling on feature tables
  DESeq2 (differential expression)  ↔  Group-by + hypothesis test on count data
  GSEA pathway analysis             ↔  Feature enrichment / set intersection

COMPRESSION RATIOS:
  Raw FASTQ: ~90 GB per 30x genome
  BAM:       ~50 GB (10-15x compression vs raw)
  CRAM:      ~15 GB (reference-anchored delta compression)
  VCF:       ~1 GB  (just the variants — 90:1 from raw)
  Equivalent: structured event data → columnar OLAP store → materialized summary
──────────────────────────────────────────────────────────────────────────────
```

**Key architectural insight:** The genome is a read-once reference (like a schema or a versioned schema migration). Every person's genome is a VCF — a diff against the reference. All downstream analysis is operating on diffs, not full copies. This is why population-scale genomics is tractable: you store one 3 GB reference + millions of 1 GB VCFs rather than millions of 90 GB FASTQs.

## Common Confusion Points

**Genome vs. exome vs. transcriptome**: The genome is all DNA in the cell nucleus. The exome is the ~1.5% of that genome encoding protein. The transcriptome is RNA — it only captures genes actively expressed at a given moment, varies by cell type and state, and changes in response to environment.

**Coverage depth vs. breadth**: "30x coverage" means the average base position is read 30 times. More coverage = better variant detection (especially heterozygotes). Breadth is the fraction of the target covered at all. Low-coverage arrays (0.1x) are sufficient for GWAS; clinical diagnosis needs 30x+ WGS or 100x WES.

**Reference genome is not your genome**: GRCh38 (the human reference) is a composite from ~20 donors, primarily of European ancestry. Your genome differs at ~3–4 million positions. The reference is a coordinate system for reporting variants, not a "normal" genome.

**Short-read accuracy vs. long-read completeness**: Illumina short reads (~150 bp) are 99.9%+ accurate per base, cheap, and excellent for SNPs/small indels. Long reads (ONT, PacBio) span repetitive regions (centromeres, segmental duplications) that short reads cannot resolve, but historically had higher error rates. PacBio HiFi solved this via circular consensus sequencing (~99.9% per base, 15–25 kb reads).

**CRISPR origin**: CRISPR was not engineered — it is a natural bacterial immune memory system. Bacteria use it to store viral DNA fragments and destroy matching sequences on reinfection. Scientists repurposed it as a programmable genome editor. (→ microbiology/08-MICROBIAL-GENETICS.md for the natural system; 07-CRISPR.md for the engineering.)
