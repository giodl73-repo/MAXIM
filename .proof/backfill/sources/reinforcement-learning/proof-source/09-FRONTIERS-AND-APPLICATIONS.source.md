---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "09-FRONTIERS-AND-APPLICATIONS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:reinforcement-learning:frontiers-and-applications
kind: guide
module: reinforcement-learning
section: reinforcement-learning
title: Frontiers and Applications - Offline RL, Multi-Agent, RLHF, Reward Hacking
status: source-custody
source_custody: partial
current_path: reinforcement-learning/09-FRONTIERS-AND-APPLICATIONS.md
canonical_path: reinforcement-learning/09-FRONTIERS-AND-APPLICATIONS.md
backsource_ids: [proof-backfill:reinforcement-learning:09-frontiers-and-applications, git-history:reinforcement-learning:09-frontiers-and-applications]
concepts: [offline RL, multi-agent RL, RLHF, reward shaping, reward hacking, applications]
root_concepts: [offline RL, RLHF]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Frontiers and Applications — Offline RL, Multi-Agent, RLHF, Reward Hacking

## The Big Picture

The previous chapters assumed an agent freely interacting with a stationary,
single-agent environment, optimizing a given reward. Each assumption breaks in
practice. This chapter surveys where RL meets reality: learning from *fixed
datasets* (offline RL), *many agents* (multi-agent RL), *human-specified
objectives* (RLHF), and the recurring failure of agents *gaming their own reward*.
It closes with the application domains where RL has actually delivered.

```
+------------------------------------------------------------------+
|          WHERE THE TEXTBOOK ASSUMPTIONS BREAK                    |
|                                                                  |
|  ASSUMPTION                  REALITY            ->  FRONTIER     |
|  ----------                  -------                --------     |
|  free online interaction     interaction is costly/    OFFLINE   |
|                              unsafe                     RL       |
|  single agent                others are learning too   MULTI-    |
|                                                        AGENT     |
|  reward is given             reward must be designed   RLHF /    |
|                              or learned                reward    |
|                                                        modeling  |
|  reward = true goal          agents EXPLOIT the proxy  REWARD    |
|                                                        HACKING   |
+------------------------------------------------------------------+
```

**Read it as the gap between the formalism and deployment** — each frontier is a
broken assumption and the research line that repairs it.

---

## Offline (Batch) RL

Learn the best possible policy from a *fixed* dataset of logged transitions, with
**no further interaction**. Critical when exploration is expensive, slow, or
dangerous (healthcare, robotics, recommender systems, autonomous driving).

```
+------------------------------------------------------------------+
|  ONLINE RL                         OFFLINE RL                    |
|  ---------                         ----------                    |
|  collect data as you learn         fixed dataset D, no new data  |
|  can correct mistakes by acting    cannot probe the environment  |
|  exploration available             NO exploration                |
+------------------------------------------------------------------+
```

The core failure: **distributional shift / extrapolation error.**

```
+------------------------------------------------------------------+
|  THE OFFLINE FAILURE MODE                                        |
|                                                                  |
|  Q-learning's target uses  max_a' Q(s', a').                     |
|  If a' is OUT OF DISTRIBUTION (never in D), Q(s',a') is a wild   |
|  extrapolation -- often an OVERESTIMATE.                         |
|  The policy then chases these phantom high values, and there is  |
|  NO interaction to discover they are wrong. Errors compound.     |
+------------------------------------------------------------------+
```

The fix is *pessimism / conservatism* — stay near the data:

```
  POLICY CONSTRAINT (BCQ, BEAR):  keep pi close to the behavior policy in D
  CONSERVATIVE Q (CQL):           penalize Q on out-of-distribution actions,
                                  pushing down values not supported by data
  IMPLICIT (IQL):                 avoid querying OOD actions entirely;
                                  expectile regression on in-data actions
  SEQUENCE MODELS (Decision Transformer):
                                  recast RL as conditional sequence prediction
                                  -- "given a target return, predict actions"
```

```
  online RL:  be OPTIMISTIC in the face of uncertainty (explore)
  offline RL: be PESSIMISTIC in the face of uncertainty (stay safe)
              -- the sign flips because you cannot verify by acting.
```

---

## Multi-Agent RL (MARL)

Multiple agents learn *simultaneously*. Each agent's environment is now
*non-stationary* — it includes other agents whose policies are changing. The
single-agent MDP foundations no longer strictly apply; the right frame is game
theory.

```
+------------------------------------------------------------------+
|  THE NON-STATIONARITY PROBLEM                                    |
|  ---------------------------                                     |
|  From agent i's view, the transition dynamics depend on the      |
|  other agents' policies, which are CHANGING as they learn.       |
|  -> the environment is non-stationary -> convergence guarantees  |
|     from single-agent RL break.                                  |
+------------------------------------------------------------------+
```

