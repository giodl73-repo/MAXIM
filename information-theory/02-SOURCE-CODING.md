# Source Coding — Data Compression Theory

## The Big Picture

```
    SOURCE CODING LANDSCAPE
    ══════════════════════════════════════════════════════════

    LOSSLESS COMPRESSION:              LOSSY COMPRESSION:
    ┌────────────────────┐            ┌──────────────────────────┐
    │ Kraft inequality   │            │ Rate-distortion theory   │
    │ Shannon source thm │            │ R(D): min rate for D     │
    │ Huffman coding     │            │ Gaussian: ½log(σ²/D)     │
    │ Arithmetic coding  │            │ JPEG: DCT + quantization │
    │ LZ77/78, LZW       │            │ H.264: motion + residual │
    │ Universal coding   │            │ Kolmogorov: theoretical  │
    └────────────────────┘            └──────────────────────────┘

    FUNDAMENTAL LIMIT: H(X) bits/symbol (lossless)
                       R(D) bits/symbol (lossy, distortion D)
```

---

## Kraft Inequality

For a uniquely decodable (UD) code with D-ary alphabet and codeword lengths l_1,...,l_n:

$$\sum_{i=1}^n D^{-l_i} \leq 1$$

**McMillan's Theorem**: Every UD code satisfies the Kraft inequality.
(Converse: for any lengths satisfying Kraft, a prefix-free code exists with those lengths.)

WLOG: we can restrict attention to prefix-free codes without loss of optimality.

```
    Kraft inequality intuition (binary D=2):
    Binary tree of depth max(l_i): each codeword "claims" a subtree.
    No claimed subtree is prefix of another (prefix-free).
    Total "fraction of tree" claimed = Σ 2^{-l_i} ≤ 1.
    Tight (= 1) iff every leaf is assigned → complete tree.

    Example: binary code for {A,B,C,D}
    lengths [1,2,3,3]: Σ 2^{-l_i} = 0.5+0.25+0.125+0.125 = 1.0 (complete)
    Valid prefix-free: A=0, B=10, C=110, D=111 ✓

    Check: invalid code [1,1,2,3] would need Σ = 0.5+0.5+0.25+0.125 = 1.375 > 1 → impossible
```

### Optimal Code Lengths

The minimum average code length L* = Σ p_i l_i satisfies:

$$H(X) \leq L^* < H(X) + 1$$

The optimal lengths are: l_i* = ⌈-log_D p_i⌉

```
    Proof of lower bound:
    For any valid code: L = Σ p_i l_i ≥ Σ p_i(-log p_i) = H(X)
    (by Gibbs inequality / log-sum)

    Proof of upper bound:
    Let l_i = ⌈-log D p_i⌉, so l_i < -log p_i + 1
    L = Σ p_i l_i < Σ p_i(-log p_i + 1) = H(X) + 1

    To get below H(X) + 1: use block coding on n symbols:
    Encode n symbols jointly → L/n < H(X^n)/n + 1/n = H(X) + 1/n → H(X) as n → ∞
    But still bounded by H(X) from below.
```

---

## Shannon Source Coding Theorem (1948)

**Formal statement**:
For an i.i.d. source with entropy H(X):
- For any R > H(X) and ε > 0: there exists a code operating at rate R bits/symbol with
  probability of error → 0 as block length n → ∞.
- For any R < H(X): any code operating at rate R has probability of error → 1.

**Proof sketch via Typical Sequences (AEP)**:

```
    AEP (Asymptotic Equipartition Property):
    For i.i.d. X₁,...,Xₙ ~ p(x):
    -(1/n) log p(X₁,...,Xₙ) → H(X) in probability

    ε-Typical Set T_ε^n: sequences where |-(1/n)log p(x^n) - H(X)| ≤ ε
    Properties:
    1. P(T_ε^n) → 1 as n → ∞ (AEP)
    2. |T_ε^n| ≤ 2^{n(H(X)+ε)} (not too many typical sequences)
    3. |T_ε^n| ≥ (1-δ)2^{n(H(X)-ε)} for large n (at least this many)

    Achievability proof:
    Assign distinct n(H(X)+ε)-bit codewords to all sequences in T_ε^n.
    Non-typical sequences: signal failure (P_error → 0 since P(T_ε^n) → 1).
    Rate = (H(X)+ε) bits/symbol.

    Converse (≥ H(X) needed):
    Using Fano's inequality: H(X^n|X̂^n) ≤ h(P_error) + n P_error log |X|
    If rate < H(X), then P_error bounded away from 0.
```

