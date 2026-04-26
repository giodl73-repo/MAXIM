# 06 — Philosophy of Science

## Demarcation, Falsificationism, Kuhn, Lakatos, Underdetermination, Realism

---

## Big Picture: Philosophy of Science

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    PHILOSOPHY OF SCIENCE                                 │
├─────────────────────────────┬────────────────────────────────────────────┤
│  EPISTEMOLOGY OF SCIENCE    │  METAPHYSICS OF SCIENCE                   │
│  ──────────────────         │  ─────────────────────                    │
│  How does science justify?  │  What do scientific theories say exist?   │
│  Demarcation                │  Scientific realism vs instrumentalism    │
│  Confirmation               │  Laws of nature                           │
│  Underdetermination         │  Natural kinds                            │
│  Induction (Hume)           │  Causation and explanation                │
│  Theory change              │  Reductionism                             │
├─────────────────────────────┴────────────────────────────────────────────┤
│  SCIENTIFIC RATIONALITY                                                  │
│  Kuhn's paradigm shifts, Lakatos's research programs,                    │
│  Feyerabend's anarchism, Bayesian confirmation, inference to best expl.  │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 1. The Demarcation Problem

### What Distinguishes Science from Non-Science?

```
WHY IT MATTERS:
  Practical: funding, policy, expert testimony, teaching in schools
  Epistemic: trusting scientific authority requires knowing what counts as science
  Legal: Daubert standard (US courts): is expert scientific testimony based on valid science?
    Frye standard (older): accepted by relevant scientific community
    Daubert factors: tested/testable? Peer reviewed? Error rate? Accepted by community?

LOGICAL POSITIVISM / VERIFICATIONISM (Vienna Circle, 1920s-30s):
  Meaningful claims are either:
    (1) Analytic: true by definition/logic (mathematics, logic)
    (2) Empirically verifiable: can be tested against observation
  Non-verifiable claims: metaphysics, theology, aesthetics (allegedly meaningless, not just false)
  Science: verifiable claims about the world
  Hume's fork: relations of ideas / matters of fact — precursor to same distinction

  PROBLEMS:
  Universal statements ("All copper conducts electricity") are not directly verifiable
    (can only observe finite instances; never exhaustively test)
  The principle of verifiability is itself neither analytic nor empirically verifiable →
    self-defeating by its own criterion
  Theoretical terms: electrons, quarks, fields — not directly observable; how to verify?
```

### Popper's Falsificationism

```
KARL POPPER (1934, Logic of Scientific Discovery):
  DEMARCATION: science = falsifiable claims; pseudo-science = unfalsifiable

  KEY INSIGHT — asymmetry of verification/falsification:
    Cannot verify "All ravens are black" (finite observations; always more ravens to check)
    CAN falsify "All ravens are black" (find one non-black raven)
    Science proceeds by bold conjectures + attempts to refute them
    When refuted: discard and try again; never proven, only corroborated

  UNFALSIFIABLE PSEUDOSCIENCE EXAMPLES:
    Freudianism: any behavior can be explained post-hoc by psychoanalytic theory
      → no observation could falsify it
    Marxist historical theory (in some formulations): history will inevitably lead to communism;
      apparent failures reinterpreted as necessary steps
    Astrology: predictions vague enough to "confirm" any outcome

  GOOD SCIENCE:
    Specific, testable predictions; clear conditions of refutation
    Einsteinian relativity: predicts light bending; specific angle; testable 1919 eclipse
    Darwin's evolution: predicts fossil record continuity; Cambrian explosion is anomaly to explain
    Quantum mechanics: specific probability predictions; tested to 12 decimal places

  PROBLEMS WITH FALSIFICATIONISM:
  Duhem-Quine thesis: a theory is never tested alone; always tested with auxiliary hypotheses
    If observation contradicts prediction: theory, OR any of the auxiliary hypotheses could be wrong
    "Any theory can be saved from refutation by suitable modification of auxiliaries"
    → Falsification is never simple; which hypothesis to reject requires judgment

  Ad hoc modifications: scientists routinely modify theories to avoid falsification
    Is this always irrational? No — sometimes a minor patch is right
    Lakatos: some ad hoc modifications are progressive; others are degenerative (see §2)

  Tacking: a theory T is falsifiable; T ∧ "moon is made of cheese" is also falsifiable
    → Falsifiability not sufficient for demarcation
```

