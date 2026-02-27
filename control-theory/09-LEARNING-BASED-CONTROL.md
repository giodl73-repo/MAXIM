# Learning-Based and Data-Driven Control

## Big Picture: From Models to Data

```
┌─────────────────────────────────────────────────────────────────────┐
│               CONTROL PARADIGM SPECTRUM                             │
│                                                                     │
│  MODEL-BASED          DATA-ASSISTED        DATA-DRIVEN              │
│  ─────────────────    ────────────────     ─────────────────────    │
│  LQR, MPC, H∞        System ID → MPC       RL, Imitation Learning   │
│  Full model known     Model learned         No model required        │
│  Optimal globally     Good if ID correct    Can handle unknowns      │
│  Fragile under        Periodic refit        Learns from interaction  │
│  model mismatch       needed                                         │
│                                                                     │
│  CONNECTIONS TO CLASSICAL THEORY:                                   │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Bellman equation:  V*(x) = min_u [c(x,u) + γ V*(f(x,u))]  │   │
│  │                                                             │   │
│  │  LQR IS RL:  V*(x) = x'Px  (P from Riccati equation)       │   │
│  │              π*(x) = -Kx   (K from P)                      │   │
│  │                                                             │   │
│  │  RL generalizes to: nonlinear f, unknown f, non-quadratic c │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  KEY CHALLENGE: Sample efficiency vs. optimality vs. safety         │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 1. Reinforcement Learning for Control

### Problem Formulation (MDP)

```
  State:   x_t ∈ ℝⁿ  (continuous)
  Action:  u_t ∈ ℝᵐ  (continuous)
  Reward:  r_t = -c(x_t, u_t)        (negative cost = reward)
  Dynamics: x_{t+1} = f(x_t, u_t) + w_t  (unknown or stochastic)

  Policy: π_θ(u|x) — stochastic or deterministic π_θ(x) = u

  Objective: max_θ  E[Σ γᵗ r_t]
             (equivalent to LQR when f is linear, c is quadratic)
```

### Policy Gradient Methods

```
┌──────────────────────────────────────────────────────────────────┐
│  REINFORCE (Monte Carlo policy gradient):                         │
│                                                                   │
│    ∇_θ J = E[Σ_t ∇_θ log π_θ(u_t|x_t) · G_t]                   │
│    G_t = Σ_{k≥t} γᵏ r_k   (return from t)                       │
│                                                                   │
│    Problem: high variance — G_t mixes good/bad actions            │
│                                                                   │
│  ACTOR-CRITIC:                                                    │
│    Actor:   π_θ  — the policy                                     │
│    Critic:  V_φ  — estimates V(x) to reduce variance              │
│    Advantage: A(x,u) = Q(x,u) - V(x) — was this action better    │
│               than average?                                        │
│                                                                   │
│    ∇_θ J ≈ E[∇_θ log π_θ(u|x) · A(x,u)]   (lower variance)     │
└──────────────────────────────────────────────────────────────────┘
```

### PPO and SAC — The Workhorses

```
PPO (Proximal Policy Optimization):
  Clip objective: L = E[min(r_t A_t, clip(r_t, 1-ε, 1+ε) A_t)]
  r_t = π_θ(u|x) / π_θ_old(u|x)  (importance ratio)
  Clip prevents large policy updates → stable training
  On-policy: must collect new data after each update

SAC (Soft Actor-Critic):
  Off-policy — reuses experience replay buffer
  Entropy-regularized: max E[Σ γᵗ (r_t + α H(π(·|x_t)))]
  Encourages exploration automatically
  Temperature α: controls exploration/exploitation tradeoff
  Near-SOTA for continuous control benchmarks

  COMPARISON:
  ┌─────────────────┬──────────┬───────────────┬───────────────┐
  │ Method          │ Policy   │ Sample Eff.   │ Stability     │
  ├─────────────────┼──────────┼───────────────┼───────────────┤
  │ PPO             │ On-policy│ Moderate      │ Very stable   │
  │ SAC             │ Off-pol. │ High          │ Stable        │
  │ TD3             │ Off-pol. │ High          │ Stable        │
  │ DDPG            │ Off-pol. │ High          │ Fragile       │
  └─────────────────┴──────────┴───────────────┴───────────────┘
