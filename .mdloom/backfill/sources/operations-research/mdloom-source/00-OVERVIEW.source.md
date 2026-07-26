---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:operations-research:overview
kind: guide
module: operations-research
section: operations-research
title: Operations Research - Landscape Overview
status: source-custody
source_custody: partial
current_path: operations-research/00-OVERVIEW.md
canonical_path: operations-research/00-OVERVIEW.md
backsource_ids: [mdloom-backfill:operations-research:00-overview, git-history:operations-research:00-overview]
concepts: [overview, operations research, mathematical optimization, decision theory]
root_concepts: [overview]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Operations Research — Landscape Overview

## The Big Picture

Operations research (OR) is the discipline of making **optimal decisions** about real systems by reducing them to mathematics. The pipeline is always the same: take a messy decision (route trucks, staff a call center, schedule jobs, allocate capital), write it as a **model** (variables, objective, constraints), **solve** the model with an algorithm whose properties you understand, and then **interpret** the solution — including how it shifts when the world changes.

```
+----------------------------------------------------------------------+
|                    THE OPERATIONS RESEARCH PIPELINE                   |
|                                                                      |
|   REAL SYSTEM        MODEL              SOLVE             INTERPRET   |
|   -----------        -----              -----             ---------   |
|   "Route the    ->   min c'x       ->   simplex /    ->   shadow      |
|    fleet"            s.t. Ax <= b        interior-pt       prices,    |
|                          x >= 0          branch&bound      sensitivity|
|                                                                      |
|   measured in        decision vars,      algorithm with    dual vals, |
|   $, time, risk      objective fn,       known complexity  what-ifs,  |
|                      feasible region     & guarantees      robustness |
+----------------------------------------------------------------------+
        |                    |                   |              |
        v                    v                   v              v
  DETERMINISTIC?      CONTINUOUS or        EXACT or         CERTAIN or
  or STOCHASTIC?      DISCRETE vars?       APPROXIMATE?     UNCERTAIN data?
```

**Read this top-down**: every OR problem walks left-to-right. The art is the modeling step; the science is choosing a solver whose complexity and optimality guarantees match the model class; the value is in the interpretation.

The library splits OR into three strata, which this directory's files traverse in order:

```
+----------------------------------------------------------------------+
|  STRATUM 1: DETERMINISTIC OPTIMIZATION  (data known exactly)         |
|    01 Linear Programming      — continuous, linear, convex polytope  |
|    02 Duality                 — the shadow economy of every LP       |
|    03 Integer Programming     — discrete vars, NP-hard               |
|    04 Network Flows           — structured LPs, integral, fast       |
|    05 Nonlinear / Convex      — smooth objectives, KKT, interior-pt  |
+----------------------------------------------------------------------+
                              |
                              v
+----------------------------------------------------------------------+
|  STRATUM 2: PERFORMANCE & RESOURCE ANALYSIS  (systems over time)     |
|    06 Queuing Theory          — congestion, waiting, throughput      |
|    07 Scheduling              — sequencing jobs on machines          |
|    08 Simulation              — when the model resists closed form   |
+----------------------------------------------------------------------+
                              |
                              v
+----------------------------------------------------------------------+
|  STRATUM 3: DECISION UNDER UNCERTAINTY  (data is random)            |
|    09 Stochastic & Dynamic    — DP, Markov decision processes,      |
|                                 stochastic programming               |
+----------------------------------------------------------------------+
```

---

## Layer 1: The Model Taxonomy

The single most important classification in OR is the **shape of the feasible region and objective**, because that — not the application domain — determines tractability.

```
                        OPTIMIZATION PROBLEMS
                        =====================
                                |
            +-------------------+-------------------+
            |                                       |
       CONTINUOUS vars                         DISCRETE vars
       (x in R^n)                              (x in Z^n)
            |                                       |
     +------+------+                         +------+------+
     |             |                         |             |
   LINEAR      NONLINEAR                  INTEGER       COMBINATORIAL
   obj+constr  obj or constr              LP (ILP)      (TSP, matching)
     |             |                         |             |
   "LP"        +---+---+                  "IP / MIP"    structure
   poly-time   |       |                  NP-hard       sometimes
   (Khachiyan  CONVEX  NONCONVEX          in general    poly (flows,
    1979)      |       |                                 matching)
               KKT     local optima
               poly    hard (NP-hard
               (int-pt  in general)
                methods)
```

