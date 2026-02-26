# Frege: Sense, Reference, and Concept Script

## Why Frege Matters

Gottlob Frege (1848–1925) is the founder of modern logic and the direct ancestor of formal semantics, type theory, and the foundations of mathematics as the 20th century understood them. His work on sense and reference gave philosophy of language its central technical vocabulary. His concept notation (Begriffsschrift) gave us quantifiers and the predicate calculus. His project of reducing arithmetic to logic gave us the Frege-Russell tradition in foundations, and indirectly Russell's Paradox.

For a TCS background: Frege is the source of the predicate calculus you used in computability theory, the function/argument distinction underlying every λ-term, and the compositionality principle underlying every denotational semantics.

```
+-----------------------------------------------------------------------+
|                         FREGE'S CONTRIBUTIONS                         |
|                                                                       |
|  LOGIC                          SEMANTICS               FOUNDATIONS   |
|  -----                          ---------               -----------   |
|  Begriffsschrift (1879)         Sense/Reference (1892)  Grundlagen    |
|  - First-order predicate logic  - Sinn (mode of         (1884)        |
|  - Quantifiers: ∀, ∃            presentation)          - Arithmetic   |
|  - Function/argument form       - Bedeutung (referent)  from logic    |
|  - Conditional strokes          - Compositionality                    |
|  - Identity statements          - Sense determines      Grundgesetze  |
|                                 reference (contextually)(1893/1903)   |
|                                 - Sense ≠ reference     - Formal      |
|                                                          derivation   |
|                                 Concept and Object       - Doomed by  |
|                                 (1892)                   Russell's    |
|                                 - functions vs objects   Paradox      |
+-----------------------------------------------------------------------+
```

---

## The Sense/Reference Distinction (1892)

Frege's paper "Über Sinn und Bedeutung" (On Sense and Reference) starts with a puzzle about identity.

### The Puzzle of Informative Identity

```
  (1) Hesperus = Hesperus         trivially true, a priori
  (2) Hesperus = Phosphorus       empirically informative!

  Both are identity statements. Both are true.
  Both are about the same object: Venus.

  But (1) is a logical tautology. (2) was a discovery.

  HOW CAN THIS BE if names just pick out objects?
  If "Hesperus" and "Phosphorus" both = Venus, then
  (1) and (2) should be identical in cognitive value.
  But they clearly are not.
```

### Frege's Solution: Two Levels

```
  EVERY EXPRESSION HAS TWO SEMANTIC VALUES:

  SENSE (Sinn)                    REFERENCE (Bedeutung)
  ------------                    ---------------------
  Mode of presentation.           The actual object,
  The "how it is given."          function, or truth value.
  Conceptual content.

  "Hesperus"                      Venus
  sense: "the star seen in        reference: the planet Venus
         the evening western sky"

  "Phosphorus"                    Venus
  sense: "the star seen before    reference: the same planet!
         sunrise in the east"

  SAME reference, DIFFERENT senses.
  This explains why (2) is informative: we learn that two
  different modes of presentation pick out the same object.
```

### The Sense/Reference Diagram

```
  EXPRESSION
  "the morning star"
       |                    SENSE: mode of
       |---→ SENSE ------→  presentation; how
       |     (Sinn)         the object is
       |                    conceptually accessed
       |
       +---→ REFERENCE ─→   OBJECT: Venus
             (Bedeutung)    (the planet itself)

  The sense DETERMINES the reference (when there is one).
  The reference does NOT determine the sense uniquely.
  Many senses can pick out the same reference.
```

### Names Without Reference: The Odysseus Problem

```
  "Odysseus set foot on the shores of Ithaca while sound asleep."

  "Odysseus" has a SENSE (the hero of Homer's epic, etc.)
  "Odysseus" has NO REFERENCE — there is no such person.

  Frege: this sentence has a sense but no truth value.
  It expresses a thought (Gedanke) but the thought cannot be
  assessed as true or false because the subject fails to refer.

  This is a consequence of Frege's bivalence: every genuine
  proposition is either true or false. A sentence with a
  non-referring name produces an expression with sense but
  no truth value — a gap in the system.

  Contrast with Russell's solution: the problem goes away
  because names are disguised descriptions and existence
  is built into the analysis. (See 02-RUSSELL.md)
```

---

## Sense of Complex Expressions: Compositionality

```
  FREGE'S COMPOSITIONALITY PRINCIPLE:
  The sense (and reference) of a complex expression is
  determined by the senses (and references) of its parts.

  REFERENCE OF A SENTENCE = its truth value (T or F)
  ("sentences refer to truth values" — unusual claim)

  SENSE OF A SENTENCE = the thought (Gedanke) it expresses

  This principle is foundational for:
<!-- @editor[content/P1]: Typo — "Davison" should be "Davidson" -->
  - Every formal semantics (Montague, Tarski, Davison)
  - Every type-theoretic semantics
  - Compiler IR: meaning of compound expressions = f(subexpressions)
  - Denotational semantics of programming languages

  Structure:
  "The morning star is a planet"
   ↑ sense of whole = function of senses of parts
         ↑ sense of "morning star" contributes to
                ↑ sense of "is a planet" contributes to
   → whole sentence expresses a thought (true or false)
```

---

## Frege's Concept Notation (Begriffsschrift)

The first complete system of predicate logic, 1879. Before Frege, logic was Aristotelian syllogistics — powerful but limited to subject/predicate structure with no variables or quantifiers.

### What Frege Added

