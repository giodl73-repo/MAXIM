# Polynomials and Fields

## The Big Picture

```
+====================================================================+
|         FIELD EXTENSIONS — THE TOWER                               |
+====================================================================+
|                                                                    |
|                    ALGEBRAICALLY CLOSED                           |
|            (every polynomial splits into linear factors)          |
|                C, F̄_p (algebraic closure)                         |
|                         /                                         |
|              ALGEBRAIC EXTENSION                                  |
|              (adjoin roots of polynomials)                        |
|                      /  |                                         |
|         Q(√2, √3) ...   |  Q(i) ...  F_{p^n}                    |
|                  \      |        /                                |
|                  GROUND FIELD: Q, F_p, R                          |
|                                                                    |
|  [K:F] = degree of extension = dim_F K as F-vector space          |
|                                                                    |
|  K algebraic over F: every α ∈ K satisfies f(α)=0 for f ∈ F[x]  |
|  K transcendental extension: exists α ∈ K satisfying no poly over F|
+====================================================================+
```

---

## Fields — Definition and Basic Examples

```
FIELD: A commutative ring F where every nonzero element has a multiplicative inverse.
  Equivalently: F is a commutative ring with at least two elements (0 ≠ 1),
  and (F\{0}, ×) is an abelian group.

CHARACTERISTIC: char(F) = smallest n with 1+1+...+1 (n times) = 0.
  If no such n: char(F) = 0.
  char(F) is always 0 or prime.

char = 0:  Q, R, C, Q(√2), number fields.
char = p:  F_p = Z/pZ, F_{p^n} (finite fields), F_p(x) (rational functions).

PRIME FIELD:
  char 0: contains Q as smallest subfield.
  char p: contains F_p = Z/pZ as smallest subfield.

FINITE FIELDS:
  F_{p^n} = GF(p^n) exists and is UNIQUE (up to isomorphism) for every prime p and n≥1.
  |F_{p^n}| = p^n.
  (F_{p^n})* is cyclic of order p^n - 1 (primitive element theorem).
  Subfields: F_{p^m} ⊆ F_{p^n} iff m | n.
  F_{p^n} ≅ F_p[x]/(f) for any irreducible f of degree n over F_p.
```

---

## Polynomial Rings over Fields

```
F[x] for field F:
  Euclidean domain with d(f) = deg(f).
  → PID: every ideal is principal.
  → UFD: unique factorization into irreducibles.

DIVISION ALGORITHM:
  For f,g ∈ F[x], g ≠ 0: ∃! q,r: f = qg + r, deg(r) < deg(g) (or r=0).

ROOT THEOREM (Factor Theorem):
  c ∈ F is a root of f(x) iff (x-c) | f(x).

MULTIPLICITY:
  c is a root of multiplicity m if (x-c)^m | f(x) but (x-c)^{m+1} ∤ f(x).
  f has at most deg(f) roots in F (counting multiplicity).
  Proof: deg(f) = n, and F[x] is a UFD.

FACTORIZATION BY DEGREE:
  Over C (algebraically closed): every f = product of linear factors.
  Over R: every f = product of linear and irreducible quadratic factors.
  Over Q: factorization can be complicated; irreducible polynomials of any degree exist.
  Over F_p: every element of F_p is a root of x^p - x; x^{p^n}-x = product of
    all monic irreducibles of degree dividing n over F_p.
```

### Irreducibility Tests

```
Over Q:
  1. Rational Root Theorem: if f = aₙxⁿ+...+a₀ ∈ Z[x] has rational root p/q (reduced),
     then p|a₀ and q|aₙ. Eliminates most candidate roots.

  2. Eisenstein's Criterion: f = aₙxⁿ+...+a₀ is irreducible over Q if ∃ prime p:
     p ∤ aₙ, p|aₙ₋₁,...,p|a₀, p²∤a₀.
     Example: x^p - p is Eisenstein (for prime p). x⁴+x³+x²+x+1 is not directly
       Eisenstein, but substituting x=y+1 gives y⁴+5y³+10y²+10y+5, Eisenstein at p=5.

  3. Reduction mod p: if f mod p is irreducible over F_p for some prime p
     (and degrees match), then f is irreducible over Q.

  4. For degree 2 or 3: irreducible iff no roots (in Q or R respectively).

Over F_p:
  Berlekamp or Cantor-Zassenhaus algorithms (polynomial time).
```

