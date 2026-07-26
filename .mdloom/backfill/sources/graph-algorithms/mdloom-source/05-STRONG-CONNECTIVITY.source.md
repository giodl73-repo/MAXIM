---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-STRONG-CONNECTIVITY.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:graph-algorithms:strong-connectivity
kind: guide
module: graph-algorithms
section: mathematics-physics
title: Strong Connectivity and Graph Decomposition
status: source-custody
source_custody: partial
current_path: graph-algorithms/05-STRONG-CONNECTIVITY.md
canonical_path: graph-algorithms/05-STRONG-CONNECTIVITY.md
backsource_ids: [mdloom-backfill:graph-algorithms:05-strong-connectivity, git-history:graph-algorithms:05-strong-connectivity]
concepts: [strongly connected components, Tarjan, Kosaraju, bridges, articulation points, 2-SAT]
root_concepts: [strong connectivity]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Strong Connectivity — SCCs, Bridges, and 2-SAT

This file is about *decomposing* a graph by connectivity structure, and it is a
showcase of one technique — a single DFS augmented with **discovery times and
low-link values** — solving four problems at once: strongly connected components,
bridges, articulation points, and (via SCCs) 2-SAT. The low-link idea is the
trick worth owning; everything here is a corollary of it.

```
  ONE DFS, FOUR RESULTS (all O(V+E))
  ==================================

   DFS assigns each vertex:
     disc[v]  = discovery time (order first reached)
     low[v]   = lowest disc reachable from v's subtree via >= 0 tree edges + 1 back edge

                         +----------------------------------------+
   DIRECTED graph -----> |  SCCs: Tarjan (1 DFS) or Kosaraju (2)  |
                         +----------------------------------------+
                                    |
                                    v  condensation (SCCs -> super-nodes) is a DAG
                         +----------------------------------------+
   UNDIRECTED graph ---> |  BRIDGES: edge (u,v) with low[v]>disc[u]|
                         |  ARTICULATION: vertex whose removal      |
                         |    splits the graph                     |
                         +----------------------------------------+
                                    |
                                    v  application
                         +----------------------------------------+
   Boolean 2-SAT -------> |  build implication graph, SCC it:      |
                         |  SAT iff no var x and ~x in same SCC    |
                         +----------------------------------------+
```

**Read top-down:** disc/low feed SCCs (directed) and bridges/articulation
(undirected); SCCs in turn solve 2-SAT.

---

## Strongly Connected Components (SCCs)

In a **directed** graph, an SCC is a maximal set of vertices that are *mutually
reachable*: for every pair u, v in the SCC, there is a path u→v *and* a path v→u.
SCCs partition the vertices. Contracting each SCC to a single super-node yields
the **condensation**, which is always a **DAG** — the "skeleton" of the graph's
reachability.

```
  Directed graph:                 SCCs:
                                  ---------------------------------
     A ---> B ---> C              {A, B, D} are mutually reachable
     ^      |      |              (A->B->D->A is a cycle)
     |      v      v              {C, E}     are mutually reachable
     D <----+      E              (C->E->C ... if E->C exists)
            |      ^
            +------+              CONDENSATION (a DAG):
                                    [ABD] ---> [CE]
                                  reachability collapses to a clean DAG.
```

