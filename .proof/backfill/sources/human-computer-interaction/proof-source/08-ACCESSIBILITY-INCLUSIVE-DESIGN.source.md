---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "08-ACCESSIBILITY-INCLUSIVE-DESIGN.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-computer-interaction:accessibility-inclusive-design
kind: guide
module: human-computer-interaction
section: human-computer-interaction
title: Accessibility and Inclusive Design - Interactive Systems for the Full Range of Human Ability
status: source-custody
source_custody: partial
current_path: human-computer-interaction/08-ACCESSIBILITY-INCLUSIVE-DESIGN.md
canonical_path: human-computer-interaction/08-ACCESSIBILITY-INCLUSIVE-DESIGN.md
backsource_ids: [proof-backfill:human-computer-interaction:08-accessibility-inclusive-design]
concepts: [accessibility, inclusive-design, disability-models, wcag, assistive-technology, accessibility-tree, conformance-vs-usability]
root_concepts: [accessibility]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Accessibility and Inclusive Design — Interactive Systems for the Full Range of Human Ability

**This guide owns** the *interactive accessibility* of computing systems: how disabled
people perceive, operate, and understand interactive systems, and how to design and
evaluate for that. It covers models of disability; the distinction between
accessibility, usability, and inclusive/universal design; the WCAG standard (dated and
bounded); how assistive technology interacts with a system through the accessibility
tree; keyboard/focus/semantics; access by sensory/motor/cognitive channel; accessible
research; the gap between conformance and actual usability; the inclusive dimensions
beyond disability (localization, literacy, bandwidth); and accessibility governance.
**It builds on** `03-INPUT-OUTPUT-MODALITIES` (the modality substrate),
`02-INTERACTION-MODELS`, and `05-USABILITY-EVALUATION` (accessible evaluation extends
those methods). **It explicitly defers** three things by a hard three-way boundary:

```
  THE THREE-WAY OWNERSHIP BOUNDARY (memorize this seam)
  --------------------------------------------------------------
  HCI (this guide)   -> interactive accessibility DESIGN & EVALUATION:
                        can a disabled person perceive/operate/understand
                        this interface, and how do we build & test that?
  human-factors/     -> OPERATOR PERFORMANCE & SAFETY EVIDENCE:
                        workload, human-error, safety-critical human-system
                        integration -- performance under load, not interface reach
  law/               -> LEGAL OBLIGATION: statutes, liability, compliance duty.
                        Named here as dated landscape only; never adjudicated.
  --------------------------------------------------------------
  Rule: this guide describes how to MAKE and MEASURE accessible interaction.
  It does not rule on legal compliance and does not model operator safety.
```

It further defers *clinical/medical* models of disability to `medicine/`/`disease/`;
*cognitive mechanisms* of perception/attention/memory to `cognitive-science/`;
*physical anthropometry and product ergonomics* to `industrial-design/05` and
`human-factors/`; and *writing-system/type mechanics* behind localization to
`linguistics/`/`typography/`.

> **This module is an educational reference on *how to design and evaluate accessible
> interactive systems*. It is **not legal or compliance advice** — it names standards
> and laws as dated landscape, and never tells a reader whether they are compliant or
> what their legal obligations are (that is `law/`). It contains **no instructions for
> defeating, exploiting, or manipulating** assistive technology or users. Standards and
> "laws" are attributed and dated, and conformance is treated as a floor, never as a
> synonym for usability.**

*Per-guide banner: WCAG version/level references are dated to their published
Recommendation and are bounded technical claims, not compliance rulings. Prevalence and
tooling figures are attributed and treated as estimates that vary by region and year.*

---

## The Big Picture: Five Independent Axes, Not One Nested Word

"Accessibility" gets collapsed into a single word, and that conflation is the root of
most bad practice. It is better read as **five independent axes** — a design *process*,
a *conformance* check, a *task-capability* outcome, a *usability* outcome, and an
*equity* outcome — each measured differently and, crucially, **not contained inside one
another**. A product can score high on one axis and low on another; none of them is a
"floor" the rest are stacked on.

```
  FIVE INDEPENDENT AXES  (not one nested word)
  ==============================================================
   1  PARTICIPATORY / INCLUSIVE DESIGN PROCESS
      -> did disabled people shape discovery, design, evaluation?
   2  TECHNICAL CONFORMANCE
      -> does it meet the standard (WCAG)?   [audit: auto + manual]
   3  TASK ACCESSIBILITY
      -> can a disabled person perceive/operate/understand the
         real task with their own AT?        [AT walkthrough, tasks]
   4  USABILITY OUTCOMES
      -> effective / efficient / satisfying for disabled users?
   5  INCLUSION / EQUITY
      -> does it reduce exclusion across the whole population?
  ==============================================================
   INDEPENDENT, not nested: high conformance (2) with low task
   accessibility (3) is the classic "passes WCAG, unusable with a
   screen reader" state. No axis is a "floor" the others sit on.
```

- **Participatory / inclusive design process** — *how it was made*: did disabled people
  shape discovery, design, and evaluation (co-design and shared authority, not
  consultation-theatre)? A process axis, evidenced by *who* actually held decision
  authority (Sections 2, 7).
- **Technical conformance** — *does it meet the standard*: WCAG and related criteria,
  established by audit (automated + manual). A necessary scaffold, and only a scaffold
  (Sections 5–6).
