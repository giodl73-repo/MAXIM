# Formal Methods — Landscape Overview

## The Big Picture

Formal methods sit on a spectrum from "add a little rigor" to "mathematically prove every property."
The spectrum is real — most industrial adoption lives in the middle, not at the extremes.

```
+------------------------------------------------------------------------------+
|                         FORMAL METHODS SPECTRUM                              |
|                                                                                |
|  LIGHTWEIGHT <───────────────────────────────────────────> HEAVYWEIGHT       |
|                                                                                |
|  TYPES &        MODEL           BOUNDED         DEDUCTIVE    FULL            |
|  LINTING        CHECKING        MODEL           PROGRAM      PROOF           |
|                                 CHECKING        ANALYSIS                     |
|                                                                                |
|  TypeScript     TLA+ TLC        CBMC            Dafny        Coq             |
|  Mypy           SPIN            KLEE            F*           Lean 4          |
|  Eslint         NuSMV           SAT-based       Infer        Isabelle        |
|  Rust types     Alloy                           VeriFast                     |
|                                                                                |
|  Cost:  LOW <───────────────────────────────────────────> VERY HIGH          |
|  ROI:   HIGH (just use it)       HIGH (protocols)         High (safety-crit) |
|  Scope: shallow/scalable         finite-state systems      full correctness    |
+------------------------------------------------------------------------------+
```

---

## The Three Pillars

Every formal method concerns itself with some combination of three activities:

```
+------------------------+    +------------------------+    +------------------------+
|     SPECIFICATION      |    |     VERIFICATION       |    |        PROOF           |
|                        |    |                        |    |                        |
|  Formally describe     |    |  Check that a model    |    |  Construct a rigorous  |
|  WHAT a system does,   |    |  satisfies a property  |    |  mathematical argument |
|  not HOW it does it.   |    |  (automatically).      |    |  (human + machine).    |
|                        |    |                        |    |                        |
|  Tools:                |    |  Tools:                |    |  Tools:                |
|  TLA+                  |    |  TLC (TLA+ checker)    |    |  Coq                   |
|  Z notation            |    |  SPIN                  |    |  Lean 4                |
|  Alloy                 |    |  NuSMV                 |    |  Isabelle/HOL          |
|  Event-B               |    |  CBMC / KLEE           |    |  HOL4                  |
|                        |    |  Z3 (SMT solver)       |    |                        |
|  Output:               |    |  Output:               |    |  Output:               |
|  Formal model          |    |  "Property holds" OR   |    |  Machine-checkable     |
|  of the design         |    |  concrete counterexmpl |    |  proof term            |
+------------------------+    +------------------------+    +------------------------+
          |                             |                             |
          +-----------------------------+-----------------------------+
                                        |
                              Most real-world work
                              combines all three
```

---

## Historical Arc

You already know the theory from MIT. Here is where the practical tooling came from:

```
1967  Floyd         Flowchart annotations — assign meaning to program states
                   (assertions on graph edges)

1969  Hoare         {P} C {Q} — the Hoare triple
                   "If P holds before C executes and C terminates, Q holds after."
                   Axiomatic semantics: rules for each language construct.

1975  Dijkstra      Weakest precondition calculus (wp)
                   wp(C, Q) = the weakest P such that {P} C {Q}
                   Turns proof obligations into predicate transformers.
                   Structured programming manifesto: "goto considered harmful."

1977  Cousot x2     Abstract interpretation — lattice-based dataflow analysis
                   The theoretical foundation for all static analyzers.

1981  Clarke,       CTL model checking — automated property verification
      Emerson,      over finite-state systems. Turing Award 2007.
      Sifakis

1983  Milner        CCS (Calculus of Communicating Systems)
                   Process algebra — formal model of concurrent computation.
                   Later: Pi-calculus (1992) — mobile processes, name passing.

1985  Bryant        Binary Decision Diagrams — canonical boolean functions,
                   enabling symbolic model checking at scale.

1992  Holzmann      SPIN released — LTL verification of concurrent protocols.
      (Bell Labs)   Still widely used for network protocols.

1994  TLA+          Lamport releases TLA+ — Temporal Logic of Actions.
      (Lamport)     State machines + temporal logic, practical for protocols.

2008  Z3            de Moura and Bjorner (Microsoft Research) release Z3.
      (MSR)         The SMT solver that powers most modern verification tools.

2005  CompCert      Xavier Leroy (INRIA) — fully verified C compiler in Coq.
                   Used in Airbus avionics.

2009  seL4          NICTA/CSIRO — verified microkernel in Isabelle/HOL.
                   10,000 LOC C formally verified to machine code.

2011  Infer         Calcagno et al. (later Facebook/Meta) — bi-abduction
                   with separation logic, finds bugs at industrial scale.

2014  AWS TLA+      Newcombe et al. — found critical bugs in DynamoDB, S3,
      (Newcombe)    EBS before they hit production. Published CACM 2015.

2017  Lean 4        Lean 4 redesign — fast, modern dependent type theory.
                   Mathlib now has >100,000 theorems (2024).

2024  AlphaProof   DeepMind — RL-trained model solving IMO-level math in Lean 4.
                   (Milestone: formal methods + ML convergence, not just toy benchmarks)
```