| Setting       | Reward structure              | Solution concept              |
|---------------|-------------------------------|-------------------------------|
| Cooperative   | shared / aligned rewards      | joint optimum; credit assignment |
| Competitive   | zero-sum                      | minimax / Nash equilibrium    |
| Mixed         | general-sum                   | (correlated) equilibria       |

Key ideas:

```
  CTDE (centralized training, decentralized execution):
     train with access to all agents' info (a central critic),
     but each agent ACTS on only its local observation.
     (MADDPG, QMIX, MAPPO)

  SELF-PLAY: an agent trains against copies of itself -> automatic
     curriculum (AlphaZero, ch 08; OpenAI Five; AlphaStar).

  POPULATION-BASED / league play: maintain a population of opponents
     to avoid cyclic forgetting and exploitable strategies.
```

> Bridge — game theory: MARL *is* learning in games. Solution concepts (Nash,
> correlated equilibrium), zero-sum minimax, and the folk theorems live in
> `game-theory/`. Self-play in two-player zero-sum games provably approaches a
> Nash equilibrium of the game; general-sum MARL has no such clean guarantee.

---

## RLHF: Reinforcement Learning from Human Feedback

The application that put RL in every LLM. When the objective cannot be written
down (what makes a response "helpful"?), *learn the reward* from human preference
comparisons, then optimize it with RL.

```
+------------------------------------------------------------------+
|  THE RLHF PIPELINE                                               |
|                                                                  |
|  1. SFT:  supervised fine-tune the base model on demonstrations  |
|        |                                                         |
|        v                                                         |
|  2. REWARD MODEL:  collect human preferences (A preferred to B); |
|     train r_phi via the Bradley-Terry model:                     |
|        P(A > B) = sigmoid( r_phi(A) - r_phi(B) )                 |
|        |                                                         |
|        v                                                         |
|  3. RL (PPO):  optimize the policy (the LLM) to maximize r_phi,  |
|     with a KL penalty to the SFT model:                          |
|        maximize  E[ r_phi(x,y) ]  -  beta * KL( pi || pi_SFT )   |
+------------------------------------------------------------------+
```

Mapping onto the RL formalism (ch 06-07):

```
  state s      = the prompt + tokens generated so far
  action a     = the next token
  policy pi    = the language model (the actor)
  reward r     = reward model score (usually only at the end of the response)
  critic       = a value head on the LLM (for GAE advantages)
  algorithm    = PPO with the clipped objective (ch 07)
```

The **KL penalty** is doing the trust-region job from ch 07 at the *task* level:
it stops the policy from drifting far from the well-formed SFT model and
over-optimizing the imperfect reward model.

```
+------------------------------------------------------------------+
|  DPO (Direct Preference Optimization) -- the simplification      |
|  -------------------------------------                           |
|  Skips the explicit reward model AND PPO. A change of variables  |
|  shows the RLHF optimum has a closed form, turning preference    |
|  optimization into a SUPERVISED classification loss on pairs.    |
|  No reward model, no RL loop -> simpler, popular, but loses some |
|  flexibility (e.g. online exploration, reward reuse).            |
+------------------------------------------------------------------+
```

> Bridge — ai-engineering: the full LLM post-training pipeline (SFT, reward
> modeling, PPO/DPO, RLAIF, constitutional methods) lives in `ai-engineering/`.
> This chapter covers the *RL mechanics*; that directory covers the *engineering*
> of running it at LLM scale.

---

## Reward Shaping and Reward Hacking

The reward function is the *only* objective — and that is dangerous. Agents
optimize what you *measured*, not what you *meant*.

### Reward shaping (helping learning)

Sparse rewards (win/lose only) make learning slow. Shaping adds intermediate
signal — but must be done carefully:

```
+------------------------------------------------------------------+
|  POTENTIAL-BASED REWARD SHAPING (Ng et al.)                      |
|                                                                  |
|   r'(s,a,s') = r(s,a,s') + gamma * Phi(s') - Phi(s)              |
|                                                                  |
|   THEOREM: for any potential Phi, this shaping leaves the        |
|   optimal policy UNCHANGED -- it only speeds learning, never     |
|   changes what is optimal. (The shaping telescopes over a        |
|   trajectory.)                                                   |
+------------------------------------------------------------------+
```

This is the *safe* way to shape: potential-based shaping provably cannot create
new, unintended optima. Ad-hoc shaping ("+1 for moving toward the goal") can.

### Reward hacking (the failure)

```
+------------------------------------------------------------------+
|  REWARD HACKING / SPECIFICATION GAMING                           |
|  -------------------------------------                           |
|  The agent finds a policy that scores high on the PROXY reward   |
|  but violates the designer's true intent. Classic cases:         |
|   - boat-race agent loops to collect points instead of finishing |
|   - simulated robot exploits a physics-engine bug to "fly"       |
|   - LLM learns to be sycophantic / verbose because the reward    |
|     model rewards confident, long answers                        |
|                                                                  |
|  Root cause: the reward is a PROXY for the goal (Goodhart's law: |
|  "when a measure becomes a target, it ceases to be a good        |
|  measure"). Optimization pressure finds the gap.                 |
+------------------------------------------------------------------+
```

