# Pharmacogenomics and Personalized Medicine

## The Big Picture

Pharmacogenomics (PGx) is the study of how genetic variation affects drug response. It explains why the same drug and dose causes therapeutic success in one patient, toxicity in another, and no effect in a third. Personalized (precision) medicine uses genetic, genomic, and other molecular data to select the right drug at the right dose.

```
+──────────────────────────────────────────────────────────────────+
|              PHARMACOGENOMICS LANDSCAPE                          |
|                                                                  |
|  GENOTYPE → PHENOTYPE → DRUG RESPONSE                           |
|                                                                  |
|  SNPs in:           Phenotype:              Drug impact:         |
|  CYP enzymes    →  PM/IM/EM/UM         →   Dose adjustment      |
|  Transporters   →  ↓/↑ drug uptake     →   Efficacy/toxicity    |
|  Drug targets   →  Altered target       →   Response or failure  |
|  HLA alleles    →  Immune reactions     →   Severe hypersensitivity|
|  Ion channels   →  Altered electrophys  →   QT prolongation      |
|                                                                  |
|  PHARMACOGENOMIC TESTING                                         |
|  Reactive: test after adverse event or failure                   |
|  Pre-emptive: test panel ONCE, consult EHR at every prescription |
+──────────────────────────────────────────────────────────────────+
```

---

## CYP Pharmacogenomics: The Core

```
METABOLIZER PHENOTYPE SPECTRUM
────────────────────────────────
  PHENOTYPE           GENOTYPE              ENZYME ACTIVITY
  ─────────────────── ──────────────────    ──────────────────────
  Poor Metabolizer    2 loss-of-func alleles  None (0%)
  (PM)
  Intermediate        1 functional +         Reduced (~50%)
  Metabolizer (IM)    1 reduced-func
  Extensive/Normal    2 functional            Normal (100%)
  Metabolizer (EM)
  Ultrarapid          Gene duplication        Increased (>200%)
  Metabolizer (UM)    (3+ functional copies)

KEY DRUGS AFFECTED BY EACH CYP GENE
──────────────────────────────────────

CYP2D6 (most polymorphic)
  Poor metabolizer: 5-10% Caucasians, 1-2% East Asians
  Ultrarapid: 1-7% Caucasians, 10-30% North Africans

  Drug         EM (normal)      PM effect        UM effect
  ──────────── ──────────────   ─────────────    ─────────────────
  Codeine      Converts to      No analgesia     Excess morphine →
               morphine         (prodrug fails)  overdose, death
  Tramadol     Active metabolite No analgesia   Excess active metabolite
               needed                            → serotonin syndrome
  TCAs         Normal levels    Toxicity at low  Inadequate therapy
               (amitriptyline)  doses
  Tamoxifen    → endoxifen      No active        —
               (active)         metabolite → ↓efficacy in breast cancer
  Metoprolol   Normal response  ↑Bradycardia    ↓Effect (↓concentration)
  Flecainide   Normal           Toxicity risk    —

CYP2C19
  Poor metabolizer: 2-5% Caucasians, 15-25% East Asians (much higher!)

  Drug         EM             PM effect          UM effect
  ──────────── ────────────── ──────────────     ────────────────────
  Clopidogrel  Active         NO antiplatelet    —
               metabolite     effect → stent
               formed         thrombosis
  PPIs         Normal         Better acid        Reduced acid suppression
               suppression    suppression        (may need higher dose)
  Voriconazole Normal levels  Toxicity risk      Inadequate therapy
               (antifungal)   (↑levels)          (↓levels)
  Escitalopram Normal         Higher levels →    —
                              may need lower dose

CYP2C9
  Drug affected: Warfarin (S-enantiomer)
  CYP2C9*2 and *3: reduced activity
  Patient on standard warfarin dose → supratherapeutic INR → bleeding
  FDA label recommends CYP2C9 + VKORC1 genotype for warfarin dosing

CYP1A2
  Strong inducer: smoking
  Drugs affected: Clozapine, olanzapine, theophylline
  Smoker on clozapine: CYP1A2 induced → faster metabolism → 40-50% lower levels
  If smoker starts antipsychotic then QUITS SMOKING:
  → CYP1A2 induction wanes → clozapine levels rise → toxicity
  Monitor levels and reduce dose proactively when patients quit smoking.
```

---

## Non-CYP Pharmacogenomics

