---
maxim_schema: maxim.frontmatter.v1
id: maxim:reinforcement-learning:model-free-control
kind: guide
module: reinforcement-learning
section: reinforcement-learning
title: Model-Free Control - SARSA, Q-Learning, Exploration
status: source-custody
source_custody: partial
current_path: reinforcement-learning/04-MODEL-FREE-CONTROL.md
canonical_path: reinforcement-learning/04-MODEL-FREE-CONTROL.md
backsource_ids: [proof-backfill:reinforcement-learning:04-model-free-control, git-history:reinforcement-learning:04-model-free-control]
concepts: [sarsa, q-learning, on-policy, off-policy, exploration, epsilon-greedy, UCB, optimism]
root_concepts: [q-learning, on-policy, off-policy]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Model-Free Control — SARSA, Q-Learning, Exploration

## The Big Picture

Control means *finding the optimal policy*, not just evaluating one. Without a
model we learn the action-value function `q` from samples and act greedily on it.
Two algorithms — SARSA and Q-learning — differ in one subtle line, and that line
is the whole on-policy / off-policy distinction.

```
+------------------------------------------------------------------+
|              MODEL-FREE CONTROL = GPI WITH SAMPLES               |
|                                                                  |
|   EVALUATE q from experience  <-->  IMPROVE: epsilon-greedy(q)   |
|                                                                  |
|   .----------------------.        .----------------------.       |
|   |       SARSA          |        |     Q-LEARNING       |       |
|   |   ON-POLICY          |        |     OFF-POLICY       |       |
|   |   target uses the    |        |   target uses the    |       |
|   |   action ACTUALLY    |        |   GREEDY action      |       |
|   |   taken next (A')    |        |   max_a' Q(S',a')    |       |
|   '----------------------'        '----------------------'       |
|         learns q_pi for                learns q_* directly       |
|         the behavior policy            regardless of behavior    |
+------------------------------------------------------------------+
```

**The fork**: when forming the bootstrap target at `S'`, SARSA plugs in the action
the policy *will actually take*; Q-learning plugs in the *best* action. One word
of difference, two different fixed points.

---

## The Exploration-Exploitation Dilemma

To act greedily you must know `q` — but to learn `q` you must try actions that
look suboptimal. If you only ever take the current-best action you never discover
a better one. This is the exploration-exploitation trade-off, and it has no
analogue in supervised learning.

```
+------------------------------------------------------------------+
|  EXPLOIT                          EXPLORE                        |
|  -------                          -------                        |
|  take argmax_a Q(s,a)             try other actions to learn     |
|  maximize reward NOW              improve Q for the future       |
|  risk: stuck in a local optimum   risk: wasted reward now        |
+------------------------------------------------------------------+
```

### Exploration strategies

```
  epsilon-GREEDY    with prob (1-eps) take argmax; with prob eps act random.
                    Simple, ubiquitous. Decay eps over time (GLIE).

  OPTIMISTIC INIT   set Q high (e.g. all rewards look great initially).
                    Greedy behavior then explores until disappointed.

  UCB               pick argmax_a [ Q(s,a) + c sqrt(ln t / N(s,a)) ].
                    Bonus for under-tried actions; directed, not random.

  BOLTZMANN         sample a ~ softmax(Q(s,.)/tau). Temperature tau controls
  (softmax)         exploration; smooth alternative to epsilon-greedy.
```

```
  eps-greedy:  undirected (random among all non-greedy actions)
  UCB:         directed   (explores the most UNCERTAIN actions)
  optimism:    directed via initialization; explores then settles
```

**GLIE** (Greedy in the Limit with Infinite Exploration) is the condition for
tabular convergence to `q_*`: every state-action pair is tried infinitely often,
*and* the policy becomes greedy in the limit. `epsilon_k = 1/k` satisfies both.

> Bridge — bandits and OR: UCB and Thompson sampling come from the multi-armed
> bandit literature, the stateless special case of RL. The bandit
> regret-minimization theory (`operations-research/`, decision theory) is the
> rigorous home of "explore the uncertain arm." RL inherits the dilemma and adds
> state.

---

## SARSA: On-Policy TD Control

