# Model Checking

## The Big Picture

Model checking: automatically verify that a finite-state model satisfies a formal property.
The key word is automatically — no human-written proofs, just state space exploration.

```
+--------------------------------------------------------------------------+
|                        MODEL CHECKING LANDSCAPE                          |
|                                                                          |
|  INPUT          TECHNIQUE              TOOLS             USE CASE        |
|  ─────          ─────────              ─────             ────────        |
|                                                                          |
|  System model + EXPLICIT-STATE        SPIN (PROMELA)    Concurrent       |
|  LTL/CTL         BFS/DFS + Buchi      TLC (TLA+)        protocols        |
|  property        on-the-fly                                              |
|                                                                          |
|  System model + SYMBOLIC (BDD)        NuSMV/SMV         Hardware,        |
|  CTL property    image computation    Cadence JasperGold control systems |
|                                                                          |
|  C/C++ code +   BOUNDED (SAT/SMT)     CBMC              Embedded C,      |
|  assertions      unroll k steps       AWS CBMC           memory safety   |
|                  check as SAT         ESBMC                              |
|                                                                          |
|  Abstracted  +  CEGAR                 BLAST, SLAM        OS drivers,     |
|  C/Java code     refine on demand     CPAchecker         software model  |
|                                                                          |
|  SMT formula +  IC3/PDR               AVR, pono          Invariant       |
|  transition     property-directed     (hardware/SW)      inference       |
|  relation        reachability                                            |
+--------------------------------------------------------------------------+

  Fundamental limitation: STATE EXPLOSION
  n concurrent components with k states each = k^n total states
  Mitigation: BDDs (compact representation), partial order reduction,
              abstraction (CEGAR), symmetry reduction, BMC (bounded)
```

---

## Kripke Structures: The Semantic Foundation

A Kripke structure M = (S, S0, R, L) where:

```
  S  = finite set of states
  S0 = initial states (S0 ⊆ S)
  R  = transition relation (R ⊆ S × S) — total (every state has a successor)
  L  = labeling function L: S -> 2^AP (which atomic propositions hold where)

  Example: simple mutual exclusion protocol
  AP = {idle1, wait1, crit1, idle2, wait2, crit2}

  States and labels:
  s0: idle1, idle2
  s1: wait1, idle2
  s2: crit1, idle2
  s3: idle1, wait2
  s4: wait1, wait2
  s5: crit1, wait2    <- crit1 and wait2 can coexist
  s6: idle1, crit2
  s7: wait1, crit2    <- wait1 and crit2 can coexist
  (s8: crit1, crit2 is EXCLUDED by the mutex property)

  Safety property to check:
  AG -(crit1 /\ crit2)   "Mutual exclusion always holds"
  (In CTL: AG means "on all paths, globally")

  Model checker explores all reachable states,
  checks if the labeling ever violates the property.
```

### CTL Model Checking Algorithm (Polynomial Time)

CTL model checking uses a fixpoint computation. For M = (S, S0, R, L):

```
  To check AG p:
  1. Compute the set of states satisfying p: [[p]] = {s | L(s) |= p}
  2. Compute [[AG p]] as greatest fixpoint:
     Z0 = S (all states)
     Zi+1 = [[p]] ∩ pre*(Zi)  where pre*(X) = states whose successors ⊆ X
     Iterate until Zi+1 = Zi
  3. Check: S0 ⊆ [[AG p]]

  To check EF p:
  1. Compute [[p]]
  2. Compute [[EF p]] as least fixpoint:
     Z0 = ∅
     Zi+1 = [[p]] ∪ pre∃(Zi)  where pre∃(X) = states with some successor in X
     Iterate until Zi+1 = Zi
  3. Check: S0 ∩ [[EF p]] ≠ ∅  (some initial state can reach p)

  Complexity: O(|S| × |phi|)  — polynomial in the state space.
  CTL model checking is one of the few verification problems in P.
```

---

## Explicit-State Model Checking: SPIN

SPIN (Simple Promela Interpreter, Gerard Holzmann, Bell Labs 1992) is the canonical
LTL model checker for concurrent protocols.

### PROMELA: The Input Language

PROMELA (Process Meta Language) — concurrent processes communicating via channels:

```promela
/* Peterson's mutual exclusion algorithm */
bool flag[2];   /* flags: processes signal intent */
byte turn;      /* turn variable */

active [2] proctype P(byte id)
{
  byte other = 1 - id;
  do
  :: /* non-critical section, then attempt */
     flag[id] = true;
     turn = other;
     /* wait until: other not interested OR it's our turn */
     (flag[other] == false || turn == id);
     /* CRITICAL SECTION */
     assert(flag[other] == false || turn == id); /* mutual exclusion */
     flag[id] = false;
  od
}

/* LTL property: mutual exclusion */
ltl mutex { [] !(P[0]@critical && P[1]@critical) }

/* LTL property: starvation freedom */
ltl liveness { [] (flag[0] -> <> P[0]@critical) }
```

### LTL Checking in SPIN

```
  SPIN verification:
    spin -a peterson.pml     -> generates verifier (pan.c)
    gcc -o pan pan.c
    ./pan -a                 -> check all LTL properties

  What SPIN does:
  1. Build product automaton: system x negation of LTL property
  2. Search for accepting cycles (Buchi acceptance)
  3. If found: counterexample trace (full state sequence)
  4. If not found (within memory): property holds

  State vector: all values of all global/local variables
  SPIN compresses: state vector -> hash (detect visited states)
  Partial order reduction: skip equivalent interleavings

  Scale: typically handles 10^7 - 10^8 states
         with 100M+ state space: need abstraction or BMC
```

### On-the-Fly Verification

SPIN uses on-the-fly verification — it interleaves the automata product construction
with the search, rather than building the full product first:

```
  Standard approach:         On-the-fly:
  Build product automaton    Generate states on demand
  (can be huge)              during DFS search
       |                     Report counterexample
       v                     immediately when found
  Search for accepting cycle
                             Avoids materializing the full
                             product automaton in memory.
```

---

## BDD-Based Symbolic Model Checking

BDDs (Binary Decision Diagrams) represent boolean functions as canonical DAGs.
The key to symbolic model checking: represent sets of states as BDDs.

### BDD Structure

```
  Variable ordering: x1 < x2 < x3 < x4

  Function f(x1,x2,x3) = (x1 /\ x2) \/ (x3)

  As a BDD (reduced, ordered):
           x1
          /  \
        (0) x2
            / \
          (0) x3
              / \
           x3  (1)
           /\
         (0)(1)

  Canonical form: unique for each function given a variable order.
  Key operations: AND, OR, NOT, EXISTS, FORALL — all polynomial in BDD size.
  Key problem: variable ordering can make BDD exponentially large or linear.
               Good orders: related variables together.
```

### Symbolic CTL Model Checking

```
  Represent:
  - Set of initial states S0   as BDD_init
  - Transition relation R      as BDD_trans (over current+next state vars)
  - Property formula phi       as BDD_phi

  Image computation:
  pre∃(X) = {s | ∃s'. R(s,s') /\ s' ∈ X}
           = ∃vars'. (BDD_trans /\ X[s/s'])

  AG p computation:
  Z = S (all states = true BDD)
  loop:
    Z_new = p /\ pre_universal(Z)   where pre_universal = pre∃ of complement
    if Z_new = Z: done
    Z = Z_new

  This eliminates explicit state enumeration entirely.
  A 10^20 state system can sometimes fit in a 10^6 node BDD.

  NuSMV: the standard BDD-based model checker.
  SMV language (hierarchical modules, synchronous/asynchronous):
  CUDD library: the most-used BDD implementation.
```

### Variable Ordering Problem

```
  Bad ordering (x1,x3,x5,...,x2,x4,x6,...):
  BDD can be exponential in the number of variables.

  Good ordering (x1,x2,x3,...):
  BDD is polynomial for many common functions.

  Heuristic orderings: interleave related variables,
  use static analysis to find dependencies.
  Dynamic reordering: sifting algorithm during construction.

  Pathological case: multiplication function — no polynomial-size
  BDD exists regardless of variable ordering. This is why BDD-based
  verification hit a wall for arithmetic-heavy hardware.
```

---

## Bounded Model Checking (BMC)

BMC unrolls the system k steps forward and encodes the resulting formula as a SAT
instance. No Buchi automata needed — just propositional logic.

### The Encoding

```
  System M, property phi, bound k:

  BMC(M, phi, k):
    Encode as propositional formula:
    I(s0) /\ T(s0,s1) /\ T(s1,s2) /\ ... /\ T(sk-1,sk)
    /\ -phi(s0) \/ -phi(s1) \/ ... \/ -phi(sk)

    where:
    I(s0)       = initial state constraint
    T(si, si+1) = transition relation unrolled
    -phi(si)    = negation of property at step i

    Send to SAT solver.
    SAT:   there IS a path of length <= k violating phi
           (SAT model = counterexample trace)
    UNSAT: no violation in k steps
           (increase k to gain more confidence)

  Key advantage: SAT solvers are very good at this.
  Key limitation: cannot prove correctness (only bounded safety).

  Completeness threshold: if k >= completeness_threshold(M, phi),
  then UNSAT => phi holds for ALL paths.
  Computing completeness threshold is hard in general.
```

