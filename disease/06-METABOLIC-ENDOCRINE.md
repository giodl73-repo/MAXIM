# Metabolic and Endocrine Disease

## The Big Picture

```
METABOLIC/ENDOCRINE DISEASE = dysregulation of feedback control systems

Most diseases here are:
  Feedback loop failures (thyroid, adrenal, pancreas)
  Receptor resistance (insulin resistance, leptin resistance)
  Enzymatic defects (lysosomal storage, inborn errors)
  Ectopic secretion (pheo, ectopic ACTH)
  Autoimmune destruction of glands (T1DM, Hashimoto, Addison)

COMMON THREAD: most manageable with hormone replacement or pharmacological modulation
  → Unlike cancer or infection, often chronic maintenance rather than cure
```

---

<!-- @editor[bridge/P2]: No old-world bridge -- endocrine disease as feedback control system failure (negative feedback disruption, set-point drift, receptor desensitization) maps directly to control theory (PID loops, gain, damping) -->

## Diabetes Mellitus

### Type 1 Diabetes: Autoimmune Destruction

```
MECHANISM:
  Autoimmune destruction of pancreatic β cells
  CD4+ T cells: help activate autoreactive CD8+ CTLs + B cells
  CD8+ CTLs: directly kill β cells (Fas/FasL, perforin/granzyme)
  Autoantibodies (markers, not always pathogenic):
    Anti-GAD65 (glutamic acid decarboxylase): most sensitive
    Anti-IA-2 / anti-islet (ICA)
    Anti-insulin (IAA): especially in children
    Anti-ZnT8 (zinc transporter 8): newer

HLA ASSOCIATIONS:
  HLA-DR3/DQ2 and HLA-DR4/DQ8: highest risk (7× ↑)
  HLA-DR2: protective
  ~50% concordance in identical twins → environment + trigger also required

PATHOPHYSIOLOGY:
  Complete/near-complete β-cell loss → absolute insulin deficiency
  No insulin → no GLUT4 translocation in muscle/fat → hyperglycemia
  No insulin → lipolysis unrestrained → FFA → liver → β-oxidation → acetyl-CoA → KETONES
  → DIABETIC KETOACIDOSIS (DKA)
  Glucagon not suppressed (insulin normally suppresses α cells) → ↑↑ gluconeogenesis + ketogenesis
```

### Diabetic Ketoacidosis (DKA)

```
PRECIPITANTS: new T1DM diagnosis, insulin omission, infection, MI, surgery

PATHOPHYSIOLOGY:
  Insulin ↓↓ + glucagon ↑↑ → lipolysis + proteolysis
  FFA → liver → β-oxidation → acetyl-CoA → ketogenesis:
    Acetyl-CoA → acetoacetate + β-hydroxybutyrate + acetone
  Ketoacids: H+ accumulation → metabolic acidosis (high AG)
  Hyperglycemia → osmotic diuresis → dehydration (4-8 L fluid deficit typical)
  K+ depletion (total body low despite possible normal/high serum K+ — insulin drives K+ into cells)

LABS:
  Glucose typically > 250-300 mg/dL
  pH < 7.3, HCO₃⁻ < 18, AG > 12
  Serum/urine ketones
  K+ — check before giving insulin (must correct if low; insulin will lower K+ further → fatal arrhythmia)

MANAGEMENT (3 Fs):
  Fluids: NS initially (correct dehydration) → switch to D5NS when glucose ~200-250
  Electrolytes: K+ replacement aggressively (target K+ 3.5-5.5 before insulin)
  Fixed rate insulin infusion: 0.1 U/kg/hr IV (regular insulin) → address hyperglycemia + stop ketogenesis
  Bicarbonate: controversial, usually not needed unless pH < 6.9
```

### Type 2 Diabetes: Insulin Resistance

```
PATHOPHYSIOLOGY:
  Phase 1: Insulin resistance (IR) in target tissues (liver, muscle, fat)
    Molecular mechanisms of IR:
      Ectopic lipid accumulation (in muscle + liver) → ceramide + DAG → PKC activation
      → serine phosphorylation of IRS-1 (instead of tyrosine) → blocks PI3K/Akt pathway
      Inflammatory cytokines (TNF-α, IL-6 from VAT) → similar IRS-1 serine phosphorylation
      mTOR/S6K1 feedback: chronic activation → phosphorylate IRS-1 → negative feedback on insulin signaling
    Result: glucose uptake impaired in muscle; liver continues gluconeogenesis despite hyperinsulinemia

  Phase 2: Compensatory hyperinsulinemia — β cells work harder to overcome IR
    Glucolipotoxicity: chronic ↑ glucose + FFA → ER stress, oxidative stress in β cells
    → β-cell apoptosis → progressive β-cell mass loss

  Phase 3: Relative insulin deficiency + IR → overt T2DM
    Eventually may need insulin (≠ Type 1 — still some β-cell function usually)

NATURAL HISTORY: Insulin resistance → IFG/IGT → T2DM → complications
PREVENTION: lifestyle modification (diet + exercise) reduces progression 58% (DPP trial)
```

