# 05 — Endocrine & Metabolic Drugs

## Insulin, Oral Antidiabetics, Thyroid, Corticosteroids, Osteoporosis, Uric Acid

---

## Big Picture: Endocrine Drug Map

```
┌──────────────────────────────────────────────────────────────────────────┐
│                   ENDOCRINE / METABOLIC DRUG TARGETS                     │
├─────────────────────┬────────────────────────────────────────────────────┤
│ GLUCOSE HOMEOSTASIS │ Insulin (replacement/supplementation)               │
│                     │ Metformin (↓ hepatic gluconeogenesis)               │
│                     │ SGLT2i (renal glucose excretion)                    │
│                     │ GLP-1 RAs (incretin effect + satiety)               │
│                     │ Sulfonylureas/glinides (↑ insulin secretion)        │
│                     │ DPP-4 inhibitors (↑ endogenous GLP-1)              │
│                     │ TZDs/pioglitazone (↑ insulin sensitivity)           │
├─────────────────────┼────────────────────────────────────────────────────┤
│ THYROID             │ Levothyroxine (T4 replacement)                      │
│                     │ PTU/methimazole (block synthesis)                   │
│                     │ Radioiodine I-131 (ablation)                        │
│                     │ β-blockers (symptom control in hyperthyroid)        │
├─────────────────────┼────────────────────────────────────────────────────┤
│ ADRENAL / STEROIDS  │ Corticosteroids (GR agonism → anti-inflammatory)   │
│                     │ Mineralocorticoids (MR agonism → Na/water)          │
│                     │ MRAs (spironolactone/eplerenone) → see 03-CV       │
├─────────────────────┼────────────────────────────────────────────────────┤
│ BONE METABOLISM     │ Bisphosphonates (↓ osteoclasts)                    │
│                     │ Denosumab (anti-RANKL → ↓ osteoclasts)             │
│                     │ Teriparatide/abaloparatide (↑ osteoblasts)         │
│                     │ SERMs (estrogen receptor modulation)                │
├─────────────────────┼────────────────────────────────────────────────────┤
│ URIC ACID / GOUT    │ Xanthine oxidase inhibitors (↓ uric acid synthesis)│
│                     │ Uricosurics (↑ uric acid excretion)                │
│                     │ Colchicine (↓ neutrophil activation)                │
└─────────────────────┴────────────────────────────────────────────────────┘
```

---

## 1. Insulin

### Insulin Pharmacokinetics by Type

```
RAPID-ACTING (meal coverage, onset 15 min, peak 1–2h, duration 3–5h):
  Lispro (Humalog), aspart (NovoLog), glulisine (Apidra)
  Analog: amino acid sequence modification → ↓ self-aggregation → faster absorption
  Fast-acting inhaled (Afrezza): ultra-rapid (peak ~15 min); lung delivery; no injection
  Fiasp (aspart + niacinamide): faster still; "ultra-rapid"

SHORT-ACTING (Regular insulin, onset 30–60 min, peak 2–4h, duration 6–8h):
  Regular (R) insulin: only insulin FDA-approved for IV infusion
  IV use: DKA management, hyperkalemia treatment, perioperative insulin infusion
  PO: must be given 30 min before meals (slower onset) → less convenient than rapid-acting

INTERMEDIATE-ACTING (NPH, onset 2–4h, peak 4–10h, duration 12–18h):
  NPH (protamine + regular): cloudy suspension; twice daily
  Significant peak → hypoglycemia risk; variable absorption
  Largely replaced by long-acting analogs but still used in some protocols

LONG-ACTING (basal insulin, onset 1–2h, nearly peakless, duration 18–24h or longer):
  Glargine (Lantus/Basaglar/Toujeo): precipitates at SC injection pH → slow absorption
    Toujeo (U-300): 3× concentrated → longer duration (~36h); less nocturnal hypoglycemia
  Detemir (Levemir): albumin-binding → extended action; twice daily (shorter t½ than glargine)
  Degludec (Tresiba): forms multi-hexamers → very long t½ (25h) → 42h duration → dosing flexibility

ULTRA-LONG (degludec): allows missed/varied dose timing; reduced hypoglycemia vs glargine

Concentration:
  U-100: 100 units/mL (standard)
  U-200: 200 units/mL (Humalog and Tresiba pens)
  U-300: 300 units/mL (Toujeo)
  U-500: 500 units/mL (for severe insulin resistance >200U/day)
  → Dose errors if concentration not accounted for
```

