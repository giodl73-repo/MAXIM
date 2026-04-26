# Algorithms & Data Structures — Engineering Reference

## The Big Picture

You have MIT 6.006 and 6.046 under your belt. This is not a tutorial — it is a **structured recall document** bridging theory to where it surfaces in production systems, modern runtimes, and distributed infrastructure. It also covers post-2000 developments: cache-oblivious models, streaming algorithms, parameterized complexity, and where classical algorithms live in real codebases.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALGORITHMIC COMPLEXITY LANDSCAPE                                           │
│                                                                             │
│  Provably Efficient                    Practically Efficient                │
│  ───────────────────────────────           ─────────────────────────────────────         │
│  Sorting:      O(n log n) optimal      TimSort, Introsort (real constants)  │
│  Shortest path: O(E log V)             Dijkstra with binary heap            │
│  MST:          O(E log V) or E α(n)    Kruskal + union-find                 │
│  Max-flow:     O(V²E) Dinic            Push-relabel in practice             │
│  Matching:     O(E√V)                  Hopcroft-Karp                        │
│                                                                             │
│  Intractable (NP-hard)                 Modern Escapes                       │
│  ───────────────────────               ─────────────────────────────────    │
│  TSP, 3-SAT, Graph Coloring           FPT (parameterized by solution size)  │
│  Independent Set, Clique              Approximation schemes (PTAS/FPTAS)    │
│  Knapsack (general), Partition        Randomized algorithms                 │
│                                                                             │
│  Complexity Hierarchy:                                                      │
│  P ⊆ NP ∩ co-NP ⊆ PH ⊆ PSPACE ⊆ EXPTIME                                  │
│  NP-hard: ≥ any NP (not necessarily in NP)                                  │
│  NP-complete: NP-hard ∩ NP                                                  │
│                                                                             │
│  Modern practical concerns:                                                 │
│  Cache efficiency (I/O model)   Parallelism (PRAM)   Streaming (polylog)    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Complexity Analysis — Formal Machinery

### Asymptotic Notation

```
f(n) = O(g(n)):   ∃c, n₀ s.t. f(n) ≤ c·g(n)  for all n ≥ n₀   [upper bound]
f(n) = Ω(g(n)):   ∃c, n₀ s.t. f(n) ≥ c·g(n)  for all n ≥ n₀   [lower bound]
f(n) = Θ(g(n)):   f = O(g) AND f = Ω(g)                        [tight bound]
f(n) = o(g(n)):   lim_{n→∞} f(n)/g(n) = 0                      [strictly dominated]
f(n) = ω(g(n)):   lim_{n→∞} f(n)/g(n) = ∞                      [strictly dominates]
```

### Amortized Analysis — Three Methods

**Aggregate**: Total cost of n operations = T(n). Amortized per operation = T(n)/n.

**Accounting**: Assign credits. Cheap ops store credits; expensive ops spend them. Invariant: credit balance ≥ 0 always.

**Potential method** (most powerful):
```
Define Φ: DataStructure → ℝ≥0
Amortized cost of op_i = actual_cost_i + Φ(state_after) - Φ(state_before)
Total amortized ≥ Total actual  (since Φ ≥ 0)
```

Classic example — dynamic array doubling:
- Define Φ = 2·size - capacity  (starts at 0 when array is empty)
- Normal insert: actual=1, Φ rises by 2 → amortized = 3 = O(1)
- Doubling insert (size=capacity=n): actual=n (copy all), Φ drops from n to 0 → amortized = n + (0 - n) = 0

### Master Theorem

```
T(n) = aT(n/b) + f(n),   a ≥ 1, b > 1,  c_crit = log_b(a)

Case 1: f(n) = O(n^(c_crit-ε))  →  T(n) = Θ(n^c_crit)       subproblems dominate
Case 2: f(n) = Θ(n^c_crit)     →  T(n) = Θ(n^c_crit · log n) balanced
Case 3: f(n) = Ω(n^(c_crit+ε)) + regularity →  T(n) = Θ(f(n)) root dominates

Key examples:
  Merge sort:    T(n)=2T(n/2)+n     → c_crit=1, Case 2  → Θ(n log n)
  Binary search: T(n)=T(n/2)+1      → c_crit=0, Case 2  → Θ(log n)
  Strassen:      T(n)=7T(n/2)+n²    → c_crit=log₂7≈2.81 > 2, Case 1 → Θ(n^log₂7) ≈ Θ(n^2.81)
  Karatsuba:     T(n)=3T(n/2)+n     → c_crit=log₂3≈1.58 > 1, Case 1 → Θ(n^log₂3) ≈ Θ(n^1.58)
```

Akra-Bazzi generalizes Master to unequal subproblem sizes.

---

## 2. Data Structures — Cache Reality

### Arrays and Cache Effects

The uniform-cost RAM model is wrong for modern CPUs:
```
L1 cache  (32KB):    ~4 cycles
L2 cache  (512KB):   ~12 cycles
L3 cache  (8MB+):    ~40 cycles
DRAM:                ~200 cycles
Cache line size:     64 bytes = 8 × int64
```

