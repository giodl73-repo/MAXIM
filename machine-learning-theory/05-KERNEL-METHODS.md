# Kernel Methods and Reproducing Kernel Hilbert Spaces

## The Big Picture

Kernel methods provide a rigorous framework for learning in infinite-dimensional function spaces while keeping computation tractable via the kernel trick. The RKHS is the function-analytic foundation; SVMs are the canonical application; and the kernel trick reappears in the Neural Tangent Kernel (Module 06).

```
+──────────────────────────────────────────────────────────────────+
|                  KERNEL METHODS LANDSCAPE                        |
|                                                                  |
|  PROBLEM: Linear methods work in ℝⁿ but data is nonlinear.       |
|                                                                  |
|  NAIVE SOLUTION: Map x ∈ ℝⁿ to φ(x) ∈ ℝᴰ (D >> n)             |
|  Learn a linear model in the feature space.                      |
|  PROBLEM: If D = ∞ (e.g., polynomial features), computation is   |
|  infinite.                                                       |
|                                                                  |
|  KERNEL TRICK: Never compute φ(x) explicitly.                    |
|  Only compute k(x, x') = ⟨φ(x), φ(x')⟩ — inner products.       |
|  All learning algorithms that only need inner products work      |
|  in O(m²) time, regardless of the (infinite) feature space.    |
|                                                                  |
|  RKHS: The function space implicitly defined by the kernel.      |
|  Learning in RKHS = learning a linear function in feature space. |
+──────────────────────────────────────────────────────────────────+
```

---

## Positive Definite Kernels

**Definition**: A function k: X × X → ℝ is a positive definite (PD) kernel if:
1. Symmetric: k(x, x') = k(x', x)
2. Positive semidefinite: for any finite set {x₁,...,xₘ}, the Gram matrix K with Kᵢⱼ = k(xᵢ, xⱼ) is PSD

```
GRAM MATRIX PSD CHECK
  For any α ∈ ℝᵐ:  Σᵢⱼ αᵢ αⱼ k(xᵢ, xⱼ) ≥ 0

INTUITION: PD kernel = inner product of feature vectors
  k(x, x') = ⟨φ(x), φ(x')⟩_H  for some Hilbert space H, map φ

  Conversely: any PD kernel defines such a map (Mercer's theorem).
```

---

## Common Kernels

