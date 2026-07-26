---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "04-DYNAMIC-PROGRAMMING.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:algorithms:dynamic-programming
kind: guide
module: algorithms
section: mathematics-physics
title: Dynamic Programming
status: source-custody
source_custody: partial
current_path: algorithms/04-DYNAMIC-PROGRAMMING.md
canonical_path: algorithms/04-DYNAMIC-PROGRAMMING.md
backsource_ids: [mdloom-backfill:algorithms:04-dynamic-programming, git-history:algorithms:04-dynamic-programming]
concepts: [dynamic programming, optimal substructure, overlapping subproblems, memoization, tabulation, knapsack, edit distance, LCS]
root_concepts: [dynamic programming]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Dynamic Programming

Dynamic programming is divide-and-conquer where the subproblems **overlap** — the
recursion re-asks the same questions exponentially often, so you solve each once and
reuse it. The whole technique reduces to one slogan: **a DP is a DAG of subproblems,
and its running time is `(#subproblems) × (work per subproblem)`**. Get the DAG
right — states, transitions, evaluation order — and the complexity falls out
mechanically. Two structural preconditions must hold: *optimal substructure* and
*overlapping subproblems*.

```
  DYNAMIC PROGRAMMING = (a DAG of subproblems)
  =====================================================================================

   WHY DP (vs plain recursion)?  the recursion tree has REPEATED nodes:

        fib(5)                              -> the SAME subproblem fib(2), fib(3)...
       /      \                                appears many times. Naive = exponential.
    fib(4)    fib(3)                           Memoize -> each computed ONCE.
    /   \      /   \
  fib(3) fib(2) fib(2) fib(1)              COLLAPSE the tree into a DAG:
  /  \    ...     ...
 ...                                          fib(5) -> fib(4) -> fib(3) -> fib(2) -> fib(1)
                                                         \-------> fib(3) (reused)
   TWO PRECONDITIONS:
   1. OPTIMAL SUBSTRUCTURE  optimum of P built from optima of subproblems
   2. OVERLAPPING SUBPROBLEMS  same subproblems recur (else it's just D&C, see 03)

   TWO IMPLEMENTATIONS:                  COMPLEXITY:
   - TOP-DOWN (memoization): recurse +     time  = #states  x  work/state
     cache; natural, lazy, only touches    space = #states  (often reducible by
     reachable states                              keeping only last row/layer)
   - BOTTOM-UP (tabulation): fill table
     in dependency (topological) order
```

**Read this as a recipe**: define the state (what a subproblem *is*), the transition
(recurrence), the base cases, and the evaluation order (a topological sort of the
subproblem DAG). Everything else is bookkeeping.

---

## Layer 1: The Two Preconditions and the DAG Framing

```
   OPTIMAL SUBSTRUCTURE                     OVERLAPPING SUBPROBLEMS
   --------------------                     -----------------------
   The optimal solution to P contains       The recursion re-encounters the SAME
   optimal solutions to subproblems.        subproblem many times.

   shortest path: a shortest s->t path      fib(n): fib(n-2) computed by both
   that goes through v is (shortest s->v)    fib(n) and fib(n-1) -> exponential
   + (shortest v->t).                        re-solves without a cache.

   FAILS for LONGEST simple path             If subproblems DON'T overlap, you have
   (subpaths needn't be simple) -> NP-hard.  divide & conquer (03), not DP.
```

The DAG view makes the cost obvious: **vertices = distinct subproblems (states),
edges = dependencies (transitions)**. Evaluating the DP is a topological traversal
of that DAG — the very same topological order a build system uses (`graph-algorithms/02`).
Running time = `Σ_states (in-degree work)` = `#states × work/state`.

```
   THE FOUR-PART DP DESIGN
   1. STATE        what does a subproblem "remember"?  (the index/keys into the table)
   2. TRANSITION   recurrence: subproblem in terms of smaller subproblems
   3. BASE CASE    smallest subproblems answered directly
   4. ORDER        topological order to fill the table (or memoize top-down)
```

---

## Layer 2: One-Dimensional DP — Fibonacci to LIS

### Fibonacci — the minimal example of the collapse

```
   naive: T(n)=T(n-1)+T(n-2) = Theta(phi^n)  EXPONENTIAL (re-solves overlap)
   memoized / tabulated: each fib(k) once -> Theta(n) time, Theta(1) space (keep 2 values)

   table:  k:    0 1 2 3 4 5 6 7
           f(k): 0 1 1 2 3 5 8 13      each = sum of previous two
```

The exponential→linear collapse is the entire value proposition of DP: caching the
overlap.

### Longest Increasing Subsequence (LIS)