---

## The Three Tool Categories

### Category 1: Model Checkers

Exhaustively explore a finite-state model. Guaranteed to find violations if they exist
within the state space you explore.

```
  You write:    A model of your protocol (state machines, actions)
  You ask:      "Does this invariant always hold?"
                "Is deadlock reachable?"
                "Does every request eventually get a response?"
  Tool answers: YES (within explored states) OR
                NO + counterexample trace showing exactly how it breaks

  Key tools:
  +---------+  PROMELA language, LTL properties, works well for
  |  SPIN   |  concurrent protocols, partial order reduction
  +---------+

  +--------+  Temporal Logic of Actions, closest to
  |  TLA+  |  informal distributed systems thinking,
  |  (TLC) |  AWS/Azure use for protocol specs
  +--------+

  +--------+  BDD-based, good for hardware and control systems
  | NuSMV  |  (successor to SMV by Clarke)
  +--------+

  +--------+  Relational model, Alloy Analyzer, finds structural
  | Alloy  |  bugs in object/data models (bounded SAT)
  +--------+
```

### Category 2: Automated Analyzers

Work directly on code (not a separate model). Sound for specific property classes.

```
  You give:   Source code (C, Java, C#, etc.)
  You ask:    "Are there null pointer dereferences?"
              "Is this buffer access safe?"
              "Do these security properties hold?"
  Tool finds: Concrete bug reports with file/line/trace

  Key tools:
  +---------+  SAT-based, C code, memory safety, buffer overflow
  |  CBMC   |  AWS uses this on their C codebases at scale
  +---------+

  +-------+  Symbolic execution, C/LLVM, maximum code coverage
  | KLEE  |  finds crashes and assertion violations
  +-------+

  +-------+  Separation logic + bi-abduction, Java/C, Meta uses
  | Infer |  on every code review, finds null deref + memory leaks
  +-------+

  +--------+  C analysis platform, MISRA compliance, DO-178C,
  | Frama-C|  formal verification for safety-critical C code
  +--------+
```

### Category 3: Proof Assistants

You construct a machine-checked mathematical proof. High effort, maximum assurance.

```
  You write:   Formal spec + proof script (tactics)
  You get:     Machine-verified certificate of correctness
               (or "type error" if your proof is wrong)

  Key tools:
  +------+  Calculus of Inductive Constructions, OCaml extraction,
  | Coq  |  CompCert, four-color theorem, the verified C compiler
  +------+

  +--------+  Dependent type theory, Lean 4 is fastest modern PA,
  | Lean 4 |  Mathlib (>100k theorems), active ML community
  +--------+

  +----------+  Higher-order logic, Sledgehammer ATP integration,
  | Isabelle |  seL4 microkernel proof, most used in CS academia
  | /HOL     |
  +----------+
```

---

## Industrial Adoption — The Real Cases

### AWS: TLA+ at Scale (Newcombe et al., CACM 2015)

```
  Problem:  Distributed storage protocols (S3 versioning,
            DynamoDB replication, EBS volume management)
            are too complex to reason about informally.

  Approach: Write TLA+ specs of the algorithms.
            Run TLC model checker.

  Findings:
  - S3 versioning: subtle invariant violation
    (counterexample trace: 7 steps to reproduce)
  - DynamoDB: 3 bugs found during spec phase (before any code)
  - EBS: identified incorrect optimization that would have
    caused data loss under specific failure scenarios

  Quote from Newcombe:
  "Without TLA+, we would have shipped the DynamoDB bug."

  Scale: 10+ engineers trained. 7+ systems specified.
  Current: AWS continues using TLA+ for new protocol designs.
```

### Microsoft: Dafny and P for System Software

