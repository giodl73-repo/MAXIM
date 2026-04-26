# Analytic Number Theory

## The Big Picture

```
+====================================================================+
|     ANALYTIC NUMBER THEORY: COMPLEX ANALYSIS MEETS INTEGERS        |
+====================================================================+
|                                                                    |
|  GENERATING FUNCTIONS over primes and integers:                    |
|                                                                    |
|  ζ(s) = Σ n^{-s} = ∏_p (1-p^{-s})^{-1}   (Dirichlet series)     |
|                                                                    |
|  ENCODE arithmetic in analytic functions                           |
|  EXTRACT arithmetic via contour integrals (Perron's formula)       |
|  ZEROS of ζ(s) ← oscillations of π(x)                            |
|                                                                    |
|  Key results:                                                      |
|  +-----------------------+    +------------------------------+     |
|  |  Prime Number Theorem |    |  Primes in APs               |     |
|  |  π(x) ~ x / ln x     |    |  Dirichlet: ∞ primes in     |       |
|  |  Proof: ζ has no zeros|    |  {a, a+q, a+2q,...}          |     |
|  |  on Re(s)=1 line      |    |  Proof: L(1,χ) ≠ 0           |     |
|  +-----------------------+    +------------------------------+     |
|           |                              |                        |
|           v                              v                        |
|  +---------------------------------------------------+            |
|  |   GENERAL FRAMEWORK: AUTOMORPHIC L-FUNCTIONS      |            |
|  |   Langlands program (open), Weil conjectures        |          |
|  |   (proved), BSD conjecture (open)                 |            |
|  +---------------------------------------------------+            |
+====================================================================+
```

---

## Dirichlet Series

```
DEFINITION:  F(s) = Σ_{n=1}^∞ a_n · n^{-s}   (s = σ + it ∈ C)

Convergence: converges for Re(s) > σ_c (abscissa of convergence).
  If a_n is bounded: σ_c ≤ 1.
  If a_n = O(n^ε) for all ε>0: σ_c ≤ 1.

MULTIPLICATION (Dirichlet convolution):
  If F(s) = Σ f(n)n^{-s} and G(s) = Σ g(n)n^{-s}, then
  F(s)·G(s) = Σ (f*g)(n) n^{-s}   where (f*g)(n) = Σ_{d|n} f(d)g(n/d)

Examples:
  Σ 1·n^{-s} = ζ(s)
  Σ φ(n)n^{-s} = ζ(s-1)/ζ(s)
  Σ μ(n)n^{-s} = 1/ζ(s)         [Möbius function is "inverse" of 1]
  Σ Λ(n)n^{-s} = -ζ'(s)/ζ(s)   [von Mangoldt function]
  Σ d(n)n^{-s} = ζ(s)²          [d(n) = # divisors]
  Σ σ_k(n)n^{-s} = ζ(s)ζ(s-k)  [σ_k = sum of k-th powers of divisors]

KEY IDENTITY:
  Σ μ(n)n^{-s} · Σ n^{-s} = 1
  ⟺  Σ_{d|n} μ(d) = [n=1]   (Möbius inversion in sum form)
```

---

## The Riemann Zeta Function

### Definition and Euler Product

```
ζ(s) = Σ_{n=1}^∞ n^{-s}  (converges absolutely for Re(s) > 1)
     = ∏_p (1 - p^{-s})^{-1}   (Euler product, Re(s) > 1)

PROOF OF EULER PRODUCT:
  ∏_p (1-p^{-s})^{-1} = ∏_p (1 + p^{-s} + p^{-2s} + ...)
  Expanding: every positive integer n appears exactly once
  (by unique factorization), contributing n^{-s}. □

This shows: ZERO-FREE REGION for ζ(s) on Re(s)>1.
  If ζ(s₀) = 0 with Re(s₀)>1, then some factor (1-p^{-s₀})^{-1} = 0,
  i.e., p^{-s₀} = 1, i.e., 1 = p^{Re(s₀)} · p^{it₀}, impossible.
```

### Analytic Continuation

```
ζ(s) extends to a meromorphic function on all of C with:
  Simple pole at s = 1 with residue 1.
  No other poles.

FUNCTIONAL EQUATION:
  Define ξ(s) = (1/2)s(s-1)π^{-s/2}Γ(s/2)ζ(s).
  Then ξ(s) = ξ(1-s).

  Equivalently: ζ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s) ζ(1-s)

This reflects the zeros:
  "Trivial" zeros: s = -2, -4, -6, ... (from sin(πs/2) = 0)
  "Non-trivial" zeros: in the "critical strip" 0 < Re(s) < 1

Special values:
  ζ(2) = π²/6    (Euler, 1734 — "Basel problem")
  ζ(4) = π⁴/90
  ζ(2k) = (-1)^{k+1} (2π)^{2k} B_{2k} / (2·(2k)!)  for k ≥ 1
  ζ(-1) = -1/12  (value of analytic continuation, NOT the series sum)
  ζ(0) = -1/2
  ζ(1) = ∞ (pole)
  ζ(3) = "Apéry's constant" — irrational (Apéry 1978), exact form unknown
```