### Insulin Regimens

```
BASAL-BOLUS (physiologic, type 1 and type 2):
  Basal: long-acting (glargine/detemir/degludec) → ~50% of total daily dose
  Bolus: rapid-acting with each meal → ~50% of TDD (divided 3 meals)
  Correction: rapid-acting for high glucose (insulin sensitivity factor = ISF)

BASAL-ONLY (type 2):
  Starting dose: 0.1–0.2 U/kg/day; titrate by 2U every 3 days to fasting goal

PREMIXED INSULIN (e.g., 70/30 NPH/regular):
  Convenient but less flexible; twice daily; peaks unpredictable

CONTINUOUS SUBCUTANEOUS INSULIN INFUSION (CSII, insulin pump):
  Uses only rapid-acting analog
  Basal rate + boluses; most physiologic; requires carb counting + training
  CGM (continuous glucose monitor) integration → hybrid closed-loop / artificial pancreas
    Tandem Control-IQ, Omnipod 5: automated insulin delivery based on CGM data
```

---

## 2. Oral/Injectable Antidiabetics

### Metformin

```
Mechanism (multiple, still debated):
  Primarily: inhibits mitochondrial Complex I (electron transport) → ↓ ATP/AMP ratio
    → activates AMPK (AMP-activated protein kinase) → ↓ hepatic gluconeogenesis (key)
    → ↓ fatty acid synthesis, ↑ fatty acid oxidation, ↑ glucose uptake
  Also: ↓ intestinal glucose absorption; gut microbiome modification
  Inhibits mTOR pathway downstream of AMPK → possible longevity/cancer effects under study

Effects: ↓ fasting glucose (↓ HbA1c ~1–2%); weight neutral/modest weight loss; ↓ CV events
  (UKPDS: ↓ CVD in overweight T2DM — independent of glucose lowering)

Lactic acidosis:
  Rare (~10 cases/100,000 patient-years); metformin accumulates in mitochondria → ↑ lactate
  RISK FACTORS: eGFR <30 (dose reduce at <45, stop at <30), iodinated contrast media (hold 48h),
    acute illness causing reduced perfusion/hypoxia, liver failure, alcohol excess
  Recontrast: hold before IV contrast if eGFR 30–60 → check SCr 48h after → resume if stable
    eGFR >60: no need to hold (FDA updated guidance 2016)

Adverse: GI (nausea/diarrhea, 20–30%); take with food; extended-release reduces GI effects
  Vitamin B12 deficiency (~10–15% long-term use): check B12 annually if >5yr
  No hypoglycemia as monotherapy (requires insulin secretagogue)
```

### SGLT2 Inhibitors (Gliflozins)

```
Mechanism: Block SGLT2 (sodium-glucose cotransporter 2) in PCT
  → Renal glucose threshold ↓ from ~200 to ~50 mg/dL → glycosuria (70–80g glucose/day excreted)
  → Osmotic diuresis → ↓ plasma volume, ↓ BP, ↓ weight

Beyond glycosuria (cardio-renal benefits):
  ↓ HF hospitalizations + CV death (EMPA-REG OUTCOME, CANVAS, DECLARE-TIMI 58)
  ↓ Renal progression (CREDENCE, DAPA-CKD) — benefit even in non-diabetic CKD
  Mechanisms uncertain: ↓ pre/afterload, ↓ renal tubular injury (tubuloglomerular feedback),
    natriuresis, ↓ sympathetic activity, ketone fuel utilization, direct cardiac effects

HbA1c reduction: ~0.5–1%; modest compared to sulfonylureas/GLP-1 RAs

Adverse:
  Genital mycotic infections (glycosuria → yeast growth): common (8–10%); especially in women; treat topically
  UTI: modest increase (osmotic diuresis partially protective)
  DKA (euglycemic): rare but serious; glucose may be <250 (euglycemic) but profound ketonemia
    Risk: sick day rules (hold SGLT2i if illness, surgery, fasting), T1DM (off-label), very low carb diet
  Amputation risk (canagliflozin signal): CANVAS trial; ? volume depletion → peripheral ischemia
    Monitor feet carefully; consider stopping if amputation risk high
  Bone fractures (canagliflozin): ↓ calcium/phosphate handling signal
  Fournier's gangrene (necrotizing fasciitis of genitalia): rare FDA warning
```

