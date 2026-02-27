# Partial Differential Equations — Landscape and Taxonomy

## The Big Picture

PDEs are equations that relate an unknown function of **multiple variables** to its partial
derivatives. They are the native language of physics: every fundamental field equation is a PDE.

```
+------------------------------------------------------------------------------+
|                    THE PDE LANDSCAPE                                          |
|                                                                              |
|   TYPE          CANONICAL EQUATION               PHYSICS                     |
|   ----          ------------------               -------                     |
|                                                                              |
|   ELLIPTIC      ∇²u = 0   (Laplace)              Electrostatics,             |
|   (steady)      ∇²u = f   (Poisson)              steady heat,                |
|                                                  Newtonian gravity            |
|                                                                              |
|   PARABOLIC     ∂u/∂t = α∇²u                     Heat diffusion,             |
|   (evolution,   (Heat / diffusion)               Brownian motion,            |
|    irreversible)                                  Schrödinger (imag t)       |
|                                                                              |
|   HYPERBOLIC    ∂²u/∂t² = c²∇²u                  Sound, light,               |
|   (wave         (Wave equation)                  seismic waves,              |
|    propagation)                                  electromagnetism            |
|                                                                              |
|   MIXED / NONLINEAR                                                          |
|   Navier-Stokes  ∂u/∂t + (u·∇)u = −∇p + ν∇²u   Fluid mechanics             |
|   KdV            u_t + 6u·u_x + u_xxx = 0        Solitons                   |
|   Schrödinger    iℏ∂ψ/∂t = Ĥψ                   Quantum mechanics           |
|   Einstein       G_μν = 8πT_μν                   General relativity          |
|   Black-Scholes  V_t + ½σ²S²V_SS + rSV_S − rV=0 Financial derivatives       |
|                                                                              |
+------------------------------------------------------------------------------+
```

The classification (elliptic / parabolic / hyperbolic) is not a bureaucratic label — it
determines what boundary conditions are appropriate, whether solutions exist and are unique,
how information propagates through the domain, and which numerical methods work.

---

## Classification Axes

### Order and Linearity

```
+----------------------------------------------------------+
|  ORDER = highest derivative appearing                     |
|                                                          |
|  1st order:   u_x + u_y = 0             (transport)     |
|  2nd order:   u_xx + u_yy = 0           (Laplace)       |
|  4th order:   u_xxxx + 2u_xxyy + u_yyyy = 0  (biharmonic)|
|                                                          |
|  LINEARITY                                               |
|                                                          |
|  Linear:       L[u] = 0  where L is a linear operator   |
|                L[αu + βv] = αL[u] + βL[v]               |
|                → superposition holds                     |
|                → powerful analytical toolkit             |
|                                                          |
|  Semilinear:   linear in highest derivatives,            |
|                nonlinear in lower:                       |
|                u_xx + u_yy = f(x, y, u, u_x)            |
|                                                          |
|  Quasilinear:  coefficients depend on u and lower        |
|                derivatives but not highest:              |
|                A(u)u_xx + B(u)u_yy = 0                  |
|                                                          |
|  Fully nonlinear: nonlinear in highest derivatives:      |
|                u_xx · u_yy − u_xy² = f  (Monge-Ampère)  |
|                                                          |
+----------------------------------------------------------+
```

### The Discriminant (2nd-Order, 2 Variables)

The general second-order linear PDE in two variables:

```
  Au_xx + 2Bu_xy + Cu_yy + Du_x + Eu_y + Fu = G

  DISCRIMINANT:  Δ = B² − AC

    Δ < 0   →   ELLIPTIC
    Δ = 0   →   PARABOLIC
    Δ > 0   →   HYPERBOLIC

  CANONICAL EXAMPLES:
    Laplace   u_xx + u_yy = 0:     A=1, B=0, C=1   → Δ = −1 < 0   ELLIPTIC
    Heat      u_t − u_xx = 0:      A=−1,B=0, C=0   → Δ =  0 = 0   PARABOLIC
    Wave      u_tt − u_xx = 0:     A=1, B=0, C=−1  → Δ =  1 > 0   HYPERBOLIC
```

Note: the classification can change with location for variable-coefficient PDEs (e.g.,
the Tricomi equation u_xx + xu_yy = 0 is elliptic for x>0, parabolic at x=0, hyperbolic
for x<0).

