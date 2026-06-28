---
maxim_schema: maxim.frontmatter.v1
id: maxim:graph-algorithms:overview
kind: guide
module: graph-algorithms
section: mathematics-physics
title: Graph Algorithms - Landscape
status: source-custody
source_custody: partial
current_path: graph-algorithms/00-OVERVIEW.md
canonical_path: graph-algorithms/00-OVERVIEW.md
backsource_ids: [proof-backfill:graph-algorithms:00-overview, git-history:graph-algorithms:00-overview]
concepts: [graph algorithms, traversal, shortest paths, network flow, NP-hard graphs]
root_concepts: [graph algorithms]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---

# Graph Algorithms — The Landscape

A graph is the one data structure that everything reduces to: a routing table is
a weighted digraph, a build system is a DAG, a dependency resolver is topological
sort with conflict backtracking, a social network is a sparse adjacency list, and
half of operations research is a flow network in disguise. This directory is the
combinatorial layer beneath all of that. It is ordered as a strict dependency
chain — representation fixes the cost model, traversal is the primitive every
later algorithm specializes, and the complexity cliff between P and NP-hard cuts
the whole field in two.

```
  graph-algorithms/ : REPRESENTATION -> TRAVERSAL -> POLYNOMIAL CORE -> THE CLIFF -> ESCAPE HATCHES
  ============================================================================================

   01 REPRESENTATION          02 TRAVERSAL              03-05 POLYNOMIAL CORE
   +------------------+       +------------------+      +-------------------------+
   | adjacency list   |       | BFS  (layers)    |      | 03 shortest paths       |
   | adjacency matrix |  -->  | DFS  (recursion) | -->  |    Dijkstra/B-F/F-W/A*  |
   | edge list / CSR  |       | topo sort (DAG)  |      | 04 spanning trees       |
   | directed/weighted|       | components/cycle |      |    Prim/Kruskal/UF      |
   +------------------+       +------------------+      | 05 connectivity         |
        |  fixes V,E              | O(V+E) frontier     |    SCC/bridges/2-SAT    |
        |  cost model             | for both BFS/DFS    +-------------------------+
        v                         v                              |  all P-time
   "every bound below       "every algorithm below               v
    is stated in V and E"    is a decorated DFS/BFS"     ==================================
                                                          THE CLIFF (P vs NP-hard)
                                                          ==================================
                                                          06 MAX-FLOW / MATCHING  (still P)
                                                             max-flow = min-cut; LP dual
                                                                |  reduction frontier
                                                                v
                                                          07 NP-HARD GRAPHS
                                                             TSP, vertex cover, coloring,
                                                             clique, independent set
                                                                |  no poly algo (unless P=NP)
                                                    +-----------+-----------+
                                                    v                       v
                                          08 SPECTRAL & RANDOM    09 PLANARITY & STRUCTURE
                                          Laplacian, PageRank,    Euler V-E+F=2, minors,
                                          random walks, expanders treewidth, embeddings
                                          (linear-algebra escape) (structural escape)
```

**Read this left to right as a dependency chain.** You cannot state a bound
without a representation (`01`). Every algorithm in `03`–`07` is a traversal
(`02`) with bookkeeping bolted on. The vertical drop after `06` is the P/NP-hard
boundary — the single most important fact in the field. The two escape hatches
(`08`, `09`) are how you make hard problems tractable: relax to linear algebra,
or exploit structure.

---

## The Five Strata

```
+--------------------------------------------------------------------------+
| STRATUM 0 — REPRESENTATION (01)                                          |
|   How V vertices and E edges live in memory. Determines whether an       |
|   edge-existence query is O(1) (matrix) or O(deg v) (list), and whether  |
|   you pay O(V^2) or O(V+E) space. EVERY bound below is quoted in V, E.   |
+--------------------------------------------------------------------------+
| STRATUM 1 — TRAVERSAL (02)                                               |
|   BFS and DFS, both O(V+E) on an adjacency list. Topological sort,       |
|   connected components, cycle detection are all DFS/BFS with one extra   |
|   array. This is the universal primitive.                               |
+--------------------------------------------------------------------------+
| STRATUM 2 — POLYNOMIAL CORE (03, 04, 05)                                 |
|   Shortest paths, minimum spanning trees, strong connectivity. All       |
|   solvable in low-degree polynomial time. The "solved" part of the field.|
+--------------------------------------------------------------------------+
| STRATUM 3 — FLOW: THE LP BRIDGE (06)                                     |
|   Max-flow/min-cut and bipartite matching. Still polynomial, but it is   |
|   the linear-programming dual frontier — the last big P-time conquest    |
|   and the gateway to operations-research/.                              |
+--------------------------------------------------------------------------+
| STRATUM 4 — THE HARD SIDE (07, 08, 09)                                   |
|   NP-hard graph problems (07) and the two ways around them: spectral     |
|   relaxation (08) and structural parameterization (09).                 |
+--------------------------------------------------------------------------+
```

