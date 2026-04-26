# Logic Foundations for Formal Methods

## The Big Picture

Formal verification runs on logic. Every tool in the landscape — model checkers, SMT
solvers, proof assistants — is ultimately manipulating logical formulas. This is the
layer map:

```
+--------------------------------------------------------------------------+
|                        LOGIC LAYERS                                      |
|                                                                            |
|  PROPOSITIONAL LOGIC         "P and Q implies R"                         |
|  SAT Solvers: DPLL, CDCL     NP-complete, but practical at millions vars |
|  MiniSat, CaDiCaL, Kissat                                                |
+--------------------------------------------------------------------------+
         |   embeds into
         v
+--------------------------------------------------------------------------+
|  FIRST-ORDER LOGIC (FOL)     Quantifiers over domains                    |
|  "For all x, if P(x) then Q(x)"                                          |
|  Semi-decidable (not fully decidable) — halting problem lurks here       |
+--------------------------------------------------------------------------+
         |   decidable fragments
         v
+--------------------------------------------------------------------------+
|  SMT: SATISFIABILITY MODULO THEORIES                                     |
|  "This formula over integers/arrays/bitvectors" — is it satisfiable?     |
|  DPLL(T) architecture: SAT core + theory solvers                         |
|  Z3, CVC5, Yices2 — the engines behind Dafny, CBMC, Infer, Lean 4      |
+--------------------------------------------------------------------------+
         |   specialized logics
         v
+--------------------------------------------------------------------------+
|  TEMPORAL LOGICS             Reasoning about TIME and STATE SEQUENCES    |
|  LTL: linear time (paths)    "Always p", "Eventually q", "p Until q"     |
|  CTL: branching time (trees) "There exists a path where...", "All paths" |
|  CTL*: full (unifies both)   Expressiveness: LTL ⊄ CTL, CTL ⊄ LTL      |
|  Used in: model checkers (SPIN, NuSMV, TLC)                              |
+--------------------------------------------------------------------------+
         |   proof systems
         v
+--------------------------------------------------------------------------+
|  HIGHER-ORDER LOGIC (HOL)    Quantify over predicates and functions      |
|  Expressiveness: all of math  Decidability: none (semi-decidable at best)|
|  Used in: Isabelle/HOL, HOL4, Coq (via CIC), Lean 4                    |
+--------------------------------------------------------------------------+
```

---

## Propositional Logic and SAT

You know propositional logic. The interesting part here is the SAT solver story — how
NP-complete problems became routinely solvable in practice.

### CNF and the Resolution Proof System

SAT solvers require input in **conjunctive normal form (CNF)**:
a conjunction of clauses, where each clause is a disjunction of literals.

```
  (x1 v -x2 v x3) /\ (-x1 v x4) /\ (x2 v -x3 v -x4)

  Satisfying assignment: x1=T, x2=F, x3=T, x4=T
```

**Resolution rule** (the core proof step):

```
  If you have:    (A v x)     and    (-x v B)
  Derive:         (A v B)            (resolvent)

  Proof of unsatisfiability = derive the empty clause
  (requires a complete derivation — exponential in worst case)
```

### DPLL: The Algorithmic Foundation (1960/1962)

Davis-Putnam-Logemann-Loveland. Everything since is a refinement of this:

```
  DPLL(formula F):
    1. Unit propagation:  If a unit clause (single literal) exists,
                          force it true, simplify F.
    2. Pure literal:      If a literal appears only positive (or only
                          negative), set it to satisfy all its clauses.
    3. Branch:            Pick an unassigned variable x.
                          Try DPLL(F[x=T]).
                          If unsat, try DPLL(F[x=F]).
    4. Return sat or unsat.

  Key insight: unit propagation does most of the work.
               Branching is rare on well-structured instances.
```

### CDCL: Conflict-Driven Clause Learning (Modern SAT Solvers)

The leap from research to industrial-scale SAT. Core idea: when a contradiction is
reached, learn a new clause that prevents the same mistake, and backjump past the
decision level that caused it.

