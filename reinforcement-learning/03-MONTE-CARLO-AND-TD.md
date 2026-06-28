---
maxim_schema: maxim.frontmatter.v1
id: maxim:reinforcement-learning:monte-carlo-and-td
kind: guide
module: reinforcement-learning
section: reinforcement-learning
title: Monte Carlo and Temporal Difference Learning
status: source-custody
source_custody: partial
current_path: reinforcement-learning/03-MONTE-CARLO-AND-TD.md
canonical_path: reinforcement-learning/03-MONTE-CARLO-AND-TD.md
backsource_ids: [proof-backfill:reinforcement-learning:03-monte-carlo-and-td, git-history:reinforcement-learning:03-monte-carlo-and-td]
concepts: [monte carlo, temporal difference, TD(0), TD(lambda), eligibility traces, bias variance]
root_concepts: [temporal difference]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Monte Carlo and Temporal Difference Learning

## The Big Picture

Now the model is gone. We learn value functions from *sampled experience* alone.
Two pure strategies sit at opposite ends of a spectrum, and the trade-off between
them — bias versus variance, set by how much you *bootstrap* — is one of the most
important dials in all of RL.

```
+------------------------------------------------------------------+
|        THE SPECTRUM: HOW FAR DO YOU LOOK BEFORE UPDATING?        |
|                                                                  |
|  MONTE CARLO                  TD(lambda)            TD(0)        |
|  (full return)                (n-step blend)        (one step)   |
|  ----------                   -----------           -------      |
|  wait for episode end         intermediate         bootstrap now |
|  G_t = r + gr + g^2 r + ...   geometric mix         r + g V(s')  |
|                                                                  |
|  no bootstrap                 partial bootstrap   full bootstrap |
|  UNBIASED                                           BIASED       |
|  HIGH variance                                      LOW variance |
|                                                                  |
|  lambda = 1  <----------------------------------->  lambda = 0   |
+------------------------------------------------------------------+
```

**Read it left-to-right as the bootstrapping dial.** Pure Monte Carlo waits for
the true return (unbiased, high variance). TD(0) updates immediately toward its
own estimate (biased by that estimate, low variance). TD(lambda) interpolates.

---

## Monte Carlo Prediction

Estimate `v_pi(s)` by *averaging actual returns* observed after visiting `s`. No
model, no bootstrapping — just the law of large numbers.

```
+------------------------------------------------------------------+
|  MONTE CARLO PREDICTION                                          |
|                                                                  |
|  run an episode under pi:  S0,A0,R1,S1,...,S_T  (terminal)       |
|  for each state S_t visited, compute the realized return:        |
|     G_t = R_{t+1} + gamma R_{t+2} + ... + gamma^{T-t-1} R_T      |
|  update toward it:                                               |
|     V(S_t)  <-  V(S_t) + alpha [ G_t - V(S_t) ]                  |
+------------------------------------------------------------------+
```

`G_t` is an *unbiased* sample of `v_pi(S_t)` — its expectation is exactly the
value. Averaging many such samples converges to the true value.

```
  first-visit MC:  average return after the FIRST visit to s per episode
  every-visit MC:  average return after EVERY visit to s
```

Both converge; first-visit gives an unbiased mean of i.i.d. returns. The catch:
MC needs *complete episodes* (no learning in continuing tasks) and the returns
are high-variance because they accumulate randomness from the entire trajectory.

---

## Temporal Difference: TD(0)

TD replaces the unknown future return `G_t` with a *bootstrapped estimate*:
`R_{t+1} + gamma V(S_{t+1})`. You update toward your own next guess.

```
+------------------------------------------------------------------+
|  TD(0) PREDICTION                                                |
|                                                                  |
|  on each step  S_t, R_{t+1}, S_{t+1}:                            |
|     delta_t = R_{t+1} + gamma V(S_{t+1}) - V(S_t)   <- TD ERROR  |
|     V(S_t)  <-  V(S_t) + alpha * delta_t                         |
+------------------------------------------------------------------+
```

The **TD error** `delta_t` is the surprise — the difference between the
bootstrapped one-step target and the current estimate. It is the single most
important quantity in model-free RL; the dopamine system in the brain encodes
something strikingly like it.

```
  MC target:   G_t                       (full sampled return, no model, no bootstrap)
  TD target:   R_{t+1} + gamma V(S_{t+1}) (one real reward + bootstrapped estimate)
  DP target:   E[ R + gamma V(S') ]       (expectation, needs model, full bootstrap)
```

