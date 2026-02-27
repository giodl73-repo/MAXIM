# Digital Filters — A Layered Guide

## The Big Picture

A digital filter is a discrete-time LTI system that modifies the frequency content of a signal.
All filters are either FIR (finite impulse response) or IIR (infinite impulse response).

```
FILTER TAXONOMY
════════════════════════════════════════════════════════════════════════

                           DIGITAL FILTERS
                                 │
              ┌──────────────────┼──────────────────┐
              │                                     │
             FIR                                   IIR
    (Finite Impulse Response)         (Infinite Impulse Response)
              │                                     │
   h[n] has finite length N             h[n] decays but never ends
   y[n] = Σ bₖ x[n-k]                  y[n] = Σ bₖ x[n-k] + Σ aₖ y[n-k]
   (no feedback)                        (has feedback / recursion)
              │                                     │
   Always stable                        Can be unstable
   Linear phase possible                More efficient (lower order)
   No analog prototype needed           Designed from analog prototypes
              │                                     │
              │             DESIGN METHODS           │
              │                                     │
   • Window method                      • Bilinear transform (BLT)
   • Parks-McClellan (optimal)          • Impulse invariance
   • Frequency sampling                 • Matched Z-transform
```

---

## Frequency Response

Every LTI filter is characterized by its **frequency response** H(e^{jω}) — the complex ratio
of output to input spectrum at each frequency:

```
H(e^{jω}) = |H(e^{jω})| · e^{j∠H(e^{jω})}
              magnitude         phase

MAGNITUDE RESPONSE shapes the amplitude:
  |H| = 1  → passband (signal passes unchanged)
  |H| = 0  → stopband (signal blocked)
  0<|H|<1  → transition band

PHASE RESPONSE determines timing:
  Linear phase: ∠H(e^{jω}) = -αω   (all frequencies delayed same amount)
  Non-linear:   different frequencies delayed differently → phase distortion

FILTER TYPES (magnitude response shape):
  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐
  │    LPF     │  │    HPF     │  │    BPF     │  │    BSF     │
  │ ████──     │  │ ──████     │  │ ──███──    │  │ ███──███   │
  │ 0     fN   │  │ 0     fN   │  │ 0    fN    │  │ 0    fN    │
  │ Low-pass   │  │ High-pass  │  │ Bandpass   │  │ Bandstop   │
  └────────────┘  └────────────┘  └────────────┘  └────────────┘
```

**Filter specifications**:
- **Passband ripple** (δp or Rp dB): allowed variation in passband
- **Stopband attenuation** (δs or Rs dB): required rejection
- **Transition band width**: frequency region between passband and stopband
- **Phase response**: linear or not?

---

## FIR Filters

```
FIR STRUCTURE (direct form, order M = N-1 taps):

x[n] ──┬──►[z⁻¹]──┬──►[z⁻¹]──┬──►[z⁻¹]──┬── ...
       │          │          │          │
       ▼          ▼          ▼          ▼
     ×b₀        ×b₁        ×b₂        ×b₃    ...
       │          │          │          │
       └──────────┴──────────┴──────────┴──►[Σ]──► y[n]

Each z⁻¹ is a one-sample delay register.
This is literally a shift register with multiply-accumulate.
```

**Transfer function**:
```
H(z) = b₀ + b₁z⁻¹ + b₂z⁻² + ... + b_{M}z⁻M

FIR has only zeros (no poles except at origin).
Always stable — no poles outside unit circle.
```

**Linear phase**: For symmetric h[n] (h[n] = h[M-n]):
- Phase ∠H(e^{jω}) = -Mω/2 (constant group delay = M/2 samples)
- All frequencies delayed by exactly the same amount
- Essential for audio, data comms, image processing

**Design methods**:

| Method | Description | Trade-off |
|--------|-------------|-----------|
| Window method | Multiply ideal h[n] by window | Simple; transition band not optimal |
| Parks-McClellan | Chebyshev equiripple optimization | Optimal; requires specification of bands |
| Frequency sampling | Specify H[k] at DFT points | Simple; can get leakage between bands |

---

## IIR Filters

