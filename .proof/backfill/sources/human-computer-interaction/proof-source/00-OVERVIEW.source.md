---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-computer-interaction:overview
kind: guide
module: human-computer-interaction
section: human-computer-interaction
title: Human-Computer Interaction - Overview and Discipline Map
status: source-custody
source_custody: partial
current_path: human-computer-interaction/00-OVERVIEW.md
canonical_path: human-computer-interaction/00-OVERVIEW.md
backsource_ids: [proof-backfill:human-computer-interaction:00-overview]
concepts: [human-computer-interaction, discipline-map, design-evaluate-loop, ownership-boundaries, safety-ethics-contract]
root_concepts: [human-computer-interaction]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Human-Computer Interaction — Overview and Discipline Map

**This guide owns** the module's *map*: what `human-computer-interaction/` is, how its
twelve guides divide the territory with **no gap and no overlap** (the ownership matrix),
what the whole module **defers** to sibling modules and why, the **design↔evaluate loop**
that organizes it, the discipline's **concise shared spine** (the datable anchors every guide
cites; the *detailed* lineage is `01`'s), the **safety/ethics contract** every guide
inherits, and the **reading order**. It owns no method of its own — each method lives in a
numbered guide; `00` only guarantees that the methods together cover the field once each.
**It builds on** nothing (it is the entry point). **It explicitly defers** every mechanism,
proof, and obligation the module rests on: cognitive **mechanisms**, Fitts/Hick
performance-law derivations, and memory/load constructs to `cognitive-science/` (esp.
`cognitive-science/09-APPLIED-BRIDGE`), while HCI owns engineering models such as GOMS;
**inferential statistics** to `statistics-applied/`;
Norman's action model and interaction design **at the physical-product level** to
`industrial-design/06-INTERACTION-DESIGN` (and product ergonomics to `industrial-design/05`);
**operator performance, workload, human-error, and safety-critical integration** to
[`human-factors/`](../human-factors/00-OVERVIEW.md); and **legal obligation** to `law/`.

> **This module is an educational reference on *how interactive computing systems are
> designed and evaluated*. It is **not** a manipulation/dark-pattern playbook, **not** legal
> or compliance advice, and **not** safety-certification guidance. Persuasive techniques are
> described to *recognize and refuse*, never to execute; standards and named "laws" are
> attributed, dated, and bounded; heuristics are heuristics, not laws; and conformance is a
> floor, not usability.**

*Per-guide banner: `00` is a coverage-and-boundary map. It states which guide owns each
concept and what the module defers; if any claim here conflicts with a guide's own text, the
guide governs and this map is the bug. Dates on standards and lineage below are to their
published sources.*

---

## The Big Picture: A Lifecycle Wrapped in Cross-Cutting Concerns

HCI is the discipline of **designing and evaluating interactive computing systems for human
use**. The single most important structural decision (ratified in the module architecture) is
to organize it **by the design↔evaluate lifecycle and its cross-cutting concerns — not by
platform (web/mobile/VR), which dates instantly, and not by re-teaching cognitive science,
which lives next door.** The twelve guides are two rings: an inner *lifecycle* and an outer
set of *cross-cutting concerns* that ride every stage.

```
  THE HCI MODULE — LIFECYCLE (inner) + CROSS-CUTTING CONCERNS (outer)
  ==================================================================
   00 OVERVIEW ....... this map: ownership, defers, safety contract, reading order

   THE LIFECYCLE (a loop, read clockwise)
   ------------------------------------------------------------------
    01 HISTORY ........ where the idioms came from, and why they persist
    02 INTERACTION .... models of how a person and a system act on each other
       MODELS
    03 I/O MODALITIES . the input/output substrate the interaction runs on
    04 DESIGN PROCESS . GENERATE candidate designs  ---------------+
    05 USABILITY ...... EVALUATE: measure & diagnose  <------+     |
       EVALUATION                                            |     |
    06 RESEARCH ....... study humans & context to feed both  |     |
       METHODS                                          iterate    generate
                                                              +-----+
   CROSS-CUTTING CONCERNS (ride every lifecycle stage)
   ------------------------------------------------------------------
    07 IA / VISUALIZATION ... structuring & showing information
    08 ACCESSIBILITY ........ the full range of human ability (an invariant)
    09 SOCIOTECHNICAL/CSCW .. interaction among many people, over time
    10 EMERGING INTERFACES .. post-WIMP paradigms, held to an evidence bar
    11 PRACTICE & ETHICS .... the profession and its refusals
  ==================================================================
   Read the inner ring as a loop: design (04) proposes, evaluation (05) disposes,
   research (06) informs both, and history/models/modalities (01-03) are the
   ground the loop stands on. The outer ring applies at every point of the loop.
```

