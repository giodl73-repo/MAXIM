# Session 17 — Information Theory

**Date:** 2026-02-22
**Track:** Engineering Sciences — Mathematics Foundations

---

## What This Session Covers

Information theory is the mathematical theory of communication and compression. Shannon (1948) asked: what is the fundamental limit of how much information a channel can carry? How much can data be compressed? The answers — channel capacity and source entropy — are among the deepest results in applied mathematics, and they underpin modern communications, cryptography, machine learning, and quantum computing.

---

## Module Index

| File | Topic | Status |
|------|-------|--------|
| `information-theory/00-OVERVIEW.md` | Field map, Shannon's framework, historical arc, why it matters | ✅ |
| `information-theory/01-ENTROPY-INFORMATION.md` | Shannon entropy, mutual information, KL divergence, information inequalities | ✅ |
| `information-theory/02-SOURCE-CODING.md` | Huffman, arithmetic/ANS coding, LZ universal compression, rate-distortion, Kolmogorov complexity | ✅ |
| `information-theory/03-CHANNEL-CODING.md` | Channel capacity, BSC/BEC/AWGN, Hamming, Reed-Solomon, LDPC, Turbo, Polar codes | ✅ |
| `information-theory/04-ML-CRYPTOGRAPHY-BRIDGE.md` | Cross-entropy = MLE, VAE ELBO, IB principle, MDL, perfect secrecy, AES confusion+diffusion, quantum information, BB84 | ✅ |

---

## Learning Arc

```
Entropy H(X) — fundamental measure of uncertainty (01)
  │
  ├─→ Source coding: compress to H(X) bits — Huffman, LZ, arithmetic (02)
  │
  ├─→ Channel coding: communicate at rate C = max I(X;Y) (03)
  │
  └─→ Applications: ML loss functions, cryptographic security, quantum info (04)
```

---

## Key Mental Models

**Entropy = irreducible randomness = minimum bits to describe.** H(X) is simultaneously: the average surprise, the minimum average code length, the minimum bits for a perfect compressor.

**Mutual information = shared information = how much Y tells you about X.** I(X;Y) = H(X) - H(X|Y). It's zero for independent variables, H(X) for deterministic functions. The data processing inequality says no computation can increase it.

**Channel capacity = maximum information flow rate.** C = max I(X;Y) over input distributions. Shannon proved you can communicate at any rate below C with arbitrarily low error — and above C, error is unavoidable. Coding theory spent 70 years finding practical codes that approach this limit.

**Cross-entropy loss = KL divergence from true distribution.** Training a neural network with cross-entropy is exactly minimizing KL(p_data || q_θ), which is maximum likelihood estimation, which is finding the model that compresses the training data most. Information theory and ML are the same thing, expressed differently.

---

## MIT / Math Connections

- **Convexity:** Jensen's inequality underlies all information inequalities (KL ≥ 0, H ≤ log|X|)
- **Linear algebra:** Mutual information I(X;Y) = KL divergence in the space of joint distributions
- **Probability theory:** Entropy rate = limit of conditional entropy = ergodic theorem analog
- **Abstract algebra / finite fields:** Reed-Solomon codes require GF(2^8); polar codes use GF(2)
- **Algorithmic theory:** Kolmogorov complexity connects to computability theory (K(x) uncomputable)
- **Quantum mechanics:** von Neumann entropy S(ρ) = -Tr(ρ log ρ) generalizes Shannon entropy

---

## Bridges to Software / Systems

| IT concept | Systems application |
|------------|-------------------|
| Huffman coding | DEFLATE (ZIP, PNG, HTTP gzip), JPEG residual coding |
| ANS (asymmetric numeral systems) | zstd, brotli, Apple LZFSE — modern system compression |
| LZ77 | ZIP, gzip, LZ4 (fast), LZMA (maximum ratio) |
| Arithmetic coding | HEVC/H.265 CABAC, JPEG 2000 |
| Reed-Solomon | CD/DVD error correction, QR codes, RAID-6, RAID storage |
| LDPC codes | WiFi 802.11n/ac/ax, 5G NR data channels |
| Polar codes | 5G NR control channels (PBCH, PDCCH) |
| Entropy sources | /dev/urandom, TPM, hardware QRNG — crypto key generation |
| Cross-entropy loss | All classification neural networks, language model training |
| ELBO / KL | VAE, DDPM (diffusion models), flow matching, VI in probabilistic ML |
| Shannon secrecy | OTP (perfect secrecy), AES (computational secrecy), TLS |
| BB84 QKD | Commercial quantum key distribution (ID Quantique, Toshiba) |