```
PHASE II ENZYME VARIANTS
─────────────────────────
TPMT (thiopurine methyltransferase)
  Inactivates: 6-mercaptopurine (6-MP), azathioprine, thioguanine
  Low activity: 1/300 people
  Standard dose in low-TPMT patient → drug accumulates → severe myelosuppression

  Clinical practice: Test TPMT before prescribing azathioprine (IBD, transplant)
  OR test NUDT15 (also affects thiopurine metabolism; important in East Asians)

  TPMT genotype → dose reduction:
    Heterozygous (IM): reduce dose 50%
    Homozygous PM: dose reduce 90% or use alternative

UGT1A1 (glucuronosyltransferase)
  Metabolizes: Irinotecan active metabolite SN-38, bilirubin
  UGT1A1*28: Gilbert syndrome polymorphism (TA repeat in promoter → ↓expression)
  Higher SN-38 → severe neutropenia and diarrhea with standard irinotecan dose
  FDA label: test UGT1A1 before high-dose irinotecan therapy

NAT2 (N-acetyltransferase)
  Slow acetylators: isoniazid (TB treatment), hydralazine, procainamide
  Slow = higher drug levels = more peripheral neuropathy (isoniazid)
  Fast = lower levels + more reactive metabolite → hepatotoxicity (isoniazid)
  Bimodal: ~50% Caucasians slow, ~10% East Asians slow

DPYD (dihydropyrimidine dehydrogenase)
  Metabolizes: Fluoropyrimidines (5-FU, capecitabine)
  DPYD*2A and other variants: ↓DPYD activity → 5-FU accumulates → SEVERE toxicity
  Symptoms: mucositis, myelosuppression, diarrhea, neurotoxicity — potentially fatal
  European guidelines: test DPYD before any 5-FU-based therapy
  FDA added DPYD testing to 5-FU label
  If DPYD heterozygous: reduce dose 50%
  If DPYD homozygous null: avoid fluoropyrimidines
```

---

## HLA-Related Drug Hypersensitivity

```
HLA ALLELES AND DRUG HYPERSENSITIVITY REACTIONS
─────────────────────────────────────────────────
Some severe drug reactions are HLA allele-dependent:

HLA-B*57:01 AND ABACAVIR
  Abacavir: nucleoside reverse transcriptase inhibitor for HIV
  HLA-B*57:01 carriers: SEVERE hypersensitivity reaction (HSR)
    Fever, rash, GI symptoms, respiratory symptoms
    FATAL if abacavir is re-challenged after reaction
  Prevalence of HLA-B*57:01: 5-8% Caucasians, 2-3% Africans, <1% Asians
  Clinical practice: Screen ALL patients before initiating abacavir (standard of care)
  If negative: use abacavir safely; reaction essentially eliminated by screening
  This is the PGx SUCCESS STORY: prospective screening prevents severe reactions.

HLA-B*15:02 AND CARBAMAZEPINE
  Carbamazepine (antiepileptic): Stevens-Johnson syndrome / toxic epidermal necrolysis
  SJS/TEN: severe mucocutaneous reaction; life-threatening
  HLA-B*15:02 prevalence: 5-15% Han Chinese, Thai, Malaysian; rare in Caucasians
  FDA Black Box: screen Han Chinese, Thai populations before starting carbamazepine
  Alternative: oxcarbazepine or lamotrigine (different HLA association)

HLA-B*58:01 AND ALLOPURINOL
  Allopurinol (gout treatment): SJS/TEN in HLA-B*58:01 carriers
  Prevalence: 6-8% Han Chinese; screening recommended in some guidelines
  for Han Chinese patients before initiating allopurinol

HLA-A*31:01 AND CARBAMAZEPINE (different HLA, different reaction type)
  Drug reaction with eosinophilia and systemic symptoms (DRESS)
  In Caucasians and Japanese; less severe than SJS/TEN but significant

MECHANISM
  HLA proteins present drug-peptide complexes to T cells.
  In wrong HLA allele context: off-target immune activation → drug reaction.
  Highly allele-specific: even nearby HLA alleles don't carry the same risk.
```

---

## Pharmacogenomics of Drug Targets

