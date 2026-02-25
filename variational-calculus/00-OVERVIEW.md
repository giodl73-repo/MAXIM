# Variational Calculus — Landscape and Taxonomy

## The Big Picture

Variational calculus asks: among all functions satisfying given constraints, which one
**extremizes a given functional** (a real number assigned to each function)?

```
+-----------------------------------------------------------------------+
|              VARIATIONAL CALCULUS LANDSCAPE                            |
|                                                                       |
|  CENTRAL QUESTION:                                                    |
|  Minimize J[u] = ∫ₐᵇ F(x, u, u') dx   over all u with u(a)=A, u(b)=B│
|                                                                       |
|  ANSWER: the Euler-Lagrange equation                                  |
|  ∂F/∂u − d/dx(∂F/∂u') = 0                                            |
|                                                                       |
|  THIS IS DEEPER THAN NEWTON:                                          |
|  Newton's laws F = ma  ← derived from this via Lagrangian mechanics   |
|  Maxwell's equations    ← extremum of the electromagnetic action      |
|  Einstein's equations   ← extremum of the Einstein-Hilbert action     |
|  Schrödinger equation   ← extremum of the quantum action              |
|                                                                       |
|  CONNECTIONS TO MODERN COMPUTING:                                     |
|  Gradient descent = discrete variational optimization                  |
|  Neural ODEs = continuous-depth variational problem                    |
|  Optimal transport = variational problem over probability measures     |
|  Pontryagin maximum principle = constrained variational control        |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## The Core Problem

```
  FUNCTIONAL:  J: V → R  maps a function u to a real number.

  Examples:
  ┌────────────────────────────────────────────────────────────────┐
  │ BRACHISTOCHRONE: J[u] = ∫₀ᵃ √(1+u'²)/√(2gu) dx              │
  │   (time for bead to slide from (0,0) to (a,b) on curve y=u(x))│
  │                                                                │
  │ GEODESIC: J[u] = ∫₀ᵀ √(1+u'²) dx  (arc length)              │
  │   (shortest path between two points on a surface)             │
  │                                                                │
  │ LEAST ACTION: J[q] = ∫ₜ₁ᵗ² [½m|q̇|² − V(q)] dt              │
  │   (integral of kinetic minus potential energy)                 │
  │                                                                │
  │ DIRICHLET ENERGY: J[u] = ½ ∫_Ω |∇u|² dx                     │
  │   (a.k.a. harmonic energy; minimized by Laplace equation)     │
  │                                                                │
  │ OPTIMAL TRANSPORT: min over maps T: ∫ c(x,T(x)) dμ(x)       │
  │   (cheapest way to move mass from distribution μ to ν)        │
  └────────────────────────────────────────────────────────────────┘
```

---

## Historical Development

```
  1696 — BRACHISTOCHRONE PROBLEM (Bernoulli)
          Posed: find curve of fastest descent.
          Solved by: Newton, Bernoulli, Leibniz, l'Hôpital (same month!)
          Answer: cycloid.

  1744 — EULER develops systematic methods
          Euler-Lagrange equation (Euler's form)

  1755 — LAGRANGE (age 19!) perfects the formalism
          Variational notation δ; δJ = 0 condition
          Lagrange: "this is the analysis of analysis"

  1788 — LAGRANGIAN MECHANICS
          Mécanique analytique — Newton's laws from least action.

  1834 — HAMILTON'S PRINCIPLE
          Principle of least action in mechanics.

  1905 — EINSTEIN special relativity (action formulation)

  1915 — EINSTEIN general relativity (Einstein-Hilbert action)

  1918 — NOETHER'S THEOREM
          Symmetry → conservation law (deepest result)

  1950s — PONTRYAGIN MAXIMUM PRINCIPLE (optimal control)

  1994 — OPTIMAL TRANSPORT (Monge-Kantorovich-Brenier)
          Wasserstein distance and earth-mover's distance.
```

---

## The Euler-Lagrange Equation

The central result: the necessary condition for a functional extremum.

```
  BASIC PROBLEM:
  J[u] = ∫ₐᵇ F(x, u(x), u'(x)) dx

  with FIXED ENDPOINT CONDITIONS: u(a) = A, u(b) = B.

  EULER-LAGRANGE EQUATION:
  ┌────────────────────────────────────────────────────────────────┐
  │  ∂F/∂u − d/dx (∂F/∂u') = 0                                   │
  │                                                                │
  │  or in notation F_u − (F_{u'})_x = 0                         │
  └────────────────────────────────────────────────────────────────┘

  This is a 2nd order ODE for u(x), with BCs u(a)=A, u(b)=B.

  QUICK EXAMPLES:
  ┌────────────────────────────────────────────────────────────────────┐
  │ F = √(1+u'²) (arc length):   E-L gives u'' = 0 → u = straight line│
  │ F = ½u'²   (Dirichlet):       E-L gives u'' = 0 → harmonic fn     │
  │ F = ½u'² − ½u² (oscillator): E-L gives u'' + u = 0 (SHO!)        │
  │ F = ½mq̇² − V(q):            E-L gives mq̈ = −∇V  (Newton's 2nd!) │
  └────────────────────────────────────────────────────────────────────┘
```

---

## Lagrangian Mechanics: The Primary Application

Newton's laws F = ma can be derived from the variational principle of least action:

```
  PRINCIPLE OF LEAST ACTION (Hamilton's principle):

  The physical trajectory q(t) from q(t₁) to q(t₂) is the one
  that makes the ACTION stationary:

  S[q] = ∫_{t₁}^{t₂} L(q, q̇, t) dt,  where L = T − V

  δS = 0  (variation with fixed endpoints)

  → Euler-Lagrange equations:
  d/dt (∂L/∂q̇ᵢ) − ∂L/∂qᵢ = 0  for each generalized coordinate qᵢ

  For L = ½mq̇² − V(q):
  d/dt(mq̇) − (−∂V/∂q) = 0
  mq̈ = −∂V/∂q = F(q)   ← Newton's second law!

  BUT: the variational principle is MORE POWERFUL than Newton's F=ma.
  It works in any coordinate system.
  It naturally handles constraints.
  It generalizes to fields (classical and quantum field theory).
```

---

## Noether's Theorem: Symmetry → Conservation

Emmy Noether (1918): the deepest result connecting symmetry and physics.

```
  NOETHER'S THEOREM:
  ┌────────────────────────────────────────────────────────────────┐
  │  Every continuous symmetry of the action → a conservation law. │
  └────────────────────────────────────────────────────────────────┘

  EXAMPLES:
  ┌──────────────────────────────────────────────────────────────────┐
  │ Symmetry               Conservation Law                          │
  │ ──────────             ─────────────────                         │
  │ Time translation       Energy conservation                       │
  │ Space translation      Momentum conservation                     │
  │ Rotation               Angular momentum conservation             │
  │ U(1) phase rotation    Electric charge conservation              │
  │ SU(2) isospin sym.     Isospin conservation (weak force)         │
  │ SU(3) color sym.       Color charge conservation (strong force)  │
  └──────────────────────────────────────────────────────────────────┘

  This is why physics has conservation laws at all.
  The conservation laws are not independent facts — they follow from
  the symmetries of the action functional.
```

---

## From Functionals to Gradient Flows: The ML Connection

```
  GRADIENT DESCENT (machine learning):
  θ_{n+1} = θ_n − η ∇_θ L(θ)

  This is EULER'S METHOD applied to the gradient flow ODE:
  dθ/dt = −∇_θ L(θ)

  In the limit η → 0 (continuous time), gradient descent is:
  a variational steepest-descent trajectory on the parameter manifold.

  NEURAL ODES (Chen et al. 2018):
  Instead of discrete layers: continuous depth.
  dh/dt = f(h(t), t; θ),  h(0) = input,  output = h(T)
  Training = optimize over θ by solving the ADJOINT equations
  (time-reversed variational problem — Pontryagin principle!)

  OPTIMAL TRANSPORT (Wasserstein distance):
  W₂(μ,ν)² = min over transport plans γ: ∫ |x−y|² dγ(x,y)
  Equivalently (Brenier): W₂² = min over maps T: ∫ |x−T(x)|² dμ
  Used in: generative models (Wasserstein GAN), distribution matching,
           data augmentation, causal inference.
```

---

## This Directory

| File | Topic |
|------|-------|
| 00-OVERVIEW.md | This file — landscape and taxonomy |
| 01-FUNCTIONALS.md | Functionals and the variational derivative |
| 02-EULER-LAGRANGE.md | Euler-Lagrange equations |
| 03-CONSTRAINTS.md | Constrained variation and Lagrange multipliers |
| 04-LAGRANGIAN-MECHANICS.md | Lagrangian mechanics |
| 05-HAMILTONIAN-MECHANICS.md | Hamiltonian mechanics and phase space |
| 06-SECOND-VARIATION.md | Second variation and stability |
| 07-DIRECT-METHODS.md | Direct methods and Sobolev spaces |
| 08-OPTIMAL-CONTROL.md | Optimal control and Pontryagin principle |
| 09-ML-CONNECTIONS.md | Connections to machine learning and gradient flows |

---

## Decision Cheat Sheet

| I want to... | Variational tool |
|--------------|-----------------|
| Find shortest/fastest path | Euler-Lagrange equation |
| Derive equations of motion | Lagrangian mechanics: δS=0 |
| Conserved quantity from symmetry | Noether's theorem |
| Change to momentum-based description | Legendre transform → Hamiltonian |
| Constrained optimization | Lagrange multipliers in variational setting |
| Check if extremum is min or max | Second variation test |
| Existence of minimizer (rigorously) | Direct methods in Sobolev spaces |
| Optimal control problem | Pontryagin maximum principle |
| Gradient descent as continuous limit | Gradient flow ODE |

---

## Common Confusion Points

**"Is this the same Lagrange as Lagrange interpolation?"**
Yes — same Joseph-Louis Lagrange (1736–1813), mathematician of extraordinary range.
The Lagrange in Lagrange multipliers, Lagrangian mechanics, Lagrange interpolation,
and the Euler-Lagrange equations is all the same person.

**"Least action says the action is 'least' — but isn't it really just stationary?"**
Right. Hamilton's principle should be called the "principle of stationary action."
The action is not always minimized — it can be a saddle point. For short paths in simple
potentials, it is a minimum. For long paths or near caustics, it may be a saddle.
The Euler-Lagrange conditions capture all stationary points, minima or not.

**"Why is variational calculus called 'calculus' of variations?"**
Leibniz introduced "calculus" for differential/integral calculus. Variational calculus
extends this to variations of entire functions (not just points). The "variation" δu
is an infinitesimal perturbation of a function, analogous to the differential dx of a
coordinate. The variational derivative δJ/δu is the functional generalization of the
gradient ∇J of a function of finitely many variables.
