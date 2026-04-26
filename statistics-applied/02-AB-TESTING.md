# A/B Testing — Online Experiments, CUPED, SRM, Bandits

## The Big Picture

```
+------------------------------------------------------------------+
|            ONLINE EXPERIMENTATION ARCHITECTURE                   |
|                                                                  |
|  REQUEST → [ASSIGNMENT] → [TREATMENT] → [LOGGING] → [ANALYSIS] |
|                                                                  |
|  ASSIGNMENT:                                                     |
|  Hash(user_id + experiment_id) → bucket (0-999)                  |
|  Bucket 0-499 → control; 500-999 → treatment                     |
|  Consistent: same user always in same bucket for that experiment |
|  Sticky: assignment doesn't change during experiment             |
|                                                                  |
|  TREATMENT:                                                      |
|  Feature flag gates (config, not code deploy)                    |
|  Real-time lookup: is this user in treatment for exp_id?         |
|                                                                  |
|  LOGGING:                                                        |
|  Every assignment event logged                                   |
|  Every downstream action logged (click, purchase, etc.)          |
|  Joined by user_id, session, or device_id                        |
|                                                                  |
|  ANALYSIS:                                                       |
|  Daily metrics computation (not real-time; aggregation latency)  |
|  Statistical test: t-test / Mann-Whitney / permutation           |
|  Guardrails, primary metric, diagnostic metrics                  |
+------------------------------------------------------------------+
```

---

## Metric Taxonomy

```
GUARDRAIL METRICS (do no harm):
  Must not regress — termination condition if violated
  Cannot trade off against primary metric
  Examples:
  • Latency (p50, p95, p99): page load time
  • Crash rate / error rate
  • Core engagement (DAU, session frequency — for features that touch core)
  • Revenue (if feature is not monetization-focused)
  → "The guardrail broke" = block ship regardless of primary metric win

PRIMARY DECISION METRIC (OEC — Overall Evaluation Criterion):
  Single metric; determines ship/no-ship
  OEC properties (Kohavi et al., "Trustworthy Online Controlled Experiments"):
  1. Measurable in the experiment time frame
  2. Directable (treatment can move it)
  3. Correlated with long-term goals (proxy for what we actually care about)
  4. Sensitive enough to detect meaningful effects

  NORTH STAR METRIC (company-level): e.g., DAU, weekly active users, LTV
  → Usually too noisy for per-experiment detection; use proxies
  PROXY METRICS: conversion, CTR, session time, scroll depth
  → Must validate that moving proxy actually moves north star (metric validation)

SECONDARY / DIAGNOSTIC METRICS:
  Help explain the primary metric movement
  Not decision-making by themselves
  Example: primary = revenue; secondary = add-to-cart, conversion funnel stages
  → "Revenue up 3%; add-to-cart up 5%, conversion up 4%, AOV down 2%"
  Signals WHERE the effect came from

RATIO METRICS (careful):
  CTR = clicks / sessions — ratio of two random variables
  Naive variance: Var(clicks/sessions) ≠ Var(clicks)/Var(sessions)
  DELTA METHOD: correct variance estimate for ratios
  Var(Y/X) ≈ (1/μ_X)² × Var(Y) + (μ_Y/μ_X²)² × Var(X) − 2(μ_Y/μ_X³)Cov(Y,X)
  All major platforms use delta method automatically; know when to question it
```

### Metric Taxonomy Summary

| Type | Purpose | Example | If violated / regresses |
|---|---|---|---|
| Guardrail | Do no harm — hard stop | p99 latency, crash rate, core DAU | Block ship regardless of primary metric win |
| Primary / OEC | Ship/no-ship decision (one metric) | Session conversion rate, revenue | Treatment wins iff statistically significant improvement |
| Secondary / diagnostic | Explain primary movement | Add-to-cart rate, funnel stages | Informational only — not decision criteria |
| North star | Long-term company health (too noisy for per-experiment detection) | Weekly active users, LTV | Validated via proxy: does proxy moving actually move north star? |
| Ratio metric | Normalized engagement (CTR, AOV) | clicks/session, revenue/visitor | Use delta method for variance; naive variance is wrong |

### Bandit vs. A/B Test Comparison