**The loop is the spine.** `04-DESIGN-PROCESS` *generates* candidate designs; `05-USABILITY-
EVALUATION` *measures and diagnoses* them; the gap between them is closed by *iteration*.
`06-RESEARCH-METHODS` feeds both by studying people and contexts. Everything else either
grounds the loop (`01` history, `02` models, `03` modalities) or crosses it (`07`–`11`).

**Bridge (software).** The whole module is a **software-engineering discipline pointed at the
human side of the system**. The design↔evaluate loop is your **build↔test loop**; `04` is
*authoring*, `05` is *testing and profiling*, `06` is *instrumentation and telemetry design*,
`02` is your **interaction/state model**, `03` is the **I/O and driver layer**, `07` is
**information architecture and observability dashboards**, `08` is **API contracts + graceful
degradation for the full client population**, `09` is **distributed/multi-user systems**, `10`
is **the experimental branch you gate behind evidence**, and `11` is **the code of conduct and
the review gate**. None of it replaces the disciplines it sits on — it composes them.

---

## Ownership Matrix — Each Concept Claimed Exactly Once (MECE)

The module's integrity rule: **every concept the module owns appears in exactly one guide.**
No gaps (an owned concept with no home) and no overlaps (a concept claimed twice). Read this
as the contract; each guide's own ownership header must agree with its row.

| # | Guide | Uniquely owns (claimed nowhere else in the module) |
|---|-------|----------------------------------------------------|
| 00 | Overview | the map, the ownership/defer matrices, the safety contract, reading order |
| 01 | History & Intellectual Roots | the intellectual lineage (memex→augmentation→GUI→web→mobile→post-GUI) and *why history constrains today's idioms* |
| 02 | Interaction Models | models of interaction **applied to computing** — gulfs, direct manipulation, modes, instrumental interaction, distributed cognition/activity theory applied |
| 03 | Input/Output Modalities | the I/O substrate — pointing/typing/touch/gesture/voice/gaze/displays; the device/technique catalog; Fitts/Hick **cited and applied** |
| 04 | Design Process | the *generate* half — UCD, double diamond, design thinking, requirements, personas, scenarios, prototyping fidelity, design systems |
| 05 | Usability Evaluation | the *measure/diagnose* half — inspection, empirical testing, the metric triad, SUS limits, formative/summative, A/B vs usability, triangulation, the sample-size ceiling |
| 06 | Research Methods | studying people/context — field studies, interviews, surveys, diary/ESM, ethnography, experiment design **for HCI**, mixed methods, research ethics |
| 07 | IA & Visualization | structuring & showing information — IA, navigation, findability, search UX, interactive data visualization, the visual-encoding grammar |
| 08 | Accessibility & Inclusive Design | interactive accessibility — disability models, WCAG (dated), the accessibility tree, access by channel, conformance-vs-usability, inclusion beyond disability, governance |
| 09 | Sociotechnical / CSCW | interaction among many people — groupware, awareness, coordination, common ground, social translucence, sociotechnical fit |
| 10 | Emerging Interfaces | post-WIMP paradigms — AR/VR/XR, tangible/ubiquitous, conversational/agentic, BCI **as interaction**, multimodal fusion; the hype-vs-evidence discipline |
| 11 | Practice & Ethics | the profession — teams/roles, critique, persuasive-design **ethics** (recognize-and-refuse), value-sensitive design, sustainability, the ethics contract |

**Two boundary calls worth stating explicitly, because they are the ones that could
double-claim:**

