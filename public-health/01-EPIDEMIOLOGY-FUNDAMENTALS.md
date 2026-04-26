# Epidemiology Fundamentals

## The Epidemiological Triad and Study Design Hierarchy

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     EPIDEMIOLOGY LANDSCAPE                                  │
│                                                                             │
│   EXPOSURE ──────────────→ OUTCOME                                          │
│   (risk factor, treatment)   (disease, death, health event)                 │
│                                                                             │
│   The core question: Is the association causal?                             │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────────┐ │
│   │              STUDY DESIGN HIERARCHY (internal validity)               │  │
│   │                                                                       │  │
│   │  STRONGEST   Randomized Controlled Trial (RCT)                        │  │
│   │      │       ├── Parallel group  ├── Crossover  ├── Cluster RCT       │  │
│   │      │                                                                │  │
│   │      │       Quasi-experimental                                       │  │
│   │      │       ├── Interrupted time series  ├── Difference-in-diff      │  │
│   │      │       ├── Regression discontinuity  ├── Instrumental variable  │  │
│   │      │                                                                │  │
│   │      │       Observational (analytical)                               │  │
│   │      │       ├── Prospective cohort  ← best for incidence/RR          │  │
│   │      │       ├── Retrospective cohort                                 │  │
│   │      │       ├── Case-control  ← best for rare diseases               │  │
│   │      │       └── Cross-sectional  ← prevalence, not incidence         │  │
│   │      │                                                                │  │
│   │  WEAKEST     Descriptive (ecological, case report, case series)       │  │
│   │                                                                       │  │
│   └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Core Measures: Incidence and Prevalence

```
INCIDENCE
  Cumulative incidence (risk):
    CI = (new cases during period) / (population at risk at start)
    Units: proportion (0–1), no time dimension
    Use: What fraction developed disease over follow-up?

  Incidence rate (incidence density):
    IR = (new cases) / (person-time at risk)
    Units: cases per 1000 person-years
    Use: When follow-up time varies across individuals

    Person-time = Σ time each individual was under observation and at risk
    Example: 100 people followed avg 2.5 years = 250 person-years

PREVALENCE
  Point prevalence: existing cases / population at time T
  Period prevalence: cases at any point during interval / population

  KEY RELATIONSHIP:
    P ≈ I × D
    Prevalence ≈ Incidence × mean disease Duration

    Implication: Effective treatment (shorter D) lowers prevalence
    without changing incidence. Improved survival can INCREASE
    prevalence of a chronic disease even if incidence is stable.
```

## Risk Measures and Their Interpretation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     RISK MEASURES                                           │
├──────────────────────────┬─────────────────────────────────────────────────┤
│  RELATIVE MEASURES       │  ABSOLUTE MEASURES                               │
├──────────────────────────┼─────────────────────────────────────────────────┤
│                          │                                                 │
│  Risk Ratio (RR)         │  Risk Difference (RD) = Attributable Risk       │
│  = CI_exposed / CI_unexpo│  = CI_exposed − CI_unexposed                    │
│                          │  Interpretation: extra risk per person exposed  │
│  Interpretation:         │                                                 │
│  RR=2: 2× more likely    │  Population Attributable Risk (PAR)             │
│  RR=1: no association    │  = p_exp × (RR − 1) / [1 + p_exp × (RR − 1)]    │
│  RR<1: protective        │  where p_exp = prevalence of exposure           │
│                          │  Interpretation: fraction of disease in         │
│  Rate Ratio              │  population attributable to exposure            │
│  = IR_exposed / IR_unexp │                                                 │
│                          │  Number Needed to Treat (NNT)                   │
│  Odds Ratio (OR)         │  = 1 / RD                                       │
│  = (a/b) / (c/d)         │  Interpretation: treat N people to prevent 1    │
│  = ad / bc (2×2 table)   │  outcome                                        │
│  → approximates RR when  │                                                 │
│    disease is rare       │  Number Needed to Harm (NNH) = 1 / RD_harm      │
│                          │                                                 │
└──────────────────────────┴─────────────────────────────────────────────────┘

2×2 TABLE:

                    Disease+    Disease−
  Exposed+            a           b         → CI_exp = a/(a+b)
  Exposed−            c           d         → CI_unexp = c/(c+d)

  RR = [a/(a+b)] / [c/(c+d)]
  OR  = (a×d) / (b×c)    ← used in case-control (cannot compute RR directly)
