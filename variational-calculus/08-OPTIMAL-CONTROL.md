# Optimal Control and Pontryagin Principle

## The Big Picture

Optimal control is variational calculus with a control input that can be constrained to a
set. The Euler-Lagrange approach doesn't work directly when the control is constrained —
the **Pontryagin Maximum Principle** (PMP) replaces it.

```
+-----------------------------------------------------------------------+
|              OPTIMAL CONTROL LANDSCAPE                                 |
|                                                                       |
|  VARIATIONAL CALCULUS:        OPTIMAL CONTROL:                        |
|  u(t) unconstrained           control u(t) ∈ U (constrained set)    |
|  Euler-Lagrange sufficient    Pontryagin MP necessary                 |
|  Smooth solutions             Possibly bang-bang solutions            |
|  No state constraints         State constraints allowed               |
|                                                                       |
|  PROBLEM: minimize J = ∫₀ᵀ L(x,u,t) dt + Ψ(x(T))                   |
|           subject to: ẋ = f(x, u, t)  (dynamics)                    |
|                        x(0) = x₀       (initial state)               |
|                        u(t) ∈ U         (control constraint)          |
|                                                                       |
|  x = state,  u = control,  L = running cost,  Ψ = terminal cost     |
|                                                                       |
|  APPLICATIONS:                                                        |
|  Aerospace: minimum fuel / time trajectories                          |
|  Robotics: minimum energy / time motion planning                      |
|  Economics: optimal capital accumulation (Ramsey model)               |
|  Neural ODEs: optimal depth in continuous networks                    |
|  RL: continuous-time limit of reinforcement learning                  |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## From Calculus of Variations to Optimal Control

The transition arises when the control is constrained:

```
  UNCONSTRAINED: minimize J[u] = ∫₀ᵀ F(t, x, ẋ) dt
  subject to: ẋ = f(x, u), which forces f(x,u) = ẋ.

  If u is FREE (no constraint U), this is standard variational calculus.
  E-L equation gives:  ∂F/∂x − d/dt(∂F/∂ẋ) = 0.

  CONSTRAINED: u(t) ∈ U ⊂ R^m (e.g., U = [−1, 1]^m)
  The function u(t) may be forced to a boundary of U.
  E-L equation requires δJ = 0 for all variations — but variations
  can't point INTO U if u is already on the boundary.
  → Interior condition E-L FAILS on boundary of U.
  → Need: Pontryagin's Maximum Principle.
```

---

## Pontryagin Maximum Principle (PMP)

Lev Pontryagin (1956) — one of the major results of 20th-century mathematics.

```
  PROBLEM:
  Minimize: J[u] = ∫₀ᵀ L(x(t), u(t), t) dt + Ψ(x(T))
  Subject to: ẋ(t) = f(x(t), u(t), t),  x(0) = x₀,  u(t) ∈ U

  HAMILTONIAN (control theory — different from mechanics!):
  H(x, p, u, t) = p · f(x, u, t) − L(x, u, t)

  (p is the costate or adjoint variable — analogous to momentum)

  PONTRYAGIN MAXIMUM PRINCIPLE:
  ┌──────────────────────────────────────────────────────────────────┐
  │ If u*(t) is optimal, then there exists costate p(t) such that:  │
  │                                                                  │
  │ 1. STATE EQUATION:  ẋ* = ∂H/∂p = f(x*, u*, t)                 │
  │                                                                  │
  │ 2. COSTATE EQUATION: ṗ = −∂H/∂x = ∂L/∂x − p·∂f/∂x            │
  │    (backward ODE! — integrated from T to 0)                     │
  │    Transversality: p(T) = −∂Ψ/∂x(T) (terminal condition for p)│
  │                                                                  │
  │ 3. MAXIMUM CONDITION:                                           │
  │    H(x*(t), p(t), u*(t), t) = max_{u ∈ U} H(x*(t), p(t), u, t)│
  │    The optimal control MAXIMIZES the Hamiltonian at each t.     │
  └──────────────────────────────────────────────────────────────────┘

  KEY DIFFERENCE from E-L:
  E-L: δH/δu = 0 (unconstrained stationarity)
  PMP: max over U (constrained maximum — may be on boundary of U)
