# 06 — Digital Signal Processing

```
DSP LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  Discrete-time, finite precision arithmetic signal processing.

  FILTER TYPES          DESIGN METHODS          IMPLEMENTATION
  ──────────────────    ──────────────────────  ────────────────────────
  FIR: MA model         Window method           Direct form I/II
    No poles, stable    Frequency sampling      Cascade of 2nd-order
    Linear phase        Parks-McClellan         Lattice form
  IIR: ARMA model       Bilinear transform      Parallel form
    Poles + zeros       Pole placement          Fixed-point arithmetic
    Smaller order                               Multirate systems
    No linear phase

  Advanced:
    Multirate: decimation, interpolation, polyphase
    Adaptive: LMS, RLS — filter coefficients that learn
    Spectral analysis: STFT, Welch method, Goertzel

  Connects to: 12-FOURIER (z-transform, DTFT), 13-LAPLACE (IIR design)
  6.003 bridge: z-transform, difference equations. DSP extends with implementation.
```

---

## 1. FIR Filters

### Definition

```
  FIR (Finite Impulse Response) filter:
    y[n] = Σₖ₌₀^(N-1) b[k]·x[n-k]    (MA — moving average model)
    H(z) = Σₖ b[k] z^(-k)             (polynomial in z^(-1))

  All poles at z=0 (or infinity) → always stable.
  Impulse response: h[n] = b[n], finite duration N taps.
  N coefficients = N-1 delays = N multipliers, N-1 adders.
```

### Linear Phase

```
  FIR can have exact linear phase if h[n] is symmetric:
    h[n] = ±h[N-1-n]   for n = 0,...,N-1

  Four types:
    Type I:  N odd, symmetric.  Linear phase all ω.
    Type II: N even, symmetric. Zero at ω=π (can't do HPF).
    Type III: N odd, antisymmetric. Zero at ω=0 and ω=π.
    Type IV: N even, antisymmetric. Zero at ω=0.

  Linear phase means constant group delay = (N-1)/2 samples.
  Linear phase preserves pulse shape — critical for data communications.
```

### FIR Design Methods

#### Window Method

```
  1. Specify ideal (brick-wall) frequency response H_d(e^(jω))
  2. Compute ideal impulse response h_d[n] = IDTFT{H_d}
     → h_d[n] = (ω_c/π)·sinc(ω_c·n/π)  for ideal LPF
  3. Truncate and shift: h[n] = h_d[n-(N-1)/2]·w[n]
     → shift by (N-1)/2 to make causal
  4. Apply window w[n] to reduce Gibbs phenomenon

  Common windows:
    Rectangular: δBW = 4π/N, peak sidelobe -13 dB
    Hann:        δBW = 8π/N, peak sidelobe -31 dB
    Hamming:     δBW = 8π/N, peak sidelobe -41 dB
    Blackman:    δBW = 12π/N, peak sidelobe -57 dB
    Kaiser:      adjustable, trade main-lobe width vs sidelobe level
      w[n] = I₀(β√(1-(2n/N-1)²)) / I₀(β)  (modified Bessel function)
      β ≈ 0.1102(A-8.7) for stopband attenuation A dB

  Filter order for Kaiser approximation:
    N ≈ (A - 7.95) / (2.285·Δω)    where Δω = ωs - ωp

  Trade-off: larger N → narrower transition band, longer delay.
```

#### Parks-McClellan (Remez Exchange) — Optimal Equiripple FIR

```
  Finds FIR with equiripple error in specified frequency bands.
  Minimizes maximum error (Chebyshev sense) over all frequencies.
  Optimal for given N, transition band, passband/stopband ripple spec.

  Input: filter specifications (ωp, ωs, δp, δs)
  Output: h[n] coefficients
  Algorithm: iterative exchange of extremal frequencies.

  Roughly 30% fewer taps than Kaiser window for same spec.
  The standard choice for production FIR filter design.
  Implemented in MATLAB firpm(), Python scipy.signal.remez().
```

