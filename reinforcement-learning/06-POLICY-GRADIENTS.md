---
maxim_schema: maxim.frontmatter.v1
id: maxim:reinforcement-learning:policy-gradients
kind: guide
module: reinforcement-learning
section: reinforcement-learning
title: Policy Gradients - The Theorem, REINFORCE, Actor-Critic, GAE
status: source-custody
source_custody: partial
current_path: reinforcement-learning/06-POLICY-GRADIENTS.md
canonical_path: reinforcement-learning/06-POLICY-GRADIENTS.md
backsource_ids: [proof-backfill:reinforcement-learning:06-policy-gradients, git-history:reinforcement-learning:06-policy-gradients]
concepts: [policy gradient theorem, REINFORCE, baseline, actor-critic, advantage, A2C, A3C, GAE]
root_concepts: [policy gradient theorem, actor-critic]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Policy Gradients — The Theorem, REINFORCE, Actor-Critic, GAE

## The Big Picture

Value-based methods learn `q` and act greedily. Policy-gradient methods skip the
intermediary and *optimize a parameterized policy* `pi(a|s; theta)` directly by
gradient ascent on expected return. This is the only natural route to continuous
action spaces and stochastic policies, and it is the foundation of every modern
deep-RL algorithm (PPO, SAC) and of RLHF.

```
+------------------------------------------------------------------+
|          VALUE-BASED  vs  POLICY-BASED  vs  ACTOR-CRITIC         |
|                                                                  |
|  VALUE-BASED          POLICY-BASED          ACTOR-CRITIC         |
|  -----------          ------------          ------------         |
|  learn q(s,a)         learn pi(a|s;theta)   learn BOTH           |
|  policy = argmax q    grad-ascend J(theta)  actor: pi(a|s;theta) |
|  implicit policy      explicit policy       critic: v(s;w)       |
|  discrete actions     continuous OK         critic reduces       |
|  off-policy easy      stochastic OK         the variance         |
|  DQN                  REINFORCE             A2C, PPO, SAC        |
+------------------------------------------------------------------+
                                 |
                                 v
+------------------------------------------------------------------+
|              THE OBJECTIVE  J(theta) = E_pi[ G_0 ]               |
|       maximize expected return by ASCENDING grad_theta J         |
+------------------------------------------------------------------+
```

**Read it as a choice of representation**: instead of learning values and reading
off a policy, parameterize the policy itself and push its parameters uphill on
return. The actor-critic column is where the field actually lives.

---

## Why Policy Gradients At All?

```
+------------------------------------------------------------------+
|  ADVANTAGE OF DIRECT POLICY OPTIMIZATION                         |
|  --------------------------------------                          |
|  - CONTINUOUS actions: argmax over q is intractable; a           |
|    parameterized pi (e.g. Gaussian) handles them natively        |
|  - STOCHASTIC optimal policies: in partially observed or         |
|    adversarial settings the best policy is randomized; argmax    |
|    q is always deterministic                                     |
|  - SMOOTH policy changes: small theta steps -> small policy      |
|    changes (value-based argmax can flip abruptly)                |
|  - directly optimizes the thing you care about (return)          |
|                                                                  |
| COST: high variance gradients; usually on-policy (sample hungry) |
+------------------------------------------------------------------+
```

---

## The Policy Gradient Theorem

The central result. The gradient of expected return does **not** require
differentiating the environment dynamics — only the policy.

```
+------------------------------------------------------------------+
|  POLICY GRADIENT THEOREM                                         |
|                                                                  |
|  grad_theta J(theta)                                             |
|     = E_pi [  grad_theta log pi(a|s; theta)  *  q_pi(s,a)  ]     |
+------------------------------------------------------------------+
```

The derivation hinges on the **log-derivative (score function) trick**:

```
  grad_theta pi(a|s;theta) = pi(a|s;theta) * grad_theta log pi(a|s;theta)
```

Sketch (one-step intuition): write `J = sum_s d(s) sum_a pi(a|s) q(s,a)`. Push the
gradient inside; the term that touches the *environment* (the distribution `d(s)`
and the dynamics inside `q`) telescopes away in the full derivation, leaving only
`grad log pi * q`. The key payoff:

```
   grad_theta J  needs NO model of p(s'|s,a) and NO grad of the dynamics.
   It is an expectation we can ESTIMATE FROM SAMPLES.
```

Intuition: increase the log-probability of actions that led to high `q`, decrease
it for low `q`. The score `grad log pi` is the direction in parameter space that
makes action `a` more likely; weighting it by `q_pi(s,a)` turns it into "make good
actions more likely."

---

## REINFORCE: Monte-Carlo Policy Gradient

Replace `q_pi(s,a)` with the sampled return `G_t` (an unbiased estimate):

