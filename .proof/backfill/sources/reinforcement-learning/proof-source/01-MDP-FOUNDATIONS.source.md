---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "01-MDP-FOUNDATIONS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:reinforcement-learning:mdp-foundations
kind: guide
module: reinforcement-learning
section: reinforcement-learning
title: MDP Foundations - Returns, Value Functions, Bellman Equations
status: source-custody
source_custody: partial
current_path: reinforcement-learning/01-MDP-FOUNDATIONS.md
canonical_path: reinforcement-learning/01-MDP-FOUNDATIONS.md
backsource_ids: [proof-backfill:reinforcement-learning:01-mdp-foundations, git-history:reinforcement-learning:01-mdp-foundations]
concepts: [markov decision process, return, discounting, value function, bellman equation, bellman optimality]
root_concepts: [markov decision process, bellman equation]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# MDP Foundations — Returns, Value Functions, Bellman Equations

## The Big Picture

Everything in RL is the consequence of one recursive identity. The Markov
Decision Process gives the objects; the Bellman equations relate them; the rest
of the field is how to solve those equations when you cannot write them down in
full.

```
+------------------------------------------------------------------+
|                      THE MDP STACK                               |
|                                                                  |
|  (S, A, p(s',r|s,a), gamma)        <- the MDP tuple              |
|            |                                                     |
|            v                                                     |
|  return  G_t = r_{t+1} + gamma r_{t+2} + ...   <- objective      |
|            |                                                     |
|            v                                                     |
|  value   v_pi(s) = E_pi[G_t | S_t = s]         <- prediction     |
|  q-value q_pi(s,a) = E_pi[G_t | S_t=s, A_t=a]                    |
|            |                                                     |
|            v                                                     |
|  BELLMAN EXPECTATION:   v_pi = r + gamma P_pi v_pi  (linear)     |
|            |                                                     |
|            v                                                     |
|  BELLMAN OPTIMALITY:    v_* = max_a [ r + gamma E v_* ] (nonlin) |
|            |                                                     |
|            v                                                     |
|  optimal policy  pi_*(s) = argmax_a q_*(s,a)   <- the goal       |
+------------------------------------------------------------------+
```

**Read top-down**: the tuple defines the world, the return defines success,
value functions summarize it, and the two Bellman equations are the fixed-point
conditions every algorithm is secretly solving.

---

## The Markov Decision Process

An MDP is the tuple `(S, A, p, gamma)`:

```
+------------------------------------------------------------------+
|  S            set of states                                      |
|  A            set of actions (A(s) if state-dependent)           |
|  p(s',r|s,a)  dynamics: joint prob of next state and reward      |
|  gamma        discount factor in [0,1)                           |
+------------------------------------------------------------------+
```

The dynamics function is the complete model. From it we derive everything else:

```
  state transition:   p(s'|s,a)   = sum_r  p(s',r | s,a)
  expected reward:    r(s,a)      = sum_{s',r} r * p(s',r | s,a)
```

**The Markov property** is the load-bearing assumption:

```
  P[S_{t+1}, R_{t+1} | S_t, A_t]  =  P[S_{t+1}, R_{t+1} | S_0,A_0,...,S_t,A_t]
```

The state is a *sufficient statistic* of history: the future is conditionally
independent of the past given the present. This is exactly the Markov assumption
you know from Markov chains, with an action and a reward bolted on. When the true
state is not observable you have a POMDP (ch 09) and must reconstruct a belief
state — but the entire core theory assumes full observability.

> Bridge — control theory: an MDP is a stochastic optimal control problem in
> discrete time. `S` is the state, `A` the control input, `p` the (stochastic)
> plant dynamics, and `-r` the cost. The Bellman optimality equation is the
> discrete-time, stochastic analogue of the Hamilton-Jacobi-Bellman PDE. See
> `control-theory/`.

---

## Returns and Discounting

The agent maximizes the **return**, the cumulative future reward. The discounted
infinite-horizon return is the workhorse:

```
  G_t  =  R_{t+1} + gamma R_{t+2} + gamma^2 R_{t+3} + ...
       =  sum_{k=0}^{inf}  gamma^k  R_{t+k+1}
```

The recursive form is what makes the Bellman machinery possible:

```
  G_t  =  R_{t+1} + gamma G_{t+1}
```

### Why discount?

```
+------------------------------------------------------------------+
|  REASON                          CONSEQUENCE                     |
|  ------                          -----------                     |
|  Mathematical convergence        gamma<1 => geometric series     |
|                                  bounded if |r| <= R_max         |
|  Uncertainty about the future    soft horizon ~ 1/(1-gamma)      |
|  Models economic/biological      a reward now > a reward later   |
|     preference for sooner reward                                 |
+------------------------------------------------------------------+
```

