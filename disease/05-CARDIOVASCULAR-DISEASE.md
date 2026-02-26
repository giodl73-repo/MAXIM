# Cardiovascular Disease

## The Big Picture

```
CVD is the leading cause of death globally (~18M/year)
All major CV diseases trace to a common upstream driver: ATHEROSCLEROSIS

ATHEROSCLEROSIS DRIVES:
  Coronary artery disease → Stable angina → ACS → MI → HF
  Cerebrovascular disease → TIA → Stroke
  Peripheral arterial disease → Claudication → Critical limb ischemia

INDEPENDENT PATHOLOGY:
  Heart failure (also from non-ischemic causes)
  Arrhythmias (structural, channelopathy, metabolic)
  Valvular disease (rheumatic, degenerative)
  Hypertension (upstream risk factor + end-organ target)
```

---

<!-- @editor[bridge/P2]: No old-world bridge -- atherosclerosis as progressive pipeline failure maps to cascading failure models in layered systems -->

## Atherosclerosis: Pathogenesis

```
STEP 1: ENDOTHELIAL DYSFUNCTION
  Triggers: dyslipidemia (oxidized LDL), hypertension (shear stress), smoking (ROS),
            diabetes (glycation), infection, hyperhomocysteinemia
  Effects: ↑ VCAM-1/ICAM-1 (adhesion molecules), ↓ NO production
  Location: predilection for areas of turbulent flow (bifurcations, curvatures)

STEP 2: LDL ACCUMULATION AND OXIDATION
  LDL enters dysfunctional endothelium → retained in intima → oxidized (oxLDL)
  oxLDL: highly inflammatory → activates endothelium + macrophages

STEP 3: FOAM CELL FORMATION
  Monocytes adhere (via VCAM-1) → transmigrate → become macrophages in intima
  Macrophages express scavenger receptors (SR-A, CD36) → take up oxLDL (not regulated)
  → Lipid-laden "foam cells" → fatty streak (earliest lesion, even in children)

STEP 4: FIBROUS PLAQUE
  Foam cells → die → lipid core + necrotic debris accumulates
  T cells → cytokines → smooth muscle cells migrate from media to intima
  SMC: produce extracellular matrix (collagen, proteoglycans) → fibrous cap
  Stable plaque: thick fibrous cap, small lipid core, calcified → stable angina

STEP 5: VULNERABLE PLAQUE RUPTURE (leads to ACS)
  Thin fibrous cap, large necrotic lipid core, inflammatory (high macrophage density)
  MMPs (from macrophages): degrade collagen in cap → PLAQUE RUPTURE
  Plaque erosion (alternative mechanism): no rupture; endothelial cells shed → thrombus on surface
  Exposed collagen + TF → platelet activation → thrombus → occlusion → MI
```

### Framingham Risk Factors

| Modifiable | Non-modifiable |
|------------|---------------|
| Dyslipidemia (↑ LDL, ↓ HDL, ↑ TG) | Age (M > 45, F > 55) |
| Hypertension | Sex (male > female before menopause) |
| Diabetes mellitus | Family history (1st degree < 55M/65F) |
| Smoking | Race/ethnicity |
| Obesity (especially visceral) | |
| Physical inactivity | |
| Diet (saturated fat, trans fat, processed food) | |

Newer risk enhancers: hs-CRP, coronary artery calcium (CAC) score, Lp(a), ApoB.

---

## Acute Coronary Syndromes (ACS)

```
SPECTRUM:
  Stable angina → UNSTABLE ANGINA (UA) → NSTEMI → STEMI

STABLE ANGINA:
  Fixed obstructive plaque → ↓ blood flow with ↑ demand (exertion)
  Reproducible, relieved by rest/nitroglycerin
  No troponin elevation (no necrosis)

UNSTABLE ANGINA (UA):
  New onset or accelerating pattern; occurs at rest
  Partial occlusion or plaque instability
  No troponin elevation (no necrosis)
  ECG: ST depression or T-wave changes (or normal)

NSTEMI (Non-ST elevation MI):
  Partial occlusion or microvascular
  Troponin POSITIVE (some necrosis)
  ECG: ST depression ± T-wave changes (no STEMI pattern)

STEMI (ST elevation MI):
  Complete occlusion of major coronary artery
  Troponin strongly positive
  ECG: ST elevation in specific leads → indicates artery involved
  EMERGENCY: time-critical — door-to-balloon < 90 minutes (PCI) or < 30 min thrombolytics if PCI unavailable
```

### Coronary Territory and ECG Leads

```
LAD (left anterior descending) → anterior wall
  ST elevation: V1-V4 (anterior leads)
  Often worst MI: "widow maker"

RCA (right coronary artery) → inferior wall
  ST elevation: II, III, aVF (inferior leads)
  Often involves SA/AV node → bradycardia, heart block

LCX (left circumflex) → lateral wall
  ST elevation: I, aVL, V5-V6 (lateral leads)
  Posterior MI: ST depression V1-V2 (reciprocal changes) — get posterior leads
```

