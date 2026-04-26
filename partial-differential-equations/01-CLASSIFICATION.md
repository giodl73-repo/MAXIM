# Classification and Well-Posedness

## Why Classification Matters

Classification is not taxonomy — it determines everything downstream:

```
+---------------------------------------------------------------+
|  CLASSIFICATION DETERMINES                                    |
|                                                               |
|  1. WHAT BOUNDARY CONDITIONS ARE APPROPRIATE                  |
|     Elliptic:   data on closed boundary ∂Ω                    |
|     Parabolic:  data at t=0 + spatial boundary                |
|     Hyperbolic: Cauchy data (value + normal derivative)       |
|                                                               |
|  2. HOW INFORMATION PROPAGATES                                |
|     Elliptic:   instantaneously, globally                     |
|     Parabolic:  infinite speed, exponential decay             |
|     Hyperbolic: finite speed (light cones / characteristics)  |
|                                                               |
|  3. WHAT REGULARITY TO EXPECT                                 |
|     Elliptic:   solutions are C∞ in the interior              |
|     Parabolic:  instantly smooth for t > 0                    |
|     Hyperbolic: kinks and discontinuities can persist         |
|                                                               |
|  4. WHICH NUMERICAL METHODS WORK                              |
|     Elliptic:   FEM, BEM, multigrid (no time-stepping)        |
|     Parabolic:  implicit time-stepping, Crank-Nicolson        |
|     Hyperbolic: upwind, Godunov, finite volumes + CFL         |
|                                                               |
+---------------------------------------------------------------+
```

---

## The 2D Second-Order Case

General linear second-order PDE in two variables x, y:

```
  Au_xx + 2Bu_xy + Cu_yy + Du_x + Eu_y + Fu = G

  A, B, C, D, E, F, G may be functions of (x,y).

  PRINCIPAL PART: Au_xx + 2Bu_xy + Cu_yy
  (lower-order terms don't affect classification)

  ASSOCIATED SYMBOL MATRIX:   M = [ A  B ]
                                   [ B  C ]

  DISCRIMINANT:  Δ = B² − AC = −det(M)

  ┌─────────────────────────────────────────┐
  │  Δ < 0  →  ELLIPTIC   (both eigenvalues │
  │            of M have same sign)         │
  │  Δ = 0  →  PARABOLIC  (one eigenvalue   │
  │            of M is zero)                │
  │  Δ > 0  →  HYPERBOLIC (eigenvalues of M │
  │            have opposite signs)         │
  └─────────────────────────────────────────┘

  VERIFICATION on canonical examples:
  Laplace   u_xx + u_yy = 0:  A=1,B=0,C=1  → Δ=−1 < 0  ELLIPTIC
  Heat      u_t  − u_xx  = 0: treat t as y: A=−1,B=0,C=0→ Δ=0=0 PARABOLIC
  Wave      u_tt − u_xx  = 0: A=−1,B=0,C=1 → Δ=1 > 0  HYPERBOLIC
```

---

## Characteristics

Characteristics are curves along which the PDE has **reduced order** — where information
naturally flows. They are the key geometric concept.

```
  For  Au_xx + 2Bu_xy + Cu_yy + ... = 0,
  characteristic curves φ(x,y) = const satisfy:

     A(dφ/dx)² − 2B(dφ/dx)(dφ/dy) + C(dφ/dy)² = 0

  Or equivalently, the family y = y(x) satisfies:
     A(dy/dx)² − 2B(dy/dx) + C = 0
     dy/dx = [B ± √(B²−AC)] / A

  ┌────────────────────────────────────────────────────────────────┐
  │ ELLIPTIC:  B²−AC < 0 → no REAL characteristic curves           │
  │   No preferred propagation direction.                          │
  │   Solutions are smooth (C∞) everywhere in the interior.        │
  │   Think: a soap film — disturb one point, whole film adjusts.  │
  │                                                                │
  │ PARABOLIC: B²−AC = 0 → ONE real characteristic family          │
  │   One degenerate direction.                                    │
  │   For the heat equation: t = const are the characteristics.    │
  │   Information moves "forward" in the degenerate direction.     │
  │                                                                │
  │ HYPERBOLIC: B²−AC > 0 → TWO real characteristic families       │
  │   Two distinct propagation directions.                         │
  │   Wave eq: t − x/c = const and t + x/c = const.                │
  │   Discontinuities travel along characteristics.                │
  └────────────────────────────────────────────────────────────────┘
```

