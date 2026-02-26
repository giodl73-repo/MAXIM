# Carbohydrates

## The Big Picture

Carbohydrates are the most versatile class of biomolecules — they serve as fuel, structural material, cell signaling molecules, and gut ecosystem substrate. The simple classification (simple vs complex) obscures enormous biochemical diversity.

<!-- @editor[diagram/P2]: Diagram lists items but doesn't show how they relate — rework as layered system view connecting taxonomy -> digestion -> blood glucose regulation -> GI/GL -> fiber fermentation -> fructose metabolism -> insulin response -->
```
CARBOHYDRATE TAXONOMY

Monosaccharides (single sugar units)
├── Glucose (C₆H₁₂O₆) — universal cellular fuel
│   α and β anomers; chair conformation; GLUT transporters specific to it
├── Fructose — fruit sugar; liver-specific metabolism; lipogenic
└── Galactose — milk sugar component; converted to glucose in liver

Disaccharides (2 monosaccharides, glycosidic bond)
├── Sucrose (α-Glc + β-Fru, 1→2) — table sugar; cleaved by sucrase
├── Lactose (β-Gal + Glc, 1→4) — milk; cleaved by lactase (lactase-phlorizin hydrolase)
└── Maltose (Glc + Glc, α-1→4) — starch hydrolysis product; cleaved by maltase

Polysaccharides (many monosaccharides)
├── Starch (digestible) — plant energy store
│   ├── Amylose: linear chains, α-1,4 glycosidic bonds (~20–30% of starch)
│   └── Amylopectin: branched, α-1,4 + α-1,6 branches every 24–30 units (~70–80%)
├── Glycogen (digestible) — animal/human energy store
│   Highly branched (branch every 8–12 units); in liver + muscle
│   Liver glycogen: ~100g, blood glucose buffer
│   Muscle glycogen: ~400g, local fuel for muscle contraction
└── Dietary Fiber (not digestible by human enzymes)
    ├── Cellulose: β-1,4 linked glucose — structural; cannot be cleaved
    ├── Hemicellulose: mixed β-linked sugars — partial fermentation
    ├── Pectin: galacturonic acid polymer — gel-forming; soluble
    └── Fructooligosaccharides (FOS)/inulin — prebiotic; fermented to SCFAs
```

---

## Digestion and Absorption

```
CARBOHYDRATE DIGESTION PATHWAY:

Mouth:
  Salivary amylase (α-amylase) → hydrolyzes α-1,4 bonds in starch
  → starch fragments (dextrins, maltose) — limited time in mouth

Stomach:
  Acidic pH (1.5–3.5) → denatures amylase → digestion pauses
  No carbohydrate-specific enzymes

Small intestine (primary site):
  Pancreatic amylase → completes starch → maltose + limit dextrins
  Brush border enzymes:
    Maltase → glucose + glucose
    Sucrase → glucose + fructose
    Lactase → glucose + galactose
    Isomaltase → cleaves α-1,6 branches

Absorption:
  Glucose: Na⁺-dependent cotransport (SGLT1) — active transport into enterocyte
           then GLUT2 (facilitated) on basolateral side → portal vein
  Fructose: GLUT5 (facilitated diffusion) on apical; GLUT2 basolateral
            much slower; partially converted to glucose in enterocytes
  Galactose: SGLT1 (same as glucose) → portal vein → liver → converted to glucose

Portal vein → liver:
  Glucose: GLUT2 (high Km, high capacity) → phosphorylated by glucokinase
           → glycolysis / glycogenesis / gluconeogenesis depending on metabolic state
  Fructose: enters liver, phosphorylated by fructokinase (not regulated by insulin)
           → bypasses key glycolytic control point → more lipogenic than glucose
```

---

## Blood Glucose Regulation

```
POSTPRANDIAL GLUCOSE (after eating):

  Carbohydrate absorbed → blood glucose rises → pancreatic β-cells sense glucose
                                                ↓
                                          Insulin secreted
                          ┌──────────────────────────────────┐
                          │ Insulin effects:                  │
                          │ • GLUT4 translocation to muscle   │
                          │   and adipose (insulin-dependent) │
                          │ • Glycogen synthesis ↑            │
                          │ • Glycolysis ↑                    │
                          │ • Gluconeogenesis ↓               │
                          │ • Lipolysis ↓ (anti-lipolytic)   │
                          └──────────────────────────────────┘
                          Blood glucose returns to ~4.5–5.5 mmol/L

FASTING GLUCOSE MAINTENANCE:

  Liver glycogen breakdown (glycogenolysis) → glucose to blood
  Liver gluconeogenesis (lactate, alanine, glycerol → glucose)
  Blood glucose maintained at ~3.5–4.5 mmol/L fasting
  Brain consumes ~120g glucose/day (~60% of RBC + brain total)

HYPERGLYCEMIA CONSEQUENCES:
  Acute: >11 mmol/L → glucosuria (glucose spills into urine)
  Chronic: non-enzymatic glycation of proteins (HbA1c measure of this)
           AGE (advanced glycation end-products) → vascular damage,
           nephropathy, retinopathy, neuropathy

HYPOGLYCEMIA (<3.5 mmol/L):
  Symptoms: shakiness, sweating, confusion, seizure
  Emergency: glucagon (from α-cells) → hepatic glycogenolysis → raises BG
```