```
  CDCL algorithm:
  ┌─────────────────────────────────────────────┐
  │  1. Unit propagate                          │
  │     If conflict: goto ANALYZE               │
  │  2. If all vars assigned: return SAT        │
  │  3. Decide: pick next variable, assign it   │
  │     (decision heuristic: VSIDS)             │
  │  4. Goto 1                                  │
  │                                             │
  │  ANALYZE (conflict analysis):               │
  │  - Walk implication graph to find           │
  │    1-UIP (unique implication point)         │
  │  - Learn conflict clause from cut           │
  │  - Backjump to appropriate decision level   │
  │  - If level 0 conflict: return UNSAT        │
  └─────────────────────────────────────────────┘

  Clause learning turns local contradictions into
  global knowledge — future search avoids same mistakes.

  VSIDS (Variable State Independent Decaying Sum):
  - Track how often each variable appears in conflict clauses
  - Decay all scores periodically
  - Prioritize highest-score variables for branching
  - Effect: focuses search on "hot" parts of the problem
```

**Modern SAT performance (2024):**
- MiniSat (2003): ~1M variable problems routine
- CaDiCaL / Kissat (2020+): ~10M+ variables on industrial instances
- Competition instances (SAT Competition): 10M+ clauses, seconds to minutes

---

## First-Order Logic

You know FOL from MIT. The verification-relevant concepts:

### Herbrand's Theorem and the Decidability Boundary

```
  FOL = semi-decidable (r.e. but not co-r.e.)
  - If a formula is valid, there exists a finite proof
  - If a formula is invalid, no procedure is guaranteed to terminate

  Herbrand's theorem: A formula is unsatisfiable iff some
  finite set of ground instances (no variables) is unsatisfiable.

  This is the foundation of resolution theorem proving:
  saturate the ground instances with resolution,
  derive contradiction if unsatisfiable.

  Key fragments that ARE decidable:
  +----------------------------+---------------------+-----------+
  | Fragment                   | Decidability        | Complexity |
  +----------------------------+---------------------+-----------+
  | Propositional logic        | Decidable           | NP-complete|
  | Monadic FOL (1-var preds)  | Decidable           | 2-EXPTIME  |
  | Presburger arithmetic      | Decidable           | 2-EXPTIME  |
  | (linear integer arithmetic)|                     |            |
  | Quantifier-free FOL        | Decidable (via SMT) | NP-hard    |
  | Full FOL                   | Semi-decidable      | r.e.       |
  | FOL + arithmetic           | Undecidable         | N/A        |
  +----------------------------+---------------------+-----------+
```

### Unification

The core operation in resolution theorem proving (and type inference):

```
  Find substitution s such that s(t1) = s(t2)

  Example:
    t1 = f(x, g(y))
    t2 = f(h(a), g(z))
    Unifier: { x -> h(a), y -> z }  (or equivalently z -> y)

  Most general unifier (MGU): the "simplest" substitution.
  Unification is decidable and O(n alpha(n)) — practically linear.
  Occurs check: x cannot unify with a term containing x.
  (Prolog omits occurs check for speed — unsound but fast.)
```

### Resolution Refutation for FOL

```
  To prove: P is valid (i.e., |-  P)
  Equivalent: prove -P is unsatisfiable (proof by contradiction)

  1. Negate the goal: take -P
  2. Skolemize: eliminate existential quantifiers
     (introduce Skolem functions/constants)
  3. Convert to CNF
  4. Apply resolution repeatedly until empty clause derived
     (or until saturated — then P was not provable this way)

  This is the basis of Vampire, E, and Prover9 —
  the first-order ATP provers that Isabelle's Sledgehammer calls.
```

---

## SMT: Satisfiability Modulo Theories

SMT is where propositional SAT meets first-order theories. The key insight: instead of
searching over all possible interpretations of FOL (undecidable), restrict to specific
theories with known decision procedures.

### Theories in Z3

