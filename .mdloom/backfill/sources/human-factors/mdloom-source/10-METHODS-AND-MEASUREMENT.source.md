---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "10-METHODS-AND-MEASUREMENT.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-factors:methods-and-measurement
kind: guide
module: human-factors
section: human-factors
title: Methods & Measurement - How Human Factors Gathers Evidence
status: source-custody
source_custody: partial
current_path: human-factors/10-METHODS-AND-MEASUREMENT.md
canonical_path: human-factors/10-METHODS-AND-MEASUREMENT.md
backsource_ids: [mdloom-backfill:human-factors:10-methods-and-measurement]
concepts: [task-analysis, hierarchical-task-analysis, cognitive-task-analysis, observation-methods, simulation-fidelity, physiological-instrumentation, coverage-sampling, usability-for-safety]
root_concepts: [methods-and-measurement]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Methods & Measurement — How Human Factors Gathers Evidence

**This guide owns** the *methods human factors uses to gather evidence about human performance*:
**task analysis** (hierarchical task analysis; cognitive task analysis), **observation** (field
study, think-aloud/verbal protocol, link analysis), **self-report** instruments (the workload/SA
measures of `03`, surveys, structured interviews), **physiological instrumentation** (eye
tracking, cardiac, pupil, EEG — the *how* behind `03`'s measures), **simulation** (fidelity and
its trade-offs), **usability-for-safety** (use-error evaluation), and — the load-bearing
discipline — **study design as a coverage/sampling problem**: does the operator, task, and
condition sample actually cover the population and the critical cases? **It builds on** `03`
(which measures workload/SA constructs; this guide owns the *study machinery*) and feeds every
other guide, which consumes its evidence. **It explicitly defers**: **inferential statistics** —
sampling theory, power, significance testing, effect-size estimation, and regression — to
[`statistics-applied/`](../statistics-applied/00-OVERVIEW.md); the **cognitive mechanism** the
measures probe to [`cognitive-science/`](../cognitive-science/00-OVERVIEW.md); and **general
interactive-usability method** to
[`human-computer-interaction/`](../human-computer-interaction/06-RESEARCH-METHODS.md) (this guide
borrows it and aims it at *safety/use-error*).

> **Safety & ethics contract (binds every human-factors guide).** This is an **educational
> systems reference**. A method here is a **way to gather evidence**, **not** a validation
> sign-off, a certification protocol, an accident-investigation procedure, or a fitness-for-duty
> test. A passing usability study does **not** certify a system safe; a physiological reading does
> **not** assess a person. The methods produce **evidence with stated coverage and uncertainty**;
> **acceptance belongs to the accountable organization and its regulator**, never to this module.

*Per-guide banner: every measure is a **proxy with a validity domain, an intrusiveness cost, and
a sampling frame**. Evidence is only as good as *whom, what, and under which conditions* you
measured — the coverage argument below is the difference between evidence and a convenient
anecdote.*

---

## The Big Picture: From Question to Bounded Evidence

Human-factors measurement runs a pipeline from a question to **bounded evidence** — and the two
places it most often breaks are the **front** (measuring the wrong task, or the task-as-imagined
rather than task-as-done) and the **sampling** (measuring a convenient few and generalizing to
everyone).

```
THE MEASUREMENT PIPELINE  (and where it breaks)
================================================================================
   QUESTION  (e.g., does the new console lower error under upset conditions?)
        |  (1) TASK ANALYSIS -- decompose the REAL task (HTA/CTA)  <- break: work-as-imagined
        v
   CHOOSE MEASURES  (performance / self-report / physiological / observation)
        |  (2) each measure has validity, sensitivity, INTRUSIVENESS, a construct claim
        v
   DESIGN THE STUDY  (who? which tasks? which conditions?)
        |  (3) SAMPLING & COVERAGE  <- break: convenience sample, critical cases uncovered
        v
   COLLECT in a SETTING  (field / simulation at some FIDELITY / lab)
        |  (4) fidelity vs cost vs ecological validity trade
        v
   BOUNDED EVIDENCE  -> hand INFERENCE (significance, power, effect size) to statistics-applied/
================================================================================
   This guide OWNS steps 1-4 (how to decompose, measure, sample, and stage). It DEFERS
   the inferential step -- whether a difference is "significant" and with what power -- to
   statistics-applied/. The signature failure it exists to prevent: generalizing a
   convenience sample without a COVERAGE argument.
```

---

## 1. Task Analysis — Decompose the Real Task First

You cannot measure or design for a task you have not decomposed. Two families:

- **Hierarchical Task Analysis (HTA)** — Annett & Duncan, **1967**. Decompose a **goal** into
  sub-goals and **operations**, governed by **plans** (the conditions under which sub-goals run).
  HTA is the workhorse input to nearly every other method (it feeds the FMEA rows of `08`, the HRA
  decomposition of `05`, and the interface layout of `06`).
- **Cognitive Task Analysis (CTA)** — for *knowledge-based* work where the difficulty is
  invisible: the **Critical Decision Method** (Klein, Calderwood & MacGregor, **1989**) and
  **Applied CTA** (Militello & Hutton, **1998**) elicit the **cues, decisions, and mental models**
  experts use. CTA is how you surface the *rule- and knowledge-based* work that HTA's operations
  can miss (`04`).

```
HTA vs CTA  (decompose the OBSERVABLE vs elicit the HIDDEN)
--------------------------------------------------------------------------------
   HTA  goal -> sub-goals -> operations, with PLANS      what is DONE (observable steps)
        good for procedures, layout (06), FMEA rows (08)
   CTA  cues -> decisions -> mental models (CDM/ACTA)    what is THOUGHT (hidden expertise)
        good for diagnosis, novel faults, knowledge work (04, 03)
   -----------------------------------------------------------------------------
   CRITICAL: analyze WORK-AS-DONE, not work-as-imagined. The procedure on paper is a
   hypothesis; the real task includes the adaptations, workarounds, and cues that only
   observation/CTA reveal (feeds the error/violation distinction of guide 04).
```

---

## 2. Observation and Self-Report

- **Direct observation and field study** capture work-as-done in context; **ethnographic** methods
  capture the culture (`11`). **Link analysis** counts movements/transitions between displays,
  controls, or people to inform layout (`06`).
- **Verbal protocol / think-aloud** (Ericsson & Simon, *Protocol Analysis*, **1984**) externalizes
  reasoning — powerful for `04`/`06`, but **reactive** (thinking aloud changes the task) and unable
  to report automatic, skill-level processing.
- **Self-report instruments** — **NASA-TLX** and the SA measures (SAGAT/SPAM/SART) of `03`, plus
  surveys and structured interviews. All are **proxies** with the confounds `03` details;
  retrospective self-report also drifts with memory and social desirability.

---

## 3. Physiological Instrumentation

The *measures* (cardiac, pupil, ocular, EEG) belong to `03`; this guide owns the **instrumentation
and its pitfalls**.

```
PHYSIOLOGICAL MEASURES  (the how -- each with an artifact/confound)
--------------------------------------------------------------------------------
   EYE TRACKING     fixations/dwell/scan path -> attention allocation (06 layout)
                    artifact: calibration drift, glasses, lighting
   CARDIAC (HR/HRV) arousal/effort proxy                 confound: physical load, caffeine
   PUPILLOMETRY     effort proxy (task-evoked response)  confound: LIGHTING dominates -> control it
   EEG / fNIRS      engagement/workload indices          artifact: motion, muscle, low field-usability
   -----------------------------------------------------------------------------
   RULE: a physiological signal is a POPULATION-level proxy with artifacts, never a readout
   of a person's mind and never a fitness test. Control the confound (lighting for pupil,
   motion for EEG) or the "workload effect" is an artifact.
```

---

## 4. Simulation and Fidelity

Because the interesting cases (upsets, emergencies) are rare or dangerous to stage live, human
factors relies on **simulation** — and the central design variable is **fidelity**.

```
FIDELITY TYPES AND THE TRADE  (higher fidelity is not always better)
--------------------------------------------------------------------------------
   PHYSICAL fidelity   does it LOOK/feel like the real console?
   FUNCTIONAL fidelity does it BEHAVE like the real system (dynamics, faults)?
   PSYCHOLOGICAL fidelity  does it induce the real STRESS/stakes/workload?
   -----------------------------------------------------------------------------
   TRADE: fidelity costs money and time; the RIGHT fidelity matches the QUESTION.
      testing alarm salience -> need functional + psychological fidelity, less physical
      testing reach/layout   -> need physical fidelity (a mock-up), less functional
   ECOLOGICAL VALIDITY: a high-physical-fidelity sim with LOW psychological fidelity (no
   real stakes) can measure the wrong thing -- calm performance that vanishes under real stress.
```

---

## 5. Usability-for-Safety (borrowed method, safety aim)

General interactive-usability method is `human-computer-interaction/`'s; human factors **borrows**
it and aims it at **use-error and use-related risk** — the errors an interface *induces* that have
safety consequences. **Formative** studies (few users, find problems) shape the design;
**summative** studies (more users, characterize performance) describe it — but even a strong
summative study **does not certify safety** (safety contract). The safety-relevant twist is that
the sample must include the **full operator range**, including operators with disabilities and the
sensory/anthropometric tails (`02`, `06`), because a safety-critical use-error in an under-sampled
sub-population is exactly the one that will be missed.

