# Consciousness — Cognitive Science

## The Big Picture

Consciousness is the problem that won't go away. Every other cognitive phenomenon — perception, memory, attention, language — can in principle be explained as information processing: describe the inputs, the representations, the computations, the outputs. Consciousness adds something else: *why is there anything it is like to undergo those processes at all?*

```
+------------------------------------------------------------------+
|  THE CONSCIOUSNESS LANDSCAPE                                     |
+------------------------------------------------------------------+
|                                                                  |
|  EASY PROBLEMS             HARD PROBLEM (Chalmers 1995)          |
|  (not actually easy)                                             |
|  ─────────────────         ──────────────────────────────────    |
|  Explain the functions      Explain why physical processing      |
|  of consciousness:          is accompanied by subjective         |
|                              experience at all.                  |
|   - Ability to report       "Even if we solved every easy        |
|     mental states            problem, we would still not         |
|   - Access to information    have explained why there is         |
|   - Sleep/wake control       something it is like to be          |
|   - Attention control        processing that information"        |
|   - Integration of                                               |
|     information             This is the "explanatory gap"        |
|                             (Levine 1983)                        |
|  These are scientific                                            |
|  problems with tractable    This may require new science,        |
|  empirical research         or may be a conceptual illusion      |
|  programs                   (Dennett, Frankish)                  |
+------------------------------------------------------------------+
```

**Chalmers (1995)**: Hard problem survives *even if* we give a complete functional account. You can explain why a system *reports* having experiences, can *integrate* information, can *attend* — and still not explain why it *feels like something*.

**Dennett's reply** (Consciousness Explained, 1991): The hard problem is a "philosopher's zombie" — a conceptual error. There *is* no further fact beyond the functional facts. If you explain all the easy problems, you've explained consciousness; the rest is confused phenomenology.

---

## Philosophical Background

### Qualia and Mary's Room

**Qualia**: The intrinsic qualitative character of conscious experience. The *redness* of red, the *painfulness* of pain, the *smell* of coffee. Something over and above the physical/functional description.

**Mary's Room** (Jackson 1982):
```
Mary the neuroscientist knows EVERYTHING about color vision:
  - Every wavelength response function of cones
  - Every neural pathway from retina to V4 to IT
  - Every algorithm the brain uses to compute color constancy
  - Every behavior difference between people viewing red vs green
  - All of this known while locked in a black-and-white room

Question: When Mary leaves the room and sees RED for the first time,
does she learn something new?

Intuitive answer: YES — she learns what red looks LIKE.
Implication: There is phenomenal knowledge not captured by
physical/functional knowledge → physicalism is false.

Dennett's reply: No, Mary doesn't learn anything new.
She merely has a new ability (to recognize and remember red).
"Ability hypothesis" (Lewis, Nemirow).
```

### Philosophical Zombies

**P-zombies** (Chalmers): Beings physically and functionally identical to us — same brain, same behavior, same functional organization — but with *no inner experience*. Dark inside.

- Are they *conceivable*? Yes (we can describe them consistently).
- Does conceivability imply possibility? Chalmers: yes → physicalism is false.
- Dennett: P-zombies aren't genuinely conceivable once you think carefully. You can't have all the functional properties without the experience — the experience *is* the function.

**The Chinese Room** (Searle 1980): A person in a room follows rules to respond to Chinese symbols without understanding Chinese. Even if the *system* passes the Turing test, the *person* doesn't understand. Therefore: syntax (symbol manipulation) ≠ semantics (meaning/understanding).

Implication: No computational system has genuine understanding — only *simulated* understanding.

---

## Global Workspace Theory (GWT)

**Baars (1988)**; Dehaene & Changeux ("global neuronal workspace"):

