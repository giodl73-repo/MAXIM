# Signal Processing — Overview

## The Big Picture

Signal processing is the mathematical engineering of information-bearing functions of time (or space).
The field spans two sovereign domains and four signal categories, unified by one fundamental duality.

```
SIGNAL CATEGORIES
═══════════════════════════════════════════════════════════════

    Continuous-time (CT)          Discrete-time (DT)
    ┌─────────────────┐           ┌─────────────────┐
    │   Deterministic │           │   Deterministic │
    │  x(t) = sin(2πft)│          │  x[n] = sin(2πfn)│
    │                 │  sample   │                 │
    │  Closed-form    │  ──────►  │  Finite samples │
    │  representation │           │  in memory      │
    └─────────────────┘           └─────────────────┘
    ┌─────────────────┐           ┌─────────────────┐
    │   Stochastic    │           │   Stochastic    │
    │  x(t) = noise   │           │  x[n] = noisy   │
    │                 │  sample   │  measurements   │
    │  Statistical    │  ──────►  │                 │
    │  description    │           │  PSD, statistics│
    └─────────────────┘           └─────────────────┘
           ▲                              │
           │                              ▼
       Analog world                  Digital world
       (physics, circuits)          (DSPs, computers)
```

---

## The Fundamental Duality

Every signal has two equivalent representations. Choosing the right domain is the central engineering decision.

```
TIME DOMAIN ◄────────────────────────────► FREQUENCY DOMAIN
                    Fourier Transform

  x(t) or x[n]                              X(f) or X[jω]

  ┌────────────┐                            ┌────────────┐
  │ What the   │                            │ What       │
  │ signal     │                            │ frequencies│
  │ looks like │                            │ it contains│
  │ over time  │                            │ and at what│
  │            │                            │ amplitudes │
  └────────────┘                            └────────────┘

  Good for:                                 Good for:
  • Causality / ordering                    • Filter design
  • Difference equations                    • Spectral analysis
  • Convolution (→ multiplication)          • Noise characterization
  • Edge/onset detection                    • Modulation / demodulation
```

The Fourier transform is an **inner product with complex exponentials** — projecting the signal
onto an orthonormal basis of sinusoids. This is linear algebra; the signal space is L²(ℝ) or ℓ²(ℤ).

---

## Signal Taxonomy

```
SIGNALS
├── By time axis
│   ├── Continuous-time (CT) — x(t), t ∈ ℝ
│   │   Tools: ODE theory, Laplace transform (s-domain), CT Fourier transform
│   └── Discrete-time (DT) — x[n], n ∈ ℤ
│       Tools: Difference equations, Z-transform (z-domain), DFT/FFT
│
├── By amplitude
│   ├── Analog — amplitude ∈ ℝ (continuous)
│   └── Digital — amplitude quantized (finite bits)
│
├── By predictability
│   ├── Deterministic — exact mathematical formula exists
│   │   ├── Periodic     — x(t) = x(t+T)  → Fourier series representation
│   │   └── Aperiodic    — finite energy, x(t)→0 as t→±∞
│   └── Stochastic — only statistical description possible
│       ├── Wide-sense stationary (WSS) — mean and autocorrelation shift-invariant
│       └── Non-stationary — statistics vary with time (EEG, speech)
│
└── By energy/power classification
    ├── Energy signal — E = ∫|x(t)|² dt < ∞  (zero average power)
    │   Examples: finite pulses, decaying exponentials
    └── Power signal — P = lim_{T→∞} (1/2T) ∫_{-T}^{T} |x(t)|² dt < ∞
        Examples: periodic signals, random noise processes
```

---

## Transform Landscape

| Signal type | Domain | Transform | Output |
|-------------|--------|-----------|--------|
| CT periodic | Continuous | Fourier Series | Discrete spectral lines cₙ |
| CT aperiodic, energy | Continuous | CT Fourier Transform | Continuous spectrum X(jω) |
| DT aperiodic, finite N | Discrete | DFT / FFT | N complex coefficients X[k] |
| DT aperiodic, infinite | Discrete | DTFT | Continuous periodic spectrum X(e^{jω}) |
| CT causal / one-sided | Continuous | Laplace transform | X(s), s ∈ ℂ |
| DT causal / one-sided | Discrete | Z-transform | X(z), z ∈ ℂ |

**The key relationships:**
- Laplace s-axis (σ+jω): imaginary axis (σ=0) ↔ CT Fourier transform
- Z-plane unit circle (|z|=1) ↔ DT Fourier transform (DTFT)
- DFT = uniformly sampled DTFT at N points on unit circle

---

## The DSP Signal Chain

```
Physics          Anti-alias     ADC               DSP Core           DAC          Reconstruct
  │              Filter (LPF)   │                    │                │            Filter
  │                │            │                    │                │              │
  ▼                ▼            ▼                    ▼                ▼              ▼
[Sound]  ──►  [Remove >fs/2] ─► [Sample]  ──►  [Filter/         [Quantized]  ──► [Smooth]  ──► [Speaker]
[Light]        (prevent        [Quantize]       Transform/        samples out      (remove        [Screen]
[RF]            aliasing)      x[n] ∈ ℤ        Analyze/                          images)        [Antenna]
                               N bits           Synthesize]
                               ADC output       y[n] ∈ ℤ
```

