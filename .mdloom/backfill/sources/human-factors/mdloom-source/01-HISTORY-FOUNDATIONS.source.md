---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "01-HISTORY-FOUNDATIONS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-factors:history-foundations
kind: guide
module: human-factors
section: human-factors
title: History & Foundations - Why the Discipline's Idioms Exist
status: source-custody
source_custody: partial
current_path: human-factors/01-HISTORY-FOUNDATIONS.md
canonical_path: human-factors/01-HISTORY-FOUNDATIONS.md
backsource_ids: [mdloom-backfill:human-factors:01-history-foundations]
concepts: [history-of-human-factors, scientific-management, knobs-and-dials, aviation-psychology, fitts-list, systems-ergonomics, resilience-engineering]
root_concepts: [history-foundations]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# History & Foundations — Why the Discipline's Idioms Exist

**This guide owns** the *intellectual lineage* of human factors and, crucially, **why the
lineage constrains today's idioms**: the descent from **scientific management** (time-and-
motion, the search for the "one best way"), through the **WWII "knobs-and-dials"** turn
(when "pilot error" was re-read as **design-induced error**) and **aviation psychology**
(Fitts, Chapanis, the Fitts list), into **post-war institutionalization** and **systems /
cognitive ergonomics** (Rasmussen, Reason), and on to **resilience engineering** (Hollnagel,
Woods, Leveson). It explains why the field still *thinks the way it does* — why function
allocation still argues with a 1951 list, why control-room design (`06`) came before
cognitive workload (`03`), and why "human error as a systems property" (`04`) is a hard-won
reversal, not a slogan. **It builds on** `00-OVERVIEW` and frames every later guide. **It
explicitly defers**: the **cognitive mechanisms** the field studies (attention, memory,
perception, decision) to [`cognitive-science/`](../cognitive-science/00-OVERVIEW.md); the
**occupational-load and lifting math** to [`02`](02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS.md); and
**error/reliability/hazard method** to [`04`](04-HUMAN-ERROR-TAXONOMIES.md)/[`05`](05-HUMAN-RELIABILITY-ANALYSIS.md)/[`08`](08-SAFETY-SYSTEMS-AND-HAZARD-ANALYSIS.md). This guide narrates *how the
field came to hold* those tools — it does not re-derive them.

> **Safety & ethics contract (binds every human-factors guide).** This is an
> **educational systems reference**, not an operations manual — and a *history* is not a
> ruling. Nothing here certifies a system, determines an accident's cause, or judges a
> person. Historical accidents are cited as **turning points in the discipline's ideas**,
> attributed and dated; causation of any real event belongs to the error/hazard methods of
> `04`/`08` and to the accountable investigators, never to a label in a timeline.
>
> **Cross-cutting accessibility invariant (a product of this lineage).** The module-wide rule that
> safety-relevant cues ride on **≥2 coding channels** (never color or tone alone) — the
> operator-safety twin of accessibility's "never color alone"
> ([`06` §3](06-DISPLAY-CONTROL-INTERFACE-DESIGN.md), owned there and in `02`) — is *itself* an
> inheritance of the WWII turn below: once "pilot error" was re-read as **design-induced error**,
> an unperceivable single-channel cue became a *design* fault, not an operator failing. The
> history explains why the invariant exists.

*Per-guide banner: every date, name, and figure below is an **attributed, dated** historical
claim, not a universal constant. A percentile, a control layout, or a function-allocation
list from 1943 or 1951 is an artifact of its era and its population — the lesson survives; the
number does not automatically travel.*

---

## The Big Picture: Four Turns That Made the Discipline

Human factors is best read as **four turns**, each a reaction to the last, each leaving an
idiom the field still uses.

