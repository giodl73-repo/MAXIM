# Language and Computing: Formal Semantics to Type Theory

## The Deep Connection

Philosophy of language and computer science share a common conceptual infrastructure: formal languages, type theory, lambda calculus, model theory, compositionality. This is not coincidence — the two fields developed in the same intellectual tradition (Frege → Russell → Church → Curry → Scott/Strachey/Montague). Understanding the lineage shows why concepts like "type," "meaning," "reference," and "context" appear in both.

```
+-----------------------------------------------------------------------+
|                    PHIL OF LANGUAGE ↔ COMPUTING                       |
|                                                                       |
|  PHILOSOPHY                          COMPUTING                        |
|  -----------                         --------                         |
|                                                                       |
|  Frege's sense/reference  ─────────→ Lambda calculus (Church 1936)    |
|  Function/argument form               Types (Church's STT 1940)       |
|                                                                       |
|  Compositionality ─────────────────→ Denotational semantics           |
|  (meaning from parts)                (Scott/Strachey 1970s)           |
|                                                                       |
|  Montague grammar ─────────────────→ Semantic parsing / NLU           |
|  (NL as formal language)             Type-theoretic semantics         |
|                                                                       |
|  Truth conditions ─────────────────→ Formal verification, Hoare logic |
|  (what makes statements true)        (pre/post conditions)            |
|                                                                       |
|  Possible worlds semantics ────────→ Modal logics in CS:              |
|  (necessity, possibility)             temporal logic, dynamic logic   |
|                                       epistemic logic for knowledge   |
|                                       representation                  |
|                                                                       |
|  Speech acts / pragmatics ─────────→ API design, protocol specs,      |
|  (what utterances DO)                 command languages               |
|                                                                       |
|  Private language argument ────────→ Public interfaces, type systems, |
|  (meaning requires public criteria)   contracts, specifications       |
+-----------------------------------------------------------------------+
```

---

## The Lambda Calculus Connection

Church's λ-calculus (1936) is the foundation of functional programming, type theory, and Montague's semantic metalanguage. All three use the same underlying formalism.

### The Curry-Howard Correspondence

```
  PROPOSITIONS AS TYPES / PROOFS AS PROGRAMS:

  LOGIC                         TYPE THEORY / PROGRAMMING
  -----                         -------------------------
  Proposition A                 Type A
  Proof of A                    Term of type A (a program)
  A → B (implication)           A → B (function type)
  A ∧ B (conjunction)           A × B (product type / tuple)
  A ∨ B (disjunction)           A + B (sum type / Either)
  ⊥ (false)                     Void (empty type / never)
  ¬A (negation A → ⊥)           A → Void
  ∀x:A.B(x) (universal)         Π-type / dependent function type
  ∃x:A.B(x) (existential)        Σ-type / dependent pair type

  LOGICAL OPERATIONS:
  Modus ponens (A, A→B ⊢ B)    Function application (f a : B)
  Proof combination             Tuple construction
  Curry-Howard:  proving a proposition = writing a program of that type
  A proof that doesn't terminate corresponds to a diverging proof.
  Proof normalization = program evaluation (β-reduction).

  LANGUAGES EXPLOITING THIS:
  Coq, Agda, Lean: dependent type theory as proof assistant.
  Idris, F*: dependently typed programming with proofs.
  Haskell: Hindley-Milner type system (intuitionistic logic fragment).
  Rust: linear types (intuitionistic linear logic fragment).
```

---

## Denotational Semantics: Montague for Programs

Dana Scott and Christopher Strachey developed denotational semantics (1970s) to give programs mathematical meanings. The architecture is exactly Montague grammar applied to programming languages.

```
  MONTAGUE GRAMMAR:                DENOTATIONAL SEMANTICS:
  -----------------                ----------------------
  Syntactic rules                  Syntactic rules (grammar)
  + semantic rules                 + semantic rules (denotation)

  [[ NP VP ]] = [[NP]]([[VP]])     [[E1 E2]] = [[E1]]([[E2]])

  Types for NL categories:         Types for PL constructs:
  e, t, e→t, (e→t)→t              Integer, Bool, State→Val, etc.

  Compositional interpretation     Compositional interpretation
  of natural language sentences    of program expressions

  Example:                         Example:
  [["walks"]] = λx.walk(x)         [[x+y]] = λσ.σ(x) + σ(y)
  [["John walks"]]                 [[x:=e]] = λσ.σ[x:=[[e]]σ]
  = [[walks]]([[John]])            [[S1;S2]] = [[S2]] ∘ [[S1]]

  SCOTT DOMAINS:
  For recursion and partiality, simple sets are not enough.
  Scott invented domain theory: complete partial orders with
  directed joins, used as the semantic domains for programs.
  This handles non-termination: the "bottom" element ⊥ represents
  undefined/diverging computation.
  Montague semantics is classical (total); PL semantics needs ⊥.
```

---

## Types and Meaning

Type systems in programming languages are a form of formal semantics.

### Types as Meanings