```

---

## 2. Model-Based RL

```
┌─────────────────────────────────────────────────────────────────┐
│  MODEL-FREE RL:  x_t → [env] → r_t, x_{t+1}   (black box)     │
│  MODEL-BASED RL: x_t → [learned f̂] → x_{t+1}  (white box)    │
│                                                                 │
│  MBRL LOOP:                                                     │
│    1. Collect real data: D = {(x,u,x',r)}                      │
│    2. Train dynamics model: f̂_φ(x,u) ≈ x'                     │
│    3. Plan/optimize inside model (rollouts, MPC, policy search) │
│    4. Execute on real system, collect more data                 │
│    5. Repeat                                                    │
│                                                                 │
│  DYNA architecture (Sutton 1990):                               │
│    Real experience → Q-function updates                         │
│    Model rollouts  → Q-function updates (cheap "hallucinated")  │
│                                                                 │
│  DREAMER (world models in latent space):                        │
│    Encode: x_t → h_t  (latent state)                           │
│    Model:  h_t → h_{t+1}  (transition in latent space)         │
│    Policy: h_t → u_t      (act in latent space)                │
│    Value:  h_t → V        (predict in latent space)            │
│    10-100x more sample efficient than model-free for some tasks │
└─────────────────────────────────────────────────────────────────┘
```

### Gaussian Processes for Control

```
  GP dynamics model: f(x,u) ~ GP(μ(x,u), k((x,u),(x',u')))

  Advantages:
  - Uncertainty quantification: σ²(x,u) tells you where model is wrong
  - Principled exploration: go where σ² is large (GP-UCB)
  - Sample efficient: 10s–100s of rollouts vs. 10,000s for model-free

  Disadvantages:
  - O(n³) training, O(n²) prediction (sparse GP approximations help)
  - Kernel choice matters — poor generalization outside training data

  PILCO (Probabilistic Inference for Learning COntrol):
  - GP dynamics + analytical policy gradient through model
  - Achieves minutes of real-world training (cart-pole, etc.)
  - Benchmark for sample efficiency
```

---

## 3. Neural Network Controllers

### Universal Approximation for Control

```
  θ*(x) ≈ π_θ(x)  where π_θ is a neural network

  PROBLEM: Stability guarantees vanish
  Classical: Lyapunov V(x) > 0, V̇(x) < 0 → proven stable
  NN policy: No guarantee without additional structure

  STRUCTURED NN CONTROLLERS:
  ┌──────────────────────────────────────────────────────────────┐
  │  Neural Lyapunov (Yudong Chen, 2019):                        │
  │    V_φ(x): NN trained to satisfy Lyapunov conditions         │
  │    Verify: V(0)=0, V(x)>0, V̇(x)=-ε·V(x)                   │
  │    Policy π certified stable in learned region-of-attraction │
  │                                                              │
  │  Input Convex NN (ICNN):                                     │
  │    V(x) = convex(x) → optimization problems stay tractable   │
  │    Used in MPC: replace quadratic cost with learned ICNN     │
  │                                                              │
  │  Koopman Operator Linearization:                             │
  │    φ(x): lift to high-dim feature space                      │
  │    K·φ(x) ≈ φ(f(x))  (linear dynamics in feature space)    │
  │    Apply linear LQR/MPC to Koopman-linearized system         │
  └──────────────────────────────────────────────────────────────┘
```

---

## 4. Safe Reinforcement Learning

### The Core Problem

```
  Standard RL: max E[Σ r_t]  — ignores constraints
  Safe RL:     max E[Σ r_t]  s.t. E[Σ c_t] ≤ d

  Constraint: c_t = 1 if unsafe, 0 otherwise (collision, joint limit, etc.)
```

### Control Barrier Functions + RL

```
┌─────────────────────────────────────────────────────────────────┐
│  CBF SAFETY FILTER ARCHITECTURE:                                │
│                                                                 │
│    RL Policy → u_nominal                                        │
│         ↓                                                       │
│    CBF Filter: solve min ||u - u_nominal||²                     │
│                       s.t. ḣ(x) + α(h(x)) ≥ 0                 │
│         ↓                                                       │
│    u_safe → System                                              │
│                                                                 │
│  h(x) ≥ 0 defines safe set (e.g., h = dist_to_obstacle - r)   │
│  CBF condition: if h(x) ≥ 0, then ḣ + αh ≥ 0 keeps h ≥ 0     │
│                                                                 │
│  KEY: Policy can explore freely — CBF intercepts only when      │
│       safety boundary is about to be violated. Minimal          │
│       intervention philosophy.                                  │
│                                                                 │
│  SHIELDING: Discrete-time analog — shield = backup safe policy  │
│  CPO (Constrained Policy Optimization): Lagrangian relaxation   │
│  TRPO-Lagrangian: trust region + constraint satisfaction        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. Imitation Learning and Offline RL

### Behavior Cloning

**Automation bridge:** Behavior cloning's covariate shift problem is the formal version of a well-known failure in CI/CD automation: a trained "auto-merge bot" fails when it encounters states the expert never generated during training. DAgger's fix — let the learned policy generate states, have the expert label them — is shadow mode with human review: run the automated system in shadow, collect cases where it diverges, have humans label those specific cases, retrain.

```
  Given: Expert demonstrations D = {(x_t, u_t*)}
  Goal:  Learn π_θ(x) ≈ u_t*

  Approach: Supervised learning — minimize ||π_θ(x_t) - u_t*||²

  PROBLEM: Covariate shift / compounding errors
  ┌──────────────────────────────────────────────────────────────┐
  │  Training: always in expert state distribution               │
  │  Deployment: small errors → novel states → large errors       │
  │  Example: autonomous driving — 1° heading error compounds    │
  │                                                              │
  │  DAGGER fix (Ross, 2011):                                    │
  │  1. π_θ executes, expert labels states visited by π_θ        │
  │  2. Train on mixed {expert states} ∪ {π_θ states}           │
  │  3. Iteratively expands training distribution                │
  └──────────────────────────────────────────────────────────────┘
```

### Inverse RL and GAIL

```
  IRL: Expert demonstrates → infer reward function → solve MDP
  Given: D_expert, find r* such that π_expert is optimal for r*

  Maximum Entropy IRL (Ziebart, 2008):
    P(τ) ∝ exp(Σ r(x_t, u_t))  — probabilistic model of demos
    Max entropy over trajectories consistent with feature matching

  GAIL (Generative Adversarial Imitation Learning):
    Discriminator D: distinguishes expert vs. policy trajectories
    Policy π: fools discriminator (generate expert-like trajectories)
    Bypass explicit reward function — directly match occupancy measure
    More scalable than IRL for high-dimensional problems

  OFFLINE RL (batch RL):
    Given: fixed dataset D (no new environment interaction)
    Challenge: distributional shift — π_θ may query OOD (s,a) pairs
    CQL (Conservative Q-Learning): penalizes Q-values for OOD actions
    IQL (Implicit Q-Learning): avoids OOD queries entirely
    Use case: robotics (expensive real-world data), healthcare, finance

  Offline RL is the control-theory formalization of learning from production
  logs without the ability to run new experiments — common in regulated
  industries or when A/B tests are too costly. The OOD action problem (policy
  recommends actions absent from training data, where Q-values are unreliable)
  is the same failure mode as recommendation systems confidently suggesting
  items with no engagement history. CQL's conservatism serves the same role
  as UCB exploration bounds in bandit systems: stay close to what you know.
```

---

## 6. Sim-to-Real Transfer

**Staging-to-production bridge:** Sim-to-real is the robotics name for the staging-to-production gap. The strategies map directly: domain randomization (randomize simulator parameters) parallels chaos engineering and environment parity testing; domain adaptation (train discriminator to match sim to real) parallels A/B testing with traffic shaping; residual RL (classical controller + learned correction) parallels conventional autoscaler + anomaly correction layer. The "gap" sources map too: contact dynamics and sensor noise in robotics correspond to network latency variance, instance heterogeneity, and cache warming effects in cloud infrastructure.

```
┌─────────────────────────────────────────────────────────────────┐
│  THE SIM-TO-REAL GAP:                                           │
│                                                                 │
│  Simulation: fast, safe, infinitely many rollouts               │
│  Reality:    slow, expensive, breaks hardware                   │
│  Gap:        contact dynamics, friction, sensor noise,          │
│              actuator delays, model mismatch                    │
│                                                                 │
│  STRATEGIES:                                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Domain Randomization:                                    │  │
│  │  Randomize masses, friction, damping, sensor noise during │  │
│  │  training. Policy learns to be robust to variation.       │  │
│  │  OpenAI Dexterous Hand: 6000 randomized params in sim     │  │
│  │                                                           │  │
│  │  Domain Adaptation:                                       │  │
│  │  Train discriminator: sim vs. real trajectory             │  │
│  │  Adapt sim to match real statistics (GRAIL, SimOpt)       │  │
│  │                                                           │  │
│  │  Meta-Learning (MAML, PEARL):                             │  │
│  │  Learn initialization that adapts quickly to new dynamics │  │
│  │  Few real rollouts → fine-tune policy                     │  │
│  │                                                           │  │
│  │  Residual RL:                                             │  │
│  │  u = u_nominal(classical) + u_residual(RL)               │  │
│  │  RL only corrects the model error                         │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Data-Driven Control Without RL

### System Identification Bridge

```
  Classical pipeline:
    1. PRBS or chirp excitation → collect I/O data
    2. Fit ARX/ARMAX/state-space model (N4SID, PEM)
    3. Validate model on holdout data
    4. Design LQR/MPC/H∞ on identified model

  This is model-based — RL not needed if system is identifiable.

  KOOPMAN OPERATOR METHODS:
    DMD (Dynamic Mode Decomposition):
      X' ≈ A X  (fit linear dynamics from trajectory data)
      SVD-based: A ≈ U Σ V' (X'V Σ⁻¹ U')
      Use for linear prediction, spectral analysis

    EDMD (Extended DMD):
      Lift: ψ(x) = [x, x², sin(x), ...]  (basis functions)
      K ψ(x) ≈ ψ(f(x))  (linear in lifted space)
      Apply LQR/MPC to Koopman-linearized system

  WILLEMS' FUNDAMENTAL LEMMA (Behavioral approach):
    If input u is persistently exciting of order L+n,
    then all length-L trajectories of the LTI system
    lie in the column space of the Hankel matrix H_L(u,y).
    → Control directly from data without explicit model
    → DeePC: MPC formulation using Hankel matrix
```

---

## Decision Cheat Sheet

```
┌───────────────────────────┬────────────────────────────────────────────┐
│  Situation                │  Best Approach                             │
├───────────────────────────┼────────────────────────────────────────────┤
│  Model known, linear,     │  LQR / MPC — no learning needed            │
│  quadratic cost           │                                            │
├───────────────────────────┼────────────────────────────────────────────┤
│  Model unknown, can       │  System ID → model-based control           │
│  excite system safely     │  (N4SID, PEM, DMD + LQR/MPC)              │
├───────────────────────────┼────────────────────────────────────────────┤
│  Model unknown, nonlinear,│  Model-free RL (SAC, PPO)                  │
│  simulator available      │  + domain randomization for sim-to-real    │
├───────────────────────────┼────────────────────────────────────────────┤
│  Sparse real-world data,  │  Model-based RL (PILCO, MBPO) or           │
│  no fast simulator        │  GP + policy search                        │
├───────────────────────────┼────────────────────────────────────────────┤
│  Expert demonstrations    │  Behavior cloning → IRL/GAIL if            │
│  available                │  compounding errors problematic            │
├───────────────────────────┼────────────────────────────────────────────┤
│  Safety-critical system   │  CBF safety filter + any RL policy         │
│                           │  OR: offline RL on safe dataset            │
├───────────────────────────┼────────────────────────────────────────────┤
│  Fixed historical dataset │  Offline RL (IQL, CQL, TD3+BC)             │
│  no new data collection   │                                            │
├───────────────────────────┼────────────────────────────────────────────┤
│  LTI system, trajectory   │  DeePC / Willems-based predictive control  │
│  data only, no model      │                                            │
└───────────────────────────┴────────────────────────────────────────────┘
```

---

## Common Confusion Points

**RL ≠ just neural networks.** Tabular Q-learning is RL. LQR is RL with the Riccati equation as the Bellman solution. The key is the sequential decision-making under uncertainty structure.

**Model-based vs. model-free trade-off isn't about final performance.** Model-based methods are more sample efficient but require accurate models. Model-free asymptotically matches model-based performance given enough data. In practice: use model-based if you have a good simulator, model-free if you don't.

**Behavior cloning is not the same as imitation learning.** BC is supervised learning on demonstrations. IRL infers the reward. GAIL matches occupancy measures. They solve increasingly hard versions of the same problem.

**The Lyapunov stability gap.** Classical controllers have formal stability proofs. RL controllers typically don't. CBF filters patch this locally but don't certify global behavior. Neural Lyapunov functions certify larger regions but training them is hard. This remains an open problem for high-dimensional systems.

**"Safe RL" often means constraint satisfaction, not formal safety.** Constrained MDP methods (CPO, Lagrangian RL) reduce constraint violations in expectation but don't guarantee zero violations. CBF safety filters give hard-constraint guarantees at the cost of performance.

**Sim-to-real is the hardest part.** Algorithms that work in simulation routinely fail in hardware. Domain randomization buys robustness but not guarantees. The gap between benchmark performance (MuJoCo) and real robotics performance remains large.
