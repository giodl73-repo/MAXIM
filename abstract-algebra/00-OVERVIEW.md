# Abstract Algebra — Landscape Overview

## The Big Picture

```
+====================================================================+
|           THE HIERARCHY OF ALGEBRAIC STRUCTURES                    |
+====================================================================+
|                                                                    |
|  MAGMA: (S, ·), closure only                                      |
|    ↓ + associativity                                               |
|  SEMIGROUP: (S, ·), associative                                   |
|    ↓ + identity                                                    |
|  MONOID: (S, ·), associative, identity e                          |
|    ↓ + inverses                                                    |
|  GROUP: (G, ·), associative, identity, inverses ← CORE STRUCTURE  |
|    ↓ + commutativity                                               |
|  ABELIAN GROUP: a·b = b·a for all a,b                            |
|    ↓ + second operation (multiplication distributing over +)       |
|  RING: (R, +, ·), abelian group under +, monoid under ·, distrib. |
|    ↓ + commutativity of ·                                          |
|  COMMUTATIVE RING                                                  |
|    ↓ + no zero divisors                                            |
|  INTEGRAL DOMAIN                                                   |
|    ↓ + unique factorization                                        |
|  UFD (Unique Factorization Domain)                                 |
|    ↓ + every ideal is principal                                    |
|  PID (Principal Ideal Domain)                                      |
|    ↓ + division algorithm                                          |
|  EUCLIDEAN DOMAIN: Z, Z[i], F[x]                                  |
|    ↓ + every nonzero element has a multiplicative inverse          |
|  FIELD: (F, +, ·), both operations form abelian groups            |
+====================================================================+
```

The power of abstraction: prove once at the group level, get the result for
S_n, GL(n,F), Z/nZ, elliptic curve groups, Galois groups — simultaneously.

<!-- @editor[diagram/P2]: Landscape diagram shows the ring-of-structures chain well but is purely vertical — doesn't show the cross-connections that motivate this learner: Galois theory bridges field extensions ↔ group theory; representation theory bridges groups ↔ modules ↔ linear algebra; category theory unifies all of them. Rework as a 2D map with lateral connections, not just a linear hierarchy -->

---

## Why Abstract Algebra

```
CONCRETE PROBLEMS THAT REQUIRED ABSTRACTION:

1. Quintic unsolvability (Abel-Ruffini, 1824):
   Is there a formula for roots of degree-5 polynomials?
   Answer: No — and the proof required inventing group theory (Galois, 1832).

2. Unique factorization in Z[√-5]:
   6 = 2·3 = (1+√-5)(1-√-5) — which is "the real factorization"?
   Answer: neither; need ideal theory (Kummer, Dedekind).

3. Error-correcting codes:
   What structures allow systematic error detection and correction?
   Answer: linear codes = subspaces over GF(2), cyclic codes = ideals in GF(2)[x]/(x^n-1).

4. Symmetry in physics:
   Why do particles come in multiplets? Why do conserved quantities exist?
   Answer: representations of Lie groups (Noether's theorem, SU(2), SU(3)).

5. Cryptography:
   What mathematical structures give one-way functions?
   Answer: cyclic groups (DH, ECC), rings of integers in number fields (NTRU, LWE).
```

---

## The Algebraic Structures — Summary

```
+--------------------------------------------------------------------+
| STRUCTURE    | OPERATIONS     | KEY AXIOMS          | EXAMPLES     |
+--------------------------------------------------------------------+
| Magma        | ·              | Closure only        | (N, -)       |
| Semigroup    | ·              | Associativity       | (N, +), (N,·)|
| Monoid       | ·              | Assoc. + identity   | (N,·, 1)     |
| Group        | ·              | + inverses          | Z, S_n, GL_n |
| Abelian grp  | +              | + commutativity     | Z, Q, R      |
| Ring         | +, ·           | Abelian grp + ring  | Z, Z[x]      |
| Comm. ring   | +, ·           | + comm. mult.       | Z, Z[x], F[x]|
| Domain       | +, ·           | + no zero divs      | Z, F[x]      |
| UFD          | +, ·           | + unique factor.    | Z, Z[x]      |
| PID          | +, ·           | + principal ideals  | Z, Z[i]      |
| Euclidean    | +, ·           | + div. algorithm    | Z, F[x], Z[i]|
| Field        | +, ·           | Both groups         | Q, R, C, F_p |
| Module       | +, R-action    | Generalized VS      | Z-modules     |
| Algebra      | +, ·, k-action | Ring + vector space | Matrix alg.  |
+--------------------------------------------------------------------+
```