---

## The One Table That Orients Everything

The single most common mistake is misquoting a
bound or forgetting a precondition. Here is the canonical reference — memorize
the **precondition** column, not just the bound.

| Problem | Best general algorithm | Time | Precondition / caveat |
|---------|------------------------|------|-----------------------|
| Traverse / reach | BFS or DFS | O(V+E) | adjacency list; O(V^2) on matrix |
| Single-source shortest path | Dijkstra (binary heap) | O((V+E) log V) | **weights ≥ 0** |
| SSSP, negative edges | Bellman-Ford | O(V·E) | handles neg edges; **detects neg cycle** |
| SSSP on a DAG | DAG relaxation | O(V+E) | acyclic only; weights any sign |
| All-pairs shortest path | Floyd-Warshall | O(V^3) | any weights, **no neg cycle**; detects them |
| Minimum spanning tree | Prim (heap) / Kruskal | O(E log V) | undirected, connected; both give MST |
| Strongly connected comps | Tarjan / Kosaraju | O(V+E) | directed graph |
| Bridges / articulation | Tarjan low-link DFS | O(V+E) | undirected |
| Topological order | Kahn / DFS | O(V+E) | DAG only (cycle ⇒ no order) |
| Max-flow | Dinic | O(V^2 · E) | integer/rational capacities |
| Max bipartite matching | Hopcroft-Karp | O(E·√V) | bipartite |
| Min vertex cover (general) | — | NP-hard | 2-approx in poly time; exact FPT in k |
| TSP (metric) | Christofides | poly, 1.5-approx | triangle inequality required |
| Graph 3-coloring | — | NP-complete | 2-coloring (bipartite) is O(V+E) |

