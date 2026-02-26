# Optimization Theory for Machine Learning
## From Convex Analysis to SGD, Adam, and Non-Convex Deep Learning

```
THE OPTIMIZATION LANDSCAPE

  Convex region                     Non-convex region (deep learning)
  ┌──────────────────┐              ┌──────────────────────────────────┐
  │  Global min = local min         │  Many local minima, saddle points │
  │  GD converges (with LR tuning)  │  SGD finds flat minima           │
  │  Strong theory, guarantees      │  Theory: NTK, loss landscape      │
  │  Logistic regression, SVM, LR   │  Neural networks                  │
  └──────────────────┘              └──────────────────────────────────┘

  Key parameters:
    L = Lipschitz constant of gradient  (L-smooth)
    μ = strong convexity constant       (μ-strongly convex)
    κ = L/μ = condition number          (determines convergence rate)
```

---

## Numerical Analysis / Operations Research Bridge

The condition number κ and convergence machinery here are identical to classical
numerical linear algebra and operations research — just in a new setting:

```
Numerical linear algebra / OR                  Optimization theory (this file)
────────────────────────────────────────────   ──────────────────────────────────────────
Condition number κ(A) = ‖A‖·‖A⁻¹‖             Condition number κ = L/μ
  → determines round-off amplification in        → same ratio: L = largest curvature
    Gaussian elimination                              μ = smallest curvature
  → determines convergence rate of CG on Ax=b  → ill-conditioned loss ↔ elongated ellipse
  → well-conditioned (κ≈1): fast, stable        → CG on Ax=b converges in O(√κ) iterations
  → ill-conditioned (κ≫1): slow, numerically       same rate as Nesterov GD: O(1/T²)
    fragile

Conjugate gradient (Ax=b):                    Nesterov accelerated gradient:
  Converges in O(√κ) iterations                Converges in O(1/√κ) per step
  Optimal for quadratic objectives             Optimal for smooth convex objectives
  Uses Krylov subspace Span{r₀,...,r_{t-1}}   Uses "lookahead" momentum
  → Both achieve the same √κ improvement       Both are lower bound-achieving

Preconditioning Ax=b → P⁻¹Ax = P⁻¹b:         Adaptive gradient methods (Adam, Adagrad):
  Choose P to make κ(P⁻¹A) ≈ 1                 Approximate diagonal preconditioning
  → same number of CG iterations as            → per-parameter LR ≈ 1/√accumulated_grad²
    perfectly conditioned system               K-FAC: full Kronecker-factored preconditioner

Quasi-Newton (Nocedal & Wright, "Numerical     L-BFGS:
  Optimization"):                               Same algorithm — same textbook
  BFGS: O(d²) memory, superlinear convergence  L-BFGS: O(md) memory via limited history
  L-BFGS: limited-memory variant               Standard in scipy.optimize.minimize

Trust region methods (OR):                     SAM (Sharpness-Aware Minimization):
  Constrain step to ball ‖δ‖ ≤ Δ               Maximize loss in ε-ball, then step
  → solve subproblem, update trust radius      → same geometry: local worst-case over
  Used in SQP, TRPO (RL)                         a norm ball

Linear programming duality (OR):              Convex duality (Lagrangian):
  Primal/dual gap → KKT conditions             Strong duality for convex problems
  → same theory, same conditions               SVMs are LP duals in disguise

Simplex (OR, linear programs):                 Coordinate descent (LASSO, GLMs):
  Move along vertex of feasible polytope        Move along one coordinate at a time
  → both exploit sparse structure              → both effective when coordinates
  → both convergence guarantees known            are (approximately) uncorrelated
```

The core insight: **machine learning optimization is numerical optimization on
high-dimensional, stochastic, non-convex objectives**. Every concept in this guide
has a numerical analysis or OR ancestor — the theory is the same, the scale and
the stochasticity are new.

---

## 1. Convex Analysis — The Foundations

**Convex set**: C is convex if ∀ x,y ∈ C, λ ∈ [0,1]: λx + (1-λ)y ∈ C

**Convex function**: f is convex if:
```
f(λx + (1-λ)y) ≤ λf(x) + (1-λ)f(y)   ∀ x,y, λ ∈ [0,1]

Equivalently (first-order):  f(y) ≥ f(x) + ∇f(x)ᵀ(y-x)
  ← tangent plane is a global lower bound

Equivalently (second-order): ∇²f(x) ≽ 0  (PSD Hessian)
```

