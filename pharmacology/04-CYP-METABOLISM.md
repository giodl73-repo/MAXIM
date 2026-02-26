# CYP450 Metabolism and Drug Interactions

## The Big Picture

The cytochrome P450 (CYP) enzyme family is the primary metabolic system for drugs. CYP enzymes are the source of most clinically significant drug-drug interactions (DDIs) and the target of pharmacogenomic variation that explains why patients respond differently to the same drug.

```
+──────────────────────────────────────────────────────────────────+
|                  CYP450 SYSTEM LANDSCAPE                         |
|                                                                  |
|  LOCATION                                                        |
|  Primarily liver (hepatocytes), also intestine, lung, brain      |
|                                                                  |
|  MECHANISM                                                        |
|  Drug (substrate) + O₂ + NADPH + CYP → oxidized drug + H₂O     |
|  (monooxygenation: inserts one oxygen atom into the drug)        |
|                                                                  |
|  WHY IT MATTERS                                                  |
|  ~90% of clinically used drugs are CYP substrates               |
|  DDIs via CYP: 20-30% of adverse drug reactions                  |
|  Genetic variants in CYP: explain 15-25% of drug response       |
|                                                                  |
|  CYP NOMENCLATURE                                                |
|  CYP[family][subfamily][isoform]                                  |
|  CYP3A4 = family 3, subfamily A, isoform 4                      |
|  Clinically relevant: CYP3A4, CYP2D6, CYP2C9, CYP2C19, CYP1A2  |
+──────────────────────────────────────────────────────────────────+
```

---

## The Major CYP Enzymes

```
CYP3A4 / CYP3A5
─────────────────
  Fraction of drugs: ~50% of all drugs (highest)
  Location: liver AND gut wall (important for first-pass)
  Substrate examples:
    Statins: simvastatin, lovastatin (NOT pravastatin, rosuvastatin)
    Calcium channel blockers: amlodipine, diltiazem, verapamil
    Immunosuppressants: cyclosporine, tacrolimus, sirolimus
    HIV drugs: most protease inhibitors and NNRTIs
    Benzodiazepines: triazolam, midazolam (NOT diazepam→CYP2C19)
    Opioids: fentanyl, oxycodone (NOT morphine)
    Antibiotics: clarithromycin, erythromycin (NOT azithromycin)
  Key inhibitors: grapefruit juice, ketoconazole, ritonavir
  Key inducers: rifampin, carbamazepine, St. John's Wort

CYP2D6
───────
  Fraction of drugs: ~25%
  Genetic variants: most polymorphic CYP enzyme (see below)
  Substrate examples:
    Antidepressants: fluoxetine, paroxetine, tricyclics
    Antipsychotics: haloperidol, risperidone, aripiprazole
    Opioids: codeine → morphine (activation!), tramadol
    Antiarrhythmics: flecainide, propafenone
    Beta-blockers: metoprolol, carvedilol, propranolol
  Key inhibitors: fluoxetine, paroxetine (self-inhibiting!) quinidine
  NO major inducers (unusual among CYPs)

CYP2C9
───────
  Fraction of drugs: ~15%
  Substrate examples:
    NSAIDs: ibuprofen, naproxen, celecoxib
    Anticoagulants: warfarin (S-enantiomer), acenocoumarol
    Antiepileptics: phenytoin (narrow TI!)
    Oral hypoglycemics: glipizide, glimepiride
  Key inhibitors: fluconazole, amiodarone, metronidazole
  Key inducers: rifampin, carbamazepine (induce this too)

CYP2C19
────────
  Fraction of drugs: ~10%
  Substrate examples:
    PPIs: omeprazole, lansoprazole, pantoprazole (major route)
    Antiplatelet: clopidogrel (prodrug → activation by CYP2C19!)
    Benzodiazepines: diazepam, clobazam
    Antifungals: voriconazole
    Antidepressants: escitalopram, citalopram
  Key inhibitors: omeprazole (self-inhibiting), fluconazole
  Key inducers: rifampin

CYP1A2
───────
  Fraction of drugs: ~5%
  Substrate examples:
    Xanthines: theophylline, caffeine
    Antipsychotics: clozapine, olanzapine (narrow TI for clozapine)
    Anticoagulants: warfarin (R-enantiomer, minor)
  Key inhibitors: ciprofloxacin, fluvoxamine, cimetidine
  Key inducers: smoking (tobacco), charbroiled meat, omeprazole
```

