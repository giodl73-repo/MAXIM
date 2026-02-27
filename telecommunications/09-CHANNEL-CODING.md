# Channel Coding — A Layered Guide

## The Big Picture

Channel coding adds redundancy to information to detect and correct errors introduced by
a noisy channel. Shannon's theorem proves a capacity limit exists; modern codes approach it.

```
CHANNEL CODING IN THE COMMUNICATION CHAIN
════════════════════════════════════════════════════════════════════

Source ──► Source   ──► Channel ──► Modulate ──► [Channel] ──► Demod ──► Channel ──► Source ──► User
           Compress     Encoder     (BPSK/QAM)    + Noise       (soft      Decoder     Decomp
           (ZIP, MP3)   (add         carry          added       outputs)   (correct
                         redundancy)  bits over              FEC)        errors)
                         FEC code     air
                         ▲
                         │
                    THIS MODULE
                    (Forward Error Correction: FEC)

KEY INSIGHT: Add controlled redundancy → can correct errors.
  No redundancy: BER at threshold → reliability limited
  With FEC: operate at lower SNR for same reliability, OR achieve lower BER at same SNR
  Coding gain: SNR reduction (dB) for same BER performance
  Typical coding gain: 4–10 dB (allows operating 4–10 dB closer to noise floor)
```

---

## Shannon Capacity — The Bound

```
SHANNON-HARTLEY THEOREM:

C = B · log₂(1 + S/N)   bits/second

C = channel capacity (maximum achievable error-free rate)
B = bandwidth (Hz)
S/N = signal-to-noise ratio (linear, not dB)

This is the hard upper bound. ANY code operating below capacity can achieve
arbitrarily low BER given sufficient code length. No code exceeds capacity.

SHANNON LIMIT FOR BPSK (1 bit/symbol):
  Capacity = 1 bit/symbol at Eb/N₀ → required minimum Eb/N₀ for code rate R
  Shannon limit for rate R = 1: Eb/N₀ ≥ ln(2) = -1.59 dB

MEANING: With a rate-1 BPSK channel code:
  Without coding: need ~6.8 dB Eb/N₀ for BER 10⁻³
  Shannon limit: -1.59 dB
  Gap: 8.4 dB — this is the "Shannon gap" that 70 years of coding theory tried to close

CODING RATE R: fraction of bits that carry information (rest is redundancy)
  R = k/n  where k = information bits, n = codeword bits
  R = 1/2: half the bits are redundancy → Eb/N₀ limit = 0 dB
  R = 3/4: more efficient but less error correction
```

---

## Fundamental Coding Concepts

```
HAMMING DISTANCE AND ERROR CORRECTION

Hamming distance d(x,y): number of bit positions where x and y differ
  x = 101100
  y = 100110
  d = 2      (positions 3 and 5 differ)

For a code with minimum Hamming distance d_min:
  Error DETECTION: up to d_min - 1 errors can be detected
  Error CORRECTION: up to ⌊(d_min-1)/2⌋ errors can be corrected

EXAMPLE: Hamming (7,4) code
  k=4 information bits, n=7 codeword bits, R=4/7≈0.57
  d_min = 3 → can correct 1 bit error per 7-bit block

SYSTEMATIC CODE: first k bits are the original data, last n-k are parity/redundancy
  Makes encoding/decoding simpler; original data immediately visible in codeword

PARITY CHECK MATRIX H (n-k × n):
  H · cᵀ = 0 for any valid codeword c
  Syndrome s = H · rᵀ: if s ≠ 0, errors occurred; syndrome pattern → error location

GENERATOR MATRIX G (k × n):
  codeword c = m · G  where m is message
  For systematic: G = [I_k | P]  where P = parity portion
```

---

## Convolutional Codes

