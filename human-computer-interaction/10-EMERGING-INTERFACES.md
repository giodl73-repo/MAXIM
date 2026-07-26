---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-computer-interaction:emerging-interfaces
kind: guide
module: human-computer-interaction
section: human-computer-interaction
title: Emerging Interfaces - Post-WIMP Paradigms Under an Evidence Bar
status: source-custody
source_custody: partial
current_path: human-computer-interaction/10-EMERGING-INTERFACES.md
canonical_path: human-computer-interaction/10-EMERGING-INTERFACES.md
backsource_ids: [proof-backfill:human-computer-interaction:10-emerging-interfaces]
concepts: [emerging-interfaces, augmented-reality, virtual-reality, tangible-computing, ubiquitous-computing, conversational-ui, agentic-ui, brain-computer-interface, multimodal-fusion]
root_concepts: [emerging-interfaces]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Emerging Interfaces — Post-WIMP Paradigms Under an Evidence Bar

**This guide owns** the post-WIMP interaction **paradigms** — immersive (AR/VR/XR), tangible and
ubiquitous computing, conversational and agentic UI, brain-computer interfaces **as an interaction
channel**, and multimodal fusion — framed as *paradigms of interaction*, not a product tour, and held
to an explicit **hype-vs-evidence** bar. **It builds on** `02` (interaction models), `03` (the
modality substrate), and `05`/`06` (the evaluation and evidence discipline it enforces). **It
explicitly defers**: *model internals* behind conversational/agentic UI to `ai-engineering/` and
`machine-learning-theory/`; *rendering/graphics internals* of immersive systems to
`computer-graphics/`; *neuroscience* of BCI to `neuroscience/`; *operator-workload/safety* of any
high-consequence deployment to `human-factors/`; and *the statistics* of any study to
`statistics-applied/`.

> **This module is an educational reference. Emerging-interface capabilities are described honestly,
> **without hype-as-fact**: a demo is not a shipped capability, and a vendor claim is not evidence.
> These paradigms raise real safety concerns (cybersickness, photosensitive risk, neural/data
> sensitivity); this guide owns the *interaction* design and defers *safety certification* to
> `human-factors/` and *legal/privacy duty* to `law/`. Named frameworks are attributed and dated.**

*Per-guide banner: numbers about emerging interfaces are **unresolved by construction**. Novelty
effects inflate early metrics, samples are tiny and self-selected (enthusiasts with the hardware),
and the measuring instruments are often **unvalidated for the new modality**. This guide reports such
numbers **as unresolved** and stays **formative** until an instrument is validated for the paradigm;
presenting a novelty-inflated metric as a settled effect is the error this guide exists to prevent.*

---

## The Big Picture: New Paradigms, Old Evidence Discipline

The frontier is not one technology but a set of **paradigms** that break the WIMP assumptions (a
single 2-D screen, a precise pointer, discrete widgets). Each moves interaction somewhere new — into
the world, onto objects, into language, into the body. The constant across all of them is the
**evidence problem**: the field is loud with demos and claims, and the discipline is to ask *what
would actually count as evidence here, and do we have it?*

```
  THE POST-WIMP PARADIGM MAP (framed as paradigms, not products)
  ------------------------------------------------------------------
   IMMERSIVE (AR/VR/XR) ...... interaction INSIDE a rendered/blended space
   TANGIBLE / UBIQUITOUS ..... interaction THROUGH physical objects & environment
   CONVERSATIONAL / AGENTIC .. interaction IN LANGUAGE; delegating to an agent
   BRAIN-COMPUTER INTERFACE .. interaction via neural signals (as an input channel)
   MULTIMODAL FUSION ......... combining channels (speech + gesture + gaze + ...)
  ------------------------------------------------------------------
   Cross-cutting EVIDENCE DISCIPLINE (the spine of this guide):
     NOVELTY effect ....... "wow" inflates early usage/satisfaction, then fades
     SELF-SELECTION ....... samples are enthusiasts who own the hardware
     UNVALIDATED INSTRUMENTS metrics/questionnaires unproven for the new modality
     DEMO != DURABLE ...... a staged demo is not a shipped, everyday capability
  ------------------------------------------------------------------
```

