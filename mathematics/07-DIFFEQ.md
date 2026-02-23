# 07 — Differential Equations: ODEs, PDEs, and the Equations of Physics

```
THE LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  ORDINARY DEs (one variable)          PARTIAL DEs (multiple variables)
  ┌──────────────────────────┐          ┌────────────────────────────────┐
  │ 1st order                │          │ Elliptic:  ∇²u = f  (Laplace) │
  │  separable               │          │ Parabolic: ∂u/∂t = α∇²u (heat)│
  │  linear (integrating μ)  │          │ Hyperbolic: ∂²u/∂t² = c²∇²u  │
  │  exact                   │          │            (wave equation)     │
  │ 2nd order                │          └────────────────────────────────┘
  │  constant coefficients   │
  │  undetermined coeff.     │          SOLUTION METHODS
  │  variation of parameters │          ┌────────────────────────────────┐
  │ Systems of ODEs          │          │ Separation of variables        │
  │  phase plane / stability │          │ Fourier series / transform     │
  └──────────────────────────┘          │ Green's functions              │
                                        │ Numerical (FEM, FDM)          │
  EVERY PHYSICS MODULE YOU'VE READ CONTAINS AT LEAST ONE DE:            │
  Newton F=ma, Maxwell ∂E/∂t, Schrödinger iℏ∂ψ/∂t, diffusion ∂T/∂t   │
  ─────────────────────────────────────────────────────────────────────┘
═══════════════════════════════════════════════════════════════════════════════
```

---

## 1. First-Order ODEs

An ODE is **first-order** if only y and y' appear (no y'', etc.).

### 1.1 Separable Equations

```
  FORM: dy/dx = f(x)·g(y)

  TECHNIQUE: separate variables, integrate both sides

  dy/g(y) = f(x) dx  →  ∫ dy/g(y) = ∫ f(x) dx

  EXAMPLE: RC circuit charging  (electronics bridge)
  C dV/dt = (V₀ - V)/R  →  dV/(V₀-V) = dt/RC
  -ln|V₀-V| = t/RC + C₁
  V(t) = V₀(1 - e^(-t/RC))     ← the exponential approach to equilibrium

  EXAMPLE: Radioactive decay
  dN/dt = -λN  →  dN/N = -λ dt  →  N(t) = N₀ e^(-λt)

  EXAMPLE: Logistic growth
  dP/dt = rP(1 - P/K)
  Separable; solution: P(t) = K/(1 + ((K-P₀)/P₀)e^(-rt))
```

### 1.2 Linear First-Order: The Integrating Factor

```
  FORM: dy/dx + P(x)y = Q(x)   (linear — y appears only to first power)

  TECHNIQUE: multiply both sides by integrating factor μ(x) = e^(∫P dx)

  d/dx[μy] = μQ(x)
  μy = ∫μQ dx  →  y = (1/μ)∫μQ dx

  WHY IT WORKS:
  d/dx[μy] = μy' + μ'y = μ(y' + (μ'/μ)y) = μ(y' + Py)
  We need μ'/μ = P, so μ = e^(∫P dx). Then d/dx[μy] = μQ, integrate directly.

  EXAMPLE: Newton's law of cooling
  dT/dt + (h/mc)T = (h/mc)T_env
  P = h/mc (constant), Q = (h/mc)T_env
  μ = e^(ht/mc)
  T(t) = T_env + (T₀ - T_env)e^(-ht/mc)    ← exponential approach
```

### 1.3 Exact Equations

```
  FORM: M(x,y) dx + N(x,y) dy = 0
  EXACT IF: ∂M/∂y = ∂N/∂x  (mixed partials equal — conservative force!)

  Then ∃ F(x,y) such that ∂F/∂x = M, ∂F/∂y = N
  Solution: F(x,y) = C

  CONNECTION TO PHYSICS: a force F = (Fx, Fy) is conservative iff
  ∂Fy/∂x = ∂Fx/∂y  (curl = 0 in 2D)
  Then F = -∇V for some potential V — same structure as exact equations.
```

### 1.4 Existence and Uniqueness

