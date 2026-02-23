# 05 — Signals & Systems (6.003 Refresher)

```
SIGNALS & SYSTEMS LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  SIGNALS                    SYSTEMS                  ANALYSIS DOMAINS
  ─────────────────────────  ──────────────────────   ────────────────────────
  Continuous: x(t)           Linear Time-Invariant    Time: convolution y=h*x
  Discrete: x[n]             (LTI) systems            Frequency: Y(ω)=H(ω)X(ω)
  Periodic, aperiodic        Non-LTI: nonlinear or    s-domain: Y(s)=H(s)X(s)
  Energy, power signals      time-varying             z-domain (discrete)
  Even/odd, complex                                   State space: ẋ=Ax+Bu

  LTI systems are characterized completely by their impulse response h(t):
    y(t) = h(t) * x(t) = ∫ h(τ)x(t-τ)dτ   (convolution)

  Fourier/Laplace transforms convert convolution → multiplication.
  This is the central insight of signals & systems.

  6.003 bridge: This IS 6.003. The module is a structured refresher.
```

---

## 1. Signal Classification

```
  Continuous-time (CT): x(t), t ∈ ℝ   (e.g., voltage from microphone)
  Discrete-time (DT): x[n], n ∈ ℤ     (e.g., sampled audio, 44100 Hz)

  Periodic:  x(t+T) = x(t) for all t    T = fundamental period
             x[n+N] = x[n] for all n    N = fundamental period

  Energy signal:   E = ∫|x(t)|² dt < ∞    (finite energy, e.g., pulse)
  Power signal:    P = lim_{T→∞} (1/2T)∫_{-T}^{T}|x(t)|² dt < ∞
                   (finite average power, e.g., periodic signal, infinite energy)

  Even:  x(-t) = x(t)     symmetric about t=0   (cosine, |t|)
  Odd:   x(-t) = -x(t)    antisymmetric         (sine, t)
  Any signal = even part + odd part:
    x_e(t) = [x(t)+x(-t)]/2,   x_o(t) = [x(t)-x(-t)]/2
```

### Key Signals

| Signal | Definition | Fourier |
|---|---|---|
| δ(t) | Dirac delta (sifting: ∫f(t)δ(t-t₀)dt = f(t₀)) | 1 |
| u(t) | Unit step (0 for t<0, 1 for t≥0) | πδ(ω) + 1/(jω) |
| e^(jω₀t) | Complex exponential | 2πδ(ω-ω₀) |
| rect(t/T) | Rectangular pulse (1 for |t|<T/2) | T·sinc(ωT/2) |
| sinc(t) = sin(πt)/(πt) | Sinc function | rect(ω/2π) |
| e^(-at)u(t) | Decaying exponential | 1/(a+jω) |
| Σ δ(t-nT) | Dirac comb | (2π/T)Σ δ(ω-k·2π/T) |
| δ[n] | Unit impulse (1 at n=0, else 0) | 1 |
| u[n] | Unit step (1 for n≥0) | e^(jω)/(e^(jω)-1) |
| a^n u[n] | Discrete exponential | 1/(1-ae^(-jω)) for |a|<1 |

---

## 2. LTI Systems — Definition and Properties

```
  Linearity: T{ax₁+bx₂} = aT{x₁} + bT{x₂}
  Time-invariance: if y(t) = T{x(t)}, then y(t-t₀) = T{x(t-t₀)}

  Why LTI is special:
    Linear + TI → completely characterized by impulse response h(t).
    Input-output: y(t) = h(t) * x(t)
    This is the convolution integral.

  Causality: h(t) = 0 for t < 0   (output depends only on past inputs)
  Stability (BIBO): ∫|h(t)|dt < ∞  (bounded input → bounded output)
    In s-domain: all poles of H(s) in left half-plane.

  Memoryless: h(t) = c·δ(t) (instantaneous output)
  Dynamic: h(t) has non-zero duration → integrator, resonator, etc.
```

---

## 3. Convolution

### Continuous-Time

```
  y(t) = x(t) * h(t) = ∫_{-∞}^∞ x(τ) h(t-τ) dτ

  How to compute graphically:
    1. Reflect h(τ) → h(-τ)
    2. Slide h(-τ) right by t → h(t-τ)
    3. Multiply x(τ) · h(t-τ), integrate over τ
    4. Result is y(t) for that specific t value
    5. Repeat for all t

  Properties:
    Commutative: x*h = h*x
    Associative: (x*h₁)*h₂ = x*(h₁*h₂)
    Distributive: x*(h₁+h₂) = x*h₁ + x*h₂

  Important: h₁*h₂ is cascade connection of two systems.
    Cascade order doesn't matter for LTI (commutative).
```

### Discrete-Time

```
  y[n] = x[n]*h[n] = Σₖ x[k]h[n-k]   (sum instead of integral)

  For finite-length sequences: FIR (finite impulse response)
    h[n] has finite duration N → convolution sum has N terms
    Length of y = length of x + length of h - 1
    Efficiently computed via FFT for large N.
```