- **`02` vs `03`.** `02` owns *models of interaction* (how action and evaluation are
  structured); `03` owns the *physical substrate* those models run on (the devices and
  techniques). Fitts' Law is *applied* in `03` (a modality-performance law) and *referenced*
  in `02`; it is **derived** in neither — that is `cognitive-science/09`.
- **`05` vs `06`.** `05` owns *usability evaluation* (measuring/diagnosing a specific design);
  `06` owns *research methods* (studying people and contexts, which may or may not involve a
  design under test). A usability test is a `05` object; an ethnography of a workplace is a
  `06` object; a summative benchmark's *statistics* belong to neither — they are
  `statistics-applied/`.

---

## Defer Matrix — What the Whole Module Names but Never Re-Derives

HCI is a *composing* discipline: it stands on mechanisms and obligations it does not own. It
**names them by reference and never rebuilds them.**

| Defers to | For | Why (the seam) |
|-----------|-----|----------------|
| `cognitive-science/09` (+ `01`–`08`) | cognitive mechanisms; Fitts/Hick performance-law derivations; memory/load constructs; perception/attention | HCI cites and applies these foundations and owns engineering models such as GOMS plus design/evaluation methods |
| `statistics-applied/` | general **inferential statistics** — hypothesis tests, power, confidence intervals, regression, corrections | HCI states *which* estimate/test a study needs and *why*; the machinery lives there |
| `industrial-design/06`, `/05` | Norman's action model & interaction design **at product level**; physical anthropometry/ergonomics | HCI `02` applies the action model to *interactive computing*; the physical-product framing stays there |
| [`human-factors/`](../human-factors/00-OVERVIEW.md) | **operator performance & safety evidence** — workload, human-error taxonomy, safety-critical human-system integration | HCI owns interaction/visualization/accessibility methods; HF supplies workload/error/performance-under-stress evidence; accountable domain organizations own acceptance |
| `law/` | **legal obligation** — accessibility statutes, privacy law, liability, compliance duty | HCI names the standards landscape (dated); it never adjudicates whether anyone is compliant |
| `psychology/` | experimental-psychology foundations; DSM; psychotherapy | HCI `06` applies study design *to HCI questions*, not psychological theory |
| `data-science/`, `computer-graphics/` | statistical-graphics theory; rendering/pipeline internals | HCI `07` owns *interactive* visualization; the estimator theory and render pipeline live there |
| `ai-engineering/`, `machine-learning-theory/` | model internals behind conversational/agentic/recommender UIs | HCI `10` owns them *as interaction paradigms*; the models live there |
| `linguistics/`, `typography/` | writing-system/script/type mechanisms behind localization/legibility | HCI `08` owns the *interaction* responsibility; the script/type mechanics live there |
| `medicine/`, `disease/` | clinical/medical models of disability, diagnosis, rehabilitation | HCI `08` uses the *interaction/social* model of disability, not the diagnosis |

---

## The Three-Way Seam: HCI ↔ Human Factors ↔ Law

The module's sharpest boundary — sharpest because all three touch the same interfaces — is a
**three-way split** that `08` demonstrates and every safety-adjacent guide inherits:

```
  WHO OWNS WHAT AT A HIGH-CONSEQUENCE INTERFACE (e.g., a clinical-device UI)
  ------------------------------------------------------------------
   HCI (this module) .... interaction DESIGN & its usability/accessibility
                          EVALUATION — can a person perceive/operate/understand it?
   human-factors/ ....... OPERATOR PERFORMANCE & SAFETY — workload, error
                          consequence, performance under stress/fatigue
   law/ ................. LEGAL OBLIGATION — is it required, by whom, with what
                          liability? Named here as dated landscape only.
  ------------------------------------------------------------------
   Neither re-derives the others. HCI never rules on compliance or certifies safety.
```

---

## Lineage — The Concise Shared Spine (the route; `01` owns the detail)

`00` owns only the **concise shared spine** — the handful of datable anchors every guide can cite
as common ground, and the **route** into the full story. The **detailed intellectual lineage** (the
narrative from memex through post-GUI, and *why* each idiom persists) is **`01`'s alone**; this
section names the anchors and points to it, it does not retell it:

