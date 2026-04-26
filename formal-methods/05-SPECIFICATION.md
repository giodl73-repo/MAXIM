# Formal Specification

## The Big Picture

Specification languages let you write a precise, unambiguous description of what a
system should do — before and separate from how it does it. The value is not just
verification: it is design clarity and communication.

```
+--------------------------------------------------------------------------+
|                    SPECIFICATION LANGUAGE LANDSCAPE                      |
|                                                                            |
|  LANGUAGE    FORMALISM        BACKEND         BEST FOR                   |
|  ────────    ─────────        ───────         ────────                   |
|  TLA+        Temporal logic   TLC (explicit   Distributed protocols      |
|  (Lamport)   + set theory     state), TLAPS   (Paxos, Raft, replication) |
|                               (proof system)                             |
|                                                                            |
|  PlusCal     Pseudocode       Transpiles to   Algorithms (easier entry   |
|  (Lamport)   (imperative)     TLA+            for engineers)             |
|                                                                            |
|  Alloy       Relational FOL   Kodkod (SAT)    Data model correctness,    |
|  (Jackson)   first-order      bounded scope   structural invariants,     |
|              + transitive     analysis        schema design              |
|              closure                                                       |
|                                                                            |
|  Z notation  Set theory       Z/Eves, ProofPwr  Sequential specs,        |
|  (Spivey)    + schemas        (verification)    IBM CICS, civil aviation |
|                                                                            |
|  Event-B     Refinement       Rodin tool      Safety-critical embedded,  |
|  (Abrial)    calculus         (proof oblig.)  Paris Metro Line 14,       |
|              B-Method family  ProB (animator) transit control systems    |
|                                                                            |
|  VDM-SL      Implicit + expl. VDMTools        Sequential + concurrent    |
|  (Bjorner)   specs, pre/post  Overture         industrial specs          |
+--------------------------------------------------------------------------+
```

---

## TLA+: Temporal Logic of Actions

TLA+ (Leslie Lamport, 1994) is the dominant formal specification language for
distributed systems. The design philosophy: distributed systems ARE state machines,
so describe them as state machines using mathematics.

### Core Concepts

```
  TLA+ model: a set of behaviors (infinite sequences of states).

  State:    An assignment of values to all state variables.
  Behavior: An infinite sequence of states: s0, s1, s2, ...

  Specification components:
  +------------------+--------------------------------------------+
  | State variables  | VARIABLES x, y, z                          |
  |                  | The mutable state of the system            |
  +------------------+--------------------------------------------+
  | Initial predicate| Init == x = 0 /\ y = {} /\ z = "idle"     |
  |                  | Which states are initial                   |
  +------------------+--------------------------------------------+
  | Next-state rel.  | Next == Action1 \/ Action2 \/ Action3      |
  |                  | What transitions are allowed               |
  +------------------+--------------------------------------------+
  | Temporal spec    | Spec == Init /\ [][Next]_vars /\ Fairness  |
  |                  | All behaviors satisfying Init and Next     |
  +------------------+--------------------------------------------+
  | Safety property  | Invariant == <some state predicate>        |
  |                  | Must hold at every reachable state         |
  +------------------+--------------------------------------------+
  | Liveness prop.   | LiveProp == <>[](ready) or similar         |
  |                  | Must hold for every behavior               |
  +------------------+--------------------------------------------+
```

### TLA+ Syntax Reference

```tla
(* Variable declarations *)
VARIABLES lock, owner, queue

(* State predicate: TypeInvariant *)
TypeOK ==
  /\ lock \in {"free", "held"}
  /\ owner \in SERVERS \cup {"none"}
  /\ queue \in SUBSET SERVERS

(* Initial state *)
Init ==
  /\ lock = "free"
  /\ owner = "none"
  /\ queue = {}

(* Action: server s acquires the lock *)
Acquire(s) ==
  /\ lock = "free"           (* ENABLED when lock is free *)
  /\ lock' = "held"          (* PRIMED var = value AFTER transition *)
  /\ owner' = s
  /\ queue' = queue \ {s}    (* remove s from waiting queue *)

(* Action: server s releases the lock *)
Release(s) ==
  /\ lock = "held"
  /\ owner = s
  /\ lock' = "free"
  /\ owner' = "none"
  /\ UNCHANGED queue

(* Action: server s requests the lock *)
Request(s) ==
  /\ lock = "held"
  /\ s \notin queue
  /\ queue' = queue \cup {s}
  /\ UNCHANGED <<lock, owner>>

(* Next-state relation: disjunction of all actions *)
Next ==
  \/ \E s \in SERVERS: Acquire(s)
  \/ \E s \in SERVERS: Release(s)
  \/ \E s \in SERVERS: Request(s)

(* Full specification with fairness *)
Spec ==
  /\ Init
  /\ [][Next]_<<lock, owner, queue>>    (* safety: stuttering allowed *)
  /\ WF_<<lock,owner,queue>>(Next)      (* weak fairness: liveness *)

(* Safety property: mutual exclusion *)
MutualExclusion ==
  \A s1, s2 \in SERVERS:
    (owner = s1 /\ owner = s2) => s1 = s2

(* Liveness: every waiting server eventually gets the lock *)
NoStarvation ==
  \A s \in SERVERS:
    (s \in queue) ~> (owner = s)    (* ~> = "leads to" *)
```

