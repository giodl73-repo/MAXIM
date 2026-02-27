# Numerical Integration (Quadrature)

## The Big Picture

Numerical integration approximates Integral_a^b f(x) dx when the antiderivative is unknown or inconvenient. The key tradeoff: more evaluation points = more accuracy = more work.

```
+------------------------------------------------------------------+
|              NUMERICAL INTEGRATION LANDSCAPE                     |
+------------------------------------------------------------------+
|                                                                  |
|  NEWTON-COTES (equally-spaced)    GAUSSIAN QUADRATURE            |
|  +------------------------+        +-----------------------+     |
|  | Midpoint: O(h^2)       |        | n points: O(h^{2n})  |     |
|  | Trapezoid: O(h^2)      |        | (degree 2n-1 exact)  |     |
|  | Simpson's: O(h^4)      |        | OPTIMAL node placement|    |
|  | Composite rules        |        | Gauss-Legendre, etc.  |     |
|  +------------------------+        +-----------------------+     |
|                                                                  |
|  ADAPTIVE INTEGRATION              MONTE CARLO                  |
|  +------------------------+        +-----------------------+     |
|  | Refine where f complex |        | Dim-independent rate  |     |
|  | Error control          |        | O(n^{-1/2})           |     |
|  | scipy.integrate.quad   |        | High-dimensional ints |     |
|  +------------------------+        +-----------------------+     |
|                                                                  |
|  ROMBERG / EXTRAPOLATION                                        |
|  +------------------------+                                      |
|  | Richardson extrapolation|                                     |
|  | Higher order from lower |                                     |
|  +------------------------+                                      |
+------------------------------------------------------------------+
```

---

## Newton-Cotes Rules

**Midpoint rule** (degree 1):

```
  Integral_a^b f(x) dx ≈ (b-a) f((a+b)/2)

  Error: (b-a)^3/24 f''(xi)  for some xi in (a,b)
  On [a,b] with n subintervals (h = (b-a)/n):
  Composite midpoint: sum of n midpoint estimates.
  Global error: O(h^2) = O(n^{-2})
```

**Trapezoid rule** (degree 1, same order as midpoint):

```
  Integral_a^b f(x) dx ≈ (b-a)/2 * (f(a) + f(b))

  Error: -(b-a)^3/12 f''(xi)
  Composite trapezoid: (h/2)(f(x_0) + 2f(x_1) + ... + 2f(x_{n-1}) + f(x_n))
  Global error: O(h^2)

  Note: trapezoid and midpoint have similar accuracy. For smooth periodic functions
  on [0, 2pi] with the full period: trapezoid rule is SPECTRALLY accurate (exponential).
  This is the Euler-Maclaurin formula: error terms cancel.
```

**Simpson's rule** (degree 3):

```
  Integral_a^b f(x) dx ≈ (b-a)/6 * (f(a) + 4f((a+b)/2) + f(b))

  Exact for polynomials up to degree 3 (despite using only 3 points — "superconvergence").
  Error: -(b-a)^5/90 f^{(4)}(xi)
  Composite Simpson's (n even subintervals):
  (h/3)(f_0 + 4f_1 + 2f_2 + 4f_3 + 2f_4 + ... + 4f_{n-1} + f_n)
  Global error: O(h^4)

  "Free" order gain: Simpson's has 3 points and O(h^4) — better than 3-point formula
  naively gives. This is because Simpson's is the Newton-Cotes rule for degree 3
  but integrated exactly when evaluated at midpoints.
```

**Higher-order Newton-Cotes**: Use more equally-spaced points. But beyond n=7, the weights become negative (Gaussian quadrature avoids this).

---

## Gaussian Quadrature

**Core idea**: Choose BOTH nodes x_i AND weights w_i to exactly integrate polynomials up to degree 2n-1 (not just 2n-1 = n-1 as with n fixed nodes).

