# Program Analysis

## The Big Picture

Program analysis covers the automated techniques for reasoning about code properties
without running the code. The intellectual core is abstract interpretation — a framework
unifying essentially all static analysis. The tools range from fast approximate analyses
(Infer, CodeQL) to deep deductive verifiers (Frama-C WP plugin).

```
+--------------------------------------------------------------------------+
|                       PROGRAM ANALYSIS LANDSCAPE                         |
|                                                                            |
|  TECHNIQUE           TOOLS              PROPERTIES         SCALE         |
|  ─────────           ─────              ──────────         ─────         |
|  Abstract            Astrée, Frama-C    Absence of         Safety-crit.  |
|  interpretation      (value analysis)   runtime errors     C (avionics)  |
|                                                                            |
|  Dataflow analysis   Clang SA, Infer    Null deref,        Any codebase  |
|  (flow-sensitive)    (flow-insens.)     resource leaks,    (scales well) |
|                                         uninitialized vars                 |
|                                                                            |
|  Symbolic execution  KLEE, angr,        Reachability,      C/binary      |
|                      S2E, Manticore     crashes, asserts   (moderate)    |
|                                                                            |
|  Separation logic    Infer (biabduct.)  Memory safety,     Java/C/ObjC   |
|                                         null deref,        (Facebook-    |
|                                         resource leaks     scale CI)     |
|                                                                            |
|  Taint analysis      CodeQL, FlowDagger Security info-     Java/Python/  |
|  (IFDS framework)    Semgrep            flow, SQL inject.  JS (CI)       |
|                                                                            |
|  Deductive           Frama-C WP,        Full functional    Safety-crit.  |
|  verification        Dafny, VeriFast    correctness        C (nuclear,   |
|                                                            aerospace)    |
+--------------------------------------------------------------------------+

  Fundamental tension:
  ┌────────────────────────────────────────────────────────────────────┐
  │  SOUNDNESS    No false negatives: if tool says "no bugs", none.    │
  │               (Conservative over-approximation.)                   │
  │  COMPLETENESS No false positives: if tool reports a bug, it's real.│
  │               (Precise under-approximation.)                       │
  │  TERMINATION  Tool always halts.                                   │
  │                                                                    │
  │  Rice's Theorem: you cannot have all three for non-trivial props.  │
  │                                                                    │
  │  Choose two:                                                       │
  │  Sound + Terminating    = possible false positives (Astrée, Infer) │
  │  Complete + Terminating = possible false negatives (testing, fuzzing│
  │  Sound + Complete       = may not terminate (semi-decision procs.) │
  └────────────────────────────────────────────────────────────────────┘
```

---

## Abstract Interpretation (Cousot & Cousot, 1977)

Abstract interpretation is the theoretical foundation for all sound static analysis.
It gives a framework for over-approximating program semantics in a way that is
provably sound.

### Galois Connections

The mathematical structure:

```
  Concrete domain (C, ⊆):   actual program states (sets of memory configurations)
  Abstract domain (A, ≤):   abstract representations (intervals, signs, polyhedra)

  Galois connection:  (C, ⊆) <──gamma──── (A, ≤)
                      (C, ⊆) ────alpha──> (A, ≤)

  alpha (abstraction): maps concrete to abstract  (best abstract approximation)
  gamma (concretization): maps abstract to concrete (what the abstraction means)

  Galois condition:
  alpha(c) ≤ a  iff  c ⊆ gamma(a)   for all c in C, a in A

  Soundness condition: alpha . gamma is the identity (or larger).
  gamma . alpha(c) ⊇ c  -- abstracting then concretizing over-approximates.

  If analysis is sound: the concrete behavior is a SUBSET of what the
  abstract analysis reports. Every real bug is covered; false positives possible.
```

### Abstract Domains

Different domains trade precision for efficiency:

```
  +------------------+-------------------------------------------+---------+
  | Domain           | Abstraction                               | Cost    |
  +------------------+-------------------------------------------+---------+
  | Signs            | x ∈ {negative, zero, positive, unknown}  | O(n)    |
  |                  | Coarse, fast. Good for div-by-zero.       |         |
  +------------------+-------------------------------------------+---------+
  | Intervals        | x ∈ [lo, hi]  (per variable)              | O(n)    |
  |                  | Tracks bounds. Buffer overflow.           |         |
  +------------------+-------------------------------------------+---------+
  | Octagons         | ±x ± y ≤ c  (pairwise constraints)       | O(n^2)  |
  |                  | More precision, catches more overflows.   |         |
  +------------------+-------------------------------------------+---------+
  | Convex polyhedra | General linear arithmetic constraints     | O(exp)  |
  |                  | Maximum precision for linear code.        |         |
  +------------------+-------------------------------------------+---------+
  | Shape analysis   | Heap structure (list, tree, DAG, cyclic)  | O(exp)  |
  |                  | Pointer safety, aliasing structure.       |         |
  +------------------+-------------------------------------------+---------+
  | Congruences      | x ≡ r (mod n)                             | O(n)    |
  |                  | Array alignment, stride patterns.         |         |
  +------------------+-------------------------------------------+---------+

  Combining domains: reduced product of abstract domains.
  Example: intervals + congruences captures both "x ∈ [0, 100]"
  and "x is even" simultaneously.
```

### Widening and Narrowing

Fixpoint computation for loops:

```
  Loop analysis problem:
  i = 0
  while i < n:
    i = i + 1

  Iteration of abstract semantics:
  Step 0: i ∈ {0}
  Step 1: i ∈ {0, 1}
  Step 2: i ∈ {0, 1, 2}
  ...  (does not converge for intervals)

  WIDENING operator (nabla):
  Speeds up convergence by jumping to a safe over-approximation.
  [a, b] nabla [c, d] = [ if c < a then -inf else a,
                           if d > b then +inf else b ]

  With widening:
  Step 0: [0, 0]
  Step 1: [0, 1]
  Step 2: [0, 1] nabla [0, 2] = [0, +inf]   <- widened to +inf
  Fixed point reached (check: next step is still [0, +inf]).

  Result: i ∈ [0, +inf]  -- sound (i can be anything from 0 up)

  NARROWING (delta): optional post-processing to tighten the result.
  Uses a few more concrete steps to recover precision lost by widening.
  After narrowing with the loop exit condition i < n:
  i ∈ [0, n-1]  -- tighter but still sound

  Trade-off:
  - Fewer widening steps: more false positives (imprecise)
  - More widening steps: slower but more precise
  - No widening: infinite iteration (does not terminate)
```

### Astrée: Sound Analysis at Scale

```
  Astrée (Cousot et al., 2003): industrial-strength abstract interpreter
  for safety-critical C code (avionics, automotive).

  Claim: zero false negatives for runtime errors (division by zero,
  buffer overflow, integer overflow, null pointer dereference).

  Verified: complete absence of runtime errors in 130,000+ lines of
  Airbus A380 primary flight control software. ZERO false negatives.
  False positive rate reduced to near zero through domain tuning.

  Key: the abstract domain is tuned specifically for avionics code
  patterns. Generic intervals work poorly; specialized relational
  domains + widening strategies handle the specific patterns.
```

---

## Dataflow Analysis

Dataflow analysis is abstract interpretation restricted to lattice-based, flow-sensitive
analyses. Every compiler optimization you know is a dataflow analysis.

### The Lattice Framework

