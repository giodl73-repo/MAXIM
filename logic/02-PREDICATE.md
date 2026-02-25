# First-Order Predicate Logic

## The Big Picture

First-Order Logic (FOL) — also called first-order predicate logic or predicate calculus — extends
propositional logic with quantifiers over a domain. It is the lingua franca of mathematics: set
theory, number theory, and group theory are all expressed in FOL. It is complete (Gödel 1929) but
undecidable (Church-Turing 1936).

```
+-------------------------------------------------------------------+
|                    FIRST-ORDER LOGIC LANDSCAPE                    |
|                                                                   |
|  SYNTAX                      SEMANTICS                            |
|  +--------------------+      +----------------------------+       |
|  | Terms:             |      | Structure M = (D, I):      |       |
|  |   variables x,y,z  |      |   Domain D (non-empty)     |       |
|  |   constants a,b    |      |   Interpretation I maps:   |       |
|  |   functions f(t)   |      |     constants -> D         |       |
|  | Formulas:          |      |     functions -> D^k -> D  |       |
|  |   atoms P(t1..tk)  |      |     predicates -> P(D^k)   |       |
|  |   connectives      |      |   Variable assignment s    |       |
|  |   Forall x. phi    |      |   M,s |= phi               |       |
|  |   Exists x. phi    |      +----------------------------+       |
|  +--------------------+                                           |
|                                                                   |
|  PROOF THEORY                DECIDABLE FRAGMENTS                  |
|  +--------------------+      +----------------------------+       |
|  | Natural deduction  |      | Monadic FOL (no functions) |       |
|  | Sequent calculus   |      | Presburger arithmetic      |       |
|  | Hilbert axioms     |      | Quantifier-free (QF)       |       |
|  | Resolution         |      | AE sentences (forall-exists|       |
|  +--------------------+      |   in prenex normal form)   |       |
|                              +----------------------------+       |
|                                                                   |
|  KEY THEOREMS                                                     |
|  +-----------------------------------------------------------+    |
|  | Completeness (Godel 1929)   Compactness                   |    |
|  | Undecidability (Church-Turing 1936)  Lowenheim-Skolem     |    |
|  +-----------------------------------------------------------+    |
+-------------------------------------------------------------------+
```

---

## Syntax

### Language Signature

A signature sigma = (C, F, P) specifies:
- **Constants** C: a, b, c, ...
- **Function symbols** F with arities: f/2, g/1, ...
- **Predicate symbols** P with arities: Less/2, Prime/1, Equal/2, ...

### Terms

Terms denote elements of the domain:
```
  term ::= x              (variable)
         | a              (constant)
         | f(t1, ..., tk)  (function application, f has arity k)

  Examples:
    x                     (just a variable)
    plus(x, s(0))         (x + 1 in Peano notation)
    f(g(a), h(b, c))      (nested functions)
```

### Formulas (Well-Formed Formulas, WFFs)

```
  phi ::= P(t1, ..., tk)   (atomic formula, P has arity k)
        | t1 = t2           (equality, if equality is in signature)
        | bot               (false)
        | neg phi
        | phi land psi
        | phi lor psi
        | phi -> psi
        | phi <-> psi
        | Forall x. phi     (x bound in phi)
        | Exists x. phi     (x bound in phi)
```

### Free vs. Bound Variables

```
  Forall x. (P(x) -> Exists y. Q(x, y))

  Bound: x (by Forall), y (by Exists)
  Free:  none in this formula

  In: P(x) -> Forall x. Q(x, y)
  Bound: x in Q(x,y)
  Free:  x in P(x) [different x!], y
```

A sentence is a formula with no free variables. Only sentences have determinate truth values
in a structure (free variables need an assignment).

---

## Semantics: Structures and Truth

### Structures

A structure M = (D, I) for signature sigma consists of:
```
  D        non-empty domain (the "universe")
  I(a)     element of D, for each constant a
  I(f)     function D^k -> D, for each k-ary function symbol f
  I(P)     subset of D^k, for each k-ary predicate P
```

Example — standard model of arithmetic:
```
  D = {0, 1, 2, 3, ...}   (natural numbers)
  I(0) = 0
  I(s) = successor function
  I(plus) = addition function
  I(times) = multiplication function
  I(Less) = {(m,n) | m < n}
```