### Safety vs Liveness in TLA+

```
  Safety: "Bad thing never happens" = prefix-closed property
  Form: Invariant (checked at every state)
        or Action property: [][P]_vars

  Liveness: "Good thing eventually happens" = not prefix-closed
  Form: F p  (eventually p)
        G F p  (always eventually p -- infinitely often)
        p ~> q  (p leads to q: whenever p, eventually q)

  Fairness conditions (required to prove liveness):
  WF_vars(A)  = Weak Fairness of A:
    If A is continuously enabled, A eventually occurs.
    (If A can always fire, it eventually does fire.)

  SF_vars(A)  = Strong Fairness of A:
    If A is enabled infinitely often, A eventually occurs.
    (Even if A is sometimes disabled, if it keeps becoming
     enabled, it eventually fires.)

  Without fairness: a scheduler that always ignores a process
  is a valid model (process never gets the lock). Fairness rules
  out such pathological schedulers.
```

### AWS TLA+ in Practice (Newcombe et al., 2015)

```
  Systems specified:
  - S3 bucket versioning protocol
  - DynamoDB replication and failure recovery
  - EBS (Elastic Block Store) volume management
  - Internal distributed lock service
  - Amazon Kinesis consumer state management

  What TLA+ caught:
  - S3 versioning: invariant violated in a 7-step sequence.
    Finding: two concurrent writers with a specific interleaving
    could result in a version being skipped permanently.
    Fix: add a serialization step in the replication protocol.

  - DynamoDB: 3 bugs found during spec writing, before coding.
    "The act of writing the spec forced us to think through
    all cases." Bugs were in the intended design, not the code.

  - EBS: an optimization for read performance was subtly wrong
    under a specific combination of failures. TLC found a
    10-step trace demonstrating data loss.

  Engineer feedback:
  "TLA+ let us have design reviews with an actual artifact to
  check, rather than arguing about ambiguous natural language."

  Process:
  1. Write TLA+ spec during design review (1-3 weeks for new protocols)
  2. Run TLC to check invariants + liveness (hours to days)
  3. Fix spec bugs (design bugs) before writing code
  4. Keep spec as documentation of intended behavior
  5. Re-run TLC when design changes

  Model sizes: typically 10^7 - 10^9 states for production protocols
```

---

## PlusCal: Algorithm-First TLA+

PlusCal is an imperative pseudocode that compiles to TLA+. Designed for engineers
who think algorithmically, not mathematically.

### PlusCal Syntax

```
--algorithm MutexAlgorithm {
  variables lock = FALSE;

  process (P \in {"p1", "p2"}) {
    ncs:     (* non-critical section label *)
      skip;  (* non-critical section *)
    wait:
      await lock = FALSE;
    acquire:
      lock := TRUE;
    crit:    (* critical section label *)
      (* do critical section work *)
      skip;
    release:
      lock := FALSE;
      goto ncs;
  }
}

(* TLC checks:
   []~(pc["p1"] = "crit" /\ pc["p2"] = "crit")
*)
```

PlusCal is especially useful when:
- The algorithm is naturally sequential with explicit steps
- Engineers are more comfortable with pseudocode
- You want to specify a known algorithm (fast-path mutex, ring leader election)

---

## Alloy: Relational Specification

Alloy (Daniel Jackson, MIT) uses first-order relational logic. Designed for finding
structural bugs in designs — "lightweight formal methods."

### The Alloy Model

