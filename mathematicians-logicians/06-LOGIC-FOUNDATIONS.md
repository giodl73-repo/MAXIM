# Logic and Foundations — Frege, Russell, Hilbert, Gödel, Church

## The Crisis and Its Resolution

This file covers the most directly relevant chapter for an MIT TCS graduate.
The figures here built and then destroyed and then rebuilt the logical foundations
of mathematics — and in doing so, invented theoretical computer science.

```
THE ARC OF FOUNDATIONS
=======================

FREGE (1879): Invent predicate logic; try to derive all of arithmetic from logic.
  "Begriffsschrift" — the most important logic text since Aristotle.

FREGE (1893): Publish Grundgesetze — formal derivation of arithmetic from logic.

RUSSELL (1902): Send Frege a letter: "Your system has a paradox."
  Set of all sets that don't contain themselves = contradiction.
  Frege: "This strikes at the foundations."

HILBERT (1900–1930): If logic has paradoxes, formalize it MORE carefully.
  Build mathematics on a COMPLETE, CONSISTENT formal system.
  Prove it's consistent. This is the Hilbert program.

GÖDEL (1930): Prove the Completeness Theorem (first-order logic is complete).
  Good news: everything provable is provable.

GÖDEL (1931): Prove the Incompleteness Theorems.
  Any consistent formal system strong enough to express arithmetic
  contains true statements it cannot prove.
  And cannot prove its own consistency.
  Hilbert's program: DEAD.

CHURCH (1936) / TURING (1936): What CAN be computed?
  Church's lambda calculus and Turing machines — equivalent models of computation.
  Halting problem: undecidable (using the diagonal argument).
  The Entscheidungsproblem: unsolvable.

CHURCH-TURING THESIS: These models capture "computation" itself.
```

---

## Gottlob Frege (1848–1925)

### Who He Was

German philosopher and mathematician. Created modern logic essentially alone.
His work was ignored for decades. Russell, reading him in 1901, was so
impressed that he called him the greatest logician since Aristotle —
then immediately sent the letter announcing the paradox.

### The Contribution: Predicate Logic

**Before Frege: Aristotle's Syllogisms**

```
PRE-FREGE LOGIC (Aristotelian syllogisms)
=========================================

All men are mortal.         Pattern: All A are B.
Socrates is a man.                  x is A.
Therefore: Socrates is mortal.      Therefore: x is B.

Limitations:
  - Only 4 logical forms (A, E, I, O statements)
  - Cannot handle relations: "every father loves some child"
  - Cannot handle quantifiers over predicates
  - Essentially useless for formalizing mathematics

Boole (1847) extended this with Boolean algebra —
but Boolean algebra is propositional (no internal structure).
```

**Frege's Begriffsschrift (1879): Predicate Logic**

```
WHAT FREGE INVENTED
=====================

1. QUANTIFIERS: ∀x and ∃x
   "For all x, if P(x) then Q(x)": ∀x (P(x) → Q(x))
   "There exists x such that P(x)": ∃x P(x)

2. FUNCTIONS as first-class logical objects
   f(x) is a function; P(x) is a predicate.
   Can quantify over objects: ∀x, ∃x.
   (Quantifying over predicates is second-order logic — more powerful.)

3. FULL EXPRESSIVENESS for mathematical statements:
   "Every natural number has a successor":
     ∀n (Natural(n) → ∃m (Natural(m) ∧ Successor(n,m)))

   "There are infinitely many primes":
     ∀n (Natural(n) → ∃p (Prime(p) ∧ p > n))

4. PROOF as a formal derivation: every step justified by a rule.

This is the logical framework used in:
  - Mathematical logic (model theory, proof theory)
  - Programming language type systems (dependent types)
  - Database query languages (relational algebra, Datalog)
  - Verification systems (Coq, Lean, Isabelle, Agda)
  - First-order logic (SMT solvers — Z3, CVC5)
```

**Frege's Logicism — The Failed Dream**

Frege's *Grundgesetze der Arithmetik* (1893, 1903) tried to derive all of
arithmetic from pure logic. The key axiom was **Basic Law V**:

{x : F(x)} = {x : G(x)} iff ∀x (F(x) ↔ G(x))

