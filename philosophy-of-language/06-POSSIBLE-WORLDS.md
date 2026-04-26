# Possible Worlds Semantics: Kripke and Lewis

## The Problem Being Solved

Modal logic — the logic of necessity and possibility — was formally developed by C.I. Lewis in the 1910s–1930s. It adds operators □ (necessarily) and ◇ (possibly) to propositional/predicate logic. But what is the SEMANTICS for these operators? What makes "necessarily P" true or false? Possible worlds semantics provides the model theory.

For a TCS background: possible worlds semantics is Kripke semantics for modal logic, which you likely encountered in temporal logic, dynamic logic, or epistemic logic. The philosophical content is richer — it addresses metaphysical necessity, the semantics of natural language, and how proper names work.

```
+-----------------------------------------------------------------------+
|                    POSSIBLE WORLDS FRAMEWORK                          |
|                                                                       |
|  ACTUAL WORLD              POSSIBLE WORLDS                            |
|  (this world)              (all ways the world could be)              |
|                                                                       |
|  "Water is H₂O" TRUE       World w2: water = XYZ (impossible: rigid)  |
|  "Obama is tall" TRUE       World w3: no Obama ever born              |
|  "There are dragons" FALSE  World w4: dragons exist                   |
|  "2+2=5" FALSE              World w5: no world — necessary falsehood  |
|                                                                       |
|  SEMANTICS:                                                           |
|  □P (necessarily P): P is true in ALL accessible worlds               |
|  ◇P (possibly P):    P is true in SOME accessible world               |
|                                                                       |
|  ACCESSIBILITY RELATION R(w, w'):                                     |
|  w' is accessible from w = w' is relevant for evaluating              |
|  necessity/possibility from perspective of w                          |
|  Different modal logics = different properties of R                   |
+-----------------------------------------------------------------------+
```

---

## Kripke Semantics for Modal Logic

Saul Kripke developed the standard model theory for modal logic in 1959 (at age 18). A Kripke model is a triple M = ⟨W, R, V⟩.

```
  W: A set of possible worlds (just abstract entities — no metaphysics yet)
  R: Accessibility relation — R ⊆ W × W
  V: Valuation — V: PropVar × W → {T, F}
     (each propositional variable gets a truth value at each world)

  TRUTH CONDITIONS:
  M, w ⊨ p         iff  V(p, w) = T                (atomic)
  M, w ⊨ ¬φ        iff  M, w ⊭ φ
  M, w ⊨ φ ∧ ψ     iff  M, w ⊨ φ  and  M, w ⊨ ψ
  M, w ⊨ □φ        iff  for all w': if R(w,w') then M, w' ⊨ φ
  M, w ⊨ ◇φ        iff  there exists w': R(w,w') and M, w' ⊨ φ

  DIFFERENT MODAL LOGICS:
  K:    No constraints on R  (minimal modal logic)
  T:    R is reflexive: R(w,w) for all w  (what's actual is possible)
  S4:   T + R is transitive  (if w' accessible, w' accessible worlds accessible)
  S5:   T + R is equivalence relation  (symmetric + transitive)
        = □P ↔ □□P, ◇P ↔ □◇P
        The standard for alethic modality (necessity, possibility)

  CS APPLICATIONS:
  Temporal logic: worlds = time points, R = "later than"
  Epistemic logic: worlds = possibilities agent doesn't exclude,
                  R = "indistinguishable from agent's perspective"
  Dynamic logic: worlds = program states, R = "program transition"
                 [α]P = □P over transitions of program α
```

---

## Kripke's Philosophical Innovations (Naming and Necessity)

Kripke's 1970 lectures (published 1980) revolutionized philosophy of language by arguing against Russell's description theory of names.

### Rigid Designators

```
  DESCRIPTION THEORY OF NAMES (Russell, Frege):
  "Aristotle" = "the philosopher who was Plato's student and
                 taught Alexander the Great"
  (or some other description)

  PROBLEMS WITH DESCRIPTION THEORY:
  1. "Aristotle could have been a farmer" seems true.
     But: if "Aristotle" = "Plato's student who taught Alexander,"
     then "Aristotle could have been a farmer" means
     "Plato's student who taught Alexander could have been
      a farmer (instead of Plato's student who taught Alexander)"
     which is nearly contradictory.

  2. What if Aristotle had not done any of these things?
     If he hadn't taught Alexander, would "Aristotle" fail to refer?
     Clearly not — Aristotle would still be Aristotle.

  3. Epistemic vs metaphysical: we could be WRONG about the
     descriptions. Aristotle might not have really taught Alexander.
     But "Aristotle" would still refer to Aristotle.

  KRIPKE'S ALTERNATIVE: RIGID DESIGNATORS

  A designator is RIGID if it refers to the same object in
  all possible worlds (where it refers at all).

  Proper names are rigid designators.
  "Aristotle" picks out the actual individual Aristotle
  in EVERY world where we consider that individual.

  Definite descriptions are typically NOT rigid:
  "The teacher of Alexander" refers to Aristotle in the actual world,
  but in a world where Plato taught Alexander, it refers to Plato.
```

