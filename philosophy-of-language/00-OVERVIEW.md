# Philosophy of Language — Landscape and Taxonomy

## The Big Picture

Philosophy of language asks: how do words, sentences, and utterances connect to the world, to meaning, and to minds? It sits at the intersection of logic, metaphysics, epistemology, and linguistics. For a TCS background: this is where the theory of formal languages intersects with the messy structure of natural language, and where semantics as computer scientists use it traces its intellectual lineage.

```
+-----------------------------------------------------------------------+
|                  PHILOSOPHY OF LANGUAGE MAP                           |
|                                                                       |
|  FORMAL TRADITION                  ORDINARY LANGUAGE TRADITION        |
|  (Frege → Russell → Carnap)        (Austin → Wittgenstein II → Grice) |
|                                                                       |
|  Goal: logical reconstruction      Goal: describe actual practice     |
|  of language; eliminate ambiguity  of language use                    |
|  Tool: formal logic / type theory  Tool: close conceptual analysis    |
|                                                                       |
|  +---------------------------+    +-------------------------------+   |
|  | SEMANTIC CORE             |    | PRAGMATIC CORE                |   |
|  | (meaning independent of   |    | (meaning in context)          |   |
|  | utterance context)        |    |                               |   |
|  |                           |    | speech acts                   |   |
|  | sense / reference         |    |   locutionary / illocutionary |   |
|  | truth conditions          |    |   / perlocutionary            |   |
|  | compositionality          |    | implicature (Grice maxims)    |   |
|  | possible worlds           |    | meaning as use                |   |
|  | formal / Montague grammar |    | language games                |   |
|  +---------------------------+    +-------------------------------+   |
|              |                                 |                      |
|              +----------------+----------------+                      |
|                               v                                       |
|                 +---------------------------+                         |
|                 | PHILOSOPHY OF MIND BRIDGE |                         |
|                 | intentionality            |                         |
|                 | propositional attitudes   |                         |
|                 | semantic externalism      |                         |
|                 | (Putnam: meanings not      |                         |
|                 |  in the head)             |                         |
|                 +---------------------------+                         |
+-----------------------------------------------------------------------+
```

---

## The Core Questions

Every position in philosophy of language is an answer to some combination of these:

```
+------------------------------------------------------------+
| QUESTION                     | KEY BATTLEGROUND            |
|------------------------------|-----------------------------|
| What is meaning?             | Use theory vs truth-        |
|                              | conditional theory          |
|------------------------------|-----------------------------|
| How do names refer?          | Description theory (Frege/  |
|                              | Russell) vs causal-         |
|                              | historical (Kripke)         |
|------------------------------|-----------------------------|
| What is the unit of          | Word? Sentence? Speech act? |
| meaning?                     | Utterance in context?       |
|------------------------------|-----------------------------|
| How does meaning relate      | Mentalism vs anti-mentalism |
| to mind?                     | Internalism vs externalism  |
|------------------------------|-----------------------------|
| Is meaning social or         | Private language argument   |
| private?                     | (Wittgenstein)              |
|------------------------------|-----------------------------|
| How do parts combine into    | Compositionality principle  |
| whole sentence meanings?     | (Frege, Montague)           |
+------------------------------------------------------------+
```

---

## Historical Arc

```
1879  Frege: Begriffsschrift — concept notation, formal logic
       |
1892  Frege: "Über Sinn und Bedeutung" — sense vs reference
       |
1905  Russell: "On Denoting" — theory of definite descriptions
       |
1913  Russell: logical atomism — world = atomic facts
       |
1921  Wittgenstein: Tractatus Logico-Philosophicus
       Picture theory of meaning; logic as scaffolding
       |
1923  Ogden & Richards: The Meaning of Meaning — semiotic triangle
       |
1934+ Carnap: logical syntax, verificationism (Vienna Circle)
       |
1940  Tarski: truth definitions (model theory foundation)
       |
1945+ Austin: Oxford ordinary language philosophy
       speech acts, "How to Do Things with Words"
       |
1950  Quine: "Two Dogmas of Empiricism" — analyticity attacked
       Word and Object (1960): radical translation indeterminacy
       |
1953  Wittgenstein: Philosophical Investigations (posthumous)
       meaning as use, language games, private language argument
       |
1957  Grice: conversational implicature, cooperative principle
       |
1963  Montague: formal semantics, treats natural language as formal
       |
1970  Kripke: "Naming and Necessity" — rigid designators
       causal-historical theory of reference, a posteriori necessity
       |
1973  Lewis: possible worlds semantics, counterpart theory
       Putnam: semantic externalism ("meanings ain't in the head")
       |
1984  Davidson: truth-conditional semantics, radical interpretation
       |
1990s Relevance theory (Sperber & Wilson), dynamic semantics
       |
2000s Interface with cognitive linguistics, formal pragmatics
```