```
  Dafny:  Specification language + verifier built on Z3.
          Ghost variables, pre/post conditions, loop invariants.
          Used internally for algorithms and data structures.

  P:      Domain-specific language for async event-driven code.
          Model checking of distributed protocols.
          Used for USB 3.0 driver stack, Windows device drivers.
          Open-sourced 2022.

  SLAM/SDV: Static Driver Verifier in Windows DDK.
          CEGAR-based model checker for driver conformance.
          Found 3000+ driver bugs before Windows Vista shipped.
          Every Windows driver must pass SDV today.
```

### seL4: The Verified Microkernel (NICTA/CSIRO, 2009)

```
  What:    L4 microkernel family, ~10,000 lines of C.

  Proof chain (Isabelle/HOL):
    Abstract spec — what the kernel should do
         | functional correctness proof
         v
    Executable spec (Haskell) — deterministic implementation
         | refinement proof
         v
    C implementation — the actual kernel code
         | compiler correctness (CompCert-based)
         v
    Binary — the deployed executable

  Properties proven:
  - Functional correctness: C matches abstract spec
  - Integrity: unauthorized write access is impossible
  - Confidentiality: information cannot leak between partitions

  Deployed in: Northrop Grumman HALE UAS, DARPA HACMS program,
  F/A-18 aircraft (Boeing), seL4 Foundation (Linux Foundation)

  Cost: 11 person-years for initial proof.
  Verification effort roughly equals implementation effort.
```

### Airbus: B-Method and DO-178C Level A

```
  DO-178C Level A: "Failure would cause catastrophic consequences
  (loss of aircraft or crew)." Highest assurance level.

  B-Method:  Refinement-based specification method.
  Tool:      Atelier B (ClearSy).

  Used in:   Paris Metro Line 14 (driverless since 1998).
             Airbus A380/A350 fly-by-wire software.
             RATP (Paris transit) brake and door control.

  Why not Coq/Lean?
  - B-Method has qualified tooling for DO-178C
  - Tool qualification (the verifier itself must be certified)
    is enormous work. Atelier B has this; Lean 4 does not yet.
```

### Intel: CPU Formal Verification

```
  Post-Pentium FDIV bug (1994): Intel lost $475M.
  Since then: formal verification is standard for CPU design.

  Tools: Internal (Forte), commercial (JasperGold, Cadence)
  Scope: Instruction set conformance, cache coherence protocols,
         pipeline hazard freedom, power management state machines.

  Why CPUs are amenable:
  - Finite state machines with well-defined spec (ISA)
  - Property checking (not full correctness) is tractable
  - Model checking scales to register-transfer level
```

---

## The Gap Question: Why Isn't All Software Verified?

```
COST FACTORS:
+------------------+--------------------------------------------+
| Spec writing     | Writing a correct formal spec is as hard   |
|                  | as writing correct code. Bugs in the spec  |
|                  | mean the proof proves the wrong thing.     |
+------------------+--------------------------------------------+
| Proof effort     | seL4: 11 person-years for 10k LOC.         |
|                  | Most software: not safety-critical enough   |
|                  | to justify this ratio.                      |
+------------------+--------------------------------------------+
| Tooling maturity | Lean 4 Mathlib is excellent for math.      |
|                  | For software, library coverage is limited. |
|                  | OS interfaces, networking stacks, databases |
|                  | lack verified models.                      |
+------------------+--------------------------------------------+
| State explosion  | Model checkers: state space grows           |
|                  | exponentially with concurrent components.   |
|                  | 10 threads x 10 states each = 10^10 states. |
+------------------+--------------------------------------------+
| Undecidability   | Full program correctness is undecidable    |
|                  | (Rice's Theorem). All sound analyzers      |
|                  | approximate — false positives are real.    |
+------------------+--------------------------------------------+
| Human factors    | Engineers aren't trained in it.             |
|                  | TLA+ is not in most CS curricula.           |
|                  | Coq has a steep learning curve.             |
+------------------+--------------------------------------------+
```

Practical answer: lightweight formal methods (types, model checking of protocols,
bounded analysis of C code) have excellent ROI. Full proof is reserved for
safety-critical code where human lives and regulatory requirements demand it.

---

## Your MIT TCS Background: What Maps to What