### GLP-1 Receptor Agonists

```
Mechanism: GLP-1 (glucagon-like peptide 1) = incretin hormone from L-cells of small intestine
  Released after meals → stimulates GLP-1R (Gs-coupled):
    ↑ Insulin secretion (glucose-dependent — no hypoglycemia when glucose normal)
    ↓ Glucagon secretion
    ↓ Gastric emptying → ↑ satiety, ↓ appetite → weight loss
    Central effects: hypothalamic satiety signaling (arcuate nucleus)

Agents (short vs long-acting):
  Short-acting: exenatide BID, lixisenatide QD → primarily ↓ postprandial glucose
  Long-acting: dulaglutide (weekly), semaglutide (weekly SC or daily PO), liraglutide (daily)
    → Both postprandial + fasting glucose; more weight loss; CV benefits
  Semaglutide (Ozempic SC, Rybelsus PO): highest weight loss (~15% at 2.4mg weekly = Wegovy)
    Tirzepatide (Mounjaro/Zepbound): dual GLP-1/GIP agonist → ~20–22% weight loss

CV benefits (LEADER, SUSTAIN-6, REWIND, HARMONY): ↓ MACE in high-risk T2DM
  Liraglutide, semaglutide, dulaglutide: FDA-approved for CV risk reduction in T2DM

Adverse:
  GI: nausea, vomiting, diarrhea (dose-dependent; titrate slowly)
  Pancreatitis: FDA warning; elevated lipase; caution in prior pancreatitis
  Thyroid C-cell tumors: rodent data (MTC) → CI in personal/family history MEN2/MTC
  Gallbladder disease: ↑ risk of gallstones (rapid weight loss slows gallbladder motility)
  Gastroparesis worsening: ↓ gastric emptying → avoid in pre-existing gastroparesis
  Weight regain on stopping: 2/3 of lost weight returns within 1 year (STEP-4 extension data)

Contraindications: history of MTC, MEN2
```

### DPP-4 Inhibitors (Gliptins)

**Mechanism:** Inhibit DPP-4 (dipeptidyl peptidase-4), the enzyme that degrades endogenous GLP-1 and GIP → prolong incretin effect.

**Drugs:** Sitagliptin (Januvia), saxagliptin, alogliptin, linagliptin, vildagliptin.

**Effect:** Moderate HbA1c ↓ (~0.5–0.8%), weight neutral, low hypoglycemia risk.

**Adverse:** Heart failure hospitalization signal (saxagliptin in SAVOR-TIMI, alogliptin in EXAMINE — not all class members); joint pain; pancreatitis; linagliptin is only one cleared by biliary/renal mixed → safest in CKD.

### Sulfonylureas

**Mechanism:** Bind SUR1 subunit of K-ATP channel on β-cells → close K-ATP → membrane depolarization → Ca²⁺ influx → insulin exocytosis (glucose-independent → hypoglycemia risk).

**Drugs:** Glipizide, glyburide, glimepiride. Glyburide: active metabolites → ↑ hypoglycemia especially elderly/CKD. Glipizide preferred in elderly.

**Adverse:** Hypoglycemia (significant, especially long-acting), weight gain, rare SIADH.

### Pioglitazone (TZD)

**Mechanism:** PPARγ (peroxisome proliferator-activated receptor γ) agonist → ↑ adiponectin → ↑ insulin sensitivity in adipose/muscle/liver. ↑ GLUT4 translocation.

**Adverse:** Fluid retention (↑ risk of HF exacerbation — avoid in NYHA III-IV), weight gain, edema, ↑ fracture risk (women), possible bladder cancer signal (with long-term use).

**CV data:** PROactive trial: ↓ secondary endpoint (not primary) CV events.

---

