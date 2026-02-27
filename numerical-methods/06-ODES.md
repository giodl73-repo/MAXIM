# Ordinary Differential Equations

## The Big Picture

ODE solvers advance a system state forward in time. The key challenges: accuracy (order of method), efficiency (step size control), and stiffness (fast vs. slow dynamics requiring different methods).

```
+------------------------------------------------------------------+
|                    ODE SOLVER TAXONOMY                           |
+------------------------------------------------------------------+
|                                                                  |
|  PROBLEM: y' = f(t, y),  y(t_0) = y_0                          |
|                                                                  |
|  NON-STIFF                         STIFF                        |
|  (time scales similar)             (fast + slow scales mixed)   |
|  +---------------------+           +-------------------+        |
|  | Runge-Kutta family  |           | BDF methods       |        |
|  | RK4: O(h^4)         |           | (VODE, LSODE)     |        |
|  | Dormand-Prince (RK45)|          | Rosenbrock        |        |
|  | Adaptive step size  |           | Implicit RK       |        |
|  +---------------------+           +-------------------+        |
|                                                                  |
|  BOUNDARY VALUE PROBLEMS           DIFFERENTIAL-ALGEBRAIC       |
|  +---------------------+           +-------------------+        |
|  | Shooting method     |           | DAE solvers       |        |
|  | Collocation         |           | Index reduction   |        |
|  | BVP4C (MATLAB/scipy)|           +-------------------+        |
|  +---------------------+                                        |
+------------------------------------------------------------------+
```

---

## Euler's Method and Basic Analysis

**Euler's method** (simplest explicit method):

```
  y_{n+1} = y_n + h f(t_n, y_n)

  Derivation: Taylor expand y(t+h) = y(t) + h y'(t) + O(h^2) = y(t) + h f(t, y(t)) + O(h^2)

  LOCAL TRUNCATION ERROR: e_{n+1} = y(t_{n+1}) - y_{n+1} = h^2/2 * y''(xi) = O(h^2)
  (error at one step, assuming y_n is exact)

  GLOBAL ERROR: sum over n = T/h steps:
  E(T) = O(T/h * h^2) = O(h)   (first-order method)

  Halving h: halves the global error, doubles the work.
  For 10^{-6} accuracy: h ~ 10^{-6} -> O(10^6) steps.
  RK4: h ~ 10^{-2} -> O(100) steps. Huge difference.

  STABILITY: For y' = lambda y (test equation, lambda complex):
  y_{n+1} = (1 + h lambda) y_n
  Stability requires |1 + h lambda| <= 1.
  For lambda = -1/tau (stable physical system):
  Requires h <= 2 tau  (step size bounded by time constant of the ODE)
```

---

## Runge-Kutta Methods

Runge-Kutta methods evaluate f at multiple intermediate points within each step to achieve higher accuracy without storing history.

**Classical RK4**:

```
  k_1 = f(t_n, y_n)
  k_2 = f(t_n + h/2, y_n + h k_1/2)
  k_3 = f(t_n + h/2, y_n + h k_2/2)
  k_4 = f(t_n + h,   y_n + h k_3)

  y_{n+1} = y_n + h (k_1 + 2k_2 + 2k_3 + k_4) / 6

  ORDER: 4 (local error O(h^5), global error O(h^4))
  COST: 4 function evaluations per step
  STABILITY: Stability region includes part of negative real axis (up to h*|lambda| <= 2.8)

  "RK4 is the workhorse of ODE solvers" -- 4th-order accuracy with 4 evaluations.
  Named after Runge (1895) and Kutta (1901).
```

**Dormand-Prince (RK45) with step-size control**:

```
  Uses 6 stages (function evaluations):
  - Computes a 4th-order estimate y^{(4)} and 5th-order estimate y^{(5)}.
  - Error estimate: ||y^{(5)} - y^{(4)}|| (embedded error estimate)
  - If error < tolerance: accept step, try larger h next.
  - If error >= tolerance: reject step, reduce h.

  Step size control rule:
  h_new = h_old * (tol / error)^{1/5}  (proportional control)
  Or with PI control for better performance:
  h_new = h_old * (tol / error)^{alpha} * (error_prev / error)^{beta}

  This is RK45 in scipy.integrate.solve_ivp, ode45 in MATLAB.
  Default for non-stiff problems. 6 function evaluations per step (one free via FSAL).
```

