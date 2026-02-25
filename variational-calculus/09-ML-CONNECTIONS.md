# Connections to Machine Learning and Gradient Flows

## The Big Picture

Variational calculus is not just classical mechanics and optimal control. It is the hidden
mathematical substrate of modern machine learning. Gradient descent is a discretized gradient
flow in function space. Neural ODEs are continuous-depth networks whose dynamics obey the
variational principle of Pontryagin. Optimal transport connects probability geometry to
variational problems (Wasserstein distance as the infimum of transport cost). Variational
autoencoders minimize a variational free energy. Lagrangian neural networks preserve Hamiltonian
structure by construction. These are all specific instances of extremizing a functional.

```
VARIATIONAL CALCULUS ↔ MACHINE LEARNING MAP
═══════════════════════════════════════════════════════════════════════════════

  VARIATIONAL CONCEPT               ML INSTANTIATION
  ──────────────────────────────    ────────────────────────────────────────
  Functional J[y]                   Loss functional L[θ] or L[f]
  Euler-Lagrange equation           Stationarity condition for parameters
  Gradient flow ẋ = −∇F             Gradient descent θ_t = −η ∇L(θ)
  Geodesic (shortest path)          Optimal transport path
  Hamilton's principle              Neural ODEs (continuous depth)
  Adjoint method / PMP              Backpropagation through time
  Wasserstein distance              Earth mover's distance for distributions
  Gibbs variational principle       ELBO in variational inference (VAE)
  Calculus of variations on Γ       Distribution-valued optimization (flows)
  Minimizing surface area           Implicit regularization of neural nets
```

---

## Gradient Descent as Variational Optimization

### From Euler-Lagrange to Gradient Flow

Consider a loss functional L[f] over functions f in a function space (e.g., the RKHS of a kernel machine). The stationarity condition δL/δf = 0 is an Euler-Lagrange equation.

**Gradient descent in function space**: Instead of solving δL/δf = 0 directly, follow the steepest descent:

    ∂f/∂t = −δL/δf    (gradient flow in function space)

This is a PDE (evolution equation for functions) whose steady state solves the original E-L equation.

**Discretization to parameter space**: If f is parameterized by θ (e.g., neural network weights), the chain rule gives:

    dθ/dt = −∇_θ L(θ)    (ODE in parameter space)

Euler discretization:

    θ_{k+1} = θ_k − η ∇_θ L(θ_k)    (gradient descent, step size η)

```
VARIATIONAL STRUCTURE OF GRADIENT DESCENT:

  CONTINUOUS TIME:
  θ̇(t) = −∇L(θ)    (gradient flow)
  Solution θ(t) → local minimum of L as t → ∞.

  DISCRETE TIME (Euler):
  θ_{k+1} = θ_k − η ∇L(θ_k)
  Implicit Euler (more stable):
  θ_{k+1} = θ_k − η ∇L(θ_{k+1})  ← proximal gradient method

  MOMENTUM (Heavy ball / Nesterov):
  v_{k+1} = γ v_k − η ∇L(θ_k)
  θ_{k+1} = θ_k + v_{k+1}
  This is the DISCRETE DAMPED HARMONIC OSCILLATOR (Euler-Lagrange with damping).
  Lagrangian: L[θ(t)] = (1/2)|θ̇|² − U(θ)  → equation of motion θ̈ + γθ̇ = −∇U
  Nesterov momentum → optimal convergence rate for convex L.

  SECOND-ORDER METHODS (Newton):
  θ_{k+1} = θ_k − H⁻¹ ∇L    (H = Hessian)
  This minimizes the second-order Taylor expansion — a quadratic variational problem.
```

### Natural Gradient

Standard gradient descent uses the Euclidean metric in parameter space. For probability distributions P(x; θ), the **natural gradient** uses the Fisher information metric:

    G(θ)ᵢⱼ = E[∂_i log P × ∂_j log P]    (Fisher information matrix)

The natural gradient:

    θ̃ = G(θ)⁻¹ ∇L(θ)

This corresponds to steepest descent in the Riemannian manifold of distributions (information geometry). The gradient flow:

    dθ/dt = −G(θ)⁻¹ ∇_θ L

is a gradient flow in the Wasserstein metric on the space of distributions — connecting to optimal transport.

---

## Neural ODEs as Variational Problems

**Chen et al. (2018)**: A neural ODE defines a continuous-depth network by an ODE:

    dz(t)/dt = f_θ(z(t), t)    z(0) = z_input,    output = z(T)