**L-smoothness** (Lipschitz gradient):
```
‖∇f(x) - ∇f(y)‖ ≤ L‖x-y‖   ∀ x,y

Equivalently: f(y) ≤ f(x) + ∇f(x)ᵀ(y-x) + (L/2)‖y-x‖²
← gradient is the upper bound, L is the curvature cap
```

**μ-strong convexity**:
```
f(y) ≥ f(x) + ∇f(x)ᵀ(y-x) + (μ/2)‖y-x‖²   μ > 0

← tangent plane + quadratic lower bound
← unique global minimum
← eigenvalues of Hessian ≥ μ everywhere
```

**Condition number κ = L/μ**: measures how "elliptic" the level sets are. High κ = elongated = slow convergence.

---

## 2. Gradient Descent Convergence

**Update rule**: `x_{t+1} = x_t - α∇f(x_t)`, step size α.

### Convex + L-smooth
```
f(x_T) - f(x*) ≤ L‖x_0 - x*‖² / (2T)   with α = 1/L

O(1/T) convergence rate — sublinear
```

**Proof sketch**: by L-smoothness, `f(x_{t+1}) ≤ f(x_t) - (1/2L)‖∇f(x_t)‖²`. Sum over T steps, use convexity to relate gradient norm to suboptimality.

### μ-strongly convex + L-smooth
```
‖x_T - x*‖² ≤ (1 - μ/L)^T ‖x_0 - x*‖²   with α = 1/L

Linear (geometric) convergence — exponential improvement
Rate: (1 - 1/κ) per step, κ = L/μ
T = O(κ log(1/ε)) steps for ε-accuracy
```

**Why condition number matters**:
```
  κ = 1   (perfectly conditioned): converge in 1 step
  κ = 10:  ~10 steps
  κ = 1000: ~1000 steps  ← typical in poorly scaled ML problems

  Preconditioning: transform problem so effective κ ≈ 1
```

### Convergence comparison
| Method | Convex | Strongly convex |
|--------|--------|----------------|
| GD | O(1/T) | O((1-1/κ)^T) |
| Nesterov accelerated | O(1/T²) | O((1-1/√κ)^T) |
| Newton's method | O(log log 1/ε) | quadratic (local) |
| Conjugate gradient | — | O((1-1/√κ)^T) + exact for quadratics |

---

## 3. SGD — Stochastic Gradient Descent

**Motivation**: for ERM, `∇f(x) = (1/n) Σ ∇fᵢ(x)` is expensive when n is huge.

**SGD**: sample one (or mini-batch) index i uniformly at random:
```
x_{t+1} = x_t - αₜ ∇fᵢ(x_t)

Unbiased: E[∇fᵢ(x)] = ∇f(x)
Noise: variance σ² = E[‖∇fᵢ(x) - ∇f(x)‖²]
```

**Convergence** (convex, diminishing LR αₜ = α/√t):
```
E[f(x̄_T) - f*] ≤ O( (L·‖x_0-x*‖² + σ²) / √T )

where x̄_T = (1/T) Σ x_t  (averaged iterate)
```

**SGD converges to a neighborhood**, not the exact minimum (fixed step size). Vanishing step size → exact minimum but slower.

**Mini-batch trade-off**:
```
  Batch size B:
    Variance reduced by B: σ²_batch = σ²/B
    But each step costs B gradient evaluations

  Optimal batch size: B* ≈ σ²/‖∇f‖²  (noise ≈ signal)
  Beyond B*, adding more samples gives diminishing returns per compute unit
```

**Why noise helps** (implicit regularization):
- SGD noise prevents convergence to sharp minima
- Sharp minima: high curvature, poor generalization
- Flat minima: low curvature, better generalization (PAC-Bayes perspective)
- This is the intuition behind batch size effects: smaller batch → more noise → flatter basin

---

## 4. Momentum Methods

### Heavy Ball (Polyak)
```
  v_{t+1} = β v_t - α ∇f(x_t)
  x_{t+1} = x_t + v_{t+1}

  Physical analogy: ball rolling in bowl, momentum accumulates in consistent directions,
  cancels in oscillating directions.
```

