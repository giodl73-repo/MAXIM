# Genome-Wide Association Studies (GWAS)

## The Big Picture

```
GWAS: CONNECTING VARIANTS TO TRAITS AT POPULATION SCALE
=========================================================

  QUESTION: Which genomic positions are statistically associated
            with a trait (disease, height, drug response, etc.)?

  STUDY DESIGN:
  ┌──────────────────────────────────────────────────────────────┐
  │  CASES: ~5,000–100,000 people WITH the trait                 │
  │  CONTROLS: ~5,000–100,000 people WITHOUT the trait           │
  │                                                              │
  │  Genotype each person at ~500,000–10,000,000 SNPs            │
  │  (via SNP array or imputation to full genome)                │
  │                                                              │
  │  For each SNP:                                               │
  │    Test: Is this allele more common in cases vs. controls?   │
  │    Statistical test: chi-squared or logistic regression      │
  │    Result: odds ratio (OR) + p-value                         │
  └──────────────────────────────────────────────────────────────┘

  SCALE:
  ─ Testing ~5 million variants genome-wide
  ─ Genome-wide significance threshold: p < 5×10⁻⁸
  ─ Why such a stringent threshold? Bonferroni correction:
    0.05 / 1,000,000 tests = 5×10⁻⁸
  ─ At p<5×10⁻⁸, expected false positives ≈ 1 across the genome

  WHAT GWAS FINDS:
  ─ Not causative variants directly (resolution ~100 kb LD block)
  ─ A "tag SNP" in LD with the true causal variant
  ─ Association signal, not mechanism
  ─ Fine-mapping needed to narrow to causal variant
```

---

## Linkage Disequilibrium (LD) and Imputation

```
  LINKAGE DISEQUILIBRIUM REVIEW
  ==============================

  LD = correlation between alleles at different positions
  arising because nearby variants are co-inherited.

  MEASUREMENT: r² statistic
  r² = 1.0: Alleles at two sites always co-occur (perfect LD)
  r² = 0.0: Alleles independent (no LD)

  WHY LD MATTERS FOR GWAS:
  ┌──────────────────────────────────────────────────────────────┐
  │ SNP ARRAY GENOTYPES 500,000 SNPs directly                    │
  │ IMPUTATION PREDICTS the remaining ~5-10 million SNPs         │
  │                                                              │
  │ Method: If SNP A is in LD (r²=0.95) with SNP B,              │
  │   and you know A's genotype, you can PREDICT B's genotype    │
  │   with ~95% accuracy using a reference panel (1000G/TOPMed)  │
  │                                                              │
  │ IMPUTATION PIPELINE:                                         │
  │ 1. Genotype array (500K SNPs) → PLINK format                 │
  │ 2. Pre-phasing: infer haplotypes (EAGLE2, SHAPEIT4)          │
  │ 3. Imputation server (Michigan/TOPMed): match to reference   │
  │ 4. Output: ~20-50 million imputed variants with R² quality   │
  │ 5. Filter: imputation quality R²>0.8 for analysis            │
  └──────────────────────────────────────────────────────────────┘

  HAPLOTYPE BLOCKS AND TAG SNPS:
  ──[SNP1 A/G]──[SNP2 C/T]──[SNP3 T/A]──  LD block
    allele A  → always C  → always T  (haplotype 1)
    allele G  → always T  → always A  (haplotype 2)

  If you genotype only SNP1, you implicitly know SNP2 and SNP3.
  SNP1 = "tag SNP" for this LD block.
```

---

## GWAS Statistical Framework

```
  GWAS REGRESSION MODEL
  ======================

  For each SNP, test:
  logit(P(case)) = β₀ + β₁ × dosage + β₂ × PC1 + ... + β₁₀ × PC10 + covariates

  dosage = 0, 1, or 2 (copies of minor allele) — additive model
  PCk = k-th principal component of the genotype matrix (ancestry control)
  covariates: age, sex, batch, first principal components

  β₁ = log(odds ratio) for each copy of minor allele
  e^β₁ = OR (odds ratio)
  p-value on β₁: is this association significant?

  MANHATTAN PLOT:
  x-axis: genomic position (chromosome 1–22, X)
  y-axis: -log10(p-value)
  Horizontal line: genome-wide significance threshold (-log10(5×10⁻⁸) = 7.3)

        chr1       chr2  ...  chr22
  8 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  GW threshold
  6 │                *                        *
  4 │      **      ***   *    *   *  *     *
  2 │  *** *** ** *****  ** ***** ***  ** ***
  0 └────────────────────────────────────────────────►

  PEAKS ("hits") = associated loci
  Each peak = a genomic region (LD block) associated with trait
```

