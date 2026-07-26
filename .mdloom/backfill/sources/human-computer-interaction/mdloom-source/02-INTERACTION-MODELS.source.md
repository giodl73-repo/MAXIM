---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "02-INTERACTION-MODELS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-computer-interaction:interaction-models
kind: guide
module: human-computer-interaction
section: human-computer-interaction
title: Interaction Models - Diagnostic Instruments for Interactive Computing
status: source-custody
source_custody: partial
current_path: human-computer-interaction/02-INTERACTION-MODELS.md
canonical_path: human-computer-interaction/02-INTERACTION-MODELS.md
backsource_ids: [mdloom-backfill:human-computer-interaction:02-interaction-models]
concepts: [interaction-models, gulfs-of-execution-evaluation, direct-manipulation, modes, instrumental-interaction, distributed-cognition, activity-theory]
root_concepts: [interaction-models]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Interaction Models — Diagnostic Instruments for Interactive Computing

**This guide owns** the *models of interaction* used to reason about interactive computing: the
seven-stage action cycle and the two gulfs **applied to software**, direct manipulation, modes
and mode errors, instrumental interaction, and distributed cognition / activity theory as
*applied* analytic lenses. It owns them **as diagnostic instruments** — a model earns its keep
only by predicting *where* an interaction will break. **It builds on** `01` (where these ideas
came from) and grounds `04`/`05` (the loop that designs against and tests these predictions).
**It explicitly defers**: the *origin and physical-product framing* of Norman's action model,
affordances, and interaction design to `industrial-design/06-INTERACTION-DESIGN` (this guide
**applies** the model to computing; it does not re-teach it); the *cognitive mechanism* behind a
breakdown — why attention lapses, why working memory overflows, why a signal goes unnoticed — to
`cognitive-science/` (esp. `09-APPLIED-BRIDGE`); the *psychophysical laws* (Fitts, Hick) that
`03` applies; and *operator workload/error in safety-critical work* to `human-factors/`.

> **This module is an educational reference. Interaction models here are analytic tools for
> designing and diagnosing interfaces — not manipulation techniques, not legal or safety rulings.
> A model that predicts where users fail can be misused to engineer friction against a user's
> interest; that is a dark pattern and is out of scope (`11`). Named laws/models are attributed
> and dated.**

*Per-guide banner: a model is admitted here only if it makes a **falsifiable prediction** that
**localizes a breakdown**, and the **empirical test must match the model's unit of analysis.**
Individual-level models (Norman's stages/gulfs, modes, instrumental interaction, mental models;
and GOMS as applied in `03`/`05`) localize a breakdown to a **specific step** and a **specific
gulf** (execution vs evaluation) that a think-aloud (`05` §4) could confirm or leave unresolved.
**System-level lenses** (distributed cognition, activity theory) instead predict a **findable
coordination/system breakdown** — confirmed by a **field study** (`06`) and measured with `09`'s
group outcomes — and need **not** map to a single gulf. Either way a model that cannot fail a
prediction is decoration, not an instrument; and matching the wrong evidence to the model (a
think-aloud for a system-level claim, or a field study for a single-user gulf) is the same
error.*

---

## The Big Picture: Interaction Is a Loop Across Two Gulfs

Every interaction is a cycle: the person forms a goal, acts on the system, and interprets what
happened. Don Norman's **seven stages of action** (developed for everyday things in
`industrial-design/06`; **applied here to computing**) split that cycle into an *execution* side
(goal → intention → action sequence → execution) and an *evaluation* side (perceive → interpret →
evaluate against the goal). Between the person and the system sit **two gulfs**: the **Gulf of
Execution** (how do I *do* this?) and the **Gulf of Evaluation** (what just *happened*?).

