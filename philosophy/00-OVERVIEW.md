# 00 — Philosophy: Landscape & Field Taxonomy

## The Discipline That Examines the Foundations of All Inquiry

---

## Big Picture: The Philosophy Map

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         PHILOSOPHY                                       │
│              The discipline that asks foundational questions             │
│              that every other field assumes away                         │
├────────────────────────────────┬─────────────────────────────────────────┤
│  FORMAL / FOUNDATIONAL         │  SUBSTANTIVE                           │
├────────────────────────────────┼─────────────────────────────────────────┤
│  Logic & Formal Methods        │  Epistemology (theory of knowledge)     │
│  ├── Propositional logic       │  ├── What is knowledge?                 │
│  ├── Predicate (FOL)           │  ├── Justification & evidence           │
│  ├── Modal logic               │  ├── Skepticism                         │
│  ├── Proof theory              │  └── Bayesian epistemology              │
│  └── Gödel's incompleteness    │                                         │
│                                │  Metaphysics (nature of reality)        │
│  Philosophy of Mathematics     │  ├── Ontology (what exists)             │
│  ├── Platonism                 │  ├── Causation & laws                   │
│  ├── Formalism (Hilbert)       │  ├── Time & persistence                 │
│  ├── Intuitionism              │  └── Modality (possible worlds)         │
│  └── Logicism (Frege/Russell)  │                                         │
│                                │  Ethics & Political Philosophy          │
│  Philosophy of Science         │  ├── Metaethics                         │
│  ├── Demarcation               │  ├── Consequentialism                   │
│  ├── Explanation               │  ├── Deontology (Kant)                  │
│  ├── Scientific realism        │  └── Virtue ethics                      │
│  └── Paradigm shifts (Kuhn)    │                                         │
│                                │  Philosophy of Mind                     │
│                                │  ├── Mind-body problem                  │
│                                │  ├── Consciousness & qualia             │
│                                │  ├── Functionalism                      │
│                                │  └── AI & machine consciousness         │
└────────────────────────────────┴─────────────────────────────────────────┘
```

---

## Prelude: Why Philosophy Matters for Engineers and Scientists

### Gödel's Shadow Over Everything

```
Gödel's incompleteness theorems (1931) — the most philosophically important results in 20th-century
mathematics, from an MIT TCS perspective:

  FIRST INCOMPLETENESS THEOREM:
  Any consistent formal system F strong enough to express arithmetic contains statements
  that are true (in the standard model) but not provable in F.

  Construction: Gödel numbering assigns natural numbers to formulas and proofs.
    Construct: G ≡ "G is not provable in F"
    If F proves G → F proves something false → F is inconsistent (contradiction)
    If F proves ¬G → F proves G is provable → but then G is false in any model
    where F is consistent → soundness violated
    Conclusion: G is true but unprovable → F is incomplete.

  SECOND INCOMPLETENESS THEOREM:
  F cannot prove its own consistency, if F is consistent.
    This killed Hilbert's Program: impossible to prove arithmetic consistent from within
    arithmetic using only finitary methods.

  TCS CONNECTION:
    Halting problem undecidability (Turing 1936): reduction to Gödel
    Rice's theorem: all non-trivial semantic properties of programs are undecidable
    Kolmogorov complexity: no program can compute K(x) for all x (non-computability)
    Proof assistants (Coq, Lean): must accept axioms on faith (can't prove consistency)
    Curry-Howard: propositions-as-types → proof ≡ program; incompleteness = some types
      are inhabited but you can't construct the term

  PHILOSOPHICAL IMPLICATIONS:
    Mathematical platonism vs formalism: if true statements exist beyond provability →
      math has a reality independent of formal systems (Gödel was a Platonist)
    Limits of mechanism: Lucas-Penrose argument (contested): human minds can see truths
      formal systems cannot → mind ≠ algorithm (most logicians reject this)
    Foundations crisis resolved pragmatically: ZFC as standard foundation; accept
      unprovable axioms; move on
```

### Philosophy of Probability (Engineers Need This)

```
FREQUENTISM:
  Probability = long-run relative frequency over repeated trials
  P(heads) = limit of #heads / #flips as n → ∞
  Problems: what about singular events? "Probability WWII started in 1939" has no repeatable
    trial. Probability of life on Mars? Of a specific diagnosis?
  Cannot handle priors; inference limited to frequentist procedures

BAYESIANISM:
  Probability = degree of rational belief
  Prior P(H) + Evidence E → Posterior P(H|E) via Bayes' theorem
  P(H|E) = P(E|H) × P(H) / P(E)
  Coherence: rational agent's degrees of belief must be probabilities (Dutch Book argument)
  Problem: subjectivity of priors; Bayesians disagree on which priors are rational

SUBJECTIVE vs OBJECTIVE BAYESIANISM:
  Subjective: any coherent prior is permissible (de Finetti)
  Objective: some priors are uniquely rational (reference priors, maximum entropy)
    Jaynes: maximum entropy principle → unique prior given constraints

RELEVANCE TO ML/STATISTICS:
  Maximum likelihood estimation: frequentist; regularization = implicit prior
  Bayesian neural networks: full posterior over weights; uncertainty quantification
  MCMC (Markov Chain Monte Carlo): sampling from posterior distributions
  Bayes optimal classifier: minimizes expected loss under posterior
  Frequentist hypothesis testing (p-values): not probability hypothesis is true;
    probability of getting this data if null hypothesis were true
    → p = 0.03 does not mean 97% chance hypothesis is true (base rate neglect)
```

---

## 1. Major Schools and Their Relations

### Analytic vs Continental Philosophy

```
ANALYTIC PHILOSOPHY (dominant in US/UK/Australia):
  Method: logical analysis of language; formal rigor; argument clarity
  Exemplars: Frege, Russell, Wittgenstein (early), Carnap, Quine, Kripke
  Relation to science: continuous; naturalized epistemology (Quine); philosophy as partner
  Relation to TCS: logic, semantics, philosophy of math, mind → deep overlap

CONTINENTAL PHILOSOPHY (France, Germany):
  Method: hermeneutics, phenomenology, dialectics; history of ideas
  Exemplars: Hegel, Husserl, Heidegger, Sartre, Derrida, Foucault
  Different mode of inquiry; engages differently with science
  Relevant for: philosophy of technology, social theory, critical theory of AI

PRAGMATISM (American tradition):
  Peirce: truth is what works for rational inquiry in the long run
  James: truth is what is useful to believe
  Dewey: naturalistic; inquiry as problem-solving; education as growth
  Contemporary: Rorty (antirealist), Brandom (inferentialism)
  Relevant: pragmatist AI evaluation (is it useful?) vs realist (does it understand?)
```

### Metaphysical Positions

```
REALISM vs ANTI-REALISM (pervasive debate in every subfield):
  Moral realism: moral facts exist independently of beliefs
  Scientific realism: theoretical entities (electrons, fields) really exist
  Mathematical platonism: numbers/structures exist independently of minds
  Anti-realist positions: instrumentalism, constructivism, conventionalism

IDEALISM vs MATERIALISM:
  Idealism: minds or ideas are fundamentally real; physical world depends on mind
    (Berkeley: esse est percipi; Kant: mind structures experience)
  Materialism/physicalism: only physical stuff exists; mental events = physical
  Dualism: mind and body are different substances (Descartes: res cogitans + res extensa)
    Interaction problem: if separate, how do they causally interact?

NATURALISM:
  Everything that exists is natural (physical); no supernatural
  Methodological naturalism: science should not appeal to supernatural
  Philosophical naturalism: philosophy continuous with science (Quine)
  Standard position in analytic philosophy and most of science
```

---

## 3. Central Problems and Their Modern Forms

### The Problem of Consciousness (Hard Problem)

```
David Chalmers' distinction (1995):
  EASY PROBLEMS: explaining cognitive functions (perception, memory, attention, verbal reports)
    These are hard scientifically but not philosophically puzzling in principle
    "Easy" = explainable by mechanism; we just need to figure out the mechanism

  HARD PROBLEM: why is there subjective experience at all?
    Why does information processing feel like anything from the inside?
    "What it's like" to see red, feel pain, taste coffee
    Even complete physical/computational account seems to leave this out

  WHY THIS MATTERS FOR AI:
    If consciousness = computation (functionalism), then sufficiently complex AI is conscious
    If consciousness requires something beyond computation (biological, quantum, ...), then not
    Current LLMs: do they have anything it's like to be them? (Almost certainly no — but
      the criteria for deciding are philosophically unclear)
    Alignment: if AI systems are conscious, what are our obligations to them?
    p-zombie: entity behaviorally identical to human but with no inner experience
      Functionalist: incoherent (function = experience); Chalmers: conceivable

