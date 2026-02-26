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

## 9. Numerical ODE Methods

```
  DISCRETIZE: replace y' = f(x,y) with a recurrence from step xₙ to xₙ₊h.

  EULER'S METHOD (first-order, for intuition only):
  yₙ₊₁ = yₙ + h·f(xₙ, yₙ)
  Global error O(h) — too large for practical use.

  RUNGE-KUTTA 4 (RK4) — the classical workhorse:
  k₁ = f(xₙ,        yₙ)
  k₂ = f(xₙ + h/2,  yₙ + h/2·k₁)
  k₃ = f(xₙ + h/2,  yₙ + h/2·k₂)
  k₄ = f(xₙ + h,    yₙ + h·k₃)
  yₙ₊₁ = yₙ + h/6·(k₁ + 2k₂ + 2k₃ + k₄)

  Global error O(h⁴). Four function evaluations per step.
  The "4" is both order and number of stages — coincidence that won't last.

  BUTCHER TABLEAU (general explicit Runge-Kutta framework):
  c │ A        kᵢ = f(xₙ + cᵢh, yₙ + h Σⱼ aᵢⱼkⱼ)
  ──┼────     yₙ₊₁ = yₙ + h Σᵢ bᵢkᵢ
    │ bᵀ

  RK4 tableau:  c=(0, ½, ½, 1),  b=(⅙, ⅓, ⅓, ⅙), A lower triangular.

  STIFFNESS — why explicit methods fail:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Stiff system: solution has components with vastly different         │
  │  timescales. Example: y' = -1000y + sin(t)  (fast decay, slow force)│
  │                                                                      │
  │  STABILITY REGION of a method: the set of h·λ ∈ ℂ where            │
  │  applied to y' = λy, the method gives bounded solutions.            │
  │                                                                      │
  │  RK4 stability region: roughly |hλ| < 2.8 (along negative real axis)│
  │  For λ = -1000: need h < 0.0028 — tiny steps for accurate solution  │
  │  even though the interesting dynamics happen at timescale O(1)!      │
  │                                                                      │
  │  Jacobian eigenvalues of stiff systems lie far in the left half-plane│
  │  → stability forces h << 1, but accuracy only needs h ~ O(1)       │
  └──────────────────────────────────────────────────────────────────────┘

  IMPLICIT METHODS — for stiff systems:
  Backward Euler:    yₙ₊₁ = yₙ + h·f(xₙ₊₁, yₙ₊₁)  (solve for yₙ₊₁)
  Stability region extends to entire left half-plane → A-stable.
  No step-size restriction from fast components.
  Cost: solve a nonlinear equation each step (Newton iterations).

  TRAPEZOIDAL RULE (Crank-Nicolson):
  yₙ₊₁ = yₙ + h/2·(f(xₙ,yₙ) + f(xₙ₊₁,yₙ₊₁))
  Second-order, A-stable. Used heavily for parabolic PDEs (heat equation).

  BDF (Backward Differentiation Formulas):
  Use several past values; BDF2 through BDF6 balance stability and accuracy.
  The solvers VODE/LSODE use BDF for stiff systems.

  DORMAND-PRINCE (RK45) — adaptive step size:
  Uses two embedded RK methods (order 4 and 5) to estimate local error.
  If error > tolerance: reject step, halve h.
  If error << tolerance: accept step, increase h.
  scipy.integrate.solve_ivp default method = 'RK45' (Dormand-Prince).

  PRACTICAL ENTRY POINT:
  from scipy.integrate import solve_ivp

  # Adaptive RK45 (non-stiff problems)
  sol = solve_ivp(f, [t0, tf], y0, method='RK45', rtol=1e-6, atol=1e-9)

  # BDF (stiff problems — chemical kinetics, neural ODEs, etc.)
  sol = solve_ivp(f, [t0, tf], y0, method='BDF', jac=jacobian_f)

  # LSODA (auto-switches between non-stiff Adams and stiff BDF)
  sol = solve_ivp(f, [t0, tf], y0, method='LSODA')

  WHEN TO USE WHAT:
  ┌───────────────────────────────────────────────────────────────────┐
  │  Non-stiff, smooth:     RK45 (Dormand-Prince) — default          │
  │  Non-stiff, high acc:   DOP853 (8th order Dormand-Prince)        │
  │  Stiff:                 BDF or Radau (scipy) — implicit          │
  │  Unknown:               LSODA — auto-detects                    │
  │  Structure-preserving:  Leapfrog/Verlet (see §10 Hamiltonian)    │
  └───────────────────────────────────────────────────────────────────┘
```