```
  PICARD'S THEOREM:
  If f and ∂f/∂y are continuous near (x₀, y₀), then
  y' = f(x,y),  y(x₀) = y₀
  has a unique solution in some interval around x₀.

  This fails when:
  ├── f is discontinuous (e.g., y' = 1/x at x=0)
  ├── ∂f/∂y blows up (e.g., y' = y^(1/3) at y=0 → multiple solutions)
  └── Solution blows up in finite time (e.g., y' = y², y(0)=1 → y=1/(1-x))
```

---

## 2. Second-Order Linear ODEs

The workhorse of physics: harmonic oscillators, beams, circuits.

```
  GENERAL FORM:
  a(x)y'' + b(x)y' + c(x)y = f(x)

  Homogeneous: f(x) = 0
  Constant coefficients: a, b, c are constants
```

### 2.1 Constant Coefficients — Characteristic Equation

```
  ay'' + by' + cy = 0

  Guess y = e^(rx):  ar² + br + c = 0   ← characteristic equation

  Three cases (discriminant Δ = b² - 4ac):

  CASE 1: Δ > 0   two real roots r₁ ≠ r₂
  y = C₁e^(r₁x) + C₂e^(r₂x)
  Physics: overdamped oscillator, no oscillation

  CASE 2: Δ = 0   repeated root r = -b/2a
  y = (C₁ + C₂x)e^(rx)
  Physics: critically damped — fastest return to equilibrium without oscillation

  CASE 3: Δ < 0   complex roots r = α ± iβ
  y = e^(αx)(C₁cos βx + C₂sin βx)
  Physics: underdamped — oscillation with exponential decay

  ┌──────────────────────────────────────────────────────────────┐
  │ PHYSICAL EXAMPLE: RLC circuit / mass-spring-dashpot         │
  │ mẍ + bẋ + kx = 0                                           │
  │ ω₀ = √(k/m) = natural frequency                            │
  │ γ  = b/2m   = damping rate                                 │
  │ r  = -γ ± √(γ² - ω₀²)                                     │
  │                                                             │
  │ Underdamped (γ < ω₀):  x(t) = Ae^(-γt)cos(ωt + φ)        │
  │ where ω = √(ω₀² - γ²)  (damped frequency < natural freq)  │
  │ Q factor = ω₀/2γ  (quality factor — cycles before decay)   │
  └──────────────────────────────────────────────────────────────┘
```

### 2.2 Method of Undetermined Coefficients

```
  For ay'' + by' + cy = f(x) where f(x) is "nice":

  GUESS TABLE:
  ┌──────────────────────────────────────────────────────────────┐
  │  f(x)                  │  Guess for yₚ                      │
  ├──────────────────────────────────────────────────────────────┤
  │  polynomial degree n   │  Aₙxⁿ + ... + A₁x + A₀           │
  │  e^(ax)               │  Ae^(ax)                            │
  │  sin(bx) or cos(bx)   │  A sin(bx) + B cos(bx)             │
  │  e^(ax)sin(bx)        │  e^(ax)(A sin bx + B cos bx)        │
  │  xⁿe^(ax)             │  (Aₙxⁿ + ...)e^(ax)               │
  └──────────────────────────────────────────────────────────────┘

  MODIFICATION RULE: if yₚ guess solves homogeneous equation,
  multiply by x (or x² if double root).

  PHYSICAL MEANING: Resonance!
  mẍ + kx = F₀cos(ω₀t)   (forcing at natural frequency)
  Guess A cos(ω₀t) fails → modification → yₚ = At sin(ω₀t)
  Amplitude grows linearly with t → unbounded growth = RESONANCE
  (Tacoma Narrows Bridge, 1940)
```

### 2.3 Variation of Parameters

```
  For any ay'' + by' + cy = f(x), given two homogeneous solutions y₁, y₂:

  yₚ = -y₁ ∫(y₂f/W) dx + y₂ ∫(y₁f/W) dx

  Wronskian: W = y₁y₂' - y₁'y₂   (≠ 0 if y₁, y₂ linearly independent)

  More general than undetermined coefficients — works for any f(x).
  Computationally messier but universally applicable.
```

