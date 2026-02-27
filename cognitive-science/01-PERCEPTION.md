# Perception — Cognitive Science

## The Big Picture

Perception is not a camera. It is an *inference engine* — the brain generates hypotheses about the external world and tests them against incoming sensory data. Helmholtz (1860s) called it **unconscious inference**. Every modern theory of perception is a variation on this theme.

```
+------------------------------------------------------------------+
|  THE PERCEPTION PIPELINE                                         |
+------------------------------------------------------------------+
|                                                                  |
|  WORLD → SENSE ORGAN → TRANSDUCTION → NEURAL SIGNAL             |
|                                                                  |
|   Two competing streams (always running simultaneously):         |
|                                                                  |
|   BOTTOM-UP (data-driven)         TOP-DOWN (hypothesis-driven)   |
|   ────────────────────            ─────────────────────────      |
|   Raw sensory input               Prior knowledge                |
|   Physical features               Expectations                   |
|   Peripheral processing           Context, goals                 |
|   Mandatory, automatic            Modulates early processing     |
|   Fast                            Can operate very early         |
|                                                                  |
|              ↓                          ↓                        |
|              └──────────┬──────────────┘                        |
|                         ↓                                        |
|              PERCEPT (best-guess interpretation)                 |
+------------------------------------------------------------------+
```

**Bottom-up** alone can't work: the same sensory signal is consistent with infinitely many world states (the *inverse optics* problem — you can't uniquely recover a 3D scene from a 2D image without priors). **Top-down** alone can't work: you'd hallucinate constantly. Normal perception integrates both.

---

## Visual Perception — The System

Vision uses ~30% of human cortex. The processing hierarchy is deep.

```
RETINA → LGN → V1 → V2 → [SPLIT] → VENTRAL STREAM
                                    (temporal lobe)
                                    "What is it?"
                                    Object recognition
                                    Face processing (FFA)
                                    Color, form, texture
                          [SPLIT] → DORSAL STREAM
                                    (parietal lobe)
                                    "Where is it? How do I
                                     interact with it?"
                                    Spatial location
                                    Action guidance
                                    Motion
```

**The two-stream hypothesis** (Ungerleider & Mishkin 1982; Milner & Goodale 1992 revision):