EXPLANATORY GAP: even if we knew every neuron's state, would we understand why there's
  experience? Levine's point: there's a gap between physical description and phenomenal quality
```

### Causation and Counterfactuals

```
HUME: no necessary connection between events; causation = constant conjunction + contiguity + priority
  Regularity theory: "A causes B" = "Whenever A, then B"
  Problem: symmetry (barometer pressure ↔ storm — correlated, but neither causes the other)

COUNTERFACTUAL THEORY (David Lewis):
  "A caused B" = in the closest possible world where A doesn't occur, B doesn't occur
  Closest world: similar to actual world, varying only what's necessary
  Problem: preemption (assassin shoots target; backup assassin ready — backup caused nothing
    even though target still dies if backup acts when actual assassin does)

INTERVENTIONIST/CAUSAL GRAPHS (Pearl):
  Causal Bayesian Networks: represent causal relationships as directed acyclic graphs
  Do-calculus: "do(X=x)" = intervention; forces X regardless of its natural causes
    Observational: P(Y | X=x) — just conditioning; no causal claim
    Interventional: P(Y | do(X=x)) — do this; cut natural causes of X
  Counterfactual query: Y_x(u) — value of Y in world where X was set to x for unit u
  THIS IS THE FRAMEWORK USED IN CAUSAL ML/STATISTICS (Pearl's Book of Why)
  Relevance: ML systems find correlations; causal ML asks "would this still work under intervention?"
```

---

## 3b. Political Philosophy

```
CORE QUESTION: What justifies political authority? What makes a state legitimate?

SOCIAL CONTRACT THEORIES:
  Hobbes: without contract, life is "nasty, brutish, short" (war of all against all).
    Rational agents cede some freedom to a sovereign for security.
    Legitimacy = effective protection; no right to rebel if sovereign fails.
  Locke: natural rights (life, liberty, property) precede the state.
    State legitimate only if it protects these rights.
    Right to revolution if it fails → foundational for US Declaration.
  Rousseau: general will (volonté générale) — the common good, not sum of preferences.
    Social contract creates collective moral agent; individual freedom preserved
    by being subject only to laws one has collectively willed.

RAWLS — A THEORY OF JUSTICE (1971):
  Original position + veil of ignorance:
    Design a just society not knowing your place in it (class, race, talents).
    Rational contractors behind veil would choose:
      (1) Equal basic liberties (liberty principle)
      (2) Fair equality of opportunity
      (3) Difference principle: inequalities justified only if they benefit
          the least-advantaged members of society
  Relevance: standard framework for AI governance debates (who bears the risk?
    who benefits? what principles would we choose not knowing our position?)

NOZICK — ANARCHY, STATE, AND UTOPIA (1974):
  Libertarian response to Rawls.
  Natural rights as side-constraints: cannot violate individual rights even
    for aggregate benefit. Taxation = forced labor.
  Minimal state (night-watchman): only state that can be justified is one
    that protects against force, theft, fraud. Nothing more.

RELEVANCE TO TECHNOLOGY GOVERNANCE:
  Rawlsian: AI benefits must reach the least well-off; worst-case protections
    are non-negotiable regardless of aggregate utility.
  Nozickian: individual autonomy and property rights constrain data use;
    consent is foundational regardless of social benefit.
  Democratic theory: platform governance is quasi-legislative; who has
    voice in norm-setting? Epistocracy vs democratic legitimacy in AI labs.
```

## 3c. Philosophy of Mathematics (cross-reference: 01-LOGIC.md §5)

```
THE FOUNDATIONAL QUESTION: What are mathematical objects, and how do we know about them?

PLATONISM (Mathematical Realism):
  Mathematical objects (numbers, sets, functions) exist independently of minds.
  Gödel was a Platonist: we perceive mathematical truths by "mathematical intuition."
  Explanatory virtue: why does math work so well in physics? (Wigner's "unreasonable
    effectiveness") — if math is invented, this is mysterious; if discovered, less so.
  Problem: epistemic access — how do we come into contact with abstract objects?

FORMALISM (Hilbert):
  Mathematics is manipulation of formal symbols according to rules.
  No abstract objects; just strings and inference rules.
  Decimated by Gödel: Hilbert's program (prove consistency of arithmetic by finitary
    means) is impossible. Formalism must accept axioms on faith.

LOGICISM (Frege, Russell):
  Mathematics = logic; mathematical truths are logical truths.
  Russell's Principia Mathematica: derive all math from logic.
  Russell's paradox undermined naive set theory (set of all sets not members of themselves).
  Type theory (Russell) as the fix → genealogy of modern type systems in PL.

INTUITIONISM (Brouwer):
  Mathematical objects are mental constructions; they exist only when constructed.
  Consequence: reject law of excluded middle (¬¬P ≠ P constructively).
  Proof must be constructive: existence proof by contradiction is illegitimate.
  → Intuitionistic type theory (Martin-Löf) → Coq, Agda, Lean foundations.
  → Curry-Howard: constructive proofs = programs; classical logic = programs with
    control operators (callcc). The foundational position has real PL consequences.

STRUCTURALISM:
  Mathematics is about structures, not specific objects.
  Natural numbers: not specific objects but any ω-sequence satisfying Peano axioms.
  Multiple realizations: the same structure can be instantiated differently.
  Explains applicability: science uses mathematical structures; which objects fill
    the structure roles is irrelevant.

See 01-LOGIC.md for proof theory, Gödel details, and proof assistants.
```

## 4. Philosophy in Modern Technical Context

### Decision Theory

```
EXPECTED UTILITY MAXIMIZATION:
  Agent has utility function U over outcomes; beliefs = probability distribution
  Chooses action a* = argmax_a Σ_s P(s) × U(outcome(a,s))
  Von Neumann-Morgenstern theorem: if preferences satisfy rationality axioms →
    can be represented by expected utility maximization

PROBLEMS WITH EXPECTED UTILITY:
  Allais paradox: people violate EU in predictable ways
  Ellsberg paradox: ambiguity aversion (unknown vs known probability)
  St. Petersburg paradox: infinite expected value; no rational max bid
  Prospect theory (Kahneman-Tversky): descriptive model; loss aversion; probability weighting

NEWCOMB'S PROBLEM:
  Predictor puts $1M in box B if it predicts you take only box B; $0 if you take both
  $1K in box A guaranteed; box B already set (opaque)
  Two-box: dominant strategy (causal decision theory — cause of boxes already determined)
  One-box: evidential decision theory (taking only B is evidence predictor put money there)
  Relevance: CDT vs EDT in AI alignment; what decision theory to build into AI agents

DUTCH BOOK ARGUMENT:
  If your probability assignments are incoherent (not proper probability), a clever bookie
  can construct a set of bets you'll accept that guarantees your loss
  → Bayesian coherence is rationality requirement
```

### Ethics and AI

```
TROLLEY PROBLEM (Philippa Foot, 1967):
  Runaway trolley will kill 5; pull lever and divert to kill 1?
  Most people: yes (utilitarian intuition)
  Footbridge version: push fat man off bridge to stop trolley and save 5?
  Most people: no (despite identical arithmetic)
  → Distinction between doing and allowing; doctrine of double effect; agent-relative ethics
  AUTONOMOUS VEHICLE VERSION: program car to kill X to save Y? Whose values? Legal liability?

MORAL STATUS OF AI:
  What properties confer moral status? Sentience (capacity for suffering)?
    Consciousness? Rationality? Social relations?
  If LLMs are not conscious: moral status = zero (no obligations to them)
  If future AI has something like experience: moral consideration required
  Difficulty: we lack reliable tests for consciousness even in humans (by analogy)

AI ALIGNMENT (technical philosophy):
  Value learning: RLHF trains on human feedback → which humans? Which preferences?
    (Preference aggregation problem → Arrow's impossibility theorem applies)
  Goodhart's Law: any measure used as a target ceases to be a good measure
  Orthogonality thesis (Bostrom): intelligence and goals are orthogonal → any goal can be
    combined with any level of intelligence (paperclip maximizer)
  Instrumental convergence: sufficiently capable agents will pursue self-preservation,
    goal-content integrity, capability acquisition regardless of terminal goals
```

---

## Bridge — Philosophy and Formal Engineering Practice

```
PHILOSOPHICAL POSITION          ENGINEERING / CS PARALLEL
─────────────────────────────────────────────────────────────────
Gödel completeness vs.          Every formal system has limits.
incompleteness:                 Type systems cannot catch all bugs.
Some truths are beyond          Turing completeness ↔ halting
provable reach.                 undecidability. Rice's theorem:
                                no semantic property of programs
                                is decidable in general.
                                Engineers live with this daily.

Hilbert's Program (formalize    Formal verification (TLA+, Coq,
everything; prove consistency): Lean, Isabelle): provably correct
failed by Gödel, but the        code. You accept axioms on faith
practice lives on in            (OS correctness, compiler, hardware).
proof-assistant culture.        seL4 verified kernel; CompCert
                                verified C compiler. Hilbert's
                                dream, bounded.

