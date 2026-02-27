# Spectral Estimation — A Layered Guide

## The Big Picture

Spectral estimation is the problem of estimating the PSD of a random process from a
finite observed record. The fundamental challenge: you never have the true, infinite-length
signal — only a short, noisy window of it.

```
THE SPECTRAL ESTIMATION PROBLEM

True PSD (unknown):   Sxx(f) = "What are the frequency components?"

Available data:        x[0], x[1], ..., x[N-1]   (N finite samples)
                       N is always too small for perfect estimation

                            │
                            ▼
                    Estimation method
                            │
                            ▼
              Ŝxx(f) = estimated PSD   ←── has variance/bias

TRADE-OFFS:
• Frequency resolution: Δf ≈ 1/T (where T = N·Ts = record length)
  More data → finer resolution — cannot be overcome
• Variance: how much the estimate fluctuates
  More data or averaging → lower variance
• Bias: systematic offset from true PSD (from windowing, model mismatch)

KEY INSIGHT: For fixed N, there's a fundamental trade-off between
frequency resolution and variance. You cannot have both simultaneously.
```

---

## The Periodogram

Simplest estimate: compute |DFT|² / N.

```
PERIODOGRAM DEFINITION

I_x(f_k) = (1/N) |X[k]|² = (1/N) |Σ x[n] e^{-j2πkn/N}|²
                                    n=0

where f_k = k·fs/N   (k = 0, 1, ..., N-1)

INTERPRETATION:
The periodogram is the squared magnitude of the DFT, normalized by N.
It's the sample version of the PSD.
```

**The periodogram problem — variance**:

```
E[I_x(f)] ≈ Sxx(f)    (asymptotically unbiased — good)

BUT: Var[I_x(f)] ≈ S²xx(f)   (variance equals the square of what we're estimating!)

This means: as N → ∞, the periodogram does NOT converge to Sxx(f) in mean-square.
The estimate stays noisy regardless of how long the record is.

WHY: Each DFT coefficient X[k] is a complex Gaussian r.v.
     |X[k]|² = |Re(X[k])|² + |Im(X[k])|² follows chi-squared(2) distribution
     → 100% coefficient of variation (std/mean = 1) for all N
```

This is the fundamental reason Bartlett (1948) invented the averaged periodogram.

---

## Welch Method

Welch's method reduces variance by averaging multiple periodograms.

```
WELCH METHOD ALGORITHM

1. Divide N-sample record into K overlapping segments of length M:
   ┌─────────────────────┐
   │ Segment 1 (length M)│
   └─────────────────────┘
         ┌─────────────────────┐
         │ Segment 2 (50% overlap)│
         └─────────────────────┘
               ┌─────────────────────┐
               │ Segment 3           │
               └─────────────────────┘

2. Apply window to each segment: w[n]·xₖ[n]

3. Compute periodogram for each segment:
   I_k(f) = (1/MU) |Σ w[n]·xₖ[n]·e^{-j2πfn}|²
   where U = (1/M)Σw²[n] (normalizes for window power)

4. Average all periodograms:
   Ŝxx(f) = (1/K) Σ I_k(f)

RESULT:
• Variance ≈ S²xx(f)/K   (K× reduction from averaging K segments)
• Frequency resolution ≈ 1/(M·Ts)   (set by segment length M, not total N)

TRADE-OFF: Using short segments (K↑) reduces variance but loses frequency resolution.
           Using long segments (K↓) preserves resolution but keeps variance high.
```

**Typical parameters**: 50% overlap, Hann window, segment length M = N/8 to N/4.
At 50% overlap with Hann window: K ≈ 2N/M independent estimates.

---

## Multitaper Spectral Estimation

Multitaper (Thomson, 1982) uses multiple orthogonal windows (tapers) applied simultaneously.

```
MULTITAPER METHOD

Key insight: One window = one taper = one periodogram.
             But multiple orthogonal tapers → multiple uncorrelated estimates.

DPSS (Discrete Prolate Spheroidal Sequences / Slepian sequences):
Optimal tapers that are:
• Maximally concentrated within bandwidth W = K/(N·Ts)
• Orthogonal to each other
• First K tapers are effectively independent (K ≈ 2NW - 1)

Algorithm:
1. Compute first K DPSS tapers {hₖ[n]}, k = 0, ..., K-1
2. For each taper: Yₖ(f) = Σ hₖ[n]·x[n]·e^{-j2πfn}
3. K eigenspectra: Sₖ(f) = |Yₖ(f)|²
4. Average: Ŝ(f) = (1/K) Σ Sₖ(f)

ADVANTAGE: K estimates averaged with only 2W bandwidth leakage.
           Better bias/variance than Welch for same record length.
COST:      Must compute K DFTs instead of 1.
           Bandwidth W must be chosen (sets taper properties).
```

---

## Parametric Methods: AR/ARMA

Instead of non-parametric (direct FFT), model the signal as output of a filter driven by white noise.

