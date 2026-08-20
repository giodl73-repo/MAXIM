---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-FUNCTION-APPROXIMATION.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:reinforcement-learning:function-approximation
kind: guide
module: reinforcement-learning
section: reinforcement-learning
title: Function Approximation - Linear Methods, the Deadly Triad, DQN
status: source-custody
source_custody: partial
current_path: reinforcement-learning/05-FUNCTION-APPROXIMATION.md
canonical_path: reinforcement-learning/05-FUNCTION-APPROXIMATION.md
backsource_ids: [proof-backfill:reinforcement-learning:05-function-approximation, git-history:reinforcement-learning:05-function-approximation]
concepts: [function approximation, linear approximation, deadly triad, DQN, experience replay, target network]
root_concepts: [function approximation, deadly triad]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Function Approximation — Linear Methods, the Deadly Triad, DQN

## The Big Picture

Tabular methods store one number per state — impossible when states number in the
billions or are continuous. We replace the table with a *parameterized function*
`v(s; w)` or `q(s,a; w)` and learn the weights `w`. This unlocks scale, but it
also breaks the convergence guarantees that contraction mappings gave us. Where
three ingredients meet — function approximation, bootstrapping, off-policy data —
learning can *diverge*. That is the **deadly triad**, and DQN is the bundle of
engineering tricks that tames it.

```
+------------------------------------------------------------------+
|         FROM TABLE TO FUNCTION: WHAT CHANGES                     |
|                                                                  |
|   TABULAR                         FUNCTION APPROXIMATION         |
|   -------                         -----------------------        |
|   V[s] one entry per state        v(s; w), w in R^d, d << |S|    |
|   updates are local               updates GENERALIZE across s    |
|   guaranteed convergence          may diverge (deadly triad)     |
|   exact                           approximate, must generalize   |
+------------------------------------------------------------------+
                                 |
                                 v
+------------------------------------------------------------------+
|              THE DEADLY TRIAD (divergence when all three)        |
|                                                                  |
|     [ FUNCTION APPROX. ]  + [ BOOTSTRAPPING ]  +  [ OFF-POLICY ] |
|         generalize            TD targets           replay/ max   |
|                                                                  |
|     any TWO is usually fine.  ALL THREE can diverge.             |
+------------------------------------------------------------------+
```

**Read it as a warning**: scale forces approximation; efficiency wants
bootstrapping; flexibility wants off-policy. Combine all three naively and the
value estimates can blow up to infinity.

---

## Value Function Approximation

We minimize the mean-squared value error, weighted by the state-visitation
distribution `mu`:

```
  VE(w)  =  sum_s mu(s) [ v_pi(s) - v(s; w) ]^2
```

The SGD update toward a target `U_t` (using the chain rule):

```
  w <- w + alpha [ U_t - v(S_t; w) ] grad_w v(S_t; w)
```

The choice of target `U_t` recapitulates ch 03:

```
  MONTE CARLO:   U_t = G_t                       (true gradient; unbiased)
  TD(0):         U_t = R + gamma v(S'; w)         (SEMI-gradient; biased)
```

**Semi-gradient** is the crucial subtlety: the TD target `R + gamma v(S';w)`
*itself depends on w*, but we do *not* differentiate through it — we treat it as a
fixed target. So TD with function approximation is not true gradient descent on
any fixed objective. This is exactly why its convergence is delicate.

```
+------------------------------------------------------------------+
|  TRUE GRADIENT (MC)        vs       SEMI-GRADIENT (TD)           |
|  - differentiate full obj.          - ignore w-dependence of     |
|  - converges (to a local min)         the bootstrap target       |
|  - slow, high variance            - fast, but no fixed objective |
|                                  - can diverge w/ off-policy     |
+------------------------------------------------------------------+
```

---

## Linear Function Approximation

The cleanest case: `v(s;w) = w^T x(s)`, a linear combination of features `x(s)`.
Then `grad_w v = x(s)`, and the semi-gradient TD(0) update is:

```
  w <- w + alpha [ R + gamma w^T x(S') - w^T x(S) ] x(S)
```