- **Task accessibility** — *can a disabled person actually perceive, operate, and
  understand the real task with their assistive technology?* An outcome measured by AT
  walkthrough and task completion — related to conformance but not the same thing, and
  **not a single binary flag**: it is per person, per task, per AT, per context (§2–4).
- **Usability outcomes** — *is it effective, efficient, and satisfying for disabled
  users* as a first-class group (the `05` triad), not merely operable (Section 6).
- **Inclusion / equity** — *does it reduce exclusion across the whole population*,
  including the non-disability dimensions (language, literacy, bandwidth, age) of
  Section 8?

These axes interact but are **independent**: conformance without task accessibility is
the classic "passes WCAG, unusable with a screen reader" state (Section 6); usability for
most without inclusion still leaves definable groups out. Do not treat any one of them as
a floor the others automatically clear, and do not read accessibility as a single
binary flag — every axis is graded, contextual, and separately evidenced.

The second load-bearing idea is the **interaction/mismatch model** of disability
(Section 1): disability is not (only) a property of a person's body but a **mismatch
between a person's abilities and the demands of an environment** — which means the
*interface*, not the person, is frequently the thing that is "disabled," and is the
thing a designer can change.

**Bridge (software).** **Technical conformance** is your **public API contract**: a
screen reader is just another *client* consuming your interface through a defined
protocol (the accessibility tree, Section 3). Meeting the contract (conformance) is like
passing your **type checks and lint** — necessary, catches whole classes of breakage, and
absolutely *not* proof the product is fast, correct, or pleasant. Green CI ≠ good
product; WCAG-pass ≠ task-accessible-and-usable with a screen reader (Section 6). The
contract is one axis, not the whole product.

---

## 1. Models of Disability — The Model Decides What You Build

The model of disability you hold silently determines where you locate the problem and
therefore what you build. Four models, roughly historical:

| Model | Locates disability in | "Fix" implied | Design consequence |
|---|---|---|---|
| **Medical** | the individual's body/impairment | cure/rehabilitate the person | disability is someone else's (clinical) problem; nothing to design |
| **Social** (Oliver 1983) | society's barriers/exclusion | remove the barriers | the *environment/interface* is the problem to change |
| **Biopsychosocial / ICF** (WHO 2001) | interaction of body, activity, participation, context | reduce barriers *and* support function | function is contextual; measure participation, not just impairment |
| **Interaction / mismatch** (Microsoft Inclusive Design 2016) | the person↔environment *mismatch* | redesign the environment to fit more people | reframes disability as a *design* variable you control |

The interaction model adds the practically vital **permanent / temporary / situational**
spectrum: a mismatch with "one arm" can be *permanent* (limb difference), *temporary*
(a broken arm), or *situational* (holding a baby). Designing for the permanent case
serves the far larger temporary and situational populations too.

```
  THE PERSONA SPECTRUM (one ability, three durations) -- Microsoft 2016
  --------------------------------------------------------------
   ability      PERMANENT        TEMPORARY          SITUATIONAL
   ----------   --------------   ----------------   ----------------------
   see          blindness        cataract/dilation  bright sun / eyes on road
   hear         deafness         ear infection      loud bar / open office
   speak        non-verbal       laryngitis         heavy accent to an ASR
   touch/reach  limb difference  broken arm         holding a bag / a baby
  --------------------------------------------------------------
   The curb-cut effect: a ramp cut for wheelchairs serves strollers,
   carts, luggage, and delivery bikes. Access built for the edge
   improves the middle -- captions used by the hearing in noisy rooms.
```

This is why the honest framing is not charity but **coverage**: the "edge case" is a
duration of a state most people pass through, and building for it widens the usable
population. *(The clinical/medical dimension of any specific condition is
`medicine/`/`disease/`; this guide uses the model, not the diagnosis.)*

---

## 2. The Five Axes — Formalized

Making the Big-Picture axes precise, because reviews and contracts turn on them. They
are **independent dimensions**, not layers of a stack — read each on its own scale:

- **Participatory / inclusive design process.** *Who shaped it, and with how much
  authority?* Disabled people involved across discovery, design, and evaluation as
  co-designers and decision-makers, not late-stage consultees (Section 7). British
  Standard **BS 7000-6** and Microsoft's Inclusive Design toolkit codify the stance
  (*"solve for one, extend to many"*); ability-based design (Wobbrock et al. 2011)
  inverts the framing to design *to the abilities a person has*.
- **Technical conformance.** *Does it meet the standard?* WCAG and related criteria,
  established by audit. Testable and standard-referenced — but conformance is a property
  of the artifact against a checklist, **not** a claim that anyone can actually use it.
- **Task accessibility.** *Can a person using assistive technology X perceive, operate,
  and understand — and complete — task T?* A capability *outcome*, and **not binary**: it
  is graded and contextual (which person, which task, which AT, which setting), measured
  by AT walkthrough and task completion, not inferred from a conformance pass.
- **Usability outcomes.** A graded measure (from `05`): effectiveness × efficiency ×
  satisfaction, *for disabled users as a first-class user group*, not an afterthought.
- **Inclusion / equity.** *Does the design reduce exclusion across the whole population*,
  including the non-disability dimensions of Section 8 (language, literacy, bandwidth,
  age, situation)?

**Universal design (the principles).** Ronald Mace / Center for Universal Design
(NC State, **1997**) — **seven principles**: equitable use; flexibility in use; simple
and intuitive; perceptible information; tolerance for error; low physical effort; size
and space for approach and use. These are *design principles*, dated and general, **not
a conformance standard** — do not cite them as pass/fail criteria; they inform the
process axis, they do not measure the conformance one.