```
  +------------------+---------------------------------------+--------------+
  | Theory           | Domain                                | Abbreviation |
  +------------------+---------------------------------------+--------------+
  | EUF              | Uninterpreted functions + equality    | EUF          |
  | Linear arithmetic| Integer or real linear constraints    | LIA / LRA    |
  | Nonlinear arith. | Polynomial constraints                | NIA          |
  | Bit-vectors      | Fixed-width integers, hardware-like   | BV           |
  | Arrays           | Extensional arrays, select/store      | A            |
  | Strings          | String constraints                    | S            |
  | Datatypes        | Algebraic data types (lists, trees)   | DT           |
  | Floating point   | IEEE 754 semantics                    | FP           |
  +------------------+---------------------------------------+--------------+

  Combinations: Z3 handles combinations of theories via
  Nelson-Oppen combination: exchange equality constraints
  between theory solvers until a fixed point or contradiction.
```

### DPLL(T) Architecture

```
  ┌──────────────────────────────────────────────────────┐
  │                    DPLL(T) CORE                      │
  │                                                        │
  │  SAT Solver                 Theory Solver T          │
  │  ────────────               ─────────────────        │
  │  Works on              <--> Handles T-consistency    │
  │  propositional          |   of assignments           │
  │  abstraction            |                            │
  │  of the formula         |   Theory propagation:      │
  │                         |   infer literals forced    │
  │  Assigns T-atoms:   --->|   by T-constraints         │
  │  (x + y <= 5)           |                            │
  │  (a[i] = b[j])          |   Theory conflict:         │
  │  (f(a) = f(b))      <---|   return explanation clause |
  │                                                        │
  │  If T-consistent: continue                           │
  │  If T-conflict:   learn clause, backjump             │
  └──────────────────────────────────────────────────────┘

  The SAT solver handles propositional structure.
  Theory solvers handle the semantics of each domain.
  They communicate via learned clauses.
```

### Z3 API Example (Python)

Encoding a simple verification condition — "is this assertion always true?":

```python
from z3 import *

# Verification condition: is it always true that
# if x > 0 and y > 0 then x + y > 0?
x, y = Ints('x y')

# Negate the property, ask if the negation is satisfiable
# If UNSAT: original property holds. If SAT: counterexample.
s = Solver()
s.add(x > 0)
s.add(y > 0)
s.add(Not(x + y > 0))   # negated conclusion

result = s.check()
# result = unsat  (the negation has no model)
# Therefore: x > 0 /\ y > 0 => x + y > 0  is valid.

# Counterexample finding:
a, b = Ints('a b')
s2 = Solver()
s2.add(a >= 0, b >= 0)
s2.add(Not(a * b >= 0))  # is a*b >= 0 always true for non-neg a,b?
# result = unsat for integers (a*b >= 0 when a,b >= 0)

# Finding a counterexample:
s3 = Solver()
s3.add(a >= -10, a <= 10, b >= -10, b <= 10)
s3.add(Not(a + b >= a))  # is a + b >= a always true? (need b >= 0)
print(s3.check())         # sat — there IS a counterexample
print(s3.model())         # e.g., b = -1
```

---

## Temporal Logics

Temporal logics extend propositional/FOL with operators for reasoning over time.
The foundation of model checking.

### LTL: Linear Temporal Logic

LTL reasons about a single infinite path (sequence of states):

```
  Path: s0 -> s1 -> s2 -> s3 -> ...

  Operators:
  ┌───────┬───────────────────────────────────────────────────┐
  | X p   | NEXT: p holds in the next state (s1)              |
  | G p   | GLOBALLY (always): p holds in all states          |
  |       | (also written as □p)                              |
  | F p   | FINALLY (eventually): p holds in some future      |
  |       | state (also written as ◇p)                        |
  | p U q | UNTIL: p holds until q becomes true               |
  |       | (q must eventually become true)                   |
  | p W q | WEAK UNTIL: p holds until q, or p holds forever   |
  | p R q | RELEASE: q holds until (and including) p does     |
  └───────┴───────────────────────────────────────────────────┘

  Examples:
  G (request -> F response)    "Every request is eventually answered"
  G (critical -> X -critical)  "Critical section is released in next step"
  G (-deadlock)                 "No deadlock ever"
  F G stable                    "Eventually, the system reaches stable state"
```

### CTL: Computation Tree Logic

CTL reasons about a tree of all possible futures (branching time):

