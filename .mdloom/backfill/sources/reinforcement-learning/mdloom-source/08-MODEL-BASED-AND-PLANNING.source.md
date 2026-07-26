---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "08-MODEL-BASED-AND-PLANNING.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:reinforcement-learning:model-based-and-planning
kind: guide
module: reinforcement-learning
section: reinforcement-learning
title: Model-Based RL and Planning - Dyna, MCTS, AlphaZero, MuZero
status: source-custody
source_custody: partial
current_path: reinforcement-learning/08-MODEL-BASED-AND-PLANNING.md
canonical_path: reinforcement-learning/08-MODEL-BASED-AND-PLANNING.md
backsource_ids: [mdloom-backfill:reinforcement-learning:08-model-based-and-planning, git-history:reinforcement-learning:08-model-based-and-planning]
concepts: [model-based RL, Dyna, MCTS, AlphaGo, AlphaZero, world models, MuZero, planning]
root_concepts: [model-based RL, MCTS]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Model-Based RL and Planning — Dyna, MCTS, AlphaZero, MuZero

## The Big Picture

Model-free methods learn values or policies from real experience. Model-based
methods learn (or are given) a model of the environment `p(s'|s,a)` and `r(s,a)`,
then *plan* against it — simulating possible futures to decide. Planning trades
*compute* for *samples*: instead of acting in the world to learn, you imagine
acting in your model. This is how AlphaGo beat Lee Sedol and how MuZero plays Atari
without even being told the rules.

```
+------------------------------------------------------------------+
|          MODEL-FREE  vs  MODEL-BASED                             |
|                                                                  |
|   MODEL-FREE                       MODEL-BASED                   |
|   ----------                       -----------                   |
|   real experience -> values/policy learn/use model -> PLAN       |
|   sample-hungry                    sample-efficient              |
|   no model error                   suffers model error           |
|   Q-learning, PPO, SAC             Dyna, MCTS, AlphaZero, MuZero |
|                                                                  |
|   DYNA bridges them: use a learned model to GENERATE extra       |
|   experience for a model-free learner.                           |
+------------------------------------------------------------------+
                                 |
                                 v
+------------------------------------------------------------------+
|   PLANNING = using a model to improve a value/policy or to       |
|   SELECT the next action by looking ahead (search/simulation).   |
+------------------------------------------------------------------+
```

**Read it as a compute-vs-samples trade**: a model lets you replace expensive real
interaction with cheap simulated interaction — provided the model is good enough.

---

## Dyna: Integrating Learning and Planning

Dyna (Sutton) is the simplest fusion. Learn a model from real transitions; then
use it to generate *simulated* transitions that feed the *same* model-free update.

```
+------------------------------------------------------------------+
|  DYNA-Q                                                          |
|                                                                  |
|   loop:                                                          |
|     1. act in the REAL world: (s,a,r,s')                         |
|     2. DIRECT RL:  Q-learning update on the real transition      |
|     3. MODEL LEARNING: store model[s,a] = (r, s')                |
|     4. PLANNING: repeat n times:                                 |
|          sample a previously-seen (s,a) from the model           |
|          Q-learning update on the SIMULATED (s,a,r,s')           |
+------------------------------------------------------------------+

   real experience  --> Q  <-- simulated experience (from the model)
        |                          ^
        v                          |
      model  ----------------------'
```

Each real step is amplified into `n+1` updates. **Prioritized sweeping** improves
on this by simulating the transitions with the largest Bellman error first (the
asynchronous-DP idea from ch 02). Dyna's weakness: a wrong model injects wrong
updates, so model error directly corrupts the value function.

---

## Planning by Search: Monte Carlo Tree Search

When the model is a *simulator* (you can roll forward from any state), you can
plan by building a search tree. MCTS is the dominant algorithm — it focuses
search on promising lines without exhaustive enumeration.

```
+------------------------------------------------------------------+
|  MCTS: FOUR PHASES PER SIMULATION                                |
|                                                                  |
|   1. SELECTION   from the root, descend by a tree policy (UCT)   |
|                  until reaching a leaf                           |
|   2. EXPANSION   add one (or more) child nodes at the leaf       |
|   3. SIMULATION  roll out to an outcome (random or a policy)     |
|      (ROLLOUT)   -> a value estimate for the leaf                |
|   4. BACKUP      propagate the result up the path, updating      |
|                  each node's visit count N and value Q           |
+------------------------------------------------------------------+
```