```
  Integral_{-1}^1 f(x) dx ≈ Sum_{i=1}^n w_i f(x_i)

  For n points: n free nodes + n free weights = 2n free parameters.
  Can make rule exact for polynomials of degree 0, 1, ..., 2n-1.
  (That is 2n conditions: 2n free parameters = system is exactly determined.)

  GAUSS-LEGENDRE NODES: zeros of Legendre polynomial P_n(x).
  GAUSS-LEGENDRE WEIGHTS: w_i = 2/((1-x_i^2)[P_n'(x_i)]^2)

  ACCURACY: Integral of any polynomial of degree <= 2n-1 is EXACT.
  For smooth f: exponential convergence in n.

  Example: n=5 points, 2*5-1 = 9th degree polynomials integrated exactly.
  Compare: n=5 Simpson's points -> 4th degree.
  Gaussian wins by orders of magnitude.
```

**Transform to general interval [a,b]**:

```
  x = ((b-a)t + (a+b)) / 2   maps t in [-1,1] to x in [a,b]
  Integral_a^b f(x) dx = (b-a)/2 * Integral_{-1}^1 f(((b-a)t+(a+b))/2) dt
```

**Variants of Gaussian quadrature**:

```
  GAUSS-CHEBYSHEV: weight w(x) = 1/sqrt(1-x^2)
  Nodes: Chebyshev zeros. Weights: pi/n (uniform!). Computed via FFT.

  GAUSS-LAGUERRE: Integral_0^inf f(x) e^{-x} dx ≈ Sum w_i f(x_i)
  Nodes: zeros of Laguerre polynomial L_n(x). For semi-infinite domains.

  GAUSS-HERMITE: Integral_{-inf}^{inf} f(x) e^{-x^2} dx ≈ Sum w_i f(x_i)
  Nodes: zeros of Hermite polynomial H_n(x). For infinite domains + Gaussian weight.
  Used in computing expectations under Normal distributions.

  CLENSHAW-CURTIS: Uses Chebyshev nodes. Slightly less accurate than Gauss-Legendre
  per node, but weights computed via FFT -> very fast for large n.
```

---

## Romberg Integration and Richardson Extrapolation

**Richardson extrapolation** uses results at two step sizes to cancel the leading error term:

```
  If Q(h) = Q_exact + C h^p + O(h^{p+2}):
  Q(h/2) = Q_exact + C (h/2)^p + O(h^{p+2})

  Combining: Q_exact = (2^p Q(h/2) - Q(h)) / (2^p - 1) + O(h^{p+2})

  One extrapolation step: order p -> order p+2.

  ROMBERG INTEGRATION:
  Start with trapezoid rule at h = b-a (2 function evaluations).
  Halve h repeatedly, computing composite trapezoid T(h/2^k).
  Apply Richardson extrapolation at each level.

  Romberg table:
  T(h)
  T(h/2)    R(1)
  T(h/4)    R(2)    R(3)
  ...

  R(k) values converge quickly. For smooth f: spectral convergence.
  Cost: n = 2^k + 1 function evaluations for level k.
```

---

## Adaptive Quadrature

Allocate more integration nodes where f is complex (high curvature):

```
  STRATEGY:
  1. Estimate error on interval [a,b]: e.g., compare Simpson and trapezoid results.
  2. If error > tolerance: recursively split [a,b] into two halves.
  3. If error <= tolerance: accept and move on.

  GLOBAL ERROR CONTROL:
  Distribute error tolerance over subintervals.
  Final error <= user-specified tolerance.

  IMPLEMENTATION (scipy.integrate.quad):
  Uses 15-point Gauss-Kronrod rule (order 15!) to estimate integral.
  Uses embedded 7-point rule to estimate error.
  Gauss-Kronrod: extends Gauss-Legendre points with additional points.
  Reuses function evaluations between different orders.

  GAUSS-KRONROD 15/7 rule:
  15 points: exactly integrates polynomials of degree <= 29.
  Error estimate: |I_15 - I_7|.
  Reliable for smooth f; adaptive subdivision handles discontinuities.
```

---

## Multi-Dimensional Integration

**Tensor product rules** (d dimensions):

```
  Integral_{[a,b]^d} f(x) dx ≈ Sum_{i_1,...,i_d} w_{i_1} ... w_{i_d} f(x_{i_1},...,x_{i_d})

  Using n points per dimension: n^d total points.
  For Gaussian quadrature in d dimensions: n^d evaluations.
  Accuracy: O(h^{2n}) still, but h = 1/n^{1/d} now.
  Effective rate: O(N^{-2n/d}) where N = n^d.

  CURSE OF DIMENSIONALITY: for d=10, n=5 -> 5^10 = ~10M evaluations.
  For d=20, n=5 -> 5^20 = ~10^14. Infeasible.
```

