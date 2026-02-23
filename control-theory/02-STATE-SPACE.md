# State-Space Representation — Modern Control Theory

## The Big Picture

State-space methods are the language of modern (post-1960) control theory. Where classical
control (Bode, Nyquist, root locus) works in the frequency domain on SISO systems,
state-space works in the time domain on **MIMO** (multi-input, multi-output) systems.
The two perspectives are mathematically equivalent for LTI systems but state-space
scales to arbitrary dimensionality.

```
+------------------------------------------------------------------+
|              STATE-SPACE MENTAL MODEL                            |
|                                                                   |
|  Physical system:                                                 |
|    Inputs u(t) ─────→ [PLANT DYNAMICS] ─────→ Outputs y(t)     |
|                           ↕                                       |
|                        State x(t)                                 |
|                   (internal variables)                            |
|                                                                   |
|  Equations:                                                       |
|    ẋ = Ax + Bu    (state update, vector ODE)                     |
|    y  = Cx + Du   (output equation)                              |
|                                                                   |
|  x ∈ ℝⁿ  : state vector (position, velocity, temperature, ...)  |
|  u ∈ ℝᵐ  : input vector (voltages, forces, flow rates, ...)     |
|  y ∈ ℝᵖ  : output vector (sensor measurements)                  |
|  A ∈ ℝⁿˣⁿ: system matrix    (dynamics)                          |
|  B ∈ ℝⁿˣᵐ: input matrix     (how input enters)                  |
|  C ∈ ℝᵖˣⁿ: output matrix    (what we can observe)               |
|  D ∈ ℝᵖˣᵐ: feedthrough (often 0 in physical systems)            |
+------------------------------------------------------------------+
```

State-space is the Hamiltonian mechanics of control: replace the high-order ODE with a
first-order vector ODE. The state x(t) is the minimal information needed to predict
all future outputs given future inputs.

---

## From ODE to State-Space

### Example: Harmonic Oscillator (mass-spring-damper)

```
ODE: mẍ + cẋ + kx = f(t)

STATE VARIABLES:   x₁ = position x,   x₂ = velocity ẋ

STATE EQUATIONS:
  ẋ₁ = x₂
  ẋ₂ = -(k/m)x₁ - (c/m)x₂ + (1/m)f

Matrix form:
  [ẋ₁]   [  0      1 ] [x₁]   [ 0  ]
  [ẋ₂] = [-k/m  -c/m ] [x₂] + [1/m ] f

  ẋ = Ax + Bu

Output (position sensor):
  y = [1  0] [x₁] + [0] f
              [x₂]
  y = Cx + Du
```

### General Procedure

```
Given: nth-order ODE   y^(n) + a_{n-1}y^(n-1) + ... + a₁ẏ + a₀y = b_m u^(m) + ... + b₀u

Set state variables:   x₁ = y, x₂ = ẏ, ..., xₙ = y^(n-1)

Companion (controllable canonical) form:
  A = [0   1   0   ...  0 ]
      [0   0   1   ...  0 ]
      [⋮                  ]
      [0   0   0   ...  1 ]
      [-a₀ -a₁ -a₂ ... -a_{n-1}]

  B = [0; 0; ... ; 0; 1]  (or with input derivatives: more complex)
```

### Transfer Function to/from State-Space

```
TRANSFER FUNCTION:
  G(s) = C(sI - A)⁻¹B + D

  This connects the two representations:
  Y(s) = G(s)U(s) = [C(sI-A)⁻¹B + D]U(s)

INVERSE (realization problem):
  Given G(s) = N(s)/D(s), find (A,B,C,D) such that C(sI-A)⁻¹B + D = G(s)
  Not unique! Infinite realizations; canonical forms pin down choice.

MINIMAL REALIZATION:
  n = deg(D(s)) when common factors between N and D canceled.
  Non-minimal realizations have unobservable or uncontrollable modes.
```

---

## Solution to State Equations

### Homogeneous (u=0): Matrix Exponential

