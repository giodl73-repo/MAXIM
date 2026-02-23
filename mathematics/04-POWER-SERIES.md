# 04 — Power Series: Taylor, Convergence, and the Functions Behind the Functions

```
THE LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  WHAT A POWER SERIES IS:
  f(x) = a₀ + a₁x + a₂x² + a₃x³ + ...  =  Σ aₙ xⁿ
                                              n=0

  ┌──────────────────────────────────────────────────────────────────────────┐
  │  TAYLOR / MACLAURIN     GENERATING FUNCTIONS     ASYMPTOTIC SERIES      │
  │  Approximation          Encode sequences         Divergent but useful    │
  │  Local → global         Combinatorics, QM        Stirling, Laplace       │
  │                                                                          │
  │  CONVERGENCE             OPERATIONS               APPLICATIONS           │
  │  Radius of conv.         Diff / integrate         Small-angle, binomial  │
  │  Root / ratio tests      Compose / multiply       ODE solutions, physics │
  └──────────────────────────────────────────────────────────────────────────┘

  THE CORE INSIGHT:
  A smooth function IS its Taylor series (in the convergence region).
  This is not an approximation — it is an identity.
  Polynomials are the atoms. Every smooth function decomposes into them.
═══════════════════════════════════════════════════════════════════════════════
```

---

## 1. The Taylor Series Formula

### 1.1 Derivation — Assume the Form, Solve for Coefficients

If f(x) equals a power series near x = a:

```
  f(x) = c₀ + c₁(x−a) + c₂(x−a)² + c₃(x−a)³ + ...

  Evaluate at x = a:         f(a) = c₀
  Differentiate, eval at a:  f'(a) = c₁
  Differentiate twice:       f''(a) = 2c₂  →  c₂ = f''(a)/2!
  Differentiate n times:     f⁽ⁿ⁾(a) = n! cₙ  →  cₙ = f⁽ⁿ⁾(a)/n!

  ┌─────────────────────────────────────────────────────────────────────┐
  │  TAYLOR SERIES about x = a:                                        │
  │                                                                     │
  │  f(x) = Σ f⁽ⁿ⁾(a)/n! · (x−a)ⁿ                                   │
  │         n=0                                                         │
  │                                                                     │
  │  MACLAURIN SERIES: Taylor about a = 0                              │
  │  f(x) = Σ f⁽ⁿ⁾(0)/n! · xⁿ                                        │
  └─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Remainder — How Good Is the Approximation?

Truncate after the nth term: error is bounded by the Lagrange remainder:

```
  Rₙ(x) = f⁽ⁿ⁺¹⁾(c) / (n+1)! · (x−a)ⁿ⁺¹     for some c between a and x

  |Rₙ(x)| ≤ M / (n+1)! · |x−a|ⁿ⁺¹
  where M = max|f⁽ⁿ⁺¹⁾| on the interval

  For eˣ with x in [0,1]:  |Rₙ| ≤ e/(n+1)! → 0 rapidly
  For sin x with x small:  |Rₙ| ≤ |x|ⁿ⁺¹/(n+1)! → 0 extremely fast

  Rule of thumb: including terms up to order n means error is order xⁿ⁺¹.
```

---

## 2. The Essential Maclaurin Series

Memorize these. Everything else is derived from them.

```
  ┌─────────────────────────────────────────────────────────────────────────┐
  │                                                                         │
  │  eˣ   = 1 + x + x²/2! + x³/3! + x⁴/4! + ...    all x               │
  │                                                                         │
  │  sin x = x − x³/3! + x⁵/5! − x⁷/7! + ...        all x               │
  │                                                                         │
  │  cos x = 1 − x²/2! + x⁴/4! − x⁶/6! + ...        all x               │
  │                                                                         │
  │  ln(1+x) = x − x²/2 + x³/3 − x⁴/4 + ...         |x| < 1             │
  │                                                                         │
  │  1/(1−x) = 1 + x + x² + x³ + ...                 |x| < 1  (geometric) │
  │                                                                         │
  │  (1+x)ᵅ = 1 + αx + α(α−1)x²/2! + α(α−1)(α−2)x³/3! + ...  |x| < 1  │
  │           (binomial series — α need not be integer)                    │
  │                                                                         │
  │  arctan x = x − x³/3 + x⁵/5 − x⁷/7 + ...        |x| ≤ 1             │
  │                                                                         │
  │  sinh x = x + x³/3! + x⁵/5! + ...                all x (no sign alts) │
  │  cosh x = 1 + x²/2! + x⁴/4! + ...                all x               │
  │                                                                         │
  └─────────────────────────────────────────────────────────────────────────┘
