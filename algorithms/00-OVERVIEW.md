---
maxim_schema: maxim.frontmatter.v1
id: maxim:algorithms:overview
kind: guide
module: algorithms
section: mathematics-physics
title: Algorithms - Landscape
status: source-custody
source_custody: partial
current_path: algorithms/00-OVERVIEW.md
canonical_path: algorithms/00-OVERVIEW.md
backsource_ids: [proof-backfill:algorithms:00-overview, git-history:algorithms:00-overview]
concepts: [algorithm design, paradigms, complexity analysis, data structures, divide and conquer, dynamic programming, greedy]
root_concepts: [algorithm design]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Algorithms — The Landscape

An algorithm is a *strategy for assembling an answer out of answers to smaller
pieces*, and the entire field is organized around two questions: **how do the
subproblems overlap**, and **how is the optimum assembled from them**. Those two
axes generate the three workhorse paradigms — divide-and-conquer, dynamic
programming, greedy — and everything else (the analysis machinery, the data
structures, the complexity boundary) exists to either *prove a strategy correct*
or *make it fast enough to run*. This directory is the general toolkit; anything
that lives on a graph (BFS/DFS, shortest paths, MST, flows, NP-hard graph
problems) lives in `graph-algorithms/` and is referenced here, never re-derived.

```
  algorithms/ : PARADIGMS  ->  ANALYSIS  ->  DATA STRUCTURES  ->  THE FRONTIER
  =================================================================================

   THE TWO AXES                         THE THREE PARADIGMS (03,04,05)
   +---------------------------+        +-----------------------------------------+
   | overlap?  subproblems     |        | 03 DIVIDE & CONQUER                     |
   |   none  -> D&C            |        |    disjoint subproblems, combine        |
   |   reuse -> DP             |        |    T(n)=aT(n/b)+f(n)  (Master thm)      |
   |                           |        | 04 DYNAMIC PROGRAMMING                  |
   | assembly? build optimum   |  -->   |    overlapping subproblems, memo/table  |
   |   one shot -> greedy      |        |    DAG of subproblems, optimal substr.  |
   |   all subs -> DP          |        | 05 GREEDY                               |
   |   recurse  -> D&C         |        |    one locally-best choice no backtrack |
   |                           |        |    proof: exchange argument / matroid   |
   +---------------------------+        +-----------------------------------------+
            |                                          |
            v                                          |
   01 ANALYSIS  (the language every bound is read in)
   +---------------------------------------------+
   | asymptotics | recurrences | amortized       |
   | Master/Akra-Bazzi | average-case | random   |
   +---------------------------------------------+
            |
            |  applied to concrete problems        each paradigm needs a fast
            v                                       substrate -> 06/07 DATA STRUCTURES
   02 SORTING & SEARCHING

   +---------------------------------------------+
   | comparison sorts: Omega(n log n) LOWER BOUND|
   | quicksort avg n log n / worst n^2           |
   | heapsort n log n (NOT stable)               |
   | counting/radix: NON-comparison, escape bound|
   | selection: O(n) median-of-medians           |
   +---------------------------------------------+

   +--------------------------------+
   | 06 heaps, balanced BST, hash,  |
   |    segment/Fenwick, skip list  |
   | 07 union-find: alpha(n) amort. |
   +--------------------------------+
        | special domain -> 08 STRINGS: KMP, Z, Rabin-Karp,
        v                               tries, suffix array/tree/automaton

            |
            +-------------------- all the above is "what we can do" ----+
                                                                        v
                                                  09 COMPLEXITY & NP — "what we cannot"
                                                  P / NP / co-NP, reductions,
                                                  NP-completeness, approximation,
                                                  randomized (RP/BPP/ZPP)
```

