---
maxim_schema: maxim.frontmatter.v1
id: maxim:graph-algorithms:np-hard-graphs
kind: guide
module: graph-algorithms
section: mathematics-physics
title: NP-Hard Graph Problems
status: source-custody
source_custody: partial
current_path: graph-algorithms/07-NP-HARD-GRAPHS.md
canonical_path: graph-algorithms/07-NP-HARD-GRAPHS.md
backsource_ids: [proof-backfill:graph-algorithms:07-np-hard-graphs, git-history:graph-algorithms:07-np-hard-graphs]
concepts: [TSP, vertex cover, graph coloring, clique, independent set, reductions, approximation]
root_concepts: [NP-hard graph problems]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---

# NP-Hard Graph Problems — The Cliff and How to Climb It

This is the other side of the field. Everything in `02`–`06` was polynomial; here
the problems are NP-hard, meaning no polynomial algorithm is known and one exists
only if P = NP. For a reader who knows reductions and complexity classes cold, the
value is in the *structure*: which problems reduce to which, how tight the
approximation bounds are, and which special cases escape hardness. The recurring
lesson — already seen with 2-SAT (`05`) and bipartite vertex cover (`06`) — is
that hardness is fragile: a small structural restriction often collapses an
NP-hard problem to P.

```
  THE NP-HARD GRAPH ZOO (and the reductions wiring them together)
  ==============================================================

                3-SAT  (canonical NP-complete, Cook-Levin)
                   |  poly-time reduction
       +-----------+-----------------------+
       v                                   v
   INDEPENDENT SET <==complement==> CLIQUE       VERTEX COVER
   (no two adjacent)  (V \ IS in     (all adjacent)  (= V minus a max
       |               complement)        ^          independent set!)
       |  S is an independent set  <=>  V\S is a vertex cover
       |
       v
   GRAPH COLORING (k-coloring: adjacent vertices differ)
       |   3-coloring is NP-complete; 2-coloring (bipartite) is O(V+E)
       v
   TSP / HAMILTONIAN CYCLE (visit every vertex; min-cost tour)
       Hamiltonicity is NP-complete; metric TSP -> 1.5-approx (Christofides)

   ESCAPES:  approximation | fixed-parameter (FPT in k) | structure (planar/bipartite)
```

**Read the reduction arrows:** independent set, clique, and vertex cover are the
*same problem in three disguises*; coloring and TSP are reached by further
reductions. The bottom row lists the three escape hatches.

---

## The Three Faces of One Problem

Independent set, clique, and vertex cover are tightly interlinked by two exact
identities — internalize these, and three "different" NP-hard problems become one.

```
  Graph G:                Complement G':           Identities (on V vertices):
                                                   ---------------------------------
    A --- B               A     B  (A-B gone)      S is an INDEPENDENT SET in G
    |    /                |                          <=> S is a CLIQUE in G'
    C    D (D isolated)   C --- D (new edges...)   S is an INDEPENDENT SET in G
                                                     <=> V\S is a VERTEX COVER in G
   {C,D} is independent   {edges flip}             so:
   (no edge between)                               max independent set + min vertex
   {A,C} is a vertex                                 cover = V   (exactly)
   cover (covers A-B,
   A-C, ...)
```

| Problem | Asks for | Identity |
|---------|----------|----------|
| **Independent set** | largest set, no two adjacent | complement of a clique in Gᶜ |
| **Clique** | largest set, all pairwise adjacent | independent set in the complement |
| **Vertex cover** | smallest set touching every edge | V minus a maximum independent set |

All three are NP-hard. But their *approximability* differs sharply — and that
asymmetry is the interesting part.

---

## Approximation — How Close Can Polynomial Time Get?

NP-hardness forbids exact polynomial solutions (unless P=NP), but *approximation*
algorithms with provable ratios often exist. The ratios are wildly uneven across
these closely-related problems — a deep fact from PCP theory.

