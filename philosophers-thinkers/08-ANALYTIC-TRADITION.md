# The Analytic Tradition — Frege, Russell, Wittgenstein, Quine, Davidson

## Why This Section Is Your Home Base

The analytic tradition is the one that most directly overlaps with theoretical computer science. The connections are not superficial:

```
  ANALYTIC PHILOSOPHY                  TCS / FORMAL METHODS
  ────────────────────                 ────────────────────
  Frege's predicate logic         ──>  Foundation of first-order logic,
  (Begriffsschrift, 1879)              formal verification, model theory

  Russell's type theory           ──>  Type systems (Curry-Howard
  (Principia Mathematica, 1910)        correspondence bridges them)

  Wittgenstein's TLP              ──>  Formal semantics; the limits of
  (picture theory, logical form)       what a formal language can express

  Hilbert's program               ──>  Completeness, decidability
  (formalize all mathematics)          (Church, Turing, Gödel responded)

  Carnap's logical syntax         ──>  Programming language semantics;
                                       distinction of syntax/semantics

  Quine's ontological commitment  ──>  What entities does a formal theory
                                       commit us to? (model theory)

  Kripke's possible worlds        ──>  Modal logic in verification;
  (semantics for modal logic)          Kripke structures in model checking
```

---

## Frege — The Inventor of Modern Logic

**Gottlob Frege (1848–1925)** was largely ignored during his lifetime. Russell and Wittgenstein eventually recognized him as the founder of modern logic and philosophy of language.

### Begriffsschrift (1879) — Concept-Script

Frege's first major work. He invented:
- **Quantifiers**: "for all x" (∀) and "there exists x" (∃)
- **Predicate-argument structure**: distinguishing functions from arguments
- **Scope**: quantifiers bind variables within their scope
- **Conditionals and negation** as logical primitives

```
  WHAT ARISTOTLE'S LOGIC COULDN'T DO:

  "Every person loves some person"
  Aristotle: can't handle this — it requires two quantifiers.
  Frege: ∀x(Person(x) → ∃y(Person(y) ∧ Loves(x,y)))

  "No greatest prime number exists"
  Aristotle: can't express this.
  Frege: ¬∃x(Prime(x) ∧ ∀y(Prime(y) → y ≤ x))

  Relational reasoning, multiple quantifiers, nested structure:
  Aristotle's syllogistic couldn't do any of this.
  Frege could. This is why modern logic is entirely post-Fregean.
```

### Sense and Reference (Sinn und Bedeutung)

One of the most important distinctions in philosophy of language:

```
  EXAMPLE: "The Morning Star" and "The Evening Star"
  Both refer to the planet Venus.
  But they have different senses — different "modes of presentation."

  The sentence "The Morning Star is the Evening Star" is
  informative — it tells us something about the world.
  If they had the same sense, it would be trivially true.

  REFERENCE (Bedeutung): the object a term picks out.
                          Both names → Venus.

  SENSE (Sinn): the mode of presentation — the descriptive
               content that determines the reference.
               Different senses → same reference.

  Propositional attitudes (belief, desire):
  "Mary believes the Morning Star is visible" can be true
  even if "Mary believes the Evening Star is visible" is false,
  even though Morning Star = Evening Star.
  → Can't substitute coreferring terms in belief contexts.
  This is the problem of intensional contexts.
```

### The Context Principle

"Never ask for the meaning of a word in isolation, but only in the context of a proposition." This anticipates Wittgenstein's later language-game view and contextualist theories of meaning.

### The Logicist Program

Frege's life project: reduce all of arithmetic to pure logic. Grundgesetze der Arithmetik (1893, 1903) was his main attempt. Basic Law V states (roughly): for any property F, there is an extension (set) of all F-things.

Russell's letter (1902) showed Basic Law V is inconsistent — it generates Russell's Paradox. Frege wrote back: "Hardly anything more unfortunate can befall a scientific writer than to have one of the foundations of his edifice shaken after the work is finished." He never recovered philosophically.

---

## Russell — Logical Atomism and the Theory of Descriptions

**Bertrand Russell (1872–1970)** is the most publicly visible philosopher of the 20th century: polymath, pacifist, Nobel laureate in literature (1950), popularizer of logic and philosophy.

### Russell's Paradox

```
  Let R = the set of all sets that are not members of themselves.
  Is R a member of itself?

  If R ∈ R: then R must NOT be a member of itself (by definition of R).
  If R ∉ R: then R IS a member of itself (by definition of R).

  Contradiction either way. → Basic Law V is inconsistent.

  Frege's system collapses. Russell must build an alternative.
```

