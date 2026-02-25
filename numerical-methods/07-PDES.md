# Partial Differential Equations

## The Big Picture

PDEs govern heat, fluid flow, waves, structural mechanics, electrostatics, and quantum mechanics. Numerical PDE methods discretize space (and time), converting the PDE into a large algebraic system.

```
+------------------------------------------------------------------+
|                    PDE NUMERICAL METHODS                         |
+------------------------------------------------------------------+
|                                                                  |
|  PDE CLASSIFICATION                                             |
|  +-------------------------------------------------------------+ |
|  | ELLIPTIC: -nabla^2 u = f  (steady state, e.g., Poisson)    | |
|  | PARABOLIC: u_t = nabla^2 u  (diffusion, heat equation)     | |
|  | HYPERBOLIC: u_tt = c^2 nabla^2 u  (waves, advection)       | |
|  +-------------------------------------------------------------+ |
|                                                                  |
|  DISCRETIZATION METHODS                                         |
|  +---------------------+  +------------------+  +-----------+  |
|  | FINITE DIFFERENCES  |  | FINITE ELEMENTS  |  | SPECTRAL  |  |
|  | Simple, structured  |  | Complex geom.    |  | High acc. |  |
|  | grids only          |  | Variational form |  | smooth f  |  |
|  | O(h^2) standard     |  | Flexible mesh    |  | O(e^{-n}) |  |
|  +---------------------+  +------------------+  +-----------+  |
|                                                                  |
|  FINITE VOLUME: Conservation laws, unstructured grids           |
|  MESHLESS: SPH, RKPM -- for large deformations                 |
+------------------------------------------------------------------+
```

---

## Finite Differences

**Basic idea**: Replace derivatives with difference quotients on a uniform grid.

**1D second-order discretization**:

```
  Grid: x_i = a + i h,  i = 0, 1, ..., N+1,  h = (b-a)/(N+1)

  FIRST DERIVATIVE:
  u'(x_i) ≈ (u_{i+1} - u_{i-1}) / (2h)      (central, O(h^2))
  u'(x_i) ≈ (u_{i+1} - u_i) / h              (forward, O(h))
  u'(x_i) ≈ (u_i - u_{i-1}) / h              (backward, O(h))

  SECOND DERIVATIVE:
  u''(x_i) ≈ (u_{i-1} - 2u_i + u_{i+1}) / h^2   (central, O(h^2))

  DERIVATION via Taylor: u(x+h) = u + hu' + h^2u''/2 + h^3u'''/6 + ...
  u(x-h) = u - hu' + h^2u''/2 - h^3u'''/6 + ...
  Subtract: u(x+h) - u(x-h) = 2h u' + O(h^3)  -> first central difference
  Add: u(x+h) + u(x-h) = 2u + h^2 u'' + O(h^4) -> second central difference
```

**Poisson equation -u'' = f on [0,1]** with u(0) = u(1) = 0:

```
  -(u_{i-1} - 2u_i + u_{i+1}) / h^2 = f_i   for i = 1, ..., N

  In matrix form: (1/h^2) * T * u = f
  where T = tridiag(-1, 2, -1) (tridiagonal matrix)

  STRUCTURE:
  T is symmetric positive definite.
  Eigenvalues: lambda_k = 4/h^2 sin^2(k pi h / 2) for k=1,...,N
  Condition number: kappa(T) = O(h^{-2}) = O(N^2) -- grows with grid refinement!
  This is why multigrid or direct solvers are needed for fine grids.

  HIGHER ORDER: O(h^4) scheme uses 5 points:
  u'' ≈ (-u_{i+2} + 16u_{i+1} - 30u_i + 16u_{i-1} - u_{i-2}) / (12h^2)
```

---

## Stability: CFL Condition

For time-dependent PDEs, the spatial discretization is not enough — the TIME STEP must also be chosen carefully for explicit methods.

**Advection equation** u_t + c u_x = 0 with upwind differencing:

```
  (u_i^{n+1} - u_i^n) / dt + c (u_i^n - u_{i-1}^n) / h = 0
  (for c > 0; upwind = backward difference in x)

  u_i^{n+1} = u_i^n - (c dt / h)(u_i^n - u_{i-1}^n)

  Define CFL number: nu = c dt / h

  VON NEUMANN STABILITY ANALYSIS:
  Substitute u_j^n = lambda^n e^{i k j h} (Fourier mode)
  lambda = 1 - nu(1 - e^{-ikh})
  |lambda|^2 = 1 - 2 nu(1-nu)(1 - cos kh)

  STABILITY: |lambda| <= 1 for all k requires nu <= 1.
  CFL CONDITION: dt <= h / c   (time step <= spatial step / wave speed)

  Physical interpretation: information travels at speed c; one time step
  should not move information more than one spatial cell.

  GENERAL CFL:  dt <= h / max_speed  (must respect the fastest wave in the system)
```

