# Modular Arithmetic

## The Big Picture

```
+====================================================================+
|              MODULAR ARITHMETIC — THE RING Z/nZ                    |
+====================================================================+
|                                                                    |
|  Z/nZ = {0, 1, 2, ..., n-1} with + and × defined mod n           |
|                                                                    |
|  STRUCTURE DEPENDS ON n:                                          |
|                                                                    |
|  n = p (prime)           n = p^k              n composite         |
|  +-----------------+    +------------------+ +------------------+ |
|  |Z/pZ is a FIELD  |    |Z/p^kZ is a ring  | |Z/nZ is a ring    | |
|  |every nonzero    |    |not a field       | |may have zero     | |
|  |element has      |    |(p is a zero      | |divisors          | |
|  |multiplicative   |    |divisor mod p^k   | |e.g. 2·3≡0(mod 6) | |
|  |inverse          |    |but not a unit)   | |                  | |
|  +-----------------+    +------------------+ +------------------+ |
|          |                                           |            |
|          v                                           v            |
|  (Z/pZ)* is cyclic               CRT: Z/mnZ ≅ Z/mZ × Z/nZ       |
|  order p-1                       when gcd(m,n)=1                  |
+====================================================================+
```

**The key question for any n**: what is the multiplicative structure of
(Z/nZ)*? Answer: it's abelian, and its exact structure determines everything
from RSA correctness to discrete logarithm hardness.

---

## Congruences

```
a ≡ b (mod n)  ⟺  n | (a - b)  ⟺  a = b + kn for some k ∈ Z

Equivalence relation:
  Reflexive:   a ≡ a (mod n)
  Symmetric:   a ≡ b → b ≡ a
  Transitive:  a ≡ b, b ≡ c → a ≡ c

Congruences respect + and ×:
  If a ≡ b (mod n) and c ≡ d (mod n), then:
  a + c ≡ b + d (mod n)
  a · c ≡ b · d (mod n)

This is the ring homomorphism Z → Z/nZ.

Division is NOT always valid:
  6 ≡ 2 (mod 4)  but  3 ≡ 1 (mod 2)  (divide by 2, halve modulus)
  ac ≡ bc (mod n) does NOT imply a ≡ b (mod n) in general.
  It implies a ≡ b (mod n/gcd(c,n)).
```

---

## Linear Congruences

```
Solve: ax ≡ b (mod n)

Step 1: d = gcd(a, n)
Step 2: If d ∤ b → NO solution
Step 3: If d | b → exactly d solutions mod n
        Divide through by d: (a/d)x ≡ (b/d) (mod n/d)
        Solve using extended Euclidean (now gcd(a/d, n/d) = 1)
        Solutions: x₀, x₀ + n/d, x₀ + 2n/d, ..., x₀ + (d-1)n/d

Special case: a·x ≡ 1 (mod n) — the modular inverse
  Exists iff gcd(a,n) = 1
  Unique mod n
  Computed by Extended Euclidean
```

---

## Chinese Remainder Theorem (CRT)

```
THEOREM: If n = n₁·n₂·...·nₖ with nᵢ pairwise coprime, then:
  Z/nZ ≅ Z/n₁Z × Z/n₂Z × ... × Z/nₖZ
as rings.

CONSEQUENCE: The system
  x ≡ a₁ (mod n₁)
  x ≡ a₂ (mod n₂)
  ...
  x ≡ aₖ (mod nₖ)
has a UNIQUE solution mod n = n₁·n₂·...·nₖ.

CONSTRUCTION:
  N = n₁·n₂·...·nₖ
  Nᵢ = N/nᵢ
  Mᵢ = Nᵢ⁻¹ mod nᵢ  (compute via Extended Euclidean)
  x = Σ aᵢ·Nᵢ·Mᵢ  (mod N)
```

### CRT Example

```
x ≡ 2 (mod 3)
x ≡ 3 (mod 5)
x ≡ 2 (mod 7)

N = 105, N₁=35, N₂=21, N₃=15
M₁ = 35⁻¹ mod 3 = 2⁻¹ mod 3 = 2  (since 2·2=4≡1)
M₂ = 21⁻¹ mod 5 = 1⁻¹ mod 5 = 1  (since 21≡1 mod 5)
M₃ = 15⁻¹ mod 7 = 1⁻¹ mod 7 = 1  (since 15≡1 mod 7)

x = 2·35·2 + 3·21·1 + 2·15·1 = 140 + 63 + 30 = 233 ≡ 23 (mod 105)

Check: 23 mod 3 = 2 ✓, 23 mod 5 = 3 ✓, 23 mod 7 = 2 ✓
```

### CRT Applications