```
  A dataflow analysis consists of:
  1. A lattice (L, ⊑) — the abstract domain
  2. A transfer function f_n: L -> L for each CFG node n
  3. A direction (forward or backward)
  4. A join operator (⊔) for merge points

  Fixpoint: iterate until no change.
  Because the lattice has finite height and transfer functions
  are monotone, this always terminates.

  ┌──────────────────────────────────────────────────────────────┐
  │  Forward analysis:  data flows from program start toward end │
  │  IN[n]  = JOIN over all predecessors p: OUT[p]               │
  │  OUT[n] = f_n(IN[n])                                         │
  │                                                              │
  │  Backward analysis: data flows from program end toward start │
  │  OUT[n] = JOIN over all successors s: IN[s]                  │
  │  IN[n]  = f_n(OUT[n])                                        │
  └──────────────────────────────────────────────────────────────┘

  Key analyses and their lattices:
  +---------------------------+----------+-----------+--------------------+
  | Analysis                  | Direction| Lattice   | What it computes   |
  +---------------------------+----------+-----------+--------------------+
  | Reaching definitions      | Forward  | 2^{Defs}  | Which defs reach   |
  |                           |          |           | each use           |
  +---------------------------+----------+-----------+--------------------+
  | Live variables            | Backward | 2^{Vars}  | Which vars are     |
  |                           |          |           | used after each pt |
  +---------------------------+----------+-----------+--------------------+
  | Available expressions     | Forward  | 2^{Exprs} | Which exprs are    |
  |                           |          |           | computed and valid |
  +---------------------------+----------+-----------+--------------------+
  | Constant propagation      | Forward  | Var->Const| Which variables    |
  |                           |          |           | have constant vals |
  +---------------------------+----------+-----------+--------------------+
  | Very busy expressions     | Backward | 2^{Exprs} | Exprs computed on  |
  |                           |          |           | all paths to exit  |
  +---------------------------+----------+-----------+--------------------+
```

### Reaching Definitions (Example)

```
  Code:
  1: x = 5
  2: y = x + 1
  3: if (...) {
  4:   x = 10
  5: }
  6: z = x + y

  Reaching defs at statement 6:
  - Definition of x: {stmt 1, stmt 4}   (both can reach stmt 6)
  - Definition of y: {stmt 2}           (only one def reaches stmt 6)

  Use: the compiler knows at stmt 6 that x might be 5 or 10.
  Application: constant folding, copy propagation, dead code elimination.
```

---

## Pointer and Alias Analysis

Pointer analysis answers: can two pointers refer to the same memory location?
This is fundamental for anything involving heap data.

### Andersen vs Steensgaard

```
  Two primary approaches, differing in precision vs speed:

  ANDERSEN (1994) — field-insensitive, flow-insensitive:
  Inclusion-based: if p = &x, then x is in pts(p).
                   if p = q, then pts(p) ⊇ pts(q).
  Propagates constraints to fixpoint.
  Complexity: O(n^3) in practice (near cubic).
  More precise: distinguishes which variables a pointer can point to.

  STEENSGAARD (1996) — unification-based:
  Union-find: if p = q, unify pts(p) and pts(q) into ONE set.
  Complexity: O(n * alpha(n)) — nearly linear.
  Less precise: groups too many pointers together (over-approximates aliasing).
  Used when speed matters more than precision (LTO, whole-program analysis).

  Field sensitivity: distinguishing p->x from p->y.
  Field-sensitive: more precise, higher cost.
  Field-insensitive: treats p->x and p->y as the same location.

  Context sensitivity: distinguish f() called from site A vs site B.
  Context-sensitive: more precise (k-CFA: k levels of call stack),
                     exponential in k in worst case.
  Context-insensitive (0-CFA): fast, less precise.

  Practical tools:
  LLVM's AA (alias analysis): default is semi-sparse flow-insensitive.
  Soot (Java): multiple pointer analysis frameworks.
  Infer: uses bi-abduction, which is context-sensitive.
```

---

## Taint Analysis and Information Flow

Taint analysis tracks the flow of untrusted data (sources) to dangerous operations
(sinks), through sanitizers that may clean the data.

### The Source-Sink-Sanitizer Model

