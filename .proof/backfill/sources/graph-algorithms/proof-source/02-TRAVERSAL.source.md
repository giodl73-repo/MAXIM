---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "02-TRAVERSAL.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:graph-algorithms:traversal
kind: guide
module: graph-algorithms
section: mathematics-physics
title: Graph Traversal
status: source-custody
source_custody: partial
current_path: graph-algorithms/02-TRAVERSAL.md
canonical_path: graph-algorithms/02-TRAVERSAL.md
backsource_ids: [proof-backfill:graph-algorithms:02-traversal, git-history:graph-algorithms:02-traversal]
concepts: [BFS, DFS, topological sort, connected components, cycle detection]
root_concepts: [graph traversal]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Graph Traversal — BFS, DFS, and Their Decorations

Traversal is *the* primitive. Almost every algorithm in this directory is a BFS
or DFS with extra bookkeeping bolted on: shortest paths is BFS/Dijkstra with a
priority queue, topological sort is DFS with a finish-time stack, SCCs are DFS
with low-link numbers, cycle detection is DFS with a color array. Master the two
walks and the bookkeeping, and the rest of the field is variations.

```
  TRAVERSAL = (1) a frontier data structure  +  (2) a per-vertex bookkeeping array
  =============================================================================

   BFS                              DFS
   frontier = QUEUE (FIFO)          frontier = STACK (LIFO) / recursion
   explores in LAYERS by distance   explores DEEP then backtracks
   O(V+E)                           O(V+E)

        s                                s
      / | \                            / | \
     1  1  1   <- layer 1             a  .  .     dive a, then a's child,
    /|     |\                         |          then backtrack, then next
   2 2     2 2 <- layer 2             b          ...
                                      |
   gives FEWEST-EDGES paths          c          gives a DFS TREE + edge types

   +-----------------------------------------------------------------+
   | DECORATE the same O(V+E) walk to get:                          |
   |   topo sort     = DFS finish-order reversed (or Kahn's BFS)    |
   |   components    = repeat traversal from each unvisited vertex  |
   |   cycle detect  = DFS with WHITE/GRAY/BLACK colors            |
   |   bipartite test= BFS 2-coloring by layer parity              |
   +-----------------------------------------------------------------+
```

**Read the box bottom-up:** BFS and DFS are the same O(V+E) skeleton differing
only in frontier discipline (queue vs stack). Everything below the line is that
skeleton plus one array.

---

## BFS vs DFS — The Core Contrast

| Property | BFS | DFS |
|----------|-----|-----|
| Frontier | queue (FIFO) | stack / recursion (LIFO) |
| Order | by distance (layers) | by depth (dive then backtrack) |
| Time | O(V+E) | O(V+E) |
| Space | O(V) — worst frontier is a full layer | O(V) — recursion depth ≤ V |
| Finds | **fewest-edges** shortest path (unweighted) | a spanning tree; finish-time order |
| Natural for | shortest hops, level structure, bipartite test | topo sort, SCC, cycle detect, backtracking |
| Implicit-graph use | uniform-cost frontier search | iterative deepening, game trees |

> BFS gives shortest paths **only when every edge has the same cost** (hop count).
> The moment edges carry weights, BFS is wrong and you escalate to Dijkstra
> (`03`) — which is, structurally, BFS with a priority queue replacing the plain
> queue.

---

## BFS — Layer by Layer

BFS dequeues a vertex, enqueues its undiscovered neighbors, and never revisits.
Because the queue is FIFO, vertices come out in non-decreasing distance from the
source — so the first time you reach a vertex is via a fewest-edges path.

```
  Graph (undirected):        BFS from s, queue trace:
                             ----------------------------------------
       s --- a --- d        dequeue  discovers   dist set
       |           |        s        a, b        a=1, b=1
       b --- c ----+        a        d           d=2
                            b        c           c=2
                            c        (a,b seen)  -
                            d        (a seen)    -
                            => order s,a,b,c,d ; dist[d]=2 via s-a-d

  LAYERS:   L0 = {s}   L1 = {a, b}   L2 = {c, d}
```

**Correctness (why first-discovery = shortest):** BFS maintains the invariant
that the queue holds vertices of at most two consecutive distances, dequeued in
non-decreasing order. When v is first dequeued, every shorter path would have
discovered it earlier; hence `dist[v]` is exactly the hop-distance. Edges within
a layer or to an already-seen vertex are ignored — they cannot shorten anything.

