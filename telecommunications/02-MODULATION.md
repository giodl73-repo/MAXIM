# Modulation — A Layered Guide

## The Big Picture

Modulation encodes information onto a carrier wave. Choose modulation based on
the channel's SNR, available bandwidth, and required robustness.

```
MODULATION TAXONOMY
════════════════════════════════════════════════════════════════════

                         MODULATION
                              │
              ┌───────────────┴───────────────┐
           ANALOG                           DIGITAL
           (continuous message)             (discrete symbols)
              │                                │
    ┌─────────┼─────────┐         ┌────────────┼────────────┐
    AM        FM       PM         ASK         FSK          PSK/QAM
  Amplitude  Freq     Phase    Amplitude    Frequency    Phase/Amplitude
  variation  variation variation on-off     shift keying  shift keying
   CW        FM radio  used in  keying                   (plus QAM)
   AM radio  TV audio  FSK/PSK  (OOK)

                                 ┌────────────┐
                                 │    OFDM    │
                                 │(multicarrier│
                                 │ modulation) │
                                 │ LTE, WiFi   │
                                 │ 5G, cable   │
                                 └────────────┘
```

---

## Analog Modulation

### Amplitude Modulation (AM)

```
AM SIGNAL:
x(t) = A_c · [1 + k_a · m(t)] · cos(2πf_c·t)

m(t) = baseband message signal, |m(t)| ≤ 1
k_a = modulation index (0 to 1)
f_c = carrier frequency

SPECTRUM:
Carrier at f_c, upper sideband at f_c ± f_m

BANDWIDTH: BW = 2 × message bandwidth B_m
AM radio: B_m ≈ 5 kHz → BW = 10 kHz (fits in AM channel spacing)

INEFFICIENCY: Carrier carries no information but uses 50-67% of power
DSB-SC (double-sideband suppressed carrier): no carrier, more efficient
SSB (single-sideband): one sideband only, BW = B_m, most efficient

PROS: Simple receiver (envelope detector); can receive with no PLL
CONS: Power inefficient; susceptible to amplitude noise
```

### Frequency Modulation (FM)

```
FM SIGNAL:
x(t) = A_c · cos(2πf_c·t + 2πk_f·∫m(τ)dτ)

k_f = frequency sensitivity (Hz/V)
Instantaneous frequency: f_i(t) = f_c + k_f·m(t)
Frequency deviation: Δf = k_f · max|m(t)|
Modulation index: β = Δf/B_m   (β >> 1 is "wideband FM")

BANDWIDTH (Carson's rule): BW ≈ 2(Δf + B_m) = 2(β+1)B_m
FM broadcast: Δf = 75 kHz, B_m = 15 kHz → BW = 180 kHz → channel spacing 200 kHz

FM NOISE ADVANTAGE:
FM acts like spreading spectrum: trading bandwidth for SNR improvement
SNR_FM / SNR_AM = 3β²(β+1) (wideband FM much better than AM for same power)
FM broadcast with β=5: 27 dB better SNR than comparable AM signal

PROS: Excellent noise immunity; constant amplitude (easy to amplify)
CONS: Bandwidth expensive; requires wider channel than AM
```

---

## Digital Modulation: Phase and Amplitude

### Constellation Diagrams

In digital modulation, each symbol represents k = log₂(M) bits, where M = constellation size.
A constellation diagram plots I (in-phase) vs Q (quadrature) components.

```
COMMON CONSTELLATIONS

BPSK (2 symbols = 1 bit/symbol):
  Q
  │    ●           ●
  │   -1           +1 → I
  │   (1)          (0)
  Simple, most robust, used when channel is terrible

QPSK (4 symbols = 2 bits/symbol):
  Q
  ●│●    Symbols at 45°, 135°, 225°, 315°
  ─┤─
  ●│●
    I
  2 bits/symbol with same BW as BPSK → 2× spectral efficiency

16-QAM (16 symbols = 4 bits/symbol):
  Q  ●●●●
     ●●●●
     ●●●●
     ●●●●  I
  4 bits/symbol, 4× BPSK — needs higher SNR

64-QAM (6 bits/symbol):
  8×8 grid
  6 bits/symbol — even higher SNR needed

256-QAM (8 bits/symbol), 1024-QAM (10 bits/symbol): used in 4G/5G downlink
```

