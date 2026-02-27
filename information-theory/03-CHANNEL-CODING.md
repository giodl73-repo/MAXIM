# Channel Coding — Capacity and Error-Correcting Codes

---

## Big Picture

```
CODE FAMILY TAXONOMY — STRUCTURE AND TRADEOFFS
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  BY STRUCTURE:         BY DESIGN PHILOSOPHY:      BY BLOCK LENGTH:      │
│  ┌────────────────┐    ┌─────────────────────┐    ┌───────────────────┐│
│  │ BLOCK CODES    │    │ ALGEBRAIC            │    │ SHORT (n<256)     ││
│  │ (n,k,d) fixed  │    │ Hamming, BCH, RS,   │    │ Hamming, BCH      ││
│  │ rate = k/n     │    │ Golay — exact math   │    │ Strong guarantees ││
│  ├────────────────┤    ├─────────────────────┤    ├───────────────────┤│
│  │ CONVOLUTIONAL  │    │ PROBABILISTIC        │    │ MEDIUM (256-10K)  ││
│  │ sliding window │    │ Turbo, LDPC, Polar   │    │ LDPC, Polar       ││
│  │ (n,k,K) memory │    │ — random-like graphs │    │ Near-Shannon      ││
│  ├────────────────┤    │   + iterative decode │    ├───────────────────┤│
│  │ RATELESS       │    └─────────────────────┘    │ LONG (10K+)       ││
│  │ Fountain/LT/   │                               │ LDPC, Turbo       ││
│  │ Raptor         │    Rate vs complexity:         │ Capacity-approach ││
│  └────────────────┘    Algebraic: O(n log n) dec   └───────────────────┘│
│                        Iterative: O(n) per iter                         │
│                        Polar: O(n log n) exact                          │
└─────────────────────────────────────────────────────────────────────────┘
```

```
NOISY CHANNEL CODING THEOREM (Shannon, 1948):
  For any channel with capacity C bits/use:
  • If R < C: ∃ a code such that P_e → 0 as block length n → ∞
  • If R > C: P_e → 1 for all codes (unavoidable error)

  C = max_{p(x)} I(X;Y)

IMPLICATIONS:
  • Can communicate reliably at ANY rate below capacity — but not above
  • The theorem is EXISTENCE — doesn't say HOW to construct the code
  • 70 years of coding theory = constructing codes that approach C efficiently

PRACTICAL CODES vs SHANNON LIMIT:
  1950: Hamming codes — first error-correcting, far from capacity
  1960: Reed-Solomon — algebraic, excellent burst error correction (CDs, QR codes)
  1993: Turbo codes — within 0.5 dB of Shannon limit (3GPP LTE data)
  1997: LDPC rediscovered — within 0.01 dB (5G NR data channels)
  2009: Polar codes — provably capacity-achieving, O(n log n) complexity (5G NR control)
```

---

## Channel Capacity

### Binary Symmetric Channel (BSC)

```
CHANNEL: bit flips with probability p (independently)
  p(y=0|x=0) = 1-p, p(y=1|x=0) = p
  p(y=0|x=1) = p, p(y=1|x=1) = 1-p

CAPACITY:
  C_BSC = 1 - h(p)  [bits/channel use]
  h(p) = binary entropy = -p log₂p - (1-p)log₂(1-p)

  p=0 (perfect): C=1 bit
  p=0.1: C = 1 - h(0.1) = 1 - 0.469 = 0.531 bits
  p=0.5 (useless): C = 0 bits

Achieved by uniform input distribution: p(x=0) = p(x=1) = 1/2
```

### Binary Erasure Channel (BEC)

```
CHANNEL: each bit erased (lost) with probability ε, received correctly otherwise
  y ∈ {0, ?, 1}  (? = erased)

CAPACITY: C_BEC = 1 - ε  [bits/channel use]
  → Fraction of bits that are not erased

Internet/wireless: erasures from packet loss; BEC models the unreliable path
```

### AWGN Channel (Gaussian)

The continuous, power-constrained channel. Models wireless and wired:

```
y = x + z,   z ~ N(0, N₀/2)  per dimension (or N₀W noise power in bandwidth W)

CAPACITY (Shannon-Hartley):
  C = W log₂(1 + SNR)   [bits/second]
  SNR = P/(N₀W)

  W = bandwidth (Hz)
  P = signal power (W)
  N₀/2 = noise PSD (W/Hz)

EXAMPLES:
  Telephone: W=3400 Hz, SNR=30 dB (1000×) → C = 3400 × log₂(1001) ≈ 34 kbps
  WiFi 802.11ac: W=160 MHz, SNR=40 dB → C ≈ 160M × 13.3 = 2.1 Gbps
  5G mmWave: W=400 MHz, short range high SNR → multi-Gbps

BANDWIDTH vs POWER:
  C ↑ linearly with W (at fixed SNR): doubling bandwidth doubles capacity
  C ↑ logarithmically with SNR: doubling power adds only log₂ bits → poor return
  → In bandwidth-limited regime: add antennas (MIMO)
  → In SNR-limited regime: add bandwidth

WIDEBAND LIMIT (P/N₀ fixed, W→∞):
  C → (P/N₀) / ln(2)  (capacity bounded even with infinite bandwidth)
```

