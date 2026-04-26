# Riemann Surfaces

## The Big Picture

Riemann surfaces are the natural habitat for multi-valued functions. Instead of forcing a choice of branch cut — and living with the discontinuity — you build a new topological space where the function is genuinely single-valued. A Riemann surface is a 1-complex-dimensional manifold: locally it looks like ℂ, but globally it may have nontrivial topology. From the MIT topology background: Riemann surfaces are oriented 2-manifolds (topological surfaces) equipped with complex analytic structure.

```
RIEMANN SURFACES — CONCEPTUAL MAP
═══════════════════════════════════════════════════════════════════════════════

  PROBLEM: log z, √z, z^{1/3} are multi-valued in ℂ
           Forcing a single value requires branch cuts with discontinuities

  SOLUTION: Build a surface S where f: S → ℂ is single-valued
            S looks like ℂ near every point but wraps around globally

  ┌─────────────────────────────────────────────────────────────────────┐
  │  RIEMANN SURFACE FOR √z                                             │
  │                                                                     │
  │  Two sheets: Sheet 1 (√z > 0), Sheet 2 (−√z)                      │
  │  Glued along branch cut (−∞, 0]                                     │
  │  Topology: cylinder ≅ ℂ* (punctured plane)                          │
  │  One loop in ℂ \ {0} → need to go around TWICE to return to start   │
  └─────────────────────────────────────────────────────────────────────┘

  CLASSIFICATION BY GENUS:
  g = 0   Riemann sphere ℙ¹ ≅ S²  (compact, simply connected)
  g = 1   Torus ℂ/Λ  (elliptic curves; doubly periodic functions)
  g ≥ 2   Higher genus (hyperbolic, universal cover = upper half-plane)

  KEY THEOREM: Every compact Riemann surface is algebraic
               (given by a polynomial equation F(w, z) = 0)
```

---

## What is a Riemann Surface?

**Definition**: A Riemann surface S is a connected Hausdorff topological space equipped with a **complex analytic atlas**: a collection of homeomorphisms (charts) φᵢ: Uᵢ → Vᵢ ⊂ ℂ covering S, such that all transition maps φⱼ ∘ φᵢ⁻¹ are holomorphic where defined.

This means: S looks like a piece of ℂ near every point (local coordinate charts), and the ways charts overlap are holomorphic (not just smooth or continuous).

**Equivalent description**: A Riemann surface is an oriented 2-real-dimensional manifold with a conformal structure — equivalently, a complex 1-manifold.

```
RIEMANN SURFACE ATLAS:
        Uᵢ ──φᵢ──→ Vᵢ ⊂ ℂ
        ↑                      transition map φⱼ∘φᵢ⁻¹
        Uᵢ∩Uⱼ ──→ φᵢ(Uᵢ∩Uⱼ) ──holomorphic──→ φⱼ(Uᵢ∩Uⱼ)
```

Key examples:
- ℂ itself (one chart, identity map)
- ℂ ∪ {∞} (Riemann sphere, two charts)
- Any open subset of ℂ
- Complex tori ℂ/Λ
- Algebraic curves {(z,w): F(z,w) = 0} in ℂ²

---

## Multi-Valued Functions and Their Riemann Surfaces

### The Logarithm: log z

In ℂ, log z = ln|z| + i arg(z) is multi-valued because arg(z) is defined modulo 2π.

The Riemann surface for log z consists of **infinitely many sheets**, one for each integer k corresponding to the branch arg(z) + 2πk:

```
RIEMANN SURFACE FOR LOG z:

  Sheets: ...  S_{-1},  S₀,  S₁,  S₂,  ...
          each a copy of ℂ \ {0}

  Gluing: going around z=0 once CCW moves you from Sₖ to S_{k+1}

  Total space: "infinite helix" — no periodicity
  Topology:  ℂ (the infinite helix is simply connected and looks like ℂ)

  On this surface: log z is single-valued
```

### The Square Root: √z

The Riemann surface for √z has **two sheets**:

- Sheet 1: principal branch, Im(√z) ≥ 0
- Sheet 2: other branch, Im(√z) < 0

```
RIEMANN SURFACE FOR √z (two sheets):

  Sheet 1  ══════════════╗
           (cut along ℝ₋) ║
  Sheet 2  ══════════════╝  glued along negative real axis

  Going around z=0 once: Sheet 1 → Sheet 2
  Going around twice:    Sheet 2 → Sheet 1  (back to start)

  Branch points: z=0 and z=∞  (monodromy permutes the two values)
  Topology: ℂ ∪ {∞} with two branch points removed, then compactified
            → Riemann sphere (genus 0)
```

### General Algebraic Functions: w² = P(z)

For w² = (z−a₁)(z−a₂)···(z−a_{2n}): a two-sheeted surface with branch points at a₁,...,a_{2n} and ∞ (if 2n is odd, ∞ is also a branch point). Topological genus = n−1.

For the elliptic curve w² = (z−a₁)(z−a₂)(z−a₃)(z−a₄): genus 1 (a torus).

---

## Branch Points and Branch Cuts

**Branch point**: A point a where analytic continuation along a loop around a returns a different value of f. The loop is not contractible in the Riemann surface sense.

