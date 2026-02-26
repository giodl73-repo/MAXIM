# Model Predictive Control

## Big Picture: Receding Horizon

```
┌─────────────────────────────────────────────────────────────────────┐
│               MODEL PREDICTIVE CONTROL — CORE IDEA                  │
│                                                                     │
│   TIME     t    t+1   t+2   t+3  ...  t+N                          │
│            ↓                                                        │
│   ┌────────────────────────────────────────────────────────────┐   │
│   │  SOLVE:  min  Σ_{k=0}^{N-1} [x_kᵀQx_k + u_kᵀRu_k]        │   │
│   │               + x_Nᵀ Px_N  (terminal cost)                 │   │
│   │  subject to:                                               │   │
│   │    x_{k+1} = A x_k + B u_k   (dynamics)                   │   │
│   │    x_k ∈ X, u_k ∈ U           (state/input constraints)   │   │
│   │    x_N ∈ X_f                  (terminal constraint)       │   │
│   └────────────────────────────────────────────────────────────┘   │
│            ↓                                                        │
│   APPLY: only u₀* (first optimal control)                          │
│            ↓                                                        │
│   SHIFT HORIZON → Repeat at t+1 with measured/estimated x(t+1)    │
│                                                                     │
│  ─────────────────────────────────────────────────────────────     │
│  Applied:  u₀* │ (discard)                                         │
│  Planned:  u₀* u₁* u₂*...u_{N-1}*                                 │
│                                                                     │
│  UNLIKE LQR: handles input/state CONSTRAINTS explicitly             │
│  UNLIKE PID: incorporates future predictions (feedforward-like)    │
└─────────────────────────────────────────────────────────────────────┘
```

MPC is the dominant advanced control strategy in industry: >5,000 industrial MPC applications in chemical processing, refining, automotive, aerospace. It is LQR generalized to handle constraints and nonlinearities.

---

## Standard Formulation

### Linear MPC (the foundation)

```
DISCRETE-TIME LINEAR SYSTEM:
  x_{k+1} = Ax_k + Bu_k
  y_k = Cx_k

FINITE-HORIZON OCP:
  min_{u₀,...,u_{N-1}}  J = Σ_{k=0}^{N-1} [x_kᵀQx_k + u_kᵀRu_k] + x_NᵀPx_N
  subject to:
    x_{k+1} = Ax_k + Bu_k    k = 0,...,N-1
    x_k ∈ X = {x : Cx ≤ d}   state constraints (polyhedron)
    u_k ∈ U = {u : Fu ≤ g}   input constraints (polyhedron)
    x_N ∈ X_f                 terminal set (stability)

PARAMETERS:
  Q ≥ 0: state weighting (penalize deviation from setpoint)
  R > 0: input weighting (penalize control effort)
  P: terminal cost matrix (crucial for stability — see below)
  N: prediction horizon
  X_f: terminal set (crucial for stability)
```

### Constraint Examples in Practice

```
INPUT CONSTRAINTS (always present):
  -u_max ≤ u_k ≤ u_max        (actuator saturation)
  -Δu_max ≤ u_k - u_{k-1} ≤ Δu_max  (rate of change limit)

STATE CONSTRAINTS (safety-critical):
  x_min ≤ x_k ≤ x_max         (physical limits)
  e.g., temperature ≤ 250°C, pressure ≤ 15 bar

SOFT CONSTRAINTS (handle infeasibility):
  Add slack variable ε ≥ 0:
    x_k ∈ X ⊕ ε·E  (allowed to violate by ε)
    Add ρ·‖ε‖² or ρ·‖ε‖₁ to cost  (penalize violation)
  Hard constraints: must hold (safety)
  Soft constraints: prefer to hold (performance)
```

---

## Stability Analysis

### Terminal Cost and Terminal Set

