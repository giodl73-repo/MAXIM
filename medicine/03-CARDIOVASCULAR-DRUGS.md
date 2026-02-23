# 03 — Cardiovascular Drugs

## Lipid-Lowering, Antihypertensives, Anticoagulants, Antiarrhythmics, Heart Failure

---

## Big Picture: CV Drug Landscape

```
┌──────────────────────────────────────────────────────────────────────────┐
│               CARDIOVASCULAR DRUG TARGETS                                │
├────────────────────────┬─────────────────────────────────────────────────┤
│ LIPID MANAGEMENT       │ Statins (HMG-CoA reductase) → LDL↓             │
│                        │ Ezetimibe (NPC1L1) → cholesterol absorption↓    │
│                        │ PCSK9 inhibitors → LDL receptor↑ → LDL↓        │
│                        │ Fibrates (PPARα) → TG↓                          │
├────────────────────────┼─────────────────────────────────────────────────┤
│ ANTIHYPERTENSIVES      │ ACEi/ARB → RAAS blockade                        │
│                        │ CCB → smooth muscle/cardiac Ca²⁺ blockade       │
│                        │ Diuretics → volume/Na depletion                 │
│                        │ β-blockers → ↓ HR/contractility/renin           │
│                        │ ARNi (ARNI) → ↑ natriuretic peptides            │
├────────────────────────┼─────────────────────────────────────────────────┤
│ ANTICOAGULANTS         │ Warfarin → vitamin K antagonism                 │
│                        │ DOACs → Xa or IIa (thrombin) inhibition         │
│                        │ Heparins → antithrombin activation              │
├────────────────────────┼─────────────────────────────────────────────────┤
│ ANTIPLATELETS          │ Aspirin → COX-1/TXA2 blockade                   │
│                        │ P2Y12 inhibitors → ADP receptor blockade        │
│                        │ GP IIb/IIIa inhibitors → final common pathway   │
├────────────────────────┼─────────────────────────────────────────────────┤
│ ANTIARRHYTHMICS        │ Vaughan-Williams I–IV classes                   │
│                        │ Adenosine → AV nodal block (SVT termination)    │
└────────────────────────┴─────────────────────────────────────────────────┘
```

---

## 1. Lipid-Lowering Agents

### Statins (HMG-CoA Reductase Inhibitors)

```
HMG-CoA → Mevalonate → → Cholesterol (rate-limiting step = HMG-CoA reductase)
  Statins block this step → ↓ intracellular cholesterol synthesis

Hepatic consequence:
  ↓ hepatic cholesterol → SREBP-2 activation → ↑ LDLR expression
  → ↑ LDL receptor number → ↑ LDL clearance from blood → ↓ plasma LDL
  Also ↓ VLDL synthesis → modest TG lowering + HDL rise

LDL reduction:
  High-intensity statins (atorvastatin 40–80mg, rosuvastatin 20–40mg): ~50% LDL↓
  Moderate-intensity statins: ~30–50% LDL↓
  Low-intensity: ~<30% LDL↓

Pleiotropic effects (beyond lipid lowering):
  ↑ eNOS → ↑ NO → vasodilation
  Anti-inflammatory (↓ CRP, ↓ macrophage activation)
  Plaque stabilization (↓ matrix metalloproteinases)
  These explain benefit that is faster than expected from LDL reduction alone

Statin intensity by drug:
  High: atorvastatin (40–80), rosuvastatin (20–40)
  Moderate: atorvastatin (10–20), rosuvastatin (5–10), simvastatin (20–40), pravastatin (40–80)
  Low: simvastatin (10), pravastatin (10–20), lovastatin (20)

Adverse effects:
  Myopathy: muscle pain (5–10% class effect); rhabdomyolysis (<0.1%)
    CK monitoring if symptomatic; ↑ risk with CYP3A4 inhibitors (azoles, macrolides, amiodarone)
    Simvastatin + amiodarone → rhabdo (don't use simvastatin >20mg with amiodarone)
    Rosuvastatin/pravastatin: less CYP3A4 dependence → fewer interactions
  ↑ Blood glucose: small ↑ T2DM risk (~10% relative); benefit >> risk in high-risk patients
  Hepatotoxicity: transaminase ↑ dose-dependent; clinically significant hepatic failure extremely rare
  No causal link to cancer, cognitive impairment (despite common beliefs)
  Statin intolerance: true myopathy in ~5%; "nocebo" effect in double-blind trials very similar to placebo

Contraindications: active liver disease, pregnancy (↓ fetal cholesterol → teratogen), breastfeeding
```

