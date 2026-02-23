# 05 — Groups, Sets, and Abstract Algebra

```
THE LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  SETS                GROUPS              RINGS / FIELDS       LIE GROUPS
  ┌──────────┐        ┌──────────────┐    ┌──────────────┐     ┌──────────────┐
  │ ∈, ⊆, ∪ │        │ closure      │    │ + and ×      │     │ group + mfld │
  │ ∩, \, ×  │   →   │ associative  │ →  │ distributive │  →  │ smooth sym.  │
  │ power set│        │ identity     │    │ inverses     │     │ U(1),SU(2)   │
  │ functions│        │ inverses     │    │ Fields: ÷    │     │ SU(3),SO(3)  │
  └──────────┘        └──────────────┘    └──────────────┘     └──────────────┘

  WHY THIS MATTERS FOR PHYSICS:
  Every conservation law = a symmetry group (Noether's theorem)
  EM gauge invariance      = U(1)          → photon (massless)
  Weak force               = SU(2)         → W±, Z bosons
  Strong force             = SU(3)         → 8 gluons
  Spacetime rotations      = SO(3)/SO(3,1) → angular momentum quantization
  Spin                     = SU(2) (double cover of SO(3))
  Standard Model gauge group = U(1) × SU(2) × SU(3)
═══════════════════════════════════════════════════════════════════════════════
```

---

## 1. Sets — The Foundation

### 1.1 Basic Operations

```
  A ∪ B   union: in A or B (or both)
  A ∩ B   intersection: in both A and B
  A \ B   difference: in A but not B
  Aᶜ      complement: not in A (relative to universe U)
  A × B   Cartesian product: {(a,b) | a ∈ A, b ∈ B}
  𝒫(A)    power set: all subsets of A (|𝒫(A)| = 2^|A|)

  De Morgan's laws:
  (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
  (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
  (Same as Boolean algebra — NOT(A OR B) = NOT(A) AND NOT(B))
```

### 1.2 Functions and Relations

```
  Function f: A → B
  ├── Injective (one-to-one):  f(a₁)=f(a₂) ⟹ a₁=a₂   (no two map to same)
  ├── Surjective (onto):       ∀b ∈ B, ∃a ∈ A: f(a)=b   (everything hit)
  └── Bijective:               both injective and surjective → invertible

  Equivalence relation ~ on A:
  ├── Reflexive:   a ~ a
  ├── Symmetric:   a ~ b ⟹ b ~ a
  └── Transitive:  a ~ b, b ~ c ⟹ a ~ c

  Equivalence classes partition A into disjoint subsets: A/~ (quotient set)
  Example: integers mod n — equivalence class [3] mod 7 = {...,-4,3,10,17,...}
```

### 1.3 Cardinality

```
  Finite sets: |A| = number of elements
  Countably infinite: |ℕ| = |ℤ| = |ℚ| = ℵ₀   (Cantor: diagonalization)
  Uncountably infinite: |ℝ| = |[0,1]| > ℵ₀    (Cantor: diagonal argument)
  |𝒫(A)| > |A| always   (Cantor's theorem)

  In physics: the Hilbert space of a quantum system can be
  separable (countable basis — bound states, discrete spectrum)
  or non-separable (continuous spectrum — position eigenstates)
```

---

## 2. Groups

### 2.1 The Definition

A **group** (G, ·) is a set G with a binary operation · satisfying:

```
  1. CLOSURE:       a, b ∈ G  ⟹  a·b ∈ G
  2. ASSOCIATIVITY: (a·b)·c = a·(b·c)     (no commutativity required!)
  3. IDENTITY:      ∃e ∈ G: e·a = a·e = a  for all a
  4. INVERSES:      ∀a ∈ G, ∃a⁻¹: a·a⁻¹ = a⁻¹·a = e

  If also: a·b = b·a for all a,b → ABELIAN (commutative) group
```

### 2.2 Examples — From Trivial to Physical

```
  GROUP           SET              OPERATION    ABELIAN?  ORDER
  ──────────────────────────────────────────────────────────────────
  Trivial         {e}              ·             Yes       1
  Integers        ℤ                +             Yes       ∞
  Rationals\{0}   ℚ*               ×             Yes       ∞
  Cyclic ℤₙ       {0,1,...,n-1}    + mod n       Yes       n
  Symmetry S₃     permutations     composition   No        6
  of triangle      of {1,2,3}
  GL(n,ℝ)         n×n invertible   matrix mult   No        ∞
                  real matrices
  O(n)            orthogonal       matrix mult   No(n≥2)   ∞
                  matrices (AᵀA=I)
  SO(n)           det=+1 orthog.   matrix mult   No(n≥2)   ∞
  U(n)            unitary (A†A=I)  matrix mult   No(n≥2)   ∞
  SU(n)           unitary, det=1   matrix mult   No(n≥2)   ∞
  ──────────────────────────────────────────────────────────────────
```