### BER vs SNR

```
PROBABILITY OF BIT ERROR vs Eb/N₀

             10⁻¹
BER          │──────────────────────── random guessing
             │
             10⁻² ─ ● BPSK/QPSK
             │         ●
             10⁻³ ─      ●
             │
             10⁻⁴ ─       ● 16-QAM needs ~5 dB more SNR than QPSK
             │              ●
             10⁻⁵ ─            ● 64-QAM another ~5 dB more
             │
             10⁻⁶ ─
             └──────────────────────────────────────────►
             0      5      10     15     20     25  Eb/N₀ (dB)

QPSK BER: Q(√(2·Eb/N₀)) ≈ (1/2)·erfc(√(Eb/N₀))
At BER = 10⁻³: Eb/N₀ ≈ 6.8 dB for QPSK; ~11 dB for 16-QAM
```

---

## OFDM: Orthogonal Frequency Division Multiplexing

<!-- @editor[bridge/P3]: OFDM section shows IFFT/FFT in the implementation block diagram but doesn't explicitly label this as "the DFT you know from signal processing or numerical methods applied to multicarrier modulation" — one sentence making this explicit ("OFDM is essentially the DFT applied to channel equalization: transform to frequency domain, apply per-subcarrier gains, transform back") would help a reader with MIT math background immediately lock in the mathematical structure rather than treating the FFT block as a mysterious DSP primitive -->

OFDM is the dominant modulation for WiFi, LTE, 5G, DVB, DOCSIS.

```
OFDM CONCEPT:

PROBLEM: Broadband channel has frequency-selective fading.
  Different frequencies have different path losses due to multipath.
  A single wideband QAM signal gets distorted differently across its bandwidth.

OFDM SOLUTION:
  Divide the bandwidth into N narrow subcarriers.
  Each subcarrier has bandwidth << coherence bandwidth of channel.
  On each narrow subcarrier: channel is flat (non-selective).
  Modulate each subcarrier independently (BPSK, QPSK, 16/64/256-QAM).
  All subcarriers transmitted simultaneously.

ORTHOGONALITY:
  Subcarrier spacing: Δf = 1/T (where T = OFDM symbol duration)
  Subcarriers are orthogonal: ∫₀ᵀ sin(2πf_k t)·sin(2πf_l t)dt = 0 for k≠l
  No interference between subcarriers — even though they overlap in frequency!

IFFT/FFT IMPLEMENTATION:
  Synthesis: IFFT{[X[0], X[1], ..., X[N-1]]} → x[n] (time-domain OFDM symbol)
  Analysis:  FFT{x[n]} → [Y[0], Y[1], ..., Y[N-1]] (demodulated symbols)
  OFDM is implemented with IFFT at transmitter, FFT at receiver. O(N log N).

  ┌──────────────────────────────────────────────────────────────────┐
  │ OFDM TRANSMITTER                                                  │
  │                                                                   │
  │ Bits → [QAM map] → [S/P] → [N-point IFFT] → [P/S] → [Add CP] → │
  │                                                                   │
  │ OFDM RECEIVER                                                     │
  │                                                                   │
  │ → [Remove CP] → [S/P] → [N-point FFT] → [1-tap equalizer per SC] → [QAM demod] → Bits │
  └──────────────────────────────────────────────────────────────────┘

CYCLIC PREFIX (CP):
  Prepend last L samples of OFDM symbol to front.
  Purpose: converts linear convolution with channel → circular convolution.
  If CP length > channel delay spread: no ISI (inter-symbol interference).
  Cost: reduces spectral efficiency by factor T/(T+CP) = N/(N+L).
```

