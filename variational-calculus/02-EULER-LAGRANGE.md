# Euler-Lagrange Equations

**Reader note**: The E-L derivation and classical examples below serve as reference. The key value for this learner is the connection between E-L and the fundamental PDEs of physics (Laplace, wave, Schrodinger as E-L equations of their action functionals), Noether's theorem, and the field-theory generalization — these sections follow the classical material.

## The Central Result

The Euler-Lagrange equation is the necessary condition for a function to extremize a
functional. It is the single most important equation in variational calculus.

```
+-----------------------------------------------------------------------+
|              EULER-LAGRANGE EQUATION                                   |
|                                                                       |
|  FUNCTIONAL:  J[u] = ∫ₐᵇ F(x, u, u') dx                             |
|                                                                       |
|  EULER-LAGRANGE EQUATION:                                             |
|  ┌────────────────────────────────────────────────────────────────┐   |
|  │  ∂F     d  (  ∂F  )                                           │   |
|  │  ── − ─── │ ───── │ = 0                                       │   |
|  │  ∂u    dx  (  ∂u' )                                           │   |
|  └────────────────────────────────────────────────────────────────┘   |
|                                                                       |
|  EXPANDED:  F_u − F_{u'x} − F_{u'u}u' − F_{u'u'}u'' = 0            |
|  (a 2nd order ODE for u(x))                                          |
|                                                                       |
|  BOUNDARY CONDITIONS:  u(a) = A,  u(b) = B  (if fixed)              |
|  OR:  natural BCs from free endpoints (F_{u'} = 0 at free end)       |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## Derivation

```
  SETUP:  u is the minimizer of J[u] = ∫ₐᵇ F(x,u,u') dx.
          u_ε(x) = u(x) + ε·η(x),  η ∈ C_c^∞(a,b) (η(a)=η(b)=0).

  For J to be stationary at u:
  d/dε J[u_ε]|_{ε=0} = 0

  d/dε J[u_ε] = d/dε ∫ F(x, u+εη, u'+εη') dx
              = ∫ [∂F/∂u · η + ∂F/∂u' · η'] dx
              = ∫ F_u η dx + ∫ F_{u'} η' dx

  INTEGRATE BY PARTS on the second integral:
  ∫ F_{u'} η' dx = [F_{u'} η]ₐᵇ − ∫ (d/dx F_{u'}) η dx
                 = 0 − ∫ (F_{u'})_x η dx     (η vanishes at endpoints)

  COMBINE:
  δJ = ∫ₐᵇ [F_u − (F_{u'})_x] η dx = 0   for ALL η

  By fundamental lemma: F_u − (F_{u'})_x = 0   ■
```

---

## Key Examples

### Arc Length: Geodesics

```
  PROBLEM: shortest path between (a,A) and (b,B)
  J[u] = ∫ₐᵇ √(1 + u'²) dx

  F = √(1+u'²),  F_u = 0,  F_{u'} = u'/√(1+u'²)

  E-L: d/dx [u'/√(1+u'²)] = 0
       → u'/√(1+u'²) = const
       → u' = const   (constant slope)
       → u(x) = mx + c  (straight line)

  ANSWER: the shortest path in the plane is a straight line. ✓
  (Obvious geometrically, but confirms the method works.)
```

### Brachistochrone: Curve of Fastest Descent

```
  PROBLEM: Bead slides from (0,0) to (a,b) under gravity.
  Find the curve shape u(x) minimizing transit time.

  T[u] = ∫₀ᵃ √(1+u'²) / √(2g·u) dx  (speed = √(2g·height))

  Wait — use the arc instead: y = u(x), ds = √(1+u'²) dx,
  speed v = √(2gy) (from energy conservation).
  time = ∫ ds/v = ∫ √(1+u'²)/√(2gu) dx

  F = √(1+u'²)/√(2gu),  F_u = −½√(1+u'²)/(u√(2gu))

  Since F has no explicit x: use the BELTRAMI IDENTITY (see below).
  F − u' F_{u'} = C

  √(1+u'²)/√(2gu) − u'·u'/(√(1+u'²)√(2gu)) = C

  1/[√(u(1+u'²))] = C'  (simplification)

  Solution: parametric form (cycloid!):
  x = r(θ − sin θ),  u = r(1 − cos θ)

  ANSWER: The brachistochrone is a cycloid — the curve traced
  by a point on the rim of a rolling circle.
```

### Minimal Surface

```
  PROBLEM: Surface of revolution with minimal area.
  Rotate u(x) around x-axis; area = 2π ∫ u·√(1+u'²) dx

  F = u√(1+u'²),  F_u = √(1+u'²),  F_{u'} = uu'/√(1+u'²)

  E-L: √(1+u'²) − d/dx[uu'/√(1+u'²)] = 0

  This simplifies to: u·u'' = 1 + u'²
  Solution: u(x) = a·cosh((x−b)/a)  (CATENARY)

  ANSWER: The minimal surface of revolution is a catenoid —
  surface formed by rotating a catenary.
  Soap film between two circular rings forms a catenoid.
```

---

## Beltrami Identity: When F Has No Explicit x

A crucial simplification when ∂F/∂x = 0 (autonomous case):

```
  IF F = F(u, u')  (no explicit x dependence):

  BELTRAMI IDENTITY:  F − u'·∂F/∂u' = C  (constant)

  DERIVATION:
  d/dx[F − u'F_{u'}] = F_u u' + F_{u'} u'' − u''F_{u'} − u'·d/dx F_{u'}
                     = u'[F_u − d/dx F_{u'}]
                     = u' · 0   (by E-L equation)
                     = 0

  So F − u'F_{u'} is constant along solutions!

  This reduces the 2nd order E-L equation to a 1st order ODE.
  Much easier to solve.

  EXAMPLES:
  Arc length: F = √(1+u'²), Beltrami → 1/√(1+u'²) = C → u' = const.
  Brachistochrone: F = √(1+u'²)/√(u), used above.
  Lagrangian with no explicit t: energy conservation (H = const).
```

---

## Multiple Variables: PDEs from E-L

For functionals with functions of several variables:

```
  J[u] = ∫_Ω F(x, u, ∇u) dx   (x ∈ R^n)

  E-L EQUATION:
  ∂F/∂u − Σᵢ ∂/∂xᵢ (∂F/∂(∂u/∂xᵢ)) = 0

  or:  F_u − ∇·(∂F/∂(∇u)) = 0

  EXAMPLES:
  ┌─────────────────────────────────────────────────────────────────┐
  │ J = ½∫|∇u|²dx:  −∇²u = 0        (Laplace equation)           │
  │ J = ½∫[|∇u|²−2fu]dx: −∇²u = f   (Poisson equation)          │
  │ J = ∫√(1+|∇u|²)dx: −∇·(∇u/√(1+|∇u|²)) = 0 (minimal surface)│
  │ J = ½∫[|∇u|²+V(x)u²]dx: −∇²u+V(x)u = 0  (Schrödinger type) │
  │ J = ½∫[u_tt²−c²u_xx²]dt dx: u_tt − c²u_xx = 0  (wave!)      │
  └─────────────────────────────────────────────────────────────────┘

  KEY INSIGHT: Every major linear PDE of physics is the E-L equation
  of a corresponding quadratic action functional.
```

---

## System E-L Equations

For multiple dependent variables u = (u₁,...,u_m):

```
  J[u₁,...,u_m] = ∫ F(x, u₁,...,u_m, u₁',...,u_m') dx

  E-L SYSTEM:  for each k = 1,...,m:
  ∂F/∂u_k − d/dx(∂F/∂u_k') = 0

  MECHANICS EXAMPLE: N particles, qi = position of particle i
  L(q, q̇) = ½Σ mᵢ|q̇ᵢ|² − V(q₁,...,q_N)

  E-L: d/dt(mᵢq̇ᵢ) = −∂V/∂qᵢ = Fᵢ  (Newton's 2nd for each particle)

  FIELD THEORY: u(x,t) is a field (function of space and time)
  L = ½(u_t² − c²u_x²) − W(u)  (Klein-Gordon if W = ½m²u²)

  E-L: ∂²u/∂t² − c²∇²u + W'(u) = 0  (nonlinear wave equation)
```

---

## Noether's Theorem: Formal Statement

```
  SETUP: Action S[q] = ∫ L(q, q̇, t) dt invariant under a
  one-parameter family of transformations:
    q → Q(q, s),   t → T(t, s)   (s = parameter, s=0 is identity)

  NOETHER'S CURRENT:
  For a variational symmetry (δS = 0):

  J = Σᵢ (∂L/∂q̇ᵢ)·(∂Qᵢ/∂s|_{s=0}) − H·(∂T/∂s|_{s=0})

  where H = Σᵢ (∂L/∂q̇ᵢ)q̇ᵢ − L  (Hamiltonian).

  CONSERVATION LAW: dJ/dt = 0 along solutions.

  ┌────────────────────────────────────────────────────────────┐
  │ SYMMETRY               CONSERVED QUANTITY                  │
  │ q → q + a (translation)  → pᵢ = ∂L/∂q̇ᵢ  (momentum)     │
  │ t → t + s (time shift)   → H = Σpq̇ − L   (energy)       │
  │ q → R(s)q (rotation)     → L = q × p       (ang. moment)  │
  │ φ → φ + s (U(1) phase)   → Q (electric charge)            │
  └────────────────────────────────────────────────────────────┘
```

---

## Conjugate Momentum and Legendre Transform

A key structure in the E-L formulation:

```
  CANONICAL MOMENTUM (conjugate to q):
  pᵢ = ∂L/∂q̇ᵢ

  PHYSICAL MEANING:
  In L = ½m|q̇|² − V(q): p = mq̇ (usual momentum).
  In electromagnetic coupling: p = mq̇ + eA/c (kinetic + vector potential).
  In relativistic L = −mc²√(1−v²/c²): p = mv/√(1−v²/c²) (relativistic momentum).

  E-L EQUATION in terms of p:
  d/dt(pᵢ) = ∂L/∂qᵢ
  ṗᵢ = ∂L/∂qᵢ  (generalized force = rate of change of momentum)

  LEGENDRE TRANSFORM (to Hamiltonian):
  H(q, p) = Σᵢ pᵢ q̇ᵢ − L(q, q̇, t)
  where q̇ is expressed as a function of p from pᵢ = ∂L/∂q̇ᵢ.
  (This requires the map q̇ → p to be invertible: ∂²L/∂q̇² nonsingular)
```

---

## Computing the E-L Equation: Procedure

```
  PROCEDURE for J[u] = ∫ₐᵇ F(x, u, u') dx:

  STEP 1: Compute partial derivatives of F.
    F_u = ∂F/∂u
    F_{u'} = ∂F/∂u'

  STEP 2: Compute total derivative of F_{u'}.
    d/dx F_{u'} = (∂F_{u'}/∂x) + (∂F_{u'}/∂u)u' + (∂F_{u'}/∂u')u''
               = F_{u'x} + F_{u'u}u' + F_{u'u'}u''

  STEP 3: E-L equation:
    F_u − F_{u'x} − F_{u'u}u' − F_{u'u'}u'' = 0

  STEP 4: Solve the 2nd order ODE with BCs.

  IF F has no explicit x (autonomous):
    Use Beltrami: F − u'F_{u'} = C (reduces to 1st order ODE).

  IF F is quadratic in u':
    F = ½A(x)u'² + B(x)uu' + ½C(x)u²
    E-L gives:  −(Au')' + ½B'u − Bu' − ½(−C+...)u = 0
    → 2nd order linear ODE.
```

---

## Decision Cheat Sheet

| Situation | Tool |
|-----------|------|
| F = F(x,u,u') | Standard E-L: F_u − (F_{u'})' = 0 |
| F has no explicit x | Beltrami identity: F − u'F_{u'} = C |
| Multiple functions | One E-L per function |
| u defined on domain in R^n | E-L: F_u − ∇·(F_{∇u}) = 0 (PDE) |
| Higher derivatives u'' in F | E-L: F_u − (F_{u'})' + (F_{u''})'' = 0 |
| Free endpoint at x=b | Natural BC: F_{u'}(b) = 0 |
| Check local minimum | Legendre condition: F_{u'u'} ≥ 0 |

---

## Common Confusion Points

**"The E-L equation is only a necessary condition — how do I know the solution is actually
a minimum?"**
The E-L equation says the first variation is zero — analogous to setting ∇f = 0. You
additionally need: (1) Legendre condition F_{u'u'} ≥ 0 (positive semidefiniteness of
second variation), and (2) no conjugate points (Jacobi condition). For many physics
problems the existence of a minimum is clear from physics (bounded-below energy), and the
E-L solution is the unique stationary point, hence the minimum.

**"What does 'stationary' mean — why not just say 'minimum'?"**
In general, δS = 0 identifies all stationary points: minima, maxima, and saddle points.
In Lagrangian mechanics, the physical trajectory is often a saddle point of the action, not
a minimum. This becomes clear for paths longer than the first conjugate point. The term
"stationary" is more honest than "minimum" — Hamilton's principle should be: "the physical
trajectory makes S stationary."

**"The Beltrami identity gives a first integral — is this just energy conservation?"**
Yes, exactly. For L(q,q̇) with no explicit time: the Beltrami identity is
L − q̇·∂L/∂q̇ = const, which is −H = const, i.e., H = const. This IS energy conservation.
Beltrami is just Noether's theorem for time-translation symmetry, applied to the variational
setting.