**The ≥2-channel invariant, from the measurement side.** A use-error study must both *verify* that
safety-relevant cues are perceivable on **≥2 coding channels** (never color or tone alone) and
*sample* the sensory/anthropometric tails a single-channel cue fails — the operator-safety twin of
accessibility's "never color alone" ([`06` §3](06-DISPLAY-CONTROL-INTERFACE-DESIGN.md)). An
under-sampled tail (a coverage failure, §Worked pass) hides exactly the operators a one-channel cue
excludes.

---

## The Boundaries (ownership in one place)

```
WHO OWNS WHAT AROUND METHODS
--------------------------------------------------------------------------------
   this guide (10)      the METHODS: task analysis, observation, instrumentation,
                        simulation, use-error study, and STUDY/SAMPLING/COVERAGE design
   statistics-applied/  the INFERENCE: sampling theory, power, significance, effect size,
                        regression, uncertainty propagation
   03 (workload/SA)     the CONSTRUCTS the instruments measure (and their confounds)
   human-computer-interaction/  general interactive-usability method (borrowed here for safety)
   cognitive-science/   the MECHANISM the measures probe
   -----------------------------------------------------------------------------
   Rule: this guide designs the study and argues COVERAGE; it hands the inferential
   statistics to statistics-applied/, validates nothing as "safe", and assesses no person.
```

---

## A Worked Study-Design Pass — The Coverage Argument (reproducible)

*Synthetic throughout. It demonstrates a **coverage/sampling argument** — the method's signature
discipline — and explicitly hands the inferential question to `statistics-applied/`. It is not a
study protocol, a validation, or a certification.*

**The question (synthetic).** Does a new console **lower operator error under upset conditions**?
Define the space the evidence must cover — **operators × tasks × conditions** — and score coverage.

```
THE SAMPLING FRAME  (orthogonal, fully CROSSED factors -- the space to cover)
--------------------------------------------------------------------------------
   Use CROSSED factors, not overlapping "strata": experience and sensory/anthropometric
   profile are DIFFERENT axes -- an experienced operator can ALSO be in the sensory tail --
   so they must be crossed, never merged into one 3-way stratum (which double-counts).
   EXPERIENCE (E):   novice | experienced                              (x2)
   PROFILE    (P):   typical | sensory/anthro TAIL                     (x2)
                     (e.g., color-vision-deficient, or 5th/95th reach)
   TASK       (T):   routine | critical/off-normal                    (x2)
   SHIFT      (C):   day | night                                      (x2)
   -----------------------------------------------------------------------------
   FULL SPACE = 2 (E) x 2 (P) x 2 (T) x 2 (C) = 16 crossed cells evidence should touch.
   (Alternative when a full cross is impractical: a REQUIREMENTS-COVERAGE MATRIX --
   map each safety requirement to the cases that must exercise it, and cover the map.)
```

**A convenience sample vs a coverage-designed sample.**

```
COVERAGE OF TWO SAMPLES  (which of the 16 cells are actually touched?)
--------------------------------------------------------------------------------
   CONVENIENCE: "8 experienced, typical-profile operators, routine task, day shift"
      cells touched = experienced x typical x routine x day = 1 of 16 -> COVERAGE = 1/16 ~ 6%
      UNCOVERED: every NOVICE cell, every TAIL-profile cell, every CRITICAL-task cell,
      every NIGHT cell
      -> the study answers a question about TYPICAL ROUTINE DAY EXPERTS and says NOTHING
         about the novice/tail/upset/night cases -- exactly the SAFETY-relevant ones.

   COVERAGE-DESIGNED: sample so every cell (esp. critical x night x novice x tail) is touched
      target >= 1 (ideally several) participants per cell -> 16 cells covered
      COVERAGE = 16/16 = 100% of the frame (sample size PER cell is the statistics-applied/
      question of power; COVERAGE is whether the cell is touched AT ALL)
   -----------------------------------------------------------------------------
   KEY DISTINCTION: COVERAGE (are the critical cells represented?) is THIS guide's;
   POWER/significance (is n-per-cell enough to detect a difference?) is statistics-applied/'s.
   A convenience sample fails on COVERAGE before any statistics are even run.
```

**Why this is the module's signature failure.** The convenience study's ~6% coverage is not a
statistics problem — no amount of significance testing fixes the fact that the **novice,
tail-profile, critical-task, and night-shift cells were never observed**. Generalizing "the new
console reduces error" from typical routine-day experts to the whole operating envelope is the
exact overreach guide `10` exists to prevent.

