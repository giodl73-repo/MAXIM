# Residues, Poles, and Laurent Series

## The Big Picture

The residue theorem is the master tool of complex integration. It reduces contour integrals — and by extension, many difficult real integrals — to the algebraic task of computing residues at isolated singularities. Laurent series are the mechanism: they extend Taylor series to handle singularities, and the residue is simply the coefficient of 1/(z − a) in the Laurent expansion.

```
RESIDUE THEOREM — CENTRAL RESULT
═══════════════════════════════════════════════════════════════════════════════

  f meromorphic in Ω (holomorphic except at isolated singularities a₁,...,aₙ)
  C a simple closed CCW curve in Ω not passing through any aₖ

  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │   ∮_C f(z) dz = 2πi × Σ_{aₖ inside C} Res(f, aₖ)                    │
  │                                                                     │
  │   where  Res(f, a) = coefficient of (z−a)^{-1} in Laurent series    │
  │           of f at a                                                 │
  └─────────────────────────────────────────────────────────────────────┘

  SINGULARITY TAXONOMY:
  ┌──────────────┬───────────────────────────────────────────────────────┐
  │ Type         │ Laurent series at a                  │ Residue        │
  ├──────────────┼──────────────────────────────────────┼────────────────┤
  │ Removable    │ no negative powers                   │ 0              │
  │ Pole order n │ finite negative powers (down to      │ coeff of       │
  │              │ (z−a)^{-n})                          │ (z−a)^{-1}    │
  │ Essential    │ infinitely many negative powers      │ coeff of       │
  │              │                                      │ (z−a)^{-1}    │
  │ Branch point │ not isolated — NOT covered here      │ N/A            │
  └──────────────┴──────────────────────────────────────┴────────────────┘
```

---

## Laurent Series

The Laurent series at an isolated singularity a is a generalization of the Taylor series that includes negative powers:

    f(z) = Σ_{n=−∞}^{∞} cₙ(z − a)ⁿ

    = ... + c_{-2}/(z−a)² + c_{-1}/(z−a) + c₀ + c₁(z−a) + c₂(z−a)² + ...

**Convergence**: In an annulus r < |z − a| < R (the region where f is holomorphic), the series converges absolutely and uniformly.

**Coefficients** (from the Cauchy integral formula):

    cₙ = (1/2πi) ∮_C f(z)/(z − a)^{n+1} dz

for any simple closed curve C in the annulus encircling a once CCW.

The **principal part** is Σ_{n<0} cₙ(z−a)ⁿ. The **analytic part** is Σ_{n≥0} cₙ(z−a)ⁿ.

---

## Singularity Classification

### Removable Singularity

f has a removable singularity at a if:
- lim_{z→a} f(z) exists and is finite
- Laurent series has no negative powers: f(z) = c₀ + c₁(z−a) + ...
- Equivalently: lim_{z→a} (z−a)f(z) = 0

Example: f(z) = sin(z)/z. Near z=0:
    sin z = z − z³/6 + z⁵/120 − ...
    sin(z)/z = 1 − z²/6 + z⁴/120 − ...
    No negative powers. Residue = 0. Redefine f(0) = 1 → holomorphic everywhere.

### Pole of Order n

f has a pole of order n at a if:
- lim_{z→a} |f(z)| = ∞
- Laurent series: c_{-n}/(z−a)^n + ... + c_{-1}/(z−a) + c₀ + ...  (c_{-n} ≠ 0)
- Equivalently: (z−a)^n f(z) has a removable singularity at a (and is nonzero there)

Special case n=1: **simple pole**. Laurent series: c_{-1}/(z−a) + c₀ + ...

### Essential Singularity

f has an essential singularity at a if:
- Laurent series has infinitely many negative powers
- lim_{z→a} f(z) does not exist (not even as ∞)

Example: f(z) = e^{1/z} near z=0:
    e^{1/z} = Σ_{n=0}^∞ (1/z)^n/n! = 1 + 1/z + 1/(2z²) + 1/(6z³) + ...
    Infinitely many negative powers. Residue = 1.

**Picard's Great Theorem**: Near an essential singularity, f takes every complex value (with at most one exception) infinitely many times. The behavior is completely chaotic.

---

## The Residue

**Definition**: Res(f, a) = c_{-1} = the coefficient of (z−a)^{-1} in the Laurent series of f at a.

**Why it matters**: The integral of (z−a)^n around a small circle is 0 for n ≠ −1 and 2πi for n = −1. So only the c_{-1} term contributes to the contour integral:

    ∮_{small circle around a} f(z) dz = 2πi · c_{-1} = 2πi · Res(f, a)

---

## Computing Residues

### At a Simple Pole (order 1)

    Res(f, a) = lim_{z→a} (z − a) f(z)

If f = g/h where g(a) ≠ 0 and h has a simple zero at a:
    Res(f, a) = g(a) / h'(a)    (L'Hôpital variant)

### At a Pole of Order n

    Res(f, a) = (1/(n−1)!) lim_{z→a} d^{n-1}/dz^{n-1} [(z−a)^n f(z)]

