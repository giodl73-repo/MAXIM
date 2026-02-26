# Philosophy by Field: Physics, Biology, Economics, Psychology, CS

## The Big Picture

General philosophy of science (demarcation, realism, causation) plays out differently in different disciplines. Each field has its own specific philosophical problems that depend on the content of the science itself. This guide covers the four most philosophically dense special sciences plus connections to TCS.

```
+------------------------------------------------------------------+
|           PHILOSOPHY BY FIELD — PROBLEM MAP                     |
+------------------------------------------------------------------+
|                                                                  |
|  PHYSICS                  BIOLOGY                                |
|  QM interpretation        Species concept (22+ definitions)     |
|  Arrow of time            Function (structural vs. etiological)  |
|  Absolute vs.             Levels of selection                   |
|  relational space         Adaptationism debate                  |
|  GR vs. QM:               Teleology naturalized                 |
|  quantum gravity                                                 |
|                                                                  |
|  ECONOMICS                PSYCHOLOGY                             |
|  Positive vs.             Folk psychology and eliminativism     |
|  normative                Multiple realizability                 |
|  Models as                Functionalism and qualia              |
|  idealizations            Computational theory of mind          |
|  Homo economicus          Church-Turing as philosophy           |
|  Friedman instrumentalism Language of thought hypothesis        |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Philosophy of Physics

### The Quantum Mechanics Interpretation Problem

QM is the most predictively accurate physical theory ever developed. Its formalism is unambiguous. Its **interpretation** — what it says about reality — is genuinely contested, with multiple incompatible accounts consistent with all observational data. This is underdetermination of theory by evidence in its purest form.

```
+------------------------------------------------------------------+
|              QM INTERPRETATIONS — COMPARISON                    |
+------------------------------------------------------------------+
|                                                                  |
|  FORMALISM: ψ evolves via Schrödinger equation.                 |
|  Measurement gives eigenvalue with Born rule probability.       |
|  Formalism: uncontested. Interpretation: 5+ serious rivals.     |
|                                                                  |
+--------------------+-------------------------------------------+ |
| INTERPRETATION     | ONTOLOGY / KEY CLAIM                      | |
+--------------------+-------------------------------------------+ |
| Copenhagen         | No fact about unmeasured quantities.      | |
| (Bohr, Heisenberg) | Wavefunction is not real; just a          | |
|                    | calculation tool. Measurement defines     | |
|                    | what was measured.                        | |
+--------------------+-------------------------------------------+ |
| Many-Worlds        | Wavefunction is real. No collapse.        | |
| (Everett 1957)     | All branches exist. Observers split       | |
|                    | at each "measurement." You are in         | |
|                    | one branch; all others also exist.        | |
+--------------------+-------------------------------------------+ |
| Bohmian Mechanics  | Hidden variables. Particles have          | |
| (de Broglie-Bohm)  | definite positions at all times.          | |
|                    | Wavefunction is real, guides particles.   | |
|                    | Reproduces QM predictions exactly.        | |
+--------------------+-------------------------------------------+ |
| QBism              | Wavefunction = agent's beliefs about      | |
| (Fuchs, Caves)     | outcomes, not objective property of       | |
|                    | the world. Measurement = agent update.    | |
|                    | Bayesian QM; deeply anti-realist.         | |
+--------------------+-------------------------------------------+ |
| Relational QM      | Wavefunction relative to observer system. | |
| (Rovelli)          | No absolute state; only relative states.  | |
+--------------------+-------------------------------------------+ |
|                                                                  |
|  ALL produce identical empirical predictions. Pure under-       |
|  determination. Choice is metaphysical, not empirical.          |
|                                                                  |
+------------------------------------------------------------------+
```

### Arrow of Time

The fundamental laws of physics (Newton, Maxwell, Schrödinger) are **time-symmetric**: they work the same forward and backward. Yet we experience time as having a direction. Eggs break, not unbreak. Memory of past, not future.

**Thermodynamic arrow**: Entropy increases in one direction (Second Law). But the Second Law is statistical, not fundamental — the probability of spontaneous entropy decrease is extremely low, not zero.

**Boltzmann's insight**: Low entropy past + statistical mechanics → entropy tends to increase. But: why was the past low-entropy? This is the **Past Hypothesis** (David Albert): the universe began in an extraordinarily low-entropy state. That boundary condition, not any fundamental time-asymmetry, grounds the arrow.

**Psychological arrow**: Memory of past, anticipation of future. Explanation: memory requires low entropy, physical traces of past events. High entropy → no traces → no memory. Memory direction tracks entropy gradient.

**Causal arrow**: Causes precede effects. Explanation: still contested. Some (Price) argue we project causal asymmetry onto a time-symmetric world.

### Absolute vs. Relational Space

**Leibniz-Clarke controversy** (1715–16): Is space an absolute container (Newton/Clarke) or merely the relation between material bodies (Leibniz)?

Newton's **bucket argument**: Spinning water concaves upward even if you remove all material reference frames. The concavity reflects rotation relative to *absolute space*. If space were just relations between bodies, there could be no absolute rotation.

**Einstein's General Relativity** (1915): Spacetime curvature is physical — not absolute in Newton's sense, but not merely relational either. The field equations make spacetime dynamic: matter curves spacetime, curved spacetime guides matter. This is a middle position.

**Relationalism revived**: Julian Barbour (Machian program): all dynamics can be expressed in terms of changing relations between bodies. The universe has no absolute clock, only relative change.

---

## Philosophy of Biology

### The Species Problem

What is a species? Biology has 22+ species concepts, and they disagree about which groups count as species. The disagreement is philosophically deep.

| Concept | Criterion | Example Problem |
|---------|-----------|-----------------|
| **Biological Species Concept** (Mayr) | Members of a natural interbreeding population reproductively isolated from others | Asexual organisms, ring species, hybridizing species |
| **Morphological Species Concept** | Grouped by morphological similarity | Cryptic species (identical morphology, non-interbreeding) |
| **Phylogenetic Species Concept** | Smallest clade with unique derived character | Inflates species count; inconsistent at fine-scale |
| **Ecological Species Concept** (Van Valen) | Occupy the same adaptive zone / ecological niche | Hard to define niche without circularity |
| **Cohesion Species Concept** | Cohesive genetic/demographic exchangeability | Underspecified for many groups |

**The philosophical question**: Is "species" a natural kind (corresponding to a real category in nature) or a human classification imposed on a continuum?

### Functional Explanation in Biology

Why does the heart beat? Two philosophical accounts:

**Cummins functional analysis**: The heart is a pump, and we describe its function by citing its contribution to the overall system it operates in (the circulatory system). Function = what something does within a containing system.

**Etiological/selected effects theory** (Millikan, Neander): The heart is *for* pumping blood because pumping blood is what the ancestors of hearts were selected for. Function = what the trait was selected for in evolutionary history.

```
CUMMINS vs. MILLIKAN:

  Question: What is the function of the appendix?

  CUMMINS: Whatever it does in the current system.
  If it now houses beneficial gut bacteria: that's its function.

  MILLIKAN: What it was selected for in evolutionary history.
  Currently uncertain (immune function?), but whatever
  caused ancestral appendix-bearers to leave more offspring.

  KEY DIFFERENCE: Is function current role or historical cause?
  Millikan: functions can be failures (hearts can fail to pump)
  Cummins: functions are what something actually does

  IMPLICATION: Millikan's account can identify malfunction
  (appendix fails its evolutionary function if infected);
  Cummins cannot distinguish function from mere effect.
