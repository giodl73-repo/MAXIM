---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "02-DYNAMIC-PROGRAMMING.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:reinforcement-learning:dynamic-programming
kind: guide
module: reinforcement-learning
section: reinforcement-learning
title: Dynamic Programming - Policy Iteration, Value Iteration, GPI
status: source-custody
source_custody: partial
current_path: reinforcement-learning/02-DYNAMIC-PROGRAMMING.md
canonical_path: reinforcement-learning/02-DYNAMIC-PROGRAMMING.md
backsource_ids: [proof-backfill:reinforcement-learning:02-dynamic-programming, git-history:reinforcement-learning:02-dynamic-programming]
concepts: [policy iteration, value iteration, generalized policy iteration, policy evaluation, policy improvement]
root_concepts: [generalized policy iteration]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Dynamic Programming — Policy Iteration, Value Iteration, GPI

## The Big Picture

Dynamic programming solves an MDP *when you have the full model*. It is the
idealized case that every model-free method approximates with samples. The two
classical algorithms — policy iteration and value iteration — are two corners of
one unifying idea: **generalized policy iteration**, the dance between evaluating
a policy and improving it.

```
+------------------------------------------------------------------+
|             GENERALIZED POLICY ITERATION (GPI)                   |
|                                                                  |
|        evaluation                   improvement                  |
|     pi --------------> v_pi    v --------------> greedy(v)       |
|        (make v match pi)          (make pi greedy wrt v)         |
|                                                                  |
|        pi  ===>  v_pi  ===>  pi'  ===>  v_pi'  ===>  ...         |
|                                                                  |
|     The two processes pull toward each other; the fixed point    |
|     of BOTH simultaneously is (pi_*, v_*).                       |
|                                                                  |
|     .----------------.                .------------------.       |
|     | POLICY ITER.   |                | VALUE ITER.      |       |
|     | full eval then |                | one eval sweep   |       |
|     | one improve    |                | folded into max  |       |
|     '----------------'                '------------------'       |
|        two extremes of the SAME loop                             |
+------------------------------------------------------------------+
```

**Read it as a loop**: evaluation makes the value function consistent with the
current policy; improvement makes the policy greedy with respect to the value
function. Iterate and you climb to the optimum.

---

## Building Block 1: Policy Evaluation

Given a fixed policy `pi`, compute `v_pi`. Two routes:

```
  DIRECT (small MDP):   v_pi = (I - gamma P_pi)^{-1} r_pi   [O(|S|^3)]

  ITERATIVE:            repeat the expectation backup until convergence
     v_{k+1}(s) = sum_a pi(a|s) [ r(s,a) + gamma sum_{s'} p(s'|s,a) v_k(s') ]
```

Iterative evaluation is just applying the contraction operator `T_pi` repeatedly:

```
  v_0  --T_pi-->  v_1  --T_pi-->  ...  -->  v_pi
  ||v_k - v_pi||_inf  <=  gamma^k ||v_0 - v_pi||_inf
```

Two sweep styles:

| Style       | Update                                  | Notes                       |
|-------------|-----------------------------------------|-----------------------------|
| Synchronous | new array `v_{k+1}` from old `v_k`      | clean, two arrays           |
| In-place (Gauss-Seidel) | overwrite `v(s)` as you go  | uses fresh values, often faster |

---

## Building Block 2: Policy Improvement

Given `v_pi`, build a better policy by acting greedily one step:

```
  pi'(s)  =  argmax_a  [ r(s,a) + gamma sum_{s'} p(s'|s,a) v_pi(s') ]
          =  argmax_a  q_pi(s, a)
```

The **policy improvement theorem** guarantees this never hurts:

```
+------------------------------------------------------------------+
|  POLICY IMPROVEMENT THEOREM                                      |
|                                                                  |
|  If  q_pi(s, pi'(s))  >=  v_pi(s)   for all s,                   |
|  then  v_pi'(s)  >=  v_pi(s)        for all s.                   |
|                                                                  |
|  Strict at any state => strictly better policy.                  |
|  If equality everywhere => pi already satisfies Bellman          |
|  optimality => pi is optimal.                                    |
+------------------------------------------------------------------+
```

