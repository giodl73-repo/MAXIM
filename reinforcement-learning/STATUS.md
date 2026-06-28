# reinforcement-learning/ — Status

## Files

| File                              | Topic                                                       | Status |
|-----------------------------------|-------------------------------------------------------------|--------|
| 00-OVERVIEW.md                    | The RL Landscape: Agent-Environment Loop and Taxonomy       | ✅ |
| 01-MDP-FOUNDATIONS.md             | MDPs, Returns, Value Functions, Bellman Equations           | ✅ |
| 02-DYNAMIC-PROGRAMMING.md         | Policy Iteration, Value Iteration, GPI                      | ✅ |
| 03-MONTE-CARLO-AND-TD.md          | MC, TD(0), TD(λ), Eligibility Traces, Bias/Variance         | ✅ |
| 04-MODEL-FREE-CONTROL.md          | SARSA vs Q-Learning, On/Off-Policy, Exploration             | ✅ |
| 05-FUNCTION-APPROXIMATION.md      | Linear Approximation, the Deadly Triad, DQN                 | ✅ |
| 06-POLICY-GRADIENTS.md            | Policy Gradient Theorem, REINFORCE, Actor-Critic, GAE       | ✅ |
| 07-DEEP-RL.md                     | TRPO, PPO, DDPG/TD3, SAC and Max-Entropy RL                 | ✅ |
| 08-MODEL-BASED-AND-PLANNING.md    | Dyna, MCTS, AlphaGo/AlphaZero, World Models, MuZero         | ✅ |
| 09-FRONTIERS-AND-APPLICATIONS.md  | Offline RL, Multi-Agent, RLHF, Reward Hacking, Applications | ✅ |

## Coverage Notes

Reinforcement learning treated as its own field: sequential decision-making
under uncertainty, learned from interaction rather than from a labeled corpus.
The directory builds on the MDP formalism (also touched in
`operations-research/09-STOCHASTIC-AND-DYNAMIC.md` from the dynamic-programming
and optimal-control angle) but develops it toward *model-free* control, policy
gradients, and deep RL — the parts that distinguish RL from classical OR. It is
deliberately not a re-derivation of generic supervised learning; it
cross-references `machine-learning-theory/` for generalization and
`ai-engineering/` for the RLHF post-training pipeline. Bridges run to
`control-theory/` (optimal control, LQR, the Hamilton-Jacobi-Bellman equation),
`operations-research/` (dynamic programming, stochastic approximation), and
`game-theory/` (multi-agent equilibria, self-play). The mathematical spine is
the Bellman equation in its expectation and optimality forms, the on-policy /
off-policy distinction, the TD-vs-MC bias-variance trade-off, the deadly triad,
the policy gradient theorem, and the trust-region / clipped-objective / maximum-
entropy families of modern policy optimization.