```
+------------------------------------------------------------------+
|  REINFORCE                                                       |
|                                                                  |
|  run an episode under pi(.;theta)                                |
|  for each step t:                                                |
|    theta <- theta + alpha * gamma^t * G_t * grad log pi(A_t|S_t) |
+------------------------------------------------------------------+
```

Unbiased, but **very high variance** — `G_t` accumulates randomness over the
entire trajectory (the same MC variance from ch 03, now in gradient space). Two
remedies: subtract a baseline, and bootstrap with a critic.

---

## Baselines: Variance Reduction for Free

Subtract any function `b(s)` that does *not* depend on the action — it leaves the
gradient unbiased (the expected score function is zero,
`E_a[grad log pi] = 0`) but can slash variance:

```
  grad_theta J = E_pi [ grad log pi(a|s) * ( q_pi(s,a) - b(s) ) ]

  E_a[ grad log pi(a|s) * b(s) ] = b(s) * E_a[grad log pi] = b(s)*0 = 0
  => subtracting b(s) does NOT change the expectation. Unbiased.
```

The best practical baseline is the **state value** `b(s) = v(s)`, giving the
**advantage** function:

```
   A_pi(s,a)  =  q_pi(s,a)  -  v_pi(s)
   "how much better is action a than the average action in state s?"

   grad J = E[ grad log pi(a|s) * A_pi(s,a) ]
```

The advantage centers the signal: positive for above-average actions, negative
for below-average. This single change is the workhorse of every modern method.

---

## Actor-Critic: Bootstrap the Gradient

REINFORCE waits for full returns. Actor-critic replaces `G_t` (or `q`) with a
*learned critic* and bootstraps — trading variance for a little bias, exactly the
ch 03 trade-off, now inside the policy gradient.

```
+------------------------------------------------------------------+
|                      ACTOR-CRITIC                                |
|                                                                  |
|   .---------.   action a    .-------------.                      |
|   | ACTOR   |-------------->| ENVIRONMENT  |                     |
|   | pi(.|s; |   s, r        '-------------'                      |
|   |  theta) |<-------------------|                               |
|   '---------'                    v                               |
|        ^                   .-----------.                         |
|        | TD error delta    |  CRITIC   |   estimates v(s; w)     |
|        '-------------------|  v(s; w)  |                         |
|                            '-----------'                         |
|                                                                  |
|   critic update:  w <- w + alpha_w * delta * grad v(s;w)         |
|   actor update:   theta <- theta + alpha_t * delta * grad log pi |
|   where  delta = r + gamma v(s';w) - v(s;w)   (TD error)         |
+------------------------------------------------------------------+
```

The TD error `delta` is an unbiased *sample of the advantage*:
`E[delta | s,a] = q_pi(s,a) - v_pi(s) = A_pi(s,a)`. So the critic's TD error *is*
the advantage estimate that weights the actor's gradient. Two GPI loops fused: the
critic evaluates, the actor improves.

```
+------------------------------------------------------------------+
|  REINFORCE          A weighted by    G_t (full MC return)        |
|  REINFORCE+baseline A weighted by    G_t - v(s)                  |
|  Actor-Critic       A weighted by    delta = r + g v(s') - v(s)  |
|                     ^ bootstrapped: lower variance, some bias    |
+------------------------------------------------------------------+
```

---

## A2C and A3C

Scaling actor-critic to deep nets needs decorrelated data without a replay buffer
(policy gradients are on-policy, so old data is off-distribution). The answer:
*parallel actors*.

```
+------------------------------------------------------------------+
|  A3C (Asynchronous Advantage Actor-Critic)                       |
|    many worker threads, each with a copy of (theta, w)           |
|    each runs its own environment, computes gradients,            |
|    ASYNCHRONOUSLY updates shared parameters.                     |
|    Parallelism decorrelates data (replaces the replay buffer).   |
|                                                                  |
|  A2C (Advantage Actor-Critic)                                    |
|    the SYNCHRONOUS version: wait for all workers, average,       |
|   one update. Simpler, GPU-friendly, usually >= A3C in practice. |
+------------------------------------------------------------------+
```

Both use n-step advantage estimates and an *entropy bonus* added to the objective
to keep the policy from collapsing prematurely (encourage exploration):

```
  objective = E[ log pi(a|s) * A ]  +  beta * H(pi(.|s))
                                         ^ entropy regularization
```

---

## Generalized Advantage Estimation (GAE)

How many steps should the advantage look ahead before bootstrapping? GAE applies
the TD(lambda) idea (ch 03) to the *advantage*, exponentially averaging n-step
advantage estimators.