Russell's response: the **Theory of Types**. Sets are arranged in a hierarchy of types. A set can only have members from a lower type. The set R (talking about "all sets") can't be formed because you can't have a set that contains sets of its own type. This eliminates the paradox by forbidding the self-reference that generates it.

This is the direct ancestor of type systems in programming languages. The Curry-Howard correspondence maps propositions to types, proofs to programs — and the foundations go through Russell.

### Theory of Definite Descriptions (1905)

"On Denoting" — often called the most important paper in analytic philosophy:

```
  PROBLEM: "The present King of France is bald."

  France has no king. Is this sentence true, false, or meaningless?
  Frege: the sentence has no truth-value (reference fails).
  Russell: analyzes the sentence so it comes out false without
           requiring a non-existent referent.

  ANALYSIS via definite description:
  "The F is G" = "There exists exactly one F, and that F is G"
  ∃x(F(x) ∧ ∀y(F(y) → y=x) ∧ G(x))

  "The present King of France is bald" =
  "There exists exactly one present King of France, and they are bald"
  = FALSE (because there is no present King of France).

  The definite description is not a name — it is an incomplete
  symbol that disappears on analysis, replaced by quantified logic.

  WHY IT MATTERS:
  Meinong had posited a "realm of subsistence" for things like
  the golden mountain and the present King of France — they don't
  exist but somehow subsist. Russell shows you don't need this:
  logical analysis eliminates apparent reference to non-existents.
```

### Logical Atomism

Russell's metaphysics (parallel to Wittgenstein's TLP project):

```
  The world consists of atomic facts — simple, logically
  independent states of affairs.

  Language, at the fundamental level, consists of atomic
  propositions corresponding to atomic facts.

  Complex propositions are truth-functions of atomic propositions.

  Philosophical analysis = decompose complex propositions until
  you reach genuine atomic propositions.

  Hidden logical form ≠ surface grammatical form.
  "The present King of France is bald" looks like a subject-predicate
  sentence but is really an existential claim.
```

---

## Wittgenstein — Two Philosophies

**Ludwig Wittgenstein (1889–1951)** is the most influential philosopher of the 20th century in the analytic tradition — possibly of all of Western philosophy. He produced two philosophies that are in near-direct opposition, and both are seminal.

### The Tractatus Logico-Philosophicus (1921)

```
  CENTRAL THESIS: Language pictures the world.

  PICTURE THEORY:
  A proposition is a logical picture of a fact.
  ─ Names refer to simple objects (in the world)
  ─ Propositions are configurations of names,
    mirroring possible configurations of objects
  ─ A true proposition pictures an actual fact;
    a false proposition pictures a possible but
    non-actual arrangement

  LOGICAL FORM: What a proposition and the fact it pictures
  share — the form of correspondence. This logical form
  can't be stated; it shows itself.

  LIMITS OF LANGUAGE:
  "The limits of my language mean the limits of my world."
  What CAN be said: contingent facts about the world.
  What CANNOT be said: ethics, aesthetics, the meaning of life,
                        the self, logic itself, mystical experience.
  "Whereof one cannot speak, thereof one must be silent."

  STRUCTURE:
  The Tractatus has a numbered structure (1, 1.1, 1.11, 1.12...)
  and ends with a self-undermining move: "My propositions serve
  as elucidations in the following way: anyone who understands me
  eventually recognizes them as nonsensical." The ladder must
  be thrown away after climbing.
```

### Philosophical Investigations (1953, posthumous)

The PI is Wittgenstein's systematic repudiation of almost everything in the TLP:

```
  PICTURE THEORY REJECTED:
  Language doesn't have one fundamental form. Language is a
  collection of very different practices with different grammars.

  LANGUAGE GAMES (Sprachspiele):
  "The word 'language-game' is meant to bring into prominence
  the fact that the speaking of language is part of an activity,
  or of a form of life."

  Examples of language games: naming, describing, giving orders,
  reporting, speculating, making up a story, singing catches,
  guessing riddles, translating, asking, thanking, cursing.

  No common essence — they share "family resemblances."

  MEANING AS USE:
  "The meaning of a word is its use in the language."
  Not: meaning is a mental image corresponding to the word.
  Not: meaning is the object the word refers to.
  Rather: the meaning of a word = how it functions in practices.

  RULE-FOLLOWING PARADOX:
  "No course of action could be determined by a rule, because
  every course of action can be made out to accord with the rule."
  How do you know you're following the right rule?
  Any behavior can be interpreted as following some rule.
  → Following a rule is a practice, not an inner interpretation.

  PRIVATE LANGUAGE ARGUMENT:
  Can there be a language that only one person could understand?
  No — because language requires criteria for correct/incorrect use.
  There can be no purely private criteria: you need a public check.
  → Mental states (pain, etc.) are not private in the way we think.
```

