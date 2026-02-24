# Metabolism and Energy

## The Big Picture

Metabolism is **the sum of all biochemical reactions that maintain life** — specifically, the conversion of food energy (chemical bonds) into ATP, heat, and structural building blocks. Energy expenditure is the body's energy demand side: the rate at which ATP is consumed in all processes. The ratio of these two determines body weight trajectory over time.

```
ENERGY BALANCE — FRAMEWORK:

  ENERGY IN                    ENERGY OUT
  ─────────────────────────────────────────────────────────────
  Food: carbohydrates           BMR (Basal Metabolic Rate)   ~60–70%
  Food: fats                    TEF (Thermic Effect of Food) ~10%
  Food: proteins                NEAT (Non-Exercise Activity) ~15–30%
  Food: alcohol                 EAT (Exercise Activity)      0–30%

  Net: Energy In − Energy Out = ΔFat stores (+ other tissues)

  LAWS:
    Energy balance follows thermodynamics (1st law): calories in = calories out + storage
    Body weight is not simply "calories in − calories out" because:
      Metabolic adaptation: BMR changes with caloric deficit
      TEF varies by macronutrient composition
      NEAT adapts to caloric intake
      → "Eat less, move more" is correct but incomplete

METABOLIC FUEL SOURCES (SUBSTRATES):
  Fed state (post-meal):        glucose + amino acids + chylomicrons
  Post-absorptive (~4–8h fast): glycogenolysis + lipolysis starts
  Overnight fast:               gluconeogenesis + fatty acid oxidation
  Prolonged fast (>24h):        ketogenesis + protein sparing
  Exercise (low intensity):     fat oxidation dominant (~70% at 65% VO₂max)
  Exercise (high intensity):    glucose oxidation dominant (anaerobic glycolysis)
```

---

## Basal Metabolic Rate (BMR) and TDEE

### BMR — Basal Metabolic Rate

```
BMR DEFINITION:
  Energy expended at complete rest, post-absorptive (12h fast), thermoneutral
  environment, no stress/illness — the minimum energy to sustain life

  Comprises:
    Organ maintenance (~80% of BMR):
      Brain:   ~20% of BMR (1.4 kg tissue; 250 mL/min O₂)
      Liver:   ~21% (major metabolic hub)
      Kidneys: ~8%
      Heart:   ~9%
      Muscle:  ~22% of BMR (but ~40% of body weight — low rate/kg vs viscera)

    Ion pump maintenance: Na⁺/K⁺-ATPase ~40% of total BMR
    Protein synthesis and turnover: ~20% of BMR
    Substrate cycling (futile cycles): ~5%

MIFFLIN-ST JEOR EQUATION (most validated for weight-normal adults):

  Men:    BMR = 10×weight(kg) + 6.25×height(cm) − 5×age(yr) + 5
  Women:  BMR = 10×weight(kg) + 6.25×height(cm) − 5×age(yr) − 161

  Example (75kg, 175cm, 40yr male):
  BMR = 10×75 + 6.25×175 − 5×40 + 5
      = 750 + 1093.75 − 200 + 5 = 1648.75 kcal/day

VERSUS HARRIS-BENEDICT (1919, revised 1984):
  Slightly less accurate than Mifflin for non-obese adults
  Still widely used in clinical settings
  Overestimates BMR by ~5% in obese individuals

VERSUS KATCH-MCARDLE:
  Uses lean body mass (LBM) instead of total body weight
  More accurate when body composition known
  BMR = 370 + 21.6 × LBM(kg)
  → Does not require age/height/sex corrections

RMR vs BMR:
  RMR (Resting Metabolic Rate): measured in non-fasted, non-strictly-controlled conditions
  ≈ 10–20% higher than true BMR
  Most clinical measurements are RMR; called BMR colloquially
```

### TDEE — Total Daily Energy Expenditure

