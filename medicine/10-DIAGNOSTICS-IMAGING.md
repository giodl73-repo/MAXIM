# 10 — Diagnostics & Imaging

## Laboratory Panels, Imaging Physics and Clinical Applications, Diagnostic Reasoning

---

## Big Picture: Diagnostics Stack

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        DIAGNOSTICS FRAMEWORK                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  LABORATORY DIAGNOSTICS                                                 │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  Hematology: CBC + diff — anemia/leukocytosis/thrombocytopenia   │   │
│  │  Metabolic: BMP/CMP — electrolytes, renal function, liver        │   │
│  │  Coagulation: PT/INR (extrinsic), aPTT (intrinsic), d-dimer      │   │
│  │  Cardiac: troponin, BNP, CK-MB (time courses matter)             │   │
│  │  Inflammatory: CRP, procalcitonin, ESR, ferritin                 │   │
│  │  ABG: acid-base + oxygenation interpretation                     │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  IMAGING MODALITIES (physics + clinical)                                │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  X-ray: ionizing; bone/air/soft tissue contrast                  │   │
│  │  CT: Hounsfield units; rapid; excellent detail; radiation dose   │   │
│  │  MRI: T1/T2/DWI/FLAIR; soft tissue; no radiation               │   │
│  │  Ultrasound: real-time; no radiation; bedside POCUS              │   │
│  │  Nuclear/PET: functional imaging; tracers; FDG/sestamibi         │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  DIAGNOSTIC REASONING                                                   │
│   Pre-test probability → test LR → post-test probability (Bayesian)    │
│   Sensitivity vs specificity trade-offs; ROC curves                    │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Complete Blood Count (CBC)

```
WHITE BLOOD CELL (WBC):
  Normal: 4.5-11.0 × 10⁹/L
  Differential:
    Neutrophils 50-70%: bacterial infection (neutrophilia), chemotherapy (neutropenia)
    Lymphocytes 20-40%: viral infections (lymphocytosis), CLL, lymphoma
    Monocytes 2-8%: monocytosis in TB, fungal, monocytic leukemias
    Eosinophils 1-4%: parasites, allergic, drug reactions, eosinophilic disorders
    Basophils 0-1%: rare; IgE-mediated; CML (basophilia)
  Left shift: immature neutrophils (bands/metamyelocytes) → suggests bacterial infection
  Reactive lymphocytes: enlarged, irregular; EBV (infectious mono)

RED BLOOD CELL (RBC) INDICES:
  MCV (Mean Corpuscular Volume) — ANEMIA CLASSIFICATION KEY:
    Microcytic (<80 fL): Iron deficiency (#1), thalassemia, anemia of chronic disease (usually normocytic)
    Normocytic (80-100 fL): ACD, hemolytic, aplastic, early iron/B12 deficiency
    Macrocytic (>100 fL): B12/folate deficiency (megaloblastic), hypothyroidism, liver disease, alcohol, reticulocytosis
  MCHC (Mean Corpuscular Hemoglobin Concentration): elevated in hereditary spherocytosis
  RDW (Red Cell Distribution Width): elevated = mixed population; iron deficiency early + B12 deficiency mix

  Reticulocyte count: assess bone marrow response
    High reticulocyte %: adequate marrow response → hemolysis or acute blood loss
    Low reticulocyte + low Hgb: bone marrow failure, B12/folate/iron deficiency, aplastic

HEMOGLOBIN + HEMATOCRIT:
  Anemia: Hgb <12 (women), <13 (men) g/dL
  Polycythemia: Hgb >16.5 (men), >16 (women); primary (PV) vs secondary (EPO-driven)

PLATELETS:
  Normal: 150-400 × 10⁹/L
  Thrombocytopenia (<150):
    Immune (ITP): isolated; peripheral destruction; test for anti-platelet antibodies
    HIT (Heparin-Induced Thrombocytopenia): 5-10 days after heparin; paradoxically THROMBOTIC
      PF4-heparin antibody → activates platelets → thrombosis; stop ALL heparin; use argatroban
    TTP (Thrombotic Thrombocytopenic Purpura): ADAMTS13 deficiency; microangiopathic hemolytic anemia
      Pentad: fever, low plt, hemolytic anemia, renal failure, neuro changes → PLASMA EXCHANGE STAT
    DIC: consumption; see below
  Thrombocytosis: reactive (iron deficiency, infection, post-splenectomy) vs essential thrombocythemia (ET)
```