| Class | Variables | Objective / Constraints | Tractability | File |
|-------|-----------|-------------------------|--------------|------|
| **LP** | continuous | linear / linear | Polynomial (interior-point); simplex exp. worst-case, poly in practice | 01, 02 |
| **Convex NLP** | continuous | convex / convex | Polynomial to ε (interior-point) | 05 |
| **Nonconvex NLP** | continuous | smooth, nonconvex | NP-hard in general; local methods | 05 |
| **ILP / MIP** | integer (or mixed) | linear | NP-hard | 03 |
| **Network flow** | continuous (integral optima) | linear, special structure | Strongly polynomial | 04 |
| **MDP** | policy | expected reward / dynamics | Poly in states+actions (LP/DP) | 09 |

**The decisive fact**: convexity, not linearity, is the watershed between easy and hard continuous optimization. Linearity is a special case of convexity. Integrality is what makes discrete problems hard.

---

## Layer 2: Why Convexity Is the Dividing Line

A set $C \subseteq \mathbb{R}^n$ is **convex** if for all $x, y \in C$ and $\lambda \in [0,1]$, $\lambda x + (1-\lambda) y \in C$. A function $f$ is convex if its epigraph is a convex set, equivalently $f(\lambda x + (1-\lambda)y) \le \lambda f(x) + (1-\lambda) f(y)$.

```
   CONVEX                              NONCONVEX
   ------                             ---------
        f(x)                              f(x)
   \                  /              \    /\        /
    \                /                \  /  \  /\  /
     \_____________ /                  \/    \/  \/
      every local min                  many local minima;
      is a GLOBAL min                  local search can
                                       get stuck
```

| Property | Convex problem | Nonconvex problem |
|----------|----------------|-------------------|
| Local optimum | Is globally optimal | May be far from global |
| Certificate of optimality | KKT conditions (sufficient) | KKT necessary only |
| Algorithm guarantee | Converges to global opt | Converges to *a* stationary point |
| Duality gap | Zero (under constraint qual.) | Generally positive |

**Bridge — old world → ML**: this is exactly why training a logistic regression (convex loss) is "solved" while training a deep network (nonconvex) is a craft. Gradient descent on a convex problem reaches the global optimum; on a deep net it reaches *a* basin, and the entire empirical practice of deep learning is about which basin. See `machine-learning-theory/` and file 05.

---

## Layer 3: The Solver Landscape

```
+----------------------------------------------------------------------+
|  PROBLEM CLASS         PRIMARY ALGORITHMS          GUARANTEE          |
|  -------------         ------------------          ---------          |
|  LP                    Simplex (Dantzig 1947)      exact; exp worst,  |
|                                                    poly in practice   |
|                        Interior-point (Karmarkar   exact to eps;      |
|                          1984, after Khachiyan)    polynomial         |
|                                                                      |
|  Convex NLP            Interior-point / Newton      poly to eps        |
|                        First-order (grad, prox)     poly to eps,       |
|                                                     slow tail          |
|                                                                      |
|  ILP / MIP             Branch & bound + cutting     exact; exp worst   |
|                          planes (branch & cut)      (NP-hard)          |
|                                                                      |
|  Network flow          Augmenting path / push-      strongly poly      |
|                          relabel / network simplex                    |
|                                                                      |
|  MDP                    Value/policy iteration, LP   poly in |S|,|A|   |
|                                                                      |
|  Resists closed form    Discrete-event simulation    statistical, not  |
|                          + Monte Carlo               exact             |
+----------------------------------------------------------------------+
```