---

## Error-Correcting Codes

### Basics

```
BLOCK CODE [n, k, d]:
  n = block length (transmitted bits)
  k = message bits
  d = minimum Hamming distance between codewords
  Rate R = k/n
  Error correction capability: t = ⌊(d-1)/2⌋ errors correctable
  Error detection: d-1 errors detectable

SPHERE PACKING BOUND (Hamming bound):
  Σ_{i=0}^t C(n,i) ≤ 2^{n-k}   (volume of t-error spheres ≤ code space)
  Perfect code: achieves equality (Hamming codes, Golay code)

SINGLETON BOUND:
  d ≤ n - k + 1
  Code achieving equality: Maximum Distance Separable (MDS) code
  Reed-Solomon codes are MDS!

GILBERT-VARSHAMOV BOUND:
  ∃ code with d ≥ δn and R ≥ 1 - h(δ)   (probabilistic existence argument)
  Random codes achieve this — hard to decode efficiently
```

### Hamming Codes

```
[7,4,3] Hamming code: n=7, k=4, d=3 → t=1 (corrects single errors)

PARITY CHECK MATRIX H (7×3):
  H = [   p₁  p₂  p₃  p₄  p₅  p₆  p₇  ]
      [ bit 1 in col = position in binary ]

  H = [0 0 0 1 1 1 1]
      [0 1 1 0 0 1 1]
      [1 0 1 0 1 0 1]

SYNDROME: s = Hc^T
  If s=0: no error
  If s≠0: s = binary representation of error position → flip that bit

PERFECT CODE: exactly 2^{n-k} = 8 syndromes, one per error pattern (including no error)

EXTENDED HAMMING [8,4,4]: add overall parity check → d=4 → detect 2 errors, correct 1
```

### Reed-Solomon Codes

```
RS(n,k) over GF(q):   q = prime power (usually q = 2^8 for bytes)
  n = q-1 symbols
  k = message symbols
  d = n-k+1 (MDS: achieve Singleton bound!)

  ENCODING: Treat message as polynomial m(x) = m₀ + m₁x + ... + m_{k-1}x^{k-1}
            Codeword: systematic + parity symbols = (m(x) × x^{n-k}) mod g(x)
            g(x) = (x-α)(x-α²)...(x-α^{n-k})  where α = primitive element of GF(2^8)

CORRECTION: Can correct up to t = (n-k)/2 symbol errors  (Berlekamp-Massey decoder)

APPLICATIONS:
  CD-ROM: RS(255,251) → corrects 2 symbol errors; with interleaving: corrects burst errors
  DVD: RS + convolutional interleaving
  QR codes: RS over GF(256) with variable redundancy
  RAID 6: RS(n,n-2) over GF(2^8) → tolerates any 2 disk failures

BURST ERRORS: RS excellent because one symbol error = one Galois field element
  regardless of how many bit errors in that byte
```

### LDPC Codes

```
Low-Density Parity-Check codes (Gallager 1962; MacKay & Neal 1996-1997).

PARITY CHECK MATRIX H: very sparse (few 1s per row/column)
  Tanner graph: bipartite graph of variable nodes + check nodes
  Variable node i: corresponds to codeword bit cᵢ
  Check node j: enforces parity constraint Σ_{i ∈ N(j)} cᵢ = 0 (mod 2)

BELIEF PROPAGATION (Sum-Product):
  Iterative message passing on Tanner graph
  Variable → check: send belief about own bit
  Check → variable: send constraint satisfaction probability
  Converges in ~50 iterations for well-designed codes

THRESHOLD PHENOMENON: Below a capacity threshold, BP decodes with P_e → 0
  LDPC can get within 0.01-0.05 dB of Shannon limit!

APPLICATIONS:
  WiFi 802.11n/ac/ax (5G NR data channels), DVB-S2 (satellite TV)
  WiMAX, 10GBase-T Ethernet
```

### Turbo Codes

```
Berrou, Glavieux, Thitimajshima (1993): "Near Shannon limit error-correcting coding"

ARCHITECTURE:
  Message u
    ├─→ Encoder 1 (RSC) → parity p₁
    └─→ Interleaver π → Encoder 2 (RSC) → parity p₂

  Transmit: (u, p₁, p₂) → rate 1/3 (or puncture some parity for higher rate)
  Interleaver: permute bits to spread burst errors, make encoders see different patterns

DECODING (BCJR/MAP decoder):
  Iterative turbo decoding: two SISO (soft-in soft-out) decoders exchange extrinsic info
  8-16 iterations → near-Shannon performance

APPLICATIONS: 3G (UMTS/WCDMA), LTE data channels, deep-space (Cassini)
```

