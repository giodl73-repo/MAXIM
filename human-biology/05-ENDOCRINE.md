# Endocrine System

## The Big Picture

```
ENDOCRINE SYSTEM = slow broadcast signaling via bloodstream
(contrast: nervous = fast, wired; paracrine = local; immune = targeted)

Signal timescale: minutes to hours to days
Amplification: 1 hormone molecule can activate thousands of downstream effects

HIERARCHY:
┌──────────────────────────────────────────────────────────┐
│  HYPOTHALAMUS (master controller)                        │
│  CRH, TRH, GnRH, GHRH, somatostatin, dopamine           │
│               ↓↓ portal blood (short circuit)            │
│  ANTERIOR PITUITARY (6 hormones)                        │
│  ACTH, TSH, LH, FSH, GH, Prolactin                     │
│               ↓↓ systemic blood                          │
│  PERIPHERAL GLANDS                                       │
│  Adrenal · Thyroid · Gonads · Liver/IGF-1               │
│               ↓↓ feedback                                │
│  (long loop to hypothalamus + pituitary; short loop)    │
└──────────────────────────────────────────────────────────┘

POSTERIOR PITUITARY: not a gland — stores hypothalamic hormones
  ADH (vasopressin) + Oxytocin — made in hypothalamus, stored/released here
```

---

## Hormone Chemistry and Receptor Types

### Three Chemical Classes

| Class | Examples | Synthesis | Solubility | Receptor location | Effect speed |
|-------|----------|-----------|-----------|-------------------|--------------|
| Peptide/protein | Insulin, GH, PTH, TSH, ADH, glucagon | Ribosome → ER → Golgi → secretory vesicles | Hydrophilic | Cell membrane (GPCR, RTK, cytokine-R) | Fast (seconds-minutes); can't cross membrane |
| Steroid | Cortisol, aldosterone, estrogen, testosterone, calcitriol | Cholesterol → mitochondria/ER; requires cholesterol | Lipophilic | Intracellular (nuclear receptors) | Slow (hours; gene transcription) |
| Amine | Thyroid hormone (T3/T4), catecholamines (NE, epi, dopamine) | Amino acid (tyrosine) derivatives | T3/T4: lipophilic despite amine; catecholamines: hydrophilic | T3/T4: nuclear; catecholamines: membrane | T3/T4: slow (gene); catecholamines: fast |

### Receptor Signaling Mechanisms

```
GPCR (G protein-coupled receptor):
  Hormone binds → conformational change → activates Gα
  Gs → adenylyl cyclase → ↑ cAMP → PKA → phosphorylation cascade
  Gi → inhibit adenylyl cyclase → ↓ cAMP
  Gq → phospholipase C → IP₃ + DAG → Ca²⁺ release + PKC

RTK (receptor tyrosine kinase):
  Insulin receptor, IGF-1R
  Ligand binding → dimerization → autophosphorylation
  → PI3K/Akt/mTOR pathway (glucose transport, protein synthesis, survival)
  → Ras/MAPK/ERK pathway (growth, proliferation)

JAK-STAT:
  GH, prolactin, cytokines
  Receptor lacks intrinsic kinase → recruits JAK2
  JAK phosphorylates STAT → STAT dimerizes → nuclear translocation → gene transcription

Nuclear receptors (steroid + thyroid hormones):
  Hormone diffuses into cell → binds cytoplasmic receptor → translocation to nucleus
  → Hormone-receptor complex binds HRE (hormone response element) on DNA
  → Activates or represses transcription → new protein synthesis (hours)
  Thyroid hormone receptors: constitutively nuclear, ligand-activated
```

---

## Hypothalamic-Pituitary Axes

### Axis Map

```
Hypothalamus → Anterior Pituitary → Peripheral → Feedback
─────────────────────────────────────────────────────────────
CRH          → ACTH              → Cortisol    → HPA axis
TRH          → TSH               → T3/T4       → HPT axis
GnRH (pulsatile) → LH + FSH     → Gonads      → HPG axis
GHRH / SST   → GH               → IGF-1 (liver) → GH axis
(Dopamine)   → (inhibits PRL)   → Prolactin   → PRL axis
```

### Pulsatility is Critical

GnRH must be pulsatile to stimulate LH/FSH. Continuous GnRH → downregulate GnRH receptors → suppress LH/FSH → castrate-equivalent.
Used clinically: GnRH agonists (initially stimulate, then suppress): prostate cancer, endometriosis, precocious puberty.

