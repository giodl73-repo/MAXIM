# Computational Models of Cognition — Cognitive Science

## The Big Picture

Computational models of cognition attempt to specify the algorithms and representations underlying mental processes precisely enough to implement and test them. This module traces four generations of models and their ongoing debates.

```
+------------------------------------------------------------------+
|  COMPUTATIONAL MODELING: FOUR GENERATIONS                        |
+------------------------------------------------------------------+
|                                                                  |
|  1950s-70s: SYMBOLIC AI          →  GPS, SOAR, production systems|
|  Mind as symbol manipulator         ACT-R, LISP programs         |
|                                                                  |
|  1985-2000: CONNECTIONISM        →  PDP, backprop, distributed   |
|  Mind as neural network             representations              |
|                                                                  |
|  1990-2010: EMBODIED/DYNAMIC     →  Robot cognition, dynamical   |
|  Mind as sensorimotor system        systems theory               |
|                                                                  |
|  2010-now: BAYESIAN/PREDICTIVE   →  Bayesian models, free energy,|
|  Mind as inference engine           active inference             |
+------------------------------------------------------------------+
```

The debate is not settled. Elements from all four generations are active in current cognitive science.

---

## Symbolic AI — The First Generation

### General Problem Solver (GPS) (Newell & Simon 1957)

The first computational cognitive model. A program that solves problems by means-ends analysis.

```
ARCHITECTURE:
  Problem Space:
    Objects (states)
    Operators (actions)
    Desired state (goal)

  Means-Ends Analysis:
    1. Detect difference between current and goal state
    2. Find operator that reduces biggest difference
    3. Apply (recursively if preconditions not met)
    4. Repeat until goal state reached

  THINK-ALOUD PROTOCOLS:
    Newell & Simon had humans solve problems while thinking aloud
    Transcripts matched GPS trace closely
    → first quantitative test of a cognitive model
```

**Legacy**: Problem space formalism is still standard. Means-ends analysis is observed across species. The key insight: cognition can be *described as computation* — and that description can be tested against behavioral data.

### SOAR (Laird, Newell, Rosenbloom 1987)

A **unified cognitive architecture** — one integrated theory of all cognition, not just problem-solving.

```
SOAR ARCHITECTURE:
  Working Memory:
    Current state + goals + operators

  Long-Term Memory:
    Procedural: production rules (IF-THEN)
    Declarative: episodic + semantic chunks
    Spatial: visuospatial imagery

  Decision Cycle:
    1. ELABORATE: apply all matching rules
    2. DECIDE: select best operator (or form subgoal if impasse)
    3. APPLY: execute selected operator

  CHUNKING:
    When a subgoal is solved, the successful path
    is compiled into a new production rule (chunk)
    → procedural learning
    → explains expertise (Chase & Simon chess data)
```

**Key property**: SOAR explains *learning* via chunking — the same process that explains chess expertise emerges from the architecture.

**Rules engine connection**: SOAR's production rules are structurally identical to rules engines used in enterprise software (Drools, CLIPS, OPS5). The RETE algorithm that optimizes rule matching in these systems was designed for exactly this kind of production system. SOAR's decision cycle — elaborate (fire all matching rules) → decide (select operator or create subgoal) → apply — maps to the forward-chaining match-resolve-act cycle in any rules engine. The architectural choice unique to SOAR is *universal subgoaling*: when no operator can be selected (an impasse), SOAR automatically creates a subgoal to resolve the impasse. This is equivalent to choosing a conflict-resolution strategy — but SOAR's strategy is recursive (subgoals can spawn sub-subgoals), making it more expressive than the priority-based conflict resolution typical in enterprise rules engines.

### ACT-R (Anderson 1983, 1993, 2007)

The most empirically successful unified cognitive architecture. **Rational Analysis** foundation: cognitive mechanisms are near-optimal given brain's statistical environment.

