# 05 — Groups, Sets, and Abstract Algebra

```
THE LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  SETS                GROUPS              RINGS / FIELDS       LIE GROUPS
  ┌──────────┐        ┌──────────────┐    ┌──────────────┐     ┌──────────────┐
  │ ∈, ⊆, ∪  │        │ closure      │    │ + and ×      │     │ group + mfld │
  │ ∩, \, ×  │   →    │ associative  │ →  │ distributive │  →  │ smooth sym.  │
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

### 1.1 ZFC Axioms — The Foundations

Modern mathematics rests on the Zermelo-Fraenkel axioms with the Axiom of Choice (ZFC). These are the foundation the Cantor cardinality material below depends on.

```
  THE ZF AXIOMS (Zermelo-Fraenkel):

  1. EXTENSIONALITY: Two sets are equal iff they have the same elements.
     A = B  ⟺  ∀x (x ∈ A ⟺ x ∈ B)

  2. PAIRING: For any a, b, the set {a, b} exists.

  3. UNION: For any family F of sets, ∪F exists.

  4. POWER SET: For any set A, the set 𝒫(A) = {X | X ⊆ A} exists.

  5. INFINITY: There exists an infinite set (formalizes ℕ).
     ∃S: ∅ ∈ S ∧ ∀x ∈ S, (x ∪ {x}) ∈ S

  6. REPLACEMENT: If F is a class function, the image F[A] of any set A exists.

  7. FOUNDATION (Regularity): Every non-empty set A has an element
     disjoint from A. This prevents A ∈ A (no self-membership).

  8. SEPARATION (Axiom schema): For any set A and formula φ,
     {x ∈ A | φ(x)} exists. (Avoids Russell's paradox — set must be
     carved from an existing set, not collected from all of V.)

  AXIOM OF CHOICE (AC): For any family of non-empty sets, there exists
  a choice function selecting one element from each.
  ∀F (∅ ∉ F → ∃f: F→∪F such that ∀A ∈ F, f(A) ∈ A)
```

**Key equivalences to AC** (each is equivalent to AC over ZF):

```
  ZORN'S LEMMA: If every chain in a partial order has an upper bound,
  the partial order has a maximal element.
  → Used constantly in algebra: every vector space has a basis (Hamel basis),
    every ring has a maximal ideal, every field has an algebraic closure.

  WELL-ORDERING THEOREM: Every set can be well-ordered.
  → Every set has a total order under which every non-empty subset has a minimum.

  TYCHONOFF'S THEOREM: Arbitrary products of compact spaces are compact.
  → The defining theorem of algebraic topology, equivalent to AC.