The distinction that keeps a team honest: **you can conform (axis 2) without being
task-accessible or usable (axes 3–4), and be usable-for-most without being inclusive
(axis 5).** Section 6 is the whole argument that conformance ≠ the outcome axes; keep the
axes separate and score them separately.

---

## 3. How Assistive Technology Interacts — The Accessibility Tree

The mechanical heart of interactive accessibility. Assistive technologies (AT) do not
read your pixels; they consume a **semantic model** of your UI called the
**accessibility tree**, exposed through a platform **accessibility API**.

```
  THE ACCESSIBILITY PIPELINE (how AT reaches the user)
  --------------------------------------------------------------
   UI element tree        semantic contract          platform bridge
   (DOM / native views)   name / role / value /       OS a11y API
        |                 state / relationships       (UIA, AX, AT-SPI)
        |  compute              |                          |
        v                       v                          v
   [ ACCESSIBILITY TREE ] --> [ PLATFORM A11Y API ] --> [ ASSISTIVE TECH ] --> user
                                                         screen reader,
                                                         magnifier, switch,
                                                         voice control, braille
  --------------------------------------------------------------
   If the semantic contract is wrong, EVERY layer downstream is wrong.
   A <div> styled to look like a button has role=none: AT sees nothing
   to announce, nothing to focus, nothing to "press".
```

An interactive element needs an accessible **name** and a correct **role**; **value** and
**state** are exposed **only when they apply**; and **descriptions** and **relationships**
complete the semantic contract when present. Name and role are the non-negotiable
interactive semantics — value/state on a control that has neither is noise:

| Property | When | Question it answers | Failure mode |
|---|---|---|---|
| **Name** | required (interactive) | what is this? ("Submit", "Search") | unlabeled icon button → announced as "button" |
| **Role** | required (interactive) | what kind of control? (button, link, checkbox) | `<div onclick>` → no role → invisible to AT |
| **Value** | when applicable | current content/setting (slider, textbox) | custom slider with no exposed value |
| **State** | when applicable | checked? expanded? disabled? selected? | menu that looks open but reports collapsed |
| **Description** | when present | extra help beyond the name (`aria-describedby`) | error/help text not tied to its field |
| **Relationships** | when present | grouping & associations (label↔field, header↔cell, owns) | radio group with no group; header not tied to cell |

- **Semantics before ARIA.** Native semantic elements (`<button>`, `<a href>`,
  `<input>`, `<nav>`) carry the correct **role and state behavior**, keyboard operability,
  and value where it applies *for free* — but the accessible **name** must still be
  supplied where the element does not derive one from its content (an icon-only
  `<button>`, an `<input>` without an associated `<label>`). **WAI-ARIA** (Accessible Rich
  Internet Applications; W3C
  Recommendation, ARIA 1.2, 2023) *supplements* semantics for custom widgets — but the
  **first rule of ARIA is "don't use ARIA if a native element will do,"** and **"no ARIA
  is better than bad ARIA":** incorrect ARIA actively lies to the accessibility tree and
  is worse than none. ARIA changes the *semantics*, never the *behavior*; you still must
  wire the keyboard and focus yourself.
- **Three distinct mechanisms, not one — "it's all the keyboard" is wrong.** Keep the
  operating mechanisms separate, because an app can satisfy one and fail another:
  - **Keyboard operability** — a **logical focus order**, a **visible focus indicator**,
    and no **keyboard traps**. This carries keyboard users *and* the ATs that emulate a
    keyboard (many switch setups, some voice commands) — but it is not what *every* AT
    uses.
  - **Accessibility API / semantic tree** — the name/role/value/state (+ description/
    relationships) that screen readers, voice control, and switch scanners *read* to
    perceive and target elements. Voice control ("click Submit") resolves by **name**; a
    touch screen reader announces by **role and name** — neither is a keypress.
  - **Touch / pointer / voice / switch input** — each has its own operable requirements:
    touch-screen-reader **gestures** (swipe / double-tap on iOS/Android), **pointer**
    gestures that must have single-pointer alternatives (no path- or multipoint-only
    action), **voice** targeting by visible label, and **switch** scanning. A
    keyboard-perfect app can still be unusable by touch AT or by voice if names/roles or
    touch targets are wrong.
  Focus management (moving focus to opened dialogs, restoring it on close, exposing focus
  to the a11y tree) remains among the highest-leverage engineering work — but it lives on
  the *keyboard-operability* mechanism and does not, by itself, deliver the semantic tree
  or the touch/pointer/voice/switch mechanisms.

**Bridge (software).** The accessibility tree is a **semantic API / typed AST over your
rendered UI**, and a screen reader is a **headless client** consuming it. `<div>`-soup is
**stringly-typed UI** — it renders but carries no contract; ARIA is **type annotations**
you add to a custom widget to restore the contract, with the same danger as a wrong type
annotation: a lie the whole toolchain now trusts. Building an inaccessible custom control
and bolting ARIA on is re-implementing `<button>` badly; using the native element is
using the standard library.

---

## 4. Access by Channel — Barrier → Mechanism → Design Response

Accessibility is concrete per sensory/motor/cognitive channel. For each: the barrier, the
AT that mediates, and the interface's responsibility.

