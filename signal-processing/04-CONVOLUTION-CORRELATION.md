# Convolution and Correlation — A Layered Guide

## The Big Picture

Convolution and correlation are the fundamental operations of LTI signal processing.
Convolution IS filtering. Correlation IS similarity measurement.

```
OPERATIONS OVERVIEW
════════════════════════════════════════════════════════════════════

Convolution (x ★ h):               Correlation (Rxy):

y[n] = Σ x[k] · h[n-k]            Rxy[n] = Σ x[k] · y[k+n]
        k                                     k

LTI filter output                  Similarity measurement

h is FLIPPED and slid              y is slid over x (no flip)
over x                             Measures lag/time offset

Use: filtering, blur, edge detect  Use: radar, sonar, match filter,
     reverb, FIR implementation         time delay estimation

═══════════════════════════════════════════════════════════════════

KEY CONNECTION:
Convolution in time ↔ Multiplication in frequency
F{x ★ h} = X(f) · H(f)     ← fundamental theorem
This is why FFT-based filtering is O(N log N) instead of O(N²)
```

---

## Linear Convolution

For sequences x[n] of length M and h[n] of length L:
- Output y[n] = x[n] ★ h[n] has length M + L - 1
- Linear convolution is acyclic (no wraparound)

```
LINEAR CONVOLUTION EXAMPLE
x = [1, 2, 3]   (M=3)
h = [1, 1]      (L=2)

Method: flip h, slide over x, multiply and sum at each position:

n=0:    h flip = [1,1], align: h=[1,1] × x=[1,2,3] → 1·1 + 0 = 1
n=1:    [1,1] shifted: h=[1,1] × x=[1,2,_] → 1·2 + 1·1 = 3
n=2:    [_,1,1] × x=[_,2,3] → 1·3 + 1·2 = 5
n=3:    [__,1,1] × x=[__,3,_] → 1·3 + 0 = 3

y = [1, 3, 5, 3]   length = 3+2-1 = 4  ✓
```

**Graphical interpretation**: Convolution is the area of overlap between x and a
flipped, sliding version of h as a function of offset n.

**Properties**:
- Commutativity: x ★ h = h ★ x
- Associativity: (x ★ h₁) ★ h₂ = x ★ (h₁ ★ h₂)  (cascade = single filter)
- Distributivity: x ★ (h₁ + h₂) = (x ★ h₁) + (x ★ h₂)  (parallel = add filters)
- Identity: x ★ δ = x  (delta is identity for convolution)

---

## Circular Convolution

DFT-based convolution is inherently circular — it assumes the signal is periodic with period N.

```
LINEAR vs CIRCULAR (N-point DFT)

Linear convolution:     y_lin[n] = Σ x[k]·h[n-k],  length = M+L-1
                                    k

Circular convolution:   y_circ[n] = Σ x[k]·h[(n-k) mod N]
                                      k

PROBLEM: If N < M+L-1, the circular convolution wraps around:
  y_lin   = [1, 3, 5, 3,  0,  0, ...]  (linear, zero tail)
  y_circ  = [1+3, 3+0, 5+0, 3+0] = [4, 3, 5, 3]  for N=4
             └── aliasing from wrap! ─┘

SOLUTION: Zero-pad both x and h to length ≥ M+L-1 before DFT.
Then circular convolution equals linear convolution.
```

**DFT-based filtering**:
```
y = IFFT{ FFT{x} × FFT{h} }   with N ≥ M+L-1
```
Complexity: O(N log N) vs O(N²) for direct method.

---

## Long-Input Convolution: Overlap-Add / Overlap-Save

For streaming audio/real-time filtering, input x is continuous (infinite) while filter h has
finite length L. Process in blocks.

```
OVERLAP-ADD METHOD

Filter h: length L
Input x: broken into blocks of length M (non-overlapping)

For each block xₖ:
1. Zero-pad xₖ to length N ≥ M+L-1
2. FFT(xₖ) × FFT(h)  (precompute FFT of h)
3. IFFT → yₖ of length N = M+L-1
4. Each yₖ output has L-1 samples of "tail" that overlap with next block
5. Add overlapping parts → correct linear convolution output

OUTPUT ASSEMBLY:
Block 1:  [────────────────────]tail₁
Block 2:  [────────────────────]tail₂
                            tail₁+[tail of block2 start]
```

