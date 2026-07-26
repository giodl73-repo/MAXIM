---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "01-REPRESENTATIONS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:graph-algorithms:representations
kind: guide
module: graph-algorithms
section: mathematics-physics
title: Graph Representations
status: source-custody
source_custody: partial
current_path: graph-algorithms/01-REPRESENTATIONS.md
canonical_path: graph-algorithms/01-REPRESENTATIONS.md
backsource_ids: [mdloom-backfill:graph-algorithms:01-representations, git-history:graph-algorithms:01-representations]
concepts: [adjacency list, adjacency matrix, edge list, CSR, sparse graphs, directed weighted graphs]
root_concepts: [graph representation]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Graph Representations

The representation is not a detail — it *is* the cost model. Every bound in the
rest of this directory is quoted in terms of V (vertices) and E (edges), and
whether a bound is achievable at all depends on whether your representation makes
"iterate neighbors of v" cheap (lists) or "does edge (u,v) exist?" cheap
(matrix). Pick wrong and an O(V+E) algorithm silently becomes O(V²).

```
  REPRESENTATIONS OF THE SAME GRAPH (V=4, E=4, directed)
  ======================================================

     Graph:                Adjacency LIST          Adjacency MATRIX
                           (array of lists)         (V x V bit/weight)
       0 ---> 1                                         to: 0 1 2 3
       |    / |             0 -> [1, 2]              from 0 [0 1 1 0]
       v   /  v             1 -> [3]                      1 [0 0 0 1]
       2 <-   3             2 -> []                       2 [0 0 0 0]
                            3 -> [2]                      3 [0 0 1 0]
                                                    
     EDGE LIST                          CSR (compressed sparse row)
     (u, v[, w]) tuples                 row_ptr = [0, 2, 3, 3, 4]
       (0,1) (0,2) (1,3) (3,2)          col_idx = [1, 2, 3, 2]
                                        (neighbors of v = col_idx[row_ptr[v] : row_ptr[v+1]])

  SPACE:   list O(V+E)   matrix O(V^2)   edge list O(E)   CSR O(V+E), cache-tight
```

**Read this as four encodings of one fact set.** The list and CSR scale with the
*number of edges*; the matrix scales with the *number of vertex pairs*. For the
sparse graphs that dominate real systems (E ≈ V, not V²), that difference is the
whole game.

---

## The Cost Model in One Table

This is the table to internalize. Density is the deciding variable: a graph is
**sparse** when E = O(V) and **dense** when E = Θ(V²).

| Operation | Adjacency list | Adjacency matrix | Edge list | CSR |
|-----------|---------------|------------------|-----------|-----|
| Space | O(V+E) | O(V²) | O(E) | O(V+E) |
| Edge exists (u,v)? | O(deg u) | **O(1)** | O(E) | O(deg u) |
| Iterate neighbors of v | **O(deg v)** | O(V) | O(E) | **O(deg v)** |
| Iterate all edges | O(V+E) | O(V²) | **O(E)** | O(V+E) |
| Add edge | O(1) | O(1) | O(1) | rebuild |
| Delete edge | O(deg u) | O(1) | O(E) | rebuild |
| Add vertex | O(1) | O(V²) rebuild | O(1) | rebuild |
| Cache behavior | pointer-chasing | dense, predictable | streaming | **best** |

> The two bolded rows are why adjacency lists win for traversal: BFS/DFS iterate
> neighbors, and the total work is Σ deg(v) = 2E (undirected) or E (directed) —
> exactly the O(V+E) that makes graph algorithms fast. On a matrix the same
> traversal pays O(V) per vertex = O(V²) regardless of how few edges exist.

---

## Why "O(V+E)" Is the Magic Number

Both BFS and DFS visit each vertex once and each edge once. On an adjacency list:

```
  total neighbor-iteration work
    = sum over all v of  deg(v)
    = 2E   (undirected)   or   E   (directed)

  plus O(V) to touch every vertex once (even isolated ones)

    => O(V + E)
```

On a matrix you cannot do better than scanning a full row per vertex:

```
  total work = sum over all v of V  =  V * V  =  O(V^2)
```

