---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-SHORTEST-PATHS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:graph-algorithms:shortest-paths
kind: guide
module: graph-algorithms
section: mathematics-physics
title: Shortest Paths
status: source-custody
source_custody: partial
current_path: graph-algorithms/03-SHORTEST-PATHS.md
canonical_path: graph-algorithms/03-SHORTEST-PATHS.md
backsource_ids: [mdloom-backfill:graph-algorithms:03-shortest-paths, git-history:graph-algorithms:03-shortest-paths]
concepts: [Dijkstra, Bellman-Ford, Floyd-Warshall, A-star, shortest paths, relaxation]
root_concepts: [shortest paths]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Shortest Paths — Preconditions Are Everything

Shortest-path algorithms are distinguished almost entirely by their
**preconditions**, not their mechanics — which is exactly why they are so easy to misapply. Every one of them is built from a single
operation — *relaxation* — but each makes a different assumption (non-negative
weights, acyclicity, no negative cycle) that, if violated, makes the algorithm not
slow but *incorrect*. The decision tree is the whole content.

```
  PICK A SHORTEST-PATH ALGORITHM BY ITS PRECONDITION
  ==================================================

                        +------------------------------+
                        | Do you need ALL pairs?        |
                        +------------------------------+
                         | yes                  | no (single source)
                         v                      v
              +---------------------+   +-------------------------------+
              | Floyd-Warshall      |   | Are any edge weights NEGATIVE?|
              | O(V^3), any weights |   +-------------------------------+
              | no neg cycle (detects|    | no                    | yes
              | them on diagonal)   |    v                       v
              +---------------------+  +----------------+  +----------------------+
                                       | Is graph a DAG?|  | Bellman-Ford         |
                                       +----------------+  | O(V*E), detects a    |
                                        | yes      | no    | NEGATIVE CYCLE        |
                                        v          v       +----------------------+
                              +----------------+ +-------------------------+
                              | DAG relaxation | | DIJKSTRA                |
                              | O(V+E),        | | O((V+E) log V) heap     |
                              | topo order     | | REQUIRES weights >= 0   |
                              +----------------+ +-------------------------+
                                                       |  have a goal + heuristic?
                                                       v
                                                  +------------------+
                                                  | A* : Dijkstra +  |
                                                  | admissible h(v)  |
                                                  +------------------+
```

**Read the tree top-down — each branch is a precondition gate.** Get the gate
wrong and you get a wrong answer, silently.

---

## Relaxation — The Single Operation Underneath All of Them

Every shortest-path algorithm repeatedly applies one update:

```
  RELAX(u, v):                          dist[]  = best-known distance from source
    if dist[u] + w(u,v) < dist[v]:      pred[]  = predecessor, to reconstruct path
        dist[v] = dist[u] + w(u,v)
        pred[v] = u                     Initialize: dist[source]=0, others=+INF

  The algorithms differ ONLY in the ORDER and NUMBER of relaxations:
    Dijkstra        : relax out of the closest unfinalized vertex (greedy, once each)
    Bellman-Ford    : relax EVERY edge, V-1 times (then once more to detect neg cycle)
    DAG relaxation  : relax edges in topological order (one pass)
    Floyd-Warshall  : relax through each intermediate vertex k (triple loop)
```

The correctness of each reduces to: *after the algorithm's relaxation schedule,
has every edge on the true shortest path been relaxed in the right order?* That's
the lens for all four proofs below.

---

## Dijkstra — REQUIRES Non-Negative Weights

Dijkstra grows a set of *finalized* vertices, always finalizing the closest
unfinalized one, then relaxing its out-edges. With a binary heap it is
**O((V+E) log V)**; with a Fibonacci heap **O(E + V log V)** (theoretical, rarely
faster in practice).

> **Precondition: all edge weights ≥ 0.** This is non-negotiable. Dijkstra
> finalizes a vertex the instant it is popped, assuming no future path can be
> cheaper. A negative edge can make a *later*, longer-hop path cheaper — but the
> vertex is already finalized and can never be re-opened. The result is wrong, not
> just suboptimal.

```
  Why a negative edge BREAKS Dijkstra:

      A --1--> B
      |        ^
      4        |
      |       -3      (edge B<-C... actually C->B with weight -3)
      v        |
      C -------+

   From A: pop A(0). Relax A->B=1, A->C=4. Heap: B(1), C(4).
   Pop B(1) and FINALIZE it as dist 1.
   Later, C->B = 4 + (-3) = 1... ties here, but make C->B = -3 from C(4):
   the true A->C->B = 4 + (-3) = 1, but had it been A->C->B = 4 + (-10),
   B's true distance is -6 -- yet B was FINALIZED at 1 and never revisited.
   => WRONG ANSWER. Use Bellman-Ford when negatives are possible.
```

Correct worked example (all non-negative):