The selection rule is **UCT** — UCB (ch 04) applied to the tree, balancing
exploiting high-value children against exploring under-visited ones:

```
   pick child a maximizing:   Q(s,a)  +  c * sqrt( ln N(s) / N(s,a) )
                              ^exploit       ^explore the under-visited
```

```
            root  (run thousands of simulations)
           / | \
          .  .  .       each node tracks (N visits, Q value)
         /\     /\
        .  .   .  .     UCT steers the search toward strong moves
       (rollouts estimate leaf values; results back up the tree)

   after the budget: play the most-visited (most-trusted) root action.
```

MCTS is **anytime** (more simulations -> better move) and needs no value function
in its pure form — random rollouts suffice. Its power is replacing brute-force
minimax with selective, statistics-guided sampling.

> Bridge — game-theory and search: pure MCTS replaces classical minimax /
> alpha-beta search (`game-theory/`, `games-history/`). Where minimax expands the
> whole tree to a fixed depth, MCTS samples deep lines selectively, which is what
> made large-branching games like Go tractable.

---

## AlphaGo and AlphaZero

AlphaGo combined MCTS with deep networks. AlphaZero distilled it into a single,
general, self-play algorithm that learned Go, chess, and shogi *tabula rasa* —
from nothing but the rules.

```
+------------------------------------------------------------------+
|  ALPHAZERO                                                       |
|                                                                  |
|   ONE network f(s) -> (p, v):                                    |
|     p = policy prior over moves    (guides MCTS expansion)       |
|     v = value estimate of s        (replaces random rollouts)    |
|                                                                  |
|   MCTS uses p and v instead of random rollouts (PUCT selection): |
|   select a maximizing: Q(s,a) + c * p(a) * sqrt(N(s))/(1+N(s,a)) |
|                                    ^ network prior steers search |
|                                                                  |
|   SELF-PLAY LOOP:                                                |
|     1. MCTS (guided by f) plays games against itself             |
|     2. MCTS's visit counts = an IMPROVED policy target pi        |
|     3. train f so p -> pi and v -> game outcome z                |
|     4. better f -> stronger MCTS -> better targets -> repeat     |
+------------------------------------------------------------------+
```

The key insight: **MCTS is a policy-improvement operator.** The network proposes a
policy `p`; MCTS, by searching, produces a *better* policy (the visit-count
distribution `pi`); the network is then trained to imitate that improved policy.
This is GPI (ch 02) with *search* as the improvement step.

```
   policy improvement  =  MCTS search   (makes p better -> pi)
   policy evaluation   =  self-play games  (outcome z trains v)
   -> the same evaluate/improve loop, with planning doing the improving.
```

AlphaZero needs the *true* rules (a perfect simulator). MuZero removes even that.

---

## MuZero: Planning with a Learned Model

MuZero (Schrittwieser et al., 2020) learns its own model — but only the parts
needed for planning. It never reconstructs the environment's observations; it
learns a *latent* dynamics that predicts only reward, value, and policy.

```
+------------------------------------------------------------------+
|  MUZERO: THREE LEARNED FUNCTIONS                                 |
|                                                                  |
|   REPRESENTATION  h: observation o -> latent state s0            |
|   DYNAMICS        g: (s_k, a_k) -> (s_{k+1}, r_{k+1})            |
|   PREDICTION      f: s_k -> (policy p_k, value v_k)              |
|                                                                  |
|   MCTS runs entirely in LATENT space using g and f.              |
|   The latent model is trained ONLY to predict reward, value,     |
|   and policy correctly along real trajectories -- NOT to         |
|   reconstruct pixels. "Value-equivalent" model.                  |
+------------------------------------------------------------------+
```

```
   o --h--> s0 --g--> s1 --g--> s2 ...        (latent rollout)
            |         |         |
            f         f         f
          (p,v)     (p,v)     (p,v)           (predictions to plan on)
```