> Old-world bridge: BFS is the unweighted special case of Dijkstra (all weights =
> 1). A FIFO queue *is* a priority queue when every key increments by exactly one
> — which is why a deque handles the 0/1-weight case (0-1 BFS) without a heap.

---

## DFS — The DFS Tree and Edge Classification

DFS dives as deep as possible before backtracking. Its real value is the
*structure* it exposes: a DFS forest plus a classification of every edge, which
is the substrate for topo sort, SCCs, bridges, and cycle detection.

```
  Directed graph, DFS from 0:        Edge types relative to the DFS tree:
                                     ------------------------------------
     0 ---> 1 ---> 2                 TREE  : edge to a freshly-discovered
     |      ^      |                         vertex (0->1, 1->2)
     v      |      v                 BACK  : edge to a GRAY ancestor  => CYCLE
     3 -----+      4                         (2->1 here) <-- proves a cycle
                                     FWD   : edge to a BLACK descendant
   discover/finish times:           CROSS : edge to a finished vertex in
     0: d=1            f=10                  another subtree
     1: d=2  3: d=3 f=4
     2: d=5  4: d=6 f=7 f=8 f=9      In an UNDIRECTED graph: only TREE and
                                     BACK edges exist (no fwd/cross).
```

The **white/gray/black** coloring is the key:

```
  WHITE = undiscovered     GRAY = on the recursion stack (being explored)
  BLACK = fully finished (subtree done)

  A BACK edge (to a GRAY vertex) is the definition of a cycle in a digraph.
```

---

## Topological Sort — Ordering a DAG

A topological order lists the vertices of a **DAG** (directed *acyclic* graph) so
that every edge points forward. It is the formal model of "do prerequisites
first": build dependencies, course prerequisites, task scheduling, package
install order. **A topo order exists iff the graph is acyclic** — a cycle is a
mutual dependency with no valid order.

```
  DAG of build targets:            Two equivalent algorithms:
                                   -------------------------------------------
     A ---> B ---> D               KAHN (BFS-style):              DFS (finish-time):
     |             ^                 repeatedly remove a vertex     run DFS, push each
     v             |                 with in-degree 0:              vertex on a stack
     C ------------+                   in-deg: A0 B1 C1 D2          when it FINISHES;
                                       remove A -> B0,C0            answer = stack popped
   valid orders:                       remove B -> D1               (reverse finish order)
     A, B, C, D                        remove C -> D0
     A, C, B, D                        remove D
                                     order: A,B,C,D            both O(V+E)
```

| Method | Mechanism | Cycle detection | Notes |
|--------|-----------|-----------------|-------|
| Kahn's algorithm | repeatedly remove in-degree-0 vertices | if vertices remain, a cycle exists | natural for streaming / partial orders |
| DFS finish order | reverse the order vertices finish | a back edge ⇒ cycle ⇒ no order | one pass, also gives edge classification |

> Old-world bridge: this is exactly what `make`, MSBuild, and Bazel compute to
> decide build order, and what NuGet/npm do for install order — except package
> managers must *also* resolve version conflicts, which turns the DAG into a SAT
> problem (`07`). Topo sort gives the order; SAT/backtracking resolves which
> versions form the DAG in the first place.

---

## Connected Components

A **connected component** is a maximal set of mutually reachable vertices. The
algorithm is "repeat traversal from every unvisited vertex" — each fresh start is
a new component.

```
  Undirected graph (3 components):     Algorithm:
                                       --------------------------------------
    0 - 1    3 - 4 - 5      7          for each vertex v:
        |                                if v unvisited:
        2                                  BFS/DFS from v, label all reached
                                           with a new component id
    comp 0: {0,1,2}                    => total work still O(V+E)
    comp 1: {3,4,5}
    comp 2: {7}   (isolated)           union-find (04) is the alternative,
                                       ideal for INCREMENTAL/streaming edges
```

For **undirected** graphs, BFS/DFS or union-find both work in O(V+E) (union-find
gives near-O(E·α) and handles edges arriving online). For **directed** graphs the
notion splits: *weakly* connected (connected ignoring direction) vs *strongly*
connected (mutually reachable respecting direction). Strong connectivity is its
own algorithm — Tarjan/Kosaraju in `05`.

---

## Cycle Detection — Different Rules for Directed vs Undirected

This is a classic trap: the cycle-detection rule **differs by graph class**.

