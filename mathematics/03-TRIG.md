# 03 — Trigonometry: The Full Refresh

```
THE LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  GEOMETRIC DEFINITION          UNIT CIRCLE                COMPLEX PLANE
  ┌──────────────────┐          ┌──────────────────┐        ┌──────────────────┐
  │   hyp            │          │      (0,1)        │        │  e^(iθ) = cos+i·sin│
  │   ╱|             │          │        │          │        │                  │
  │  ╱ |opp          │          │  (-1,0)┼──(1,0)  │        │  eiπ + 1 = 0     │
  │ ╱θ |             │          │        │          │        │  (Euler's formula│
  │╱___|             │          │      (0,-1)       │        │  = everything)   │
  │    adj           │          └──────────────────┘        └──────────────────┘
  └──────────────────┘
  sin θ = opp/hyp              P = (cos θ, sin θ)          z = r·e^(iθ)
  cos θ = adj/hyp              for any angle θ
  tan θ = opp/adj = sin/cos    UNIT CIRCLE IS THE MASTER DEFINITION

  WHY THIS MATTERS FOR YOU:
  Fourier transform, Laplace, phasors, EM waves, quantum states —
  all collapse to complex exponentials. Trig is just the real/imag parts.

  COMPLEX UNIFICATION: sin z and cos z are entire functions on ℂ defined by
  the same power series. Circular and hyperbolic functions are the SAME
  function on different axes: cos(iz) = cosh(z), sin(iz) = i sinh(z).
═══════════════════════════════════════════════════════════════════════════════
```

---

## 1. The Unit Circle — The Only Definition That Matters

Forget SOH-CAH-TOA. The real definition:

```
UNIT CIRCLE
                        90° = π/2
                           │
            135°=3π/4      │        45°=π/4
                    ╲      │      ╱
                     ╲     │     ╱
  180°=π ─────────────●────┼────●───────── 0° = 0 = 2π
                     ╱     │     ╲
                    ╱      │      ╲
            225°=5π/4      │        315°=7π/4
                           │
                        270°=3π/2

  Point at angle θ: P(θ) = (cos θ, sin θ)

  Key values — memorize these, derive the rest:
  ┌────────────────────────────────────────────────────────────────┐
  │  θ (rad)  │  θ (deg)  │  cos θ      │  sin θ      │  tan θ   │
  ├───────────┼───────────┼─────────────┼─────────────┼──────────┤
  │  0        │    0°     │  1          │  0          │  0       │
  │  π/6      │   30°     │  √3/2       │  1/2        │  1/√3    │
  │  π/4      │   45°     │  √2/2       │  √2/2       │  1       │
  │  π/3      │   60°     │  1/2        │  √3/2       │  √3      │
  │  π/2      │   90°     │  0          │  1          │  ∞       │
  │  π        │  180°     │ -1          │  0          │  0       │
  │  3π/2     │  270°     │  0          │ -1          │  ∞       │
  │  2π       │  360°     │  1          │  0          │  0       │
  └────────────────────────────────────────────────────────────────┘

  Memory trick: cos starts at 1, sin starts at 0.
  The 30-45-60 triangle values: 1/2, √2/2, √3/2 — increasing order.
```

### Signs by Quadrant

```
              sin +
              cos -       sin +
                          cos +
  II    │    I
        │
────────┼────────
        │
  III   │   IV
              sin -
  sin -       cos +
  cos -

  "All Students Take Calculus" (All, Sin, Tan, Cos positive in Q I–IV)
```

---

## 2. The Fundamental Identities

### 2.1 Pythagorean (from x² + y² = 1)

```
  sin²θ + cos²θ = 1          ← the master identity
  1 + tan²θ = sec²θ          ← divide master by cos²θ
  cot²θ + 1 = csc²θ          ← divide master by sin²θ
```

### 2.2 Angle Addition — The Ones You Need to Derive Everything