### The Modal Argument

```
  COMPARING:

  "Aristotle was the teacher of Alexander"
  True in the actual world, but false in worlds where
  Alexander had a different teacher.
  → CONTINGENT (could have been otherwise)

  "Aristotle = Aristotle"
  True in all worlds. Necessarily true.
  → NECESSARY (trivially)

  BUT:

  "Hesperus = Phosphorus" (both = Venus)
  In every world where both exist and refer,
  they pick out Venus. So this is NECESSARY if true.
  But it was an ASTRONOMICAL DISCOVERY.
  It is a posteriori (known by observation, not logic).

  KRIPKE'S CRUCIAL DISTINCTION:
  NECESSITY ≠ A PRIORI
  CONTINGENCY ≠ A POSTERIORI

  Traditional view conflated these.
  Kant assumed: all necessary truths are a priori.
  Kripke shows: "Hesperus = Phosphorus" is:
    - Necessarily true (if true — it is)
    - A posteriori (discovered empirically)

  Kinds of truth:
  A priori necessary:   "2+2=4", logical truths
  A priori contingent:  some definitions, reference-fixers
  A posteriori necessary: "Water is H₂O", "Hesperus = Phosphorus"
  A posteriori contingent: most empirical facts
```

---

## Natural Kind Terms and Semantic Externalism

Kripke extended his analysis to natural kind terms: "water," "gold," "tiger."

### The Twin Earth Argument (Putnam)

```
  HILARY PUTNAM's thought experiment (1975):

  EARTH: H₂O fills the oceans. We call it "water."
  TWIN EARTH: Superficially identical, but the liquid that
  fills the oceans has molecular formula XYZ (different compound).
  Tastes, behaves identically to our water.
  Twin Earth inhabitants call it "water" too.

  QUESTION: In 1750, before chemistry was known, did
  Earthlings and Twin Earthlings mean the same thing by "water"?

  PUTNAM'S ANSWER: NO.
  "Water" on Earth picks out H₂O.
  "Water" on Twin Earth picks out XYZ.
  Even though the two communities had identical mental states
  and couldn't tell the difference.

  CONCLUSION (Semantic Externalism):
  "Meanings ain't in the head."
  What a term refers to depends on the EXTERNAL WORLD,
  not just on the speaker's mental representation.
  The MEANING of "water" includes reference to the actual
  chemical substance in the speaker's environment.

  INDEXICALITY OF NATURAL KINDS:
  "Water" is implicitly indexical: "the stuff that is the same
  substance as this" (demonstrating the local liquid).
  The meaning includes the actual substance discovered to be H₂O.
```

### The Causal-Historical Theory of Reference

```
  KRIPKE/PUTNAM'S ALTERNATIVE TO DESCRIPTION THEORY:

  HOW NAMES GET THEIR REFERENCE:
  1. INITIAL GROUNDING (dubbing event):
     "Let's call this baby 'Aristotle'."
     Or: "This substance is 'gold'."
     The reference is fixed by ostension or description
     (but the reference, once fixed, tracks the object,
     not the description).

  2. CAUSAL CHAIN:
     The name is passed from speaker to speaker in a
     community via a causal chain of reference-preserving uses.
     Each user intends to use the name as others have used it.
     The reference travels through the chain.

  3. REFERENCE PRESERVED, NOT VIA DESCRIPTION:
     I can refer to Aristotle without knowing ANY description
     that uniquely picks him out.
     My use is causally connected to a chain going back to
     people who were acquainted with (or close to) Aristotle.

  DIAGRAM:
  Aristotle ──(dubbing)──→ person A
                              ↓ (communication)
                           person B
                              ↓
                           ...
                              ↓
                           ME (today)

  My use of "Aristotle" refers to Aristotle because
  my use is linked, by a chain of communication,
  to an initial baptism of the actual person.
```

---

## Lewis: Modal Realism and Counterpart Theory

David Lewis (1941–2001) accepted possible worlds not just as a semantic tool but as REAL entities. This is the most controversial position in modal metaphysics.

### Modal Realism