TD is the hybrid: it *samples* (like MC, no model) and *bootstraps* (like DP). It
can learn online, step-by-step, from incomplete episodes, and in continuing
tasks.

---

## The Bias-Variance Trade-Off

This is the crux. State it precisely.

```
+------------------------------------------------------------------+
|                MONTE CARLO          vs          TD(0)            |
|                ----------------                 -------          |
|  Target        G_t (true return)    R_{t+1} + gamma V(S_{t+1})   |
|  Bias          ZERO (unbiased)      BIASED (uses estimate V)     |
|  Variance      HIGH (whole traj.)   LOW (one transition)         |
|  Bootstraps?   no                   yes                          |
|  Needs model?  no                   no                           |
|  Episodes?     complete only        online, incomplete ok        |
|  Markov?       works either way     exploits Markov structure    |
+------------------------------------------------------------------+
```

Why MC is unbiased but high-variance: `G_t` is a single sample of a sum of many
random rewards, so `E[G_t] = v_pi` exactly, but its spread grows with episode
length.

Why TD is biased but low-variance: the target depends on the *current estimate*
`V(S_{t+1})`, which is wrong early on (bias), but it is a single one-step
quantity, so it has far less variance. As `V` converges, the bias vanishes.

```
  ERROR DECOMPOSITION (informal):

  MC:   error = pure variance        (bias = 0)
  TD:   error = small variance + bias(from bootstrapping)

  Early training: TD's bias hurts but its low variance lets it move fast.
  Tabular, enough data: BOTH converge to v_pi.
```

Empirically TD usually learns faster on Markov problems because it exploits the
recursive structure rather than waiting for whole returns. There is a clean
contrast in their fixed points on a *batch* of data: batch MC minimizes
mean-squared error to the observed returns, while batch TD(0) converges to the
value function of the *maximum-likelihood MDP* fit to the data — TD implicitly
builds a model.

---

## n-Step Returns: Bridging MC and TD

Don't bootstrap after one step — bootstrap after `n`. The n-step return:

```
  G_t^{(n)} = R_{t+1} + gamma R_{t+2} + ... + gamma^{n-1} R_{t+n}
              + gamma^n V(S_{t+n})
```

```
  n = 1   ->  TD(0)         (bootstrap immediately)
  n = inf ->  Monte Carlo   (never bootstrap; full return)
  1<n<inf ->  intermediate; often best in practice (n ~ 4..8 common)
```

n-step methods frequently beat both extremes because a moderate `n` balances the
bias of early bootstrapping against the variance of long returns.

---

## TD(lambda) and Eligibility Traces

Rather than pick one `n`, average *all* n-step returns with geometrically decaying
weights `(1-lambda) lambda^{n-1}` — the **lambda-return**:

```
  G_t^lambda = (1 - lambda) sum_{n=1}^{inf} lambda^{n-1} G_t^{(n)}

  lambda = 0  ->  TD(0)        (all weight on the 1-step return)
  lambda = 1  ->  Monte Carlo  (all weight on the full return)
```

```
  weight on n-step return:
    (1-lambda)              n=1
    (1-lambda) lambda       n=2
    (1-lambda) lambda^2     n=3   ...   (geometric, sums to 1)
```

The **forward view** (lambda-return) is conceptually clean but needs the whole
future. The **backward view** with *eligibility traces* makes it online and
incremental — and the two are provably equivalent.

```
+------------------------------------------------------------------+
|  BACKWARD VIEW: TD(lambda) WITH ELIGIBILITY TRACES               |
|                                                                  |
|  eligibility trace per state (accumulating):                     |
|     e(s) <- gamma * lambda * e(s)   for all s                    |
|     e(S_t) <- e(S_t) + 1            (the just-visited state)     |
|                                                                  |
|  one TD error updates EVERY state by its eligibility:            |
|     delta_t = R_{t+1} + gamma V(S_{t+1}) - V(S_t)                |
|     V(s) <- V(s) + alpha * delta_t * e(s)   for all s            |
+------------------------------------------------------------------+
```

The trace `e(s)` is a fading memory of how recently and how often state `s` was
visited. A TD error flows backward to all recently-visited states, weighted by
their traces — solving the *temporal credit assignment* problem (which earlier
state deserves credit for this surprise?) without storing whole trajectories.

```
   visited:   s1 ... s2 ... s3 ... [reward surprise here]
   trace:    fading <- fading <- big
   credit flows backward, decayed by (gamma*lambda) per step
```

