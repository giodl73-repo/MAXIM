# Attention and Memory — Cognitive Science

## The Big Picture

Attention determines what gets processed deeply; memory determines what persists. They are deeply intertwined — attention gates entry into working memory, working memory sustains attention, and long-term memory shapes what attention selects.

```
+------------------------------------------------------------------+
|  ATTENTION AND MEMORY: THE PIPELINE                              |
+------------------------------------------------------------------+
|                                                                  |
|  SENSORY INPUT                                                   |
|       |                                                          |
|       v                                                          |
|  SENSORY REGISTERS (iconic ~250ms / echoic ~2-4s)               |
|       |                                                          |
|       | ← ATTENTION SELECTS ←─────────────────────────+        |
|       v                                               |         |
|  WORKING MEMORY (active, limited capacity)            |         |
|       |    ← Long-term knowledge shapes WM ──────────-+         |
|       v                                                          |
|  LONG-TERM MEMORY (vast, persistent)                             |
|       |                                                          |
|       v                                                          |
|  BEHAVIOR / RESPONSE                                             |
+------------------------------------------------------------------+
```

---

## Attention — The Selection Problem

The brain has limited processing capacity. The signal reaching the senses far exceeds what can be processed deeply. **Attention** is the set of mechanisms that selects, prioritizes, and amplifies some signals at the expense of others.

**The cocktail party problem** (Cherry 1953): How do you follow one conversation in a noisy room full of conversations? Subjects wearing headphones could shadow (repeat aloud) one ear's message while ignoring the other. They retained almost nothing of the unattended message — but they noticed their own name, and they noticed the message switching from speech to tones.

---

## Bottleneck Models of Attention

Three classic models, each locating the "bottleneck" at a different point in processing:

```
BROADBENT (1958)          TREISMAN (1964)         DEUTSCH-NORMAN (1963)
Early Selection           Attenuation             Late Selection

Sensory buffer            Sensory buffer          Sensory buffer
    |                         |                       |
 [FILTER]                 [ATTENUATOR]            Full analysis
 (physical                (reduces signal          of all inputs
  features:               of unattended             |
  location,               channel, doesn't      [SELECTION]
  pitch)                  eliminate it)          at response
    |                         |                  selection stage
Only attended            Attended + weak            |
input analyzed           unattended processed    One output
    |                         |
    v                         v
Response                  Response
```

| Model | Bottleneck location | Key evidence | Problem |
|-------|--------------------|--------------|---------|
| Broadbent | Early (physical) | Shadowing: lose unattended meaning | Own name heard on unattended channel — can't be if filtered early |
| Treisman | Early-ish (attenuated) | Relevant words on unattended channel break through | More complex architecture needed |
| Deutsch-Norman | Late (semantic) | Semantic processing of unattended input | Capacity wasted analyzing everything |

**Lavie's Load Theory** (1995+): The correct model depends on **perceptual load**:
- *High perceptual load* in attended task → no capacity left for unattended stimuli → early selection
- *Low perceptual load* → spare capacity processes unattended stimuli → late selection
- Both Broadbent and Deutsch-Norman are right under different conditions.

---

## Feature Integration Theory (Treisman & Gelade 1980)

How do you find a red vertical bar among red horizontal bars and blue vertical bars? You need to *bind* features (color + orientation) — they don't come pre-bound.

```
PREATTENTIVE FEATURES (pop out in parallel — free):
  Color    Orientation    Motion    Size    Curvature
  Can search entire field simultaneously
  "Red thing" pops out regardless of distractors

CONJUNCTIONS (require serial attention — costly):
  "Red AND vertical" requires binding features
  Search time ∝ number of distractors (serial scan)
```

**Feature maps** → a **master map of locations** ← attention spotlight binds features at attended location.

**Illusory conjunctions**: Briefly presented colored shapes under divided attention → subjects report seeing combinations that didn't appear (red circle + blue square → blue circle). Attention failure produces incorrect bindings.

---

## The Attentional Blink

In Rapid Serial Visual Presentation (RSVP) at ~10 items/second:
- Detect T1 (first target) ✓
- Detect T2 if presented 200–500ms after T1 → severe impairment
- T2 at lag 1 (immediately after T1) is spared ("lag-1 sparing")
- T2 at lag 8+ fully recoverable

**Interpretation**: After processing T1, the "gate" to working memory is closed for ~500ms while T1 is consolidated. T2 arrives during this refractory period and is lost.

```
Time: 0ms  100ms  200ms  300ms  400ms  500ms  600ms  700ms
Items: X    X    [T1]   X    [T2?]   X     X    [T2?]
                  ↑                   ↑                 ↑
             Gate opens         Blink zone          Gate re-opens
             T1 enters WM       T2 missed            T2 seen
```

Reveals: **conscious perception is gated**, not continuous. You can miss things you're looking for.

---

## Spatial Attention — Posner Cueing

**Covert vs overt attention**: You can attend to a location without moving your eyes (covert). Your eyes and attention are partially decoupled.

