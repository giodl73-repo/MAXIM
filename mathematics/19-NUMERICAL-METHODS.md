# Numerical Methods — Complete Reference

## The Big Picture

```
NUMERICAL METHODS
═══════════════════════════════════════════════════════════════════════════

  FLOATING POINT              ROOT FINDING                  LINEAR SYSTEMS
  ─────────────               ────────────                  ─────────────
  IEEE 754 representation     Bisection, IVT                Gaussian elimination
  Machine epsilon ε_mach      Newton-Raphson (quadratic)    LU decomposition
  Rounding, overflow/underflow Secant, Brent's method       Cholesky (SPD)
  Catastrophic cancellation   Fixed-point iteration         Iterative (CG, GMRES)
  Condition number κ(A)       Convergence orders            Sparse methods

  INTERPOLATION &             DIFFERENTIATION               INTEGRATION (QUADRATURE)
  APPROXIMATION               & DERIVATIVES                 ──────────────────────
  ─────────────────           ─────────────                 Riemann → Trapezoidal
  Polynomial interpolation    Finite differences            Simpson's rule
  Newton's divided differences Forward/central/backward     Gaussian quadrature
  Spline interpolation        Richardson extrapolation      Adaptive quadrature
  Least squares, regression   Automatic differentiation     Monte Carlo integration

  ODEs                        PDEs                          EIGENVALUE PROBLEMS
  ────                        ────                          ────────────────────
  Euler's method              Finite differences            Power iteration
  Runge-Kutta (RK4)           Finite element method         QR algorithm
  Stiffness, implicit methods Spectral methods              Arnoldi / Lanczos
  Adaptive step control       Method of lines               Rayleigh quotient

  ┌─────────────────────────────────────────────────────────────────────┐
  │  Core theme: approximate continuous mathematics on discrete,        │
  │  finite-precision machines — understand and control the error       │
  └─────────────────────────────────────────────────────────────────────┘
```

**Why it matters**: Every scientific computation, simulation, ML training loop,
physics engine, and signal processing pipeline runs numerical methods under the hood.
Understanding floating-point pitfalls, conditioning, stability, and convergence rates
is what separates algorithms that work from ones that silently produce garbage.
MIT background means you've seen some of this; focus here is on the full picture
with error analysis as the unifying thread.

---

## 1. Floating-Point Arithmetic

### 1.1 IEEE 754 Representation

```
FLOATING-POINT NUMBER: (−1)ˢ · m · 2ᵉ

         sign  exponent    significand (mantissa)
float32:  1 bit   8 bits       23 bits   → ~7 decimal digits
float64:  1 bit  11 bits       52 bits   → ~15-16 decimal digits
float16:  1 bit   5 bits       10 bits   → ~3-4 decimal digits (ML training)
bfloat16: 1 bit   8 bits        7 bits   → ~2-3 digits (Google TPU, large range)

BIAS REPRESENTATION of exponent:
  float64: stored exponent E = e + 1023 (bias)
  Actual exponent range: −1022 to +1023 (E=0 and E=2047 reserved)

SPECIAL VALUES:
  E = 2047, mantissa = 0:  ±∞ (1/0, overflow)
  E = 2047, mantissa ≠ 0:  NaN (0/0, ∞−∞, sqrt(−1))
  E = 0, mantissa ≠ 0:     subnormal (gradual underflow near 0)
  NaN ≠ NaN (NaN comparisons always false — common bug)

MACHINE EPSILON:
  ε_mach = 2⁻⁵² ≈ 2.22×10⁻¹⁶  (float64)
  ε_mach = 2⁻²³ ≈ 1.19×10⁻⁷   (float32)
  ε_mach = 2⁻¹⁰ ≈ 9.77×10⁻⁴   (float16)

  Definition: smallest ε s.t. fl(1 + ε) > 1.
  fl(x) = x(1 + δ), |δ| ≤ ε_mach  (relative rounding error of any operation)

UNIT IN THE LAST PLACE (ULP): distance to next representable float.
  ulp(x) ≈ ε_mach · |x|
```

### 1.2 Rounding Modes and Error Accumulation

```
IEEE 754 ROUNDING MODES:
  Round to nearest (ties to even): default, minimizes bias
  Round toward +∞ / −∞: used in interval arithmetic
  Round toward zero: truncation

FLOATING-POINT ARITHMETIC GUARANTEE:
  For IEEE 754 operations +, −, ×, ÷, √:
    fl(x ⊕ y) = (x ⊕ y)(1 + δ),  |δ| ≤ ε_mach
  Each operation has at most 1 ULP error.

ERROR ACCUMULATION:
  n additions of numbers of similar magnitude: error ~ √n · ε_mach · x  (random walk)
  Worst case: n · ε_mach · x  (systematic)
  Compensated summation (Kahan): error ~ O(ε_mach) regardless of n  ← crucial for ML loss

CATASTROPHIC CANCELLATION:
  a - b where a ≈ b: relative error amplified enormously.
  Example: x² - 1 near x=1 → use (x-1)(x+1) instead.
  cos(x) - 1 near x=0 → use -2sin²(x/2).
  Quadratic formula: b² >> 4ac, -b + √(b²-4ac) ≈ 0 → use -2c/(b + √(b²-4ac)).
```

<!-- @editor[bridge/P2]: Missing connection between catastrophic cancellation and practical numerical libraries — numpy's np.expm1(x) and np.log1p(x) exist precisely to avoid cancellation for x≈0. Also: fused multiply-add (FMA) instruction computes a*b+c with a single rounding error instead of two, relevant for performance-critical inner product computations in ML. -->

### 1.3 Condition Number

