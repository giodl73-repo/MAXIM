---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "04-MINIMUM-SPANNING-TREES.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:graph-algorithms:minimum-spanning-trees
kind: guide
module: graph-algorithms
section: mathematics-physics
title: Minimum Spanning Trees
status: source-custody
source_custody: partial
current_path: graph-algorithms/04-MINIMUM-SPANNING-TREES.md
canonical_path: graph-algorithms/04-MINIMUM-SPANNING-TREES.md
backsource_ids: [mdloom-backfill:graph-algorithms:04-minimum-spanning-trees, git-history:graph-algorithms:04-minimum-spanning-trees]
concepts: [minimum spanning tree, Prim, Kruskal, union-find, cut property, cycle property]
root_concepts: [minimum spanning tree]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Minimum Spanning Trees — Prim, Kruskal, and Why Greedy Works

A minimum spanning tree (MST) connects all V vertices of a weighted, *undirected*,
*connected* graph using V−1 edges of minimum total weight. The remarkable fact is
that the obvious greedy strategies — Prim's "grow from a seed" and Kruskal's "add
cheapest safe edge" — both provably produce an MST. The reason is two structural
theorems (the cut property and the cycle property), and understanding *those* is
the real content; the algorithms are corollaries.

```
  TWO GREEDY ALGORITHMS, ONE OPTIMUM
  ==================================

  Graph (undirected, weighted):       PRIM (grow a tree from a seed):
                                         start {A}; repeatedly add the cheapest
       A --1-- B                         edge LEAVING the tree.
       |     / |                         {A} -1-> B  -> {A,B} -2-> C -> {A,B,C} ...
       4   2   3                       KRUSKAL (sort edges, add if no cycle):
       |  /    |                         sort: (A,B)=1,(B,C)=2,(B,D)=3,(A,C)=4,(C,D)=5
       C --5-- D                         add 1 ok, add 2 ok, add 3 ok -> 3 edges, done.

   MST = { A-B(1), B-C(2), B-D(3) }   total weight 6, exactly V-1 = 3 edges
   (both algorithms yield this same total; here the tree is even identical)

   +-----------------------------------------------------------------+
   | WHY GREEDY IS OPTIMAL:                                          |
   |   CUT property  : the min-weight edge crossing any cut is SAFE  |
   |                   (in SOME MST). Prim exploits this directly.   |
   |   CYCLE property: the max-weight edge of any cycle is NOT in    |
   |                   any MST. Kruskal's "reject if cycle" uses it. |
   +-----------------------------------------------------------------+
```

**Read the box bottom-up:** both algorithms are greedy, and both are correct for
the same reason — the cut and cycle properties guarantee the greedy choice is
never a mistake.

---

## Preconditions and the Output Contract

> **Preconditions:** the graph is **undirected, connected, and weighted.** If it
> is *disconnected*, there is no spanning *tree*; you get a **minimum spanning
> forest** (one tree per component). MST has no meaning on a directed graph — the
> directed analogue is the *minimum arborescence* (Chu-Liu/Edmonds), a different
> and harder problem.

> **Output:** exactly V−1 edges, total weight minimized. **Both Prim and Kruskal
> produce an MST of identical total weight.** The *tree itself* is unique iff all
> edge weights are distinct; with ties, different MSTs (and different algorithms)
> may pick different edges of equal total weight.

---

## The Two Structural Theorems

Everything rests on these. They are about *which edges must or must not appear*,
independent of any algorithm.

```
  CUT PROPERTY                          CYCLE PROPERTY
  ------------                          --------------
  A "cut" splits V into (S, V\S).       Take any cycle.
  Consider all edges crossing it.       Its strictly-MAX-weight edge is in
  The MINIMUM-weight crossing edge      NO minimum spanning tree.
  belongs to SOME MST. (It is "safe".)

     S | V\S                               cycle: A-B(1)-C(2)-A(4)
   A---+---C   crossing edges: A-C(4),     the max edge A-C(4) can be dropped:
   |   |   |   B-D(3)... the cheapest        replace it by going A-B-C, cheaper.
   B---+---D   crossing edge is SAFE.        => 4-edge never in an MST.
```