The historical arc worth internalizing: **Dantzig's simplex (1947)** solved LP in practice for decades before anyone knew LP was in P. **Khachiyan (1979)** proved LP polynomial via the ellipsoid method — a theoretical breakthrough that was useless in practice. **Karmarkar (1984)** gave a polynomial *and* practical interior-point method, which is why large LPs today are often solved by interior-point rather than simplex.

---

## Layer 4: Duality — The Idea That Runs Through Everything

Every optimization problem (the **primal**) has a shadow problem (the **dual**). For LP this is exact and beautiful:

```
   PRIMAL (resource allocation)        DUAL (resource pricing)
   ----------------------------        -----------------------
   max  c'x   "maximize profit"        min  b'y   "minimize cost of
   s.t. Ax <= b  (resource limits)     s.t. A'y >= c   buying out the
        x >= 0                              y >= 0      resources"

   weak duality:   c'x <= b'y  ALWAYS (any feasible pair)
   strong duality: c'x* = b'y* AT OPTIMUM  (LP: holds under feasibility)

   dual variable y_i = SHADOW PRICE of constraint i
                     = marginal value of one more unit of resource i
```

Duality is not LP trivia. It is the conceptual engine behind:
- **Shadow prices / sensitivity** — what is a constraint *worth*? (file 02)
- **Optimality certificates** — complementary slackness proves a solution optimal (02)
- **KKT conditions** — the nonlinear generalization of LP duality (05)
- **Max-flow/min-cut** — a duality theorem in disguise (04)
- **Game theory** — LP duality ⟺ von Neumann's minimax theorem (`game-theory/`)
- **SVM training** — the dual is where the kernel trick lives (`machine-learning-theory/`)

**This is the throughline of the directory.** Master file 02 and the rest gets easier.

---

## Old World → OR World Bridges

For a reader coming from systems engineering and software architecture:

| You already know | OR concept it maps to |
|------------------|------------------------|
| Constraint solving / SAT in a build system | Integer programming feasibility (file 03) |
| Graph algorithms (shortest path, max-flow) | Network flows are LPs with integral optima (04) |
| Capacity planning a service | Queuing theory: M/M/c sizing (06) |
| Critical path in a project plan (MS Project) | PERT/CPM scheduling (07) |
| A/B test or load test | Monte Carlo / discrete-event simulation (08) |
| Caching policy, retry/backoff tuning | Markov decision process: optimize a policy (09) |
| Autoscaler rules | Stochastic control / DP under random demand (09) |
| Gradient descent in training | Convex optimization, first-order methods (05) |

The mental shift: in software you usually *implement* a heuristic. In OR you *prove* a bound — you can certify "this is within 2% of optimal" or "no schedule beats this." That certificate is the deliverable.

---

## Layer 5: Deterministic vs. Stochastic — The Other Axis

```
                    IS THE DATA KNOWN?
                    ==================
                          |
          +---------------+----------------+
          |                                |
       KNOWN EXACTLY                  RANDOM / UNCERTAIN
       (deterministic)               (stochastic)
          |                                |
   +------+------+               +---------+---------+
   |             |               |                   |
  STATIC      DYNAMIC          STATIC              DYNAMIC
  one shot    over time        one shot            over time
   |             |               |                   |
   LP/IP      multi-stage     stochastic          MDP, stochastic
   (01-05)    DP (det.)       programming          control,
                              (09): here-and-now   queuing (06),
                              + recourse            simulation (08)
```

| Axis | Deterministic | Stochastic |
|------|---------------|------------|
| Static (one decision) | LP, IP, convex (01–05) | Stochastic programming, 2-stage recourse (09) |
| Dynamic (sequential) | Deterministic DP (09) | MDP, queuing, simulation (06, 08, 09) |

**Bridge to control theory**: dynamic deterministic optimization *is* the Bellman equation / dynamic programming, and the stochastic dynamic case *is* the MDP / Hamilton-Jacobi-Bellman framework. See `control-theory/` for the continuous-time HJB view and file 09 for the discrete MDP view.

---

## How the Files Connect