**Heat equation** u_t = D u_xx with explicit Euler:

```
  u_i^{n+1} = u_i^n + D dt/h^2 (u_{i-1}^n - 2u_i^n + u_{i+1}^n)

  CFL-like stability: D dt / h^2 <= 1/2   (more restrictive than advection!)

  For d-dimensions: dt <= h^2 / (2d D)

  CONSEQUENCE: To halve h (double resolution) and keep stable:
  must divide dt by 4 (in 2D: by 8). Work scales as h^{-4} in 2D.
  VERY EXPENSIVE for fine grids with explicit methods.
  IMPLICIT METHODS (Crank-Nicolson, BDF): no stability restriction on dt.
```

---

## Crank-Nicolson (Time Discretization)

For parabolic PDEs: average the spatial operator between n and n+1 time levels.

```
  Heat equation: u_t = D u_xx

  EXPLICIT EULER:   (u^{n+1} - u^n)/dt = D u^n_xx         (O(dt), O(h^2))
  IMPLICIT EULER:   (u^{n+1} - u^n)/dt = D u^{n+1}_xx      (O(dt), O(h^2), A-stable)
  CRANK-NICOLSON:   (u^{n+1} - u^n)/dt = D/2 (u^n_xx + u^{n+1}_xx)  (O(dt^2), O(h^2))

  Crank-Nicolson in matrix form:
  (I - dt D/(2h^2) T) u^{n+1} = (I + dt D/(2h^2) T) u^n

  Solve tridiagonal system at each time step.
  STABILITY: UNCONDITIONALLY STABLE for any dt > 0.
  ACCURACY: Second order in both space and time.
  DRAWBACK: Can exhibit oscillations for discontinuous initial data.
             (Crank-Nicolson is A-stable but not L-stable; doesn't damp oscillations.)
```

---

## Finite Element Method

FEM is the dominant method for engineering applications with complex geometry and heterogeneous materials.

**Variational formulation**: Convert the PDE to a weak form.

```
  EXAMPLE: -nabla^2 u = f on Omega, u = 0 on boundary.

  WEAK FORM: Find u in V = H^1_0(Omega) such that for all v in V:
  Integral_Omega nabla u . nabla v dx = Integral_Omega f v dx

  Derivation: multiply PDE by test function v, integrate by parts:
  - Integral nabla^2 u . v dx = Integral nabla u . nabla v dx - Integral_{boundary} (nabla u . n) v dS
  Since v = 0 on boundary: boundary term vanishes.

  The bilinear form a(u,v) = Integral nabla u . nabla v dx and linear form L(v) = Integral f v dx.
  Weak form: a(u,v) = L(v) for all v in V.
```

**Galerkin discretization**:

```
  Approximate u ≈ u_h = Sum_j U_j phi_j  in finite-dimensional V_h subset V

  phi_j: piecewise polynomial basis functions (hat functions, etc.)
  Substituting into weak form:
  Sum_j U_j a(phi_j, phi_i) = L(phi_i) for all i

  In matrix form: K U = F
  K_{ij} = a(phi_j, phi_i)  (stiffness matrix, sparse!)
  F_i = L(phi_i)             (load vector)
  K is symmetric positive definite -> use Cholesky or CG.
```

**FEM mesh types**:

```
  1D: Line elements (intervals)
  2D: Triangular elements (most common), quadrilateral elements
  3D: Tetrahedral elements, hexahedral (brick) elements

  Mesh quality matters: highly elongated elements -> ill-conditioned K.
  Mesh adaptation: refine where error is large, coarsen where error is small.
  Automatic mesh generation: Delaunay triangulation, advancing front.
```

**Error estimate**: For piecewise linear elements (P1) on a shape-regular mesh:

```
  ||u - u_h||_{H^1} <= C h ||u||_{H^2}   (O(h) in H^1 norm)
  ||u - u_h||_{L^2} <= C h^2 ||u||_{H^2}  (O(h^2) in L^2 norm, "superconvergence")

  For higher-order elements (P_k):
  ||u - u_h||_{H^1} <= C h^k ||u||_{H^{k+1}}
```

---

## Spectral Methods

For smooth solutions on regular geometries: spectral methods achieve exponential convergence.

**Fourier spectral method** (periodic domains):

