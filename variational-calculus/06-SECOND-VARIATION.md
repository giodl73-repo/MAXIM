# Second Variation and Stability

## The Big Picture

The Euler-Lagrange equation identifies stationary points of a functional — but not whether
they are minima, maxima, or saddle points. The second variation is the functional analogue
of the Hessian matrix.

```
+-----------------------------------------------------------------------+
|              FIRST vs. SECOND VARIATION                               |
|                                                                       |
|  FUNCTION f: R^n → R             FUNCTIONAL J: V → R                  |
|  ─────────────────────────       ─────────────────────                |
|  f(x+v) ≈ f(x) + ∇f·v + ½vᵀHv  J[u+εη] ≈ J[u] + εδJ + ½ε²δ²J   |
|  Stationary: ∇f = 0              Stationary: δJ = 0                   |
|  Local min:  H ≻ 0               Local min: δ²J > 0  (all η≠0)        |
|  (positive definite Hessian)     (positive second variation)          |
|  Local max:  H ≺ 0               Local max: δ²J < 0                   |
|  Saddle:     H indefinite        Saddle: δ²J changes sign             |
|                                                                       |
|  ADDITIONAL COMPLICATION in infinite dimensions:                      |
|  "Positive second variation" does NOT guarantee global minimum.       |
|  Require: coercivity, lower semicontinuity for global results.        |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## Computing the Second Variation

For J[u] = ∫ₐᵇ F(x, u, u') dx:

```
  EXPAND J[u+εη] to 2nd order in ε:

  J[u+εη] = ∫ F(x, u+εη, u'+εη') dx

  Taylor expand F in ε:
  F(x, u+εη, u'+εη') = F(x,u,u')
    + ε[F_u η + F_{u'} η']
    + ½ε²[F_{uu} η² + 2F_{uu'} ηη' + F_{u'u'} η'²] + O(ε³)

  SECOND VARIATION:
  δ²J[u;η] = ∫ₐᵇ [F_{uu} η² + 2F_{uu'} ηη' + F_{u'u'} η'²] dx

  INTEGRATE BY PARTS (optional):
  Using η η' = (η²)'/2 and integration by parts on the F_{uu'} term:
  δ²J = ∫ₐᵇ [(F_{uu} − (F_{uu'})') η² + F_{u'u'} η'²] dx
       = ∫ₐᵇ [P(x) η² + Q(x) η'²] dx

  where P = F_{uu} − d/dx F_{uu'},  Q = F_{u'u'}.
```

---

## Legendre Condition: Necessary for Minimum

```
  LEGENDRE NECESSARY CONDITION for local minimum:

  Q(x) = F_{u'u'} ≥ 0   for all x ∈ [a,b]

  PROOF BY CONTRADICTION:
  Suppose Q(x₀) < 0 for some x₀.
  Choose η concentrated near x₀: η_ε(x) = η(x/ε)/√ε.
  The η'² term dominates as ε → 0:
  δ²J[u;η_ε] ≈ Q(x₀) ∫ η'² → Q(x₀) · C < 0.
  So δ²J < 0 for some η → not a minimum.

  STRICT LEGENDRE CONDITION:
  Q(x) = F_{u'u'} > 0   for all x ∈ [a,b]
  (strictly positive — sometimes needed for stronger results)

  PHYSICAL MEANING:
  For L = ½mq̇² − V(q):  F_{u'u'} = m > 0. ✓
  For L = ½mq̇² + V(q) (wrong sign):  This would give a maximum.
  The kinetic energy term must be positive for a minimum.
```

---

## Jacobi Equation and Conjugate Points

The Legendre condition is necessary but NOT sufficient. The Jacobi condition provides
the additional requirement:

```
  JACOBI EQUATION:
  For the quadratic functional Q[η] = δ²J[u;η] = ∫(P η² + Q η'²)dx,
  the corresponding E-L equation is:

  −d/dx(Q η') + P η = 0     (JACOBI EQUATION)
  or:  −(Q η')' + P η = 0

  This is a 2nd-order ODE for η(x), arising from minimizing δ²J.

  CONJUGATE POINTS:
  A CONJUGATE POINT to a is a point x* ∈ (a,b] such that the
  Jacobi equation has a nontrivial solution η with η(a) = η(x*) = 0.

  JACOBI CONDITION (necessary for strong local minimum):
  There is no conjugate point in (a,b).
  Equivalently: the only solution to the Jacobi equation with η(a)=0
  that vanishes again in (a,b] is η ≡ 0.

  PICTURE:
  a ──────────────────── b  (no conjugate point: OK)
  a ──────── x* ───── b     (conjugate point at x*: NOT a local min)

  If x* ∈ (a,b): a nearby curve J[u_ε] < J[u] exists → u not a min.
  If x* = b: borderline case (may be weak minimum).
```

### Relationship to Sturm-Liouville

```
  The Jacobi equation −(Qη')' + Pη = 0 is a STURM-LIOUVILLE equation.

  Eigenvalue problem: −(Qη')' + Pη = λη on [a,b] with η(a)=η(b)=0.

  NO CONJUGATE POINTS ↔ SMALLEST EIGENVALUE λ₁ > 0.

  This connects: second-order stability ↔ positivity of S-L operator.

  COMPUTATIONAL: Check whether the Jacobi equation initial value problem
    η'' + ... = 0,  η(a) = 0,  η'(a) = 1
  has a zero in (a,b). The first zero, if it exists, is the first
  conjugate point.
```

---

## Complete Conditions for a Weak Local Minimum

```
  WEAK LOCAL MINIMUM (local in the C¹ topology):
  ┌──────────────────────────────────────────────────────────────┐
  │ SUFFICIENT CONDITIONS:                                       │
  │ 1. E-L equation satisfied (δJ = 0)                           │
  │ 2. Strict Legendre: F_{u'u'} > 0 on [a,b]                    │
  │ 3. No conjugate points in (a,b)                              │
  │                                                              │
  │ These three conditions TOGETHER are sufficient for u to be   │
  │ a strict weak local minimum.                                 │
  └──────────────────────────────────────────────────────────────┘

  NECESSARY CONDITIONS (for any local minimum):
  1. E-L equation (δJ = 0)
  2. Legendre: F_{u'u'} ≥ 0
  3. No conjugate points in (a,b) (open interval)

  DIFFERENCE BETWEEN WEAK AND STRONG:
  Weak: nearby in C¹ norm (both u and u' close to the minimum).
  Strong: nearby in C⁰ norm (u close, but u' possibly different).
  Strong minimum requires: Weierstrass E-function E(x,u,u',q)=
  F(x,u,q)−F(x,u,u')−(q−u')F_{u'}(x,u,u') ≥ 0 for all q.
```

---

## Physical Interpretation: Stability of Equilibria

```
  MECHANICS: u(t) = equilibrium position, q*

  E-L equation: force balance (static equilibrium).
  Second variation: stability of the equilibrium.

  δ²S[q*; η] > 0 ↔ q* is a stable equilibrium (potential energy minimum)

  EXAMPLE: ball on a hillside
  V(q):
       /\
      /  \___
     /       \___
  ─────────────────→ q
      min    max

  At minimum: V''(q*) > 0 → F_{u'u'} = m > 0, P = V''(q*) > 0
  Second variation > 0 → stable equilibrium.

  At maximum: V''(q*) < 0 → P < 0
  Second variation indefinite → unstable equilibrium.

  CLASSICAL FIELD THEORY:
  Stability of a field configuration φ(x):
  δ²S[φ; δφ] > 0 → stable (no tachyonic modes)
  If some η has δ²S < 0 → unstable (perturbation grows exponentially)
```

---

## Conjugate Points in Mechanics

In Lagrangian mechanics, conjugate points are related to caustics:

```
  DEFINITION IN MECHANICS:
  t* is conjugate to t₁ along a trajectory q(t) if there exists
  a "Jacobi field" J(t) (solution to linearized equations of motion)
  with J(t₁) = J(t*) = 0.

  PHYSICAL MEANING:
  Two nearby trajectories emanating from q(t₁) meet again at t*.
  In optics: this is a CAUSTIC (where rays focus).
  In quantum mechanics: the WKB approximation breaks down at conjugate points.

  MASLOV INDEX:
  When the trajectory passes through conjugate points, the wavefunction
  accumulates a phase shift of π/2 per conjugate point.
  The total phase accumulation is counted by the Maslov index.
  This appears in the Gutzwiller trace formula (semiclassical periodic orbits).

  APPLICATIONS:
  • Optics: ray caustics (rainbows, lens aberrations)
  • Seismology: focusing of seismic waves
  • Orbital mechanics: Lagrange points and gravitational focusing
  • Quantum chaos: semiclassical periodic orbit theory
```

---

## Second Variation for Multiple Variables

For J[u] = ∫_Ω F(x, u, ∇u) dx:

```
  SECOND VARIATION:
  δ²J[u;η] = ∫_Ω [F_{uu}η² + 2F_{u,∇u}·η∇η + ∇ηᵀ F_{∇u,∇u} ∇η] dx

  LEGENDRE-HADAMARD CONDITION (necessary for minimum):
  Σᵢⱼ ∂²F/∂(∂u/∂xᵢ)∂(∂u/∂xⱼ) ξᵢξⱼ ≥ 0   for all ξ ∈ R^n

  (Positivity in each direction in x-space)

  RANK-ONE CONVEXITY:
  F(∇u) is rank-one convex if t → F(A + t ξ⊗η) is convex for all ξ,η.
  Weaker than convexity of F, but necessary for local minimum.

  QUASICONVEXITY (Morrey, 1952):
  ∫_{[0,1]^n} F(A + ∇η) dx ≥ F(A)|[0,1]^n|   for all η ∈ W₀^{1,∞}
  This is the correct condition for existence of minimizers in
  multiple dimensions (weak lower semicontinuity).
```

---

## Morse Theory: Topology from Critical Points

The second variation connects to deep topology:

```
  MORSE THEORY (Morse, 1925):
  The topology of a manifold is encoded in the critical points of
  any smooth function (or functional).

  MORSE INDEX μ(u):
  The number of negative eigenvalues of the second variation at
  a critical point u (= dimension of the "descending manifold").

  μ = 0: local minimum
  μ = 1: saddle point (one negative direction)
  μ = k: k negative directions

  MORSE INEQUALITIES:
  If M_k = number of critical points of index k, and b_k = Betti numbers of M:
  M_k ≥ b_k (and alternating sum: Σ (−1)^k M_k = χ(M) = Euler characteristic)

  APPLICATIONS TO PDEs:
  Critical points of functionals on function spaces → solutions of PDEs.
  Morse theory gives: multiplicity of solutions, topology of solution spaces.

  Floer homology: Morse theory on infinite-dimensional manifolds,
  applied to Hamiltonian mechanics and gauge theory (led to gauge theory
  proofs of 4-manifold topology results by Donaldson-Witten).
```

---

## Decision Cheat Sheet

| Question | Tool |
|----------|------|
| Is the E-L solution a minimum? | Check second variation > 0 |
| Necessary condition for minimum? | Legendre: F_{u'u'} ≥ 0 |
| Sufficient condition for weak local min? | Strict Legendre + no conjugate points |
| Conjugate point exists? | Jacobi equation has a zero in (a,b) |
| Stability of equilibrium? | Second variation of potential > 0 |
| Global minimum vs. local? | Need coercivity + lower semicontinuity (direct methods) |
| Multiple solutions to E-L? | Morse theory counts them via Morse index |

---

## Common Confusion Points

**"The Legendre condition F_{u'u'} > 0 is necessary AND the Jacobi condition. Why both?"**
Legendre ensures the second variation is bounded below locally (no rapid oscillation
instability). Jacobi ensures no "focusing" of nearby trajectories in the domain. Both
can fail independently: Legendre can hold but conjugate points exist (harmonic oscillator
beyond half-period), or Legendre can fail directly.

**"Action in mechanics: is it always a minimum?"**
No. For a harmonic oscillator, action is a minimum for paths shorter than the period T,
but at t = T/2 there is a conjugate point, and for t > T/2 the action is a saddle.
The "principle of least action" should be "principle of stationary action."

**"What does the Maslov index have to do with quantum mechanics?"**
In the WKB (semiclassical) approximation, the wavefunction is ψ ≈ A(x) e^{iS(x)/ℏ}.
Near conjugate points, the amplitude A blows up (caustic) and the approximation breaks
down. After passing through a caustic, ψ picks up a phase shift of e^{-iπ/2} (one factor
per conjugate point). The Maslov index counts conjugate points, determining the quantum
phase shift of semiclassical wavefunctions. This appears in Bohr-Sommerfeld quantization:
∮ p dq = (n + μ/4)·2πℏ where μ is the Maslov index.