| Dimension | A/B Test | Multi-Armed Bandit |
|---|---|---|
| Allocation during experiment | Fixed 50/50 (equal exploration) | Adaptive — shifts toward better arm |
| Primary objective | Estimate causal effect | Minimize regret during exploration |
| Treatment effect estimate | Unbiased | Biased (arms selected more after looking good) |
| Use case | Clean causal knowledge, feature launch, guardrail checking | Many variants, ad creative, recommendation selection |
| Statistical framework | Frequentist / anytime-valid inference | Bayesian (Thompson) or frequentist (UCB) |
| Interference detection | Full SRM checks, SUTVA auditing | Not standard |
| When NOT to use | (rarely wrong choice for serious decisions) | When you need a causal estimate or regulatory rigor |

---

## Sample Ratio Mismatch (SRM)

```
DEFINITION:
  SRM: the ratio of units in treatment vs control in analysis data
       DOES NOT MATCH the intended randomization ratio

  Expected: 50/50 (1:1 randomization)
  Observed in analysis: 48/52 (different)
  → SRM detected

DETECTION:
  Chi-squared test: χ² = Σ(observed - expected)² / expected
  p < 0.001 (very conservative threshold) → investigate SRM before analysis
  Even small SRM (49/51) with millions of users → statistically significant → must check

CAUSES OF SRM:
  1. BOT TRAFFIC: bots assigned but not logged (or logged differently)
  2. LOGGING BUG: treatment arm logs events differently from control
  3. SURVIVORSHIP BIAS: one arm has higher churn → less data survives
  4. REDIRECT/TIMING: treatment page loads slower → some requests abort → logged differently
  5. BROWSER/CLIENT CACHING: treatment/control serve different cached content inconsistently
  6. ASSIGNMENT BUG: hash collision or off-by-one in bucket boundaries

ROOT CAUSE STEPS:
  1. Check assignment log: were units assigned at right ratio?
  2. Check exposure/trigger log: were triggered units at right ratio?
  3. Check analysis data: where did the divergence happen?
  4. Compare by platform, country, browser → find where ratio breaks

RULE: NEVER ANALYZE AN EXPERIMENT WITH SRM.
  SRM means your assignment and analysis populations are different
  → Any significance finding is untrustworthy
  → Ship/no-ship decision invalid
  → Fix the issue and re-run, or analyze only the clean subset (with care)
```

---

## CUPED — Variance Reduction

```
PROBLEM:
  Outcome metric Y has high variance → need large N for statistical power
  Example: 10% CTR experiment; user CTR variance is high (some users never click)
  → Power requires millions of users; experiment runs for weeks

CUPED (Control Using Pre-Experiment Data):
  Deng, Xu, Ghosh, Zhang (2013) — Microsoft ExP team
  Key insight: user's pre-experiment behavior is highly predictive of post-experiment behavior

  PROCEDURE:
  Let Y_i = observed outcome in experiment period
  Let X_i = covariate (typically: same metric in pre-experiment period)
  Compute theta (θ) = Cov(Y, X) / Var(X)  [OLS coefficient]
  Adjusted metric: Ỹ_i = Y_i − θ(X_i − E[X])

  VARIANCE REDUCTION:
  Var(Ỹ) = Var(Y) × (1 − ρ²)
  ρ = Cor(Y, X) = correlation between pre and post metric
  ρ = 0.7: variance reduction = 1 − 0.49 = 51%
  ρ = 0.5: variance reduction = 1 − 0.25 = 25%

  TYPICAL VALUES:
  Revenue metrics: ρ ~0.5-0.7 → 25-51% variance reduction
  CTR metrics: ρ ~0.6-0.8 → 36-64% variance reduction
  Binary conversion: ρ lower (regression to mean); still useful

  KEY PROPERTIES:
  • Unbiased: E[Ỹ_treatment] − E[Ỹ_control] = E[Y_treatment] − E[Y_control]
    (θ × (E[X_treatment] - E[X_control]) = 0 if randomized)
  • Valid: t-test on Ỹ is valid; same type I error control
  • Requires: pre-experiment data for same users (new users excluded)

CUPAC (Control Using Predictions As Covariates):
  Tang et al. (2020) — DoorDash
  Use ML model prediction of Y from pre-experiment features as covariate
  → Better model → higher ρ → more variance reduction
  → Can reach ρ = 0.9+ for predictable metrics
  → Implementation: train model on historical data; use prediction as X_i in CUPED
```

---

## Novelty and Primacy Effects