```
  Graph:                    Dijkstra from A:
     A --1--> B --2--> D     pop  finalize  relax
     |        |        ^     A    A=0       B=1, C=4
     4        3        |     B    B=1       C=min(4,1+3)=4, D=1+2=3
     v        |        |     D    D=3       (nothing improves)
     C <------+        |     C    C=4       (D already 3)
       (C unused here) |     => dist: A=0 B=1 D=3 C=4   path A->B->D
```

The finalization invariant — *when v is popped, dist[v] is final* — holds
precisely because every edge is ≥ 0, so any alternative path leaves through a
vertex at least as far and can only add non-negative weight.

---

## Bellman-Ford — Negative Edges and Negative-Cycle Detection

Bellman-Ford relaxes **every edge, V−1 times**. After V−1 rounds every shortest
path (which has at most V−1 edges if no negative cycle exists) is correct. It runs
in **O(V·E)** — slower than Dijkstra, but it tolerates negative edges and, with
one extra round, *detects negative cycles*.

```
  Bellman-Ford(source):
    repeat V-1 times:
        for each edge (u,v,w):  RELAX(u,v)
    # detection round:
    for each edge (u,v,w):
        if dist[u] + w < dist[v]:   ==> a NEGATIVE CYCLE is reachable

  Why V-1 rounds: a simple shortest path has at most V-1 edges. Round i
  guarantees all shortest paths using <= i edges are correct. After V-1
  rounds, all are correct -- UNLESS a negative cycle lets paths keep improving
  forever, which is exactly what the V-th round detects.
```

```
  Negative EDGE is fine:            Negative CYCLE makes "shortest" undefined:

     A --4--> B                        A --1--> B
     |       /                         ^        |
     2     -3   <- neg edge, OK         -4      1
     |    /                            |        v
     v   v                             D <--1-- C
     C                                 cycle A->B->C->D->A = 1+1+1-4 = -1 < 0
   dist computed fine; no cycle.       => loop forever to get -inf
                                          Bellman-Ford's V-th round flags it.
```

> **Distinguish two things that are easily conflated:** a negative *edge* is legal and
> Bellman-Ford handles it. A negative *cycle* makes "shortest path" *undefined*
> (you can loop it forever for −∞), and Bellman-Ford's job is to *detect and
> report* it, not to return a number. Dijkstra can do neither.

> Old-world bridge: distance-vector routing (RIP) is distributed Bellman-Ford —
> each router relaxes against its neighbors' advertised distances. The infamous
> "count-to-infinity" problem is precisely a negative-cycle-like instability in
> that distributed relaxation. Link-state routing (OSPF) is instead Dijkstra run
> locally on the full topology.

---

## DAG Shortest Paths — Beat Dijkstra When Acyclic

If the graph is a **DAG**, relax edges in *topological order* and you are done in
a single O(V+E) pass — faster than Dijkstra and it handles negative weights too
(a DAG has no cycles, so no negative cycle is possible).

```
  DAG, topo order [A,B,C,D]:        Relax in topo order:
                                    A: dist 0; relax A->B(2), A->C(6)
    A --2--> B --3--> D             B: dist 2; relax B->D = 2+3 = 5
    |        |                      C: dist 6; relax C->D = 6+? (if worse, ignore)
    6        v                      D: dist 5
    +------> C                      => O(V+E), negatives OK, no heap needed
```

This is the right tool for **PERT/CPM project scheduling** (longest path in a DAG,
the "critical path", is the same algorithm with max instead of min — see
`operations-research/07-SCHEDULING.md`).

---

## Floyd-Warshall — All-Pairs by Dynamic Programming

Floyd-Warshall computes shortest paths between *every* pair in **O(V³)** time,
O(V²) space. The DP is elegant: consider allowing intermediate vertices
1..k one at a time.

```
  for k in 1..V:           dist[i][j] = min( dist[i][j],          # path not using k
    for i in 1..V:                           dist[i][k]+dist[k][j])# path through k
      for j in 1..V:
        relax i->j via k    The k loop MUST be outermost.

  Detects negative cycles: if any dist[i][i] < 0 after the triple loop,
  vertex i lies on a negative cycle.
```

| | Bound | Weights | Negative cycle |
|---|-------|---------|----------------|
| V Dijkstras | O(V·(V+E) log V) | **≥ 0 only** | n/a |
| V Bellman-Fords | O(V²·E) | any | detects |
| Floyd-Warshall | O(V³) | any | detects (diagonal < 0) |
| Johnson's | O(V·E + V² log V) | any (reweights) | detects (in the B-F phase) |

> For dense graphs (E ≈ V²) Floyd-Warshall's O(V³) ties V Dijkstras and beats V
> Bellman-Fords, with far simpler code (a 3-line triple loop on a matrix). For
> **sparse** graphs with negative edges, **Johnson's algorithm** wins: it
> Bellman-Ford-reweights once to remove negatives (preserving shortest paths via a
> potential function), then runs V Dijkstras — O(V·E + V² log V).