```
  DIRECTED:  DFS, a BACK edge (to a GRAY/on-stack vertex) = cycle.
             A black (finished) vertex is NOT a cycle (that's a fwd/cross edge).

       0 -> 1 -> 2 -> 0     2->0 reaches GRAY 0  => CYCLE
                            (0 is still on the recursion stack)

  UNDIRECTED: DFS, any edge to a visited vertex that is NOT your DFS parent = cycle.
              (the edge back to your parent is the same edge you arrived on)

       0 - 1 - 2 - 0       at 2, edge 2-0 hits visited 0 (not parent 1) => CYCLE
       but 1-0 from inside 1 is just the parent edge, ignore it.

  Alternative for undirected: union-find. Adding an edge whose endpoints are
  ALREADY in the same set closes a cycle (this is exactly Kruskal's reject test, 04).
```

| Graph class | Detection rule | Pitfall |
|-------------|----------------|---------|
| Directed | DFS back edge to a **gray** (on-stack) vertex | a black vertex is NOT a cycle |
| Undirected | DFS edge to any visited **non-parent** vertex | forgetting to exclude the parent edge ⇒ false positive |
| Undirected (incremental) | union-find: endpoints already unioned | — |

> Bonus traversal trick — **bipartite test**: 2-color the graph by BFS layer
> parity (even layers one color, odd the other). A conflict (an edge joining two
> same-colored vertices) proves an odd cycle, hence not bipartite. This is 2-SAT's
> graph cousin (`05`) and the precondition for bipartite matching (`06`).

---

## Old World → New World Bridges

| You know it as… | It is traversal of… |
|-----------------|---------------------|
| `make` / MSBuild / Bazel build order | topological sort of a DAG |
| npm / NuGet install order | topo sort (+ SAT for version conflicts) |
| Recursive directory walk (`os.walk`, `dir /s`) | DFS of the filesystem tree |
| Web crawler / `wget --recursive` | BFS/DFS of the link graph |
| `git log --graph`, `git bisect` | DAG traversal of commit ancestry |
| Garbage collector mark phase | DFS/BFS from roots over the object graph |
| Spreadsheet recalculation order | topo sort of the cell-dependency DAG |
| Network broadcast / flooding | BFS from the source |

The GC bridge is exact: a tracing garbage collector's mark phase *is* a graph
traversal from the root set over the object reference graph; "unreachable"
literally means not visited by the traversal.

---

## Decision Cheat Sheet

| Goal | Use | Why |
|------|-----|-----|
| Fewest-edges path (unweighted) | BFS | layers = distances |
| Any path / reachability | BFS or DFS | both O(V+E) |
| Build / dependency order | topological sort | edges = prerequisites |
| Detect a cycle (directed) | DFS, gray-vertex back edge | distinguishes back from fwd/cross |
| Detect a cycle (undirected) | DFS non-parent visited, or union-find | exclude the parent edge |
| Count / label components (undirected) | repeated BFS/DFS, or union-find | one label per fresh start |
| Mutually-reachable sets (directed) | SCC (`05`), not plain components | reachability is asymmetric |
| Is the graph bipartite? | BFS 2-coloring by layer parity | conflict ⇒ odd cycle |
| Explore a huge/infinite state space | DFS w/ iterative deepening, or BFS frontier | implicit graph |

---

## Common Confusion Points

**"BFS always finds the shortest path."** Only on *unweighted* graphs (or
uniform-weight, where hop count = cost). With arbitrary weights, BFS finds the
fewest-*edges* path, which need not be the cheapest. Escalate to Dijkstra (`03`).
For 0/1 weights, 0-1 BFS with a deque suffices; no heap needed.

**"DFS and BFS find different connected components."** No — for an *undirected*
graph the components are a fixed partition; both traversals find identical
component sets. They differ only in the *tree structure* and *visit order* within
a component, not in which vertices are mutually reachable.

**"A topological sort is unique."** Rarely. Any DAG with parallel/independent
chains has many valid topo orders (the example above has both A,B,C,D and
A,C,B,D). A *unique* topo order exists iff the DAG has a Hamiltonian path (a total
order). Don't rely on a specific order unless you've imposed a tiebreak.

**"Cycle detection is the same for directed and undirected graphs."** It is not.
Directed: a back edge to an *on-stack* (gray) vertex. Undirected: an edge to any
visited *non-parent* vertex — and you must explicitly skip the parent edge or
every single edge looks like a cycle. Mixing the two rules is a frequent bug.

**"Recursion depth is free."** DFS recursion depth can reach V; on a long path
(V = 10^6) native recursion blows the stack. Production DFS uses an explicit
stack. This is an engineering precondition, not a complexity one — the bound is
still O(V+E), but the constant factor lives on the call stack.