### At an Essential Singularity

Must compute Laurent series directly — no shortcut.

### Summary Table

```
SINGULARITY TYPE    RESIDUE FORMULA
─────────────────────────────────────────────────────────
Simple pole         lim_{z→a} (z−a)f(z)
f = g/h, h'(a)≠0   g(a)/h'(a)
Pole of order n     (1/(n−1)!) lim_{z→a} d^{n-1}/dz^{n-1}[(z−a)ⁿf(z)]
Essential           Compute Laurent series, read off c_{-1}
```

---

## The Residue Theorem — Proof

For f meromorphic in Ω with isolated singularities a₁, ..., aₙ inside closed curve C:

By deforming C into small circles Cₖ around each aₖ (valid since f is holomorphic between C and the circles):

    ∮_C f dz = Σₖ ∮_{Cₖ} f dz = Σₖ 2πi · Res(f, aₖ)

More carefully, for each small circle Cₖ with the Laurent series of f:

    ∮_{Cₖ} f dz = ∮_{Cₖ} [Σ cₙ(z−aₖ)ⁿ] dz = Σ cₙ ∮ (z−aₖ)ⁿ dz = 2πi · c_{-1}

Since ∮ (z−aₖ)ⁿ dz = 0 for n ≠ −1 and 2πi for n = −1.

---

## Evaluating Real Integrals — Main Techniques

### Type 1: ∫_{-∞}^{∞} R(x) dx, R rational

Close contour in upper half-plane (large semicircle). Show arc → 0 via ML inequality (rational: degree denominator ≥ degree numerator + 2).

    ∫_{-∞}^{∞} R(x) dx = 2πi × Σ Res(R, poles in upper half-plane)

Example:
    ∫_{-∞}^{∞} dx/(1+x²) = 2πi · Res(1/(1+z²), z=i) = 2πi · 1/(2i) = π

Check: the answer is [arctan x]_{-∞}^{∞} = π/2 − (−π/2) = π. ✓

### Type 2: ∫_{-∞}^{∞} R(x)e^{iax} dx, a > 0 real

Same setup. Arc → 0 by Jordan's lemma (e^{iaz} decays for Im(z) > 0 when a > 0).

    ∫_{-∞}^{∞} R(x)e^{iax} dx = 2πi × Σ Res(R(z)e^{iaz}, upper half-plane)

Taking real/imaginary parts gives ∫ R(x)cos(ax) dx and ∫ R(x)sin(ax) dx.

### Type 3: ∫_0^{2π} R(cos θ, sin θ) dθ (rational in trig)

Substitute z = e^{iθ}, cos θ = (z + 1/z)/2, sin θ = (z − 1/z)/(2i), dz = iz dθ:

    ∫_0^{2π} R(cos θ, sin θ) dθ = ∮_{|z|=1} R(...) dz/(iz)

Then apply residue theorem to poles inside |z| = 1.

### Type 4: ∫_0^∞ x^{α-1} R(x) dx (Mellin-type)

Use keyhole contour wrapping around branch cut of x^{α-1} = e^{(α-1)log x} along positive real axis.

```
KEYHOLE CONTOUR
        Im
         │
         │   large circle (radius R)
    ─────│──╭────────────────────────────╮
         │ ╭╯  × (pole)                  ╰╮
         │─┼──────────────────────────────── Re
    ─────│ ╰╮                            ╭╯
         │   ╰────────────────────────────╯
                 (small circle, radius ε)
                 ↑
         branch cut along positive real axis
```

---

## Worked Examples

**Example 1: Simple pole**

f(z) = 1/(z(z−1)(z−2)), evaluate ∮_{|z|=3/2} f dz.

Poles at z=0, 1, 2. Inside |z|=3/2: z=0 and z=1.

Res(f, 0) = lim_{z→0} z·f(z) = 1/(0−1)(0−2) = 1/2
Res(f, 1) = lim_{z→1} (z−1)·f(z) = 1/(1·(1−2)) = −1

∮ f dz = 2πi(1/2 + (−1)) = 2πi(−1/2) = −πi

**Example 2: Second-order pole**

f(z) = e^z/(z−1)², evaluate ∮_{|z|=2} f dz.

Pole of order 2 at z=1. Inside |z|=2: z=1.

Res(f, 1) = d/dz[e^z]|_{z=1} = e¹ = e

∮ f dz = 2πi · e

**Example 3: Evaluating a real integral**

∫_{-∞}^{∞} cos(x)/(1+x²) dx

Consider ∮ e^{iz}/(1+z²) dz over upper half-plane.
Pole in UHP: z = i (simple pole).
Res(e^{iz}/(1+z²), i) = e^{i·i}/(2i) = e^{-1}/(2i)

∮ = 2πi · e^{-1}/(2i) = π/e = π·e^{-1}

