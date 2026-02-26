# Number Theory — Complete Reference

## The Big Picture

```
NUMBER THEORY
═══════════════════════════════════════════════════════════════════════════

  CLASSICAL                   ANALYTIC                     ALGEBRAIC
  ─────────                   ────────                     ─────────
  Divisibility, GCD, LCM      Zeta ζ(s) and L-functions    Algebraic integers
  Primes, primality tests      Dirichlet's theorem          Rings of integers
  Unique factorization         Prime counting π(x)          Ideals, factorization
  Modular arithmetic           Riemann Hypothesis           Quadratic fields
  Chinese Remainder Theorem    Distribution of primes       Class groups, units

  ARITHMETIC FUNCTIONS         DIOPHANTINE EQUATIONS        MODERN / CRYPTO
  ────────────────────         ─────────────────────        ──────────────────
  φ(n), μ(n), τ(n), σ(n)     Pell's equation x²−Dy²=1    RSA, DH, ECDH
  Multiplicativity, Dirichlet  Pythagorean triples          Discrete log problem
  convolution                  Waring's problem             Elliptic curve theory
  Möbius inversion             Fermat's Last Theorem        Lattices, LWE
  Completely multiplicative    Sums of squares              Post-quantum crypto

  ┌─────────────────────────────────────────────────────────────────────┐
  │  Core theme: Structure of integers, prime distribution, and the    │
  │  algebraic/analytic tools that underpin all of cryptography        │
  └─────────────────────────────────────────────────────────────────────┘
```

**Why it matters for a VP/engineer**: Number theory *is* cryptography. RSA, Diffie-Hellman,
elliptic curves, lattice-based post-quantum schemes — all require understanding primes,
modular arithmetic, and discrete logarithms at a working level. MIT TCS background means
you've seen much of this; this module refreshes it with the crypto angle prominent.

---

## 1. Divisibility and the Integers

### 1.1 Divisibility

```
a | b  ("a divides b") : ∃k ∈ ℤ such that b = k·a

PROPERTIES:
  a|b and b|c  →  a|c          (transitivity)
  a|b and a|c  →  a|(mb + nc)  (linear combinations)
  a|b and b|a  →  a = ±b

DIVISION ALGORITHM:
  For any a,b with b > 0: unique q,r with  a = q·b + r,  0 ≤ r < b
  q = quotient = ⌊a/b⌋,   r = remainder = a mod b
```

### 1.2 GCD, LCM, Bezout's Identity

```
GCD(a,b): largest positive integer dividing both a and b.
LCM(a,b): smallest positive integer divisible by both.

gcd(a,b) · lcm(a,b) = a·b   (for positive integers)

EUCLIDEAN ALGORITHM: O(log min(a,b)) steps
  gcd(a,0) = a
  gcd(a,b) = gcd(b, a mod b)

  Example: gcd(252, 198):
    252 = 1·198 + 54
    198 = 3·54  + 36
     54 = 1·36  + 18
     36 = 2·18  +  0  →  gcd = 18

EXTENDED EUCLIDEAN ALGORITHM:
  Returns x,y such that  a·x + b·y = gcd(a,b)  (BEZOUT'S IDENTITY)

  Bezout coefficients not unique: (x + kb/d, y − ka/d) are also solutions.

COPRIME (relatively prime): gcd(a,b) = 1.
  If gcd(a,b) = 1 and a|bc, then a|c  (Euclid's lemma, key for UFD proofs).
```

### 1.3 Unique Factorization (Fundamental Theorem of Arithmetic)

```
THEOREM: Every integer n > 1 is uniquely expressible as:
  n = p₁^e₁ · p₂^e₂ · ⋯ · pₖ^eₖ    (p₁ < p₂ < ⋯ < pₖ primes, eᵢ ≥ 1)

CONSEQUENCES:
  gcd(a,b) = Π pᵢ^min(eᵢ,fᵢ)
  lcm(a,b) = Π pᵢ^max(eᵢ,fᵢ)

  Number of divisors:  τ(n) = d(n) = Π (eᵢ + 1)
  Sum of divisors:     σ(n) = Π (pᵢ^(eᵢ+1) − 1)/(pᵢ − 1)

UFD FAILURE: In ℤ[√−5], 6 = 2·3 = (1+√−5)(1−√−5)
  → unique factorization into primes fails in rings beyond ℤ.
  This failure motivated algebraic number theory (Kummer's ideal numbers → modern ideals).
```

---

## 2. Primes

### 2.1 Fundamental Facts

```
EUCLID'S THEOREM: Infinitely many primes.
  Proof: Suppose finitely many p₁,...,pₖ. Consider N = p₁⋯pₖ + 1.
  N is divisible by some prime not in the list. Contradiction.

SIEVE OF ERATOSTHENES: finds primes up to N in O(N log log N).

PRIME COUNTING FUNCTION π(x): number of primes ≤ x.
  π(10) = 4, π(100) = 25, π(10⁶) = 78498, π(10⁹) = 50847534

PRIME NUMBER THEOREM (PNT, Hadamard/de la Vallée-Poussin 1896):
  π(x) ~ x/ln(x)   as x → ∞
  Equivalently: pₙ ~ n ln n   (n-th prime asymptotic)
  Better: li(x) = ∫₂ˣ dt/ln(t)  approximates π(x) with error O(x·exp(−c√ln x))
  Under RH: |π(x) − li(x)| < (1/8π)√x · ln x

DIRICHLET'S THEOREM ON PRIMES IN ARITHMETIC PROGRESSIONS (1837):
  If gcd(a,d) = 1, there are infinitely many primes of the form a + nd, n∈ℕ.
  Density: primes equidistributed among φ(d) residue classes mod d.
  Proof: L-functions, Dirichlet characters (first use of analytic methods).
```

