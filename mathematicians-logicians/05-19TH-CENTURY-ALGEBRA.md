# 19th-Century Algebra — Galois, Abel, Cayley, Lie, Noether

## The Revolution: From Solving Equations to Studying Structure

Before 1800, algebra meant "finding formulas for roots of polynomials." After 1900,
it meant "studying abstract structures (groups, rings, fields, modules)." The
transformation happened in the 19th century, driven by the figures here.

```
THE ALGEBRAIC REVOLUTION
=========================

OLD PROGRAM (pre-1800): Solve equations
  Quadratic: x = (-b ± √(b²-4ac)) / 2a  ← Babylonians, Al-Khwarizmi
  Cubic: Cardano's formula (1545)
  Quartic: Ferrari's formula (1545)
  Quintic: ???  ← Open problem for 280 years

NEW QUESTION (Ruffini 1799, Abel 1824): WHY can't you solve the quintic?

GALOIS'S ANSWER (1832): Associate a GROUP to the equation.
  Whether the group is "solvable" (in a technical sense) determines
  whether the equation can be solved by radicals.

  This shifts the question from "find the roots" to
  "understand the SYMMETRY STRUCTURE of the roots."

CAYLEY (1854): Abstract group theory — groups without reference to equations.
LIE (1874): Continuous groups (Lie groups) — symmetry of differential equations.
NOETHER (1921): Abstract algebra — rings, ideals, modules as the unifying framework.

The progression: equation → group → abstract algebra → category theory
```

---

## Évariste Galois (1811–1832)

### Who He Was

French mathematician who died in a duel at age 20. In his short life he
created Galois theory — the connection between group theory and polynomial roots.
He submitted papers to the French Academy twice; they were lost or rejected.
The night before his duel, he wrote a summary of his mathematical ideas.
The letter was published in 1846, 14 years after his death.

### The Contribution: Galois Theory

**The Quintic is Unsolvable — Why**

```
THE QUESTION
=============
Quadratic formula: x = (-b ± √D) / 2a where D = b²-4ac
Cubic formula:     exists (Cardano, 1545) — involves cube roots
Quartic formula:   exists (Ferrari, 1545) — involves 4th roots
Quintic:           x⁵ + ax + b = 0 — general formula? NONE EXISTS.

WHY? Galois's answer:

Step 1: Define the GALOIS GROUP of a polynomial.
  Given f(x) with roots r₁, ..., rₙ, the Galois group Gal(f) consists of
  all permutations of the roots that preserve every algebraic relation
  between them.

  Example: x² - 2 has roots ±√2.
    The only non-trivial relation: r₁ + r₂ = 0.
    The permutation r₁ ↔ r₂ preserves this.
    Gal(x² - 2) = Z₂ (cyclic group of order 2).

Step 2: A polynomial is solvable by radicals iff its Galois group is
  a SOLVABLE GROUP.

  A group G is solvable if there's a chain:
    G = G₀ ⊇ G₁ ⊇ ... ⊇ Gₙ = {e}
  where each Gᵢ/Gᵢ₊₁ is abelian.
  (The group can be "taken apart" by abelian quotients.)

  Quadratic Galois group ≤ S₂ (order 2): solvable → formula exists ✓
  Cubic Galois group ≤ S₃ (order 6): solvable → formula exists ✓
  Quartic Galois group ≤ S₄ (order 24): solvable → formula exists ✓
  Quintic Galois group = S₅ (order 120): NOT solvable → no formula ✗

S₅ is not solvable because A₅ (alternating group on 5 elements,
order 60) is SIMPLE — no normal subgroups — and not abelian.
```

**The Galois Correspondence — The Deep Theorem**

