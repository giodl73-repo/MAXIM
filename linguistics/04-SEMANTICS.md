# Semantics — Linguistic Meaning

## The Big Picture

Semantics is the study of linguistic meaning — what words and sentences mean, how meaning composes, and how it relates to truth conditions and the world.

```
+-------------------------------------------------------------------+
|                    SEMANTICS LANDSCAPE                             |
|                                                                   |
|  TRUTH-CONDITIONAL          COMPOSITIONAL                        |
|  SEMANTICS                  SEMANTICS                            |
|  (Frege, Tarski,            (how word meanings                   |
|   Montague)                  combine — Frege's               |
|  Meaning = intension         principle: meaning of              |
|  + extension                 whole from parts)                   |
|                                                                   |
|  LAMBDA CALCULUS            LEXICAL SEMANTICS                    |
|  for semantic               (word meaning:                       |
|  composition — TCS bridge   prototype theory,                    |
|  (types, function app,      thematic roles,                      |
|   quantifier raising)       frames, fields)                      |
|                                                                   |
|  SCOPE AMBIGUITY            SEMANTIC RELATIONS                   |
|  (every, some, not —        synonymy, antonymy,                  |
|   quantifier scope)         hyponymy, meronymy,                  |
|                             entailment, presupposition           |
+-------------------------------------------------------------------+
```

---

## Part I: Truth-Conditional Semantics

**Frege's program** (1892): Distinguish *sense* (Sinn) and *reference* (Bedeutung):

```
SENSE vs. REFERENCE:

  "The morning star" ————————\
                              +——→  Venus  (same REFERENCE)
  "The evening star" ————————/

  But different SENSE — you can discover they're the same (it's informative),
  which wouldn't be possible if sense = reference.

  Frege: sense determines reference.
  "The morning star" = the unique celestial body visible before sunrise
  "The evening star" = the unique celestial body visible after sunset
  Both descriptions pick out Venus, but via different senses.
```

**Extension and Intension:**

| Term | Definition | Example |
|------|------------|---------|
| **Extension** | The actual set of things in the world that a term picks out | Extension of "cat" = all cats in the actual world |
| **Intension** | The function from possible worlds to extensions | "cat" picks out the set of cats in each possible world |
| **Truth value** | Extension of a sentence (T or F) | "Snow is white" has extension TRUE |
| **Proposition** | Intension of a sentence | The meaning of "Snow is white" — true in worlds with white snow |

**Tarski's Convention T:**

A semantic theory is adequate iff for every sentence S:
```
"S" is true iff S.

"Snow is white" is true iff snow is white.
```

Simple and profound: meaning is given by truth conditions, not by use. This grounds formal semantics.

---

## Part II: Compositionality — Frege's Principle

**Principle of Compositionality:**
The meaning of a complex expression is a function of the meanings of its parts and how they are syntactically combined.

```
COMPOSITIONALITY IN ACTION:

"The cat sat on the mat"

  [[the cat]] = the unique salient cat in context (Russell: ιx[cat(x)])
  [[sat]] = λx.λe.sat(x)(e)  (a function: takes x, returns event property)
  [[on the mat]] = λx.on(x, mat)
  ...combine according to syntactic structure
```

**Why compositionality matters:** Natural language has infinite sentences. Speakers understand novel sentences. They must be computing meaning from parts — there's no way to memorize all possible sentences.

**Limits of strict compositionality:** Idioms ("kick the bucket"), metaphors, certain constructions — meaning not fully predictable from parts. Formal semantics handles these via non-compositional lexical entries or construction grammar.

---

## Part III: Lambda Calculus for Semantics — The TCS Bridge

You know λ-calculus. Here it is deployed for natural language semantics (Montague Grammar, 1970).

### Type Theory for Semantic Types

```
BASIC TYPES:
  e — entity type (individuals in the domain: people, places, things)
  t — truth value (true or false)

FUNCTION TYPES (recursive):
  ⟨e, t⟩ — function from entities to truth values = a PREDICATE / SET
  ⟨e, ⟨e, t⟩⟩ — function from entities to predicates = a RELATION
  ⟨⟨e, t⟩, t⟩ — function from predicates to truth values = a QUANTIFIER
  ⟨s, t⟩ — function from possible worlds to truth values = PROPOSITION

EXAMPLES:
  "cat"    : ⟨e, t⟩    — a set of cats: λx.cat(x)
  "sees"   : ⟨e, ⟨e, t⟩⟩ — relation: λy.λx.sees(x, y)
  "every"  : ⟨⟨e,t⟩, ⟨⟨e,t⟩, t⟩⟩ — takes predicate, returns predicate-to-t
```

### Function Application