```
FOUR TURNS OF HUMAN FACTORS  (each turn leaves an idiom that later guides inherit)
================================================================================
   TURN 1  FIT THE PERSON TO THE JOB          ~1900-1940  scientific management
      Taylor, the Gilbreths: measure the task, find "the one best way", select/train
      -> idiom inherited: TASK ANALYSIS and time-and-motion (feeds guide 10)
      -> blind spot: the human is a variable to optimize, not a system to design for

   TURN 2  FIT THE JOB TO THE PERSON          ~1940-1960  knobs-and-dials / aviation
      Fitts, Chapanis: "pilot error" is DESIGN-INDUCED error; shape-code the controls
      -> idiom inherited: DISPLAY/CONTROL design and compatibility (feeds guide 06)
      -> blind spot: still mostly the PHYSICAL interface; the mind is a black box

   TURN 3  FIT THE SYSTEM TO THE MIND         ~1960-1990  systems / cognitive ergonomics
      Rasmussen (SRK), Reason (GEMS): error is a SYSTEMS property; model the operator's
      cognition; Three Mile Island (1979) makes control-room HF unignorable
      -> idiom inherited: ERROR TAXONOMY and cognitive workload/SA (feeds guides 03, 04)

   TURN 4  FIT THE ORGANIZATION TO FAILURE    ~1990-now   resilience engineering
      Hollnagel, Woods, Leveson: safety is what goes RIGHT under variability (Safety-II);
      model the whole socio-technical system (STAMP)
      -> idiom inherited: HRO, just culture, Safety-II, STAMP/STPA (feeds guides 08, 11)
================================================================================
   The arc: from fitting the PERSON to the job -> the JOB to the person -> the SYSTEM to
   the mind -> the ORGANIZATION to failure. Each turn widened the unit of analysis.
```

The single most important thing this history explains: the **unit of analysis keeps
widening** — from the *worker's motions* (Turn 1) to the *control* (Turn 2) to the
*operator's cognition* (Turn 3) to the *whole socio-technical system* (Turn 4). Every later
guide sits somewhere on this arc.

---

## 1. Turn 1 — Scientific Management: Fit the Person to the Job (~1900–1940)

The discipline's prehistory is **industrial efficiency**, not safety.

- **Frederick W. Taylor**, *The Principles of Scientific Management* (**1911**): decompose a
  job into elements, time each, find "the one best way," and select/train workers to it. The
  worker is an input to optimize.
- **Frank & Lillian Gilbreth** (**1910s–1920s**): *motion* study (Taylor timed; the Gilbreths
  filmed and decomposed motion into elemental "therbligs"). Lillian Gilbreth's psychological
  emphasis is an early bridge toward the human sciences.
- **The Hawthorne studies** (Western Electric, Elton Mayo and colleagues, **1924–1932**):
  attempts to relate lighting/rest to output produced the enduring, still-debated observation
  that *being studied* changes behavior — the **"Hawthorne effect."** It opened the
  *organizational* dimension the field would not fully own until Turn 4 (`11`).

**Idiom inherited:** systematic **task analysis** (guide `10`) and the very idea that work can
be *measured*. **Blind spot the next turn attacks:** the human is treated as a component to be
selected and trained to a fixed design — "fit the person to the job." When the machines got
fast and lethal enough (aircraft), that stopped working.

---

## 2. Turn 2 — Knobs-and-Dials & Aviation Psychology: Fit the Job to the Person (~1940–1960)

World War II put average operators in high-consequence machines under time pressure, and the
result was a data set of **catastrophic, repeatable "pilot error"** that selection and
training could not fix. The turn was to blame the **design**, not the pilot.

- **Alphonse Chapanis** (**1943–1944**): the classic case — B-17 pilots retracted the landing
  gear after landing because the **gear and flap controls were identical and adjacent**.
  Chapanis's fix was **shape-coding** (a wheel-shaped knob for the gear, a flap-shaped knob for
  the flaps) — the birth of **display/control compatibility** (guide `06`).
- **Paul Fitts & Richard Jones** (**1947**): a systematic analysis of hundreds of "pilot-error"
  incidents re-classified them as **design-induced** (control confusion, reversed expectations)
  — the founding argument that error is a property of the *human–machine fit*.
- **The Fitts list / MABA-MABA** (Fitts, **1951**): the first **function-allocation** heuristic
  — "Men-Are-Better-At" (judgment, improvisation, pattern under noise) vs "Machines-Are-Better-
  At" (speed, force, repetition, simultaneous channels). It is *still* the reference point every
  automation argument reacts to (guide `07`).

**Idiom inherited:** **compatibility, coding, and function allocation** (`06`, `07`). **Blind
spot the next turn attacks:** it is still mostly the *physical* interface; the operator's
*cognition* is a black box.

> **Institutionalization.** The **Ergonomics Research Society** (UK, **1949**) coined
> *ergonomics* (K. F. H. Murrell); the **Human Factors Society** (US, **1957**) named the
> American branch. Two names, one discipline — "ergonomics" leaning physical/European,
> "human factors" leaning cognitive/US, now used interchangeably (`00`).

---

