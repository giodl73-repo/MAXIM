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

## Decision Cheat Sheet

| Need to... | Use... |
|-----------|--------|
| Find a value from the unit circle | Memorize the 30-45-60 triangle |
| Simplify sin²+cos² expressions | Pythagorean identity |
| Expand sin(A±B), cos(A±B) | Angle addition formulas |
| Integrate sin² or cos² | Half-angle identities |
| Multiply two sinusoids | Product-to-sum formulas |
| Add two nearly-equal sinusoids | Sum-to-product → beats |
| Represent AC signals algebraically | Phasors via Euler's formula |
| Solve a general triangle | Law of sines or cosines |
| Work with exponential decay + oscillation | Hyperbolic trig |
| Take roots/powers of complex numbers | De Moivre's theorem |
| Build Fourier / Laplace intuitively | Orthogonality + Euler |

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

---

*Next: `mathematics/04-POWER-SERIES.md` — Taylor, Maclaurin, radius of convergence, asymptotic expansion, the generating functions that connect everything.*
