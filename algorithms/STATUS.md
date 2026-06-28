# algorithms/ — Status

## Files

| File | Topic | Status |
|------|-------|--------|
| 00-OVERVIEW.md | Landscape: paradigms → analysis → data structures → the complexity frontier | ✅ |
| 01-ANALYSIS.md | Asymptotics, recurrences, Master/Akra-Bazzi, amortized, average-case, probabilistic | ✅ |
| 02-SORTING-SEARCHING.md | Comparison sorts, Ω(n log n) bound, non-comparison sorts, order statistics, search | ✅ |
| 03-DIVIDE-AND-CONQUER.md | Recurrence-driven design: merge/quick, Karatsuba, Strassen, FFT, closest pair | ✅ |
| 04-DYNAMIC-PROGRAMMING.md | Optimal substructure, overlapping subproblems, DAG-of-subproblems, classic DPs | ✅ |
| 05-GREEDY.md | Exchange argument, matroids, scheduling, Huffman; when greedy is provably optimal | ✅ |
| 06-DATA-STRUCTURES.md | Heaps, balanced BSTs, hash tables, segment/Fenwick trees, skip lists | ✅ |
| 07-UNION-FIND-AMORTIZED.md | Disjoint sets, path compression + union by rank, inverse-Ackermann, potential method | ✅ |
| 08-STRINGS.md | KMP, Z-algorithm, Rabin-Karp, tries, suffix arrays/trees/automata, Aho-Corasick | ✅ |
| 09-COMPLEXITY-AND-NP.md | P/NP/co-NP, reductions, NP-completeness, approximation, randomized classes | ✅ |

## Completed

2026-06-27 — All 10 content files written. General-purpose algorithm design and
analysis (CLRS / 6.046 scope) plus the data structures that make the bounds
achievable. Every complexity bound is stated as best/average/worst with the
governing precondition; stability and in-place properties are called out
explicitly per sort; amortized-vs-worst-case is distinguished everywhere it
matters (hash tables, dynamic arrays, union-find, Fibonacci heaps).

## Coverage Notes

This directory is the *general* algorithms-and-data-structures reference; all
graph-specific material (BFS/DFS, shortest paths, MST, flows, SCC, NP-hard graph
problems) lives in `graph-algorithms/` and is cross-referenced rather than
duplicated. The ordering is a design pipeline: paradigms and the analysis machinery
(`00`,`01`) come first because every later bound is read in that language; the
three workhorse paradigms — divide-and-conquer (`03`), dynamic programming (`04`),
greedy (`05`) — are framed as three points on a single "how do subproblems overlap
and how is the optimum assembled" axis; data structures (`06`,`07`) are the
amortized-cost engines that turn O(n²) naive loops into O(n log n); strings (`08`)
are the one combinatorial domain rich enough for its own toolkit; and complexity
(`09`) draws the line between what these techniques can and cannot reach.

Treatment is peer-level for a reader who knows Big-O, automata, reductions, and
the P-vs-NP landscape cold: no re-derivation of asymptotic notation, no "what is
an array." Preconditions are stated as theorems (comparison sorts cannot beat
Ω(n log n); quicksort is avg O(n log n)/worst O(n²); heapsort is O(n log n) but
not stable; counting/radix are non-comparison and escape the bound under integer-key
assumptions; hash-table operations are O(1) amortized *expected*, never worst-case).
Worked ASCII traces are checked step by step.

Key cross-references: `computing/26-ALGORITHMS.md` (the survey this directory
expands), `computing/21-AUTOMATA.md` (complexity classes underpinning `09`),
`graph-algorithms/` (all graph topics, especially `03`/`04`/`07` there for flows,
MST, and NP-hard graph problems), `programming-language-theory/` (Curry-Howard,
type-driven correctness, the lambda-calculus cost models behind functional DP),
`operations-research/` (LP/duality for approximation in `09`, scheduling in `05`,
network flows as the LP-dual of `graph-algorithms/06`), and `cryptography/`
(Rabin-Karp hashing in `08`, one-way functions and the average-case hardness
that `09`'s randomized classes lean on).
