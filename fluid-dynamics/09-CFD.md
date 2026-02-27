# Computational Fluid Dynamics

## The Big Picture

CFD is the numerical solution of the governing equations of fluid dynamics. It is the "third pillar" of fluid mechanics alongside theory and experiment. The field connects fluid physics to algorithm design: different equation types require different discretization strategies, and the nonlinearity of Navier-Stokes imposes unique stability constraints. From the MIT TCS background, CFD is applied numerical linear algebra + time-stepping algorithms + domain decomposition — running at petascale and beyond.

<!-- @editor[content/P2]: The opening correctly frames CFD as "domain decomposition — running at petascale and beyond" but the file never delivers on this: no section on parallel CFD, MPI communication patterns, halo-cell exchange, or the parallel scaling challenges (communication vs compute, Amdahl's law on the Poisson solve). This is precisely the bridge the learner calibration calls out ("CFD → parallel computing patterns they know from Azure"). The intro promise is unmet. Add a section on parallel CFD: domain decomposition, halo exchange, why the pressure Poisson solve is the parallel bottleneck (global reduction), and how modern CFD codes (OpenFOAM, Nek5000) achieve near-linear scaling to 10⁴–10⁵ cores. -->

```
CFD PIPELINE
═══════════════════════════════════════════════════════════════════════════════

  PHYSICS PROBLEM                  NUMERICAL APPROACH
  ─────────────────────────────    ─────────────────────────────────────────
  Continuous domain Ω              Mesh (grid): discretize Ω into cells/nodes
  PDE: ∂φ/∂t + N(φ) = 0          Discrete equations: Σ aᵢⱼφⱼ = bᵢ
  Boundary conditions              Boundary condition enforcement
  Initial conditions               Time integration: explicit or implicit
  Analytical solution (rare)       Iterative solver: AMG, Krylov, Newton

  MAIN DISCRETIZATION METHODS:
  ┌────────────────────────────────────────────────────────────────────┐
  │  FDM  Finite Difference Method   (structured grids, simple)        │
  │  FVM  Finite Volume Method       (conservation, unstructured OK)   │
  │  FEM  Finite Element Method      (variational, complex geometry)   │
  │  SM   Spectral Methods           (smooth problems, high accuracy)  │
  └────────────────────────────────────────────────────────────────────┘
```

---

## Finite Difference Method (FDM)

Approximate derivatives by finite differences on a structured grid.

**First derivative** (central, 2nd-order accurate):

    ∂u/∂x|ᵢ ≈ (uᵢ₊₁ − uᵢ₋₁) / (2Δx)    + O(Δx²)

**Second derivative** (central, 2nd-order):

    ∂²u/∂x²|ᵢ ≈ (uᵢ₊₁ − 2uᵢ + uᵢ₋₁) / Δx²    + O(Δx²)

**FDM for Laplace (Poisson solver)**:

    ∇²u = 0  →  (uᵢ₊₁,ⱼ + uᵢ₋₁,ⱼ + uᵢ,ⱼ₊₁ + uᵢ,ⱼ₋₁ − 4uᵢ,ⱼ) / Δx² = 0

This is the discrete 5-point stencil for Laplace in 2D. Results in a banded sparse linear system.

**Advantages**: Simple to implement, easy to analyze (von Neumann stability), high-order variants straightforward.

**Limitations**: Requires structured (orthogonal) grids. Complex geometry (airfoil shapes, branching pipes) is difficult.

---

## Finite Volume Method (FVM)

The dominant method for engineering CFD. Based on integrating the conservation law over discrete control volumes (cells).

**Control volume form** of mass conservation:

    d/dt ∫∫∫_V ρ dV + ∯_{∂V} ρ**v**·**n** dA = 0

**Discretize**: sum over faces of each cell:

    d(ρᵢ Vᵢ)/dt + Σ_{faces} ρ_f **v**_f · **A**_f = 0

where subscript f = face centroid value, **A**_f = face area vector.

```
FVM CONTROL VOLUME:

     N (north)
      │
  W ──●── E    ● = cell center  (where unknowns are stored)
      │         face fluxes computed between adjacent cells
     S (south)

  Flux through East face = ρ_E u_E A_E
  Net flux ≠ 0 → cell value changes
```

**Key features**:
- Exactly conserves mass, momentum, energy over each cell and globally
- Works on unstructured meshes (triangles, tetrahedra, polyhedra)
- Naturally handles complex geometry
- Industry standard for industrial CFD (OpenFOAM, ANSYS Fluent, CFX)

**Reconstruction**: How to compute face values from cell-center values — first-order (upwind), second-order (linear interpolation + limiters), higher-order (ENO/WENO for shocks).

---

## Finite Element Method (FEM)

Based on variational (weak) formulation. Dominant in structural mechanics; used in CFD for incompressible flows.

**Weak form** of Navier-Stokes: multiply by test function w, integrate by parts:

    ∫_Ω ρ(∂u/∂t + u·∇u)·w dΩ = ∫_Ω (−p∇·w + ν∇u:∇w) dΩ + boundary terms

**Galerkin discretization**: expand u ≈ Σ uᵢ φᵢ(x) where φᵢ are basis functions (shape functions). Substitute and use w = φⱼ:

    M du/dt + K(u)u + Gp = f    (after discretization)
    Bᵀu = 0    (incompressibility, B = divergence operator matrix)

**Saddle-point problem**: The inf-sup (LBB) condition must be satisfied — the pressure and velocity spaces cannot be chosen independently. Violating this leads to spurious pressure modes. Standard choice: Taylor-Hood elements (P2/P1 — quadratic velocity, linear pressure).

**Stabilized FEM**: SUPG (Streamline-Upwind Petrov-Galerkin) adds artificial diffusion in the streamline direction to stabilize convection-dominated flows.

---

## Spectral Methods

For smooth problems on simple domains, spectral methods achieve **exponential convergence** — error decreases as e^{-N} where N is the number of modes. Compare with polynomial convergence O(Δx^p) for FDM/FVM.

**Fourier spectral method** (periodic problems):

    u(x) = Σ_{k=-N/2}^{N/2} û_k e^{ikx}

Derivatives: ∂u/∂x → iku (exact in spectral space)
Time advance in spectral space, multiply by ik each time step.

**Chebyshev spectral method** (non-periodic, bounded domain):

    u(x) = Σ_n c_n T_n(x)   (T_n = Chebyshev polynomials)

Collocation at Chebyshev points: xⱼ = cos(jπ/N) for j = 0, ..., N.

**Spectral Element Method**: Divide domain into elements; use high-order Chebyshev within each element. Gets geometric flexibility of FEM + accuracy of spectral.

```
ACCURACY COMPARISON:
  FDM/FVM, order p:   error ~ Δx^p   (algebraic decay)
  Spectral:           error ~ e^{-αN}  (exponential decay, for smooth f)

  For 6-digit accuracy:
  FDM 2nd order:  need N ~ 10^3 points per dimension  → 10^9 in 3D
  Spectral:       need N ~ 50 points per dimension     → 10^5 in 3D  (!!)

  But: spectral fails for non-smooth problems (shocks → Gibbs phenomenon)
```

---

## Pressure-Velocity Coupling (Incompressible)

The incompressibility constraint ∇·**v** = 0 is a constraint on velocity, not directly an equation for pressure. This creates the pressure-velocity coupling problem.

### Projection (Fractional Step) Method

1. **Predict**: u* = uⁿ + Δt[advection + viscous] (ignoring pressure)
2. **Correct**: Solve ∇²p^{n+1} = (1/Δt)∇·u*  (Poisson equation for pressure)
3. **Update**: u^{n+1} = u* − Δt∇p^{n+1}

Step 2 is a Poisson solve — the computational bottleneck. Uses FFT (periodic), multigrid, or direct sparse solver.
<!-- @editor[bridge/P3]: Mention of "multigrid, Krylov, direct sparse solver" is correct but left as a bare list. Learner has numerical methods background; a one-sentence bridge connecting multigrid to the algebraic multigrid (AMG) preconditioners used in production CFD (same as used in PETSc, Trilinos, Azure HPC workloads), and noting that the Poisson solve is why the pressure equation is the parallel bottleneck (requires global information vs local flux computation), would ground these references. -->

### SIMPLE Algorithm (Semi-Implicit Method for Pressure-Linked Equations)

Iterative method for steady-state problems:
1. Guess p*
2. Solve momentum → u*
3. Solve pressure correction equation
4. Update p, u
5. Repeat until convergence

SIMPLE, SIMPLEC, PISO — variants used in most commercial CFD codes.

---

## Time Integration

**Explicit methods** (e.g., Runge-Kutta 4):

    u^{n+1} = u^n + Δt F(u^n, tⁿ)  [RK4 is 4-stage]

Stability: Δt < CFL condition:

    CFL = |u|Δt/Δx < 1  (advection)    and    ν Δt/Δx² < 0.5  (diffusion)

**Limitation**: viscosity imposes severe time step restriction (Δt ~ Δx²/ν) for fine grids.

**Implicit methods** (e.g., Crank-Nicolson, backwards Euler):

    u^{n+1} = u^n + Δt F(u^{n+1}, t^{n+1})  [fully implicit: solve system at each step]

Unconditionally stable (no CFL restriction). But: nonlinear system at each step → Newton iterations.

**Semi-implicit**: Treat viscous term implicitly (no diffusion CFL), advection explicitly. Best of both worlds for low-Re flows.

---

## Turbulence Modeling in CFD

As discussed in 05-TURBULENCE.md:

```
TURBULENCE MODELING OPTIONS IN CFD:
  Method     What's resolved  What's modeled   Cost ratio
  ─────────────────────────────────────────────────────────
  DNS        Everything       Nothing          Re^{11/4}
  LES        l > Δ            l < Δ           Re^{1.8}
  RANS       Mean only        All turbulence   1 (baseline)
  DES/DDES   LES far from wall  RANS near wall   moderate

  Industrial standard: k-ω SST RANS for most engineering problems
  Research trend: wall-modeled LES as computing power grows
```

**y⁺ requirement** (near-wall resolution):
- Low-Re RANS (resolves viscous sublayer): y⁺ < 1
- High-Re RANS with wall functions: 30 < y⁺ < 300
- LES: y⁺ ~ 1 or use wall models (y⁺ ~ 30–50)

Getting y⁺ wrong is one of the most common CFD user errors.

---

## Mesh Generation

**Structured meshes**: logically regular grid (i,j,k indices). Efficient for simple geometry. Algebraic, elliptic, or hyperbolic generation.

**Unstructured meshes**: arbitrary connectivity. Flexible for complex geometry. Delaunay triangulation (2D), Delaunay tetrahedralization (3D), advancing front.

**Hybrid meshes**: structured near walls (prism layers for boundary layer resolution) + unstructured elsewhere. Best of both worlds for industrial CFD.

```
MESH QUALITY METRICS:
  Aspect ratio:   cell should be close to equilateral (AR ~ 1)
                  except in BL where AR can be 1000:1 (thin, elongated)
  Skewness:       cell should not be too skewed (< 0.85 typically)
  Orthogonality:  faces should be perpendicular to cell-center line
  y⁺:            first cell height at walls (matches turbulence model)
```

---

## CFD Software Landscape

```
OPEN SOURCE:
  OpenFOAM      FVM, C++, everything, widely used in academia and industry
  SU2           FVM/FEM, unstructured, aerospace focus, gradient-based optimization
  FEniCS        FEM, Python, research
  Nek5000       Spectral element, DNS/LES, high performance

COMMERCIAL:
  ANSYS Fluent  FVM, dominant industrial CFD
  ANSYS CFX     FVM, element-based FVM, strong for turbomachinery
  STAR-CCM+     FVM, strong for vehicle aerodynamics, Siemens
  Comsol        FEM, multiphysics, simulation + design

SPECIALIZED:
  OpenLB        Lattice Boltzmann (mesoscale physics)
  PALM          Atmospheric boundary layer LES
  AMREX/PeleC   Adaptive mesh refinement, reacting flows
  NEKTAR++      Spectral/hp element, high-order
```

---

## Verification and Validation (V&V)

**Verification**: Are we solving the equations right? (Code correctness)
- Grid convergence study: refine mesh → check if solution converges at expected rate
- Method of Manufactured Solutions (MMS): fabricate exact solution; verify code recovers it
- Order of convergence: ε ~ Δx^p; verify p matches theory

**Validation**: Are we solving the right equations? (Model accuracy)
- Compare CFD to experiment
- Assess uncertainty: numerical error + modeling error + measurement error
- Define validation metrics: local quantities, integral forces, spectra

```
GRID CONVERGENCE STUDY (Richardson extrapolation):
  Run simulation on three meshes: h₁ < h₂ < h₃ (refine by factor r)
  If converging at order p:
    φ_h ≈ φ_exact + C hᵖ

  Estimate exact: φ_exact ≈ φ₁ + (φ₁ − φ₂)/(r^p − 1)  (Richardson)
  Report GCI (Grid Convergence Index) as error estimate
```

---

## Decision Cheat Sheet

| Need to... | Method |
|-----------|-------|
| Simple geometry, high accuracy | FDM (structured, high-order) |
| Complex geometry, conservation | FVM (unstructured) |
| Solid mechanics compatibility, incompressible | FEM |
| Very high accuracy, smooth flow | Spectral / Spectral element |
| Industrial turbulent flow | RANS (k-ω SST) with FVM |
| Time-accurate turbulence | LES or hybrid DES |
| Incompressible time advance | Projection method (Poisson for pressure) |
| Steady-state incompressible | SIMPLE algorithm |
| Assess solution accuracy | Grid convergence study + Richardson extrapolation |

---

## Common Confusion Points

**FVM conserves quantities; FDM does not inherently**: FVM is built on integral conservation laws, so mass, momentum, and energy are conserved for each cell exactly. FDM is a pointwise approximation — it can be conservative if carefully formulated, but it's not automatic.

**CFL condition is necessary but not sufficient for stability**: The CFL condition limits the time step for advection. But for Navier-Stokes, viscous stability (Δt < Δx²/ν) is often more restrictive. And for nonlinear problems, the stability limit can be hard to predict analytically.

**Convergence of iterative solvers vs convergence of solution**: SIMPLE algorithm converges iteratively toward a steady state. Grid convergence studies check that the converged solution changes as the mesh is refined. Both must be checked: a well-converged iterative solution on a coarse mesh is still a coarse-mesh result.

**y⁺ is not a global target but a local one**: y⁺ = y u_τ/ν depends on the local friction velocity u_τ = √(τ_w/ρ), which varies over the surface. The first cell height Δy must be chosen to put the first cell center in the target y⁺ range everywhere. This requires an estimate of u_τ at each wall location before meshing.
