# Algebraic Number Theory

## The Big Picture

```
+====================================================================+
|        THE PROGRAM: FIX UNIQUE FACTORIZATION                       |
+====================================================================+
|                                                                    |
|  Z: unique factorization holds ✓                                   |
|  Z[√-5]: FAILS — 6 = 2·3 = (1+√-5)(1-√-5)                       |
|                                                                    |
|  REMEDY: Factor IDEALS, not elements.                              |
|                                                                    |
|  Every nonzero ideal in O_K factors uniquely as product of         |
|  prime ideals.  ← The Dedekind factorization theorem              |
|                                                                    |
|  MEASURE OF FAILURE:                                               |
|  Class group Cl(K) = {fractional ideals} / {principal ideals}     |
|  |Cl(K)| = h_K (class number)                                     |
|  h_K = 1 ⟺ O_K is a PID ⟺ unique element factorization           |
|                                                                    |
|  HIERARCHY:                                                        |
|  Euclidean domain → PID → UFD → integral domain                   |
|  Z is Euclidean (so PID, so UFD)                                  |
|  Z[√-5]: not UFD, not PID, h = 2                                  |
|  Z[i] (Gaussian integers): h = 1 → PID, unique factorization ✓   |
+====================================================================+
```

---

## Number Fields

```
DEFINITION: A number field K is a finite extension of Q.
  K = Q(α) for some algebraic number α (root of an irreducible f ∈ Q[x]).
  [K:Q] = deg(f) = degree of K over Q.

EXAMPLES:
  Q(√2) = {a + b√2 : a,b ∈ Q}    degree 2  (real quadratic field)
  Q(√-1) = Q(i) = {a+bi : a,b ∈ Q}  degree 2  (Gaussian rationals)
  Q(√-5) = {a + b√-5 : a,b ∈ Q}   degree 2  (class number 2)
  Q(ζₙ) where ζₙ = e^{2πi/n}        degree φ(n)  (cyclotomic field)
  Q(∛2) = {a+b∛2+c∛4 : a,b,c ∈ Q}  degree 3  (cubic field)

CLASSIFICATION OF QUADRATIC FIELDS Q(√d), d squarefree:
  d > 0: real quadratic field (two real embeddings, unit group infinite)
  d < 0: imaginary quadratic field (complex conjugate pair, unit group finite)

EMBEDDINGS:
  A degree-n field K has exactly n embeddings K → C.
  r₁ = number of real embeddings
  2r₂ = number of complex (non-real) embeddings
  r₁ + 2r₂ = n
```

---

## Rings of Integers

```
DEFINITION: O_K = ring of algebraic integers of K
  = {α ∈ K : α satisfies a monic polynomial with Z coefficients}

O_K is a free Z-module of rank n = [K:Q].
It has an integral basis {ω₁, ..., ωₙ}: every element = Σ aᵢωᵢ, aᵢ ∈ Z.

EXAMPLES:
  K = Q:                 O_K = Z
  K = Q(√d), d ≡ 2,3 (mod 4):  O_K = Z[√d] = {a+b√d : a,b ∈ Z}
  K = Q(√d), d ≡ 1 (mod 4):    O_K = Z[(1+√d)/2]  ← note: NOT Z[√d]!

  d=5: O_K = Z[(1+√5)/2] — includes the golden ratio φ = (1+√5)/2.
  d=-3: O_K = Z[(1+√-3)/2] = Z[ω] where ω = e^{2πi/3}.
  d=-1: O_K = Z[i] (Gaussian integers).
  d=-5: O_K = Z[√-5].

Cyclotomic: O_{Q(ζₙ)} = Z[ζₙ].

DISCRIMINANT Δ_K:
  det[σᵢ(ωⱼ)]² where σᵢ are the embeddings.
  Measures how "spread" the ring is.
  |Δ_K| grows with K; Minkowski: |Δ_K| ≥ some bound depending on n.
```

### Norm and Trace