---

## 3. Systems of ODEs

### 3.1 Matrix Form

```
  System: dx/dt = Ax  (x ∈ ℝⁿ, A constant matrix)

  Solution: x(t) = e^(At) x(0)

  MATRIX EXPONENTIAL:
  e^(At) = I + At + (At)²/2! + (At)³/3! + ...

  If A = PDP⁻¹ (diagonalizable):
  e^(At) = Pe^(Dt)P⁻¹ = P·diag(e^(λ₁t),...,e^(λₙt))·P⁻¹

  GENERAL SOLUTION:
  x(t) = Σᵢ cᵢ e^(λᵢt) vᵢ   (linear combination of modes)

  Each mode: e^(λᵢt) vᵢ
  ├── λᵢ real negative: exponential decay
  ├── λᵢ real positive: exponential growth
  ├── λᵢ = α ± iβ: oscillation × exp(αt)
  └── λᵢ = 0: constant (neutral stability)
```

### 3.2 Phase Plane Analysis

For 2D systems ẋ = f(x,y), ẏ = g(x,y):

```
  EQUILIBRIUM POINTS: f(x*,y*) = 0 and g(x*,y*) = 0
  Linearize near (x*, y*): let A = Jacobian [∂f/∂x ∂f/∂y; ∂g/∂x ∂g/∂y] at (x*,y*)
  Local behavior determined by eigenvalues of A:

  ┌─────────────────────────────────────────────────────────────────┐
  │  Eigenvalues of A        │  Type of equilibrium                │
  ├─────────────────────────────────────────────────────────────────┤
  │  λ₁ < λ₂ < 0            │  Stable node (overdamped)           │
  │  0 < λ₁ < λ₂            │  Unstable node                      │
  │  λ₁ < 0 < λ₂            │  Saddle point (unstable)            │
  │  α ± iβ, α < 0          │  Stable spiral (underdamped)        │
  │  α ± iβ, α > 0          │  Unstable spiral                    │
  │  ± iβ (α = 0)           │  Center (nonlinear: need 2nd order) │
  └─────────────────────────────────────────────────────────────────┘

  EXAMPLES:
  Predator-prey (Lotka-Volterra): periodic orbits around center
  Pendulum:  stable center at (0,0), saddle at (π,0)
  Van der Pol: limit cycle (nonlinear oscillator)
```

### 3.3 Stability — Lyapunov

```
  An equilibrium x* is:
  STABLE: trajectories starting near x* stay near x*
  ASYMPTOTICALLY STABLE: trajectories starting near x* → x* as t → ∞
  UNSTABLE: trajectories leave neighborhood

  For linear systems: asymptotically stable ↔ all eigenvalues have Re(λ) < 0

  LYAPUNOV FUNCTION V(x): like an energy function
  If V(x) > 0 for x ≠ x* and dV/dt < 0 along trajectories → asymptotically stable
  (No need to solve the DE; just find a suitable V)

  CONNECTION TO PHYSICS:
  Physical energy E is usually a Lyapunov function (E decreasing = stability)
  If friction > 0: dE/dt < 0 → equilibrium is asymptotically stable
```

---

## 4. Partial Differential Equations

### 4.1 The Three Canonical Types

```
  ┌────────────────────────────────────────────────────────────────────┐
  │  ELLIPTIC: ∇²u = f                                                │
  │  Laplace equation: ∇²u = 0                                        │
  │  Poisson equation: ∇²u = f                                        │
  │  Steady-state: no time dependence                                  │
  │  Boundary value problem: specify u on all boundaries              │
  │  Physics: electrostatics, gravitational potential, steady heat    │
  ├────────────────────────────────────────────────────────────────────┤
  │  PARABOLIC: ∂u/∂t = α∇²u                                         │
  │  Heat equation / diffusion equation                                │
  │  Initial value problem: specify u at t=0                          │
  │  Solution smooths out: initial sharp features diffuse away        │
  │  Physics: heat conduction, diffusion, Schrödinger (with i!)       │
  ├────────────────────────────────────────────────────────────────────┤
  │  HYPERBOLIC: ∂²u/∂t² = c²∇²u                                     │
  │  Wave equation                                                     │
  │  Initial value problem: specify u AND ∂u/∂t at t=0               │
  │  Finite propagation speed c: wavefronts, characteristics          │
  │  Physics: EM waves, acoustic waves, gravitational waves           │
  └────────────────────────────────────────────────────────────────────┘

  Mnemonic:
  Elliptic  = Equilibrium  (no time)
  Parabolic = Parachute    (smooths/damps)
  Hyperbolic = Holler      (waves propagate)
```

