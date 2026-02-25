# Computational Number Theory

## The Big Picture

```
+====================================================================+
|       COMPUTATIONAL NUMBER THEORY — COMPLEXITY LANDSCAPE           |
+====================================================================+
|                                                                    |
|  EASY (polynomial time):                                          |
|  +------------------+  +------------------+  +------------------+ |
|  | GCD / inverse    |  | Modular exp.     |  | PRIMES (AKS)     | |
|  | O(log² n)        |  | O(log³ n)        |  | O(log^6 n)       | |
|  +------------------+  +------------------+  +------------------+ |
|                                                                    |
|  EFFICIENT PROBABILISTIC (expected poly time):                    |
|  +------------------+  +------------------+                       |
|  | Miller-Rabin     |  | Jacobi symbol    |                       |
|  | O(k log³ n)      |  | O(log² n)        |                       |
|  +------------------+  +------------------+                       |
|                                                                    |
|  SUB-EXPONENTIAL (known best, not poly):                          |
|  +------------------+  +------------------+                       |
|  | Integer factoring|  | Discrete log     |                       |
|  | NFS: L[1/3,1.923]|  | Index calculus   |                       |
|  +------------------+  +------------------+                       |
|                                                                    |
|  QUANTUM POLYNOMIAL:                                              |
|  +-----------------------------------------------+               |
|  | Shor's algorithm: factoring AND discrete log  |               |
|  | O((log n)³) on a quantum computer             |               |
|  +-----------------------------------------------+               |
+====================================================================+
```

---

## Primality Testing

### Fermat Pseudoprimes — Why Fermat Fails

```
FERMAT TEST: If n is prime and gcd(a,n)=1, then a^{n-1} ≡ 1 (mod n).
  Contrapositive: if a^{n-1} ≢ 1 (mod n), then n is composite.

PROBLEM: Carmichael numbers.
  n is a Carmichael number if a^{n-1} ≡ 1 (mod n) for ALL gcd(a,n)=1.
  Smallest: 561 = 3·11·17.
  Korselt's criterion: n is Carmichael iff n is squarefree and (p-1)|(n-1) for all p|n.
  There are infinitely many Carmichael numbers (Alford-Granville-Pomerance, 1994).

Fermat test gives no guarantee against Carmichael numbers.
```

### Miller-Rabin Primality Test

```
FOUNDATION: Strong pseudoprime test.

Write n-1 = 2^s · d, d odd.

Miller-Rabin test with base a:
  Compute a^d mod n.
  If a^d ≡ 1 (mod n): PASS (probably prime for this base)
  Otherwise: compute a^{2d}, a^{4d}, ..., a^{2^{s-1}d} mod n.
    If any ≡ -1 (mod n): PASS (probably prime)
    If none ≡ -1: COMPOSITE (with certainty)

If n is PRIME: Miller-Rabin always passes all bases.
If n is COMPOSITE: at least 3/4 of bases ∈ {2,...,n-2} cause a FAIL.

ALGORITHM:
  Repeat k times with random bases:
    If any base fails: return COMPOSITE
  Return PROBABLY PRIME (error prob ≤ (1/4)^k)

FOR DETERMINISTIC RESULT:
  If n < 3.3×10^{24}: test bases {2,3,5,7,11,13,17,19,23,29,31,37} — sufficient.
  Under GRH: test a ≤ 2(ln n)² — deterministic.

Complexity: O(k · log³ n) per test (k = number of bases).
  For k=20: error probability < 4^{-20} ≈ 10^{-12}. Used in practice.

WHY IT WORKS:
  If n is prime, then x²≡1(mod n) implies x≡±1.
  (Since Z/nZ is a field when n is prime — quadratic has at most 2 roots.)
  If n is composite: x²≡1 may have solutions ±1 AND others.
  Miller-Rabin hunts for these "non-trivial square roots of 1."
```

### AKS Primality Test (Agrawal-Kayal-Saxena, 2002)