## 10. Hamiltonian Mechanics

```
  LAGRANGIAN MECHANICS (variational formulation):
  L(q, q̇, t) = T - V   (kinetic − potential energy)
  Action: S = ∫ L dt
  Euler-Lagrange equations: d/dt(∂L/∂q̇ᵢ) - ∂L/∂qᵢ = 0
  These are 2nd-order ODEs for the configuration q(t).

  LEGENDRE TRANSFORM → HAMILTONIAN:
  Conjugate momentum:  pᵢ = ∂L/∂q̇ᵢ
  Hamiltonian: H(q, p, t) = Σᵢ pᵢq̇ᵢ - L(q, q̇, t)
  (pᵢq̇ᵢ - L: replace q̇ by p using the momentum definition)

  HAMILTON'S EQUATIONS (canonical form):
  ┌───────────────────────────────────────────────────────┐
  │   q̇ᵢ = +∂H/∂pᵢ                                      │
  │   ṗᵢ = -∂H/∂qᵢ                                      │
  └───────────────────────────────────────────────────────┘
  These are 2n FIRST-ORDER ODEs for (q,p) ∈ phase space ℝ²ⁿ.
  (vs. n second-order Euler-Lagrange equations — same content, different form)

  H is conserved when ∂H/∂t = 0:
  dH/dt = Σᵢ(∂H/∂qᵢ q̇ᵢ + ∂H/∂pᵢ ṗᵢ) = Σᵢ(∂H/∂qᵢ ∂H/∂pᵢ - ∂H/∂pᵢ ∂H/∂qᵢ) = 0 ✓

  POISSON BRACKET:
  {f, g} = Σᵢ (∂f/∂qᵢ ∂g/∂pᵢ - ∂f/∂pᵢ ∂g/∂qᵢ)
  Hamilton's equations: q̇ = {q, H},  ṗ = {p, H}
  Conservation law: {A, H} = 0 ↔ A is conserved
  In QM: Poisson bracket → commutator: {·,·} → (1/iℏ)[·,·]

  SYMPLECTIC STRUCTURE:
  Phase space ℝ²ⁿ with coordinates (q₁,...,qₙ,p₁,...,pₙ) carries a
  canonical 2-form:  ω = Σᵢ dqᵢ ∧ dpᵢ
  ω is closed (dω=0) and non-degenerate → symplectic manifold.
  Hamilton's flow preserves ω (Liouville's theorem):
  LIOUVILLE'S THEOREM: phase space volume is preserved under Hamiltonian flow.
  Φₜ*ω = ω  →  det(dΦₜ/d(q,p)) = 1  (Jacobian = 1)
  Physics: phase space density of an ensemble of systems is incompressible.
  Statistics/information theory: Hamiltonian systems preserve entropy.

  CANONICAL TRANSFORMATIONS (q,p) → (Q,P) that preserve ω = Σ dQᵢ∧dPᵢ.
  New coordinates are equally valid for Hamilton's equations with same H (in new coords).
  Generator functions F(q,Q) or F(q,P) specify the transformation.
  Action-angle variables: for integrable systems, canonical transform puts
  dynamics in simple form: Q̇ᵢ = νᵢ (constant frequencies), Ṗᵢ = 0.

  SYMPLECTIC INTEGRATORS (structure-preserving numerics):
  Standard RK4 does NOT preserve the symplectic form → energy drifts over long times.
  Symplectic methods exactly preserve a modified Hamiltonian → no energy drift.

  LEAPFROG / STÖRMER-VERLET (2nd order):
  p_{n+½} = pₙ - (h/2) ∂V/∂q(qₙ)
  q_{n+1} = qₙ + h · p_{n+½}/m
  p_{n+1} = p_{n+½} - (h/2) ∂V/∂q(q_{n+1})

  ├── Symplectic (preserves phase space volume exactly)
  ├── Time-reversible: reverse momentum → time runs backward
  ├── Energy oscillates but does NOT drift even for long integrations
  └── Used in: molecular dynamics (LAMMPS, GROMACS), N-body simulations,
      HMC (Hamiltonian Monte Carlo) for Bayesian inference

  WHY HMC IS RELEVANT TO ML:
  Hamiltonian Monte Carlo uses leapfrog to propose MCMC steps.
  The Hamiltonian H(q,p) = -log π(q) + ‖p‖²/2 (negative log-posterior + kinetic).
  Leapfrog trajectories propose distant samples; Metropolis accepts/rejects.
  Result: far lower autocorrelation than random-walk Metropolis.
  Stan (Bayesian inference) uses NUTS (No U-Turn Sampler) = adaptive HMC.
```

