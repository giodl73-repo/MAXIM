# Statistical Inference

## The Big Picture

Statistical inference is the inversion of probability: given data, recover the generating model.

```
+------------------------------------------------------------------+
|                STATISTICAL INFERENCE FRAMEWORK                   |
+------------------------------------------------------------------+
|                                                                  |
|  DATA                                                            |
|  X_1, ..., X_n  ~  P_theta   (i.i.d., parametric model)        |
|                                                                  |
|  GOAL: Recover theta (or something about theta) from X_1,...,X_n |
|                                                                  |
|  TASKS:                                                          |
|  +-----------------+  +------------------+  +-----------------+ |
|  | ESTIMATION      |  | HYPOTHESIS TEST  |  | CONFIDENCE SETS | |
|  | theta_hat = ?   |  | H0: theta=theta0 |  | CI contains     | |
|  | MLE, MOM, etc.  |  | vs H1: theta!=0  |  | theta with 95%  | |
|  +-----------------+  +------------------+  +-----------------+ |
|                                                                  |
|  ESTIMATOR PROPERTIES:                                          |
|  Consistency:   theta_hat -> theta in probability               |
|  Unbiasedness:  E[theta_hat] = theta                            |
|  Efficiency:    achieves Cramer-Rao lower bound                 |
|  Robustness:    insensitive to model misspecification           |
+------------------------------------------------------------------+
```

---

## Maximum Likelihood Estimation

MLE is the dominant estimation framework. It selects the parameter value that makes the observed data most probable.

**Definition**:

```
  L(theta; x_1,...,x_n) = Product_{i=1}^n p(x_i; theta)
                         (likelihood function)

  l(theta) = log L(theta) = Sum_{i=1}^n log p(x_i; theta)
             (log-likelihood: sums are easier than products)

  MLE: theta_hat = argmax_theta l(theta)

  First-order conditions (score equations):
  d/d_theta l(theta) = Sum_i s(x_i; theta) = 0
  Where s(x; theta) = d/d_theta log p(x; theta) is the score function.
```

**MLE for exponential families** is particularly clean:

```
  p(x | theta) = h(x) exp(eta(theta)^T T(x) - A(theta))

  Score equation: dA/d_eta = (1/n) Sum T(x_i)

  The MLE sets the EXPECTED sufficient statistic equal to the
  OBSERVED sufficient statistic.

  Example: Normal(mu, sigma^2) with both unknown:
  mu_hat = x_bar,  sigma_hat^2 = (1/n) Sum (x_i - x_bar)^2
  (Note: sigma_hat^2 is biased; divide by n-1 for unbiased s^2)
```

**Asymptotic properties of MLE** (under regularity conditions):

```
  1. CONSISTENCY: theta_hat -> theta_0 in probability  (MLE converges)

  2. ASYMPTOTIC NORMALITY:
     sqrt(n)(theta_hat - theta_0)  --d-->  Normal(0, I(theta_0)^{-1})

     Where I(theta) = -E[d^2/d_theta^2 log p(X; theta)]
     is the Fisher information matrix.

  3. EFFICIENCY: MLE achieves the Cramer-Rao lower bound asymptotically.
     No consistent estimator can have smaller asymptotic variance.
```

---

## Fisher Information and Cramer-Rao Bound

**Fisher information**: Measures the amount of information about theta in a single observation X.

```
  Scalar theta:
  I(theta) = E[(d/d_theta log p(X; theta))^2]
           = -E[d^2/d_theta^2 log p(X; theta)]
           = Var[score]

  Matrix theta:
  I(theta)_{ij} = E[partial_i log p * partial_j log p]
                = -E[partial_i partial_j log p]
```

**Cramer-Rao Lower Bound**:

```
  For any UNBIASED estimator theta_hat of theta:
  Var(theta_hat) >= 1 / (n * I(theta))

  Matrix version:
  Cov(theta_hat) - (n I(theta))^{-1}  is positive semidefinite

  An estimator achieving equality is called EFFICIENT.
  The MLE is asymptotically efficient (achieves CRLB as n -> inf).
```

The CRLB is the fundamental precision limit for unbiased estimation — analogous to the Heisenberg uncertainty principle but for statistics.

---

## Method of Moments

Simpler than MLE; less efficient but robust and closed-form:

```
  Population k-th moment: mu_k(theta) = E_theta[X^k]
  Sample k-th moment:     m_k = (1/n) Sum x_i^k

  MOM estimator: solve mu_k(theta) = m_k for k = 1, ..., dim(theta)

  Example: Gamma(alpha, beta) with E[X] = alpha/beta, E[X^2] = alpha(alpha+1)/beta^2
  m_1 = alpha/beta  =>  alpha_hat = m_1^2 / (m_2 - m_1^2)
  m_2 = alpha(alpha+1)/beta^2  =>  beta_hat = m_1 / (m_2 - m_1^2)

  MOM is consistent (by LLN) but not necessarily asymptotically efficient.
```

