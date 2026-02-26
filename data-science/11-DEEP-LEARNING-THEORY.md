# Deep Learning Theory
## Why Deep Nets Work — Universal Approximation, NTK, Scaling Laws, and More

```
THE DEEP LEARNING THEORY MAP

  Why can they represent?    Why can they be trained?   Why do they generalize?
  ────────────────────────   ───────────────────────    ───────────────────────
  Universal approximation    Loss landscape             Double descent
  Expressivity vs depth      NTK (infinite-width)       Implicit bias of GD
  Attention as sparse lookup Lazy training regime       Flat minima (SAM)

  Why do they get better with scale?
  ───────────────────────────────────
  Scaling laws (Kaplan, Chinchilla)
  Emergent abilities
  Phase transitions
```

---

## 1. Universal Approximation

**Theorem (Cybenko 1989, Hornik 1991)**: A single hidden layer neural net with any continuous non-polynomial activation σ can approximate any continuous function on a compact domain to any ε accuracy — given enough hidden units.

```
  f(x) ≈ Σ_{j=1}^N c_j σ(w_j^T x + b_j)

  For N large enough: sup_{x∈K} |f(x) - g(x)| < ε  for any g ∈ C(K)
```

**What UAT doesn't say**:
- It doesn't say how large N needs to be (can be exponential in dimension)
- It doesn't say GD finds the approximating weights
- It's an existence result, not a constructive algorithm

**Width vs depth trade-off**:
```
  Width: 1 hidden layer needs exponentially many units to represent some functions
  Depth: O(poly(d)) units suffice with logarithmic depth (for piecewise linear functions)

  Formal result (Eldan & Shamir 2016): there exist functions representable by
  depth-3 networks of poly(d) width that require exponential width for depth-2.

  Intuition: depth ≡ composition of simple functions → exponential expressivity growth
```

**Activation functions and approximation**:
```
  ReLU: σ(x) = max(0,x)
    Creates piecewise linear functions
    N neurons, depth L → at most 2^{NL} linear regions (but exponential in depth)

  Smooth activations (sigmoid, tanh, GELU):
    Universal in the function space sense, smoother optimization landscape
    GELU (Gaussian Error Linear Unit): x·Φ(x) — preferred for transformers
```

---

## 2. Depth and Expressivity

```
  Circuit complexity analogy (MIT TCS connection):

  ┌────────────────────────────────────────────────────────┐
  │  Shallow circuit  ≡  wide shallow network              │
  │  Deep circuit     ≡  deep narrow network               │
  │                                                         │
  │  NC¹ ⊂ NC² ⊂ ... ⊂ P  (likely strict, unproven)       │
  │   ↕                                                     │
  │  depth-1 ⊂ depth-2 ⊂ ... (strict separation in size)  │
  └────────────────────────────────────────────────────────┘

  Depth separation theorems tell us that depth is computationally necessary.
  In practice: depth enables hierarchical feature reuse.
```

**Hierarchical features**:
```
  CNNs on images:
    Layer 1: edges, frequencies
    Layer 2: textures, corners
    Layer 3: object parts
    Layer 4+: objects, scenes

  This hierarchy is learned, not designed.
  Deeper layers: increasingly abstract, more invariant representations.
```

---

## 3. Attention — The Mathematics

Scaled dot-product attention (Vaswani et al. 2017):

```
  Inputs:
    Q ∈ ℝ^{n×d_k}  (queries)
    K ∈ ℝ^{m×d_k}  (keys)
    V ∈ ℝ^{m×d_v}  (values)

  Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V

  QKᵀ ∈ ℝ^{n×m}:  raw attention scores (query-key compatibility)
  /√d_k:           scale to prevent softmax saturation
  softmax:         row-wise normalization → attention weights ∈ Δ^m
  · V:             weighted combination of values
```

**Why √d_k scaling?**
```
  If Q, K have entries ~N(0,1), then (Q·K^T)_{ij} = Σ_{l=1}^{d_k} q_l k_l
  E[(qᵢ·kⱼ)²] = d_k  (sum of d_k unit-variance terms)
  Std dev ≈ √d_k

  Without scaling: softmax input has std ≈ √d_k
  For large d_k (e.g., 64): logits in range ±8 → softmax ≈ one-hot → vanishing gradients
  With √d_k scaling: std ≈ 1 → gradients flow normally
```