### 2.2 Primality Testing

```
TRIAL DIVISION: O(√n). Sufficient for small n.

FERMAT PRIMALITY TEST:
  If p is prime: aᵖ⁻¹ ≡ 1 (mod p) for gcd(a,p)=1  (Fermat's little theorem)
  Test: pick random a, check aⁿ⁻¹ ≡ 1 (mod n).
  PROBLEM: Carmichael numbers (e.g., 561 = 3·11·17) pass for all a coprime to n!
    Carmichael number: composite n satisfying aⁿ⁻¹ ≡ 1 (mod n) for all gcd(a,n)=1.

MILLER-RABIN TEST (probabilistic, industry standard):
  Write n−1 = 2ˢ·d (d odd). For random a:
    Compute a^d mod n.
    If ≡ 1 or −1 mod n: probably prime (this base passes).
    Else: square s times. If some squaring gives −1: probably prime.
    Else: definitely composite.

  Error probability ≤ 1/4 per witness.
  k rounds: error ≤ (1/4)ᵏ.
  For n < 3·10¹²: {2,3,5,7,11,13,17} witnesses are DETERMINISTIC.
  Under GRH: O((log n)²) deterministic witnesses suffice.

AKS PRIMALITY TEST (2002, Agrawal-Kayal-Saxena):
  First deterministic polynomial-time primality test: O(log⁶ n).
  Theoretical landmark; Miller-Rabin still used in practice (faster).

LUCAS PRIMALITY TEST: uses factorization of n−1; deterministic but requires factor.
```

<!-- @editor[bridge/P2]: Missing the connection between primality testing and the broader context of randomized algorithms — Miller-Rabin is a classic example of a coRP algorithm (always correct on composites, probably correct on primes). The question of whether PRIMES ∈ P was open until AKS. Connection to derandomization: is every BPP problem in P? AKS is evidence yes. -->

### 2.3 Integer Factorization

```
TRIAL DIVISION: O(√n). Impractical beyond ~10¹⁵.

POLLARD'S RHO (Floyd cycle detection):
  Heuristic O(n^(1/4)) per factor. Used in practice for medium n.
  x_{i+1} = x²ᵢ + c mod n. Detect cycle → gcd gives factor.

QUADRATIC SIEVE (QS):
  Subexponential: O(exp(√(log n · log log n)))
  Best for n < 10¹⁰⁰ (roughly).

GENERAL NUMBER FIELD SIEVE (GNFS):
  Fastest known: O(exp((64/9)^(1/3) (log n)^(1/3) (log log n)^(2/3)))
  RSA-768 (768 bits, 232 digits) factored in 2009: ~2000 CPU-years.
  RSA-2048 (currently secure): beyond reach by large factor.

SHOR'S ALGORITHM (quantum): O((log n)³) — polynomial!
  Reduces factoring to period-finding of aˣ mod n.
  Practical quantum factoring: requires millions of error-corrected qubits.
  RSA is theoretically broken by quantum computers — motivates PQC.
```

---

## 3. Modular Arithmetic

### 3.1 Congruences

```
a ≡ b (mod n)  iff  n | (a−b)  iff  a mod n = b mod n

ARITHMETIC RULES:
  a ≡ b, c ≡ d  ⟹  a+c ≡ b+d,  a·c ≡ b·d  (mod n)
  aᵏ ≡ bᵏ  (mod n)

CANCELLATION: ac ≡ bc (mod n)  ⟹  a ≡ b (mod n/gcd(c,n))
  If gcd(c,n) = 1: ac ≡ bc → a ≡ b  (true cancellation)

MODULAR INVERSE: a⁻¹ mod n exists iff gcd(a,n) = 1.
  Compute via extended Euclidean: a·x + n·y = 1  →  x = a⁻¹ mod n.
```

### 3.2 ℤ/nℤ — The Ring of Integers mod n

```
ℤ/nℤ = {0, 1, ..., n−1} under +ₙ and ×ₙ.

FIELD iff n is prime:  ℤ/pℤ = 𝔽ₚ  (every nonzero element invertible)

(ℤ/nℤ)× = group of units = {a : gcd(a,n)=1}
  |(ℤ/nℤ)×| = φ(n)  (Euler's totient)

STRUCTURE OF THE UNITS:
  n = pᵏ (p odd prime):  (ℤ/pᵏℤ)× ≅ ℤ/φ(pᵏ)ℤ  (cyclic)
  n = 2ᵏ (k≥3):         (ℤ/2ᵏℤ)× ≅ ℤ/2 × ℤ/2^(k-2)  (NOT cyclic)
  n = Π pᵢᵉⁱ:           (ℤ/nℤ)× ≅ Π (ℤ/pᵢᵉⁱℤ)×  (CRT)

PRIMITIVE ROOT (generator of cyclic group):
  g is a primitive root mod n if g generates (ℤ/nℤ)×.
  Exists iff n = 1, 2, 4, pᵏ, or 2pᵏ for odd prime p.
  For prime p: there are φ(p−1) primitive roots mod p.
```