```
NEURAL ODE STRUCTURE:

  Discrete (ResNet):   z_{k+1} = z_k + f_θ_k(z_k)    (Euler step)
                       ↕
  Continuous (NeuralODE): ż = f_θ(z, t)               (ODE, shared θ)

  ANALOGY:
  Discrete ResNet ↔ Explicit Euler discretization of ODE
  As layer depth → ∞ and step size → 0: ResNet → Neural ODE.

  PONTRYAGIN STRUCTURE:
  z(t) is the STATE,  f_θ is the DYNAMICS.
  Training NeuralODE = optimal control problem:
    Minimize loss L(z(T))
    Subject to: ż = f_θ(z,t),  z(0) = z_input
    Control: parameters θ (or: control u(t) = f_θ(z,t))
```

**Adjoint method for Neural ODE gradients**: From the Pontryagin Maximum Principle (see 08-OPTIMAL-CONTROL.md), the gradient of L(z(T)) with respect to the initial state and parameters requires an adjoint ODE solved backward in time:

    da(t)/dt = −a(t) ∂f/∂z    a(T) = ∂L/∂z(T)    (backward costate/adjoint)

    dL/dθ = ∫₀^T a(t) ∂f/∂θ dt

This is the **continuous-time backpropagation** — the adjoint method = BPTT in continuous limit.

```
ADJOINT METHOD = CONTINUOUS BACKPROP:

  DISCRETE (ResNet):
  Forward: z₀ → z₁ → ... → z_T
  Backward: δz_T → δz_{T-1} → ... → δz_0   (reverse chain rule)
  Gradient: ∂L/∂θ_k = δz_{k+1} × ∂f_{θ_k}/∂θ_k

  CONTINUOUS (NeuralODE):
  Forward: ż = f_θ(z,t)  [integrate forward, ODE solver]
  Backward: ȧ = −aᵀ ∂f/∂z  [adjoint ODE, integrate backward]
  Gradient: dL/dθ = ∫₀^T aᵀ ∂f/∂θ dt

  ADVANTAGE: O(1) memory (no stored activations) — just run backward ODE.
  COST: Two ODE solves per training step.
```

---

## Optimal Transport as a Variational Problem

**Monge-Kantorovich problem**: Given two probability distributions μ (source) and ν (target), find the transport plan π(x, y) (coupling of μ and ν) that minimizes the expected transport cost:

    W_p^p(μ, ν) = inf_{π ∈ Π(μ,ν)} ∫∫ c(x, y) dπ(x, y)

where c(x, y) = |x − y|^p is the cost of moving mass from x to y, and Π(μ, ν) is the set of joint distributions with marginals μ and ν.

**Wasserstein distance**: W_p(μ, ν) = [W_p^p(μ, ν)]^{1/p} is a metric on probability distributions.

```
MONGE PROBLEM (original, 1781):
  Find a deterministic map T: ℝ^d → ℝ^d such that T#μ = ν (pushforward),
  minimizing ∫ c(x, T(x)) dμ(x).

  For c(x,y) = |x−y|²: T is the gradient of a convex function T = ∇φ.
  Brenier's theorem (1991): THE solution is T(x) = ∇φ(x) where φ satisfies
  the Monge-Ampère equation: det(∇²φ(x)) = μ(x)/ν(∇φ(x)).

KANTOROVICH RELAXATION:
  Relax to joint distributions (transport plans):
  min_{π ≥ 0}  ∫∫ c(x,y) dπ(x,y)
  subject to: ∫ dπ(x,y) = dμ(x)  and  ∫ dπ(x,y) = dν(y)

  This is a LINEAR PROGRAM — convex, solvable via duality.

KANTOROVICH DUAL (Wasserstein-2):
  W₂²(μ,ν) = sup_{φ convex} [∫ φ dμ − ∫ φ* dν]
  where φ*(y) = sup_x [⟨x,y⟩ − φ(x)] is the convex conjugate.
  This is a VARIATIONAL PROBLEM over convex functions φ.
```

**Benamou-Brenier formula**: Wasserstein-2 distance has a fluid mechanics interpretation:

    W₂²(μ, ν) = inf_{ρ(t,x), v(t,x)} ∫₀^1 ∫ |v(t,x)|² dρ(t,x) dt

where the infimum is over all density-velocity pairs (ρ, v) satisfying the continuity equation ∂_t ρ + ∇·(ρv) = 0 with ρ(0) = μ and ρ(1) = ν.

This is an action principle: the Wasserstein geodesic minimizes the kinetic energy of the transport flow.