```
CONDITION NUMBER of a problem: ratio of relative change in output to relative change in input.
  κ = |relative output change| / |relative input change|

  Well-conditioned: κ ~ 1  (small input error → small output error)
  Ill-conditioned: κ >> 1  (small input error → large output error)
  Singular: κ = ∞

CONDITION NUMBER OF A MATRIX:
  κ(A) = ‖A‖ · ‖A⁻¹‖ = σ_max / σ_min   (using operator 2-norm + SVD)
  For Ax = b: relative error in x ≤ κ(A) · (relative error in b + relative error in A)
  κ(A) = 1: orthogonal matrix (ideal)
  κ(A) large: nearly singular, solution unreliable

NUMERICAL RANK: number of singular values above threshold (not actual rank).
  Used in low-rank approximation, truncated SVD.

RULE OF THUMB:
  If κ(A) ~ 10ᵏ, expect to lose ~k decimal digits of accuracy in solution.
  κ ~ 10¹² with float64 (15 digits) → ~3 reliable digits in solution.
```

---

## 2. Root Finding

### 2.1 Bisection Method

```
PROBLEM: Find x* with f(x*) = 0.
ASSUMPTION: f continuous on [a,b], f(a)·f(b) < 0  (IVT guarantees root).

ALGORITHM:
  While (b−a)/2 > tol:
    c = (a+b)/2
    if f(c) = 0: return c
    if sign(f(a)) = sign(f(c)): a = c
    else: b = c

CONVERGENCE: Linear (order 1). Error halves each step.
  After n steps: |xₙ − x*| ≤ (b−a)/2ⁿ
  Steps to get tolerance ε: n = log₂((b−a)/ε)
  Guaranteed but slow.

PROS: always converges, no derivative needed, simple.
CONS: slow (linear), requires sign change, 1D only.
```

### 2.2 Newton-Raphson Method

```
IDEA: linearize f at current point, solve linear equation.
  x_{n+1} = xₙ − f(xₙ)/f'(xₙ)

GEOMETRIC INTERPRETATION: xₙ₊₁ = x-intercept of tangent line at (xₙ, f(xₙ)).

CONVERGENCE: Quadratic (order 2) near simple root x*.
  |x_{n+1} − x*| ≤ C · |xₙ − x*|²
  where C = |f''(x*)|/(2|f'(x*)|)
  → doubles correct digits each iteration (~10 iterations for 64-bit precision from decent start).

MULTIPLE ROOTS: Convergence degrades to linear at root of multiplicity m.
  Fix: use x_{n+1} = xₙ − m·f(xₙ)/f'(xₙ)  or  Schröder's method.

FAILURES: diverge if f'(xₙ) ≈ 0, cycle if bad starting point, slow for flat functions.

NEWTON IN ℝⁿ (nonlinear systems):
  F: ℝⁿ → ℝⁿ,   x_{k+1} = xₖ − J_F(xₖ)⁻¹ F(xₖ)
  J_F = Jacobian (n×n matrix). Solve J·Δx = −F at each step (never invert J explicitly).
  Same quadratic convergence. Cost per step: O(n³) LU factorization.

QUASI-NEWTON (Broyden): update approximate Jacobian cheaply.
  Avoids re-computing/factoring full Jacobian.
```

<!-- @editor[bridge/P2]: Newton-Raphson in ℝⁿ is the foundation of optimization — L-BFGS and trust-region methods are quasi-Newton methods for unconstrained optimization (scipy.optimize.minimize). The connection between Newton's method for systems and Newton's method for optimization (minimizing f = solving ∇f = 0) should be explicit. Also: inexact Newton (solve J·Δx = −F only approximately) is the basis for practical implementations at scale. -->

### 2.3 Other Root-Finding Methods

```
SECANT METHOD:
  x_{n+1} = xₙ − f(xₙ)·(xₙ − xₙ₋₁)/(f(xₙ) − f(xₙ₋₁))
  Finite difference approximation of Newton (no f' needed).
  Convergence: superlinear, order φ = (1+√5)/2 ≈ 1.618 (golden ratio).

BRENT'S METHOD (combination):
  Combines bisection (safe) + secant/inverse quadratic interpolation (fast).
  Guaranteed to converge, fast when possible.
  Industry standard for scalar root-finding in practice.

FIXED-POINT ITERATION:
  Rewrite f(x)=0 as x = g(x).  Iterate xₙ₊₁ = g(xₙ).
  Converges iff |g'(x*)| < 1  (contractive mapping, Banach fixed-point theorem).
  Convergence order = 1 (linear) if g'(x*) ≠ 0.
  Choice of g matters enormously: same equation, different g, different convergence.

MÜLLER'S METHOD: fits parabola through 3 points. Finds complex roots. Order ~1.84.

CONVERGENCE ORDERS SUMMARY:
  Method             Order    Cost/step     Notes
  ───────────────────────────────────────────────────────
  Bisection          1        1 eval        Guaranteed
  Fixed-point        1        1 eval        Need |g'|<1
  Secant             1.618    1 eval        No derivative
  Newton             2        1 eval + 1 deriv  Need good start
  Newton (mult m)    1→2      with Schröder fix
  Halley             3        2 evals + 2 derivs  Overkill usually
```

---

## 3. Solving Linear Systems

### 3.1 Direct Methods — Gaussian Elimination

