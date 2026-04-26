# Formal Semantics: Montague Grammar

## The Project

Richard Montague (1930–1971) made a radical claim: natural language has the same logical status as formal languages, and can be given rigorous compositional semantics using the same tools used for logical calculi. His paper "The Proper Treatment of Quantification in Ordinary English" (1973, posthumous) is the founding document of formal semantics as a discipline.

For TCS background: Montague grammar IS typed lambda calculus applied to natural language. The semantic metalanguage is Church's simple type theory. Compositionality is the Frege principle formalized as a homomorphism. If you understand denotational semantics of programming languages, you understand the architecture of Montague semantics.

```
+-----------------------------------------------------------------------+
|                    FORMAL SEMANTICS LANDSCAPE                         |
|                                                                       |
|  MONTAGUE (1970s)              DAVIDSON (1967–1980s)                  |
|  Universal grammar             Truth-conditional semantics            |
|  Intensional logic + λ-calc    Event semantics                        |
|  PTQ — "English is a fragment  Action sentences analyzed via          |
|  of a formal language"         events as first-class entities         |
|  Denotational: phrases →       Davidson: T-sentences as the           |
|  mathematical objects          core of meaning theory                 |
|                                                                       |
|  CONTINUATIONS/TYPE-SHIFTING   DYNAMIC SEMANTICS (1990s)              |
|  Montague extended:            Discourse representation theory        |
|  flexible types, continuations Pronouns across sentences              |
|  in natural language semantics Dynamic predicate logic                |
+-----------------------------------------------------------------------+
```

---

## Compositionality

The foundational principle, going back to Frege.

```
  FREGE'S PRINCIPLE:
  The meaning of a complex expression is a FUNCTION of:
  (1) the meanings of its constituent parts
  (2) the syntactic rule combining them

  FORMALIZATION AS HOMOMORPHISM:
  Let [[ · ]] : Expressions → Meanings be the semantic function.

  Compositionality: if α is the result of combining A and B
  by syntactic rule r, then:
  [[α]] = Fr([[A]], [[B]])
  where Fr is the semantic operation corresponding to r.

  EXAMPLE:
  [[every man walks]]
  = [[walks]]([[every man]])  ← apply VP denotation to NP meaning
  = {w : w is a walking event} applied to the GQ "every man"
  = True iff every man is in the extension of "walks"

  WHAT THIS REQUIRES:
  Every syntactic category must have a corresponding semantic type.
  Every syntactic rule must have a corresponding semantic operation.
  Syntax and semantics must be in structural correspondence.
```

---

## Types in Montague Grammar

