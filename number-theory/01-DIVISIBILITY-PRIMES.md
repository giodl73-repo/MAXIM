# Divisibility and Primes

## The Big Picture

```
+================================================================+
|              DIVISIBILITY — THE LATTICE OF DIVISORS            |
+================================================================+
|                                                                |
|  DIVISION ALGORITHM:  a = qb + r,  0 ≤ r < b                  |
|         |                                                      |
|         v                                                      |
|  GCD via EUCLIDEAN ALGORITHM                                   |
|  gcd(a,b) = gcd(b, a mod b) = ... = gcd(d, 0) = d            |
|         |                                                      |
|         v                                                      |
|  BEZOUT'S IDENTITY:  ∃s,t ∈ Z: sa + tb = gcd(a,b)            |
|  (Extended Euclidean — constructive)                           |
|         |                                                      |
|         v                                                      |
|  UNIQUE FACTORIZATION THEOREM (UFT):                          |
|  n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ  uniquely                   |
|         |                                                      |
|         v                                                      |
|  PRIME DISTRIBUTION:                                          |
|  π(x) ~ x/ln x  (Prime Number Theorem)                       |
|  Primes thin out but never stop                               |
+================================================================+
```

The structure: divisibility defines a **partial order** on N.
Primes are the atoms — the irreducible elements of this order.
UFT says the partial order has a unique decomposition in terms of atoms.

---

## The Division Algorithm

For any integers a, b with b > 0:
```
∃! q, r ∈ Z:  a = qb + r,  0 ≤ r < |b|

q = quotient = ⌊a/b⌋
r = remainder = a mod b
```

This is not just a computational tool — it is the axiom that makes Z a
Euclidean domain, which guarantees gcd exists and Bezout holds.

**Euclid's Algorithm:**
```
gcd(a, b):
  while b ≠ 0:
    a, b = b, a mod b
  return a

Example: gcd(1071, 462)
  1071 = 2·462 + 147   → gcd(462, 147)
   462 = 3·147 + 21    → gcd(147, 21)
   147 = 7·21 + 0      → return 21

gcd(1071, 462) = 21
```

**Complexity**: O(log min(a,b)) divisions — the Fibonacci numbers give
worst-case inputs (consecutive Fibonacci numbers require the most steps).

**Extended Euclidean** — tracks Bezout coefficients:
```
gcd(a,b) = sa + tb  for some s,t ∈ Z

Algorithm maintains two rows (s₀,t₀,r₀) and (s₁,t₁,r₁):
  Start: (1,0,a) and (0,1,b)
  Step: q = r₀ div r₁; new row = old_row₀ - q·old_row₁

Application: Find modular inverse of a mod n.
  a·x ≡ 1 (mod n) ⟺ ax + ny = 1 ⟺ gcd(a,n) = 1
  Extended Euclidean gives x directly.
```

---

## GCD, LCM, and Bezout

### Key Properties

```
gcd(a,b) = gcd(b,a)
gcd(a,0) = a
gcd(ka, kb) = k·gcd(a,b)
gcd(a,b)·lcm(a,b) = |a·b|

Bezout: gcd(a,b) = d  ⟹  ∃s,t: sa + tb = d
         d is the SMALLEST POSITIVE integer representable as sa + tb
```

### The Divisibility Lattice

For n = 12:
```
        12
       /  \
      4    6
     / \  / \
    2    3    (meets)
     \  /
      1

Divisors of 12: {1,2,3,4,6,12}
gcd = meet (greatest lower bound)
lcm = join (least upper bound)
```

This is a distributive lattice isomorphic to the product of chains
N^k where k = number of distinct prime factors.

### Euclid's Lemma (the key tool)

```
If p is prime and p | ab, then p | a or p | b.

Proof: If p ∤ a, then gcd(p,a) = 1 (p has no divisors between 1 and p).
       Bezout: sp + ta = 1
       Multiply by b: spb + tab = b
       p | spb and p | pab, so p | b.  □

This is EXACTLY what fails in Z[√-5]:
  2 | (1+√-5)(1-√-5) = 6, but 2 ∤ (1+√-5) and 2 ∤ (1-√-5).
  "2" is not prime in Z[√-5] in the sense of Euclid's lemma.
  (It's irreducible but not prime — these coincide in PIDs, not in general.)
```

---

## Unique Factorization Theorem