```
  sin(A + B) = sin A cos B + cos A sin B
  cos(A + B) = cos A cos B − sin A sin B
  tan(A + B) = (tan A + tan B) / (1 − tan A tan B)

  Proof via rotation matrices (the "real" proof):
  ┌          ┐   ┌          ┐   ┌              ┐
  │ cos(A+B) │   │ cos A  -sin A│   │ cos B  -sin B│
  │          │ = │              │ × │              │
  │ sin(A+B) │   │ sin A   cos A│   │ sin B   cos B│
  └          ┘   └              ┘   └              ┘

  Expanding top-left: cos A cos B - sin A sin B ✓
  Expanding bottom-left: sin A cos B + cos A sin B ✓
```

### 2.3 Double Angle — Derived from Addition with B = A

```
  sin 2A = 2 sin A cos A
  cos 2A = cos²A − sin²A = 1 − 2sin²A = 2cos²A − 1
  tan 2A = 2 tan A / (1 − tan²A)
```

### 2.4 Half Angle — Solving cos 2A forms for sin²A, cos²A

```
  sin²A = (1 − cos 2A) / 2        ← cos 2A = 1 − 2sin²A → rearranged
  cos²A = (1 + cos 2A) / 2        ← cos 2A = 2cos²A − 1 → rearranged

  Why these matter: you integrate sin² and cos² constantly in physics.
  ∫sin²θ dθ = θ/2 − sin(2θ)/4 + C   (use the half-angle form)
```

### 2.5 Product-to-Sum — Key for Fourier / Beating

```
  sin A cos B = ½[sin(A+B) + sin(A−B)]
  cos A cos B = ½[cos(A+B) + cos(A−B)]
  sin A sin B = ½[cos(A−B) − cos(A+B)]

  Physical meaning: two oscillators multiplied = sum and difference frequencies
  This is literally AM radio demodulation, beat frequencies in waves,
  and the mechanism behind Fourier analysis.
```

### 2.6 Sum-to-Product — Interference Pattern

```
  sin A + sin B = 2 sin((A+B)/2) cos((A−B)/2)
  cos A + cos B = 2 cos((A+B)/2) cos((A−B)/2)
  cos A − cos B = −2 sin((A+B)/2) sin((A−B)/2)

  Physical meaning: superposition of two waves at nearly same frequency
  → beats (slow envelope × fast carrier)
```

---

## 3. Euler's Formula — The Master Key

This is the most important formula in applied mathematics:

```
  e^(iθ) = cos θ + i sin θ                ← Euler's formula

  Proof via Taylor series:
  e^x = 1 + x + x²/2! + x³/3! + x⁴/4! + ...

  e^(iθ) = 1 + iθ + (iθ)²/2! + (iθ)³/3! + (iθ)⁴/4! + ...
          = 1 + iθ − θ²/2! − iθ³/3! + θ⁴/4! + iθ⁵/5! − ...

  Real parts:  1 − θ²/2! + θ⁴/4! − ... = cos θ  ✓
  Imag parts:  θ − θ³/3! + θ⁵/5! − ... = sin θ  ✓
```

**The full complex statement.** The formula holds for all z ∈ ℂ, not just
real θ. The functions e^z, sin z, cos z are each defined on all of ℂ by the
same power series — they are entire functions (analytic on all of ℂ, no
singularities anywhere). Key consequences of the complex extension:

```
  Periodicity:  e^(z + 2πi) = e^z  for all z ∈ ℂ
                The imaginary axis adds periodicity; the real part adds growth.

  Zeros of sin z:  sin z = 0 iff z = nπ  for n ∈ ℤ  (no other zeros)
  Poles of tan z:  tan z = sin z/cos z has poles at z = π/2 + nπ

  Pythagorean identity over ℂ:  sin²z + cos²z = 1  holds for all z ∈ ℂ
  (follows from the power series definitions, not geometry)

  cos z = (e^(iz) + e^(-iz)) / 2     holds for all z ∈ ℂ
  sin z = (e^(iz) − e^(-iz)) / 2i    holds for all z ∈ ℂ
```

The real trig functions are restrictions of these entire functions to the real
line. The complex viewpoint reveals why, e.g., the Taylor series for 1/cos x
has radius of convergence π/2 — the nearest singularity in ℂ is the pole of
cos z at z = ±π/2, distance π/2 from the origin.

### Consequences — Everything Follows