### CBMC: C Bounded Model Checker

CBMC (Daniel Kroening, ETH Zurich) applies BMC directly to C/C++ programs:

```
  Input: C source code + assertions (or implicit: buffer bounds, null checks)

  CBMC pipeline:
  C source
      | parsing + type checking
      v
  GOTO program (internal SSA-like IR)
      | symbolic execution / unrolling
      v
  Logical formula (CNF / SMT)
      | SAT/SMT solver (MiniSat, Z3)
      v
  SAT: print counterexample (variable values at each step)
  UNSAT: property holds within the bound

  Handles:
  - Buffer overflow / out-of-bounds access
  - Null pointer dereference
  - Integer overflow
  - User-specified assert()
  - Division by zero
  - Memory leaks (with some effort)

  Limitations:
  - Loops: require unrolling bound (--unwind N)
  - Heap: modeled but limited precision
  - External libraries: require stubs/models
```

### AWS CBMC Usage

```
  AWS C Common library: 50,000+ lines of C for cross-platform support
  (used by every AWS SDK in C).

  Process:
  1. Write harness (entry point with non-deterministic inputs)
  2. Specify properties (memory safety + functional assertions)
  3. Run CBMC with unwind bounds for loops
  4. Integrate in CI (CBMC as a test step)

  Properties checked:
  - All memory accesses in bounds
  - No use-after-free
  - No null pointer dereference
  - No integer overflow
  - Custom functional invariants

  Scale: hundreds of CBMC proofs run in CI.
  Harnesses: ~200 lines each for typical verification units.
  Runtime: minutes per proof (parallelized in CI).
```

---

## CEGAR: Counterexample-Guided Abstraction Refinement

The scalability answer for software model checking. Instead of verifying the full
concrete program, verify an abstraction, then refine when the abstraction lies.

```
  CEGAR Loop:
  ┌──────────────────────────────────────────────────────┐
  │                                                      │
  │   Concrete Program  --abstract-->  Abstract Model    │
  │                                         |            │
  │                                    model check       │
  │                                         |            │
  │                               ┌────────┴──────────┐  │
  │                               |                   |  │
  │                          Property            Counterexample  │
  │                            holds              found          │
  │                            (DONE)                |          │
  │                                        simulate on concrete  │
  │                                                   |          │
  │                                       ┌───────────┴───────┐ │
  │                                       |                   | │
  │                                  Spurious CE         Real bug│
  │                                  (abstraction        (DONE) │
  │                                   too coarse)               │
  │                                       |                     │
  │                                  Refine abstraction         │
  │                                  (add predicates)           │
  │                                       |                     │
  │                                  Back to model check        │
  └──────────────────────────────────────────────────────────────┘

  Key idea: predicate abstraction.
  The abstract state is defined by the set of predicates that hold.
  A predicate is a boolean condition over program variables.
  Example predicates: x > 0, ptr != NULL, size <= MAXSIZE

  SLAM (Microsoft Research, 2001):
  - Applied CEGAR to Windows device driver verification
  - Drivers must follow API call protocols (acquire before release, etc.)
  - Predicate abstraction + CEGAR + BDD-based model checking
  - Found 3000+ violations before Windows Vista shipped
  - Became SDV (Static Driver Verifier) — mandatory for Windows drivers
```

---

## TLA+ Checker (TLC): Explicit-State for Distributed Protocols

TLC is the model checker for TLA+ specifications. Unlike SPIN (process algebra), TLC
directly executes the mathematical state machine description.

### TLC Architecture

```
  TLA+ Spec
       | parse + type inference
       v
  TLC configuration
  (CONSTANTS, INVARIANTS, PROPERTIES)
       |
       v
  Breadth-first / depth-first state space exploration
       |
       | state: assignment of all state variables
       | init:  states satisfying Init predicate
       | next:  states reachable via Next action
       v
  Check at each state:
  - Invariants (safety): Is this state valid?
  - Temporal properties (liveness): Are fairness conditions satisfied?
       |
  Invariant violated: print violating state + trace
  Deadlock (no Next transitions): print trace
  All states explored, no violation: "Model checking complete"

  Symmetry reduction: if model has symmetric structure (e.g., N
  identical servers), TLC exploits it to reduce state space by N!.

  Fingerprinting: states stored by hash, not full content.
  Distributed TLC: TLC can use multiple JVM processes.
```

