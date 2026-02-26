# Personalized Medicine and Clinical Genomics

## The Big Picture

```
PERSONALIZED MEDICINE: GENOMICS IN THE CLINIC
===============================================

  SPECTRUM OF CLINICAL APPLICATIONS:
  ┌──────────────────────────────────────────────────────────────────┐
  │                                                                   │
  │  PHARMACOGENOMICS                                                 │
  │  Which drugs work for you? Which are dangerous?                  │
  │  Germline variants in drug-metabolizing genes                    │
  │                                                                   │
  │  RARE DISEASE DIAGNOSIS                                          │
  │  ~7,000 rare diseases, ~80% genetic cause                       │
  │  Exome/genome sequencing as diagnostic endpoint                  │
  │  ~35% diagnostic yield (undiagnosed disease programs)           │
  │                                                                   │
  │  CANCER GENOMICS                                                 │
  │  Tumor sequencing to match therapy to mutation                  │
  │  Resistance mutation monitoring                                  │
  │  Liquid biopsy for early detection                               │
  │                                                                   │
  │  PREIMPLANTATION / PRENATAL                                     │
  │  PGT-M: single-gene disease testing of embryos                  │
  │  cfDNA: cell-free DNA in maternal blood for trisomy             │
  │                                                                   │
  │  HEREDITARY CANCER / RISK                                       │
  │  BRCA1/2, Lynch syndrome, APC, TP53                             │
  │  Polygenic risk scores in population screening                  │
  │                                                                   │
  │  INFECTIOUS DISEASE                                              │
  │  Pathogen sequencing for outbreak investigation                  │
  │  Drug resistance prediction (TB, HIV)                            │
  └──────────────────────────────────────────────────────────────────┘

  MARKET CONTEXT (2024):
  Clinical WES: ~$400–800 per test
  Clinical WGS: ~$700–2,000 per test
  Gene panel: ~$200–500 per test (25–500 genes)
  SNP array: ~$50–200 per test
  Sequencing in FDA-approved CDx: ~$300–600 (companion diagnostics)
```

---

## Pharmacogenomics (PGx)

```
  PHARMACOGENOMICS: THE DRUG-GENE INTERACTION MAP
  ==================================================

  CORE PRINCIPLE: Genetic variants affect drug metabolism,
  response, and toxicity. Same dose → different outcomes.

  CYP450 ENZYME SUPERFAMILY (the key metabolizers):
  ┌──────────────────────────────────────────────────────────────────┐
  │ CYP2D6  Most polymorphic CYP gene                                │
  │         Metabolizes: codeine, tamoxifen, tramadol,              │
  │                      antidepressants (fluoxetine, paroxetine)   │
  │         Poor metabolizer (PM): toxic accumulation of prodrug   │
  │         Ultrarapid metabolizer (UM): no effect from prodrug    │
  │                                                                   │
  │ CYP2C19 Metabolizes: clopidogrel (Plavix), PPIs, SSRIs         │
  │         *2 allele: loss-of-function (28% of East Asians)        │
  │         PM + clopidogrel → no antiplatelet effect → stent clot │
  │         FDA Black Box Warning: test before prescribing           │
  │                                                                   │
  │ CYP2C9  Metabolizes: warfarin, NSAIDs                           │
  │         *2, *3 alleles → reduced metabolism → bleeding risk     │
  │         Dosing algorithm: warfarin dose = f(CYP2C9, VKORC1)    │
  │                                                                   │
  │ CYP3A4/5 Metabolizes: ~50% of all drugs (statin, tacrolimus)   │
  │          Less polymorphic; inducible (rifampin, carbamazepine) │
  └──────────────────────────────────────────────────────────────────┘

  METABOLIZER PHENOTYPE CLASSIFICATION:
  PM = Poor Metabolizer:    Two nonfunctional alleles
  IM = Intermediate:        One reduced-function allele
  NM = Normal:              Two functional alleles
  RM = Rapid Metabolizer:   One increased-function allele
  UM = Ultrarapid Metabolizer: Gene duplication → extra enzyme

  NON-CYP PGx EXAMPLES:
  TPMT: Thiopurine methyltransferase — metabolizes azathioprine/6-MP
    Deficient patients: catastrophic bone marrow suppression
    Now tested before pediatric chemotherapy protocols
  DPYD: DPD enzyme — metabolizes 5-fluorouracil
    Deficient: life-threatening mucositis/neutropenia
    DPYD testing now required before 5-FU in many guidelines
  UGT1A1: Irinotecan (camptothecin) metabolism
    *28 allele: severe diarrhea/neutropenia — dose reduction needed
  HLA-B*57:01: Abacavir (HIV drug) hypersensitivity
    HLA-B*57:01 carriers: fatal Stevens-Johnson syndrome
    Standard of care: test before prescribing

  CLINICAL PGOMICS PANELS (e.g., GeneSight, Blueprint Genetics):
  ─ Type 40–80 key PGx variants across 5–10 CYP genes
  ─ Algorithm reports actionable gene-drug pairs
  ─ Currently used for: psychiatry, oncology, cardiology, pain management
```