```
RSA speedup:
  Decryption: m = c^d mod n (n = pq)
  Without CRT: one big exponentiation mod n
  With CRT:
    m_p = c^{d mod (p-1)} mod p  ← small modulus
    m_q = c^{d mod (q-1)} mod q  ← small modulus
    Combine via CRT
  Speedup: ~4× (two quarter-size exponentiations vs one full-size)
  This is how all real RSA implementations work.

Integer arithmetic in multi-precision:
  Represent big integer as residues mod several small primes.
  Arithmetic is parallel, no carries.
  Recover result via CRT.
  Used in: NTT-based polynomial multiplication (cryptography).
```

---

## Euler's Phi Function

```
φ(n) = |{k : 1 ≤ k ≤ n, gcd(k,n) = 1}|

Multiplicative: φ(mn) = φ(m)φ(n) when gcd(m,n) = 1
Formula: φ(n) = n · ∏_{p|n} (1 - 1/p)

Examples:
  φ(1) = 1
  φ(p) = p-1  (for prime p)
  φ(p^k) = p^k - p^{k-1} = p^{k-1}(p-1)
  φ(12) = φ(4)·φ(3) = 2·2 = 4  → {1,5,7,11}
  φ(pq) = (p-1)(q-1)  for distinct primes p,q  ← RSA key formula

Sum formula: Σ_{d|n} φ(d) = n
  (Proof: partition {1,...,n} by gcd(k,n))
```

---

## Fermat's Little Theorem and Euler's Theorem

```
FERMAT'S LITTLE THEOREM (1640, proved Euler 1736):
  If p is prime and p ∤ a, then:
  a^{p-1} ≡ 1 (mod p)
  Equivalently: a^p ≡ a (mod p) for ALL a.

Proof: Consider {a, 2a, 3a, ..., (p-1)a} mod p.
  These are all distinct and nonzero (since p ∤ a and p prime).
  So they're a permutation of {1, 2, ..., p-1}.
  Product: a^{p-1}·(p-1)! ≡ (p-1)! (mod p)
  Cancel (p-1)!: a^{p-1} ≡ 1.  □

EULER'S THEOREM (generalization):
  If gcd(a,n) = 1, then:
  a^{φ(n)} ≡ 1 (mod n)

Proof: same argument with (Z/nZ)* (the invertible elements mod n).
  |((Z/nZ)*)| = φ(n). The set {a·k : k ∈ (Z/nZ)*} permutes (Z/nZ)*.
  Product argument gives a^{φ(n)} ≡ 1.  □

RSA CORRECTNESS:
  Choose e,d with ed ≡ 1 (mod φ(n)).  [n=pq, φ(n)=(p-1)(q-1)]
  Encryption: c = m^e mod n
  Decryption: c^d = m^{ed} = m^{1+kφ(n)} = m·(m^{φ(n)})^k ≡ m·1^k = m
  (using Euler's theorem, valid when gcd(m,n)=1 — almost always true)
```

### Wilson's Theorem

```
p is prime  ⟺  (p-1)! ≡ -1 (mod p)

Left to right: (p-1)! mod p. Elements with self-inverse:
  x² ≡ 1 (mod p) → x ≡ ±1. Only 1 and p-1.
  All other elements pair off with distinct inverses.
  Product = 1·...·(paired terms each = 1)·...(p-1) = (p-1) ≡ -1.

Right to left: If p composite, p = ab with 1 < a,b < p.
  Then a | (p-1)!, so (p-1)! ≡ 0 (mod a), not ≡ -1 (mod p).

Practical: Wilson's theorem is not useful for testing primality
  (computing (p-1)! requires exponential time in digits of p).
  But it's a clean characterization.
```

---

## Structure of (Z/nZ)*

```
STRUCTURE THEOREM:
  (Z/nZ)* ≅
    trivial                          if n = 1
    Z/2                              if n = 2
    Z/(p-1)                          if n = p (prime) — CYCLIC
    Z/(p^{k-1}(p-1))                 if n = p^k (odd prime)
    Z/2 × Z/2^{k-2}                  if n = 2^k, k ≥ 3
    product of above                  if n = p₁^{a₁}·...·pₖ^{aₖ}

CRITICAL FACT: (Z/pZ)* is cyclic of order p-1.
  A generator is called a PRIMITIVE ROOT mod p.
  Its powers hit every nonzero element mod p.
  This is the foundation of Diffie-Hellman.

Example: p = 7, (Z/7Z)* = {1,2,3,4,5,6}, order 6
  Is 3 a primitive root?
  3¹=3, 3²=2, 3³=6, 3⁴=4, 3⁵=5, 3⁶=1 → yes, hits all 6 nonzero elements.
  Is 2 a primitive root?
  2¹=2, 2²=4, 2³=1 → order 3, hits only {1,2,4}. NOT a primitive root.
```

---

## Fast Modular Exponentiation

