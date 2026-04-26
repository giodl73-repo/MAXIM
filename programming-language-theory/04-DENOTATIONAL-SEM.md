# Denotational Semantics: Scott Domains, Continuity, Full Abstraction

## The Big Picture

Denotational semantics assigns mathematical objects to programs — independently of how they compute. The meaning of a program is a function, and the theory is built to handle recursion (which requires fixed points) and higher-order functions (which require function spaces that are themselves domains).

```
+--------------------------------------------------------------------------+
|                    DENOTATIONAL SEMANTICS LANDSCAPE                      |
+--------------------------------------------------------------------------+
|                                                                          |
|  GOAL: ⟦t⟧ ∈ D — assign mathematical object from domain D to term t    |
|                                                                          |
|  THE PROBLEM WITH NAIVE SEMANTICS:                                       |
|  Recursive function f x = if x=0 then 1 else x * (f (x-1))             |
|  What mathematical object is f?                                          |
|  f : Int → Int, but f is defined in terms of itself                     |
|  → Need a domain with a notion of approximation                         |
|                                                                          |
|  SCOTT'S SOLUTION (1969–70):                                            |
|  Domains = partial orders with certain completeness properties           |
|  Meaning of recursion = LEAST FIXED POINT                               |
|  ⟦fix f⟧ = ⊔{fⁿ(⊥) | n ≥ 0}  (least upper bound of approximations)   |
|                                                                          |
|  ADEQUACY THEOREM:                                                       |
|  ⟦t⟧ = ⟦v⟧ iff t →* v   (denotational agrees with operational)        |
|                                                                          |
|  FULL ABSTRACTION (FAILURE):                                            |
|  ⟦t₁⟧ = ⟦t₂⟧ iff t₁ ≈ t₂ (contextual equivalence)?                   |
|  For PCF (Milner's problem 1977): NO — fails without parallel or       |
|  SOLVED by: game semantics (Abramsky et al. 1990s)                     |
+--------------------------------------------------------------------------+
```

---

## 1. Scott Domains

Dana Scott (1969–70) — invented to give semantics to λ-calculus (which can apply functions to themselves, requiring D ≅ D → D).

**Partial order with bottom**:
```
A DOMAIN D = (D, ⊑, ⊥) is a poset with:
  ⊑ (approximation order): d₁ ⊑ d₂ means "d₁ is less defined than d₂"
  ⊥ (bottom): the least element (totally undefined)

  Flat domain for Int:
    D = {⊥, 0, 1, 2, 3, ...}  (⊥ ⊑ n for all n; n, m incomparable for n≠m)

  ⊥ means "hasn't computed yet / diverges"
  n means "the computation terminated with value n"

LIFTING: if D is a set {d₁, d₂, ...}, then D⊥ = D ∪ {⊥}
  with d₁ ⊑ d₂ iff d₁ = ⊥ or d₁ = d₂
  → Flat domain: only comparison is ⊥ ≤ everything
```

**Directed-complete partial orders (dcpo)**:
```
DIRECTED SET: S ⊆ D is directed if:
  1. S is nonempty
  2. For any d₁, d₂ ∈ S, there exists d₃ ∈ S with d₁ ⊑ d₃ and d₂ ⊑ d₃
  (S is "consistently upperly bounded")

DCPO (directed-complete partial order):
  Every directed set S has a least upper bound: ⊔S ∈ D

INTUITION:
  Directed sets are approximation chains (each element is more defined than previous)
  f : D → D is computable only if it preserves these approximation chains
  → Scott continuity
```

**Scott continuity**:
```
SCOTT CONTINUOUS FUNCTION:
  f : D → E is Scott continuous if:
  1. f is monotone: d₁ ⊑ d₂ → f(d₁) ⊑ f(d₂)
  2. f preserves directed lubs: f(⊔S) = ⊔{f(d) | d ∈ S}

  INTUITION: if you give f better and better approximations of its input,
             you get better and better approximations of its output.
             No "sudden jumps" — computable functions are continuous.

THEOREM (Scott): Every computable function is Scott continuous.
  (Converse fails: there are continuous functions that aren't computable,
   but all computable ones are continuous.)

THIS IS THE TYPE OF "FUNCTION WE CAN COMPUTE":
  [D → E] (continuous functions from D to E) is itself a domain
  → Higher-order functions have domains
  → We can give denotational semantics to higher-order languages
```

---

## 2. Fixed Points and the Meaning of Recursion