**Bridge (software).** Treat every emerging-interface claim like a **benchmark from a vendor on their
own rig**: interesting, directional, and not evidence about your workload until independently
reproduced on a representative sample with a validated harness. The move you already make — "cool
demo; where's the reproducible measurement on a real population?" — is exactly the discipline this
guide enforces.

---

## 1. The Evidence Discipline — Why Most Numbers Here Are Unresolved

This is the guide's spine, stated before any paradigm so every claim below inherits it.

```
  READING AN EMERGING-INTERFACE CLAIM (the hype-vs-evidence checklist)
  ------------------------------------------------------------------
   1. NOVELTY: was usage/satisfaction measured before the novelty wore off?
      (a longitudinal study is needed; a first-session "delight" is not an effect)
   2. SAMPLE: who was in it? enthusiasts who bought the headset are SELF-SELECTED;
      the result doesn't transfer to the general population (external validity, 06)
   3. INSTRUMENT: was the metric VALIDATED for this modality? (a SUS or a presence
      questionnaire may not measure what it claims in VR; construct validity, 06)
   4. CONFOUNDS: cybersickness, fatigue, and learning confound performance numbers
   5. DEMO vs DURABLE: a controlled demo is not an everyday, at-scale capability
  ------------------------------------------------------------------
   DEFAULT VERDICT: "promising, UNRESOLVED." Stay FORMATIVE (find & fix, guide 05)
   until a validated instrument on a representative sample gives a real measurement.
```

The failing test from the scaling contract: reporting a **novelty-inflated** metric ("users completed
tasks 40% faster in VR!") as a **settled effect**, when it came from a first-session, self-selected,
unvalidated-instrument study. The honest report names it *unresolved by construction* and treats the
paradigm's evaluation as formative until the instruments catch up.

---

## 2. Immersive — AR / VR / XR

The immersive paradigm places interaction **inside** a rendered or blended space, along Milgram &
Kishino's **reality-virtuality continuum** (**1994**: real → augmented reality → augmented virtuality
→ virtual), collectively "mixed" or "extended" reality (XR).

- **Presence and immersion.** *Immersion* is the system's technical fidelity; *presence* is the user's
  felt "being there." Presence is measured with questionnaires (e.g., Witmer & Singer, **1998**) whose
  **validity is itself debated** — a live example of the unvalidated-instrument problem (§1). Report
  presence scores as contested constructs, not hard measurements.
- **Interaction challenges (what's genuinely hard).** Locomotion (moving through a space larger than
  the room without sickness), **selection/manipulation at a distance**, **text entry** (no keyboard),
  and **cybersickness** — measured by the Simulator Sickness Questionnaire (Kennedy et al., **1993**),
  a real confound with **demographic variation** in susceptibility. These are the `02`/`03` gulfs and
  modalities in a 3-D setting.
- **Deferral.** The rendering, tracking, and display internals are `computer-graphics/`'s; this guide
  owns the *interaction techniques* and their (mostly formative) evaluation.

---

## 3. Tangible and Ubiquitous Computing — Interaction in the World

The counter-paradigm to "stare at a screen": computing **embedded in physical objects and the
environment**. Its lineage (from `01`): Weiser's **ubiquitous computing** (**1991**) and **calm
technology** (Weiser & Brown, **1996**); Ishii & Ullmer's **"Tangible Bits"** (**1997**), coupling
digital information to graspable physical objects; and Dourish's **embodied interaction** (*Where the
Action Is*, **2001**), grounding interaction in our physical and social being-in-the-world.