```

---

## Bang-Bang Control

When the control constraint is active, solutions are typically at the boundary:

```
  LINEAR CONTROL: f(x,u) = A(t)x + B(t)u,  u ∈ [−1, 1]^m

  H = p·(A(t)x + B(t)u) − L
  ∂H/∂u = pᵀB(t)  (switching function)

  MAXIMUM of H over u ∈ [−1,1]^m:
  u*_i(t) = sign(ψᵢ(t))  where ψ(t) = B(t)ᵀp(t)

  This is BANG-BANG CONTROL: u switches between −1 and +1.
  Each component of u is either at its maximum or minimum value.

  SWITCHING SURFACE: where ψᵢ(t) = 0.
  The control switches when the switching function changes sign.

  EXAMPLE: Minimum time to stop a car.
  ẋ₁ = x₂ (position), ẋ₂ = u (velocity, u ∈ [−1,1])
  Minimize time T subject to x(T) = 0.

  Optimal: full brake u=−1 then full acceleration? NO.
  Optimal: full acceleration u=+1 to some point, then full brake u=−1.
  BANG-BANG with ONE switch. The switching curve is a parabola.
```

---

## Bellman's Principle and HJB Equation

An alternative approach: dynamic programming.

```
  BELLMAN'S PRINCIPLE OF OPTIMALITY (1957):
  An optimal control, for any sub-interval [t,T], is optimal for
  the remaining problem starting at (x(t), t).

  "Whatever the initial state and initial decision are, the remaining
  decisions must constitute an optimal policy with regard to the state
  resulting from the first decision."

  VALUE FUNCTION:
  V(x, t) = min_{u(·)} ∫_t^T L(x,u,s) ds + Ψ(x(T))
  (minimum cost to go from state x at time t)

  HAMILTON-JACOBI-BELLMAN (HJB) EQUATION:
  ┌────────────────────────────────────────────────────────────────┐
  │  −∂V/∂t = min_{u ∈ U} [L(x,u,t) + ∇V · f(x,u,t)]           │
  │  = min_{u ∈ U} [L(x,u,t) + ∇_x V · f(x,u,t)]               │
  │  Terminal condition: V(x,T) = Ψ(x)                           │
  └────────────────────────────────────────────────────────────────┘

  HJB is a NONLINEAR PDE for V(x,t) (Hamilton-Jacobi type).
  Once V is known: optimal control u*(x,t) = argmin_{u∈U}[L + ∇V·f]

  RELATIONSHIP TO PMP:
  If V is smooth: ∇_x V(x*(t), t) = −p(t)  (costate = gradient of value function)
  V satisfies HJB ↔ PMP conditions satisfied along optimal trajectory.
  HJB gives the global solution; PMP gives the local (trajectory) conditions.

  VISCOSITY SOLUTIONS:
  HJB is typically non-smooth (optimal control often bang-bang).
  Crandall-Lions (1983) viscosity solution theory handles non-smooth V.
```

---

## Linear Quadratic Regulator (LQR)

The most important special case — admits a closed-form solution:

```
  LQR PROBLEM:
  Minimize J = ∫₀ᵀ [xᵀQx + uᵀRu] dt + xᵀ(T) P_T x(T)
  Subject to: ẋ = Ax + Bu,   x(0) = x₀
  (Q ≥ 0, R > 0, P_T ≥ 0 symmetric matrices)

  U = R^m (unconstrained!) → PMP gives interior condition.

  COSTATE EQUATION:  ṗ = −Qx − Aᵀp
  OPTIMALITY:  Ru + Bᵀp = 0  →  u* = −R⁻¹Bᵀp

  ASSUME p(t) = −P(t)x(t)  (Riccati ansatz):
  ṗ = −Ṗx − Pẋ = −Qx − Aᵀp = −Qx + AᵀPx
  −(Ṗx + P(Ax + Bu)) = −Qx + AᵀPx
  Substituting u* = R⁻¹Bᵀ P x:

  RICCATI EQUATION:
  −Ṗ = Aᵀ P + PA − PBR⁻¹Bᵀ P + Q
  P(T) = P_T

  OPTIMAL CONTROL:  u*(t) = −K(t) x(t)  where K(t) = R⁻¹Bᵀ P(t)
  LINEAR FEEDBACK CONTROL.

  INFINITE HORIZON (T→∞, stabilizing P):
  P satisfies ALGEBRAIC RICCATI EQUATION:
  Aᵀ P + PA − PBR⁻¹Bᵀ P + Q = 0
  K = R⁻¹Bᵀ P = constant feedback gain matrix.
  Standard feedback controller for linear systems.

  BRIDGE TO AZURE/VSTS: LQR is the foundation of model-predictive control
  (MPC) used in real-time manufacturing, cloud resource allocation, etc.
