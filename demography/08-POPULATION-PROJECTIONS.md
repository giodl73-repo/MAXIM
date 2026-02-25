# Population Projections

## Projection Framework

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    POPULATION PROJECTION APPROACHES                          │
│                                                                               │
│  DETERMINISTIC SCENARIOS       PROBABILISTIC             SIMPLIFIED          │
│  ──────────────────────────    ─────────────────         ──────────────────  │
│  UN: Low/Medium/High variants  UN probabilistic          Extrapolation       │
│  Conditional on assumed        forecasts (since 2015)    Exponential model   │
│  fertility/mortality/migration Time series of            Logistic model      │
│  paths                         fertility rates           (S-curve)           │
│                                Bayesian model            Cohort model        │
│                                Uncertainty intervals     simplifications     │
│                                                                               │
│  COHORT-COMPONENT MODEL: Standard method for all serious projection          │
│  - Projects each age-sex cohort forward using fertility, mortality, migration │
│  - Leslie matrix formulation                                                 │
│  - Requires assumptions for each demographic component                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Cohort-Component Model — Full Specification

```
COHORT-COMPONENT METHOD:
  The standard workhorse for population projection.
  Projects population by age group and sex separately,
  applying fertility rates to women of childbearing age
  and survival rates to each cohort.

STEP-BY-STEP ALGORITHM:
  Input: N(x, s, t) = population in age group x, sex s, at time t

  1. SURVIVAL (advance all cohorts one time period):
     N(x+n, s, t+n) = N(x, s, t) × sSₓ(t)
     where sSₓ = survival ratio = nLx+n / nLx (from life table)
     For oldest age group (open interval): survival + new entrants

  2. BIRTHS (generate new youngest cohort from fertility rates):
     B(t) = Σₓ ASFR(x, t) × N(x, female, t) × n
     (sum over 5-year age groups of reproductive-age women)

  3. SURVIVAL OF BIRTHS:
     N(0-4, male, t+5) = B(t) × (1/(1+SRB)) × ₅L₀ / l₀ × 5
     N(0-4, female, t+5) = B(t) × (SRB/(1+SRB)) × ₅L₀ / l₀ × 5
     where SRB = sex ratio at birth (typically ~1.05 males per female)

  4. MIGRATION (add net migrants to appropriate age/sex groups):
     N(x, s, t+n) += NM(x, s, t)
     (Net migrants allocated by assumed age-sex distribution)

  PROJECTED POPULATION: iterate forward in 5-year steps

  LESLIE MATRIX FORM (without migration):
  n(t+n) = A × n(t)
  where n is full age-sex vector, A is the age-sex projection matrix
  (See 01-POPULATION-DYNAMICS for matrix structure)
```

## UN World Population Prospects Methodology

```
UN WPP (World Population Prospects):
  Published every 2 years by UN Population Division, DESA.
  WPP2022: latest major revision.
  Coverage: 237 countries/territories.

DATA SOURCES:
  Fertility: UNPD synthesis from census, survey, vital registration
  Mortality: similar synthesis + special methods for child mortality
    (UN IGME: Inter-Agency Group on Child Mortality Estimation)
    cause-of-death models for LMICs
  Migration: synthesis of bilateral flow data + residual estimation

KEY MODELS:
  Fertility projection (Alkema et al. 2011; UN methodology):
    Bayesian hierarchical time series model for TFR
    Phase I (TFR > 5): fertility decline modeled as logistic function of time
    Phase II (TFR in transition): rate of decline modeled as random walk
    Phase III (TFR < 2.1): autoregressive model around 1.85-2.1 range
    Implemented as probabilistic forecast with credible intervals

  Mortality projection (UN mortality model):
    Life expectancy projection using Coherent Kannisto-Thatcher method
    Sex-specific projections; convergence modeled at very high LE
    Country-specific adjustments for HIV/AIDS, tobacco

SCENARIO VARIANTS:
  Deterministic scenarios (WPP):
    Medium: central estimate
    Low:    Medium TFR − 0.5 children
    High:   Medium TFR + 0.5 children
    Zero migration: Medium fertility/mortality, no net migration
    Constant fertility: Current period fertility throughout
    Constant mortality: Current mortality throughout
    Instant replacement: Fertility immediately → replacement

  Probabilistic forecast (since WPP2015):
    Bayesian hierarchical models → 80% and 95% prediction intervals
    UN 2100 projection (WPP2022):
      Median: 10.4B
      80% CI: 9.4B – 12.7B
      95% CI: 8.9B – 12.4B  ← enormous uncertainty
```

## Uncertainty in Long-Run Projections

```
SOURCES OF PROJECTION UNCERTAINTY:

  FERTILITY:
    Most uncertain component long-term.
    Will Sub-Saharan Africa follow similar transition path to Asia?
    How far will fertility fall in East Asia? Recovery possible?
    What are actual fertility desires vs. constrained fertility?

  MORTALITY:
    Less uncertain historically — generally declining.
    Key uncertainties:
    - Pace of mortality improvement at old ages
    - Effect of climate change on mortality
    - Pandemic risk (COVID-19 showed sudden mortality shocks)
    - Long COVID, drug overdose epidemics (US LE already declining)

  MIGRATION:
    Most episodic and politically determined component.
    Policy shocks: Brexit → UK migration patterns shifted
    Conflict: Syrian civil war → 5M+ international refugees
    Climate migration: difficult to project; potentially large
    Political unpredictability makes migration projections least reliable

PROJECTION UNCERTAINTY BY HORIZON:
  5-year:    Small: age structure largely determined by existing population
             Migration uncertainty; mortality shocks possible
  10-year:   Moderate: fertility choices affect birth cohort size
  20-year:   Substantial: fertility rates highly uncertain
  30-year:   Large: cumulative fertility uncertainty dominates
  50-year+:  Very large: multiple demographic generations of uncertainty
  100-year:  Scenarios rather than forecasts; structural uncertainty dominant

IIASA ALTERNATIVE PROJECTIONS:
  International Institute for Applied Systems Analysis.
  Wittgenstein Centre for Demography and Global Human Capital.
  Uses education as additional projection variable (beyond age/sex).
  More educated women → lower fertility → slower growth.
  Education scenarios lead to different population outcomes.
  IIASA 2023 "advanced scenario" (fast education spread):
    Global peak ~9.7B around 2070; decline to ~8.8B by 2100.
    Substantially lower than UN median due to education-fertility link.
```

