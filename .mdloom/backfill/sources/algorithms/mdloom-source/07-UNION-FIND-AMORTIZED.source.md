---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "07-UNION-FIND-AMORTIZED.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:algorithms:union-find-amortized
kind: guide
module: algorithms
section: mathematics-physics
title: Union-Find and Amortized Analysis
status: source-custody
source_custody: partial
current_path: algorithms/07-UNION-FIND-AMORTIZED.md
canonical_path: algorithms/07-UNION-FIND-AMORTIZED.md
backsource_ids: [mdloom-backfill:algorithms:07-union-find-amortized, git-history:algorithms:07-union-find-amortized]
concepts: [union-find, disjoint set union, path compression, union by rank, inverse ackermann, amortized analysis, potential method]
root_concepts: [union-find]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Union-Find and Amortized Analysis

Union-Find (disjoint-set union, DSU) maintains a partition of elements into disjoint
sets under two operations — `find` (which set is x in?) and `union` (merge two sets)
— and it is the cleanest masterpiece of amortized analysis in the field. With two
small heuristics (union by rank, path compression) a sequence of `m` operations on
`n` elements runs in `O(m·α(n))`, where `α` is the inverse Ackermann function — for
all practical `n`, `α(n) ≤ 4`. This guide both gives the structure and uses it as the
worked example for the **potential method** of amortized analysis (`01`).

```
  UNION-FIND: a partition under find + union, near-constant per operation
  =====================================================================================

   FOREST REPRESENTATION: each set = a rooted tree; the ROOT is the set's representative.

      {1,2,3}   {4,5}      arrays:  parent: [.,1,1,1,4,4]   (1 and 4 are roots)
        1         4                 rank:   [.,1,0,0,1,0]
       / \        |
      2   3       5
     find(3) = climb to root = 1.    union(3,5): make root 4 point to root 1 (by rank).

   TWO HEURISTICS (both needed for the bound):
     UNION BY RANK   attach the shorter tree under the taller (rank ~ height upper bound)
                     -> keeps trees O(log n) tall by itself
     PATH COMPRESSION on find, point every node on the path DIRECTLY at the root
                     -> flattens the tree for future finds

   THE BOUNDS (state them exactly):
     by rank ALONE OR compression alone:  O(log n) amortized per op
     by rank AND path compression:        O(alpha(n)) amortized per op   [Tarjan]
       alpha(n) = inverse Ackermann <= 4 for n up to ~2^65536  -> effectively O(1)
     a SINGLE find can still be O(log n); the bound is AMORTIZED over the sequence.
```

**Read the bound carefully**: the `α(n)` is *amortized*, not worst-case — one
unlucky `find` traverses a long chain, but path compression pays it forward so the
*total* over any sequence is `O(m·α(n))`. This is the canonical "the average over the
sequence is what's guaranteed" structure.

---

## Layer 1: The Naive Structure and Why It's Slow

```
   NAIVE: union by just pointing one root at the other, no heuristic.
   Adversary unions in a chain:  union(1,2),union(2,3),union(3,4),...

      1 <- 2 <- 3 <- 4 <- 5    (a degenerate path)
   find(5) walks the whole chain -> O(n).  m finds -> O(mn). BAD.

   The two heuristics independently fix the height, and TOGETHER give alpha(n).
```

---

## Layer 2: Union by Rank

Attach the tree with smaller rank under the one with larger rank; on a tie, increment
the new root's rank. Rank is an *upper bound on height*.

```
   union(x,y):
     rx = find(x); ry = find(y)
     if rank[rx] < rank[ry]: parent[rx] = ry
     elif rank[rx] > rank[ry]: parent[ry] = rx
     else: parent[ry] = rx; rank[rx] += 1   # tie: pick one, bump its rank

   INVARIANT: a tree of rank r has >= 2^r nodes.
   => rank <= log2(n)  => height <= log2(n)  => find is O(log n) by rank ALONE.
```

The `2^r` node bound is the key lemma: rank only increments on a tie of equal-rank
trees, which doubles the subtree size, so rank `r` certifies at least `2^r` members —
exactly bounding height by `log n`.

---

## Layer 3: Path Compression

On every `find`, after locating the root, repoint every node along the path directly
to the root. Future finds on those nodes are O(1).

```
   find(x) with compression:
     if parent[x] != x: parent[x] = find(parent[x])   # recurse, then flatten
     return parent[x]

   BEFORE find(7):          AFTER find(7) compresses the path 7->5->3->1:
        1                        1
        |                       /|\ \
        3                      3 5 7 (and 2,4,6 flattened too)
        |
        5
        |
        7
   every node on the find path now points STRAIGHT at the root.
```

Compression alone (without rank) also gives `O(log n)` amortized. The magic is the
*combination*.

---

## Layer 4: The α(n) Bound and the Potential Method

With both heuristics, Tarjan's analysis gives `O(α(n))` amortized per operation. The
proof is a **potential-method** argument (`01`) — the marquee application of that
technique.

