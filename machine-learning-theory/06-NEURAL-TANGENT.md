# Neural Tangent Kernel and Infinite-Width Networks

## The Big Picture

The Neural Tangent Kernel (NTK, Jacot et al. 2018) characterizes the dynamics of gradient descent on infinitely wide neural networks. It reveals that training an infinite-width network is equivalent to kernel regression with a specific kernel — the NTK — that stays constant throughout training.

```
+──────────────────────────────────────────────────────────────────+
|              NEURAL TANGENT KERNEL FRAMEWORK                     |
|                                                                  |
|  SETUP                                                           |
|  Network f(x; θ) parameterized by θ ∈ ℝᴾ                       |
|  P = number of parameters (neurons × weights)                    |
|                                                                  |
|  NTK DEFINITION                                                  |
|  K^(t)(x, x') = ⟨∇_θ f(x; θᵗ), ∇_θ f(x'; θᵗ)⟩                |
|                                                                  |
|  INFINITE-WIDTH MIRACLE                                          |
|  As width → ∞:                                                   |
|  (1) NTK converges to a deterministic kernel K*                  |
|  (2) K^(t) stays constant during training: K^(t) = K* for all t  |
|  (3) Training = kernel regression with K*                        |
|                                                                  |
|  IMPLICATION: For sufficiently wide networks, training is        |
|  equivalent to kernel regression in a fixed RKHS.                |
+──────────────────────────────────────────────────────────────────+
```

---

## Gradient Descent as Kernel Regression

**Start with the continuous-time gradient flow** (infinitesimal learning rate):

```
GRADIENT FLOW DYNAMICS
────────────────────────
  dθ/dt = -∇_θ L(θ)   where  L(θ) = (1/2)||f(X;θ) - y||²

  df(X;θ)/dt = J(θ) · dθ/dt = -J(θ) · J(θ)ᵀ · (f(X;θ) - y)

where J(θ)ᵢⱼ = ∂f(xᵢ;θ)/∂θⱼ  is the Jacobian (m × P matrix)

DEFINE KERNEL MATRIX
  K(θ) = J(θ) · J(θ)ᵀ   (m × m matrix)
  K(θ)ᵢⱼ = ⟨∇_θ f(xᵢ;θ), ∇_θ f(xⱼ;θ)⟩  = NTK evaluated at (xᵢ,xⱼ)

DYNAMICS OF RESIDUALS
  d(f(X;θ) - y)/dt = -K(θ) · (f(X;θ) - y)

  If K(θ) is CONSTANT = K*:
    f(X;θᵗ) - y = e^{-K* t} · (f(X;θ⁰) - y)
    → Exponential convergence at rate = min eigenvalue of K*
    → At t→∞: f(X;θ∞) = y  (interpolates training data)
```

---

## Bridge: Random Matrix Theory → NTK Eigenvalue Spectrum

The NTK matrix K^(0) ∈ ℝ^{m×m} at initialization is a random matrix (a random feature kernel matrix). Its eigenvalue spectrum controls both convergence rate and generalization. Random matrix theory (RMT) is the natural framework:

```
MARCHENKO-PASTUR LAW
  For a random feature matrix Φ ∈ ℝ^{m×n} with iid entries (n = width),
  the empirical spectral distribution of (1/n)ΦΦᵀ converges as m,n → ∞
  with γ = m/n fixed to the Marchenko-Pastur distribution:

    ρ_MP(λ) = (1/2πγ) √((λ+ - λ)(λ - λ-)) / λ
    λ± = (1 ± √γ)²

  λ_min(K) ≈ (1 - √γ)² · σ²   (if γ < 1, i.e., n > m)
  If γ > 1 (m > n): K is rank-deficient; λ_min = 0.

NTK SPECTRUM AND TRAINING CONVERGENCE
  Convergence rate of gradient descent = λ_min(K^∞).
  For K^∞ determined by a PD kernel over m points:

  • If K^∞ has all eigenvalues bounded away from 0 (full rank, well-conditioned):
    linear convergence rate = λ_min(K^∞) > 0.

  • Condition number κ(K^∞) = λ_max/λ_min determines convergence speed:
    large κ → slow convergence (stiff system of ODEs).

  • For ReLU NTK on uniform sphere data:
    eigenvalues decay polynomially ~ j^{-d-1} where d = input dimension.
    λ_min → 0 as m grows relative to d — generalization degrades.

WIGNER SEMICIRCLE AND WEIGHT INITIALIZATION
  At initialization, weight matrices Wˡ have iid Gaussian entries.
  The singular value distribution of Wˡ follows the Marchenko-Pastur law.
  The signal propagation through layers (mean field theory) depends on:
    q¹(x,x') = E[(Wˡ·x)(Wˡ·x')] = σ²_w · ‖x‖² δ_{x=x'}
  Controlled by the weight variance σ²_w — the "edge of chaos" initialization
  (σ²_w = 2 for ReLU) corresponds to spectral radius ≈ 1, keeping gradients
  from vanishing or exploding.

FREE PROBABILITY (operator-valued generalization)
  For compositional models (deep networks), the spectral distribution of
  products of random matrices is analyzed via free convolution (Voiculescu):
    ρ_{AB} = ρ_A ⊞ ρ_B  (free convolution, not classical convolution)
  This is the correct tool for deep network spectra where layer widths vary.
```

The practical implication: NTK theory predicts that wider networks (more neurons → larger n relative to m) have better-conditioned K^∞, faster convergence, and better generalization. This aligns with empirical scaling laws. RMT quantifies exactly how the conditioning improves with width.

## Convergence of Infinite-Width Networks

```
WIDTH SCALING AND NTK
──────────────────────
Consider a fully connected network with L layers, width n:

  Layer ℓ: hᵗ⁺¹(x) = (1/√n) Wℓ · σ(hˡ(x)) + bˡ

  NTK at initialization (random Wˡ, bˡ):
    K^(0)(x, x') = E_θ[⟨∇_θ f(x;θ), ∇_θ f(x';θ)⟩]

  As n → ∞: K^(0) → K^∞ (deterministic limit)

  KEY THEOREM (Jacot, Gabriel, Hongler 2018)
  For n → ∞ (appropriately normalized):
  (1) At initialization: K^(0) converges in probability to K^∞
  (2) During training: K^(t) stays close to K^∞ for all t
  (3) Training dynamics are determined by K^∞ alone

  "The kernel does not change."
```

---

## The NTK Formula (Recursive)

The NTK can be computed analytically for fully-connected networks:

```
NTK RECURSION
──────────────
For a depth-L network with activation σ:

  K^∞(x, x') = Σᵢ₌₁ᴸ Θᵢ(x, x')

where the kernel decomposition involves:

  Σ⁰(x, x') = x·x'/d   (input correlation)

  Kᵢ(x, x') = E_{(u,v) ~ N(0, [Σⁱ⁻¹])}[σ(u)σ(v)]   (covariance kernel)

  Σᵢ(x, x') = E_{(u,v) ~ N(0, [Σⁱ⁻¹])}[σ(u)σ(v)]   (next layer kernel)

  Θᵢ(x, x') = K̃ᵢ(x, x') · E[σ'(u)σ'(v)]   (derivative contribution)

SPECIFIC CASE: ReLU activation
  Kᵢ can be computed in closed form via arc-cosine kernels:
    E[ReLU(u)ReLU(v)] = (1/2π)(sin θ + (π-θ)cos θ) ||u||||v||
  where θ = arccos(u·v/(||u||||v||))
```

---

## NTK and Lazy Training

```
LAZY TRAINING REGIME
─────────────────────
When width n → ∞ (or learning rate small), parameters barely move:

  ||θᵗ - θ⁰||₂ → 0 as n → ∞ (for fixed t)

  "Lazy" because parameters stay near initialization.
  Network behaves as a linearized model around θ⁰:

    f(x; θ) ≈ f(x; θ⁰) + ⟨∇_θ f(x; θ⁰), θ - θ⁰⟩

  This linearized model = kernel regression with NTK.

CONTRAST WITH FEATURE LEARNING
  Finite-width networks: θ moves significantly during training.
  Features (internal representations) evolve.
  This is the "feature learning" regime — where neural nets
  outperform kernel methods in practice.

  NTK regime:  parameters barely move → no feature learning
  Feature learning regime:  parameters move → representations improve

  The gap between NTK theory and practical neural nets
  = the gap between kernel regression and feature learning.
```

