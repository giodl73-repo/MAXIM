# Probability and Statistics — Bayes, Gauss, Pearson, Fisher, Kolmogorov, Wald

## The Problem: From Gambling to Inference to Decision

```
THE EVOLUTION OF PROBABILITY
==============================

ERA 1 — GAMBLING (1650–1800)
  Pascal + Fermat → expected value, combinatorics
  Bernoulli (Jakob) → law of large numbers, Bernoulli trials
  De Moivre → normal approximation to binomial
  Bayes → inverse probability (from effects to causes)
  Laplace → analytic probability, central limit theorem

ERA 2 — MEASUREMENT (1800–1900)
  Gauss → least squares, normal distribution as error model
  Quetelet → statistics applied to human populations
  Galton → regression to the mean, correlation
  Pearson → chi-square, correlation coefficient, biometrics

ERA 3 — MATHEMATICAL STATISTICS (1900–1950)
  Fisher → maximum likelihood, significance testing, design of experiments
  Student (Gosset) → t-distribution, small-sample statistics
  Neyman + Pearson (Egon) → hypothesis testing framework

ERA 4 — AXIOMATIZATION (1933)
  Kolmogorov → probability on measure spaces: the rigorous foundation
  Khinchin → laws of large numbers in full generality
  Cramér → mathematical statistics textbook (unified the field)

ERA 5 — DECISION THEORY (1940–1970)
  Wald → sequential analysis, statistical decision theory
  De Finetti → subjective probability, Dutch book arguments
  Savage → subjective expected utility (foundations of Bayesianism)
```

---

## Thomas Bayes (~1702–1761)

### Who He Was

English minister and amateur mathematician. Published no mathematics in his
lifetime. After his death, his friend Richard Price found a manuscript and
published it as "An Essay towards solving a Problem in the Doctrine of Chances"
(1763).

### The Contribution: Inverse Probability

**The Problem Bayes Solved**

```
BAYES'S PROBLEM
================

Ordinary probability (forward):
  "I know the bias of the coin. What's the probability of seeing k heads
   in n flips?" → Binomial distribution.

Bayes's problem (inverse):
  "I've seen k heads in n flips. What can I infer about the bias of the coin?"
  → This is reasoning from EFFECTS to CAUSES.

Bayes's theorem (stated by Bayes, proved by Laplace):
  P(θ | data) = P(data | θ) · P(θ) / P(data)

  P(θ):          PRIOR — what you believed about θ before seeing data
  P(data | θ):   LIKELIHOOD — probability of data given hypothesis θ
  P(θ | data):   POSTERIOR — updated belief after seeing data
  P(data):       NORMALIZING CONSTANT — ensures posterior sums to 1

Bayes's "theorem" is a trivial consequence of conditional probability:
  P(A|B) = P(B|A)P(A) / P(B)

The INSIGHT is using it for inference:
  treat the model parameter θ as a random variable with a prior,
  update it to a posterior using observed data.
```

**Why "Bayesian Statistics" Is a Worldview, Not Just a Theorem**

The Bayesian approach requires a prior P(θ). Frequentists objected: where does
the prior come from? Isn't it subjective? This philosophical dispute drove
statistics for 150 years. Modern practice: use both frameworks for different purposes.

```
BAYESIAN vs FREQUENTIST
========================

Frequentist:
  Parameters are fixed (unknown) constants.
  Only randomness is in the data.
  Probability = long-run frequency.
  p-value = P(data this extreme | H₀ true)

Bayesian:
  Parameters are random variables with distributions.
  Prior encodes previous knowledge/beliefs.
  Posterior = updated knowledge.
  Credible interval = interval containing θ with 95% posterior probability.

Modern machine learning: mostly Bayesian in structure.
  Deep learning: typically frequentist in fitting (SGD minimizes loss)
  Bayesian neural networks: explicitly put distributions on weights
  Gaussian processes: full Bayesian treatment of function space
  Variational inference: approximate Bayesian inference at scale
```

---

## Carl Friedrich Gauss — Statistics (See Also File 03)

### The Statistical Contribution