```
  Expand u(x,t) = Sum_k u_hat_k(t) e^{ikx}

  For linear PDE Lu = f:
  Differential operators become algebraic in Fourier space.
  d/dx e^{ikx} = ik e^{ikx} -> d/dx becomes multiplication by ik.
  nabla^2 e^{ikx} = -k^2 e^{ikx}

  Poisson -nabla^2 u = f on [0, 2pi]^d (periodic):
  -(-k^2) u_hat_k = f_hat_k
  u_hat_k = f_hat_k / k^2   (for k != 0)

  CONVERGENCE: For infinitely smooth f: error decreases FASTER THAN ANY POWER of h.
  For analytic f: exponential convergence O(e^{-c N}).

  COST: O(N log N) per time step (FFT).
  Standard for weather prediction, plasma physics, turbulence simulation.
```

**Chebyshev spectral method** (non-periodic):

```
  Expand on [-1,1]: u(x) ≈ Sum_{k=0}^{N} c_k T_k(x)

  Differentiation: spectral differentiation matrix D (N x N dense, but small N sufficient).
  Collocation at Chebyshev-Gauss-Lobatto points x_j = cos(j pi / N).

  CONVERGENCE: Exponential for analytic functions.
  Used in: fluid stability analysis, plasma physics, spectral element methods.
```

---

## Finite Volume Method

Designed for conservation laws (mass, momentum, energy conservation):

```
  CONSERVATION LAW: u_t + div F(u) = 0

  FINITE VOLUME: Integrate over each cell C_i:
  d/dt Integral_{C_i} u dV + Integral_{boundary C_i} F . n dS = 0

  d/dt U_i + (1/|C_i|) Sum_{faces} F_{face} * Area_{face} = 0

  Key: The FLUX F_{face} between adjacent cells must be consistently defined.
  Fluxes automatically conserve: what leaves C_i enters C_{i+1}.

  RIEMANN SOLVERS: Compute the flux between cells by solving the Riemann problem
  (1D: two adjacent constant states, F = ?)
  Exact Riemann solver, Roe solver, HLLC solver.

  UPWIND SCHEMES: For advection, use flux from the "upwind" direction.
  HIGH-RESOLUTION SCHEMES: Combine upwind stability with second-order accuracy.
  Limiters (minmod, superbee) prevent unphysical oscillations.

  Used in: computational fluid dynamics (CFD), weather modeling, astrophysics.
```

---

## Decision Cheat Sheet

| PDE Type | Geometry | Preferred Method |
|---|---|---|
| Elliptic (Poisson, Laplace) | Simple (rectangle) | Finite differences + multigrid |
| Elliptic | Complex/unstructured | Finite element method |
| Parabolic (heat), small to medium | Regular | FD with Crank-Nicolson |
| Parabolic, complex geometry | Any | FEM + implicit time integration |
| Hyperbolic (wave), smooth | Periodic | Spectral (Fourier) |
| Hyperbolic, conservation law | Any | Finite volume + Riemann solver |
| Navier-Stokes (turbulence) | Simple, turbulence | Spectral / pseudo-spectral |
| Navier-Stokes, engineering | Complex geometry | FVM (OpenFOAM, Fluent) |
| Elasticity, structural | Complex 3D | FEM (ANSYS, Abaqus, FEniCS) |
| High accuracy, smooth solution | Simple | Spectral element method |

---

## Common Confusion Points

**"Finite differences are less accurate than FEM."**
Not inherently. On uniform grids with smooth solutions, FD and FEM of the same order achieve the same accuracy. FEM's advantage is flexibility with complex geometry and the variational framework providing clean error bounds. For structured grids, FD is simpler and often faster.

**"The CFL condition limits accuracy."**
The CFL condition limits the maximum stable time step, not accuracy per se. Using dt = CFL * h / c is stable; using dt = 0.1 * CFL * h / c is more accurate (and still stable). For smooth solutions, accuracy improves as both h and dt are refined. The CFL only constrains the ratio dt/h for stability.

**"Spectral methods are always better."**
Only for smooth solutions on regular domains. Spectral methods lose their exponential convergence when: (1) the solution has discontinuities or steep gradients, (2) the domain is complex (needs geometrical flexibility of FEM/FVM). For turbulent flows: spectral methods in simple geometries (DNS), FVM in complex geometries (LES).

**"FEM gives the exact solution."**
FEM gives the best approximation in the finite-dimensional subspace V_h — it minimizes the error in the energy norm over V_h. This is the "Galerkin orthogonality" property. But it is still an approximation: the true solution u is in the infinite-dimensional H^1_0, not V_h.