```

### Levels of Selection

Does natural selection act on genes (Dawkins), organisms, or groups?

**Genic selectionism** (Dawkins, Williams): The gene is the unit of selection. Organisms are "survival machines" built by genes to replicate. Group-level traits are explained by gene-level selection.

**Organism-level selection**: Standard Darwinism. Individual organisms differ in fitness; selection acts on organisms.

**Group selection** (Wilson, Sober): Selection can act on groups of organisms. Altruism evolves if groups with altruists outcompete groups without. This was long rejected but has been partially rehabilitated via multilevel selection theory.

**Levels of selection debate** has practical stakes: whether altruism, cooperation, and social behavior evolved via group or kin selection (Hamilton's kin selection / inclusive fitness) determines how to model social evolution.

### Gould and Lewontin: The Spandrels of San Marco (1979)

Stephen Jay Gould and Richard Lewontin attacked **adaptationism** — the tendency to explain every biological trait as an adaptation to something.

A **spandrel** is an architectural space created as a by-product of mounting a dome on arches (as in San Marco basilica). Spandrels are not *for* their elaborate decorations — the decoration is a by-product.

Gould/Lewontin: many biological traits are spandrels — by-products of other adaptations, not adaptations themselves. Adaptationists "invent just-so stories" for every trait. The human chin, for example, may be a spandrel of jaw development constraints, not an adaptation.

---

## Philosophy of Economics

### Positive vs. Normative

**Positive economics**: What is the case (empirical claims: supply and demand, GDP measurement, inflation rates).

**Normative economics**: What ought to be the case (policy recommendations: minimum wage, redistribution, carbon tax).

Hume's is-ought gap applies: you cannot derive normative conclusions from positive ones alone. A full cost-benefit analysis is positive; the decision to adopt a policy is normative (requires value weights).

Much debate about whether economic claims (especially welfare economics) are genuinely positive or are normative in disguise (e.g., Pareto efficiency as a criterion embeds a specific value stance).

### Models as Idealizations

Economic models routinely include assumptions known to be false:
- Perfectly rational actors with complete information
- Infinite divisibility of goods
- Competitive equilibrium with identical agents
- Zero transaction costs

**Friedman's instrumentalism** (1953): A theory's assumptions don't need to be realistic — only its predictions need to be accurate. The "as if" methodology. Firms behave as if they maximize profit, even if managers don't consciously optimize.

**Critique**: If the assumptions are false, the model gives wrong predictions in out-of-sample contexts. The GFC (2008) is exhibit A — models with unrealistic assumptions about risk correlation failed catastrophically.

**Idealization as methodology**: Weisberg distinguishes minimal models (capture one mechanism in isolation), targetless models (no specific target, develop theory), and multiple models (triangulating on a phenomenon via different idealizations). Economic models are a mix of all three.

---

## Philosophy of Psychology

### Folk Psychology and Eliminative Materialism

**Folk psychology**: The everyday framework of beliefs, desires, intentions, and reasons that explains human behavior. "She took the umbrella because she believed it would rain and wanted to stay dry."

**Paul Churchland's eliminative materialism** (1981): Folk psychological categories (beliefs, desires) don't correspond to real kinds in the brain. They are like phlogiston — useful approximations of a folk theory that will be replaced by mature neuroscience. There are no beliefs; there are just neuronal states.

**Jerry Fodor's response**: Folk psychology is incredibly predictively powerful — it's the best theory of human behavior available. If eliminative materialism is right, we can't explain why folk psychology works so well. Also: multiple realizability means mental level is autonomous from neural level (see 07-CAUSATION.md).

### Functionalism

**Functionalism** (Putnam, Lewis): Mental states are defined by their functional roles — causal relations to inputs, outputs, and other mental states — not by their physical substrate.

Pain = whatever state is caused by tissue damage, causes avoidance behavior, interacts with beliefs and desires in the characteristic way. Pain can be realized by C-fibers in humans, different neurons in octopuses, silicon chips in robots.

```
FUNCTIONALISM — MULTIPLE REALIZABILITY:

  Pain:
  Human:     C-fiber activation → Pain state → avoidance
  Octopus:   ? neurons → Pain state → avoidance
  Robot:     ? silicon → Pain state → avoidance

  If they all have the same functional profile,
  they all have pain — regardless of substrate.

  IMPLICATIONS:
  - Mental states are real (not eliminated)
  - Mental states are multiply realizable
  - Neuroscience cannot replace psychology
    (different level, different laws)