### 3.3 Euler's Theorem and Fermat's Little Theorem

```
EULER'S THEOREM:
  If gcd(a,n) = 1:   a^φ(n) ≡ 1 (mod n)

FERMAT'S LITTLE THEOREM (n = p prime):
  aᵖ⁻¹ ≡ 1 (mod p)   for a ≢ 0 (mod p)
  aᵖ ≡ a (mod p)      for all a (including a divisible by p)

LAGRANGE'S THEOREM (group theory):
  Order of any element divides |G| = φ(n).
  If g has order d mod p, then aᵏ ≡ 1 (mod p) iff d|k.

COMPUTING POWERS: fast exponentiation — square-and-multiply O(log e) multiplications.
  aᵉ mod n: write e in binary, square and conditionally multiply.
  This is the core of RSA encryption/decryption, Miller-Rabin, etc.

EULER TOTIENT FUNCTION:
  φ(1) = 1
  φ(p) = p − 1      (p prime)
  φ(pᵏ) = pᵏ − pᵏ⁻¹ = pᵏ⁻¹(p−1)
  φ(mn) = φ(m)φ(n)   if gcd(m,n) = 1  (multiplicative)
  φ(n) = n · Π_{p|n} (1 − 1/p)
```

### 3.4 Chinese Remainder Theorem (CRT)

```
CRT: If n₁,...,nₖ pairwise coprime, the system:
    x ≡ a₁ (mod n₁)
    x ≡ a₂ (mod n₂)
    ⋮
    x ≡ aₖ (mod nₖ)
  has unique solution mod N = n₁·n₂·⋯·nₖ.

CONSTRUCTION:
  Nᵢ = N/nᵢ
  Mᵢ = Nᵢ⁻¹ mod nᵢ  (exists since gcd(Nᵢ, nᵢ) = 1)
  x = Σ aᵢ·Nᵢ·Mᵢ  mod N

RING ISOMORPHISM:
  ℤ/Nℤ ≅ ℤ/n₁ℤ × ⋯ × ℤ/nₖℤ   (when nᵢ pairwise coprime)

APPLICATIONS:
  RSA-CRT speed-up: compute mod p and mod q separately, combine (4× faster decryption)
  Polynomial interpolation: CRT for polynomials
  Multi-precision arithmetic: base-ℬ representation via CRT
  Secret sharing (Asmuth-Bloom scheme): CRT-based threshold secret sharing
```

---

## 4. Arithmetic Functions

### 4.1 Classical Functions

```
ARITHMETIC FUNCTION: f: ℤ⁺ → ℂ

MULTIPLICATIVITY:
  f is multiplicative:          f(mn) = f(m)f(n) when gcd(m,n) = 1
  f is completely multiplicative: f(mn) = f(m)f(n) always

TABLE OF CLASSICAL FUNCTIONS:

Function  | Symbol  | Definition              | Value at pᵉ     | Type
──────────┼─────────┼─────────────────────────┼─────────────────┼──────────────
Totient   | φ(n)    | |{k≤n : gcd(k,n)=1}|   | pᵉ−pᵉ⁻¹        | multiplicative
Divisors  | d(n)=τ(n)| #{d : d|n}             | e+1             | multiplicative
Sum divs  | σ(n)    | Σ_{d|n} d               | (pᵉ⁺¹−1)/(p−1) | multiplicative
Möbius    | μ(n)    | see below               | −1 if e=1, else 0| multiplicative
Liouville | λ(n)    | (−1)^Ω(n)               | (−1)ᵉ           | completely mult
Identity  | ε(n)    | [n=1]                   | [e=0]            | completely mult
Unit fn   | 1(n)    | 1                       | 1               | completely mult
Id fn     | id(n)   | n                       | pᵉ              | completely mult

MÖBIUS FUNCTION:
  μ(1) = 1
  μ(n) = 0 if n has any prime factor squared (not squarefree)
  μ(p₁p₂⋯pₖ) = (−1)ᵏ  (product of k distinct primes)
```

### 4.2 Dirichlet Convolution and Möbius Inversion

```
DIRICHLET CONVOLUTION:
  (f * g)(n) = Σ_{d|n} f(d)·g(n/d)

  Multiplicative × multiplicative = multiplicative.
  Forms a commutative ring under + and *.
  Identity element: ε (= [n=1]).

KEY RELATIONS:
  φ = μ * id   (φ(n) = Σ_{d|n} μ(d)·(n/d))
  σ = 1 * id   (σ(n) = Σ_{d|n} d)
  d = 1 * 1    (d(n) = Σ_{d|n} 1)
  μ * 1 = ε    (Σ_{d|n} μ(d) = [n=1])

MÖBIUS INVERSION:
  f(n) = Σ_{d|n} g(d)  ↔  g(n) = Σ_{d|n} μ(n/d)·f(d)   (= (f * μ)(n))
  Exact analogue of Möbius inversion on the divisibility poset.
```