**Measurement-quality checks (per measure).**

```
IS THE MEASURE ANY GOOD?  (four questions before you trust a number)
--------------------------------------------------------------------------------
   VALIDITY      does it measure the construct? (a pupil change may be lighting, not effort)
   SENSITIVITY/  does it move with the manipulation? (a floor/ceiling measure won't)
     DIAGNOSTICITY
   INTRUSIVENESS does measuring it CHANGE the task? (a secondary-task probe adds load;
                 think-aloud is reactive)
   RELIABILITY   would a repeat / another rater agree? (record inter-rater for coded data)
```

**Uncertainty / validity / bias note.** (1) The frame and coverage percentages are **synthetic**,
but the *pattern* — convenience samples systematically miss the critical/night/novice/tail cells —
is real and is the WEIRD/convenience-sample problem in operator research. (2) **Coverage is
necessary, not sufficient**: touching every cell says nothing about *how many* per cell — that is
`statistics-applied/`'s power question. (3) Every measure carries the validity/intrusiveness
caveats above; a "workload reduction" can be a measurement artifact (lighting, reactivity). (4)
This is a **study-design demonstration**, not a protocol, a validation, or a certification, and no
physiological reading here assesses any person.

---

## A Fully Worked Case — Designing the Evidence for a Redesign (illustrative, fictional)

*Fictional. It demonstrates method selection and coverage design — not a study protocol,
validation, or certification for any real system.*

**Setting.** *Fictional* **Cygnet Utilities** wants evidence on whether a redesigned alarm console
"works." Human factors designs the *evidence*, not a verdict:

1. **Decompose the real task first (§1).** HTA the operator's alarm-response task; CTA the
   *diagnosis* of an upset (the hidden, knowledge-based part) — capturing work-as-done, not the
   paper procedure (`04`).
2. **Choose measures for the question (§2–3).** Primary: **error/response performance** on
   scenarios; secondary: **NASA-TLX** (workload) and a **SAGAT** freeze (SA) from `03`; **eye
   tracking** for alarm salience — each with its confound controlled (lighting for pupil, calibration
   for gaze).
3. **Design for coverage, refuse the convenience sample (§Worked pass).** Cross the factors —
   **experience** (novice/experienced) × **profile** (typical/sensory-anthro tail) × **task**
   (routine/off-normal) × **shift** (day/night) — and sample so every cell is touched (or, if a
   full cross is impractical, build a **requirements-coverage matrix**). The convenient "typical
   day-shift experts on routine alarms" would leave the dangerous cells dark.
4. **Choose the setting and fidelity (§4).** Use a **functional + psychological**-fidelity
   simulator so the upset scenarios induce real workload; physical fidelity of the exact bezel
   matters less than behaving and *feeling* like an upset.
5. **Hand off inference and acceptance (§Boundaries).** Whether the observed workload/error
   difference is **statistically significant and adequately powered** goes to
   `statistics-applied/`; whether the console is **accepted** is Cygnet's and its regulator's — the
   study yields **bounded evidence with stated coverage**, not a "safe" verdict.

**Reading.** Real task decomposed, measures matched to the question with confounds controlled, and
— the crux — a **coverage-designed sample** that touches the critical cells, with inference and
acceptance deferred. The method's job is trustworthy evidence, not a sign-off.

---

## Reader Tasks (answerable from this guide)

1. **Pick HTA vs CTA.** For "lay out the controls by how the operator moves between them" vs
   "understand how an expert diagnoses a novel fault," choose the task-analysis method and justify it
   (§1).
2. **Compute coverage and name the gap.** For the convenience sample "8 experienced,
   typical-profile operators, routine task, day shift," compute coverage of the **16-cell crossed
   frame** (E×P×T×C), list the uncovered safety-relevant cells, and explain why *no* statistical
   test repairs a coverage failure (§Worked pass).
3. **Separate coverage from power.** Explain the difference between "did we touch the critical
   night/novice/tail cells?" (this guide) and "is n-per-cell enough to detect a difference?"
   (`statistics-applied/`), and why the first must be answered first (§Worked pass, Boundaries).
4. **Control a measurement confound.** Given "pupil diameter rose, so workload rose," name the
   dominant confound and the control you'd add, and state the intrusiveness cost of a secondary-task
   probe (§3, Worked pass).
5. **Choose fidelity for the question.** For testing alarm salience under stress vs testing reach,
   say which fidelity types matter most and why a high-physical/low-psychological simulator can
   measure the wrong thing (§4).

---

## Decision Cheat Sheet

