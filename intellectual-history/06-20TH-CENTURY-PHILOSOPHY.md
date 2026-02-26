# 20th Century Philosophy and Science

## The Big Picture

The 20th century saw a deep split in Western philosophy between analytic and continental
traditions, while philosophy of science became its own discipline. The Vienna Circle tried
to make philosophy scientific; Heidegger and the phenomenologists went in the opposite
direction. By mid-century, both traditions were wrestling with the limits of their own
methods.

```
+-------------------------------------------------------------------+
|              20TH CENTURY PHILOSOPHY LANDSCAPE                    |
|                                                                   |
|  ANALYTIC TRADITION           CONTINENTAL TRADITION               |
|  +---------------------+      +---------------------------+       |
|  | Vienna Circle:      |      | Phenomenology:            |       |
|  | logical positivism  |      | Husserl, Heidegger,       |       |
|  | (Schlick, Carnap,   |      | Merleau-Ponty, Sartre     |       |
|  | Neurath, Ayer)      |      |                           |       |
|  |                     |      | Existentialism:           |       |
|  | Cambridge:          |      | Heidegger, Sartre,        |       |
|  | Russell, Moore,     |      | Camus, de Beauvoir        |       |
|  | early Wittgenstein  |      |                           |       |
|  |                     |      | Frankfurt School:         |       |
|  | Oxford:             |      | Horkheimer, Adorno,       |       |
|  | late Wittgenstein,  |      | Marcuse, Habermas         |       |
|  | Austin, Ryle, Ayer  |      |                           |       |
|  |                     |      | Hermeneutics:             |       |
|  | Late 20th century:  |      | Gadamer, Ricoeur          |       |
|  | Quine, Rawls,       |      |                           |       |
|  | Kripke, Chalmers    |      |                           |       |
|  +---------------------+      +---------------------------+       |
|                                                                   |
|  PHILOSOPHY OF SCIENCE                                            |
|  +-----------------------------------------------------------+    |
|  | Logical empiricism -> Popper -> Kuhn -> Lakatos ->        |    |
|  | Feyerabend -> Laudan -> Scientific realism debate         |    |
|  +-----------------------------------------------------------+    |
+-------------------------------------------------------------------+
```

---

## The Vienna Circle and Logical Positivism

```
  VIENNA CIRCLE (1920s-1930s):
  Moritz Schlick, Rudolf Carnap, Otto Neurath, Herbert Feigl.
  Friedrich Waismann. Affiliated: A.J. Ayer, Carl Hempel.

  CORE THESES:

  VERIFICATION PRINCIPLE:
  A statement is meaningful iff it is either:
  (a) Analytically true (true by definition: "bachelors are unmarried")
  (b) Empirically verifiable (in principle testable by observation)

  Everything else = metaphysical pseudo-statement = meaningless.

  TARGETS:
  Traditional metaphysics ("What is Being?")
  Ethics as non-cognitive (emotivist theory: "Murder is wrong" = "Boo murder!")
  Theology

  PROGRAMME:
  Unified science (Neurath): all sciences reducible to physics (physicalism).
  Formal logic (Carnap): philosophy becomes the logic of science.
  Protocol sentences: observation reports as foundations.

  FATE:
  Vienna Circle dispersed by Nazism: members fled to US and UK.
  Logical positivism dominated Anglo-American philosophy of science 1930s-50s.
  Then collapsed under internal and external pressure.
```

## Engineering Bridge: Verification, Type Systems, and Decidability

The Vienna Circle's verification principle — "a statement is meaningful iff it is empirically verifiable or analytically true" — is the philosophical precursor to several foundational ideas in programming languages and formal methods. The MIT TCS background makes this immediate:

**Verification principle → static type checking.** A well-typed expression is one whose meaning can be verified at compile time without running it. The type checker is a mechanical verifier of a restricted class of semantic claims. Carnap's dream: turn all philosophy into the "logic of science." Type theory's achievement: turn a restricted class of semantic claims into decidable verification. The Curry-Howard correspondence makes this precise — propositions are types, proofs are programs, verification is type-checking.