```

**The qualia objection** (Nagel, Chalmers): Even if we know all the functional facts, we seem to be missing something — **what it's like** to be in that state. Functionalism tells you the causal role of pain; it doesn't explain why pain feels like something. This is Chalmers's "hard problem of consciousness."

---

## Connections to Computer Science and TCS

### The Church-Turing Thesis as Philosophy

The Church-Turing thesis: every effectively computable function is Turing-computable. This is not a theorem — it cannot be proved. It is a philosophical claim about the extension of "computation."

**Physical Church-Turing thesis**: Every physical process is computable by a Turing machine. This is a substantial metaphysical claim — it says the universe is effectively a digital computer. Contested by quantum computation (does quantum computing go beyond classical Turing?) and by hypercomputation proposals.

**Strong Church-Turing thesis**: Every physically realizable computation can be simulated efficiently by a probabilistic Turing machine. Quantum computing potentially violates this (Shor's algorithm provides exponential speedup for factoring).

### The Computational Theory of Mind

**The mind is a computational system**: Mental states are computational states; mental processes are computational processes. Cognitive science: the brain computes.

**Fodor's Language of Thought hypothesis** (LOTH): Thought is a language — there is a syntactically structured medium of mental representation ("Mentalese") over which computational operations are defined. Thinking = manipulating Mentalese expressions.

Connection to TCS: if mental processing is computation, then complexity theory applies to cognition. Bounded rationality (Simon) = cognition operating under computational constraints. Some cognitive biases may be artifacts of approximately-correct heuristics running in polynomial time on problems that are NP-hard if solved exactly.

```
TCS → COGNITION CONNECTIONS:

  Satisfiability (NP-hard)
  → Humans use greedy/heuristic search, not exhaustive
  → Cognitive "satisficing" (Simon) is computationally rational

  Inference under uncertainty (Bayesian inference)
  → Exact Bayesian inference is #P-hard in general
  → Humans approximate — variational inference, sampling
  → Explain cognitive biases as rational approximations

  Pattern recognition (learning theory)
  → Human concept learning = PAC learning under noise?
  → Or something more structured (inductive logic programming)

  The question: what complexity class does cognition fall in?
  Not settled. But TCS provides the right vocabulary.