```
  e^(iθ) = cos θ + i sin θ
  e^(-iθ) = cos θ − i sin θ

  Adding:    cos θ = (e^(iθ) + e^(-iθ)) / 2
  Subtracting: sin θ = (e^(iθ) − e^(-iθ)) / 2i

  Euler's identity (most beautiful equation in math):
  e^(iπ) + 1 = 0    ← e, i, π, 1, 0 all in one equation

  COMPLEX EXPONENTIAL REPLACES ALL TRIG:
  Instead of tracking sin and cos separately, track e^(iωt).
  Real part = cos ωt (in-phase component)
  Imag part = sin ωt (quadrature component)
```

### Phasors — Why Engineers Love This

```
  AC signal: V(t) = V₀ cos(ωt + φ)

  Phasor representation: Ṽ = V₀ e^(iφ)   (drop the e^(iωt), it's understood)
  Actual signal: V(t) = Re[Ṽ · e^(iωt)]

  Addition of signals with same ω:
  V₁ cos(ωt + φ₁) + V₂ cos(ωt + φ₂) = Re[Ṽ₁ e^(iωt) + Ṽ₂ e^(iωt)]
                                       = Re[(Ṽ₁ + Ṽ₂) e^(iωt)]

  → Add phasors as complex numbers. Let e^(iωt) carry through.
  → Differential equations → algebraic equations (this is 6.003's entire basis)

  Impedance:
  Resistor:  Z_R = R          (real, no phase shift)
  Capacitor: Z_C = 1/(iωC)    (imaginary, −90° phase shift)
  Inductor:  Z_L = iωL        (imaginary, +90° phase shift)
```

---

## 4. Inverse Trig Functions

### 4.1 Definitions and Ranges

```
  arcsin: [-1, 1] → [-π/2, π/2]
  arccos: [-1, 1] → [0, π]
  arctan: (-∞, ∞) → (-π/2, π/2)

  atan2(y, x): full quadrant-aware version, range (-π, π]
  Use atan2 in code always — it handles all quadrants correctly.
```

### 4.2 Key Values

```
  arcsin(0) = 0       arccos(1) = 0       arctan(0) = 0
  arcsin(1) = π/2     arccos(0) = π/2     arctan(1) = π/4
  arcsin(-1) = -π/2   arccos(-1) = π       arctan(∞) = π/2
  arcsin(1/2) = π/6   arccos(1/2) = π/3    arctan(√3) = π/3
```

### 4.3 Derivatives — You Need These for Physics

```
  d/dx arcsin(x) = 1/√(1−x²)
  d/dx arccos(x) = −1/√(1−x²)
  d/dx arctan(x) = 1/(1+x²)

  Integral version:
  ∫ dx/√(1−x²) = arcsin(x) + C
  ∫ dx/(1+x²) = arctan(x) + C   ← appears constantly in QM, EM
```

---

## 5. Hyperbolic Trig Functions

These appear in transmission lines, wave mechanics, relativistic physics, and solutions to differential equations.

### 5.1 Definitions — Analogous to Circular Trig

```
  sinh x = (e^x − e^(-x)) / 2     ← "sine hyperbolic"
  cosh x = (e^x + e^(-x)) / 2     ← "cosine hyperbolic"
  tanh x = sinh x / cosh x

  Compare:
  sin x = (e^(ix) − e^(-ix)) / 2i     circular, on unit circle
  sinh x = (e^x − e^(-x)) / 2         hyperbolic, on unit hyperbola

  Connection: sinh(ix) = i sin(x)
              cosh(ix) = cos(x)        ← substitute ix into circular
```

**The unification over ℂ**: sin z and sinh z are the same function evaluated
at different arguments. Specifically:

```
  cos(iz) = cosh(z)     for all z ∈ ℂ
  sin(iz) = i sinh(z)   for all z ∈ ℂ

  Proof: cos(iz) = (e^(i·iz) + e^(-i·iz))/2 = (e^(-z) + e^z)/2 = cosh(z) ✓
```

The complex plane has the real axis for circular behavior and the imaginary
axis for hyperbolic behavior. They are not two different families of functions —
they are one entire function on ℂ, restricted to two perpendicular axes.