---

## The Sense/Reference Architecture (Frege's Core Insight)

This one distinction reappears throughout philosophy of language and in type theory:

```
  EXPRESSION: "Hesperus"

  +--------------------+
  | SENSE (Sinn)       |   Mode of presentation.
  | "the star visible  |   How the object is conceptualized.
  | in the evening"    |   Different senses can pick out same referent.
  +--------------------+
           |
           | determines (in the right circumstances)
           v
  +--------------------+
  | REFERENCE          |   The actual object in the world.
  | (Bedeutung)        |   Venus.
  +--------------------+

  KEY: "Hesperus" and "Phosphorus" have the SAME reference (Venus),
       but DIFFERENT senses (different descriptions).

  This is why:
    "Hesperus = Hesperus"   is trivially true (a = a)
    "Hesperus = Phosphorus"  is informative! (discovered empirically)

  Same object, different modes of presentation.
  CS analogy: two different pointers to the same heap object,
  but with different "type annotations" describing how to access it.
```

---

## Truth-Conditional Semantics vs Use Theory

```
  TRUTH-CONDITIONAL (Frege, Davidson)     USE THEORY (Wittgenstein II)
  --------------------------------        ----------------------------
  Meaning = truth conditions.             Meaning = how expressions
  "Snow is white" means what it           are used in practice.
  does because it is true iff snow
  is white.                               "Ask not for the meaning,
                                          ask for the use."
  Tarski's Convention T:
  "P" is true iff P                       Language games: reporting,
                                          commanding, promising,
  Connects meaning to world structure.    greeting, joking, calculating.
  Clean formal semantics.
                                          No one language game = core.
  Awkward for:                            All are equally valid.
  - commands ("Close the door!")
  - questions ("What time is it?")        Better for performatives,
  - performatives ("I promise...")        commands, questions.
```

---

## Speech Act Layering (Austin/Searle)

```
  Utterance: "Can you pass the salt?"

  LAYER 1: LOCUTIONARY ACT
  +-----------------------------------------+
  | Literal content: a yes/no question about |
  | the hearer's physical ability to pass   |
  | salt.                                   |
  +-----------------------------------------+
                   |
                   v
  LAYER 2: ILLOCUTIONARY ACT
  +-----------------------------------------+
  | What the speaker is DOING by saying it: |
  | REQUESTING (not asking about ability).  |
  | The illocutionary force.                |
  +-----------------------------------------+
                   |
                   v
  LAYER 3: PERLOCUTIONARY ACT
  +-----------------------------------------+
  | The EFFECT on the hearer:               |
  | They pass the salt.                     |
  | (Causal consequence of the utterance.)  |
  +-----------------------------------------+

  Different sentences can share illocutionary force:
  "Pass the salt."            → direct request
  "Can you pass the salt?"    → indirect request (same force)
  "I'd love some salt."       → indirect request (even more indirect)
```

---

## Possible Worlds: The Semantic Tool for Modality

```
  MODAL STATEMENT: "Water is necessarily H₂O."

  Without possible worlds:
  How do we evaluate "necessarily"? No truth table handles it.

  With possible worlds:
  +--------------------------------------------------+
  | ACTUAL WORLD      | POSSIBLE WORLD 1             |
  | Water = H₂O       | Water = XYZ ← impossible!    |
  | (this world)      | (Kripke: there IS no world   |
  |                   | where water ≠ H₂O; it's rigid)|
  +--------------------------------------------------+

  □P   = P is true in ALL accessible worlds (necessity)
  ◇P   = P is true in SOME accessible world (possibility)

  Kripke's key move: RIGID DESIGNATORS
  Names like "water", "gold", "Aristotle" refer to the SAME
  thing in all possible worlds (where they refer at all).
  Definite descriptions ("the teacher of Alexander") are
  NOT rigid — different people might fit the description
  in different worlds.
```