```

### Connecting eˣ, sin x, cos x — Euler Confirmed

```
  e^(ix) = 1 + ix + (ix)²/2! + (ix)³/3! + (ix)⁴/4! + ...
         = 1 + ix − x²/2! − ix³/3! + x⁴/4! + ix⁵/5! − ...
         = (1 − x²/2! + x⁴/4! − ...) + i(x − x³/3! + x⁵/5! − ...)
         = cos x + i sin x    ✓

  The series proof of Euler's formula.
  sin and cos are just the odd and even parts of eˣ evaluated on the imaginary axis.
```

---

## 3. Convergence

### 3.1 Radius of Convergence

A power series Σ aₙ(x−a)ⁿ converges for |x−a| < R and diverges for |x−a| > R.

```
  ┌────────────────────────────────────────────────────────────────┐
  │                                                                │
  │  Diverges  │  Boundary  │  Converges  │  Boundary │ Diverges  │
  │  ──────────┼────────────┼─────────────┼───────────┼──────────  │
  │            a−R          a            a+R                       │
  │                                                                │
  │  R = 0:    only converges at x = a                            │
  │  R = ∞:    converges for all x (eˣ, sin x, cos x)            │
  │  0 < R < ∞: converges on open interval, boundary case-by-case │
  └────────────────────────────────────────────────────────────────┘
```

### 3.2 Computing R — Two Methods

**Ratio Test** (when ratios are clean):

```
  R = lim |aₙ/aₙ₊₁|   as n → ∞

  For eˣ: aₙ = 1/n!, aₙ₊₁ = 1/(n+1)!
  R = lim (1/n!)/(1/(n+1)!) = lim (n+1) = ∞  ✓

  For ln(1+x): aₙ = (-1)ⁿ⁺¹/n
  R = lim (1/n)/(1/(n+1)) = lim (n+1)/n = 1  ✓
```

**Root Test** (when ratio test is messy):

```
  R = 1 / limsup |aₙ|^(1/n)   as n → ∞   (Cauchy-Hadamard formula)
```

### 3.3 Why the Radius Is What It Is — Complex Perspective

```
  The radius of convergence = distance to the nearest singularity
  in the COMPLEX plane, even if you're only working on the real line.

  ln(1+x): singularity at x = -1 (complex distance = 1) → R = 1
  1/(1+x²): singularities at x = ±i (distance = 1 from origin) → R = 1
             Even though the real function looks smooth at x = 1!

  This is why 1/(1+x²) has R = 1 even though it's perfectly smooth on ℝ.
  The complex poles at ±i determine the real convergence radius.
```

---

## 4. Operations on Power Series

Inside the radius of convergence, treat series like polynomials.

### 4.1 Differentiation and Integration — Term by Term

```
  If f(x) = Σ aₙ xⁿ  (|x| < R), then:

  f'(x) = Σ n·aₙ xⁿ⁻¹    (same R)
          n=1

  ∫f(x)dx = Σ aₙ/(n+1) · xⁿ⁺¹ + C   (same R, check endpoints)
             n=0

  Example: derive the series for ln(1+x) from 1/(1+x):
  1/(1+x) = 1 − x + x² − x³ + ...   (geometric with −x)
  Integrate both sides:
  ln(1+x) = x − x²/2 + x³/3 − x⁴/4 + ...   ✓

  Example: derive arctan from 1/(1+x²):
  1/(1+x²) = 1 − x² + x⁴ − x⁶ + ...   (geometric with −x²)
  Integrate:
  arctan x = x − x³/3 + x⁵/5 − x⁷/7 + ...   ✓
