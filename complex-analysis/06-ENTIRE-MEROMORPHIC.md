# Entire and Meromorphic Functions

## The Big Picture

Entire functions (holomorphic on all of ℂ) have no singularities in the finite plane — they can only grow toward infinity. Meromorphic functions allow poles. The theory of entire functions describes how they can grow and how their zeros are distributed. The key insight is that you can *prescribe* the zeros of an entire function (within constraints) and build the function from its zero set via infinite products. The Hadamard factorization theorem does this for functions of finite order, making it the entire-function analogue of partial-fraction decomposition for rational functions.

```
ENTIRE AND MEROMORPHIC FUNCTIONS — MAP
═══════════════════════════════════════════════════════════════════════════════

  ENTIRE (no singularities anywhere in ℂ):
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Polynomials    Growth: |f(z)| ~ |z|ⁿ         Zeros: finite          │
  │  e^z, sin z    Growth: exponential              Zeros: discrete      │
  │  e^{e^z}       Growth: superexponential         Zeros: none?         │
  └──────────────────────────────────────────────────────────────────────┘

  GROWTH RATE — ORDER ρ:
  ρ = limsup_{r→∞}  log log M(r) / log r     M(r) = max_{|z|=r} |f(z)|

  ┌──────────────┬──────────────┬────────────────────────────────────────┐
  │  Function    │  Order ρ     │  Notes                                 │
  ├──────────────┼──────────────┼────────────────────────────────────────┤
  │  Polynomial  │  0           │  Hadamard: finitely many zeros         │
  │  e^z         │  1           │  No zeros                              │
  │  sin z       │  1           │  Zeros at nπ                           │
  │  e^{z²}      │  2           │  No zeros                              │
  │  e^{e^z}     │  ∞           │  Not of finite order                   │
  └──────────────┴──────────────┴────────────────────────────────────────┘

  MEROMORPHIC (entire except isolated poles):
  Every meromorphic function on ℂ ∪ {∞} is a rational function.
  On ℂ: quotient of two entire functions f = g/h
```

---

## Order and Type of Entire Functions

**Order ρ** measures how fast an entire function grows:

    M(r) = max_{|z|=r} |f(z)|    (maximum modulus on circle of radius r)

    ρ = limsup_{r→∞} log log M(r) / log r

Equivalently: f has order ρ if for every ε > 0:
    M(r) ≤ e^{r^{ρ+ε}} for large r, but M(r) > e^{r^{ρ−ε}} infinitely often.

**Type τ** (for fixed finite order ρ):

    τ = limsup_{r→∞} log M(r) / rρ

For f = e^z: ρ = 1, τ = 1. For f = e^{az}: ρ = 1, τ = |a|. For f = e^{z²}: ρ = 2, τ = 1.

**Examples of orders**:

| Function | Order ρ | Type τ |
|---------|---------|--------|
| Polynomial of degree n | 0 | 0 |
| e^{az} | 1 | |a| |
| sin(az) | 1 | |a| |
| cos(az) | 1 | |a| |
| e^{z²} | 2 | 1 |
| e^{z^n} | n | 1 |
| Σ z^n/n^n | 0 | 0 |
| e^{e^z} | ∞ | — |

---

## Weierstrass Factorization Theorem

**Problem**: Given a sequence {aₙ} of complex numbers with |aₙ| → ∞, construct an entire function with zeros exactly at the aₙ (with prescribed multiplicities).

**Naive attempt**: ∏ₙ (1 − z/aₙ) may not converge.

**Solution**: Introduce convergence factors (Weierstrass elementary factors):

    E(z, p) = (1 − z) · e^{z + z²/2 + ... + z^p/p}

This is a polynomial times an exponential chosen so that |1 − E(z/a, p)| ≤ |z/a|^{p+1} for |z| ≤ |a|.

**Weierstrass Theorem**: For any sequence {aₙ} → ∞, there exist integers pₙ ≥ 0 such that

    f(z) = z^m · ∏ₙ E(z/aₙ, pₙ)

is an entire function with zeros exactly at 0 (multiplicity m) and aₙ (each of specified multiplicity). The product converges absolutely and uniformly on compact sets.

The pₙ can always be chosen to equal n (though often smaller values work):

    ∏ₙ E(z/aₙ, n)  always converges if  Σ (|z|/|aₙ|)^{n+1}  converges.

---

## Hadamard Factorization Theorem

For entire functions of **finite order**, Weierstrass factorization takes a cleaner form:

**Hadamard's Theorem**: Let f be entire of finite order ρ ≥ 0. Write:
- m = order of zero at 0 (m = 0 if f(0) ≠ 0)
- a₁, a₂, ... = non-zero zeros (with multiplicity)
- p = integer ≥ ρ − 1 (the genus)

Then:
    f(z) = z^m · e^{g(z)} · ∏ₙ E(z/aₙ, p)

