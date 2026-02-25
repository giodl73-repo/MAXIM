# Quadratic Reciprocity

## The Big Picture

```
+====================================================================+
|           QUADRATIC RESIDUES AND RECIPROCITY                       |
+====================================================================+
|                                                                    |
|  QUESTION: Is a a perfect square mod p?                           |
|  i.e., does x² ≡ a (mod p) have a solution?                      |
|                                                                    |
|  LEGENDRE SYMBOL:                                                  |
|     (a/p) = { 1  if a is QR mod p (and p∤a)                      |
|             { -1 if a is QNR mod p                                |
|             { 0  if p | a                                         |
|                                                                    |
|  EULER'S CRITERION:  (a/p) ≡ a^{(p-1)/2} (mod p)                 |
|                                                                    |
|  GAUSS'S GOLDEN THEOREM (Quadratic Reciprocity):                  |
|  For distinct odd primes p, q:                                     |
|     (p/q)(q/p) = (-1)^{(p-1)/2 · (q-1)/2}                        |
|                                                                    |
|  SUPPLEMENTS:                                                      |
|     (-1/p) = (-1)^{(p-1)/2}  →  QR iff p ≡ 1 (mod 4)            |
|     ( 2/p) = (-1)^{(p²-1)/8} →  QR iff p ≡ ±1 (mod 8)           |
+====================================================================+
```

Quadratic reciprocity is the "crown jewel" of elementary number theory —
Gauss called it his "theorema aureum" (golden theorem) and gave at least
8 proofs. It answers whether solving x² ≡ p (mod q) is related to solving
x² ≡ q (mod p) — a non-obvious connection between two different primes.

---

## Quadratic Residues

```
a is a quadratic residue (QR) mod p if:
  gcd(a,p) = 1  AND  ∃x: x² ≡ a (mod p)

Otherwise a is a quadratic non-residue (QNR) mod p.

Count: exactly (p-1)/2 QRs and (p-1)/2 QNRs in (Z/pZ)*.

Why (p-1)/2? The map x ↦ x² on (Z/pZ)* is 2-to-1:
  x² = (-x)² mod p (since (-1)² = 1)
  So the image has (p-1)/2 elements — exactly the QRs.

QR × QR = QR
QR × QNR = QNR
QNR × QNR = QR
(Multiplication rule — analogous to +/- for signs)
```

### Finding Square Roots mod p

```
TONELLI-SHANKS ALGORITHM: Given a QR a mod p, find √a.

Case 1: p ≡ 3 (mod 4)  [simplest]
  √a ≡ a^{(p+1)/4} (mod p)
  (Because (a^{(p+1)/4})² = a^{(p+1)/2} = a · a^{(p-1)/2} = a · 1 = a)

Case 2: p ≡ 1 (mod 4)  [requires Tonelli-Shanks]
  Write p-1 = 2^s · q with q odd.
  Find a non-residue n (random search, 50% chance each try).
  Use lifting algorithm to compute √a.
  O(log² p) expected.

Application: ECDSA signature verification requires square roots in F_p.
  Point decompression (recover y from x on elliptic curve): needs √(x³+ax+b) mod p.
```

---

## The Legendre Symbol

```
(a/p) — pronounced "a over p" or "the Legendre symbol of a with respect to p"

DEFINITION:
  (a/p) = 0     if p | a
  (a/p) = 1     if a is QR mod p (a ≢ 0)
  (a/p) = -1    if a is QNR mod p

COMPUTATION — Euler's criterion:
  (a/p) ≡ a^{(p-1)/2} (mod p)
  This is +1 or -1 (or 0), so the congruence gives exact equality.

PROPERTIES:
  Completely multiplicative: (ab/p) = (a/p)(b/p)
  (a²/p) = 1 for all a with p∤a  (squares are always QRs)
  (a/p) = (b/p) if a ≡ b (mod p)  (well-defined on Z/pZ)
  Σ_{a=0}^{p-1} (a/p) = 0  (equal QRs and QNRs cancel)

EXAMPLES:
  Is 6 a QR mod 13?
  (6/13) = (2/13)(3/13)
  (2/13): 13 ≡ 5 (mod 8) → (-1)^{(169-1)/8} = (-1)^{21} = -1 → 2 is QNR mod 13
  (3/13): by QR: (3/13)(13/3) = (-1)^{1·6} = 1, so (3/13) = (13/3) = (1/3) = 1
  (6/13) = (-1)(1) = -1 → 6 is QNR mod 13. Verify: 6^6 ≡ ? (mod 13)
  6² = 36 ≡ 10, 6³ ≡ 60 ≡ 8, 6^6 ≡ 64 ≡ 12 ≡ -1 (mod 13) ✓
```

