# Combinatorics and Graph Theory — Complete Reference

## The Big Picture

```
COMBINATORICS & GRAPH THEORY
═══════════════════════════════════════════════════════════════════════════

  COUNTING                    GRAPH THEORY                  EXTREMAL / RAMSEY
  ─────────                   ────────────                  ─────────────────
  Basic counting principles   Graphs, digraphs              Turán theorem
  Permutations, combinations  Trees, spanning trees         Ramsey R(s,t)
  Multinomials                Eulerian / Hamiltonian        Szemerédi regularity
  Inclusion-exclusion         Planarity, graph coloring     Probabilistic method
  Pigeonhole principle        Matching, Hall's theorem      Extremal graph theory

  GENERATING FUNCTIONS        ALGEBRAIC COMBINATORICS       ALGORITHMS ON GRAPHS
  ────────────────────        ───────────────────────       ────────────────────
  OGFs (ordinary)             Chromatic polynomial          BFS / DFS
  EGFs (exponential)          Möbius inversion (posets)     Shortest paths
  Formal power series         Polya's enumeration theorem   MST (Kruskal/Prim)
  Transfer matrix method      Burnside's lemma              Network flow (max-flow)
  Analytic combinatorics      Symmetric functions           NP-hard classics

  ┌─────────────────────────────────────────────────────────────────────┐
  │  Core theme: counting discrete structures + understanding their     │
  │  connectivity, coloring, and global properties                      │
  └─────────────────────────────────────────────────────────────────────┘
```

**Why it matters for a VP/engineer**: Graph algorithms are everywhere — dependency
resolution (DAG topological sort), network routing (shortest paths), scheduling
(graph coloring), ML (GNNs, knowledge graphs), distributed systems (consensus as
graph reachability), and compiler design (SSA, control flow graphs). Generating
functions are the "transfer function" of combinatorics — same calculus-based
machinery you know from Laplace, applied to counting.

---

## 1. Counting Fundamentals

### 1.1 The Basic Principles

```
RULE OF PRODUCT: |A × B| = |A| · |B|
  "Do A in m ways AND B in n ways → m·n total"
  Generalization: |A₁ × A₂ × ⋯ × Aₖ| = |A₁| · |A₂| · ⋯ · |Aₖ|

RULE OF SUM: |A ∪ B| = |A| + |B|   when A ∩ B = ∅
  "Do A in m ways OR B in n ways → m+n total"
  Generalization: |A₁ ∪ A₂ ∪ ⋯| = Σ|Aᵢ|   (pairwise disjoint)

BIJECTION PRINCIPLE: |A| = |B| iff there exists a bijection f: A → B
  Proof technique: construct an explicit bijection rather than counting directly.
  Classic example: binary strings of length n ↔ subsets of [n]
```

### 1.2 Permutations and Combinations

```
ARRANGEMENTS (ORDER MATTERS):
  n objects, all distinct:                     n! = n·(n-1)·⋯·1
  Choose r of n, order matters (r-perm):       P(n,r) = n!/(n-r)!
  Permutations with repetition (multiset):     n!/(n₁! n₂! ⋯ nₖ!)

SELECTIONS (ORDER DOESN'T MATTER):
  Choose r from n (binomial coefficient):      C(n,r) = n!/(r!(n-r)!) = (n choose r)
  Stars and bars (r objects into n bins):      C(n+r-1, r)

KEY IDENTITIES:
  Pascal's rule:        C(n,k) = C(n-1,k-1) + C(n-1,k)
  Symmetry:             C(n,k) = C(n,n-k)
  Vandermonde's:        Σₖ C(m,k)·C(n,r-k) = C(m+n,r)
  Binomial theorem:     (x+y)ⁿ = Σₖ C(n,k) xᵏ yⁿ⁻ᵏ
  Sum of row:           Σₖ C(n,k) = 2ⁿ
  Absorption identity:  k·C(n,k) = n·C(n-1,k-1)
  Hockey stick:         Σᵢ₌₀ʳ C(n+i, i) = C(n+r+1, r)
```

### 1.3 Inclusion-Exclusion Principle (IEP)

The IEP is the fundamental overcounting correction:

```
|A₁ ∪ A₂ ∪ ⋯ ∪ Aₙ| = Σ|Aᵢ| − Σ|Aᵢ∩Aⱼ| + Σ|Aᵢ∩Aⱼ∩Aₖ| − ⋯

Formal: = Σ_{∅≠S⊆[n]} (−1)^(|S|+1) |∩ᵢ∈S Aᵢ|
```

**Canonical applications**:

| Problem | What Aᵢ represents | Answer uses |
|---------|-------------------|-------------|
| Surjections from [n] to [k] | f misses output i | k! · Σ(-1)ʲ C(k,j)(k-j)ⁿ/k! |
| Derangements D(n) | permutation fixes i | n!·Σ(-1)ᵏ/k! ≈ n!/e |
| Euler's totient φ(n) | integers divisible by pᵢ | n·Π(1−1/pᵢ) |
| Problème des ménages | couples sit adjacent | — |

**Derangement formula** (no fixed points):
```
D(n) = n! · Σₖ₌₀ⁿ (−1)ᵏ/k!   →   lim D(n)/n! = 1/e ≈ 0.368

D(n) = (n−1)[D(n−1) + D(n−2)]   (recurrence)
```

### 1.4 Pigeonhole Principle

```
BASIC: n+1 objects → n boxes ⟹ some box has ≥ 2 objects.

GENERALIZED: m objects → n boxes ⟹ some box has ≥ ⌈m/n⌉ objects.

NON-OBVIOUS APPLICATIONS:
  • Among any 5 points in a unit square, two are within √2/2 distance
  • In any sequence of mn+1 reals, there's a monotone subsequence of length n+1
    (Erdős-Szekeres theorem — uses pigeonhole on (LIS length, LDS length) pairs)
  • Among n+1 integers from {1,...,2n}, some divides another
  • Every sequence of n² + 1 distinct reals has monotone subsequence of length n+1
```

### 1.5 Multinomial Coefficients

```
(x₁ + x₂ + ⋯ + xₖ)ⁿ = Σ_{n₁+⋯+nₖ=n} (n choose n₁,n₂,...,nₖ) x₁^n₁⋯xₖ^nₖ

Multinomial coefficient: n!/(n₁!n₂!⋯nₖ!)   where Σnᵢ = n

Number of ways to partition n objects into groups of sizes n₁,...,nₖ.
```

---

## 2. Generating Functions

Generating functions convert combinatorial recurrences into algebraic manipulations.
The **mental model**: sequences ↔ formal power series — same as z-transforms for
counting.

### 2.1 Ordinary Generating Functions (OGFs)

