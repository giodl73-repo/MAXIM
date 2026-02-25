# Functionals and the Variational Derivative

## Functionals: From Functions to Numbers

A **functional** is a map from a space of functions to the real numbers.

```
+-----------------------------------------------------------------------+
|              FUNCTIONS vs. FUNCTIONALS                                 |
|                                                                       |
|  FUNCTION:   f: R^n → R                                              |
|  Input:  a point x ∈ R^n (finite-dimensional vector)                  |
|  Output: a number f(x) ∈ R                                            |
|  Extremum condition:  ∇f(x) = 0   (gradient = 0)                     |
|                                                                       |
|  FUNCTIONAL:  J: V → R   (V = function space)                         |
|  Input:  a FUNCTION u ∈ V  (infinite-dimensional "point")            |
|  Output: a number J[u] ∈ R                                            |
|  Extremum condition:  δJ/δu = 0   (variational derivative = 0)       |
|                                                                       |
|  KEY: infinite-dimensional optimization requires infinite-dimensional  |
|  calculus — this is what variational calculus provides.               |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## Integral Functionals: The Standard Form

```
  BASIC INTEGRAL FUNCTIONAL:
  J[u] = ∫ₐᵇ F(x, u(x), u'(x)) dx

  F is called the LAGRANGIAN or LAGRANGE DENSITY.
  (x = independent variable, u = function, u' = derivative)

  MULTI-VARIABLE:
  J[u] = ∫_Ω F(x, u, ∇u) dx   (x ∈ R^n, u: Ω → R)

  MULTIPLE FUNCTIONS:
  J[u,v] = ∫ₐᵇ F(x, u, v, u', v') dx  (system case)

  HIGHER DERIVATIVES:
  J[u] = ∫ₐᵇ F(x, u, u', u'') dx   (beam bending, thin plates)

  EXAMPLES:
  ┌───────────────────────────────────────────────────────────────┐
  │ Arc length:         J[u] = ∫√(1+u'²) dx                     │
  │ Area functional:    J[u] = ∫∫ √(1+u_x²+u_y²) dA            │
  │ Dirichlet energy:   J[u] = ½∫|∇u|² dA                       │
  │ Elastic energy:     J[u] = ½∫EI(u'')² dx  (beam)            │
  │ Least action:       S[q] = ∫[½m|q̇|² − V(q)] dt             │
  │ Optimal transport:  W²[T] = ∫|x − T(x)|² dμ(x)             │
  │ Log-likelihood:     L[θ] = Σ log p(xᵢ; θ) (with θ = fn)    │
  └───────────────────────────────────────────────────────────────┘
```

---

## Variations: The Infinite-Dimensional Differential

The variation δu is a perturbation of the function u.

```
  ADMISSIBLE VARIATIONS:
  Given u satisfying endpoint conditions u(a)=A, u(b)=B,
  a variation η(x) must satisfy η(a) = η(b) = 0  (fixed endpoints).

  PERTURBED FUNCTION:  u_ε(x) = u(x) + ε·η(x)

  VARIATION OF THE FUNCTIONAL:
  J[u + εη] = ∫ F(x, u+εη, u'+εη') dx

  = ∫ F(x,u,u') dx + ε ∫ [∂F/∂u · η + ∂F/∂u' · η'] dx + O(ε²)

  FIRST VARIATION:
  δJ[u; η] = dJ[u+εη]/dε|_{ε=0}
           = ∫ₐᵇ [F_u · η + F_{u'} · η'] dx

  where F_u = ∂F/∂u,  F_{u'} = ∂F/∂u'.

  STATIONARY CONDITION: J is stationary at u if δJ[u;η] = 0 for ALL η.
  This is the calculus of variations analogue of ∇f = 0.
```

---

## Integration by Parts: Deriving E-L

```
  The key step: integrate the η' term by parts.

  δJ = ∫ₐᵇ [F_u · η + F_{u'} · η'] dx

     = ∫ₐᵇ F_u · η dx + [F_{u'} · η]ₐᵇ − ∫ₐᵇ (d/dx F_{u'}) · η dx

     = [F_{u'} · η]ₐᵇ + ∫ₐᵇ [F_u − d/dx(F_{u'})] · η dx

  FIXED ENDPOINTS: η(a) = η(b) = 0 → boundary term vanishes.

  δJ = ∫ₐᵇ [F_u − d/dx(F_{u'})] · η dx = 0   for ALL η

  By the FUNDAMENTAL LEMMA of calculus of variations:
  if ∫ₐᵇ f(x)·η(x) dx = 0 for all smooth η with η(a)=η(b)=0,
  then f(x) = 0 everywhere on [a,b].

  → EULER-LAGRANGE EQUATION:  F_u − d/dx(F_{u'}) = 0
```

### Fundamental Lemma of Calculus of Variations

```
  LEMMA: If f ∈ C[a,b] and ∫ₐᵇ f(x)η(x) dx = 0 for every η ∈ C_c^∞(a,b),
  then f(x) = 0 for all x ∈ [a,b].

  PROOF SKETCH:
  Suppose f(x₀) > 0 for some x₀ ∈ (a,b).
  By continuity, f > 0 in some interval [x₀−δ, x₀+δ].
  Choose η ≥ 0 supported in [x₀−δ, x₀+δ].
  Then ∫ fη > 0 — contradiction.

  This is the bridge from "δJ=0 for all η" to the E-L equation.
  It's the variational calculus version of:
  "if ⟨v,w⟩ = 0 for all w, then v = 0."
```

---

## The Variational Derivative (Functional Gradient)

For functionals of the form J[u] = ∫ F(x,u,∇u) dx, define:

```
  VARIATIONAL DERIVATIVE (Fréchet derivative):
  δJ/δu = ∂F/∂u − ∇·(∂F/∂(∇u))

  This is the "gradient" of J as a function of the infinite-dimensional
  argument u. The Euler-Lagrange equation is simply:

  δJ/δu = 0

  EXAMPLES:
  ┌─────────────────────────────────────────────────────────────────┐
  │ Dirichlet: J[u] = ½∫|∇u|² dx                                   │
  │   δJ/δu = −∇²u   (the negative Laplacian)                     │
  │   δJ/δu = 0 → ∇²u = 0  (Laplace equation)                    │
  │                                                                 │
  │ Area: J[u] = ∫√(1+|∇u|²) dA                                   │
  │   δJ/δu = −∇·(∇u/√(1+|∇u|²))                                 │
  │   = −(mean curvature H of the surface u)                       │
  │   δJ/δu = 0 → H = 0  (minimal surface equation)               │
  │                                                                 │
  │ Action: S[q] = ∫L(q,q̇)dt                                       │
  │   δS/δq = ∂L/∂q − d/dt(∂L/∂q̇)                                │
  │   δS/δq = 0 → Euler-Lagrange equations of mechanics            │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Natural Boundary Conditions

When the endpoints are NOT fixed, the boundary term does not vanish:

```
  δJ = [F_{u'}η]ₐᵇ + ∫ₐᵇ [F_u − (F_{u'})'] η dx = 0

  If endpoint b is FREE (no constraint on u(b)):
  The term F_{u'}(b)·η(b) must also vanish for arbitrary η(b).
  → NATURAL BOUNDARY CONDITION: F_{u'}(b) = 0.

  EXAMPLE: Neumann BC for Dirichlet functional.
  J[u] = ½∫₀ᴸ u'² dx, u(0) = 0 (fixed), u(L) free.
  F = ½u'², F_{u'} = u'
  E-L: u'' = 0 → u linear.
  Natural BC: u'(L) = 0 → Neumann condition emerges naturally!

  SIGNIFICANCE:
  Essential BCs (Dirichlet): prescribed on function u directly.
  Natural BCs (Neumann): emerge from the variational formulation.
  This is exactly the FEM Essential vs. Natural BC distinction.
```

---

## Second Variation: Local vs. Global Extrema

```
  SECOND VARIATION: the analogue of the Hessian.

  J[u+εη] = J[u] + ε δJ[u;η] + ½ε² δ²J[u;η,η] + O(ε³)

  For a stationary point (δJ = 0), the second variation determines
  whether it is a minimum, maximum, or saddle:

  δ²J[u;η] = ∫ₐᵇ [F_{uu} η² + 2F_{uu'} ηη' + F_{u'u'} η'²] dx

  LEGENDRE CONDITION (necessary for local minimum):
  F_{u'u'} ≥ 0  for all x ∈ [a,b]

  (Analogy: for f(x) at a minimum, f'' ≥ 0)

  JACOBI CONDITION (necessary for strong local minimum):
  No conjugate points exist on [a,b].
  (A conjugate point is where the Jacobi equation has a vanishing solution)

  FULL LOCAL MINIMUM: Legendre + Jacobi conditions both satisfied.
  GLOBAL MINIMUM: requires additional coercivity (direct methods).
```

---

## Functionals with Higher Derivatives

```
  BEAM BENDING (Euler-Bernoulli):
  J[u] = ½ ∫₀ᴸ EI (u'')² dx − ∫₀ᴸ q(x)u dx

  F = ½EI(u'')² − qu,  depends on u, u', u''

  E-L EQUATION FOR HIGHER ORDER:
  For J[u] = ∫ F(x,u,u',u'') dx:
  E-L: F_u − (F_{u'})' + (F_{u''})'' = 0

  For beam: 0 − 0 + (EI·u'')'' − q = 0
  → (EI u'')'' = q   (4th order ODE — biharmonic)

  GENERAL RULE for J[u] = ∫ F(x,u,u',...,u^{(n)}) dx:
  E-L: Σ_{k=0}^n (−1)^k d^k/dx^k (∂F/∂u^{(k)}) = 0
```

---

## Functional Analysis Background

```
  FUNCTION SPACES FOR VARIATIONAL PROBLEMS:

  L²[a,b]:  {u: ∫|u|² < ∞}  (square-integrable)
  H¹[a,b]:  {u ∈ L²: u' ∈ L²}  (Sobolev space)
  C¹[a,b]:  continuously differentiable functions

  The variational derivative δJ/δu lives in the DUAL SPACE V*.

  FRÉCHET DERIVATIVE (rigorous first variation):
  J[u+h] = J[u] + DJ[u]·h + o(‖h‖)
  DJ[u] is a bounded linear functional — the Fréchet derivative.
  δJ/δu is the Riesz representative of DJ[u] (via inner product).

  GÂTEAUX DERIVATIVE (directional derivative):
  dJ/dε|_{ε=0} J[u+εη]  in direction η.
  Less demanding than Fréchet (no uniform remainder bound needed).
  Sufficient for deriving E-L equations.

  COMPACT OPERATORS:
  For J[u] = ½‖u‖² − ∫ g(x)u(x)dx  (quadratic functionals),
  critical points are solutions to linear equations.
  Spectral theory of compact self-adjoint operators → eigenfunction expansions.
```

---

## Decision Cheat Sheet

| Concept | Definition |
|---------|------------|
| Functional J[u] | Map from functions to numbers: J: V → R |
| Variation δu | Perturbation: u → u + εη, η with η=0 at endpoints |
| First variation δJ | dJ[u+εη]/dε at ε=0; analogue of directional derivative |
| Stationary condition | δJ[u;η] = 0 for all admissible η |
| Variational derivative δJ/δu | The E-L expression: the "gradient" of J |
| E-L equation | δJ/δu = 0 (necessary condition for extremum) |
| Natural BC | Emerges from free-endpoint variation; analogue of Neumann BC |
| Second variation δ²J | Analogue of Hessian; positive definite → local minimum |
| Legendre condition | F_{u'u'} ≥ 0 (necessary for minimum) |

---

## Common Confusion Points

**"The E-L equation is a necessary condition. Can I have a stationary point that's not a
minimum?"**
Absolutely. Just like f'(x)=0 identifies both minima and maxima of a function, E-L
identifies all stationary points: minima, maxima, and saddle points. The second variation
test distinguishes them. In Lagrangian mechanics, the physical trajectory is a saddle
point of the action (not a minimum) for paths longer than the first conjugate point.

**"What's the difference between δJ/δu = 0 and ∇J = 0?"**
Notation only: δJ/δu and ∇J both mean "the gradient of J with respect to u." In finite
dimensions we write ∇f(x) = 0; in infinite dimensions (functional space) we write δJ/δu = 0
or DJ[u] = 0. The conceptual idea is identical: find the point where the "slope" of J
in every direction is zero.

**"Why does the variational derivative of the Dirichlet functional give the Laplacian?"**
J[u] = ½∫|∇u|²dx; F_u = 0, ∂F/∂(∇u) = ∇u.
δJ/δu = −∇·(∇u) = −∇²u.
Setting to zero: ∇²u = 0 (Laplace equation).
So the harmonic functions are exactly the minimizers of the Dirichlet energy. This is
the variational characterization of Laplace's equation.