---

## Quadratic Reciprocity — The Golden Theorem

### Statement

```
For distinct odd primes p and q:

  (p/q) · (q/p) = (-1)^{(p-1)/2 · (q-1)/2}

Equivalently:
  (p/q) · (q/p) = -1  if p ≡ q ≡ 3 (mod 4)
  (p/q) · (q/p) = +1  otherwise

So:
  If p ≡ 1 (mod 4) OR q ≡ 1 (mod 4): (p/q) = (q/p)   [they agree]
  If p ≡ q ≡ 3 (mod 4): (p/q) = -(q/p)               [they disagree]
```

### What This Means

```
Is 3 a QR mod 11?

Direct: compute 3^5 mod 11.
  3^2=9, 3^4=81≡4, 3^5≡12≡1 (mod 11). So (3/11) = 1. Yes.

Using QR:
  p=3 ≡ 3 (mod 4), q=11 ≡ 3 (mod 4). Both ≡ 3 (mod 4).
  So (3/11) = -(11/3) = -(11 mod 3 / 3) = -(2/3)
  2 mod 3: is 2 a QR mod 3? 1²=1, 2²=4≡1 → only QR is 1. So (2/3) = -1.
  (3/11) = -(-1) = 1 ✓
```

### The Computational Payoff

```
Without QR: Computing (a/p) requires computing a^{(p-1)/2} mod p.
  For 100-digit p: still fast, but requires p-1 factored.

With QR (Jacobi symbol algorithm):
  Like Euclidean algorithm, reduces (a/p) in O(log a · log p) steps.
  Never need a^{(p-1)/2}.

QR as a recursive reduction:
  (a/p) where a < p:
    If a = 1: return 1
    If a = 2: use supplement
    If a is even: (a/p) = (2/p)(a/2 / p)  [multiplicativity]
    If a is odd: use QR to flip, reduce a mod p, recurse
```

---

## The Jacobi Symbol

```
DEFINITION: For odd n > 0 with n = p₁^{a₁} · ... · pₖ^{aₖ}:
  (a/n) = (a/p₁)^{a₁} · ... · (a/pₖ)^{aₖ}

CRITICAL DIFFERENCE from Legendre:
  (a/n) = 1 does NOT imply a is a QR mod n.
  (a/n) = -1 DOES imply a is a QNR mod n.
  (a/n) = 0 iff gcd(a,n) > 1.

Example: (2/9) = (2/3)² = (-1)² = 1, but x²≡2(mod 9) has no solution.

PROPERTIES (same as Legendre):
  (ab/n) = (a/n)(b/n)
  (a/mn) = (a/m)(a/n)

QUADRATIC RECIPROCITY FOR JACOBI:
  For odd coprime m,n > 0:
  (m/n)(n/m) = (-1)^{(m-1)/2 · (n-1)/2}

  Supplements hold:
  (-1/n) = (-1)^{(n-1)/2}
  (2/n) = (-1)^{(n²-1)/8}

This gives an O(log n) algorithm to compute (a/n) without factoring n.
```

### Jacobi Symbol Algorithm (Eisenstein/Gauss)

```
function jacobi(a, n):
  assert n > 0 and n is odd
  if n == 1: return 1
  a = a mod n
  if a == 0: return 0
  result = 1
  while a != 0:
    while a is even:
      a /= 2
      if n mod 8 in {3, 5}: result = -result  // (2/n) supplement
    swap a, n
    if a mod 4 == 3 and n mod 4 == 3: result = -result  // QR flip sign
    a = a mod n
  if n == 1: return result
  else: return 0

Runs in O(log² max(a,n)) — same as Euclidean algorithm.
No factorization needed.
```

---

## Applications

### Solovay-Strassen Primality Test