```
   THE INVERSE ACKERMANN FUNCTION alpha(n):
     Ackermann A(m,n) grows astronomically; alpha is its (very slow) inverse.
       alpha(n) <= 1  for n <= 2
       alpha(n) <= 2  for n <= 4
       alpha(n) <= 3  for n <= 16
       alpha(n) <= 4  for n <= 2^2^2^16  (a number with ~19729 digits)
     => for ANY n that fits in this universe, alpha(n) <= 4. Effectively constant, but
        NOT a true constant -- the bound is genuinely O(m alpha(n)), and that is TIGHT
        (Fredman-Saks lower bound: you cannot do better in the cell-probe model).

   POTENTIAL-METHOD SKETCH (why it works):
     Assign each non-root node a POTENTIAL based on the rank gap to its parent
     (a "level" derived from the Ackermann hierarchy).
     - union: O(1) actual, bounded potential change.
     - find:  each node whose parent-rank jumps a "level" is charged O(1) to the
       operation; nodes that don't are paid by their DECREASING potential.
     Amortized cost per op = actual + dPhi = O(alpha(n)).
   This is the SAME machinery as 01's dynamic-array proof, applied to a far subtler
   potential function.
```

**This bound is tight, not just convenient.** Fredman and Saks proved a matching
`Ω(α(n))` lower bound in the cell-probe model — so union-find is genuinely *not* O(1)
per operation, even though `α(n) ≤ 4` makes it indistinguishable from constant in
practice. It is the rare data structure whose exact amortized complexity is a
non-constant, provably optimal function.

---

## Layer 5: What Union-Find Powers

```
   APPLICATIONS (the find/union pattern in the wild)
   -------------------------------------------------
   KRUSKAL'S MST          cycle test = "are u,v already connected?" = find(u)==find(v)
                          (graph-algorithms/04) -- DSU is what makes Kruskal O(E log E)
   CONNECTED COMPONENTS   offline/incremental connectivity in a graph (graph-algorithms/02)
   PERCOLATION / grids    merge open neighboring cells, query top-bottom connectivity
   IMAGE SEGMENTATION     merge adjacent similar pixels into regions
   EQUIVALENCE / UNIFY    type unification, equality saturation (programming-language-theory/)
   DYNAMIC CONNECTIVITY   incremental (union-only) is easy; full (with deletes) needs more

   NOTE: union-find handles INCREMENTAL connectivity (only adds). Edge DELETION needs
   link-cut trees / Euler-tour trees -- a different, harder structure.
```

The Kruskal connection is the canonical one: union-find is exactly the structure that
answers "would adding this edge form a cycle?" in near-constant time, turning the MST
greedy (`05`, `graph-algorithms/04`) from O(VE) into O(E log E). Type unification in a
compiler (`programming-language-theory/`) uses the same `union`/`find` to merge type
variables — a bridge any compiler-literate engineer will recognize.

---

## Old World → New World Bridges

| You already know | The union-find / amortized concept |
|---|---|
| "Are these two nodes in the same cluster?" | `find(u) == find(v)` — O(α(n)) amortized membership test |
| Kruskal's MST cycle check | union-find is the structure that makes it fast (`graph-alg/04`) |
| Type unification in a type checker | `union`/`find` over type variables (`programming-language-theory/`) |
| Incremental graph connectivity in a tool | union-only DSU; deletions need link-cut trees |
| Dynamic-array "O(1) push" amortized | Same potential-method reasoning, simpler Φ (`01`) |
| "It's O(1) for all practical purposes" | α(n) ≤ 4 — true operationally, but *provably* not constant |

The type-unification bridge lands for anyone who has touched a compiler: Hindley-Milner
inference merges equivalence classes of type variables, and the engine underneath is
exactly this `union`/`find`.

---

## Decision Cheat Sheet

| I need... | Use | Bound |
|---|---|---|
| Incremental connectivity / merge sets | union-find (rank + compression) | O(α(n)) amortized |
| Kruskal MST cycle test | union-find | O(α(n)) per edge |
| Connected components offline | union-find | O((V+E)·α(V)) |
| Type/term unification | union-find over variables | O(α(n)) amortized |
| Connectivity with *deletions* | link-cut / Euler-tour trees | O(log n) — not DSU |
| Prove a sequence amortized bound | potential method (`01`) | Φ + ΔΦ |
| Just union by rank, simpler | rank only | O(log n) amortized |

---

## Common Confusion Points

### "Union-find is O(1) per operation"

It is **O(α(n)) amortized**, and that bound is *tight* (Fredman-Saks lower bound) — it
is genuinely not constant. For every realistic `n`, `α(n) ≤ 4`, so it is
indistinguishable from O(1) in practice, but quoting it as O(1) in a complexity proof
is incorrect. A *single* `find` can also be O(log n); only the sequence is near-constant.

### "Either union-by-rank or path compression alone gives α(n)"

No — *each one alone* gives only `O(log n)` amortized. The `O(α(n))` bound requires
**both** heuristics together. Implementations that include only one are asymptotically
slower (still fine for many uses, but not the famous bound).

### "Union-find handles dynamic connectivity, including edge deletion"

It handles **incremental** (union-only) connectivity. It cannot efficiently *delete*
an edge / split a set — undoing a union is not an O(α) operation. Fully dynamic
connectivity (insertions and deletions) needs link-cut trees or Euler-tour trees with
O(log n)-style bounds.

### "Rank equals the tree's height"

Rank is an *upper bound* on height, not the exact height. Path compression flattens
trees and reduces actual heights below their ranks (ranks are never decremented). The
analysis only needs rank as a monotone, `2^r`-node-certifying quantity, not as the
true height.

### "α(n) and log*(n) are the same"

They are both extremely slow-growing, but α (inverse Ackermann) grows *even slower*
than log* (iterated logarithm). The union-find bound is the tighter `α(n)`; conflating
them understates how good the result is. Both are ≤ small constants for any real `n`,
but they are different functions.