**Posner cueing paradigm** (1980):
```
  1. Fixation point +
  2. Cue (arrow left/right, or peripheral flash)
  3. Target appears at cued or uncued location

  VALID cue (80%): target at cued location → faster RT
  INVALID cue (20%): target at uncued location → slower RT

  PERIPHERAL cue: capture attention even if not predictive
  (exogenous / reflexive / bottom-up)

  CENTRAL arrow: only helps if predictive
  (endogenous / voluntary / top-down)
```

**Spotlight metaphor**: Attention is a spotlight — enhances processing at attended location, relative suppression elsewhere. But the spotlight isn't homogeneous; the *gradient* of attention can be modified (zoom lens model).

---

<!-- @editor[bridge/P2]: Working memory as a computational resource is the most direct hook for this learner. The transition from the bottleneck models to working memory should explicitly draw the cache analogy: phonological loop ≈ L1 cache (fast, small, serial access); visuospatial sketchpad ≈ separate memory-mapped region; central executive ≈ cache controller/scheduler. The ~3-4 chunk capacity = cache line count, with LTM as backing store. This is the bridge that makes WM limits immediately actionable for system designers. Currently missing entirely. -->

## Working Memory — Baddeley & Hitch

The Atkinson-Shiffrin "modal model" (1968) had a simple short-term store. Baddeley & Hitch (1974) showed it was actually a multi-component system — the **working memory model**.

```
+------------------------------------------------------------------+
|  WORKING MEMORY (Baddeley 1974, revised 2000)                   |
+------------------------------------------------------------------+
|                                                                  |
|              CENTRAL EXECUTIVE                                   |
|         (attention + control + coordination)                     |
|         Frontal cortex                                           |
|              /           \           \                           |
|             /             \           \                          |
|  PHONOLOGICAL LOOP    VISUOSPATIAL    EPISODIC BUFFER            |
|  (inner speech)        SKETCHPAD      (integrated episodes,      |
|  ~2 seconds of         (visual+        binds WM with LTM)        |
|   speech rehearsal)     spatial)       Added in 2000 revision    |
|  Broca's area           Parietal                                 |
|  + premotor             cortex                                   |
+------------------------------------------------------------------+
          ↕                    ↕                    ↕
                    LONG-TERM MEMORY
```

**The four components**:

| Component | Function | Capacity | Evidence |
|-----------|----------|----------|---------|
| **Phonological loop** | Verbal/acoustic rehearsal | ~2 sec speech | Articulatory suppression + word length effects |
| **Visuospatial sketchpad** | Spatial + visual information | ~4 items | Separate from verbal; mental rotation |
| **Central executive** | Coordinates, controls, allocates | Very limited | Frontal lobe damage = executive dysfunction |
| **Episodic buffer** | Integrates WM with LTM; binds features | ~4 episodes | Explains how WM and LTM interact |

**Capacity**: Miller's "magical number 7" (1956) measured digit span, which benefits from rehearsal. The "true" WM capacity without rehearsal is ~**3–4 chunks** (Cowan 2001). What counts as a chunk depends on long-term knowledge.

---

## Long-Term Memory — Taxonomy

```
LONG-TERM MEMORY
├── DECLARATIVE (explicit — conscious access)
│   ├── EPISODIC — personal events, autobiography
│   │   "I had lunch at the Pike Place Market in 2019"
│   │   Hippocampus-dependent
│   └── SEMANTIC — general knowledge, facts
│       "The capital of France is Paris"
│       Neocortex; survives hippocampal damage
└── NONDECLARATIVE (implicit — no conscious access)
    ├── PROCEDURAL — skills, habits
    │   Riding a bike, touch typing
    │   Basal ganglia + cerebellum
    ├── PRIMING — facilitated processing from prior exposure
    │   Implicit word completion, repetition priming
    │   Neocortex
    └── CONDITIONING
        Classical (amygdala) + instrumental (basal ganglia)
```