```
NOMINAL STABILITY REQUIRES CAREFUL DESIGN:
  MPC without terminal conditions can be unstable (finite horizon ≠ infinite horizon)

THEOREM (Mayne-Rawlings):
  MPC is asymptotically stable if:
  1. P = DARE solution: P = Q + AᵀPA - AᵀPB(R + BᵀPB)⁻¹BᵀPA
     (same P as infinite-horizon LQR — terminal cost = LQR cost-to-go)
  2. X_f = maximal positively invariant set under LQR control law
     i.e., X_f = {x : u_LQR(x) = -Kx ∈ U and Ax + Bu_LQR(x) ∈ X ∩ X_f}
     Computed iteratively: X_f^0 = X, X_f^{i+1} = X_f^i ∩ Pre(X_f^i) until convergence
  3. N large enough that x₀ feasible → x_N ∈ X_f achievable

PROOF IDEA:
  V(x_t) = J*(x_t)  (optimal MPC cost) is a Lyapunov function
  V(x_{t+1}) ≤ V(x_t) - x_tᵀQx_t  (by shifting optimal sequence)
  V is bounded below by 0, decreasing → converges to 0
  (LaSalle: {x : V̇ = 0} = {0} → origin is AS)

INFINITE-HORIZON EQUIVALENCE:
  If N ≥ n + m (prediction horizon ≥ system order + some buffer)
  and terminal conditions above hold: MPC recovers infinite-horizon LQR performance
  → MPC = LQR but with constraints handled explicitly
```

---

## QP Solver: From OCP to Optimization

### Condensed Formulation

```
CONDENSED FORM: eliminate state variables, optimize only over U = [u₀,...,u_{N-1}]

x₁ = Ax₀ + Bu₀
x₂ = A²x₀ + ABu₀ + Bu₁
...
x_N = Aᴺx₀ + [Aᴺ⁻¹B ... AB  B] · U
       └── constant ──┘ └────── Φ ──────┘

BATCH QP:
  J = Uᵀ(ΦᵀQΦ + R̄)U + 2xₒᵀAᴺᵀQΦU + const
  subject to: GU ≤ h (stacked state + input constraints)

  → Standard QP: min ½Uᵀ H U + fᵀU  s.t. GU ≤ h

COMPLEXITY: QP has Nu·N variables, 2(Nx + Nu)·N constraints
  Horizon N = 20, states Nx = 10, inputs Nu = 3 → 60 variables, ~1300 constraints
  Modern QP solvers (OSQP, qpOASES): solve in microseconds to milliseconds
```

### Sparse Formulation

```
SPARSE FORM: keep both x and u as decision variables

  Decision vector: [x₀, u₀, x₁, u₁, ..., x_N]

  ADVANTAGES of sparse over condensed:
  + Scales better with N (condensed: Hessian is (Nm)² dense; sparse: stays banded)
  + Better numerical conditioning (condensed: condition number grows as N²)
  + Natural for warm-starting: previous solution shifts one step

  SPARSE SOLVERS: FORCES Pro, HPIPM, osqp-MPC
  CONDENSED SOLVERS: qpOASES (fast for small N), OSQP (condensed or sparse)

  TRADEOFF: Condensed wins for short horizons (N ≤ 20) and few states
            Sparse wins for long horizons (N > 50) or large state dimension
```

---

## Nonlinear MPC (NMPC)

### Full Formulation

```
NONLINEAR OCP:
  min_{u(·)}  ∫₀ᵀ l(x(t), u(t)) dt + V_f(x(T))
  subject to:  ẋ = f(x, u)   (nonlinear ODE)
               g(x, u) ≤ 0   (path constraints)
               h(x_f, T) = 0 (terminal constraints)

DIRECT METHODS (transcribe ODE → NLP):
  1. MULTIPLE SHOOTING: discretize time into intervals, constrain continuity
     Decision variables: x₀, u₀, x₁, u₁, ..., x_N, u_{N-1}, (x₁_actual,...)
     NLP constraints: x_{k+1} = F_k(x_k, u_k)  (simulation of ODE over interval)
     NLP solver: IPOPT (interior point), SNOPT

  2. DIRECT COLLOCATION: parameterize x(t) as polynomial between nodes
     Derivatives = collocation conditions (not ODE integration)
     Denser NLP but often faster convergence

  CASADI + IPOPT: standard open-source NMPC toolkit
    opti = ca.Opti()
    X = opti.variable(nx, N+1)    # state trajectory
    U = opti.variable(nu, N)      # control trajectory
    opti.minimize(sum_cost)
    opti.subject_to(dynamics_constraints)
    opti.subject_to(X[:, 0] == x0)
    sol = opti.solve()
```