```
GALOIS CORRESPONDENCE
======================

Given a polynomial f(x), let K be the splitting field (the smallest
field containing all roots), and F be the base field (e.g., Q).

FUNDAMENTAL THEOREM OF GALOIS THEORY:
  There is a perfect anti-isomorphism between:
    { subgroups of Gal(K/F) }  ←→  { subfields F ⊆ L ⊆ K }

  Bigger subgroup ↔ Smaller subfield
  Smaller subgroup ↔ Larger subfield
  Normal subgroup ↔ Galois extension (field with extra symmetry)

Consequences:
  - Why √2 + √3 is algebraic over Q: its minimal polynomial is
    x⁴ - 10x² + 1, and the Galois group structure tells you
    exactly which subfields exist.
  - Impossibility of trisecting an angle with compass/straightedge:
    trisection requires solving a cubic that doesn't split into
    quadratic subfields — the Galois group prevents it.
  - Squaring the circle impossible: π is transcendental (not algebraic),
    and constructible lengths must be algebraic.
```

This structure — a group acting on objects, subgroups corresponding to
invariant substructures — reappears throughout mathematics and physics:
symmetry groups of physical laws, Galois representations in number theory,
and in computer science: type theory correspondences (Curry-Howard-Lambek
is a Galois-correspondence-like theorem between proofs and types and categories).

---

## Niels Henrik Abel (1802–1829)

### Who He Was

Norwegian mathematician who died at 26 of tuberculosis. Independently proved
the unsolvability of the quintic (before Galois, in 1824). Developed the theory
of elliptic functions and integrals, abelian integrals, and proved the addition
theorem for hyperelliptic integrals.

### The Contribution: Abel-Ruffini and Abelian Groups

**The Abel-Ruffini Theorem**

Abel's proof of the quintic's unsolvability (1824) preceded Galois's (1832) and
was more direct. He proved: the general polynomial of degree ≥ 5 cannot be solved
by radicals.

His proof method: Assume a radical formula exists; analyze the structure of
algebraic expressions that can appear; show the symmetry requirements cannot be satisfied.
The proof was correct but dense. Galois explained *why* via group theory.

**Abelian Groups**

A group is **abelian** (named after Abel) if ab = ba for all elements.
The commutativity property is named after him because of his work on:

```
ABELIAN INTEGRALS AND JACOBIANS
=================================

Abel's theorem (1826): Relations between integrals of the form ∫ R(x,y)dx
  where y² = polynomial in x (hyperelliptic integrals).

  These integrals appeared in problems like:
    - Arc length of an ellipse
    - Period of a pendulum (large amplitudes)
    - Motion under inverse-cube-law gravity

  Abel showed these satisfy addition formulas generalizing sin²θ + cos²θ = 1.
  The algebraic structure behind these additions is ABELIAN.

Riemann extended: The "Jacobian variety" J(C) of a curve C of genus g
  is a g-dimensional complex torus — an abelian group.
  Jacobians are fundamental to modern algebraic geometry and arithmetic.
```

**Abel's Convergence Theorem**

If Σ aₙ converges, then lim_{x→1⁻} Σ aₙxⁿ = Σ aₙ.
(Power series with a convergent sum are continuous up to the boundary.)
Used in analysis and Fourier theory.

---

## Arthur Cayley (1821–1895)

### Who He Was

British mathematician. Lawyer by profession for 14 years while doing mathematics.
Made fundamental contributions to: matrix theory, abstract group theory, algebraic
geometry, graph theory, and invariant theory. One of the most prolific mathematicians
of the 19th century (~1,000 papers).

### The Contribution: Matrices and Abstract Groups

**Matrix Algebra**

```
CAYLEY'S MATRIX THEORY (1858)
==============================

Before Cayley: Arrays of numbers appeared in solving linear systems (Gauss),
  but were not treated as algebraic objects with their own operations.

Cayley defined:
  - Matrix addition: (A+B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ
  - Matrix multiplication: (AB)ᵢⱼ = Σₖ AᵢₖBₖⱼ
  - The identity matrix I
  - Matrix inverse: A⁻¹ where AA⁻¹ = I (when it exists)
  - Determinant (in terms of cofactors)

Key properties he proved:
  - Matrix multiplication is NOT commutative: AB ≠ BA in general
  - The Cayley-Hamilton theorem:
    Every matrix satisfies its own characteristic polynomial.
    If p(λ) = det(λI - A) = λⁿ + aₙ₋₁λⁿ⁻¹ + ... + a₀, then
    p(A) = Aⁿ + aₙ₋₁Aⁿ⁻¹ + ... + a₀I = 0 (the zero matrix).

Cayley-Hamilton applications:
  - Compute A⁻¹ from the characteristic polynomial
  - Control theory: stability analysis of linear systems
  - Quantum mechanics: operator algebra
  - Machine learning: matrix powers and series
```

