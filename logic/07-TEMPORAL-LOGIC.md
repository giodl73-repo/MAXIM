# Temporal Logic and Model Checking

## The Big Picture

Temporal logic adds a **time axis** to modal logic. LTL (Linear Temporal Logic) reasons
about infinite traces. CTL/CTL* reason about branching trees of states. Model checking
automatically verifies whether a finite-state system satisfies a temporal specification.

```
+-------------------------------------------------------------------+
|                 TEMPORAL LOGIC AND MODEL CHECKING                 |
|                                                                   |
|  LOGICS              STRUCTURES             ALGORITHMS            |
|  +------------+      +------------------+   +------------------+  |
|  | LTL        |      | Kripke structure |   | Explicit-state   |  |
|  | (linear,   |      | M = (S, T, L):   |   | (SPIN: DFS,      |  |
|  | paths)     |      | S = states       |   |  Buchi automata)  |  |
|  |            |      | T = transitions  |   | Symbolic (BDD)   |  |
|  | CTL        |      | L = labels       |   | SAT-based (BMC)  |  |
|  | (branching,|      |                  |   | CEGAR            |  |
|  | trees)     |      | Computation path:|   | IC3/PDR          |  |
|  |            |      | s0 -> s1 -> s2...|   +------------------+  |
|  | CTL*       |      +------------------+                         |
|  | (both)     |                                                   |
|  +------------+      TOOLS                                        |
|                      +------------------------------------------+ |
|  MU-CALCULUS         | SPIN (LTL)  NuSMV/nuXmv (CTL, BDD, SAT)  | |
|  +------------+      | Uppaal (timed automata)                   | |
|  | Least/     |      | PRISM (probabilistic)                     | |
|  | Greatest   |      | TLA+ (Lamport, industrial use at AWS)     | |
|  | fixpoints  |      | nuXmv, ABC, Cadence JasperGold            | |
|  +------------+      +------------------------------------------+ |
+-------------------------------------------------------------------+
```

---

## Linear Temporal Logic (LTL)

### Intended Semantics

LTL formulas are evaluated over **infinite sequences** (traces) of states:

```
  pi = s0 s1 s2 s3 ...   (infinite sequence, omega-word)

  pi^i = s_i s_{i+1} ...  (suffix starting at position i)
```

### Syntax

```
  phi ::= p              (atomic proposition)
        | top | bot
        | neg phi
        | phi land psi
        | phi lor psi
        | phi -> psi
        | X phi           (neXt: phi holds at next position)
        | G phi           (Globally: phi holds at ALL future positions)
        | F phi           (Finally: phi holds at SOME future position)
        | phi U psi       (Until: phi holds until psi; psi eventually holds)
        | phi W psi       (Weak Until: phi U psi or G phi)
        | phi R psi       (Release: psi holds until and including when phi holds)
```

### Truth Conditions

```
  pi, i |= p          iff  p in L(s_i)
  pi, i |= neg phi    iff  pi, i |/= phi
  pi, i |= phi land psi  iff  pi,i |= phi  and  pi,i |= psi
  pi, i |= X phi      iff  pi, i+1 |= phi
  pi, i |= G phi      iff  for all j >= i: pi, j |= phi
  pi, i |= F phi      iff  exists j >= i: pi, j |= phi
  pi, i |= phi U psi  iff  exists j >= i: pi, j |= psi
                           AND for all k with i <= k < j: pi, k |= phi
```

### LTL Laws

```
  F phi  ===  top U phi
  G phi  ===  phi R bot  ===  neg F neg phi
  phi R psi  ===  neg(neg phi U neg psi)
  phi W psi  ===  (phi U psi) lor G phi

  Duality:
    neg G phi  ===  F neg phi
    neg F phi  ===  G neg phi
    neg(phi U psi) ===  (neg psi) W (neg phi land neg psi)
    neg X phi  ===  X neg phi

  Expansion laws:
    phi U psi  ===  psi lor (phi land X(phi U psi))
    G phi  ===  phi land X G phi
    F phi  ===  phi lor X F phi
```

### LTL Examples

```
  System properties expressed in LTL (p = request, q = grant):

  "Every request is eventually granted":
    G(p -> F q)

  "Between request and grant, no second request":
    G(p -> (neg p U q))

  "Grant never occurs without a preceding request":
    neg q U (p land neg q)

  "The system never deadlocks" (no deadlock = some transition available):
    G(available)

  "Property p holds infinitely often":
    G F p

  "Property p holds from some point on":
    F G p

  Mutual exclusion (c1, c2 = in critical section):
    G(neg(c1 land c2))
```

---

## CTL: Computation Tree Logic

### Motivation

LTL quantifies implicitly over a single execution path. CTL explicitly quantifies over
**paths in a branching structure**.

