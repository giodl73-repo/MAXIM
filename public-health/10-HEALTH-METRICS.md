# Health Metrics

## The Measurement Problem in Population Health

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HEALTH MEASUREMENT LANDSCAPE                              │
│                                                                               │
│  WHAT TO MEASURE:                                                             │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │  Mortality-based       Morbidity-based      Composite                  │  │
│  │  ────────────────       ───────────────      ─────────                 │  │
│  │  Crude death rate       Incidence rate        DALY                     │  │
│  │  Age-specific MR        Prevalence            QALY                     │  │
│  │  Cause-specific MR      Disability rate       HALE                     │  │
│  │  Life expectancy        DALYs (YLD component) HALYs (general)          │  │
│  │  YLL                    Quality-of-life scores                          │  │
│  │  Infant mortality rate  Activity limitations                            │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
│                                                                               │
│  FUNDAMENTAL PROBLEM: Mortality tells you nothing about conditions           │
│  people live with. 2B people have chronic pain, vision loss, depression —   │
│  none counted in mortality statistics.                                        │
│                                                                               │
│  SOLUTION: composite metrics (DALY/QALY) capture both mortality              │
│  and morbidity in a single comparable unit.                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Mortality Rate Calculations

```
CRUDE DEATH RATE (CDR):
  CDR = (Total deaths / Midyear population) × 1000
  Units: deaths per 1,000 population per year
  Problem: confounded by age structure (elderly populations have higher CDR
  independent of health conditions)

AGE-SPECIFIC DEATH RATE (ASDR):
  ASDR_i = (Deaths in age group i / Population in age group i) × 1000
  Age groups: typically 0, 1-4, 5-9, ..., 80-84, 85+

STANDARDIZED MORTALITY RATE:
  Controls for age structure differences between populations.
  Allows valid comparisons across countries/time periods.

  DIRECT STANDARDIZATION:
    Apply age-specific death rates of each study population
    to the age distribution of a standard population.
    SMR_direct = Σ (ASDR_i × W_i)
    where W_i = proportion of standard population in age group i

  INDIRECT STANDARDIZATION:
    Apply age-specific death rates of a reference population
    to the age structure of the study population.
    Expected deaths = Σ (ASDR_ref_i × N_i)
    SMR = Observed deaths / Expected deaths
    SMR > 1: higher mortality than reference
    SMR < 1: lower mortality than reference

  Indirect standardization used when study population is small
  (ASDR_i estimates unstable). Direct when age-specific data available.

INFANT MORTALITY RATE (IMR):
  IMR = (Deaths <1 year / Live births) × 1000
  One of the most sensitive indicators of population health and development.
  Strong correlation with: income, sanitation, healthcare access, nutrition
  US 2022: ~5.6 per 1,000 live births (high by peer country standards: UK 3.6)

NEONATAL MORTALITY RATE (NMR):
  Deaths in first 28 days of life per 1,000 live births
  ~47% of all under-5 deaths occur in neonatal period

UNDER-5 MORTALITY RATE (U5MR):
  Deaths before age 5 per 1,000 live births
  SDG target: ≤25 per 1,000 by 2030
  Global progress: 93 in 1990 → 37 in 2021 (huge achievement)
  Sub-Saharan Africa: ~71 in 2021 (highest region)
```

## Life Expectancy and Life Tables

```
PERIOD LIFE TABLE:
  Hypothetical cohort constructed from current age-specific mortality rates.
  Answers: "If current death rates persist, how long would a newborn live?"

  Life table columns:
  x:      Age (years)
  lx:     Number surviving to age x (cohort starts at l0 = 100,000)
  dx:     Deaths in interval [x, x+1] = lx − l(x+1)
  qx:     Probability of death in interval [x, x+1] = dx/lx
  px:     Probability of surviving interval = 1 − qx
  Lx:     Person-years lived in interval [x, x+1]
          = (lx + l(x+1))/2 for non-infant intervals
  Tx:     Total person-years lived beyond age x = Σ Lj for j ≥ x
  ex:     Life expectancy at age x = Tx / lx
          e0 = life expectancy at birth

  COHORT LIFE TABLE: follows actual birth cohort over time.
  Used for historical analysis; not available for current populations.

LIFE EXPECTANCY AT BIRTH (e0):
  Approximate values (2023):
  Japan: 84.3 (global leader)
  South Korea: 83.6
  Switzerland: 83.5
  Australia: 83.2
  France: 82.1
  United Kingdom: 80.7
  United States: 78.8 (below peer-country average; drug overdoses, CVD)
  Brazil: 73.4
  India: 70.2
  Nigeria: 54.7
  Chad: 54.0 (near-global minimum)

DECOMPOSITION OF LIFE EXPECTANCY DIFFERENCES:
  Arriaga decomposition: attribute ΔLE to contributions from each age group.
  Example: US-Japan ΔLE ≈ 5 years → which age groups drive the gap?
  Answer: age 50-74 cardiovascular disease + drug overdose + obesity
  (not neonatal/infant mortality, where US-Japan gap is smaller)
```

