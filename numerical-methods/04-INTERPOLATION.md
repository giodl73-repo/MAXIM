# Interpolation and Approximation

## The Big Picture

Interpolation constructs a function passing through given data points. Approximation finds a "best" function that approximately fits data. Both are foundational for integrating functions, solving ODEs, and representing smooth data.

```
+------------------------------------------------------------------+
|              INTERPOLATION AND APPROXIMATION LANDSCAPE           |
+------------------------------------------------------------------+
|                                                                  |
|  DATA: (x_0, y_0), ..., (x_n, y_n)                             |
|                                                                  |
|  POLYNOMIAL INTERPOLATION          PIECEWISE / SPLINES           |
|  +------------------------+        +--------------------+        |
|  | Lagrange interpolation |        | Cubic splines      |        |
|  | Newton's divided diff  |        | B-splines          |        |
|  | Runge's phenomenon!    |        | NURBS              |        |
|  +------------------------+        +--------------------+        |
|                                                                  |
|  CHEBYSHEV APPROXIMATION           SCATTERED DATA                |
|  +------------------------+        +--------------------+        |
|  | Minimax approximation  |        | Radial basis funcs |        |
|  | Exponential convergence|        | Kriging / GPs      |        |
|  | for smooth functions   |        | Natural neighbor   |        |
|  +------------------------+        +--------------------+        |
|                                                                  |
|  BEST APPROXIMATION (L^2)          REGRESSION (noisy data)      |
|  Least squares polynomial          (see 07-REGRESSION-MODELS)   |
|  Fourier series, wavelets                                       |
+------------------------------------------------------------------+
```

---

## Polynomial Interpolation

**Fundamental theorem**: Given n+1 distinct points (x_0, y_0), ..., (x_n, y_n), there is exactly one polynomial of degree <= n passing through all of them.

**Lagrange form**:

```
  p_n(x) = Sum_{i=0}^n y_i L_i(x)

  Where L_i(x) = Product_{j!=i} (x - x_j) / (x_i - x_j)
  (Lagrange basis polynomial: L_i(x_j) = delta_{ij})

  Good for theoretical analysis. Computationally: O(n^2) to evaluate.
```

**Newton's divided differences** (preferred computation):

```
  p_n(x) = c_0 + c_1(x-x_0) + c_2(x-x_0)(x-x_1) + ... + c_n Product_{i=0}^{n-1}(x-x_i)

  Divided differences:
  c_0 = y_0
  c_1 = [y_0, y_1] = (y_1 - y_0) / (x_1 - x_0)
  c_2 = [[y_0, y_1], [y_1, y_2]] = ([y_1,y_2] - [y_0,y_1]) / (x_2 - x_0)
  ...

  ADVANTAGE: Adding a new data point adds one new term — O(n) update.
  Horner's method evaluates in O(n) operations.
```

**Error of polynomial interpolation**:

```
  If f is (n+1)-times differentiable and p_n is the interpolating polynomial:
  f(x) - p_n(x) = f^{(n+1)}(xi) / (n+1)! * Product_{i=0}^n (x - x_i)

  For some xi between min(x_i) and max(x_i).

  The term omega(x) = Product_{i=0}^n (x - x_i) depends on the node placement.
  Minimizing max |omega(x)| over [a,b] leads to CHEBYSHEV NODES.
```

---

## Runge's Phenomenon — Why High-Degree Polynomials Fail

A critical warning: high-degree polynomial interpolation on equally-spaced nodes can oscillate wildly near the endpoints.

```
  EXAMPLE: Runge's function f(x) = 1 / (1 + 25 x^2) on [-1, 1].

  With n equally-spaced nodes:
  max|f(x) - p_n(x)| GROWS as n increases near x = +/-1.
  At n=20: the polynomial oscillates with amplitude >> 1 near the endpoints.
  This despite f being infinitely differentiable!

  CAUSE: omega(x) = Product(x - x_i) for equally-spaced nodes grows near endpoints.
  The interpolation error bound explodes.

  FIXES:
  1. Use Chebyshev nodes (optimal node placement, avoids Runge)
  2. Use piecewise polynomial interpolation (splines) with many low-degree pieces
  3. Use Chebyshev/Legendre basis for global approximation of smooth functions
```

