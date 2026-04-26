# Reinforcement Learning
## MDPs, Bellman Equations, Policy Gradients, and Modern Deep RL

```
THE RL FRAMEWORK

  ┌───────────────────────────────────────────────────────┐
  │                                                         │
  │   Agent ──action aₜ──► Environment                    │
  │      ▲                      │                         │
  │      │ state sₜ₊₁           │                         │
  │      │ reward rₜ₊₁          │                         │
  │      └──────────────────────┘                         │
  │                                                         │
  │  Goal: maximize E[Σ γᵗ rₜ]                             │
  │                                                         │
  │  Three classes:                                         │
  │    Value-based:   learn V* or Q*, derive policy        │
  │    Policy-based:  directly optimize policy π           │
  │    Actor-Critic:  both simultaneously                  │
  └───────────────────────────────────────────────────────┘
```

---

## 1. Markov Decision Process — Formal Definition

**MDP**: (S, A, P, R, γ)
```
  S:      state space
  A:      action space
  P(s'|s,a): transition dynamics
  R(s,a,s'): reward function
  γ ∈ [0,1): discount factor

  Markov property: P(sₜ₊₁ | sₜ, aₜ, sₜ₋₁, ...) = P(sₜ₊₁ | sₜ, aₜ)
  The future depends only on the current state, not history.
```

**Policy**: π(a|s) — probability distribution over actions given state.
- Deterministic: π: S → A
- Stochastic: π: S → Δ(A)

**Return**: `G_t = Σ_{k=0}^∞ γᵏ rₜ₊ₖ₊₁` — discounted sum of future rewards.

**Why discount?**
- Financial: future rewards worth less (time preference)
- Mathematical: ensures G_t is finite for infinite-horizon problems
- γ → 1: longer-horizon planning; γ → 0: myopic (greedy)

---

## Operations Research / Control Theory Bridge

Anyone with an OR, control theory, or quantitative finance background already knows
the Bellman framework under different names:

```
Operations Research / Control Theory            RL / ML vocabulary
───────────────────────────────────────────     ────────────────────────────────────────
Stochastic dynamic program (Bellman 1952)       Markov Decision Process (MDP)
  State variable s_t                              State s ∈ S
  Decision variable u_t                           Action a ∈ A
  System dynamics f(s,u,w) (w = noise)            Transition P(s'|s,a)
  Stage reward g_t(s,u)                           Reward R(s,a)

Backward induction (finite horizon DP)          Value iteration (infinite horizon)
  Vₙ(s) = max_u [ g(s,u) + E[V_{n+1}(f(s,u,w)) ]  V(s) = max_a Σ P(s'|s,a)[R + γV(s')]

Contraction mapping (Banach fixed point)        Bellman operator is γ-contraction
  T is contraction ⟹ unique fixed point V*       → guaranteed convergence to V*
  Geometric convergence rate                      Same proof, same rate

Hamilton-Jacobi-Bellman (HJB) equation         Continuous-time Bellman equation
  ∂V/∂t + max_u[ f(x,u)·∇V + L(x,u) ] = 0     (Bellman in continuous time)
  Used in: LQR, stochastic control (Itô)         Connects RL to control theory

Discount factor in NPV analysis                 Discount factor γ in RL
  V = Σₜ (1/(1+r))^t · CF_t                     G_t = Σₖ γᵏ r_{t+k}
  r = discount rate = time value of money        γ ∈ [0,1) = time preference parameter
  r small → long horizon; r large → myopic       γ→1 long horizon; γ→0 myopic

Linear Quadratic Regulator (LQR)                Model-based RL with linear dynamics
  Minimize Σ (xᵀQx + uᵀRu)                      Quadratic cost ↔ quadratic reward
  Solved by Riccati equation                     Exact solution exists; rare in practice

Policy evaluation (solve V for fixed π)         Policy evaluation = linear system
  V^π = (I - γPπ)^{-1} r_π                      Same equation: iterate or solve directly
```

The core contribution of the RL literature is scaling these ideas to large/continuous
state spaces using function approximation (neural networks) and handling the case
where the model P is unknown (model-free learning).

---

## 2. Value Functions and Bellman Equations

**State-value function**: `V^π(s) = E_π[G_t | sₜ = s]`

**Action-value function**: `Q^π(s,a) = E_π[G_t | sₜ = s, aₜ = a]`

**Bellman expectation equations**:
```
V^π(s)   = Σ_a π(a|s) Σ_{s'} P(s'|s,a) [R(s,a,s') + γ V^π(s')]

Q^π(s,a) = Σ_{s'} P(s'|s,a) [R(s,a,s') + γ Σ_{a'} π(a'|s') Q^π(s',a')]
```