**Multi-head attention**:
```
  head_i = Attention(Q W_i^Q, K W_i^K, V W_i^V)
  MultiHead(Q,K,V) = Concat(head_1,...,head_h) W^O

  Each head attends to a different "subspace" of the representation.
  h=8 heads, d_k = d_model/h  (constant total compute)
```

**Attention is O(n²) in sequence length**: for n tokens, QKᵀ has n² entries. For n=100K (long documents), n²=10^10. This is the fundamental bottleneck → sparse attention, linear attention, state space models.

**Attention as retrieval**:
```
  Keys K = "database entries"
  Query Q = "search query"
  Values V = "contents to retrieve"

  Hard retrieval (argmax → one-hot attention): nearest neighbor lookup
  Soft retrieval (softmax): continuous interpolation across all entries
  Transformer: differentiable, end-to-end trainable key-value memory
```

---

## 4. Batch Normalization

**Operation** (Ioffe & Szegedy 2015):
```
  For activation x ∈ ℝ^d over batch B = {x_1,...,x_m}:

    μ_B = (1/m) Σ x_i              batch mean
    σ²_B = (1/m) Σ (x_i - μ_B)²   batch variance

    x̂_i = (x_i - μ_B) / √(σ²_B + ε)     normalize
    y_i = γ x̂_i + β                       scale and shift (learned)
```

**Why it works** — two competing theories:

**Theory 1 — Internal Covariate Shift (original claim)**:
Reduces shift in distribution of layer inputs during training. Allows higher LR.
*Problem*: empirically contested — removing BN from covariate shift perspective doesn't clearly hurt.

**Theory 2 — Smooths the loss landscape** (Santurkar et al. 2018):
BN makes loss more Lipschitz smooth. Larger gradient steps remain valid. Better-conditioned optimization.
*Supported by*: measuring gradient predictiveness and Lipschitz constant with/without BN.

**Layer Normalization** (Ba et al. 2016): normalize across features, not batch.
```
  LN(x) = γ · (x - μ_x)/σ_x + β   where statistics computed over feature dim

  Works at batch size 1 → preferred for:
    - Transformers (variable length sequences)
    - RNNs (sequential processing)
    - Inference scenarios
```

**Comparison**:
| | BatchNorm | LayerNorm | GroupNorm | InstanceNorm |
|--|-----------|-----------|-----------|--------------|
| Normalize over | batch | features | feature groups | spatial |
| Works with batch=1 | ❌ | ✅ | ✅ | ✅ |
| Used in | CNNs | Transformers | Detection | Style transfer |

---

## 5. Neural Tangent Kernel (NTK)

For infinitely-wide neural networks, gradient descent training behaves like kernel regression.

