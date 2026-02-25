# Demography — Landscape Overview

## The Big Picture: Population as a Dynamical System

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEMOGRAPHY LANDSCAPE                                      │
│                                                                               │
│  FORMAL DEMOGRAPHY               SOCIAL DEMOGRAPHY                           │
│  (mathematical/statistical)      (contextual/behavioral)                     │
│                                                                               │
│  ┌─────────────────────┐         ┌─────────────────────────────────────┐    │
│  │ Life tables          │         │ SES gradients in fertility/mortality │    │
│  │ Cohort-component     │         │ Race/ethnicity × demographic outcomes│    │
│  │ projection           │         │ Gender and reproductive behavior     │    │
│  │ Fertility/mortality  │         │ Migration and identity               │    │
│  │ measurement          │         │ Religion and family formation        │    │
│  │ Population momentum  │         │ Policy effects on demographics       │    │
│  └─────────────────────┘         └─────────────────────────────────────┘    │
│                                                                               │
│  THREE FUNDAMENTAL PROCESSES:                                                 │
│  FERTILITY (births) + MORTALITY (deaths) + MIGRATION (in/out)               │
│  → determines population SIZE, STRUCTURE, DISTRIBUTION                      │
│                                                                               │
│  MATHEMATICAL STRUCTURE:                                                      │
│  Population = a dynamical system                                             │
│  Balancing equation = first-order difference equation                        │
│  Leslie matrix = age-structured linear system (eigenvalue theory)            │
│  Life table = survival function (same hazard framework as reliability)       │
│  Stable population theory = steady-state of the demographic system          │
└─────────────────────────────────────────────────────────────────────────────┘
```

## The Balancing Equation

The fundamental accounting identity of demography:

```
P(t+1) = P(t) + B(t) − D(t) + IM(t) − EM(t)

where:
  P(t)  = population at time t
  B(t)  = births in period (t, t+1)
  D(t)  = deaths in period (t, t+1)
  IM(t) = in-migration in period
  EM(t) = out-migration in period

Natural increase (NI) = B − D
Net migration (NM)    = IM − EM
Growth = NI + NM

This is a first-order discrete-time difference equation.
Continuous form: dP/dt = (b − d)P + NM(t)
where b = crude birth rate, d = crude death rate (per person)
```

## Data Sources

| Source | Coverage | Frequency | Strengths | Weaknesses |
|---|---|---|---|---|
| **Census** | All people in territory | Every 10 years (typically) | Complete count; age/geography detail | Expensive; undercounting; 10-year lag |
| **Vital registration** | Births, deaths, marriages | Continuous | Timely; cause-of-death | Poor coverage in LMICs; ~60% global completeness |
| **Demographic surveys** | Nationally representative samples | Every 3-5 years | Fertility, mortality estimates; LMICs | Recall error; sampling error |
| **Administrative registers** | Population movements | Continuous | Nordic countries: near-perfect | Requires unique person ID, linked systems |
| **Censuses + surveys** | Combined estimation | Ongoing | Fills gaps between sources | Model dependence |

**DHS (Demographic and Health Survey)**: USAID-funded standardized surveys in ~90 LMICs. Gold standard for fertility/mortality estimates where vital registration is poor. Collects full birth histories, contraceptive use, child mortality, HIV.

## Key Rate Concepts

```
CRUDE RATES (per 1,000 population):
  CBR = Births / Population × 1000   (Crude Birth Rate)
  CDR = Deaths / Population × 1000   (Crude Death Rate)
  Problem: confounded by age structure
  CBR high in young populations even if fertility per woman is low
  CDR low in young populations even if age-specific death rates are high

AGE-SPECIFIC RATES:
  ASFR_x = Births to women aged x / Women aged x × 1000
  ASDR_x = Deaths at age x / Population at age x × 1000

PERIOD vs. COHORT RATES:
  Period:  measures rates across all age groups in a single calendar year
           → snapshot of current behavior; may be distorted by timing changes
  Cohort:  follows a birth cohort through time
           → "pure" measure of completed fertility/mortality for that cohort
           → only fully observable after the cohort has completed reproduction/died