**Bellman optimality equations** (for optimal policy π*):
```
V*(s)   = max_a Σ_{s'} P(s'|s,a) [R(s,a,s') + γ V*(s')]

Q*(s,a) = Σ_{s'} P(s'|s,a) [R(s,a,s') + γ max_{a'} Q*(s',a')]

Optimal policy: π*(s) = argmax_a Q*(s,a)
```

**Key insight**: Bellman optimality equations are a system of n equations in n unknowns (one per state). Can be solved by dynamic programming.

**Contraction mapping**: the Bellman optimality operator T is a γ-contraction:
```
‖TV - TV'‖_∞ ≤ γ‖V - V'‖_∞

→ unique fixed point V* (Banach fixed point theorem)
→ iterating T converges geometrically to V*
```

---

## 3. Dynamic Programming

Exact solutions when model P is known.

### Value Iteration
```
  Initialize V(s) = 0 ∀s
  Repeat until convergence:
    V(s) ← max_a Σ_{s'} P(s'|s,a) [R(s,a,s') + γ V(s')]

  Complexity per sweep: O(|S|² |A|)
  Convergence: ‖V_k - V*‖_∞ ≤ γᵏ ‖V_0 - V*‖_∞
```

### Policy Iteration
```
  1. Policy evaluation: solve V^π (linear system or repeated application)
  2. Policy improvement: π'(s) = argmax_a Q^π(s,a)
  3. Repeat until π' = π

  Convergence: finite (|S|^|A| policies, each step strictly improves)
  In practice: faster convergence than value iteration for same accuracy
```

**Policy gradient theorem** foreshadowing: if |S| is too large or continuous, you can't enumerate all states. Need function approximation.

---

## 4. Temporal Difference Learning

**TD(0)** — online, model-free V learning:
```
  V(sₜ) ← V(sₜ) + α [rₜ₊₁ + γ V(sₜ₊₁) - V(sₜ)]
                     └────────────────────────────┘
                               TD target - current estimate = TD error δₜ
```

**TD error** δₜ = rₜ₊₁ + γ V(sₜ₊₁) - V(sₜ):
- Positive: transition was better than expected → increase V(sₜ)
- Negative: worse than expected → decrease V(sₜ)
- δₜ = 0: value estimates are consistent (Bellman equation holds)

**Bootstrap vs Monte Carlo**:
```
  Monte Carlo: G_t = rₜ₊₁ + γrₜ₊₂ + ... (wait for episode end)
    - Unbiased estimate of V^π(s)
    - High variance (long sum of random variables)

  TD: use rₜ₊₁ + γ V(sₜ₊₁) (one-step bootstrap)
    - Biased (V is approximate)
    - Lower variance (one step)

  TD(λ): interpolate with eligibility traces
    G_t^λ = (1-λ) Σ_{n=1}^∞ λ^{n-1} G_t^{(n)}
    λ=0 → TD(0), λ=1 → Monte Carlo
```

---

## 5. Q-Learning and DQN

**Q-learning** (Watkins 1989) — off-policy TD for Q*:
```
  Q(sₜ, aₜ) ← Q(sₜ, aₜ) + α [rₜ₊₁ + γ max_{a'} Q(sₜ₊₁, a') - Q(sₜ, aₜ)]
                                └────────────────────────────────────────────┘
                                                  TD target (using greedy policy)
```

**Off-policy**: the target uses `max_{a'} Q(sₜ₊₁, a')` regardless of the behavior policy. Learn Q* while following any exploration policy.

**Convergence**: Q-learning converges to Q* under tabular setting with:
- All (s,a) visited infinitely often
- Step sizes satisfying Robbins-Monro: Σαₜ = ∞, Σαₜ² < ∞

**Deep Q-Network (DQN)** (Mnih et al. 2015):
```
  Q(s, a; θ) ← neural network approximating Q*

  Two critical tricks for stability:
  1. Experience Replay:
       Store (sₜ, aₜ, rₜ₊₁, sₜ₊₁) in replay buffer D
       Sample random mini-batch for updates
       Breaks temporal correlations → stable training

  2. Target Network:
       Use separate network Q(·; θ⁻) for TD targets
       θ⁻ updated slowly (copy every C steps)
       Prevents "chasing a moving target" → stable targets

  Loss: L(θ) = E_{(s,a,r,s')~D}[(r + γ max_{a'} Q(s',a'; θ⁻) - Q(s,a; θ))²]
```

**Double DQN**: `max_{a'} Q(s',a'; θ)` can overestimate. Fix:
```
  a* = argmax_{a'} Q(s',a'; θ)          ← select with online network
  target = r + γ Q(s', a*; θ⁻)         ← evaluate with target network
```

