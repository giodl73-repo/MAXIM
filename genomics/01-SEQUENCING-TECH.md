# Sequencing Technologies

## The Big Picture

```
SEQUENCING TECHNOLOGY GENERATIONS
===================================

  GENERATION 1: SANGER (1977–present for Sanger, gold standard for short targets)
  ─────────────────────────────────────────────────────────────────────────────────
  Principle: Chain-termination — ddNTPs stop extension at known bases
  Read length: 600–1,000 bp
  Throughput: ~96 samples/run (capillary)
  Cost: ~$0.50–1.00/read
  Use today: Validation of specific variants, Sanger confirmation of CRISPR edits

  GENERATION 2: SHORT-READ (Illumina, 2006–present, dominates market)
  ─────────────────────────────────────────────────────────────────────
  Principle: Bridge PCR amplification + sequencing by synthesis (SBS)
  Read length: 75–300 bp (typically 2×150 bp paired-end)
  Throughput: ~3.2 billion reads/run (NovaSeq X)
  Cost: ~$6–10/Gb; $200–500/WGS genome
  Error rate: ~0.1% per base
  Weakness: Cannot span repetitive regions >300 bp

  GENERATION 3: LONG-READ (Oxford Nanopore, PacBio, 2011–present)
  ─────────────────────────────────────────────────────────────────
  Oxford Nanopore (ONT):
    Principle: Electrical signal as DNA threads through protein pore
    Read length: N50 ~15–50 kb; individual reads up to 4 Mb
    Cost: ~$50–100/Gb (PromethION)
    Error rate: Raw ~5–10%; with Dorado basecalling ~2–5%
    Unique: Real-time, can detect base modifications directly

  PacBio HiFi (CCS):
    Principle: Single molecule real-time (SMRT) + circular consensus
    Read length: 10–25 kb (HiFi mode)
    Accuracy: >99.9% (Phred Q30+) per base
    Cost: ~$10–20/Gb (Revio platform)
    Sweet spot: High accuracy + long reads → best of both worlds

  SPECIALIZED (4th generation concepts)
  ───────────────────────────────────────
  Spatial transcriptomics (10x Visium): Gene expression with x,y coordinates
  Single-cell (10x scRNA-seq): Per-droplet barcoding, one cell per barcode
  Direct RNA sequencing (ONT): Sequence RNA without cDNA conversion step
```

---

## Illumina: Deep Dive on the Dominant Platform

Illumina holds ~80% of the global sequencing market. Understanding its chemistry explains the data you work with.

```
  ILLUMINA WORKFLOW
  =================

  STEP 1: LIBRARY PREPARATION
  ┌──────────────────────────────────────────────────────┐
  │ Fragment DNA to ~300–500 bp (sonication or enzyme)   │
  │ Repair ends, add A-tail                              │
  │ Ligate adapters (P5 and P7 sequences)                │
  │ Add sample-specific barcode (index) for multiplexing │
  │ PCR amplify (6–12 cycles)                            │
  └──────────────────────────────────────────────────────┘
              │
              ▼
  STEP 2: CLUSTER GENERATION ON FLOW CELL
  ┌──────────────────────────────────────────────────────┐
  │ DNA fragments bind to complementary oligos on glass  │
  │ Bridge PCR: fragment bends, hybridizes to neighbor,  │
  │   amplifies in place → cluster of ~1,000 copies      │
  │ Result: spatially isolated "clonal cluster"          │
  │ ~3.2 billion clusters/NovaSeq X flowcell             │
  └──────────────────────────────────────────────────────┘
              │
              ▼
  STEP 3: SEQUENCING BY SYNTHESIS (SBS)
  ┌──────────────────────────────────────────────────────┐
  │ Add all 4 fluorescent, reversibly-terminated dNTPs   │
  │ Polymerase incorporates one nucleotide               │
  │ Laser excites: camera reads which color per cluster  │
  │ Remove terminator, wash, repeat for next cycle       │
  │ Each cycle = one base read                           │
  │ 150 cycles = 150 bp per read                         │
  └──────────────────────────────────────────────────────┘
              │
              ▼
  STEP 4: BASE CALLING
  ┌──────────────────────────────────────────────────────┐
  │ Raw: fluorescence intensity images per cycle         │
  │ Basecaller converts images → FASTQ file              │
  │ Each base gets quality score Q = -10 log₁₀(P_error) │
  │ Q30 = 0.1% error, Q40 = 0.01% error                 │
  └──────────────────────────────────────────────────────┘

  KEY LIMITATION: Bridge PCR requires local amplification.
  This means reads are short (polymerase falls off, signal
  degrades), and repetitive sequences collapse (identical
  clusters are indistinguishable).
```

