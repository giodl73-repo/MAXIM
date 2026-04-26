# 13 — Laplace Transform & Control

```
LAPLACE LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  Time domain f(t)  ←────────────────────────────────►  s-domain F(s)
   t ≥ 0, ICs included                                   s = σ + iω ∈ ℂ

  ┌─────────────────────────────────────────────────────────────────────┐
  │  Fourier Transform:  ω real, works when f(t) has finite energy      │
  │  Laplace Transform:  s = σ+iω complex, works for growing signals    │
  │                      Encodes initial conditions automatically       │
  │                      Turns ODEs → algebraic equations in s          │
  └─────────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────────┐
  │                    s-plane geometry                                   │
  │                                                                       │
  │    iω ↑                                                               │
  │       │  ×  ×  ×  │  poles here = oscillation                         │
  │       │            │                                                  │
  │  ─────┼────────────┼───────→ σ                                        │
  │       │            │                                                  │
  │  Left half-plane   │  Right half-plane                                │
  │  σ < 0: STABLE     │  σ > 0: UNSTABLE                                │
  │                                                                       │
  │  Imaginary axis = Fourier (set σ=0 in F(s) → get H(jω))             │
  └───────────────────────────────────────────────────────────────────────┘

  Applications:
    Circuit analysis → impedance Z(s), transfer functions
    Control systems → stability, Bode plots, PID design
    6.003 bridge: H(s) in s-domain ↔ H(jω) frequency response
```

---

## 1. Definition and Region of Convergence

### Bilateral Laplace Transform and the Fourier Bridge

The bilateral (two-sided) Laplace transform is the general form:

```
  F(s) = ∫_{-∞}^{∞} f(t) e^{-st} dt      s = σ + iω ∈ ℂ

  ROC of bilateral transform: a vertical strip {s : σ₁ < Re(s) < σ₂}
  — not a half-plane, but a strip between two abscissas of convergence.

  The Fourier transform is bilateral Laplace restricted to the imaginary axis:
    F(iω) = ∫_{-∞}^{∞} f(t) e^{-iωt} dt   (set σ = 0 in the bilateral form)

  This is exact, not analogical. The Fourier transform exists iff the ROC
  includes the imaginary axis (σ = 0 is in the convergence strip).

  Causality vs. stability are separate concerns in the bilateral picture:
    Causal f(t) (supported on t ≥ 0): ROC is {σ > σ_min} (right half-plane)
    Anti-causal: ROC is {σ < σ_max} (left half-plane)
    Two-sided (non-causal): ROC is a strip σ₁ < σ < σ₂
    If ROC strip contains σ = 0, Fourier transform exists.
    A causal signal with all poles in LHP has ROC {σ > max pole Re} ⊃ {σ > 0}
    — includes the imaginary axis, so both Fourier and Laplace exist.
```

The one-sided (unilateral) transform is the engineering workhorse for causal
systems with initial conditions:

### One-Sided (Unilateral) Laplace Transform

```
  F(s) = ℒ{f(t)} = ∫₀^∞ f(t) e^(-st) dt    s = σ + iω ∈ ℂ

  Inverse:
  f(t) = ℒ⁻¹{F(s)} = (1/2πi) ∫_{σ-i∞}^{σ+i∞} F(s) e^(st) ds   (Bromwich integral)

  In practice: use partial fractions + table lookup, not direct integration.
  The Bromwich integral is evaluated by residue theorem (14-COMPLEX-ANALYSIS).
```

### Connection to Probability — Moment Generating Functions

```
  The bilateral Laplace transform of a probability density f_X(x) is
  exactly the moment generating function:

    M_X(t) = E[e^{tX}] = ∫_{-∞}^{∞} e^{tx} f_X(x) dx = ℒ{f_X}(-t)

  MGF = bilateral Laplace at s = -t.

  Consequences:
    Derivatives of M_X at 0 give moments: M_X^(n)(0) = E[X^n]
    For independent X,Y: M_{X+Y}(t) = M_X(t)·M_Y(t)
      ← corresponds to convolution theorem for Laplace
    Cumulant generating function: K_X(t) = log M_X(t)
      K_X'(0) = E[X],  K_X''(0) = Var(X),  K_X'''(0) = third cumulant
    Lévy-Khintchine formula: K_X(t) = iμt - σ²t²/2 + ∫(e^{itx}-1-itx/(1+x²))ν(dx)
    characterizes all infinitely divisible distributions (Poisson, Gaussian, stable)
    via the Lévy measure ν.

  The characteristic function φ_X(t) = E[e^{itX}] = M_X(it) is the bilateral
  Laplace evaluated on the imaginary axis — same as the Fourier transform of f_X.
  It always exists (unlike MGF, which may not for heavy-tailed distributions).
```