```
OGF of sequence (a₀, a₁, a₂, ...):   A(x) = Σₙ aₙ xⁿ

DICTIONARY OF OGFs:
  aₙ = 1:                  1/(1−x)          = 1 + x + x² + ⋯
  aₙ = C(n,k):             xᵏ/(1−x)^(k+1)
  aₙ = Fibonacci:          x/(1−x−x²)
  aₙ = Catalan Cₙ:         (1−√(1−4x))/(2x)
  aₙ = n:                  x/(1−x)²
  aₙ = nᵏ:                 x·D[x·D[⋯1/(1−x)]]   (k Euler operators)

OPERATIONS:
  Shift right (aₙ₋₁):     x·A(x)
  Sum prefix (Σₖ₌₀ⁿaₖ):   A(x)/(1−x)
  Convolution (Σₖ aₖbₙ₋ₖ): A(x)·B(x)
  Hadamard product:         ∮ A(t)·B(x/t) dt/(2πit)
```

**Solving recurrences with OGFs**:
```
Fibonacci: fₙ = fₙ₋₁ + fₙ₋₂,  f₀=0, f₁=1

F(x) = x + x·F(x) + x²·F(x)
F(x)(1−x−x²) = x
F(x) = x/(1−x−x²)

Partial fractions → closed form Binet formula:
  fₙ = (φⁿ − ψⁿ)/√5   where φ=(1+√5)/2, ψ=(1−√5)/2
```

### 2.2 Exponential Generating Functions (EGFs)

```
EGF: Â(x) = Σₙ aₙ xⁿ/n!

Use EGFs when aₙ counts labeled structures (permutations, functions, etc.)
Rule: EGF of convolution Σₖ C(n,k)aₖbₙ₋ₖ   =   Â(x)·B̂(x)

DICTIONARY OF EGFs:
  aₙ = 1:              eˣ              = Σ xⁿ/n!
  aₙ = n!:             1/(1−x)         (derangement connection)
  aₙ = D(n):           e⁻ˣ/(1−x)
  aₙ = Bell Bₙ:        e^(eˣ−1)        (partitions of [n])
  aₙ = Stir2(n,k)·k!:  (eˣ−1)ᵏ/k!     (surjections to k-element set)
  aₙ = nⁿ (rooted labeled trees): x·e^(x·nⁿ⁻¹)
```

**Labeled vs. unlabeled**: OGF for unlabeled, EGF for labeled. Bell numbers Bₙ
(number of set partitions of [n]): B₀=1, B₁=1, B₂=2, B₃=5, B₄=15, B₅=52.

### 2.3 Transfer Matrix Method

For counting paths/words in automata/graphs:

```
Count paths of length n in graph G:
  Let A = adjacency matrix.
  [Aⁿ]ᵢⱼ = number of walks of length n from i to j.

Generating function for total walks: Σₙ (1ᵀAⁿ1) xⁿ = 1ᵀ(I − xA)⁻¹1

For regular languages: DFA has k states → transfer matrix k×k
  Rational generating function ⟺ regular language
```

### 2.4 Catalan Numbers

```
Cₙ = C(2n,n)/(n+1) = C(2n,n) − C(2n,n+1)

C₀=1, C₁=1, C₂=2, C₃=5, C₄=14, C₅=42, C₆=132

OGF: C(x) = (1 − √(1−4x))/(2x)
Recurrence: Cₙ₊₁ = Σₖ₌₀ⁿ Cₖ Cₙ₋ₖ

ALL COUNT THE SAME Cₙ THINGS (Catalan family):
  • Triangulations of (n+2)-gon
  • Full binary trees with n+1 leaves
  • Valid parenthesizations of n+1 factors
  • Paths below diagonal: lattice from (0,0) to (2n,0) not crossing x-axis
  • Stack-sortable permutations of [n] (avoiding 231)
  • Monotone paths in n×n grid not crossing diagonal
```

### 2.5 Analytic Combinatorics — Extracting Asymptotics from Singularities

The **Flajolet-Sedgewick framework** (from their 2009 book *Analytic Combinatorics*)
gives a systematic way to extract asymptotic coefficients from generating functions
via complex analysis — turning the OGF into an asymptotic formula for aₙ.

**Core principle**: the dominant singularity of A(x) closest to the origin controls
the exponential growth rate of aₙ.

```
SINGULARITY TYPE → ASYMPTOTICS:

A(x) has a simple pole at x = ρ:
  aₙ ~ C · ρ⁻ⁿ            (exponential growth only)

A(x) has algebraic singularity (x=ρ)^α at x = ρ:
  aₙ ~ C · ρ⁻ⁿ · n^{−α−1} (exponential × polynomial correction)

A(x) = P(x)/√(1 − x/ρ):
  aₙ ~ C · ρ⁻ⁿ · n^{−1/2} (typical for Catalan-type)

A(x) = P(x)(1 − x/ρ)^{3/2}:
  aₙ ~ C · ρ⁻ⁿ · n^{−5/2} (typical for plane trees, maps)
```

**Transfer theorems** (singularity analysis): for A(x) with algebraic singularity
at ρ of the form A(x) ~ Σ cₖ (1 − x/ρ)^{αₖ} near x = ρ, the coefficients satisfy:
```
[xⁿ] A(x) ~ Σ cₖ · ρ⁻ⁿ · n^{−αₖ−1} / Γ(−αₖ)
```
This requires the singularity to be isolated in its Δ-domain (a domain wider than
the disk of convergence, like a "dented disk").

**Examples — automatic asymptotics**:
```
Catalan Cₙ: OGF = (1 − √(1−4x))/(2x), singularity at x = 1/4.
  Near x = 1/4: C(x) ~ 1 − √(1−4x)/2 + ... (algebraic, exponent 1/2)
  → Cₙ ~ 4ⁿ / (n^{3/2} √π)

Ballot numbers, Non-crossing partitions, Planar maps:
  All have the n^{-3/2} correction → square-root singularity structure

Labeled trees (nⁿ⁻²): EGF T(x) = xeᵀ⁽ˣ⁾ (Lambert W equation)
  Singularity at x = 1/e: T(x) near 1/e involves √(1 − ex)
  → nⁿ⁻² ~ √(2π) · n^{n−1/2} eˉⁿ  (Stirling refinement of Cayley)
```

**Saddle-point method**: for EGFs with entire (no finite singularity) generating
functions, the dominant contribution to aₙ = n! [xⁿ] Â(x) comes from the saddle
point of the integrand in the Cauchy integral formula. Used for analyzing
permutations, derangements, set partitions (Bell numbers).

**Algorithmic significance**: these asymptotics give the average-case complexity of
algorithms on random combinatorial structures — random binary search trees have
average depth Θ(log n) with exactly the right constant (2 ln n), derivable from the
EGF singularity structure.

---

## 3. Graph Theory Fundamentals

### 3.1 Definitions and Vocabulary

