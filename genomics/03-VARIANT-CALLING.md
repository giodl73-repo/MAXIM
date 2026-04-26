# Variant Calling and Population Genomics

## The Big Picture

```
VARIANT CALLING: FINDING WHAT DIFFERS FROM REFERENCE
======================================================

  GENOME = reference sequence (GRCh38, 3.2 Gb)
  YOUR GENOME = ~3–4 million positions where you differ

  VARIANT CLASSES BY SIZE:
  ┌──────────────────────────────────────────────────────────────────┐
  │ SNP   Single Nucleotide Polymorphism  1 bp substitution          │
  │       REF: A  ALT: G  (most common, ~3 million per genome)       │
  │                                                                  │
  │ Indel INsertion/DELetion              1–50 bp                    │
  │       REF: ATCG  ALT: ATC (deletion of G)                        │
  │       Frameshift if in coding region                             │
  │                                                                  │
  │ CNV   Copy Number Variant             1–10 Mb                    │
  │       Extra or missing copies of large genomic segments          │
  │       ~1,000 CNVs per genome vs. reference                       │
  │                                                                  │
  │ SV    Structural Variant              50 bp–Mb                   │
  │       Inversions, translocations, large insertions/deletions     │
  │       ~1,000–10,000 SVs per genome vs. reference                 │
  │                                                                  │
  │ Tandem Repeat Variation (STR/VNTR)                               │
  │       Variation in repeat copy number                            │
  │       Medical: HTT (Huntington's), FMR1 (fragile X)              │
  └──────────────────────────────────────────────────────────────────┘

  SIGNAL DETECTION FRAMING:
  Variant calling is fundamentally a signal detection problem.
  True variant signal competes with sequencing errors (~0.1% per base).
  At 30x coverage, a heterozygous variant appears in ~15 reads.
  A sequencing error at any position appears in ~0.03 reads.
  Statistical test: Is this above the noise floor?
```

---

## GATK HaplotypeCaller Pipeline

The Genome Analysis Toolkit (GATK) from the Broad Institute is the field standard for germline variant calling.

```
  GATK BEST PRACTICES PIPELINE
  ==============================

  INPUT: Sorted, deduplicated, BQSR-recalibrated BAM

  STEP 1: HAPLOTYPECALLER — LOCAL REASSEMBLY
  ┌─────────────────────────────────────────────────────────┐
  │ For each genomic region with evidence of variation:     │
  │ 1. Collect all reads overlapping the region             │
  │ 2. REASSEMBLE reads using local de Bruijn graph         │
  │    (avoids reference bias from alignment)               │
  │ 3. Identify all candidate haplotypes in graph           │
  │ 4. Score each read against each candidate haplotype     │
  │    using pair-HMM (Hidden Markov Model)                 │
  │ 5. Bayesian genotyping: P(G|D) for each genotype G      │
  └─────────────────────────────────────────────────────────┘

  THE HMM IN HAPLOTYPECALLER:
  ─────────────────────────────
  Models three processes simultaneously:
    - Read bases matching the haplotype (match state M)
    - Insertions in the read vs. haplotype (insert state I)
    - Deletions in the read vs. haplotype (delete state D)

  Output per site: genotype likelihoods GL(0/0), GL(0/1), GL(1/1)
  Log-scaled: PL = -10 log₁₀(GL) in GVCF format

  STEP 2: GVCF MODE (per-sample)
  ┌─────────────────────────────────────────────────────────┐
  │ Output: .g.vcf file with:                               │
  │   - All variant sites with likelihoods                  │
  │   - Non-variant sites with confidence of REF call       │
  │ Purpose: Enables joint calling across many samples      │
  │          without reprocessing all BAMs together         │
  └─────────────────────────────────────────────────────────┘

  STEP 3: GENOTYPEGVCFS (joint calling)
  ┌─────────────────────────────────────────────────────────┐
  │ Combine N sample GVCFs                                  │
  │ Call genotypes jointly (uses all samples to calibrate)  │
  │ Captures rare variants detectable only by seeing allele │
  │ in the full cohort context                              │
  └─────────────────────────────────────────────────────────┘

  STEP 4: VARIANT QUALITY SCORE RECALIBRATION (VQSR)
  ┌─────────────────────────────────────────────────────────┐
  │ Problem: Single quality threshold → poor precision/recall│
  │ Solution: Train Gaussian mixture model on known variants │
  │ Training data: HapMap, 1000G, dbSNP (known true positives)│
  │ Features: QD, MQ, FS, SOR, MQRankSum, ReadPosRankSum    │
  │ Output: VQSLOD score + PASS/FILTER labels               │
  │ For small cohorts (<30 samples): use CNN-based scoring  │
  └─────────────────────────────────────────────────────────┘
```