```
If n is prime and gcd(a,n) = 1:
  (a/n) ≡ a^{(n-1)/2} (mod n)   [Euler's criterion]

If n is composite, this may fail.

Test: Choose random a. Compute:
  LHS: Jacobi symbol (a/n)  — fast with algorithm above
  RHS: a^{(n-1)/2} mod n    — fast with square-and-multiply
  If LHS ≢ RHS: n is COMPOSITE (with certainty)
  If LHS ≡ RHS: n is probably prime ("Euler pseudoprime" to base a)

Error probability: < 1/2 per test. After k tests: < (1/2)^k.
Replaced in practice by Miller-Rabin (stronger — detects more composites).
```

### Euler's Criterion as Quadratic Residue Check

```
Fast QR test in cryptographic implementations:
  Is a a QR mod p?
  Compute a^{(p-1)/2} mod p.
  Result is 1 (QR) or -1 ≡ p-1 (QNR).
  O(log p) multiplications.

Used in:
  - Deterministic point generation for ECC (Elligator, hash-to-curve)
  - Deciding which of two candidate y-values to use when decompressing
    an EC point
  - Checking if DSA/ECDSA nonces are safe
```

### Quadratic Residue Assumption in Cryptography

```
The QR assumption: given n=pq and a chosen QNR mod n,
  it's computationally hard to distinguish QRs from QNRs mod n.

(Without knowing p and q, computing (a/n) = (a/p)(a/q) requires
  knowing the factorization.)

Applications:
  - Goldwasser-Micali encryption: encrypt 0 as random QR, 1 as QNR
    Decryption: check if c is QR mod p (using Legendre symbol with p known)
  - Blum integers: n = pq with p≡q≡3(mod 4) — used in BBS PRNG
  - QR-based oblivious transfer protocols
```

---

## Higher Reciprocity Laws

```
Gauss also proved BIQUADRATIC reciprocity (4th power symbols).
Eisenstein proved CUBIC reciprocity.
Hilbert unified all: the HILBERT SYMBOL and PRODUCT FORMULA.

The general framework: CLASS FIELD THEORY.
  Artin's reciprocity (1927) generalizes QR to all number fields.
  The Legendre symbol (p/q) becomes an Artin symbol Frob_p in Gal(Q(√q)/Q).
  The product formula Π_v (a,b)_v = 1 (over all "places" v including ∞)
  is the ultimate reciprocity law.

This is the foundation of the Langlands program — connecting:
  Number theory (L-functions) ↔ Representation theory (automorphic forms)
  The deepest open problem in modern mathematics.
```

---

## Decision Cheat Sheet

| Task | Method |
|------|--------|
| Check if a is QR mod p (p prime) | Euler's criterion: a^{(p-1)/2} mod p |
| Compute (a/n) without factoring n | Jacobi symbol algorithm (O(log² n)) |
| Find √a mod p when p ≡ 3 (mod 4) | a^{(p+1)/4} mod p |
| Find √a mod p in general | Tonelli-Shanks algorithm |
| Determine if a is QR mod n (composite) | Need factorization (QR assumption hard without it) |
| Probabilistic primality test | Solovay-Strassen (Jacobi-based); Miller-Rabin better |
| Understand (-1/p) | (p ≡ 1 mod 4) iff (-1 is QR mod p) |
| Understand (2/p) | (p ≡ ±1 mod 8) iff (2 is QR mod p) |

---

## Common Confusion Points

**"(a/n) = 1 means a is a square mod n."**
Only when n is prime. For composite n, (a/n) = 1 is necessary but not
sufficient for a to be a QR. The Jacobi symbol can be 1 even for non-squares.
This is exactly the Goldwasser-Micali hard problem — distinguishing the cases.

**"Quadratic reciprocity is symmetric."**
It's almost symmetric but has a sign: (p/q) = (q/p) unless BOTH p,q ≡ 3 (mod 4).
Memorize: the sign flip happens exactly when the exponent (p-1)(q-1)/4 is odd,
i.e., when p ≡ q ≡ 3 (mod 4).

**"QR is just about squares — purely elementary."**
The Legendre symbol is a Dirichlet character mod p. The sum Σ (n/p) e^{2πin/p}
is a Gauss sum, and |Gauss sum|² = p. This connects to Fourier analysis on
finite groups, which connects to the proof of PNT in arithmetic progressions.

**"Tonelli-Shanks is obscure."**
It's implemented in Python as `pow(a, (p+1)//4, p)` for the easy case, and
Python's `sympy` implements the full algorithm. In practice, it's called
constantly in cryptographic code (EC point decompression).