```
THEOREM: PRIMES is in P.
  There is a deterministic polynomial-time algorithm for primality testing.

Key idea: if p is prime, then for any a with gcd(a,p)=1:
  (x + a)^p ≡ x^p + a (mod p)  [in (Z/pZ)[x]/(x^r - 1)]

AKS checks this for several values of r and a.

ALGORITHM (simplified):
  1. If n = a^b for a,b > 1: COMPOSITE.
  2. Find smallest r such that ord_r(n) > (log n)².
  3. If gcd(a,n) > 1 for some a ≤ r: COMPOSITE.
  4. If n ≤ r: PRIME.
  5. For a = 1 to ⌊√φ(r) log n⌋:
       If (x+a)^n ≢ x^n + a (mod x^r - 1, n): COMPOSITE.
  6. PRIME.

Complexity: O(log^{6+ε} n) — polynomial.

PRACTICAL STATUS:
  AKS is SLOW in practice compared to Miller-Rabin.
  For 1000-bit n: Miller-Rabin (30 rounds) takes microseconds; AKS takes minutes.
  Used for: theoretical completeness (PRIMES ∈ P is a landmark result).
  Not used in: real cryptographic implementations (Miller-Rabin is standard).

The practical tools:
  OpenSSL, GPG: Miller-Rabin with sufficient rounds.
  GMP (GNU Multi-Precision): Deterministic for small n, probabilistic for large.
```

---

## Integer Factoring

### Trial Division

```
Algorithm: test divisors 2, 3, 5, 7, ..., up to √n.
Complexity: O(√n) = O(2^{(log n)/2}) — exponential in digits.
  For 100-bit n: √n ≈ 2^{50} ≈ 10^{15} — infeasible.
  For 20-bit n: √n ≈ 1000 — fine.

Practical use: always start with trial division for small factors (< 10^6).
  An 1024-bit RSA modulus will have no small factors by construction.
```

### Pollard Rho Algorithm

```
Idea: find cycle in a pseudo-random sequence mod n.

Floyd's cycle detection:
  x₀ = 2
  x_{i+1} = x_i² + 1 (mod n)  [or any polynomial f(x)]
  y = x (tortoise-hare: y advances 2 steps per x step)

  Compute gcd(|x-y|, n) at each step.
  A non-trivial gcd gives a factor.

WHY IT WORKS (birthday paradox):
  In Z/pZ (p is a prime factor of n), the sequence x_i mod p is pseudo-random
  of period roughly √p (birthday paradox in a set of size p).
  A collision mod p: xᵢ ≡ xⱼ (mod p) but not mod n → gcd finds p.

Complexity: O(n^{1/4}) = O(p^{1/2}) where p is smallest prime factor.
  For n = pq (balanced): complexity O(n^{1/4}).
  For n = 2^{1024}: smallest factor could be huge → might need full NFS.

Practical:
  Factors up to ~20-30 digits efficiently.
  Used as a preprocessing step before NFS.
```

### Pollard p-1 Algorithm

```
For primes p where p-1 has only small prime factors (p-1 is "smooth"):

Choose B (smoothness bound), compute M = lcm(1,...,B) or M = ∏_{p^k ≤ B} p^k.
Compute a^M mod n for random a.
gcd(a^M - 1, n) may reveal factor p if p-1 | M.

Works because: if p-1 | M, then by Fermat's little theorem, a^M ≡ 1 (mod p),
so p | gcd(a^M - 1, n).

Complexity: O(B · log B · log² n) with B chosen to catch smooth p-1.
Implication: RSA primes must NOT be chosen such that p-1 is smooth.
  Safe primes p = 2q+1 (q prime) resist this attack (p-1 = 2q, only factor q is huge).
```

### Quadratic Sieve (QS)

```
Idea: find x, y with x² ≡ y² (mod n), x ≢ ±y (mod n) → gcd(x-y, n) is a factor.

FACTOR BASE: small primes {p₁, ..., pₜ}.

1. Sieve: find many "B-smooth" numbers: x²-n that factor over the factor base.
   For each x near √n: compute x²-n. If it factors over {p₁,...,pₜ}, record it.
2. Linear algebra: find subset of smooth relations whose product is a perfect square.
   (Via linear algebra over GF(2) — find kernel of exponent matrix mod 2.)
3. Combine: if Π(xᵢ²-n) = y² and Π xᵢ² = z², then (z-y)(z+y) ≡ 0 (mod n).

Complexity: L_n[1/2, 1] = exp(c·√(ln n · ln ln n)).
  For 512-bit n: feasible.
  For 768-bit n: hard.
  For 1024-bit n: infeasible with QS.
```

