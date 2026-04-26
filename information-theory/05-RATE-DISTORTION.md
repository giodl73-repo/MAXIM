# Rate-Distortion Theory

```
THE FUNDAMENTAL TRADEOFF

Source X ──[Encoder]──> codeword (R bits/symbol) ──[Decoder]──> X̂

     Perfect reproduction:  R = H(X)          D = 0
     Tolerate distortion:   R = R(D) < H(X)   D > 0
     Extreme compression:   R → 0             D → D_max

     Key question: What is the minimum rate R to achieve distortion ≤ D?

     ┌─────────────────────────────────────────────────────┐
     │  R                                                  │
     │  │  R(0) = H(X) ──────────────────────────────•     │
     │  │              \                                   │
     │  │               \  R(D) curve                      │
     │  │                \      (convex, non-increasing)   │
     │  │                 \                                │
     │  │                  '─────────────────────────      │
     │  │                           D_max    D             │
     │  └────────────────────────────────────────────      │
     │  D_max = E[d(X, x̂_const)] for best constant x̂       │
     └─────────────────────────────────────────────────────┘
```

---

## 1. Formal Definition

**Distortion measure**: d(x, x̂) ≥ 0 with d(x,x) = 0. Common choices:

| Measure | Formula | Domain |
|---------|---------|--------|
| Hamming | 1[x ≠ x̂] | Discrete |
| Squared error | (x - x̂)² | Continuous |
| Absolute error | |x - x̂| | Continuous |
| Log loss | log(1/p(x)) | Probabilistic |

**Rate-distortion function**:

```
R(D) = min_{p(x̂|x)} I(X; X̂)

subject to:
  1. E[d(X, X̂)] = Σ_{x,x̂} p(x)p(x̂|x) d(x,x̂) ≤ D
  2. p(x̂|x) ≥ 0, Σ_{x̂} p(x̂|x) = 1  ∀x
```

The optimization is over all stochastic maps (test channels) p(x̂|x).

**R(D) theorem** (Shannon 1959): For any R > R(D), there exists a sequence of (2^{nR}, n) codes
with expected distortion → D. For R < R(D), expected distortion > D for any code.

Properties of R(D):
- R(D) is convex and non-increasing in D
- R(0) = H(X) for lossless case (discrete source)
- R(D_max) = 0 where D_max = min_{x̂} E[d(X, x̂)]
- Domain: D ∈ [D_min, D_max] where D_min = Σ_x p(x) min_{x̂} d(x, x̂)

---

## 2. Shannon Lower Bound

For continuous sources with differential entropy:

```
R(D) ≥ h(X) - max h(X̂)
             E[d(X,X̂)]≤D

For squared-error distortion:
  max h(X̂) subject to E[(X-X̂)²] ≤ D  →  achieved by Gaussian X̂
  h(N(0,D)) = ½ log(2πeD)

Shannon lower bound:
  R(D) ≥ h(X) - ½ log(2πeD)
```

This is tight for Gaussian sources. For non-Gaussian sources with same variance, R(D) ≥ R_Gaussian(D)
— the Gaussian source is hardest to compress at a given D.

**Proof sketch**: I(X;X̂) = h(X̂) - h(X̂|X) ≥ h(X̂) - h(X-X̂|X) ≥ h(X̂) - h(X-X̂).
With E[(X-X̂)²] ≤ D, entropy power inequality gives h(X-X̂) ≤ ½ log(2πeD).

---

## 3. Gaussian Source: R(D) in Closed Form

```
X ~ N(0, σ²), distortion = squared error

        ┌
        │  ½ log₂(σ²/D)    if D ≤ σ²
R(D) = ─┤
        │  0                if D > σ²
        └

Rearranged: D(R) = σ² · 2^{-2R}   (distortion at rate R)

At R = 0:  D = σ²     (just use mean 0; error = variance)
At R = 1:  D = σ²/4   (1 bit halves log-distortion)
At R → ∞:  D → 0      (exact reproduction)
```