---

## A\* — Dijkstra With a Goal and a Heuristic

When you have a *single target* and a heuristic estimate `h(v)` of the remaining
distance, A\* orders the frontier by `f(v) = dist[v] + h(v)` instead of `dist[v]`.
It explores the same way as Dijkstra but biased toward the goal, expanding far
fewer vertices in practice.

```
  Dijkstra frontier key:  g(v)           = cost so far
  A* frontier key:        f(v) = g(v) + h(v)   (h = estimate to goal)

         start ......... explores in a circle (Dijkstra)
           \
            \......      A* explores an ellipse stretched toward the goal
                 goal

  PRECONDITIONS on h:
    ADMISSIBLE   : h(v) <= true distance to goal   => A* finds OPTIMAL path
    CONSISTENT   : h(u) <= w(u,v) + h(v)  (triangle)=> no vertex re-expanded
                   (consistent => admissible; the stronger, usual requirement)
```

| h(v) | Behavior |
|------|----------|
| h(v) = 0 everywhere | A\* degenerates to **Dijkstra** (admissible but uninformed) |
| h = admissible (e.g. straight-line distance ≤ road distance) | optimal path, fewer expansions |
| h = consistent | optimal, and no vertex is ever re-opened |
| h *overestimates* | A\* is fast but **may return a non-optimal path** |

> Old-world bridge: A\* is the workhorse of game pathfinding and GPS routing.
> Production routers go further (Contraction Hierarchies, ALT) but the principle
> is the same — a good heuristic prunes the search. The straight-line (Euclidean)
> distance is admissible for road networks because no road is shorter than the
> crow-flight line.

---

## Decision Cheat Sheet

| Situation | Algorithm | Time | Precondition |
|-----------|-----------|------|--------------|
| Unweighted shortest path | BFS (`02`) | O(V+E) | uniform edge cost |
| Single source, weights ≥ 0 | Dijkstra | O((V+E) log V) | **no negative edges** |
| Single source, some negatives | Bellman-Ford | O(V·E) | detects neg cycle |
| Single source on a DAG | topo-order relax | O(V+E) | acyclic; any weights |
| Single source + target + heuristic | A\* | ≤ Dijkstra | admissible h |
| All pairs, dense | Floyd-Warshall | O(V³) | no neg cycle (detects) |
| All pairs, sparse, negatives | Johnson's | O(V·E + V² log V) | detects neg cycle |
| Need to *detect* a negative cycle | Bellman-Ford / Floyd-Warshall | O(V·E) / O(V³) | — |

---

## Common Confusion Points

**"Dijkstra works if I just add a big constant to make weights positive."** No.
Adding a constant `c` to every edge penalizes paths with *more edges* by `c` per
edge, so it changes which path is shortest. The reweighting that *does* preserve
shortest paths is Johnson's potential function `w'(u,v) = w(u,v) + h(u) − h(v)`,
which telescopes to zero along any path and so never changes the *argmin*, only
shifts all path lengths by `h(source) − h(target)`. That's a real technique; the
"add a constant" version is wrong.

**"Bellman-Ford returns the shortest path even with a negative cycle."** It
*cannot* — "shortest" is undefined when a negative cycle is reachable (you can
loop to −∞). Bellman-Ford's contract is to *detect and report* the negative
cycle, not to return a meaningless number. If your application needs a number
anyway, you must redefine the problem (e.g. shortest *simple* path, which is
NP-hard).

**"V−1 iterations of Bellman-Ford is a heuristic."** It is exact and tight. A
shortest path in a graph with no negative cycle is simple, hence has ≤ V−1 edges,
hence is fully relaxed after V−1 rounds. The V-th round exists solely to detect
the negative-cycle case. Stopping early when a round makes no change is a valid
optimization.

**"A\* always beats Dijkstra."** Only with a *good admissible* heuristic. With
h = 0 it *is* Dijkstra. With an inadmissible (overestimating) heuristic it's fast
but can return a suboptimal path. With a heuristic that's admissible but weak, the
overhead of computing `h` can make it slower than plain Dijkstra. The heuristic
quality is everything.

**"Floyd-Warshall's loops can be in any order."** No — the **k loop must be
outermost**. The DP invariant is "shortest paths using only intermediate vertices
≤ k"; computing that requires k to be the outer dimension. Swapping the loops
produces wrong distances. This is the single most common Floyd-Warshall bug.

**"Negative edges and negative cycles are the same problem."** A negative *edge*
is benign — Bellman-Ford, DAG relaxation, and Floyd-Warshall all handle it. A
negative *cycle* makes the problem ill-posed. Keep them mentally separate: the
first is a weight sign, the second is a structural pathology.