```
IIR STRUCTURE (direct form II, order N):

         b₀      b₁      b₂
x[n]──►[×]──┬──►[+]──►[×]──►[+]──► y[n]
            │          │
           [z⁻¹]      [z⁻¹]
            │   a₁ ←──┘
           [+]◄──── feedback ─────
            │   a₂ ←──────────────
           [z⁻¹]
            └────────────────────
```

**Transfer function**:
```
         b₀ + b₁z⁻¹ + b₂z⁻² + ... + b_N z⁻N
H(z) = ─────────────────────────────────────────
          1 + a₁z⁻¹ + a₂z⁻² + ... + a_N z⁻N

IIR has both poles and zeros.
STABILITY: all poles must be inside unit circle |z| < 1.
```

**Efficiency**: IIR achieves sharp frequency selectivity with far fewer coefficients than FIR.
A 6th-order IIR can match what might require a 100-tap FIR. This matters for real-time DSP.

---

## IIR Filter Families

All classic IIR filter designs are approximations to the ideal brickwall filter, optimizing
different properties:

```
FILTER FAMILY COMPARISON (lowpass, same order N=5)

Magnitude response:           Phase response:
│                             │
│ Butterworth:   smooth       │ Butterworth:   smooth, monotone
│ ─────────────────────       │
│ Chebyshev I:   equiripple   │ Chebyshev I:   worse phase
│ ─╱╲──────────────────       │
│ Chebyshev II:  equiripple   │ Chebyshev II:  stop only
│ ──────────────╱╲──          │
│ Elliptic:      equiripple   │ Elliptic:      worst phase
│ ─╱╲──────────╱╲──          │                (most nonlinear)
│ Bessel:        gentle slope │ Bessel:        maximally linear phase
│ ──────────────────          │                (best group delay)
└──────────────────────►f     └────────────────────────────────►f
```

| Filter Type | Magnitude | Phase | Transition Band | Use When |
|-------------|-----------|-------|-----------------|----------|
| Butterworth | Maximally flat (monotone) | Moderate | Widest | Simple, clean design |
| Chebyshev I | Equiripple in passband | Poor | Narrower | Passband ripple OK |
| Chebyshev II | Equiripple in stopband | Better | Narrower | Need exact stopband |
| Elliptic (Cauer) | Equiripple both | Worst | Narrowest | Minimum order |
| Bessel | Very gentle rolloff | Best (linear) | Widest | Phase fidelity matters |

**Butterworth**: poles on semicircle in s-plane at equal angular spacing. N-th order:
rolloff = -20N dB/decade beyond cutoff.

**Elliptic** gives steepest transition for given order but worst phase. Optimal for minimum
order when specs are sharp. Every dB of extra attenuation costs, so elliptic maximizes
attenuation per pole.

---

## Filter Design via Bilinear Transform

Standard approach: design analog prototype → convert to digital via bilinear transform.

```
BILINEAR TRANSFORM

Maps s-plane → z-plane:
         2   1 - z⁻¹
s = ─── · ──────────        (replace s with this expression)
        Ts   1 + z⁻¹

Properties:
• Maps entire jω axis to unit circle (no aliasing)
• Maps stable s-plane poles (left half) to inside z unit circle
• Nonlinear frequency warping: ω_d = 2/Ts · tan(Ω_a · Ts/2)

FREQUENCY WARPING:
Analog frequency Ω_a maps to digital frequency ω_d, but nonlinearly.
Must pre-warp critical frequencies before designing analog prototype.

Example: want digital cutoff at ω_c = π/4 rad/sample with fs = 8kHz
Pre-warp: Ω_a = 2·fs·tan(ω_c/2) = 2·8000·tan(π/8) = 6,627 Hz
Design Butterworth at Ω_a = 6,627 Hz → bilinear transform → digital filter at ω_c exactly.
```

---

## The Biquad: Standard Building Block

Second-order sections (biquads) are the standard implementation unit for IIR filters.
Every higher-order IIR is implemented as a cascade of biquads.

```
BIQUAD TRANSFER FUNCTION:

       b₀ + b₁z⁻¹ + b₂z⁻²
H(z) = ─────────────────────      (one pair of conjugate poles, one pair of zeros)
        1 + a₁z⁻¹ + a₂z⁻²

CASCADE for higher order:

Input ──► [Biquad 1] ──► [Biquad 2] ──► [Biquad 3] ──► Output
          (2nd order)    (2nd order)    (2nd order)
          H₁(z)          H₂(z)          H₃(z)
```

