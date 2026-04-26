# 02 — Epistemology

## Knowledge, Justification, Gettier, Reliabilism, Bayesian Epistemology

---

## Big Picture: Epistemology Landscape

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         EPISTEMOLOGY                                     │
│                    Theory of knowledge and justified belief              │
│                                                                          │
│   Individual ←──────────────────────────────────────────→ Social         │
│                                                                          │
├────────────────────────────────┬─────────────────────────────────────────┤
│  INDIVIDUAL EPISTEMOLOGY       │  SOCIAL EPISTEMOLOGY                    │
│  ──────────────────────        │  ────────────────────                   │
│  What is knowledge?            │  Testimony and trust                    │
│  Traditional JTB analysis      │  Expert disagreement                   │
│  Gettier problem               │  Scientific consensus                  │
│  Internalism vs externalism    │  Epistemic injustice                   │
│  Rationalism vs empiricism     │  Peer disagreement                     │
│  Foundationalism vs coherentism│                                         │
│         │                      │          │                              │
│         │ (formalization)      │          │ (formalization)              │
│         ↓                      │          ↓                              │
├────────────────────────────────┼─────────────────────────────────────────┤
│  FORMAL EPISTEMOLOGY           │  NATURALIZED EPISTEMOLOGY               │
│  ─────────────────────         │  ──────────────────────                 │
│  Bayesian probability theory   │  Quine: epistemology as science         │
│  Epistemic logic               │  Cognitive science of knowledge         │
│  Formal learning theory        │  Evolutionary debunking                 │
│  Formal theories of belief rev │  Reliabilism                            │
│                                │                                         │
│   Formal ←──────────────────── ┼ ───────────────────────→ Naturalized    │
└────────────────────────────────┴─────────────────────────────────────────┘

Quadrant dynamics:
  Individual → Social:  move from first-person "what do I know?" to
    third-person "how do communities form and transmit knowledge?"
  Individual → Formal:  formalize justification conditions; use
    probability/modal logic to model credences and belief revision.
  Social → Naturalized: scientific consensus, peer trust, and
    institutional knowledge become empirical objects of study.
  Formal → Naturalized: Bayesian epistemology meets cognitive science
    (are humans actually Bayesian?); reliabilism as bridge concept
    (justification = produced by a reliable process).