**Generalized Method of Moments (GMM)**: Uses more moment conditions than parameters and minimizes a weighted quadratic form. Handles models where the full likelihood is intractable but moment conditions are available. Common in econometrics.

---

## Sufficient Statistics

A statistic T(X) is **sufficient** for theta if the conditional distribution of X given T(X) does not depend on theta.

```
  Fisher-Neyman Factorization Theorem:
  T(X) is sufficient  <=>
  L(theta; x) = g(T(x), theta) * h(x)

  (Likelihood factors into a function of T and theta, and a function of x alone)

  Examples:
  Normal(mu, sigma^2 known): T(x) = Sum x_i  (or equivalently x_bar)
  Poisson(lambda): T(x_1,...,x_n) = Sum x_i
  Bernoulli(p): T(x_1,...,x_n) = Sum x_i
  Uniform(0, theta): T(x_1,...,x_n) = max(x_i)
```

**Minimal sufficient statistic**: The coarsest sufficient statistic — contains exactly the information about theta in the data, nothing more.

**Complete sufficient statistics + Rao-Blackwell theorem**: If T is sufficient and theta_hat is any unbiased estimator, then E[theta_hat | T] is an unbiased estimator with Var <= Var(theta_hat). Conditioning on a sufficient statistic improves or maintains efficiency.

---

## Hypothesis Testing

**Setup**:

```
  H_0 (null hypothesis): theta in Theta_0
  H_1 (alternative):     theta in Theta_1

  Test: A decision rule that maps data to {Reject H_0, Fail to Reject H_0}

  TYPE I ERROR (alpha): P(Reject H_0 | H_0 true)   (false positive)
  TYPE II ERROR (beta): P(Fail to reject H_0 | H_1 true) (false negative)
  POWER = 1 - beta = P(Reject H_0 | H_0 false)

  SIZE: test has size alpha if P(reject | H_0) <= alpha for all theta in Theta_0
  LEVEL alpha: size <= alpha
```

**p-value**:

```
  p = P(test statistic at least as extreme | H_0 true)

  If p < alpha, reject H_0 at level alpha.

  p is a random variable with Uniform(0,1) distribution under H_0.
  Under H_1, p concentrates near 0.

  p-value is NOT:
  - P(H_0 is true | data)
  - The probability that you made a mistake
  - 1 - probability the result is real
```

**Neyman-Pearson Lemma**: For simple H_0 vs. simple H_1, the most powerful test of size alpha is the likelihood ratio test:

```
  Reject H_0 if  Lambda(x) = p(x | theta_1) / p(x | theta_0)  >  c_alpha

  This is optimal: no test with the same size has greater power.
```

---

## Common Test Statistics

```
  Z-TEST (known variance):
  Z = (X_bar - mu_0) / (sigma / sqrt(n))  ~  Normal(0,1) under H_0
  Use when n is large or sigma known.

  t-TEST (unknown variance):
  T = (X_bar - mu_0) / (S / sqrt(n))  ~  t_{n-1} under H_0
  S = sample std dev.  Use for small n with Normal data.

  TWO-SAMPLE t-TEST:
  T = (X_bar - Y_bar) / SE   ~  t_nu
  Tests if two population means differ.

  CHI-SQUARED TEST (goodness of fit):
  Q = Sum (O_i - E_i)^2 / E_i  ~  chi^2_{k-1} under H_0
  Tests if observed counts fit expected distribution.

  LIKELIHOOD RATIO TEST:
  Lambda = -2 log [L(theta_0) / L(theta_hat)]  ~  chi^2_d  under H_0
  d = dim(Theta_1) - dim(Theta_0) = number of constraints.
  Wilks' theorem: valid asymptotically.

  F-TEST (comparing variances or nested regression models):
  F = (RSS_0 - RSS_1)/q / (RSS_1/(n-p))  ~  F_{q, n-p}  under H_0
```

---

## Confidence Intervals

A 95% confidence interval [L(X), U(X)] satisfies:

```
  P(L(X) <= theta <= U(X)) >= 0.95   for all theta

  The interval is random; theta is fixed.
  95% of such intervals (from repeated experiments) contain theta.

  Construction via pivoting:
  If (X_bar - mu) / (S/sqrt(n)) ~ t_{n-1}, then:
  X_bar +/- t_{n-1, 0.025} * S/sqrt(n)  is a 95% CI for mu.

  Duality: CI and hypothesis test are two sides of the same coin.
  theta_0 in CI  <=>  H_0: theta = theta_0 not rejected at level alpha.
```

**Wald, score, and likelihood-ratio intervals**:

```
  WALD:           theta_hat +/- z_{alpha/2} * SE(theta_hat)
                  Easy but poor coverage for small n.

  SCORE (Wilson for proportions):
                  Inverts the score test
                  Better coverage properties near boundaries

  LIKELIHOOD RATIO:
                  {theta: -2 log L(theta) <= chi^2_{1,alpha}}
                  Profile likelihood intervals for complex models
```

