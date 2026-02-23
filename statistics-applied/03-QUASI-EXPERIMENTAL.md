# Quasi-Experimental Methods — DiD, RDD, Synthetic Control, IV

## The Big Picture

```
+------------------------------------------------------------------+
|        IDENTIFICATION STRATEGIES: ASSUMPTIONS AND CONTEXTS       |
|                                                                  |
|  METHOD         | CORE ASSUMPTION           | NATURAL CONTEXT    |
|  DiD            | Parallel trends           | Policy rollout,    |
|                 | (untreated → counterfactual)| staggered adoption|
|                 |                           |                    |
|  RDD            | Continuity at threshold   | Eligibility rules, |
|                 | (no sorting/manipulation) | test score cutoffs |
|                 |                           |                    |
|  Synthetic Ctrl | Pre-treatment fit as      | Single treated     |
|                 | counterfactual proxy      | unit, many periods |
|                 |                           |                    |
|  IV             | Exclusion restriction     | Natural experiments|
|                 | (Z→D, Z not → Y directly) | lottery, geography |
|                 |                           |                    |
|  ITS            | Stable trend before event | Single series,     |
|                 | → counterfactual trend    | many time periods  |
|                 |                           |                    |
|  NONE OF THESE IDENTIFY WITHOUT THEIR ASSUMPTION.                |
|  The assumption is untestable; assess its plausibility.          |
+------------------------------------------------------------------+
```

---

## Difference-in-Differences (DiD)

```
SETUP:
  Treated group (T): receives treatment at time t₀
  Control group (C): never treated (or treated later)
  Pre-period: before t₀
  Post-period: after t₀

TWO-PERIOD DiD ESTIMATOR:
  β_DiD = (Ȳ_T,post − Ȳ_T,pre) − (Ȳ_C,post − Ȳ_C,pre)

  Equivalently (regression form):
  Y_it = α + β₁×Treated_i + β₂×Post_t + β_DiD×(Treated_i × Post_t) + ε_it

  Coefficient β_DiD = the DiD estimate

  INTUITION:
  Treatment effect = change in T − change in C
  → Control group tells you what would have happened to T absent treatment
  → Valid IF: control group's trend is the counterfactual for treatment group

PARALLEL TRENDS ASSUMPTION (the identifying assumption):
  "In the absence of treatment, treated and control groups would have had
  parallel (not necessarily equal) trends in the outcome."

  FORMALLY: E[Y_T,post(0) − Y_T,pre(0)] = E[Y_C,post − Y_C,pre]
    Y_T,post(0) = counterfactual outcome for treated if untreated (unobservable)
    Satisfied in expectation when this condition holds

  TESTING PRE-TRENDS:
  If parallel trends holds, pre-treatment trends should be parallel
  Plot outcome over time by group before treatment:
  → Parallel → supportive evidence (not proof)
  → Non-parallel pre-trends → assumption likely violated; DiD invalid

  Event study specification:
  Y_it = α + Σ_k β_k × (Treated_i × 1[t−t₀=k]) + γ_i + δ_t + ε_it
  γ_i = unit fixed effects; δ_t = time fixed effects
  β_k for k<0: should be ~0 (pre-treatment effects)
  β_k for k≥0: treatment effects over time
```

### Two-Way Fixed Effects (TWFE) and Staggered DiD

```
CLASSIC TWFE (Two-Way Fixed Effects):
  Y_it = α_i + δ_t + β×(Treated_i × Post_it) + ε_it
  α_i = unit FE (removes unit-level confounders)
  δ_t = time FE (removes common time shocks)
  β = average treatment effect under parallel trends

STAGGERED ADOPTION PROBLEM:
  If different units adopt treatment at different times (common in policy):
  Unit 1: treated from period 5
  Unit 2: treated from period 8
  Unit 3: never treated

  Classic TWFE TWFE with staggered adoption = BIASED estimator
  Why: TWFE uses already-treated units as "controls" for later-treated units
  If effects are heterogeneous across time or units → negative weights possible
  → β can be negative even if every unit's treatment effect is positive

  CALLAWAY-SANT'ANNA (2021) ESTIMATOR:
  Identify group-time average treatment effects: ATT(g,t) where g = cohort (when treated)
  Aggregate only over valid (not-yet-treated) control groups
  Aggregate ATT(g,t) to get overall or dynamic effects
  R packages: did, csdid; Stata: csdid

  ALTERNATIVES:
  Sun-Abraham (2021): interaction-weighted estimator
  Borusyak et al. (2021): imputation-based estimator
  De Chaisemartin-D'Haultfoeuille (2020): first-difference approach

  RULE: For staggered DiD, use Callaway-Sant'Anna or equivalent; NOT classic TWFE
```