(Two concepts determine the same "extension" iff they apply to exactly
the same objects.) Russell's paradox shows this is inconsistent.

**Russell's Paradox (1902)**

Let R = {x : x ∉ x} — the set of all sets that do not contain themselves.

Does R ∈ R?
- If R ∈ R, then by definition R ∉ R — contradiction.
- If R ∉ R, then R satisfies the condition, so R ∈ R — contradiction.

This uses Frege's Basic Law V to construct an impossible set.
Frege's system was broken. He saw it immediately: "A scientist can
hardly encounter anything more undesirable than to have the foundations
give way just as the work is finished."

---

## Bertrand Russell (1872–1970)

### Who He Was

British mathematician, philosopher, Nobel laureate in Literature, political
activist. *Principia Mathematica* (1910–1913, with A.N. Whitehead) attempted
to rebuild mathematics on solid logical foundations after the paradox.

### The Contribution: Type Theory and *Principia Mathematica*

**Type Theory — The Fix for Russell's Paradox**

```
RUSSELL'S TYPE THEORY
======================

The paradox arises because R = {x : x ∉ x} allows a set to
be a member of itself. Russell's fix: STRATIFY objects into types.

Type hierarchy:
  Type 0: Individuals (atoms)
  Type 1: Sets of individuals — predicates on type 0
  Type 2: Sets of sets of individuals — predicates on type 1
  ...

Rule: A set of type n can only contain elements of type < n.
  Therefore "x ∉ x" is type-theoretically malformed:
  x can't be both a member-of (requiring lower type) and the set itself.

This is the DIRECT ancestor of:
  - Modern type systems in programming languages
  - Haskell's kinds (types of types)
  - Coq/Lean's dependent type hierarchies (Prop, Type 0, Type 1, ...)
  - Universe polymorphism in proof assistants

Russell's paradox → type theory → modern type systems → TypeScript, Rust, etc.
The lineage is direct.
```

**Principia Mathematica (1910–1913)**

PM attempted to derive all of mathematics from a small set of logical axioms
in the ramified type theory. Famous for taking ~360 pages to prove 1 + 1 = 2.