**Abstract Group Theory (1854)**

Cayley gave the first abstract definition of a group:
A set G with a binary operation · satisfying:
1. Closure: a·b ∈ G
2. Associativity: (a·b)·c = a·(b·c)
3. Identity: ∃e, a·e = e·a = a
4. Inverses: ∃a⁻¹, a·a⁻¹ = a⁻¹·a = e

Before this, "groups" existed only concretely (Galois groups, permutation groups,
symmetry groups). Cayley abstracted the pattern.

**Cayley's Theorem**: Every group is isomorphic to a group of permutations.
(Every abstract group can be concretely realized as symmetries of a set.)

**Cayley Graph**: A group's structure visualized as a directed graph where
vertices are elements and edges represent multiplication by generators.
Used in geometric group theory, computational group theory, and the theory
of distributed computation (Cayley graphs give optimal communication networks
for certain parameters).

---

## Sophus Lie (1842–1899)

### Who He Was

Norwegian mathematician. Friend of Felix Klein. Together they developed the
Erlangen Programme (1872): classify geometries by their symmetry groups.
Lie's contribution: continuous symmetry groups (what we now call Lie groups).

### The Contribution: Lie Groups and Lie Algebras

```
LIE'S MOTIVATION
=================

Galois: DISCRETE symmetries of polynomial equations → finite groups
Abel/Jacobi: Symmetries of integral addition → abelian groups
Lie: CONTINUOUS symmetries of differential equations → Lie groups

Just as Galois groups control solvability of polynomial equations,
Lie groups control solvability of differential equations.

What is a Lie group?
  A group that is ALSO a smooth manifold,
  where multiplication and inversion are smooth maps.

Examples:
  SO(2): rotations of a circle = {e^(iθ) : θ ∈ R}  (a circle)
  SO(3): rotations in 3D = a 3D manifold (SO(3) ≅ RP³)
  SU(2): special unitary 2×2 matrices = a 3-sphere S³
  GL(n,R): invertible n×n matrices = open subset of Rⁿ²
  U(1): complex numbers of modulus 1 = a circle
```

**Lie Algebras**

```
LIE ALGEBRAS — THE TANGENT SPACE AT THE IDENTITY
==================================================

A Lie algebra 𝔤 is the tangent space of a Lie group G at the identity,
with a bracket operation [X,Y] = XY - YX.

Key fact: Every Lie group determines a Lie algebra.
  Near the identity, group multiplication is captured by the algebra.

Lie's theorem: Lie algebras can be classified (by Killing forms,
  root systems, Dynkin diagrams) — and this classifies Lie groups.
  The classification was completed by Wilhelm Killing and Élie Cartan.

Simple Lie algebras: Aₙ = 𝔰𝔩(n+1), Bₙ = 𝔰𝔬(2n+1), Cₙ = 𝔰𝔭(2n),
  Dₙ = 𝔰𝔬(2n), plus exceptional: G₂, F₄, E₆, E₇, E₈.

WHY LIE GROUPS MATTER (Modern Physics):
  Every continuous symmetry in physics is a Lie group.
  Noether's theorem: symmetry → conservation law.

  Symmetry group          Conservation law
  ------------------      ----------------
  Time translation        Energy
  Space translation       Momentum
  Rotation SO(3)          Angular momentum
  U(1) gauge symmetry     Electric charge
  SU(2) × U(1) gauge      Electroweak charges
  SU(3) gauge             Color charge (QCD)

  The Standard Model of particle physics is the Lagrangian of a
  gauge theory with gauge group SU(3) × SU(2) × U(1).
  Every term in it is Lie theory.
```

**The Exponential Map**

