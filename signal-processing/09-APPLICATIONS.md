# DSP Applications — A Layered Guide

## The Big Picture

DSP is the invisible infrastructure of modern technology. Every domain from audio to radar
to medicine to ML uses the same mathematical toolkit — just different signals and targets.

```
DSP APPLICATION MAP
════════════════════════════════════════════════════════════════════

   AUDIO                RADAR/SONAR          MEDICAL              ML/AI
   ──────               ─────────────        ───────              ─────
   EQ, dynamics,        Pulse compression,   ECG, EEG,            Feature extraction,
   reverb, codec        Doppler, CFAR        fMRI, ultrasound     spectrograms, MFCC

                      CORE DSP TOOLS
   ┌──────────────────────────────────────────────────────────────┐
   │ FFT/DFT | Filters (FIR/IIR) | Convolution | PSD estimation  │
   │ Z-transform | Correlation | Wavelets | Sampling theory       │
   └──────────────────────────────────────────────────────────────┘

   IMAGE               COMMUNICATIONS        CONTROL              INSTRUMENTATION
   ──────              ──────────────        ───────              ──────────────
   Kernels, edge,      Equalization,         Feedback,            Lock-in amplifiers,
   compression,        demodulation,         vibration sensing,   spectrum analyzers,
   OCR                 channel coding        servo                lock-on filters
```

---

## Audio DSP

### Equalization (EQ)

EQ filters modify the amplitude vs. frequency response of an audio signal.

```
EQ TYPES

Parametric EQ band (single):
  Biquad with peaking filter:
  H(z) = (b₀ + b₁z⁻¹ + b₂z⁻²) / (1 + a₁z⁻¹ + a₂z⁻²)
  Parameters: center frequency fc, gain G (dB), bandwidth Q

  Response:   ┌── +G dB ──┐
              ╱            ╲
  ────────────              ────────────
              fc             (bell curve)

Graphic EQ: fixed set of bands (31-band = ISO octave centers)
              Each band is an independent biquad.

Shelving EQ:
  Low shelf: boost/cut all frequencies below fc
  High shelf: boost/cut all frequencies above fc
```

### Dynamics Processing

```
COMPRESSOR / LIMITER

PURPOSE: Reduce dynamic range (loud peaks → brought down, quiet raised up)

ALGORITHM:
1. Compute signal level (RMS or peak):  L[n] = |x[n]| or moving RMS
2. Gain computation (in dB):
   If L > threshold: G = threshold + (L - threshold)/ratio - L  (gain reduction)
   If L ≤ threshold: G = 0 dB
3. Apply attack/release smoothing to G (prevent clicking)
4. Apply gain: y[n] = x[n] · 10^{G[n]/20}

KEY PARAMETERS:
• Threshold: level above which compression kicks in (-20 dBFS typical)
• Ratio: compression slope (4:1 = 4 dB above threshold → 1 dB output)
• Attack: time constant to respond (1–50 ms: fast = pumping, slow = natural)
• Release: time to recover (50–500 ms)
• Makeup gain: compensate average level after compression
• Knee: hard (sharp) vs soft (gradual onset)
```

### Digital Reverb

```
REVERB ALGORITHMS

Real room: x[n] ★ h[n] where h[n] = room impulse response (RIR)

For a real room h[n] can be 1–5 seconds @ 44.1 kHz = 44,100–220,500 samples.
Direct FFT convolution: overlap-add with precomputed H[k].

Algorithmic reverb (cheaper):
Schroeder reverb (1962): cascade of comb filters + allpass filters
• Comb filter: y[n] = x[n] + g·y[n-D]  (feedback delay line)
  → models a single reflection path with decay
• Allpass filter: flattens spectral coloration
• Parallel comb filters + series allpass → dense reverb tail

Freeverb: 8 parallel comb + 4 series allpass (open source, widely used)

Modern: FDN (Feedback Delay Network) — matrix of cross-coupled delay lines.
Convolution reverb: real RIR measured with impulse (starter pistol or sweep).
```

### Audio Codec Pipeline (MP3/AAC)

```
PERCEPTUAL AUDIO CODING

1. Filter bank: MDCT (modified DCT) → 576 frequency subbands
2. Psychoacoustic model:
   - Compute masking threshold: strong tones mask nearby weaker ones
   - Compute masking threshold vs frequency curve
3. Bit allocation: allocate more bits to unmasked subbands
4. Quantize: coarser quantization where masking allows
5. Entropy coding: Huffman coding of quantized coefficients

COMPRESSION: CD (1411 kbps) → MP3 128 kbps → 11:1 reduction
KEY INSIGHT: Human ear can't hear what's masked — throw away that information.

PSYCHOACOUSTIC MASKING TYPES:
• Simultaneous masking: loud tone at 1 kHz masks quieter tone at 1.2 kHz
• Temporal masking: loud sound masks sounds 50–200 ms before/after (pre/post-masking)
```

---

## Radar and Sonar

### Pulse Compression