### Nesterov Accelerated Gradient (NAG)
```
  y_{t+1} = x_t + β(x_t - x_{t-1})           ← lookahead step
  x_{t+1} = y_{t+1} - α ∇f(y_{t+1})          ← gradient at lookahead

  Rate: O(1/T²) for convex, O((1-1/√κ)^T) for strongly convex
  Optimal for first-order methods — matches lower bound (Nesterov 1983)
```

**Why NAG is optimal**: gradient at the lookahead point y is "more informative" than gradient at current x. Information-theoretic lower bound for first-order convex optimization: Ω(1/T²). NAG achieves it.

---

## 5. Adaptive Learning Rate Methods

**Motivation**: different parameters have different gradient scales. A single global LR is suboptimal.

### AdaGrad
```
  G_t = Σ_{s=1}^t g_s g_sᵀ   (sum of outer products, diagonal approximation: G_t = Σ g_s²)
  x_{t+1} = x_t - α · g_t / √(G_t + ε)

  Effective LR per parameter: α / √(accumulated squared gradients)
  Sparse features: rarely updated → small G → large effective LR → catches up
  Problem: G_t grows monotonically → LR → 0, training stops
```

### RMSProp
```
  v_t = ρ v_{t-1} + (1-ρ) g_t²    ← exponential moving average of squared grad
  x_{t+1} = x_t - α · g_t / √(v_t + ε)

  Fixes AdaGrad's dying LR by using EMA instead of sum
```

### Adam (Kingma & Ba, 2014)
```
  m_t = β₁ m_{t-1} + (1-β₁) g_t          ← 1st moment (momentum)
  v_t = β₂ v_{t-1} + (1-β₂) g_t²         ← 2nd moment (uncentered variance)

  Bias correction (crucial at start when m₀=v₀=0):
    m̂_t = m_t / (1 - β₁ᵗ)
    v̂_t = v_t / (1 - β₂ᵗ)

  x_{t+1} = x_t - α · m̂_t / (√v̂_t + ε)

  Default hyperparameters: β₁=0.9, β₂=0.999, ε=1e-8, α=1e-3
```

**Why bias correction matters**: at t=1, without correction m̂_1 = g_1 (full signal). With correction m̂_1 = (1-β₁)g_1/(1-β₁) = g_1. At t=1000, correction factor ≈ 1 — EMA has warmed up.

**AdamW**: decoupled weight decay. Original Adam: `x += -α(m̂/√v̂) - α·λ·x`. AdamW: `x = (1-λ)x - α(m̂/√v̂)`. The difference: in Adam, weight decay is adapted; in AdamW, it's not. AdamW is preferred for transformers.

**Adam vs SGD**: Adam converges faster, SGD (with tuned schedule) often generalizes better. In practice: use Adam for transformers/LLMs; SGD+momentum for vision (ResNet, etc.).

---

## 6. Second-Order Methods

**Newton's method**:
```
  x_{t+1} = x_t - [∇²f(x_t)]^{-1} ∇f(x_t)

  Quadratic convergence (near optimum): ‖x_{t+1} - x*‖ ≤ C‖x_t - x*‖²
  Each step: O(d³) for Hessian inversion — infeasible for large neural nets
```

**Quasi-Newton (L-BFGS)**:
```
  Approximate H^{-1} using curvature from recent (s_k, y_k) pairs:
    s_k = x_{k+1} - x_k,  y_k = ∇f(x_{k+1}) - ∇f(x_k)

  Limited memory: keep last m=10-20 pairs → O(md) memory
  Used for: small-scale ML, fine-tuning, scientific computing
  Not used for: stochastic settings (gradient noise breaks curvature estimates)
```

**Shampoo / K-FAC**: approximate full-matrix preconditioning for neural nets. Kronecker-factored Hessian approximation. Effective in practice but expensive. Used in large-scale training at Google.

---

## 7. Learning Rate Schedules

```
  Constant LR:         α_t = α                    ← simple, needs tuning
  Step decay:          α_t = α · γ^{floor(t/T)}   ← discrete drops
  Cosine annealing:    α_t = α_min + ½(α_max-α_min)(1 + cos(πt/T))
  Cosine with warmup:  linear warmup for W steps, then cosine
  1-cycle:             warmup + decay in 1 cycle (Smith, superconvergence)
  Warmup (transformers): α_t = d_model^{-0.5} · min(t^{-0.5}, t · warmup^{-1.5})
```