```
TDEE COMPONENTS:

  TDEE = BMR × PAL (Physical Activity Level)

  PAL (Activity Factor):
    Sedentary (desk job, little exercise):         1.2
    Lightly active (light exercise 1–3d/wk):       1.375
    Moderately active (moderate exercise 3–5d/wk): 1.55
    Very active (hard exercise 6–7d/wk):           1.725
    Extra active (hard exercise + physical job):   1.9

  TDEE COMPONENTS MORE PRECISELY:
    BMR:  Basal metabolic rate (~60–70% of TDEE in sedentary)
    TEF:  Thermic effect of food (~10% of calories consumed)
    NEAT: Non-exercise activity thermogenesis (~15–50% variable)
    EAT:  Exercise activity thermogenesis (~0–30% depending on training)

TEF — Thermic Effect of Food:
  Protein:       20–30% of calories consumed (digestion + protein synthesis)
  Carbohydrates: 5–10% of calories
  Fat:           0–3% of calories (minimal processing cost)
  Alcohol:       ~20%

  → 100 kcal protein → 70–80 kcal net to body
  → 100 kcal fat → 97–100 kcal net to body
  → High-protein diet: metabolic advantage ~200–300 kcal/day vs equicaloric low-protein

NEAT — The Wild Card:
  All movement that isn't formal exercise:
    Fidgeting, walking to bathroom, posture changes, spontaneous activity
  Range: 200–1000 kcal/day between individuals of same body composition!
  NEAT adapts: overfeeding → NEAT increases (up to +500 kcal/day in some)
  Caloric restriction → NEAT decreases (compensation; reduces deficit achieved)
  → Most of the "I don't lose weight when I diet" = NEAT suppression

METABOLIC ADAPTATION (Adaptive Thermogenesis):
  Extended caloric restriction → BMR decreases beyond predicted by weight loss
  Component 1: reduced body mass → less tissue to maintain (expected)
  Component 2: additional 100–300 kcal/day suppression beyond mass prediction
  → Thyroid hormones drop (T3 especially); sympathetic tone decreases
  → "The Biggest Loser study" (Rosenbaum 2016): 6yr follow-up
    Contestants: BMR still 500 kcal/day BELOW predicted for their weight
    → Persistent metabolic adaptation; not transient
  → Implication: weight loss is harder to maintain than to achieve
```

---

## Respiratory Quotient (RQ)

```
RQ DEFINITION:
  RQ = CO₂ produced / O₂ consumed (molar ratio, measured by indirect calorimetry)
  Reflects which substrate is being oxidized

SUBSTRATE RQ VALUES:
  Pure carbohydrate oxidation:  RQ = 1.0
    Glucose: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O
    CO₂/O₂ = 6/6 = 1.0

  Pure fat oxidation:           RQ = 0.7
    Palmitate: C₁₆H₃₂O₂ + 23O₂ → 16CO₂ + 16H₂O
    CO₂/O₂ = 16/23 = 0.695

  Pure protein oxidation:       RQ = 0.82
    Average amino acid mixture → variable; ≈ 0.82

  Mixed diet (typical):         RQ = 0.80–0.85

  Lipogenesis (fat synthesis):  RQ > 1.0 (carbs converted to fat → CO₂ > O₂)
    Heavy carb overfeeding: RQ can reach 1.1–1.3

  Ketosis:                      RQ ~0.65–0.70 (almost pure fat oxidation)

FOOD QUOTIENT (FQ):
  RQ of the diet composition consumed
  Not same as measured RQ (body uses stores, not just food eaten)
  If FQ = RQ: fat balance (neither gaining nor losing fat stores)
  If RQ > FQ: net fat storage (more carbs burned than consumed)
  If RQ < FQ: net fat oxidation (fat being mobilized from stores)

INDIRECT CALORIMETRY:
  Measurement: metabolic cart with ventilated canopy or mouthpiece
  Measures: O₂ consumption, CO₂ production per minute
  Calculates: substrate oxidation rates + actual measured REE
  Clinical use: ICU patients, eating disorders, sports nutrition
  Provides: measured vs. predicted BMR (significant discrepancies common)
```

---

## Fed and Fasted States

```
METABOLIC STATE TRANSITIONS:

  Meal ─► FED STATE ─────────────────── (2–4h post-meal)
  │         Insulin dominant
  │         Glucose: 5–8 mmol/L blood
  │         Liver: glycogen synthesis + lipogenesis
  │         Muscle: glucose uptake + protein synthesis
  │         Adipose: triglyceride synthesis; lipolysis OFF
  │
  └──────► POST-ABSORPTIVE ──────────── (4–8h, "between meals")
  │         Insulin falling; glucagon rising
  │         Glycogenolysis (liver glycogen → glucose → blood)
  │         Blood glucose maintained ~4.5–5 mmol/L
  │         Lipolysis beginning; FFA rising
  │
  └──────► EARLY FASTING ─────────────── (8–16h, "overnight fast")
  │         Glucagon/cortisol/adrenaline dominant
  │         Glycogen depleting (~400–500 kcal glycogen stores)
  │         Gluconeogenesis activating (amino acids, glycerol → glucose)
  │         Lipolysis active; FFA and glycerol released from adipose
  │         Ketones beginning
  │
  └──────► PROLONGED FASTING ──────────── (16h–days)
            Liver glycogen depleted
            Gluconeogenesis supplying glucose (brain + RBCs still need it)
            Ketogenesis active → BHB/AcAc supply alternative fuel to brain
            Protein sparing increases as brain adapts to ketones
            Fat oxidation dominant (~70–80% of energy)

INSULIN: THE MASTER SWITCH:
  Fed: insulin high → GLUT4 translocates → muscle/fat uptake glucose
       Glucokinase active in liver → glycogen synthesis
       mTOR activated → protein synthesis
       HSL inhibited → no lipolysis
  Fasted: insulin low → HSL active → lipolysis → FFA + glycerol released
          GLUT4 internalized → muscle uses FFA + ketones preferentially
          Glycogen phosphorylase → glycogenolysis

GLUCONEOGENESIS SUBSTRATES:
  Amino acids (Ala, Gln dominant) → PEP → glucose  [muscle catabolism source]
  Glycerol (from lipolysis of triglycerides) → DHAP → glucose
  Lactate (Cori cycle) → pyruvate → OAA → glucose [recycling]
  Occurs primarily in: liver (90%) and kidney (10%)
  Rate limiting enzyme: PEPCK (induced by glucagon/cortisol; inhibited by insulin)
```