Montague used a typed intensional logic (based on Church's simple type theory). Types are the "interface" between syntax and semantics.

### Basic Types

```
  BASIC TYPES:
  e:  type of entities (individuals in the domain)
  t:  type of truth values {0, 1}
  s:  type of possible worlds (for intensionality)

  FUNCTION TYPES:
  If σ and τ are types, then (σ → τ) is the type of
  a function from σ to τ.

  (Usually written ⟨σ, τ⟩ in Montague tradition, or σ → τ in λ-calc)
```

### Types for English Categories

```
  SEMANTIC TYPE         ENGLISH CATEGORY        EXAMPLE

  e                     Individual term         John, the man
  t                     Proposition/sentence    "John walks"
  e → t                 Predicate (1-place)     "walks" = λx.walks(x)
  e → e → t             2-place relation        "loves" = λyλx.loves(x,y)
  (e → t) → t           Generalized Quantifier  "every man"
  ((e→t)→t)→ t          Sentence-level quantif. "most men walk"

  VERB PHRASE:
  "walks" : e → t
  [[walks]] = λx . walks(x)
  Applied to individual [[John]] = john:
  [[walks]](john) = walks(john) : t  ✓

  TRANSITIVE VERB:
  "loves" : e → e → t
  [[loves]] = λy λx . loves(x, y)
  [[loves]](mary)(john) = loves(john, mary)  ← "John loves Mary"
  (Note the order of abstraction: object first, then subject)
```

---

## Generalized Quantifiers

The key innovation: treating noun phrases as second-order entities.

```
  TRADITIONAL LOGIC (Frege/Russell):
  "Every man walks" =  ∀x(man(x) → walks(x))

  PROBLEM with compositionality:
  "John" and "every man" occupy the same syntactic position (NP).
  "John" denotes an INDIVIDUAL: type e.
  "every man" cannot denote an individual.
  They must have the same semantic type for compositionality to work.

  MONTAGUE'S SOLUTION: GENERALIZED QUANTIFIERS (GQ)
  Treat BOTH "John" and "every man" as type (e → t) → t
  = a function from sets to truth values
  = a SET OF SETS

  [[John]] = λP . P(john)
  "John" denotes the set of all properties John has.
  {"walks", "talks", "breathes", ...}
  Applied to a predicate P: is john in P?

  [[every man]] = λP . ∀x(man(x) → P(x))
  "Every man" denotes: {P : every man is P}
  Applied to "walks": ∀x(man(x) → walks(x))

  [[some man]] = λP . ∃x(man(x) ∧ P(x))
  [[no man]]   = λP . ¬∃x(man(x) ∧ P(x))
  [[most men]] = λP . |{x: man(x) ∧ P(x)}| > |{x: man(x) ∧ ¬P(x)}|

  UNIFORM TYPE:
  All noun phrases have type (e → t) → t.
  The VP has type e → t.
  Sentence = NP applied to VP:
  [[S]] = [[NP]]([[VP]])  ← compositionality!
```

---

## Intensions and Possible Worlds in Montague

Natural language is full of intensional contexts: "believes," "necessarily," "possibly," "seeks," etc. Montague handled these using possible worlds directly in the types.

```
  THE PROBLEM:
  "John seeks a unicorn" — but there are no unicorns!
  "Seeks" cannot take a unicorn as its direct object (no entity).
  "John seeks a president" — but "a president" doesn't pick out
  a specific individual.

  Montague added:
  s:  the type of possible worlds (indices)

  INTENSION of expression of type τ:
  A function from possible worlds (and times) to the extension.
  If α has type τ, then ⌃α (the intension of α) has type s → τ.

  [[unicorn]] at world w = the set of unicorns in w
  (may be empty in the actual world, non-empty in others)

  [[seeks]] : e → (s → e → t) → t
  "seeks" takes an entity (the seeker) and an INTENSION of an NP
  (a function from worlds to sets).
  "Seeks a unicorn" = seeks something that is a unicorn in some
  relevant worlds.

  THIS IS INTENSIONAL LOGIC:
  All expressions have both an extension (value at a world)
  and an intension (function from worlds to values).
  Frege's sense ≈ intension in Montague grammar.
  The type-theoretic formulation makes it precise and computable.
```

---

## Lambda Calculus as the Semantic Metalanguage

```
  Montague's semantic metalanguage IS typed lambda calculus.
  Denotations are built via λ-abstraction and application.

  LAMBDA ABSTRACTION:
  λx . body        "the function that takes x and returns body"

  LAMBDA APPLICATION:
  (λx . body)(arg) → body[x := arg]    (β-reduction)

  BUILDING UP MEANINGS COMPOSITIONALLY:

  [[walks]]  = λx . walk(x)
  [[John]]   = λP . P(j)
  [[John walks]] = [[John]]([[walks]])
                 = (λP . P(j))(λx . walk(x))
                 = (λx . walk(x))(j)     ← β-reduction
                 = walk(j)               ← β-reduction
                 ∈ {T, F}

  THE POINT: The SAME mechanical operation (β-reduction) handles all
  compositional combination. No special-case rules needed.
  Syntax provides structure; λ-abstraction provides the meaning.

  CS PARALLEL:
  Denotational semantics of programming languages
  uses EXACTLY this:
  [[E1 E2]] = [[E1]]([[E2]])   (application)
  [[λx.E]]  = λv . [[E]][x:=v]  (abstraction)
  The semantics is a homomorphism from syntax to a domain.
  Scott domains are the mathematical structure underlying this.
```

---

## Davidson's Truth-Conditional Approach

Donald Davidson (1917–2003) offered an alternative approach: use Tarski's truth theory as the core of a meaning theory.

```
  DAVIDSON'S PROPOSAL (1967):
  To know the meaning of a sentence S is to know its
  truth conditions.
  A truth theory for a language is a meaning theory for it.

  TARSKI'S CONVENTION T (adapted):
  A theory of truth for language L entails, for every sentence s of L:
  " s" is true-in-L iff p
  where p states the truth conditions of s.

  "Snow is white" is true iff snow is white.
  "It is raining" is true iff it is raining (at context c).

  COMPOSITIONALITY IN DAVIDSON:
  The truth theory must be COMPOSITIONAL —
  the truth conditions of complex sentences derive from
  the contributions of parts and structure.
  Davidson proved this can be done for a fragment of English
  using standard predicate calculus.

  EVENT SEMANTICS (Davidson, 1967):
  For action sentences, Davidson introduced events as
  first-class entities.

  "Brutus stabbed Caesar" = ∃e. stab(e) ∧ agent(e,Brutus) ∧ patient(e,Caesar)

  ADVANTAGE:
  "Brutus stabbed Caesar in the back with a knife slowly"
  = ∃e. stab(e) ∧ agent(e,Brutus) ∧ patient(e,Caesar)
        ∧ in(e,back) ∧ with(e,knife) ∧ slowly(e)
  Adverbs become predicates on events — fully compositional.
  Without events: you'd need new predicates for every adverb combination.
```

---

## Type-Theoretic Semantics and CS

```
  CURRY-HOWARD CORRESPONDENCE:
  Types in logic       ↔    Types in programming
  Propositions         ↔    Types
  Proofs               ↔    Programs
  Proof normalization  ↔    Program evaluation (β-reduction)

  Montague's type theory for natural language semantics
  IS the same type theory underlying typed λ-calculi (System F,
  Hindley-Milner, dependent types).

  FORMAL SEMANTICS → NLP:
  Semantic parsing: map natural language sentences to
  logical forms (λ-calculus expressions).
  Tools: λ-DCS, SEMPRE, compositional semantic parsers.
  Modern: fine-tuned language models generate λ-calculus or
  SQL or first-order logic from natural language queries.

  DENOTATIONAL SEMANTICS OF PROGRAMMING LANGUAGES:
  Scott & Strachey (1970s): assign mathematical denotations
  to program constructs compositionally.
  [[skip]] = identity state transformer
  [[x:=e]] = λσ . σ[x := [[e]]σ]
  [[C1;C2]] = [[C2]] ∘ [[C1]]
  This IS Montague semantics applied to programs instead of English.

  KNOWLEDGE REPRESENTATION:
  First-order logic, description logics, OWL —
  all use the same apparatus (type theory, model theory)
  to represent structured knowledge.
  Semantic web: RDF/OWL = formal semantics applied to web data.

  QUESTION ANSWERING SYSTEMS:
  Lambda calculus denotations for questions:
  "What is the capital of France?"
  = λx . capital-of(x, France)
  Applied to a knowledge base → Paris
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is compositionality formally? | The semantic interpretation function is a homomorphism from syntactic structure to semantic structure |
| What type does "every man" have in Montague? | (e → t) → t — a generalized quantifier; a function from predicates to truth values |
| What type does "walks" have? | e → t — a function from individuals to truth values |
| What is the semantic metalanguage of Montague grammar? | Typed lambda calculus (Church's simple type theory) + intensional operators |
| What does Davidson's event semantics do? | Introduces events as first-class entities, making adverbs predicates on events |
| What is an intension? | A function from possible worlds to extensions — the type s → τ in Montague's system |
| What connects Montague grammar to programming language theory? | Both use typed lambda calculus compositionally; denotational semantics IS Montague semantics for programs |

---

## Common Confusion Points

**Montague semantics ≠ generative grammar**: Chomsky's generative grammar studies syntactic competence — what sentences are grammatical. Montague grammar provides the semantics for syntactically analyzed sentences. They are compatible but independent projects.

**Intension ≠ sense**: Frege's Sinn is roughly approximated by Montague's intensions (functions from worlds to extensions). But they are not identical: Frege's sense is an abstract object, while Montague's intension is a function in a mathematical model. The connection is close enough to be explanatory but not definitional identity.

**Generalized quantifiers are second-order**: "Every man" of type (e → t) → t is a second-order function — it takes a property (set) and returns a truth value. This is second-order logic territory. Natural language quantification is inherently second-order (it is undecidable in general for this reason).

**Denotational semantics of PLs is direct Montague**: Dana Scott and Christopher Strachey built denotational semantics for programming languages using the same typed lambda calculus framework Montague used for natural language. This is not coincidence — it is the same mathematical infrastructure applied to two different formal languages.

**Lambda calculus β-reduction IS semantic composition**: When you apply [[NP]] to [[VP]], what you are doing computationally is β-reduction. The semantic derivation for "John walks" is literally a lambda calculus computation. This is why formal semanticists think of sentence meaning as computable (in principle).