**Theorem (Fundamental Theorem of Arithmetic):**
Every integer n > 1 has a unique representation:
```
n = p₁^{a₁} · p₂^{a₂} · ... · pₖ^{aₖ}

where p₁ < p₂ < ... < pₖ are primes and a_i ≥ 1.
```

**Proof sketch:**
- *Existence*: Induction. If n is not prime, n = ab with a,b < n. By induction,
  a and b factor. Combine.
- *Uniqueness*: Suppose n = p₁·...·pₛ = q₁·...·qₜ (primes, not necessarily distinct).
  Since p₁ | q₁·...·qₜ, by Euclid's lemma p₁ | qⱼ for some j.
  Since qⱼ is prime and p₁ ≥ 2, p₁ = qⱼ. Cancel and induct.

**Why UFT is special:**
```
Z[√-5]:  6 = 2·3 = (1+√-5)(1-√-5)
  Both factorizations use irreducible elements.
  Euclid's lemma fails because Z[√-5] is not a PID.
  To restore unique factorization: use ideals instead of elements.
  (2) = (2, 1+√-5)² in the ideal sense.
```

---

## Primes

### Definition and Basic Facts

```
p is prime if p ≥ 2 and its only divisors are 1 and p.

1 is NOT prime by convention — this makes UFT statement cleaner
  (otherwise "unique" is wrong: 6 = 2·3 = 1·2·3 = 1·1·2·3...)

Primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, ...
```

### Euclid's Proof: Infinitely Many Primes

```
Suppose p₁, p₂, ..., pₙ is the complete list of primes.
Let N = p₁·p₂·...·pₙ + 1.
N > pᵢ for all i, so N is not on our list.
N has a prime divisor p (by UFT existence).
p | N and p | p₁·...·pₙ  →  p | 1  → contradiction.
Therefore no finite list is complete.  □

Note: N itself need not be prime. Example:
  2·3·5·7·11·13 + 1 = 30031 = 59·509.
```

### Stronger Results: Dirichlet's Theorem

```
If gcd(a,q) = 1, then there are infinitely many primes ≡ a (mod q).

Examples:
  Infinitely many primes ≡ 1 (mod 4): 5, 13, 17, 29, 37, ...
  Infinitely many primes ≡ 3 (mod 4): 3, 7, 11, 19, 23, ...
  Infinitely many primes ≡ 1 (mod 6): 7, 13, 19, 31, 37, ...

Proof uses Dirichlet L-functions — see 07-ANALYTIC-NUMBER-THEORY.md.
Purely elementary proof: known only for special cases (a=1, a=-1 mod q).
```

---

## Prime Distribution

### The Prime Counting Function π(x)

```
π(x) = |{p ≤ x : p prime}|

Empirical values:
  π(100)    = 25     (25/100 = 25% of numbers ≤ 100)
  π(1000)   = 168    (16.8%)
  π(10^6)   = 78498  (7.8%)
  π(10^9)   = 50847534 (5.1%)
  π(10^12)  ≈ 3.76×10^10 (3.8%)

Pattern: proportion decreases, ~ 1/ln(x)
```

### Prime Number Theorem

```
π(x) ~ x / ln(x)  as x → ∞

"~" means the ratio π(x) / (x/ln x) → 1.

Better approximation: the logarithmic integral
  Li(x) = ∫₂^x dt/ln(t)  ≈  x/ln(x) + x/(ln x)² + 2x/(ln x)³ + ...

The Riemann Hypothesis predicts:
  |π(x) - Li(x)| < (1/8π) · √x · ln(x)  for all x ≥ 2.657

Unconditionally we only know:
  |π(x) - Li(x)| < C · x · e^{-c·√(ln x)}  (de la Vallée Poussin)
```

### Gaps Between Primes

```
Prime gap g_n = p_{n+1} - p_n

Smallest gap: g = 2 (twin primes: 3,5; 11,13; 17,19; 29,31; ...)
Average gap near x: ~ ln(x)  (by PNT)
Maximal gap: grows (Cramér conjecture: max gap near x is ~ (ln x)²)

Zhang's theorem (2013): lim inf g_n < 246
  i.e., there are infinitely many prime pairs within distance 246.
  Polymath8b improved the bound. Twin prime conjecture: lim inf g_n = 2.

Bertrand's Postulate: for n ≥ 1, there exists prime p with n < p ≤ 2n.
  Proved by Chebyshev 1852; elementary proof by Ramanujan/Erdős.
```

---

## Sieve of Eratosthenes

