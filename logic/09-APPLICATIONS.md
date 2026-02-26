# Applications: Program Verification and AI Reasoning

## The Big Picture

Logic is the engineering foundation of formal verification, type theory, and AI knowledge
representation. SAT/SMT solvers power hardware verification, compiler analysis, and security
tools. Dependent type theory (Lean, Coq) produces machine-checked proofs. Description logics
underlie knowledge graphs and OWL ontologies.

```
+-------------------------------------------------------------------+
|              LOGIC IN ENGINEERING AND AI                          |
|                                                                   |
|  PROGRAM VERIFICATION        SAT / SMT SOLVING                   |
|  +--------------------+      +---------------------------+        |
|  | Hoare logic        |      | SAT: Boolean (CDCL)       |        |
|  | Weakest precond.   |      | SMT: theories over SAT    |        |
|  | Model checking     |      |  - EUF (equality + funcs) |        |
|  | Separation logic   |      |  - Arithmetic (LIA, LRA)  |        |
|  | Concurrency        |      |  - BitVectors             |        |
|  | Total correctness  |      |  - Arrays                 |        |
|  +--------------------+      |  - Strings                |        |
|                              | Tools: Z3, CVC5, Yices    |        |
|  TYPE THEORY / PROOF ASSISTANTS                                   |
|  +--------------------+      +---------------------------+        |
|  | Curry-Howard       |      | AI REASONING              |        |
|  | Martin-Lof TT      |      | +-----------------------+ |        |
|  | Calculus of Constr |      | | Knowledge graphs      | |        |
|  | Lean 4             |      | | Description logics    | |        |
|  | Coq / Rocq         |      | | OWL / RDF / SPARQL    | |        |
|  | Isabelle/HOL       |      | | Logic programming     | |        |
|  | Agda               |      | | Answer set programming| |        |
|  +--------------------+      | | Probabilistic logic   | |        |
|                              +-+-----------------------+-+        |
+-------------------------------------------------------------------+
```

---

**Formal verification lineage — from Code Contracts to Dafny**: The Hoare logic pipeline below has a direct lineage you may have encountered: Microsoft Research's **Spec#** (2004–2010) was a C# extension adding preconditions, postconditions, and object invariants as `requires`/`ensures`/`invariant` annotations, checked by the **Boogie** verifier (which translates to verification conditions discharged by Z3). **.NET Code Contracts** (shipped in .NET 4.0, 2010) were a library-level version of the same idea: `Contract.Requires(...)`, `Contract.Ensures(...)`, runtime checking + static analysis via cccheck. Both were direct Hoare-logic implementations: the annotation language IS the precondition/postcondition language, and the static checker IS a VC generator feeding an SMT solver.

The modern successor pipeline: **Dafny** (Rustan Leino, also from MSR) is Spec#'s intellectual heir — a language designed from the ground up for verification, compiling to Boogie → Z3. **Frama-C** does the same for C (using the ACSL annotation language → Why3 → multiple backends including Z3 and CVC5). The conceptual pipeline is identical to what Spec# did; the tooling matured substantially. If you wrote `[Requires]` annotations in .NET Code Contracts, you were writing Hoare preconditions.

## Hoare Logic and Program Verification

### Hoare Triples

```
  HOARE TRIPLE: {P} C {Q}

  P = precondition (predicate on state before C runs)
  C = command (program)
  Q = postcondition (predicate on state after C runs, assuming termination)

  Partial correctness: IF C terminates starting in a state satisfying P,
                       THEN the final state satisfies Q.
  Total correctness:   C DOES terminate, AND final state satisfies Q.
```

### Hoare Logic Rules

