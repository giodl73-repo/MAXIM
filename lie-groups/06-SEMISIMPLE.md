# Classification of Simple Lie Algebras

## The Big Picture

The classification theorem for simple Lie algebras over C is one of the great achievements of
19th-century mathematics: there are exactly four infinite families and five exceptional cases.
This is a complete, finite list. The proof uses root systems (05-ROOT-SYSTEMS.md) as the
combinatorial bridge.

```
+----------------------------------------------------------------------+
|         COMPLETE CLASSIFICATION OF SIMPLE LIE ALGEBRAS OVER C       |
+----------------------------------------------------------------------+
|                                                                      |
|  CLASSICAL SERIES (infinite families):                               |
|                                                                      |
|  A_n  (n>=1):  sl(n+1,C)  =  Lie algebra of SU(n+1) (compact form)  |
|                dim = n(n+2),  rank = n                               |
|                                                                      |
|  B_n  (n>=2):  so(2n+1,C) =  Lie algebra of SO(2n+1)               |
|                dim = n(2n+1), rank = n                               |
|                                                                      |
|  C_n  (n>=3):  sp(2n,C)   =  Lie algebra of Sp(2n)                  |
|                dim = n(2n+1), rank = n                               |
|                                                                      |
|  D_n  (n>=4):  so(2n,C)   =  Lie algebra of SO(2n)                  |
|                dim = n(2n-1), rank = n                               |
|                                                                      |
|  EXCEPTIONAL (5 isolated cases):                                     |
|                                                                      |
|  G_2:  dim=14,  rank=2   F_4:  dim=52,  rank=4                      |
|  E_6:  dim=78,  rank=6   E_7:  dim=133, rank=7                      |
|  E_8:  dim=248, rank=8                                               |
|                                                                      |
+----------------------------------------------------------------------+
```

---

## The Killing Form and Semisimplicity

**Definition:** The Killing form on a Lie algebra g is:
```
B(X,Y) = tr(ad_X . ad_Y)
```
where ad_X: g -> g, ad_X(Z) = [X,Z], and tr is the trace as a linear operator on g.

**Cartan's criterion for semisimplicity:** g is semisimple if and only if B is non-degenerate
(i.e., B(X,Y) = 0 for all Y implies X = 0).

**Cartan's criterion for solvability:** g is solvable if and only if B([g,g], g) = 0,
equivalently B(X,Y) = 0 for all X in [g,g] and all Y in g.

**Proof sketch of semisimplicity criterion:** If g is not semisimple, it has a non-trivial
abelian ideal I. For X in I and arbitrary Y, Z in g: ad_X . ad_Y maps g -> [g,I] subset I,
and ad_X . ad_Y . ad_Z maps g -> ... -> I. The composition maps into I at each step, making
the trace computable by restriction to I — eventually giving tr(ad_X . anything) = 0, so
B(X, -) = 0, contradicting non-degeneracy.

**For compact real forms:** On a compact semisimple Lie algebra, B is negative definite.
This gives g an inner product (X,Y) = -B(X,Y), making g into a metric Lie algebra. The
compact form is the one used in physics (SU(n), SO(n), Sp(n)).

---

## The Classical Series: A_n

**g = sl(n+1,C) = traceless (n+1)x(n+1) complex matrices, [X,Y] = XY-YX.**

**Compact real form:** su(n+1) (skew-Hermitian traceless matrices).
**Compact group:** SU(n+1).

**Rank:** n. Cartan subalgebra h = diagonal traceless matrices (n free entries).

**Root system:** A_n. Roots are e_i - e_j for i != j (1 <= i,j <= n+1), where e_i is the
linear functional extracting the i-th diagonal entry.

**Dimensions:**
- sl(n+1): dim = (n+1)^2 - 1 = n(n+2)
- Rank: n
- Number of roots: n(n+1) (n(n+1)/2 positive roots)

**Special cases:**

| Algebra | Group | Physics |
|---------|-------|---------|
| A_1 = sl(2) | SU(2) | Angular momentum; weak force |
| A_2 = sl(3) | SU(3) | Color/QCD; flavor SU(3) |
| A_4 = sl(5) | SU(5) | Georgi-Glashow GUT model |

**sl(2) in detail:** The prototype. Generators H,E,F with [H,E]=2E, [H,F]=-2F, [E,F]=H.
Everything in semisimple Lie theory is built by understanding sl(2) subalgebras — each root
gives an sl(2) subalgebra, and the representation theory of sl(2) controls the entire structure.

---

## The Classical Series: B_n and D_n

**B_n = so(2n+1,C):** Skew-symmetric (2n+1)x(2n+1) complex matrices.
- Compact form: so(2n+1) inside SO(2n+1)
- Rank n, dim n(2n+1)
- Root system B_n: n long roots {pm e_i} and n(n-1) short roots {pm e_i pm e_j, i<j}
- (Convention can reverse long/short; B_n has two root lengths)