### 5.2 Identities — Parallel to Circular (with sign flip)

```
  cosh²x − sinh²x = 1             ← note: MINUS not plus (hyperbola not circle)
  sinh(x+y) = sinh x cosh y + cosh x sinh y
  cosh(x+y) = cosh x cosh y + sinh x sinh y
```

### 5.3 Where They Appear

```
  Transmission lines (distributed LC):
    V(x) = V⁺ cosh(γx) + V⁻ sinh(γx)

  Relativistic velocity addition:
    v = c tanh(φ)    where φ = rapidity (Minkowski geometry)

  Hanging cable (catenary):
    y = a cosh(x/a)

  Wave equation solutions:
    Evanescent fields (skin depth, tunneling): decay as e^(-x/δ) = cosh/sinh form
```

---

## 6. Trig in Calculus

### 6.1 Derivatives — The Essential Six

```
  d/dx sin x = cos x
  d/dx cos x = −sin x
  d/dx tan x = sec²x
  d/dx csc x = −csc x cot x
  d/dx sec x = sec x tan x
  d/dx cot x = −csc²x

  Note the pattern: sin ↔ cos with a sign flip on the way "down"
  (differentiating cos brings in the −)
```

### 6.2 Key Integrals

```
  ∫ sin x dx = −cos x + C
  ∫ cos x dx = sin x + C
  ∫ tan x dx = ln|sec x| + C
  ∫ sec x dx = ln|sec x + tan x| + C

  Power reduction (use constantly in physics):
  ∫₀²π sin²(nωt) dt = π/ω          ∫₀²π cos²(nωt) dt = π/ω
  ∫₀²π sin(nωt)cos(mωt) dt = 0      for all integers n, m
  ∫₀²π sin(nωt)sin(mωt) dt = 0      for n ≠ m   (orthogonality!)
  ∫₀²π cos(nωt)cos(mωt) dt = 0      for n ≠ m

  ORTHOGONALITY IS THE BASIS OF FOURIER SERIES.
```

### 6.3 Trig Substitution

```
  Pattern               Substitution        Identity used
  ──────────────────────────────────────────────────────
  √(a²−x²)             x = a sin θ         1−sin²θ = cos²θ
  √(a²+x²)             x = a tan θ         1+tan²θ = sec²θ
  √(x²−a²)             x = a sec θ         sec²θ−1 = tan²θ
```

---

## 7. Angles, Waves, and the Bridge to Signals

### 7.1 Sinusoidal Parameters

```
  y(t) = A sin(ωt + φ) + C

  A   = amplitude
  ω   = angular frequency [rad/s]   ω = 2πf
  f   = frequency [Hz]              f = 1/T
  T   = period [s]
  φ   = phase shift [rad]           positive φ → shifted left (earlier)
  C   = DC offset

  SPATIAL wave: y(x) = A sin(kx + φ)
  k = wavenumber [rad/m]   k = 2π/λ
  λ = wavelength [m]

  TRAVELING wave: y(x,t) = A sin(kx − ωt)
  Phase velocity: v = ω/k = λf
```

### 7.2 Beats — Two Frequencies Close Together

```
  y = sin(ω₁t) + sin(ω₂t)

  Using sum-to-product (section 2.6):
  = 2 sin((ω₁+ω₂)t/2) · cos((ω₁−ω₂)t/2)
       └──── fast carrier ──┘   └── slow envelope ──┘

  ω_carrier = (ω₁+ω₂)/2         average frequency
  ω_beat = (ω₁−ω₂)/2            half the difference (beats at ω₁−ω₂)

  You hear this when two guitar strings are slightly out of tune.
  The Doppler effect, RF mixing, and lock-in detection all use this.
```

### 7.3 Phase vs Group Velocity

```
  Phase velocity:  v_p = ω/k   (speed of a single frequency component)
  Group velocity:  v_g = dω/dk  (speed of the envelope / information)

  For non-dispersive medium (ω ∝ k):  v_p = v_g
  For dispersive medium (ω = ω(k) nonlinear):  v_p ≠ v_g

  Water waves: long waves travel faster than short waves → dispersion
  Quantum mechanics: v_g = p/m (particle velocity), v_p = E/p = p/2m ≠ v_g
  Waveguides: v_p > c is possible, but v_g < c (no information FTL)
```

