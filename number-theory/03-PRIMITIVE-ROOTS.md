# Primitive Roots and the Discrete Logarithm

## The Big Picture

```
+====================================================================+
|          MULTIPLICATIVE STRUCTURE OF Z/pZ                          |
+====================================================================+
|                                                                    |
|  (Z/pZ)* = {1, 2, ..., p-1}  under multiplication mod p          |
|                                                                    |
|  This is a CYCLIC GROUP of order p-1                              |
|                                                                    |
|       g (primitive root) generates everything:                     |
|  g¹, g², g³, ..., g^{p-1} = 1  hits all of (Z/pZ)*              |
|                                                                    |
|  DISCRETE LOGARITHM (DLP):                                        |
|  Given g, a, p — find x such that gˣ ≡ a (mod p)                  |
|                                                                    |
|  ┌─────────────────┐         ┌──────────────────────────┐         |
|  │  EASY direction │         │  HARD direction (DLP)    │         |
|  │  gˣ mod p       │         │  log_g(a) mod p          │         |
|  │  O(log x) steps │         │  best: sub-exp time      │         |
|  │  (square+mult.) │         │  (index calculus)        │         |
|  └─────────────────┘         └──────────────────────────┘         |
+====================================================================+
```

The asymmetry between exponentiation (easy) and discrete log (hard) is
the mathematical foundation of Diffie-Hellman key exchange and ElGamal
encryption. The structure of the group determines both the correctness
of these protocols and their security.

---

## Order of an Element

```
DEFINITION: The order of a in (Z/nZ)* is the smallest positive integer k such that:
  a^k ≡ 1 (mod n)
  Written: ord_n(a) = k

Properties:
  a^m ≡ 1 (mod n)  ⟺  ord_n(a) | m
  In particular: ord_n(a) | φ(n)  [Lagrange's theorem applied to the group]
  ord_n(a) | λ(n)  [Carmichael function = exponent of the group]

Example: Compute orders in (Z/7Z)* = {1,2,3,4,5,6}
  ord(1) = 1   (1^1 = 1)
  ord(2) = 3   (2^1=2, 2^2=4, 2^3=8≡1)
  ord(3) = 6   (3^1=3, 3^2=2, 3^3=6, 3^4=4, 3^5=5, 3^6=1)
  ord(4) = 3   (4^1=4, 4^2=2, 4^3=1)
  ord(5) = 6   (5^1=5, 5^2=4, 5^3=6, 5^4=2, 5^5=3, 5^6=1)
  ord(6) = 2   (6^1=6, 6^2=36≡1)

Orders divide φ(7) = 6 = {1,2,3,6} ✓
Elements of order 6 (= p-1): {3, 5} — these are the primitive roots.
```

---

## Primitive Roots

```
DEFINITION: g is a primitive root mod p if ord_p(g) = p-1.
  Equivalently: the powers g⁰, g¹, ..., g^{p-2} are a permutation of {1,...,p-1}.
  Equivalently: g generates (Z/pZ)* as a cyclic group.

EXISTENCE THEOREM: Primitive roots exist mod p for any prime p.
  More precisely:
  - Primitive roots exist mod pᵏ for any prime p and k ≥ 1
    (with a minor adjustment for p=2, k ≥ 3)
  - Primitive roots exist mod 2pᵏ for odd prime p
  - NO primitive roots mod n when n = 2^k (k≥3), n = p^a·q^b, etc.
    (group is not cyclic in those cases)

NUMBER OF PRIMITIVE ROOTS: φ(p-1) primitive roots exist mod p.
  (Number of generators of a cyclic group of order m is φ(m))
  Example: p=7, φ(6) = φ(2)φ(3) = 1·2 = 2. Two primitive roots: {3,5} ✓
  Example: p=11, φ(10) = φ(2)φ(5) = 1·4 = 4. Four primitive roots: {2,6,7,8}.
```

### How to Find a Primitive Root

```
Algorithm (for prime p):
  1. Compute φ(p) = p-1
  2. Factor p-1 = q₁^{a₁} · q₂^{a₂} · ... · qₖ^{aₖ}
  3. For candidate g = 2, 3, 5, ...:
     For each prime factor qᵢ of p-1:
       Compute g^{(p-1)/qᵢ} mod p
       If any equals 1: g is NOT a primitive root, try next g
     If none equal 1: g IS a primitive root

Why this works: g has order p-1 iff g^{(p-1)/q} ≢ 1 (mod p) for all prime q|p-1.
  (If ord(g) < p-1, then ord(g) divides (p-1)/q for some prime q|p-1.)

Expected number of candidates to test: O(log log p) (primitive roots are dense).
```

