# graph-algorithms/ — Status

## Files

| File | Topic | Status |
|------|-------|--------|
| 00-OVERVIEW.md | Landscape: representations → traversal → paths → flows → hard problems | ✅ |
| 01-REPRESENTATIONS.md | Adjacency list/matrix, edge list, CSR; directed/weighted/multigraph tradeoffs | ✅ |
| 02-TRAVERSAL.md | BFS, DFS, topological sort, connected components, cycle detection | ✅ |
| 03-SHORTEST-PATHS.md | Dijkstra, Bellman-Ford, Floyd-Warshall, A*; preconditions and bounds | ✅ |
| 04-MINIMUM-SPANNING-TREES.md | Prim, Kruskal, union-find, cut/cycle properties | ✅ |
| 05-STRONG-CONNECTIVITY.md | SCCs (Tarjan/Kosaraju), bridges/articulation points, 2-SAT | ✅ |
| 06-MAX-FLOW-MATCHING.md | Ford-Fulkerson/Edmonds-Karp/Dinic, max-flow min-cut, bipartite matching | ✅ |
| 07-NP-HARD-GRAPHS.md | TSP, vertex cover, coloring, clique, independent set; reductions, approximation | ✅ |
| 08-SPECTRAL-AND-RANDOM.md | Laplacian, spectral clustering, PageRank, random walks, expanders | ✅ |
| 09-PLANARITY-AND-STRUCTURE.md | Planarity, Euler's formula, graph minors, treewidth, embeddings | ✅ |

## Completed

2026-06-27 — All 10 content files written. Full coverage from data structures
through provably hard problems, with every complexity bound and correctness
precondition stated explicitly (audited against the Dijkstra non-negativity /
Bellman-Ford negative-cycle / max-flow=min-cut invariants).

## Coverage Notes

Graph algorithms as the combinatorial engine beneath routing, build systems,
dependency resolution, scheduling, and network analysis. The directory is
ordered as a dependency chain: you cannot reason about complexity bounds until
you fix a representation (`01`), and every later algorithm is a structured
traversal (`02`). Shortest paths (`03`), spanning trees (`04`), and connectivity
(`05`) are the polynomial core; max-flow/matching (`06`) is the LP-dual bridge to
operations research; NP-hard graphs (`07`) mark the complexity cliff; spectral
(`08`) and structural (`09`) methods are the two escape hatches — linear algebra
and structural parameters respectively.

Treatment is peer-level for a reader who knows complexity theory and reductions
cold: no re-derivation of Big-O, no "what is a graph." Preconditions are stated
as theorems (Dijkstra requires non-negative weights; Bellman-Ford handles
negative edges and detects negative cycles; Prim/Kruskal both yield an MST;
max-flow value equals min-cut capacity). Worked ASCII graphs are checked.

Key cross-references: `computing/26-ALGORITHMS.md` (the algorithms survey this
directory expands), `computing/21-AUTOMATA.md` (complexity classes for `07`),
`operations-research/04-NETWORK-FLOWS.md` (the LP/min-cost-flow side of `06`),
`distributed-systems/` (graph structure of consensus, gossip, partition),
`machine-learning-theory/` (spectral methods, graph neural nets, PAC bounds for
`08`), `numerical-methods/` (sparse linear algebra, eigensolvers for the
Laplacian), and `number-theory/`/`abstract-algebra/` (algebraic graph theory).