- **The founding synthesis:** Card, Moran & Newell, *The Psychology of Human-Computer
  Interaction* (**1983**) — the book that named the field and imported cognitive modeling
  (GOMS) into system design.
- **The professional home:** ACM **SIGCHI** (founded **1982**; the CHI conference series from
  **1983**) — the community whose curricula give the module its map.
- **The standards backbone:** ISO **9241** — usability as effectiveness/efficiency/
  satisfaction-in-context (`9241-11`, 1998; rev. 2018) and human-centred design (`9241-210`).

`01` traces the deeper roots (Bush's memex, 1945; Engelbart's augmentation, 1962–68; the Xerox
PARC/Star GUI lineage) that explain *why* today's idioms exist. Dates are load-bearing: an
idiom's age often explains its persistence.

---

## The Safety / Ethics Contract (inherited by every guide)

Every guide embeds or references these five pillars. They are the module's review gate.

1. **No manipulation / dark-pattern playbook.** Persuasive and attention-engineering
   techniques are described *to recognize and ethically refuse*, never as actionable coercion,
   deception, or addiction design. Any actionable manipulation recipe is a **BLOCK** (`11`,
   and the A/B-metric caveat in `05`).
2. **No legal / compliance advice.** Accessibility and privacy law is **dated landscape**
   only; the module never rules on compliance or obligation (that is `law/`; sharpest in
   `08`).
3. **No safety-certification guidance.** For interfaces whose failure risks harm, HCI owns the
   interaction/usability method only; operator-performance/safety defers to `human-factors/`.
4. **Research ethics as concept, not IRB substitute.** Human-subjects guidance (consent,
   welfare, privacy, compensation, accessible participation) is principle-level (`06`, `08`),
   never a warrant to skip ethics review.
5. **Standards and "laws" are attributed, dated, and bounded.** WCAG versions, statutes, and
   named "laws" (Fitts, Hick) carry dates; **heuristics are heuristics, not laws**, and
   **conformance is a floor, not usability**.

