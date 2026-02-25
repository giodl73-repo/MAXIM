# Mortality and Life Expectancy

## Mortality Analysis Framework

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MORTALITY ANALYSIS FRAMEWORK                              │
│                                                                               │
│  DATA:                    MEASURES:               MODELS:                   │
│  Vital registration        Age-specific death rate  Gompertz-Makeham         │
│  Census + survey           Standardized rate        Lee-Carter               │
│  Verbal autopsy            Life expectancy          Logistic hazard           │
│  SRS (Sample Reg System)   Years of life lost       Compression models        │
│                            Survivorship curve                                │
│                            Cause-of-death decomp.                            │
│                                                                               │
│  PERIOD vs. COHORT:                                                          │
│  Period life table: snapshot of current conditions (synthetic cohort)        │
│  Cohort life table: follows actual birth cohort through time                 │
│  Cross-sectional: bias when mortality changing rapidly (period underestimates│
│    actual cohort survival when mortality is improving)                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

## The Life Table — Full Specification

```
LIFE TABLE COLUMNS:

  x:   Exact age at start of interval
  n:   Width of interval (1 year for complete, 5 years for abridged)

  nqx: Probability of dying in interval [x, x+n) given alive at x
       = conditional death probability
       nqx = nDx / Nx   (from observed data; adjusted for person-time)

  lx:  Number surviving to exact age x from radix l₀
       Radix l₀ = 100,000 (conventional)
       l(x+n) = lx × (1 − nqx)

  ndx: Deaths in interval [x, x+n)
       ndx = lx − l(x+n) = lx × nqx

  nLx: Person-years lived in interval [x, x+n)
       nLx ≈ n × (lx + l(x+n)) / 2    (for non-infant)
       Exception: 1L0 uses special factor a₀ to account for early-year deaths
       a₀ = average fraction of year lived by those who die in year 0
           ≈ 0.1-0.15 in high-mortality settings; ≈ 0.3 in low-mortality

  Tx:  Total person-years lived beyond age x
       Tx = Σ nLj for j ≥ x

  ex:  Complete expectation of life at age x
       ex = Tx / lx
       e₀ = T₀ / l₀ = life expectancy at birth

EXAMPLE (abridged, modern low-mortality population):
  x    lx       nqx      ndx    nLx      Tx      ex
  0    100,000  0.0040   400    99,680   8,370,000  83.7
  1    99,600   0.0010   100    398,200  8,270,320  83.0
  5    99,500   0.0005    50    497,375  7,872,120  79.1
  ...
  80   50,000   0.15    7,500  228,750   720,000   14.4
  85+  25,000   1.000  25,000  170,000   170,000    6.8
```

## The Gompertz Model of Mortality

```
GOMPERTZ (1825):
  Force of mortality (hazard) increases exponentially with age:
  μ(x) = α × e^{βx}
  where α = baseline mortality level, β = rate of aging (senescence rate)

  This is also written as:
  μ(x) = a × b^x   (equivalent form)
  where a = initial mortality level, b = e^β

  BIOLOGICAL INTERPRETATION:
  β reflects rate of physiological deterioration with age.
  Remarkably stable across species — β ≈ 0.08/year for humans
  (mortality roughly doubles every 8.7 years from age 30-85).

  GOMPERTZ-MAKEHAM MODIFICATION:
  μ(x) = α × e^{βx} + γ
  γ = age-independent mortality component (accidents, infections)
  Better fit at young adult ages where accidents dominate.

  SURVIVORSHIP FUNCTION (Gompertz):
  S(x) = exp[-(α/β)(e^{βx} - 1)]

  FIT RANGE: Excellent for ages 30-85.
  Breaks down:
  - Below 30: accidents/exogenous mortality dominate; not exponential rise
  - Above 90-95: mortality deceleration (mortality plateau) observed
    → logistic hazard fits better at very old ages

MORTALITY DECELERATION AT EXTREME AGE:
  Observed in most populations: μ(x) growth slows above age 95.
  Hypotheses:
  1. Selection: frailest individuals die early; survivors are hardier (heterogeneity)
  2. Biological repair mechanisms maintain competitively at very old age
  3. Data quality: age misreporting at extreme ages (common in LMICs)
  Evidence: primarily selection + data quality; true biological plateau debated.
  Maximum recorded lifespan: Jeanne Calment (France), 122 years 164 days.
```

