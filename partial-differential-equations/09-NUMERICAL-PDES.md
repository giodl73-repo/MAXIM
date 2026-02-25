# Numerical Methods for PDEs

## The Big Picture

Numerical PDE methods discretize continuous problems onto finite-dimensional systems.
Three major families: Finite Differences (FD), Finite Elements (FEM), and Spectral methods.
Each has a distinct philosophy and ideal domain of application.

```
+-----------------------------------------------------------------------+
|              NUMERICAL PDE METHODS LANDSCAPE                          |
|                                                                       |
|  FINITE DIFFERENCES (FD):                                             |
|  Replace derivatives by difference quotients on a regular grid.       |
|  Simple to implement. Works best on rectangular domains.              |
|  O(h^p) accuracy from Taylor expansion.                               |
|                                                                       |
|  FINITE ELEMENTS (FEM):                                               |
|  Discretize the WEAK FORMULATION on a mesh.                           |
|  Handles complex geometries. Rigorous error theory (Céa's lemma).    |
|  Sparse linear system; exploits local support of basis functions.     |
|                                                                       |
|  FINITE VOLUMES (FV):                                                 |
|  Conservative discretization: integrate PDE over control volumes.     |
|  Automatically preserves conservation laws.                           |
|  Standard in CFD (fluid dynamics), hyperbolic conservation laws.      |
|                                                                       |
|  SPECTRAL METHODS:                                                    |
|  Expand in global basis (Fourier, Chebyshev, spherical harmonics).   |
|  Exponential convergence for smooth problems.                         |
|  Dense operations; poor for discontinuities.                          |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## Finite Difference Approximations

### Deriving Difference Formulas

```
  TAYLOR EXPANSION:
  u(x+h) = u(x) + h u'(x) + h²/2 u''(x) + h³/6 u'''(x) + ...
  u(x−h) = u(x) − h u'(x) + h²/2 u''(x) − h³/6 u'''(x) + ...

  FIRST DERIVATIVES:
  Forward:   [u(x+h) − u(x)]/h = u'(x) + h/2·u''  + O(h²)   [1st order]
  Backward:  [u(x) − u(x−h)]/h = u'(x) − h/2·u''  + O(h²)   [1st order]
  Centered:  [u(x+h) − u(x−h)]/(2h) = u'(x) + h²/6·u''' + O(h²) [2nd order]

  SECOND DERIVATIVE:
  [u(x+h) − 2u(x) + u(x−h)]/h² = u''(x) + h²/12·u'''' + O(h⁴)  [2nd order]

  HIGHER ORDER:
  [−u(x+2h) + 16u(x+h) − 30u(x) + 16u(x−h) − u(x−2h)] / (12h²)
  = u''(x) + O(h⁴)  [4th order central]

  STENCIL NOTATION:
  Δ²_h u_i = (u_{i-1} − 2u_i + u_{i+1}) / h²    (1D Laplacian)

  2D LAPLACIAN (5-point stencil):
  ∇²_h u_{ij} = [u_{i-1,j} + u_{i+1,j} + u_{i,j-1} + u_{i,j+1} − 4u_{ij}] / h²
```

---

## Elliptic Equations: Finite Difference

```
  POISSON ON SQUARE GRID:
  −∇²u = f in Ω = [0,1]², u=g on ∂Ω

  GRID: x_i = ih, y_j = jh, i,j = 0,...,N+1, h = 1/(N+1)
  UNKNOWNS: u_{ij} for interior nodes i,j = 1,...,N

  DISCRETE SYSTEM:
  −(u_{i-1,j} + u_{i+1,j} + u_{i,j-1} + u_{i,j+1} − 4u_{ij}) = h²f_{ij}

  MATRIX FORM: AU = b  (A is sparse, N²×N² system)

  A = sparse block-tridiagonal matrix
  Bandwidth = O(N) = O(1/h)

  SOLVERS:
  • Direct: Gaussian elimination → O(N⁴) ops (too slow for large N)
  • Banded: exploits bandwidth → O(N³) = O(h⁻³)
  • Multigrid: O(N²) = O(h⁻²) = OPTIMAL
  • PCG with good preconditioner: O(N² log N)

  ACCURACY:
  ‖u − u_h‖_∞ ≤ C h²  (for smooth u and f)
  Derived by: truncation error is O(h²), discrete maximum principle.
```

---

## Parabolic Equations: Time-Stepping

### Explicit vs. Implicit

```
  HEAT EQUATION:  u_t = α u_xx  on [0,L]

  SEMI-DISCRETE: replace x-derivative by FD, keep t continuous:
  du_i/dt = α (u_{i-1} − 2u_i + u_{i+1}) / h²  = −α/h² A_h u

  This is an ODE system: u_t = −M·u  where M = α/h² A_h.
  Eigenvalues of M: μ_n = 4α/h² sin²(nπh/2L)   (all real, positive)
  Max eigenvalue: μ_max ≈ 4α/h² = O(α/h²)

  EULER EXPLICIT (Forward Euler in time):
  (u_i^{n+1} − u_i^n)/Δt = α (u_{i-1}^n − 2u_i^n + u_{i+1}^n)/h²

  STABILITY ANALYSIS (Von Neumann):
  Substitute u_i^n = ξ^n e^{ikx_i}:
  ξ = 1 − 4r sin²(kh/2)  where r = αΔt/h²
  |ξ| ≤ 1 ↔ r ≤ 1/2

  CFL CONDITION:  Δt ≤ h²/(2α)
  Parabolic stability: Δt = O(h²) — very restrictive!
  Halve h → time step must be 4x smaller.

  EULER IMPLICIT (Backward Euler):
  (u_i^{n+1} − u_i^n)/Δt = α (u_{i-1}^{n+1} − 2u_i^{n+1} + u_{i+1}^{n+1})/h²

  Solve linear system each step: (I + r A_h) U^{n+1} = U^n
  UNCONDITIONALLY STABLE (any Δt). First order in time.

  CRANK-NICOLSON (θ-method with θ=½):
  (u^{n+1}−u^n)/Δt = α/2 [(u^{n+1}_{xx} + u^n_{xx})]
  Solve: (I + r/2 A_h) U^{n+1} = (I − r/2 A_h) U^n
  UNCONDITIONALLY STABLE. SECOND order in time. THE STANDARD.
```

### CFL Condition Summary

```
  ┌─────────────────────────────────────────────────────────────┐
  │  EQUATION     METHOD      STABILITY         ORDER           │
  │  ─────────    ──────      ─────────         ─────           │
  │  Heat         Explicit    Δt ≤ h²/2α        O(Δt + h²)     │
  │  Heat         Implicit    Unconditional     O(Δt + h²)     │
  │  Heat         C-N         Unconditional     O(Δt² + h²)    │
  │  Wave         Explicit    Δt ≤ h/c (CFL!)   O(Δt² + h²)   │
  │  Wave         Implicit    Unconditional*    O(Δt² + h²)    │
  │  Conv. u_t+cu_x=0  Upwind  Δt ≤ h/c        O(Δt + h)     │
  │                                                             │
  │  *Wave implicit: unconditionally stable but dispersive     │
  └─────────────────────────────────────────────────────────────┘
```

---

## Hyperbolic Equations: Upwinding and Godunov

### Advection Equation

```
  u_t + c·u_x = 0  (c > 0: rightward advection)

  NAIVE CENTERED SCHEME (unstable for all Δt):
  (u_i^{n+1} − u_i^n)/Δt + c(u_{i+1}^n − u_{i-1}^n)/(2h) = 0
  → UNSTABLE for all Δt > 0 (von Neumann: |ξ| > 1 for all modes)

  UPWIND SCHEME (c > 0: backward difference — "upwind" = upstream):
  (u_i^{n+1} − u_i^n)/Δt + c(u_i^n − u_{i-1}^n)/h = 0
  → STABLE if CFL: cΔt/h ≤ 1.

  CFL NUMBER: ν = cΔt/h  (dimensionless)
  Must satisfy ν ≤ 1 for upwind stability.

  PHYSICAL MEANING:
  CFL condition: in one time step, information moves at most one cell.
  If ν > 1: information "jumps" cells, scheme can't track it → instability.

  VON NEUMANN ANALYSIS of upwind:
  u_i^n = ξ^n e^{ikx_i}
  ξ = 1 − ν(1 − e^{−ikh}) = 1 − ν + νe^{−ikh}
  |ξ|² = 1 − 2ν(1−ν)(1 − cos(kh)) ≤ 1  iff 0 ≤ ν ≤ 1.
```

### Godunov's Method: Conservation Laws

```
  CONSERVATION LAW: u_t + f(u)_x = 0

  FINITE VOLUME PHILOSOPHY:
  Integrate over cell [x_{i-1/2}, x_{i+1/2}] × [t^n, t^{n+1}]:
  U_i^{n+1} = U_i^n − Δt/Δx [F_{i+1/2} − F_{i-1/2}]

  NUMERICAL FLUX F_{i+1/2}: approximation of ∫ f(u) dt at interface.
  KEY: must be CONSISTENT and CONSERVATIVE (no spurious sources/sinks).

  GODUNOV (1959): F_{i+1/2} = f(u*) where u* solves the RIEMANN PROBLEM
  between left state U_i and right state U_{i+1}.

  RIEMANN PROBLEM: u_t + f(u)_x = 0 with piecewise constant IC
    u(x,0) = U_L  for x < 0
              U_R  for x > 0
  Solution is a similarity solution (waves: shocks, rarefactions, contacts).

  UPWIND GODUNOV for scalar (f = cu):
    F_{i+1/2} = f(U_i)  if c > 0  (left state if wave moves right)
    F_{i+1/2} = f(U_{i+1})  if c < 0

  HIGHER-ORDER:
  Godunov is only 1st order (piecewise constant reconstruction).
  MUSCL (2nd order): piecewise linear reconstruction with limiters.
  WENO (5th+ order): weighted essentially non-oscillatory — smooth
                    near smooth regions, non-oscillatory near shocks.
```

---

## Von Neumann Stability Analysis

The systematic method for checking stability of FD schemes:

```
  PROCEDURE:
  1. Write scheme as u_j^{n+1} = Σ_k a_k u_{j+k}^n (linear scheme)

  2. Substitute u_j^n = ξ^n e^{ijkh} (complex Fourier mode)
     k = wave number ∈ [−π/h, π/h]

  3. Compute amplification factor ξ(k):
     ξ = ξ(k) from the scheme

  4. STABLE iff |ξ(k)| ≤ 1 for ALL wave numbers k.

  EXAMPLE: Explicit heat equation:
  ξ(k) = 1 − 4r sin²(kh/2)   where r = αΔt/h²
  |ξ| ≤ 1 iff −2 ≤ −4r sin²(kh/2) ≤ 0
  → 0 ≤ r ≤ 1/2 ← CFL condition for heat equation

  CONDITIONAL STABILITY: only stable for small Δt.
  UNCONDITIONAL STABILITY: stable for all Δt > 0.

  For nonlinear schemes: linearize around mean state, apply analysis.
  This is necessary but not always sufficient for nonlinear stability.
```

---

## Multigrid: Optimal Elliptic Solvers

```
  WHY ITERATIVE SOLVERS ALONE ARE SLOW:
  Gauss-Seidel, Jacobi: good at reducing HIGH-frequency errors.
  Low-frequency errors ("smooth errors") converge very slowly.
  On a 1D problem with N unknowns: O(N²) iterations for full convergence.

  KEY INSIGHT (multigrid):
  What's smooth on the fine grid looks OSCILLATORY on a coarse grid.
  Apply smoother on coarse grid to kill those errors cheaply!

  V-CYCLE:
  ┌──────────────────────────────────────────────────────────────┐
  │ 1. PRE-SMOOTH: ν₁ smoothing steps (Gauss-Seidel) on fine grid│
  │ 2. RESTRICT: compute residual r = b − Au, restrict to coarse  │
  │              grid: r^H = I_h^H r^h                           │
  │ 3. COARSE SOLVE: solve A^H e^H = r^H (direct if small enough) │
  │    or RECURSE: apply V-cycle on coarse grid                  │
  │ 4. PROLONGATE: interpolate correction e^h = I_H^h e^H        │
  │ 5. CORRECT: u ← u + e^h                                     │
  │ 6. POST-SMOOTH: ν₂ smoothing steps                          │
  └──────────────────────────────────────────────────────────────┘

  COMPLEXITY: O(N) per V-cycle, O(N) total for full convergence.
  This is OPTIMAL — you can't do better than linear time for N unknowns.

  APPLICATIONS: Poisson equation, linear elasticity, anything elliptic.
  ALGEBRAIC MULTIGRID (AMG): doesn't need geometry; infers grid hierarchy
  from the matrix structure. Works for unstructured FEM meshes.
```

---

## Spectral Methods

```
  PERIODIC DOMAINS: FOURIER SPECTRAL

  Represent: u(x) ≈ u_N(x) = Σ_{k=−N/2}^{N/2} û_k e^{ikx}

  DIFFERENTIATION: ∂u_N/∂x → ik·û_k  (exact in frequency space)
  EVALUATION: use FFT for O(N log N) transforms

  PSEUDOSPECTRAL METHOD:
  Compute u in physical space at collocation points.
  Differentiate via FFT (spectral accuracy for smooth u).
  Evaluate nonlinear terms pointwise in physical space.
  → Handles nonlinear PDEs efficiently.

  ACCURACY: For u ∈ C^∞ (periodic), convergence is SPECTRAL:
  ‖u − u_N‖ = O(N^{−k}) for all k.
  Faster than any polynomial rate.
  But: Gibbs phenomenon at discontinuities; dense matrix structure.

  NON-PERIODIC: CHEBYSHEV SPECTRAL
  Collocation at Chebyshev points: x_j = cos(jπ/N)
  Represent: u(x) ≈ Σ a_k T_k(x)  (Chebyshev polynomials)
  Uses DCT (discrete cosine transform) for O(N log N) computation.
  Handles non-periodic BCs naturally; exponential convergence.
```

---

## Boundary Element Method (BEM)

```
  BEM PHILOSOPHY:
  For problems with constant coefficients in infinite or semi-infinite domains:
  Use Green's theorem to reduce the volume PDE → SURFACE integral equation.
  Only the BOUNDARY needs to be discretized.

  FOR LAPLACE (3D):
  Green's formula:
  u(x) = ∫_{∂Ω} [G(x,y) ∂u/∂n(y) − u(y) ∂G/∂n(y)] dS(y)

  Discretize ∂Ω (N boundary elements) → NxN dense linear system.
  Volume unknowns: 0. Boundary unknowns: N (much smaller than FEM N²).

  TRADEOFFS:
  +: Only boundary needs meshing — complex 3D geometries easier.
  +: Infinite domains handled naturally (Green's function decays).
  −: Dense system (N×N BEM vs. N²×N² sparse FEM, but N is smaller).
  −: Requires known Green's function (restricts to constant coefficients).
  −: Integration of singular kernels requires care.

  FAST MULTIPOLE METHOD (FMM):
  Reduces dense N×N BEM system-vector product from O(N²) to O(N log N).
  Key: far-field interactions compressed via multipole expansions.
  Among the top 10 algorithms of the 20th century (Dongarra & Sullivan, 2000).
```

---

## Method Comparison

```
  +──────────────+──────────────+──────────────+──────────────+
  |              |   FINITE     |   FINITE     |   SPECTRAL   |
  |              | DIFFERENCES  |  ELEMENTS    |              |
  +──────────────+──────────────+──────────────+──────────────+
  | Geometry     | Rect/tensor  | Arbitrary    | Rect/sphere  |
  | handling     | product only | (meshed)     |              |
  +──────────────+──────────────+──────────────+──────────────+
  | Accuracy     | O(h^p)       | O(h^p)       | Exponential  |
  |              | Taylor order | by p-order   | for smooth u |
  +──────────────+──────────────+──────────────+──────────────+
  | Discontinuit | Upwind ok    | OK w/ care   | Gibbs phenom |
  | ies/shocks   |              |              |              |
  +──────────────+──────────────+──────────────+──────────────+
  | Implementation| Very simple | Moderate     | Moderate     |
  | complexity   |              |              |              |
  +──────────────+──────────────+──────────────+──────────────+
  | Dominant use | CFD (FV),    | Structural,  | Weather,     |
  |              | wave prop.   | elasto, heat | geophysics   |
  +──────────────+──────────────+──────────────+──────────────+
```

---

## Decision Cheat Sheet

| Problem | Recommended Method |
|---------|-------------------|
| Poisson on regular grid | FD (5-point stencil) + multigrid |
| Poisson on complex geometry | FEM (P1 or P2) + AMG |
| Heat equation, moderate time | FD Crank-Nicolson; or Method of Lines + BDF2 |
| Heat equation, stiff (α large) | Implicit FD/FEM |
| Wave equation, explicit | FD leapfrog + CFL |
| Hyperbolic conservation laws | FV Godunov + MUSCL; WENO for high accuracy |
| Smooth solution, periodic | Fourier spectral + pseudospectral |
| Smooth solution, non-periodic | Chebyshev collocation |
| Infinite domain, constant coeff | BEM + FMM |
| Large sparse elliptic system | AMG or multigrid preconditioned CG |

---

## Common Confusion Points

**"FD and FEM both converge at O(h²). Why use FEM?"**
For rectangular domains with smooth coefficients, FD is simpler and equivalent.
FEM wins when: (1) the domain has a complex boundary, (2) the coefficients are
discontinuous (heterogeneous media), (3) you need local refinement (mesh adaptivity),
or (4) you need the rigorous error theory (Céa, Aubin-Nitsche) for certification.
Also, FEM naturally handles Neumann BCs via boundary integrals.

**"CFL condition for wave equation: Δt ≤ h/c. Why is this tighter than heat equation's
Δt ≤ h²/2α?"**
For the wave equation the constraint is Δt = O(h), so refining h by 2 doubles the
number of time steps. For the heat equation (explicit) it's Δt = O(h²), so halving h
requires 4× more time steps. Hyperbolic PDEs have proportional CFL scaling, which is
actually BETTER than parabolic. This is why parabolic equations almost always use
implicit time-stepping (Crank-Nicolson) while hyperbolic equations can often use explicit.

**"What's the difference between finite volumes and finite differences?"**
Both use a mesh. FD approximates derivatives at grid points using Taylor expansion.
FV integrates the conservation law over control volumes, producing a discrete conservation
statement. For smooth problems on regular grids they can give identical schemes.
The FV advantage is: (1) exact conservation (important for shocks), (2) natural handling
of nonuniform grids, (3) straightforward extension to unstructured meshes. This is why CFD
codes (OpenFOAM, Fluent) primarily use finite volumes.