Linked list traverse of n nodes → n cache misses.
Array traverse of n int64 → n/8 cache misses.

**Practical consequence**: For n < 10³, sorted array + binary search often beats a BST. B-tree (branching factor 64–512) beats both at database scale because each disk/cache page holds many keys.

### Hash Tables

```
Chaining                            Open addressing (linear probing)
──────────────────────────────      ─────────────────────────────────────
Bucket → linked list                H(k), H(k)+1, H(k)+2, ...
Load factor α = n/m                 Load factor α < 0.7 (empirically)
Expected O(1+α) per operation       Cache-friendly (no pointer chasing)
Works for α > 1                     Deletion: tombstones or backward shift
                                    Robin Hood hashing minimizes variance
```

Universal hash family (Wegman-Carter): H_{a,b}(k) = ((ak+b) mod p) mod m
- p prime > universe size, a ∈ {1,..,p-1}, b ∈ {0,..,p-1} chosen randomly
- For any x≠y: Pr[H(x)=H(y)] ≤ 1/m → collision prob independent of key values

**FKS perfect hashing**: For static set S of n keys, O(n) space, O(1) worst-case lookup.
- Two-level: first-level m=n buckets, second level h_j has m_j = O(n_j²) slots (n_j = bucket size)
- Expected total second-level size = O(n)

### Priority Queues

| Structure | Insert | Extract-min | Decrease-key | Merge | Notes |
|-----------|--------|-------------|--------------|-------|-------|
| Binary heap | O(log n) | O(log n) | O(log n) | O(n) | Best cache perf |
| d-ary heap | O(log_d n) | O(d log_d n) | O(log_d n) | O(n) | d=4 good in practice |
| Binomial heap | O(log n) | O(log n) | O(log n) | O(log n) | Mergeable |
| Fibonacci heap | O(1) amort | O(log n) amort | O(1) amort | O(1) | Theory: Dijkstra O(E+V log V) |
| Pairing heap | O(1) amort | O(log n) amort | O(log n) amort | O(1) | Fibonacci killer in practice |

Fibonacci heaps: beautiful theory, poor cache behavior. Binary heap + lazy deletion wins in practice for n < 10⁶.

### Balanced BSTs

**Red-Black Tree** (Java TreeMap, C++ std::map, Linux kernel CFS):
- 4 invariants: root black; red nodes have black children; all root→null paths have equal black-height; leaves are null (black)
- Height ≤ 2 log₂(n+1). Rotations fix violations after insert/delete.

**AVL Tree**: |height(L) - height(R)| ≤ 1 at every node. Height ≤ 1.44 log₂(n+1). More rotations on insert/delete, faster lookups than RB.

**Skip List** (Redis sorted sets, LevelDB, Java ConcurrentSkipListMap):
- Level chosen geometrically: P(level k) = p^(k-1)(1-p). Expected O(log n) per op.
- Easy lock-free implementation (CAS on forward pointers). Excellent for concurrent access.

**Splay Tree**: Every accessed node splayed to root. O(log n) amortized. Working-set property: if last m queries hit set of k distinct items, total cost = O(m log k). Static optimality.

**B+ Tree** (every RDBMS index):
- Degree t: each internal node has t-1 to 2t-1 keys, t to 2t children
- All data at leaves; leaves linked in doubly-linked list (range scans)
- Height = O(log_t n). For t=512, log₅₁₂(10¹²) ≈ 4 levels → 4 disk I/Os for any lookup
- PostgreSQL, MySQL InnoDB, SQL Server: all clustered B+ tree indexes

### Union-Find (Disjoint Set Union)

```
MakeSet(x), Find(x) [with path compression], Union(x, y) [by rank]

Path compression: on Find(x), set every node on path to root directly to root
Union by rank:    attach smaller-rank tree under larger-rank root

With both optimizations: amortized O(α(n)) per operation
α(n) = inverse Ackermann function: α(10^80) = 4 — effectively O(1)
Tarjan (1975) proved this is optimal.
```

Production uses: Kruskal's MST, dynamic connectivity, image segmentation, cycle detection, Git merge-base computation.

---

## 3. Sorting

### Comparison Sort Lower Bound

Ω(n log n) comparisons required in the worst case. Proof via decision tree: must distinguish n! permutations; binary tree with n! leaves has depth ≥ log₂(n!) = Θ(n log n) by Stirling.

### Sorting Reference

| Algorithm | Best | Average | Worst | Space | Stable | Use when |
|-----------|------|---------|-------|-------|--------|----------|
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | n < 16, nearly-sorted |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | External sort, linked lists |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | General in-memory |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | Worst-case O(n log n) needed |
| Introsort | O(n log n) | O(n log n) | O(n log n) | O(log n) | ❌ | std::sort (GCC/MSVC/Clang) |
| pdqsort | O(n) | O(n log n) | O(n log n) | O(log n) | ❌ | Rust std::sort, C++ Boost.Sort |
| TimSort | O(n) | O(n log n) | O(n log n) | O(n) | ✅ | Real-world data |
| Radix sort | O(d·n) | O(d·n) | O(d·n) | O(n+k) | ✅ | Integer keys, fixed width |
| Counting sort | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ | Small integer range k |

