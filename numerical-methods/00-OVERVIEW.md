# Numerical Methods — Landscape Overview

## The Big Picture

Numerical methods are algorithms for approximating the solutions of mathematical problems that cannot be solved analytically. The fundamental challenge: computers work with floating-point approximations to real numbers, and the errors accumulate.

<!-- @editor[diagram/P2]: Landscape lists four isolated boxes but doesn't show the dependency flow — the FOUNDATION box should visually feed upward into the four problem boxes, and arrows should show how linear systems feed eigenvalue methods (via Cholesky reduction) and how all four feed into the scientific computing stack. Rework as layered system view showing data flow between problem classes. -->
```
+------------------------------------------------------------------+
|              NUMERICAL METHODS LANDSCAPE                         |
+------------------------------------------------------------------+
|                                                                  |
|  THE FOUR CORE PROBLEMS:                                        |
|                                                                  |
|  1. SOLVE LINEAR SYSTEMS    Ax = b                              |
|     +-------------------+                                        |
|     | Direct: LU, QR    |                                        |
|     | Iterative: CG,    |                                        |
|     | GMRES, multigrid  |                                        |
|     +-------------------+                                        |
|                                                                  |
|  2. EIGENVALUE PROBLEMS     Av = lambda v                       |
|     +-------------------+                                        |
|     | Power iteration   |                                        |
|     | QR algorithm      |                                        |
|     | Lanczos, SVD      |                                        |
|     +-------------------+                                        |
|                                                                  |
|  3. INTEGRATION             Int_a^b f(x) dx                     |
|     +-------------------+                                        |
|     | Newton-Cotes      |                                        |
|     | Gaussian quad.    |                                        |
|     | Monte Carlo       |                                        |
|     +-------------------+                                        |
|                                                                  |
|  4. DIFFERENTIAL EQUATIONS  y' = f(t,y), Lu = f                 |
|     +-------------------+                                        |
|     | ODE: RK4, BDF     |                                        |
|     | PDE: FD, FEM,     |                                        |
|     | spectral methods  |                                        |
|     +-------------------+                                        |
|                                                                  |
|  FOUNDATION:                                                     |
|  Floating-point arithmetic, error analysis,                     |
|  conditioning, stability                                        |
+------------------------------------------------------------------+
```

---

## The Critical Distinction: Stability, Conditioning, Accuracy

This is the most important distinction in numerical computing. Even mathematicians who are expert in algorithm theory conflate these.

```
  CONDITIONING (property of the PROBLEM):
  How much does the output change when the input changes slightly?
  kappa = condition number = max (||delta output|| / ||output||) / (||delta input|| / ||input||)

  Large kappa = ill-conditioned problem = small input errors -> large output errors.
  This is a property of the mathematical problem, not the algorithm.
  You CANNOT fix ill-conditioning by choosing a better algorithm.

  STABILITY (property of the ALGORITHM):
  Does the algorithm amplify errors already present in the computation?
  A backward-stable algorithm: computes the exact answer to a slightly perturbed problem.
  A forward-stable algorithm: the computed output is close to the true output.

  You CAN choose a stable algorithm even for ill-conditioned problems.
  A stable algorithm on a well-conditioned problem gives accurate results.
  A stable algorithm on an ill-conditioned problem gives the "best possible" results.
  An unstable algorithm on a well-conditioned problem can give terrible results.

  ACCURACY (property of the RESULT):
  How close is the computed answer to the true answer?
  Accuracy = f(conditioning of problem, stability of algorithm)
  Accuracy = kappa * machine_epsilon (roughly, for well-designed algorithms)
```

```
  +-------------------+------------------+------------------+
  |                   | STABLE algorithm | UNSTABLE alg     |
  +-------------------+------------------+------------------+
  | WELL-CONDITIONED  | ACCURATE RESULT  | May be OK or bad |
  | PROBLEM           |                  |                  |
  +-------------------+------------------+------------------+
  | ILL-CONDITIONED   | Best possible    | GARBAGE          |
  | PROBLEM           | (inherent error) |                  |
  +-------------------+------------------+------------------+
```

---

## Module Map

