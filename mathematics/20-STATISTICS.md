# Statistics — Complete Reference

## The Big Picture

Statistics is the mathematical framework for making inferences from data under uncertainty. You know probability theory (from MIT) — this guide builds on that to cover **statistical inference** (estimation and hypothesis testing), **regression theory** (OLS → GLMs), **Bayesian methods**, and **resampling** (bootstrap/permutation). The bridge to ML is explicit throughout.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  STATISTICAL INFERENCE LANDSCAPE                                             │
│                                                                              │
│  Frequentist                          Bayesian                               │
│  ─────────────────────────────────    ──────────────────────────────────     │
│  Parameters are fixed, unknown        Parameters are random variables        │
│  Data is random (from sampling)       Prior + Likelihood → Posterior         │
│  Inference via sampling distributions p(θ|X) ∝ p(X|θ) · p(θ)               │
│  Confidence intervals: random, not θ  Credible intervals: about θ           │
│  p-values: P(data|H₀), not P(H₀|data) Natural probability statements        │
│                                                                              │
│  Point Estimation      Interval Estimation     Hypothesis Testing            │
│  ──────────────────    ─────────────────────   ─────────────────────         │
│  MLE, MOM              CI (Wald, exact, boot)  NHST, p-values               │
│  MAP (Bayesian)        Credible intervals      Bayes factors                 │
│  UMVUE (theory)        Prediction intervals    Multiple testing              │
│                                                                              │
│  Models                                                                      │
│  ─────────────────────────────────────────────────────────────────────       │
│  Linear regression (OLS) → Ridge/LASSO → GLMs (logistic/Poisson/Gamma)     │
│  Nonparametric (Mann-Whitney, KS, rank tests) → bootstrap equivalents       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Point Estimation

### Framework

Let X₁, ..., Xₙ ~ iid F_θ, θ ∈ Θ. An **estimator** is a function θ̂(X₁,...,Xₙ) of the data.

**Properties of estimators**:
```
Bias:       Bias(θ̂) = E[θ̂] - θ
Variance:   Var(θ̂) = E[(θ̂ - E[θ̂])²]
MSE:        MSE(θ̂) = Var(θ̂) + Bias(θ̂)²    [bias-variance decomposition]

Consistent: θ̂ →ₚ θ as n→∞ (convergence in probability)
Efficient:  achieves Cramér-Rao lower bound
```

### Method of Moments (MOM)

Equate population moments to sample moments. Solve for parameters.

```
Example: Gamma(α, β) distribution. E[X] = α/β, Var(X) = α/β².
  Sample moments: X̄, s²
  Solve: α/β = X̄, α/β² = s²
  → β̂ = X̄/s², α̂ = X̄²/s²

Simple, consistent, but usually not efficient (MLE is better).
```

### Maximum Likelihood Estimation (MLE)

```
L(θ; x₁,...,xₙ) = ∏ᵢ f(xᵢ; θ)    [likelihood = joint density at observed data]
ℓ(θ) = log L(θ) = Σᵢ log f(xᵢ; θ) [log-likelihood, easier to maximize]

MLE: θ̂_MLE = argmax_θ ℓ(θ)
```

**Properties of MLE** (large sample / regular models):
- Consistent: θ̂_MLE →ₚ θ₀
- Asymptotically normal: √n(θ̂_MLE - θ₀) →_d N(0, I(θ₀)⁻¹)
- Asymptotically efficient: achieves Cramér-Rao bound
- Equivariant: if θ̂ is MLE of θ, then g(θ̂) is MLE of g(θ)

**Fisher information**:
```
I(θ) = -E[∂²/∂θ² log f(X;θ)]       [for scalar θ]
     = E[(∂/∂θ log f(X;θ))²]        [equivalent form via score function]

Fisher information matrix (FIM) for vector θ:
I(θ)_{jk} = -E[∂²ℓ/∂θⱼ∂θₖ]

Observed FIM: use -(∂²ℓ/∂θ²)|_{θ=θ̂} (negative Hessian at MLE)
Standard errors: SE(θ̂_j) = √[I(θ̂)⁻¹]_{jj}
```

### Cramér-Rao Lower Bound

For any unbiased estimator θ̂ of θ:
```
Var(θ̂) ≥ 1/I(θ)    [scalar case]
Cov(θ̂) ≥ I(θ)⁻¹   [matrix inequality: Cov - I⁻¹ is positive semidefinite]
```

