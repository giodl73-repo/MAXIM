# Probabilistic Machine Learning
## Uncertainty as a First-Class Citizen

```
THE PROBABILISTIC FRAMING

  Frequentist:   θ is fixed, unknown. Data is random. Estimate θ̂ from data.
  Bayesian:      θ is random. Encode prior belief p(θ). Update with data via Bayes.

  p(θ | D) = p(D | θ) · p(θ) / p(D)
                ↑           ↑         ↑
            likelihood    prior   evidence (normalizer)

  Posterior p(θ|D) is the full answer — not a point estimate, a distribution.
```

---

## 1. Bayesian Inference — Core Mechanics

**The four quantities**:
```
  p(θ)       prior       — belief about θ before seeing data
  p(D | θ)   likelihood  — probability of data given parameter
  p(θ | D)   posterior   — updated belief after data
  p(D)       evidence    — marginal likelihood = ∫ p(D|θ)p(θ)dθ
```

**Posterior predictive**: for a new point x*:
```
p(y* | x*, D) = ∫ p(y* | x*, θ) p(θ | D) dθ
```
This is the Bayesian prediction — marginalize over all θ weighted by posterior. Not a single model's prediction, but an average over a distribution of models.

**Maximum A Posteriori (MAP)**:
```
θ_MAP = argmax p(θ | D) = argmax [ log p(D|θ) + log p(θ) ]
                                        ↑              ↑
                                  log-likelihood    log-prior

  Gaussian prior p(θ) = N(0, σ²I)  →  log p(θ) = -‖θ‖²/2σ²  →  L2 regularization
  Laplace prior  p(θ) ∝ exp(-λ‖θ‖₁) →  L1 regularization
```

MAP is the bridge between Bayesian inference and regularized optimization.

---

## 2. Conjugate Priors

When posterior has the same distributional form as the prior, computation is closed-form.