**Visual.**
- *Blind* → screen reader (JAWS, NVDA, Narrator, VoiceOver, TalkBack) and/or refreshable
  **braille** display consuming the a11y tree (Section 3). Responsibility: complete name
  and role (with value/state where applicable) plus descriptions and relationships; text
  alternatives for images; structure (headings, landmarks, lists) so
  navigation-by-structure works.
- *Low vision* → magnification, high contrast, and **reflow**. Responsibility: don't
  break on 200–400% zoom; support reflow to a single column (WCAG 1.4.10); meet the
  contrast criteria — **WCAG 1.4.3** (Contrast (Minimum), AA) governs **text**: **4.5:1**
  for normal text, **3:1** for large text; **WCAG 1.4.11** (Non-text Contrast, AA)
  governs **non-text**: **3:1** for UI components and graphical objects — never hard-code
  tiny fonts.
- *Color vision deficiency* → responsibility: **never encode meaning by color alone**
  (WCAG 1.4.1) — pair color with text, icon, or pattern (the red/green status dot needs a
  label).

**Auditory.**
- *Deaf / hard of hearing* → responsibility: **captions** for pre-recorded and live audio
  (WCAG 1.2.2/1.2.4), **transcripts**, and — for some users whose first language is a
  signed language — sign-language interpretation. Never make sound the *only* signal
  (pair an alert beep with a visual cue).

**Motor / dexterity.**
- *Limited or no fine motor control* → keyboard-only, **switch access** (scanning),
  **voice control** (speak commands/labels), eye-gaze, alternative keyboards.
  Responsibility: full keyboard operability (Section 3); adequate **target size** (WCAG
  2.2 **2.5.8** Target Size (Minimum), AA: **24×24 CSS px**) — but this is **not** a
  blanket rule: SC 2.5.8 carries defined **exceptions** (adequate **spacing** around a
  smaller target, an **equivalent** control elsewhere on the page, **inline** targets
  within a sentence, sizing left to the **user agent**, or where a specific presentation
  is **essential**); no motion-only or drag-only operations (WCAG 2.2 Dragging
  Movements); generous timing and the ability to extend or disable time limits (WCAG
  2.2.1).

**Cognitive / learning.**
- *Attention, memory, language, executive-function differences* → the least
  standard-covered, most under-served channel (the W3C **COGA** task force addresses it).
  Responsibility: **plain language**; consistency and predictability (WCAG 2.2 Consistent
  Help); reduced memory load (recognition over recall); error tolerance and clear
  recovery; reduced distraction; not requiring a cognitive test to log in (WCAG 2.2
  Accessible Authentication). *Why* a given design taxes working memory is
  `cognitive-science/`'s to explain; this guide owns the design response.

```
  ONE BARRIER, MANY ACCOMMODATIONS -- e.g. "status is shown only in red"
  --------------------------------------------------------------
   channel        who it blocks          the same fix that helps everyone
   ------------   -------------------     --------------------------------
   visual/color   color-blind users      add a text label + icon to the color
   visual/blind   screen-reader users    expose status as text in the a11y tree
   cognitive      low-literacy/stressed   use a plain, unambiguous status word
  --------------------------------------------------------------
   One inclusive fix (label + icon + accessible text) closes three gaps.
```

---

## 5. WCAG 2.2 — What the Standard Is, Dated and Bounded

The **Web Content Accessibility Guidelines** are the dominant technical standard.
Versions and dates matter and must be cited:

- **WCAG 2.0** — W3C Recommendation, **11 December 2008**.
- **WCAG 2.1** — **5 June 2018** (added mobile, low-vision, cognitive criteria).
- **WCAG 2.2** — **5 October 2023** (current 2.x Recommendation; added 9 success
  criteria, e.g., Focus Not Obscured, Dragging Movements, Target Size Minimum,
  Accessible Authentication, Consistent Help; **removed 4.1.1 Parsing** as obsolete).
- **WCAG 3.0** — an **early Working Draft**, *not* a Recommendation, with a *different*
  (scored, not pass/fail) conformance model. Do not cite 3.0 as a current requirement.

Structure — the **POUR** principles, then guidelines, then testable success criteria at
three levels:

```
  WCAG STRUCTURE (2.x)
  --------------------------------------------------------------
   4 PRINCIPLES (POUR)
     Perceivable   -- can they sense the content? (alt text, contrast, captions)
     Operable      -- can they operate it? (keyboard, timing, target size)
     Understandable-- can they understand it? (readable, predictable, input help)
     Robust        -- does it work with AT now and later? (name/role/value)
        |
        v  13 GUIDELINES
        v  success criteria, each tagged a LEVEL:
     A    = minimum / essential
     AA   = the common target and typical legal reference threshold
     AAA  = enhanced; W3C says do NOT require AAA across a whole site as policy
  --------------------------------------------------------------
   Conformance is per level and (mostly) all-or-nothing: to claim AA you meet
   ALL A and AA criteria for full pages/flows, incl. "accessibility supported"
   (works with the AT your users actually have).
```

**Bounding the standard — read these honestly:**

- WCAG is a **web-content** standard (native mobile/desktop map to it via EN 301 549 and
  platform guidance, imperfectly). It is a **necessary scaffold**, not a sufficient
  definition of an accessible experience.
- Coverage is **uneven across disabilities**: strong on perceivable/operable for
  sensory/motor access, **comparatively weak on cognitive** accessibility (an active gap
  the COGA work addresses).
- Success criteria are **testable minimums**, which is their strength and their trap: a
  page can satisfy every criterion mechanically and still be hostile to use (Section 6).