---

## Huffman Coding

Optimal prefix-free code for a known distribution.

**Algorithm** (David Huffman, 1952):
1. Sort symbols by probability: p₁ ≥ p₂ ≥ ... ≥ pₙ
2. Take two lowest-probability symbols, merge into new symbol with probability = sum
3. Repeat until one symbol remains
4. Assign 0/1 to each branch while going back

```
    Example: X = {A=0.4, B=0.3, C=0.2, D=0.1}

    Step 1: Merge D(0.1) + C(0.2) → CD(0.3)
    Step 2: Merge CD(0.3) + B(0.3) → BCD(0.6)
    Step 3: Merge BCD(0.6) + A(0.4) → ABCD(1.0)

    Tree:
         ABCD
        /    \
       A(0)  BCD(1)
            /    \
          B(0)   CD(1)
               /    \
             C(0)   D(1)

    Codewords: A=0, B=10, C=110, D=111

    Average length L = 0.4×1 + 0.3×2 + 0.2×3 + 0.1×3
                     = 0.4 + 0.6 + 0.6 + 0.3 = 1.9 bits/symbol

    H(X) = -0.4 log 0.4 - 0.3 log 0.3 - 0.2 log 0.2 - 0.1 log 0.1
         = 0.529 + 0.521 + 0.464 + 0.332 = 1.846 bits/symbol

    Redundancy: L - H = 1.9 - 1.846 = 0.054 bits/symbol (2.9% overhead)

    OPTIMALITY of Huffman:
    Huffman minimizes E[l_i] among all prefix-free codes for this distribution.
    Proof by exchange argument: any deviation can be shown to increase E[l_i].

    EXTENDED HUFFMAN: encode n symbols jointly → approach H(X) within 1/n bits
    ADAPTIVE HUFFMAN: update tree as symbols arrive (no prior knowledge of distribution)
```

---

## Arithmetic Coding

Achieves H(X) asymptotically (vs Huffman: H(X) + ε for arbitrary ε but only with large blocks).

**Core idea**: represent entire message as a single fraction in [0,1).

```
    Encoding: source sequence x₁ x₂ ... xₙ → interval [L, H) ⊂ [0,1)

    Initialize: L = 0, H = 1 (entire unit interval)
    For each symbol x_i with cumulative distribution F(x):
      Width = H - L
      New L = L + Width × F(x_i - 1)  [F(-∞) = 0 by convention]
      New H = L + Width × F(x_i)

    Final interval has width = ∏ p(x_i) = p(x₁,...,xₙ) = 2^{-n × (1/n)log(1/p)}
    → encode using -log₂(width) bits to identify interval
    → arithmetic coding achieves H(X) exactly (n → ∞, or using integer tricks)

    Example: binary source P(0)=0.8, P(1)=0.2. Encode "001"
    Symbol 0: L=0, H=0.8 (cumulative: P(0)=0.8)
    Symbol 0: L=0, H=0.64 (within [0,0.8), new interval is [0, 0.64))
    Symbol 1: interval [0.64×0.8, 0.64×1.0) = [0.512, 0.64)
    Output: any number in [0.512, 0.64), e.g. 0.6 requires ~1 bit to specify

    Length: -log₂(0.64-0.512) = -log₂(0.128) = 2.97 bits for 3 symbols
    H("001") = H(0)×2 + H(1)×1 = 2×0.322 + 0.699 = 1.343 bits
    Rate: 2.97/3 = 0.99 bits/symbol vs H(X) = 2×0.8×(-log0.8)/3+... ≈ 0.72 bits/symbol
    (example doesn't reach H because we need prefix-free termination; asymptotically ok)
```

**LLM connection**: Language models assign p(next_token | context). Arithmetic coding
with a language model as the source is EXACTLY this coding algorithm.
GPT-4-class models achieve ~4 bits/token on text → 2× compression vs raw UTF-8 (~8 bits/token).