### PCSK9 Inhibitors

```
PCSK9 (proprotein convertase subtilisin/kexin type 9):
  Binds LDL receptor on hepatocyte surface → targets LDLR for degradation
  ↑ PCSK9 → ↓ LDLR recycling → ↑ plasma LDL

PCSK9 inhibitors (mAbs):
  Evolocumab (Repatha): every 2 weeks or monthly SC injection
  Alirocumab (Praluent): biweekly SC injection
  Inclisiran: siRNA (small interfering RNA) that silences PCSK9 mRNA → twice-yearly SC injection

Effect: ~60% additional LDL reduction on top of maximally tolerated statin
  Can achieve LDL <20 mg/dL (as low as physiologically needed)
  FOURIER (evolocumab) + ODYSSEY OUTCOMES (alirocumab): CV event reduction proven

Indications: ASCVD + LDL >70 on max statin + ezetimibe; FH (familial hypercholesterolemia)
Cost: ~$6,000–14,000/yr; major barrier; prior authorization requirements
```

### Other Lipid Drugs

```
EZETIMIBE:
  Inhibits NPC1L1 (cholesterol transporter at brush border of small intestine)
  ↓ cholesterol absorption → ↓ portal delivery to liver → ↑ LDLR expression
  LDL↓ ~18–20% added to statin; well-tolerated; PO once daily

FIBRATES (gemfibrozil, fenofibrate):
  PPARα agonist → ↑ lipoprotein lipase → ↑ VLDL clearance → TG↓ 25–50%
  Modest HDL↑; minimal LDL effect
  Primary use: severe hypertriglyceridemia (TG >500 → pancreatitis risk)
  Gemfibrozil: inhibits CYP2C8 → ↑ statin (especially repaglinide, gemfibrozil + statin = myopathy)
  Fenofibrate: preferred with statins (less CYP interaction)

NIACIN:
  Inhibits DGAT2 and VLDL secretion; ↑ HDL (↑ apoA-I production)
  Largely abandoned: HPS2-THRIVE + AIM-HIGH showed no CV benefit added to statin
  Side effect: flushing (prostaglandin-mediated; ↓ with aspirin pretreatment), hyperglycemia, hyperuricemia
```

---

## 2. Antihypertensives

### ACE Inhibitors

```
RAAS overview:
  Angiotensinogen → (renin) → Angiotensin I → (ACE) → Angiotensin II
  AT II: ↑ aldosterone → Na/water retention; ↑ SNS → vasoconstriction; direct pressor

ACE (kininase II) also degrades bradykinin → ↑ bradykinin from ACE inhibition
  Bradykinin → prostaglandins → NO → vasodilation, cough (ACEi adverse effect)

DRUGS: captopril (short-acting), enalapril, lisinopril, ramipril, benazepril

Effects: ↓ SVR, ↓ aldosterone, ↓ AT II; afferent/efferent arteriole dilation (eGFR: may ↓ slightly initially then stabilizes)

Adverse effects:
  Dry cough (10–20%): bradykinin accumulation → prostaglandins; class effect; substitute ARB
  Angioedema (0.1–0.3%): bradykinin + substance P; can be life-threatening; CLASS contraindication
  Hyperkalemia: ↓ aldosterone → ↓ K excretion; avoid with potassium-sparing diuretics/K supplements
  SCr rise: normal <30% (afferent/efferent dilation → ↓ GFR → expected; functional, not nephrotoxicity)
    SCr rise >30% → think bilateral RAS, volume depletion, NSAIDs
  TERATOGENIC: fetal renal tubular dysgenesis (2nd/3rd trimester) → absolute CI in pregnancy
```

### ARBs (Angiotensin Receptor Blockers)

```
DRUGS: losartan, valsartan, irbesartan, candesartan, olmesartan, telmisartan

Mechanism: block AT1 receptor (AT II still made, ↑ AT II but can't act)
  AT II → AT2 receptor still active (vasodilation, antiproliferative) — potentially advantageous
  No bradykinin accumulation → NO cough; very low angioedema risk

Same indications as ACEi: HF, CKD + proteinuria, post-MI, DM nephropathy
Same contraindications: pregnancy, bilateral RAS, hyperkalemia
COMBINATION ACEi + ARB: DO NOT combine (↑ hyperkalemia, AKI, hypotension without added CV benefit)
```

