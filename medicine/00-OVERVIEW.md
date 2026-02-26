# 00 — Medicine & Pharmacology Overview

## PK/PD, Drug Development, Regulatory, Special Populations

---

<!-- @editor[bridge/P2]: No CS/systems bridge -- PK/PD maps to control theory (input/output/feedback/steady-state convergence); ADME is a pipeline with transforms at each stage; therapeutic index is a safety margin like numerical stability bounds -->
<!-- @editor[diagram/P2]: Diagram lists items but does not show relationships -- rework as layered system view showing PK-to-PD flow, feedback loops, and how drug classes connect to core concepts -->

## Big Picture: The Drug Landscape

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    PHARMACOLOGY FRAMEWORK                                │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PHARMACOKINETICS (PK)          PHARMACODYNAMICS (PD)                   │
│  "what the body does to drug"   "what drug does to body"                │
│                                                                          │
│  A — Absorption                 Receptor binding                        │
│  D — Distribution               Dose-response curve                     │
│  M — Metabolism                 Therapeutic index                       │
│  E — Elimination                Agonism / antagonism                    │
│                                                                          │
│  ──────────────────────────────────────────────────────────             │
│                                                                          │
│  DRUG DEVELOPMENT PIPELINE                                               │
│                                                                          │
│  Target → Lead → Preclinical → Phase I → Phase II → Phase III → NDA    │
│                                                                          │
│  ──────────────────────────────────────────────────────────             │
│                                                                          │
│  DRUG CLASS MODULES IN THIS DIRECTORY:                                  │
│  01 Antibiotics   02 Antivirals/Vaccines   03 Cardiovascular            │
│  04 CNS           05 Endocrine/Metabolic   06 Cancer                    │
│  07 Immunomodulators  08 Respiratory/GI   09 Anesthesia                 │
│  10 Diagnostics/Imaging                                                  │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Pharmacokinetics — ADME

### Absorption

```
Routes and bioavailability (F):
  IV:     F = 100% (definition)
  IM/SC:  F = 75–100% (bypasses gut)
  PO:     Variable; limited by:
    ├── GI absorption (solubility, permeability, transporters)
    ├── Gut wall metabolism (CYP3A4 in enterocytes)
    └── First-pass hepatic metabolism (portal circulation → liver)

First-pass effect:
  PO drug → portal vein → liver → CYP metabolism before systemic circulation
  High first-pass drugs need large PO dose or alternative route
  Examples: nitroglycerin (SL), morphine (IV > PO), lidocaine (IV only),
            testosterone (injectable/transdermal — extensive gut/liver metabolism)

Bioavailability calculation:
  F = AUC_oral / AUC_IV   (area under concentration-time curve)

Henderson-Hasselbalch and absorption:
  Weak acids (pKa~4): stomach (pH 2) → mostly unionized → well-absorbed
  Weak bases (pKa~8): intestine (pH 6–7) → mostly unionized → absorbed
  Ionized form: water-soluble, cannot cross membranes
```

### Distribution

```
Volume of distribution (Vd):
  Vd = Amount of drug in body / Plasma concentration
  Units: liters (or L/kg)

  Vd = plasma volume (~3L)          → stays in blood (heparin, proteins)
  Vd = ECF (~12–14L)                → polar, doesn't enter cells
  Vd = TBW (~42L)                   → crosses into cells
  Vd >> 42L (100s–1000s L)          → extensive tissue binding (chloroquine, amiodarone)

Protein binding:
  Albumin: binds acidic drugs (warfarin, phenytoin, NSAIDs)
  α1-acid glycoprotein (AGP): binds basic drugs (lidocaine, propranolol)
  Only free (unbound) drug is pharmacologically active
  Displacement interactions (e.g., warfarin displaced by NSAIDs) → transient ↑ free drug

Blood-brain barrier (BBB) penetration:
  Requires: lipophilicity, small MW, low protein binding, not P-gp substrate
  P-glycoprotein (MDR1): efflux pump at BBB; substrate drugs excluded
  Inflammation (meningitis) can disrupt BBB → allows penetration of normally excluded drugs
```

### Metabolism

