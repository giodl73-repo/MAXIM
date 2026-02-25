# Probability & Statistics — Landscape Overview

## The Big Picture

Two disciplines sharing notation but answering different questions:

```
+------------------------------------------------------------------+
|              PROBABILITY & STATISTICS LANDSCAPE                   |
+------------------------------------------------------------------+
|                                                                  |
|  PROBABILITY THEORY              STATISTICAL INFERENCE           |
|  (deductive)                     (inductive)                     |
|  +-----------------------+       +-----------------------+       |
|  | Given a model,        |       | Given data,           |       |
|  | what data should      |       | what model explains   |       |
|  | we expect?            |       | it?                   |       |
|  +-----------------------+       +-----------------------+       |
|          |                               |                       |
|          v                               v                       |
|  Measure theory foundation      Frequentist vs. Bayesian        |
|  (rigorous)                     (philosophical split)           |
|                                                                  |
|  STOCHASTIC PROCESSES           INFORMATION GEOMETRY             |
|  +-----------------------+       +-----------------------+       |
|  | Systems evolving      |       | Statistical manifolds,|       |
|  | under randomness      |       | Fisher metric, KL     |       |
|  | Markov, Brownian,     |       | divergence as         |       |
|  | martingales           |       | geometry              |       |
|  +-----------------------+       +-----------------------+       |
|                                                                  |
+------------------------------------------------------------------+
|                    CONNECTS TO                                    |
|  information-theory/  mathematics/  data-science/  physics/     |
+------------------------------------------------------------------+
```

---

## The Two Schools of Statistical Inference

This is the most important conceptual fork in the field. Both schools are mathematically valid; they answer different questions.

```
                    DATA x observed
                          |
          +---------------+---------------+
          |                               |
          v                               v
  FREQUENTIST                      BAYESIAN
  ----------                       -------
  Parameters theta are fixed,      Parameters theta are random
  unknown constants.               variables with a prior.
  Data is random.                  Data updates beliefs.
          |                               |
          v                               v
  P(X | theta)                     P(theta | X) ~ P(X|theta) P(theta)
  Likelihood only.                 Posterior ~ Likelihood x Prior.
          |                               |
          v                               v
  Answer: "95% CI means            Answer: "P(theta in [a,b] | data)
  95% of such intervals            = 0.95" -- a direct
  contain theta." Weird.           probability statement.
          |                               |
          v                               v
  MLE, hypothesis tests,           MCMC, variational inference,
  p-values, power analysis         model comparison via WAIC
```

**The philosophical disagreement**: Frequentists say probability is a long-run frequency — it only applies to repeatable events. Bayesians say probability is a degree of belief — it applies to any uncertainty, including one-off events.

---

## The Measure-Theoretic Foundation