---

## Multiple Testing

When testing m hypotheses simultaneously, the type I error rate inflates:

```
  If all H_0i are true and each test has level alpha:
  P(at least one false rejection) = 1 - (1-alpha)^m  ->  1 as m grows

  Example: m=100, alpha=0.05:  P(at least one false rejection) ≈ 0.994

  CORRECTIONS:
  Bonferroni: use alpha/m per test.  Controls FWER (family-wise error rate).
              Conservative; valid for any dependence structure.

  Benjamini-Hochberg: control FDR (false discovery rate = E[FP / max(R, 1)])
              Sort p-values: p_(1) <= ... <= p_(m).
              Reject H_0(k) for all k <= max{k: p_(k) <= k*q/m}.
              Less conservative than Bonferroni; controls expected proportion of false discoveries.

  Bonferroni is for: "I don't want any false positives."
  BH is for: "I expect some false positives; I want the proportion bounded."
```

<!-- @editor[content/P2]: Multiple testing section covers Bonferroni and BH but is missing: Holm-Bonferroni (uniformly more powerful than Bonferroni, always preferred), Storey's q-value (FDR estimation using empirical null distribution), and the modern resampling-based approaches (Westfall-Young permutation correction for dependent tests). Also missing the distinction between FWER and FDR for different scientific contexts (drug trials vs. genomics). Worth extending for a learner who will encounter multiple testing in ML model selection contexts. -->

---

<!-- @editor[content/P1]: Bootstrap and resampling are completely absent — this is an explicit gap in the learner calibration ("DOES need: bootstrap and resampling"). The bootstrap (Efron 1979) is the dominant modern tool for confidence intervals without distributional assumptions, and connects directly to this learner's interest in non-parametric inference. Missing: nonparametric bootstrap, parametric bootstrap, block bootstrap for dependent data, bootstrap confidence intervals (percentile, BCa, studentized), and the theoretical justification (bootstrap consistency). This is P1 — it is explicitly called out as needed and is absent. -->

## Efficiency, Robustness, and Misspecification

**Efficiency**: How close an estimator is to the Cramer-Rao bound. MLE is efficient asymptotically for correctly-specified models.

**Robustness**: Performance under model misspecification. MLE can fail badly if the assumed distribution is wrong. Robust alternatives:

```
  M-estimators: theta_hat = argmin Sum rho(x_i, theta)
  For squared error: rho = (x-mu)^2 -> mean
  For absolute error: rho = |x-mu| -> median (breakdown point 50%)
  For Huber loss: quadratic near 0, linear in tails -> bounded influence

  Breakdown point: fraction of contaminated observations before
  the estimator can take arbitrarily bad values.
  Sample mean: breakdown point 0% (one outlier -> unbounded bias)
  Median: breakdown point 50% (need majority contamination)
```

**Quasi-likelihood**: Use MLE estimating equations even when the full distribution is not specified, requiring only correct mean specification. Gives consistent estimators under mean misspecification; standard errors require sandwich estimator.

---

## Decision Cheat Sheet

| Goal | Method | Notes |
|---|---|---|
| Point estimation, likelihood known | MLE | Asymptotically efficient |
| Point estimation, likelihood intractable | GMM, M-estimation | Moment-based |
| Test simple vs. simple hypothesis | Likelihood ratio test | Neyman-Pearson optimal |
| Test composite hypothesis | LRT, score test, Wald test | Asymptotically chi-squared |
| Interval estimation | Confidence interval (pivot or LR) | Exact or approximate |
| Multiple testing, few false positives | Bonferroni | FWER control, conservative |
| Multiple testing, many tests (genomics) | Benjamini-Hochberg | FDR control |
| Robust to outliers | Median, M-estimators, Huber | Reduces efficiency |

---

## Common Confusion Points

**"The MLE is always unbiased."**
No. The Normal variance MLE sigma_hat^2 = (1/n) Sum (x_i - x_bar)^2 is biased by a factor of (n-1)/n. Bias is traded off for other properties (consistency, efficiency). For small n, bias-corrected estimators may be preferred.

**"A large p-value supports the null hypothesis."**
A large p-value means the data are not surprising under H_0. It does not mean H_0 is likely true. The test may simply lack power. "Absence of evidence is not evidence of absence" — this is the type II error.

**"The confidence interval is the plausible range for theta."**
This is the Bayesian credible interval interpretation. The frequentist CI is not a statement about the probability that theta is in a particular realized interval — theta either is or isn't in [L, U]. The 95% refers to the long-run procedure, not the specific interval you computed.

**"MLE requires the model to be correct."**
MLE under misspecification converges to the value that minimizes KL divergence from the true distribution to the model family — the "best approximation" within the model class. This is the Kullback-Leibler projection and can be useful even under misspecification.
