# Applied Statistics — Overview

## The Landscape

```
+------------------------------------------------------------------+
|              APPLIED STATISTICS: WHAT YOU'RE REALLY DOING       |
|                                                                  |
|  THE FUNDAMENTAL QUESTION HIERARCHY (Pearl's Ladder):           |
|  Rung 1 — ASSOCIATION: P(Y | X)                                 |
|    "What do I see?" — observational data, correlations          |
|    Available from any dataset                                    |
|                                                                  |
|  Rung 2 — INTERVENTION: P(Y | do(X))                           |
|    "What happens if I act?" — requires randomization or strong  |
|    identifying assumption + structural model                     |
|    RCTs directly reach this rung                                 |
|                                                                  |
|  Rung 3 — COUNTERFACTUAL: P(Y_x=1 | X=0)                       |
|    "What would have happened?" — individual-level causal effects |
|    Requires structural causal model (SCM), not just distribution |
|                                                                  |
|  OBSERVATIONAL DATA LIVES ON RUNG 1.                            |
|  Most "data science" conclusions claim rung 2 from rung 1 data. |
|  Getting rung 2 from rung 1 requires an identification strategy. |
+------------------------------------------------------------------+
```

---

## Frequentist vs Bayesian Frameworks

```
FREQUENTIST (Neyman-Pearson + Fisher):

PHILOSOPHICAL STANCE:
  Parameters (θ) are FIXED but unknown constants
  Data (X) is RANDOM — different samples would give different X
  Probability = long-run frequency of events

CONFIDENCE INTERVAL (misunderstood):
  "95% CI" means:
  If we repeated this procedure on 100 different samples from the same population,
  ~95 of those CIs would contain the true parameter
  It does NOT mean: "95% probability the true value is in THIS interval"
  → The true value is fixed; it either is or isn't in the interval
  → The procedure has 95% coverage; any single CI is not "95% probable"

P-VALUE (misunderstood):
  p = P(observed test statistic or more extreme | H₀ is true)
  IT IS NOT:
  • P(H₀ is true given data) — that would be Bayesian
  • P(effect is real)
  • Probability the result is "due to chance"
  → p is the probability of data, not of hypotheses

NEYMAN-PEARSON vs FISHER:
  Fisher: p-value as measure of evidence against H₀ (continuous measure)
  Neyman-Pearson: binary decision rule (accept/reject H₀) with fixed α, β
  The modern practice muddles both: declare "significance" (Neyman-Pearson language)
  using a p-value threshold (Fisher language) that was never intended as decision boundary
  → ASA Statement on p-values (2016): "Do not base conclusions solely on p<0.05"
  → "Moving to a World Beyond p<0.05" (2019 supplement): "retire statistical significance"

+------------------+---------------------------------------------+
| FREQUENTIST WINS | Regulatory/confirmatory settings (FDA, ICH) |
|                  | Type I error control pre-specified          |
|                  | Repeated-use procedures (quality control)   |
+------------------+---------------------------------------------+

BAYESIAN:

PHILOSOPHICAL STANCE:
  Parameters (θ) have probability distributions (degree-of-belief)
  Prior p(θ): belief about θ before seeing data
  Likelihood p(X|θ): probability of data given parameter
  Posterior p(θ|X) ∝ p(X|θ) × p(θ): updated belief after data

  BAYES' THEOREM:
  p(θ|X) = [p(X|θ) × p(θ)] / p(X)
  Posterior ∝ Likelihood × Prior

CREDIBLE INTERVAL:
  "95% credible interval" means:
  Given the data and prior, there is 95% probability that θ is in this range
  → This IS the statement people mistakenly attribute to frequentist CIs
  → Genuine probability statement about the parameter (given prior + data)

+------------------+---------------------------------------------+
| BAYESIAN WINS    | Decision under uncertainty (expected utility)|
|                  | Hierarchical models (partial pooling)       |
|                  | Sequential updating (clinical adaptive)     |
|                  | Small samples + domain knowledge            |
|                  | Communicating uncertainty to stakeholders    |
+------------------+---------------------------------------------+
```

---