**Meaningfulness → decidability.** "Meaningful iff verifiable" has an exact TCS counterpart: a property is decidable iff there is an algorithm that verifies it for all inputs. Undecidable properties (Rice's theorem: any non-trivial property of program behavior is undecidable) are, in a precise sense, "not fully verifiable" — you can check finite approximations but not the general claim. The Vienna Circle's problem (self-refutation of the verification principle) has a TCS mirror: the halting problem shows that the verifier cannot verify itself.

**Protocol sentences → formal specifications.** The logical positivists wanted "protocol sentences" — theory-neutral observation reports that serve as the foundation of knowledge. The engineering analogue is formal specifications (TLA+, Alloy, Z) and property-based tests: machine-checkable descriptions of what a system must do, serving as the ground truth against which implementations are verified.

**The collapse of logical positivism → type theory's response.** The problems that destroyed logical positivism (Quine's holism, theory-ladenness of observation, Duhem-Quine underdetermination) motivated the development of dependent type theory and proof assistants. Coq, Lean, Agda: if you cannot have theory-neutral observation, you can at least have machine-checked proof. The philosophical defeat generated the constructive mathematics response.

**Quine's holism → unit vs. integration testing.** "Statements don't face experience one at a time but as a corporate body" — no individual test isolates a single claim. Unit tests test individual components in isolation (requiring mocks, stubs: the epistemically problematic move of assuming the environment is neutral). Integration tests test the corporate body but lose the ability to isolate failures. This is Quine's holism as testing methodology.

### Problems with Logical Positivism

```
  1. THE VERIFICATION PRINCIPLE IS SELF-REFUTING:
     Is "a statement is meaningful iff verifiable" itself verifiable?
     It is neither analytic nor empirically testable. By its own criterion, meaningless.

  2. HOLISM (Quine, "Two Dogmas of Empiricism," 1951):
     The analytic/synthetic distinction is untenable.
     Statements don't face experience one at a time but as a corporate body.
     No individual statement is immune to revision in light of experience.
     Even logic could in principle be revised.

  3. THEORY-LADENNESS OF OBSERVATION (Hanson, Kuhn):
     Observation is not theory-neutral.
     Protocol sentences are not pure data points; they are already theoretical.

  4. UNDERDETERMINATION (Duhem-Quine):
     Evidence underdetermines theory choice.
     For any evidence set, infinitely many theories are consistent with it.

  5. PROBLEM OF INDUCTION (Hume, Popper):
     No finite observations entail any universal law.
     Verification by observation cannot establish general laws.
```

---

## Wittgenstein: Two Philosophies

### Early Wittgenstein (Tractatus, 1921)

```
  TRACTATUS LOGICO-PHILOSOPHICUS (1921):
  The world is the totality of facts (not things).
  Language pictures facts: atomic propositions correspond to atomic facts.
  The logical form of the picture mirrors the logical form of the fact.

  SHOWING VS. SAYING:
  Logic and the structure of language SHOW themselves but cannot be SAID.
  "Whereof one cannot speak, thereof one must be silent."
  Ethics, aesthetics, the "mystical" — these cannot be said, only shown.
  (This is NOT dismissal; it is placing them beyond language.)

  RECEPTION:
  Vienna Circle read Tractatus as supporting their program.
  Wittgenstein thought they missed the point: the mystical matters,
  it just can't be put into propositional language.
```

### Late Wittgenstein (Philosophical Investigations, 1953)

```
  PHILOSOPHICAL INVESTIGATIONS (published posthumously, 1953):
  Recantation of almost everything in the Tractatus.

  LANGUAGE GAMES:
  Language is not a single picture system but a diverse collection of practices.
  Words get meaning from their use in forms of life, not from correspondence.
  "Meaning is use."

  PRIVATE LANGUAGE ARGUMENT:
  Cannot have a purely private language (for inner experience).
  Language is essentially public and rule-governed.
  Criteria for correct rule-following must be inter-subjective.

  FAMILY RESEMBLANCE:
  Categories like "game" do not share a common essence.
  They share overlapping and criss-crossing similarities (family resemblances).
  Undermines essentialism in philosophy and linguistics.

  PHILOSOPHY AS THERAPY:
  Philosophy's job is to dissolve pseudo-problems (which arise from
  misunderstanding language), not solve them.
  "Philosophy leaves everything as it is."

  INFLUENCE: Ordinary language philosophy (Austin, Ryle, Oxford school),
  philosophy of mind, social science philosophy.
```

---

## Phenomenology