```
NORM: N_{K/Q}(α) = ∏_{σ:K→C} σ(α)  (product over all embeddings)
TRACE: Tr_{K/Q}(α) = Σ_{σ:K→C} σ(α)

For K = Q(√d):
  N(a+b√d) = a² - db²
  Tr(a+b√d) = 2a

Properties:
  N(αβ) = N(α)N(β)  (multiplicative)
  Tr(α+β) = Tr(α) + Tr(β)  (linear)
  N(α) ∈ Z for α ∈ O_K
  α is a unit in O_K ⟺ N(α) = ±1

Units in Z[√-5]:
  N(a+b√-5) = a² + 5b² = ±1 → only a=±1, b=0.
  Units: {±1} only.

Units in Z[√2]:
  N(a+b√2) = a² - 2b² = ±1 → Pell equation!
  Fundamental unit: 1+√2, N(1+√2) = 1-2 = -1.
  All units: ±(1+√2)^k, k ∈ Z.  (Infinite unit group)
```

---

## Ideal Factorization

### Why Elements Fail

```
In Z[√-5]:
  2 · 3 = (1+√-5)(1-√-5) = 6
  All four factors are irreducible (no way to factor further in O_K).
  Euclid's lemma fails for 2: 2 | (1+√-5)(1-√-5) but 2 ∤ (1+√-5).

In terms of ideals:
  (2)   = p₁ · p̄₁  where p₁ = (2, 1+√-5)
  (3)   = p₂ · p̄₂  where p₂ = (3, 1+√-5)
  (1+√-5) = p₁ · p₂
  (1-√-5) = p̄₁ · p̄₂

So: (6) = (2)·(3) = p₁·p̄₁·p₂·p̄₂ = (1+√-5)·(1-√-5) ← same ideal factorization!
The apparent non-uniqueness in elements is resolved in ideals.
```

### Prime Ideal Factorization

```
DEDEKIND'S THEOREM:
  Every nonzero ideal I ⊆ O_K factors uniquely as:
  I = p₁^{e₁} · p₂^{e₂} · ... · pₖ^{eₖ}  (pᵢ distinct prime ideals, eᵢ ≥ 1)

HOW A RATIONAL PRIME p SPLITS IN O_K:
  Write pO_K = p₁^{e₁} · ... · pₖ^{eₖ}

  Each prime pᵢ above p has a residue field: O_K/pᵢ ≅ F_{p^{fᵢ}}
  The INERTIA DEGREE fᵢ = [O_K/pᵢ : F_p].
  IDENTITY: Σ eᵢfᵢ = [K:Q]

TYPES OF SPLITTING (for K = Q(√d), degree 2):
  p SPLITS:    pO_K = p₁·p₂, two distinct primes, e=1, f=1+1=2 ✓
  p INERT:     pO_K = p, prime stays prime, e=1, f=2
  p RAMIFIES:  pO_K = p², one prime squared, e=2, f=1

  Criterion (for Q(√d)):
    p splits     iff (d/p) = 1  (d is QR mod p)
    p is inert   iff (d/p) = -1 (d is QNR mod p)
    p ramifies   iff p | Δ_K
```

### Example: Splitting in Q(√-5)

```
K = Q(√-5), Δ_K = -20.

Ramified primes: divisors of 20 = {2, 5}.
  2O_K = (2, 1+√-5)² = p₁²
  5O_K = (5, √-5)²   = p₂²

For other primes p, use Legendre symbol (-5/p) = (-1/p)(5/p):
  p=3: (-5/3) = (-2/3) = (-1/3)(2/3) = ...
    (-1/3) = (-1)^{(3-1)/2} = (-1)^1 = -1
    (2/3) = (-1)^{(9-1)/8} = (-1)^1 = -1
    (-5/3) = (-1)(-1) = 1 → 3 SPLITS
  p=7: (-5/7) = (-1/7)(5/7)
    (-1/7) = (-1)^3 = -1
    (5/7) = (7/5)(-1)^{2·3} = (7/5) = (2/5) = (-1)^{(25-1)/8} = (-1)^3 = -1
    (-5/7) = (-1)(-1) = 1 → 7 SPLITS
  p=11: (-1/11)=1, (5/11): (5/11)(11/5) = (-1)^{5·2}=1, (11/5)=(1/5)=1, so (5/11)=1
    (-5/11) = 1·1 = 1 → 11 SPLITS
  p=13: (-5/13) = (-1/13)(5/13)
    (-1/13) = (-1)^6 = 1
    (5/13)(13/5) = (-1)^{6·2}=1, (13/5)=(3/5), (3/5)(5/3)=(-1)^{1·2}=1
    (5/3) = (2/3) = -1, so (3/5) = -1/(−1) = 1... Let me recompute:
    (5/13): 5^6 mod 13 = 5,25≡12,60≡8,40≡1 → 5^6 ≡ ... checking: 5²=25≡12,
    5³≡60≡8,5^6≡64≡12≡-1 → (5/13)=-1.
    (-5/13) = 1·(-1) = -1 → 13 IS INERT in Q(√-5).
```