## 3. Thyroid Drugs

### Hypothyroidism — Replacement

**Levothyroxine (T4):** Synthetic T4; once-daily PO; converts peripherally to T3 (active). Long t½ (~7 days) → stable levels; safe if doses missed. Take 30–60 min before breakfast (↑ absorption) or consistently at bedtime. Interactions: calcium/antacids/iron → ↓ absorption (separate by 4h).

**Liothyronine (T3):** Faster onset; shorter t½ (1 day); used in myxedema coma (IV); some prefer combo T4/T3 for residual symptoms.

**Target:** TSH in normal range (0.5–4.5 mIU/L). Subclinical hypothyroidism: treat if TSH >10 or symptomatic or pregnant.

**Pregnancy:** ↑ levothyroxine requirements by 25–50% (↑ TBG, fetal demands) → adjust dose early.

### Hyperthyroidism — Treatment

**Thionamides (antithyroid drugs):**
```
Methimazole (MMI): blocks thyroid peroxidase (TPO) → ↓ oxidation of iodide → ↓ thyroid hormone synthesis
  Also blocks coupling reaction (iodotyrosine → T3/T4)
  Once daily; preferred over PTU (except 1st trimester)
  Adverse: rash (common), agranulocytosis (0.3%), hepatotoxicity (rare), aplastic anemia

PTU (propylthiouracil): blocks TPO + blocks peripheral T4→T3 conversion (inhibits type 1 deiodinase)
  Preferred: thyroid storm (faster), 1st trimester (methimazole → choanal atresia/aplasia cutis risk)
  More frequent dosing (TID); hepatotoxic (black box for hepatic failure — less preferred long-term)
  PTU vs MMI in pregnancy: PTU in 1st trimester → MMI in 2nd/3rd
```

**Radioiodine (I-131):** Sodium iodide-131; taken PO → concentrated in thyroid → β-radiation → thyroid ablation (weeks-months). Most common treatment in US. Goal: hypothyroidism (then replace with levothyroxine). CI in pregnancy, active TED (thyroid eye disease: can worsen).

**β-blockers (propranolol preferred — also blocks T4→T3):** Symptomatic control (palpitations, tremor, anxiety, heat intolerance) while awaiting thionamide effect. Also preferred in thyroid storm.