```
  SKIP:
     ─────────────────
     {P} skip {P}

  ASSIGNMENT:
     ──────────────────────────
     {Q[E/x]} x := E {Q}

     (Substitute E for x in Q to get the precondition)

  SEQUENTIAL:
     {P} C1 {R}    {R} C2 {Q}
     ─────────────────────────
        {P} C1; C2 {Q}

  CONDITIONAL:
     {P land B} C1 {Q}    {P land neg B} C2 {Q}
     ─────────────────────────────────────────────
     {P} if B then C1 else C2 {Q}

  WHILE (partial correctness):
     {I land B} C {I}
     ──────────────────────────────
     {I} while B do C {I land neg B}

     I = loop invariant

  CONSEQUENCE:
     P' => P    {P} C {Q}    Q => Q'
     ──────────────────────────────────
              {P'} C {Q'}
```

### Weakest Precondition Calculus (Dijkstra)

```
  wp(C, Q) = "weakest precondition": the largest set of states from which
              C is guaranteed to terminate with Q satisfied.

  wp(skip, Q)         = Q
  wp(x := E, Q)       = Q[E/x]
  wp(C1; C2, Q)       = wp(C1, wp(C2, Q))
  wp(if B then C1 else C2, Q) = (B -> wp(C1, Q)) land (neg B -> wp(C2, Q))
  wp(while B do C, Q) = ... (requires fixpoint: WF ordering for termination)

  For total correctness of while: need a loop VARIANT (decreasing natural number).
```

### Verification Conditions

Modern verification tools (Dafny, Frama-C, Why3) work by:
```
  1. Developer annotates program with invariants, pre/post conditions.
  2. VC generator computes verification conditions (logical formulas).
  3. SMT solver (Z3, CVC5) discharges the VCs automatically.
  4. If all VCs are valid: program is correct with respect to specification.

  PIPELINE:
  Annotated source
       |
       v  VC Generator (wp calculus)
  Verification Conditions (FOL formulas)
       |
       v  SMT Solver (Z3)
  VALID / COUNTEREXAMPLE
```

---

## Separation Logic