```
  HUSSERL (1859-1938): Founder.
  Phenomenology: description of the structures of consciousness and experience.
  "Return to the things themselves" — describe experience as it actually presents itself.

  INTENTIONALITY: Consciousness is always directed at an object.
  (Not: "I experience" but "I experience X".)

  REDUCTION (epoché): Bracket the question of whether objects really exist;
  just describe how they appear to consciousness.

  HEIDEGGER (1889-1976):
  Being and Time (1927): fundamental ontology — the question of Being.
  Dasein ("being-there"): human existence as Being-in-the-world.
  Thrownness, projection, falling, anxiety.
  Authenticity: owning one's own existence (vs. das Man — "they," the crowd).
  Technology as "enframing" (Gestell): reduces beings to "standing reserve."
  Language is "the house of Being."

  HEIDEGGER'S NAZISM:
  Heidegger joined the Nazi party in 1933; was Rector of Freiburg.
  The Black Notebooks (2014) show systematic anti-Semitism.
  The "Heidegger case" is a continuing controversy in continental philosophy:
  Can you separate his philosophy from his politics?
  (Faye: the philosophy is Nazi. Habermas: separate but related.)

  SARTRE (1905-1980):
  Existence precedes essence: there is no human nature prior to existence.
  We are "condemned to be free."
  Radical freedom and radical responsibility.
  Bad faith (mauvaise foi): denying one's freedom.
  Being and Nothingness (1943).

  SIMONE DE BEAUVOIR (1908-1986):
  The Second Sex (1949): women are "the Other" in a male-defined world.
  "One is not born, but rather becomes, a woman."
  Phenomenological feminism: gender is a situation, not an essence.
```

---

## Analytic Philosophy: The Main Line

### Russell and Frege

```
  FREGE (1848-1925):
  Begriffsschrift (1879): first modern logical notation.
  Sense and reference (Sinn und Bedeutung):
  "The morning star" and "the evening star" have same reference (Venus),
  different sense. Important for semantics and philosophy of language.

  RUSSELL (1872-1970):
  Theory of descriptions: "The current king of France is bald" —
  how can this be false, not just meaningless, if there is no current king?
  Answer: analyze as "There exists a unique x who is king of France and is bald."
  This eliminates apparent reference to non-existing objects.

  PRINCIPIA MATHEMATICA (1910-13, with Whitehead):
  Derive all of mathematics from logical axioms.
  Russell's paradox was the stimulus: the set of all sets that don't contain
  themselves leads to contradiction. Resolved by type theory.
```

### Quine and Naturalism

```
  WILLARD VAN ORMAN QUINE (1908-2000):
  "Two Dogmas of Empiricism" (1951): Demolished logical positivism's foundations.
  Two dogmas: (1) analytic/synthetic distinction, (2) reductionism.
  Web of belief: our beliefs face experience as a corporate body.
  Ontological relativity: there is no fact of the matter about what a theory
  is "really" about; only relative to a background theory.

  NATURALISM: Philosophy is continuous with science. No first philosophy.
  Epistemology is naturalized: a branch of empirical psychology.
  "Epistemology is concerned with the foundations of science. Conceived thus...
  epistemology falls into place as a chapter of psychology."

  INDETERMINACY OF TRANSLATION:
  Given all behavioral facts, there is no fact of the matter about the
  correct translation between languages. Radical translation is indeterminate.
  (Challenged by Chomsky and Davidson.)
```

### John Rawls and Political Philosophy

```
  RAWLS (A Theory of Justice, 1971):
  Revived normative political philosophy (which logical positivism had declared meaningless).

  ORIGINAL POSITION:
  Imagine choosing principles of justice from behind a "veil of ignorance":
  you don't know your social position, race, gender, natural talents, conception of good.

  PRINCIPLES OF JUSTICE:
  1. Equal basic liberties for all.
  2. Difference principle: inequalities permitted only if they benefit the
     least advantaged members of society.
     (Social and economic inequalities must be to the greatest benefit
     of the least fortunate.)

  INFLUENCE: Dominant framework in Anglo-American political philosophy.
  Challenged by: Nozick (libertarianism), communitarians (MacIntyre, Sandel,
  Walzer), Amartya Sen (capabilities approach), feminist critics.
```

---

## The Analytic-Continental Divide

```
  ANALYTIC                          CONTINENTAL
  ────────                          ────────────
  Clarity, rigor, formal precision  Historical, hermeneutic, phenomenological
  Logic as tool                     Language as constitutive
  Problems: truth, reference,       Problems: existence, power, embodiment,
  knowledge, mind                   meaning, suffering, death
  Science as model                  Critique of science's pretensions
  Narrow specialization             Broad "total" philosophy
  Argument: deductive               Argument: interpretive, dialectical
  British, American (mainly)        German, French (mainly)

  Origins of split:
  Frege, Russell vs. Husserl (different responses to the same crisis in math)
  Wittgenstein's Tractatus: both read it; read it differently.

  NOTABLE CROSSINGS:
  Merleau-Ponty influenced cognitive science and philosophy of mind.
  Habermas drew on both Hegel/Marx AND analytic philosophy.
  Brandom, McDowell: analytic philosophy of mind meets Hegel.
  Chalmers, philosophers of mind: draw on both.
```