### 4.3 Dirichlet Series

```
DIRICHLET SERIES of f: F(s) = Σ_{n=1}^∞ f(n)/nˢ

RIEMANN ZETA FUNCTION:
  ζ(s) = Σ 1/nˢ = Π_{p prime} 1/(1−p⁻ˢ)   (Euler product, Re(s)>1)

  Analytic continuation to all ℂ except s=1 (simple pole).
  Functional equation: ζ(s) = 2ˢπˢ⁻¹ sin(πs/2) Γ(1−s) ζ(1−s)

NOTABLE VALUES:
  ζ(2) = π²/6   (Basel problem, Euler 1734)
  ζ(4) = π⁴/90
  ζ(2k) = (−1)^(k+1) (2π)^(2k) B_{2k} / (2(2k)!)  (Bernoulli numbers)
  ζ(−1) = −1/12  (regularized, analytic continuation — Ramanujan)
  ζ(0) = −1/2
  ζ(1) = divergent (simple pole, residue 1)

DIRICHLET SERIES ↔ CONVOLUTION:
  (Σ f(n)/nˢ)(Σ g(n)/nˢ) = Σ (f*g)(n)/nˢ
  1/ζ(s) = Σ μ(n)/nˢ   (Möbius function generates inverse of ζ)
  ζ(s)² = Σ d(n)/nˢ    (divisor function)
  ζ(s−1)/ζ(s) = Σ φ(n)/nˢ
```

---

## 5. Quadratic Residues

### 5.1 Quadratic Residues

```
QUADRATIC RESIDUE mod p (p odd prime):
  a is a QR mod p if ∃x: x² ≡ a (mod p).
  a is a QNR (quadratic non-residue) if no such x exists.

COUNT: exactly (p−1)/2 nonzero QRs mod p, (p−1)/2 QNRs.

EULER'S CRITERION:
  a^((p-1)/2) ≡ +1 (mod p)  iff  a is a QR mod p
  a^((p-1)/2) ≡ −1 (mod p)  iff  a is a QNR mod p

LEGENDRE SYMBOL:
  (a/p) = { 0  if p|a
           { +1 if a is QR mod p
           { −1 if a is QNR mod p

  = a^((p-1)/2) mod p  (by Euler's criterion)

PROPERTIES:
  (ab/p) = (a/p)(b/p)             (completely multiplicative in a)
  (a/p) = (b/p) if a ≡ b (mod p)
  (−1/p) = (−1)^((p-1)/2)  = +1 iff p ≡ 1 (mod 4)
  (2/p) = (−1)^((p²-1)/8)  = +1 iff p ≡ ±1 (mod 8)
```

### 5.2 Quadratic Reciprocity

```
QUADRATIC RECIPROCITY (Gauss 1796 — his "golden theorem"):
  For distinct odd primes p, q:
    (p/q)(q/p) = (−1)^((p-1)/2 · (q-1)/2)

  Equivalently:
    (p/q)(q/p) = +1  unless  p ≡ q ≡ 3 (mod 4)
    (p/q)(q/p) = −1  if     p ≡ q ≡ 3 (mod 4)

  "Is p a QR mod q?" and "Is q a QR mod p?" are linked, with a sign flip
  only when both ≡ 3 mod 4.

JACOBI SYMBOL (a/n): extends Legendre to composite n.
  (a/n) = Π (a/pᵢ)^eᵢ  where n = Π pᵢᵉⁱ
  (a/n) = −1 → a is NOT a QR mod n.
  (a/n) = +1 → a MIGHT be a QR mod n (not conclusive for composite n).
  Jacobi symbol obeys same reciprocity law and is efficient to compute.
```

### 5.3 Square Roots mod p

```
TONELLI-SHANKS ALGORITHM: Compute √a mod p in O(log² p) time.
  Write p−1 = Q·2ˢ (Q odd).
  Start with initial estimate, iteratively correct.

CIPOLLA'S ALGORITHM: Alternative O(log² p), simpler to implement.

SQUARE ROOTS mod pᵏ: use Hensel's lemma to lift.

SQUARE ROOTS mod pq (RSA modulus):
  Computing √a mod n where n=pq is equivalent to factoring n!
  This is why RSA hardness = factoring hardness.
```

<!-- @editor[bridge/P2]: Quadratic residues connect directly to the Rabin cryptosystem (squaring mod n, hardness = factoring) and to zero-knowledge proofs — the classic Goldwasser-Micali scheme encrypts bits using QR/QNR. Also useful: Blum integers (p ≡ q ≡ 3 mod 4) ensure −1 is QNR, giving the Blum-Blum-Shub PRNG. These are natural crypto payoffs for this section. -->

---

## 6. Diophantine Equations

### 6.1 Linear Diophantine Equations

```
ax + by = c has integer solutions iff gcd(a,b) | c.

IF solvable:
  General solution: (x₀ + tb/d, y₀ − ta/d) for t ∈ ℤ
  where (x₀,y₀) is a particular solution (from extended Euclidean)
  and d = gcd(a,b).
```