```
  THE ACTION CYCLE AND THE TWO GULFS  (Norman; applied to software)
  ==================================================================
                          GOAL ("submit the expense")
                            |
      EXECUTION SIDE        v                 EVALUATION SIDE
      -----------------------------           -----------------------------
      intention to act                        evaluate vs the goal
      sequence of actions                     interpret the perception
      execute the actions                     perceive system state
             |                                        ^
             v                                        |
        [ GULF OF EXECUTION ]  ---->  SYSTEM  ---->  [ GULF OF EVALUATION ]
        "can I express what I         (state    "can I tell what state
         want in the actions          changes)   it is in, and whether
         the system offers?"                     I got closer to the goal?"
  ==================================================================
   A USABILITY PROBLEM LIVES IN A GULF, AT A STAGE. Naming which gulf and
   which stage IS the diagnosis -- and it is what a model must predict.
```

**The move that makes this a discipline and not a vocabulary:** a model is only useful if it
**predicts a breakdown you can go look for.** "This control has poor affordance" is decoration
until it becomes: *"at the action-selection stage, a first-time user will not see that the row is
tappable (Gulf of Execution), so they will stall before opening the detail — a think-aloud on
first-use tasks will show the stall or leave it unresolved."* Every model below is presented that
way: what it predicts, at which stage/gulf, and how you would find out it was wrong.

**Bridge (software).** The two gulfs map onto an API you didn't design: the **Gulf of Execution**
is **discoverability and ergonomics of the interface** — can the caller express intent with the
operations exposed? The **Gulf of Evaluation** is **observability** — can the caller tell, from
what comes back, what state the system is in and whether the call worked? A confusing UI is an API
with poor discoverability and poor observability; direct manipulation narrows both.

---

## 1. Norman's Stages and Gulfs, Applied — The Base Instrument

Applied to computing, the seven stages give the field its **fault-localization grid**. You do not
ask "is this usable?"; you ask *at which stage* the user's cycle breaks and *in which gulf*.

| Stage | The user's question | Gulf | A computing failure at this stage |
|-------|---------------------|------|-----------------------------------|
| Goal | what do I want? | — | user's goal doesn't match any task the system supports |
| Intention | what should I do? | execution | no visible path to the goal (feature exists but is unfindable) |
| Action sequence | in what order? | execution | correct actions exist but the required order is non-obvious |
| Execution | do it | execution | target too small / gesture unsupported (a `03` modality issue) |
| Perceive | what changed? | evaluation | no feedback: the state changed but nothing signaled it |
| Interpret | what does that mean? | evaluation | feedback present but ambiguous ("Done" — done *what*?) |
| Evaluate | am I closer? | evaluation | user can't tell if the outcome advanced the goal |

*Falsifiable prediction (the pattern for the whole guide).* Locate a suspected problem at a stage
and gulf, then state what a user will do: *"the upload succeeds but the only feedback is below the
fold (Perceive stage, Gulf of Evaluation), so users will re-click Upload, producing duplicates."*
A think-aloud confirms the re-click, or leaves it **unresolved** (a discovery sample can't refute
a low-frequency prediction — `05` §6). *Failing test:* if a claim can't be turned into "user will
do X at stage Y," it is not using the model as an instrument.

*Deferral.* *Why* the user doesn't perceive the feedback — the attention/perception mechanism — is
`cognitive-science/`'s; the model here only localizes *where* the cycle breaks. The origin of the
stages/gulfs and their physical-product form is `industrial-design/06`'s; this guide applies them
to software.

---

## 2. Direct Manipulation — Narrowing Both Gulfs, and Where It Fails