- **AAA is not "better compliance"**; W3C explicitly advises against blanket AAA
  requirements because some AAA criteria are impossible for some content.

*(Whether any standard is legally required, for whom, and where — Section 508, ADA, EN
301 549, the European Accessibility Act — is `law/`'s domain. Section 9 names them as
dated landscape only.)*

---

## 6. Conformance vs Actual Usability — The Central Honesty

This is the accessibility twin of `05`'s "SUS is not usability," and the single most
important professional judgment in the guide: **passing WCAG is a floor and a proxy, not
a measure of whether disabled people can actually use the thing.**

```
  CONFORMANCE  is NOT  USABILITY
  --------------------------------------------------------------
   AUTOMATED CHECK passes ...... only a MINORITY of WCAG issues are
                                 machine-detectable at all (see the
                                 recall note below) -> "0 errors" means
                                 "no MACHINE-FOUND errors", not "accessible"
   MANUAL AUDIT passes (AA) .... every criterion met on paper, yet the
                                 screen-reader task can still take 10x longer,
                                 or dead-end, or be technically-labelled noise
   ACTUAL USABILITY ........... a disabled user completes the real task
                                 effectively, efficiently, without agony
  --------------------------------------------------------------
   Each layer is necessary and none is sufficient. The bottom layer is
   the strongest evidence -- but still BOUNDED (Section 7), not ground truth.
```

Concretely: alt text can be present *and* useless ("image123.png"); every control can be
labeled *and* the focus order can scramble the flow; an ARIA live region can be *valid*
and announce so much that the user turns it off. The empirical backdrop: automated
analyses like the annual **WebAIM Million** report have found detectable WCAG failures on
the large majority of top home pages (WebAIM Million 2024: ~96%), and automated tools
reliably catch only a **minority** of real barriers — so "our scanner is green" is a
statement about the scanner, not the experience.

**A note on the "recall" figure.** *Recall* here means the share of *genuine*
accessibility barriers that an automated tool detects. It is a **minority** — automated
tooling reliably catches only a fraction of real barriers, well below 100% — but no single
precise figure is defensible: recall depends heavily on the tool, its ruleset, the page,
and how "a barrier" is counted, and the available tool-comparison and audit analyses do
not share a common denominator that would pin one number. Absent a **named primary
comparison and its denominator**, state it qualitatively — **a minority / limited
recall** — not as a measured rate; the load-bearing claim is only that automated recall is
well below 100%.

The correction is method, from `05`, extended: **conformance testing (automated + manual
expert audit) tells you about the floor; usability testing with disabled participants
gives you bounded evidence about actual use** — evidence for the specific people, tasks,
AT, and contexts you sampled, **never ground truth.** Treat them as different instruments,
report both, and state the bounds of the sample.

**Bridge (software).** This is exactly **green CI vs a good product**. Your accessibility
linter is a **static analyzer with limited recall**: it flags provable violations (missing
alt, low contrast) and is blind to semantic wrongness (unhelpful alt, illogical order),
just as a linter can't tell you your correct-compiling function returns the wrong answer.
You still run integration tests with real users — here, users with disabilities.

---

## 7. Participatory Practice & Accessible Research — With, and By, Disabled People

The discipline here is **"nothing about us without us":** disabled people are not just
*subjects* at the end of the process but **participants and decision-makers throughout
it** — and even the best evaluation yields **bounded evidence**, never ground truth.
Three things, and mature teams do all three.

**(a) Disabled-led participatory / co-design across the lifecycle.** Involve disabled
people (and disabled designers and engineers on the team) at every stage, not as a final
audit:

- **Discovery** — lived experience defines the real barriers and priorities *before*
  requirements are set; the problem framing itself is co-owned.
- **Design** — co-design sessions where disabled participants shape solutions (the
  process axis of §2), not merely react to finished mockups.
- **Evaluation** — testing *with* disabled users (part (b)), closing the loop.
- **Community authority.** On decisions that affect a disabled community, that community
  holds real authority — a voice that can change or stop the design, not a comment box.
  Consulting disabled people and then overriding them is participation-theatre.
- **Compensation.** Pay disabled participants and co-designers fairly for their expertise
  and time; lived-experience and AT expertise are skilled labor, not a favor to be
  extracted. Unpaid "advocacy" and emotional labor are an equity failure, not a saving.

**(b) Evaluating the product's accessibility.** A layered method:

```
  ACCESSIBILITY EVALUATION STACK (cheap/shallow -> expensive/deep)
  --------------------------------------------------------------
   1. AUTOMATED scan .......... fast, CI-friendly, low recall (§6), false sense of done
   2. MANUAL EXPERT AUDIT ..... criterion-by-criterion vs WCAG; keyboard + AT walkthrough
   3. AT WALKTHROUGH .......... operate the real flow with NVDA/VoiceOver/switch/voice
   4. USABILITY TEST w/ ....... disabled participants, real tasks = strong but BOUNDED
      DISABLED USERS          evidence (extends guide 05's methods), not ground truth
  --------------------------------------------------------------
   Stop-short at 1-2 and you ship "conformant but unusable" (Section 6).
```

**(c) Making the research itself accessible** — because a study that excludes disabled
participants (inaccessible consent forms, mouse-only tasks, uncaptioned sessions) cannot
evaluate accessibility. Practical discipline, all from `05`/`06` extended:

- **Recruit for AT diversity, and don't treat disabled users as a monolith.** Screen-
  reader users are not interchangeable with low-vision or cognitive-disability users;
  even among screen-reader users, JAWS/NVDA/VoiceOver expertise differs. Over-recruit per
  segment (the per-segment discovery-sample logic from `05` §6 applies here too).
- **Respect AT expertise.** Test with the participant's *own* AT and configuration where
  possible; a lab screen reader at default verbosity is not their setup.
- **Welfare, consent, compensation, privacy.** Accessible consent materials; fair
  compensation (part (a)); no fatigue-inducing marathon sessions; careful handling of
  disability data (sensitive). These are *research-ethics principles this guide flags* —
  not an IRB substitute and not legal advice.
- **Remote vs in-person trade-offs.** Remote widens reach but adds setup friction and
  selection bias (who has the device/bandwidth/AT and the literacy to join).

**Bounded evidence, not ground truth.** However well you do all of this, a usability test
is evidence about **the specific people, tasks, AT versions, and contexts you sampled** —
not a universal verdict. A different disabled user, a newer AT build, a different task or
a slower network can surface what your sample could not. Report *who* and *what* you
covered, and treat the result as strong-but-bounded evidence, never proof that the system
is "accessible" for everyone.

---

## 8. Beyond Disability — Inclusive Dimensions That Are Not Optional

Inclusive design's "reduce exclusion" mandate extends past disability, and for a global
system these dimensions are *central*, not caveats:

- **Localization & internationalization.** Language, script direction (RTL), text
  expansion, locale formats, culturally variable icons. (Script/type *mechanism* is
  `linguistics/`/`typography/`; the *interaction* responsibility — does the UI reflow for
  RTL, does the ASR accept the accent — is here.)
- **Literacy & numeracy.** Plain language and clear numbers serve low-literacy users,
  non-native speakers, stressed users, *and* cognitive-accessibility users at once — the
  curb-cut effect again.
- **Bandwidth & device.** Low-end devices, metered/intermittent connectivity, small
  screens, feature phones. A 6 MB "accessible" page is inaccessible to a user on a slow
  metered connection. Progressive enhancement and graceful degradation are *inclusion*
  techniques, not just performance ones.
- **Age & situational constraints.** Older adults (often multiple mild, co-occurring
  impairments) and situational limits (sunlight, noise, one-handed, distracted) are the
  large populations that access work quietly serves.

**Bridge (software).** Situational disability *is* **degraded-mode operation**: bright sun
= temporary low vision; a loud room = temporary deafness; carrying a bag = temporary
one-handed. You already design services for degraded networks and partial failures;
inclusive design is the same fault-tolerance stance pointed at the human side of the
system.

---

## 9. Procurement and Governance — Accessibility as an Organizational Capability

Accessibility fails as heroics and succeeds as a *system*. The governance mechanisms
(described as mechanisms, **not** as legal obligations):

- **Shift left.** The cheapest accessibility is designed-in: an **accessible design
  system / component library** makes the accessible path the default path, so product
  teams inherit correct semantics, focus, and contrast. This is the single highest-
  leverage governance move — fix `<button>` once, fix it everywhere.
- **Automated gates in CI**, understood for what they are (Section 6): a low-recall
  regression guard, not a sign-off.
- **Conformance artifacts.** A **VPAT** (Voluntary Product Accessibility Template),
  produced as an **ACR** (Accessibility Conformance Report), is the industry document a
  buyer requests to see a product's claimed conformance. Named here as an *artifact and a
  process*; its truthfulness depends on the audit behind it, and it is not a usability
  guarantee.
- **Procurement.** Organizations bake accessibility requirements into purchasing so they
  don't buy inaccessible tools. The *mechanism* is a requirement in a contract; the
  *legal force* of any such requirement is `law/`.
- **Roles, ownership, maturity.** A named owner, training, and a maturity model move an
  org from reactive-remediation to designed-in accessibility.

**Overlays are not governance.** Third-party "accessibility overlay" widgets that promise
one-line compliance are widely rejected by the accessibility community and disabled users
(see the *Overlay Fact Sheet*, overlayfactsheet.com, first published **2021**) — they can
*degrade* AT interaction and do not deliver actual usability. The absence of a shortcut is
itself a governance fact.

---

## A Worked Inclusive-Design Case (illustrative, fictional)

*Fictional throughout, to show the three-way boundary and the conformance-vs-usability
gap in motion. No real jurisdiction, product, or law is described, and nothing here is
legal advice.*

**System.** *Rivergate Benefits*, a fictional government portal where residents apply for
an income-support benefit. It is used by a population skewed toward older adults, people
with disabilities, low-literacy and multilingual users, and people on low-end phones over
metered data — i.e., the exact population access work serves.

**Boundary in action (the three-way split).**
- *HCI (this guide)* owns: designing the application flow so it is perceivable/operable/
  understandable, and *evaluating* that with disabled users.