```
module FileSystem

sig File {}
sig Directory extends File {
  contents: set File
}
sig Root extends Directory {}

-- Constraint: no cycles in directory structure
fact NoDirectoryCycles {
  no d: Directory | d in d.^contents
  -- "no directory is reachable from itself via contents"
}

-- Constraint: every non-root file has exactly one parent
fact OneParent {
  all f: File - Root |
    one d: Directory | f in d.contents
}

-- Assertion: root is reachable from every file
assert RootReachable {
  all f: File | Root in f.^~contents + f
}

check RootReachable for 5
-- Alloy Analyzer: check with up to 5 files/directories
-- If counterexample found: visualize it as a graph
```

### Alloy Analyzer: Bounded SAT Checking

```
  Alloy's approach: small scope hypothesis
  "Most bugs appear with small instances (3-5 objects)."
  (Jackson's empirical claim, borne out in practice.)

  Process:
  1. Alloy spec defines:
     - Signatures (types / sets of atoms)
     - Relations (arrows between atoms)
     - Facts (constraints always true)
     - Assertions (properties to check)
  2. Kodkod backend: translates to boolean SAT
     (atoms are represented as boolean variables)
  3. SAT solver finds a counterexample (violating instance)
     or reports "no counterexample in this scope"

  Visualization: Alloy shows counterexamples as node-edge diagrams.
  This is enormously useful -- you SEE the structure of the bug.

  Best uses:
  - Data model correctness (database schema invariants)
  - API protocol correctness (call sequence constraints)
  - Security policy checking (access control models)
  - Finding structural bugs in object-oriented designs
```

---

## Z Notation

Z (referencing Zermelo-Fraenkel set theory — pronounced "Zed") uses typed set theory
and schemas.

### Schema Structure

```
  State schema: declares state variables and invariants
  ┌─── Library ─────────────────────────────┐
  │ stock: BOOK --> N                       │
  │ issued: PATRON -->> BOOK                │
  ├──────────────────────────────────────────┤
  │ dom issued ⊆ dom stock                   │
  └──────────────────────────────────────────┘

  Operation schema: pre and post conditions
  ┌─── Checkout ───────────────────────────────────────┐
  │ DeltaLibrary           (* state changes *)         │
  │ p?: PATRON             (* input -- ? suffix *)     │
  │ b?: BOOK               (* input *)                 │
  ├────────────────────────────────────────────────────┤
  │ b? ∈ dom stock                    (* precondition *)│
  │ b? ∉ ran issued                   (* book available*)│
  │ issued' = issued ∪ {p? |-> b?}    (* book issued *) │
  │ stock' = stock                    (* unchanged *)   │
  └────────────────────────────────────────────────────┘

  XiLibrary = DeltaLibrary with no state change
  DeltaLibrary = before state + after state (primed variables)

  Schema calculus: combine schemas via conjunction, disjunction,
  sequential composition, hiding.
```

### Z in Industrial Use

```
  IBM CICS (Customer Information Control System):
  - Used Z to specify the transactional behavior
  - Found ambiguities in natural language documentation
  - Led to a cleaner implementation

  UK Defence Standard 00-55:
  - Required Z notation for safety-critical software specifications

  Current status:
  Z is less used now -- TLA+ and Alloy have largely replaced it
  for new work. Z's contribution: established the schema calculus
  and the "write the spec in set theory" approach.
```

---

## Event-B: Refinement-Based Specification

Event-B (Jean-Raymond Abrial, 2005) is the successor to B-Method. Designed around
formal refinement: start with an abstract spec, refine it to an implementation.

### Core Structure

```
  MACHINE TrafficLight
  VARIABLES colour
  INVARIANTS
    colour ∈ {red, amber, green}
  EVENTS
    Initialisation
      BEGIN colour := red END

    ToGreen
      WHEN colour = red
      THEN colour := green END

    ToAmber
      WHEN colour = green
      THEN colour := amber END

    ToRed
      WHEN colour = amber
      THEN colour := red END
  END

  Proof obligations (generated automatically by Rodin):
  - Invariant preservation: each event preserves the invariant
  - Refinement consistency: refined events simulate abstract ones
  - Feasibility: guard conditions are achievable

  Refinement: introduce implementation details, add variables,
  split events, add guards, but preserve the abstract invariant.
```

### Event-B in Practice: Paris Metro Line 14

```
  Paris Metro Line 14: fully automated (no driver) since 1998.
  System: CBTC (Communication-Based Train Control)

  Specification process (using B-Method, Event-B predecessor):
  1. Write abstract B specification of safety properties
     (no two trains on same track segment)
  2. Verify with Atelier B (automated proof obligations)
  3. Refine to implementation level
  4. Generate code from refined model
  5. Verify each refinement step

  DO-178C qualified toolchain: Atelier B is tool-qualified
  for DO-178C Level A (catastrophic failure level).

  Adoption: >50 automated metro systems worldwide use this approach.
```

