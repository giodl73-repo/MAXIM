# Bioinformatics Pipelines and File Formats

## The Big Picture

```
BIOINFORMATICS AS SOFTWARE ENGINEERING
========================================

  ANALOGY MAP (your prior art → bioinformatics):
  ┌──────────────────────────────────────────────────────────────────┐
  │ MSBuild / Azure DevOps pipeline  ↔  Snakemake / Nextflow / WDL   │
  │ Azure Data Factory               ↔  Nextflow / Cromwell          │
  │ ETL pipeline stages              ↔  Read QC → Align → Call       │
  │ Structured file formats          ↔  FASTQ / BAM / VCF / BED      │
  │ Schema / OpenAPI spec            ↔  SAM spec / VCF spec (htslib) │
  │ Pipeline checkpointing           ↔  Snakemake --rerun-incomplete │
  │ Distributed compute (ADF)        ↔  Terra / DNAnexus / AWS       │
  │ Data lake / Delta Lake           ↔  Hail / AllOfUs / gnomAD      │
  │ Version control                  ↔  Git + DVC (data version ctrl) │
  └──────────────────────────────────────────────────────────────────┘

  THE STANDARD GERMLINE WGS PIPELINE:
  ┌────────────────────────────────────────────────────────────────┐
  │  FASTQ (raw)                                                   │
  │     │ QC: FastQC, MultiQC                                      │
  │     │ Trim: Trimmomatic / fastp (optional)                     │
  │     ▼                                                          │
  │  Alignment: BWA-MEM2 → SAM                                     │
  │     │ Convert + sort: samtools sort → BAM                      │
  │     │ Index: samtools index → BAM.bai                          │
  │     ▼                                                          │
  │  Mark duplicates: Picard MarkDuplicates → deduped BAM          │
  │     ▼                                                          │
  │  BQSR: GATK BaseRecalibrator + ApplyBQSR → recal BAM           │
  │     ▼                                                          │
  │  Variant calling: GATK HaplotypeCaller → GVCF                  │
  │     │ Joint genotyping: GenomicsDBImport + GenotypeGVCFs       │
  │     ▼                                                          │
  │  VQSR → Filtered VCF                                           │
  │     │ Annotation: VEP / ANNOVAR                                │
  │     ▼                                                          │
  │  Results: Annotated VCF + TSV reports                          │
  └────────────────────────────────────────────────────────────────┘
```

---

## File Formats: The Data Contracts

### FASTQ

```
  FASTQ FORMAT (raw sequencing reads)
  =====================================

  Four lines per read:

  @SEQ_ID_FLOWCELL_LANE_TILE_X_Y 1:N:0:BARCODE    ← Read ID
  ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG  ← Sequence
  +                                                   ← Separator
  FFFFFFFFFFFFFFFF:FFFF,FFFFFFFFFFF:FFFFF:FFFFF:F    ← Quality (ASCII)

  QUALITY ENCODING (Phred+33 ASCII):
  ASCII char → integer → quality score Q
  '!' = 0 = Q0 (P_error = 1.0)    worst
  '+' = 10 = Q10 (P_error = 0.1)
  '5' = 20 = Q20 (P_error = 0.01)
  'F' = 37 = Q37 (P_error = 2×10⁻⁴)
  'I' = 40 = Q40 (P_error = 10⁻⁴)  best

  Q = -10 × log₁₀(P_error)

  PAIRED-END FILES:
  Sample1_R1.fastq.gz   → Read 1 (forward)
  Sample1_R2.fastq.gz   → Read 2 (reverse complement)
  Files are paired: read i in R1 corresponds to read i in R2

  TYPICAL SIZE: ~30 GB compressed per 30x WGS sample
  COMPRESSION: .gz (gzip), .bz2, or .zst
  Streaming decompression → most tools don't need full decompress
```

### SAM/BAM/CRAM