**UMVUE** (Uniformly Minimum Variance Unbiased Estimator): Achieves CRB for all θ. Found via Rao-Blackwell theorem (condition unbiased estimator on sufficient statistic) and Lehmann-Scheffé (complete sufficient statistic). Classic example: X̄ for N(μ,σ²) is UMVUE for μ.

**Completeness and sufficiency**:
- Sufficient statistic T(X): p(X|T(X), θ) independent of θ. T captures all information about θ.
- Complete statistic: E[g(T)] = 0 for all θ implies g = 0 a.e. Rules out other unbiased estimators.
- Exponential family members have complete sufficient statistics (natural parameters).

### MAP Estimation (Bayesian Point Estimate)

```
θ̂_MAP = argmax_θ p(θ|X) = argmax_θ [ℓ(θ) + log p(θ)]

MAP with Gaussian prior N(0, σ²_prior):
  log p(θ) = -θ²/(2σ²_prior) + const
  → MAP minimizes ℓ(θ) - ||θ||²/(2σ²_prior)  [negative log-likelihood + L2 penalty]
  → Ridge regression is MAP with Gaussian prior.

MAP with Laplace prior: L1 penalty → LASSO.
MLE = MAP with flat (improper uniform) prior.
```

---

## 2. Interval Estimation

### Confidence Intervals (Frequentist)

**Definition**: A 95% CI means: if we repeated the experiment many times and computed the CI each time, 95% of those intervals would contain the true θ. The interval is random; θ is fixed.

**Wald CI** (large sample):
```
θ̂ ± z_{α/2} · SE(θ̂)
where z_{α/2} = 1.96 for 95% CI (from N(0,1))
SE(θ̂) from observed Fisher information or standard formulas

Valid when √n(θ̂ - θ)/SE →_d N(0,1) (CLT applies)
Can have poor coverage for small n or when θ̂ near boundary.
```

**Exact CI** (when sampling distribution known):
- Normal mean: t-interval with t_{n-1} distribution when σ unknown
- Proportion: Clopper-Pearson (exact binomial); Wilson interval (better small-sample behavior)
- Variance: χ² interval

**t-distribution**: t = (X̄ - μ)/(S/√n) ~ t_{n-1}. Heavier tails than normal; accounts for estimating σ. Converges to N(0,1) as n→∞.

**Likelihood ratio CI**: Invert likelihood ratio test.
```
{θ: 2[ℓ(θ̂) - ℓ(θ)] ≤ χ²_{1,α}}
```
Better coverage than Wald for non-normal, curved likelihood.

### Bootstrap Confidence Intervals

When sampling distribution unknown or small sample:
```
1. Draw B bootstrap samples X*₁, ..., X*_B each of size n with replacement from data.
2. Compute θ̂* for each bootstrap sample.
3. Bootstrap distribution approximates sampling distribution of θ̂.

Types:
  Percentile CI:   [θ̂*_{(α/2)}, θ̂*_{(1-α/2)}]    [simple, biased]
  BC_a (bias-corrected accelerated): adjusts for bias and skewness.
    More accurate for non-symmetric sampling distributions.
  Studentized (bootstrap-t): best coverage but needs variance estimate.

B = 1000 typical, B = 10000 for publication CI.
```

### Prediction Intervals vs Confidence Intervals

```
CI for μ:      X̄ ± t_{n-1,α/2} · (s/√n)    [uncertainty about mean]
PI for X_{n+1}: X̄ ± t_{n-1,α/2} · s·√(1+1/n) [uncertainty about new observation]

PI is always wider than CI.
PI accounts for both:
  1. Uncertainty in μ (same as CI)
  2. Natural variability of individual observations around μ
```

---

## 3. Hypothesis Testing

### Neyman-Pearson Framework

```
Null hypothesis H₀, alternative H₁.
Test statistic T(X). Rejection region R.

Type I error (false positive): Reject H₀ when H₀ true.  Probability = α (level).
Type II error (false negative): Fail to reject when H₁ true. Probability = β.
Power: 1 - β = Pr(reject | H₁ true). Want high power.

p-value: P(T ≥ t_obs | H₀) = smallest α at which we would reject.
  p-value is NOT: P(H₀ | data). It's P(data as extreme | H₀).

Significance: p < 0.05 → reject at 5% level. Convention, not a law.
```