### Real-Time Iteration (RTI)

```
CHALLENGE: Full NLP solve at each timestep may be too slow for fast systems

RTI (Diehl, 2001): Single SQP iteration per timestep instead of full convergence

STANDARD SQP:
  Linearize NLP around current iterate → solve QP → update → repeat until converge

RTI:
  At time t: start from previous (shifted) solution
  Do exactly 1 SQP step (prepare phase + feedback phase)
  → Suboptimal but feasible, stability preserved if initial solution good

PREPARATION/FEEDBACK SPLIT:
  Preparation: build Jacobians, Hessian (can be done during sampling period)
  Feedback: solve condensed QP with new measurement x(t) → milliseconds

  Preparation (expensive): run during previous control period
  Feedback (cheap, <1ms): use new state measurement to get u₀

WHEN TO USE RTI:
  Fast dynamics (T_s ≤ 100ms), NMPC with moderate N (≤ 20)
  ACADO toolkit implements RTI; also in acados
```

---

## Explicit MPC

```
PRECOMPUTE OPTIMAL CONTROL LAW OFFLINE:

For linear MPC with polytopic constraints, the optimal control law is
piecewise affine (PWA) on polytopic regions of the state space:

  u*(x) = Fᵢx + gᵢ  for x ∈ Rᵢ   (polyhedral region)

APPROACH:
  1. Solve parametric QP off-line (via multi-parametric programming)
  2. Get: {Rᵢ, Fᵢ, gᵢ} — lookup table of regions and control laws
  3. Online: binary search tree to find which region x falls in → evaluate Fᵢx + gᵢ

ADVANTAGES:
  Online computation: O(log n_regions) — microseconds even on simple processors
  No QP solver needed at runtime → suitable for embedded automotive/aerospace

LIMITATIONS:
  Number of regions grows exponentially with state dimension (curse of dimensionality)
  Practical for: n_x ≤ 5-6, N ≤ 10, few constraints
  Larger systems: storage and search become infeasible

  TOOLS: MPT3 toolbox (MATLAB), pyMPC
```

---

## Applications

```
┌──────────────────────────────────────────────────────────────────────┐
│ APPLICATION          │ STATE VARS        │ CONSTRAINTS               │
├──────────────────────┼───────────────────┼───────────────────────────┤
│ Distillation column  │ Temperatures,     │ Feed rates, product specs,│
│ (chemical plant)     │ compositions      │ valve limits              │
├──────────────────────┼───────────────────┼───────────────────────────┤
│ HVAC optimization    │ Zone temps,       │ Comfort bounds, max power │
│                      │ humidity, CO₂     │ draw, rate limits         │
├──────────────────────┼───────────────────┼───────────────────────────┤
│ Autonomous vehicle   │ Position, heading,│ Road boundaries, accel/  │
│ trajectory planning  │ velocity          │ decel limits, obstacle    │
│                      │                   │ avoidance (soft or hard)  │
├──────────────────────┼───────────────────┼───────────────────────────┤
│ Batch reactor        │ Temperature,      │ Maximum temperature, pH   │
│ control              │ concentration     │ range, feed rate limits   │
├──────────────────────┼───────────────────┼───────────────────────────┤
│ Power grid           │ Frequency,        │ Generator ramp rates,     │
│ economic dispatch    │ voltage, SOC      │ line flow limits, storage │
├──────────────────────┼───────────────────┼───────────────────────────┤
│ Aircraft GLA         │ Wing bending,     │ Control surface rates,    │
│ (gust load alleviate)│ accelerations     │ structural load limits    │
└──────────────────────┴───────────────────┴───────────────────────────┘
```

---

## MPC as PID + Constraints + Preview