The PM enterprise ultimately failed to be the foundation of mathematics
(Gödel's incompleteness theorems showed no such complete foundation exists),
but it:
- Established formal proof as a rigorous concept
- Made mathematical logic a serious academic discipline
- Directly influenced Hilbert's program and Gödel's work
- The type theory became the foundation of modern programming language theory

---

## David Hilbert (1862–1943)

### Who He Was

German mathematician, Göttingen professor. The most influential mathematician
of the early 20th century. Created or fundamentally reshaped: algebraic
geometry, functional analysis, mathematical physics, logic, and proof theory.
His 23 problems (1900 address) set the agenda for 20th century mathematics.

### The Contribution: Formalism and the Hilbert Program

**Hilbert's Axiomatization Philosophy**

```
HILBERT'S VIEW
===============

Mathematics should be FORMALIZED:
  - All objects are defined by axioms
  - All proofs are formal derivations
  - A proof is valid if it follows the rules, regardless of "meaning"

"Mathematics knows no races or geographic boundaries;
 for mathematics, the cultural world is one country."

The ideal formal system should be:
  1. COMPLETE: every true statement is provable
  2. CONSISTENT: no contradictions (can't prove both P and ¬P)
  3. DECIDABLE: there is an algorithm to determine if any statement is provable

This is the HILBERT PROGRAM.
```

**Hilbert's 23 Problems (1900)**

```
SELECTED HILBERT PROBLEMS — CURRENT STATUS
============================================

Problem 1: Continuum Hypothesis
  Status: INDEPENDENT of ZFC (Gödel 1940, Cohen 1963)

Problem 2: Prove arithmetic is consistent
  Status: IMPOSSIBLE (Gödel 1931 — incompleteness)

Problem 8: Riemann Hypothesis
  Status: OPEN (Millennium Prize Problem)

Problem 10: Algorithm for Diophantine equations
  Status: NO SUCH ALGORITHM (Matiyasevich 1970)

Problem 17: Represent non-negative polynomials as sums of squares
  Status: SOLVED (Artin 1927)

Problem 23: Further development of calculus of variations
  Status: Open-ended — substantially developed

The problems were enormously influential — solving any one was
a career-defining achievement.
```

**Hilbert Spaces**

Hilbert generalized Euclidean space to infinite dimensions:
A Hilbert space H is a complete inner product space.

```
HILBERT SPACES
==============

Finite-dimensional: Rⁿ with dot product
Infinite-dimensional: L²[0,1] = square-integrable functions on [0,1]
  Inner product: ⟨f,g⟩ = ∫₀¹ f(x)g(x)dx
  Norm: ‖f‖ = √⟨f,f⟩

Basis theorem: Every Hilbert space has an orthonormal basis
  {eₙ} such that f = Σ ⟨f,eₙ⟩ eₙ for all f.

For L²[0,1]: The Fourier series is exactly this expansion.
  The Fourier basis {e^(2πinx)} is orthonormal.
  Every L² function = its Fourier series in this sense.

Hilbert spaces are the natural setting for:
  - Quantum mechanics (states are vectors in a Hilbert space)
  - Signal processing (L² functions, Fourier analysis)
  - Machine learning (kernel methods — the kernel is an inner product)
  - PDE theory (Sobolev spaces are Hilbert spaces)
```

---

## Kurt Gödel (1906–1978)

### Who He Was

Austrian-American logician. Paranoid in his later years (suspected that people
were trying to poison him; stopped eating and starved to death in 1978).
Before the paranoia, he did the two most important results in 20th-century logic.

### The Contribution: Completeness and Incompleteness

**Completeness Theorem (1930) — Good News**

```
GÖDEL'S COMPLETENESS THEOREM
==============================

Setting: First-order logic (predicate logic, the kind Frege invented).

Theorem: If a statement φ is true in every model of a set of axioms Γ
  (i.e., Γ ⊨ φ), then φ is provable from Γ (Γ ⊢ φ).

In other words: semantic truth (true in all models) = syntactic provability.
  Truth and proof COINCIDE in first-order logic.

Corollary: If Γ has no finite contradictions, it has a model.
  (Compactness theorem — foundational for model theory)

Corollary: The valid sentences of first-order logic are recursively enumerable
  — there is a mechanical procedure to enumerate all provable sentences.

This is GOOD news: first-order logic is powerful enough to capture proof,
  and proof captures truth.
```

**First Incompleteness Theorem (1931) — Shocking News**

```
GÖDEL'S FIRST INCOMPLETENESS THEOREM
======================================

Statement: Any consistent formal system F that:
  (a) contains a sufficient fragment of arithmetic
  (b) is recursively enumerable (the axioms can be listed by a program)
  ...must contain a statement G_F that is:
  - TRUE (in the standard model)
  - UNPROVABLE in F

The CONSTRUCTION:
  Step 1: Gödel numbering
    Assign every symbol, formula, and proof a natural number code.
    This encodes "statements about proofs" as arithmetic statements.

  Step 2: Self-reference
    Construct G_F: "This statement is not provable in F."
    More precisely: a statement whose Gödel number codes
    a sentence asserting its own unprovability.

  Step 3: Diagonalize
    If G_F is provable → G_F is false → F proves falsehoods → F is inconsistent.
    If G_F is not provable → G_F is true → F cannot prove all truths.
    Either F is inconsistent, or there are true unprovable statements.

  SAME STRUCTURE AS:
    - Cantor's diagonal argument (File 04)
    - Russell's paradox
    - Turing's halting problem

  All four are diagonal arguments.
```

**Second Incompleteness Theorem (1931)**

```
GÖDEL'S SECOND INCOMPLETENESS THEOREM
======================================

Statement: No consistent formal system F (satisfying the conditions above)
  can prove its own consistency.

Formally: If F ⊢ Con(F) (F proves "I am consistent"),
  then F is inconsistent.

DESTROYS HILBERT'S PROGRAM:
  Hilbert wanted to prove arithmetic is consistent using only arithmetic.
  Gödel proved that this is impossible.
  You can only prove F consistent using a STRONGER system F'.
  But then you'd need to prove F' consistent using F''... and so on.

What remains:
  - Mathematics is still reliable — we just can't have a finite proof
    that it's ALL reliable
  - For any specific statement, we can usually prove or disprove it
  - The incompleteness theorems are about the limits of formal systems,
    not about whether mathematics "works" in practice
```

**Gödel and the Halting Problem**

Gödel's Incompleteness Theorem and Turing's Halting Problem (1936) are the same
result in different clothing:

```
GÖDEL ↔ TURING CORRESPONDENCE
================================

Gödel (1931):                    Turing (1936):
  System: formal proof theory      System: Turing machines
  Self-reference: Gödel numbering  Self-reference: Universal TM
  Statement: "I am unprovable"     Input: program on its own code
  Result: true but unprovable      Result: halting undecidable
  Mechanism: diagonal argument     Mechanism: diagonal argument

The undecidability of the halting problem is the computability
version of Gödel's incompleteness.

Both use: self-referential construction + contradiction.
Both produce: limits on what formal systems / programs can determine.
```

---

## Alonzo Church (1903–1995)

### Who He Was

American logician, Princeton professor. Supervised Turing's PhD.
Created lambda calculus (1932–1941) as a formal theory of computation.
Independently proved the undecidability of the Entscheidungsproblem
(simultaneously with Turing, 1936).

### The Contribution: Lambda Calculus and Computability

**Lambda Calculus**

```
LAMBDA CALCULUS — THE CORE LANGUAGE
=====================================

Everything in lambda calculus is a function.

Syntax: three forms
  Variables:     x, y, z, ...
  Abstraction:   λx. M   (function with parameter x and body M)
  Application:   M N      (apply function M to argument N)

Reduction:
  β-reduction (application): (λx. M) N → M[N/x]
    (substitute N for x in M)

  α-renaming: λx. M ↔ λy. M[y/x] (renaming bound variables)

Everything is built from functions:
  True  := λt. λf. t   (take two args, return first)
  False := λt. λf. f   (take two args, return second)
  Not   := λb. b False True
  And   := λp. λq. p q False
  If    := λb. λt. λf. b t f

Natural numbers (Church encoding):
  0 := λf. λx. x         (apply f zero times to x)
  1 := λf. λx. f x        (apply f once)
  2 := λf. λx. f (f x)    (apply f twice)
  n := λf. λx. fⁿ x

This is purely abstract — no numbers, no booleans, no "types."
Just functions. Yet it can compute anything computable.
```

**Church's Undecidability of the Entscheidungsproblem (1936)**

Hilbert's Entscheidungsproblem: Is there an algorithm that takes a
first-order logic statement and decides whether it is provable?

Church proved: No. The halting problem for lambda calculus is undecidable,
and from this, the validity of first-order logic is undecidable.

Church did this independently and simultaneously with Turing. Turing's
formulation (with Turing machines) was more intuitive and became standard.
Church's lambda calculus was more mathematical and became the foundation
of functional programming.

**Church-Turing Thesis**

```
CHURCH-TURING THESIS
=====================

Church's lambda calculus and Turing's machines are computationally equivalent:
  - Any function computable by a Turing machine can be computed in LC
  - Any function computable in LC can be computed by a Turing machine

More generally: All "reasonable" models of computation are equivalent.
  Also equivalent: μ-recursive functions (Gödel/Kleene), random access machines,
  cellular automata (Conway's Game of Life is Turing complete),
  the C programming language, Python, Haskell, ...

The THESIS (not provable, but a claim about physical reality):
  Every effectively computable function is computable by a Turing machine.

  "Effectively computable" means: can be computed by a human following
  a finite set of rules mechanically, without insight.

This thesis is the definition of "algorithm." It cannot be proved (since
"effectively computable" is not formally defined). It can only be supported
by evidence — every proposed computation model has turned out equivalent.

Quantum computers: They compute the SAME functions as Turing machines
  (same class of decidable problems). They may be FASTER for some problems
  (BQP ⊆ PSPACE, and BQP may not equal P), but they can't compute
  functions that are Turing-undecidable.
```

**Lambda Calculus and Modern Programming**

```
LAMBDA CALCULUS IN MODERN LANGUAGES
=====================================

Church's lambda calculus is the theoretical foundation of:

Functional programming:
  Haskell: Pure lambda calculus with types (System F + type classes)
  ML/OCaml: Lambda calculus + let-polymorphism (Hindley-Milner)
  Clojure, Erlang, F#: Lambda calculus + side effects in controlled ways

Type theory:
  Simply typed lambda calculus (STLC): add types to Church's calculus
  System F: polymorphic (∀ types) — Hindley-Milner is a subset
  Dependent types (Coq, Lean, Agda): types depend on values
  Linear types (Rust's ownership): affine/linear type theory

The Curry-Howard correspondence:
  Types          ↔  Propositions
  Programs       ↔  Proofs
  λx: A. M       ↔  "Given a proof of A, here is a proof of B"
  Function type  ↔  Implication
  Product type   ↔  Conjunction
  Sum type       ↔  Disjunction
  Dependent type ↔  Universal quantifier

This is the Curry-Howard isomorphism: writing a program IS writing a proof.
Proof assistants (Coq, Lean, Isabelle) use this directly.
TypeScript's type system, Rust's type system, Haskell's type system —
all are fragments of typed lambda calculi.
```

---

## Comparison Table

| Figure | Dates | Core Contribution | What It Broke | What It Built |
|--------|-------|-------------------|--------------|---------------|
| **Frege** | 1848–1925 | Predicate logic, logicism | Aristotelian syllogisms | All of modern logic, type theory |
| **Russell** | 1872–1970 | Russell's paradox, type theory, PM | Frege's Basic Law V | Type theory → PLs, proof assistants |
| **Hilbert** | 1862–1943 | Formalism, Hilbert program, Hilbert spaces | Naive foundationalism | Proof theory, functional analysis, QM |
| **Gödel** | 1906–1978 | Completeness, incompleteness theorems | Hilbert's program | Computability theory, proof theory |
| **Church** | 1903–1995 | Lambda calculus, Entscheidungsproblem | Hilbert's program | Functional programming, type theory, PL semantics |

---

## Who to Cite for What

| Concept | Cite | Notes |
|---------|------|-------|
| Predicate logic (∀, ∃) | Frege | *Begriffsschrift* 1879 |
| Logicism (mathematics from logic) | Frege, Russell | Both tried; both failed |
| Russell's paradox | Russell | 1902 letter to Frege |
| Type theory (original) | Russell | *Principia Mathematica* |
| Curry-Howard correspondence | Church + Curry + Howard | Church: lambda calculus; Howard: types-as-propositions |
| Formalism / axiomatic method | Hilbert | Hilbert program |
| Hilbert space | Hilbert | Functional analysis |
| Gödel completeness theorem | Gödel | First-order logic is complete (1930) |
| Gödel incompleteness theorem | Gödel | No consistent system proves all truths (1931) |
| Lambda calculus | Church | 1932–1941 |
| Church-Turing thesis | Church + Turing | All reasonable computation models equivalent |
| Entscheidungsproblem undecidability | Church + Turing | Independent simultaneous 1936 |

---

## Common Confusion Points

**"Gödel proved mathematics is inconsistent"** — He proved that any consistent
system strong enough to express arithmetic is INCOMPLETE (contains unprovable truths).
Inconsistency is the opposite: an inconsistent system proves everything, including
contradictions. The incompleteness theorems assume consistency and conclude incompleteness.

**"The Halting Problem and Gödel's theorem are different results"** — They are the
same result in two different languages. The diagonal argument is the core of both.
Understanding one fully means understanding the other.

**"Lambda calculus is obscure theory"** — Every time you write `x => x + 1` in
JavaScript, `\x -> x + 1` in Haskell, or `lambda x: x + 1` in Python, you are
writing lambda calculus. The "lambda" in lambda expressions is literally Church's
lambda, λ. Modern PLs are implemented lambda calculi with syntactic sugar.

**"Hilbert's program completely failed"** — It failed at its maximal goal. But
Gödel's completeness theorem (for first-order logic) was a success of the program.
Hilbert spaces are a success. Proof theory, model theory, and computational complexity
theory — all emerged from attempts to understand the limits of Hilbert's program.
The failure was productive.

**"Church and Turing proved the same thing"** — They proved the same result
(undecidability) but developed different computational models. Church's lambda
calculus became the foundation of functional programming and type theory.
Turing's machines became the standard model for complexity theory (P vs NP,
NP-hardness) and for the theory of formal languages. The two traditions meet
in PL theory: operational semantics (Turing-like) and denotational semantics
(Church-like) are dual perspectives on the same programs.