**Neyman-Pearson Lemma**: For simple H₀: θ=θ₀ vs simple H₁: θ=θ₁, the most powerful test of level α uses rejection region based on likelihood ratio:
```
Λ(x) = L(θ₁; x) / L(θ₀; x) > k
```
This is the UMP (Uniformly Most Powerful) test for simple hypotheses.

### Common Tests

| Test | Hypotheses | Statistic | Assumptions |
|------|-----------|-----------|-------------|
| One-sample t | H₀: μ = μ₀ | t = (X̄-μ₀)/(s/√n), df=n-1 | Normal or n large |
| Two-sample t | H₀: μ₁ = μ₂ | Welch t, df via Satterthwaite | Normal or n large |
| Paired t | H₀: μ_D = 0 | t on differences | Differences normal |
| One-prop z | H₀: p = p₀ | z = (p̂-p₀)/√(p₀(1-p₀)/n) | np₀ ≥ 5 |
| Two-prop z | H₀: p₁ = p₂ | z with pooled estimate | Large n |
| ANOVA (F-test) | H₀: all μ equal | F = MSB/MSW, df=(k-1,n-k) | Normal, equal variance |
| χ² goodness-of-fit | H₀: distribution is F₀ | Σ(O-E)²/E, df=k-1-params | Expected counts ≥ 5 |
| χ² independence | H₀: X⊥Y | Σ(O-E)²/E, df=(r-1)(c-1) | Expected counts ≥ 5 |

### Power Analysis and Sample Size

```
For two-sample t-test detecting effect size δ = μ₁ - μ₂:
  n = 2σ²(z_{α/2} + z_β)² / δ²  [approximate]

Effect size: Cohen's d = δ/σ. Small=0.2, medium=0.5, large=0.8.
Standard: α=0.05, power=0.80 → z_{α/2}=1.96, z_β=0.84
  → n ≈ 2(1.96+0.84)²/d² = 16/d²  [rough rule: 16/d² per group]

For d=0.5 (medium): n ≈ 64 per group.
For d=0.2 (small): n ≈ 400 per group.
```

### Multiple Testing Problem

**Family-wise error rate (FWER)**: P(any false rejection) → inflates as number of tests grows.

```
Bonferroni correction: use α' = α/m for m tests.
  Strict, conservative. Controls FWER.
  Power loss proportional to m (bad for large m).

Holm-Bonferroni (step-down Bonferroni): less conservative.
  Sort p-values p_(1) ≤ p_(2) ≤ ... ≤ p_(m).
  Reject p_(i) if p_(j) ≤ α/(m-j+1) for all j ≤ i.

Benjamini-Hochberg (FDR control): controls false discovery RATE, not FWER.
  Sort p-values. Reject p_(i) if p_(i) ≤ (i/m)·α.
  FDR = E[V/R | R > 0] ≤ α. V = false rejections, R = total rejections.
  Less conservative than Bonferroni. Standard in genomics (20,000 tests).
```

**Why p-hacking inflates false positive rate**: If you test 20 hypotheses at α=0.05 and all are null, you expect 1 false positive. Reporting only significant result → 100% false discovery rate.

---

## 4. Linear Regression

### OLS (Ordinary Least Squares)

```
Model: Y = Xβ + ε,  ε ~ N(0, σ²Iₙ)
X: n×p design matrix (n observations, p predictors including intercept)
β: p-vector of coefficients
Y: n-vector of responses

OLS estimator: β̂ = argmin ||Y - Xβ||²
  Solution: β̂ = (X'X)⁻¹X'Y   [normal equations: X'Xβ = X'Y]
  Fitted values: Ŷ = Hʏ where H = X(X'X)⁻¹X' [hat matrix, projection onto col(X)]
  Residuals: ê = Y - Ŷ = (I-H)Y
  σ̂² = ||ê||² / (n-p)   [unbiased estimator of σ²]
```

**Gauss-Markov theorem**: Under E[ε|X]=0, Var(ε|X)=σ²I, OLS is BLUE (Best Linear Unbiased Estimator). Best = minimum variance among all linear unbiased estimators.

