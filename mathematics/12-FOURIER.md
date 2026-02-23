# 12 — Fourier Analysis

```
FOURIER LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  Time domain f(t)  ←────────────────────────────────►  Frequency domain F(ω)
                          Fourier Transform pair

  ┌──────────────────────────────────────────────────────────────────────┐
  │  FOURIER SERIES         periodic f(t)  →  discrete spectrum         │
  │  FOURIER TRANSFORM      aperiodic f(t) →  continuous spectrum       │
  │  DTFT                   discrete-time sequence → continuous ω       │
  │  DFT / FFT              finite sequence → finite spectrum           │
  │  STFT / Wavelet         time-varying spectra                        │
  └──────────────────────────────────────────────────────────────────────┘

  Central unity:
    e^(iωt) = cos(ωt) + i·sin(ωt)    ← complex exponentials are eigenfunctions
    of all LTI systems.  Every signal is a superposition of them.

  Physics connections:
    Maxwell: plane waves e^(i(k·x-ωt))       Heat eq: Fourier series solution
    QM: momentum eigenstate e^(ipx/ℏ)         Heisenberg: Δx·Δp ≥ ℏ/2
    Optics: diffraction = 2D Fourier transform

  6.003 bridge:  H(jω) = CTFT of impulse response h(t)
```

---

## 1. Fourier Series

### Setup: Periodic Functions on [-L, L]

```
  f(t) with period 2L:  f(t + 2L) = f(t)

  Decompose as sum of harmonics (orthogonal basis):

    f(t) = a₀/2 + Σₙ₌₁^∞ [aₙ cos(nπt/L) + bₙ sin(nπt/L)]

  Coefficients (inner products with basis functions):
    a₀ = (1/L) ∫₋ₗᴸ f(t) dt                    ← DC component (mean)
    aₙ = (1/L) ∫₋ₗᴸ f(t) cos(nπt/L) dt
    bₙ = (1/L) ∫₋ₗᴸ f(t) sin(nπt/L) dt
```

### Complex Exponential Form

```
  f(t) = Σₙ₌₋∞^∞ cₙ e^(inπt/L)

  cₙ = (1/2L) ∫₋ₗᴸ f(t) e^(-inπt/L) dt

  Relationship:  c₀ = a₀/2,   cₙ = (aₙ - ibₙ)/2,   c₋ₙ = (aₙ + ibₙ)/2
  For real f(t): c₋ₙ = cₙ*   (Hermitian symmetry)
```

### Standard Period 2π (ω₀ = 1)

```
  f(θ) = Σₙ cₙ e^(inθ)

  cₙ = (1/2π) ∫₋π^π f(θ) e^(-inθ) dθ
```

### Orthogonality — Why It Works

```
  ⟨e^(imθ), e^(inθ)⟩ = (1/2π) ∫₋π^π e^(imθ) e^(-inθ) dθ = δₘₙ

  The complex exponentials {e^(inθ)} form an orthonormal basis for L²([−π,π]).
  Fourier coefficients are just projections onto basis vectors.
  This is the spectral theorem (06-LINEAR-ALGEBRA) applied to infinite dimensions.
```

### Convergence

```
  Pointwise: converges to f(t) if f is smooth (C¹ piecewise)
  At jump discontinuity: converges to [f(t⁺) + f(t⁻)]/2
  Gibbs phenomenon: 9% overshoot near jump, persists as N → ∞

  L² convergence: ||f - Σₙ₌₋ₙᴺ cₙ e^(inθ)||₂ → 0
    (energy is preserved: Parseval's theorem)
```

### Parseval's Theorem

```
  (1/2π) ∫|f(θ)|² dθ = Σₙ |cₙ|²

  Energy in time domain = Energy in frequency domain.
  Fundamental conservation law underlying all signal processing.
```

### Classic Fourier Series Examples

| f(t) on [-π,π] | Fourier series | Key insight |
|---|---|---|
| Square wave (±1) | (4/π)Σ sin((2k-1)t)/(2k-1) | Odd harmonics only |
| Triangle wave | (8/π²)Σ (-1)^((k-1)/2) sin((2k-1)t)/(2k-1)² | Faster decay (smoother) |
| Sawtooth | (2/π)Σ (-1)^(n+1) sin(nt)/n | All harmonics |
| Dirac comb Σ δ(t-2πk) | (1/2π)Σ e^(int) | All harmonics equal amplitude |