```
To find all primes ≤ N:
  List: 2, 3, 4, ..., N
  Mark all multiples of 2 starting at 4
  Mark all multiples of 3 starting at 9
  Mark all multiples of 5 starting at 25
  ...
  Mark all multiples of p for each prime p ≤ √N
  Unmarked = primes

Complexity: O(N log log N) — almost linear.

Why only up to √N?
  If n ≤ N is composite, it has a prime factor p ≤ √N.
  (If all factors > √N, their product > N — contradiction.)
```

### Analytic Sieve Theory

```
Legendre's sieve (inclusion-exclusion):
  π(x) - π(√x) + 1 = Σ_{d | P(√x)} μ(d) · ⌊x/d⌋

where P(y) = product of all primes ≤ y, μ = Möbius function.

Problem: inclusion-exclusion has 2^{π(√x)} terms → exponential.
Brun's sieve (1919): truncate the inclusion-exclusion, get bounds.
  Result: Σ_{p,p+2 twin primes} 1/p converges (Brun's constant ≈ 1.902).
  Even if infinitely many twin primes, their reciprocals sum to a finite number.
  (Compare: Σ 1/p diverges — primes are denser.)

Selberg's sieve (1947): optimization via quadratic forms.
  Used in proofs of bounded prime gaps.
```

---

## Number-Theoretic Functions

```
Function        Definition                    Multiplicative?
--------------------------------------------------------
φ(n) — Euler   |{k ≤ n : gcd(k,n)=1}|        Yes
μ(n) — Möbius  0 if p²|n; (-1)^k if          Yes
                n = p₁...pₖ distinct primes
σ(n)           Σ_{d|n} d  (sum of divisors)   Yes
τ(n)           Σ_{d|n} 1  (# divisors)        Yes
Λ(n) — Mangoldt ln p if n=pᵏ; 0 otherwise    Not multiplicative
                                               (but important)
ω(n)           # distinct prime factors       Additive

Multiplicative: f(mn) = f(m)f(n) when gcd(m,n) = 1
Completely multiplicative: f(mn) = f(m)f(n) always

Dirichlet convolution: (f*g)(n) = Σ_{d|n} f(d)g(n/d)
  (Multiplicative functions form a group under Dirichlet convolution)
  Möbius inversion: g = f * 1  ⟹  f = g * μ
```

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Compute gcd(a,b) | Euclidean algorithm |
| Find modular inverse of a mod n | Extended Euclidean |
| Factor n quickly (small) | Trial division up to √n |
| Factor n (medium, ~20 digits) | Pollard rho |
| Factor n (large, ~200+ digits) | Number field sieve |
| Test if n is prime (quick) | Miller-Rabin (probabilistic) |
| Test if n is prime (certain) | AKS (deterministic, slower) |
| Count primes ≤ x | PNT: π(x) ≈ Li(x) ≈ x/ln(x) |
| Find all primes ≤ N | Sieve of Eratosthenes |
| Sum over divisors | Dirichlet convolution / Möbius inversion |
| Prove primes in AP | Dirichlet L-functions |

---

## Common Confusion Points

**"1 should be prime."**
The modern convention (1 is not prime) makes UFT cleaner and number-theoretic
functions work correctly: μ(1) = 1 (not (-1)^0), φ(1) = 1, etc. Historically,
some authors considered 1 prime. The modern convention has been universal since
at least the 19th century.

**"Every prime is odd."**
2 is prime and even. 2 is the "oddest" prime — it's the only even prime.
Its evenness causes special cases everywhere: QR, Wilson's theorem (p=2 is trivial),
Goldbach (sum of two primes — one must be 2 for the sum to be odd prime + 2 = odd).

**"gcd(a,b) = 1 means a and b have no common factors."**
Correct, but the implication is: any equation in a,b can be "split" mod a and mod b
independently. This is the heart of CRT.

**"Prime Number Theorem says primes are rare."**
At scale they thin out, but not uniformly. The gap between consecutive primes
near x is typically ln(x) — so near 10^100, gaps average 230. But PNT also
says there are ~ 10^98 primes up to that point. They thin out but there are
still astronomically many.

**"Bezout gives one solution s,t."**
Bezout's identity gives infinitely many solutions:
  sa + tb = gcd(a,b)
  (s + kb/d)a + (t - ka/d)b = gcd(a,b) for any k ∈ Z.
The Extended Euclidean gives the minimal |s| + |t| solution.