---

## Variant Types in Detail

### SNPs and Indels

```
  SNP CLASSIFICATION BY FUNCTIONAL IMPACT
  =========================================

  CODING VARIANTS:
  - Synonymous (silent): AGC → AGT, both = Serine. No AA change.
  - Missense: changes amino acid (CAG → CAA, Gln → Gln is synonymous;
              but CAG → GAG is Gln → Glu — missense)
  - Nonsense: creates stop codon (CAG → TAG, Gln → STOP)
  - Frameshift: indel not divisible by 3 → all downstream AAs wrong

  SPLICING VARIANTS:
  - Affect canonical splice sites (GT...AG at intron boundaries)
  - Can cause exon skipping or intron retention

  REGULATORY VARIANTS:
  - Promoter, enhancer, UTR regions
  - Affect when/where gene is expressed, not protein sequence
  - Examples: eQTLs (expression QTLs) detected by GWAS

  VARIANT ANNOTATION TOOLS:
  ┌───────────────────────────────────────────────────────────┐
  │ VEP (Variant Effect Predictor, Ensembl)                   │
  │   - Maps variants to transcripts                          │
  │   - Predicts functional consequence                       │
  │   - SIFT/PolyPhen scores for missense                     │
  │                                                           │
  │ ANNOVAR                                                   │
  │   - Gene-based, region-based, filter-based annotation     │
  │   - Links to ClinVar, dbSNP, gnomAD frequencies           │
  │                                                           │
  │ SnpEff                                                    │
  │   - Fast Java tool for variant annotation                 │
  │   - Common in cancer genomics pipelines                   │
  └───────────────────────────────────────────────────────────┘
```

### Structural Variants

```
  STRUCTURAL VARIANT TYPES
  =========================

  ┌─────────────────────────────────────────────────────────────────┐
  │                                                                 │
  │  DELETION:        ──[A]──[B]──[C]──  →  ──[A]──[C]──            │
  │                         ↑ [B] removed                           │
  │                                                                 │
  │  INSERTION:       ──[A]──[B]──  →  ──[A]──[NEW]──[B]──          │
  │                                                                 │
  │  INVERSION:       ──[A]──[B]──[C]──  →  ──[A]──[B']──[C]──    │
  │                         ↑ [B] reversed                          │
  │                                                                 │
  │  DUPLICATION:     ──[A]──[B]──  →  ──[A]──[B]──[B]──[B]──     │
  │  (tandem)                ↑ [B] copied                           │
  │                                                                 │
  │  TRANSLOCATION:   Segment moves to different chromosome         │
  │                   der(22;9) Philadelphia chromosome in CML      │
  │                                                                 │
  │  MOBILE ELEMENT:  Transposable element inserts at new location  │
  │                   (LINE-1 / Alu retrotransposition)             │
  └─────────────────────────────────────────────────────────────────┘

  SV DETECTION BY READ EVIDENCE:
  Split reads: Single read aligns to two locations → breakpoint
  Discordant pairs: Paired reads too far apart, wrong orientation
  Read depth: Fewer reads in deleted region; more in duplicated
  Long reads: Directly span breakpoints → gold standard

  TOOLS: Sniffles2 (ONT long-read), PBSV (PacBio), DELLY, Manta (Illumina)
```

---

## Population Genomics

### 1000 Genomes and gnomAD