The interaction claims worth holding: tangibles leverage **physical affordances and two-handed,
spatial skills** the GUI can't; ubicomp aims to move computing to the **periphery of attention** (calm
technology). The honest limits: tangibles are hard to make general or reconfigurable (a physical
control does one thing), and "calm" ambient displays are easy to propose and hard to prove *not*
annoying — again a formative-evaluation posture (§1).

---

## 4. Conversational and Agentic UI — Interaction in Language

Interaction in natural language, and delegation to software **agents**. As an *interaction paradigm*
(the model internals — LLMs, ASR, dialogue — are `ai-engineering/`'s):

```
  THE GULFS OF A LANGUAGE INTERFACE (guide 02, in a new setting)
  ------------------------------------------------------------------
   GULF OF EXECUTION .. "what can I say?" -- an invisible, unbounded command
                        space; no menu to scan. Discoverability is the core problem.
   GULF OF EVALUATION . "did it understand? did it do the right thing?" -- output
                        may be fluent but wrong; fluency != correctness.
   GROUNDING & REPAIR . misunderstanding is frequent; cheap correction is essential
                        (common ground, guide 09, applied to human-agent dialogue)
  ------------------------------------------------------------------
```

**Agentic UI** (an agent that takes multi-step action on the user's behalf) adds interaction problems
this guide owns: **delegation and oversight** (what did it do, can I review/undo it?), **trust
calibration** (the danger of **automation bias** — over-trusting automation; cited from Parasuraman &
Riley, **1997**, and Lee & See, **2004**; the mechanism is `cognitive-science/`/`human-factors/`), and
**mixed-initiative** design (Horvitz, **1999**: when should the system act vs ask?). Two honesty
points a peer must hold: **fluency is not correctness** (a confident wrong answer is a specific, severe
evaluation-gulf failure), and **anthropomorphic framing** ("the assistant understands you") can inflate
trust past what the system earns — a `11` concern when it's used to extract over-reliance.

---

## 5. Brain-Computer Interfaces — As an Interaction Channel

BCIs read neural signals as an **input channel** (the neuroscience is `neuroscience/`'s; this guide
owns only the interaction framing). The sober picture, against heavy hype:

- **It is a low-bandwidth, noisy input channel (dated, and bounded).** Non-invasive (EEG) BCIs have
  **low information-transfer rates** and high error, requiring training and calibration — the
  characterization from the foundational review (Wolpaw et al., *Clinical Neurophysiology*, **2002**),
  still broadly current for consumer EEG. The **research** high-water mark is **invasive/intracortical**
  and recent: single-participant demonstrations reached ~**90 characters/min** (imagined handwriting;
  Willett et al., *Nature*, **2021**) and ~**60–78 words/min** for attempted-speech decoding (Willett
  et al., *Nature*, **2023**; Metzger et al., *Nature*, **2023**) — impressive, but **small-N research
  demonstrations** (often one implanted participant), carrying surgical risk, **not** a shipped or
  consumer capability. The honest framing is a *narrow, effortful, and still largely experimental
  input channel*, not telepathy.
- **Its clearest value is accessibility.** For users with severe motor disability, even a low-bandwidth
  channel can restore communication or control — a `08` access modality of real importance, to be
  designed and evaluated with the same rigor and *with* those users.
- **The evidence and ethics flags are large.** Most consumer BCI claims are demos or novelty; neural
  and intent data are maximally sensitive (a `law/`/privacy and `11` concern); and any clinical or
  safety-critical use defers safety analysis to `human-factors/` and clinical judgment to `medicine/`.
  Report capabilities as *promising and unresolved*, never as settled.

---

## 6. Multimodal Fusion — Combining Channels

Combining input channels so they **complement** each other — the paradigm's origin is Bolt's
**"Put-That-There"** (**1980**: point while speaking, resolving "that" by gaze/gesture and the command
by speech). Multimodal interaction works when the channels are **complementary** (speech names, gesture
locates; each covers the other's weakness) and **redundant where it matters** (a critical action
confirmable more than one way — a `03`/`08` requirement).

The hard parts this guide owns: **fusion** (aligning inputs across channels in time and meaning),
**error compounding** (each channel has its own error rate; naive fusion can multiply them), and
**mode/attention management** across channels. Multimodal claims inherit the full evidence discipline
(§1) — the "natural, effortless" framing is a hypothesis, usually tested on tiny expert samples.

---

## A Worked Evidence Read (illustrative, fictional)

*Fictional, to show the hype-vs-evidence discipline applied to a claim. No real product.*

**Claim.** *Vantage*, a fictional VR training vendor, advertises: **"Trainees learn 42% faster in our
VR module and rate it 9/10."**

- **Novelty (§1.1).** The study measured a **first session**. VR's novelty reliably inflates
  engagement and self-rated satisfaction; without a **longitudinal** design showing the gain persists
  after the wow fades, the "42% faster" is **unresolved**, not an effect.
- **Sample (§1.2).** Participants were **volunteers who liked VR** (self-selected enthusiasts) —
  external validity is weak; the result doesn't transfer to the general trainee population (`06`).
- **Instrument (§1.3).** "9/10" came from an **ad-hoc satisfaction item** unvalidated for VR, and the
  "42%" used a task metric not shown to mean the same thing in VR as on a screen (construct validity).
  And "42%" is reported **with no sample size, estimator, or CI** — under `05`'s discipline it is not a
  measurement at all.
- **Confounds (§1.4).** No mention of **cybersickness** dropout (susceptible participants may have left
  the study, biasing the sample) or of learning/fatigue confounds.
- **Verdict.** **"Promising, unresolved."** The honest program stays **formative**: run a longitudinal
  study on a representative sample with a **validated** learning-outcome measure and a real difference
  test (`05` §6; stats → `statistics-applied/`) before claiming a durable effect. The interaction-design
  work (locomotion, selection, sickness mitigation, and — a carried invariant — **accessibility** for
  trainees who can't use a standard headset, plus a non-VR alternative) proceeds regardless.

**Reading.** The claim was not dismissed and not believed — it was **read against the evidence
checklist**, its numbers reported as **unresolved by construction**, and the evaluation kept
**formative** until validated instruments exist. That is the discipline the paradigm requires.

---

## Reader Tasks (answerable from this guide)

1. **Apply the evidence checklist.** Given "users are 30% more productive with our AR glasses (n
   reported: 8 employees, one session)," walk the novelty / self-selection / unvalidated-instrument /
   demo-vs-durable checks and state the honest verdict (promising, unresolved).
2. **Diagnose a language-interface gulf.** Given "users don't know what to ask our chatbot," name the
   gulf (execution — invisible command space) and two interaction fixes (suggested prompts, cheap
   repair), citing the discoverability problem.
3. **Calibrate trust in an agent.** Given an agentic tool that "handles your inbox," name the oversight
   and automation-bias risks (fluency ≠ correctness; over-reliance), and the interaction affordances
   that mitigate them (review, undo, visible actions).
4. **Frame sensitive and multimodal interfaces honestly.** Explain why a consumer "mind-reading"
   headset is a low-bandwidth, noisy input channel (promising for accessibility, unresolved as a
   mass modality) and why its data are especially sensitive (`11`, `law/`). Then, for a hands-busy
   AR repair task, combine speech (naming) and gaze/gesture (locating) so each covers the other's
   weakness, with redundant confirmation for the critical step (`03`/`08`).
5. **Hold a tangible/ubicomp claim to the evidence bar.** Given "our calm ambient dashboard cut
   interruptions and everyone loved the tangible dial," name what tangibles genuinely buy (physical
   affordances, two-handed/spatial skill, the **periphery of attention** — calm technology) and their
   honest limits (a physical control does one thing; "calm" is easy to propose and hard to prove *not*
   annoying), and say why the result stays **formative** until a longitudinal field study on a
   representative sample confirms it (§1, §3).

---

## Decision Cheat Sheet

| Situation | Do | Because (this guide) |
|-----------|----|--------------------|
| any emerging-interface metric | run the **evidence checklist**; default "unresolved" | novelty / self-selection / unvalidated instruments (§1) |
| an early "delight/faster" result | demand a **longitudinal** study | novelty inflates first-session numbers (§1) |
| a VR/AR selection or locomotion problem | treat as `02`/`03` **gulfs/modalities in 3-D** | it's interaction design; rendering → `computer-graphics/` (§2) |
| a tangible / ambient ("calm") design claim | credit affordances/periphery; keep it **formative** until field-proven | a tangible does one thing; "calm" is hard to prove non-annoying (§3) |
| "what can I say?" to an agent | fix **discoverability**; suggest prompts | invisible command space (execution gulf) (§4) |
| an agent that acts for the user | design **oversight + undo + visible actions** | automation bias; fluency ≠ correctness (§4) |
| a "mind-reading" BCI claim | read as **low-bandwidth, sensitive, unresolved** | hype-vs-evidence + data sensitivity (§5) |
| combining channels | design for **complementarity**, guard error compounding | multimodal fusion trade-offs (§6) |
| any safety-critical deployment | route safety to **`human-factors/`**, legal to **`law/`** | this guide owns interaction, not certification |
| the model/rendering/neural internals | defer to `ai-engineering/` / `computer-graphics/` / `neuroscience/` | HCI owns them as *paradigms* |

---

## Common Confusion Points

**"Studies show VR training is dramatically better."** Most such numbers are **first-session, self-
selected, unvalidated-instrument** results inflated by novelty. Until a longitudinal study on a
representative sample with a validated measure and a difference test says so, treat the gain as
**unresolved** (§1, worked case).

**"The AI assistant understood me, so it's reliable."** Fluency is not correctness. A confident, fluent
output can be wrong — a severe evaluation-gulf failure — and anthropomorphic framing inflates trust past
what the system earns. Design for oversight and repair (§4).

**"BCIs let you control computers with your mind."** Today they are **low-bandwidth, noisy input
channels** needing training; their clearest value is **accessibility** for users with severe motor
disability, and their data is exceptionally sensitive. Consumer "mind-reading" claims are demos/novelty
(§5).

**"Multimodal interfaces are natural and effortless."** A hypothesis, usually tested on tiny expert
samples. Multimodal works when channels are **complementary**, but fusion and **error compounding** are
hard, and "natural" doesn't survive the evidence checklist unexamined (§6).

**"It's the future, so we should ship it now."** A demo is not a durable, at-scale capability, and being
early is not evidence of working. The paradigm may be the future *and* the current metric be unresolved
— both can be true (§1).

---

## Global, WEIRD, and Resource Caveats

- **The hardware is expensive and unevenly available, which biases the evidence.** Headsets, sensors,
  and BCI rigs are costly; studies over-sample wealthy, Western, able-bodied enthusiasts, so the
  evidence base is **doubly WEIRD** (novelty *and* self-selection). Generalizing it to a global or
  general population is unwarranted.
- **Bodies and abilities are not uniform.** Cybersickness susceptibility varies by demographic; VR/AR
  often assume stereo vision, full mobility, and standard hand function; voice assumes fluent speech in
  a supported language (`03` ASR caveats); BCI signals vary across people. An emerging interface that
  "works" for the demo population can exclude many — accessibility and alternatives are first-class, not
  afterthoughts (`08`).
- **The carried invariants ride hardest here.** *Accessibility of the sample and of the interface:* new
  paradigms must be designed and evaluated **with** disabled users and always paired with an accessible
  alternative channel (`08`); a headset-only or voice-only path strands part of the population.
  *Safety/ethics floor:* no hype-as-fact, no manipulation via anthropomorphism or over-trust (`11`),
  neural/behavioral data treated as sensitive (`law/`), and any physical-harm risk (photosensitivity,
  sickness, fatigue) routed to `human-factors/` for safety analysis — this guide certifies nothing.
