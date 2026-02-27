# Sampling Theory — A Layered Guide

## The Big Picture

Sampling converts a continuous-time signal into a discrete-time sequence.
The Nyquist-Shannon theorem tells you exactly what you lose (and don't lose) in this conversion.

```
SAMPLING PIPELINE
══════════════════════════════════════════════════════════════════════

Continuous        Anti-alias    Ideal         Quantizer     Digital
  Signal            Filter      Sampler       (ADC)         Signal
                   (LPF)
  x(t)   ───►  [f < fs/2]  ──►  x[n]=x(nTs)  ──►  xq[n]   ──►  bits

                    │                │               │
                    │                │               │
               Removes content   Samples at      Rounds to
               above Nyquist      rate fs         B bits
               BEFORE aliasing  = 1/Ts          2^B levels

  Reconstruction (DAC):

  bits   ──►  xq[n]  ──►  [Hold]  ──►  [Reconstruct  ──►  x̂(t)
                           (S&H)       filter fLPF<fs/2]

══════════════════════════════════════════════════════════════════════
```

---

## Nyquist-Shannon Sampling Theorem

**Statement**: A bandlimited signal with no frequency content above B Hz can be **perfectly
reconstructed** from samples taken at rate fs ≥ 2B samples/second.

```
FREQUENCY DOMAIN VIEW

x(t) spectrum (bandlimited to B):         After sampling at fs:
                                          Spectrum repeats every fs Hz
      │                                         │
   ───┤   ████                    ████ ... ─────┤─ ... ████ ... ████ ...
      │  ─B   B                         0      fs   2fs
      0       f                         └── if fs>2B, no overlap (good)
                                              if fs<2B, overlap → ALIASING
```

The sampling operation mathematically multiplies x(t) by an impulse train (comb function):

```
p(t) = Σ δ(t - nTs)        (impulse train at rate fs = 1/Ts)
        n

xs(t) = x(t) · p(t) = Σ x(nTs)·δ(t - nTs)

Xs(jω) = (1/Ts) · Σ X(j(ω - k·2π/Ts))   (copies every 2π/Ts radians)
                   k
```

**Perfect reconstruction condition**: No spectral overlap → require fs > 2B.
If met, the original can be recovered with an ideal lowpass filter: H(jω) = Ts for |ω| < π/Ts, 0 otherwise.

---

## Aliasing

When the sampling rate is too low, high frequencies "fold back" and appear as lower frequencies.

```
ALIASING MECHANISM

Signal at frequency f, sampled at fs:

If f = 100 Hz, fs = 400 Hz  → no alias, appears at 100 Hz ✓
If f = 300 Hz, fs = 400 Hz  → alias! appears at |300-400| = 100 Hz  ✗
If f = 500 Hz, fs = 400 Hz  → alias! appears at |500-400| = 100 Hz  ✗

General formula: alias frequency = |f - round(f/fs) · fs|

FOLDING DIAGRAM (fs = 400 Hz, Nyquist = 200 Hz):

      0 Hz  ─────────── 200 Hz ─────────── 400 Hz ─────────── 600 Hz
      ├─────────────────────┤←─────────────┤←─────────────────┤
      DC                Nyquist           fs               3fs/2
      Signals here appear  These fold back to [0, 200 Hz]
      correctly            as aliases
```

**Prevention**: Anti-alias filter (AAF) — lowpass filter with cutoff at fs/2 — applied
BEFORE sampling. This is a hard requirement, not optional.

**Audio example**: CD audio: fs = 44,100 Hz → Nyquist = 22,050 Hz → AAF must attenuate
everything above ~20 kHz before the ADC samples.

---

## Quantization

Real ADCs also quantize amplitude into discrete levels.

```
QUANTIZATION ERROR

B-bit ADC:  2^B quantization levels
Full-scale voltage range: ±Vfs

Quantization step: Δ = 2·Vfs / 2^B

Quantization error: -Δ/2 ≤ e[n] ≤ +Δ/2 (uniform distribution)

Quantization noise power: σ²_q = Δ²/12 = (2·Vfs)² / (12·2^{2B})

SQNR (signal-to-quantization-noise ratio) for full-scale sine:
SQNR ≈ 6.02B + 1.76 dB

Rule of thumb: each additional bit ≈ 6 dB improvement in dynamic range
```

| ADC Bits | SQNR (ideal) | Dynamic Range | Typical Use |
|----------|-------------|---------------|-------------|
| 8 | ~50 dB | 256 levels | Low-cost audio, video |
| 12 | ~74 dB | 4,096 levels | Instrumentation |
| 16 | ~98 dB | 65,536 levels | CD audio, high-quality |
| 24 | ~146 dB | 16M levels | Studio recording (noise floor limits at ~120 dB) |

---

## Oversampling and Noise Shaping

Sampling above the Nyquist rate spreads quantization noise over a wider band.

```
OVERSAMPLING BENEFIT

Sample at M × fs (oversampling ratio = M):

Quantization noise power is fixed (σ²_q),
but it's now spread over [0, M·fs/2] instead of [0, fs/2].

After digital lowpass filter keeping [0, fs/2]:

Noise in band = σ²_q / M

SNR improvement = 10·log₁₀(M) dB ≈ 0.5 dB per doubling of sample rate
(adding 1 effective bit requires 4× oversampling)
```

**Noise shaping** (sigma-delta): Push quantization noise out of the signal band
by feeding quantization error back through a loop filter. Enables 1-bit ADCs with
very high oversampling to achieve 16-24 bit equivalent SQNR in the audio band.

```
SIGMA-DELTA MODULATOR (1-bit)

         ┌──────────────────────────────────────┐
         │                                      │
x(t) ──►+──► [Loop filter H(z)] ──► [1-bit] ──►+──► Digital stream
         ▲-                              │      │    at M·fs
         │                              └──────┘
         └─────── feedback ─────────────────────

Quantizer noise E(z) sees transfer function: NTF(z) = 1 - H(z)
Design H(z) as integrator → NTF = highpass → noise shaped away from DC
```

---

## ADC/DAC Architecture Overview

```
ADC TYPES vs SPEED/RESOLUTION TRADE-OFF

Speed (samples/sec)
│
│  GS/s  Flash ADC ────────────────────────────────────────────●
│        (comparator array, 2^B comparators for B bits)
│        Fastest; limited to ~8 bits; ultrasound/radar
│
│  MS/s  SAR ADC   ──────────────────────────────●
│        (successive approximation register)
│        Mid-speed, mid-resolution; best efficiency
│        Dominant in microcontrollers, IoT sensors
│
│  kS/s  Delta-Sigma ──────────────────────────●
│        (1-bit oversampling + noise shaping)
│        High resolution (up to 24 bit)
│        Audio, industrial instrumentation, ΔΣ ADC
│
└──────────────────────────────────────────────────────────────►
   Low resolution (8-bit)                     High resolution (24-bit)
```

---

## DAC and Reconstruction

The DAC output is a staircase (zero-order hold), not a smooth curve.

```
ZERO-ORDER HOLD EFFECT

Digital samples: ─●──●──●──●──●──
Ideal D/A:       ─/──/──/──/──/── (impulse train, then filter)
ZOH output:      ─████████████─── (holds each sample until next)

ZOH introduces spectral shaping: H_ZOH(f) = Ts·sinc(f·Ts)·e^{-jπfTs}

This attenuates high frequencies — reconstruction filter must compensate
(inverse sinc pre-emphasis) for flat frequency response.
```

---

## Decision Cheat Sheet

| Situation | Recommendation |
|-----------|----------------|
| Choosing sample rate for audio (20 kHz) | 44.1 kHz or 48 kHz (standard) |
| Need to sample at exactly 2B? | No — you need fs > 2B with margin for real AAF rolloff |
| Anti-alias filter not sharp enough? | Oversample (4–8×) then decimate digitally |
| Want 24-bit audio ADC? | Use sigma-delta — only practical 24-bit ADC architecture |
| High-speed instrumentation | SAR ADC — best power/speed/resolution balance |
| Radar / oscilloscope | Flash ADC — GS/s range, accept ~8 bits |
| Hearing noise floor in digital audio | Dither before quantization |

---

## Common Confusion Points

**"Nyquist rate" vs. "Nyquist frequency"**: Nyquist rate = 2B (minimum sample rate for bandwidth B).
Nyquist frequency = fs/2 (maximum representable frequency for a given sample rate). Different things.

**Anti-aliasing happens BEFORE ADC, not after**: Once aliased, the information is destroyed.
No digital filter can un-alias. The AAF must be analog.

**Oversampling + decimation is ubiquitous**: Modern ADCs sample at 64–512× the audio rate,
apply a digital filter, then downsample. This relaxes the analog AAF requirements from
brick-wall to gentle rolloff, and gets noise shaping for free.

**Nyquist is for bandlimited signals**: If your signal isn't bandlimited (it has infinite bandwidth
in theory, like a square wave), you're always aliasing. Square waves, sharp edges, anything with
discontinuities has infinite bandwidth and can't be perfectly sampled. Real systems just
pre-filter (which distorts the edges).

<!-- @editor[content/P2]: Compressed sensing / sub-Nyquist sampling absent. Nyquist is the classical lower bound under the bandlimited assumption — compressed sensing (Candès, Romberg, Tao 2006; Donoho 2006) breaks it when the signal is sparse in some basis. The recovery condition (RIP, incoherence), L1 minimization (basis pursuit), and practical implications (MRI acceleration, single-pixel camera, spectrum sensing) are explicitly in the learner's "does need" list. This is a significant modern extension of sampling theory that belongs here. -->