### Wave Equation Characteristics Worked Example

```
  u_tt − c²u_xx = 0

  Characteristic ODE:  −c²(dy)² + (dx)² = 0  (with y=t)
                       dx/dt = ±c
                       → t − x/c = const   (right-moving)
                       → t + x/c = const   (left-moving)

  Change of variables:  ξ = x + ct,  η = x − ct

  Canonical form:  u_ξη = 0

  General solution:  u(ξ,η) = F(ξ) + G(η) = F(x+ct) + G(x−ct)

  This is d'Alembert's formula. The two characteristic families
  are precisely the right-moving and left-moving wave directions.
```

---

## Canonical Forms

By a local change of variables, every 2nd-order linear PDE reduces to:

```
  ELLIPTIC CANONICAL FORM:
      u_ξξ + u_ηη + lower-order = 0   (Laplace-like)

  PARABOLIC CANONICAL FORM:
      u_ξξ + lower-order = 0          (one direction only)

  HYPERBOLIC CANONICAL FORM (first form):
      u_ξη + lower-order = 0          (mixed derivative)

  HYPERBOLIC CANONICAL FORM (wave form):
      u_ξξ − u_ηη + lower-order = 0   (wave-like)

  These two hyperbolic forms are equivalent via ξ = s+r, η = s−r.
```