So the *same algorithm* is O(V+E) or O(V²) purely by representation. For a social
graph with V = 10^9 and average degree 200 (E ≈ 2×10^11), the list is ~200 GB of
edges; the matrix is 10^18 entries — physically impossible. **Sparse graphs
mandate sparse representations.** This is the single most consequential choice in
the field.

---

## CSR — The Production Representation

Compressed Sparse Row (CSR, a.k.a. Compressed Row Storage) is what serious graph
engines actually use: GraphBLAS, most GNN frameworks, sparse linear-algebra
libraries (`numerical-methods/`), and high-performance BFS all run on CSR. It is
an adjacency list flattened into two contiguous arrays.

```
  Adjacency list:                 CSR (two flat arrays):
    0 -> [1, 2]                      row_ptr = [0, 2, 3, 3, 4]   (length V+1)
    1 -> [3]                         col_idx = [1, 2, 3, 2]      (length E)
    2 -> []
    3 -> [2]                       neighbors of vertex v:
                                     col_idx[ row_ptr[v] .. row_ptr[v+1] )

                                   deg(v) = row_ptr[v+1] - row_ptr[v]
```

```
   row_ptr index:   0    1    2    3    4
                  +----+----+----+----+----+
                  | 0  | 2  | 3  | 3  | 4  |
                  +----+----+----+----+----+
                    |    |    |    \____\___ vertex 2 and 3 both start..
                    |    |    |               (3==3 => vertex 2 has NO edges)
                    v    v    v
   col_idx:       [ 1 ,  2 ,  3 ,  2 ]
                   \_v0_/  \v1/ \v3/
```