**Inference**:
```
β̂ ~ N(β, σ²(X'X)⁻¹)   [exactly under normality assumption]
  → β̂_j ~ N(β_j, σ²[(X'X)⁻¹]_{jj})

t-statistic: t_j = β̂_j / (σ̂ · √[(X'X)⁻¹]_{jj}) ~ t_{n-p}
             under H₀: β_j = 0

F-statistic: tests all non-intercept coefficients simultaneously
             F = [(RSS₀ - RSS₁)/q] / [RSS₁/(n-p)] ~ F_{q, n-p}
             where RSS₀ = residual SS under null, q = restrictions.

R² = 1 - RSS/TSS = fraction of variance explained.
Adjusted R² = 1 - (RSS/(n-p)) / (TSS/(n-1)). Penalizes for extra parameters.
```

**Geometric interpretation**: OLS projects Y onto column space of X. β̂ is the coefficient vector for that projection. Residuals are orthogonal to col(X): X'ê = 0.

### OLS Assumptions and Diagnostics

```
A1: Linearity: E[Y|X] = Xβ. Diagnostic: residuals vs fitted (no pattern).
A2: Full rank: X'X invertible (no perfect multicollinearity).
    Diagnostic: VIF (Variance Inflation Factor) = 1/(1-R²_j) for regressor j.
    VIF > 10 → severe multicollinearity.
A3: Exogeneity: E[ε|X] = 0. Violated by omitted variables, endogeneity.
    Fix: instrumental variables (IV) regression.
A4: Homoskedasticity: Var(ε_i) = σ² constant.
    Diagnostic: Breusch-Pagan test, scale-location plot.
    Fix: robust (White's HC) standard errors, WLS.
A5: No autocorrelation: Cov(ε_i, ε_j) = 0 for i≠j.
    Diagnostic: Durbin-Watson test. Fix: GLS, HAC standard errors.
A6: Normality: ε ~ Normal. Only needed for finite-sample inference (t/F tests).
    Large n: CLT rescues inference without normality.
    Diagnostic: Q-Q plot, Shapiro-Wilk test.
```

**Robust standard errors** (Heteroskedasticity-Consistent, White 1980):
```
Var(β̂)_HC = (X'X)⁻¹ [Σᵢ ê²ᵢ xᵢxᵢ'] (X'X)⁻¹
Valid even when Var(εᵢ) ≠ σ² (heteroskedastic errors).
Use HC3 (small-sample corrected) as default. R: lm_robust(). Python: statsmodels with cov_type='HC3'.
```

### Regularized Regression

```
Ridge (L2 penalty): β̂_ridge = argmin ||Y - Xβ||² + λ||β||²
  Solution: β̂_ridge = (X'X + λI)⁻¹X'Y
  Shrinks all coefficients toward 0. No variable selection.
  MAP interpretation: Gaussian prior N(0, σ²/λ · I).
  Bias-variance tradeoff: λ↑ → bias↑, variance↓.

LASSO (L1 penalty): β̂_LASSO = argmin ||Y - Xβ||² + λ||β||₁
  No closed form. Solved via coordinate descent or LARS.
  Sparse solution: many coefficients exactly 0. → Feature selection.
  MAP interpretation: Laplace prior.

Elastic Net: λ₁||β||₁ + λ₂||β||² — combines LASSO sparsity with ridge stability.
  Best for correlated predictors (LASSO picks arbitrarily among correlated).

Cross-validation for λ: k-fold CV to choose λ minimizing out-of-sample error.
```

### Collinearity and Subset Selection

**Best subset selection**: O(2^p). Not practical for p > 30.

**Forward stepwise**: Add predictors one at a time by largest F-statistic. Greedy, O(p²).

**AIC/BIC model selection**:
```
AIC = 2p - 2ℓ(β̂)          [Akaike Information Criterion]
BIC = p·log(n) - 2ℓ(β̂)    [Bayesian IC — stronger penalty for large n]

Smaller is better. BIC more conservative (prefers fewer predictors).
AIC → asymptotically recovers true model if true model is complex (many params).
BIC → consistent: recovers true model if finite.
```

---

## 5. Generalized Linear Models (GLMs)

### Framework

GLMs extend OLS to non-Gaussian responses:
```
Components:
  1. Random component: Y ~ exponential family distribution
     Exponential family: f(y;θ) = exp[yθ - b(θ) + c(y,φ)]
     Mean: μ = b'(θ),  Variance: Var(Y) = φ·b''(θ)

  2. Systematic component: η = Xβ  [linear predictor]

  3. Link function: g(μ) = η, i.e., g(E[Y|X]) = Xβ
     Natural link: g(μ) = θ (canonical link)
```