---

## 2. Metabolic Panels (BMP/CMP)

```
BASIC METABOLIC PANEL (BMP):
  Na+: 135-145 mEq/L
    Hyponatremia: assess osmolality and volume status → SIADH vs hypothyroid vs adrenal vs redistribution
    Hypernatremia: water deficit; central/nephrogenic DI; hyperaldosteronism
  K+: 3.5-5.0 mEq/L
    Hypokalemia: diarrhea, vomiting, diuretics, hyperaldosteronism, renal tubular acidosis
    Hyperkalemia: renal failure, ACEi/ARBs/potassium-sparing diuretics, adrenal insufficiency, rhabdomyolysis
  Cl-: 95-105 mEq/L; HCO3-: 22-29 mEq/L

ANION GAP: AG = Na - (Cl + HCO3); normal 8-12 mEq/L
  Elevated AG metabolic acidosis (MUDPILES):
    Methanol, Uremia, DKA, Propylene glycol / Paraldehyde, Isoniazid / Iron, Lactic acidosis, Ethanol / Ethylene glycol, Salicylates
  Non-anion gap (hyperchloremic) metabolic acidosis: diarrhea, RTA, early renal failure, carbonic anhydrase inhibitors

BUN/CREATININE + eGFR:
  BUN: 7-25 mg/dL; creatinine: 0.6-1.2 mg/dL (M), 0.5-1.1 (F)
  BUN:Cr ratio >20: pre-renal (dehydration, GI bleed with protein reabsorption)
  eGFR: CKD-EPI formula (best for clinical use); normal >90 mL/min/1.73m²
    CKD stages: G1 (eGFR ≥90), G2 (60-89), G3a (45-59), G3b (30-44), G4 (15-29), G5 (<15)
  Creatinine limitations: muscle mass affects baseline; doesn't rise until ~50% renal function lost

LIVER FUNCTION TESTS (LFTs):
  AST, ALT: hepatocellular damage markers (AST more nonspecific; also cardiac, muscle)
    ALT >3× ULN: drug-induced liver injury threshold (DILI); ALT/AST ratio
    AST:ALT >2:1: alcoholic hepatitis (acetaldehyde depletes pyridoxal-5-phosphate → AST)
  ALP: hepatic canalicular + bone (alkaline phosphatase); elevated in cholestasis + bone disease
    Elevated ALP + elevated GGT → hepatic origin (GGT normal in bone disease)
  GGT: sensitive for hepatic/biliary disease; induced by alcohol; not bone
  Bilirubin: total = direct (conjugated) + indirect (unconjugated)
    Pre-hepatic (indirect bili ↑): hemolysis, Gilbert syndrome
    Hepatic (both ↑): hepatitis, cirrhosis
    Post-hepatic/obstructive (direct ↑, ALP ↑): cholestasis, biliary obstruction, PBC/PSC
  Albumin: 3.5-5.0 g/dL; synthetic function; low = chronic liver disease, malnutrition, protein-losing
  PT/INR: synthetic function; factor VII (shortest half-life); prolonged in acute liver failure or warfarin
```

---

## 3. Coagulation Studies

