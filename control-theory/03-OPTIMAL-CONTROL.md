# Optimal Control — LQR, LQG, Pontryagin, HJB

## The Big Picture

Optimal control asks: **among all admissible inputs u(t), which one minimizes a given
cost functional J?** This turns control design from an art (where to place poles?) into
an optimization problem with a rigorous solution. Two main paths:

```
+------------------------------------------------------------------+
|               OPTIMAL CONTROL PATHS                              |
|                                                                   |
|  INDIRECT METHODS (calculus of variations approach)              |
|  ─────────────────────────────────────────────────               |
|  Pontryagin Minimum Principle (PMP)                              |
│  → Necessary conditions for optimality (Hamiltonian system)      |
|  → Works for constrained inputs, nonlinear systems               |
|  → Bang-bang control, minimum-time problems                      |
|                                                                   |
|  DIRECT METHODS (dynamic programming approach)                   |
|  ────────────────────────────────────────────                    |
|  Hamilton-Jacobi-Bellman (HJB) equation                         |
|  → Sufficient conditions; optimal value function V*(x,t)         |
|  → LQR: HJB + linear + quadratic = algebraic Riccati equation   |
|  → Works backward in time; curse of dimensionality in general    |
|                                                                   |
|  LQR = Linear Quadratic Regulator                                |
|  LQG = LQR + Kalman Filter (stochastic version)                 |
|  H∞  = Minimax (worst-case disturbance)                         |
+------------------------------------------------------------------+
```

---

## Calculus of Variations Primer

Optimal control extends classical calculus of variations to dynamical systems.

```
CLASSICAL PROBLEM: minimize J = ∫_{t₀}^{t_f} L(x(t), ẋ(t), t) dt

Euler-Lagrange equation (necessary condition):
  ∂L/∂x - d/dt(∂L/∂ẋ) = 0

Example: shortest path in ℝ² (L = √(1 + ẋ²))
  E-L → ẍ = 0 → x(t) is linear → straight line ✓

OPTIMAL CONTROL EXTENSION:
  State dynamics: ẋ = f(x, u, t)  (constraint)
  Cost: J = Φ(x(t_f)) + ∫_{t₀}^{t_f} L(x, u, t) dt
  Optimal: u*(t) minimizes J over all admissible inputs

  Control Hamiltonian: H(x, u, λ, t) = L(x, u, t) + λᵀf(x, u, t)
  λ(t) = costate (Lagrange multiplier for dynamics constraint)
```

---

## Pontryagin Minimum Principle (PMP)

**Necessary conditions** for optimal control:

```
THEOREM (Pontryagin et al. 1962):
  If u*(t) is optimal with trajectory x*(t), then ∃ costate λ*(t) ≠ 0 such that:

  1. STATE EQUATION:
     ẋ* = ∂H/∂λ = f(x*, u*, t)

  2. COSTATE EQUATION:
     λ̇* = -∂H/∂x|_{x*,u*,λ*}  ← costate flows "backward" in time

  3. MINIMALITY CONDITION:
     H(x*, u*(t), λ*, t) = min_u H(x*, u, λ*, t)  for all t ∈ [t₀, t_f]

  4. BOUNDARY CONDITIONS:
     x*(t₀) = x₀  (initial state fixed)
     λ*(t_f) = ∂Φ/∂x|_{t_f}  (transversality condition)

  This gives a TWO-POINT BOUNDARY VALUE PROBLEM (TPBVP):
    forward: ẋ = f(x, u, t)
    backward: λ̇ = -∂H/∂x
    boundary: x(t₀) = x₀, λ(t_f) = ∂Φ/∂x
```

### Bang-Bang Control (Minimum Time)

```
MINIMUM TIME PROBLEM: minimize t_f, subject to ẋ = Ax + Bu, |u| ≤ 1

H = 1 + λᵀ(Ax + Bu) = 1 + λᵀAx + λᵀBu

Minimality: min_u H ⟺ min_u (λᵀB)u
  Since u ∈ [-1, +1]:
    u* = -sign(λᵀB)  ← bang-bang! (switches between ±1)

Switching function σ(t) = λᵀ(t)B:
  σ > 0 → u* = -1
  σ < 0 → u* = +1
  σ = 0 → singular arc (more analysis needed)

This explains why minimum-time controllers for rockets, F1 cars, robotics are
bang-bang — full throttle or full brake, nothing in between.
```