---

## 2. IIR Filters

### Definition

```
  IIR (Infinite Impulse Response) filter:
    y[n] = Σₖ bₖ x[n-k] - Σₖ aₖ y[n-k]   (ARMA model, feedback)
    H(z) = B(z)/A(z) = (Σ bₖ z^(-k)) / (1 + Σ aₖ z^(-k))

  Poles at roots of A(z).
  Stable iff all poles inside unit circle.
  Infinite impulse response (decays exponentially for stable filter).
  Fewer coefficients than FIR for same specification.
  Cannot have exact linear phase.
```

### IIR Design via Bilinear Transform

```
  Start with analog prototype H_a(s) (Butterworth, Chebyshev, etc.)
  Apply bilinear transform:
    s = (2/T)·(z-1)/(z+1)    or equivalently  z = (1+sT/2)/(1-sT/2)

  Properties:
    jω axis (stable region boundary) → unit circle
    LHP → inside unit circle (stable → stable)
    No aliasing (unlike impulse invariant method)

  Frequency warping: digital ω_d vs analog ω_a:
    ω_a = (2/T)·tan(ω_d·T/2)    (prewarping)
    ω_d = (2/T)·arctan(ω_a·T/2)

  Pre-warp the critical frequency before designing analog prototype:
    ω_a = (2/T)·tan(ω_d·T/2)
  Then design analog filter at ω_a, apply bilinear transform.
  Result: digital filter with correct response at ω_d.
```

### IIR Direct Form Structures

```
  Direct Form I: straightforward but needs 2(N-1) delay elements.
    y[n] = b₀x[n] + b₁x[n-1] + ... - a₁y[n-1] - ...
    Store: x[n-1],...,x[n-N] AND y[n-1],...,y[n-N]

  Direct Form II (canonical): N delay elements (shared).
    w[n] = x[n] - a₁w[n-1] - a₂w[n-2] - ...
    y[n] = b₀w[n] + b₁w[n-1] + b₂w[n-2] + ...
    Minimum memory but worse numerical behavior than Transposed Form II.

  Transposed Form II: numerically superior.
    Preferred for fixed-point implementations.
    Same N delays, different signal flow → less quantization error accumulation.

  Second-Order Sections (SOS) / Biquad:
    Cascade of 2nd-order (biquad) sections:
    H(z) = K · Π [(b₀ₖ + b₁ₖz⁻¹ + b₂ₖz⁻²)/(1 + a₁ₖz⁻¹ + a₂ₖz⁻²)]
    Best numerical stability — poles and zeros paired near each other.
    Standard representation in scipy.signal, MATLAB.
```

---

## 3. FIR vs IIR Comparison

| Property | FIR | IIR |
|---|---|---|
| Stability | Always stable | Depends on pole locations |
| Linear phase | Yes (symmetric) | No |
| Delay | High (N-1)/2 samples | Lower (for same spec) |
| Order for given spec | High | Low (~5–10× fewer) |
| Arithmetic | Multiply-add only | Adds feedback |
| Numerical sensitivity | Low | Higher (near-unity poles) |
| Design | Window or Parks-McClellan | Bilinear transform from analog |
| Use case | When linear phase required | When low order/delay important |
| Example | Audio EQ, communication | 60 Hz notch filter, audio |

---

## 4. Fixed-Point DSP

