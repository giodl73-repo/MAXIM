# Number Theory — Landscape Overview

## The Big Picture

```
+===========================================================================+
|                    NUMBER THEORY — FOUR BRANCHES                          |
+===========================================================================+
|                                                                           |
|  ELEMENTARY          ANALYTIC              ALGEBRAIC       COMPUTATIONAL  |
|  +------------+    +------------+        +------------+  +------------+  |
|  |Divisibility|    |Riemann ζ(s)|        |Number      |  |Primality   |  |
|  |GCD/LCM/UFT |    |L-functions |        |fields K    |  |testing     |  |
|  |Congruences |    |PNT         |        |Rings O_K   |  |Factoring   |  |
|  |CRT         |    |Dirichlet   |        |Ideal class |  |DLP         |  |
|  |Prim. roots |    |series      |        |group       |  |Sieving     |  |
|  |Quad. recip.|    |Sieves      |        |Class field |  |NFS/Pollard |  |
|  +------------+    +------------+        +------------+  +------------+  |
|        |                 |                     |                |        |
|        +--------+--------+------+--------------+                |        |
|                 |               |                               |        |
|          CONNECTIONS       CONNECTIONS                    APPLICATIONS    |
|          TO GEOMETRY       TO PHYSICS                                     |
|          Elliptic curves   RMT ↔ ζ zeros                 RSA, ECC        |
|          Algebraic geom.   Quantum chaos                  Reed-Solomon    |
|          Modular forms      GUE spacing                   Lattice crypto  |
+===========================================================================+
```

**The central tension**: primes are defined locally (indivisibility) but their
global distribution (how many primes ≤ x?) requires complex analysis to understand.
That gap between local definition and global behavior IS number theory.

---

## Branch Descriptions

### Elementary Number Theory

The foundations: divisibility, GCD, unique factorization, congruences,
Euler's φ function, primitive roots, quadratic residues. Everything that
can be stated without limits or field extensions.

Do not mistake "elementary" for "easy." Quadratic reciprocity has 246 known
proofs. Elementary sieves give the best known bounds on twin primes.

### Analytic Number Theory

Uses tools from complex analysis — Riemann ζ(s), Dirichlet L-functions,
contour integrals — to prove facts about integers.

The Prime Number Theorem (π(x) ~ x/ln x) was first proved analytically.
No purely combinatorial proof is known that is as sharp.

The Riemann Hypothesis lives here.

### Algebraic Number Theory

Generalizes Z to rings of integers O_K in number fields K = Q(α).
The central discovery: unique factorization fails in O_K, but *ideal*
factorization is always unique.

The measure of failure: the class group Cl(K). If |Cl(K)| = 1, unique
factorization holds. Otherwise, the class number h_K measures the obstruction.

This is the foundation of modern lattice-based post-quantum cryptography.

### Computational Number Theory

Asks: what is the computational complexity of number-theoretic problems?

Key insight: **primality testing** (PRIMES) is in P. **Integer factoring** is
not known to be in P, not known to be NP-complete, and not known to be
efficiently quantum-tractable beyond Shor's algorithm. Its intermediate
status is precisely what makes RSA/DH security unclear — we rely on
empirical hardness, not a complexity separation.

---

## The Central Objects

```
THE INTEGERS Z:
  n > 1 has unique factorization:  n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ
  This FAILS in Z[√-5]:  6 = 2·3 = (1+√-5)(1-√-5)
  → drives algebraic number theory

THE RIEMANN ZETA FUNCTION:
  ζ(s) = Σ_{n≥1} n^{-s}  (Re s > 1)
       = ∏_p (1 - p^{-s})^{-1}   ← Euler product over all primes
  Extends meromorphically to C, pole at s=1, functional equation ξ(s)=ξ(1-s)
  Non-trivial zeros → prime distribution

THE EULER PHI FUNCTION φ(n):
  φ(n) = |{k : 1 ≤ k ≤ n, gcd(k,n) = 1}|
  = n · ∏_{p|n} (1 - 1/p)
  Fermat-Euler: a^{φ(n)} ≡ 1 (mod n) when gcd(a,n) = 1
  RSA correctness depends entirely on this.

DIRICHLET CHARACTERS χ:
  Completely multiplicative: χ(mn) = χ(m)χ(n)
  Periodic mod q: χ(n+q) = χ(n)
  L(s,χ) = Σ χ(n) n^{-s}  ← L-function, generalizes ζ
  Dirichlet's theorem: infinitely many primes in each {a, a+q, a+2q,...}
                        when gcd(a,q) = 1. Proved using L(1,χ) ≠ 0.
```

---