---

## Chebyshev Nodes and Approximation

**Chebyshev nodes** minimize the Runge phenomenon:

```
  Chebyshev nodes on [-1, 1]:
  x_k = cos((2k+1)pi / (2(n+1)))   for k = 0, 1, ..., n

  These are the extrema of the Chebyshev polynomial T_{n+1}(x).
  They cluster near +/-1 (denser sampling near endpoints where polynomials oscillate).

  Chebyshev error bound:
  max|f - p_n| <= (1/(n+1)!) * (1/2)^n * max|f^{(n+1)}|  (on [-1,1])

  For analytic f (infinitely smooth): SPECTRAL CONVERGENCE (exponential in n).
  This is much faster than any algebraic rate.
```

**Chebyshev polynomials**:

```
  T_0(x) = 1, T_1(x) = x, T_n(x) = 2x T_{n-1}(x) - T_{n-2}(x)

  Properties:
  T_n(cos theta) = cos(n theta)   (connection to Fourier series)
  |T_n(x)| <= 1 for x in [-1,1]   (bounded)
  T_n(x) = 2^{n-1} x^n + ...     (leading coefficient 2^{n-1})
  T_n is the monic polynomial with smallest max-norm (divided by leading coefficient).

  BEST APPROXIMATION: Chebyshev expansion Sum_k c_k T_k(x) converges exponentially
  for analytic f. Coefficients computed by FFT (Chebyshev == Fourier on cos transform).
```

**Chebfun**: A MATLAB/Julia toolbox representing functions as their Chebyshev expansions. Arithmetic on functions (add, multiply, integrate, differentiate) is exact up to machine precision.

---

## Splines — Piecewise Polynomial Interpolation

Instead of one high-degree polynomial, use many low-degree polynomials joined at breakpoints (knots).

**Cubic spline**: piecewise cubic, C^2 across knots.

```
  Given nodes a = x_0 < x_1 < ... < x_n = b and values y_0, ..., y_n:

  On each interval [x_i, x_{i+1}]: a cubic S_i(x) = a_i + b_i(x-x_i) + c_i(x-x_i)^2 + d_i(x-x_i)^3

  CONDITIONS:
  Interpolation: S_i(x_i) = y_i, S_i(x_{i+1}) = y_{i+1}   (2n conditions)
  C^1 continuity: S_i'(x_{i+1}) = S_{i+1}'(x_{i+1})        (n-1 conditions)
  C^2 continuity: S_i''(x_{i+1}) = S_{i+1}''(x_{i+1})      (n-1 conditions)
  Total: 4n unknowns, 4n-2 conditions => 2 free conditions.

  NATURAL SPLINE: S''(x_0) = S''(x_n) = 0  (zero curvature at endpoints)
  NOT-A-KNOT: third derivative continuous at x_1 and x_{n-1}
  PERIODIC: for periodic data

  SOLUTION: Tridiagonal system for the second derivatives (O(n) by banded Cholesky).
```

**Error of cubic spline**:

```
  For f in C^4[a,b] with natural spline S:
  ||f - S||_inf <= C h^4 ||f^{(4)}||_inf   (h = max node spacing)

  4th order convergence: halve h, reduce error by factor 16.
  Better than linear interpolation (O(h^2)) and quadratic (O(h^3)).
```

**B-splines**: A basis for spline spaces that is computationally superior — and the same basis functions used in the finite element method (07-PDES):

```
  B-SPLINES IN THIS MODULE          B-SPLINES IN FEM (07-PDES)
  ──────────────────────────────────────────────────────────────────────
  B_{i,p}(x): basis function        φ_i(x): FEM basis function (same object)
  Interpolant: S(x) = Σ c_i B_i    FEM approx: u_h(x) = Σ U_j φ_j
  Coefficients c_i: fit data        Coefficients U_j: solve K U = F
  Local support on (x_i, x_{i+p+1}) Local support → sparse stiffness K
  K_{ij} = ∫ B_i' B_j' dx          Stiffness matrix (same integral!)
```