---

## Metabolic Flexibility

```
METABOLIC FLEXIBILITY DEFINITION:
  The capacity of cells to switch between glucose and fat oxidation
  depending on substrate availability and energy demands

  High metabolic flexibility:
    Fed state → glucose oxidation; RQ rises toward 1.0
    Fasted state → fat oxidation; RQ falls toward 0.7
    Exercise (low intensity) → fat oxidation; rapidly switches
    Exercise (high intensity) → glucose oxidation; rapidly switches

  Low metabolic flexibility (metabolic inflexibility):
    Characteristic of obesity, insulin resistance, Type 2 diabetes
    → Impaired suppression of fat oxidation in fed state
    → Impaired switch to fat oxidation in fasted state
    → Both states: incomplete substrate oxidation; intermediary accumulation

CELLULAR MECHANISM — RANDLE CYCLE:
  Original Randle hypothesis (1963): glucose-fatty acid cycle
  FFA → mitochondrial β-oxidation → elevated acetyl-CoA/CoA ratio
  → Inhibits pyruvate dehydrogenase (PDH) → blocks glucose → pyruvate → AcCoA
  → Elevated citrate → inhibits PFK → blocks glycolysis
  → Glucose uptake and oxidation suppressed when fat available
  Modern refinement: metabolic inflexibility involves ceramides, DAG,
    ROS from incomplete β-oxidation, mitochondrial dysfunction

EXERCISE AND SUBSTRATE CROSSOVER:
  At low exercise intensity (~40–50% VO₂max): fat dominates (~70% energy)
  At crossover point (~65% VO₂max): 50/50 fat/glucose
  At high intensity (>80% VO₂max): glucose/glycogen dominant
  → High-intensity exercise → anaerobic glycolysis → lactate → fatigue
  → Training effect: shifts crossover point upward → fat oxidation at higher intensity

FAT ADAPTATION / LOW CARB TRAINING:
  Prolonged low-carb diet → upregulates fat oxidation enzymes (CPT1, β-oxidation)
  → Better fat utilization at moderate intensity
  → BUT: impairs ability to oxidize glucose at high intensity
  → "The elephant in the room": race pace requires glycolytic flux
  → Sports science: periodized approach (high carb for race; low carb for base)
```

---

## Ketosis and Ketogenesis