**Key insight**: Each additional bit reduces distortion by factor 4 (6 dB in signal processing).
This is the theoretical limit — JPEG/MP3/etc. approach but don't achieve it.

**Why Gaussian is special**: For X ~ N(0,σ²) and squared error, the optimal test channel is:
X̂ = X + N(0, D) after scaling, or equivalently X̂ = αX where α = 1 - D/σ². The reconstruction
noise is independent Gaussian, matching the channel coding duality.

---

## 4. Gaussian Vector Source: Reverse Waterfilling

For X = (X₁,...,Xₙ) with independent components Xᵢ ~ N(0,σᵢ²), total distortion D_total:

```
Reverse waterfilling: allocate distortions Dᵢ to minimize total rate

  R(D) = Σᵢ max(0, ½ log₂(σᵢ²/λ))

  Dᵢ = min(λ, σᵢ²)     ← water level λ chosen so Σ Dᵢ = D_total

     σᵢ²  ┌───┐                    Variance profile
          │   │   ┌───┐
          │   │   │   │   ┌───┐
          │   │   │   │   │   │  ┌───┐
λ ───────────────────────────────────────  "water level"
          │   │   │   │   │   │  │///│  ← these get 0 bits (σ² ≤ λ)
          └───┘   └───┘   └───┘  └───┘
           i=1     i=2     i=3    i=4
        (allocate bits above λ)
```

**Contrast with waterfilling** (channel capacity): power allocation fills water upward into channels
with good SNR. Rate-distortion reverse waterfilling fills water downward — allocate bits only to
components with variance ABOVE the water level. Components with σᵢ² ≤ λ get zero bits; set X̂ᵢ = 0.

**Application**: Transform coding. Apply KL transform (PCA) to decorrelate source, then reverse
waterfill. Theoretical optimum for Gaussian vectors. JPEG approximates this with DCT + quantization.

---

## 5. Blahut-Arimoto Algorithm

Computes R(D) for discrete sources numerically via alternating optimization.

```
Inputs: p(x), d(x,x̂)
Output: R(D) for given D (or s parameter version)

Parametric form: R(s) = min_{p(x̂|x)} [I(X;X̂) - s·E[d(X,X̂)]]   s ≤ 0
                 D(s) = E[d(X,X̂)] at optimal p(x̂|x)

Initialize: p(x̂) uniform

Iterate until convergence:
  E-step (fix p(x̂), update p(x̂|x)):
    p(x̂|x) ∝ p(x̂) · exp(s·d(x,x̂))

  M-step (fix p(x̂|x), update p(x̂)):
    p(x̂) = Σ_x p(x)·p(x̂|x)

Convergence: geometric rate; I(X;X̂) decreases monotonically
```

**EM connection**: The Blahut-Arimoto algorithm is an EM algorithm on a mixture model.
E-step computes posterior p(x̂|x); M-step computes marginal. The Lagrangian −I(X;X̂) + s·E[d]
is the free energy. Convergence follows from EM convergence theory (coordinate ascent on
convex-concave saddle point).

**Complexity**: Each iteration O(|X|·|X̂|). Sweep over s parameter traces out the R(D) curve.

---

## 6. Transform Coding and Lossy Compression in Practice

**Transform coding theorem**: For a Gaussian source with correlation matrix K_X, the optimal
linear transform is the KL transform (eigenvectors of K_X). After decorrelation:
1. Apply eigendecomposition K_X = UΛUᵀ
2. Transform: Y = UᵀX  (components have variances λ₁ ≥ λ₂ ≥ ... ≥ λₙ)
3. Reverse waterfill across variances {λᵢ}
4. Quantize each component independently

**DCT as approximation**: For stationary sources with high inter-sample correlation, DCT
approximates the KL transform. JPEG uses 8×8 DCT blocks — rate-distortion suboptimal but
fast and compatible with learned quantization matrices.

