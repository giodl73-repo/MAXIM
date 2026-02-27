# Groups

<!-- @editor[diagram/P2]: Opening diagram is the four axioms — correct but the learner knows these cold from MIT. The "big picture" for this audience should map the landscape of group theory: finite vs. infinite, abelian vs. non-abelian, classification branches (Sylow/CFSG/solvable), and where computational group theory sits. The axioms belong in the first section, not as the landscape diagram -->

## The Big Picture

```
+====================================================================+
|                    THE GROUP AXIOMS                                 |
+====================================================================+
|                                                                    |
|  A GROUP (G, ·) satisfies:                                        |
|  1. CLOSURE:       a · b ∈ G for all a, b ∈ G                    |
|  2. ASSOCIATIVITY: (a · b) · c = a · (b · c)                     |
|  3. IDENTITY:      ∃e ∈ G: e · a = a · e = a  for all a          |
|  4. INVERSES:      ∀a ∈ G ∃a⁻¹: a · a⁻¹ = a⁻¹ · a = e          |
|                                                                    |
|  ABELIAN: additionally a · b = b · a for all a, b.               |
|                                                                    |
|  The identity and inverses are UNIQUE (provable from the axioms). |
+====================================================================+

                          EXAMPLES OF GROUPS
+---------------+----------+---------------------+-------------------+
| Group         | Operation | Order               | Abelian?          |
+---------------+----------+---------------------+-------------------+
| Z             | +         | ∞                   | Yes               |
| Z/nZ          | + mod n   | n                   | Yes               |
| (Z/nZ)*       | × mod n   | φ(n)                | Yes               |
| Q*, R*, C*    | ×         | ∞                   | Yes               |
| S_n           | compose   | n!                  | n≤2 only          |
| A_n           | compose   | n!/2                | n≤3 only          |
| D_n (dihedral)| compose   | 2n                  | n≤2 only          |
| GL(n,F)       | ×         | ∞ (or finite for F_p)| No (n≥2)         |
| SL(n,F)       | ×         | ∞ (or finite)       | No (n≥2)          |
| SO(n)         | ×         | ∞ (Lie group)       | n≤2 only          |
| SU(2)         | ×         | ∞ (Lie group)       | No                |
| (Z/pZ)* (p prime)| ×     | p-1                 | Yes (cyclic)      |
+---------------+----------+---------------------+-------------------+
```

---

<!-- @editor[audience/P2]: "The Axioms — Minimal and Provable" section walks through closure, associativity, identity, inverses, then proves uniqueness of identity and cancellation from scratch. This learner has MIT graduate-level groups — skip the axiom derivations, pivot immediately to what's structurally interesting: the minimal axiom systems, one-sided axioms, and the connection to monoids/semigroups in the algebraic hierarchy -->
you can prove right identity and right inverses. The standard 4-axiom list is
pedagogically convenient.

**Uniqueness of identity:**
```
If e and e' both satisfy ea=ae=a:
  e = e·e' = e'  (use e' as identity in first, e as identity in second).
```

**Uniqueness of inverses:**
```
If ab=e and ac=e, then:
  b = eb = (ca)b = c(ab) = ce = c.
```

**Cancellation:**
```
Left cancellation: ab = ac → b = c.
  (Multiply both sides on left by a⁻¹.)
Right cancellation: ba = ca → b = c.
```

---

## Key Examples in Depth

### Symmetric Group S_n

```
S_n = all bijections {1,...,n} → {1,...,n}, under composition.
|S_n| = n!.  Non-abelian for n ≥ 3.

Two-line notation for σ ∈ S_4:
  σ = (1 2 3 4)  means 1→2, 2→3, 3→4, 4→1.
      (2 3 4 1)
  In cycle notation: σ = (1 2 3 4), a single 4-cycle.

Composition: σ∘τ means "apply τ first, then σ."
  (1 2)(1 3) = ?  Apply (1 3) first: 1→3, 3→1; then (1 2): 3→3, 1→2.
  Net: 1→3, 3→2, 2→2 ... computing:
  1 →^{(13)} 3 →^{(12)} 3: so 1→3.
  2 →^{(13)} 2 →^{(12)} 1: so 2→1.
  3 →^{(13)} 1 →^{(12)} 2: so 3→2.
  Result: (1 3 2) = (1 2)(1 3).  [Note: S_3 is non-abelian.]
```

### Dihedral Group D_n