---

## Philosophy of Mind

```
  MIND-BODY PROBLEM (20th century framing):
  SUBSTANCE DUALISM (Descartes): mind and body are separate substances.
  Abandoned by most: how do they interact?

  IDENTITY THEORY (Place, Smart, 1950s-60s):
  Mental states = brain states. Pain = C-fiber firing.
  PROBLEM: Multiple realizability (Putnam). Robots might have pain.
  Pain cannot be identical to C-fiber firing if something else can also realize pain.

  FUNCTIONALISM (Putnam 1960s):
  Mental states are defined by functional roles (input-output relations),
  not physical substrate. Implementable in neurons, silicon, etc.
  The dominant view in cognitive science and AI.

```
  ENGINEERING BRIDGE: Functionalism IS interface-based programming.

  Putnam's claim: mental state M is whatever plays the causal role of M
  (receives inputs of type X, produces outputs of type Y, transitions
  to state Z). Substrate (neurons, silicon) is irrelevant.

  Interface contract: IPaymentProcessor.charge(amount, currency) → Receipt
  is whatever plays the causal role defined by the interface. The
  implementation (Stripe, PayPal, in-memory mock) is irrelevant to
  any consumer that depends on the interface.

  Multiple realizability -> Dependency injection:
  "Pain can be realized in neurons OR silicon" is exactly "ILogger
  can be realized by ConsoleLogger OR FileLogger OR CloudLogger."
  The container injects the concrete realization at runtime; the
  dependent code never knows the substrate.

  The "hard problem" for software:
  Chalmers's hard problem (why is there SOMETHING IT IS LIKE to be
  in state M?) has no engineering analogue — because software systems
  are defined entirely by their functional behavior. This is why
  functionalism is complete as a theory of software in a way it may
  not be as a theory of mind.

  Substrate independence -> Portability:
  The same program runs on x86, ARM, RISC-V — multiple realizability
  is the formal basis of the ISA abstraction layer. The program is
  defined by its functional behavior, not by the transistors.
```

  HARD PROBLEM (Chalmers, 1995):
  Even if we explain all the functional and behavioral aspects of mind
  (the "easy problems"), we have not explained WHY there is subjective experience.
  Why is there "something it is like" to see red?
  Zombie argument: a physically identical being with no inner experience
  is conceivable; therefore physical facts don't determine phenomenal facts.

  ELIMINATIVISM (Churchland):
  Folk psychology (beliefs, desires) is a false theory.
  Future neuroscience will replace, not reduce, mentalistic vocabulary.
```

---

## Decision Cheat Sheet

| I want to understand... | Go to |
|---|---|
| What logical positivism claimed | Vienna Circle section |
| Why logical positivism failed | Problems section |
| Wittgenstein's two philosophies | Early (picture theory) vs. late (language games) |
| Phenomenology and Heidegger | Phenomenology section |
| Analytic vs. continental split | Divide section |
| Rawls and political philosophy | Rawls section |
| Mind-body problem and functionalism | Philosophy of mind section |

---

## Common Confusion Points

**Analytic does not mean "clear" and continental does not mean "obscure."**
The division is methodological and historical. Hegel is in the continental tradition but
extremely difficult. Analytic philosophers can be obscure too (early Carnap). The stereotypes
are real tendencies, not absolute differences.

**Wittgenstein is not one philosopher.**
Tractatus Wittgenstein and Investigations Wittgenstein are almost opposed. The Vienna Circle
used the Tractatus; Wittgenstein himself repudiated logical positivism. Many analytic
philosophers were embarrassed by the Investigations.

**"Phenomenology" has different meanings.**
Husserl's technical phenomenology (reduction, intentionality, essences) is very different
from Heidegger's phenomenology (Being-in-the-world, Dasein). Sartre used Husserl's method
with Heideggerian themes. The word is used loosely in cognitive science to mean "subjective
experience."

**Rawls is not the same as utilitarianism.**
Rawls explicitly argues against utilitarian principles of justice. Utilitarianism allows
sacrificing individuals for the aggregate. Rawls's difference principle protects the worst-off
regardless of aggregate improvement. They are rival theories.