### TLA+ Safety vs Liveness

```
  Safety property:   "Bad thing never happens"
  Form: Invariant (checked at every state) or
        Action invariant (checked at every transition)

  Example (mutual exclusion):
  MutexInvariant == ~(pc[1] = "crit" /\ pc[2] = "crit")

  Liveness property: "Good thing eventually happens"
  Form: Temporal formula with F (eventually), fairness conditions

  Example (starvation freedom):
  NoStarvation == \A i \in {1,2}: [](pc[i] = "wait" => <>(pc[i] = "crit"))

  Fairness (required to make liveness meaningful):
  WF_vars(Next)  = weak fairness: if Next is enabled, it eventually happens
  SF_vars(Next)  = strong fairness: if Next is enabled infinitely often,
                                     it eventually happens

  Without fairness conditions, the model checker can find "starvation" by
  always scheduling the other process. Fairness rules this out.
```

### Practical TLA+ Example: Distributed Lock

**Note**: This example also appears in `05-SPECIFICATION.md` with a focus on spec writing syntax. Here the emphasis is on the model-checking workflow: running TLC, interpreting counterexamples, and verifying properties.

```tla
------------------------------ MODULE DistLock ------------------------------
VARIABLES lock, owner, waiting

TypeInvariant ==
  /\ lock \in {"free", "held"}
  /\ owner \in {"none", "p1", "p2"}
  /\ waiting \subseteq {"p1", "p2"}

Init ==
  /\ lock = "free"
  /\ owner = "none"
  /\ waiting = {}

Acquire(p) ==
  /\ lock = "free"
  /\ lock' = "held"
  /\ owner' = p
  /\ waiting' = waiting \ {p}

Request(p) ==
  /\ lock = "held"
  /\ owner # p
  /\ waiting' = waiting \cup {p}
  /\ UNCHANGED <<lock, owner>>

Release(p) ==
  /\ lock = "held"
  /\ owner = p
  /\ lock' = "free"
  /\ owner' = "none"
  /\ UNCHANGED waiting

Next == \E p \in {"p1", "p2"}:
           \/ Acquire(p)
           \/ Request(p)
           \/ Release(p)

MutualExclusion == lock = "held" => \E p: owner = p /\ p # "none"
NoTwoOwners == ~(owner = "p1" /\ owner = "p2")  (* trivially true *)

Spec == Init /\ [][Next]_<<lock, owner, waiting>> /\
        WF_<<lock,owner,waiting>>(Next)

EventualAcquisition == \A p \in {"p1","p2"}:
  p \in waiting ~> owner = p

THEOREM Spec => [](MutualExclusion /\ NoTwoOwners)
THEOREM Spec => EventualAcquisition

=============================================================================
```

---

## State Explosion: Scale and Mitigation

```
  Why it's hard:
  +------------------+------------------+------------------------------+
  | Concurrent comps | States each      | Total state space            |
  +------------------+------------------+------------------------------+
  | 10               | 10               | 10^10 = 10 billion           |
  | 20               | 10               | 10^20 (beyond any computer)  |
  | 100              | 2 (bit each)      | 2^100 = 10^30               |
  +------------------+------------------+------------------------------+

  Mitigation techniques:
  ┌────────────────────────────────────────────────────────────────┐
  │ Partial order reduction: many interleavings are equivalent.    │
  │ Skip: if A and B are independent (no shared variables),        │
  │ A;B and B;A reach the same state — explore only one.          │
  │ SPIN: POR built in. Reduction: often 10x-100x.                 │
  ├────────────────────────────────────────────────────────────────┤
  │ Symmetry reduction: if components are identical (by type),     │
  │ many states are permutations of each other — collapse them.    │
  │ TLC: symmetry set annotation. Reduction: N! for N processes.   │
  ├────────────────────────────────────────────────────────────────┤
  │ BDD-based symbolic: represent state SETS, not individual       │
  │ states. BDD of 10^20 states can be tiny if structure is right. │
  ├────────────────────────────────────────────────────────────────┤
  │ Abstraction (CEGAR): coarsen the model. Only refine where      │
  │ counterexamples are spurious.                                  │
  ├────────────────────────────────────────────────────────────────┤
  │ BMC: don't prove for all steps — just up to bound k.           │
  │ Great for bug finding; insufficient for full verification.     │
  ├────────────────────────────────────────────────────────────────┤
  │ IC3/PDR: property-directed reachability — incrementally        │
  │ builds inductive invariants without explicit enumeration.      │
  │ State of the art for hardware verification (2011+).            │
  └────────────────────────────────────────────────────────────────┘
```