---

## Inhibition: Mechanism and Clinical Impact

```
CYP INHIBITION → SUBSTRATE CONCENTRATION INCREASES
────────────────────────────────────────────────────

REVERSIBLE INHIBITION (competitive)
  Inhibitor competes with substrate for active site.
  Effect immediate; reverses when inhibitor cleared.
  Magnitude: depends on Cinhib / Ki ratio.
  Quantified by DDI ratio = AUC_with / AUC_without

  AUC ratio = 1 + [I] / Ki    (simple competitive model)

  Example: Ketoconazole inhibits CYP3A4.
    If simvastatin is CYP3A4 substrate:
    Cmax of simvastatin ↑ 15-20×!
    Risk: severe myopathy/rhabdomyolysis.
    Clinical decision: contraindicated combination.

MECHANISM-BASED (IRREVERSIBLE) INHIBITION
  Inhibitor is activated by CYP to form reactive intermediate.
  Intermediate covalently binds and inactivates the enzyme.
  Effect is delayed (needs multiple doses) but long-lasting.
  Recovery requires new CYP synthesis (days to weeks).

  Examples:
    Erythromycin: nitroso intermediate binds CYP3A4
    Diltiazem, verapamil: mechanism-based CYP3A4 inhibitors
    Ritonavir: potent mechanism-based CYP3A4 inhibitor
    → Ritonavir "boosting": deliberately uses CYP3A4 inhibition
       to increase levels of other HIV drugs (lopinavir/ritonavir)

  Time course of inhibition recovery:
    After stopping erythromycin: DDI lasts 1-2 weeks.
    After stopping amiodarone (mechanism-based CYP2D6 + 2C9):
    Effects last months (drug has 40-day half-life + irreversible).
```

---

## Induction: Mechanism and Clinical Impact

```
CYP INDUCTION → SUBSTRATE CONCENTRATION DECREASES
────────────────────────────────────────────────────
Inducer activates nuclear receptors (PXR, CAR, AhR) which upregulate
CYP transcription → more enzyme → faster substrate metabolism.

ONSET: Gradual (enzyme synthesis takes days).
  Full effect: 1-2 weeks.
  Offset after stopping inducer: 1-2 weeks.

CLINICAL CONSEQUENCE: Therapeutic failure

  EXAMPLE: Rifampin (potent CYP3A4 inducer)
    Patient on oral contraceptive (ethinyl estradiol, CYP3A4 substrate)
    Starts rifampin for TB treatment
    → Estrogen metabolism ↑ → plasma levels drop → contraceptive failure
    → Pregnancy despite "taking the pill"
    Management: use backup contraception; switch to non-hormonal method.

  EXAMPLE: St. John's Wort (OTC herbal, CYP3A4 inducer)
    Patient on cyclosporine (immunosuppressant, CYP3A4 substrate)
    Starts St. John's Wort for depression
    → Cyclosporine levels fall → rejection episode in transplant patient
    This has caused documented organ rejections.

KEY INDUCERS (remember these)
  Rifampin    — strongest; CYP3A4, CYP2C9, CYP2C19, P-gp
  Carbamazepine — anticonvulsant; induces CYP3A4 and its OWN metabolism
  Phenytoin   — anticonvulsant; strong CYP3A4 inducer
  St. John's Wort — OTC herbal; patients don't disclose!
  Dexamethasone — high-dose steroid; weak-moderate CYP3A4 induction
  Smoking     — CYP1A2 induction (clozapine dose doubles in smokers)
```

