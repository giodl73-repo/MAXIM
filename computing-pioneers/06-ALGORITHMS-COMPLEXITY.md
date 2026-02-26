# Algorithms and Complexity — Dijkstra, Knuth, Cook, Karp

## Era Overview

```
ALGORITHMS AS A SCIENCE: 1950–1975
====================================

  Before 1950: Algorithms existed but were not studied systematically.
               No framework for comparing algorithms.
               No notion of computational complexity.

  1956 ─── DIJKSTRA: Shortest-path algorithm. First rigorous algorithmic analysis.
  1959 ─── DIJKSTRA: Shortest-span tree (Prim-Dijkstra).
  1961 ─── DIJKSTRA: Mutex/semaphore (concurrent programming primitives).
  1965 ─── KNUTH: TAOCP Vol 1 draft. "Big-O" notation standardized for CS.
  1968 ─── KNUTH: TAOCP Vol 1 published. Algorithm analysis as discipline.
  1968 ─── DIJKSTRA: "Go To Statement Considered Harmful" — structured programming.
  1971 ─── COOK: NP-completeness theorem. SAT is NP-complete.
  1972 ─── KARP: 21 classic NP-complete problems.
  1975 ─── KNUTH: TeX development begins (published 1978).
           Knuth publishes Concrete Mathematics (1989).
```

---

## Edsger Dijkstra (1930–2002)

### Bio Snapshot

Dutch mathematician and computer scientist. Leiden, Amsterdam, Eindhoven, Texas. One of the most quotable figures in computing — "Computer science is no more about computers than astronomy is about telescopes." Won Turing Award 1972. Wrote his scientific correspondence by hand on paper, mailed it to a distribution list (EWD — Edsger W. Dijkstra memos), and rejected email as degrading to the craft of thinking.

### Shortest-Path Algorithm (Dijkstra's Algorithm, 1956)

**Context**: Dijkstra was 26, working at the Mathematical Centre in Amsterdam. He needed to demonstrate the ARMAC computer at a public exhibition and chose a map problem as the display problem. He designed the algorithm in about 20 minutes (by his own account) without paper and pencil.

```
DIJKSTRA'S ALGORITHM
======================

  Input:  Weighted directed graph G = (V, E, w) with w ≥ 0,
          source vertex s.
  Output: Shortest-path distances d[v] from s to all v ∈ V.

  ALGORITHM:
    Initialize: d[s] = 0, d[v] = ∞ for all v ≠ s
                prev[v] = undefined
                Q = priority queue containing all vertices

    While Q is not empty:
      u = vertex in Q with minimum d[u]   ← EXTRACT-MIN
      Remove u from Q

      For each neighbor v of u:
        alt = d[u] + w(u, v)
        If alt < d[v]:
          d[v] = alt
          prev[v] = u                      ← RELAX

    Return d, prev

  COMPLEXITY:
    With binary heap: O((V + E) log V)
    With Fibonacci heap: O(E + V log V)  ← optimal for dense graphs
    With simple array: O(V²)             ← fine when V is small

  CORRECTNESS PROOF (informal):
    The key invariant: when u is extracted from Q, d[u] is final.
    Why? Because all remaining paths to u go through some vertex v
    still in Q with d[v] ≥ d[u] (since edge weights ≥ 0).
    Any path that first goes through v and then to u would be
    ≥ d[v] + something ≥ d[u]. So no shorter path can exist.
    This fails with negative weights (Bellman-Ford needed instead).
```

**Applications**:
- OSPF (Open Shortest Path First) — the dominant interior routing protocol for IP networks. Every router running OSPF is running Dijkstra's algorithm.
- GPS navigation — A* (A-star, 1968) is Dijkstra with a heuristic added. GPS uses bidirectional Dijkstra variants.
- Game pathfinding — nearly all game AI pathfinding is A* on a grid graph.

### Semaphores and Concurrent Programming (1965)

Dijkstra invented the **semaphore** as a synchronization primitive for concurrent processes. This is the foundation of all OS synchronization.