### Calcium Channel Blockers (CCBs)

```
DIHYDROPYRIDINES (DHP): L-type Ca²⁺ channels in vascular smooth muscle
  Amlodipine (long-acting), nifedipine, felodipine, isradipine, clevidipine (IV)
  Effects: peripheral vasodilation → ↓ SVR → ↓ BP; minimal cardiac conduction effect
  Adverse: reflex tachycardia (nifedipine >> amlodipine), peripheral edema (capillary dilation)
  Use: HTN, stable angina, vasospastic angina (Prinzmetal's)

NON-DIHYDROPYRIDINES: L-type Ca²⁺ channels in heart (SA node, AV node, myocardium)
  Verapamil: ↓ HR + ↓ AV conduction + ↓ contractility; more cardiac than diltiazem
  Diltiazem: intermediate between DHP and verapamil
  Use: SVT (rate control), AF rate control, vasospastic angina, hypertension (when β-blocker CI)
  Contraindicated: with β-blockers (additive heart block/bradycardia), HFrEF (negative inotrope)
  Verapamil + β-blocker = potentially fatal bradycardia/heart block
```

### Diuretics

```
THIAZIDES (HCTZ, chlorthalidone, indapamide):
  NCC (Na-Cl co-transporter) in DCT → ↓ Na/Cl reabsorption → ↑ urine Na/water
  Reduce pre-load + SVR (long-term: direct vasodilation beyond volume depletion)
  Chlorthalidone preferred over HCTZ (longer t½, proven CV outcomes)
  Adverse: hypokalemia (↑ aldosterone from volume depletion), hyponatremia (↓ diluting ability),
    hyperuricemia (compete with urate for tubular secretion), hyperglycemia, dyslipidemia (minor)
  Contraindicated: severe hyponatremia, gout (relative)

LOOP DIURETICS (furosemide, torsemide, bumetanide, ethacrynic acid):
  NKCC2 in thick ascending loop → most powerful diuresis
  Torsemide: better oral bioavailability than furosemide (less variable absorption)
  Use: acute pulmonary edema, chronic HF, ascites, hypercalcemia, hyperkalemia (↑ Ca excretion too)
  Adverse: hypokalemia, hypomagnesemia, ototoxicity (high-dose IV, especially ethacrynic acid)
  "Loop" diuretics + aminoglycosides = synergistic ototoxicity

POTASSIUM-SPARING:
  Spironolactone/eplerenone: MRA (mineralocorticoid receptor antagonist) → ↓ aldosterone effects
    Use: HFrEF (life-saving), HTN, hyperaldosteronism, ascites
    Adverse: hyperkalemia (↑ with ACEi/ARB), gynecomastia (spironolactone > eplerenone)
  Amiloride/triamterene: ENaC blockers → ↓ Na reabsorption in collecting duct
    Minimal antihypertensive effect alone; combined with thiazide to prevent hypokalemia
```

### β-Blockers

```
Mechanisms: ↓ HR (SA node), ↓ AV conduction, ↓ contractility, ↓ renin release (↓ β1 at JGA)

SELECTIVITY:
  β1-selective (cardioselective): metoprolol, atenolol, bisoprolol, esmolol
    ↓ β2 blockade → safer in asthma/COPD at lower doses (not truly safe, but less bronchospasm)
  Non-selective (β1 + β2): propranolol, nadolol, timolol, sotalol, carvedilol (α1 + β)
  Carvedilol: α1 + non-selective β → ↓ SVR + ↓ HR/contractility; preferred in HFrEF

ISA (intrinsic sympathomimetic activity): acebutolol, pindolol — partial agonists; less resting HR reduction

Approved HF β-blockers (proven mortality benefit):
  Carvedilol, metoprolol succinate (CR/XL), bisoprolol
  NOT atenolol, NOT propranolol (not shown to reduce mortality in HF)
  Titrate up slowly; acute decompensation is contraindication to starting (not stopping)

Adverse: bradycardia, hypotension, fatigue, ↓ exercise tolerance, depression (controversial), erectile dysfunction, ↓ glucose recovery (T1DM), blunt hypoglycemia awareness
Contraindications: acute decompensated HF, cardiogenic shock, SSS, high-degree AV block, severe reactive airway disease (non-selective), untreated pheochromocytoma (unopposed α)
```