```
ACT-R ARCHITECTURE:

  MODULES (each mapped to brain region):
  +──────────────────────────────────────────────────+
  | VISUAL   MANUAL   AURAL   VOCAL   IMAGINAL       |
  | (occipital) (motor) (temporal) (speech) (parietal)|
  +──────────────────────────────────────────────────+
              ↕ one chunk per cycle
  +──────────────────────────────────────────────────+
  |              CENTRAL PROCEDURAL SYSTEM           |
  |              (basal ganglia — production selection)|
  |              ~50ms per production cycle          |
  +──────────────────────────────────────────────────+
              ↕ retrieval requests
  +──────────────────────────────────────────────────+
  |         DECLARATIVE MEMORY (hippocampus)         |
  |         Activation = log(sum of uses × recency)  |
  |         Retrieval time = f(1/activation)         |
  +──────────────────────────────────────────────────+
```

**Activation equation**: A chunk's activation (probability and speed of retrieval):
```
  A_i = B_i + Σ W_j × S_ji + noise

  B_i = base-level activation (log of practice + recency)
  W_j = attention weight of goal element j
  S_ji = associative strength from j to chunk i

  → Explains spacing effect, fan effect, priming, expertise
```

**ACT-R predictions are quantitative**: Not just qualitative fits to data — millisecond-level RT predictions that match human data. One of the few theories in cognitive science with genuine predictive power.

---

## Connectionism — The Second Generation

**Rumelhart & McClelland (1986)** — "Parallel Distributed Processing" (two volumes, the PDP bible).

**Core ideas**:
1. **Distributed representation**: Concepts represented as patterns of activation across many units; no single unit = one concept
2. **Learning via backpropagation**: Adjust weights to minimize prediction error
3. **Emergent behavior**: Complex cognition from simple learning rules and units
4. **Subsymbolic**: No explicit rules or symbols — behavior emerges from statistics

```
LOCALIST vs DISTRIBUTED representation:

Localist (classical AI):
  [APPLE] ← one node, one concept

Distributed (PDP):
  APPLE = {0.8, 0.3, 0.1, 0.9, 0.2, 0.7, ...}
           activation pattern across 50 units

  ORANGE = {0.7, 0.4, 0.2, 0.8, 0.3, 0.6, ...}
            similar pattern to APPLE (similar concept)

  Properties:
    - Similarity = closeness in activation space
    - Generalization comes "for free"
    - Graceful degradation (partial damage, partial function)
    - Automatic generalization to novel inputs
```

**Key PDP results**:

**English past tense** (Rumelhart & McClelland 1986):
```
Train network on regular + irregular verbs.
Network produces "wented" for "went" (overgeneralization)
before mastering irregular.
This U-shaped learning curve was seen as evidence for
implicit learning without explicit rules.
But: it also makes quantitative errors classical grammar doesn't.
Debate: does it really model what children do?
```

**TRACE model** (McClelland & Elman 1986): Connectionist model of speech perception. Feature → phoneme → word levels with top-down and bottom-up connections. Accounts for phoneme restoration effect (hear context-appropriate phoneme even when replaced by noise), lexical influence on phoneme perception.

**IAC (Interactive Activation and Competition)** (McClelland & Rumelhart 1981): Word recognition. Letter features activate letters; letters activate words; words feed back to letters. Explains word superiority effect (letters in words recognized faster than isolated letters).

---

## The Symbol vs Sub-Symbol Debate

**Fodor & Pylyshyn (1988)** — "Connectionism and Cognitive Architecture: A Critical Analysis":

**Two key properties of human thought that connectionism must explain**:

1. **Systematicity**: If you can think "John loves Mary" you can think "Mary loves John." Thought comes in structurally related families. This requires explicit compositional structure — symbols combined by rules.

2. **Productivity**: Humans can produce and understand infinitely many novel sentences/thoughts. Requires recursive generative rules.

```
Fodor & Pylyshyn's claim:
  These properties are ARCHITECTURAL — they come from the
  explicit combinatorial structure of the representational system.

  Connectionists would need to "implement" a symbolic system
  to get these properties — they can't emerge from the statistics.
  At best, connectionism is an implementation story
  (Marr: implementational level), not an algorithmic story.
```

**Connectionist responses**:
- **Smolensky (1990)**: Tensor product representations can exhibit systematicity without discrete symbols
- **Empirical success**: Neural networks *do* learn linguistic structure (word2vec, BERT, GPT-4) — what does this prove about systematicity?
- **Large language models**: Appear to exhibit productivity and systematicity in practice — but compositionality and systematic generalization remain active research problems