Greedy improvement satisfies the hypothesis by construction (the greedy action's
q-value is at least the policy's average q-value). So each improvement step gives
a policy at least as good — and since there are finitely many deterministic
policies, the process terminates at `pi_*`.

---

## Algorithm 1: Policy Iteration

Alternate *full* evaluation with *one* greedy improvement:

```
+------------------------------------------------------------------+
|  POLICY ITERATION                                                |
|                                                                  |
|  initialize pi arbitrarily                                       |
|  loop:                                                           |
|    1. POLICY EVALUATION:  solve v_pi (to convergence)            |
|    2. POLICY IMPROVEMENT:  pi' = greedy(v_pi)                    |
|    3. if pi' == pi: return pi_* = pi                             |
|       else pi <- pi'                                             |
+------------------------------------------------------------------+

   pi_0 -> v_{pi_0} -> pi_1 -> v_{pi_1} -> ... -> pi_* -> v_*
        E          I        E          I       E
```

**Convergence**: finite MDPs have finitely many deterministic policies; each
iteration strictly improves (or stops), so policy iteration converges in a finite
number of iterations — often very few (single digits), because each improvement
step is a large, global jump. Its cost is the expensive full evaluation inside
each iteration.

---

## Algorithm 2: Value Iteration

Don't bother evaluating each policy fully. Fold a single evaluation sweep and the
improvement into one update — apply the *optimality* operator `T*` directly:

```
+------------------------------------------------------------------+
|  VALUE ITERATION                                                 |
|                                                                  |
|  initialize v arbitrarily                                        |
|  repeat until ||v_{k+1} - v_k||_inf < theta:                     |
|  v_{k+1}(s) = max_a [ r(s,a) + gamma sum_{s'} p(s'|s,a) v_k(s')] |
|  then extract:  pi(s) = argmax_a [ r(s,a) + gamma sum p v(s') ]  |
+------------------------------------------------------------------+
```

This is fixed-point iteration on the contraction `T*`, converging geometrically
to `v_*`. There is no explicit policy until the end — the `max` *is* the implicit
improvement.

### Policy Iteration vs Value Iteration

```
+--------------------------------+--------------------------------+
|  POLICY ITERATION              |  VALUE ITERATION               |
|  ----------------              |  ---------------               |
|  full eval to convergence,     |  one sweep (max) per step      |
|  then one greedy step          |  no separate policy            |
|  few iterations, each costly   |  many cheap iterations         |
|  exact policy each round       |  policy emerges at the end     |
|  uses T_pi then greedy         |  uses T* directly              |
+--------------------------------+--------------------------------+
```

Both are GPI; they differ only in *how much evaluation* happens between
improvements. Truncating evaluation to `k` sweeps gives **modified policy
iteration**, the continuum between them.

---

## The Unifying View: Generalized Policy Iteration

```
                       v_*, pi_*   (joint fixed point)
                          *
                         /|
       greedy(v)        / | evaluation
       improvement     /  | v -> v_pi
                      /   |
              pi ----*    |
                     \    |
                      \   |
        the two lines  \  |
        meet only at    \ |
        optimality       \|
                          *
```

GPI is *any* interleaving of policy evaluation (toward `v_pi`) and policy
improvement (toward greedy). The two constraints conflict everywhere except at
the optimum, where being greedy with respect to your own value function is
*consistent* — that consistency is exactly the Bellman optimality equation. This
abstraction is the backbone of the entire rest of the book:

```
  DP:           full-model evaluation + greedy improvement
  Monte Carlo:  sampled-return evaluation + greedy improvement   (ch 03-04)
  TD / SARSA:   bootstrapped evaluation + epsilon-greedy improve (ch 04)
  Actor-Critic: critic evaluates, actor improves                 (ch 06)
```

Recognizing GPI in a new algorithm tells you immediately what it is doing.

---

## Worked Example: Gridworld Value Iteration

A 1x4 corridor, states `0 1 2 3`, terminal goal at state 3 (reward +1 on
entering it, 0 elsewhere), gamma = 0.9, deterministic moves left/right, walls at
the ends. Start `v = 0` everywhere.

```
  Sweep 1 (each state takes max over left/right):
    v(2) = 0 + 0.9 * v(3=terminal->1 on entry) ... entering 3 gives +1
    v(2) = 1 + 0.9*0 = 1.0      (move right into goal)
    v(1) = 0 + 0.9*v(2)=0   (v(2) still 0 this sweep if synchronous)
  Sweep 2:
    v(2) = 1.0
    v(1) = 0 + 0.9*1.0 = 0.9
  Sweep 3:
    v(0) = 0 + 0.9*0.9 = 0.81
```

Converged values and greedy policy:

```
  state:   0      1      2      3(goal)
  v_*:    0.81   0.9    1.0     -
  pi_*:   ->     ->     ->      -      (always move toward the goal)
```

The value decays by gamma per step away from the goal — `gamma^d` for distance
`d` — exactly the geometric discounting of a single terminal reward.

---

## Efficiency and Asynchronous DP

Full sweeps over `|S|` states are infeasible when `|S|` is astronomical (Go has
~10^170 states). Two escape hatches motivate everything after this chapter:

```
+------------------------------------------------------------------+
|  PROBLEM: full sweeps over all states are impossible at scale.   |
|                                                                  |
|  ESCAPE 1: ASYNCHRONOUS DP                                       |
|    update states in any order, even repeatedly; still converges  |
|    if every state is updated infinitely often.                   |
|                                                                  |
|  ESCAPE 2: SAMPLE instead of sweep     -> Monte Carlo / TD (ch3) |
| ESCAPE 3: APPROXIMATE v instead of tabulate -> func approx (ch5) |
+------------------------------------------------------------------+
```

Asynchronous DP also justifies prioritized updates (sweep states with large
Bellman error first) — the seed of *prioritized experience replay* in DQN (ch 05)
and of *prioritized sweeping* in Dyna (ch 08).

> Bridge — operations research: this is exactly the dynamic-programming
> treatment of finite MDPs in `operations-research/09-STOCHASTIC-AND-DYNAMIC.md`.
> The difference downstream is that OR usually keeps the model; RL drops it and
> learns from samples. Value iteration is also the discrete analogue of solving
> the Hamilton-Jacobi-Bellman equation in `control-theory/`.

---

## Common Confusion Points

### "Why does policy iteration converge in so few steps?"

Each improvement is a *global* greedy step over all states at once — a large jump
in policy space. The number of distinct deterministic policies is finite, and you
never revisit one, so termination is fast. The cost is hidden inside the full
evaluation each round.

### "Is value iteration just policy iteration with one evaluation sweep?"

Almost. Value iteration folds the single sweep and the improvement into one `max`
backup, never materializing an intermediate policy. Truncating evaluation to `k`
sweeps (modified policy iteration) interpolates continuously between the two.

### "Do I need the reward and transition model?"

Yes — DP is the *model-based, model-known* corner. Both the improvement step
(`argmax` over a one-step lookahead) and the evaluation step require `p` and `r`.
Removing that requirement is the entire reason ch 03 onward exists.

### "Synchronous vs in-place updates — does it matter?"

Both converge. In-place (Gauss-Seidel) often converges faster because later
updates in a sweep use already-improved values, but it makes the iterates
order-dependent. Asynchronous DP generalizes this: update any state any time, as
long as none is starved.

---

## Decision Cheat Sheet

| Situation                                  | Use                                   |
|--------------------------------------------|---------------------------------------|
| Known small MDP, want exact optimum        | Policy iteration or value iteration   |
| Evaluation is cheap, want fewest iterations | Policy iteration                     |
| Evaluation is expensive, want simplicity   | Value iteration                       |
| Want a tunable middle ground               | Modified policy iteration (k sweeps)  |
| State space too large to sweep             | Async DP / sample (ch 03) / approx (ch 05) |
| Some states matter more                    | Prioritized / asynchronous sweeps     |
| Need a policy without a model              | You cannot use DP — go to ch 04       |
