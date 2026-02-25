# Propositional Logic and Truth Tables

## The Big Picture

Propositional logic (PL) is the simplest logic: Boolean variables, connectives, no quantifiers.
Everything is decidable. It is the foundation for SAT solvers, circuit verification, BDDs, and
all hardware design.

```
+------------------------------------------------------------------+
|               PROPOSITIONAL LOGIC LANDSCAPE                      |
|                                                                  |
|  SYNTAX             SEMANTICS            ALGORITHMS              |
|  +-----------+      +-----------+        +-----------+           |
|  | Formulas  |      | Truth     |        | Truth     |           |
|  | built from|      | tables    |        | table     |           |
|  | atoms and |      |           |        | (2^n rows)|           |
|  | connectives      | Valuation |        | DPLL      |           |
|  +-----------+      | (atoms -> |        | CDCL      |           |
|                     |  {0,1})   |        | BDD       |           |
|  NORMAL FORMS       +-----------+        | Resolution|           |
|  +-----------+                           +-----------+           |
|  | NNF       |      SATISFIABILITY                               |
|  | CNF       |      +-----------+        APPLICATIONS            |
|  | DNF       |      | SAT       |        +-----------+           |
|  | Tseitin   |      | (NP-comp) |        | Circuit   |           |
|  +-----------+      | UNSAT     |        | hardware  |           |
|                     | Tautology |        | SMT base  |           |
|                     +-----------+        | Bounded MC|           |
|                                          +-----------+           |
+------------------------------------------------------------------+
```

---

## Syntax

### Language

A propositional formula is built from:
- **Atoms**: p, q, r, ... (propositional variables)
- **Connectives**: neg (not), land (and), lor (or), implies (->), iff (<->)
- **Constants**: top (true), bot (false)

Grammar:
```
phi ::= p                   (atom)
      | top | bot           (constants)
      | neg phi             (negation)
      | phi land phi        (conjunction)
      | phi lor phi         (disjunction)
      | phi -> phi          (implication)
      | phi <-> phi         (biconditional)
      | (phi)               (parentheses)
```

### Operator Precedence (high to low)

```
  neg       (highest — tightest binding)
  land
  lor
  ->        (right-associative: p -> q -> r means p -> (q -> r))
  <->       (lowest)
```

---

## Semantics: Truth Tables

A **valuation** v maps atoms to {0,1}. Truth of a formula under v is defined inductively:

| phi | v(phi) |
|-----|--------|
| p | v(p) |
| top | 1 |
| bot | 0 |
| neg phi | 1 - v(phi) |
| phi land psi | min(v(phi), v(psi)) |
| phi lor psi | max(v(phi), v(psi)) |
| phi -> psi | 0 iff v(phi)=1 and v(psi)=0, else 1 |
| phi <-> psi | 1 iff v(phi) = v(psi) |

### Truth Table for Core Connectives

```
  p   q  | neg p  p land q  p lor q  p -> q  p <-> q
  --------|--------------------------------------------------
  0   0  |   1       0         0        1        1
  0   1  |   1       0         1        1        0
  1   0  |   0       0         1        0        0
  1   1  |   0       1         1        1        1
```

Key observations:
- **Implication** is false only when antecedent is true and consequent is false.
- **Biconditional** is true exactly when both sides have the same value.
- Material implication (p -> q) is equivalent to (neg p lor q).

---

## Normal Forms

### Negation Normal Form (NNF)

Only neg appears immediately in front of atoms. Push negations inward using De Morgan:
```
  neg(phi land psi)  ===  (neg phi lor neg psi)
  neg(phi lor psi)   ===  (neg phi land neg psi)
  neg neg phi        ===  phi
  neg(phi -> psi)    ===  (phi land neg psi)
```

### Conjunctive Normal Form (CNF)

Conjunction of disjunctions (clauses):
```
  CNF: (p lor q lor neg r) land (neg p lor s) land (q lor neg s)

  Clause: disjunction of literals
  Literal: atom or its negation
```