```
  Tree:        s0
              / \
            s1   s2
           / \     \
          s3  s4    s5
          ...

  Path quantifiers: A (all paths), E (exists a path)
  Combined with temporal operators: X, G, F, U

  But CTL requires operators to be paired:
  AX p   - All next states: p holds in ALL successors
  EX p   - Exists next state: p holds in SOME successor
  AG p   - All paths, always: p holds on all states of all paths
  EG p   - Exists a path: p holds globally on that path
  AF p   - All paths, eventually: p holds on all paths
  EF p   - Exists a path: p holds eventually on that path
  A[p U q] - All paths: p until q
  E[p U q] - Exists a path: p until q

  Key CTL properties:
  AG (-deadlock)             "No reachable deadlock on any path"
  AG (request -> AF response) "All paths: every request answered"
  EF (state = ready)         "It's possible to reach ready state"
```

### CTL vs LTL: The Expressiveness Gap

This is subtle and important — neither subsumes the other:

```
  Expressible in LTL but not CTL:
    FG p  ("eventually always p" — along EVERY path)
    The path quantifier is implicit in LTL (all paths).

  Expressible in CTL but not LTL:
    EG p  ("there EXISTS a path where p always holds")
    CTL can talk about SOME path; LTL cannot.

  CTL* unifies both:
  - Path quantifiers (A, E) can appear anywhere
  - Fully subsumes both LTL and CTL
  - But CTL* model checking is harder (PSPACE-complete vs
    CTL: polynomial, LTL: PSPACE-complete)

  In practice:
  - TLA+ uses a variant of LTL with action formulas
  - SPIN uses LTL (checks all paths implicitly)
  - NuSMV supports both CTL and LTL
  - Hardware verification mostly uses CTL (local properties easier)
```

### Buchi Automata: The LTL/Automata Connection

LTL model checking reduces to Buchi automaton intersection emptiness:

```
  LTL Formula phi
       |
       | (translate — exponential in worst case, polynomial for common formulas)
       v
  Buchi Automaton A_phi     (accepts exactly the infinite paths satisfying phi)
       |
       |  [also build]
       v
  Buchi Automaton A_M       (state space of the system M as an automaton)
       |
       | intersect
       v
  A_M x A_(-phi)            (paths of M that violate phi)
       |
       | check emptiness (does it accept any infinite word?)
       v
  Empty -> phi holds for all paths of M   (return "verified")
  Non-empty -> pull out accepting run      (return counterexample)

  Emptiness of Buchi automata = reachability of an accepting state
  in a strongly connected component (SCC).
  Standard algorithm: Tarjan's SCC + reachability.
  This is the core of SPIN.
```

---

## Modal Logic

Modal logic adds operators for necessity (box) and possibility (diamond):

```
  Kripke structure: M = (W, R, V)
    W = set of possible worlds (states)
    R = accessibility relation between worlds
    V = valuation (which propositions hold where)

  □p  (necessarily p): p holds in ALL worlds accessible from here
  ◇p  (possibly p):    p holds in SOME world accessible from here

  Modal systems (axiom schemas):
  K:  □(p -> q) -> (□p -> □q)       (distribution — all systems)
  T:  □p -> p                         (reflexivity — what's necessary is true)
  4:  □p -> □□p                      (transitivity — S4 = K + T + 4)
  5:  ◇p -> □◇p                      (euclidean — S5 = S4 + 5)

  S5 with multiple agents = epistemic logic:
    K_i(p)  "agent i knows p"
    Used in: cryptographic protocol verification (BAN logic),
             distributed knowledge reasoning, game theory
```

---

## Godel Incompleteness: What It Actually Means for Verification

You know the theorems. Here is the precise implication for formal verification:

```
  Godel First Incompleteness Theorem:
  Any consistent formal system F that can express basic arithmetic
  contains a true statement that F cannot prove.

  What this DOES mean for verification:
  - No complete proof system for arithmetic exists
  - Any automated prover will have unprovable true statements
  - Interactive provers (Coq, Lean) cannot escape this — they
    rely on you to provide the key insights

  What this does NOT mean:
  - It does not mean "verification is impossible"
  - For specific finite state systems: model checking is complete
    within the state space (no Godel issues)
  - For decidable theories (Presburger arithmetic, linear arithmetic):
    decision procedures exist that are sound AND complete
    for that theory
  - The incompleteness is about the general case, not specific
    domains we actually care about in practice

  Rice's Theorem (more relevant in practice):
  Any non-trivial semantic property of programs is undecidable.
  This means: no tool can be simultaneously:
    1. Sound (no false negatives — never misses a real bug)
    2. Complete (no false positives — never flags non-bugs)
    3. Terminating (always gives an answer)
  You pick two. Modern static analyzers pick (1) + (3): sound
  and terminating, but with false positives.
```

