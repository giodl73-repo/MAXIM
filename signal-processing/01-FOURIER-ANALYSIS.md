# Fourier Analysis — A Layered Guide

## The Big Picture

Fourier analysis decomposes a signal into sinusoidal components. The framework has four variants —
choose based on whether your signal is continuous/discrete and periodic/aperiodic.

```
FOURIER FAMILY TREE
══════════════════════════════════════════════════════════════════════

   Signal type              Transform              Output
   ─────────────────────────────────────────────────────────────────
   CT, periodic             Fourier Series         Discrete cₙ
   x(t+T) = x(t)           FS                     spectral lines

   CT, aperiodic            Fourier Transform      Continuous X(jω)
   x(t) → 0 as t→±∞       CFT                    spectrum

   DT, periodic (period N)  Discrete Fourier       N complex
   x[n+N] = x[n]           Series                 coefficients

   DT, any finite N         DFT / FFT              X[k], k=0..N-1
   (treated as 1 period)   (computable)            N-point spectrum

   DT, infinite sequence    DTFT                   Continuous X(e^jω)
   general x[n]            (theoretical)           ω-periodic, 2π

══════════════════════════════════════════════════════════════════════
In practice: everything becomes a DFT/FFT because that's what
computers can compute. The others are analysis/design tools.
```

---

## Fourier Series

For a T-periodic signal x(t), decompose into complex exponentials:

```
         +∞
x(t) =   Σ  cₙ · e^{j·n·ω₀·t}        where ω₀ = 2π/T (fundamental)
        n=-∞

          1   T
cₙ  =   ─── ∫  x(t) · e^{-j·n·ω₀·t} dt
          T   0

Interpretation: cₙ is the amplitude and phase of the nth harmonic.
|cₙ| = magnitude spectrum (one-sided: multiply by 2 for n>0)
∠cₙ = phase spectrum
```

**Why complex exponentials?**: They're eigenfunctions of differentiation (and LTI systems).
If you input e^{jωt} to an LTI system, output is H(jω)·e^{jωt} — same frequency, scaled.

**Convergence**: Dirichlet conditions (finite discontinuities, finite variation) → pointwise
convergence except at discontinuities where it converges to midpoint. Gibbs phenomenon:
~9% overshoot at jump discontinuities, independent of N.

### Parseval's Theorem (Power Form)

```
1   T                  +∞
─ ∫  |x(t)|² dt  =   Σ  |cₙ|²
T   0                 n=-∞

Power in time domain = Sum of power in each harmonic
```

---

## Continuous Fourier Transform

For aperiodic signals (Fourier series in the limit T→∞):

```
                   +∞
X(jω) = F{x(t)} = ∫  x(t) · e^{-jωt} dt      (Analysis)
                  -∞

                   1   +∞
x(t) = F⁻¹{X(jω)} = ─── ∫  X(jω) · e^{jωt} dω  (Synthesis)
                   2π  -∞
```

**Key transform pairs** (memorize these):

| Time domain x(t) | Frequency domain X(jω) | Notes |
|------------------|------------------------|-------|
| δ(t) | 1 | Impulse → flat spectrum |
| 1 | 2πδ(ω) | DC → impulse at DC |
| e^{-at}u(t), a>0 | 1/(a+jω) | Exponential decay → Lorentzian |
| rect(t/T) | T·sinc(ωT/2π) | Rectangular pulse → sinc |
| sinc(t) | π·rect(ω/(2π)) | Sinc → rectangular |
| e^{jω₀t} | 2πδ(ω-ω₀) | Sinusoid → spectral line |
| Gaussian e^{-t²} | √π·e^{-ω²/4} | Gaussian ↔ Gaussian |