### Truth Definition (Tarski 1933)

With variable assignment s: Variables -> D:

```
  M, s |= P(t1,...,tk)   iff   (val(t1),...,val(tk)) in I(P)
  M, s |= t1 = t2         iff   val(t1) = val(t2)
  M, s |= bot              iff   never
  M, s |= neg phi          iff   M, s |/= phi
  M, s |= phi land psi     iff   M, s |= phi and M, s |= psi
  M, s |= phi lor psi      iff   M, s |= phi or M, s |= psi
  M, s |= Forall x. phi    iff   for ALL d in D: M, s[x:=d] |= phi
  M, s |= Exists x. phi    iff   for SOME d in D: M, s[x:=d] |= phi

  where val(x) = s(x), val(a) = I(a), val(f(t1..tk)) = I(f)(val(t1)..val(tk))
```

### Validity and Satisfiability

```
  M |= phi          phi is true in M under all variable assignments
  |= phi            phi is valid (true in ALL structures)  [tautology]
  phi is satisfiable  some structure M with some assignment satisfies phi
```

Key: in FOL, validity means true in every possible domain and every interpretation.

---

## Quantifier Rules and Laws

### Quantifier Equivalences

```
  Forall x. phi   ===   neg Exists x. neg phi
  Exists x. phi   ===   neg Forall x. neg phi

  Forall x. (phi land psi)   ===   (Forall x. phi) land (Forall x. psi)
  Exists x. (phi lor psi)    ===   (Exists x. phi) lor  (Exists x. psi)

  Forall x. (phi lor psi)    [NOT equivalent to distributing]
  [unless x not free in phi: then  ===  phi lor Forall x. psi]

  Forall x. Forall y. phi   ===   Forall y. Forall x. phi  [order swappable]
  Exists x. Exists y. phi   ===   Exists y. Exists x. phi  [order swappable]

  Forall x. Exists y. phi   =/=   Exists y. Forall x. phi  [ORDER MATTERS]
```

The last point is crucial: "For every x there exists y..." is weaker than "There exists y
such that for every x..." The Forall-Exists order encodes the structure of a problem
(e.g., game-theoretic reasoning, database queries).

### Prenex Normal Form

Every FOL formula is equivalent to one with all quantifiers out front:
```
  Q1 x1. Q2 x2. ... Qn xn. phi_matrix

  where Q_i in {Forall, Exists} and phi_matrix is quantifier-free.
```

Prenex form is used in resolution theorem proving (Skolemization happens after prenexing).

### Skolemization

Eliminates Exists quantifiers by introducing Skolem functions:
```
  Forall x. Exists y. P(x, y)

  Replace y with f(x) where f is a new function symbol:
  Forall x. P(x, f(x))

  Rule: the Skolem function takes all universally quantified variables
        in scope as arguments.

  Forall x. Forall z. Exists y. P(x, y, z)
  =>  Forall x. Forall z. P(x, f(x,z), z)
```

Skolemization preserves satisfiability (not logical equivalence). The Skolemized formula is
satisfiable iff the original is. Used to put formulas into universal form for resolution.

---

## Herbrand's Theorem

Fundamental theorem connecting FOL satisfiability to propositional satisfiability.

```
  Herbrand Universe H(phi): all ground terms constructible from
  the constants and function symbols in phi (plus a constant if none present).

  Herbrand Base: all ground atomic formulas using predicates from phi.

  Herbrand's Theorem (1930):
    A universal formula Forall x1...xn. phi is UNSATISFIABLE
    iff
    some FINITE set of ground instances of phi is propositionally unsatisfiable.

  Consequence: FOL is semi-decidable.
    For UNSAT: we can enumerate ground instances until we find a propositional refutation.
    For SAT: we might enumerate forever without conclusion.
```

This is the theoretical basis for resolution theorem proving: work with Herbrand instances.

---

## Unification

Unification is the algorithm for making two terms identical by substituting variables.

```
  Problem: find substitution sigma such that sigma(t1) = sigma(t2)

  Examples:
    f(x, a)  and  f(b, y)
    MGU: {x -> b, y -> a}
    Result: f(b, a)

    f(x, x)  and  f(a, b)
    FAIL: x would need to be both a and b

    f(x, g(x))  and  f(g(y), y)
    Naive: {x -> g(y)} then {y -> g(y)} but then y = g(g(y)) = ...
    FAIL (occur check): x appears in g(x), so x -> g(x) would be circular
```

