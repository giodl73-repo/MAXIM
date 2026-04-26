# Population Dynamics

## The Balancing Equation as a Dynamical System

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    POPULATION CHANGE MECHANICS                              │
│                                                                               │
│  P(t+1) = P(t) + B(t) − D(t) + IM(t) − EM(t)                              │
│                                                                               │
│  Components:                                                                  │
│  B(t)  = Births in period t → t+1        determined by ASFR × women_x       │
│  D(t)  = Deaths in period t → t+1        determined by ASDR × N_x           │
│  IM(t) = In-migrants in period            driven by economic/political forces │
│  EM(t) = Out-migrants in period           selective, age/skill-structured   │
│                                                                               │
│  NATURAL INCREASE:  NI = B − D                                              │
│  NET MIGRATION:     NM = IM − EM                                            │
│  GROWTH:            ΔP = NI + NM                                            │
│                                                                               │
│  Population growth rate: r = ΔP/P = (NI + NM)/P                             │
│  ≈ CBR − CDR + Net migration rate                                           │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘

Continuous form (closed population, no migration):
  dP/dt = (b(t) − d(t)) × P(t)
  where b(t) = birth rate per person, d(t) = death rate per person

If b − d = r is constant:
  P(t) = P(0) × e^{rt}
  Exponential growth (Malthusian model)

Doubling time: t₂ = ln(2)/r ≈ 0.693/r
  r = 0.03 (3% growth) → t₂ ≈ 23 years
  r = 0.01 (1% growth) → t₂ ≈ 69 years  (Rule of 70)
```

## Rates — Crude vs. Age-Specific

```
CRUDE BIRTH RATE (CBR):
  CBR = B / P_mid × 1000
  P_mid = midyear population
  Units: live births per 1,000 population per year
  Typical range: 8-15 (low fertility countries) to 35-50 (high fertility countries)

CRUDE DEATH RATE (CDR):
  CDR = D / P_mid × 1000
  Typical range: 6-10 (most countries) to 15+ (extremely old or high-mortality populations)
  Paradox: CDR often LOW in high-mortality LMICs because age structure is young
  Japan CDR > Bangladesh CDR even though Japanese health is far better

RATE OF NATURAL INCREASE (RNI):
  RNI = (CBR − CDR) / 1000
  = proportional annual growth from natural increase only
  Global 2023: CBR ≈ 17.7, CDR ≈ 7.7 → RNI ≈ 1.0%

AGE-SPECIFIC DEATH RATE (ASDR):
  ASDR_x = D_x / N_x × 1000
  where D_x = deaths at age x, N_x = population at age x

AGE-SPECIFIC FERTILITY RATE (ASFR):
  ASFR_x = B_x / W_x × 1000
  where B_x = births to women aged x, W_x = women aged x
  Summed across reproductive ages (15-49) → General Fertility Rate
  Weighted appropriately → TFR (see 02-FERTILITY)
```

## The Age Structure Effect

Age structure profoundly affects crude rates independent of true health/fertility conditions:

```
POPULATION A (young structure):          POPULATION B (old structure):
Age  Population   Deaths  ASDR           Age  Population  Deaths  ASDR
0-29    6,000       12     2.0            0-29   2,000       4      2.0
30-59   3,000       30    10.0            30-59  4,000      40     10.0
60+     1,000       80    80.0            60+    4,000     320     80.0

Total: 10,000      122    CDR=12.2        Total: 10,000    364    CDR=36.4

SAME AGE-SPECIFIC RATES → 3× different crude death rates.
CDR comparison between Population A and B is MEANINGLESS.
Must use age-standardized rates or life expectancy.

RESOLUTION:
  Direct standardization: apply both populations' ASDR to a standard
  age distribution → compare standardized rates.
  Or: compare age-specific rates directly (ASDR_x by age group).
  Or: compute life expectancy (summary of age-specific mortality pattern).
```

## Population Momentum

One of the most important and counterintuitive concepts in demography:

```
POPULATION MOMENTUM:
  Even after fertility drops to EXACTLY replacement level (NRR = 1),
  population continues to grow for generations.

  MECHANISM:
  A young population has more women in reproductive ages than a
  stable population with the same age-specific fertility.
  Even at replacement fertility, these extra women produce more births
  than the relatively small elderly cohort's deaths.
  Net: population grows until age structure normalizes.

  QUANTIFICATION:
  Momentum factor M = P_ultimate / P_current
  M = e0 × NRR_current / (T × P_current/B)
  (roughly: M ≈ 1 + (1/r) × change in NRR when at NRR>1)

  PRACTICAL ESTIMATES:
  India (2020): If fertility dropped to replacement today → population
    grows ~25% before stabilizing (from ~1.38B to ~1.7B)
  Sub-Saharan Africa: momentum factor ~1.5-2.0
    Population would roughly double even with immediate replacement fertility

  POLICY IMPLICATION:
  Demographic momentum means interventions take decades to affect population size.
  Fertility programs started today change population size in 2050-2070.
  The window to affect Africa's 2050-2100 population size is NOW.
```

## The Lotka-Leslie Framework

```
CONTINUOUS STABLE POPULATION (LOTKA 1907):
  Stable population characterized by intrinsic rate r, satisfying:

  1 = ∫₀^∞ e^{-rx} × l(x) × m(x) dx        (Euler-Lotka equation)

  l(x) = survivorship (life table) to age x
  m(x) = age-specific maternity function (ASFR for females)

  Stable age distribution: c(x) = b × l(x) × e^{-rx}
  where b = 1 / ∫₀^∞ l(x) e^{-rx} dx