```
  OLD (Aristotelian):              NEW (Frege, 1879):
  "All men are mortal"             ∀x(Man(x) → Mortal(x))
  "Socrates is a man"              Man(Socrates)
  "Socrates is mortal"             ∴ Mortal(Socrates)

  Frege introduced:
  - QUANTIFIERS: ∀ (universal), ∃ (existential)
  - VARIABLES ranging over a domain
  - PREDICATE LETTERS: properties and relations
  - FUNCTION symbols: f(x), g(x,y)
  - The conditional: P → Q
  - Negation: ¬P
  - Identity: a = b

  This is the predicate calculus you used in TCS courses.
  Every proof system in CS — Hoare logic, temporal logic,
  type theory, modal logic — extends this base.
```

### Function/Argument Form

```
  KEY INSIGHT: Propositions have function-argument structure.
  This anticipates λ-calculus and type theory.

  "5 is a prime number"  =  Prime(5)
                                ↑        ↑
                            concept   object
                            (function) (argument)

  Concept = unsaturated (has a gap)
  Object  = saturated (fills the gap)

  Frege: "The concept 'prime' is essentially incomplete.
          The name '5' completes it."

  Compare:
  λx. (prime x)  applied to  5  →  (prime 5)
  This is exactly the λ-calculus that Church formalized.
  Church's λ-calculus is Frege's function/argument formalized.
```

---

## Concept and Object (1892)

A second major paper, often overshadowed by Sense/Reference.

```
  OBJECTS: complete, saturated
  All individuals: Socrates, the number 7, the planet Venus,
  truth values (T, F are objects for Frege), extensions of concepts.

  CONCEPTS: incomplete, unsaturated, predicate-like
  "__ is prime" — needs an argument
  "__ is taller than __" — needs two arguments (a relation)

  CRUCIAL: A concept is NOT an object.
  "The concept 'horse'" — when you nominalize a concept,
  you produce an OBJECT that refers to the concept,
  but it is no longer the concept itself.
  (Frege calls this the "concept 'horse' paradox".)

  This distinction maps to:
  TYPE THEORY:   a : Type   vs   f : Type → Type
  Functions vs their values; types vs terms.
```

---

## Frege on Identity

```
  METALINGUISTIC VIEW (early Frege):
  "a = b" means: the signs "a" and "b" refer to the same thing.
  Problem: makes identity a linguistic fact, not a worldly one.

  OBJECT-LEVEL VIEW (later Frege, after Sense/Reference):
  "a = b" states that the object referred to by "a" is
  the same as the object referred to by "b".
  The informativeness of "a = b" when a ≠ b (as descriptions)
  is explained by their different SENSES.

  This gives us:
  a = a   →  trivially true (same sense, same reference)
  a = b   →  potentially informative (different senses,
              discovered to have same reference)
```

---

## Frege's Logical Hierarchy

```
  TRUTH VALUES (T, F)
  are the references of sentences
           ↑
  THOUGHTS (Gedanken)
  are the senses of sentences
  = what sentences express
  = shareable, objective (not psychological)
           ↑
  CONCEPTS and RELATIONS
  are functions from objects to truth values
  (functions from n-tuples of objects to T/F)
           ↑
  OBJECTS
  are the references of names and definite descriptions
  (individuals, numbers, truth values themselves)
```

---

## The Frege-Russell Connection

```
  Frege → Russell correspondence (1902):
  Russell discovered that Frege's Basic Law V
  (every concept has an extension = the set of
  things falling under it) leads to contradiction.

  Russell's Paradox:
  Let R = {x : x ∉ x}   ("the set of all sets not
                          members of themselves")
  R ∈ R  ↔  R ∉ R        ← contradiction

  This is derivable in Frege's system.
  The Grundgesetze project collapsed.

  But: the predicate calculus survived intact.
  Russell and Whitehead built on Frege's logic (not on
  Basic Law V) in Principia Mathematica.
  Russell's theory of types was the repair.
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why is "a = a" trivial but "a = b" informative? | Same reference, different senses — learning they corefer is non-trivial |
| What is a "sense"? | Mode of presentation — how an expression conceptually presents its referent |
| What is a "Bedeutung"? | The actual referent: an object, a function, or a truth value |
| What does a sentence refer to? | Its truth value (T or F) — unusual but Fregean |
| What does a sentence express? | A thought (Gedanke) — its sense |
| Why are concepts "unsaturated"? | They have gaps to be filled by object-names; function/argument analogy |
| What is Frege's compositionality principle? | The sense/reference of a complex expression = f(senses/references of parts) |

---

## Common Confusion Points

**"Bedeutung" ≠ "meaning"**: Many translators use "meaning" for Bedeutung, which obscures the sense/reference distinction. Bedeutung = reference, the actual object. Sinn = mode of presentation. Frege is rigorous: do not conflate them.

**Senses are objective, not psychological**: Frege insists senses (thoughts) are not mental images or psychological states. They are abstract objects grasped by multiple minds. "2 + 2 = 4" expresses the same thought regardless of who thinks it. He is a Platonist about senses.

**Frege's system is inconsistent**: Basic Law V (naïve comprehension) leads to Russell's Paradox. Frege's LOGIC (predicate calculus) is consistent and is what we inherited. His FOUNDATIONS OF ARITHMETIC failed.

**Function/argument ≠ subject/predicate**: Traditional grammar says "Socrates" is the subject and "is mortal" is the predicate. Frege reinterprets: "is mortal" is an unsaturated function (a concept), "Socrates" is the argument (an object). The grammatical categories and the logical categories can diverge.

**Frege's two-dimensional semantics**: Expressions have BOTH a sense AND a reference. In indirect discourse ("John believes that..."), the expression inside the belief context refers to its SENSE, not its usual reference. This is Frege's account of intensional contexts — the reference shifts in oblique discourse.