---

## LZ77 and Universal Compression

**Lempel-Ziv 1977 (LZ77)**: sliding window compression (basis for ZIP, gzip, deflate).

```
    ENCODING:
    Sliding window: look-back buffer (32KB in gzip) + lookahead buffer
    For each position in lookahead:
      Find longest match in look-back window (position, length, next char)
      Encode as (offset, length, literal)
    If no match: (0, 0, literal character)

    Example: "ABRACADABRA"
    First occurrence: literals A,B,R,A,C,A,D (no look-back to find)
    "ABRA": match in look-back at offset 7, length 4
    → (7, 4) = reference back 7 characters, copy 4

    DECODING: reconstruct from (offset, length, literal) triples
    Self-referential copies possible (RLE-like: offset 1, length 100 → 100 copies of previous char)

    LZ78 (1978): dictionary-based, no sliding window
    LZW: derivative of LZ78, used in GIF (controversial patent history)

    ASYMPTOTIC OPTIMALITY (Ziv-Lempel theorem):
    LZ77/78 is asymptotically optimal for any stationary ergodic source
    Without knowing the source statistics a priori → UNIVERSAL compressor
    Rate → H(X) as n → ∞

    Proof idea: with high probability, LZ phrases in typical string of length n
    cover the string, and average phrase length → log n × 1/H(X) → each phrase
    uses ~log n bits → total ≈ n H(X) bits.
```

---

## Shannon Source Coding Theorem for Rate-Distortion (Lossy)

For lossy compression, allow some distortion d(x, x̂) between original x and reconstruction x̂.

**Rate-distortion function**:
$$R(D) = \min_{p(\hat{x}|x): \mathbb{E}[d(X,\hat{X})] \leq D} I(X;\hat{X})$$

```
    Achievability: for any R > R(D), there exists a code that reproduces X with
    expected distortion ≤ D using R bits/symbol.
    Converse: any code with expected distortion ≤ D must use ≥ R(D) bits/symbol.

    GAUSSIAN SOURCE, MSE DISTORTION:
    X ~ N(0,σ²), d(x,x̂) = (x-x̂)²
    R(D) = ½ log₂(σ²/D) for D ≤ σ²  (zero otherwise)
    → Each halving of distortion costs ½ bit/symbol

    BERNOULLI SOURCE p (BSS), HAMMING DISTORTION:
    d(x,x̂) = 1 if x ≠ x̂, else 0
    R(D) = H_b(p) - H_b(D) for D ≤ min(p, 1-p)
    = H(source) - H(noise): best rate at distortion D

    VECTOR QUANTIZATION:
    n-dimensional source → R bits total = R/n bits/dimension
    Distortion-rate D(R) = σ² 2^{-2R} for Gaussian (achievable asymptotically)
    → Geometric: each extra bit per dimension reduces distortion by 6 dB (factor 4)

    Practical limit: 1 byte JPEG block (8×8=64 coefficients, ~0.5 bits/pixel)
    vs. theoretical: R(D) for natural images much lower (images are structured)
```

---

## JPEG Compression Pipeline

```
    IMAGE PIPELINE (JPEG, lossy)
    ════════════════════════════════════════════════════════

    RGB image
         │
         ▼ Color space conversion
    YCbCr (luminance Y, chrominance Cb/Cr)
    Downsample Cb/Cr by 2× (human eye less sensitive to color detail)
         │
         ▼ Block DCT (8×8 blocks)
    Spatial domain → Frequency domain
    DCT-II: X[u,v] = (2/N)C(u)C(v) Σ_{x,y} x[i,j]cos(π(2i+1)u/2N)cos(π(2j+1)v/2N)
    DC coefficient (u=v=0) = average block luminance
    AC coefficients = spatial frequency content
         │
         ▼ QUANTIZATION (lossy step!)
    Divide each coefficient by quantization table Q[u,v]
    Round to nearest integer: round(X[u,v] / Q[u,v])
    High Q → coarser quantization → more loss → smaller file
    Quality=50 (standard): typical Q values 1-100
    High frequencies: larger Q → more reduction → visual quality insensitive
         │
         ▼ Zigzag scan + run-length encoding
    Reorder 8×8 block in zigzag (low freq → high freq)
    Exploit sparsity: long runs of zeros in high-frequency coefficients
    RLE on runs of zeros
         │
         ▼ Huffman coding (lossless step)
    Encode the quantized coefficients
    Separate Huffman tables for DC and AC coefficients
    DC: difference from previous block (DPCM)
    AC: (run-length, amplitude) pair coding

    Performance: compression ratio 10:1 to 30:1 for moderate quality
    → From ~24 bits/pixel (raw RGB) to ~1-2 bits/pixel (JPEG)
    → Theory: entropy rate of natural images ~0.1-0.5 bits/pixel
              (most visual information is redundant; spatial correlation is huge)
```

