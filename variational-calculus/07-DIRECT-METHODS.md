# Direct Methods and Sobolev Spaces

## The Big Picture

The Euler-Lagrange equation is a *necessary* condition for an extremum, but doesn't guarantee
that a minimizer exists. **Direct methods** prove existence by working directly with minimizing
sequences, bypassing the E-L equation entirely.

```
+-----------------------------------------------------------------------+
|              DIRECT METHODS CONCEPT                                   |
|                                                                       |
|  CLASSICAL APPROACH:                                                  |
|  1. Derive E-L equation.                                              |
|  2. Solve E-L to find candidate minimizer.                            |
|  3. Verify it's actually a minimum.                                   |
|  PROBLEM: E-L may have no smooth solution. Existence not guaranteed.  |
|                                                                       |
|  DIRECT METHODS (Tonelli, 1910s):                                     |
|  1. Show J[u] is bounded below (infimum exists).                      |
|  2. Take minimizing sequence: u_n with J[u_n] → inf J.                |
|  3. Extract convergent subsequence (compactness).                     |
|  4. Show J is lower semicontinuous: J[u*] ≤ lim inf J[u_n].         |
|  5. Conclude: J[u*] = inf J — the minimizer exists.                   |
|                                                                       |
|  ANALOGY: In Rⁿ, min of f on compact set K exists by EVT.           |
|  Direct methods: replace "compact set" by "weakly compact" set in   |
|  Sobolev space, and "continuous" by "weakly lower semicontinuous."    |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## Why Classical Existence Fails

### The Weierstrass Non-Existence Example (1870)

```
  PROBLEM: Minimize J[u] = ∫₋₁¹ x²(u')² dx
  subject to u(−1) = −1, u(1) = 1.

  The infimum is 0. Why?

  MINIMIZING SEQUENCE:
  u_n(x) = arctan(nx)/arctan(n)

  u_n(−1) = −1, u_n(1) = 1. ✓

  J[u_n] = ∫₋₁¹ x² · [n/((n²x²+1)arctan(n))]² dx → 0  as n→∞.

  BUT: u_n converges to the step function u*(x) = sign(x),
  which is NOT in the space of smooth functions,
  and (u*)' = 2δ(x), so J[u*] is not well-defined classically.

  LESSON: Infimum is achieved only in a LARGER SPACE (Sobolev, BV).
  Classical smooth minimizers don't always exist.
  Must work in the right function space.
```

---

## Sobolev Spaces: The Right Setting

Sobolev spaces provide the natural habitat for variational problems:

```
  W^{k,p}(Ω):  {u ∈ L^p(Ω) : D^α u ∈ L^p(Ω) for |α| ≤ k}

  NORM: ‖u‖_{W^{k,p}} = (Σ_{|α|≤k} ‖D^α u‖^p_{L^p})^{1/p}

  SPECIAL CASES:
  W^{0,p} = L^p(Ω)
  W^{1,2} = H¹(Ω)  [the most important for variational problems]
  W^{1,1}(Ω) = BV(Ω) — functions of bounded variation (closure)

  W₀^{k,p}(Ω): closure of C_c^∞(Ω) — functions with zero boundary trace.

  KEY PROPERTIES:
  ┌──────────────────────────────────────────────────────────────────┐
  │ REFLEXIVITY: W^{k,p} is reflexive for 1 < p < ∞.               │
  │   → Every bounded sequence has a weakly convergent subsequence.  │
  │   (This is the key compactness property for direct methods.)     │
  │                                                                  │
  │ SOBOLEV EMBEDDING: if k − n/p > j, then W^{k,p} ↪ C^j.        │
  │   n=3, p=2: H¹ ↪ L^6  (into Lebesgue spaces)                  │
  │             H² ↪ C⁰  (into continuous functions)               │
  │                                                                  │
  │ RELLICH-KONDRACHOV: if q < p* = np/(n−p), W^{1,p}↪↪ L^q      │
  │   (compactly embedded — bounded sequences converge strongly)     │
  │                                                                  │
  │ POINCARÉ INEQUALITY: ‖u‖_L^p ≤ C ‖∇u‖_L^p for u ∈ W₀^{1,p}  │
  │   → ‖∇u‖ alone controls ‖u‖ — coercivity follows.             │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Weak Convergence and Weak Lower Semicontinuity

```
  WEAK CONVERGENCE in Banach space X:
  u_n ⇀ u  (weakly) if  ⟨φ, u_n⟩ → ⟨φ, u⟩  for all φ ∈ X*.

  Example: In H¹(Ω):
  u_n ⇀ u  iff  ∫ u_n v dx → ∫ u v dx and ∫ ∇u_n · ∇v dx → ∫ ∇u · ∇v dx
  for all v ∈ H¹.

  KEY FACT: In reflexive Banach spaces, bounded sequences have
  weakly convergent subsequences.
  (Banach-Alaoglu theorem)

  WEAK LOWER SEMICONTINUITY (wlsc):
  J is wlsc if: u_n ⇀ u  →  J[u] ≤ lim inf J[u_n].

  THIS IS THE CRITICAL PROPERTY FOR DIRECT METHODS.
  (Stronger than continuity would allow: limit of J's could overshoot.)

  Note: wlsc is WEAKER than continuity. Many functionals that are NOT
  weakly continuous ARE weakly lower semicontinuous.
```

---

## Convexity and Lower Semicontinuity

```
  THEOREM (Tonelli-Morrey):
  For J[u] = ∫_Ω F(x, u, ∇u) dx:

  F convex in (u, ∇u) → J is weakly lower semicontinuous in W^{1,p}.

  More precisely: if F(x, u, A) is convex in A (for each fixed x,u),
  then J is wlsc in W^{1,p}.

  PROOF SKETCH:
  u_n ⇀ u weakly. ∇u_n ⇀ ∇u weakly.
  By convexity of F in A:
  F(x, u, ∇u) ≤ F(x, u, ∇u_n) + D_A F(x,u,∇u)·(∇u−∇u_n)

  Integrate, take lim inf:
  ∫F(x,u,∇u) ≤ lim inf ∫F(x,u,∇u_n) + D_A F · (∇u − weak limit ∇u_n)
  = lim inf J[u_n] + 0   (the last term → 0 by weak convergence)  ■

  NON-CONVEX F: need QUASICONVEXITY (Morrey 1952):
  F is quasiconvex if: ∫_{[0,1]^n} F(A+∇η) ≥ F(A) for all η ∈ W₀^{1,∞}.
  Quasiconvexity ↔ J is weakly lower semicontinuous.
  Convexity ⟹ Quasiconvexity ⟹ Rank-one convexity.
  None of the reverses hold in general (Šverák, 1993).
```

---

## The Fundamental Theorem of Direct Methods

```
  THEOREM: J[u] has a minimizer on V = {u ∈ W^{1,p}: u|_{∂Ω} = g} if:

  1. COERCIVITY:      J[u_n] → ∞ whenever ‖u_n‖_{W^{1,p}} → ∞
                      (no escape to infinity)

  2. WLSC:           J is weakly lower semicontinuous in W^{1,p}
                      (limit infimum ≤ infimum of sequence)

  PROOF:
  Let m = inf_{u∈V} J[u] > −∞ (bounded below from coercivity).
  Take minimizing sequence u_n: J[u_n] → m.
  u_n is bounded in W^{1,p} (from coercivity).
  Reflexivity → subsequence u_{n_k} ⇀ u* weakly in W^{1,p}.
  wlsc: J[u*] ≤ lim inf J[u_{n_k}] = m.
  Also J[u*] ≥ m (m is the infimum).
  Conclusion: J[u*] = m — minimizer exists!  ■
```

---

## Growth Conditions and Coercivity

```
  COERCIVITY OF F:
  J[u] = ∫_Ω F(x,u,∇u) dx is coercive if:
  J[u] → ∞ as ‖u‖_{W^{1,p}} → ∞.

  SUFFICIENT: F(x,u,A) ≥ α|A|^p − β  for some α>0, β≥0.
  Then J[u] ≥ α∫|∇u|^p − β|Ω| ≥ α‖u‖^p_{W^{1,p}/C} − const.

  p-GROWTH CONDITIONS:
  Standard assumption: c₁|A|^p − C ≤ F(x,u,A) ≤ c₂(|A|^p + 1)
  p = 2: natural for L² theory, linear elliptic PDEs
  p = 1: total variation regularization (BV functions, L1 TV)
  p → ∞: Lipschitz, Chebyshev approximation
  1 < p < ∞: natural for nonlinear PDEs (p-Laplacian)

  p-LAPLACIAN (prototype nonlinear elliptic):
  J[u] = ∫|∇u|^p dx,  minimizer satisfies:
  −Δ_p u = −div(|∇u|^{p-2}∇u) = 0

  p=2: ordinary Laplacian
  p=1: total variation (edge-preserving image denoising, ROF model)
  p=∞: Lipschitz extension (infinity-Laplacian)
```

---

## Non-Existence and Relaxation

When direct methods fail (non-quasiconvex F), minimizers may not exist:

```
  NON-EXISTENCE EXAMPLE: F(A) = (|A|² − 1)² on R (1D)
  J[u] = ∫₀¹ (u'² − 1)² dx, u(0) = u(1) = 0.

  Infimum = 0 (never achieved):
  Minimizing sequence: u_n(x) = piecewise linear zig-zag with slope ±1.
  J[u_n] = 0, but limit function u* ≡ 0 has J[u*] = 1.
  No minimizer in W^{1,∞}.

  RELAXATION: replace F by its quasiconvex envelope QF:
  QF(A) = inf_{η ∈ W₀^{1,∞}} ∫_{[0,1]^n} F(A+∇η)

  The relaxed problem with QF has a minimizer.
  For 1D: QF = convex hull of F.
  For vector-valued: quasiconvex hull ≠ convex hull in general.

  PHYSICAL INTERPRETATION:
  Non-convex energies → microstructure.
  The zig-zag minimizing sequence corresponds to fine-scale oscillations
  (microstructure in elastic crystals, shape-memory alloys).
  The relaxed problem describes the macroscopic (averaged) behavior.
```

---

## Gamma-Convergence

A notion of convergence for functionals, handling dimension reduction and homogenization:

```
  J_ε Γ-converges to J₀ if:

  (1) LOWER BOUND: if u_ε → u, then J₀[u] ≤ lim inf J_ε[u_ε]
  (2) UPPER BOUND (recovery): for all u, ∃u_ε → u with
      J_ε[u_ε] → J₀[u]

  KEY THEOREM: if J_ε Γ-converges to J₀ and u_ε minimize J_ε,
  then u_ε converge to minimizer of J₀.

  APPLICATIONS:
  • HOMOGENIZATION: J_ε[u] = ∫ F(x/ε, ∇u) dx (rapidly oscillating coeff.)
    Γ-limit = ∫ F_hom(∇u) dx  (effective homogeneous medium)
  • PHASE TRANSITIONS: Modica-Mortola functional
    J_ε[u] = ∫[ε|∇u|² + W(u)/ε] dx
    Γ-limit = perimeter functional ∫|∇u| (phase interfaces)
  • BRITTLE FRACTURE: Ambrosio-Tortorelli approximation of crack energy.
  • MACHINE LEARNING: deep networks as Γ-limits of shallow networks??
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Does a minimizer exist? | Check coercivity + weak lower semicontinuity |
| F convex in ∇u → wlsc? | Yes (Tonelli-Morrey) |
| F non-convex → wlsc? | Need quasiconvexity (stronger condition) |
| Minimizing sequence bounded? | Yes, from coercivity |
| Weak convergence + wlsc → ? | J[u*] ≤ lim inf J[u_n] → u* is a minimizer |
| Minimizer doesn't exist — what then? | Relaxation (quasiconvex envelope); microstructure |
| Perturbed/scaled functionals → limit? | Γ-convergence gives the right limit problem |
| Sobolev embedding in 3D? | H¹ ↪ L^6, H² ↪ C⁰ |

---

## Common Confusion Points

**"Weak convergence vs. strong convergence — what's the practical difference?"**
Strong: u_n → u means ‖u_n − u‖ → 0. The functions actually get close pointwise (in some
average sense). Weak: u_n ⇀ u means only ∫u_n v → ∫ u v for all test functions v. Weak
convergence is much more permissive — for example, sin(nx) ⇀ 0 weakly in L² (oscillations
average out) but ‖sin(nx)‖ = 1/√2 ≠ 0 (does NOT converge strongly).

**"If J is wlsc and we have a weakly convergent minimizing sequence, why don't we get
equality J[u*] = lim J[u_n] (instead of just ≤)?"**
Because wlsc says J[u*] ≤ lim inf. We also have J[u_n] → inf J ≤ J[u*] (since u* is
admissible). So J[u*] ≤ inf J ≤ J[u*] → J[u*] = inf J = lim J[u_n]. It works out to
equality, but you need both the ≤ from wlsc AND the ≥ from u* being admissible.

**"The Weierstrass example: the infimum is 0 but no minimizer achieves it. Why not just
say inf is achieved by a 'generalized function'?"**
That's exactly what happens in Sobolev theory. The step function sign(x) is in L^∞ but
not in H¹ (it has a derivative that's a delta function, not in L²). If you work in BV
(bounded variation space), you can achieve the infimum — but BV is not a reflexive Banach
space, so the standard direct method needs modification (use weak* convergence instead).
The point is: the space you work in determines what minimizers exist.