---

## Glycemic Index and Glycemic Load

### Glycemic Index (GI)

```
GI = (Area Under Curve of test food) / (Area Under Curve of reference food) × 100

Reference food: pure glucose (GI=100) or white bread (GI=100)

GI categories:
  Low GI (< 55): lentils (30), kidney beans (28), whole grain oats (55)
  Medium GI (55–70): brown rice (64), sucrose (65), orange juice (57)
  High GI (> 70): white bread (75), white rice (73), baked potato (85)

What GI measures: how fast blood glucose rises after a STANDARD 50g carbohydrate load

GI limitations:
  • Measured in isolation — meals have mixed macronutrient composition
  • Fat and protein slow gastric emptying → lower GI of any food in context
  • Portion size not captured (50g carbohydrate from watermelon requires a huge serving)
  • Individual variation is enormous (CGM studies show 2-fold variation in response)
```

### Glycemic Load (GL)

```
GL = GI × (grams of carbohydrate per serving) / 100

Example: Watermelon
  GI = 76 (high)
  But: 1 cup watermelon has only ~11g carbohydrate (mostly water)
  GL = 76 × 11 / 100 = 8.4  (low!) — not metabolically concerning per serving

Example: Baked potato (medium, 150g):
  GI = 85
  Carbohydrate per serving: ~30g
  GL = 85 × 30 / 100 = 25.5  (high — metabolically significant)

GL categories:
  Low: <10 per meal   Medium: 10–20   High: >20

GL is more practically useful than GI alone
```

---

## Dietary Fiber — The Fermentation Economy

Fiber is not nutritionally inert — it is a **substrate for the gut microbiome**.

```
FIBER FERMENTATION IN COLON:

  Undigested fiber arrives in cecum/colon
       ↓
  Gut bacteria (Bifidobacteria, Lactobacillus, Ruminococcus, Bacteroides)
  ferment fiber → SHORT-CHAIN FATTY ACIDS (SCFAs)
       ↓
  PRIMARY SCFAs:
    Butyrate (C4):  ~15–20% of SCFAs
      → Primary fuel for colonocytes (colon cells prefer butyrate over glucose)
      → Anti-inflammatory; histone deacetylase inhibitor
      → Reduced production linked to colorectal cancer risk
    Propionate (C3): ~25%
      → Absorbed → liver → gluconeogenesis substrate; satiety signaling
      → Reduces hepatic lipogenesis
    Acetate (C2): ~60%
      → Peripheral tissues, including muscle
      → Acetyl-CoA substrate; cardiac fuel

  OTHER FERMENTATION OUTCOMES:
    Gas: CO₂, H₂, CH₄ (methane in some individuals)
    Minor: branched-chain fatty acids (from protein fermentation)
    pH: SCFA lower colonic pH → inhibit pathogen growth

  SCFA ABSORPTION:
    Colonocytes absorb SCFAs apically; butyrate oxidized locally (~10% energy)
    Propionate + acetate → portal vein → liver
```

### Fiber Types and Clinical Effects

| Fiber type | Solubility | Fermentability | Key effects |
|-----------|-----------|---------------|-------------|
| Cellulose | Insoluble | Low | Stool bulk; transit time; colon health |
| Pectin | Soluble | High | Cholesterol lowering (bile acid sequestration); glucose buffering |
| β-glucan | Soluble | High | LDL reduction (FDA heart claim); glycemic dampening |
| Inulin/FOS | Soluble | High (prebiotic) | Bifidobacteria proliferation; SCFA; gas |
| Psyllium | Soluble (gel) | Moderate | Cholesterol; glycemia; constipation |
| Resistant starch | Semi-soluble | High | Butyrate production; insulin sensitivity |

Resistant starch types:
- RS1: physically inaccessible (intact cell walls — unprocessed grains)
- RS2: raw starch granules (green banana, raw potato)
- RS3: retrograde starch (cooled cooked potato, rice — increases with cooling)
- RS4: chemically modified starches

Practical: cooked-and-cooled rice/potato has significantly more RS3 than freshly cooked.

---

## Fructose: The Liver Bypass Problem

Fructose and glucose have the same molecular formula but dramatically different metabolic fates.