**Rule of thumb**: Smoothness ↔ decay rate. If f is Cᵏ, then cₙ = O(1/|n|^(k+1)).

---

## 2. Continuous Fourier Transform (CTFT)

### Definition

```
  Forward:  F(ω) = ∫₋∞^∞ f(t) e^(-iωt) dt        (analysis)
  Inverse:  f(t) = (1/2π) ∫₋∞^∞ F(ω) e^(iωt) dω   (synthesis)

  Alternative convention (symmetric):
    F(ν) = ∫ f(t) e^(-2πiνt) dt    (ν in Hz, not rad/s)
    f(t) = ∫ F(ν) e^(2πiνt) dν     (no 1/2π factor)

  Engineering convention:
    F(f) = ∫ f(t) e^(-2πift) dt
    The two conventions differ by where 2π lands.
```

### Key Properties

```
  Linearity:       af + bg  ←→  aF + bG

  Time shift:      f(t-t₀) ←→  e^(-iωt₀) F(ω)      (phase shift)
  Freq shift:      e^(iω₀t) f(t) ←→ F(ω-ω₀)        (modulation)

  Scaling:         f(at) ←→ (1/|a|) F(ω/a)          (uncertainty principle)

  Convolution:     (f*g)(t) = ∫f(τ)g(t-τ)dτ ←→ F(ω)·G(ω)
                   f(t)·g(t) ←→ (1/2π)(F*G)(ω)

  Differentiation: f'(t)    ←→ iω F(ω)
                   (-it)f(t) ←→ F'(ω)
  Integration:     ∫f dτ    ←→ F(ω)/(iω) + πF(0)δ(ω)

  Parseval:        ∫|f(t)|² dt = (1/2π)∫|F(ω)|² dω

  Duality:         F{F(t)}(ω) = 2πf(-ω)
```

### Transform Table

| f(t) | F(ω) | Notes |
|---|---|---|
| δ(t) | 1 | Dirac delta → flat spectrum |
| 1 | 2πδ(ω) | DC → impulse at ω=0 |
| e^(-at)u(t), a>0 | 1/(a+iω) | Decaying exponential |
| e^(-a|t|) | 2a/(a²+ω²) | Two-sided exponential |
| e^(-t²/2) | √(2π)e^(-ω²/2) | Gaussian → Gaussian |
| rect(t) | sinc(ω/2) = sin(ω/2)/(ω/2) | Box → sinc |
| sinc(t) | π·rect(ω/2) | Sinc → box |
| cos(ω₀t) | π[δ(ω-ω₀) + δ(ω+ω₀)] | Cosine → two spikes |
| sin(ω₀t) | iπ[δ(ω+ω₀) - δ(ω-ω₀)] | Sine → two spikes |
| e^(iω₀t) | 2πδ(ω-ω₀) | Complex exponential → spike |
| Σ δ(t-nT) | (2π/T)Σ δ(ω-2πk/T) | Dirac comb → Dirac comb |

**Gaussian transforms to Gaussian**: this is the only function that maps to itself under Fourier transform (up to scaling). It's the ground state of the harmonic oscillator.

---

## 3. Uncertainty Principle

```
  The time-bandwidth product has a fundamental lower bound:

    Δt · Δω ≥ 1/2

  where:
    Δt² = (1/||f||²) ∫ t² |f(t)|² dt       (RMS time spread)
    Δω² = (1/||F||²) ∫ ω² |F(ω)|² dω       (RMS bandwidth)

  Equality iff f(t) = Ae^(-t²/2σ²) e^(iω₀t)   (Gaussian envelope)

  Physics:  Δx · Δp ≥ ℏ/2   is just this theorem with p = ℏk
    The wavefunction ψ(x) and its Fourier transform φ(k) = ψ̃(k)
    cannot both be arbitrarily narrow.

  Engineering implication:
    Short pulses require large bandwidth.
    "On for 1 ns" pulse needs ~1 GHz bandwidth.
    Sharp filters in frequency ↔ long ringing in time.
    You cannot localize in both time and frequency simultaneously.
```

---

## 4. Sampling Theorem (Nyquist-Shannon)