```
COAGULATION CASCADE REVIEW:
  Intrinsic path: XII → XI → IX → VIII (+ IXa) → X
  Extrinsic path: VII + TF → X
  Common path: X → V → prothrombin → thrombin → fibrinogen → fibrin

PT (Prothrombin Time):
  Tests extrinsic + common pathways (factors VII, X, V, II, I)
  Normal: 11-13 seconds; INR = PT_patient/PT_mean_normal
  Prolonged PT/INR: warfarin, liver disease, vitamin K deficiency, factor VII/X/V/II deficiency
  Warfarin: inhibits vitamin K-dependent factors (II, VII, IX, X, protein C/S)

aPTT (Activated Partial Thromboplastin Time):
  Tests intrinsic + common pathways (all factors EXCEPT VII and XIII)
  Normal: 25-35 seconds
  Prolonged aPTT: heparin (UFH), hemophilia A/B (VIII/IX deficiency), vWD (severe type 3), lupus anticoagulant (paradoxically thrombotic despite prolonged aPTT)
  UFH monitoring: target aPTT 60-100 sec (2-3× normal) or anti-Xa 0.3-0.7 IU/mL

MIXING STUDY:
  Prolong PT or aPTT → mix 1:1 with normal plasma
  Corrects: factor deficiency (add missing factors from normal plasma)
  Does not correct: inhibitor (lupus anticoagulant, acquired factor VIII inhibitor) — inhibitor in patient sample blocks normal plasma factors too

D-DIMER:
  Fibrin degradation product; elevated in: DVT, PE, DIC, pregnancy, malignancy, post-op, infection
  High sensitivity (99%) but LOW specificity for PE
  Use: rule OUT PE (Wells score low + d-dimer negative → very unlikely); do NOT use to rule IN
  Age-adjusted d-dimer: threshold = age × 10 µg/L (>50 years); reduces unnecessary CT-PA

FIBRINOGEN (normal 200-400 mg/dL):
  Acute phase reactant: rises in inflammation
  Falls in: DIC (consumption), severe liver disease, fibrinogenolysis

DIC (Disseminated Intravascular Coagulation):
  Simultaneous activation of clotting + fibrinolysis → consumption of all components
  Hallmarks: ↑PT/INR + ↑aPTT + ↓platelets + ↓fibrinogen + ↑D-dimer + ↑FDPs (fibrin degradation products)
  Causes: sepsis (most common), massive tissue injury, obstetric complications, malignancy
  Treatment: treat underlying cause; FFP for PT/aPTT; cryoprecipitate for fibrinogen; platelets if <50k with bleeding

THROMBOELASTOGRAPHY (TEG/ROTEM):
  Point-of-care viscoelastic test; whole blood clot formation + strength + lysis in real time
  Parameters: R-time (clot initiation), K-time (clot kinetics), α-angle (fibrin cross-linking speed), MA (max amplitude = platelet + fibrin strength), LY30 (fibrinolysis)
  Guide transfusion in massive hemorrhage (trauma, cardiac surgery, liver transplant)
```

---

## 4. Cardiac Biomarkers

```
TROPONIN (cTnI, cTnT):
  Proteins: troponin complex regulates actin-myosin contraction; released when cardiomyocytes die
  High-sensitivity troponin (hsTn): detects lower concentrations; changes over time more informative than single value

  TIME COURSE IN ACUTE MI:
    hsTnI: rises 1-3 hrs after MI; peaks 12-24 hrs; normalizes 5-7 days
    Use serial: hsTn at 0h + 1h (or 0h + 3h): rise ≥50% → AMI
    "Demand ischemia" (type 2 MI): troponin elevation without plaque rupture (sepsis, PE, tachyarrhythmia)

  Causes of elevated troponin:
    Cardiac: AMI, myocarditis, cardiac contusion, ablation, cardioversion
    Non-cardiac: PE (RV strain), sepsis, renal failure, stroke, critical illness
    Troponin level × trend × clinical context = interpretation

BNP and NT-proBNP:
  Released by ventricular cardiomyocytes in response to wall stretch (volume overload / pressure overload)
  BNP: <100 pg/mL low prob HF; >400 high prob; 100-400 gray zone
  NT-proBNP: longer half-life (1-2 hrs vs 20 min); <300 pg/mL rules out HF
  Both elevated in: heart failure (systolic/diastolic), PE (RV dysfunction), AF, renal failure
  Obesity: lower BNP/NT-proBNP (adipose tissue clears BNP)
  Clinical use: dyspnea workup; monitor HF treatment response; prognosis

CK-MB (Creatine Kinase - Myocardial Band):
  Less sensitive/specific than troponin; largely superseded
  Still useful: reinfarction (CK-MB rises again after normalization before troponin); timing of MI
  CK-MB/total CK ratio >5%: suggests cardiac origin vs skeletal muscle injury

MYOGLOBIN:
  Earliest marker: rises 1-2 hrs; very sensitive but not cardiac-specific
  Negative myoglobin: high NPV to exclude AMI if presenting early (rarely used now with hsTn)
```

---

## 5. Blood Gas Analysis (ABG/VBG)