**Dissociation evidence (H.M. — patient Henry Molaison)**:
- Bilateral hippocampectomy (1953) for epilepsy
- Result: dense anterograde amnesia (can't form new episodic memories)
- But: intact working memory, intact procedural learning (mirror drawing), intact semantic memory for pre-surgical knowledge
- Demonstrates: episodic memory ≠ procedural ≠ WM — these are dissociable systems

---

## Encoding — Levels of Processing

**Craik & Lockhart (1972)**: Memory depth is determined by how deeply material is *processed*, not by the "store" it's in.

```
SHALLOW ──────────────────────────────────────► DEEP
  Structural      Phonological      Semantic
  (appearance)    (sound)           (meaning)

  "Is the word    "Does it          "Does it fit:
  in capital       rhyme with        'The ___
  letters?"        'hat'?"           jumped'"?

  Worse retention ──────────────────► Better retention
```

**Elaborative vs maintenance rehearsal**:
- Maintenance: repeat "7481" over and over → doesn't improve long-term retention
- Elaborative: link to meaning, create associations → much better retention

**Implication for software engineering**: Code review is elaborative rehearsal. Reading docs is maintenance rehearsal. Testing/writing code is elaborative. This is why teaching or writing documentation about something improves your own understanding.

<!-- @editor[bridge/P3]: Natural bridge to the transformer attention mechanism is missing here. The feature integration theory (serial binding via attention spotlight) is structurally analogous to the query-key-value attention mechanism: the spotlight selects features at a location (query), binds them from feature maps (keys/values). This connection is a clean bridge from cognitive attention research to the ML attention mechanism that would resonate for an AI-interested reader. One paragraph would suffice. -->

---

## Forgetting — Ebbinghaus and Interference

**Ebbinghaus forgetting curve** (1885): Retention of nonsense syllables over time. Exponential decay:
```
100% |*
     | \
  50% |  \
     |   \*
  25% |    \  *
     |     \    *  *  *
   0% +--+--+--+--+------→ time
      1h 1d 2d 1w  1mo
```

**Spacing effect**: Forgetting is NOT just a problem. It is *necessary* for spacing to help. Reactivating a memory when it has partially faded strengthens it more than re-studying while still fresh. **Distributed practice beats massed practice** (see 09-APPLIED-BRIDGE.md).

**Interference theory** — forgetting as competition between memories:
- **Proactive interference (PI)**: Old learning interferes with new. Why it's hard to memorize a new phone number when you've had the same number for years.
- **Retroactive interference (RI)**: New learning disrupts old. Learning a new programming language syntax can initially interfere with the old one.

---

## False Memory — Loftus

Memory is not a recording. It is **reconstructive** — filled in from knowledge, expectations, and post-event information.

**Misinformation effect** (Loftus & Palmer 1974):
- Subjects watch car accident video
- Question 1: "How fast were the cars going when they *smashed*?" vs "*contacted*?"
- *Smashed* → higher speed estimates, and one week later: more likely to report (non-existent) broken glass
- Post-event questions *alter* the memory, not just the report

**Lost in the mall study** (Loftus & Pickrell 1995):
- Experimenters convinced ~25% of subjects they had been *lost in a mall as a child* (a false event, verified with family)
- Subjects developed rich, confident false memories
- Demonstrates: entire *events* can be implanted

**Reconsolidation** (Nader et al. 2000):
- Memories become labile when *reactivated* — they must be reconsolidated
- Window to modify: briefly reactivate memory, introduce misinformation before reconsolidation completes
- Clinical implication: exposure therapy + reconsolidation blockers for PTSD
- Mechanism: protein synthesis inhibition post-reactivation erases the memory

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why do I lose the unattended channel? | Early selection bottleneck (Broadbent), or spare capacity consumed (Lavie high load) |
| Why can I hear my name across the room? | Attenuation model (Treisman) — unattended channel weakened, not blocked; your name has a low threshold |
| Why does the gorilla go unnoticed? | Inattentional blindness — task demands consume all capacity; gorilla never gets selected |
| Why do I forget after massed cramming? | No spacing — memories not reactivated at the right interval; no consolidation advantage |
| Why do eyewitnesses make errors? | Reconstructive memory + misinformation effect; post-event info alters the trace |
| How many items can WM hold? | 3–4 chunks (without rehearsal); more with chunking via LTM knowledge |
| Why can't H.M. form new memories? | Hippocampus required for episodic encoding; intact for procedural and semantic |
| Why does testing work better than re-reading? | Retrieval practice — see 09-APPLIED-BRIDGE.md |

---

## Common Confusion Points

**Working memory ≠ short-term memory**: STM (Atkinson-Shiffrin) is a storage buffer. WM (Baddeley) is an active manipulation workspace with multiple sub-systems. The central executive does *attention and control*, not just storage.

**Declarative ≠ explicit ≠ conscious**: Declarative memory has *two* sub-types: episodic and semantic. You can have intact semantic memory with destroyed episodic memory. "Explicit" = can verbally report; nondeclarative = can't. These distinctions matter clinically.

**Forgetting ≠ loss**: Information may still be *there* but inaccessible (retrieval failure). This explains why recognition is easier than recall — more retrieval cues. The information is often not *gone*, just not accessible via the current retrieval route.

**Levels of processing ≠ stages of processing**: "Levels" means depth of semantic analysis, not the number of processing stages. Shallow processing can be multi-stage; a single deep encoding beats multiple shallow ones.

**False memories ≠ lying**: False memories feel real and confident. Loftus's subjects genuinely believed the false mall experience. This is not confabulation from brain damage — it is a property of *normal* reconstructive memory. Confidence ≠ accuracy.

**Cross-reference**: For the neural mechanisms of hippocampal memory consolidation, theta oscillations, and place cells, see `neuroscience/02-SYSTEMS-CIRCUITS.md`. For the applied implications for learning, see `cognitive-science/09-APPLIED-BRIDGE.md`.