| Likelihood | Conjugate prior | Posterior |
|-----------|----------------|-----------|
| Bernoulli(θ) | Beta(α, β) | Beta(α + #heads, β + #tails) |
| Categorical(θ) | Dirichlet(α) | Dirichlet(α + counts) |
| Normal(μ, σ²) known σ² | Normal(μ₀, τ²) | Normal (closed form) |
| Normal(μ, σ²) known μ | Inverse-Gamma(a, b) | Inverse-Gamma(a + n/2, ...) |
| Poisson(λ) | Gamma(α, β) | Gamma(α + Σxᵢ, β + n) |

**Why conjugates matter**: closed-form posterior → no MCMC or VI needed. Bayesian naive Bayes, Dirichlet-Multinomial for topic models, and Gaussian processes all exploit conjugacy.

---

## 3. Graphical Models

Graphical models encode conditional independence structure. The graph is the model.

### Directed Graphical Models (Bayesian Networks)

```
  Nodes = random variables
  Directed edges = direct probabilistic influence

  Example: naive Bayes

    [Class C]
    /   |   \
   v    v    v
  [X₁] [X₂] [X₃]       p(C, X₁, X₂, X₃) = p(C) p(X₁|C) p(X₂|C) p(X₃|C)

  Each node conditioned on its parents. Joint = product of conditionals.
```

**d-separation** (directed separation): the graphical criterion for conditional independence. Three fundamental patterns:
```
  Chain:   A → B → C      A ⊥ C | B   (B blocks)
  Fork:    A ← B → C      A ⊥ C | B   (B blocks)
  Collider: A → B ← C     A ⊥ C       (B unblocks when conditioned on!)
```

Collider (v-structure) is counterintuitive — conditioning on a common effect introduces dependence between causes. This is **Berkson's paradox** in epidemiology.

### Undirected Graphical Models (Markov Random Fields)

```
  No edge between X and Y  →  X ⊥ Y | all other nodes

  Joint: p(x) = (1/Z) Π_c ψ_c(x_c)    where ψ_c are potential functions
                  ↑
           partition function — intractable in general
```

Used in image segmentation (MRF priors), Ising models, CRFs for sequence labeling.

---

## 4. Exact Inference — Belief Propagation

For tree-structured graphs, belief propagation computes exact marginals in O(n · |states|²).

**Sum-product algorithm** on a factor graph:
```
  Messages from variable to factor:
    μ_{x→f}(x) = Π_{g ∈ ne(x)\f} μ_{g→x}(x)

  Messages from factor to variable:
    μ_{f→x}(x) = Σ_{x_f\x} [ f(x_f) Π_{y ∈ ne(f)\x} μ_{y→f}(y) ]

  Marginal: p(x) ∝ Π_{f ∈ ne(x)} μ_{f→x}(x)
```

For graphs with cycles: loopy belief propagation (not exact, but often works). Junction tree algorithm: exact inference on general graphs via chordalization — exponential in treewidth.

---

## 5. MCMC — Approximate Posterior Sampling

When the posterior has no closed form (most interesting cases), approximate it by drawing samples.

### Metropolis-Hastings

```
  Given current state θ_t, propose θ' ~ q(θ' | θ_t)

  Accept with probability:
    α = min(1, p(θ'|D) q(θ_t|θ') / p(θ_t|D) q(θ'|θ_t))

  If q is symmetric: α = min(1, p(θ'|D) / p(θ_t|D))  ← Metropolis

  Result: Markov chain with stationary distribution = target posterior
```

**Gibbs sampling**: special case where you sample each variable conditioned on all others. Accept probability = 1. Requires tractable conditionals.

**Hamiltonian Monte Carlo (HMC)**:
```
  Augment θ with momentum r. Define Hamiltonian:
    H(θ, r) = -log p(θ|D) + ½ r^T M^{-1} r
                   ↑ potential         ↑ kinetic

  Simulate Hamiltonian dynamics (leapfrog integrator) to propose distant θ'
  that are accepted with high probability.

  NUTS (No-U-Turn Sampler): automated HMC — PyMC, Stan, NumPyro
```

HMC dramatically reduces autocorrelation compared to random-walk MH. The gold standard for Bayesian inference in practice.

**Diagnostics**:
- R̂ (Gelman-Rubin): convergence of multiple chains, want R̂ < 1.01
- Effective sample size (ESS): number of independent equivalent samples
- Trace plots: should look like "hairy caterpillars" — good mixing

---

## 6. Variational Inference

Rather than sampling from the posterior, approximate it with a tractable distribution.

**Setup**:
```
  True posterior: p(θ | D)   ← intractable

  Approximate with: q(θ; φ) from a tractable family Q (e.g., mean-field Gaussians)

  Objective: minimize KL(q ‖ p(θ|D)) over φ

  KL(q ‖ p) = E_q[log q(θ)] - E_q[log p(θ|D)]
             = E_q[log q(θ)] - E_q[log p(D,θ)] + log p(D)
             ≥ 0

  Since KL ≥ 0:  log p(D) ≥ E_q[log p(D,θ)] - E_q[log q(θ)]
                                     ↑
                              ELBO (Evidence Lower BOund)

  Maximizing ELBO  ≡  minimizing KL(q ‖ p(·|D))
```

**ELBO decomposition**:
```
ELBO(q) = E_q[log p(D|θ)] - KL(q(θ) ‖ p(θ))
               ↑                    ↑
          expected likelihood    regularization: keep q near prior
```

**Mean-field approximation**: assume q(θ) = Π_i q_i(θ_i) — fully factored posterior. Exact in some exponential family cases. Underestimates posterior variance (mode-seeking behavior of KL(q‖p)).

**Black-box VI**: reparameterization trick enables gradient-based optimization:
```
  θ = g(ε; φ),  ε ~ p(ε)     (reparameterize sampling step)

  ∇_φ E_q[f(θ)] = E_{p(ε)}[∇_φ f(g(ε;φ))]   ← differentiable through sampling
```

This is the foundation of VAEs.

---

## 7. Variational Autoencoders (VAE)

The VAE is variational inference with neural network amortization.

```
  Generative model:   z ~ p(z) = N(0,I),  x|z ~ p_θ(x|z) = N(f_θ(z), σ²I)
  Inference model:    q_φ(z|x) = N(μ_φ(x), diag(σ²_φ(x)))   ← encoder

  ┌──────────────────────────────────────────────┐
  │  x  →  [Encoder q_φ]  →  μ,σ  →  z  →  [Decoder p_θ]  →  x̂  │
  │                              ↑                                  │
  │                    reparameterize: z = μ + σ⊙ε, ε~N(0,I)      │
  └──────────────────────────────────────────────┘

  ELBO = E_{q_φ(z|x)}[log p_θ(x|z)] - KL(q_φ(z|x) ‖ p(z))
              ↑ reconstruction loss           ↑ KL regularization (closed form for Gaussians)
```

**KL closed form** (Gaussian encoder, standard normal prior):
```
KL(N(μ,σ²) ‖ N(0,1)) = ½ Σ_j (μ_j² + σ_j² - log σ_j² - 1)
```

**Why VAE isn't just an AE**: the KL term forces a structured latent space. Without it, the encoder collapses to deterministic and you get a standard autoencoder.

**Known limitations**:
- Blurry reconstructions (mean of decoder distribution)
- Posterior collapse in language VAEs
- Mode-seeking KL(q‖p) underestimates variance

---

## 8. Normalizing Flows

Transform a simple base distribution (Gaussian) into a complex target distribution via a chain of invertible differentiable maps.

```
  z₀ ~ p₀(z) = N(0,I)

  x = f_K ∘ f_{K-1} ∘ ... ∘ f_1(z₀)

  Change of variables:
    log p(x) = log p₀(z₀) - Σ_{k=1}^K log |det J_{f_k}(z_{k-1})|
                                                   ↑
                                         Jacobian determinant of each transform
```

**Requirement**: each f_k must be
1. Invertible (to sample: z → x; to evaluate density: x → z)
2. Have tractable Jacobian determinant

**Architectures**:
```
  RealNVP (affine coupling layers):
    Split x into (x_A, x_B)
    y_A = x_A,  y_B = x_B ⊙ exp(s(x_A)) + t(x_A)
    Triangular Jacobian → det = exp(Σ s(x_A))  ← cheap

  Autoregressive flows (MAF/IAF):
    x_i = f(x_{<i}; θ)
    Triangular Jacobian → det is product of diagonal

  Neural ODE / Continuous NF:
    dx/dt = f_θ(x, t)   ← flow defined by ODE
    log p via instantaneous change of variables
```

**VAE vs Flow vs GAN**:
```
  VAE:   tractable lower bound, approximate posterior, latent space
  Flow:  exact likelihood, no latent compression, memory-intensive
  GAN:   no likelihood, just samples, implicit density, mode collapse risk
  Diff:  denoising diffusion — score matching, iterative refinement, SOTA quality
```

---

## 9. Gaussian Processes

A distribution over functions. The infinite-dimensional generalization of the multivariate Gaussian.

```
  f ~ GP(m, k)   means:

  For any finite set of inputs X = {x_1,...,x_n}:
    f(X) ~ N(m(X), K(X,X))

  where K_ij = k(x_i, x_j)  ← kernel / covariance function
```

**Posterior GP** (regression, noise σ²):
```
  Given y = f(X) + ε, ε ~ N(0, σ²I):

  f* | X, y, X* ~ N(μ*, Σ*)

  μ* = K(X*,X) [K(X,X) + σ²I]^{-1} y
  Σ* = K(X*,X*) - K(X*,X) [K(X,X) + σ²I]^{-1} K(X,X*)
```

Exact inference: O(n³) in training size — bottleneck for large datasets. Sparse GPs, inducing points (SVGP) bring this to O(nm²) where m ≪ n.

**Kernels encode inductive bias**:
| Kernel | Inductive bias |
|--------|---------------|
| RBF / SE | Smooth, infinitely differentiable |
| Matérn 3/2 | Once differentiable |
| Matérn 1/2 | Continuous but not differentiable |
| Periodic | Exactly periodic |
| Linear | Linear functions |
| Deep kernel (DKL) | Learned feature + GP |

---

## 10. Decision Cheat Sheet

| Method | When to use | Tractable? | Gives samples? |
|--------|------------|-----------|----------------|
| Conjugate Bayes | Simple likelihood + matching prior | ✅ Exact | ✅ |
| MAP | Point estimate, large scale | ✅ Optimization | ❌ |
| MCMC (HMC/NUTS) | Gold standard, moderate dim | Slow | ✅ |
| Mean-field VI | Large scale, approximate OK | ✅ Fast | ✅ |
| VAE | Generative model with latent structure | ✅ + neural | ✅ |
| Normalizing flow | Exact density needed | ✅ + neural | ✅ |
| GP | Small-medium data, uncertainty needed, Bayesian opt | O(n³) exact | ✅ |
| Diffusion | High-quality generation | Training cost | ✅ |

---

## 11. Where This Surfaces in Practice

```
  MAP ↔ regularized loss minimization (L2 = Gaussian prior, L1 = Laplace)
  VI / ELBO ↔ VAE training objective in PyTorch
  NUTS/HMC ↔ PyMC, Stan, NumPyro for Bayesian models
  GP ↔ GPyTorch, scikit-learn GaussianProcessRegressor
  Bayesian optimization ↔ Ax, BoTorch (GP posterior → acquisition function)
  Normalizing flows ↔ nflows, zuko, PyTorch distributions transforms

  LLM connection:
    RLHF reward model → Bayesian update on human preferences
    KL penalty in PPO → keep policy near prior (reference model)
    Uncertainty in generation → temperature, beam search as VI approximations
```

---

## 12. Common Confusion Points

1. **"Bayesian = better"** — Bayesian inference gives calibrated uncertainty only if the prior is right. A misspecified prior can be worse than a well-tuned point estimate.

2. **"ELBO maximization = exact posterior"** — ELBO is a lower bound. The gap `KL(q‖p)` can be large, especially in high dimensions. The posterior approximation quality depends on the variational family.

3. **"VAE is a better autoencoder"** — VAE is a generative model. Its reconstruction quality trades off against the KL regularization. For compression/representation, a deterministic AE often wins.

4. **"MCMC always converges"** — MCMC converges to the stationary distribution asymptotically. With finite samples, you have a sample from a distribution that might still be far from the posterior (poor mixing, multimodality).

5. **"KL(q‖p) vs KL(p‖q)"** — Direction matters. KL(q‖p) (used in VI) is mode-seeking — q concentrates on one mode, ignores others. KL(p‖q) is mean-seeking — used in expectation propagation, handles multimodality better but is harder to optimize.

6. **"Normalizing flows = exact posterior"** — Flows give exact likelihood under the flow model, but the model itself is an approximation. The flow doesn't find the true posterior; it finds the closest distribution in the flow family.

7. **"GPs don't scale"** — Sparse GPs (inducing points, SVGP) + GPU implementations (GPyTorch) scale to millions of points. Deep kernel learning combines neural feature learning with GP uncertainty.