```
GRAPH G = (V, E)
  V: vertices (nodes)
  E ⊆ V×V: edges

Variants:
  Simple graph:    no self-loops, no multi-edges
  Multigraph:      multiple edges allowed
  Directed (digraph): edges (u,v) ≠ (v,u)
  Weighted:        w: E → ℝ

KEY PARAMETERS:
  n = |V|  (order of G)
  m = |E|  (size of G)
  deg(v) = degree of vertex v
  Handshaking lemma: Σᵥ deg(v) = 2m   (even number of odd-degree vertices)
  δ(G) = min degree,  Δ(G) = max degree

ADJACENCY MATRIX A:   Aᵢⱼ = 1 if (i,j) ∈ E
INCIDENCE MATRIX B:   Bᵢₑ = ±1 for endpoint of edge e
LAPLACIAN L = D − A:  D = degree diagonal matrix
  Properties: L is positive semi-definite, smallest eigenvalue = 0 (constant vector)
  Second eigenvalue λ₂ = algebraic connectivity (Fiedler value)
```

### 3.2 Graph Families and Notation

| Notation | Graph | Properties |
|----------|-------|------------|
| Kₙ | Complete graph | n(n-1)/2 edges, (n-1)-regular |
| Kₘ,ₙ | Complete bipartite | Bipartite, mn edges |
| Cₙ | Cycle | 2-regular, n edges |
| Pₙ | Path | n-1 edges |
| Qₙ | n-cube | 2ⁿ vertices, n-regular, bipartite |
| Wₙ | Wheel | Cₙ + hub, planar if n ≤ 4 |
| Petersen | Famous 3-regular | Non-Hamiltonian, non-planar, 10 vertices |

### 3.3 Connectivity

```
PATH: sequence v₀,e₁,v₁,e₂,...,vₖ  (allow repeated vertices)
WALK: same but edge distinct
TRAIL: edges distinct, vertices may repeat
CYCLE: closed walk, edge distinct, v₀=vₖ
SIMPLE PATH/CYCLE: vertices also distinct

CONNECTIVITY:
  Connected: path between every pair
  k-connected: removing any k-1 vertices leaves it connected
  κ(G) = vertex connectivity = min cut size
  λ(G) = edge connectivity ≤ κ(G) ≤ δ(G)   (Whitney's theorem)

MENGER'S THEOREM: max vertex-disjoint paths from s to t = min vertex cut separating s,t
  (Equivalently via max-flow min-cut: max-flow = min-cut)

STRONGLY CONNECTED (digraph): path from every u to every v
  SCCs computed by Kosaraju's or Tarjan's algorithm in O(V+E)
```

### 3.4 Trees

```
TREE: connected graph with n vertices and n-1 edges.
Equivalent conditions — any one implies all:
  (1) Connected, n-1 edges
  (2) Acyclic, n-1 edges
  (3) Connected, acyclic (forest)
  (4) Unique path between every pair of vertices
  (5) Minimally connected (removing any edge disconnects)
  (6) Maximally acyclic (adding any edge creates cycle)

FOREST: disjoint union of trees (k components → n-k edges)

CAYLEY'S FORMULA: number of labeled trees on [n] vertices = nⁿ⁻²
  Proof by Prüfer sequence: bijection {labeled trees on [n]} ↔ sequences in [n]^(n-2)

SPANNING TREE: tree subgraph visiting all n vertices
  Every connected graph has a spanning tree.
  Number of spanning trees = any cofactor of Laplacian L (Matrix-Tree Theorem)
  # spanning trees = (1/n) · λ₁λ₂⋯λₙ₋₁   (product of nonzero Laplacian eigenvalues)

ROOTED TREES: one vertex designated root; parent/child relationship
  Height h, depth of vertex v
  Binary tree: each node ≤ 2 children
  Full binary tree: each internal node has exactly 2 children
  Complete binary tree: all levels full except possibly last (heap-shaped)

TREE TRAVERSALS: pre-order (root,L,R), in-order (L,root,R), post-order (L,R,root)
```

---

## 4. Spanning Trees and Minimum Spanning Trees

### 4.1 Spanning Tree Algorithms

```
BFS SPANNING TREE:
  Run BFS from source → BFS tree = tree of shortest (hop-count) paths
  O(V+E) time

DFS SPANNING TREE:
  Back edges → cycles;  Tree edges form DFS tree
  DFS numbers, finish times → topological sort, SCCs
  O(V+E) time

MST — MINIMUM SPANNING TREE:
  Minimum weight spanning tree of weighted graph.

KRUSKAL'S ALGORITHM:  O(E log E)
  Sort edges by weight.
  Greedily add edge if it doesn't create cycle (use Union-Find/DSU).

PRIM'S ALGORITHM:  O(E log V) with binary heap, O(E + V log V) with Fibonacci heap
  Start from any vertex. Maintain priority queue of min-weight edges crossing cut.
  Add cheapest edge, expand frontier.

CUT PROPERTY (correctness proof):
  For any partition (S, V\S), the minimum weight edge crossing the cut is in SOME MST.

CYCLE PROPERTY:
  The maximum weight edge in any cycle is NOT in any MST (if weights distinct).
```

### 4.2 Matroid Theory View of MST

```
GRAPHIC MATROID:
  Ground set E(G), independent sets = forests (acyclic subgraphs)
  Matroid axioms hold: (I1) ∅ independent, (I2) hereditary, (I3) exchange property

Any greedy algorithm on a matroid returns the optimal basis.
MST = greedy on graphic matroid ← explains why Kruskal/Prim work.

MATROID UNION/INTERSECTION: generalizes matching, arboricity.
  k-arboricity: min number of forests covering all edges (Nash-Williams theorem)
```

---

## 5. Graph Traversal Algorithms

```
BREADTH-FIRST SEARCH (BFS):
  Uses queue (FIFO). Explores in layers.
  Computes: shortest paths (unweighted), bipartiteness test, connected components.
  O(V+E) time and space.

DEPTH-FIRST SEARCH (DFS):
  Uses stack (or recursion). Explores as deep as possible first.
  Classifies edges: tree, back (→ cycle), forward, cross (in directed graphs only)
  Computes: topological sort (reverse finish order in DAG), SCCs, bridges, cut vertices
  O(V+E) time.

DFS EDGE CLASSIFICATION (undirected):
  Tree edge:  first time visiting neighbor
  Back edge:  neighbor is ancestor (u,v) with dfs_num[v] < dfs_num[u]
  No forward/cross edges in undirected DFS

TOPOLOGICAL SORT (DAG only):
  Kahn's: BFS starting from all zero in-degree nodes.
  DFS: output nodes in reverse finish time order.
  Application: build systems (make, Maven, npm), compiler scheduling, task ordering.
```

---

## 6. Shortest Paths

