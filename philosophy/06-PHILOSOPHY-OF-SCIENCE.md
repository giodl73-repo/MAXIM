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
│  Kuhn's paradigm shifts, Lakatos's research programs,                   │
│  Feyerabend's anarchism, Bayesian confirmation, inference to best expl. │
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

<!-- @editor[content/P2]: Reductionism listed in landscape diagram (Metaphysics of Science) but not covered — relevant debate about whether all science reduces to physics; inter-level explanation matters for this learner's systems-thinking background -->
<!-- @editor[content/P2]: Natural kinds listed in landscape diagram but absent — connects to Kripke (covered in 03-METAPHYSICS) and classification in biology/chemistry; deserves a brief subsection or cross-reference -->
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

<!-- @editor[bridge/P1]: Missing old-world → new-world bridge section — natural parallel: Kuhn's paradigm shifts → platform migrations (mainframe→client-server→web→cloud→AI); Lakatos's progressive vs degenerative → healthy vs dying frameworks — any senior engineer has lived through paradigm shifts and would immediately connect -->
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
