# 03 — Metaphysics

## Ontology, Causation, Time, Modality, Identity, Laws of Nature

---

## Big Picture: Metaphysics Landscape

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         METAPHYSICS                                      │
│          The philosophical study of the fundamental nature of reality    │
├──────────────────────┬───────────────────────────┬───────────────────────┤
│  ONTOLOGY            │  CAUSATION & EXPLANATION  │  MODALITY             │
│  (what exists)       │  (what explains what)     │  (necessary/possible) │
├──────────────────────┼───────────────────────────┼───────────────────────┤
│  Realism vs          │  Humean regularity        │  Possible worlds      │
│  anti-realism        │  Counterfactual (Lewis)   │  De re vs de dicto    │
│  Universals vs       │  Causal powers            │  Essential properties │
│  nominalism          │  Interventionism (Pearl)  │  Mereology            │
│  Abstract entities   │  Probabilistic causation  │  Haecceity            │
│  Physical ontology   │  Laws of nature           │                       │
├──────────────────────┴───────────────────────────┴───────────────────────┤
│  IDENTITY AND PERSISTENCE              │  TIME                          │
│  Personal identity                     │  A-theory vs B-theory           │
│  Ship of Theseus                       │  Presentism vs eternalism       │
│  4D vs 3D persistence                  │  Time travel                   │
│  Vagueness and identity                │  Direction of time             │
└────────────────────────────────────────┴────────────────────────────────┘
```

---

## 1. Ontology — What Exists?

### The Categories of Being

```
FUNDAMENTAL METAPHYSICAL QUESTION: What is there?
Quine's criterion: the ontological commitments of a theory are the objects over which
  its first-order variables must range for the theory to be true
  "To be is to be the value of a bound variable"
  → Entity exists iff ∃x that is that entity in the theory's quantification

BASIC ONTOLOGICAL CATEGORIES:

  PARTICULARS: individual existing things
    Concrete particulars: physical objects, events, processes (located in space-time)
    Abstract particulars (tropes): instances of properties (redness-of-this-apple)

  UNIVERSALS: properties and relations shared by multiple particulars
    Realism about universals: universals genuinely exist independently
      Transcendent realism (Plato): forms exist in a separate realm
      Immanent realism (Aristotle): universals exist in their instances; no instances → no universal
    Nominalism: only particulars exist; universals are names we apply
      Predicate nominalism: "red" applies to multiple things; no red universal needed
      Class nominalism: red things = the class of red objects; class is the "universal"
      Trope nominalism: properties are particulars (tropes); resemblance relations explain commonality

  ABSTRACT OBJECTS: exist but are not in space-time; not causally efficacious
    Mathematical objects (numbers, sets, functions)
    Propositions, types, laws
    Platonic view: these exist mind-independently
    Anti-realist view: they're useful fictions, constructs, or mere abstraction