**D_n = so(2n,C):** Skew-symmetric 2n x 2n complex matrices.
- Compact form: so(2n) inside SO(2n)
- Rank n, dim n(2n-1)
- Root system D_n: roots {pm e_i pm e_j : i < j} (all same length — simply-laced)

**Overlap cases** (same Lie algebra, different labeling):
```
B_1 iso A_1 = sl(2)      (so(3) iso su(2))
D_2 iso A_1 + A_1        (so(4) iso su(2) + su(2))
D_3 iso A_3              (so(6) iso su(4))
```
This is why the series start at n=2 for B, n=4 for D — lower ranks coincide with A-series.

**D_n spinors:** The D_n Dynkin diagram has a forked end:
```
o---o---...---o
               \
                o   <- spinor node
               /
o---o---...---o

(The two branch nodes give the two spinor representations of SO(2n).)
```
The two spinor representations of SO(2n) are the "half-spinors" of dimension 2^{n-1}.

---

## The Classical Series: C_n

**C_n = sp(2n,C):** Matrices X satisfying X^T J + J X = 0 for the standard symplectic J.
- Compact form: sp(n) (compact symplectic group)
- Rank n, dim n(2n+1)
- Root system C_n: roots {pm 2e_i} (long) and {pm e_i pm e_j, i<j} (short)

**Overlap:** C_1 iso B_1 iso A_1 = sl(2). The series starts at n=3 for C (n=1,2 give A,B cases).

**Physical relevance:** The symplectic group Sp(2n,R) appears in:
- Hamiltonian mechanics (canonical transformations on phase space R^{2n})
- Metaplectic representation (projective rep of Sp(2n) — the quantum harmonic oscillator)
- Siegel modular forms (higher-genus generalization of modular forms)

---

## The Exceptional Lie Algebras

These are the five Lie algebras outside the infinite series. Each was discovered by Killing
(1888–90) and corrected by Cartan (1894).

**G_2: rank 2, dim 14**

```
Dynkin diagram: o≡≡>o  (triple bond, arrow pointing to shorter root)
Root system: 12 roots (6 short, 6 long), related to the octonions
```