```
  Source:     Where untrusted data enters
              - HTTP request parameters
              - Database reads (if DB is untrusted)
              - Environment variables
              - File contents

  Sink:       Where tainted data causes harm
              - SQL query execution   -> SQL injection
              - HTML output           -> XSS
              - exec() / system()     -> command injection
              - File path operations  -> path traversal
              - Deserialization       -> RCE

  Sanitizer:  Operations that remove the taint
              - HTML escaping / encoding
              - SQL parameterization
              - Input validation + rejection

  Analysis: track taint (a label) through the program.
  If tainted data reaches a sink without passing through
  a sanitizer: report a potential vulnerability.

  IFDS Framework (Reps, Horwitz, Sagiv 1995):
  Interprocedural Finite Distributive Subset problems.
  Taint analysis is an IFDS problem: the set of tainted variables
  at each point is the distributive combination of taints from
  all program paths reaching that point.
  Complexity: O(n^3) interprocedurally — polynomial and practical.
```

### CodeQL: Declarative Taint Analysis

```
  CodeQL (GitHub/Microsoft, originally Semmle):
  Represent the code as a queryable database.
  Write queries in QL (a Datalog-like language) over the code graph.

  Example CodeQL query (SQL injection in Java):
  import java
  import semmle.code.java.dataflow.TaintTracking
  import DataFlow::PathGraph

  class SqlInjectionConfig extends TaintTracking::Configuration {
    SqlInjectionConfig() { this = "SqlInjectionConfig" }

    override predicate isSource(DataFlow::Node source) {
      source instanceof RemoteFlowSource
    }

    override predicate isSink(DataFlow::Node sink) {
      sink instanceof QueryParameter  // SQL query parameter
    }
  }

  from SqlInjectionConfig config, DataFlow::PathNode source, DataFlow::PathNode sink
  where config.hasFlowPath(source, sink)
  select sink.getNode(), source, sink, "SQL injection from $@", source.getNode(), "user input"

  Deployed: GitHub Advanced Security (GHSA) runs CodeQL on
  millions of repos. Default queries cover OWASP Top 10.
  Custom queries: teams write domain-specific queries for
  their own security invariants.
```

---

## Symbolic Execution

Symbolic execution executes a program with symbolic (not concrete) inputs, maintaining
path conditions (constraints on the symbols) along each execution path.

### How It Works

```
  Concrete execution:
  int f(int x) {
    if (x > 0) return x * 2;
    else return -x;
  }
  f(5)  ->  returns 10  (one path, one answer)

  Symbolic execution:
  x = X (symbolic)
  Branch 1: X > 0 is TRUE  (path condition: X > 0)
    returns 2*X
  Branch 2: X > 0 is FALSE  (path condition: X ≤ 0)
    returns -X

  At each branch, the symbolic executor:
  1. Forks execution (takes both branches)
  2. Adds branch condition to path condition for each fork
  3. Queries SMT solver: "Is this path condition satisfiable?"
     If not: prune this path (unreachable).
  4. At error points: query "Is error reachable on this path?"

  Finding a bug: the SMT model is a CONCRETE INPUT that triggers the bug.
```

### KLEE: Symbolic Execution for LLVM

```
  KLEE (Cadar, Dunbar, Engler, Stanford 2008):
  Symbolic executor for LLVM bitcode (C/C++).

  What KLEE finds:
  - Assertion violations (assert() calls)
  - Buffer overflows (array out-of-bounds)
  - Null pointer dereferences
  - Division by zero
  - Use of uninitialized memory

  How to use:
  1. Compile with clang -emit-llvm
  2. Mark inputs as symbolic: klee_make_symbolic(&input, sizeof(input), "input")
  3. Run KLEE: klee program.bc
  4. KLEE generates: test cases for each path, error reports

  KLEE results (original paper):
  - Coreutils (GNU utilities): found 56 bugs in 96 programs
  - Busybox: found 21 crashes
  - Generated test suites with higher coverage than existing tests

  Path explosion problem:
  Each branch doubles the paths. n branches = 2^n paths.
  Mitigations:
  - Search heuristics: prioritize unexplored code (coverage-guided)
  - Merging: merge similar states at join points
  - Compositional analysis: analyze functions in isolation
  - Bounded: limit exploration depth / time
```