---

## Anterior Pituitary: Six Hormones

| Hormone | Stimulated by | Inhibited by | Target | Effect |
|---------|--------------|-------------|--------|--------|
| ACTH | CRH (stress, circadian) | Cortisol (−FB), somatostatin | Adrenal cortex | Cortisol + androgens synthesis |
| TSH | TRH | T3/T4 (−FB), somatostatin | Thyroid | T3/T4 synthesis + release |
| LH | GnRH (pulsatile) | Sex hormones (−FB) | Gonads | Testosterone (M); ovulation + corpus luteum (F) |
| FSH | GnRH (pulsatile) | Inhibin, sex hormones | Gonads | Spermatogenesis (M); follicle development (F) |
| GH | GHRH, ghrelin | Somatostatin, IGF-1 (−FB), glucose | Liver, muscle, fat, bone | IGF-1 production; lipolysis; protein synthesis; linear growth |
| Prolactin | Dopamine withdrawal, TRH, suckling | Dopamine (tonically inhibits) | Breast | Milk production; suppresses GnRH (lactational amenorrhea) |

**Sella turcica anatomy**: pituitary sits in a bony sella; expanding pituitary tumor compresses optic chiasm (bitemporal hemianopia) and compresses other pituitary cells (hypopituitarism).

---

## Posterior Pituitary

Made in hypothalamus, axons project to posterior pituitary (neurohypophysis), released there:

### ADH (Vasopressin / AVP)

```
Stimuli: ↑ plasma osmolality (osmoreceptors, threshold ~285 mOsm/kg)
         ↓ blood volume/pressure (baroreceptors — override osmolality in extremis)
         Pain, nausea, nicotine

Action:  V2 receptors (kidney collecting duct) → cAMP → insert aquaporin-2 (AQP2)
         → water reabsorption → dilute urine becomes concentrated

V1a receptors (vascular smooth muscle) → vasoconstriction (high doses)

Disorders:
  Diabetes insipidus (DI): ↓ ADH or ↓ V2 response → dilute polyuria + hypernatremia
    Central DI: ↓ ADH synthesis (head trauma, pituitary lesion) → treat with desmopressin
    Nephrogenic DI: normal ADH, nonfunctional V2/AQP2 (lithium toxicity, X-linked mutation)
  SIADH: ↑ ADH inappropriately → water retention → hyponatremia
```

### Oxytocin

Uterine contraction (parturition), milk ejection (let-down reflex), pair bonding, trust.
**Positive feedback**: stretch of uterine cervix → more oxytocin → more contraction → delivery (then placenta delivers, loop breaks).

---

## Thyroid: T3 and T4

```
SYNTHESIS:
  Thyroid follicular cells concentrate iodide (NIS symporter: 2 Na⁺ : 1 I⁻)
  Iodide → iodine (peroxidase oxidation)
  Thyroglobulin (TG) protein in follicle lumen iodinated at tyrosines
  MIT (monoiodotyrosine) + DIT (diiodotyrosine) coupled:
    MIT + DIT = T3 (triiodothyronine, active form, 20% direct thyroid, 80% peripheral T4 → T3)
    DIT + DIT = T4 (thyroxine, prohormone, major secreted product)

T4 → T3 conversion: deiodinase enzymes in target tissues
T3 is 3–4× more potent than T4; shorter half-life (1 day vs 7 days)
~99.9% of T3/T4 bound to TBG (thyroxine-binding globulin), albumin — only free fraction active
```

### Thyroid Hormone Effects

```
METABOLIC: ↑ BMR, ↑ O₂ consumption, ↑ thermogenesis (↑ Na/K-ATPase expression)
CARDIAC: ↑ HR, ↑ contractility (↑ β₁ receptor expression)
CNS: essential for fetal brain development (cretinism if deficient)
     Adults: ↑ alertness, anxiety in excess
GROWTH: required for normal GH action and bone maturation
CATECHOLAMINE sensitization: ↑ adrenergic receptor expression
```

| Condition | TSH | Free T4 | Common causes |
|-----------|-----|---------|---------------|
| Primary hypothyroidism | ↑↑ | ↓ | Hashimoto's (autoimmune), iodine deficiency, post-thyroidectomy |
| Secondary hypothyroidism | ↓ | ↓ | Pituitary failure |
| Primary hyperthyroidism | ↓ | ↑ | Graves' disease (TSH-R stimulating Ab), toxic adenoma |
| Subclinical hypothyroidism | ↑ | Normal | Treat if symptomatic or TSH > 10 |