```
CONCEPTUAL BRIDGE (for engineers familiar with PID):

PID:  u(t) = Kp·e(t) + Ki∫e(t)dt + Kd·ė(t)
  - Reacts to current + past error
  - Tuned for typical disturbances
  - No explicit constraint handling (anti-windup patches this partially)

MPC:  u(t) = argmin future cost subject to constraints
  - Optimizes over horizon (looks ahead)
  - Explicitly handles saturation, rate limits, safety constraints
  - Degrades gracefully: when far from constraints, behaves like LQR
  - Near constraints: modifies control to stay feasible

WHEN MPC OVER PID:
  + Multiple interacting loops (multivariable plant)
  + Hard constraints that cannot be saturated away
  + Economic objective mixed with control (maximize yield, minimize energy)
  + Preview information available (vehicle trajectory, weather forecast for HVAC)

WHEN PID OVER MPC:
  + Simple SISO loop, constraints rarely active
  + Embedded system without computational budget for QP
  + Real-time requirement < 1ms (though explicit MPC bridges this)
  + Operator needs simple tuning handles
```

---

## Decision Cheat Sheet

```
┌──────────────────────────────────────────────────────────────────────┐
│ SCENARIO                     │ RECOMMENDATION                       │
├──────────────────────────────┼───────────────────────────────────────┤
│ Linear plant, hard           │ Linear MPC with condensed QP;        │
│ constraints, T_s > 10ms      │ OSQP or qpOASES; terminal cost/set  │
├──────────────────────────────┼───────────────────────────────────────┤
│ Nonlinear dynamics,          │ NMPC with multiple shooting +        │
│ T_s > 100ms                  │ IPOPT; CasADi for automatic diff.   │
├──────────────────────────────┼───────────────────────────────────────┤
│ Nonlinear, fast dynamics     │ RTI-NMPC (single SQP iteration);    │
│ (T_s < 100ms)                │ acados or ACADO toolkit              │
├──────────────────────────────┼───────────────────────────────────────┤
│ Embedded, no QP solver,      │ Explicit MPC (MPT3 offline);        │
│ simple system (n_x ≤ 5)      │ PWA lookup at runtime                │
├──────────────────────────────┼───────────────────────────────────────┤
│ Economic objective           │ Economic MPC: replace quadratic cost │
│ (maximize yield, etc.)       │ with economic objective; stability   │
│                              │ via dissipativity theory             │
├──────────────────────────────┼───────────────────────────────────────┤
│ Stability guarantee needed   │ Terminal cost P = DARE, terminal set │
│                              │ X_f = max positively invariant set   │
│                              │ under LQR; verify N sufficient       │
└──────────────────────────────┴───────────────────────────────────────┘
```

---

## Common Confusion Points

**Feasibility ≠ stability in MPC.** A controller can be feasible at every step (always find a solution) yet be unstable (state grows unboundedly). Terminal conditions (terminal cost P, terminal set X_f) are what provide the stability guarantee, not just feasibility.

**Increasing N always helps stability (for large enough N) but doesn't help feasibility.** A longer horizon gives more slack to satisfy terminal constraints, improving stability. But if the initial state is too far from the feasible region, no N helps. The choice of N trades off computation vs stability robustness.

**Soft constraints can make your "MPC" crash the system.** If you soften all constraints for feasibility, the system may violate safety constraints (hard) to improve performance objectives. Hard constraints must remain hard for safety-critical applications; soft constraints are for performance limits.

**NMPC with RTI is not the same as running LQR.** RTI gives a suboptimal solution (one SQP step, not full convergence). It provides stability guarantees only under specific conditions on the quality of the initial guess and the contraction properties of the NLP. Don't assume RTI stability without checking the theory.

**The condensed form Hessian is full (dense).** Even if A, B are sparse, the batch Hessian Φᵀ(Q⊗I)Φ + R̄ is dense because the input propagates through N steps. For long horizons with large state dimensions, the sparse formulation is far more efficient and numerically better conditioned.

**MPC is not a panacea for constraints.** MPC optimally handles constraints in the prediction horizon, but it relies on an accurate model. Model mismatch causes constraint violations in practice. Robust MPC (tube MPC, min-max MPC) provides constraint satisfaction guarantees under bounded model error — at the cost of more conservative control and higher computational load.