```
PROBLEM: Solve Ax = b,  A ∈ ℝⁿˣⁿ.

GAUSSIAN ELIMINATION: O(n³/3) operations.
  Forward elimination: reduce A to upper triangular U.
  Back substitution: solve Ux = b' in O(n²).

LU DECOMPOSITION: A = L·U  (lower · upper triangular)
  Factorize once O(n³): solve Ly = b (forward sub O(n²)), Ux = y (back sub O(n²)).
  Efficient for multiple right-hand sides.

PARTIAL PIVOTING: permute rows to put largest element in pivot position.
  PA = LU  (P = permutation matrix)
  Improves numerical stability. Essential in practice.
  Complete pivoting (rows + columns): more stable but 2× slower, rarely needed.

CHOLESKY DECOMPOSITION: A = LLᵀ  (A symmetric positive definite)
  A = LLᵀ: L is lower triangular with positive diagonal.
  2× faster than LU: ~n³/6 ops. Automatically stable (no pivoting needed).
  Applications: normal equations, SPD systems (FEM, GP regression).

SPECIAL STRUCTURE EXPLOITATION:
  Banded matrix (bandwidth b): O(nb²) — sparse ODE BVPs
  Tridiagonal (b=1): O(n) — Thomas algorithm
  Toeplitz: O(n log² n) — signal processing, convolutions
  Sparse general: fill-in problem → reorder (AMD, Nested Dissection) before factoring
```

<!-- @editor[bridge/P2]: Missing the connection to scipy.linalg and numpy.linalg — scipy.linalg.lu, scipy.linalg.cho_factor/cho_solve, and the LAPACK routines they wrap (dgesv, dpotrf, dgetrf). In practice: numpy.linalg.solve uses LAPACK dgesv (LU+pivoting). When to use scipy vs numpy for linear systems. Also worth noting: for n > ~5000, direct methods become impractical for dense matrices and GPU GEMM (cuBLAS) is the go-to. -->

### 3.2 Conditioning and Stability

```
FORWARD ERROR: ‖x̂ − x‖/‖x‖ ≤ κ(A) · ‖r‖/(‖A‖‖x̂‖)
  where r = b − Ax̂ is the residual.

BACKWARD ERROR: how big must perturbation be to make x̂ exact?
  Small backward error = numerically stable algorithm.
  Gaussian elimination with partial pivoting: backward stable in practice
  (theoretical growth factor 2ⁿ⁻¹ but exponential growth never observed).

ITERATIVE REFINEMENT: compute r = b − Ax̂, solve AΔx = r, update x̂ += Δx.
  Each iteration multiplies error by ~κ(A)·ε_mach.
  Can improve accuracy to ~ε_mach regardless of conditioning (in mixed precision).
```

### 3.3 Iterative Methods for Large Systems

Direct O(n³) methods impossible for n ~ 10⁶ (PDE discretizations).

```
STATIONARY ITERATIVE METHODS:
  Jacobi:       x^(k+1)ᵢ = (bᵢ − Σ_{j≠i} aᵢⱼ xⱼ^k) / aᵢᵢ
  Gauss-Seidel: use updated values immediately.
  SOR (successive over-relaxation): Gauss-Seidel + parameter ω ∈ (0,2).
  Converge iff spectral radius ρ(iteration matrix) < 1.
  Slow for large systems.

KRYLOV SUBSPACE METHODS:
  Conjugate Gradient (CG): for SPD systems.
    Minimizes ‖x−x*‖_A over Krylov subspace Kₖ = span{r₀, Ar₀, ..., A^(k-1)r₀}
    Convergence: ‖eₖ‖_A ≤ 2((√κ−1)/(√κ+1))ᵏ ‖e₀‖_A
    k iterations to achieve tolerance ε: k ~ (√κ/2) log(2/ε)
    O(n) per iteration (just matrix-vector multiply for sparse A).

  GMRES: for non-symmetric systems.
    Minimizes residual over Krylov subspace.
    Full GMRES: O(k²n) — stores all Krylov vectors.
    Restarted GMRES(m): bounded memory, may stagnate.

  BiCGSTAB: for non-symmetric, more memory-efficient than GMRES.

PRECONDITIONING: P⁻¹Ax = P⁻¹b  (P ≈ A, easy to invert)
  Reduces effective condition number.
  Incomplete LU (ILU), algebraic multigrid (AMG), domain decomposition.
  Preconditioning is an art — problem-specific.

MULTIGRID: O(n) for elliptic PDEs. Smoothing + coarse-grid correction.
  V-cycle, W-cycle. Geometric vs. algebraic multigrid.
  Best asymptotic complexity for many PDE problems.
```

---

## 4. Interpolation and Approximation

### 4.1 Polynomial Interpolation

```
PROBLEM: Find polynomial p(x) of degree ≤ n passing through (x₀,y₀),...,(xₙ,yₙ).

EXISTENCE AND UNIQUENESS: Unique polynomial of degree ≤ n through n+1 distinct points.

LAGRANGE INTERPOLATION:
  p(x) = Σᵢ yᵢ Lᵢ(x)
  Lᵢ(x) = Π_{j≠i} (x−xⱼ)/(xᵢ−xⱼ)
  O(n²) evaluation.

NEWTON'S DIVIDED DIFFERENCES:
  p(x) = [y₀] + [y₀,y₁](x−x₀) + [y₀,y₁,y₂](x−x₀)(x−x₁) + ⋯
  [yᵢ,...,yⱼ]: divided difference (recursive formula).
  Add new points cheaply: O(n) to add one more point.
  Barycentric form: O(n) evaluation, numerically stable.

INTERPOLATION ERROR:
  f(x) − p(x) = f^(n+1)(ξ)/(n+1)! · Π(x − xᵢ)
  Error depends on: smoothness of f, node placement, degree n.
```

### 4.2 Runge's Phenomenon and Chebyshev Nodes

```
RUNGE'S PHENOMENON:
  Equally spaced nodes + high-degree polynomial = large oscillations near endpoints.
  f(x) = 1/(1+25x²) on [−1,1]: error INCREASES as n increases with uniform nodes.

FIX: CHEBYSHEV NODES:
  xₖ = cos((2k+1)π/(2n+2)),  k = 0,...,n   (roots of Chebyshev polynomial Tₙ₊₁)
  Minimize ‖Π(x−xᵢ)‖∞ over all node choices.
  Error bound: ‖f − pₙ‖∞ ≤ (1/2ⁿ) · ‖f^(n+1)‖∞/(n+1)!
  Nearly optimal approximation.

CHEBYSHEV POLYNOMIALS:
  Tₙ(cos θ) = cos(nθ)
  T₀=1, T₁=x, Tₙ₊₁ = 2x·Tₙ − Tₙ₋₁
  |Tₙ(x)| ≤ 1 on [−1,1].
  Tₙ has leading coefficient 2ⁿ⁻¹.
  Extremal property: Tₙ/2ⁿ⁻¹ is the monic polynomial of degree n with smallest ∞-norm.
```