```
  f(t) is bandlimited: F(ω) = 0 for |ω| > ω_max = 2πB  (B in Hz)

  Nyquist sampling theorem:
    Sample at rate fₛ ≥ 2B (Nyquist rate).
    f(t) is exactly reconstructable from samples {f(nT)}, T = 1/fₛ.

  Reconstruction:
    f(t) = Σₙ f(nT) · sinc(π(t-nT)/T)     (sinc interpolation)

  Aliasing (what goes wrong at fₛ < 2B):
    Frequency components above fₛ/2 fold back into [0, fₛ/2].
    Alias of ω_sig appears at ω_alias = |ω_sig - k·ω_s|  for integer k.

  ┌──────────────────────────────────────────────────────────────────┐
  │  Proof sketch via Dirac comb:                                    │
  │  Sampling = multiply by Σ δ(t-nT)                               │
  │  Fourier of Dirac comb = (ωₛ)·Σ δ(ω - kωₛ)                     │
  │  Sampled spectrum = (1/T) Σₖ F(ω - kωₛ)  (periodic replicas)   │
  │  If B < fₛ/2: replicas don't overlap → recoverable by LPF       │
  │  If B ≥ fₛ/2: replicas overlap = aliasing = information loss    │
  └──────────────────────────────────────────────────────────────────┘
```

---

## 5. Discrete Fourier Transform (DFT)

### Definition

```
  Input: N-point sequence x[n], n = 0, 1, ..., N-1
  Output: N-point sequence X[k], k = 0, 1, ..., N-1

  Analysis:   X[k] = Σₙ₌₀^(N-1) x[n] W_N^(nk)     where W_N = e^(-2πi/N)
  Synthesis:  x[n] = (1/N) Σₖ₌₀^(N-1) X[k] W_N^(-nk)

  Frequency bin k corresponds to analog frequency ω = 2πk/(NT) = 2πk·fₛ/N
  Frequency resolution = fₛ/N  (improves with more samples N)
```

### DFT as Matrix Multiplication

```
  X = F_N · x    where (F_N)_{kn} = W_N^(kn)

  F_N is unitary (up to scale 1/√N).
  DFT = projection onto orthogonal basis {e^(2πikn/N)}_{k=0}^{N-1}

  Direct computation: O(N²)
  FFT: O(N log N)
```

### DFT Properties

```
  Periodicity:  X[k+N] = X[k],   x[n+N] = x[n]    (circular arithmetic)
  Conjugate symmetry: X[N-k] = X[k]* for real x[n]
  Circular convolution: x[n]⊛y[n] ↔ X[k]·Y[k]
  Parseval: Σ|x[n]|² = (1/N) Σ|X[k]|²
```

### Spectral Leakage and Windowing

```
  Analyzing finite segment of infinite signal → implicit rectangular window.
  Rect window has high sidelobes in spectrum (sinc sidelobes at -13 dB first).
  Non-integer frequency → energy "leaks" into adjacent bins.

  Windowing: multiply by w[n] before DFT to shape spectrum.

  Window comparison:
  ┌────────────────┬─────────────┬────────────────┬───────────────────────┐
  │ Window         │ Main lobe   │ Peak sidelobe  │ Rolloff               │
  ├────────────────┼─────────────┼────────────────┼───────────────────────┤
  │ Rectangular    │ 4π/N wide   │ −13 dB         │ −20 dB/decade         │
  │ Hann           │ 8π/N        │ −31 dB         │ −60 dB/decade         │
  │ Hamming        │ 8π/N        │ −41 dB         │ −20 dB/decade         │
  │ Blackman       │ 12π/N       │ −57 dB         │ −18 dB/decade         │
  │ Flat-top       │ 20π/N       │ −93 dB         │ Poor                  │
  └────────────────┴─────────────┴────────────────┴───────────────────────┘

  Trade-off: Narrow main lobe (frequency resolution) vs low sidelobes (dynamic range)
  Hann: good general purpose
  Flat-top: accurate amplitude measurement
  Blackman-Harris: highest sidelobe suppression
```

---

## 6. Fast Fourier Transform (FFT)

### Cooley-Tukey Algorithm

```
  Insight: N-point DFT of x[n] splits into two N/2-point DFTs.

  Split into even/odd:
    X[k] = Σₙ₌₀^(N/2-1) x[2n] W_N^(2nk) + Σₙ₌₀^(N/2-1) x[2n+1] W_N^((2n+1)k)
          = Σₙ x[2n] W_{N/2}^(nk) + W_N^k · Σₙ x[2n+1] W_{N/2}^(nk)
          = E[k] + W_N^k · O[k]        (butterfly operation)

  For k < N/2:    X[k] = E[k] + W_N^k · O[k]
  For k ≥ N/2:    X[k] = E[k-N/2] - W_N^k · O[k-N/2]   (twiddle factor)

  Recursion to N=1 (trivial DFT).
  Complexity: T(N) = 2T(N/2) + N  →  O(N log N)    (Master Theorem Case 2)

  Radix-2 requires N = 2^m.
  Mixed-radix (3, 5, 7...): works for any N but more complex.
  Prime-length: Rader/Bluestein algorithms.
```