### Number Field Sieve (NFS)

```
The best known algorithm for factoring large integers.

KEY INSIGHT: Work in Z and a ring Z[α] (where α is a root of a polynomial),
  looking for "smooth" elements in BOTH rings simultaneously.

Setup:
  Choose polynomial f(x) of degree d, compute m = n^{1/d} approximately.
  Let α = root of f. Map: Z → Z[α] by x ↦ x-mα.
  Norm in Z[α]: N(x-mα) = f(m) ... (roughly)

Algorithm:
  Sieve for pairs (a,b) such that both a-bm (in Z) and a-bα (in Z[α]) are smooth.
  Matrix step: eliminate to find a square on both sides.
  Square root step: compute square roots in Z and Z[α].
  Factor: gcd extracts the factor.

Complexity: L_n[1/3, (64/9)^{1/3}] ≈ L_n[1/3, 1.923]

  L_n[α, c] = exp((c+o(1)) (ln n)^α (ln ln n)^{1-α})
  α=0: polynomial time    α=1: exponential    α=1/3: NFS complexity

For α=1/3 (NFS): grows faster than poly, slower than exponential.
Crossover from QS to NFS: around 100 decimal digits.

PRACTICAL RECORDS:
  RSA-768 (768-bit, 232 digits): factored 2009 by NFS.
  RSA-829 (250 digits): factored 2020.
  RSA-2048: estimated >10^{15} years with NFS on classical hardware.
  RSA-2048: hours with Shor's algorithm on a large quantum computer (>4000 logical qubits).
```

---

## Sieving Algorithms

### Sieve of Eratosthenes (Primes up to N)

```
Algorithm:
  Bit array: sieve[2..N], initially all True.
  For p = 2, 3, 5, ..., ⌊√N⌋:
    If sieve[p] = True:
      For k = p², p²+p, p²+2p, ..., N:  sieve[k] = False
  Return {p : sieve[p] = True}

Time: O(N log log N).   Space: O(N).
For N = 10^9: ~1 billion operations — feasible in seconds.
For N = 10^{12}: 1TB of memory needed — use segmented sieve.

SEGMENTED SIEVE: Sieve in blocks of size √N.
  Memory: O(√N).  Time: O(N log log N).
  Practical for N up to ~10^{12}.
```

### Wheel Factorization

```
Optimization: skip multiples of 2, 3, 5, 7 from the start.
  Only test residues coprime to 2·3·5·7 = 210.
  φ(210) = 48 out of 210 candidates — 77% reduction.

For sieving: start sieve at 11, step by residues {1,11,13,17,...} mod 210.
  This is the "wheel" and it reduces constant factors significantly.
```

### Smooth Number Counting

```
ψ(x, y) = |{n ≤ x : n is y-smooth (all prime factors ≤ y)}|

DICKMAN'S FUNCTION ρ(u):
  ψ(x, y) ~ x · ρ(u)  where u = ln(x)/ln(y)

  ρ(1) = 1
  ρ(u) = 0 for u < 0... wait, ρ is defined for u > 0:
  For u ∈ (0,1]: ρ(u) = 1
  For u > 1: u·ρ'(u) = -ρ(u-1)

  ρ(2) ≈ 0.307, ρ(3) ≈ 0.048, ρ(4) ≈ 0.00491, ...

RELEVANCE TO FACTORING:
  Sieving algorithms need smooth numbers.
  The probability that a random number near x is B-smooth = ρ(ln x / ln B).
  Choose B to maximize smooth number density vs. factor base size.
```

---

## Elliptic Curve Method (ECM)

