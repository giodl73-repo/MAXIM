# Genome Assembly

## The Big Picture

```
GENOME ASSEMBLY AS A GRAPH PROBLEM
====================================

  INPUT: Millions of short (or long) reads — fragments of the genome
  OUTPUT: Contiguous sequences (contigs → scaffolds → chromosomes)

  THE CORE CHALLENGE:
  Genome = ~3.2 billion bp
  Short reads = ~150 bp each
  Ratio: 21 million reads to cover at 1x
  With 30x coverage: ~640 million reads

  Assembly is reconstruction from overlapping fragments:
  Like reconstructing a 3-billion-character book from
  640 million randomly-sampled 150-character snippets,
  where some pages repeat verbatim hundreds of times.

  ASSEMBLY APPROACHES:
  ┌─────────────────────────────────────────────────────────────────┐
  │                                                                  │
  │  REFERENCE-GUIDED ASSEMBLY                                       │
  │  ─────────────────────────                                       │
  │  Align reads to existing reference genome                        │
  │  Fast, reliable for known organisms                              │
  │  Cannot find sequences absent from reference                     │
  │  Tools: BWA-MEM2, minimap2                                       │
  │                                                                  │
  │  DE NOVO ASSEMBLY                                                │
  │  ─────────────────                                               │
  │  Build genome from scratch, no reference needed                  │
  │  Harder: must solve the graph problem                            │
  │  Required for: new species, large structural variants            │
  │  Tools: Hifiasm (HiFi), Flye (ONT), SPAdes (Illumina)           │
  └─────────────────────────────────────────────────────────────────┘
```

---

## The Three Assembly Paradigms

### 1. Overlap-Layout-Consensus (OLC) — Conceptual Baseline

```
  OLC PARADIGM (original approach, still used in long-read assemblers)
  =====================================================================

  STEP 1: OVERLAP
  Find all pairs of reads that share a suffix/prefix
  Read A: ATCGATCGATCG
  Read B:       ATCGATCGATTT
  Overlap: ATCGATCG (8 bp shared)

  STEP 2: LAYOUT
  Build overlap graph:
  - Nodes = reads
  - Edges = overlaps above threshold length

  A ──────► B ──────► C ──────► D
         ↘
          E ──────► F

  STEP 3: CONSENSUS
  Walk the graph, call consensus sequence at each position
  Output: contig sequences

  PROBLEM: With millions of reads, all-vs-all overlap is O(n²) — infeasible.
  Solution: de Bruijn graphs (next section) or minimap/MHAP heuristic overlap.
```

### 2. de Bruijn Graph (DBG) — The Dominant Approach for Short Reads

```
  DE BRUIJN GRAPH: THE CS DATA STRUCTURE AT THE HEART OF GENOME ASSEMBLY
  ========================================================================

  KEY IDEA: Decompose reads into k-mers (substrings of length k)
  Build graph: k-mers are edges, (k-1)-mers are nodes

  Example with k=4 (real assemblers use k=21–99):

  Reads: ATCGATCG, TCGATCGT

  All 4-mers from reads:
    ATCG, TCGA, CGAT, GATC, ATCG (duplicate!)
    TCGA (duplicate!), CGAT (duplicate!), GATC, ATCG, TCGT

  Unique (k-1)=3-mers as nodes:
    ATC, TCG, CGA, GAT, TCG, CGT

  Edges (4-mers):
    ATC → TCG  (from ATCG)
    TCG → CGA  (from TCGA)
    CGA → GAT  (from CGAT)
    GAT → ATC  (from GATC)
    TCG → CGT  (from TCGT)

  GRAPH:
         ATCG                ATCG
  ATC ────────► TCG ────────► CGA ────────► GAT
                │
                │ TCGT
                └────────────► CGT

  GENOME RECONSTRUCTION: Follow Eulerian path through graph
  This converts O(n²) all-vs-all comparison to O(n) graph traversal!

  COMPLEXITY REDUCTION:
  OLC approach: O(n²) comparisons
  DBG approach: O(n·k) to build graph + O(n) traversal
  For n=640 million reads, k=31: ~20 billion operations vs ~4×10¹⁷

  WHY IT WORKS: The Eulerian path theorem guarantees a path using
  every edge exactly once when in-degree = out-degree at each node.
  In the genome, every k-mer should appear in a consistent context.

  THE CATCH: REPEATS
  If the genome contains a repeat longer than k:

  Genome: UNIQUE_A──[REPEAT]──UNIQUE_B──[REPEAT]──UNIQUE_C

  The repeat collapses into a single node — ambiguous path.
  Assembler creates a "bubble" or "fork" in the graph.
  Solution: Longer k-mers, paired-end reads, or long reads to span.
```

### 3. Long-Read Assembly (OLC + Graph Simplification)