Gauss's statistical work was motivated by practical problems: astronomical
measurement with errors, geodesy (measuring the shape of the Earth).

**Method of Least Squares**

```
GAUSS'S LEAST SQUARES
======================

Problem: n measurements y₁, ..., yₙ of a quantity x with errors εᵢ.
  yᵢ = x + εᵢ

What is the best estimate of x?

Gauss (1795, published 1809): Choose x̂ to minimize Σᵢ (yᵢ - x̂)².
  Solution: x̂ = (1/n) Σ yᵢ = the sample mean.

Why is minimizing squared errors better than, say, absolute errors?
Gauss's answer: If errors are Gaussian, then the mean is the maximum
likelihood estimate. So least squares = maximum likelihood under Gaussian errors.

Gauss-Markov theorem: Under any distribution of errors (not just Gaussian),
  as long as errors have zero mean and constant variance,
  the least squares estimator is BLUE:
  Best Linear Unbiased Estimator.
  "Best" = minimum variance among all linear unbiased estimators.

This is why linear regression is defensible even when errors aren't Gaussian.
```

---

## Karl Pearson (1857–1936)

### Who He Was

British mathematician and statistician. Founded the first statistics department
(University College London). Applied Francis Galton's ideas to create
mathematical statistics as a discipline. Also a strong eugenicist — a reminder
that technical brilliance and moral failure coexist.

### The Contribution: Correlation, Chi-Square, and Biometrics

**Pearson's Correlation Coefficient**

```
PEARSON'S r
============

For two variables X and Y measured in n cases:

  r = Σ(xᵢ - x̄)(yᵢ - ȳ) / √[Σ(xᵢ - x̄)² · Σ(yᵢ - ȳ)²]

  r ∈ [-1, 1]
  r = 1:  perfect positive linear relationship
  r = 0:  no linear relationship
  r = -1: perfect negative linear relationship

This is the normalized inner product of the centered variables.
Geometrically: cos of the angle between the centered data vectors.

Important:
  r = 0 does NOT mean no relationship — only no LINEAR relationship.
  Y = X² has r ≈ 0 if X is symmetric around 0.
  Always plot the data. Anscombe's quartet makes this point.
```

**Chi-Square Test (1900)**

The chi-square test of goodness of fit: do observed frequencies match expected?

Χ² = Σᵢ (Oᵢ - Eᵢ)² / Eᵢ

Under the null hypothesis, Χ² follows a chi-square distribution with (k-1)
degrees of freedom. This is one of the most widely used hypothesis tests.

**Principal Component Analysis (PCA)**

Pearson (1901) introduced PCA as a method for finding the "principal axes"
of a cloud of points — the directions of maximum variance. This is now
the standard dimensionality reduction technique in data science and ML.

---

## Ronald Aylmer Fisher (1890–1962)

### Who He Was

British statistician and biologist. Made foundational contributions to statistics,
genetics, and evolutionary biology. His *Statistical Methods for Research Workers*
(1925) and *The Design of Experiments* (1935) defined 20th-century empirical science.
Also an influential eugenicist — again, technical and moral dissonance.

### The Contribution: The Entire Modern Statistical Method

**Maximum Likelihood Estimation**

```
MAXIMUM LIKELIHOOD
==================

Fisher (1912, systematized 1920s):
  Given data x₁,...,xₙ and a parametric model p(x|θ),
  choose θ̂ to maximize the likelihood:

  θ̂_MLE = argmax_θ L(θ) = argmax_θ ∏ᵢ p(xᵢ|θ)

  Equivalently, maximize log-likelihood: Σᵢ log p(xᵢ|θ)

WHY MLE?
  1. It is asymptotically unbiased: E[θ̂_MLE] → θ as n → ∞
  2. It achieves the Cramér-Rao lower bound (minimum variance asymptotically)
  3. Invariant under reparametrization: if θ̂ is MLE, so is g(θ̂)
  4. Consistent: θ̂ → θ in probability as n → ∞

MLE in machine learning:
  Cross-entropy loss = negative log-likelihood for classification.
  Minimizing cross-entropy = maximizing likelihood of correct labels.
  MSE loss = negative log-likelihood for Gaussian errors.
  So "training a neural network" = MLE over parameters.
```