```

## Confounding — The Core Threat to Causal Inference

```
CONFOUNDING:
  A confounder C is associated with both the exposure E and outcome D,
  and is not in the causal pathway from E to D.

  E ────────────────────→ D
  ↑                      ↑
  └──────── C ────────────┘

  Classic example: Coffee (E) and pancreatic cancer (D).
  Confounders: Smoking (associated with both coffee drinking AND cancer).
  Spurious association if smokers also drink more coffee.

METHODS TO CONTROL CONFOUNDING:

  At design stage:
  ├── Randomization (eliminates confounding by known and unknown factors)
  ├── Restriction (study only unexposed to confounder)
  ├── Matching (case-control: match on confounders)
  └── Propensity score matching (observational studies)

  At analysis stage:
  ├── Stratification (Mantel-Haenszel pooling across strata)
  ├── Multivariable regression (adjust for measured confounders)
  ├── Instrumental variable (IV) analysis
  └── Difference-in-differences (quasi-experimental)

  Cannot control: Unmeasured/unknown confounders
  → This is why RCTs are the gold standard for causal inference

EFFECT MODIFICATION (INTERACTION):
  Not confounding — a true biological heterogeneity.
  The effect of E on D differs across levels of a third variable M.
  Should be reported, not adjusted away.
  Example: Aspirin prevents heart attacks in men more than women.
```

## Study Designs: Strengths and Limitations

| Design | Direction | OR/RR | Rare disease? | Rare exposure? | Cost | Time |
|---|---|---|---|---|---|---|
| **RCT** | Forward | RR directly | Poor (need huge N) | Yes | Highest | Long |
| **Prospective cohort** | Forward | RR directly | Poor | Yes | High | Long |
| **Retrospective cohort** | Backward | RR directly | Poor | Yes | Medium | Faster |
| **Case-control** | Backward | OR (≈RR if rare) | Excellent | Poor | Low | Fast |
| **Cross-sectional** | None | Prevalence OR | OK | OK | Low | Fast |
| **Ecological** | Aggregated | Ecological RR | OK | OK | Low | Fast |

**Ecological fallacy**: Associations at population level do not necessarily hold at individual level. Aggregate data on income and health outcomes cannot tell you whether richer individuals within a country are healthier.

## Bias Taxonomy

```
SELECTION BIAS: Systematic error from how participants are selected
  ├── Healthy worker effect: employed cohorts healthier than general pop
  ├── Berkson's bias: hospital controls differ from community (case-control)
  ├── Loss to follow-up: dropout correlated with outcome
  └── Volunteer bias: study participants healthier than non-participants

INFORMATION (MEASUREMENT) BIAS: Systematic error in measuring exposure/outcome
  ├── Recall bias: cases remember exposures better than controls
  ├── Observer bias: investigator differentially classifies based on hypothesis
  ├── Differential misclassification: bias direction predictable
  └── Non-differential misclassification: bias toward null (underestimation)

CONFOUNDING: Third variable creates spurious association (see above)
```

## Bradford Hill Criteria — Structured Causal Inference

Published 1965. These are not criteria that must all be met — they are considerations that strengthen or weaken a causal inference. No single criterion is necessary or sufficient.

| Criterion | Meaning | Stronger when... |
|---|---|---|
| **Strength** | Magnitude of association | RR large (hard to explain by bias alone) |
| **Consistency** | Replicated across studies/settings | Multiple independent studies agree |
| **Specificity** | Exposure causes only this outcome | One cause → one effect (weakest criterion) |
| **Temporality** | Cause precedes effect | REQUIRED — only non-optional criterion |
| **Biological gradient** | Dose-response relationship | More exposure → more disease |
| **Plausibility** | Biological mechanism exists | Known pathway consistent with finding |
| **Coherence** | Consistent with natural history | Doesn't contradict known biology |
| **Experiment** | Removing exposure reduces disease | Quasi-experimental or intervention evidence |
| **Analogy** | Similar cause-effect known | Analogous drug-disease pair exists |

**Connection to statistics-applied/**: Bradford Hill is structured causal reasoning under observational constraints — the epidemiologist's answer to "we can't randomize, so what do we do?" It anticipates the modern potential outcomes framework (Rubin, 1974) and DAG-based causal inference (Pearl). Temporality maps exactly to the requirement that cause precedes effect in any causal DAG.

## Sensitivity, Specificity, and Screening

```
DIAGNOSTIC TEST PERFORMANCE:

                    True state:
                    Disease+    Disease−
  Test+       TP (true pos)    FP (false pos)    → PPV = TP/(TP+FP)
  Test−       FN (false neg)   TN (true neg)     → NPV = TN/(TN+FN)
                    ↓                ↓
               Sensitivity      Specificity
             = TP/(TP+FN)     = TN/(TN+FP)