```
SEMANTIC COMPOSITION = FUNCTION APPLICATION (β-reduction):

  "John runs"
  [[John]]  = j                           (type e)
  [[runs]]  = λx.run(x)                   (type ⟨e, t⟩)
  [[John runs]] = [[runs]]([[John]])
               = (λx.run(x))(j)
               = run(j)                   (type t)

  "John sees Mary"
  [[sees]]  = λy.λx.sees(x,y)            (type ⟨e, ⟨e, t⟩⟩)
  [[Mary]]  = m                           (type e)
  [[sees Mary]] = (λy.λx.sees(x,y))(m)
               = λx.sees(x,m)            (type ⟨e, t⟩)
  [[John sees Mary]] = (λx.sees(x,m))(j)
                     = sees(j, m)         (type t)
```

### Quantifiers

The most powerful use of λ-semantics: quantifiers as generalized quantifiers.

```
"Every cat runs"

  [[every]] = λP.λQ.∀x[P(x) → Q(x)]    (type ⟨⟨e,t⟩, ⟨⟨e,t⟩, t⟩⟩)
  [[cat]]   = λx.cat(x)                 (type ⟨e, t⟩)

  [[every cat]] = [[every]]([[cat]])
               = (λP.λQ.∀x[P(x) → Q(x)])(λx.cat(x))
               = λQ.∀x[cat(x) → Q(x)]   (type ⟨⟨e,t⟩, t⟩)

  [[every cat runs]]
               = (λQ.∀x[cat(x) → Q(x)])(λx.run(x))
               = ∀x[cat(x) → run(x)]    (type t)

  Translation: "for every x, if x is a cat, then x runs"
```

**Some** (existential quantifier):
```
  [[some]] = λP.λQ.∃x[P(x) ∧ Q(x)]

  "Some cat runs" → ∃x[cat(x) ∧ run(x)]
```

---

## Part IV: Quantifier Scope Ambiguity

Scope ambiguity is real and systematic — not just vagueness:

```
"Every student read some book"

READING 1 (∀ > ∃ — surface scope):
  ∀x[student(x) → ∃y[book(y) ∧ read(x, y)]]
  "For every student, there exists a (possibly different) book they read."
  → students may have read different books

READING 2 (∃ > ∀ — inverse scope):
  ∃y[book(y) ∧ ∀x[student(x) → read(x, y)]]
  "There exists a specific book that every student read."
  → one book, read by all students

Both readings are grammatical for this sentence. In context, disambiguation
via discourse.
```

**Quantifier Raising (QR)**: In LF (Logical Form), quantifiers move to take scope:

```
"Every student_i [t_i read some book]"
→ QR "every student" to high position
→ "some book_j [every student_i [t_i read t_j]]"

The two readings correspond to two LF derivations with different QR orders.
```

---

## Part V: Semantic Relations

### Between Words

| Relation | Definition | Example |
|----------|------------|---------|
| **Synonymy** | Same meaning (near-synonymy is common; full synonymy rare) | purchase/buy, sofa/couch |
| **Antonymy** | Opposed meanings (three types below) | hot/cold, alive/dead |
| **Hyponymy** | X is a subtype of Y (X entails Y) | rose → flower, oak → tree |
| **Meronymy** | X is a part of Y | finger → hand, wheel → car |
| **Polysemy** | One word, multiple related meanings | "bank" (river bank, financial institution) |
| **Homonymy** | One form, multiple unrelated meanings | "bat" (animal, cricket bat) |
| **Semantic field** | Words related by domain | Temperature: hot/warm/cool/cold/tepid/lukewarm |

**Three types of antonymy:**

| Type | Description | Example |
|------|-------------|---------|
| **Gradable** | A continuum between them; negating one doesn't assert the other | hot/cold — not hot ≠ cold (could be warm) |
| **Complementary** | Binary — exactly one of each pair is true | alive/dead, open/closed |
| **Converse** | Describe same relation from different viewpoints | above/below, buy/sell, parent/child |

---

## Part VI: Entailment, Presupposition, Implicature

Three different ways sentences "imply" other things:

```
ENTAILMENT:
  S entails S' iff in every world where S is true, S' is true.
  Logical consequence.

  "John knows that Mary left" → "Mary left"  (entailment — knowledge is factive)
  Negation: "John doesn't know that Mary left" → "Mary left"  (presupposition — survives)

  Entailment does NOT survive negation:
  "John ate the pizza" → "The pizza was eaten"
  "John didn't eat the pizza" → ↝ "The pizza was eaten"  ✗
```

```
PRESUPPOSITION:
  S presupposes S' iff both S and ¬S require S' to be true.

  "The king of France is bald" presupposes "There is a king of France"
  "The king of France is not bald" presupposes "There is a king of France"
  Both are truth-valueless if France has no king (or false — theoretically disputed)

  Russell's analysis: presupposition as existential entailment
  "The F is G" = ∃x[F(x) ∧ ∀y[F(y) → y=x] ∧ G(x)]

  But if presupposition fails: sentence is strange, not just false.
```

```
IMPLICATURE:
  S implicates S' iff S's utterance (pragmatically) suggests S',
  but this is cancelable without contradiction.

  "Some students passed" implicates "Not all students passed"
  (quantity implicature — speaker would have said "all" if that were true)
  But: "Some students passed — in fact, all of them did" — not contradictory

  Implicature is the business of PRAGMATICS (next file).
```

---

