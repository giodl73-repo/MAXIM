# Cognitive Science — Overview

## The Big Picture

Cognitive science is a deliberately multi-disciplinary field. No single parent discipline owns it. The founding premise (1956–1980): mental life can be studied scientifically by treating cognition as *information processing*.

```
+------------------------------------------------------------------+
|                  COGNITIVE SCIENCE HEXAGON                        |
|                                                                  |
|              PHILOSOPHY                                           |
|            (mind, logic,                                          |
|             consciousness)                                        |
|                  /\                                               |
|                 /  \                                              |
|                /    \                                             |
|   LINGUISTICS ------  PSYCHOLOGY                                  |
|  (language,    \    /  (behavior,                                 |
|   syntax,       \  /   cognition,                                 |
|   semantics)     \/    development)                               |
|                  |                                                |
|         NEUROSCIENCE  COMPUTER SCIENCE                            |
|        (brain mechanisms) (computation,                           |
|              \         AI, algorithms)                            |
|               \            /                                      |
|         ANTHROPOLOGY (culture, evolution,                         |
|                      cross-cultural cognition)                    |
+------------------------------------------------------------------+
```

**What holds it together**: Marr's three-level framework — the same question asked at three different layers of analysis.

---

## Marr's Three Levels (The Organizing Framework)

David Marr (1982, "Vision") gave the field its methodological backbone. *Every* cognitive system can be analyzed at three levels:

```
+---------------------------------------------------------------+
|  LEVEL              QUESTION           EXAMPLE (Vision)       |
+---------------------------------------------------------------+
|  COMPUTATIONAL    What does the       Recover 3D structure    |
|  (the "what")     system compute?     from 2D retinal input   |
|                   What is the goal?                            |
+---------------------------------------------------------------+
|  ALGORITHMIC      How does it         Edge detection,         |
|  (the "how")      compute it?         stereo matching,        |
|                   What                Primal sketch           |
|                   representations     algorithms              |
|                   and processes?                               |
+---------------------------------------------------------------+
|  IMPLEMENTATIONAL How is it           Retinal ganglion        |
|  (the "in what")  physically          cells, V1 simple        |
|                   realized?           cells, cortical         |
|                   What hardware?      columns                  |
+---------------------------------------------------------------+
```

**Why this matters**: Levels are *largely independent*. The same computational-level theory can be implemented in neurons, silicon, or rules. Cognitive science often proceeds at the algorithmic level without committing to implementation. Neuroscience primarily works at the implementational level. AI/CS works mostly at the computational + algorithmic levels.

**The key insight**: You can't explain *why* a system does what it does purely from the hardware. You need all three levels.

---

## The Cognitive Revolution (1956)

Three papers, one conference, one year:

```
BEFORE 1956                          AFTER 1956
+---------------------------+        +---------------------------+
| BEHAVIORISM               |        | COGNITIVISM               |
| (Watson, Skinner)         |        |                           |
|                           |        |                           |
| Mind = black box          |   -->  | Mind = information        |
| Only behavior is          |        | processing system         |
| observable/scientific     |        |                           |
| S → R (stimulus-response) |        | S → [internal            |
|                           |        |  representations +        |
| 40 years of reinforcement |        |  processes] → R           |
| schedules                 |        |                           |
+---------------------------+        +---------------------------+
```

**The three founding moments**:

| Date | Event | Significance |
|------|-------|-------------|
| April 1956 | Dartmouth AI Conference | "Artificial intelligence" coined; Newell+Simon present Logic Theorist |
| September 1956 | MIT Symposium on Information Theory | Miller presents "The Magical Number Seven"; Chomsky presents critique of finite-state grammars |
| 1957 | Chomsky's review of Skinner's "Verbal Behavior" | Demolished behaviorist account of language; showed grammar requires internal structure |

**George Miller (1956)**: Working memory capacity ≈ 7 ± 2 *chunks*. (Later revised: ~4 chunks, or ~3-4 items without chunking.)

**Newell & Simon's Logic Theorist**: A computer program that proves mathematical theorems by search. First demonstration that machines could do symbolic reasoning — and that programs could be *psychological theories*.

**Chomsky's critique of Skinner**: Language is not learned by reinforcement alone. Children acquire rules, not sequences. The stimulus-response framework cannot account for productivity (infinite sentences from finite rules) or the poverty of the stimulus (children know things they weren't taught).

---

## The Computer Metaphor for Mind

The founding metaphor: **mind is to brain as software is to hardware**.

```
+-----------------------------+-----------------------------+
|  COMPUTER                   |  MIND                       |
+-----------------------------+-----------------------------+
|  Hardware (CPU, RAM)        |  Brain (neurons, circuits)  |
|  Operating system           |  Cognitive architecture     |
|  Programs                   |  Mental processes           |
|  Data structures            |  Mental representations     |
|  Input/output               |  Perception/behavior        |
|  Algorithms                 |  Cognitive strategies       |
|  Symbol manipulation        |  Thinking                   |
+-----------------------------+-----------------------------+
```