| Problem | Best poly-time approximation | Hardness of approximation |
|---------|------------------------------|---------------------------|
| **Vertex cover** | **2** (greedy on a maximal matching) | no better than ~1.36 unless P=NP; no 2−ε under UGC |
| **Metric TSP** | **1.5** (Christofides) | no PTAS unless P=NP (APX-hard) |
| **General TSP** | **inapproximable** to any constant | NP-hard even to approximate |
| **Independent set** | **no constant factor** | n^(1−ε)-inapproximable |
| **Clique** | no constant factor | n^(1−ε)-inapproximable |
| **Graph coloring** | within O(n^(1−ε)) is hard | very hard to approximate |

```
  THE 2-APPROXIMATION FOR VERTEX COVER (clean, and worth knowing):
    find a MAXIMAL matching M (greedily). Output BOTH endpoints of every M-edge.
      - it's a cover: any uncovered edge could extend M, contradicting maximality
      - it's <= 2*OPT: OPT must include >= 1 endpoint of each matched edge,
        and the matched edges are disjoint, so OPT >= |M|; we output 2|M|.

  CHRISTOFIDES FOR METRIC TSP (1.5-approx; requires triangle inequality):
    1. build an MST (04)              2. min-weight matching on ODD-degree MST vertices
    3. Eulerian circuit on MST+matching   4. shortcut repeats (triangle ineq. ensures
                                             shortcutting never increases cost)
    => tour <= 1.5 * OPT
```

> **The metric precondition is load-bearing.** Christofides' 1.5 guarantee
> *requires the triangle inequality* (w(u,w) ≤ w(u,v)+w(v,w)) — without it,
> shortcutting can increase cost and the bound collapses. General TSP (arbitrary
> weights) is inapproximable to *any* constant unless P=NP (a tour-approximator
> would solve Hamiltonian cycle exactly). Always state whether you're in the
> metric case. *(Note: in 2021 Karlin-Klein-Oveis Gharan beat 1.5 by ~10⁻³⁶ for
> metric TSP — historically important, practically Christofides is still the
> reference.)*

> The independent-set vs vertex-cover asymmetry is striking: they're complementary
> (IS + VC = V), yet vertex cover has a 2-approx while independent set has *no
> constant-factor* approximation. The reason: a small additive error in a *small*
> optimum (vertex cover) is a small ratio, but the same additive error in a
> *large* optimum's complement (independent set) is catastrophic. Complementary
> problems need not be equally approximable.

---

## When Hardness Evaporates — The Escape Hatches

The single most useful practical fact: NP-hardness is a *worst-case, general-graph*
statement. Restrict the structure and the problem often becomes polynomial.

```
  PROBLEM            HARD ON...           BUT EASY (poly) ON...
  -------            ---------            ---------------------
  Vertex cover       general graphs       BIPARTITE (Konig, 06): = max matching
  Graph coloring     general (3-color NP) BIPARTITE = 2-colorable: O(V+E) BFS test
  Coloring           general              PLANAR: 4-colorable (4-color theorem);
                                            5-coloring is poly-constructive
  Independent set    general              TREES/bipartite: poly via DP/matching
  TSP                general (inapprox.)   METRIC: 1.5-approx; EUCLIDEAN: PTAS (Arora)
  SAT                3-SAT (NP-complete)   2-SAT: O(V+E) via SCC (05); Horn: linear
  Max-cut            general (NP-hard)     PLANAR: poly-time
```

This table is the punchline of the whole NP-hard story for a practitioner: **find
the structure.** Real instances are rarely worst-case general graphs — they're
planar (maps, circuits), bipartite (assignment), bounded-degree, or low-treewidth
(`09`). The escape is usually a property of *your* graph, not a better algorithm
for the abstract problem.

### Fixed-Parameter Tractability (FPT)

A second escape: confine the exponential blow-up to a *parameter* k (e.g. the
solution size), not the input size n.

```
  Vertex cover of size <= k:   solvable in O(2^k * (V+E))   -- FPT in k
    branch: for each edge, one endpoint MUST be in the cover. Pick one,
    recurse with k-1. Depth-k binary tree => 2^k leaves, each O(V+E).
    For small k (say k <= 40) this beats brute force enormously, even on big graphs.
```