## The Major Open Problems

```
+----------------------------------------------------------------+
| PROBLEM               | STATEMENT                  | STATUS   |
+----------------------------------------------------------------+
| Riemann Hypothesis    | All nontrivial zeros of    | OPEN     |
|                       | ζ(s) have Re(s) = 1/2      | (1859–)  |
+----------------------------------------------------------------+
| Goldbach              | Every even n>2 = sum of    | OPEN     |
|                       | two primes                 | (1742–)  |
+----------------------------------------------------------------+
| Twin Prime            | Infinitely many p, p+2     | OPEN     |
|                       | both prime                 | Zhang    |
|                       |                            | 2013:    |
|                       |                            | gap<246  |
+----------------------------------------------------------------+
| Birch-Swinnerton-Dyer | L(E,1)=0 ⟺ |E(Q)|=∞        | OPEN     |
|                       | (Millennium problem)       |          |
+----------------------------------------------------------------+
| abc conjecture        | For a+b=c coprime, c has   | Claimed  |
|                       | few large prime factors    | by Mochi-|
|                       |                            | zuki     |
|                       |                            | (2012,   |
|                       |                            | disputed)|
+----------------------------------------------------------------+
| Landau problems       | Primes p²+1, Legendre,     | OPEN     |
|                       | Opperman, Brocard           |          |
+----------------------------------------------------------------+
| Integer Factoring     | Is FACTOR in P?            | OPEN     |
|                       |                            | (crypto  |
|                       |                            | security |
|                       |                            | depends  |
|                       |                            | on this) |
+----------------------------------------------------------------+
```

---

## Why This Matters to CS

```
SECURITY:
  RSA              ← IFP: factor n = pq given only n
  Diffie-Hellman   ← DLP: find x given g^x mod p
  Elliptic Curve   ← ECDLP: harder per bit than DLP for RSA
  NTRU/Kyber       ← SVP/CVP in ideal lattices (post-quantum)
  AES (GF(2^8))    ← Finite field arithmetic (irreducible poly mod 2)

RELIABILITY:
  CRC codes           ← Polynomial arithmetic over GF(2)
  Reed-Solomon        ← Polynomial eval over finite fields (used in CDs,
                         DVDs, QR codes, RAID-6, cloud storage)
  LDPC codes          ← Sparse parity-check matrices over GF(2)
  BCH codes           ← Cyclic codes over finite fields

EFFICIENCY:
  FFT              ← Roots of unity; NTT over Z/pZ (used in crypto)
  Multiplicative   ← Hash: h(k) = ⌊m·(k·A mod 1)⌋, A irrational
  hashing
  LCG PRNGs        ← x_{n+1} = ax_n + b (mod m); period = m iff
                      gcd(b,m)=1, a≡1 mod every prime factor of m,
                      a≡1 mod 4 if 4|m (Hull-Dobell)
```

---

## Complexity Landscape

```
+-----------------------------------------------------------+
| PROBLEM         | BEST CLASSICAL         | Quantum class  |
+-----------------------------------------------------------+
| PRIMES          | AKS: O(log^6 n)        | Also poly      |
| (is n prime?)   | Miller-Rabin: O(k·log³n|                |
|                 | prob., k = rounds)     |                |
+-----------------------------------------------------------+
| FACTORING       | NFS: L_n[1/3, 1.923]   | Shor: O(log³n) |
| (factor n)      | (sub-exp, super-poly)  |                |
|                 | Not NP-complete (known)|                |
+-----------------------------------------------------------+
| DLP             | Index calculus, NFS    | Shor handles   |
| (g^x ≡ a mod p) | variants: sub-exp      | DLP too        |
+-----------------------------------------------------------+
| ECDLP           | BSGS: O(√p), Pohlig-   | Shor handles   |
|                 | Hellman for smooth ord | ECDLP too      |
+-----------------------------------------------------------+
| SVP             | LLL: poly-time, 2^n    | No known       |
| (shortest vec)  | approx; exact: NP-hard | quantum speedup|
|                 | in worst case          | (post-quantum) |
+-----------------------------------------------------------+

L_n[α,c] = exp((c+o(1)) · (ln n)^α · (ln ln n)^{1-α})
  α=0: polynomial  α=1: exponential  α=1/3: NFS
```

---

## Historical Arc