### 6.2 Pythagorean Triples

```
PYTHAGOREAN TRIPLE: integers a,b,c with a²+b²=c².

PRIMITIVE TRIPLE (gcd(a,b,c)=1):
  Parametrized by m > n > 0, gcd(m,n)=1, not both odd:
    a = m²−n², b = 2mn, c = m²+n²

  Every primitive triple arises this way.
  E.g., (m,n)=(2,1) → (3,4,5); (3,2) → (5,12,13); (4,1) → (15,8,17).

All Pythagorean triples: multiply any primitive by k ≥ 1.
```

### 6.3 Sums of Squares

```
FERMAT'S THEOREM ON SUMS OF TWO SQUARES:
  Odd prime p = a² + b² iff p ≡ 1 (mod 4).
  p = 2: 2 = 1² + 1².
  p ≡ 3 (mod 4): NOT a sum of two squares.

SUM OF TWO SQUARES FOR GENERAL n:
  n = a² + b² iff in prime factorization of n, every prime p ≡ 3 (mod 4)
  appears to an even power.

LAGRANGE'S FOUR-SQUARE THEOREM:
  Every positive integer is a sum of four squares.
  n = a² + b² + c² + d² always.
  Proof: quaternion norm is multiplicative (Euler's four-square identity).

LEGENDRE'S THREE-SQUARE THEOREM:
  n = a²+b²+c² iff n ≠ 4^a(8b+7) for any a,b ≥ 0.

WARING'S PROBLEM:
  Every n is sum of at most g(k) k-th powers.
  g(2) = 4, g(3) = 9, g(4) = 19.
```

### 6.4 Pell's Equation

```
PELL'S EQUATION: x² − Dy² = 1  (D > 0, D not a perfect square)

Always has infinitely many solutions.
FUNDAMENTAL SOLUTION (x₁, y₁): smallest positive solution.
  All solutions generated from fundamental: xₙ + yₙ√D = (x₁ + y₁√D)ⁿ

CONTINUED FRACTION METHOD:
  √D has periodic continued fraction: √D = [a₀; a₁, a₂, ..., aₗ, a₁, a₂, ...]
  Fundamental solution found in convergents of √D.

GENERALIZED PELL: x² − Dy² = N  (same continued fraction machinery).

CONNECTION TO ALGEBRAIC NT:
  Solutions = units in ring ℤ[√D].
  Dirichlet's unit theorem: rank of unit group = r₁ + r₂ − 1 in number field.
```

### 6.5 Fermat's Last Theorem

```
FERMAT'S LAST THEOREM (1637 conjecture, Wiles 1995):
  No integers x,y,z > 0 satisfy xⁿ + yⁿ = zⁿ for n ≥ 3.

PROOF PATH (wildly simplified):
  Frey (1984): Galois representation attached to hypothetical Fermat solution is "strange".
  Serre's ε-conjecture + Ribet (1990): this representation cannot come from modular form.
  Wiles (1995): Taniyama-Shimura conjecture for semistable elliptic curves.
    Every elliptic curve E/ℚ is modular (L(E,s) = L(f,s) for modular form f).
  Combining: Fermat solution → elliptic curve → modular form → contradiction.
  Breuil-Conrad-Diamond-Taylor (2001): full Taniyama-Shimura-Weil (now Modularity Theorem).

ELEMENTARY CASES:
  n=3: Euler (1770)
  n=4: Fermat himself (descent method)
  p prime: regular primes (Kummer 1847 — most primes up to 125 are regular)
  General p < 10⁶: computational (1993)
```

---

## 7. p-adic Numbers

### 7.1 Construction

```
p-ADIC VALUATION: vₚ(n) = largest k with pᵏ | n.
  vₚ(0) = +∞
  vₚ(pᵏ·m) = k + vₚ(m)  (m not divisible by p)

p-ADIC ABSOLUTE VALUE:
  |n|ₚ = p^(−vₚ(n))
  |0|ₚ = 0

Non-Archimedean: |x + y|ₚ ≤ max(|x|ₚ, |y|ₚ)  [ultrametric inequality, STRONGER than triangle]

ℚₚ (p-adic numbers): completion of ℚ with respect to |·|ₚ.
  Just as ℝ = completion of ℚ with |·|∞, ℚₚ = completion with |·|ₚ.
  By Ostrowski's theorem: these are ALL absolute values on ℚ.

ADELES: restricted product ℝ × Π ℚₚ = 𝔸ℚ
  Modern number theory lives here — all primes simultaneously.
```

### 7.2 p-adic Integers and Structure

```
ℤₚ = {x ∈ ℚₚ : |x|ₚ ≤ 1} = p-adic integers

Representation: every x ∈ ℤₚ uniquely as
  x = a₀ + a₁p + a₂p² + ⋯   (aᵢ ∈ {0,...,p−1})
  "Power series in p" — infinite to the LEFT in p-adic, not right!

HENSEL'S LEMMA:
  If f(a₀) ≡ 0 (mod p) and f'(a₀) ≢ 0 (mod p), then f has a root in ℤₚ.
  "Lift a solution mod p to solution mod p∞."
  E.g., x² ≡ a (mod p) with solution → unique √a in ℤₚ.

TEICHMÜLLER REPRESENTATIVES: (p−1)-th roots of unity in ℤₚ.

WHY p-ADICS MATTER:
  • Hasse-Minkowski: quadratic forms over ℚ → iff over ℝ and all ℚₚ
    ("local-global principle" = check everywhere locally)
  • Modularity, l-adic Galois representations (key in Wiles's proof)
  • p-adic L-functions, Iwasawa theory
```