Philosophical foundations of    Schema-first (relational, typed):
knowledge (rationalism vs.      rationalist architecture — structure
empiricism):                    imposed before data arrives.
How much structure to impose    Schema-last (NoSQL, document store):
on data vs. let it emerge.      empiricist — let structure emerge
                                from the data itself.
                                Any data architect has made this
                                trade-off explicitly.

Kuhn's paradigm shifts:         Platform migrations: every 10-15
Normal science → crisis →       years, a new computational paradigm
new paradigm. The old paradigm  replaces the old.
is incommensurable with the     mainframe → client-server → web →
new; no neutral comparison.     cloud → mobile → AI.
                                Old skills don't directly transfer;
                                the new paradigm has its own
                                ontology (containers ≠ VMs, even
                                though they serve some of the same
                                function). You cannot evaluate the
                                new paradigm from entirely within
                                the old one's terms.

Rawlsian veil of ignorance:     API design and system design under
Design principles without       uncertainty about who the caller will
knowing your position.          be. Design contracts that are fair
                                to all future callers, not just the
                                first one you have in mind.
                                "You are not the user."

Arrow's Impossibility Theorem:  No aggregation of diverse team
No consistent social choice     preferences (on architecture, stack,
function satisfying basic       process) satisfies all fairness
fairness axioms exists.         criteria simultaneously. Org
                                decision-making is inherently
                                constrained by impossibility results.
                                Acknowledgment of this is more
                                productive than searching for the
                                "right" aggregation procedure.