**Branch cut**: A curve removed from ℂ to make a specific branch single-valued. The choice is conventional.

```
STANDARD BRANCH CUTS:
  log z:   cut along (−∞, 0]   (negative real axis)
  z^{1/2}: cut along (−∞, 0]
  z^α:     cut along (−∞, 0]

ALTERNATIVE CUTS (all valid):
  Cut along positive real axis:   Log with arg ∈ (0, 2π)
  Cut along imaginary axis:       another valid branch
```

**Monodromy**: Analytic continuation of f along a loop γ based at z₀ gives a permutation of the values of f at z₀. This permutation is the monodromy of γ. Monodromy is a group homomorphism:

    π₁(ℂ \ {branch points}, z₀) → Sₙ   (permutation group)

For √z: π₁(ℂ \ {0}) = ℤ, monodromy sends generator → transposition (1 2) in S₂.
After going around twice: (1 2)² = identity → back to start.

---

## Compact Riemann Surfaces and Genus

Every compact (closed, bounded) Riemann surface is a **topological surface** classified by its genus g ≥ 0:

```
GENUS CLASSIFICATION:

  g = 0:  Riemann sphere S² = ℂ ∪ {∞} = ℙ¹
          Simply connected, χ = 2 − 2g = 2
          All compact genus-0 surfaces are conformally equivalent

  g = 1:  Torus T² = ℂ/Λ  (quotient by lattice Λ = ℤ + τℤ)
          NOT simply connected: π₁ = ℤ × ℤ
          Elliptic curves — classified by j-invariant
          χ = 0

  g ≥ 2:  Higher genus — algebraic curves F(z,w) = 0 of higher degree
          Universal cover = upper half-plane ℍ
          Uniformization: S = ℍ/Γ for a Fuchsian group Γ
          Hyperbolic geometry
          χ = 2 − 2g < 0
```

**Riemann-Hurwitz formula**: For a holomorphic map f: S → T of compact Riemann surfaces of genus g(S) and g(T), with ramification points (branch points) where f is e-to-1 locally for e > 1:

    2g(S) − 2 = deg(f) · (2g(T) − 2) + Σ (eₚ − 1)

where the sum is over all ramification points p of f.

This determines the genus of an algebraic curve from its degree and branch structure.

---

## The Uniformization Theorem

**Uniformization Theorem** (Poincaré-Koebe): Every simply connected Riemann surface is conformally equivalent to exactly one of:
1. The Riemann sphere ℂ ∪ {∞} (spherical / elliptic)
2. The complex plane ℂ (Euclidean / parabolic)
3. The upper half-plane ℍ or unit disk D (hyperbolic)

This is the classification of simply connected Riemann surfaces. Since every Riemann surface S has a universal cover S̃, and S̃ is simply connected:

    S̃ = ℙ¹, ℂ, or ℍ    (and S = S̃ / Deck transformations)

```
DECK TRANSFORMATIONS:
  S̃ = ℙ¹:  only trivial deck group → S = ℙ¹  (Riemann sphere)
  S̃ = ℂ:   deck group ⊂ translations → S = ℂ or ℂ/Λ (torus)
  S̃ = ℍ:   deck group = Fuchsian group → all other cases (hyperbolic)
```

---

## Holomorphic Functions on Riemann Surfaces

On a compact Riemann surface S, a **holomorphic function** (globally defined, no poles) must be **constant** (by maximum modulus principle — S is compact, |f| achieves its max).

The interesting objects are:
- **Meromorphic functions**: holomorphic except at poles (= rational functions in the algebraic model)
- **Holomorphic forms (differentials)**: ω = f(z) dz, locally
- **Abelian differentials of the first kind**: holomorphic forms on all of S

The **Riemann-Roch theorem** counts linearly independent meromorphic functions and differentials with prescribed poles/zeros on a compact Riemann surface. It generalizes both the Taylor series counting in ℂ and the theory of elliptic functions.

---

## Elliptic Functions (Torus Surfaces)

A torus ℂ/Λ (Λ = ℤω₁ + ℤω₂ a lattice) carries **doubly periodic meromorphic functions**: functions f with f(z + ω₁) = f(z) and f(z + ω₂) = f(z).

**Weierstrass ℘-function**:

    ℘(z; Λ) = 1/z² + Σ_{ω∈Λ\{0}} [1/(z−ω)² − 1/ω²]