**Two invariants ride every guide, whatever its topic** (propagated from `08` and named in
`05`'s scaling contracts): (1) *Accessibility of the sample* — disabled users and their
assistive technology are a **first-class segment**, sized per segment, never a final-audit
afterthought; a study that silently excludes them is under-powered for the population, not
done. (2) *Safety/ethics floor* — the five pillars above hold regardless of method or metric.

---

## Reading Order

```
  READING MAPS (pick your entry)
  ------------------------------------------------------------------
  FULL PASS (recommended)  00 -> 01 -> 02 -> 03 -> 04 -> 05 -> 06
                           -> 07 -> 08 -> 09 -> 10 -> 11
  "I BUILD PRODUCTS"       00 -> 04 -> 05 -> 02 -> 03 -> 08 -> 11
  "I DO RESEARCH"          00 -> 06 -> 05 -> 02 -> 09
  "I CARE ABOUT REACH"     00 -> 08 -> 03 -> 07 -> 09
  "WHAT'S NEXT?"           00 -> 02 -> 10 (held to 05's evidence bar) -> 11
  ------------------------------------------------------------------
  05 and 08 were authored first, as boundary prototypes; they are the
  module's honesty spine (discovery != measurement; conformance != usability).
```

---

## Reader Tasks (answerable from this guide)

1. **Route a question to its owning guide.** Given "how many users do I need to *claim* a
   completion rate?", "is my status-by-color accessible?", and "why does this menu feel
   modal?", name the owning guide (`05`; `08`; `02`) and the module it ultimately defers the
   *mechanism/stat* to (`statistics-applied/`; none — `08` owns it; `cognitive-science/`).
2. **Detect a boundary violation.** Given a draft `03` section that *re-derives* Fitts' Law
   from first principles, state which rule it breaks (defer derivation to
   `cognitive-science/09`; `03` only cites/applies) and how to fix it.
3. **Apply the safety contract.** Given "our guide should include the exact copy that maximizes
   sign-up regret before users notice," state which pillar it violates (pillar 1) and that the
   correct treatment is recognize-and-refuse in `11`, not a recipe.
4. **Place a high-consequence interface.** For an infusion-pump UI, split the work three ways:
   HCI owns interaction design + usability/accessibility evaluation; `human-factors/` owns
   operator workload/error/safety; `law/` owns legal obligation.
5. **Justify the organization.** Explain why the module is not organized as "web UX / mobile UX
   / VR UX" (platform organization dates instantly and duplicates content) and what organizes
   it instead (the design↔evaluate lifecycle + cross-cutting concerns).

---

## Decision Cheat Sheet

| I want to… | Read | Because |
|------------|------|---------|
| understand where an idiom came from | `01` | history constrains today's idioms |
| reason about *how* a UI is acted on | `02` | interaction models (applied) |
| choose an input/output technique | `03` | the modality substrate + applied Fitts/Hick |
| *generate* a design | `04` | the design process (hypotheses, not results) |
| *measure/diagnose* a design | `05` | usability evaluation (discovery ≠ measurement) |
| study users/contexts | `06` | research methods (each with its own validity contract) |
| structure/show information | `07` | IA & interactive visualization |
| reach the full range of ability | `08` | accessibility (conformance ≠ usability) |
| design for groups over time | `09` | sociotechnical/CSCW |
| evaluate a post-WIMP paradigm | `10` | emerging interfaces, held to the evidence bar |
| know what a professional refuses | `11` | practice & ethics |
| the *mechanism/law* behind an effect | `cognitive-science/09` | HCI defers derivation |
| the *statistics* behind a study | `statistics-applied/` | HCI defers the machinery |
| whether I'm *legally required* to | `law/` | HCI never adjudicates obligation |

---

## Common Confusion Points

**"HCI is just UI design / just usability testing."** No. Design (`04`) and evaluation (`05`)
are two stages of one loop, and the loop sits inside history, models, modalities, research,
IA, accessibility, collaboration, emerging paradigms, and ethics. Reducing the field to either
half loses the other half and all the cross-cutting concerns.

**"HCI owns Fitts' Law / cognitive load / the Norman action model."** No. HCI *applies* those;
the **derivations** live in `cognitive-science/09` (the laws and mechanisms) and
`industrial-design/06` (the action model at product level). This module cites and uses; it
does not re-teach.

**"HCI is organized by platform."** No. It is organized by the design↔evaluate lifecycle plus
cross-cutting concerns, precisely because a platform organization (web/mobile/VR) dates
instantly and duplicates content across guides. `10` is the only paradigm-specific guide, and
it is framed as *paradigms* under an evidence bar.

**"Accessibility is a chapter you can skip if you're short on time."** No. `08` is a full guide
*and* an invariant: its accessibility-of-the-sample and safety/ethics floor ride every other
guide, whatever the method.

**"If the module names a standard or a law, it's telling me what's required or true."** No.
Standards and named laws are **dated, attributed, and bounded** landscape. WCAG conformance is
a floor, not usability; a passing usability score is one instrument's reading; legal obligation
is `law/`'s to state, not this module's.

---

## Global, WEIRD, and Resource Caveats

- **The method and standards canon is WEIRD- and resource-rich-first.** Much of HCI's method
  base was validated on Western, educated, tech-literate, English-speaking convenience samples
  (Henrich et al. 2010); its dominant standards, tools, and assistive technologies skew to
  English/Latin scripts and well-resourced settings. Every guide flags where its methods,
  instruments, or "laws" do not transport unexamined.
- **Bandwidth, device, and literacy are first-order, not caveats.** For much of the world the
  binding constraint is a low-end phone on metered data with mixed literacy in a non-dominant
  language; `08` and `03` treat this as a design context to *work*, not a footnote to append.
- **The module is standalone and educational.** It is independently readable; external sources
  may support fact-checking but are not a completion gate. It is not legal, compliance, or
  safety-certification advice, and it names its own limits (e.g., digital-accessibility statute
  depth is deferred to `law/` and, as `08` notes, is not yet deeply covered there).