```
RADAR WAVEFORM DESIGN

Simple pulse radar:
  • Transmit short pulse (narrow → good range resolution)
  • Short pulse → low energy → poor range
  • Constraint: range_res = c·τ/2 where τ = pulse width

Pulse compression solves the range/energy trade-off:
  • Transmit LONG coded pulse (high energy)
  • After reception, apply matched filter (compression)
  • Output: narrow peak with full energy

LINEAR FM CHIRP (LFM):
  x(t) = rect(t/T) · exp(j·π·k·t²)   where k = B/T (chirp rate)
  Bandwidth B, duration T → time-bandwidth product TBP = BT >> 1

  After matched filter: sinc-shaped output with width ≈ 1/B
  Pulse compression ratio = TBP (typical: 100–10,000)

RANGE SIDELOBE LEVEL: LFM has sinc sidelobes (-13 dB).
Apply amplitude weighting (Taylor window) to reduce sidelobes to -40 dB or lower.
```

### Doppler Processing

```
DOPPLER SHIFT: Moving target shifts frequency of received echo

fd = 2·v·fc/c   (v = target velocity, fc = carrier frequency, c = speed of light)

Example: fc = 10 GHz, v = 30 m/s → fd = 2000 Hz (detectable)

DOPPLER PROCESSING:
Pulse-Doppler radar: transmit coherent pulse train
At each range bin, sequence of N pulses → apply DFT across slow-time
→ Doppler spectrum shows target velocity

CFAR (Constant False Alarm Rate):
Adaptive detection threshold based on local noise level estimate.
Reference cells around each range-Doppler bin → threshold = noise_estimate × scaling_factor
→ constant probability of false alarm regardless of noise level
```

---

## Medical Signal Processing

### ECG (Electrocardiogram)

```
ECG SIGNAL CHARACTERISTICS:
Sample rate: 500–1000 Hz (standard clinical), up to 5 kHz (research)
Frequency content: 0.05–150 Hz (signal), 50/60 Hz (powerline noise)
Key features: P wave, QRS complex, T wave, ST segment

DSP PIPELINE:
1. Baseline wander removal:
   Drift at 0.05–0.5 Hz (breathing, movement)
   Solution: highpass filter at 0.5 Hz or cubic spline baseline estimation

2. Powerline notch filter:
   Notch at 50 Hz (Europe) or 60 Hz (US)
   IIR notch biquad: H(z) with zeros on unit circle at ω = 2π·50/fs

3. EMG noise removal:
   Muscle noise above 100 Hz
   Lowpass at 100–150 Hz (Butterworth or FIR)

4. QRS detection (Pan-Tompkins algorithm, 1985):
   a. Bandpass 5–15 Hz (QRS energy band)
   b. Differentiate: d/dt amplifies high-freq components of QRS
   c. Square: |x|² (all positive, enhances peaks)
   d. Moving window integration: width ≈ 150 ms
   e. Threshold detection with adaptive threshold
   f. Result: R-wave fiducial points → heart rate, HRV
```

### EEG (Electroencephalogram)

```
EEG FREQUENCY BANDS:
Band     | Range  | State
─────────────────────────────────────────
Delta    | 0.5–4 Hz  | Deep sleep
Theta    | 4–8 Hz    | Drowsy, meditation
Alpha    | 8–13 Hz   | Relaxed, eyes closed
Beta     | 13–30 Hz  | Alert, active thinking
Gamma    | 30–100 Hz | High cognitive processing

DSP: Bandpass filter to each band → power in each band → feature vector.

ICA (Independent Component Analysis): Separate EEG channels into
independent sources → removes eye blink artifacts, cardiac artifacts.

BCI (Brain-Computer Interface): Real-time EEG → feature extraction →
classifier → control signal. P300 event-related potential is key BCI target.
```

---

## ML Feature Extraction

### MFCC (Mel-Frequency Cepstral Coefficients)

The dominant audio feature for speech recognition, speaker identification, audio classification.

```
MFCC PIPELINE

x[n] (audio) ──► [Pre-emphasis] ──► [Framing 20–50ms] ──► [Hamming window]
         ──► [FFT] ──► [Mel filterbank] ──► [log] ──► [DCT] ──► MFCCs

STEPS:
1. Pre-emphasis: y[n] = x[n] - 0.97·x[n-1]  (boost high frequencies)
2. Frame: divide into overlapping 20–50ms frames (25ms frame, 10ms hop typical)
3. Window: Hamming window per frame
4. FFT: typically 512 or 1024 points
5. Mel filterbank: triangular filters on Mel scale
   Mel(f) = 2595·log₁₀(1 + f/700)   (perceptual frequency scale)
   Human ear: logarithmic frequency perception
   Apply 26–40 triangular filters on Mel scale → 26–40 energies
6. Log: human perception of loudness is logarithmic
7. DCT: decorrelates filterbank outputs → 13–40 MFCC coefficients
   (only first 12–13 kept; higher coefficients encode fine spectral detail)

PLUS: Δ (delta) and ΔΔ (delta-delta) coefficients capture temporal dynamics.
Final feature vector: 39 features per 10ms frame (13 MFCC + 13Δ + 13ΔΔ)
```

### Spectrograms for Deep Learning