**OFDM key parameters (LTE example)**:

```
LTE (4G) OFDM PARAMETERS:
  Subcarrier spacing: Δf = 15 kHz
  FFT size: 2048 (for 20 MHz BW)
  Useful symbol duration: T = 1/15kHz = 66.7 µs
  Cyclic prefix: 4.7 µs (normal CP) → 160 + 144 × 6 samples
  Number of resource blocks (RBs): 100 (for 20 MHz, 12 subcarriers/RB)

5G NR NUMEROLOGY:
  Multiple subcarrier spacings: μ = 0 (15 kHz) to μ = 4 (240 kHz)
  Higher μ: shorter symbol time → less latency, handles higher Doppler
  Sub-6 GHz: μ=0,1,2; mmWave: μ=2,3,4
```

---

## Spectral Efficiency Comparison

```
MODULATION SPECTRAL EFFICIENCY LADDER

Modulation    Bits/symbol   Required SNR    Applications
───────────────────────────────────────────────────────────────
BPSK           1           ~6.8 dB @BER 10⁻³  Low-SNR links, GPS
QPSK           2           ~6.8 dB @BER 10⁻³  3G CDMA, satellite
8-PSK          3           ~10 dB              DVB-S2
16-QAM         4           ~11.5 dB            LTE, WiFi
64-QAM         6           ~17.5 dB            Cable, LTE good coverage
256-QAM        8           ~24 dB              LTE high SNR, WiFi 802.11ac
1024-QAM      10           ~29 dB              Cable DOCSIS 3.1, WiFi 6
4096-QAM      12           ~35 dB              WiFi 7 (802.11be)
```

---

## Decision Cheat Sheet

| Channel Condition | Best Modulation |
|------------------|-----------------|
| Very low SNR / high BER tolerance | BPSK |
| Balanced robustness/efficiency | QPSK |
| Good SNR, need high data rate | 64-QAM or 256-QAM |
| Multipath channel (WiFi, LTE, 5G) | OFDM (handles frequency-selective fading) |
| Satellite link (power-limited) | BPSK or QPSK with strong FEC |
| Cable modem (very clean channel) | 1024-QAM or 4096-QAM |
| FM radio (analog, noise immune) | Wideband FM (β = 5) |
| Backup emergency comms (robust) | BPSK + LDPC or turbo codes |

---

## Common Confusion Points

**OFDM doesn't reduce peak-to-average power ratio (PAPR) problem**: OFDM signals have high PAPR
(up to 10-12 dB) because N subcarriers can add in phase occasionally. This requires linear amplifiers
with power backoff → reduces power efficiency. This is a major practical drawback. 5G uplink
uses DFT-spread OFDM (SC-FDMA in LTE, π/2 BPSK in 5G) to reduce PAPR from the mobile.

**QPSK has same Eb/N₀ requirement as BPSK**: For the same BIT error rate, QPSK (2 bits/symbol)
requires the same Eb/N₀ as BPSK (1 bit/symbol). QPSK doubles spectral efficiency "for free"
in terms of required SNR per bit. This is a key insight — the "cost" is in the symbol SNR, not bit SNR.

**Bandwidth efficiency vs power efficiency**: BPSK is power-efficient but bandwidth-inefficient.
256-QAM is bandwidth-efficient but power-inefficient. Spread spectrum (DSSS, FHSS) trades bandwidth
for power efficiency (operates below noise floor). These trade-offs define the design space.

**Constellation size is adaptive in modern systems**: LTE/5G and WiFi use Adaptive Modulation and
Coding (AMC) — continuously select modulation and coding rate based on measured channel conditions.
Near the base station: 256-QAM. Cell edge: QPSK. This is why speeds drop as you move away from the AP.
