---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "01-CLINICAL-ENCOUNTER.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:clinical-medicine:clinical-encounter
kind: guide
module: clinical-medicine
section: clinical-medicine
title: The Clinical Encounter - History and Physical as Information Architecture
status: source-custody
source_custody: partial
current_path: clinical-medicine/01-CLINICAL-ENCOUNTER.md
canonical_path: clinical-medicine/01-CLINICAL-ENCOUNTER.md
backsource_ids: [proof-backfill:clinical-medicine:01-clinical-encounter]
concepts: [clinical-encounter, problem-representation, semantic-qualifiers, illness-scripts, hypothesis-driven-gathering]
root_concepts: [clinical-reasoning]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# The Clinical Encounter — History and Physical as Information Architecture

**This guide owns** the clinical encounter treated as **information architecture**: how a
clinician turns a person's story and body into structured, decision-ready data —
hypothesis-driven data gathering, the compression step called **problem representation**,
the abstraction layer of **semantic qualifiers**, and the expert knowledge structures
(**illness scripts**) that gathered data is matched against. **It builds on** nothing
inside the module (it is the entry point) and feeds `02-DIFFERENTIAL-DIAGNOSIS` (the
problem representation is what a differential is generated *from*). **It explicitly
defers** the *anatomy and physiology* a finding reflects to `human-biology/`; the
*diseases* a script encodes to `disease/`; the *test catalog* to `medicine/10`; and the
*psychology of the interview relationship* to `psychology/`. This is **not** a how-to for
performing a history or physical exam — it is the *information theory* of the encounter:
what signal each maneuver carries and how it is structured for reasoning.

> **This module is an educational reference about *how clinical medicine reasons and
> how care is organized* — the cognitive and system architecture of the discipline.
> It is *not* medical advice. It does not diagnose, does not give treatment, dosing,
> or procedure instructions, does not give emergency or first-aid instructions, and
> is *not a substitute* for evaluation by a licensed clinician. Worked cases are
> illustrative teaching vignettes showing *how a clinician thinks*, not what any
> reader should do. For personal concerns, appropriate care comes from qualified
> local professionals; emergencies are handled through local emergency services.**

*Per-guide banner: educational reference on how the history and physical are structured as
information — not instructions for examining anyone, not a symptom checker, and not a
source of personal diagnosis. Finding-performance numbers are illustrative and attributed
where a real study is named.*

---

## The Big Picture: The Encounter Is an ETL Pipeline, Not a Recording

The novice model is "collect everything, then think." The expert model is a **filter that
runs while it collects**: a clinician forms candidate hypotheses within the first
sentences and gathers data *to discriminate among them*, compressing a messy narrative
into a few abstractions that index directly into stored disease knowledge.

```
THE ENCOUNTER AS AN INFORMATION PIPELINE  (this guide owns the transforms)
==========================================================================
  RAW SIGNAL                 EXTRACT + PROBE            STRUCTURE + INDEX
  the person's story          (hypothesis-driven)        (decision-ready)

  [ NARRATIVE ]  -------->  [ HISTORY ]  ----------->  [ PROBLEM REPRESENTATION ]
   words, worry,             targeted questions          one-sentence abstract:
   context, timeline         chosen to discriminate      "an <epi> patient with
        |                    among live hypotheses        <tempo> <system> <syndrome>"
        v                          |                             |
  [ BODY ]  ------------->  [ PHYSICAL EXAM ]  ------->          | uses SEMANTIC
   observable signs          targeted maneuvers with            v  QUALIFIERS
                             known signal properties     [ MATCH vs ILLNESS SCRIPTS ]
                                   |                       stored disease templates
                                   v                             |
                             [ SERIALIZE: note / oral present ]  v
                                                          feeds 02 (differential)
==========================================================================
  Read left-to-right: raw human signal in, abstracted + indexed representation out.
  The gather step is a QUERY PLANNER, not a full table scan; the output is a compressed
  key that illness scripts are looked up by. Collection and reasoning run together.
```

Three consequences drive the rest of the guide:

1. **Gathering is hypothesis-driven, not exhaustive** (Section 1). Which question or
   maneuver comes next is chosen by what would best separate the current hypotheses — a
   query plan, not a scan.