```
ẋ = Ax,  x(0) = x₀

Solution: x(t) = e^{At} x₀

MATRIX EXPONENTIAL:
  e^{At} = I + At + (At)²/2! + (At)³/3! + ...
         = Σ_{k=0}^∞ (At)^k / k!

  Properties:
    e^{A·0} = I
    d/dt e^{At} = A e^{At}
    (e^{At})⁻¹ = e^{-At}
    e^{A(t₁+t₂)} = e^{At₁} e^{At₂}  (but e^{(A+B)t} ≠ e^{At}e^{Bt} unless [A,B]=0)
```

### General Solution: Variation of Parameters

```
ẋ = Ax + Bu, x(0) = x₀

x(t) = e^{At} x₀ + ∫₀ᵗ e^{A(t-τ)} B u(τ) dτ

       ───────────   ────────────────────────────────
       homogeneous   particular (convolution with input)
```

### Eigenvalue Analysis

```
EIGENVALUES of A = {λᵢ} determine stability and response:

If A is diagonalizable: A = VΛV⁻¹  (V = eigenvectors, Λ = diag(λᵢ))
  e^{At} = V e^{Λt} V⁻¹

  e^{Λt} = diag(e^{λ₁t}, e^{λ₂t}, ..., e^{λₙt})

  e^{λt} behavior:
    Re(λ) < 0:  decaying exponential (stable mode)
    Re(λ) > 0:  growing exponential (unstable mode)
    Re(λ) = 0, Im(λ) ≠ 0: sustained oscillation
    λ = 0:  constant (integrator)

STABILITY CRITERION:
  System ẋ = Ax is asymptotically stable
  ⟺ all eigenvalues of A have Re(λᵢ) < 0
  ⟺ all poles of transfer function in left half s-plane
```

---

## Controllability

A system is **controllable** if any initial state x₀ can be driven to any desired state
xf in finite time by some input u(t).

```
CONTROLLABILITY MATRIX:
  𝒞 = [B | AB | A²B | ... | A^{n-1}B]   (n × nm matrix)

KALMAN RANK CONDITION:
  System (A,B) is controllable ⟺ rank(𝒞) = n

CONTROLLABILITY GRAMIAN (alternative test):
  W_c(t) = ∫₀ᵗ e^{Aτ} B Bᵀ e^{Aᵀτ} dτ
  Controllable ⟺ W_c(t) is positive definite for any t > 0

PHYSICAL INTERPRETATION:
  If rank(𝒞) = r < n: only r-dimensional subspace reachable.
  n - r modes are "hidden" from the input — cannot be controlled.

MINIMUM ENERGY CONTROL:
  Minimum input energy to reach x_f from x₀=0:
    u*(t) found via W_c(T)⁻¹ (requires W_c invertible, i.e., controllable)
    Minimum energy = x_fᵀ W_c(T)⁻¹ x_f
```

**Example:** Why differential drive robot always has rank-deficient 𝒞 in 3D:
```
[x, y, θ] state, [v, ω] input (velocity, angular rate)
A = 0 (kinematic model), B = [cos θ, 0; sin θ, 0; 0, 1]
rank(𝒞) = rank([B, AB]) = ... depends on current θ
→ Locally controllable but not globally by linear criteria alone
```

---

## Observability

A system is **observable** if the initial state x₀ can be uniquely determined from
observations of y(t) over a finite time interval.

```
OBSERVABILITY MATRIX:
  𝒪 = [C; CA; CA²; ...; CA^{n-1}]   (np × n matrix)

KALMAN RANK CONDITION:
  System (A,C) is observable ⟺ rank(𝒪) = n

OBSERVABILITY GRAMIAN:
  W_o(t) = ∫₀ᵗ e^{Aᵀτ} Cᵀ C e^{Aτ} dτ
  Observable ⟺ W_o(t) positive definite

DUALITY:
  (A,B) controllable ⟺ (Aᵀ,Bᵀ) observable
  Controllab. and observab. are dual problems (transpose and swap B↔C)
```

---

## State Feedback Control

If all states are measurable, use **state feedback**: u = -Kx + Nr