### 4.3 Spline Interpolation

```
PROBLEM WITH HIGH-DEGREE POLYNOMIALS: unstable, oscillatory.
FIX: piecewise low-degree polynomials ("splines").

CUBIC SPLINE:
  Piecewise cubic on each interval [xᵢ, xᵢ₊₁].
  Conditions:
    • Interpolates data: S(xᵢ) = yᵢ
    • Continuous first derivatives: S'(xᵢ⁺) = S'(xᵢ⁻)
    • Continuous second derivatives: S''(xᵢ⁺) = S''(xᵢ⁻)
  → 4(n−1) unknowns, 4(n−1)−2 conditions from continuity → 2 more needed.
  Boundary conditions: natural (S''=0 at ends), clamped (S'=slope at ends), not-a-knot.

TRIDIAGONAL SYSTEM: moments Mᵢ = S''(xᵢ) satisfy tridiagonal linear system → O(n).

B-SPLINES: basis splines — numerically stable, used in NURBS (CAD/CAM), fonts (TrueType).
BEZIER CURVES: de Casteljau algorithm — subdivision, convex hull property. PostScript, SVG.

NATURAL CUBIC SPLINE: minimizes ∫(S'')² dx among all interpolants — smoothest.
```

### 4.4 Least Squares Approximation

```
OVERDETERMINED SYSTEM: m equations, n unknowns (m >> n).
  Ax ≈ b,  minimize ‖Ax − b‖₂²

NORMAL EQUATIONS: AᵀAx = Aᵀb
  Condition number κ(AᵀA) = κ(A)².  Can be catastrophically ill-conditioned.

QR DECOMPOSITION (preferred): A = QR (Q orthogonal, R upper triangular)
  QRx = b → Rx = Qᵀb → back-substitute. κ(R) = κ(A).
  Algorithms: Householder reflections (stable), Gram-Schmidt (less stable).
  O(mn²) for m×n matrix.

TRUNCATED SVD: A = UΣVᵀ, keep top k singular values.
  Best rank-k approximation (Eckart-Young theorem): ‖A − Aₖ‖₂ = σₖ₊₁.
  Used in PCA, dimensionality reduction, denoising.

RIDGE REGRESSION (Tikhonov regularization):
  min ‖Ax−b‖² + λ‖x‖²  →  (AᵀA + λI)x = Aᵀb
  Adds λI to diagonal → better conditioning, biased estimator.
```

---

## 5. Numerical Differentiation

### 5.1 Finite Difference Formulas

```
FORWARD DIFFERENCE: f'(x) ≈ (f(x+h) − f(x))/h
  Error: O(h)  (first-order)

BACKWARD DIFFERENCE: f'(x) ≈ (f(x) − f(x−h))/h
  Error: O(h)

CENTRAL DIFFERENCE: f'(x) ≈ (f(x+h) − f(x−h))/(2h)
  Error: O(h²)  ← preferred for smooth functions

SECOND DERIVATIVE:
  f''(x) ≈ (f(x+h) − 2f(x) + f(x−h))/h²   Error: O(h²)

GENERAL STENCIL COEFFICIENTS: from Taylor expansion or polynomial interpolation.
  Can derive O(h⁴), O(h⁶), ... formulas using more points.

STEP SIZE DILEMMA:
  Truncation error: O(hᵖ) → want h small
  Round-off error: O(ε_mach/h) → want h large
  Optimal h: minimize total error.
  For central difference: hₒₚₜ ~ (ε_mach)^(1/3) ~ 10⁻⁵ for float64.
  Total error at hₒₚₜ ~ (ε_mach)^(2/3) ~ 10⁻¹⁰.
```

### 5.2 Richardson Extrapolation

```
IDEA: Use lower-order approximations at h and h/2, cancel leading error term.

If F(h) = F(0) + c·hᵖ + O(h^(p+2)):
  F_extrapolated = [2ᵖ·F(h/2) − F(h)] / (2ᵖ − 1)
  Error: O(h^(p+2))  — gain 2 orders!

ROMBERG INTEGRATION: Richardson extrapolation applied to trapezoidal rule.
  Build Richardson table from h, h/2, h/4, ... → accelerate convergence.
```

### 5.3 Automatic Differentiation (AD)

```
AD ≠ symbolic differentiation ≠ finite differences.
AD computes exact derivatives (to machine precision) by applying chain rule to code.

FORWARD MODE:
  Propagate dual numbers (value, derivative) forward.
  Compute ∂f/∂xᵢ in one pass for ONE input variable.
  Cost: ~2-4× single function evaluation.

REVERSE MODE (BACKPROPAGATION):
  Forward pass: compute and record operations (tape/Wengert list).
  Backward pass: propagate adjoints from output to inputs.
  Compute ALL ∂f/∂xᵢ in one forward + one backward pass.
  Cost: ~3-10× single function evaluation, O(n) memory.

WHEN TO USE WHICH:
  n inputs, 1 output (e.g., ML loss): reverse mode (backprop) is O(1) cost.
  1 input, m outputs: forward mode.
  n inputs, m outputs: min(n,m) modes, or Jacobian-vector products.

IMPLEMENTATIONS: JAX, PyTorch autograd, TensorFlow, Zygote (Julia), Enzyme.

HIGHER DERIVATIVES: forward-over-reverse for Hessians. Typically expensive.
  Hessian-vector products: O(1) cost via forward-over-reverse.
  Full Hessian: O(n) reverse passes.
```