**Cut property (proof sketch):** Let e be the min crossing edge of cut (S, V\S).
Suppose an MST T excludes e. Adding e to T creates a cycle that must cross the cut
on some other edge e′ with w(e′) ≥ w(e). Swap: T − e′ + e is a spanning tree of
weight ≤ w(T), so it's also an MST and contains e. Hence e is safe. ∎

**Cycle property** is the contrapositive: the heaviest edge on a cycle is always
swappable for a lighter alternative path, so it never *needs* to be in an MST.

> These are *exchange arguments* — the same proof technique behind matroid
> greedy-optimality. An MST is exactly the minimum-weight basis of the **graphic
> matroid**, which is the deep reason greedy works here and not for, say, TSP.

---

## Kruskal — Sort, Then Add If No Cycle

Kruskal sorts all edges by weight and adds each edge unless it would form a cycle
(checked via union-find). It is **O(E log E) = O(E log V)** — dominated by the
sort. (E ≤ V², so log E ≤ 2 log V; the two are equal up to a constant.)

```
  Kruskal:
    sort edges ascending by weight
    for each edge (u,v) in order:
        if find(u) != find(v):     # endpoints in different components?
            add (u,v) to MST        # YES -> safe (cut property), keep it
            union(u, v)
        # else they're already connected -> adding closes a CYCLE -> reject
                                    #         (cycle property)

  Trace on the example graph:
    (A,B)1: A,B separate -> ADD,  union -> {A,B}
    (B,C)2: B,C separate -> ADD,  union -> {A,B,C}
    (B,D)3: B,D separate -> ADD,  union -> {A,B,C,D}   3 edges, STOP
    (A,C)4: same set     -> REJECT (would cycle)
    (C,D)5: same set     -> REJECT
```

The "reject if endpoints already connected" test is the cycle property in action,
and the engine that makes it O(α) per edge is **union-find**.

---

## Union-Find (Disjoint-Set Union) — Near-Constant Per Operation

Union-find maintains a partition of vertices into disjoint sets with two
operations: `find(x)` (which set?) and `union(x,y)` (merge two sets). With both
optimizations — **union by rank/size** and **path compression** — m operations on
n elements run in **O(m · α(n))**, where α is the inverse Ackermann function,
< 5 for any conceivable n. Effectively constant.

```
  Forest of parent pointers (each set = a tree, root = representative):

   find(x): follow parent pointers to the root.
            PATH COMPRESSION: re-point every node on the path directly to root.

      before find(D):        after find(D) (compressed):
        A                       A
        |                      /|\
        B                     B C D    <- all now point straight at the root
        |
        C
        |
        D

   union(x,y): link the SHORTER tree under the TALLER (union by rank/size),
               keeping trees shallow so future finds stay fast.
```

| Optimization | Without | With both |
|--------------|---------|-----------|
| Per-operation amortized | O(log n) or worse | **O(α(n)) ≈ O(1)** |
| What it does | — | path compression flattens; union-by-rank stays balanced |

> Union-find is also the engine for **incremental connectivity** (`02`),
> **cycle detection in a growing undirected graph**, and offline **least common
> ancestor** queries. It's one of the highest-leverage 30 lines in all of
> algorithms.

---

## Prim — Grow One Tree From a Seed

Prim starts from any vertex and repeatedly adds the cheapest edge leaving the
current tree, using a priority queue keyed by "cheapest known edge to the tree."
With a binary heap it is **O(E log V)**; with a Fibonacci heap **O(E + V log V)**;
with no heap on a dense matrix, **O(V²)** — which *beats* the heap version when
E ≈ V².

```
  Prim from A (priority queue of frontier edges):
    tree={A}; push A's edges. cheapest = A-B(1) -> add B. tree={A,B}
    frontier now: B-C(2), B-D(3), A-C(4). cheapest = B-C(2) -> add C. tree={A,B,C}
    frontier: B-D(3), C-D(5).             cheapest = B-D(3) -> add D. DONE.
    MST = {A-B, B-C, B-D}, weight 6.

  Each step picks the min crossing edge of the cut (tree, rest) == CUT PROPERTY.
```