```
  SAM FORMAT (Sequence Alignment/Map)
  =====================================

  HEADER (@SQ, @RG, @HD):
  @HD  VN:1.6  SO:coordinate    ← format version, sort order
  @SQ  SN:chr1  LN:248956422    ← reference sequence + length
  @RG  ID:sample1  SM:samplename PL:ILLUMINA LB:lib1

  ALIGNMENT RECORD (11 mandatory fields):
  ┌────────────────────────────────────────────────────────────────┐
  │ Col  Field    Example       Description                        │
  │ 1    QNAME    read123       Read ID                            │
  │ 2    FLAG     83            Bitwise flags (see below)          │
  │ 3    RNAME    chr1          Reference chromosome               │
  │ 4    POS      1000000       1-based leftmost position          │
  │ 5    MAPQ     60            Mapping quality                    │
  │ 6    CIGAR    100M          Alignment description              │
  │ 7    RNEXT    =             Mate's chromosome (= means same)   │
  │ 8    PNEXT    1000300       Mate's position                    │
  │ 9    TLEN     400           Template length                    │
  │ 10   SEQ      ATCGATCG...   Read sequence                      │
  │ 11   QUAL     FFFFF:F...    Base quality scores                │
  └────────────────────────────────────────────────────────────────┘

  FLAG FIELD (bitwise): Common values
  1    = read paired
  2    = read properly paired
  4    = read unmapped
  8    = mate unmapped
  16   = read reverse strand
  256  = not primary alignment
  1024 = PCR duplicate (Picard-marked)
  2048 = supplementary (chimeric) alignment

  CIGAR OPERATIONS:
  M  = alignment match (can be mismatch)
  I  = insertion in read vs. reference
  D  = deletion in read vs. reference
  N  = skip (intron in RNA-seq)
  S  = soft clip (unmapped at ends)
  H  = hard clip (trimmed, not in SEQ field)
  Example: 50M10I40M = 50 match, 10-bp insertion, 40 match

  FORMATS:
  SAM: text, human-readable, large (NEVER store long-term)
  BAM: binary compressed SAM, indexed with .bai
  CRAM: reference-compressed BAM, ~3x smaller, needs reference to decode
```

### VCF

```
  VCF FORMAT (Variant Call Format)
  ==================================

  HEADER (lines starting with ##):
  ##fileformat=VCFv4.3
  ##reference=GRCh38
  ##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency">
  ##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
  ##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">
  #CHROM POS ID REF ALT QUAL FILTER INFO FORMAT SAMPLE1 SAMPLE2

  DATA RECORDS:
  chr1  1000000  rs12345  A  G  100  PASS  AF=0.05;DP=45  GT:GQ:DP  0/1:99:45  0/0:99:50

  FIELD DEFINITIONS:
  ┌────────────────────────────────────────────────────────────────┐
  │ CHROM  Chromosome                                              │
  │ POS    1-based position                                        │
  │ ID     dbSNP ID or '.'                                         │
  │ REF    Reference allele (from reference genome)                │
  │ ALT    Alternate allele(s), comma-separated if multiple        │
  │ QUAL   Phred-scaled genotype quality (-10 log₁₀ P(wrong))      │
  │ FILTER PASS or filter names that the variant failed            │
  │ INFO   Key=value pairs: AF, DP, SOR, QD, etc.                │
  │ FORMAT Per-sample format field definition                      │
  │ SAMPLE Per-sample values: 0/1:99:45                            │
  └────────────────────────────────────────────────────────────────┘

  GENOTYPE ENCODING:
  0/0 = homozygous reference
  0/1 = heterozygous (one alt allele)
  1/1 = homozygous alternate
  0|1 = phased heterozygous (| = phased, / = unphased)
  ./.  = missing

  GVCF (genomic VCF):
  ─ Per-sample file from GATK HaplotypeCaller
  ─ Contains: all variant sites + non-variant blocks
  ─ Non-variant blocks: <NON_REF> pseudo-allele
  ─ Purpose: enables joint calling without reprocessing all BAMs

  COMMON INFO ANNOTATIONS:
  DP = total depth at site
  AF = allele frequency in cohort
  QD = quality by depth (QUAL/DP) — filter signal quality
  FS = Fisher strand bias — directional sequencing error signal
  SOR = strand odds ratio — strand bias
  MQ = mapping quality of aligned reads
```

### BED, GTF, and Others

