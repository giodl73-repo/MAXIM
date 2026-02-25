# Limit Theorems

## The Big Picture

Limit theorems explain why statistical practice works. They are the mathematical bedrock under every sample mean, every confidence interval, and every SGD training run.

```
+------------------------------------------------------------------+
|                     LIMIT THEOREM HIERARCHY                      |
+------------------------------------------------------------------+
|                                                                  |
|  LAWS OF LARGE NUMBERS (LLN)                                     |
|  "Sample means converge to population means"                    |
|  Weak LLN: convergence in probability                           |
|  Strong LLN: convergence almost surely                          |
|                          |                                       |
|                          v                                       |
|  CENTRAL LIMIT THEOREM (CLT)                                    |
|  "The fluctuations around the mean are Normal"                  |
|  Rate of convergence: 1/sqrt(n)                                 |
|                          |                                       |
|                          v                                       |
|  DERIVED RESULTS                                                 |
|  Slutsky's theorem    -- combine convergence types              |
|  Continuous mapping   -- apply continuous functions             |
|  Delta method         -- CLT for transformed statistics         |
|  Berry-Esseen         -- quantify CLT error rate               |
|                                                                  |
+------------------------------------------------------------------+
|                  APPLICATIONS                                     |
|  Algorithm average-case analysis   Monte Carlo integration      |
|  SGD convergence theory            Confidence intervals         |
|  A/B test sample sizes             Extreme value theory         |
+------------------------------------------------------------------+
```

---

## Law of Large Numbers — Weak Form

**Setup**: X_1, X_2, ... i.i.d. with E[X_1] = mu < inf.

**Weak LLN** (Chebyshev version, requires finite variance):

```
  Define X_bar_n = (1/n) Sum_{i=1}^n X_i

  For all epsilon > 0:
  P(|X_bar_n - mu| > epsilon) -> 0   as n -> inf

  "Convergence in probability": the sample mean is close
  to mu with high probability, for large n.

  PROOF SKETCH (finite variance case):
  E[X_bar_n] = mu                        (linearity)
  Var(X_bar_n) = sigma^2 / n             (independence)
  By Chebyshev: P(|X_bar_n - mu| > eps) <= sigma^2 / (n eps^2) -> 0
```

The Chebyshev proof is short but needs finite variance. The LLN holds under much weaker conditions.

**Weak LLN (Kolmogorov, finite mean only)**:

Requires only E|X_1| < inf. The proof uses truncation and characteristic functions — the finiteness of the first moment is the essential condition.

---

## Law of Large Numbers — Strong Form

**Strong LLN** (Kolmogorov):

```
  P(X_bar_n -> mu) = 1                  (almost sure convergence)

  Stronger than weak: not just high probability for each n,
  but the entire sequence converges on a probability-1 set.

  Condition: E|X_1| < inf.
  If E|X_1| = inf, the sample mean can diverge almost surely.
```

**The Borel-Cantelli Lemma** (key tool in the proof):

```
  If Sum_{n=1}^inf P(A_n) < inf,
  then P(A_n occurs infinitely often) = 0.

  Conversely (with independence):
  If Sum P(A_n) = inf and A_n independent,
  then P(A_n occurs infinitely often) = 1.

  Intuition: "infinitely often" is controlled by the series of probabilities.
```

**Algorithm analysis connection**: Average-case complexity uses strong LLN. If an algorithm has expected cost mu per operation (with finite variance), and you run it on n independent inputs, the total cost converges to n*mu almost surely. Monte Carlo algorithms rely on this: the empirical average of f(X_i) converges to E[f(X)] for any f with finite expectation.

---

## Central Limit Theorem

**Setup**: X_1, X_2, ... i.i.d. with E[X_1] = mu, Var(X_1) = sigma^2 < inf.

**CLT**:

```
  sqrt(n) (X_bar_n - mu) / sigma  --d-->  Normal(0, 1)

  Equivalently:
  sqrt(n) (X_bar_n - mu)  --d-->  Normal(0, sigma^2)

  Or in CDF terms:
  P(sqrt(n)(X_bar_n - mu)/sigma <= x)  ->  Phi(x)

  Where Phi = standard normal CDF.
```

**Proof via characteristic functions**: This is the cleanest proof.

```
  Let Y_i = (X_i - mu)/sigma.  Then E[Y_i] = 0, E[Y_i^2] = 1.

  S_n = (1/sqrt(n)) Sum Y_i

  phi_{S_n}(t) = [phi_{Y}(t/sqrt(n))]^n

  Taylor expand phi_Y(t) = 1 - t^2/2 + o(t^2) near t=0
  (using E[Y]=0, E[Y^2]=1)

  phi_{S_n}(t) = [1 - t^2/(2n) + o(1/n)]^n  ->  e^{-t^2/2}

  And e^{-t^2/2} is the CF of Normal(0,1). QED.
```