---

## Rare Disease Diagnosis

```
  RARE DISEASE GENOMICS: THE DIAGNOSTIC ODYSSEY
  ================================================

  SCALE:
  ~7,000 recognized rare diseases
  ~80% have identified genetic basis
  ~30 million people affected in the US
  Average time to diagnosis: 5–7 years (the "diagnostic odyssey")

  TESTING STRATEGY (tiered):
  ┌──────────────────────────────────────────────────────────────┐
  │ TIER 1: TARGETED PANEL (if phenotype suggests specific gene) │
  │   e.g., CFTR for CF; FBN1 for Marfan; dystrophin for DMD    │
  │   Fast, cheap (~$200), high depth (>1000x)                   │
  │                                                               │
  │ TIER 2: WHOLE EXOME SEQUENCING (WES)                        │
  │   Captures all ~20,000 genes at once                         │
  │   Diagnostic yield: ~25–40% in rare disease (higher for      │
  │   early-onset severe phenotypes)                             │
  │   Cost: ~$400–800                                            │
  │   Analysis: trio (proband + both parents) maximizes yield   │
  │                                                               │
  │ TIER 3: WHOLE GENOME SEQUENCING (WGS)                       │
  │   Captures non-coding, structural variants missed by WES    │
  │   Diagnostic yield: ~5–15% additional over WES              │
  │   Used for: exome-negative cases; suspected regulatory/SV   │
  │   Cost: ~$700–2,000                                          │
  └──────────────────────────────────────────────────────────────┘

  TRIO ANALYSIS CONCEPT:
  Proband (affected child) + mother + father
  ─ De novo variants: present in proband, absent in both parents
    → strong evidence of pathogenicity for severe early-onset disease
  ─ Recessive: both parents carrier, proband homozygous/compound het
  ─ X-linked: mother carrier, affected son

  VARIANT INTERPRETATION PIPELINE:
  ┌──────────────────────────────────────────────────────────────┐
  │ 1. Filter by frequency: gnomAD AF <0.1% for severe disease  │
  │ 2. Filter by consequence: LoF + missense in disease genes   │
  │ 3. Filter by inheritance: de novo / homozygous / comp. het  │
  │ 4. Functional prediction: CADD score, SIFT, PolyPhen        │
  │ 5. Literature search: gene in disease databases (OMIM)      │
  │ 6. ACMG classification: P/LP/VUS/LB/B                       │
  │ 7. Return result: typically 1–5 candidate variants          │
  └──────────────────────────────────────────────────────────────┘

  REANALYSIS: Diagnostic yield increases with time
  Re-analyzing negative exomes every 2–3 years recovers ~10% more
  (new gene-disease associations established in OMIM/ClinGen)
```

---

## Somatic Cancer Genomics