```
  00-OVERVIEW (this file)
  |
  +-- 01-FLOATING-POINT       IEEE 754, rounding modes, catastrophic cancellation
  |   Condition numbers, backward error analysis, interval arithmetic
  |
  +-- 02-LINEAR-SYSTEMS       Gaussian elimination, LU/QR/Cholesky factorizations
  |   Iterative: CG, GMRES, preconditioning, multigrid
  |
  +-- 03-EIGENVALUE-METHODS   Power iteration, QR algorithm, Lanczos, SVD
  |   Randomized algorithms (RandSVD), applications
  |
  +-- 04-INTERPOLATION        Lagrange/Newton polynomial interpolation
  |   Splines (cubic, B-spline), radial basis functions, Chebyshev approximation
  |
  +-- 05-NUMERICAL-INTEGRATION Newton-Cotes, Gaussian quadrature
  |   Adaptive integration, Monte Carlo, quasi-Monte Carlo
  |
  +-- 06-ODES                 Euler, Runge-Kutta, stiff systems (BDF/Rosenbrock)
  |   Boundary value problems: shooting, collocation
  |
  +-- 07-PDES                 Finite differences, finite elements
  |   Spectral methods, finite volumes, CFL stability condition
  |
  +-- 08-OPTIMIZATION         Gradient descent and variants, Newton/quasi-Newton
  |   Convex optimization, interior point methods, global methods
  |
  +-- 09-SCIENTIFIC-COMPUTING BLAS/LAPACK/ScaLAPACK, sparse matrices
      GPU computing, NumPy/SciPy/Julia/MATLAB ecosystem
```

---

## Error Sources and Propagation

```
  ERROR TAXONOMY:

  1. TRUNCATION ERROR: approximating an infinite series by a finite one.
     Example: Euler method approximates e^h = 1 + h + h^2/2 + ... with 1 + h.
     Truncation error = O(h^2) per step.

  2. ROUNDING ERROR: representing real numbers with finite bits.
     Machine epsilon eps_mach: smallest eps such that fl(1 + eps) > 1.
     For IEEE 754 double precision: eps_mach = 2.22e-16 (~16 significant digits).

  3. DISCRETIZATION ERROR: replacing continuous problems with discrete ones.
     Examples: derivatives by finite differences, integrals by quadrature sums.
     Controlled by the mesh/step size h.

  4. PROPAGATED ROUNDING ERROR: rounding errors compound through operations.
     After n operations with individual error eps: total error ≈ n * eps.
     In matrix multiplication of n x n matrices: ~ n * eps_mach amplification.

  FLOATING-POINT ARITHMETIC PRINCIPLE:
  fl(x op y) = (x op y)(1 + delta)   for |delta| <= eps_mach
  Each operation introduces a small relative error.
```

---

## Asymptotic Analysis: Order of Convergence

```
  An algorithm with error e(h) has ORDER OF CONVERGENCE p if:
  e(h) = O(h^p) as h -> 0

  This is the SAME Big-O notation from algorithm analysis (MIT TCS background).
  But h is a step size, not input size. Smaller h = more accuracy but more work.

  ERROR-WORK TRADEOFF:
  For an algorithm using n evaluations with step h = 1/n:
  Work = O(n), Error = O(h^p) = O(n^{-p})

  To halve the error with a p-th order method: multiply work by 2^p.
  p=1 (Euler): double work -> halve error
  p=2: quadruple work -> halve error
  p=4 (RK4): 16x work -> halve error
  Spectral: exponential convergence for smooth functions

  CONVERGENCE RATE COMPARISON (table for integration):
  Method          Rate        Evaluations for 10^{-12} error
  Midpoint rule   O(h^2)      ~10^6
  Simpson's rule  O(h^4)      ~1000
  Gaussian quad.  O(h^{2n})   ~20   (for smooth functions!)
  Monte Carlo     O(n^{-1/2}) ~10^{24} ... but dim-independent
```

---

## The Curse of Dimensionality in Numerics

A fundamental challenge distinct from (but related to) the ML concept:

```
  For d-dimensional numerical integration with step h per dimension:
  Number of grid points = (1/h)^d
  For 10^{-4} error with O(h^4) method: h = 0.1, points = 10^d

  d=1:  10 points      (trivial)
  d=5:  100,000 points  (feasible)
  d=10: 10^10 points    (infeasible)
  d=20: 10^20 points    (impossible)

  SOLUTION: Monte Carlo integration (O(n^{-1/2}) rate, independent of d).
  For high-dimensional physics simulation, finance, statistics: MC is often only option.
  Quasi-Monte Carlo (low-discrepancy sequences) gives O(n^{-1} log(n)^d).
```

---

<!-- @editor[bridge/P1]: No automatic differentiation → backpropagation bridge anywhere in the overview. The learner explicitly needs AD, and the connection "reverse-mode AD = backprop = gradient computation for all of module 08" is the single most important bridge in this section for someone coming from an ML-aware CS background. Should appear here in the connections map. -->

<!-- @editor[bridge/P2]: No GPU-accelerated numerical linear algebra bridge in the overview. The learner needs cuBLAS/cuSPARSE patterns (explicitly listed in calibration). The module map notes 09-SCIENTIFIC-COMPUTING covers GPU but the overview itself gives no orientation to where GPU enters the picture — a reader scanning the overview wouldn't know this is covered. -->

## Key Connections to Other Library Directories

```
  mathematics/
    Real analysis: limits, convergence, completeness (underpins all convergence proofs)
    Linear algebra: matrix decompositions (LU, QR, SVD) are the core algorithms
    Complex analysis: contour integration, spectral theory of operators

  data-science/
    NumPy/SciPy implement BLAS/LAPACK (see 09-SCIENTIFIC-COMPUTING)
    Matrix operations in ML = numerical linear algebra at scale
    Gradient descent (08) connects to ML training
    SVD (03) = PCA in machine learning

  differential-geometry/
    Manifold optimization (Riemannian SGD) is in 08-OPTIMIZATION
    Geodesic computation on manifolds uses ODE solvers (06)
    FEM on curved surfaces uses differential geometry tools

  probability-statistics/
    Monte Carlo integration connects to stochastic processes
    MCMC sampling = numerical methods for Bayesian inference
    Random matrix theory underlies RandSVD analysis
```

---

## Decision Cheat Sheet

| Problem | Standard Method | When to Use Iterative Instead |
|---|---|---|
| Dense Ax=b, n < 10^4 | LU factorization | — |
| Dense Ax=b, A symmetric PD | Cholesky | — |
| Sparse Ax=b, n > 10^4 | CG / GMRES | Always for sparse large systems |
| Top-k eigenvalues, large A | Lanczos / LOBPCG | — |
| All eigenvalues, dense A | QR algorithm | — |
| SVD of large matrix | RandSVD | Approximate SVD, huge matrices |
| Smooth f(x) integral, 1D | Gaussian quadrature | — |
| High-dimensional integral | Monte Carlo | d > 5 or so |
| ODE, non-stiff | Runge-Kutta 4/5 | — |
| ODE, stiff | BDF / Rosenbrock | Stiffness ratio >> 1 |
| PDE on simple geometry | Finite differences | Complex geometry -> FEM |
| PDE on complex geometry | Finite element method | — |
| Convex optimization | Interior point | Global convergence needed |
| Smooth non-convex | BFGS / L-BFGS | Large scale -> L-BFGS |
| Discrete/combinatorial | Simulated annealing | Continuous -> gradient methods |

---

## Common Confusion Points

**"More accurate algorithm = better algorithm."**
Accuracy is a function of both the algorithm AND the problem conditioning. A highly accurate algorithm on an ill-conditioned problem still gives poor results. Choose your algorithm based on stability AND the problem's condition number.

**"Using higher precision fixes floating-point problems."**
It helps for mildly ill-conditioned problems. But if kappa ~ 10^{20}, you need 20 extra decimal digits of precision — not feasible. The fix is to reformulate the problem (better conditioning) or change the algorithm (iterative refinement, preconditioning).

**"Direct methods are always better than iterative methods."**
For large sparse systems: no. LU factorization of a sparse n x n matrix creates fill-in (non-sparse intermediate factors). CG/GMRES operate on sparse matrices without fill-in, using only matrix-vector products. For n = 10^6 sparse systems (typical PDEs), iterative methods are the only option.