---

## The Class Group

```
DEFINITION:
  A fractional ideal is a nonzero O_K-submodule I ⊆ K with dI ⊆ O_K for some d ∈ Z.
  Fractional ideals form a group under ideal multiplication.
  Principal fractional ideals: I = αO_K for α ∈ K*.

  Cl(K) = {fractional ideals of O_K} / {principal fractional ideals}
         = Pic(Spec O_K)  [scheme-theoretic view]

  h_K = |Cl(K)|  (class number)
  h_K = 1  ⟺  O_K is a PID  ⟺  unique element factorization

CLASS NUMBERS (imaginary quadratic Q(√-d)):
  d:     1  2  3  5  6  7  10  11  13  14  15  17  19  23  ...  163
  h:     1  1  1  2  2  1   2   1   2   4   2   4   1   3  ...    1

The nine imaginary quadratic fields Q(√-d) with h=1 (Stark-Heegner theorem):
  d = 1, 2, 3, 7, 11, 19, 43, 67, 163

GAUSS'S CONJECTURE (proved 1966-1967 by Baker and Stark):
  Only finitely many imaginary quadratic fields with any given class number.
  Explicitly determined for h=1,2,3,...
```

### Class Group Computation

```
MINKOWSKI'S THEOREM: Every ideal class contains an ideal of norm ≤ M_K,
where M_K is the Minkowski bound:

  M_K = (4/π)^{r₂} · (n!/n^n) · √|Δ_K|  (simplified)

For Q(√-d): M_K ≈ (2/π)√d.

To compute Cl(K):
  1. Compute M_K.
  2. Factor all rational primes p ≤ M_K into prime ideals.
  3. These prime ideals GENERATE Cl(K).
  4. Find relations among them (via norm computations).

Example: K = Q(√-5), |Δ|=20, M_K ≈ (2/π)√5 ≈ 1.42 · 2.24 ≈ 2.85.
  Only need primes p ≤ 2.
  (2) = (2, 1+√-5)² — gives one prime ideal p₁ = (2, 1+√-5).
  p₁² = (2) — principal. So p₁ has order ≤ 2 in Cl.
  Is p₁ principal? Need α with N(α) = 2, i.e., a²+5b²=2 → impossible.
  So p₁ has order exactly 2 in Cl(K).
  Cl(Q(√-5)) = Z/2, h=2. ✓
```

---

## Dirichlet's Unit Theorem

```
O_K* (units of O_K) ≅ μ_K × Z^{r₁+r₂-1}

where:
  μ_K = finite cyclic group of roots of unity in K
  r₁ = # real embeddings K → R
  r₂ = # conjugate pairs of complex embeddings
  r₁ + 2r₂ = [K:Q]

UNIT RANK = r₁ + r₂ - 1:
  Imaginary quadratic (r₁=0, r₂=1): rank 0+1-1 = 0 → finite unit group
    Q(√-1): units = {±1, ±i} = Z/4
    Q(√-3): units = {±1, ±ω, ±ω²} = Z/6
    Most Q(√-d): units = {±1} = Z/2
  Real quadratic (r₁=2, r₂=0): rank 2+0-1 = 1 → unit group = {±1}×Z
    Fundamental unit ε₁ generates the infinite part.
    Q(√2): ε₁ = 1+√2 (fundamental unit)
    Q(√5): ε₁ = (1+√5)/2 = φ (golden ratio)
  Totally real cubic (r₁=3, r₂=0): rank 2 → two fundamental units.
```