```

### 4.2 Composition — Substitute One Series Into Another

```
  e^(sin x) = ?

  sin x = x − x³/6 + x⁵/120 − ...
  Let u = sin x, then e^u = 1 + u + u²/2! + u³/3! + ...

  e^(sin x) = 1 + (x − x³/6 + ...) + (x − ...)²/2 + (x − ...)³/6 + ...
            = 1 + x + x²/2 − x⁴/8 + ...

  (Keep only through desired order, drop higher terms)

  Key trick: substitute into the exponential series, multiply carefully,
  and discard terms beyond your target order.
```

### 4.3 Multiplication — Cauchy Product

```
  (Σ aₙ xⁿ)(Σ bₙ xⁿ) = Σ cₙ xⁿ   where cₙ = Σ aₖ bₙ₋ₖ
                                              k=0

  Example: sin x · cos x  (should give ½ sin 2x)
  = (x − x³/6 + x⁵/120 − ...)(1 − x²/2 + x⁴/24 − ...)
  = x·1 + x·(-x²/2) + (-x³/6)·1 + ...
  = x − x³/2 − x³/6 + ... = x − 2x³/3 + ...

  Check: ½ sin 2x = ½(2x − (2x)³/6 + ...) = x − 4x³/6 + ... = x − 2x³/3 + ... ✓
```

---

## 5. Small-Angle and Physical Approximations

The reason power series matter most in physics: truncate to get tractable formulas.

### 5.1 Small-Angle Approximations (θ in radians)

```
  sin θ ≈ θ               (first term only, error O(θ³))
  cos θ ≈ 1 − θ²/2        (two terms, error O(θ⁴))
  tan θ ≈ θ               (first term, error O(θ³))

  Valid for |θ| << 1 radian (roughly |θ| < 0.3 for 1% error)

  Applications:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Pendulum: exact equation  d²θ/dt² = -(g/L) sin θ                  │
  │            linearized:     d²θ/dt² ≈ -(g/L) θ   → harmonic motion  │
  │            Period T = 2π√(L/g)  (only valid for small swings)       │
  │                                                                      │
  │  Snell's law at near-normal incidence: n₁θ₁ ≈ n₂θ₂                 │
  │  Diffraction: sin θ ≈ θ for θ << 1 → Rayleigh criterion            │
  │  EM waves at near-grazing: cos θ ≈ 1 → large reflection            │
  └──────────────────────────────────────────────────────────────────────┘
```

### 5.2 Binomial Approximation — Used Constantly

```
  (1 + x)ᵅ ≈ 1 + αx   for |x| << 1

  Special cases:
  1/√(1+x) = (1+x)^(-½) ≈ 1 − x/2
  √(1+x)   = (1+x)^(½)  ≈ 1 + x/2
  1/(1+x)  = (1+x)^(-1) ≈ 1 − x

  Physics examples:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Relativistic kinetic energy for v << c:                            │
  │  E = mc²/√(1−v²/c²) = mc²(1−v²/c²)^(-½)                          │
  │    ≈ mc²(1 + v²/2c²) = mc² + ½mv²    ✓ recovers Newtonian KE      │
  │                                                                      │
  │  Gravitational redshift for weak field (GM/rc² << 1):              │
  │  f_obs/f_emit = √(1−2GM/rc²) ≈ 1 − GM/rc²                         │
  │                                                                      │
  │  Doppler shift for v << c:                                          │
  │  f_obs = f√((1+v/c)/(1−v/c)) ≈ f(1 + v/c)                         │
  └──────────────────────────────────────────────────────────────────────┘
```

### 5.3 Exponential Approximations

```
  eˣ ≈ 1 + x           for small x  (critical in statistics, QM)
  e^(-x) ≈ 1 − x + x²/2

  In physics:
  Boltzmann factor: e^(-E/kT) for high-T (E << kT):
    e^(-E/kT) ≈ 1 − E/kT   → equipartition theorem limit

  Decay: e^(-λt) for short times t << 1/λ:
    ≈ 1 − λt  → linear approximation to exponential decay