TRADEOFFS:
  Higher threshold → higher specificity, lower sensitivity
  Lower threshold → higher sensitivity, lower specificity

  In screening programs: favor high sensitivity (don't miss cases)
  In confirmatory tests: favor high specificity (avoid false positives)

BAYES' THEOREM IN DIAGNOSIS:
  PPV = (Sensitivity × Prevalence) /
        (Sensitivity × Prevalence + (1−Specificity) × (1−Prevalence))

  Even a 99% sensitive and 99% specific test has PPV ≈ 50% when
  disease prevalence is 1%. This is why screening general populations
  for rare diseases generates false positive floods.
```

## Survival Analysis Basics

Survival analysis handles time-to-event data where not all subjects reach the event (censoring):

```
Kaplan-Meier:
  S(t) = Π_{ti≤t} [(ni − di) / ni]
  where ni = at-risk at time ti, di = events at ti
  Non-parametric. Handles censoring. Produces survival curve.

Log-rank test: Compares survival curves between groups (non-parametric).

Cox proportional hazards:
  h(t|X) = h0(t) × exp(β₁X₁ + β₂X₂ + ... + βkXk)
  Semi-parametric: baseline hazard h0(t) unspecified, covariates parametric.
  Hazard ratio (HR) = exp(βi) for covariate Xi.
  HR = 2 means 2× instantaneous rate of the event at any time.
```

## Meta-analysis and Systematic Review

```
HIERARCHY OF EVIDENCE:
  Systematic review + meta-analysis
          ↑
  Multiple RCTs
          ↑
  Single RCT
          ↑
  Cohort studies
          ↑
  Case-control
          ↑
  Case series/expert opinion

META-ANALYSIS:
  Pools effect estimates across studies.
  Fixed-effects model: assumes single true effect, variation is sampling error.
  Random-effects model: assumes true effect varies across studies (heterogeneity).

  I² statistic: proportion of variance due to heterogeneity
    I² < 25%: low heterogeneity
    I² 25-75%: moderate
    I² > 75%: high — pooling questionable

  Funnel plot: asymmetry suggests publication bias.
  Egger's test: formal test for funnel plot asymmetry.
```

## Decision Cheat Sheet

| Scenario | Study design | Key measure |
|---|---|---|
| Evaluate new drug for efficacy | RCT | RR, NNT |
| Follow smokers forward to cancer | Prospective cohort | RR, incidence rate |
| Investigate rare cancer cluster | Case-control | OR (≈ RR if rare) |
| Estimate population disease burden | Cross-sectional | Prevalence |
| Test policy effect at ecological level | Ecological / ITS | Ecological RR |
| Adjust for confounders in cohort | Multivariable Cox | HR |
| Pool 20 RCTs on same intervention | Meta-analysis | Pooled RR/OR, I² |
| Establish causation from observational data | Bradford Hill criteria | Weight of evidence |
| Screen general population for disease | Bayes PPV analysis | PPV, false positive rate |

## Common Confusion Points

**OR vs RR**: OR always overestimates RR when disease is common (>10% prevalence). For rare diseases, OR ≈ RR. Case-control studies can only compute OR. Cohort studies and RCTs compute RR directly. Never interpret OR as if it were RR when disease is common.

**Confounding vs. effect modification**: Confounding is a nuisance to control. Effect modification is a finding to report. If the effect of aspirin on MI differs by sex, that's effect modification — analyzing only the overall effect misses important biological heterogeneity.

**Significance vs. precision**: Statistical significance (p < 0.05) says nothing about effect size. A huge study finds statistically significant RR = 1.003 — meaningless clinically. A small study finds non-significant RR = 2.1 with CI [0.9, 4.8] — possibly important, just underpowered. Always report effect size and confidence interval.

**Lead time bias in screening**: If screening detects disease earlier but doesn't change time of death, survival from diagnosis appears longer — not because treatment works, but because the clock started earlier. Always compare age-at-death or cause-specific mortality, not survival-from-diagnosis.

**Temporality is the only required Bradford Hill criterion**: All others are probabilistic evidence. An association where the exposure follows the disease cannot be causal by definition — the criterion is absolute.