```
DIJKSTRA'S ALGORITHM:  O((V+E) log V) with binary heap
  Non-negative weights only. Priority queue, expand minimum-distance node.

BELLMAN-FORD:  O(VE)
  Allows negative weights, detects negative cycles.
  Relax all edges V-1 times. A Vth pass that relaxes → negative cycle.

FLOYD-WARSHALL (all-pairs):  O(V³)
  dp[k][i][j] = shortest i→j using only vertices {1,...,k} as intermediates.
  Transitive closure (Boolean) same recurrence.

JOHNSON'S (all-pairs, sparse):  O(VE + V² log V)
  Reweight using Bellman-Ford to make all edges non-negative, then Dijkstra from each.

A* (heuristic):  Dijkstra with admissible heuristic h(v) ≤ actual distance to target.
  Expands nodes in order of f(v) = g(v) + h(v). Optimal if h is admissible.
```

---

## 7. Network Flow

### 7.1 Max-Flow / Min-Cut

```
FLOW NETWORK: directed graph G=(V,E), source s, sink t, capacity c(e) ≥ 0.

FLOW: f: E → ℝ satisfying:
  Capacity: f(e) ≤ c(e)
  Conservation: Σ f(in) = Σ f(out) for all v ≠ s,t

MAX-FLOW MIN-CUT THEOREM (Ford-Fulkerson 1956):
  max flow value = min s-t cut capacity

  s-t CUT: partition (S,T) with s∈S, t∈T; capacity = Σ c(u,v) for u∈S, v∈T.

FORD-FULKERSON METHOD:
  While augmenting path exists in residual graph Gf:
    Push flow along path, update residual capacities.
  O(max_flow · E)  — can be infinite with irrational capacities!

EDMONDS-KARP (BFS augmenting paths): O(VE²)
DINIC'S ALGORITHM (blocking flows in level graph): O(V²E)
  Unit capacities: O(E·√V)  ← bipartite matching time!

RESIDUAL GRAPH Gf:
  For edge (u,v) with f(u,v) < c(u,v): forward edge with residual c-f
  For edge (u,v) with f(u,v) > 0: backward edge with residual f
```

### 7.2 Reductions to Max-Flow

```
BIPARTITE MATCHING (König's theorem):
  Max matching = Min vertex cover in bipartite graphs
  Reduce: s→left, left→right (capacity 1), right→t. Max-flow = max matching.
  O(E√V) with Hopcroft-Karp.

HALL'S THEOREM (perfect matching):
  Bipartite G=(L∪R, E) has perfect matching iff |N(S)| ≥ |S| for all S ⊆ L.
  "Every set of women knows enough men."

CIRCULATION WITH DEMANDS:
  Lower bound l(e) ≤ f(e) ≤ u(e). Reduce to standard max-flow.

MINIMUM COST FLOW:
  Minimize Σ cost(e)·f(e) subject to flow constraints.
  SSP (successive shortest paths), cycle-canceling algorithms.
```

---

## 8. Eulerian and Hamiltonian Graphs

```
EULERIAN CIRCUIT: visits every EDGE exactly once, returns to start.
EULERIAN PATH: visits every edge exactly once, may start ≠ end.

EULER'S THEOREM:
  Undirected: Eulerian circuit ↔ connected + all vertices even degree
              Eulerian path (s to t) ↔ connected + exactly 2 odd-degree vertices
  Directed: Eulerian circuit ↔ strongly connected + in-degree = out-degree ∀v
            Eulerian path ↔ connected + one vertex (in+1=out) + one (out+1=in), rest equal

  Algorithm: Hierholzer's O(E) — grow tour greedily, stitch subcircuits.

HAMILTONIAN CYCLE: visits every VERTEX exactly once, returns to start.
  NP-hard to decide (vs. Euler which is poly-time).
  No clean characterization known.

DIRAC'S THEOREM (sufficient condition):
  If n ≥ 3 and δ(G) ≥ n/2, then G is Hamiltonian.

ORE'S THEOREM:
  If deg(u) + deg(v) ≥ n for every non-adjacent pair u,v, then G is Hamiltonian.

TSP (Traveling Salesman Problem):
  Find minimum-weight Hamiltonian cycle.
  NP-hard in general. 3/2-approximation (Christofides, 1976).
  Metric TSP: Christofides → now improved to (3/2−ε) by Karlin-Klein-Oveis Gharan 2021.
```

---

## 9. Graph Coloring

### 9.1 Vertex Coloring

```
PROPER k-COLORING: assign colors from [k] to vertices so no two adjacent share a color.
χ(G) = chromatic number = minimum k needed.

BASIC FACTS:
  χ(G) ≥ ω(G)           clique number (lower bound)
  χ(G) ≤ Δ(G) + 1       greedy upper bound (Welsh-Powell)
  χ(G) ≤ Δ(G)            Brooks' theorem (unless Kₙ or odd cycle)

FOUR COLOR THEOREM (1976, Appel-Haken): χ(G) ≤ 4 for any planar graph.
FIVE COLOR THEOREM: Simpler proof.
TWO COLORS ↔ BIPARTITE: χ(G) = 2 iff G has no odd cycle.
THREE COLORING: NP-hard to decide if χ(G) ≤ 3.

GRAPH COLORING ALGORITHM (greedy):
  Order vertices v₁,...,vₙ. Assign smallest available color.
  Uses at most Δ+1 colors. Optimal order → degeneracy d → χ ≤ d+1.

CHROMATIC POLYNOMIAL P(G,k):
  Number of proper k-colorings as polynomial in k.
  Deletion-contraction: P(G,k) = P(G−e, k) − P(G/e, k)
  Evaluations: P(G,0)=0, P(G,1)=0 (if edges), P(G,2)=0 iff non-bipartite
```

### 9.2 Edge Coloring

```
EDGE COLORING (proper): no two edges sharing a vertex get same color.
χ'(G) = edge chromatic number = min edge colors needed.

VIZING'S THEOREM:
  Δ(G) ≤ χ'(G) ≤ Δ(G) + 1
  Class 1 (= Δ) or Class 2 (= Δ+1). All bipartite graphs are Class 1.

Connection to timetabling, scheduling (bipartite = feasible assignment).
```

### 9.3 List Coloring and Choosability

```
LIST COLORING: each vertex v has list L(v) of allowed colors.
ch(G) = choosability = min k such that G is k-choosable from any lists of size k.

LIST COLORING CONJECTURE (proved for bipartite):
  χ'(G) = ch'(G)   (edge choosability = edge chromatic number)

Planar graphs: ch(G) ≤ 5 (Thomassen), and planar + no triangle ≤ 4.
```

---

## 10. Planarity

### 10.1 Planar Graphs

```
PLANAR GRAPH: can be drawn in the plane with no edge crossings.

EULER'S FORMULA: V − E + F = 2   (connected planar graph)
  V = vertices, E = edges, F = faces (including unbounded outer face)

CONSEQUENCES:
  E ≤ 3V − 6             (planar simple graph, V≥3)
  E ≤ 2V − 4             (triangle-free planar, V≥3)
  δ(G) ≤ 5 for planar G  → inductive 6-coloring proof

KURATOWSKI'S THEOREM:
  G is planar ↔ G contains no subdivision of K₅ or K₃,₃
  (subdivision = replace edge by path)

WAGNER'S THEOREM:
  G is planar ↔ G has no K₅ or K₃,₃ as a MINOR
  (minor = edge contraction / deletion)

PLANARITY TESTING: O(V) — Hopcroft-Tarjan algorithm (LR planarity).
```