---

## Formal Semantics: Compositionality

```
  FREGE'S PRINCIPLE:
  The meaning of a complex expression is a function of
  the meanings of its parts and their mode of combination.

  MATHEMATICAL FORMULATION (Montague):
  If α is a syntactic rule combining A and B,
  then there is a corresponding semantic rule
  combining [A] and [B] into [α(A,B)].

  This is why type theory works:
  (λx:τ. body) : τ → σ          (function type)
  f : τ → σ    applied to  a : τ  yields  f(a) : σ

  Syntax drives semantics.
  The λ-calculus IS Montague's underlying semantic language.
```

---

## Module Map

| File | Topic | Key Figures |
|------|-------|-------------|
| 01-FREGE.md | Sense, reference, concept script | Frege |
| 02-RUSSELL.md | Descriptions, logical atomism | Russell |
| 03-EARLY-WITTGENSTEIN.md | Picture theory, logical form | Wittgenstein I |
| 04-LATE-WITTGENSTEIN.md | Language games, meaning as use | Wittgenstein II |
| 05-SPEECH-ACTS.md | Locutionary/illocutionary/perlocutionary | Austin, Searle |
| 06-POSSIBLE-WORLDS.md | Kripke semantics, rigid designation | Kripke, Lewis |
| 07-FORMAL-SEMANTICS.md | Montague grammar, compositionality | Montague, Davidson |
| 08-PRAGMATICS.md | Grice's maxims, implicature | Grice, Sperber & Wilson |
| 09-COMPUTING-BRIDGE.md | Lambda calculus, type theory, denotational semantics | Church, Curry, Scott |

---

## Decision Cheat Sheet

| Question | Short Answer | See |
|----------|-------------|-----|
| What makes a name refer to its object? | Causal-historical chain (Kripke), not description alone | 06-POSSIBLE-WORLDS.md |
| What is the meaning of a sentence? | Its truth conditions (formal) or its use (pragmatic) | 03, 04, 07 |
| How can two coreferential terms differ in meaning? | Frege's sense/reference: same Bedeutung, different Sinn | 01-FREGE.md |
| What makes "The present king of France is bald" false vs nonsense? | Russell's theory of descriptions: it's false, not nonsensical | 02-RUSSELL.md |
| What does language DO beyond describe? | Speech acts — promise, warn, command, declare | 05-SPEECH-ACTS.md |
| How is compositionality formalized? | Montague grammar, type-theoretic semantics | 07-FORMAL-SEMANTICS.md |
| What is the computing connection? | Lambda calculus = Montague's semantic metalanguage | 09-COMPUTING-BRIDGE.md |
| Why can't meaning be private? | Wittgenstein's private language argument | 04-LATE-WITTGENSTEIN.md |

---

## Common Confusion Points

**Sense vs meaning vs reference**: "Meaning" is the informal term. Frege's technical split: Sinn (mode of presentation) vs Bedeutung (the actual referent). Some translate Bedeutung as "meaning," creating confusion. Bedeutung literally = "significance" but Frege uses it for the object referred to.

**Wittgenstein I vs II are not compatible**: The Tractatus and the Investigations are near-contradictory. Wittgenstein I thought language pictures logical form; II thought that view was a philosopher's disease he personally had spread. Do not synthesize them — they represent a radical change of mind.

**Austin's "performative" vs Butler's "performativity"**: Austin's performatives ("I hereby promise...") do things rather than describe. Judith Butler's "performativity" (identity is performed through repetition) is a later appropriation of Austin's term for a very different project.

**Possible worlds ≠ science fiction**: Possible worlds in Kripke/Lewis are a semantic device for evaluating modal statements. "Necessarily P" = P is true in all accessible worlds. It is model theory for modal logic, nothing more exotic.

**Analytic/synthetic distinction**: Quine's "Two Dogmas" (1950) attacked the idea that there are sentences true purely by meaning (analytic). This is central to understanding what Carnap and the Vienna Circle were doing and why Quine rejected it.