### 4.2 Separation of Variables

```
  TECHNIQUE: assume u(x,t) = X(x)T(t), substitute, separate by variable.

  HEAT EQUATION on [0,L] with u(0,t) = u(L,t) = 0:
  ∂u/∂t = α ∂²u/∂x²

  Assume u = X(x)T(t):
  X(x)T'(t) = α X''(x)T(t)
  T'/αT = X''/X = -λ    (both sides = constant, say -λ)

  X equation: X'' + λX = 0,  X(0) = X(L) = 0
  Solutions: Xₙ(x) = sin(nπx/L),  λₙ = (nπ/L)²   (eigenvalue problem!)

  T equation: T' = -αλₙT
  Solutions: Tₙ(t) = e^(-αλₙt) = e^(-α(nπ/L)²t)

  GENERAL SOLUTION (superposition — valid by linearity):
  u(x,t) = Σ bₙ sin(nπx/L) e^(-α(nπ/L)²t)
             n=1

  INITIAL CONDITION u(x,0) = f(x):
  f(x) = Σ bₙ sin(nπx/L)   ← Fourier sine series
  bₙ = (2/L) ∫₀ᴸ f(x)sin(nπx/L) dx
```

### 4.3 Wave Equation — D'Alembert Solution

```
  1D WAVE EQUATION: ∂²u/∂t² = c²∂²u/∂x²

  D'ALEMBERT'S SOLUTION:
  u(x,t) = f(x - ct) + g(x + ct)

  Any solution is a superposition of a rightward and leftward traveling wave.
  f and g determined by initial conditions u(x,0) and ∂u/∂t(x,0).

  Physical interpretation:
  ├── f(x-ct): shape f, moving right at speed c
  └── g(x+ct): shape g, moving left at speed c

  STANDING WAVES (wave equation on [0,L], fixed ends):
  uₙ(x,t) = sin(nπx/L)(Aₙcos(ωₙt) + Bₙsin(ωₙt))
  ωₙ = nπc/L  (normal mode frequencies)
  Superposition → full solution (Fourier series in space)
```

### 4.4 Laplace Equation — Steady State

```
  ∇²u = 0   (u_xx + u_yy = 0 in 2D)

  KEY PROPERTY: solutions are HARMONIC — they satisfy the mean value property
  u(x₀, y₀) = (1/2π) ∫₀²π u(x₀+r cosθ, y₀+r sinθ) dθ
  (value at center = average over any surrounding circle)

  CONSEQUENCE: No interior maxima or minima (maximum principle)
  Extreme values of u occur on the boundary.
  Physics: electric potential has no local extrema in free space (Earnshaw!)

  SEPARATION IN CARTESIAN:
  u(x,y) = (A cosh(kx) + B sinh(kx))(C cos(ky) + D sin(ky))
  or       (Ae^(kx) + Be^(-kx))(C cos(ky) + D sin(ky))

  SEPARATION IN POLAR:
  u(r,θ) = Σ (Aₙrⁿ + Bₙr^(-n))(Cₙcos(nθ) + Dₙsin(nθ))
```

---

## 5. Fourier Series Solutions — The Full Picture