```

---

## 6. Asymptotic Series

Not all useful series converge. An **asymptotic expansion** approximates a function even if the series diverges.

### 6.1 Stirling's Approximation

```
  n! ~ √(2πn) · (n/e)ⁿ                           (leading order)

  Full Stirling series (asymptotic, diverges but very useful):
  ln(n!) = n ln n − n + ½ ln(2πn) + 1/12n − 1/360n³ + ...

  Error using just √(2πn)(n/e)ⁿ:
  n = 10:   exact = 3628800,  Stirling = 3598695  (0.8% error)
  n = 100:  error < 0.008%

  Used in: statistical mechanics (entropy S = k ln Ω with Ω ~ N!),
           combinatorics, information theory (Shannon entropy derivation)
```

### 6.2 Laplace's Method — Dominant Contribution to an Integral

```
  For integrals of the form ∫ e^(nf(x)) dx  as n → ∞:
  The integral is dominated by the maximum of f(x).

  Near the maximum x₀: f(x) ≈ f(x₀) − ½|f''(x₀)|(x−x₀)²

  ∫ e^(nf(x)) dx ≈ e^(nf(x₀)) √(2π/n|f''(x₀)|)    (Gaussian integral result)

  This is the saddle-point method / stationary phase approximation.
  Used in: statistical mechanics partition functions, quantum path integrals,
           Airy function asymptotics, WKB approximation in QM.
```

---

## 7. Generating Functions

A generating function encodes a sequence {a₀, a₁, a₂, ...} as the coefficients of a power series:

```
  G(x) = Σ aₙ xⁿ  =  a₀ + a₁x + a₂x² + ...
          n=0

  The sequence is "generated" by reading off coefficients.
  Algebraic operations on G correspond to operations on the sequence.
```

### 7.1 The Geometric Series — Simplest Generating Function

```
  G(x) = 1/(1−x) = Σ xⁿ        → generates {1, 1, 1, 1, ...}

  G(x) = 1/(1−rx) = Σ rⁿ xⁿ    → generates {1, r, r², r³, ...}

  G(x) = x/(1−x)² = Σ n xⁿ     → generates {0, 1, 2, 3, ...}
```

### 7.2 Fibonacci via Generating Functions

```
  F₀=0, F₁=1, Fₙ = Fₙ₋₁ + Fₙ₋₂

  G(x) = Σ Fₙ xⁿ
  Using the recurrence: G(x) = x/(1−x−x²)
  Partial fractions → closed form: Fₙ = (φⁿ − ψⁿ)/√5
  where φ = (1+√5)/2 (golden ratio), ψ = (1−√5)/2

  The algebra of generating functions converts recurrences → algebra.
```

### 7.3 Exponential Generating Functions

```
  EGF: G(x) = Σ aₙ xⁿ/n!        (divide by n! — natural for counting labeled structures)

  eˣ is the EGF for aₙ = 1 (all ones)
  e^(2x) is the EGF for aₙ = 2ⁿ

  In physics: the partition function Z = Σ e^(-Eₙ/kT) is a generating function
  for the moments of energy: ⟨Eⁿ⟩ = (-1)ⁿ ∂ⁿ ln Z / ∂β ⁿ
  where β = 1/kT
```

---

## 8. Power Series and Differential Equations

### 8.1 Series Solutions to ODEs

When an ODE has no closed-form solution, assume a power series:

```
  Example: y'' + xy' + y = 0   (Hermite-like equation)

  Assume y = Σ aₙ xⁿ
  y' = Σ n aₙ xⁿ⁻¹,  y'' = Σ n(n−1) aₙ xⁿ⁻²

  Substitute, collect by power of x, set each coefficient to zero:
  → recurrence relation for aₙ
  → two independent solutions (matching degree of ODE)

  The method works whenever x=0 is an ordinary point of the ODE.
  The radius of convergence of the solution equals the distance to the
  nearest singularity of the coefficient functions.