---

## 6. Policy Gradient Methods

**Direct optimization**: instead of learning V/Q and deriving π, directly optimize `J(θ) = E_{τ~π_θ}[G(τ)]`.

**Policy gradient theorem** (Sutton et al. 1999):
```
  ∇_θ J(θ) = E_{τ~π_θ}[ Σₜ ∇_θ log π_θ(aₜ|sₜ) · G_t ]

  Proof sketch:
    J(θ) = Σ_τ p(τ; θ) R(τ)
    ∇J = Σ_τ ∇p(τ;θ) R(τ)
       = Σ_τ p(τ;θ) ∇log p(τ;θ) R(τ)    (log-derivative trick)
       = E_τ[ ∇log p(τ;θ) R(τ) ]
       = E_τ[ Σₜ ∇log π_θ(aₜ|sₜ) · R(τ) ]   (only π depends on θ)
```

**REINFORCE** (Monte Carlo policy gradient):
```
  Collect trajectory τ, compute G_t
  θ ← θ + α Σₜ ∇_θ log π_θ(aₜ|sₜ) G_t
```

**Baseline**: subtract a state-dependent baseline b(s) to reduce variance:
```
  ∇J = E[ Σₜ ∇log π_θ(aₜ|sₜ) (G_t - b(sₜ)) ]
  Unbiased: E[∇log π · b(s)] = 0 (b independent of a)
  Optimal baseline: b(s) = V^π(s) → advantage A(s,a) = Q(s,a) - V(s)
```

**Advantage function**: A^π(s,a) = Q^π(s,a) - V^π(s)
- A > 0: action a is better than average for state s
- A < 0: action a is worse than average

---

## 7. Actor-Critic Methods

Combine policy (actor) and value function (critic):

```
  Actor:  π_θ(a|s)     ← policy, updated by policy gradient
  Critic: V_φ(s) or Q_φ(s,a)  ← value function, updated by TD

  Actor update:  θ ← θ + α ∇_θ log π_θ(aₜ|sₜ) δₜ
  Critic update: φ ← φ - α ∇_φ (δₜ)²     where δₜ = rₜ + γV_φ(sₜ₊₁) - V_φ(sₜ)
```

**A3C** (Asynchronous Advantage Actor-Critic): multiple parallel actors, each interacting with a copy of the environment. Asynchronous gradient updates to shared network. Variance reduced via advantage estimation.

**GAE (Generalized Advantage Estimation)**:
```
  δₜ = rₜ + γ V(sₜ₊₁) - V(sₜ)    1-step TD error

  Â_t^{GAE(γ,λ)} = Σ_{l=0}^∞ (γλ)^l δₜ₊ₗ

  λ=0 → 1-step TD estimate (low variance, high bias)
  λ=1 → Monte Carlo (high variance, low bias)
  λ≈0.95 in practice (PPO default)
```

---

## 8. PPO — Proximal Policy Optimization

**Problem with vanilla policy gradients**: too large an update can collapse performance, and you can't reuse data (on-policy requirement).

**TRPO** (Trust Region Policy Optimization): constrain KL divergence:
```
  max_θ E[r_t(θ) Â_t]   subject to  E[D_KL(π_old ‖ π_θ)] ≤ δ

  where r_t(θ) = π_θ(aₜ|sₜ) / π_old(aₜ|sₜ)  (importance sampling ratio)
```

**PPO** (Schulman et al. 2017): approximation of TRPO without constraint solver:
```
  L^{CLIP}(θ) = E_t[ min(r_t(θ) Â_t,  clip(r_t(θ), 1-ε, 1+ε) Â_t) ]

  If Â_t > 0 (good action):  don't let r_t grow too far beyond 1+ε
  If Â_t < 0 (bad action):   don't let r_t shrink too far below 1-ε

  ε ≈ 0.2 in practice.

  Full objective:
  L(θ) = L^{CLIP}(θ) - c₁ L^{VF}(θ) + c₂ H[π_θ](sₜ)
              ↑               ↑                 ↑
         policy loss    value loss        entropy bonus (exploration)
```

**Why PPO dominates**:
- Simple to implement, no constraint solver
- Stable: clipping prevents catastrophic updates
- Sample efficient: can take multiple gradient steps on same batch (within trust region)
- Default RL algorithm for most applications

---

## 9. SAC — Soft Actor-Critic (Maximum Entropy RL)

**Maximum entropy objective**:
```
  J(π) = Σₜ E_{(sₜ,aₜ)~π}[ R(sₜ,aₜ) + α H(π(·|sₜ)) ]
                                              ↑
                                      entropy bonus: prefer uncertain policies

  Temperature α: tradeoff between reward maximization and entropy
  α → 0: standard RL; α → ∞: uniform random policy
```