```
SEMAPHORE — DIJKSTRA'S DEFINITION
===================================

  A semaphore S is an integer with two atomic operations:

  P(S) / wait(S) / down(S):
    while S ≤ 0: wait   (block)
    S := S - 1

  V(S) / signal(S) / up(S):
    S := S + 1          (may wake a waiting process)

  MUTUAL EXCLUSION (mutex) with binary semaphore (S initialized to 1):
    P(S)      ← acquire
    critical section
    V(S)      ← release

  COUNTING SEMAPHORE (S initialized to N):
    Allows N concurrent accesses.
    E.g., a pool of N database connections.
    P decrements count; V increments count.
    P blocks when count = 0.
```

Dijkstra also proved the **Dining Philosophers** problem (1965) and formalized the **Banker's Algorithm** for deadlock avoidance. These remain the canonical examples in OS courses worldwide.

### Go To Considered Harmful (1968)

Dijkstra's letter to the editor of Communications of the ACM:

"The quality of programmers is a decreasing function of the density of go to statements in the programs they produce."

The argument: an unstructured `goto` makes it impossible to reason about a program locally. To understand any piece of code, you must track all possible paths that could have led to that point. Structured control flow (if/else, while, for, procedures) constrains these paths in ways that make programs comprehensible.

This letter is largely responsible for the structured programming revolution. By 1980, goto was effectively banned from polite company (except for error handling in C, where structured alternatives were worse). Every modern language's control flow design is a response to Dijkstra's argument.

---

## Donald Knuth (1938–present)

### Bio Snapshot

American mathematician and computer scientist. Case Institute of Technology, Caltech. Stanford. Turing Award 1974. Published The Art of Computer Programming (TAOCP) from 1968 to present — a multi-volume work on algorithms that he estimates will take his lifetime to complete. Also created TeX (the mathematical typesetting system), METAFONT, and literate programming. Famously took himself off email in 1990 because it was "destroying my ability to do research."

### The Art of Computer Programming

TAOCP is simultaneously:
- The most thorough reference on fundamental algorithms ever written
- An exercise in mathematical rigor applied to programming
- A work that has been "almost finished" since 1966

```
TAOCP — STRUCTURE AND SCOPE
=============================

  Volume 1: Fundamental Algorithms (1968)
    Basic programming concepts, data structures,
    number systems, information structures.
    The "MIX" assembly language (later MMIX — a RISC design).

  Volume 2: Seminumerical Algorithms (1969)
    Random number generation, arithmetic,
    number theory as applied to computation.

  Volume 3: Sorting and Searching (1973)
    Every practical and theoretical sort algorithm.
    Search trees, hashing, string matching.

  Volume 4A: Combinatorial Algorithms, Part 1 (2011)
    Bitwise tricks, combinatorial generation,
    satisfiability.

  Volume 4B: Combinatorial Algorithms, Part 2 (2022)
    More SAT, graph problems.

  Volumes 4C–7: In progress.

  FAMOUSLY: Bill Gates said "If you think you're a really
  good programmer... read [TAOCP]. You should definitely send
  me a resume if you can read the whole thing."
```

**Knuth's analytical contributions**:
- **Big-O formalization**: Knuth standardized the O, Θ, Ω notation for algorithm complexity in a form that is now universal. (O-notation predates him — Bachmann 1894, Landau 1909 — but Knuth made it the standard tool for CS.)
- **Knuth-Morris-Pratt (KMP) algorithm** (1977): Linear-time string matching. With Morris and Pratt.
- **Knuth-Bendix algorithm** (1970): Term rewriting, equational logic, unification — foundations of computer algebra systems.

### TeX

Knuth was disgusted by the typesetting quality of TAOCP's second edition (1976) — the new digital typesetting looked worse than hot metal type. He spent the next decade building TeX.