```
Phase I reactions: oxidation/reduction/hydrolysis
  CYP450 enzymes (liver microsomes — ER membrane):
    CYP3A4: ~50% of drugs; inducible by rifampin, carbamazepine, St. John's wort
    CYP2D6: codeine → morphine; polymorphic (UM/EM/IM/PM)
    CYP2C9: warfarin, phenytoin, NSAIDs
    CYP2C19: omeprazole, clopidogrel (prodrug activation); PM = ~15% Asians
    CYP1A2: theophylline, caffeine; induced by smoking

Phase II reactions: conjugation (glucuronidation/sulfation/acetylation/glutathione)
  Make drug more water-soluble → renal/biliary excretion
  UDP-glucuronosyltransferases (UGTs) most important
  N-acetyltransferase (NAT2): INH, hydralazine, procainamide; polymorphic (fast/slow acetylators)

Prodrugs require metabolism for activation:
  Clopidogrel → active thiol (CYP2C19); PMs don't respond
  Codeine → morphine (CYP2D6); UMs → toxic morphine levels
  Enalapril → enalaprilat (esterases)
  Valacyclovir → acyclovir (gut/liver esterases)
```

### Elimination

```
Renal clearance:
  CLrenal = GFR × fu − Treabsorption + Tsecretion
  (fu = unbound fraction; tubular secretion via OAT/OCT transporters)
  Drugs eliminated renally: dose-reduce in CKD (metformin, digoxin, aminoglycosides)

Half-life (t½):
  t½ = 0.693 × Vd / CL
  Time to steady state: 4–5 × t½
  Time to elimination: ~4–5 × t½ (97% eliminated at 5 × t½)

Steady-state concentration:
  Css = Dose rate / (CL)    (for continuous infusion)
  Css = F × Dose / (CL × τ) (for multiple dosing, τ = dosing interval)
  Depends only on clearance and dosing rate — NOT on Vd

Zero-order vs first-order kinetics:
  First-order (most drugs): rate ∝ concentration → constant t½, predictable
  Zero-order (saturable): constant rate regardless of concentration
    Alcohol, phenytoin, salicylates (at high doses)
    → Small dose increase → large plasma concentration increase → toxicity
```

---

## 2. Pharmacodynamics

### Receptor Types

```
G protein-coupled receptors (GPCRs): 7-TM domains
  Gs → ↑ adenylyl cyclase → ↑ cAMP (β-adrenergic, glucagon, TSH)
  Gi → ↓ adenylyl cyclase → ↓ cAMP (α2-adrenergic, opioids, M2)
  Gq → ↑ PLCβ → ↑ IP3/DAG → ↑ Ca²⁺ (α1, M1/M3, H1, AT1)

Ion channel receptors (ligand-gated): fastest response (ms)
  nAChR, GABA-A, NMDA, 5-HT3 — direct ion flow

Receptor tyrosine kinases (RTKs): dimerization → autophosphorylation → cascade
  Insulin, EGF, PDGF, IGF-1 receptors

Nuclear receptors: transcription factor activation (hours-days)
  Steroids (GR, MR, ER, AR), thyroid hormones, retinoic acid, vitamin D
```

### Dose-Response Concepts

```
Log-dose vs response curve (sigmoidal):

     100% ─────────────────────── Emax
      │                     ╱───────────
  %  │                   ╱
  R  │                ╱
  e  50% ─────────╱
  s  │         ╱   ↑ EC50
  p  │      ╱
  o  │   ╱
  n  │╱
  s  0%
  e       ──────────────────── log[dose]

EC50: concentration producing 50% maximal effect
Emax: maximum possible effect
Potency: EC50 comparison (lower EC50 = more potent)
Efficacy: Emax comparison (which drug can produce greater maximal effect)

Therapeutic index (TI) = TD50 / ED50
  (median toxic dose / median effective dose)
  Wide TI: penicillin (very safe)
  Narrow TI: digoxin, warfarin, lithium, aminoglycosides, phenytoin, theophylline
  → Narrow TI drugs require monitoring (drug levels)
```

### Agonist Types

```
Full agonist: activates receptor to full Emax (morphine at μ-receptor)
Partial agonist: activates but submaximal Emax (buprenorphine at μ)
  In presence of full agonist: acts as functional antagonist (competitive partial agonist)
Inverse agonist: reduces constitutive activity below baseline (some antihistamines)
Competitive antagonist: blocks receptor, reversible — shifts dose-response right
  (Km ↑, Emax unchanged with enough agonist)
Non-competitive antagonist: reduces Emax (irreversible or allosteric binding)
Allosteric modulator: changes receptor conformation without binding orthosteric site
  Positive: BZDs at GABA-A (↑ Cl⁻ flux frequency)
  Negative: some mGluR modulators
```

---