---

## Field Extensions

```
DEFINITION: K is a field extension of F, written K/F, if F ⊆ K and K is a field.

DEGREE: [K:F] = dimₐF K (as F-vector space).
  Finite if [K:F] < ∞; otherwise infinite.

TOWER LAW:
  If F ⊆ K ⊆ L (tower of extensions):
  [L:F] = [L:K] · [K:F].

EXAMPLE:
  Q ⊆ Q(√2) ⊆ Q(√2, √3).
  [Q(√2):Q] = 2 (basis {1, √2}).
  [Q(√2,√3):Q(√2)] = 2 (√3 ∉ Q(√2); basis {1, √3} over Q(√2)).
  [Q(√2,√3):Q] = 4 (basis {1, √2, √3, √6}).
```

### Algebraic Extensions

```
α ∈ K is ALGEBRAIC over F if ∃f(x) ∈ F[x], f ≠ 0, with f(α) = 0.
α is TRANSCENDENTAL over F if no such f exists.

MINIMAL POLYNOMIAL of α over F:
  The unique monic irreducible polynomial m_{α,F}(x) ∈ F[x] with m_{α,F}(α) = 0.
  [F(α):F] = deg(m_{α,F}).

  F(α) = F[x]/(m_{α,F}) as a field.  ← key construction

EXAMPLES:
  √2 over Q: m = x²-2. [Q(√2):Q] = 2.
  i over R: m = x²+1. [C:R] = 2.
  ∛2 over Q: m = x³-2. [Q(∛2):Q] = 3.
  ζ₅ = e^{2πi/5} over Q: m = x⁴+x³+x²+x+1 (5th cyclotomic polynomial). [Q(ζ₅):Q] = 4.
  π over Q: transcendental (Lindemann, 1882). No algebraic extension Q(π)/Q is finite.
  e over Q: transcendental (Hermite, 1873).

ALGEBRAIC EXTENSION: every element is algebraic over F.
  Finite extensions are algebraic.
  Algebraic numbers Ā = {α ∈ C : α algebraic over Q}: infinite algebraic extension of Q.
```

### Simple Extensions

```
Simple extension: K = F(α) for a single element α.

When α is algebraic with minimal polynomial m(x) of degree n:
  F(α) ≅ F[x]/(m(x))
  Basis: {1, α, α², ..., α^{n-1}}.
  Addition: componentwise.
  Multiplication: reduce using m(α) = 0.

Example: Q(√2):
  Basis {1, √2}.
  (a + b√2)(c + d√2) = (ac+2bd) + (ad+bc)√2.
  Inverse of (a+b√2): 1/(a+b√2) = (a-b√2)/(a²-2b²).  [norm = a²-2b²]

Example: GF(4) = F_2(α) where α² + α + 1 = 0 (m irreducible over F_2):
  Elements: {0, 1, α, α+1}.
  Multiplication: α² = α+1, (α+1)α = α²+α = (α+1)+α = 1, etc.
  Note: GF(4)* is cyclic of order 3: α has order 3 (α, α², α³=1).
```

---

## Splitting Fields

```
SPLITTING FIELD of f(x) over F:
  Smallest extension K/F over which f splits into linear factors.
  K = F(α₁,...,αₙ) where f(x) = a·∏(x-αᵢ) in K[x].

EXISTENCE AND UNIQUENESS:
  Every polynomial over F has a splitting field.
  Splitting field is unique up to isomorphism fixing F.

EXAMPLES:
  f = x²-2 over Q: splitting field = Q(√2) (roots ±√2, both in Q(√2)).
  f = x³-2 over Q: splitting field = Q(∛2, ω) where ω = e^{2πi/3}.
    [Q(∛2, ω):Q] = 6.  (Roots: ∛2, ω∛2, ω²∛2.)
  f = x^p - 1 over Q: splitting field = Q(ζ_p).  [Q(ζ_p):Q] = p-1.
  f = xⁿ - a over Q: splitting field = Q(a^{1/n}, ζ_n).

NORMAL EXTENSION: K/F is normal if K is the splitting field of some f ∈ F[x].
  Equivalently: every irreducible polynomial over F that has one root in K
  splits completely in K.
```