**Analysis of Variance (ANOVA)**

Fisher developed ANOVA to analyze agricultural experiments (he worked at
Rothamsted Experimental Station). ANOVA decomposes the variance of a response
variable into components attributable to different factors.

The F-test (Fisher's F) tests whether group means differ significantly.
The F-distribution is named for him.

**p-values and Significance Testing**

Fisher introduced p-values as a measure of evidence against a null hypothesis.
The p-value = P(test statistic ≥ observed | H₀ true).

```
FISHER'S P-VALUE vs NEYMAN-PEARSON DECISION THEORY
====================================================

Fisher's view: p-value measures evidence.
  p < 0.05 is a useful threshold but not a mechanical rule.
  The data analyst uses judgment; p-value is one input.

Neyman-Pearson (Jerzy Neyman + Egon Pearson) view:
  Specify α (Type I error rate) and β (Type II error rate) in advance.
  Choose a decision rule with controlled error rates.
  No "evidence" — just decisions.

Modern practice: a confused hybrid.
  Scientists say "p < 0.05" as if it were a Neyman-Pearson decision
  but interpret it as Fisher's evidence.
  The American Statistical Association's 2016 statement warned about
  p-value misuse.

The "replication crisis" in psychology, medicine, and other fields
partly traces to misuse of p-values (fishing for significance,
optional stopping, multiple comparisons without correction).
```

**Design of Experiments**

Fisher's three principles:
1. **Replication**: Repeat experiments to estimate variability
2. **Randomization**: Randomly assign treatments to units (controls confounding)
3. **Blocking**: Group similar units together to reduce noise

These principles govern every clinical trial, A/B test, and agricultural
experiment since 1935. When you run an A/B test at Microsoft, you use
Fisher's design principles (randomization, replication, and controlling
for user-level blocking).

**Fisher Information and the Cramér-Rao Bound**

```
FISHER INFORMATION
==================

Fisher information I(θ) measures how much information data carries about θ:

  I(θ) = E[(∂/∂θ log p(X|θ))²]

Cramér-Rao bound:
  Var(θ̂) ≥ 1/I(θ)  for any unbiased estimator θ̂

  No unbiased estimator can have variance below 1/I(θ).
  The MLE achieves this bound asymptotically (it's efficient).

Fisher information matrix (multiparameter):
  I(θ)ᵢⱼ = E[∂²/∂θᵢ∂θⱼ (-log p(X|θ))]

The natural gradient in machine learning: SGD uses Euclidean gradient;
  natural gradient uses the inverse Fisher information matrix to
  preconditioning the gradient. This is what Adam/RMSprop approximate.
  Amari's information geometry formalizes this.
```

---

## Andrei Kolmogorov (1903–1987)

### Who He Was

Soviet mathematician, Moscow State University. Made contributions to:
probability theory (the rigorous foundations), complexity theory (Kolmogorov
complexity), turbulence theory, information theory, dynamical systems,
intuitionistic logic, and topology. One of the most broadly contributing
mathematicians of the 20th century.

### The Contribution: The Axiomatic Foundation of Probability

**Kolmogorov's Axioms (1933)**

```
KOLMOGOROV'S PROBABILITY AXIOMS
=================================

Before Kolmogorov: probability was computed by rules (frequency, symmetry)
  but not founded on rigorous mathematics. Series of paradoxes and disputes.

Kolmogorov (1933) — "Grundbegriffe der Wahrscheinlichkeitsrechnung":
  A probability space is a triple (Ω, ℱ, P) where:
    Ω = sample space (set of all outcomes)
    ℱ = σ-algebra of measurable events (subsets of Ω, closed under
        complement, countable union)
    P: ℱ → [0,1] satisfying:
      1. P(Ω) = 1
      2. P(A) ≥ 0 for all A ∈ ℱ
      3. Countable additivity: if A₁, A₂, ... are disjoint,
         P(∪ Aᵢ) = Σ P(Aᵢ)

Everything in probability follows from these three axioms.

WHY MEASURE THEORY:
  Discrete probability is easy (sum over outcomes).
  Continuous probability (probability density functions) needs integration.
  What is the "probability" of a specific real number? 0.
  But the probability of an interval is positive.
  Lebesgue measure theory (Lebesgue, 1902) handles this properly.
  Kolmogorov put probability on Lebesgue's foundations.
```