**Read this top-down**: pick a paradigm by how subproblems overlap (`03`–`05`),
state its cost as a recurrence or amortized bound (`01`), apply it to sorting and
searching as the canonical case study (`02`), implement it on a data structure
that makes the bound achievable (`06`,`07`), specialize to strings where the
structure is rich enough to demand its own toolkit (`08`), and finally locate the
problem relative to the P/NP frontier to know whether an *exact efficient* answer
is even possible (`09`).

---

## The Three Paradigms on One Axis

The paradigms are not a menu of unrelated tricks. They are three answers to the
same structural question.

```
                     "How do subproblems relate, and how do I assemble the answer?"

  DISJOINT subproblems          OVERLAPPING subproblems          NO subproblems —
  solved INDEPENDENTLY          REUSED across the tree           one GREEDY choice
  then COMBINED                 (memoize / tabulate)             commits the rest
        |                              |                                |
        v                              v                                v
  +--------------+              +--------------+                 +--------------+
  | DIVIDE &     |              | DYNAMIC      |                 | GREEDY       |
  | CONQUER (03) |              | PROGRAMMING  |                 | (05)         |
  |              |              | (04)         |                 |              |
  | mergesort    |              | edit distance|                 | Huffman      |
  | quicksort    |              | knapsack     |                 | activity sel.|
  |FFT, Karatsuba|              | matrix chain |                 | Kruskal/Prim*|
  | Strassen     |              | LCS, LIS     |                 | Dijkstra*    |
  +--------------+              +--------------+                 +--------------+
        |                              |                                |
  recursion tree                DAG of subproblems              proven by exchange
  has DISTINCT nodes            has SHARED nodes                argument or matroid
  => recurrence T(n)            => #states x work/state         => greedy-stays-ahead

  * Kruskal/Prim/Dijkstra are greedy algorithms that live in graph-algorithms/
    — listed here only to place them on the axis.
```

**The DP/D&C distinction is exactly subproblem overlap.** Mergesort's two halves
never share work, so it is divide-and-conquer with a clean recurrence. Naive
recursive Fibonacci *re-solves* `fib(k)` exponentially often — that overlap is the
signal to memoize, turning it into DP. Greedy is the degenerate case where you
never branch at all: one locally optimal choice provably extends to a global
optimum, so there is no subproblem tree to manage — but you owe a correctness
proof (exchange argument or matroid structure) because the claim is non-obvious.

---

## The Analysis Layer (what every bound is written in)

You know asymptotic notation; the point of `01-ANALYSIS.md` is the *machinery that
produces* the bounds, and three distinctions that trip up even strong engineers:

```
  WORST-CASE        vs   AVERAGE-CASE      vs   AMORTIZED
  -----------            ------------           ---------
  adversary picks        random input,          ANY sequence of ops,
  the input              expectation over it    total / #ops
                                                (no randomness needed)

  quicksort: O(n^2)      quicksort: O(n log n)  dynamic array push: O(1)
                                                amortized (not per-op!)
  guaranteed ceiling     typical behavior       guaranteed average over a
                         (can be unlucky)       sequence — a CONTRACT, not luck
```

- **Amortized ≠ average-case.** Average-case is an expectation over a *random
  input distribution* and can be defeated by an adversary. Amortized is a
  worst-case guarantee over a *sequence of operations* — no probability involved.
  A dynamic array's push is O(1) amortized for *any* push sequence; quicksort is
  O(n log n) average only if the input (or pivot) is random.
- **Expected vs worst.** A hash table is O(1) *expected amortized*, never O(1)
  worst-case — a malicious key set can collide everything into O(n). This
  distinction is load-bearing in `06` and in `09`'s randomized classes.
- **Recurrence solving** (Master theorem, Akra-Bazzi, recursion trees) is the
  engine behind every divide-and-conquer bound in `03`; the **potential method**
  is the engine behind every amortized bound in `06`/`07`.

---

## The Comparison-Sort Lower Bound (the field's cleanest impossibility)

Sorting is the canonical case study because it carries a *provable* lower bound
that separates "clever engineering" from "fundamental limit."