**Introsort**: Quicksort → switch to heapsort when recursion depth > 2·log₂n → insertion sort for n < 16. GCC's `std::sort`. No worst case, small constants.

**pdqsort (pattern-defeating quicksort)**: The standard sort in Rust's `std::sort` and C++ Boost.Sort. Introsort is the baseline; pdqsort adds pattern detection on top:
- **Nearly-sorted or reverse-sorted input**: detected via cheap prescan; switches to insertion sort
- **Many duplicates or all-equal**: detected via equal-element tracking; avoids O(n²) on pathological pivot sequences
- **Random data**: behaves like Introsort (quicksort with median-of-3 pivot, heapsort fallback)
- **Adversarial pivot sequences**: heapsort fallback (same as Introsort) prevents worst case

The insight: real-world data is almost never uniformly random. Nearly-sorted arrays (common after an earlier sort plus a few inserts) and arrays with many duplicates (enum columns, boolean fields) are the norm in production. pdqsort's O(n) best case on these patterns is why Rust's sort benchmarks better than textbook quicksort at the same O(n log n) average — the constants collapse for common inputs.

**TimSort**: Detect natural runs (ascending or descending). Merge runs via "galloping" mode that adapts to the data's existing order. Python `list.sort()`, Java `Arrays.sort()` for objects, Android SDK.

**Quicksort analysis**: With random pivot, expected comparisons = 2n ln n ≈ 1.39 n log₂n. Median-of-three pivot reduces constants significantly.

### External Sort

When n doesn't fit in RAM (database context):
```
Phase 1: Read M-element chunks, sort in-memory, write sorted runs to disk.
         Produces ⌈N/M⌉ sorted runs.

Phase 2: k-way merge of all runs using a min-heap.
         One merge pass if k = ⌈N/M⌉.
         Multi-pass if memory insufficient for k-way merge.

I/O complexity: O((N/B) · log_{M/B}(N/B)) block transfers.
  N = total elements, B = block size, M = memory.
```

Every database ORDER BY, hash join build phase, and GROUP BY uses external sort or hash aggregation.

---

## 4. Graph Algorithms

### Representations

| Structure | Space | Edge check | Neighbor iterate | Use when |
|-----------|-------|------------|-----------------|----------|
| Adjacency matrix | O(n²) | O(1) | O(n) | Dense graphs, Floyd-Warshall |
| Adjacency list | O(n+m) | O(deg) | O(deg) | Sparse graphs (standard) |
| CSR (Compressed Sparse Row) | O(n+m) | O(log deg) | O(deg) | Graph processing systems, cache-friendly |
| Edge list | O(m) | O(m) | O(m) | Kruskal's, sparse problem setup |

### BFS and DFS

```
BFS from s:
  O(n+m). Explores level by level.
  BFS tree = shortest-path tree (unweighted). All paths in BFS tree are shortest.
  Level k = all vertices at distance k from s.

DFS:
  O(n+m). Explores as deep as possible before backtracking.
  Edge classification in directed graph:
    Tree edge:    v discovered through u
    Back edge:    v is ancestor of u  →  cycle exists
    Forward edge: v is descendant of u, already finished
    Cross edge:   v in different subtree or already processed
  In undirected graph: only tree and back edges exist.
```

### Shortest Path Algorithm Reference

| Algorithm | Complexity | Negative edges | Use when |
|-----------|------------|----------------|----------|
| BFS | O(V+E) | No (unweighted) | Unweighted shortest path |
| Dijkstra (binary heap) | O((V+E) log V) | No | Standard SSSP, non-negative weights |
| Dijkstra (Fibonacci heap) | O(E + V log V) | No | Dense graphs, theory |
| Bellman-Ford | O(VE) | Yes | Negative edges, cycle detection |
| SPFA | O(V+E) avg / O(VE) worst | Yes | Avoid — adversarial inputs kill it |
| A* | O(E log V) | No | Point-to-point with good heuristic |
| Floyd-Warshall | O(V³) | Yes (no neg cycles) | All-pairs, dense graph |
| Johnson's | O(V² log V + VE) | Yes (reweighted) | All-pairs, sparse graph |

### Strongly Connected Components

**Kosaraju's** (two passes, conceptually clean):
1. DFS on G, record finish times
2. DFS on Gᵀ (reversed edges) in decreasing finish-time order
3. Each DFS tree in step 2 is one SCC

**Tarjan's** (one pass, implementation standard):
```
Maintain: discovery time disc[v], low[v] = min disc reachable from v's subtree, stack
When low[v] == disc[v]: v is SCC root → pop stack until v
Time: O(n+m)
```

**Kosaraju vs Tarjan**: Same asymptotic complexity. Tarjan is one pass (better constants). Kosaraju requires reversing the graph. Both O(n+m).

### Shortest Paths — Detail

**Dijkstra**:
```
Prerequisites: non-negative edge weights
Data structure: min-heap on (dist, vertex)
Algorithm: extract min, relax all edges from extracted vertex
Time: O((n+m) log n) with binary heap
      O(m + n log n) with Fibonacci heap

Correctness: When vertex v extracted, d[v] is final.
Proof: d[v] ≤ d[u] for all remaining u in heap.
       Adding any path through remaining vertices can only increase cost.
```

