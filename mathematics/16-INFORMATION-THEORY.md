# Information Theory — Complete Reference

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         INFORMATION THEORY                                  │
│          Shannon (1948): communication as a mathematical problem            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ENTROPY FAMILY                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  H(X)          Shannon entropy of a source                           │  │
│  │  H(X,Y)        Joint entropy                                         │  │
│  │  H(X|Y)        Conditional entropy   (uncertainty remaining)         │  │
│  │  I(X;Y)        Mutual information    (shared information)            │  │
│  │  D(P||Q)       KL divergence         (information gain / surprise)   │  │
│  │  H(P,Q)        Cross-entropy         = H(P) + D(P||Q)                │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  CODING THEOREMS                                                            │
│  ┌───────────────────────────┐  ┌───────────────────────────┐             │
│  │  SOURCE CODING            │  │  CHANNEL CODING           │             │
│  │  Can compress to H(X)     │  │  Can transmit at C bits   │             │
│  │  bits per symbol          │  │  per use reliably         │             │
│  │  (no lossless below H)    │  │  (no reliable above C)    │             │
│  └───────────────────────────┘  └───────────────────────────┘             │
│                                                                             │
│  ML CONNECTIONS                                                             │
│  Cross-entropy loss  •  KL in VAEs  •  Mutual info in ICA                 │
│  Information bottleneck  •  Fisher info + Cramér-Rao  •  MDL              │
└─────────────────────────────────────────────────────────────────────────────┘
```

Shannon's 1948 paper "A Mathematical Theory of Communication" founded the field.
The key move: define **information** operationally — as the minimum number of bits
needed to describe outcomes — rather than semantically. Information is surprise.

---

## Shannon Entropy

### Definition

For a discrete random variable X with distribution P(X = xᵢ) = pᵢ:

```
H(X) = −Σᵢ pᵢ log pᵢ     (bits if log₂; nats if ln; avoiding 0 log 0 = 0)
```

**Units**: bits (log₂), nats (ln), trits (log₃). Information theory uses bits by
convention; ML often uses nats for cleaner calculus.

**Interpretation**: H(X) is the expected number of bits needed to describe a
sample from X, i.e., the average surprise under P.

Self-information of outcome xᵢ: I(xᵢ) = −log pᵢ.
- Certain event (pᵢ = 1): I = 0 bits — no surprise, no information.
- Fair coin flip (pᵢ = ½): I = 1 bit — exactly one bit of information.
- Rare event (pᵢ = 1/1000): I ≈ 10 bits — very surprising.

H(X) = E[I(X)] = expected self-information.

### Properties

```
Non-negativity:    H(X) ≥ 0, with equality iff X is deterministic
Maximum:           H(X) ≤ log |𝒳|, with equality iff X is uniform
                   (uniform distribution has maximum entropy)