---

## 8. Law of Sines and Cosines

For triangles that aren't right-angled:

```
  GENERAL TRIANGLE:
          C
         /\
        /  \
     b /    \ a
      /      \
     /_______ \
    A    c     B

  Law of Sines:    a/sin A = b/sin B = c/sin C = 2R   (R = circumradius)

  Law of Cosines:  c² = a² + b² − 2ab cos C
                   (Pythagorean theorem when C = 90°)

  Use Sines when: two angles and a side known (AAS, ASA)
  Use Cosines when: two sides and included angle (SAS), or all three sides (SSS)
```

---

## 9. Complex Numbers — Trig in Disguise

### 9.1 Rectangular and Polar Forms

```
  z = a + bi               rectangular form
  z = r e^(iθ)             polar form
  z = r(cos θ + i sin θ)   polar expanded

  r = |z| = √(a² + b²)    modulus
  θ = arg(z) = atan2(b, a) argument

  Conjugate: z* = a − bi = r e^(-iθ)
  |z|² = z · z* = a² + b²
```

### 9.2 Operations in Polar Form

```
  Multiplication: z₁z₂ = r₁r₂ e^(i(θ₁+θ₂))    multiply moduli, add angles
  Division:       z₁/z₂ = (r₁/r₂) e^(i(θ₁−θ₂)) divide moduli, subtract angles
  Powers:         zⁿ = rⁿ e^(inθ)               De Moivre's theorem
  Roots:          z^(1/n) = r^(1/n) e^(i(θ+2πk)/n)  n roots for k = 0,1,...,n−1

  De Moivre's theorem:
  (cos θ + i sin θ)ⁿ = cos(nθ) + i sin(nθ)

  Useful for: deriving multiple-angle formulas without memorization
  e.g., cos 3θ = Re[(e^iθ)³] = Re[e^(3iθ)] = cos³θ − 3cosθ sin²θ
```

### 9.3 Roots of Unity

```
  Solutions to zⁿ = 1:
  z_k = e^(2πik/n)   for k = 0, 1, ..., n−1

  These are evenly spaced around the unit circle at angles 2π/n apart.

  n=2: {1, -1}
  n=4: {1, i, -1, -i}
  n=8: {e^(iπk/4) for k=0..7} ← the DFT is built on 8th/Nth roots of unity

  DISCRETE FOURIER TRANSFORM = projection onto roots of unity.
  The FFT is an efficient algorithm for computing these projections.
```

---

## 10. Fourier Series — The Payoff of Orthogonality

The orthogonality integrals in §6.2 are not just computational tools — they
say that {1, cos θ, sin θ, cos 2θ, sin 2θ, ...} forms an orthonormal basis
for L²([0, 2π]), the Hilbert space of square-integrable functions on the circle.

**The Fourier series** of f ∈ L²([0, 2π]):

```
  f(θ) = a₀/2 + Σ (aₙ cos nθ + bₙ sin nθ)
                n=1

  Coefficients (L² inner products with the basis elements):

  a₀ = (1/π) ∫₀²π f(θ) dθ
  aₙ = (1/π) ∫₀²π f(θ) cos(nθ) dθ    n ≥ 1
  bₙ = (1/π) ∫₀²π f(θ) sin(nθ) dθ    n ≥ 1

  Complex form (cleaner for computation):
  f(θ) = Σ cₙ e^(inθ)    where cₙ = (1/2π) ∫₀²π f(θ) e^(-inθ) dθ
          n∈ℤ
```

**L² convergence theorem**: For any f ∈ L²([0, 2π]), the Fourier series
converges to f in the L² norm:

```
  ‖f − Sₙ‖₂ → 0  as  n → ∞

  where Sₙ is the nth partial sum. Equivalently (Parseval's identity):

  ∫₀²π |f(θ)|² dθ = π(a₀²/2 + Σ (aₙ² + bₙ²)) = 2π Σ |cₙ|²
```

