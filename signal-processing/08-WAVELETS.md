# Wavelets — A Layered Guide

## The Big Picture

Wavelets solve a problem the Fourier transform cannot: analyzing signals with
time-varying frequency content. The key insight is **multiresolution** — use
wide windows for low frequencies, narrow windows for high frequencies.

```
THE PROBLEM WITH FOURIER

Fourier Transform of x(t):
• Tells you which frequencies are present
• Tells you nothing about WHEN they occur
• Captures global frequency content

Example: chirp signal (frequency sweeps from low to high)
  Fourier spectrum: broad smear — "all frequencies present" — useless timing info
  You lose: when does each frequency occur?

Musical note in time: ─────────────────────────────────────────────►
  [silence ...]  [NOTE F#]  [silence ...]  [NOTE B♭]  [silence ...]

  FT magnitude:  Shows F# and B♭ present — but when? FT can't say.

THIS IS THE LIMITATION THAT MOTIVATED TIME-FREQUENCY ANALYSIS
```

---

## Short-Time Fourier Transform (STFT)

First fix: slide a window over the signal and take FT of each windowed segment.

```
STFT DEFINITION:

X(τ, f) = ∫ x(t) · w(t-τ) · e^{-j2πft} dt

w(t-τ): window function centered at time τ
τ: time position (slide the window)
f: frequency

OUTPUT: 2D time-frequency representation (spectrogram = |X(τ,f)|²)

HEISENBERG-GABOR UNCERTAINTY PRINCIPLE:
Δt · Δf ≥ 1/(4π)

Cannot simultaneously have arbitrary time resolution AND frequency resolution.
Short window → good time resolution, poor frequency resolution
Long window → good frequency resolution, poor time resolution
```

**The STFT limitation**:

```
FIXED RESOLUTION PROBLEM

STFT uses the SAME window width for all frequencies:

High frequency (short period):    Low frequency (long period):
  ┌──window──┐                      ┌──────── same window ────────┐
  │ ╫╫╫╫╫╫╫╫│                      │ ╫                           │
  └──────────┘                      └────────────────────────────┘
  Many cycles fit → good freq res   Less than one cycle → bad freq res

Result: fixed grid in time-frequency plane
   freq │────────────────────
        │ same boxes everywhere
        │────────────────────
        │────────────────────
        └──────────────────────► time

But we want: high freq → narrow time boxes (fast events)
             low freq  → wide time boxes (slow events)
→ LOGARITHMIC FREQUENCY SCALE → wavelets
```

---

## Wavelet Transform

The continuous wavelet transform (CWT) addresses STFT's fixed-resolution limitation
by using scaled (stretched/compressed) versions of a single mother wavelet ψ(t).

```
CONTINUOUS WAVELET TRANSFORM:

W_x(a, b) = (1/√|a|) ∫ x(t) · ψ*((t-b)/a) dt

a: scale parameter (a>1 = dilate/stretch → low frequency analysis)
              (0<a<1 = compress → high frequency analysis)
b: translation parameter (time position of the wavelet)

Mother wavelet ψ(t): localized oscillating function with:
• Zero mean: ∫ψ(t) dt = 0  (oscillation, "wave" part)
• Finite energy: ∫|ψ(t)|² dt < ∞  (localization, "-let" = little part)

RESULT: Logarithmically-spaced frequency resolution
   freq │▓▓│▓▓▓│▓▓▓▓▓▓│▓▓▓▓▓▓▓▓▓▓▓▓│
        │  │   │      │             │
        │hi│ ↑ │      │  low freq:  │
        │fr│ narrow   │  wide time  │
        │eq│ time     │  broad freq │
        └──────────────────────────► time
```

---

## Mother Wavelets

Different wavelets are optimized for different signal characteristics:

```
WAVELET FAMILIES

Haar (simplest):
ψ(t) = +1 for 0 ≤ t < 1/2
       -1 for 1/2 ≤ t < 1
        0 otherwise

   ┌──────┐          Compact support: 1
   │  +1  │          Discontinuous
   ┤──────┤──────    Good for: edges, step functions
   │  -1  │          Bad for: smooth signals
   └──────┘

Morlet:
ψ(t) = e^{-t²/2} · e^{jω₀t}   (Gaussian-modulated complex sinusoid)

   ╭─────╮            No compact support (infinite)
  ╱       ╲           Good for: oscillatory signals
 │         │          Used in: geophysics, EEG, audio analysis
  ╲       ╱
   ╰─────╯

Daubechies (D-4, D-8, ...):
Compactly supported, orthonormal wavelets.
No closed-form expression — defined by filter coefficients.
Good for: general signal compression, image processing (JPEG 2000)

Mexican Hat (ψ = -d²/dt² Gaussian):
"Ricker wavelet" in geophysics. Symmetric, real-valued.

Biorthogonal:
Separate analysis and synthesis wavelets. Used in JPEG 2000.
Allows symmetric FIR filters (linear phase) at cost of non-orthogonality.
```

---

## Multiresolution Analysis (MRA)

The mathematical framework behind the discrete wavelet transform.

```
MRA FRAMEWORK

A multiresolution analysis is a sequence of subspaces:
... ⊂ V₋₁ ⊂ V₀ ⊂ V₁ ⊂ ... = L²(ℝ)

where each Vⱼ captures "approximation at resolution 2ʲ"

The "detail" between Vⱼ and Vⱼ₊₁ is the wavelet subspace Wⱼ:
Vⱼ₊₁ = Vⱼ ⊕ Wⱼ     (orthogonal direct sum)

PRACTICAL MEANING:
V₀: coarse approximation (low-frequency content)
W₀: detail at this level (frequency band between V₀ and V₁)
W₁: detail at next level (higher frequency band)
...

FILTER BANK INTERPRETATION:
                                H₀(z) (lowpass) ──► ↓2 ──► coarse approx
Signal x[n] ──► split ──┤
                                H₁(z) (highpass) ──► ↓2 ──► detail coefficients
```

---

## Discrete Wavelet Transform (DWT)

The DWT is implemented as a cascade of two-channel filter banks.

```
DWT ANALYSIS (decomposition):

x[n] ──┬──► [H₀(z)] ──► [↓2] ──► cA₁  (approximation level 1)
       │
       └──► [H₁(z)] ──► [↓2] ──► cD₁  (detail level 1)

Then apply again to cA₁:

cA₁ ──┬──► [H₀(z)] ──► [↓2] ──► cA₂  (approximation level 2)
      │
      └──► [H₁(z)] ──► [↓2] ──► cD₂  (detail level 2)

... and so on for J levels.

RESULT for signal of length N:
{cAJ (N/2ᴶ samples), cDJ, cD_{J-1}, ..., cD₁}
Total samples = N  (perfect reconstruction — no information loss)

FILTER DESIGN CONSTRAINT (perfect reconstruction):
H₀ and H₁ must be QMF (Quadrature Mirror Filters):
H₁(z) = z^{-(N-1)} · H₀(-z⁻¹)   for orthogonal wavelets
```

**Daubechies coefficients for D-4 (4-tap) lowpass filter**:
```
h₀ = [(1+√3), (3+√3), (3-√3), (1-√3)] / (4√2)
   ≈ [0.4830, 0.8365, 0.2241, -0.1294]

These define both the wavelet ψ(t) and scaling function φ(t).
The wavelet is the impulse response of the highpass filter.
```

---

## DWT Frequency-Scale Correspondence