```
Lenstra's algorithm (1985): exploits elliptic curves to factor n.

IDEA: Generalize Pollard p-1 from multiplicative group (Z/pZ)* to
  elliptic curve group E(Z/pZ).

Algorithm:
  Choose random elliptic curve E over Z/nZ and point P ∈ E.
  Compute k·P (k = product of prime powers up to B₁).
  If at any step a gcd with n is nontrivial: factor found.

Why better than p-1:
  For each prime p|n, we're working in E(Z/pZ), which has order in (p-√p, p+√p).
  Since we don't know p, we try many curves — each gives a different group order.
  If any group order is B₁-smooth, we find the factor.

Complexity: L_p[1/2, √2] where p is smallest prime factor.
  Much better than QS/NFS for finding SMALL prime factors.

Practical: ECM finds factors up to ~60 digits efficiently.
  Used as preprocessing before NFS for large composites.
  Record: factor of 83 digits found by ECM (2013).
```

---

## Greatest Common Divisor and Modular Arithmetic — Algorithms

```
EUCLIDEAN ALGORITHM:
  gcd(a, b):  O(log min(a,b)) divisions.
  Binary GCD: avoids division, uses shifts. Better for hardware.

EXTENDED EUCLIDEAN:
  Returns (g, s, t) with sa + tb = g.
  O(log² n) bit operations (each step: one division + bookkeeping).

MODULAR EXPONENTIATION:
  pow(a, e, n): square-and-multiply. O(log e) multiplications mod n.
  Each multiplication: O((log n)²) bit operations.
  Total: O(log e · (log n)²).

MONTGOMERY MULTIPLICATION:
  Avoids division in modular multiplication using a "Montgomery form."
  Key in embedded systems and hardware RSA implementations.
  Precompute R = 2^k (k = bit length of n).
  Mont(A, B) = A·B·R^{-1} mod n — computable without division.

BARRETT REDUCTION:
  Alternative to Montgomery for software implementations.
  Precompute floor(R/n) once; fast repeated mod operations.
```

---

## Decision Cheat Sheet

| Task | Best Algorithm | Complexity |
|------|---------------|------------|
| Compute gcd(a,b) | Euclidean | O(log min(a,b)) |
| Modular inverse a⁻¹ mod n | Extended Euclidean | O(log² n) |
| Modular exponentiation aᵉ mod n | Square-and-multiply | O(log e · log² n) |
| Test primality (probabilistic) | Miller-Rabin | O(k log³ n) |
| Test primality (deterministic) | AKS | O(log^6 n) |
| Factor n, small factors | Pollard rho | O(n^{1/4}) |
| Factor n, p-1 smooth | Pollard p-1 | O(B log B log² n) |
| Factor n, ECM (mid-size factors) | Lenstra ECM | L_p[1/2, √2] |
| Factor n (large, general) | Number Field Sieve | L_n[1/3, 1.923] |
| Find all primes ≤ N | Sieve of Eratosthenes | O(N log log N) |

---

## Common Confusion Points

**"AKS made Miller-Rabin obsolete."**
For theoretical purposes, AKS matters: it proved PRIMES ∈ P. For practical
primality testing, Miller-Rabin is used in every cryptographic library. AKS
is far slower in practice (e.g., a 1024-bit number takes seconds with Miller-Rabin,
much longer with AKS). The field is "use Miller-Rabin; generate strong primes."

**"NFS can factor RSA-2048 eventually."**
The complexity L_n[1/3, 1.923] for n=RSA-2048 gives a number astronomically
larger than the age of the universe in computation steps. NFS factored RSA-768
in 2009 after years of computation. RSA-1024 is feasible for nation-states
with massive compute. RSA-2048 is believed safe for the foreseeable future
against classical computers.

**"Shor's algorithm runs on current quantum computers."**
Current quantum computers have only O(100) physical qubits with high error rates.
Shor's algorithm needs thousands of LOGICAL qubits (with error correction).
A 2048-bit RSA factorization needs ~4000 logical qubits or ~1 million physical qubits.
Not available now; timeline is 10-20+ years if quantum computing advances.

**"Pollard rho runs in O(√n) time."**
It runs in O(n^{1/4}) time for balanced semiprimes n = pq, because it factors
at the O(√p) ≈ O(n^{1/4}) scale. The O(√p) is on p, the smallest prime factor.
For n with a tiny prime factor p, it runs in O(p^{1/2}) — very fast.