```
  LONG-READ ASSEMBLY WITH HIFIASM
  =================================

  With PacBio HiFi reads (15–25 kb, >99.9% accuracy):
  - Reads are longer than most repeats
  - Simple overlap-based approach works much better
  - Hifiasm builds a "string graph" (simplified OLC)

  HIFIASM ALGORITHM:
  1. Correct remaining errors via read overlap
  2. Build string graph (reads as nodes, overlaps as edges)
  3. Simplify: trim tips, pop bubbles, remove transitive edges
  4. Walk paths to generate contigs
  5. Phase: separate haplotypes using heterozygous variants

  RESULT QUALITY:
  ┌───────────────────────────────────────────────────┐
  │ SHORT-READ ASSEMBLY (Illumina only)               │
  │   N50 contig: ~50–100 kb                          │
  │   Genome completeness: ~95% (repeats unresolved)  │
  │   Telomeres: missing                               │
  │   Centromeres: missing                             │
  ├───────────────────────────────────────────────────┤
  │ LONG-READ ASSEMBLY (PacBio HiFi)                  │
  │   N50 contig: ~30–100 Mb (chromosome-scale)       │
  │   Genome completeness: >99.5%                     │
  │   Most centromeres: resolved                       │
  ├───────────────────────────────────────────────────┤
  │ TELOMERE-TO-TELOMERE (HiFi + ONT ultra-long)      │
  │   N50 contig: >100 Mb (complete chromosomes)      │
  │   Genome completeness: ~100%                       │
  │   T2T-CHM13 (2022): First complete human genome   │
  └───────────────────────────────────────────────────┘
```

---

## Assembly Quality Metrics

```
  ASSEMBLY QUALITY METRICS
  =========================

  N50: Length of contig such that 50% of the total assembly
       is in contigs of that length or longer.

  Example: Assembly of 100 Mb total with contigs:
    50 Mb, 20 Mb, 15 Mb, 8 Mb, 4 Mb, 2 Mb, 1 Mb...
    Cumulative: 50, 70, 85, 93...
    50% of 100 Mb = 50 Mb → N50 = 50 Mb (the first contig)

  N50 is the key comparator: higher = better assembly continuity.

  OTHER METRICS:
  ┌────────────────────────────────────────────────────────┐
  │ Contig N50          Continuity of assembled sequences  │
  │ Scaffold N50        Continuity including gaps (Ns)     │
  │ % genome assembled  Coverage of reference              │
  │ BUSCO score         Completeness of expected genes     │
  │ QV (quality value)  Per-base accuracy of assembly      │
  │ # assembly errors   Misassemblies vs. reference        │
  └────────────────────────────────────────────────────────┘

  BUSCO (Benchmarking Universal Single-Copy Orthologs):
  - Tests assembly for presence of conserved single-copy genes
  - A high-quality vertebrate genome: >98% BUSCO complete
  - Reports: Complete + Fragmented + Missing + Duplicated
```

---

## Haplotype Phasing

```
  THE PHASING PROBLEM
  ====================

  Human genome is DIPLOID: two copies of each chromosome
  (one maternal, one paternal)

  Naive assembly collapses both haplotypes into one sequence:
  Hap1: A...G...T (maternal)
  Hap2: A...C...T (paternal)
  Collapsed: A...R...T (R = degenerate/ambiguous base)

  WHY PHASING MATTERS:
  - Compound heterozygous disease: two mutations in SAME gene,
    but on DIFFERENT chromosomes → each protein copy is broken
    Only diagnosable with phasing
  - Imprinting: some genes expressed only from maternal OR paternal copy
  - HLA genes: highly variable, precise typing requires phasing

  PHASING APPROACHES:
  ┌─────────────────────────────────────────────────────────┐
  │ TRIO SEQUENCING                                          │
  │ Sequence child + both parents                           │
  │ Mendelian inheritance assigns each variant to a parent  │
  │ Gold standard, expensive                                 │
  ├─────────────────────────────────────────────────────────┤
  │ STATISTICAL PHASING (SHAPEIT4/EAGLE2)                   │
  │ Use linkage disequilibrium patterns from large panels   │
  │ Population-informed but probabilistic                   │
  │ Works for common variants; poor for rare variants       │
  ├─────────────────────────────────────────────────────────┤
  │ HIFIASM PHASING (Hi-C or trio mode)                     │
  │ Long HiFi reads span multiple heterozygous variants     │
  │ Physical linkage on same read → phase blocks            │
  │ Hi-C chromatin proximity data resolves chromosome-scale │
  │ Output: two haplotype-resolved assemblies (haplo1+2)    │
  └─────────────────────────────────────────────────────────┘
```

---

## Telomere-to-Telomere Assembly (T2T)