**Kolmogorov's Law of Large Numbers (Strong)**

If X₁, X₂, ... are iid with E[X] = μ, then P(lim_{n→∞} (X₁+...+Xₙ)/n = μ) = 1.

The average converges to the mean **almost surely** (with probability 1).
This is stronger than convergence in probability (the weak LLN of Bernoulli/Chebyshev).

**Kolmogorov Complexity**

```
KOLMOGOROV COMPLEXITY (1965)
==============================

The Kolmogorov complexity K(x) of a string x is:
  The length of the shortest program that outputs x and halts.

Intuition: How "random" or "structured" is a string?
  "000000000000000" has low K — a short program generates it.
  A truly random string has K ≈ its own length (no shorter description).

Key facts:
  - K(x) is not computable (follows from halting problem)
  - K(x) ≤ |x| + O(1) (you can always describe x by printing it)
  - Most strings of length n have K(x) ≈ n (most strings are "random")

Connection to Shannon entropy:
  Shannon entropy H(X) = expected K(X) up to a constant.
  Kolmogorov complexity is the ABSOLUTE information in a single string.
  Shannon entropy is the average information in a distribution.

Applications:
  - Theoretical foundation of data compression
  - Occam's razor formalized: the simplest explanation (shortest program)
  - MDL principle (Minimum Description Length) for model selection
  - Randomness tests: a "random" string has high K complexity
```

---

## Abraham Wald (1902–1950)

### Who He Was

Romanian-American statistician. Fled Nazi-occupied Austria to the US in 1938.
At Columbia's Statistical Research Group during WWII, developed sequential
analysis. Died in a plane crash in India in 1950.

### The Contribution: Sequential Analysis and Statistical Decision Theory

**Sequential Analysis and the WALD Equation**

Classic statistics: decide on sample size n in advance, then collect n observations.
Wald's insight: Why not decide as you go, stopping when you have enough evidence?

```
SEQUENTIAL ANALYSIS
====================

Sequential Probability Ratio Test (SPRT):
  At each observation, compute the likelihood ratio:
    Λₙ = P(data₁,...,dataₙ | H₁) / P(data₁,...,dataₙ | H₀)

  Decision rule:
    If Λₙ ≥ B (upper threshold): accept H₁, stop.
    If Λₙ ≤ A (lower threshold): accept H₀, stop.
    Otherwise: take one more observation.

WALD proved:
  This procedure controls both Type I and Type II error rates.
  On average, it uses FEWER observations than fixed-sample tests
  with the same error guarantees.

Why it matters now:
  - A/B tests in tech companies: sequential tests let you stop early
    when significance is clear or futility is apparent
  - Clinical trials: stopping rules for efficacy or harm
  - Anomaly detection in streaming data
  - Adaptive learning algorithms

Microsoft, Google, Amazon all use variants of Wald's sequential testing
for their A/B testing infrastructure (with modifications to control
for "peeking" problems).
```

**Statistical Decision Theory**

Wald's *Statistical Decision Functions* (1950) unified all of statistics
under a decision-theoretic framework:

```
WALD'S DECISION THEORY
=======================

A statistical problem:
  - Nature has a "state of the world" θ ∈ Θ (unknown parameter)
  - You observe data X
  - You must take action a ∈ A
  - Loss function L(θ, a) = how bad it is to take action a when truth is θ

A decision rule δ: X → A maps observations to actions.
Risk: R(θ, δ) = E_θ[L(θ, δ(X))] (expected loss under truth θ)

Key concepts:
  Admissibility: δ is admissible if no other rule is uniformly better
  Minimax: choose δ to minimize max_θ R(θ, δ) (worst-case optimal)
  Bayes: choose δ to minimize average risk under a prior π(θ)

Wald proved: Under regularity conditions,
  every admissible decision rule is a Bayes rule (for some prior).
  Bayes rules are complete — they cover all admissible procedures.

Connection to game theory: minimax = Nash equilibrium in a game
  between the statistician and "nature."
```

