# Optimization — Complete Reference

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         OPTIMIZATION LANDSCAPE                              │
│              minimize f(x)  subject to constraints on x                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  By structure of f:                                                         │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐                  │
│  │   CONVEX      │  │  NON-CONVEX   │  │  COMBINATORIAL│                  │
│  │               │  │               │  │               │                  │
│  │ Local = global│  │ Many local min│  │ Discrete vars │                  │
│  │ Poly-time     │  │ NP-hard often │  │ NP-hard often │                  │
│  │ LP, QP, SOCP  │  │ Deep learning │  │ TSP, ILP      │                  │
│  └───────────────┘  └───────────────┘  └───────────────┘                  │
│                                                                             │
│  By constraints:                                                            │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐                  │
│  │ UNCONSTRAINED │  │  EQUALITY     │  │  INEQUALITY   │                  │
│  │               │  │               │  │               │                  │
│  │ ∇f = 0        │  │ Lagrange mult │  │ KKT conditions│                  │
│  │ Gradient desc │  │ h(x) = 0      │  │ g(x) ≤ 0      │                   │
│  └───────────────┘  └───────────────┘  └───────────────┘                  │
│                                                                             │
│  Key algorithms by regime:                                                  │
│  Convex+smooth → gradient descent, Newton, L-BFGS                         │
│  Convex LP/QP  → simplex, interior point                                   │
│  Non-convex    → SGD + variants (ML), simulated annealing, genetic algos  │
│  Combinatorial → branch & bound, LP relaxation, heuristics                │
└─────────────────────────────────────────────────────────────────────────────┘
```

**The fundamental insight**: the structure of the problem (convex vs. non-convex,
smooth vs. non-smooth, constrained vs. unconstrained) determines both the
difficulty and the algorithm. Knowing which regime you're in is the first step.

---

## Unconstrained Optimization

### Optimality Conditions

For f: ℝⁿ → ℝ sufficiently smooth, at a local minimum x*:

```
First-order necessary:    ∇f(x*) = 0             (x* is a "stationary point")
Second-order necessary:   ∇²f(x*) ⪰ 0            (Hessian is PSD)
Second-order sufficient:  ∇²f(x*) ≻ 0            (Hessian is PD → strict local min)
```

**Hessian ∇²f** is the n×n matrix of second partials: (∇²f)ᵢⱼ = ∂²f/∂xᵢ∂xⱼ.
Second-order Taylor expansion:

```
f(x* + d) ≈ f(x*) + ∇f(x*)ᵀd + ½ dᵀ∇²f(x*)d
```

If H = ∇²f(x*) is positive definite, then f(x* + d) > f(x*) for all small d ≠ 0.

**Saddle points**: ∇f = 0 but H has both positive and negative eigenvalues.
In ML this is the dominant obstacle — not local minima, which are rare in
high dimensions and tend to have similar loss to global minima.

### Gradient Descent

```
x_{k+1} = x_k − α ∇f(x_k)        α = step size (learning rate)
```

**Convergence for L-smooth, μ-strongly convex f**:
```
‖x_k − x*‖² ≤ (1 − μ/L)^k ‖x_0 − x*‖²