### Myocardial Infarction: Zones and Biomarkers

```
THREE ZONES (concentric around occlusion):
  Central: NECROSIS (irreversible — infarcted tissue)
  Middle: INJURY (reversible if reperfused quickly — current of injury = ST elevation)
  Outer: ISCHEMIA (reversible — T wave changes, repolarization abnormality)

BIOMARKER TIME COURSE:
  Myoglobin: rises 1-4 hr, peaks 6-7 hr, normalizes 24 hr (not cardiac-specific)
  Troponin I/T: rises 3-12 hr, peaks 24-48 hr, normalizes 5-14 days (gold standard)
  CK-MB: rises 3-12 hr, peaks 24 hr, normalizes 48-72 hr (useful for reinfarction timing)

High-sensitivity troponin (hs-TnI/T): detectable in first hour → 0/1 hr algorithm for rapid rule-out
```

### Complications of MI

| Timing | Complication | Mechanism |
|--------|-------------|-----------|
| Minutes–hours | Arrhythmias (VF/VT) | ↑ irritability of ischemic myocardium |
| 1–3 days | Acute pericarditis | Epicardial inflammation from transmural MI |
| 1–7 days | Papillary muscle rupture | Inferior MI → posterior PM necrosis → acute MR → flash pulmonary edema |
| 3–7 days | Ventricular free wall rupture | Necrotic wall tears → pericardial tamponade → cardiac arrest |
| 3–7 days | Ventricular septal defect (VSD) | Septal necrosis → acute shunt → biventricular failure |
| Weeks–months | Ventricular aneurysm | Infarcted wall bulges → thrombus, persistent ST elevation, arrhythmia |
| Weeks–months | Dressler syndrome | Pericarditis/pericardial effusion from post-MI autoimmune reaction |

---

## Heart Failure

```
DEFINITION: Heart cannot pump sufficient output to meet metabolic demands (or does so at elevated filling pressures)

HFrEF (Reduced EF) — systolic failure:
  EF < 40%
  Can't contract adequately: post-MI, dilated CM, myocarditis
  Mechanism: ↓ SV → ↓ CO → compensatory:
    ↑ Sympathetic (↑ HR, ↑ contractility, ↑ afterload) → initially helpful, long-term toxic
    ↑ RAAS (↑ Na retention, ↑ volume) → initially helpful, long-term harmful
    Ventricular remodeling: eccentric hypertrophy (dilation + wall thinning) → worsening EF

HFpEF (Preserved EF) — diastolic failure:
  EF ≥ 50% (or 40–50% = "borderline/HFmrEF")
  Can't relax and fill: HTN (hypertrophied stiff ventricle), HCM, restrictive CM, amyloid
  Mechanism: ↑ filling pressures → pulmonary congestion → dyspnea with normal EF
  More common in elderly, women, hypertensive, obese, diabetic
```

### Compensatory Mechanisms → Decompensation

```
RAAS ACTIVATION (chronic HF):
  ↓ CO → ↓ renal perfusion → ↑ renin → Ang II → aldosterone
  → Na/water retention → ↑ preload → initially restores CO (Frank-Starling)
  → Chronic: ↑↑ volume → pulmonary edema + peripheral edema + further ventricular dilation

SYMPATHETIC ACTIVATION (chronic HF):
  ↑ HR, ↑ contractility, ↑ vasoconstriction (↑ afterload)
  Initially compensatory; chronically: receptor downregulation, myocyte toxicity, arrhythmias

TREATMENT TARGETS:
  β-blockers: block chronic sympathetic toxicity; improve EF over months (bisoprolol, carvedilol, metoprolol XL)
  ACEi/ARBs/ARNi (sacubitril-valsartan): block RAAS; ↓ remodeling; sacubitril = neprilysin inhibitor → ↑ ANP
  Aldosterone antagonists (spironolactone, eplerenone): block K-wasting, anti-fibrotic
  SGLT2 inhibitors (dapagliflozin, empagliflozin): cardiorenoprotective (mechanism not fully explained — partly osmotic, partly metabolic)
  Ivabradine: HCN1 If channel blocker → ↓ HR (without negative inotropy) if HR ≥ 70 and sinusrhythm
  BNP/NT-proBNP: diagnostic marker; ↑ in HF (released from stretched cardiomyocytes)
```

---

## Valvular Disease