This is the PDE analogue of putting a quadratic form in diagonal form
(Sylvester's law of inertia).

---

## Higher Dimensions: Principal Symbol

In n independent variables x = (x₁,...,xₙ):

```
  OPERATOR:  L[u] = Σ_{i,j} a_{ij}(x) ∂²u/∂x_i∂x_j + lower-order

  PRINCIPAL SYMBOL:  p(x,ξ) = Σ_{i,j} a_{ij}(x) ξ_i ξ_j = ξᵀ A(x) ξ

  where ξ = (ξ₁,...,ξₙ) is the "frequency" or "covector" variable.

  CLASSIFICATION by eigenvalues of A(x):

  ┌────────────────────────────────────────────────────────────────┐
  │ All eigenvalues same nonzero sign     → ELLIPTIC               │
  │ One zero eigenvalue, rest same sign   → PARABOLIC              │
  │ One eigenvalue opposite sign to rest  → HYPERBOLIC             │
  │ (the "time" direction has opposite sign)                       │
  │ More than one opposite sign           → ULTRAHYPERBOLIC        │
  │ (more than one "time" direction — typically ill-posed)         │
  └────────────────────────────────────────────────────────────────┘

  Connection to Fourier analysis: replace ∂/∂x_j → iξ_j.
  Then L → p(x,ξ) (the symbol). Classification is about the
  sign structure of this quadratic form.
```

---

## Systems of PDEs: Hyperbolicity Revisited

For a first-order system Σ_j A_j ∂u/∂x_j = f:

```
  SYMMETRIC HYPERBOLIC SYSTEM (Friedrichs):
  All A_j are symmetric matrices, A_n is positive definite.

  STRONGLY HYPERBOLIC:
  For all ξ, the matrix Σ A_j ξ_j has real eigenvalues and
  a complete set of eigenvectors.

  Eigenvalues = CHARACTERISTIC SPEEDS.
  Eigenvectors = CHARACTERISTIC VARIABLES (decouple the system).

  EXAMPLES:
  Maxwell's equations:
    ∂B/∂t + ∇×E = 0,  ∂E/∂t − c²∇×B = 0
    → Symmetric hyperbolic system for (E,B).
    Characteristic speeds: 0 (×2 per direction) and ±c (×2).

  Linear elasticity:
    ρ∂²u/∂t² = Σ ∂σ_{ij}/∂x_j   (u = displacement)
    → Symmetric hyperbolic system.
    Characteristic speeds: longitudinal and shear wave speeds.
```

---

## Well-Posedness (Hadamard's Criteria)

```
  A PROBLEM IS WELL-POSED if:
  ┌──────────────────────────────────────────────────────────────┐
  │ 1. EXISTENCE:   at least one solution exists                 │
  │ 2. UNIQUENESS:  at most one solution (unique)                │
  │ 3. STABILITY:   solution depends continuously on data        │
  │                 small changes in BCs/ICs → small solution    │
  │                 changes (in an appropriate norm)             │
  └──────────────────────────────────────────────────────────────┘
```

### Hadamard's Counterexample: Elliptic Cauchy Problem

```
  Problem: u_xx + u_yy = 0 with data on y=0:
      u(x,0) = 0,   u_y(x,0) = ε·sin(nx)

  Solution: u_n(x,y) = (ε/n) sin(nx) sinh(ny)

  As n → ∞:  data → 0  (‖u_y(·,0)‖_∞ = ε → 0 with ε = 1/n)
             but solution → ∞  (‖u_n(·,y)‖ ~ e^{ny}/n → ∞)

  HIGH FREQUENCIES are exponentially amplified.
  → ELLIPTIC CAUCHY PROBLEM IS ILL-POSED.
  → Never specify both u and ∂u/∂n on the same piece of boundary
    for an elliptic problem.
```

### Parabolic: Forward vs. Backward

```
  FORWARD HEAT:   u_t − u_xx = 0, u(x,0) = u₀(x)
  Solution:       u(x,t) = ∫ K(x−y,t) u₀(y) dy
                  where K(z,t) = (4παt)^{−1/2} e^{−z²/4αt}  (heat kernel)
  → WELL-POSED. Smoothes instantly. Energy decays.

  BACKWARD HEAT:  u_t + u_xx = 0 (run time backward)
  Or equivalently: recover u(x,0) from u(x,T).

  Mode analysis: u = e^{inx} has time evolution e^{n²t}.
  At t=T: u ~ e^{n²T}.  Inverting: multiply by e^{−n²T}.
  For large n: e^{n²T} → ∞ catastrophically.

  → ILL-POSED. Appears in: image deblurring, data assimilation,
    inverse heat problems, geothermal exploration.
    Solved in practice with Tikhonov regularization.
```

### Hyperbolic Well-Posedness

```
  WAVE EQUATION CAUCHY PROBLEM:
      u_tt − c²u_xx = 0,  u(x,0) = u₀,  u_t(x,0) = v₀

  d'Alembert solution:
      u(x,t) = ½[u₀(x+ct) + u₀(x−ct)] + 1/(2c) ∫_{x−ct}^{x+ct} v₀(s) ds

  → WELL-POSED. Energy is conserved:
      E(t) = ½ ∫ [u_t² + c²u_x²] dx = E(0)

  Note: regularity NOT improved.
  If u₀ has a jump discontinuity, that jump travels forever.
  This is physical: shocks persist in wave problems.
```

---

## Energy Methods: The Universal Tool

Energy estimates are the workhorse of PDE theory:

```
  PARABOLIC ENERGY ESTIMATE:

  Multiply heat equation u_t = α·u_xx by u, integrate over [0,L]:

  d/dt ∫₀ᴸ u²/2 dx = α ∫₀ᴸ u·u_xx dx
                    = α [u·u_x]₀ᴸ − α ∫₀ᴸ u_x² dx
                    = −α ∫₀ᴸ u_x² dx  (with Dirichlet BC: u=0 at ends)
                    ≤ 0

  So: ‖u(·,t)‖²_L² ≤ ‖u₀‖²_L²  (energy decreases — dissipation)

  Uniqueness follows: if u₁, u₂ both solve the same problem,
  w = u₁ − u₂ solves w_t = αw_xx with w(x,0) = 0.
  Energy estimate → ‖w(·,t)‖ = 0 → w ≡ 0.

  HYPERBOLIC ENERGY ESTIMATE:

  Multiply wave equation u_tt = c²u_xx by u_t, integrate:

  d/dt ½ ∫ [u_t² + c²u_x²] dx = 0

  Energy E(t) is CONSERVED (no dissipation).
  Same trick proves uniqueness.
```

---

## Maximum Principles

For elliptic and parabolic problems:

```
  ELLIPTIC (STRONG) MAXIMUM PRINCIPLE:

  If Lu = Σ a_{ij} u_{x_ix_j} + Σ b_i u_{x_i} ≥ 0 in Ω (connected),
  and u achieves its maximum at an interior point,
  then u is constant.

  COROLLARIES:
  • Harmonic function (∇²u = 0): max and min only on ∂Ω.
  • Uniqueness for Dirichlet: if ∇²u=0 and u=0 on ∂Ω then u≡0.
  • Comparison: if ∇²u ≥ ∇²v and u ≤ v on ∂Ω, then u ≤ v in Ω.
  • Mean value property: u(x₀) = avg u on any sphere around x₀.

  PARABOLIC MAXIMUM PRINCIPLE:

  If u_t − L[u] ≤ 0 in Ω × (0,T), the maximum is achieved
  on the PARABOLIC BOUNDARY:
      Γ = (Ω × {0}) ∪ (∂Ω × [0,T])
  (initial time slice or lateral boundary — NOT the top t=T).

  Physical meaning: temperature peaks come from past boundary
  data. The future cannot "cause" a higher temperature inside.
```

---

## Lax-Milgram: Elliptic Existence Theory

```
  LAX-MILGRAM THEOREM:

  Let V be a Hilbert space with norm ‖·‖_V.
  Let a: V × V → R be a bilinear form satisfying:
    CONTINUITY:  |a(u,v)| ≤ M ‖u‖_V ‖v‖_V    for some M > 0
    COERCIVITY:  a(u,u) ≥ α ‖u‖²_V             for some α > 0

  Then for every F ∈ V*, there exists UNIQUE u ∈ V such that:
      a(u,v) = F(v)  for all v ∈ V.

  APPLICATION TO POISSON:
    Problem:    −∇²u = f in Ω,  u = 0 on ∂Ω
    Weak form:  ∫_Ω ∇u·∇v dx = ∫_Ω fv dx  for all v ∈ H₀¹(Ω)
    Here:       a(u,v) = ∫_Ω ∇u·∇v dx,  F(v) = ∫_Ω fv dx
    V = H₀¹(Ω),  ‖u‖_V = (∫|∇u|²)^{1/2}
    Coercivity:  from Poincaré inequality ∫|∇u|² ≥ C∫|u|²
    → Unique weak solution exists.

  This is the theoretical foundation of the Finite Element Method.
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What BCs for Laplace / Poisson? | Dirichlet, Neumann, or Robin on entire ∂Ω |
| Can I give both u and ∂u/∂n for Laplace on a curve? | No — ill-posed (Hadamard example) |
| What BCs for heat equation? | IC u(x,0)=u₀ + spatial BCs for all t>0 |
| Why is backward heat equation ill-posed? | High-freq modes grow as e^{n²T} |
| Why does wave equation need two ICs? | Second-order in t → two free constants per mode |
| What is a characteristic? | Curve along which PDE reduces order; info travels along them |
| What is domain of dependence? | Set of ICs that determine u(x₀,t₀) — a cone for hyperbolic |
| How to prove uniqueness for a PDE? | Assume two solutions, subtract, prove difference is zero by energy estimate |
| What is Lax-Milgram used for? | Proving existence and uniqueness of weak (FEM) solutions |

---

## Common Confusion Points

**"Parabolic is 'between' elliptic and hyperbolic?"**
Exactly right. The discriminant Δ = B²−AC traces a continuous path:
Δ < 0 (elliptic) → Δ = 0 (parabolic) → Δ > 0 (hyperbolic).
Physically: diffusion with faster and faster wave speed → as wave speed → ∞, the hyperbolic
wave equation degenerates into the instantaneous-propagation elliptic equation; parabolic
sits at the boundary with infinite speed but finite diffusion.

**"What's the difference between strong and weak maximum principle?"**
Weak: max cannot be in the interior unless achieved on the boundary.
Strong: if max is achieved at ANY interior point, the function is constant everywhere.
Strong version requires connectivity of the domain and a non-degenerate operator.

**"How does ill-posedness appear computationally?"**
Run backward heat numerically with no regularization: each time step amplifies errors
exponentially. The computation diverges. Regularization (adding small forward diffusion,
truncating high modes) makes it tractable — at the cost of resolution. This tradeoff
(stability vs. resolution) is the central tension of inverse problem computation.