Concavity:         H(λP + (1−λ)Q) ≥ λH(P) + (1−λ)H(Q) — concave in P
Chain rule:        H(X₁,...,Xₙ) = Σᵢ H(Xᵢ | X₁,...,Xᵢ₋₁)
Data processing:   if Z = f(X), then H(Z) ≤ H(X) (processing can't create info)
```

### Examples

| Distribution | Entropy |
|-------------|---------|
| Bernoulli(p): H = −p log p − (1−p) log(1−p) | Max 1 bit at p=½; 0 at p=0 or p=1 |
| Uniform on {1,...,n} | log₂ n bits |
| Geometric(p) | [−p log p − (1−p) log(1−p)] / p |
| Poisson(λ) | λ(1 − log λ) + e^{−λ} Σ λⁿ log(n!)/n! (no closed form) |

**Entropy of English text**: ~1–1.3 bits/character (highly redundant). Shannon
estimated this by having people predict the next character.

---

## Joint and Conditional Entropy

### Joint Entropy

```
H(X,Y) = −ΣΣ p(x,y) log p(x,y)
```

**Chain rule**: H(X,Y) = H(X) + H(Y|X) = H(Y) + H(X|Y)

### Conditional Entropy

```
H(Y|X) = Σₓ P(X=x) H(Y|X=x) = −ΣΣ p(x,y) log p(y|x)
```

H(Y|X) is the remaining uncertainty about Y after observing X.

**Non-negativity**: H(Y|X) ≥ 0, with equality iff Y is determined by X.
**Conditioning reduces entropy**: H(Y|X) ≤ H(Y), with equality iff X ⊥ Y.

### Subadditivity

```
H(X,Y) ≤ H(X) + H(Y)     with equality iff X ⊥ Y
```

Independent variables have maximum joint entropy. Dependence reduces it.

### Information Diagram

```
       H(X)              H(Y)
  ┌──────────────────────────────┐
  │       │           │          │
  │  H(X|Y) │  I(X;Y) │ H(Y|X)   │
  │       │           │          │
  └──────────────────────────────┘
         H(X,Y) = H(X|Y) + I(X;Y) + H(Y|X)
```

This Venn diagram of entropy: I(X;Y) is the overlap.

---

## Mutual Information

### Definition

```
I(X;Y) = H(X) − H(X|Y) = H(Y) − H(Y|X) = H(X) + H(Y) − H(X,Y)

         = ΣΣ p(x,y) log [p(x,y) / (p(x)p(y))]     (log-likelihood ratio form)
```

I(X;Y) measures how much knowing Y reduces uncertainty about X.

**Symmetric**: I(X;Y) = I(Y;X) — information is mutual.

**Non-negative**: I(X;Y) ≥ 0, with equality iff X ⊥ Y (log-sum inequality).

**Relation to KL**:
```
I(X;Y) = D(P_{XY} || P_X ⊗ P_Y)
```
Mutual information = KL divergence between the joint and the product of marginals.
It measures how far the joint distribution is from independence.

### Data Processing Inequality

If X → Y → Z form a Markov chain (Z depends on past only through Y):
```
I(X;Z) ≤ I(X;Y)     and     I(X;Z) ≤ I(Y;Z)
```

Processing can only lose information, never create it.

**Corollary**: sufficient statistics. T(X) is sufficient for θ iff I(X;θ) = I(T(X);θ).
Any further compression of T loses information about θ.

### Applications in ML

**Feature selection**: maximize I(feature; label). Mutual information captures
non-linear dependencies (unlike correlation).

**InfoMax / ICA**: Independent Component Analysis maximizes mutual information
between input and output to find statistically independent components. The
objective: I(Y; X) = H(Y) − H(Y|X) where Y = Wx.

**Information bottleneck** (Tishby et al.): find a compressed representation T
of X that retains maximal information about Y:
```
max I(T;Y) − β I(T;X)      (β controls compression/accuracy tradeoff)
```
Claimed to explain what deep networks learn (debated).

### MI as a Nonparametric Independence Criterion

Because I(X;Y) = 0 iff X ⊥ Y (regardless of distribution), mutual information is a
**nonparametric independence criterion** that captures arbitrary dependencies —
polynomial, periodic, multimodal — that correlation (which only detects linear
dependence) completely misses.

**HSIC** (Hilbert-Schmidt Independence Criterion) is a kernel-based analogue that is
also zero iff X ⊥ Y, amenable to efficient computation.

**MINE — Mutual Information Neural Estimator** (Belghazi et al. 2018): estimate I(X;Y)
in high dimensions by exploiting the Donsker-Varadhan representation:
```
I(X;Y) = D(P_{XY} || P_X ⊗ P_Y)
        = sup_{T: Ω→ℝ} E_{P_{XY}}[T] − log E_{P_X⊗P_Y}[eᵀ]
```
Maximize over a neural network T parameterized by θ. The supremum is achieved at
T* = log p(x,y)/(p(x)p(y)) — the log density ratio. MINE makes MI estimation
tractable for the high-dimensional continuous distributions that appear in deep learning,
enabling MI-based regularizers, disentanglement losses, and contrastive objectives
(InfoNCE, which underpins SimCLR and other self-supervised methods).

---

## KL Divergence

### Definition

```
D(P||Q) = Σₓ P(x) log [P(x) / Q(x)] = E_P [log P(x)/Q(x)]
```

(For continuous: replace sum by integral.)

**Interpretation**: extra bits needed to encode samples from P using a code
optimized for Q instead of P. "Surprise" at seeing P when expecting Q.

**Non-negative**: D(P||Q) ≥ 0 with equality iff P = Q (Gibbs' inequality).
*Proof*: −log is convex, so by Jensen's inequality: E_P[−log Q/P] ≥ −log E_P[Q/P] = 0.

**Asymmetric**: D(P||Q) ≠ D(Q||P) in general. Not a metric.

### Forward vs. Reverse KL

```
Forward KL (inclusive): D(P||Q) — min when Q covers all modes of P
  Q must be nonzero wherever P is nonzero
  "mean-seeking" — averages over all modes of P
  Used in: maximum likelihood (MLE = minimize D(P_data || P_model))

Reverse KL (exclusive): D(Q||P) — min when Q concentrates on a mode of P
  Q can be zero wherever P is small
  "mode-seeking" — latches onto one mode, ignores others
  Used in: variational inference, ELBO
```

This asymmetry is fundamental:
- **MLE** minimizes D(P_true || P_θ): the model must cover all observed data
- **VI** minimizes D(Q || P_true): the variational posterior seeks one mode

### ELBO (Evidence Lower Bound)

In variational inference, the log evidence log p(x) decomposes as:
```
log p(x) = ELBO(q) + D(q(z|x) || p(z|x))
ELBO(q)  = E_q[log p(x,z)] − E_q[log q(z|x)]
         = E_q[log p(x|z)] − D(q(z|x) || p(z))

log p(x) ≥ ELBO(q)   (D ≥ 0, so ELBO is a lower bound)
```

Maximizing ELBO = maximizing log p(x) while minimizing KL between approximate
and true posterior. **VAEs** optimize this objective end-to-end.

### f-Divergences

KL is one member of a family. For convex f with f(1) = 0:

```
D_f(P||Q) = ∫ q(x) f(p(x)/q(x)) dx
```

| Name | f(t) | Notes |
|------|------|-------|
| KL (forward) | t log t | MLE |
| KL (reverse) | −log t | Variational inference |
| Total variation | ½ | t−1 | | Bounded in [0,1] |
| χ² | (t−1)² | Hypothesis testing |
| Hellinger² | (√t−1)² | Symmetric, bounded |
| Jensen-Shannon | Symmetrized KL | GAN objective (original) |

**GAN objective**: original GANs minimize Jensen-Shannon divergence between the
real and generated distributions. Wasserstein GAN uses Earth Mover distance instead
(not an f-divergence), which has better gradient properties.

---

## Cross-Entropy

### Definition

```
H(P, Q) = −Σ P(x) log Q(x) = H(P) + D(P||Q)
```

Cross-entropy = true entropy + KL divergence. Measures average surprise under Q
when the true distribution is P.

**Minimizing H(P,Q) over Q (with fixed P) = minimizing D(P||Q)** — same optimal Q,
since H(P) doesn't depend on Q. This is why **cross-entropy loss = MLE**.

### Cross-Entropy Loss in ML

For classification with true labels P (one-hot: P(y=k) = 1 for the correct class)
and model probabilities Q (softmax output):

```
ℓ = −Σ_k P(k) log Q(k) = −log Q(y_true)
```

For a mini-batch: average over samples.

**Why cross-entropy, not MSE for classification?**
- Cross-entropy has smooth, well-behaved gradients w.r.t. logits before softmax
- MSE gradients vanish when the sigmoid/softmax output saturates
- Cross-entropy = MLE under a categorical model → statistically principled

**Binary cross-entropy** (logistic loss):
```
ℓ = −y log p − (1−y) log(1−p)     where p = σ(logit)
```

This is the negative log-likelihood of a Bernoulli random variable.

---

## Jensen's Inequality

For a convex function φ and random variable X:

```
φ(E[X]) ≤ E[φ(X)]
```

For concave φ the inequality flips. This single inequality proves essentially
everything in information theory:

| Result | Convex function used |
|--------|---------------------|
| H(X) ≥ 0 | φ = −log (concave) |
| H(X) ≤ log | 𝒳 | | Jensen on log |
| D(P || Q) ≥ 0 | φ = −log (applied to Q/P) |
| H(Y | X) ≤ H(Y) | Conditioning reduces entropy |
| Data processing ineq | Repeated Jensen |

---

## Source Coding Theorem

### Entropy as the Compression Limit

**Shannon's source coding theorem**: for an i.i.d. source with entropy H(X) bits:
- No lossless compression scheme can use fewer than H(X) bits per symbol on average
- Codes exist that achieve average length arbitrarily close to H(X)

This gives compression an absolute limit. It's a **theoretical** result (infinite
block lengths); practical codes approximate it.

### Huffman Coding

Assign shorter codewords to more probable symbols. Optimal prefix-free code.
Construction: build a tree bottom-up by repeatedly merging the two least probable
symbols. Average length satisfies: H(X) ≤ L̄ < H(X) + 1.

**The +1 gap**: Huffman codes symbol-by-symbol. Coding blocks of n symbols at once
achieves average length per symbol in [H(X), H(X) + 1/n] → H(X) as n→∞.

### Arithmetic Coding

Encode a sequence as a single number in [0,1), partitioning the interval by
probabilities. Approaches H(X) exactly for long sequences. Used in gzip, JPEG,
H.264. The AEP (below) explains why it works.

### Modern Compression: ANS and Capacity-Achieving Codes

**Asymmetric Numeral Systems (ANS / tANS)**: Jarek Duda (2014). The practical
successor to arithmetic coding — same asymptotic efficiency (approaches H(X) bits
per symbol) but with significantly lower computational overhead. Used in:
- **Zstandard** (Facebook, RFC 8478): tANS for literal lengths, match lengths
- **LZ4** with Huffman for high-speed compression
- **JPEG XL**: ANS-based entropy coding in the Brotli and JXL codecs

ANS encodes symbols by treating the state as a big integer and interleaving symbol
probabilities into it — conceptually a bijection between sequences and integers,
like arithmetic coding but with integer arithmetic instead of interval subdivision.

**Capacity-achieving channel codes** — the practical realization of Shannon's channel
coding theorem:

```
Turbo codes (Berrou 1993):   iterative decoding, BER near Shannon limit
  → 3G cellular, deep-space (NASA)

LDPC codes (Gallager 1960, rediscovered 1990s):
  Sparse parity-check matrices. Belief propagation decoding.
  → 10Gb Ethernet, WiFi 802.11n, DVB-S2

Polar codes (Arıkan 2009):
  Provably capacity-achieving under successive cancellation decoding.
  Mathematical construction via channel polarization: split N synthetic
  channels into ~NC "good" ones and ~N(1-C) "bad" ones.
  → 5G NR (control channel), Apple Data Compression Library
```

The connection: H(X) bits per symbol for sources → C bits per channel use for
channels. Both are exact, information-theoretic limits that took decades to approach
in practice. Polar codes are the first provably capacity-achieving codes with
efficient O(N log N) encoding and decoding.

### Asymptotic Equipartition Property (AEP)

For i.i.d. X₁,...,Xₙ ~ P:

```
−(1/n) log P(X₁,...,Xₙ) → H(X)   in probability (law of large numbers applied to log P)
```

**Typical set** A_ε^(n): sequences where −(1/n) log P ≈ H(X) ± ε.

Properties:
- P(A_ε^(n)) → 1 as n → ∞ (almost all long sequences are typical)
- |A_ε^(n)| ≈ 2^{nH(X)} (only exponentially many typical sequences)
- All typical sequences have roughly equal probability 2^{−nH(X)}

**Compression insight**: you only need to encode the ~2^{nH(X)} typical sequences.
Everything else can be assigned a special codeword (probability → 0). This is
why H(X) bits per symbol is achievable.

---

## Channel Capacity

### The Channel Model

```
Discrete memoryless channel:
  Input X → [Channel W(y|x)] → Output Y
  Each use: Y drawn from W(·|x) given input x
  Channel is "memoryless": uses are independent given the inputs
```

### Mutual Information as Capacity

**Capacity**: C = max_{P(X)} I(X;Y) bits per channel use.

**Shannon's channel coding theorem**:
- For any rate R < C: there exist codes of rate R achieving error probability → 0
- For any rate R > C: every code has error probability bounded away from 0

The capacity C is a sharp threshold. Below it: reliable communication is possible.
Above it: not.

### Common Channels

**Binary Symmetric Channel (BSC)**:
```
P(Y=0|X=0) = P(Y=1|X=1) = 1−p    (correct transmission)
P(Y=1|X=0) = P(Y=0|X=1) = p      (flip probability p)

C_BSC = 1 − H(p) = 1 − H_b(p)    (H_b = binary entropy function)
```
At p=0 or p=1: C=1 (perfect or perfectly inverted). At p=½: C=0 (useless channel).

**Binary Erasure Channel (BEC)**:
```
P(Y=X) = 1−ε,  P(Y=?) = ε    (erased with probability ε)

C_BEC = 1 − ε    (simple — just lose ε fraction of symbols)
```

**AWGN Channel** (Gaussian noise, power constraint P):
```
Y = X + Z,   Z ~ N(0, N₀/2),   E[X²] ≤ P

C = ½ log₂(1 + P/(N₀/2))   (Shannon-Hartley theorem, bits per channel use)
```

In bandwidth W Hz: C = W log₂(1 + SNR) bits per second. Every 3 dB increase in
SNR adds one bit per symbol. The fundamental limit for any modulation scheme.

### Converse: Why Can't We Exceed Capacity?

Fano's inequality: for any estimator X̂ of X from Y, with error probability Pₑ:
```
H(X|Y) ≤ H(Pₑ) + Pₑ log(|𝒳|−1)
```
If Pₑ → 0 then H(X|Y) → 0 → I(X;Y) → H(X). But I(X;Y) ≤ C by definition of C.
So H(X) ≤ C, meaning at most C bits per symbol can be reliably communicated.

---

## Differential Entropy

For a continuous random variable X with density f:

```
h(X) = −∫ f(x) log f(x) dx
```

**Caution**: differential entropy is not a proper limit of discrete entropy.
It can be negative (e.g., Uniform([0, ½])). Differences of differential entropies
are meaningful; absolute values less so.

### Maximum Entropy Distributions

Among all distributions with a given constraint, the maximum entropy distribution is:

| Constraint | Max-entropy distribution |
|-----------|-------------------------|
| Support [a,b] | Uniform([a,b]) |
| Mean = μ, support ℝ₊ | Exponential(1/(μ−a)) |
| Mean = μ, variance = σ² | Gaussian N(μ, σ²) |
| Mean = 0, covariance = Σ | Multivariate Gaussian N(0, Σ) |

**The Gaussian is the maximum entropy distribution for given variance.** This is
why it's the worst case in many information-theoretic bounds — least structured,
most uncertain — and why Gaussian noise is the hardest to communicate through.

### Differential Entropy of Gaussians

```
h(N(μ, σ²)) = ½ log(2πeσ²)    (in nats)

h(N(0, Σ)) = ½ log det(2πe Σ) = ½ log[(2πe)ⁿ det Σ]
```

**KL between Gaussians** (closed form — critical for VAEs):
```
D(N(μ₁,Σ₁) || N(μ₂,Σ₂)) = ½ [tr(Σ₂⁻¹Σ₁) + (μ₂−μ₁)ᵀΣ₂⁻¹(μ₂−μ₁) − n + log(det Σ₂/det Σ₁)]

For VAE (Σ₁=diag(σᵢ²), μ₁=μᵢ, Σ₂=I, μ₂=0):
D(q(z|x) || N(0,I)) = ½ Σᵢ (μᵢ² + σᵢ² − 1 − log σᵢ²)
```

---

## Fisher Information

### Definition

For a parametric family {p(x; θ)}, the **Fisher information** about θ in one observation:

```
I(θ) = E_θ[(∂/∂θ log p(X; θ))²] = −E_θ[∂²/∂θ² log p(X; θ)]

The "score" s(x;θ) = ∂/∂θ log p(x;θ) has E[s]=0 and Var[s] = I(θ).
```

**Matrix Fisher information** for θ ∈ ℝᵈ:
```
[I(θ)]ᵢⱼ = E[∂ log p/∂θᵢ · ∂ log p/∂θⱼ] = −E[∂² log p/∂θᵢ∂θⱼ]
```

### Cramér-Rao Bound

For any unbiased estimator T(X) of θ:

```
Var(T) ≥ 1/I(θ)         (scalar case)
Cov(T) ≥ I(θ)⁻¹         (matrix case, in PSD order)
```

No unbiased estimator can have variance below 1/I(θ). The bound is tight (achieved
by the MLE asymptotically — see Fisher efficiency).

**Intuition**: high Fisher information means the distribution changes sharply with θ
→ easy to distinguish nearby θ values → tighter estimation possible.

### Natural Gradient

The Fisher information matrix is the **Riemannian metric** on the statistical
manifold {p(x; θ)}. The ordinary gradient ∂L/∂θ is not invariant to
reparameterization; the **natural gradient** is:

```
ñ∇L = I(θ)⁻¹ ∇L
```

Natural gradient descent follows the steepest ascent on the manifold of
distributions, invariant to reparameterization. Used in:
- Natural policy gradient (reinforcement learning)
- K-FAC (Kronecker-Factored Approximate Curvature) — approximate natural gradient for neural nets
- Online EM for latent variable models

### Fisher Information and KL

```
D(p(·;θ+ε) || p(·;θ)) ≈ ½ εᵀ I(θ) ε    (for small ε)
```

Fisher information is the local curvature of KL divergence in parameter space.
This explains why it's the right metric for comparing nearby distributions.

---

## Rate-Distortion Theory

For lossy compression — accepting some distortion D to compress below H(X):

```
Rate-distortion function:  R(D) = min_{p(x̂|x): E[d(X,X̂)] ≤ D} I(X;X̂)
```

R(D) is the minimum bits/symbol needed to reconstruct X within average distortion D.

**For Gaussian source** X ~ N(0, σ²) with squared error distortion:
```
R(D) = max(½ log(σ²/D), 0)     (bits)
```
At D=0: R = ∞ (perfect reconstruction requires infinite rate).
At D=σ²: R = 0 (just predict the mean — no bits needed).

**Water-filling**: for vector Gaussian source (PCA components with variances σᵢ²),
the optimal scheme allocates bits to components like water filling:
```
Rᵢ = max(½ log(μ/σᵢ²), 0)    where μ is chosen so Σ Rᵢ = R_total
```
Allocate bits to less noisy (smaller σᵢ²) components first.

### Rate-Distortion in Practice: Learned Compression and the Perception-Distortion Tradeoff

**Water-filling and MIMO**: The water-filling solution is not just a compression
result — it is the optimal power allocation for MIMO (multiple-input multiple-output)
channels. Each spatial eigenmode of the channel has its own "noise level"; transmit
more power on better eigenmodes, zero power on poor ones. The math is identical to
Gaussian rate-distortion with σᵢ² replaced by noise-to-signal ratios.

**Learned image compression** (neural codecs): BPG, WebP, HEIC, JPEG XL all push
toward the R(D) limit for natural images. Neural approaches (Ballé et al. 2017+,
used in Google's WebP and codec research) model images with a learned prior and
optimize the ELBO — which is exactly R(D) in disguise. The trade-off is:
```
Rate: number of bits used = −log p(ẑ)  (quantized latent entropy)
Distortion: reconstruction loss d(x, x̂)
```

**Blau-Michaeli perception-distortion tradeoff (2018)**: A fundamental result showing
that perceptual quality (measured by any full-reference perceptual metric or divergence
between distribution of real and reconstructed images) and distortion (MSE/PSNR) are
in fundamental tension — you cannot simultaneously minimize both. The achievable
region in (distortion, perception) space is a convex curve; moving along it requires
trading one for the other. This explains why high-PSNR codecs look blurry while
GAN-based codecs look sharp but have higher MSE.

---

## Minimum Description Length (MDL)

**Two-part MDL**: choose model M and encode data D:
```
L(M) + L(D|M)    (model description length + data given model)
```

This is Occam's razor formalized. Minimizing MDL ≈ Bayesian model selection with
a uniform prior on models. Avoids overfitting: complex models (small L(D|M)) need
large L(M).

**Rissanen's MDL**: parameter θ ∈ ℝᵈ estimated from n samples requires
≈ (d/2) log n bits to describe (analogous to BIC).

### Kolmogorov Complexity — The Algorithmic Counterpart

MDL's statistical foundation has a deeper TCS counterpart: **algorithmic information
theory** (Solomonoff, Kolmogorov, Chaitin — 1960s).

```
Kolmogorov complexity of string x:
  K(x) = min { |p| : U(p) = x }   (length of shortest program on universal TM U
                                     that outputs x)
```

K(x) is the ultimate compression of x — the length of the shortest description.
It is **uncomputable** (K is not computable by any algorithm), but it is
conceptually prior to Shannon entropy.

**Relationship to Shannon entropy**:
```
For a computable distribution P:    E[K(x)] ≈ H(X)     (to O(log n) terms)
Conditional complexity:              K(x|y) ≈ H(X|Y)
Joint complexity:                    K(x,y) ≈ K(x) + K(y|x)
```
These parallels are exact (up to lower-order additive constants), but K is an
intrinsic property of individual strings while H is a property of distributions.

**Solomonoff induction**: the theoretically optimal predictor — weight all
computable hypotheses by 2^{−K(hypothesis)}. Learns any computable sequence in
the limit. Uncomputable in practice, but bounds all computable prediction algorithms
by the universal prior M(x) = Σ_{p: U(p)=x} 2^{−|p|}.

**Incompressibility method** (combinatorial lower bounds): to show a problem
requires Ω(f(n)) resources, exhibit an input x that is Kolmogorov-random (K(x) ≥ |x|),
then show the algorithm would compress x if it ran faster. Classic applications:
lower bounds for sorting decision trees, randomness extractors, communication complexity.

**MDL vs K-complexity**: MDL uses a specific model class (parametric family) and
penalizes by description length within that class. K-complexity is model-class-agnostic
— it considers all programs. MDL is the computable, practical version; K is the
Platonic ideal.

---

## Information Theory in ML — Reference Map

```
ML concept                   Information theory concept
──────────────────────────────────────────────────────
Cross-entropy loss           H(P_data, P_model) = H(P_data) + D(P_data||P_model)
KL regularizer in VAE        D(q(z|x) || p(z)) — match approx posterior to prior
GAN training (original)      Minimize JS divergence between real and generated
Mutual information in RL     Maximize I(policy; environment state)
Information bottleneck       max I(T;Y) − β I(T;X)
BIC / MDL                    Model complexity = (d/2) log n bits
Natural gradient / K-FAC     Steepest descent on statistical manifold
Sufficient statistic         T(X) s.t. I(X;θ) = I(T(X);θ)
Attention entropy (LLMs)     H(attention weights) — measure of focus
Max-entropy RL               Maximize E[R] + α H(π) — entropy-regularized policy
Calibration                  ECE = ‖P_true − P_predicted‖ — KL interpretation
```

### VAE ELBO — Full Derivation

```
log p(x) = log ∫ p(x,z) dz
         = log ∫ q(z|x) [p(x,z)/q(z|x)] dz
         ≥ ∫ q(z|x) log [p(x,z)/q(z|x)] dz    (Jensen, log is concave)
         = E_q[log p(x|z)] − D(q(z|x) || p(z))
         = ELBO

Gap = D(q(z|x) || p(z|x)) ≥ 0
Maximizing ELBO ↔ min D between approx and true posterior + max likelihood
```

The reconstruction term E[log p(x|z)] forces good reconstructions.
The KL term D(q||p(z)) forces the posterior to stay close to the prior N(0,I).
Tension between the two = compression/accuracy tradeoff.

### Information-Theoretic Generalization Bounds

A fundamental question: why do overparameterized neural networks generalize?
Information theory provides one lens through the **mutual information between
training data and learned weights**.

**Russo-Zou bound** (2016): For a learning algorithm A that takes training set S
and outputs weights W:
```
E[generalization gap] ≤ √(I(S; W) / (2n))    (for bounded losses)
```
where I(S; W) is the mutual information between the training set and the output
weights. Algorithms that don't "memorize" their training data (small I(S;W)) must
generalize well.

**Connection to PAC learning and VC dimension**: the classical VC bound says
```
generalization gap ≤ O(√(VC-dimension / n))
```
This bounds capacity via the hypothesis class complexity. The information-theoretic
bound instead tracks the actual compression of S into W by the specific algorithm —
potentially much tighter for stochastic optimizers like SGD, which have limited
information about the training set due to noise.

**CMI (Conditional Mutual Information) bounds** (Steinke-Zakynthinou 2020):
condition on a supersample and use ghost samples to eliminate the exponential
union bound. Gives tighter bounds for algorithms that are stable with respect to
individual examples (data-dependent, algorithm-dependent bounds rather than
worst-case over hypothesis class).

---

## Decision Cheat Sheet

| Need | Tool |
|------|------|
| How much info in a signal? | Shannon entropy H(X) |
| How much info shared by two variables? | Mutual information I(X;Y) |
| How different are two distributions? | KL divergence D(P\|\|Q) |
| Training a classifier (multiclass) | Cross-entropy loss = −log Q(y_true) |
| VAE regularization | KL(q(z\|x) \|\| p(z)) — closed form for Gaussians |
| GAN divergence | JS divergence (original GAN), Wasserstein (WGAN) |
| Compression limit | H(X) bits/symbol — absolute lower bound |
| Transmission rate limit | C = max I(X;Y) — Shannon capacity |
| Estimation variance lower bound | Cramér-Rao: Var(T̂) ≥ 1/I(θ) |
| Optimizer invariant to reparameterization | Natural gradient = I(θ)⁻¹∇L |
| Which model fits data without overfitting? | MDL / BIC: penalize by (d/2) log n |
| Maximum entropy distribution for given mean/var | Gaussian N(μ, σ²) |
| Nonparametric independence test | I(X;Y) = 0 iff X⊥Y; estimate via MINE for high-d |
| Modern lossless compression | ANS (Zstandard), polar codes approach capacity |
| Generalization bound for learning algorithm | I(S;W) mutual info bound (Russo-Zou) |

---

## Common Confusion Points

**KL divergence is not a distance**: D(P||Q) ≠ D(Q||P) and triangle inequality
fails. Jensen-Shannon divergence (½D(P||M) + ½D(Q||M), M=(P+Q)/2) is symmetric
and bounded in [0, log 2], but still not a metric in general.
The **Wasserstein distance** (Earth Mover Distance) is a true metric on distributions.

**Cross-entropy ≠ KL divergence**: H(P,Q) = H(P) + D(P||Q). They're equal only
when H(P) = 0. Minimizing cross-entropy w.r.t. Q is the same as minimizing KL
(since H(P) is constant), but their absolute values differ.

**Differential entropy can be negative**: unlike discrete entropy. h(Uniform[0, ½]) =
log(½) = −1 nat < 0. This is fine — differential entropy is not "bits needed to
describe a real number" (that's infinite); it's a relative concept.

**Entropy of 0 log 0 = 0**: the convention is 0 log 0 = 0 by continuity (lim_{p→0} p log p = 0).
Don't plug p = 0 into −log p = ∞.

**Mutual information is not linear**: I(X;Y,Z) ≠ I(X;Y) + I(X;Z). The correct
decomposition is I(X;Y,Z) = I(X;Y) + I(X;Z|Y) (chain rule for MI).

**Forward vs. reverse KL in practice**:
- D(P_data||Q_model): zero-forcing — model must not assign zero to anything P_data
  assigns positive mass. Favors overdispersed Q. MLE = this direction.
- D(Q_model||P_data): zero-avoiding — model avoids regions P_data avoids.
  Favors concentrated Q on one mode. VI = this direction, hence posterior collapse.

**Shannon capacity is per channel use, not per second**: C bits/use × W uses/second
= CW bits/second. The Shannon-Hartley formula already incorporates bandwidth W.

**Kolmogorov complexity vs Shannon entropy**: K(x) is defined for individual strings
and is uncomputable. H(X) is defined for distributions and is computable. They
agree in expectation but diverge for individual strings. A Kolmogorov-random string
(K(x) ≈ |x|) is individually incompressible; most strings drawn from a uniform
distribution are Kolmogorov-random.