The coefficients cₙ are the projections of f onto the orthonormal basis
vectors e^(inθ)/√(2π) — exactly the same Gram-Schmidt decomposition you'd
do in any Hilbert space. This is not a physics approximation; it is exact
in L².

**Pointwise convergence** is subtler (Dirichlet kernel, Gibbs phenomenon):

```
  Dirichlet's theorem: if f has one-sided limits and is piecewise smooth,
  the Fourier series converges pointwise to (f(θ⁺) + f(θ⁻))/2 at each point
  — the average of left and right limits.

  Gibbs phenomenon: at a jump discontinuity, the partial sums overshoot by
  ~9% of the jump height, regardless of how many terms are included.
  The overshoot doesn't disappear — it concentrates near the discontinuity.
  This matters for signal processing: Gibbs ringing in bandlimited systems.
```

**Connection to the DFT**: the discrete Fourier transform is exactly the
Fourier series formula applied to a periodic sequence sampled at N evenly
spaced points. The DFT coefficients Cₖ = Σₙ f[n] e^(-2πink/N) are the
discrete analog of cₙ. The FFT computes all N coefficients in O(N log N)
vs the naive O(N²) — this is the single most important algorithm in signal
processing, and its correctness relies on the orthogonality of roots of unity.

In NumPy: `np.fft.fft(x)` computes the DFT; `np.fft.rfft(x)` for real inputs.

---

## 11. Chebyshev Polynomials — Trig Over [-1,1]

The substitution x = cos θ transforms trig functions over [0,π] into
polynomials over [-1,1]:

```
  Tₙ(x) = cos(n arccos x)     ← nth Chebyshev polynomial of the first kind

  T₀(x) = 1
  T₁(x) = x
  T₂(x) = 2x² − 1
  T₃(x) = 4x³ − 3x
  Tₙ₊₁(x) = 2x Tₙ(x) − Tₙ₋₁(x)    ← three-term recurrence
```

**Why Chebyshev polynomials matter** (the equioscillation theorem):
The best degree-n polynomial approximation to f on [-1,1] in the L∞ norm
equioscillates between its extrema at least n+2 times. Chebyshev polynomials
are extremal: |Tₙ(x)| ≤ 1 for x ∈ [-1,1], and Tₙ oscillates between ±1
exactly at n+1 Chebyshev nodes. Consequences:

```
  1. Interpolation at Chebyshev nodes minimizes the maximum interpolation
     error (avoids Runge's phenomenon for high-degree polynomial interpolation).

  2. The Chebyshev basis expands functions with exponential convergence for
     analytic functions on [-1,1] — far faster than the Taylor basis.

  3. Orthogonality: ∫₋₁¹ Tₘ(x)Tₙ(x) / √(1−x²) dx = (π/2) δₘₙ  (m,n > 0)
     This is the trig orthogonality ∫₀π cos(mθ)cos(nθ)dθ under x = cos θ.

  4. Spectral methods (pseudospectral PDE solvers) expand solutions in
     Chebyshev series: scipy.special.chebyt(n) gives the nth polynomial;
     numpy.polynomial.chebyshev.chebval evaluates Chebyshev expansions.
```

The connection: trig orthogonality over [0,π] is exactly polynomial orthogonality
with the Chebyshev weight 1/√(1−x²) over [-1,1]. Fourier series on the circle
and Chebyshev approximation on an interval are the same mathematics.

---

## Connections to Adjacent Mathematics

**Complex analysis.** Over ℂ, sin z and cos z are entire functions (no
singularities in ℂ). Their zeros are exactly at the expected real points:
sin z = 0 at z = nπ, cos z = 0 at z = π/2 + nπ, for n ∈ ℤ. The periodicity
e^(z+2πi) = e^z means the complex exponential is doubly periodic on ℂ (when
extended — this connects to elliptic functions, which are meromorphic functions
with two independent periods, generalizing trig to genus-1 surfaces).