```
AR (AutoRegressive) MODEL OF ORDER p:

x[n] = -a₁x[n-1] - a₂x[n-2] - ... - aₚx[n-p] + w[n]

x[n] is a linear combination of past p samples + white noise w[n].

PSD:           Ŝxx(f) = σ²_w / |A(f)|²

where A(f) = 1 + a₁e^{-j2πf} + ... + aₚe^{-j2πpf}
      σ²_w = white noise variance

ESTIMATION: Yule-Walker equations (solve linear system for {aₖ} given autocorrelation estimates)
            or Burg algorithm (robust, forward-backward LP).

WHY USEFUL: AR model can represent sharp spectral peaks with very few parameters.
            A 6th-order AR can model 3 sinusoids — no window effects, high resolution.
            Welch might need 1000 points to achieve the same resolution.
```

**ARMA** adds moving-average terms: x[n] = Σaₖx[n-k] + Σbₖw[n-k].
More general but harder to estimate (nonlinear parameter estimation).

---

## MUSIC and ESPRIT: Subspace Methods

High-resolution methods for sinusoidal signals in noise. Can resolve closely spaced frequencies
with very short data records.

```
SIGNAL MODEL:

x[n] = Σ αₖ e^{j2πfₖn} + noise     (p complex sinusoids + white noise)
        k=1

EIGENDECOMPOSITION OF COVARIANCE MATRIX:

Rxx = E[x·xᴴ] = Σ σₖ² vₖvₖᴴ

After eigendecomposition, the eigenvectors split into:
• Signal subspace: K eigenvectors corresponding to K largest eigenvalues
• Noise subspace: N-K eigenvectors corresponding to smallest eigenvalue σ²_n

KEY PROPERTY: The steering vectors e(f) = [1, e^{j2πf}, ..., e^{j2πf(N-1)}]ᵀ
              for the true frequencies fₖ are ORTHOGONAL to the noise subspace.
```

**MUSIC (MUltiple SIgnal Classification)**:
```
MUSIC pseudo-spectrum:

P_MUSIC(f) = ─────────────────────────────────────────
             eᴴ(f) · [noise subspace projector] · e(f)

= eᴴ(f) · Eₙ · EₙH · e(f)   (where Eₙ = noise eigenvectors)

Peaks of P_MUSIC → true frequencies (where e(f) ⊥ noise subspace → denominator → 0)

RESOLUTION: Can resolve two sinusoids separated by << 1/N·Ts (Rayleigh limit)
REQUIREMENT: Know p (number of sinusoids) in advance (or estimate it)
```

**ESPRIT (Estimation of Signal Parameters via Rotational Invariance)**:
Exploits shift structure of the signal model. Solves an eigenvalue problem.
More robust to array calibration errors than MUSIC. Gives direct frequency estimates, not a spectrum.

```
COMPARISON OF SPECTRAL ESTIMATION METHODS

Method         | Resolution | Variance | Assumptions | Computation
───────────────────────────────────────────────────────────────────
Periodogram    | 1/NTs      | S²xx     | None        | O(N log N)
Welch          | 1/MTs      | S²xx/K   | WSS         | K FFTs
Multitaper     | 2W         | low      | WSS         | K FFTs
AR(p)          | high       | low      | x is AR(p)  | O(pN) or O(p²)
MUSIC          | superhigh  | moderate | p sinusoids | O(N² + K·N)
ESPRIT         | superhigh  | good     | p sinusoids | O(N²)
```

---

## Decision Cheat Sheet

| Situation | Method |
|-----------|--------|
| Quick, general PSD estimate | Welch (50% overlap, Hann window) |
| Narrowband spectral analysis, bias control | Multitaper |
| Known AR/MA process, estimate parameters | Burg AR or Yule-Walker |
| Few sinusoids in noise, need high resolution | MUSIC or ESPRIT |
| Number of sinusoids unknown | MUSIC with model order selection (MDL/AIC) |
| Detecting a specific known frequency | Goertzel algorithm (DFT at one frequency) |
| Non-stationary signal | Short-time processing (STFT) → time-frequency |

---

## Common Confusion Points

**The periodogram doesn't converge**: This surprises people. More data makes it less noisy
in the sense that you see more detail, but variance at each frequency bin stays at ~100%
of the true value. You need averaging (Welch) or modeling (AR) to reduce variance.

**Welch resolution vs record length**: Welch resolution = 1/(M·Ts) where M = segment length,
NOT the full record N. If you want 1 Hz resolution you need M ≥ 1/Hz · fs samples per segment,
regardless of total record length N.

**MUSIC assumes white noise**: The signal subspace / noise subspace separation requires that
the noise floor is flat (white). Colored noise violates this and causes MUSIC to fail.
Pre-whiten the data (apply inverse filter) before MUSIC if noise is colored.

**You must know the model order**: All parametric methods (AR, MUSIC, ESPRIT) require
specifying the number of signal components p. Use Akaike Information Criterion (AIC) or
Minimum Description Length (MDL) to estimate p from data. Wrong p → split peaks or missed peaks.

<!-- @editor[content/P2]: Compressed sensing / atomic norm minimization for spectral estimation absent. MUSIC and ESPRIT are subspace methods but require knowing p and are sensitive to model mismatch. Modern alternatives: atomic norm minimization (Bhaskar et al. 2013) recovers a sparse line spectrum from compressed measurements via convex optimization — directly bridges to the learner's "sparse recovery" interest. Super-resolution via total variation / LASSO with a DFT dictionary is the same idea in discrete form. This connects spectral estimation to the convex optimization / sparse signal recovery thread that the calibration flags as needed. -->