```

### Computability and the Mind

**Penrose-Lucas argument**: Gödel's incompleteness theorem shows that for any consistent formal system, there are truths it cannot prove. Humans can recognize the Gödelian unprovable sentence as true. Therefore human cognition is not computable by any formal system.

**Standard response**: Penrose-Lucas confuses the Gödel sentence for a *fixed* formal system. For humans to "recognize" the Gödelian truth, they would need to be certain their own cognitive system is consistent — which they cannot know (for the same Gödelian reasons). The argument has a reflexivity problem.

The Penrose argument is relevant because it is a direct application of TCS (specifically computability theory) to a philosophical thesis about mind.

---

## Decision Cheat Sheet

| Field | Core Philosophical Problem | Best Entry Point |
|-------|---------------------------|-----------------|
| **QM interpretation** | Multiple incompatible interpretations, all empirically equivalent | Underdetermination (05); collapse vs. Many-Worlds vs. Bohm |
| **Arrow of time** | Fundamental laws time-symmetric; experience isn't | Past Hypothesis + statistical mechanics |
| **Species concept** | 22+ definitions, no consensus | Biological vs. phylogenetic vs. ecological concepts |
| **Adaptation** | Not every trait is an adaptation; spandrels exist | Gould/Lewontin; selected-effects vs. Cummins function |
| **Economic models** | Known-false assumptions; predictive success | Friedman instrumentalism; idealization types |
| **Folk psychology** | Beliefs/desires real or eliminable? | Churchland vs. Fodor; functionalism |
| **Computational mind** | Is mind a Turing machine? | Church-Turing; LOTH; Penrose-Lucas |

---

## Common Confusion Points

**QM interpretation is not about understanding the math**: The formalism (Hilbert space, operators, Born rule) is not in dispute. Every physicist can do the calculations. The dispute is about what the formalism *means* — what the world is like if QM is correct.

**Many-Worlds is testable (in principle)**: The complaint that Many-Worlds is untestable is not quite right. If the many branches exist and interfere with each other under some conditions, that interference is observable — quantum erasure experiments are evidence for branch structure. The question is whether the existence of other branches (when they don't interfere with us) is confirmed by evidence. Underdetermination applies here: it is empirically equivalent (when branches decohere) to collapse interpretations.

**"Arrow of time" is different from the direction of time**: Time may have a direction (from past to future) but the asymmetry we experience (entropy increase, memory of past not future) requires explanation. The direction of time may be fundamental; the asymmetry of our experience requires the Past Hypothesis.

**The Penrose-Lucas argument is rejected by most logicians**: It depends on confusing semantic truth-recognition with provability within a system. Humans cannot actually recognize the Gödel sentence for their own cognitive system as true — they would need to know their system is consistent, which is itself unprovable.
