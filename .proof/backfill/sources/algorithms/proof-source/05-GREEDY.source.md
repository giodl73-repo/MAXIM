---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-GREEDY.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:algorithms:greedy
kind: guide
module: algorithms
section: mathematics-physics
title: Greedy Algorithms
status: source-custody
source_custody: partial
current_path: algorithms/05-GREEDY.md
canonical_path: algorithms/05-GREEDY.md
backsource_ids: [proof-backfill:algorithms:05-greedy, git-history:algorithms:05-greedy]
concepts: [greedy algorithms, exchange argument, matroid, huffman coding, activity selection, scheduling]
root_concepts: [greedy algorithms]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Greedy Algorithms

A greedy algorithm makes the locally optimal choice at each step and never
reconsiders. It is the cheapest paradigm — no subproblem table, no backtracking —
but it owes a **proof** that local optimality implies global optimality, because the
claim is false for most problems. The two proof techniques are the *exchange
argument* (greedy stays ahead of any optimal solution) and *matroid theory* (the
structural characterization of exactly when greedy is guaranteed optimal). Knowing
which problems have that structure is the entire skill.

```
  GREEDY: one irrevocable locally-best choice per step, never backtrack
  =====================================================================================

        +-----------------------------------------------------------------+
        | At each step: choose the option that looks best RIGHT NOW.      |
        | Commit. Never reconsider. -> O(n log n) typical (sort + scan).  |
        +-----------------------------------------------------------------+
                 |                                    |
        WHEN IT WORKS (provably optimal)     WHEN IT FAILS (only a heuristic)
        ----------------------------         --------------------------------
        activity selection                   0/1 knapsack (use DP, 04)
        fractional knapsack                  general TSP (NP-hard, 09 / graph-alg/07)
        Huffman coding                       longest path, set cover (only approx)
        MST: Kruskal, Prim (graph-alg/04)    coin change (non-canonical coin systems)
        Dijkstra (graph-alg/03)
        scheduling to minimize lateness
                 |
                 v
        WHY: two structural certificates
        +--------------------------+    +-------------------------------+
        | EXCHANGE ARGUMENT        |    | MATROID                       |
        | transform any optimal    |    | (E, I) with hereditary +      |
        | solution into the greedy |    | exchange property             |
        | one without worsening it |    | => greedy on weights is       |
        +--------------------------+    | OPTIMAL (Rado-Edmonds thm)    |
                                        +-------------------------------+
```

**The discipline**: greedy is trivial to *write* and treacherous to *trust*. Never
ship a greedy algorithm for an optimization problem without an exchange argument or a
matroid certificate — otherwise it is a heuristic, and you must say so.

---

## Layer 1: The Anatomy of a Greedy Algorithm

```
   greedy(items):
      sort items by some KEY                # the greedy criterion — choosing this is the design
      solution = empty
      for item in sorted order:
         if item is FEASIBLE with solution:  # respects the constraint
            add item to solution             # COMMIT — never undo
      return solution
```

Two ingredients define a greedy algorithm and both must be justified:

- **Greedy-choice property**: a globally optimal solution can be reached by a
  sequence of locally optimal (greedy) choices. *This is what you must prove.*
- **Optimal substructure**: after the greedy choice, the remaining subproblem is of
  the same kind and an optimal solution to it combines with the greedy choice. (Same
  property DP needs, `04` — greedy is the case where you also get greedy-choice, so
  you skip the table.)

---

## Layer 2: The Exchange Argument (the universal proof)

The exchange argument proves greedy optimal by showing **any** optimal solution can
be transformed, step by step, into the greedy one without ever getting worse.

### Activity selection — maximize non-overlapping intervals

```
   GREEDY CRITERION: always pick the activity that FINISHES EARLIEST among compatible ones.

   activities (start,finish):
      a1(1,4) a2(3,5) a3(0,6) a4(5,7) a5(3,9) a6(5,9) a7(6,10) a8(8,11) a9(8,12) a10(2,14) a11(12,16)
   sort by finish time:  4,5,6,7,9,9,10,11,12,14,16
   pick a1(.,4) -> next compatible start>=4: a4(5,7) -> next start>=7: a8(8,11) -> a11(12,16)
   SELECTED: a1, a4, a8, a11  (4 activities — optimal)

   timeline:  [a1==]   [a4=]    [a8==]      [a11==]
              1   4   5  7     8    11     12    16
```

**Exchange proof sketch**: let O be any optimal solution and g the
earliest-finishing activity. If O does not contain g, swap O's first activity for g
— g finishes no later, so it cannot conflict with anything O scheduled after, and
|O| is unchanged. Repeat. So a greedy solution is as large as any optimal one. ∎