### Concolic Execution

Concrete + Symbolic execution combined (DART, CUTE, SAGE):

```
  Algorithm:
  1. Run concretely with random input -> get a concrete path
  2. Collect path condition along this path
  3. Negate last branch condition -> get a new path condition
  4. Solve with SMT -> get new concrete input that takes different path
  5. Run concretely with new input -> step 2

  Benefits:
  - Starts with concrete execution (handles complex code)
  - Avoids complex environment modeling (system calls, libraries)
  - Scales better than pure symbolic (no path explosion from concrete)

  SAGE (Microsoft Research, 2008):
  - Applied to binary programs (x86)
  - Found 1/3 of all Windows 7 security bugs
  - Still running internally at Microsoft (reportedly)
```

---

## Separation Logic and Infer

Separation logic (Reynolds 2002) extends Hoare logic with a * operator (separating
conjunction) that enables LOCAL REASONING about heap-manipulating programs.

### The Frame Rule

```
  Standard Hoare logic: compositionality fails for heap operations.
  If you have: {P} C {Q}
  You CANNOT conclude: {P * R} C {Q * R}  in general.
  Because: C might modify the heap locations described by R.

  Separation logic adds the frame rule:
  {P} C {Q}
  ──────────────────────────  (provided C does not modify vars(R))
  {P * R} C {Q * R}

  Separating conjunction P * Q:
  "The heap is split into two DISJOINT parts:
   one satisfying P, the other satisfying Q."

  This enables: prove C correct in isolation (with P, Q).
  Then apply the frame rule to add any R not touched by C.
  LOCAL REASONING: you only think about what C actually touches.

  Classic example:
  P = x -> 3 * y -> 5   (* x points to 3, y points to 5, disjoint *)
  C = [x] := 7          (* write 7 to the location x points to *)
  Q = x -> 7 * y -> 5   (* x now points to 7, y unchanged *)

  Frame with R = z -> 9:
  {x -> 3 * y -> 5 * z -> 9} C {x -> 7 * y -> 5 * z -> 9}
  -- z is unchanged because C only touches x's location.
```

### Infer: Bi-Abduction and Industrial Scale

```
  Infer (Calcagno et al., 2011 -> Facebook/Meta 2013):
  The key innovation: BI-ABDUCTION.

  Standard analysis problem:
  To analyze f() calling g(), you need the precondition of g.
  But g's precondition depends on how f calls it.
  Circular dependency -> interprocedural analysis is expensive.

  Bi-abduction solution:
  Given: {P} g() {Q} (some known spec for g)
  And: a call site where g is called with precondition P'

  Infer SIMULTANEOUSLY finds:
  - Anti-frame A: the extra precondition needed  (P' = P * A)
  - Frame F:      the extra postcondition that holds  (Q' = Q * F)

  This lets Infer analyze each procedure in isolation,
  then compose analyses bottom-up through the call graph.

  Result: sound, compositional, INTER-PROCEDURAL analysis
  that scales to millions of lines of code.

  What Infer finds:
  - Null pointer dereferences
  - Memory leaks (resource leaks)
  - Use after free
  - Thread safety violations (Race Detection mode)
  - Buffer overflows (with RacerD mode)

  Meta deployment:
  - Runs on EVERY diff (code review) for Facebook/Instagram/WhatsApp
  - Analyzes Java (Android), C/C++, Objective-C
  - ~1000 bugs found per month at Meta
  - False positive rate tuned to keep developer trust
  (sounds expensive; most bugs are automatically fixed suggestions)
```

---

## Frama-C: The C Analysis Platform

Frama-C (CEA LIST, INRIA) is a platform for multiple analyses of C code, using a
shared intermediate representation (Cil — C Intermediate Language).

### Architecture