Before 1933 (Kolmogorov's axiomatization), probability was informal. Kolmogorov grounded it in measure theory — the same framework used for Lebesgue integration.

```
  MEASURE THEORY                    PROBABILITY THEORY
  (from analysis)                   (Kolmogorov)
  +-----------------------+         +-----------------------+
  | Measurable space      |  maps   | Probability space     |
  | (Omega, F)            | ------> | (Omega, F, P)         |
  |                       |   to    |                       |
  | Measure mu: F->[0,inf)|         | Measure P: F -> [0,1] |
  | (total mass arbitrary)|         | (total mass = 1)      |
  +-----------------------+         +-----------------------+
           |                                  |
           v                                  v
  Measurable function               Random variable
  f: Omega -> R                     X: Omega -> R  (same thing)
           |                                  |
           v                                  v
  Integral f dmu (Lebesgue)         E[X] = Integral X dP
```

**The payoff**: Discrete and continuous distributions are unified. The expectation E[X] is a Lebesgue integral — no separate formulas for "sum over discrete" vs. "integrate over density."

---

## Module Map

```
  00-OVERVIEW (this file)
  |
  +-- 01-PROBABILITY-FOUNDATIONS    Measure-theoretic setup
  |   sigma-algebras, Kolmogorov axioms, measurability
  |
  +-- 02-RANDOM-VARIABLES           The workhorses
  |   distributions, moments, MGFs, characteristic functions
  |   common families: Normal, Poisson, Exponential, etc.
  |
  +-- 03-LIMIT-THEOREMS             Why the machinery pays off
  |   LLN (weak/strong), CLT, Slutsky, Delta method
  |   connection to algorithm average-case analysis
  |
  +-- 04-STOCHASTIC-PROCESSES       Adding time
  |   Markov chains, Brownian motion, martingales
  |   Poisson processes, Ito calculus intro
  |
  +-- 05-STATISTICAL-INFERENCE      Classical statistics
  |   MLE, method of moments, hypothesis testing
  |   p-values, confidence intervals, power
  |
  +-- 06-BAYESIAN-STATISTICS        The Bayesian school
  |   Priors, posteriors, conjugacy, MCMC, HMC
  |   model selection: BIC, WAIC, Bayes factors
  |
  +-- 07-REGRESSION-MODELS          Core applied tool
  |   Linear models, GLMs, ridge/lasso, mixed effects
  |
  +-- 08-TIME-SERIES                Dependent data
  |   ARIMA, spectral analysis, state space, Kalman filter
  |
  +-- 09-INFORMATION-GEOMETRY       Where it gets beautiful
      Fisher information metric, statistical manifold
      KL divergence as geometry, natural gradient
```

---

## Key Connections to Other Library Directories

```
  information-theory/
    Entropy H(X) = -E[log P(X)]         (probability + logarithm)
    KL divergence D_KL(P||Q)            (covered deeply in 09)
    Mutual information I(X;Y)           (bridge between the two)

  mathematics/
    Measure theory                      (foundation for 01)
    Real analysis                       (needed for LLN proofs)
    Linear algebra                      (regression in 07)
    Topology                            (needed for 09's manifold)

  data-science/
    Distributions appear in ML          (Gaussian, categorical)
    MLE is how most ML models train     (01 -> 05 -> data-science)
    Bayesian networks, variational AE   (06 -> data-science)
    SGD convergence relies on LLN/CLT   (03 -> data-science)

  physics/
    Statistical mechanics               (entropy, partition functions)
    Quantum probability                 (density matrices)
    Stochastic ODEs / Langevin          (04 -> physics)
```

---

## Probability vs. Statistics: Division of Labor

| Question | Discipline | Example |
|----------|-----------|---------|
| If P(H)=0.6, what is P(7 heads in 10 flips)? | Probability | Binomial(10, 0.6) |
| I saw 7 heads in 10 flips — what is P(H)? | Statistics | MLE, CIs, Bayes |
| How does a random walk behave over time? | Stochastic processes | Brownian motion |
| Do patients on drug A live longer than drug B? | Statistical inference | Hypothesis test |
| What distribution best explains this data? | Model selection | Bayes factor, BIC |
| How does Fisher information constrain estimators? | Information geometry | Cramer-Rao bound |

---

## This Directory vs. statistics-applied/

The library also contains `statistics-applied/` (Social Sciences section) which covers:
- Experimental design and A/B testing
- Survey sampling methods
- Causal inference (Pearl's do-calculus, potential outcomes)
- Applied regression in social science contexts

**This directory** covers the **mathematical foundations**:
- Why probability spaces exist and what they formalize
- Convergence theorems and their proofs
- The geometry of the space of probability distributions

If you want to run an A/B test: `statistics-applied/`.
If you want to understand why the CLT works: this directory.

---

## Decision Cheat Sheet

| I need to... | See |
|---|---|
| Understand sigma-algebras and why they're necessary | 01-PROBABILITY-FOUNDATIONS |
| Know the common distributions and when to use each | 02-RANDOM-VARIABLES |
| Understand why averages converge and CLT applies | 03-LIMIT-THEOREMS |
| Model a system evolving randomly over time | 04-STOCHASTIC-PROCESSES |
| Compute MLEs and confidence intervals | 05-STATISTICAL-INFERENCE |
| Use MCMC or understand Bayesian model comparison | 06-BAYESIAN-STATISTICS |
| Fit a regression or regularized model | 07-REGRESSION-MODELS |
| Analyze time series data | 08-TIME-SERIES |
| Understand natural gradient and Fisher information | 09-INFORMATION-GEOMETRY |

---

## Common Confusion Points

**"Probability is just counting — measure theory is overkill."**
For finite sample spaces, yes. For continuous distributions, no. The paradoxes that motivated Kolmogorov (Bertrand paradox, Borel-Kolmogorov paradox) arise precisely without a rigorous foundation. The Bertrand paradox shows that "uniform distribution" on a continuous set is ill-defined without specifying the sigma-algebra.

**"A confidence interval means there is a 95% chance theta is inside."**
This is the Bayesian credible interval interpretation. The frequentist CI means: if you repeated the procedure many times, 95% of the resulting intervals would contain the true theta. The true theta is fixed; the interval is random.

**"p < 0.05 means the result is probably true."**
A p-value is P(data at least this extreme | H_0 true). It says nothing directly about P(H_0 | data) — that requires Bayes' theorem and a prior on hypotheses. This is the base rate fallacy at scale.

**"Bayesian statistics requires subjective priors, so it is not objective."**
Prior choice is a modeling decision encoding genuine structural constraints — parameters must be positive, effect sizes are rarely enormous. With sufficient data, the posterior concentrates near the truth regardless of the prior (Bernstein-von Mises theorem). Frequentist methods also make modeling choices (test statistics, distributional assumptions) that are equally subjective.