```
KETOSIS THRESHOLD:
  Normal fasting: ketones ~0.1–0.5 mmol/L (trace)
  Nutritional ketosis: 0.5–3.0 mmol/L (dietary keto or prolonged fast)
  Starvation ketosis: 3–5 mmol/L (extended fast)
  DKA (diabetic ketoacidosis): >10–25 mmol/L + low insulin + hyperglycemia

  Key trigger: hepatic glycogen depletion → insulin drop → fatty acid mobilization

HEPATIC KETOGENESIS PATHWAY:

  Adipose lipolysis → FFA → liver
  FFA → β-oxidation → Acetyl-CoA (×2 from each FA)

  When acetyl-CoA overwhelms TCA cycle capacity:
  2 × Acetyl-CoA → Acetoacetyl-CoA (acetoacetyl-CoA thiolase)
                   + 1 × Acetyl-CoA → HMG-CoA (HMG-CoA synthase)
                   HMG-CoA → Acetoacetate (AcAc) + Acetyl-CoA (HMG-CoA lyase)

  Acetoacetate → β-hydroxybutyrate (BHB) [NADH-dependent; reversible]
               → Acetone [spontaneous; exhaled; fruity breath]

  Transport: BHB + AcAc exported to bloodstream → peripheral tissues

KETONE UTILIZATION:
  Brain: takes up BHB; converts to AcAc → succinyl-CoA → TCA cycle
  Heart: prefers BHB over glucose (higher ATP per O₂ than glucose)
  Muscle: uses BHB at rest; switches back to glucose during exercise
  Kidney: can use ketones; can also synthesize glucose

WHY KETOSIS IS "PROTEIN SPARING":
  Brain requires ~120g glucose/day normally
  → In extended fast, brain adapts to ketones → glucose demand drops to ~40g/day
  → Less gluconeogenesis from amino acids needed → less muscle catabolism
  → Starvation: without ketosis, brain demands would require ~100g protein/day catabolism
  → With ketosis: ~20–30g protein/day loss (still some, but much less)

KETOGENIC DIET (nutritional ketosis):
  Typically: <20–50g carbohydrate/day; moderate protein; high fat
  Carb restriction → depletes liver glycogen → insulin drops → ketogenesis activates
  Onset: 2–4 days of strict restriction
  "Keto flu" (days 3–7): electrolyte loss, fatigue → resolves with Na/K/Mg
  Long-term adaptation: 3–6 weeks → full fat-oxidative enzyme upregulation

  CLINICAL USES:
    Epilepsy (pediatric drug-resistant): ~40–50% reduction in seizures (strong evidence)
    Type 2 diabetes: significant BG reduction; often medication reduction
    Weight loss: effective at 6–12 months; comparative at 24 months vs other diets
    Alzheimer's (theoretical): glucose utilization impaired; ketones alternative fuel
    Cancer (adjunct): some tumors glucose-dependent (Warburg effect); unproven clinical benefit

  RISKS:
    Kidney stones (oxalate + urate) — especially pediatric epilepsy protocols
    Hyperlipidemia: LDL-C rises in subset (heterozygous FH risk)
    Nutrient deficiency if vegetables restricted
    Saturated fat increase → ApoB increase in hyperresponders
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Most accurate BMR formula | Mifflin-St Jeor (for typical adults); Katch-McArdle if LBM known |
| Why caloric restriction slows metabolism | Adaptive thermogenesis: NEAT + hormonal suppression (T3, leptin) |
| RQ 0.7 means what? | Nearly pure fat oxidation |
| RQ 1.0 means what? | Nearly pure carbohydrate oxidation |
| When does gluconeogenesis begin? | ~8–16h fast; rates increase as glycogen depletes |
| When is ketosis nutritional vs dangerous? | <3 mmol/L + normal insulin = nutritional; >10 + DM + no insulin = DKA |
| Why does keto help epilepsy? | Not fully known; BHB has direct neuromodulatory effects; glucose/mTOR suppression |
| Exercise at low intensity burns what? | Fat dominant until ~65% VO₂max crossover |
| What is NEAT? | All non-exercise movement; highly variable; adapts to caloric intake |

---

## Common Confusion Points

**Caloric deficit causes weight loss; adaptive thermogenesis fights it**
The law of thermodynamics is correct: eat less than you burn and you lose weight. The complication is that "how much you burn" is not fixed — BMR decreases, NEAT decreases, and TEF changes. The deficit you create is smaller than the diet change you made. This is why maintenance after weight loss requires permanent diet adjustment, not just "eat normal again."

**Ketosis ≠ ketoacidosis**
Nutritional ketosis (0.5–3 mmol/L) is a normal metabolic state with intact insulin signaling that limits ketone production. Diabetic ketoacidosis requires the combination of severe insulin deficiency + hyperglycemia → unchecked hepatic ketogenesis. A healthy person in nutritional ketosis cannot develop DKA — insulin suppresses the runaway ketogenesis pathway.

**Fat burning ≠ fat loss**
During a ketogenic diet you oxidize more fat at rest. But "burning fat" means oxidizing dietary fat or stored fat. If fat intake is high (as on keto), the fat oxidized is primarily dietary. Net fat loss from stores requires total caloric deficit. High fat oxidation rate at rest does not guarantee body fat reduction.

**BMR is not what a sedentary person burns daily**
BMR is the energy cost of lying still awake in a thermoneutral room after a 12-hour fast. Sedentary daily expenditure is ~1.2× BMR. The most important variable is NEAT — the difference between 1.2× and 1.5× BMR is almost entirely NEAT variation. People who fidget and stand lose significantly more weight on identical diets than people who sit still.

**High-intensity exercise uses glucose, not fat**
"Fat-burning zone" advice (low-intensity exercise) is based on relative substrate percentages but misses absolute amounts. At 80% VO₂max, you burn fewer fat grams per minute than at 60% VO₂max, but you burn far more total calories — and post-exercise EPOC (excess post-exercise oxygen consumption) increases fat oxidation for hours after. Total energy expenditure, not substrate percentage, drives fat loss.