---

## 8. Algebraic Number Theory Essentials

### 8.1 Number Fields

```
NUMBER FIELD K: finite extension of ℚ.
  K = ℚ(α) where α is algebraic over ℚ with minimal polynomial f(x).
  [K:ℚ] = degree = deg(f).

RING OF INTEGERS 𝒪_K: algebraic integers in K.
  ℤ ⊂ 𝒪_K ⊂ K,   𝒪_K ∩ ℚ = ℤ
  𝒪_K is a free ℤ-module of rank [K:ℚ].

QUADRATIC FIELDS ℚ(√d) (d squarefree):
  𝒪_K = ℤ[√d]          if d ≡ 2,3 (mod 4)
  𝒪_K = ℤ[(1+√d)/2]    if d ≡ 1   (mod 4)   ← "half-integers"
  Discriminant Δ = 4d or d (resp.).

PRIME SPLITTING: how rational prime p behaves in 𝒪_K.
  p𝒪_K = 𝔭₁^e₁ ⋯ 𝔭_g^eg
  In ℚ(√d): p splits if Kronecker symbol (d/p)=1, stays inert if −1, ramifies if 0.
```

### 8.2 Ideals and Unique Factorization

```
THE FIX FOR UFD FAILURE:
  In general 𝒪_K, elements may not factor uniquely into primes.
  BUT: every nonzero ideal factors UNIQUELY into prime ideals.
  𝒪_K is a Dedekind domain.

IDEAL CLASS GROUP Cl(K):
  Fractional ideals mod principal ideals.
  h_K = |Cl(K)| = class number.
  h_K = 1  iff  𝒪_K is a UFD.
  ℚ(√−1): h=1 (Gaussian integers, UFD)
  ℚ(√−5): h=2 (where 6 = 2·3 = (1+√−5)(1−√−5) fails UFD)

MINKOWSKI BOUND: h_K is computable; every ideal class contains ideal of small norm.

DIRICHLET'S UNIT THEOREM:
  𝒪_K× ≅ μ_K × ℤ^(r₁+r₂−1)
  μ_K = roots of unity in K
  r₁ = real embeddings, r₂ = pairs of complex embeddings (r₁+2r₂=[K:ℚ])
  "Pell's equation = unit group of real quadratic field"
```

<!-- @editor[content/P2]: Missing cyclotomic fields ℚ(ζₙ) — the algebraic number theory most directly tied to cryptography. Galois group Gal(ℚ(ζₙ)/ℚ) ≅ (ℤ/nℤ)×. Ring of integers ℤ[ζₙ]. Class number h(ℚ(ζₚ)) = 1 for p ≤ 19 (regular primes). This is the arithmetic behind RLWE-based cryptography (polynomial ring ℤ[x]/(xⁿ+1) ≅ ℤ[ζ_{2n}] for n a power of 2). Connection between algebraic NT and PQC is the core payoff here. -->

---

## 9. Cryptography — The Payoff

### 9.1 RSA

```
RSA SETUP:
  Choose large primes p, q (~1024-2048 bits each).
  n = p·q   (public modulus, 2048-4096 bits)
  φ(n) = (p−1)(q−1)
  Choose e coprime to φ(n), 1 < e < φ(n). Often e = 65537 = 2¹⁶+1.
  d = e⁻¹ mod φ(n)  (private key exponent, via extended Euclidean)
  Public key: (n, e).  Private key: (n, d).

ENCRYPT: c = mᵉ mod n
DECRYPT: m = cᵈ mod n

CORRECTNESS: cᵈ = mᵉᵈ = m^(1 + kφ(n)) ≡ m (mod n) by Euler's theorem.

SECURITY:
  Breaking RSA = factoring n (in standard model).
  Given φ(n) or d, can factor n.
  OAEP padding required (raw RSA vulnerable to attacks).

RSA-CRT SPEEDUP: compute m^d mod p and m^d mod q separately using d_p = d mod (p−1),
  d_q = d mod (q−1), then CRT to combine. Roughly 4× faster decryption.

KEY SIZES (2024):
  RSA-2048: 112-bit security equivalent
  RSA-3072: 128-bit security equivalent
  RSA-4096: ~140 bits
  Recommended transition to elliptic curves (256 bits → 128-bit security, much smaller).
```

<!-- @editor[bridge/P2]: Missing common RSA attacks — small exponent attack (e=3, m small → m³ < n, just take cube root), Wiener's attack (small d via continued fractions), fault attacks (glitching CRT computation leaks p or q), timing side-channels. These are the reason why OAEP and constant-time implementations matter, and they're natural payoffs for the number theory developed above. -->

### 9.2 Discrete Logarithm Problem