---

## 2. Scientific Change: Kuhn and Lakatos

### Kuhn's Paradigm Shifts

```
THOMAS KUHN (The Structure of Scientific Revolutions, 1962):
  Most influential philosophy of science work of 20th century; changed how science is discussed

PARADIGM: an exemplary achievement that defines the field; framework of assumptions,
  methods, problems, and standards for a scientific community
  Normal science: puzzle-solving within the paradigm; doesn't question fundamental assumptions
  Not just a theory: includes instruments, exemplars, values, metaphysical commitments

STAGES OF SCIENTIFIC DEVELOPMENT:
  Pre-paradigm science: multiple competing schools; no consensus framework
  Normal science: Big paradigm in place; fill in the details; refine the theory
    Puzzles: problems you try to solve within the paradigm
    Anomalies: observations that don't fit; normal science tries to explain them away
  Crisis: accumulation of anomalies that paradigm cannot handle; normal science fails
    Extraordinary science: fundamental assumptions questioned; competing alternatives appear
  Revolution: paradigm shift to new paradigm; old paradigm abandoned

INCOMMENSURABILITY:
  Old and new paradigms cannot be directly compared in a common neutral vocabulary
  Different problems, different standards, different meanings of key terms
  Newton's "mass" and Einstein's "mass" are not the same concept
  Rational reconstruction post-hoc: we tell stories about why new paradigm is "better,"
    but this is not the logic that drove the actual change
  Kuhn: paradigm choice is partly non-rational (gestalt switch; social factors)

EXAMPLES:
  Ptolemaic → Copernican → Newtonian → Einsteinian astronomy
  Phlogiston → Lavoisier's oxygen-based combustion
  Newtonian → quantum/relativistic mechanics
  Plate tectonics revolution (1960s): previously "obvious" constraints (continents don't move)
    overturned; geologists' entire research program reorganized

CRITICISMS:
  Irrationalism: if paradigm choice is not fully rational, science is just "mob psychology"
    Kuhn's response: there are values that persist across paradigm changes (accuracy, consistency,
      breadth, simplicity, fruitfulness); just insufficient to uniquely determine choice
  What is a paradigm?: Kuhn identified 21 different senses; concept vague
  Progress: Kuhn later acknowledged scientific progress exists, even across paradigms
```

### Lakatos's Research Programs

```
IMRE LAKATOS: scientific methodology of research programs; reconciles Popper with Kuhn

RESEARCH PROGRAM: series of theories evolving over time, sharing:
  Hard core: central assumptions protected from refutation by convention
    Newtonian mechanics: F=ma is not directly falsified by any anomaly
  Protective belt: auxiliary hypotheses that absorb anomalies; can be modified
  Negative heuristic: don't attack the hard core
  Positive heuristic: directions for extending and developing the theory

PROGRESSIVE vs DEGENERATIVE:
  Progressive: program makes novel predictions that are later confirmed
    Einstein's relativity → predicted gravitational lensing (confirmed 1919)
    Newtonian mechanics + perturbation theory → predicted Neptune's position (confirmed)
  Degenerative: program only explains anomalies post-hoc; no novel predictions
    Modifying theory AFTER the fact to explain known data → not progress

COMPARISON WITH KUHN:
  Lakatos: scientists are rational in protecting core; rationality survives paradigm change
  Kuhn: incommensurability; social factors in paradigm choice
  Lakatos: progress = scientific methodology over time tracks problem-solving; not individual decisions
  Both: reject simple falsificationism; understand science as complex social enterprise

COMPARISON WITH POPPER:
  Popper: falsification is immediate; one negative result should refute
  Lakatos: scientists are right to hold onto research programs; immediate abandonment is not rational
  "Sophisticated falsificationism": whole programs are tested over time; not individual theories
```

### Feyerabend's Anarchism

