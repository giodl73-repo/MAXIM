# Random Variables and Distributions

## The Big Picture

```
+------------------------------------------------------------------+
|                   DISTRIBUTION FAMILIES                          |
+------------------------------------------------------------------+
|                                                                  |
|  DISCRETE                      CONTINUOUS                        |
|  +--------------------+        +--------------------+           |
|  | Bernoulli          |        | Uniform            |           |
|  | Binomial           |        | Normal (Gaussian)  |           |
|  | Geometric          |        | Exponential        |           |
|  | Negative Binomial  |        | Gamma              |           |
|  | Poisson            |        | Beta               |           |
|  | Hypergeometric     |        | Cauchy             |           |
|  | Categorical        |        | Student-t          |           |
|  | Multinomial        |        | Chi-squared        |           |
|  +--------------------+        | Log-normal         |           |
|                                | Pareto (heavy tail)|           |
|  DERIVED FROM NORMAL           +--------------------+           |
|  +-----------------------------+                                 |
|  | Chi-squared: sum of sq normal r.v.s                         |
|  | t-distribution: normal / sqrt(chi-sq / n)                   |
|  | F-distribution: ratio of chi-squareds                       |
|  | Wishart: multivariate chi-squared (for covariances)         |
|  +-----------------------------+                                 |
|                                                                  |
|  EXPONENTIAL FAMILY (unified framework)                         |
|  Normal, Poisson, Exponential, Binomial, Gamma, Beta, ...       |
+------------------------------------------------------------------+
```

---

## Characterizing a Distribution

Four equivalent ways to specify the distribution of a real-valued r.v. X:

```
  1. CDF (Cumulative Distribution Function)
     F(x) = P(X <= x)
     Always exists. Right-continuous, non-decreasing, F(-inf)=0, F(+inf)=1.
     Works for discrete, continuous, and mixed.

  2. PMF (Probability Mass Function) -- discrete only
     p(x) = P(X = x)
     F(x) = Sum_{k <= x} p(k)

  3. PDF (Probability Density Function) -- absolutely continuous
     f(x) such that P(X in A) = Integral_A f(x) dx
     f >= 0, Integral f = 1.  Note: f(x) is NOT P(X = x).

  4. Characteristic function
     phi_X(t) = E[e^{itX}]    (Fourier transform of the distribution)
     Always exists. Uniquely determines the distribution.
     phi_{X+Y}(t) = phi_X(t) phi_Y(t)  if X, Y independent.
```

**The characteristic function** is the probability theorist's tool of choice for proving the CLT and computing distributions of sums. The moment generating function E[e^{tX}] (the Laplace transform of the distribution) works when it exists in a neighborhood of 0, but the CF always exists.

---

## Moments and Cumulants

```
  MOMENTS (raw and central)
  E[X^k]          = k-th raw moment
  E[(X - mu)^k]   = k-th central moment  (mu = E[X])

  mu = E[X]        mean (1st raw moment)
  Var(X) = E[(X-mu)^2] = E[X^2] - mu^2  (2nd central moment)
  sigma = sqrt(Var(X))   standard deviation

  Skewness = E[(X-mu)^3] / sigma^3    (3rd standardized moment)
  Kurtosis = E[(X-mu)^4] / sigma^4    (4th standardized moment)
             Excess kurtosis = kurtosis - 3
             Normal has excess kurtosis 0.

  CUMULANTS (cleaner for sums)
  log E[e^{tX}] = Sum_k kappa_k t^k / k!
  kappa_1 = mean, kappa_2 = variance, kappa_3 = skewness x sigma^3
  For independent X,Y: kappa_k(X+Y) = kappa_k(X) + kappa_k(Y)  (all k)
  For Normal: all cumulants beyond kappa_2 are zero.
```

---

## The Normal Distribution — Central Object

```
  X ~ Normal(mu, sigma^2)

  PDF:   f(x) = (1 / sqrt(2 pi sigma^2)) exp(-(x-mu)^2 / (2 sigma^2))
  CDF:   Phi((x-mu)/sigma)  where Phi = standard normal CDF
  MGF:   exp(mu*t + sigma^2*t^2/2)
  CF:    exp(i*mu*t - sigma^2*t^2/2)
  E[X] = mu,  Var(X) = sigma^2

  KEY PROPERTIES:
  1. Stable: Normal + Normal = Normal (same family under convolution)
  2. Maximum entropy given fixed mean and variance
  3. Closed under linear transformations: aX + b ~ Normal(a*mu+b, a^2*sigma^2)
  4. Sum of n i.i.d. Normal: X_bar ~ Normal(mu, sigma^2/n)
```

**Multivariate Normal**:

```
  X ~ N(mu, Sigma)   where mu in R^n, Sigma is n x n PSD matrix

  PDF: (2 pi)^{-n/2} |Sigma|^{-1/2} exp(-1/2 (x-mu)^T Sigma^{-1} (x-mu))

  Key: Marginals and conditionals of multivariate Normal are Normal.
  Conditional: (X_1 | X_2 = x_2) ~ Normal(mu_1 + Sigma_12 Sigma_22^{-1}(x_2 - mu_2),
                                            Sigma_11 - Sigma_12 Sigma_22^{-1} Sigma_21)
```

---

## Common Distribution Reference

### Discrete Distributions

| Distribution | Parameters | Mean | Variance | Key Use |
|---|---|---|---|---|
| Bernoulli(p) | p in [0,1] | p | p(1-p) | Binary outcome |
| Binomial(n,p) | n>=1, p in [0,1] | np | np(1-p) | k successes in n trials |
| Geometric(p) | p in (0,1] | 1/p | (1-p)/p^2 | Trials until first success |
| NegBin(r,p) | r>=1, p in (0,1] | r/p | r(1-p)/p^2 | Trials until r-th success |
| Poisson(lambda) | lambda > 0 | lambda | lambda | Counts in fixed interval |
| Hypergeometric | N,K,n | nK/N | --- | Sampling without replacement |

**Poisson as Binomial limit**: Bin(n, lambda/n) -> Poisson(lambda) as n -> inf. The Poisson distribution models rare events in a large number of trials.

### Continuous Distributions

| Distribution | Parameters | Mean | Variance | Key Use |
|---|---|---|---|---|
| Uniform(a,b) | a < b | (a+b)/2 | (b-a)^2/12 | No information prior |
| Exponential(lambda) | lambda > 0 | 1/lambda | 1/lambda^2 | Waiting times |
| Gamma(alpha, beta) | alpha,beta > 0 | alpha/beta | alpha/beta^2 | Sum of exponentials |
| Beta(alpha, beta) | alpha,beta > 0 | alpha/(alpha+beta) | --- | Probabilities, Bayesian priors |
| Normal(mu, sigma^2) | sigma > 0 | mu | sigma^2 | Universal via CLT |
| Log-Normal(mu, sigma^2) | --- | e^{mu + sigma^2/2} | --- | Multiplicative processes |
| Cauchy(x_0, gamma) | --- | undefined | undefined | Heavy tails, no moments |
| Pareto(x_m, alpha) | x_m,alpha > 0 | depends | depends | Power law tails |
| Student-t(nu) | nu > 0 | 0 (nu>1) | nu/(nu-2) | Inference with unknown variance |
| Chi-squared(k) | k > 0 | k | 2k | Sum of squared normals |

---

## The Exponential Family

Many distributions share a common structure — the exponential family:

```
  p(x | theta) = h(x) exp(eta(theta)^T T(x) - A(theta))

  Where:
  h(x)      = base measure (often 1)
  eta(theta) = natural parameters
  T(x)      = sufficient statistics
  A(theta)  = log-partition function (cumulant generating function of T)

  Examples:
  Normal(mu, sigma^2):   eta = (mu/sigma^2, -1/(2 sigma^2))
                         T(x) = (x, x^2)
  Poisson(lambda):       eta = log(lambda), T(x) = x
  Binomial(n, p):        eta = log(p/(1-p)), T(x) = x  (logit!)
  Exponential(lambda):   eta = -lambda, T(x) = x
```

**Why the exponential family matters**:
1. **Sufficient statistics**: T(X) contains all information about theta (Fisher-Neyman factorization)
2. **Conjugate priors**: The Bayesian prior for an exponential family likelihood is itself in the exponential family
3. **Information geometry**: The natural parameters eta form coordinates on the statistical manifold
4. **MLE**: The MLE equation reduces to E_theta[T(X)] = T_bar (sample average of sufficient statistics)
5. **GLMs**: Generalized linear models use exponential family distributions as response distributions

---

## Multivariate Distributions and Copulas

**Joint distributions** when X and Y are not independent:

```
  Joint PDF: f(x,y)   with f(x,y) >= 0 and Double integral f = 1
  Marginals: f_X(x) = Integral f(x,y) dy
  Conditional: f_{Y|X}(y|x) = f(x,y) / f_X(x)

  Covariance: Cov(X,Y) = E[(X-muX)(Y-muY)] = E[XY] - E[X]E[Y]
  Correlation: rho = Cov(X,Y) / (sigma_X * sigma_Y)  in [-1,1]

  WARNING: rho = 0 does NOT imply independence.
  Uncorrelated means no LINEAR dependence, not no dependence.
```

