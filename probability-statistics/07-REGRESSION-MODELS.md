# Regression Models

## The Big Picture

Regression models the relationship between a response Y and predictors X. The family ranges from OLS to GLMs to mixed effects to regularized high-dimensional models.

```
+------------------------------------------------------------------+
|                      REGRESSION TAXONOMY                         |
+------------------------------------------------------------------+
|                                                                  |
|  CLASSICAL LINEAR                                                |
|  +---------------------------+                                   |
|  | OLS: Y = Xbeta + epsilon  |  epsilon ~ Normal(0, sigma^2 I)   |
|  | Assumptions: linearity, independence, homoscedasticity        |
|  +---------------------------+                                   |
|          |                                                       |
|          v                                                       |
|  GENERALIZED LINEAR MODELS (GLMs)                                |
|  +---------------------------+                                   |
|  | Relax Normality of Y.     |  Y ~ Exponential family           |
|  | link(E[Y]) = X beta       |  (Logistic, Poisson, Gamma, ...)  |
|  +---------------------------+                                   |
|          |                                                       |
|          v                                                       |
|  REGULARIZED / HIGH-DIMENSIONAL                                  |
|  +---------------------------+                                   |
|  | Ridge: L2 penalty         |  For multicollinearity            |
|  | Lasso: L1 penalty         |  For sparse models                |
|  | Elastic Net: L1 + L2      |  For correlated predictors        |
|  +---------------------------+                                   |
|          |                                                       |
|          v                                                       |
|  MIXED EFFECTS MODELS                                            |
|  +---------------------------+                                   |
|  | Fixed effects + random    |  For grouped / repeated data      |
|  | effects for groups        |  Partial pooling                  |
|  +---------------------------+                                   |
+------------------------------------------------------------------+
```

---

## Ordinary Least Squares

**Setup**: Y = X beta + epsilon, where X is n x p, epsilon ~ Normal(0, sigma^2 I).

```
  OLS estimator: beta_hat = argmin ||Y - X beta||^2
               = (X^T X)^{-1} X^T Y    (assuming X full rank)

  This is both:
  - The BLUE (Best Linear Unbiased Estimator) by Gauss-Markov
  - The MLE under Normal errors

  Residuals: e = Y - X beta_hat = (I - H) Y  where H = X(X^T X)^{-1} X^T
  H is the "hat matrix" — the orthogonal projection onto col(X).

  SSR (Sum of Squared Residuals) = Y^T (I-H) Y = ||e||^2
  SST (Total SS) = ||Y - Y_bar||^2
  R^2 = 1 - SSR/SST = fraction of variance explained by X
```

**Gauss-Markov theorem**: Under linear model assumptions (linearity, independence, homoscedasticity, exogeneity — NOT normality), OLS is BLUE among all linear unbiased estimators.

**Inference**:

```
  beta_hat ~ Normal(beta, sigma^2 (X^T X)^{-1})

  (beta_hat_j - beta_j) / SE(beta_hat_j) ~ t_{n-p}

  F-test for overall model:
  F = (R^2/p) / ((1-R^2)/(n-p-1)) ~ F_{p, n-p-1} under beta=0
```

---

## Geometry of OLS

OLS has a clean geometric interpretation that connects to the SVD:

```
  col(X)              col(X)^perp
  +---------+         +---------+
  |         |         |         |
  |  X beta |         |    e    |
  |   = Hy  |   +     | = (I-H)y|
  |         |         |         |
  +---------+         +---------+
             --------------------
                   Y = Hy + (I-H)Y

  OLS minimizes ||Y - X beta||^2 by projecting Y onto col(X).
  beta_hat is the coefficients in this projection.

  Pythagorean theorem: ||Y||^2 = ||X beta_hat||^2 + ||e||^2
  R^2 = cos^2(angle between Y and col(X))
```

**SVD connection**: X = U S V^T (economy SVD). Then:

```
  beta_hat = V S^{-1} U^T Y
  H = U U^T  (projection onto column space of X)

  Small singular values in S lead to large variance in beta_hat.
  This is the multicollinearity problem: when X^T X is ill-conditioned.
  Ridge regression stabilizes by replacing S^{-1} with S/(S^2 + lambda).
```