```

## Decision Cheat Sheet

| Philosophical Problem | Current Best Position | Why It Matters Practically |
|----------------------|-----------------------|---------------------------|
| Mind-body problem | Functionalism (dominant in philosophy of AI); Hard problem unsolved | AI consciousness criteria; alignment obligations |
| Foundations of math | ZFC set theory; Gödel limits; pragmatic acceptance | Proof assistants; undecidability limits |
| Scientific realism | Structural realism (moderate); instrumentalism for quantum | Interpretation of ML models as "understanding" |
| Causation | Interventionist/Pearl | Causal ML; do-calculus; model-based RL |
| Probability foundations | Subjective Bayesianism with calibration | ML uncertainty quantification; p-value misinterpretation |
| Ethics for AI | No consensus; deontological constraints + consequentialist goals | Alignment; content policy; autonomous systems |

---

## Common Confusion Points

**Philosophy ≠ speculation:** At its best, philosophy is rigorous argument about foundational questions. Kripke's modal logic, Gödel's incompleteness proofs, Tarski's semantic theory of truth, Arrow's impossibility theorem — all are philosophical results with mathematical precision.

**Gödel doesn't say "anything goes":** Incompleteness means some truths are unprovable within a system — not that truth is subjective or that formal systems are useless. ZFC set theory is a perfectly good foundation for working mathematics despite Gödel.

**The hard problem is not confused:** The easy problems of consciousness (explaining cognitive functions) are important and hard. The hard problem (why there's subjective experience) is a different question that's not answered by solving the easy problems. Chalmers's distinction is well-taken.

**Bayesianism and frequentism coexist:** Most working statisticians use both depending on context. Bayesian methods excel at incorporating prior knowledge and updating incrementally. Frequentist methods excel at providing guarantees that don't depend on prior specification. Knowing both is professional hygiene.

**Philosophy of mind ≠ neuroscience:** Neuroscience answers "how does the brain process X?" Philosophy of mind asks "what is the relationship between brain processes and mental states?" — a conceptual question, not empirical. Both are needed; neither substitutes for the other.