```
GLUCOSE:
  Absorbed → portal vein → liver
  Glucokinase: glucose → G6P (regulated: inhibited by G6P)
  G6P → glycogen (if glycogen depleted)
     → glycolysis → ATP
     → glucose to circulation (brain, muscle)
  Insulin required for muscle/adipose uptake (GLUT4 translocation)

FRUCTOSE:
  Absorbed → portal vein → liver (nearly all first-pass)
  Fructokinase: fructose → F1P (NOT regulated — high flux regardless of metabolic state)
  F1P → DHAP + glyceraldehyde → enters glycolysis BELOW the rate-limiting PFK step

  Consequences:
    → Bypasses phosphofructokinase (PFK) rate-limiting step — no throttle
    → High flux → acetyl-CoA → de novo lipogenesis → VLDL → ↑ triglycerides
    → Uric acid production (fructokinase consumes ATP → AMP → uric acid)
    → Does NOT stimulate insulin or leptin proportionally (poor satiety signal)
    → High chronic fructose → visceral fat, hepatic steatosis (NAFLD/MASLD)
```

High-fructose corn syrup (HFCS) vs sucrose:
- HFCS-55 (55% fructose, 45% glucose): not dramatically different from sucrose (50/50) in biochemistry
- The issue is total fructose consumption, not HFCS specifically
- Sugar-sweetened beverages = most concentrated source; liquid calories don't suppress solid food intake

---

## Insulin Response in Context

```
INSULIN RESPONSE IS NOT INHERENTLY PATHOLOGICAL

Insulin index (II) measures insulin response (not glucose response):
  Protein: insulin-stimulating despite not raising glucose
           (leucine is potent insulin secretagogue)
  Fat: minimal insulin response
  Carbohydrate: moderate-to-high

Common misconception: carbs → insulin spike → fat storage → obesity
Reality:
  1. Insulin promotes both glucose oxidation AND storage — context dependent
  2. Healthy individuals: insulin rises, glucose cleared, insulin returns to baseline
  3. Pathology = chronically elevated FASTING insulin = insulin resistance
     → caused by: excess total calories + sedentary lifestyle + visceral fat
     → high carb intake in energy surplus → promotes IR
     → same carb intake in energy balance + active → no problem

Insulin resistance (IR):
  Peripheral tissues (muscle, adipose) less responsive to insulin
  → pancreas compensates by secreting more insulin
  → eventually β-cell exhaustion → Type 2 diabetes
  → independent risk factor for CVD, certain cancers

Low-carb diets and insulin:
  Reduce postprandial glucose and insulin excursions
  Effective for blood glucose control in T2DM
  Not the only mechanism — caloric restriction and weight loss work too
```

---

## Decision Cheat Sheet

| Goal | Carbohydrate strategy |
|------|----------------------|
| Stable blood glucose | Low GI foods; combine with fat, fiber, protein |
| Sustained exercise fuel | High-glycogen stores (moderate-high CHO) |
| Rapid energy for sprint/HIIT | High GI carbs during/immediately after |
| Gut microbiome support | Diverse fiber (pectin, inulin, β-glucan, RS3) |
| LDL cholesterol reduction | β-glucan (oats, barley) — FDA heart-health claim |
| Reduce visceral fat / MASLD | Reduce fructose-containing beverages; total caloric restriction |
| T2DM blood glucose control | Low-carbohydrate diet reduces HbA1c in trials |
| Ketosis | < 30–50g total CHO/day → hepatic ketogenesis |

---

## Common Confusion Points

**"Complex carbohydrate" ≠ slow digestion**
White flour is a complex carbohydrate (polysaccharide) with a high GI (70+) because the fine particle size and processing make it rapidly digestible. Legumes are "complex" and have low GI because of their fiber matrix and cell wall structure. Particle size and physical form matter more than the simple/complex chemical distinction.

**Sucrose and HFCS are not biochemically equivalent in all contexts**
Sucrose is cleaved by sucrase into free fructose + glucose in the GI tract — essentially identical to HFCS-50. HFCS-55 (soft drinks) has slightly more free fructose. The practical difference in moderate consumption is small; the dose is what matters.

**Fiber recommendations are minimum targets, not ideal intake**
Recommended intake: 25g (women), 38g (men) per day. Average US intake: ~15g/day. Hunter-gatherer estimates: 70–100g/day. The gut microbiome may be chronically substrate-deprived at modern Western fiber intakes.

**Glycogen depletion is not the same as hitting the "wall"**
"Bonking" (hitting the wall) in endurance sports happens when liver glycogen falls, blood glucose drops, and fat oxidation can't sustain high exercise intensity. Muscle glycogen is a local fuel — depleting muscle glycogen in one muscle doesn't help other muscles. Glycogen loading before a marathon makes sense; glycogen loading before a 5K does not.

**Insulin doesn't directly cause weight gain**
Insulin inhibits lipolysis (fat breakdown) and promotes fat storage when calories are in surplus. But if you're in caloric deficit, high insulin doesn't cause fat accumulation — there's no substrate to store. The carbohydrate-insulin model of obesity (fat storage → hunger → overeat) remains scientifically debated; caloric balance is the primary driver.