### 2.3 Subgroups and Lagrange's Theorem

```
  H ≤ G (H is a subgroup of G) if H is a group under G's operation.
  Test: closed under operation, contains identity, closed under inverses.

  Left coset of H in G:   gH = {g·h | h ∈ H}
  Right coset:            Hg = {h·g | h ∈ H}

  LAGRANGE'S THEOREM: If G finite, |H| divides |G|
  → Group of order 7 has only trivial subgroups (7 is prime → cyclic)
  → Crucial for understanding why certain quantum numbers are allowed

  Normal subgroup N ◁ G:  gN = Ng for all g (left = right cosets)
  Quotient group: G/N — the cosets form a group under coset multiplication
```

### 2.4 Homomorphisms and Isomorphisms

```
  HOMOMORPHISM φ: G → H satisfies φ(a·b) = φ(a)·φ(b)
  (structure-preserving map)

  Kernel: ker(φ) = {g ∈ G | φ(g) = e_H}   ← always a normal subgroup
  Image:  im(φ) = {φ(g) | g ∈ G}

  FIRST ISOMORPHISM THEOREM: G/ker(φ) ≅ im(φ)
  (quotient by the kernel ≅ the image)

  ISOMORPHISM: bijective homomorphism → groups are "the same structure"

  KEY EXAMPLES:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  exp: (ℝ, +) → (ℝ⁺, ×)     φ(x) = eˣ                             │
  │       φ(a+b) = e^(a+b) = eᵃeᵇ = φ(a)φ(b)  ✓  (isomorphism)       │
  │                                                                      │
  │  det: (GL(n,ℝ), ×) → (ℝ*, ×)                                       │
  │       det(AB) = det(A)det(B)  ✓   (homomorphism, not isomorphism)   │
  │       kernel = SL(n,ℝ) = {matrices with det=1}                      │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## 3. Cyclic Groups and Classification

### 3.1 Cyclic Groups

```
  ℤₙ = {0, 1, 2, ..., n-1} under addition mod n
  Generated by a single element: ℤₙ = ⟨1⟩ = {1, 2, 3, ..., 0}

  Every group of prime order p is cyclic ≅ ℤₚ

  U(1) = {e^(iθ) | θ ∈ [0,2π)} under multiplication = circle group
  ≅ ℝ/ℤ (real line mod 1)
  = continuous version of ℤₙ
  THIS IS THE GAUGE GROUP OF ELECTROMAGNETISM.
```

### 3.2 Classification of Finite Abelian Groups

```
  Every finite abelian group ≅ ℤₙ₁ × ℤₙ₂ × ... × ℤₙₖ
  where each nᵢ divides nᵢ₊₁ (or equivalently, each is a prime power)

  Examples:
  ℤ₆ ≅ ℤ₂ × ℤ₃   (since gcd(2,3)=1)
  ℤ₄ ≇ ℤ₂ × ℤ₂   (different structure — ℤ₄ has an element of order 4)

  Order of element a: smallest positive n with aⁿ = e
```

---

## 4. Permutation Groups

### 4.1 Symmetric Group Sₙ

```
  Sₙ = all permutations of {1, 2, ..., n}
  |Sₙ| = n!

  S₃ = {e, (12), (13), (23), (123), (132)}
  (12) = swap 1 and 2;  (123) = 1→2→3→1 (3-cycle)

  Cycle notation: (1 3 5)(2 4) means 1→3→5→1, 2→4→2

  Every permutation = product of transpositions (2-cycles)
  Even permutation: even number of transpositions → subgroup Aₙ (alternating)
  |Aₙ| = n!/2

  Cayley's theorem: Every finite group embeds in some Sₙ.
```

### 4.2 Parity and Physics

```
  Parity operator P in QM: flips spatial coordinates x → -x
  P² = identity → eigenvalues ±1
  Even parity states: ψ(-x) = +ψ(x)   (cosines, s-orbitals)
  Odd parity states:  ψ(-x) = -ψ(x)   (sines, p-orbitals)

  Parity is a ℤ₂ symmetry (group of order 2: {+1, -1} under multiplication)
  EM and gravity conserve parity. Weak force VIOLATES parity (Wu 1956).