```
                 SPECIALIZED MODULES
      ┌──────────────────────────────────┐
      │  Vision   Auditory  Language   │
      │  Memory   Emotion   Motor      │
      └──────────────┬───────────────┘
                     │ compete for access
                     ▼
         ┌───────────────────────────────┐
         │    GLOBAL WORKSPACE           │
         │   (conscious access)          │
         │                               │
         │   When a module "wins" and    │
         │   broadcasts to the global    │
         │   workspace, its content      │
         │   becomes CONSCIOUS and is    │
         │   available to all other      │
         │   modules                     │
         └───────────────────────────────┘
                     │ broadcast
                     ▼
         All specialized modules receive
         the broadcast → global availability
```

**Neural correlate** (Dehaene et al.):
- **Fronto-parietal network** + **long-range cortico-cortical connections**
- Conscious access: late (~300ms), large-amplitude, widespread activation — an "ignition"
- Unconscious processing: local, early, specialized
- Late amplification wave (P3b ~300-400ms) = consciousness signature

**Empirical evidence**:
- Binocular rivalry: alternating percepts correlate with fronto-parietal ignition
- Masking: unmasked stimuli ignite; masked ones don't — even if early processing is identical
- Anesthesia: loss of consciousness correlates with loss of long-range cortical connectivity

