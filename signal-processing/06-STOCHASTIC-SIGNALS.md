# Stochastic Signals — A Layered Guide

## The Big Picture

A stochastic signal is one that can only be described statistically — no formula predicts
each sample exactly. Noise, turbulence, financial prices, ECG variability are all stochastic.
The power spectral density (PSD) is the frequency-domain description of a random process.

```
STOCHASTIC SIGNAL FRAMEWORK
════════════════════════════════════════════════════════════════════

Random process X(t):          Ensemble of realizations
One realization x₁(t): ────────────────────────────────────►
Another:         x₂(t): ──────────────────────────────────►
Another:         x₃(t): ─────────────────────────────────►
                                    │
                              At any time t₀:
                              X(t₀) is a RANDOM VARIABLE
                              with a PDF p(x, t₀)

Complete description: joint PDF p(x₁, t₁; x₂, t₂; ...) — intractable in general

PRACTICAL DESCRIPTION for WSS processes:
• Mean: μ_X = E[X(t)] — constant (not a function of t)
• Autocorrelation: Rxx(τ) = E[X(t)X(t+τ)] — depends only on lag τ
• Power Spectral Density: Sxx(f) = F{Rxx(τ)}
```

---

## Random Process Definitions

**Random process** X(t): indexed collection of random variables, one for each t.

**Strict-sense stationary (SSS)**: All statistics are shift-invariant.
Joint PDF of {X(t₁), ..., X(tₙ)} = Joint PDF of {X(t₁+τ), ..., X(tₙ+τ)} for all τ, n.

**Wide-sense stationary (WSS)**: Weaker condition (sufficient for most DSP):
1. E[X(t)] = μ (constant, independent of t)
2. E[X(t)X(t+τ)] = Rxx(τ) (depends only on lag τ, not absolute time t)
3. E[|X(t)|²] < ∞

WSS is the key assumption for PSD analysis and Wiener-Khinchin.

**Ergodic**: Time averages = ensemble averages. Allows estimating statistics from a single
long realization (which is all you ever have in practice).
```
E[X(t)] = lim_{T→∞} (1/2T) ∫_{-T}^{T} x(t) dt    (ergodic in the mean)
```

---

## Autocorrelation Function

```
AUTOCORRELATION: Rxx(τ) = E[X(t) · X(t+τ)]

PROPERTIES:
• Rxx(0) = E[|X(t)|²] = average power (always ≥ 0)
• Rxx(τ) = Rxx(-τ)   (even function, symmetric)
• |Rxx(τ)| ≤ Rxx(0)  (peak at zero lag)
• For periodic X: Rxx(τ) is also periodic with same period
• For WSS X: Rxx(τ) → 0 as τ → ∞ (if X is ergodic and not periodic)

INTERPRETATION:
Rxx(τ) measures "memory" — how similar the signal is to itself τ seconds later.
• Wide Rxx → slowly varying signal (low bandwidth)
• Narrow Rxx → rapidly varying signal (high bandwidth)
• τ = 0 spike only (white noise) → completely uncorrelated sample-to-sample
```

---

## Power Spectral Density

The PSD is the Fourier transform of the autocorrelation function.

```
WIENER-KHINCHIN THEOREM:

Sxx(f) = F{Rxx(τ)} = ∫_{-∞}^{∞} Rxx(τ) e^{-j2πfτ} dτ

Inverse: Rxx(τ) = ∫_{-∞}^{∞} Sxx(f) e^{j2πfτ} df

Total power: Rxx(0) = E[|X(t)|²] = ∫_{-∞}^{∞} Sxx(f) df

PROPERTIES OF PSD:
• Sxx(f) ≥ 0 for all f  (non-negative)
• Sxx(f) = Sxx(-f)      (even for real processes)
• Units: power per Hz (W/Hz or V²/Hz)
• PSD × bandwidth = power in that band
```

**Physical meaning**: Sxx(f) tells you how much power the signal has per unit bandwidth
at frequency f. Integrate over any band to get total power in that band.

---

## Passing Random Signal Through LTI System

```
INPUT              LTI SYSTEM h(t)           OUTPUT
X(t) ─────────────► [H(f)] ────────────────► Y(t)

Output PSD:    Syy(f) = |H(f)|² · Sxx(f)
Output mean:   μ_Y = H(0) · μ_X
Output power:  E[|Y(t)|²] = ∫|H(f)|² Sxx(f) df

This is the fundamental tool for noise analysis:
• Given input noise PSD Sxx(f)
• Know filter frequency response |H(f)|²
• Output noise power = area under |H(f)|² × Sxx(f)
```

**Cross-correlation and cross-PSD**:
```
Rxy(τ) = E[X(t)·Y(t+τ)]
Sxy(f) = F{Rxy(τ)} = H(f) · Sxx(f)
```

---

## Noise Types