```
MIT COURSE                     FORMAL METHODS RELEVANCE
──────────────────────────────────────────────────────────────────
Automata theory                MODEL CHECKING: Kripke structures ARE
(DFA, NFA, Buchi automata)     automata. LTL model checking reduces to
                               Buchi automaton intersection emptiness.

Formal language theory         SMT SOLVERS: decision procedures for
(regular, context-free,        fragments of first-order logic map
Chomsky hierarchy)             to recognizable languages (Presburger
                               arithmetic = Presburger automata).

Computability theory           UNDECIDABILITY: Rice's Theorem directly
(halting problem, Rice)        explains why no static analyzer can be
                               sound + complete + terminating.

Lambda calculus / type theory  PROOF ASSISTANTS: Coq's CIC is dependent
(STLC, System F)               type theory. Lean 4's type theory is
                               MLTT with universes. You have the base.

Logic (propositional, FOL)     SAT/SMT SOLVERS: DPLL is resolution
                               refutation for propositional logic.
                               Z3 extends this to theories over FOL.

Complexity theory              PRACTICAL LIMITS: SAT is NP-complete
(NP, PSPACE, co-NP)            but modern SAT solvers handle millions
                               of variables. Model checking is
                               PSPACE-complete (explicit state).
```

New concepts to add to your model:
- Temporal logics (LTL/CTL) — you know automata, this is a small extension
- SMT solving architecture (DPLL(T)) — new infrastructure, not new math
- Proof tactics and the tactic/term distinction in proof assistants
- Industrial specification patterns (TLA+, Z, Alloy notation)
- Separation logic — extends Hoare logic with frame rules for heap reasoning

---

## Tooling Summary Table

| Tool | Category | Input | Properties | Best For |
|------|----------|-------|------------|----------|
| TLA+ / TLC | Model checker | TLA+ spec | Safety, liveness, deadlock | Distributed protocols |
| SPIN | Model checker | PROMELA | LTL | Concurrent protocols |
| NuSMV | Model checker | SMV | CTL, LTL | Hardware, control systems |
| Alloy | Model checker | Alloy | Structural invariants | Data model correctness |
| CBMC | BMC | C/C++/Java | Memory safety, assertions | Embedded/AWS C code |
| KLEE | Sym. exec. | LLVM IR | Assertions, crashes | C/C++ coverage/bug finding |
| Infer | Abs. interp. | Java, C, C# | Null deref, memory leaks | Large codebases, CI |
| Z3 | SMT solver | SMT-LIB, APIs | Satisfiability | Backend for other tools |
| Frama-C | Analysis platform | C | Full functional (WP plugin) | Safety-critical C |
| Dafny | Deductive verifier | Dafny | Pre/post/invariants | Algorithms, data structures |
| Coq | Proof assistant | Gallina | Full correctness | Compilers, math, critical SW |
| Lean 4 | Proof assistant | Lean 4 | Full correctness | Mathematics, active research |
| Isabelle/HOL | Proof assistant | Isabelle | Full correctness | OS kernels, academia |

---

## Decision Cheat Sheet

| Situation | Tool / Approach |
|-----------|----------------|
| Designing a distributed protocol (consensus, replication) | TLA+ — write spec before code |
| Verifying concurrent protocol has no deadlock | SPIN (PROMELA) |
| Finding memory bugs in C before shipping | CBMC or Infer |
| Running bug-finding on every pull request | Infer or CodeQL |
| Verifying C safety-critical code (DO-178C) | Frama-C + WP plugin |
| Checking a data model for structural inconsistencies | Alloy |
| Need a machine-checked proof of an algorithm | Dafny (lighter) or Coq/Lean 4 (full) |
| Verifying an OS kernel / security property | Isabelle/HOL (seL4 approach) |
| Solving SMT constraints programmatically | Z3 Python API |
| Learning proof assistants | Lean 4 + Mathlib (best tooling 2024+) |

---

## Common Confusion Points

**"Model checking vs theorem proving — which is better?"**

Not the right question. They solve different problems:
- Model checker: exhaustive on finite state spaces, fully automated, gives counterexamples
- Theorem prover: works for infinite state spaces, requires human guidance, gives proofs
In practice: use model checking to find bugs, theorem proving to certify correctness.

**"Formal verification guarantees correctness"**

It guarantees the implementation matches the spec. If the spec is wrong, you've proven
the wrong thing. Garbage in, garbage out — the spec is the hard part.

**"This only works for small/toy programs"**

seL4 (10k LOC), CompCert (70k LOC), AWS S3/DynamoDB protocols (production scale).
The difficulty scales with proof depth, not raw LOC.

**"TLA+ requires a formal methods PhD"**

No. Lamport specifically designed TLA+ to be learnable by working engineers.
Newcombe 2015 describes engineers learning it without prior formal methods training.
The hardest part is writing a good spec — that is a design skill, not a math skill.

**"If the math is undecidable, verification tools cannot work"**

Rice's theorem says no tool can decide ALL semantic properties for ALL programs.
But specific properties (memory safety, null dereference) on bounded executions ARE
decidable. The art is choosing decidable fragments that match your actual requirements.