### Robinson's Unification Algorithm

```
  unify(s, t):
    if s = t: return {} (empty substitution)
    if s is variable x:
      if x in vars(t): FAIL (occur check)
      return {x -> t}
    if t is variable x:
      if x in vars(s): FAIL (occur check)
      return {x -> s}
    if s = f(s1..sk), t = f(t1..tk):
      sigma1 = unify(s1, t1)
      sigma2 = unify(sigma1(s2), sigma1(t2))
      ...
      return sigma_k o ... o sigma1
    else: FAIL (different function symbols or arities)
```

Most General Unifier (MGU): unification produces the most general solution; all other
unifiers are instantiations of the MGU.

---

## Decidable Fragments of FOL

FOL overall is undecidable, but fragments are:

| Fragment | Decidability | Notes |
|----------|--------------|-------|
| Monadic FOL (no function symbols, unary predicates only) | Decidable | Löwenheim 1915 |
| Presburger arithmetic (add but no mult over naturals) | Decidable | 2EXP-complete |
| Quantifier-free (QF) fragments | Decidable | Depends on theory |
| AE sentences (forall...exists, quantifier-free matrix, no functions) | Decidable | Ackermann class |
| EA sentences with unary predicates | Decidable | |
| Full FOL with arithmetic (Peano) | Undecidable | Church-Turing 1936 |
| FOL over reals (Tarski) | Decidable | But very high complexity |

The theory of real closed fields (Tarski 1948) is decidable — FOL about real numbers with
+, *, 0, 1, <. This is the theoretical basis for reasoning about polynomial inequalities.

---

## First-Order Theories

A **theory** is a set of sentences closed under logical consequence.

### Key Theories

```
  THEORY OF EQUALITY (=):
    Reflexivity, symmetry, transitivity, congruence.
    Decidable (free theory of equality).

  PEANO ARITHMETIC (PA):
    0, s (successor), +, x, induction schema.
    Undecidable. Incomplete (Godel 1931).

  PRESBURGER ARITHMETIC:
    0, 1, + over naturals. No multiplication.
    Decidable (doubly exponential).

  THEORY OF REAL CLOSED FIELDS (RCF):
    0, 1, +, *, < over reals.
    Decidable (Tarski 1948) but nonelementary.

  ROBINSON ARITHMETIC (Q):
    PA minus induction schema.
    Undecidable. Can interpret enough arithmetic to apply Godel.
```

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Express "every x has a property" | Forall x. P(x) |
| Express "some x has a property" | Exists x. P(x) |
| Negate a universal | neg Forall x. phi  ===  Exists x. neg phi |
| Negate an existential | neg Exists x. phi  ===  Forall x. neg phi |
| Eliminate Exists for resolution | Skolemization |
| Make two terms match by substitution | Unification (Robinson's algorithm) |
| Check satisfiability of ground formula | Herbrand lifting -> propositional SAT |
| Decide arithmetic without multiplication | Presburger arithmetic decision procedure |
| Decide real polynomial arithmetic | Tarski's quantifier elimination (CAD algorithm) |

---

## Common Confusion Points

**Free vs. bound variables.**
In Forall x. P(x), the x is bound. In P(x) land Q(y), both x and y are free. Free variables
are like parameters; their truth depends on the assignment. Bound variables are renamed
consistently — Forall x. P(x) is the same as Forall z. P(z) (alpha-renaming).

**Quantifier order matters.**
Forall x. Exists y. y > x (true in naturals) vs. Exists y. Forall x. y > x (false in naturals).
Swapping Forall and Exists changes the meaning. This is the most common error.

**Terms vs. formulas.**
Terms denote objects: f(x, a). Formulas express properties/relations: P(f(x, a)).
You cannot quantify over predicates in FOL — that would be second-order.

**Skolemization is not equivalence-preserving.**
Forall x. Exists y. P(x, y) and Forall x. P(x, f(x)) are not logically equivalent —
they may have different models. But they are equisatisfiable: one is satisfiable iff the other is.

**The occur check.**
Unification without occur check (as in standard Prolog) can produce circular substitutions that
are unsound. Standard Prolog omits it for efficiency, which is technically unsound but rarely
matters in practice.