### Hyperosmolar Hyperglycemic State (HHS)

```
T2DM equivalent of DKA (but different):
  Some residual insulin → prevents ketogenesis (ketones minimal/absent)
  But extreme hyperglycemia (glucose often > 600-1000 mg/dL) → profound osmotic diuresis
  → Severe dehydration + hyperosmolality (> 320 mOsm/kg)
  → Altered consciousness/coma from brain dehydration
  Much more severe dehydration than DKA (10-12 L fluid deficit)
  Mortality higher than DKA (~5-15% vs ~1%)
  Treatment: aggressive IV fluids (0.9% NS initially, then 0.45%) + insulin
```

### Diabetic Complications

```
MICROVASCULAR (from hyperglycemia → protein glycation, polyol pathway, oxidative stress):
  Retinopathy: microaneurysms → exudates → neovascularization (proliferative DR)
    → vitreous hemorrhage / tractional retinal detachment → blindness
    Laser photocoagulation / anti-VEGF (ranibizumab) for proliferative DR
  Nephropathy: microalbuminuria → proteinuria → glomerulosclerosis (Kimmelstiel-Wilson nodules)
    → CKD → ESRD (leading cause of ESRD in developed world)
    ACEi/ARB: standard of care for diabetic nephropathy (↓ efferent constriction → ↓ GFR stress)
    SGLT2 inhibitors: additional renoprotection
  Neuropathy: glove-and-stocking sensory neuropathy → loss of pain/temp → Charcot foot
    Autonomic: gastroparesis, orthostatic hypotension, sexual dysfunction, anhidrosis

MACROVASCULAR (from accelerated atherosclerosis):
  CVD: 2-4× risk of MI/stroke vs non-diabetic
  PAD: 20× risk of below-knee amputation
  All amplified by hypertension + dyslipidemia (metabolic syndrome)
```

---

## Metabolic Syndrome

```
DEFINITION (ATP III/AHA — meet 3 of 5):
  1. Abdominal obesity: waist ≥ 102 cm (M) / ≥ 88 cm (F)
  2. Fasting glucose ≥ 100 mg/dL or T2DM
  3. BP ≥ 130/85 mmHg or on treatment
  4. TG ≥ 150 mg/dL
  5. HDL < 40 mg/dL (M) / < 50 mg/dL (F)

UNIFYING MECHANISM: Visceral adipose tissue (VAT) dysfunction
  VAT ≠ subcutaneous fat (metabolically inert)
  VAT: pro-inflammatory adipokine secretion (TNF-α, IL-6, CRP, resistin)
  ↓ Adiponectin (insulin-sensitizing, anti-inflammatory) from enlarged adipocytes
  Portal drainage of FFA from VAT → liver → insulin resistance + dyslipidemia (↑ TG, ↓ HDL)

  ATHEROGENIC DYSLIPIDEMIA (triad):
    ↑ Triglycerides: ↑ VLDL output from liver (IR → ↑ fatty acid flux to liver)
    ↓ HDL: CE transfer from HDL to VLDL (↑ CETP activity) → HDL particles smaller + fewer
    ↑ sdLDL (small dense LDL): TG-enriched LDL → hepatic lipase cleaves → small, more atherogenic

Prevalence: ~35% of US adults (MetS); ~1 billion globally
```

---

## Thyroid Disorders

### Hypothyroidism

```
HASHIMOTO'S THYROIDITIS (most common cause in iodine-replete countries):
  Autoimmune: CD4+ Th1 → macrophage activation; CD8+ CTL → thyrocyte killing
  Autoantibodies: anti-TPO (thyroid peroxidase) — 95%+; anti-thyroglobulin (60%)
  Anti-TSH receptor blocking antibodies (minority)
  Histology: lymphocytic infiltration + germinal centers + Hürthle cell change (oxyphilic metaplasia)
  Progression: subclinical (↑ TSH, normal T4) → overt hypothyroidism (↑ TSH, ↓ fT4)
  Association: ↑ risk thyroid lymphoma (rare but 60× vs general population)

OTHER CAUSES:
  Iodine deficiency: most common worldwide cause of hypothyroidism (goiter + cretinism)
  Post-thyroidectomy / post-radioiodine
  Central hypothyroidism: ↓ TSH + ↓ T4 (pituitary or hypothalamic failure)
  Medications: lithium, amiodarone, interferons, checkpoint inhibitors

SYMPTOMS:
  Fatigue, cold intolerance, constipation, weight gain, bradycardia, depression
  Myxedema: non-pitting edema (mucopolysaccharide accumulation in skin)
  Myxedema coma: severe decompensation (hypothermia, altered consciousness, hypoventilation)

TREATMENT: levothyroxine (synthetic T4); TSH-guided dosing
```