```
  T2T-CHM13: FIRST COMPLETE HUMAN GENOME (2022)
  ===============================================

  Background: The Human Genome Project (2003) produced a "complete"
  genome, but ~8% was never assembled — centromeres, telomeres,
  and segmental duplications were left as gaps.

  The gap regions are:
  - CENTROMERES: ~1–4 Mb of alpha-satellite repeats, tandem arrays
  - TELOMERES: (TTAGGG)ₙ repeats, ~10–15 kb at chromosome ends
  - SEGMENTAL DUPLICATIONS: >90% identical copies of large segments

  WHY SHORT READS FAIL:
    Alpha-satellite repeat unit: 171 bp
    Illumina read: 150 bp
    Result: Every read maps to multiple locations → unresolvable

  T2T SOLUTION:
    ONT ultra-long reads: up to 1 Mb → spans entire centromere
    PacBio HiFi: high accuracy to distinguish near-identical copies

    ┌──────────────────────────────────────────────────────────┐
    │ CHROMOSOME 8 CENTROMERE EXAMPLE                          │
    │                                                          │
    │ Previous reference: 3 Mb gap of Ns                       │
    │ T2T assembly: 2.8 Mb of perfectly resolved alpha-sat     │
    │ ONT reads that span it: individual reads >2 Mb           │
    │                                                          │
    │ Key biology revealed:                                     │
    │ - 182 previously unknown protein-coding genes found      │
    │ - 99 new copies of medically relevant NOTCH2NL gene      │
    │ - Structural variants completely invisible before         │
    └──────────────────────────────────────────────────────────┘

  PANGENOME REFERENCE (2023 — ongoing):
  - 94 individuals, diverse ancestry → 47 diploid assemblies
  - Each assembly T2T quality → 94 complete haplotype assemblies
  - Graph-based reference: replaces single linear reference
  - Captures population-level structural variation
```

---

## Reference-Guided Alignment (the production path)

For most studies, de novo assembly is not needed. Instead, reads are aligned to the reference genome:

```
  REFERENCE ALIGNMENT PIPELINE
  ==============================

  FASTQ (raw reads)
       │
       ▼ BWA-MEM2 (Illumina) or minimap2 (long reads)
  SAM (text alignments)
       │
       ▼ samtools view -Sb
  BAM (binary SAM, unsorted)
       │
       ▼ samtools sort
  Sorted BAM
       │
       ▼ samtools index
  Sorted BAM + .bai index
       │
       ▼ Picard MarkDuplicates
  Deduped BAM (PCR duplicates flagged)
       │
       ▼ GATK BaseQualityScoreRecalibration (BQSR)
  Recalibrated BAM (ready for variant calling)

  KEY ALIGNMENT CONCEPTS:
  - Primary alignment: Best-scoring alignment for a read
  - Secondary alignment: Alternative alignments (multimappers)
  - Supplementary: Chimeric/split reads (part of long read)
  - MAPQ score: Mapping quality (-10 log₁₀ P(wrong position))
  - MAPQ 0 = multimapper (equally good alignments elsewhere)
  - MAPQ 60 = uniquely mapped, high confidence
```

---

## Decision Cheat Sheet

| Goal | Approach | Tool |
|------|----------|------|
| Map reads to known genome | Reference alignment | BWA-MEM2, minimap2 |
| Assemble novel organism | De novo assembly | Hifiasm (HiFi), Flye (ONT), SPAdes (Illumina) |
| Resolve structural variants | Long-read de novo or SV caller | Sniffles, pbsv, SVABA |
| Get chromosome-scale assembly | HiFi + Hi-C | Hifiasm + 3D-DNA |
| Complete telomere-to-telomere | HiFi + ONT ultra-long | verkko assembler |
| Phase haplotypes | Trio or Hi-C | Hifiasm trio/Hi-C mode |
| Assess assembly quality | BUSCO + N50 + QV | BUSCO, merqury |
| Build pangenome | Multiple T2T assemblies | Minigraph-Cactus |

---

## Common Confusion Points

**Contig vs. scaffold vs. chromosome**: A contig is a contiguous assembled sequence with no gaps. A scaffold is multiple contigs ordered and oriented using long-range information (Hi-C, optical maps, genetic maps) with gaps filled by Ns. A chromosome-scale sequence is a full chromosome, ideally from telomere to telomere.

**Why k-mer size matters in de Bruijn graphs**: Larger k reduces false overlaps between repetitive regions but requires more read depth (longer k-mers are less likely to be seen by chance). Typical assemblers use adaptive k-mers or iterative k-mer sizes (SPAdes). For most human genome assembly, k=31 or k=51 is standard for Illumina.

**N50 is not the whole story**: A high N50 says sequences are long, but not that they're correct. An assembler could produce one 3 Gb contig with massive misassemblies and have N50 = 3 Gb. BUSCO, QV (quality value), and alignment to known reference are needed to assess accuracy alongside N50.

**Why repeats are the central problem**: ~45% of the human genome is repetitive (transposable elements, satellite repeats, segmental duplications). Any repeat longer than your read length creates an ambiguous branch in the assembly graph. Long reads essentially solve this — a 25 kb read can span almost all transposable elements (most <10 kb). Centromeres (Mb-scale satellite repeats) still require ultra-long ONT.