Linear B-splines (p=1) are the "hat functions" of standard FEM. Cubic B-splines (p=3) give C^2 FEM spaces with O(h^3) convergence in H^1. IGA (Isogeometric Analysis) uses the *same* NURBS that define the CAD geometry as the FEM basis — eliminating mesh generation entirely.

```
  B-splines of degree p: local support, non-negative, partition of unity.
  B_{i,p}(x): nonzero only on (x_i, x_{i+p+1})   (p+1 consecutive intervals)

  Every spline of degree p is a linear combination of B-splines:
  S(x) = Sum_i c_i B_{i,p}(x)

  ADVANTAGES:
  Stable computation (well-conditioned basis)
  Local support: changing c_i affects only nearby region
  Refinement: inserting a knot is O(n) (knot insertion algorithm)
  Used in CAD, finite element analysis, and computer graphics (NURBS)
```

---

## Scattered Data Interpolation

When data points are not on a regular grid:

**Radial Basis Functions (RBF)**:

```
  Interpolant: s(x) = Sum_{i=1}^n c_i phi(||x - x_i||)

  phi is a radial function:
  phi(r) = e^{-r^2/eps^2}    (Gaussian RBF -- infinitely smooth)
  phi(r) = sqrt(r^2 + eps^2) (multiquadric -- conditional positive definite)
  phi(r) = r^3               (cubic RBF -- conditionally positive definite)
  phi(r) = r^2 log r         (thin plate spline -- minimal bending energy)

  SOLVE FOR c: Phi c = y  where Phi_{ij} = phi(||x_i - x_j||)

  Phi is symmetric. For many phi choices: Phi is positive definite -> unique solution.

  INTERPOLATION vs. REGRESSION mode:
  Interpolation: pass through all points (n x n system)
  RBF regression: minimize ||s(x_i) - y_i||^2 + lambda * roughness (add smoothing)

  ADVANTAGES: Works in any dimension, any point distribution.
  DISADVANTAGES: Dense n x n system (O(n^3) direct solve, O(n^2) storage).
  For large n: use FMM (fast multipole method) for O(n log n) mat-vec products.
```

**Kriging (Gaussian Process Regression)**:

```
  Statistical interpolation assuming f is a realization of a GP:
  f(x) ~ GP(0, k(x, x'))   (zero mean GP with kernel k)

  Posterior mean (the interpolant):
  mu(x) = k(x, X)^T (K + sigma^2 I)^{-1} y

  where K_{ij} = k(x_i, x_j) and sigma^2 = noise variance.

  For exact interpolation (sigma^2 = 0): reduces to RBF interpolation
  with kernel = covariance function.

  Provides UNCERTAINTY QUANTIFICATION: posterior variance tells you where
  predictions are uncertain. This is what RBF interpolation lacks.

  Connection to probability-statistics/: see 04-STOCHASTIC-PROCESSES (GPs)
  and 06-BAYESIAN-STATISTICS (GP regression is Bayesian non-parametric regression).
```
  Cross-references: probability-statistics/04-STOCHASTIC-PROCESSES (GPs as stochastic processes)
  and probability-statistics/06-BAYESIAN-STATISTICS (GP regression as Bayesian nonparametric regression).

---

## Polynomial Approximation (vs. Interpolation)

Interpolation passes through the data. Approximation finds the "best" polynomial in some sense.

**Best L^inf (minimax) approximation**:

```
  Find p* in P_n (polynomials of degree <= n) minimizing max |f(x) - p(x)| on [a,b].

  Chebyshev's theorem: p* is characterized by having (n+2) points where the error
  alternates between +/- the maximum error (equioscillation).

  Remez algorithm: iterative method to find minimax polynomial.
  Converges quadratically.
```