```
NOVELTY EFFECT:
  New experience → users behave differently simply because it's new
  Inflates treatment effect during initial experiment period
  Decays as novelty wears off
  → Short experiment: treatment "wins" due to novelty, not actual value
  → Deployed feature: effect disappears → no real improvement

  EXAMPLE:
  New recommendation widget → users click more (curious)
  After 2 weeks: click rate returns to baseline
  Short experiment captures only the novelty spike

PRIMACY EFFECT (opposite):
  Users are ACCUSTOMED to current experience → change hurts performance initially
  Inflates control performance or deflates treatment
  → Treatment loses experiment; deployed change eventually wins as habits form
  → Common with UI changes where users need to re-learn

DETECTION:
  Day-by-day: plot metric by experiment day
  → Novelty: sharp spike on day 1-3, then decay toward baseline
  → Primacy: below-baseline on day 1-3, then rise toward true effect

  LONG-TERM HOLDBACK:
  Hold out small % of users from change (1-5%) for weeks/months
  → Direct measure of long-term effect vs short-term
  → Infrastructure cost: must maintain old experience for holdback group
  → Used by major platforms for significant feature launches

  COHORT ANALYSIS:
  New users (less primacy bias): compare new users to veterans
  → New users: no existing habit to disrupt → effect likely reflects true value
  → Veterans: primacy dominated
```

---

## Multiple Testing

```
THE PROBLEM:
  If you test N hypotheses each at α=0.05 and all null hypotheses are true:
  E[false positives] = N × 0.05
  → 20 tests → expected 1 false positive
  → 100 metrics → expected 5 false "discoveries"

FAMILY-WISE ERROR RATE (FWER):
  P(at least one false positive) across all tests in the family
  Target: control FWER ≤ α

  Bonferroni: α_individual = α / N
  → Most conservative; each test at α/N
  → Correct but very low power when N is large

  Holm-Bonferroni: step-down procedure
  → Sort p-values ascending: p₁ ≤ p₂ ≤ ... ≤ pₙ
  → Reject pᵢ if pᵢ ≤ α/(N-i+1) for all j ≤ i
  → Uniformly more powerful than Bonferroni; still controls FWER

FALSE DISCOVERY RATE (FDR):
  Benjamini-Hochberg (1995): control E[false positives / total positives] ≤ q
  → Less strict than FWER; appropriate when many tests expected to be non-null
  → Sort p-values ascending: p₁ ≤ p₂ ≤ ... ≤ pₙ
  → Reject all pᵢ ≤ (i/N) × q
  → Widely used in genomics (thousands of genes), online metrics (many secondaries)

IN A/B TESTING PRACTICE:
  Guardrails: FWER control (one false alarm = stop experiment → Bonferroni/Holm)
  Primary metric: pre-specified single test → no correction needed
  Secondary/diagnostic: FDR control acceptable; exploratory, not decision-making
  Subgroup analysis: heavily penalize for multiple comparisons OR report as exploratory

SEQUENTIAL TESTING APPROACH:
  mSPRT (Johari et al., 2017): mixture sequential probability ratio test
  • Computes likelihood ratio at each data point
  • Valid p-value at any stopping time (no inflation from continuous monitoring)
  • Implementation: weight function over θ (prior on effect size)
  Used by: Optimizely (stats accelerator), Google, LinkedIn
  Trade-off: lower power than fixed-horizon test at same final N (pay for flexibility)
```

---

## Interference and Network Effects

```
SUTVA IN ONLINE PLATFORMS:
  Violation: your treatment affects my outcomes
  Examples:
  • Social network: show user A new feature → A creates more content
    → B sees A's content change → B's behavior changes
    → B is in control but affected by A's treatment
  • Marketplace: Uber surge pricing test → treated drivers get more trips
    → Fewer drivers available for control riders → control is contaminated
  • Communication apps: treat user A → A sends more messages to B
    → B responds more → B's engagement rises (but B is in control)

SOLUTIONS:

1. CLUSTER RANDOMIZATION:
   Assign at group level (geographic cluster, social cluster)
   → Users within cluster all in same condition
   → Reduces inter-cluster interference
   Cost: fewer independent units → loss of power
   Challenge: must define clusters correctly (social clusters are fuzzy)

2. SWITCHBACK DESIGN (time-based):
   Alternate treatment periods (T, C, T, C) over time
   All units get same treatment at any given time
   → No cross-unit interference in the same time window
   → Time-based interference still possible (habit formation)
   Used by: Lyft, DoorDash for driver pricing experiments
   Requires: fast effect and short treatment windows (hourly, daily)

3. GRAPH CLUSTERING RANDOMIZATION:
   Detect communities in social graph
   → Randomize entire communities to T or C
   → Within community: interference; between: minimal
   NetEase/Airbnb/LinkedIn research on community detection for experimentation

4. TWO-SIDED MARKETPLACE:
   Experiment on buyers only or sellers only; measure other side as downstream metric
   → Or: GEO randomization (different cities/regions get treatment)
```

