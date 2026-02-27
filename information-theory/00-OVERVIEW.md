# Information Theory — Landscape Overview

## The Big Picture

<!-- @editor[diagram/P2]: Diagram maps Shannon's 3 problems (1948) but doesn't show the field landscape — the 9 guide files (entropy measures, source coding, channel coding, rate-distortion, network IT, algorithmic IT, quantum IT, information geometry) and how they branch from Shannon's foundation. Rework as a layered tree: Shannon core → sub-fields → modern results. -->

```
    INFORMATION THEORY LANDSCAPE
    ══════════════════════════════════════════════════════════

    FUNDAMENTAL QUESTION: How much "information" is in a message?
    And what does that mean physically?

    SHANNON'S THREE PROBLEMS (1948):
    ┌─────────────────────────────────────────────────────────┐
    │  1. LOSSLESS COMPRESSION                                │
    │     Source → Source Encoder → Compressed bits           │
    │     Limit: entropy H(X) bits/symbol                    │
    │     Theorem: cannot compress below H(X) on average     │
    │                                                          │
    │  2. RELIABLE COMMUNICATION OVER NOISY CHANNEL           │
    │     Source → Channel Encoder → Noisy Channel →          │
    │     Channel Decoder → Sink                              │
    │     Limit: channel capacity C bits/use                  │
    │     Theorem: can communicate reliably iff R < C         │
    │                                                          │
    │  3. CRYPTOGRAPHY (1949 paper)                           │
    │     Perfect secrecy: H(M|C) = H(M) → OTP               │
    │     Key length lower bound: |K| ≥ |M|                   │
    └─────────────────────────────────────────────────────────┘

    SYSTEM DIAGRAM:
    Source → [Source Encoder] → [Channel Encoder] →
    → [Channel: p(y|x)] → [Channel Decoder] → [Source Decoder] → Sink

    Each block corresponds to a fundamental theorem.
    The source encoder compresses to H(X).
    The channel encoder adds redundancy to approach C.
    They're separate operations (source-channel separation theorem).
```

---

## Entropy: The Fundamental Measure

Shannon's entropy of a discrete random variable X with distribution p:

$$\boxed{H(X) = -\sum_{x} p(x) \log_2 p(x) \text{ bits}}$$

Interpretation: H(X) = average number of bits needed to represent one sample from X.

```
    Examples:
    Fair coin (p=0.5): H = -(0.5 log 0.5 + 0.5 log 0.5) = 1 bit
    Biased coin (p=0.9): H = -(0.9 log 0.9 + 0.1 log 0.1) = 0.469 bits
    Die (uniform, 6 faces): H = log₂ 6 = 2.585 bits
    Constant (p=1): H = 0 bits
    128 equally likely outcomes: H = 7 bits

    H(X) = minimum average description length in bits
         = average surprise: -log₂ p(x) bits for outcome x
         = average code length of optimal prefix-free code (Huffman)
```

---

## Historical Arc

| Year | Person | Contribution |
|------|--------|-------------|
| 1924 | Nyquist | Bandwidth limits telegraph transmission speed |
| 1928 | Hartley | Logarithmic measure of information: log(N) |
| 1948 | Shannon | "A Mathematical Theory of Communication" — the paper |
| 1949 | Shannon | "Communication Theory of Secrecy Systems" — crypto IT |
| 1951 | Shannon | "Prediction and Entropy of Printed English" — 1 bit/letter |
| 1954 | McMillan | Proof of Kraft inequality uniqueness |
| 1957 | Huffman | Optimal prefix-free code construction algorithm |
| 1977 | Ziv, Lempel | LZ77 (universal compression without knowing source) |
| 1978 | Pinsker | D_KL lower bound on total variation distance |
| 1990s | Gallager + others | LDPC codes rediscovered, turbo codes |
| 2009 | Arıkan | Polar codes — first provably capacity-achieving with explicit construction |

---

## Shannon's Theorems (Stated)

**Source Coding Theorem** (Shannon 1948):
For an i.i.d. source X with entropy H(X) and any ε > 0, there exists an encoding of
n symbols into n(H(X) + ε) bits that allows reliable decoding with probability → 1.
Moreover, any encoding with fewer than n(H(X) - ε) bits per symbol must have P_error bounded away from 0.

**Noisy Channel Coding Theorem** (Shannon 1948):
For a discrete memoryless channel with capacity C = max_{p(x)} I(X;Y):
- For any rate R < C: there exist codes with P_error → 0 as n → ∞.
- For any rate R > C: P_error → 1 for any code.