### 10.2 Graph Minors and Robertson-Seymour

```
GRAPH MINOR: H is a minor of G if H is obtained from G by edge/vertex deletions + contractions.

ROBERTSON-SEYMOUR THEOREM (2004): graphs are well-quasi-ordered by minor relation.
  Consequence: every minor-closed property (planarity, bounded treewidth, etc.)
  is decidable — characterized by finitely many forbidden minors.

TREEWIDTH: planarity = tw ≤ 2 in some sense; many NP-hard problems poly-time on bounded tw.
HADWIGER'S CONJECTURE (open): χ(G) ≥ k → G has Kₖ as minor.
```

---

## 11. Trees and Special Structures

### 11.1 Tree Decomposition and Treewidth

```
TREEWIDTH tw(G):
  Measure of "how tree-like" G is.
  Trees: tw=1. Cycles: tw=2. Kₙ: tw=n-1.

TREE DECOMPOSITION: pair (T, {Xᵢ}) where T is tree, Xᵢ ⊆ V (bags) such that:
  (1) ∪Xᵢ = V
  (2) For each edge (u,v)∈G, ∃i: u,v ∈ Xᵢ
  (3) For each v: {i | v ∈ Xᵢ} is connected subtree of T
  tw(G) = min over decompositions of (max bag size − 1)

APPLICATIONS:
  Many NP-hard problems (independent set, coloring, Hamiltonian) poly-time if tw ≤ k.
  Cholesky fill-in ~ treewidth (sparse matrix methods).
  Message passing on graphical models (belief propagation) exact for trees → junction tree for DAGs.
```

### 11.2 Bipartite Graphs

```
BIPARTITE: vertex set 2-partitioned V = L ∪ R, edges only cross.
  Characterization: no odd cycles ↔ 2-colorable.

BIPARTITE MATCHING: maximum matching = max |M| where M ⊆ E, no two edges share vertex.
  König's theorem: max matching = min vertex cover (bipartite only!)
  Hopcroft-Karp: O(E√V) — augmenting paths via BFS layers.

PERFECT MATCHING: |M| = |L| = |R|. Exists iff Hall's condition.

LATIN SQUARES: n×n array, each row/column uses [n] once.
  = edge coloring of Kₙ,ₙ (has perfect matching by Hall's)
```

---

## 12. Ramsey Theory

**Core principle**: complete disorder is impossible — any large enough structure
must contain ordered sub-structure.

### 12.1 Ramsey Numbers

```
GRAPH RAMSEY NUMBER R(s,t):
  Minimum n such that every 2-coloring of edges of Kₙ contains:
    • red Kₛ, or
    • blue Kₜ

KNOWN VALUES:
  R(3,3) = 6         famous: 6 people → 3 mutual friends or 3 mutual strangers
  R(3,4) = 9
  R(3,5) = 14
  R(4,4) = 18
  R(5,5) = ?         known: 43 ≤ R(5,5) ≤ 48  (open for 40 years)

RAMSEY BOUND:
  R(s,t) ≤ C(s+t-2, s-1)         (Pascal triangle bound)
  R(k,k) ≤ 4ᵏ                     exponential upper bound
  R(k,k) ≥ (k/e)·2^(k/2)         probabilistic lower bound (Erdős 1947)

  The gap between upper/lower for R(k,k) is wide — major open problem.
  Breakthrough 2023: Campos-Griffiths-Morris-Sahasrabudhe improved upper to (4-ε)ᵏ
```

### 12.2 Ramsey-Type Theorems

```
VAN DER WAERDEN'S THEOREM:
  For any k and r: there exists N such that any r-coloring of [N]
  contains a monochromatic arithmetic progression of length k.

HALES-JEWETT THEOREM: Hypercube generalization.
  For any alphabet size t and length k: combinatorial lines in t^n.

SCHUR'S THEOREM:
  For any k-coloring of [N] (N large enough), there exist x,y,z (same color) with x+y=z.

RADO'S THEOREM: characterizes which systems of equations are partition regular.

APPLICATIONS:
  • Theoretical CS: lower bounds via Ramsey argument
  • Number theory: proofs of regularity/structure in dense sets
  • Probabilistic method: Erdős's foundational tool
```

---

## 13. Extremal Graph Theory

### 13.1 Turán's Theorem

```
TURÁN GRAPH T(n,r): complete r-partite graph on n vertices with parts as equal as possible.
  Extremal graph: densest graph with no (r+1)-clique.

TURÁN'S THEOREM:
  Every graph on n vertices with > ex(n, Kᵣ₊₁) edges contains Kᵣ₊₁.
  ex(n, Kᵣ₊₁) = e(T(n,r)) = (1 − 1/r) · n²/2 + O(n)

MANTEL'S THEOREM (r=2): Triangle-free graph on n vertices has ≤ n²/4 edges.
  Equality iff G = Kₙ/₂,ₙ/₂.

KRUSKAL-KATONA THEOREM: extremal for hypergraphs (shadows of k-uniform families).

FORBIDDEN SUBGRAPH PROBLEM:
  ex(n, H) = max edges in n-vertex H-free graph.
  For bipartite H: ex(n,H) = O(n^(2-1/s)) (Zarankiewicz / Kővári-Sós-Turán)
  ex(n, K_{s,s}) ≤ (1/2)s^(1/s) n^(2-1/s) + ... (dense open cases!)
```

### 13.2 The Probabilistic Method

Erdős's revolutionary technique: show existence by proving positive probability.

```
FIRST MOMENT METHOD (first moment principle):
  If E[X] < 1 for some "bad" random variable X ≥ 0, then Pr[X=0] > 0.

LOVÁSZ LOCAL LEMMA (LLL):
  Events A₁,...,Aₙ, each Pr[Aᵢ] ≤ p, each Aᵢ depends on at most d others.
  If ep(d+1) ≤ 1 → Pr[∩ Āᵢ] > 0.
  (Used to show proper coloring exists, good codes exist, etc.)

ALTERATION METHOD:
  Build a random structure, then fix the flaws.
  E.g., independent set: take each vertex independently w/ prob p.
    Expected edges in induced subgraph → delete one vertex per edge.
    Expected remaining vertices ≥ n·p − m·p².  Optimize p = 1/(2Δ).
    → independent set of size ≥ n/(2Δ).

RANDOM LOWER BOUND FOR R(k,k):
  Color edges of Kₙ red/blue independently w.p. 1/2.
  E[# monochromatic Kₖ] = C(n,k)·2·2^(-C(k,2)) < 1 iff n < 2^(k/2)/√(ek).
  → R(k,k) > n. This is the probabilistic lower bound.
```