**Best L^2 (least squares) approximation**:

```
  Find p* minimizing Integral |f(x) - p(x)|^2 w(x) dx

  With Legendre weight w=1: Legendre polynomial expansion.
  With Chebyshev weight w = 1/sqrt(1-x^2): Chebyshev expansion.

  These give the Fourier-type series for functions on [-1,1].
  Coefficients computed via orthogonality.
```

**Approximation theory and ML**: Neural networks are universal approximators (Stone-Weierstrass). The rate at which they approximate functions depends on smoothness (Barron's theorem: functions with bounded first moment of Fourier transform can be approximated by O(1/sqrt(n)) networks with n hidden units). This connects approximation theory to ML generalization. The practical question — "how do we optimize these approximators?" — is answered by automatic differentiation: reverse-mode AD (backpropagation) computes the gradient of a loss function through the entire approximation pipeline in O(cost of one evaluation), enabling gradient-based optimization of arbitrarily complex approximators (see 08-OPTIMIZATION and 09-SCIENTIFIC-COMPUTING for the AD machinery).

---

## Multivariate Interpolation

On grids: tensor product constructions (full tensor grid or sparse grids).

```
  TENSOR PRODUCT (full grid):
  f(x_1, ..., x_d) approximated on n^d grid points.
  Curse of dimensionality: n^d points needed.

  SPARSE GRIDS (Smolyak construction):
  Combine lower-dimensional grids to approximate d-dimensional functions.
  Points: O(n (log n)^{d-1}) instead of O(n^d).
  Error: O(n^{-p} (log n)^{(d-1)(p+1)}) vs. O(n^{-p}) for tensor product.
  Practical for d <= 10-15.

  ADAPTIVE SPARSE GRIDS:
  Refine grid only where function is non-smooth.
  Dimensionally adaptive methods (ADADRAW, SPARSE_GRIDS toolkit).
```

---

## Decision Cheat Sheet

| Situation | Method | Notes |
|---|---|---|
| Few points, smooth f, 1D | Cubic spline | C^2, O(h^4) error |
| Few points, analytic f, 1D | Chebyshev interpolation | Spectral convergence |
| High-degree polynomial, 1D | Chebyshev nodes | Avoid Runge phenomenon |
| Equal-spaced nodes, smooth f | Cubic spline | Not high-degree polynomial |
| CAD / geometric curves | B-spline / NURBS | Local control, stable |
| Scattered data, moderate n | Thin plate spline / RBF | Works in any dim |
| Scattered data with uncertainty | Gaussian process (kriging) | Provides uncertainty |
| High-dimensional function, d<=15 | Sparse grids | Avoid curse of dim |
| High-dimensional function, d>20 | Monte Carlo or neural surrogate | Curse wins otherwise |

---

## Common Confusion Points

**"More nodes = better polynomial interpolation."**
Only with smart node placement (Chebyshev nodes). Equally-spaced high-degree polynomial interpolation suffers Runge's phenomenon — oscillations grow near the endpoints. For equally-spaced nodes, use splines (many pieces of low degree) rather than one high-degree polynomial.

**"Spline interpolation is always smooth."**
C^2 splines (natural cubic splines) are smooth in the visual sense but not infinitely smooth — they have a discontinuous 3rd derivative at the knots. For truly smooth interpolation, use higher-order splines or Chebyshev expansions.

**"RBF interpolation always gives a unique solution."**
Only for specific radial functions. Thin plate splines require adding a polynomial correction term (conditional positive definiteness). Gaussian RBFs are unconditionally positive definite but can be ill-conditioned for small epsilon (the shape parameter eps must be chosen carefully: too large = smooth but inaccurate; too small = accurate but ill-conditioned).

**"Interpolation and regression are the same when there is no noise."**
Exact interpolation (zero residual) is a special case. Regression models prefer a smooth function that approximately fits data, accepting non-zero residuals in exchange for regularization (smoothness). For noisy data, interpolating every point over-fits; regression/smoothing splines are appropriate.