```
  +──────────────────────────────────────────────────────────+
  │                       Frama-C                            │
  │                                                          │
  │  C source -> CIL normalization -> Kernel (AST + state)   │
  │                                                          │
  │  Plugins (each provides an analysis):                    │
  │                                                          │
  │  ┌────────┐  ┌─────────┐  ┌──────────┐  ┌──────────┐     │
  │  | Value  |  |   WP    |  |   EVA    |  | PathCrawler│   │
  │  |(abs.   |  |(deductive|  |(evolved  |  |(structural │   │
  │  | interp.)  | verif.) |  | value)   |  | coverage) │   │
  │  └────────┘  └─────────┘  └──────────┘  └──────────┘    │
  │       |           |              |              |         │
  │       └───────────┴──────────────┴──────────────┘        │
  │                         |                                 │
  │                   Shared kernel + annotations             │
  └──────────────────────────────────────────────────────────┘

  ACSL (ANSI/ISO C Specification Language):
  Annotations in C comments for specifying preconditions, postconditions,
  loop invariants, predicates.

  /*@ requires \valid(a + (0..n-1));
    @ requires n > 0;
    @ ensures \forall int i; 0 <= i < n ==> a[i] == \old(a[i]) || a[i] == v;
    @ ensures \exists int i; 0 <= i < n && a[i] == v;
    @*/
  void fill(int *a, int n, int v);
```

### WP Plugin: Hoare-Style Deductive Verification

```
  WP (Weakest Precondition) plugin:
  Given ACSL annotations, generates proof obligations.
  Sends obligations to SMT solvers (Alt-Ergo, Z3, CVC4).

  Workflow:
  1. Write C code
  2. Add ACSL annotations (preconditions, postconditions, invariants)
  3. Run Frama-C WP plugin
  4. SMT solvers discharge proof obligations automatically
  5. Remaining goals: handle manually or with Coq

  DO-178C qualification:
  Frama-C has been tool-qualified for DO-178C Level A by CEA LIST.
  Used in: French nuclear plant software (EDF), Airbus avionics,
  railway control systems (Alstom), automotive (AUTOSAR).

  Example use:
  - CEA LIST verified absence of runtime errors in C code
    for a railway interlocking system (~50,000 LOC C)
  - 98% of proof obligations automatically discharged
  - Remaining 2% discharged manually in Coq
```

---

## The Static Analysis Taxonomy

Putting it all together — what does each analysis technique guarantee?

```
  ┌────────────────┬──────────┬────────────┬───────────┬──────────────────┐
  | Technique       | Sound    | Complete   | Terminates | False Positives  |
  ├────────────────┼──────────┼────────────┼───────────┼──────────────────┤
  | Abs. interpret. | Yes      | No         | Yes        | Yes (tunable)    |
  | (Astrée)        |          |            |            |                  |
  ├────────────────┼──────────┼────────────┼───────────┼──────────────────┤
  | Infer           | Yes *    | No         | Yes        | Yes (low rate)   |
  | (bi-abduction)  | (* for   |            |            |                  |
  |                 |  analyzed|            |            |                  |
  |                 |  paths)  |            |            |                  |
  ├────────────────┼──────────┼────────────┼───────────┼──────────────────┤
  | Symbolic exec.  | Yes      | No         | No **      | No               |
  | (KLEE)          |          |            | (path expl)|                  |
  ├────────────────┼──────────┼────────────┼───────────┼──────────────────┤
  | BMC (CBMC)      | Yes      | Yes ***    | Yes        | No               |
  |                 |          | (within    |            |                  |
  |                 |          |  bound)    |            |                  |
  ├────────────────┼──────────┼────────────┼───────────┼──────────────────┤
  | Taint (CodeQL)  | No       | No         | Yes        | Low              |
  |                 | (heurist.)|           |            |                  |
  ├────────────────┼──────────┼────────────┼───────────┼──────────────────┤
  | Deductive verif.| Yes      | Yes        | Yes        | No               |
  | (Frama-C WP)    |          | (requires  |            | (but requires    |
  |                 |          |  annots.)  |            |  annotations)    |
  └────────────────┴──────────┴────────────┴───────────┴──────────────────┘
```