```
        01 LINEAR PROGRAMMING  <----geometry, simplex
              |
              | every LP has a...
              v
        02 DUALITY  <----shadow prices, complementary slackness, KKT seed
              |
        +-----+----------------------------+
        |                                  |
        v                                  v
   03 INTEGER PROG                   04 NETWORK FLOWS
   (LP relaxation = bound)           (LP with integral optima;
   branch & bound, cuts               max-flow/min-cut = duality;
        |                             cross-ref graph-algorithms/)
        |
        v
   05 NONLINEAR / CONVEX  <----KKT generalizes LP duality; bridge to ML
        |
   = = = = = = = = = = = = = = = = = = = = = = = = = = = =  (uncertainty wall)
        |
        v
   06 QUEUING  --07 SCHEDULING-- 08 SIMULATION
        |              |              |
        +--------------+--------------+
                       |
                       v
              09 STOCHASTIC & DYNAMIC (DP / MDP / stochastic programming)
```

---

## Decision Cheat Sheet

| I need to... | Use | File |
|--------------|-----|------|
| Allocate continuous resources, linear costs | Linear programming | 01 |
| Know what a constraint is worth / do what-if | Duality, shadow prices, sensitivity | 02 |
| Make yes/no or count decisions (assignment, knapsack) | Integer programming, branch & bound | 03 |
| Route flow, match, assign on a graph | Network flows | 04 |
| Optimize a smooth nonlinear objective | Convex optimization / KKT | 05 |
| Size a server pool / understand wait times | Queuing theory (M/M/c) | 06 |
| Sequence jobs on machines, find critical path | Scheduling, PERT/CPM | 07 |
| Analyze a system with no closed form | Simulation (DES, Monte Carlo) | 08 |
| Make sequential decisions under randomness | DP / MDP / stochastic programming | 09 |
| Prove a solution is optimal | Duality / complementary slackness / KKT | 02, 05 |
| Bound how far from optimal a heuristic is | Approximation algorithms / LP relaxation | 03, 07 |

---

## Common Confusion Points

### "Is OR the same as machine learning?"

No, but they overlap at the optimization layer. ML *learns* a model from data; OR *builds* a model from domain structure and optimizes it. Both reduce to optimization — and convex optimization (file 05) is the shared substrate. ML training is "minimize loss"; OR is "minimize cost subject to constraints." The constraints are the difference: OR problems are constraint-dominated.

### "Why is integer programming hard when linear programming is easy?"

Dropping the integrality requirement (the **LP relaxation**) gives an easy convex polytope. Integrality carves out a discrete lattice of points inside that polytope, destroying convexity. ILP is NP-hard (it can encode SAT, partition, etc.). The whole of file 03 is techniques to exploit the easy relaxation to attack the hard integer problem.

### "Simplex is exponential — isn't LP supposed to be polynomial?"

Both are true and not contradictory. **LP the problem** is in P (Khachiyan's ellipsoid 1979; Karmarkar's interior-point 1984 are polynomial-time algorithms). **Simplex the algorithm** has exponential worst-case behavior (Klee–Minty cube, 1972), yet is observed to run in roughly linear-in-constraints time on practical instances; smoothed analysis (Spielman–Teng 2001) explains why. So: LP ∈ P; simplex is a non-polynomial algorithm that is excellent in practice.

### "Deterministic vs. stochastic — which do I use?"

If your data is a firm forecast and you make one decision, deterministic (01–05). If demand/arrivals/yields are genuinely random and decisions unfold over time, you need the stochastic-dynamic stratum (06, 08, 09). The classic mistake is solving a deterministic model on *average* inputs (the "flaw of averages") when the system is nonlinear — Jensen's inequality guarantees the average outcome ≠ outcome of the average. File 08 and 09 address this directly.

### "Where do network flows fit — graph algorithms or OR?"

Both. Max-flow, min-cost flow, and assignment are LPs with totally unimodular constraint matrices, so they live in OR's duality theory; they also have purpose-built combinatorial algorithms (Ford–Fulkerson, Hungarian, push–relabel) that live in graph algorithms. File 04 treats them as the bridge and cross-references a future `graph-algorithms/` directory for the pure-algorithmic view.