```
  POPULATION REFERENCE DATABASES
  ================================

  1000 GENOMES PROJECT (2008–2015, now expanded):
  - 2,504 individuals from 26 populations
  - Low-coverage WGS (~7x) + exome
  - Goal: Catalog all common variants (MAF >1%)
  - Data: ~88 million SNPs, ~3.6 million indels

  gnomAD v4.1 (Genome Aggregation Database):
  - 730,947 exomes + 76,215 genomes
  - 14 ancestral populations (diverse)
  - Use: Filter likely benign variants (if in 1,000 people, not rare disease)
  - Key metric: allele frequency (AF) per population
  - AF >1% = common variant (likely benign for Mendelian disease)
  - AF <0.01% = ultra-rare (high prior for pathogenicity)

  gnomAD constraint metrics:
  ┌─────────────────────────────────────────────────────────┐
  │ pLI (probability of LoF intolerance): 0–1               │
  │   pLI > 0.9 = gene likely lethal to lose one copy       │
  │   Used for: assessing deleteriousness of LoF variants   │
  │                                                         │
  │ Z-score (missense constraint): negative = constrained   │
  │   High Z = gene under strong purifying selection        │
  └─────────────────────────────────────────────────────────┘
```

### Linkage Disequilibrium

```
  LINKAGE DISEQUILIBRIUM (LD): THE CORRELATION STRUCTURE OF VARIANTS
  ===================================================================

  DEFINITION: Two variants in LD if they co-occur more often
  than expected by random assortment.

  WHY IT OCCURS:
  - Physical proximity on chromosome → transmitted together
  - Unless recombination separates them over generations

  MEASUREMENT: r² or D'
  r² = 1.0: Perfect LD — knowing one allele perfectly predicts other
  r² = 0.0: Complete LD absence — independent

  LD BLOCKS:
  Genome is divided into ~100,000 LD blocks
  Within a block: ~5–15 kb, variants highly correlated
  Between blocks: recombination hotspots break correlation

  PRACTICAL IMPLICATION FOR GWAS:
  You don't need to genotype every SNP.
  If you type a "tag SNP" with high LD to a nearby variant,
  you implicitly type all nearby correlated variants.
  HapMap/1000G provide LD information for tag SNP selection.

  HAPLOTYPE BLOCKS:
  ──[SNP1]──[SNP2]──[SNP3]──|──[SNP4]──[SNP5]──
  │<──── LD Block 1 ────>│  │<── Block 2 ──>│
    All in LD (r²>0.8)         All in LD
    Tagged by one SNP          Tagged by one SNP
```

---

## Variant Interpretation: ACMG Framework

```
  ACMG/AMP VARIANT CLASSIFICATION (5 tiers)
  ==========================================

  PATHOGENIC (P)
  ─ Strong evidence: known disease variant in ClinVar
  ─ Population: absent from gnomAD
  ─ Functional: null variant in dominant LoF disease gene

  LIKELY PATHOGENIC (LP)
  ─ Strong evidence but not confirmed
  ─ Co-segregation with disease in family

  VARIANT OF UNCERTAIN SIGNIFICANCE (VUS)
  ─ The most common and challenging category
  ─ Not enough evidence to classify
  ─ ~30–50% of clinical exome reports include VUS

  LIKELY BENIGN (LB)
  ─ Common in population, no functional evidence of harm

  BENIGN (B)
  ─ High allele frequency in gnomAD; known benign variant

  CRITERIA (summarized):
  ┌────────────────────────────────────────────────────────┐
  │ PVS1: Null variant in LoF-intolerant gene              │
  │ PS1–4: Pathogenic evidence (frequency/functional/etc)  │
  │ PM1–6: Moderate pathogenic evidence                    │
  │ PP1–5: Supporting pathogenic evidence                  │
  │ BA1: AF >5% in gnomAD → Benign standalone            │
  │ BS1–4: Strong benign evidence                          │
  │ BP1–7: Supporting benign evidence                      │
  └────────────────────────────────────────────────────────┘

  DATABASES:
  ClinVar: Variant-disease classifications (public)
  HGMD: Human Gene Mutation Database (paid, comprehensive)
  ClinGen: Gene curation + variant interpretation guidance
  OMIM: Online Mendelian Inheritance in Man
```

