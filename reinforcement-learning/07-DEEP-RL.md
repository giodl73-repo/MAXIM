---
maxim_schema: maxim.frontmatter.v1
id: maxim:reinforcement-learning:deep-rl
kind: guide
module: reinforcement-learning
section: reinforcement-learning
title: Deep RL - TRPO, PPO, DDPG/TD3, SAC and Max-Entropy RL
status: source-custody
source_custody: partial
current_path: reinforcement-learning/07-DEEP-RL.md
canonical_path: reinforcement-learning/07-DEEP-RL.md
backsource_ids: [proof-backfill:reinforcement-learning:07-deep-rl, git-history:reinforcement-learning:07-deep-rl]
concepts: [TRPO, PPO, clipped objective, DDPG, TD3, SAC, maximum entropy RL, trust region]
root_concepts: [PPO, SAC]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Deep RL — TRPO, PPO, DDPG/TD3, SAC and Max-Entropy RL

## The Big Picture

Deep RL is policy optimization made *stable* at neural-network scale. Naive policy
gradients take destructively large steps; one bad update collapses the policy and,
because the policy generates its own data, it never recovers. The modern
algorithms are answers to one question: **how do you take the biggest policy
improvement step that is still safe?** Two lineages answer it differently.

```
+------------------------------------------------------------------+
|              TWO LINEAGES OF DEEP POLICY OPTIMIZATION            |
|                                                                  |
|   ON-POLICY (trust region)        OFF-POLICY (deterministic /    |
|   ---------------------            max-entropy actor-critic)     |
|                                   ---------------------------    |
|   constrain step size so the      reuse a replay buffer; learn   |
|   new policy stays CLOSE to old   a Q-critic + an actor          |
|                                                                  |
|   TRPO  -> PPO                    DDPG -> TD3 -> SAC             |
|   (KL trust region -> clip)       (det. PG -> twin-Q -> entropy) |
|                                                                  |
|   stable, simple, sample-hungry   sample-efficient, fiddly       |
+------------------------------------------------------------------+
                                 |
                                 v
+------------------------------------------------------------------+
|   ALL share the ch 06 core:  grad J = E[ grad log pi * A ]       |
|   They differ ONLY in how they CONTROL the update.               |
+------------------------------------------------------------------+
```

**Read it as two answers to step-size control**: trust-region/clipping (keep the
new policy near the old) versus off-policy actor-critic with stabilizers (twin
critics, target networks, entropy).

---

## The Problem: Policy Collapse

```
+------------------------------------------------------------------+
|  WHY VANILLA POLICY GRADIENT IS FRAGILE                          |
|  -------------------------------------                           |
|  - the gradient is in PARAMETER space, but we care about         |
|    POLICY space; a small theta step can be a HUGE policy change  |
|  - one over-large step -> policy collapses to garbage            |
|  - collapsed policy generates garbage data -> no recovery        |
|  (the closed feedback loop has no fixed dataset to fall back on) |
|                                                                  |
|  FIX: limit how far the policy distribution moves per update.    |
+------------------------------------------------------------------+
```

The natural distance between policies is the **KL divergence**, not Euclidean
distance in `theta`. This is the seed of trust-region methods.

---

## TRPO: Trust Region Policy Optimization

TRPO maximizes a surrogate objective subject to a hard KL constraint — the new
policy must stay within a "trust region" of the old one.

```
+------------------------------------------------------------------+
|  TRPO                                                            |
|                                                                  |
|  maximize_theta  E[ ratio * A ]                                  |
|     where ratio r(theta) = pi(a|s;theta) / pi(a|s;theta_old)     |
|                                                                  |
|  subject to     E[ KL( pi_old(.|s) || pi(.|s) ) ]  <=  delta     |
+------------------------------------------------------------------+
```

The importance ratio `r(theta)` lets TRPO evaluate the *new* policy using data
from the *old* one (limited off-policy reuse). It is solved with the natural
gradient (the Fisher information metric) and a conjugate-gradient step — correct
and monotonically improving in theory, but heavy: second-order, complex to
implement.

> Bridge — optimization: the KL constraint induces the *natural gradient*
> (Amari) — steepest ascent in the Fisher-Rao metric of distribution space rather
> than Euclidean parameter space. This is the same information geometry that
> appears in `machine-learning-theory/` and statistics. PPO is the cheap
> first-order approximation that captures most of the benefit.

---

## PPO: The Clipped Objective

PPO (Schulman et al., 2017) keeps TRPO's "stay close to the old policy" intent but
replaces the hard KL constraint with a *clipped* surrogate — first-order, trivial
to implement, and the de-facto default in deep RL and RLHF.