**The Philosophical Method in PI**: Philosophy doesn't solve problems — it dissolves them by showing they arose from misunderstanding language. "Philosophy is a battle against the bewitchment of our intelligence by means of our language."

---

## The Vienna Circle and Logical Positivism

Between TLP and PI came the Vienna Circle (1920s–1930s): Schlick, Carnap, Neurath, Ayer. They read Wittgenstein's TLP as licensing a **verificationist criterion of meaning**:

```
  VERIFICATION PRINCIPLE:
  A statement is meaningful if and only if it is:
  (a) analytically true (true by logic/definition), OR
  (b) empirically verifiable (testable by observation)

  Everything else is meaningless — not false, but nonsense.
  Theology, metaphysics, ethics: all literally meaningless.

  The Vienna Circle applied this to demolish traditional
  philosophy and build scientific philosophy.

  Problem: the verification principle itself is neither
  analytically true nor empirically verifiable.
  It is self-refuting.

  Carnap modified to: pragmatic adoption of a "linguistic
  framework" — you choose a language system; within it,
  questions are meaningful; without it, they're meaningless.
```

---

## Quine — Two Dogmas of Empiricism

**W.V.O. Quine (1908–2000)** is the central figure in mid-20th-century analytic philosophy. His 1951 paper "Two Dogmas of Empiricism" is the most important intervention in analytic philosophy since Wittgenstein's PI.

### The Two Dogmas

```
  DOGMA 1: The Analytic/Synthetic Distinction
  Analytic truths (true by meaning alone, like "All bachelors
  are unmarried") vs. synthetic truths (true by fact).

  Quine's attack:
  "Bachelors are unmarried" is analytic because "bachelor" and
  "unmarried man" are synonymous. But what is synonymy?
  It requires analyticity to define it. Circular.

  No non-circular account of the analytic/synthetic distinction
  has been given. Quine concludes: it's a dogma — an article of
  faith without clear content.

  DOGMA 2: Reductionism
  Each meaningful statement has a set of sense experiences that
  would confirm or disconfirm it.

  Quine's attack (Duhem-Quine thesis):
  Statements face experience "not individually but only as
  a corporate body." The whole system of science faces the
  tribunal of experience together. Any observation that conflicts
  with theory can be accommodated by revising other parts
  of the system.

  CONSEQUENCE:
  If both dogmas fail, the boundary between philosophy and
  empirical science dissolves. Philosophy is not uniquely
  a priori or analytic — it is continuous with natural science.
  "Epistemology naturalized" — epistemology is part of
  cognitive science, not a first-philosophy.
```

### Ontological Commitment

"To be is to be the value of a bound variable":

```
  QUINE'S CRITERION:
  What does a theory commit you to believing exists?
  Answer: whatever you quantify over (∃x such that...).

  "There are prime numbers greater than 100"
  ∃x(Prime(x) ∧ x > 100)
  → This theory commits you to numbers existing.

  If you want to be a nominalist (no abstract objects),
  you must paraphrase statements about numbers so they don't
  quantify over numbers.

  This connects to the TCS question: what does a formal
  theory's semantics commit you to? Model theory asks exactly
  what Quine is asking.
```

---

## Davidson — Radical Interpretation and Anomalous Monism

**Donald Davidson (1917–2003)** extends and transforms both Quine's naturalism and the philosophy of language.

### Radical Interpretation

How do you interpret a completely foreign language with no linguistic help at all? You must maximize agreement — assume the speaker is generally right about the world (the Principle of Charity). Without this assumption, translation is impossible.

```
  PRINCIPLE OF CHARITY:
  Interpret a speaker so that their beliefs come out mostly true.

  Reason: If they held mostly false beliefs, you couldn't explain
  how they function in the world. Successful action requires
  mostly correct beliefs about the environment.

  Implication: radical disagreement about beliefs requires
  sharing a large background of agreement. Genuine translation
  requires agreement on most things.

  ANTI-RELATIVISM: There is no coherent "scheme" so different
  from ours that it could be largely false. (Against
  "conceptual schemes" that carve up reality differently —
  Davidson argues the scheme/content distinction doesn't work.)
```

### Anomalous Monism

