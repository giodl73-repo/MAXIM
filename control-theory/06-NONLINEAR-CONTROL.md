# Nonlinear Control

## Big Picture: Why Linearization Isn't Enough

```
┌─────────────────────────────────────────────────────────────────────┐
│                NONLINEAR PHENOMENA — A TAXONOMY                     │
│                                                                     │
│  LINEAR WORLD          vs.      NONLINEAR WORLD                    │
│  ──────────────────────         ───────────────────────────         │
│  Single equilibrium             Multiple equilibria                 │
│  Stability = global             Stability = local (Lyapunov)        │
│  No limit cycles                Limit cycles (self-sustained osc.)  │
│  Superposition holds            No superposition                    │
│  Freq. response meaningful      Harmonics generated                 │
│  Phase portrait: rays/spirals   Rich phase portrait geometry        │
│                                                                     │
│  TOOLS:                                                             │
│  Phase plane ──► Lyapunov ──► Feedback lin ──► Sliding mode        │
│  (2D analysis)  (stability)   (exact cancel) (robustness)          │
│                                                                     │
│  REALITY CHECK: Most engineered systems are nonlinear.             │
│  Linear control works when: operating near equilibrium, small       │
│  disturbances, adequate gain/phase margins for the linearization.   │
│  Nonlinear control needed when: large excursions, saturation,       │
│  time-varying operating point, need for global guarantees.          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Phase Plane Analysis (2D Systems)

### Equilibria and Their Classification

```
SYSTEM: ẋ₁ = f₁(x₁, x₂),  ẋ₂ = f₂(x₁, x₂)
EQUILIBRIUM: f₁(x*) = 0, f₂(x*) = 0

LINEARIZATION at x*:
  A = Jacobian[f](x*) = [∂f₁/∂x₁  ∂f₁/∂x₂]
                         [∂f₂/∂x₁  ∂f₂/∂x₂]

CLASSIFICATION from eigenvalues λ₁, λ₂ of A:
  ┌──────────────────────────────────────────────────────────────┐
  │ EIGENVALUES           │ TYPE       │ STABILITY               │
  ├───────────────────────┼────────────┼─────────────────────────┤
  │ λ₁, λ₂ < 0 (real)    │ Stable node│ Asymptotically stable   │
  │ λ₁, λ₂ > 0 (real)    │ Unstable   │ Unstable                │
  │                       │ node       │                         │
  ├───────────────────────┼────────────┼─────────────────────────┤
  │ λ₁ < 0 < λ₂ (real)   │ Saddle     │ Unstable (saddle)       │
  ├───────────────────────┼────────────┼─────────────────────────┤
  │ λ = α ± jβ, α < 0    │ Stable     │ Asymptotically stable   │
  │                       │ spiral     │                         │
  │ λ = α ± jβ, α > 0    │ Unstable   │ Unstable                │
  │                       │ spiral     │                         │
  ├───────────────────────┼────────────┼─────────────────────────┤
  │ λ = ±jβ (purely imag.)│ Center     │ Stable (Lyapunov) but  │
  │                       │            │ NOT asymptotically —    │
  │                       │            │ linearization ambiguous │
  └───────────────────────┴────────────┴─────────────────────────┘

  NOTE: Center is ambiguous — nonlinear terms determine actual behavior
  (could be stable focus, unstable focus, or true center depending on
  higher-order terms). Hartman-Grobman theorem fails here.
```

### Limit Cycles and Poincaré-Bendixson

```
VAN DER POL OSCILLATOR:
  ẍ - μ(1 - x²)ẋ + x = 0     (μ > 0)

  For small x: negative damping (energy input) → growing oscillation
  For large x: positive damping (energy dissipation) → amplitude decreases
  Result: stable limit cycle — self-sustained oscillation

POINCARÉ-BENDIXSON THEOREM:
  If a bounded region R ⊂ ℝ² has no equilibria, then any trajectory
  that stays in R must approach a limit cycle.

  CONSTRUCTIVE USE:
  1. Find trapping region (nullclines bound trajectories inside)
  2. Rule out equilibria inside region
  3. Conclude: limit cycle must exist (existence proof)