With `|R| <= R_max`, the return is bounded: `|G_t| <= R_max / (1 - gamma)`. The
quantity `1/(1-gamma)` is the *effective horizon* — gamma = 0.99 looks roughly
100 steps ahead. Choosing gamma is choosing how far-sighted the agent is, and it
materially changes the optimal policy, not just convergence speed.

| Setting          | Return                          | Notes                         |
|------------------|---------------------------------|-------------------------------|
| Episodic         | sum to terminal state           | natural horizon; gamma can = 1 |
| Continuing, discounted | gamma < 1 infinite sum    | the default                   |
| Continuing, average-reward | lim (1/T) sum r_t       | advanced; avoids gamma choice  |

---

## Value Functions

A policy `pi(a|s)` induces two value functions — the expected return:

```
  STATE VALUE:        v_pi(s)   = E_pi[ G_t | S_t = s ]
  ACTION VALUE:       q_pi(s,a) = E_pi[ G_t | S_t = s, A_t = a ]
```

They are linked by the policy and by a one-step lookahead:

```
  v_pi(s)   = sum_a pi(a|s) q_pi(s,a)               (average over actions)

  q_pi(s,a) = r(s,a) + gamma sum_{s'} p(s'|s,a) v_pi(s')   (one step + value)
```

The diagram is the *backup* — the flow of value from successor states back to the
current one:

```
              s                        (state node)
            / | \
       a1  /  |a2 \ a3                  pi(a|s)
          v   v    v
        .q.  .q.  .q.                   action nodes  q_pi(s,a)
        /\   /\    /\
       /  \ /  \  /  \  r, p(s'|s,a)
      s'  s' s' s' s' s'                (successor states v_pi(s'))
```

---

## The Bellman Expectation Equation

Substitute the two relations into each other and you get the defining recursion
for a *fixed* policy:

```
+------------------------------------------------------------------+
|  BELLMAN EXPECTATION EQUATION (state value)                      |
|                                                                  |
|  v_pi(s) = sum_a pi(a|s) [ r(s,a)                                |
|                          + gamma sum_{s'} p(s'|s,a) v_pi(s') ]   |
+------------------------------------------------------------------+
```

In vector form over the finite state space this is **linear**:

```
  v_pi  =  r_pi  +  gamma P_pi v_pi          (P_pi = transition matrix under pi)
  =>  v_pi  =  (I - gamma P_pi)^{-1} r_pi    (closed-form solution!)
```

For a known, small MDP you can solve a fixed policy's value by inverting an
`|S| x |S|` matrix. `(I - gamma P_pi)` is invertible because gamma < 1 makes the
spectral radius of `gamma P_pi` less than 1. This is the foundation of *policy
evaluation* (ch 02).

The action-value form:

```
  q_pi(s,a) = r(s,a) + gamma sum_{s'} p(s'|s,a) sum_{a'} pi(a'|s') q_pi(s',a')
```

---

## The Bellman Optimality Equation

The optimal value function `v_*(s) = max_pi v_pi(s)` does not average over actions
— it *maximizes*. That `max` makes the equation **nonlinear**, with no closed form:

```
+------------------------------------------------------------------+
|  BELLMAN OPTIMALITY EQUATION                                     |
|                                                                  |
|  v_*(s)   = max_a [ r(s,a) + gamma sum_{s'} p(s'|s,a) v_*(s') ]  |
|                                                                  |
| q_*(s,a) = r(s,a) + gamma sum_{s'} p(s'|s,a) max_{a'} q_*(s',a') |
+------------------------------------------------------------------+
```

The optimal policy is then *greedy* with respect to `q_*`:

```
  pi_*(s)  =  argmax_a  q_*(s,a)
```