where g(z) is a polynomial of degree ≤ ρ.

```
HADAMARD FACTORIZATION STRUCTURE:
  f(z) = [power of z] × [exponential of polynomial] × [Weierstrass product over zeros]
          ─────────────   ─────────────────────────    ─────────────────────────────────
          zero at origin   "background growth"          zeros at aₙ
```

**Specialization to order 1**: For f entire of order ≤ 1:

    f(z) = z^m · e^{az+b} · ∏ₙ (1 − z/aₙ) e^{z/aₙ}

where a, b are constants and the product converges because Σ 1/|aₙ| < ∞ (for order < 1) or Σ 1/|aₙ|² < ∞ (for order ≤ 1).

---

## Classic Examples

### Sine Function

    sin(πz) = πz · ∏_{n=1}^{∞} (1 − z²/n²)

Zeros at n ∈ ℤ, order 1. This follows from Hadamard with genus p=1.

Rearranging:
    sin(πz) / (πz) = ∏_{n=1}^{∞} (1 − z²/n²)

Setting z = 1/2 gives Wallis's formula: π/2 = ∏ₙ (4n²)/(4n²−1).
Comparing coefficients gives the Basel problem: Σ 1/n² = π²/6.

### Gamma Function

The **Gamma function** is meromorphic (not entire), with poles at 0, −1, −2, ...:

    1/Γ(z) = z · e^{γz} · ∏_{n=1}^{∞} (1 + z/n)e^{-z/n}

(Weierstrass product for 1/Γ — note 1/Γ is entire with zeros at poles of Γ)

Here γ = Euler-Mascheroni constant = lim_{n→∞} (1 + 1/2 + ... + 1/n − ln n) ≈ 0.5772.

The Gamma function satisfies:
    Γ(n+1) = n!    (extends factorial)
    Γ(z+1) = z·Γ(z)    (functional equation)
    Γ(z)Γ(1−z) = π/sin(πz)    (reflection formula)

---

## Jensen's Formula

**Jensen's Formula** relates the zeros of an analytic function inside a disk to its values on the boundary:

For f holomorphic on {|z| ≤ r}, f(0) ≠ 0, zeros z₁, ..., zₙ inside {|z| < r} (counted with multiplicity):

    log|f(0)| = −Σₖ log(r/|zₖ|) + (1/2π) ∫_0^{2π} log|f(re^{iθ})| dθ

Rearranged:
    (1/2π) ∫_0^{2π} log|f(re^{iθ})| dθ − log|f(0)| = Σₖ log(r/|zₖ|) ≥ 0

**Meaning**: The logarithmic mean of |f| on a circle exceeds log|f(0)|, with equality iff f has no zeros inside. Each zero contributes positively to the excess.

**Application**: Jensen's formula is the key tool in understanding the distribution of zeros: it relates N(r) (number of zeros in |z| ≤ r) to the growth of M(r).

---

**Nevanlinna theory** quantifies what Picard states qualitatively. Where Picard says "f takes every value except possibly one," Nevanlinna's first and second main theorems measure *how often*: the counting function N(r, a) (number of times f = a in |z| < r) and the proximity function m(r, a) combine into the Nevanlinna characteristic T(r) = N(r, a) + m(r, a), which is independent of a up to O(1). The Second Main Theorem bounds the "deficiency" δ(a) = 1 − limsup N(r,a)/T(r) by Σ δ(aⱼ) ≤ 2 — at most two values can be taken less often than average (the Picard exceptional values). This theory underlies modern complex dynamics: the Julia set of a rational map R: ℙ¹ → ℙ¹ is the set where iterates Rⁿ are not equicontinuous, and Nevanlinna theory controls the distribution of preimages.

---

## Picard's Theorems

**Little Picard**: If f is entire and not a polynomial, it takes every complex value except possibly one.

More precisely: A non-constant entire function takes every value in ℂ with at most one exception. e^z is the canonical example: it omits 0, takes every other value.

**Great Picard**: Near an essential singularity, f takes every complex value (with at most one exception) infinitely many times.

These are remarkable rigidity results. In the neighborhood of an essential singularity, the function is "dense in all of ℂ."

```
HIERARCHY:
  f has a removable singularity at a   →  f extends holomorphically, bounded near a
  f has a pole of order n at a         →  |f(z)| → ∞ as z→a
  f has an essential singularity at a  →  Picard: f dense near a  (Casorati-Weierstrass)
```

**Casorati-Weierstrass (weaker than Picard)**: If f has an essential singularity at a, then for any r > 0 and any w ∈ ℂ, there exist z with |z−a| < r and |f(z)−w| < ε. In other words, f is dense in ℂ near an essential singularity.

---

## Meromorphic Functions

A **meromorphic function** on a domain Ω is holomorphic on Ω except at a set of isolated poles.

**Quotient structure**: f is meromorphic on Ω iff f = g/h where g, h are holomorphic on Ω with h not identically zero.