### Region of Convergence (ROC)

```
  The integral ∫₀^∞ f(t) e^(-st) dt converges only for certain s values.
  ROC = {s ∈ ℂ : ℜ(s) > σ_min}   (right half-plane from some σ_min)

  For f(t) = e^(at):
    F(s) = 1/(s-a),  ROC: σ > a  (pole at s=a, excluded from ROC)

  For f(t) = e^(-at) (a > 0):
    F(s) = 1/(s+a),  ROC: σ > -a
    On jω axis (σ=0 > -a): F(jω) = 1/(a+jω)  ← Fourier transform exists

  If all poles in left half-plane:
    ROC includes jω axis → Fourier transform = F(jω) = F(s)|_{s=jω}
    Causally stable systems: H(jω) is just H(s) evaluated on imaginary axis.
```

---

## 2. Transform Table

| f(t), t ≥ 0 | F(s) | Notes |
|---|---|---|
| δ(t) | 1 | Impulse |
| u(t) | 1/s | Step |
| t | 1/s² | Ramp |
| tⁿ | n!/s^(n+1) | Polynomial |
| e^(at) | 1/(s-a) | Exponential |
| sin(ωt) | ω/(s²+ω²) | Sine |
| cos(ωt) | s/(s²+ω²) | Cosine |
| e^(at)sin(ωt) | ω/((s-a)²+ω²) | Damped sine |
| e^(at)cos(ωt) | (s-a)/((s-a)²+ω²) | Damped cosine |
| t e^(at) | 1/(s-a)² | Repeated pole |
| tⁿ e^(at) | n!/(s-a)^(n+1) | Order-n pole |
| u(t-a) (delayed step) | e^(-as)/s | Time delay |
| f(t-a)u(t-a) | e^(-as)F(s) | Any delayed function |

---

## 3. Properties

```
  Linearity:       af + bg  ←→  aF + bG

  Time shift:      f(t-a)u(t-a) ←→ e^(-as)F(s)      (causal delay)
  Freq shift:      e^(at)f(t)   ←→ F(s-a)            (modulation)

  Differentiation:
    f'(t)    ←→ sF(s) - f(0⁻)              ← initial condition appears!
    f''(t)   ←→ s²F(s) - sf(0⁻) - f'(0⁻)
    f^(n)(t) ←→ sⁿF(s) - sⁿ⁻¹f(0⁻) - ... - f^(n-1)(0⁻)

  Integration:     ∫₀ᵗ f(τ)dτ ←→ F(s)/s

  Convolution:     (f*g)(t) ←→ F(s)·G(s)             (same as Fourier)

  Initial value:   lim_{t→0+} f(t) = lim_{s→∞} sF(s)
  Final value:     lim_{t→∞} f(t)  = lim_{s→0} sF(s)  (only if limit exists)

  Scaling:         f(at) ←→ (1/a)F(s/a)
```

---

## 4. Solving ODEs with Initial Conditions

```
  Standard ODE:
    y'' + 5y' + 6y = u(t),    y(0) = 1,  y'(0) = -1

  Take Laplace transform:
    [s²Y - sy(0) - y'(0)] + 5[sY - y(0)] + 6Y = 1/s

    s²Y - s·1 - (-1) + 5(sY - 1) + 6Y = 1/s
    (s² + 5s + 6)Y = 1/s + s + 1 - 1 + 5
    (s² + 5s + 6)Y = 1/s + s + 4

    Y(s) = 1/[s(s²+5s+6)] + (s+4)/(s²+5s+6)
         = 1/[s(s+2)(s+3)] + (s+4)/[(s+2)(s+3)]

  Partial fraction decomposition then table lookup → y(t).
  Initial conditions encoded automatically in the s-domain equation.
```

### Partial Fractions

```
  Y(s) = N(s)/D(s)   where deg(N) < deg(D)

  Simple real poles s = pₖ:
    Y(s) = Σₖ Aₖ/(s - pₖ)
    Aₖ = (s - pₖ)Y(s)|_{s=pₖ}    (residue at pₖ)

  Repeated pole s = p of order m:
    Y(s) = A₁/(s-p) + A₂/(s-p)² + ... + Aₘ/(s-p)ᵐ
    Aₖ = (1/(m-k)!) · d^(m-k)/ds^(m-k) [(s-p)ᵐ Y(s)]|_{s=p}

  Complex conjugate pair s = α ± jβ:
    Y(s) = (As + B)/((s-α)² + β²)
    → e^(αt)[C·cos(βt) + D·sin(βt)]   in time domain
```