---

## The Prime Number Theorem

### Statement

```
PRIME NUMBER THEOREM (Hadamard + de la Vallée Poussin, 1896):

  π(x) ~ x / ln(x)  as x → ∞

where π(x) = |{p ≤ x : p prime}|.

BETTER: π(x) ~ Li(x) where Li(x) = ∫₂^x dt/ln(t) = li(x) - li(2)

  π(x) = Li(x) + O(x·exp(-c·√ln x))  (zero-free region result)
  If RH: π(x) = Li(x) + O(√x · ln x)

EQUIVALENT FORM (Chebyshev's ψ function):
  ψ(x) = Σ_{p^k ≤ x} ln(p) = Σ_{n ≤ x} Λ(n) ~ x

  PNT ⟺ ψ(x) ~ x  ⟺  ζ(1+it) ≠ 0 for all real t ≠ 0
```

### Proof Sketch (Analytic Method)

```
STEP 1: Connect ψ(x) to ζ via Perron's formula.
  -ζ'(s)/ζ(s) = Σ Λ(n) n^{-s}

  Perron's formula: ψ(x) = (1/2πi) ∫_{c-i∞}^{c+i∞} (-ζ'(s)/ζ(s)) · x^s/s · ds
  (c > 1 — converges absolutely)

STEP 2: Move contour left to Re(s) = 1 - ε.
  Pick up residues from:
  - s=1 (simple pole of ζ): residue = x (from -ζ'/ζ ~ 1/(s-1), x^s/s|_{s=1} = x)
  - s=ρ (zeros of ζ): each gives -x^ρ/ρ
  - s=0 and trivial zeros: contribute lower-order terms

STEP 3: KEY LEMMA: ζ(1+it) ≠ 0 for all real t ≠ 0.
  Proof: Use the trigonometric identity 3+4cos θ+cos 2θ ≥ 0 and
  ζ(σ)³|ζ(σ+it)|⁴|ζ(σ+2it)| ≥ 1 (from Euler product).
  As σ → 1⁺, ζ(σ)³ ~ (σ-1)^{-3} → 0.
  This forces |ζ(σ+it)|⁴ to blow up if ζ(1+it)=0, contradicting boundedness.

STEP 4: Zero-free region gives ψ(x) = x - Σ_{ρ} x^ρ/ρ + small error.
  The sum over zeros is small because zeros are away from Re(s)=1 line.
  ψ(x) → x → PNT. □
```

---

## Dirichlet L-Functions and Primes in APs

```
DIRICHLET CHARACTER χ mod q:
  Completely multiplicative: χ(mn) = χ(m)χ(n)
  Periodic: χ(n+q) = χ(n)
  χ(n) = 0 if gcd(n,q) > 1
  Orthogonality: Σ_{n mod q} χ(n)χ̄(n') = {φ(q) if χ=χ'; 0 otherwise}

Principal character χ₀: χ₀(n) = 1 if gcd(n,q)=1, 0 otherwise.
  L(s, χ₀) = ζ(s) · ∏_{p|q} (1 - p^{-s})

DIRICHLET L-FUNCTIONS:
  L(s, χ) = Σ_{n=1}^∞ χ(n) n^{-s} = ∏_p (1 - χ(p)p^{-s})^{-1}  (Re s > 1)

DIRICHLET'S THEOREM:
  If gcd(a,q) = 1, then Σ_{p≡a(mod q)} 1/p = +∞.
  Moreover: π(x; q, a) ~ (1/φ(q)) · x/ln x  (equal distribution)

KEY STEP: Prove L(1, χ) ≠ 0 for χ ≠ χ₀.
  This is analogous to ζ(1+it) ≠ 0.
  For real χ: L(1,χ) > 0 by positivity argument (most subtle case).
  For complex χ: follows from ζ(1+it) ≠ 0 applied to the "conductor" of χ.

SUMS over primes in AP via character orthogonality:
  Σ_{p≡a(mod q)} n^{-s} = (1/φ(q)) Σ_{χ mod q} χ̄(a) · (-L'/L)(s,χ)

The sum over characters picks out the residue class a.
```

---

## Analytic Sieves