---

## Regression Discontinuity Design (RDD)

```
SETUP:
  Assignment rule: if Running Variable X ≥ threshold c → treated (T=1)
                   if X < c → control (T=0)
  Estimand: local average treatment effect at the threshold
  LATE_RDD = E[Y(1) - Y(0) | X = c]

IDENTIFYING ASSUMPTION (continuity):
  E[Y(0) | X] is continuous at X = c
  "Potential untreated outcomes are continuous at the threshold"
  → No jump in outcomes at c absent the treatment
  → Implies: units just above and just below c are comparable (in expectation)

ESTIMATION — LOCAL LINEAR REGRESSION:
  Separately on each side of cutoff c, within bandwidth h:
  Fit: Y = α + β×(X−c) + ε  for X ∈ [c−h, c)
  Fit: Y = α + τ + β'×(X−c) + ε  for X ∈ [c, c+h]
  τ = jump at cutoff = RDD estimate

  BANDWIDTH SELECTION:
  MSE-optimal bandwidth (Calonico-Cattaneo-Titiunik 2014):
  Trades bias (wider h → more extrapolation → more bias) vs variance (narrower → fewer obs)
  R/Stata: rdrobust implements optimal bandwidth + robust inference

  ROBUSTNESS CHECKS:
  Different bandwidths: does estimate change systematically?
  Polynomial order: linear preferred; higher polynomials overfit
  Donut RDD: exclude observations exactly at cutoff (manipulation concern)

SHARP vs FUZZY RDD:
  Sharp: P(T=1 | X≥c) = 1, P(T=1 | X<c) = 0 (perfect compliance)
  Fuzzy: P(T=1 | X≥c) jumps discontinuously at c but ≠ 1
  → Fuzzy RDD: use cutoff as instrument for actual treatment
  → Estimate = Sharp RDD estimate / First stage (jump in P(T=1))
  → IV interpretation: LATE for compliers at the threshold

MANIPULATION TEST (McCrary test):
  If units can manipulate their X value to just above cutoff → bunching
  → Density of X should be continuous at c
  Test: estimate density discontinuity at c (kernel density each side)
  If significant jump in density → manipulation suspected → validity threatened
  R: rddensity package (Cattaneo et al.)
```

---

## Synthetic Control (Abadie-Diamond-Hainmueller 2010)

```
SETUP:
  J+1 units: 1 treated, J potential controls
  T₀ periods before treatment; T₁ periods after
  Goal: construct counterfactual for the treated unit

METHOD:
  Find weights W = (w₂, w₃, ..., w_{J+1}) with wⱼ ≥ 0, Σwⱼ = 1
  such that the weighted combination of control units:
  • Matches treated unit's pre-treatment outcome trajectory
  • Matches pre-treatment predictor values (X: GDP, demographics, etc.)

  Optimization:
  min_{W} ||X₁ − X₀W||_V (distance in predictor space)
  subject to: matches pre-treatment outcomes (Y₁_pre ≈ Σwⱼ × Y_j,pre)

  V: diagonal matrix with variable-specific weights (chosen to minimize pre-period MSPE)

ESTIMATE:
  Post-treatment effect at time t:
  α̂_t = Y₁_t − Σwⱼ × Y_j,t
  (gap between actual treated unit and synthetic control)

INFERENCE — PERMUTATION:
  No asymptotic distribution theory → use placebo/permutation tests
  Run synthetic control for EACH control unit (as if it were treated)
  → Distribution of placebo effects across J control units
  → If actual treated unit's effect is in extreme tail → significant

  Significance: rank actual treated unit's effect vs J placebos
  p-value = (rank in distribution of |effects|) / (J+1)
  Often display "spaghetti plot" of all placebo paths vs actual

ADVANTAGES vs DiD:
  No parallel trends assumption (pre-trends test is part of the method)
  Pre-treatment fit is explicit and visible (not assumed)
  Handles continuous divergence, not just level shift
  Works well with a single treated unit (DiD needs many treated units for precision)

LIMITATIONS:
  Requires long pre-treatment period (many periods to achieve good fit)
  Convex hull restriction: synthetic control must be within convex hull of donors
  (can't extrapolate beyond observed control outcomes)
  Only one treated unit (or a few) — not suitable for many treated units
```