## 3. Turn 3 — Systems & Cognitive Ergonomics: Fit the System to the Mind (~1960–1990)

As process plants, aircraft, and computers grew complex, the interesting errors moved
*inside the head* — a mis-formed intention, a wrong mental model — and the unit of analysis
widened from the control to the **cognitive system**.

- **Jens Rasmussen — Skill/Rule/Knowledge (SRK)** (**1983**): behavior runs at three levels
  (automatic skill, stored rules, effortful knowledge-based reasoning), and errors differ by
  level. SRK underwrites both error taxonomy (`04`) and ecological interface design (`06`).
- **James Reason — GEMS and the Swiss-cheese model** (*Human Error*, **1990**): the
  **slip/lapse/mistake** taxonomy, **latent conditions**, and the reframing of error as a
  **systems property** with **defenses-in-depth** that line up holes. This is the intellectual
  core of `04` and `08`.
- **Three Mile Island** (**1979**): the accident that made **control-room human factors**
  unignorable — a confusing indication and a mode-misleading valve light turned a minor fault
  into a partial meltdown. It is cited here as the *turning point that funded and legitimized*
  cognitive systems engineering — **not** as a causation ruling (that belongs to the official
  investigations and to the methods of `04`/`08`).

**Idiom inherited:** the **error taxonomy** and **cognitive workload / situation awareness**
as first-class variables (`03`, `04`). **Blind spot the next turn attacks:** even a good
cognitive model still treats safety as the *absence of error* in an individual operator.

---

## 4. Turn 4 — Resilience Engineering: Fit the Organization to Failure (~1990–now)

The newest turn widens the unit of analysis one more time — to the **whole socio-technical
organization** — and *inverts* the question.

- **High-Reliability Organizations** (Weick, Sutcliffe, and the Berkeley group, **1990s–2000s**):
  some organizations run hazardous technology with far fewer accidents than expected — through
  *mindfulness*, preoccupation with failure, and deference to expertise (`11`).
- **Safety-I → Safety-II** (Erik Hollnagel, **~2014**): Safety-I studies *what goes wrong*
  (count and remove failures); **Safety-II** studies *what goes right* — how operators adapt to
  keep a variable system working — and treats everyday performance variability as the source of
  *both* success and failure (`11`).
- **STAMP / STPA** (Nancy Leveson; foundational paper *Safety Science* **2004**; *Engineering a
  Safer World*, MIT Press **2011**): recast safety as a **control problem** — accidents as
  inadequate control of a socio-technical system, not chains of component failures (`08`).

**Idiom inherited:** **HRO, just culture, Safety-II, and control-theoretic hazard analysis**
(`08`, `11`). The arc is complete: the discipline now designs for a *system that will vary and
must stay safe anyway*.

---

## 5. Why the Lineage Constrains Today's Idioms

The history is not decoration; it explains **live constraints**:

```
LINEAGE -> LIVE CONSTRAINT  (why the field still argues the way it does)
--------------------------------------------------------------------------------
   Fitts list (1951)        -> every automation debate (07) still starts from MABA-MABA,
                               even though "fixed lists" are now seen as too static
   knobs-and-dials (1940s)  -> display/control design (06) matured DECADES before
                               cognitive workload (03) -- the physical came first
   Reason/Rasmussen (1980s) -> "human error" is a START of analysis, not an end (04),
                               a reversal that still fights the folk "blame the operator"
   Three Mile Island (1979) -> control-room HF and mode-visibility (06) are treated as
                               safety-critical, not cosmetic
   Safety-II (2010s)        -> counting failures (Safety-I) is no longer the whole story;
                               resilience (11) is now a design target
```

The most important inheritance is **epistemic**: because the field learned the hard way that
a 1940s "average airman" cockpit fit almost no one, and that a 1951 function list is a
heuristic and not a law, human factors is *constitutionally suspicious of universalized
figures*. That suspicion is the module's bounded-model stance (`02`, `05`).

---

## A Worked "Dating" Pass — The "Average Airman" Collapse (attributed + reproducible)

*This is the history guide's quantitative demonstration: a **dated study** plus a
**reproducible arithmetic illustration** of why it mattered. It imports no exposure math and
draws no operational conclusion.*

**The dated study.** Lieutenant **Gilbert S. Daniels**, *The "Average Man"?* (Wright Air
Development Center, Technical Note, **1952**), measured **4,063** US airmen on **10** body
dimensions and asked how many were "average" (within a middle band) on **all ten**. The
answer, famously, was **zero**. The result helped push the US Air Force from **fixed-size**
cockpits to **adjustable** ones (adjustable seats, pedals, harnesses) — the historical seed of
guide `02`'s *design-for-a-distribution* logic.