## Estimands (ICH E9(R1))

```
THE ESTIMAND FRAMEWORK:

Problem: "average treatment effect" sounds unambiguous but isn't.
What population? What happens to intercurrent events?
(Intercurrent events: events after randomization that affect interpretation)

ESTIMAND = the treatment effect you actually want to estimate
ESTIMATOR = the statistical procedure used to estimate it
ESTIMATE = the specific number from that analysis

FIVE STRATEGIES FOR INTERCURRENT EVENTS (ICH E9(R1)):

  1. TREATMENT POLICY:
     Ignore the intercurrent event; analyze all outcomes regardless
     Example: patient switches to rescue medication → include their outcome anyway
     "What is the effect of being assigned treatment X, regardless of what else happens?"

  2. HYPOTHETICAL:
     What if the intercurrent event had not occurred?
     Example: what if no one had discontinued? (counterfactual)
     Requires assumptions about counterfactual outcomes

  3. COMPOSITE:
     Intercurrent event IS part of the outcome
     Example: discontinuation = treatment failure → count as bad outcome
     Requires clinical judgment about what "failure" means

  4. WHILE ON TREATMENT:
     Outcome is only the period while on assigned treatment
     Example: analyze only on-treatment days

  5. PRINCIPAL STRATUM:
     Restrict to subgroup of patients who would not have had the intercurrent event
     Example: complier average causal effect (CACE)

WHY ESTIMANDS MATTER:
  Study A: "treatment reduces pain" (while-on-treatment estimand)
  Study B: "treatment reduces pain" (treatment policy estimand)
  Same trial, different answer, for legitimate reasons
  → Meta-analysis combining them is problematic
  → Pre-specify the estimand before collecting data
```

---

## Identification vs Estimation

```
IDENTIFICATION:
  Question: CAN the causal effect be recovered from observational data in principle?
  (Before thinking about sample size or statistics)

  Requires: assumptions about the data-generating process (the causal structure)
  Tool: DAG (Directed Acyclic Graph) — draw the causal structure

  Example:
  Q: Does education cause higher wages?
  DAG: Education ← Ability → Wages; Education → Wages
  Problem: Ability is an unobserved confounder (Ability → both Education and Wages)
  → OLS of Wage ~ Education is BIASED (education picks up ability effect)
  → Need: instrument for education (affects education but not wages directly)
  → Or: control for ability (but it's unobserved)

  Identification strategies: RCT, IV, RDD, DiD, Synthetic Control
  Each relies on a different set of assumptions
  These assumptions are UNTESTABLE (by definition — if testable, you'd need another assumption)
  But some are MORE PLAUSIBLE than others given context

ESTIMATION:
  Given identified causal effect, how to estimate it efficiently?
  OLS, IV, IPW, doubly-robust estimators, machine learning (DML)
  Finite-sample concerns: variance, bias-variance tradeoff
  Standard errors: heteroskedasticity-robust, cluster-robust, bootstrap

THE ORDER MATTERS:
  1. Specify the estimand
  2. Argue identification (causal structure + assumption)
  3. Choose estimator
  4. Report estimate with uncertainty
  Skipping step 2 (going from data → estimate without causal argument)
  produces correlations, not causal effects, regardless of statistical sophistication
```

---

## Common Errors in Empirical Work