---

## Algebraic Closure

```
F̄ (algebraic closure of F):
  Algebraically closed: every polynomial in F̄[x] has a root in F̄.
  Algebraic over F: every element satisfies a polynomial over F.
  Unique up to isomorphism over F.

EXAMPLES:
  Q̄ = algebraic numbers (all algebraic numbers).  [Q̄:Q] = ∞.
  R̄ = C.  [C:R] = 2.
  F̄_p = union of all GF(p^n).  Infinite.

Algebraically closed fields have no proper algebraic extensions.
C is algebraically closed (Fundamental Theorem of Algebra).
R is NOT: x²+1 has no real roots.
Q is NOT: x²-2 has no rational roots.
```

---

## Finite Fields

```
GF(p^n) = F_{p^n} — the unique finite field of order p^n.

CONSTRUCTION: F_p[x]/(f) where f is any irreducible polynomial of degree n over F_p.
  Multiple choices of f give isomorphic fields (but different "coordinate systems").

PROPERTIES:
  All elements satisfy x^{p^n} = x.
  (F_{p^n})* = cyclic group of order p^n - 1.
  Frobenius automorphism: φ(x) = x^p is a field automorphism of F_{p^n}.
  Gal(F_{p^n}/F_p) = ⟨Frobenius⟩ ≅ Z/nZ.  ← cyclic, generated by Frobenius.

SUBFIELDS: F_{p^m} ⊆ F_{p^n} iff m | n.
  Lattice of subfields = divisibility lattice of divisors of n.

APPLICATIONS:
  F_2 = GF(2): binary arithmetic.
  GF(2^8): AES byte operations (irreducible polynomial x^8+x^4+x^3+x+1).
  GF(2^m) or GF(p^m): Reed-Solomon codes, BCH codes, elliptic curves.

FACTORING x^n - 1 OVER F_p:
  x^{p^n} - x = product of all monic irreducibles of degree | n over F_p.
  x^{p^n-1} - 1 = product of all monic irreducibles of degree | n.
  This gives: # monic irreducibles of degree n over F_p = (1/n) Σ_{d|n} μ(n/d)p^d.
```

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Find degree [F(α):F] | deg(minimal polynomial of α over F) |
| Check if α is algebraic | Find polynomial f ∈ F[x] with f(α)=0 |
| Check irreducibility over Q | Rational root theorem, Eisenstein, reduction mod p |
| Construct GF(p^n) | F_p[x]/(f) for irreducible f of degree n |
| Find splitting field of f | Adjoin all roots of f; check degree using tower law |
| Determine char(F) | 1+1+...=0 first time, or 0 if never |
| Count elements of GF(p^n) | Exactly p^n |
| Find order of α in GF(p^n)* | Find smallest k with α^k=1; must divide p^n-1 |
| Primitive element of GF(p^n)* | Generator of cyclic group; order p^n-1 |

---

## Common Confusion Points

**"Q(√2, √3) has degree 4, but √6 = √2·√3 ∈ Q(√2,√3), so why isn't the degree 3?"**
The degree is determined by the dimension as a vector space, not by the number of
generators. Q(√2,√3) has basis {1,√2,√3,√6} — dimension 4. The fact that √6
is in this field doesn't reduce the dimension.

**"Algebraic extensions and finite extensions are the same."**
Finite extensions (finite degree [K:F]) are algebraic. But algebraic extensions
can be infinite: the algebraic closure Q̄ over Q has infinite degree.
Every element satisfies a polynomial over Q, but the extension is infinite-dimensional
as a vector space.

**"GF(4) = {0,1,2,3}."**
GF(4) has characteristic 2, so it cannot contain 2 or 3 as distinct non-zero elements
(since 1+1=0 in characteristic 2). GF(4) = {0,1,α,α+1} where α²+α+1=0.
The integers mod 4 form Z/4Z, which is NOT a field (2·2 = 4 ≡ 0 — zero divisor).

**"Splitting fields and algebraic closures are the same."**
The splitting field of a specific polynomial f is the smallest field over which f splits.
The algebraic closure is the splitting field of ALL polynomials simultaneously.
Splitting field of x⁴-2 over Q has degree 8; Q̄ has infinite degree.