**Current status** (2025): Deep learning handles distributional semantics brilliantly; still fails on:
- Out-of-distribution systematic generalization (SCAN benchmark)
- Compositional novel concept learning (Lake's Omniglot)
- Causal/counterfactual reasoning

The debate is not resolved. It has become the core of current NLP+AI research.

**Where LLMs fail on systematicity (2023-2025 evidence)**:

| Benchmark / Finding | What It Tests | LLM Performance |
|---------------------|---------------|-----------------|
| **SCAN** (Lake & Baroni 2018) | Compositional generalization to novel command combinations | Standard seq2seq fails catastrophically on held-out compositions; meta-learning helps somewhat |
| **COGS** (Kim & Linzen 2020) | Systematic structural generalization in semantic parsing | Transformers fail on novel PP-attachment and role-binding combinations |
| **Reversal curse** (Berglund et al. 2023) | If trained on "A is B," can the model infer "B is A"? | GPT-4 and others fail — training on "Olaf Scholz is Chancellor of Germany" does NOT produce "The Chancellor of Germany is Olaf Scholz" reliably |
| **Marcus's critique** (2020+) | Systematic variable binding: "every A that R's a B, S's a C" | LLMs approximate via distributional statistics but fail on novel variable-binding patterns outside training distribution |

The pattern: LLMs handle distributional semantics and in-distribution generalization brilliantly, but systematic compositional generalization — the core of Fodor & Pylyshyn's argument — remains a genuine weakness. The debate is whether this will yield to scale (more data, larger models) or requires architectural change (hybrid neuro-symbolic systems, structured attention).

---

## Bayesian Brain and Predictive Coding

### Bayesian Models of Perception

The starting insight: perception is *inverse inference*. Given sensory data, infer the most probable world state that caused it.

**Bayesian perceptual model**:
```
  Posterior ∝ Likelihood × Prior

  P(world | sensory data) ∝ P(sensory data | world) × P(world)

  Perception = most probable world given data AND priors
```

**Ernst & Banks (2002)**: Combined visual and haptic size judgments are near-optimal maximum likelihood estimates. Humans *actually* weight cues by their inverse variance — the Bayesian prediction. This is the strongest empirical support for the Bayesian brain hypothesis.

**Weiss, Simoncelli & Adelson (2002)**: Motion illusions arise from Bayesian integration of motion signals with a prior for slow motion. The "Bayesian brain" makes specific, correct predictions about which illusions occur and when.

### Predictive Coding (Rao & Ballard 1999)

Implements Bayesian inference in neural architecture:

```
HIERARCHY:
  Higher cortical area:   Prediction (top-down)
                              ↕
  Lower cortical area:    Prediction error (bottom-up)

  Process:
  1. Higher area sends PREDICTION of lower area activity
  2. Lower area computes: actual input - prediction = ERROR
  3. Only ERROR (surprise) is sent upward — not the raw signal
  4. Higher area updates its model to reduce error

  Key: The bulk of corticocortical connections are FEEDBACK.
  These are the prediction signals. Feedforward = prediction errors.
```

**What this explains**:
- Attention: increases precision weighting on errors in attended locations
- Perception: what we see is the prediction, only error signals get updated
- Surprise: large prediction error = salient, conscious, noticeable
- Hallucination: top-down predictions dominate, errors suppressed (weak data weighting)
- Psychedelics: disrupt precision weighting → errors flood consciousness → dissolved world model

## Engineering Bridge: Free Energy as the ELBO

```
FRISTON'S FREE ENERGY              ML / VARIATIONAL INFERENCE EQUIVALENT
──────────────────────────────────────────────────────────────────────────────
Free energy F                       Negative ELBO: F = -ELBO
  F = KL[Q(θ) || P(θ|data)]        KL divergence between approximate
      - log P(data)                 posterior Q and true posterior P
                                    Plus the negative log-evidence

Generative model P(data|θ)          VAE decoder
  Brain's model of how hidden       Maps latent variables to predicted
  causes θ produce sensory data     observations

Recognition model Q(θ|data)         VAE encoder
  Brain's approximate posterior     Maps observations to approximate
  over hidden causes                posterior over latents

Minimizing F by updating Q          Training the encoder
  = perceptual inference            = amortized variational inference

Minimizing F by updating P          Training the decoder
  = learning (synaptic plasticity)  = improving the generative model

Minimizing F by changing data       NO DIRECT ML ANALOG (this is new)
  = active inference (action)       Agent changes the world to make
                                    observations match predictions
                                    — this is what distinguishes
                                    Friston from standard VI
```

The key insight: the ELBO from variational autoencoders is *exactly* Friston's free energy with opposite sign. Maximizing ELBO = minimizing free energy. The brain runs approximate variational inference where perception is the E-step (update Q), learning is the M-step (update generative model parameters), and active inference is the genuinely novel addition — the agent acts on the world to reduce prediction error rather than only updating internal beliefs. This is why predictive processing is simultaneously a theory of perception (updating Q), learning (updating P), and action (changing data).

### Free Energy Principle (Friston 2005+)

**Unifies perception + action + learning + attention in one formalism**:

```
FREE ENERGY (F) ≈ surprise (negative log evidence)
                = Kullback-Leibler divergence between
                  internal model Q(θ) and true posterior P(θ|data)

Minimizing F:
  - Updates the model (perception / learning)
  - Changes the world to match the model (action)

Biological systems minimize F by:
  PERCEPTUAL INFERENCE: update beliefs to match sensory input
  ACTIVE INFERENCE: act to bring sensory input in line with
                    prior beliefs (predictions about desired states)
```

**Active inference**: Action is not chosen to *maximize reward* (RL formulation) but to *minimize expected free energy* — fulfill predicted sensations. This unifies perception and action without a separate reward function. Homeostasis is "predicted" sensory state.

---

## Reinforcement Learning as Cognitive Model

The biggest neuroscience-AI success story.

### Rescorla-Wagner Model (1972)
Classical conditioning: learning to predict US (unconditioned stimulus) from CS (conditioned stimulus).

```
ΔV(CS) = αβ(λ - ΣV)

  V(CS) = associative strength of CS
  λ = maximum conditioning (when US occurs)
  αβ = learning rate parameters
  ΣV = total prediction by all present CSi

Key: learning stops when total prediction = actual outcome
→ blocking effect: if CS1 already predicts US, adding CS2 → no learning of CS2
```

### TD Learning (Sutton & Barto 1988)
Extends Rescorla-Wagner to *temporal* predictions:

```
δ(t) = r(t+1) + γV(t+1) - V(t)

  δ = temporal difference error
  r = reward at next time step
  γ = discount factor
  V(t) = value at current state

This is the PREDICTION ERROR:
  δ > 0: better than expected → increase V
  δ < 0: worse than expected → decrease V
  δ = 0: exactly as expected → no change
```

### Dopamine = Prediction Error Signal (Schultz 1997)

```
EARLY LEARNING:
  Reward →          Dopamine burst (reward itself surprising)

AFTER CONDITIONING:
  CS (tone) →       Dopamine burst (CS now predicts reward)
  Reward →          No dopamine burst (reward was predicted)
  Expected reward
  doesn't arrive →  Dopamine DIP below baseline

Prediction:
  Dopamine firing = TD prediction error δ(t)

  Schultz recorded monkey dopamine neurons during
  classical conditioning → exactly matched TD learning curve
```

**Why this is important**: It's a direct bridge between computational RL theory, behavior (conditioning), and neural mechanism (dopamine). One of the cleanest Marr-level analyses in neuroscience. Explains drug addiction (drugs directly activate dopamine = false prediction error, system "learns" drugs are valuable independent of normal learning).

---

## Embodied Cognition — The Challenge

**Varela, Thompson & Rosch — "The Embodied Mind" (1991)**:

The classic AI/cognitive science view: mind processes *representations* of the world. The body is just I/O.

**Embodied cognition**: The body *constitutes* cognition, not just executes it.

```
CLASSIC VIEW:                 EMBODIED VIEW:
  Brain → representation of    Sensorimotor loops
  world → action                constitute concepts

  Example: "left" is an        "Left" is anchored to
  arbitrary symbol             body's left-hand side,
                               grasping, spatial
                               orientation

  Color perception = cone      Color categories
  wavelength responses         reflect body's need to
                               discriminate actionable
                               surfaces
```

**Barsalou's "Perceptual Symbol Systems" (1999)**:
- Concepts are grounded in modality-specific *simulations* (motor, visual, tactile, affective)
- Thinking about a hammer activates motor cortex (hammer-grasping)
- Thinking about a lemon activates gustatory cortex
- Concepts are not amodal symbols — they are *re-enactments* of sensorimotor experience

**Evidence**:
- "ACE inhibitor" → clinical students' motor cortex activates (associated with swallowing action)
- Color knowledge activates color areas even in verbal tasks
- Motor cortex damage can impair understanding of action words

**Critique from Mahon & Caramazza**: Activation of sensorimotor areas during conceptual tasks may be *epiphenomenal* or *downstream* — the concept is represented amodally; sensorimotor areas are recruited for elaboration, not core representation.

### Extended Mind (Clark & Chalmers 1998)

**Parity principle**: If a process outside the brain, when performed by the brain, would be counted as cognitive, then it IS cognitive.

**Otto notebook thought experiment**:
```
Otto has Alzheimer's. He carries a notebook where he writes
information he would otherwise remember.
Otto uses the notebook functionally identically to how
Inga uses her hippocampus.
Claim: the notebook IS Otto's memory — literally.
Otto's beliefs are partly constituted by the notebook's contents.
```

**Implication**: The boundary of "the mind" is not the skull. Phones, computers, language, institutions can be *literally* part of cognitive systems.

**Response from critics**: There's a disanalogy — memory in the head is automatically available; the notebook requires an extra step. Also, the notebook can be stolen, altered, lost — the causal coupling isn't right.

---

## Decision Cheat Sheet

| Model | What it's good for | What it misses |
|-------|------------------|----------------|
| **ACT-R** | Quantitative RT predictions, learning curves, dual task | Embodied processes, large-scale language |
| **SOAR** | Problem solving, learning, unified theory | Emotion, development, detailed perception |
| **Connectionist** | Pattern recognition, statistical learning, distributional semantics | Systematic generalization, compositionality |
| **Bayesian** | Perception, cue integration, rational behavior | Computational intractability for large models |
| **Predictive coding** | Visual perception, attention, hallucination, psychedelics | Action, social cognition |
| **RL/TD learning** | Instrumental learning, addiction, dopamine signal | Planning, model-based reasoning |
| **Embodied** | Action-oriented concepts, metaphor, grounded language | Abstract thought, mathematics |

---

## Common Confusion Points

**Connectionism ≠ deep learning**: PDP connectionism (1986) and modern deep learning are related but not the same. Modern deep learning has much larger architectures, better optimizers, and is trained on vastly more data. The theoretical debates (systematicity, compositionality) apply with equal force to GPT-4 as to the original PDP networks.

**Bayesian brain ≠ brain does exact Bayesian inference**: Real Bayesian inference is computationally intractable for complex environments. The claim is that the brain *approximates* Bayesian inference, or implements it for specific restricted domains. The debate is whether the approximation is good enough to explain behavior.

**Free energy ≠ thermodynamic free energy**: Friston's free energy is a mathematical quantity from variational Bayes (specifically the ELBO — evidence lower bound from variational inference). The name is analogous, not identical, to physical free energy.

**"Attention" in transformers ≠ attention in cognitive science**: Transformer self-attention (Q, K, V matrices) computes a globally parallel, soft-weighted sum over all positions. Cognitive attention (Treisman, Posner) is serial, capacity-limited, and spotlight-like — it selects a subset of inputs and suppresses the rest. The shared name is historical accident. Transformer attention is closer to *content-addressable memory lookup* than to cognitive attention. The practical confusion: LLM practitioners sometimes claim their models "attend" to inputs in a psychologically plausible way. They don't — transformer attention has no capacity bottleneck, no serial scanning, and no attentional blink. The cognitive bottleneck is *why* working memory is limited; transformer attention has no such constraint.

**ACT-R ≠ brain mapping**: ACT-R's module-to-brain-region mapping (e.g., production system = basal ganglia) is a hypothesis that has been tested with fMRI — with reasonable but imperfect success. The mapping is informed by, not proved by, the fMRI data.

**Cross-reference**: For the neural implementation of RL (dopamine, basal ganglia, OFC), see `neuroscience/03-COGNITION-COMPUTATION.md`. For AI applications of these models (LLMs, RL agents), see `ai-engineering/04-AGENTS.md`. For search algorithms underlying GPS/SOAR, see `computing/26-ALGORITHMS.md`.