The radical idea: a model does not need to predict the *world*, only the
quantities that matter for decisions (reward, value, policy). MuZero matched
AlphaZero on board games and exceeded model-free agents on Atari — *without being
given the rules.* This **value-equivalence** principle is the frontier of
model-based RL.

---

## World Models and Learned Simulators

A parallel line learns a *generative* model of the environment and trains the agent
inside the "dream."

```
+------------------------------------------------------------------+
|  WORLD MODELS / DREAMER                                          |
|  -----------------------                                         |
|  - learn a latent dynamics model (often a recurrent/VAE/RSSM)    |
|  - train the policy by IMAGINED rollouts inside the model        |
|    (backprop value gradients through the learned dynamics)       |
|  - extreme sample efficiency: most learning happens "in dreams"  |
|  - Dreamer line: strong on continuous control from pixels        |
+------------------------------------------------------------------+
```

```
  real env (few samples) --> learn world model --> imagine many
                                                    rollouts -->
                            train actor/critic entirely in imagination
```

The distinction from MuZero: world models try to *reconstruct/predict
observations* (a generative model you can roll out and even visualize), whereas
MuZero learns only a decision-relevant latent. Both shift the bulk of learning off
the real environment.

---

## The Spectrum of "How Much Model"

```
+------------------------------------------------------------------+
| MODEL-FREE ......  DYNA  ......  MCTS/AZ  ....  MUZERO  .. WORLD |
|                                                           MODELS |
|  no model      model for      model =         learned      full  |
|              extra data    given          value-      generative |
|                               simulator       equivalent   model |
|                                               latent model       |
|  Q-learn/PPO   Dyna-Q        AlphaZero      MuZero       Dreamer |
+------------------------------------------------------------------+
   <-- more samples needed            more compute/planning -->
   <-- robust to model error          more sensitive to model error |
```

---

## Common Confusion Points

### "Is MCTS reinforcement learning or just search?"

Both. In its pure form (random rollouts) it is a planning/search algorithm needing
only a simulator. In AlphaZero it becomes RL: its visit counts define a policy
improvement step, and self-play generates the training data. The boundary between
planning and learning is exactly what model-based RL blurs.

### "Why does MuZero not predict observations?"

Because reconstructing pixels wastes capacity on detail irrelevant to decisions.
MuZero's model is trained to be *value-equivalent* — it only needs to predict the
reward, value, and policy along real trajectories accurately enough to plan. This
is why it can plan in games like Atari where a full generative model would be
extremely hard.

### "Model-based is more sample-efficient — why not always use it?"

Model error. A learned model is wrong, and planning against a wrong model can
confidently choose bad actions (compounding errors over long rollouts). Model-free
methods are slower but cannot be misled by a bad model. The art is using the model
where it is reliable (short horizons, well-visited regions).

### "How is AlphaZero's self-play related to GPI?"

MCTS search is the policy-improvement operator (it turns the network's prior `p`
into a stronger policy `pi`); self-play game outcomes provide the policy
evaluation signal for the value head. Training the network on both is exactly the
evaluate/improve loop of ch 02, with search doing the improving.

### "Dyna vs experience replay — aren't both reusing data?"

Replay (ch 05) reuses *real* past transitions. Dyna generates *new, simulated*
transitions from a learned model, including for state-action pairs not recently
visited. Replay cannot invent transitions; a model can — at the risk of inventing
wrong ones.

---

## Decision Cheat Sheet

| Situation                                        | Use                             |
|--------------------------------------------------|---------------------------------|
| Have a perfect simulator, discrete moves         | MCTS                            |
| Two-player perfect-information game, learn from scratch | AlphaZero (MCTS + self-play) |
| Same, but no access to the rules / dynamics      | MuZero (learned latent model)   |
| Want to amplify scarce real data, model-free core | Dyna-Q (+ prioritized sweeping) |
| Continuous control, extreme sample efficiency    | World models / Dreamer          |
| Model is unreliable / long horizons              | Stay model-free (ch 04-07)      |
| Large branching factor, anytime decisions        | MCTS (UCT)                       |
| Want planning to improve a learned policy        | MCTS as a policy-improvement operator |