```
  MIND-BODY PROBLEM (Davidson's solution):

  Physical events and mental events are identical (monism).
  But mental properties can't be reduced to physical properties
  (anomalous — no strict psychophysical laws).

  Token identity: every mental event = some physical event.
  Type non-identity: no mental type (pain, belief) = physical type.

  Why no psychophysical laws?
  Mental description is governed by rationality norms
  (beliefs and desires must be coherent).
  Physical description is governed by strict causal laws.
  These are different kinds of explanatory framework.
  You can't have strict laws connecting them.

  IMPLICATION: Eliminative materialism (replace mental talk
  with neuroscience) is wrong — mental vocabulary is
  irreducibly normative.
```

---

## Comparison Table

| Figure | Key Move | Central Text | TCS Connection |
|--------|----------|-------------|----------------|
| **Frege** | Invented quantifier logic; sense/reference | Begriffsschrift, "Sense and Reference" | Foundation of formal logic, model theory |
| **Russell** | Theory of types (response to paradox); theory of descriptions | Principia Mathematica, "On Denoting" | Type systems; Curry-Howard |
| **Wittgenstein (TLP)** | Language pictures world; limits of language | Tractatus Logico-Philosophicus | Formal semantics; decidability limits |
| **Wittgenstein (PI)** | Meaning as use; language games; rule-following | Philosophical Investigations | Pragmatics; language as social practice |
| **Carnap** | Linguistic frameworks; logical syntax | Logical Syntax of Language | Programming language semantics |
| **Quine** | No analytic/synthetic distinction; naturalized epistemology | "Two Dogmas," Word and Object | Ontological commitment; formal theory |
| **Davidson** | Radical interpretation; anomalous monism | Essays on Actions and Events | Mental vocabulary irreducibility |

---

## Who to Cite for What

| Concept | Cite |
|---------|------|
| Invention of predicate logic | Frege (Begriffsschrift, 1879) |
| Sense vs. reference | Frege ("Sense and Reference," 1892) |
| Russell's Paradox | Russell (letter to Frege, 1902) |
| Type theory (response to paradox) | Russell (Principia Mathematica, 1910) |
| Theory of definite descriptions | Russell ("On Denoting," 1905) |
| Language pictures facts | Wittgenstein (TLP, 1921) |
| Limits of language / silence | Wittgenstein (TLP §6.54–7) |
| Meaning as use; language games | Wittgenstein (PI §43, §§1–20) |
| Private language impossibility | Wittgenstein (PI §§243–315) |
| No analytic/synthetic distinction | Quine ("Two Dogmas," 1951) |
| Naturalized epistemology | Quine ("Epistemology Naturalized," 1969) |
| Radical interpretation / charity | Davidson ("Radical Interpretation," 1973) |
| Token identity / anomalous monism | Davidson ("Mental Events," 1970) |

---

## Common Confusion Points

**Frege's logic vs. Aristotle's logic** — Aristotle's syllogistic handles only subject-predicate sentences in fixed moods. Frege's predicate logic handles arbitrary relational structure, multiple quantifiers, and complex embeddings. Modern mathematics, computer science, and formal verification use Frege's logic. Aristotle's logic is historically important but technically obsolete.

**Russell's paradox is a curiosity** — It's a foundational crisis. It showed that naive set theory (Frege's Basic Law V) is inconsistent. The responses to it — type theory (Russell), Zermelo-Fraenkel set theory, von Neumann-Bernays-Gödel set theory — shaped all of 20th-century foundations of mathematics. Type systems in programming languages are a direct technical descendant.

**Wittgenstein TLP and PI are by different authors in effect** — Wittgenstein publicly repudiated the picture theory, the logical form doctrine, and the idea of a hidden logical structure. PI opens with a direct critique of Augustine's picture of language learning (and by implication, the TLP's assumptions). The early and late Wittgenstein are genuinely different philosophical positions.

**Quine attacked the distinction between logic and empirical claim** — "Two Dogmas" is sometimes read as saying mathematics is just empirical (revisable by experiment). Quine says mathematics is part of our web of belief and could in principle be revised under sufficiently extreme empirical pressure — but in practice, it's the last thing we'd revise. This is holism, not empiricism about logic.

**Kripke (not covered above but crucial)** — Saul Kripke's Naming and Necessity (1980) attacks Frege and Russell's description theory of names. Names are "rigid designators" — they refer to the same individual in all possible worlds, independent of any description. Water = H₂O is necessarily true but empirically discovered (a posteriori necessity). This revived metaphysics after Quine's apparent demolition. Kripke's possible-worlds semantics for modal logic is directly used in model checking (Kripke structures) in formal verification.