---

## Hamilton-Jacobi-Bellman (HJB) Equation

**Sufficient conditions** via dynamic programming (Bellman 1957):

```
BELLMAN'S PRINCIPLE OF OPTIMALITY:
  "An optimal policy has the property that whatever the initial state
   and initial decisions, the remaining decisions must constitute an
   optimal policy with regard to the state resulting from first decision."

OPTIMAL VALUE FUNCTION:
  V*(x, t) = min_{u[t,t_f]} J = min_{u[t,t_f]} [Φ(x(t_f)) + ∫_t^{t_f} L dτ]

HJB EQUATION (PDE for V*):
  -∂V*/∂t = min_u [L(x, u, t) + (∂V*/∂x) f(x, u, t)]

  Boundary condition: V*(x, t_f) = Φ(x)

OPTIMAL CONTROL from V*:
  u*(x, t) = argmin_u [L(x, u, t) + (∂V*/∂x) f(x, u, t)]

RELATIONSHIP TO PMP:
  Costate: λ*(t) = ∂V*/∂x|_{x*(t),t}
  Both give same u*; HJB gives value function (global), PMP gives trajectory (local)

CURSE OF DIMENSIONALITY:
  HJB is a PDE in n+1 dimensions (state + time)
  Grid-based solution: exponential in n
  → Practical only for low-dimensional systems (n ≤ 4-5 typically)
  → LQR solves it analytically for linear-quadratic case

<!-- @editor[bridge/P3]: The curse of dimensionality in HJB has a direct analog in distributed systems planning: optimal resource scheduling across N services with M constraint dimensions is NP-hard, and approximate methods (greedy, LP relaxation, receding-horizon MPC) are the practical answer for the same reason that LQR and MPC supplant direct HJB solutions. Worth a one-sentence bridge. -->
```

---

## LQR — Linear Quadratic Regulator

The most important optimal control result: closed-form solution for linear systems.

```
PROBLEM:
  System:  ẋ = Ax + Bu
  Cost:    J = ½ xᵀ(t_f)S x(t_f) + ½ ∫₀^{t_f} [xᵀQx + uᵀRu] dt

  Q ≥ 0   (state cost, positive semi-definite)
  R > 0   (input cost, positive definite)
  S ≥ 0   (terminal state cost)

  Q weights: how much do you care about state deviation?
  R weights: how expensive is control effort?

SOLUTION (via HJB with V* = xᵀPx):
  Optimal control:  u*(t) = -R⁻¹Bᵀ P(t) x(t)
  State feedback gain: K(t) = R⁻¹Bᵀ P(t)

  P(t) satisfies the MATRIX RICCATI EQUATION (finite horizon):
    -Ṗ = AᵀP + PA - PBR⁻¹BᵀP + Q,   P(t_f) = S
    (backward-in-time ODE for the n×n matrix P)

INFINITE-HORIZON LQR (t_f → ∞):
  Riccati equation becomes ALGEBRAIC RICCATI EQUATION (ARE):
    AᵀP + PA - PBR⁻¹BᵀP + Q = 0   (solve for steady-state P ≥ 0)

  Optimal control: u* = -Kx   where K = R⁻¹BᵀP  ← constant gain!
  Closed-loop: ẋ = (A - BK)x  (asymptotically stable if (A,B) controllable, (A,Q^½) observable)
```

### ARE Solution