### Polar Codes

```
Arıkan (2009): First provably capacity-achieving code with O(n log n) encode/decode.

KEY IDEA: "Channel polarization"
  Combine n=2^m uses of a noisy channel W
  Apply recursive butterfly transform (like FFT butterfly)
  After n steps: ≈ nC "perfect" synthetic channels + n(1-C) "useless" channels
  → "Frozen" bits: set to 0 on useless channels (known to both sides)
  → Information bits: sent on perfect channels

  As n→∞: fraction C channels become perfect, fraction 1-C become useless
  → Rate = C → capacity-achieving!

DECODING: Successive cancellation (SC): O(n log n)
  Improved: SC-List (SCL): nearly as good as ML

APPLICATIONS: 5G NR control channels (PBCH, PDCCH) — chosen over LDPC
             Due to low complexity, provable optimality, short blocklength performance
```

---

## Modern Applications

### RAID Erasure Coding

```
RAID 5 (single parity): XOR of k disks → tolerates 1 failure
RAID 6 (double parity): RS(k+2,k) → tolerates 2 failures
Erasure codes for storage (Ceph, HDFS EC, Azure, Facebook f4):
  RS(14,10): store 1.4× data; tolerate 4 simultaneous failures
  Facebook f4: warm storage → RS + XOR code for 2× fault tolerance

REGENERATING CODES: minimize repair bandwidth (not just fault tolerance)
  MSR (minimum storage regenerating): only download fraction of data to repair
  → Important for large distributed storage (HDFS, S3 background)
```

### Network Coding

```
CLASSIC ROUTING: each node just forwards packets
NETWORK CODING: intermediate nodes can XOR/combine packets

BUTTERFLY NETWORK EXAMPLE:
  Source sends A and B over a network with bottleneck link
  Without coding: can't send both A and B over bottleneck
  With coding: send A⊕B over bottleneck → receivers decode A and B separately
  → Achieves multicast capacity (Ahlswede et al. 2000)

RANDOM LINEAR NETWORK CODING (RLNC):
  Each node sends random GF(q) linear combinations of received packets
  Receiver collects enough linearly independent combinations → decode (Gaussian elim)
  Distributed, no central coordination
  BitTorrent-like: peers spread random combinations → eventual decoding
```

---

## Decision Cheat Sheet

| Code family | Rate vs capacity | Encode | Decode | Use case |
|-------------|-----------------|--------|--------|---------|
| Hamming [7,4,3] | Far (t=1) | O(n) | O(n) | DRAM ECC, simple logic |
| Reed-Solomon | MDS (optimal d) | O(n log n) | O(n²) or O(n log n) | CDs, QR codes, RAID6 |
| LDPC | Near-Shannon | O(n) | O(n) iter. | WiFi, 5G data, satellite |
| Turbo | Near-Shannon | O(n) | O(n) iter. | LTE, 3G, deep-space |
| Polar | Shannon-achieving | O(n log n) | O(n log n) | 5G NR control channels |
| Fountain (LT, Raptor) | Rate-less, ≈ 1 | O(n log n) | O(n log n) | File broadcast, MBMS |

---

## Common Confusion Points

**Capacity is in bits per channel use, not bits per second.** Shannon's C = max I(X;Y) is bits/use. To get bits/second, multiply by uses/second. The Shannon-Hartley formula C = B log₂(1 + SNR) already incorporates bandwidth B, giving bits/second directly — but that's the AWGN continuous-channel result, not the general DMC formula.

**Shannon capacity is for DMC; AWGN uses the continuous formula.** The discrete memoryless channel (DMC) has C = max_{p(x)} I(X;Y) over a finite alphabet. The AWGN channel uses C = ½ log(1 + P/N₀W) with continuous inputs. These are different theorems for different channel models.

**LDPC threshold is sharp.** Below the threshold noise level, LDPC error probability drops to zero with block length (like a phase transition). Above threshold, performance degrades rapidly. This is the "waterfall" curve — the transition from P_e ≈ 1 to P_e ≈ 0 is abrupt, not gradual.

**Polar codes are capacity-achieving asymptotically, not at finite length.** Arikan's 2009 result proves polar codes achieve capacity as n → ∞ with O(n log n) encoding/decoding. At practical block lengths (n = 256–2048), polar codes with CRC-aided list decoding are competitive but not dominant — LDPC often outperforms at medium blocks.

**Sphere-packing bound and random coding exponent address different questions.** Sphere-packing (Hamming) gives a hard upper bound on rate for given distance. The random coding exponent gives the error exponent (how fast P_e → 0) at rates below capacity. Both are fundamental but measure different things.