- *human-factors/* would own (deferred): if caseworkers use a high-throughput internal
  triage console under time pressure, their **workload and error rates** under load — an
  operator-performance question, not an interface-reach question.
- *law/* owns (deferred): whether the portal is legally *required* to meet a given
  standard, and any liability. This guide does **not** rule on that.

**Design.** Built on an accessible design system: native semantics, keyboard-first, 4.5:1
contrast, plain-language labels, no color-only status, captions on the help videos,
generous timeouts, target sizes ≥ 24×24 px, RTL support for one official language, and a
low-bandwidth mode that drops to a lightweight page.

**Evaluation — and the conformance-vs-usability gap.** An automated scan is green, and a
manual expert audit finds the flow meets **WCAG 2.2 AA** on paper. But a **usability test
with disabled participants** (Section 7) surfaces what conformance missed:
- A screen-reader user *can* complete the income step (it's labeled and reaches AA) but it
  takes ~4× longer because a valid-but-noisy ARIA live region re-announces the whole
  summary on every keystroke. **Conformant, not usable.**
- A low-literacy user abandons at a legally-worded eligibility question that is
  *technically* "understandable" per the criteria but not in practice.
- A user on a metered connection times out on the document-upload step because the
  "accessible" page still ships a heavy script bundle.

**Fixes.** Throttle/summarize the live region; rewrite the eligibility question in tested
plain language; make upload work on the low-bandwidth path. None of these were WCAG
*failures* — they are the gap between conformance and the experience, caught only because
the team tested with the actual excluded users.

**Reading.** Rivergate reached **conformance** (AA) before it reached **task accessibility
and usability** (disabled users completing the real task without agony), and it aimed for
**inclusion** (the same plain-language and low-bandwidth fixes that helped disabled users
helped everyone). The team scores those axes **separately** (§2), defers the
legal-requirement question to counsel, and defers any caseworker-console workload question
to a future human-factors review — the three-way boundary held.

**A non-Western, low-bandwidth branch (same benefit, a different deployment).** Now deploy
the same benefit in a low-income, largely rural region: most residents reach it on
**shared or low-end Android phones over metered 2G/3G**, in **languages with limited
digital-type and complex-script or RTL needs**, with **low text literacy in the official
language**, and where **commercial screen readers are unaffordable** — the common AT is
free/bundled (TalkBack, community text-to-speech) or none. The five axes do not change;
the design responses do, and this is a *branch to work*, not a caveat to note:

- **AT access is not assumable.** Do not design for JAWS-on-desktop; the realistic AT is
  TalkBack on a budget phone — or a feature-phone **USSD/IVR** channel with no screen
  reader at all. Audio-first flows and an **SMS/USSD fallback** are accessibility
  features here, not extras.
- **Bandwidth is an access barrier, not a performance nicety.** A "conformant" page that
  ships megabytes fails a metered 2G user as surely as a missing label fails a
  screen-reader user. Ship a genuinely light path, offline-tolerant forms, and resumable
  uploads.
- **Literacy and language.** Plain language is load-bearing, not polish; pair every
  critical step with **icons, audio, and the user's own language** (not only the official
  one), and test comprehension *with* low-literacy users rather than trusting a
  readability score.
- **Participatory, locally.** Co-design and testing must be **with residents of that
  region on their actual devices and AT** (Section 7); a capital-city lab on office
  Wi-Fi measures a different system. Community authority and fair compensation apply here
  too.

The reading is the same shape as Rivergate but for a population the WEIRD default silently
excludes: the same five axes, **re-evidenced** for this context — not a paragraph of
apology appended to a Western design.

**On the legal deferral — an honesty note.** This guide routes every "are we legally
required to?" question to `law/`. As of this prototype, the `law/` module does **not yet
deeply cover digital-accessibility statutes** (it treats the ADA only in the *employment*
context and does not yet address Section 508, the EAA, EN 301 549, or web/app
accessibility duty). So the deferral target is currently incomplete: the legal-obligation
question is **deferred, not answered** — this guide still names the standards landscape as
dated context only and routes duty and compliance to `law/` and qualified counsel, which
is exactly why it must not be read as legal advice.

---

## Reader Tasks (answerable from this guide)

1. **Diagnose a barrier across the stack.** Given "order status is shown only as a red
   dot," name the channel(s) blocked (color-blind and screen-reader and low-literacy
   users), the WCAG principle at stake (Perceivable; 1.4.1 use of color), and one
   inclusive fix that closes all three (label + icon + accessible text). (§4, §5.)
2. **Explain conformant-but-unusable.** Given "we pass WCAG 2.2 AA and the scanner is
   green," explain why a screen-reader user can still be unable to use the flow, what
   evaluation would catch it (AT walkthrough + usability test with disabled users), and
   why a "green scan" catches only a minority of real barriers (its *recall*; §6). (§6, §7.)
3. **Place responsibility on the right owner.** Given three concerns — "the button has no
   accessible name," "the ER-console operator is overloaded at peak," "are we legally
   required to conform?" — assign them to HCI, human-factors, and law respectively, and
   justify from the three-way boundary. (Header, §9, worked case.)
4. **Design an accessible study.** Sketch a usability test that evaluates a checkout for
   accessibility: recruit for AT diversity (don't treat disabled users as one segment),
   test with participants' own AT, provide accessible consent, and size discovery per
   segment. (§7.)
5. **Scope inclusion for a global rollout.** For a benefits portal used on low-end phones
   in several languages, list the inclusive dimensions beyond disability that must be
   addressed (localization/RTL, literacy, bandwidth/device, age/situational) and one
   design response to each. (§8, worked case.)

---

## Decision Cheat Sheet

| Situation | What to do | Why (this guide) |
|---|---|---|
| "Is it accessible?" | ask **for whom, doing what, with which AT** | accessibility is a per-user, per-task capability, not a global flag (Big Picture, §2) |
| Building a custom control | use the **native element** first; add ARIA only to fill gaps | no ARIA is better than bad ARIA; native semantics give **role/state behavior + keyboard** for free, but you still supply the accessible **name** where needed (icon buttons, inputs), **value/state only when applicable**, and **relationships/descriptions** where required (§3) |
| Any interactive element | verify **name + role** (value/state when applicable; + description/relationships) and keyboard operability | AT reads the a11y tree; keyboard, touch/pointer/voice/switch are distinct mechanisms (§3) |
| Status shown by color | add **text + icon**; never color-alone | WCAG 1.4.1; serves color-blind + screen-reader + low-literacy (§4) |
| Automated scan is green | treat as **low recall** (a minority of barriers; §6); run manual audit + AT walkthrough + user test | conformance is a scaffold, not usability (§6, §7) |
| Claiming "WCAG AA" | it means **all A+AA criteria on full flows**, dated to WCAG 2.2 (2023) | conformance is per-level, mostly all-or-nothing (§5) |
| "AAA to be safe" | **don't** blanket-require AAA | W3C advises against it; some AAA is impossible for some content (§5) |
| Testing accessibility | test **with disabled users on their own AT** | lived-usability evidence beats the checklist — but is bounded, not ground truth (§7) |
| A vendor sends a VPAT/ACR | read it as a **claim**, verify the audit, still test usability | an artifact ≠ a usable product (§9) |
| Someone pitches an a11y "overlay" | **decline**; invest in the design system | overlays don't deliver usability and can harm AT (§9) |
| "Are we legally required to?" | **route to `law/`** | this guide names standards, never adjudicates obligation (header, §5, §9) |
| Operator overloaded under time pressure | **route to `human-factors/`** | operator performance/safety is HF, not interface reach (header) |

---

## Common Confusion Points

**"Accessible means WCAG-compliant."** No. WCAG conformance is a testable *floor* and a
proxy; a fully AA-conformant page can be slow, confusing, or dead-ended for a real AT user
(§6). Conformance and usability are different instruments — report both.

**"We tested with a screen reader once, so it's accessible."** No. One AT, at default
settings, by a sighted developer, is not evaluation. Accessibility needs multiple AT types,
users' own configurations, and — for bounded evidence of real use — usability testing
*with disabled people* (§7).

**"The automated checker passed, so we're done."** No. Automated tools catch only a
minority of barriers (their *recall* is well below 100% — no single precise fraction is
defensible without a named primary comparison and denominator; §6) and are blind to
*semantic* wrongness — unhelpful alt text, illogical focus order, noisy live regions all
pass the scanner (§6).

**"ARIA makes things accessible."** Often the opposite. ARIA changes semantics, not
behavior, and *wrong* ARIA lies to the accessibility tree — "no ARIA is better than bad
ARIA." Prefer native elements; reserve ARIA for genuine custom widgets and wire the
keyboard yourself (§3).

**"Accessibility is only for permanent disability, a small minority."** No. The permanent/
temporary/situational spectrum means most people are in a mismatch state sometimes (a
broken arm, bright sun, a noisy train); WHO estimates ~16% (~1.3 billion, 2022) experience
significant disability, and situational coverage is far larger (§1, §8).

**"Inclusive design is just accessibility with a nicer name."** No — and neither is a
layer of the other. They are independent axes (§ Big Picture, §2): the *process* axis
(did disabled people co-design it?), the *conformance* axis (does it meet WCAG?), *task
accessibility* (can they do the task with their AT?), *usability outcomes* (is it good
for them?), and *inclusion/equity* (who is still excluded?). You can conform without
being task-accessible or usable, and be usable-for-most without being inclusive (§1, §2).

**"An accessibility overlay/plugin will make our site compliant."** No. Overlays are widely
rejected by disabled users and can degrade AT; there is no one-line fix. Durable
accessibility comes from an accessible design system and testing with users (§9).

**"Accessibility is a cost for a few; it slows everyone else down."** No — the curb-cut
effect: captions serve people in noisy rooms, plain language serves stressed and non-native
readers, keyboard operability serves power users, low-bandwidth modes serve everyone on bad
networks. Access built for the edge improves the middle (§1, §8).

---

## Global, WEIRD, and Resource Caveats

- **The standards and AT canon is English/Latin-script- and resource-rich-first.** WCAG,
  its testing tools, and the major screen readers were built primarily around English and
  Latin scripts; support for many languages, complex scripts, and signed languages is
  thinner, and high-quality AT (braille displays, premium screen readers, reliable ASR for
  under-resourced languages) is unevenly available and often expensive.
- **Prevalence and models are not universal.** The ~16% / ~1.3 billion figure (WHO 2022) is
  a global estimate that varies by region, definition, and measurement; the social and
  interaction models are themselves products of particular (largely Western) disability-
  rights movements, and other cultures frame disability, family, and independence
  differently. Attribute and date; do not universalize one region's model or numbers.
- **Bandwidth, device, and literacy are first-order globally.** For much of the world the
  binding constraint is a low-end phone on metered data with mixed literacy and a
  non-dominant language — so a heavy "WCAG-conformant" page can be *less* accessible in
  practice than a lightweight plain-language one. Inclusion that stops at WCAG AA on a fast
  laptop has not met a global user base.
- **Legal frameworks are jurisdictional and out of scope here.** Section 508, the ADA, EN
  301 549, and the European Accessibility Act (application from 2025) differ by place, apply
  to different actors, and change over time; which (if any) binds a given product is a
  `law/` question this guide deliberately does not answer.