| Situation | Method | Why (this guide) |
|---|---|---|
| Need to decompose an observable procedure | **HTA** (goals→ops→plans) | feeds FMEA/HRA/layout (§1) |
| Need the hidden expert reasoning | **CTA / CDM / ACTA** | surfaces knowledge-based work (§1) |
| Capture work-as-done in context | **field observation / ethnography** | procedure ≠ reality (§1–2) |
| Externalize reasoning on a task | **think-aloud** (mind reactivity) | proxy for the plan; reactive (§2) |
| Attention allocation on a display | **eye tracking** (control lighting) | informs layout/salience (§3, `06`) |
| Rare/dangerous scenarios | **simulation** at fidelity matched to the question | stage the upset safely (§4) |
| Find use-errors with safety impact | **usability-for-safety** (full operator range) | borrowed from HCI, aimed at risk (§5) |
| Tempted to generalize a few operators | **build a coverage argument first** | convenience samples miss critical cells (§Worked pass) |
| "Is this difference significant / powered?" | hand to **`statistics-applied/`** | inference is deferred (Boundaries) |
| "Does this validate/certify the system?" | **out of scope** — org + regulator decide | safety contract |

---

## Common Confusion Points

**"We tested it with 8 users, so it generalizes."** Not without a **coverage argument**. Eight
typical day-shift experts on the routine task cover ~6% (1 of 16 cells) of a crossed
experience×profile×task×shift frame and miss every safety-critical cell. Coverage is a *design*
property you must argue, separate from sample size (§Worked pass).

**"Coverage and statistical power are the same thing."** No. **Coverage** asks whether the critical
cells are *touched at all* (this guide); **power** asks whether *n-per-cell* can detect a difference
(`statistics-applied/`). A study can be well-powered on the wrong, uncovered population (§Worked
pass, Boundaries).

**"A physiological signal reads the operator's mind."** It is a **proxy with artifacts** — pupil
tracks lighting as much as effort, EEG tracks motion. Control the confound, treat it as
population-level evidence, and never use it as a fitness test (§3, safety contract).

**"Higher-fidelity simulation is always better."** Fidelity should match the **question**; a
gorgeous physical mock-up with no real stakes (low psychological fidelity) can measure calm
performance that evaporates under real stress (§4).

**"A passing usability study certifies the system safe."** It produces **evidence** of use-error
performance for the sample tested; it is not a safety certificate, and acceptance belongs to the
organization and regulator (§5, safety contract).

---

## Global, WEIRD & Resource Caveats

- **The operator-research canon is WEIRD/convenience-sampled.** Much HF evidence comes from
  available, Western, often young/student or expert-operator samples; the *methods* transfer, but any
  *result* inherits its sample's bounds. The coverage argument is precisely the antidote — name whom
  you measured.
- **Instrumentation is resource-gated.** Eye trackers, EEG, and high-fidelity simulators are
  resource-rich tools; low-resource settings rely on observation, structured interview, and low-cost
  simulation. That is *not* inferior evidence if the **coverage** is argued — a well-covered
  observational study can beat a high-tech convenience sample.
- **The tails are a safety sample, not an afterthought.** Operators with disabilities and the
  sensory/anthropometric tails (`02`, `06`) must be a first-class stratum, because a safety-critical
  use-error in an under-sampled sub-population is the one that gets missed — under-sampling them is a
  safety bias, not a mere coverage gap.

---

## A Contrasting Example (non-WEIRD, low-resource)

*Fictional, to show method choice when instrumentation is scarce.*

**Setting.** A *fictional* municipal water utility in a low-income region wants evidence on a new
manual-logging procedure but has **no** eye trackers, **no** simulator, and a small, mixed-experience
crew.

**How the methods adapt.**
- **Method substitution, not method abandonment.** Replace instrumented workload with **structured
  observation + NASA-TLX** (a paper instrument) and **think-aloud** on real tasks; replace the
  simulator with **low-fidelity tabletop scenarios** that still induce the decision. The *reasoning*
  (HTA the task, measure workload/SA, observe work-as-done) is intact.
- **Coverage over sample size.** With a small crew, the crux is **coverage**: deliberately include
  the night-shift, the newest operator, and any operator at the sensory/anthropometric tails, and the
  off-normal task — a well-*covered* small study beats a larger convenience sample of day-shift
  experts.
- **Defer inference and refuse the verdict.** With few participants, the utility should treat results
  as **formative/bounded evidence**, hand any significance/power question to `statistics-applied/`,
  and **not** claim the procedure is "validated" or "safe" — acceptance stays with the utility and its
  authority. The honest output is *covered, bounded evidence*, not a certification.