```
  TD residual:   delta_t = r_t + gamma v(s_{t+1}) - v(s_t)

  GAE:  A_t^{GAE(gamma,lambda)} = sum_{l=0}^{inf} (gamma lambda)^l delta_{t+l}

    lambda = 0 :  A_t = delta_t            (1-step; low variance, biased)
    lambda = 1 :  A_t = G_t - v(s_t)       (full MC advantage; unbiased, high var)
    0<lambda<1 :  smooth bias-variance interpolation
```

```
+------------------------------------------------------------------+
|  GAE = the bias-variance dial for the ADVANTAGE estimate.        |
|  gamma controls the horizon; lambda controls how much you trust  |
|  the critic's bootstrap vs the sampled rewards.                  |
|  Typical: gamma=0.99, lambda=0.95  (used by PPO, ch 07).         |
+------------------------------------------------------------------+
```

GAE is the standard advantage estimator feeding PPO and most modern on-policy
agents — it is the practical realization of the bias-variance theory from ch 03,
applied where it matters most.

> Bridge — RLHF and LLMs: when an LLM is fine-tuned with RLHF, the language model
> *is* the actor `pi(a|s;theta)` (tokens = actions), a reward model supplies the
> reward, a value head is the critic, and PPO does the optimization with GAE
> advantages. Every term in this chapter appears verbatim in the RLHF pipeline —
> see ch 09 and `ai-engineering/`.

---

## Worked Example: The Score Function on a Softmax Policy

Policy `pi(a|s;theta) = softmax(theta^T phi(s,a))`. The score is the classic
softmax gradient:

```
  grad_theta log pi(a|s) = phi(s,a) - E_{a'~pi}[ phi(s,a') ]
                         = (observed feature) - (expected feature under pi)
```

So the REINFORCE update for one step is:

```
  theta <- theta + alpha * A(s,a) * ( phi(s,a) - E_{a'~pi}[phi(s,a')] )
```

Interpretation: if action `a` had positive advantage, push `theta` to make
`phi(s,a)` more favored relative to the policy's average — increasing
`pi(a|s)`. If the advantage is negative, push the other way. The expected-feature
subtraction is the policy's own baseline appearing naturally in the score.

---

## Common Confusion Points

### "Why doesn't the policy gradient need the dynamics?"

Because of the log-derivative trick: the gradient lands entirely on
`log pi(a|s;theta)`, which you control and can differentiate. The environment's
contribution enters only through the *sampled* `q`/return/advantage, not through
its derivative. You never differentiate `p(s'|s,a)`.

### "Baseline subtraction — doesn't it bias the gradient?"

No, as long as the baseline depends only on the state (not the action). The
expected score function is zero, so `E[grad log pi * b(s)] = 0` exactly. The
baseline changes only the *variance*, never the expectation.

### "Advantage vs TD error vs return — how do they relate?"

```
  return G_t        : unbiased, high variance (REINFORCE)
  G_t - v(s)        : unbiased advantage estimate, lower variance
  delta = r+gv'-v   : 1-step bootstrapped advantage (biased, low variance)
  GAE(gamma,lambda) : tunable blend of all the above
```

They are points on the same bias-variance spectrum, all estimating the same
underlying advantage `A_pi(s,a)`.

### "Why are policy gradients usually on-policy?"

The expectation `E_pi[...]` is taken under the *current* policy. Data from an old
policy is off-distribution and needs importance weighting, whose variance
explodes (ch 04). PPO (ch 07) makes limited off-policy reuse safe with a clipped
ratio; SAC goes fully off-policy by reformulating the objective.

### "Actor-critic vs REINFORCE-with-baseline — same thing?"

Close but not identical. REINFORCE-with-baseline uses the full MC return `G_t`
minus `v(s)` (no bootstrapping in the actor's weight). Actor-critic *bootstraps*:
it uses `r + gamma v(s')` (the TD error) as the advantage, introducing bias to
cut variance. The critic in REINFORCE+baseline is only a baseline; in actor-critic
it is also part of the target.

---

## Decision Cheat Sheet

| Situation                                      | Use                               |
|------------------------------------------------|-----------------------------------|
| Continuous action space                        | Policy gradient / actor-critic    |
| Need a stochastic optimal policy               | Policy gradient                   |
| Simplest unbiased policy-gradient baseline     | REINFORCE                         |
| Cut REINFORCE variance, stay unbiased          | Add a state-value baseline (advantage) |
| Want low-variance online updates               | Actor-critic (TD-error advantage) |
| Scale on-policy AC across many envs            | A2C (sync) / A3C (async)          |
| Tune the advantage bias-variance trade-off     | GAE (gamma, lambda)               |
| Encourage exploration in a policy              | Entropy bonus (or SAC, ch 07)     |
| Want a robust modern default                   | PPO with GAE (ch 07)              |
| Fine-tune an LLM from preferences              | PPO + reward model (RLHF, ch 09)  |
