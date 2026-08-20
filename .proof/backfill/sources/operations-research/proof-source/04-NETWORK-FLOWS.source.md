---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "04-NETWORK-FLOWS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:operations-research:network-flows
kind: guide
module: operations-research
section: operations-research
title: Network Flows - Max-Flow/Min-Cut, Min-Cost Flow, Assignment
status: source-custody
source_custody: partial
current_path: operations-research/04-NETWORK-FLOWS.md
canonical_path: operations-research/04-NETWORK-FLOWS.md
backsource_ids: [proof-backfill:operations-research:04-network-flows, git-history:operations-research:04-network-flows]
concepts: [network flows, max-flow min-cut, min-cost flow, assignment problem, total unimodularity]
root_concepts: [network flows]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Network Flows — Max-Flow/Min-Cut, Min-Cost Flow, and Assignment

> **Cross-reference**: Network flows sit at the boundary of operations research and graph algorithms. This file treats them as **structured linear programs** — emphasizing the LP/duality view, total unimodularity, and the OR algorithms. A future `graph-algorithms/` directory will treat the same problems from the pure combinatorial-algorithm side (data structures, asymptotic refinements, push-relabel internals). Where the algorithmic detail belongs there, this file points to it.

## The Big Picture

Network-flow problems route a divisible commodity through a directed graph subject to **capacities** (edge limits) and **conservation** (flow in = flow out at every interior node). They are the most beautiful corner of OR because their constraint matrices are **totally unimodular**: the LP relaxation has integer vertices automatically, so these NP-hard-looking problems are actually **strongly polynomial**.

```
+----------------------------------------------------------------------+
|                 NETWORK FLOWS: THE WHOLE PICTURE                      |
|                                                                      |
|   GRAPH                          LINEAR PROGRAM                       |
|   -----                          --------------                       |
|   nodes V, arcs E            ->  variables f_e (flow on each arc)    |
|   capacities u_e            ->   0 <= f_e <= u_e                      |
|   conservation at node v    ->   sum_in f = sum_out f  (flow bal.)   |
|   source s, sink t                                                   |
|                                                                      |
|        [s] --10--> (a) --9--> [t]                                    |
|          \         ^          /                                      |
|           4        |5        15                                      |
|            \       |        /                                        |
|             v      |       v                                         |
|             (b) --6+----->(c)                                        |
|                                                                      |
|   FOUR CANONICAL PROBLEMS:                                           |
|     Max flow      -- push the most s->t                              |
|     Min cut       -- the dual / bottleneck (= max flow!)            |
|     Min-cost flow -- cheapest way to ship d units                   |
|     Assignment    -- min-cost perfect matching (special transport)  |
|                                                                      |
|   KEY FACT: the node-arc incidence matrix is TOTALLY UNIMODULAR,    |
|   so integer capacities => integer optimal flow (no rounding!).     |
+----------------------------------------------------------------------+
```