```
+------------------------------------------------------------------+
|  PPO CLIPPED OBJECTIVE                                           |
|                                                                  |
|   r(theta) = pi(a|s;theta) / pi(a|s;theta_old)                   |
|                                                                  |
|   L_CLIP = E[ min(  r(theta) * A,                                |
|                     clip(r(theta), 1-eps, 1+eps) * A ) ]         |
|                                                                  |
|   typical eps = 0.2                                              |
+------------------------------------------------------------------+
```

The mechanism, by sign of the advantage:

```
  A > 0 (good action):   want to INCREASE r. But clip caps it at 1+eps.
                         Past 1+eps, the objective FLATTENS -> no incentive
                         to push the ratio further. Bounded step.

  A < 0 (bad action):    want to DECREASE r. Clip floors it at 1-eps.
                         Below 1-eps, objective flattens -> bounded step.

  the min() makes the clip a PESSIMISTIC bound: it only ever removes
  incentive to move too far; it never rewards a large ratio change.
```

```
   L_CLIP as a function of r (for A>0):

   objective
      |          ____________   <- clipped flat region (no more gain)
      |         /
      |        /
      |_______/______________  r
            1-eps  1   1+eps

   the policy can improve, but only up to the (1+eps) trust boundary.
```

Full PPO objective adds a value-function loss and an entropy bonus:

```
  L = L_CLIP  -  c1 * (v(s) - v_target)^2  +  c2 * H(pi(.|s))
                  ^ critic regression          ^ exploration
```

PPO runs multiple SGD epochs over each batch of on-policy data (the clip makes
this safe), uses GAE for advantages (ch 06), and is the algorithm behind RLHF for
LLMs (ch 09).

### TRPO vs PPO

```
+--------------------------------+--------------------------------+
|  TRPO                          |  PPO                           |
|  ----                          |  ---                           |
|  hard KL constraint            |  clipped ratio (soft)          |
|  second-order (Fisher, CG)     |  first-order SGD               |
|  monotonic-improvement proof   |  heuristic, works great        |
|  complex implementation        |  ~10 lines of objective        |
+--------------------------------+--------------------------------+
```

---

## DDPG and TD3: Off-Policy Deterministic Actor-Critic

For continuous control with sample efficiency, go *off-policy* with a replay
buffer. DDPG learns a deterministic actor `mu(s;theta)` and a Q-critic, applying
the chain rule through the critic — the **deterministic policy gradient**.

```
+------------------------------------------------------------------+
|  DDPG (deterministic policy gradient)                            |
|                                                                  |
|   critic: minimize  ( Q(s,a;w) - y )^2,                          |
|     y = r + gamma Q(s', mu(s'; theta^-); w^-)   (target nets)    |
|                                                                  |
|   actor:  ascend  grad_theta Q(s, mu(s;theta); w)                |
|     = grad_a Q * grad_theta mu       (chain rule through critic) |
|                                                                  |
|   exploration: add noise to mu(s) (it is deterministic)          |
+------------------------------------------------------------------+
```

DDPG is sample-efficient but notoriously unstable — it overestimates Q (the same
maximization bias from ch 04, now with neural nets). **TD3** fixes it with three
tricks:

```
+------------------------------------------------------------------+
|  TD3 (Twin Delayed DDPG) — three fixes for DDPG instability      |
|  -----------------------                                         |
|  1. TWIN CRITICS:    learn Q1, Q2; use min(Q1,Q2) in the target  |
|                      -> fights overestimation (clipped double-Q) |
|  2. DELAYED ACTOR:   update the actor (and targets) less often   |
|                      than the critic -> critic stabilizes first  |
|  3. TARGET SMOOTHING: add noise to the target action             |
|                      -> regularizes the Q surface, avoids sharp  |
|                         peaks the actor could exploit            |
+------------------------------------------------------------------+
```

The twin-critic `min` is double Q-learning's maximization-bias fix adapted to
continuous actions: taking the minimum of two estimates is a deliberate
*under*-estimate that cancels the optimistic bias of the `max`.

---

## SAC: Maximum-Entropy RL

Soft Actor-Critic reframes the objective itself: maximize reward **and** policy
entropy. The agent is rewarded for acting as randomly as possible while still
solving the task.

```
+------------------------------------------------------------------+
|  MAXIMUM-ENTROPY OBJECTIVE                                       |
|                                                                  |
|   J(pi) = sum_t E[ r(s_t,a_t)  +  alpha * H( pi(.|s_t) ) ]       |
|                                        ^ entropy bonus           |
|   alpha = temperature: trades reward against exploration/        |
|           stochasticity (can be auto-tuned to a target entropy). |
+------------------------------------------------------------------+
```

This changes the Bellman backup into a **soft** version — the value of a state
includes an entropy term, and the optimal policy is a *softmax over Q* rather than
a hard argmax:

```
  soft value:   V(s) = E_{a~pi}[ Q(s,a) - alpha log pi(a|s) ]
  soft policy:  pi(a|s) proportional to exp( Q(s,a) / alpha )   (Boltzmann)
  soft Q target: y = r + gamma ( min(Q1',Q2')  -  alpha log pi(a'|s') )
```

```
+------------------------------------------------------------------+
|  WHY MAX-ENTROPY HELPS                                           |
|  --------------------                                            |
|  - EXPLORATION is built into the objective (not a bolt-on bonus) |
|  - ROBUSTNESS: stochastic policies hedge against model error     |
|  - MULTIMODALITY: can represent several near-optimal behaviors   |
|  - stable, sample-efficient, off-policy (replay buffer)          |
+------------------------------------------------------------------+
```

SAC combines: max-entropy objective + twin critics (from TD3) + a stochastic
(reparameterized Gaussian) actor + off-policy replay. It is the strong default for
continuous control today.

> Bridge — statistical mechanics: the max-entropy / Boltzmann policy
> `pi proportional to exp(Q/alpha)` is exactly the Gibbs distribution with energy
> `-Q` and temperature `alpha`. The "soft" value function is a free energy. This
> connection to `statistical-mechanics/` is not a metaphor — the math is the same.

---

## The Deep-RL Map

```
+------------------------------------------------------------------+
| ALGO   | ON/OFF  | ACTION   | POLICY     | KEY IDEA              |
|--------|---------|----------|------------|-----------------------|
| TRPO   | on*     | both     | stochastic | hard KL trust region  |
| PPO    | on*     | both     | stochastic | clipped ratio         |
| A2C    | on      | both     | stochastic | sync advantage AC     |
| DDPG   | off     | continuous| determin. | det. PG + replay      |
| TD3    | off     | continuous| determin. | twin-Q, delay, smooth |
| SAC    | off     | continuous| stochastic | max-entropy AC       |
| DQN    | off     | discrete | implicit   | value-based (ch 05)   |
+------------------------------------------------------------------+
  *limited off-policy reuse via the importance ratio within a batch
```

---

## Common Confusion Points

### "Why clip the ratio instead of constraining KL directly?"

PPO's clip is a cheap, first-order surrogate for TRPO's KL trust region. It
removes the incentive to move the policy ratio beyond `1 +/- eps`, achieving the
"stay close to old" effect without computing the Fisher matrix or doing a
line search. It is not exactly a KL bound, but empirically it captures the benefit
at a fraction of the complexity.

### "Why does the `min` in PPO matter?"

Without the `min`, a large advantageous ratio could be rewarded without bound. The
`min` makes the bound *pessimistic*: it clips only in the direction that would let
the update overshoot, and never lets the clipping *increase* the objective. It
turns the clip into a one-sided trust region.

### "Deterministic (DDPG) vs stochastic (SAC) actor — when which?"

Deterministic actors are sample-efficient but need injected noise for exploration
and are prone to brittle Q-exploitation. Stochastic max-entropy actors (SAC)
explore by construction, are more robust, and usually train more reliably. SAC is
the safer default; TD3 is competitive and simpler conceptually.

### "Is PPO off-policy because of the importance ratio?"

Only mildly. PPO reuses each batch for a few epochs (slightly off-policy within
the batch), but it discards the data afterward and re-collects under the new
policy. True off-policy methods (DQN, SAC) keep a long-lived replay buffer of old
data. PPO is best called "on-policy with limited reuse."

### "Why twin critics with a min, not a max or a mean?"

The `max` operator in Q-learning systematically overestimates (ch 04). Taking the
`min` of two independently-noisy critics deliberately *under*-estimates, which
empirically cancels the overestimation and stabilizes the actor that climbs the
critic. A mean would not correct the bias.

---

## Decision Cheat Sheet

| Situation                                       | Use                              |
|-------------------------------------------------|----------------------------------|
| Robust, simple default; discrete or continuous  | PPO                              |
| Want monotonic-improvement guarantees           | TRPO (or PPO in practice)        |
| Continuous control, sample efficiency matters    | SAC (default) or TD3            |
| Continuous control, deterministic actor wanted   | TD3 (not raw DDPG)             |
| Exploration is the bottleneck                    | SAC (max-entropy) or entropy bonus |
| Q-values overestimated in continuous control     | TD3 / SAC twin critics          |
| Discrete actions, value-based                    | DQN / Rainbow (ch 05)           |
| Fine-tuning an LLM from a reward model           | PPO (RLHF, ch 09)               |
| Very limited environment interaction             | Off-policy (SAC) or offline RL (ch 09) |