```

---

## Minimum Principle vs. Maximum Principle

```
  NOTE ON SIGN CONVENTIONS:
  Pontryagin's original formulation: MAXIMUM principle.
  H = pᵀf − L (cost function L is subtracted).
  Maximize H over u ∈ U.

  ALTERNATIVE: MINIMUM principle.
  H = pᵀf + L (cost function L is added).
  Minimize H over u ∈ U.

  Both are equivalent; sign depends on convention for costate.

  MNEMONIC:
  "We want to minimize cost J. We maximize the Hamiltonian H."
  The optimal control maximizes H at each time instant.
  Intuitively: p encodes the value of the state, and H = p·ẋ − L
  is the rate of value accumulation minus cost.
```

---

## Adjoint Method: Gradient via PMP

The adjoint (costate) equation provides efficient gradient computation:

```
  GRADIENT OF J w.r.t. PARAMETERS θ in ẋ = f(x, u, θ):

  NAIVE: finite difference — perturb θ by ε, rerun simulation.
  Cost: O(dim(θ)) × simulation cost.

  ADJOINT METHOD:
  1. Forward pass: integrate ẋ = f(x, u, θ), store x(t).
  2. Backward pass: integrate costate equation backward:
     ṗ = −(∂f/∂x)ᵀ p − ∂L/∂x,   p(T) = ∂Ψ/∂x(T)
  3. Gradient: dJ/dθ = ∫₀ᵀ pᵀ ∂f/∂θ dt

  Cost: ONE forward + ONE backward pass, regardless of dim(θ).
  O(1) × simulation cost.

  THIS IS EXACTLY BACKPROPAGATION IN CONTINUOUS TIME.

  NEURAL ODE (Chen et al. 2018):
  Parameterize the ODE by a neural network: f(x,t;θ) = NN_θ(x,t).
  Training = compute dJ/dθ via adjoint method.
  The adjoint equation is the continuous-time version of backprop through
  time (BPTT) in recurrent neural networks.
```

---

## Time-Optimal Control

The minimum-time problem:

```
  MINIMUM TIME from x₀ to target set X_f:
  Minimize T = ∫₀ᵀ 1 dt = T
  Subject to: ẋ = f(x,u), x(0) = x₀, x(T) ∈ X_f, u(t) ∈ U.

  This is the prototypical optimal control problem.

  PMP: H = p·f (L=1, but we absorb 1 into the Hamiltonian by redefining H)
  Maximum condition: u* = argmax_{u∈U} p·f(x,u)

  PONTRYAGIN'S THEOREM:
  For a controllable linear system ẋ = Ax + Bu, u ∈ U (convex, compact),
  the minimum-time control is BANG-BANG, switching between extremes of U.
  Moreover, the number of switches is ≤ n−1 (for generic problems, where n = dim x).

  The switching is determined by the sign of the switching function ψ(t) = pᵀB.
```

---

## Decision Cheat Sheet

| Problem type | Method |
|-------------|--------|
| Unconstrained control, smooth | Euler-Lagrange equation |
| Constrained control u ∈ U | Pontryagin Maximum Principle |
| Linear dynamics + quadratic cost | LQR → Riccati equation → linear feedback |
| Global optimal policy | HJB equation (backward PDE for value function) |
| Gradient of J w.r.t. parameters | Adjoint method (one backward pass) |
| Minimum time | Bang-bang control, switching from PMP |
| Neural ODE training | Adjoint method = continuous-time backprop |
| Stochastic control | HJB with Itô terms (stochastic optimal control) |

---

## Common Confusion Points

**"The control Hamiltonian H = p·f − L. Why subtract L instead of adding it?"**
By convention: we minimize J = ∫L dt, and we want to MAXIMIZE H. The sign ensures that
maximizing H is equivalent to minimizing cost. If you use the alternate convention (minimize
H = p·f + L), the costate equation has the opposite sign. The physics is the same; only
the sign convention differs.

**"PMP gives necessary conditions. How do I know the PMP solution is optimal?"**
For convex problems (convex U, linear f in u, convex L): PMP is also sufficient.
For general problems: PMP is only necessary. You need to check second-order conditions
or verify globally. In practice, if you have the HJB solution V(x,t), then u*(x,t) =
argmin[L + ∇V·f] gives the globally optimal control, and PMP conditions will be satisfied.

**"What's the relationship between the Pontryagin Hamiltonian and the physics Hamiltonian?"**
They look similar but are different. In optimal control: H(x,p,u) = p·f − L, where p is
the costate (Lagrange multiplier for the dynamics). In mechanics: H(q,p) = Σpᵢq̇ᵢ − L.
The structural similarity is not a coincidence — optimal control is a generalization of
mechanics where the Lagrangian is the cost, the dynamics constraint is the equation of
motion, and the costate is the momentum. The PMP is Hamilton's equations for this system.