---

## Adrenal Glands

```
ADRENAL GLAND (sits atop each kidney):
  CORTEX (3 layers — "GFR from outside in"):
    Zona Glomerulosa (outer) → Mineralocorticoids (aldosterone)
      Regulation: RAAS (Ang II) + K⁺ (direct), NOT ACTH primarily
      Action: Na⁺ reabsorption + K⁺ excretion (DCT/collecting duct)
    Zona Fasciculata (middle) → Glucocorticoids (cortisol)
      Regulation: ACTH (diurnal + stress-driven)
      Action: anti-inflammatory, immunosuppressive; gluconeogenesis;
              fat mobilization; protein catabolism; permissive for catecholamines
    Zona Reticularis (inner) → Sex steroids (DHEA, androstenedione)
      Regulation: ACTH
      Action: weak androgens (converted to testosterone/estrogen peripherally)

  MEDULLA (neural crest origin — modified sympathetic ganglion):
    → Epinephrine (80%) + Norepinephrine (20%)
    Stimulated by: preganglionic sympathetic (acetylcholine)
    Action: "fight-or-flight" — ↑ HR, ↑ BP, ↑ glucose (glycogenolysis), bronchodilate
```

### Key Cortisol Physiology

- Circadian rhythm: peaks ~8 AM, nadir midnight
- Stress response: CRH → ACTH → cortisol surge within 20 min
- Immunosuppression: ↓ prostaglandins, ↓ cytokines (IL-1, IL-6, TNF), ↓ leukocyte trafficking
- Metabolic effects: ↑ gluconeogenesis, ↑ protein catabolism, ↑ lipolysis, ↑ appetite
- Pathology:
  - Cushing syndrome (excess cortisol): central obesity, striae, HTN, DM, osteoporosis, moon face, buffalo hump
  - Addison disease (adrenal insufficiency): fatigue, hypotension, hyponatremia, hyperkalemia, hyperpigmentation (↑ ACTH → ↑ MSH from POMC)

---

## Pancreas: Insulin and Glucagon

```
ISLETS OF LANGERHANS (~1% of pancreas):
  β cells (65%): Insulin
  α cells (25%): Glucagon
  δ cells (10%): Somatostatin (inhibits both locally)

FED STATE (↑ blood glucose, ↑ amino acids):
  β cells → Insulin ↑
    Mechanism: glucose → GLUT2 → glycolysis → ↑ ATP/ADP → KATP channel closes
    → membrane depolarization → voltage-gated Ca²⁺ in → exocytosis
  Insulin actions:
    ↑ GLUT4 translocation to membrane (muscle, adipose) → ↑ glucose uptake
    ↑ Glycogen synthesis (liver + muscle)
    ↑ Protein synthesis
    ↑ Fat synthesis; ↓ lipolysis
    ↓ Gluconeogenesis (liver)
    ↑ K⁺ uptake by cells (important clinically: insulin drives K⁺ into cells)

FASTED STATE (↓ blood glucose):
  α cells → Glucagon ↑
    ↑ Glycogenolysis (liver)
    ↑ Gluconeogenesis
    ↑ Lipolysis → FFA + ketone body production
    ↑ Glucagon ≠ gluconeogenesis in muscle (muscle has no glucagon receptor)
```

### Diabetes Mellitus

| | Type 1 | Type 2 |
|--|--------|--------|
| Mechanism | Autoimmune β-cell destruction | Insulin resistance → β-cell exhaustion |
| Insulin | Absent | Relative deficiency |
| Ketoacidosis | Common (DKA) | Rare (HHS — hyperosmolar) |
| Age onset | Usually childhood | Usually adult (but increasing in youth) |
| Treatment | Insulin mandatory | Lifestyle → oral agents → insulin |

---

## Calcium Regulation: PTH / Calcitonin / Vitamin D