**Kernel methods bridge**: If you know kernel SVMs or Gaussian Processes, the NTK
maps directly. The NTK Θ(x, x') is the kernel induced by the neural network's
parameterization. In the lazy training regime, the network function lives in the
RKHS defined by Θ — exactly the setting of kernel regression. Training gradient
descent on a squared loss with this kernel converges (because Θ is PSD in the
infinite-width limit), and the converged solution is the minimum-norm interpolant
in that RKHS. The entire well-developed theory of kernel learning — generalization
bounds, representer theorem, condition number of K — applies directly. The key
difference from a fixed GP/SVM kernel: in finite networks, Θ itself changes during
training (the "feature learning" regime), which is precisely what makes neural nets
more powerful than fixed kernels on structured data.

**Setup**: consider a network f(x; θ) with parameters θ ∈ ℝ^p.

**NTK definition**:
```
  Θ(x, x') = ∇_θ f(x; θ)ᵀ ∇_θ f(x'; θ)   ∈ ℝ (scalar for 1-output net)

  This is a kernel measuring how similarly two inputs affect the parameters.
```

**Key result** (Jacot et al. 2018):
```
  In the infinite-width limit:
  1. NTK Θ stays approximately constant during training (lazy training regime)
  2. Training with gradient descent on MSE → kernel regression with kernel Θ

  f(x; θ_T) ≈ y_train · (K + λI)^{-1} K(·, x_train)   ← kernel regression solution

  Where K_{ij} = Θ(x_i, x_j)
```

**Implications**:
- Infinite-width nets are linear models in function space (around initialization)
- Convergence guaranteed for sufficiently wide nets (K is PD)
- Explains why wide nets train smoothly and generalize (kernel generalization theory applies)

**Limitations of NTK**:
- Only applies in lazy training regime (small parameter changes)
- Real neural nets learn features (kernel changes) — this is the source of their power over fixed kernels
- Finite-width nets deviate significantly — feature learning regime

**Feature learning vs lazy training**:
```
  Lazy (NTK) regime:  large initialization, small LR
    → parameters barely move, function changes linearly
    → equivalent to kernel regression

  Feature learning regime: small initialization, large LR
    → parameters move substantially, kernel changes
    → network learns representations, not just fitting
    → this is where neural nets beat fixed kernels

  μP (maximal update parameterization, Yang et al.): scaling that maintains
  feature learning at all widths → better LR transfer across scale
```

---

## 6. Double Descent in Deep Learning

(Already covered in 07-STATISTICAL-LEARNING, restated here for DL context.)

```
  Test error
    │
    │  ╲     /───────  Epoch-wise double descent
    │   ╲___/
    │    ↑
    └────┴──────────────→ Training epochs / model size

  Also occurs as a function of model size (param count).
  Interpolation threshold: exactly when model can fit training set.
```

**Mechanisms in deep learning**:
1. **Model size double descent**: interpolation at `n_params ≈ n_data`
2. **Epoch-wise double descent**: test error rises then falls during training at the threshold
3. **Label noise amplifies the effect**: clean data shows mild double descent; noisy labels = pronounced hump

**Practical consequence**: don't stop training just because test error temporarily rises.

---

## 7. Scaling Laws

**Kaplan et al. (OpenAI, 2020)** — power law relationship:
```
  L(N) ∝ N^{-α_N}  (loss vs parameters, infinite data)
  L(D) ∝ D^{-α_D}  (loss vs data, infinite compute)
  L(C) ∝ C^{-α_C}  (loss vs compute, optimally allocated)

  Exponents for language models:
    α_N ≈ 0.076
    α_D ≈ 0.095
    α_C ≈ 0.050

  Implication: for fixed compute, scale both N and D — neither alone is optimal.
  Kaplan et al. recommended: scale N faster than D (flawed, as Chinchilla showed).
```

**Chinchilla (Hoffmann et al., DeepMind, 2022)**:
```
  Compute-optimal training: given compute budget C = 6ND (approx):

    N_opt ∝ C^{0.5}
    D_opt ∝ C^{0.5}

  Optimal allocation: N ≈ 20D (train for ~20 tokens per parameter)

  Example:
    GPT-3 (175B params, 300B tokens): undertrained by Chinchilla criteria
    Chinchilla (70B params, 1.4T tokens): better than GPT-3 with less compute

  Implication: most large models are undertrained; given a fixed N, train much longer.
```

**Neural scaling law structure**:
```
  L(N, D) = E + A/N^α + B/D^β   (three components)

    E = irreducible entropy (Bayes optimal loss)
    A/N^α = contribution from finite model size
    B/D^β = contribution from finite data

  These terms are additive and independent — model size and data are separable.
```

---

## 8. Emergent Abilities

At certain scale thresholds, qualitatively new capabilities appear discontinuously.

```
  Benchmark performance
    │
    │                    ╱
    │___________________╱
    │                   ↑
    └───────────────────┴──→ Model scale (FLOP or params)
                         emergent threshold

  Examples:
    Chain-of-thought reasoning:  ~62B params threshold
    Few-shot arithmetic:         ~1B params
    In-context learning:         ~100M params
    BIG-Bench tasks:             vary widely
```

**Debate**:
- **Sharp emergence hypothesis**: true phase transitions due to composing capabilities
- **Metric artifact hypothesis** (Schaeffer et al. 2023): continuous improvement in probability space; nonlinear metrics (accuracy) create apparent discontinuities. Smooth metrics show smooth improvement.

**Phase transitions analogy** (statistical physics): sudden changes in macroscopic behavior from continuous microscopic dynamics. Whether deep learning has true phase transitions is an open question.

---

## 9. Diffusion Models — Score-Based Generative Models

Diffusion models are now the dominant framework for high-quality generation (images,
audio, protein structure, video). The core idea: learn to reverse a gradual noising
process by learning the score function of the data distribution.

### Forward Process (DDPM — Denoising Diffusion Probabilistic Models)

```
Given data x₀ ~ q(x₀), define a fixed Markov chain that gradually adds Gaussian noise:

  q(xₜ | x_{t-1}) = N(xₜ; √(1-βₜ) x_{t-1}, βₜ I)

  where β₁,...,βᵀ is a noise schedule (small, increasing)

Closed-form marginal at any timestep t (αₜ = Π_{s=1}^t (1-βₛ)):

  q(xₜ | x₀) = N(xₜ; √ᾱₜ x₀, (1-ᾱₜ) I)
  ⟹  xₜ = √ᾱₜ x₀ + √(1-ᾱₜ) ε,   ε ~ N(0, I)

At T large (T=1000 in DDPM), xᵀ ≈ N(0, I) — pure noise, independent of x₀.
```

### Reverse Process — Learning to Denoise

```
The true reverse p(x_{t-1} | xₜ) is intractable (requires knowing q(x₀)).
Learn a neural network approximation:

  p_θ(x_{t-1} | xₜ) = N(x_{t-1}; μ_θ(xₜ, t), Σ_θ(xₜ, t))

Ho et al. (DDPM): parameterize as noise prediction:
  ε_θ(xₜ, t) ≈ ε  (predict the noise added at step t)

  μ_θ(xₜ, t) = (1/√αₜ)(xₜ - βₜ/√(1-ᾱₜ) · ε_θ(xₜ, t))
```

### Training Objective

```
Simple noise prediction loss (Ho et al. simplified ELBO):

  L = E_{t, x₀, ε}[ ‖ε - ε_θ(√ᾱₜ x₀ + √(1-ᾱₜ)ε, t)‖² ]

  ← predict the added noise from the noisy sample at timestep t

Equivalent to minimizing a reweighted ELBO over the Markov chain.
In practice: uniform sampling of t ∈ {1,...,T}, single ε sample per x₀.
```

### Score Function Connection (Song & Ermon)

```
Score function of a distribution: s(x) = ∇_x log q(x)

For q(xₜ | x₀) = N(xₜ; √ᾱₜ x₀, (1-ᾱₜ)I):

  ∇_{xₜ} log q(xₜ | x₀) = -(xₜ - √ᾱₜ x₀) / (1-ᾱₜ) = -ε / √(1-ᾱₜ)

  ⟹  ε_θ(xₜ, t) ≈ -√(1-ᾱₜ) · s_θ(xₜ, t)

Learning ε_θ ≡ learning the score function s_θ of the noised distribution.
Score matching ↔ noise prediction: two views of the same objective.
```

### SDE Framework (Song et al. 2021)

```
Continuous-time generalization. Forward process:

  dx = f(x, t)dt + g(t)dW   ← SDE (stochastic differential equation)
                                f = drift, g = diffusion, W = Wiener process

Reverse SDE (Anderson 1982):

  dx = [f(x,t) - g(t)² ∇_x log p_t(x)] dt + g(t)dW̄

The reverse process has the same SDE form — requires the score s(x,t) = ∇_x log p_t(x).

Deterministic ODE version (probability flow ODE):
  dx = [f(x,t) - ½ g(t)² ∇_x log p_t(x)] dt
  Same marginals; faster sampling; enables exact likelihood computation.
```

### Sampling — DDIM and Beyond

```
DDPM sampling: T=1000 steps — slow (1 second per image on A100)

DDIM (Song et al. 2020): non-Markovian process, same training objective:
  Invert xₜ → x_{t-Δ} in larger steps → T=50 steps with same quality

DPM-Solver, PLMS: higher-order ODE solvers → T=10-20 steps

Consistency models: single-step distillation → T=1 step

Latent Diffusion (LDM / Stable Diffusion):
  Encode x₀ → z₀ via VAE encoder
  Run diffusion in latent space z (much smaller than pixel space)
  Decode z₀ → x̂₀ via VAE decoder
  → 4-8× cheaper than pixel diffusion; quality competitive
```

### Conditioning — Guidance

```
Classifier guidance (Dhariwal & Nichol 2021):
  Shift score toward high log p(y|x) (use separate classifier):
  s̃_θ(xₜ, t, y) = s_θ(xₜ, t) + γ ∇_{xₜ} log p_φ(y | xₜ)
  Guidance scale γ trades diversity for fidelity.

Classifier-free guidance (Ho & Salimans 2022):
  Train conditional and unconditional models jointly (null condition with prob p):
  s̃ = s_θ(xₜ, t, ∅) + γ (s_θ(xₜ, t, y) - s_θ(xₜ, t, ∅))
  No separate classifier needed.
  Used by: Stable Diffusion, DALL-E 3, Imagen — universal in practice.
```

### Connections to Other Generative Frameworks

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  Framework      │  Explicit density  │  Sampling     │  Training objective  │
├─────────────────┼────────────────────┼───────────────┼──────────────────────┤
│  VAE            │  Lower bound (ELBO)│  1 step       │  ELBO                │
│  Normalizing    │  Exact (change of  │  1 step       │  Exact NLL           │
│  Flows          │    variables)      │               │                      │
│  GAN            │  None (implicit)   │  1 step       │  Adversarial (unstable)│
│  Diffusion      │  Lower bound (ELBO)│  T steps      │  Noise prediction L₂ │
│  (DDPM)         │  exact via ODE     │  (10-1000)    │  (simple, stable)    │
└─────────────────┴────────────────────┴───────────────┴──────────────────────┘

Diffusion advantage: simple training objective (just MSE), stable, no mode collapse,
no adversarial game. Quality: best among all generative frameworks for images.
Cost: slow sampling (mitigated by DDIM/consistency models).
```

---

## 10. Decision Cheat Sheet

| Concept | Key result | Practical implication |
|---------|-----------|----------------------|
| UAT | ∃ shallow net for any f | Existence, not trainability |
| Depth separation | Depth exponentially more efficient | Don't use shallow wide nets |
| NTK | Infinite width → kernel regression | Wide nets are smoothly trainable |
| Lazy vs feature learning | Small init → feature learning | Use standard init, not huge init |
| BatchNorm | Smooths loss landscape | Use BN in CNNs; LN in transformers |
| Scaling laws | L ∝ N^{-α}, optimal N∝D | Chinchilla allocation for training |
| Double descent | Overparameterize + long train | Don't early-stop at the hump |
| Emergent abilities | Threshold capabilities | Expect qualitative jumps at scale |

---

## 11. Common Confusion Points

1. **"UAT means 1 hidden layer is enough"** — Theoretically yes, practically no. The required width can be exponential in the input dimension. Depth provides an exponential savings.

2. **"NTK explains why neural nets work"** — NTK explains the lazy training regime (large init, small step). Real neural nets in the feature learning regime behave very differently — they learn representations, which is why they beat fixed kernels.

3. **"BatchNorm prevents internal covariate shift"** — This was the original claim but is contested. The more reliable explanation is that BN smooths the loss landscape. Use LN for transformers.

4. **"Scaling laws mean more compute always helps"** — Power laws predict diminishing returns. Doubling compute gives a small percentage improvement. And real-world constraints (data quality, context length) create non-power-law failure modes.

5. **"Emergent abilities are fundamentally new"** — Possibly a measurement artifact. If you measure with a continuous metric (token probability), the improvement is smooth. Emergent behavior may arise from threshold-crossing in a continuous underlying curve.

6. **"Attention is always O(n²)"** — Standard attention is O(n²). Flash Attention is O(n²) in FLOPs but O(n) in HBM memory. Linear attention / Mamba (SSM) approximates attention with O(n) FLOPs. For n < 4K, standard attention with Flash is fast in practice.

7. **"Double descent means overfitting isn't real"** — Overfitting still exists. Double descent shows that in the overparameterized regime, further training / model growth eventually helps. It doesn't mean you can ignore regularization.