```
   STATE: dp[i] = length of LIS ENDING at index i.
   TRANS: dp[i] = 1 + max{ dp[j] : j < i and a[j] < a[i] }   (0 if none)
   answer = max_i dp[i].

   a   = [10, 9, 2, 5, 3, 7, 101, 18]
   dp  = [ 1, 1, 1, 2, 2, 3,   4,  4]
                         ^         ^ LIS length 4 (e.g. 2,5,7,18 or 2,3,7,101)
   #states n, work O(n) each -> O(n^2).  (A patience-sorting + binary search
   variant does O(n log n) — see 02 for the binary-search-on-predicate idea.)
```

---

## Layer 3: Two-Dimensional DP — Edit Distance, LCS, Knapsack

These are the workhorses; the table is a grid, the transition looks at a constant
number of neighbors.

### Edit (Levenshtein) distance — O(mn)

```
   STATE: dp[i][j] = min edits to turn A[1..i] into B[1..j].
   TRANS: if A[i]==B[j]: dp[i][j] = dp[i-1][j-1]
          else: 1 + min( dp[i-1][j]   (delete),
                         dp[i][j-1]   (insert),
                         dp[i-1][j-1] (substitute) )
   BASE:  dp[i][0]=i, dp[0][j]=j

   A = "SUNDAY"  B = "SATURDAY"        (answer = 3)
          ""  S  A  T  U  R  D  A  Y
       "" 0   1  2  3  4  5  6  7  8
       S  1   0  1  2  3  4  5  6  7
       U  2   1  1  2  2  3  4  5  6
       N  3   2  2  2  3  3  4  5  6
       D  4   3  3  3  3  4  3  4  5
       A  5   4  3  4  4  4  4  3  4
       Y  6   5  4  4  5  5  5  4  3   <- answer dp[6][8] = 3
   time O(mn), space O(mn) -> O(min(m,n)) keeping two rows.
```

### Longest Common Subsequence (LCS)

```
   STATE: dp[i][j] = LCS length of A[1..i], B[1..j].
   TRANS: A[i]==B[j] -> dp[i-1][j-1]+1   else max(dp[i-1][j], dp[i][j-1]).

   A="ABCBDAB" B="BDCABA"  ->  LCS length 4 (e.g. "BCBA" or "BDAB")
   time O(mn).  Backtrack through the table to recover the actual subsequence.
```

LCS is the engine behind `diff`, three-way merges, and `git`'s textual diffs — a
bridge any engineer who has read a code review touches daily.

### 0/1 Knapsack — and why greedy FAILS here

```
   STATE: dp[i][w] = max value using first i items within capacity w.
   TRANS: dp[i][w] = max( dp[i-1][w],                       (skip item i)
                          dp[i-1][w - wt[i]] + val[i] )      (take item i, if wt[i]<=w)

   items (wt,val): (1,1) (3,4) (4,5) (5,7)   capacity W=7
            w: 0 1 2 3 4 5 6 7
   item1(1,1):  0 1 1 1 1 1 1 1
   item2(3,4):  0 1 1 4 5 5 5 5
   item3(4,5):  0 1 1 4 5 6 6 9
   item4(5,7):  0 1 1 4 5 7 8 9   <- max value 9  (items (3,4)+(4,5))
   time O(nW)  -- PSEUDO-polynomial (W is a value, not input size). See 09.
```

**Greedy by value/weight ratio fails for 0/1 knapsack** — it works only for the
*fractional* variant (`05`). That failure is the textbook line between greedy and DP.

---

## Layer 4: DP on Intervals and Trees

### Matrix-chain multiplication — interval DP, O(n³)

Choosing the parenthesization that minimizes scalar multiplications. The optimum
over a sub-chain depends on a *split point*, so the state is an interval `[i..j]`.

```
   STATE: dp[i][j] = min cost to multiply A_i..A_j.
   TRANS: dp[i][j] = min over split k in [i,j-1]:
              dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]    (p = dimension array)
   BASE:  dp[i][i] = 0.
   Fill by increasing chain length.  #states O(n^2), work O(n) each -> O(n^3).
```

This is exactly what a query optimizer does choosing **join order** — the
associativity tree of joins is a matrix-chain over relation sizes. A senior
engineer's "the planner picked a bad join order" is a matrix-chain DP gone wrong.

### Tree DP — DP over a subproblem DAG that *is* a tree

```
   STATE: f(v) computed from f(children of v).  Post-order traversal = the topo order.
   e.g. max-weight independent set on a tree:
     incl(v) = w(v) + sum over children c of excl(c)
     excl(v) = sum over children c of max(incl(c), excl(c))
   answer = max(incl(root), excl(root)).   O(n) — one pass.
```