```
PAUL FEYERABEND (Against Method, 1975):
  There is no scientific method; methodology changes with science; constraints on science
  slow it down
  "Anything goes": successful scientists have violated every methodological rule
  Galileo: used rhetoric, aesthetic arguments, non-standard methods to defeat Ptolemy
  Proliferation of theories: more theories competing → more scientific progress
  Critique of rationality of demarcation: no principled reason to privilege science
    over indigenous knowledge, astrology, witchcraft in all contexts

  MOST EXTREME POSITION: scientific knowledge is not epistemically privileged
    Science is one "tradition" among others; state should not enforce scientific worldview

  INFLUENCE:
    Sociologists of scientific knowledge (Bloor, Barnes): social factors fully explain
      scientific belief (not just discovery but justification)
    Science studies / feminist epistemology: standpoint, social values in science
    Mainstream philosophy: rejects strong Feyerabendian relativism; accepts that
      values and context affect science WITHOUT concluding science is non-rational
```

---

## 3. Scientific Realism vs Anti-Realism

### The Debate

```
SCIENTIFIC REALISM:
  Mature, successful scientific theories are approximately true descriptions of the world
  Theoretical entities (electrons, quarks, spacetime) really exist
  Success of science best explained by approximate truth of theories

  NO MIRACLES ARGUMENT (Putnam):
    If mature scientific theories were not approximately true, the success of science
    would be a miracle — incredibly unlikely
    → Best explanation of scientific success = approximate truth

ANTI-REALISM:
  Instrumentalism: theories are tools for prediction; no claim about hidden reality
    "All we can assert is predictive success; 'electrons exist' is not verifiable"
    van Fraassen's constructive empiricism: science aims to be empirically adequate
      (true about what is observable); agnostic about theoretical entities
    If theory saves the phenomena (correctly predicts observations): good enough

  Conventionalism: theoretical choices are conventions; not truth-apt at level of structure
  Social constructivism: scientific facts are socially constructed (strong version — extreme)

PESSIMISTIC META-INDUCTION (anti-realist):
  History of science: many successful theories later turned out false/abandoned
    Phlogiston: explained combustion well; doesn't exist
    Ether: explained wave propagation; doesn't exist
    Caloric fluid, vital force, luminiferous ether
  If past successful theories were false → current successful theories probably also false
  → Should not be realists about current theoretical entities

REALIST RESPONSES:
  Structural realism (Worrall): structures (mathematical relations) are preserved through
    revolutions; not specific theoretical entities
    Fresnel → Maxwell: specific ether structures abandoned; mathematical relations preserved
    "What is retained is the mathematical framework, not its physical interpretation"
  Entity realism (Hacking): we should be realists about entities we can manipulate
    If you use electrons to do things (spray them, bend them), you're justified in believing they exist
    More confident about entities than theories that postulate them
```

---

## 4. Underdetermination

### Theory and Evidence

```
DUHEM-QUINE UNDERDETERMINATION:
  Any theory consistent with any evidence if you adjust auxiliary hypotheses sufficiently
  "No finite set of observations uniquely determines a theory"
  "Data underdetermines theory"

  Duhem (local): for any failed prediction, scientists have choices about which hypothesis to blame
  Quine (global): entire webs of belief face experience as a corporate body
    Any belief can be saved from refutation; logic and mathematics are revisable in principle
    (though they're at the center of the web; revision would be costly)

  CONSEQUENCE: Holism — beliefs never tested individually but in groups; cannot isolate
    a single hypothesis for testing

  REALIST RESPONSE: underdetermination is only logical; in practice, theoretical virtues
    (simplicity, unifying power, coherence, novel predictions) substantially narrow choices
    Scientists don't have genuinely equivalent alternatives most of the time

UNDERDETERMINATION AND ML MODELS:
  Multiple neural architectures can fit the same training data equally well
  Different inductive biases lead to different generalization behavior
  No training data tells you which to prefer; architectural choices are theoretical choices
  Regularization = imposing simplicity preference (like Ockham's razor in physics)
  Gradient descent implicitly biases toward certain solutions — an underspecified "auxiliary hypothesis"
```

---

## 5. Scientific Explanation

### Models of Explanation