---

## 3. Heart Failure Drugs

```
NEUROHORMONAL MODEL OF HF:
  ↓ cardiac output → SNS activation → ↑ NE → ↑ HR, ↑ vasoconstriction
                   RAAS activation → AT II + aldosterone → Na/water retention
  These compensatory mechanisms → maladaptive long-term → ventricular remodeling

"Fabulous 4" HFrEF drugs that improve mortality:
  1. ACEi or ARB (if ARNI not used)
  2. β-blocker (carvedilol/metoprolol succinate/bisoprolol)
  3. MRA (spironolactone/eplerenone)
  4. SGLT2 inhibitor (dapagliflozin/empagliflozin)
  + ARNI (sacubitril-valsartan) replaces ACEi/ARB if tolerated (PARADIGM-HF: ↓ mortality vs enalapril)
```

**ARNI (Angiotensin Receptor-Neprilysin Inhibitor):**
- Sacubitril-valsartan (Entresto): valsartan (ARB) + sacubitril (neprilysin inhibitor)
- Neprilysin degrades natriuretic peptides (BNP/ANP) → sacubitril inhibits neprilysin → ↑ NP
- ↑ ANP/BNP → ↑ natriuresis + diuresis + vasodilation → ↓ pre/afterload
- Do NOT combine with ACEi (↑ angioedema risk — neprilysin also degrades bradykinin/substance P); 36h washout

**SGLT2 inhibitors in HF:**
- Dapagliflozin, empagliflozin: reduce HF hospitalization + CV death in HFrEF AND HFpEF
- Mechanisms beyond glycosuria: ↓ pre-load (osmotic diuresis), ↓ interstitial volume, ↑ hematocrit, ↓ cardiac fibrosis/inflammation, ketone body utilization (more efficient cardiac fuel?)

**Ivabradine:**
- If-channel (funny current) inhibitor in SA node → ↓ HR without inotropic effects
- Indication: HFrEF + resting HR >70 on maximally tolerated β-blocker; sinus rhythm
- SHIFT trial: ↓ HF hospitalization (not mortality)

**Hydralazine + Isosorbide Dinitrate:**
- Combination used in African American patients with HFrEF (A-HeFT trial: ↓ mortality)
- Alternative when ACEi/ARB/ARNI not tolerated; less effective than ACEi overall

**Diuretics in HF:** Symptom control (volume overload); no mortality benefit
**Digoxin:** ↓ HF hospitalizations; no mortality effect; useful in AF + HF (rate control); narrow TI

---

## 4. Anticoagulants

### Warfarin

```
Mechanism: inhibits VKORC1 (vitamin K epoxide reductase complex) → ↓ γ-carboxylation of clotting factors II, VII, IX, X (and protein C, S)
  Factors II, VII, IX, X require γ-carboxylation for Ca²⁺-dependent activation on phospholipid membrane

Monitoring: INR (international normalized ratio)
  INR = (PT_patient / PT_normal)^ISI
  Target INR: 2.0–3.0 (most indications), 2.5–3.5 (mechanical mitral valve)

PK variability:
  CYP2C9 polymorphisms → ↓ metabolism → ↑ warfarin effect (dose reduction needed)
  VKORC1 polymorphisms → ↓ enzyme expression → ↑ warfarin sensitivity
  FDA label: CYP2C9 + VKORC1 genotyping available for initial dosing

Drug interactions (extensive — warfarin is a top DDI drug):
  ↑ INR (↑ bleeding risk): amiodarone (CYP2C9 inhibition), azoles, metronidazole, fluconazole,
    macrolides (erythro/clarithro), NSAIDs (displace from albumin), cimetidine, alcohol (acute)
  ↓ INR (↓ efficacy): rifampin, carbamazepine, phenytoin, St. John's wort, alcohol (chronic)

Management of elevated INR:
  INR 4–10, no bleeding: hold warfarin, monitor; oral vitamin K (2.5mg PO) for INR >8
  INR >10, no bleeding: hold + oral vitamin K (5mg PO)
  Life-threatening bleeding: FFP or 4-factor PCC (faster) + IV vitamin K 10mg

Unique advantages of warfarin: reversible, monitored, effective for any anticoagulation indication
  Still preferred: mechanical heart valves (DOACs inferior, FDA boxed warning for warfarin only)
```

### DOACs (Direct Oral Anticoagulants)