```
WAVELET FREQUENCY BANDS for J-level DWT, sample rate fs:

Level | Band            | Samples per level | Signal content
──────┼─────────────────┼───────────────────┼──────────────────
cD₁  | [fs/4, fs/2]    | N/2               | Highest freq detail
cD₂  | [fs/8, fs/4]    | N/4               | Second-highest
cD₃  | [fs/16, fs/8]   | N/8               | ...
...  | ...             | ...               | ...
cDⱼ  | [fs/2^{J+1}, fs/2^J] | N/2^J       | ...
cAⱼ  | [0, fs/2^{J+1}] | N/2^J            | Coarsest approx

For speech at fs = 8 kHz, 5-level DWT:
cD₁: 2000–4000 Hz  (fricatives, sibilants)
cD₂: 1000–2000 Hz  (formant region)
cD₃: 500–1000 Hz   (vowel fundamentals)
cD₄: 250–500 Hz    (pitch harmonics)
cD₅: 125–250 Hz    (low pitch)
cA₅: 0–125 Hz      (DC + very low)
```

---

## JPEG 2000 and Wavelet Image Compression

```
JPEG 2000 vs JPEG COMPARISON

JPEG (1992):              JPEG 2000 (2000):
8×8 DCT blocks          Entire image wavelet transform
Block artifacts at       No blocking artifacts
low bitrates            Progressive transmission
Poor at low bitrates    Better at all bitrates
                        Lossless and lossy modes
                        Region-of-interest coding

JPEG 2000 STEPS:
1. Color transform: RGB → YCbCr
2. 2D DWT: CDF 9/7 biorthogonal wavelet (lossy) or Le Gall 5/3 (lossless)
3. Coefficient quantization: more aggressive at fine scales
4. EBCOT entropy coding: embedded block coding with optimized truncation

WAVELET DECOMPOSITION (2D, 3-level):
Original → LL₃ | LH₃ | LH₂ | LH₁
(image)      ─── ─────── ──────────
            HL₃ | HH₃ |
            ────────────   HH₂ |  HH₁
            HL₂ | HL₁

LL = low-low (coarse approximation)
LH = low-high (horizontal edges)
HL = high-low (vertical edges)
HH = high-high (diagonal edges)
```

---

## Decision Cheat Sheet

| Application | Wavelet Choice | Why |
|-------------|---------------|-----|
| Image compression | Biorthogonal CDF 9/7 or 5/3 | Linear phase, good compression |
| Edge detection | Haar | Compact support, step-response |
| Audio analysis | Morlet | Time-frequency localization |
| Biomedical (ECG/EEG) | Daubechies D-4 to D-8 | Regularity matches signal |
| Geophysics | Mexican hat (Ricker) | Matches seismic wavelet shape |
| Denoising | Daubechies + thresholding | Energy compaction |
| Want Fourier-like interpretation | Morlet CWT | Frequency axis intuitive |

---

## Common Confusion Points

**DWT ≠ CWT**: Discrete Wavelet Transform uses discrete scales and shifts (dyadic),
computed as filter banks. Fast: O(N). Continuous Wavelet Transform uses continuous scale/shift,
is redundant (over-complete), and is O(N² ) or O(N log N) per scale. CWT is for analysis;
DWT is for coding/compression.

**Orthogonal vs biorthogonal**: Orthogonal DWT (Daubechies): h₀ = h₁ flipped/negated.
Analysis and synthesis filters are the same. Biorthogonal: analysis ≠ synthesis filters.
Enables symmetric (linear-phase) filters at the cost of non-orthogonality. JPEG 2000 uses
biorthogonal for this reason (linear phase → no edge artifacts).

**The uncertainty principle doesn't disappear**: Wavelets obey the same Heisenberg principle
as STFT. What wavelets do is make the time-bandwidth product constant across scales — a choice
to allocate time resolution where needed (high frequencies) and frequency resolution where needed
(low frequencies), matching the logarithmic structure of most natural signals.

**Wavelet denoising**: Signal energy concentrates in few large coefficients; noise spreads over
many small ones. Threshold small coefficients → sparse representation → reconstruction with
reduced noise. This is optimal for piecewise-smooth signals. Called wavelet shrinkage or
soft-thresholding (Donoho-Johnstone).