### Hyperthyroidism

```
GRAVES' DISEASE (most common cause):
  Autoimmune: TSI (thyroid-stimulating immunoglobulin) = IgG antibodies against TSH receptor
  → Activating antibodies → mimic TSH → ↑ T3/T4 synthesis + thyroid growth (goiter)
  Unique features (distinguish from other causes):
    Exophthalmos (proptosis): orbital fibroblast infiltration (TSH-R on orbital fibroblasts + GAG accumulation)
    Pretibial myxedema: dermopathy
    Thyroid acropachy (rare): clubbing + periosteal bone formation

OTHER CAUSES:
  Toxic multinodular goiter: autonomous hot nodules (↑ T3/T4, suppressed TSH)
  Toxic adenoma: single autonomous nodule
  Subacute thyroiditis (de Quervain): viral → destruction → release of stored T3/T4 → transient hyperthyroid
  Thyrotoxicosis factitia: exogenous T4 ingestion (suppressed TG differentiates from intrinsic disease)
  Amiodarone: contains 37% iodine → type 1 (Jod-Basedow: extra iodine → excess synthesis) or type 2 (destructive)

SYMPTOMS:
  Heat intolerance, weight loss despite ↑ appetite, palpitations (AF), tremor, diarrhea
  Lid lag/lid retraction (adrenergic)
  Thyroid storm: fever, altered consciousness, extreme tachycardia — life-threatening

TREATMENT:
  Thionamides (propylthiouracil — PTU, methimazole/carbimazole): inhibit TPO + iodination
    PTU also blocks T4→T3 conversion (preferred in pregnancy 1st trimester, thyroid storm)
  β-blockers: symptom control (↓ adrenergic symptoms, ↓ HR) — propranolol also ↓ T4→T3
  Radioiodine (¹³¹I): ablates thyroid (preferred definitive treatment in USA for Graves)
  Surgery (thyroidectomy): large goiter, pregnant, failed medical management
```

---

## Adrenal Disease

### Adrenal Insufficiency (AI)

```
PRIMARY AI — ADDISON'S DISEASE:
  Destruction of adrenal cortex → ↓ cortisol, ↓ aldosterone, ↓ DHEA
  Causes: Autoimmune (most common in developed world, 80%) — anti-21-hydroxylase Ab
           TB (most common worldwide historically); HIV/CMV/fungi (AIDS)
           Hemorrhage: Waterhouse-Friderichsen (bilateral adrenal hemorrhage in septicemia, esp. meningococcemia)
  ACTH ↑↑ (no cortisol feedback) → MSH co-released from POMC → HYPERPIGMENTATION (buccal mucosa, sun-exposed, scars)
  Lab: ↓ Na (aldosterone loss), ↑ K (aldosterone loss), ↓ glucose, ↑ eosinophils
  Adrenal crisis: hypotension + hyponatremia + shock; treat with IV hydrocortisone + NS

SECONDARY AI:
  Pituitary failure → ↓ ACTH → ↓ cortisol (adrenal atrophy)
  Aldosterone PRESERVED (regulated by RAAS, not ACTH) → no hyperkalemia or hyperpigmentation
  No ACTH → no MSH → no hyperpigmentation (distinction from primary AI)
  Common cause: long-term exogenous steroid therapy → HPA axis suppression → abrupt withdrawal = secondary AI

TERTIARY AI:
  Hypothalamic failure → ↓ CRH → ↓ ACTH → ↓ cortisol
```

### Cushing Syndrome and Disease