```
SPECTROGRAM AS IMAGE INPUT

Audio → STFT → |X(τ, f)|² → log-scale → image

Treat as 2D image → CNN or Vision Transformer
Used for:
• Music genre classification
• Bird song identification
• Environmental sound classification
• Wake word detection (Hey Siri, OK Google)

VARIANTS:
Mel spectrogram: compress frequency axis to Mel scale
Log-mel spectrogram: most common for deep learning (YAMNet, VGGish, AST)
CQT (constant-Q transform): logarithmic frequency bins, good for music
```

<!-- @editor[bridge/P2]: The ML section shows CNNs consuming spectrograms but never makes the explicit bridge from classical DSP to learned DSP — the central connection the learner calibration flags as needed. A CNN convolutional layer IS a bank of learned FIR filters: kernel weights = filter coefficients, stride = downsampling, depth = number of filter channels. Backprop is gradient descent on the filter bank. Pooling layers = downsampling (cf. DWT ↓2). The entire spatial-hierarchy of CNN features maps directly to multiresolution filter banks. Attention mechanisms (transformer) are dynamic, input-dependent filters: Q·Kᵀ softmax weighting = data-driven spectral shaping. This bridge from classical filter banks → learned filter banks → attention-as-filtering should appear explicitly here as a section (e.g., "DSP → Deep Learning Correspondence"). -->

### Signal Features in ML Pipelines

```
COMMON DSP FEATURES FOR ML

Time domain:     Zero crossing rate, RMS energy, kurtosis, skewness
Spectral:        Centroid, rolloff, flux, bandwidth, flatness
Frequency bands: Energy in each octave band
MFCC:           Dominant for speech/audio
Wavelets:        Multi-scale energy features
Autocorrelation: Period estimation (pitch detection)
Line spectrum:   LPC coefficients (linear prediction for speech)

FEATURE PIPELINE (typical):
Signal ──► Preprocessing ──► Segmentation ──► Feature extraction ──► Normalization ──► ML model
          (filter/resample)  (frames, HOP)   (FFT, MFCC, etc.)     (z-score, minmax)
```

---

## Image Processing via 2D Convolution

```
2D CONVOLUTION AS FILTERING

I_out[m,n] = Σ Σ I_in[m-j, n-k] · K[j,k]
              j  k

Common 2D kernels:
┌─────────────────────────────────────────────────────────────────┐
│ Gaussian blur (low-pass):        Edge detection (Sobel X):      │
│  1/16 · [1 2 1]                  [-1  0  1]                     │
│          [2 4 2]                  [-2  0  2]                     │
│          [1 2 1]                  [-1  0  1]                     │
│                                                                   │
│ Sharpen:                         Laplacian (edge enhance):      │
│  [0  -1   0]                      [ 0  1   0]                   │
│  [-1  5  -1]                      [ 1 -4   1]                   │
│  [0  -1   0]                      [ 0  1   0]                   │
└─────────────────────────────────────────────────────────────────┘

SEPARABILITY: if K[j,k] = h₁[j]·h₂[k], then 2D convolution = 1D + 1D
  Cost: O(N²·K²) → O(N²·K) with separability (Gaussian is separable)
```

---

## Decision Cheat Sheet

| Application | Key DSP Operation |
|-------------|-------------------|
| Audio EQ | Parametric biquad IIR filter |
| Audio compression | MDCT + perceptual masking |
| Digital reverb (quality) | FFT overlap-add convolution with RIR |
| Digital reverb (cheap) | Schroeder/FDN comb/allpass |
| Radar range | Pulse compression (matched filter / FFT) |
| Radar velocity | DFT across pulse train (Doppler) |
| ECG beat detection | Pan-Tompkins (bandpass + square + integrate) |
| Speech features | MFCC (13–40 coefficients per frame) |
| Audio classification | Log-mel spectrogram + CNN |
| Image blur/sharpen | 2D convolution with appropriate kernel |

---

## Common Confusion Points

**MFCC vs mel spectrogram**: MFCC applies DCT after the log-mel filterbank — decorrelates
the coefficients. Log-mel spectrogram stops before DCT. Deep learning models often prefer
log-mel spectrograms directly (no need for decorrelation — neural nets handle correlation).
MFCC with DCT was designed for Gaussian mixture models (GMMs) that assume independence.

**Frame size vs hop size**: STFT frame size determines frequency resolution (wider = better freq res).
Hop size (overlap) determines time resolution of the output spectrogram. These are independent.
50% overlap is the standard (frame size = 2× hop size).

**ECG powerline noise**: A simple IIR notch is dangerous for ECG analysis — it distorts ST segments
and QRS morphology. Clinical ECG systems use linear-phase FIR notch filters to avoid phase
distortion. This is why "linear phase FIR" matters in medical devices.

**Radar vs sonar**: Both use pulse-echo with matched filter. Key difference: radar uses EM waves
(c = 3×10⁸ m/s), sonar uses acoustic waves (c ≈ 1,500 m/s in water). Sonar Doppler is much
more pronounced for a given velocity because wavelengths are much longer.