```
HARKing (Hypothesizing After Results are Known):
  Run analysis → find what's significant → write paper claiming that was the hypothesis
  Result: published findings with massively inflated false positive rates
  Fix: pre-registration (write hypothesis + analysis plan BEFORE seeing data)
  OSF (Open Science Framework), AEA Trial Registry, ClinicalTrials.gov

P-HACKING / RESEARCHER DEGREES OF FREEDOM:
  Optional stopping: check p-value repeatedly, stop when p<0.05
  Multiple endpoints: test 10 outcomes, report only the significant one
  Flexible covariates: add/remove controls until p<0.05
  Subsetting: analyze all subgroups until one is significant
  → Each flexibility doubles the false positive rate
  → A study with 20 researcher degrees of freedom and p<0.05 threshold:
    expected false positive rate can exceed 60%
  Fix: pre-registration, multiple comparison correction, sequential testing methods

UNDERPOWERED STUDIES:
  Powered at 20-50% for realistic effect sizes (very common in psychology, medicine)
  → Most published effects are exaggerated (winner's curse)
  → Small samples produce noisy estimates; only large (exaggerated) effects clear the threshold
  → Even "replicated" findings from underpowered studies are unreliable
  Fix: a priori power analysis; target 80-90% power at realistic (not optimistic) MDE

SIMPSON'S PARADOX:
  Trend in each subgroup reverses when groups are combined
  Example: drug appears better overall; but worse in both young and old patients
  Reason: confounding by age (old patients get drug more AND have worse outcomes)
  Fix: stratify by confounders before combining; causal analysis of the DAG

OVERFITTING:
  In-sample fit ↑ with complexity; out-of-sample performance ↓
  p-value on individual coefficient: not a model selection criterion
  Fix: cross-validation, held-out test sets, information criteria (AIC/BIC/LOO-CV)
```

---

## Module Map

```
statistics-applied/
├── 00-OVERVIEW.md           ← you are here
├── 01-EXPERIMENTAL-DESIGN.md  RCT, power, factorial, blocking, adaptive
├── 02-AB-TESTING.md            Online experiments, CUPED, SRM, bandits
├── 03-QUASI-EXPERIMENTAL.md    DiD, RDD, IV, synthetic control, event study
├── 04-BAYESIAN-PRACTICE.md     Stan/PyMC, MCMC, credible intervals, hierarchical
└── 05-RELIABILITY-SPC.md       Weibull, bathtub curve, control charts, Cpk

COMPLEMENTS:
  mathematics/20-STATISTICS — statistical theory (probability, inference, asymptotic)
  data-science/13-CAUSAL-INFERENCE — causal ML (DML, causal forests, CATE estimation)
  This directory — the practice: experimental design, A/B infrastructure, tools
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What does a 95% CI actually mean? | If we repeated this sampling procedure many times, ~95% of computed CIs would contain the true parameter. NOT "95% probability the true value is here." |
| What does p=0.03 actually mean? | P(data this extreme or more extreme | H₀ is true) = 0.03. Not: probability H₀ is true = 3%. Not: 97% chance the effect is real. |
| Frequentist vs Bayesian — when to use which? | Frequentist: pre-specified type I error control, regulatory, repeated-use procedures. Bayesian: decision under uncertainty, hierarchical models, sequential updating, small samples with domain knowledge. |
| What is Pearl's rung 2? | Interventional distribution: P(Y\|do(X)) — what happens when you actively set X. Distinct from P(Y\|X) (observation). Requires randomization or causal identification assumption. |
| What is an estimand? | The specific treatment effect you want to estimate — defined by the target population and the strategy for handling intercurrent events. Precedes choice of estimator. |
| What is HARKing? | Hypothesizing After Results are Known — writing a hypothesis to match the significant finding. Inflates false positive rates dramatically. Fixed by pre-registration. |

---

## Common Confusion Points

**Statistical significance ≠ practical significance:** p=0.001 on a tiny effect in a huge sample means nothing practically. p=0.08 on a large effect in a small sample may be practically important. Effect size (Cohen's d, OR, NNT) is always more informative than the p-value for practical decisions.

**Replication crisis implications:** Psychology (~50% replication), medicine, economics — all have substantial published literatures that don't replicate. The cause: underpowered studies + p-hacking + publication bias. Use these bodies of literature with appropriate skepticism; effect sizes are likely inflated.

**Causal inference is not magic:** All methods for getting rung 2 from rung 1 data require ASSUMPTIONS. RDD requires continuity at threshold. IV requires exclusion restriction. DiD requires parallel trends. These are untestable. The methods don't "solve" confounding; they reframe which assumption you're betting on.

**Pre-registration doesn't prevent learning from data:** Pre-registration specifies the primary analysis. Post-hoc exploratory analyses are still valid — just labeled "exploratory." The distinction is between confirmatory (pre-registered, strict type I error) and exploratory (hypothesis-generating, not inferentially valid alone).