```
TEX — TECHNICAL DESIGN
========================

  TeX:       Typesetting engine. Precise box-and-glue model.
             Everything is positioned to ~1 nanometer precision.
             Stability guarantee: once a document typeset, always the same.

  METAFONT:  Font design system. Fonts as mathematical curves.
             Computer Modern fonts — universal in academic publishing.

  LaTeX:     Macro package on top of TeX (Lamport, 1984).
             THE document format for math, CS, physics papers.
             arXiv submits papers in LaTeX. ACM, IEEE, Springer all accept LaTeX.

  Why it matters:
    Every research paper the learner has ever read in a technical journal
    was probably typeset in TeX/LaTeX.
    The standard math rendering on the web (MathJax, KaTeX) renders TeX syntax.
    Jupyter notebooks render TeX math.
```

---

## Stephen Cook (1939–present)

### Bio Snapshot

American-Canadian mathematician. Harvard, Michigan, Berkeley, Toronto. Turing Award 1982. Published "The Complexity of Theorem Proving Procedures" in 1971 — the paper that founded modern complexity theory.

### NP-Completeness

**Context**: By the late 1960s, computer scientists had noticed that some problems seemed inherently hard — no matter how clever the algorithm, they seemed to require exponential time. Others were easy. No one had a framework for categorizing this.

```
THE COMPLEXITY CLASS HIERARCHY
================================

  P (Polynomial time):
    Problems solvable in O(nᵏ) for some constant k.
    Examples: sorting, shortest path, matrix multiplication,
              primality testing (AKS, 2002).

  NP (Nondeterministic Polynomial time):
    Problems where a proposed solution can be VERIFIED in polynomial time.
    (Equivalently: solvable in poly time by a nondeterministic TM.)
    Examples: SAT, Hamiltonian path, TSP, graph coloring, factoring*.

  NP-hard:
    At least as hard as the hardest problems in NP.
    (A poly-time algorithm for any NP-hard problem solves all of NP.)

  NP-complete:
    In NP AND NP-hard.
    The "complete" problems in NP: if any one is in P, all of NP is in P.

  P ⊆ NP  (trivially — any poly-time solvable problem has
            poly-time verifiable solutions)
  P = NP? The biggest open question in mathematics.

  *Factoring is in NP (easy to verify) but not known to be NP-complete.
   This is why RSA encryption works: factoring large numbers seems hard.
```

**Cook's Theorem (1971)**:

```
COOK'S THEOREM
===============

  Boolean Satisfiability (SAT):
    Given a Boolean formula, is there an assignment of
    truth values to variables that makes it true?

    Example: (x₁ ∨ x₂) ∧ (¬x₁ ∨ x₃) ∧ (¬x₂ ∨ ¬x₃)
    Satisfiable? Yes: x₁=T, x₂=F, x₃=T.

  Cook proved:
    1. SAT is in NP (a proposed assignment can be verified in poly time).
    2. Every problem in NP can be reduced to SAT in polynomial time.

  Therefore: SAT is NP-complete.

  The REDUCTION technique:
    To prove problem A is NP-hard, show that SAT (or any known NP-hard
    problem) can be transformed into A in polynomial time.
    If you can solve A efficiently, you can solve SAT efficiently.
    Since SAT is NP-hard, A must be NP-hard too.

  Cook's proof uses the fact that a nondeterministic Turing machine
  computation of polynomial length can be encoded as a SAT formula
  of polynomial size. Any NP problem = some NDTM computation = SAT.
```

---

## Richard Karp (1935–present)

### Bio Snapshot

American mathematician and computer scientist. Harvard, MIT, Berkeley. Turing Award 1985. Published "Reducibility Among Combinatorial Problems" (1972) — one year after Cook.

### The 21 NP-Complete Problems

Cook showed SAT is NP-complete. Karp showed that 21 specific combinatorial problems that had resisted efficient algorithms for decades were all NP-complete — all reducible to each other. This unified a huge swath of hard problems under one framework.