### Population Stratification

```
  POPULATION STRATIFICATION: THE MAIN CONFOUNDER
  ================================================

  PROBLEM: Different ancestries have:
  1. Different allele frequencies (many variants differ)
  2. Different disease rates (due to environment, other genetics)

  If your cases are predominantly one ancestry and controls another,
  you will find thousands of false positives — variants that differ
  by ancestry, not by disease.

  EXAMPLE (famous Simpson's Paradox version):
  Chopstick use is extremely common in Japan; so is type 2 diabetes.
  Naïve association: chopstick use "causes" T2D.
  Real cause: ancestry is a confounder.

  SOLUTION: PRINCIPAL COMPONENT ANALYSIS (PCA) OF GENOTYPES
  ┌─────────────────────────────────────────────────────────┐
  │ 1. Compute covariance matrix of genotypes (samples × SNPs)│
  │ 2. PCA decomposition: PC1, PC2, ... explain ancestry    │
  │ 3. In most studies:                                     │
  │    PC1 ≈ European vs. African ancestry axis             │
  │    PC2 ≈ East Asian vs. South Asian axis                │
  │    PC3–10: finer structure                              │
  │ 4. Include top 10 PCs as covariates in regression       │
  │    → removes ancestry-driven association                │
  └─────────────────────────────────────────────────────────┘

  GENOMIC INFLATION FACTOR (λ):
  Median χ² statistic / expected median under H₀
  λ = 1.0: no inflation (expected under correct model)
  λ > 1.05: stratification or other bias likely
  QQ plot: observed p-values vs. expected — diagonal = well-calibrated
```

---

## Fine-Mapping: Narrowing to Causal Variants

```
  FINE-MAPPING
  =============

  GWAS hit = association signal in a ~100-500 kb LD block.
  The "tag SNP" may not be causal — just in LD with the real variant.
  Fine-mapping uses statistics to narrow to a credible set.

  APPROACHES:
  ┌──────────────────────────────────────────────────────────┐
  │ CONDITIONAL ANALYSIS                                     │
  │   Condition on the lead SNP, look for residual signal    │
  │   Identifies multiple independent signals in same locus  │
  │                                                          │
  │ BAYESIAN FINE-MAPPING (FINEMAP, SUSIE)                   │
  │   Compute posterior inclusion probability (PIP) per SNP  │
  │   "Credible set": smallest set of SNPs covering 95%      │
  │   of posterior probability of containing causal variant  │
  │   Good locus: 1–3 SNP credible set                       │
  │   Bad locus: 100 SNP credible set (all in LD)            │
  │                                                          │
  │ FUNCTIONAL ANNOTATION (LDSC, CAVIARBF)                   │
  │   Prioritize SNPs in regulatory elements (ENCODE, ATAC)  │
  │   eQTL colocalization: is the GWAS hit also an eQTL?     │
  └──────────────────────────────────────────────────────────┘

  eQTL: Expression quantitative trait locus
  A variant that affects gene expression level
  If GWAS hit = eQTL for gene X → evidence X is the mechanism
  Tool: SMR (Summary-based Mendelian Randomization), coloc
```

---

## Polygenic Risk Scores (PRS)

