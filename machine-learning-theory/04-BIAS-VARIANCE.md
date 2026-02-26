# Bias-Variance Tradeoff and Model Selection

## The Big Picture

The bias-variance decomposition is a formal analysis of generalization error as a sum of two competing terms. It provides the classical picture of model selection — a picture that modern overparameterized models appear to violate (until you understand double descent).

```
+──────────────────────────────────────────────────────────────────+
|                  BIAS-VARIANCE FRAMEWORK                         |
|                                                                  |
|  TOTAL EXPECTED ERROR = BIAS² + VARIANCE + IRREDUCIBLE NOISE    |
|                                                                  |
|  BIAS: Error from wrong assumptions in the model class           |
|        Underfitting. Too simple. High if H can't represent f*.  |
|                                                                  |
|  VARIANCE: Error from sensitivity to training set fluctuations  |
|            Overfitting. Too complex. High if model memorizes S.  |
|                                                                  |
|  NOISE: Irreducible. Intrinsic randomness in the label process.  |
|         Cannot be eliminated by any model.                       |
|                                                                  |
|    ↑                                                             |
|  Error                                            Total error    |
|    |              Variance                      ╱               |
|    |               ╱╲                          ╱                |
|    |              ╱  ╲                        ╱                 |
|    |             ╱    ╲                      ╱                  |
|    |            ╱      ╲                    ╱                   |
|    |  Bias²    ╱        ╲__________________╱                    |
|    |───────────────────────────────────────                     |
|    +───────────────────────────────────────→ Model complexity   |
|                              ↑                                   |
|                          Optimal point                           |
+──────────────────────────────────────────────────────────────────+
```

---

## Formal Decomposition

**Setup**: Regression with squared loss. Data generated as y = f(x) + ε where E[ε] = 0, Var[ε] = σ².

```
BIAS-VARIANCE DECOMPOSITION
─────────────────────────────

For a fixed test point x, let ĥ_S(x) be the predictor trained on S.
Expected squared error over S and ε:

E_{S,ε}[(y - ĥ_S(x))²]

= (E_S[ĥ_S(x)] - f(x))²    +    Var_S[ĥ_S(x)]    +    σ²
  ─────────────────────────       ────────────────        ────
         Bias²                        Variance         Noise

WHERE
  Bias(x)     = E_S[ĥ_S(x)] - f(x)        (average prediction - true value)
  Variance(x) = E_S[(ĥ_S(x) - E_S[ĥ_S(x)])²]   (variation across training sets)

DERIVATION KEY STEP
  E[(y - ĥ)²] = E[(y - f + f - E[ĥ] + E[ĥ] - ĥ)²]
  = E[ε²] + (f - E[ĥ])² + E[(E[ĥ] - ĥ)²] + cross terms
  Cross terms vanish by independence. QED.
```

---

## Bridge: Stein's Phenomenon and James-Stein → Bias-Variance Tradeoff

The bias-variance tradeoff is not a new insight from ML — it is the content of Stein's phenomenon (1956) and the James-Stein estimator (1961), which resolved an open question in classical statistics.

```
THE STEIN PARADOX
  Estimating the mean θ ∈ ℝᵈ of a Gaussian: X ~ N(θ, I).
  Natural (unbiased) estimator: θ̂_MLE = X.
  Expected squared error: E[‖X - θ‖²] = d.

  James-Stein estimator (d ≥ 3):
    θ̂_JS = (1 - (d-2)/‖X‖²) · X

  Risk: E[‖θ̂_JS - θ‖²] < d for all θ.

  θ̂_MLE is INADMISSIBLE in ≥ 3 dimensions:
  A biased estimator uniformly dominates the unbiased one.
```