```
  CANCER GENOMICS IN CLINICAL PRACTICE
  ========================================

  COMPANION DIAGNOSTICS (CDx): FDA-approved tumor genomic tests
  that determine which drug to use.

  KEY ACTIONABLE ALTERATIONS:
  ┌──────────────────────────────────────────────────────────────────┐
  │ ALTERATION      CANCER           DRUG                            │
  │ EGFR exon 19/21 NSCLC            Erlotinib/Osimertinib           │
  │ ALK fusion      NSCLC            Crizotinib/Alectinib            │
  │ HER2 amplif.    Breast           Trastuzumab/T-DM1               │
  │ BRAF V600E      Melanoma/CRC     Vemurafenib/Dabrafenib          │
  │ BRCA1/2         Ovarian/Breast   Olaparib (PARP inhibitor)       │
  │ MSI-H/dMMR      Pan-cancer       Pembrolizumab (PD-1)           │
  │ KRAS G12C       NSCLC/CRC        Sotorasib/Adagrasib             │
  │ FGFR2 fusion    Cholangiocarc.   Pemigatinib                     │
  │ RET fusion      NSCLC/Thyroid    Selpercatinib                   │
  │ NTRK fusion     Pan-cancer       Larotrectinib                   │
  └──────────────────────────────────────────────────────────────────┘

  TUMOR MUTATIONAL BURDEN (TMB) AND MSI:
  ─ TMB: mutations per Mb; High TMB (>10/Mb) → pembrolizumab approval
  ─ MSI-H/dMMR: mismatch repair deficiency → TMB very high
    → FDA approval for any MSI-H solid tumor (pan-cancer)
  ─ Measured by: panel sequencing (FoundationOne, MSK-IMPACT)

  COMPREHENSIVE GENOMIC PROFILING (CGP):
  ─ FoundationOne CDx: 324-gene panel, FDA-approved
  ─ MSK-IMPACT: 468-gene panel (Memorial Sloan Kettering)
  ─ TEMPUS xT: 648-gene panel + RNA fusion detection
  ─ Output: Full somatic alterations + MSI + TMB + signatures

  RESISTANCE MONITORING:
  EGFR T790M: Primary resistance mutation to 1st/2nd-gen EGFR TKI
  Osimertinib (3rd-gen) overcomes T790M → but EGFR C797S emerges
  Serial monitoring via liquid biopsy tracks resistance evolution
```

---

## Liquid Biopsy (ctDNA)

```
  LIQUID BIOPSY: SEQUENCING CANCER DNA FROM BLOOD
  ==================================================

  MECHANISM:
  Tumor cells release DNA fragments into bloodstream
  Cell-free DNA (cfDNA) = mix of normal + tumor DNA
  Tumor fraction: 0.01% – 50% (varies with stage/tumor type)

  TECHNOLOGY:
  ┌──────────────────────────────────────────────────────────────┐
  │ cfDNA extraction from 5–10 mL plasma (not whole blood)      │
  │ Library prep with unique molecular identifiers (UMIs)        │
  │ Ultra-deep sequencing (500x–100,000x target depth)          │
  │ Error correction via UMI consensus sequencing               │
  │ Detection threshold: ~0.1% VAF (with deep sequencing)       │
  └──────────────────────────────────────────────────────────────┘

  CLINICAL APPLICATIONS:
  ┌──────────────────────────────────────────────────────────────┐
  │ TREATMENT MONITORING:                                         │
  │   Serial cfDNA tracks tumor burden over time                 │
  │   Clearance of ctDNA → response to therapy                  │
  │   Rising ctDNA → progression before imaging shows it        │
  │                                                               │
  │ RESISTANCE DETECTION:                                         │
  │   EGFR T790M detectable in cfDNA before clinical progression │
  │   Guides switch from 1st → 3rd-gen EGFR inhibitor           │
  │                                                               │
  │ MINIMAL RESIDUAL DISEASE (MRD):                              │
  │   Post-surgery ctDNA → predicts recurrence                  │
  │   Personalized assay: tumor-informed (know mutations)        │
  │   BESPOKE study: ctDNA at day 30 predicts 3-yr survival     │
  │                                                               │
  │ EARLY DETECTION (GRAIL Galleri):                             │
  │   Methylation + fragment pattern across 50+ cancer types    │
  │   Tissue-of-origin signal → localize tumor                  │
  │   Sensitivity varies: ~50–90% for stage 3–4, ~20% stage 1  │
  └──────────────────────────────────────────────────────────────┘
```

---

## Prenatal and Preimplantation