```
Compute a^e mod n efficiently.

NAIVE: e multiplications — O(e) — exponential in bit length of e.
SQUARE-AND-MULTIPLY: O(log e) multiplications — polynomial.

Algorithm:
  result = 1
  base = a mod n
  while e > 0:
    if e is odd: result = result * base mod n
    e = e >> 1   (integer divide by 2)
    base = base * base mod n
  return result

Example: 3^13 mod 7
  13 = 1101₂
  3^1 mod 7 = 3
  3^2 mod 7 = 2
  3^4 mod 7 = 4
  3^8 mod 7 = 2
  3^13 = 3^8 · 3^4 · 3^1 = 2·4·3 = 24 ≡ 3 (mod 7)

This is O(log e) multiplications mod n. Each multiplication is O((log n)²).
Total: O((log e)(log n)²) — fast enough for RSA key sizes (e.g., e=65537, n=2048-bit).
```

---

## Carmichael Function

```
λ(n) = lcm of orders of all elements of (Z/nZ)*
     = lcm(λ(p₁^{a₁}), ..., λ(pₖ^{aₖ}))

λ(p^k) = p^{k-1}(p-1) for odd prime p
λ(2) = 1, λ(4) = 2, λ(2^k) = 2^{k-2} for k ≥ 3

Property: a^{λ(n)} ≡ 1 (mod n) for all gcd(a,n)=1
  λ(n) | φ(n)  but λ(n) may be much smaller than φ(n)

RSA improvement: use λ(n) = lcm(p-1, q-1) instead of φ(n) = (p-1)(q-1)
  Results in smaller d (private exponent)
  ed ≡ 1 (mod λ(n)) is sufficient for correctness
  This is "RSA with CRT exponents"
```

---

## Quadratic Residues Preview

```
a is a quadratic residue mod p if x² ≡ a (mod p) has a solution.

Euler's criterion: a^{(p-1)/2} ≡ 1 (mod p) iff a is a QR mod p
                   a^{(p-1)/2} ≡ -1 (mod p) iff a is a non-residue

This connects to the Legendre symbol (p-1)/2 power test and to
quadratic reciprocity — see 04-QUADRATIC-RECIPROCITY.md.
```

---

## Decision Cheat Sheet

| Need to... | Method |
|-----------|--------|
| Solve ax ≡ b (mod n) | Extended Euclidean, check d=gcd(a,n)|b |
| Find a⁻¹ mod n | Extended Euclidean |
| Solve system of congruences | CRT (pairwise coprime moduli) |
| Compute a^e mod n | Square-and-multiply |
| Understand RSA exponent formula | Euler φ(n) or Carmichael λ(n) |
| Know if a^n ≡ a (mod n) for all a | n is 1, prime, or Carmichael number |
| Understand (Z/pZ)* structure | Cyclic of order p-1, primitive roots exist |
| Speed up RSA decryption 4× | Apply CRT decomposition |
| Reduce RSA d (private exponent) | Use λ(n) = lcm(p-1,q-1) not φ(n) |

---

## Common Confusion Points

**"φ(n) is the correct exponent for Euler's theorem."**
True, but λ(n) is the *minimal* exponent that works for ALL elements.
For RSA, ed ≡ 1 (mod λ(n)) is sufficient and gives smaller d.
Some RSA implementations use φ(n) (larger d, more computation) — functionally
equivalent but slightly less efficient.

**"CRT requires moduli to be prime."**
No — CRT requires moduli to be *pairwise coprime*. They don't need to be prime.
Example: Z/12Z ≅ Z/4Z × Z/3Z (since gcd(4,3)=1). But NOT Z/8Z × Z/3Z ≅ Z/24Z
... wait, that IS valid: gcd(8,3)=1, 8×3=24.

**"a ≡ b (mod n) and a ≡ b (mod m) implies a ≡ b (mod nm)."**
Only if gcd(n,m)=1. In general: a ≡ b (mod lcm(n,m)).
CRT requires coprimality for the ring isomorphism to hold.

**"Fermat's Little Theorem tests primality."**
It rules out primality: if a^{n-1} ≢ 1 (mod n), then n is composite.
But if a^{n-1} ≡ 1 (mod n), n MIGHT be prime. Carmichael numbers
(like 561 = 3·11·17) satisfy a^{n-1} ≡ 1 for all gcd(a,n)=1, yet are
composite. Miller-Rabin fixes this by also checking square roots of 1.

**"(Z/nZ)* is always cyclic."**
Only when n = 1, 2, 4, p^k, or 2p^k for odd prime p.
For n = 8: (Z/8Z)* = {1,3,5,7} ≅ Z/2 × Z/2 (not cyclic, no element of order 4).
This is why DH over Z/2^k is bad — the group is not cyclic, making the
discrete log easier.