```
Factor Xa inhibitors:
  Apixaban (Eliquis): BID; preferred (safest bleeding profile in multiple trials)
  Rivaroxaban (Xarelto): QD (with evening meal); convenient
  Edoxaban (Savaysa): QD; requires initial parenteral anticoagulation transition
  Betrixaban (Bevyxxa): extended prophylaxis in hospitalized medical patients

Direct thrombin (IIa) inhibitors:
  Dabigatran (Pradaxa): BID; high renal clearance (80%) → ↓ dose in CKD, avoid if GFR <30
    Reversible: idarucizumab (Praxbind) — specific reversal agent

Xa inhibitors reversal:
  Andexanet alfa (Andexxa): recombinant inactive FXa — binds/sequesters Xa inhibitors
  Ciraparantag: universal reversal agent (investigational)

DOAC vs warfarin (from ARISTOTLE/ROCKET-AF/RE-LY/ENGAGE trials in AF):
  ↓ intracranial hemorrhage (~50% RRR vs warfarin)
  Non-inferior or superior for stroke prevention
  ↑ GI bleeding (rivaroxaban, dabigatran, edoxaban) vs warfarin
  No monitoring required; fewer drug/food interactions
  CI: mechanical heart valves, severe MS (high thrombus burden), pregnancy

DOAC in renal impairment:
  Apixaban: safest; dose-adjust only at GFR <25 with ≥2 of: age >80, weight <60kg, SCr >1.5
  Rivaroxaban: avoid if GFR <30 (AF indication)
  Dabigatran: avoid if GFR <30 (risk of drug accumulation + bleeding)
```

### Heparins

```
UNFRACTIONATED HEPARIN (UFH):
  Potentiates antithrombin (AT) ~1000× → ↓ Xa, IIa, IXa, Xla
  Requires AT binding (Pentasaccharide sequence on heparin) → AT conformational change
  IV infusion; monitor aPTT (target 60–100s, varies by protocol)
  Reversal: protamine sulfate (neutralizes by electrostatic binding)
  Use: acute anticoagulation, ACS, VTE, cardiopulmonary bypass, ECMO
  Adverse: HIT (heparin-induced thrombocytopenia — see below)

LMWH (enoxaparin, dalteparin):
  Shorter chains → predominantly anti-Xa (not IIa)
  SubQ dosing, predictable PK → no monitoring needed (except renal failure, extremes of weight)
  Monitor anti-Xa level in pregnancy, renal failure, obesity
  Reversal: partial with protamine (doesn't fully neutralize anti-Xa activity)

FONDAPARINUX:
  Synthetic pentasaccharide only → binds AT → inhibits Xa only (NOT IIa)
  No HIT (doesn't interact with PF4-heparin antibody system)
  SQ once daily; renal clearance; no protamine reversal

HIT (Heparin-Induced Thrombocytopenia):
  Type I: direct platelet aggregation (mild, non-immune, within 2 days) — benign
  Type II: IgG antibodies against PF4-heparin complex → platelet activation + thrombosis (devastating)
    Onset: days 5–14 (or sooner if prior heparin exposure)
    Platelets ↓ >50% from baseline; but usually 30,000–80,000 (not critically low)
    Paradox: THROMBOSIS risk despite thrombocytopenia (arterial + venous)
    Management: STOP ALL heparin (UFH + LMWH), switch to NON-heparin anticoagulant
      Argatroban (direct thrombin inhibitor, hepatic clearance)
      Bivalirudin (direct thrombin inhibitor, plasma clearance)
      Fondaparinux (low HIT risk, no cross-reactivity in practice)
      Do NOT give platelets (fuels thrombosis)
      Do NOT give warfarin until platelets recover (protein C/S depletion → warfarin necrosis)
```

---

## 5. Antiplatelets