Tree DP makes the DAG framing literal: the dependency DAG is the tree itself, and
post-order is its topological sort.

---

## Layer 5: Memoization vs Tabulation, and Space Reduction

```
   TOP-DOWN (memoization)              BOTTOM-UP (tabulation)
   ----------------------              ----------------------
   recursive + cache                   iterative, fill table in topo order
   touches only REACHABLE states       fills ALL states (even unneeded)
   natural to write from recurrence    no recursion overhead, cache-friendly
   risk: stack depth on deep recursion easy to reduce space (drop old rows)
   lazy                                eager

   SPACE REDUCTION: if dp[i][*] depends only on dp[i-1][*], keep TWO rows -> O(width).
     edit distance: O(mn) -> O(min(m,n)).   knapsack: O(nW) -> O(W).
     (Hirschberg's trick recovers the actual alignment in O(m+n) space via D&C+DP.)
```

```
   WHICH IMPLEMENTATION?
   memoization  -> sparse reachable state space; recurrence is natural; few states touched
   tabulation   -> dense state space; want space reduction / no recursion limit; cache locality
```

---

## Old World → New World Bridges

| You already know | The DP concept |
|---|---|
| A build system topologically ordering targets | DP is a DAG of subproblems filled in topological (dependency) order |
| `git diff` / three-way merge | LCS / edit-distance DP over the two file versions |
| A query planner choosing join order | Matrix-chain DP over relation cardinalities |
| Spreadsheet recalculation order | Topological evaluation of a dependency DAG — same shape as a DP table fill |
| Memoizing an expensive pure function | Top-down DP: cache by argument tuple = the state |
| Viterbi decoding / HMM inference | DP over a trellis (state × time grid) — `machine-learning-theory/` |
| Regex/automaton matching | DP over (input position × NFA state) — `08`, `computing/21-AUTOMATA.md` |

The build-system bridge is the load-bearing one: any engineer who has reasoned about
"what must finish before this can start" already understands a DP's evaluation order
— DP just adds a *value recurrence* on top of the dependency DAG.

---

## Decision Cheat Sheet

| Problem shape | DP design | Complexity |
|---|---|---|
| Sequence, value-ending-here | dp[i] from dp[<i] (LIS) | O(n²) (or O(n log n)) |
| Two sequences aligned | grid dp[i][j] (edit dist, LCS) | O(mn) |
| Subset under a budget | dp[i][w] (knapsack) | O(nW) **pseudo-poly** |
| Best split of an interval | dp[i][j] over split k (matrix chain) | O(n³) |
| Optimum over a tree | f(v) from children, post-order | O(n) |
| Path/count on a grid | dp[i][j] from up/left neighbors | O(mn) |
| Subproblems *don't* overlap | use divide-and-conquer instead | go to `03` |
| Greedy choice provably optimal | use greedy instead (cheaper) | go to `05` |

---

## Common Confusion Points

### "DP is just recursion with a cache"

That is the *implementation* (top-down). The *insight* is the precondition pair —
optimal substructure and overlapping subproblems — plus identifying the right
**state** so the DAG is polynomial-sized. A cache on the wrong state explodes; the
hard part is the modeling, not the caching.

### "0/1 knapsack is O(nW), so it's polynomial"

It is **pseudo-polynomial**: W is a numeric *value*, and its encoding length is
log W bits, so O(nW) is exponential in the input *size*. 0/1 knapsack is NP-hard;
the DP is efficient only when W is small. This distinction (value vs encoding
length) is exactly the one that defines weak vs strong NP-hardness in `09`.

### "Greedy and DP solve the same problems"

Greedy is the special case where one locally optimal choice provably extends to the
global optimum (matroid/exchange structure, `05`) — then you skip the DP table.
0/1 knapsack and edit distance have *no* such structure, so greedy fails and DP is
required. Fractional knapsack *does* — greedy is optimal there. Same-looking problems,
different paradigm.

### "Bottom-up is always better than top-down"

Bottom-up avoids recursion overhead and enables space reduction, but it fills *all*
states even when only a sparse subset is reachable; top-down (memoization) touches
only reachable states, which can be a huge win on sparse DAGs. Choose by state-space
density and recursion-depth limits.

### "Optimal substructure always holds for optimization problems"

No — longest *simple* path has optimal-substructure failure (a subpath of a longest
simple path need not itself be a longest simple path, because of the simplicity
constraint), which is why it is NP-hard while shortest path is polynomial. Verifying
optimal substructure is a real proof obligation, not a formality.