```
ABG INTERPRETATION (Henderson-Hasselbalch approach):
  pH: 7.35-7.45; pCO2: 35-45 mmHg; HCO3: 22-26 mEq/L
  pO2: 80-100 mmHg (on room air); SpO2: 95-100%

STEP-BY-STEP APPROACH:
  1. Is it acidosis or alkalosis? pH < 7.35 = acidosis; > 7.45 = alkalosis
  2. Primary disorder: respiratory (CO2) or metabolic (HCO3)?
     Acidosis:
       Respiratory: ↑CO2 (hypoventilation)
       Metabolic: ↓HCO3 (loss or fixed acid accumulation)
     Alkalosis:
       Respiratory: ↓CO2 (hyperventilation)
       Metabolic: ↑HCO3 (loss of acid or bicarbonate gain)
  3. Is there compensation?
     Metabolic acidosis: CO2 compensates ↓ (hyperventilation); Winter's formula: expected pCO2 = 1.5×HCO3 + 8 ± 2
     Metabolic alkalosis: CO2 compensates ↑ (hypoventilation; limited by hypoxia trigger)
     Respiratory acidosis: HCO3 compensates ↑ (renal; acute: +1 per 10 CO2; chronic: +3.5 per 10 CO2)
     Respiratory alkalosis: HCO3 compensates ↓ (acute: -2 per 10 CO2; chronic: -5 per 10 CO2)
  4. Anion gap if metabolic acidosis
  5. Delta-delta if elevated AG: [(AG-12)/(24-HCO3)] — if >2: metabolic alkalosis hidden; if <1: non-AG acidosis hidden

A-a GRADIENT:
  A-a = PAO2 - PaO2
  PAO2 (alveolar): PAO2 = (FiO2 × [Patm - PH2O]) - PaCO2/RQ = FiO2×713 - PaCO2/0.8 (at sea level, room air)
  Normal A-a: 5-15 mmHg (increases with age: upper limit = age/4)
  Elevated A-a: V/Q mismatch (PE, pneumonia, ARDS), diffusion impairment, shunt
  Normal A-a with low PaO2: hypoventilation (CO2 displaces O2 in alveolus)

VBG vs ABG:
  Venous gas: easier (IV or peripheral stick); venous pH ~0.03-0.05 lower; VCO2 ~6-8 higher
  Adequate for: acid-base assessment (pH, HCO3, CO2 — venous CO2 reliably tracks arterial)
  Cannot replace ABG for: oxygenation (pO2 meaningless venously), A-a gradient
```

---

## 6. Imaging: X-ray

```
PHYSICAL BASIS:
  X-ray photons interact with tissue via photoelectric effect + Compton scatter
  Attenuation: bone (Ca2+ → photoelectric) >> soft tissue >> fat >> air
  Image: differential transmission → detector/film; dense = white (bright); lucent = black (dark)

CHEST X-RAY (CXR) APPROACH (ABCDE):
  A — Airway: trachea midline; carina angle; assess for deviation
  B — Bones: ribs, clavicles, scapulae; fractures, lytic lesions
  C — Cardiac: cardiothoracic ratio <50% (PA film); heart borders (R=RA, L=LV); aortic knuckle
  D — Diaphragm: right slightly higher; costophrenic angles sharp; air under diaphragm (perforation)
  E — Everything else: lungs (opacification = consolidation/collapse/effusion/mass); mediastinum; soft tissue; tubes/lines

RADIOGRAPHIC DENSITIES (white → black):
  Metal > bone > soft tissue/fluid > fat > air
  Silhouette sign: loss of border between two structures of same density when adjacent

LUNG PATTERNS:
  Airspace/Alveolar: fluffy, patchy, air bronchograms; consolidation or pulmonary edema
  Interstitial: reticular, nodular, reticulonodular; ILD, lymphangitic carcinomatosis, viral
  Hyperinflation: flattened diaphragm, barrel chest, horizontal ribs; COPD/emphysema
  Pleural effusion: blunting of costophrenic angle (>200 mL); meniscus sign; blunts costo-diaphragmatic angle
  Pneumothorax: lung edge visible; absent lung markings beyond edge; look for tension (mediastinal shift)
```

---

## 7. Imaging: CT