### 13.3 Szemerédi Regularity Lemma

The regularity lemma (Szemerédi 1975) is the central structural result of extremal
graph theory and additive combinatorics. It says every dense graph looks, at coarse
resolution, like a union of pseudo-random bipartite graphs.

**Definition — ε-regular pair**: a bipartite graph (A, B, E) is **ε-regular** if
for all A' ⊆ A with |A'| ≥ ε|A| and B' ⊆ B with |B'| ≥ ε|B|:
```
|d(A',B') − d(A,B)| ≤ ε       where d(A,B) = |E(A,B)| / (|A|·|B|)
```
The density between large subsets is close to the global density — the bipartite
graph looks random at the scale ε.

**Szemerédi Regularity Lemma**: For every ε > 0, there exists M(ε) such that every
graph G = (V, E) with n ≥ M(ε) vertices has an **ε-regular partition**
V = V₀ ∪ V₁ ∪ ⋯ ∪ Vₖ where:
```
|V₀| ≤ εn                         (exceptional set, small)
|V₁| = |V₂| = ⋯ = |Vₖ|            (equal-size parts)
1/ε ≤ k ≤ M(ε)                     (number of parts is bounded)
all but ε·C(k,2) pairs (Vᵢ,Vⱼ) are ε-regular
```
The number of parts M(ε) is a tower function of 1/ε (unavoidably so — Gowers showed
the tower is necessary). The partition is computable in polynomial time.

**Applications**:

*Triangle removal lemma* (Ruzsa-Szemerédi 1976): If G has o(n³) triangles then
G can be made triangle-free by removing o(n²) edges. Consequence: if every edge of
a graph is in exactly one triangle, the graph has o(n²) edges.

*Green-Tao theorem (2004)*: the primes contain arithmetic progressions of arbitrary
length. Proof outline: primes are "pseudorandom" in a sense that Szemerédi-type
arguments apply (via the transference principle of Green-Tao). The primes are not
dense (they have density zero), but they are dense among the "pseudoprimes," which
makes the combinatorial machinery applicable.

*Counting lemma*: complementing the regularity lemma — any ε-regular partition of
a graph that looks like a pattern H contains approximately the "right" number of
copies of H that you would expect from a random graph with the same edge densities.

*Efficient approximate counting*: for any fixed graph H, counting the number of
copies of H in G to within ε·n^{|V(H)|} is achievable in polynomial time via
the regularity partition.

---

## 14. Algebraic Graph Theory

### 14.1 Spectral Graph Theory

```
ADJACENCY SPECTRUM:
  Eigenvalues λ₁ ≥ λ₂ ≥ ... ≥ λₙ of adjacency matrix A.
  Largest λ₁ ≤ Δ, λ₁ ≥ average degree.
  For d-regular: λ₁ = d.
  Bipartite ↔ spectrum symmetric about 0.

LAPLACIAN SPECTRUM:
  0 = μ₀ ≤ μ₁ ≤ ... ≤ μₙ₋₁ (Laplacian L = D − A)
  μ₁ = 0 with multiplicity = number of connected components.
  μ₁ > 0 (connected) = algebraic connectivity (Fiedler value)
  μₙ₋₁ ≤ n (complete graph)

CHEEGER INEQUALITY (graph version):
  h(G)²/(2Δ) ≤ μ₁ ≤ 2h(G)
  where h(G) = min_{S} |∂S| / min(|S|, |V\S|)  (edge isoperimetric ratio)

EXPANDER GRAPHS:
  Regular graph, small λ₂/λ₁ (spectral gap large).
  Random walks mix fast. Efficient error-correcting codes. Pseudorandomness.
  Explicit constructions (Ramanujan graphs, Cayleygraphs of SL₂(𝔽_p)).

INTERLACING THEOREM (Cauchy):
  Eigenvalues of induced subgraph interlace eigenvalues of full graph.
```

### 14.2 Random Graphs and Sharp Thresholds

Random graph models exhibit **sharp threshold phenomena**: properties appear
suddenly at a critical edge probability p* rather than gradually.

**Erdős-Rényi G(n,p)**: n vertices, each edge present independently with probability p.
```
PHASE TRANSITIONS IN G(n,p):
  p = c/n,  c < 1:   all components have size O(log n)  (sub-critical)
  p = 1/n:           giant component emerges — size Θ(n^{2/3})   [threshold]
  p = c/n,  c > 1:   unique giant component of size Θ(n),
                      all other components O(log n)  (super-critical)
  p = log(n)/n:      connectivity threshold — graph becomes connected a.s.  [threshold]
  p = k·log(n)/n:    minimum degree ≥ k appears a.s.
```

**Proof technique for giant component** (c > 1): branching process argument.
Start from vertex v; explore neighbors as a Galton-Watson branching process with
offspring distribution Binomial(n-1, p) ≈ Poisson(c). For c > 1, extinction
probability q < 1 (supercritical branching process). The survival probability is
the giant component fraction.

**Stochastic block model (SBM)**: generalization of G(n,p) for community structure.
```
n vertices, k communities of size n/k each.
Edge probability p within communities, q between (p > q).
INFORMATION-THEORETIC threshold for exact recovery of communities:
  √(n·p) − √(n·q) ≥ √(2 log k)   (Abbe-Sandon 2015)

SPECTRAL ALGORITHM: eigenvectors of adjacency matrix A (or normalized Laplacian).
  For two communities: Fiedler vector (second eigenvector of L) clusters correctly
  when SNR = (p−q)²·(n/k) / (p + q) > 1  (spectral threshold).
  Below this threshold: no polynomial-time algorithm can recover communities
  (under planted clique hardness).
```

The SBM is the canonical model for **community detection** in network science —
used to benchmark graph clustering algorithms (spectral clustering, Louvain,
label propagation). The spectral algorithm works because the planted community
structure perturbs the leading eigenvalues away from the Wigner semicircle
distribution of the bulk (random matrix theory provides the analysis).

### 14.3 Graph Polynomials

```
CHROMATIC POLYNOMIAL P(G, k):
  Deletion-contraction: P(G−e, k) − P(G/e, k)
  Evaluations:
    k = 0: P = 0
    k = 1: P = 0 unless |E|=0
    (-1)ⁿ P(G, −1) = number of acyclic orientations of G

TUTTE POLYNOMIAL T(G; x, y):
  Two-variable generalization encoding many graph invariants.
  T(G; 2, 1) = number of spanning forests
  T(G; 1, 2) = number of spanning subgraphs
  T(G; 1, 1) = number of spanning trees
  T(G; 2, 0) = number of acyclic orientations
  Connected to partition functions in statistical mechanics (Potts model).

RELIABILITY POLYNOMIAL: probability edges independently intact; graph connected.
```

---

## 15. Möbius Inversion on Posets