---

## Generalized Linear Models

GLMs extend OLS to non-Normal response distributions. Three components:

```
  1. RANDOM component: Y ~ Exponential family distribution
     (Bernoulli, Poisson, Gamma, Inverse-Gaussian, ...)

  2. SYSTEMATIC component: eta = X beta  (linear predictor)

  3. LINK function: g(mu) = eta  where mu = E[Y|X]
     g is a monotone function connecting mean to linear predictor.

  Common GLM instances:
  +------------------+-------------+----------+-------------------+
  | Name             | Distribution| Link g() | Use Case          |
  +------------------+-------------+----------+-------------------+
  | Linear regression| Normal      | identity | Continuous Y      |
  | Logistic regr.   | Bernoulli   | logit    | Binary outcome    |
  | Probit regr.     | Bernoulli   | probit   | Binary outcome    |
  | Poisson regr.    | Poisson     | log      | Count data        |
  | Neg. Binomial    | Neg. Binom  | log      | Overdispersed cts |
  | Gamma regression | Gamma       | log/inv  | Positive Y, skewed|
  | Multinomial      | Multinomial | logit    | Multi-class       |
  +------------------+-------------+----------+-------------------+
```

**Logistic regression** in detail:

```
  Y_i ~ Bernoulli(pi_i)
  logit(pi_i) = log(pi_i / (1-pi_i)) = X_i beta

  pi_i = 1 / (1 + exp(-X_i beta))  (sigmoid function)

  LOG-ODDS INTERPRETATION:
  beta_j = change in log-odds per unit increase in X_j
  Odds ratio: exp(beta_j) = multiplicative change in odds

  FITTING: No closed form. IRLS (Iteratively Reweighted Least Squares)
  or gradient-based optimization.

  Log-likelihood: l(beta) = Sum_i [y_i log pi_i + (1-y_i) log(1-pi_i)]
                = Sum_i [y_i X_i beta - log(1 + exp(X_i beta))]
```

**IRLS**: GLMs are fit by iteratively solving weighted least squares problems. At each step, compute a working response Z and working weights W, solve OLS with these. Converges to MLE.

---

## Regularization: Ridge, Lasso, Elastic Net

Regularization adds a penalty to the loss function to control model complexity.

**Ridge regression (L2 penalty)**:

```
  beta_hat_ridge = argmin ||Y - X beta||^2 + lambda ||beta||^2

  Closed form: beta_hat = (X^T X + lambda I)^{-1} X^T Y

  Effect of lambda:
  - lambda=0: OLS (no regularization)
  - lambda->inf: beta_hat -> 0 (full regularization)

  SVD form: beta_ridge = V diag(s_i / (s_i^2 + lambda)) U^T Y
  Small eigenvalues s_i get more shrinkage.

  BAYESIAN INTERPRETATION: Ridge = MAP with Normal(0, sigma^2/lambda) prior on beta.
  DOES NOT do variable selection: all coefficients are nonzero.
  Best for: multicollinearity, all predictors genuinely relevant.
```

**Lasso (L1 penalty)**:

```
  beta_hat_lasso = argmin ||Y - X beta||^2 + lambda ||beta||_1

  No closed form (|beta_j| not differentiable at 0).
  Solved by coordinate descent, LARS, or ADMM.

  KEY PROPERTY: Induces sparsity. Some beta_j exactly = 0.
  This is variable selection — Lasso selects a subset of predictors.

  WHY L1 GIVES SPARSITY (geometric intuition):
  The L1 ball (diamond shape) has corners at axes.
  Optimal often occurs at a corner -> zero coefficients.
  L2 ball (sphere) has no corners; optimum is rarely exactly zero.

  BAYESIAN INTERPRETATION: Lasso = MAP with Laplace(0, 1/lambda) prior.
  Best for: high-dimensional sparse problems (many predictors, few relevant).
```

**Elastic Net (L1 + L2)**:

```
  Penalty: alpha * lambda ||beta||_1 + (1-alpha)/2 * lambda ||beta||^2

  Combines: Lasso sparsity + Ridge grouping effect.
  When predictors are correlated: Lasso arbitrarily picks one;
  Elastic net tends to select the whole group.

  alpha = 1: Lasso; alpha = 0: Ridge.
  Usually alpha in [0.1, 0.9].
```

**Choosing lambda**: Cross-validation. K-fold CV computes prediction error for each lambda on held-out data. Choose lambda_min (min CV error) or lambda_1se (largest lambda within 1 SE of min).

---

## Model Diagnostics

```
  RESIDUAL ANALYSIS:
  e_i = y_i - y_hat_i  (raw residuals)
  r_i = e_i / (sigma * sqrt(1 - h_ii))  (studentized residuals)

  Leverage: h_ii = [H]_{ii}   (how influential is observation i's X)
  Cook's distance: D_i = (beta_hat - beta_hat_{-i})^T X^T X (beta_hat - beta_hat_{-i}) / (p sigma^2)
  (How much does beta change if we delete observation i?)

  DIAGNOSTIC PLOTS:
  Residuals vs. fitted: check linearity, homoscedasticity
  Q-Q plot of residuals: check normality
  Scale-location plot: check homoscedasticity
  Residuals vs. leverage: identify influential points
```

**Variance Inflation Factor (VIF)**:

```
  VIF_j = 1 / (1 - R_j^2)

  Where R_j^2 is R-squared from regressing X_j on all other X_k.
  VIF_j > 5-10 indicates multicollinearity for variable j.
  High VIF -> inflated standard errors -> unreliable inference.
  Fix: ridge regression, remove collinear predictors, PCA regression.
```

---

## Mixed Effects Models

For data with group structure: students within schools, measurements within patients, regions within countries.

```
  LINEAR MIXED MODEL:
  Y_{ij} = X_{ij} beta + Z_{ij} b_i + epsilon_{ij}

  Y_{ij} = observation j in group i
  X_{ij} beta = fixed effects (same for all groups)
  Z_{ij} b_i  = random effects (group-specific)
  b_i ~ Normal(0, D)  (random effects distribution)
  epsilon_{ij} ~ Normal(0, sigma^2)

  Examples:
  - Repeated measures: time effects (fixed) + individual intercepts (random)
  - Schools: school-level covariates (fixed) + school random effects
  - Longitudinal: treatment effect (fixed) + subject random slopes
```

**Random intercepts model**:

```
  Y_{ij} = mu + alpha_i + epsilon_{ij}
  mu = overall mean (fixed)
  alpha_i ~ Normal(0, tau^2) (group-specific offset, random)

  ICC (Intraclass Correlation Coefficient):
  ICC = tau^2 / (tau^2 + sigma^2)
  = fraction of variance attributable to group membership
  ICC near 0: groups don't matter, use OLS
  ICC near 1: within-group observations nearly identical
```

**Connection to Bayesian hierarchical models**: Linear mixed models ARE Bayesian hierarchical models with Normal priors on random effects, fitted by REML (Restricted Maximum Likelihood). REML is empirical Bayes — it estimates the hyperparameters (tau^2) from the data.

---

## High-Dimensional Regression

When p >> n (more predictors than observations):

```
  OLS fails: X^T X is singular. Many solutions with ||e||^2 = 0.

  Regularization is essential:
  - Lasso: automatic variable selection, O(n p) computation
  - Ridge: stable, no variable selection, closed form

  THEORETICAL GUARANTEES (for Lasso):
  If true beta has s nonzero coefficients and X satisfies
  "Restricted Eigenvalue Condition", then:

  ||beta_hat_lasso - beta_0||_2 = O(s log(p) / n)^{1/2}

  Rate: sqrt(s log(p) / n) rather than sqrt(p/n) for ridge.
  The sparsity s controls difficulty, not ambient dimension p.
```