---

## H.264/HEVC/AV1: Video Compression

```
    VIDEO CODING PRINCIPLES
    ════════════════════════════════════════════════════════

    TEMPORAL PREDICTION (major difference from JPEG):
    I-frame: full JPEG-like coding (intra, no reference)
    P-frame: predicted from previous frames (forward prediction)
    B-frame: bidirectional prediction from past AND future frames
    Motion vectors: (dx, dy) pointing to best matching block in reference

    Motion compensation: subtract predicted block from actual block → residual
    Residual often near zero for slow motion → high compression of residual

    CODING STRUCTURE:
    GOP (Group of Pictures): I P P B P B B P ... (repeat pattern)
    Random access: must have I-frame to restart decoding
    GOP size tradeoff: large → better compression, worse seek time

    INTRA PREDICTION within frame:
    Predict from neighboring blocks already decoded
    H.264: 9 modes, HEVC: 35 modes, AV1: 56 modes
    Angular prediction: extrapolate from edge pixels along direction

    TRANSFORM + QUANTIZATION:
    4×4 or 8×8 DCT on residual block (same principle as JPEG)
    Rate-distortion optimization (RDO): choose prediction mode + quantization
    to minimize D + λR (Lagrange multiplier λ = distortion/bit tradeoff)

    ENTROPY CODING:
    CABAC (Context-Adaptive Binary Arithmetic Coding): ~15% better than Huffman
    Context model from neighboring blocks → better probability estimation

    COMPRESSION RATIOS:
    H.264 baseline: ~1-2 Mbps for 1080p30 (vs raw: 1 Gbps = 500:1 compression!)
    HEVC: ~35% better than H.264 for same quality
    AV1: ~30% better than HEVC (royalty-free, used by YouTube/Netflix)
    H.266/VVC: ~50% better than HEVC (2020 standard)
```

---

## Kolmogorov Complexity

The information-theoretic measure of the "complexity" of a single string.

$$K(x) = \min_{p: U(p) = x} |p|$$

where U is a universal Turing machine and |p| is the length of program p.

```
    PROPERTIES:
    K(x) ≤ |x| + O(1)  (trivial program: just print x)
    K(x) ≤ K(x|y) + K(y) + O(log K(y))
    K(xy) ≤ K(x) + K(y) + O(1)  (concatenation)
    K(x) ≥ H(X) on average for typical strings from source X (Shannon vs Kolmogorov)
    K(x) uncomputable: cannot decide if a program of length k outputs x
    (reduce from halting problem: if K(x) computable → contradicts Berry paradox / Chaitin)

    INCOMPRESSIBLE STRINGS:
    Most strings are incompressible: K(x) ≥ |x| - c for most x of length n
    "Random" strings = incompressible (cannot be shorter programs)
    Kolmogorov random = maximal algorithmic complexity for length

    MINIMUM DESCRIPTION LENGTH (MDL):
    Choose hypothesis H minimizing: L(H) + L(data|H)
    = two-part code: code for model + code for data given model
    → Bayesian model selection: prior = 2^{-L(H)}, P(data|H) = 2^{-L(data|H)}
    → MDL ≡ MAP (maximum a posteriori) Bayesian inference

    MDL = OCCAM'S RAZOR FORMALIZED:
    Prefer simpler hypotheses (shorter L(H)) that explain data well (shorter L(data|H))
    Tradeoff automatically handled by two-part code minimization
```