Condition number κ = L/μ governs convergence rate.
Optimal step size α = 1/L.   Rate: (1 − 1/κ) per step.
For κ = 1000: need ~6900 steps to reduce error 1000×.
```

### Convergence Lower Bounds and Nesterov Optimality

These rates are tight — there are matching lower bounds:

```
  Nesterov lower bound (first-order oracle complexity):
  For ANY first-order method (using only gradient evaluations), on the class
  of L-smooth convex functions, after k steps:

    f(x_k) - f* ≥ Ω(L‖x_0 - x*‖² / k²)

  Gradient descent achieves O(L‖x_0-x*‖²/k) — suboptimal by a factor of k.
  Nesterov accelerated gradient achieves O(L‖x_0-x*‖²/k²) — matches the lower bound.
  Accelerated gradient descent (NAG) is an optimal first-order method for convex f.

  For μ-strongly convex and L-smooth:
    Lower bound: any first-order method needs Ω(√κ log 1/ε) iterations.
    Gradient descent: O(κ log 1/ε) — suboptimal by √κ.
    Nesterov accelerated: O(√κ log 1/ε) — optimal.

  This makes acceleration not just a heuristic but a computational necessity
  for high-condition-number problems (κ = 10⁶ is common in ML).

  ┌───────────────────────────────────────────────────────────────────────┐
  │  Method            │  Convex rate    │  Strongly convex rate          │
  ├───────────────────────────────────────────────────────────────────────┤
  │  Gradient descent  │  O(1/k)         │  O((1-1/κ)^k)                 │
  │  Nesterov (opt.)   │  O(1/k²) ← opt │  O((1-1/√κ)^k) ← opt         │
  │  Lower bound       │  Ω(1/k²)        │  Ω((1-1/√κ)^k)               │
  └───────────────────────────────────────────────────────────────────────┘

  Nesterov acceleration (momentum formulation):
    y_{k+1} = x_k − (1/L) ∇f(x_k)           (gradient step)
    x_{k+1} = y_{k+1} + (k-1)/(k+2) (y_{k+1} - y_k)   (momentum step)
  The momentum coefficient (k-1)/(k+2) → 1 is not heuristic — it's derived
  to make the "estimate sequence" method work.
```

**L-smoothness**: ‖∇f(x) − ∇f(y)‖ ≤ L‖x − y‖. Gradient doesn't change faster
than L per unit distance. Ensures steps of size 1/L always decrease f.

**Strong convexity** (μ > 0): f(y) ≥ f(x) + ∇f(x)ᵀ(y−x) + (μ/2)‖y−x‖².
Implies unique global minimum.

### Step Size Rules

| Rule | Formula | Notes |
|------|---------|-------|
| Fixed | α_k = α | Need α ≤ 1/L; simple |
| Backtracking (Armijo) | Reduce α until f(x−α∇f) ≤ f(x) − c·α‖∇f‖² | No L required |
| Wolfe conditions | Armijo + curvature | Standard for quasi-Newton |
| Exact line search | α = argmin_α f(x_k − α∇f) | Optimal; expensive |
| Polyak | α_k = (f(x_k) − f*)/‖∇f‖² | Optimal; requires knowing f* |

### Newton's Method

```
x_{k+1} = x_k − [∇²f(x_k)]⁻¹ ∇f(x_k)     (Newton direction: dₙ = −H⁻¹∇f)
```

Locally approximate f by its quadratic Taylor expansion; minimize the quadratic exactly.

**Convergence**: quadratic near x* — once ‖x_k − x*‖ < ε, next iterate has
error O(ε²). Doubles digits of accuracy per step.

**Cost per step**: O(n³) for H⁻¹. Prohibitive for n > 10³. ML models with 10⁹
parameters: completely impractical.

**Modified Newton**: add δI when H is not PD (saddle points): H + δI ≻ 0.
Ensures descent direction, handles non-convex regions.

### Quasi-Newton: BFGS and L-BFGS

Approximate H⁻¹ incrementally from gradient differences — no explicit Hessian.

```
BFGS (rank-2 update to inverse Hessian approximation B_k):
  s_k = x_{k+1} − x_k,   y_k = ∇f_{k+1} − ∇f_k,   ρ_k = 1/(y_kᵀ s_k)
  B_{k+1} = (I − ρ_k s_k y_kᵀ) B_k (I − ρ_k y_k s_kᵀ) + ρ_k s_k s_kᵀ