```
   A comparison sort only learns about the input through "is a[i] < a[j]?".
   Each comparison is a binary branch in a DECISION TREE.

                         a<b?
                        /     \
                     yes       no
                     /           \
                  b<c?          a<c?      ...  a tree of YES/NO comparisons
                  / \           / \
               abc  a<c?     bac  b<c?         LEAVES = the n! possible orderings
                    ...           ...

   A binary tree with n! leaves has height >= log2(n!) = Theta(n log n).
   Height = worst-case # comparisons.  => Omega(n log n).  No comparison sort beats it.
```

Counting sort, radix sort, and bucket sort run in O(n) — they do **not** violate
this, because they are *non-comparison* sorts: they read the key bits/values
directly and never ask "is a < b?". The bound only constrains the comparison
model. Knowing exactly which model a lower bound applies to is the difference
between "impossible" and "impossible *under these assumptions*" — the same move
that powers reductions in `09`.

---

## Old World → New World Bridges

These map prior art every senior engineer carries into the vocabulary here.

| You already know | In this directory it is |
|---|---|
| A `Dictionary<K,V>` / hash map "is O(1)" | O(1) **amortized expected**; worst-case O(n) under collisions — see `06` |
| `List<T>.Add` is "basically free" | O(1) **amortized** via geometric doubling; one resize is O(n) — see `01` |
| A query planner choosing a join order | Matrix-chain / DP optimization over an associativity tree — see `04` |
| A build system topologically ordering targets | A DAG of subproblems — the same shape DP fills in dependency order — see `04` |
| `OrderBy` / a B-tree index keeping data sorted | Balanced BST / comparison sort; the Ω(n log n) floor applies — see `02`,`06` |
| A priority queue / scheduler | Binary or Fibonacci heap; decrease-key cost drives Dijkstra — see `06` |
| "This regex is slow on adversarial input" | Catastrophic backtracking vs linear automaton matching — see `08` |
| "We can only approximate this NP-hard thing" | Approximation ratio + LP relaxation, formalized — see `09` |

The DP-as-DAG bridge is the single most useful one: any senior engineer has hand-rolled
a topological-order fill-in (build graphs, spreadsheet recalc, query plans). DP is
that, with the recurrence stating each node's value in terms of its predecessors.

---

## What Lives Here vs in graph-algorithms/

```
  algorithms/  (THIS directory — general)        graph-algorithms/  (separate)
  -------------------------------------          -----------------------------
  sorting, searching, selection                  BFS, DFS, topological sort
  divide & conquer (FFT, Strassen)               Dijkstra, Bellman-Ford, Floyd-Warshall
  DP on sequences/intervals/trees                MST (Prim, Kruskal)
  greedy + matroids (abstract)                   SCC, bridges, 2-SAT
  heaps, BST, hash, segment/Fenwick              max-flow / min-cut, matching
  union-find (the structure)                     NP-hard GRAPH problems (TSP, coloring)
  string algorithms                              spectral, planarity
  P/NP/approximation/randomized (general)
```

When a topic here has a graph instantiation, this directory states the abstract
result and points across: greedy/matroids (`05`) explain *why* Kruskal is optimal;
the DP-as-DAG framing (`04`) is the same DAG `graph-algorithms/02` topologically
sorts; the P/NP machinery (`09`) is what classifies the NP-hard graph problems in
`graph-algorithms/07`.

---

## How To Read This Directory

```
  Start ->  00 OVERVIEW (this file)        the map and the two axes
            |
            v
  Tools ->  01 ANALYSIS                     the language of every bound
            |
            v
  Case   -> 02 SORTING & SEARCHING          the canonical worked domain + lower bound
            |
            +--> 03 DIVIDE & CONQUER  ---+
            +--> 04 DYNAMIC PROGRAMMING  +--  the three paradigms (read together)
            +--> 05 GREEDY            ---+
            |
            v
  Engines-> 06 DATA STRUCTURES             make the bounds achievable
            07 UNION-FIND & AMORTIZED      the alpha(n) masterpiece + potential method
            |
            v
  Domain -> 08 STRINGS                      one rich combinatorial specialty
            |
            v
  Limit  -> 09 COMPLEXITY & NP              what is and isn't reachable
```