DISCRETE LESLIE MATRIX (1945):
  Projects age-structured population one period at a time.

  n(t+1) = A × n(t)

  where n(t) = vector of population by age class [n₁, n₂, ..., nₖ]

  A = Leslie matrix:
  ┌─────────────────────────────────────────────────────────────────┐
  │  F₁   F₂   F₃  ...  Fₙ  ← fertilities (weighted by survival)  │
  │  P₁   0    0   ...  0   ← P₁ = survival prob from age 1 to 2    │
  │  0    P₂   0   ...  0   ← P₂ = survival from age 2 to 3         │
  │  0    0    P₃  ...  0                                           │
  │  :                  :                                           │
  │  0    0    0   ...  Pₙ  ← final class: open interval (P=Pₙ)     │
  └─────────────────────────────────────────────────────────────────┘

  Fᵢ = ½ × (fᵢ + fᵢ₊₁ × Pᵢ) × (P₀/2)    (births in age class i)
  Pᵢ = nᵢ(x+1) / nᵢ(x)                   (survival fraction)

  EIGENVALUE ANALYSIS:
  Dominant eigenvalue λ₁ = e^r = finite rate of increase per period
  λ₁ > 1: growing  λ₁ = 1: stationary  λ₁ < 1: declining

  Stable age distribution: dominant right eigenvector of A
  Reproductive value: dominant left eigenvector of A
  (reproductive value = expected future contribution to population from a
  given age class, relative to a newborn — Fisher 1930)

  Sensitivity analysis:
  ∂λ/∂aᵢⱼ = vᵢ × wⱼ / (v · w)
  (sensitivity of growth rate to matrix element = left eigenvector × right)

  ELASTICITY: proportional sensitivity = (aᵢⱼ/λ) × ∂λ/∂aᵢⱼ
  Elasticities sum to 1 → can compare relative importance of vital rates.
  For most long-lived species (including humans): elasticity of survival >> fertility
  For r-strategists (high fertility): fertility elasticity dominates
```

## Population Growth Phases

```
GLOBAL POPULATION MILESTONES:
  1 billion:   ~1804
  2 billion:   ~1927   (123 years)
  3 billion:   ~1960   (33 years)
  4 billion:   ~1974   (14 years)
  5 billion:   ~1987   (13 years)
  6 billion:   ~1999   (12 years)
  7 billion:   ~2011   (12 years)
  8 billion:   ~2022   (11 years)
  9 billion:   ~2037   (projected, 15 years — slowing)
  10 billion:  ~2057   (projected, 20 years — slowing further)
  Peak:        ~10-11B around 2080-2100 (UN medium variant)

GROWTH RATE TREND:
  Peak global growth rate: ~2.1% in 1963
  2023: ~0.9%
  Projected: <0.5% by 2050

  Global population is near its demographic inflection point.
  Growth decelerating; eventual stabilization and potential decline.
  Regional divergence: Sub-Saharan Africa still >2.5% growth;
  Europe, East Asia: near zero or negative.
```

## Decomposing Population Change

### Country Decomposition of Growth (approx. 2020s)

| Country | CBR | CDR | RNI | Net Migration Rate | Total Growth | Key dynamic |
|---|---|---|---|---|---|---|
| United States | 11 | 8 | +0.3% | +0.4% | +0.7% | Below-replacement fertility sustained by high immigration |
| Germany | 9 | 12 | −0.3% | +0.4% | +0.1% | Natural decrease offset by immigration — common in Western Europe |
| Nigeria | 38 | 10 | +2.8% | −0.1% | +2.7% | Very high natural increase dominates; migration marginal |
| Japan | 7 | 12 | −0.5% | +0.1% | −0.4% | Natural decrease + minimal net migration → sustained population decline |
| India | 17 | 7 | +1.0% | −0.1% | +0.9% | Declining from TFR 2.0; growth rate decelerating toward zero |

**Demographic decomposition**: population change is decomposed into contributions from (1) fertility shifts, (2) mortality shifts, (3) migration, and (4) age structure interaction effects (pure compositional shift). The **Kitagawa decomposition (1955)** is the standard method for separating rate effects from compositional effects; widely used in comparative demographic analysis.

## Decision Cheat Sheet

| Dynamic question | Tool |
|---|---|
| Project population 1 year forward | Balancing equation with estimated B, D, NM |
| Project population 20-50 years | Leslie matrix / cohort-component model |
| Why CDR differs despite similar health | Age structure confounding → use age-standardized rates |
| How much will population grow after fertility hits replacement? | Population momentum calculation |
| What drives long-run growth rate? | Intrinsic rate r from Euler-Lotka |
| Compare growth contributions (fertility vs. migration) | Decompose NI vs. NM in balancing equation |

## Common Confusion Points

**Natural increase ≠ natural growth**: Natural increase = births − deaths. Growth rate also includes migration. Germany has negative natural increase but near-zero total growth (due to immigration). The two components often move in opposite directions in high-income countries.

**The Rule of 70 is approximate**: Doubling time ≈ 70/r% only for small r. At r = 10%, exact doubling time is 7.27 years (70/10 ≈ 7). At r = 1%, exact = 69.3 years (70/1 ≈ 70). The approximation deteriorates for large growth rates, but holds well for the small rates typical in human populations.

**Leslie matrix vs. cohort-component model**: These are equivalent frameworks. Leslie matrix = explicit matrix algebra formulation. Cohort-component = step-by-step procedure that produces the same result. The Leslie matrix formulation makes the eigenvalue/eigenvector structure explicit and enables sensitivity/elasticity analysis.

**Momentum is asymmetric**: Population momentum is usually discussed for growing populations (young structure → continued growth). But an old population below replacement also has momentum — toward continued decline. Germany: below-replacement fertility for 50+ years → age structure skewed old → deaths persistently exceed births even with modestly improving age-specific mortality.