> **Why "strongly"?** *Weakly* connected = connected if you ignore edge
> directions (just `02`'s components on the underlying undirected graph).
> *Strongly* connected requires mutual reachability *respecting* direction — a
> genuinely harder, directed-only notion.

### Tarjan vs Kosaraju — Two Linear Algorithms

| | Tarjan | Kosaraju |
|---|--------|----------|
| DFS passes | **one** | **two** (graph, then transpose Gᵀ) |
| Extra structure | a stack of "open" vertices + low-link | finish-order stack, then transpose |
| Time | O(V+E) | O(V+E) |
| Needs the transpose Gᵀ? | no | yes (reverse all edges) |
| Intuition | low[v]==disc[v] ⇒ v roots an SCC | 2nd DFS in reverse finish order peels SCCs |

```
  KOSARAJU (easiest to reason about):
    1. DFS on G, push each vertex on a stack when it FINISHES.
    2. Transpose the graph (reverse every edge) -> G^T.
    3. Pop vertices off the stack; DFS each in G^T. Each DFS tree = one SCC.

  TARJAN (one pass, the production choice):
    DFS maintaining disc[] and low[]. Keep visited-but-unassigned vertices on a
    stack. When a vertex v finishes with low[v]==disc[v], it is the ROOT of an
    SCC: pop the stack down to v -- those vertices are exactly that SCC.
```

> Old-world bridge: SCC condensation is how you find **circular dependencies** in
> a module/package graph. NuGet/npm "cyclic dependency" errors are non-trivial
> SCCs in the dependency digraph; a valid build order (topo sort, `02`) exists
> *only* on the condensation DAG, never inside an SCC.

---

## Bridges and Articulation Points — Single Points of Failure

In an **undirected** graph, a **bridge** is an edge whose removal increases the
number of connected components; an **articulation point** (cut vertex) is a vertex
whose removal does the same. These are exactly the single points of failure in a
network — the things a resilient design must avoid.

```
  Undirected graph:                 BRIDGE: edge B-C
                                    -------------------------------
     A --- B --- C --- D            removing B-C disconnects {A,B} from {C,D}.
            \   /                   ARTICULATION POINTS: B and C
             (no - acyclic here)    removing B isolates A; removing C isolates D.

     With a cycle, no bridge:       Low-link test:
     A --- B --- C                    edge (u,v) is a BRIDGE iff  low[v] > disc[u]
            \   /                      (v's subtree has NO back edge above u)
             D                       u is an ARTICULATION point iff some child v
     B-C, C-D, D-B form a cycle:       has  low[v] >= disc[u]  (root: >= 2 children)
     no single edge removal splits.
```

The mechanism is the same disc/low DFS as Tarjan. The intuition: an edge (u→v) in
the DFS tree is a bridge exactly when v's subtree cannot "escape above" u via any
back edge — formally `low[v] > disc[u]`. A back edge provides redundancy; its
absence is a single point of failure.

> Old-world bridge: this is automated **network resilience analysis**. A bridge in
> the physical topology is a link whose failure partitions the network; an
> articulation point is a router/switch whose failure does. The same DFS that
> finds SCCs in your service-call graph finds the single points of failure in your
> infrastructure.

---

## Biconnectivity — The Redundancy Guarantee

A graph is **biconnected** if it has no articulation points: every pair of
vertices lies on a common cycle, so there are *two vertex-disjoint paths* between
any two vertices (Menger's theorem). Biconnected components partition the *edges*.
This is the formal statement of "the network survives any single node failure" —
exactly the property a fault-tolerant topology design targets.

```
  k-connectivity (Menger's theorem):
    a graph is k-vertex-connected  <=>  every pair has k vertex-disjoint paths
    a graph is k-edge-connected    <=>  every pair has k edge-disjoint paths

  These connectivity numbers are computable via MAX-FLOW (06): the max number of
  edge-disjoint s-t paths equals the min s-t cut (Menger == max-flow/min-cut).
```

> This is the bridge to `06`: edge-connectivity *is* a min-cut computation.
> Menger's theorem (vertex/edge-disjoint paths) is the combinatorial face of the
> max-flow/min-cut theorem. The same duality recurs throughout the directory.

---

## 2-SAT — Boolean Satisfiability in Linear Time

General SAT is NP-complete (`07`), but the special case where every clause has
**exactly two literals** (2-SAT) is solvable in **O(V+E)** — and the algorithm is
*pure SCC*. This is one of the most satisfying reductions in the field: a logic
problem becomes a graph-connectivity problem.

```
  Each 2-clause (a OR b) is logically two IMPLICATIONS:
        (a OR b)  ==  (~a => b)  AND  (~b => a)

  Build the IMPLICATION GRAPH: a vertex for each literal x and ~x; an edge for
  each implication. Then:

     SATISFIABLE  <=>  no variable x has  x  and  ~x  in the SAME SCC.

  Why: x and ~x in one SCC means x => ~x AND ~x => x, forcing x = ~x. Contradiction.

  Assignment: in the condensation DAG (reverse topo order), set a literal TRUE if
  its SCC comes AFTER its negation's SCC.

  Example: (x OR y) AND (~x OR y) AND (~y OR z)
     edges: ~x->y, ~y->x, x->y, ~y->x, y->z, ~z->y ...
     compute SCCs; check no {x,~x} pair shares one -> SATISFIABLE, read off values.
```

| SAT variant | Complexity | Method |
|-------------|------------|--------|
| 2-SAT | **O(V+E)** | implication graph + SCC |
| Horn-SAT | linear | unit propagation |
| 3-SAT (and general SAT) | **NP-complete** | DPLL/CDCL heuristics (`07`) |

> The jump from 2-SAT (polynomial) to 3-SAT (NP-complete) is the cleanest
> illustration of the complexity cliff in the whole directory: one extra literal
> per clause moves you from a linear-time SCC computation to the canonical
> NP-complete problem. This is the boundary the learner knows from complexity
> theory, made concrete.

---

## Old World → New World Bridges

| You know it as… | It is a connectivity-decomposition of… |
|-----------------|----------------------------------------|
| Circular package/module dependencies | a non-trivial SCC in the dependency digraph |
| Valid build order requires no cycles | topo sort works only on the SCC condensation DAG |
| Single point of failure in a network | an articulation point / bridge |
| "Two independent network paths" SLA | biconnectivity / 2-edge-connectivity |
| Deadlock detection (wait-for graph) | a cycle = SCC in the resource wait-for graph |
| Constraint config "A implies B" feasibility | 2-SAT on the implication graph |

The deadlock bridge is exact: an OS deadlock is a cycle in the resource-allocation
*wait-for* graph; detecting deadlock is detecting a non-trivial SCC, the same
Tarjan pass.

---

## Decision Cheat Sheet

| Goal | Use | Time |
|------|-----|------|
| Mutually-reachable groups (directed) | Tarjan or Kosaraju SCC | O(V+E) |
| One-pass SCC, production code | Tarjan | O(V+E) |
| SCC, easiest to reason about | Kosaraju (needs transpose) | O(V+E) |
| Reachability skeleton of a digraph | condensation (SCCs → DAG) | O(V+E) |
| Find single-point-of-failure edges | bridges (low-link DFS) | O(V+E) |
| Find single-point-of-failure nodes | articulation points | O(V+E) |
| Verify "survives any single failure" | biconnectivity test | O(V+E) |
| Solve a 2-literal-clause SAT | 2-SAT via implication-graph SCC | O(V+E) |
| Detect a deadlock / circular dependency | SCC on wait-for / dependency graph | O(V+E) |
| k disjoint paths between two nodes | max-flow / min-cut (`06`) | flow time |

---

## Common Confusion Points

**"Weakly and strongly connected are the same."** No. Weakly connected ignores
direction (it's just `02`'s undirected components on the underlying graph).
Strongly connected requires mutual reachability *respecting* direction. A simple
directed path A→B→C is weakly connected (one piece) but has three singleton SCCs
(no vertex can reach back). Always specify which you mean.

**"The condensation can have a cycle."** Never. Contracting each SCC to a node
*always* yields a DAG. If the condensation had a cycle, the SCCs on that cycle
would themselves be mutually reachable, so they'd be a single larger SCC —
contradicting maximality. This acyclicity is what lets you topo-sort the
condensation.

**"Bridges and articulation points are the same thing."** Related but distinct.
A bridge is an *edge* whose removal disconnects; an articulation point is a
*vertex* whose removal disconnects. Every bridge endpoint is usually an
articulation point, but a graph can have articulation points and *zero* bridges
(e.g. two triangles sharing one vertex — that shared vertex is an articulation
point, but no single edge is a bridge).

**"Tarjan needs the transpose graph."** No — *Kosaraju* needs the transpose (its
second DFS runs on Gᵀ). *Tarjan* is a single DFS on the original graph using the
low-link stack. Confusing which algorithm needs the transpose is a common slip.

**"2-SAT is hard because SAT is NP-complete."** 2-SAT is *polynomial* — O(V+E) via
SCC. The NP-completeness of general SAT kicks in at 3 literals per clause. The
2-literal restriction is special precisely because each clause becomes two clean
implications, and implication is transitive (hence captured by reachability/SCC).
3-SAT has no such two-implication decomposition.