Two trace variants:

| Trace type     | Update at revisit          | Effect                         |
|----------------|----------------------------|--------------------------------|
| Accumulating   | `e(s) += 1`                | repeated visits add up         |
| Replacing      | `e(s) = 1`                 | resets to 1; more stable       |
| Dutch          | mix (used in true online TD) | exact equivalence to forward |

---

## Monte Carlo and TD Control (preview)

Prediction estimates `v_pi`; *control* finds `pi_*`. Wrap prediction in GPI
(ch 02): evaluate `q` from samples, then act epsilon-greedily. MC control and TD
control (SARSA, Q-learning) are the subject of ch 04 — they learn `q` not `v`
precisely because, without a model, `q` is what you need to act greedily.

```
  MC control:   episode -> q estimates -> epsilon-greedy -> repeat
  TD control:   step    -> q bootstrap  -> epsilon-greedy -> repeat   (ch 04)
```

> Bridge — stochastic approximation: the update
> `V <- V + alpha(target - V)` is the Robbins-Monro algorithm for finding the
> root of `E[target - V] = 0`. Convergence requires the classic step-size
> conditions `sum alpha = inf, sum alpha^2 < inf`. See
> `operations-research/` and `numerical-methods/`.

---

## Worked Example: MC vs TD on a Short Chain

States `A -> B -> terminal`, gamma = 1. One episode observed:
`A, r=0, B, r=1, terminal`. So the realized return from A is `G_A = 0 + 1 = 1`,
from B is `G_B = 1`. Start `V(A)=V(B)=0`, alpha = 0.5.

```
  MONTE CARLO (uses full returns G):
    V(A) <- 0 + 0.5*(1 - 0) = 0.5
    V(B) <- 0 + 0.5*(1 - 0) = 0.5

  TD(0) (bootstraps off the NEXT state's value):
    at A: delta = 0 + 1*V(B) - V(A) = 0 + 0 - 0 = 0  -> V(A) stays 0
    at B: delta = 1 + 1*V(term=0) - V(B) = 1 - 0 = 1 -> V(B) <- 0.5
```

After one episode TD has not yet propagated value to A (its bootstrap target
`V(B)` was still 0 when A was updated). MC moved both immediately. Over many
episodes the value flows back through the chain step by step in TD — the
"backward creep" that eligibility traces accelerate.

---

## Common Confusion Points

### "Bootstrapping vs sampling — what's the difference?"

```
  SAMPLING    = use a real, observed quantity (an actual reward/return)
  BOOTSTRAP   = update an estimate toward another ESTIMATE (V(S_{t+1}))

  MC: samples, does not bootstrap
  DP: bootstraps, does not sample (uses the model's expectation)
  TD: samples AND bootstraps  <- the powerful, dangerous combination
```

### "Why is TD biased if it converges to the right answer?"

Bias is about a *finite-sample* expectation. The TD target uses the current
(imperfect) `V`, so for any fixed imperfect `V` the target is biased. As `V`
converges to `v_pi`, the bias vanishes and the fixed point is correct. MC's target
is unbiased at every step.

### "Does higher lambda always help?"

No. `lambda` trades bias for variance like `n` does. lambda near 1 is
low-bias/high-variance (MC-like); lambda near 0 is high-bias/low-variance
(TD-like). The best lambda is problem-dependent — often in the 0.7-0.95 range
empirically.

### "Eligibility traces — are they memory of states or of gradients?"

In tabular RL the trace is per-state. With function approximation (ch 05-06) the
trace is per-*parameter*: `e <- gamma*lambda*e + grad V(s)`. Same idea, applied
to the weight vector instead of a state table.

---

## Decision Cheat Sheet

| Situation                                   | Use                                  |
|---------------------------------------------|--------------------------------------|
| Episodic task, want unbiased estimates      | Monte Carlo                          |
| Continuing task or want to learn online     | TD(0)                                |
| Strongly Markov problem, want speed         | TD (exploits structure)              |
| Want to tune the bias-variance dial         | n-step or TD(lambda)                 |
| Need online TD with multi-step credit       | TD(lambda) + eligibility traces      |
| Want stability over speed in traces         | Replacing (not accumulating) traces  |
| Want the best of both empirically           | n-step (n ~ 4-8) or lambda ~ 0.9     |
| Moving to control                           | Learn `q`, add epsilon-greedy (ch 04) |