**Kleene fixed-point theorem** (for dcpos):
```
KLEENE FIXED-POINT THEOREM:
  Let D be a dcpo with bottom ⊥.
  Let f : D → D be Scott continuous.
  Then f has a least fixed point:

    fix(f) = ⊔{fⁿ(⊥) | n ≥ 0}
           = ⊔{⊥, f(⊥), f(f(⊥)), f(f(f(⊥))), ...}

  And fix(f) = f(fix(f)).

PROOF SKETCH:
  The chain ⊥ ⊑ f(⊥) ⊑ f²(⊥) ⊑ ... is directed (monotone f)
  → It has a lub ⊔ = fix(f) (by dcpo completeness)
  → f(⊔) = ⊔{f(fⁿ(⊥))} = ⊔{f^(n+1)(⊥)} = ⊔ (by continuity + reindexing)
  → fix(f) is a fixed point
  → Minimality: any other fixed point d satisfies ⊥ ⊑ d → f(⊥) ⊑ f(d) = d → ... → fix(f) ⊑ d
```

**Semantics of recursion**:
```
RECURSIVE FUNCTION:  fact = λn. if n=0 then 1 else n * (fact (n-1))

DENOTATIONAL MEANING:
  ⟦fact⟧ = fix(F)  where  F = λf. λn. if n=0 then 1 else n * (f (n-1))

  F : (Int⊥ → Int⊥) → (Int⊥ → Int⊥)   (a continuous functional)
  fix(F) : Int⊥ → Int⊥

  APPROXIMATION SEQUENCE:
  F⁰(⊥) = ⊥                    (totally undefined)
  F¹(⊥) = λn. if n=0 then 1 else n * ⊥(n-1) = {0→1, else→⊥}
  F²(⊥) = {0→1, 1→1, else→⊥}
  F³(⊥) = {0→1, 1→1, 2→2, else→⊥}
  ...
  fix(F) = {n → n! for all n ≥ 0}   (full factorial function)
```

---

## 3. Adequacy

The adequacy theorem links denotational to operational semantics:

```
ADEQUACY THEOREM (for a language like PCF):

  ⊢ e : τ and ⟦e⟧ ≠ ⊥  iff  e →* v   (for some closed value v)
  AND when they agree: ⟦e⟧ = ⟦v⟧

READING:
  "e terminates" (operationally: reduces to a value) iff
  its denotation is not ⊥ (the undefined element)

PROOF DIRECTION 1 (soundness): e →* v → ⟦e⟧ = ⟦v⟧
  By induction on the reduction sequence.
  Each step preserves denotational value (Preservation theorem analogue).

PROOF DIRECTION 2 (completeness): ⟦e⟧ ≠ ⊥ → e →* v
  Harder: requires "computability" (realizability) argument.
  Every non-⊥ denotation corresponds to a terminating computation.

SIGNIFICANCE:
  Adequacy says denotational and operational semantics agree on termination.
  You can reason about programs in the domain (mathematics) and
  trust that operational behavior corresponds.
  Compilers preserve denotations (when they're verified like CompCert).
```

---

## 4. The Full Abstraction Problem

Robin Milner (1977) posed the full abstraction problem for PCF (a simple functional language):

```
CONTEXTUAL EQUIVALENCE:
  e₁ ≈_ctx e₂  iff  for all contexts C[−]:
    C[e₁] terminates iff C[e₂] terminates

  "Operationally equivalent" — no context can tell them apart.

FULL ABSTRACTION:
  A denotational semantics ⟦−⟧ is fully abstract if:
    ⟦e₁⟧ = ⟦e₂⟧  iff  e₁ ≈_ctx e₂

  Denotational equality ↔ operational equivalence.
  The semantics is "tight" — it identifies exactly what programs
  can't be distinguished by any context.

MILNER'S PROBLEM:
  The standard Scott domain semantics of PCF is NOT fully abstract.

  Two PCF terms that are OPERATIONALLY DISTINCT but DENOTATIONALLY EQUAL:
  por (parallel or): por e₁ e₂ = true if either e₁ = true or e₂ = true
                                 (may return true even if one argument diverges)

  In PCF without parallel or: you cannot write por.
  But in Scott domain semantics: ⟦e₁⟧ = ⟦e₂⟧ for two PCF terms
  that would be distinguished if parallel or were added.

  → Denotational semantics over-identifies programs — identifies more
    programs as equal than operational semantics does.

  SOLUTION 1: Add parallel or to PCF (makes language fully abstract but impure)
  SOLUTION 2: Game semantics
```

**Game Semantics** (Abramsky, Jagadeesan; Hyland, Ong; 1990s):
```
GAME SEMANTICS IDEA:

  Programs = strategies in a game between:
    Opponent (O): environment, asks questions
    Proponent (P): program, gives answers

  For function A → B:
    O asks question in B (what output do you want to compute?)
    P asks counter-question in A (give me input)
    O answers in A
    P answers in B

  SEQUENCE OF MOVES: O asks → P answers → O asks → ...

  STRATEGY = deterministic function from opponent moves to proponent moves
           = a FUNCTION from interaction sequences to next P-move

FULL ABSTRACTION RESULT:
  ⟦e₁⟧_game = ⟦e₂⟧_game  iff  e₁ ≈_ctx e₂

  Game semantics is fully abstract for PCF!
  (Abramsky-Jagadeesan 1994, Hyland-Ong 1999)

WHY IT WORKS:
  Games model the interaction structure of computation precisely
  The "opponent" captures all possible contexts
  Sequential strategies = PCF-definable functions
  (Adding concurrency: innocent strategies no longer enough)
```