```
OVERLAP-SAVE METHOD (more common in practice)

Keep a sliding buffer of length N = M+L-1 (overlapping input)
1. Fill buffer (L-1 old samples + M new samples)
2. Compute N-point FFT of buffer
3. Multiply by H[k]
4. IFFT
5. Discard first L-1 samples (they contain circular aliasing)
6. Output M valid samples
7. Slide buffer: keep last L-1 samples for next block
```

**Computational cost**: N = M+L-1 ≈ next power of 2.
For M=1024 input block, L=256 filter: N=2048, cost ≈ 2048·log₂(2048)/1024 ≈ 22 mults/sample.
Compare: direct convolution = 256 mults/sample. 11× speedup.

---

## Cross-Correlation

Cross-correlation measures the similarity between x and y as a function of time lag τ:

```
Rxy[n] = Σ x[k] · y[k+n] = Σ x[k] · y[k+n]
          k                  k

or equivalently: Rxy[n] = x[-n] ★ y[n]  (convolution with x reversed)

Normalized: ρxy[n] = Rxy[n] / √(Rxx[0]·Ryy[0])   ∈ [-1, +1]
```

**Key insight**: Rxy[n] peaks at n = n₀ when y is a delayed copy of x by n₀ samples.
This gives the time delay estimate.

**Applications**:
- **Radar/sonar**: transmitted pulse correlated with received echo → range
- **Time delay estimation**: two microphones, find which signal arrived first
- **GPS**: known C/A code correlated with received signal → time of arrival → position
- **Vibration analysis**: find resonances, transfer functions

---

## Autocorrelation

Autocorrelation is cross-correlation of a signal with itself:

```
Rxx[n] = Σ x[k] · x[k+n]
          k

PROPERTIES:
• Rxx[0] = Σ|x[k]|² = signal energy (peak at zero lag)
• Rxx[n] = Rxx[-n]  (even function, symmetric)
• |Rxx[n]| ≤ Rxx[0] for all n
• For periodic x with period P: Rxx[n] is also periodic with period P

FOURIER PAIR:
F{Rxx[n]} = |X(f)|² = Power Spectral Density (PSD)
→ Wiener-Khinchin theorem (see 06-STOCHASTIC)
```

---

## Matched Filter

The matched filter maximizes SNR at a specific time instant in the presence of white noise.

```
MATCHED FILTER DESIGN

Given known signal s[n] of length L contaminated by noise:
Received: x[n] = α·s[n - n₀] + w[n]   (delayed signal + white noise)

Optimal filter: h[n] = s[L-1-n]  (time-reversed version of s)
Filter output: y[n] = x[n] ★ h[n] = Rsx[n]  (cross-correlation)

At n = n₀ + L - 1:
  Signal term: α · Rss[0] = α · ∫|s|²   (maximum possible, by Cauchy-Schwarz)
  Noise term:  minimum

Peak SNR = 2·E_s / N₀   where E_s = signal energy, N₀ = noise PSD

RADAR PULSE COMPRESSION:
Transmit long coded pulse (high energy) → correlate with replica →
detect narrow pulse (high range resolution) with full energy
This is why radar waveforms are designed for good autocorrelation properties
(low sidelobes) — LFM chirp, phase-coded sequences (Barker codes, Gold codes).
```

---

## Decision Cheat Sheet

| Task | Method |
|------|--------|
| Apply FIR filter to short signal | Direct convolution (sum products) |
| Apply FIR filter to long streaming signal | Overlap-save or overlap-add |
| Long filter × long signal | FFT × FFT, IFFT |
| Detect known signal in noise | Matched filter (correlate with replica) |
| Estimate time delay between two signals | Cross-correlation peak |
| Measure signal energy | Autocorrelation at lag 0 |
| Detect periodicity in a signal | Autocorrelation for recurring peaks |
| Implement 2D image filtering | 2D convolution (separable if possible) |

---

## Common Confusion Points

**Convolution flips, correlation doesn't**: h[n-k] in convolution reverses h.
Rxy[n] = Σx[k]y[k+n] slides y without flipping. The difference matters when
the signals are not symmetric.

**Circular convolution aliasing**: If you take IFFT{FFT{x}·FFT{h}} without zero-padding
to at least M+L-1, the output wraps around — the tail of the convolution appears at
the beginning. Always zero-pad.

**Correlation ≠ causality**: High cross-correlation at lag τ means y is predictable from
x with delay τ. It says nothing about which causes which. Fundamental statistics principle.

**Matched filter maximizes SNR, not resolution**: The matched filter output peak SNR is
2E_s/N₀. Width of the main lobe is ∼1/bandwidth(s). To improve range resolution,
increase signal bandwidth (LFM chirp, phase codes), not output SNR.