**Why CNF matters**: SAT solvers operate on CNF. Resolution works on clauses. All major
algorithms (DPLL, CDCL) require CNF input.

### Disjunctive Normal Form (DNF)

Disjunction of conjunctions (terms/minterms):
```
  DNF: (p land q) lor (neg p land r) lor (neg q land neg r)
```

DNF makes satisfiability trivial (check if any term is satisfiable — i.e., no atom and its
negation in the same term). But DNF can be exponentially larger than the original formula.

### Tseitin Transformation

CNF conversion without exponential blowup. Introduce fresh variables for subformulas:
```
  For each subformula psi, introduce variable x_psi.
  Add clauses encoding: x_psi <-> [definition of psi in terms of subformulas].

  Example: phi = p land (q lor neg r)
  x1 = q lor neg r   => add: (neg x1 lor q lor neg r) land (neg q lor x1) land (r lor x1)
  x2 = p land x1     => add: (neg x2 lor p) land (neg x2 lor x1) land (neg p lor neg x1 lor x2)
  Add: x2   (top-level must be true)

  Result: linear in size of original formula (vs. exponential for naive CNF).
```

Tseitin is what every SAT preprocessor does. You feed it an arbitrary formula; it outputs
an equisatisfiable CNF of linear size.

---

## SAT: The Satisfiability Problem

**Problem**: Given a propositional formula phi, does there exist a valuation making phi true?

### Complexity

```
  SAT is NP-complete (Cook 1971, Levin 1973).

  Certificates: a satisfying valuation is polynomial to verify.
  Hardness: every NP problem reduces to SAT in polynomial time.

  Special cases:
  2-SAT (each clause has 2 literals):  decidable in O(n+m) via SCC
  3-SAT:                               NP-complete
  Horn-SAT (at most 1 positive literal per clause): P (unit propagation)
  MAX-SAT:                             NP-hard optimization
```

### DPLL Algorithm

Davis-Putnam-Logemann-Loveland (1960/1962). The foundation of all modern SAT solvers.

```
  DPLL(phi):
    Apply unit propagation:
      If clause has single literal l, set l=true, simplify.
    Apply pure literal rule:
      If p appears only positive, set p=true. Only negative, set p=false.
    If phi is empty (all clauses satisfied): return SAT.
    If phi contains empty clause: return UNSAT.
    Choose atom p via heuristic.
    Return DPLL(phi[p:=true]) or DPLL(phi[p:=false]).
```

```
  DPLL search tree for (p lor q) land (neg p lor r) land (neg q lor neg r):

                     root
                   /       \
              p=T              p=F
             /                   \
      (r) land (neg q lor neg r)  (q) land (neg q lor neg r)
          /          \                 /              \
       r=T          r=F             q=T              q=F
       check        BACKTRACK       (neg r)          UNSAT (empty clause)
       neg q lor neg r              r=F: SAT
```

### CDCL: Conflict-Driven Clause Learning

Modern SAT solvers (MiniSat, CaDiCaL, Kissat) use CDCL — DPLL plus:
- **Conflict analysis**: When UNSAT branch hit, analyze the conflict to learn a new clause.
- **Non-chronological backjumping**: Jump back further than 1 level.
- **VSIDS heuristic**: Variable State Independent Decaying Sum — prioritize recently conflicted variables.

CDCL can solve industrial instances with millions of variables. The learned clause database
grows but is periodically cleaned (clause forgetting/restarts).

---

## Binary Decision Diagrams (BDDs)

Alternative to CNF for representing Boolean functions compactly.

```
  Formula: (p land q) lor (neg p land r)

  BDD (ordered by p, q, r):

              p
             / \
           T     F
           |     |
           q     r
          / \   / \
         T   F T   F
         |   | |   |
        [1] [0][1] [0]

  Reduced Ordered BDD (ROBDD): canonical form.
  - Merge identical subgraphs.
  - Remove redundant tests (both branches lead to same node).
```

BDDs are canonical (same formula = same graph). Operations (and, or, neg) are polynomial on
BDD size. But worst case BDD size is exponential (multiplication function, for instance).

