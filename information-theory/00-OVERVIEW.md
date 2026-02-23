# Information Theory — Overview

---

## Big Picture

```
SHANNON (1948): A Mathematical Theory of Communication

FUNDAMENTAL QUESTION: How much can you compress? How fast can you transmit?
  │
  ├── SOURCE CODING (compression)
  │     "Represent messages using as few bits as possible"
  │     Limit: H(X) bits/symbol (Shannon entropy)
  │
  ├── CHANNEL CODING (reliability)
  │     "Transmit through noisy channel with arbitrarily low error"
  │     Limit: C bits/use (channel capacity)
  │
  └── RATE-DISTORTION (lossy compression)
        "Trade off fidelity for compression"
        R(D): minimum rate for maximum distortion D

KEY INSIGHT: These limits are achievable in principle.
The gap between theory and practice = coding theory (algebraic + probabilistic).
```

```
INFORMATION THEORY MAP:

        Source                       Channel                     Sink
    (random process)            (noisy medium)              (receiver)

  X ~ p(x) ──→ ENCODER ──→ Y  ~ p(y|x) ──→ DECODER ──→ X̂

  Source entropy:  H(X)          Capacity: C = max_{p(x)} I(X;Y)
  Compressed bits: ≥ H(X)        Error rate: → 0 if rate < C
```

---

## Why an MIT Math/TCS Person Cares

Information theory is the foundation of:

1. **Cryptography:** One-time pad is provably perfect (Shannon 1949). Perfect secrecy requires H(key) ≥ H(message). AES security analyzed via information-theoretic arguments.

2. **Statistical learning theory:** PAC learning, VC dimension, MDL (Minimum Description Length). Information-theoretic bounds on generalization.

3. **Machine learning:** Cross-entropy loss IS the optimal coding length. KL divergence IS regret of using wrong model. Mutual information IS feature relevance. VAE objective IS rate-distortion.

4. **Compression:** ZIP, JPEG, MP3, H.264 — all exploiting information-theoretic limits.

5. **Quantum information:** Quantum entropy, quantum channel capacity, quantum error correction (CSS codes). Quantum advantage in information tasks.

6. **Neuroscience:** Efficient coding hypothesis (Barlow): neural representations compress sensory information. Neural channel capacity measurements.

---

## Field Map

```
INFORMATION THEORY
│
├── Classical (Shannon)
│     Entropy, mutual information, channel capacity
│     Data compression: Huffman, arithmetic, Lempel-Ziv
│     Channel coding: Hamming, turbo codes, LDPC, polar codes
│
├── Rate-Distortion Theory
│     Lossy compression with distortion measure
│     Blahut-Arimoto algorithm, Gaussian RD
│
├── Multi-User / Network
│     Multiple access channel, broadcast channel
│     Network coding, Slepian-Wolf (distributed compression)
│
├── Algorithmic Information Theory (Kolmogorov)
│     Kolmogorov complexity K(x): shortest program producing x
│     Incompressibility, randomness, Solomonoff induction
│
└── Quantum Information Theory
      von Neumann entropy, quantum channel capacity
      Holevo bound, quantum error correction
```

---

## Module Map

| File | Topic |
|------|-------|
| `01-ENTROPY-INFORMATION.md` | Shannon entropy, mutual information, KL divergence, information inequalities |
| `02-SOURCE-CODING.md` | Data compression — Huffman, arithmetic, LZ, rate-distortion, Kolmogorov |
| `03-CHANNEL-CODING.md` | Channel capacity, noisy channel theorem, error-correcting codes |
| `04-ML-CRYPTOGRAPHY-BRIDGE.md` | Cross-entropy loss, VAE, MDL, feature selection, cryptography, quantum information |

---

## Historical Arc

```
1948: Shannon — "A Mathematical Theory of Communication" (Bell Labs)
      Defined entropy, mutual information, channel capacity, source/channel coding theorems
      → Arguably the most important engineering paper of the 20th century

1950: Shannon — "Programming a Computer for Playing Chess"
1949: Shannon — "Communication Theory of Secrecy Systems" (perfect secrecy, OTP)
1950s: Hamming codes (1950), Reed-Solomon codes (1960)
1962: Gallager — LDPC codes (rediscovered 1990s → turbo era)
1993: Turbo codes (Berrou et al.) — near-Shannon performance
1995: Shor code — first quantum error-correcting code
1996: LDPC codes rediscovered (Berrou, then MacKay & Neal)
2008: Polar codes (Arıkan) — provably capacity-achieving with efficient encoding/decoding
2016: Polar codes selected for 5G NR control channels
2020s: Neural network-based compression (LLM as universal compressor?)
```