---

## Integration with Development Workflow

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │  FAST (seconds): Run on every commit                                 │
  │  - Type checker (already running)                                    │
  │  - Infer (on changed files)                                          │
  │  - CodeQL basic queries                                              │
  │  - Clang Static Analyzer                                             │
  ├──────────────────────────────────────────────────────────────────────┤
  │  MEDIUM (minutes-hours): Run on PR / nightly                          │
  │  - Full Infer analysis                                                │
  │  - CodeQL full query suite                                            │
  │  - CBMC for critical C modules (with proof harnesses)                │
  │  - KLEE for new algorithms                                            │
  ├──────────────────────────────────────────────────────────────────────┤
  │  SLOW (days-weeks): Run at milestones / pre-release                  │
  │  - Frama-C WP with ACSL annotations                                  │
  │  - Symbolic execution full coverage                                  │
  │  - Abstract interpretation (full program Astrée run)                 │
  ├──────────────────────────────────────────────────────────────────────┤
  │  ONE-TIME (months-years): Safety-critical certification               │
  │  - Full Coq/Lean proof                                                │
  │  - seL4-style proof chain                                             │
  │  - DO-178C Level A tool qualification                                 │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## Decision Cheat Sheet

| Situation | Tool / Technique |
|-----------|-----------------|
| Find null deref / resource leaks in Java on every PR | Infer (Meta's approach) |
| Find security vulnerabilities (SQL injection, XSS) in Java/Python/JS | CodeQL |
| Check memory safety of embedded C (buffer overflow, null) | CBMC or Infer |
| Need sound absence of runtime errors in safety-critical C | Frama-C + Value analysis or Astrée |
| Full functional correctness for certified C code (DO-178C) | Frama-C + WP plugin + ACSL |
| Find bugs in a new algorithm / data structure in C | KLEE (symbolic execution) |
| Pointer aliasing information for compiler optimization | LLVM AA (Andersen-based) |
| Track sensitive data flow (GDPR compliance, PII tracking) | Taint analysis (CodeQL or Semgrep) |
| Prove heap-manipulating code correct modularly | Separation logic + VeriFast or Infer |
| Full proof of complex algorithm (sorting, graph theory) | Coq or Lean 4 (deductive) |

---

## Common Confusion Points

**"Infer is sound, so it finds all bugs"**

Infer is sound for the properties it checks, but only for code it analyzes. It does
not analyze all code paths equally, does not model concurrency fully, and misses bugs
in code it abstracts away. "Sound" means it does not report false negatives for analyzed
paths. It does not mean "finds everything."

**"Symbolic execution is always better than fuzzing"**

For structured inputs with many branches: symbolic execution (KLEE) is better.
For complex formats, network protocols, large state spaces: fuzzing (AFL, libFuzzer)
scales better. Concolic execution (SAGE) bridges both. In practice, both are
complementary — run both for comprehensive coverage.

**"Abstract interpretation always has too many false positives"**

Astrée achieved near-zero false positives on Airbus A380 code by domain tuning.
The false positive rate depends heavily on which abstract domain is used and how
it is parameterized for the specific code base. Generic tools (Frama-C value analysis)
have higher false positive rates; tuned tools (Astrée) do not.

**"CodeQL is a static analyzer"**

CodeQL is a code query engine. It represents the code as a relational database and
lets you write queries in QL. Some queries implement static analysis (taint tracking);
others check code style, find API misuse, or search for patterns. It is a platform,
not a single analysis.

**"The frame rule in separation logic is just modular design"**

The frame rule is a PROOF RULE that enables modular formal reasoning. "Modular design"
is an informal principle. The difference: with separation logic, you can construct
machine-checked proofs that correctly reason about heap aliasing. Informal modularity
gives no such guarantee — you can convince yourself, but the checker cannot verify it.