---

## The Isomorphism Theorems — The Structural Core

Every category of algebraic structures has isomorphism theorems. For groups:

```
FIRST ISOMORPHISM THEOREM:
  If φ: G → H is a homomorphism, then G/ker(φ) ≅ im(φ).
  "Every image is a quotient; every quotient is an image."

SECOND ISOMORPHISM THEOREM:
  If H ≤ G, N ◁ G, then H/(H∩N) ≅ HN/N.
  (HN = {hn : h∈H, n∈N}, subgroup when N is normal)

THIRD ISOMORPHISM THEOREM:
  If N ◁ K ◁ G and N ◁ G, then (G/N)/(K/N) ≅ G/K.
  "Quotient of quotients is a quotient."

These hold verbatim for rings (with ideals instead of normal subgroups),
modules, vector spaces — universal in algebra.
```

---

## Galois Theory — The Crown Jewel

```
CENTRAL QUESTION: Can the roots of f(x) ∈ Q[x] be expressed by radicals?

GALOIS CORRESPONDENCE:
  K/Q field extension ↔ Gal(K/Q) group
  Subfields of K ↔ Subgroups of Gal(K/Q)
  Normal subfields ↔ Normal subgroups

  f(x) solvable by radicals ⟺ Gal(f) is a solvable group.

  Degree ≤ 4: symmetric groups S₁,S₂,S₃,S₄ are solvable → radicals exist.
  Degree 5: S₅ is NOT solvable (contains A₅, which is simple, nonabelian).
            Most degree-5 polynomials have Gal = S₅ → not solvable by radicals.

The proof of the quintic's unsolvability is the paradigm of using group
theory to answer a question that appears purely algebraic.
```

---

## Category Theory — The Unifying Language

```
CATEGORY THEORY speaks about algebraic structures without specifying them.

A CATEGORY C consists of:
  Objects: Ob(C)
  Morphisms: Hom(A,B) for each pair of objects
  Composition: f: A→B, g: B→C → g∘f: A→C
  Identity: id_A for each A.

Examples:
  Grp: groups + group homomorphisms
  Ring: rings + ring homomorphisms
  Vect_k: vector spaces over k + linear maps
  Top: topological spaces + continuous maps
  Set: sets + functions

FUNCTOR: A "morphism of categories" F: C → D preserving composition.
  Forgetful functor: Grp → Set (forget group structure, keep underlying set)
  Free functor: Set → Grp (free group on a set) — left adjoint to forgetful

NATURAL TRANSFORMATION: A morphism of functors.
  The isomorphism theorems ARE natural transformations.

Connection to programming (Haskell):
  Functor typeclass = functor C → Hask (category of Haskell types)
  Monad = a monoid in the category of endofunctors
  (Reader, State, IO are all monads = endofunctor monoids on Hask)
```

---

## Connections to Computer Science

```
TYPE THEORY:
  Product types (A, B) = product in category of types
  Sum types A | B = coproduct (disjoint union)
  Function types A → B = exponential object B^A
  Dependent types = indexed families → topos theory

  Curry-Howard isomorphism:
    Types ↔ Propositions
    Terms (programs) ↔ Proofs
    Function types A→B ↔ Logical implication A⟹B
  This is a category-theoretic statement (Cartesian closed categories ↔ intuitionistic logic).

COMPILER THEORY:
  Monoids: string concatenation, used for "associativity" of code gen.
  Free monoids: lists (free monoid on single element set = N).
  Regular languages: recognized by finite monoids.
  (Kleene-Myhill: language is regular iff its syntactic monoid is finite)

<!-- @editor[bridge/P1]: Missing group isomorphism problem — a canonical TCS topic that directly connects abstract algebra to computational complexity. GI is in NP ∩ coAM; Babai's 2015 quasipolynomial algorithm was a landmark result. This learner's MIT TCS background makes this a primary bridge point; any TCS/Math person coming from complexity theory needs this connection prominently -->
  Linear codes = subspaces of F_q^n.
  Cyclic codes = ideals in F_q[x]/(x^n-1).
  Reed-Solomon = polynomial evaluation codes over F_q.
  All require field arithmetic, polynomial rings, ideal theory.
```