**Key properties**:
- Linearity: F{ax+by} = aX + bY
- Time shift: F{x(t-t₀)} = e^{-jωt₀}·X(jω)  (phase rotation, same magnitude)
- Frequency shift: F{e^{jω₀t}x(t)} = X(j(ω-ω₀))  (modulation theorem)
- **Convolution ↔ Multiplication**: F{x★h} = X(jω)·H(jω)  (fundamental)
- Time scaling: F{x(at)} = (1/|a|)·X(jω/a)  (compress time → expand frequency)
- Differentiation: F{x'(t)} = jω·X(jω)  (derivative → multiply by jω)
- Parseval: ∫|x(t)|²dt = (1/2π)∫|X(jω)|²dω

---

## Discrete Fourier Transform

The DFT is what computers actually compute. Given N samples x[0], x[1], ..., x[N-1]:

```
Analysis:             N-1
X[k] = Σ  x[n] · W_N^{nk}   where  W_N = e^{-j2π/N}
         n=0

                          k = 0, 1, ..., N-1

           1   N-1
Synthesis: x[n] = ─   Σ  X[k] · W_N^{-nk}
           N  k=0

           n = 0, 1, ..., N-1
```

**Physical meaning of X[k]**:
- k=0: DC component (zero frequency)
- k=1: fundamental frequency = fs/N Hz
- k=N/2: Nyquist frequency = fs/2 Hz
- k=N/2+1 to N-1: negative frequencies (mirror of k=1 to N/2-1 for real inputs)

```
DFT output layout for real input (N=8):
Index: 0   1   2   3   4   5   6   7
       DC  f   2f  3f  fN  -3f -2f -f
            │               │
            │               └── Nyquist (real for real input)
            └── fundamental = fs/N
```

**Complexity**: Direct DFT = O(N²) multiplications. For N=1024, that's 1M ops.

---

## FFT — Cooley-Tukey Radix-2

The FFT reduces DFT from O(N²) to O(N log N) by exploiting DFT symmetry.

```
KEY INSIGHT: W_N^{n(k+N/2)} = -W_N^{nk}  (twiddle factor symmetry)

Split N-point DFT into two N/2-point DFTs (even/odd samples):

              N/2-1                     N/2-1
X[k] =   Σ  x[2m]·W_{N/2}^{mk}  +  W_N^k · Σ  x[2m+1]·W_{N/2}^{mk}
          m=0                       m=0

         ═══════════════════════      ══════════════════════════════
              E[k] (even DFT)          W_N^k · O[k] (odd DFT)

BUTTERFLY OPERATION:
        ┌───┐       ┌────────────┐
  a ───►│   │───►  a + W·b
        │ × │
  b ───►│ W │───►  a - W·b
        └───┘
```

**Recursion**: Split N → N/2 → N/4 → ... → 1. At each level: N/2 butterfly ops.
log₂(N) levels × N/2 butterflies = O(N log N).

**Impact at N=1024**: DFT needs ~1M multiplications; FFT needs ~5,000.
This is what made real-time audio/radar/communications DSP possible after 1965.

```
FFT PERFORMANCE
───────────────────────────────────────
N         DFT (N²)   FFT (N·log₂N)   Speedup
───────────────────────────────────────
64        4,096       384             10.7×
1,024     1,048,576   10,240          102×
1,048,576 10^12       20,971,520      47,000×
───────────────────────────────────────
```

**Variants**: Radix-4 FFT, split-radix FFT, prime-factor FFT (for non-power-of-2 N),
Bluestein FFT (arbitrary N via convolution). Libraries like FFTW auto-select.

---

## Spectral Leakage and Windowing

**The leakage problem**: When you take a finite-length DFT, you're implicitly multiplying the
signal by a rectangular window w[n] = 1 for 0≤n<N, 0 elsewhere. In the frequency domain,
this convolution with a sinc-shaped DTFT causes energy from one frequency to "leak" into
adjacent bins.

```
LEAKAGE VISUALIZATION

True signal (two tones):         DFT with rectangular window:
                                  (leakage from sinc sidelobes)
 ●        ●                        ●●●●●●●●●●●●●
 f₁       f₂                    f₁              f₂
 (clean lines)                  (smeared, sidelobes mix)
```

**Window functions**: Taper the signal to zero at edges before DFT.
Trade-off: **main lobe width** (frequency resolution) vs. **sidelobe level** (leakage rejection).

| Window | Main Lobe Width | Peak Sidelobe (dB) | Use Case |
|--------|-----------------|---------------------|----------|
| Rectangular | 2/N (narrowest) | -13 dB (worst) | When you need resolution and know no leakage |
| Hann (raised cosine) | 4/N | -31 dB | General purpose audio |
| Hamming | 4/N | -41 dB | Speech processing |
| Blackman | 6/N | -57 dB | When leakage rejection matters more than resolution |
| Blackman-Harris | 8/N | -92 dB | Precision spectral analysis |
| Kaiser (β=14) | variable | -100+ dB | Programmable trade-off |
| Flat top | 8/N | -93 dB | Amplitude accuracy (calibration) |

```
WINDOW SHAPE COMPARISON (N=32)

Rectangular: ████████████████████████████████
Hann:        ▁▂▄▆▇█████████████████▇▆▄▂▁
Blackman:    ▁▁▂▃▅▇█████████████▇▅▃▂▁▁

Tapered windows sacrifice frequency resolution to reduce leakage.
```

**Zero-padding**: Adding zeros before FFT increases the DFT output density (interpolation
in frequency domain) but does NOT improve frequency resolution. Resolution is determined
by the actual signal length T, not N. Zero-padding is for display/interpolation only.

---

## Decision Cheat Sheet

| Situation | Choice | Reason |
|-----------|--------|--------|
| Analyzing a finite buffer of data | DFT / FFT | Only computable form |
| Design continuous-time system | CT Fourier Transform | Rational H(jω) |
| Periodic signal, spectral lines | Fourier Series | Exact representation |
| Need lowest sidelobes | Blackman-Harris or Kaiser | 90+ dB rejection |
| Need finest frequency resolution | Rectangular window | Narrowest main lobe |
| General spectral analysis | Hann window | Good balance |
| Amplitude-accurate measurement | Flat-top window | Minimizes amplitude error |
| Non-power-of-2 length N | FFTW or Bluestein | Auto-selects algorithm |

---

## Common Confusion Points

**DFT is circular, not linear**: DFT implicitly assumes x[n] is one period of a periodic sequence.
If you use DFT for linear convolution, you must zero-pad to length ≥ M+L-1 to prevent circular
aliasing (where tail wraps around and corrupts the beginning).

**Zero-padding ≠ better resolution**: Padding zeros interpolates the spectrum (smoother curve)
but you're not learning anything new — you can't resolve two close frequencies just by zero-padding.
Resolution requires longer observation time T.

**Real signal → symmetric DFT**: For real x[n], X[k] = X*[N-k]. Upper half of DFT output is
redundant. Only need X[0] to X[N/2] (N/2+1 unique values). This is why one-sided spectra
are plotted up to fs/2.

**Gibbs phenomenon**: Any attempt to reconstruct a signal with a discontinuity using a finite
Fourier series will show ~9% overshoot near the jump, regardless of how many terms you include.
Reducing this requires windowing (Lanczos σ factor) or using a different basis entirely.

**Phase is as important as magnitude**: Minimum-phase, linear-phase, all-pass — these are
defined by phase behavior. Many beginners look only at |X[k]| and lose all timing information.