**Why biquads?**: Quantization errors and numerical stability are localized.
A 10th-order direct-form filter accumulates numerical errors catastrophically.
Five cascaded biquads, each with 5 coefficients (b₀,b₁,b₂,a₁,a₂), are numerically robust.

**Audio EQ**: Every parametric EQ band is a biquad. The "Audio EQ Cookbook" by R. Bristow-Johnson
provides standard biquad coefficient formulas for peaking EQ, shelving, notch, allpass, bandpass.

---

## Decision Cheat Sheet

| Requirement | Choice | Why |
|-------------|--------|-----|
| Linear phase essential | FIR (symmetric) | Only way to guarantee linear phase |
| Minimum latency (group delay) | FIR (low order) or Bessel IIR | |
| Minimum coefficient count | Elliptic IIR | Steepest transition / order |
| Smooth, no ripple | Butterworth | Maximally flat magnitude |
| Phase integrity (pulses) | Bessel or FIR | Maximally linear group delay |
| Audio EQ (parametric) | Biquad IIR | Standard implementation |
| Antialiasing filter (cheap hardware) | Butterworth analog | Simple pole placement |
| Sharp FIR without ripple | Kaiser window | Control sidelobe/BW trade-off |
| Minimum FIR taps for specs | Parks-McClellan | Optimal Chebyshev equiripple |

---

## Common Confusion Points

**FIR needs many more taps than IIR**: A Butterworth IIR with 4 poles matches frequency
selectivity that would require 100+ FIR taps. The trade-off: IIR has nonlinear phase
and can be unstable; FIR is always stable and can have linear phase.

**Cascade vs parallel form**: Cascade (series) biquads are standard for IIR because
coefficient quantization errors stay localized. Direct high-order form is numerically
disastrous at any order above ~8 in single precision.

**Phase vs group delay**: Phase response ∠H(e^{jω}). Group delay = -d(phase)/dω.
Constant group delay = linear phase. You want flat group delay if timing matters.
A signal through a non-flat group delay filter has its frequency components arriving
at different times — that's dispersion/smearing.

**"Order" means different things**: FIR order M = number of delay taps = M+1 coefficients.
IIR order N = number of poles = N coefficients each in numerator and denominator.
An N-th order IIR can match roughly a 10N to 20N-order FIR for the same spec.

## Adaptive Filters

Adaptive filters adjust their coefficients in real time to minimize an error signal — they are gradient descent applied to FIR filter coefficients.

```
ADAPTIVE FILTER STRUCTURE
                    ┌──────────────────┐
  x[n] ──────────► │  FIR filter w[n]  │──► y[n] = wᵀx
                    └──────────────────┘       │
                           ▲                    ▼
                    weight update          e[n] = d[n] - y[n]
                    w[n+1] = w[n] + μ·e[n]·x[n]     (LMS)
                           ▲
                    d[n] (desired signal)

LMS (Least Mean Squares, Widrow-Hoff 1960):
  w[n+1] = w[n] + μ · e[n] · x[n]
  μ = step size (learning rate — same parameter as in SGD)
  Convergence: 0 < μ < 2/(λ_max) where λ_max = largest eigenvalue of Rxx
  Misadjustment: excess MSE ∝ μ·M (M = filter order)
  Cost: O(M) per sample — very cheap

RLS (Recursive Least Squares):
  Minimizes weighted least squares over all past data (exponential forgetting λ)
  Convergence: much faster than LMS (~M× fewer samples)
  Cost: O(M²) per sample — expensive but justified for fast-changing environments

APPLICATIONS:
  Echo cancellation (telephone, video): model echo path, subtract estimate
  Active noise control: generate anti-noise signal to cancel acoustic noise
  Channel equalization: invert channel distortion in real time
  System identification: estimate unknown plant transfer function online
```

LMS is literally stochastic gradient descent on the MSE cost function with the FIR filter weights as parameters — the same algorithm that trains neural networks, applied to a linear model. RLS is the recursive form of weighted least squares (normal equations updated incrementally).