```
TARGET GENE VARIANTS → ALTERED DRUG RESPONSE
──────────────────────────────────────────────

VKORC1 (vitamin K epoxide reductase)
  Warfarin target: VKORC1 + CYP2C9 together explain ~50% of warfarin dose variability
  VKORC1 -1639G>A: ↓VKORC1 expression → more sensitive to warfarin → ↓dose needed
  Genotype-guided dosing algorithm: FDA label, several clinical trials
  Validated warfarin dosing: uses VKORC1 + CYP2C9 + CYP4F2 + clinical factors

CFTR (cystic fibrosis)
  Specific CFTR mutations determine which modulator drug works:
    F508del (most common, ~70%): elexacaftor/tezacaftor/ivacaftor (Trikafta)
    G551D: ivacaftor (Kalydeco) was the first precision CF drug
    Class I mutations (stop codons): ataluren (not yet FDA approved)
  CF is the model for genotype-directed precision therapy

SCN1A (voltage-gated Na+ channel)
  Dravet syndrome: SCN1A loss-of-function mutations → severe childhood epilepsy
  Na+ channel blockers (carbamazepine, lamotrigine, phenytoin): WORSEN Dravet
  → Contraindicated if SCN1A mutation confirmed

BRCA1/BRCA2 (DNA repair)
  Germline BRCA1/2 mutations → hereditary breast/ovarian cancer
  Pharmacogenomic implication: PARP inhibitors (olaparib, rucaparib, niraparib)
  Work by synthetic lethality: BRCA-deficient cells cannot repair PARP-inhibited damage.
  Only effective (approved) in tumors with BRCA mutation (germline or somatic).

EGFR (epidermal growth factor receptor)
  NSCLC EGFR mutations (exon 19 del, L858R): predict response to osimertinib
  T790M resistance mutation: acquired; detect in ctDNA → switch to osimertinib
  KRAS G12C, ALK fusions: predict response to sotorasib, alectinib respectively
```

---

## Engineering Bridge: Pharmacogenomics as Runtime Configuration

Pharmacogenomics is the biological equivalent of hardware capability detection and feature-flag-gated deployment.

```
  PHARMACOGENOMICS              SOFTWARE / HARDWARE PARALLEL
  ──────────────────────────────────────────────────────────────────────
  CYP genotype                  Hardware capability profile:
    CYP2D6 *1/*1 (EM)           → Standard CPU with full clock speed
    CYP2D6 *4/*4 (PM)           → Deprecated hardware: drug accumulates,
                                   increase toxicity risk
    CYP2D6 *1×N (UM)            → Overclocked: drug eliminated too fast,
                                   underdosing at standard dose
  Genotyping ≡ running CPUID instruction before drug deployment.

  CPIC lookup table             Compatibility matrix / feature flag lookup:
  (gene × drug → action)        Given (CYP2C19, clopidogrel) → reduce dose
                                or switch drug. This is exactly a capability
                                matrix: capability × workload → recommended
                                configuration. CPIC is the published spec.

  Pre-emptive PGx panel in EHR  Capability manifest stored at deploy time:
  (genotype once, use at any Rx) Run genotyping once → store in EHR →
                                alert at prescribing time. The manifest is
                                checked at every prescription (deployment)
                                event. No need to re-test.

  Pharmacovigilance signal +    Production incident → post-deploy hotfix:
  PGx retrospective analysis    Adverse event cluster → analyze by genotype →
                                find PGx interaction → update CPIC guideline →
                                add check to prescribing system. Full
                                incident-to-patch cycle.

  HLA-B*5701 screening          Whitelist for hardware compatibility:
  (abacavir, carbamazepine)     HLA-B*5701 allele → severe hypersensitivity
                                to abacavir. Screen before prescribing =
                                compatibility check before enabling feature.
                                HLA-B*1502 → carbamazepine SJS in Han Chinese.

  TPMT / DPYD deficiency        Capacity estimation before heavy workload:
  (thiopurines, 5-FU)           TPMT low/absent → thiopurine toxicity from
                                excess active metabolite. DPYD deficiency
                                → 5-FU neurotoxicity from drug accumulation.
                                Check metabolic capacity before high-demand task.
  ──────────────────────────────────────────────────────────────────────
```

---

## Pre-Emptive Pharmacogenomic Testing

```
PRE-EMPTIVE PGx PANELS
────────────────────────
Concept: Test patient once for a panel of PGx variants.
Store results in EHR. Alert pharmacist/prescriber at point of prescribing.

MAJOR INSTITUTIONS
  Vanderbilt PREDICT program: 1+ million patients genotyped
  Mayo Clinic RIGHT program
  Multiple academic medical centers worldwide

CPIC (Clinical Pharmacogenomics Implementation Consortium)
  Publishes evidence-based guidelines for PGx-drug pairs.
  Tiers: A (actionable) → B (actionable in specific contexts) → C → D
  Free, publicly available: cpicpgx.org

TYPICAL PANEL GENES
  CYP2D6, CYP2C19, CYP2C9, CYP3A5
  VKORC1 (warfarin)
  TPMT/NUDT15 (thiopurines)
  DPYD (fluoropyrimidines)
  HLA-B*57:01 (abacavir), HLA-B*15:02 (carbamazepine)
  G6PD (rasburicase, primaquine)
  SLCO1B1 (statin myopathy)

SLCO1B1 (OATP1B1 TRANSPORTER)
  Transports statins into hepatocytes.
  SLCO1B1 *5 variant: ↓transporter function → ↑plasma statin concentration
  → Higher risk of statin-associated muscle symptoms (SAMS) / myopathy
  Specifically: simvastatin (highest risk), less with atorvastatin/rosuvastatin.
  CPIC guideline: SLCO1B1 *5 → avoid simvastatin ≥40 mg; prefer rosuvastatin/pravastatin.
```