Standard Hoare logic cannot reason about heap-manipulating programs or concurrency.
Separation logic (O'Hearn, Reynolds, Yang 2001) extends it.

```
  NEW CONNECTIVE: "star" (*)

  P * Q   =   P and Q hold for DISJOINT parts of the heap.
  P -* Q  =   "magic wand": if we add a heap satisfying P, the combined heap satisfies Q.

  FRAME RULE (key innovation):
     {P} C {Q}
     ───────────────────────────── (where C does not touch vars in R)
     {P * R} C {Q * R}

  This allows LOCAL REASONING:
  Prove C correct on a small part of the heap (P),
  then "frame" to larger contexts without reproving.

  EXAMPLES:
  {x -> a} x.next := y {x -> y}    (x is a heap cell pointing to a)
  {x -> a * y -> b} swap(x, y) {x -> b * y -> a}

  SEPARATION LOGIC FOR CONCURRENCY (Concurrent Separation Logic):
  Threads own disjoint parts of the heap.
  Sharing is explicit (lock ownership).
  Races are statically excluded by type/logic.
```

---

## SAT Solving: Internals

You know from Module 01 that SAT is NP-complete and CDCL is the algorithm. Here is
how modern industrial solvers work:

```
  MODERN CDCL SOLVER (CaDiCaL, Kissat, MiniSat):

  +---------+    +-----------+    +-----------+    +----------+
  | Decide  | -> | Propagate | -> | Conflict? | -> | Analyze  |
  +---------+    | (BCP:     |    +-----------+    | (1-UIP   |
  Choose a       | unit prop)|         |           | scheme)  |
  literal        +-----------+         v           +----------+
  to assign.                      Backjump to           |
                                  level, add            v
                                  learned clause.   Learn new clause.
                                                    (add to clause DB)

  KEY METRICS:
  Decisions per second: 10^6 to 10^8
  Learned clauses: can be millions (periodic cleanup needed)
  VSIDS: bump variable score on each conflict; decay periodically.
  Restarts: periodic, to avoid getting stuck in bad search region.
```

### Preprocessing

Before search, modern solvers apply:
- **Variable elimination (VE)**: resolve out variables that appear few times.
- **Subsumption**: remove clauses subsumed by shorter ones.
- **Vivification**: strengthen clauses by testing subsets.
- **Inprocessing**: preprocessing applied during search (in CaDiCaL).

---

## SMT Solving

SMT (Satisfiability Modulo Theories) extends SAT with background theories.

```
  SMT ARCHITECTURE:

  SMT formula
      |
      v
  Preprocessor / Simplifier
      |
      v
  Boolean abstraction: replace theory atoms with Boolean variables
      |    (Tseitin if needed)
      v
  +-----------+            +-----------------+
  | SAT solver|  <-------> | Theory solvers  |
  | (DPLL/    |  query T   | T-SAT / T-UNSAT |
  | CDCL core)|  learn T-  | for each theory |
  +-----------+  clauses   +-----------------+

  COMBINED THEORIES (Nelson-Oppen method):
  Theories must be "stably infinite" and share sort signatures.
  Each theory solver handles its own atoms.
  Conflict propagation via shared equalities.
```

### Built-in Theories in Z3 / CVC5

```
  THEORY          EXAMPLE FORMULAS              USE CASE
  ─────           ────────────────              ────────
  QF_EUF          f(x)=y land f(y)=z -> f(x)=z  Equality + uninterpreted funcs
                  (congruence closure)

  QF_LIA          x + y < 5 land y > 2           Linear integer arithmetic
                  land x > 0

  QF_LRA          x + y <= 5.5 land y >= 2.3      Linear real arithmetic

  QF_NIA          x * x = 4                       Nonlinear integer arith.
                                                   (undecidable in general)

  QF_BV           (x bvand y) bveq 0              Bit-vector arithmetic
                  (bit-precise reasoning)

  QF_A            a[i] = v -> a[i] = v            Array theory (McCarthy)
                  (store/select axioms)

  QF_S            len(s) > 3 land prefix(s,"hi")  String theory
```

### Z3 in Practice

```python
  # Z3 Python API example
  from z3 import *

  x, y = Ints('x y')
  solver = Solver()
  solver.add(x + y > 5, x > 0, y > 0, x < 3)
  if solver.check() == sat:
      print(solver.model())   # prints x=2, y=4 (or similar)
  else:
      print("UNSAT")

  # Bit-vector reasoning
  bv = BitVec('x', 32)
  solver.add((bv & (bv - 1)) == 0)   # x is a power of 2
  solver.add(bv > 100)
```

---

## Program Verification Tools

```
  TOOL          LOGIC BASIS         LANGUAGE      USE CASE
  ────          ────────────        ────────      ────────
  Dafny         Hoare + ghost spec  Dafny         General programs, AWS
  Frama-C       Hoare + WP (Why3)   C             Safety-critical C
  Viper         Permission logic    Viper IR       Rust/Java verification
  VeriFast      Separation logic    C/Java         Heap-heavy code
  Why3          WP calculus         WhyML         Backend for many tools
  CBMC          BMC (SAT-based)     C/C++         Bug finding (bounded)
  Infer         Bi-abduction        C/Java/ObjC   Facebook/Meta, null deref
  SeaHorn       Horn clause CHC     C/LLVM        Safety verification
```

---

## Curry-Howard Correspondence in Depth

The isomorphism between proofs and programs (covered in Module 03, extended here):

```
  PROPOSITIONS AS TYPES:

  Proposition          Type
  ──────────          ────
  P -> Q              P -> Q   (function type)
  P land Q            P * Q    (product/pair type)
  P lor Q             P + Q    (sum/variant type)
  bot                 void     (empty type)
  top                 unit     (trivial type)
  neg P               P -> void

  PROOFS AS PROGRAMS:

  Proof of P -> Q     Lambda abstraction: fun (x: P) -> term : Q
  Proof of P land Q   Pair: (proof_P, proof_Q) : P * Q
  Proof of P lor Q    Injection: Left(proof_P) : P + Q
  Elimination (MP)    Function application: f(x)
  Normalization       Beta reduction

  CLASSICAL LOGIC:
  neg neg P -> P  (DNE)    corresponds to call/cc (continuations)
  P lor neg P (LEM)         corresponds to exceptions / control flow
```

### Dependent Type Theory

```
  DEPENDENT TYPES (Martin-Löf, 1973):
  Types can depend on VALUES.

  Pi type:  Pi (x: A). B(x)   = dependent function type
            (Forall x: A, B(x) in logic)
            Program: f(x: A) -> B(x)  (return type depends on input)

  Sigma type: Sigma (x: A). B(x)  = dependent pair type
              (Exists x: A, B(x) in logic)
              Program: (witness, proof) -- pair of a value and a proof about it

  EXAMPLES:
  Vec (A: Type) (n: Nat) : Type    (vector of As of length n)
  head : Pi (n: Nat). Vec A (n+1) -> A   (safe head: length > 0 is IN TYPE)

  LEAN 4 EXAMPLE:
  def head {α : Type} : (l : List α) → l.length > 0 → α
    | a :: _, _ => a
    | [], h => absurd h (Nat.not_lt_zero 0)
  -- The proof obligation (l.length > 0) is a program argument.
```

---

## Proof Assistants

```
  PROOF ASSISTANT    LOGIC BASIS              NOTABLE USES
  ────────────────   ──────────               ────────────
  Lean 4             CIC + mathlib4           Mathlib (100k+ theorems)
                     (Calculus of Ind. Constr) Fermat's Last Theorem proof
                                              (ongoing formalization)
  Coq / Rocq         CIC                      CompCert (certified C compiler)
                                              4-Color Theorem (Gonthier 2005)
  Isabelle/HOL       Higher-Order Logic       seL4 (verified microkernel)
                     + tactics                Archive of Formal Proofs
  Agda               Martin-Lof Type Theory   Cubical Agda (HoTT)
  Idris 2            Dependent types          Dependent-typed programming
  ACL2               First-order + induction  Floating-point verification (AMD)
```

---

## Knowledge Representation and Reasoning

**Relational-to-graph query bridge**: Knowledge graphs and SPARQL occupy the same conceptual space as relational databases and SQL, but with a different data model and a different formal semantics. The key differences and correspondences:

```
  RELATIONAL (SQL / Entity Framework)     KNOWLEDGE GRAPH (OWL / SPARQL)
  ─────────────────────────────────────   ─────────────────────────────────
  Table                                   Class (OWL: owl:Class)
  Row                                     Individual (ABox assertion)
  Foreign key                             Object property (RDF triple: s p o)
  Schema (DDL)                            Ontology / TBox (class + property defs)
  JOIN                                    Triple pattern matching in SPARQL
  NULL (absence)                          Open World Assumption: absence ≠ false
  Unique row identity (PRIMARY KEY)       IRI as global identifier
  SQL query → result set                  SPARQL SELECT → result bindings
  Stored procedure                        SPARQL CONSTRUCT / DESCRIBE
  CHECK constraint                        OWL class restriction (owl:maxCardinality)
  Foreign key constraint enforcement      Closed World reasoning (requires extra step)
```

The critical semantic difference: relational databases use **Closed World Assumption** (if a fact is not in the database, it is false — the database is complete). OWL/RDF uses **Open World Assumption** (if a fact is not asserted, it may still be true — the knowledge base is incomplete). This is why SPARQL queries can return surprising results: `ASK { :Alice :hasSibling :Bob }` can return false even if Alice exists, because Alice's siblings are simply not asserted, not because she has none. For the EF/SQL programmer: this is the opposite of `WHERE NOT EXISTS (...)` semantics — the OWA turns every such query into a maybe rather than a no.

### Description Logics and OWL

```
  KNOWLEDGE BASE = TBox + ABox

  TBox (terminology): class and property definitions
    Human sqsubseteq Animal
    Forall hasParent. Human sqsubseteq Human
    Exists hasSibling. top sqsubseteq Person

  ABox (assertions): individual facts
    Human(Alice), hasParent(Alice, Bob), Human(Bob)

  REASONING TASKS:
  Satisfiability:     Is the KB consistent?
  Subsumption:        Does Human sqsubseteq Animal hold?
  Instance checking:  Is Alice a Human?
  Retrieval:          Which individuals are Human?

  TOOLS: HermiT, Pellet, FaCT++ (OWL reasoners)
  LANGUAGE: OWL 2 (Web Ontology Language, W3C standard)
  USE CASES: Biomedical ontologies (GO, SNOMED CT), knowledge graphs
```

### Logic Programming

```
  PROLOG (1972):
  Knowledge base = Horn clauses
  Query = goal to prove

  ancestor(X, Y) :- parent(X, Y).
  ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

  parent(alice, bob).
  parent(bob, carol).

  ?- ancestor(alice, carol).   % true

  EXECUTION MODEL: SLD resolution (depth-first, left-to-right).
  Negation as failure: neg p succeeds if p fails to prove.
  Cut (!): prune search tree.

  DATALOG: Prolog without function symbols.
  Always terminates. Equivalent to relational algebra + recursion.
  Used in: Datomic, Souffle (program analysis), BigDatalog.
```

### Answer Set Programming (ASP)

```
  ASP extends Datalog with stable model semantics:
  Non-monotonic reasoning: rules can be overridden.
  Allows: negation as failure with self-defeating loops.

  Example (graph coloring):
    color(X, red) :- vertex(X), not color(X, blue), not color(X, green).
    color(X, blue) :- vertex(X), not color(X, red), not color(X, green).
    :- edge(X,Y), color(X,C), color(Y,C).   % constraint: adjacent = different colors

  Solver: Clingo (combines Gringo grounder + Clasp SAT solver)
  Applications: planning, scheduling, configuration, bioinformatics.
```

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Prove C is correct given specs | Hoare logic / Dafny / Frama-C |
| Reason about heap-manipulating programs | Separation logic / VeriFast / Viper |
| Automatically check safety of a finite system | Model checker (SPIN, NuSMV, TLA+/TLC) |
| Solve constraint satisfaction with arithmetic | SMT solver (Z3, CVC5) |
| Prove a mathematical theorem with machine-checking | Lean 4 / Coq / Isabelle |
| Write a type with dependent constraints (e.g., Vec A n) | Lean 4 / Agda |
| Query a knowledge graph | SPARQL + OWL / Description logic |
| Do logic programming / deductive query | Datalog / Prolog / Souffle |
| Find bugs in C without running it | CBMC (BMC) / Frama-C / Infer |
| Verify hardware | SAT-based BMC / IC3 (Cadence JasperGold) |

---

## Common Confusion Points

**Hoare logic partial vs. total correctness.**
{P} C {Q} (partial): IF C terminates AND P holds, THEN Q holds.
{P} C {Q} (total): P holds IMPLIES C terminates AND Q holds.
Most VCs you discharge with SMT are partial correctness. Total requires variant (termination).

**SMT vs. SAT.**
SAT handles Boolean formulas. SMT handles formulas with background theories (arithmetic,
arrays, strings). Z3 is an SMT solver that contains a SAT core plus theory solvers.
Z3 solves SAT problems too (it subsumes SAT).

**Lean vs. Coq vs. Isabelle.**
Lean 4 (Moura, 2021): dependent type theory, strongly growing mathlib. Best for pure math.
Coq (INRIA): Calculus of Inductive Constructions. Mature, used for CompCert.
Isabelle/HOL (Paulson): higher-order logic, good for system verification (seL4).
All three can write and verify formal proofs, but have different ergonomics and ecosystems.

**Datalog vs. Prolog.**
Datalog: no function symbols, always terminates, bottom-up (or top-down with tabling).
Prolog: allows function symbols (lists, trees), depth-first search, may not terminate.
Datalog is used in program analysis tools (DOOP, Souffle) because it guarantees termination.

**Description logics vs. FOL.**
DL is a decidable fragment of FOL. OWL 2 is based on SROIQ DL. Full FOL is undecidable.
Knowledge graphs (Wikidata, Schema.org) use a subset of OWL (OWL 2 EL is PTIME).