## Stochastic vs. Deterministic Projections

```
DETERMINISTIC SCENARIOS:
  Specify assumed paths for fertility, mortality, migration.
  No explicit uncertainty quantification.
  Pros: transparent, interpretable, policy-relevant ("what if" analysis)
  Cons: range of scenarios not a probability distribution
    (High and Low variants are NOT confidence intervals)

  COMMON MISTAKE: UN High and Low variants span ± 0.5 TFR from medium.
  These are NOT the 95% confidence interval.
  Actual uncertainty is larger and irregular.

PROBABILISTIC FORECASTING:
  Bayesian hierarchical models (Raftery, Alkema, et al.; adopted by UN):
  Approach:
  1. Model past TFR trajectories for all countries
  2. Estimate prior distribution for parameters
  3. Update with country-specific data
  4. Sample future trajectories → posterior predictive distribution
  5. Apply to mortality model → sample life expectancy trajectories
  6. Combine in cohort-component model → population trajectory distribution

  RESULT: 80% and 95% prediction intervals for population by country

  UN 2100 Probabilistic Results (WPP2022):
  World:           10.4B median  [9.4–12.7B at 80%]
  Africa:          3.9B median   [3.2–5.3B at 80%]
  Asia:            4.7B median   [4.0–5.6B at 80%]
  Europe:          0.72B median  [0.65–0.79B at 80%]
  N. America:      0.45B median  [0.39–0.52B at 80%]
  Latin America:   0.72B median  [0.58–0.92B at 80%]

  KEY: Africa's uncertainty range spans 2.1B people. More than all of Europe.
  The key uncertainty is Sub-Saharan Africa fertility transition speed.

  This is Bayesian forecasting under uncertainty — see statistics-applied/.
  The UN model is a production-quality Bayesian hierarchical time series model
  with explicit credible intervals — exactly what Bayesian forecasting is for.
```

## Illustrative Projections — Key Countries

```
UN WPP2022 POPULATION PROJECTIONS (2050 and 2100 median):

Country         2023       2050       2100
──────────────────────────────────────────────────
India           1,428M     1,670M     1,530M   (peak ~2065)
China           1,426M     1,317M       771M   (sustained decline)
United States     340M       375M       394M
Nigeria           224M       377M       546M
Pakistan          231M       367M       421M
Brazil            216M       231M       185M
Bangladesh        173M       204M       151M
DR Congo          101M       215M       432M
Ethiopia          124M       216M       323M
Tanzania          65M        129M       244M
Germany            83M        81M        82M
Japan             123M        97M        60M
South Korea        52M        46M        24M
Italy              60M        53M        43M

KEY TAKEAWAYS:
- India will remain world's most populous through 2100 (UN median)
- China: sustained rapid decline; Japan-like trajectory
- Nigeria, DRC, Tanzania, Ethiopia: dramatic growth; fertility transition speed = key uncertainty
- Germany, Japan, South Korea, Italy: sustained population decline
- US: slow growth (immigration sustaining it)
```

## Decision Cheat Sheet

| Projection question | Method |
|---|---|
| Project population 5-20 years | Cohort-component model with best-estimate vital rates |
| Project population 30-100 years | Probabilistic forecast with credible intervals |
| Test sensitivity to fertility assumptions | Deterministic high/low scenarios |
| Get official national/global projections | UN WPP (wpp.un.org); latest = WPP2022 |
| Alternative with education variables | IIASA/Wittgenstein Centre SSP projections |
| Quantify projection uncertainty | UN probabilistic forecast 80%/95% intervals |
| Understand why Africa's projection so uncertain | Fertility transition speed is the dominant unknown |

## Common Confusion Points

**UN Low and High variants are NOT confidence intervals**: They are deterministic scenarios with ±0.5 TFR deviation from medium. The probabilistic forecasts (since WPP2015) provide actual credible intervals. The scenario range understates true uncertainty; the probabilistic intervals are wider.

**Projections ≠ forecasts ≠ predictions**: A projection is conditional: "IF fertility follows path X, population will be Y." A forecast assigns probability to outcomes. A prediction is a single-point statement. Long-run population projections are better understood as conditional scenarios than unconditional forecasts.

**Short-run projections are much more accurate**: 5-10 year projections are primarily constrained by existing age structure (the population will age regardless of fertility). 50+ year projections are dominated by fertility uncertainty. The 2100 range spans billions of people — it's a plausible scenario envelope, not a narrow forecast.

**Population projections assume no catastrophes**: UN projections don't include pandemic scenarios, nuclear war, major famine, or other catastrophic events. They model "normal" demographic evolution. Actual trajectories could deviate dramatically from any projection if such events occur.