**The unifying theme**: these are all LPs (file 01) with a special matrix that guarantees integrality (file 03's TU escape hatch), and their duals (file 02) have crisp combinatorial meaning (cuts, potentials, prices).

---

## Layer 1: The Network LP and Total Unimodularity

A flow network is a directed graph $G=(V,E)$ with arc capacities $u_e \ge 0$. A **flow** $f$ assigns $f_e \in [0, u_e]$ to each arc satisfying **conservation** at every node except source/sink.

```
   THE MAX-FLOW LP:

   max   |f| = (net flow out of s)
   s.t.  sum_{e into v} f_e - sum_{e out of v} f_e = 0   for v != s,t  (balance)
         0 <= f_e <= u_e                                  (capacity)

   The balance constraints' coefficient matrix is the
   NODE-ARC INCIDENCE MATRIX: each column (arc) has exactly
   one +1 (head) and one -1 (tail). THIS MATRIX IS TOTALLY UNIMODULAR.
```

**Theorem (Integrality).** If all capacities (and supplies/demands) are integers, then there exists an integer optimal flow, and standard flow algorithms produce one. *Reason*: the incidence matrix is totally unimodular (file 03), so every vertex of the feasible polytope is integral — the LP and IP coincide.

```
   WHY TU MATTERS HERE:

   "min-cost flow looks like an integer program (ship whole units)"
        but
   "its constraint matrix is TU"
        therefore
   "the LP relaxation already gives integer answers -- it's in P."

   This is the single reason network problems escape NP-hardness.
```

| Network constraint matrix | Property |
|---------------------------|----------|
| Node-arc incidence (directed) | Totally unimodular |
| Bipartite incidence (assignment) | Totally unimodular |
| Interval matrices | Totally unimodular |

---

## Layer 2: Max-Flow / Min-Cut

The crown jewel. An **s-t cut** $(S, \bar S)$ partitions nodes with $s \in S$, $t \in \bar S$; its **capacity** is the total capacity of arcs crossing from $S$ to $\bar S$.

```
   A CUT separates s from t. Its capacity = sum of forward arcs across it.

         S side       |        S-bar side
       +-----------+  |  +-----------+
       | [s]  (a)  |--|->| (c)  [t]  |
       |      (b)  |--|->|           |
       +-----------+  |  +-----------+
                      ^
                   the cut; capacity = sum of arcs crossing left->right
```

**Theorem (Max-Flow Min-Cut, Ford–Fulkerson 1956).** In any network with a single source $s$ and sink $t$, the **maximum value of an s-t flow equals the minimum capacity of an s-t cut**.

This is **LP duality** (file 02) made combinatorial: the max-flow LP is the primal, the min-cut LP is its dual, and strong duality says their optima coincide. The integrality of the cut comes from total unimodularity.

```
   max-flow  =  min-cut       <-- strong duality, specialized

   PRIMAL: max flow value        DUAL: min cut capacity
   (push commodity)              (cheapest set of arcs to sever s from t)
   The dual variables are node "potentials"; the optimal cut is read off
   from which nodes are reachable in the residual graph at termination.
```

### Augmenting-Path Algorithms (the residual-graph idea)

```
   FORD-FULKERSON SCHEME:
   1. Start with zero flow.
   2. Build the RESIDUAL graph (leftover forward capacity +
      backward "undo" capacity equal to current flow).
   3. Find an augmenting path s->t with positive residual capacity.
   4. Push flow = the path's bottleneck residual. Update residuals.
   5. Repeat until no augmenting path. The reachable set from s
      in the final residual graph defines the MIN CUT.
```

| Algorithm | Augmenting-path choice | Complexity | Note |
|-----------|------------------------|------------|------|
| Ford–Fulkerson (generic) | any path | $O(E \cdot |f^*|)$ | not polynomial if capacities huge/irrational |
| Edmonds–Karp | shortest (BFS) path | $O(V E^2)$ | strongly polynomial |
| Dinic | blocking flows on level graph | $O(V^2 E)$ | $O(E\sqrt V)$ on unit-capacity (bipartite matching) |
| Push–relabel (Goldberg–Tarjan) | preflow + height labels | $O(V^2 E)$, $O(V^3)$ variants | fast in practice |

*(The deep algorithmic internals — dynamic trees, the $O(VE)$ and recent almost-linear-time max-flow results — belong in `graph-algorithms/`. Here the point is the **duality** and **integrality**.)*

**Caution on Ford–Fulkerson**: with *irrational* capacities and bad path choices it may not terminate; with integer capacities it always terminates (each augmentation increases integral flow by $\ge 1$). Edmonds–Karp's shortest-path rule guarantees polynomial termination regardless.

---

## Layer 3: Min-Cost Flow — the General Model

Min-cost flow generalizes nearly every network problem: ship a required amount of flow at minimum total cost, respecting capacities. Each node $v$ has a **supply/demand** $b_v$ ($>0$ source, $<0$ sink, $=0$ transshipment), each arc a cost $c_e$ per unit and capacity $u_e$.

```
   MIN-COST FLOW LP:
   min  sum_e c_e f_e
   s.t. (flow balance with supplies)  net_out(v) - net_in(v) = b_v  for all v
        0 <= f_e <= u_e
   (feasible iff sum_v b_v = 0)
```

**Special cases — min-cost flow is the parent of them all:**

```
                       MIN-COST FLOW
                      (cost + capacity)
              /         |          |         \
             /          |          |          \
        MAX FLOW    SHORTEST    TRANSPORTATION  ASSIGNMENT
       (costs=0,    PATH        (bipartite,     (transport with
        add s->t    (unit       supply/demand    supplies all 1,
        return arc) supply at    no capacities)  bipartite)
                    s, demand t)
```

| Problem | Reduction to min-cost flow |
|---------|----------------------------|
| Max flow | All costs 0; add a high-capacity $t \to s$ arc of cost $-1$; minimize |
| Shortest path | Supply 1 at $s$, demand 1 at $t$, arc costs = lengths |
| Transportation | Bipartite supplies → demands, no intermediate capacities |
| Assignment | Transportation with all supplies = demands = 1 |

**Algorithms for min-cost flow**: network simplex (specialized simplex with spanning-tree bases — extremely fast in practice), cost-scaling push–relabel, and successive shortest paths (with node potentials to keep reduced costs nonnegative). The **optimality condition** is combinatorial and dual: a flow is optimal iff there exist node **potentials** $\pi_v$ (the dual variables) such that no arc has negative reduced cost $c_e - \pi_{tail} + \pi_{head}$ in the residual graph (no negative-cost residual cycle).

```
   OPTIMALITY (complementary slackness, file 02, specialized):
   reduced cost c_e^pi = c_e - pi_u + pi_v
     f_e = 0       => c_e^pi >= 0
     0 < f_e < u_e => c_e^pi = 0
     f_e = u_e     => c_e^pi <= 0
   Equivalently: NO negative-cost cycle in the residual graph.
```

---

## Layer 4: The Assignment Problem

Assign $n$ agents to $n$ tasks at minimum total cost, one-to-one. It is a min-cost flow on a complete bipartite graph with unit supplies/demands.

```
   AGENTS        TASKS         cost matrix C (n x n)
   [a1] ------> [t1]           assign exactly one task per agent
   [a2] ------> [t2]           minimize sum of assigned costs
   [a3] ------> [t3]

   LP:  min sum_ij c_ij x_ij
        s.t. sum_j x_ij = 1  (each agent one task)
             sum_i x_ij = 1  (each task one agent)
             x_ij >= 0       (TU => integer optimum: x_ij in {0,1} automatically)
```

**Birkhoff–von Neumann theorem**: the vertices of the doubly-stochastic polytope (the assignment LP's feasible region) are exactly the **permutation matrices**. So the LP relaxation's optimal vertex is a genuine permutation — integrality for free, again from TU.

**The Hungarian algorithm** (Kuhn 1955, Munkres) solves assignment in $O(n^3)$. It is a primal-dual method: maintain dual potentials (a "labeling"), grow an equality subgraph, and augment along alternating paths — the assignment-specific instance of successive-shortest-path min-cost flow.

```
   HUNGARIAN ALGORITHM = primal-dual on the assignment LP:
   - dual variables (row/col potentials) maintain reduced-cost >= 0
   - tight arcs (reduced cost 0) form the "equality graph"
   - find a max matching in the equality graph (augmenting paths)
   - if not perfect, adjust potentials to admit more tight arcs
   - terminates with a perfect matching = optimal assignment.
```

**Bridge to ML**: the assignment problem is the optimal-transport problem in the discrete, unit-mass case. Modern ML uses **entropic-regularized optimal transport (Sinkhorn algorithm)** for differentiable, GPU-friendly approximate assignment — see `machine-learning-theory/`. The Wasserstein distance is the min-cost transportation value.

---

## Layer 5: Where This Overlaps graph-algorithms/

```
+----------------------------------------------------------------------+
|  CONCEPT                 THIS FILE (OR view)    graph-algorithms/    |
|  -------                 -----------------      (future, algo view)  |
|  Max-flow/min-cut        duality theorem,       Dinic/push-relabel   |
|                          TU, LP framing         data structures,     |
|                                                 almost-linear bounds |
|  Shortest path           special min-cost flow  Dijkstra/Bellman-Ford|
|  Matching                assignment LP, Birkhoff Hopcroft-Karp,       |
|                                                 blossom (Edmonds)    |
|  Min-cost flow           potentials = duals     scaling algorithms   |
+----------------------------------------------------------------------+
```

**The division of labor**: OR cares *why* these are tractable (TU, LP duality) and how they connect to general optimization (min-cost flow as a unifying LP). Graph algorithms cares *how fast* and with what data structures. A reader who wants the $O(E \log V)$ Dijkstra heap details or Edmonds' blossom contraction for non-bipartite matching should go there; this file establishes the LP/duality scaffolding those algorithms optimize within.

---

## Old World → Network-Flow Bridges

| You already know | Network-flow analogue |
|------------------|------------------------|
| Bandwidth/capacity provisioning | Max-flow: the min-cut is your true bottleneck |
| Load balancer behind a bottleneck link | Min-cut = the limiting cross-section |
| Job-to-worker assignment (scheduling) | Assignment problem, Hungarian $O(n^3)$ |
| Shortest-path routing (OSPF/Dijkstra) | Shortest path = unit min-cost flow |
| Bipartite matching (ads ↔ slots, users ↔ servers) | Max matching = max flow on unit-capacity bipartite graph |
| Optimal transport / Sinkhorn in ML | Transportation problem, regularized |
| Reliability: minimum set of links to cut a path | Min-cut directly |

The systems takeaway: when you see "route X through a capacitated graph," check first whether it's a flow problem — if so it is **polynomial and integral**, no MIP needed. Recognizing the network structure (TU) is the difference between an $O(n^3)$ solve and an NP-hard branch-and-bound.

---

## Decision Cheat Sheet

| Problem | Model | Algorithm | Complexity |
|---------|-------|-----------|------------|
| Most flow s→t | Max flow | Dinic / push–relabel | $O(V^2 E)$ |
| True bottleneck of a network | Min cut | = max flow (then read residual reachability) | same |
| Cheapest way to ship demand | Min-cost flow | Network simplex / cost-scaling | strongly poly |
| One-to-one min-cost matching | Assignment | Hungarian | $O(n^3)$ |
| Many-to-many supply→demand | Transportation | Network simplex | strongly poly |
| Shortest route | Shortest path | Dijkstra / Bellman–Ford | see `graph-algorithms/` |
| Non-bipartite matching | General matching | Edmonds' blossom | see `graph-algorithms/` |
| Continuous OT in ML | Optimal transport | Sinkhorn (entropic) | see `machine-learning-theory/` |

---

## Common Confusion Points

### "Why are network flows easy when general IP is NP-hard?"

**Total unimodularity.** The node-arc incidence matrix has determinant $\pm 1$ or $0$ for every square submatrix, so the LP relaxation's vertices are all integer. The integrality requirement that makes general IP hard (file 03) is automatically satisfied here — you solve the LP and get integers for free. Recognizing TU structure is the whole game.

### "Max-flow equals min-cut — is that obvious?"

No, it is a theorem (Ford–Fulkerson 1956) and a genuine instance of **LP strong duality** (file 02). One direction (max flow ≤ min cut) is weak duality and easy: any flow is bounded by any cut's capacity. The reverse (they're equal) needs the augmenting-path argument or LP duality. The min cut is *constructed* from the residual graph at termination — it's the set of nodes still reachable from $s$.

### "Assignment vs. transportation vs. min-cost flow — same thing?"

Nested specializations. Min-cost flow is the parent. Transportation is min-cost flow on a bipartite supply/demand graph with no intermediate nodes. Assignment is transportation with all supplies and demands equal to 1 (so the solution is a permutation). Solving the most general form (min-cost flow) handles them all, but the specialized algorithms (Hungarian for assignment) are faster on their niche.

### "Ford–Fulkerson is $O(E|f^*|)$ — that's not polynomial!"

Correct — generic Ford–Fulkerson is **pseudo-polynomial** (depends on the flow value, hence on capacity magnitudes) and can even fail to terminate with irrational capacities. The fix is the **choice of augmenting path**: Edmonds–Karp (shortest path by BFS) gives strongly polynomial $O(VE^2)$; Dinic and push–relabel improve further. Always cite the *specific* algorithm's bound, not generic Ford–Fulkerson.

### "Node potentials in min-cost flow — where do those come from?"

They are the **dual variables** of the flow-balance constraints (file 02). The reduced cost $c_e - \pi_u + \pi_v$ is the network analogue of an LP reduced cost, and the optimality condition "no negative-cost residual cycle" is complementary slackness specialized to flows. Successive-shortest-path algorithms maintain these potentials to keep all residual reduced costs nonnegative so Dijkstra (not Bellman–Ford) can be used each iteration.

### "Should I model my problem as a flow or as a general MIP?"

If the constraints are pure conservation + capacity (and any integrality is the only nonlinearity), it's a flow — solve it as such and enjoy polynomial, integral solutions. The moment you add side constraints that break TU (e.g., "either arc A *or* arc B but not both," or a budget across arcs), you generally fall back to MIP (file 03). The skill is spotting how much of your problem is flow-structured and isolating the rest.