```

### Mathematical Platonism

```
THE QUESTION: Do numbers exist?
  Platonism: yes, in a mind-independent abstract realm
    Frege: numbers are logical objects; 2 = the class of all two-membered classes
    Gödel: we have mathematical intuition that "perceives" abstract objects
    Benacerraf: if numbers exist abstractly, how do we know about them?
      (causal theory of knowledge: knowledge requires causal contact → abstract objects
       can't be causally accessed → how can we know anything about them?)

  Formalism: mathematics is manipulation of formal symbols; no commitment to objects
    Hilbert: mathematics is a formal game; consistency is all that matters
    Objection: Gödel's theorems show formal systems can't capture all mathematical truth

  Structuralism: numbers are positions in structures; there is no single number 2
    Any structure isomorphic to the natural numbers is "the" natural numbers
    Avoids ontological commitment to particular numbers
    Shapiro, Resnik: mathematical structures are what's real

  Fictionalism: mathematical statements are false (there are no numbers)
    but mathematical "fiction" is useful for describing physical reality
    Field's "Science Without Numbers": physics can be reformulated without mathematics

  WHAT ENGINEERS/SCIENTISTS ASSUME: implicitly Platonist (numbers "are out there")
    but the question is genuinely open at the philosophical level
```

---

## 2. Causation

### Humean Regularity Theory

```
HUME'S ANALYSIS (1739):
  No necessary connection between cause and effect; just constant conjunction
  Causation = constant conjunction + contiguity in time/space + temporal priority
  "We may define a cause to be an object, followed by another, and where all the objects
   similar to the first are followed by objects similar to the second"

  PROBLEMS:
  Symmetry: pressure drop precedes storm AND storm precedes calm; both correlate
    Barometer reading correlates with storm; not causal
  Effect before cause?: in physics, some regularities are symmetric in time
  Overdetermination: two boulders simultaneously crush car; either would have sufficed;
    each regularist cause but neither "the" cause
  Pre-emption: one assassin shoots target; backup ready but not needed;
    backup regularist cause is satisfied (backup's condition → death-from-backup) but didn't cause
```

### Counterfactual Theory (David Lewis)

```
LEWIS (1973):
  C causes E iff (i) C and E both occur and (ii) in the closest possible world
  where C does not occur, E does not occur

  POSSIBLE WORLDS: Lewis's modal realism
    Possible worlds are concrete existing things (as real as actual world)
    "Actual world" = just the world we happen to inhabit; not privileged except indexically
    Similarity/closeness of worlds: measured by match of particular facts + laws
    This is controversial: most accept possible worlds as a useful fiction, not real

  HANDLING BAROMETER: in closest world where pressure doesn't drop, storm doesn't occur
    → Pressure drop causes storm (correct)
    In closest world where barometer reads high, storm may or may not occur
    (depends on why barometer reads high)
    → Barometer reading doesn't cause storm (correct)

  PROBLEMS:
  Pre-emption: Rock1 and Rock2 thrown; Rock1 hits window first; Rock2 would have hit if Rock1 missed
    Counterfactual: in world where Rock1 not thrown, Rock2 breaks window
    → Rock1 doesn't cause window breaking by Lewis's theory? (wrong)
    Lewis: elaborate "influence" theory to handle; increasingly complicated

  Transitivity: if A → B → C, does A cause C?
    "Short circuits" and causal chains: overdetermination through chains
```

### Interventionist Causation (Pearl/Woodward)

```
STRUCTURAL CAUSAL MODELS (SCM):
  Variables: X₁, ..., Xₙ (can be discrete or continuous)
  Structural equations: each Xᵢ = fᵢ(parents(Xᵢ), Uᵢ)
    where Uᵢ are exogenous disturbances
  DAG: directed edges from parents to children (structural, not associational)

DO-OPERATOR:
  do(X=x): intervention that sets X to x, ignoring its natural causes
  P(Y | do(X=x)): causal effect; NOT the same as P(Y | X=x) (observational)
  Difference: conditioning adjusts for background correlation; do-intervention cuts parents

  Example: smoking → tar → cancer; smoking → cancer (direct)
    P(cancer | do(smoking=yes)) ≠ P(cancer | smoking=yes) when confounded
    Backdoor criterion: block confounding paths to identify causal effect
    Front-door criterion: use mediator to identify effect despite unmeasured confounders

COUNTERFACTUALS IN SCMs:
  Y_x(u): "what would Y have been if X were set to x, for individual u with background U=u"
  Three-step: (1) Abduction — update distribution over U given observed facts
    (2) Action — intervene: do(X=x) [modify structural equations]
    (3) Prediction — compute Y in modified model

  Why this matters for ML: standard ML optimizes P(Y|X) (observational); fails under distribution shift
    Causal models are invariant to interventions; predict correctly under domain shifts
    OOD generalization: causal features are stable; spurious correlations are not

THREE RUNGS OF CAUSATION (Pearl's Ladder):
  Rung 1 — Association: P(Y|X) — what is? statistical correlation
  Rung 2 — Intervention: P(Y|do(X)) — what if? causal effect of forcing X
  Rung 3 — Counterfactual: P(Y_x | X=x', Y=y') — what if it had been? individual-level

  Standard ML = Rung 1 only; causal ML requires Rungs 2-3
```

---

## 3. Modality and Possible Worlds

### De Dicto vs De Re

```
DE DICTO (about words/propositions):
  □("The number of planets is 8") — necessarily, the proposition "planets = 8" is true
  This is FALSE — the number of planets is a contingent fact (could have been 7 or 9)
  The statement is about how things are described, not the thing itself

DE RE (about things themselves):
  □(8 is the number of planets) — 8 is necessarily the number of planets
  ALSO FALSE — still contingent fact (though the number 8 is necessarily 8)
  But: □(8 is greater than 7) — here, 8 necessarily has this property

  KRIPKE'S RIGID DESIGNATORS (1970, Naming and Necessity):
    A term is a rigid designator if it refers to the same object in all possible worlds
    Names are rigid designators: "Aristotle" refers to Aristotle in all worlds
    Descriptions are non-rigid: "The teacher of Alexander" — different person could have
      taught Alexander in other possible worlds

    "Water is H₂O": necessarily true (metaphysically), even though discovered empirically
      In no possible world is something water without being H₂O
      (Compare: discovered a posteriori but necessary once discovered)
    "Heat is molecular motion": same — metaphysically necessary, discovered empirically

    This undermines Frege's sense-reference distinction as a general theory of names
    And undermines logical positivism's identification of necessity with analyticity
```

### Essences and Essentialism

```
ESSENTIALISM: objects have some properties essentially (in all possible worlds where they exist)
  and others accidentally (might not have had them)

  Aristotelian: essential properties are those defining the natural kind
    Water: essentially H₂O; accidentally colorless (could be colored water in some sense)
    Human: essentially rational animal

  Modern: Kripkean essentialism
    Natural kinds: water, gold, tigers — essential properties given by microstructure
    Origin essentialism (Kripke): you are essentially the product of that particular sperm
      and egg — no possible world where you exist but originated differently

  ANTI-ESSENTIALISM: Quine
    Essentialism is modality de re; this presupposes individual essences
    Without rigid designators, "the same object in different possible worlds" is unclear
    Mathematical objects: OK for modality; physical objects: questionable
```

---

## 4. Time

### A-Theory vs B-Theory

```
A-THEORY (McTaggart's A-series):
  Properties: past, present, future — these flow; what is present now was future
  PRESENTISM: only the present exists; past and future are not real
  GROWING BLOCK: past and present exist; future does not (yet)
  A-theorists: time genuinely passes; the present is metaphysically special

B-THEORY (McTaggart's B-series):
  Relations: earlier-than, simultaneous-with, later-than — these are PERMANENT
  Block universe / eternalism: past, present, future all equally real
  No objective "now"; "now" is indexical (like "here")
  Relativity of simultaneity (special relativity): support for B-theory
    Two events simultaneously for one observer ≠ simultaneously for moving observer
    → There is no objective "present" across all of space → eternalism more natural

MCTAG GART'S PARADOX:
  (1) A-determination (pastness, presentness, futurity) is essential to time
  (2) A-properties involve contradictions: every event is past AND present AND future
  (3) The regress response (these hold at different times) just restates the problem
  Conclusion: time is unreal (McTaggart)
  Response: A-theorists: the regress is benign; the indexical analysis resolves it

DIRECTION OF TIME:
  Fundamental physics is (mostly) time-symmetric: equations work equally for t and -t
  Yet: thermodynamics has arrow of time (entropy increases)
  Initial condition: low-entropy Big Bang explains why entropy increases in our direction
  Albert's "Past Hypothesis": there is a matter of fact about which direction is future
    because of the initial low-entropy boundary condition
```

### Personal Identity and Persistence

```
PERSISTENCE QUESTION: What makes you the same person over time?

PSYCHOLOGICAL CONTINUITY (Locke, Parfit):
  Memory: you are the same person as the earlier person you remember being (Locke)
  Problems: memory gaps; false memories; transitive chains of memory
  Psychological continuity: overlapping chains of psychological connections
    (memories, beliefs, desires, intentions, character traits)
  Parfit's Reductionism: personal identity = further fact? No — just continuous psychology
    Identity is not what matters in survival; what matters is continuation of psychology

PHYSICAL CONTINUITY (animalism, van Inwagen):
  You are a biological organism; persistence = organism's persistence
  Brain transplant: you go with the brain (most say); animalist: the organism stays

NARRATIVE IDENTITY (Ricoeur, MacIntyre):
  Identity constituted by ongoing narrative we tell about ourselves
  Practical identity; relevant to moral and legal contexts

SHIP OF THESEUS:
  Replace planks one by one until none original; original ship?
    Continuity answer: yes (gradual replacement preserves identity)
  Reassemble original planks: which is "the" ship?
    "Original material" account: reassembled ship is original
  FOUR-DIMENSIONALISM handles this:
    Objects are four-dimensional worm through space-time; ship-stage at each time
    "Original ship" and "replacement ship" are overlapping or distinct worms depending on convention
```

---

## 4b. Mereology — Part-Whole Ontology

```
MEREOLOGY: the formal study of part-whole relations.
  Core relation: "x is part of y" (Pxy) — reflexive, antisymmetric, transitive.
  Classical Extensional Mereology (CEM) adds:
    Unrestricted Composition: for any objects, there exists an object
      that is their mereological sum. (Controversial: implies there is
      an object composed of your coffee cup + the Eiffel Tower.)
    Extensionality: objects with the same proper parts are identical.

PARTHOOD AXIOMS (Simons' classical formulation):
  P(x,x)                                  — Reflexivity
  P(x,y) ∧ P(y,x) → x=y                  — Antisymmetry
  P(x,y) ∧ P(y,z) → P(x,z)              — Transitivity
  ¬P(x,y) → ∃z[P(z,x) ∧ ¬O(z,y)]        — Strong Supplementation
  ∃x φ(x) → ∃y∀z[O(z,y) ↔ ∃x(φ(x)∧O(z,x))]  — Unrestricted Fusion

WHERE MEREOLOGY IS DISPUTED:
  Is the Ship of Theseus the same after part replacement? (identity over time)
  Is a lump of clay numerically identical to the statue it composes?
  Are there plural entities, or only mereological sums?

MEREOLOGY IN FORMAL METHODS AND KR:
  OWL / Description Logic: hasComponent, hasPart properties;
    mereological relations in biomedical ontologies (SNOMED, FMA).
    "Liver has-part hepatocyte" — the part-whole hierarchy is a
    distinct relation from subClassOf.
  Mereotopology (Casati & Varzi): extend mereology with topological
    primitives (connectedness, boundary). Used in spatial databases,
    geographic information systems (GIS), qualitative spatial reasoning.
  Region Connection Calculus (RCC8): eight mereotopological relations
    between spatial regions. Used in AI spatial reasoning systems.
  Software decomposition: "module X is part of subsystem Y" is
    mereological. The formal difficulty — whether wholes are just
    their parts or something more — parallels the architecture debate
    over emergent system properties that can't be reduced to components.
```

## 4c. Haecceity — Thisness and Individual Essence

```
HAECCEITY ("thisness" — from Latin haec, "this"):
  A haecceity is a non-qualitative property that makes an individual
  the particular individual it is — distinct from all qualitative
  properties (mass, color, position, history).
  "Being Barack Obama" is a haecceity; it is not shared by anyone else
  regardless of how qualitatively similar they might be.
  Haecceities are contrasted with suchness (qualitative properties).

THE PHILOSOPHICAL PROBLEM:
  Leibniz's Law (Identity of Indiscernibles): if x and y share all
    qualitative properties, then x = y.
  If this law holds: there are no haecceities — identity follows
    entirely from qualitative properties.
  But: in quantum mechanics, two electrons can be in states with
    absolutely identical qualitative properties (same position, spin,
    energy in a symmetric wavefunction). Are they identical or two?
    If two, their individuation must be non-qualitative — haecceities.
  This is why haecceitism matters in philosophy of physics:
    it is the metaphysical question of particle individuality.

HAECCEITISM IN POSSIBLE-WORLDS SEMANTICS:
  Haecceitist: whether an individual exists in a possible world is
    a primitive fact; qualitative description does not determine
    trans-world identity.
  Anti-haecceitist: trans-world identity is always determined by
    qualitative facts. No bare "thisness" — similarity and causal
    history fully ground cross-world identity.

CS CONNECTION (database identity):
  Primary keys vs. natural keys: a surrogate key (auto-increment ID,
    UUID) is a haecceity — it picks out the individual without
    reference to qualitative properties. A natural key (email address,
    SSN) is suchness — the individual is identified by properties.
  The philosophical problem of haecceitism maps directly onto the
    practical engineering question of entity identity.
  If two rows are qualitatively identical (same name, address, date of birth),
    are they the same person or two different people? The haecceitist
    says: only a non-qualitative ID resolves this. The anti-haecceitist
    says: any identical rows must be duplicates.
```

## 5. Laws of Nature

```
HUMEAN REGULARITY THEORY:
  Laws = true universal generalizations in the "best system" of axioms
  Best System Account (Lewis): laws = theorems of the deductive system that best balances
    simplicity and strength (informativeness) in describing the Humean mosaic
  No necessary connection; just actual pattern

NOMIC NECESSITY (Armstrong, Dretske, Tooley):
  Laws = necessary connections between universals
  N(F, G): it is a law that F-things are G-things; N is a second-order relation between universals
  Explains why laws support counterfactuals: if universals are necessarily connected,
    then even in counterfactual scenarios, the law holds

DISPOSITIONALISM (Bird, Ellis):
  Natural properties are essentially dispositional (have powers/dispositions)
  Fragility: essentially disposed to break under impact
  Laws = conceptual truths about what property-powers do
  No contingency about laws: given the properties, the laws couldn't be otherwise

STATISTICAL vs DETERMINISTIC LAWS:
  Deterministic: given initial conditions, outcome fixed (classical mechanics)
  Statistical: given initial conditions, probability distribution over outcomes (QM)
  Fundamental indeterminism: quantum mechanics suggests world is genuinely probabilistic
    (not just epistemic uncertainty about hidden variables — Bell's theorem rules out
     local hidden variables)
```

---

## Bridge — Metaphysics and System Design

```
METAPHYSICAL PROBLEM               SYSTEM DESIGN PARALLEL
─────────────────────────────────────────────────────────────────
Ship of Theseus / persistence:     Entity lifecycle modeling.
What makes an object the same      A customer record updated 1,000 times
object through change?             — is it the same customer? Which
                                   fields are essential (identity) vs.
                                   accidental (changeable without loss
                                   of identity)?
                                   Surrogate key: non-qualitative (like
                                   haecceity) — row is this row regardless
                                   of all property changes.
                                   Natural key: qualitative — identity
                                   constituted by values.
                                   Event sourcing: the entity IS its
                                   event history (four-dimensionalist;
                                   the entity is a sequence of stages).

Universals vs. particulars:        Class hierarchies / type systems.
Do abstract types exist, or only   "Animal" is a universal; "Rex the
individual instances?              dog" is a particular.
                                   Platonist reading: types exist
                                   independently of instances.
                                   Nominalist reading: types are
                                   constructs over instances; the
                                   instance is what's real.
                                   Trope theory: properties are
                                   individual — "Rex's brownness" is
                                   not the same as "Fido's brownness,"
                                   even if they look the same. Relevant
                                   to object equality semantics (value
                                   equality vs reference equality).

Modal logic / possible worlds:     Test and property verification.
Necessity: true in all possible    Assert: "this invariant holds in
worlds. Possibility: true in       ALL states the system can reach"
some.                              (necessity). Modal logic formalizes
                                   this. TLA+ uses □ (always) and
                                   ◇ (eventually) — temporal modal
                                   operators — as first-class operators
                                   for system specifications.

Mereology:                         Component / subsystem decomposition.
Part-whole relations; when does    Is the sum of components identical
a collection become a whole?       to the system? Emergent behavior
                                   (the system exhibits properties no
                                   component has alone) is the mereology
                                   question. Microservices: the system
                                   = sum of services? Or is the service
                                   mesh a distinct whole?

Causation (interventionist):       Debugging / root cause analysis.
Pearl's do-calculus: what would    "If I had changed X, would Y still
happen if we intervened on X?      have happened?" Interventionist
Counterfactual reasoning.          causation is exactly the mental
                                   model of debugging: hold everything
                                   constant; change one variable;
                                   observe effect. RCA (Root Cause
                                   Analysis) applies this framework.
```

## Decision Cheat Sheet

| Question | Main Positions | Current Lean |
|----------|---------------|--------------|
| Do numbers exist? | Platonism, formalism, structuralism, fictionalism | Structuralism or Platonism (no consensus) |
| Do universals exist? | Realism, nominalism, trope theory | Trope theory or moderate realism |
| What is causation? | Regularity (Hume), counterfactual (Lewis), interventionist (Pearl) | Interventionist for science/AI |
| Does time flow? | A-theory (yes), B-theory (no; block universe) | B-theory (supports SR) |
| What makes you you over time? | Psychological, physical, narrative continuity | Psychological continuity (dominant) |
| What are laws of nature? | Regularity, nomic necessity, dispositionalism | Debated; best systems for physics |

---

## Common Confusion Points

**Metaphysics is not speculation:** Contemporary analytic metaphysics uses rigorous arguments, thought experiments as testing devices, and formal tools (modal logic, mereology) to investigate these questions. It's not less rigorous than science — it has different methods appropriate to its domain.

**Possible worlds don't require ontological commitment:** Most philosophers use possible worlds talk as a useful fiction or metaphor for modality. Lewis was unusual in arguing they're as real as the actual world. You can use possible worlds semantics (it's just a formal framework) without buying into modal realism.

**Essentialism and natural kind terms:** Kripke's insight that "water" rigidly designates H₂O means that scientists, not philosophers, tell us what water essentially is. This is a point about how reference works for natural kind terms, not a claim about metaphysics alone — it has implications for the meaning of natural kind words.

**The B-theory doesn't deny that we experience time as flowing:** The B-theory says there's no objective "now" outside of individual perspective. Our experience of the present is a fact about where we are in the block universe — like the fact that "here" is where I am. The experience of time passing is real as experience; what the B-theorist denies is the metaphysical claim that one temporal position is objectively privileged.

**Causal models are not just statistics:** Pearl's interventionist framework is designed to capture causal structure that survives intervention — which purely statistical models don't. When you ask "would X still cause Y if we intervened?" you're asking a Rung-2 question. Standard ML answers only Rung-1 questions, which is why it fails under distribution shift caused by interventions.