```
DLP: Given g, y in a group G, find x such that gˣ = y.
  Easy to compute gˣ mod p; hard to invert.

DIFFIE-HELLMAN KEY EXCHANGE (1976):
  Public: prime p, generator g of (ℤ/pℤ)×.
  Alice: picks secret a, sends A = gᵃ mod p.
  Bob:   picks secret b, sends B = gᵇ mod p.
  Shared: K = gᵃᵇ = Aᵇ = Bᵃ mod p.
  Eavesdropper sees g,p,A,B but can't compute gᵃᵇ without solving DLP.

DLP ATTACKS:
  Baby-step giant-step:  O(√p) time and space.
  Pohlig-Hellman:        O(√max prime factor of p−1) — use safe primes (p where (p−1)/2 is prime)
  Index calculus (sub-exp): works for 𝔽ₚ× but NOT for elliptic curves!

ELGAMAL ENCRYPTION: probabilistic encryption built on DH.
  DSA/ECDSA: digital signatures from discrete log.

SECURITY: p should be ≥ 2048 bits for 112-bit security.
  Group order should have large prime factor (safe/strong primes).
```

### 9.3 Elliptic Curves

```
ELLIPTIC CURVE over 𝔽ₚ:
  y² = x³ + ax + b  (mod p),  4a³ + 27b² ≠ 0 (mod p)
  Points: solutions (x,y) ∈ 𝔽ₚ × 𝔽ₚ, plus "point at infinity" 𝒪.

GROUP LAW: E(𝔽ₚ) forms an abelian group under chord-and-tangent addition.
  P + Q: draw line through P,Q, reflect x-axis intersection.
  P + P (doubling): tangent line.
  𝒪 = identity.

GROUP ORDER |E(𝔽ₚ)| ~ p  (Hasse-Weil: |#E − (p+1)| ≤ 2√p)

ECDLP: given P and Q = kP, find k. Harder per bit than DLP in 𝔽ₚ×.
  No sub-exponential algorithm known for EC over prime fields.
  Best: generic Pollard-ρ in O(√q) where q = group order.

NIST CURVES: P-256, P-384, P-521 (prime field, NIST-recommended)
DJBCURVE25519: Bernstein's Curve25519 — x25519 = Diffie-Hellman on Curve25519 (modern standard)
  Montgomery form: y² = x³ + 486662x² + x mod (2²⁵⁵−19)

EC KEY SIZES:
  256-bit key → 128-bit security  (vs RSA-3072 for same security)
  384-bit key → 192-bit security
  521-bit key → 260-bit security

ECDSA: signing (k-random nonce critical! PS3 reuse → key recovery)
ECDH: key exchange on elliptic curves (x25519 in TLS 1.3)
```

<!-- @editor[content/P2]: Missing pairing-based cryptography — bilinear pairings e: E(𝔽_q) × E(𝔽_q) → 𝔽_{q^k}. Enable: identity-based encryption (IBE), BLS signatures (short, aggregatable — used in Ethereum 2.0), and the MOV attack (reduces ECDLP to DLP in 𝔽_{q^k}). Supersingular isogeny cryptography (SIKE) was also a PQC candidate (broken 2022). The diversity of EC-based constructions goes well beyond ECDH/ECDSA. -->

### 9.4 Post-Quantum Cryptography (Lattices)

```
MOTIVATION: Shor's algorithm breaks RSA and ECDH in polynomial quantum time.
  NIST PQC standardization (finalized 2024):
    ML-KEM (Kyber): key encapsulation — default for key exchange
    ML-DSA (Dilithium): digital signatures
    SLH-DSA (SPHINCS+): hash-based signatures
    (FALCON also selected for signatures)

LATTICE BASICS:
  Lattice Λ ⊂ ℝⁿ: Λ = {Σ aᵢbᵢ : aᵢ ∈ ℤ} for basis {b₁,...,bₙ}
  Different bases → same lattice (basis reduction: LLL algorithm)

HARD PROBLEMS:
  SVP (Shortest Vector Problem): find shortest nonzero vector in Λ. NP-hard (worst-case).
  CVP (Closest Vector Problem): find lattice point nearest a target. NP-hard.

LWE (Learning With Errors, Regev 2005):
  Given Ax + e = b mod q (x secret, e small noise), recover x.
  Hard for quantum computers (worst-case lattice problems reduce to LWE).
  ML-KEM/CRYSTALS-Kyber based on Module-LWE.

RLWE (Ring LWE): LWE over polynomial ring ℤ[x]/(xⁿ+1).
  Much more efficient (polynomial operations).
  Kyber, Dilithium use Module variants.

LLL BASIS REDUCTION: O(n⁵ log³ B) — solves "approximate" SVP.
  Used in: breaking knapsack cryptosystems, finding short polynomial factorizations,
  COPPERSMITH method for finding small roots of polynomials mod N (partial key recovery for RSA).
```

---

## 10. Analytic Number Theory Highlights

### 10.1 The Riemann Hypothesis