---

## Solution Strategy Map

```
+-----------------------------------------------------------------------+
|                    HOW TO APPROACH A PDE                               |
|                                                                       |
|   Step 1: Classify type                                               |
|   +-----------+   +-----------+   +-----------+                       |
|   | ELLIPTIC  |   | PARABOLIC |   | HYPERBOLIC|                       |
|   +-----------+   +-----------+   +-----------+                       |
|        |               |               |                              |
|   Step 2: Choose analytical method                                    |
|        |               |               |                              |
|   Separation    Separation +    Separation +                          |
|   of variables  Fourier series  d'Alembert                            |
|   Green's fn    Heat kernel     Characteristics                       |
|   Potential     Fourier/Laplace Fourier transform                     |
|   theory        transform       Riemann method                        |
|        |               |               |                              |
|   Step 3: Numerical (when analytic fails)                             |
|   FEM (dominant)  FD implicit   FD explicit + CFL                     |
|   BEM             Crank-Nicolson Godunov / upwind                     |
|   Spectral        Spectral      Spectral                              |
|        |               |               |                              |
|   Step 4: Specify boundary / initial conditions                       |
|   +-----------------+  +--------------------+                         |
|   | Dirichlet: u=g  |  | Neumann: ∂u/∂n = h |                        |
|   | (value given)   |  | (flux given)        |                        |
|   +-----------------+  +--------------------+                         |
|   +-------------------+  +-----------------------+                    |
|   | Robin: ∂u/∂n+αu=g |  | Cauchy: u and ∂u/∂n   |                   |
|   | (mixed)            |  | both given            |                   |
|   +-------------------+  | (ok for hyperbolic;    |                   |
|                           |  ill-posed for ellip!) |                   |
|                           +-----------------------+                    |
+-----------------------------------------------------------------------+
```

---

## The Core Equations: Reference Table

```
+-------------+-------------------------------------------+---------------------+
| EQUATION    | FORM                                      | MODELS              |
+-------------+-------------------------------------------+---------------------+
| Laplace     | ∇²u = 0                                   | Electrostatic pot., |
|             | u_xx + u_yy + u_zz = 0                    | steady-state heat,  |
|             |                                           | irrotational flow   |
+-------------+-------------------------------------------+---------------------+
| Poisson     | ∇²u = f(x)                                | Gravity potential,  |
|             |                                           | charge distribution |
+-------------+-------------------------------------------+---------------------+
| Heat        | u_t = α∇²u                                | Diffusion,          |
|             | (α = thermal diffusivity > 0)             | Brownian motion,    |
|             |                                           | chemical diffusion  |
+-------------+-------------------------------------------+---------------------+
| Wave        | u_tt = c²∇²u                              | Acoustics, EM,      |
|             | (c = wave speed)                          | seismics, strings   |
+-------------+-------------------------------------------+---------------------+
| Helmholtz   | ∇²u + k²u = 0                             | Time-harmonic       |
|             | (wave eq. with u ~ e^{iωt} ansatz)        | wave scattering     |
+-------------+-------------------------------------------+---------------------+
| Schrödinger | iℏ ψ_t = −(ℏ²/2m)∇²ψ + Vψ               | Quantum mechanics   |
|             | (parabolic in imaginary time)             | electron dynamics   |
+-------------+-------------------------------------------+---------------------+
| Navier-Stokes| u_t + (u·∇)u = −∇p/ρ + ν∇²u            | Viscous fluid flow  |
|             | ∇·u = 0 (incompressible)                  | (existence/smooth.  |
|             |                                           |  in 3D: open!)      |
+-------------+-------------------------------------------+---------------------+
| Burgers     | u_t + u·u_x = ν·u_xx                      | Shock formation,    |
|             | (ν=0: inviscid Burgers)                   | turbulence model    |
+-------------+-------------------------------------------+---------------------+
| KdV         | u_t + 6u·u_x + u_xxx = 0                  | Solitons, shallow   |
|             |                                           | water waves         |
+-------------+-------------------------------------------+---------------------+
| Biharmonic  | ∇⁴u = ∇²(∇²u) = 0                        | Elasticity, Stokes  |
|             |                                           | slow viscous flow   |
+-------------+-------------------------------------------+---------------------+
| Eikonal     | |∇u|² = n(x)²  (n = refractive index)    | Geometric optics,   |
|             | (nonlinear 1st order)                     | ray tracing         |
+-------------+-------------------------------------------+---------------------+
```