| Valve | Lesion | Cause | Key Features |
|-------|--------|-------|-------------|
| Aortic | Stenosis | Calcific (elderly), bicuspid AoV (younger), rheumatic | Angina + syncope + HF (SAD triad); systolic ejection murmur; low EF late sign |
| Aortic | Regurgitation | Bicuspid AoV, endocarditis, Marfan's, aortic dilation | Widened pulse pressure, bounding "water-hammer" pulse; diastolic decrescendo murmur |
| Mitral | Stenosis | Almost always rheumatic (M. pyogenes → immune-mediated) | Atrial fibrillation; pulmonary HTN; opening snap + mid-diastolic rumble |
| Mitral | Regurgitation | MVP (most common), ruptured papillary, dilated CM, endocarditis | Holosystolic murmur; LA/LV dilation; pulmonary congestion |
| Tricuspid | Regurgitation | RV dilation (secondary), carcinoid, IV drug use endocarditis | Pulsatile liver; JVD; systolic murmur at left sternal border (increases with inspiration — Carvallo's sign) |

**Endocarditis**: S. viridans (subacute, native valve, dental procedures); S. aureus (acute, any valve, IVDA); HACEK organisms (culture-negative). Modified Duke criteria. Echocardiogram (TEE > TTE). Embolic phenomena (Janeway lesions, Osler nodes, Roth spots, splenic infarcts).

---

## Arrhythmias

```
ATRIAL FIBRILLATION (AF): most common sustained arrhythmia
  Mechanism: multiple re-entrant wavelets in atria (chaotic electrical activity)
  Risk: age, HTN, valvular disease, HF, thyrotoxicosis, alcohol ("holiday heart"), sleep apnea
  Consequences:
    Loss of "atrial kick" (10-30% ↓ CO — poorly tolerated in HFpEF)
    Thrombus in LAA (left atrial appendage) → cardioembolic stroke (~5×↑ stroke risk)
    Tachycardia-induced cardiomyopathy (if rate uncontrolled for months)
  CHA₂DS₂-VASc score: anticoagulation risk stratification for stroke prevention
    (CHF, HTN, Age ≥ 75 [2pts], DM, Stroke/TIA [2pts], Vascular disease, Age 65-74, Sex = female)
  Treatment: rate control (β-blockers, diltiazem, digoxin) or rhythm control (cardioversion, ablation)
  Anticoagulation: DOACs (apixaban, rivaroxaban, dabigatran) preferred over warfarin (fixed dosing, less monitoring)

VENTRICULAR TACHYCARDIA (VT) / VENTRICULAR FIBRILLATION (VF):
  VT (≥3 beats at ≥100 bpm from ventricular origin): may be sustained or non-sustained
  VF: completely disorganized → no CO → sudden cardiac death (SCD)
  Substrate: scar from prior MI (re-entrant circuit), HCM, channelopathies (LQTS, Brugada)
  Treatment: defibrillation (VF), anti-arrhythmics (amiodarone, lidocaine), ICD (implantable cardioverter-defibrillator)

HEART BLOCKS:
  1st degree: prolonged PR (> 200 ms) — benign
  2nd degree Mobitz I (Wenckebach): PR progressively lengthens → dropped QRS — usually benign (AV node)
  2nd degree Mobitz II: fixed PR → sudden dropped QRS — more serious (infranodal)
  3rd degree (complete): no P-QRS relationship; atria + ventricles independently paced — syncope/death; needs pacemaker

LONG QT SYNDROME:
  Prolonged QT → Torsades de Pointes (TdP) → VF → SCD
  Congenital: LQTS 1-15 (most common: LQT1 KCNQ1, LQT2 KCNH2, LQT3 SCN5A)
  Acquired: drugs (quinidine, sotalol, haloperidol, azithromycin, chloroquine), hypoK, hypoMg, bradycardia
  Treatment: β-blockers (LQT1/2), mexiletine (LQT3), ICD (high risk), avoid triggers
```

---

## Hypertension

```
DEFINITION: SBP ≥ 130 mmHg or DBP ≥ 80 mmHg (ACC/AHA 2017)
  Stage 1: 130-139/80-89
  Stage 2: ≥ 140/90
  Hypertensive urgency: > 180/110 without end-organ damage
  Hypertensive emergency: > 180/120 WITH end-organ damage (MAP lowered by 25% in 1st hour then gradual)

PRIMARY (ESSENTIAL) HTN: ~95% of cases
  Multifactorial: genetic predisposition + obesity/salt intake/RAAS dysregulation/sympathetic
  No single cause identifiable

SECONDARY HTN (~5%): identifiable cause
  Renal artery stenosis (fibromuscular dysplasia in young women; atherosclerotic in elderly men): bruit
  Primary hyperaldosteronism (Conn syndrome): resistant HTN + hypokalemia; adrenal adenoma → adrenal CT + aldosterone/renin ratio
  Pheochromocytoma: episodic HTN + headache + diaphoresis + palpitations; 24hr urine metanephrines
  Obstructive sleep apnea: recurrent hypoxia → sympathetic surges
  Hypothyroidism, hyperthyroidism, hypercortisolism, coarctation of aorta

END-ORGAN DAMAGE (from chronic uncontrolled HTN):
  Heart: LVH (hypertensive HCM → HFpEF), coronary artery disease
  Brain: stroke (ischemic or hemorrhagic), vascular dementia
  Kidney: hypertensive nephrosclerosis → CKD (second leading cause of ESRD)
  Eyes: hypertensive retinopathy (AV nicking, flame hemorrhages, papilledema in emergency)
  Aorta: dissection (DeBakey/Stanford classification; A involves ascending = emergency surgery, B = medical)
```

---

## Stroke

```
ISCHEMIC (80%):
  THROMBOTIC: in-situ atherosclerotic plaque in large artery ruptures
    Large vessel: carotid, MCA, ACA, PCA, basilar
  EMBOLIC: clot from another site lodges in cerebral artery
    Cardioembolic: AF, MI, valvular, dilated CM (most common embolic source)
    Artery-to-artery: carotid plaque → fragment → MCA
  LACUNAR: small vessel disease from HTN/DM → lipohyalinosis → small deep infarcts
    Syndromes: pure motor, pure sensory, ataxic hemiparesis, dysarthria-clumsy hand

HEMORRHAGIC (20%):
  Intracerebral hemorrhage (ICH): HTN (putamen/thalamus/pons/cerebellum), amyloid angiopathy (lobar)
  Subarachnoid hemorrhage (SAH): ruptured aneurysm (berry aneurysm) → "worst headache of life" (thunderclap)

PENUMBRA CONCEPT:
  Core infarct: dead neurons (no recovery)
  Ischemic penumbra: oligemic but viable if perfused quickly
  → Thrombolysis/thrombectomy saves penumbra → functional recovery

TREATMENT:
  Ischemic: tPA (alteplase) within 4.5 hours of symptom onset (no hemorrhage, no large infarct)
  Mechanical thrombectomy: LVO (large vessel occlusion) → up to 24 hr with perfusion imaging selection
  Hemorrhagic: blood pressure control, reverse anticoagulation, neurosurgical consult

NIHSS (NIH Stroke Scale): 0–42 score; > 4 = typically qualifies for intervention

TIA (transient ischemic attack): stroke-like symptoms resolving < 24 hr (typically < 1 hr)
  ABCD² score for stroke risk prediction
  High stroke risk in first 48 hr after TIA → evaluate urgently (carotid imaging, cardioembolic workup, risk factor control)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Stable vs unstable angina: key distinction? | Troponin: stable = no rise (no necrosis). Unstable = clinical change + no troponin (or NSTEMI if troponin rises) |
| Highest priority in STEMI? | Time to reperfusion — door-to-balloon < 90 min (PCI) or thrombolytics if PCI unavailable < 30 min |
| HFrEF drugs that improve survival? | RAAS blockade (ACEi/ARB/ARNi) + β-blocker + MRA (aldosterone antagonist) + SGLT2 inhibitor ("Fab 4") |
| AF + stroke risk: when anticoagulate? | CHA₂DS₂-VASc ≥ 2 in men, ≥ 3 in women → anticoagulate (DOAC preferred over warfarin) |
| LQTS: why do drugs like azithromycin prolong QT? | Block hERG (KCNH2 = LQT2 gene) → delayed repolarization → ↑ risk TdP |
| Secondary HTN workup: most common cause? | Primary hyperaldosteronism (~10% of hypertensives) — check aldosterone:renin ratio |

---

## Common Confusion Points

**Troponin elevation ≠ MI only**
Troponin rises whenever myocardium is stressed/injured: PE, myocarditis, HF decompensation, sepsis, renal failure (impaired clearance), ablation, defibrillation. The pattern (rise-and-fall vs stable) and clinical context distinguish ACS from other causes.

**Hypertensive emergency: don't lower BP too fast**
Autoregulation of cerebral blood flow shifts with chronic HTN — brain "expects" high pressure. Rapid normalization → cerebral ischemia. Standard: ↓ MAP by ~25% in first hour, then gradual. Exception: aortic dissection (target SBP < 120 in 20 min).

**AF ablation: pulmonary vein isolation**
~90% of AF triggers originate in pulmonary vein sleeves (myocardial tissue extending into PV). RF/cryoablation isolates all 4 PV ostia → success in ~60–80% for paroxysmal AF. Not "cure" — can recur, often requires repeat procedures.

**STEMI without coronary occlusion (MINOCA)**
~5% of STEMI: coronary vasospasm (Prinzmetal), embolism, coronary dissection (SCAD), Takotsubo, MI type 2 (demand ischemia). Normal coronary angiogram ≠ no MI if troponin elevated.