---

## Discrete Logarithm Problem

```
Given: prime p, primitive root g, element a ∈ (Z/pZ)*
Find: x ∈ {0, 1, ..., p-2} such that gˣ ≡ a (mod p)

Notation: x = log_g(a) (mod p)  or  x = ind_g(a)  (index)

INDEX ARITHMETIC (analog of logarithm rules):
  log_g(ab) ≡ log_g(a) + log_g(b) (mod p-1)
  log_g(a^k) ≡ k·log_g(a) (mod p-1)
  log_g(1) = 0
  log_g(g) = 1

Example (p=7, g=3):
  3⁰=1, 3¹=3, 3²=2, 3³=6, 3⁴=4, 3⁵=5
  Index table: ind_3(1)=0, ind_3(3)=1, ind_3(2)=2, ind_3(6)=3, ind_3(4)=4, ind_3(5)=5

  Compute 5·6 mod 7 via indices:
  ind(5·6) = ind(5) + ind(6) = 5 + 3 = 8 ≡ 2 (mod 6)
  5·6 ≡ 3² = 2 (mod 7). Check: 30 mod 7 = 2 ✓
```

---

## DLP Algorithms

### Baby-Step Giant-Step (BSGS)

```
Goal: find x with gˣ ≡ a (mod p). Let m = ⌈√(p-1)⌉.
Write x = im - j where 0 ≤ i,j < m.
Then gˣ = g^{im-j} = (g^m)^i · g^{-j} ≡ a
         → (g^m)^i ≡ a · gʲ

Algorithm:
  Baby steps: Compute a·gʲ for j = 0,...,m-1. Store in hash table.
  Giant steps: Compute (g^m)^i for i = 0,...,m-1. Look up in table.
  Match: output x = im - j.

Complexity: Time O(√p), Space O(√p).
  For p ≈ 2^{128}: √p ≈ 2^{64} — completely infeasible.
  This is why DH parameters need p of 2048+ bits.
  This is why ECC at 256 bits gives equivalent security to RSA at 3072 bits
  (ECDLP requires O(√p) with p≈2^{256}, DLP in Z/pZ requires sub-exp).
```

### Pohlig-Hellman Algorithm

```
If p-1 has small prime factors, DLP is EASY.

Algorithm: Reduce DLP mod p to DLP in smaller groups.
  Factor p-1 = q₁^{a₁} · ... · qₖ^{aₖ}
  For each prime power qᵢ^{aᵢ}:
    Find xᵢ = x mod qᵢ^{aᵢ} using a DLP in a group of order qᵢ
  Combine via CRT to get x mod (p-1).

Complexity: O(Σ aᵢ(√qᵢ + log p)) — fast when qᵢ are all small.

LESSON FOR CRYPTOGRAPHY:
  Choose p such that p-1 has a LARGE prime factor q.
  Typically: p = 2q + 1 where q is prime ("safe prime").
  Then (Z/pZ)* has a cyclic subgroup of order q, and Pohlig-Hellman
  gives no speedup (q is already as large as possible).
  DH parameters require p is safe prime or q (the subgroup order) is large.
```

### Index Calculus

```
Best algorithm for DLP in (Z/pZ)*. Sub-exponential time.

Idea: Exploit that small primes appear frequently in random exponents.
  Factor base: F = {p₁, p₂, ..., pₜ} (small primes)

Phase 1 (relation gathering):
  For random k:
    Compute gᵏ mod p
    If gᵏ mod p factors completely over F (it's "smooth"):
      Record relation: k ≡ Σ eᵢ log_g(pᵢ) (mod p-1)
  Accumulate enough relations to solve the linear system.

Phase 2 (individual log):
  For the target a, find k such that a·gᵏ is smooth.
  Use Phase 1 results to compute log_g(a).

Complexity: L_p[1/2, c] = exp(c · √(ln p · ln ln p))
  Sub-exponential but super-polynomial.
  This is why we need 2048-bit p for DH (not 256-bit like ECC).
```

---

## Comparison: DLP vs ECDLP