```

Superlinear convergence in practice.

**L-BFGS**: store only last m pairs (s_k, y_k), m ≈ 10–20. Apply two-loop
recursion to compute B_k ∇f in O(mn). **Standard for large-scale smooth
optimization** (scipy `minimize(method='L-BFGS-B')`, PyTorch `LBFGS`).

### Information Geometry and Natural Gradient

The standard gradient ∇_θ L treats the parameter space as Euclidean (‖Δθ‖₂).
But when θ parameterizes a probability distribution, the natural geometry is
given by the Fisher information metric:

```
  Fisher information matrix:
    F(θ)ᵢⱼ = E_{x~p(·;θ)}[∂_i log p(x;θ) · ∂_j log p(x;θ)]
            = -E[∂_i ∂_j log p(x;θ)]

  F(θ) defines a Riemannian metric on the manifold of distributions.
  The geodesic distance is the Fisher-Rao distance, closely related to KL divergence:
    D_KL(p(·;θ) || p(·;θ+dθ)) ≈ ½ dθᵀ F(θ) dθ  (to second order)

  Natural gradient descent: steepest descent in KL-divergence (Fisher) metric.
    θ ← θ − α F(θ)^{-1} ∇L(θ)

  Key property: parameterization invariance.
  Standard gradient depends on the parameterization (chain rule changes ∇L).
  Natural gradient is invariant: if θ = g(φ), the update in φ-space gives
  the same distribution update as in θ-space. This is the "right" notion
  of steepest descent for statistical models.

  Examples:
    For diagonal Gaussian N(μ, σ²): F is diagonal with 1/σ² and 2/σ².
    Natural gradient scales each direction by its Fisher curvature.
    For softmax: natural gradient is exactly Newton's method on logistic loss.

  Practical approximations (F(θ)^{-1} is n×n — too large for neural nets):
    K-FAC (Kronecker-Factored Approximate Curvature):
      Assumes layers independent, approximates F as Kronecker product.
      F_layer ≈ A ⊗ G  where A = input covariance, G = gradient covariance.
      Invert cheaply: (A⊗G)^{-1} = A^{-1} ⊗ G^{-1}.
    EKFAC, KFRA: refinements with better approximation quality.

  Connection to Adam: Adam's v_k tracks E[(∇f)²] per coordinate ≈ diagonal F.
  Adam is an approximation to natural gradient with a diagonal Fisher estimate.
  This is why Adam is effective: it approximates second-order information cheaply.