```
DEDUCTIVE-NOMOLOGICAL (DN) MODEL (Hempel and Oppenheim):
  Scientific explanation = valid deductive argument from laws + initial conditions
  Explanandum: what is to be explained (event or regularity)
  Explanans: laws of nature + particular conditions
  Must be deductively valid: explanans entail explanandum

  EXAMPLE: Why did this iron rod expand?
    Law: all iron rods expand when heated
    Initial condition: this rod was heated
    Conclusion: this rod expanded

  PROBLEMS:
  Irrelevance: valid argument; not explanatory
    Height of flagpole + sun angle → shadow length (explains)
    Shadow length + sun angle → flagpole height (does not explain; reverse is non-explanatory)
    Both are valid DN explanations; criterion doesn't distinguish
  Asymmetry problem: explanation has direction; DN is symmetric in valid deduction
  Probability: many events explained by statistical laws; DN doesn't cover this

STATISTICAL EXPLANATION:
  Inductive-Statistical (IS): statistical laws + conditions → high probability outcome
    Smoking (90% lung cancer probability) + patient smoked → patient got lung cancer
    Only explains high-probability events; doesn't explain low-probability (why THIS patient?)

CAUSAL-MECHANICAL MODEL (Salmon):
  Explanation = showing how mechanisms produce the outcome
  Causal process: transmits mark; genuine causal chain
  Counterfactual: if cause hadn't occurred, effect wouldn't have
  More physically realistic; handles asymmetry (cause before effect)

UNIFICATION THEORY (Friedman, Kitcher):
  Science explains by reducing number of independent phenomena requiring separate explanation
  Gravity: unifies celestial mechanics + terrestrial falling + tides → one theory
  Good explanation: expands range of phenomena with fewer independent premises
  Problem: can unify by adding disjunctions; not all unification is explanatory

MECHANISTIC EXPLANATION (Machamer, Darden, Craver):
  Biology/neuroscience/cognitive science: explain by describing mechanisms
  Mechanism: entities and activities organized to produce phenomena
  Multi-level: same mechanism described at different levels; all levels are genuine explanations
  Reductionism: complete mechanistic explanation reaches lowest level? Debated in philosophy of biology
```

---

## 5b. Reductionism and the Unity of Science

```
THE REDUCTIONIST THESIS:
  All sciences reduce to physics. Chemistry reduces to quantum mechanics.
  Biology reduces to chemistry. Psychology reduces to neuroscience.
  Ultimately: one fundamental science; all others are applied physics.

OPPENHEIM AND PUTNAM (1958) — UNITY OF SCIENCE HIERARCHY:
  Social groups
  Individual organisms
  Cells
  Molecules
  Atoms
  Elementary particles
  Each level reduces to the level below.

ARGUMENTS FOR REDUCTIONISM:
  Historical success: chemistry was successfully reduced to quantum
    mechanics (chemical bonding = electron orbital overlap).
  Explanatory ideal: reduce to fundamental mechanisms; eliminate
    unexplained primitives. "Why does this material conduct?"
    → electron band structure → Pauli exclusion principle → QM.
  Ontological parsimony: one fundamental ontology rather than
    multiple irreducible levels.

ARGUMENTS AGAINST REDUCTIONISM (anti-reductionism):

  MULTIPLE REALIZABILITY (Putnam):
    Mental states, functional states, and high-level properties
    can be instantiated in multiple different physical substrates.
    "Pain" is realizable in neurons, silicon, or octopus neurons.
    If chemistry reduced entirely to QM, there would be no way to
    explain why the SAME chemical properties appear in many QM implementations.
    Higher-level properties are real because they pick out genuine
    invariants across substrate variation.

  EMERGENCE:
    Some properties of wholes genuinely cannot be predicted from
    the properties of parts alone — they are emergent.
    Weak emergence: in principle reducible but too computationally
      complex to derive in practice. (Most thermodynamics.)
    Strong emergence (contested): properties that are in principle
      irreducible. Consciousness is the usual candidate.
    Practical: consciousness, economic behavior, and ecosystem
    dynamics have not been reduced to physics. This may be
    epistemic limitation or genuine ontological irreducibility.

  CAUSAL AUTONOMY OF HIGHER LEVELS:
    Economic explanations work. "The company went bankrupt because
    it could not service its debt" is a good explanation that
    doesn't require a particle-physics account to be valid.
    Higher-level causal explanations are not eliminated by the
    existence of lower-level ones; they carve out different
    causal structures.
    Davidson's anomalous monism: mental events are physical events;
    but there are no strict psychophysical laws (the mental is
    anomalous). Reason-based explanation is not reducible to
    physical-causal explanation even if the events are identical.

INTER-LEVEL EXPLANATION IN SYSTEMS THINKING:
  Complex software systems exhibit the same structure:
    Network effects, emergent behaviors, performance under load,
    cascading failures — cannot be predicted purely from
    component specifications.
    "The service degrades above 10k req/s" is a system-level
    property not derivable from any single component's spec.
    Reductionist engineering tries to derive all system properties
    from components; systems engineering acknowledges that
    system-level properties require system-level models.
    This is the engineering instantiation of the reductionism debate.
```

