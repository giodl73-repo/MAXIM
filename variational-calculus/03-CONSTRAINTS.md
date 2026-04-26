# Constrained Variation and Lagrange Multipliers

## The Big Picture

Real variational problems often have constraints: the function must satisfy auxiliary
conditions in addition to the boundary conditions.

```
+-----------------------------------------------------------------------+
|              CONSTRAINED VARIATION                                    |
|                                                                       |
|  UNCONSTRAINED: extremize J[u] over all admissible u                  |
|  → Euler-Lagrange equation                                            |
|                                                                       |
|  ISOPERIMETRIC CONSTRAINT:                                            |
|  extremize J[u] subject to K[u] = C (integral constraint)             |
|  → E-L for J − λK  (Lagrange multiplier λ)                            |
|                                                                       |
|  HOLONOMIC (POINTWISE) CONSTRAINT:                                    |
|  extremize J[u] subject to g(x, u, u') = 0                            |
|  → E-L for F + λ(x)g (multiplier is a FUNCTION)                     |
|                                                                       |
|  NON-HOLONOMIC (DIFFERENTIAL) CONSTRAINT:                             |
|  constraint involves velocities in a non-integrable way               |
|  → Requires special treatment                                         |
|                                                                       |
|  CONNECTION TO OPTIMIZATION:                                          |
|  This is infinite-dimensional constrained optimization.               |
|  Same idea as KKT conditions but in function spaces.                  |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## Isoperimetric Problems

The classical isoperimetric problem: among all closed curves of length L, find the one
enclosing maximum area.

```
  GENERAL ISOPERIMETRIC PROBLEM:
  Extremize J[u] = ∫ₐᵇ F(x, u, u') dx
  subject to K[u] = ∫ₐᵇ G(x, u, u') dx = C  (fixed value)

  LAGRANGE MULTIPLIER METHOD:
  Form the augmented functional:
  Φ[u] = J[u] − λ K[u] = ∫ₐᵇ [F − λG] dx

  The Lagrange multiplier λ is a CONSTANT.

  E-L EQUATION FOR AUGMENTED FUNCTIONAL:
  (F − λG)_u − d/dx (F − λG)_{u'} = 0
  i.e.:  F_u − λG_u − d/dx(F_{u'} − λG_{u'}) = 0

  DETERMINE λ: from the constraint K[u] = C.

  INTUITION: Moving along the constraint surface K=C,
  the derivative of J vanishes when J and K have parallel gradients:
  δJ = λ δK   →   δ(J − λK) = 0.
```

### Classical Isoperimetric: Circle Maximizes Area

```
  PROBLEM: Among curves of length L enclosing area A, maximize A.
  Parametric: (x(t), y(t)) for t ∈ [0,1] (closed curve).

  AREA (Green's formula): A = ½ ∫₀¹ (x ẏ − y ẋ) dt
  LENGTH:                 L = ∫₀¹ √(ẋ² + ẏ²) dt  = const

  Augmented: A − λL = ½∫(xẏ − yẋ) dt − λ∫√(ẋ²+ẏ²) dt

  E-L for x and y:
  x: ẏ − d/dt[−y − λẋ/v] = 0   (v = √(ẋ²+ẏ²))
  y: −ẋ − d/dt[x − λẏ/v] = 0

  Solution: circle of radius r = 1/(2λ).
  Constraint L = 2πr → λ = π/L, r = L/2π.
  Maximum area: A = πr² = L²/4π.

  ISOPERIMETRIC INEQUALITY:  4πA ≤ L²  (equality iff circle)
```

---

## Queen Dido's Problem (Historical)

```
  Dido's problem: maximize area enclosed between a curve and
  a straight shoreline, with curve of fixed length.

  One side is the x-axis (straight line from 0 to a).
  Curve u(x) connects (0,0) to (a,0).

  Maximize: A = ∫₀ᵃ u dx
  Subject to: L = ∫₀ᵃ √(1+u'²) dx  (fixed length)

  Augmented: ∫₀ᵃ [u − λ√(1+u'²)] dx

  E-L: 1 − λ d/dx[u'/√(1+u'²)] = 0
  → u'/√(1+u'²) = (x − x₀)/λ   (integrating)
  → (x−x₀)² + u² = λ²  (circle of radius λ)

  ANSWER: Semicircle. Dido should construct a semicircular city.
  (Historical: Carthage was semi-circular. Virgil, Aeneid.)
```

---

## Holonomic Constraints: Multiplier as a Function

For pointwise constraints g(x, u, u') = 0 at every x:

```
  PROBLEM: Extremize J[u] = ∫ F(x, u, u') dx
  subject to g(x, u, u') = 0 for all x ∈ [a,b].

  LAGRANGE MULTIPLIER: λ(x) is now a FUNCTION (not a constant).

  AUGMENTED FUNCTIONAL:
  Φ[u, λ] = ∫ₐᵇ [F(x,u,u') + λ(x)g(x,u,u')] dx

  E-L EQUATIONS:
  (F + λg)_u − d/dx(F + λg)_{u'} = 0
  g(x, u, u') = 0   (the constraint is enforced by E-L for λ)

  This is a system for u(x) and λ(x) simultaneously.
```

### Pendulum with Constraint

```
  Pendulum: rod length ℓ, mass m at tip.
  Cartesian coordinates: (x,y), constraint x² + y² = ℓ².

  Unconstrained L = ½m(ẋ² + ẏ²) + mgy
  Constraint: g = x² + y² − ℓ² = 0

  LAGRANGIAN WITH MULTIPLIER:
  L + λg = ½m(ẋ² + ẏ²) + mgy + λ(x² + y² − ℓ²)

  E-L equations:
  mẍ = 2λx   (λ = Lagrange multiplier = tension/2ℓ for the rod)
  mÿ = mg + 2λy

  Constraint: x² + y² = ℓ²

  Physical meaning: 2λ = T/ℓ where T is the tension in the rod.
  The multiplier IS the constraint force.
```

---

## Non-Holonomic Constraints

Constraints that cannot be integrated to purely positional form:

```
  HOLONOMIC: constraint = f(q₁,...,q_n, t) = 0
  (depends only on positions, not velocities)
  Can reduce number of DOF.
  Lagrange multipliers → constraint forces.

  NON-HOLONOMIC: constraint = f(q, q̇, t) = 0
  (depends on velocities in a non-integrable way)
  Cannot reduce DOF by simple substitution.
  Requires: Lagrange-d'Alembert principle.

  EXAMPLES:
  • Rolling without slipping:  ẋ = r·θ̇  (can be integrated → holonomic)
  • Rolling without slipping on a plane (x,y):
    ẋ = r cosφ · θ̇
    ẏ = r sinφ · θ̇
    These two together are non-integrable for general paths.
  • Knife-edge (skate blade): blade moves only along its direction.

  LAGRANGE-D'ALEMBERT for non-holonomic:
  Σ (d/dt ∂L/∂q̇ᵢ − ∂L/∂qᵢ) δqᵢ = 0
  for all virtual displacements δq consistent with constraint.

  Non-holonomic constraints lead to:
  • Anholonomic geometry (Berry phase in quantum mechanics)
  • Sub-Riemannian geometry
  • Motion planning in robotics
```

---

## Eigenvalue Problems as Variational Problems

The Sturm-Liouville eigenvalue problem has a natural variational formulation:

```
  STURM-LIOUVILLE:  −(pu')' + qu = λwu  on [a,b]

  RAYLEIGH QUOTIENT:
  R[u] = ∫[p(u')² + qu²] dx / ∫ w u² dx

  VARIATIONAL CHARACTERIZATION:
  λ₁ = min R[u]  (over H₀¹, u ≠ 0)
  λ₂ = min R[u]  (over u ⊥ φ₁ in L²_w-norm)
  λ_n = min R[u]  (over u ⊥ φ₁,...,φ_{n-1})

  This is the MIN-MAX THEOREM (Courant-Fischer).

  APPLICATIONS:
  • Fundamental frequency of a drum = √λ₁ (lowest eigenvalue of −∇²)
  • Smallest eigenvalue of a matrix ↔ ground state energy
  • Kohn-Sham DFT: minimize energy over electron density
  • FEM: approximates eigenvalues from above (by Galerkin projection)

  RAYLEIGH-RITZ METHOD:
  Approximate λ₁ by minimizing R over a trial function space.
  Always gives an UPPER BOUND: R[trial] ≥ λ₁.
```

---

## Isoperimetric Constraints in PDE Context

```
  ENERGY MINIMIZATION WITH MASS CONSTRAINT:

  Problem: minimize ∫_Ω |∇u|² dx subject to ∫_Ω u² dx = 1, u=0 on ∂Ω.

  Augmented: minimize ∫|∇u|² dx − λ ∫u² dx

  E-L: −∇²u = λu  (eigenvalue problem for −∇²!)

  λ = smallest eigenvalue of −∇²
  u = corresponding eigenfunction

  This shows: the ground state of a quantum particle in a box (infinite
  square well) minimizes the kinetic energy for fixed normalization.

  NONLINEAR CONSTRAINT: ∫_Ω |u|^p dx = 1 (Lp normalization)
  More general nonlinear eigenvalue problem.
  Arises in: nonlinear Schrödinger equations, Gross-Pitaevskii (BEC).
```

---

## Penalty Method: Relaxing Constraints

```
  Instead of enforcing constraint g[u] = 0 exactly,
  penalize violations:

  J_ε[u] = J[u] + (1/ε) K[u]²

  As ε→0: constraint enforced more and more strictly.
  The Lagrange multiplier λ ≈ K[u]/ε automatically.

  AUGMENTED LAGRANGIAN:
  L_ρ[u, λ] = J[u] − λ K[u] + (ρ/2) K[u]²

  Saddle point of L_ρ w.r.t. (u,λ).
  Better conditioning than pure penalty method.
  Foundation of ADMM (Alternating Direction Method of Multipliers).

  ML CONTEXT: L2 regularization in neural networks:
  L_reg(θ) = L(θ) + λ‖θ‖²
  This is J[u] + λ·(norm constraint) — isoperimetric regularization.
  The regularization parameter λ IS a Lagrange multiplier for the
  constraint ‖θ‖² ≤ C.
```

---

## Decision Cheat Sheet

| Constraint type | Method | Multiplier |
|----------------|--------|------------|
| Integral constraint ∫G dx = C | Isoperimetric: E-L for F − λG | λ = constant |
| Pointwise constraint g(x,u,u')=0 | Holonomic: E-L for F + λ(x)g | λ(x) = function |
| Velocity constraint, integrable | Holonomic (convert) | reduces DOF |
| Velocity constraint, non-integrable | Lagrange-d'Alembert | Constraint forces |
| Eigenvalue problem | Rayleigh quotient minimization | λ = eigenvalue |
| Approximate constraint | Penalty method / augmented Lagrangian | Automatic |

---

## Common Confusion Points

**"Lagrange multiplier is a constant for integral constraints — why does it become a function
for pointwise constraints?"**
For an integral constraint K[u] = C, you have ONE constraint (one number = one constant).
For a pointwise constraint g(x,u)=0, you have INFINITELY MANY constraints (one per point x).
Each needs its own multiplier → λ(x) is a function. The multiplier λ(x) is identified with
the constraint force at position x (e.g., tension in a rod).

**"Rayleigh quotient gives an upper bound for λ₁. Is it always above the true eigenvalue?"**
Yes. The Rayleigh-Ritz principle: R[v] ≥ λ₁ for all v ≠ 0 in the domain of L, with equality
only when v is the first eigenfunction φ₁. This means any trial function gives an upper bound
on the ground-state energy (quantum mechanics) or fundamental frequency (acoustics). FEM
eigenvalues always overestimate true eigenvalues for this reason.

**"Is regularization in machine learning really a Lagrange multiplier?"**
Exactly. Lasso (L1 penalty) corresponds to a Lagrange multiplier for ‖θ‖₁ ≤ C.
Ridge regression (L2 penalty) corresponds to ‖θ‖₂² ≤ C. The regularization
parameter λ in L(θ) + λ‖θ‖² is the Lagrange multiplier for the norm constraint.
Different values of λ trace out the Pareto frontier between data fit and model complexity.