```

---

## Convex Analysis

### Convex Sets

C is **convex** if for any x, y ∈ C and λ ∈ [0,1]:  λx + (1−λ)y ∈ C.

**Examples**: halfspaces {aᵀx ≤ b}, balls, ellipsoids, polyhedra {Ax ≤ b},
PSD cone {X : X ⪰ 0}.

**Separating hyperplane theorem**: disjoint convex sets can always be separated
by a hyperplane. Foundation of SVMs.

**Extreme points**: vertices of a polytope — cannot be written as a convex
combination of other points. LP optima always occur at extreme points.

### Convex Functions

f is **convex** if dom f is convex and:
```
f(λx + (1−λ)y) ≤ λf(x) + (1−λ)f(y)   for all x, y ∈ dom f,  λ ∈ [0,1]
```

**Equivalent characterizations**:
- First-order:  f(y) ≥ f(x) + ∇f(x)ᵀ(y−x)   (tangent plane underestimates)
- Second-order: ∇²f(x) ⪰ 0 everywhere          (non-negative curvature)

**Key property**: every local minimum is a global minimum.

**Strongly convex** (μ > 0): f(y) ≥ f(x) + ∇f(x)ᵀ(y−x) + (μ/2)‖y−x‖².
Unique global minimum.

| Function | Convex? | Notes |
|----------|---------|-------|
| Affine aᵀx + b | Both convex and concave | |
| ‖x‖ (any norm) | ✅ | Triangle inequality |
| xᵀAx, A ⪰ 0 | ✅ | Quadratic form |
| eˣ | ✅ | f'' = eˣ > 0 |
| x log x | ✅ | f'' = 1/x > 0 |
| log(Σ eˣⁱ) | ✅ | log-sum-exp; gradient = softmax |
| max(x₁,...,xₙ) | ✅ | Pointwise max of linears |
| log(x) | Concave | |
| log det(X), X ≻ 0 | Concave | On PD matrices |

**Closure**: non-negative linear combo of convex = convex; pointwise max of
convex = convex; composition h∘g with h convex nondecreasing, g convex = convex.

### Subgradients (Non-smooth Convex)

For non-differentiable convex f (‖x‖₁, hinge loss), g is a **subgradient** at x if:
f(y) ≥ f(x) + gᵀ(y−x) for all y.

**Subdifferential** ∂f(x) = all subgradients. At smooth points ∂f = {∇f}.

**Subgradient method**: x_{k+1} = x_k − α_k g_k,  g_k ∈ ∂f(x_k).
Converges but no guaranteed descent per step — slower than gradient descent.

---

## Constrained Optimization: Lagrange Multipliers

### Equality Constraints

**Problem**: min f(x) s.t. h(x) = 0 (h: ℝⁿ → ℝᵐ, m < n).

**Lagrangian**: L(x, λ) = f(x) + λᵀh(x),   λ ∈ ℝᵐ.

**First-order necessary condition** (FONC) at x* (under regularity):
```
∇_x L(x*, λ*) = 0  →  ∇f(x*) + λ*ᵀ∇h(x*) = 0
∇_λ L(x*, λ*) = 0  →  h(x*) = 0
```

**Geometric meaning**: at the optimum, ∇f is a linear combination of the
constraint gradients ∇hᵢ — you cannot move along the constraint surface to
decrease f.

**Regularity (LICQ)**: ∇h₁,...,∇hₘ linearly independent at x*. Needed for
λ* to exist uniquely.

### KKT Conditions (Inequality Constraints)

**Problem**: min f(x) s.t. gᵢ(x) ≤ 0, hⱼ(x) = 0.

**Lagrangian**: L(x, μ, λ) = f(x) + μᵀg(x) + λᵀh(x),   μ ≥ 0.

**KKT conditions** (necessary under LICQ; sufficient for convex):
```
Stationarity:         ∇f(x*) + μ*ᵀ∇g(x*) + λ*ᵀ∇h(x*) = 0
Primal feasibility:   g(x*) ≤ 0,   h(x*) = 0
Dual feasibility:     μ* ≥ 0
Complementary slack:  μᵢ* gᵢ(x*) = 0   for all i
```

**Complementary slackness**: either gᵢ(x*) = 0 (constraint active) or μᵢ* = 0
(constraint inactive and irrelevant at the solution). This is the key KKT insight.

**SVM example**:
```
minimize   ½‖w‖²
subject to yᵢ(wᵀxᵢ + b) ≥ 1

KKT complementary slack: αᵢ(yᵢ(wᵀxᵢ+b) − 1) = 0
→ Only support vectors (on the margin boundary) have αᵢ > 0.
  All other training points don't affect the solution.