---

## Cancer Variant Calling (Somatic)

```
  GERMLINE vs. SOMATIC VARIANT CALLING
  ======================================

  GERMLINE (constitutional):
  - Present in all cells of the body
  - Inherited or de novo mutation
  - Every cell has 2 copies (diploid)
  - Expected VAF at heterozygous site: ~50%
  - Called by: GATK HaplotypeCaller

  SOMATIC (cancer-specific):
  - Mutation acquired during tumor development
  - Present in fraction of tumor cells (subclonal architecture)
  - Normal cells in tumor biopsy dilute the signal
  - Expected VAF: can be 5–50% depending on tumor purity
  - Called by: Mutect2 (tumor-normal paired)

  TUMOR-NORMAL PAIRED ANALYSIS:
  ┌─────────────────────────────────────────────────────────┐
  │ Normal sample: establishes germline background          │
  │ Tumor sample:  contains somatic mutations               │
  │                                                         │
  │ Mutect2 model:                                          │
  │ P(somatic | reads in tumor, reads in normal)            │
  │ Filters: panel of normals (PoN), germline AF filter     │
  │                                                         │
  │ Tumor Mutational Burden (TMB):                          │
  │ # somatic mutations per Mb of genome                    │
  │ Low: <5/Mb (most cancers)                               │
  │ High: >10/Mb (mismatch repair deficient, good IO rx)    │
  └─────────────────────────────────────────────────────────┘

  SOMATIC SIGNATURES (COSMIC):
  Different mutational processes leave different patterns
  - Signature 1: Age-related C→T at CpG (deamination)
  - Signature 2: APOBEC (C→T in TCx context)
  - Signature 4: Tobacco (C→A transversions)
  - Signature 6: Mismatch repair deficiency
  Pattern decomposition identifies etiology of mutations
```

---

## Decision Cheat Sheet

| Goal | Tool/Method |
|------|-------------|
| Call germline SNPs/indels | GATK HaplotypeCaller → VQSR |
| Call somatic variants (cancer) | GATK Mutect2 (tumor-normal) |
| Call structural variants (Illumina) | Manta, DELLY |
| Call structural variants (long-read) | Sniffles2 (ONT), PBSV (PacBio) |
| Call copy number variants | GATK CNV pipeline, CNVkit |
| Annotate variant consequence | VEP (Ensembl), ANNOVAR |
| Filter by population frequency | gnomAD (AF filter, pLI) |
| Classify clinical variants | ACMG/AMP 5-tier framework |
| Large-scale cohort genotyping | GATK joint calling + GenomicsDB |
| Cancer mutational signatures | SigProfilerExtractor (COSMIC) |

---

## Common Confusion Points

**VAF vs. genotype**: Variant allele fraction (VAF) is the fraction of reads supporting the alternate allele. For germline heterozygous variants, VAF should be ~50%. For somatic variants in a tumor, VAF varies with tumor purity and clonal fraction. A VAF of 10% could mean: 20% tumor cells, all carrying the variant.

**Why BQSR matters**: Base quality scores from the sequencer are systematically miscalibrated (context-dependent errors, machine-specific biases). BQSR (Base Quality Score Recalibration) uses known variant sites (dbSNP) as anchors — any apparent "variant" at a known homozygous reference site must be a sequencing error, used to build an empirical error model and correct quality scores.

**VUS abundance**: ~30–50% of clinical exome reports contain at least one VUS. This is not a failure — it reflects the boundary of current knowledge. Many VUS are reclassified over time as evidence accumulates. Returning VUS to patients requires careful communication of uncertainty.

**Multiallelic sites**: At a single position, multiple different ALT alleles can exist in a population (e.g., A→G and A→T at the same site). Standard VCF calling may report these as separate records. Joint calling across large cohorts is essential to handle multiallelic sites correctly — a single-sample pipeline may miss or misclassify the minor allele.