---

## Decidability Reference

```
  DECIDABLE FRAGMENTS (relevant to verification):
  +-----------------------------------+-----------+------------------------------+
  | Theory / Fragment                 | Complexity| Solver                       |
  +-----------------------------------+-----------+------------------------------+
  | Propositional logic (SAT)         | NP-complete| Z3, CaDiCaL, MiniSat        |
  | Linear arithmetic (integers)      | NP-hard   | Z3 (LIA theory solver)       |
  | Linear arithmetic (reals)         | PTIME     | Simplex in Z3                |
  | Presburger arithmetic             | 2-EXPTIME | Z3 / Omega                   |
  | Quantifier-free linear arith.     | PTIME     | Simplex                      |
  | Quantifier-free bitvectors        | NP-complete| Z3 (BV theory solver)        |
  | Arrays (quantifier-free)          | NP-hard   | Z3 (array theory solver)     |
  | Monadic second-order logic        | decidable | MONA tool                    |
  | Linear temporal logic (model ck.) | PSPACE    | SPIN, TLC                    |
  | CTL model checking                | P         | NuSMV                        |
  | First-order logic (full)          | semi-dec. | Prover9, Vampire, E          |
  | Higher-order logic                | semi-dec. | Isabelle, Coq, Lean 4        |
  | FOL + arithmetic (mixed)          | undecidable| n/a (approximations only)   |
  +-----------------------------------+-----------+------------------------------+
```

---

## Decision Cheat Sheet

| I need to... | Logic / Tool |
|---|---|
| Check if a propositional formula is satisfiable | SAT solver (Z3, CaDiCaL) |
| Verify a property over integer arithmetic | SMT with LIA theory (Z3) |
| Check memory safety of C code (buffer, overflow) | SMT with BV theory (CBMC -> Z3) |
| Verify a distributed protocol safety property | LTL/CTL model checker (TLC, SPIN) |
| Express "every request eventually gets a response" | LTL: G(request -> F response) |
| Express "there is a path to the error state" | CTL: EF(error) |
| Check that a state is reachable on some execution | CTL: EF(state) |
| Prove an algorithm correct for all inputs | FOL + proof assistant (Lean, Coq) |
| Reason about what an agent knows | Epistemic logic (S5 + K_i operators) |
| Determine if two programs have the same behavior | Bisimulation (process algebra) |

---

## Common Confusion Points

**"SAT is NP-complete, so it's impractical"**

NP-complete means worst-case exponential. Modern SAT solvers with CDCL handle
industrial instances (millions of variables) in seconds. The average case is
tractable. Worst-case inputs are rare in practice.

**"LTL and CTL are the same thing with different notation"**

They have strictly different expressiveness:
- LTL: FG p is expressible; EG p is not (no path quantifier)
- CTL: EG p is expressible; FG p is not (operators must be paired)
Use LTL when you want "on every execution path"; use CTL when you want
"there exists an execution where."

**"SMT solver = theorem prover"**

An SMT solver decides satisfiability of quantifier-free formulas over theories.
It cannot prove universally quantified statements directly (it would need to
enumerate all possible inputs). Proof assistants use SMT oracles for specific
subgoals, but the proof structure is constructed separately.

**"Godel means we cannot verify anything important"**

Godel incompleteness concerns infinite domains and universal statements about all
programs. Finite-state model checking has no incompleteness issue — it exhausts
the state space. For infinite-state systems, the relevant limit is undecidability
(Rice's Theorem), which means you choose what soundness/completeness tradeoffs
to make.

**"Temporal logic requires knowing the full execution history"**

The opposite. Temporal logic formulas are evaluated at a state — the semantics
looks forward (future), not backward. Past operators exist (LTL-past) but are
not standard. Model checking explores forward from the initial state.