## 11. Chaos and Nonlinear Dynamics

```
  CHAOS: deterministic system with sensitive dependence on initial conditions.
  Long-term prediction impossible even with perfect knowledge of equations.

  LYAPUNOV EXPONENTS — quantifying sensitive dependence:
  Two nearby trajectories x(t) and x(t) + δ(0) diverge as:
  ‖δ(t)‖ ≈ ‖δ(0)‖ e^(λt)

  λ = lim_{t→∞} (1/t) log(‖δ(t)‖/‖δ(0)‖) = maximal Lyapunov exponent

  λ > 0: CHAOS — nearby trajectories diverge exponentially
  λ < 0: stable fixed point or limit cycle
  λ = 0: on a periodic orbit or at a bifurcation

  Doubling time = log(2)/λ. For λ=1 and 1% initial error: 100× magnification
  takes log(100)/1 ≈ 4.6 time units. This is the prediction horizon.

  LORENZ SYSTEM — the canonical strange attractor:
  ẋ = σ(y - x)
  ẏ = x(ρ - z) - y       σ=10, ρ=28, β=8/3 (Lorenz's atmospheric values)
  ż = xy - βz

  ┌──────────────────────────────────────────────────────────────────────┐
  │  Three coupled nonlinear ODEs. Deterministic. Dissipative (volume   │
  │  contracts at rate -(σ+1+β)). Trajectories confined to a bounded   │
  │  region. But within that region: CHAOS.                             │
  │                                                                     │
  │  STRANGE ATTRACTOR: bounded invariant set with fractal structure.   │
  │  Trajectories on it diverge (λ > 0) yet stay on the attractor.     │
  │  Fractal dimension ≈ 2.06 (slightly more than a 2D surface).       │
  │                                                                     │
  │  "Butterfly effect" (Lorenz 1963): sensitivity to initial           │
  │  conditions makes deterministic weather prediction impossible        │
  │  beyond ~2 weeks.                                                   │
  └──────────────────────────────────────────────────────────────────────┘

  LOGISTIC MAP — discrete analog (period-doubling route to chaos):
  xₙ₊₁ = r·xₙ(1 - xₙ)   xₙ ∈ [0,1], r ∈ [0,4]

  r < 1:     xₙ → 0   (extinction)
  1 < r < 3: xₙ → fixed point x* = 1 - 1/r
  r ≈ 3.45:  period-2 orbit (FIRST BIFURCATION)
  r ≈ 3.54:  period-4 orbit
  r ≈ 3.56:  period-8 ...
  r ≈ 3.57:  chaos onset (Feigenbaum point)
  r = 4:     full chaos (ergodic on [0,1])

  FEIGENBAUM CONSTANT δ = 4.669...:
  Ratio of successive bifurcation intervals converges to δ universally
  (for any map with a quadratic maximum). Appears in physical experiments.

  BIFURCATIONS — qualitative changes in phase portrait as parameter varies:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Saddle-node:     two equilibria merge and annihilate               │
  │  Transcritical:   two equilibria swap stability                     │
  │  Pitchfork:       one equilibrium splits into three (symmetry-break)│
  │  Hopf:            stable equilibrium becomes unstable + limit cycle │
  │    Subcritical Hopf: discontinuous jump to large amplitude          │
  │    Supercritical Hopf: smooth growth of oscillation amplitude       │
  └──────────────────────────────────────────────────────────────────────┘

  POINCARÉ-BENDIXSON THEOREM (2D only):
  Bounded trajectory in ℝ² with no equilibria → must approach a limit cycle.
  Chaos is impossible in 2D autonomous ODEs — need ≥ 3 dimensions.
  (Lorenz is 3D; the logistic map is 1D but discrete.)

  CONNECTION TO ML:
  Loss landscape dynamics in deep learning have been analyzed through the
  lens of dynamical systems: gradient flow dx/dt = -∇L(x) (gradient flow ODE).
  Flat minima, saddle points, and basin geometry correspond directly to
  dynamical systems concepts. Batch noise introduces stochastic perturbations —
  the noisy gradient flow ẋ = -∇L + η(t) is a Langevin equation (see §10).
```