```
  POLYGENIC RISK SCORES: AGGREGATE GENETIC RISK
  ===============================================

  CONCEPT:
  Most complex traits (height, BMI, T2D, schizophrenia) are
  "polygenic" — influenced by thousands of variants, each with
  tiny individual effect.

  PRS = Σ (effect size_i × dosage_i) for all significant SNPs

  Height example:
  - ~10,000 SNPs explain ~40% of height variance
  - Each SNP: effect size 0.01–0.3 cm per allele
  - PRS = weighted sum of all alleles
  - Top PRS decile vs. bottom: ~15 cm height difference

  CONSTRUCTION:
  1. GWAS summary statistics (effect sizes from base population)
  2. LD clumping/thresholding OR more sophisticated methods:
     - LDpred2: Bayesian shrinkage of effect sizes
     - PRSice2: C+T approach (clumping + thresholding)
  3. Apply to target population: weight × genotype per SNP
  4. Validate in independent cohort

  CLINICAL APPLICATIONS:
  ┌─────────────────────────────────────────────────────────┐
  │ Coronary artery disease PRS (Inouye et al. 2018):       │
  │   Top 8% PRS = 3x increased risk vs. average            │
  │   Comparable to monogenic familial hypercholesterolemia │
  │                                                         │
  │ Breast cancer PRS:                                      │
  │   Combined with BRCA1/2 testing in clinical use         │
  │   Top percentile PRS + no BRCA1/2 → preventive measures │
  │                                                         │
  │ LIMITATIONS:                                            │
  │   PRS trained on European ancestry → poor transferability│
  │   to non-European populations (LD patterns differ)      │
  │   Active research: multi-ancestry PRS methods           │
  └─────────────────────────────────────────────────────────┘
```

---

## Mendelian Randomization (MR)

```
  MENDELIAN RANDOMIZATION: CAUSAL INFERENCE FROM GWAS
  =====================================================

  PROBLEM: GWAS finds associations, not causation.
  Is LDL → heart disease causal? Or confounded?
  (Maybe people with high LDL also have unhealthy diets that cause both.)

  MENDELIAN RANDOMIZATION APPROACH:
  ┌──────────────────────────────────────────────────────────┐
  │ Instrumental variable: Use genetic variants as "natural  │
  │ randomization" for the exposure.                         │
  │                                                          │
  │ Analogy: Random assignment in RCT → genetic assignment   │
  │   RCT: randomly give statin vs. placebo                  │
  │   MR: people with LDL-lowering alleles vs. LDL-raising   │
  │       alleles (randomly assigned at conception)          │
  │                                                          │
  │ LOGIC:                                                   │
  │ If variant → LDL ↑ (confirmed by LDL GWAS)               │
  │ And variant → heart disease ↑ (confirmed by CHD GWAS)    │
  │ And variant affects CHD only through LDL (key assumption)│
  │ → CAUSAL evidence that LDL → CHD                         │
  └──────────────────────────────────────────────────────────┘

  TWO-SAMPLE MR:
  Use summary statistics from two separate GWAS
  (exposure GWAS + outcome GWAS, can be different samples)

  SENSITIVITY ANALYSES:
  MR-Egger: tests for directional pleiotropy
  Weighted median: robust to 50% invalid instruments
  MR-PRESSO: detects outlier SNPs

  KEY LIMITATION: PLEIOTROPY
  If variant affects multiple traits (common!), the "only
  through LDL" assumption fails → biased estimate.
  Multiple sensitivity analyses are required.
```

---

## Biobanks

```
  LARGE-SCALE BIOBANKS DRIVING MODERN GWAS
  ==========================================

  ┌──────────────────────────────────────────────────────────────┐
  │ BIOBANK                N          KEY FEATURE                │
  │ UK Biobank          502,000       500+ traits, deep phenotype│
  │ FinnGen             500,000+      Population isolate (rare)  │
  │ All of Us (NIH)     1,000,000+    Diverse US ancestry        │
  │ BioMe (Mount Sinai) 50,000        NYC diversity              │
  │ deCODE (Iceland)    ~166,000      ~50% of Iceland population │
  │ BBMRI (Europe)      >500,000      Meta-analysis consortium   │
  └──────────────────────────────────────────────────────────────┘

  META-ANALYSIS:
  Combine results from multiple cohorts for greater power
  Method: Fixed-effects meta-analysis of summary statistics (METAL)
  Example: Type 2 diabetes GWAS → 600,000 cases → 1,000+ loci found
```

---

## Decision Cheat Sheet