```
  IN MONTAGUE GRAMMAR:
  "walks" has type e → t
  This tells us: "walks" MEANS a function from individuals to truth values.
  The TYPE encodes the meaning's SHAPE.

  IN PROGRAMMING LANGUAGES:
  f : Int → Int → Bool
  This tells us: f takes two integers and returns a boolean.
  The TYPE encodes the computation's SHAPE.

  HOWARD'S OBSERVATION:
  Types ARE propositions.
  A function of type A → B is a proof that A implies B.
  Writing a program of type A is constructing evidence of A.

  DEPENDENT TYPES EXTEND THIS:
  Π (x : Nat). Vec Nat x   → "for all n, a vector of length n"
  Σ (x : Nat). Vec Nat x   → "some n and a vector of length n"
  = types that DEPEND on values
  = propositions with quantifiers over values
  = the full predicate calculus encoded in types

  ML's POLYMORPHISM (∀ a. a → a):
  The type ∀a.a→a (the identity function's type).
  This is a second-order formula: for all types a, a function a→a.
  Girard/Reynolds parametricity: the ONLY inhabitant is the identity.
  Types are propositions; polymorphic types are second-order propositions.
```

---

## Reference, Scope, and Binding

The philosophy of reference maps directly to variable scoping in programming languages.

```
  NAMES IN PHILOSOPHY:           IDENTIFIERS IN PLs:
  --------------------           -------------------
  Rigid designator                 Free variable (refers to something)
  (Kripke: name → object)          x in "x + 1" refers to x's binding

  Definite description             Expression with implicit existential:
  (Russell: the F)                 "array[i]" = "the element at index i"
                                   — implicitly requires i to be valid

  Sense (Frege)                    Name in an expression: has type
  = mode of presentation           (how the compiler "sees" it)
  (how the object is accessed)

  Reference                        The value bound to the identifier
  = the actual object              at runtime

  Non-referring names              Null/undefined/void
  ("the present king of            = the failure of a name to bind
  France has no reference")        to a valid value

  SCOPE AND BINDING:
  "∀x.P(x)" — x is BOUND inside P(x).
  "λx. body" — x is bound in body. β-reduction substitutes.
  A free variable in a term = an unresolved reference.
  A closed term = no free variables = self-contained meaning.
  A well-typed closed term = a complete, meaningful program.

  SHADOWING: inner x shadows outer x = same surface syntax,
  different binding context. Exactly the referent/sense split:
  same "name," different reference contexts.
```

---

## Modal Logic in Computer Science

Kripke semantics for modal logic is not just philosophical — it is the foundation of formal verification and knowledge representation.

```
  TEMPORAL LOGIC:
  Worlds = program states (or time points).
  Accessibility = "next state" / "reachable state" relation.

  LTL (Linear Temporal Logic):
  □P   = P holds now and in all future states
  ◇P   = P holds now or at some future state
  Xp   = P holds at the NEXT state
  P U Q = P holds until Q holds

  CTL (Computation Tree Logic):
  AG P  = Along All paths, Globally P (for all futures)
  EF P  = there Exists a path where eventually P
  AF P  = Along all paths, eventually P (liveness)
  EG P  = there Exists a path where Globally P

  MODEL CHECKING (Clarke, Emerson, Sifakis — Turing Award 2007):
  Given: a Kripke model M and a temporal formula φ.
  Check: M ⊨ φ  (does the model satisfy the formula?)
  Used in: hardware verification, protocol verification,
  operating system correctness proofs.
  Azure Service Fabric: uses model checking for protocol validation.

  DYNAMIC LOGIC:
  [α]P = "after program α, P holds" (all executions)
  ⟨α⟩P = "after program α, P holds" (some execution)
  Hoare triple: {P} α {Q} = [α under P → Q]
  = Pre/post condition reasoning for programs.
  This is Hoare logic expressed as dynamic modal logic.

  EPISTEMIC LOGIC:
  Worlds = possible situations an agent considers possible.
  KiP = "agent i knows P"
  = P is true in all worlds agent i cannot distinguish from actual.
  Used in: multi-agent systems, cryptographic protocol verification,
  game theory, distributed systems consensus reasoning.
```

---

## Pragmatics and API Design

Speech act theory and Gricean pragmatics apply to the design of programming interfaces.

```
  SPEECH ACTS → API SEMANTICS:

  Austin's felicity conditions:
  For a speech act to succeed: right person, right context,
  right procedure, complete execution.

  API PRECONDITIONS (same structure):
  List.RemoveAt(i):
  - Object must be initialized (right context)
  - i must be in bounds (precondition / felicity condition)
  - Caller must have appropriate access (right person)
  = Violation → exception (like a misfire)

  PERFORMATIVE DECLARATIONS → SIDE-EFFECTING OPERATIONS:
  "I hereby fire you" = declarative that changes institutional state.
  db.SaveChanges() = declarative that changes database state.
  Thread.Start() = performative that creates a new thread.

  LOCUTIONARY / ILLOCUTIONARY / PERLOCUTIONARY:
  Method call (locutionary) → its intended effect (illocutionary) →
  actual side effects on the system (perlocutionary).

  GRICE'S MAXIMS → GOOD API DESIGN:
  Quantity: provide necessary information, not more
  = minimal API surface; no spurious parameters
  Quality: say what is true
  = accurate documentation; no misleading method names
  Relation: be relevant
  = methods grouped by concern; no leaky abstractions
  Manner: be clear and orderly
  = consistent naming conventions; no surprise behaviors

  "API DESIGN IS COMMUNICATION DESIGN."
  An API is a language with a syntax (signatures), a semantics
  (what calls do), and pragmatics (how they are used in context).
```