Every Lie group is related to its Lie algebra by the exponential map:
exp: 𝔤 → G, sending X ↦ e^X (matrix exponential or formal series)

This connects the algebra (linear, easy to analyze) to the group
(curved manifold, harder). It's the reason differential equations with
continuous symmetry can be solved by "infinitesimal" (algebraic) methods.

---

## Emmy Noether (1882–1935)

### Who She Was

German mathematician. Could not hold a university position for years due to
being a woman — she lectured at Göttingen under Hilbert's name. Eventually
given an honorary title. Fled Nazi Germany in 1933 to Bryn Mawr College in
the US. Died of surgical complications two years later.

Described by Einstein as "the most significant creative mathematical genius
thus far produced," and by Hilbert and Weyl as the most important woman in
mathematics. Neither endorsement is adequate to describe the scope of what
she actually did.

### The Contribution: Modern Abstract Algebra and Noether's Theorem

**Abstract Algebra — The Noetherian Program**

```
WHAT NOETHER UNIFIED
=====================

Before Noether, there were:
  - Number theory (Gauss, Dedekind)
  - Polynomial rings (19th century algebra)
  - Group theory (Galois, Cayley, Lie)
  - Vector spaces (19th century)
  - Invariant theory (Cayley, Hilbert)

All ad hoc, with different methods for each domain.

Noether's contribution (especially "Idealtheorie in Ringbereichen", 1921):
  Define RINGS, IDEALS, and MODULES axiomatically.
  Prove theorems that apply to ALL of them simultaneously.
  What's true of numbers because of their ring structure is
  also true of polynomials, of functions, of matrices.

A RING (Noether's definition, generalized):
  A set with two operations (+ and ×), addition abelian,
  multiplication associative, distributes over addition.
  No assumption of commutativity, inverses, or cancellation.

An IDEAL in a ring R:
  A subset I ⊆ R such that:
    - Closed under addition: a,b ∈ I → a+b ∈ I
    - Closed under multiplication by any ring element: a ∈ I, r ∈ R → ra ∈ I

A NOETHERIAN RING:
  A ring satisfying the ascending chain condition:
  Every chain of ideals I₁ ⊆ I₂ ⊆ I₃ ⊆ ... stabilizes.
  Equivalently: every ideal is finitely generated.

  Examples: Z is Noetherian. Every PID. Polynomial rings over a field.
  Hilbert basis theorem (which Noether reproved cleanly):
  If R is Noetherian, so is R[x].
```

**Why the Ascending Chain Condition Matters for Computer Science**

```
NOETHERIAN STRUCTURES IN CS
============================

A Noetherian structure means: any ascending sequence of "larger and larger"
objects must eventually stabilize. This is a termination guarantee.

Applications:
  - Term rewriting systems: if the term structure is Noetherian,
    rewriting terminates (no infinite chains of rewrites)
  - Program analysis: type systems and abstract interpretation use
    Noetherian lattices to guarantee analysis termination
  - Logic programming: certain resolution strategies terminate on
    Noetherian constraints
  - Database optimization: query containment in certain logics

Every time you use a static analysis tool that guarantees it terminates,
there's often a Noetherian argument underneath.
```

**Noether's Theorem — The Connection Between Symmetry and Conservation**

```
NOETHER'S THEOREM (1915, published 1918)
=========================================

For a physical system described by a Lagrangian L[q, q̇, t]:
  Every continuous symmetry of L corresponds to a conserved quantity.
  Conversely, every conservation law corresponds to a symmetry.

Precise statement:
  If the action S = ∫L dt is invariant under a one-parameter family
  of transformations q → q + ε·η(q,t) + O(ε²), then
  J = ∂L/∂q̇ · η is conserved: dJ/dt = 0.

Examples:
  L is invariant under time translation (L doesn't depend on t)
    → Energy is conserved: dE/dt = 0

  L is invariant under spatial translation
    → Momentum is conserved: dp/dt = 0

  L is invariant under rotation
    → Angular momentum is conserved

This is NOT just a clever observation — it is a profound theorem stating
that conservation laws and symmetries are EQUIVALENT. If you discover
a conservation law, you can hunt for its symmetry. If you break a symmetry,
you will lose the corresponding conservation.

This theorem governs all of modern physics:
  - Why energy is conserved: time-translation symmetry
  - Why charge is conserved: U(1) gauge symmetry
  - Why the proton doesn't decay (probably): baryon number conservation
    related to a global U(1) symmetry
```