```

**Independence of AC from ZF**: Gödel (1938) showed that if ZF is consistent,
so is ZF+AC (AC cannot be disproved from ZF). Cohen (1963, forcing technique)
showed that ZF+¬AC is also consistent. AC is genuinely independent.

### 1.2 Basic Operations

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

### 1.3 Functions and Relations

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

### 1.4 Cardinality and Set-Theoretic Arithmetic

```
  Finite sets: |A| = number of elements
  Countably infinite: |ℕ| = |ℤ| = |ℚ| = ℵ₀   (Cantor: diagonalization)
  Uncountably infinite: |ℝ| = |[0,1]| > ℵ₀    (Cantor: diagonal argument)
  |𝒫(A)| > |A| always   (Cantor's theorem)

  CARDINAL ARITHMETIC:
  ℵ₀ + ℵ₀ = ℵ₀           (union of two countable sets is countable)
  ℵ₀ × ℵ₀ = ℵ₀           (ℤ×ℤ is countable — enumerate by diagonals)
  2^ℵ₀ = |ℝ| = |𝒫(ℕ)|    (beth number ℶ₁)

  ORDINALS vs CARDINALS:
  Ordinals encode order type: ω = {0,1,2,...}, ω+1 = {0,1,2,...,ω}
  Cardinals encode size: ℵ₀ = |ω|, ℵ₁ = |ω₁| (first uncountable ordinal)
  Ordinal arithmetic: ω+1 ≠ 1+ω (non-commutative); 2·ω = ω ≠ ω·2

  CONTINUUM HYPOTHESIS (CH): Is ℵ₁ = 2^ℵ₀?
  Is there a cardinal strictly between ℵ₀ and |ℝ|?
  Gödel (1938): CH is consistent with ZFC (if ZFC is consistent)
  Cohen (1963): ¬CH is consistent with ZFC
  CH is INDEPENDENT of ZFC — it can neither be proved nor disproved.

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
  │  exp: (ℝ, +) → (ℝ⁺, ×)     φ(x) = eˣ                                 │
  │       φ(a+b) = e^(a+b) = eᵃeᵇ = φ(a)φ(b)  ✓  (isomorphism)           │
  │                                                                      │
  │  det: (GL(n,ℝ), ×) → (ℝ*, ×)                                         │
  │       det(AB) = det(A)det(B)  ✓   (homomorphism, not isomorphism)    │
  │       kernel = SL(n,ℝ) = {matrices with det=1}                       │
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
  𝔽_{2⁸} = GF(256)  — AES encryption uses this field for its S-box
  𝔽ₚ for prime p  — RSA, Diffie-Hellman, elliptic curve cryptography

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
  │  Ch 1-2:  Matrix groups (GL, SL, O, U) — concrete examples first     │
  │  Ch 3-6:  Abstract groups — cosets, normal subgroups, products       │
  │  Ch 7:    More group theory — Jordan-Hölder, solvable groups         │
  │  Ch 8:    Rings — ideals, quotient rings, ring homomorphisms         │
  │  Ch 9-10: Fields and Galois theory                                   │
  │  Ch 11:   Linear groups over fields                                  │
  │  Ch 12-13: Modules, structure theorem for abelian groups             │
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
  │  U(1) — Electromagnetism                                               │
  │  ───────────────────────────────────────────────────────────────────   │
  │  G = {e^(iθ) | θ ∈ ℝ} ≅ S¹                                             │
  │  𝔤 = iℝ (purely imaginary numbers)  [trivial: all elements commute]    │
  │  Generator: Y (hypercharge) — one generator, one gauge boson (photon)  │
  │  Gauge field: Aμ (the EM 4-potential)                                  │
  │  Invariance of physics under ψ → e^(iα)ψ → conservation of charge      │
  └────────────────────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────────────────────┐
  │  SU(2) — Weak Force / Spin                                             │
  │  ───────────────────────────────────────────────────────────────────   │
  │  G = {2×2 unitary matrices, det=1}  ≅ S³ (3-sphere)                    │
  │  𝔤 = 𝔰𝔲(2) = {traceless anti-Hermitian 2×2 matrices}                   │
  │  Basis generators: Tₐ = σₐ/2  (a = 1,2,3)                              │
  │  where σ₁,σ₂,σ₃ are the Pauli matrices                                 │
  │                                                                        │
  │  [T₁,T₂] = iT₃,  [T₂,T₃] = iT₁,  [T₃,T₁] = iT₂                    │
  │                                                                        │
  │  3 generators → 3 gauge bosons: W⁺, W⁻, W⁰ (→ Z⁰ after mixing)         │
  │                                                                        │
  │  AS SPIN: Jₓ, Jy, Jz satisfy same commutation relations                │
  │  [Jₓ,Jy] = iℏJz etc. — angular momentum algebra is SU(2) algebra       │
  │  Spin-½ particles are in the fundamental (2D) representation of SU(2)│
  └────────────────────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────────────────────┐
  │  SU(3) — Strong Force (QCD)                                            │
  │  ───────────────────────────────────────────────────────────────────   │
  │  G = {3×3 unitary matrices, det=1}                                     │
  │  𝔤 = 𝔰𝔲(3) — 8-dimensional                                             │
  │  Basis: Gell-Mann matrices λ₁,...,λ₈                                   │
  │  8 generators → 8 gauge bosons: 8 gluons                               │
  │  Quarks come in 3 "colors": (r, g, b) = fundamental representation     │
  │  Gluons are in the adjoint (8D) representation                         │
  └────────────────────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────────────────────┐
  │  SO(3) vs SU(2) — The Double Cover                                     │
  │  ───────────────────────────────────────────────────────────────────   │
  │  SO(3) = rotations in 3D space (det=1 orthogonal matrices)             │
  │  SU(2) = 2×2 unitary, det=1                                            │
  │                                                                        │
  │  There is a 2-to-1 homomorphism: SU(2) → SO(3)                         │
  │  Both +U and -U ∈ SU(2) map to the same rotation in SO(3)              │
  │  SU(2) is the "double cover" of SO(3)                                  │
  │                                                                        │
  │  Physical consequence: a spin-½ particle requires a 720° rotation      │
  │  to return to its original state (not 360°)                            │
  │  This is DIRECTLY because SU(2) double covers SO(3).                   │
  │  Half-integer spin is not a mystery — it's representation theory.      │
  └────────────────────────────────────────────────────────────────────────┘
```

### 7.4 Representations and Character Theory

```
  A REPRESENTATION of group G is a homomorphism ρ: G → GL(V)
  (G acts as invertible linear transformations on vector space V)

  Dimension of representation = dim(V)

  SU(2) representations:
  ┌──────────────────────────────────────────────────────────────────┐
  │  Spin s  │  Dim = 2s+1  │  Particle type                         │
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

**Character theory** — the complete theory of representations:

```
  CHARACTER of a representation ρ:
  χ_ρ: G → ℂ,   χ_ρ(g) = Tr(ρ(g))

  Key properties:
  - Class function: χ_ρ(hgh⁻¹) = χ_ρ(g)  (constant on conjugacy classes)
  - Determines the representation: two reps are isomorphic iff χ_ρ = χ_σ
  - χ of direct sum: χ_{ρ⊕σ} = χ_ρ + χ_σ
  - χ of tensor product: χ_{ρ⊗σ} = χ_ρ · χ_σ

  ORTHOGONALITY OF CHARACTERS (for finite groups):
  ⟨χ_ρ, χ_σ⟩ = (1/|G|) Σ_{g∈G} χ_ρ(g) χ_σ(g)* = δ_{ρσ}

  For compact Lie groups (like SU(2), U(1)), the sum is replaced by a
  Haar integral: ∫_G χ_ρ(g) χ_σ(g)* dg = δ_{ρσ}.

  CHARACTER TABLE (for finite groups):
  Rows = irreducible representations, Columns = conjugacy classes.
  Entry = character value on that conjugacy class.

  S₃ character table:
  ┌──────┬───┬─────┬──────┐
  │ irrep│ e │(12) │(123) │  ← conjugacy class
  ├──────┼───┼─────┼──────┤
  │ triv │ 1 │  1  │  1   │  dim 1: trivial representation
  │ sgn  │ 1 │ -1  │  1   │  dim 1: sign representation (even/odd perm)
  │ std  │ 2 │  0  │ -1   │  dim 2: standard representation
  └──────┴───┴─────┴──────┘

  Sum of squares of dimensions = |G|: 1² + 1² + 2² = 6 = |S₃| ✓

  BURNSIDE'S LEMMA (orbit counting via characters):
  |X/G| = (1/|G|) Σ_{g∈G} |X^g|
  (number of orbits = average number of fixed points)
  Used to count distinct colorings, necklaces, etc. under symmetry.

  PETER-WEYL THEOREM (for compact Lie groups G):
  L²(G) = ⊕_ρ V_ρ ⊗ V_ρ*
  (Hilbert space of G decomposes as direct sum over irreps, each appearing
  with multiplicity equal to its dimension)

  For U(1) = S¹: the irreps are e^(inθ), n ∈ ℤ → Peter-Weyl = Fourier series.
  Representation theory = generalized Fourier analysis on groups.
```

---

## 8. Cryptography — Where Finite Algebra Lives

The algebraic structures in this file are the mathematical foundations of modern public-key cryptography. This is not tangential — it is one of the most consequential applications of abstract algebra in engineering.

**RSA — ℤ/nℤ and Euler's theorem**:

```
  Setup: n = pq (product of large primes), public key (n, e), private key d
  where ed ≡ 1 (mod φ(n)), φ(n) = (p-1)(q-1) = |ℤ/nℤ|*|

  Encryption:  C ≡ Mᵉ (mod n)
  Decryption:  M ≡ Cᵈ (mod n)

  Correctness: Euler's theorem says M^(φ(n)) ≡ 1 (mod n) for gcd(M,n)=1
  → M^(ed) = M^(1+kφ(n)) = M · (M^φ(n))^k ≡ M (mod n)

  Security: computing φ(n) requires factoring n — hard for large n.
  The ring ℤ/nℤ and its multiplicative group (ℤ/nℤ)* = {units mod n} are
  the algebraic heart of RSA.
```

**Diffie-Hellman key exchange — cyclic groups**:

```
  Discrete logarithm problem: given g^x mod p, find x.
  This is believed computationally hard in (ℤ/pℤ)* for large prime p.

  Protocol: Alice sends g^a mod p, Bob sends g^b mod p.
  Shared secret: (g^a)^b = (g^b)^a = g^(ab) mod p.

  Security relies on the group (ℤ/pℤ)* being cyclic of order p-1,
  with the discrete log being computationally indistinguishable from
  random in the group — this is a statement about the group structure.
```

**Elliptic curve cryptography (ECC) — groups over finite fields**:

```
  Elliptic curve E over 𝔽_p: y² = x³ + ax + b (mod p)

  Points on E form an abelian group under the chord-and-tangent law:
  - Identity: the "point at infinity" O
  - Inverse of (x,y): is (x,-y)
  - Addition P+Q: draw line through P,Q, reflect third intersection

  The discrete log problem in E(𝔽_p) is harder than in (ℤ/pℤ)*
  → smaller key sizes for equivalent security (256-bit ECC ≈ 3072-bit RSA)

  ECC is used in TLS 1.3, SSH, Bitcoin (secp256k1 curve), and Signal.
  The algebraic structure is exactly the finite-field group theory of §5.2.
```

**AES — 𝔽_{2⁸} arithmetic**:

```
  AES SubBytes (S-box): evaluates a specific map over 𝔽_{2⁸} = GF(256).
  𝔽_{2⁸} = 𝔽₂[x]/(x⁸ + x⁴ + x³ + x + 1)  ← quotient ring by irreducible poly

  Elements: polynomials over 𝔽₂ of degree < 8 (256 of them)
  Multiplication: polynomial multiplication mod the irreducible polynomial
  The S-box computation is: take multiplicative inverse in 𝔽_{2⁸}, then
  apply an 𝔽₂-affine transformation.

  Lattice-based cryptography (post-quantum): hard problems on module lattices
  over polynomial rings ℤ[x]/(xⁿ+1) — the ring-learning-with-errors (RLWE)
  problem. These are quotient rings whose algebraic structure (NTT-friendly
  factorization of xⁿ+1 over primes) enables efficient multiplication.
```

---

## 9. Noether's Theorem

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

## 10. Quick Reference — Group Vocabulary

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

## Connections to Adjacent Mathematics

**Algebraic topology.** The fundamental group π₁(X, x₀) is literally a group
associated to a topological space (homotopy classes of loops). The SU(2)/SO(3)
double cover is already in the file — the algebraic fact that π₁(SO(3)) = ℤ₂
(SO(3) is not simply connected) is what forces the double cover. Higher
homotopy groups πₙ(X) are abelian for n ≥ 2 (Eckmann-Hilton argument).
Covering space theory is the topological version of the Galois correspondence:
subgroups of π₁(X) ↔ covering spaces of X, mirroring subgroups of Gal(K/F)
↔ intermediate field extensions.

**Algebraic number theory.** The integers ℤ generalize to rings of integers
O_K in number fields K/ℚ. These rings share many group-theoretic properties:
the ideal class group Cl(O_K) measures the failure of unique factorization
(O_K has unique factorization iff Cl(O_K) is trivial). The class group is
a finite abelian group classified by the structure theorem of §3.2 — its
structure is deeply connected to the arithmetic of K. The Galois group
Gal(K/ℚ) acts on Cl(O_K), giving the full machinery of class field theory.
Dedekind domains generalize PIDs in exactly the way that accounts for this.

**Category theory.** Groups, rings, and fields are categories: objects are
groups (rings, fields), morphisms are homomorphisms. Free groups are free
objects: the free group on a set S satisfies a universal mapping property —
any function S → G (group) extends uniquely to a homomorphism F(S) → G.
Free objects are the left adjoint to the forgetful functor. Products (direct
products G×H), coproducts (free products G*H), kernels, and cokernels are
all categorical constructions, computable uniformly across algebraic categories.
The natural isomorphism theorem G/ker(φ) ≅ im(φ) is a universal property.
At the MIT Math level, the categorical framing is the standard unifying language.

---

## Decision Cheat Sheet

| Question | Answer | Why |
|---------|--------|-----|
| Is (ℤ, +) a group? | Yes — abelian, infinite | Closure, assoc, 0, negatives ✓ |
| Is (ℕ, +) a group? | No — no inverses | 1 has no additive inverse in ℕ |
| Is (ℤ, ·) a group? | No — no inverses | 2 has no multiplicative inverse in ℤ |
| What's the gauge group of EM? | U(1) | Photon is the 1 generator |
| What's the gauge group of the weak force? | SU(2) | W±, Z are the 3 generators |
| What's the gauge group of QCD (strong)? | SU(3) | 8 gluons = 8 generators |
| Why does spin-½ need 720° rotation? | SU(2) double covers SO(3) | π₁(SO(3)) = ℤ₂ |
| How many gluons? | 8 | dim(𝔰𝔲(3)) = 3²−1 = 8 |
| How many photons? | 1 | dim(𝔲(1)) = 1 |
| What does a normal subgroup give you? | A well-defined quotient group | gN = Ng → G/N is a group |
| What does Galois theory connect? | Field extensions ↔ subgroups of Gal(K/F) | Order-reversing bijection |
| What does Noether's theorem say? | Symmetry → conservation law | Continuous symmetry of action |
| Why is RSA secure? | Discrete log / factoring hard | Ring structure of ℤ/nℤ |
| Why does ECC beat RSA in key size? | Discrete log harder on elliptic curves | Group structure of E(𝔽_p) |
| How does AC connect to algebra? | Zorn → every vector space has a basis | Every ring has maximal ideal |
| Is CH provable from ZFC? | No — independent (Gödel/Cohen) | Forcing / relative consistency |

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

**"What does the Axiom of Choice have to do with algebra?"**
Without AC, you cannot prove that every vector space has a basis, that every ring has a maximal ideal, or that every field has an algebraic closure. These are all Zorn's lemma arguments. The statements are unprovable in ZF alone. In practice: AC is almost universally accepted, but it's worth knowing that these results are AC-dependent — they can't be "witnessed" constructively.

---

*Next: `mathematics/06-LINEAR-ALGEBRA.md` — vectors, matrices, eigenvalues, SVD, and the full machinery that QM is built on.*