```
D_n = symmetries of regular n-gon.
Generators: r = rotation by 2π/n, s = a reflection.
Relations: r^n = e,  s² = e,  srs^{-1} = r^{-1}  (i.e., srs = r^{-1}).

Elements: {e, r, r², ..., r^{n-1}, s, sr, sr², ..., sr^{n-1}}
|D_n| = 2n.

D_3 ≅ S_3: label vertices 1,2,3. Rotations = even permutations. Reflections = transpositions.

D_4 (square):
  r = (1 2 3 4),  s = (1 4)(2 3)  [reflection across vertical axis]
  Subgroups: {e}, {e,r²}, {e,r,r²,r³}, {e,s}, {e,sr²}, {e,sr,sr³}, ...
  Has 3 subgroups of order 2 and 1 of order 4 besides the cyclic {r}.
```

### Quaternion Group Q_8

```
Q_8 = {1, -1, i, -i, j, -j, k, -k} under quaternion multiplication.
  i² = j² = k² = ijk = -1.
  ij = k, ji = -k, jk = i, kj = -i, ki = j, ik = -j.

|Q_8| = 8.  Non-abelian.
Every subgroup of Q_8 is normal! (Q_8 is a Hamiltonian group.)
  This distinguishes Q_8 from D_4 (which has non-normal subgroups).

Subgroups: {1}, {±1}, {±1,±i}, {±1,±j}, {±1,±k}, Q_8.
  {±1}: the unique element of order 2 (the "center" has order 2).

Connection to SU(2):
  Q_8 embeds in SU(2) via i↦iσ_z, j↦iσ_y, k↦iσ_x (Pauli matrices times i).
  This is the reason spin-1/2 particles have double-valued representations.
```

---

## Order of Elements

```
ord(a) = smallest positive k with a^k = e.

PROPERTIES:
  ord(a) divides |G|  (Lagrange — the subgroup ⟨a⟩ has order ord(a))
  ord(a^k) = ord(a) / gcd(k, ord(a))
  In abelian group: ord(ab) | lcm(ord(a), ord(b))  (may be less)

COMPUTATION:
  In Z/nZ: ord([k]) = n/gcd(k,n).
  In S_n: ord(σ) = lcm(cycle lengths of σ).
    Example: (1 2 3)(4 5) ∈ S_5: lcm(3,2) = 6.
  In GL(2,F_p): harder — Jordan normal form.

CYCLIC GROUPS: G = ⟨a⟩ is cyclic iff ∃a with ord(a) = |G|.
  Generators of Z/nZ: elements of order n = {k : gcd(k,n)=1}.
  Count: φ(n) generators.
```

---

## Subgroups

```
SUBGROUP TEST (H ≤ G):
  H ≠ ∅ and ∀a,b ∈ H: ab⁻¹ ∈ H.

SUBGROUPS OF Z: all are nZ = {0, ±n, ±2n, ...}.
  Lattice: mZ ⊆ nZ iff n|m.
  gcd(m,n)Z = mZ + nZ  (Bezout: generated by gcd).
  lcm(m,n)Z = mZ ∩ nZ.

SUBGROUPS OF Z/nZ: one subgroup of order d for each d|n.
  Subgroup of order d: ⟨n/d⟩ = {0, n/d, 2n/d, ..., (d-1)n/d}.
  Lattice of subgroups of Z/12Z: divides of 12 form the lattice.

SUBGROUPS OF S_n:
  A_n (even permutations, index 2).
  Stab(i) = {σ ∈ S_n : σ(i)=i} ≅ S_{n-1}.
  Sylow subgroups of prime order.
```

---

## Lagrange's Theorem and Cosets

```
LEFT COSET of H in G: aH = {ah : h ∈ H}.
  Two left cosets are either EQUAL or DISJOINT.
  Every element of G is in exactly one left coset.
  All cosets have the same size |H|.

COSET PARTITION: G = H ⊔ a₁H ⊔ a₂H ⊔ ...  (disjoint union)
  |G| = [G:H] · |H|  where [G:H] = number of cosets.

LAGRANGE:
  |H| | |G|,  |a| | |G|,  a^{|G|} = e.

CONVERSE fails: A_4 has order 12, no subgroup of order 6.

INDEX 2 SUBGROUPS are always normal (easy proof):
  H has index 2 → only two cosets: H and G\H.
  Left coset aH = right coset Ha (when a ∉ H, both equal G\H).
  So aH = Ha for all a → H normal.
  Example: A_n has index 2 in S_n → A_n ◁ S_n.
```