---

## Multi-Armed Bandits vs A/B Tests

```
EXPLORATION-EXPLOITATION TRADEOFF:
  A/B test: explore EQUALLY (50/50 throughout), then exploit (deploy winner)
  → Maximum information → minimum opportunity cost during experiment?
  → No: allocating 50% to loser has regret if one arm is clearly better

  BANDIT: adaptively shift allocation toward better-performing arm
  → Reduce opportunity cost during experimentation
  → Trade: get less precise statistical estimate

BANDIT ALGORITHMS:
  ε-greedy:
    With prob ε: explore (random arm)
    With prob 1-ε: exploit (best arm so far)
    Simple; ε-annealing (decrease ε over time)
    Problem: random exploration even when clearly best known

  UCB (Upper Confidence Bound):
    Score each arm: μ̂ₐ + c × √(log(t)/nₐ)
    → Mean reward + exploration bonus (decreases as arm is more sampled)
    → Deterministic; no randomness in selection
    → c is tuning parameter (higher c = more exploration)
    → Optimal regret: O(log T) — near-optimal

  Thompson Sampling:
    For each arm: sample from posterior distribution of reward
    Select arm with highest sample
    → Bayesian: posterior = Beta(#successes+1, #failures+1) for Bernoulli
    → Naturally explores more when uncertain, exploits when confident
    → Empirically best in practice for many settings
    → Simple implementation; extends to non-Bernoulli rewards (hierarchical models)

WHEN BANDITS vs A/B:
  USE BANDIT:
  • Many variants (product selection, ad creative)
  • High iteration velocity; exploration cheap
  • Business objective = minimize regret during experiment
  • Effect size large and stable; detection not the primary goal

  USE A/B TEST:
  • Need clean causal estimate of effect (for long-term decision)
  • Guardrails and interference checking needed
  • Launching new feature (not selecting among existing variants)
  • Need to understand WHY, not just WHAT wins
  • Regulatory/scientific rigor required

  CRITICAL NOTE:
  Thompson sampling provides BIASED estimates of treatment effects
  (arms are allocated more after looking good → selection effects)
  → Do NOT use bandit-assigned data for causal inference post-hoc
  → If you need a causal estimate, run a proper A/B test
```

---

## Heterogeneous Treatment Effects (HTE)