| Distribution | Support | Link | Application |
|-------------|---------|------|-------------|
| Normal | ℝ | identity: μ = Xβ | Continuous outcome, OLS |
| Binomial | {0,...,n} | logit: log(μ/(1-μ)) = Xβ | Binary outcome |
| Poisson | {0,1,2,...} | log: log(μ) = Xβ | Count data |
| Gamma | (0,∞) | inverse: 1/μ = Xβ | Positive continuous |
| Inverse Gaussian | (0,∞) | 1/μ² = Xβ | Positive, right-skewed |

### Logistic Regression

```
P(Y=1|X) = σ(Xβ) = 1/(1 + e^{-Xβ})    [sigmoid function]
log-odds: log[P/(1-P)] = Xβ

Log-likelihood: ℓ(β) = Σᵢ [yᵢXᵢβ - log(1+e^{Xᵢβ})]
Concave in β → unique global maximum. No closed form → Newton-Raphson / IRLS.

Interpretation: exp(β_j) = odds ratio for unit increase in X_j.
  If β_j = 0.5: odds of Y=1 multiply by e^0.5 ≈ 1.65 per unit increase in X_j.

Fitted probabilities: p̂_i = σ(X_iβ̂).
Deviance = -2ℓ(β̂). Null deviance = -2ℓ(intercept only).
Likelihood ratio test: D₀ - D₁ ~ χ²_p under H₀: all slopes = 0.
Pseudo-R² (McFadden): 1 - ℓ(model)/ℓ(null). Ranges 0 to 1. 0.2-0.4 considered good.
```

### Estimation via IRLS (Iteratively Reweighted Least Squares)

GLMs fit via Newton-Raphson / Fisher scoring, equivalent to IRLS:
```
At iteration t:
  W_t = diag[Var(μ̂ᵢ)⁻¹ (∂μᵢ/∂ηᵢ)²]    [working weights]
  z_t = η̂ + W_t⁻¹(Y - μ̂)                [working response]
  β_{t+1} = (X'W_tX)⁻¹ X'W_tz_t         [WLS step]

Converges to MLE.
```

### Poisson Regression

```
log(E[Y|X]) = Xβ  → E[Y|X] = exp(Xβ)

Interpretation: exp(β_j) = multiplicative effect on expected count per unit X_j.
Offset: if exposure time tᵢ varies, use log(tᵢ) as fixed offset term.

Overdispersion: Var(Y) > E[Y] (data more variable than Poisson assumes).
  Check: deviance/df >> 1.
  Fixes: quasi-Poisson (scale dispersion parameter), Negative Binomial regression.
```

---

## 6. Nonparametric Tests

When distributional assumptions fail (non-normal data, small n):

| Parametric | Nonparametric equivalent | When |
|-----------|------------------------|------|
| One-sample t | Wilcoxon signed-rank | One sample, unknown distribution |
| Two-sample t | Mann-Whitney U (Wilcoxon rank-sum) | Two groups, unknown distribution |
| Paired t | Wilcoxon signed-rank on differences | Paired data, non-normal |
| One-way ANOVA | Kruskal-Wallis H | K groups, non-normal |
| Pearson correlation | Spearman ρ or Kendall τ | Monotone not linear relationship |
| — | Kolmogorov-Smirnov test | Test two distributions equal |
| — | Sign test | Median = m₀ |

**Mann-Whitney U**: Under H₀ that distributions F=G, test statistic = number of pairs (xᵢ, yⱼ) with xᵢ > yⱼ. Asymptotically normal. Tests stochastic dominance, not equality of means.

**KS test** (Kolmogorov-Smirnov): D = sup_x |F̂ₙ(x) - G(x)|. If G is continuous: √n·D →_d Kolmogorov distribution. Powerful for distribution differences in center; less powerful in tails.

**Bootstrap for nonparametric inference**:
```
Many nonparametric procedures are bootstrap-based:
  - No distributional assumption.
  - Resample with replacement from data.
  - Estimate SE, CI, p-value from bootstrap distribution.

Permutation test (exact nonparametric):
  - Under H₀: any group label assignment equally likely.
  - Compute test statistic for all (or random) permutations of labels.
  - p-value = fraction of permutations with statistic ≥ observed.
  - Exact: no asymptotic approximation needed.
```

---

## 7. Bayesian Inference

### Bayes' Theorem for Inference