| Goal | Method/Tool |
|------|-------------|
| Run GWAS for complex disease | PLINK2 + SAIGE (for imbalanced case-control) |
| Impute genotype array to genome | Michigan Imputation Server / TOPMed |
| Correct for population stratification | PCA covariates (flashpca2) |
| Find independent signals at locus | Conditional analysis (GCTA-COJO) |
| Fine-map to credible set | SuSiE or FINEMAP |
| Compute polygenic risk score | LDpred2 or PRSice2 |
| Causal inference from GWAS | Two-sample MR (TwoSampleMR R package) |
| Find eQTLs for GWAS colocalization | coloc R package |
| LD calculation / score regression | LDSC (LD score regression) |
| Visualize GWAS results | qqman, CMplot, LocusZoom |

---

## GWAS as Large-Scale A/B Testing and Feature Selection

```
GWAS ↔ A/B TESTING + FEATURE SELECTION
──────────────────────────────────────────────────────────────────────────────
GWAS IS A MASSIVELY PARALLEL A/B TEST:

  Classic A/B test: one treatment, two groups, one metric, one p-value
  GWAS: 5,000,000 "treatments" (alleles), two groups (cases/controls),
        one metric per allele (trait), 5,000,000 p-values

  Multiple-testing correction:
    A/B testing: Bonferroni or BH-FDR across variants
    GWAS: p < 5×10⁻⁸ (Bonferroni for ~1M independent tests)
    Same principle: threshold must scale with number of tests

  Statistical power:
    A/B: power from sample size × effect size
    GWAS: same — rare variants need larger N; small effects need larger N
    Meta-analysis = pooling A/B test results across cohorts (METAL = forest plot at scale)

PRS ↔ FEATURE IMPORTANCE AGGREGATION:

  Random forest / XGBoost: feature importance = how much each feature
    (SNP) predicts the target (disease)
  PRS = weighted sum of all SNP contributions to a continuous risk score
  β_i in GWAS = effect size = analogous to feature weight in a linear model

  GWAS → PRS pipeline is exactly supervised learning:
    Training set: GWAS on discovery cohort
    Model: linear combination of SNP dosages × effect sizes
    Regularization: LDpred2 applies Bayesian shrinkage (like ridge regression
      on correlated features) to handle LD = feature correlation
    Validation: evaluate PRS in held-out cohort (AUC, calibration)
    Generalization problem: PRS trained on European ancestry → poor transfer
      to African ancestry = domain shift in transfer learning

MENDELIAN RANDOMIZATION ↔ INSTRUMENTAL VARIABLE REGRESSION:

  IV regression: use an exogenous instrument Z to estimate causal effect
    of X on Y when X is confounded
  MR: genetic variant Z (randomly assigned at conception) → instruments
    for exposure X (LDL) → estimates causal effect on outcome Y (CHD)
  Assumption violation (pleiotropy) = IV invalidity (instrument affects Y
    through pathways other than X)
  Sensitivity analyses (MR-Egger, MR-PRESSO) = IV validity tests
──────────────────────────────────────────────────────────────────────────────
```

## Common Confusion Points

**GWAS hits are rarely in coding regions**: ~90% of GWAS hits fall in non-coding regions (introns, intergenic). This is because most causal variants affect gene regulation (enhancers, promoters), not protein sequence. This is why ENCODE/epigenomics is critical for GWAS interpretation.

**OR vs. absolute risk**: A GWAS hit with OR = 1.5 sounds large. But if baseline risk is 1% (e.g., type 1 diabetes), OR 1.5 → 1.5% absolute risk. Most GWAS effect sizes are modest and not individually clinically actionable — PRS aggregates them.

**Winner's curse**: The first time a variant reaches genome-wide significance, its effect size is usually overestimated (selection bias toward extreme values that crossed the threshold). Replication in independent cohorts + meta-analysis corrects this.

**Ancestry portability of PRS**: A PRS built from European GWAS doesn't work well in African populations. Reasons: LD patterns differ (different ancestral haplotypes), causal variant frequencies differ, training data lacks diversity. Multi-ancestry GWAS and trans-ethnic fine-mapping are active research areas.

**Heritability ≠ GWAS explained**: Twin studies estimate height is ~80% heritable. GWAS explains ~30–40% of variance. The gap ("missing heritability") comes from: rare variants not on arrays, epistasis, structural variants, and power limitations. Larger GWAS keep recovering more heritability.