**What GWT explains well**: Access consciousness (what's available for report, reasoning, verbal report). What it *doesn't* explain: why the "winning" broadcast is accompanied by phenomenal experience (the hard problem).

---

<!-- @editor[bridge/P2]: Global Workspace Theory is presented as a cognitive architecture with a "broadcast" mechanism, but the connection to software architecture is not made. GWT is structurally identical to a message bus / publish-subscribe system: specialized modules are subscribers, the global workspace is the shared bus, and "ignition" is a broadcast event. The fronto-parietal network is the bus controller. For a software architect this is the immediately graspable framing — and it raises the right question: what's the routing/arbitration policy? (attention = priority queue). Make this explicit. -->

## Integrated Information Theory (IIT)

**Tononi (2004, 2008, 2014)**:

**Core claim**: Consciousness = **phi (Φ)** = the amount of integrated information in a system.

```
Phi measures: How much information is generated by the system
              AS A WHOLE, over and above the information
              generated by its parts independently.

High phi: Each part's activity depends on all other parts
          (highly integrated, not decomposable)

Low phi:  Parts can be understood independently
          (feedforward network: Φ = 0)
          (XOR gate: surprisingly high Φ)
          (simple reflex arc: low Φ)
```

**Mathematical framework**:
- Identify the "minimum information partition" — the weakest conceptual cut through the system
- Phi = information that would be lost if the system were cut at that partition
- A system is conscious iff Φ > 0

**Implications**:
- **Panpsychism**: Any system with Φ > 0 is conscious. A thermostat has tiny but nonzero Φ.
- **Feedforward networks have Φ = 0**: A purely feedforward neural network (like a standard convolutional net) has zero phi — no feedback, no integration across time. This implies current AI systems are not conscious.
- **Cerebellum has very low Φ**: Despite having more neurons than cerebral cortex, the cerebellum has highly regular, parallel, largely feedforward organization → low Φ → predicts: damage to cerebellum doesn't impair consciousness (correct clinically).
- **Cerebral cortex has high Φ**: Dense recurrent connectivity → high integration.

**Criticisms**:
- XOR circuit has high phi but we don't think it's conscious
- Φ is computationally intractable to calculate for anything larger than toy systems
- IIT is unfalsifiable in practice
- Scott Aaronson (CS): IIT leads to absurd conclusions about large grids of logic gates

<!-- @editor[bridge/P2]: Aaronson's critique is mentioned but not given the weight it deserves for a CS reader. Aaronson showed that IIT implies a large 2D grid of XOR gates would have astronomical Φ and thus extremely high consciousness — which most people find absurd. His blog post "Why I Am Not An Integrated Information Theorist" (2014) is the canonical CS-person's dissection of IIT's problems. For this learner, this is the most credible external validity check on IIT and deserves more than a single bullet. Add 2-3 sentences on the computational complexity argument specifically. -->

---

## Higher-Order Theories (HOT)

**Rosenthal (1997)**: A mental state is *conscious* iff there is a (suitably related) **higher-order representation** of that state.

```
FIRST-ORDER STATE:             HIGHER-ORDER THOUGHT:
  Visual system processes         "I am seeing red"
  red light                       (meta-representation of
  → first-order representation      the first-order state)
    of red

  This first-order state is CONSCIOUS only if there is
  a higher-order thought (HOT) accompanying it.

  If the HOT is absent: the state is unconscious
  (even if it causally affects behavior)
```

**Prediction**: Prefrontal cortex (higher-order representation) is necessary for consciousness. Local cortical damage without PFC involvement = unconscious processing.

**HOT vs GWT**: Both require "higher-level" processing for consciousness. GWT says *broadcasting* = consciousness; HOT says *meta-representation* = consciousness. Empirically, these are hard to distinguish.

---

<!-- @editor[bridge/P2]: The Predictive Processing / Free Energy section is the most important for this learner — it connects directly to variational inference in ML. Friston's free energy IS the negative ELBO from variational Bayes: F = -ELBO = KL[Q(θ)||P(θ)] - log P(data). Minimizing free energy = maximizing the evidence lower bound, the same objective used in VAEs (variational autoencoders). The brain as an approximate inference engine, using Q(θ) as the variational posterior, is a precise mapping this reader will recognize. Make this bridge explicit here and cross-reference 08-COMPUTATIONAL-MODELS. -->

## Predictive Processing and Active Inference

**Clark & Friston (2013)**:

```
BRAIN AS BAYESIAN INFERENCE MACHINE:

  TOP-DOWN PREDICTIONS              BOTTOM-UP PREDICTION ERRORS
  ─────────────────────             ─────────────────────────────
  Generative model predicts         Sensory input
  sensory input                     |
  |                                 | if mismatch:
  v                                 v   prediction error
  What I expect to see          sent UPWARD to update model
  What I expect to hear
  What my body will feel

  Perception = minimize prediction error
  (best model of causes of sensory input)

  Action = bring sensory input in line with predictions
  (active inference: move body to make predictions true)
```

**Consciousness on PP**:
- Conscious percept = the brain's best current model of the causes of its inputs
- Hallucinations = predictions without error correction (model wins over data)
- High precision weighting on predictions → illusions; high weighting on errors → hypervigilance
- Psychedelics: reduce precision of predictions → more error signals dominate → dissolution of stable world model

**Free energy principle** (Friston): The brain acts to minimize surprise (unexpectedness of sensory input) — equivalent to maintaining accurate generative models. Perception, action, attention, learning all serve this goal.

---

## Split-Brain (Gazzaniga & Sperry)

Patients with corpus callosum severed (commissurotomy, treatment for severe epilepsy):

```
LEFT HEMISPHERE               RIGHT HEMISPHERE
  - Language dominant           - Non-language (in most people)
  - Controls right hand         - Controls left hand
  - Sees right visual field     - Sees left visual field
                                - Spatial/artistic
  Connected via                 Connected to...
  corpus callosum → CUT

POST-SURGERY:
  Flash word "apple" to left visual field (→ right hemisphere):
  - Patient CANNOT name it (right hemisphere has no language)
  - Patient can POINT to apple with left hand (right hemi controls left hand)
  - When asked what word was shown: "I don't know"
  - When asked what they're pointing at: "An apple" (left hemisphere confabulates)
```

**The "interpreter" hypothesis** (Gazzaniga): The left hemisphere *constructs post-hoc explanations* for behavior it didn't cause. The left hemisphere is an "interpreter" — it generates narrative explanations for actions generated by other (disconnected) systems.

**Implication for consciousness**: This suggests that our sense of unified conscious experience may be a *construction* — especially the verbal account of "why we did what we did." Much action is generated by non-verbal systems; the verbal left hemisphere creates a plausible narrative.

---

## Disorders of Consciousness

```
SPECTRUM:
  BRAIN DEATH ── VEGETATIVE STATE ── MCS ── LOCKED-IN ── NORMAL
  (no brain activity) (arousal but no  (minimal    (aware but  (aware +
                       awareness)      awareness)  paralyzed)   mobile)

VS (Vegetative State): Eyes open, sleep/wake cycles, but no signs of awareness.
MCS (Minimally Conscious State): Inconsistent but reproducible signs of awareness.
LIS (Locked-In Syndrome): Full awareness; quadriplegia; only eye movement remains.
```

**Adrian Owen's work** (fMRI communication with VS patients):
```
Patient in apparent VS asked to imagine playing tennis → SMA activates
Patient asked to imagine walking through rooms → parahippocampal activates

Then used to COMMUNICATE: "imagine tennis = yes, imagine rooms = no"
Some patients answer autobiographical questions correctly

→ These patients are CONSCIOUS despite appearing unresponsive
→ Standard behavioral scales miss them
→ fMRI reveals preserved awareness
```

---

## The Binding Problem

The visual system processes color, orientation, motion, shape in different areas simultaneously. Somehow they're combined into a unified percept — the red, round, rolling ball.

**How does the brain bind features processed in separate regions?**

```
  COLOR (V4)      SHAPE (V1/V2/LOC)    MOTION (MT)
      |                  |                   |
      └──────────────────┴───────────────────┘
                         |
                    BINDING MECHANISM?
                         |
                    unified percept:
                    "RED ROUND ROLLING BALL"
```

**Temporal binding hypothesis**: Neurons processing the same object fire synchronously at ~40 Hz (gamma oscillations). Synchrony = "these features belong together."
- **Evidence**: gamma synchrony in visual cortex correlates with figure-ground perception
- **Problems**: doesn't explain how synchrony is "read" elsewhere; weak evidence from recordings

**Spatial attention binding** (Treisman FIT): Attention to a location binds features at that location. This is why illusory conjunctions occur under divided attention.

**Object files** (Kahneman, Treisman, Gibbs 1992): The visual system maintains "object files" — temporary representations that accumulate feature bindings for tracked objects over time.

---

## Decision Cheat Sheet

| Theory | Consciousness = ? | Strength | Weakness |
|--------|------------------|----------|---------|
| **GWT** | Global broadcast to workspace | Neural evidence, predictive | Doesn't address hard problem |
| **IIT** | Integrated information (Φ) | Principled math, explains cerebellum | Panpsychism, computationally intractable |
| **HOT** | Higher-order representation of state | Explains reportability | What makes HOT conscious? Regress? |
| **Predictive processing** | Best model of causes of input | Unified framework, clinical relevance | Doesn't directly address phenomenal |
| **Dennett eliminativism** | There's nothing extra to explain | Avoids hard problem | Counterintuitive; denies qualia |

---

## Common Confusion Points

**Access consciousness vs phenomenal consciousness** (Block 1995): *Access* = available for reasoning/report/control. *Phenomenal* = has a subjective feel. These *can* dissociate (blindsight: access to stimulus without phenomenal experience). GWT explains access consciousness well. The hard problem is about phenomenal consciousness.

**IIT's Φ = 0 for feedforward nets**: This is a feature, not a bug, from Tononi's perspective. It aligns with intuitions (most people doubt feedforward nets are conscious). But it implies current deep learning systems are not conscious — a strong claim.

**Split-brain ≠ two separate consciousnesses**: The right hemisphere shows *some* independent processing, but the extent of separate conscious streams is debated. Post-surgery patients report feeling like one person; the dissociations appear only under specific experimental conditions.

**"Neural correlates of consciousness" ≠ explanation of consciousness**: Finding that fronto-parietal activation correlates with conscious reports is not the same as explaining *why* that activation is accompanied by experience. The NCC research program is progress on the easy problems; it doesn't solve the hard problem.

**Cross-reference**: For the neural correlates of sleep/wake/anesthesia (implementing aspects of GWT and IIT predictions), see `neuroscience/02-SYSTEMS-CIRCUITS.md`. For philosophy of mind (functionalism, Chinese Room, eliminative materialism), see `philosophy/04-PHILOSOPHY-OF-MIND.md` (planned). Predictive processing connects to Bayesian models — see `cognitive-science/08-COMPUTATIONAL-MODELS.md`.