### FFT in Practice

```
  FFTW ("Fastest Fourier Transform in the West"): plans optimal factorization.
  NumPy/SciPy: np.fft.fft, scipy.fft.fft
  GPU FFT: cuFFT, millions of transforms in parallel.

  Zero-padding: pad x[n] with zeros before FFT → denser sampling of DTFT.
    Does NOT improve frequency resolution (information hasn't changed).
    Does interpolate existing bins → smoother plot.

  Overlap-add / overlap-save: efficient block processing via FFT convolution.
  Real FFT: if x[n] real, only N/2+1 unique outputs needed.
```

---

## 7. Short-Time Fourier Transform (STFT)

```
  Problem: FT is global — can't locate when a frequency occurs.

  STFT:  X(τ, ω) = ∫ f(t) w(t-τ) e^(-iωt) dt

  Slide window w(t) along t, compute FT at each position τ.

  Spectrogram: |X(τ,ω)|²   — power at each (time, frequency) point.
  Displayed as colormap: x=time, y=frequency, color=power.

  Time-frequency resolution trade-off (uncertainty principle):
    Wide window → good frequency resolution, poor time resolution
    Narrow window → good time resolution, poor frequency resolution
    Resolution box: Δt · Δω ≥ 1/2  (fixed area)

  Fixed resolution everywhere — limitation of STFT.
```

### Wavelet Transform

```
  Wavelets overcome the fixed-resolution limitation.

  Continuous WT:  W(a,b) = (1/√|a|) ∫ f(t) ψ*((t-b)/a) dt
    a = scale (~ 1/frequency),   b = translation (time position)

  Dyadic WT: a = 2^j, b = k·2^j  (octave scales, integer shifts)

  Key property: Multi-resolution analysis (MRA)
    Coarse scales: see global structure (low freq)
    Fine scales: see fine detail (high freq)
    → Constant relative bandwidth: Δω/ω = const

  Applications:
    Signal denoising (threshold wavelet coefficients)
    JPEG-2000 (wavelet-based image compression)
    Seismic analysis, ECG, audio compression (MP3 uses wavelet-like MDCT)
    Multirate filter banks (polyphase decomposition ↔ wavelet)
```

---

## 8. 2D Fourier Transform

### Definition

```
  F(u,v) = ∫∫ f(x,y) e^(-i2π(ux+vy)) dx dy

  f(x,y) = ∫∫ F(u,v) e^(+i2π(ux+vy)) du dv

  Separable: if f(x,y) = g(x)h(y), then F(u,v) = G(u)H(v)

  2D DFT:
    F[k,l] = ΣₘΣₙ f[m,n] W_M^(mk) W_N^(nl)
    Separable → row-wise 1D FFT, then column-wise 1D FFT
    Total: O(MN log(MN))
```

### 2D Properties

```
  Rotation: f rotated by θ ←→ F rotated by θ
  Projection-slice theorem:
    1D FT of a projection of f at angle θ
    = slice through F at angle θ
    → Basis of CT reconstruction (filtered backprojection)

  2D convolution: (f*g)(x,y) ←→ F(u,v)·G(u,v)
    → Convolution theorem works in 2D
    → Implement 2D convolution via 2D FFT for large kernels
```

### k-Space in MRI

```
  MRI measures Fourier transform of spin density directly in k-space.

  k = (γ/2π) ∫₀ᵗ G(τ) dτ    (k-space position determined by gradient history)

  Image = 2D inverse FT of k-space.

  Sampling strategies:
    Cartesian: row by row (standard)
    Radial: spoke by spoke (motion-robust)
    Spiral: efficient but requires gradient system

  Undersampling (compressed sensing MRI):
    ρ(x) = argmin ||ρ||₁ subject to F(ρ) measured = data
    Sparsity in wavelet domain allows 10× undersampling.
```

### Diffraction as Fourier Transform