**The functionalist claim**: What matters is the *functional organization*, not the substrate. Pain is the functional state that is caused by damage and causes avoidance behavior — same function, different implementation (neurons vs silicon).

**What this bought**:
- Legitimized talking about mental representations
- Provided precise formal models (production systems, connectionist networks)
- Linked psychology to computer science

**What this misses** (see 4E cognition below):
- The body shapes cognition (not just executes it)
- Emotions are not just output labels
- Context and culture aren't input parameters
- Real-time, embodied action doesn't match batch-processed symbolic computation

---

## 4E Cognition — The Challenge to the Computer Metaphor

Starting ~1990s, a cluster of critiques:

```
+------------------------------------------------------------------+
|  4E COGNITION                                                    |
+------------------------------------------------------------------+
|                                                                  |
|  EMBODIED           Body shape, sensorimotor capacities,         |
|                     and muscle-memory constitute cognition.      |
|                     Example: concepts of "grasping" are          |
|                     grounded in hand-action systems.             |
|                     (Varela, Thompson, Rosch — "The Embodied     |
|                     Mind" 1991; Lakoff & Johnson)                |
|                                                                  |
|  EMBEDDED           Cognition is always in an environment that   |
|                     scaffolds it. Humans offload to environment  |
|                     constantly (notepads, calendars, signs).     |
|                     (Hutchins — distributed cognition)           |
|                                                                  |
|  EXTENDED           Cognitive processes extend beyond skull      |
|                     and into tools and environment.              |
|                     Otto notebook thought experiment:            |
|                     if Otto uses notebook as memory, his         |
|                     beliefs are partly external.                 |
|                     (Clark & Chalmers 1998)                      |
|                                                                  |
|  ENACTED            Cognition is not representation of a         |
|                     pre-given world. It is the bringing-forth    |
|                     of a world through sensorimotor activity.    |
|                     (Merleau-Ponty tradition; Varela)            |
+------------------------------------------------------------------+
```

**Where the field stands**: Neither pure symbol-manipulation nor pure embodied enactivism. Current mainstream: **predictive processing / active inference** (Friston, Clark) attempts a synthesis — brain predicts its sensory input, and action reduces prediction error. This is simultaneously computational (Marr level 2) and embodied (action is part of inference).

---

## Field Map — What's in This Series

```
+------------------------------------------------------------------+
|  COGNITIVE-SCIENCE MODULE MAP                                    |
+------------------------------------------------------------------+
|                                                                  |
|  CORE PROCESSES              THEORY + META                       |
|  ─────────────               ────────────                        |
|  01-PERCEPTION               07-CONSCIOUSNESS                    |
|     visual/auditory/multi-      hard problem, GWT, IIT, PP       |
|     sensory + change blindness                                   |
|                              08-COMPUTATIONAL-MODELS             |
|  02-ATTENTION-MEMORY            GPS/ACT-R, connectionism,         |
|     filter models, Baddeley,    Bayesian brain, RL + dopamine,   |
|     LTM taxonomy, false mem     embodied cognition               |
|                                                                  |
|  03-REASONING-JUDGMENT       APPLIED                             |
|     dual-process, biases,    09-APPLIED-BRIDGE                   |
|     prospect theory             HCI/UX, learning science,        |
|                                 engineering biases,              |
|  04-LANGUAGE-THOUGHT            replication crisis               |
|     Broca/Wernicke, Sapir-                                       |
|     Whorf, concepts, LoT     DEVELOPMENT                         |
|                              06-DEVELOPMENT                      |
|  05-PROBLEM-SOLVING             Piaget, Vygotsky, ToM,           |
|     problem space, insight,     marshmallow replication          |
|     chunking, creativity,                                        |
|     flow                                                         |
+------------------------------------------------------------------+
```

**Cross-references**:
- `neuroscience/` — implementational-level details (neurons, circuits, systems)
- `ai-engineering/` — where cognitive models become AI systems
- `linguistics/` (Session 12) — language processing in depth
- `philosophy/` (planned) — consciousness, philosophy of mind, epistemology

---

## Historical Arc — Four Waves

| Wave | Period | Dominant Paradigm | Key Figures |
|------|--------|------------------|-------------|
| **1. Cognitive revolution** | 1956–1970 | Symbolic information processing | Miller, Newell, Simon, Chomsky |
| **2. Connectionism** | 1985–2000 | Neural networks, distributed representation | Rumelhart, McClelland, Hinton |
| **3. Embodiment + Dynamics** | 1990–2010 | 4E cognition, dynamical systems | Varela, Brooks, Thelen |
| **4. Predictive processing** | 2010–present | Bayesian brain, active inference | Friston, Clark, Dehaene |