```

---

## Duality

### Lagrangian Duality

**Dual function**: g(λ, μ) = inf_x L(x, λ, μ). Always concave.

**Dual problem**: max g(λ, μ) s.t. μ ≥ 0.

**Weak duality**: d* ≤ p* (always). The duality gap p* − d* ≥ 0.

**Strong duality** (Slater's condition): if primal is convex and has a strictly
feasible point, then d* = p* — no duality gap.

**Why duality matters**:
1. Dual may be easier to solve
2. λᵢ* = ∂p*/∂bᵢ — shadow price of constraint i (sensitivity analysis)
3. SVM dual turns a primal QP in (w,b) into dual QP in αᵢ, enabling kernel trick

### LP Duality

Primal: min cᵀx s.t. Ax ≥ b, x ≥ 0

Dual:  max bᵀy s.t. Aᵀy ≤ c, y ≥ 0

Strong duality always holds for feasible LPs. Dual provides a lower-bound
certificate of optimality.

---

## Linear Programming

### Standard Form and Geometry

```
min cᵀx  s.t.  Ax = b,  x ≥ 0
```

Feasible set = convex polytope. **Fundamental theorem**: if optimum exists,
it is attained at a vertex (extreme point = basic feasible solution).

**Basic feasible solution**: choose m linearly independent columns B (a "basis"),
set non-basic variables to 0, solve xB = B⁻¹b ≥ 0.

### Simplex Method

Pivot between adjacent vertices with non-increasing cost:
```
1. Start at a BFS
2. Reduced costs: c̄N = cN − cBᵀ B⁻¹N
3. If c̄N ≥ 0: optimal
4. Enter variable j with c̄ⱼ < 0
5. Ratio test: leave variable with smallest xBᵢ/(B⁻¹N)ᵢⱼ
6. Pivot, repeat
```

Worst case exponential (Klee-Minty), but O(m) pivots in practice.

### Interior Point Methods

Follow the **central path** — trajectory of solutions to:
```
min cᵀx − (1/t) Σ log(xᵢ)    as t → ∞
```
Polynomial time: O(n³·⁵ L). Better for large dense LPs; harder to warm-start.

**Simplex vs. IPM**: simplex faster in practice for sparse problems and
warm-starting; IPM better for large dense problems and LP relaxations.

---

## Quadratic Programming

```
min  ½ xᵀQx + cᵀx   s.t.  Ax ≤ b,  Cx = d
```

**Convex QP** (Q ⪰ 0): polynomial-time solvable. Includes:
- Least squares, ridge regression, LASSO (via reformulation)
- SVM training, portfolio optimization (Q = covariance matrix)

**Active set method**: maintain active constraint guess, solve equality QP,
update active set. Fast for small-medium problems.

**Least squares** (fundamental QP):
```
min ‖Ax − b‖²  →  x* = (AᵀA)⁻¹Aᵀb    (normal equations)
Regularized: min ‖Ax−b‖² + λ‖x‖²  →  x* = (AᵀA + λI)⁻¹Aᵀb
```
Solve via Cholesky (if AᵀA is PD) or QR (more stable numerically).

---

## Gradient Methods for Machine Learning

### Online Learning and Regret Minimization

SGD viewed as an online learning algorithm connects optimization to statistical
learning theory:

```
  Online learning setup: at step t,
    1. Predict θ_t
    2. Observe loss function fₜ(·)
    3. Suffer loss fₜ(θ_t)
    4. Update θ_{t+1}

  Regret: R_T = Σ_{t=1}^T fₜ(θ_t) − min_θ Σ_{t=1}^T fₜ(θ)
  Measures how much worse we do vs. the best fixed θ in hindsight.

  SGD achieves: R_T ≤ ‖θ_1 - θ*‖² / (2α) + α Σ ‖gₜ‖²
  With step α = D/(G√T):  R_T = O(DG√T)   where D = diameter, G = grad bound.
  Average regret R_T/T → 0 (sublinear regret = no-regret algorithm).

  Online-to-batch conversion:
    Run online algorithm, output average θ̄_T = (1/T)Σ θ_t.
    Excess risk: E[f(θ̄_T)] - f* ≤ R_T/T = O(1/√T).
    This recovers the O(1/√T) convergence rate for SGD from an online perspective.

  Follow-the-Regularized-Leader (FTRL):
    θ_{t+1} = argmin_θ { Σ_{s≤t} fₛ(θ) + (1/η)R(θ) }
    Generalizes SGD; with R(θ) = ‖θ‖²/2, reduces to online gradient descent.

  AdaGrad as FTRL:
    FTRL with per-coordinate adaptive regularizer.
    Achieves O(√(Σ‖gₜ‖²)) regret — automatically adapts to sparse gradients.
    For sparse features (NLP), most gₜ,ᵢ = 0; AdaGrad gives O(√(sparse updates))
    per coordinate, far better than O(√T).

  PAC learning connection:
    n iid samples, hypothesis class H with VC dimension d.
    Uniform convergence (via concentration): O(d/ε²·log 1/δ) samples suffice.
    SGD on convex surrogate loss achieves this bound efficiently.
    For non-convex (deep learning): no clean PAC bound — generalization is not
    explained by VC dimension (models are heavily overparameterized).
    Modern explanation: implicit regularization of SGD, flat minima, NTK regime.