```

---

## 5. Rings and Fields

### 5.1 Rings

A **ring** (R, +, ·) has two operations:

```
  (R, +) is an abelian group
  (R, ·) is associative with identity
  Distributive: a·(b+c) = a·b + a·c

  Examples:
  ℤ, ℝ, ℂ, ℝ[x] (polynomials), M_n(ℝ) (matrices — non-commutative ring)

  Integral domain: commutative ring, no zero divisors (ab=0 ⟹ a=0 or b=0)
  ℤ is an integral domain. M_n(ℝ) is not commutative. ℤ/6ℤ has zero divisors (2·3=0).
```

### 5.2 Fields

A **field** is a commutative ring where every nonzero element has a multiplicative inverse:

```
  ℚ, ℝ, ℂ, 𝔽ₚ = ℤ/pℤ (p prime), 𝔽_{p^n} (finite fields)

  Field axioms: (F, +) abelian group, (F*, ×) abelian group, distributive

  KEY FINITE FIELDS:
  𝔽₂ = {0,1} mod 2 — Boolean arithmetic, error-correcting codes
  𝔽₁₆ = GF(16)    — AES encryption uses 𝔽_{2⁸}
  𝔽ₚ for prime p  — elliptic curve cryptography

  In physics: ℝ and ℂ are the fields that matter.
  Quantum mechanics is linear algebra over ℂ.
```

### 5.3 Ideals and Quotient Rings

```
  Ideal I of ring R: closed under addition and "absorbs" multiplication:
  r ∈ R, i ∈ I ⟹ r·i ∈ I and i·r ∈ I

  Quotient ring R/I: cosets a + I form a ring
  Example: ℤ/nℤ = integers mod n (n generates the ideal nℤ = {...,-2n,-n,0,n,2n,...})

  In ring theory, ideals play the role that normal subgroups play in group theory.
```

---

## 6. Artin's Algebra — The Key Theorems

You've read Artin. Here's the structure:

```
  ARTIN'S ALGEBRA ARCHITECTURE
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Ch 1-2:  Matrix groups (GL, SL, O, U) — concrete examples first   │
  │  Ch 3-6:  Abstract groups — cosets, normal subgroups, products      │
  │  Ch 7:    More group theory — Jordan-Hölder, solvable groups        │
  │  Ch 8:    Rings — ideals, quotient rings, ring homomorphisms        │
  │  Ch 9-10: Fields and Galois theory                                  │
  │  Ch 11:   Linear groups over fields                                 │
  │  Ch 12-13: Modules, structure theorem for abelian groups            │
  └──────────────────────────────────────────────────────────────────────┘

  GALOIS THEORY KEY IDEA:
  Field extension K/F has a Galois group Gal(K/F) =
  automorphisms of K fixing F.

  The Galois correspondence:
  Subgroups of Gal(K/F) ↔ Intermediate fields F ⊆ L ⊆ K
  (order-reversing bijection)

  WHY IT MATTERS: solvability of polynomial by radicals
  ↔ Galois group is solvable (composition series with abelian factors)
  Quintic is not generally solvable because S₅ contains A₅ which is simple.
```

---

## 7. Lie Groups — Continuous Symmetry in Physics

### 7.1 What a Lie Group Is

```
  A LIE GROUP is simultaneously:
  ├── a group (abstract algebra)
  └── a smooth manifold (differential geometry)

  The group operations (multiplication and inversion) are smooth maps.

  Intuition: a continuous family of symmetries parameterized smoothly.

  SO(2) = rotations in 2D = circle = S¹ (1-parameter family)
  SO(3) = rotations in 3D (3-parameter family — 3 Euler angles)
  U(1)  = phase rotations e^(iθ) = circle (1-parameter)
  SU(2) = 2×2 unitary matrices, det=1 (3-parameter — sphere S³)