```
CONVOLUTIONAL CODES

Process input as a stream, not blocks.
Output depends on current input AND previous K-1 inputs (K = constraint length).

Example: Rate 1/2, K=3, generators G₁=111, G₂=101

Input shift register:   [m_n] [m_{n-1}] [m_{n-2}]
                          │         │          │
               G₁:  ──────●─────────●──────────●──► XOR → c₁
               G₂:  ──────●─────────────────────●──► XOR → c₂

For each input bit: 2 output bits (rate 1/2)

TRELLIS REPRESENTATION:
  State = contents of shift register (K-1 bits)
  Transition: input bit → new state + output bits
  Valid codewords = valid paths through trellis

VITERBI ALGORITHM (1967):
  Maximum likelihood decoding of convolutional codes
  Finds path through trellis with minimum Hamming distance to received sequence
  Complexity: O(2^K × L) where L = sequence length
  Optimal for AWGN channel
  Used in: 2G/3G cellular, satellite, DSL, storage

PUNCTURING: Remove some output bits → higher rate code
  Rate 1/2 → rate 2/3 by removing every other bit from one stream
  Standard approach for variable-rate convolutional codes
```

---

## Turbo Codes (1993)

```
TURBO CODES — THE FIRST NEAR-SHANNON CODES

Berrou, Glavieux, Thitimajshima, 1993: "Near Shannon Limit Error-Correcting Coding"
  Rate 1/2 turbo code at BER 10⁻⁵: Eb/N₀ = 0.7 dB
  Shannon limit for R=1/2: Eb/N₀ = 0 dB
  Gap: 0.7 dB — practically at the Shannon limit!

TURBO ENCODER:
         input m ──────────────────────────────────────────► (systematic bits)
                  │                                                   │
                  └──► [RSC encoder 1] ──► c₁ bits ─────────────────►│
                                                                       │
                  └──► [Interleaver] ──► m' ──► [RSC encoder 2] ──► c₂ bits

RSC: Recursive Systematic Convolutional code
Interleaver: permutes the input bits pseudo-randomly

Output: [m, c₁, c₂] = rate 1/3 or punctured to higher rate

TURBO DECODER (iterative):
  Two BCJR (MAP) soft decoders, exchange soft information (extrinsic LLRs)
  Iterate 8-16 times → approach optimal MAP decoding

  Decoder 1 ──── L-values (LLRs) ────► Decoder 2
             ◄── Updated LLRs ─────────
             → Iterate → converge to near-optimal decision

APPLICATIONS: 3G UMTS/CDMA2000, 4G LTE (data), deep space (CCSDS)
```

---

<!-- @editor[bridge/P2]: LDPC Codes section is strong on the math but missing the storage erasure coding bridge — LDPC codes are used in NAND flash (NVMe SSDs), HDDs, and optical communications; the same code family (sparse parity-check matrices, belief propagation decoding) appears in Azure storage as Reed-Solomon erasure coding for geo-redundant durability; the learner's Azure infrastructure runs on these codes in every storage tier; framing LDPC as "the FEC that protects your Azure SSDs and object storage, not just wireless channels" makes this immediately practical rather than theoretical -->

## LDPC Codes (1960 / 1996)

```
LDPC (Low-Density Parity-Check) CODES

Gallager (1960): invented LDPC, largely forgotten
MacKay & Neal (1996): rediscovered, shown to approach Shannon limit

STRUCTURE: Parity check matrix H is sparse (low density of 1s)
  n = 1000 bits, k = 500 bits: H is 500×1000 with ~3-5 ones per column

FACTOR GRAPH / TANNER GRAPH:
  Variable nodes (n): one per coded bit
  Check nodes (n-k): one per parity check equation
  Edges connect variable to check nodes

BELIEF PROPAGATION DECODING:
  Message passing on Tanner graph
  Variable nodes send probability estimates to check nodes
  Check nodes update and send back revised probabilities
  Iterate 10-100 times → converge to codeword

PERFORMANCE: Approaches Shannon limit within 0.3-0.5 dB for long codes

APPLICATIONS:
  IEEE 802.11n/ac/ax (WiFi): 3 code rates × 3 block sizes
  DVB-S2 (satellite TV): 5 code rates, 2 block sizes
  10GBase-T Ethernet: 2048-bit blocks
  5G NR data channel (PDSCH): length-flexible LDPC codes
```

---

## Polar Codes (2008) — The 5G Standard