---

## File-by-File Guide

| File | Core Content |
|------|-------------|
| 01-GROUPS.md | Axioms, examples, Lagrange's theorem, subgroups |
| 02-SUBGROUPS-QUOTIENTS.md | Normal subgroups, cosets, quotients, isomorphism theorems |
| 03-PERMUTATION-GROUPS.md | Cayley's theorem, cycle notation, alternating group |
| 04-RINGS-IDEALS.md | Ring axioms, ideals, quotient rings, domain hierarchy |
| 05-POLYNOMIALS-FIELDS.md | Polynomial rings, field extensions, degree theory |
| 06-GALOIS-THEORY.md | Galois correspondence, solvability, quintic impossibility |
| 07-REPRESENTATION-THEORY.md | Characters, Schur's lemma, character tables, applications |
| 08-MODULES-LINEAR-ALGEBRA.md | Modules, free/projective/injective, structure theorem |
| 09-CATEGORY-THEORY.md | Categories, functors, natural transforms, Yoneda, adjoints |
| 10-APPLICATIONS.md | Reed-Solomon, crystallography, crypto, quantum groups |

<!-- @editor[content/P2]: File-by-file table lists topic coverage but omits depth signals — reader can't tell which files are full guides vs. thin; add page-count/section-count column or a depth annotation (e.g., "includes Sylow, group actions, Burnside") -->

---

## Decision Cheat Sheet

| You want to... | Structure needed |
|---------------|-----------------|
| Understand symmetry | Groups |
| Solve polynomial equations | Galois theory (field extensions + groups) |
| Work with integers mod n | Ring theory (Z/nZ) |
| Understand error-correcting codes | Field theory, polynomial rings, ideals |
| Understand representations (physics) | Representation theory |
| Unify all mathematics | Category theory |
| Understand RSA/AES | Ring/field theory (Z/nZ, GF(2^8)) |
| Post-quantum crypto (NTRU/LWE) | Module theory over rings of integers |
| Haskell/functional programming | Category theory (functors, monads) |
| Classify manifolds (topology) | Homology groups (abelian group theory) |

---

## Common Confusion Points

**"Abstract algebra is just fancy generalization with no substance."**
Galois theory literally proved the quintic is unsolvable — a purely concrete
algebraic question, answered by group-theoretic abstraction. Reed-Solomon codes
(which protect every CD, DVD, QR code, and RAID-6 array) are ideals in polynomial
rings over finite fields. The abstraction carries computational and theoretical weight.

**"Groups, rings, fields — all the same thing."**
Groups have ONE binary operation. Rings have TWO (addition + multiplication),
with distributivity linking them. Fields are rings where every nonzero element
has a multiplicative inverse. These are genuinely different with genuinely
different theories.

**"Normal subgroup means the subgroup is 'normal' (natural)."**
"Normal" means: invariant under conjugation (gNg^{-1} = N for all g ∈ G).
This is the exactly the right condition for the quotient G/N to be a group.
Not every subgroup is normal (e.g., in S₃, the subgroup {e, (12)} is NOT normal).

**"Category theory is too abstract to matter."**
Functional programming languages (Haskell, Scala, F#) are built on categorical
foundations. The Curry-Howard isomorphism makes proof assistants (Coq, Lean,
Agda) work. Sheaf theory (categories + topology) underlies modern algebraic geometry.
"Abstract nonsense" (a term Steenrod coined ironically) is productive nonsense.