```
CT PHYSICS:
  Rotate X-ray source + detectors around patient; multiple projections → mathematical reconstruction
  Hounsfield Units (HU): scale relative to water
    Air:      −1000 HU (black)
    Fat:      −100 to −50 HU (very dark)
    Water:    0 HU (reference)
    Soft tissue: +20 to +80 HU (gray)
    Blood:    +40 to +60 HU (slightly brighter than soft tissue)
    Bone:     +400 to +1000 HU (very bright, white)
    Metal implants: >+1000 HU + beam hardening artifacts

  Windowing: adjust display to optimize contrast for specific tissue
    Lung window: wide window, low level (e.g., C=-600 HU, W=1500)
    Bone window: wide window, high level (e.g., C=400, W=2000)
    Soft tissue/abdomen: C=50, W=400

ACQUISITION:
  Helical/spiral CT: continuous rotation; table moving; fast; 3D reconstruction possible
  Multi-detector CT (MDCT): 16-320 detector rows; sub-millimeter slices; fast organ imaging
  High-pitch acquisition: cardiac gating; dual-source CT; ECG-synchronized for heart

CONTRAST PHASES (IV iodinated contrast):
  Non-contrast: calcification, blood (hemorrhage bright), baseline density
  Arterial phase: 25-30 sec after injection; aorta/visceral arteries bright; arterial lesions
  Portal venous phase: 60-70 sec; liver parenchyma enhances maximally; most abdominal pathology
  Delayed phase: 3-5 min; nephrograms; some lesions better characterized (cholangiocarcinoma)

RADIATION DOSE:
  CT: significant radiation; effective dose 2-15 mSv per scan (CXR: ~0.1 mSv; chest CT: ~7 mSv)
  ALARA principle: As Low As Reasonably Achievable
  Automatic exposure control (AEC): modulates mAs based on patient size → reduce dose
  Iterative reconstruction: reduces noise without increasing dose; allows lower mAs scans
  Contrast risks: contrast nephropathy (CIN) in eGFR <30; prehydrate; use iso-osmolar contrast; hold nephrotoxics

CT-SPECIFIC INDICATIONS:
  Head: stroke (ischemic vs hemorrhagic — urgent non-contrast), subdural/epidural hematoma, hydrocephalus
  Chest: PE (CT pulmonary angiography), lung cancer staging, HRCT for ILD
  Abdomen: acute abdomen, bowel obstruction, renal stones (non-contrast), liver lesions, AAA
  Trauma: whole-body CT (polytrauma); high sensitivity/specificity for solid organ injury
```

---

## 8. Imaging: MRI

```
MRI PHYSICS:
  Hydrogen nuclei (protons) have spin → magnetic moment → align with strong external B0 field
  RF pulse: excites protons; precession at Larmor frequency (ω = γ × B0; 3T: 128 MHz)
  Relaxation:
    T1 longitudinal (spin-lattice): recovery of Mz; tissue regrows magnetic alignment
    T2 transverse (spin-spin): decay of Mxy; protons lose phase coherence
  Signal: depends on proton density + T1 + T2 relaxation of tissue

T1-WEIGHTED IMAGES:
  SHORT TR, SHORT TE
  Bright (white): fat, subacute hemorrhage (metHgb), proteinaceous fluid, gadolinium enhancement, marrow, melanin
  Dark (black): water (CSF, edema), cortical bone (no protons)
  Use: anatomy; post-contrast (fat usually suppressed); bone marrow

T2-WEIGHTED IMAGES:
  LONG TR, LONG TE
  Bright: water (CSF, edema, most pathology), free fluid, effusions
  Dark: fat (unless fat-saturation applied), fibrous tissue, air, hemosiderin
  Use: pathology detection; "water is bright on T2"
  Mnemonic: T2 = Trouble (pathology) = bright

SEQUENCE GUIDE:
  FLAIR (Fluid Attenuated IR): T2 with CSF nulled; suppresses bright CSF → periventricular WM lesions
    MS plaques, subarachnoid hemorrhage (blood stays bright, CSF nulled)
  DWI (Diffusion-Weighted): Brownian motion restriction → bright
    Acute ischemic stroke: restricted diffusion bright (cytotoxic edema); visible in minutes
    Abscess, acute demyelination, CJD, lymphoma (highly cellular)
  FLAIR + DWI combination: ischemic stroke >4.5h FLAIR bright; <4.5h FLAIR negative; thrombolysis window
  MR Angiography (MRA): time-of-flight or contrast-enhanced; vascular anatomy; aneurysms, stenosis
  SWI (Susceptibility Weighted): hemosiderin, calcium, deoxygenated blood, iron; microbleeds

GADOLINIUM CONTRAST:
  T1 shortening → enhanced tissues appear bright on T1
  Blood-brain barrier breakdown: enhancement in tumors, abscesses, active MS plaques, meningitis
  NSF (Nephrogenic Systemic Fibrosis): gadolinium in severe renal failure (GFR <15-30) → fibrosis
    Use macrocyclic chelates (gadobutrol, gadoteridol) → most stable; avoid linear agents in renal failure

MRI CLINICAL INDICATIONS (vs CT):
  MRI superior: brain (soft tissue, posterior fossa — less artifact than CT), spine, soft tissue tumors, cartilage, fetal imaging, cardiac (wall motion, scar), liver lesions (hepatocellular), MR cholangiopancreatography (MRCP)
  CT superior: lung parenchyma, calcification, acute head trauma (fast), patient with pacemaker/metallic implants
```