```

### Stochastic Gradient Descent (SGD)

Training loss f(θ) = (1/N) Σᵢ fᵢ(θ). Full gradient costs O(N) — use mini-batches:

```
g_k = (1/|B|) Σ_{i∈B} ∇fᵢ(θ_k)        (unbiased: E[g_k] = ∇f(θ_k))
θ_{k+1} = θ_k − α_k g_k
```

Per-step cost O(|B|) ≪ O(N). Gradient noise is helpful in non-convex settings:
escapes sharp minima, finds flatter (more generalizable) basins.

**Convergence** (convex, Robbins-Monro): Σ α_k = ∞, Σ α_k² < ∞.
Classic choice: α_k = α/√k.

### Momentum

```
v_{k+1} = β v_k − α ∇f(θ_k)
θ_{k+1} = θ_k + v_{k+1}         (β = 0.9 typical)
```

Damps oscillations in narrow ravines; accelerates along consistent gradient directions.

**Nesterov momentum** (NAG): compute gradient at lookahead point θ + β(θ_k − θ_{k-1}).
Achieves optimal O(1/k²) rate for convex f (vs. O(1/k) for plain gradient descent).

### Adam and Variants

**Adam** (the default deep learning optimizer):
```
m_k = β₁ m_{k-1} + (1−β₁) ∇f           (1st moment: gradient mean)
v_k = β₂ v_{k-1} + (1−β₂) (∇f)²        (2nd moment: uncentered variance)
m̂_k = m_k / (1−β₁^k),   v̂_k = v_k / (1−β₂^k)    (bias correction)
θ ← θ − α · m̂_k / (√v̂_k + ε)

Defaults: β₁=0.9, β₂=0.999, ε=1e-8, α=1e-3
```

**Bias correction**: at step 1, m₁ = (1−β₁)∇f ≈ 0.1∇f — biased toward zero
because initialized at 0. Division by (1−β₁^k) corrects this cold-start effect.

**AdamW** (decoupled weight decay): apply weight decay directly to parameters
rather than adding L2 to loss (which interacts badly with Adam's adaptive scaling):
```
θ ← θ − α · m̂_k/(√v̂_k + ε) − α·λ·θ
```
AdamW is the standard for transformer and LLM training.

### Adaptive Methods Summary

| Optimizer | Key idea | Best for |
|-----------|---------|---------|
| SGD | Plain gradient | CNNs (when tuned) |
| SGD + momentum | Exponential moving average of gradient | CNNs, best final loss |
| AdaGrad | Per-dim scale by cumulative squared grad | Sparse features/NLP |
| RMSProp | AdaGrad with exponential forgetting | RNNs |
| Adam | Momentum + adaptive per-dim scale + bias correction | Transformers, default |
| AdamW | Adam + decoupled weight decay | LLMs, fine-tuning |
| L-BFGS | Full quasi-Newton (full-batch only) | Small models, scipy |

### Learning Rate Schedules

| Schedule | Use |
|----------|-----|
| Constant | Fine-tuning |
| Cosine annealing | LLM pre-training |
| Linear warmup + cosine | Transformers (prevent early divergence) |
| 1-cycle | Fast convergence (fast.ai) |
| Inverse sqrt | Theory-backed, NLP |

**Why warmup**: at initialization, gradients are large and unreliable. Linear
warmup lets the optimizer stabilize before using full learning rate.

**SGD vs. Adam in practice**: SGD+momentum often finds flatter minima (better
generalization) but requires careful tuning. Adam converges faster with less
tuning but may find sharper minima. Empirical rule: Adam for transformers, SGD
for vision models where tuning effort is justified.

---

## Convex Problem Hierarchy

```
LP  ⊂  QP  ⊂  SOCP  ⊂  SDP  ⊂  General convex