**Rate constraint**: sample rate fs determines max representable frequency = fs/2 (Nyquist).
**Computation**: FFT made real-time DSP possible — O(N log N) vs O(N²) DFT (Cooley-Tukey 1965).

---

## Module Map

```
signal-processing/
│
├── 01-FOURIER-ANALYSIS       The mathematical engine
│       Fourier Series → DFT → FFT; windowing; spectral leakage
│
├── 02-SAMPLING-THEORY        Analog-to-digital boundary
│       Nyquist-Shannon; aliasing; ADC/DAC; sigma-delta
│
├── 03-FILTERS                Frequency shaping
│       FIR vs IIR; filter families (Butterworth/Chebyshev/elliptic); design
│
├── 04-CONVOLUTION-CORRELATION  Core operations
│       Linear convolution; circular; cross-correlation; matched filter
│
├── 05-Z-TRANSFORM            System analysis
│       Poles/zeros; ROC; stability; digital biquad
│
├── 06-STOCHASTIC-SIGNALS     When signals are random
│       PSD; Wiener-Khinchin; noise types (white/1/f/thermal/shot); SNR
│
├── 07-SPECTRAL-ESTIMATION    Measuring frequency from finite data
│       Periodogram; Welch; MUSIC; ESPRIT
│
├── 08-WAVELETS               Time-frequency analysis
│       STFT limits; multiresolution; DWT; JPEG 2000
│
└── 09-APPLICATIONS           Where DSP lives
        Audio; image processing; radar; medical; ML features
```

**Modern extensions not fully covered:** Compressed sensing (sub-Nyquist sampling via L1 minimization, RIP condition — see brief treatment in 02-SAMPLING-THEORY Common Confusion Points). The CNN-as-learned-filter-bank bridge and attention-as-dynamic-filtering are covered in 09-APPLICATIONS under the DSP-to-Deep-Learning correspondence section.

---

## Key Quantities

| Quantity | Symbol | Unit | Notes |
|----------|--------|------|-------|
| Frequency | f | Hz | cycles per second |
| Angular frequency | ω | rad/s | ω = 2πf |
| Normalized frequency | f̂ | cycles/sample | f̂ = f/fs ∈ [0,1) |
| Digital angular frequency | ω̂ | rad/sample | ω̂ = 2πf̂ ∈ [0,2π) |
| Sample rate | fs | Hz | samples per second |
| Nyquist frequency | fN | Hz | fN = fs/2 |
| Signal power | P | W (or dBW) | ∫\|x\|² dt normalized |
| SNR | SNR | dB | 10·log₁₀(Psignal/Pnoise) |

**dB conventions**: power ratios → 10·log₁₀; amplitude ratios → 20·log₁₀ (because P∝A²).

---

## Bridges to Prior Knowledge

| MIT / Azure Background | DSP Equivalent |
|------------------------|----------------|
| Inner product ⟨f,g⟩ in Hilbert space | Fourier coefficient: cₙ = ⟨x(t), e^{jnω₀t}⟩/T |
| Eigenvalue equation Av = λv | Sinusoids are eigenfunctions of LTI: H(e^{jω})e^{jωn} |
| Hilbert space L²(ℝ) | Space of finite-energy signals |
| Linear algebra projection | Spectral analysis as basis decomposition |
| Difference equations (recurrences) | IIR filter implementation |
| Finite state machine with shift register | FIR filter tap-delay line |
| Probability distribution | Power spectral density (energy distribution in frequency) |
| Azure pipeline stages | Signal processing chain (cascade of LTI systems) |
| Poisson process | Shot noise, Poisson spectral statistics |

| CNN convolutional layer | Bank of learned FIR filters (kernel weights = coefficients, backprop = filter optimization) |
| Attention mechanism (transformer) | Dynamic, input-dependent filter: Q·Kᵀ softmax = data-driven spectral shaping |
| Pooling layers | Downsampling (cf. DWT ↓2) |

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Periodic or aperiodic signal? | Fourier Series vs. Fourier Transform |
| Continuous math vs. computable? | CT FT vs. DFT (FFT in practice) |
| Need to reduce noise at certain frequencies? | Filter design (FIR or IIR) |
| Characterize a random/noisy signal? | PSD, Wiener-Khinchin theorem |
| Signal has time-varying frequency? | STFT or wavelet transform |
| Few sinusoids in noise (high resolution)? | MUSIC / ESPRIT subspace methods |
| Need frequency resolution from short record? | Welch / multitaper averaging |
| Long convolution efficiently? | FFT-based overlap-add/overlap-save |

---

## Common Confusion Points

**Discrete-time ≠ digital**: DT means sampled in time; digital adds quantization of amplitude.
Most DSP theory works on DT (infinite precision); real ADCs also quantize → quantization noise.

**Frequency resolution vs. bandwidth**: DFT bin resolution = fs/N Hz/bin.
More samples N → finer frequency resolution. This is independent of signal bandwidth.

**dBFS vs. dBSPL vs. dBm**: Three different reference points.
dBFS = digital full scale (max ADC value = 0 dBFS); dBSPL = acoustic (20 µPa); dBm = RF power (1 mW).

**LTI is the abstraction that makes everything work**: linear + time-invariant → system fully
characterized by impulse response h[n]; output = input ★ h. Any nonlinearity or time-variance
breaks the Fourier / convolution framework. Speech, radar, and biomedical signals often need
special treatment when they're non-stationary.