```
  Floating-point (IEEE 754): automatic scaling, 32-bit float typical.
  Fixed-point: programmer manages scaling, cheaper hardware.

  Two's complement representation:
    Qm.n format: m integer bits, n fractional bits.
    Q1.15 ("Q15"): 1 sign bit, 15 fractional bits. Range: [-1, 1-2^(-15)].
    Q15 for filter coefficients: |coefficients| must be ≤ 1.
    Scale coefficients to fit: if max coeff = 0.5, shift by 1.

  Quantization effects:
    Coefficient quantization: finite precision → pole/zero locations shift.
    Roundoff noise: arithmetic produces small errors that accumulate.
    Overflow: intermediate results exceed register width → catastrophic.

  Overflow strategies:
    Saturation: clip to max value (better than wrapping for most signals)
    Guard bits: use extra bits for intermediate accumulation
    Block floating point: dynamic scaling per block

  Limit cycles:
    IIR filters can oscillate with constant output even with zero input.
    Due to quantization making recursive computation orbit a cycle.
    Prevent: use magnitude truncation (vs rounding) in feedback path.
    Check: pole magnitude after quantization still < 1?
```

---

## 5. Multirate Signal Processing

### Downsampling (Decimation)

```
  x_D[n] = x[Mn]    (keep every M-th sample)

  Z-transform: X_D(z) = (1/M) Σₖ₌₀^(M-1) X(z^(1/M) W_M^k)
  DTFT:        X_D(e^(jω)) = (1/M) Σₖ X(e^(j(ω-2πk)/M))

  Aliasing occurs if x[n] has energy above ω = π/M.
  Anti-aliasing filter: LPF with ωc ≤ π/M before downsampling.
  Decimation = LPF + downsample (in that order).
```

### Upsampling (Interpolation)

```
  x_U[n] = x[n/M] if n multiple of M, else 0    (insert M-1 zeros between samples)

  DTFT: X_U(e^(jω)) = X(e^(jωM))   (compressed spectrum, copies appear)

  Image rejection filter: LPF with ωc = π/M after upsampling.
  Scales output by M.
  Interpolation = upsample + LPF (in that order).
```

### Polyphase Decomposition

```
  Key computational insight: filter then decimate = polyphase filters then decimate.
  Saves computation by M.

  Decompose H(z) = Σₖ z^(-k) Eₖ(z^M)   (M polyphase components)
  Each Eₖ operates on M-th rate → compute N/M multiplications per output sample.

  Efficient FIR decimator:
    Direct approach: filter at high rate, then decimate. Wasteful.
    Polyphase: M parallel filters at low rate. M× less computation.

  Efficient interpolator:
    Direct: upsample then filter at high rate. Wasteful.
    Polyphase: M parallel filters at low rate, commutator at output. M× less computation.

  Application: sample rate conversion (e.g., 44100 Hz CD → 48000 Hz audio)
    Rational factor M/L: upsample by L, filter, decimate by M. Or polyphase.
```

---

## 6. Spectral Analysis

### Power Spectral Density

```
  PSD S_x(ω) = E[|X(jω)|²] / T   (expected power per unit frequency)

  Periodogram: |X_N(e^(jω))|²/N   (direct FFT of finite data — biased, high variance)

  Welch Method (practical standard):
    1. Divide signal into overlapping segments (50% overlap typical)
    2. Apply window (Hann) to each segment
    3. FFT each segment → periodogram
    4. Average periodograms
    → Reduced variance (more segments = better average)
    → Frequency resolution = fₛ/L where L = segment length
    Trade-off: more averaging (shorter segments) → worse resolution.
```

### Goertzel Algorithm

```
  Compute single DFT bin k from N samples.
  Direct DFT: O(N) complex multiplications per bin, but need all bins.
  FFT: O(N log N) for all bins.
  Goertzel: O(N) for just one bin — efficient when need < log(N) specific bins.

  Recursion:
    y[n] = 2cos(2πk/N)·y[n-1] - y[n-2] + x[n]
    X[k] = y[N] - e^(-j2πk/N)·y[N-1]

  Use case: DTMF tone detection (need only 8 specific frequencies from phone keypad).
```

---

## 7. Adaptive Filters