## 5c. Natural Kinds

```
NATURAL KINDS: categories that "cut nature at its joints" (Plato's Phaedrus).
  A natural kind is a real category in the world, not a human convenience.
  Gold: all instances share an underlying nature (atomic number 79).
  Water: all instances are H₂O (Kripke/Putnam).
  Tiger: all members share an essence (species membership, genetic).

KRIPKE AND PUTNAM ON NATURAL KINDS (1972-1975):
  Traditional view (Frege/Russell): "water" is defined by description
    ("the colorless, drinkable liquid"). Meaning determines reference.
  Kripke: names are rigid designators — they pick out the same object
    in all possible worlds, not by description but by causal connection.
  Putnam: "water" refers to whatever shares the microstructural essence
    of what we called "water" when we introduced the term.
    In 1750, chemists didn't know water is H₂O. But "water" was already
    referring to H₂O — the reference was fixed by samples, not description.
    "Meaning ain't in the head": the extension of "water" is partly
    determined by the world (H₂O), not just by mental content.

THE ESSENCE STRUCTURE:
  Surface features: liquid, transparent, quenches thirst.
  Deep structure: H₂O (the microstructural essence).
  Scientific discovery: reveals the essence that was always there.
  Consequence: XYZ that looks exactly like water but is not H₂O is
    not water — even if every behavioral/functional criterion is met.
    (Putnam's "Twin Earth" thought experiment.)

CONTESTED NATURAL KINDS:
  Biological species: is "species" a natural kind?
    Multiple species concepts (biological, phylogenetic, ecological)
    suggest no unique answer. Kinds may be pragmatic relative to
    explanatory goals.
  Social categories: is "race" a natural kind? Most biologists: no
    (human genetic variation is clinal; racial categories don't track
    genomic clusters in any robust way). Social theorists: "race" is
    socially real even if not biologically natural.
  Mental states: is "depression" a natural kind? If so, it picks out
    a real mechanism. If not, it's a clinical convention that may
    obscure diverse underlying mechanisms.

RELEVANCE TO CLASSIFICATION SYSTEMS:
  Ontologies and taxonomies: are categories natural kinds (real)
    or conventions (useful fictions)?
  Medical ontologies (SNOMED, ICD): disease categories — natural kinds
    with real mechanisms, or pragmatic groupings for clinical convenience?
  ML classification: does a neural network learn natural kinds when it
    learns to classify objects? Or convenient clusters in input space?
    Naturalness of learned representations is an active research question.
  Data modeling: "customer," "order," "product" — are these natural kinds
    in the business domain or modeling conventions? The answer affects
    how the ontology should behave under domain evolution.
```

## 6. Quantum Mechanics — Interpretations

```
MEASUREMENT PROBLEM:
  Quantum state evolves by Schrödinger equation (deterministic, linear)
  Upon measurement: state "collapses" to definite value (indeterministic)
  Why collapse? What causes it? When does it happen?
  → No purely physical answer within QM formalism itself

COPENHAGEN INTERPRETATION (Bohr/Heisenberg):
  Wave function: mathematical tool for predicting measurement outcomes; not physical reality
  Collapse: occurs upon measurement (interaction with classical apparatus)
  "There is no quantum world. There is only quantum description." (Bohr)
  Complementarity: wave and particle aspects are complementary; not simultaneously definable
  Anti-realist: don't ask what's "really happening" between measurements
  Status: still dominant in physics practice ("shut up and calculate")

MANY-WORLDS INTERPRETATION (Everett 1957):
  Wave function always evolves by Schrödinger equation; no collapse
  Measurement: the universe branches; all outcomes realized in different branches
  Preferred by many physicists and philosophers (Deutsch, Carroll, Wallace)
  No special role for "observation" or "consciousness"
  Problems: probability — how to derive Born rule from branching structure?
    Preferred basis: what determines the "branching" (decoherence approximately answers this)
    Ontological extravagance: infinitely many branches is a high cost

BOHMIAN MECHANICS (Pilot Wave Theory):
  Particles are real; guided by a "pilot wave" (the quantum potential)
  Deterministic: given initial positions, everything is determined
  Non-local: pilot wave is instantaneously affected by events anywhere
  Reproduces all QM predictions; but non-locality is uncomfortable (Bell's theorem)
  Not used in practice; proof that deterministic hidden-variable theory exists (contra EPR worry)

DECOHERENCE:
  Open quantum systems: entanglement with environment effectively destroys interference
  Explains "classical appearance" of macroscopic world without collapse postulate
  Does NOT solve measurement problem completely: decoherence explains no-interference;
    doesn't select which branch is "actual" (preferred basis selected approximately)
  Consistent with Many-Worlds; also with other interpretations

QBism (Quantum Bayesianism — Fuchs, Mermin):
  Wave function = agent's beliefs (degrees of credence) about measurement outcomes
  Collapse = Bayesian update; not physical process
  Fully subjective; quantum mechanics is a user's manual, not description of reality
  Copenhagen-like but explicitly Bayesian; avoids measurement problem by retreating from ontology
```