**General Runge-Kutta structure** (Butcher tableau):

```
  BUTCHER TABLEAU:
  c | A    (A = Runge-Kutta matrix, c = nodes, b = weights)
  --|---
    | b^T

  Stage values: k_i = f(t_n + c_i h, y_n + h Sum_j a_{ij} k_j)
  Step:         y_{n+1} = y_n + h Sum_i b_i k_i

  EXPLICIT: A is strictly lower triangular (a_{ij} = 0 for j >= i).
  IMPLICIT: A has nonzero upper entries -> solve nonlinear system at each step.
  DIAGONALLY IMPLICIT (DIRK): A is lower triangular (a_{ii} != 0).
    Each stage: scalar or small nonlinear solve.

  IMPLICIT METHODS ARE REQUIRED FOR STIFF PROBLEMS.
```

---

## Stiffness

**Stiff ODEs** have components that evolve on vastly different time scales:

```
  EXAMPLE: Robertson's chemical kinetics
  y1' = -0.04 y1 + 10^4 y2 y3
  y2' = 0.04 y1 - 10^4 y2 y3 - 3*10^7 y2^2
  y3' = 3*10^7 y2^2

  Time scales: fast (y2, time scale ~10^{-7}) and slow (y1, y3, time scale ~10^3).
  Stiffness ratio: 10^10.

  With explicit RK4: stability requires h <= time_scale_fast = 10^{-7}.
  Total time T = 10^{11} steps. INFEASIBLE.

  With an implicit stiff solver: h can be O(slow_time_scale) = O(10^3).
  ~10^8 steps. Feasible.
```

**Stiffness ratio**: lambda_max / lambda_min of the Jacobian J = df/dy.

```
  DETECTING STIFFNESS:
  - Explicit solver repeatedly rejects steps or takes very small steps.
  - Stiffness ratio >> 1.
  - Behavior: fast transient quickly dies, then slow dynamics remain.

  STIFF SOLVERS:
  Use stability regions that include large portions of the negative real axis.
  A-stable: entire left half-plane is stable (ideal for stiff problems).
  L-stable: A-stable + stability -> 0 as |lambda*h| -> inf.
```

---

## BDF Methods (Backward Differentiation Formula)

BDF methods are implicit linear multistep methods, standard for stiff problems:

```
  BDF-1 (implicit Euler):
  y_{n+1} = y_n + h f(t_{n+1}, y_{n+1})
  Solve nonlinear: g(y_{n+1}) = y_{n+1} - y_n - h f(t_{n+1}, y_{n+1}) = 0
  Using Newton's method: J g delta = -g(y), y <- y + delta.
  STABILITY: A-stable, L-stable.

  BDF-2:
  y_{n+1} = (4/3) y_n - (1/3) y_{n-1} + (2/3) h f(t_{n+1}, y_{n+1})
  A-stable for orders 1-2. Conditionally A-stable for orders 3-6.

  GENERAL BDF-k (k = 1,...,6):
  Linear combination of k past values + implicit evaluation at t_{n+1}.
  Requires k starting values (use Runge-Kutta to start).
  Orders 1-2: A-stable. Orders 3-6: A(alpha)-stable (stable in a cone of the left half-plane).

  SCIPY: solve_ivp with method='Radau' or method='BDF'.
  MATLAB: ode15s (variable-order BDF), ode23s (Rosenbrock), ode23t (trapezoidal).
```

**Jacobian computation via automatic differentiation.** BDF and Rosenbrock methods need the Jacobian J = df/dy at each step. Three approaches:

```
  METHOD                  COST              ACCURACY
  ──────────────────────────────────────────────────────────────────────
  Finite differences      O(n) evaluations  O(√eps_mach) — truncation vs. roundoff
  Forward-mode AD         O(n) forward      Machine-precision exact
    (dual numbers)          passes           One pass per column of J
  Reverse-mode AD         O(n) backward     Machine-precision exact
    (backprop)              passes           One pass per row of J
  Sparse Jacobian +       O(p) passes       Exact, where p = graph coloring number
    coloring (AD)           (p << n)          of the sparsity pattern
```