This is the bias-variance tradeoff in its purest form: θ̂_JS introduces bias (shrinks toward 0) to reduce variance (each coordinate's estimate becomes more stable). The reduction is exactly:

```
  Risk(θ̂_JS) = d - (d-2)² · E[1/‖X‖²]
              = d - (variance reduction from shrinkage)
                + (bias² from shrinkage toward 0)

  The net effect is negative (better than MLE) for d ≥ 3
  because the variance reduction outweighs the bias introduced.
```

**Stein's Unbiased Risk Estimate (SURE).** For any estimator θ̂(X) of a Gaussian mean, SURE gives an unbiased estimate of E[‖θ̂ - θ‖²] from data alone (without knowing θ). SURE = ‖θ̂(X) - X‖² + 2·div(θ̂(X)) - d, where div is the divergence of the estimator function. This allows bias-variance optimization without a held-out set — directly applicable to denoising, ridge regression (SURE selects λ), and wavelet thresholding.

**Lasso via soft-thresholding = Stein-type shrinkage.** Soft-thresholding estimator θ̂ᵢ = sign(Xᵢ) max(|Xᵢ| - λ, 0) is a componentwise James-Stein-type shrinkage. Stein's framework predicts its optimality for sparse θ.

## What Each Term Represents

```
BIAS: WHERE DOES IT COME FROM?
  • Hypothesis class H cannot represent f* (misspecification)
  • Regularization that biases estimates toward simpler models
  • Wrong priors in Bayesian models

  Examples of high-bias models:
    Linear regression when f* is quadratic
    Shallow decision tree when f* is complex
    L2-regularized model with too-large λ

VARIANCE: WHERE DOES IT COME FROM?
  • Small training set relative to model complexity
  • High-dimensional parameter space
  • Noise amplification through complex models

  Examples of high-variance models:
    Deep neural net with millions of params, 100 training examples
    Nearest-neighbor with k=1
    Unregularized polynomial regression, high degree

NOISE: IRREDUCIBLE
  • Inherent randomness in the data generation process
  • Label noise, measurement error, aliasing
  • Lower bound on expected error regardless of model
```

---

## The Classical U-Curve and Model Selection

```
CLASSICAL PICTURE: U-SHAPED TEST ERROR CURVE
────────────────────────────────────────────

  Error
    │                                          Total (test)
    │ ▲                                     ╱
    │  ╲ Bias²                            ╱
    │   ╲                               ╱
    │    ╲          Variance          ╱
    │     ╲         ╱               ╱
    │      ╲       ╱   Total       ╱
    │       ╲     ╱   (train)     ╱
    │        ╲   ╱ ──────────────
    │         ╲ ╱
    │          ╳  ← Optimal model complexity
    │           ╲
    └────────────────────────────────────────→ Model complexity

  Train error: monotonically decreasing
  Test error:  U-shaped, with minimum at optimal complexity

  Model selection: choose complexity at the minimum of test error.
```

**Classical prescriptions from this picture:**
- Cross-validation to estimate test error
- Early stopping as approximate regularization
- Regularization (L1/L2) to control effective complexity
- Model selection criteria: AIC, BIC, MDL

---

## The Bias-Variance Tradeoff in Classification

For 0-1 loss, the decomposition is more complex — there is no clean additive form because loss is not squared:

```
CLASSIFICATION (0-1 loss)
──────────────────────────
No clean additive decomposition in general.

Several variants exist:

  DOMINGOS (2000): Signed bias-variance-noise
    • Bias: systematic errors (same direction)
    • Variance: random errors (vary with training set)
    • Noise: Bayes error floor

  BAYESIAN: Via squared loss on posterior probabilities
    P(Y=1|X=x) → apply regression decomposition to probabilities

  PRACTICAL IMPLICATION
    Bias-variance intuition still applies qualitatively.
    Large model, small data → overfitting → high effective variance.
    Small model, large data → underfitting → high bias.
```

---

## Bias-Variance as a Function of Training Set Size

```
FIXED MODEL CLASS, VARYING m
───────────────────────────────

  m small:  Variance dominates. Model memorizes few samples.
            Test >> Train error (large generalization gap).

  m → ∞:   Variance → 0. Bias remains fixed (determined by H).
            Test error → Bias² + σ²  (learning curve asymptote)

  LEARNING CURVE
    ↑
  Error
    │ ████                         ← Test error
    │ ████╲
    │ ████ ╲────────────────────   ← Test converges to bias + noise
    │ ████  ╲                      ← Train error rises toward asymptote
    │  ↑    ╲────────────────────  ← Train error (starts at 0)
    │ optimal
    └────────────────────────→ m (training set size)

  If test and train error converge to a HIGH value: bias problem
  If test and train error converge to a LOW value: good model
  If gap between test and train stays large: variance problem
```

---

## Regularization as Bias-Variance Control

```
RIDGE REGRESSION (L2 regularization)
──────────────────────────────────────
  ĥ_λ = argmin_{w} [ (1/m)||Xw - y||² + λ||w||² ]

  Solution:  ŵ_λ = (XᵀX + λI)⁻¹ Xᵀy

  BIAS:     E[ŵ_λ] = (XᵀX + λI)⁻¹ XᵀX · w*
            Bias = λ · (XᵀX + λI)⁻¹ · w*   [nonzero if λ > 0]

  VARIANCE: Var[ŵ_λ] = σ² · (XᵀX + λI)⁻¹ XᵀX (XᵀX + λI)⁻¹
            Smaller than OLS variance (λ shrinks eigenvalues)

  AS λ INCREASES:
    Bias↑   Variance↓
    Optimal λ balances these; found via cross-validation.

LASSO (L1 regularization)
  Same bias-variance tradeoff but induces sparsity.
  Useful when true w* is sparse.

DROPOUT (neural nets)
  Approximates ensemble of models → variance reduction.
  Effective regularization without explicit penalty term.
```

---

**AIC and BIC derivations.** AIC = -2 log L + 2k follows from Akaike (1974): minimizing AIC is asymptotically equivalent to minimizing expected KL divergence KL(P_true || P_model) — the expected information loss from using the model instead of the true distribution. The 2k penalty is an asymptotic bias correction: the MLE overfits by approximately k/m in expected KL, so penalizing by 2k (on the -2 log L scale) corrects this. BIC = -2 log L + k log m follows from the Laplace approximation to the marginal likelihood: ∫ P(data|θ) P(θ) dθ ≈ P(data|θ̂_MAP) · (2π/m)^{k/2} · |I(θ̂)|^{-1/2}, where the (2π/m)^{k/2} term gives the k log m penalty. BIC is a model evidence approximation; AIC is a predictive risk estimator.

## Model Selection Methods

```
METHOD              APPROACH                      NOTES
──────────────────  ──────────────────────────    ──────────────────────
Hold-out validation Train/val/test split          Simple; wastes data
K-fold CV           Rotate through k folds        Better use of data
Leave-one-out CV    K-fold with K=m               Expensive; unbiased
Bootstrap           Resample with replacement     Good for small data
AIC                 -2 log L + 2k                Penalizes complexity
                    (k = num parameters)          Asymptotically efficient
BIC                 -2 log L + k·log m           Penalizes more with m
                    (m = sample size)             Consistent model selection
MDL                 Minimum description length    Information-theoretic
```

**AIC vs BIC**:
- AIC minimizes expected KL divergence — good for prediction
- BIC is consistent (finds true model as m → ∞) — good for model identification
- In practice, BIC penalizes complexity more and selects simpler models

---

## Connection to Regularization Theory

```
REGULARIZATION AS IMPLICIT BIAS CONTROL
──────────────────────────────────────────

TIKHONOV REGULARIZATION (generalization of L2)
  Adds ||Lw||² for some operator L
  L = identity → Ridge; L = differences → smoothness prior

KERNEL RIDGE REGRESSION
  In RKHS with kernel k:
    ĥ = argmin_{h ∈ H_k} [ (1/m)Σ loss(h(xᵢ),yᵢ) + λ||h||²_{H_k} ]

  Bias: controlled by λ and richness of k (can represent f*?)
  Variance: O(tr(K)/(λ²m)) where K is the kernel Gram matrix

  Optimal λ ~ m^{-2/(2β+d)} for Sobolev spaces (β smoothness, d dims)
  → Regularization must decrease as m grows

**Spectral decomposition of kernel ridge regression bias-variance.** Via Mercer decomposition of the kernel (eigenfunctions φⱼ, eigenvalues μⱼ), the kernel ridge estimator decomposes as:

```
  BIAS²    = Σⱼ (   λ/(λ + μⱼ)  )² fⱼ²    (signal filtered by regularization)
  VARIANCE = σ² Σⱼ ( μⱼ/(λ + μⱼ) )² / m    (noise amplified by kernel)

  where fⱼ = ⟨f*, φⱼ⟩ are the signal's projections onto eigenfunctions.

  As λ → 0:  bias → 0, variance → σ² Σⱼ 1/m  (explodes if Σμⱼ diverges)
  As λ → ∞:  variance → 0, bias → Σⱼ fⱼ² = ‖f*‖²  (complete shrinkage)

  Optimal λ balances dBIAS²/dλ = -dVARIANCE/dλ.

SOBOLEV EIGENVALUE DECAY AND OPTIMAL RATES
  For β-smooth f* in d dimensions, eigenvalues decay μⱼ ~ j^{-2β/d}.
  Optimal λ ~ m^{-2β/(2β+d)} balances bias and variance sums,
  giving excess risk O(m^{-2β/(2β+d)}) — the classical nonparametric rate.
  More smoothness (large β) → faster rate; higher dimension (large d) → slower.
```

THE DOUBLE DESCENT PROBLEM
  Classical theory says: increase complexity → increase variance → overfit
  Practice shows: keep increasing complexity past interpolation → underfit
                  decreases again (benign overfitting)
  This is Module 07. The bias-variance picture is incomplete.
```

---

## Decision Cheat Sheet

| Observation | Diagnosis | Fix |
|-------------|-----------|-----|
| Train error low, test error high | High variance | More data, regularization, simpler model |
| Both train and test error high | High bias | More complex model, different features |
| Train and test error both high, equal | High bias | Same |
| Train and test error both converge but to same high value | Bias floor = Bayes error, or model misspecified | Check model family |
| Test error U-shaped with model complexity | Classic bias-variance | Find optimal complexity via CV |
| Test error keeps decreasing with complexity | Double descent | Module 07 |
| Adding regularization increases test error | Already high bias | Reduce λ or use different regularization |

---

## Common Confusion Points

**"Bias-variance is for regression — does it apply to classification?"**
The squared-loss decomposition is exact and clean only for regression. For classification, additive decompositions exist but are less clean. The qualitative insight holds: simple models have systematic errors (bias); complex models on small datasets are erratic (variance). The practical tools (cross-validation, regularization) apply in both settings.

**"Adding more features always increases variance — is that true?"**
In the classical regime (m > p), yes. But in the overparameterized regime (p ≫ m), adding features can actually reduce variance by enabling the model to fit the data without bending into extreme shapes. This is the benign overfitting phenomenon — not captured by classical bias-variance analysis.

**"Ensemble methods reduce variance — do they also reduce bias?"**
Averaging reduces variance (law of large numbers on the ensemble). Bias of the ensemble equals the average bias of each member — no systematic reduction. But boosting deliberately constructs ensemble members to reduce bias iteratively, so it can reduce both. Bagging reduces variance. Boosting reduces bias primarily.

**"Best model minimizes test error — isn't that trivially the cross-validation answer?"**
Yes, but: (1) cross-validation has its own bias-variance tradeoff (k-fold CV with small k is biased; LOO-CV has high variance); (2) you don't have access to the true test distribution; (3) in online/distributional-shift settings, the test distribution changes. CV is the right practical tool but is not a panacea.