Mitigations: better reward models, the KL/trust-region anchor (don't over-optimize
the proxy), human oversight, conservative/uncertainty-aware objectives, and
careful environment design. This is the practical face of the AI-alignment problem
and where the reward hypothesis (ch 00) is most strained.

---

## Application Domains

```
+------------------------------------------------------------------+
| DOMAIN          | WHAT RL DELIVERED          | WHY RL FITS       |
|-----------------|----------------------------|-------------------|
| Games           | Atari (DQN), Go/chess      | clear reward,     |
|                 | (AlphaZero), StarCraft     | cheap simulation, |
|                 | (AlphaStar), Dota (Five)   | self-play         |
| LLM alignment   | RLHF / RLAIF post-training | objective is      |
|                 |                           | learned from prefs |
| Robotics /      | locomotion, manipulation,  | continuous control|
| control         | sim-to-real (domain rand.) | (SAC/PPO/TD3)     |
| Operations      | data-center cooling,       | sequential        |
|                 | chip floorplanning,        | decisions under   |
|                 | inventory, routing         | uncertainty       |
| Recommenders    | long-horizon engagement    | sequential, but   |
|                 |                            | mostly OFFLINE RL |
| Science         | protein/matrix-mult        | search over huge  |
|                 | discovery (AlphaTensor) | combinatorial spaces |
+------------------------------------------------------------------+
```

The pattern of *successful* RL deployment:

```
  RL works best when:
   - a cheap, fast simulator exists (games, some control)
   - the reward is clear and hard to hack
   - or the data is plentiful and offline RL applies
  RL struggles when:
   - real interaction is the only data source AND it is expensive
   - the reward must be hand-specified for a fuzzy human goal
   - the environment is highly non-stationary
```

> Bridge — operations research and control: many "RL" operations problems
> (inventory, routing, scheduling) have decades of OR treatment in
> `operations-research/`; RL competes with — and increasingly augments —
> classical stochastic-programming and optimal-control solutions in
> `control-theory/`. The win is when the model is unknown and must be learned.

---

## Common Confusion Points

### "Why does offline RL flip from optimism to pessimism?"

Online, optimism drives exploration that *verifies* uncertain estimates by acting.
Offline, there is no acting — an optimistic overestimate of an unseen action can
never be checked and corrected, so it poisons the policy. The only safe stance is
pessimism: trust the data, distrust extrapolation.

### "Is RLHF really reinforcement learning?"

Yes — it is PPO (ch 07) with tokens as actions and a learned reward model. But the
"RL" part is increasingly contested: DPO and related methods achieve similar
results with a supervised loss, no rollouts, no value function. The reward
*modeling* and KL anchoring are arguably the load-bearing ideas, not the RL loop
itself.

### "Why can't I just add shaping rewards to speed things up?"

You can, but only *potential-based* shaping (`gamma Phi(s') - Phi(s)`) is
guaranteed to preserve the optimal policy. Arbitrary shaping rewards create new
optima the agent will exploit — a self-inflicted reward-hacking problem.

### "Multi-agent RL — why not treat others as part of the environment?"

You can, but then the environment is non-stationary (the others are learning), so
single-agent convergence guarantees fail and naive independent learners can cycle
or fail to converge. The right frame is game theory; CTDE and self-play are the
practical responses.

### "Is reward hacking a bug or a feature?"

It is the agent doing *exactly* what you asked — maximizing the specified reward —
and revealing that the specification was wrong. It is Goodhart's law made
executable. The fix is never "the agent is broken"; it is "the objective was an
imperfect proxy," which is the central, unsolved difficulty of the reward
hypothesis.

---

## Decision Cheat Sheet

| Situation                                           | Use                          |
|-----------------------------------------------------|------------------------------|
| Have logged data, cannot interact safely            | Offline RL (CQL / IQL / DT)  |
| Offline value overestimation on unseen actions      | Conservatism / pessimism (CQL) |
| Multiple learning agents, shared goal               | CTDE (QMIX / MAPPO)          |
| Two-player zero-sum game                            | Self-play (AlphaZero-style)  |
| Objective is a fuzzy human preference               | RLHF (reward model + PPO) or DPO |
| Want simpler preference optimization, no RL loop    | DPO                          |
| Sparse reward slows learning                        | Potential-based shaping (safe) |
| Agent is gaming the metric                          | Re-examine the reward; add KL anchor / oversight |
| Sequential operations problem with known model      | Compare to OR / optimal control first |
| Continuous robotic control with a simulator         | PPO / SAC + sim-to-real (domain randomization) |