## 3. Drug-Drug Interactions

```
PHARMACOKINETIC INTERACTIONS:

CYP inducers → ↓ substrate plasma levels (↓ efficacy):
  Rifampin, carbamazepine, phenytoin, phenobarbital, St. John's wort, efavirenz, smoking
  Examples: rifampin + warfarin → ↑ warfarin dose needed
            St. John's wort + oral contraceptives → contraception failure

CYP inhibitors → ↑ substrate plasma levels (↑ toxicity):
  Azole antifungals (ketoconazole > itraconazole >> fluconazole): CYP3A4
  Macrolides (erythromycin/clarithromycin, NOT azithromycin): CYP3A4
  Grapefruit juice: CYP3A4 irreversible inhibition in gut wall
  Fluoxetine/paroxetine: CYP2D6 inhibition
  Amiodarone: CYP2C9/3A4 inhibition → ↑ warfarin → bleeding
  Examples: statins + azoles → myopathy; tacrolimus + azoles → nephrotoxicity

PHARMACODYNAMIC INTERACTIONS:

Synergy: combined effect > sum of individual effects
  BZD + alcohol → CNS/respiratory depression (↑ mortality)
  Aminoglycoside + β-lactam → bactericidal synergy

Antagonism: combined effect < sum
  Naloxone reverses opioid → functional antagonism
  Vitamin K reverses warfarin at level of GC receptor (PD antagonism)
```

---

## 4. Drug Development Pipeline

```
TARGET IDENTIFICATION
  Genomics (GWAS), proteomics, phenotypic screening → biological target
  CRISPR validation: knock out gene → confirm phenotype reversal

LEAD DISCOVERY
  HTS (high-throughput screening) of compound libraries
  Fragment-based discovery (FBDD): small fragments → elaborated
  Structure-based design: X-ray/cryo-EM of target → rational design

PRECLINICAL STUDIES
  In vitro: cell-based assays, SAR (structure-activity relationship)
  In vivo: animal models (rodent/primate) → PK, toxicology, ADME
  IND application → FDA permission to start clinical testing

PHASE I (safety/PK, ~20–80 healthy volunteers)
  Single ascending dose (SAD) → multiple ascending dose (MAD)
  PK parameters, MTD (maximum tolerated dose), dose selection for Ph II
  Oncology: patients (not healthy volunteers); starting at 1/10th toxic dose

PHASE II (efficacy/dose, ~100–300 patients)
  Proof-of-concept; dose-ranging; early efficacy signal
  ~60–70% of drugs that reach Phase II fail here

PHASE III (confirmatory RCT, ~1000–10,000 patients)
  Randomized, controlled, often double-blind, multi-center
  Powered for primary endpoint (regulatory approval threshold)
  ~25% of drugs that reach Phase III fail

NDA/BLA SUBMISSION (NDA = small molecule; BLA = biologic)
  FDA review: 10–12 months standard; priority/accelerated review: 6 months
  Advisory committee meetings for controversial approvals

PHASE IV (post-marketing surveillance)
  Pharmacovigilance, safety signals in real-world populations
  REMS (Risk Evaluation and Mitigation Strategy) for high-risk drugs
  Black box warnings can be added based on Phase IV signals
```

---

## 5. Regulatory Pathways

```
STANDARD APPROVAL: full efficacy + safety data from clinical trials
ACCELERATED APPROVAL (Subpart H): surrogate endpoint (biomarker likely to predict outcome)
  Requires post-market confirmatory trial; withdrawal if fails
  Examples: many cancer drugs (tumor response rate → survival assumed)
BREAKTHROUGH THERAPY DESIGNATION: FDA intensive guidance; faster review
FAST TRACK: rolling review; frequent FDA interaction
PRIORITY REVIEW: 6-month goal vs 10-month standard (serious condition + unmet need)
ORPHAN DRUG DESIGNATION: diseases affecting <200,000 in US
  Benefits: 7-year market exclusivity, tax credits, waived fees

BIOSIMILARS (Biologics Price Competition + Innovation Act 2009):
  Highly similar biologic with no clinically meaningful differences
  Interchangeable biosimilar: pharmacist can substitute without prescriber consult
  Not automatically substitutable (complex structure, immunogenicity variability)
  Examples: adalimumab biosimilars (humira → Hadlima/Hyrimoz)

GENERIC DRUGS (Hatch-Waxman 1984):
  Bioequivalent to brand (same dosage form, strength, route, rate/extent of absorption)
  Require Abbreviated NDA (ANDA) — no full clinical trials
  Bioequivalence: 90% CI of AUC and Cmax ratios within 80–125% of reference
```