**Reproducible illustration (synthetic, to show the mechanism).** Suppose each dimension's
"average band" captures a fraction *p* of people, and — as a deliberately simplifying
assumption — dimensions were independent. Then the fraction average on *all k* dimensions is
`p^k`:

```
THE MULTIVARIATE COLLAPSE  (synthetic arithmetic; p = middle-band fraction per dimension)
--------------------------------------------------------------------------------
   p = 0.30 (middle 30% band on each dimension, independence ASSUMED)
      k = 1 dimension   ->  0.30            (30% are "average")
      k = 3 dimensions  ->  0.30^3 = 0.027  (~2.7%)
      k = 5 dimensions  ->  0.30^5 = 0.00243 (~0.24%)
      k = 10 dimensions ->  0.30^10 ~= 5.9e-6  (~6 per million -> ~0 in 4,063)
   -> the "average person" on MANY dimensions at once essentially does not exist.
```

**Uncertainty / validity / bias note.** (1) The independence assumption is *false* — real
body dimensions are positively correlated, so the true fraction is **higher** than `p^k` but
still collapses toward zero as *k* grows (guide `02` does the correlated, bivariate-normal
version properly; here the point is the *direction*, and the arithmetic is a synthetic
illustration, not Daniels's exact method). (2) The Daniels sample is **1950s US military
airmen** — WEIRD, male, selected, and dated; the *lesson* (design for a distribution)
transfers, the *numbers* do not. (3) This is a **historical-methodology** demonstration, not
an anthropometric assessment of any real population — that modeling belongs to `02`.

---

## A Fully Worked Case — Reading an Idiom Back to Its Turn (illustrative, fictional)

*Fictional. It shows how the lineage explains a present-day design argument — not a ruling
about any real system.*

**Setting.** A *fictional* team designing a new tram cab argues: "just automate the
speed-limit enforcement fully — the driver keeps missing it." A human-factors reviewer uses
the **history** to structure the argument, not to settle it:

1. **Name the turn each claim comes from.** "The driver keeps missing it" is a **Turn 1**
   ("blame/train the person") reflex; "the control confused them" is a **Turn 2** move; "what's
   the driver's mental model and workload?" is **Turn 3**; "what happens to the *system* when
   the automation is trusted and then fails?" is **Turn 4** (the ironies of automation, `07`).
2. **Surface the inherited idiom.** The "just automate it" proposal is a **Fitts-list (1951)**
   argument — machines-are-better-at vigilance — and the reviewer flags that the *same 1951
   list* also warns that humans are the fallback when the machine hits its boundary, which is
   where automation surprises live (`07`).
3. **Refuse the ahistorical shortcut.** Because the field learned from **Three Mile Island**
   that a confusing indication plus a trusted-but-wrong signal is its own hazard, the reviewer
   routes the *mode-visibility* question to `06` and the *function-allocation* trade-off to
   `07`, rather than accepting "full automation" as obviously safe.
4. **Keep the boundary.** *Why* the driver's attention lapses is **cognitive-science**'s; the
   *speed-enforcement system* is **`transportation/`**'s; whether to adopt the change is the
   **operator and its regulator**'s. History supplies the *frame*, not the verdict.

**Reading.** The lineage turned "just automate it" from a slogan into a structured set of
owned questions and honest deferrals — which is exactly what a foundations guide is for.

---

## Reader Tasks (answerable from this guide)

1. **Place five milestones on the four turns.** Assign Taylor (1911), Chapanis's landing-gear
   fix (1943), the Fitts list (1951), Reason's Swiss cheese (1990), and STAMP (2004) to their
   turn, and state the *idiom* each left behind (§1–4).
2. **Run the average-man collapse.** With `p = 0.30` and independence, compute the average-on-
   all fraction for `k = 1, 3, 5`; explain why correlated dimensions make the true number
   *larger but still collapsing*, and why the honest conclusion is "design for a distribution"
   (Worked pass, §2).
3. **Date a figure.** Given "the cockpit is sized to the 1950 average airman," explain — using
   Daniels — why that is a *dated, population-bound* figure and not a universal human constant,
   and what the field did instead (§2, Worked pass).
4. **Trace an idiom to its turn.** For "we allocate the boring vigilance task to the automation
   and keep judgment with the operator," name the 1951 source and the later warning that
   complicates it (§2, §5; forward to `07`).
5. **Hold the boundary.** State one thing this history guide owns (the *lineage of ideas*) and
   two it defers (the *cognitive mechanism* and the *lifting/exposure math*), and why a history
   should not import either (opening, §5).

---

## Decision Cheat Sheet

| If you're asking... | The history says | Go to |
|---|---|---|
| "Why do we still argue MABA-MABA?" | it descends from the **Fitts list (1951)** | `07` |
| "Why is control/display design so mature?" | the **knobs-and-dials** turn (1940s) came first | `06` |
| "Why isn't 'human error' the final answer?" | **Reason/Rasmussen (1980s)** made it a systems property | `04`, `08` |
| "Why do we design adjustable, not average?" | **Daniels (1952)**: nobody is average on everything | `02` |
| "Why model the whole organization?" | **resilience engineering / Safety-II (2010s)** | `11` |
| "Why is a mode-confusing indication a hazard?" | **Three Mile Island (1979)** made it one | `06` |
| "Is this old figure still valid?" | treat it as **dated and population-bound**, re-verify | `02`, `10` |
| "Why did this accident happen?" | **out of scope** — causation is `04`/`08` + investigators | — |

---

## Common Confusion Points

**"Ergonomics and human factors are different fields."** They are two names (UK/physical vs
US/cognitive origins) for one discipline, now used interchangeably (§2). MAXIM splits *product-
form* ergonomics (`industrial-design/05`) from *quantitative-systems* human factors by
**depth**, not by the historical label.

**"Scientific management was human factors."** It was the *prehistory* — it measured tasks but
fit the *person to the job*. The discipline proper begins when WWII flipped that to fitting the
*job to the person* (§1–2).

**"'Human error' was always understood as a systems problem."** No — that is a hard-won
**Turn 3** reversal (Rasmussen/Reason, 1980s). The folk instinct to "blame and retrain the
operator" is the **Turn 1** reflex the field spent decades overturning (§3, §5).

**"The Fitts list tells you what to automate."** It is a **1951 heuristic**, not a law; it
still frames the debate but is criticized as too static, and it also names the human as the
*fallback* — which is where automation surprises live (§2, §5; `07`).

**"A historical accident proves a cause."** This guide cites accidents as **turning points in
the discipline's ideas**, dated and attributed; causation of any real event belongs to the
methods of `04`/`08` and the official investigators (safety contract, §3).

---

## Global, WEIRD & Resource Caveats

- **The canonical history is Western and military/industrial.** Taylorism (US industry), the
  knobs-and-dials turn (US/UK military aviation), and the founding societies (UK 1949, US 1957)
  are a *particular* lineage; other industrial cultures developed parallel practices that this
  standard narrative under-represents. The dates and names are attributed, not universal.
- **Founding datasets are WEIRD/selected.** Daniels's airmen (1952) are male, US, military, and
  fit — the *origin* of design-for-a-distribution is itself a biased sample, which is exactly why
  guide `02` insists on naming whose population a percentile describes.
- **The "turns" are a teaching simplification.** Real practice mixed all four turns at once, and
  organizations at different resource levels still sit at different turns today — a low-resource
  workshop may operate in a "Turn 1" world while a high-reliability plant works in "Turn 4." The
  arc is a lens, not a ladder every organization has climbed.

---

## A Contrasting Example (non-WEIRD, low-resource)

*Fictional, to show the lineage is not the only path to the same insight.*

**Setting.** A *fictional* artisanal boatyard in a low-income coastal region has, for
generations, shape-coded its winch and brake levers by feel (a knurled grip means "brake") and
rotates crews off the heavy-haul station on a tide-based rhythm. It has **no** Chapanis, no
Fitts list, and no written task analysis.

**What the history clarifies.** The boatyard independently arrived at **Turn 2** idioms
(shape-coding to prevent control confusion) and **Turn 1/Turn 4** practices (rotation to manage
fatigue; deference to the most experienced hauler). The lesson: the *insights* are not the
property of the Western timeline — they recur wherever consequential work meets human limits.
What the formal lineage adds is **naming, dating, and generalizing** the idioms so they can be
taught and checked — and what it must not do is treat its own dates and figures as universal, or
imply the boatyard's undocumented practice is unsafe because it is unwritten (that would be a
certification ruling the module does not make).