---

## 5. Transfer Functions and LTI Systems

```
  LTI system: Y(s) = H(s)·X(s)    (zero initial conditions)

  Transfer function:  H(s) = Y(s)/X(s) = output/input in s-domain

  Physical meaning:
    H(s) = ℒ{h(t)}   where h(t) = impulse response
    y(t) = h(t)*x(t)  →  Y(s) = H(s)X(s)   (convolution theorem)

  General form:
    H(s) = K · Πᵢ(s - zᵢ) / Πⱼ(s - pⱼ)
    zᵢ = zeros of H(s)    (frequency inputs that produce zero output)
    pⱼ = poles of H(s)    (natural frequencies of the system)

  Stability:
    BIBO stable iff all poles in LHP: ℜ(pⱼ) < 0 for all j
    Marginally stable: poles on jω axis (oscillates forever)
    Unstable: any pole with ℜ(p) > 0

  Frequency response (from transfer function):
    H(jω) = H(s)|_{s=jω}    (only valid if ROC includes jω axis)
    = magnitude |H(jω)| and phase ∠H(jω) = Bode plot data
```

### RLC Circuit Example

```
  Series RLC:  Ldi/dt + Ri + (1/C)∫i dt = v_in(t)
  Take Laplace (zero ICs):
    (Ls + R + 1/(Cs))I(s) = V_in(s)
    Z(s) = Ls + R + 1/(Cs)    ← impedance in s-domain

  H(s) = I(s)/V_in(s) = 1/Z(s) = Cs/(LCs² + RCs + 1)

  Poles at s = -R/(2L) ± √[(R/2L)² - 1/LC]
    Underdamped (R small): complex poles near jω₀ → oscillation at ω₀ = 1/√LC
    Critically damped: poles coincide at -R/2L
    Overdamped: two real negative poles
```

---

## 6. Bode Plots

### Concept

```
  Bode plot = log-log frequency response of H(jω)
    Magnitude: 20 log₁₀|H(jω)| in dB vs log ω
    Phase: ∠H(jω) in degrees vs log ω

  Key insight: log converts multiplication to addition.
    H(jω) = H₁(jω)·H₂(jω)···
    20 log|H| = 20 log|H₁| + 20 log|H₂| + ...
    → Add individual Bode plots graphically.
```

### Building Blocks

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │  1. Constant K:                                                     │
  │     Mag: 20 log|K| dB (flat line)    Phase: 0° or ±180°             │
  │                                                                     │
  │  2. Pole at origin 1/s:                                             │
  │     Mag: -20 dB/decade    Phase: -90° (constant)                    │
  │                                                                     │
  │  3. Simple real pole 1/(1 + s/ωₚ):                                  │
  │     Low ω: 0 dB, 0°                                                 │
  │     High ω: -20 dB/decade, -90°                                     │
  │     At ω = ωₚ (corner freq): -3 dB, -45°                            │
  │                                                                     │
  │  4. Simple real zero (1 + s/ωz):                                    │
  │     Same but +20 dB/decade, +90°                                    │
  │                                                                     │
  │  5. Complex conjugate pair 1/(s² + 2ζω₀s + ω₀²):                    │
  │     Resonance peak at ω₀, height 1/2ζ                               │
  │     -40 dB/decade above ω₀                                          │
  │     Phase swings -180° through ω₀                                   │
  └─────────────────────────────────────────────────────────────────────┘
```

### Reading a Bode Plot

```
  Slope tells you system order in each frequency region.
  -20 dB/decade per pole, +20 dB/decade per zero.
  Phase slope: -90°/decade per pole in high-freq region.

  Gain crossover ωgc: |H(jωgc)| = 1 (0 dB)
  Phase margin PM = 180° + ∠H(jωgc)
    PM > 0° → stable closed loop
    PM > 45° → well-damped response

  Phase crossover ωpc: ∠H(jωpc) = -180°
  Gain margin GM = 1/|H(jωpc)|  in dB: GM = -20 log|H(jωpc)|
    GM > 0 dB → stable

  GM > 10 dB, PM > 45°: typical design targets for robust stability