```
+------------------------------------------------------------------+
|  CONVERGENCE OF LINEAR TD(0)                                     |
|                                                                  |
|  ON-POLICY linear TD(0):  CONVERGES to the TD fixed point w_TD.  |
|     - not the best linear fit; off by a factor up to 1/(1-gamma) |
|       from the true minimum VE (the "TD fixed point" w_TD).      |
|  OFF-POLICY linear TD(0):  CAN DIVERGE (Baird's counterexample). |
+------------------------------------------------------------------+
```

Feature engineering — tile coding, radial basis functions, polynomial bases,
Fourier bases — was the pre-deep-RL craft. Linear methods are well-understood and
stable on-policy, which is why much of the *theory* still lives here even though
practice has moved to neural nets.

---

## The Deadly Triad in Detail

```
+------------------------------------------------------------------+
|  INGREDIENT          WHY WE WANT IT        WHAT IT RISKS         |
|  ----------          --------------        ---------------       |
|  Function approx.    scale to huge S       updates leak across   |
|                      generalize            states uncontrollably |
|  Bootstrapping       sample efficiency,    targets move with w;  |
|                      online, low variance  no fixed objective    |
|  Off-policy          reuse data (replay),  state distribution    |
|                      learn greedy policy   mismatch amplifies    |
|                      while exploring       errors                |
+------------------------------------------------------------------+

  Remove ANY one => stable:
    - drop bootstrapping  -> Monte Carlo + approx (true gradient): stable
    - drop off-policy     -> on-policy TD + approx: stable (converges)
    - drop approx         -> tabular: always converges
```

Baird's counterexample is the canonical divergence: a simple MDP where off-policy
linear TD sends weights to infinity even though a perfect representation exists.
The mechanism: the semi-gradient update is not a contraction under the
off-policy distribution, so the iteration map has an unstable mode that
self-amplifies.

```
  DIVERGENCE MECHANISM (intuition):
    update v(s) up -> generalization raises v(s') too
    -> bootstrap target R + gamma v(s') rises
    -> next update raises v(s) again -> positive feedback -> infinity
```

Gradient-TD methods (GTD, TDC) fix this with a true gradient on the projected
Bellman error, but in practice deep RL instead uses the DQN tricks below to make
the triad behave well enough.

---

## Deep Q-Networks (DQN)

DQN (Mnih et al., 2015) learns `q(s,a; w)` with a neural net and reaches
human-level play on Atari from pixels. It *has* all three triad ingredients —
neural-net approximation, TD bootstrapping, off-policy `max` with a replay buffer
— and survives via two stabilizing tricks.

```
+------------------------------------------------------------------+
|  DQN LOSS  (semi-gradient TD on the optimality target)           |
|                                                                  |
|   L(w) = E_{(s,a,r,s') ~ D} [ ( y - q(s,a; w) )^2 ]              |
|   with  y = r + gamma max_a' q(s', a'; w^-)                      |
|                                  ^^^^                            |
|                          target-network weights (frozen copy)    |
+------------------------------------------------------------------+
```

### Trick 1: Experience Replay

```
  store transitions (s,a,r,s') in a buffer D
  train on RANDOM MINIBATCHES sampled from D

  why it helps:
   - BREAKS correlation between consecutive samples (i.i.d.-like batches)
   - REUSES each transition many times (sample efficiency)
   - smooths the data distribution -> tames the off-policy leg
```

### Trick 2: Target Network

```
  keep a SEPARATE frozen copy w^- of the weights for the target y.
  update w^- <- w  only every C steps (or via slow Polyak averaging).

  why it helps:
   - the bootstrap target stops moving every step
   - decouples target from the rapidly-changing online network
   - tames the BOOTSTRAPPING leg (a near-stationary objective)
```

Together: replay calms off-policy correlation; the target network calms
bootstrapping. The two ingredients of the triad that DQN cannot remove (it needs
the neural net for scale and off-policy `max` for control) are *stabilized*
rather than eliminated.

---

## The DQN Improvement Stack ("Rainbow")

DQN spawned a family of orthogonal improvements, combined in *Rainbow*:

```
+------------------------------------------------------------------+
|  EXTENSION            FIXES / ADDS                               |
|  ---------            -----------                                |
|  Double DQN           maximization bias: select with online w,   |
|                       evaluate with target w^-                   |
|  Dueling DQN          split q = V(s) + A(s,a); learn state value |
|                       separately from action advantage           |
|  Prioritized Replay  sample high-TD-error transitions more often |
|                       (prioritized sweeping, ch 02 idea)         |
|  Multi-step (n-step) n-step TD targets (ch 03) for faster credit |
|  Noisy Nets           learnable parametric noise for exploration |
| Distributional (C51) learn the DISTRIBUTION of returns, not mean |
|  Rainbow              all of the above, combined                 |
+------------------------------------------------------------------+
```

Double DQN's target makes the maximization-bias fix from ch 04 concrete:

```
  vanilla DQN:  y = r + gamma  max_a'  q(s', a'; w^-)
  Double DQN:   y = r + gamma  q( s', argmax_a' q(s',a'; w);  w^- )
                                       ^select with online   ^evaluate with target
```

> Bridge — supervised learning: DQN turns RL into a sequence of supervised
> regression problems — fit `q(s,a;w)` to targets `y` by minibatch SGD. The
> replay buffer manufactures the i.i.d.-like dataset that supervised learning
> assumes. The deep-net details (CNNs, optimizers, generalization) belong to
> `machine-learning-theory/` and `ai-engineering/`; here the focus is the RL-
> specific instability the targets introduce.

---

## Worked Example: Why the Target Network Matters

Imagine a single shared weight `w`, feature `x=1`, so `q = w`. One self-loop with
reward 0, gamma = 0.9. The TD target is `0 + 0.9 * q = 0.9 w`. Semi-gradient
update with alpha = 1:

```
  WITHOUT target net (target uses current w):
    w <- w + (0.9 w - w) = w + (-0.1 w) = 0.9 w     -> shrinks toward 0 (here OK)

  Now flip the sign structure (off-policy weighting overweights this state),
  effectively scaling the update; the map becomes w <- k*w with |k|>1:
    w <- 1.1 w -> 1.21 w -> ... -> infinity         (DIVERGENCE)

  WITH a frozen target w^- (updated every C steps):
    target = 0.9 w^-  is CONSTANT during the inner updates
    w converges toward 0.9 w^- each phase -> stable, no runaway feedback
```

The frozen target removes the positive-feedback loop between the estimate and its
own bootstrap target — the precise mechanism behind the triad's divergence.

---

## Common Confusion Points

### "Why is TD called semi-gradient?"

Because we differentiate the prediction `v(S;w)` but *not* the target
`R + gamma v(S';w)`, even though the target also depends on `w`. A true gradient
would differentiate both; doing so (residual gradient) is stable but slow and
biased toward smoothing. Semi-gradient is faster and standard, at the cost of
no fixed objective.

### "Does function approximation alone cause divergence?"

No. Function approximation with Monte Carlo (no bootstrapping) is true gradient
descent and converges. On-policy TD with linear approximation converges. You need
*all three* legs of the triad together to risk divergence.

### "Is the TD fixed point the best linear approximation?"

No. On-policy linear TD converges to `w_TD`, which can be worse than the best
possible linear fit `w_MC` (the minimizer of VE) by a factor up to `1/(1-gamma)`.
TD trades approximation quality for speed and online learning.

### "Replay buffer makes DQN off-policy — isn't that bad given the triad?"

It is the dangerous leg, yes — which is exactly why DQN *also* needs the target
network and careful tuning. Replay's correlation-breaking benefit outweighs its
off-policy cost in practice, but it is why DQN can still be brittle and why
on-policy methods (ch 07) trade sample efficiency for stability.

---

## Decision Cheat Sheet

| Situation                                      | Use                               |
|------------------------------------------------|-----------------------------------|
| Large/continuous state space                   | Function approximation            |
| Want provable on-policy convergence            | Linear features + on-policy TD    |
| Off-policy linear method that won't diverge     | Gradient-TD (GTD/TDC)            |
| Discrete actions, pixels, want scale           | DQN                               |
| Q-values overestimated                         | Double DQN                        |
| Some states matter much more than actions      | Dueling DQN                       |
| Want sample-efficient replay                   | Prioritized experience replay     |
| Need richer return signal                      | Distributional RL (C51/QR-DQN)    |
| Want the strong default value-based agent      | Rainbow                           |
| Continuous actions                             | Policy-gradient / actor-critic (ch 06-07) |
| Seeing divergence                              | Check the triad; add target net, lower lr, go on-policy |