---

## Variational Autoencoders

The VAE (Kingma-Welling 2013) solves a variational problem over distributions.

**Setup**: Observed data x, latent variable z. Model: prior P(z), decoder P(x|z; θ). Goal: maximize log P(x) = log ∫ P(x|z; θ) P(z) dz (intractable integral).

**Variational bound**: Introduce encoder Q(z|x; φ) (approximate posterior).

    log P(x) ≥ ELBO(θ, φ; x)
              = E_{Q(z|x;φ)} [log P(x|z; θ)] − KL(Q(z|x;φ) || P(z))

```
ELBO AS VARIATIONAL FREE ENERGY:

  ELBO(θ,φ;x) = E_Q[log P(x|z; θ)]   −   KL(Q(z|x;φ) || P(z))
               = reconstruction term  −   regularization term

  VARIATIONAL STRUCTURE:
  log P(x) = ELBO + KL(Q||P(z|x))
             ↕
  True posterior P(z|x) ↔ Ground truth potential
  Approximate Q(z|x; φ) ↔ Variational ansatz
  KL divergence          ↔ Error in variational approximation
  ELBO = log P(x) − KL  ↔ Φ(Q) = −F[Q] (negative free energy)

  Maximizing ELBO over φ → Q → P(z|x) (minimize KL gap).
  Maximizing ELBO over θ → better generative model.

  THE REPARAMETERIZATION TRICK:
  Sample z ~ Q(z|x; φ) = N(μ_φ(x), σ_φ(x)) as z = μ + σ ε, ε ~ N(0,I).
  Now E_Q[f(z)] is differentiable in φ.
  This is a CHANGE OF VARIABLES in the variational integral.
```

**Connection to optimal transport**: The VAE KL regularization term can be replaced by a Wasserstein distance, giving the Wasserstein autoencoder (WAE). The ELBO becomes a transport cost, and the variational problem becomes optimal transport.

---

## Lagrangian Neural Networks

**Greydanus et al. (2019)**: A neural network that learns the Lagrangian L(q, q̇) directly from trajectory data, then derives the equations of motion via Euler-Lagrange.

**Structure**:
1. Neural network L_θ(q, q̇) (unconstrained)
2. Dynamics derived from E-L: d/dt(∂L_θ/∂q̇) − ∂L_θ/∂q = 0
3. Solve for q̈:  q̈ = (∂²L_θ/∂q̇²)⁻¹ [∂L_θ/∂q − (∂²L_θ/∂q∂q̇) q̇]

```
LAGRANGIAN NN vs STANDARD NN:

  STANDARD NN:
  Learn f(q, q̇) → q̈ directly (black box).
  No structural constraint — can violate energy conservation.

  LAGRANGIAN NN:
  Learn L(q, q̇) → derive q̈ via E-L (structure-preserving).
  Automatically satisfies Noether's theorem:
  If L doesn't depend on qᵢ: ∂L/∂q̇ᵢ = const (conserved momentum).
  If L doesn't depend on t: total energy E = q̇ᵢ ∂L/∂q̇ᵢ − L is conserved.

  HAMILTONIAN NN (Greydanus et al.):
  Learn H(q, p) → derive dynamics via Hamilton's equations.
  ṗ = −∂H/∂q,  q̇ = ∂H/∂p
  Symplectic structure preserved: phase space volume is conserved.
  Better long-term energy conservation than Lagrangian NN.
```

---

## Schrödinger Bridge and Diffusion Models

The **Schrödinger bridge problem**: Given two distributions μ₀ and μ₁, find the stochastic process that "interpolates" between them with the minimum amount of randomness (minimum KL divergence from Brownian motion).

    min_{P : P₀=μ₀, P₁=μ₁} KL(P || W)    (W = Wiener measure)

This is a variational problem over stochastic processes — a "stochastic optimal transport."

**Connection to diffusion models** (DDPM, score matching):

```
DIFFUSION MODEL = STOCHASTIC OPTIMAL TRANSPORT:

  Forward process: x₀ → x_T (add noise to data over T steps)
  Reverse process: x_T → x₀ (remove noise = generate data)

  The reverse process is the time-reversal of the forward diffusion:
  ẋ = f(x,t) − g²(t) ∇_x log p_t(x)   [reverse SDE]
  where ∇_x log p_t(x) is the SCORE FUNCTION.

  SCORE MATCHING: train a network s_θ(x,t) ≈ ∇_x log p_t(x).
  Loss: E[‖s_θ(x_t,t) − ∇ log p_t(x_t|x_0)‖²]
  This is a variational functional minimization over s_θ.

  VARIATIONAL STRUCTURE:
  The diffusion process minimizes a stochastic action functional.
  Schrödinger bridge = constrained minimum-entropy stochastic process.
  DDPM ≈ time-reversed Ornstein-Uhlenbeck process.
  The score function ∇ log p(x) = −∇U (gradient of log density = energy force).
```