SARSA updates `Q(S,A)` toward a target built from the *next action the policy
actually chooses*. Its name is the tuple it uses: **S**tate, **A**ction,
**R**eward, next **S**tate, next **A**ction.

```
+------------------------------------------------------------------+
|  SARSA  (on-policy)                                              |
|                                                                  |
|  observe S, choose A ~ epsilon-greedy(Q)                         |
|  take A, observe R, S'                                           |
|  choose A' ~ epsilon-greedy(Q)        <- the SAME policy         |
|     Q(S,A) <- Q(S,A) + alpha[ R + gamma Q(S',A') - Q(S,A) ]      |
|  S,A <- S',A'                                                    |
+------------------------------------------------------------------+
```

The target `R + gamma Q(S',A')` uses `A'`, the action the *behavior* (epsilon-
greedy) policy will take. So SARSA learns `q_pi` for the policy it is *actually
following*, exploration included. It evaluates the policy it executes.

---

## Q-Learning: Off-Policy TD Control

Q-learning's target uses `max_a' Q(S', a')` — the value of the *greedy* action,
regardless of what the behavior policy does next.

```
+------------------------------------------------------------------+
|  Q-LEARNING  (off-policy)                                        |
|                                                                  |
|  observe S, choose A ~ epsilon-greedy(Q)   (behavior policy)     |
|  take A, observe R, S'                                           |
|   Q(S,A) <- Q(S,A) + alpha[ R + gamma max_a' Q(S',a') - Q(S,A) ] |
|  S <- S'                                                         |
+------------------------------------------------------------------+
```

The target `max_a' Q(S',a')` is a sampled version of the Bellman *optimality*
operator. So Q-learning estimates `q_*` directly — the **target policy is greedy**
while the **behavior policy explores**. That separation is exactly what
"off-policy" means.

```
  behavior policy   = how you ACT and gather data        (epsilon-greedy)
  target policy     = the policy you are LEARNING about   (greedy, for Q-learning)

  on-policy  : behavior == target   (SARSA)
  off-policy : behavior != target   (Q-learning)
```

---

## SARSA vs Q-Learning, Precisely

```
+--------------------------------+--------------------------------+
|  SARSA                         |  Q-LEARNING                    |
|  -----                         |  ----------                    |
|  target: R + g Q(S', A')       |  target: R + g max_a Q(S',a)   |
|  A' from behavior policy       |  greedy max, any behavior      |
|  ON-policy                     |  OFF-policy                    |
|  learns q_pi (behavior incl.   |  learns q_* (optimal,          |
|     exploration cost)          |     ignores exploration cost)  |
|  Bellman EXPECTATION backup    |  Bellman OPTIMALITY backup     |
|  safer near danger             |  optimal but riskier path      |
+--------------------------------+--------------------------------+
```

### The Cliff Walk: why the difference is real

The canonical example. A grid with a cliff along the bottom edge; falling off
gives -100, each step -1, goal at the far corner. Behavior is epsilon-greedy.

```
   S . . . . . . . . . G        <- the optimal (shortest) path hugs the cliff
   C C C C C C C C C C C        <- the cliff (-100 if you step in)

   Q-LEARNING: learns the OPTIMAL path right along the cliff edge.
               But while EXPLORING (epsilon), it occasionally steps off
               and racks up -100 penalties. Higher online cost.

   SARSA:      learns a SAFER path one row up from the cliff.
               Because its target accounts for the exploratory A',
               it "knows" epsilon will sometimes push it off, so it
               avoids the edge. Lower online cost, longer path.
```

The lesson: Q-learning converges to `q_*` (the optimal greedy policy) but its
*online behavior during learning* can be worse because it ignores the cost of its
own exploration. SARSA's on-policy target internalizes that cost. As epsilon -> 0
(GLIE), both converge to the same optimal greedy policy.

---

## Expected SARSA and a Family Tree

Expected SARSA removes the variance of sampling `A'` by taking the *expectation*
over the policy's actions:

```
  target = R + gamma sum_a' pi(a'|S') Q(S', a')
```

```
+------------------------------------------------------------------+
|              THE TD-CONTROL FAMILY (target at S')                |
|                                                                  |
|  SARSA           R + gamma Q(S', A')          sample of pi       |
|  Expected SARSA  R + gamma E_{a~pi}[Q(S',a)]  expectation of pi  |
|  Q-learning      R + gamma max_a Q(S', a)     greedy policy      |
|                                                                  |
|  Q-learning = Expected SARSA with the GREEDY target policy       |
|  (so it is the off-policy member of the same family)             |
+------------------------------------------------------------------+
```

Expected SARSA can be run on- or off-policy and usually has lower variance than
SARSA at slightly higher per-step cost.

### Maximization Bias and Double Q-Learning

The `max` in Q-learning is biased: taking the max over noisy estimates
*overestimates* the true max (Jensen's inequality, `E[max] >= max[E]`). This
**maximization bias** inflates Q-values.

```
  fix: DOUBLE Q-LEARNING. Keep two estimates Q1, Q2.
       use one to SELECT the action, the other to EVALUATE it:
         a* = argmax_a Q1(S', a)
         target = R + gamma Q2(S', a*)
       decouples selection from evaluation -> unbiased max.
```

This idea returns as **Double DQN** in ch 05.

---

## Off-Policy Learning and Importance Sampling

Q-learning is off-policy *for free* because its target (the greedy `max`) does not
depend on the behavior policy's action probabilities. General off-policy
prediction of `v_pi` from data generated by a different behavior policy `b`
requires **importance sampling** to correct the distribution mismatch:

```
  rho_t = pi(A_t|S_t) / b(A_t|S_t)        (per-step importance ratio)

  weight the return (or each step) by the product of ratios so that
  E_b[ rho * G ] = E_pi[ G ].
```

```
  ORDINARY IS:   unbiased, but variance can be UNBOUNDED (product of ratios)
  WEIGHTED IS:   biased but consistent, far lower variance (preferred)
```

The variance of long importance-sampling products is a core pain of off-policy MC
and a reason TD-based off-policy methods (which bootstrap, shortening the product)
are favored — at the cost of joining the deadly triad (ch 05).

---

## Common Confusion Points

### "What single thing makes Q-learning off-policy?"

The `max` in its target. It evaluates the *greedy* policy no matter which action
the behavior policy actually took, so the thing being learned (target policy) is
decoupled from the thing being executed (behavior policy). SARSA's `Q(S',A')` ties
them together.

### "Will SARSA and Q-learning ever agree?"

Yes — as exploration vanishes (epsilon -> 0), the behavior policy becomes greedy,
`A' = argmax`, and SARSA's target equals Q-learning's. They differ only while
meaningful exploration is happening.

### "Is off-policy always better because it can reuse data?"

Off-policy is more flexible (replay buffers, learning the greedy policy while
exploring) but more fragile. With function approximation it is one leg of the
deadly triad and can diverge. On-policy methods are more stable, which is why PPO
(ch 07) is on-policy.

### "epsilon-greedy vs UCB — which to use?"

epsilon-greedy is undirected and trivially simple; it wastes exploration on
clearly-bad actions. UCB and Thompson sampling are *directed* (explore the
uncertain, not the random) and have better regret bounds, but need an uncertainty
estimate, which is hard with deep function approximators. Deep RL mostly still
uses epsilon-greedy or entropy bonuses (ch 07).

### "Why does optimistic initialization explore?"

If all Q-values start high, every action looks great until tried. Greedy behavior
then systematically tries each action (and is "disappointed" down to reality),
giving exploration for free early on — but only once, so it does not handle
non-stationarity.

---

## Decision Cheat Sheet

| Situation                                       | Use                                |
|-------------------------------------------------|------------------------------------|
| Want the optimal greedy policy, tabular         | Q-learning                         |
| Online performance during learning matters (risk) | SARSA (on-policy, accounts for exploration) |
| Want lower-variance TD control                  | Expected SARSA                     |
| Q-values look inflated / overestimated          | Double Q-learning                  |
| Want directed exploration with regret bounds    | UCB / Thompson sampling            |
| Simplest possible exploration                   | epsilon-greedy (decay it, GLIE)    |
| Stationary task, want free early exploration    | Optimistic initialization          |
| Off-policy prediction of a different policy     | Importance sampling (weighted)     |
| Continuous actions / large state spaces         | Function approximation (ch 05-07)  |