---

## Bridge — Philosophy of Science and Engineering Practice

Every senior engineer has lived through paradigm shifts and framework evolution. The philosophy of science provides a precise vocabulary for analyzing what you've experienced:

```
PHILOSOPHY OF SCIENCE              ENGINEERING / TECHNOLOGY PARALLEL
─────────────────────────────────────────────────────────────────
KUHN: PARADIGM SHIFTS
─────────────────────────────────────────────────────────────────
Normal science: puzzle-solving      Production engineering within a
within accepted framework.          stable stack. Optimizing, fixing
Anomalies accumulate that           bugs, adding features. Works
the paradigm cannot explain.        within the paradigm's terms.

Crisis: anomalies can no longer     The scaling/maintenance cliff:
be ignored; the paradigm is         existing architecture cannot absorb
strained. Multiple competing        the new requirements. Competing
approaches emerge. Nobody can       frameworks emerge. Debates about
agree on fundamentals.              "what we should migrate to."

Revolution: new paradigm replaces   Platform migration:
the old. Incommensurability:        mainframe → client-server (1980s)
the new paradigm's ontology         client-server → web (1995-2005)
is incompatible with the old's;     web → cloud + microservices (2010s)
you cannot fully evaluate the       cloud → AI-native (2020s)
new from within the old.            The old paradigm's vocabulary
                                    (batch jobs, two-tier apps, VMs)
                                    doesn't translate directly.
                                    "Containers aren't VMs" — this
                                    is incommensurability.

────────────────────────────────────────────────────────────────
LAKATOS: RESEARCH PROGRAMMES
────────────────────────────────────────────────────────────────
Hard core: protected assumptions    Core framework commitments:
that define the programme.          "We are building on Kubernetes."
  Never falsified directly;         "We use the actor model."
  protected by auxiliary            These assumptions are not revisited
  hypotheses.                       every sprint; they are protected.

Protective belt: auxiliary          Framework-level problem-solving:
hypotheses that absorb anomalies    When Kubernetes doesn't handle our
and protect the hard core.          load pattern, we adjust the
  Modified when experiments fail;   deployment configuration (auxiliary
  hard core unchanged.              hypothesis), not the platform choice.

Progressive programme:              Healthy framework:
Predicts novel facts before         Framework is gaining ground, solving
they are observed.                  new problems, attracting talent,
Expanding empirical content.        generating useful abstractions.
                                    Kubernetes: extended from containers
                                    to serverless, ML workflows, edge.

Degenerative programme:             Dying framework:
Explains anomalies post-hoc;        Framework is sustained by heroic
no novel predictions.               auxiliary-hypothesis patching.
Losing ground to competitors.       "Yes, but you just need to configure
Hard to distinguish from            it correctly." The docs are longer
progressive from the inside.        than the code they're trying to
                                    explain. New projects don't choose it.

────────────────────────────────────────────────────────────────
POPPER: FALSIFICATIONISM
────────────────────────────────────────────────────────────────
Scientific claim: bold, risky       Testable hypothesis in A/B testing:
predictions that could be           "This feature will increase 7-day
falsified by specific observations. retention by 3% in the treatment
                                    group." Falsifiable; specific;
                                    risky. A real scientific claim.

Unfalsifiable claim: no possible    "This change will improve the
observation could disprove it.      user experience." Non-falsifiable
Irrefutable but unscientific.       without operationalization.
                                    Product claims that survive any
                                    outcome are unfalsifiable.

Corroboration:                      Surviving rigorous tests:
A hypothesis is corroborated if     A/B tests, load tests, adversarial
it has survived many severe tests.  testing. The hypothesis that survived
Not "confirmed" — still            hardest scrutiny is most trustworthy;
tentative.                          not "proven."

────────────────────────────────────────────────────────────────
SCIENTIFIC REALISM / INSTRUMENTALISM
────────────────────────────────────────────────────────────────
Scientific realism:                 Model realism:
Theoretical entities (electrons)    The ML model's internal
really exist; theories describe     representations correspond to
the world approximately correctly.  real structure in the domain.
                                    "The model has learned a concept
                                    of 'edge' in layer 3." This is a
                                    realist reading.

Instrumentalism:                    Model instrumentalism:
Theories are tools for prediction;  "The model works" is all that
whether they describe reality is    matters. Whether it "understands"
a meaningless question.             anything is a category error.
                                    The realist/instrumentalist debate
                                    about science is also the debate
                                    about AI interpretability.

Duhem-Quine underdetermination:     Multiple consistent architectures:
Same data fits many theories;       Multiple model architectures can
theory choice requires extra-       achieve the same benchmark scores.
empirical virtues (simplicity,      Architecture choice requires
scope, coherence with background    extra-empirical criteria: compute
theory).                            efficiency, interpretability,
                                    engineering simplicity.
                                    "The data underdetermine the model"
                                    is exactly the Duhem-Quine thesis
                                    applied to ML.
```

