# Information Theory — Shannon, Nyquist, Hamming

## Era Overview

```
INFORMATION THEORY: 1924–1960
===============================

  1924 ─── NYQUIST: "Certain Factors Affecting Telegraph Speed"
           Sampling theorem precursor. Bandwidth limits transmission rate.

  1927 ─── NYQUIST-JOHNSON noise formula (thermal noise floor).

  1928 ─── HARTLEY: "Transmission of Information"
           Logarithmic measure of information. Precursor to Shannon entropy.

  1937 ─── SHANNON: MIT master's thesis.
           Proves Boolean algebra maps to electrical switching circuits.
           (Arguably the most important master's thesis in history.)

  1948 ─── SHANNON: "A Mathematical Theory of Communication"
           Bell System Technical Journal. Two-part paper.
           Defines: entropy, channel capacity, source/channel coding theorems.
           Establishes information theory as a discipline.

  1949 ─── SHANNON: "Communication in the Presence of Noise"
           Nyquist-Shannon sampling theorem formalized.

  1950 ─── HAMMING: "Error Detecting and Error Correcting Codes"
           Bell System Technical Journal.
           Hamming codes — first systematic error-correcting codes.

  1959 ─── SHANNON: "Coding for a Noisy Channel" — capacity bounds tightened.
```

---

## Claude Shannon (1906–2001)

### Bio Snapshot

MIT undergraduate (electrical engineering + mathematics), MIT master's, Bell Labs 1941–1956, MIT professor 1957–1978. Known for riding unicycles down Bell Labs hallways while juggling. Became a reclusive investor in his later years (early tech stocks). Died of Alzheimer's.

### The 1937 Master's Thesis

Shannon's master's thesis, "A Symbolic Analysis of Relay and Switching Circuits," proved that the algebra Boole invented in 1854 as an abstract system of logic maps perfectly onto the behavior of electrical switches in series and parallel.

```
BOOLEAN ALGEBRA ↔ SWITCHING CIRCUITS
======================================

  Boolean AND  ↔  Switches in series (both must close)
  Boolean OR   ↔  Switches in parallel (either can close)
  Boolean NOT  ↔  Inverter (normally-closed relay)
  Boolean 1    ↔  Closed circuit (current flows)
  Boolean 0    ↔  Open circuit (no current)

  Before Shannon: engineers designed circuits by intuition and trial-and-error.
  After Shannon:  circuit design = algebraic manipulation.
                  Minimize a Boolean expression = minimize transistor count.
                  Prove circuit equivalence = prove algebraic equality.
```

This is the bridge that makes digital computing possible. Without it, there is no principled way to design or verify logic circuits. The thesis was submitted in 1937 when Shannon was 21.

### The 1948 Paper — Information Theory

"A Mathematical Theory of Communication" solved a fundamental engineering question: what is the maximum rate at which you can transmit information reliably over a channel with noise?

**Entropy — measuring information**:

```
SHANNON ENTROPY
================

  For a discrete random variable X with outcomes x₁,...,xₙ
  and probabilities p₁,...,pₙ:

  H(X) = -Σᵢ pᵢ log₂(pᵢ)   [bits]

  Properties:
    H = 0     when one outcome has probability 1 (no uncertainty)
    H = log₂n when all n outcomes are equally likely (maximum uncertainty)
    H ≥ 0     always

  EXAMPLES:
    Fair coin: H = -(0.5 log₂ 0.5 + 0.5 log₂ 0.5) = 1 bit

    Biased coin (p=0.9, 1-p=0.1):
      H = -(0.9 log₂ 0.9 + 0.1 log₂ 0.1) ≈ 0.469 bits
      (less uncertainty → less information per toss)

    English text: H ≈ 1.0–1.5 bits/character
      (high redundancy — you can often predict the next letter)

    Random binary: H = 1 bit/bit
      (maximum entropy = no compressibility)
```

**Why entropy matters for compression**: Shannon proved that the theoretical minimum average codeword length to encode symbols from source X is H(X) bits/symbol. No compression algorithm can do better on average. This is the source coding theorem.

```
SOURCE CODING THEOREM (Shannon, 1948)
=======================================

  Any source with entropy H can be compressed to H bits/symbol on average.
  No lossless compression can achieve fewer than H bits/symbol on average.

  Compression = removing redundancy.
  Redundancy = H_max - H(X)  where H_max = log₂(alphabet size)

  IMPLICATIONS:
    gzip, zip, zstd, lzma — all provably cannot exceed Shannon's bound
    JPEG, MP3, HEVC — lossy; they sacrifice fidelity to go below Shannon
    Shannon tells you when a compressor is near-optimal
    Shannon tells you when you are wasting bits
```

**Channel capacity — the noisy channel theorem**:

```
CHANNEL CAPACITY — SHANNON-HARTLEY THEOREM
============================================

  For a channel with bandwidth B (Hz) and signal-to-noise ratio S/N:

  C = B · log₂(1 + S/N)   [bits/second]

  This is the maximum rate at which information can be transmitted
  with ARBITRARILY SMALL error probability.

  EXAMPLES:
    Phone line: B = 3400 Hz, SNR ≈ 1000 (30 dB)
    C = 3400 · log₂(1001) ≈ 33,900 bits/second ≈ 34 Kbps
    (This is why 56K modems were the theoretical ceiling on phone lines)

    WiFi 802.11n: B = 20 MHz, SNR ≈ 1000
    C = 20×10⁶ · log₂(1001) ≈ 200 Mbps (per stream, theoretical max)

  Shannon says: you CAN approach C with proper coding.
  Shannon does NOT say how to achieve it.
  (Finding capacity-achieving codes took decades — turbo codes 1993,
   LDPC codes ~2001, polar codes 2009)
```

**The noisy channel coding theorem**: This is Shannon's most surprising result. It says that for any channel with capacity C, you can transmit at any rate R < C with arbitrarily small error probability — just by using a sufficiently clever code. The noise does not ultimately limit reliability; it limits rate.

```
NOISY CHANNEL CODING THEOREM
==============================

  For any rate R < C (channel capacity):
    ∃ a code with rate R such that the probability of
    decoding error can be made arbitrarily small.

  For any rate R > C:
    The probability of error is bounded away from 0,
    regardless of the code used.

  The PROOF is probabilistic: Shannon showed random codes
  achieve this, but didn't construct the codes explicitly.
  Finding good explicit codes was the work of the next 50 years.

  This is the theoretical basis for:
    - TCP/IP error detection and retransmission
    - Forward error correction (FEC) in storage and telecom
    - QR codes
    - Hard drives (LDPC codes recover from ~10⁻¹⁵ bit error rate)
    - Space probes (Reed-Solomon codes on Voyager)
```

### Shannon's Other Contributions