## The Lee-Carter Model

The dominant model for mortality forecasting:

```
LEE-CARTER MODEL (1992):
  ln(μ(x,t)) = αₓ + βₓ × κₜ + εₓₜ

  where:
  μ(x,t) = central death rate at age x in year t
  αₓ      = age-specific average mortality level
  βₓ      = age-specific sensitivity to temporal change
  κₜ      = time index capturing overall mortality change
  εₓₜ     = error term

  METHOD: Singular value decomposition (SVD) of the matrix
  of log death rates − their age averages → extracts dominant
  temporal trend κₜ and associated age pattern βₓ.

  FORECASTING:
  Project κₜ as a random walk with drift: κ(t+1) = κ(t) + d + σε
  Convert projected κₜ → age-specific rates → life table → e₀

  STRENGTHS: Parsimonious; data-driven; uncertainty quantification natural
  WEAKNESSES: Extrapolates trends; doesn't account for structural breaks
    (cohort effects, medical advances, behavioral changes)
  EXTENSIONS: Lee-Miller, Booth-Maindonald-Smith, Cairns-Blake-Dowd (CBD for old-age)
```

## Cause-of-Death Analysis and Decomposition

```
CAUSE-OF-DEATH CLASSIFICATION:
  ICD (International Classification of Diseases) — WHO maintained.
  Currently ICD-11 (2022 implementation).
  Underlying cause of death: the disease/injury that initiated
  the chain of events leading to death.

  UNDERLYING vs. MULTIPLE CAUSES:
  Death certificate: underlying cause + contributing causes
  Diabetes may cause death via CVD → underlying = diabetes or CVD depending
  on how the chain is coded.

ARRIAGA DECOMPOSITION (1984):
  Decomposes difference in life expectancy between two populations
  (or same population at two time points) into contributions by age.

  ΔLE = e₀^A − e₀^B = Σₓ (δₓ_direct + δₓ_indirect)

  where δₓ_direct: contribution from mortality change at age x
        δₓ_indirect: contribution from downstream survival effects

  EXAMPLE — US vs. Japan ΔLE ≈ 5 years:
  Age 0-14:     +0.2 yr  (US slightly worse infant mortality)
  Age 15-49:    +0.8 yr  (US drug overdoses, accidents dominate)
  Age 50-74:    +2.1 yr  (US CVD, obesity, diabetes)
  Age 75+:      +1.9 yr  (US CVD, cancer at old age)
  Total:         +5.0 yr

CAUSE-OF-DEATH DECOMPOSITION:
  Extends Arriaga to decompose by cause:
  Which causes of death account for ΔLE between groups?

  US-Japan gap decomposed:
    Drug overdoses: ~0.8 yr
    Cardiovascular disease: ~1.8 yr
    Diabetes: ~0.5 yr
    Obesity-related cancers: ~0.4 yr
    Homicide/violence: ~0.3 yr
    → All preventable causes
```

## Survivorship Curves and Mortality Patterns

```
THREE MAIN SURVIVORSHIP CURVE TYPES:

  TYPE I (Convex — humans in rich countries):
  l(x) stays near 100K until old age, then drops sharply
  l(x)
  100K|████████████████████
      |                   ██████
      |                        ████
      |                            ██
      |                              ████
   0  |_______________________________|___ age
                                          ~80-85

  TYPE II (Linear — birds, some mammals):
  Constant mortality rate through life
  l(x) = l₀ × e^{-dx}

  TYPE III (Concave — most fish, invertebrates, plants):
  Very high early mortality (most die young); survivors persist
  l(x) drops rapidly early then flattens

  HUMAN TRAJECTORY OVER HISTORY:
  High-mortality historical populations: Type II-ish (constant high mortality)
  Modern populations: Type I (nearly rectangular — "rectangular" survivorship)
  Rectangularization trend: increasing survival through adulthood → sharp terminal drop
```

## Compression of Morbidity vs. Expansion