```
p(θ|X) ∝ p(X|θ) · p(θ)
Posterior ∝ Likelihood × Prior

Summary statistics of posterior:
  Posterior mean:   ∫ θ · p(θ|X) dθ   [minimizes E[L] for L₂ loss]
  Posterior median: minimizes E[L] for L₁ loss
  MAP:              argmax p(θ|X)      [mode; L₀ loss]
  Credible interval: [a,b] with ∫_a^b p(θ|X) dθ = 0.95
```

**Credible interval vs Confidence interval**:
- CI: P(CI contains θ | θ) = 0.95. θ is fixed; CI is random.
- Credible interval: P(θ ∈ [a,b] | data) = 0.95. Direct probability statement about θ.

### Conjugate Priors

When prior and posterior are in the same family — closed-form posterior:

| Likelihood | Conjugate Prior | Posterior | Notes |
|-----------|----------------|-----------|-------|
| Binomial(n,p) | Beta(α,β) | Beta(α+k, β+n-k) | k = successes |
| Poisson(λ) | Gamma(α,β) | Gamma(α+Σxᵢ, β+n) | |
| Normal(μ,σ²) | Normal(μ₀,σ₀²) | Normal (updated) | σ² known |
| Normal(μ,σ²) | NIG(μ₀,κ,α,β) | NIG (updated) | μ,σ² both unknown |
| Multinomial(p) | Dirichlet(α) | Dirichlet(α+counts) | |
| Exponential(λ) | Gamma(α,β) | Gamma(α+n, β+Σxᵢ) | |

**Beta-Binomial posterior intuition**:
```
Prior: Beta(α,β) — interpret as α-1 pseudosuccessess, β-1 pseudofailures.
After k successes in n trials:
  Posterior: Beta(α+k, β+n-k)
  Posterior mean: (α+k)/(α+β+n)
  As n→∞: posterior mean → k/n = MLE (prior washed out)
  Effective sample size of prior: α+β.
```

### Hierarchical Models

```
θᵢ | μ, τ ~ N(μ, τ²)    [group-level: school, patient, etc.]
μ ~ N(μ₀, σ₀²)          [hyperprior]
τ ~ HalfCauchy(0, s)    [hyperprior]

Yᵢⱼ | θᵢ, σ ~ N(θᵢ, σ²) [observation level]

Partial pooling: estimates θᵢ shrunk toward grand mean μ.
  No pooling: estimate each group independently (high variance).
  Complete pooling: assume all θᵢ = μ (high bias).
  Partial pooling: Bayes optimal tradeoff.

Classic: Efron-Morris (1975) "Stein's paradox": estimating 7+ group means simultaneously,
  shrinkage estimators dominate MLE by MSE — James-Stein estimator.
```

### MCMC (Markov Chain Monte Carlo)

When posterior has no closed form:

```
Metropolis-Hastings:
  1. Propose θ* ~ q(·|θ_current)   [proposal distribution]
  2. Accept with probability min(1, [p(θ*)·q(θ|θ*)] / [p(θ)·q(θ*|θ)])
  3. θ_next = θ* if accepted, else θ_current.
  Converges to target p(θ|X) under mild conditions.

Gibbs sampling:
  When full conditional p(θ_j | θ_{-j}, X) easy to sample from.
  Cycle through each coordinate, sampling from full conditional.
  Special case of Metropolis (always accept).

HMC (Hamiltonian Monte Carlo):
  Introduce momentum p. Run Hamiltonian dynamics (position θ, momentum p).
  Leapfrog integrator. Samples θ with much lower autocorrelation than random walk.
  NUTS (No-U-Turn Sampler): auto-tuned HMC. Used in Stan, PyMC.
```

---

## 8. Regression Extensions

### Mixed Effects / Hierarchical Linear Models

```
Y = Xβ + Zu + ε

β: fixed effects (population-level)
u: random effects (group-level deviations), u ~ N(0, D)
ε ~ N(0, σ²I)

Marginal model: E[Y] = Xβ, Var(Y) = ZDZ' + σ²I

Random intercept model:
  Yᵢⱼ = β₀ + β₁Xᵢⱼ + u_i + εᵢⱼ
  u_i ~ N(0, τ²): random school/group effect
  ICC (intraclass correlation) = τ²/(τ²+σ²): within-group correlation.

Fitting: REML (Restricted Maximum Likelihood) for variance components.
  REML accounts for degrees of freedom used for fixed effects.
  lme4 (R), statsmodels.MixedLM (Python).
```