---

## Sylow Theorems

```
|G| = p^a · m,  gcd(p,m) = 1.  A Sylow p-subgroup has order p^a.

SYLOW I: Sylow p-subgroups exist.
SYLOW II: All Sylow p-subgroups are conjugate: gPg^{-1} = Q.
SYLOW III: n_p = # Sylow p-subgroups satisfies n_p ≡ 1 (mod p) and n_p | m.

APPLICATION — classify groups of order 15 = 3·5:
  n_3 | 5 and n_3 ≡ 1 (mod 3): n_3 ∈ {1,4} ∩ {1,4}: wait, divisors of 5: {1,5}.
  n_3 ≡ 1 (mod 3) and n_3 | 5: n_3 = 1.  So Sylow 3-subgroup P is normal.
  n_5 | 3 and n_5 ≡ 1 (mod 5): n_5 = 1. Sylow 5-subgroup Q is normal.
  G = P × Q ≅ Z/3 × Z/5 ≅ Z/15 (since gcd(3,5)=1).
  Every group of order 15 is cyclic. ✓

APPLICATION — classify groups of order p² (p prime):
  n_p = # Sylow p-subgroups of p² = p^2 ≡ 1 (mod p) and n_p | 1.
  n_p = 1.  The unique Sylow p-subgroup is normal, so G is abelian.
  By the classification of finite abelian groups: G ≅ Z/p² or Z/p × Z/p.
```

---

<!-- @editor[bridge/P1]: Missing computational group theory section — the group isomorphism problem (GI), Babai's 2015 quasipolynomial-time algorithm, and the gap between GI and graph isomorphism are canonical TCS topics this learner will want. Also missing: Schreier-Sims algorithm for permutation groups, base/strong generating sets, and how group-theoretic algorithms underpin computer algebra systems (GAP, Magma). These are the tools that make group theory computable and directly connect to this learner's TCS background -->

<!-- @editor[bridge/P2]: No connection between group actions and symmetry in ML/physics — the learner calibration explicitly flags "group actions → symmetry in ML/physics" as a best bridge. Equivariant neural networks (G-CNNs, E(n)-equivariant GNNs) use group actions as a core design primitive; this section covers group actions purely abstractly without the ML connection -->

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Verify G is a group | Check 4 axioms (or subgroup criterion for H ≤ G) |
| Find order of element a | Smallest k with a^k = e; in S_n: lcm of cycle lengths |
| Show a^{|G|} = e | Lagrange: ord(a) divides |G| |
| Count elements of each order in Z/nZ | Elements of order d: φ(d), for each d|n |
| Classify all abelian groups of order n | Factor n = ∏p_i^{a_i}; apply structure theorem per prime |
| Analyze group of given order | Sylow theorems for prime factorization |
| Show H ≤ G | Two-step criterion: H ≠ ∅ and ab⁻¹ ∈ H |
| Show H ◁ G (normal) | gHg⁻¹ = H for all g; or index 2 |

---

## Common Confusion Points

**"Left and right cosets are the same."**
They're equal iff H is normal. For non-normal H: aH ≠ Ha in general.
Example in S_3: H = {e,(12)}, a = (123).
  aH = {(123),(123)(12)} = {(123),(13)}.
  Ha = {(123),(12)(123)} = {(123),(23)}.  Different.

**"Lagrange's converse holds."**
A_4 is the standard counterexample. Order 12, but no subgroup of order 6.
The converse holds for: abelian groups (structure theorem), p-groups (Sylow I),
and whenever the order is prime (only one possible group: Z/p).

**"SU(2) ≅ SO(3)."**
SU(2) is a double cover of SO(3), not isomorphic. The map SU(2) → SO(3) is
a 2-to-1 surjective homomorphism with kernel {±I}. This "covering" is why
spin-1/2 particles (SU(2) representations) cannot be reduced to orbital angular
momentum (SO(3) representations). The kernel {±I} is why a 360° rotation gives
-ψ for spinors, not +ψ.

**"All groups of order p^k are abelian."**
True for p (order = prime) and p² — not for p³ or higher.
Groups of order 8 = 2³: D_4 and Q_8 are non-abelian (with Z/8, Z/4×Z/2, Z/2³ abelian).