---

## 6. Special Populations

### Renal Dosing

```
CKD dose adjustments needed when:
  Drug primarily renally cleared (>30% unchanged in urine)
  Drug has renally cleared active/toxic metabolites
  Drug causes nephrotoxicity (aminoglycosides, NSAIDs, amphotericin B)

GFR estimation: CKD-EPI (more accurate than Cockcroft-Gault for modern use)
Cockroft-Gault: CrCl = (140-age) × weight / (72 × SCr) × 0.85 (if female)

High-risk drugs in CKD: NSAIDs (worsen GFR, Na retention, ↑ K), metformin (lactic acidosis),
  direct oral anticoagulants (dabigatran >95% renal), aminoglycosides, contrast agents
```

### Hepatic Dosing

```
Child-Pugh score (5–15 points): bilirubin, albumin, INR, ascites, encephalopathy
  Child A (5–6): mild; minimal dose change usually needed
  Child B (7–9): moderate; reduce dose of extensively metabolized drugs
  Child C (10–15): severe; avoid hepatotoxic drugs; protein-bound drugs altered

Drugs requiring hepatic dose reduction:
  High first-pass drugs (morphine, verapamil, propranolol) → ↑ oral bioavailability in cirrhosis
  Coagulation factor synthesis ↓ → ↑ warfarin effect
```

### Pregnancy

```
FDA Pregnancy Labeling (PLLR, replaced old A/B/C/D/X categories 2015):
  Now narrative: fetal risk summary, clinical considerations, data sections

Safe in pregnancy (general):
  Antibiotics: penicillins, cephalosporins, azithromycin, clindamycin
  Insulin (preferred over oral agents for DM in pregnancy)
  Thyroid replacement (levothyroxine)
  Heparin/LMWH (warfarin crosses placenta → teratogenic)

Contraindicated in pregnancy:
  Warfarin (embryopathy weeks 6–12; intracranial hemorrhage in fetus)
  ACE inhibitors/ARBs (2nd/3rd trimester: fetal renal agenesis, oligohydramnios)
  Statins (↓ fetal cholesterol synthesis → organogenesis disruption)
  Methotrexate (antifolate → NTDs, fetal death)
  Thalidomide, isotretinoin, valproate, tetracyclines (teeth/bone)
  NSAIDs (3rd trimester → premature ductus closure)
```

### Pediatric PK

```
Neonates: immature CYP enzymes → ↑ drug exposure (especially CYP1A2/2D6/3A4)
  Glucuronidation (UGT) immature → chloramphenicol gray baby syndrome
Infants: CYP3A7 → CYP3A4 transition; enzyme activity may exceed adults by year 1–2
Children: weight-based dosing (mg/kg); volume of distribution differs (↑ body water fraction)
  Higher renal clearance per kg → may need higher mg/kg dosing for some drugs

Contraindicated in children:
  Aspirin (<12yr): Reye syndrome (hepatic encephalopathy with viral illness)
  Tetracyclines (<8yr): tooth discoloration, bone growth inhibition
  Fluoroquinolones (<18yr general guidance): cartilage toxicity in animal models
  (FQ exceptions: anthrax/plague prophylaxis, or no alternatives)
```

### Elderly

```
Beers Criteria (AGS): lists drugs to avoid/use-with-caution in adults ≥65
  Physiological changes:
  ↓ GFR → ↑ renally cleared drug levels
  ↓ Hepatic blood flow → ↑ first-pass → ↑ oral bioavailability of high-EP drugs
  ↑ Body fat / ↓ lean mass → ↑ Vd for lipophilic drugs (BZDs)
  ↓ Albumin → ↑ free fraction of highly protein-bound drugs
  ↑ CNS sensitivity to BZDs, opioids, anticholinergics

Beers list highlights: long-acting BZDs, antihistamines (anticholinergic), tricyclics,
  muscle relaxants, NSAIDs (GI bleed, renal), first-gen antipsychotics (fall/sedation)
```

---

## 7. Drug Naming Conventions