**What the CLT says geometrically**: No matter what shape the original distribution has, summing n i.i.d. copies and centering/scaling produces something that looks increasingly Normal. The Normal is the attractor of the convolution semigroup.

---

## Berry-Esseen Theorem — Quantifying CLT Error

The CLT says convergence happens; Berry-Esseen says how fast:

```
  If E|X_1|^3 = rho < inf, then:

  sup_x |P(S_n <= x) - Phi(x)| <= C * rho / (sigma^3 * sqrt(n))

  Where C is a universal constant (best known: C < 0.4748).

  Rate: O(1/sqrt(n)).

  For n=100 with typical distributions: error ~ 0.05 or less.
  For n=1000: error ~ 0.015.

  This quantifies when CLT-based confidence intervals are accurate.
```

---

## Generalizations of the CLT

**Non-identically distributed (Lindeberg-Feller CLT)**:

```
  For independent (NOT necessarily identically distributed) X_i:
  The CLT holds if the Lindeberg condition holds:
  For all eps > 0:
  (1/s_n^2) Sum_i E[(X_i - mu_i)^2 * 1{|X_i - mu_i| > eps s_n}] -> 0

  Where s_n^2 = Sum_i Var(X_i).

  Informal: No single term dominates the variance of the sum.
```

**Heavy-tailed CLT (Stable distributions)**:

```
  If X has a heavy tail (|x|^{-alpha} decay, 0 < alpha < 2):
  The normalized sum S_n / n^{1/alpha} converges to an alpha-stable distribution.
  For alpha=2: recovers the Gaussian CLT.
  For alpha=1: sum / n*log(n) -> Cauchy.
  These are the Levy stable distributions.
```

---

## Slutsky's Theorem

**Slutsky**: If X_n -d-> X and Y_n -p-> c (constant), then:

```
  X_n + Y_n  --d-->  X + c
  X_n * Y_n  --d-->  cX
  X_n / Y_n  --d-->  X/c   (if c != 0)
```

**Why it matters**: Statistical estimators often involve plugging in estimated quantities. If you have a CLT for X_n and a consistent estimator Y_n -> c, you can combine them. Used constantly for t-statistics, estimated standard errors, etc.

**Example — Student t-statistic**:

```
  sqrt(n)(X_bar - mu)/sigma  --d-->  Normal(0,1)    (CLT)

  Sample standard deviation: s_n -> sigma in probability  (consistency)

  By Slutsky:
  sqrt(n)(X_bar - mu)/s_n  --d-->  Normal(0,1)/1 = Normal(0,1)

  (Exact finite-n distribution is t_{n-1}; CLT gives the limit.)
```

---

## Continuous Mapping Theorem

If X_n -d-> X and g is continuous (or continuous a.e. w.r.t. the law of X):

```
  g(X_n)  --d-->  g(X)

  Works for:
  - a.s. convergence -> a.s. convergence
  - in probability -> in probability
  - in distribution -> in distribution
```

**Example**: If X_n -d-> Normal(0,1), then X_n^2 -d-> Chi-squared(1).

---

## The Delta Method

The delta method applies the CLT + continuous mapping to derive asymptotic distributions for transformed statistics.

**Setup**: sqrt(n)(T_n - theta) -d-> Normal(0, sigma^2) and g is differentiable at theta.

```
  Delta method:
  sqrt(n)(g(T_n) - g(theta))  --d-->  Normal(0, [g'(theta)]^2 * sigma^2)

  Proof sketch: First-order Taylor expansion g(T_n) ≈ g(theta) + g'(theta)(T_n - theta)
  Then apply Slutsky.

  Multivariate version:
  sqrt(n)(g(T_n) - g(theta))  --d-->  Normal(0, gradient_g^T * Sigma * gradient_g)
```

**Example — log transform**:

```
  If sqrt(n)(X_bar - mu) --d-> Normal(0, sigma^2), then:
  sqrt(n)(log(X_bar) - log(mu)) --d-> Normal(0, sigma^2/mu^2)

  This gives asymptotic CI for log(mu): log(X_bar) ± z_{alpha/2} * s/(sqrt(n) * X_bar)
```

**Application — MLE asymptotics**: The delta method with the information inequality gives asymptotic distributions for functions of MLEs.

---

## Law of the Iterated Logarithm

Stronger than the CLT — tells you the exact rate of fluctuations in the almost sure limit:

```
  limsup_{n->inf}  S_n / sqrt(2n log log n)  =  sigma     a.s.
  liminf_{n->inf}  S_n / sqrt(2n log log n)  = -sigma     a.s.

  Where S_n = Sum_{i=1}^n (X_i - mu).

  The sample mean fluctuates at rate sqrt(log log n / n), which is
  slightly faster than 1/sqrt(n) but much slower than any power of n.
```

This is the "sharp" result beyond the CLT: the CLT tells you the distribution of fluctuations, the LIL tells you how large they get almost surely.

---

## Large Deviations Theory

While LLN and CLT describe typical behavior, large deviations theory quantifies the probability of rare events far from the mean.

```
  Cramer's theorem: For i.i.d. X_i with log-MGF Lambda(t) = log E[e^{tX}]:

  P(X_bar_n >= x)  ≈  exp(-n I(x))   for x > mu

  Where I(x) = sup_t {tx - Lambda(t)}  is the Legendre transform of Lambda.
  I(x) is called the rate function or Cramer transform.

  I(x) = 0 at x = mu, I(x) > 0 for x != mu, I is convex.
  Rate of exponential decay: e^{-n I(x)}.
```

**Connection to information theory**: The rate function I(x) is the KL divergence between the distribution "tilted" to have mean x and the original distribution. Large deviations and relative entropy are deeply related.

---

## Connection to Algorithm Analysis

The MIT TCS background makes this precise:

```
  PROBABILITY THEORY          ALGORITHM ANALYSIS
  ------------------          ------------------
  LLN convergence             Average-case cost converges
  CLT fluctuations            Variance of runtime
  Large deviations            Probability of worst-case behavior
  Hoeffding inequality        PAC learning sample complexity
  Markov/Chebyshev            Probability amplification (BPP)

  Specifically for randomized algorithms:
  - The LLN underlies why randomized rounding works
  - The CLT underlies why Monte Carlo gives sqrt(n) convergence
  - Large deviations bound failure probabilities for
    boosting (AdaBoost fails with probability exp(-n epsilon^2))
```

**Monte Carlo integration**: For f: R^d -> R and X ~ Uniform([0,1]^d):

```
  Integral f(x) dx = E[f(X)]  (by definition of uniform expectation)

  Estimator: (1/n) Sum f(X_i)  where X_i i.i.d. Uniform([0,1]^d)

  By CLT: error ~ Normal(0, Var(f(X))/n)
  RMSE ~ sigma_f / sqrt(n)

  Key insight: convergence rate is O(1/sqrt(n)) regardless of dimension d.
  Deterministic quadrature in d dimensions: O(n^{-k/d}) for k-smooth f.
  For d > 2k, Monte Carlo wins. For high-dimensional integration, Monte Carlo
  is often the only viable method.
```

---

## Decision Cheat Sheet

| Theorem | What It Gives | Conditions |
|---|---|---|
| Weak LLN | X_bar -> mu in probability | E|X| < inf |
| Strong LLN | X_bar -> mu a.s. | E|X| < inf |
| CLT (iid) | Gaussian fluctuations at rate 1/sqrt(n) | Finite variance |
| Berry-Esseen | CLT error O(1/sqrt(n)) | Finite 3rd moment |
| Lindeberg-Feller | CLT for non-iid | Lindeberg condition |
| Slutsky | Combine distribution limits | One limit is constant |
| Continuous mapping | Apply continuous functions to limits | g continuous a.e. |
| Delta method | CLT for smooth transformations | g differentiable at theta |
| Large deviations | Exponential tail bounds | MGF finite near 0 |
| Hoeffding | Exponential bound for bounded r.v.s | Bounded X_i |

---

## Common Confusion Points

**"The CLT says everything is Normal."**
The CLT applies to *sums* (or means) of many i.i.d. terms with finite variance. Individual observations need not be Normal. The sum of 30+ Poisson, exponential, or binomial r.v.s will be approximately Normal; a single observation will not be.

**"Strong LLN is strictly stronger than weak LLN."**
Yes: a.s. convergence implies convergence in probability, but not vice versa. The distinction matters for dependent observations and processes — a sample path that converges a.s. is qualitatively different from one that merely converges in probability.

**"The Berry-Esseen rate means CLT is slow."**
O(1/sqrt(n)) is actually quite fast in practice. For n=100, the CLT approximation is accurate to within ~5% in the tails. For n=1000, it's ~1.5%. The bound is worst-case; for symmetric distributions the error is often much smaller.

**"Slutsky applies to any sequence."**
The c in Slutsky must be a constant, not a random variable. If Y_n -d-> Y for a non-degenerate random variable Y, you cannot simply write X_n + Y_n -d-> X + Y (this would need joint convergence of (X_n, Y_n)).