| Stream | Pathway | Function | Lesion effect |
|--------|---------|----------|---------------|
| **Ventral** | V1 → V4 → IT (inferotemporal) | Object recognition, identity | Visual agnosia (can't name objects) |
| **Dorsal** | V1 → MT → parietal | Spatial, action guidance | Optic ataxia (can't reach accurately) |

**Key: Goodale & Milner's revision** — it's not "what" vs "where" but "what" vs "how." Patient D.F. had ventral stream damage: couldn't recognize object orientation, but when asked to *post a letter* through a slot, her hand rotated correctly. Perception for recognition vs. perception for action dissociate.

**Milestones in visual hierarchy**:

| Area | Key properties |
|------|---------------|
| **Retinal ganglion cells** | Center-surround receptive fields; ON/OFF channels |
| **LGN** | P (parvocellular, color+detail) vs M (magnocellular, motion) channels |
| **V1** (primary visual cortex) | Orientation selectivity (Hubel & Wiesel 1959, Nobel 1981); ocular dominance columns; spatial frequency |
| **V4** | Color; form |
| **MT/V5** | Motion; direction selectivity |
| **FFA** (fusiform face area) | Face-selective; prosopagnosia when damaged |
| **PPA** (parahippocampal place area) | Scenes, places |
| **LOC** (lateral occipital complex) | Object shape |

---

## Gestalt Principles — Organizing the Visual Field

Gestalt psychologists (Wertheimer, Köhler, Koffka — Berlin, ~1920s): perception organizes raw input into coherent wholes. The phrase: *"the whole is other than the sum of its parts."*

```
Six core principles:

 PROXIMITY          SIMILARITY         CLOSURE
  * * . . *          * * # # *         ( _ _ )  ← perceived as circle
  * * . . *          * * # # *         despite gap
  * * . . *          * * # # *
  Two groups          Two groups
  by distance         by symbol

 CONTINUITY         FIGURE-GROUND      COMMON FATE
  ─────────          ####.....          * * * * →  these dots
  ─────────          ####.....          * * * * →  moving together
  Lines seen as       Which region       are grouped
  continuous, not     is "figure"?       together
  broken              (Rubin vase)
```

**Why Gestalt principles exist**: They implement regularities about the natural world. Objects tend to have similar texture, move together, form closed contours. These principles are heuristics that work because they exploit statistical structure in natural scenes.

**Marr interpretation**: Gestalt principles operate at the **algorithmic level** — they describe *how* the visual system groups elements. The computational-level explanation is: recover surfaces and objects from image regions by exploiting co-occurrence statistics.

---

## Color Perception — Two Theories, Both Right

**Young-Helmholtz Trichromacy** (receptor level):
- Three cone types: L (long, ~560 nm red), M (medium, ~530 nm green), S (short, ~430 nm blue)
- Any color = weighted sum of L, M, S activations
- Predicts: color matches, mixing, common forms of color blindness

**Hering's Opponent-Process Theory** (post-receptor, ganglion cells + LGN):
```
Three opponent channels:
  Red vs Green    (L - M)
  Blue vs Yellow  (S - [L+M])
  Black vs White  (overall luminance)
```
- Predicts: afterimages (stare at red → green afterimage)
- Predicts: opponent colors can't coexist (no "reddish green")
- Explains: yellow is perceived as primary even though no "yellow cone"

**The resolution**: Both are correct — at different levels of the hierarchy. Cones implement trichromacy; post-receptor cells compute opponent channels. This is a textbook example of Marr's point that implementational and algorithmic levels can look very different.

---

## Depth Perception — Cues and Integration

```
MONOCULAR CUES (one eye sufficient):
+----------------------------------+
|  Perspective (parallel lines     |
|   converge to vanishing point)   |
|  Occlusion (A blocks B → A near) |
|  Relative size (farther = smaller|
|  Texture gradient                |
|  Motion parallax (nearer things  |
|   move faster in visual field)   |
|  Shading (light-from-above prior)|
|  Aerial perspective (blue haze)  |
+----------------------------------+

BINOCULAR CUES:
+----------------------------------+
|  Stereopsis (binocular           |
|   disparity — slightly different |
|   images → retinal disparity →   |
|   depth; Bela Julesz random-dot  |
|   stereogram proved this)        |
|  Convergence (eyes rotate in     |
|   for near objects — reliable    |
|   only within ~2 meters)         |
+----------------------------------+
```

**Bayesian cue combination** (Ernst & Banks 2002): depth cues are combined as weighted averages, with weights proportional to their reliability (inverse variance). This is Maximum Likelihood Estimation — the same precision-weighted fusion used in Kalman filters for sensor fusion. Under Gaussian noise, the optimal Bayesian estimate is a precision-weighted (1/sigma^2) average of the individual cue estimates: x_combined = (x1/sigma1^2 + x2/sigma2^2) / (1/sigma1^2 + 1/sigma2^2). The fact that human depth perception matches this formula quantitatively is one of the strongest pieces of evidence for the Bayesian brain hypothesis.

---

## Perceptual Constancy

The world is perceived as stable even though the retinal image changes with distance, angle, and illumination.

| Constancy | Challenge | Mechanism |
|-----------|-----------|-----------|
| **Size** | Same object = different retinal size at different distances | Rescaling by perceived distance (Emmert's Law) |
| **Shape** | Circle tilted = ellipse on retina | Correction for slant using surface orientation cues |
| **Color** | Object color changes radically under different illuminants | Color constancy: estimate illuminant, then discount it (Land's Retinex) |
| **Lightness** | Same reflectance looks different in light vs shadow | Estimate illumination, compute reflectance |

**Why illusions occur**: When the mechanisms for computing constancy are fed misleading cues. The Müller-Lyer illusion, the moon illusion, Adelson's checker shadow — all arise from valid inference rules applied to constructed situations that violate their assumptions.

---

## Auditory Scene Analysis

The **cocktail party problem** (Cherry 1953): how does the auditory system segregate simultaneous sound sources into separate streams?

```
PHYSICAL SIGNAL (mixed waveform)
         |
         v
SCENE ANALYSIS HEURISTICS:
  Harmonicity: sounds sharing a harmonic series → one source
  Onset synchrony: sounds starting together → one source
  Spatial location: same direction → one source
  Continuity: sounds continuing through brief interruption → one source
  Timbre consistency: similar spectral profile → one source
         |
         v
PERCEPTUAL STREAMS (A vs B, voice vs instrument)
```

**Auditory streaming** (van Noorden 1975): alternating tones (A-B-A-B-A-B) perceived as one stream or two depending on pitch difference and rate. High rate + large pitch gap → two streams. This demonstrates that streaming is a *temporal* phenomenon, not just a spectral one.

---

## Multisensory Integration

The brain constantly combines signals from different senses. The result is not just averaging — it's *near-optimal Bayesian fusion*.

**McGurk Effect** (1976): See "ga" face + hear "ba" audio → perceive "da." Vision overrides audition for speech. Demonstrates:
1. Speech perception is *inherently* multisensory
2. Top-down crossmodal binding operates mandatorily (can't "unhear" it even knowing the trick)

**Rubber Hand Illusion**: Synchronous touch on hidden real hand + visible rubber hand → rubber hand feels like "your" hand. Body ownership is a probabilistic inference about which signals originate from "self." Demonstrates: bodily self is constructed, not given.

**Ventriloquist Effect**: Sound appearing to come from visual source (puppet's mouth). Spatial capture by vision — vision has lower spatial uncertainty than audition.

**Temporal binding window**: Stimuli within ~50ms of each other tend to be integrated into one event. Outside that window, they're processed as separate.

---

## Change Blindness and Inattentional Blindness

**Change blindness** (Rensink, O'Regan, Clark 1997; Simons 2000):
- During saccades, blinks, cuts, or flickers, large scene changes go undetected
- "The door study": person asks for directions, is replaced by a different person mid-conversation — most people don't notice
- Implication: **we don't have a rich internal representation of the visual scene**. We sample on demand rather than maintaining a picture.

**Inattentional blindness** (Simons & Chabris 1999):
- Subjects count basketball passes; gorilla walks through the scene; ~50% miss it
- Attention gates conscious perception
- Implication: **attention is necessary for awareness**, not just for performance

```
COMMON MISCONCEPTION:
  "We see everything in the visual field"
       |
       v NO
  We consciously perceive only what
  attention selects and working memory
  encodes. The rest is sampled on demand.
```

**Transience and sparse representation**: Visual perception is not a photograph. It's a hypothesis generator that picks the most relevant features for the current task. Everything else is available for rapid sampling if needed, but is not maintained in detail.

---

## Decision Cheat Sheet

| Design Problem | Perceptual Mechanism | What to Do |
|---------------|---------------------|------------|
| Alert must be noticed instantly | Bottom-up salience (preattentive pop-out) | Use color, motion, or onset — features that bypass attention bottleneck |
| User misreads a display under stress | Top-down expectation override | Design for violated expectations — make critical state changes break the expected pattern |
| Users miss a critical change on screen | Change blindness | Don't rely on change alone — add a transient signal (flash, motion) at the change location |
| Training sim produces wrong depth judgments | Monocular cue conflict | Ensure texture gradient, occlusion, and motion parallax are consistent — binocular disparity alone is insufficient |
| Color-coded status is misread | Opponent-process + constancy failure | Don't rely on color alone (accessibility); use redundant coding (shape, position, label) |
| Audio alert masked by environment | Auditory streaming failure | Use frequency/timbre distinct from ambient noise; exploit onset synchrony to bind alert components |
| Multimodal display produces confusion | Cross-modal conflict (McGurk/ventriloquist) | Ensure spatial and temporal alignment of visual + auditory signals; vision will capture spatial, audio will capture temporal |
| Users fail to detect rare events | Inattentional blindness under high load | Reduce perceptual load on primary task during critical monitoring, or use automated detection with salient alerting |

---

## Common Confusion Points

**"Bottom-up is early, top-down is late"**: False. Top-down feedback reaches V1 (primary visual cortex) within 100ms. The "early/late" framing maps poorly onto the anatomy. The two streams are always active; they're better described as information sources that get fused.

**Two-stream as two independent systems**: They're not. The dorsal stream (action) uses ventral stream information for object recognition in grasping. Damage to one affects both. Think of them as two *modes of use* of visual information, not two isolated channels.

**Gestalt principles as "just descriptions"**: They're principled reflections of natural scene statistics. Proximity grouping works because objects that are near each other in the image often belong to the same surface. Gestalt principles are implicitly Bayesian.

**Change blindness as "bad vision"**: It's not a deficit. It reflects an *efficient* system that doesn't waste resources representing irrelevant details. The system computes on demand. The cost: surprise when things do change in expected non-salient locations.

**Color perception: "which theory is right?"**: Both are right at different levels. Cones = trichromatic; ganglion/LGN/cortex = opponent process. A common exam trick.

**Cross-reference**: For the neural implementation details of V1, retinal cells, LGN, and auditory cortex, see `neuroscience/02-SYSTEMS-CIRCUITS.md`. For the Bayesian formalization of perception, see `cognitive-science/08-COMPUTATIONAL-MODELS.md`.