```
POLAR CODES — Arıkan (2008)

THEORETICAL BASIS:
  Channel polarization: given N = 2^n copies of a BSC channel
  Apply a butterfly transform (similar to FFT)
  → Channels split into "polarized" channels: some very reliable (capacity →1), some very noisy (capacity →0)
  → Send information on good channels, freeze bad channels to known values

ENCODING:
  G_N = F^{⊗n}  where F = [1 0; 1 1]  (Kronecker product)
  x = u · G_N   (u = information bits + frozen zeros)
  Linear complexity encoding: O(N log N)

DECODING:
  Successive Cancellation (SC): O(N log N), suboptimal
  SC-List (SCL): L paths maintained → near-optimal, O(L × N log N)
  CRC-Aided SCL: use CRC to select among list → best performance

PERFORMANCE:
  First code proven to achieve Shannon capacity for BEC (Binary Erasure Channel)
  For AWGN: slightly inferior to LDPC at finite lengths, competitive at N>10,000

5G NR ADOPTION:
  Control channel (PDCCH, PUCCH): polar codes (short blocks, 100-512 bits)
  Data channel (PDSCH, PUSCH): LDPC codes (long blocks, 1000s of bits)
  Reason: polar codes excel at short blocks; LDPC at long blocks

APPLICATIONS: 5G NR control, IoT links, satellite control
```

---

## HARQ (Hybrid ARQ)

```
HARQ: Combines FEC (forward error correction) with ARQ (automatic repeat request)

TYPE I HARQ: Send coded packet → receiver tries to decode
  Success → ACK → discard
  Failure → NACK → retransmit same packet, receiver discards old copy

TYPE II (Chase Combining): Same as Type I but receiver COMBINES retransmissions
  Soft bits from 1st and 2nd transmission summed (MRC combining)
  → SNR gain: +3 dB per additional copy (coherent combining)
  → Effective rate decreases with retransmissions

TYPE III (Incremental Redundancy, IR-HARQ):
  1st transmission: systematic bits + some parity (e.g., rate 3/4)
  If NACK: send additional parity bits (different ones)
  2nd transmission: combine → effective rate = 1/2 (more error correction)
  3rd: combine → effective rate = 1/3
  → Rate adapts automatically to channel quality

BENEFIT: Acts as adaptive modulation coding (AMC) fallback
  When channel is good: no retransmissions needed → high throughput
  When channel is bad: retransmissions → lower effective rate but reliable delivery

HARQ ROUND TRIP TIME: 4 subframes in LTE (4 × 1 ms) → 8 HARQ processes running in parallel
5G NR: flexible scheduling, mini-slots allow faster HARQ
```

---

## Decision Cheat Sheet

| Application | Code Choice | Reason |
|-------------|-------------|--------|
| 3G/4G LTE data | Turbo codes (4G) | Near-Shannon, proven |
| 5G NR data | LDPC | Better at long blocks |
| 5G NR control | Polar codes | Best at short blocks |
| WiFi 802.11n/ac/ax | LDPC | Flexible, standard |
| Satellite broadcast (DVB-S2) | LDPC + BCH outer code | Excellent threshold |
| Deep space (Voyager era) | Convolutional + Viterbi | Long constraint length |
| Storage (NAND flash, HDD) | LDPC | Low complexity at target BER |
| Quick and dirty implementation | Convolutional + Viterbi | Well-understood, libraries available |
| Ultra-reliable (URLLC 5G) | Polar + CRC + retransmission | Block error rate focus |

---

## Common Confusion Points

**"Error-correcting code" vs "source coding"**: Source coding (compression: ZIP, JPEG, MP3) removes
redundancy. Channel coding ADDS redundancy. They're opposites in purpose but applied in sequence:
compress first, then protect. If you try channel coding before compression, you're protecting
redundant bits — wasteful.

**Coding gain is not free**: LDPC at rate 1/2 corrects errors but uses 2× the bandwidth (or half
the spectral efficiency). The gain is on Eb/N₀ (energy per BIT), not on spectral efficiency.
You pay bandwidth to get coding gain. For power-limited channels (satellite), this trade is worth it.
For bandwidth-limited channels (cellular spectrum), you want highest-rate codes.

**Shannon limit assumes Gaussian noise**: The Shannon-Hartley theorem is for AWGN (additive white
Gaussian noise) channels. Real channels have fading, impulsive noise, co-channel interference —
these can be better or worse than AWGN. Capacity theorems exist for general channel models but
AWGN is the foundational case.

**Turbo codes aren't used in 5G data**: 4G LTE used turbo for data; 5G NR switched to LDPC.
Reason: at very high data rates (Gbps), turbo decoding is slow (sequential iterations, hard to
parallelize). LDPC decoding parallelizes well → enables the required throughput with reasonable chip area.