```
  REPRODUCTIVE GENOMICS
  ======================

  NONINVASIVE PRENATAL TESTING (NIPT):
  ─ cfDNA in maternal blood: ~10–15% is from placenta (not fetus)
  ─ Counts chromosomal DNA: extra chr21 signal → trisomy 21 detected
  ─ Sensitivity: ~99.5% for trisomy 21; lower for other trisomies
  ─ No procedure risk (vs. amniocentesis ~0.1–0.3% miscarriage)
  ─ Detects: T21 (Down), T18 (Edwards), T13 (Patau), sex chromosome

  PREIMPLANTATION GENETIC TESTING (PGT):
  ┌──────────────────────────────────────────────────────────────┐
  │ PGT-M (Monogenic): Test embryo for specific disease-causing  │
  │   variant (e.g., BRCA1, CF, Huntington's, sickle cell)      │
  │   Protocol: IVF → biopsy 5–10 cells from blastocyst         │
  │   Whole genome amplify → targeted sequencing                │
  │   Select unaffected embryos for transfer                    │
  │                                                               │
  │ PGT-A (Aneuploidy): Check all 24 chromosomes for copy number │
  │   Detects trisomy, monosomy, segmental gains/losses          │
  │   Reduces miscarriage rate; controversial for older patients  │
  │                                                               │
  │ PGT-SR (Structural Rearrangement): For carriers of          │
  │   chromosomal inversions/translocations                       │
  └──────────────────────────────────────────────────────────────┘
```

---

## Hereditary Cancer

```
  HEREDITARY CANCER SYNDROMES
  =============================

  HEREDITARY BREAST/OVARIAN CANCER (HBOC):
  BRCA1/2 genes — tumor suppressors for homologous recombination
  BRCA1 carrier:  ~70% lifetime breast cancer risk; ~40–46% ovarian
  BRCA2 carrier:  ~69% breast cancer risk; ~10–27% ovarian
  Management: Enhanced screening; risk-reducing surgery; PARP inhibitors

  LYNCH SYNDROME:
  Mismatch repair genes: MLH1, MSH2, MSH6, PMS2, EPCAM
  Microsatellite instability (MSI-H) in tumors
  Colorectal cancer: 50–80% lifetime risk
  Endometrial cancer: 25–60% lifetime risk
  Management: Colonoscopy every 1–2 years; prophylactic surgery consideration

  Li-Fraumeni (TP53), APC/FAP, PTEN (Cowden), RB1, VHL, NF1/2...

  GENETIC COUNSELING REQUIRED:
  ─ Pre-test counseling: implications, who else to test
  ─ Post-test counseling: result interpretation
  ─ Cascade testing: first-degree relatives of carriers

  MULTI-GENE PANEL TESTING:
  Previously: BRCA1/2 only. Now: 30–80 gene panels
  Challenge: More VUS with more genes tested
  Clinical utility: evidence-based recommendations per gene (NCCPA)
```

---

## Decision Cheat Sheet

| Clinical Scenario | Genomic Test |
|-------------------|-------------|
| Suspected genetic disease in child | WES trio (proband + parents) |
| Adult-onset familial cancer risk | Hereditary cancer panel (30–80 genes) |
| NSCLC driver mutation for therapy | CGP panel (FoundationOne CDx) |
| Monitor cancer treatment response | ctDNA (liquid biopsy) |
| Drug toxicity risk (psychiatric meds) | PGx panel (CYP2D6/2C19/2C9) |
| Warfarin dosing | CYP2C9 + VKORC1 genotyping |
| Abacavir (HIV) safety | HLA-B*57:01 testing |
| Prenatal trisomy screening | NIPT (cfDNA) |
| Embryo selection (IVF) | PGT-M or PGT-A |
| Population cancer screening | Multi-cancer early detection (GRAIL) |
| Exome-negative rare disease | WGS (captures non-coding + SVs) |
| Refractory cancer, any type | TMB/MSI testing + immunotherapy |

---

## Clinical Genomics Pipelines as Decision Support Systems