---

## CYP Polymorphisms

```
GENETIC VARIANTS IN CYP ENZYMES
─────────────────────────────────
CYP2D6: Most variable. 100+ alleles described.

  Phenotype           CYP2D6 genotype              Prevalence
  ─────────────────   ──────────────────────────   ──────────────────────
  Poor metabolizer    2 loss-of-function alleles   5-10% Europeans/Asians
                                                   1-2% Africans
  Intermediate        1 functional + 1 null        30-40% of population
  Extensive (normal)  2 functional alleles         ~50% Europeans
  Ultrarapid          Gene duplication (>2 copies) 1-7% Europeans
                                                   10-30% North Africans

CLINICAL CONSEQUENCES OF CYP2D6 POLYMORPHISM

  CODEINE → MORPHINE (via CYP2D6)
    Poor metabolizer: codeine has NO analgesic effect (cannot convert)
    Ultrarapid: codeine → excess morphine → TOXICITY
    Fatal case: breastfeeding mother who was ultrarapid CYP2D6;
    infant died of morphine toxicity from breast milk.
    FDA warning: ultrarapid CYP2D6 metabolizers should not use codeine.

  ANTIDEPRESSANTS
    Poor metabolizer: standard doses → toxic concentrations of TCAs/fluoxetine
    Ultrarapid: standard doses → subtherapeutic → treatment failure
    CYP2D6 genotyping can guide antidepressant selection.

CYP2C19 POLYMORPHISM
  ~20% Asians, 2-5% Caucasians are poor CYP2C19 metabolizers.

  CLOPIDOGREL (prodrug → active thienopyridine via CYP2C19)
    Poor metabolizer: clopidogrel not activated → no antiplatelet effect
    → Stent thrombosis despite "antiplatelet therapy"
    FDA Black Box Warning: genotype patients if high cardiovascular risk.
    Alternative: prasugrel, ticagrelor (not CYP2C19 dependent).

  PPIs
    Poor metabolizers have higher PPI levels → better acid suppression
    → Actually beneficial for H. pylori eradication.

CYP2C9 POLYMORPHISM
  Poor metabolizers: reduced warfarin dose required.
  VKORC1 + CYP2C9 genotyping → pharmacogenomic warfarin dosing algorithm.
```

---

## Phase II Enzymes: UGT, NAT, TPMT

```
UDP-GLUCURONOSYLTRANSFERASE (UGT)
──────────────────────────────────
  Adds glucuronic acid to drug → water-soluble conjugate → excreted.
  UGT1A1: bilirubin conjugation; Gilbert's syndrome (reduced UGT1A1 activity)

  IRINOTECAN (colon cancer):
    Prodrug → SN-38 (active, toxic) by carboxylesterase
    SN-38 → SN-38-glucuronide (inactive) by UGT1A1
    UGT1A1*28 (Gilbert's polymorphism): reduced UGT1A1 → SN-38 accumulates
    → Severe diarrhea and neutropenia at standard doses.
    FDA label includes UGT1A1 genotype recommendation for dose reduction.

N-ACETYLTRANSFERASE (NAT2)
  Acetylates drugs including isoniazid, hydralazine, procainamide.
  Slow acetylators vs fast acetylators (bimodal distribution).
  ~50% of Caucasians are slow acetylators; ~10% of Japanese.

  ISONIAZID (TB treatment):
    Slow acetylator: higher isoniazid levels → higher risk of peripheral neuropathy
    Fast acetylator: lower isoniazid levels + more acetylhydrazine (hepatotoxic)
    Management: supplement B6 in slow acetylators; monitor LFTs in fast.

THIOPURINE METHYLTRANSFERASE (TPMT)
  Inactivates thiopurines (azathioprine, 6-mercaptopurine, thioguanine).
  1/300 people have very low or no TPMT activity.
  Low TPMT: active drug accumulates → severe myelosuppression.
  Standard practice: test TPMT before starting azathioprine in IBD, transplant.
```