```
KARP'S 21 NP-COMPLETE PROBLEMS (1972)
=======================================

  From satisfiability:
    SAT → 3-SAT → CLIQUE → INDEPENDENT SET → VERTEX COVER
    SAT → 3-DIMENSIONAL MATCHING → SET PACKING → SET COVERING
    3-SAT → CHROMATIC NUMBER → CLIQUE COVER
    3-SAT → EXACT COVER
    3-SAT → HITTING SET → STEINER TREE → 3-DIMENSIONAL MATCHING
    3-SAT → KNAPSACK → JOB SEQUENCING → PARTITION
    PARTITION → MAX CUT
    3-SAT → DIRECTED HAMILTONIAN CYCLE → UNDIRECTED HAMILTONIAN CYCLE → TSP

  WHAT THIS MEANS IN PRACTICE:
    If you are trying to find a polynomial-time algorithm for any of these,
    you are (unknown to yourself) trying to prove P = NP.
    Stop and use approximation algorithms or heuristics instead.

  REAL-WORLD NP-COMPLETE PROBLEMS:
    Scheduling: job shop scheduling, exam timetabling
    Network: minimum spanning network design (with constraints)
    Logistics: vehicle routing, traveling salesman
    Circuit design: VLSI layout, register allocation
    Protein folding: simplified models
    Compiler: optimal register allocation is NP-hard in general
              (solved in practice with heuristics: graph coloring)
```

**Impact of Cook+Karp**: The combined result gave practitioners a clear signal: if your optimization problem is NP-complete, exact polynomial-time algorithms are almost certainly impossible (assuming P ≠ NP). You should look for:
1. Approximation algorithms (solutions within a factor of optimal)
2. Parameterized algorithms (efficient when some parameter is small)
3. Heuristics (fast in practice, no worst-case guarantee)
4. Exact algorithms for small instances

This is why every compiler has heuristic register allocators, every cloud scheduler uses greedy heuristics, and every TSP solver for real maps uses branch-and-bound with good lower bounds.

---

## Comparison Table

| Figure | Life | Key Result | Year | Impact |
|--------|------|-----------|------|--------|
| Dijkstra | 1930–2002 | Shortest path; semaphores; structured programming | 1956–1968 | Every router, every GPS, every mutex, every structured language |
| Knuth | 1938– | TAOCP; TeX; KMP; algorithm analysis | 1968– | Algorithm analysis framework; all technical publishing |
| Cook | 1939– | SAT is NP-complete | 1971 | Complexity theory; knew which problems to give up on |
| Karp | 1935– | 21 NP-complete problems | 1972 | Mapped the terrain of intractability |

---

## Who to Cite for What

| Concept | Figure |
|---------|--------|
| Shortest path (non-negative weights) | Dijkstra (1956) |
| Semaphore / mutex primitives | Dijkstra (1965) |
| Dining philosophers / deadlock | Dijkstra (1965) |
| Structured programming (no goto) | Dijkstra (1968) |
| Algorithm analysis notation (Big-O) | Knuth (standardized) |
| KMP string search | Knuth-Morris-Pratt (1977) |
| SAT NP-complete | Cook (1971) |
| NP-completeness reductions | Karp (1972) |
| P vs NP problem | Cook (1971 formulation) |

---

## Common Confusion Points

**"Dijkstra's algorithm works with negative edges."**
No. The greedy proof breaks: once a node is settled, a later negative edge could provide a shorter path. Use Bellman-Ford (O(VE)) for graphs with negative edges. Use Floyd-Warshall (O(V³)) for all-pairs with negative edges (no negative cycles).

**"If P = NP, all problems become easy."**
The question is whether P = NP — we don't know. If yes, it would mean every NP problem is solvable in polynomial time, but that polynomial could be n^10000, still impractical. The cryptographic implications would be severe regardless (public-key cryptography relies on NP-hard-adjacent problems).

**"TAOCP is a practical book."**
It is the most rigorous algorithmic reference in existence, not a practical guide to writing code quickly. It uses a custom assembly language (MIX/MMIX) for portability across decades. Most programmers cite it as the authority and refer to it for theoretical bounds; few read it cover-to-cover.

**"Structured programming means no goto in any context."**
Dijkstra's argument is about reasoning about programs. In C, the `goto` pattern for resource cleanup (jump to a common cleanup block at function end) is actually more structured than deeply nested if-else chains. Linux kernel code uses this pattern extensively. The argument is about what makes code comprehensible, not a blanket ban.