<!-- @editor[bridge/P2]: Missing the connection between AD and optimization algorithms — JAX's jit+grad+vmap is the standard pattern. Also: checkpointing (gradient checkpointing / rematerialization) trades compute for memory in reverse-mode AD by not storing all intermediate activations. This is essential for training large models and directly connects numerical methods to ML engineering practice. -->

---

## 6. Numerical Integration (Quadrature)

### 6.1 Basic Rules

```
GOAL: Approximate I = ∫ₐᵇ f(x) dx.

MIDPOINT RULE: I ≈ (b−a)·f((a+b)/2)
  Error: O(h²) per interval, O(h²) composite (n intervals: h=(b−a)/n).

TRAPEZOIDAL RULE: I ≈ (h/2)[f(a) + 2f(x₁) + ⋯ + 2f(xₙ₋₁) + f(b)]
  Error: O(h²) composite.
  Surprisingly: for PERIODIC smooth functions on [0,1], trapezoidal is spectrally accurate!
  Error ~ O(e^(−2πd/h)) where d = distance to singularity in complex plane.

SIMPSON'S RULE: I ≈ (h/3)[f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + ⋯ + f(xₙ)]
  Error: O(h⁴) composite. Two times more accurate than trapezoidal.
  Composite Simpson = degree-2 Newton-Cotes rule.

NEWTON-COTES RULES (general):
  Use polynomial interpolant through equispaced nodes.
  n=1: Trapezoidal (O(h²)), n=2: Simpson (O(h⁴)), n=3: 3/8 rule (O(h⁴)), n=4: Boole (O(h⁶)).
  High-order Newton-Cotes have negative weights → unstable.
```

### 6.2 Gaussian Quadrature

```
KEY INSIGHT: Quadrature nodes AND weights are free to choose.
With n points, match polynomials of degree 2n-1 (twice what Newton-Cotes gives).

GAUSS-LEGENDRE: nodes = roots of Legendre polynomial Pₙ(x) on [−1,1].
  Exact for polynomials of degree ≤ 2n−1.
  Error: ∫f − ΣwᵢF(xᵢ) = f^(2n)(ξ)·(2/(2n+1))·((n!)⁴/(2n)!³)·(b−a)^(2n+1)/(4n+1)

GAUSS-HERMITE: weight e^(−x²) on (−∞,+∞). For expectations over Gaussians.
GAUSS-LAGUERRE: weight e^(−x) on [0,∞). For integrals over positive axis.
GAUSS-CHEBYSHEV: weight 1/√(1−x²). Analytically exact quadrature nodes.
GAUSS-KRONROD: embedded rule for error estimation (used in QUADPACK/scipy.integrate).

COMPARISON:
  n-point rule:   Trapezoidal O(h²),  Gauss-Legendre exact for degree 2n-1
  For smooth f: Gaussian converges faster. For periodic f: trapezoidal is king.
```

### 6.3 Adaptive Quadrature

```
IDEA: estimate local error, subdivide only where needed.

STRATEGY:
  Compute I_coarse (coarse rule) and I_fine (refined rule).
  If |I_coarse − I_fine| < tol: accept I_fine.
  Else: subdivide interval and recurse.

GAUSS-KRONROD (n=15 points):
  7-point Gauss embedded in 15-point Kronrod.
  Error estimate from difference. QUADPACK default.

ADAPTIVE SIMPSON: double intervals until error small enough.
  scipy.integrate.quad uses QUADPACK (Fortran, highly reliable).

IMPROPER INTEGRALS:
  ∫₀^∞ f(x) dx: Gauss-Laguerre or substitution x = t/(1−t), then Gauss-Legendre.
  Near singularities: Gauss-Chebyshev or change of variable.
```

### 6.4 Monte Carlo Integration

```
MONTE CARLO: ∫_Ω f(x) dx ≈ (Vol(Ω)/N) Σᵢ f(xᵢ), xᵢ ~ Uniform(Ω).
  Error: O(N^(−1/2)) — independent of dimension d!
  Beats all deterministic methods for d ≥ 4-5 in terms of complexity.

VARIANCE REDUCTION:
  Importance sampling: sample from q(x) ∝ |f(x)|.
    Estimator: (1/N) Σ f(xᵢ)/q(xᵢ).
    Variance → 0 when q ∝ f.
  Control variates: subtract correlated known-expectation quantity.
  Antithetic variates: use (u, 1−u) pairs from [0,1].
  Stratified sampling: divide domain into strata, sample from each.

QUASI-MONTE CARLO: low-discrepancy sequences (Halton, Sobol, Faure).
  Error: O((log N)^d / N) — better than MC for smooth integrands.

MARKOV CHAIN MONTE CARLO (MCMC):
  Sample from high-dimensional distributions (Bayesian posteriors, partition functions).
  Metropolis-Hastings, Gibbs sampling, Hamiltonian MC (HMC).
  HMC uses gradient of log p — combines leapfrog ODE integrator + acceptance step.
  NUTS (No-U-Turn Sampler) = adaptive HMC, default in Stan/PyMC.
```

---

## 7. Ordinary Differential Equations

### 7.1 Initial Value Problems