**Representation theory.** The functions e^(inθ) for n ∈ ℤ are the characters
of the irreducible representations of U(1) = S¹ (the circle group). Fourier
series is harmonic analysis on U(1): decomposing L²(S¹) into irreducible
U(1)-representations. This generalizes: for compact groups G, the
Peter-Weyl theorem says L²(G) decomposes into matrix coefficients of
irreducible representations. Fourier analysis on ℝ (using e^(iωt)) is the
non-compact analog, and the irreducible representations of ℝ are exactly
the characters x ↦ e^(iωx) — one for each ω ∈ ℝ.

**Functional analysis.** The Fourier basis {e^(inθ)/√(2π)} is a complete
orthonormal system in L²([0,2π]). Completeness means: if f ∈ L² and all
Fourier coefficients vanish, then f = 0 a.e. The L² theory of Fourier series
is the prototype for spectral theory of self-adjoint operators on Hilbert spaces.

---

## Decision Cheat Sheet

| Need to... | Use... | When condition holds |
|-----------|--------|----------------------|
| Find a value from the unit circle | Memorize the 30-45-60 triangle | — |
| Simplify sin²+cos² expressions | Pythagorean identity | — |
| Expand sin(A±B), cos(A±B) | Angle addition formulas | — |
| Integrate sin² or cos² | Half-angle identities | — |
| Multiply two sinusoids | Product-to-sum formulas | — |
| Add two nearly-equal sinusoids | Sum-to-product → beats | ω₁ ≈ ω₂ |
| Represent AC signals algebraically | Phasors via Euler's formula | Fixed ω |
| Decompose periodic function into frequencies | Fourier series | f ∈ L²([0,2π]) |
| Best polynomial approximation on interval | Chebyshev polynomials | x ∈ [-1,1] |
| Solve a general triangle | Law of sines or cosines | — |
| Work with exponential decay + oscillation | Hyperbolic trig | Evanescent fields |
| Take roots/powers of complex numbers | De Moivre's theorem | — |
| Evaluate trig at complex argument | Entire function extension | z ∈ ℂ |

---

## Common Confusion Points

**"Radians vs degrees — does it matter?"**
Always use radians in calculus and physics. The derivative d/dx sin(x) = cos(x) is only true in radians. In degrees: d/dx sin(x°) = (π/180) cos(x°). The Taylor series and Euler's formula require radians.

**"Why does cos differentiate to −sin but sin differentiates to +cos?"**
Think geometrically. At θ=0, sin is at its minimum slope: cos(0) = 1 (rising). At θ=π/2, sin is at its peak — zero slope: cos(π/2) = 0. Cos at θ=0 is at its peak — zero slope: -sin(0) = 0. Cos starts decreasing: -sin(π/6) = -1/2 (negative, consistent with cos decreasing).

**"Is arctan(y/x) the same as atan2(y, x)?"**
No. arctan(y/x) loses quadrant information — it only returns (-π/2, π/2). atan2(y, x) returns the full (-π, π] range. In code: always use atan2. In physics: be careful about which quadrant your angle lives in.

**"What's the difference between phase velocity and group velocity?"**
Phase velocity is how fast the crests of a single frequency move. Group velocity is how fast a pulse (a packet of frequencies) moves — this is what carries information and energy. In free space EM waves, they're equal. In dispersive media (glass, waveguides), they differ.

**"I keep confusing sinh and sin."**
The real difference: sin oscillates (bounded between ±1), sinh grows without bound. At small x: sinh x ≈ x ≈ sin x (both start linear). For large x: sinh x ≈ e^x /2 (exponential growth). The Pythagorean identity: sin²+cos²=1 (circle), cosh²−sinh²=1 (hyperbola, minus sign!).

**"Does the Fourier series converge to f everywhere?"**
L² convergence: yes, the series converges in the L² norm to f (for any f ∈ L²).
Pointwise convergence: at points where f is smooth, yes. At jump discontinuities,
the series converges to the average of left and right limits, and exhibits Gibbs
overshoot near the jump. For continuous f with absolutely convergent Fourier
coefficients (Σ|cₙ| < ∞), the convergence is uniform.

*Next: `mathematics/04-POWER-SERIES.md` — Taylor, Maclaurin, radius of convergence, asymptotic expansion, the generating functions that connect everything.*