```
ALGEBRAIC RICCATI EQUATION:
  AᵀP + PA - PBR⁻¹BᵀP + Q = 0

SOLVING:
  Hamiltonian matrix approach:
    H = [ A       -BR⁻¹Bᵀ]
        [-Q       -Aᵀ    ]   (2n × 2n)

  H has n eigenvalues in LHP, n in RHP (symmetric about imaginary axis).
  P = V₂ V₁⁻¹  where [V₁; V₂] spans the n-dim stable invariant subspace of H.

  In practice: scipy.linalg.solve_continuous_are(), MATLAB lqr() function.

MATLAB/Python:
  # Python (scipy):
  from scipy.linalg import solve_continuous_are
  P = solve_continuous_are(A, B, Q, R)
  K = np.linalg.inv(R) @ B.T @ P

STABILITY GUARANTEE:
  If (A,B) stabilizable and (A, Q^½) detectable:
  LQR closed-loop (A-BK) is always asymptotically stable.
  Infinite gain margin (≥ 6 dB guaranteed) and phase margin ≥ 60°
  → Remarkable robustness properties.
```

### Q and R Tuning Intuition

<!-- @editor[bridge/P2]: The Q/R trade-off is the control-theory formalization of a resource allocation decision that this learner makes constantly: Q weights how much you care about deviation from target (SLA violations, error budget burn rate), R weights how expensive correction is (compute cost, deployment risk, toil). Setting Q_ii = 1/(max acceptable xᵢ)² via Bryson's rule is the same reasoning as setting SLO error budget percentages — normalize by tolerance. The explicit bridge to SLO/error budget thinking would land well here. -->

```
TUNING GUIDELINES:
  Start with: Q = Cᵀ C (weight output error)
              R = I (unit control effort)

  Q_ii large → state xᵢ must stay small (aggressive control)
  Q_ii small → state xᵢ can deviate (relaxed control)
  R_ii large → control uᵢ expensive (conservative control)
  R_ii small → control uᵢ cheap (aggressive control)

  ρ = R/Q trade-off: as R→0, K→∞ (all state errors penalized heavily)
                     as R→∞, K→0 (control expensive, do nothing)

  BRYSON'S RULE (practical starting point):
    Q_ii = 1 / (max acceptable xᵢ)²
    R_jj = 1 / (max acceptable uⱼ)²
```

---

## LQG — Linear Quadratic Gaussian

LQR + Kalman filter = optimal stochastic control under separation principle:

```
STOCHASTIC SYSTEM:
  ẋ = Ax + Bu + w    (process noise: w ~ N(0, W))
  y  = Cx + v         (measurement noise: v ~ N(0, V))

SEPARATION PRINCIPLE FOR LQG:
  1. Design Kalman filter (optimal observer for noise):
     x̂̇ = Ax̂ + Bu + L(y - Cx̂)
     L = Σ Cᵀ V⁻¹   (Kalman gain)
     Σ = estimation error covariance (satisfies Riccati equation)

  2. Design LQR as if full state available:
     u = -K x̂   (feed back estimated state)

  3. Combine: LQG = LQR state feedback + Kalman state estimator.

DUAL RICCATI EQUATIONS:
  LQR:    AᵀP + PA - PBR⁻¹BᵀP + Q = 0    → K = R⁻¹BᵀP
  Kalman: AΣ + ΣAᵀ - ΣCᵀV⁻¹CΣ + W = 0   → L = ΣCᵀV⁻¹

  Note perfect duality: (A,B,Q,R) ↔ (Aᵀ,Cᵀ,W,V)

LQG CLOSED-LOOP EIGENVALUES = eigenvalues(A-BK) ∪ eigenvalues(A-LC)
  (Separation principle holds for stochastic case too)

LQG CAVEAT:
  LQR guarantees 6dB gain margin, 60° phase margin.
  LQG does NOT — combining with Kalman can destroy margins!
  → Use LTR (Loop Transfer Recovery) or H∞ for guaranteed robustness.
```

---

## H∞ Control (Minimax / Robust)

When you need robustness guarantees, not just nominal performance:

```
H∞ PROBLEM:
  Minimize the H∞ norm of the closed-loop transfer function T_{zw}:
  ‖T_{zw}‖_∞ = sup_ω σ_max(T_{zw}(jω)) < γ

  w = exogenous input (disturbances, noise, model uncertainty)
  z = performance output (regulated signals)
  γ = performance bound (minimize or achieve below threshold)

PHYSICAL MEANING:
  ‖T_{zw}‖_∞ < γ means: for any disturbance w with ‖w‖₂ ≤ 1,
  the performance output satisfies ‖z‖₂ < γ.
  = worst-case disturbance amplification is bounded by γ.

H∞ STATE-SPACE SOLUTION (Doyle-Glover-Khargonekar-Francis 1989):
  Solve two coupled Riccati equations:
    AᵀP + PA + PBᵤ Bᵤᵀ P + CᵀC - PB₁ B₁ᵀP/γ² = 0   (control)
    AΣ + ΣAᵀ + ΣCᵤᵀ Cᵤ Σ + BB ᵀ - ΣC₁ᵀ C₁ Σ/γ² = 0  (filter)

  Solution exists iff both Riccati solutions are positive definite
  and ρ(PΣ) < γ² (spectral radius condition).

H∞ vs LQG:
  LQG: optimal for known noise statistics; no guaranteed margins
  H∞: suboptimal for known stats, but guaranteed worst-case bound
  H∞ is "pessimistic" but robust to model uncertainty
```

---

## Model Predictive Control (MPC) — Preview

When you have **constraints** on states and inputs (most real systems):

```
MPC OPTIMIZATION (at each time step k):
  min  Σ_{j=0}^{N-1} [x(k+j|k)ᵀ Q x(k+j|k) + u(k+j)ᵀ R u(k+j)]
       + x(k+N|k)ᵀ P_f x(k+N|k)
  subject to:
    x(k+j+1|k) = A x(k+j|k) + B u(k+j)      (dynamics)
    x_min ≤ x(k+j|k) ≤ x_max                  (state constraints)
    u_min ≤ u(k+j) ≤ u_max                    (input constraints)

  Apply only u*(k|k), then re-solve at k+1 (receding horizon)

LQR vs MPC:
  LQR: no constraints, closed-form, optimal, instant to evaluate
  MPC: handles constraints, re-solves QP at each step, computationally heavier
  LQR = infinite-horizon unconstrained MPC (in steady state)
```

---

## Decision Cheat Sheet

| Scenario | Method |
|----------|--------|
| Linear system, no constraints, choose gains | LQR (solve algebraic Riccati) |
| LQR with noisy measurements | LQG (add Kalman filter, separation principle) |
| Need guaranteed stability margins | LQR alone (60° PM, 6dB GM) |
| Need guaranteed robustness to uncertainty | H∞ control |
| Constraints on states or inputs | MPC (receding-horizon QP) |
| Minimum-time control | PMP → bang-bang controller |
| Nonlinear system, continuous | PMP + shooting method for TPBVP |
| Analytical optimal value function | HJB (limited to low-dimension) |
| Large-scale nonlinear | Differential dynamic programming (DDP/iLQR) |
| Tune Q and R weights | Bryson's rule, then iterate |

## Common Confusion Points

**LQR is optimal for the model but not necessarily for the real system.** LQR optimality
is with respect to the quadratic cost and the *exact* linear model. Model mismatch
can degrade performance significantly. Robustness analysis (gain/phase margins) should
always accompany LQR design.

**LQG loses LQR's robustness guarantees.** Adding the Kalman filter (certainty equivalence)
can reduce gain margin to near zero. Doyle (1978) showed an example with zero gain
margin. LTR (loop transfer recovery) or H∞ design restores margins.

**HJB is a PDE, not an ODE.** The value function V*(x,t) is a scalar function of
the state (n-dimensional) and time — solving it on a grid is exponential in n.
LQR is the unique case where V* = xᵀPx quadratic form → collapses to matrix equation.

**Pontryagin gives necessary, not sufficient conditions.** u* satisfying PMP may be a
minimum, maximum, or saddle point of J. Additional conditions (strengthened Legendre-
Clebsch condition, convexity) are needed for sufficiency.

**MPC is not LQR with constraints.** MPC uses a finite horizon N and solves a QP
at each step; LQR uses infinite horizon with closed-form K. As N→∞ (and with
terminal cost chosen from LQR), they converge, but finite MPC is genuinely different.