**Why warmup matters for Adam**: at initialization, gradient estimates are noisy; the second moment v_t hasn't stabilized. Warmup gives Adam time to calibrate adaptive LR before taking large steps.

---

## 8. Loss Landscape in Deep Learning

### Saddle Points vs Local Minima
```
  Classical fear: gradient descent gets stuck in local minima
  Modern understanding: in high dimensions, local minima are rare

  At a critical point ∇f(x*) = 0:
    If Hessian has all positive eigenvalues → local minimum
    If Hessian has all negative eigenvalues → local maximum
    If Hessian has mixed signs → saddle point

  Random matrix theory: for large networks, saddle points dominate.
  Probability of all eigenvalues positive → 0 exponentially in depth/width.

  GD escapes saddle points in poly time (perturbed GD, Jin et al. 2017)
```

### Sharp vs Flat Minima
```
  Sharp minimum:  high curvature (large Hessian eigenvalues)
                  small basin → small perturbation → large loss increase
                  generalizes poorly

  Flat minimum:   low curvature (small Hessian eigenvalues)
                  large basin → robust to perturbation → good generalization
                  SGD noise preferentially finds flat basins

  Sharpness-Aware Minimization (SAM):
    x_t+1 = x_t - α ∇f(x_t + ε ∇f(x_t) / ‖∇f(x_t)‖)
    Explicitly seeks flat minima by maximizing sharpness before gradient step
```

### The Role of Overparameterization
```
  Classical (convex): more parameters → more capacity → potentially worse
  Modern (neural nets): overparameterization makes optimization easier

  Loss landscape of overparameterized nets:
    - Many equivalent global minima (symmetry, permutation)
    - Connected manifold of global minima (mode connectivity)
    - SGD finds and stays near global minimum manifold
    - Implicit bias of GD: min-norm solution
```

---

## 9. Decision Cheat Sheet

| Scenario | Method | Why |
|----------|--------|-----|
| Convex, small data | L-BFGS | Superlinear convergence, no LR tuning |
| Convex, large n | SGD with schedule | Per-sample cost, variance OK |
| Convex, ill-conditioned | Nesterov / conjugate gradient | Optimal first-order rate |
| Neural net, general | AdamW + cosine+warmup | Adaptive LR, decoupled decay |
| Vision models | SGD + momentum + cosine | Better generalization than Adam |
| Transformers / LLMs | AdamW + warmup + cosine | Standard, well-validated |
| RL policy | Adam or SGD | PPO uses Adam; value net sometimes SGD |
| Generalization matters most | SAM + base optimizer | Explicit flat minimum seeking |

---

## 10. Common Confusion Points

1. **"Adam converges faster so it generalizes better"** — Faster convergence ≠ better generalization. SGD+momentum often finds flatter minima than Adam, especially for vision. The right choice depends on the task.

2. **"Decreasing LR eliminates the noise"** — With a decaying LR (αₜ → 0), SGD converges to the exact minimum. But that minimum might be sharp. Noise at the right scale is beneficial.

3. **"Local minima are the main problem in deep learning"** — Empirically, local minima quality is similar to global minima in overparameterized nets. Saddle points and plateaus are more problematic, and these are addressable.

4. **"Weight decay = L2 regularization"** — In SGD they're equivalent. In Adam, they're not: L2 regularization adds λx to the gradient, which gets adapted by Adam's second moment. Weight decay (AdamW) applies the decay directly to x, bypassing adaptation. AdamW is correct.

5. **"Higher batch size = worse generalization"** — The relationship is via the effective noise level. Linear scaling rule (Goyal et al.): scale LR linearly with batch size to maintain noise level. Warmup helps at large batch sizes.

6. **"Momentum accelerates convergence always"** — Heavy ball momentum can diverge on non-convex problems or with large step sizes. Nesterov momentum has theoretical guarantees; heavy ball doesn't for non-strongly-convex problems.

7. **"The learning rate is the most important hyperparameter"** — Arguably yes, but the LR schedule shape matters as much as the initial value. Warmup + cosine is robust across a wide range of peak LRs.