For stiff ODE systems from PDE semi-discretization (n = 10^4–10^6), J is sparse with known sparsity pattern. Graph coloring of the sparsity pattern reduces the cost from O(n) AD passes to O(p) where p is the chromatic number of the column intersection graph — typically p = 5–10 for structured meshes. This is what DifferentialEquations.jl (SparseDiffTools.jl) and SUNDIALS use in practice. Forward-mode AD via dual numbers (ForwardDiff.jl, `jax.jacfwd`) is the standard choice because J is square and typically has more rows than needed output dimensions per pass.

**Newton's method for the implicit solve** (at each BDF step):

```
  Must solve: F(y_{n+1}) = 0  (nonlinear algebraic equation)
  Newton step: J_F delta = -F(y_{n+1})  where J_F = I - h beta J_f
  (J_f = Jacobian of f, J_F = Jacobian of the algebraic equation)

  This requires the Jacobian of f (or a finite-difference approximation).
  Cost: one LU factorization of J_F per Newton step.
  LU is REUSED across multiple Newton iterations (if J_F doesn't change much).
  Modern BDF codes: lazy Jacobian evaluation, reuse LU many times.
```

---

## Rosenbrock Methods

For mildly stiff problems: Rosenbrock methods are explicit schemes equivalent to one Newton step of implicit Euler (linearized at the start of the step):

```
  ROSENBROCK-WANNER 3(2):
  k1: (I - h gamma J) k1 = h f(t_n, y_n)
  k2: (I - h gamma J) k2 = h f(t_n + a21 h, y_n + a21 h k1) + c21 k1
  y_{n+1} = y_n + m1 k1 + m2 k2
  Error estimate: y_{n+1} - y_est = e1 k1 + e2 k2

  COST: One LU factorization per step (vs. multiple for Newton-based BDF).
  ORDER: 3rd order accuracy.
  A-stable: entire left half-plane stable.
  GOOD FOR: moderately stiff problems, cheap Jacobian computation.

  scipy: solve_ivp method='Radau' (implicit Runge-Kutta, higher accuracy for stiff)
  MATLAB: ode23s
```

---

## Boundary Value Problems

Initial value problems (IVPs): initial state known, integrate forward.
Boundary value problems (BVPs): conditions specified at BOTH ends of the interval.

```
  EXAMPLE: y'' = f(x, y, y'), y(0) = alpha, y(L) = beta.

  SHOOTING METHOD:
  1. Guess missing initial condition: y'(0) = s (unknown)
  2. Solve IVP with y(0) = alpha, y'(0) = s.
  3. Check: y(L) = beta?
  4. Adjust s using Newton's method: ds = (y_L(s+ds) - y_L(s)) / ds
  5. Converge to s* such that y(L) = beta.

  ADVANTAGES: Uses powerful IVP solvers.
  DISADVANTAGES: May be unstable for strongly growing solutions.
  Multiple shooting: divide interval, apply shooting on each subinterval.

  COLLOCATION (bvp4c/bvp5c in MATLAB, solve_bvp in scipy):
  Approximate solution by piecewise polynomial in space and time.
  Choose polynomial coefficients to satisfy ODE at "collocation points."
  Results in a large algebraic system (sparse banded).
  More stable than shooting for difficult problems.
```

---

## Differential-Algebraic Equations (DAEs)

DAEs mix differential equations and algebraic constraints:

```
  EXAMPLE: Index-1 DAE
  y1' = f1(t, y1, y2)    (differential equation)
  0 = g(t, y1, y2)       (algebraic constraint)

  Used in: circuit simulation (Kirchhoff laws), mechanical systems (constraints),
  chemical process simulation (stoichiometry).

  INDEX: Number of times you need to differentiate the constraints to convert to ODE.
  Index 1: well-conditioned (standard DAE solvers handle this)
  Index 2: mechanical systems with velocity constraints
  Index 3: mechanical systems with position constraints (very stiff)
  Index > 1: often requires index reduction before numerical solution.

  SOLVERS: DASSL, SUNDIALS/IDA, MATLAB ode15i.
```

---

## Symplectic Integrators (Hamiltonian Systems)