```
NOISE TYPE TAXONOMY

Power/Hz                         Spectral Density
   │
   │ White noise (flat):  ─────────────────────── (constant S₀)
   │
   │ Pink noise (1/f):   ╲                         (Sxx ∝ 1/f)
   │                      ╲                        common in nature
   │
   │ Red/Brownian (1/f²):  ╲                       (Sxx ∝ 1/f²)
   │                         ╲                     random walk
   │
   │ Blue noise (f):      ╱                         (Sxx ∝ f)
   │                     ╱
   │
   └─────────────────────────────────────────────────────► f
```

| Noise Type | PSD Shape | Origin | Example |
|------------|-----------|--------|---------|
| White | Flat: Sxx = N₀/2 | Thermal/shot at high freq | Resistor thermal noise |
| Pink (1/f) | Sxx ∝ 1/f | Many physical systems | Semiconductor flicker, music |
| Red/Brownian | Sxx ∝ 1/f² | Random walk (integrated white) | Wind speed, stock prices |
| Blue | Sxx ∝ f | Differentiated white | Some microphone noise |
| Violet | Sxx ∝ f² | Differentiated pink | — |
| Bandlimited white | Flat in band, 0 outside | Filtered white | ADC quantization noise |

**Thermal (Johnson-Nyquist) noise**: Unavoidable noise in any resistor at temperature T.
PSD: Sxx = 4kTR (W/Hz), where k = Boltzmann constant = 1.38×10⁻²³ J/K.
Voltage noise: √(4kTRB) V_rms over bandwidth B.

**Shot noise**: Discrete electron arrivals in semiconductors.
PSD: Si = 2qI (A²/Hz), where q = electron charge, I = DC current.

---

## Signal-to-Noise Ratio

```
SNR = Signal power / Noise power = Ps/Pn   (dimensionless ratio)
SNR_dB = 10·log₁₀(Ps/Pn)

ALTERNATIVE SNR DEFINITIONS (context matters!):

SNR (signal processing): Ps/Pn — how loud is signal vs noise

Eb/N₀ (digital comms): Energy per bit / noise density — BER performance metric

SQNR (ADC): Signal power / quantization noise power ≈ 6.02B + 1.76 dB

SINAD: Signal + noise + distortion / noise + distortion — amplifier quality

NF (noise figure, RF): NF = SNR_in/SNR_out (dB) — degradation added by component
      NF = 0 dB → ideal (no noise added); typical LNA NF ≈ 0.5–2 dB

NOISE FLOOR: Minimum detectable signal level.
   In receiver: -174 dBm/Hz + NF + 10·log(BW) + required SNR
```

---

## Cross-Spectral Density and Coherence

```
COHERENCE: measures linear correlation between two signals as function of frequency.

γ²_xy(f) = |Sxy(f)|² / (Sxx(f) · Syy(f))    ∈ [0, 1]

γ² = 1: X and Y are linearly related at frequency f (same source, deterministic relationship)
γ² = 0: X and Y are completely uncorrelated at frequency f
γ² between: linear relationship mixed with noise

USE: Identify if two sensors see the same source at which frequencies.
```

---

## Decision Cheat Sheet

| Situation | Tool |
|-----------|------|
| Characterize noise content vs frequency | PSD (Sxx) |
| Find signal memory / correlation time | Autocorrelation function Rxx(τ) |
| Estimate output noise through a filter | Syy = \|H\|² · Sxx |
| Check if two signals share a source | Coherence function γ²(f) |
| Find time delay between two noisy signals | Cross-correlation peak |
| Noise from a resistor at temperature T | Thermal noise: 4kTR W/Hz |
| Is the process stationary? | Check if mean and autocorrelation shift-invariant |
| Estimate PSD from data | Welch method (see 07-SPECTRAL-ESTIMATION) |

---

## Common Confusion Points

**White noise is an idealization**: True white noise has infinite power (Sxx = constant over
all frequencies → power = ∫Sxx df = ∞). In practice, "white" means flat within the band of
interest. Thermal noise is white up to ~6 THz (kT frequency), well beyond any circuit bandwidth.

**Ergodicity is assumed, not proven**: In practice, we estimate statistics from one long realization
and assume it's representative of the ensemble. This fails for non-ergodic processes (e.g.,
each realization has its own frequency drift — taking one realization doesn't give you the
ensemble statistics).

**PSD has units, and they matter**: For a voltage signal, PSD has units V²/Hz.
Integrate over 1 Hz bandwidth → V² → take sqrt → V_rms per √Hz.
This is why amplifier noise specs are given in nV/√Hz — makes them bandwidth-independent.

**WSS does not imply ergodic, and ergodic does not imply strict-sense stationary**:
These are independent conditions. Most DSP textbooks assume both WSS and ergodic without
being explicit about it.

<!-- @editor[content/P2]: Kalman filter absent — this is the natural capstone for stochastic signals through LTI systems. Kalman = optimal linear estimator for state-space models with Gaussian noise, equivalent to Wiener filter in the recursive/causal case. The derivation (predict → update, Riccati equation) is the practical counterpart to Wiener-Hopf. For a learner who uses Azure IoT/telemetry or control systems this is directly applicable. At minimum, note the Wiener filter → Kalman filter relationship. -->