```
+-------------------------------------------------------------------+
| PROBLEM    | GROUP           | Best attack   | Security bits      |
+-------------------------------------------------------------------+
| DLP        | (Z/pZ)*         | Index calculus| 128-bit: p≈3072b  |
|            |                 | sub-exp time  | 256-bit: p≈15360b |
+-------------------------------------------------------------------+
| ECDLP      | E(F_p) (ellip-  | BSGS/Pollard  | 128-bit: p≈256b    |
|            | tic curve group)| rho: O(√p)    | 256-bit: p≈512b    |
+-------------------------------------------------------------------+

Key insight: No sub-exponential algorithm is known for ECDLP in general.
  For generic groups, BSGS is optimal (Shoup's lower bound).
  ECC gives much smaller key sizes for equivalent security.
  RSA-2048 ≈ ECC-224 in security level.

Both broken by Shor's algorithm on a quantum computer.
Post-quantum alternative: SVP/CVP in lattices (not broken by Shor).
```

---

## Primitive Roots in Other Contexts

### Primitive Roots mod p^k (odd prime p)

```
If g is a primitive root mod p, then either:
  - g is a primitive root mod pᵏ for all k ≥ 1, OR
  - g + p is a primitive root mod pᵏ for all k ≥ 1.

So primitive roots exist mod pᵏ, just with order φ(pᵏ) = p^{k-1}(p-1).
```

### Primitive Roots in F_{p^n} (Finite Fields)

```
The multiplicative group F_{p^n}* = (GF(p^n))* is cyclic of order p^n - 1.
Primitive roots (called primitive elements) generate all nonzero elements.
Used in: Reed-Solomon codes, AES's GF(2^8) arithmetic, elliptic curves.

GF(2^8) in AES:
  Polynomial ring: GF(2)[x]/(x^8 + x^4 + x^3 + x + 1)
  256 elements, (GF(2^8))* is cyclic of order 255
  Generator: 0x03 (the polynomial x+1)
```

---

## Generalized Discrete Logarithm

```
In any cyclic group G = ⟨g⟩ of order n:
  DLP: given g, a ∈ G, find x with gˣ = a.

Same algorithms apply (BSGS, Pohlig-Hellman, Pollard rho).
The "hardness" depends on the group:

  (Z/pZ)* — sub-exponential attacks exist (index calculus)
  E(F_p)  — only generic attacks known (O(√p))
  Class group of Q(√-d) — intermediate difficulty
  Symmetric group — easy (structure too rigid)
  SL(2, F_p) — used in some post-quantum proposals

The choice of group is the key cryptographic design decision.
```

---

## Decision Cheat Sheet

| Task | Method |
|------|--------|
| Check if g is primitive root mod p | Verify g^{(p-1)/q} ≢ 1 for all prime q|p-1 |
| Find primitive root mod p | Test candidates; expected O(log log p) trials |
| Compute discrete log (small p) | Baby-step giant-step: O(√p) |
| Compute discrete log (p-1 smooth) | Pohlig-Hellman: fast |
| Compute discrete log (general large p) | Index calculus: sub-exp |
| Choose DH parameters | p safe prime (p=2q+1) or q large prime subgroup order |
| Understand ECDLP hardness | No sub-exp attack known; O(√p) generic lower bound |
| Understand why 256-bit ECC ≈ 3072-bit DH | ECC: generic O(√p); DH: sub-exp index calculus |

---

## Common Confusion Points

**"Primitive root mod p is unique."**
There are φ(p-1) primitive roots mod p, not one. For p=7 there are 2,
for p=11 there are 4. Any primitive root can be used for DH.

**"Primitive roots exist for all n."**
They exist for n = 1, 2, 4, pᵏ, 2pᵏ (p odd prime). They do NOT exist for
n = p·q (distinct odd primes) or n = 2ᵏ (k≥3). If you try to do DH mod
a composite n without a primitive root, the group is not cyclic and the
protocol may leak information or not work correctly.

**"DLP is hard for the same reason factoring is hard."**
They're different problems with different algorithms. Index calculus works
on DLP in (Z/pZ)* but not on factoring. The NFS for factoring is related
but distinct. Empirically they seem to require similar key sizes for
similar security, but this is a coincidence of practical parameters,
not a theoretical equivalence.

**"Pohlig-Hellman shows DLP is easy."**
It shows DLP is easy *when the group order is smooth*. Safe primes (p=2q+1)
are specifically designed to prevent this — the subgroup of order q is hard.

**"Shor's algorithm solves DLP but not factoring."**
Shor's algorithm solves BOTH DLP and factoring in polynomial quantum time.
DLP: find the period of gˣ mod p (same period-finding framework as factoring).
This is why both RSA (factoring) and DH/ECC (DLP) are post-quantum broken.