---

## Wittgenstein's Private Language Argument and Public Interfaces

```
  THE ARGUMENT: A purely private language is impossible.
  Without public criteria for correct application,
  there is no distinction between correct use and merely
  seeming correct.

  CS ANALOG:
  A "private type" that only the implementer can check for
  validity is useless. What makes a type system useful is
  its PUBLIC, MECHANICALLY CHECKABLE criteria.
  The type checker = the external criterion for correct application.

  INTERFACES:
  An interface specification IS public criteria for correctness.
  Without a spec (Liskov Substitution, contracts, tests),
  there is no stable notion of "correct implementation."
  A "private" understanding of what the interface means
  is exactly the private language situation.

  DUCK TYPING vs STRONG TYPES:
  Duck typing: if it walks like a duck, call it a duck.
  = Implicit, practice-based criteria (like Wittgenstein's use-theory).
  Works when usage conventions are stable and shared.
  Fails when the community of practice is too small or implicit.

  STRONG STATIC TYPES:
  Public criteria encoded mechanically.
  The type system is the shared language-game rule-book.
  Violations are "grammatically incorrect" — refused by the compiler.
```

---

## Frege's Sense/Reference in Type Systems

```
  FREGE:
  "Hesperus" (sense) → Venus (reference)
  "Phosphorus" (sense) → Venus (same reference, different sense)

  PROGRAMMING:
  List<int> (type = sense) → the runtime list object (reference)
  object (base type sense) → same runtime object (same reference)

  TYPE COVARIANCE:
  "Hesperus = Phosphorus" is informative (different senses, same ref).
  string = IEnumerable<char> is informative
  (different types, but one is the other's implementation).

  NOMINAL vs STRUCTURAL TYPING:
  Nominal (Java/C#): types are identified by NAME (= Fregean sense).
  Two classes with identical structure but different names = different types.
  Structural (Go interfaces, TypeScript): types are identified by STRUCTURE.
  Two types with the same structure are interchangeable.
  = Closer to reference than to sense.

  NEWTYPE / OPAQUE TYPES:
  newtype Email = Email String  -- Haskell
  record Email(string Value); // C# record struct
  Same underlying representation (sense = same structure)
  But DIFFERENT types in the type system.
  = Frege's insight: same reference (string) but different senses (Email, Name).
  The purpose of newtype/opaque types IS Frege's distinction,
  applied to the domain of values and types.
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is Curry-Howard? | Propositions = types; proofs = programs; proof normalization = evaluation |
| What is denotational semantics? | Compositional assignment of mathematical meanings to program constructs — Montague for PLs |
| What does Kripke semantics formalize in CS? | Modal logic (temporal, epistemic, dynamic) — model checking, formal verification |
| What is Hoare logic in this framework? | Pre/post conditions = modal logic with [program]P notation (dynamic logic) |
| What does Frege's sense/reference map to? | Type vs value (sense = type; reference = runtime value); nominal vs structural typing |
| What is the private language argument's relevance to CS? | Public type specifications and interfaces are the external criteria that make private computation shareable |
| How does Grice apply to APIs? | Maxims of Quantity (minimal surface), Quality (accurate docs), Relation (cohesion), Manner (clarity) |

---

## Common Confusion Points

**Curry-Howard is not just an analogy**: The correspondence is structural — the proofs of a logic ARE the programs of the corresponding type system. In dependent type theory, this identification is complete: every proposition is a type; every proof is a program. This is implemented in Coq, Agda, and Lean.

**Denotational semantics ≠ operational semantics**: Denotational: what does the program mean (as a mathematical function)? Operational: how does the program compute (step by step)? Both are valid approaches; they should agree on the final result. Denotational is more abstract and compositional; operational is closer to implementation.

**Types are not just documentation**: In a sound type system, a well-typed program cannot go wrong in type-specific ways. The type system enforces constraints mechanically. This is the difference between types and comments — types are checked, comments are not. The Wittgenstein point: types provide public criteria for correctness.

**Temporal logic LTL vs CTL**: LTL evaluates formulas over paths (sequences of states). CTL evaluates over computation trees (branching futures). They have incomparable expressive power. Model checkers like SPIN use LTL; NuSMV/UPPAAL support CTL. The choice matters for what properties you can express.

**"Meaning is use" in PLs**: Wittgenstein's slogan applies to programming too — the meaning of a programming construct is how it is used by the community of programmers. Language design communities evolve shared uses that become normative. This is why "best practices" are semiotic facts, not logical necessities.
