---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "09-PLANARITY-AND-STRUCTURE.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:graph-algorithms:planarity-and-structure
kind: guide
module: graph-algorithms
section: mathematics-physics
title: Planarity and Graph Structure
status: source-custody
source_custody: partial
current_path: graph-algorithms/09-PLANARITY-AND-STRUCTURE.md
canonical_path: graph-algorithms/09-PLANARITY-AND-STRUCTURE.md
backsource_ids: [mdloom-backfill:graph-algorithms:09-planarity-and-structure, git-history:graph-algorithms:09-planarity-and-structure]
concepts: [planarity, Euler formula, graph minors, treewidth, embeddings, Kuratowski]
root_concepts: [planarity, treewidth]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Planarity and Graph Structure — The Structural Escape Hatch

This is the second escape hatch from `07`'s hardness, and the more profound one:
instead of relaxing to linear algebra (`08`), *exploit the graph's structure*.
Planar graphs (drawable without crossings) and bounded-treewidth graphs ("tree-
like" graphs) admit polynomial or even linear algorithms for problems that are
NP-hard in general. The crowning theory — Robertson-Seymour graph minors — is one
of the deepest results in combinatorics, and it explains *why* structure defeats
hardness in a uniform way.

```
  STRUCTURE DEFEATS HARDNESS
  ==========================

   PLANARITY                         TREEWIDTH
   (geometric structure)             (decomposition structure)
   -------------------------         ----------------------------------
   drawable with no edge crossings   "how far from being a tree?"
        |                                 |
        |  Euler:  V - E + F = 2           |  tree (tw=1) -> series-parallel (tw=2)
        |  forbidden minors: K5, K3,3      |  -> ... -> clique K_n (tw = n-1)
        v                                  v
   LINEAR-TIME planarity test        BOUNDED treewidth => DP solves NP-hard
   (Hopcroft-Tarjan, Boyer-Myrvold)  problems in poly time (Courcelle's theorem)

         +---------------------------------------------------------+
         | ROBERTSON-SEYMOUR (graph minors): every minor-closed    |
         | family has a FINITE set of forbidden minors. Implies    |
         | poly-time membership tests for huge classes of problems.|
         +---------------------------------------------------------+
```

**Read left and right as two kinds of structure** — geometric (planarity) and
decompositional (treewidth) — unified at the bottom by the graph-minors theory.

---

## Euler's Formula — The Backbone of Planar Graphs

For any **connected planar** graph drawn without crossings, with V vertices, E
edges, and F faces (regions, including the unbounded outer one):

```
                          V - E + F = 2

  Example (a cube graph drawn planar):  V=8, E=12, F=6  ->  8 - 12 + 6 = 2  OK
  Example (a triangle):                 V=3, E=3,  F=2  ->  3 - 3  + 2 = 2  OK
                                                            (2 faces: inside + outside)
```

Two corollaries that bound how dense a planar graph can be (the source of the
linear-time algorithms — **a planar graph is sparse**):

```
  For a simple planar graph with V >= 3:
       E <= 3V - 6                  (so E = O(V): planar graphs are SPARSE)
  If additionally triangle-free (e.g. bipartite):
       E <= 2V - 4

  Consequence: every planar graph has a vertex of degree <= 5.
  Consequence: BFS/DFS/MST/etc. on planar graphs run in O(V), since E = O(V).
```

This sparsity (E = O(V)) is why the O(V+E) algorithms of `02`–`04` all become
*linear in V* on planar graphs, and it underpins the planar separator theorem
below.

---

## Testing Planarity — Kuratowski, Wagner, and Linear-Time Tests

Whether a graph *can* be drawn without crossings is decidable in **linear time**,
and characterized exactly by two forbidden substructures.

```
  THE TWO OBSTRUCTIONS (a graph is planar IFF it avoids both):

     K5 (5 mutually               K3,3 (complete bipartite,
      connected vertices)          3+3, "utilities" graph)
        *                            *   *   *
       /|\                            \ /|\ /
      * - *                            X | X
       \|/                            / \|/ \
        *--*                          *   *   *

  KURATOWSKI: planar  <=>  no SUBDIVISION of K5 or K3,3 as a subgraph.
  WAGNER:     planar  <=>  no K5 or K3,3 as a MINOR (delete/contract edges).

  ALGORITHMS:  Hopcroft-Tarjan (1974) and Boyer-Myrvold (2004) both test
               planarity AND produce an embedding in O(V) time.
```

| Tool | Statement | Use |
|------|-----------|-----|
| Euler's formula | V − E + F = 2 | quick non-planarity check via E ≤ 3V−6 |
| Kuratowski's theorem | planar ⇔ no K₅/K₃,₃ *subdivision* | characterization |
| Wagner's theorem | planar ⇔ no K₅/K₃,₃ *minor* | minor-based characterization |
| Boyer-Myrvold / Hopcroft-Tarjan | linear-time test + embedding | the practical algorithm |

> Old-world bridge: this is the math under **PCB and VLSI layout** and **graph
> drawing**. A circuit routable on a single layer with no vias is a planar graph;
> non-planarity (a K₅ or K₃,₃ minor) forces a crossing — i.e. another layer.
> Force-directed and orthogonal graph-layout engines test and exploit planarity to
> draw clean diagrams.

---

## The Four-Color Theorem and Planar Coloring

Graph coloring is NP-hard in general (`07`), but planarity tames it dramatically:

```
  FOUR-COLOR THEOREM (Appel-Haken 1976, first major computer-assisted proof):
     every planar graph is 4-colorable.

  Practically:
     2-colorable?  -> O(V+E) bipartite test (02), planar or not
     5-coloring    -> constructive, O(V) (uses the degree-<=5 vertex)
     4-coloring    -> guaranteed to EXIST, but FINDING it is still nontrivial
     3-coloring    -> NP-complete EVEN for planar graphs!
```

Note the sharp line: 4-colorability is *guaranteed* for planar graphs, but
*3-colorability of planar graphs remains NP-complete*. Planarity bounds the chromatic
number (≤ 4) without making every coloring question easy — structure helps, but
not unboundedly.

---

## Treewidth — How Tree-Like Is the Graph?

**Treewidth** measures how close a graph is to being a tree. A tree has treewidth
1; a clique on n vertices has treewidth n−1; most "real" sparse graphs have small
treewidth. The payoff: **any graph of bounded treewidth solves a huge class of
NP-hard problems in polynomial (often linear) time** via dynamic programming over
its *tree decomposition*.

```
  A TREE DECOMPOSITION covers the graph with overlapping "bags" of vertices
  arranged in a tree, such that:
    1. every vertex is in some bag
    2. every edge's endpoints share some bag
    3. the bags containing any vertex form a connected subtree

  Graph:   A-B-C-D  with B-D also:        Tree decomposition (bags):
                                            {A,B} -- {B,C,D} -- {C,D}
  WIDTH of a decomposition = (max bag size) - 1.
  TREEWIDTH = minimum width over all valid tree decompositions.
     tree -> tw 1 ;  cycle -> tw 2 ;  k x k grid -> tw k ;  K_n -> tw n-1
```

```
  WHY IT WORKS (Courcelle's theorem, informally):
    any problem expressible in monadic second-order logic (which includes vertex
    cover, independent set, dominating set, 3-coloring, Hamiltonicity, ...) is
    solvable in  f(treewidth) * O(V)  time -- LINEAR in V for fixed treewidth.

    The DP runs bag-by-bag up the tree; the bag size bounds the state space
    (2^bag for a subset problem), so small bags => small state => fast.
```

| Graph class | Treewidth | NP-hard problems become… |
|-------------|-----------|--------------------------|
| Tree / forest | 1 | trivially poly (DP on the tree) |
| Series-parallel | 2 | poly |
| Outerplanar | ≤ 2 | poly |
| k × k grid | k | poly for fixed k (exp in k) |
| Planar, diameter d | O(d) | poly when d small |
| Clique Kₙ | n − 1 | no help (as hard as general) |

> This is the **FPT escape** of `07` made structural: vertex cover is FPT in the
> *solution size* k, and *also* FPT in *treewidth*. Many real graphs (program
> control-flow graphs, dependency graphs, road networks locally) have small
> treewidth, so "NP-hard" problems on them are fast in practice. Bounded treewidth
> is the single most powerful general-purpose structural escape hatch.

---

## Graph Minors — The Unifying Theory

The **Robertson-Seymour graph minors theorem** (proved across ~20 papers,
1983-2004) is the structural capstone. A *minor* of G is any graph obtainable by
deleting vertices/edges and contracting edges. A graph family is *minor-closed* if
minors of members stay in the family (planar graphs, bounded-treewidth graphs,
and many others are minor-closed).

```
  ROBERTSON-SEYMOUR:  every minor-closed family has a FINITE set of
                      forbidden minors (an "obstruction set").

  Consequences:
   * Wagner's K5/K3,3 characterization of planarity is the SIMPLEST instance.
   * For ANY fixed minor H, "does G contain H as a minor?" is decidable in
     O(V^3) time  -> O(V^2) (improved). So every minor-closed property has a
     POLYNOMIAL membership test... though the constant can be astronomical and
     the obstruction set is often non-constructive (existence, not the list).
```

This is why structure systematically defeats hardness: minor-closed graph classes
(planar, bounded genus, bounded treewidth, knotless, ...) *all* inherit polynomial
recognition and, frequently, polynomial algorithms for otherwise-NP-hard problems.
It is the theoretical reason the escape hatches of this file exist at all.

---

## Old World → New World Bridges

| You know it as… | It is a structural-graph property |
|-----------------|-----------------------------------|
| Single-layer PCB / VLSI routing | planarity (K₅/K₃,₃ minor ⇒ needs another layer) |
| Subway / metro map "clean" drawing | planar embedding (orthogonal layout) |
| Map coloring (no two neighbors alike) | four-color theorem on the planar adjacency graph |
| Control-flow-graph analysis in a compiler | usually low treewidth ⇒ fast dataflow DP |
| Road network locally tree-like | bounded treewidth / planar separators speed routing |
| SQL query-plan / join-graph optimization | small-treewidth join graphs ⇒ tractable DP |

The compiler bridge is the most resonant for this reader: structured (goto-free)
program control-flow graphs have *bounded treewidth*, which is precisely why
dataflow analyses and register allocation, NP-hard in the abstract, run fast on
real code. Structure in the input — not a cleverer algorithm — is doing the work.

---

## Decision Cheat Sheet

| Situation | Use | Result |
|-----------|-----|--------|
| Can this be drawn without crossings? | Boyer-Myrvold planarity test | O(V), yes/no + embedding |
| Quick non-planarity sanity check | Euler: is E > 3V−6? | if yes, definitely non-planar |
| Color a planar map | four-color theorem | ≤ 4 colors guaranteed to exist |
| Is it 2-colorable? | bipartite BFS test (`02`) | O(V+E), planar or not |
| 3-color a planar graph | — | **still NP-complete** |
| NP-hard problem on a tree-like graph | tree-decomposition DP | poly if treewidth bounded |
| Decide a minor-closed property | forbidden-minor / RS test | poly (huge constant) |
| Speed up routing on a planar/road graph | planar separator decomposition | divide-and-conquer |
| Exploit small-treewidth program graph | Courcelle DP | linear for fixed treewidth |

---

## Common Confusion Points

**"Planar means it's drawn without crossings."** Planar means it *can be* drawn
without crossings — a property of the graph, not of a particular drawing. A planar
graph drawn carelessly will have crossings; planarity testing finds whether a
crossing-free embedding *exists*. (A specific crossing-free drawing is a *planar
embedding*.)

**"Euler's formula works for any graph."** It holds for *connected planar* graphs
as drawn (V − E + F = 2). For a planar graph with c connected components it's
V − E + F = 1 + c. It says nothing about non-planar graphs (which have no
well-defined face count in the plane), and the F term requires an actual planar
embedding to count faces.

**"Four colors suffice, so planar coloring is easy."** Four-colorability is
*guaranteed to exist* for planar graphs, but determining 3-colorability of a planar
graph is still NP-complete, and even *finding* a 4-coloring is nontrivial (the
existence proof is computer-assisted). "≤ 4 colors exist" ≠ "coloring is easy."

**"Low treewidth means the graph is small or sparse."** Neither. A graph can be
large and dense yet have small treewidth (a long thin grid), or small and sparse
yet have large treewidth relative to its size. Treewidth measures *tree-likeness*
(how it decomposes), independent of size and only loosely related to density. A
clique is sparse-looking per vertex but has the maximum treewidth n−1.

**"Graph minors theory gives practical algorithms."** It guarantees polynomial-time
*existence*, but the constants are often galactic and the forbidden-minor
obstruction sets are frequently non-constructive (proven finite without being
listed). Robertson-Seymour is a profound *existence* theory; treewidth DP and
explicit planarity tests are what you actually run. Don't expect a usable algorithm
to fall directly out of the minors theorem.
