# Source Coding — Data Compression

---

## Big Picture

```
SOURCE CODING THEOREM (Shannon 1948):
  Any lossless code for i.i.d. X ~ p(x) requires ≥ H(X) bits/symbol.
  Achievable with a code of expected length < H(X) + 1 bits/symbol.
  (The +1 goes to zero with block coding of n symbols: → H(X) exactly)

LOSSLESS COMPRESSION:
  Exploit statistical structure (redundancy) → shorter representation
  Limit: entropy rate H(X)

LOSSY COMPRESSION (rate-distortion):
  Allow controlled distortion → compress below H(X)
  Limit: R(D) = rate-distortion function

PRACTICAL GAP:
  Huffman: ≤ H(X)+1 (optimal for fixed-length symbols)
  Arithmetic: ≤ H(X)+2/n (near-optimal for blocks)
  LZ77/LZ78: H(X) asymptotically (universal, no model needed)
  Modern: zstd, brotli, LZMA — within 5% of optimal in practice
```

---

## Prefix Codes and Huffman Coding

### Prefix (Instantaneous) Codes

```
KRAFT INEQUALITY: For a uniquely decodable code with codeword lengths l₁,...,lₙ:
  Σᵢ D^{-lᵢ} ≤ 1   (D = alphabet size, usually D=2)

  Prefix code (no codeword is prefix of another) satisfies Kraft with equality.
  ANY uniquely decodable code can be replaced by prefix code of same lengths.

EXAMPLE (4 symbols):
  a: 0.5    → code: 0      (1 bit)    Huffman optimal
  b: 0.25   → code: 10     (2 bits)
  c: 0.125  → code: 110    (3 bits)
  d: 0.125  → code: 111    (3 bits)

  Expected length: 0.5×1 + 0.25×2 + 0.125×3 + 0.125×3 = 1.75 bits/symbol
  Entropy: H = -(0.5 log 0.5 + 0.25 log 0.25 + 2×0.125 log 0.125) = 1.75 bits
  → Exact match! (probabilities are powers of 2 → perfect Huffman code)
```

### Huffman Algorithm

```
ALGORITHM:
  1. Sort symbols by probability (ascending)
  2. Merge two lowest-probability symbols into combined node (p₁+p₂)
  3. Re-sort and repeat until one root node
  4. Assign 0/1 to branches at each merge

OPTIMALITY: Huffman code minimizes expected code length among all prefix codes.
  H(X) ≤ L(C_Huffman) < H(X) + 1

ADAPTIVE HUFFMAN: update tree as symbols arrive → no prior model needed
CANONICAL HUFFMAN: sort by length, then lexicographic → standard in DEFLATE

LIMITATIONS:
  - Per-symbol: fractional bits wasted (can't code 0.1 bit)
  - Static: requires known distribution
  - Not universal: different source needs different code
```

---

## Arithmetic Coding

```
IDEA: Map entire message to one number in [0,1)
  Assign each symbol a sub-interval proportional to its probability
  Each successive symbol narrows the interval

EXAMPLE (symbols A=0.7, B=0.3):
  Initial: [0, 1)
  After A: [0, 0.7)   (A occupies [0, 0.7))
  After B: [0.49, 0.7) (B occupies [70%, 100%) of current interval)
  After A: [0.49, 0.637) (A occupies [0%, 70%) of current interval)
  Output: any number in [0.49, 0.637), e.g. "0.5" → code: 0 1 (2 bits for 3 symbols)

CODE LENGTH: message of n symbols → interval width 2^{-nH(X)} → needs nH(X) bits
→ Achieves entropy exactly for block coding (unlike Huffman's +1)

PRACTICAL ISSUES:
  Precision: interval becomes tiny → use integer arithmetic with renormalization
  ANS (Asymmetric Numeral Systems, Duda 2009): faster than arithmetic coding
    → Used in: ZSTD, Apple LZFSE, Facebook ZSTD, brotli
    rANS (range ANS): near-arithmetic entropy with simpler decoding
```

---

## Universal Compression: Lempel-Ziv

No model needed — adapts to source statistics.

### LZ77 (1977)

```
ALGORITHM:
  Sliding window (search buffer + look-ahead buffer)
  For each position: find longest match in previous L bytes
  Encode: (offset, length, next_char)

EXAMPLE:
  Input:   "abracadabra"
  "abra" → (0, 0, 'a'), (0, 0, 'b'), (0, 0, 'r'), (0, 0, 'a')
  "cada" → (0, 0, 'c'), (3, 1, 'd'), ...
  "abra" → match at offset 7, length 4 → (7, 4, #) (reference earlier "abra")

USED IN: DEFLATE (ZIP, PNG, HTTP compression = gzip), LZSS, LZ4
```

### LZ78 / LZW (1978)

```
ALGORITHM: Build dictionary incrementally from parsed phrases

LZW (1984, Welch):
  Initialize dictionary with all single characters
  Read characters until string not in dict
  Output: index of longest match
  Add match+next_char to dictionary

USED IN: GIF (8-bit), TIFF, early modem compression (V.42bis)
PATENT (Unisys): caused GIF controversy 1994; expired 2003
```

### Optimality of LZ

