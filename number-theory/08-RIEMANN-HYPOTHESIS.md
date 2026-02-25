# The Riemann Hypothesis

## The Big Picture

```
+====================================================================+
|              THE RIEMANN HYPOTHESIS (1859–)                        |
+====================================================================+
|                                                                    |
|  STATEMENT: All non-trivial zeros of ζ(s) lie on Re(s) = 1/2.    |
|                                                                    |
|  The critical strip:    0 < Re(s) < 1                             |
|                                                                    |
|        σ=0      σ=1/2 (critical line)      σ=1                   |
|         |           |                        |                    |
|         |    zeros? |  ← RH says all zeros   |                   |
|         |    here   |     are on this line   |                    |
|         |      ·    |                        |                    |
|         |      ·    |   14.134...i           |                    |
|         |      ·    |   21.022...i           |                    |
|         |      ·    |   25.010...i           |                    |
|         |      ·    |   30.424...i           |                    |
|         |      ·    |   32.935...i           |                    |
|         |           |   (all known zeros)    |                    |
|         |           |                        |                    |
|  Trivial zeros: -2, -4, -6, ... (off to left, real axis)         |
+====================================================================+
```

---

## Precise Statement

```
ζ(s) — the Riemann zeta function — is defined by:
  ζ(s) = Σ_{n=1}^∞ n^{-s}  for Re(s) > 1
  Extended by analytic continuation to all s ≠ 1.

ZEROS:
  Trivial zeros: s = -2, -4, -6, ...  [from the functional equation]
  Non-trivial zeros: s = σ + it with 0 ≤ σ ≤ 1 (known region)

RIEMANN HYPOTHESIS:
  Every non-trivial zero s = σ + it satisfies σ = 1/2.
  Equivalently: all non-trivial zeros lie on the line {1/2 + it : t ∈ R}.

Known (unconditionally):
  All non-trivial zeros satisfy 0 < Re(s) < 1  (proven by Hadamard)
  ζ(s) ≠ 0 on Re(s) = 1 (proven by Hadamard and de la Vallée Poussin — used to prove PNT)
  ζ(1/2 + it) = 0 for the first zero at t ≈ 14.134725...

Numerical verification:
  First 10^13 zeros all on critical line (Gourdon 2004 and subsequent computations).
  More than 10^{22} zeros verified (as of recent computations).
```

---

## Why It Matters — Consequences of RH

### For Prime Distribution

```
EXPLICIT FORMULA (Riemann, 1859):
  ψ(x) = Σ_{n≤x} Λ(n) = x - Σ_ρ x^ρ/ρ - ln(2π) + small

where ρ ranges over non-trivial zeros.

IF RH (all ρ = 1/2 + it):
  Each x^ρ = x^{1/2+it} = x^{1/2} · e^{it ln x}
  Amplitude: |x^ρ/ρ| = x^{1/2}/|ρ|

  Error bound: |ψ(x) - x| ≤ (1/8π) x^{1/2} (ln x)²  for x ≥ 2.657
  → |π(x) - Li(x)| < (1/8π) √x · ln x  for x ≥ 2.657

IF RH FAILS (some ρ = σ₀ + it with σ₀ > 1/2):
  That zero contributes x^{σ₀+it}/ρ — amplitude x^{σ₀} >> √x.
  Prime counting error is much larger, oscillations are larger.
```

### For Mathematics

```
CONDITIONAL ON RH (partial list):

PRIME GAPS:
  p_{n+1} - p_n = O(√p_n · ln p_n) — tight bound on gap size.
  Unconditionally: O(p_n^{21/40}) (Huxley's result).

PRIMALITY TESTING:
  Extended Riemann Hypothesis (ERH) for L(s,χ) zeros:
  Miller-Rabin is DETERMINISTIC if ERH holds: test all bases a ≤ 2(ln n)².
  Without ERH: Miller-Rabin is probabilistic.

ARTIN'S CONJECTURE:
  Every non-square a ≠ -1 is a primitive root for infinitely many primes.
  Proved conditionally on GRH (Hooley 1967).

GOLDBACH-TYPE RESULTS:
  Under GRH: every odd n > 5 is a sum of three primes (proved conditionally,
  unconditionally proved by Vinogradov for n sufficiently large ~10^{30000}).

EXPLICIT BOUNDS everywhere:
  Hundreds of theorems have tighter (effective) forms under RH.
  Without RH: same theorem exists but with unspecified constants or worse bounds.
```

---

## Numerical Evidence

### Zero Computation