---

## LLMs as Compressors

```
    COMPRESSION-PREDICTION EQUIVALENCE (Ziv 1978, Shannon 1951):
    A probability model p(x_i|x_{i-1},...,x_1) defines a compressor:
    Encode x_i using -log₂ p(x_i|context) bits → arithmetic coding
    → Compressor reaches H(source) if model is perfect
    → Better model → better compression

    LANGUAGE MODELS ARE COMPRESSORS:
    GPT-4 on English text: ~2-3 bits/byte (≈1 bit/character)
    vs raw UTF-8: 8 bits/byte
    vs gzip: ~3.5 bits/byte
    → Best LLMs beat gzip by ~20-30% on natural language!

    CHINCHILLA COMPRESSION EXPERIMENTS (DeepMind 2023):
    Train LLM on enwik9 (first 10^9 bytes of Wikipedia)
    Compress using LLM probabilities + arithmetic coding
    Result: LM achieves ~900MB for enwik9 (vs raw: 1000MB, vs gzip: 300MB)
    → LLMs are better compressors than general-purpose algorithms on natural language
    → BUT: LLM itself takes GBs → "amortized" compression requires large corpus

    THEORETICAL CONNECTION:
    Intelligence = compression = prediction (Solomonoff, Hutter)
    Universal compressor = universal predictor (via AIT)
    AGI = minimizes K(world model) while maximizing prediction accuracy
    This is the theoretical grounding for: scale + more data → better LLMs
```

---

## Decision Cheat Sheet

| Task                            | Algorithm         | Rate          | Complexity        |
|---------------------------------|------------------|---------------|-------------------|
| Text compression                | LZ4/Zstandard    | ~2-3 bits/byte| O(n) fast         |
| High-ratio text compression     | LSTM/LM + AC     | ~1-2 bits/byte| O(n²) quadratic   |
| Image compression (lossy)       | JPEG / WebP      | 0.5-2 bits/px | O(n log n) DCT    |
| Image lossless                  | PNG (deflate)    | ~8-12 bits/px | O(n log n)        |
| Video compression               | H.264/H.265/AV1  | ~0.01 bits/px | O(n²) search      |
| Audio compression               | AAC, Opus        | 128-320 kbps  | O(n log n) MDCT   |
| Optimal prefix code             | Huffman          | H(X) to H+1   | O(n log n) sort   |
| Near-optimal, adaptive          | Arithmetic coding| H(X)          | O(n) per symbol   |
| Universal (unknown source)      | LZ77/LZ78        | → H as n→∞    | O(n) amortized    |
| Optimal lossy                   | Rate-distortion  | R(D)          | NP-hard in general|

---

## Common Confusion Points

**Huffman achieves H(X) + at most 1 bit/symbol overhead — not H(X) exactly**: Huffman is
optimal among prefix-free codes but cannot achieve fractional bit lengths (codeword lengths
are integers). For highly skewed distributions (one symbol with probability 0.99), Huffman
assigns 1 bit but H(X) ≈ 0.08 bits — 12× overhead. Arithmetic coding handles this correctly.

**LZ algorithms don't know the source distribution — and still achieve H(X)**: This is
the universality property. LZ77 builds an implicit model of the source as it encodes,
and the model converges to the true distribution for stationary ergodic sources. This
is why zip compresses different types of files reasonably well without being told the
source statistics.

**Rate-distortion R(D) is a one-way curve**: R(D) says the minimum rate to achieve distortion
D. It's not always true that operating at rate R always achieves distortion exactly R(D)^{-1}.
The curve says: if you're willing to tolerate distortion D, you can compress to R(D).
If you compress to rate R, the achievable distortion is D = R^{-1}(R). In practice,
JPEG/H.264/AV1 are 5-10× above R(D) for natural images due to engineering constraints.

**Kolmogorov complexity and Shannon entropy are different things**: K(x) applies to a single
string; H(X) applies to a distribution over strings. For typical strings from a distribution,
K(x) ≈ n H(X) (Theorem: |K(x)/n - H(X)| → 0 in probability). But K(x) can be much larger
or smaller than n H(X) for atypical strings. K is absolute; H is distributional.