```
CUSHING SYNDROME: excess cortisol from any source
  Exogenous (iatrogenic): most common cause overall — chronic steroid therapy
  Endogenous:
    ACTH-dependent (80%):
      Cushing DISEASE: pituitary corticotroph adenoma → ↑ ACTH → bilateral adrenal hyperplasia
      Ectopic ACTH: small cell lung cancer, carcinoid, pheo, medullary thyroid CA
    ACTH-independent (20%):
      Adrenal adenoma or carcinoma → autonomous cortisol secretion → ↓↓ ACTH (suppressed)

DIAGNOSIS ALGORITHM:
  Step 1: Confirm hypercortisolism:
    24-hr urine free cortisol (UFC) — elevated
    Late-night salivary cortisol — elevated (should be nadir at midnight)
    Overnight low-dose DST (1 mg dexamethasone at 11 PM → AM cortisol < 1.8 μg/dL in normal)

  Step 2: ACTH level:
    ↑ ACTH → ACTH-dependent
    ↓/undetectable ACTH → ACTH-independent (adrenal tumor)

  Step 3: If ACTH-dependent → distinguish pituitary vs ectopic:
    High-dose DST (8 mg): pituitary adenoma suppresses (> 50% ↓ cortisol); ectopic does not
    CRH stimulation: pituitary responds with ↑ ACTH; ectopic does not
    IPSS (inferior petrosal sinus sampling): central:peripheral ACTH gradient > 2:1 = pituitary source

CLINICAL FEATURES:
  Central obesity (buffalo hump, moon face), skin striae (purple, > 1 cm wide), bruising
  Proximal myopathy, osteoporosis, hypertension, DM, immunosuppression
  Women: hirsutism, acne, menstrual irregularity (adrenal androgens)
```

### Pheochromocytoma

```
Catecholamine-secreting tumor of adrenal medulla (or paraganglioma if extra-adrenal)

"RULE OF 10s" (historically; now known to be inaccurate but embedded in lore):
  10% bilateral, 10% malignant, 10% extra-adrenal, 10% pediatric, 10% familial
  Updated: ~25% are hereditary (VHL, RET/MEN2, NF1, SDH gene mutations)

SYMPTOMS: episodic (paroxysmal):
  Headache, hypertension (sustained or paroxysmal), diaphoresis, palpitations (5 Ps → actually 4: headache, HTN, hyperhidrosis, palpitations)
  "Hypertensive crises" precipitated by palpation, exercise, anesthesia, contrast dye, certain drugs (β-blockers — block vasodilatory β2 → unmasked α1 vasoconstriction → crisis)

BIOCHEMISTRY:
  Produce: epinephrine (if adrenal medulla), NE (extra-adrenal or adrenal), dopamine (malignant)
  Diagnosis: plasma free metanephrines OR 24-hr urine fractionated metanephrines (highest sensitivity)
  Biochemical diagnosis first, then imaging (CT/MRI, MIBG scintigraphy, Ga-DOTATATE PET)

PRE-OPERATIVE MANAGEMENT (critical — surgery without prep → hypertensive crisis death):
  1. α-blockade FIRST (phenoxybenzamine or prazosin/doxazosin — minimum 7-14 days)
  2. Then β-blockade (NEVER β-block before α-block — would leave α1 unopposed → hypertensive crisis)
  3. Volume loading (patients are volume-depleted from chronic catecholamine-induced vasoconstriction)
  Treatment: surgical resection
```

---

## Obesity and Weight Regulation

```
ADIPOKINES:
  LEPTIN (from adipocytes): satiety signal
    ↑ fat mass → ↑ leptin → hypothalamic arcuate nucleus → ↓ appetite + ↑ energy expenditure
    LEPTIN RESISTANCE: obese humans have high leptin but impaired signaling at hypothalamus
    (analogous to insulin resistance) → doesn't correct appetite
  ADIPONECTIN (from adipocytes): insulin-sensitizing, anti-inflammatory
    ↓ in obesity → contributes to IR + CVD risk
    ↑ with exercise, weight loss, TZDs

GUT HORMONES:
  GHRELIN: "hunger hormone" — stomach → ↑ before meals, ↓ after
    Only known peripheral orexigenic (appetite-stimulating) hormone
    Paradox: obese individuals have lower fasting ghrelin (expected? no — but meal suppression blunted)
  GLP-1 + PYY: post-meal anorexigenic signals (↓ appetite)
    Bariatric surgery (Roux-en-Y) → ↑↑ GLP-1/PYY → major mechanism of metabolic benefit beyond restriction

PHARMACOLOGY:
  GLP-1 receptor agonists (semaglutide, liraglutide, tirzepatide):
    Tirzepatide = GLP-1 + GIP dual agonist → 15-20% body weight loss in trials
    Also: ↓ appetite (hypothalamic action), ↓ gastric emptying, ↑ insulin, ↓ glucagon
  Naltrexone-bupropion (Contrave): combined opioid antagonist + dopamine/NE reuptake inhibitor
  Orlistat: lipase inhibitor → 30% fat malabsorption
  Bariatric surgery: most effective long-term (Roux-en-Y, sleeve gastrectomy)
```