```

### 8.2 The Classic Physics Special Functions

All arise from power series solutions to named ODEs:

```
  ODE                            Series Solution          Physics
  ──────────────────────────────────────────────────────────────────
  y'' − 2xy' + 2ny = 0          Hermite Hₙ(x)           QM harmonic oscillator
  (1−x²)y'' − 2xy' + n(n+1)y=0 Legendre Pₙ(x)          Angular momentum in QM
  x²y'' + xy' + (x²−n²)y = 0   Bessel Jₙ(x)            Cylindrical problems
  y'' − (2n+1−x²)y = 0          Parabolic cylinder       QM problems
  (1−x²)y'' − xy' + n²y = 0    Chebyshev Tₙ(x)          Numerical analysis

  All of these are power series that terminate (become polynomials)
  for certain parameter values n — that's the quantization condition!
  Hermite polynomials terminate for integer n → discrete energy levels.
```

---

## 9. Key Limits Involving Series

These appear as building blocks across physics:

```
  lim(x→0) sin(x)/x = 1        (from sin x ≈ x)
  lim(x→0) (eˣ−1)/x = 1       (from eˣ ≈ 1+x)
  lim(x→0) ln(1+x)/x = 1      (from ln(1+x) ≈ x)
  lim(x→∞) (1+x/n)ⁿ = eˣ      (definition of e as a limit)
  lim(n→∞) (1+1/n)ⁿ = e        (classic e definition)
  lim(x→0) (1−cos x)/x² = 1/2  (from cos x ≈ 1 − x²/2)

  These are all disguised Taylor series, first-order truncations.
```

---

## Decision Cheat Sheet

| Need to... | Tool |
|-----------|------|
| Approximate sin/cos/tan for small angle | Truncate Taylor to first non-trivial term |
| Approximate (1+x)ᵅ for small x | Binomial: 1 + αx |
| Find pattern in a sequence | Generating function |
| Solve ODE without closed-form | Power series substitution |
| Integrate 1/(1+x²), 1/√(1−x²) | Use the known arctan/arcsin series |
| Evaluate n! for large n | Stirling's approximation |
| Approximate an integral dominated by a peak | Laplace / saddle-point method |
| Check if series converges | Ratio test (factorial/exponential), root test |
| Derive ln, arctan series | Integrate geometric series |
| Find the physics behind quantization | Series solution terminates at integer n |

---

## Common Confusion Points

**"Does Taylor series = the function, or is it an approximation?"**
Both, depending on context. Within the radius of convergence, for analytic functions, the infinite Taylor series *equals* the function exactly — it's an identity, not an approximation. Truncating at finite terms gives an approximation. Most "nice" functions (eˣ, sin, cos, polynomials, rational functions away from poles) are analytic. Pathological counterexample: f(x) = e^(-1/x²) has all-zero Taylor coefficients at x=0 but isn't identically zero.

**"Why does ln(1+x) only converge for |x| ≤ 1?"**
The singularity is at x = -1 (ln(0) = -∞). The series can't reach past a singularity. As a complex function, the singularity is at distance 1 from the origin, giving R = 1. At x = 1: the series converges (alternating series test → ln 2). At x = -1: diverges to -∞.

**"What's an asymptotic expansion if it diverges?"**
The series gives an increasingly accurate approximation as you add more terms — up to a point. Then the terms start growing and the partial sums diverge. But the optimal truncation (stop just before the smallest term) can give extraordinary accuracy. Stirling is like this: the full series diverges, but the first few terms give exponentially good approximations for large n.

**"Why do generating functions work for recurrences?"**
A linear recurrence like Fₙ = Fₙ₋₁ + Fₙ₋₂ becomes a functional equation on G(x): G(x) = xG(x) + x²G(x) + (initial conditions). Solve algebraically for G(x), then extract coefficients. You've turned an iterative recurrence into algebra. Same principle behind z-transforms (discrete Laplace) in DSP.

**"What's the connection between power series and Fourier series?"**
Both decompose functions into basis elements (xⁿ vs sin/cos). Power series are local (converge near a point). Fourier series are global (converge over a period). The orthogonality of sin/cos (module 03) is analogous to the fact that xⁿ terms are "independent" in Taylor. Fourier series are actually Taylor series — evaluated on the unit circle in the complex plane via e^(inθ).

---

*Next: `mathematics/05-GROUPS-SETS-ALGEBRA.md` — sets, groups, rings, fields, Artin review, and the symmetry groups that run all of physics (U(1), SU(2), SU(3)).*