## DALY — Disability-Adjusted Life Year

```
DALY DEFINITION:
  One DALY = one year of healthy life lost to disease.
  DALYs = YLL + YLD

  DALY was designed to:
  1. Combine mortality and morbidity in one metric
  2. Enable cross-condition comparison
  3. Enable cost-effectiveness comparison ($/DALY averted)
  4. Be based on observable, measurable parameters

YEARS OF LIFE LOST (YLL):
  YLL_d = N_d × L_d
  N_d = number of deaths from cause d in the population
  L_d = expected years of life lost per death at that age

  Standard life expectancy (GBD 2010+): 88.9 years for all ages, both sexes.
  (Previously: sex-specific; changed for equity reasons — women's longer life
  expectancy was built into the metric, causing female deaths to generate less YLL)

  Example: 100 deaths from traffic accidents at average age 28
  L = 88.9 − 28 = 60.9 years per death
  YLL = 100 × 60.9 = 6,090

YEARS LIVED WITH DISABILITY (YLD):
  YLD = P × DW × L
  P = number of prevalent cases
  DW = disability weight (0 to 1 scale)
  L = average duration of the condition (or 1 year for period estimates)

  DISABILITY WEIGHTS:
  Determined from population surveys (multi-country, 2010 GBD revision).
  Method: paired comparison surveys (N>50,000 respondents globally)
    "Person A has [condition description]. Person B has [condition description].
     Which person is healthier?" → probabilistic ranking → utility scale.

  Selected DW values (GBD 2019):
    Mild hearing loss (<35 dB):          0.010
    Mild depression:                     0.145
    Moderate depression:                 0.396
    Moderate hearing loss (35-49 dB):    0.031
    Severe hearing loss (50-64 dB):      0.158
    Blindness:                           0.187
    Moderate dementia:                   0.377
    Severe stroke (long-term):           0.552
    Active AIDS (without ART):           0.582
    Paraplegia:                          0.573
    Terminal cancer (last 3 months):     0.540

  MATHEMATICAL STRUCTURE:
  DW is a von Neumann-Morgenstern utility function over health states.
  The expected disutility calculation is additive over independent conditions.
  Multiple co-occurring conditions: combined DW = 1 − Π(1 − DW_i)
  (ensures combined DW < 1 and < death; conditions are multiplicatively combined)

DALY CALCULATION EXAMPLE:
  Major depressive disorder, 30-year-old female, 1-year episode:
  DW = 0.396 (moderate depression)
  Duration L = 1 year (acute episode model)
  YLD = 1 × 0.396 × 1 = 0.396 DALYs per incident case

  If 100,000 incident cases: YLD = 39,600 DALYs
  YLL = 0 (depression rarely fatal in this model; suicide accounted separately)
  Total DALYs = 39,600
```

## QALY — Quality-Adjusted Life Year

```
QALY DEFINITION:
  One QALY = one year of life lived in perfect health.
  QALYs = Σ [time in state i × utility of state i]

  QALY vs. DALY:
  QALY: measures GAINS from intervention (more = better)
  DALY: measures BURDEN of disease (less = better)
  Both express health as utility × time but in opposite directions.

HEALTH UTILITIES (QALY WEIGHTS):
  0 = death (or health equivalent to death)
  1 = perfect health
  Some states scored < 0: worse than death (e.g., severe dementia,
    extreme pain, complete dependency)

METHODS TO DERIVE UTILITIES:
  Standard Gamble (SG):
    "What probability p of perfect health vs. certain death would make you
    indifferent between that gamble and your current health state?"
    Answer = utility (theoretically grounded in von Neumann-Morgenstern expected utility)

  Time Trade-Off (TTO):
    "How many years of perfect health are equivalent to T years in your
    current health state?"
    Utility = t/T (years willing to trade / total years)

  EQ-5D: Most widely used preference-based instrument.
    5 dimensions: mobility, self-care, usual activities, pain/discomfort,
    anxiety/depression. Each scored 1-5 → mapped to utility via
    country-specific population preference tariffs.
    EQ-5D-3L: ~243 health states; EQ-5D-5L: ~3,125 states

  SF-6D: Derived from SF-36 survey; wider utility range

COST-EFFECTIVENESS USING QALYS:
  ICER = ΔCost / ΔQALYs
  Willingness-to-pay (WTP) threshold: if ICER < threshold → adopt

  Thresholds:
  NICE (UK):     £20,000-30,000/QALY (~$25,000-38,000)
  WHO guidance:  1× GDP per capita (definitely adopt) to 3× GDP (possible)
  US:            No official threshold; $100,000-$150,000/QALY commonly cited
  World Bank:    $100-$200/DALY averted in LMICs often used

  ICER league table (US, illustrative):
  Statins (high-risk primary prevention): ~$25,000-50,000/QALY
  ACE inhibitors for hypertension:        ~$10,000-30,000/QALY
  Mammography (biennial, age 50-74):      ~$30,000-50,000/QALY
  Dialysis (ESRD):                        ~$50,000-100,000/QALY
  Expensive cancer drugs (end-stage):     $200,000-$1,000,000+/QALY
```