| Kernel | Formula | Feature Space | Properties |
|--------|---------|--------------|------------|
| Linear | k(x,x') = xᵀx' | ℝⁿ itself | Trivial — no lift |
| Polynomial (deg d) | k(x,x') = (xᵀx' + c)ᵈ | Monomials up to degree d | Finite-dim features |
| RBF / Gaussian | k(x,x') = exp(-||x-x'||²/2σ²) | Infinite-dim | Universal approximator |
| Laplace | k(x,x') = exp(-||x-x'||/σ) | Infinite-dim | Heavier tails than RBF |
| Matérn | k(x,x') = (complicated) | Sobolev space H^ν | Differentiability-controlled |
| Periodic | k(x,x') = exp(-2sin²(π|x-x'|/p)/σ²) | Fourier features | For periodic data |
| String kernel | Counts common subsequences | Sequence space | NLP applications |

**RBF kernel feature space explicitly:**
k(x, x') = exp(-||x-x'||²/2σ²) = Σ_{α} (x^α · x'^α / α!) · e^{-||x||²/2} · e^{-||x'||²/2}
The feature map has infinitely many components indexed by multi-indices α.

---

## Bochner's Theorem and the Spectral Characterization of Kernels

For translation-invariant kernels k(x, x') = k(x − x'), there is a complete harmonic analysis characterization:

```
BOCHNER'S THEOREM (1933)
  A continuous function k: ℝⁿ → ℝ is the covariance function of a
  stationary process (i.e., a positive definite kernel) if and only if
  it is the Fourier transform of a non-negative finite measure p(ω):

    k(x - x') = ∫ e^{iωᵀ(x-x')} p(ω) dω = E_{ω~p}[e^{iωᵀ(x-x')}]

  p(ω) is the spectral density (or spectral measure) of the kernel.
  k is PD ⟺ p is a non-negative measure.

SPECTRAL DENSITIES OF STANDARD KERNELS
  RBF kernel:       k(r) = exp(-r²/2σ²)
                    p(ω) = N(0, σ⁻²I)   [Gaussian spectral density]

  Laplace kernel:   k(r) = exp(-|r|/σ)
                    p(ω) ∝ (1 + σ²ω²)⁻¹  [Cauchy spectral density]

  Matérn-ν kernel:  k(r) = (2^{1-ν}/Γ(ν))(√2ν r/ℓ)ν K_ν(√2ν r/ℓ)
                    p(ω) ∝ (2ν/ℓ² + ‖ω‖²)^{-(ν + d/2)}  [Student-t spectral]
                    ν = ½: Laplace; ν → ∞: RBF.

  Periodic kernel:  p(ω) = discrete measure on integer frequencies.
```

**Implication: Random Fourier Features (Rahimi & Recht 2007).** Bochner's theorem gives an unbiased Monte Carlo estimator for any translation-invariant kernel:

```
RANDOM FOURIER FEATURES
  Sample ω₁,...,ω_D ~ p(ω),  bⱼ ~ Uniform[0, 2π]

  Define explicit feature map:
    z(x) = √(2/D) · [cos(ω₁ᵀx + b₁), ..., cos(ωᴰᵀx + bᴅ)] ∈ ℝᴰ

  Then: E[z(x)ᵀz(x')] = k(x - x')

  → z(x)ᵀz(x') ≈ k(x, x') with variance O(1/D)

PRACTICAL CONSEQUENCE
  Instead of O(m²) kernel matrix, compute O(mD) feature matrix.
  D ~ 10³ random features approximates RBF kernel to <1% error.
  Training O(mD²) instead of O(m³) — crucial for large m.
  Prediction O(D) instead of O(m) per test point.
```

The Random Fourier Features construction is Bochner's theorem made algorithmic. The spectral density tells you how to sample: for RBF, draw from a Gaussian; for Laplace, draw from a Cauchy. For non-translation-invariant kernels (e.g., polynomial, string kernels), Bochner doesn't apply directly — but analogous random feature constructions exist via Mercer expansions or structured matrices.

## Mercer's Theorem

The fundamental theorem connecting kernels to feature maps:

```
MERCER'S THEOREM
─────────────────
Let X be a compact metric space, k: X × X → ℝ continuous and PD.

Then there exist:
  • Eigenfunctions φⱼ: X → ℝ, orthonormal in L²(X)
  • Eigenvalues μⱼ ≥ 0

Such that:
  k(x, x') = Σⱼ μⱼ φⱼ(x) φⱼ(x')   [convergence in L²]

FEATURE MAP
  φ(x) = (√μ₁ φ₁(x), √μ₂ φ₂(x), ...)   ← in ℓ² sequence space

  k(x, x') = ⟨φ(x), φ(x')⟩_{ℓ²}

INTERPRETATION
  • Smooth kernels: eigenvalues decay fast → effective finite dimension
  • Rough kernels: slow decay → many relevant directions
  • RBF on [0,1]: eigenvalues decay as e^{-cj²} (extremely fast)
```

---

## Reproducing Kernel Hilbert Spaces (RKHS)

The RKHS is the function space where learning happens:

```
RKHS CONSTRUCTION
──────────────────
Given PD kernel k, define:

  H_k = closure of { Σᵢ αᵢ k(·, xᵢ) : αᵢ ∈ ℝ, xᵢ ∈ X }

with inner product:
  ⟨Σᵢ αᵢ k(·, xᵢ), Σⱼ βⱼ k(·, x'ⱼ)⟩_{H_k} = Σᵢⱼ αᵢ βⱼ k(xᵢ, x'ⱼ)

REPRODUCING PROPERTY (the key property)
  For any f ∈ H_k and any x ∈ X:
    f(x) = ⟨f, k(·, x)⟩_{H_k}

  "Evaluating f at x is a linear functional in H_k."
  k(·, x) is the "representer" of the evaluation functional at x.

NORM INTERPRETATION
  ||f||²_{H_k} = smoothness of f with respect to the kernel
  RBF kernel: smooth functions in H_k (Sobolev-like)
  Functions with large RKHS norm are "rough"
```

---

## The Representer Theorem

The core result that makes kernel learning tractable in infinite-dimensional H:

```
REPRESENTER THEOREM (Kimeldorf & Wahba 1971, Schölkopf et al. 2001)
─────────────────────────────────────────────────────────────────────
Consider the optimization problem:

  min_{f ∈ H_k}  R(f(x₁),...,f(xₘ), y₁,...,yₘ) + λ · Ω(||f||_{H_k})

where R is any loss, Ω is monotone increasing.

Then the minimizer has the form:

  f*(x) = Σᵢ₌₁ᵐ αᵢ k(x, xᵢ)

PROOF SKETCH:
  Decompose any f = f_∥ + f_⊥ where
    f_∥ is in span{k(·,x₁),...,k(·,xₘ)}
    f_⊥ is orthogonal to this span

  f_⊥ doesn't affect any f(xᵢ) (reproducing property).
  But f_⊥ contributes to ||f||² → can remove it to decrease penalty.
  → Optimal f has no f_⊥ component. QED.

IMPLICATION
  Infinite-dimensional optimization → finite-dimensional optimization.
  Solve for m coefficients α ∈ ℝᵐ, not infinite-dim function.

**Lagrangian duality perspective.** The representer theorem is the primal manifestation of strong duality for the infinite-dimensional convex program. The primal is convex (quadratic loss + convex norm penalty) and Slater's condition holds (the feasible set is the entire RKHS), so strong duality gives zero duality gap. The dual problem is finite-dimensional: the dual variables are m Lagrange multipliers αᵢ (one per training point), and the dual solution directly gives the representer theorem coefficients. The primal ∞-dimensional problem → finite dual is the same mechanism that turns the n-dimensional linear ridge regression into the m-dimensional kernel ridge regression via the identity (XᵀX + λI)⁻¹Xᵀ = Xᵀ(XXᵀ + λI)⁻¹.
```

---

## Kernel Ridge Regression

```
KERNEL RIDGE REGRESSION
────────────────────────
  min_{f ∈ H_k}  (1/m)||y - f(X)||² + λ||f||²_{H_k}

By representer theorem, f*(x) = Σᵢ αᵢ k(x, xᵢ) = k(x,·)ᵀα

  Let K be the m×m Gram matrix: Kᵢⱼ = k(xᵢ, xⱼ)

  Objective in α:  (1/m)||y - Kα||² + λ αᵀKα

  Solution:  α* = (K + λmI)⁻¹ y   [m×m linear system]

PREDICTION
  f*(x) = k(x, X)ᵀ α* = k(x,X)ᵀ (K + λmI)⁻¹ y

COMPLEXITY
  Training: O(m³) for matrix inversion
  Prediction: O(m) per test point

COMPARISON
  Linear ridge regression in ℝⁿ:  (XᵀX + λI)⁻¹Xᵀy
  Kernel ridge regression:          K(K + λI)⁻¹y
  These are related by duality: primal (n-dim) ↔ dual (m-dim).
```

---

## Support Vector Machines

```
HARD MARGIN SVM
────────────────
  Data: {(xᵢ, yᵢ) : yᵢ ∈ {-1,+1}}
  Find hyperplane w·x + b = 0 with maximum margin.

  max_{w,b}  2/||w||   subject to  yᵢ(w·xᵢ + b) ≥ 1 ∀i

  Equivalent:  min_{w,b}  (1/2)||w||²  s.t. yᵢ(w·xᵢ+b) ≥ 1

  Lagrangian dual:
    max_α  Σᵢ αᵢ - (1/2) Σᵢⱼ αᵢ αⱼ yᵢ yⱼ xᵢᵀxⱼ
    s.t.   αᵢ ≥ 0, Σᵢ αᵢ yᵢ = 0

  KERNEL SVM: Replace xᵢᵀxⱼ → k(xᵢ, xⱼ)
  Never compute φ(x) explicitly!

SOFT MARGIN SVM
  min_{w,b,ξ}  (1/2)||w||² + C·Σᵢ ξᵢ
  s.t.  yᵢ(w·xᵢ + b) ≥ 1 - ξᵢ,  ξᵢ ≥ 0

  C controls tradeoff: large C → hard margin, low bias, high variance
                       small C → soft margin, more bias, lower variance
```

---

## Generalization Bounds for Kernel Methods

```
SVM MARGIN BOUND
─────────────────
Let f(x) = Σᵢ αᵢ yᵢ k(x, xᵢ) and margin γ = min yᵢ f(xᵢ)/||w||.
With probability ≥ 1-δ:

  R(f) ≤ R̂_γ(f) + O( √( (B²C²)/(γ²m) + log(1/δ)/m ) )

where B = max_x √k(x,x), C = diameter of X in feature space.

KERNEL RIDGE REGRESSION EXCESS RISK
  If f* ∈ H_k with ||f*||_{H_k} ≤ M, then:
    E[||f_λ - f*||²_{L²}] ≤ O( M² · (λ + 1/(λm)) · polylog )

  Optimal λ ~ 1/√m → rate O(m^{-1/2}) generally
  Better with eigenvalue decay: up to O(m^{-2β/(2β+1)}) for β-smooth f*
```

---

## Decision Cheat Sheet

| Situation | Method | Key Hyperparameter |
|-----------|--------|-------------------|
| Nonlinear classification, small-medium data | Kernel SVM | C (margin), kernel bandwidth |
| Nonlinear regression | Kernel ridge regression | λ (regularization), kernel |
| Unknown feature space, smooth data | RBF kernel | σ (bandwidth) |
| Polynomial features needed | Polynomial kernel | degree d, constant c |
| Time series / sequences | Sequence kernels | Gap penalty, length |
| Want interpretable features | Explicit feature map | Degree, Fourier features |
| Large m (> 10⁶) | Random Fourier features | Approximation rank |

---

## Kernel Methods vs Neural Networks

```
COMPARISON (circa 2012-2024)
─────────────────────────────

KERNEL METHODS                     NEURAL NETWORKS
──────────────                     ───────────────
Convex optimization                Non-convex (SGD)
Global optimum guaranteed          Local optima (but SGD finds good ones)
Sample complexity bounds tight     Bounds vacuous (VC too large)
O(m³) training time                O(m) per parameter update
Fixed feature space                Learned representations
Theoretically principled           Empirically dominant

KEY INSIGHT
  On structured data (vision, language), neural nets learn
  features that are exponentially better than any fixed kernel.
  Kernel methods require the right kernel (feature choice = the hard part).
  Neural nets amortize feature learning into training.

RESURGENCE: NEURAL TANGENT KERNEL (Module 06)
  Infinite-width neural net training ≡ kernel regression with NTK.
  Connects neural nets and kernel theory.
  But: NTK regime is not where real neural nets operate.
```

---

## Common Confusion Points

**"RKHS is infinite-dimensional — how do I actually compute in it?"**
You never compute in the infinite-dimensional space directly. The representer theorem guarantees the optimizer lies in the finite-dimensional span {k(·,x₁),...,k(·,xₘ)}. All computation reduces to working with the m×m Gram matrix K.

**"What makes a kernel 'universal'?"**
A kernel is universal if the RKHS H_k is dense in C(X) (continuous functions). RBF kernel is universal on compact X: any continuous function can be approximated arbitrarily well by functions in H_k. Universal → can represent any target function → zero bias (if sufficient data). Non-universal kernels have bias baked in.

**"C in SVM vs λ in kernel ridge — are they the same?"**
They trade off the same way (model complexity vs data fit) but enter differently. In kernel ridge: λ multiplies the RKHS norm penalty. In SVM: C multiplies the hinge loss. They are inversely related: large C (low regularization) in SVM corresponds to small λ in ridge. You can show soft-margin SVM and kernel ridge regression are equivalent under square loss.

**"Why did kernel methods lose to neural nets in deep learning era?"**
Feature engineering is the bottleneck. Kernel methods need you to specify the kernel — which defines the feature space. For images, text, audio, the right features are not known in advance. Neural nets learn features from data. Additionally, kernel methods scale as O(m³); neural nets scale to billions of parameters and samples via GPU parallelism.