```
ASPIRIN:
  Irreversibly inhibits COX-1 (and COX-2 at higher doses) → ↓ TXA2 (platelet)
  TXA2 = vasoconstrictor + platelet activator
  Duration: platelet lifespan 7–10 days (replace ~10%/day)
  Low dose (81mg): COX-1 preferential; high dose (325mg): COX-1 + COX-2

P2Y12 INHIBITORS (ADP receptor blocker):
  Clopidogrel: prodrug → CYP2C19 activation → irreversible P2Y12 blockade
    CYP2C19 PMs (10–15% Caucasians, 50–60% Asian) → reduced activation → ↓ efficacy
    Class effect: no reversible antidote; hold 5 days before elective surgery
  Ticagrelor: NOT a prodrug; direct, reversible P2Y12 binding; no CYP dependence → predictable
    Hold 5 days before surgery (some guidelines 3 days)
  Prasugrel: prodrug, faster and more complete activation than clopidogrel
    Contraindicated: prior stroke/TIA (↑ ICH), age >75, weight <60kg (net harm)
    More potent → ↑ bleeding risk but ↓ ischemic events in ACS vs clopidogrel

DAPT (Dual Antiplatelet Therapy) = aspirin + P2Y12 inhibitor:
  After PCI + stent: minimum 1 month (BMS), 3–6 months (DES), up to 12 months; then aspirin alone
  ACS: 12 months DAPT preferred; extended for very high ischemic risk

GP IIb/IIIa INHIBITORS: abciximab (mAb), eptifibatide, tirofiban
  Block final common pathway of platelet aggregation (fibrinogen bridge)
  IV only; adjunct in high-risk PCI; largely replaced by potent P2Y12 agents + direct thrombin inhibitors
  Major bleeding risk
```

---

## 6. Antiarrhythmics — Vaughan-Williams Classification

```
CLASS I — Na⁺ channel blockers (membrane stabilizers):
  Ia (moderate block + ↑ APD): quinidine, procainamide, disopyramide
    ↓ Vmax of AP; ↑ refractory period; proarrhythmic (torsades de pointes)
    Quinidine: historical; digoxin interaction (↑ digoxin levels)
    Procainamide: IV load for stable VT; lupus-like syndrome (NAPA metabolite)
  Ib (weak block + ↓ APD): lidocaine, mexiletine, phenytoin
    Lidocaine: IV use only; ventricular arrhythmias in acute MI; CNS toxicity (seizures)
    Mexiletine: PO; chronic ventricular arrhythmias; LQTS3 (reduces QTc)
  Ic (strong block, no APD effect): flecainide, propafenone
    CAST trial: ↑ mortality in post-MI patients (proarrhythmic)
    SAFE use: structurally normal hearts (SVT, AF in non-CAD patients)

CLASS II — β-blockers:
  Metoprolol, atenolol, esmolol (ultra-short IV)
  ↓ SA node automaticity, ↓ AV conduction, ↑ AV nodal refractory period
  Use: rate control in AF/flutter, SVT, post-MI (↓ VT/VF), appropriate sinus tachycardia

CLASS III — K⁺ channel blockers (↑ APD, ↑ refractory period):
  Amiodarone: multi-class (I/II/III/IV) — most effective antiarrhythmic
    Use: ventricular arrhythmias (VT/VF), AF cardioversion and rhythm control
    Toxicity: pulmonary toxicity (interstitial pneumonitis), thyroid (hypo + hyper — iodine-rich),
      corneal microdeposits (benign), photosensitivity, peripheral neuropathy, hepatotoxicity
      t½ 40–55 days → toxicities can persist months after stopping
    Drug interactions: ↑ warfarin, ↑ digoxin, ↑ statins (CYP2C9/3A4 inhibition)
  Sotalol: β-blocker + Class III; use: AF/flutter rhythm control, VT
    Proarrhythmic: dose-dependent QTc prolongation → torsades; requires QTc monitoring
  Dronedarone: amiodarone analog without iodine (less thyroid/lung toxicity)
    ANDROMEDA: ↑ mortality in severe HF → avoid in HFrEF or permanent AF + CV comorbidities
  Ibutilide/dofetilide: IV/PO; AF/flutter cardioversion; QTc monitoring required

CLASS IV — Calcium channel blockers (non-DHP):
  Verapamil, diltiazem: ↓ AV conduction → rate control in AF/flutter, SVT termination
  Contraindicated with β-blockers (heart block), WPW + AF (↑ accessory pathway conduction)

ADENOSINE:
  Not Vaughan-Williams classified; A1 receptor → Gi → ↑ IKAch → hyperpolarization of AV node
  Terminates AV-nodal dependent SVTs (AVNRT, AVRT) — diagnostic + therapeutic
  Very short t½ (seconds); give rapid IV push + flush; patients must be warned (brief asystole)
  Side effects: brief chest tightness, dyspnea, flushing, transient AV block
  CI: asthma (bronchoconstriction via A2B receptor), heart transplant recipients (↑ sensitivity), WPW + AF

DIGOXIN:
  Na/K-ATPase inhibition → ↑ intracellular Na → ↑ NCX → ↑ intracellular Ca → ↑ contractility
  Vagotonic (↑ ACh via vagal activation) → ↓ AV conduction → rate control in AF
  Narrow TI; toxicity: arrhythmias, GI, visual disturbances (yellow-green halos)
  ↑ toxicity: hypokalemia (competes with digoxin at Na/K-ATPase), hypomagnesemia, hypothyroidism, renal failure
  Drug interactions: quinidine, amiodarone, verapamil → ↑ digoxin levels
```