## Decision Cheat Sheet

| Topic | Key Positions | Current Status |
|-------|--------------|----------------|
| Demarcation | Verificationism (defeated), Falsificationism (partial), pragmatic criteria | No clean criterion; Kuhnian/Lakatosian |
| Scientific change | Popper (falsification), Kuhn (paradigms), Lakatos (programs) | Lakatos most influential for practicing scientists |
| Scientific realism | Realism, instrumentalism, constructive empiricism, structural realism | Structural realism vs constructive empiricism |
| Explanation | DN model (refuted), causal-mechanical, unification, mechanistic | Causal-mechanistic + unification |
| QM interpretation | Copenhagen, Many-Worlds, Bohmian, QBism | Many-Worlds gaining ground; Copenhagen dominant in practice |
| Underdetermination | Duhem-Quine: always some; in practice, constrained by theoretical virtues | Moderate underdetermination (not global) |

---

## Common Confusion Points

**Falsificationism doesn't mean you discard on first anomaly:** Real scientific practice doesn't and shouldn't. Lakatos showed that protecting a research program's core from anomalies is rational as long as the program is progressive. The question is whether modifications are ad hoc or generate novel predictions. Kuhn showed that anomaly accumulation drives crises, not individual refutations.

**Underdetermination doesn't make science arbitrary:** Logical underdetermination is true — data doesn't uniquely determine theory. But practical underdetermination is much less severe. Scientists' theoretical virtues (simplicity, coherence, predictive power, unification) substantially constrain theory choice. The space of equally well-supported alternatives is usually tiny, not infinite.

**Kuhn did not claim science is irrational:** He described the social and psychological dimensions of scientific change accurately. He acknowledged that theoretical virtues persist across paradigm changes. His claim about incommensurability is contested but does not entail irrationalism — different paradigms can be compared even if there's no neutral translation.

**Copenhagen is not the same as saying "QM is just math":** Copenhagen says the wave function is a predictive tool, not a description of physical reality. This is an interpretive stance (anti-realist), not a refusal to interpret. Many working physicists use Copenhagen because it lets them calculate without committing to ontology — pragmatic, not confused.

**Structural realism vs full realism:** You don't have to choose between "theoretical entities definitely exist" and "science is purely instrumental." Structural realism offers a middle path: what's preserved across theory change is mathematical structure; specific physical interpretation may change, but the relations are approximately correct.

**The no-miracles argument cuts both ways:** Realists say: scientific success would be miraculous without approximate truth. Anti-realists say: the no-miracles argument is circular (uses an inference-to-best-explanation to validate science's own inference-to-best-explanation). The argument's probative force depends on your background epistemology.