```
  Far-field (Fraunhofer) diffraction pattern U(x,y) at distance D:

    U(u,v) ∝ ∫∫ A(x,y) e^(-i2π(xu+yv)/λD) dx dy

  = Fourier transform of aperture function A(x,y)!

  Telescope resolution: circular aperture A = circle of diameter d
    FT of circle = Airy disk  (first zero at 1.22λ/d)
    Rayleigh criterion: resolve two objects separated by 1.22λ/d
```

---

## 9. Connections to Physics and Engineering

```
  Heat equation (07-DIFFEQ):
    ∂u/∂t = α ∂²u/∂x²

    FT in x: d/dt Û(k,t) = -αk² Û(k,t)
    Û(k,t) = Û(k,0) e^(-αk²t)    → exponential decay per mode
    High-k (fine structure) decays faster.
    u(x,t) = ∫ Û(k,0) e^(-αk²t) e^(ikx) dk

  Wave equation:
    ∂²u/∂t² = c² ∂²u/∂x²
    FT: d²/dt² Û(k,t) = -c²k² Û   →  Û = A e^(±ickt)
    Dispersion relation: ω = ck

  Schrödinger equation:
    iℏ ∂ψ/∂t = -ℏ²/(2m) ∂²ψ/∂x² + V(x)ψ
    FT: ψ̃(p) = FT of ψ(x)  (momentum space wavefunction)
    ⟨x⟩ = ∫x|ψ|²dx,   ⟨p⟩ = ∫p|ψ̃|²dp   (Born rule)

  Convolution theorem ↔ LTI systems (6.003):
    y(t) = (h * x)(t)  →  Y(ω) = H(ω)·X(ω)
    Transfer function H(ω) = FT of impulse response h(t)
    Filter design = shaping H(ω)
```

---

## 10. Decision Cheat Sheet

| Situation | Tool | Notes |
|---|---|---|
| Periodic function, continuous time | Fourier series | Discrete spectrum |
| Aperiodic function, continuous time | CTFT | Continuous spectrum |
| Finite sequence | DFT / FFT | O(N log N), circular |
| Need spectrum + time localization | STFT | Fixed Δt·Δω box |
| Multi-resolution (coarse+fine) | Wavelet | Constant relative bandwidth |
| 2D image analysis / filtering | 2D FFT | Separate FFT on rows then columns |
| MRI reconstruction | Inverse 2D FFT of k-space | Projection-slice theorem |
| Spectral leakage in DFT | Apply window (Hann, Blackman) | Trades resolution for sidelobe level |
| Convolution large arrays | Multiply via FFT → IFFT | O(N log N) vs O(N²) |
| Differentiation in PDE | Multiply by iω in FT domain | Diagonalizes ∂/∂x |
| Accuracy of amplitude measurement | Flat-top window | Wide lobe but accurate amplitude |

---

## 11. Common Confusion Points

**1. DFT assumes periodicity**
The DFT treats x[n] as one period of an infinite periodic sequence. Time-aliasing occurs if the signal isn't periodic in the window — circular wraparound effects. This is distinct from spectral aliasing. Zero-padding helps avoid time-aliasing artifacts.

**2. Zero-padding improves interpolation, not resolution**
Adding zeros before DFT gives more frequency bins but doesn't reveal new frequencies. True spectral resolution requires more data, not more zeros. Padding is just interpolation of the underlying DTFT.

**3. The 2π placement is a convention choice**
Three common conventions:  (ω-convention: factor 1/2π on synthesis), (symmetric: 1/√2π on both), (ν-convention: no 2π factors). Pick one and stick to it within a calculation. Mixing conventions produces wrong results.

**4. Negative frequencies are real**
For real-valued signals, X(-ω) = X(ω)* (conjugate symmetry). Negative frequencies are not redundant "copies" — they're required for the real signal representation. Complex exponentials e^(iωt) need both +ω and -ω to produce a real cosine.

**5. Uncertainty principle limits compression**
You cannot design a window that is simultaneously short in time AND narrow in frequency. This is mathematical, not an engineering limitation. The Gabor limit Δt·Δω = 1/2 (Gaussian) is the optimal bound.

**6. Wavelet vs STFT: what's actually different**
STFT: fixed window width → fixed Δt and Δω everywhere.
WT: narrow window at high frequencies (short wavelets), wide window at low frequencies (long wavelets). Same Δω/ω ratio everywhere. This gives better time localization of transients at high frequencies, where you need it.