---

## Oxford Nanopore: Electrical Sequencing

```
  OXFORD NANOPORE TECHNOLOGY (ONT)
  =================================

  CONCEPT: Measure electrical current as single DNA molecule
           threads through a protein pore in a membrane

  ┌─────────────────────────────────────────────────────┐
  │                  NANOPORE PORE                       │
  │                                                      │
  │  Upper chamber (+)                                   │
  │  ─────────────────────────────                       │
  │         A   T   G   C   C                            │
  │          ╲  │  /  │  /                               │
  │           ┌─┴──┴──┴──┘                               │
  │           │  PROTEIN PORE  │                         │
  │           └────────────────┘                         │
  │  ─────────────────────────────                       │
  │  Lower chamber (−)                                   │
  │                                                      │
  │  Each base in the pore produces a characteristic     │
  │  electrical signal (picoampere level)                │
  │  Neural network (Dorado) converts signal → sequence  │
  └─────────────────────────────────────────────────────┘

  ADVANTAGES:
  - Real-time output (bases called as sequenced)
  - No theoretical read length limit (record: ~4.2 Mb single read)
  - Detects base modifications directly (5-methylcytosine changes signal)
  - MinION: USB-stick sized, field-deployable, ~$1,000 device
  - PromethION: 48 flow cells, production scale

  DISADVANTAGE:
  - Raw error rate ~5–10% (improving rapidly)
  - Homopolymers (AAAAA) are hard to count precisely
  - Needs high molecular weight input DNA (>10 kb preferred)
```

---

## PacBio HiFi: High Accuracy Long-Read

```
  PACBIO SMRT SEQUENCING
  =======================

  STEP 1: Single molecule in zero-mode waveguide (ZMW)
    - ZMW = tiny well, ~20 nm diameter
    - Single DNA polymerase attached at bottom
    - Each fluorescent base incorporation detected in real-time

  STEP 2: Circular DNA template (SMRTbell)
    - DNA ligated into circular library
    - Polymerase reads same molecule multiple times (passes)

  STEP 3: HiFi = Circular Consensus Sequencing (CCS)
    ┌─────────────────────────────────────────────────┐
    │ Polymerase circles 10-kb molecule ~10–15 times  │
    │ Each pass has ~85% accuracy (raw)               │
    │ Consensus of passes → >99.9% accuracy per base  │
    │ Still gives ~15–25 kb average read length       │
    └─────────────────────────────────────────────────┘

  RESULT: "Best of both worlds" — long reads WITH high accuracy
  Use cases: de novo genome assembly, phasing, structural variant calling
```

---

## Single-Cell Sequencing (10x Genomics Chromium)

```
  10x GENOMICS DROPLET WORKFLOW
  ==============================

  STEP 1: GEL BEAD MICROFLUIDICS
  ┌─────────────────────────────────────────────────┐
  │ Cell suspension flows through microfluidic chip │
  │ Each cell + gel bead encapsulated in oil droplet│
  │ Gel bead carries 10-bp cell barcode + UMI oligos│
  │ Throughput: ~10,000 cells per run               │
  └─────────────────────────────────────────────────┘
              │
              ▼
  STEP 2: REVERSE TRANSCRIPTION IN DROPLET
  ┌─────────────────────────────────────────────────┐
  │ Cell lyses in droplet                           │
  │ mRNA captured by poly-T tail on oligo           │
  │ Reverse transcriptase makes cDNA                │
  │ Each mRNA molecule tagged with:                 │
  │   - Cell barcode (which cell)                   │
  │   - UMI (unique molecular identifier per mRNA)  │
  └─────────────────────────────────────────────────┘
              │
              ▼
  STEP 3: ILLUMINA SEQUENCING
  ┌─────────────────────────────────────────────────┐
  │ Droplets broken; cDNA pooled and amplified      │
  │ Short reads sequenced on standard Illumina      │
  │ Cell barcode identifies which cell each read    │
  │ UMI allows deduplication (remove PCR duplicates)│
  │ Output: sparse matrix: cells × genes            │
  └─────────────────────────────────────────────────┘

  DATA: Gene expression matrix, ~20,000 genes × ~10,000 cells
  Typical sparsity: ~80–90% zeros (most genes not detected per cell)
  Analysis: Seurat (R) or Scanpy (Python) for clustering, UMAP
```