G_2 is the automorphism group of the octonions O. The octonion algebra is the unique
normed division algebra in 8 dimensions (R, C, H, O — these are all normed division algebras
by Hurwitz's theorem). The octonions are non-associative, and G_2 is the group of
non-associative algebra automorphisms: { phi: O -> O : phi(xy) = phi(x)phi(y), phi is linear }.

The 7-dimensional representation of G_2 is the imaginary octonions. G_2 has compact real form G_2^c
(the 14-dim compact group) and split form G_2^* (non-compact, 14-dim).

**F_4: rank 4, dim 52**

```
Dynkin diagram: o---o==>o---o  (one double bond)
```

F_4 is related to the exceptional Jordan algebra — the 27-dimensional algebra of 3x3 Hermitian
matrices over the octonions (Albert algebra). F_4 = Aut(J_{3,O}).

**E_6: rank 6, dim 78**

```
Dynkin diagram:       o
                      |
              o---o---o---o---o
```

E_6 has 72 roots + 6 Cartan = 78 total. Appears in:
- Heterotic string theory: E_8 x E_8 gauge group; the E_6 subalgebra after compactification
- Grand unified theories: the exceptional GUT E_6 contains SU(3)xSU(2)xU(1) and predicts
  additional particles
- 27-dim fundamental representation: related to the 27 lines on a cubic surface (classical
  algebraic geometry!)

**E_7: rank 7, dim 133**

```
Dynkin diagram:           o
                          |
              o---o---o---o---o---o
```

E_7 has a 56-dim representation (the smallest non-trivial rep). Appears in:
- M-theory compactification
- Freudenthal magic square (exceptional structures from normed algebras)
- 28 bitangents to a quartic curve (classical algebraic geometry)

**E_8: rank 8, dim 248**

```
Dynkin diagram:               o
                              |
              o---o---o---o---o---o---o
```

The largest exceptional algebra. Remarkable properties:
- The adjoint representation V_{248} is the smallest non-trivial representation
  (the adjoint rep IS the smallest rep — unusual)
- The E_8 root lattice is the densest known lattice packing in 8 dimensions
- |W(E_8)| = 696,729,600
- The Cartan matrix of E_8 is the matrix of the E_8 lattice, which is self-dual

**E_8 in physics:** Heterotic string theory requires gauge group E_8 x E_8 (in 10 dimensions).
After compactification on a Calabi-Yau manifold, E_8 can break to E_6, SO(10), SU(5) — possible
grand unification groups. The 248 "dimensions" of E_8 correspond to 248 string modes.

---

## The Structure of the Proof (Killing-Cartan Classification)

The proof that the Dynkin diagrams exhaust all simple Lie algebras has several steps:

```
STEP 1: Every semisimple g decomposes into simple summands.
  (Killing form non-degenerate; decompose into orthogonal ideals)

STEP 2: Every simple g has a root system Phi.
  (Cartan subalgebra exists; simultaneous diagonalization gives roots)

STEP 3: Root systems are classified by Dynkin diagrams.
  (Geometric argument: allowed Cartan matrix entries constrain the
  diagram. Key constraint: Cartan matrix must be positive definite.
  Enumeration rules out all cases except {A,B,C,D,E,F,G}.)

STEP 4: Each Dynkin diagram comes from a unique simple Lie algebra.
  (Existence: construct g from generators and relations using the
  Serre relations. Uniqueness: the Serre relations determine g.)
```

**Serre relations:** Given a Cartan matrix A = (a_{ij}), the Serre generators are
{H_i, E_i, F_i} satisfying:
```
[H_i, H_j] = 0
[H_i, E_j] = a_{ij} E_j
[H_i, F_j] = -a_{ij} F_j
[E_i, F_j] = delta_{ij} H_i
(ad_{E_i})^{1-a_{ij}} (E_j) = 0  for i != j
(ad_{F_i})^{1-a_{ij}} (F_j) = 0  for i != j
```
These last two are the Serre relations (the "nilpotency conditions"). They impose exactly the
restrictions needed to get a finite-dimensional Lie algebra from the Cartan matrix.

---

## Real Forms

A **real form** of a complex Lie algebra g_C is a real Lie algebra g_R such that
g_R tensor_R C iso g_C. Each complex simple Lie algebra has multiple real forms.

**Types of real forms for A_n = sl(n+1,C):**

| Real form | Description | Compact? |
|-----------|-------------|---------|
| su(n+1) | skew-Hermitian traceless | Yes (compact) |
| sl(n+1,R) | real traceless matrices | No |
| su(p,q) with p+q=n+1 | indefinite signature | No |

**Cartan's classification of real forms:** Every real semisimple Lie algebra g_R has a unique
compact real form (up to conjugacy). The real forms are classified by the involutions of g_C
(Cartan involutions).

**Symmetric spaces:** The coset G/K where K is the fixed-point set of a Cartan involution is a
Riemannian symmetric space. Cartan's classification of real forms gives a classification of
symmetric spaces — there are finitely many types (A through G plus some variants).

---

## Dimension Formula Summary

| Series | dim g | rank | # roots |
|--------|--------|------|---------|
| A_n | n(n+2) | n | n(n+1) |
| B_n | n(2n+1) | n | 2n^2 |
| C_n | n(2n+1) | n | 2n^2 |
| D_n | n(2n-1) | n | 2n(n-1) |
| G_2 | 14 | 2 | 12 |
| F_4 | 52 | 4 | 48 |
| E_6 | 78 | 6 | 72 |
| E_7 | 133 | 7 | 126 |
| E_8 | 248 | 8 | 240 |

---

## Decision Cheat Sheet

| You're working with... | Lie algebra | Related group |
|-----------------------|-------------|---------------|
| n x n traceless matrices | A_{n-1} = sl(n) | SU(n) |
| (2n+1) x (2n+1) skew-sym | B_n = so(2n+1) | SO(2n+1) |
| 2n x 2n skew-sym | D_n = so(2n) | SO(2n) |
| Symplectic 2n x 2n | C_n = sp(2n) | Sp(2n) |
| Octonion automorphisms | G_2 | Exceptional G_2 |
| Heterotic string theory | E_8 | E_8 x E_8 gauge group |
| GUT model | E_6 | E_6 GUT |

---

## Common Confusion Points

**"B_n and C_n are dual":** They are Langlands dual: the coroots of B_n are the roots of C_n
and vice versa. Same Dynkin diagram shape, reversed arrow. This duality is important in the
geometric Langlands program and S-duality in gauge theory.

**"The exceptional algebras come from nowhere":** They come from the octonions. The division
algebras R, C, H, O are classified (Hurwitz's theorem). The exceptional Lie algebras arise from
the octonions via the Freudenthal-Tits magic square — a 4x4 array where each entry is a Lie
algebra built from pairs of normed division algebras. E_8 corresponds to (O,O) in this square.

**"D_3 = A_3 is a coincidence":** It is: so(6) iso su(4). The isomorphism is explicit: SU(4)
acts on the 6-dimensional space of 4x4 complex skew matrices (isomorphic to C^6), and this
action factors through SO(6). This "accidental isomorphism" is used in the AdS/CFT correspondence
(SO(6) rotation symmetry of S^5 iso SU(4) R-symmetry of N=4 SYM).

**"Compact means compact form means negative definite Killing form":** Yes. The compact real
form of g_C has negative definite Killing form. The correspondence: compact Lie group G
has Lie algebra g_R where B is negative definite. This is also why SU(n), SO(n), Sp(n) have
nice finite-dimensional representation theory.