**Meromorphic on ℂ ∪ {∞} = rational**: A function meromorphic on the entire Riemann sphere is a rational function R(z) = p(z)/q(z).

**Partial fractions (meromorphic case)**: A meromorphic function with poles at a₁, ..., aₙ (of orders m₁, ..., mₙ) can be written:

    f(z) = polynomial + Σⱼ Σ_{k=1}^{mⱼ} cⱼₖ/(z − aⱼ)^k

This is the meromorphic analogue of partial-fraction decomposition for rational functions.

---

## Infinite Products

Convergence of infinite products ∏ₙ (1 + aₙ) is closely related to convergence of Σ aₙ:

    ∏ₙ (1 + aₙ) converges absolutely ↔ Σ |aₙ| < ∞

For holomorphic functions: ∏ₙ fₙ(z) converges uniformly on compact sets if Σ |fₙ(z) − 1| converges uniformly on compact sets.

**Connection to the zeta function**: Euler's product formula

    ζ(s) = ∏_{p prime} (1 − p^{−s})^{−1}

is an infinite product over primes, converging for Re(s) > 1. It factors ζ as a "Weierstrass-like product" over prime-indexed factors, encoding the fundamental theorem of arithmetic in analytic form.

---

**From Hadamard product to prime distribution.** The Hadamard factorization of ξ(s) is not merely a structural result — it is the engine of the explicit formula for primes. Taking logarithmic derivatives of the product gives −ζ'/ζ(s) = ... + Σ_ρ [1/(s−ρ) + 1/ρ] + ..., where the sum runs over non-trivial zeros. Feeding this into Perron's formula (contour integration, see 07-ANALYTIC-CONTINUATION.md) yields the von Mangoldt explicit formula: ψ(x) = x − Σ_ρ x^ρ/ρ − log(2π) − (1/2)log(1 − x^{−2}). Each zero ρ contributes an oscillatory correction x^ρ/ρ to the prime counting function. The PNT follows because the zero-free region forces Re(ρ) < 1, making the sum o(x). RH (all Re(ρ) = 1/2) would give the optimal error O(√x log x).

---

## The Riemann Zeta Function Preview

The Hadamard factorization of ξ(s) = (1/2)s(s−1)π^{−s/2}Γ(s/2)ζ(s) (the completed zeta function, which is entire of order 1):

    ξ(s) = ξ(0) · ∏_{ρ} (1 − s/ρ) e^{s/ρ}

where the product is over the non-trivial zeros ρ of ζ(s).

**Riemann Hypothesis**: All non-trivial zeros lie on Re(s) = 1/2. In terms of Hadamard factorization: the "Weierstrass product" for ξ has all its zeros on the critical line.

From Jensen's formula: the number N(T) of zeros with 0 < Im(ρ) < T satisfies

    N(T) = (T/2π) log(T/2πe) + O(log T)    (Riemann-von Mangoldt formula)

So zeros become more densely spaced at height T, with average gap 2π/log T.

---

## Decision Cheat Sheet

| Need to... | Tool |
|-----------|------|
| Construct entire function with prescribed zeros | Weierstrass factorization |
| Factor entire function of finite order | Hadamard factorization |
| Count zeros of f in |z| ≤ r | Jensen's formula, argument principle |
| Show f takes every value | Picard's theorem (if f is entire, non-polynomial) |
| Determine growth rate of entire f | Compute order ρ = limsup log log M(r) / log r |
| Express meromorphic f in partial fractions | Decompose into poles + polynomial part |
| Derive Basel sum Σ 1/n² | Compare coefficients in Weierstrass product for sin |

---

## Common Confusion Points

**Weierstrass theorem is non-constructive for the pₙ**: The theorem guarantees the product converges for some choice of pₙ, but finding the minimal choice requires more work. For functions of finite order ρ, Hadamard gives a specific choice: pₙ = ⌊ρ⌋.

**An entire function of order 0 is not necessarily a polynomial**: Order 0 means log M(r)/r^ε → 0 for all ε > 0. The function f(z) = Σ z^n/(n!) = e^z has order 1, not 0. But Σ z^n/n^n grows slower than any exponential — order 0 — yet it is a non-polynomial entire function.

**Picard's theorem does not say f takes every value with bounded multiplicity**: In fact, near an essential singularity (or for a transcendental entire function by Great Picard), the function typically takes each non-exceptional value *infinitely often* in every neighborhood. There is no bound.

**Meromorphic ≠ rational**: On ℂ, there are meromorphic functions that are not rational (e.g., tan z = sin z/cos z — not a rational function). On the Riemann sphere ℂ ∪ {∞}, every meromorphic function IS rational.

**Jensen's formula requires f(0) ≠ 0**: If f has a zero of order m at 0, write f(z) = z^m g(z) with g(0) ≠ 0, and apply Jensen to g. The formula for f then picks up −m log r from the z^m factor.