```
CLOSED-LOOP SYSTEM with state feedback:
  u = -Kx + Nr   (K ∈ ℝᵐˣⁿ, N = precompensator for tracking)

  ẋ = Ax + Bu = Ax + B(-Kx + Nr) = (A - BK)x + BNr
  y  = Cx

  Closed-loop A_cl = A - BK
  Closed-loop eigenvalues = eigenvalues of (A - BK)

GOAL: Choose K to place eigenvalues of A - BK at desired locations.

POLE PLACEMENT (arbitrary):
  Theorem: If (A,B) is controllable, eigenvalues of (A-BK) can be
  placed ANYWHERE in ℂ by appropriate choice of K.

  SISO (m=1): Ackermann's formula
    K = eₙᵀ 𝒞⁻¹ p(A)
    where eₙᵀ = [0 ... 0 1], p(A) = desired characteristic polynomial evaluated at A

  MIMO: more degrees of freedom; use place() algorithms or optimization
```

### Desired Pole Placement

```
DESIRED POLE LOCATIONS depend on specs:
  Rise time tr: ωn ≈ 1.8/tr
  Overshoot: ζ from OS% = exp(-πζ/√(1-ζ²))
  Settling time: ζωn ≈ 4/ts (2% criterion)

  Place dominant poles at s = -ζωn ± jωn√(1-ζ²)
  Place remaining (n-2) poles 5-10× farther left (fast modes, negligible)

  Rule of thumb: non-dominant poles at Re(s) < 5 × Re(dominant poles)

ENERGY CONSIDERATION:
  Poles too far left → fast response but large u(t) values
  Physical actuators have limits: don't place poles unrealistically fast
```

---

## State Observer (Luenberger Observer)

When not all states are measurable (which is the common case), estimate x from output y:

```
OBSERVER (ESTIMATOR):
  x̂̇ = Ax̂ + Bu + L(y - Cx̂)
     = (A - LC)x̂ + Bu + Ly

  x̂ = estimated state
  L ∈ ℝⁿˣᵖ = observer gain matrix (to be designed)

ESTIMATION ERROR:
  Define ẽ = x - x̂

  ẽ̇ = ẋ - x̂̇
     = (Ax + Bu) - ((A - LC)x̂ + Bu + Ly)
     = A(x - x̂) - LC(x - x̂)
     = (A - LC)ẽ

  Error dynamics: ẽ(t) = e^{(A-LC)t} ẽ(0)

  Choose L so eigenvalues of (A - LC) are stable and fast
  → error ẽ → 0 exponentially

POLE PLACEMENT FOR OBSERVER:
  Theorem: If (A,C) is observable, eigenvalues of (A-LC) can be placed
  anywhere by appropriate choice of L.
  (Dual of state feedback! Just replace: A→Aᵀ, B→Cᵀ, K→Lᵀ)

OBSERVER POLE PLACEMENT GUIDELINE:
  Observer poles 3-10× faster than controller poles
  (want estimation to converge before control loop cares)
  But: faster observer → more noise amplification
```

---

## Separation Principle

The most important theorem for observer-based control:

```
SEPARATION PRINCIPLE (Certainty Equivalence):
  Design state feedback K (ignoring estimation error) SEPARATELY from
  Design observer gain L (ignoring control problem)
  Then use: u = -Kx̂

  Combined system closed-loop eigenvalues =
    eigenvalues of (A - BK)  ∪  eigenvalues of (A - LC)
  (completely decoupled!)

COMBINED STATE EQUATIONS:
  [ẋ ]   [A-BK    BK  ] [x ]   [B ]
  [ẽ̇ ] = [  0   A-LC  ] [ẽ ] + [0 ] r

  y = [C  0] [x; ẽ]

  Block triangular → eigenvalues = union of two sets.
```

This is the foundation of the Kalman filter (optimal observer) combined with LQR
(optimal state feedback) = LQG (Linear Quadratic Gaussian) controller.

---

## Canonical Forms