---

## What the NTK Predicts

```
NTK PREDICTIONS
────────────────
Under NTK regime (infinite width, small learning rate):

(1) GLOBAL CONVERGENCE
    Gradient descent converges to global minimum (not just local)
    because optimization is linear (kernel regression).

(2) GENERALIZATION
    Generalization = RKHS generalization with kernel K^∞.
    Rademacher complexity of H_{K^∞} bounds the gap.

(3) ARCHITECTURE ENCODES INDUCTIVE BIAS
    K^∞ depends on network architecture.
    Convolutional nets → translation-equivariant K^∞
    Recurrent nets → sequential structure in K^∞
    The NTK captures architectural inductive bias precisely.

(4) INTERPOLATION
    At t → ∞, network interpolates training data exactly.
    Generalization depends on smoothness of K^∞.
```

---

## Limitations of the NTK

```
WHERE NTK FAILS TO DESCRIBE PRACTICE
──────────────────────────────────────

(1) NTK REGIME ≠ PRACTICAL REGIME
    Real networks have finite width.
    In practice, learning rate is not infinitesimal.
    Parameters move far from initialization.
    Feature learning happens — representations improve.

(2) NTK BOUNDS STILL VACUOUS
    Even with kernel theory, for m = 10⁶, d = 10⁸ parameters:
    RKHS bound ~ √(tr(K)/m) is not small enough.

(3) NTK DOESN'T EXPLAIN NEURAL NET SUPERIORITY
    Practical nets outperform kernel regression with NTK.
    This means feature learning (beyond NTK) is responsible.
    NTK describes what happens — but not why nets beat kernels.

(4) PHASE TRANSITIONS
    Practical nets exhibit phase transitions (grokking, double descent)
    not predicted by NTK (kernel regression has no phase transitions).

MEAN FIELD THEORY: alternative approach for large but finite width
  Parameters move, kernels evolve, representations are learned.
  Harder to analyze but closer to practice.
```

---

## Finite-Width Corrections

```
1/n CORRECTIONS TO NTK
────────────────────────
For width n < ∞, the NTK evolves during training:

  K^(t) = K^∞ + (1/n) · δK^(t) + O(1/n²)

The correction δK^(t) captures feature learning at leading order.

MEAN FIELD LIMIT (different from NTK)
  Instead of n → ∞ with fixed initialization variance:
  Consider particles (neurons) evolving in weight space.
  The measure over neurons evolves via Wasserstein gradient flow.
  Feature learning is represented as distribution over neurons shifting.

  This gives a separate theory closer to practical training.

**Mean field theory: Wasserstein gradient flow perspective (Mei, Montanari, Nguyen 2018).** In the mean field limit, treat each neuron as a particle with weight vector θᵢ ∈ ℝᵈ. The network is a weighted sum f(x; μ) = ∫ h(x, θ) dμ(θ) where μ is a probability measure over weight space. Training minimizes a functional F[μ] = R(μ) + λ·Ω(μ) over the space of measures (the Wasserstein space W₂). The gradient flow in W₂ is:

```
  ∂μ/∂t = div(μ · ∇_θ (δF/δμ))

  — the continuity equation of the measure μ evolving under velocity field ∇_θ (δF/δμ).
  — This is a PDE on the space of probability measures.
  — Neurons evolve as interacting particles driven by the functional gradient.
```

Unlike the NTK (where parameters barely move), mean field theory allows the measure μ to change significantly — neurons cluster, split, and rearrange. Feature learning is captured as the measure μ concentrating on neurons that represent task-relevant features. The NTK and mean field regimes are distinct infinite-width limits depending on the parameterization (NTK parameterization vs mean field / μP parameterization).
```

---

## Connections to Other Theory