LP:   Linear objective + linear constraints
QP:   Quadratic objective + linear constraints
SOCP: ‖Ax+b‖ ≤ cᵀx+d (second-order cone)
SDP:  F(x) ⪰ 0 (semidefinite constraint) — covers eigenvalue bounds, LMIs
```

**SDP applications**: MAX-CUT 0.878-approximation, control theory (LMIs),
covariance estimation, sum-of-squares proofs.

**CVXPY** — disciplined convex programming in Python:
```python
import cvxpy as cp
x = cp.Variable(n)
prob = cp.Problem(
    cp.Minimize(cp.sum_squares(A @ x - b) + λ * cp.norm1(x)),  # LASSO
    [x >= 0]
)
prob.solve()   # dispatches to OSQP / SCS / MOSEK automatically
```

---

## Proximal Algorithms

For f = g + h where g is smooth, h is non-smooth (e.g., ‖x‖₁):

```
Proximal operator:   prox_{αh}(v) = argmin_x { h(x) + (1/2α)‖x−v‖² }

Proximal gradient:   x_{k+1} = prox_{αh}(x_k − α ∇g(x_k))
```

For h = λ‖·‖₁, proximal operator = **soft thresholding**:
```
(prox_{αλ‖·‖₁}(v))ᵢ = sign(vᵢ) · max(|vᵢ| − αλ, 0)
```
Gradient step on smooth part, shrink-to-zero for sparsity → LASSO.

**FISTA** (Fast ISTA): add Nesterov momentum to proximal gradient → O(1/k²).

**ADMM**: split variables for composite objectives and distributed problems.
Standard for federated learning and large-scale regularized regression.

---

## Non-Convex Landscape (ML)

### Convergence to Stationary Points

For non-convex f, gradient descent cannot guarantee global optimality. The
standard convergence result is:

```
  For L-smooth f (not necessarily convex), gradient descent with α = 1/L:

  After T steps:  min_{k ≤ T} ‖∇f(x_k)‖² ≤ 2L(f(x_0) − f*) / T

  I.e., the minimum gradient norm over T steps is O(1/T).
  We converge to a stationary point (∇f = 0), but it could be a saddle or local min.
  Complexity to find ε-stationary point: T = O(L(f(x_0)-f*)/ε²).

  For SGD with bounded variance E[‖gₜ - ∇f(xₜ)‖²] ≤ σ²:
    min_{k ≤ T} E[‖∇f(x_k)‖²] ≤ O(L(f₀-f*)/T + σ/√T)
  Noise term σ/√T dominates; step size must decay to zero.

  Perturbed gradient descent (Jin et al. 2017):
    Add Gaussian noise ξ_k ~ N(0, δI) to the gradient occasionally.
    If f satisfies the strict saddle property (every saddle has at least one
    strictly negative Hessian eigenvalue), perturbed GD escapes saddles
    in polynomial time and converges to an approximate local minimum.
    Rate: O(1/ε^4) iterations to find ε-second-order stationary point
    (‖∇f‖ ≤ ε and λ_min(∇²f) ≥ -√ε).

  Strict saddle property:
    Holds (conjectured) for neural networks under mild conditions.
    Empirical evidence: loss landscapes of overparameterized networks
    have essentially no poor local minima — saddle points dominate.
    This is why SGD works in practice despite non-convexity.