```
ATE = E[Y(1) - Y(0)]: average over everyone
  → Useful for: should we deploy this? (population-level)

CATE (Conditional ATE) = E[Y(1) - Y(0) | X]:
  Effect for subgroup defined by features X
  → Useful for: personalization, targeting, policy optimization

SUBGROUP ANALYSIS (DANGEROUS):
  Test 20 subgroups → expected 1 false positive
  Temptation: "It worked for users under 30 but not over 30"
  → Likely false; power was not pre-specified for this subgroup
  → Requires: pre-specified + Bonferroni correction + confirmation study

CAUSAL FORESTS (Wager & Athey, 2018):
  Generalization of random forests for CATE estimation
  Honest trees: split → estimate mechanism separate from fitting
  R² package: grf (generalized random forests)
  Key output: CATE_i for each unit + uncertainty estimates
  Wager-Athey test for heterogeneity: is any subgroup variation signal or noise?

DOUBLE ML (Chernozhukov et al.):
  Semi-parametric CATE estimation with arbitrary ML for nuisance
  Two-step: (1) residualize Y and T using ML models; (2) regress Y-residual ~ T-residual
  Valid at root-n rate despite high-dimensional controls
  econml package (Microsoft) implements

HTE IN PRACTICE:
  1. Confirm main effect first (don't hunt for HTE without main effect)
  2. Pre-register specific subgroup hypotheses (no fishing)
  3. Use calibrated methods (causal forests, DML) rather than interaction terms
  4. Require replication before personalizing based on HTE
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is SRM and what do you do? | Sample Ratio Mismatch: observed treatment/control ratio ≠ intended ratio. Indicates logging bug, bot traffic, or survivorship bias. NEVER analyze; investigate and fix first. |
| How does CUPED reduce experiment duration? | Pre-experiment covariate reduces outcome variance by (1-ρ²). For ρ=0.7: 51% variance reduction → 51% fewer users needed → same power at half the sample. |
| What is novelty effect vs primacy effect? | Novelty: users click/engage more because experience is new; inflates treatment. Primacy: users are habituated to old experience; initial disruption deflates treatment. Opposite biases, both time-decaying. |
| When should I use Thompson sampling? | When you have many variants, high throughput, and the goal is to minimize regret (opportunity cost) during exploration. Not when you need a clean causal estimate — bandits bias effect estimates. |
| Why does multiple testing require correction? | Testing N independent hypotheses at α=0.05 each: E[false positives] = 0.05N. FWER methods (Bonferroni, Holm) control P(any false positive). FDR methods (BH) control expected false discovery proportion. |
| What is the mSPRT? | Mixture Sequential Probability Ratio Test: anytime-valid p-value that doesn't inflate with continuous monitoring. Allows stopping when significance reached without pre-specifying interim count. |
| How does cluster randomization affect power? | Reduces effective N by design effect = 1 + (cluster_size - 1) × ICC. For typical cluster sizes and ICC, may require 2-5× more raw observations. |

---

## CS and Systems Bridges

| A/B testing concept | CS / systems analogue |
|---|---|
| Assignment via hash(user_id + experiment_id) | Deterministic sharding: the same input always produces the same shard — consistent, sticky assignment with no central state; identical to consistent hashing for cache or load-balancer routing |
| Feature flag gates (config, not deploy) | Feature toggles / dark launches: the treatment is a runtime config change, not a code deployment — same operational model used in continuous delivery to decouple deploy from release |
| SRM detection (chi-squared on assignment counts) | Data pipeline integrity check: SRM is an invariant violation in the logging pipeline; detecting it is equivalent to running a checksum on pipeline output — the statistical test is the audit |
| Guardrail metrics (hard stop on regression) | Service-level objectives (SLOs) with automated rollback: p99 latency or error rate guardrails are structurally identical to SLO breach alerts that trigger automatic traffic reversal |
| CUPED (regress out pre-experiment covariate) | Control variate in Monte Carlo simulation: reduce variance by subtracting a correlated known quantity — the reduction factor is (1-ρ²), same as variance reduction from control variates in numerical integration |
| mSPRT / anytime-valid inference | Streaming analytics with valid stopping: computes a likelihood ratio that is a valid test statistic at every sample size, enabling continuous monitoring without type I error inflation — analogous to online algorithms that maintain invariants at every step |
| Multiple testing (Bonferroni / BH) | Multiple comparison correction in benchmarking: testing 20 performance metrics against a baseline requires family-wise error rate control to avoid false regressions; same methods apply |
| Causal forests / Double ML for HTE | Heterogeneous subgroup analysis with ML: modern CATE estimation methods (grf, econml) replace the naive "split by segment" approach with calibrated, uncertainty-aware effect estimates — reduces false discovery in personalization |

## Common Confusion Points

**A/B testing is not just statistics:** The hardest problems are operational: consistent assignment, correct logging, SRM detection, novelty effects. Many "significant" A/B results fail to materialize post-launch because of logging or assignment issues, not statistical errors.

**Bandits don't replace A/B tests:** Bandits minimize regret during exploration. A/B tests estimate causal effects. These are different objectives. Netflix/Google/Microsoft run both in different contexts. The choice depends on whether the experiment's goal is to minimize regret or to generate causal knowledge.

**CUPED doesn't eliminate confounding:** CUPED reduces variance via regression adjustment on pre-experiment covariates. It does NOT create causal identification from observational data. You must still have valid randomization for CUPED-adjusted analysis to be causal.

**"Segment performed significantly differently" is almost always noise:** If you have 50 segments and test each at α=0.05, expected 2.5 false "significant differences." Any post-hoc subgroup finding needs validation on a fresh experiment. The more segments you test, the more skeptical you should be of any individual finding.