---

## Comparison Table

| Figure | Dates | Core Contribution | Built On | Built Into |
|--------|-------|-------------------|----------|------------|
| **Galois** | 1811–1832 | Group theory, Galois theory, solvability | Lagrange, Ruffini | Cayley, Klein, modern algebra |
| **Abel** | 1802–1829 | Quintic unsolvability, abelian groups/integrals | Euler, Lagrange | Riemann, complex analysis, algebraic geometry |
| **Cayley** | 1821–1895 | Matrix algebra, abstract group theory | Galois, Hamilton | Linear algebra, quantum mechanics, network theory |
| **Lie** | 1842–1899 | Continuous symmetry groups, Lie algebras | Klein, Cayley | All of modern physics (Standard Model) |
| **Noether** | 1882–1935 | Abstract algebra (rings/modules), Noether's theorem | Dedekind, Hilbert | All of algebra, physics (symmetry-conservation) |

---

## Who to Cite for What

| Concept | Cite | Notes |
|---------|------|-------|
| Galois group of a polynomial | Galois | The original source |
| Unsolvability of the quintic (group-theoretic) | Galois | Abel gave a different proof earlier |
| Galois correspondence (subgroups ↔ subfields) | Galois | Fundamental theorem of Galois theory |
| Unsolvability of the quintic (direct proof) | Abel-Ruffini | Abel 1824, independent of Galois |
| Abelian groups (named for) | Abel | His abelian integrals were commutative |
| Matrix multiplication definition | Cayley | *Memoir on the Theory of Matrices* 1858 |
| Cayley-Hamilton theorem | Cayley-Hamilton | Every matrix satisfies its characteristic poly |
| Abstract group definition | Cayley | 1854 |
| Cayley's theorem (every group is a permutation group) | Cayley | |
| Lie groups (continuous symmetry groups) | Lie | Fundamental to modern physics |
| Lie algebras | Lie | Tangent space at identity of Lie group |
| Symmetry-conservation law connection | Noether | *Noether's theorem* 1915/1918 |
| Abstract ring/ideal/module theory | Noether | *Idealtheorie* 1921 |
| Noetherian rings (ascending chain condition) | Noether | Ubiquitous in algebra and CS |

---

## Common Confusion Points

**"Galois was too young to do serious mathematics"** — Galois did create Galois
theory before age 21. The work is genuinely difficult and profound. The reason
it was not immediately accepted was partly his age, partly his political activities,
and mostly the difficulty of reading his compressed prose.

**"Abel proved what Galois proved"** — They independently proved the same result
(quintic unsolvability) but by different methods. Abel's proof (1824) was more
direct. Galois's approach (1832) was deeper — he explained WHY by introducing
group theory, which became the more influential framework.

**"Matrix multiplication was obvious"** — The non-commutativity of matrices
(AB ≠ BA) was not obvious and was initially confusing. The insight that arrays
of numbers could be algebraic objects with their own arithmetic was Cayley's.
Hamilton had introduced quaternions earlier (1843, non-commutative algebra),
and this influenced Cayley.

**"Noether's theorem is just physical intuition"** — It is a precise mathematical
theorem. The statement requires the Lagrangian framework (File 03) and the
calculus of variations. The result is that every smooth symmetry (one-parameter
Lie group action) corresponds to a conserved charge. It applies in quantum field
theory as well as classical mechanics.

**"Lie groups are only for physicists"** — Lie theory pervades modern mathematics:
algebraic groups, representation theory, differential geometry, number theory
(automorphic forms, Langlands program), combinatorics (symmetric functions as
representations of GL(n)), and computer graphics (rotation group SO(3),
quaternions for 3D rotations).