```
~300 BC  Euclid — Elements: Euclidean algorithm, infinitely many primes
~250 AD  Diophantus — Arithmetica: polynomial equations over Q
1640     Fermat — a^{p-1} ≡ 1 (mod p); xⁿ+yⁿ=zⁿ stated
1736     Euler — φ(n), generalization, ζ(2)=π²/6, product formula
1796     Gauss — Disquisitiones Arithmeticae: congruences, QR, cyclotomy
1837     Dirichlet — primes in arithmetic progressions; L-functions
1859     Riemann — 8-page paper on π(x); introduces ζ(s) as complex function
1896     Hadamard + de la Vallée Poussin — PNT proved independently
1900     Hilbert — 23 problems; RH is part of #8
1920s    Artin — L-functions, reciprocity laws; class field theory
1940s    Weil — conjectures on counting points on varieties over F_q
1974     Deligne — proves Weil conjectures (Ramanujan conjecture included)
1977     Rivest-Shamir-Adleman — RSA public-key cryptosystem
1985     Koblitz + Miller — elliptic curve cryptography
1994     Wiles — Fermat's Last Theorem (modular forms + Galois repr.)
1994     Shor — quantum polynomial-time factoring algorithm
2002     AKS — PRIMES in P (deterministic polynomial time)
2013     Zhang — first bounded prime gaps (< 7×10^7, later reduced to 246)
2016     NIST post-quantum project begins — lattice crypto front-runner
```

---

## File-by-File Guide

| File | Core Content |
|------|-------------|
| 01-DIVISIBILITY-PRIMES.md | Euclidean algorithm, Bezout, UFT, infinitely many primes, prime counting |
| 02-MODULAR-ARITHMETIC.md | Z/nZ, CRT, Euler φ, Fermat/Euler theorems, Wilson |
| 03-PRIMITIVE-ROOTS.md | (Z/pZ)* cyclic, order, DLP, index arithmetic |
| 04-QUADRATIC-RECIPROCITY.md | Legendre symbol, QR theorem, Jacobi symbol |
| 05-DIOPHANTINE-EQUATIONS.md | Linear, Pell, Pythagorean triples, FLT overview |
| 06-ALGEBRAIC-NUMBER-THEORY.md | Number fields, O_K, ideal factorization, class group |
| 07-ANALYTIC-NUMBER-THEORY.md | ζ(s), Dirichlet series, PNT proof sketch, L-functions |
| 08-RIEMANN-HYPOTHESIS.md | Statement, evidence, GUE connection, consequences |
| 09-COMPUTATIONAL-NUMBER-THEORY.md | Primality tests, factoring, sieving |
| 10-CRYPTOGRAPHY-CONNECTIONS.md | RSA/DH/ECC/lattice security reductions |

---

## Decision Cheat Sheet

| Need to... | Use |
|-----------|-----|
| Compute gcd(a,b) efficiently | Euclidean algorithm |
| Solve ax ≡ b (mod n) | Extended Euclidean + CRT |
| Check if n is prime (fast, probabilistic) | Miller-Rabin |
| Check if n is prime (deterministic) | AKS (slower in practice) |
| Factor n (~50 digits) | Pollard rho |
| Factor n (~300+ digits) | Number field sieve |
| Understand RSA security | IFP, φ(n), modular inverse |
| Understand ECC security | ECDLP, group order, Hasse's theorem |
| Build post-quantum scheme | SVP/CVP in ideal lattices, module-LWE |
| Count primes ≤ x | π(x) ~ x/ln x (PNT); better: Li(x) |
| Prove primes in arithmetic progressions | Dirichlet L-functions |

---

## Common Confusion Points

**"Elementary" means it uses no analysis.**
Elementary ≠ easy. Elementary sieves (Brun's sieve, Selberg's sieve)
are extremely powerful. The "elementary" proof of PNT (Selberg-Erdős, 1948)
is harder to understand than the analytic proof.

**"Factoring is NP-hard."**
Not known. Factoring is in NP ∩ co-NP. NP-hard problems are believed NOT
to be in co-NP. Factoring's complexity class is genuinely unknown —
it could be in P, it could be strictly between P and NP-complete.

**"ζ(s) = Σ 1/nˢ diverges everywhere except Re(s)>1."**
True for the series. But ζ(s) is analytically continued to all of C \ {1}.
The "values" at Re(s) ≤ 1 (like ζ(-1) = -1/12) are values of the
continuation, not the divergent series. Ramanujan summation agrees.

**"The Euler product and the series are the same thing."**
Both equal ζ(s) for Re(s)>1. The product encodes multiplicativity of n^{-s}.
The series encodes additive structure. Their equality = unique factorization
of integers, translated to complex analysis. This is profound.

**"Class field theory is irrelevant to modern computing."**
The structure of ideal class groups in number fields is directly relevant
to the security of ideal-lattice cryptography (NTRU, Kyber, Falcon).
Understanding how far O_K is from a PID determines attack surface.