**Perfect Secrecy Theorem** (Shannon 1949):
A cipher achieves perfect secrecy (H(M|C) = H(M)) if and only if H(K) ≥ H(M)
and each key is used with equal probability.

---

## Information Has Physical Reality

Shannon's information theory connects to thermodynamics through work extractable from information.

**Szilard Engine** (1929):
- Maxwell's demon problem: demon measures molecule position → can sort hot/cold → violates 2nd law?
- Resolution: measuring (acquiring information) costs nothing; but ERASING the measurement (resetting demon's memory) costs energy.

**Landauer's Principle** (1961):
Erasing one bit of information requires dissipating at least:

$$\boxed{E_{min} = k_B T \ln 2 \approx 2.87 \times 10^{-21} \text{ J at 300K}}$$

```
    Physical interpretation:
    Information is NOT free. Every irreversible computation (erasure) costs energy.
    Reversible computation (Toffoli gate, etc.) can in principle be free.
    Modern CPU: ~10⁻¹⁸ J per bit operation (10³× above Landauer limit)
    → Enormous room for improvement toward physical limits

    The connection:
    Thermodynamic entropy S = k_B ln W (Boltzmann)
    Shannon entropy H = -Σ p log p (nats if ln; bits if log₂)
    S = k_B ln 2 × H (in bits)
    → Shannon entropy and thermodynamic entropy are the same quantity in different units
    → Erasing 1 bit: ΔS ≥ k_B ln 2 → ΔE = T·ΔS ≥ k_B T ln 2 ✓

    Maxwell's demon resolution (Brillouin 1956, Landauer 1961, Bennett 1982):
    Demon must erase its measurement record each cycle
    → Erasure of k_B T ln 2 entropy per bit → 2nd law preserved
    → Information IS entropy; there is no free thermodynamic lunch
```

---

## Connection to TCS (For Learner's Background)

### Kolmogorov Complexity

<!-- @editor[audience/P2]: Basic K(x) properties (upper bound, chain rule, uncomputability, Shannon ≥ H on average) are MIT TCS core curriculum — learner knows these. Compress to a one-line recall and pivot immediately to the MDL and circuit-complexity applications, which are the useful bridges here. -->

K(x) = length of shortest program that outputs x and halts.

```
    PROPERTIES:
    K(x) ≤ |x| + O(1) (can always just print x literally)
    K(x) ≤ K(x|y) + K(y) + O(log K(y)) (chain rule)
    K(x) uncomputable (via halting problem — decide if program halts outputting x)
    K(x) ≥ H(X) on average (for typical strings from source)
    K(x) and K(x|y) satisfy analog of chain rule

    MINIMUM DESCRIPTION LENGTH (MDL):
    Occam's razor formalized: best model = shortest program (theory + data)
    MDL model selection: choose model M that minimizes L(M) + L(data|M)
    where L = description length
    → Equivalent to Bayesian model selection (Rissanen 1978)

    CIRCUIT COMPLEXITY LOWER BOUNDS via entropy:
    If computing f(x) requires C gates, then H(f(x)) ≤ C (rough argument)
    → Information-theoretic arguments give lower bounds on circuit size
    → Razborov/Rudich natural proofs barrier: entropy arguments cannot give
      super-polynomial lower bounds against P/poly (under certain crypto assumptions)
```

### Communication Complexity

```
    Two players (Alice and Bob) have inputs x and y.
    Goal: compute f(x,y) by exchanging bits on a shared channel.
    Min bits exchanged = communication complexity CC(f).

    Lower bounds via entropy:
    CC(f) ≥ H(f(x,y)) - min(H(f(x,y)|x), H(f(x,y)|y))
    → Equality function f(x,y) = [x=y]: CC = Θ(n) by entropy argument

    Information complexity:
    IC_μ(f) = min protocol P: I(X;Π_{Alice}) + I(Y;Π_{Bob}) subject to μ,ε
    Π = transcript, μ = input distribution
    CC ≥ IC ≥ H(output)

    Amortized: CC_amortized(f^n) → IC(f) per copy (direct sum theorem)
```

---

## Modern Applications

```
    ┌─────────────────────────────────────────────────────────────┐
    │  APPLICATION MAP                                             │
    │                                                             │
    │  SOURCE CODING (compression):                               │
    │  ZIP/gzip: LZ77 + Huffman → 2-3:1 on text                  │
    │  brotli (Google): LZ + Huffman → web compression            │
    │  JPEG: DCT + quantization + Huffman → image 10:1            │
    │  H.264/HEVC/AV1: motion prediction + residual + entropy     │
    │  → 200:1 compression ratio on video                         │
    │                                                             │
    │  CHANNEL CODING (error correction):                         │
    │  HDD: Reed-Solomon, LDPC → read-after-write verification   │
    │  SSD (NAND flash): BCH, LDPC → handle flash cell errors     │
    │  WiFi (802.11n+): LDPC, BCC                                 │
    │  5G NR: LDPC (data), polar codes (control) — 2019 standard  │
    │  Deep space (Voyager, Cassini): convolutional + Reed-Solomon │
    │  Satellite (DVB-S2): LDPC + BCH                             │
    │                                                             │
    │  CRYPTOGRAPHY:                                              │
    │  OTP: provably perfect secrecy (keypad in WWII, Kremlin hotline) │
    │  Shamir secret sharing: IT-secure threshold sharing         │
    │  BB84 QKD: quantum key distribution (security from QM)      │
    │                                                             │
    │  MACHINE LEARNING:                                          │
    │  Cross-entropy loss ← H(p,q) = H(p) + KL(p||q)             │
    │  VAE ELBO ← variational inference (same as FEP!)            │
    │  Information bottleneck ← I(X;Z) vs I(Y;Z) tradeoff        │
    │  Perplexity = 2^{H} ← model quality measure                │
    │  LLM compression = arithmetic coding with LM probs          │
    └─────────────────────────────────────────────────────────────┘
```

---

## Decision Cheat Sheet — Which IT Tool for What?

| Problem                           | Tool                        | Formula/Result                  |
|-----------------------------------|----------------------------|---------------------------------|
| How much can I compress X?        | Entropy H(X)               | Min bits/symbol = H(X)          |
| What's redundancy in X?           | H(X) vs log|X|             | R = 1 - H(X)/log|X|             |
| How much info Y gives about X?    | Mutual information I(X;Y)  | I = H(X) + H(Y) - H(X,Y)        |
| How channel max rate?             | Channel capacity C          | C = max_{p(x)} I(X;Y) bits/use  |
| How similar are P and Q?          | KL divergence D(P||Q)      | ≥0, = 0 iff P=Q                |
| How to choose model?              | MDL = K(model) + K(data|model) | Shortest description wins    |
| Minimum energy to erase 1 bit?    | Landauer limit              | k_B T ln 2 ≈ 3×10⁻²¹ J          |
| Can I communicate at rate R?      | Shannon capacity C          | Yes iff R < C                   |
| How many secret bits from QKD?    | S(ρ) + eavesdropper error  | BB84 key rate formula           |

---

## Common Confusion Points

**Entropy doesn't measure "how much we don't know"**: H(X) measures the average number of
bits needed to specify a value of X under distribution p. A distribution you know perfectly
(say, a fair coin) has H = 1 bit. A distribution you're uncertain about (say, some unknown
coin) has the same H = 1 bit if you've correctly estimated it's fair. Entropy is a property
of the distribution, not of your beliefs about the distribution.

**Information is not the same as meaning**: Shannon's theory quantifies information in a
strictly syntactic sense — the bits needed to represent outcomes. It says nothing about
semantics (what the message MEANS) or pragmatics (how useful it is). "The dog barked" and
a random string of the same length might have similar entropy from an information theory
perspective but completely different semantic content.

**KL divergence is not a distance**: D_KL(P||Q) is not symmetric (D_KL(P||Q) ≠ D_KL(Q||P))
and doesn't satisfy the triangle inequality. It's not a metric in the mathematical sense.
The "distance" interpretation is intuitive but imprecise. When you minimize KL(p||q) in
machine learning, you get different behavior than minimizing KL(q||p) — choosing between
them is a design decision (mean-seeking vs mode-seeking behavior).

**The noisy channel theorem is existential, not constructive**: Shannon proved that good codes
exist (random codes work) but didn't say HOW to construct them or decode them efficiently.
The decades of work after Shannon were finding constructive, computationally efficient codes
that approach capacity: turbo codes (1993), LDPC (rediscovered 1999), polar codes (2009).
Polar codes are the first with both proof of capacity and O(n log n) encoding/decoding.