```
FIRST 40 ZEROS (imaginary parts of 1/2 + it_n):
  t₁  = 14.134725...
  t₂  = 21.022039...
  t₃  = 25.010857...
  t₄  = 30.424876...
  t₅  = 32.935061...
  t₆  = 37.586178...
  t₇  = 40.918719...
  t₈  = 43.327073...
  t₉  = 48.005150...
  t₁₀ = 49.773832...

All computed zeros to date: on the critical line.
Gram's law (rough rule): consecutive zeros interlace with the zeros of
  Re(ζ(1/2+it)) and Im(ζ(1/2+it)) — holds for most t, fails "Gram blocks."
```

### Statistical Evidence: GUE Hypothesis

```
RANDOM MATRIX THEORY CONNECTION (Montgomery-Dyson, 1972):

Hugh Montgomery computed the PAIR CORRELATION of zeros:
  R₂(α) = Σ_{ρ≠ρ'} δ(γ-γ') (distribution of distances between zeros)
  Result: behaves like the distribution of eigenvalue spacings of
  random Hermitian matrices from the GUE (Gaussian Unitary Ensemble).

Specifically: the pair correlation function is
  R₂(x) = 1 - (sin(πx)/πx)²

This is IDENTICAL to the eigenvalue spacing of random Hermitian matrices.

Freeman Dyson (physicist) recognized this as GUE immediately when
Montgomery mentioned it at a tea party at the IAS (1972).

IMPLICATION:
  Zeros of ζ behave like energy levels of a chaotic quantum system.
  Primes are somehow "quantized."
  The operator whose eigenvalues are zero imaginary parts is sometimes
  called the "Hilbert-Pólya operator" — it hasn't been found, but:
  if it exists as a self-adjoint operator on a Hilbert space, RH follows.
```

### Statistical Counts

```
π(x) vs. Li(x) error:
  x = 10^6:   |π(x) - Li(x)| = |78498 - 78627.5| ≈ 129
  x = 10^9:   |π(x) - Li(x)| ≈ 1700
  x = 10^12:  |π(x) - Li(x)| ≈ 38000
  x = 10^22:  |π(x) - Li(x)| < 10^11

Error grows much slower than x^{1/2+ε} — consistent with RH.

SKEWES' NUMBER: The first x where Li(x) < π(x).
  Skewes (1933): < 10^{10^{10^{34}}} assuming RH.
  Lehman (1966): < 10^{1167} unconditionally.
  Current best: first crossover near x ≈ e^{727.952...} ≈ 1.397×10^{316}.
  Actual crossover has not been reached computationally.
```

---

## The Critical Strip Structure

```
SYMMETRIES:
  Functional equation: ξ(s) = ξ(1-s) → zeros symmetric about Re(s)=1/2
  Complex conjugation: ζ(s̄) = ζ̄(s) → zeros symmetric about Re(s)=0 line
  Combined: zeros come in quadruples {ρ, 1-ρ, ρ̄, 1-ρ̄}
  On critical line: ρ and ρ̄ (same real part = 1/2)

THE CRITICAL LINE THEOREM (Hardy, 1914):
  Infinitely many zeros lie on Re(s) = 1/2.
  [Does not say ALL zeros are there — just infinitely many]

SELBERG'S THEOREM (1942):
  A positive proportion of all zeros lie on Re(s) = 1/2.
  At least 1/3 (later improved to 40.7% by Conrey, 1989).

KNOWN:
  All zeros with |Im(s)| < T satisfy Re(s) = 1/2 for T ≤ T₀ (T₀ ~ 10^{22}).
  This is verified numerically, not proved.
```

---

## Equivalent Formulations

```
RH is equivalent to each of these:

1. (von Koch, 1901):
   |π(x) - Li(x)| = O(√x · ln x)

2. (Schoenfeld, 1976):
   |π(x) - Li(x)| < (1/8π)√x·ln x  for all x ≥ 2657.

3. Robin's criterion (1984):
   σ(n) < eᵞ · n · ln(ln(n))  for all n > 5040
   (where σ(n) = sum of divisors, γ = Euler-Mascheroni constant ≈ 0.5772...)

4. Lagarias's criterion (2002):
   σ(n) ≤ Hₙ + eᴴⁿ · ln(Hₙ)  for all n ≥ 1
   (where Hₙ = 1+1/2+...+1/n is the n-th harmonic number)

5. Li's criterion (1997):
   RH ⟺ all Li coefficients λₙ = 1/(n-1)! dⁿ/dsⁿ[sⁿ⁻¹ ln ξ(s)]|_{s=1} are positive.

6. Weil's explicit formula positivity:
   A certain distribution related to zeros is positive semi-definite.
```

---

## Connections to Other Areas

### Quantum Chaos