```
IVP: y' = f(t, y),  y(t₀) = y₀   (y ∈ ℝⁿ, f: ℝ × ℝⁿ → ℝⁿ)

EULER'S METHOD (explicit):
  yₙ₊₁ = yₙ + h·f(tₙ, yₙ)
  Order 1: local error O(h²), global error O(h).
  Simple, unstable for stiff problems.

RUNGE-KUTTA 4 (RK4): classic workhorse.
  k₁ = f(tₙ, yₙ)
  k₂ = f(tₙ + h/2, yₙ + h·k₁/2)
  k₃ = f(tₙ + h/2, yₙ + h·k₂/2)
  k₄ = f(tₙ + h, yₙ + h·k₃)
  yₙ₊₁ = yₙ + (h/6)(k₁ + 2k₂ + 2k₃ + k₄)
  Order 4: local error O(h⁵), global error O(h⁴).

DORMAND-PRINCE (RK45): RK4 + RK5 embedded pair for adaptive step size.
  scipy.integrate.solve_ivp default. MATLAB ode45 = same.
  Error estimate from difference of 4th and 5th order solutions.

ADAPTIVE STEP SIZE CONTROL:
  Double step if error < tol_lo, halve if error > tol_hi.
  Classic: PIController, DOPRI5.
```

<!-- @editor[bridge/P2]: Missing Butcher tableaux — the systematic framework for constructing and analyzing Runge-Kutta methods. The order conditions (tree-based Butcher theory) explain why RK4 is order 4 and why constructing higher-order explicit methods gets expensive. Also: symplectic integrators (Störmer-Verlet) for Hamiltonian systems — conserve energy exactly over long integration, critical for molecular dynamics and n-body simulation. -->

### 7.2 Convergence and Consistency

```
TAYLOR SERIES ANALYSIS:
  y(tₙ₊₁) = y(tₙ) + h·y'(tₙ) + (h²/2)y''(tₙ) + ⋯  (exact)
  Local truncation error (LTE): τₙ = y(tₙ₊₁) − y(tₙ) − Φ(tₙ,yₙ,h)
    Φ = method's increment function.
  Order p: LTE = O(h^(p+1)).

STABILITY (Dahlquist test equation): y' = λy,  Re(λ) < 0.
  Exact: y(t) = eλt → 0.
  Euler: yₙ = (1+hλ)ⁿ → 0 iff |1+hλ| < 1 → stability region is disk of radius 1 centered at -1.
  RK4 stability region: larger, but still finite in complex plane.

DAHLQUIST THEOREM: Explicit methods have bounded stability regions.
  Cannot be A-stable (stable for all Re(λ)<0).
  Implicit methods can be A-stable (stable for entire left half-plane).

CONVERGENCE = CONSISTENCY + STABILITY (Lax-Richtmyer for PDEs, Dahlquist for ODEs).
```

### 7.3 Stiff Equations

```
STIFF ODE: has solution components decaying on very different timescales.
  Example: y' = λy + (1−λ)cos(t) − (1+λ)sin(t),  λ = −10⁶
  Fast transient dies quickly, but explicit methods need h < 2/|λ| = 2×10⁻⁶ throughout!
  Solution is smooth but explicit methods require tiny h. Wasteful.

TEST: condition number of Jacobian ∂f/∂y. Large negative real eigenvalues = stiff.

IMPLICIT EULER:
  yₙ₊₁ = yₙ + h·f(tₙ₊₁, yₙ₊₁)   (implicit nonlinear equation for yₙ₊₁)
  Stability region: entire left half-plane (A-stable). Unlimited step size.
  Cost: solve nonlinear system each step (Newton iteration).

TRAPEZOIDAL RULE (Crank-Nicolson):
  yₙ₊₁ = yₙ + (h/2)[f(tₙ,yₙ) + f(tₙ₊₁,yₙ₊₁)]
  A-stable, order 2. Standard for parabolic PDEs.

BDF METHODS (Backward Differentiation Formulas):
  Use past values: Σ αₖyₙ₋ₖ = h·β₀·f(tₙ, yₙ)
  BDF1 = Implicit Euler. BDF2,...,BDF6 are A(α)-stable.
  MATLAB ode15s = variable-order BDF.

ROSENBROCK METHODS: linearly implicit — one Newton step per stage. Good for moderate stiffness.
```

### 7.4 Boundary Value Problems

```
BVP: y'' = f(x,y,y'),  y(a) = α,  y(b) = β

SHOOTING METHOD:
  Convert to IVP: guess y'(a) = s, solve forward to b, adjust s to hit y(b) = β.
  Newton's method on F(s) = y(b;s) − β.

FINITE DIFFERENCE METHOD:
  Discretize [a,b]: xᵢ = a + ih, h = (b−a)/n.
  y''(xᵢ) ≈ (yᵢ₋₁ − 2yᵢ + yᵢ₊₁)/h²
  → tridiagonal linear system. O(n).

FINITE ELEMENT METHOD (Galerkin):
  Write y ≈ Σcⱼφⱼ(x) (basis functions).
  Impose ∫(−y'' − f)φᵢ = 0  (weak form / weighted residual).
  FEM: piecewise linear/quadratic φⱼ on elements.
  Produces sparse banded system.

COLLOCATION (BVP solvers): scipy.integrate.solve_bvp, bvp4c in MATLAB.
  Fit polynomial in each interval satisfying ODE at collocation points.
```

---

## 8. Eigenvalue Problems

### 8.1 Power Iteration and Variants

```
POWER ITERATION (dominant eigenvalue):
  Start v₀, iterate vₖ₊₁ = Avₖ/‖Avₖ‖.
  Converges to eigenvector for λ₁ (largest |eigenvalue|).
  Convergence rate: (|λ₂|/|λ₁|)ᵏ — slow if eigenvalues close.

RAYLEIGH QUOTIENT: r(v) = vᵀAv/vᵀv → eigenvalue estimate.
  Converges quadratically near eigenvector.

INVERSE ITERATION: apply power iteration to (A − μI)⁻¹.
  Finds eigenvalue nearest to shift μ.
  Rayleigh quotient iteration: update shift using Rayleigh quotient.
  Convergence: cubically! Very fast near eigenvalue.

DEFLATION: found eigenvalue λ₁ → compute A₁ = A − λ₁v₁v₁ᵀ → find next eigenvalue.
```