---

## Decision Cheat Sheet

| Indication | Drug(s) of Choice | Notes |
|-----------|-------------------|-------|
| LDL reduction primary target | High-intensity statin | Atorvastatin 40–80 or rosuvastatin 20–40 |
| LDL still high on max statin | + Ezetimibe → + PCSK9i | Additive: statin + eze + PCSK9i → LDL <20 possible |
| HTN + HF + CKD | ACEi or ARB | Renoprotective; avoid ACEi if bilateral RAS |
| HTN + HF + proteinuria (diabetic) | ACEi or ARB first | Do NOT combine ACEi + ARB |
| HTN + HFrEF + proteinuria | ARNI (sacubitril-valsartan) | Superior to ACEi for HF mortality |
| AF rate control | β-blocker or non-DHP CCB | Diltiazem or verapamil; avoid CCB in HFrEF |
| AF rhythm control (no structural HD) | Flecainide or propafenone | CAST data → CI in CAD/HFrEF |
| AF rhythm control (structural HD) | Amiodarone, sotalol, dofetilide | Amiodarone most effective; sotalol OK if EF ok |
| Stable VT (wide complex) | Amiodarone or procainamide IV | Lidocaine second line |
| SVT (termination) | Adenosine 6mg IV rapid push | If fails: 12mg; then 18mg; then verapamil/diltiazem |
| AF anticoagulation | DOAC (apixaban preferred) | Warfarin only if mechanical valve |
| DVT/PE anticoagulation | DOAC | Rivaroxaban or apixaban preferred; parenteral initially |
| HIT | Argatroban or bivalirudin | STOP heparin; do NOT give platelets |
| ACS + PCI | DAPT (aspirin + ticagrelor or prasugrel) | Ticagrelor preferred over clopidogrel in most ACS |

---

## Common Confusion Points

**Statin intolerance: myopathy vs rhabdomyolysis vs asymptomatic CK rise:**
Myalgia without CK elevation (~5%): often nocebo; CK <3× ULN with symptoms: monitor carefully; CK 3–10× with symptoms: hold statin; CK >10× ULN or rhabdo: stop immediately + hydrate.

**ACEi cough vs angioedema:** Cough is common (bradykinin prostaglandins), managed by switching to ARB. Angioedema is rare but dangerous; switching to ARB still carries small risk (bradykinin still elevated by ARB since ACE still blocked? No — ACE not blocked by ARB, so bradykinin is degraded). Actually ARB angioedema risk is much lower. After ACEi angioedema: ARB is usually safe with monitoring.

**Warfarin vs DOAC for mechanical valves:** DOACs FAILED in RE-ALIGN trial for mechanical valves (dabigatran → ↑ thromboembolic and bleeding events). Warfarin is the ONLY option for mechanical valves. Reason: very high thrombus burden requires more reliable anticoagulation than DOACs provide at mechanical valve.

**Flecainide/propafenone safety:** Safe in structurally normal hearts (e.g., paroxysmal AF in young healthy patients). CAST taught us these ↑ mortality post-MI due to ischemic reentry circuit vulnerability. Screen for CAD/EF <40% before prescribing.

**Amiodarone thyroid:** Contains 37% iodine by weight (Wolff-Chaikoff effect → hypothyroid; Jod-Basedow effect → hyperthyroid). Check TFTs every 6 months. Amiodarone-induced thyrotoxicosis (AIT) can be life-threatening (type 1: excess iodine → ↑ synthesis; type 2: destructive thyroiditis).

**Ticagrelor vs clopidogrel:** Ticagrelor has dyspnea side effect (unclear mechanism — possibly adenosine-related), and twice-daily dosing vs once. But no CYP2C19 dependence → predictable. Preferred in NSTEMI/STEMI unless high bleeding risk.