When the *answer* is small (a few critical nodes), FPT turns "NP-hard" into "fast
in practice." This underlies kernelization and modern exact solvers.

---

## Old World → New World Bridges

| You know it as… | It is the NP-hard problem… |
|-----------------|----------------------------|
| Register allocation in a compiler | graph coloring (interference graph) — `computing/22` |
| Wireless channel / frequency assignment | graph coloring |
| Exam / room scheduling with conflicts | coloring / independent set |
| Selecting non-conflicting features/jobs | maximum independent set |
| Minimum monitors to watch every link | minimum vertex cover |
| Vehicle routing / delivery tour | TSP (with capacity ⇒ VRP, harder still) |
| Package dependency conflict resolution | SAT (general) — why npm/NuGet resolution is hard |
| Finding tight communities in a network | clique / dense-subgraph |

The register-allocation bridge is the canonical one for a compiler-literate
reader: the interference graph (variables alive simultaneously) is colored with k
= number of registers; uncolorable ⇒ spill to memory. Chaitin's allocator is
graph coloring with heuristics, exactly because optimal coloring is NP-hard.

---

## Decision Cheat Sheet

| Situation | Approach | Guarantee |
|-----------|----------|-----------|
| Vertex cover, need a fast answer | greedy on maximal matching | 2-approx |
| Vertex cover, answer is small (k) | FPT branching | exact, O(2ᵏ·(V+E)) |
| Vertex cover on a bipartite graph | König ⇒ max matching (`06`) | **exact, poly** |
| Metric TSP (triangle inequality) | Christofides | 1.5-approx |
| Euclidean TSP | Arora/Mitchell PTAS | (1+ε)-approx |
| General TSP (arbitrary weights) | heuristics (2-opt, LK) | **no constant guarantee** |
| Graph coloring, general | greedy / DSATUR heuristic | no good guarantee |
| Is it 2-colorable? | BFS bipartite test (`02`) | exact, O(V+E) |
| Coloring a planar graph | 5/4-color theorems | ≤ 4 colors guaranteed |
| Max independent set, tree/bipartite | DP / matching | exact, poly |
| Max independent set, general | branch-and-bound / heuristic | no constant approx |
| Any NP-hard graph problem | **first check the structure** | planar/bipartite/small-k may be poly |

---

## Common Confusion Points

**"NP-hard means no algorithm exists."** It means no *polynomial* algorithm is
known (and none exists unless P=NP). Exact exponential algorithms always exist
(brute force); FPT algorithms are exact and fast when a parameter is small;
approximation algorithms run in polynomial time with a provable error bound. "NP-
hard" constrains *worst-case polynomial exactness*, nothing more.

**"All NP-hard problems are equally hard to approximate."** Emphatically false,
and it's one of the deepest results in the area. Vertex cover has a 2-approx;
independent set (its complement!) has no constant-factor approximation; metric TSP
has 1.5 but general TSP has none. Approximability is a finer classification than
NP-hardness — two NP-hard problems can sit at opposite ends of it.

**"Christofides gives 1.5 for any TSP."** Only for **metric** TSP — the triangle
inequality is required for the shortcutting step to not increase cost. On general
(non-metric) TSP there is *no* constant-factor approximation unless P=NP. Quoting
"1.5-approx" without the metric precondition is a classic precision error.

**"2-coloring and 3-coloring are similar in difficulty."** They straddle the
complexity cliff. 2-coloring = bipartiteness testing = O(V+E) BFS (`02`).
3-coloring is NP-complete. One extra color flips the problem from linear to
intractable — the graph-coloring analogue of the 2-SAT/3-SAT jump in `05`.

**"Vertex cover is hard, so monitoring a bipartite network is hard."** No — on
bipartite graphs minimum vertex cover equals maximum matching (König, `06`), hence
polynomial. Always check whether your real graph has exploitable structure before
accepting the general-case hardness verdict. The structure usually *is* there.