This equals ∫_{-∞}^{∞} e^{ix}/(1+x²) dx (arc integral → 0 by Jordan's lemma).
Real part: ∫_{-∞}^{∞} cos(x)/(1+x²) dx = π/e

---

## Argument Principle and Rouché's Theorem

**Argument Principle**: For f meromorphic in Ω with zeros zₖ (order mₖ) and poles pⱼ (order nⱼ) inside C:

    (1/2πi) ∮_C f'(z)/f(z) dz = Σ mₖ − Σ nⱼ = Z − P

where Z = number of zeros (counted with multiplicity), P = number of poles.

The left side = winding number of f(C) around 0 = (1/2πi) ∮ d(log f) = change in argument of f divided by 2π.

**Rouché's Theorem**: If |g(z)| < |f(z)| on C (a simple closed curve), then f and f+g have the same number of zeros inside C.

*Proof*: On C, f+g is never zero (|f+g| ≥ |f| − |g| > 0). Deform f+g to f continuously; winding number of zeros cannot change by integer jumps under continuous deformation. □

**Application — Fundamental Theorem of Algebra** (alternate proof):
For p(z) = zⁿ + aₙ₋₁zⁿ⁻¹ + ... + a₀ on |z| = R large:
  |zⁿ| > |aₙ₋₁zⁿ⁻¹ + ... + a₀| for R sufficiently large.
By Rouché, p(z) has the same number of zeros inside |z|=R as zⁿ, which has n zeros.

---

**The Mellin transform and its number-theoretic payoff.** The keyhole integral above is a special case of the Mellin transform: M{f}(s) = ∫₀^∞ x^{s−1} f(x) dx. The Mellin transform is the *multiplicative* Fourier transform (substituting x = e^t converts it to a Fourier transform). Its inversion formula is a vertical contour integral — exactly the Bromwich integral from signal processing. For number theory, the critical application is **Perron's formula**: the sum Σ_{n≤x} aₙ can be extracted from its Dirichlet series F(s) = Σ aₙ n^{−s} via the contour integral (1/2πi) ∫_{c−i∞}^{c+i∞} F(s) x^s/s ds. This is Mellin inversion applied to the counting problem, and it is the mechanism by which the analytic properties of ζ(s) (zeros, poles, growth) translate into the distribution of primes. See 07-ANALYTIC-CONTINUATION.md for the full PNT proof chain.

---

## Connection to Signal Processing (Z-transform Bridge)

The Z-transform X(z) = Σ x[n] z^{-n} is a Laurent series in z^{-1}. The **inverse Z-transform** uses contour integration:

    x[n] = (1/2πi) ∮_C X(z) z^{n-1} dz

where C is a contour encircling all poles of X(z). By the residue theorem:

    x[n] = Σ Res(X(z) z^{n-1}, poles of X inside C)

The **poles of X(z)** determine the time-domain behavior of the signal:
- Pole at |z| > 1 → growing (causal, unstable)
- Pole at |z| < 1 → decaying (causal, stable)
- Pole on |z| = 1 → oscillatory (marginally stable)

This is the discrete-time counterpart of Laplace poles in the s-plane. Complex analysis makes both computationally tractable.

---

## Decision Cheat Sheet

| Task | Method |
|------|--------|
| Compute ∮ f dz | Residue theorem: 2πi × Σ Res(f, interior poles) |
| Find residue at simple pole | lim_{z→a}(z−a)f(z) |
| Find residue at simple pole f=g/h | g(a)/h'(a) |
| Find residue at pole of order n | Differentiate (z−a)^n f(z) n−1 times |
| Evaluate ∫_{-∞}^{∞} R(x) dx | Close UHP, sum residues in UHP |
| Evaluate ∫ R(cos θ, sin θ) dθ | z = e^{iθ} substitution, unit circle |
| Count zeros inside C | Argument principle or Rouché's theorem |
| Identify singularity type | Look at Laurent series principal part |

---

## Common Confusion Points

**Laurent series is not unique globally**: The Laurent series of f at a is unique, but f can have different Laurent series in different annuli centered at a. If f is holomorphic on 0 < |z−a| < R, there's one series. If there's another annulus R < |z−a| < S, there's a different series there.

**Residue = 0 does not mean singularity is removable**: An essential singularity can have c_{-1} = 0. A pole of order 2 with Laurent series 1/(z−a)² has no c_{-1} term — residue 0. "Residue 0" means the contour integral around that point is 0, not that the singularity is removable.

**Rouché requires strict inequality |g| < |f| on C**: The bound must hold on the entire contour C, not just at some points. If equality holds anywhere on C, f+g might vanish on C and the theorem fails.

**Jordan's Lemma is for e^{iaz} with a > 0 in the upper half-plane**: For a < 0, close in the lower half-plane. For real integrals involving cos or sin, factor out e^{iax} = cos(ax) + i sin(ax) and take real/imaginary parts of the complex integral.

**The argument principle counts zeros minus poles, not just zeros**: If f has a pole inside C, it contributes −1 to the count. The net count (1/2πi)∮ f'/f dz gives Z − P. To count only zeros: ensure f is holomorphic inside C (no poles).