**Thyroid storm:** Life-threatening decompensated hyperthyroidism. Treatment: PTU (load 500–1000mg, then 250mg q4h) + β-blocker (propranolol) + hydrocortisone (blocks T4→T3 conversion, relative adrenal insufficiency) + iodide (Lugol's solution or KI — 1h after PTU to avoid using iodine for synthesis).

**Potassium iodide (Wolff-Chaikoff effect):** High iodide transiently inhibits thyroid hormone synthesis → used in thyroid storm prep + radioiodine protection (nuclear emergencies).

---

## 4. Corticosteroids

### Glucocorticoid Mechanism

```
Cortisol / synthetic GCs bind cytoplasmic GR (glucocorticoid receptor) → nuclear translocation
  → Transactivation: GRE binding → ↑ anti-inflammatory genes (lipocortin/annexin A1, IκB)
  → Transrepression: ↓ NF-κB, ↓ AP-1 → ↓ pro-inflammatory cytokines (IL-1, IL-6, TNF, IL-8)

Anti-inflammatory effects:
  ↓ Arachidonic acid release (lipocortin → ↓ phospholipase A2)
  ↓ COX-2 expression
  ↓ Lymphocyte migration, ↓ macrophage activation, ↓ neutrophil chemotaxis
  ↓ Endothelial adhesion molecule expression

Metabolic effects: ↑ gluconeogenesis, ↑ proteolysis, ↑ lipolysis, ↑ bone resorption
```

### Dose Equivalencies and Mineralocorticoid Activity

| Drug | Anti-inflammatory potency | Mineralocorticoid potency | Duration |
|------|--------------------------|--------------------------|---------|
| Cortisol (hydrocortisone) | 1 | 1 | Short |
| Prednisone/prednisolone | 4 | 0.8 | Intermediate |
| Methylprednisolone | 5 | 0.5 | Intermediate |
| Triamcinolone | 5 | 0 | Intermediate |
| Dexamethasone | 25 | 0 | Long (t½ ~36h) |
| Fludrocortisone | 10 | 125–150 | Intermediate |
| Betamethasone | 25 | 0 | Long |

**Dexamethasone uses:** Brain edema (cerebral), COVID-19 (RECOVERY trial — ↓ mortality in severe/mechanically ventilated), fetal lung maturity (24–34 weeks gestation), adrenal suppression test (overnight dex suppression test — 1mg at midnight → cortisol at 8am; normal <1.8 μg/dL), nausea/vomiting (CINV, PONV), croup (racemic epinephrine + dex IM/PO).

**HPA axis suppression:**
```
Exogenous GC → ↑ plasma cortisol
  → Negative feedback on hypothalamus (↓ CRH) + pituitary (↓ ACTH)
  → Adrenal cortex atrophy (disuse)

Duration threshold for suppression:
  Single dose: no significant suppression
  <10mg/day prednisone equivalent: minimal risk
  >20mg/day for >3 weeks: likely suppression
  Taper required: don't abruptly stop → adrenal crisis if suppressed

Adrenal crisis: vasomotor collapse, hypoglycemia, hyponatremia, hyperkalemia
  Treatment: hydrocortisone 100mg IV → 50mg q8h then taper
  "Sick day rules": double dose during illness/surgery
```

**Corticosteroid adverse effects (dose/duration-dependent):**

| System | Effect |
|--------|--------|
| Metabolic | Hyperglycemia (steroid DM), dyslipidemia, truncal obesity, Cushing habitus |
| Bone | Osteoporosis (↓ Ca absorption, ↑ osteoclast activity, ↓ osteoblast activity); avascular necrosis of femoral head |
| GI | Peptic ulcers (especially + NSAIDs); GI bleed |
| Immunologic | Immunosuppression → opportunistic infections; TB reactivation (TNFi+steroids > steroids alone) |
| Ophthalmologic | Posterior subcapsular cataracts; ↑ IOP → glaucoma |
| Neuropsychiatric | Euphoria, insomnia, psychosis (at high doses) |
| Skin | Easy bruising, thin skin, impaired wound healing, striae |
| Adrenal | HPA suppression (see above) |

**Inhaled corticosteroids (ICS):** Fluticasone, budesonide, beclomethasone. Local effect → first-pass hepatic metabolism of swallowed drug → minimal systemic absorption at standard doses. Rinse mouth (oral candidiasis), spacer device (↑ lung delivery, ↓ oropharyngeal deposition).

---

## 5. Osteoporosis Drugs

### Bisphosphonates

**Mechanism:** Structural analogs of pyrophosphate → accumulate in bone matrix → ingested by osteoclasts during resorption → intracellular inhibition:
- **Non-nitrogen-containing** (etidronate): converted to non-hydrolyzable ATP analog → toxic to osteoclast
- **Nitrogen-containing** (alendronate, risedronate, ibandronate, zoledronate): inhibit farnesyl pyrophosphate synthase → ↓ prenylation of GTP-binding proteins → osteoclast apoptosis

**Drugs and administration:**
- Alendronate: weekly PO (70mg); risedronate: weekly/monthly PO
- Ibandronate: monthly PO or quarterly IV
- Zoledronate (Reclast): annual IV infusion; most potent; acute-phase reaction (flu-like) after first dose (prevented by acetaminophen)

**Duration (bisphosphonate holiday):**
- After 5 years (oral) or 3 years (IV zoledronate): consider drug holiday in low-risk patients
- Risk of atypical femoral fracture ↑ with prolonged use (10yr) → holiday allows bone renewal
- High-risk patients (prior fracture, T-score < -2.5): continue or switch to anabolic agent

**Adverse:**
- **Esophagitis:** Must remain upright 30–60 min after PO dose; full glass water; CI in achalasia/esophageal dysmotility
- **ONJ (osteonecrosis of the jaw):** Uncommon; ↑ with IV bisphosphonates, cancer patients, dental procedures → dental exam before starting
- **Atypical femoral fracture (AFF):** Rare; stress fracture after >5 years; dull thigh pain prodrome
- Hypocalcemia (IV forms → transient ↓ Ca)
- Acute-phase reaction (IV zoledronate): flu-like 24–72h → NSAID/acetaminophen

### Denosumab (Prolia)

**Mechanism:** Fully human mAb targeting RANKL (receptor activator of NF-κB ligand). RANKL binds RANK on osteoclast precursors → differentiation/activation. Denosumab blocks RANKL → ↓ osteoclast number and function → ↓ bone resorption.

**Administration:** 60mg SC every 6 months.

**Advantages:** Any renal function (no renal clearance), more potent than bisphosphonates in some studies.

**Critical issue — discontinuation:** Stopping denosumab → RANKL rebound → massive osteoclast activation → vertebral fracture surge within 12–18 months after stopping. Must transition to bisphosphonate if stopping denosumab.

### Teriparatide/Abaloparatide (Anabolic Agents)

**Teriparatide (Forteo):** Recombinant PTH 1-34; SC daily injection; preferentially stimulates osteoblasts (intermittent PTH → anabolic; continuous PTH → catabolic). Black box: osteosarcoma in rats → CI >2yr, history of bone cancer/Paget's/prior radiation.

**Abaloparatide (Tymlos):** PTHrP analog; SC daily; similar efficacy; lower hypercalcemia incidence.

**Romosozumab (Evenity):** Sclerostin inhibitor (sclerostin ↓ Wnt signaling → inhibits osteoblasts); monthly SC × 12 months; dual mechanism (↑ bone formation + ↓ resorption); CV risk signal → CI in prior MI/stroke within 1 year.

### SERMs

**Raloxifene (Evista):** SERM — estrogen agonist in bone (↑ BMD, ↓ fractures), antagonist in breast (↓ breast cancer risk — used in high-risk women). No uterine stimulation (unlike tamoxifen). ↑ DVT/PE risk (like estrogen). Vasomotor symptoms can worsen. Spine fracture reduction; modest hip fracture data.

---

## 6. Uric Acid / Gout

### Acute Gout Treatment

```
NSAIDs: indomethacin/naproxen — first-line; avoid in CKD/peptic ulcer/elderly
Colchicine:
  Mechanism: binds tubulin → ↓ microtubule polymerization → ↓ neutrophil motility, ↓ inflammasome
    assembly (↓ IL-1β release), ↓ neutrophil adhesion/chemotaxis
  Use: acute attack (<24h from onset); low-dose proven equivalent to high-dose (Terkeltaub RCT)
    Low dose: 1.2mg then 0.6mg 1h later (total 1.8mg)
    High dose: 0.6mg q1h × 6 doses (≥8mg total — outdated)
  Adverse: GI (diarrhea, nausea); myopathy (especially with CYP3A4 inhibitors → ↑ colchicine levels);
    bone marrow suppression (overdose)
  Drug interactions: macrolides (CYP3A4/P-gp inhibitors) → ↑ colchicine toxicity
Corticosteroids: methylprednisolone/prednisone — if NSAIDs/colchicine CI; IM or PO; joint injection
```

### Urate-Lowering Therapy (Prophylaxis)

**Start ULT 2–4 weeks after acute attack resolves (starting during acute attack can prolong/worsen flare).**

**Target:** Uric acid (urate) <6 mg/dL (or <5 in tophaceous gout).

**Allopurinol:**
- Competitive inhibitor of xanthine oxidase → ↓ uric acid synthesis
- Active metabolite: oxypurinol (renally cleared → dose reduce in CKD)
- Start low (100mg/day) → titrate monthly to target → dose up to 800mg/day
- **Allopurinol hypersensitivity syndrome (AHS):** Life-threatening SJS/TEN/organ failure; HLA-B*5801 (Asian, Black populations) → screen before starting; start low dose + slow titration ↓ risk
- Drug interaction: ↑ azathioprine/6-MP toxicity (xanthine oxidase inactivates these → TPMT inhibition needed if co-prescribed)

**Febuxostat:**
- Non-purine xanthine oxidase inhibitor; more potent than allopurinol; no dose adjust in mild-moderate CKD
- CARES trial: ↑ CV mortality vs allopurinol → not for patients with CVD (FDA boxed warning)
- Alternative in allopurinol allergy (non-cross-reactive)

**Probenecid:**
- Uricosuric: inhibits URAT1 (urate transporter in PCT) → ↓ urate reabsorption → ↑ urinary urate excretion
- Adequate hydration required (↑ urinary uric acid → nephrolithiasis risk if low urine output)
- Only for under-excreters (24h urine uric acid <800mg/day); useless if eGFR <30; drug interactions (↑ β-lactam levels by same transporter)

**Pegloticase (Krystexxa):** PEGylated uricase (recombinant); converts urate → allantoin (soluble → excreted); for severe refractory gout; IV infusion biweekly; anaphylaxis risk; anti-drug antibody development → check uric acid before each infusion (if urate ↑ → antibodies developing → stop to avoid infusion reactions); often used with low-dose MTX or MMF to reduce immunogenicity.

---

## Decision Cheat Sheet

| Condition | First-Line Drug | Key Notes |
|-----------|----------------|-----------|
| T2DM, no major complications | Metformin | First-line; add SGLT2i if HF/CKD, GLP-1 RA if weight/MACE |
| T2DM + HF | SGLT2i (empagliflozin, dapagliflozin) | Reduces HF hospitalization, CV death |
| T2DM + CKD (eGFR >20) | SGLT2i (dapagliflozin, canagliflozin) | Slows CKD progression; CREDENCE/DAPA-CKD |
| T2DM + ASCVD/high CV risk | GLP-1 RA (semaglutide, liraglutide) | MACE reduction proven |
| T2DM + obesity | GLP-1 RA or tirzepatide | Most weight loss (~15–22%) |
| T1DM basal | Insulin degludec or glargine | Peakless, predictable |
| Hyperthyroidism | Methimazole (not 1st trimester) | PTU in 1st trimester or thyroid storm |
| Hypothyroidism | Levothyroxine | TSH target 0.5–4.5; ↑ dose in pregnancy |
| Thyroid storm | PTU + propranolol + hydrocortisone + iodide (wait 1h after PTU) | |
| Osteoporosis | Alendronate or zoledronate | Severe (T-score < -3.0, vertebral fracture): teriparatide first |
| Acute gout | NSAIDs or colchicine (low dose) | Start within 24h for best effect |
| Chronic gout prevention | Allopurinol (titrated to <6 mg/dL) | Screen HLA-B*5801 in high-risk populations |

---

## Common Confusion Points

**Metformin and contrast:** Old guidelines said hold all metformin before any contrast. Current: hold only if eGFR 30–60 (assess risk); no need to hold if eGFR >60. IV contrast causes transient renal ↓ → metformin accumulation → lactic acidosis risk in marginal renal function.

**SGLT2i DKA is euglycemic:** Glucose can be <200 mg/dL, yet patient has severe DKA (high anion gap, low pH, ketones). Mechanism: ↑ glucagon (hypoinsulinemia from osmotic diuresis), ↑ ketogenesis, ↑ lipolysis. Test for ketones even if glucose seemingly "OK."

**GLP-1 RA vs DPP-4i:** GLP-1 RAs provide pharmacologic (supraphysiologic) GLP-1 levels → much stronger effect (↓ HbA1c 1–2% vs 0.5–0.8%), weight loss (GLP-1 RAs↓ weight, DPP-4i neutral). Both glucose-dependent → no hypoglycemia as monotherapy.

**Allopurinol and azathioprine:** Azathioprine (6-MP) is metabolized by xanthine oxidase. Allopurinol blocks XO → massive ↑ 6-MP levels → severe myelosuppression. Reduce azathioprine dose to 25% if must co-prescribe, or use different ULT agent. This is a potentially fatal interaction.

**Bisphosphonate holiday:** NOT for all patients. Holiday reduces atypical femoral fracture risk but increases vertebral fracture risk in high-risk patients. Framework: oral bisphos 5 years or IV zoledronate 3 years → reassess; holiday only if T-score improved and no prior vertebral fracture.

**Denosumab discontinuation syndrome:** Unlike bisphosphonates (long half-life in bone), denosumab has no reservoir → RANKL rebound within 6 months of missing dose. Must have a plan for transition before prescribing.