---

## Gout and Hyperuricemia

```
URIC ACID METABOLISM:
  Purines (ATP → AMP → IMP; dietary purines) → xanthine → uric acid
  Xanthine oxidase: final step (drug target: allopurinol = XO inhibitor; febuxostat = XO inhibitor)
  Urate: final catabolite in humans (no uricase, unlike most other mammals → must excrete)
  Excretion: 70% renal, 30% GI
  Hyperuricemia: overproduction OR underexcretion (most common: 90%)

GOUT PATHOGENESIS:
  Serum uric acid > 6.8 mg/dL → supersaturation → MONOSODIUM URATE (MSU) crystal deposition
  MSU crystals: needle-shaped, negatively birefringent (yellow under polarized light parallel to axis)
    ↓
  Crystals engulfed by neutrophils/macrophages → NLRP3 inflammasome → caspase-1 → IL-1β
  → Acute intense inflammatory arthritis (1st MTP joint = podagra, most classic)
  → Fever, warmth, erythema, swelling — can mimic septic arthritis

STAGES:
  Asymptomatic hyperuricemia → Acute flare (MTP, ankle, knee) → Intercritical → Chronic tophaceous gout
  Tophi: monosodium urate deposits in soft tissue (ear helix, olecranon, Achilles)

TREATMENT:
  Acute flare: colchicine (early, < 12-24 hr); NSAIDs; corticosteroids if contraindications
    Colchicine: blocks tubulin polymerization → inhibits neutrophil motility + NLRP3 activation
  Urate-lowering therapy (after ≥ 2 flares): allopurinol (first-line); febuxostat; probenecid (uricosuric)
  Target: serum urate < 6 mg/dL (< 5 for tophaceous gout)
  Triggers: alcohol (esp. beer/spirits), organ meats, seafood, diuretics, cyclosporine, low-dose aspirin
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| DKA vs HHS: key distinction? | DKA: T1DM, significant ketoacidosis (pH < 7.3), less severe hyperglycemia. HHS: T2DM, minimal ketones, extreme hyperglycemia + osmolality, more profound dehydration |
| Graves vs Hashimoto's: same HLA? | Graves: HLA-DR3/DQ2. Hashimoto: HLA-DR4/DR5. Different though both autoimmune thyroid. |
| Why give α-blocker before β-blocker in pheo? | β-blockade without α-blockade → removes vasodilatory β2 effect → unopposed α1 vasoconstriction → hypertensive crisis → stroke/death |
| Addison vs secondary AI: hyperpigmentation present? | Only PRIMARY Addison's → ↑ ACTH → MSH from POMC → hyperpigmentation. Secondary/tertiary AI: ↓ ACTH → no hyperpigmentation. |
| Insulin in DKA: start immediately? | Check K+ first. Insulin drives K+ into cells. If serum K+ < 3.5, give K+ replacement first — otherwise risk fatal hypokalemia-induced arrhythmia |
| MSU crystals vs CPPD: how to differentiate? | Gout: MSU = negatively birefringent needles. Pseudogout (CPPD): calcium pyrophosphate = positively birefringent rhomboids. Both are joint fluid crystal analysis. |

---

## Common Confusion Points

**Cushing disease vs Cushing syndrome: precise usage**
Cushing disease: pituitary ACTH-secreting adenoma specifically (subset of Cushing syndrome).
Cushing syndrome: any cause of excess cortisol (exogenous, adrenal, ectopic, or pituitary).
Most exams use "Cushing syndrome" for the general entity and "Cushing disease" only for the pituitary form.

**HbA1c: what it measures and its limitations**
HbA1c = proportion of hemoglobin glycated at N-terminal valine of β chain; reflects average blood glucose over ~3 months (RBC lifespan). Limitations: hemolytic anemia/hemoglobinopathies (falsely low); iron deficiency/renal failure (falsely high); recent transfusion confounds. Not valid for diagnosis in hemolytic states.

**Metabolic syndrome → not a disease per se**
MetS is a cluster of risk factors that multiply CVD/T2DM risk. It's a clinical construct, not a single disease mechanism. Individual components (HTN, dyslipidemia, IR) are each treated on their own merits.

**Type 2 DM with insulin: not the same as Type 1**
T2DM patients who need insulin still have some residual β-cell function, insulin resistance as the primary problem, and are not prone to DKA under ordinary circumstances (some insulin present suppresses ketogenesis). They can develop HHS (the T2 decompensation equivalent).