2. **The output is an abstraction, not a transcript** (Sections 3–4). Problem
   representation compresses the raw story into semantic qualifiers that map onto stored
   knowledge; the compression *is* the reasoning.
3. **Expert disease knowledge is pre-structured as illness scripts** (Section 5), so
   diagnosis becomes script *retrieval and matching*, not de-novo deduction.

**Bridge (software).** This is extract-transform-load with an optimizer. The history/exam
is extraction with a query planner (gather the field that most reduces uncertainty next);
problem representation is lossy compression to a canonical key; semantic qualifiers are the
schema that key is written in; illness scripts are the indexed records the key looks up;
and the note is serialization. A junior engineer dumps every log line; a senior one queries
for the field that discriminates the two live hypotheses. Same instinct.

---

## 1. Hypothesis-Driven Data Gathering

The single biggest novice/expert gap in the encounter is *when* hypotheses appear. Studies
of clinical reasoning (Elstein's work on hypothetico-deductive reasoning, 1978; and the
broader expertise literature) find that experienced clinicians generate a small set of
candidate hypotheses within the first minute — sometimes the first sentences — and then
gather data **to test and separate them**, not to fill a fixed template.

```
  NOVICE (exhaustive)                 EXPERT (hypothesis-driven)
  ------------------                  --------------------------
  ask every question on the form  ->  form 2-4 hypotheses early
  collect a large flat record     ->  ask the question that best DISCRIMINATES them
  reason only at the end          ->  update after each answer; re-plan the next question
  high volume, low signal density ->  low volume, high signal density
```

The mechanism is **iterative hypothesis testing**: each answer updates belief (the odds
math is guide 03) and re-plans the next probe. The chief concern and the first minutes of
the history of present illness carry the most information precisely because they are where
hypotheses are cheapest to generate and the query plan is most open.

**Data domains and what each is for** (structure, not a checklist to run on anyone):

| Domain | What it captures | Primary reasoning role |
|---|---|---|
| Chief concern | the person's own framing of why they came | sets the top of the differential; anchors the encounter |
| History of present illness (HPI) | the symptom's story over time | highest-yield discriminator; the tempo + character live here |
| Past medical/surgical history | prior diagnoses, operations | shifts priors; supplies predisposing conditions for scripts |
| Medications / allergies | current agents, reactions | drug-effect and interaction hypotheses (reasoning → 06) |
| Family history | heritable risk | adjusts pretest probability for genetic conditions |
| Social history | exposures, occupation, habits, context | risk modifiers; also the goals/values later guides need |
| Review of systems (ROS) | a structured sweep for missed problems | a safety net that catches what the focused HPI skipped |

The review of systems is the interesting one architecturally: it is a **broad low-prior
scan** deliberately run *after* the focused, high-prior HPI. It has the same property as
any broad scan (guide 03): it surfaces incidental positives with low predictive value, so
its findings are weighted lightly unless they connect to an active hypothesis.

**Symptom characterization frameworks** (mnemonics that structure *what* to elicit about a
symptom, e.g., OLDCARTS — Onset, Location, Duration, Character, Aggravating/Alleviating,
Radiation, Timing, Severity; or SOCRATES for pain). These are **information schemas**, not
scripts a reader should run: each axis is a feature dimension whose value helps separate
hypotheses. "Onset: sudden vs gradual" is a single high-information bit; "character:
pressure vs sharp" is another. The frameworks exist to make sure the discriminating
dimensions are actually captured.

---

## 2. The Physical Exam as Targeted Measurement