**Sparse grids** (mitigate curse):

```
  Smolyak sparse grid rule: O(n (log n)^{d-1}) points.
  Accuracy: O(h^p (log n)^{(d-1)p}) for p-th order rule.
  Practical for d <= 10-15.
```

---

## Monte Carlo Integration

For d >> 5, Monte Carlo is often the only practical method:

```
  BASIC MONTE CARLO:
  Integral_{[0,1]^d} f(x) dx ≈ (1/N) Sum_{i=1}^N f(X_i)
  where X_i ~ Uniform([0,1]^d) i.i.d.

  By LLN: converges to the true integral.
  By CLT: error ~ Normal(0, Var(f)/N) -> RMSE = sigma_f / sqrt(N)

  RATE: O(N^{-1/2}) -- INDEPENDENT OF DIMENSION d.
  This is why MC is used for high-dimensional problems.

  DRAWBACK: Slow rate O(N^{-1/2}).
  For 3 decimal digits: N = 10^6 evaluations.
  For 6 decimal digits: N = 10^{12} evaluations.
  MC is impractical for low-dimensional, high-precision integration.

  VARIANCE REDUCTION TECHNIQUES:
  1. Antithetic variables: pair X_i with 1-X_i. Negative correlation reduces variance.
  2. Control variates: if g(X) ≈ f(X) and Integral g is known analytically:
     f_controlled = f(X) - c*(g(X) - E[g])  (choose c to minimize variance)
  3. Importance sampling (see below)
  4. Stratified sampling: divide [0,1]^d into subregions, sample each proportionally.
```

**Importance sampling**:

```
  GOAL: Efficiently estimate E_p[f(X)] = Integral f(x) p(x) dx

  If p(x) is concentrated (e.g., most mass in small region):
  Sample uniformly -> most samples contribute negligibly.

  IMPORTANCE SAMPLING:
  Choose proposal distribution q(x) that concentrates where |f(x) p(x)| is large.
  E_p[f(X)] = Integral f(x) p(x)/q(x) * q(x) dx = E_q[f(X) p(X)/q(X)]

  Estimator: (1/N) Sum f(X_i) p(X_i)/q(X_i)  where X_i ~ q

  Optimal q*: q*(x) proportional to |f(x)| p(x) (makes variance = 0 if sign of f known).

  APPLICATIONS:
  Rare event simulation (probability of failure)
  Bayesian posterior computation (SIS, sequential importance sampling)
  Off-policy reinforcement learning
```

**Quasi-Monte Carlo (QMC)**:

```
  Replace random samples with LOW-DISCREPANCY SEQUENCES
  (more evenly distributed than random).

  Halton sequences, Sobol sequences, lattice rules.

  RATE: O((log N)^d / N) for d-dimensional integration of smooth f.
  Better than MC: O(N^{-1}) vs. O(N^{-1/2}).
  But the constant (log N)^d can be large for large d.

  PRACTICAL: QMC beats MC for d <= 20 and N < 10^9 for smooth integrands.
  Beyond: random sampling is hard to beat without structure exploitation.
```

---

## Integration in Probability and Physics

**Gaussian integrals (analytic)**:

```
  Integral_{-inf}^{inf} e^{-x^2/2} dx = sqrt(2 pi)
  Integral_{-inf}^{inf} x^{2n} e^{-x^2/2} dx = (2n-1)!! sqrt(2 pi)   (double factorial)

  Multivariate: Integral_{R^n} exp(-x^T A x / 2) dx = (2pi)^{n/2} / sqrt(det A)
  (A positive definite)

  These are the foundation of Gaussian quadrature (Gauss-Hermite uses these weights).
  In statistics: normalizing constants for Gaussian posteriors.
```

**Path integrals (physics)** — the ultimate high-dimensional integration problem:

```
  Feynman path integral: Z = Integral [Dx(t)] exp(iS[x]/hbar)
  An integral over ALL PATHS from initial to final state.
  The "space" is infinite-dimensional: each path x(t) is a point in function space.

  THE NUMERICAL CHALLENGE:
  Direct integration is impossible (infinite-dimensional). Three escape routes:

  1. WICK ROTATION (imaginary time):
     Replace t → -iτ, turning oscillatory exp(iS) into decaying exp(-S_E).
     The Euclidean action S_E makes the integrand a proper probability density.
     NOW it is a well-defined Monte Carlo problem: sample field configurations
     from P(config) ∝ exp(-S_E), compute observables as MC averages.

  2. LATTICE QCD — the flagship application:
     Discretize spacetime on a 4D hypercubic lattice (e.g., 64^3 × 128 sites).
     Each "sample" = full gauge field configuration (SU(3) matrix per link).
     Sampling: Hybrid Monte Carlo (HMC) — molecular dynamics + Metropolis accept/reject.
     Cost: O(10^{18}) FLOPs per configuration. Top-500 supercomputer scale.
     This is the most computationally expensive Monte Carlo application in science,
     and the only first-principles method for computing hadron masses, strong coupling α_s, etc.

  3. STATIONARY PHASE / SADDLE POINT:
     Approximate by expanding around the classical path (extremum of S).
     Gaussian integral around the saddle → determinant of the fluctuation operator.
     This connects to complex analysis (contour deformation, steepest descent).
```

The connection to this module: lattice QCD IS Monte Carlo integration (section above) applied to a ~10^7-dimensional integral. Importance sampling, Markov chain sampling (HMC), and variance reduction all apply directly. The Metropolis algorithm from the MC section is the accept/reject step in HMC.

---

**Differentiating through integrals — the AD connection.** Integration and differentiation are dual operations, and AD can differentiate through numerical integration. If a loss function involves an integral (or an ODE solve, which is an integral in disguise), reverse-mode AD computes dL/dp by running the ODE solver backward via the adjoint method (see 06-ODES and 09-SCIENTIFIC-COMPUTING). This is the foundation of neural ODEs: define a model as an ODE, integrate forward with an adaptive solver, and differentiate the loss through the entire integration via the adjoint — all at O(cost of forward solve) regardless of the number of ODE time steps.

---

## Decision Cheat Sheet

| Situation | Method | Notes |
|---|---|---|
| 1D, smooth f, high accuracy | Gauss-Legendre (n=5-20) | Spectral convergence |
| 1D, smooth f, error control | scipy.integrate.quad | Adaptive Gauss-Kronrod |
| 1D, general/unknown f | Composite Simpson or Romberg | Reliable, automatic |
| 1D, periodic function | Composite trapezoid (full period) | Spectral accuracy |
| d <= 5, smooth f | Sparse grids | Better than MC per eval |
| d > 10, any f | Monte Carlo | Dim-independent rate |
| High precision needed, high-d | Quasi-Monte Carlo (Sobol) | Better constant than MC |
| E_p[f(X)] with rare events | Importance sampling | Variance reduction |
| f has singularities | Adaptive quadrature | Handles splits automatically |

---

## Common Confusion Points

**"More quadrature points always help."**
Gaussian quadrature with n points integrates degree-2n-1 polynomials exactly. For functions with singularities or low smoothness, spectral convergence breaks down and the optimal strategy is adaptive integration (split near singularities).

**"Monte Carlo's O(sqrt(N)) rate is too slow."**
Slow per function evaluation, but function evaluations can be parallelized trivially. For high-dimensional problems (d > 10), MC outperforms deterministic methods because the curse of dimensionality makes grid-based methods exponentially worse. For N = 10^6 (easily parallelized on GPU), error is ~0.001 for reasonably-behaved f.

**"Romberg integration is obsolete."**
Romberg with the trapezoid rule is still excellent for smooth 1D integrals where evaluations are cheap. The automatic error control via Richardson extrapolation is simple to implement and efficient. It is superseded by adaptive Gauss-Kronrod for general purposes but remains relevant for smooth periodic functions.

**"Quasi-Monte Carlo always beats Monte Carlo."**
QMC beats MC for smooth, moderate-dimensional problems (d <= 20). For very high dimensions (d = 100+), the log(N)^d factor dominates. For functions with discontinuities or heavy tails, QMC's theoretical guarantees weaken. Practical choice depends on the integrand's smoothness and the dimension.