```

**Saddle points dominate** in high dimensions — far more common than bad local
minima. SGD noise escapes saddle points naturally; second-order methods use
negative curvature directions explicitly.

**Flat minima hypothesis**: flatter minima (small Hessian eigenvalues) generalize
better — less sensitive to weight perturbation.

**SAM** (Sharpness-Aware Minimization):
```
θ* = argmin max_{‖ε‖≤ρ} f(θ + ε)
```
Explicitly seeks flat minima. Strong empirical results on vision tasks.

**Neural tangent kernel**: infinite-width networks behave like kernel regression —
gradient descent is convex in that limit. Explains why overparameterized networks
converge despite apparent non-convexity.

---

## Applications Cheat Sheet

| Problem | Formulation | Algorithm |
|---------|-------------|-----------|
| Least squares | min ‖Ax−b‖² | Normal equations / QR |
| Ridge regression | min ‖Ax−b‖² + λ‖x‖² | Closed form |
| LASSO | min ‖Ax−b‖² + λ‖x‖₁ | ISTA/FISTA, ADMM |
| SVM | min ½‖w‖² s.t. margin constraints | QP (SMO dual) |
| Portfolio | min xᵀΣx s.t. μᵀx ≥ r, 1ᵀx=1 | QP (Gurobi, CVXPY) |
| NN training | min L(θ) non-convex | Adam/SGD + schedule |
| LP allocation | min cᵀx s.t. Ax ≤ b | Simplex / interior point |
| MAX-CUT | NP-hard integer | SDP relaxation (0.878 approx) |
| LASSO path | All λ values | LARS algorithm |

---

## Decision Cheat Sheet

| Situation | Algorithm |
|-----------|-----------|
| Convex, smooth, small n | L-BFGS (scipy, torch LBFGS) |
| Convex, smooth, large n | Gradient descent with backtracking |
| Convex, high κ, need speed | Nesterov accelerated gradient (optimal for convex) |
| LP | Simplex or interior point (scipy.linprog, Gurobi) |
| QP convex | OSQP, CVXOPT, Gurobi |
| Non-smooth regularization | Proximal gradient (ISTA/FISTA, ADMM) |
| General convex (SOCP/SDP) | CVXPY + MOSEK |
| Neural network | Adam/AdamW + cosine LR + warmup |
| CNN (best final loss) | SGD + momentum + tuned schedule |
| Integer program | Gurobi, CPLEX (branch and bound) |
| Black-box, no gradients | Bayesian optimization, CMA-ES |
| Parameter space = distributions | Natural gradient / K-FAC |
| Need to escape saddles (non-convex) | Perturbed GD or SGD (noise escapes naturally) |

---

## Common Confusion Points

**KKT necessary vs. sufficient**: KKT is necessary at every local optimum (under
LICQ). For convex problems, KKT is also sufficient — any KKT point is globally
optimal. For non-convex problems, a KKT point might be a local min, local max,
or saddle.

**Gradient descent on Lagrangian ≠ constrained optimization**: running GD-ascent
on L(x, λ) (min over x, max over λ) works for convex-concave L (LP, QP duals)
but cycles on general non-convex problems.

**Adam's ε is not just numerical**: ε also lower-bounds the effective step size
per dimension, preventing stagnation in dense gradient dimensions. Too small ε
with noisy gradients → instability.

**log-sum-exp is convex**: log(Σ eˣⁱ) is convex, so cross-entropy loss is a
convex function of the logits. This is why logistic regression is convex despite
the sigmoid nonlinearity.

**Simplex on vertices, IPM in interior**: IPM stays strictly feasible, approaching
the boundary only asymptotically. Better for large dense LPs; no warm-starting.
Simplex excels on sparse problems and can warm-start from a previous solution.

**L-BFGS vs. Adam**: L-BFGS is full-batch. SGD-based stochastic variants (oLBFGS,
SFO) exist but are complex. For mini-batch neural network training, Adam/AdamW
dominates. L-BFGS is excellent for small-scale ML (sklearn's logistic regression
uses `solver='lbfgs'` by default).

**Nesterov vs. momentum**: standard momentum (heavy ball) does not achieve the
optimal O(1/k²) rate in general — it achieves O(1/k²) only for quadratics.
Nesterov's acceleration achieves O(1/k²) for all L-smooth convex functions and
is provably optimal. The momentum coefficient must grow as (k−1)/(k+2), not stay
fixed at β.