```

---

## 1. The Traditional Analysis of Knowledge

### Justified True Belief (JTB)

```
PLATO'S MENO/THEAETETUS: Knowledge = justified true belief
  Three conditions necessary AND sufficient:
  (1) TRUTH: S knows that p only if p is true (you can't know false things)
  (2) BELIEF: S knows that p only if S believes that p (you can't know what you don't believe)
  (3) JUSTIFICATION: S knows that p only if S is justified in believing that p
      (distinguishes knowledge from mere lucky true belief)

WHY EACH CONDITION IS NECESSARY:
  Truth: "I knew the car was parked there" but it was towed = you didn't know, you believed
  Belief: knowing something you don't believe? Strange; most require belief
  Justification: stopped clock shows right time; true belief but not knowledge
    Correct answer on exam by pure guessing: true belief but not knowledge
```

### Gettier's Refutation (1963)

```
Edmund Gettier (1963, 3-page paper): JTB is not sufficient for knowledge

GETTIER CASE 1:
  Smith has good evidence that Jones will get the job (employer said so; Jones has 10 coins)
  Smith forms justified belief: "The person who will get the job has 10 coins in their pocket"
  But: Smith gets the job; and Smith also (unknown to himself) has 10 coins in his pocket
  Smith's justified true belief: "The person who will get the job has 10 coins"
  But Smith doesn't know this — it's justified true belief but not knowledge

GETTIER CASE 2 (Barn Facade County):
  Henry drives through a county filled with barn facades; one real barn exists
  Henry looks at the real barn; forms true justified belief "that's a barn"
  But: he couldn't distinguish it from the many facades
  Question: does Henry know there's a barn?
  Most people: NO — he was just lucky; he'd form the same belief looking at a facade

STRUCTURE OF GETTIER CASES:
  Agent has justified (even excellent) reasons for a belief
  Belief happens to be true
  But: the justification and the truth are only accidentally connected
  → Knowledge requires something beyond JTB: the justification must be appropriately
    connected to the truth-maker

RESPONSES TO GETTIER:
  Add a fourth condition:
    No false lemmas (Smith's case): belief must not be derived through false intermediate beliefs
    Defeasibility theory: no true proposition would defeat the justification if believed
    Problems: each fourth condition generates new Gettier-style counterexamples

  Reliability theories (see §3): external connection between belief and truth
  Contextualism: "knows" is context-sensitive; Gettier cases highlight this
  Epistemic luck: luck is incompatible with knowledge
```

---

## 2. Structure of Justification

### Foundationalism vs Coherentism

```
FOUNDATIONALISM:
  Beliefs form a hierarchical structure:
  Basic beliefs: justified independently, without inferential support from other beliefs
    Candidates: perception, memory, introspection, rational intuition
    Examples: "I see red," "I feel pain," "2+2=4"
  Non-basic beliefs: justified by inference from basic (or other) beliefs
  Chain of justification terminates at foundational beliefs

  STRONG foundationalism (Descartes): basic beliefs must be certain/infallible
    Cogito ergo sum: I think, therefore I am — the one indubitable belief
    Everything else derived from this via clear and distinct perception
    Problem: can derive very little; most knowledge is uncertain

  MODEST foundationalism (most contemporary): basic beliefs need not be infallible
    Perceptual beliefs are defeasibly basic (override absent defeater)
    Internalist question: what makes a belief basic? (usually: noninferential causation)

  PROBLEMS: What makes basic beliefs basic (not just "what I believe without argument")?
    Infinite regress argument: either beliefs form a chain terminating in basics (found),
    or a circular structure (coherentist), or infinite regress (unacceptable)

COHERENTISM:
  No privileged foundations; beliefs justified by fitting into a coherent system
  "The test of a belief's truth is its coherence with the rest of one's belief system"
  Justification is holistic: web of belief, not pyramid structure (Quine's metaphor)

  PROBLEMS: circularity (my beliefs are justified because they cohere with each other?);
    input problem (coherence is internal; how does external world get in?)
    Neurath's boat: we repair the ship at sea plank by plank; never from dry dock

INFINITISM (Klein): infinite chains of justification are possible and required
  Most unusual response; few defenders
```

### Internalism vs Externalism

```
INTERNALISM: justification depends only on factors internal to the mind
  Accessibility condition: what justifies a belief must be accessible to introspection
  What you can know from the armchair determines your justification
  Deontological: justified = followed the right epistemic rules
  Chisholm, Conee and Feldman ("Evidentialism")

EXTERNALISM: justification can depend on factors external to/inaccessible to the mind
  Reliabilism: a belief is justified if produced by a reliable cognitive process
    Not required to know the process is reliable; external fact determines justification
  Causal theory (Goldman): knowledge requires appropriate causal connection to the fact
  Proper functionalism (Plantinga): belief is warranted if produced by cognitive faculties
    functioning properly in an appropriate environment, successfully aimed at truth

INTERNALISM PROBLEM with Gettier:
  If justification is purely internal, the internal situation in Gettier cases seems fine
  → Gettier shows purely internal justification isn't enough for knowledge
  → Externalism seems better positioned to handle this

EXTERNALISM PROBLEM:
  "New evil demon": inhabitants of a demon world have same internal states as us
    but beliefs unreliably produced (demon creates false experiences)
    Internalist: their beliefs are equally justified (same internal evidence)
    Externalist: their beliefs are NOT justified (unreliably formed) — counterintuitive?
  "Clairvoyant": person has reliable clairvoyant faculty; uses it without knowing it's reliable
    Externalist: beliefs are justified (reliable process)
    Internalist: beliefs are NOT justified (no reason to trust the faculty)
```

---

## 3. Reliabilism

### Process Reliabilism (Goldman)

```
CORE THESIS: A belief is justified iff it is produced by a reliable cognitive process
  Reliable: process that tends to produce more true beliefs than false beliefs
  Process: perception, memory, introspection, inference, testimony-acceptance, reasoning

VIRTUOUS CIRCLE AVOIDED: you don't need to know your perception is reliable
  External fact (reliably formed) is what makes belief justified
  "Epistemically internalist" access not required

KEY RESULT: explains why perception/memory are better than wishful thinking
  Perception: generally reliable (evolutionary pressure; world-tracking mechanisms)
  Wishful thinking: unreliable (motivated by desires, not evidence)
  Intuition: reliability depends on domain (mathematical intuitions vs social biases)

PROBLEM — THE GENERALITY PROBLEM:
  Which process description do we use? "Vision" (reliable) vs "vision in poor lighting"
    (unreliable) vs "vision in poor lighting of red barn facade" (unreliable)?
  Any belief-forming process can be described at more or less specific level
  No principled criterion for the "right" level of description
  Reliabilists have not fully solved this

NORMAL WORLDS RELIABILISM: processes reliable in "normal" worlds count as justifying
  Addresses demon world case: demon victims have justified beliefs (processes reliable in normal worlds)

VIRTUE EPISTEMOLOGY (Sosa, Greco, Zagzebski):
  Extends reliabilism to intellectual virtues
  Knowledge = true belief from intellectual virtues (stable reliable cognitive dispositions)
  "Apt belief": accurate (true), adroit (skilled exercise of virtue), accurate because adroit
    → True belief from intellectual virtue, because of that virtue (no Gettier luck)
  Animal knowledge (apt): belief acquired through reliable faculties
  Reflective knowledge: reflectively understands own reliability and place in larger picture
```

---

## 4. Bayesian Epistemology

### Probability as Epistemic Rationality

```
BAYESIAN FRAMEWORK:
  Degree of belief (credence): real number in [0,1] representing strength of belief
  Not binary: belief vs disbelief; continuous spectrum
  Rational agent's credences: must satisfy probability axioms (Kolmogorov)
    (1) P(φ) ≥ 0
    (2) P(⊤) = 1 (tautologies have credence 1)
    (3) P(φ ∨ ψ) = P(φ) + P(ψ) if φ, ψ mutually exclusive

DUTCH BOOK ARGUMENT (de Finetti):
  If credences violate probability axioms, a clever bookie can construct a set of bets
  such that the agent accepts each bet but is guaranteed to lose money overall
  → Incoherent credences = pragmatically irrational; susceptible to exploitation
  → Rational agent's credences must be coherent (satisfy probability axioms)

CONDITIONALIZATION:
  Upon learning E with certainty:
    P_new(H) = P(H|E) = P(E|H) × P(H) / P(E)    (Bayes' theorem)
  This is the rule for rational belief update
  Jeffrey conditionalization: softer version when evidence itself is uncertain

PRIOR PROBABILITY:
  P(H) before evidence: your credence before observation
  Where does the prior come from? Major controversy:
    Subjective Bayesian (de Finetti): any coherent prior is permissible
      Only constraint: coherence; update by conditionalization; convergence eventually
    Objective Bayesian (Jaynes): logic determines the unique rational prior
      Maximum entropy principle: prior that makes fewest assumptions given constraints
      Principle of indifference: equal probability to symmetric alternatives
    Reference priors (Bernardo): invariant under reparametrization
```

### Confirmation Theory

```
BAYESIAN CONFIRMATION:
  Evidence E confirms hypothesis H iff P(H|E) > P(H)
    E raises the credence in H
  Evidence E disconfirms H iff P(H|E) < P(H)
  E is neutral re H iff P(H|E) = P(H)

  Degree of confirmation: Bayes factor P(E|H) / P(E|¬H)
    > 1: E confirms H; > 10: strong evidence; > 100: decisive

HYPOTHETICO-DEDUCTIVISM (HD):
  Theory T confirmed by evidence E if T deductively implies E (and E obtained)
  Problems: (1) T always conjoined with auxiliaries (Duhem-Quine); what is confirmed?
    (2) Tacking problem: T confirmed by E; T ∧ "moon is made of cheese" also confirmed?
    (3) Symmetry: T implies E; E also implied by many other theories
  Bayesianism handles all these more naturally (prior probabilities differentiate theories)

RAVENS PARADOX (Hempel):
  "All ravens are black" equivalent to "All non-black things are non-ravens"
  Observing a black raven: confirms "all ravens are black" (obvious)
  Observing a green leaf: confirms "all non-black things are non-ravens" →
    therefore confirms "all ravens are black"? (counterintuitive)
  Bayesian resolution: observing green leaf does technically confirm "all ravens are black"
    but by an astronomically small amount (there are vastly more non-ravens than ravens)
    The confirmation is real but negligible; intuition misleads about degree, not existence

GRUE PARADOX (Goodman):
  Define: grue = green if observed before time T, blue if observed after T
  "All emeralds are grue" is confirmed by every green emerald observed before T
  Both "all emeralds are green" and "all emeralds are grue" are equally confirmed by past evidence
  → Which hypothesis to project? Goodman: "projectible" predicates are "entrenched" (natural/familiar)
  Relevance: ML overfitting is the computational grue problem; regularization = entrenchment
```

---

## 5. Rationalism vs Empiricism

```
RATIONALISM:
  Some knowledge is a priori (independent of experience)
  Reason alone can yield substantive knowledge
  Mathematics, logic, ethics: known through pure reason
  Innate ideas (Descartes, Leibniz): some concepts/knowledge built into mind
  Kant: synthetic a priori knowledge — arithmetic, geometry, causation (Kant), space

EMPIRICISM:
  All knowledge derives from sensory experience
  Nothing in intellect not first in the senses (Locke, Hume, Berkeley)
  Hume's fork: relations of ideas (logic/math — analytic, necessary) vs
    matters of fact (empirical — contingent, can only be known by experience)
  A priori claims are analytic (true by meaning) — not substantive knowledge about world
  Kant's response: some a priori is synthetic (not mere tautology); empiricists wrong about math

QUINEAN NATURALISM (reconciliation of sorts):
  No analytic/synthetic distinction (sharp); no a priori/a posteriori sharp line
  Logic and math are part of the "web of belief" — subject to revision under extreme
    empirical pressure (though very central; hard to revise)
  Epistemology continuous with natural science; empirical psychology studies how we know
  The division between philosophy and science is not sharp

RELEVANCE TO AI/ML:
  Rationalist approach: build in domain structure and priors; knowledge graphs; type systems
  Empiricist approach: learn everything from data; tabula rasa deep learning
  Modern synthesis: inductive biases, architectural priors (CNNs for spatial locality,
    Transformers for sequence) + massive data
  Noam Chomsky: language acquisition requires innate universal grammar (rationalist about language)
  LLMs: learn language from data alone; neither pure rationalist nor pure empiricist
```
## Bridge — Epistemology and System Architecture

```
EPISTEMOLOGICAL POSITION         SYSTEM DESIGN PARALLEL
─────────────────────────────────────────────────────────────────
Rationalism: knowledge comes      Schema-first design: impose structure
from reason; structure is prior   before data arrives. Relational DB,
to experience.                    typed APIs, formal ontologies.
                                  You know the shape of knowledge in
                                  advance; data must conform to it.

Empiricism: knowledge comes       Schema-last / schema-flexible:
from experience; structure        NoSQL, document stores, data lakes.
emerges from data.                Let the data arrive; infer schema
                                  from what you observe. Structure
                                  is posterior, not prior.

Foundationalism: knowledge        Type systems / formal specs:
rests on a small set of basic,    axioms + inference rules. Some
self-evident beliefs from which   statements are foundational (axioms);
everything else is derived.       all others are derived. Coq/Lean
                                  proof assistants instantiate this.

Coherentism: beliefs are          Consistency constraints:
justified by their coherence      no single belief is privileged; the
with the whole system.            system is valid if internally
                                  consistent. Property-based testing:
                                  no single test is "basic"; all
                                  properties must be mutually coherent.

Reliabilism (Goldman):            Automated testing / CI:
a belief is justified if          "My belief-forming process (unit test
produced by a reliable            suite) reliably produces true
belief-forming process.           beliefs." The justification is the
                                  reliability of the process, not the
                                  content of any individual test.

Bayesian epistemology:            ML systems:
prior beliefs + evidence →        prior (architecture + regularization)
posterior. Update by Bayes.       + data → posterior weights. The
                                  epistemological position is the
                                  same; the implementation differs.
```

---

## 6. Social Epistemology

```
TESTIMONY AND TRUST:
  We know most of what we know through testimony (reading, instruction,
  communication with others). The epistemology of testimony asks when
  and why testimony transmits knowledge.
  Reductionism (Hume): testimony justified only when we have independent
    inductive evidence of the speaker's reliability. No default trust.
  Anti-reductionism (Coady): testimony has a default epistemic status;
    trust is prima facie warranted and defeasible by specific evidence
    against the speaker. (More plausible: we couldn't function if
    we required independent verification of every testimony source.)
  Virtue-theoretic: what cognitive virtues does a good epistemic agent
    need to navigate testimony reliably? Open-mindedness, calibration,
    intellectual humility.

EXPERT DISAGREEMENT AND SCIENTIFIC CONSENSUS:
  Peer disagreement problem: if equally reliable agents on the same evidence
    disagree, what is the rational response?
    Equal weight view: suspend judgment; average credences.
    Steadfast view: stick with your own assessment (you have privileged
      access to your own reasoning that your peer does not).
    Conciliatory view: partial revision toward peer's position.
  Experts vs. non-experts: non-experts should generally defer to expert
    consensus — but not uncritically. Need to identify experts, assess
    whether consensus actually exists, and evaluate conflicts of interest.
  Scientific consensus ≠ unanimous agreement: consensus is the dominant
    position after appropriate evidence-evaluation by qualified community.
    Manufactured doubt (tobacco, climate): deliberately create impression
    of expert disagreement where little exists.

EPISTEMIC INJUSTICE (Miranda Fricker, 2007):
  Two kinds of epistemic injustice — wrongs done to a person specifically
  in their capacity as a knower.

  Testimonial injustice: credibility deflated due to identity prejudice.
    A woman reports a crime; police discount her account based on gender.
    A patient's pain dismissed by a doctor based on demographic assumptions.
    Not just a moral wrong — an epistemic wrong: reliable testimony excluded
    from the pool of evidence used to form beliefs.

  Hermeneutical injustice: gap in collective interpretive resources puts
    someone at an unfair epistemic disadvantage.
    Before "sexual harassment" was named (Catharine MacKinnon, 1979), victims
    had experiences but no concept to make sense of them, report them, or
    get them taken seriously.
    The concept gap is structural: those who most need the resource are
    least likely to have had a hand in creating the shared vocabulary.

RELEVANCE TO AI/ML SYSTEMS:
  Testimonial injustice → training data bias:
    If historical human decisions reflect testimonial injustice
    (medical diagnoses, credit decisions, judicial outcomes), a model
    trained on that data reproduces the injustice at scale.
    COMPAS recidivism predictor: trained on data reflecting biased
    prior outcomes; perpetuated them algorithmically.

  Hermeneutical injustice → representational harm:
    AI systems trained on corpora that lack vocabulary for certain
    groups' experiences will be unable to model those experiences.
    "I was harassed at work" processed by a model trained on corpora
    where this is rare or absent → poor response quality for
    affected communities.

  Epistemic peer disagreement → model ensemble and calibration:
    When models trained on the same data with different inductive
    biases disagree — what weight to give each? Same structure as the
    peer disagreement problem. Calibration research asks whether
    the "steady-fast" (overconfident model) or "equal-weight"
    (ensemble average) approach performs better empirically.

STANDPOINT EPISTEMOLOGY:
  Social position affects what one can and cannot know.
  Marginalized groups may have epistemic access to facts about oppression
    that others structurally lack. Not relativism: some standpoints provide
    better epistemic access to some truths (not all truths).
  Research implications: including affected communities in research design
    is not just ethics — it is epistemically necessary to capture relevant
    evidence. Community-based participatory research.
```
```

---

## Decision Cheat Sheet

| Position | Core Claim | Problem |
|----------|-----------|---------|
| JTB | Knowledge = justified true belief | Gettier counterexamples |
| No-false-lemmas | Add: no false intermediate step | Too narrow; some Gettier cases survive |
| Process reliabilism | Belief justified iff from reliable process | Generality problem; demon world |
| Virtue epistemology | Knowledge = apt belief from virtue | How to individuate virtues |
| Bayesianism | Rational belief = coherent degrees of credence | Prior subjectivity; computability |
| Foundationalism | Justification terminates in basic beliefs | What makes beliefs basic |
| Coherentism | Justification from fit with belief system | Circularity; input problem |

---

## Common Confusion Points

**Gettier cases are not edge cases:** The Gettier problem is not a trivial puzzle about unusual scenarios. It exposes that the traditional analysis is fundamentally incomplete — justified true belief is not sufficient for knowledge. The philosophical profession moved from dismissing this 3-page paper to recognizing it as one of the most important epistemological results of the 20th century.

**Bayesianism is descriptive AND normative:** As a descriptive theory, Bayesianism is false — humans don't reason probabilistically. As a normative theory (how rational agents should reason), it's well-supported. The Dutch Book argument shows coherence is a requirement of rationality, not a description of how anyone actually reasons.

**A priori ≠ innate:** A priori knowledge is knowledge that doesn't depend on experience for its justification. Innate knowledge is knowledge present at birth. These are different — you can have a priori knowledge that is not innate (you learn it through reasoning without experience) and innate knowledge that is empirically justified.

**Internalism vs externalism is not about what beliefs you can form:** It's about what constitutes justification. Internalists say: what justifies your belief is always something you have access to by reflection. Externalists say: you can be justified even by factors you can't introspect (reliability of perceptual faculties, causal connections to the world).

**Relativism is not the same as fallibilism:** Fallibilism: even our most careful beliefs might be wrong; knowledge doesn't require certainty. Relativism: truth is relative to persons/cultures. Fallibilism is widely accepted and correct. Strong relativism is self-undermining and rejected by most epistemologists.