---

## Spatial Transcriptomics

```
  SPATIAL TX CONCEPT
  ==================

  Problem: scRNA-seq destroys tissue architecture
           (cells dissociated before sequencing)

  Solution: Measure gene expression WITH spatial position in tissue

  10x VISIUM (capture-array based):
  ┌─────────────────────────────────────────────────────┐
  │ Tissue section placed on array of ~5,000 spots       │
  │ Each spot has oligos with spatial barcode + poly-T   │
  │ mRNA diffuses down, captured at nearest spot         │
  │ After library prep, Illumina sequencing              │
  │ Result: gene expression at 55 μm spot resolution     │
  └─────────────────────────────────────────────────────┘

  XENIUM / MERFISH (in situ hybridization):
  - Probes for specific genes hybridize in tissue slice
  - Sequential fluorescence imaging reads gene identity
  - Single-cell + single-molecule resolution
  - But limited to pre-defined gene panel (~300–1,000 genes)
```

---

## Technology Comparison

| Attribute | Sanger | Illumina | ONT (PromethION) | PacBio HiFi |
|-----------|--------|----------|------------------|-------------|
| Read length | 600–1,000 bp | 150 bp | 10 kb–4 Mb | 15–25 kb |
| Accuracy | >99.99% | ~99.9% | ~95–98% raw | >99.9% |
| Throughput | ~1 kb/run | ~3.2B reads/run | ~290 Gb/run | ~360 Gb/run |
| Cost/Gb | ~$500 | ~$6–10 | ~$50–100 | ~$10–20 |
| Time to result | 4–8 hr | 1–3 days | Real-time | 1–2 days |
| Detect methylation | No | No (separate assay) | Yes (direct) | Yes (with kinetics) |
| De novo assembly | Poor | Poor (short) | Excellent | Excellent |
| SNP/indel calling | Good | Excellent | Good (with depth) | Excellent |
| Structural variants | No | Poor | Excellent | Excellent |
| Portability | No | No | MinION: Yes | No |

---

## Decision Cheat Sheet

| Goal | Best Technology |
|------|----------------|
| SNPs/small indels, population scale | Illumina WGS or WES |
| Validate a specific variant | Sanger sequencing |
| De novo genome assembly | PacBio HiFi + ONT hybrid |
| Structural variant discovery | ONT or PacBio HiFi |
| Real-time / field sequencing | ONT MinION |
| Detect DNA methylation directly | ONT (direct sequencing) |
| Single-cell transcriptomics | 10x Genomics + Illumina |
| Expression with spatial context | 10x Visium / Xenium |
| Complete telomere-to-telomere assembly | ONT ultra-long + PacBio HiFi |
| RNA sequencing (transcriptomics) | Illumina (mostly) or ONT direct RNA |

---

## Common Confusion Points

**Why paired-end?** Illumina reads from both ends of a fragment (2×150 bp). The fragment is ~400 bp, so you get the outer 150 bp from each end with a ~100 bp gap. This helps with alignment (both ends constrain placement) and detecting structural variants (if paired ends land in unexpected orientations or distances).

**UMIs vs. barcodes in scRNA-seq**: The cell barcode identifies which droplet (= which cell) a read came from. The UMI identifies which individual mRNA molecule produced that read — after PCR amplification, multiple reads with the same UMI are duplicates of the same molecule and should be counted once.

**Coverage vs. read count**: "30x WGS" means 30 reads per base position on average. 100 million reads each 150 bp long = 15 Gb of sequence. Human genome = 3 Gb. So 15 Gb / 3 Gb = 5x coverage — you need ~270 million reads for 30x human WGS.

**ONT error profile**: ONT errors are not random; they cluster at homopolymer runs (stretches of the same base: AAAAAAA is hard to count). This is a systematic error, not just noise, so it cannot be overcome simply by sequencing deeper. Newer models (R10 pore) have improved substantially here.

**Short-read vs. long-read cost comparison**: Illumina is cheaper per base ($6–10/Gb vs. $50–100/Gb for ONT), but for structural variant analysis or de novo assembly, you need far fewer long reads to achieve the same result — the cost comparison depends heavily on the application.