**Soft Bellman equations**:
```
  V_soft(s)   = E_a[ Q_soft(s,a) - α log π(a|s) ]
  Q_soft(s,a) = R(s,a) + γ E_{s'}[ V_soft(s') ]
```

**SAC algorithm**:
```
  Off-policy actor-critic with:
  - Replay buffer (like DQN)
  - Two Q-networks (min of both to reduce overestimation)
  - Soft policy update: π_θ(·|s) = argmin_π D_KL(π ‖ exp(Q/α))
  - Automatic temperature tuning: minimize -α(log π(aₜ|sₜ) + H_target)
```

**SAC vs PPO**:
| | PPO | SAC |
|--|-----|-----|
| On/off-policy | On-policy | Off-policy |
| Sample efficiency | Moderate | High |
| Stability | Very stable | Stable |
| Continuous actions | ✅ | ✅ (designed for) |
| Discrete actions | ✅ | More complex |
| Hyperparameter sensitivity | Low | Moderate |

---

## 10. RLHF — RL from Human Feedback

The bridge from RL to LLMs:

```
  Phase 1: Supervised Fine-Tuning (SFT)
    Train base LLM on high-quality demonstrations
    → SFT model π_SFT

  Phase 2: Reward Model Training
    Collect human preference data: (prompt, response A, response B, preference)
    Train reward model r_φ(s, a) to predict human preference
    Bradley-Terry model: P(A > B) = σ(r(A) - r(B))
    Loss: -E[log σ(r(yw) - r(yl))]   (yw=winner, yl=loser)

  Phase 3: RL Fine-Tuning (PPO)
    max_θ E_{s~prompts, a~π_θ}[ r_φ(s,a) - β D_KL(π_θ ‖ π_SFT) ]
                                    ↑                    ↑
                            reward model              KL penalty (stay near SFT)
```

**Why KL penalty**: without it, policy exploits reward model (reward hacking). Keep policy near the reference model to prevent degenerate outputs.

**DPO (Direct Preference Optimization)**: eliminates RL entirely. Closed-form optimal policy given preference data:
```
  L_{DPO}(θ) = -E[ log σ( β log (π_θ(yw)/π_ref(yw)) - β log (π_θ(yl)/π_ref(yl)) ) ]
```

Equivalent to RLHF but more stable, no reward model needed.

---

## 11. Decision Cheat Sheet

| Method | Model-free? | On/off-policy | Continuous actions | When to use |
|--------|------------|---------------|-------------------|-------------|
| Value iteration / PI | No (model needed) | — | ❌ | Known tabular MDP |
| Q-learning / DQN | Yes | Off | ❌ (discrete) | Discrete action games |
| REINFORCE | Yes | On | ✅ | Simple, low-dim |
| A2C/A3C | Yes | On | ✅ | Parallelizable envs |
| PPO | Yes | On | ✅ | General default |
| SAC | Yes | Off | ✅ (designed for) | Continuous robotics |
| RLHF/DPO | Yes | Both | ✅ (language) | LLM alignment |

---

## 12. Common Confusion Points

1. **"Q-learning is off-policy because it uses a replay buffer"** — Q-learning is off-policy because its target uses `max_a Q(s',a)` regardless of the behavior policy. Replay buffer enables off-policy learning but isn't the definition.

2. **"Policy gradients are on-policy, so they're less efficient"** — On-policy methods can only use data from the current policy. PPO's clipped objective allows multiple mini-batches from one rollout, improving efficiency. SAC (off-policy) can reuse all past data.

3. **"High entropy = exploration"** — Maximum entropy RL seeks a policy that is stochastic (high entropy) while also getting high reward. This isn't the same as random exploration. The entropy bonus prevents premature commitment to suboptimal deterministic policies.

4. **"RLHF trains the model to please humans"** — RLHF trains the model to score well on the reward model, which itself was trained to predict human preferences. Reward hacking (getting high scores via reward model flaws) is a real failure mode.

5. **"The Bellman equation is always the right framework"** — Bellman assumes the Markov property. If your state is incomplete (partial observability), you need POMDPs. Transformers use full context as state, partly working around this.

6. **"Actor-critic is just using both V and Q"** — Actor-critic separates the policy (actor, what to do) from the value estimator (critic, how good is this state). The critic provides a baseline/advantage signal. Not quite the same as having both V and Q tables.

7. **"DPO is strictly better than RLHF"** — DPO is simpler and more stable, but RLHF with a separate reward model allows iterative improvement and can handle out-of-distribution prompts differently. Active area of research; neither is definitively superior.