```
  WHY FOURIER SERIES WORK FOR PDEs:

  1. The eigenfunctions of d²/dx² on [0,L] with Dirichlet BCs are sin(nπx/L).
     These form a COMPLETE ORTHONORMAL BASIS for L²([0,L]).

  2. Any f ∈ L²([0,L]) = Σ bₙ sin(nπx/L)  (Fourier sine series)
     Any g ∈ L²([0,L]) = a₀/2 + Σ(aₙcos + bₙsin)  (full Fourier series)

  3. Linear PDE with these boundary conditions → each Fourier mode evolves
     independently (decoupled ODEs in time for each mode's coefficient).

  FOURIER COEFFICIENTS:
  Full series on [-L, L]:
  aₙ = (1/L) ∫₋ₗᴸ f(x) cos(nπx/L) dx
  bₙ = (1/L) ∫₋ₗᴸ f(x) sin(nπx/L) dx

  Parseval's theorem: Σ(aₙ² + bₙ²) = (1/L)∫|f|²dx
  (energy in frequency domain = energy in space domain)

  GIBBS PHENOMENON:
  Near a jump discontinuity, Fourier partial sums overshoot by ~9%.
  The overshoot doesn't disappear as N → ∞ — it narrows but stays 9%.
  This is why sharp edges in signals (digital audio, images) cause ringing.
```

---

## 6. Green's Functions

The complete solution engine for linear PDEs:

```
  IDEA: For Lu = f (L = linear differential operator):
  Find G(x, x') such that LG(x, x') = δ(x - x')
  Then: u(x) = ∫ G(x, x') f(x') dx'

  G is the RESPONSE to a point source (delta function input).
  Knowing G → can solve for any source f by superposition.

  EXAMPLES:
  ┌────────────────────────────────────────────────────────────────────┐
  │  Operator L        │  Green's function G(r, r')                  │
  ├────────────────────────────────────────────────────────────────────┤
  │  -d²/dx² on ℝ     │  |x-x'|/2                                   │
  │  -∇² on ℝ³        │  1/(4π|r-r'|)  ← Coulomb's law potential!  │
  │  -∇² on ℝ²        │  -(1/2π)ln|r-r'|                            │
  │  ∂/∂t - α∂²/∂x²  │  (1/√(4παt))e^(-(x-x')²/4αt) ← Gaussian!  │
  └────────────────────────────────────────────────────────────────────┘

  Coulomb's law IS the Green's function for Poisson's equation.
  The Gaussian diffusion kernel IS the Green's function for the heat equation.
```

---

## 7. The Physics DE Bestiary

Every major equation from your physics modules decoded:

```
  EQUATION                    FORM              TYPE        PHYSICS
  ──────────────────────────────────────────────────────────────────────
  Newton                      mẍ = F(x,ẋ,t)    2nd ODE     mechanics
  Harmonic oscillator         ẍ + ω₀²x = 0     2nd ODE     circuits, QM
  Damped oscillator           ẍ + 2γẋ + ω₀²x=0 2nd ODE     RLC, mech
  Forced oscillator           ẍ+2γẋ+ω₀²x=F/m  2nd ODE     resonance
  Radioactive decay           ṅ = -λn           1st ODE     decay
  RC circuit                  V̇ + V/RC = V₀/RC  1st ODE     electronics
  Heat equation               ∂T/∂t = κ∇²T     Parabolic   heat
  Wave equation               ∂²u/∂t² = c²∇²u  Hyperbolic  waves, EM
  Maxwell (wave form)         □²E = 0           Hyperbolic  light
  Schrödinger (time dep.)     iℏ∂ψ/∂t = Hψ     Parabolic   QM (with i!)
  Schrödinger (time ind.)     Hψ = Eψ           Eigenvalue  energy levels
  Laplace / Poisson           ∇²V = 0 / -ρ/ε₀  Elliptic    electrostatics
  Diffusion (MHD)             ∂B/∂t=η∇²B+∇×(v×B) Parabolic+  MHD induction
  Navier-Stokes               ρ(∂v/∂t+v·∇v)=.. Nonlinear   fluid mechanics
  ──────────────────────────────────────────────────────────────────────
  Schrödinger is parabolic but with imaginary diffusion coefficient iℏ
  → waves don't damp, they oscillate (probability is conserved)
```

---

## 8. Boundary vs Initial Value Problems