---

## 5. Category Theory Connection

The connection between typed lambda calculus and category theory (Lambek, Scott 1980s):

```
LAMBEK-SCOTT CORRESPONDENCE:

  TYPED LAMBDA CALCULUS          CARTESIAN CLOSED CATEGORY (CCC)
  ─────────────────────          ─────────────────────────────────
  Types                    ↔     Objects
  Terms (programs)         ↔     Morphisms (arrows)
  Function type A → B      ↔     Exponential object Bᴬ
  Product type A × B       ↔     Categorical product A × B
  Unit type 1              ↔     Terminal object 1
  Type substitution        ↔     Composition
  β-reduction              ↔     Unique morphism through exponential
  η-expansion              ↔     Extensionality of morphisms

  EVERY CCC GIVES A MODEL OF STLC.
  EVERY STLC THEORY GIVES A CCC.
  → Categorical semantics = algebraic structure that abstracts over models

DOMAIN THEORY AS CATEGORY:
  Objects: Scott domains (dcpos)
  Morphisms: Scott continuous functions
  → This is a CCC (with appropriate constructions)
  → Gives denotational semantics for STLC

  Function space D → E is a domain:
  F ⊑ G iff ∀d ∈ D: F(d) ⊑ G(d)   (pointwise order)
  This is needed for the exponential object.

SIGNIFICANCE:
  Categorical semantics is compositional: meaning of compound term
  = composition of meanings of parts
  Sound design principle for language features: define categorical structure,
  get semantics for free
  → Monads as monoids in the category of endofunctors
    (the formal basis of Moggi's monadic semantics)
```

---

## 6. Connection to Modern Languages

```
DENOTATIONAL SEMANTICS IN PRODUCTION:

HASKELL:
  Types are types in a CCC (with lazy semantics)
  ⊥ is the bottom element of every flat domain
  Haskell values include ⊥: undefined :: a
  seq forces to WHNF ≠ forcing to NF (domain theory explains this)
  The semantics of Haskell is "continuous" — lazy thunks are domain elements

RUST:
  Rust's operational semantics formalized as "Stacked Borrows" model
  (Ralf Jung et al.) — small-step style
  Not domain-based; instead: memory model with validity invariants

COERCIONS IN GHC CORE (System Fc):
  GHC's Core language has explicit coercions (type equality witnesses)
  Denotational: coercions denote identity functions (no runtime cost)
  → "Newtype coercion" and "type family coercion" are denotationally trivial

VERIFIED COMPILERS (CompCert):
  CompCert proves: ⟦compile(p)⟧_machine = ⟦p⟧_source
  This is an adequacy + preservation theorem for a real compiler
  Uses Coq to mechanize the proof
  The semantics are both operational (concrete machine) and
  abstract (C source semantics)
```

---

## Decision Cheat Sheet

| Concept | What it gives you | Key theorem |
|---------|-------------------|-------------|
| Scott domain (dcpo + ⊥) | Meaning of partial/non-terminating computations | Kleene fixed point |
| Scott continuity | Types of computable functions | Every computable function is continuous |
| Fixed-point semantics | Meaning of recursion | fix(f) = ⊔{fⁿ(⊥)} |
| Adequacy theorem | Operational ↔ denotational agreement | ⟦e⟧ ≠ ⊥ iff e →* v |
| Full abstraction | Denotational identifies exactly what operational can't distinguish | Milner's PCF problem |
| Game semantics | Solves full abstraction for PCF | Abramsky-Hyland-Ong |
| CCC correspondence | Types = objects; terms = morphisms | Lambek-Scott |

---

## Common Confusion Points

**⊥ in domain theory ≠ ⊥ in Haskell exactly**: Domain-theoretic ⊥ is the least element representing non-termination. Haskell's `undefined :: a` and infinite loops are both ⊥. But Haskell's `undefined` also throws an exception when forced — exception semantics are not pure domain theory (they require effects). The domain semantics is the pure-computation fragment.

**Full abstraction is not just about observable termination**: Full abstraction requires that the denotational semantics distinguishes exactly the programs that contextual equivalence distinguishes — for ALL observations, not just termination. The failure in PCF is subtle: the Scott semantics equates programs that a parallel context could distinguish.

**Category theory is not required to use denotational semantics**: The CCC correspondence is theoretically beautiful but you don't need it to apply domain theory. The practical use is: (1) understand what ⊥ means; (2) understand fixed-point semantics of recursion; (3) reason about program equivalence via denotational equality rather than reduction sequences.

**Game semantics is not just for theoretical interest**: Game semantics has been applied to verify security protocols, to give semantics to object-oriented languages with aliasing, and to model-check concurrent programs. The "interaction sequence" model of programs is the basis of separation logic's framing (which Rust's borrow checker informally implements).