```

### 7.2 Lie Algebras — The Linearization

```
  Near the identity, a Lie group looks like a vector space: the LIE ALGEBRA 𝔤

  For a matrix Lie group G:
  𝔤 = {X | e^(tX) ∈ G for all t ∈ ℝ}   (tangent space at identity)

  LIE BRACKET: [X, Y] = XY − YX   (commutator of matrices)
  ├── Antisymmetric: [X,Y] = −[Y,X]
  └── Jacobi identity: [X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0

  The Lie algebra encodes the local structure; the group is the global structure.
  Knowing 𝔤 determines G near the identity (and globally for simply-connected groups).
```

### 7.3 The Physics Lie Groups — In Detail

```
  ┌────────────────────────────────────────────────────────────────────────┐
  │  U(1) — Electromagnetism                                              │
  │  ─────────────────────────────────────────────────────────────────── │
  │  G = {e^(iθ) | θ ∈ ℝ} ≅ S¹                                          │
  │  𝔤 = iℝ (purely imaginary numbers)  [trivial: all elements commute]  │
  │  Generator: Y (hypercharge) — one generator, one gauge boson (photon) │
  │  Gauge field: Aμ (the EM 4-potential)                                 │
  │  Invariance of physics under ψ → e^(iα)ψ → conservation of charge    │
  └────────────────────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────────────────────┐
  │  SU(2) — Weak Force / Spin                                            │
  │  ─────────────────────────────────────────────────────────────────── │
  │  G = {2×2 unitary matrices, det=1}  ≅ S³ (3-sphere)                  │
  │  𝔤 = 𝔰𝔲(2) = {traceless anti-Hermitian 2×2 matrices}                │
  │  Basis generators: Tₐ = σₐ/2  (a = 1,2,3)                            │
  │  where σ₁,σ₂,σ₃ are the Pauli matrices                               │
  │                                                                        │
  │  [T₁,T₂] = iT₃,  [T₂,T₃] = iT₁,  [T₃,T₁] = iT₂                    │
  │                                                                        │
  │  3 generators → 3 gauge bosons: W⁺, W⁻, W⁰ (→ Z⁰ after mixing)     │
  │                                                                        │
  │  AS SPIN: Jₓ, Jy, Jz satisfy same commutation relations              │
  │  [Jₓ,Jy] = iℏJz etc. — angular momentum algebra is SU(2) algebra    │
  │  Spin-½ particles are in the fundamental (2D) representation of SU(2)│
  └────────────────────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────────────────────┐
  │  SU(3) — Strong Force (QCD)                                           │
  │  ─────────────────────────────────────────────────────────────────── │
  │  G = {3×3 unitary matrices, det=1}                                    │
  │  𝔤 = 𝔰𝔲(3) — 8-dimensional                                          │
  │  Basis: Gell-Mann matrices λ₁,...,λ₈                                  │
  │  8 generators → 8 gauge bosons: 8 gluons                              │
  │  Quarks come in 3 "colors": (r, g, b) = fundamental representation   │
  │  Gluons are in the adjoint (8D) representation                        │
  └────────────────────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────────────────────┐
  │  SO(3) vs SU(2) — The Double Cover                                   │
  │  ─────────────────────────────────────────────────────────────────── │
  │  SO(3) = rotations in 3D space (det=1 orthogonal matrices)           │
  │  SU(2) = 2×2 unitary, det=1                                          │
  │                                                                        │
  │  There is a 2-to-1 homomorphism: SU(2) → SO(3)                       │
  │  Both +U and -U ∈ SU(2) map to the same rotation in SO(3)            │
  │  SU(2) is the "double cover" of SO(3)                                 │
  │                                                                        │
  │  Physical consequence: a spin-½ particle requires a 720° rotation    │
  │  to return to its original state (not 360°)                           │
  │  This is DIRECTLY because SU(2) double covers SO(3).                 │
  │  Half-integer spin is not a mystery — it's representation theory.    │
  └────────────────────────────────────────────────────────────────────────┘
```

### 7.4 Representations

```
  A REPRESENTATION of group G is a homomorphism ρ: G → GL(V)
  (G acts as invertible linear transformations on vector space V)

  Dimension of representation = dim(V)

  SU(2) representations:
  ┌──────────────────────────────────────────────────────────────────┐
  │  Spin s  │  Dim = 2s+1  │  Particle type                        │
  ├──────────┼──────────────┼───────────────────────────────────────┤
  │  s = 0   │  1D          │  Scalar (Higgs, pions)                │
  │  s = 1/2 │  2D (spinor) │  Electrons, quarks, neutrinos         │
  │  s = 1   │  3D (vector) │  Photon, W±, Z (massive spin-1)       │
  │  s = 3/2 │  4D          │  Delta baryon, gravitino (SUSY)       │
  │  s = 2   │  5D          │  Graviton (theoretical)               │
  └──────────┴──────────────┴───────────────────────────────────────┘

  Irreducible representation (irrep): cannot be decomposed further
  Schur's Lemma: any map between two irreps is either 0 or an isomorphism
```

---

## 8. Noether's Theorem

The deepest connection between symmetry and physics:

```
  NOETHER'S THEOREM (1915):
  Every continuous symmetry of the action ↔ a conserved quantity

  ┌────────────────────────────────────────────────────────────────────┐
  │  Symmetry                      Conserved Quantity                  │
  ├────────────────────────────────────────────────────────────────────┤
  │  Time translation (t → t+ε)    Energy                             │
  │  Spatial translation (x → x+a) Linear momentum                    │
  │  Rotation (SO(3))              Angular momentum                    │
  │  U(1) phase (ψ → e^(iα)ψ)     Electric charge                    │
  │  SU(2) isospin                 Isospin (approximate, QCD)         │
  │  Lorentz boost                 Center-of-mass motion              │
  └────────────────────────────────────────────────────────────────────┘

  The symmetry group of the laws of physics IS the structure of the laws.
  Conservation laws are not additional postulates — they follow from symmetry.
```

---

## 9. Quick Reference — Group Vocabulary

```
  Order of group G:    |G| — number of elements
  Order of element a:  smallest n > 0 with aⁿ = e
  Center Z(G):         {g | gx = xg for all x} — elements that commute with all
  Commutator [a,b]:    a⁻¹b⁻¹ab — measures non-commutativity
  Derived subgroup G': generated by all commutators — abelianization G/G'
  Solvable group:      composition series with abelian factors (Galois)
  Simple group:        no proper normal subgroups (the "atoms" of group theory)
  Direct product G×H:  elements (g,h), componentwise operation
  Semidirect product:  G⋊H — one factor acts on the other (non-trivial twist)
```

---

## Decision Cheat Sheet

| Question | Answer |
|---------|--------|
| Is (ℤ, +) a group? | Yes — abelian, infinite |
| Is (ℕ, +) a group? | No — no inverses |
| Is (ℤ, ·) a group? | No — 0 has no inverse, and others don't either (e.g., 2·? = 1 has no integer solution) |
| What's the gauge group of EM? | U(1) |
| What's the gauge group of the weak force? | SU(2) |
| What's the gauge group of QCD (strong)? | SU(3) |
| Why does spin-½ need 720° rotation? | SU(2) double covers SO(3) |
| How many gluons? | 8 (dim of SU(3) adjoint representation) |
| How many photons? | 1 (dim of U(1) adjoint = 1) |
| What does a normal subgroup give you? | A well-defined quotient group |
| What does Galois theory connect? | Field extensions ↔ subgroups of Galois group |
| What does Noether's theorem say? | Symmetry → conservation law |

---

## Common Confusion Points

**"Why does non-commutativity matter for physics?"**
Non-abelian gauge theories (SU(2), SU(3)) have gauge bosons that interact with *each other* — unlike photons. Gluons carry color charge and interact with other gluons. This is why the strong force is so different from EM: non-abelian gauge theory = self-interacting gauge bosons. The non-commutativity of the Lie algebra directly produces this self-interaction.

**"What's the difference between a Lie group and its Lie algebra?"**
The Lie algebra is the tangent space at the identity — it's a local, linear approximation. The Lie group is the full global object. For SU(2): the Lie algebra 𝔰𝔲(2) is 3D space with the cross product as the bracket. The Lie group SU(2) is the 3-sphere S³. Exponentiating elements of the algebra gives you elements of the group: e^(iθ·σ/2) ∈ SU(2).

**"Artin proves everything twice — matrix groups first, then abstract. Why?"**
Concrete before abstract. Matrix groups give you working intuition; you can compute. Abstract groups then reveal the universal structure. The same pedagogical move: in physics, you do specific Hamiltonians before abstract quantum mechanics.

**"SO(3) vs O(3) — what's the difference?"**
O(3) includes all orthogonal matrices: rotations (det=+1) AND reflections (det=-1). SO(3) includes only rotations. The "S" stands for "Special" = determinant 1. In QM, parity (spatial reflection) is a separate symmetry operation not in SO(3). The full spatial symmetry group is O(3) = SO(3) × ℤ₂.

**"Why is SU(2) a double cover of SO(3) and not equal to it?"**
SU(2) ≅ S³ (simply connected). SO(3) ≅ ℝP³ (projective 3-space, not simply connected — has π₁ = ℤ₂). The 2:1 map sends ±U → same rotation. The non-triviality of this covering is *why half-integer spin exists*. If the universe were described by SO(3) alone, only integer spins would be possible. The physical electrons tell us the universe uses SU(2).

---

*Next: `mathematics/06-LINEAR-ALGEBRA.md` — vectors, matrices, eigenvalues, SVD, and the full machinery that QM is built on.*
