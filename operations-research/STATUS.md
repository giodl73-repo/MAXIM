# operations-research/ — Status

## Files

| File | Topic | Status |
|------|-------|--------|
| 00-OVERVIEW.md | Landscape: modeling → optimization → decision under uncertainty; the OR pipeline | ✅ |
| 01-LINEAR-PROGRAMMING.md | Standard form, geometry of the feasible polytope, simplex method, complexity | ✅ |
| 02-DUALITY.md | Dual construction, weak/strong duality, complementary slackness, shadow prices | ✅ |
| 03-INTEGER-PROGRAMMING.md | Branch-and-bound, cutting planes, LP relaxation, NP-hardness | ✅ |
| 04-NETWORK-FLOWS.md | Max-flow/min-cut, min-cost flow, assignment; overlap with graph-algorithms | ✅ |
| 05-NONLINEAR-CONVEX.md | Convexity, KKT conditions, gradient/interior-point methods; ML bridge | ✅ |
| 06-QUEUING-THEORY.md | Little's law, M/M/1, M/M/c, Kendall notation, Jackson networks | ✅ |
| 07-SCHEDULING.md | Job-shop, critical path/PERT, list scheduling, approximation bounds | ✅ |
| 08-SIMULATION.md | Monte Carlo, discrete-event simulation, variance reduction, simulate vs solve | ✅ |
| 09-STOCHASTIC-AND-DYNAMIC.md | Dynamic programming, Markov decision processes, stochastic programming | ✅ |

## Completed

2026-06-27 — All 10 content files written. Full coverage: deterministic optimization (LP, duality, IP, network flows, convex) through stochastic and dynamic decision-making (queuing, scheduling, simulation, DP/MDP/stochastic programming).

## Coverage Notes

Operations research is the discipline of mathematical decision-making: building models of systems, optimizing over them, and reasoning under uncertainty. This directory covers the deterministic optimization core (linear, integer, network, and convex programming with full duality theory), the queuing/scheduling/simulation triad for performance and resource analysis, and the stochastic-dynamic layer (DP, MDPs, stochastic programming). Treatment is mathematically rigorous: theorems stated with hypotheses, complexity bounds exact (simplex exponential worst-case but polynomial in practice; interior-point polynomial; strong LP duality under feasibility). Key cross-references: `game-theory/` (LP duality ↔ minimax theorem, MDPs ↔ stochastic games), `numerical-methods/` (interior-point and gradient methods, linear algebra), `control-theory/` (DP ↔ Bellman/HJB, LQR), `machine-learning-theory/` (LP relaxation, convex optimization, gradient descent, RL ↔ MDPs), `probability-statistics/` (Markov chains, Poisson processes, Monte Carlo), and a future `graph-algorithms/` (network flows ↔ max-flow/matching algorithms).