**Compressed sensing connection**: These are the same results — if a signal is sparse in some basis and you take random measurements, Lasso recovery is exact (up to noise). LASSO = L1 relaxation of the NP-hard subset selection problem (L0 penalty).

**Restricted Isometry Property (RIP)** — why random matrices enable sparse recovery:

```
  X satisfies RIP of order s with constant delta_s if:
  (1 - delta_s) ||beta||^2 <= ||X beta||^2 / n <= (1 + delta_s) ||beta||^2
  for all s-sparse vectors beta.

  RIP says: X approximately preserves norms of sparse vectors.
  If delta_{2s} < sqrt(2) - 1: Lasso recovers the true s-sparse beta exactly (noiseless)
  or within O(sigma sqrt(s log p / n)) (noisy).

  WHY RANDOM MATRICES WORK (random matrix theory):
  Gaussian random X (n×p, entries iid N(0,1/n)) satisfies RIP with high probability
  when n >= C s log(p/s). This is near-optimal: any matrix requires n >= Omega(s log(p/s)).
  The proof uses concentration of eigenvalues of X^T X restricted to s-sparse subspaces.
```

**Debiased Lasso** (for valid inference after selection): The Lasso estimate is biased (shrinkage). For confidence intervals on individual coefficients, the debiased/desparsified Lasso corrects the bias: β̂_debiased = β̂_lasso + (X^T X / n)^{-1} X^T (Y − X β̂_lasso) / n. Under sparsity conditions, β̂_debiased is asymptotically Normal, enabling valid CIs.

---

## Decision Cheat Sheet

| Situation | Model | Key Hyperparameter |
|---|---|---|
| Continuous Y, Gaussian errors | OLS | None |
| Binary Y | Logistic regression | None (or regularization lambda) |
| Count Y | Poisson regression | None |
| Count Y with overdispersion | Negative binomial regression | Dispersion |
| Positive Y, skewed | Gamma regression | None |
| Multicollinearity, all predictors matter | Ridge | lambda (CV) |
| Sparse true model | Lasso | lambda (CV) |
| Correlated predictors, sparse model | Elastic Net | alpha, lambda (CV) |
| Grouped/repeated-measures data | Linear mixed model | Random effects variance |
| p >> n | Lasso/Ridge | lambda (CV) |

---

## Common Confusion Points

**"R^2 = 0.8 means the model is good."**
R^2 measures variance explained, not predictive accuracy or model validity. You can have R^2 = 0.99 with a badly misspecified model (Anscombe's quartet). Always check residual diagnostics.

**"The Lasso always selects the right variables."**
Lasso is consistent for variable selection only under the "irrepresentable condition" — the relevant predictors cannot be too correlated with irrelevant ones. For highly correlated predictors, Lasso's selection is unstable; Elastic Net is more reliable.

**"Fixed effects vs. random effects is a philosophical choice."**
It is partly philosophical (are groups a sample from a population?) but also practical: random effects require distributional assumptions (Normality) for the random component; fixed effects consume a parameter per group. Random effects enable prediction for new groups; fixed effects do not. The ICC guides the choice.

**"Ridge regression shrinks coefficients to zero."**
Ridge shrinks toward zero but never reaches it (for finite lambda). Lasso does reach exactly zero (inducing sparsity). This is the fundamental difference between L2 and L1 penalties.

**Predictive vs. causal regression — a critical distinction.** OLS minimizes prediction error E[(Y − X β̂)²]. This does NOT mean β̂ₖ is the causal effect of Xₖ on Y. Causal interpretation requires: (1) no unmeasured confounders (all common causes of X and Y are in the model); (2) no reverse causation (X causes Y, not Y causes X); (3) no collider bias (not conditioning on a common effect). Under these assumptions — formalized in Pearl's do-calculus as the "back-door criterion" — the OLS coefficient β̂ₖ estimates E[Y | do(Xₖ = x+1)] − E[Y | do(Xₖ = x)]. Without these assumptions, β̂ₖ is a useful predictor but not a causal quantity. See `statistics-applied/` for the full causal inference machinery (potential outcomes, instrumental variables, difference-in-differences, regression discontinuity).