```
  OTHER KEY FORMATS
  ==================

  BED (Browser Extensible Data) — genomic intervals:
  chr1  1000  2000  geneName  0  +
  [chrom] [start] [end] [name] [score] [strand]
  ZERO-BASED, HALF-OPEN: start=0 means first base
  BED12: 12 fields (gene structure, exons within block)
  Use: Regulatory regions, peak files, gene boundaries

  GTF/GFF — gene annotation:
  chr1  HAVANA  gene  11869  14409  .  +  .  gene_id "ENSG00000223972"
  [seqname] [source] [feature] [start] [end] [score] [strand] [frame] [attributes]
  ONE-BASED, INCLUSIVE: start=1 means first base
  GTF2 / GFF3: slightly different attribute syntax
  Use: STAR alignment annotation; count matrices from featureCounts

  BIGWIG — quantitative signal track:
  Binary indexed format for continuous values (e.g., coverage, ChIP signal)
  Efficient random access to any region
  Tools: deeptools (bamCoverage → bigwig); UCSC liftover

  IMPORTANT COORDINATE TRAP:
  ┌──────────────────────────────────────────────────────┐
  │ BED: 0-based, half-open  [0, end)                    │
  │ VCF: 1-based, inclusive  position = 1-based          │
  │ GTF: 1-based, inclusive                              │
  │ SAM/BAM: 1-based, inclusive (POS field)              │
  │                                                      │
  │ Converting between formats? Off-by-one errors lurk.  │
  │ chr1:1000-2000 in BED = chr1:1001-2000 in VCF/GTF    │
  └──────────────────────────────────────────────────────┘
```

---

## Workflow Systems

### Snakemake

```
  SNAKEMAKE: PYTHON-BASED WORKFLOW SYSTEM
  =========================================

  CONCEPT: Like GNU Make but with Python and bioinformatics awareness
  EXECUTION MODEL: Reverse dependency resolution (like Make)
    1. Define desired outputs
    2. Snakemake finds rules to generate them
    3. Infers execution order from file dependencies
    4. Only re-runs if input is newer than output (checkpointing)

  SYNTAX:

  rule bwa_align:
      input:
          reads1 = "data/{sample}_R1.fastq.gz",
          reads2 = "data/{sample}_R2.fastq.gz",
          ref = "reference/GRCh38.fa"
      output:
          bam = "aligned/{sample}.sorted.bam",
          bai = "aligned/{sample}.sorted.bam.bai"
      threads: 16
      shell:
          """
          bwa-mem2 mem -t {threads} {input.ref} \
              {input.reads1} {input.reads2} | \
          samtools sort -@ {threads} -o {output.bam}
          samtools index {output.bam}
          """

  RUNNING:
  snakemake --cores 64 --snakefile Snakefile results/sample1.vcf

  EXECUTION BACKENDS:
  ─ Local (--cores N)
  ─ SLURM (--cluster "sbatch --mem {resources.mem} -c {threads}")
  ─ Google Cloud (--google-lifesciences)
  ─ Azure Batch (via azure executor plugin)
```

### Nextflow

```
  NEXTFLOW: DATAFLOW-BASED WORKFLOW
  ===================================

  CONCEPT: DSL built on Groovy; processes are functions; channels = data streams
  Used by: nf-core (community-curated pipelines); Terra; cloud-native

  KEY DIFFERENCES FROM SNAKEMAKE:
  Nextflow uses channels (streams) not files as primary data model
  Better for dynamic pipelines (scatter-gather, conditional)
  Better cloud-native (AWS Batch, Azure Batch, GCP LS natively)
  nf-core provides production-ready standard pipelines

  EXAMPLE (Nextflow DSL2):
  process bwa_mem {
      input:
          tuple val(sample), path(reads)
          path reference
      output:
          tuple val(sample), path("*.bam")

      script:
      """
      bwa-mem2 mem -t ${task.cpus} ${reference} ${reads} | \
      samtools sort -o ${sample}.bam
      """
  }

  workflow {
      reads_ch = Channel.fromFilePairs("data/*_R{1,2}.fastq.gz")
      ref_ch = file("reference/GRCh38.fa")
      bwa_mem(reads_ch, ref_ch)
  }

  NF-CORE STANDARD PIPELINES:
  nf-core/sarek:     WGS variant calling (germline + somatic)
  nf-core/rnaseq:    RNA-seq (alignment + quantification)
  nf-core/chipseq:   ChIP-seq (alignment + peak calling)
  nf-core/atacseq:   ATAC-seq
  nf-core/methylseq: WGBS (bisulfite sequencing)
```

### WDL / Cromwell