```
POSET (P, ≤): partially ordered set.

ZETA FUNCTION ζ(x,y) = 1 if x ≤ y, else 0 (on intervals).
MÖBIUS FUNCTION μ(x,y): defined by Σ_{x≤z≤y} μ(x,z) = [x=y]

MÖBIUS INVERSION:
  f(y) = Σ_{x≤y} g(x)  ↔  g(y) = Σ_{x≤y} μ(x,y) f(x)

EXAMPLES:
  Boolean lattice 2^[n]: μ(A,B) = (-1)^(|B\A|)  → classical inclusion-exclusion!
  Integer divisibility: μ(1,n) = classical Möbius function from number theory
    μ(n) = 0 if n has squared prime factor
    μ(n) = (-1)^k if n = product of k distinct primes

BURNSIDE'S LEMMA (orbit counting):
  |X/G| = (1/|G|) Σ_{g∈G} |X^g|
  Number of distinct colorings = average over symmetries of fixed-point count.
  Polya enumeration theorem: more refined version using cycle index.
```

---

## 16. Graph Algorithms Summary

```
ALGORITHM          COMPLEXITY     PROBLEM
─────────────────────────────────────────────────────────
BFS                O(V+E)         SSSP (unweighted), bipartite check, connectivity
DFS                O(V+E)         Topological sort, SCCs, bridges, cut vertices
Dijkstra           O((V+E)logV)   SSSP (non-negative weights)
Bellman-Ford       O(VE)          SSSP with negative edges / negative cycle detect
Floyd-Warshall     O(V³)          All-pairs shortest paths (dense)
Johnson            O(VE+V²logV)   All-pairs shortest paths (sparse)
Kruskal            O(E log E)     MST with Union-Find
Prim               O(E log V)     MST with priority queue
Ford-Fulkerson     O(E·F)         Max flow (integer capacities)
Edmonds-Karp       O(VE²)         Max flow (BFS augmenting paths)
Dinic              O(V²E)         Max flow; O(E√V) for unit capacities
Hopcroft-Karp      O(E√V)         Bipartite max matching
Kosaraju/Tarjan    O(V+E)         Strongly connected components
Hopcroft-Tarjan    O(V)           Planarity testing
Tarjan low-link    O(V+E)         Bridges and articulation points
```

### Union-Find (Disjoint Set Union)

```
Data structure for dynamic connectivity / Kruskal's.

find(x): return root of x's component (with path compression)
union(x,y): merge components of x and y (union by rank/size)

With path compression + union by rank: O(α(n)) amortized per operation
  where α = inverse Ackermann function — essentially O(1).

class DSU:
    def __init__(self, n): self.parent = list(range(n)); self.rank = [0]*n
    def find(self, x):
        if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        x,y = self.find(x), self.find(y)
        if x == y: return False
        if self.rank[x] < self.rank[y]: x,y = y,x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]: self.rank[x] += 1
        return True
```

---

## 17. NP-Hard Graph Problems

```
INDEPENDENT SET: max set with no edges — NP-hard
  k-independent set: k-clique in complement graph

VERTEX COVER: min set touching every edge — NP-hard
  VC + Independent Set = n (complement relationship)
  2-approximation: take both endpoints of maximal matching

CLIQUE: max complete subgraph — NP-hard
  Parameterized: k-clique in O(n^(k/3)) via fast matrix mult

GRAPH COLORING: decide χ(G) ≤ 3 — NP-hard (χ ≤ 2 is poly-time)
  4-coloring planar graphs — poly-time (4CT gives existence, constructive)

HAMILTONIAN CYCLE: NP-hard in general; poly-time on tournaments, interval graphs
  TSP: NP-hard, but (3/2)-approx (Christofides)

STEINER TREE: connect subset of terminals with min-cost tree — NP-hard
  (contrast: Spanning tree = all terminals = poly-time)

GRAPH ISOMORPHISM: neither known P nor NP-complete
  GI-complete: special complexity class
  Quasi-poly: Babai 2016 n^(polylog n) algorithm
```

### Inapproximability and Parameterized Complexity

The PCP theorem (probabilistically checkable proofs, Arora-Safra 1992) transforms
NP-hardness into inapproximability. The key result: 3-SAT has a "gap" — it is
NP-hard to distinguish satisfiable instances from those where every assignment
violates at least ε of the clauses, for some constant ε > 0.

**Sharp inapproximability bounds** (PCP corollaries):
```
MAX INDEPENDENT SET:  NP-hard to approximate within n^{1-ε} for any ε > 0
  (Håstad 1999 — tight, since trivial O(n) upper bound)

MAX CLIQUE:           NP-hard to approximate within n^{1-ε}
  (same graph as complement: clique in G = independent set in Ḡ)

CHROMATIC NUMBER:     NP-hard to approximate within n^{1-ε}
  (Feige-Kilian 1998; coloring with O(log n) colors is hard unless P=NP)

MAX 3-SAT:            NP-hard to approximate better than 7/8 ratio
  (Håstad 1997 — 7/8 is the random assignment bound; tight)

VERTEX COVER:         NP-hard to approximate below 2 − ε
  (Khot-Regev 2008, under Unique Games Conjecture)
  Polynomial integrality gap of 2 in the LP relaxation.
```

**Unique Games Conjecture (UGC)**: Khot 2002. If true, many 2-approximation
algorithms for vertex cover and similar problems are tight — the SDP/LP integrality
gaps are the true approximation thresholds.

**Parameterized complexity** — beyond NP-hardness, refine by parameter k:
```
FPT (Fixed-Parameter Tractable): solvable in f(k) · poly(n)
  k-VERTEX COVER: O(1.2738^k + k·n) — crown decomposition + bounded search tree
  k-FEEDBACK VERTEX SET: FPT
  k-DOMINATING SET: FPT on planar graphs (bidimensionality), W[2]-hard in general

W[1]-hard: unlikely to be FPT (parameterized hardness)
  k-CLIQUE: O(n^k) is essentially optimal (no FPT under ETH)
  k-INDEPENDENT SET: W[1]-hard

ETH (Exponential Time Hypothesis): 3-SAT cannot be solved in 2^{o(n)}.
  Implies: k-clique requires n^{Ω(k)} time.
  Strong ETH (SETH): stronger, implies many conditional lower bounds.
```

---

## 18. Connections to Computer Science and ML

### 18.1 Graphs in Systems

```
DAG APPLICATIONS:
  Dependency resolution:      npm, pip — topological sort of packages
  Build systems:              Bazel, Ninja — task DAG
  Database query plans:       operator DAG
  Compiler SSA form:          control flow graph (possibly cyclic)
  Git commits:                DAG (merge = multiple parents)
  Spark/Flink:                dataflow DAG

RANDOM WALKS ON GRAPHS:
  PageRank: stationary distribution of random walk on web graph.
    π = M·π   (M = teleporting random walk matrix)
    Power iteration convergence rate = 2nd eigenvalue of M.
  Graph partitioning (Spectral clustering):
    Fiedler vector (eigenvector of μ₁) gives low-conductance cut.

NETWORK FLOW IN PRACTICE:
  Bipartite matching → job scheduling, assignment problems
  Min-cost flow → transportation, supply chain
  Multi-commodity flow → network routing (LP relaxation)
```