```
Compression standard comparison:

┌──────────────┬─────────────────┬──────────────────┬─────────────────────┐
│ Standard     │ Transform       │ Entropy coding   │ R-D gap vs Shannon  │
├──────────────┼─────────────────┼──────────────────┼─────────────────────┤
│ JPEG         │ DCT (8×8)       │ Huffman          │ ~2-3 dB             │
│ JPEG-2000    │ DWT (9/7)       │ EBCOT (MQ-coder) │ ~0.5-1 dB           │
│ H.264        │ DCT + motion    │ CABAC            │ ~0.5 dB             │
│ H.265/HEVC   │ DCT (4×4-32×32) │ CABAC            │ ~0.3 dB             │
│ AV1/VVC      │ DCT/DST + adapt │ ANS              │ ~0.1-0.2 dB         │
│ Neural (2024)│ Learned         │ ANS + hyperprior │ Near Shannon        │
└──────────────┴─────────────────┴──────────────────┴─────────────────────┘
```

---

## 7. Quantization Theory

**Scalar quantization**: Map continuous X → discrete X̂ via quantization regions {Rᵢ} and
reconstruction points {x̂ᵢ}. For N levels over distortion D:

**Lloyd-Max conditions** (necessary for optimal quantizer):
1. Nearest-neighbor: Rᵢ = {x : d(x, x̂ᵢ) ≤ d(x, x̂ⱼ) ∀j}
2. Centroid: x̂ᵢ = E[X | X ∈ Rᵢ]  (minimizes MSE given regions)

For squared error + high-rate approximation (many levels N):
```
MSE ≈ 1/(12N²) · [∫ p(x)^{1/3} dx]³

Optimal density of quantization points: f_q(x) ∝ p(x)^{1/3}
  (more points where density is high, but not proportional to p)
```

**Entropy-coded quantization** (rate-distortion optimal):
- Scalar uniform quantization + arithmetic coding approaches R(D) for Gaussian sources
- At high rates, entropy H(X̂) ≈ h(X) - log(Δ) where Δ = step size
- R(D) = h(X) - log(√(12D)) for large N (Gaussian sources approach this)

---

## 8. Vector Quantization

VQ maps blocks of n samples to codewords from codebook C = {c₁,...,cₖ}.
Rate = (log₂ k)/n bits per sample. As n → ∞, VQ achieves R(D) (shape gain + memory gain).

```
┌─────────────────────────────────────────────────────────────────┐
│  VQ for n-dimensional vectors:                                  │
│                                                                 │
│  Training: LBG algorithm (k-means generalization)               │
│    Init: split codebook (Lloyd doubling)                        │
│    Iterate: Voronoi partition + centroid update                 │
│    Convergence: monotone decrease in quantization error         │
│                                                                 │
│  Variants:                                                      │
│    Residual VQ (RVQ): quantize, then quantize residual          │
│      X → q₁(X) → X - q₁(X) → q₂(X-q₁) → ...                     │
│      Used in: neural codec language models (EnCodec, DAC)       │
│                                                                 │
│    Product Quantization (PQ): split vector, quantize subspaces  │
│      X = [X₁, X₂, ..., Xₘ]  (d/m dimensions each)               │
│      Rate = m · log₂(k)/n  bits/sample                          │
│      Used in: FAISS ANN search, ANN vector databases            │
└─────────────────────────────────────────────────────────────────┘
```

**PQ as ANN index**: Decompose vector into m subspaces, each with k centroids.
Asymmetric distance computation (ADC) approximates L2 distance without full reconstruction.
Connects to information-theoretic lower bound: optimal lossy compression of query-database pairs.

---

## 9. Perceptual Distortion and Generative Models

Mean squared error is a terrible perceptual metric. Shannon's theory works for any distortion
measure — but the choice of measure changes what R(D) means in practice.

**The perception-distortion tradeoff** (Blau-Michaeli, 2018):