```
  Filters with time-varying coefficients that adapt to optimize a criterion.

  Setup:
    x[n] = input
    d[n] = desired signal
    y[n] = w[n]ᵀ·x_vec[n]   (filter output)
    e[n] = d[n] - y[n]       (error)
    Update w[n] to minimize E[e²[n]] (mean square error)

  LMS (Least Mean Squares):
    w[n+1] = w[n] + 2μ·e[n]·x_vec[n]
    μ = step size (controls convergence speed vs misadjustment)
    0 < μ < 1/λ_max  for stability  (λ_max = max eigenvalue of R_xx)
    Computational cost: O(N) per sample — simple
    Convergence: slow if eigenvalue spread of R_xx is large

  RLS (Recursive Least Squares):
    Minimizes exact LS criterion (weighted sum of past errors).
    w[n+1] = w[n] + K[n]·e[n]   (Kalman-like gain K[n])
    O(N²) per sample — more expensive but faster convergence
    Good for non-stationary signals.

  Applications:
    Echo cancellation (hands-free phone): model room impulse response
    Noise cancellation: reference noise signal + adaptive subtract
    Equalization (channel inversion in communications)
    System identification: adaptive model → converges to system
    Beamforming: adaptive weights on antenna array
```

---

## 8. Decision Cheat Sheet

| Need... | Use |
|---|---|
| Linear phase filter (pulse fidelity) | FIR (symmetric) |
| Minimum order filter, delay OK | IIR via bilinear transform |
| Simple LPF/HPF/BPF design | Window method FIR |
| Optimal equiripple FIR | Parks-McClellan (remez) |
| Convert analog prototype to digital | Bilinear transform |
| Frequency-accurate digital filter | Pre-warp cutoff before bilinear |
| Efficient decimation/interpolation | Polyphase decomposition |
| PSD estimate from finite data | Welch method |
| Detect specific DFT bins only | Goertzel algorithm |
| Filter adapts to changing signal | LMS or RLS adaptive |
| Echo/noise cancellation | LMS adaptive filter |
| Fixed-point implementation | SOS/biquad, Transposed Direct Form II |
| Check stability of designed IIR | All pole magnitudes < 1 |

---

## 9. Common Confusion Points

**1. FIR linear phase requires exact symmetry**
h[n] = h[N-1-n] exactly. If h[N-1-n] ≠ h[n] (even by quantization), linear phase is lost. In fixed-point: store only (N+1)/2 coefficients for Type I symmetric FIR, compute the rest by symmetry — saves memory and ensures exact symmetry.

**2. Bilinear transform warps all frequencies, not just cutoff**
The bilinear transform maps all of jω axis to unit circle, but not linearly. Low frequencies map nearly linearly, high frequencies compress. Only pre-warping the specified critical frequency gives the correct digital response there. If you need multiple critical frequencies (e.g., both passband edge and stopband edge), you can only exactly map one — the other will shift.

**3. IIR design from analog prototype assumes causal, stable prototype**
Butterworth poles are designed to be in LHP of s-plane (stable). Bilinear transform then puts them inside unit circle (stable z-domain). If you start with an unstable analog prototype, the digital filter is also unstable. The stability mapping is conditional on the analog prototype being stable.

**4. Decimation filter cutoff is π/M, not ωc of original**
If you decimate by M and want to preserve signal below f_s/2 of the new rate, you must filter to π/M (= f_s/(2M)) before decimating. A common error is keeping the original LPF cutoff. The anti-aliasing filter must be designed for the lower rate.

**5. LMS step size μ: too large diverges, too small barely adapts**
There's no single right μ. Rule: μ < 1/(N·P) where N = filter order, P = input power. Normalized LMS (NLMS) adjusts μ by input power automatically: μ_eff = μ/(ε + ||x||²). Use NLMS in practice to handle input level variation.

**6. SOS/biquad representation vs direct form**
Direct form IIR with high-order polynomial A(z) in denominator: near-pole-zero cancellations with finite precision cause massive coefficient sensitivity. SOS avoids this by pairing each pair of poles with nearby zeros into 2nd-order sections. Always use SOS for fixed-point IIR filters of order ≥ 4.