```

---

## 7. PID Control

```
  Plant G(s). Controller C(s). Unity negative feedback.

  Open-loop: L(s) = C(s)·G(s)
  Closed-loop: T(s) = L(s)/(1 + L(s))   (input→output)
  Sensitivity: S(s) = 1/(1 + L(s))       (disturbance rejection)

  PID controller:
    u(t) = Kₚ·e(t) + Kᵢ∫e(t)dt + Kd·de/dt

    C(s) = Kₚ + Kᵢ/s + Kd·s = (Kd·s² + Kₚ·s + Kᵢ)/s

    P action:  proportional to error → reduces steady-state error
    I action:  integrates error → eliminates steady-state error (type 1 system)
    D action:  derivative → damps overshoot, improves transient

  Tuning: Ziegler-Nichols (experimental), pole placement, IMC design.

  Issues:
    Derivative kick: D term amplifies noise (use filtered derivative Kd·s/(τs+1))
    Integral windup: integrator saturates during large errors (add anti-windup)
    D term in some controllers only on output, not error (avoids setpoint kick)
```

### Nyquist Stability Criterion

The Nyquist criterion connects complex analysis (winding numbers / argument
principle) directly to feedback stability:

```
  Setup: closed-loop system with open-loop L(s) = C(s)G(s).
  Question: how many closed-loop poles are in the RHP?

  Argument principle: if F(s) is meromorphic, as s traverses a closed contour
  Γ clockwise, F(s) encircles the origin N = Z - P times clockwise,
  where Z = zeros and P = poles of F inside Γ.

  Nyquist contour Γ: indented semicircle enclosing the entire RHP (jω axis
  from -j∞ to +j∞, semicircle at ∞, small indentations around jω-axis poles).

  Apply argument principle to F(s) = 1 + L(s):
    Closed-loop poles = zeros of 1 + L(s).
    Poles of 1 + L(s) = poles of L(s) (open-loop poles).
    Clockwise encirclements of -1 by L(jω) as ω goes from -∞ to +∞:
      N = Z_RHP_closed - P_RHP_open
    Stable closed loop: Z_RHP_closed = 0
      → N = -P_RHP_open  (counterclockwise encirclements = # open-loop RHP poles)

  ┌─────────────────────────────────────────────────────────────────────┐
  │  Nyquist stability criterion:                                       │
  │  Closed-loop is stable iff the Nyquist plot of L(jω)                │
  │  encircles −1 exactly P times counterclockwise,                     │
  │  where P = number of open-loop RHP poles.                           │
  │                                                                     │
  │  For open-loop stable L(s) (P=0): closed-loop stable iff            │
  │  Nyquist plot does NOT encircle −1 at all.                          │
  └─────────────────────────────────────────────────────────────────────┘

  Connection to margins:
    Phase margin = how much additional phase lag before −1 is encircled.
    Gain margin = how much gain increase before −1 is encircled.
    These are not just numerical targets — they're distances to instability
    on the Nyquist plot.

  Routh-Hurwitz: algebraic test (polynomial coefficients) for LHP roots.
    All coefficients of char. poly. aₙsⁿ+...+a₀ must be positive (necessary).
    Routh array: systematic test for sufficient conditions.
    Useful when you have an explicit characteristic polynomial and no plot.
```

---

## 8. z-Transform — Discrete-Time Counterpart

### Definition and the Sampling Derivation

The z-transform is not analogical to Laplace — it is the exact Laplace
transform of a sampled (impulse-train) signal:

```
  Sampling: x_s(t) = x(t) · Σₙ δ(t - nT) = Σₙ x[n] δ(t - nT)

  Laplace transform of x_s(t):
    X_s(s) = ∫ x_s(t) e^{-st} dt = Σₙ x[n] e^{-snT}

  Define z = e^{sT}:
    X(z) = Σₙ x[n] z^{-n}   ← the z-transform

  The substitution z = e^{sT} is exact, not an approximation.
  Every z-domain property follows from this derivation:

  s-plane → z-plane mapping via z = e^{sT}:
  ┌─────────────────────┬──────────────────────────────────────────┐
  │  s-plane region     │  z-plane image                           │
  ├─────────────────────┼──────────────────────────────────────────┤
  │  Left half-plane    │  Inside unit circle |z| < 1             │
  │  σ < 0              │  |e^{σT}| = e^{σT} < 1 since σ < 0     │
  │  Right half-plane   │  Outside unit circle |z| > 1            │
  │  Imaginary axis     │  Unit circle |z| = 1                    │
  │  σ = 0, s = jω      │  z = e^{jωT} — unit circle traversal    │
  └─────────────────────┴──────────────────────────────────────────┘

  Stability: poles inside unit circle ← not an analogy, it's the same
  condition "poles in LHP" mapped through z = e^{sT}.

  Analog prototype to digital filter conversion:
    Impulse invariant: match h[n] = h(nT) at sample points.
      Direct: zₖ = e^{pₖT} maps s-poles to z-poles exactly.
      Problem: aliasing if H(s) is not bandlimited.

    Bilinear transform (Tustin): s = (2/T)(z-1)/(z+1)
      Exact mapping that takes the entire jω axis bijectively onto the unit circle.
      No aliasing, but frequency warping: ω_analog = (2/T)tan(ω_digital·T/2)
      Requires pre-warping the critical frequencies before designing the prototype.
```

### Region of Convergence (z-domain)

```
  For causal sequences: ROC = {|z| > r} for some r
  For anti-causal: ROC = {|z| < r}
  Stable causal system: ROC includes unit circle, all poles inside unit circle.
```

### z-Transform Properties and Table

| x[n] | X(z) | ROC |
|---|---|---|
| δ[n] | 1 | All z |
| u[n] | 1/(1-z⁻¹) = z/(z-1) | | z | > 1 |
| aⁿ u[n] | 1/(1-az⁻¹) = z/(z-a) | | z | > | a | |
| n·aⁿ u[n] | az⁻¹/(1-az⁻¹)² | | z | > | a | |
| cos(ω₀n)u[n] | (1-cos(ω₀)z⁻¹)/(1-2cos(ω₀)z⁻¹+z⁻²) | | z | > 1 |
| sin(ω₀n)u[n] | sin(ω₀)z⁻¹/(1-2cos(ω₀)z⁻¹+z⁻²) | | z | > 1 |

```
  Delay: x[n-k] ←→ z^(-k)X(z)
  Convolution: x[n]*h[n] ←→ X(z)H(z)
  Difference equation: same role as s in Laplace for ODEs
```

### Difference Equations → z-Domain

```
  Σₖ aₖ y[n-k] = Σₖ bₖ x[n-k]    (difference equation)

  z-transform:   (Σₖ aₖ z^(-k)) Y(z) = (Σₖ bₖ z^(-k)) X(z)

  H(z) = Y(z)/X(z) = Σbₖ z^(-k) / Σaₖ z^(-k)   = B(z)/A(z)

  Poles and zeros at roots of A(z) and B(z).
  Stability: all poles inside unit circle.
  Frequency response: H(e^(jω)) = H(z)|_{z=e^(jω)}
```

---

## 9. Laplace vs Fourier vs z

```
  ┌─────────────────┬──────────────────────────────────────────────────┐
  │                 │ Tool                                             │
  ├─────────────────┼───────────┬───────────┬──────────────────────────┤
  │ Domain          │ Fourier   │ Laplace   │ z-transform              │
  ├─────────────────┼───────────┼───────────┼──────────────────────────┤
  │ Time            │ Continuous│ Continuous│ Discrete                 │
  │ Domain variable │ ω ∈ ℝ     │ s ∈ ℂ     │ z ∈ ℂ                    │
  │ Stability axis  │ ω axis    │ jω axis   │ Unit circle              │
  │ Stable region   │ N/A       │ LHP       │ Inside unit circle       │
  │ ICs handled?    │ No        │ Yes       │ Yes                      │
  │ Convergence     │ Need L²   │ Any growth│ Any causal               │
  │ Physical use    │ Spectra   │ Circuits, │ Digital filters, DSP     │
  │                 │ PDEs      │ control   │                          │
  └─────────────────┴───────────┴───────────┴──────────────────────────┘

  Unified picture:
    s = σ + jω   (continuous)
    z = e^(sT)   (sampled version — exact, not approximate)
    ω real: Fourier (s on imaginary axis = Laplace with σ=0)

  DTFT: let z = e^(jω) in z-transform → frequency response of discrete system.
  DFT: sample DTFT at N equally spaced frequencies → FFT computable.
```

---

## 10. Impedance Method — Circuits in s-Domain

```
  Resistor:    Z_R(s) = R
  Capacitor:   Z_C(s) = 1/(sC)     [→ 1/(jωC) for sinusoidal steady-state]
  Inductor:    Z_L(s) = sL         [→ jωL]

  Replace every element with impedance.
  Solve using KVL, KCL, voltage divider — purely algebraic.
  Result is H(s) = V_out(s)/V_in(s) directly.

  Example — Low-Pass RC:
    H(s) = [1/(sC)] / [R + 1/(sC)] = 1/(1 + sRC) = 1/(1 + s/ω_c)
    ω_c = 1/(RC)  [rad/s]   corner frequency
    f_c = 1/(2πRC) [Hz]
    |H(jω)| = 1/√(1 + (ω/ω_c)²)
    At ω = ω_c: |H| = 1/√2 = -3.01 dB (the "3dB frequency")
    Phase: ∠H(jω) = -arctan(ω/ω_c)   → -45° at ω_c
```

---

## 11. Decision Cheat Sheet

| Need to... | Use |
|---|---|
| Solve ODE with ICs, get time response | Laplace, partial fractions, table |
| Analyze steady-state sinusoidal response | H(jω) = H(s) | _{s=jω} (Bode) |
| Design a filter for continuous circuit | H(s) poles/zeros, then realize as RLC/op-amp |
| Check stability of continuous system | Routh-Hurwitz or: all poles in LHP? |
| Check stability with loop gain known | Nyquist criterion: encirclements of -1 |
| Design digital filter | z-transform, poles inside unit circle |
| Analyze sampling and aliasing | z = e^(sT), unit circle = Nyquist |
| Understand frequency shaping | Bode plots — slopes reveal pole/zero structure |
| Model signal flow through LTI system | Transfer function H(s) or H(z) |
| Convert analog prototype to digital | Bilinear transform: s = 2(z-1)/[T(z+1)] |
| Find DC gain | H(0) (s→0) or H(1) (z→1, z-domain DC) |
| Find bandwidth | Frequency where | H(jω) | drops to -3 dB |
| Tune feedback controller | PM and GM from Bode, then adjust C(s) |
| Compute E[X^n] of a distribution | MGF: M_X^(n)(0) = E[X^n] = bilateral Laplace at -t |

---

## 12. Common Confusion Points

**1. Laplace ≠ Fourier — they're related but not the same**
Setting s = jω works only when the ROC includes the imaginary axis (all poles in LHP). If a system is unstable, H(s) exists in the RHP but H(jω) doesn't — can't just substitute jω. For stable causal systems, H(jω) = H(s)|_{s=jω} is valid and gives the sinusoidal frequency response.

**2. Left half-plane = stable, but "left" is for s-domain**
In z-domain, stability means poles inside the unit circle |z| < 1. This is because z = e^(sT): LHP (σ < 0) maps to |z| = e^(σT) < 1. Applying LHP intuition to z-domain directly is wrong.

**3. The final value theorem has conditions**
lim_{t→∞} f(t) = lim_{s→0} sF(s) only if all poles of sF(s) are in the LHP. If the system is oscillating or unstable, the final value theorem gives a meaningless answer. Always check pole locations first.

**4. Bode asymptotes are approximations**
The straight-line Bode sketches are asymptotic approximations. At corner frequencies, the actual magnitude differs by exactly 3 dB (for simple poles/zeros), not by the asymptote jump. Phase is also not a step function — it spans a decade below to a decade above the corner frequency.

**5. z^(-1) means "one sample delay"**
In z-domain: z^(-1) is a unit delay operator, not a fraction. H(z) = z^(-1) means the output is the input delayed by one sample T seconds. This is the fundamental building block of all digital filters: difference equations are the z-domain analog of differential equations.

**6. Bilinear transform warps frequency**
Converting analog filter H(s) to digital via s = 2(z-1)/[T(z+1)] (Tustin's method) introduces frequency warping: ω_digital = (2/T)arctan(ω_analog·T/2). The analog cutoff ωc should be pre-warped: ωc_analog = (2/T)tan(ωc_digital·T/2) before designing the prototype. This is called pre-warping and must be done to get the specified digital cutoff.

**7. Bilateral vs unilateral Laplace — which ROC is a strip vs half-plane**
The unilateral (one-sided, causal) transform always has ROC = right half-plane {σ > σ_min}. The bilateral transform has ROC = a strip {σ₁ < σ < σ₂}. The Fourier transform exists iff σ = 0 is inside the bilateral ROC. Stability (ROC containing the jω axis) and causality (support on t ≥ 0) are separate properties that happen to coincide for stable causal systems.
