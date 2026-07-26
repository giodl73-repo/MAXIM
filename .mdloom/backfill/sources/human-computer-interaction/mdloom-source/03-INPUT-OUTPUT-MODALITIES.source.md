---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-INPUT-OUTPUT-MODALITIES.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-computer-interaction:input-output-modalities
kind: guide
module: human-computer-interaction
section: human-computer-interaction
title: Input and Output Modalities - The Interaction Substrate
status: source-custody
source_custody: partial
current_path: human-computer-interaction/03-INPUT-OUTPUT-MODALITIES.md
canonical_path: human-computer-interaction/03-INPUT-OUTPUT-MODALITIES.md
backsource_ids: [mdloom-backfill:human-computer-interaction:03-input-output-modalities]
concepts: [input-modalities, output-modalities, pointing, touch, gesture, voice, gaze, fitts-law-applied, hick-law-applied]
root_concepts: [input-output-modalities]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Input and Output Modalities — The Interaction Substrate

**This guide owns** the *substrate* every interaction runs on: the input channels (pointing,
typing, touch, gesture, voice, gaze, pen) and output channels (visual displays, audio, haptics),
the device/technique design space, and the **applied performance laws** (Fitts, Hick–Hyman) that
let you *predict and compare* modality performance. **It builds on** `02` (the models the substrate
serves) and feeds `04`/`05` (design choices and their evaluation). **It explicitly defers** the
*derivation* of Fitts' and Hick's laws and the psychophysics beneath them to
`cognitive-science/09-APPLIED-BRIDGE` (this guide **cites and applies**, never re-derives); *display
rendering and pipeline internals* to `computer-graphics/`; *signal/DSP internals* of audio and
sensors to `signal-processing/`; *ASR/model internals* behind voice to `ai-engineering/`; *physical
anthropometry and product ergonomics* to `industrial-design/05` and `human-factors/`; and *legal
accessibility duty* to `law/` (the accessibility of each modality is `08`'s to design).

> **This module is an educational reference. Modality performance figures below are engineering
> estimates, not universal constants: named "laws" are attributed and dated, and every throughput/
> time/error comparison names its estimator and sample or is marked illustrative. Nothing here is a
> safety-certification (operator performance under load is `human-factors/`) or legal advice.**

*Per-guide banner: a modality claim is a **performance claim**. Every throughput/error/time
comparison in this guide either names its **estimator and its *n*** or is explicitly labeled
**illustrative and bounded**. Fitts' and Hick's laws appear only as **cited, device- and
population-bounded applied laws** with dates; an undated or universalized "law," or a benchmark
reported without its sample and estimator, is a bug.*

---

## The Big Picture: A Transducer Loop Between Human and System

Interaction is a loop of **transductions**: the human's motor system drives an *input transducer*
(a device turning movement/sound/gaze into signals), the system computes, and an *output
transducer* (a display/speaker/actuator) drives the human's *sensory* system. Every modality is a
point in that loop with its own bandwidth, precision, error model, and cost.

```
  THE MODALITY LOOP
  ------------------------------------------------------------------
   HUMAN motor            INPUT transducer         SYSTEM
   (hand, voice,   ---->  (mouse, touch,     ---->  compute
    eyes, body)           mic, camera, pen)              |
        ^                                                v
   HUMAN sensory   <----  OUTPUT transducer   <----  render
   (vision, hearing,      (display, speaker,          state
    touch)                haptic actuator)
  ------------------------------------------------------------------
   Each arrow has a BANDWIDTH, a PRECISION, an ERROR MODEL, and a COST.
   "Which modality?" = which loop best fits the task, body, and context.
```

Input devices differ along a small **design space** (Card, Mackinlay & Robertson, "A Morphological
Analysis of the Design Space of Input Devices," ACM TOIS, **1991**; Buxton's foundational input
taxonomy, 1980s):

```
  THE INPUT DESIGN SPACE (a few axes that decide fit)
  ------------------------------------------------------------------
   what is sensed .... position | motion | force ; linear | rotary
   dimensionality .... degrees of freedom (DOF): 1 (slider) .. 6 (6-DOF wand)
   discrete/continuous discrete (keys, buttons) vs continuous (mouse, touch)
   direct/indirect ... direct (touch the object) vs indirect (mouse -> cursor)
   absolute/relative . absolute (pen on tablet) vs relative (mouse, trackpad)
  ------------------------------------------------------------------
   A "technique" = a device + a mapping + feedback. The same device supports
   many techniques; the technique, not the device, is what you evaluate.
```

**Bridge (software).** A modality is a **driver plus an encoding**: the input transducer is a
device driver producing an event stream; the technique is the **event-handling and mapping layer**;
the output transducer is your **rendering/notification backend**. Choosing a modality is choosing an
**I/O interface with a throughput and an error rate** — exactly the reasoning you apply when picking
a transport (low-latency small messages vs high-throughput bulk), except the client is a human body.

---

## 1. Pointing and Fitts' Law — Applied, Bounded, Dated

The best-established applied law in interface design. **Fitts' Law** (Paul Fitts, **1954**) models
the **movement time to acquire a target** as a function of distance and target size. HCI uses the
**Shannon formulation** (MacKenzie, "Fitts' law as a research and design tool in human–computer
interaction," *HCI*, **1992**):

```
  FITTS' LAW (Shannon form; MacKenzie 1992)  -- APPLIED, not derived here
  ------------------------------------------------------------------
     MT = a + b * ID          movement time = intercept + slope * difficulty
     ID = log2( A / W + 1 )   index of difficulty (bits); A = distance, W = width
     throughput  TP = IDe / MT (bits/s)  -- ISO 9241-411 uses the EFFECTIVE ID:
                                            target width adjusted to the observed
                                            endpoint spread (accuracy), so speed
                                            and accuracy are folded together
  ------------------------------------------------------------------
   a, b are EMPIRICAL constants for a given device + user population + posture.
   They are NOT universal: a mouse, a trackpad, a thumb, and a gaze pointer
   each have different a, b. Report them with the device and the sample.
```

What the law lets you *predict and compare*, and its **bounds**:

- **Design predictions.** Bigger targets and shorter travel are faster; edges and corners act as if
  infinitely large in one axis (the pointer stops at the screen edge), which is *why* menu bars live
  at the screen edge. These are applied consequences, stated as directional predictions.
- **The comparison metric is throughput, and it has an *n*.** To compare two pointing techniques you
  run an **ISO 9241-411** (2012; successor to 9241-9, 2000) multi-directional tapping task and report
  **effective throughput (bits/s) with its sample size and variance** — *effective* because the
  standard adjusts the target width to the observed endpoint spread, folding accuracy into the score,
  so it is not a raw ID/MT and is not gameable by trading accuracy for speed. Never a bare "faster."
  *Illustrative and bounded:* published mouse throughputs commonly fall in a low-single-digit bits/s
  range while some indirect or gaze techniques fall lower, but the exact value depends on device,
  task, and population, so it must be measured, not asserted.
- **Bounds (where it does not apply).** Fitts' Law is for **rapid, aimed, pointer-based movement to a
  single target**. It does *not* model trajectory/steering tasks (that is the **steering law**,
  Accot & Zhai, 1997), multi-target or cognitive search, or dragging with heavy cognitive load. Using
  it outside aimed pointing is the classic over-generalization.

*Deferral.* *Why* the speed–accuracy trade-off takes this log form — the information-theoretic and
motor-control account — is `cognitive-science/09`'s. This guide uses the law as a **bounded design
and comparison tool** and always attaches the device and sample.

---

## 2. Choice Reaction and the Hick–Hyman Law — Applied and Sharply Bounded

For **choosing among options**, the **Hick–Hyman Law** (William Hick, **1952**; Ray Hyman, **1953**)
models decision time as logarithmic in the number of *equally likely* alternatives:

```
  HICK-HYMAN LAW  -- APPLIED, and easy to misuse
  ------------------------------------------------------------------
     RT = a + b * log2( n + 1 )     n = number of equiprobable choices
  ------------------------------------------------------------------
   PREDICTS: one well-organized menu of many items can beat several nested
   menus, because deciding is log(n), while stepping through levels is linear.
   BOUNDS (where it FAILS):
     - choices not equally likely (real menus never are) -> weight them
     - the user must SEARCH/READ each item (visual scan dominates, not decision)
     - the user already knows the target (expert, spatial memory -> near-constant)
```

The load-bearing honesty: Hick–Hyman governs **decision among known, equiprobable options**. Real
menus involve **visual search and reading**, which do not follow Hick–Hyman and often dominate, so
"fewer options is always faster" is a **misapplication**. The correct applied claim is narrow: for
genuine equiprobable choice, flatter beats deeper; otherwise, measure.

*Deferral.* The derivation (information-theoretic choice) and the search/attention mechanisms belong
to `cognitive-science/09`. This guide owns only the bounded application and its failure conditions.

---

## 3. Text Entry — Measures Before Claims

Text entry is where "faster keyboard" claims most need discipline, because the metrics are
standardized and the comparisons are notorious for unsourced numbers.

| Measure | What it is | Trap |
|---------|-----------|------|
| **WPM** (words/min) | throughput; 1 "word" = 5 characters by convention | must state entry method, corpus, and whether errors were corrected |
| **KSPC** (keystrokes/char) | effort per character (predictive text lowers it) | low KSPC ≠ fast if each key is slow or error-prone |
| **error rate** (e.g., MSD / total error rate, Soukoreff & MacKenzie, CHI **2003**) | uncorrected + corrected errors, from the minimum string distance | reporting speed without an error rate is meaningless (speed–accuracy trade-off) |

The applied points: **physical QWERTY** persists by installed base and switching cost (`01`; its own
optimality is contested, not settled); **soft
(touch) keyboards** trade tactile feedback and precision for flexibility and are dominated by target
size (§5) and language-model correction; **thumb typing** on phones follows its own speed–accuracy
curve. *Any* "input method A beats B" claim must carry **WPM *and* error rate *and* the sample and
corpus** — a speed number alone is not a result (this is `05`'s discovery-vs-measurement discipline
pointed at typing).

---

## 4. Touch and Gesture — Directness at the Cost of Precision

Touch (mainstream since 2007, `01`) collapses the pointer's indirection into **direct contact**, but
pays for it:

```
  TOUCH: WHAT DIRECTNESS COSTS
  ------------------------------------------------------------------
   + direct: the finger IS the pointer (narrows the execution gulf, §02)
   + gestures: pinch/swipe/rotate are first-class continuous actions
   - the "fat finger": the contact area is large and imprecise
   - occlusion: the finger/hand hides the very target it acts on
   - no hover: the pointer has no "before-press" state (hover idioms break)
  ------------------------------------------------------------------
   Design response: adequate TARGET SIZE and spacing. WCAG 2.2 SC 2.5.8
   Target Size (Minimum), AA: 24x24 CSS px, WITH defined exceptions
   (spacing / equivalent control / inline / user-agent / essential) -- see 08.
```

Gestures add expressive, chorded, and continuous input (Buxton's *chunking and phrasing*, 1986: a
compound gesture entered as one "phrase" lowers cognitive segmentation), but they are **invisible and
unlabeled** — a gesture has no affordance until learned, which is a discoverability (execution-gulf)
cost, and **path- or multipoint-only** gestures exclude users who cannot perform them (a `08` matter:
WCAG 2.2 requires single-pointer alternatives and no drag-only operation). The applied rule: gestures
*accelerate experts* and *strand novices and some disabled users* unless paired with a visible,
operable alternative.

---

## 5. Voice and Conversational Input — A Channel with a Real Error Model

Voice input turns the microphone into an input transducer via automatic speech recognition (ASR).
As an **interaction modality** (the model internals are `ai-engineering/`'s), its defining properties:

- **Hands-free / eyes-free.** Its unique value is contexts where hands and eyes are busy or absent
  (driving, cooking, motor or visual disability) — a `08` access channel and a situational-disability
  win (`08` §8).
- **It has a measurable error model: word error rate (WER).** Voice is not "natural and free"; it has
  a recognition error rate that varies with noise, vocabulary, and — critically — **speaker
  demographics**. *Attributed, dated:* Koenecke et al. (*PNAS*, **2020**) documented substantially
  higher ASR error rates for Black than white speakers across major commercial systems; accent and
  under-resourced languages show similar gaps. Treat WER as a **population-dependent** figure, never a
  single system constant.
- **The interaction cost of errors is high.** A mis-recognition mid-command forces a repair dialog;
  invisible command vocabularies create an execution-gulf discoverability problem ("what can I say?").
  These are the *interaction* responsibilities this guide owns; the acoustic/model machinery is
  deferred.

---

## 6. Gaze, Pen, and Mid-Air — Specialist Modalities and Their Signature Failures

- **Gaze.** Fast to *point* (the eye reaches a target almost instantly) but plagued by the **"Midas
  touch" problem** (Jacob, **1990**): the eye is always looking, so distinguishing *intent to select*
  from *mere looking* is the core difficulty — hence dwell-time, blink, or confirm-by-other-modality
  selection. Gaze is a powerful access modality (`08`) for users who cannot use hands, bounded by
  calibration and fatigue.
- **Pen / stylus.** High-precision, absolute, direct; excellent for drawing, annotation, and CJK/
  complex-script handwriting entry (a globalization point, §caveats). Hover and pressure add DOF a
  finger lacks.
- **Mid-air gesture / body.** Expressive and touchless, but suffers **fatigue** ("gorilla arm") and
  weak feedback; strong for short, coarse interactions, weak for sustained precise ones.

Each is admitted here with its **signature failure** named — that is the performance-claim
discipline applied to specialist channels.

---

## 7. Output — Displays, Audio, Haptics

Output modalities are transducers into the human senses; each has a design contract this module owns
(the *rendering* is deferred).

| Channel | Carries well | Design contract (owned by HCI; bounds noted) |
|---------|--------------|----------------------------------------------|
| **Visual display** | dense, parallel, spatial, persistent information | legibility, contrast (WCAG 1.4.3 text 4.5:1 / 1.4.11 non-text 3:1, from `08`), reflow, not-by-color-alone; rendering internals → `computer-graphics/` |
| **Audio** (speech, earcons, auditory icons) | alerts, eyes-free status, ambient awareness | audio is **transient and serial** — never the *only* channel for critical info (`08`); earcons (abstract) vs auditory icons (Gaver, 1986: everyday-sound metaphors) |
| **Haptics** (vibration, force feedback) | private, eyes-free confirmation; texture/force in VR | low bandwidth; strong as a *redundant* confirmation, weak as a sole carrier |

The cross-modality rule (and a `08` invariant): **critical information must be available on more than
one channel**, because any single channel excludes someone and fails in some context (a beep in a
loud room, a color in sunlight, a vibration in a pocket on a table).

---

## A Worked Modality Choice (illustrative, fictional)

*Fictional, to show bounded performance reasoning. No real product or benchmark.*

**Context.** *TrailMate*, a fictional hiking app. Two tasks: (a) mark a waypoint while walking, one-
handed, in bright sun, gloves on; (b) enter a long trip note back at camp.

- **Task (a) — mark a waypoint.** Ruled out: precise touch targets (gloves + motion + occlusion +
  sunlight glare all degrade touch precision; small targets fight WCAG 2.5.8). Chosen: a **single
  large hardware/edge button** (Fitts: a screen-edge or physical target is effectively large in one
  axis → low ID → fast and error-tolerant), with **haptic** confirmation (eyes-free, works in
  sunlight where a visual-only cue fails). The claim "large edge target is faster and more error-
  tolerant here" is a **directional Fitts prediction**, to be confirmed by an ISO 9241-411-style
  measure with a real sample before it's stated as a number.
- **Task (b) — long note.** Chosen: **voice with a visible transcript and easy correction**, because
  it is hands-free-ish and fast for prose — *but* the design must budget for **WER** (noise at camp,
  accents) with a low-friction repair path and a **typing fallback** (voice can't be the only method:
  a `08` alternative-channel requirement and a WER-population caveat).

**Reading.** Every choice is justified by a **bounded** performance argument (Fitts as directional
prediction; voice with an explicit error model and fallback), and every quantitative claim is flagged
as *to be measured*, not asserted. That is the modality-as-performance-claim discipline.

---

## Reader Tasks (answerable from this guide)

1. **Apply Fitts' Law within its bounds.** Explain why menu bars sit at the screen edge and why big
   buttons are faster to hit, then state where Fitts' Law does *not* apply (steering/trajectory,
   search) and what you'd measure (ISO 9241-411 throughput, with its sample) to compare two pointers.
2. **Catch a Hick–Hyman misuse.** Given "we cut the menu from 12 items to 6, so selection is faster,"
   state the conditions under which Hick–Hyman applies (equiprobable, decision-bound choice) and why a
   read-and-search menu may not get faster — and that the honest move is to measure.
3. **Demand a complete text-entry claim.** Given "our new keyboard is 15% faster," list what's
   missing before it's a result (error rate, method, corpus, sample) and why speed alone is
   meaningless under the speed–accuracy trade-off.
4. **Design a modality for a hands-busy, eyes-busy context.** Pick a channel for confirming an action
   while driving (audio/haptic, not a visual-only cue), and justify with the transducer loop and the
   more-than-one-channel rule.
5. **Bound a voice claim by population.** Given "voice input works for everyone," cite the ASR
   demographic-disparity finding (Koenecke et al. 2020) and require WER be treated as population-
   dependent, with a non-voice fallback (a `08` requirement).

---

## Decision Cheat Sheet

| The task/context is… | Prefer | Because (bounded) |
|----------------------|--------|-------------------|
| acquire a visible target fast | pointing/touch with **big targets, short travel** | Fitts: lower ID → lower MT (aimed movement only) |
| choose among genuine equiprobable options | one **flat, organized** menu | Hick–Hyman: decide in log(n), not linear stepping |
| enter lots of text, hands free | **voice** + visible transcript + typing fallback | fast for prose, but budget WER (population-dependent) + alternative |
| precise drawing / CJK handwriting | **pen/stylus** | absolute, high-precision, pressure/hover DOF |
| hands-busy / eyes-busy confirmation | **audio + haptic** (redundant) | eyes-free, private; never the sole critical channel |
| user cannot use hands | **gaze / switch / voice** (from `08`) | access channels; mind Midas-touch (gaze), WER (voice) |
| compare two input techniques | run **ISO 9241-411**, report **throughput + n** | a bare "faster" is not a measurement |
| the *why* behind Fitts/Hick | `cognitive-science/09` | HCI applies; it does not derive |

---

## Common Confusion Points

**"Fitts' Law gives you the movement time."** Only for **aimed pointing to a single target**, and
only with **device- and population-specific** constants *a*, *b*. It does not cover steering, search,
or heavy cognitive load, and its constants are not universal — report them with the device and sample
(§1).

**"Fewer menu items is always faster (Hick's Law)."** No. Hick–Hyman governs **equiprobable
decision**, not the **visual search and reading** that dominate real menus, and not experts using
spatial memory. "Flatter beats deeper" holds narrowly; otherwise measure (§2).

**"Voice is natural, so it just works."** No. Voice has a **word error rate** that varies with noise,
accent, and speaker demographics (Koenecke et al. 2020); command vocabularies are invisible; error
repair is costly. It's a powerful channel with a real error model and needs a fallback (§5).

**"Touch is more precise than a mouse because it's direct."** No. Touch is *direct* but *imprecise*
(fat finger, occlusion, no hover). Directness narrows the execution gulf; it does not buy precision —
which is why target size and spacing matter so much (§4).

**"A speed number proves a modality is better."** No. Every modality comparison is a **performance
claim** needing an **estimator, an error rate, and a sample** (this is `05`'s discipline). Speed
without accuracy and *n* is not a result (§3, banner).

---

## Global, WEIRD, and Resource Caveats

- **Input methods are script- and language-bound.** QWERTY and Latin-centric text entry do not
  serve CJK, Indic, Arabic, or other complex scripts equally; **input method editors (IMEs)**,
  handwriting/pen, and voice are first-order, not add-ons, for much of the world. The "keyboard" is
  not a universal.
- **ASR and gesture recognition carry demographic and environmental bias.** Recognition accuracy
  varies with accent, dialect, language resourcing, ambient noise, and (for vision-based gesture)
  skin tone and lighting. Treat every recognition-rate figure as **population- and context-
  dependent**, and never ship a recognition-only path without an alternative.
- **Devices and bandwidth bound the modality.** Low-end phones, small screens, feature phones, and
  metered/2G connections change which output channels are even available; a rich haptic-and-video
  confirmation is inaccessible where a lightweight text/audio path is not (`08` §8). The two module
  invariants ride here: every modality must have an **accessible alternative channel** sized for the
  full population, and no modality choice may be inverted into engineered friction against the user
  (`11`) — and where a modality failure could cause physical harm (a missed alarm), operator-load
  analysis is `human-factors/`'s.