---

## Instrumental Variables (IV)

```
SETUP:
  Want to estimate: Y = f(D, ε)  (effect of D on Y)
  Problem: D is endogenous (E[D × ε] ≠ 0)
  Instrument Z:
  1. Relevance: Z affects D (first stage: F-stat > 10 rule of thumb)
  2. Exclusion restriction: Z affects Y only THROUGH D (unverifiable but arguable)
  3. Independence: Z is "as good as randomly assigned" (exogenous)

CLASSIC NATURAL EXPERIMENT EXAMPLES:
  Draft lottery → military service → earnings (Angrist, 1990)
  Quarter of birth → schooling → wages (Angrist-Krueger, 1991)
  Geographic proximity to college → college attendance → wages
  Rainfall → agricultural productivity → political institutions
  Distance to abortion provider → abortion rate → birth outcomes

TWO-STAGE LEAST SQUARES (2SLS):
  Stage 1: D̂ = π₀ + π₁Z + controls + ν (regress D on Z)
           F-statistic on Z in stage 1 = measure of relevance
  Stage 2: Y = β₀ + β_IV × D̂ + controls + ε

  β_IV = (covariance of Z with Y) / (covariance of Z with D)
       = Reduced form / First stage

  WALD ESTIMATOR (simplest IV, binary Z, binary D):
  β_IV = [E(Y|Z=1) − E(Y|Z=0)] / [E(D|Z=1) − E(D|Z=0)]
  = Intent-to-treat effect / Compliance rate

WHAT IV ESTIMATES (LATE):
  With heterogeneous treatment effects, IV estimates:
  LATE = Local Average Treatment Effect for COMPLIERS
  Compliers: units who take treatment if Z=1 and don't if Z=0
  Not: always-takers (take treatment regardless of Z)
  Not: never-takers (refuse treatment regardless of Z)
  → LATE may not equal ATE (effect for compliers ≠ average effect)
  → Important when using IV for policy recommendations to non-compliers

WEAK INSTRUMENTS:
  First stage F-stat < 10: weak instrument warning
  Consequence: 2SLS is biased toward OLS (endogenous!) in small samples
  Bias formula: B = 1/(F-stat) (approximate)
  SOLUTIONS:
  • Find stronger instrument
  • LIML (Limited Information Maximum Likelihood): less biased under weakness
  • Anderson-Rubin test: valid under weak instruments
  • Stock-Wright-Yogo weak instrument test: formal F-stat threshold

EXCLUSION RESTRICTION VIOLATIONS:
  Most IV debates are about whether the exclusion restriction holds
  Examples:
  • Quarter of birth: if Z→ school quality (not just quantity) → exclusion violated
  • Geographic instrument: if distance proxies omitted community factors → violated
  Cannot be tested statistically (is fundamentally assumption about counterfactual world)
  Can be argued by ruling out alternative pathways
```

---

## Event Studies

```
SETUP:
  Panel data: many units, many periods
  Event: some units experience event at different times (staggered)
  Goal: estimate dynamic treatment effects (how does effect evolve over time)

SPECIFICATION:
  Y_it = α_i + δ_t + Σ_{k=K_min}^{K_max} β_k × D_{it}^k + ε_it
  D_{it}^k = 1 if unit i is k periods from event at time t
  β_k: estimated effect k periods before/after event
  Typically normalize: β_{-1} = 0 (period before event = baseline)

  PRE-PERIOD: k < 0 → β_k should be ≈ 0 (test of parallel trends)
  POST-PERIOD: k ≥ 0 → β_k = estimated treatment effect at k periods after

TYPICAL VISUAL:
  Plot β_k with CI over relative time k
  → Should show flat pre-trend → sharp change at k=0 → stabilize or grow/decay
  → Pre-trend violation: systematic trend before event → confounding

STACKING EVENT STUDY:
  Separate event study for each event cohort
  → Stack datasets and include cohort × time FEs
  → Avoids TWFE contamination from other event cohorts as controls
  Cengiz et al. (2019): minimum wage application; Baker, Larcker, Wang (2022)
```