**Bellman-Ford**:
```
Works with negative edge weights. Detects negative cycles.
Relax all m edges, repeat n-1 times.
If any relaxation succeeds on pass n → negative cycle reachable from s.
Time: O(nm).
Used in: OSPF (routing), currency arbitrage detection.
```

**SPFA** (Shortest Path Faster Algorithm): Bellman-Ford with a queue (relax only neighbors of updated vertices). Average O(m), worst case O(VE). On adversarial inputs (grids, graphs designed to force many re-relaxations), SPFA degrades to the full O(VE) bound. In competitive programming this is a known attack; in production use Dijkstra + Johnson's reweighting instead.

**A\*** (heuristic search):
```
Extend Dijkstra with heuristic h(v).
Expand nodes by f(v) = g(v) + h(v), where g(v) = dist from source.

Admissible: h(v) ≤ true_dist(v, target).  Guarantees optimal path found.
Consistent (monotone): h(u) ≤ w(u,v) + h(v) for all edges (u,v).
  → h decreases by at most edge weight along any path.

Consistency is strictly stronger than admissibility.
  - Admissible but not consistent: A* may expand the same node multiple times
    (must allow re-expansion when a shorter path arrives).
  - Consistent: each node expanded at most once (standard closed-set optimization works).

For grid pathfinding, Manhattan distance is consistent.
For Euclidean graphs, straight-line distance is consistent.
Used in: game pathfinding, navigation, robot planning.
```

**Floyd-Warshall** (all-pairs):
```
dp[i][j][k] = shortest path from i to j using intermediate vertices ⊆ {1..k}
Recurrence: dp[i][j][k] = min(dp[i][j][k-1],  dp[i][k][k-1] + dp[k][j][k-1])
Time: O(n³), Space: O(n²) (drop third dimension)
Detects negative cycles: dp[i][i] < 0 after completion.
```