---

## Clinical Decision Framework for DDIs

```
DDI RISK ASSESSMENT
──────────────────────

Step 1: Identify if either drug is a CYP substrate, inhibitor, or inducer.
Step 2: Match CYP enzyme (3A4? 2D6? 2C9?).
Step 3: Estimate magnitude:
         Weak inhibitor: AUC change <2×
         Moderate:       2-5× AUC change
         Strong:         >5× AUC change
Step 4: Assess clinical consequence:
         Narrow TI substrate? → High risk
         Wide TI substrate? → Usually manageable
Step 5: Choose action:
         Contraindicated / Avoid / Use with caution + monitoring / Acceptable

DDI MATRIX (selected)
  Inhibitor    Substrate(s)              Clinical consequence
  ──────────── ────────────────────────  ───────────────────────────────
  Ketoconazole Simvastatin, tacrolimus   10-20× AUC → rhabdomyolysis, nephrotoxicity
  Fluoxetine   Tamoxifen (→ active met)  ↓ Active metabolite → therapy failure
  Rifampin     Oral contraceptives       Contraceptive failure
  Ritonavir    Most HIV PI/NNRTI         Used intentionally to boost drug levels
  Ciprofloxacin Clozapine, theophylline  1A2 inhibition → toxicity
  Amiodarone   Warfarin, digoxin        Bleeding, digoxin toxicity
```

---

## Decision Cheat Sheet

| Situation | CYP Question | Action |
|-----------|-------------|--------|
| Starting new drug with warfarin patient | Is it CYP2C9 inhibitor or inducer? | Check; adjust warfarin dose + INR |
| Statin not working at usual dose | Is patient on CYP3A4 inducer (rifampin)? | Increase statin dose or switch to pravastatin |
| Transplant patient starting new antibiotic | Is antibiotic CYP3A4 inhibitor? (erythromycin, clarithromycin) | Use azithromycin instead or monitor cyclosporine |
| Clopidogrel patient needing PPI | Is omeprazole CYP2C19 inhibitor? | Use pantoprazole instead |
| Patient taking codeine with no analgesia | CYP2D6 poor metabolizer? | Consider alternative opioid (not tramadol) |
| Clozapine patient starts smoking | CYP1A2 induced by tobacco? | Expect drop in clozapine levels → may need dose ↑ |

---

## Common Confusion Points

**"Ritonavir is an HIV drug being used to block CYP metabolism — why is that intentional?"**
Ritonavir is a potent, irreversible CYP3A4 inhibitor. HIV protease inhibitors are CYP3A4 substrates with poor oral bioavailability. Pairing any protease inhibitor with low-dose ritonavir "boosts" the partner drug's levels 5-20× — making dosing practical. In modern regimens, cobicistat (no antiviral activity, pure CYP inhibitor) is often used instead.

**"How can a drug inhibit its own metabolism?"**
Mechanism-based inhibitors become activated by CYP and then inactivate it. If the drug is also the substrate, it inhibits its own pathway. Example: fluoxetine and paroxetine are both CYP2D6 substrates AND CYP2D6 inhibitors. Over time, they inhibit their own metabolism → plasma levels rise over weeks of dosing (nonlinear kinetics).

**"CYP genotyping sounds important — why don't all patients get it?"**
Cost and limited actionability for most drugs. For a few drugs (warfarin, clopidogrel, codeine, irinotecan, thiopurines), genotyping is clinically validated and actionable. For most drugs, empirical dose titration is more practical than genotyping every patient. As costs drop (whole-genome sequencing), pre-emptive pharmacogenomic panels (test once, use lifetime) are becoming standard.