```

## Stable Population Theory (Lotka)

```
STABLE POPULATION (Lotka 1907):
  If ASFR and ASDR remain constant → population converges to stable
  age structure regardless of initial age distribution.

  The stable age structure is determined by:
  c(x) = b × l(x) × e^{-rx}
  where: c(x) = proportion of population at age x
         b    = birth rate of stable population
         l(x) = survivorship to age x (from life table)
         r    = intrinsic rate of natural increase (Lotka's r)

  Lotka's r satisfies the Euler-Lotka equation:
  1 = ∫₀^∞ e^{-rx} × l(x) × m(x) dx
  where m(x) = maternity function (ASFR)

  This is the characteristic equation of the demographic system.
  r > 0: growing population; r = 0: stationary; r < 0: declining

STATIONARY POPULATION:
  r = 0, NRR = 1, stable age structure.
  Special case where birth rate = death rate.

CONNECTION TO LINEAR ALGEBRA:
  Leslie matrix formulation:
  n(t+1) = A × n(t)
  where n(t) = age-structured population vector
  A = Leslie matrix (survival rates on subdiagonal, fertility on first row)
  Dominant eigenvalue λ = e^r = finite rate of increase
  Stable age structure = dominant right eigenvector of A
  Reproductive value vector = dominant left eigenvector of A
```

## Population Pyramid Types

```
THREE FUNDAMENTAL SHAPES:

  EXPANSIVE (high birth, high death):   STATIONARY:          CONSTRICTIVE:
  High CBR + CDR declining              Low birth + low death  Low birth rate
  Young population, wide base           Near-equal widths      Narrow base
                                        Rectangular
       |  |                                  |  |                    | ██ |
       | ██|                                 | ██|                   |████|
       |████|                               |████|                  |██████|
       |██████|                             |████|                   |████|
       |████████|                           |████|                   | ██ |

  Examples: Sub-Saharan Africa    Examples: Japan, W. Europe    Japan (future)
            Afghanistan, Niger    Scandinavia                   Germany

TRANSITION:
  Hourglass-like intermediate stages during demographic transition
  Bulge moves upward as the large birth cohort ages through
  → "Demographic echo" (baby boom cohort)
```

## Module Map

| Module | Mathematical Content |
|---|---|
| 01-POPULATION-DYNAMICS | Balancing equation; difference equations; momentum |
| 02-FERTILITY | TFR, NRR, Bongaarts model; tempo-quantum distinction |
| 03-MORTALITY-LIFE-EXPECTANCY | Life tables; Gompertz; hazard functions; decomposition |
| 04-MIGRATION | Gravity models; selectivity; network effects |
| 05-DEMOGRAPHIC-TRANSITION | Classic + second transition; convergence vs. divergence |
| 06-AGING | Dependency ratios; support ratios; social security math |
| 07-URBANIZATION | Urban hierarchy; Zipf's law; scaling laws |
| 08-POPULATION-PROJECTIONS | Cohort-component; Leslie matrix; stochastic projection |
| 09-DEMOGRAPHIC-DIVIDEND | Age-structure → savings → growth mechanism |

## Decision Cheat Sheet

| Demographic question | Key concept |
|---|---|
| How fast will this population grow? | r from Euler-Lotka; or balancing equation + trend rates |
| What drives population aging? | Fertility decline (primary) + mortality decline |
| Is population decline inevitable? | TFR < NRR = 1 → eventual decline, but momentum delays it |
| Will Africa's population triple? | UN median projection yes; depends on fertility transition speed |
| What is the demographic dividend? | Young working-age bulge → high savings → investment → growth |
| How are cities distributed by size? | Zipf power law (rank × size ≈ constant) |
| Best way to project population 30 years out? | Cohort-component model with probabilistic fertility assumptions |

## Common Confusion Points

**Period TFR vs. completed cohort fertility**: Period TFR (summed ASFR across all ages in one year) distorted by tempo effects (timing shifts). If women delay births, period TFR dips below cohort completed fertility. Many European countries have period TFR ~1.5 but completed fertility closer to 1.7-1.8 — the gap is tempo distortion, not a pure quantum shift.

**Population momentum**: Even after fertility falls to replacement level (TFR ≈ 2.1), population continues growing for 50-70 years due to the large cohort of young women entering reproductive ages. Sub-Saharan Africa has enormous momentum — even with rapid fertility decline, population will roughly double from current trajectory because of its young age structure.

**Replacement-level fertility ≠ 2.0**: Exact replacement TFR depends on sex ratio at birth (~1.05 males per female) and female mortality before completing reproduction. In high-mortality settings, replacement TFR > 2.1. In low-mortality settings, ~2.05-2.10. Used as threshold: below = below-replacement, above = above-replacement.

**Migration is the most unpredictable demographic variable**: Fertility and mortality follow relatively smooth long-run trends. Migration is episodic, politically determined, and subject to policy shocks. Population projections for countries with high migration rates have much larger uncertainty bands than those for closed populations.