A profound fact (Bellman's principle of optimality): a deterministic optimal
policy *always exists* for a finite MDP, and acting greedily with respect to
`v_*` (with a one-step model) or `q_*` (no model needed) is optimal. This is why
so much of RL chases `q_*`: it converts the global, multi-step optimization into
a local, one-step `argmax`.

### Expectation vs Optimality, side by side

```
+--------------------------------+--------------------------------+
|  BELLMAN EXPECTATION           |  BELLMAN OPTIMALITY            |
|  --------------------          |  -------------------           |
|  evaluates a fixed pi          |  finds the best pi             |
|  sum_a pi(a|s) (...)           |  max_a (...)                   |
|  LINEAR in v                   |  NONLINEAR (max) in v          |
| closed form via matrix inverse |  no closed form; iterate       |
|  -> policy evaluation          |  -> value iteration            |
+--------------------------------+--------------------------------+
```

---

## The Bellman Operator and Why Iteration Works

Define the Bellman optimality operator `T*` on value functions:

```
  (T* v)(s)  =  max_a [ r(s,a) + gamma sum_{s'} p(s'|s,a) v(s') ]
```

`T*` is a **gamma-contraction** in the max-norm:

```
  || T* u  -  T* v ||_inf   <=   gamma  || u - v ||_inf
```

By the Banach fixed-point theorem, repeatedly applying `T*` converges
geometrically to the unique fixed point `v_*`, from *any* starting `v`. The same
holds for the expectation operator `T_pi` with fixed point `v_pi`.

```
   v_0  --T*-->  v_1  --T*-->  v_2  -->  ...  -->  v_*
   ||v_k - v_*||  <=  gamma^k ||v_0 - v_*||      (geometric)
```

This single contraction property is *why every value-based method converges* in
the tabular case — value iteration, Q-learning, TD — and its breakdown under
function approximation is exactly the deadly triad (ch 05).

> Bridge — numerical analysis: this is fixed-point iteration `x = T(x)` with a
> contraction mapping, identical in spirit to Jacobi iteration for linear
> systems. gamma plays the role of the spectral radius bound. See
> `numerical-methods/`.

---

## Worked Example: A Two-State MDP

States `{A, B}`, two actions `{stay, switch}`, gamma = 0.9. Deterministic
dynamics, rewards as shown:

```
  stay@A   -> A, r = +1
  switch@A -> B, r =  0
  stay@B   -> B, r = +2
  switch@B -> A, r =  0
```

Intuitively B is the better state (+2 vs +1). The optimal policy should reach and
stay in B. Solve the optimality equations:

```
  v_*(B) = max{ 2 + 0.9 v_*(B),  0 + 0.9 v_*(A) }   <- "stay" should win
  v_*(A) = max{ 1 + 0.9 v_*(A),  0 + 0.9 v_*(B) }   <- "switch" should win
```

Guess pi_*: stay@B, switch@A. Then:

```
  v_*(B) = 2 + 0.9 v_*(B)        =>  v_*(B) = 2 / 0.1 = 20
  v_*(A) = 0 + 0.9 v_*(B)        =>  v_*(A) = 0.9 * 20 = 18
```

Verify the maxes hold:

```
  at A: stay = 1 + 0.9*18 = 17.2  vs  switch = 0 + 0.9*20 = 18.0  -> switch wins. OK
  at B: stay = 2 + 0.9*20 = 20.0  vs  switch = 0 + 0.9*18 = 16.2  -> stay wins.   OK
```

So `v_* = (18, 20)`, `pi_* = (switch, stay)`. The greedy policy with respect to
`v_*` is optimal, exactly as the theory promises.

---

## Common Confusion Points

### "Why is the expectation equation linear but the optimality one isn't?"

The expectation equation *averages* over actions with fixed weights `pi(a|s)` — a
linear operation, so `v_pi = r + gamma P_pi v_pi` is a linear system. The
optimality equation takes a `max` over actions, which is piecewise-linear and
convex but not linear. No matrix inverse exists; you iterate.

### "v vs q — when do I need which?"

```
  v(s)    needs a model to act greedily:
          pi(s) = argmax_a [ r(s,a) + gamma sum p(s'|s,a) v(s') ]
  q(s,a)  acts greedily with NO model:
          pi(s) = argmax_a q(s,a)
```

This is precisely why model-free control (ch 04) learns `q`, not `v`: with `q`
you can choose actions without ever knowing the dynamics.

### "Does the optimal policy depend on gamma?"

Yes — not just convergence speed. A small gamma makes the agent myopic and can
flip which action is optimal in a state. gamma is a *modeling choice* about
horizon, not a free hyperparameter to tune for speed alone.

### "Is the optimal policy unique?"

The optimal *value function* `v_*` is unique. The optimal *policy* need not be —
ties in the `argmax` give multiple optimal policies. But at least one
deterministic optimal policy always exists for a finite MDP.

---

## Decision Cheat Sheet

| I have / want...                          | Use                                   |
|-------------------------------------------|---------------------------------------|
| A known small MDP, want a fixed policy's value | Bellman expectation, matrix inverse |
| A known MDP, want the optimal value       | Bellman optimality, iterate `T*` (ch 02) |
| To act without a model                    | Learn `q`, act greedily               |
| To act with a model                       | Learn `v`, one-step lookahead         |
| To reason about convergence               | gamma-contraction in max-norm         |
| To set the planning horizon               | gamma; effective horizon ~ 1/(1-gamma) |
| A non-Markovian / partially observed task | Reconstruct state / belief (POMDP, ch 09) |