### 4.5 PDEs on Manifolds — Bridge to 09-MANIFOLDS

```
  The PDEs above are formulated on flat ℝⁿ. Curved spaces require the
  Laplace-Beltrami operator ∆_M, which generalizes ∇² to manifolds.

  LAPLACE-BELTRAMI OPERATOR on a Riemannian manifold (M, g):
  ∆_M f = (1/√|g|) ∂ᵢ(√|g| gⁱʲ ∂ⱼf)

  On ℝⁿ with Euclidean metric: gⁱʲ = δⁱʲ → ∆_M = ∂₁²+...+∂ₙ² = ∇². ✓
  On the 2-sphere S² (θ,φ): ∆_{S²} = (1/sinθ)∂_θ(sinθ ∂_θ) + (1/sin²θ)∂_φ²
  Eigenfunctions: spherical harmonics Yₗᵐ(θ,φ), eigenvalues -l(l+1).

  THE DIFFERENTIAL EQUATIONS ON MANIFOLDS:
  Heat equation:       ∂u/∂t = α∆_M u
  Wave equation:       ∂²u/∂t² = c²∆_M u
  Schrödinger:         iℏ∂ψ/∂t = (-ℏ²/2m ∆_M + V)ψ
  Eigenvalue problem:  ∆_M φ = -λφ  (Laplace-Beltrami spectrum)

  CAN YOU HEAR THE SHAPE OF A DRUM? (Kac 1966):
  The spectrum {λ₁, λ₂, ...} of ∆_M on a compact manifold M encodes
  geometric information: dimension, volume, total scalar curvature (via
  the heat kernel expansion). Non-isometric manifolds can have identical
  spectra (Milnor 1964 counterexample in 16D; Gordon-Webb-Wolpert 1992 in 2D).
  But the spectrum determines "most" of the geometry.

  DIFFUSION MAPS IN ML (Coifman-Lafon 2006):
  Given high-dimensional data X = {x₁,...,xₙ} ⊂ ℝᵈ lying near a manifold:
  1. Build kernel matrix K_{ij} = exp(-‖xᵢ-xⱼ‖²/ε)  (Gaussian kernel)
  2. Normalize to get row-stochastic matrix M (Markov chain on data)
  3. Eigenvectors of M ↔ eigenfunctions of ∆_M on the underlying manifold
  4. Embed data in eigenvector coordinates → nonlinear dimensionality reduction

  ├── Euclidean distance in the embedding = diffusion distance on manifold
  │   (accounts for intrinsic geometry, not ambient Euclidean distance)
  ├── Robust to noise: diffusion averages over many paths
  └── t-SNE and UMAP are related but use different kernels and objectives

  SPECTRAL GEOMETRY AND GRAPH LAPLACIANS:
  Replace continuous manifold with a graph G = (V, E, w):
  Graph Laplacian: L = D - A  (D = degree matrix, A = adjacency matrix)
  Normalized Laplacian: L_sym = D^(-1/2) L D^(-1/2)
  This is the discrete Laplace-Beltrami operator on the graph.
  Spectral clustering: eigenvectors of L capture cluster structure.
  Graph neural networks: convolution = polynomial of L (spectral filtering).

  → See 09-MANIFOLDS.md §2 for the full tangent space / Riemannian machinery.
  → The Laplace-Beltrami eigenfunctions form the natural basis for PDEs on
    any compact Riemannian manifold: separation of variables = eigenfunction expansion.
```