```
CLINICAL GENOMICS ↔ DECISION SUPPORT / RULE ENGINES / MONITORING
──────────────────────────────────────────────────────────────────────────────
ACMG VARIANT CLASSIFICATION = WEIGHTED DECISION TABLE:

  Problem: given a variant (row), classify as P/LP/VUS/LB/B (5-class output)
  Method: sum weighted evidence criteria (28 named criteria: PVS1, PS1..., PM1..., etc.)

  Evidence criteria structure:
  ┌────────────────────────────────────────────────────────────────┐
  │ Criterion  Weight   Type    Meaning                            │
  │ PVS1       Very    Pathog.  Loss-of-function in LoF gene       │
  │ PS1        Strong  Pathog.  Same AA change, known pathogenic   │
  │ PM2        Moder.  Pathog.  Absent/low freq in gnomAD          │
  │ BP7        Supp.   Benign   Synonymous, no splice prediction   │
  └────────────────────────────────────────────────────────────────┘

  This IS a decision tree / rule engine with evidence weights:
  Equivalent to: rules engine in an expert system (Drools, CLIPS)
  Modern variant interpretation tools (Emedgene, Fabric, Alissa) are
  ML-augmented rule engines that automate this classification

CANCER GENOMIC PROFILING (CGP) = MONITORING DASHBOARD WITH ALERT RULES:

  CGP panel (FoundationOne CDx, MSK-IMPACT):
  - Sequence 300–650 genes at high depth in tumor
  - Filter: somatic variants only (subtract germline / normal sample)
  - Alert on: variants in clinically actionable genes with FDA/guideline support
  - Output: actionable alterations (like PagerDuty alerts from noisy telemetry)
  - Noise: VUS, passenger mutations = monitoring noise without clinical signal

  Mapping:
  Tumor genome variants     ↔  System telemetry (millions of metrics)
  Normal genome subtraction ↔  Baseline normalization / anomaly detection
  Tier 1 actionable variant ↔  P0 alert (requires immediate response)
  VUS                       ↔  Warning-level alert (monitor, no action yet)
  Passenger mutation        ↔  Noise (no action, log only)
  TMB / MSI-H               ↔  Aggregate system health metric
  Serial ctDNA monitoring   ↔  Real-time uptime / SLA metric with trending

LIQUID BIOPSY (ctDNA) = CONTINUOUS INTEGRATION TESTING:

  Each blood draw = CI pipeline run
  Detect ctDNA level        ↔  Test suite passing / failing
  Rising ctDNA              ↔  Test failure trend → impending production issue
  ctDNA clearance           ↔  All tests green → treatment is working
  Resistance mutation        ↔  New failure mode discovered → need new fix
  Detection threshold 0.1%  ↔  Signal-to-noise floor in the monitoring stack

VARIANT INTERPRETATION PIPELINE = DATA QUALITY PIPELINE:

  gnomAD allele frequency filter (AF < 0.1%) ↔  Outlier filtering (common = noise)
  ClinVar lookup             ↔  Reference data join (known variants)
  CADD score (deleteriousness)↔  Model score (ML feature in variant prioritization)
  Inheritance filtering      ↔  Constraint satisfaction (de novo / recessive mode)
  VUS reclassification over time ↔  Data quality label updates as new evidence arrives
──────────────────────────────────────────────────────────────────────────────
```

## Common Confusion Points

**WES missing the diagnosis**: Whole exome sequencing misses: (1) deep intronic variants that affect splicing, (2) large structural variants (most CNVs), (3) repeat expansion diseases (Huntington's, fragile X, spinocerebellar ataxias — require specific assays), (4) mitochondrial DNA variants (poorly captured). WGS covers these but costs more.

**Germline vs. somatic BRCA**: A patient with breast cancer can have BRCA2 variants in two ways: (1) germline — inherited, present in all cells, heritable risk to family; (2) somatic — acquired only in the tumor, not inherited. A tumor BRCA2 variant detected on CGP panel does not tell you which. Germline testing requires a separate blood sample and dedicated germline sequencing.

**ctDNA sensitivity limitations**: Liquid biopsy sensitivity depends on tumor shedding. CNS tumors shed minimally into blood (better detected in CSF). Many early-stage cancers shed near the detection limit. A negative liquid biopsy never rules out cancer — it means ctDNA is below the detection threshold.

**VUS in hereditary cancer**: ~40–60% of patients undergoing BRCA1/2 testing receive a VUS result. This means uncertain, not benign. The correct management for VUS is the same as for someone with no variant found — increased family communication if evidence changes. Do not manage as pathogenic unless reclassified.

**Pharmacogenomics is not theragnostics**: PGx tells you about drug metabolism (how fast your body processes a drug). It does not directly predict efficacy for complex diseases (whether the drug will control your condition). These are different aspects of drug response.