```
RIEMANN ZETA FUNCTION ζ(s) = Σ n⁻ˢ = Π (1−p⁻ˢ)⁻¹  for Re(s) > 1
  Analytically continued to ℂ \ {1}.

TRIVIAL ZEROS: negative even integers s = −2, −4, −6, ...
NONTRIVIAL ZEROS: ρ = 1/2 + it (RH claims they all lie on critical line Re(s) = 1/2)

RIEMANN HYPOTHESIS: All nontrivial zeros have Re(ρ) = 1/2.
  Status: unproven. Oldest and most famous open problem in mathematics.
  Verified for first 10¹³+ zeros (all on critical line).
  Millennium Prize Problem ($1M prize).

CONSEQUENCES OF RH (if true):
  π(x) − li(x) = O(√x log x)  (sharp prime counting error)
  For any ε > 0: π(x) = li(x) + O(x^(1/2+ε))
  Gaps between consecutive primes: pₙ₊₁ − pₙ = O(√pₙ log pₙ)

ANALOGUE RH: Proved for function fields (Weil 1948), finite fields (Deligne 1974).
  The proof of the Weil conjectures uses étale cohomology — modern algebraic geometry.
```

### 10.2 Primes in Short Intervals and Gaps

```
BERTRAND'S POSTULATE (Chebyshev 1850): For n ≥ 1, prime p with n < p ≤ 2n.
  Strengthened: prime in (n, n + c·n/ln n] for small enough c.

TWIN PRIMES: primes p with p+2 also prime. (3,5), (5,7), (11,13), ...
  Twin prime conjecture: infinitely many. Open.
  Zhang (2013): infinitely many prime pairs with gap < 7×10⁷.
  Maynard-Tao (2014): gaps < 246. Polymath project: further progress.

PRIME GAPS: consecutive prime gaps pₙ₊₁ − pₙ.
  Cramér conjecture: max gap around pₙ is O((log pₙ)²).
  Green-Tao theorem (2004): primes contain arbitrarily long arithmetic progressions.
  Goldbach's conjecture: every even n > 2 is sum of two primes. Open.
  Goldbach verified up to ~4×10¹⁸.
  Helfgott (2013): every odd n > 5 is sum of three primes (weak Goldbach, proved).
```

---

## 11. Decision Cheat Sheet

| Need | Tool | Key result |
|------|------|-----------|
| Compute gcd | Euclidean algorithm | O(log n) |
| Solve ax+by=c | Extended Euclidean | Bezout coefficients |
| Solve system of congruences | CRT | Unique solution mod N=Πnᵢ |
| Modular inverse | Extended Euclidean | O(log n) |
| Modular exponentiation | Square-and-multiply | O(log e) mults |
| Test primality (fast) | Miller-Rabin | Probabilistic, error < 4⁻ᵏ |
| Test primality (deterministic) | AKS | O(log⁶ n) — slow in practice |
| Factor small n | Trial / Pollard-ρ | O(n^(1/4)) |
| Factor large n | GNFS | Subexponential |
| Quadratic residue? | Euler's criterion | O(log p) |
| Square root mod p | Tonelli-Shanks | O(log² p) |
| RSA setup | φ(n)=(p−1)(q−1), Bezout for d | Pick e=65537 |
| ECDH key exchange | Group law on E(𝔽ₚ) | 256-bit → 128-bit security |
| Post-quantum KEM | ML-KEM (Kyber) / LWE | NIST 2024 standard |

---

## 12. Common Confusion Points

**Euler's theorem vs. Fermat's little theorem**: FLT is the special case n = prime p
(φ(p) = p−1). Euler's theorem handles composite n, but requires gcd(a,n)=1.

**Carmichael numbers**: Composite numbers that pass Fermat's test for all bases.
561 = 3·11·17 is the smallest. They don't fool Miller-Rabin, which is why we use that instead.

**RSA security = factoring, but not provably equivalent**: We know factoring → break RSA.
We do NOT know RSA → factoring in general. There might be ways to decrypt without factoring.
(Recovering d from e,n does imply factoring, however.)

**DLP vs ECDLP**: Discrete log in 𝔽ₚ× has index calculus (sub-exponential).
On elliptic curves, no such algorithm exists — so 256-bit EC = 3072-bit RSA in security,
much shorter keys.

**p-adic integers ℤₚ vs 𝔽ₚ**: ℤₚ is characteristic zero (infinite), 𝔽ₚ = ℤ/pℤ
is characteristic p (finite, p elements). Common notation clash — 𝔽ₚ is the field.

**Prime ≠ irreducible in non-UFDs**: In ℤ[√−5], 3 is irreducible (can't factor) but not
prime (doesn't satisfy p|ab → p|a or p|b). In ℤ (UFD), prime = irreducible.

**LWE noise is essential**: If e = 0, LWE is easy linear algebra (Gaussian elimination).
The noise makes it hard AND introduces the "learning" problem structure.

**Quadratic reciprocity direction**: (p/q) = "is p a square mod q?"
The law swaps p↔q with possible sign flip. It's not immediately obvious why this would
hold at all — the proof requires serious machinery (Gauss sums, characters, etc.).

**Class number 1 does not mean ℤ[α] = 𝒪_K**: Sometimes the ring of integers is
larger than ℤ[α]. E.g., ℤ[(1+√5)/2] vs ℤ[√5]. Always compute the discriminant.