---

## Pharmacogenomics in Oncology: The Tumor Genotype

```
TUMOR (SOMATIC) PHARMACOGENOMICS
──────────────────────────────────
Beyond germline PGx, tumor genomics drives oncology drug selection:

  NEXT-GENERATION SEQUENCING (NGS) PANELS
  FoundationOne CDx, Guardant360, MSK-IMPACT, Tempus
  Sequence tumor DNA → identify actionable mutations
  FDA-approved companion diagnostics for specific drugs

  MUTATION → DRUG (selected)
  BRAF V600E/K → Vemurafenib, dabrafenib (melanoma, thyroid, NSCLC)
  EGFR exon19del/L858R → Erlotinib, gefitinib, osimertinib (NSCLC)
  ALK fusion → Crizotinib, alectinib (NSCLC)
  RET fusion → Selpercatinib, pralsetinib (thyroid, lung)
  KRAS G12C → Sotorasib, adagrasib (NSCLC, CRC)
  NTRK fusion → Larotrectinib, entrectinib (any solid tumor, tumor-agnostic)
  BRCA1/2 mut → Olaparib, rucaparib (breast, ovarian, prostate, pancreatic)
  MSI-H/dMMR → Pembrolizumab (any solid tumor, tumor-agnostic)
  TMB-H → Pembrolizumab (tumor-agnostic, specific ≥10 mut/Mb threshold)
  HER2 amplification → Trastuzumab, pertuzumab, T-DM1, T-DXd

LIQUID BIOPSY (ctDNA)
  Circulating tumor DNA in blood → detect mutations without tissue biopsy.
  Applications:
    Early detection: low-sensitivity but improving (Galleri test)
    Minimal residual disease: detect relapse before clinical symptoms
    Resistance monitoring: detect T790M, BCR-ABL mutations as they emerge
    Tumor heterogeneity: sample is mix of all clones, not single biopsy site
```

---

## Decision Cheat Sheet

| Drug | PGx Test | Action If Variant Present |
|------|---------|--------------------------|
| Abacavir | HLA-B*57:01 | Do NOT use if positive |
| Carbamazepine (Asian patients) | HLA-B*15:02 | Avoid; use alternative |
| Clopidogrel | CYP2C19 PM status | Use prasugrel or ticagrelor |
| Warfarin | CYP2C9 + VKORC1 | Genotype-guided dose algorithm |
| Codeine | CYP2D6 UM/PM | UM: avoid (overdose risk); PM: no effect |
| Azathioprine/6-MP | TPMT | Low activity: dose reduce 90% |
| Irinotecan (high-dose) | UGT1A1*28 | Dose reduce if homozygous |
| 5-FU/capecitabine | DPYD | Dose reduce or avoid if deficient |
| Simvastatin ≥40 mg | SLCO1B1*5 | Switch to rosuvastatin or pravastatin |
| Clozapine patient smoking | CYP1A2 induction | Monitor levels; adjust dose |

---

## Common Confusion Points

**"If we can genotype everyone, why not use PGx for all drugs?"**
CPIC grades evidence: most drugs have insufficient evidence for routine PGx-based dosing. The gene-drug pairs with strong evidence are a minority. Also, most drug response variance is NOT explained by genetics — disease severity, comedications, organ function, adherence, and patient age matter more for most drugs. PGx fills a specific niche of high-impact decisions.

**"The HLA tests seem like they just avoid drugs — is PGx mostly about avoiding toxicity?"**
Dual purpose: avoid toxicity (HLA, TPMT, DPYD) AND optimize efficacy (CYP2D6 for codeine/tamoxifen, CYP2C19 for clopidogrel). The safety angle gets more attention because "patient nearly died" is a more compelling story than "patient's antidepressant was underdosed." Efficacy PGx is equally important but less visible.

**"ctDNA tests say they can detect cancer early — are they ready for screening?"**
Emerging but not yet standard. The GRAIL Galleri test detects cancer signal across 50+ cancer types from a blood draw — FDA approved for high-risk individuals, not general population screening. Sensitivity is lower for early-stage tumors (most important to detect). Specificity requires validation. False positives have costs (imaging, biopsy, anxiety). The technology is improving rapidly; population-level screening is likely in the 2030s with better evidence.