**Direct manipulation** (Shneiderman 1983; the lineage runs back to Sutherland's Sketchpad, `01`)
is the interaction style that most directly attacks both gulfs. Its three properties:

```
  DIRECT MANIPULATION (Shneiderman 1983) -- what it does to the gulfs
  ------------------------------------------------------------------
   1. continuous representation of the object of interest
   2. physical action / labeled button-press in place of command syntax
   3. rapid, incremental, REVERSIBLE actions with immediately visible effect
  ------------------------------------------------------------------
   Effect: narrows the GULF OF EXECUTION (act on the thing, no syntax to recall)
           narrows the GULF OF EVALUATION (effect is visible immediately)
   Cost:   the object must be VISIBLE and SPATIAL to be manipulated directly.
```

But direct manipulation is **not universally superior**, and saying so is where the model earns
its keep. It fails, predictably, when:

- **The object is abstract or invisible.** You cannot directly manipulate "all files older than 30
  days" or "every third row." Bulk, conditional, and repeated operations are where **command,
  query, and programmatic** interfaces beat direct manipulation — *falsifiable prediction:* on a
  "delete all archived items" task, direct-manipulation users will select-and-delete in a slow,
  error-prone loop (Gulf of Execution at the action-sequence stage), while a filter+command path
  will not. A think-aloud on that task confirms or leaves it unresolved.
- **The action is destructive or high-volume.** Immediacy plus low friction is exactly wrong when
  a slip is costly; direct manipulation's *reversibility* property is what saves it, and an
  interface that offers the immediacy without the undo has taken the risk and dropped the
  mitigation.

*Deferral.* The *speed* advantage of pointing at a visible target is Fitts' Law territory —
**cited and applied in `03`**, derived in `cognitive-science/09`. This guide owns only the
*structural* claim: direct manipulation trades generality for immediacy, and the trade is
predictable per task.

---

## 3. Modes and Mode Errors — The Most Falsifiable Model in the Guide

A **mode** is a state in which the *same user action produces a different result*. A **mode
error** occurs when a user acts as if the system were in one mode while it is in another. This is
the cleanest instrument in the module: modes generate *specific, findable* errors.

```
  THE ANATOMY OF A MODE ERROR
  ------------------------------------------------------------------
   same gesture, two meanings, depending on hidden state:
     CAPS LOCK on   ->  "a" produces "A"
     vi normal mode ->  "d" deletes; vi insert mode -> "d" types 'd'
     map "rotate" vs "pan" mode -> one-finger drag does different things
  ------------------------------------------------------------------
   Prediction: users will apply the WRONG mode's action after their
   attention leaves the mode indicator -- at the action stage, Gulf of
   Execution. The error is at a specific step and is confirmable.
```

The design responses, each with its own prediction:

- **Eliminate the mode** (Larry Tesler's modelessness campaign — "Don't Mode Me In"; note Tesler's
  broader **law of conservation of complexity**, that complexity is moved, not destroyed). If no
  mode exists, the mode error cannot occur — the strongest possible fix, when affordable.
- **Make the mode heavily visible and effortful to hold.** Spring-loaded / **quasimodes** (Jef
  Raskin, *The Humane Interface*, 2000): the mode persists only while the user physically holds a
  key, so it cannot be silently forgotten. *Prediction:* quasimodal designs produce far fewer
  persistent-mode errors than latched modes, because the mode's state is tied to muscle, not
  memory.

*Falsifiable prediction / failing test.* For any suspected mode, predict the exact wrong action a
user will take once the mode indicator leaves their attention. If you cannot name the wrong action
and the step it happens at, you have not found a mode error — you have a hunch. *Why* the indicator
leaves attention is `cognitive-science/`'s; *that* it will, and what breaks when it does, is this
model's.

---

## 4. Instrumental Interaction — A Model with Built-In Metrics

For post-WIMP and modern GUIs, **instrumental interaction** (Michel Beaudouin-Lafon, CHI **2000**)
reframes the interface as **domain objects** manipulated through **interaction instruments**
(a scrollbar, a handle, a command — a mediator between the user and the object, analogous to a
physical tool). Its power for this guide is that it comes with **three measurable properties** that
*predict* friction:

```
  INSTRUMENTAL INTERACTION -- three properties that predict friction
  ------------------------------------------------------------------
   DEGREE OF INDIRECTION .... spatial + temporal offset between acting on the
                              instrument and the object's response
                              (a distant slider changing an off-screen value = high)
   DEGREE OF INTEGRATION .... ratio of input-device DOF to instrument DOF
                              (a 2-DOF mouse driving a 1-DOF scrollbar = mismatch)
   DEGREE OF COMPATIBILITY .. similarity between the physical action and the
                              object's response (drag up to move up = high)
  ------------------------------------------------------------------
   Prediction: HIGH indirection, LOW integration, or LOW compatibility each
   predict a specific evaluation- or execution-gulf cost, per instrument.
```

*Falsifiable prediction.* Rate an instrument on the three axes and predict the cost: a color
picker whose hue slider is far from the swatch (high indirection) predicts an evaluation-gulf lag —
users will over-shoot and correct because the effect is offset from the action. A think-aloud plus
time-on-task (`05`) confirms the correction loop or leaves it unresolved. *Failing test:* if
raising indirection or lowering compatibility on an instrument produces **no** predicted change in
behavior, the model was not doing work here.

---

## 5. Distributed Cognition and Activity Theory — Changing the Unit of Analysis

Sometimes the breakdown is not inside one head but in the **system of people, artifacts, and
representations**. Two *applied* lenses widen the unit of analysis — and each still must predict a
findable breakdown, but a **system-level** one: it is confirmed by a **field study** (`06`) and
measured with `09`'s coordination outcomes, and it need **not** map to a single execution/
evaluation gulf (banner).

- **Distributed cognition** (Edwin Hutchins, *Cognition in the Wild*, **1995**; "How a Cockpit
  Remembers Its Speeds," 1995): cognition is spread across people and artifacts, and **the interface
  is part of the cognitive system**, holding and transforming representational state. *Prediction:*
  if a design moves a piece of shared state off a visible external representation and into one
  person's head (e.g., replacing a visible shared checklist with a silent automated step), a
  coordination breakdown will appear at the hand-off — a *findable* **system-level** failure (the
  *other* actor loses access to the shared state), confirmed in the field, not localized to one
  person's gulf. This is the intellectual bridge to `09` (CSCW).
- **Activity theory** (Vygotsky/Leont'ev roots; Engeström's activity systems, **1987**; introduced
  to HCI by Bonnie Nardi, *Context and Consciousness*, **1996**; Kaptelinin & Nardi, 2006): analyze
  the **activity** (subject–tool–object, mediated by rules, community, division of labor), not the
  isolated click. *Prediction:* a tool that fits the task but violates the surrounding **rules or
  division of labor** (e.g., a "faster" approval flow that removes a signature step the
  organization relies on) will be **rejected or worked around** even though it passes a single-user
  usability test — a breakdown you find in the field (`06`), not the lab.

*Deferral and honesty.* These lenses are **descriptive and generative**, not predictive in the
tight statistical sense; their falsifiability is *qualitative* — they predict *where* to look for a
breakdown, and a field study confirms or fails to find it. Presenting them as more precise than
that would overclaim. The *cognitive mechanisms* they invoke are `cognitive-science/`'s; the
*social/organizational* system is `09`'s. This guide owns only their use as fault-localizers.

---

## 6. Mental Models and the System Image — Where Predictions Come From

Underneath every prediction above sits the **mental-model** account (roots in Craik 1943; Norman's
framing): the designer holds a **design model**; the user builds a **user's model** from experience;
the two never meet directly — they communicate **only through the *system image*** (everything the
system presents: UI, feedback, docs, behavior).

```
  DESIGN MODEL  --(communicated only via)-->  SYSTEM IMAGE  --(read by)-->  USER'S MODEL
  ------------------------------------------------------------------
   If the SYSTEM IMAGE is incomplete or inconsistent, the user builds a
   WRONG model -- and a wrong model predicts SYSTEMATIC, repeatable errors,
   not random ones. Predictable error is the signature of a model mismatch.
```

*Falsifiable prediction.* A model mismatch predicts **systematic** error: users who believe
"closing the window quits the app" will lose unsaved work in a repeatable, non-random way. If the
errors you observe are *systematic and consistent with a specific wrong belief*, you have a model
mismatch (fix the system image); if they are *scattered and idiosyncratic*, you likely have a
motor/perceptual issue (a `03` or `cognitive-science/` matter) instead. Distinguishing the two is
exactly what makes the mental-model account an instrument.

---

## A Worked Diagnosis (illustrative, fictional)

*Fictional, to show the models composing into one fault-localization. No real product.*

**System.** *Ledgerly*, a fictional web tool for reconciling bank transactions. Users report it
"feels confusing." That report is a symptom; the models turn it into located, testable faults.

- **Fault A (mode error, §3).** The transaction list has a hidden "match mode" vs "edit mode";
  the same click either links a transaction or opens it for editing. *Prediction:* after attention
  leaves the small mode chip, users will edit when they meant to match (action stage, Gulf of
  Execution). *Fix:* make it a **quasimode** or split the actions.
- **Fault B (evaluation gulf, §1).** A successful match shows a subtle green tick with no text.
  *Prediction:* at the Perceive/Interpret stages, users won't register the match and will re-match
  (Gulf of Evaluation). *Fix:* explicit, textual, above-the-fold confirmation.
- **Fault C (instrumental, §4).** The "confidence" slider that controls auto-match is on a
  settings page, far from the list it affects (high **indirection**). *Prediction:* users will
  over-adjust and thrash because the effect is offset from the action. *Fix:* co-locate the control
  with its effect.
- **Fault D (model mismatch, §6).** Users believe "reconciled" means "sent to the bank"; it only
  means "marked locally." *Prediction:* **systematic** surprise when nothing reaches the bank. *Fix:*
  repair the **system image** — rename the state and show what it does/doesn't do.

**Reading.** "Confusing" decomposed into four faults, each **localized to a stage and a gulf** and
each stated as *what a user will do*. A think-aloud (`05` §4) on scripted tasks confirms A, B, D and
leaves C unresolved if the settings page isn't visited — *unresolved, not cleared* (`05` §6). The
models did their job: they turned a vibe into predictions. What they did **not** do is explain
*why* attention drifts or *how fast* the pointing is — those are `cognitive-science/` and the
Fitts-in-`03` matters, deferred by design.

---

## Reader Tasks (answerable from this guide)

1. **Localize a complaint to a stage and gulf.** Given "I clicked Save and nothing happened, so I
   clicked it three more times," name the stage (Perceive) and gulf (Evaluation), and give the
   prediction a think-aloud would check (repeated clicks / duplicate saves).
2. **Decide when direct manipulation is the wrong instrument.** Given "users must delete every
   invoice older than a year," argue that a filter+command beats select-and-delete, and state the
   execution-gulf prediction that distinguishes them.
3. **Find and fix a mode error.** Given a drawing app where the space bar toggles pan/draw, name
   the wrong action users will take once the indicator leaves attention, and propose a quasimode
   fix — then state why the fix reduces the error.
4. **Score an instrument for friction.** Given a brightness slider that lives in a menu three taps
   from the photo it affects, rate its degree of indirection and predict the resulting behavior
   (over-adjust/thrash), naming the gulf.
5. **Match the failure and model to the right evidence.** Given two bug reports — "everyone loses
   work by closing the window" vs "taps sometimes miss the small icon" — assign the first to a
   system-image/mental-model fix and the second to a `03` motor/performance issue. Then contrast
   both with "the shared dashboard will improve team coordination": that is a **system-level**
   distributed-cognition/activity-theory claim requiring field evidence (`06`) and `09`
   coordination outcomes, not a single-user think-aloud. The evidence must match the model's unit
   of analysis.

---

## Decision Cheat Sheet

| The breakdown looks like… | Reach for | It predicts / localizes |
|---------------------------|-----------|-------------------------|
| "I don't know how to start / what to do" | Gulf of Execution, intention/action-sequence stage (§1) | the feature is unfindable or the order is non-obvious |
| "I can't tell what happened / if it worked" | Gulf of Evaluation, perceive/interpret stage (§1) | missing or ambiguous feedback |
| "the same action did different things" | modes / mode error (§3) | the wrong-mode action, at the action stage |
| "this control is slow/awkward to use" | instrumental interaction (§4) | high indirection / low integration / low compatibility |
| "the number's slow to converge as I drag a distant slider" | degree of indirection (§4) | an evaluation-gulf correction loop |
| "people keep making the *same* wrong assumption" | mental model / system image (§6) | systematic (not random) error from a wrong user model |
| "it tests fine solo but the team won't adopt it" | activity theory / distributed cognition (§5) | a rules/division-of-labor or hand-off breakdown (→ `09`, field study `06`) |
| "why does attention drift / memory fail here?" | `cognitive-science/09` | HCI defers the mechanism |
| "how fast is the pointing/choice itself?" | `03` (Fitts/Hick applied) | HCI defers the derivation |

---

## Common Confusion Points

**"Direct manipulation is always best."** No. It narrows both gulfs for **visible, spatial**
objects and immediate actions, and loses to command/query/programmatic interfaces for **abstract,
bulk, conditional, or repeated** operations. The trade (generality for immediacy) is predictable
per task (§2).

**"Modes are always bad."** No. Modes are a source of a **specific, findable error class**, and the
right fix is often elimination — but heavily-visible or spring-loaded **quasimodes** are a
legitimate design when a mode is genuinely needed. The problem is a *silent, latched, forgettable*
mode (§3).

**"These models explain why users behave as they do."** Only partly, and that's the point of the
deferral. The models tell you **where** a cycle breaks and **what** a user will do; the **why**
(attention, memory, perception) is `cognitive-science/`'s. A model here is a fault-localizer, not a
theory of mind.

**"A model is right if it sounds insightful."** No. A model earns its place **only** by making a
prediction that could be wrong — "users will do X at stage Y." A framing that can absorb any outcome
("well, that's an affordance issue too") is decoration, not an instrument (banner, §1).

**"This is the same as Norman's book."** It applies Norman's action model **to interactive
computing**; the model's **origin, derivation, and physical-product framing** live in
`industrial-design/06`. Read that guide for the model itself; read this one for its use as a
software-diagnosis instrument.

---

## Global, WEIRD, and Resource Caveats

- **Model naturalness is culturally learned, not universal.** "Drag up to scroll up," red-means-stop,
  left-to-right progress, and even the desktop metaphor are **learned conventions** (see `01`) that
  do not transport unexamined. Right-to-left scripts, different color semantics, and unfamiliarity
  with the desktop metaphor can flip a "high compatibility" instrument into a low-compatibility one
  for another population. Compatibility (§4) is relative to the user's learned expectations.
- **Distributed cognition and activity theory are unit-of-analysis choices, not measurements.** They
  are strongest as **generative** lenses for *where to look*; treating their outputs as precise
  predictions overclaims (§5). Their qualitative predictions are confirmed by field study (`06`),
  bounded to the setting studied.
- **The two module invariants ride here.** *Accessibility of the model:* a "direct manipulation"
  design that assumes a precise pointer and a visual object can be a wall for screen-reader, switch,
  and voice users — the accessibility tree (`08`) is the *real* interface for AT, and a model that
  ignores it is under-specified for the population, not done. *Safety/ethics floor:* a model that
  predicts where users fail must not be inverted into engineered friction against the user's interest
  (a dark pattern, `11`), and where a mode error could cause physical harm, the operator-safety
  analysis is `human-factors/`'s, not this guide's.