- **Cryptography**: "Communication Theory of Secrecy Systems" (1949) — proved one-time pads are perfectly secure, defined confusion vs. diffusion, laid foundations for modern cryptanalysis
- **Artificial intelligence**: "Programming a Computer for Playing Chess" (1950) — first systematic analysis of computer chess, min-max search, evaluation functions
- **Information and uncertainty**: The connection between Shannon entropy and thermodynamic entropy (Boltzmann's H) was noted by Shannon himself and later formalized by Jaynes — they are the same mathematical object

---

## Harry Nyquist (1889–1976)

### Bio Snapshot

Swedish-American engineer. Bell Telephone Laboratories for 37 years. 138 patents. Known for the Nyquist sampling theorem, Nyquist stability criterion (control theory), and thermal noise analysis.

### The Nyquist-Shannon Sampling Theorem

```
NYQUIST-SHANNON SAMPLING THEOREM
==================================

  A bandlimited continuous signal with maximum frequency f_max
  can be perfectly reconstructed from discrete samples taken
  at a rate of at least 2·f_max samples per second.

  The Nyquist rate = 2·f_max.

  EXAMPLES:
    Human hearing: 20 Hz to 20 kHz
    CD audio sample rate: 44,100 Hz  (> 2 × 20,000 = 40,000 Hz)
    Phone audio: 0–4 kHz → 8,000 samples/second (standard PSTN)
    HD video: captured at 24/30/60 fps (temporal sampling)

  WHY IT WORKS (intuition):
    At 2·f_max samples/sec, you capture one sample per half-cycle
    of the highest frequency. That is enough to characterize a
    sinusoid (the fundamental building block of all signals).
    Fewer samples → aliasing: high frequencies masquerade as low.

  ALIASING (sampling below Nyquist rate):
    A 5 kHz tone sampled at 8 kHz looks like a 3 kHz tone.
    A film camera at 24 fps makes wagon wheels appear to spin backward.
    Aliased data cannot be unaliased — information is lost.
```

**Who formally proved it**: Nyquist described the relationship in 1924–1928. Shannon proved it formally in 1949. Whittaker (1915) had earlier mathematical antecedents. Kotelnikov (USSR, 1933) independently proved it. The theorem is often called the Nyquist-Shannon-Kotelnikov theorem in Europe.

**Impact**: The theorem is why every analog-to-digital converter in existence includes a low-pass (anti-aliasing) filter before the sampling stage. It is the theoretical basis for the entire field of digital signal processing and all digital audio/video.

---

## Richard Hamming (1915–1998)

### Bio Snapshot

American mathematician. Los Alamos during the Manhattan Project. Bell Labs 1946–1976. Naval Postgraduate School. Known for inventing Hamming codes, Hamming distance, and Hamming window (signal processing). Also known for his lecture "You and Your Research" — required reading for anyone doing technical work.

### Hamming Codes

**The problem**: Bell Labs in 1947 used relay computers to run programs on weekends. Errors caused by relay failures would corrupt calculations, detected only when someone read the printout Monday morning — after running all weekend. Hamming wanted automatic error detection and correction.

```
ERROR DETECTION VS. ERROR CORRECTION
======================================

  Parity bit (detection only):
    Add 1 bit such that total 1-bits is even.
    Can detect single-bit errors.
    Cannot locate the error → cannot correct.

  Hamming code (detection + correction):
    Add enough parity bits to uniquely identify which bit flipped.
    Correct it automatically.
    Key: each parity bit covers a specific subset of data bits.
```

```
HAMMING(7,4) CODE — HOW IT WORKS
==================================

  4 data bits + 3 parity bits = 7-bit codeword.

  Bit positions:  1  2  3  4  5  6  7
  Types:          p  p  d  p  d  d  d
                  (p=parity, d=data)

  Parity bit p1 (pos 1) covers: 1, 3, 5, 7
  Parity bit p2 (pos 2) covers: 2, 3, 6, 7
  Parity bit p4 (pos 4) covers: 4, 5, 6, 7

  The "coverage" pattern: each position is covered by the
  parity bits whose positions sum to it.
  Position 5 = 4+1 → covered by p1 and p4.

  ERROR CORRECTION:
    When you receive a codeword, check each parity bit.
    If parity bit at position 2^k fails, set bit k of syndrome.
    The syndrome value = binary position of the flipped bit.

  Example: bit 5 flipped
    p1 covers position 5 → p1 fails → syndrome bit 0 = 1
    p2 does not cover pos 5 → p2 passes → syndrome bit 1 = 0
    p4 covers position 5 → p4 fails → syndrome bit 2 = 1
    Syndrome = 101₂ = 5₁₀ → flip bit 5 → corrected.

  HAMMING BOUND: minimum bits needed to correct t errors in n-bit word:
    n - k ≥ log₂(Σᵢ₌₀ᵗ C(n,i))
    Where k = data bits, n-k = parity/check bits.
```

**Hamming distance**: The Hamming distance between two strings is the number of positions where they differ. Hamming codes guarantee that any two valid codewords differ in at least 3 positions (Hamming distance ≥ 3). This means:
- A single-bit error cannot produce another valid codeword → detectable and correctable
- A double-bit error produces an invalid codeword → detectable but not correctable

**Legacy**: Hamming codes are the ancestors of all modern error-correcting codes. Every RAID array (the technology you know from storage systems), every ECC RAM module, every QR code, every CD/DVD, every flash storage device, every satellite link — uses error correction that traces directly to Hamming's 1950 paper. The math is deeper now (Reed-Solomon, LDPC, polar codes) but the fundamental framework is Hamming's.

---

## Comparison Table

| Figure | Life | Key Work | Problem Solved | Legacy |
|--------|------|---------|---------------|--------|
| Shannon | 1906–2001 | Mathematical Theory of Communication (1948) | How much information? How much noise-resilient throughput? | Entire field of information theory, compression, coding |
| Nyquist | 1889–1976 | Sampling theorem (1924/1949) | How to digitize analog signals | All ADCs, digital audio/video |
| Hamming | 1915–1998 | Error-correcting codes (1950) | How to recover from bit errors | ECC RAM, RAID, QR codes, all storage |

---

## Who to Cite for What

| Concept | Figure |
|---------|--------|
| Information entropy definition | Shannon (1948) |
| Source coding theorem (compression limit) | Shannon (1948) |
| Channel capacity (Shannon-Hartley formula) | Shannon + Hartley |
| Noisy channel coding theorem | Shannon (1948) |
| Perfect secrecy / one-time pad | Shannon (1949) |
| Nyquist rate / sampling theorem | Nyquist (1924), Shannon (1949 proof) |
| Aliasing | Nyquist-Shannon |
| Hamming distance | Hamming (1950) |
| Error-correcting codes (first systematic) | Hamming (1950) |
| Boolean algebra → digital circuits | Shannon (1937 thesis) |

---

## Common Confusion Points

**"Shannon's entropy is just compression ratio."**
Entropy is the theoretical minimum. Actual compression algorithms (gzip, zstd) approach this limit for typical data but can never consistently beat it. The entropy tells you whether your compressor has room for improvement.

**"The Nyquist frequency is the sampling rate."**
The Nyquist frequency is HALF the sampling rate — it is the maximum frequency that can be represented. A 44,100 Hz sample rate can represent signals up to 22,050 Hz (the Nyquist frequency).

**"Hamming codes protect against any number of errors."**
Standard Hamming codes correct single-bit errors and detect (but cannot correct) double-bit errors. Extended Hamming codes (SEC-DED — single error correct, double error detect) add one more parity bit and are standard in ECC RAM. RAID 5/6 uses more sophisticated codes (Reed-Solomon variants) for multi-drive fault tolerance.

**"ECC RAM is about data integrity, not error correction."**
Both. ECC RAM detects and corrects single-bit errors silently during normal operation. Servers have ECC RAM because in production, cosmic rays and DRAM cell leakage cause occasional bit flips — without ECC, a flipped bit in kernel memory causes a silent corruption that may manifest hours later as mysteriously wrong results or a crash. ECC makes these events correctable. This is Hamming's contribution running inside every server you have ever deployed.