**Use cases**: Hardware equivalence checking (used at Intel, IBM), symbolic model checking,
formal verification of circuits.

---

## Resolution

Proof system for propositional logic over clauses.

```
  Resolution rule:
        C1 lor p        C2 lor neg p
        ───────────────────────────────
               C1 lor C2

  Example:
        (p lor q)  and  (neg p lor r)
        resolving on p:  (q lor r)

  Resolution refutation:
        To prove phi is UNSAT, resolve until deriving empty clause [].
```

```
  Soundness: if empty clause is derived, formula is UNSAT.
  Completeness (for refutation): if formula is UNSAT, empty clause is derivable.

  Not polynomially bounded for all proofs (exponential lower bounds exist).
```

Resolution is the basis of:
- Prolog's SLD resolution (ordered, selected literal, linear)
- Early automated theorem provers (Robinson 1965)
- The Davis-Putnam procedure (precursor to DPLL)

---

## Functional Completeness

A set of connectives is **functionally complete** if every Boolean function is expressible.

```
  {neg, land}:         Complete  (De Morgan: lor = neg(neg p land neg q))
  {neg, lor}:          Complete
  {neg, ->}:           Complete  (NAND = Sheffer stroke, NOR = Peirce arrow)
  {NAND} alone:        Complete  (neg p = p NAND p)
  {NOR} alone:         Complete  (neg p = p NOR p)
  {land, lor}:         NOT complete (can't express negation)
  {->}:                NOT complete (p->q->p is always true but p is not)
  {land, lor, ->}:     NOT complete (all always monotone)
```

---

## Connection to Circuits

Propositional logic IS circuit design:

```
  Propositional formula         Boolean circuit
  -----------------------       ----------------
  Atom p                        Input wire
  neg p                         NOT gate
  p land q                      AND gate
  p lor q                       OR gate
  SAT(phi)                      Circuit has input making output 1
  UNSAT(phi)                    Circuit never outputs 1
  Tautology(phi)                Circuit always outputs 1

  Circuit satisfiability is NP-complete (same as SAT).
  Circuit equivalence is co-NP-complete.
```

This is why SAT solvers are used in hardware verification. The question "do these two circuits
compute the same function?" reduces to "is this circuit unsatisfiable?" — which SAT handles.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Check if formula is satisfiable | DPLL / CDCL SAT solver (e.g., Z3, CaDiCaL) |
| Convert to CNF without blowup | Tseitin transformation |
| Check tautology | Check UNSAT of negation |
| Check equivalence of two formulas | Check UNSAT of (phi XOR psi) |
| Represent Boolean function canonically | ROBDD |
| Prove propositional validity via rules | Resolution refutation |
| Decide 2-SAT efficiently | SCC on implication graph |
| Work with Horn clauses | Unit propagation (linear time) |

---

## Common Confusion Points

**Satisfiable vs. valid vs. tautology.**
A formula is satisfiable if some valuation makes it true. A tautology (valid) is true under
ALL valuations. To check if phi is a tautology: check if neg phi is unsatisfiable.

**Implication in logic vs. implication in English.**
Material implication (p -> q) is true whenever p is false. "If 2+2=5 then the moon is cheese"
is logically true. This shocks everyone once. The repair is strict/relevant implication in
non-classical logics, but PL uses material implication throughout.

**CNF vs. DNF complexity tradeoff.**
CNF makes UNSAT easy to witness (one unsatisfied clause), but SAT is hard (NP-complete).
DNF makes SAT easy to witness (one satisfied term), but UNSAT is hard (co-NP-complete).
Neither wins — the two problems are dual.

**DPLL vs. CDCL.**
DPLL is the algorithm. CDCL is DPLL plus clause learning plus non-chronological backjumping.
Modern solvers are CDCL. "DPLL" often colloquially refers to the whole family.

**BDDs are not always compact.**
BDDs can be exponentially large for some functions (multiplication is a classic example).
The ordering of variables matters enormously. Finding the optimal ordering is NP-complete.