```
COMPRESSION OF MORBIDITY HYPOTHESIS (Fries 1980):
  As populations age and medicine improves:
  → Life expectancy reaches biological limit (~85 years)
  → Chronic disease onset shifts later in life
  → Period of morbidity/disability "compresses" near end of life
  → Healthy lifespan ≈ total lifespan (die healthy, then quickly)

  EXPANSION OF MORBIDITY HYPOTHESIS (Gruenberg 1977 / Kramer 1980):
  Medical progress extends life by treating disease but not curing it.
  → More people live longer WITH disability and chronic disease
  → Morbidity period EXPANDS relative to total lifespan

  DYNAMIC EQUILIBRIUM HYPOTHESIS (Manton 1982):
  Neither pure compression nor pure expansion.
  Disease prevalence rises but severity is reduced by medical management.
  Period with some disability constant; severe disability decreasing.

  EMPIRICAL EVIDENCE (US, UK):
  Self-reported disability in late life: mixed trends
  Some conditions improving (severe functional limitation): consistent with compression
  Some expanding (multi-morbidity, dementia): consistent with expansion
  HALE vs. LE trends: HALE growing slower than LE in many countries → mild expansion
  No consensus; country- and condition-specific
```

## Mortality Trends and COVID-19 Impact

```
LONG-RUN TRENDS:
  Global life expectancy:
  1950: ~48 years
  2000: ~67 years
  2019: ~73.4 years
  Growth rate ~0.5 years per calendar year (roughly)

  MAJOR GAINS FROM:
  Infant/child mortality: vaccines, antibiotics, nutrition, sanitation
  Cardiovascular disease: statins, antihypertensives, smoking reduction
  Cancer: earlier detection, better treatment
  HIV/AIDS: antiretroviral therapy (ART) from 1996 → huge gains in SSA

COVID-19 IMPACT ON MORTALITY:
  2020-2021: Largest setback in global life expectancy since WWII
  Global LE fell ~1.8 years (2019 to 2021) by WHO estimates
  US: LE fell from 78.8 (2019) to 76.4 (2021) — 2.4 year decline
  Russia: ~5 year decline
  Excess mortality vs. reported COVID deaths:
    Excess mortality estimates: 15-18M globally (vs. 6M reported)
    Model: compare observed deaths 2020-21 to predicted from pre-pandemic trends

EXCESS MORTALITY:
  Excess mortality = observed deaths − expected deaths (counterfactual)
  Avoids problems with variable COVID testing/attribution across countries
  The Economist, WHO, IHME all published competing estimates (methodology varies)
  Convergent finding: actual mortality impact 2-3× reported COVID death count
```

## Decision Cheat Sheet

| Mortality question | Tool |
|---|---|
| Summarize mortality across ages in one number | Life expectancy e₀ |
| Compare populations with different age structures | Age-standardized death rates or life expectancy |
| Model how mortality risk changes with age | Gompertz: μ(x) = α·e^{βx} |
| Forecast future mortality trajectory | Lee-Carter model with projected κt |
| Attribute LE difference to age groups | Arriaga decomposition |
| Attribute LE difference to cause of death | Cause-of-death decomposition |
| Assess disability-adjusted health | HALE (Healthy Adjusted Life Expectancy) |
| Measure impact of a disease intervention | Reduction in cause-specific mortality → ΔLE |

## Common Confusion Points

**Life expectancy reflects CURRENT conditions, not future experience**: A life expectancy of 82 computed in 2023 means: if 2023 age-specific death rates persist forever, a newborn would live 82 years. Actual cohorts born today will likely live longer (if mortality continues improving) or shorter (if conditions worsen). The period life table is a snapshot, not a forecast.

**e₀ at birth vs. conditional life expectancy**: Infant mortality substantially depresses e₀. In high-infant-mortality settings, a child who survives to age 5 has much higher remaining life expectancy than e₀ suggests. e₅ + 5 (total life expectancy conditional on surviving to age 5) is sometimes more informative.

**Gompertz doubling time vs. calendar doubling time**: Gompertz β ≈ 0.085 means mortality HAZARD doubles every ~8 years from age 30-85. This is a statement about individual aging risk, not population growth. Doubling time of hazard = ln(2)/β = 0.693/0.085 ≈ 8.2 years.

**Cause-of-death data quality**: In countries without complete vital registration (<60% of deaths have certified cause), cause-of-death data is modeled. GBD redistributes "garbage codes" (ill-defined causes like "heart failure" or "old age") to probable underlying causes. This modeling introduces uncertainty; cause-specific comparisons across countries with very different data quality require caution.