---

## 9. Imaging: Ultrasound

```
PHYSICS:
  Piezoelectric transducer: applies electrical pulse → crystal vibrates → generates ultrasound wave (2-18 MHz)
  Echo: reflected waves from tissue interfaces → crystal vibrates → electrical signal → image
  Frequency vs penetration trade-off:
    High frequency (5-15 MHz): superficial structures, excellent resolution, poor penetration
    Low frequency (2-5 MHz): deep structures, poor resolution, better penetration
  B-mode (brightness): gray-scale; standard 2D imaging
  M-mode: motion over time; cardiac valve motion, aortic root
  Doppler: frequency shift from moving targets (blood, valves)

ECHOGENICITY:
  Hyperechoic (bright): bone, gallstones, calcification, fresh clot, fibrous tissue, interfaces
  Hypoechoic (dark): homogeneous solid tissue, fresh fluid
  Anechoic (black): simple fluid (bile, urine, CSF) → no internal echoes + posterior acoustic enhancement
  Posterior enhancement: sound transmits freely through fluid → brighter deep to cyst (confirms simple fluid)
  Acoustic shadow: bone/stone blocks transmission → dark shadow deep to structure

CLINICAL APPLICATIONS:
  FAST (Focused Assessment with Sonography in Trauma):
    4 views: pericardium, hepatorenal (Morrison's pouch), splenorenal, bladder/pelvis
    Positive FAST: free fluid → hemoperitoneum / hemopericardium → OR decision
    Limited: hollow viscus injury; retroperitoneal bleed; obese patients

  POCUS (Point-of-Care Ultrasound):
    Cardiac (FOCUS): ventricular function, pericardial effusion, valve assessment
    Lung: pneumothorax (absent sliding sign), pleural effusion, consolidation (B-lines for pulmonary edema)
    Vascular: IVC diameter (fluid responsiveness); DVT (non-compressibility of vein)
    Abdominal: aorta, gallbladder, bladder, kidneys

  OBSTETRIC: placenta, fetal biometry, amniotic fluid, nuchal translucency (T21 screening)
  MUSCULOSKELETAL: rotator cuff, tendons, joints (effusion), guided injections
  NO RADIATION: safe in pregnancy, children, repeated exams
```

---

## 10. Nuclear Medicine and PET

```
SCINTIGRAPHY / SPECT:
  Radiotracer: γ-emitting isotope (Tc-99m most common; 6-hr half-life; 140 keV γ)
  Detection: gamma camera; collimator defines direction; crystal + PMT detect events
  SPECT: multiple projections → 3D tomographic images of tracer distribution

  Common studies:
    Bone scan (Tc-99m MDP): osteoblastic activity; metastases, occult fractures, osteomyelitis
    Myocardial perfusion (Tc-99m sestamibi): ischemia vs infarction; stress + rest
    VQ scan: ventilation-perfusion matching; PE diagnosis (mismatched defects = PE); alternative if CT-PA contraindicated
    Renal scan (Tc-99m MAG3): split renal function, urinary obstruction
    Thyroid scan (I-131/Tc-99m pertechnetate): function/anatomy; hot vs cold nodules

PET (Positron Emission Tomography):
  β+ emitter: positron annihilates with electron → two 511 keV γ coincident events → localization
  FDG (fluorodeoxyglucose, ¹⁸F): glucose analog; taken up by metabolically active cells
    High metabolic rate: cancer, infection, inflammation
    PET/CT: anatomic + metabolic fusion; staging, treatment response, recurrence detection
    Exceptions: brain always hot (glucose-based activity); bladder (FDG excreted)
  Other tracers:
    ¹¹C-choline, PSMA (¹⁸F/⁶⁸Ga): prostate cancer staging
    ⁶⁸Ga-DOTATATE: neuroendocrine tumors (somatostatin receptor)
    FDG-PET/CT: lymphoma staging (Deauville scoring), lung cancer, colorectal
    Amyloid PET (¹⁸F-florbetapir): Alzheimer's amyloid plaques
    FDG-PET false negatives: low-grade tumors, mucinous tumors, small lesions, hyperglycemia (competition)

RADIATION PROTECTION:
  ALARA; iodine-131 therapy patients hospitalized temporarily (high dose)
  Pregnancy: PET/CT avoided unless critically necessary; ¹³¹I-therapy absolutely contraindicated
  Dosimetry: effective dose FDG PET/CT ~7-8 mSv; SPECT bone scan ~3-4 mSv
```