```
The Hilbert-Pólya conjecture (1910s):
  There exists a self-adjoint operator H on a Hilbert space
  whose eigenvalues are {t_n : 1/2 + it_n is a zero of ζ}.
  Self-adjoint → real eigenvalues → RH would follow.

Berry-Keating Hamiltonian (1999):
  H = xp (position × momentum in 1D)
  In quantum mechanics: H = -(ih)(x·d/dx + d/dx·x)/2
  Spectrum related to zeros, but no satisfactory model exists.

Odlyzko-Schönhage algorithm: compute millions of zeros precisely.
Comparison with GUE eigenvalue statistics: near-perfect match.
This is the most compelling numerical evidence for RH.
```

### Zeros and Primes — Visualization

```
ψ(x) = x - Σ_ρ x^ρ/ρ - log(2π) + ...

If RH: x^ρ = √x · e^{it log x} — oscillations of fixed amplitude √x.

FOURIER ANALOGY:
  The "spectrum" of ψ(x) (think: Fourier transform in log x) reveals
  peaks at the imaginary parts of zeros {t_n}.
  Each zero contributes a frequency t_n to the oscillations of π(x).
  Primes create "music" whose notes are the zero imaginary parts.

This is Riemann's original insight: primes and ζ zeros are Fourier duals
of each other. The prime distribution is "smooth" iff zeros are on the
critical line (oscillations all have the same amplitude).
```

---

## Why RH is Hard

```
APPROACHES THAT HAVE BEEN TRIED:

Algebraic/geometric:
  Weil proved the analogue of RH for curves over finite fields (1948, Riemann Hypothesis
  for function fields). Deligne proved it for varieties (1974 — Weil conjectures).
  The method: geometric, uses the Frobenius endomorphism and étale cohomology.
  Analog for the classical ζ: the "geometric" structure is missing.

Spectral:
  Find H with ζ zeros as eigenvalues. Not constructed yet.
  Some partial models (Connes's noncommutative geometry framework, 1999).

Probabilistic:
  GUE statistics match — but statistics don't prove individual values.

Elementary:
  Many claimed elementary proofs have all had flaws.
  The structure of ζ near Re(s)=1 requires subtle complex analysis.

Status: OPEN. Probably the deepest open problem in mathematics.
  Clay Mathematics Institute: $1,000,000 prize.
  Part of Hilbert's 8th problem (1900).
```

---

## Generalized Riemann Hypothesis

```
GRH extends RH to all Dirichlet L-functions:

For every Dirichlet character χ, all non-trivial zeros of L(s,χ)
have real part exactly 1/2.

Consequences of GRH:
  Primes in AP: |π(x;q,a) - x/φ(q)/ln x| = O(√x log x / φ(q))
  Deterministic Miller-Rabin: primality testing for n by testing a ≤ 2(ln n)²
  Artin's conjecture on primitive roots
  Tight distribution results for primes in short intervals

GRAND RIEMANN HYPOTHESIS (GRH extended):
  All zeros of automorphic L-functions (Langlands) on Re(s) = 1/2.
  This includes: Dedekind zeta, Hecke L-functions, elliptic curve L-functions.
```

---

## Decision Cheat Sheet

| If you want to... | RH says... |
|------------------|-----------|
| Bound π(x) error tightly | |π(x)-Li(x)| < (1/8π)√x·ln x |
| Make Miller-Rabin deterministic | Test bases a ≤ 2(ln n)² under ERH |
| Understand prime gaps | p_{n+1}-p_n = O(√p_n log p_n) |
| Use Robin's criterion | σ(n) < eᵞ·n·ln(ln n) for n>5040 |
| Understand GUE connection | Zero spacings = random Hermitian eigenvalue spacings |
| Know what's been verified | All zeros with |Im| < T₀ ~ 10²² are on critical line |

---

## Common Confusion Points

**"RH has been proved / disproved multiple times."**
Many flawed proofs have circulated. None have survived peer review.
The Clay Institute requires publication in a major refereed journal and
two years of community review. No submission has passed this bar.

**"ζ(-1) = -1/12 means RH is false because -1 ≠ 1/2."**
s = -1 is a trivial zero location: ζ(-1) = -1/12 ≠ 0. The trivial zeros are
at s = -2, -4, -6, ..., not s = -1. RH is a statement about the non-trivial zeros.

**"Weil's proof for function fields proves RH."**
Weil proved RH for zeta functions of algebraic curves over FINITE fields.
The analogous proof for ζ(s) over Q doesn't directly apply — the "geometry"
of the classical case is missing. This is the main reason RH is hard.

**"10^{22} zeros on the line proves RH."**
It doesn't. There could be a zero off the critical line with very large
imaginary part. Numerical verification provides strong evidence, not proof.
The Riemann-Siegel formula allows efficient computation of zeros, but
not all zeros in an unbounded region.