```
SIEVE METHODS: Estimate the count of numbers with no small prime factors.

Let A = set of integers in [1,x], P = set of sieving primes.
S(A, P, z) = |{n ∈ A : gcd(n, ∏_{p∈P,p≤z} p) = 1}|

INCLUSION-EXCLUSION:
  S(A,P,z) = Σ_{d|P(z)} μ(d) |A_d|  where A_d = {n ∈ A : d|n}

PROBLEM: 2^{π(z)} terms — exponential.

BRUN'S SIEVE (1919): Truncate at small d. Gives UPPER and LOWER bounds.
  Brun's theorem: Σ_{p: p,p+2 prime} (1/p + 1/(p+2)) < ∞  (Brun's constant ≈ 1.902)

SELBERG'S SIEVE (1947): Optimize λ_d weights for upper bound.
  S(A,P,z) ≤ x/ln²z + O(...)  → improved error terms.

LARGE SIEVE INEQUALITY:
  |Σ_{n≤N} a_n e^{2πinα_j}|² ≤ (N + Q²) Σ|a_n|²  for well-spaced α_j.
  Extends to Dirichlet characters, gives Bombieri-Vinogradov theorem.

BOMBIERI-VINOGRADOV THEOREM:
  Σ_{q≤Q} max_{a,gcd(a,q)=1} |π(x;q,a) - Li(x)/φ(q)| ≪ x/(ln x)^A
  for any A>0, Q ≤ √x/(ln x)^B.
  "GRH on average" — as powerful as assuming the Generalized RH.
```

---

## The Explicit Formula

```
RIEMANN'S EXPLICIT FORMULA (1859):
  ψ(x) = x - Σ_ρ x^ρ/ρ - ln(2π) - (1/2)ln(1-x^{-2})

where ρ ranges over NON-TRIVIAL ZEROS of ζ(s).

This is exact (not asymptotic)! Every zero contributes an oscillation.

VISUALIZATION:
  ψ(x) = x [main term] + Σ_ρ x^ρ/ρ [oscillations from zeros]
                                      ↑
                       each zero ρ = 1/2 + it contributes
                       an oscillation with frequency t and
                       amplitude x^{1/2}/|ρ| (if RH holds)

CONSEQUENCE OF RH:
  All ρ have Re(ρ) = 1/2, so x^ρ = x^{1/2} · e^{it ln x}.
  Oscillations have size O(√x), giving |ψ(x) - x| = O(√x log²x).
  If RH fails, some ρ has Re(ρ) > 1/2, giving larger oscillations.
```

---

## Beyond the Riemann Zeta Function

```
DEDEKIND ZETA FUNCTION:
  ζ_K(s) = Σ_{I⊆O_K, I≠0} N(I)^{-s} = ∏_{p prime ideal} (1-N(p)^{-s})^{-1}
  Extends ζ to number fields. Encodes ideal structure.

CLASS NUMBER FORMULA:
  lim_{s→1} (s-1)ζ_K(s) = 2^{r₁}(2π)^{r₂}·h_K·R_K / (w_K · √|Δ_K|)
  where h_K = class number, R_K = regulator (volume of unit lattice),
  w_K = # roots of unity, r₁,r₂ = embedding counts.

HECKE L-FUNCTIONS:
  Generalize Dirichlet L-functions to number fields.
  L(s, ψ) for Hecke characters ψ on K.

ARTIN L-FUNCTIONS:
  For a Galois extension L/K and representation ρ: Gal(L/K) → GL_n(C):
  L(s, ρ) = ∏_p det(I - ρ(Frob_p)N(p)^{-s})^{-1}
  Artin's conjecture: non-trivial Artin L-functions are entire.
  Known for abelian representations; open for non-abelian.

AUTOMORPHIC L-FUNCTIONS (Langlands):
  All L-functions = automorphic L-functions.
  Includes: elliptic curve L-functions, modular form L-functions, Artin L-functions.
  FLT proof used this: modularity theorem = elliptic curve L-functions are automorphic.
```

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Count primes ≤ x precisely | ψ(x) and explicit formula; Li(x) approximation |
| Understand why PNT uses complex analysis | ζ zeros control ψ(x) oscillations |
| Prove primes in AP {a+nq} | Dirichlet L-functions, L(1,χ) ≠ 0 |
| Understand sieve methods | Brun/Selberg: inclusion-exclusion + truncation |
| Connect ζ values to number theory | Class number formula, special values |
| Understand RH consequences | Error term in PNT becomes O(√x log² x) |
| Understand the Langlands program | Unification of all L-functions |

---

## Common Confusion Points

**"ζ(s) = Σ 1/nˢ has nothing to do with primes."**
The Euler product shows exactly the connection: unique factorization in Z
becomes the product formula ζ(s) = ∏_p (1-p^{-s})^{-1}. The zeros of ζ
control the error in prime counting via the explicit formula.

**"Analytic continuation of ζ gives ζ(-1) = -1/12, so 1+2+3+... = -1/12."**
The series 1+2+3+... diverges. ζ(-1) = -1/12 is the VALUE of the analytic
continuation at s=-1. This is NOT the sum of the series. Ramanujan summation
assigns this value via a different regularization, which agrees. But treating
it as a literal sum of positive integers is wrong.

**"Dirichlet characters are just functions on Z/qZ."**
They're multiplicative characters on (Z/qZ)*, extended to Z by periodicity
and 0 on numbers sharing a factor with q. The orthogonality relations and
the ability to build L-functions from them are the key structural properties.

**"The Bombieri-Vinogradov theorem proves GRH."**
It proves a statement that is AS STRONG as GRH for applications to sieve
methods, averaged over q ≤ √x. But GRH is a statement about individual
characters and all t, not just an average.