### Causal Inference with Regression

OLS estimates association, not causation. For causation:

```
Potential outcomes framework (Rubin):
  Y_i(1): outcome if treated.  Y_i(0): outcome if untreated.
  ATE = E[Y_i(1) - Y_i(0)]   [average treatment effect]
  Fundamental problem: observe only one potential outcome per unit.

Identifying ATE requires:
  Ignorability/unconfoundedness: treatment T ⊥ (Y(0),Y(1)) | X
  → Regression adjustment: E[Y|T=1,X] - E[Y|T=0,X] averaged over X.
  Valid only when all confounders X measured and controlled.

Instrumental variables (IV): instrument Z affects T but not Y directly.
  Two-stage least squares (2SLS):
    Stage 1: Regress T on Z, X → get Ŷ
    Stage 2: Regress Y on Ŷ, X → LATE (local ATE for compliers)
  Used for: Mendelian randomization (genetics as IV), natural experiments.

Regression discontinuity (RD): treatment assigned by threshold on running variable.
  At threshold: treated and untreated otherwise comparable.
  Identifies ATE at the threshold (local effect).

Difference-in-differences (DiD):
  ATT = (Ȳ_{treated,post} - Ȳ_{treated,pre}) - (Ȳ_{control,post} - Ȳ_{control,pre})
  Requires parallel trends assumption.
```

---

## Decision Cheat Sheet

```
Task:                                     Method:
────────────────────────────────────────  ──────────────────────────────────────────
Estimate parameter, known distribution    MLE (asymptotically efficient)
Small sample, want Bayes point estimate   MAP (with prior)
Confidence interval, large n              Wald CI: θ̂ ± z·SE
Confidence interval, small n or skewed   Bootstrap CI (BC_a)
Compare two means, normal data            Two-sample t-test (Welch)
Compare two means, non-normal/small n     Mann-Whitney U
Compare >2 groups, normal                 One-way ANOVA + Tukey HSD
Compare >2 groups, non-normal             Kruskal-Wallis + Dunn's test
Test independence of two categorical vars χ² test of independence
Continuous outcome, predict from features OLS regression
Binary outcome                            Logistic regression
Count outcome                             Poisson (or NegBin if overdispersed)
Positive continuous outcome               Gamma GLM
Multiple testing (large scale, e.g. GWAS) Benjamini-Hochberg FDR control
Bayesian updating, closed form            Conjugate prior (Beta-Binomial, etc.)
Complex hierarchical model               MCMC via Stan/PyMC (NUTS sampler)
Causal effect, RCT                       t-test on randomized assignment
Causal effect, observational             IV, DiD, RD — match the design
```

---

## Common Confusion Points

**p-value ≠ P(H₀ is true)**: p = P(data this extreme | H₀ true). It's about data, not hypotheses. P(H₀|data) requires a prior on H₀ — that's a Bayesian quantity.

**Confidence interval ≠ credible interval**: 95% CI does NOT mean "95% probability θ is in this interval." It means 95% of CIs constructed this way will contain θ. The credible interval (Bayesian) does support direct probability statements.

**Statistical significance ≠ practical significance**: With n=100,000 you can detect a difference of 0.001 at p<0.001. That doesn't mean the difference matters. Always report effect sizes.

**Multiple testing correction depends on family**: If you test 1000 SNPs, apply Bonferroni or BH. If you run one preregistered test, no correction needed. The "family" is the set of tests where you care about joint error rate.

**REML vs ML for mixed models**: ML maximizes joint likelihood of β and u — biased for variance components because fixed effects use up df. REML integrates out fixed effects first → unbiased variance estimates. Use REML for inference on variance components; ML for comparing models with different fixed effects (since REML log-likelihood depends on fixed effects specification).

**Gauss-Markov ≠ minimum variance generally**: OLS is BLUE — best among Linear Unbiased estimators. With normality assumption, OLS is the global UMVUE. Without normality, nonlinear estimators can be better (e.g., LAD regression under Laplace errors).

**Bootstrap doesn't fix small samples**: Bootstrap approximates the sampling distribution of θ̂. If n=5 and data is non-normal, the bootstrap distribution may still be a poor approximation. Bootstrap works best when n is moderate-large (n ≥ 30 as rough guide).

**Logistic regression coefficients are log-odds, not probabilities**: exp(β) = odds ratio. The probability increase for a unit change in X depends on the baseline probability (nonlinear).