### 8.2 QR Algorithm

```
QR ALGORITHM: compute all eigenvalues of A.

BASIC FORM:
  A₀ = A
  For k = 1,2,...:
    Aₖ = QₖRₖ  (QR decomposition)
    Aₖ₊₁ = RₖQₖ  (reverse order)
  Aₖ → Schur form T (upper triangular, eigenvalues on diagonal).

WITH SHIFTS: Aₖ − μₖI = QₖRₖ → Aₖ₊₁ = RₖQₖ + μₖI.
  Wilkinson shift: converges cubically for 2×2 blocks.

PRACTICAL QR ALGORITHM:
  1. Reduce A to Hessenberg form H (upper triangular + one subdiagonal): O(n³) once.
  2. Apply QR iterations to H: each iteration O(n²).
  3. Total: O(n³). Converges in ~2n iterations typically.
  LAPACK's dgehrd/dhseqr: production implementation.

FOR SYMMETRIC A (A=Aᵀ):
  Reduce to tridiagonal T (not Hessenberg): O(n³), uses Householder.
  QR on tridiagonal: O(n) per iteration.
  → all eigenvalues in O(n²).

LANCZOS ALGORITHM: for large sparse A (symmetric).
  Build Krylov subspace Kₖ = span{v, Av, ..., A^(k-1)v}.
  Produces tridiagonal Tₖ (Ritz values = eigenvalue approximations).
  O(kn) for k eigenvalues, k << n.
  Numerical issues: loss of orthogonality → need re-orthogonalization.

ARNOLDI ALGORITHM: generalization of Lanczos to non-symmetric A.
  Used in GMRES (Krylov subspace + eigenvalue connection).
```

---

## 9. Partial Differential Equations — Numerical

### 9.1 Finite Difference Methods for PDEs

```
HEAT EQUATION: ∂u/∂t = α∂²u/∂x²

FTCS (Forward Time Central Space) — EXPLICIT:
  uᵢⁿ⁺¹ = uᵢⁿ + r(uᵢ₋₁ⁿ − 2uᵢⁿ + uᵢ₊₁ⁿ),   r = αΔt/(Δx)²
  Stability condition: r ≤ 1/2  (CFL-type for parabolic)
  If r > 1/2: unconditionally unstable (oscillates, diverges).

BTCS (Backward Time Central Space) — IMPLICIT (Crank-Nicolson for θ=1/2):
  Solves tridiagonal system each step. Unconditionally stable. O(n) per step.

WAVE EQUATION: ∂²u/∂t² = c²∂²u/∂x²
  CFL CONDITION: c·Δt/Δx ≤ 1  (Courant-Friedrichs-Lewy condition)
  Explicit method stable only if wave doesn't cross more than one cell per timestep.
  Physical: information can't travel faster than numerical domain of dependence.

LAPLACE EQUATION: ∂²u/∂x² + ∂²u/∂y² = 0
  Elliptic: no time evolution. Boundary value problem.
  5-point stencil → sparse linear system. Solve with multigrid O(n) or Cholesky.

VON NEUMANN STABILITY ANALYSIS:
  Substitute uⱼⁿ = ρⁿ eᵢʲᵏΔx, find growth factor ρ(k).
  Stable iff |ρ(k)| ≤ 1 for all wavenumbers k.
```

### 9.2 Finite Element Method (FEM)

```
FEM WORKFLOW:
  1. WEAK FORM: multiply PDE by test function v, integrate by parts.
     −∇·(κ∇u) = f  →  ∫κ∇u·∇v dx = ∫fv dx  for all v.

  2. DISCRETIZATION: u ≈ Σ uⱼφⱼ(x), v ∈ span{φᵢ}.
     → Ku = f  where Kᵢⱼ = ∫κ∇φᵢ·∇φⱼ dx (stiffness matrix)
                        fᵢ = ∫f·φᵢ dx (load vector)

  3. K is SPARSE (each φᵢ overlaps few φⱼ).
     Solve with sparse Cholesky (CHOLMOD) or multigrid.

ELEMENTS: linear triangles/quads (2D), tetrahedra/hexahedra (3D).
  Higher order: quadratic, cubic elements (p-FEM).

FEM ADVANTAGES VS FD:
  • Handles complex geometries
  • Variational formulation → energy minimization
  • Natural treatment of Neumann BCs
  • h-p adaptive refinement

GALERKIN vs PETROV-GALERKIN vs STREAMLINE DIFFUSION: stabilization for convection.
```

### 9.3 Spectral Methods

```
SPECTRAL METHODS: expand solution in global smooth basis functions.
  u(x) ≈ Σₖ ûₖ ψₖ(x)

Fourier spectral: ψₖ = eⁱᵏˣ. Exponential convergence for periodic smooth problems.
  O(N log N) FFT for transforms. Standard for turbulence simulation (DNS).

CHEBYSHEV SPECTRAL: ψₖ = Tₖ(x). Non-periodic, high accuracy.

PSEUDOSPECTRAL: compute derivatives in spectral space, nonlinear terms in physical space.
  Differentiation matrix D: d/dx in spectral = diagonal multiplication.
  Error: exponential for smooth (spectral accuracy) vs algebraic for FD/FE.

DEALIASING: aliasing from nonlinear terms in Fourier spectral. 3/2-rule.

TRADEOFFS:
  FD/FE: O(hᵖ), complex geometry, sparse systems.
  Spectral: exponential convergence, simple geometry, dense transforms.
```

---

## 10. Numerical Linear Algebra in ML