```
STEM SYSTEM (INN — International Nonproprietary Name):
Small molecules:
  −olol   = β-blocker (metoprolol, atenolol, carvedilol)
  −pril   = ACE inhibitor (lisinopril, enalapril, ramipril)
  −sartan = ARB (losartan, valsartan, irbesartan)
  −ipine  = dihydropyridine CCB (amlodipine, nifedipine, felodipine)
  −statin = HMG-CoA reductase inhibitor (atorvastatin, rosuvastatin)
  −floxacin = fluoroquinolone (ciprofloxacin, levofloxacin)
  −cillin = penicillin class (amoxicillin, nafcillin, piperacillin)
  −cycline = tetracycline class (doxycycline, minocycline)
  −azole  = antifungal or PPI (omeprazole, fluconazole — different!)
  −navir  = HIV protease inhibitor (ritonavir, darunavir)
  −vir    = antiviral (acyclovir, ganciclovir, remdesivir)
  −tidine = H2 blocker (famotidine, ranitidine)
  −zosin  = α1 blocker (prazosin, doxazosin, terazosin)

Biologics (monoclonal antibodies):
  Structure: [target/source prefix] + [source infix] + -mab
  Source infix:
    -o-    = mouse (murino-) → fully mouse → high immunogenicity
    -xi-   = chimeric (~25% mouse)
    -zu-   = humanized (~5–10% mouse)
    -u-    = fully human
  Target prefix examples:
    -lim-  = immune (immunomodulatory)
    -cir-  = cardiovascular
    -tu-   = tumor
    -vi-   = viral
  Examples:
    infliXImab: chimeric, anti-TNF (immunomodulatory)
    adalimUmab: fully human, anti-TNF
    trastUZUmab: humanized, anti-HER2 (tumor)
    rituXImab: chimeric, anti-CD20 (tumor/immune)
    pembroliZUmab: humanized, anti-PD-1 (tumor)

  Bispecific: [target1][target2]-[source]-mab (blinatumomab = CD3×CD19)
  ADC: [mAb] + [linker] + [payload]; named like mAb (T-DM1 = trastuzumab-emtansine)
  Fusion proteins: target + immunoglobulin Fc (etanercept = TNFR2-Fc; abatacept = CTLA-4-Fc)

Kinase inhibitors (-nib):
  -tinib  = general kinase inhibitor
  -ciclib = CDK inhibitor (palbociclib)
  -rafenib= RAF inhibitor (vemurafenib)
```

---

## Decision Cheat Sheet

| PK Parameter | What it tells you | Key drugs where it matters |
|-------------|------------------|---------------------------|
| Bioavailability (F) | Fraction reaching systemic circulation | NTG (SL due to F~0 PO), morphine (PO F~20–30%) |
| Vd large (>5 L/kg) | Extensive tissue distribution | Amiodarone (~60 L/kg), chloroquine, digoxin |
| t½ long | Infrequent dosing, slow offset | Amiodarone (40–55 days), amlodipine (35–50h) |
| Narrow TI | Monitoring required | Digoxin, warfarin, lithium, phenytoin, aminoglycosides |
| CYP3A4 substrate | Interaction-prone | Tacrolimus, statins, many HIV drugs |
| Renal eliminated | Dose-reduce in CKD | Dabigatran, metformin, aminoglycosides, digoxin |

---

## Common Confusion Points

**Potency vs efficacy:** Potency = EC50 (how much drug needed for effect). Efficacy = Emax (maximum achievable effect). A partial agonist can be more potent than a full agonist but have lower efficacy. "Efficacy" in clinical trials means "does the drug work" — not the PD definition.

**Vd is not a real volume:** It's a theoretical volume needed to account for the drug if it were uniformly distributed at the measured plasma concentration. Drugs with Vd > 42L are extensively sequestered in tissues.

**Steady state ≠ therapeutic:** Steady state (4–5 t½) means input = output; the concentration may be above or below therapeutic range. Loading doses are used when t½ is long (digoxin, amiodarone) to reach therapeutic concentration faster.

**Phase I metabolism not always "detoxification":** Phase I can generate reactive/toxic intermediates (acetaminophen → NAPQI via CYP2E1). Phase II conjugation usually inactivates. But some Phase II products are toxic (glucuronide of NSAIDs → GI toxicity).

**CYP induction vs inhibition onset:** Inhibition is immediate (rapid rise in substrate levels). Induction requires protein synthesis (days to weeks onset; also days-weeks to wear off after stopping inducer).

**Bioequivalence ≠ therapeutic equivalence:** Two generics bioequivalent to brand are bioequivalent to each other, but this is a population-level statistical statement. For NTI drugs (narrow TI), even 80–125% variation can matter. FDA has tighter requirements for some NTI drugs.