**Note**: These waves didn't replace each other — they coexist and debate. Symbolic models (ACT-R) are still heavily used. Deep learning is the grandchild of connectionism. Bayesian models are partly continuous with rationalist cognitive science. The debate about what cognition fundamentally *is* remains open.

---

## Key Concepts Glossary

| Term | Definition |
|------|-----------|
| **Cognition** | Mental processes: perception, attention, memory, reasoning, language, problem-solving |
| **Representation** | An internal state that stands for something else (a symbol, an image, a distributed pattern) |
| **Process** | Operations over representations (search, matching, transformation, retrieval) |
| **Mental model** | A working simulation of a situation used to reason and predict |
| **Module** | A domain-specific, informationally encapsulated cognitive system (Fodor) |
| **Heuristic** | A fast, efficient cognitive shortcut — usually good, sometimes wrong |
| **Executive function** | Top-down control: inhibition, working memory, cognitive flexibility |
| **Metacognition** | Thinking about one's own thinking; monitoring and controlling cognition |
| **Situated cognition** | Cognition as deeply shaped by its physical and social context |

---

<!-- @editor[bridge/P1]: Missing Turing Test → computability bridge for this learner. The overview introduces the "computer metaphor for mind" without noting that the Turing Test is a decidability question in disguise: behavioral indistinguishability = membership in a language. A reader from MIT TCS sees this immediately and it earns credibility. Add 2-3 sentences connecting the Church-Turing thesis to functionalism, and note where this breaks down (Searle's Chinese Room, Penrose). -->

<!-- @editor[bridge/P1]: The four-waves table (Symbolic → Connectionist → Embodied → Predictive) maps directly onto the GOFAI vs connectionism debate this learner knows cold. No bridge is drawn. Add a row or note explicitly linking Wave 1 = GOFAI/production systems, Wave 2 = connectionist resurgence (this learner likely remembers the 1986 PDP books), and note that Wave 4 (predictive processing / Friston) is variational inference — the same ELBO they've seen in VAEs. This bridge is load-bearing for 08-COMPUTATIONAL-MODELS. -->

## Decision Cheat Sheet — Which Framework for Which Question?

| Question | Best Framework | Where in This Series |
|----------|---------------|---------------------|
| What does a cognitive system compute? | Marr computational level | Throughout |
| How does the brain implement memory? | Neuroscience / implementational | neuroscience/ |
| Why do people make bad decisions? | Dual-process + heuristics/biases | 03-REASONING-JUDGMENT |
| Is consciousness a physical process? | Hard problem / GWT / IIT | 07-CONSCIOUSNESS |
| How do children develop reasoning? | Piaget + Vygotsky + ToM | 06-DEVELOPMENT |
| How does language affect thought? | Sapir-Whorf empirical data | 04-LANGUAGE-THOUGHT |
| Why are experts fast? | Chunking + deliberate practice | 05-PROBLEM-SOLVING |
| How should I design a UI? | Cognitive load, Fitts, Hick | 09-APPLIED-BRIDGE |
| Does the brain compute Bayesian inference? | Predictive processing | 08-COMPUTATIONAL-MODELS |

---

<!-- @editor[structure/P2]: Decision Cheat Sheet guides to specific sub-modules but doesn't help the learner decide *which computational framework* to use for a given modeling question (GPS/SOAR vs connectionist vs Bayesian vs active inference). This is the most likely question a VP-Engineering-turned-AI-enthusiast brings to the overview. Add a "choose your modeling framework" row or a separate mini-table. -->

## Common Confusion Points

**"Cognitive science" vs "cognitive psychology"**: CogSci is the interdiscipline; cognitive psychology is the psychology sub-field that focuses on perception, memory, attention, reasoning. CogSci includes philosophy, linguistics, neuroscience, and AI.

**Marr levels are independent, not a hierarchy**: Low-level doesn't mean "foundational." You can have a complete algorithmic-level theory without knowing the implementation. Many deep insights come from the computational level (e.g., Bayesian perceptual models) without specifying neurons.

**Modularity debate**: Fodor's "Modularity of Mind" (1983) claimed input systems (vision, language) are modular (domain-specific, informationally encapsulated, fast) but central cognition is not. Neural network approaches see less sharp boundaries. The debate continues — fMRI shows domain-specificity, but also massive cross-domain connectivity.

**Symbol vs connectionism is not resolved**: Deep learning is not "the solution" to the symbol/sub-symbol debate. It handles pattern recognition magnificently; it still struggles with systematic generalization, compositionality, and causal reasoning in the way symbolic systems do. This is exactly what Fodor & Pylyshyn predicted would be hard.

**4E cognition vs computational cognition**: These are not necessarily opposed. Predictive processing / active inference (Friston) is *both* computational (it's formal Bayesian inference) *and* embodied (action is part of inference, not separate output). The divide is less sharp than the 1990s polemics suggested.