---

## Class Field Theory — Overview

```
ABELIAN EXTENSIONS OF Q (Kronecker-Weber, 1886):
  Every abelian extension of Q is contained in a cyclotomic field Q(ζₙ).
  Equivalently: Gal(Q^{ab}/Q) ≅ Ẑ* = ∏_p Z_p*.

CLASS FIELD THEORY (Hilbert, Takagi, Artin 1920s):
  Generalizes to: for a number field K, abelian extensions of K
  are controlled by generalized class groups (idèle class groups).

  The Artin map: for each prime p of K, associates a Frobenius element
  Frob_p ∈ Gal(L/K) for any abelian extension L/K.
  The product formula: the Artin map is surjective and controlled by
  arithmetic of K.

CONNECTION TO QUADRATIC RECIPROCITY:
  QR is a SPECIAL CASE of Artin reciprocity!
  The Legendre symbol (p/q) is the Frobenius of p in Q(√q)/Q.
  QR says: Frob_p in Q(√q)/Q is related to Frob_q in Q(√p)/Q.
  The sign is determined by the ramification at ∞ (the "place at infinity").
```

---

## Connections to Lattice Cryptography

```
IDEAL LATTICES:
  An ideal I ⊆ O_K is also a lattice in K ⊗ R ≅ R^n.
  "Shortest vector" in I = short element of O_K.
  SVP in ideal lattices ← hard problem (but structured)

RING-LWE (Learning With Errors over rings):
  Sample: (a, b = a·s + e) where a,b ∈ O_K/(q), s is the secret, e is error
  Security reduces to worst-case problems on ideal lattices in Q(ζₙ).
  Used in: CRYSTALS-Kyber (KEM), CRYSTALS-Dilithium (signatures) — both NIST PQC standards.

THE CLASS GROUP RELEVANCE:
  Attacks on ring-LWE relate to distinguishing ideal classes.
  NTRU uses special ideals in number rings.
  If O_K has large class number h_K, there are more distinct ideal types —
  this affects both the hardness and the implementation.
```

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Find O_K for Q(√d) | Z[√d] if d≡2,3 mod 4; Z[(1+√d)/2] if d≡1 mod 4 |
| Check if p splits/inerts/ramifies in Q(√d) | Legendre symbol (d/p) and divisors of Δ |
| Compute norm of element | a²-db² for Q(√d) |
| Find units in Q(√d), d>0 | Fundamental unit via Pell equation x²-dy²=±1 |
| Compute class number h_K | Factor primes ≤ Minkowski bound, find relations |
| Determine if O_K is a PID | h_K = 1 |
| Understand ideal factorization failure | Class group Cl(K) measures the failure |
| Connect to post-quantum crypto | Ring-LWE, NTRU ← ideal lattice problems |

---

## Common Confusion Points

**"O_K is always Z[α] where K = Q(α)."**
False. The ring of integers O_K may not be monogenic (generated by one element).
Even when it is (as for most quadratic fields), the generator depends on the
discriminant: Q(√5) has O_K = Z[(1+√5)/2], not Z[√5].

**"Class number h_K = 1 is typical."**
For imaginary quadratic fields Q(√-d), only 9 values of d give h=1
(Stark-Heegner). For real quadratic fields, h=1 is more common but still
special. For higher degree fields, class numbers grow.

**"Ideal factorization is just like element factorization."**
Not quite: you can multiply ideals, but you can't "add" them (as elements).
The ideal product I·J = {Σ aᵢbⱼ : aᵢ ∈ I, bⱼ ∈ J} is not pointwise product.
And a prime ideal p does NOT imply p is generated by a prime element.

**"Minkowski's bound is the bound on element norms."**
It's a bound on ideal norms: every ideal class contains an ideal of norm
≤ M_K. This is used to compute the class group finitely (only finitely
many prime ideals of bounded norm need be checked).