### Scheduling to minimize maximum lateness

```
   GREEDY CRITERION: earliest deadline first (EDF).
   Exchange proof: any inversion (a later-deadline job before an earlier-deadline job)
   can be swapped without increasing max lateness. Removing all inversions yields the
   EDF schedule, so EDF is optimal.  -> classic exchange argument.
```

The exchange argument template: *assume an optimal solution differs from greedy at
the first choice; swap to match greedy; show it did not get worse; induct.*

---

## Layer 3: Huffman Coding (greedy that builds a tree)

Huffman builds an optimal prefix-free code by greedily merging the two
lowest-frequency symbols.

```
   frequencies: A:45  B:13  C:12  D:16  E:9  F:5
   repeatedly merge the two smallest into a subtree (a min-heap of weights, see 06):

   merge E(9)+F(5)=14         heap: A45 B13 C12 D16 [14]
   merge C(12)+B(13)=25       heap: A45 D16 [14] [25]
   merge [14]+D(16)=30        heap: A45 [25] [30]
   merge [25]+[30]=55         heap: A45 [55]
   merge A(45)+[55]=100       -> ROOT

                    (100)
                   /     \
                A:45      (55)
                         /    \
                      (25)    (30)
                      /  \    /   \
                   C:12 B:13 (14) D:16
                            /  \
                         F:5   E:9

   codes (left=0,right=1): A=0  C=100 B=101 F=1100 E=1101 D=111
   avg bits/symbol = sum(freq*depth)/100 = (45*1 + 13*3 + 12*3 + 16*3 + 9*4 + 5*4)/100
                   = (45+39+36+48+36+20)/100 = 224/100 = 2.24 bits   (optimal prefix code)
```

**Why greedy is optimal here (exchange)**: in an optimal prefix tree the two
lowest-frequency symbols must be siblings at maximum depth — if not, swapping them
down does not increase the weighted path length. So merging them first is safe, and
induction on the reduced alphabet finishes the proof. Huffman is the optimality
backbone of entropy coding — cross-ref `information-theory/` (Shannon's source-coding
bound) and `computing/`/`cryptography/` for the compression and encoding context.

---

## Layer 4: Matroids — the Structural Certificate

A matroid is the abstract structure that **guarantees** greedy is optimal, and it
explains *why* MST (Kruskal/Prim) and scheduling work while knapsack does not.

```
   A matroid M = (E, I): a ground set E and a family I of "independent" subsets with
     1. HEREDITARY:   A in I and B subset A  =>  B in I
     2. EXCHANGE:     A,B in I, |A|<|B|      =>  exists x in B\A with A+{x} in I

   RADO-EDMONDS THEOREM:
     For ANY weight function on E, the greedy algorithm
       (sort elements by weight desc; add each if it keeps the set independent)
     finds a MAXIMUM-WEIGHT independent set.
   <=> greedy is optimal for EVERY weighting   IFF   the structure is a matroid.

   EXAMPLES that ARE matroids:
     - graphic matroid: E = edges, independent = acyclic (forests)
       => greedy = KRUSKAL'S MST algorithm (graph-algorithms/04).  Optimal by Rado-Edmonds.
     - uniform / partition matroids: scheduling with deadlines.
   NOT a matroid:
     - knapsack feasibility (weight <= W) violates exchange  => greedy NOT optimal (use DP).
```

This is the deep answer to "when can I trust greedy?": **iff the feasible sets form
a matroid**, greedy is optimal for every weighting. Kruskal's correctness (`graph-algorithms/04`)
is literally the Rado-Edmonds theorem applied to the graphic matroid.

```
   GREEDY OPTIMALITY DECISION
   feasible sets form a matroid?       -> greedy optimal for all weights (Rado-Edmonds)
   exchange argument goes through?     -> greedy optimal for this problem
   neither?                            -> greedy is a HEURISTIC; bound it (09) or use DP (04)
```

---

## Layer 5: Where Greedy Fails (and what to do instead)

```
   PROBLEM                 GREEDY DOES                       CORRECT APPROACH
   -------                 -----------                       ----------------
   0/1 knapsack            ratio-greedy -> suboptimal         DP O(nW) (04)
   fractional knapsack     ratio-greedy -> OPTIMAL            greedy (matroid-like)
   coin change (canonical) largest-coin -> optimal (US coins) greedy works
   coin change (arbitrary) largest-coin -> can fail           DP
   general TSP             nearest-neighbor -> arbitrarily bad  approx / DP / B&B (09)
   set cover               most-coverage -> H(n)-approx        no better unless P=NP (09)
   vertex cover            -> 2-approximation via greedy       approximation (graph-alg/07)
```