For Hamiltonian systems (energy-conserving dynamics), standard Runge-Kutta methods drift in energy over long integrations. Symplectic integrators preserve the geometric structure of phase space.

```
  HAMILTONIAN SYSTEM:
  q' = ∂H/∂p    (position evolution)
  p' = -∂H/∂q   (momentum evolution)
  H(q, p) = T(p) + V(q)   (kinetic + potential energy)

  STÖRMER-VERLET (LEAPFROG) — the standard symplectic method:
  p_{n+1/2} = p_n - (h/2) ∂V/∂q(q_n)            (half-step momentum)
  q_{n+1}   = q_n + h ∂T/∂p(p_{n+1/2})           (full-step position)
  p_{n+1}   = p_{n+1/2} - (h/2) ∂V/∂q(q_{n+1})   (half-step momentum)

  ORDER: 2nd (local error O(h^3), global error O(h^2))
  COST: 1 force evaluation per step (same as explicit Euler!)

  WHY SYMPLECTIC?
  Symplecticity = area-preserving map in (q,p) phase space.
  Consequence: energy oscillates but does NOT drift. Over 10^9 steps:
    RK4:     energy drift grows linearly (error accumulates)
    Verlet:  energy bounded within O(h^2) of true energy (no drift)

  This is NOT conservation of energy — it is conservation of a
  "shadow Hamiltonian" H_tilde = H + O(h^2), which stays close to H.
  For solar system simulations, molecular dynamics, and any long-time
  integration where energy drift is catastrophic, symplectic wins.

  HIGHER-ORDER SYMPLECTIC:
  Yoshida composition: combine Verlet steps with different dt to get
  4th, 6th, 8th order symplectic integrators.
  Cost: 3 force evaluations for 4th order (vs. 4 for RK4).
```

When to use symplectic vs. standard RK: if the system is Hamiltonian and the integration is long-time (10^3+ periods), symplectic integrators are essential. For short-time or dissipative systems, standard RK45 is fine — energy conservation is not the constraint.

---

## Decision Cheat Sheet

| Problem Type | Method | Notes |
|---|---|---|
| Non-stiff, smooth | Dormand-Prince (RK45) | Default choice |
| Non-stiff, high accuracy | Runge-Kutta-Fehlberg 7(8) | More evaluations, better accuracy |
| Stiff, general | BDF (scipy Radau or BDF) | Implicit, adaptive order |
| Mildly stiff | Rosenbrock (ode23s) | Cheaper than full implicit |
| Very stiff, tight accuracy | Gauss-Legendre IRK | A-stable, high-order |
| Conservative system (Hamiltonian) | Symplectic integrator (Verlet, Leapfrog) | Preserves energy long-term |
| BVP, well-behaved | Collocation (bvp4c) | Reliable, mesh-adaptive |
| BVP, shooting OK | Shooting + Newton | Simple, fast if stable |
| DAE index 1 | IDA / DASSL | State-of-art |

---

## Common Confusion Points

**"RK4 is 4th order, so it is very accurate."**
Order 4 means global error O(h^4). For h=0.1: error ~10^{-4} per unit time. For h=0.01: error ~10^{-8}. The accuracy depends on h AND the smoothness of f. If f has a discontinuity, the error loses its high-order property near the discontinuity.

**"Stiff solvers are slower per step, so they should only be used when necessary."**
Stiff solvers ARE slower per step (they require a Jacobian and linear solves). But for stiff problems, explicit solvers take enormously many steps just for stability. For stiffness ratio 10^8, an implicit solver might use 1000 steps while an explicit solver would need 10^{11} steps. The implicit solver wins by 8 orders of magnitude in total work.

**"An implicit solver always converges."**
Implicit solvers require solving a nonlinear system at each step using Newton's method. Newton's method can fail if: (1) initial guess (the explicit predictor) is too far from the solution, (2) the Jacobian is singular, or (3) the step size is too large. Adaptive codes handle this by reducing h when Newton fails.

**"The shooting method is unstable."**
Simple shooting can be unstable for problems with exponentially growing solutions (the boundary condition is sensitive to initial perturbations). Multiple shooting on subintervals is stable. Collocation avoids the issue entirely by directly discretizing the solution, making it robust for a broader class of BVPs.