BENDIXSON-DULAC CRITERION (ruling out limit cycles):
  If ∂(Bf₁)/∂x₁ + ∂(Bf₂)/∂x₂ ≠ 0 in R (doesn't change sign)
  for some function B(x₁, x₂) > 0, then no limit cycles in R.

NOTE: All of this is specific to 2D. In 3D+: chaos is possible (Lorenz).
  Poincaré-Bendixson has no 3D analog.
```

---

## Lyapunov Stability Theory

### Stability Definitions

```
EQUILIBRIUM x* = 0 (translate to origin without loss of generality)

STABLE (Lyapunov): ∀ε > 0, ∃δ > 0 such that ‖x(0)‖ < δ → ‖x(t)‖ < ε ∀t ≥ 0
  (trajectories starting close stay close)

ASYMPTOTICALLY STABLE: Lyapunov stable AND x(t) → 0 as t → ∞
  (trajectories converge to origin)

GLOBALLY ASYMPTOTICALLY STABLE (GAS): Asymptotically stable AND
  domain of attraction = ℝⁿ (every trajectory converges to 0)
  → This is the gold standard for controlled systems
```

### Lyapunov's Direct Method

```
LYAPUNOV FUNCTION V: ℝⁿ → ℝ

CONDITIONS FOR STABILITY:
  V(0) = 0
  V(x) > 0 for x ≠ 0  (positive definite)
  V̇(x) = (∂V/∂x) f(x) ≤ 0  (non-positive definite along trajectories)
  → Lyapunov stable

CONDITIONS FOR ASYMPTOTIC STABILITY:
  Same as above, but V̇(x) < 0 for x ≠ 0  (negative definite)
  → Asymptotically stable; V is a strict Lyapunov function

LaSALLE'S INVARIANCE PRINCIPLE (extends to V̇ ≤ 0):
  If V̇ ≤ 0 in Ω, let E = {x ∈ Ω : V̇ = 0}
  Let M = largest invariant set in E
  Then: every trajectory starting in Ω converges to M
  → Handles V̇ ≤ 0 (not strictly negative definite)
  Example: V̇ = 0 only at x = 0 → origin is AS even though V̇ is only semi-definite

GLOBAL ASYMPTOTIC STABILITY (BONUS CONDITION):
  Add: V(x) → ∞ as ‖x‖ → ∞  (radially unbounded)
  → Guarantees global (not just local) asymptotic stability
```

### Finding Lyapunov Functions

```
LINEAR SYSTEMS: ẋ = Ax
  V(x) = xᵀPx where P solves the Lyapunov equation:
  AᵀP + PA = -Q  for any Q > 0 (positive definite)
  Solution P > 0 exists ⟺ A is Hurwitz (all eigenvalues in LHP)

POLYNOMIAL SYSTEMS (Sum of Squares, SOS):
  Want V polynomial, V > 0, V̇ < 0
  → Rewrite as SOS program:
    V(x) = σ₀(x) (SOS polynomial ≥ 0)
    -V̇(x) - ε‖x‖² = σ₁(x) (SOS)
  → Semidefinite program (SDP) — solves via MATLAB SOSTOOLS, DSOS/SDSOS

PHYSICAL INTUITION (energy shaping):
  For mechanical systems: V = kinetic + potential energy
    V = ½q̇ᵀMq̇ + U(q)  where M = inertia matrix, U = potential
    V̇ = -q̇ᵀDq̇ ≤ 0 when damping matrix D ≥ 0
  → Physical energy is a Lyapunov function if system is passive

NO SYSTEMATIC PROCEDURE IN GENERAL:
  Finding Lyapunov functions is an art/heuristic for nonlinear systems.
  SOS programs automate polynomial case but don't cover everything.
```

---

## Feedback Linearization

### Input-Output Linearization

```
GOAL: Find a nonlinear state feedback u = α(x) + β(x)v such that
  the closed-loop from v to output y is exactly linear (differential equation).

RELATIVE DEGREE r: Number of times you must differentiate output y
  before the input u explicitly appears.

  y⁽⁰⁾ = h(x)
  y⁽¹⁾ = ∂h/∂x · f(x)
  y⁽²⁾ = Lf²h(x)    (Lie derivative: Lfh = ∂h/∂x · f)
  ...
  y⁽ʳ⁾ = Lfʳh(x) + LgLfʳ⁻¹h(x) · u    (u appears at r-th derivative)

  Lie derivative: Lfh = ∂h/∂x · f(x)

LINEARIZING CONTROL:
  u = 1/LgLfʳ⁻¹h · [-Lfʳh + v]

  → y⁽ʳ⁾ = v  (pure integrator chain of length r — exactly linear!)

STATE TRANSFORMATION:
  Define: z₁ = y, z₂ = ẏ, ..., zᵣ = y⁽ʳ⁻¹⁾  → linear subsystem ż = Az + Bv
  Remaining n-r states: internal dynamics (zero dynamics when y ≡ 0)
```

### Zero Dynamics and Stability Condition

```
ZERO DYNAMICS: Internal dynamics when output is held to zero (y ≡ 0)
  by appropriate input.

MINIMUM PHASE: Zero dynamics are asymptotically stable
  (analogy: minimum phase in linear systems = all zeros in LHP)

CRITICAL: Feedback linearization is only safe if the system is minimum phase!
  Non-minimum phase zero dynamics = internal instability
  (bounded output, unbounded internal states)

EXAMPLE — Pendulum-on-cart:
  State: [x (cart pos), ẋ, θ (angle), θ̇]
  Output: y = x (cart position)
  Relative degree: 2 (ÿ depends on u)
  Zero dynamics: pendulum angle when cart is fixed
  Minimum phase? YES if pendulum hangs down (stable equilibrium θ = 0)
  NOT minimum phase if pendulum is inverted (balancing problem):
    → Use different output or full-state feedback approach

GLOBAL VALIDITY:
  Feedback linearization requires LgLfʳ⁻¹h(x) ≠ 0 (invertibility)
  This may fail at certain states (singularities)
  Domain of validity must be checked carefully
```

---

## Sliding Mode Control

### Sliding Surface Design

```
SYSTEM: ẋ = f(x) + g(x)u + d(x)  where d(x) is disturbance, ‖d‖ ≤ D

SLIDING SURFACE: s(x) = 0
  Define: s(x) = cᵀe  where e = x - x_d (tracking error)
  For r-th order system: s = e⁽ʳ⁻¹⁾ + c_{r-2}e⁽ʳ⁻²⁾ + ... + c₀e
  When s = 0: error dynamics are governed by polynomial λʳ⁻¹ + c_{r-2}λʳ⁻² + ... + c₀
  → Choose coefficients for desired sliding dynamics (stable polynomial)

REACHING CONDITION: sṡ < 0  (trajectories driven toward s = 0)
  → Once on the surface, they stay on it (positive invariant manifold)

CONTROL LAW:
  u = u_eq + u_sw
  u_eq = equivalent control (what would maintain s = 0 nominally)
  u_sw = -k · sgn(s)  (discontinuous switching component)

  Choose k > D/|Lg s| + η (η > 0)  to overcome disturbance
```

### Finite-Time Convergence Proof

```
LYAPUNOV FUNCTION: V = s²/2

V̇ = sṡ = s[s_eq + LgS · u_sw + d_s]
   = s[0 - k · sgn(s) + d_s]      (u_eq cancels s_eq)
   ≤ -k|s| + D|s|                  (disturbance bound)
   = -(k - D)|s|                   (if k > D)
   = -(k - D)√(2V)

V̇ ≤ -c√V  where c = (k - D)√2

SOLUTION: √V(t) ≤ √V(0) - ct/2
→ V → 0 in finite time t* = 2√V(0)/c = |s(0)|/(k-D) · √2

FINITE-TIME CONVERGENCE: Sliding surface reached in finite time t*
After reaching: s(t) = 0 for all t ≥ t* (sliding mode maintained)
During sliding: error dynamics governed by stable polynomial (designed above)
→ Asymptotic tracking despite bounded disturbances d(x)
```

### Chattering Problem

```
IDEAL SLIDING: Infinitely fast switching — creates chattering
  High-frequency oscillation in control signal u
  → Excites unmodeled high-frequency dynamics
  → Mechanical wear, actuator damage

BOUNDARY LAYER SMOOTHING:
  Replace sgn(s) with saturation: sat(s/φ)
  where φ = boundary layer thickness

  Inside |s| < φ: u_sw = -(k/φ)s  (linear in the layer)
  Outside |s| ≥ φ: u_sw = -k·sgn(s) (original)

TRADEOFF:
  Smaller φ: less steady-state error, more chattering
  Larger φ: no chattering, but steady-state error ∝ φ
  Sliding mode → continuous approximation, losing some robustness
```

---

## Backstepping

```
PROBLEM: Strict-feedback systems (each state feeds only forward)
  ẋ₁ = f₁(x₁) + g₁(x₁)x₂
  ẋ₂ = f₂(x₁,x₂) + g₂(x₁,x₂)x₃
  ...
  ẋₙ = fₙ(x) + gₙ(x)u

RECURSIVE LYAPUNOV DESIGN:
  Step 1: Treat x₂ as "virtual control" for x₁-subsystem
    Choose x₂* = α₁(x₁) to make V₁ = x₁² decrease
    Define tracking error: z₂ = x₂ - α₁(x₁)

  Step 2: Design for [x₁, z₂]-system
    V₂ = V₁ + z₂²/2
    Choose x₃* = α₂(x₁, x₂) so V̇₂ ≤ -c₁x₁² - c₂z₂²

  Continue until actual control u appears...

RESULT: Globally stabilizing controller with explicit Lyapunov function
DRAWBACK: Differentiating virtual controls αₖ creates "explosion of terms"
  — derivatives grow exponentially, implementation becomes complex
  → Dynamic Surface Control (DSC) uses filters instead of analytic derivatives
```

---

## Passivity-Based Control

```
PASSIVE SYSTEM: ∃ storage function V(x) ≥ 0, V(0) = 0 such that:
  V̇(x, u) ≤ yᵀu   (power supplied ≥ rate of energy storage)
  V̇ = yᵀu - d(x)  where d(x) ≥ 0 is dissipation

EULER-LAGRANGE MECHANICAL SYSTEMS:
  M(q)q̈ + C(q,q̇)q̇ + G(q) = τ  (robot dynamics)
  V = ½q̇ᵀM(q)q̇ + U(q)  (kinetic + potential energy)
  V̇ = q̇ᵀτ  →  passive with input τ, output q̇

IDA-PBC (Interconnection and Damping Assignment — Passivity Based Control):
  Desired closed-loop energy: H_d(x) (shape to have minimum at setpoint)
  Inject virtual damping: u = u_es + u_di  (energy shaping + damping injection)

  RESULT: Closed loop is passive with modified energy H_d → converges to minimum

ADVANTAGES:
  Global stability results for robot/power electronics control
  Physical interpretation of control action
  Modular: can interconnect passive subsystems → passive total system
```

---

## Decision Cheat Sheet

```
┌──────────────────────────────────────────────────────────────────────┐
│ SCENARIO                     │ RECOMMENDATION                       │
├──────────────────────────────┼───────────────────────────────────────┤
│ 2D system, need stability    │ Phase plane + Poincaré-Bendixson for │
│ analysis or limit cycle study│ existence; Lyapunov for stability     │
├──────────────────────────────┼───────────────────────────────────────┤
│ Need global stability proof  │ Lyapunov direct method; SOS programs │
│ (not just local linear)      │ for polynomial systems                │
├──────────────────────────────┼───────────────────────────────────────┤
│ Exact linearization desired  │ Feedback linearization; FIRST check  │
│ (cancel nonlinearities)      │ minimum phase (zero dynamics stable) │
├──────────────────────────────┼───────────────────────────────────────┤
│ Disturbance rejection,       │ Sliding mode; tune k for disturbance │
│ finite-time convergence      │ bound; add boundary layer for        │
│                              │ chattering reduction                  │
├──────────────────────────────┼───────────────────────────────────────┤
│ Strict-feedback structure,   │ Backstepping (systematic Lyapunov    │
│ need systematic design       │ design); DSC for lower complexity    │
├──────────────────────────────┼───────────────────────────────────────┤
│ Robotics, port-Hamiltonian   │ Passivity-based control (IDA-PBC);  │
│ systems, power electronics   │ energy shaping + damping injection   │
└──────────────────────────────┴───────────────────────────────────────┘
```

---

## Common Confusion Points

**Lyapunov stability is NOT the same as BIBO stability.** Lyapunov stability is about autonomous systems (no input) and behavior near equilibrium. BIBO stability is about bounded inputs producing bounded outputs. For nonlinear systems with inputs, Input-to-State Stability (ISS) is the right concept: ISS guarantees that if input u is bounded, state x is bounded, with explicit gain function.

**Feedback linearization works globally only if the diffeomorphism is global.** The coordinate change (x → z) must be a valid diffeomorphism everywhere in the state space, and LgLfʳ⁻¹h ≠ 0 everywhere. In practice, these conditions fail outside some region, and the controller has a domain of validity.

**Sliding mode chattering is not just a nuisance — it can destroy systems.** High-frequency control switching excites structural modes in flexible robots, heats actuators, and degrades seals in hydraulics. The boundary layer fixes chattering at the cost of removing the sliding mode's key property (exact disturbance rejection). Higher-order sliding mode control (super-twisting algorithm) achieves finite-time convergence without chattering for second-order sliding surfaces.

**Backstepping requires exact knowledge of nonlinear terms.** The virtual control laws αₖ(x₁,...,xₖ) must be differentiated, requiring exact knowledge of f₁,...,fₖ. With unknown nonlinearities, adaptive backstepping or NN-based estimation is needed to approximate the unknown functions.

**Phase plane analysis is limited to n = 2.** For 3D systems, trajectories can be chaotic (Lorenz). Limit cycles in 3D are possible but not guaranteed by trapping regions alone. Poincaré sections (intersections of trajectories with a 2D plane) extend the analysis to higher dimensions but are much more complex.

**LaSalle's invariance principle requires the system to be autonomous (no explicit t dependence).** For time-varying systems ẋ = f(x, t), LaSalle does not apply directly. Use Barbalat's lemma: if V̇ is uniformly continuous and ∫₀^∞ V̇ dt converges, then V̇ → 0. This is the standard tool for proving convergence in adaptive control.