```
  WDL (WORKFLOW DESCRIPTION LANGUAGE) + CROMWELL
  ================================================

  WDL: Broadinstitute's language for GATK Best Practices
  Cromwell: execution engine for WDL
  Used on: Terra (Broad Institute cloud), DNAnexus, Azure

  WDL STRUCTURE:
  version 1.0

  task HaplotypeCaller {
      input {
          File input_bam
          File input_bam_index
          File ref_fasta
          String sample_name
      }
      command <<<
          gatk HaplotypeCaller \
              -I ~{input_bam} \
              -R ~{ref_fasta} \
              -O ~{sample_name}.g.vcf.gz \
              -ERC GVCF
      >>>
      output {
          File output_gvcf = "~{sample_name}.g.vcf.gz"
      }
      runtime {
          memory: "16 GB"
          cpu: 4
          docker: "broadinstitute/gatk:4.5.0.0"
      }
  }

  TERRA PLATFORM (Broad/NHGRI):
  ─ Google Cloud-based genomics workspace
  ─ WDL/Cromwell execution engine
  ─ Integrated with data from dbGaP, AnVIL, gnomAD
  ─ All of Us Researcher Workbench uses similar infrastructure
```

---

## Reference Databases

```
  KEY GENOMICS DATABASES
  =======================

  SEQUENCE REFERENCES:
  ┌───────────────────────────────────────────────────────────────┐
  │ GRCh38 (hg38)      Human reference genome, current (2013)     │
  │ T2T-CHM13 (2022)   First complete human genome                │
  │ GRCm39             Mouse reference genome                     │
  │ Source: NCBI RefSeq, UCSC Genome Browser, Ensembl             │
  └───────────────────────────────────────────────────────────────┘

  VARIANT DATABASES:
  ┌───────────────────────────────────────────────────────────────┐
  │ dbSNP (NCBI)        All submitted SNPs + rsIDs                │
  │ ClinVar (NCBI)      Clinical variant interpretations          │
  │ gnomAD              Population frequencies, constraint        │
  │ COSMIC              Somatic cancer mutations                  │
  │ ClinGen             Gene-disease validity curation            │
  │ PharmGKB            Pharmacogenomics variant-drug pairs       │
  └───────────────────────────────────────────────────────────────┘

  GENE ANNOTATION:
  ┌───────────────────────────────────────────────────────────────┐
  │ Ensembl             Gene models (GENCODE annotation set)      │
  │ RefSeq (NCBI)       Curated transcripts and proteins          │
  │ UCSC Genome Browser  Visual browser + annotation tracks       │
  │ OMIM                Online Mendelian Inheritance in Man       │
  │ GTEx                Tissue-specific gene expression + eQTLs   │
  └───────────────────────────────────────────────────────────────┘

  PROTEIN/PATHWAY:
  ┌───────────────────────────────────────────────────────────────┐
  │ UniProt             Protein sequences + function              │
  │ Reactome            Human pathway hierarchy                   │
  │ STRING              Protein-protein interaction network       │
  │ AlphaFold DB        Predicted 3D structures for ~200M proteins │
  └───────────────────────────────────────────────────────────────┘
```

---

## Cloud Genomics Platforms

```
  CLOUD GENOMICS: AZURE AND BEYOND
  ==================================

  MICROSOFT GENOMICS (Azure):
  ─ Managed BWA-MEM + GATK service on Azure
  ─ API-driven: submit FASTQ → get BAM/VCF back
  ─ Integrated with Azure Blob Storage
  ─ PARABRICKS (GPU-accelerated GATK): 30x genome in ~20 min
    on 8× A100 GPUs (vs. ~24 hr on 32 CPUs)

  TERRA (Broad Institute):
  ─ Google Cloud Compute, uses GCS for storage
  ─ WDL/Cromwell execution engine
  ─ Integrated data access: dbGaP, AnVIL, UK Biobank
  ─ Shared analysis environment: workspaces (like Azure DevOps boards)

  DNANEXUS:
  ─ AWS and Azure execution
  ─ Used by: UK Biobank Research Access Platform
  ─ DNAnexus apps = containerized tools (like Azure Container Apps)

  AWS HEALTHOMICS:
  ─ Managed genomics workflows (AWS Batch + WDL/Nextflow)
  ─ HealthOmics storage: purpose-built for genomics data
  ─ Sequence store, variant store, annotation store

  COST STRUCTURE (approximate):
  30x WGS alignment (BWA-MEM2 + GATK): ~$5–15/sample (cloud)
  1,000 genome cohort: ~$5,000–15,000 compute
  Storage: $0.02–0.03/GB/month (cool tier) = ~$1.50/WGS BAM/month
```