---

## 11. Diagnostic Reasoning

Diagnostic reasoning is Bayesian inference applied to a binary classification problem with non-zero base rates. The vocabulary is different from ML/statistics but the math is identical:

```
MEDICAL TERM          ML / STATISTICS EQUIVALENT
──────────────────────────────────────────────────────────────────────────
Sensitivity           Recall / True Positive Rate (TPR)
                      TP/(TP+FN) — of all true positives, what fraction
                      did the test catch?

Specificity           True Negative Rate (TNR) = 1 - FPR
                      TN/(TN+FP) — of all true negatives, what fraction
                      did the test correctly exclude?

Positive predictive   Precision
value (PPV)           TP/(TP+FP) — of positive test results, fraction
                      that are true positives (prevalence-dependent)

Negative predictive   NPV: TN/(TN+FN) — of negatives, fraction correct
value (NPV)

ROC curve             Identical to ML ROC curve — TPR vs FPR at all
                      thresholds; AUC is the same AUC used in ML model
                      evaluation

Pre-test probability  Prior probability P(disease) before test
Post-test probability Posterior probability P(disease|test result)
Bayesian updating     Bayes' theorem: posterior = prior × likelihood
                      Post-test odds = Pre-test odds × LR
                      (this IS posterior inference; LR is the likelihood
                      ratio of the evidence)

Calibration curve     PPV vs predicted probability — same concept used
                      to evaluate ML classifier calibration
```

SENSITIVITY AND SPECIFICITY:
```
  Sensitivity (Sn): TP/(TP+FN) = P(test+|disease)
  Specificity (Sp): TN/(TN+FP) = P(test-|no disease)

  SnNout / SpPin:
    High Sensitivity → Negative test rules OUT (screening; FN is costly)
    High Specificity → Positive test rules IN (confirmation; FP is costly)

  ROC curve: plot TPR vs FPR at all thresholds; AUC = overall discrimination
  Threshold choice: move cutoff → trade off Sn vs Sp (exactly as in ML
    threshold tuning — depends on cost of FP vs FN in clinical context)
```

LIKELIHOOD RATIOS (LR):
```
  LR+ = Sensitivity / (1-Specificity) = P(test+|disease) / P(test+|no disease)
  LR- = (1-Sensitivity) / Specificity = P(test-|disease) / P(test-|no disease)
  Interpretation: LR+ >10 = large increase; LR- <0.1 = large decrease (in post-test probability)
  Moderate: LR+ 5-10 or LR- 0.1-0.2 = moderate change
```

BAYESIAN UPDATING (Fagan nomogram):
```
  Pre-test odds = Pre-test probability / (1 - Pre-test probability)
  Post-test odds = Pre-test odds × LR
  Post-test probability = Post-test odds / (1 + Post-test odds)

  Example: DVT
    Clinical assessment (Wells score high): pre-test prob = 60%
    D-dimer positive: LR+ ≈ 2 (not very useful to confirm — low specificity)
    D-dimer negative: LR- ≈ 0.08 (very useful to exclude — high sensitivity)
    → D-dimer is a rule-out test (high Sn); not a rule-in test

  Why PPV varies with prevalence: In a low-prevalence population, even a
  high-specificity test has low PPV (many false positives relative to true
  positives) — the "screening paradox." This is precisely why the same ML
  model applied to a rare-event dataset performs differently than on a
  balanced dataset. Pre-test probability = prevalence in the tested
  population; the model's performance is always conditional on it.
```

NUMBER NEEDED TO TREAT / TEST:
  NNT = 1/ARR; NNH = 1/ARI; Number needed to screen = 1/(detection rate reduction)

PRE-TEST PROBABILITY SOURCES:
  Clinical decision rules: Wells (DVT/PE), HEART score (ACS), CURB-65 (pneumonia), Alvarado (appendicitis)
  Published prevalence in population presenting with that chief complaint
  Skilled history + exam: can move pre-test prob dramatically before ordering ANY test