```
DOMINANT OPERATIONS IN ML:

GEMM (General Matrix Multiply): BLAS Level 3. C = αAB + βC.
  GPU achieves ~70% peak FLOPS on GEMM (vs 5-10% on sparse).
  Transformer attention: softmax(QKᵀ/√d)V — all GEMM.

SVD IN ML:
  PCA: SVD of data matrix X = UΣVᵀ.
  Truncated SVD: top-k components. O(mnk) for m×n matrix, rank k.
  Randomized SVD (Halko-Martinsson-Tropp 2011): O(mn log k) — huge speedup.
    Project onto random subspace, QR, small SVD.

CONDITION NUMBERS IN TRAINING:
  Ill-conditioned loss Hessian → slow convergence for gradient descent.
  κ(H) = λ_max/λ_min → steps in directions of small curvature must be tiny.
  Adam/AdamW: diagonal preconditioning, normalizes by √(second moment).
  Natural gradient: full Fisher information preconditioner (see information theory module).

SPARSE MATRIX FORMATS:
  CSR (Compressed Sparse Row): row-major, fast row operations.
  CSC (Compressed Sparse Column): col-major.
  COO (coordinate): easy to build, convert to CSR/CSC for computation.
  Sparse matrix × dense vector: O(nnz). GNN message passing is this.

FLOATING-POINT IN TRAINING:
  bfloat16 for weights+activations (same exponent range as float32, less mantissa).
  float32 for accumulation, loss scaling, master weights.
  FP8 (Hopper/Ada): E4M3 for forward, E5M2 for backward gradients.
  Mixed precision: AMP in PyTorch. See 04-PYTORCH module.
```

<!-- @editor[bridge/P2]: Missing the connection between numerical stability and modern deep learning training problems — gradient vanishing/exploding as a conditioning problem (deep networks = product of Jacobians, spectral radii compound multiplicatively). Batch normalization and layer normalization are numerical stabilizers — they condition the optimization landscape. Gradient clipping is an emergency numerical stabilizer. These are the numerical methods perspective on standard ML practices. -->

---

## 11. Decision Cheat Sheet

| Problem | Method | Complexity | Notes |
|---------|--------|-----------|-------|
| Root of scalar f | Brent's | O(log 1/ε) | Safe + fast, no derivative needed |
| Root, derivative known | Newton | O(log log 1/ε) | Quadratic convergence, near simple root |
| Linear system, dense SPD | Cholesky | O(n³/6) | 2× faster than LU |
| Linear system, dense general | LU+pivoting | O(n³/3) | LAPACK dgesv |
| Linear system, large sparse SPD | CG+AMG | O(n) | Multigrid preconditioned |
| Linear system, large sparse general | GMRES+ILU | O(kn) per restart | k = iterations |
| Interpolation, smooth function | Chebyshev nodes | O(n²) | Avoid Runge's phenomenon |
| Interpolation, general | Cubic spline | O(n) | Smooth, stable |
| Least squares | QR decomposition | O(mn²) | Stable, κ(R)=κ(A) not κ²(A) |
| Integration, smooth 1D | Gauss-Legendre | O(n⁻²ⁿ) | Exponentially fast for smooth f |
| Integration, periodic | Trapezoidal | O(e^{-c/h}) | Spectrally accurate |
| Integration, high-dimension | Monte Carlo | O(N^{-1/2}) | Dimension-independent |
| ODE, non-stiff | RK45 (DOPRI5) | O(hᵖ) adaptive | scipy solve_ivp default |
| ODE, stiff | BDF/Radau | — | scipy solve_ivp method='BDF' |
| All eigenvalues, dense | QR algorithm | O(n³) | LAPACK dsyev/dgeev |
| Few eigenvalues, sparse | Lanczos/Arnoldi | O(kn) | k << n |
| Derivatives of code | Reverse-mode AD | O(1) × cost(f) | Backpropagation |

---

## 12. Common Confusion Points

**Stability vs. Accuracy**: High-order method doesn't mean stable. A 4th-order explicit
method for a stiff ODE is spectacularly accurate and simultaneously completely unstable.
Stability is about what happens to errors; accuracy is about the truncation error.

**Condition number vs. stability**: Condition number is a property of the *problem*
(inherent ill-posedness). Stability is a property of the *algorithm*. An ill-conditioned
problem solved with a stable algorithm gives the best possible answer. An ill-conditioned
problem solved with an unstable algorithm gives garbage.

**Machine epsilon ≠ smallest float**: ε_mach ≈ 2.2×10⁻¹⁶ is the *relative* rounding
unit for float64. The smallest positive float64 is ~5×10⁻³²⁴ (subnormal). The smallest
*normal* positive float64 is ~2.2×10⁻³⁰⁸. These are very different things.

**NaN propagates silently**: NaN + anything = NaN. Any comparison with NaN returns false.
This is intentional (IEEE 754) but means NaN can corrupt an entire computation if not checked.

**Normal equations for least squares**: Never use AᵀAx = Aᵀb directly — condition number
squares. Use QR or SVD. This is why numpy.linalg.lstsq uses SVD, not normal equations.

**Gaussian quadrature is not always best**: For periodic smooth functions, the humble
trapezoidal rule achieves spectral accuracy — faster than any Gaussian rule. Gauss is
best for non-periodic smooth functions.

**Explicit vs. implicit for stiff ODEs**: Explicit methods need h < 2/|λ_max| for stability.
If λ_max = 10⁶ but you only care about dynamics at timescale 1, you need 10⁶ steps.
Implicit methods let you use h ~ 1 (the timescale you care about) — 10⁶× fewer steps.

**Backpropagation is reverse-mode AD**: Not a separate algorithm. "Backprop" is just
what ML people call reverse-mode automatic differentiation. The chain rule applied in
reverse order through a computational graph.

**Richardson extrapolation doubles the order**: If you have an O(h²) method, one step of
Richardson gives O(h⁴). This is how Romberg integration builds high accuracy from
the trapezoidal rule. Same idea as polynomial extrapolation on error.