```
  CTL PATH QUANTIFIERS:
  A phi  =  All paths from this state satisfy phi
  E phi  =  Exists a path from this state satisfying phi

  CTL STATE FORMULAS composed from:
    Path quantifiers: A, E
    Temporal operators: X, G, F, U

  RESTRICTION: in CTL, every temporal operator must be immediately preceded
               by a path quantifier (AX, AF, AG, AU, EX, EF, EG, EU).
```

### CTL Syntax

```
  phi ::= p
        | top | bot
        | neg phi | phi land psi | phi lor psi
        | AX phi    (on All paths: neXt phi)
        | EX phi    (there Exists a path: neXt phi)
        | AG phi    (on All paths: Globally phi)
        | EG phi    (there Exists a path: Globally phi)
        | AF phi    (on All paths: Finally phi)
        | EF phi    (there Exists a path: Finally phi)
        | A[phi U psi]   (All paths: phi Until psi)
        | E[phi U psi]   (Exists a path: phi Until psi)
```

### CTL Truth Conditions on a Kripke structure M = (S, T, L)

```
  M, s |= AX phi   iff  for all t with (s,t) in T: M, t |= phi
  M, s |= EX phi   iff  exists t with (s,t) in T: M, t |= phi
  M, s |= AG phi   iff  for all paths pi from s, all i: M, pi(i) |= phi
  M, s |= EG phi   iff  exists path pi from s, for all i: M, pi(i) |= phi
  M, s |= AF phi   iff  for all paths pi from s, exists i: M, pi(i) |= phi
  M, s |= EF phi   iff  exists path pi from s, exists i: M, pi(i) |= phi
```

### CTL vs. LTL Expressiveness

```
  CTL and LTL are INCOMPARABLE in expressiveness (neither subsumes the other).

  Expressible in LTL, not CTL:
    G F p  (p holds infinitely often — on all paths)
    LTL is "path-quantifier implicit": it talks about all paths uniformly.
    CTL can't express "on all paths, p holds infinitely often" directly.

  Expressible in CTL, not LTL:
    EG p  (there exists a path on which p holds forever — fairness witness)
    AF AG p  (on all paths, from some point p holds forever)
    AG EF p  (from every reachable state, there is some path back to p)
```

---

## CTL*: Unifying Both

CTL* combines the path quantifiers of CTL with the unrestricted path formulas of LTL:

```
  CTL* = CTL + LTL  (both subsume into CTL*)

  CTL* state formulas:
    phi ::= p | neg phi | phi land psi | A psi | E psi
  CTL* path formulas:
    psi ::= phi | neg psi | psi land psi | X psi | psi U psi | G psi | F psi

  CTL* model checking: EXPTIME (harder than CTL which is PTIME)
  CTL* satisfiability: 2EXPTIME
```

---

## Model Checking Algorithms

### CTL Model Checking (Clarke, Emerson, Sifakis — Turing Award 2007)

For a finite Kripke structure M with state space S and a CTL formula phi:

```
  LABELING ALGORITHM:
  Mark each state with the set of subformulas of phi true at that state.
  Work bottom-up on the formula structure.

  Base cases (atoms): mark directly from L(s).

  Inductive cases:
    phi land psi: states marked by both phi and psi.
    neg phi: states not marked by phi.
    EX phi: states with at least one phi-marked successor.
    AX phi: states with all successors phi-marked.
    EF phi: BFS/DFS from phi-states backward along T.
    AG phi: BFS/DFS from neg phi-states forward; mark complement.
    EU[phi U psi]: iterative fixed-point computation.
    AU[phi U psi]: iterative fixed-point computation.

  Time complexity: O(|S| * |phi|)
  PTIME in combined state space and formula size.
```

### Fixed-Point Semantics

```
  AF phi  =  mu X. (phi lor AX X)         (least fixed point)
  EG phi  =  nu X. (phi land EX X)        (greatest fixed point)
  EF phi  =  mu X. (phi lor EX X)         (least fixed point)
  AG phi  =  nu X. (phi land AX X)        (greatest fixed point)

  MU-CALCULUS generalizes all of CTL/LTL via mu (least) and nu (greatest) fixpoints.
```

### LTL Model Checking via Büchi Automata (SPIN)

```
  LTL MODEL CHECKING:

  1. Negate property: check if system satisfies neg phi (equivalently, find counterexample).
  2. Convert neg phi to a Büchi automaton A_{neg phi}.
     (Büchi = finite automaton accepting infinite words with acceptance condition:
      some final state visited infinitely often)
  3. Build product automaton M x A_{neg phi}.
  4. Check for accepted run in the product.
     (Accepted run = path that visits an accepting state infinitely often)
  5. If accepting run found: counterexample to phi.
     If no accepting run: M |= phi.

  BÜCHI AUTOMATON for LTL formula phi:
  Obtained via tableau construction.
  Size: exponential in |phi|.
  LTL model checking: PSPACE-complete.
```

### Symbolic Model Checking (McMillan 1993)

Instead of explicit state enumeration, represent state sets as BDDs:

```
  SYMBOLIC MODEL CHECKING:

  State set as BDD: Boolean function f(x1,...,xn) over state variables.
  Transition relation T(x, x') as BDD.
  Pre/post-image computation via BDD operations.

  AG phi: start with neg phi states; compute backward reachability.
  Fixed-point computation on BDD-represented sets.

  ADVANTAGE: can handle 10^20+ states (where explicit is hopeless).
  DISADVANTAGE: BDD size can blow up for some transition relations.
```

### Bounded Model Checking (SAT-based, Biere et al. 1999)

```
  BOUNDED MODEL CHECKING (BMC):

  Unroll the transition system k steps.
  Encode: (s0 in Init) and T(s0,s1) and T(s1,s2) and ... and T(s_{k-1},s_k)
          and (neg phi at some step in [0..k])
  Feed to SAT solver.

  If SAT: counterexample of length k found.
  If UNSAT: no counterexample of length <= k (not a proof of phi!).

  For safety properties (AG phi), BMC finds bugs but doesn't prove correctness.
  IC3/PDR (2010): extends BMC to prove safety by maintaining invariants.

  INDUSTRIAL USE: Hardware verification at Intel, AMD, ARM.
  SAT-based BMC scaled better than BDDs for many industrial circuits.
```

---

## State Explosion Problem

The fundamental challenge in model checking:

```
  System with n boolean state variables: 2^n states.
  System composed of k modules each with m states: m^k states.

  Example:
    10 parallel processes, each with 10 states: 10^10 = 10 billion states.

  MITIGATIONS:
  +--------------+----------------------------------------------------+
  | Technique    | Idea                                               |
  +--------------+----------------------------------------------------+
  | Symbolic     | BDDs represent exponential state sets compactly    |
  | Partial order| Only explore one interleaving of concurrent events |
  |  reduction   | (many interleavings give same outcome)              |
  | Abstraction/ | Model the system at a higher level of abstraction  |
  |  CEGAR       | Counterexample-Guided Abstraction Refinement       |
  | SAT/BMC      | Unfold k steps instead of exploring all states     |
  | Compositional| Verify components separately, compose results       |
  +--------------+----------------------------------------------------+
```

---

## TLA+ (Temporal Logic of Actions)

Lamport's specification language used at Amazon, Microsoft, Oracle:

```
  TLA+ = Set theory + temporal logic

  SPECIFICATION STRUCTURE:
    Init: initial state predicate
    Next: state transition relation
    Spec: Init and G[Next]_vars  ("G" is "always," subscript for stuttering)

  PROPERTIES:
    Safety: AG(phi)     -- "nothing bad happens"
    Liveness: AG(p -> AF q)  -- "something good eventually happens"
    Fairness: WF_vars(Next) -- "the system doesn't stutter forever"

  TLC MODEL CHECKER: explicit state model checker for TLA+ specs.
  Apalache: symbolic model checker for TLA+ (SMT-based).

  INDUSTRIAL USE:
  Amazon uses TLA+ for S3, DynamoDB, EC2 protocols.
  Microsoft uses it for internal distributed systems specs.
  Leslie Lamport: Turing Award 2013.
```

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Specify "always eventually" (response) | LTL: G(p -> F q) |
| Specify "there exists a safe path" | CTL: EG safe |
| Specify "every path is safe" | CTL: AG safe |
| Specify "globally infinitely often" | LTL: G F p (not in CTL) |
| Model check a small finite system | Explicit-state (SPIN for LTL, NuSMV for CTL) |
| Model check with huge state space | Symbolic BDD (NuSMV) or BMC (SAT-based) |
| Find counterexample quickly | BMC (SAT-based bounded model checking) |
| Prove safety without bound | IC3/PDR algorithm |
| Specify distributed protocols | TLA+ with TLC model checker |

---

## Common Confusion Points

**LTL vs. CTL paths.**
LTL formulas are evaluated on paths — they implicitly quantify over all paths. CTL explicitly
puts A or E before each temporal operator. CTL*  is the common generalization.

**AF p is not the same as not EG not p (or is it?).**
AF p ≡ neg EG neg p. This IS an equivalence in CTL. The duality between all-paths and
exists-path is exact. Confusions arise when mixing with LTL.

**CTL model checking is PTIME but LTL is PSPACE.**
CTL's restriction (temporal operator always paired with path quantifier) enables the
linear-time labeling algorithm. LTL requires automaton construction (exponential in formula).
CTL* (both) is EXPTIME.

**BMC finding no counterexample is not a proof.**
BMC unrolls k steps. If no bug in k steps: no counterexample of length <= k, not "no bug."
You need either infinite k (impractical) or IC3/PDR for actual safety proofs.

**Fairness in model checking.**
Without fairness, a process that can always run may always be blocked by the scheduler
in a model. Fairness assumptions (weak fairness, strong fairness) constrain the scheduler
to explore "reasonable" executions. LTL with fairness: G F enabled -> G F executed.