```
THEOREM: LZ codes achieve the entropy rate of any stationary ergodic process.
  L_n(LZ) / n → H(X) as n → ∞

Convergence is slow (O(log n) terms) → large blocks needed for near-optimal
Modern compressors: combine LZ (structure) + Huffman/ANS (residuals)
  ZSTD: LZ77 + Huffman for literals + ANS for offsets/lengths
  LZMA (7z, xz): LZ77 + range coding → best ratio for cold storage
  brotli: LZ77 + Huffman + second-order context modeling → HTTP compression
```

---

## Rate-Distortion Theory

Lossy compression: accept distortion D, minimize bitrate R.

```
RATE-DISTORTION FUNCTION:
  R(D) = min_{p(x̂|x): E[d(X,X̂)]≤D} I(X;X̂)

  d(x,x̂) = distortion measure (e.g., squared error for AWGN)
  X̂ = reconstructed source

GAUSSIAN SOURCE with MSE distortion:
  X ~ N(0,σ²), d(x,x̂) = (x-x̂)²
  R(D) = ½ log(σ²/D)   for D ≤ σ²
  R(D) = 0             for D > σ²

  Inverse: D(R) = σ² × 2^{-2R}  (doubling bits → halving distortion)
  → 6 dB/bit improvement in SNR for Gaussian source

VECTOR GAUSSIAN (water-filling):
  Source X ~ N(0, K), K = covariance
  Decompose via SVD: K = Σ σᵢ² uᵢuᵢᵀ
  Water-fill: allocate bits to variance components
  λ = water level: Dᵢ = min(σᵢ², λ)
  R(D) = ½ Σᵢ max(0, log(σᵢ²/λ))
  → Allocate more bits to high-variance components
```

### Practical Lossy Codecs

```
IMAGE COMPRESSION:
  JPEG (DCT + quantization + Huffman/arithmetic):
    Divide into 8×8 blocks → DCT → quantize (perceptual weighting) → entropy code
    DCT concentrates energy in low frequencies → most high-freq coefficients ≈ 0
    Quality 90 → 10:1 compression with minimal artifact

  JPEG 2000 (wavelet + arithmetic):
    Discrete Wavelet Transform → progressive quality layers → lossless mode
    Better than JPEG at high compression, poor adoption

  HEIC/AVIF (H.265/AV1 intra): 2× better than JPEG at same quality

AUDIO:
  MP3 (MPEG-1 Layer III): psychoacoustic model + modified DCT + Huffman
  AAC: better than MP3 at same bitrate → default for iOS, YouTube
  Opus: modern, covers speech + music → WebRTC

VIDEO:
  H.264/AVC (2003): inter-frame prediction + DCT + CABAC → HDTV
  H.265/HEVC (2013): 2× H.264 at same quality → 4K streaming
  AV1 (2018, open source): competitive with H.265, royalty-free → YouTube, Netflix
  Prediction modes: intra (spatial), inter (temporal motion compensation)
  Reference frames: B-frames can reference future → non-causal → 3× efficiency
```

---

## Kolmogorov Complexity

Algorithmic information theory — a different view of "information content."

```
DEFINITION: K(x) = min length of program p such that U(p) = x
  U = universal Turing machine (fixed, reference machine)
  K(x) = length of shortest description of x

INCOMPRESSIBILITY:
  Most strings of length n have K(x) ≥ n - O(1)
  (Most strings are incompressible = random)
  |{x : K(x) < n}| < 2ⁿ (by counting argument)

PROPERTIES:
  K(x) ≤ |x| + O(1)   (can always just copy x)
  K(xy) ≤ K(x) + K(y|x) + O(log n)
  K(x) is UNCOMPUTABLE: reduces to halting problem
  K(x|y): conditional KC (length of shortest program for x given y)

RANDOM STRINGS:
  x is (algorithmically) random if K(x) ≥ |x| - O(1)
  "No regularities" → cannot compress

RELATION TO SHANNON:
  H(X) = E[K(X)] ± O(log n)  (up to log terms, Kolmogorov ≈ Shannon expectation)
  Shannon: worst-case over ensemble; Kolmogorov: individual string

MINIMUM DESCRIPTION LENGTH (MDL):
  Best model = shortest total description: |model| + |data|model|
  MDL ≈ BIC (Bayesian Information Criterion) with slight differences
  Model selection via MDL = find model that compresses data most
```

---

## Decision Cheat Sheet

| Method | Rate | Pros | Cons | Use case |
|--------|------|------|------|---------|
| Huffman | H(X) + [0,1) | Simple, fast | +1 bit overhead, static | Images (JPEG residuals) |
| Arithmetic | H(X) + ε | Near-optimal | Complex, patent history | HEVC CABAC |
| ANS/rANS | H(X) | Fast, near-optimal | Newer | zstd, brotli |
| LZ77 | H(X) asympt. | Universal, no model | Slow convergence | DEFLATE, ZIP |
| LZMA | Best ratio | Near-optimal | Slow | 7z, xz, git objects |
| brotli | Good ratio | HTTP, precomputed dict | Slow compress | HTTP/2, WOFF2 |
| zstd | Good ratio + speed | Tunable | — | Facebook, Linux kernel |