```
Perception quality P(D): how "realistic" is the reconstruction
Distortion D:            pixel-level fidelity (MSE, SSIM)

┌─────────────────────────────────────────────────────────┐
│  P                                                      │
│  │ • (perfect perception, high distortion)              │
│  │   [generative models: hallucinate details]           │
│  │    \                                                 │
│  │     \   Pareto frontier                              │
│  │      \                                               │
│  │       \                                              │
│  │        • (low distortion, imperfect perception)      │
│  │          [averaging: blurry but PSNR-optimal]        │
│  └──────────────────────────────────────── D            │
└─────────────────────────────────────────────────────────┘
```

**Key result**: Perfect perceptual quality (P(D) = 0) requires additional noise injection.
Minimum distortion at perfect perception equals the Wasserstein distance W₂(p_X, p_{X̂}).

**Learned metrics**: MS-SSIM, LPIPS (learned perceptual image patch similarity) use neural
features as basis for distortion. Rate-distortion theory still applies — just with a different
distortion measure that better predicts human perception.

**Generative model implication**: Diffusion models, GANs, and flow models operate at the
high-perception / high-distortion corner. They achieve low perceptual distortion by sampling
from p(X̂|compressed_code) rather than MAP decoding. This trades pixel accuracy for realism.

---

## Decision Cheat Sheet

| Source type | Distortion metric | Optimal approach | Standard |
|-------------|-------------------|------------------|----------|
| Gaussian scalar | MSE | Gaussian test channel | Shannon limit |
| Gaussian vector | MSE | KL transform + reverse waterfill | JPEG-2000 (approx) |
| Speech | Perceptual | LPC + VQ (MELP) / neural codec | Opus, EnCodec |
| Image (natural) | PSNR | DCT/DWT + entropy code | JPEG, JPEG-2000 |
| Image (perceptual) | LPIPS | Diffusion / GAN decoder | Stable Diffusion |
| Video | PSNR/VMAF | Motion + DCT + CABAC | H.265, AV1 |
| High-dim vectors | L2 approx | Product quantization | FAISS, ScaNN |
| Symbolic/text | Hamming | Source coding (lossless) | zstd, brotli |
| Genomic | Specialized bio | Reference-based compression | CRAM |

**Rate budget intuition** (images at 512×512×3 = 786,432 pixels):
- Uncompressed: 8 bits/pixel = 6.3 MB
- JPEG quality 90: ~0.8 bits/pixel ≈ 80 KB
- JPEG-2000: ~0.4 bits/pixel ≈ 40 KB
- Neural (2024): ~0.1 bits/pixel ≈ 10 KB (near R(D) for MSE)
- Shannon limit (MSE): ~0.08 bits/pixel (theoretical, not practical)

---

## Common Confusion Points

**R(D) vs D(R)**: R(D) = minimum rate for distortion ≤ D. D(R) = minimum distortion at rate R.
They're inverses. You'll see both in papers; context determines which parameterization is used.

**Waterfilling vs reverse waterfilling**: Waterfilling = channel capacity (allocate power to
good channels). Reverse waterfilling = rate-distortion (allocate bits, skip low-variance
components). Both have water levels but the directions differ.

**R(0) for continuous sources**: For continuous X, R(0) = ∞ (infinite bits for exact reproduction).
The Gaussian R(D) formula shows R → ∞ as D → 0. This is correct — continuous sources need
infinite bits for perfect fidelity.

**VQ achieving R(D)**: Scalar quantization generally cannot achieve R(D) (shape gap).
VQ with dimension n → ∞ achieves R(D) but is computationally intractable. PQ is a structured
compromise: polynomial complexity, bounded loss from optimal.

**MSE optimality of averaging**: For MSE distortion, the optimal decoder is E[X|code] —
the conditional mean. This is why MMSE estimators are correct for MSE but produce blurry
outputs. The perception-distortion tradeoff explains why MAP or sampling decoders look better.

**Blahut-Arimoto parameter s**: The algorithm parameterizes by s ≤ 0 (Lagrange multiplier
on distortion). Each s gives one (R,D) point on the curve. To get a specific D, you binary
search on s. The curve is traced by varying s from 0 (D = D_max) to −∞ (D → D_min).