---

## Specification Patterns

Patterns encode common temporal properties in reusable form:

```
  Pattern: Universality (P always holds)
  LTL:   G p
  CTL:   AG p
  TLA+:  []p  or  Invariant

  Pattern: Absence (P never holds)
  LTL:   G ~p
  CTL:   AG ~p
  TLA+:  []~p  (safety invariant)

  Pattern: Existence (P holds at some point)
  LTL:   F p
  CTL:   EF p
  TLA+:  <>p  (eventuality)

  Pattern: Response (after P, Q eventually follows)
  LTL:   G(p -> F q)
  CTL:   AG(p -> AF q)
  TLA+:  [](p => <>q)  or  p ~> q  (leads-to)

  Pattern: Precedence (P never holds without prior Q)
  LTL:   ~q U p -> G ~p
  TLA+:  ~p W q  (p weak-until q)

  Practical rule of thumb:
  Safety properties = invariants. TLA+ Invariant clause.
  Liveness properties = leads-to. TLA+ ~> or temporal formula.
  Verify safety first (easier, model checker handles it).
  Liveness requires fairness conditions -- add only what's needed.
```

---

## Specification Antipatterns

```
  ANTIPATTERN: Specifying implementation, not behavior
  Bad:   The server sends a TCP ACK within 100ms.
  Better: Every request receives a response.

  ANTIPATTERN: Over-constraining (specifying too much)
  Bad:   Lock is acquired in strict FIFO order.
  Better: Lock is eventually acquired by every waiting process.
  (FIFO is an implementation choice, not a requirement.)

  ANTIPATTERN: Under-constraining (specifying too little)
  Bad:   The system makes progress.
  Better: Every request eventually gets a response, even under
          arbitrary failures of non-faulty nodes.

  ANTIPATTERN: Confusing liveness and safety
  "The lock is always available" is actually TWO properties:
  Safety:   The lock is never held by two processes simultaneously.
  Liveness: A process waiting for the lock eventually gets it.

  ANTIPATTERN: Writing the spec AFTER the implementation
  You lose the main benefit: finding design bugs before coding.
  The spec should be written DURING design, alongside whiteboard diagrams.

  ANTIPATTERN: Spec diverges from implementation without update
  The spec is only useful as long as it accurately models the system.
  Treat spec updates as first-class work when code changes.
```

---

## Decision Cheat Sheet

| Situation | Notation |
|-----------|----------|
| Distributed protocol (Raft, Paxos, consensus) | TLA+ (run TLC) |
| Algorithm with sequential control flow | PlusCal (compiles to TLA+) |
| Data model / schema structural correctness | Alloy (Alloy Analyzer) |
| Sequential system with pre/post conditions | Z notation or VDM-SL |
| Safety-critical embedded (DO-178C toolchain) | Event-B + Rodin / B-Method |
| API call sequence protocol | Alloy or TLA+ |
| Microservice invariants (data consistency) | TLA+ (model the protocol) |
| "Is this design correct before we code it?" | Alloy for structure, TLA+ for behavior |
| Need refinement (abstract -> implementation) | Event-B |
| Azure service protocol design | TLA+ (same approach as AWS) |

---

## Common Confusion Points

**"TLA+ is only for distributed systems"**

TLA+ is general -- it models any state-based system. It excels at distributed protocols
because those are exactly "interleaved concurrent state machines." But it has been used
for hardware protocols, security models, and sequential algorithms.

**"PlusCal is easier, so use it instead of TLA+"**

PlusCal is easier for sequential algorithms with explicit steps. For inherently parallel
or reactive systems, TLA+ actions are more natural. PlusCal compiles to TLA+, so you
can mix both -- write the algorithm in PlusCal, add TLA+ temporal properties.

**"Alloy proves properties for all inputs"**

Alloy uses bounded verification (small scope). It does NOT prove properties for all
instances of all sizes. It finds counterexamples up to the scope you specify.
"No counterexample in scope 5" is evidence, not proof.

**"TLA+ specs are too hard for software engineers to learn"**

Newcombe 2015 is evidence against this. The learning curve is set theory notation
(union, intersection, quantifiers) and the action model. Engineers with CS backgrounds
typically learn it in 1-2 weeks. The hard part is writing a GOOD spec.

**"Fairness conditions make everything complicated"**

Start without fairness -- TLC will check safety. Add weak fairness (WF) as the
default for liveness. Only add strong fairness (SF) when WF is insufficient.
In practice, WF covers most liveness requirements.