```
  LEWIS'S CLAIM:
  Possible worlds are REAL, concrete, physical entities —
  as real as the actual world.
  They exist; they are just spatiotemporally inaccessible from us.
  "Actual" is an indexical: it means "this world, where I am."
  (Like "here" and "now" — indexical, not a special status.)

  WHY POSIT REAL POSSIBLE WORLDS?
  Lewis's argument: theoretical simplicity and explanatory power.
  They provide:
  - Semantics for modal operators without mystery
  - Analysis of counterfactuals
  - Analysis of properties (as sets of possible individuals)
  - Analysis of propositions (as sets of possible worlds)
  - Analysis of causation (counterfactual dependence)
  Everything can be cashed out in terms of worlds + individuals.

  OBJECTION: Too many worlds! You believe in unicorns (in some world)?
  Lewis: yes, somewhere — just not here. "There are unicorns"
  is context-sensitive; in our world, false; in theirs, true.
```

### Counterpart Theory

```
  PROBLEM: In modal realism, the same individual cannot literally
  exist in multiple worlds (worlds are spatiotemporally isolated).

  So what does "Aristotle could have been a farmer" mean?

  COUNTERPART THEORY:
  In possible worlds where Aristotle could have been a farmer,
  there is a COUNTERPART of Aristotle — someone sufficiently similar
  to the actual Aristotle — who is a farmer.

  Modal statements about individuals are about their counterparts
  in other worlds.

  "Aristotle could have been a farmer"
  = "There is a world w and an individual y in w such that
    y is a counterpart of Aristotle, and y is a farmer in w"

  CONTRAST WITH KRIPKE:
  Kripke: the same individual exists in multiple worlds
  (trans-world identity). Names are rigid designators
  across worlds for the SAME individual.
  Lewis: no trans-world individuals. Counterparts instead.
  This matters for puzzle cases in modal metaphysics.
```

---

## Possible Worlds and Counterfactuals

```
  "If Kangaroos had no tails, they would topple over."

  LEWIS'S ANALYSIS (Counterfactuals, 1973):
  A counterfactual P □→ Q is true iff:
  The CLOSEST worlds where P is true are worlds where Q is also true.

  CLOSENESS = similarity to the actual world.
  The "closest" tailless-kangaroo worlds are those that differ
  minimally from the actual world — same physics, same biology,
  just tail-less kangaroos.
  In those closest worlds, kangaroos topple.
  → The counterfactual is TRUE.

  CONTRAST:
  "If kangaroos had no tails, they would have evolved different balance"
  requires worlds that differ more from actuality.
  Whether it is true depends on which worlds are "closer."

  SPHERES OF SIMILARITY:
  Each world w is surrounded by concentric spheres of similarity.
  Inner sphere: closest worlds.
  P □→ Q: in the innermost P-world sphere, Q holds.

  CS APPLICATION:
  Counterfactual reasoning is fundamental to:
  - Causal inference (causation as counterfactual dependence)
  - Program verification: does this code change produce the desired effect?
  - Explaining AI decisions: "What would need to be different for X
    to get the loan?" (counterfactual explanation in ML)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is a rigid designator? | A name that refers to the same object in all possible worlds |
| Are proper names rigid? | Yes (Kripke): "Aristotle" picks out Aristotle in every world |
| What is semantic externalism? | Meaning is not in the head — it depends on the external world (Putnam) |
| What is a posteriori necessity? | A necessary truth discovered empirically: "Water is H₂O" |
| What is modal realism (Lewis)? | Possible worlds are real, concrete, existing entities — as real as ours |
| What is counterpart theory? | Modal statements about individuals are about their counterparts in other worlds |
| How do counterfactuals work semantically? | P □→ Q: Q is true in the closest possible worlds where P is true |

---

## Common Confusion Points

**"Possible world" ≠ "an alternate universe"**: In Kripke semantics, a possible world is a mathematical model — a set with a valuation. It has no metaphysical weight. In Lewis's modal realism, possible worlds are real. These are very different claims. Most philosophical and logical use of "possible worlds" is Kripke semantics (models), not Lewis (metaphysics).

**Rigid designators ≠ direct reference always**: Kripke says names are rigid. He does not say names have no descriptive content at all (that is the more radical "Millian" view: names are mere labels). Kripke is compatible with there being a reference-fixing description. The point is that once reference is fixed, the name RIGIDLY picks out that individual.

**A posteriori necessary ≠ analytic necessary**: "Water is H₂O" is necessary (water = H₂O in all worlds) but discovered empirically. "Bachelors are unmarried" is necessary AND analytic (true by definition/meaning). These come apart in Kripke's framework.

**Accessibility relation varies by modal logic**: S5 accessibility is an equivalence relation (everything is accessible from everything). S4 is transitive but not symmetric. T is only reflexive. These correspond to different interpretations of "possibility" — logical, epistemic, deontic, temporal. Confusing which modal logic you're using is the most common error.

**Counterpart theory is controversial even among modal realists**: Some accept Lewis's modal realism but reject counterpart theory, holding that individuals exist "transworld." The debate is about how to handle de re modal properties (modal properties of individuals) in a possible worlds framework.