IMAGING APPROPRIATENESS:
  ACR Appropriateness Criteria: evidence-based; which imaging for which indication
  Incidentalomas: incidentally discovered lesions requiring follow-up algorithms (Bosniak for renal cysts, Lung-RADS for CT lung nodules, Bi-RADS for mammography)
  Radiomics + AI: automated lesion detection and characterization; FDA-cleared tools for intracranial hemorrhage, chest PE, diabetic retinopathy
```

---

## 12. Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Anemia: microcytic + low ferritin? | Iron deficiency anemia (IDA) |
| Anemia: macrocytic + hypersegmented neutrophils? | B12 or folate deficiency (megaloblastic) |
| Prolonged PT + normal aPTT? | Factor VII deficiency or early warfarin; extrinsic pathway only |
| Prolonged aPTT + normal PT? | Hemophilia A/B (VIII/IX); heparin (UFH); lupus anticoagulant (paradoxically thrombotic) |
| DIC lab pattern? | ↑PT/INR + ↑aPTT + ↓platelets + ↓fibrinogen + ↑D-dimer |
| Troponin elevation in non-MI? | PE (RV strain), myocarditis, sepsis, renal failure, demand ischemia |
| CT Hounsfield Units: blood vs water? | Blood ~50 HU; water 0 HU; bone +1000; air -1000 |
| MRI: T1 bright tissue? | Fat, gadolinium enhancement, subacute hemorrhage (metHgb) |
| MRI: T2 bright tissue? | Water (edema, CSF, pathology); "water is bright on T2" |
| DWI MRI bright = ? | Restricted diffusion; acute ischemic stroke, abscess, highly cellular tumors |
| US anechoic with posterior enhancement? | Simple fluid (cyst, bile, effusion); benign finding |
| PET tracer for cancer staging? | FDG (¹⁸F-fluorodeoxyglucose); metabolically active tumors |
| D-dimer: rule in or rule out PE? | Rule OUT (high sensitivity, low specificity); negative in low-prob clinical context |
| High Sn test negative = ? | SnNout: rules out disease; e.g., d-dimer negative in low-prob PE = excluded |

---

## Common Confusion Points

**AST vs ALT in liver disease:** Both are hepatocellular damage markers, but ALT is more liver-specific. AST also rises in cardiac/muscle injury. AST:ALT ratio >2:1 classically suggests alcoholic hepatitis (alcohol depletes pyridoxine needed for ALT more than AST). ALT > AST: non-alcoholic liver disease, viral hepatitis, medications.

**Troponin is sensitive but not specific for MI:** Any myocardial cell death elevates troponin — ischemia, myocarditis, direct injury, or metabolic stress. "Troponin elevation" ≠ "STEMI." Clinical context + EKG + imaging determine whether it's an acute coronary syndrome vs demand ischemia vs myocarditis vs PE-related RV strain. The serial rise pattern (delta troponin) is more specific for acute MI than single elevated value.

**CT contrast phases — getting the timing right:** Arterial phase is for vascular anatomy (dissection, arterial bleed, tumor arterial supply). Portal venous phase is for most abdominal parenchymal lesions (liver, spleen, pancreas). A single-phase post-contrast scan defaults to portal venous phase. Ordering "CT abdomen with contrast" without specifying phase may not answer your clinical question.

**MRI T1 vs T2: what's white?** Quick rule: T1 = "fat is bright, water is dark"; T2 = "water is bright, fat can be dark." Pathology (edema, tumor, inflammation) contains water → usually bright on T2. Post-gadolinium T1 images show enhancement where BBB or blood vessels are abnormal. Fat suppression helps separate fat brightness from pathologic enhancement.

**D-dimer is not a rule-IN test:** D-dimer has high sensitivity (~99%) but very low specificity for PE. Almost any illness (infection, cancer, recent surgery, pregnancy) elevates D-dimer. A positive d-dimer means almost nothing. A NEGATIVE d-dimer in a low-probability patient means PE is very unlikely (LR- ~0.08). The test is only useful as a rule-out, not a rule-in.

**Ultrasound posterior enhancement vs shadow:** Posterior acoustic enhancement = sound passes easily through a fluid-filled structure → tissues deep to it receive more sound → appear brighter. This confirms fluid. Acoustic shadow = dense structure (stone, bone) blocks sound → dark shadow deep to it. These two patterns are opposites and key to US interpretation.