---

<!-- @editor[diagram/P2]: The Solution Strategy Map and Analytical Toolkit diagram cover only classical analytical methods. For this learner, the landscape is incomplete without modern PDE theory (Sobolev spaces, weak formulations, elliptic regularity) and ML-based approaches (PINNs, neural operators, diffusion models as SDEs) visible at the overview level. The diagram presents the field as if numerical methods are a fallback after analytical methods fail — not as a first-class domain. Rework to show the modern theory layer alongside the classical layer. -->

## Key Analytical Tools

```
+------------------------------------------------------------------+
|                   ANALYTICAL TOOLKIT                              |
|                                                                  |
|  SEPARATION OF VARIABLES                                         |
|  Assumes u(x,t) = X(x)·T(t)  (or X(x)·Y(y) etc.)              |
|  Reduces PDE → coupled system of ODEs                            |
|  Works on: rectangular, cylindrical, spherical domains           |
|  Produces: eigenfunction expansions                              |
|                                                                  |
|  FOURIER SERIES / TRANSFORM                                      |
|  Represent solution as superposition of modes                    |
|  Finite domain  → Fourier series (discrete spectrum)            |
|  Infinite domain → Fourier transform (continuous spectrum)      |
|  Turns ∂/∂x into multiplication by ik                           |
|  Turns ∂²/∂x² into multiplication by −k²                       |
|                                                                  |
|  GREEN'S FUNCTIONS                                               |
|  G(x,y) = response at x to point source at y                    |
|  Solution: u(x) = ∫ G(x,y) f(y) dy                              |
|  Think: impulse response / convolution kernel                    |
|  (Same concept as transfer function in systems/controls)         |
|                                                                  |
|  METHOD OF CHARACTERISTICS                                       |
|  First-order PDEs: follow characteristic curves                  |
|  PDE becomes ODE along characteristics                           |
|  Reveals shock formation (when characteristics cross)            |
|                                                                  |
|  TRANSFORM METHODS                                               |
|  Laplace: converts t-derivative to algebraic in s               |
|  Fourier: converts x-derivative to algebraic in k               |
|  Reduces PDE → ODE or algebraic equation                         |
|                                                                  |
+------------------------------------------------------------------+
```

<!-- @editor[content/P2]: The overview makes no mention of ML-based PDE approaches at the landscape level. Physics-Informed Neural Networks (PINNs), Fourier Neural Operators (FNO), DeepONet, and diffusion models as SDEs (the heat equation as the forward noising process in score-based generative models) are significant modern developments explicitly needed by this learner. These should appear alongside classical methods in the overview — not deferred to individual files. -->

---

## Well-Posedness (Hadamard, 1902)

A PDE problem is **well-posed** if it has:
1. **Existence** — a solution exists
2. **Uniqueness** — only one solution
3. **Stability** — small changes in data produce small changes in solution

```
+--------------------------------------------------+
|  BOUNDARY CONDITIONS AND WELL-POSEDNESS           |
|                                                  |
|  ELLIPTIC (Laplace, Poisson):                    |
|   Appropriate: boundary of entire domain Ω       |
|   ✓ Dirichlet:  u = g on ∂Ω                     |
|   ✓ Neumann:    ∂u/∂n = h on ∂Ω                 |
|   ✓ Robin:      ∂u/∂n + αu = g on ∂Ω            |
|   ✗ Cauchy:     both u and ∂u/∂n → ill-posed     |
|                                                  |
|  PARABOLIC (Heat):                               |
|   ✓ IC: u(x,0) = u₀(x)  (initial data)          |
|   ✓ BC: Dirichlet or Neumann on spatial ∂Ω      |
|   ✗ Final-time data: ill-posed (backward heat)   |
|                                                  |
|  HYPERBOLIC (Wave):                              |
|   ✓ Cauchy IVP: u(x,0) = u₀, u_t(x,0) = v₀     |
|   ✓ Mixed: Cauchy IC + spatial boundary for Ω   |
|   ✓ Characteristic BCs for outflow boundaries   |
|                                                  |
+--------------------------------------------------+
```

---

## Information Propagation: The Core Physical Intuition