## 12. Neural ODEs

```
  RESNET VIEWED AS AN ODE:
  A ResNet block: h_{l+1} = h_l + f(h_l, θ_l)
  As depth → ∞ with step size h → 0:
  dh/dt = f(h(t), t, θ)
  h(0) = input,  h(1) = output

  A NEURAL ODE (Chen et al. 2018) defines its hidden state as the solution
  of an ODE parameterized by a neural network f.

  FORWARD PASS: solve the IVP numerically (e.g., Dormand-Prince RK45).
  BACKWARD PASS (gradient computation): needs d(loss)/dθ.
  Naive approach: backprop through every ODE solver step → O(memory).

  ADJOINT SENSITIVITY METHOD:
  Define adjoint state a(t) = d(loss)/dh(t)   (gradient with respect to state)
  The adjoint satisfies its own ODE, run BACKWARDS:
  da/dt = -a(t)ᵀ · ∂f/∂h(h(t), t, θ)

  Then:  d(loss)/dθ = -∫₁⁰ a(t)ᵀ · ∂f/∂θ dt

  This is EXACTLY variation of parameters (§2.3) for the adjoint equation.
  The adjoint ODE and the parameter gradient integral are solved simultaneously
  by running one backward ODE solve — O(1) memory regardless of integration steps.

  ┌──────────────────────────────────────────────────────────────────────┐
  │  BENEFITS:                                                           │
  │  ├── Adaptive depth: ODE solver uses as many steps as accuracy needs│
  │  ├── Constant memory: adjoint method avoids storing all activations │
  │  ├── Continuous-time models: natural for irregularly sampled data   │
  │  └── Latent ODE: encode time series → initial condition → decode    │
  │                                                                      │
  │  DISADVANTAGES:                                                      │
  │  ├── Training is slower (ODE solves are expensive at high accuracy) │
  │  ├── Stiff dynamics → stiff ODE solver required (implicit methods)  │
  │  └── Hard to train deep: adjoint sensitivity can become unstable    │
  └──────────────────────────────────────────────────────────────────────┘

  RELATED: DIFFUSION MODELS AS SDEs
  Denoising diffusion probabilistic models (DDPMs) are continuous-time:

  FORWARD (noising) SDE:  dx = f(x,t)dt + g(t)dW   (Langevin-type)
  Gradually adds Gaussian noise to destroy data distribution.

  REVERSE (denoising) SDE (Anderson 1982):
  dx = [f(x,t) - g(t)² ∇_x log p_t(x)] dt + g(t)dW̄
  The score function ∇_x log p_t(x) is learned by the neural network.

  DDIM (Song et al.) uses the probability flow ODE (deterministic version):
  dx/dt = f(x,t) - ½ g(t)² ∇_x log p_t(x)
  Faster sampling: 50 steps instead of 1000 because no stochastic noise.

  This is a direct application of §3 (systems of ODEs) and §1.1 (separable
  equations via the heat equation connection) to modern generative ML.

  CONTINUOUS NORMALIZING FLOWS (CNFs):
  Learn a diffeomorphism z₁ = T(z₀) by integrating dz/dt = f(z,t,θ).
  Change of variables: log p(z₁) = log p(z₀) - ∫₀¹ tr(∂f/∂z) dt
  (trace of Jacobian — the continuous version of the log-determinant Jacobian)
  FreeForm Jacobian of Arbitrary Couplings (FFJORD) makes this tractable
  via Hutchinson's trace estimator (randomized O(d) instead of O(d²)).
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