---

## QC Metrics

```
  STANDARD QC CHECKPOINTS
  =========================

  SEQUENCING QUALITY (FastQC / MultiQC):
  ─ Per-base quality scores (should be Q30+ in middle)
  ─ GC content (should match genome composition ~42%)
  ─ Adapter content (should be near 0 after trimming)
  ─ Duplication rate (acceptable: 20–40% for WGS at 30x)

  ALIGNMENT QC (samtools flagstat / Picard CollectWgsMetrics):
  ─ Alignment rate: >95% properly paired reads mapped
  ─ Mean coverage: target 30x for WGS (±20% acceptable)
  ─ % bases ≥Q20: >90%
  ─ Coverage uniformity: should be relatively flat (no dropouts)
  ─ Insert size distribution: peak at ~350–450 bp for WGS

  VARIANT CALLING QC:
  ─ Transition/Transversion ratio (Ti/Tv):
    WGS: ~2.1 (expected from biology)
    Exome: ~3.0 (more functional variation selected)
    If Ti/Tv << expected: batch artifact, contamination, or errors
  ─ Novel variant rate: >90% of SNPs should be in dbSNP
  ─ Het/hom ratio: ~1.5–2.0 for typical human genome

  RNA-SEQ QC:
  ─ Mapping rate to transcriptome: >80%
  ─ Ribosomal RNA contamination: <5%
  ─ % exonic reads: >60% (RNA-seq should be in exons)
  ─ 5'/3' bias: even coverage across transcript length
  ─ Strandedness: matches library prep protocol
  ─ Genes detected (>10 counts): >15,000 for good quality
```

---

## Decision Cheat Sheet

| Need | Tool |
|------|------|
| Align Illumina reads to reference | BWA-MEM2 (DNA) or STAR (RNA) |
| Align long reads | minimap2 (both ONT and PacBio) |
| Mark PCR duplicates | Picard MarkDuplicates or samtools markdup |
| Convert/sort/index SAM/BAM | samtools view, sort, index |
| QC raw reads | FastQC + MultiQC |
| QC aligned data | Picard CollectWgsMetrics / CollectRnaSeqMetrics |
| Run GATK pipeline | nf-core/sarek or GATK Best Practices WDL |
| Workflow orchestration (local/HPC) | Snakemake |
| Workflow orchestration (cloud) | Nextflow + nf-core |
| Cloud execution on Terra | WDL + Cromwell |
| Cloud GPU acceleration | NVIDIA Parabricks (GATK on GPU) |
| Intersect genomic intervals | bedtools intersect |
| Create coverage tracks | deeptools bamCoverage |
| Visualize alignments | IGV (Integrative Genomics Viewer) |

---

## Common Confusion Points

**BAM vs. CRAM**: BAM is ~50 GB for a 30x WGS. CRAM stores only the differences from the reference and is ~15 GB — a 3x saving. CRAM requires the original reference genome to decode. For long-term archival, CRAM is preferred. For active analysis, either works; many tools now handle CRAM natively.

**0-based vs. 1-based coordinates**: BED files are 0-based half-open (the first base of the chromosome is position 0, and intervals are [start, end) — end is not included). VCF and GTF are 1-based inclusive. Converting between them: BED position 1000 = VCF position 1001. This is one of the most common sources of off-by-one bugs in bioinformatics.

**FASTQ quality encoding history**: Early Illumina data (pre-1.8) used Phred+64 encoding; modern data (1.8+) uses Phred+33. If quality characters look like uppercase letters (I, J, K) and values seem anomalously high, you may have a Phred+64 file being treated as Phred+33. FastQC detects this.

**WDL vs. Nextflow vs. Snakemake**: All three solve the same DAG scheduling problem. Snakemake is best for local/HPC with Python familiarity (like Make). Nextflow is best for cloud-native execution and dynamic pipelines. WDL is used specifically for GATK Best Practices on Terra/Cromwell. The nf-core project has become the de facto standard for community-curated pipelines.