```
  ELLIPTIC: Information propagates INSTANTLY everywhere.

  +---------+    Change a boundary value → entire interior adjusts
  |         |    immediately. No preferred direction. No "time".
  |    ·    |    Solution at any point depends on ALL boundary data.
  |         |    Think: soap film on a wire frame. Equilibrium.
  +---------+


  PARABOLIC: Information propagates at INFINITE speed but decays.

  t=0:   ─────────────────[spike]────────────────── x
  t=ε:   ──────────────[Gaussian]────────────────── x
  t=T:   ─────────────────[flat]──────────────────── x

  Every point is immediately influenced by the spike.
  But influence diminishes exponentially with distance.
  Irreversible: running time backward is ill-posed.


  HYPERBOLIC: Information propagates at FINITE speed c.

  t=0:   ──────────────[spike at x=0]───────────── x
  t=1:   ────────────────────X──────────────────── x (nothing outside)
                           [−c,+c]
  t=2:   ─────────────────X─────X──────────────── x
                         [−2c] [+2c]

  Domain of influence: forward light cone.
  Domain of dependence: backward light cone.
  Outside the cone: EXACTLY zero effect (causality).
```

---

## This Directory

| File | Topic |
|------|-------|
| 00-OVERVIEW.md | This file — landscape and taxonomy |
| 01-CLASSIFICATION.md | Classification and well-posedness in depth |
| 02-FIRST-ORDER.md | First-order PDEs, method of characteristics |
| 03-WAVE-EQUATION.md | Wave equation and hyperbolic systems |
| 04-HEAT-EQUATION.md | Heat equation and parabolic systems |
| 05-LAPLACE-POISSON.md | Laplace and Poisson equations |
| 06-FOURIER-METHODS.md | Fourier methods and separation of variables |
| 07-GREENS-FUNCTIONS.md | Green's functions and distributions |
| 08-VARIATIONAL-WEAK.md | Weak formulations, Sobolev spaces, FEM foundation |
| 09-NUMERICAL-PDES.md | Numerical methods for PDEs |

---

## Decision Cheat Sheet

| I want to model... | Equation | Boundary conditions |
|--------------------|----------|---------------------|
| Steady-state temperature / electrostatics | Laplace / Poisson (elliptic) | Boundary values or fluxes on ∂Ω |
| Diffusion over time | Heat equation (parabolic) | IC + spatial BCs |
| Wave propagation, acoustics | Wave equation (hyperbolic) | IC (position + velocity) |
| Time-harmonic waves / resonance modes | Helmholtz ∇²u + k²u = 0 | Radiation or Dirichlet |
| Quantum particle dynamics | Schrödinger (parabolic) | IC (wavefunction) |
| Viscous fluid flow | Navier-Stokes (nonlinear parabolic) | No-slip + IC |
| Shock waves, traffic flow | Inviscid Burgers (nonlinear hyperbolic) | Characteristics + entropy |
| Soliton / nonlinear waves | KdV | Periodic or decaying IC |
| Elasticity / plate bending | Biharmonic | Clamped or free BCs |

---

## Common Confusion Points

**"Is the heat equation parabolic? It has time in it."**
The presence of a first-order time derivative with a second-order space derivative is exactly
the parabolic signature. The wave equation has second-order time derivative (hyperbolic). That
difference in time-derivative order is why heat flow is irreversible and wave propagation is not.

**"Can I specify both Dirichlet and Neumann conditions on the same boundary?"**
For elliptic problems: no. Specifying both is Cauchy data, and the elliptic Cauchy problem is
generically ill-posed (Holmgren's theorem). On a given boundary piece you get either the value
or the flux, not both.

**"Why is Navier-Stokes a Millennium Prize problem if we solve it numerically all the time?"**
Numerical solutions exist. The open question is mathematical: does a smooth (C∞) solution
always exist in 3D for all time for smooth initial data, or do singularities form? The
numerics don't resolve the theoretical question — they can miss or smooth singularities.

**"What does the Laplacian ∇² actually measure?"**
At any point x, ∇²u(x) = limit as r→0 of [average of u on sphere of radius r around x]
minus u(x), divided by r²/2n (n = dimension). It is the difference between u at a point
and its local average. Laplace equation ∇²u=0 says u equals its local average — that's the
mean value property of harmonic functions.