The physical exam is not a ritual sweep; each maneuver is a **measurement with signal
properties** — a sensitivity, a specificity, and therefore a likelihood ratio (guide 03).
The mature literature on this is the *Rational Clinical Examination* series (JAMA,
1990s–2000s; McGee's *Evidence-Based Physical Diagnosis*), which reports the LRs of
individual findings. That reframes the exam from "look for everything" to "perform the
maneuvers whose result would move a live hypothesis across a threshold."

```
  EACH EXAM MANEUVER = ONE MEASUREMENT
  -------------------------------------------------------------
  finding present  -> multiply pretest odds by LR+  (guide 03)
  finding absent   -> multiply pretest odds by LR-
  -------------------------------------------------------------
  A maneuver with LR near 1 is ritual, not measurement: it changes no belief.
  A maneuver is worth doing when its result can cross a decision threshold.
```

**Properties that make exam data different from lab data:**

| Property | Consequence for reasoning |
|---|---|
| **Operator-dependent** | inter-rater reliability varies by finding; a "soft" sign is a noisy sensor |
| **Bedside, immediate, cheap** | high value-of-information when it can redirect the workup before any test |
| **Often low sensitivity** | absence rarely rules out; many findings are SpPin (present rules in) not SnNout |
| **Gestalt vs discrete** | some signal is holistic pattern recognition, hard to decompose into named findings |

The architectural point: the exam is **not** a lower-tech substitute for tests; it is a
*different sensor class* with its own error model, best used to reshape the pretest
probability that later tests will update. This guide owns that framing; the *techniques*
themselves belong to clinical training, and are deliberately not described here.

---

## 3. Problem Representation — The Compression Step

The **problem representation (PR)** is the pivot of the entire encounter: a **one- or
two-sentence abstract summary** of the case that a clinician (and every downstream reader)
reasons from. It is a lossy, deliberate compression of the raw narrative into the terms
that index disease knowledge. A well-formed PR names, in abstract language:

```
  PROBLEM REPRESENTATION = a compressed, abstracted case key
  ----------------------------------------------------------------
   [ demographics/epidemiology ] + [ temporal pattern ] +
   [ clinical syndrome in abstract terms ]
  ----------------------------------------------------------------
  RAW (patient words):  "I'm 71. Over the last three months my skin and eyes went
                         yellow, my stools are pale, and I've lost weight, but it
                         doesn't hurt."
  PR (abstracted):      "An older adult with subacute, progressive, PAINLESS
                         obstructive-pattern jaundice and weight loss."
  ----------------------------------------------------------------
  The PR is what the differential (02) is generated from. Two clinicians who build the
  same PR will usually generate the same differential; a bad PR mis-indexes the lookup.
```

Why the PR matters so much:

- **It selects the differential.** The abstract terms in the PR are the *keys* that
  retrieve illness scripts (Section 5). "Painless" vs "painful," "subacute" vs "sudden"
  each swing the retrieved set. A concrete transcript cannot do this; only the abstraction
  can.
- **It is a shared artifact.** The oral presentation and the note's assessment line are the
  PR made portable (guide 07). A crisp PR is the highest-bandwidth handoff in medicine.
- **It exposes reasoning errors early.** If the PR is vague ("patient with abdominal
  symptoms"), the differential will be vague; a sharp PR is testable and falsifiable.

**Bridge (software).** The PR is a canonical cache key derived from noisy input. Just as a
good cache key normalizes away irrelevant variation (case, whitespace, ordering) while
preserving the identity-bearing features, a good PR strips the incidental narrative and
keeps the discriminating abstractions. A poorly normalized key causes cache misses; a poor
PR causes diagnostic misses.

---

## 4. Semantic Qualifiers — The Abstraction Layer

**Semantic qualifiers (SQs)** are the paired, abstract descriptors that translate a
patient's concrete words into the medical abstractions an illness script is written in.
They are the *schema* the problem representation is expressed in, and the transformation
from lay language to SQ is itself a diagnostic act.

```
  SEMANTIC QUALIFIER PAIRS  (the abstraction vocabulary)
  ----------------------------------------------------------------
  acute            <-> chronic
  sudden           <-> gradual
  constant         <-> intermittent / episodic
  localized        <-> diffuse
  proximal         <-> distal
  unilateral       <-> bilateral
  progressive      <-> stable / resolving
  painful          <-> painless
  exertional       <-> at-rest
  ----------------------------------------------------------------
  "It comes and goes" -> INTERMITTENT.  "It's spreading" -> PROGRESSIVE + DIFFUSE.
  The same word set maps every complaint onto a small abstract space that scripts index.
```

Two findings from the reasoning literature make SQs load-bearing:

1. **Expert PRs contain more semantic qualifiers than novice PRs.** Bordage's work on
   "semantic competence" (1990s) associated the density and correctness of SQs with
   diagnostic accuracy: experts recode the story into abstract oppositions; novices repeat
   concrete details. The recoding is where the diagnosis begins.
2. **The mapping is many-to-one and lossy on purpose.** Dozens of patient phrasings
   collapse onto "intermittent," which is exactly what lets a finite set of illness scripts
   cover an unbounded set of presentations.

**Bridge (software / ML).** SQs are feature engineering: the raw text is embedded into a
low-dimensional, discriminative feature space before classification. Just as a good feature
representation makes a downstream classifier's job easy (and a bad one makes it impossible),
a rich, accurate SQ encoding makes illness-script matching tractable, while a literal,
un-abstracted case description defeats it. The clinician is the encoder; the illness scripts
are the trained classifier.

---

## 5. Illness Scripts — How Disease Knowledge Is Stored

An **illness script** is the structured mental representation of a disease that experienced
clinicians store and match against. Rather than a flat list of facts, a script is a
schema with slots:

```
  ILLNESS SCRIPT (schema for one disease-as-experienced)
  ----------------------------------------------------------------
  PREDISPOSING CONDITIONS   who gets it, exposures, risk factors (the "epidemiology" slot)
  PATHOPHYSIOLOGY / FAULT   the mechanism, at the level a clinician needs (defers: disease/)
  CLINICAL CONSEQUENCES     the syndrome: time course, key features, discriminating signs
  ----------------------------------------------------------------
  Matching = fill the script's slots from the problem representation and score the fit.
  Experts carry thousands of scripts, richly cross-linked; novices carry textbook facts
  not yet compiled into scripts.
```

The theory (Schmidt & Boshuizen's "knowledge encapsulation," 1990s) is that learners begin
with detailed causal/pathophysiologic networks and, with clinical experience, **encapsulate**
that knowledge into compact scripts indexed by presentation. This explains three observed
things:

- **Experts are faster *and* more accurate**, not one at the expense of the other: script
  retrieval is pattern matching, cheaper than deducing from mechanism each time.
- **Experts can still "unpack" a script** to reason mechanistically when a case does not fit
  — the causal network is encapsulated, not lost. This unpacking is the deliberate System-2
  move of guide 02.
- **Scripts include a "prototype" and remembered "instances."** A new case is matched both
  to the abstract prototype and to specific past patients ("exemplars") — dual storage that
  makes reasoning robust but also seeds bias (guide 02: the vivid recent case distorts
  availability).

**The encounter's job, restated:** build a problem representation, in semantic qualifiers,
rich enough to retrieve the right small set of illness scripts. Everything in Sections 1–4
serves that retrieval.

---

## Fully Worked Case — Building a Representation (illustrative, fictional)

All details below are invented to show the *information transforms*; nothing here is a
diagnosis, and no reader should map it to themselves. The clinical specifics are abstract
(the disease catalog lives in `disease/`).

**Raw narrative (input).** A fictional patient says: *"I'm 68. For about two months I get
this tight pressure across my chest when I walk up the hill to my house. It goes away if I
stop and rest for a few minutes. It's never happened just sitting around. It's slowly
happening on smaller hills than before."*

**Step 1 — hypothesis-driven gathering (Section 1).** The clinician forms a small
hypothesis set from the first sentence (exertional chest pressure → cardiac-ischemic,
musculoskeletal, and a couple of others) and asks the questions that *discriminate*: relation
to exertion vs rest, what relieves it, trajectory over time, associated features. Each answer
re-plans the next question rather than running a fixed form.

**Step 2 — semantic-qualifier encoding (Section 4).**

| Patient words | Semantic qualifier |
|---|---|
| "when I walk up the hill" / "never just sitting" | **exertional**, not at-rest |
| "goes away if I stop and rest" | **relieved by rest**, **intermittent** |
| "for about two months" | **subacute-to-chronic** |
| "smaller hills than before" | **progressive** |
| "tight pressure across my chest" | **pressure-quality**, **central** |

**Step 3 — problem representation (Section 3).** The abstractions compose into a PR:
*"An older adult with a two-month history of progressive, exertional, rest-relieved central
chest pressure."* This is the compressed key — not the transcript.

**Step 4 — illness-script retrieval (Section 5).** The PR's keys (**exertional +
rest-relieved + progressive**) retrieve a small set of scripts whose "clinical consequences"
slot matches that pattern, and rank them; scripts that require *at-rest* or *sudden* onset
score poorly and drop. The PR has done the indexing.

**Step 5 — targeted exam as measurement (Section 2).** The clinician then performs the
maneuvers whose findings carry the highest LRs for the retrieved hypotheses — not a
head-to-toe sweep — to reshape the pretest probability that any subsequent test (guide 03)
will update.

**What the encounter produced.** Not a diagnosis — a **decision-ready representation**: a
sharp PR, a ranked script set (the seed of guide 02's differential), and a pretest
probability positioned for the testing logic of guide 03. The reasoning happened *in the
compression*, before any test was ordered.

---

## Reader Tasks (answerable from this guide)

1. **Encode a narrative into semantic qualifiers and a PR.** Given a fictional complaint,
   map the lay phrases to SQ pairs and compose a one-sentence problem representation, then
   explain why the abstraction (not the transcript) is what drives the differential.
   (Sections 3–4.)
2. **Explain hypothesis-driven vs exhaustive gathering.** Contrast the novice "run the whole
   form" approach with the expert "ask the discriminating question next," and connect the
   choice to value of information from guide 03. (Section 1.)
3. **Weigh an exam finding as a measurement.** Given a finding with a stated LR+, describe
   how it reshapes a pretest probability and why a finding with LR ≈ 1 is ritual rather than
   measurement. (Section 2, links to 03.)
4. **Diagnose a weak problem representation.** Given a vague PR ("patient with belly pain"),
   explain what information it fails to carry (no tempo, no qualifiers, no epidemiology) and
   how that degrades every downstream step. (Section 3.)
5. **Explain why experts are faster *and* more accurate.** Use illness scripts and knowledge
   encapsulation to resolve the apparent paradox, and note where the same script storage
   seeds cognitive bias (forward reference to 02). (Section 5.)

---

## Decision Cheat Sheet

| Situation | What the skilled encounter does | Why (this guide) |
|---|---|---|
| The story begins | forms 2–4 hypotheses early, then gathers to **discriminate** them | gathering is a query plan, not a scan (§1) |
| A symptom needs characterizing | captures the **discriminating dimensions** (onset, tempo, character, relievers) | each axis is a high-information bit (§1) |
| Choosing exam maneuvers | performs the ones whose finding carries a **useful LR** for a live hypothesis | the exam is measurement, not ritual (§2, §03) |
| Summarizing the case | compresses to a **problem representation** in abstract terms | the PR is the key the differential is built from (§3) |
| Translating patient words | recodes them into **semantic qualifiers** (acute/chronic, painless/painful…) | SQs are the schema scripts are indexed by (§4) |
| Reasoning toward disease | matches the PR against stored **illness scripts** and scores fit | expert knowledge is pre-structured as scripts (§5) |
| Handing the case off | transmits the **PR + ranked scripts**, not the raw transcript | the abstraction is the high-bandwidth artifact (§3, §07) |

---

## Common Confusion Points

**"The history is just asking questions; the exam is just looking."** No — both are
*targeted measurement under a hypothesis*. The skilled version chooses each question and
maneuver to separate live hypotheses, and weights findings by their signal properties
(LRs). A flat, exhaustive sweep collects volume, not information.

**"Problem representation is just a summary."** It is a *lossy, deliberate abstraction*,
not a précis. Its job is to strip incidental narrative and keep the semantic qualifiers
that index illness scripts. A transcript summarizes; a PR *reasons* by choosing which
abstractions to preserve.

**"Semantic qualifiers are jargon for describing symptoms."** They are the low-dimensional
feature space that makes matching tractable. The recoding from "it comes and goes" to
"intermittent" is a diagnostic step: it is where the unbounded space of patient phrasings
collapses onto the finite space of stored scripts.

**"Experts must reason more slowly and carefully than novices."** Usually the reverse for
familiar presentations: script retrieval (System 1, guide 02) is fast *and* accurate.
Experts slow to mechanistic reasoning (System 2) precisely when a case does *not* fit a
script — the deliberate unpacking, not the default mode.

**"This guide will teach me to take a history or do an exam."** It will not, by design. It
owns the *information architecture* — what signal each step carries and how the encounter is
structured for reasoning. Performing a history or exam on a real person is a trained
clinical skill and is out of scope; the anatomy behind a finding lives in `human-biology/`
and the diseases behind a script live in `disease/`.