---

## 4. Fourier Transform in Systems Analysis

### Frequency Response

```
  For LTI system with impulse response h(t):
    H(jω) = ∫ h(t) e^(-jωt) dt   (Fourier transform of h(t))

  H(jω) = frequency response = transfer function on jω axis.

  Input-output in frequency domain:
    Y(jω) = H(jω) · X(jω)    (multiplication, not convolution!)

  |H(jω)| = magnitude response (gain vs frequency)
  ∠H(jω) = phase response    (phase shift vs frequency)

  Ideal LPF:  H(jω) = rect(ω/2ω_c)  (1 for |ω|<ω_c, 0 otherwise)
    h(t) = ω_c/π · sinc(ω_c t/π)    (sinc function — non-causal!)
    Non-causal → can't be realized exactly → always approximate.
```

### Group Delay

```
  Group delay: τ(ω) = -d∠H(jω)/dω

  Physical meaning: time delay experienced by a narrow-band signal at frequency ω.
  Constant group delay → all frequencies delayed equally → shape preserved.

  Linear phase: ∠H(jω) = -ωt_0  →  τ = t_0 (constant)
    FIR filters can have exact linear phase (symmetric coefficients).
    IIR filters cannot (poles introduce phase nonlinearity).
```

---

## 5. Laplace Transform in Systems Analysis (CT)

```
  H(s) = ∫ h(t) e^(-st) dt  (Laplace of impulse response)
  Y(s) = H(s) X(s)

  Pole-zero plot:
    H(s) = K·Π(s-zᵢ)/Π(s-pⱼ)
    Zeros zᵢ: frequencies where H=0 (input blocked)
    Poles pⱼ: natural frequencies (resonances, instabilities)

  Reading the pole-zero plot:
    |H(jω)|: product of distances from zeros / product of distances from poles
    ∠H(jω): sum of angles to zeros - sum of angles to poles

  Real poles: exponential modes (stable if in LHP)
  Complex conjugate poles: damped sinusoidal modes (stable if in LHP)
  Poles on jω axis: sustained oscillation (marginally stable)
  Poles in RHP: growing, unstable
```

---

## 6. Sampling — Bridge Between CT and DT

```
  x[n] = x(nT)   (ideal sampling)
  fₛ = 1/T = sampling rate

  Nyquist-Shannon: reconstruct x(t) from x[n] iff fₛ ≥ 2·f_max

  Sampled spectrum (periodic replicas at multiples of ωₛ):
    X_s(jω) = (1/T) Σₖ X(j(ω - kωₛ))   where ωₛ = 2π/T

  Anti-aliasing filter: LPF with ωc = ωₛ/2 applied before sampling.
    Removes any components that would alias.
    Real ADCs always need anti-aliasing; sometimes integrated on-chip.

  Reconstruction: LPF with ωc = ωₛ/2 applied to DAC output.
    Removes spectral replicas.
    Real DACs always need reconstruction filter (smoothing).

  Oversampling:
    Sample at kfₛ (k > 1). Noise spreads over wider band → lower in-band noise.
    Sigma-delta ADC: oversample by 64–512×, digital filter+decimate.
    Allows lower precision analog components.
```

---

## 7. Z-Transform (Discrete-Time Systems)

```
  For DT LTI:
    H(z) = Σₙ h[n] z^(-n)   (z-transform of impulse response)
    Y(z) = H(z) X(z)

  Frequency response: H(e^(jω)) = H(z)|_{z=e^(jω)}
    DTFT evaluated on unit circle.

  Stability: all poles of H(z) inside unit circle (|pole| < 1)
  Causal: h[n] = 0 for n < 0

  Difference equations ↔ H(z):
    y[n] + a₁y[n-1] + ... = b₀x[n] + b₁x[n-1] + ...
    H(z) = (b₀ + b₁z⁻¹ + ...) / (1 + a₁z⁻¹ + ...)

  FIR: all poles at z=0 (or no poles). Always stable.
  IIR: poles at other locations. Can be unstable.
```

---

## 8. State-Space Representation

### Continuous-Time

```
  ẋ(t) = A·x(t) + B·u(t)      state equation
  y(t) = C·x(t) + D·u(t)      output equation

  x ∈ ℝⁿ: state vector (n = system order)
  u ∈ ℝᵐ: input vector
  y ∈ ℝᵖ: output vector
  A: n×n, B: n×m, C: p×n, D: p×m

  Transfer function from state space:
    H(s) = C(sI-A)⁻¹B + D

  Eigenvalues of A = poles of H(s) = natural frequencies.
  Stable iff all eigenvalues of A have negative real parts.

  Solution:
    x(t) = e^(At)x(0) + ∫₀ᵗ e^(A(t-τ))B·u(τ)dτ
    Matrix exponential e^(At) = Σₖ (At)^k/k!
```