---

## Comparison Table

| Figure | Dates | Core Contribution | Framework | Still Used |
|--------|-------|-------------------|-----------|------------|
| **Bayes** | ~1702–1761 | Inverse probability | Prior → posterior | Bayesian inference, ML |
| **Gauss** | 1777–1855 | Normal distribution, least squares | Error model | Linear regression, Kalman filter |
| **Pearson** | 1857–1936 | Correlation, chi-square, PCA | Descriptive statistics | Every intro stats course |
| **Fisher** | 1890–1962 | MLE, ANOVA, experiment design, p-values | Frequentist inference | All scientific research |
| **Kolmogorov** | 1903–1987 | Probability axioms, complexity | Measure-theoretic | Mathematical probability, compression theory |
| **Wald** | 1902–1950 | Sequential analysis, decision theory | Decision-theoretic | A/B testing, clinical trials |

---

## Who to Cite for What

| Concept | Cite | Notes |
|---------|------|-------|
| Bayes' theorem | Bayes + Laplace | Bayes stated, Laplace proved and extended |
| Bayesian inference (prior → posterior) | Bayes + Laplace | Modern Bayesianism also Savage, de Finetti |
| Least squares | Gauss (Legendre) | Gauss developed first, Legendre published first |
| Normal distribution as error model | Gauss | Derived from MLE assumptions |
| Pearson correlation coefficient | Pearson | Named for him |
| Chi-square test | Pearson | 1900 |
| PCA | Pearson (1901) + Hotelling (1933) | Both contributed |
| Maximum likelihood | Fisher | Systematized 1912–1920s |
| p-value | Fisher | "Significance" level |
| ANOVA / F-test | Fisher | Agricultural experiments, generalized |
| Design of experiments (randomization) | Fisher | *Design of Experiments* 1935 |
| Fisher information / Cramér-Rao bound | Fisher + Cramér + Rao | |
| Probability axioms | Kolmogorov | *Grundbegriffe* 1933 |
| Kolmogorov complexity | Kolmogorov (+ Solomonoff, Chaitin) | 1965 |
| Sequential probability ratio test | Wald | 1947 |
| Statistical decision theory | Wald | *Statistical Decision Functions* 1950 |

---

## Common Confusion Points

**"p < 0.05 means there's a 95% chance the result is real"** — This is the most
common misinterpretation of p-values. A p-value of 0.05 means: IF the null hypothesis
is true, there would be a 5% chance of seeing data at least this extreme. It says
nothing about the probability of the hypothesis being true (that requires Bayes).

**"Bayesian statistics is subjective"** — The prior is chosen by the analyst,
which is subjective. But: (1) frequentist statistics has subjective choices too
(choice of test, significance level, stopping rule). (2) With enough data, the
posterior converges regardless of the prior. (3) Empirical Bayes estimates priors
from data itself. Subjectivity is a real concern, not a refutation.

**"Kolmogorov axioms say what probability IS"** — They don't. They define a
formal structure that probability must satisfy. The axioms say nothing about whether
probability represents frequencies (frequentist interpretation) or degrees of belief
(Bayesian). The interpretation debate is philosophical, not mathematical.

**"Wald's sequential tests are universally applicable"** — They require the
likelihood ratio to be computed, which needs a fully specified alternative hypothesis.
In modern A/B testing, modifications are needed to avoid the "peeking" problem:
if you check sequential results multiple times without a proper sequential test,
you inflate Type I error rates.

**"Pearson's correlation detects relationships"** — Pearson's r detects linear
relationships. Nonlinear relationships (quadratic, periodic) can give r ≈ 0 even
with strong dependence. Alternatives: Spearman's rank correlation (monotone
relationships), mutual information (any statistical dependence), distance correlation.
Always plot the data before trusting a correlation number.