**Johnson's** (all-pairs, sparse graphs):
- Reweight using Bellman-Ford potentials h[v] (one Bellman-Ford from virtual source s')
- New weight: w'(u,v) = w(u,v) + h[u] - h[v] ≥ 0
- Run Dijkstra from each vertex on reweighted graph
- Time: O(nm + n² log n) = O(V² log V + VE). Better than Floyd-Warshall's O(V³) when m = o(n²/log n) — i.e., sparse graphs.

**Bidirectional Dijkstra**: Run Dijkstra simultaneously from source and target. Terminate when the search frontiers meet. In practice halves the search space for point-to-point queries — the key optimization in road network routing (Google Maps, OSRM).

### Minimum Spanning Trees

**Cut property**: For any cut (S, V\S), the minimum-weight crossing edge belongs to some MST. **Cycle property**: For any cycle C, the maximum-weight edge in C is not in any MST (assuming distinct weights).

**Kruskal's**:
```
Sort edges by weight: O(m log m)
Process in order: add edge iff it connects two different components (DSU)
Total: O(m log m) — dominated by sort
```

**Prim's**:
```
Start from any vertex. Maintain cut (S, V\S).
Greedily add minimum-weight crossing edge.
With binary heap:     O(m log n)
With Fibonacci heap:  O(m + n log n)  ← asymptotically optimal
```

**Borůvka's**: Each component finds cheapest outgoing edge, all added simultaneously. O(m log n). Parallelizes trivially → used in parallel MST algorithms.

### Network Flow

**Ford-Fulkerson framework**:
```
While augmenting path s→t exists in residual graph:
  Augment by bottleneck capacity of path
Max-flow = when no augmenting path exists
O(E · max_flow) — unbounded with irrational capacities (Ford-Fulkerson pathological case)
```

**Edmonds-Karp**: BFS augmenting paths. O(VE²). Augment along shortest (fewest edges) path each time.

**Dinic's algorithm**:
```
1. BFS to build level graph (edges from level l to l+1 only, dist(s,v) = level(v))
2. Find blocking flow in level graph (DFS, advance until stuck, retreat and delete)
3. Repeat from step 1 until no s-t path in level graph

Time: O(V²E) general.
      O(E√V) for unit-capacity graphs → bipartite matching.
      O(E V^(2/3)) for unit-capacity general → faster in practice.
```

**Push-relabel** (Goldberg-Tarjan): O(V²√E) with FIFO selection. Maintain preflow (excess at each node). Push excess to lower-labeled neighbors. Relabel when stuck. Better than Dinic for dense graphs in practice.

**Max-flow min-cut theorem**: max-flow value = min-cut capacity (Ford-Fulkerson, Elias-Feinstein-Shannon, 1956). One of the deepest results in combinatorics — equivalent to LP duality, König's theorem, Menger's theorem.

### Bipartite Matching

**Hall's theorem**: Perfect matching exists in G=(L∪R, E) iff ∀S⊆L: |N(S)| ≥ |S|.

**Hungarian (Kuhn's) algorithm**: Augmenting path via DFS. O(VE) per augmentation, O(V²E) total.

**Hopcroft-Karp**: Find shortest augmenting paths via BFS, augment along a maximal set simultaneously. O(E√V). Optimal for bipartite matching.

**Assignment problem (weighted bipartite)**: Hungarian algorithm (Kuhn-Munkres). O(V³). Find min-cost perfect matching. Used in: container scheduling, airline crew assignment, stable matching.

---

## 5. Dynamic Programming

### The Paradigm

DP works when:
1. **Overlapping subproblems**: Same subproblems recur (unlike divide-and-conquer which partitions)
2. **Optimal substructure**: Optimal solution contains optimal solutions to its subproblems

```
Two styles:
  Top-down (memoization):              Bottom-up (tabulation):
  def dp(i, j):                        for i in range(n):
    if (i,j) in cache: return cache     for j in range(m):
    ... compute from dp(i-1,j), ...       table[i][j] = ...
    cache[(i,j)] = result
    return result
```

Bottom-up avoids recursion overhead and enables space optimization (often only need last row/column).

### Problem Reference

| Problem | State | Recurrence | Complexity |
|---------|-------|------------|------------|
| LCS | dp[i][j] = LCS(A[:i], B[:j]) | A[i]==B[j]: dp[i-1][j-1]+1; else max(dp[i-1][j], dp[i][j-1]) | O(nm) |
| Edit distance | dp[i][j] = edit(A[:i], B[:j]) | insert/delete/replace | O(nm) |
| LIS | dp[i] = LIS ending at i | O(n²) DP; O(n log n) with patience sorting | O(n log n) |
| 0/1 Knapsack | dp[i][w] | take item i or skip | O(nW) pseudo-poly |
| Coin change | dp[amount] | min coins for amount | O(amount· | coins | ) |
| Matrix chain | dp[i][j] = cost for M_i..M_j | split at k | O(n³) |
| Optimal BST | dp[i][j] | root selection (Knuth speedup) | O(n²) |
| Egg drop | dp[k][n] | binary search on floor | O(k log n) |

### Advanced DP Techniques

**Bitmask DP**: State = subset of n elements encoded as n-bit integer. O(2ⁿ · n).
- TSP: dp[mask][v] = min cost to visit subset `mask`, ending at vertex v.
- dp[mask][v] = min over u∈mask: dp[mask ^ (1<<v)][u] + cost[u][v]
- Final answer: min over v: dp[(1<<n)-1][v] + cost[v][0]

**Divide-and-conquer DP optimization**: When optimal split point opt(i,j) ≤ opt(i,j+1). Reduces O(n³) → O(n² log n) or O(n²).

**Knuth-Yao speedup**: dp[i][j] uses opt[i][j-1] ≤ opt[i][j] ≤ opt[i+1][j]. Reduces O(n³) → O(n²).

**Convex Hull Trick (CHT)**: When dp[i] = min_j (f(j) + slope(j) · i). Maintain lower envelope of lines using convex hull / monotone deque. O(n) if queries monotone.

**Li Chao segment tree**: Dynamic line insertion + point queries. O(n log C) for queries in range [0, C]. Used when slopes are not monotone.

---

## 6. String Algorithms

### Pattern Matching

```
Naïve:         O(nm) — scan all positions, compare

KMP:
  Build failure function π: π[i] = longest proper prefix of P[:i+1] that is also suffix
  Use π to skip redundant comparisons after mismatch
  Time: O(n+m), Space: O(m)

Rabin-Karp:
  Rolling polynomial hash: advance window in O(1)
  O(n+m) expected; O(nm) worst case (hash collisions)
  Strength: multi-pattern search (hash all k patterns, single O(n) text scan)

Boyer-Moore:
  Scan right-to-left; bad character + good suffix heuristics
  O(n/m) best case on random text; O(nm) worst case
  Used in grep, text editors

Aho-Corasick (multi-pattern):
  Build trie of k patterns (total length L). Add failure links (BFS).
  Text search: O(n + |matches|) after O(L) preprocessing.
  Applications: antivirus scanners, intrusion detection, content filtering.
```

### Suffix Structures

**Suffix array**: SA[i] = start index of i-th lexicographically smallest suffix.
- Construction: Naïve O(n² log n). DC3/Skew O(n). SA-IS O(n) (practical).
- With LCP array (lcp[i] = LCP of suffix SA[i] and SA[i-1]): most string problems solvable.

**Suffix tree**: Compressed trie of all suffixes. O(n) via Ukkonen's algorithm.
- Enables: O(m) pattern search, arbitrary LCP queries, all classical string problems.
- In practice: suffix arrays preferred (2-3x less memory, better cache behavior).

**Z-array**: Z[i] = length of longest substring starting at i matching a prefix of S. O(n) construction. Equivalent power to KMP for single pattern.

---

## 7. Advanced Data Structures

### Range Query Structures

```
Fenwick Tree (Binary Indexed Tree):
  Supports: point update + prefix sum query.
  Time: O(log n) each. Build: O(n).
  Operations use binary representation: update goes "up" (i += i & -i),
  query goes "down" (i -= i & -i).
  Compact, fast, simple to implement. Extend to 2D: O(log² n).

Segment Tree:
  Supports: range query + point update (O(log n)).
  With lazy propagation: range update + range query (O(log n)).
  Any associative operator: sum, min, max, gcd, XOR.
  Can be made persistent (path copying: O(log n) new nodes per update).

Sparse Table:
  Precompute st[i][j] = op(A[i..i+2^j-1]) for all i, j.
  Build: O(n log n). Query: O(1) for idempotent ops (min, max, gcd).
  Query: op(st[l][k], st[r-2^k+1][k]) where 2^k ≤ r-l+1.
  Static only (no updates).
```

### Heavy-Light Decomposition (HLD)

Partition tree into O(log n) heavy paths (each path formed by following heaviest child).
Map paths onto a 1D array. Segment tree on that array.
Tree path queries (sum/max/min from u to v): O(log² n) = O(log n paths × O(log n) per segment tree query).

### Persistent Data Structures

Create new version of structure after each update, sharing unchanged parts.

**Persistent segment tree (path copying)**:
- Each update creates O(log n) new nodes (one per level).
- All old versions remain accessible.
- Space: O(n log n) for n updates.
- Applications: range k-th smallest offline, persistent arrays, version history.

### Cache-Oblivious Algorithms

Design without knowing B (block size) or M (memory size), yet achieve optimal I/O complexity for any values.

**van Emde Boas tree layout**: Recursively split BST at median level. Each subtree stored contiguously. For any B, top ≈√B levels fit in one cache block → O(log_B n) cache misses. Achieves B-tree efficiency without knowing B.

**Cache-oblivious matrix multiply**: Divide matrices recursively. When problem fits in cache, no further misses. Total I/O: O(n³/(B√M)) — matches bandwidth lower bound.

**Funnelsort**: Cache-oblivious sorting. O(n/B · log_{M/B}(n/B)) I/Os — optimal for any B, M.

---

## 8. Randomized Algorithms

### Las Vegas vs Monte Carlo

| Type | Correctness | Time | Examples |
|------|------------|------|---------|
| Las Vegas | Always correct | Expected poly | Randomized quicksort, hash tables |
| Monte Carlo | Correct w/ high prob | Always poly | Miller-Rabin, Freivalds, randomized rounding |

**Randomized quicksort**: Choose pivot uniformly at random. Via indicator variables:
```
E[comparisons] = Σ_{i<j} Pr[i and j are compared]
Pr[ranks i and j compared] = 2/(j-i+1)  (one is chosen as pivot before the other)
E[total] = 2 Σ_{i<j} 1/(j-i+1) = 2 Σ_{k=1}^{n-1} (n-k)/k+1 ≈ 2n ln n
```

### Streaming Algorithms

Process in one pass, O(polylog n) space:

| Problem | Algorithm | Space | Error |
|---------|-----------|-------|-------|
| Distinct element count | HyperLogLog | O(1/ε² + log log n) | ±ε relative |
| Frequency estimation | Count-Min Sketch | O((1/ε) log(1/δ)) | ε·‖a‖₁ additive |
| Heavy hitters (> εn) | Misra-Gries | O(1/ε) | Exact |
| ε-quantiles | Greenwald-Khanna | O((1/ε) log(εn)) | ε-additive rank |
| Set membership (lookup only) | Bloom filter | O(n log(1/ε)) bits | ε false positive rate |
| Set membership + delete | Cuckoo filter | O(n log(1/ε)) bits | ε false positive rate |
| Set membership, static | XOR filter | O(n log(1/ε)) bits | ε false positive rate, best space |

**HyperLogLog**: Hash elements to binary strings. Track leading zeros. 2^(max leading zeros) estimates distinct count. Use 2^b buckets to reduce variance. Redis `PFCOUNT`, BigQuery COUNT DISTINCT, Presto.

**Count-Min Sketch**: d×w matrix, d hash functions. Increment a[i][h_i(x)] for each row i. Query min(a[i][h_i(x)]). Error ≤ ε‖a‖₁ with prob ≥ 1-δ using d=log(1/δ), w=⌈e/ε⌉.

**Bloom filter**: Set membership with false positives, no false negatives. No deletion support. Used in: Cassandra SSTable index, Chrome malicious URL filter, Bitcoin SPV.

**Cuckoo filter** (Fan et al. 2014): Stores fingerprints in a cuckoo hash table. Supports deletion (Bloom filter cannot). Better cache performance than Bloom (fingerprints stored contiguously in arrays, not spread across k hash positions). Similar false-positive rates and space. Redis 4.0+ ships a Cuckoo filter module. The trade-off in one line: **Bloom = lookup only; Cuckoo = lookup + delete**.

**XOR filter** (Graf-Lemire 2019): Most space-efficient static filter — 1.23 bits per element at 1% false-positive rate, vs Bloom's ~9.6 bits. No deletion, no dynamic insertion. Build once from a fixed set; query in O(1). Useful when the set is known ahead of time (e.g., static blocklists, precomputed lookup tables).

---

## 9. NP-Completeness and Beyond

### The Reduction Framework

To prove X is NP-hard: **reduce FROM** known NP-hard Y **TO** X.
- Polynomial-time function f: instances of Y → instances of X
- y ∈ Y ⟺ f(y) ∈ X

```
NP-hard problem landscape:

SAT (Cook 1971)
   ↓ reduce to
3-SAT → Independent Set → Vertex Cover → Clique
3-SAT → 3-Coloring → Hamiltonian Cycle → TSP
3-SAT → Subset Sum → Partition → Knapsack (general)
```

### Common NP-Complete Problems

| Problem | Decision version | Notes |
|---------|-----------------|-------|
| SAT / 3-SAT | ∃ assignment satisfying formula? | Cook-Levin first NP-complete |
| Independent Set | ∃ IS of size ≥ k? | Vertex cover complement |
| Vertex Cover | ∃ VC of size ≤ k? | FPT: O(2^k · n) |
| Clique | ∃ clique of size ≥ k? | W[1]-hard parameterized |
| Hamiltonian Cycle | ∃ HC in graph? | TSP version adds weights |
| Graph 3-Coloring | Colorable with 3 colors? | NPC even for planar graphs |
| Subset Sum | ∃ subset with sum = T? | FPT via meet-in-middle |
| Partition | Split set into two equal halves? | Special case of subset sum |

### Approximation Algorithms

| Problem | Best approximation | Inapproximability |
|---------|-------------------|-------------------|
| Vertex Cover | 2-approx (maximal matching) | > 1.36 unless UGC |
| TSP (metric) | 1.5 (Christofides), 1.499... (Karlin-Klein-Oveis Gharan 2021) | > 220/219 unless P=NP |
| TSP (general) | No constant factor | Unless P=NP |
| Set Cover | Hₙ ≈ ln n (greedy) | Optimal up to constant (PCP) |
| MAX-3SAT | 7/8 (random assignment achieves this) | Optimal (PCP theorem) |
| k-Center | 2-approx (greedy) | > 2 unless P=NP |
| Knapsack | FPTAS: (1+ε) in O(n²/ε) | Admits FPTAS |

**PCP theorem** (Arora-Safra 1992, Arora-Lund-Motwani-Sudan-Szegedy 1992): NP = PCP(log n, 1). Implies hardness of approximation for many problems.

### Parameterized Complexity

| Problem | Parameter | Complexity | Algorithm |
|---------|-----------|------------|-----------|
| Vertex Cover | k (solution size) | FPT: O(2^k · n) | Bounded search tree |
| Feedback Vertex Set | k | FPT: O(4^k · n²) | Iterative compression |
| k-Clique | k | W[1]-hard | No f(k)·n^O(1) expected |
| Dominating Set | k | W[2]-hard | Even harder than W[1] |
| Treewidth (computation) | w (treewidth) | FPT: O(2^w · n) | Many NP-hard problems FPT on bounded treewidth |

**ETH** (Exponential Time Hypothesis): 3-SAT requires Ω(2^n) time. Rules out n^o(k) algorithms for k-Clique.

**SETH** (Strong ETH): k-SAT requires 2^((1-ε)n) for any ε>0. Implies fine-grained hardness of many polynomial-time problems (edit distance, LCS require Ω(n^(2-ε)) under SETH).

---

## 10. Theory Wins vs Cache Reality

Algorithms that look compelling on paper but underperform in practice — the gap between asymptotic analysis and hardware reality.

| Algorithm | Theory | Practice | Why |
|-----------|--------|----------|-----|
| Fibonacci heap | O(log n) decrease-key, O(E + V log V) Dijkstra | Slow | Cache-hostile pointer chasing; each node is a separately allocated object; working set thrashes L1/L2 |
| van Emde Boas tree | O(log log U) per op | Slow | Huge constant factors; recursive structure blows the cache; practical only for very large U (≥10⁸) |
| Suffix automaton | O(n) construction, O(n) space | Complex to implement | Suffix array + LCP array handles almost all the same problems, is simpler, and has better cache behavior |
| Treap / skip list | O(log n) balanced BST | Use `std::map` (red-black tree) | Mature RB-tree implementations are heavily tuned; treaps/skip lists have more pointer indirection |
| SPFA | O(V+E) average | Avoid in production | O(VE) worst case is easily triggered; Dijkstra + Johnson's reweighting is strictly better |
| Lazy segment tree | O(log n) range update + query | Good, but watch constants | Standard segment tree often faster in practice for simple range sums due to simpler inner loop |
| 4-Russian method | O(n²/log n) for boolean matrix multiply | Not used | Huge constant; BLAS-optimized O(n³) with SIMD beats it for all practical n |

**The pattern**: pointer-chasing data structures (linked structures, trees with separately allocated nodes) lose to contiguous arrays on modern hardware even when their asymptotic complexity is better. The L1/L2 cache miss cost (~12–40 cycles) dominates when the working set doesn't fit in cache.

**Production rule of thumb**: Trust asymptotic analysis for algorithm selection; distrust it for constant-factor comparisons. Profile before replacing a simple O(n log n) with a complex O(n) when n < 10⁶.

---

## Where These Algorithms Live in Production

| Algorithm | Codebase |
|-----------|----------|
| B+ trees | Every RDBMS index (PostgreSQL, MySQL, SQL Server, SQLite) |
| Hash tables (open addressing) | Python dict, Java HashMap, V8 object properties, Redis internals |
| Dijkstra | Google Maps, OSPF routing daemon, GPS navigation |
| Bidirectional Dijkstra | Road network routing (OSRM, Valhalla, HERE) |
| Union-Find | Kruskal's in network topology tools, Git merge-base, image segmentation |
| Aho-Corasick | clamav, Snort IDS, multiple-string grep |
| Suffix arrays | Full-text search (Elasticsearch uses inverted index with suffix-array ideas) |
| Bipartite matching | Kubernetes pod scheduling, resource allocation |
| HyperLogLog | Redis PFCOUNT, BigQuery/Presto COUNT DISTINCT, Spark cardinality |
| Count-Min Sketch | Network flow analysis (Cisco), database cardinality estimation |
| Bloom filters | Cassandra SSTable, Bitcoin SPV, Chrome safe browsing |
| Cuckoo filters | Redis modules, network packet filtering (deletion required) |
| TimSort | Python list.sort(), Java Arrays.sort() (objects), Android SDK |
| pdqsort | Rust std::sort, C++ Boost.Sort, Go (partially inspired) |
| Segment tree | PostgreSQL range types, game engines, competitive programming |
| KMP/Boyer-Moore | grep, vim `/`, database LIKE with trailing wildcard |
| Floyd-Warshall | Small routing tables, all-pairs in small graphs |

---

## Decision Cheat Sheet

```
Need:                                        Use:
────────────────────────────────────────     ──────────────────────────────────────────
Dynamic sorted set, predecessor queries      Red-black tree (std::map) or skip list
Static range min/max queries                 Sparse table: O(1) query
Dynamic range queries                        Segment tree or Fenwick tree
Shortest path, non-negative weights          Dijkstra O((V+E)logV)
Shortest path, point-to-point               Bidirectional Dijkstra (half the search)
Shortest path, negative edges                Bellman-Ford O(VE)
All-pairs shortest paths, dense             Floyd-Warshall O(V³)
All-pairs shortest paths, sparse            Johnson's O(V² log V + VE)
MST                                          Kruskal + DSU for sparse, Prim + heap for dense
Maximum flow                                 Dinic O(V²E); push-relabel for dense
Bipartite max matching                       Hopcroft-Karp O(E√V)
Min-cost bipartite matching                  Hungarian O(V³)
Single pattern search                        KMP or Z-algorithm
Multiple pattern search                      Aho-Corasick
Substring queries                            Suffix array + LCP or suffix tree
Distinct count, streaming                    HyperLogLog
Frequency count, streaming                   Count-Min Sketch
Set membership, lookup only                  Bloom filter
Set membership + deletion                    Cuckoo filter
Set membership, static, best space          XOR filter
Connected components, dynamic                Union-Find (DSU) O(α(n)) ≈ O(1)
NP-hard with small parameter k               FPT algorithm (Vertex Cover: O(2^k · n))
NP-hard, approximation needed                Check approximability: PTAS/FPTAS/constant ratio
```

---

## Common Confusion Points

**Hash table is O(1)** — average case with good hash + controlled load factor. Worst case O(n) when all keys collide. Python 3.3+ uses SipHash for dict/set (randomized per-process), defeating adversarial inputs.

**Dijkstra with negative edges** — does not work. A finalized node can later be reached via negative edge with shorter distance. Use Bellman-Ford or Johnson's reweighting.

**Amortized ≠ average case**: Amortized O(1) means n operations cost O(n) total; individual operations can cost O(n). Average case is expectation over random inputs. Both are valid but measure different things.

**Greedy correctness requires proof**: Greedy works for MST (cut/cycle properties), Huffman codes, activity selection, Dijkstra (non-negative). Does NOT work for knapsack, TSP, coin change with non-canonical denominations. Always prove exchange argument or greedy-stays-ahead lemma.

**NP-hard vs NP-complete**: TSP optimization (find minimum tour) is NP-hard but NOT in NP — you can't verify optimality in polynomial time. TSP decision (∃ tour ≤ k?) is NP-complete. Clique optimization is NP-hard but outside NP.

**Reduction direction**: To prove X is NP-hard, reduce FROM 3-SAT TO X. Not the other way. You're showing "if we could solve X in poly time, we could solve 3-SAT in poly time."

**Cache effects dominate at small n**: Insertion sort beats merge sort for n < 16 despite O(n²) vs O(n log n). A pointer-based BST loses to a sorted array for n < 100 due to cache misses. Profile before trusting asymptotic analysis for production code.

**Fibonacci heap in theory vs practice**: O(m + n log n) Dijkstra is theoretically optimal but Fibonacci heap's large constant factor and poor cache behavior means binary heap wins for n < 10⁶. Use binary heap in practice; Fibonacci heap is a theory tool.

**A* admissibility vs consistency**: Admissible heuristic (h ≤ true cost) guarantees finding the optimal path but may re-expand nodes. Consistent/monotone heuristic (triangle inequality on h) guarantees each node expanded at most once. For standard A* with a closed set, you need consistency — admissibility alone is not sufficient.