> The four bolded preconditions are the load-bearing ones. **Dijkstra is wrong on
> negative edges** — not slow, *wrong* (it finalizes a vertex's distance the
> moment it's popped, and a later negative edge can never re-open it). Use
> Bellman-Ford there, and use it again specifically to *detect* a negative cycle.

---

## Old World → New World Bridges

These are not analogies for a beginner; they are the same algorithm under two
names that a systems engineer has already met.

| You already know it as… | It is really… | Covered in |
|-------------------------|---------------|------------|
| OSPF / link-state routing | Dijkstra on the topology graph | `03` |
| BGP path-vector / RIP | distributed Bellman-Ford | `03` |
| `make` / MSBuild / Bazel dependency order | topological sort of a DAG | `02` |
| NuGet / npm version resolution | DAG + SAT/backtracking on conflicts | `02`, `07` |
| `git` commit ancestry, rebase | DAG traversal, LCA | `02` |
| Spanning-tree protocol (STP, 802.1D) | a spanning tree (not minimum) of the LAN | `04` |
| Network capacity planning | max-flow / min-cut | `06` |
| Scheduler with mutually-exclusive jobs | graph coloring / independent set | `07` |
| PageRank / "importance" ranking | stationary distribution of a random walk | `08` |
| VLSI / PCB layout, no crossings | planar embedding | `09` |

The deepest bridge: **min-cut is the dual of max-flow, and LP duality is the same
theorem you met in operations research.** `06` makes this explicit and hands off
to `operations-research/02-DUALITY.md` and `04-NETWORK-FLOWS.md`.

---

## How the Files Chain

```
        01 REPRESENTATION
              |  (fixes the cost model in V, E)
              v
        02 TRAVERSAL  ----------------+-----------------+
         BFS / DFS / topo             |                 |
              |                       |                 |
   +----------+----------+            |                 |
   v          v          v            v                 v
  03 SHORTEST 04 MST    05 STRONG    06 FLOW           (DFS is the
  PATHS       Prim/     CONNECTIVITY  max-flow          engine inside
  Dijkstra    Kruskal   SCC/bridges   = min-cut         05's low-link
  Bellman-F   union-    2-SAT         matching          and 09's planar
  Floyd-W     find                     |                test)
   |                                    | reduction
   |  (all polynomial)                  v
   +------------------------------> 07 NP-HARD GRAPHS
                                     TSP/cover/coloring/clique
                                        |
                              +---------+---------+
                              v                   v
                       08 SPECTRAL          09 PLANARITY
                       & RANDOM             & STRUCTURE
                       (relax to            (exploit
                        linear algebra)      structure)
```

---

## Decision Cheat Sheet

| I need to… | Reach for | Why / precondition |
|------------|-----------|--------------------|
| Find *any* path / check reachability | BFS or DFS (`02`) | O(V+E); BFS gives fewest-edges path |
| Shortest path, all weights ≥ 0 | Dijkstra (`03`) | heap version O((V+E) log V) |
| Shortest path, some negative edges | Bellman-Ford (`03`) | O(V·E); also detects neg cycles |
| Shortest path on a DAG | topo-order relaxation (`03`) | O(V+E), beats Dijkstra |
| All-pairs distances, dense graph | Floyd-Warshall (`03`) | O(V^3), trivial to code |
| Cheapest connecting network | Prim or Kruskal (`04`) | both are MST; Kruskal needs union-find |
| Build / dependency order | topological sort (`02`) | cycle ⇒ impossible build |
| Find tightly-coupled clusters (directed) | Tarjan SCC (`05`) | single-pass O(V+E) |
| Find single points of failure | bridges / articulation (`05`) | low-link DFS |
| Assign jobs↔workers 1:1 | bipartite matching (`06`) | Hopcroft-Karp O(E√V) |
| Max throughput / capacity bottleneck | max-flow / min-cut (`06`) | Dinic O(V²E) |
| Route a salesman / vehicle | TSP heuristics (`07`) | NP-hard; metric ⇒ Christofides 1.5 |
| Register allocation / frequency assign | graph coloring (`07`) | NP-hard; greedy + heuristics |
| Rank nodes by importance | PageRank / eigenvector (`08`) | power iteration on the graph |
| Partition / cluster a graph | spectral clustering (`08`) | Fiedler vector of the Laplacian |
| Lay out a graph without crossings | planarity test (`09`) | linear-time (Boyer-Myrvold) |
| Solve NP-hard on a "thin" graph | treewidth DP (`09`) | poly if treewidth bounded |

---

## Common Confusion Points

**"Dijkstra is just a faster Bellman-Ford."** No — it solves a *strictly smaller*
problem. Dijkstra requires non-negative weights and is *incorrect* (not merely
slow) with negative edges. Bellman-Ford is the more general algorithm; Dijkstra
buys speed by exploiting the non-negativity invariant (a finalized vertex is
never improved again). Trade generality for the log factor only when you've
verified weights ≥ 0.

**"Prim vs Kruskal — one must be better."** Both produce *a* minimum spanning
tree (identical weight; the tree itself may differ only when edge weights tie).
Choose by representation: Prim suits dense graphs and adjacency matrices
(O(V²) without a heap); Kruskal suits sparse edge lists and pairs naturally with
union-find. Neither is "the right one."

**"Topological sort is a kind of shortest path."** No. Topo sort is a *linear
ordering* of a DAG consistent with its edges — it has no weights and no notion of
distance. It *enables* O(V+E) shortest paths on a DAG (relax in topo order), but
the ordering itself is pure reachability structure.

**"NP-hard means exponential, so it's hopeless."** NP-hardness is a worst-case
statement. Real instances are often tractable via approximation (vertex cover has
a 2-approx; metric TSP has Christofides' 1.5-approx), fixed-parameter tractability
(`09`'s treewidth, FPT in the solution size k), or structure (planar graphs admit
PTASs). The cliff is real but climbable — that's the whole point of `07`–`09`.

**"This duplicates `computing/26-ALGORITHMS.md`."** That file is a *survey* —
one section on graphs among sorting, DP, and data structures. This directory is
the *depth*: full preconditions, proofs of correctness, exact bounds, and the
hard-problem theory. Use `26` for orientation, this directory for the real thing.