## Part VII: Prototype Theory (Rosch)

Classical theory: meaning = necessary and sufficient conditions. "Bachelor" = adult + male + unmarried.

**Problem**: Most concepts don't have sharp boundaries:
- Is a tomato a fruit? (botanically yes, culinarily no)
- Is Pluto a planet? (definitional dispute, not a logic error)
- Is a penguin a bird? (yes but atypical — doesn't fit the "bird schema")

<!-- @editor[audience/P3]: Prototype theory section explains categorization from scratch — the learner has type theory and set-membership from MIT TCS; lead with the contrast to classical (necessary+sufficient) rather than building up from basics -->
**Prototype theory** (Rosch 1975):

```
CATEGORY STRUCTURE:
  Core/Prototype: most typical member(s) — robin for BIRD
  Gradient: members with varying degrees of membership
  Fuzzy boundaries: no sharp in/out

  BIRD:
    Central: robin, sparrow, finch
    Less typical: chicken, penguin, ostrich, bat (not a bird, but "bird-like")
    Family resemblance: no one feature shared by all

TYPICALITY EFFECTS:
  "Is a robin a bird?" → fast RT
  "Is a penguin a bird?" → slower RT
  "A robin is a more typical bird than a penguin" — felicitous statement
```

**Basic level categories:** The most cognitively privileged level (neither too abstract nor too specific):
- Superordinate: furniture (too abstract, few shared features)
- **Basic level**: chair (most informative, fastest identification)
- Subordinate: rocking chair (too specific for efficient categorization)

---

## Part VIII: Thematic Roles

Between syntax and semantics: the argument structure of verbs.

```
THEMATIC (Θ) ROLES:

  AGENT:     volitional initiator of action — John broke the window.
  PATIENT:   entity undergoing change of state — the window (broke)
  THEME:     entity in motion or being located — I put the book on the shelf.
  EXPERIENCER: entity undergoing mental state — John fears dogs.
  GOAL:      endpoint of motion — I sent it to Mary.
  SOURCE:    origin of motion — She came from Paris.
  INSTRUMENT: means by which action performed — She cut it with a knife.
  BENEFACTIVE: entity for whose benefit — I baked a cake for her.
  LOCATION:  place where action occurs — He lives in Paris.
```

**Linking to syntax** (the **Linking** or **Argument Realization** problem):

```
AGENT → Subject in active sentences
PATIENT → Object in active sentences → Subject in passive
EXPERIENCER → Subject with psychological verbs ("John fears dogs")
              or Object ("Dogs frighten John") — alternation reveals structure

"John broke the window"  — John=AGENT/Subject, window=PATIENT/Object
"The window broke"       — window=PATIENT/Subject (unaccusative)
"John broke the window with a hammer" — hammer=INSTRUMENT/PP
```

---

## Decision Cheat Sheet

| Phenomenon | Analysis | Formal tool |
|------------|----------|------------|
| "The morning star = the evening star" | Sense ≠ reference | Fregean sense/Bedeutung |
| "Every student read some book" (ambiguous) | Quantifier scope | QR in LF, two derivations |
| "John knows that Mary left" → "Mary left" even when negated | Presupposition (factive) | Presupposition trigger |
| "Some students passed" ⇝ "not all" | Quantity implicature | Gricean maxims |
| "Robin is a better example of bird than ostrich" | Prototype effects | Typicality gradient |
| "The cat" refers to a specific cat | Definite description | Russell's ιx operator |
| "John admires himself" — who does "himself" refer to? | Binding + semantics | Anaphora resolution |
| "dog" means what? | Lexical semantics | Extension = set of dogs; Intension = λw.{x | dog(x) in w} |

---

## Common Confusion Points

**Truth conditions ≠ propositional content ≠ meaning:**
"Can you pass the salt?" — truth conditions are about the hearer's ability (probably true), but meaning/use is a request. Pragmatics (next file) handles the gap.

**Sense and reference are Frege's, not universal:**
Many philosophers use "meaning" and "reference" differently. In linguistics, "semantic content" often conflates sense and reference. The Frege/Russell debate about definite descriptions is still live.

**Entailment vs. Logical Implication:**
In formal semantics, entailment is the semantic relation (truth in all worlds). Logical implication (derivability) is the proof-theoretic relation. They align under completeness, but the distinction matters.

**Polysemy vs. Homonymy:**
"Bank" (river/financial) = homonymy (historically unrelated — two different words). "Run" (run a race, run a business, colors run) = polysemy (related meanings, one word — all involve some notion of flow/process). The line is blurry and sometimes theoretically motivated.

**Prototype theory doesn't replace classical categories everywhere:**
Mathematical concepts (prime number, triangle) have classical definitions with necessary and sufficient conditions. Prototype effects are strongest for natural kinds and artifacts, not for formal/scientific categories.

**Lambda calculus here is not computation:**
In semantics, λ-terms are meaning representations — mathematical objects, not running programs. β-reduction is a modeling tool for compositionality, not an algorithm being executed (though in computational semantics, that distinction blurs).