```
CONTROLLABLE CANONICAL FORM (companion form):
  A = [0   1   0  ...  0]     B = [0]
      [0   0   1  ...  0]         [0]
      [⋮                ]         [⋮]
      [-a₀ -a₁ -a₂ ... -a_{n-1}]  [1]
  Useful for: Ackermann's formula, SISO design

OBSERVABLE CANONICAL FORM:
  A = (controllable canonical)ᵀ,  B = Cᵀ of controllable
  Useful for: observer design via duality

JORDAN NORMAL FORM:
  A = V J V⁻¹  where J is block-diagonal with Jordan blocks
  Useful for: modal analysis, decoupled dynamics
  Each Jordan block corresponds to an eigenvalue + algebraic multiplicity

MODAL FORM:
  If A has distinct real eigenvalues: A diagonal
  ẋ = Λx + Bu (decoupled integrators)
  Useful for: understanding which modes input excites
```

---

## Stability Analysis

### Lyapunov Method for State-Space

```
LYAPUNOV STABILITY THEOREM:
  System ẋ = f(x) is asymptotically stable at x=0 if:
  ∃ V(x) > 0 (positive definite) with V(0) = 0
              V̇(x) = ∇V(x)·f(x) < 0 (negative definite)

  V(x) = "Lyapunov function" (generalized energy)

FOR LINEAR SYSTEMS (ẋ = Ax):
  Lyapunov equation: AᵀP + PA = -Q
  (P symmetric positive definite, Q symmetric positive definite)
  System stable ⟺ unique P > 0 exists (for any Q > 0)
  V(x) = xᵀPx is Lyapunov function

  Interpretation: P is "energy metric"; AᵀP+PA=-Q says energy dissipates
```

---

## Discrete-Time State-Space

For digital control systems (what actually runs in software):

```
DISCRETE-TIME MODEL:
  x[k+1] = A_d x[k] + B_d u[k]
  y[k]   = C x[k] + D u[k]

  From continuous (ZOH — zero-order hold at sampling period T_s):
    A_d = e^{A·T_s}
    B_d = ∫₀^{T_s} e^{Aτ} B dτ = (A_d - I) A⁻¹ B  (if A invertible)

STABILITY:
  Discrete-time: stable iff all eigenvalues of A_d inside unit circle |λ| < 1
  (analogous to left half-plane condition for continuous)

Z-TRANSFORM RELATIONSHIP:
  z-domain transfer function: H(z) = C(zI - A_d)⁻¹B_d + D
  Poles of H(z) = eigenvalues of A_d

CONTROLLABILITY/OBSERVABILITY:
  Same rank conditions as continuous case — just substitute A_d, B_d
```

---

## Decision Cheat Sheet

| Task | Method |
|------|--------|
| Model a system with multiple inputs/outputs | State-space (A,B,C,D) |
| Check if all states can be controlled | Rank of controllability matrix 𝒞 |
| Check if all states can be inferred from outputs | Rank of observability matrix 𝒪 |
| Place closed-loop poles (full state) | State feedback K via Ackermann or place() |
| Estimate states from outputs | Luenberger observer (pole placement on A-LC) |
| Combine observer + state feedback | Separation principle: design independently |
| Analyze stability of nonlinear system | Lyapunov function V(x) > 0, V̇ < 0 |
| Convert continuous to digital control | Zero-order hold discretization |
| Find transfer function from state-space | G(s) = C(sI-A)⁻¹B + D |

## Common Confusion Points

**Controllability ≠ stabilizability.** Controllability requires ALL modes reachable.
Stabilizability (weaker) only requires unstable modes to be controllable. For feedback
design, stabilizability is sufficient.

**Observability ≠ detectability.** Observability requires ALL states inferable.
Detectability requires unstable states to be observable. The Kalman filter needs
detectability, not full observability.

**State feedback needs all states; observer reconstructs missing ones.** The separation
principle says you can first design K pretending you have full state, then design L
to estimate the state, and combine. The eigenvalues don't interact.

**Eigenvalues of A ≠ closed-loop poles.** The plant eigenvalues (A's eigenvalues) are
the open-loop poles. State feedback moves them to eigenvalues of (A-BK). Observer
places its own poles at eigenvalues of (A-LC). Both are free to choose.

**Non-minimal realizations have hidden modes.** If the transfer function numerator
and denominator share a common factor, there are unobservable AND uncontrollable
modes that cancel in the I/O description but are physically present (and can
be unstable — internal stability matters even when I/O looks fine).