## HALE — Health-Adjusted Life Expectancy

```
HALE (Healthy Life Expectancy):
  Life expectancy × quality adjustment (based on time in disability)
  = years of life expected to be lived in full health

  HALE = LE − (years lived with disability weighted by DW)
  Or constructed from life table analogous to LE, replacing person-years
  with health-adjusted person-years (using DW-adjusted Lx)

  EXAMPLE VALUES (2019):
  Japan:        74.1 years HALE (LE 84.3) → 10.2 years with disability
  United States: 66.1 years HALE (LE 78.5) → 12.4 years with disability
  India:         60.3 years HALE (LE 70.4) → 10.1 years with disability
  Nigeria:       51.7 years HALE (LE 62.6) → 10.9 years with disability

  HALE gaps between countries often larger than LE gaps.
  High-income countries: longer life but also longer disability period
  ("expansion of morbidity" vs. "compression of morbidity" debate).

COMPRESSION OF MORBIDITY (Fries, 1980):
  Hypothesis: as populations live longer, the period of disability
  will compress near end of life (healthier most of life, then rapid decline).
  Evidence: mixed. Some countries show compression; others show expansion.
  Depends on: NCD prevention quality, healthcare effectiveness, social conditions.
```

## GBD Comparative Risk Assessment

```
POPULATION ATTRIBUTABLE FRACTION (PAF):
  PAF = [P_e × (RR − 1)] / [1 + P_e × (RR − 1)]
  P_e = prevalence of exposure
  RR = relative risk (causal, from meta-analysis)

  PAF = fraction of disease in population attributable to the risk factor
  if exposure were eliminated (or reduced to theoretical minimum)

THEORETICAL MINIMUM RISK EXPOSURE LEVEL (TMREL):
  Not zero exposure — physiologically plausible minimum
  (e.g., TMREL for blood pressure: 110-115 mmHg systolic)
  (e.g., TMREL for BMI: 20-25 kg/m²)

TOP ATTRIBUTABLE RISK FACTORS (GBD 2019, global DALYs):
  High systolic blood pressure:     10.8M deaths / 212M DALYs
  Tobacco smoking:                   8.7M deaths / 200M DALYs
  High fasting plasma glucose:       6.5M deaths / 171M DALYs
  High BMI:                          5.0M deaths / 149M DALYs
  Ambient PM2.5:                     4.2M deaths / 103M DALYs
  Diet (overall):                   11M deaths (composite risk)
  Alcohol:                           2.4M deaths / 95M DALYs
  Physical inactivity:               0.8M deaths / 17M DALYs

  IMPLICATION: Blood pressure control + tobacco elimination + glucose
  control + obesity reduction would prevent more deaths than any
  other interventions. These target the same proximate risk factors
  (CVD, diabetes, cancer). Primary prevention + NCD management =
  highest-value investment in most populations.
```

## Decision Cheat Sheet

| Metric question | Metric to use |
|---|---|
| Compare life expectancy across countries | e0 from period life table (age-standardized) |
| Control for age structure in death rate comparison | Direct or indirect standardization |
| Capture both mortality AND morbidity burden | DALY = YLL + YLD |
| Prioritize health investments by cost-effectiveness | ICER = ΔCost/ΔQALY; compare to WTP threshold |
| Measure healthy years expected, not just total years | HALE |
| Attribute disease burden to modifiable risk factors | GBD CRA → PAF × total DALYs = attributable DALYs |
| Evaluate clinical treatment coverage decision | QALY-based cost-effectiveness (NICE model) |
| Compare global burden across disease categories | GBD total DALYs by cause |

## Common Confusion Points

**YLL uses a standard life table, not actual life expectancy**: GBD YLL uses 88.9 years for everyone regardless of country. A 30-year-old dying in Nigeria gets the same YLL as a 30-year-old dying in Japan. This is a philosophical choice (equal value of all lives); earlier GBD used age discounting and sex-specific LE which were dropped for equity reasons.

**DALY vs. QALY direction**: DALYs are burden (lost health — more is worse). QALYs are benefit (health gained — more is better). DALY = YLL + YLD; QALY uses 1 − DW where DW ≈ DALY disability weight. They're mathematically related but conceptually used differently. $/DALY averted and $/QALY gained are the same intervention evaluation expressed from opposite perspectives.

**Direct vs. indirect standardization**: Direct = apply study rates to standard population. Indirect = apply reference rates to study population, compare observed to expected. Indirect (SMR) is used when age-specific rates in the study population are unstable (small numbers). Direct allows comparison between multiple populations on one standard base.

**Disability weights are not objective**: DW values come from population surveys of perceived disability severity. They reflect cultural and contextual value judgments. DW for deafness varies between hearing and deaf communities. GBD DWs reflect the majority hearing population's perception of deafness — controversial in disability rights communities. This is an inherent limitation of aggregating disparate health states into a single utility scale.