### 18.2 Graph Neural Networks (GNNs)

```
MESSAGE PASSING NEURAL NETWORKS:
  hᵥ⁽ˡ⁾ = UPDATE(hᵥ⁽ˡ⁻¹⁾, AGG({hᵤ⁽ˡ⁻¹⁾ : u ∈ N(v)}))

  GCN (Kipf-Welling 2017):   H⁽ˡ⁺¹⁾ = σ(D̃⁻¹/² Ã D̃⁻¹/² H⁽ˡ⁾ W⁽ˡ⁾)
    Ã = A + I (self-loops), D̃ degree of Ã
    Spectral interpretation: low-pass filter on graph Laplacian spectrum

  GraphSAGE:   sample and aggregate (inductive learning)
  GAT:         graph attention (weighted neighbor aggregation)

WL ISOMORPHISM TEST:
  Message-passing GNNs ≤ Weisfeiler-Leman (1-WL) in expressiveness.
  GNNs can't distinguish regular non-isomorphic graphs.
  Higher-order GNNs ≡ k-WL.

GRAPH TRANSFORMERS:
  Attention over all node pairs O(n²). Uses positional encodings (Laplacian eigenvectors).
  Overcomes WL expressiveness limitations.

KNOWLEDGE GRAPHS:
  Entities = vertices. Relations = edge labels (heterogeneous graph).
  TransE, RotatE, DistMult — embedding learning for KG completion.
```

### 18.3 Combinatorics in CS Theory

```
INFORMATION-THEORETIC LOWER BOUNDS:
  Decision tree complexity: depth = O(log |leaf set|)
  Comparison sort Ω(n log n): binary tree has ≤ 2ᵈ leaves at depth d
    → depth ≥ log₂(n!) ≈ n log n

EXPANDER CODES: Sipser-Spielman linear-time decodable error-correcting codes.
  Based on expander graphs. Min-distance ∝ expansion ratio.

DERANDOMIZATION:
  Expanders → pseudorandom generators → BPP vs P.
  Hitting sets, ε-nets.

COMMUNICATION COMPLEXITY:
  2-party: Alice has x, Bob has y → compute f(x,y) with min bits exchanged.
  Partition number, fooling sets, rank lower bounds.
  Connection to circuit complexity.

HASH FUNCTIONS AND UNIVERSAL HASHING:
  Family H is k-universal: for distinct x₁,...,xₖ and any y₁,...,yₖ,
    Pr_{h∈H}[h(xᵢ)=yᵢ ∀i] = 1/mᵏ
  2-universal via affine maps h(x) = (ax+b) mod p mod m.
```

---

## 19. Decision Cheat Sheet

| Problem | Algorithm | Complexity | Notes |
|---------|-----------|-----------|-------|
| Connected? | BFS/DFS | O(V+E) | |
| Shortest path (unweighted) | BFS | O(V+E) | |
| Shortest path (weighted, pos) | Dijkstra | O((V+E)logV) | |
| Shortest path (neg weights) | Bellman-Ford | O(VE) | Detects neg cycles |
| All-pairs shortest paths | Floyd-Warshall | O(V³) | Or Johnson for sparse |
| MST | Kruskal or Prim | O(E log E) | Kruskal simpler, Prim better dense |
| Max flow | Dinic | O(V²E) | Unit: O(E√V) |
| Bipartite matching | Hopcroft-Karp | O(E√V) | |
| Min vertex cover (bipartite) | König's + matching | O(E√V) | König: MVC = max match |
| Topological sort | Kahn's BFS | O(V+E) | Detects cycle |
| SCCs | Tarjan/Kosaraju | O(V+E) | |
| Planarity | Hopcroft-Tarjan | O(V) | |
| Eulerian circuit | Hierholzer | O(E) | Check degrees first |
| Hamiltonian cycle | — | NP-hard | No known poly-time |
| k-coloring (k≥3) | — | NP-hard | 2-coloring = bipartite check |
| Clique number | — | NP-hard | Exact |
| Independent set | — | NP-hard | 2-approx via matching |
| Dynamic connectivity | Link-cut trees | O(log n) amortized | Advanced |
| Asymptotics of [xⁿ]A(x) | Singularity analysis | — | Dominant singularity of A(x) |
| Community detection | Spectral (Fiedler vector) | O(n log n) | SBM with SNR above threshold |

---

## 20. Common Confusion Points

**Euler vs. Hamilton**: Euler visits every *edge* once (easy, O(E)). Hamilton visits
every *vertex* once (NP-hard). People mix these up constantly.

**Matching ≠ Covering**: Max matching and min vertex cover are dual (bipartite), but the
equality (König's theorem) fails for non-bipartite graphs.

**Tree ≠ Forest**: A tree is a connected acyclic graph. A forest allows disconnected
components (multiple trees). k components, n vertices → n-k edges.

**Graph coloring hardness**: 2-coloring (bipartite check) is O(V+E). 3-coloring is
NP-complete. 4-coloring is poly-time for planar graphs (4CT). General 4-coloring is
NP-hard.

**Ramsey theory**: R(3,3)=6 is famous — it's the smallest number guaranteeing structure.
The exact values R(5,5), R(6,6) are open despite enormous effort.

**Generating functions are formal**: They don't need to converge. Operations (multiply,
differentiate) are purely algebraic. Convergence analysis (singularity, asymptotics via
Cauchy integral) is a separate step for extracting coefficients.

**χ(G) vs. ω(G)**: Clique number ω(G) is a lower bound for χ(G), but not always tight.
Perfect graphs (Chudnovsky et al. 2006): χ(G) = ω(G) for all induced subgraphs
iff G has no induced odd hole or its complement.

**Planarity by drawing**: Planarity is about *existence* of a crossing-free drawing,
not a specific drawing. K₅ and K₃,₃ are the two obstruction minors (Wagner/Kuratowski).

**Flow networks and LP duality**: Max-flow min-cut is LP duality for the flow LP.
Every min-cut theorem (König's, Hall's, Menger's) is a special case of LP duality or
max-flow min-cut. They're all the same theorem in different disguises.

**GNNs and 1-WL**: Standard message-passing GNNs can't distinguish all non-isomorphic
graphs — they're limited to the expressive power of 1-WL color refinement. This is why
graph transformers and higher-order GNNs exist.

**Szemerédi vs. regularity**: The regularity lemma gives a structural decomposition;
the counting lemma gives the quantitative statement about subgraph densities. Both are
needed together to apply the framework. The tower bound on M(ε) is unavoidable (Gowers).