```
INTEGRATED Ca²⁺ AXIS:

Low Ca²⁺ (<8.5 mg/dL):
  Parathyroid glands (4 small glands behind thyroid)
  Chief cells sense Ca²⁺ via CaSR (calcium-sensing receptor)
  Low Ca²⁺ → CaSR less activated → PTH secreted

  PTH actions (3 organs):
    Kidney: ↑ Ca²⁺ reabsorption (DCT), ↑ phosphate excretion, ↑ 1α-hydroxylase
    Bone: osteoclast activation → Ca²⁺ + phosphate release
    Gut: indirect (via ↑ calcitriol)

  Vitamin D activation:
    Skin: UVB → 7-dehydrocholesterol → cholecalciferol (D3)
    Liver: 25-hydroxylase → 25-OH vitamin D (storage form, measured clinically)
    Kidney: PTH → 1α-hydroxylase → 1,25-(OH)₂ vitamin D (calcitriol, active)
    Action: ↑ Ca²⁺ + phosphate absorption (intestine), ↑ renal reabsorption

High Ca²⁺:
  C cells (parafollicular) of thyroid → Calcitonin
  ↓ Osteoclast activity
  ↑ Renal Ca²⁺ excretion
  Minor role in adults (main importance: fetal/neonatal, salmon physiology)
```

---

## Growth Axis: GH and IGF-1

```
GHRH (pulsatile, sleep, fasting, exercise, stress)
  ↓
GH (anterior pituitary, pulsatile)
  ├── Direct effects: lipolysis, anti-insulin, IGF-1 independent
  └── Liver: GH → IGF-1 (insulin-like growth factor 1)
        → Bone growth (epiphyseal plates), muscle protein synthesis,
          organomegaly, anti-apoptosis

SOMATOSTATIN (hypothalamus + pancreatic δ cells): inhibits GH + TSH + insulin/glucagon

GH excess (acromegaly in adults): large hands/feet/jaw, HTN, DM, carpal tunnel
GH deficiency (children): short stature, treat with recombinant GH
IGF-1 levels: best measure of GH status (GH itself is pulsatile, hard to interpret)
```

---

## Sex Hormones

```
MALE HPG AXIS:
  GnRH (pulsatile) → LH + FSH
  LH → Leydig cells → Testosterone (dihydrotestosterone via 5α-reductase in prostate/skin)
  FSH → Sertoli cells → spermatogenesis + inhibin B
  Inhibin B → inhibits FSH (−FB)
  Testosterone → inhibits GnRH + LH (−FB)

FEMALE HPG AXIS (cyclic):
  See reproductive module (09) for detailed cycle
  Estrogen (follicular, corpus luteum): Sertoli cell equivalent → endometrial growth, secondary sex chars
  Progesterone (luteal): endometrial maintenance, ↓ LH/FSH, thermogenic
  Aromatase: converts androgens → estrogens (adipose, ovary, placenta)
    ↑ Adipose → ↑ estrogen in obese women (endometrial cancer risk, PCOS)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Peptide vs steroid hormone: which acts faster? | Peptide (membrane receptor, 2nd messenger, seconds-min); steroid (nuclear, gene transcription, hours) |
| TSH high or low in primary hypothyroidism? | TSH high (pituitary not suppressed, trying to stimulate a failing thyroid) |
| What does cortisol do to the immune system? | Suppresses it — ↓ prostaglandins, ↓ cytokines, ↓ leukocyte trafficking (steroids = anti-inflammatory) |
| Aldosterone vs ADH: what each controls? | Aldosterone: Na⁺ (and therefore volume). ADH: water (and therefore osmolality) |
| Why does insulin drive K⁺ into cells? | Na/K-ATPase activation in skeletal muscle — major clinical use: give insulin in hyperkalemia |
| PTH net effect on serum phosphate? | ↓ (phosphaturic effect at kidney dominates over bone resorption release) |

---

## Common Confusion Points

**T3 vs T4: which to measure?**
Clinically measure TSH (most sensitive), then free T4. T3 is more active but harder to interpret (varies with illness — "sick euthyroid" lowers T3 without true thyroid disease).

**GH pulsatility makes direct measurement useless**
Measure IGF-1 as a surrogate (reflects integrated 24h GH secretion). Random GH levels are uninterpretable.

**Addison vs Cushing vs secondary hypo/hypercortisolism**
- Addison (primary adrenal failure): low cortisol + high ACTH → hyperpigmentation (ACTH/MSH from POMC)
- Cushing syndrome: high cortisol from any cause
- Cushing disease (specific): pituitary ACTH-secreting adenoma
- Secondary adrenal insufficiency: pituitary failure → low ACTH → low cortisol → no hyperpigmentation

**DHEA and weak androgens — clinical relevance**
Adrenal DHEA is the precursor to most androgens in postmenopausal women and a significant contributor in men. CAH (congenital adrenal hyperplasia): enzyme defects in cortisol synthesis → ACTH ↑ → adrenal androgens ↑ → virilization.