```
   PRIM grows ONE connected blob:        KRUSKAL grows a FOREST that merges:

     (A)        (A)-(B)      (A)-(B)        A  B  C  D   ->  A-B  C  D
      |   ->     |       ->   | \           (separate)      then  A-B-C  D
                              (C) (D)                       then  A-B-C-D
```

---

## Prim vs Kruskal — Choose by Representation

| | Prim | Kruskal |
|---|------|---------|
| Strategy | grow one tree (vertex-centric) | merge a forest (edge-centric) |
| Core data structure | priority queue | sort + union-find |
| Time (heap / sort) | O(E log V) | O(E log V) |
| Time, dense (E≈V²) | **O(V²)** with array, no heap | O(V² log V) |
| Best when | dense graphs, adjacency matrix | sparse graphs, edge list given |
| Edges arrive online | awkward (tree must stay connected) | natural (sort, union as they come) |
| Both produce | **an MST** | **an MST** (identical total weight) |

> Neither is "better." Prim suits dense graphs and the adjacency-matrix O(V²)
> form; Kruskal suits sparse graphs already represented as an edge list and pairs
> with union-find. For E ≈ V² choose Prim-without-heap; for E ≈ V choose either.

---

## Old World → New World Bridges

| You know it as… | It relates to MST via… |
|-----------------|------------------------|
| Spanning Tree Protocol (STP, 802.1D) | builds *a* spanning tree to kill L2 loops — RSTP uses path *cost*, edging toward minimum |
| Network/cluster cabling to minimize cost | the textbook MST application (least cable to connect all sites) |
| Single-linkage hierarchical clustering | the merge order *is* Kruskal — clusters merge by nearest pair |
| Circuit / chip net routing (minimize wire) | Steiner-tree relaxes to MST when no extra junctions allowed |
| Image segmentation (Felzenszwalb) | MST-based region merging on the pixel graph |

The single-linkage clustering bridge is exact: running Kruskal and stopping after
k−1 merges leaves exactly k connected components — that *is* single-linkage
agglomerative clustering into k clusters.

---

## Decision Cheat Sheet

| Situation | Use | Reason |
|-----------|-----|--------|
| Sparse graph, edge list available | Kruskal | sort + union-find, O(E log V) |
| Dense graph (E ≈ V²) | Prim, array (no heap) | O(V²) beats heap versions |
| Edges streaming / arriving online | Kruskal | union as edges come |
| Need k clusters | Kruskal, stop after V−k unions | leaves k components |
| Graph disconnected | either ⇒ minimum spanning **forest** | one tree per component |
| Directed graph | neither — use Chu-Liu/Edmonds arborescence | MST is undirected-only |
| Need incremental connectivity queries | union-find alone | O(α) per op |
| Want second-best MST / sensitivity | cycle property + edge swaps | replace one tree edge |

---

## Common Confusion Points

**"Prim and Kruskal can give different-weight trees."** Never. Both produce a
minimum spanning tree, so the *total weight is identical and optimal*. Only the
specific edge set can differ, and only when edge weights tie. If all weights are
distinct, the MST is unique and both algorithms return the exact same tree.

**"MST gives the shortest path between two vertices."** No — that's a category
error. The MST minimizes *total connection cost across all vertices*; the path
between two vertices *within* the MST is generally **not** their shortest path.
Shortest paths is `03` (Dijkstra/Bellman-Ford); MST is a global optimum, not a
pairwise one.

**"MST works on directed graphs."** No. MST is defined only for undirected
graphs. The directed analogue — a minimum-weight *arborescence* rooted at r,
where every vertex is reachable from r — requires Chu-Liu/Edmonds and is a
distinct algorithm. Don't run Prim/Kruskal on a digraph.

**"Negative edge weights break MST algorithms."** They don't. Unlike shortest
paths (where negatives change everything), Prim and Kruskal are correct with
negative weights — the cut and cycle properties never assumed non-negativity.
There's no "negative cycle" pathology because a tree has no cycles by definition.

**"Union-find is O(log n) per operation."** With *both* path compression and
union-by-rank it is O(α(n)) amortized — inverse Ackermann, effectively constant.
With only one of the two optimizations it degrades to O(log n). With neither it
can hit O(n) per find. The near-constant bound requires both.