```
  INITIAL VALUE PROBLEM (IVP):
  ├── ODE or time-dependent PDE
  ├── Data specified at one time t=0: u(x,0) = f(x)
  ├── Solution marches forward in time
  └── Unique solution (Picard) given smoothness

  BOUNDARY VALUE PROBLEM (BVP):
  ├── ODE or elliptic PDE
  ├── Data specified on boundary of spatial domain
  ├── May have: unique solution, no solution, or infinitely many
  └── Eigenvalue problems are BVPs: Ly = λy, y(0)=y(L)=0

  TYPES OF BOUNDARY CONDITIONS:
  Dirichlet:  u = g on boundary          (fixed value)
  Neumann:    ∂u/∂n = g on boundary      (fixed flux/gradient)
  Robin:      αu + β∂u/∂n = g           (mixed — convection BCs)
  Periodic:   u(0) = u(L), u'(0) = u'(L)

  PHYSICS EXAMPLES:
  Dirichlet: fixed voltage, fixed temperature
  Neumann:   insulated wall (∂T/∂n=0), conductor (∂V/∂n ∝ surface charge)
  Robin:     convective heat transfer to ambient (Newton's law of cooling)
```

---

## Decision Cheat Sheet

| Equation form | Method |
|--------------|--------|
| y' = f(x)g(y) | Separate variables |
| y' + P(x)y = Q(x) | Integrating factor μ = e^(∫P dx) |
| M dx + N dy = 0, ∂M/∂y = ∂N/∂x | Exact equation — find potential F |
| ay'' + by' + cy = 0 | Characteristic equation ar²+br+c=0 |
| ay'' + by' + cy = f(x), f nice | Undetermined coefficients |
| ay'' + by' + cy = f(x), f arbitrary | Variation of parameters |
| System ẋ = Ax | Matrix exponential, eigendecomposition |
| PDE on finite domain, linear BCs | Separation of variables + Fourier |
| PDE on infinite domain | Fourier/Laplace transform |
| Any linear DE with point source | Green's function |
| Nonlinear ODE near equilibrium | Linearize, classify eigenvalues |

---

## Common Confusion Points

**"How is Schrödinger's equation parabolic (heat-like) but solutions don't decay?"**
The heat equation ∂u/∂t = α∇²u has α > 0 (real), causing exponential decay e^(-αk²t) for each Fourier mode. Schrödinger has iℏ∂ψ/∂t = -ℏ²/2m ∇²ψ, so effectively α = iℏ/2m (imaginary). Fourier modes go as e^(-ik²ℏt/2m) — complex exponentials, not decaying. Norm is preserved: |e^(iθ)| = 1. The "i" converts diffusion into wave propagation.

**"When does separation of variables fail?"**
When the domain is not rectangular/cylindrical/spherical, when the boundary conditions mix variables, or when the PDE has non-constant coefficients that can't be separated. Also fails for nonlinear PDEs. It's a special technique that works beautifully for the standard physics PDEs and their natural geometries.

**"What's the difference between a particular solution and the general solution?"**
For Lu = f: yₚ (particular) is any one solution. The homogeneous equation Lu = 0 has a solution space of dimension n (for nth order). General solution = yₚ + (any homogeneous solution). The n free constants are fixed by n initial or boundary conditions.

**"Why do eigenvalue problems appear in PDEs?"**
Separation of variables always produces an ODE eigenvalue problem in the spatial variable: X'' = -λX with boundary conditions. The boundary conditions select the allowed λ values (discrete spectrum) and their eigenfunctions. This is why quantum mechanics — which is Schrödinger's PDE — has discrete energy levels: they're the eigenvalues of the Hamiltonian with appropriate boundary conditions.

**"What's a Green's function intuitively?"**
It's the impulse response of a differential operator — identical to the impulse response H(t) of a linear system in 6.003. If you know how the system responds to a unit impulse at every point, you know the response to any source by superposition. The Coulomb potential 1/r is the "impulse response" to a point charge; convolve with any charge distribution to get the potential.

---

*Next: `mathematics/08-TOPOLOGY.md` — open sets, continuity, homotopy, and the topological invariants that show up in condensed matter physics.*