### Discrete-Time

```
  x[n+1] = A·x[n] + B·u[n]
  y[n]   = C·x[n] + D·u[n]

  Solution: x[n] = Aⁿx[0] + Σₖ₌₀^(n-1) A^(n-1-k)B·u[k]

  Stability: all eigenvalues of A inside unit circle.
  Discretization of CT system: A_d = e^(AT), B_d = (e^(AT)-I)A⁻¹B
    (exact if input held constant between samples)
```

### Why State Space?

```
  Transfer function:  scalar, single-input single-output, hides internal state
  State space:        multi-input multi-output (MIMO), reveals internal structure
    Controllability: can we reach any state from any initial state with inputs?
      Controllable iff rank([B AB A²B ... A^(n-1)B]) = n
    Observability: can we determine initial state from outputs?
      Observable iff rank([C CA CA² ... CA^(n-1)]ᵀ) = n

  State-space = modern control theory. Transfer functions = classical control.
  Modern control: LQR, Kalman filter (optimal observer), H∞ (robust control).
```

---

## 9. Interconnected Systems

```
  ┌───────────────────────────────────────────────────────────────────┐
  │  Series (cascade):  H = H₁ · H₂   (multiply transfer functions)  │
  │                                                                    │
  │  Parallel:  H = H₁ + H₂   (add transfer functions)               │
  │                                                                    │
  │  Feedback:                                                         │
  │         E = X - Y·B                                               │
  │         Y = E·A                                                   │
  │         Y = A·X/(1+AB)   (closed-loop TF)                        │
  │                                                                    │
  │  Control loop:                                                     │
  │    R ──►(Σ)──►[C(s)]──►[G(s)]──► Y                               │
  │          ↑─────────────────────┘                                  │
  │                                                                    │
  │    Closed-loop: T = CG/(1+CG)                                     │
  │    Sensitivity: S = 1/(1+CG)   (disturbance rejection)           │
  └───────────────────────────────────────────────────────────────────┘
```

---

## 10. Decision Cheat Sheet

| Situation | Tool |
|---|---|
| Find output of LTI to arbitrary input | Convolution y(t) = h(t)*x(t) |
| Find frequency response | H(jω) = FT of h(t) |
| Find system with ICs | Laplace Y(s) = H(s)X(s) + IC terms |
| Design stable analog filter | Poles of H(s) in LHP |
| Design stable digital filter | Poles of H(z) inside unit circle |
| Verify linear phase (no distortion) | Check FIR symmetry → linear phase |
| Find natural frequencies | Eigenvalues of A (state space) |
| MIMO system, multiple I/O | State-space representation |
| Sample/reconstruct correctly | fₛ ≥ 2·f_max, anti-aliasing filter |
| Represent simple DT filter | Difference equation ↔ H(z) |
| Analyze control loop stability | Phase margin from loop gain bode plot |

---

## 11. Common Confusion Points

**1. LTI ≠ all systems; most interesting ones are not LTI**
Anything with nonlinearity (saturation, transistors, diodes) or time-varying behavior (time-multiplexed, LTV) is not LTI. The convolution theorem only works for LTI. Superposition only applies to linear systems. When in doubt: is the system both linear (scaling + superposition) and time-invariant (shift input → shift output)?

**2. Convolution is not multiplication (in time domain)**
y(t) = h(t)·x(t) is wrong. y(t) = h(t)*x(t) (convolution) is right. In frequency domain, multiplication is correct: Y(ω) = H(ω)·X(ω). The transform swaps the operations. This confusion causes errors in filter analysis.

**3. BIBO stability: poles in LHP, not just stable-looking poles**
A pole at s = -0.001 is technically stable but gives a time constant τ = 1000 seconds. Whether this is "practically stable" depends on application. Also: BIBO stability requires ALL poles in LHP — even one in RHP makes it unstable regardless of the others.

**4. Sampling rate must exceed twice the highest frequency in the signal**
Common error: thinking fₛ ≥ f_max. Correct: fₛ ≥ 2·f_max. The factor of 2 comes from both positive and negative frequency components needing separation. Audio CD: f_max = 20 kHz → fₛ = 44.1 kHz (slightly above 40 kHz with margin for anti-aliasing filter roll-off).

**5. Group delay, not phase, determines signal distortion**
A filter with constant phase shift at all frequencies does distort (it advances/delays all frequencies equally in phase, but that's fine for certain applications). What matters for pulse distortion is group delay τ(ω) = -d∠H/dω. If group delay varies with frequency, different frequency components arrive at different times → pulse spreading.

**6. State space and transfer function are equivalent only for controllable and observable systems**
H(s) = C(sI-A)⁻¹B + D, but if the system has uncontrollable or unobservable modes, those modes are hidden from the transfer function (pole-zero cancellation). Two systems with same H(s) can have different state trajectories if one has hidden unstable modes. This is why "pole-zero cancellation for stability" is dangerous.