The set-cover case is instructive: greedy is *not optimal* but it is the **best
possible** polynomial approximation (ratio `ln n`, tight unless P=NP). So "greedy
fails" sometimes means "greedy is the optimal *approximation*" — a result that lives
in `09`'s approximation theory.

### Worked failure: 0/1 knapsack defeats ratio-greedy

```
   items (wt,val): X(10,60) Y(20,100) Z(30,120)  capacity 50
   value/weight:   X=6.0    Y=5.0      Z=4.0
   ratio-greedy: take X (val 60), take Y (val 100) -> weight 30, value 160. Stop (Z won't fit).
   OPTIMAL: take Y+Z -> weight 50, value 220.   Greedy loses by 60.  -> use DP (04).
```

---

## Old World → New World Bridges

| You already know | The greedy concept |
|---|---|
| MST in a network designer (Kruskal/Prim) | Greedy on the *graphic matroid* — optimal by Rado-Edmonds (`graph-algorithms/04`) |
| Dijkstra in a routing layer | Greedy: always finalize the closest unsettled node (`graph-algorithms/03`) |
| A scheduler picking next-deadline jobs | Earliest-deadline-first, optimal by exchange argument |
| `gzip`/Huffman in a compressor | Greedy prefix-code construction, optimal entropy code (`information-theory/`) |
| LRU/cache eviction heuristics | Greedy heuristics — *not* always optimal (Belady's optimal is offline) |
| A load balancer's greedy bin-packing | Greedy bin-packing is a bounded *approximation*, not optimal (`09`) |

The MST bridge is the load-bearing one: a senior engineer trusts Kruskal because "it
works," and the matroid framing tells them *exactly why* it is provably optimal —
and why the same greedy instinct on knapsack or TSP is not.

---

## Decision Cheat Sheet

| Problem | Greedy criterion | Optimal? | Proof / else |
|---|---|---|---|
| Activity selection | earliest finish time | yes | exchange argument |
| Minimize max lateness | earliest deadline first | yes | exchange (swap inversions) |
| Huffman / prefix code | merge two least-frequent | yes | exchange on tree depth |
| MST | lightest safe edge | yes | graphic matroid (`graph-alg/04`) |
| Fractional knapsack | highest value/weight | yes | matroid-like exchange |
| Coin change (canonical) | largest coin first | yes (US/euro) | system-dependent |
| 0/1 knapsack | value/weight ratio | **no** | use DP (`04`) |
| General TSP | nearest neighbor | **no** | NP-hard; approx (`09`) |
| Set cover | max new coverage | **no** | best poly approx ln n (`09`) |
| Any weighting, feasible sets = matroid | by weight | **yes** | Rado-Edmonds |

---

## Common Confusion Points

### "Greedy is just a heuristic"

For *some* problems it is provably optimal — Huffman, MST, activity selection,
Dijkstra are exact. The word "heuristic" applies only where no exchange argument or
matroid structure exists (TSP, 0/1 knapsack). Calling all greedy "heuristic"
erases the proven cases; calling it "always optimal" is the opposite error.

### "If greedy gives the right answer on my examples, it's correct"

Examples prove nothing — greedy on 0/1 knapsack is right on many instances and wrong
on the (10,60)/(20,100)/(30,120) instance above. Correctness requires an exchange
argument or matroid certificate; otherwise you must treat it as an approximation and
bound the error (`09`).

### "Greedy and DP are different categories of problems"

They overlap. Greedy is the *special case of DP* where the greedy-choice property
holds, so you can commit to one choice instead of trying all of them — turning an
O(nW) table into an O(n log n) sort-and-scan. When greedy-choice fails, you fall back
to the full DP. Fractional knapsack (greedy) vs 0/1 knapsack (DP) is the same problem
family split by exactly this property.

### "Coin change is always greedy"

Only for *canonical* coin systems (like US/euro denominations) does largest-coin-first
give the minimum number of coins. For arbitrary denominations (e.g. {1,3,4} making 6),
greedy gives 4+1+1=3 coins but optimal is 3+3=2 — you need DP.

### "Matroid theory is academic, not practical"

The matroid certificate is the *operational* answer to "can I trust this greedy
algorithm for any input?" — yes iff the feasible sets form a matroid (Rado-Edmonds).
That is precisely why Kruskal's MST is guaranteed correct and a greedy knapsack is
not; it is the practical guardrail, not abstraction for its own sake.