---

## Decision Cheat Sheet

| I need to... | Go to | Key result |
|---|---|---|
| Solve a divide-and-conquer recurrence | `01` | Master theorem / Akra-Bazzi |
| Tell amortized from average-case | `01` | sequence-guarantee vs input-expectation |
| Pick a sort with a stability guarantee | `02` | mergesort/Timsort stable; heap/quick not |
| Beat O(n log n) sorting | `02` | only via non-comparison (counting/radix), needs integer keys |
| Find the k-th smallest in O(n) | `02` | quickselect (avg) / median-of-medians (worst) |
| Multiply huge integers / polynomials fast | `03` | Karatsuba O(n^1.585) / FFT O(n log n) |
| Decide D&C vs DP | `00`,`04` | subproblems disjoint → D&C; overlapping → DP |
| Optimize over a sequence/interval/tree | `04` | optimal substructure + memo/table |
| Prove a greedy choice is optimal | `05` | exchange argument or matroid |
| Keep a dynamic min/max + decrease-key | `06` | binary heap; Fibonacci for O(1) decrease-key |
| Range query + point update in O(log n) | `06` | Fenwick (prefix) / segment tree (general) |
| Maintain disjoint sets near-constant time | `07` | union by rank + path compression → α(n) |
| Match a pattern in O(n+m) | `08` | KMP / Z-algorithm (linear, no backtracking) |
| Index all substrings of a text | `08` | suffix array (O(n log n)) / suffix automaton (O(n)) |
| Decide if a problem is hopeless exactly | `09` | reduce a known NP-complete problem to it |
| Get a provable bound on an approximation | `09` | approximation ratio / LP relaxation |

---

## Common Confusion Points

### "Quicksort is O(n log n)" — incomplete

Quicksort is **average** O(n log n) and **worst-case O(n²)** (already-sorted input
with a naive first-element pivot). Randomized pivoting makes the O(n log n) hold
*in expectation for any input*, but the worst case is still O(n²). Heapsort is
O(n log n) *worst-case* but **not stable** and has poor cache behavior. There is no
single "best" sort; `02` gives the full property matrix.

### "Hash tables are O(1)" — only amortized expected

O(1) is **amortized expected** under a good hash function and bounded load factor.
Worst-case is O(n) (everything collides), and an adversary who knows your hash can
force it — which is exactly why production hash maps use randomized/SipHash-style
hashing. Never quote hash-table O(1) as a worst-case guarantee in `09`-style analysis.

### "DP and divide-and-conquer are the same thing"

Both recurse on subproblems; the difference is **overlap**. Mergesort's halves are
disjoint (D&C, recurrence). Fibonacci/edit-distance subproblems recur exponentially
(DP, memoize). If your recursion tree has repeated nodes, you have a DP and naive
recursion is exponential; if every node is distinct, memoization buys nothing.

### "Greedy is just being lazy / heuristic"

A *correct* greedy algorithm is provably optimal — Huffman coding and MST are
greedy and exactly optimal. Greedy fails for 0/1 knapsack and general TSP. The
dividing line is structural (matroid / exchange property), covered in `05`; calling
greedy a "heuristic" conflates the proven cases with the failures.

### "Counting/radix sort break the Ω(n log n) bound"

They don't — they sidestep it. The Ω(n log n) bound is **only** for *comparison*
sorts. Counting/radix are non-comparison and assume integer keys in a bounded
range; their O(n) (really O(n+k) / O(d·(n+k))) holds under those preconditions,
which a general comparison sort cannot assume. See `02`.