---

## Interrupted Time Series (ITS)

```
SETUP:
  Single unit, T time periods
  Structural break at t₀
  Goal: estimate effect of event at t₀ on level and/or trend

MODEL:
  Y_t = β₀ + β₁×t + β₂×D_t + β₃×(D_t × t) + ε_t
  D_t = 1[t ≥ t₀]
  β₀: intercept
  β₁: pre-event trend
  β₂: level change at event (immediate effect)
  β₃: trend change after event (long-term effect)

COUNTERFACTUAL:
  Projected pre-event trend extended as counterfactual
  → How would outcome have evolved WITHOUT the intervention?

ASSUMPTIONS:
  1. Pre-event trend is stable and correctly estimated
  2. No other events occur at t₀ (single intervention assumption)
  3. Errors are uncorrelated (or corrected: Newey-West, ARIMA-OLS)

AUTOCORRELATION:
  Time series data: usually autocorrelated
  OLS SE underestimates uncertainty if errors are correlated
  Fix: HAC (Heteroskedasticity and Autocorrelation Consistent) standard errors
  → Newey-West: lags up to m = T^(1/3) typically
  Or: model autocorrelation explicitly (ARIMA-OLS)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| When does classic TWFE DiD fail? | Staggered adoption with heterogeneous treatment effects. Uses late-treated units as controls for early-treated → negative weights → biased. Use Callaway-Sant'Anna instead. |
| What is the RDD identifying assumption? | Continuity of potential outcomes at the threshold — units just above/below the cutoff are comparable. Violated if units can sort/manipulate their running variable (test: McCrary density test). |
| What does IV estimate (not ATE)? | LATE: Local Average Treatment Effect for compliers only. Compliers = units who comply with instrument. May differ from ATE if compliers are different from full population. |
| What is the F-stat rule of thumb in IV? | First stage F-statistic > 10 indicates strong instrument. Below 10: weak instruments → 2SLS biased toward OLS → use LIML or find stronger instrument. |
| When to use synthetic control? | Single treated unit (or few), long pre-treatment panel, need visible pre-treatment fit. Doesn't require parallel trends assumption; fit is the assumption. |
| What is the exclusion restriction? | IV assumption: Z affects Y only through D, not through any other pathway. Untestable statistically; must be argued by ruling out alternative channels. |
| What pre-treatment test validates DiD? | Plot outcome by group over time pre-treatment. Parallel pre-trends support the parallel trends assumption (necessary but not sufficient). Also: test β_k ≈ 0 for k<0 in event study specification. |

---

## Common Confusion Points

**Parallel pre-trends ≠ parallel trends assumption:** Pre-period parallel trends is a TESTABLE implication of the parallel trends assumption. It's necessary but not sufficient. Trends could be parallel pre-treatment and diverge post-treatment for reasons unrelated to treatment (confounding event at t₀). Always ask: "what else happened at treatment time?"

**IV LATE ≠ ATE:** This is widely misunderstood. IV estimates the effect for compliers. Policy implications from IV estimates apply to complier-like populations, not the general population. A job training program effect for those who comply when given lottery access may not equal the effect for those who would never comply regardless.

**RDD is local:** RDD estimates the treatment effect at the threshold. Not at other values of the running variable. If the threshold is, e.g., test score = 60, the estimated effect is for students at exactly 60, not students generally. Extrapolating from local RDD estimates to the full population requires additional assumptions.

**Synthetic control doesn't work well with many treated units:** The method is designed for N_treated = 1 (or very few). With many treated units, use DiD methods. Synthetic control with many treated units = complex aggregation problem; the inference method (permutation) also breaks down.