Properties:
- Doubly periodic with periods ω₁, ω₂
- Has a double pole at each lattice point, no other singularities
- Satisfies: (℘')² = 4℘³ − g₂℘ − g₃  (differential equation!)
- This ODE defines an elliptic curve: Y² = 4X³ − g₂X − g₃

**Significance**: The map z ↦ (℘(z), ℘'(z)) embeds ℂ/Λ into ℙ² as an elliptic curve. The geometry of elliptic curves (central to number theory, cryptography) is the complex analysis of tori.

**The cryptography bridge: torus → Weierstrass equation → ECC.** The equation (℘')² = 4℘³ − g₂℘ − g₃ is a Weierstrass cubic — the *same* form Y² = X³ + aX + b used in elliptic curve cryptography (ECC) over finite fields 𝔽ₚ. The group law is identical in both settings: on the complex torus ℂ/Λ, addition is z₁ + z₂ mod Λ; on the cubic curve, this corresponds exactly to the chord-and-tangent construction (draw a line through P₁, P₂; it hits the curve at a third point; reflect to get P₁ + P₂). Over ℂ the group is a torus (S¹ × S¹). Over 𝔽ₚ the group is finite, and the discrete logarithm problem in this group is the basis for ECDH and ECDSA. The complex-analytic structure (lattice, j-invariant, complex multiplication) directly informs which curves over 𝔽ₚ are cryptographically strong.

---

**Riemann-Roch Theorem** — the central counting result for compact Riemann surfaces:

For a divisor D on a compact surface S of genus g, with K the canonical divisor:

    l(D) − l(K − D) = deg(D) + 1 − g

where l(D) = dim of space of meromorphic functions with poles bounded by D.

| Consequence | Follows from |
|------------|-------------|
| Every genus-0 curve is ℙ¹ | l(p) = 2 for a point p → nonconstant meromorphic function of degree 1 → isomorphism to ℙ¹ |
| Every genus-1 curve embeds as a cubic | l(3p) = 3 → embedding in ℙ² as degree-3 curve (Weierstrass form Y² = X³ + aX + b) |
| Genus-2 curves are hyperelliptic | l(K) = 2 → canonical map is 2:1 to ℙ¹ |
| g ≥ 2 curves embed in ℙ^{g-1} | l(K) = g → canonical embedding (for non-hyperelliptic) |

**Moduli of Riemann surfaces.** Different complex structures on a genus-g topological surface are parametrized by the **moduli space M_g**, which has complex dimension 3g − 3 (for g ≥ 2). The construction uses Teichmüller theory: Teichmüller space T_g is a (3g−3)-dimensional complex manifold, and M_g = T_g / (mapping class group). For g = 1: M₁ = ℍ/SL(2,ℤ) (one complex parameter τ, the modular parameter of the torus). For g = 2: M₂ has dimension 3.

---

## Connection to Topology (MIT Background)

From the MIT math background, this connects to:

| Complex Analysis | Topology |
|-----------------|----------|
| Riemann surface genus g | Oriented 2-manifold, H₁(S, ℤ) ≅ ℤ^{2g} |
| Holomorphic 1-forms | H¹(S, ℝ) of dimension 2g |
| Ramified covering f: S → T | Branched covering of surfaces |
| Monodromy of branch points | π₁ action on fiber = permutation representation |
| Uniformization theorem | Classification of simply connected surfaces |
| Riemann-Hurwitz | Euler characteristic formula for branched covers |

The **Euler characteristic** of a compact Riemann surface of genus g: χ = 2 − 2g.
Gauss-Bonnet applied to the hyperbolic metric gives: Area(S) = −2π χ(S) = 2π(2g−2) for g ≥ 2.

---

## Decision Cheat Sheet

| Question | Answer |
|---------|--------|
| Why does log z need a branch cut? | It's multi-valued; Riemann surface makes it single-valued on two-sheet cover |
| How many sheets does √z need? | 2 (quadratic equation → 2 roots) |
| How many sheets does z^{1/3} need? | 3 |
| What is the genus of a smooth plane curve of degree d? | g = (d−1)(d−2)/2 |
| What is the genus of w² = P_{2g+2}(z)? | g |
| Universal cover of genus-g Riemann surface (g≥2)? | Upper half-plane ℍ |
| What is an elliptic function? | Doubly periodic meromorphic function on ℂ/Λ |
| What does Riemann-Roch compute? | dim of spaces of meromorphic functions with bounded poles |

---

## Common Confusion Points

**Riemann surface ≠ Riemannian manifold**: A Riemann surface is a 1-complex-dimensional manifold (2 real dimensions) with a complex structure. A Riemannian manifold is any manifold with a metric tensor. A Riemann surface *carries* a Riemannian metric (the metric induced by its complex structure), but "Riemann surface" specifically refers to the complex structure.

**Branch point ≠ branch cut**: Branch points are intrinsic geometric features of the multi-valued function (where monodromy is nontrivial). Branch cuts are artificial choices of line to remove to get a single-valued branch. The Riemann surface makes the function single-valued without any cuts.

**Not every Riemann surface is compact**: ℂ, D (disk), ℍ (upper half-plane), ℂ \ {0}, etc., are non-compact Riemann surfaces. The Riemann sphere is the only compact simply connected one.

**Elliptic curves are genus-1 Riemann surfaces, not "curves" in the elementary sense**: An elliptic curve is a smooth genus-1 projective algebraic curve — which, over ℂ, is a torus. The term "curve" refers to complex dimension 1 (= real dimension 2). The connection to elliptic integrals (arc length of an ellipse) is historical.

**The j-invariant classifies tori up to conformal equivalence**: Two lattices Λ, Λ' give conformally equivalent tori iff j(Λ) = j(Λ'). The j-invariant of an elliptic curve controls many algebraic and arithmetic properties (CM theory, modularity of elliptic curves over ℚ).