**Why CSR wins:** the neighbor list of every vertex is a *contiguous* slice of one
array, so traversal is a cache-friendly sequential scan with no pointer chasing.
The cost is mutability — adding an edge means rebuilding `row_ptr`/`col_idx`, so
CSR is for *static* graphs (load once, query many times). Weighted graphs add a
parallel `weights[]` array indexed identically to `col_idx`. The mirror form,
**CSC** (compressed sparse *column*), stores in-edges instead of out-edges — you
keep both when you need to walk the graph backward (e.g. Kosaraju's transpose in
`05`, PageRank's incoming links in `08`).

> Old-world bridge: CSR is to graphs what a clustered index is to a table — the
> data is physically ordered for the dominant access pattern (range scan over one
> vertex's neighbors), trading update cost for read locality. Same engineering
> trade you made choosing clustered vs. heap tables in SQL Server.

---

## Directed, Weighted, Multigraphs, and Self-Loops

The representation must encode the *graph class*, and getting this wrong corrupts
every downstream algorithm.

```
  UNDIRECTED edge {u,v}        DIRECTED edge (u,v)
    store BOTH u->v AND v->u     store ONLY u->v
    deg sum = 2E                 out-deg sum = in-deg sum = E
    matrix is SYMMETRIC          matrix need not be symmetric

   u <---> v                     u -----> v
    (one logical edge,            (one edge; reverse may not exist)
     two list entries)

  WEIGHTED                      MULTIGRAPH              SELF-LOOP
    list: (v, w) pairs            multiple u->v edges     edge (v,v)
    matrix: store w not bit       list allows dups        list: v in adj[v]
    matrix: 0 vs INF =            matrix needs a count    matrix: diagonal entry
     "no edge" sentinel matters!   or edge-id, not a bit
```

The classes form an inclusion hierarchy. Each generalization breaks an assumption
some algorithm depends on:

| Class | Generalizes by allowing… | Breaks the assumption that… |
|-------|--------------------------|------------------------------|
| Simple undirected | — (baseline) | — |
| Directed (digraph) | asymmetric edges | reachability is symmetric (now need SCCs, `05`) |
| Weighted | edge costs | all edges are equal (now need Dijkstra, not BFS) |
| Weighted, neg edges | negative costs | Dijkstra's non-negativity invariant (need B-F, `03`) |
| Multigraph | parallel edges | (u,v) is unique — matters for flow & matching |
| With self-loops | (v,v) edges | the diagonal is zero |

> The classic representation bug: storing a weighted matrix with `0` for "no
> edge." Then a legitimate zero-weight edge is indistinguishable from absence, and
> a shortest-path algorithm treats missing edges as free. Use a sentinel (`+∞`
> for shortest-path matrices, a separate boolean for existence) — never overload
> `0`.

---

## The Implicit Graph — When You Never Build It

A huge fraction of real graph algorithms run on a graph that is *never
materialized*. The vertices are states; the edges are generated on demand by a
successor function. This is the dominant pattern in search and planning.

```
  EXPLICIT graph                   IMPLICIT graph
  --------------                   --------------
  adjacency built in memory        successors(state) computed on the fly

  e.g. road network loaded         e.g. chess: vertex = board position,
       into CSR                          edges = legal moves
                                    e.g. Sudoku, puzzle states, build-time
   neighbors(v) = array lookup           dependency expansion

                                    neighbors(v) = successors(v)  [a function]
```

The algorithms (`02`–`03`, A\* especially) don't care: they call
`neighbors(v)` whether it's an array slice or a move generator. This is why a
state-space planner and a road-network router run the *same* Dijkstra/A\* code.
The implicit form is mandatory when the graph is astronomically large (chess has
~10^46 reachable positions) or infinite — you explore only the reachable frontier.

---

## Old World → New World Bridges

| You know it as… | It is a graph representation of… |
|-----------------|----------------------------------|
| SQL self-referencing FK (`manager_id`) + recursive CTE | an adjacency list walked by traversal |
| A relational join table `(left_id, right_id)` | an edge list |
| A bitmap / bitset of reachability | a boolean adjacency matrix row |
| Sparse matrix in MATLAB/SciPy (`csr_matrix`) | literally CSR — same structure |
| An ORM lazy-loading related entities | an implicit graph (successors on demand) |
| `git` storing commits with parent pointers | adjacency list of a DAG (`02`) |

The MATLAB/SciPy bridge is exact, not loose: a graph's adjacency matrix *is* a
sparse matrix, BFS is a sparse matrix-vector product over a boolean semiring, and
this is the entire premise of GraphBLAS and the linear-algebra view in `08`.

---

## Decision Cheat Sheet

| Situation | Use | Reason |
|-----------|-----|--------|
| Sparse graph, lots of traversal | adjacency list / CSR | O(V+E) iteration |
| Static graph, performance-critical | CSR | contiguous, cache-friendly |
| Dense graph (E ≈ V²) | adjacency matrix | O(1) edge query, space already O(V²) |
| Need fast "edge exists?" | adjacency matrix or hash set | O(1) lookup |
| Algorithm iterates all edges (Kruskal) | edge list | O(E) natural form |
| Graph mutates constantly | adjacency list (hash sets) | O(1) add/delete |
| Graph too big / infinite to store | implicit (successor fn) | never materialize |
| Need to walk edges backward | keep CSR + CSC | in-edges in O(deg) |
| Weighted matrix | store weights, **`+∞`** for absent | don't overload `0` |

---

## Common Confusion Points

**"Adjacency matrix is wasteful, never use it."** False for dense graphs and for
algorithms that *want* O(1) edge queries or matrix algebra. Floyd-Warshall (`03`)
is naturally a matrix algorithm; transitive closure is matrix Boolean
multiplication; small dense graphs (V ≤ a few thousand) are fine. The matrix is
wrong specifically for *sparse* graphs and *traversal*.

**"Undirected and directed are basically the same."** They differ structurally.
An undirected edge is two directed half-edges; the moment you need SCCs, topo
sort, or transpose graphs you are in directed-graph territory where reachability
is asymmetric. Storing an undirected graph as a digraph (both directions) is fine;
treating a digraph as undirected silently invents edges.

**"CSR is just an adjacency list."** Conceptually yes, mechanically no. The
flattening into two contiguous arrays is what delivers cache performance and
enables SIMD/GPU traversal — and what costs you O(E) rebuild on mutation. The
distinction matters exactly when performance does.

**"E can be ignored next to V²."** Only for dense graphs. For sparse graphs E is
the *smaller* term and the entire reason O(V+E) beats O(V²). Always carry both V
and E in a bound until you know the density regime; collapsing prematurely is how
wrong complexity bounds creep in.

**"Storing weights as 0 for missing edges is fine."** It is the canonical
representation bug. `0` is a valid weight; absence is not zero cost, it is
infinite cost. Use `+∞` in distance/weight matrices and a separate existence flag
when zero-weight edges are possible.