```
NTK ←→ KERNEL RIDGE REGRESSION
  NTK training = kernel ridge with K^∞ + Tikhonov regularization
  Implicit regularization from stopping early → λ depends on t

NTK ←→ GAUSSIAN PROCESSES
  Random neural net at initialization = Gaussian process
  with covariance kernel = NNGP kernel (related to NTK)
  Training neural net with squared loss = GP posterior inference
  (in the NTK/infinite-width limit)

**NNGP vs NTK: two kernels, two views of the infinite-width network.** The NNGP kernel K_NNGP(x, x') = E_θ[f(x;θ) f(x';θ)] is the covariance of the random function at initialization — the prior in GP regression. The NTK kernel K_NTK(x, x') = E_θ[⟨∇_θ f(x;θ), ∇_θ f(x';θ)⟩] captures how the function changes during training. Recursively:

```
  K_NNGP(x, x') = Σᵣ₌₀ᴸ K̃ᵣ(x, x')       (sum of layer-wise covariance kernels)

  K_NTK(x, x')  = Σᵣ₌₀ᴸ K̃ᵣ(x, x') · Σᵣ'≥ᵣ Σ̃ᵣ'(x, x')   (includes derivative contributions)

  Schematically: K_NTK = K_NNGP + (derivative / backpropagation terms)
```

Training the network with MSE loss corresponds to GP posterior inference with kernel K_NTK (not K_NNGP). The random network at initialization is a GP with kernel K_NNGP. The trained network (in the NTK limit) is a GP posterior with kernel K_NTK and likelihood determined by the training data. These are different — and for deep networks, K_NTK has richer structure due to the depth-dependent derivative terms.

NTK ←→ DOUBLE DESCENT
  In NTK regime, the interpolating solution is unique (kernel is PD)
  → minimum-norm interpolant in RKHS
  → benign overfitting under certain conditions (Module 07)

NTK ←→ MEAN FIELD
  NTK: width → ∞, parameters nearly frozen  [lazy training]
  Mean field: width → ∞, particles evolve   [active training]
  These are different infinite-width limits depending on scaling.
```

---

## Decision Cheat Sheet

| Question | NTK Answer |
|----------|-----------|
| Does gradient descent converge globally? | Yes, for infinite-width networks |
| What does the network compute at convergence? | Kernel regression with K^∞ |
| Does the kernel change during training? | No (infinite-width); yes (finite) |
| Why do real networks beat kernel methods? | Feature learning — beyond NTK regime |
| How to compute NTK for a given architecture? | Recursive formula; closed form for fully-connected + ReLU |
| Is NTK useful for finite networks? | As a first-order approximation, yes; fails to capture feature learning |
| What is the effective prior in NTK regression? | RKHS with K^∞ norm — encodes architectural inductive bias |

---

## Common Confusion Points

**"If training is just kernel regression, why bother with neural nets?"**
Kernel regression with NTK is what happens at infinite width with lazy training. Finite-width networks in practice operate in the feature-learning regime, where they learn better representations than any fixed kernel can provide. The NTK limit is a useful theoretical tool, not a description of what makes neural nets powerful.

**"NTK says kernel doesn't change — but I've seen papers showing it does change"**
The NTK is constant in the strict infinite-width limit. For finite but large width, it changes by O(1/n). In practice (small width), the kernel changes substantially, especially for early layers. The NTK theorem has a proviso: "as width → ∞." Real networks are always finite-width.

**"Why does the NTK depend on the architecture?"**
Because the NTK is defined as ⟨∇_θ f(x), ∇_θ f(x')⟩, and the gradient depends on the functional form of the network. Different architectures (convnets, transformers, RNNs) produce different gradients → different NTKs → different inductive biases. This is a formal way to say "architecture matters."

**"NTK regime vs lazy training — are they the same?"**
Yes, under appropriate scaling. When the learning rate is O(1/P) (where P = number of parameters) or when width → ∞, parameters move by O(1/√n) → "lazy." This is the NTK regime. When learning rate is larger or width is finite, parameters move significantly — feature learning regime. The NTK paper defines a specific parameterization that guarantees the lazy/NTK regime.