**Copulas** (Sklar's theorem): Any joint CDF F(x,y) can be written as:

```
  F(x,y) = C(F_X(x), F_Y(y))

  Where C: [0,1]^2 -> [0,1] is the copula.
  The copula captures dependence structure SEPARATELY from marginals.

  Common copulas:
  Gaussian copula: dependence from multivariate normal (but with arbitrary marginals)
  Clayton: stronger lower-tail dependence
  Gumbel: stronger upper-tail dependence
  t-copula: heavy-tail joint dependence
```

Copulas matter in risk management and finance — the 2008 financial crisis partly arose from mis-specifying copula structure (using Gaussian when actual tail dependence was much stronger).

---

## Transforms and Their Uses

```
  MOMENT GENERATING FUNCTION (MGF)
  M_X(t) = E[e^{tX}]
  When it exists near t=0: E[X^k] = M_X^{(k)}(0)   (k-th derivative at 0)
  M_{X+Y}(t) = M_X(t) M_Y(t)  if X, Y independent.
  Does NOT always exist (e.g., Cauchy distribution).

  CHARACTERISTIC FUNCTION
  phi_X(t) = E[e^{itX}]  (always exists)
  Inversion: f(x) = (1/2 pi) Integral phi_X(t) e^{-itx} dt
  If phi_X = phi_Y then X and Y have the same distribution.

  PROBABILITY GENERATING FUNCTION (discrete only)
  G_X(z) = E[z^X] = Sum_k P(X=k) z^k
  Useful for sums of random counts.
  G_{X+Y}(z) = G_X(z) G_Y(z)  if X, Y independent.

  LAPLACE TRANSFORM
  L_X(s) = E[e^{-sX}]  (for X >= 0)
  Connects to waiting-time analysis, reliability, queueing.
```

---

## Order Statistics and Extreme Values

For X_1, ..., X_n i.i.d. with CDF F(x):

```
  Order statistics: X_{(1)} <= X_{(2)} <= ... <= X_{(n)}
  (sorted sample)

  CDF of X_{(k)}: F_{(k)}(x) = Sum_{j=k}^{n} C(n,j) F(x)^j (1-F(x))^{n-j}

  Minimum X_{(1)}: P(X_{(1)} > x) = (1-F(x))^n -> e^{-n(1-F(x))}
  Maximum X_{(n)}: P(X_{(n)} <= x) = F(x)^n
```

**Extreme Value Theory**: The maximum of many i.i.d. r.v.s converges (after normalization) to one of three limiting distributions — Frechet, Weibull, or Gumbel (the max-stable distributions). This is the "other CLT" for extremes rather than averages.

---

## Decision Cheat Sheet

| Distribution | Use When |
|---|---|
| Bernoulli(p) | Single binary outcome |
| Binomial(n,p) | Fixed number of independent binary trials |
| Poisson(lambda) | Count of rare events in fixed time/space |
| Negative Binomial | Count data with overdispersion (variance > mean) |
| Exponential(lambda) | Continuous waiting times (memoryless) |
| Gamma(alpha, beta) | Sum of alpha exponentials; positive continuous |
| Normal(mu, sigma^2) | Large sums (CLT), measurement error, inference |
| Log-Normal | Multiplicative processes; prices, sizes |
| Beta(alpha, beta) | Prior on probabilities; proportions |
| Student-t(nu) | Inference with estimated variance; heavy tails |
| Cauchy | Heavy-tailed noise; unstable distributions |
| Pareto | Power-law phenomena; wealth, word frequency |

---

## Common Confusion Points

**"Density f(x) is a probability."**
No. For continuous distributions, P(X = x) = 0 for every x. The density f(x) is the Radon-Nikodym derivative of P_X w.r.t. Lebesgue measure. Probabilities come from integrating f over intervals. f(x) can be greater than 1 (e.g., Beta(5,1) near x=1 has f(1)=5).

**"Uncorrelated implies independent."**
Only for multivariate Normal. The classic counterexample: X ~ Uniform(-1,1), Y = X^2. Then Cov(X,Y) = E[X^3] - E[X]E[X^2] = 0, yet Y is completely determined by X.

**"The MGF always exists."**
The Cauchy distribution has no MGF (its tails are too heavy — E[e^{tX}] = inf for any t > 0). The characteristic function E[e^{itX}] always exists because |e^{itX}| = 1.

**"The Poisson distribution is an approximation."**
It is the exact distribution for counts in a Poisson process — events occurring at constant rate lambda with independent inter-arrival times. It is also the Binomial limit, but Poisson processes are physically real (radioactive decay, shot noise).

**"Higher moments always exist."**
For distributions with heavy tails (Pareto with alpha <= 2, Student-t with nu <= 2, Cauchy), variance is infinite. For Cauchy, even the mean is undefined (the integral doesn't converge absolutely).