---

## Implicit Bias and the Variational Perspective on Generalization

Why does gradient descent on overparameterized networks generalize despite having enough parameters to memorize training data? The variational perspective provides insight.

**Implicit bias of gradient descent**: Among all neural network functions f_θ that achieve zero training loss, gradient descent converges to the one that minimizes a particular norm — determined by the network architecture.

```
IMPLICIT VARIATIONAL PROBLEM:

  For a two-layer neural net: gradient descent finds the minimum-norm
  function in the RKHS of the neural tangent kernel.

  For deep linear networks: gradient descent finds the minimum nuclear
  norm (sum of singular values) solution.

  For shallow networks: Barron's theorem — shallow networks can approximate
  any function f with bounded ‖f̂‖₁ (Fourier norm), with error O(1/√n).
  This is a variational approximation problem.

  INTERPRETATION:
  Training ≡ constrained optimization
  Loss = 0 constraint
  Implicit functional to minimize: ‖f‖_K (RKHS norm)
  Gradient descent is doing the variational minimization implicitly.

  RIDGE REGRESSION ANALOGY:
  Standard regression: min_θ ‖y − Xθ‖² + λ‖θ‖²
  This minimizes a quadratic functional (E-L: (XᵀX + λI)θ = Xᵀy)
  Deep learning implicit regularization = analogous functional minimization,
  but for the minimum-norm interpolant (λ → 0).
```

---

## Decision Cheat Sheet

| ML Problem | Variational Formulation | Key Object |
|-----------|------------------------|-----------|
| Gradient descent | Gradient flow dθ/dt = −∇L | Euler-Lagrange of L[θ(t)] |
| Momentum optimization | Damped Hamiltonian dynamics | Lagrangian ½|θ̇|² − L |
| Neural ODE training | Optimal control (Pontryagin) | Adjoint ODE (backward) |
| Natural gradient | Riemannian gradient flow | Fisher information metric G |
| Optimal transport | Monge-Kantorovich problem | Kantorovich dual (convex conjugate) |
| Wasserstein distance | Kinetic energy action | Benamou-Brenier formula |
| VAE training | Maximize ELBO = −F[Q] | Variational free energy |
| Lagrangian NN | Learn Lagrangian L(q,q̇) | Euler-Lagrange derivatives |
| Hamiltonian NN | Learn Hamiltonian H(q,p) | Hamilton's equations |
| Diffusion model | Schrödinger bridge | Reverse SDE with score function |
| Generalization | Implicit variational problem | Minimum-norm interpolant |

---

## Common Confusion Points

**Backpropagation IS the adjoint method, not just "similar to it"**: The chain rule for computing ∂L/∂θ through a neural network is exactly the discrete adjoint method (costate equation) of optimal control theory. The "backward pass" in backprop is the backward integration of the costate ODE. This was recognized independently in control theory (Bryson-Frazier, 1960s) and neural networks (Rumelhart-Hinton-Williams, 1986).

**Wasserstein distance is not the same as KL divergence for comparing distributions**: KL divergence is not a metric (asymmetric, infinite if supports differ), while Wasserstein distance is a proper metric on distributions with finite moments. KL measures "information difference"; Wasserstein measures "transport cost." For smooth distributions near each other, W₂² ≈ Fisher-Rao metric. They are both variational — the infimum/supremum formulations are dual to each other.

**The ELBO lower bounds log P(x) — but training maximizes it, not log P(x)**: The ELBO = log P(x) − KL(Q||P(z|x)). Maximizing ELBO over φ minimizes the KL gap. Maximizing over θ increases log P(x) and simultaneously brings Q closer to P(z|x). The bound is tight only when Q = P(z|x), which is generally impossible for a simple Gaussian encoder against a complex posterior.

**Neural ODEs are not more general than deep networks — just parameterize differently**: A Neural ODE with T time steps and a smooth f_θ is approximated by an ODE solver, which uses many function evaluations. The total computation is similar to a ResNet with comparable depth. The advantage is memory efficiency (adjoint method) and the ability to use adaptive ODE solvers that place evaluations where the dynamics changes rapidly.