---

## IC3 / PDR: Property-Directed Reachability

IC3 (Bradley, 2011) / PDR (Property-Directed Reachability) is the current state of the
art for proving safety properties without BDD or explicit enumeration:

```
  Goal: prove P is an inductive invariant (or find counterexample).

  Key idea: maintain a sequence of "frames":
  F0, F1, F2, ..., Fk where:
  - F0 = Init (initial states)
  - Fi -> Fi+1 (each frame is a subset of the previous)
  - All Fi satisfy P (safety maintained)
  - Fi+1 blocks all k+1-step predecessors of bad states

  IC3 Algorithm (sketch):
  1. Check if any Fi = Fi+1 (fixed point) -> property proven
  2. Find a bad state reachable in k steps
  3. Try to block it: add clause to Fk preventing that state
  4. If clause propagates back to F0: real counterexample
  5. Propagate clauses forward to consolidate frames
  6. Increment k if no bad state found at current depth

  Why it's better than BDDs for many problems:
  - Incremental: doesn't build complete reachable set
  - SAT-based: leverages modern SAT solvers + UNSAT cores
  - Learns inductive invariants on-the-fly
  - Avoids BDD variable ordering problem

  Used in: hardware model checking (JasperGold), software
  (CPAchecker IC3 backend), AVR for microcontrollers.
```

---

## Tool Comparison

| Tool | Input | Technique | Properties | Scale | Counterexamples |
|------|-------|-----------|------------|-------|-----------------|
| SPIN | PROMELA | Explicit, Buchi | LTL | 10^8 states | Yes, full trace |
| TLC | TLA+ | Explicit + symmetry | Safety, liveness | 10^8-10^9 | Yes, full trace |
| NuSMV | SMV | BDD symbolic | CTL, LTL | 10^20+ (if BDDs small) | Yes |
| CBMC | C/C++ | BMC (SAT) | Assertions, memory | Bounded | Yes, C-level |
| SLAM/SDV | C + API spec | CEGAR | Protocol conformance | Drivers | Yes |
| CPAchecker | C | CEGAR, IC3 | Reachability | Software | Yes |
| Alloy | Alloy | BMC (SAT) | Relational inv. | Small scopes | Yes, visual |

---

## Decision Cheat Sheet

| Situation | Tool / Technique |
|-----------|-----------------|
| Protocol has 10 processes, need to verify in < 1 hour | TLC with symmetry reduction |
| Concurrent C++ data structure, need to find race conditions | SPIN or TLC with PROMELA/TLA+ model |
| Need to prove C function never overflows buffer | CBMC (set unwind bound for loops) |
| Windows-style driver must follow API calling protocol | SLAM/SDV-style CEGAR |
| Hardware pipeline: no deadlock, no protocol violation | NuSMV (BDD-based) or IC3 |
| Want to find bugs quickly, don't need full proof | CBMC with small bounds |
| Need to verify a Paxos implementation is correct | Write TLA+ spec, run TLC |
| System has 10^25 states but simple structure | BDD-based (NuSMV) |
| Property: "this error state is unreachable" | IC3/PDR (fastest for safety) |

---

## Common Confusion Points

**"BMC not finding a violation means the property holds"**

Only within the bound k. UNSAT from CBMC with --unwind 10 means "no bug in 10
iterations of the loop." Increase the bound for more confidence. Without computing
the completeness threshold, you cannot claim full correctness.

**"SPIN verifies infinite execution traces"**

SPIN searches for accepting cycles in the Buchi product automaton — which correspond
to infinite executions violating the LTL property. But the state space must be
finite. SPIN does not handle infinite data domains.

**"BDD-based symbolic model checking scales to any size"**

BDDs can be exponentially large for certain functions (especially arithmetic). The
"million states in a small BDD" story only works when the state space has exploitable
structure. Multiplication circuits have exponential BDDs — this killed pure BDD
approaches for arithmetic hardware.

**"TLA+ TLC verifies the actual implementation"**

TLC verifies a TLA+ model (a mathematical state machine). The model must be
separately checked to match the implementation. TLA+ is for design-level verification.
For code-level verification, use CBMC or a proof assistant.

**"Model checking finds all bugs"**

Within the explored state space. State explosion may prevent full exploration.
And the model/spec must correctly capture the real system. Model checking finds
violations of specified properties — properties you didn't specify are not checked.
