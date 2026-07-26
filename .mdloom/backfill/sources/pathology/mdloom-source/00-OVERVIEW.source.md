---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:pathology:overview
kind: guide
module: pathology
section: pathology
title: Pathology - Overview
status: source-custody
source_custody: partial
current_path: pathology/00-OVERVIEW.md
canonical_path: pathology/00-OVERVIEW.md
backsource_ids: [mdloom-backfill:pathology:00-overview]
concepts: [discipline-map, mechanism-result-diagnosis-spine, ownership-boundaries, non-advice-contract, reading-order]
root_concepts: [pathology]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Pathology — Overview

**This guide owns** the *map of the discipline*: the two orthogonal splits that organize
pathology (**anatomic vs clinical** pathology, and **general vs systemic** pathology), the
**mechanism → result → diagnosis spine** that this module is built around, the
**ownership/boundary table** that keeps `pathology/` from duplicating its neighbors, the
module-wide **four-pillar non-advice / non-procedure contract**, the reading order, and the
recurring software/systems mental models the mechanism guides reuse. **It builds on**
`human-biology/` (normal structure and function — the baseline a lesion departs from) and
`biology/`/`biochemistry/` (the cellular machinery that fails). **It is the front door** to
the twelve-guide module: the seven mechanism guides (`01`–`07`), the laboratory-result and
anatomic-technique guides (`08`, `09`), the diagnosis-and-reporting guide (`10`), and the
laboratory-as-a-quality-system guide (`11`).

**It explicitly defers** — and names by reference, never re-deriving — the following:

- **disease entities, catalogs, and natural history** to `disease/`; this module uses
  lesions only as *illustrations of a mechanism or a method*, never as a checklist of
  conditions;
- **the diagnostics/reference-range catalog and imaging physics** to
  `medicine/10-DIAGNOSTICS-IMAGING`, and **Bayesian belief-updating** (pretest → posttest,
  likelihood ratios, thresholds, the decision to act) to
  `clinical-medicine/03-DIAGNOSTIC-TEST-INTERPRETATION`;
- **immune-cell biology** to `immunology/`, **gene/pathway mechanism** to `genomics/` and
  `biochemistry/`, **organism biology/taxonomy** to `microbiology/` and `virology/`, and
  **normal physiology** to `human-biology/`;
- **statute, precedent, and forensic/legal (cause- and manner-of-death) determination** to
  `law/` and `criminology/` — out of scope here.

> **This module is an educational reference about *how pathology and the laboratory produce
> and reason about findings* — the mechanism-to-diagnosis architecture of the discipline. It
> is *not* medical advice. It does *not* interpret any reader's own results, images, slides,
> or lesions, does *not* diagnose, does *not* give treatment, dosing, or emergency
> instructions, and is *not a substitute* for evaluation by a licensed clinician or an
> accredited laboratory. It gives *no specimen-collection or laboratory-operating
> instructions* and *no forensic or legal determinations*. All cases are fictional teaching
> vignettes, and every numeric value is an illustrative teaching figure, attributed and
> dated where it names a real standard — never a clinical cutoff.**

*Per-guide banner: this is the module map and its non-advice/non-procedure contract — never
self-diagnosis, never personal-result or personal-slide interpretation, never a bench or
collection procedure, never forensic/legal advice. Disease entities are named only to
illustrate a mechanism; the catalog is `disease/`.*

---

## The Big Picture: A Causal Chain From Injury to Signed Diagnosis

Pathology is the study of **disease as a departure from normal structure and function**, and
of **how that departure is made observable, measured, and named**. The novice mental model
is "pathology = looking at slides." The expert model is a **causal pipeline**: an injurious
stimulus perturbs a cell, the perturbation propagates up through tissue as a *lesion*, the
lesion is sampled and turned into a *result* or an *image*, and a reasoner turns the observed
pattern into a *signed diagnosis* that a clinician then acts on. This module owns the whole
middle of that pipeline — the *why* of the lesion and the *how* of the finding — and hands
the *what to do* to `clinical-medicine/`.

```
THE MECHANISM -> RESULT -> DIAGNOSIS SPINE  (this module owns the shaded middle)
================================================================================
  normal structure/function            <-- human-biology/ (the baseline)
        |
        |  injurious stimulus (hypoxia, toxin, organism, immune, genetic, physical)
        v
  ===== MECHANISM ==========================================  guides 01-07
  [ CELL ]  injury / adaptation / death   ------------------  01
  [ TISSUE ] inflammation & repair · hemodynamics · immune  02 · 03 · 04
  [ GROWTH ] neoplasia · genetic/developmental · environmental 05 · 06 · 07
        |   "why does the lesion look and behave the way it does?"
        v
  ===== FINDING ============================================  guides 08-09
  [ RESULT ]  a bounded laboratory number/flag  -----------  08
  [ SLIDE ]   a fixed, stained, sampled substrate ---------  09
        |   "how is the observation manufactured, and how far to trust it?"
        v
  ===== DIAGNOSIS ==========================================  guide 10
  [ REASON ]  pattern -> differential -> ancillary evidence
        |     -> calibrated certainty -> classification -> REPORT
        v
  signed diagnosis  ---------------------------------------> clinical-medicine/
        |   "belief update + action live downstream, NOT here"
  ===== SYSTEM =============================================  guide 11
  [ QUALITY ] the diagnostic laboratory as a quality system: QC/QA/EQA,
              error taxonomy across the whole process, governance as concept
```

Two facts from this diagram govern the whole module. First, **the transferable content is
the organ-agnostic mechanism and the organ-agnostic method**, not a per-organ disease list:
how a cell is injured, how tissue inflames and repairs, how a neoplasm behaves, and how a
morphologic pattern becomes a calibrated report transfer across every organ. Second, **the
module stops at the signed finding**; it never updates a clinician's belief or recommends an
action. Keeping *produce-the-finding* separate from *decide-what-to-do* is the safety spine
of the whole design.

**Bridge — the compiler pipeline.** The spine maps cleanly onto a toolchain a senior
engineer already knows: `human-biology/` is the *source language* (the intended behavior);
the mechanism guides are *how the program goes wrong at runtime*; `08`/`09` are the
*instrumentation and sampling* that make a failure observable; `10` is the *diagnosis pass*
that turns a stack trace into a typed, signed report; and `clinical-medicine/` is the
*operator* who reads the report and decides to roll back. This module owns the failure
model, the instrumentation, and the diagnosis pass — not the operational decision.

---

## 1. The Two Orthogonal Axes That Organize the Discipline

Pathology has **two independent top-level splits**. They are orthogonal — any real diagnostic
question sits somewhere on both axes at once — and confusing them is the first source of
disorientation.

```
AXIS A: WHAT SUBSTRATE?              AXIS B: HOW GENERAL?
========================            =====================
  ANATOMIC PATHOLOGY                  GENERAL PATHOLOGY
  tissue & cells; morphology            mechanisms that recur EVERYWHERE
  (biopsy, cytology, autopsy)           (injury, inflammation, neoplasia)
        |                                     |
        | vs                                  | vs
        v                                     v
  CLINICAL PATHOLOGY                  SYSTEMIC PATHOLOGY
  laboratory testing of fluids          organ-specific disease
  (chemistry, hematology, micro,        (this-organ-this-entity)
   molecular, transfusion)              -> DEFERRED to disease/
```

**Axis A — anatomic vs clinical pathology** distinguishes the *substrate* the discipline
reasons over. **Anatomic pathology** works from **tissue and cells** — the morphology of a
biopsy, a resection, a cytology preparation, or an autopsy — and its product is a
*diagnosis from a pattern* (owned here by `09` technique and `10` reasoning).
**Clinical pathology** (laboratory medicine) works from **fluids and analytes** — chemistry,
hematology, coagulation, microbiology, molecular, transfusion — and its product is a
*bounded result* (owned here by `08`, with the quality system in `11`).

**Axis B — general vs systemic pathology** distinguishes *how organ-specific* the knowledge
is. **General pathology** is the set of **mechanisms that recur in every organ**: a cell is
injured the same way in heart and kidney; inflammation runs the same program in lung and
liver; a neoplasm obeys the same growth logic in colon and breast. **Systemic pathology** is
the **organ-specific catalog** — *this* entity in *this* organ — and it is **deferred to
`disease/`** by design (writing it here would triplicate `disease/` + `human-biology/` +
`clinical-medicine/`).

This module deliberately owns **general pathology + the diagnostic/laboratory apparatus** and
teaches the diagnostic method as a *reusable procedure*, exactly as chemistry organizes "by
problem, not technique" and clinical-medicine organizes "by reusable reasoning, not per-organ
specialty." When an organ or entity appears in guides `01`–`10`, it appears **only to
illustrate a mechanism or a method**, with the entity itself owned by `disease/`.

| Axis | Left pole | Right pole | This module owns | Deferred |
|---|---|---|---|---|
| A (substrate) | Anatomic (tissue/cells) | Clinical (fluids/analytes) | Both — `09`/`10` and `08`/`11` | — |
| B (generality) | General (recurring mechanism) | Systemic (organ entity) | General (`01`–`07`) + method (`10`) | Systemic → `disease/` |

---

## 2. What the Module Owns vs Defers — the Boundary Table

Every guide names its neighbors by reference and re-derives none of them. The single most
important boundary is the **three-way lab-interpretation split**, ratified with this module.

```
THREE-WAY LAB-INTERPRETATION SPLIT
==================================
  pathology/08            medicine/10                 clinical-medicine/03
  (this module)           (the catalog)               (the decision)
  ------------            -----------------           --------------------
  HOW the result is       WHICH test it is,           HOW a clinician turns
  generated and how       its panel and its           the released result into
  far to trust it   --->  reference band       --->   an updated belief and
  (number + uncertainty                               an action
   + flags)               (name + interval)           (prior x LR -> posterior)
```

| Defers to | For |
|---|---|
| `disease/` | Disease entities, catalogs, natural history, and entity-specific grading/staging systems |
| `medicine/10-DIAGNOSTICS-IMAGING` | The test **catalog**, reference intervals/ranges, panel membership, analyte time-courses, imaging **physics** |
| `clinical-medicine/03` | **Bayesian belief updating** — pretest/posttest probability, likelihood ratios, thresholds, action |
| `clinical-medicine/02` | The *clinical* differential and its cognitive-bias framing (borrowed by reference in `10`) |
| `human-biology/` | Normal structure and physiology — the baseline a lesion departs from |
| `immunology/` | Immune-cell biology and signaling (this module owns hypersensitivity *as a tissue lesion*, `04`) |
| `microbiology/`, `virology/` | Organism biology/taxonomy (this module owns *how a micro/molecular result is generated*, `08`) |
| `genomics/`, `biochemistry/` | Gene/pathway mechanism (this module owns the *lesion*, not the normal pathway) |
| `chemistry/04-ANALYTICAL-QUANTITATIVE` | The general analytical formalism — calibration, LOD/LOQ, method validation (`08` applies it to biological matrices) |
| `public-health/`, `statistics-applied/` | Population **screening programs** and study-design methods |
| `law/`, `criminology/` | Statute/precedent; forensic/legal cause- and manner-of-death determination — **out of scope** |

The rule of thumb: **`pathology/` owns the *lesion*, the *result*, and the *diagnosis
method*; it never owns the *entity*, the *catalog*, the *belief update*, or the *action*.**

---

## 3. The Four-Pillar Non-Advice / Non-Procedure Contract

This is the safety contract that heads the module and is embedded (as a banner) in every
guide. Four pillars, each a hard line the content does not cross.

```
FOUR-PILLAR CONTRACT  (every guide, every case)
===============================================
  [1] NO self-diagnosis / no personal-result or personal-slide interpretation
      -> explains how the lab and the pathologist reason IN GENERAL;
         never what a reader's own result/image/lesion means. Cases are fictional.
  [2] NO specimen-collection or laboratory-operating instructions
      -> technique is described as PRINCIPLE and CONSTRAINT (guide 09),
         never as a runnable bench SOP (no reagents/times/temperatures/steps).
  [3] NO forensic/legal advice
      -> autopsy/forensic content is conceptual; no cause-of-death,
         manner-of-death, or legal determination.
  [4] THIRD-PERSON descriptive voice; illustrative, dated numbers
      -> no second-person imperatives; every threshold is labeled
         illustrative and, where it names a real standard, attributed & dated.
```

The mechanism guides (`01`–`07`) obey the same contract: they explain *why a lesion forms and
what it means mechanistically in general*, they name disease entities only as illustrations
(the entity is `disease/`), and they present every grade, interval, or classification as an
**attributed, dated, evolving framework** — never a frozen universal cutoff. Classification
systems (WHO tumor classifications, CAP protocols, AJCC/UICC staging, ISO/CLSI laboratory
standards) are periodically revised by expert bodies; this module teaches the *reasoning* and
points to where current guidance lives, rather than memorializing one edition's numbers.

---

## 4. The Guide Map and Reading Order

Twelve guides: an overview plus eleven numbered guides, in three bands.

| # | Guide | Band | Uniquely owns |
|---|---|---|---|
| 00 | `00-OVERVIEW` | map | This map, the spine, the boundary table, the four-pillar contract |
| 01 | `01-CELL-INJURY-ADAPTATION-AND-DEATH` | mechanism | Reversible/irreversible injury; adaptations; necrosis vs apoptosis; accumulations |
| 02 | `02-INFLAMMATION-AND-TISSUE-REPAIR` | mechanism | Acute/chronic inflammation as a program; mediators; granulomas; repair/fibrosis |
| 03 | `03-HEMODYNAMIC-DISORDERS-THROMBOSIS-AND-SHOCK` | mechanism | Edema/congestion; hemostasis; Virchow's triad; thrombosis/embolism/infarction; shock |
| 04 | `04-IMMUNOPATHOLOGY-AND-TISSUE-INJURY` | mechanism | Hypersensitivity I–IV as tissue-injury; autoimmunity; rejection; immunodeficiency-as-lesion |
| 05 | `05-NEOPLASIA-CARCINOGENESIS-AND-TUMOR-BIOLOGY` | mechanism | Hallmarks; benign/malignant; anaplasia; invasion/metastasis; carcinogenesis; nomenclature principles |
| 06 | `06-GENETIC-DEVELOPMENTAL-AND-METABOLIC-PATHOLOGY` | mechanism | Inherited-disease pathology; malformation mechanisms; storage/inborn errors as lesions |
| 07 | `07-ENVIRONMENTAL-NUTRITIONAL-AND-TOXIC-INJURY` | mechanism | Physical/chemical/toxic injury; deficiency/overload lesions; exposure pathology |
| 08 | `08-LABORATORY-MEDICINE` | finding | How a laboratory result is generated and bounded (the three-way split's anchor) |
| 09 | `09-ANATOMIC-PATHOLOGY-TECHNIQUE` | finding | Gross-to-glass technique as principle/constraint (no runnable SOPs) |
| 10 | `10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING` | diagnosis | Morphology-to-diagnosis reasoning and the report as an interface |
| 11 | `11-QUALITY-ERROR-AND-THE-DIAGNOSTIC-LABORATORY-AS-SYSTEM` | system | The diagnostic service as a quality system |

**Reading order.** Three entry points depending on what a reader wants:

- **The mechanism path** (`01` → `02` → `03` → `04` → `05` → `06` → `07`): read straight
  through for general pathology. `01` (how a single cell fails) is the foundation the rest
  build on; `02` (the tissue-level response) and `03` (the vascular substrate) come next;
  `04`–`07` are the four great *causes* of injury (immune, neoplastic, genetic, environmental).
- **The laboratory path** (`08` → `11`): read for *how a result is made and how the lab is
  governed as a system*. `08` owns one result; `11` owns the cross-process program.
- **The diagnosis path** (`09` → `10`): read for *how a slide is made and how a pattern
  becomes a signed report*. `10` is where the whole module converges.

A first-time reader who wants the shortest complete arc reads `00` → `01` → `05` → `08` →
`10`: the spine, the founding mechanism, the growth mechanism, the result, and the diagnosis.

---

## 5. The Recurring Shape of a Mechanism Guide

Every mechanism guide (`01`–`07`) is built on the same three-layer formalism, so the module
reads like one book rather than seven essays. Recognizing the shape makes each guide faster
to navigate.

```
THE THREE-LAYER FORMALISM  (repeated in every mechanism guide)
==============================================================
  MOLECULAR   the switch that flips: ATP, ROS, a caspase cascade,
     |        a mutated oncoprotein, a complement fragment
     v
  CELLULAR    what the cell does in response: swells, adapts, dies,
     |        proliferates, accumulates a substance
     v
  TISSUE      what becomes visible as a LESION: a pattern of necrosis,
     |        an infiltrate, a scar, a mass, a deposit
     v
  (-> 09/10)  how that lesion is sampled and turned into a diagnosis
```

The guides move **top-down** — molecular switch → cellular response → tissue lesion → the
downstream finding — and each closes with worked fictional cases, a Decision Cheat Sheet, and
Common Confusion Points. This is deliberately the same "start with the landscape, layer
downward, end with a decision table" contract the rest of MAXIM uses.

**Bridge — layers of a stack trace.** The molecular switch is the *faulting instruction*; the
cellular response is the *thread state* after the fault; the tissue lesion is the
*application-level symptom* an operator sees; and `10` is the *post-mortem analysis* that
attributes the symptom to a root cause. A pathology guide reads a lesion the way an SRE reads
an incident: symptom → mechanism → root cause, never symptom → action directly.

## 6. A Worked Navigation Case and Solved Reader Tasks

The overview's job is **routing**: given a scenario, which guide owns each question? The
following fictional case walks one specimen down the mechanism → result → diagnosis spine and
names the owner of every step. Read it as a router, never as a diagnosis.

**A worked navigation case (fictional).** A firm mass is excised from a fictional patient who
also has an unrelated flagged blood test. Trace the threads down the spine:

```
NAVIGATING ONE FICTIONAL SPECIMEN DOWN THE SPINE
================================================
  THREAD      the question it asks                     owner guide(s)
  ------      --------------------                     --------------
  MECHANISM   why is there a mass; why did tissue      05 · 01 · 02
              scar instead of regenerate?
  FINDING     how was the blood flag made; how did     08 (result) ·
              the mass become a slide?                 09 (slide)
  DIAGNOSIS   what does the pattern mean, as a          10
              signed report?
  SYSTEM      was the whole process in control; who     11
              owns a cross-step error?
  ACTION      what does the patient have; what         NOT here ->
              should be done?                          disease/ · clinical-medicine/
```

- The **mechanism** thread — *why is there a mass, and why did injured tissue scar instead of
  regenerate?* — routes to the mechanism guides: neoplastic growth logic is `05`, cell
  injury/adaptation/death is `01`, and inflammation-and-repair is `02`. Rule: a *why does the
  lesion behave this way* question lands in `01`–`07`.
- The **finding** thread — *how was the blood flag manufactured and bounded, and how was the mass
  turned into a stained section?* — routes to `08` (the bounded laboratory result with its
  uncertainty and flags) and `09` (the fixed, stained, sampled substrate and where it loses
  information). Rule: a *how is the observation made, and how far do I trust it* question lands in
  `08`/`09`.
- The **diagnosis** thread — *how does the observed pattern become a signed, classified report?* —
  routes to `10` (pattern → differential → ancillary evidence → calibrated certainty →
  classification → report). Rule: a *what does the pattern mean, as a report* question lands in
  `10`.
- The **system** thread — *was the end-to-end process in control, and who owns an error that spans
  result and slide?* — routes to `11`. Rule: a *cross-process quality/error/governance* question
  lands in `11`.
- The **action** thread — *what does the patient have, and what should be done?* — **leaves the
  module**: the entity catalog is `disease/` and the decision is `clinical-medicine/`. This is the
  four-pillar non-advice contract of `§3` in action.

### Solved Reader Tasks (answerable from this overview)

Each task is a **routing** exercise — where a question lives — not a personal-result
interpretation.

**Task 1 — "A slide shows a scar. Which guide explains *why* it scarred, and which explains *how*
the scar became a slide?"**
Two different threads on the spine. *Why* a tissue repairs by scar rather than regeneration is a
**mechanism** question owned by `02` (inflammation and tissue repair). *How* the tissue became a
fixed, stained section is a **finding-manufacture** question owned by `09`. The rule: separate
*why the lesion is what it is* (`01`–`07`) from *how the observation was made* (`08`/`09`).

**Task 2 — "A result and a slide disagree. Where is that reconciled, and where is it *not*?"**
Reconciling a pattern against ancillary evidence into one **signed interpretation** is the
diagnosis pass owned by `10`. Whether the *process* that produced both was in control — and who
owns a discordance spanning result and slide — is the **system** question owned by `11`. What the
reconciled diagnosis means for the patient is downstream in `clinical-medicine/`.

**Task 3 — "Someone asks, 'what antibiotic should this patient get?' Is that a pathology
question?"**
No. The module owns *produce-the-finding*, never *decide-what-to-do*. Naming the organism or
lesion mechanism is here (`01`–`07`); manufacturing and bounding the identifying result is `08`;
the signed report is `10`; but the therapeutic decision is `clinical-medicine/`, and the disease
catalog is `disease/`. That boundary is the four-pillar contract of `§3`.

**Task 4 — "Two guides both seem to own 'error.' How do `08` and `11` divide it?"**
`08` owns the uncertainty and failure modes of **one laboratory result** (its measurand, bias,
interference, flags). `11` owns the **cross-process quality system** — QC/QA/EQA and an error
taxonomy spanning the whole pipeline from accession to signed report. The cheat-sheet rule: `08`
owns one result; `11` owns the program that governs all of them.

**Task 5 — "Where does 'what the pattern means' stop being this module's job?"**
At the **signed finding**. `10` turns a pattern into a calibrated, classified, reported
interpretation and *stops*. The belief update in a clinician's head and the resulting action are
`clinical-medicine/` by design — the safety spine that keeps *produce-the-finding* separate from
*decide-what-to-do*.

---

## Decision Cheat Sheet

| Topic to understand | Start with | Key caveat |
|---|---|---|
| Why a single cell dies or adapts | `01-CELL-INJURY` | Reversible and irreversible injury sit on a continuum; the "point of no return" is a mechanism, not a clock |
| Why tissue reddens, swells, or scars | `02-INFLAMMATION-AND-REPAIR` | Inflammation is a *program*, not a synonym for infection; repair can restore or scar |
| Why a clot, embolus, or shock forms | `03-HEMODYNAMIC-DISORDERS` | Hemostasis is protective; thrombosis is the same machinery in the wrong place/time |
| How the immune system injures its own tissue | `04-IMMUNOPATHOLOGY` | Hypersensitivity here is a *tissue-injury mechanism*; immune-cell biology is `immunology/` |
| Why a growth is benign or malignant | `05-NEOPLASIA` | Malignancy = capacity for destructive invasion + aggressive/metastatic spread, not size/speed; basement-membrane breach is the *epithelial* criterion (leukemias/lymphomas qualify without it) |
| How an inherited or metabolic defect becomes a lesion | `06-GENETIC-DEVELOPMENTAL-METABOLIC` | The gene mechanism is `genomics/`; this module owns the tissue consequence |
| How the environment, nutrition, or toxins injure tissue | `07-ENVIRONMENTAL-NUTRITIONAL-TOXIC` | Dose, duration, and host factors shape the lesion; exposure is not destiny |
| How a laboratory number is manufactured and bounded | `08-LABORATORY-MEDICINE` | The result carries uncertainty and flags; the catalog is `medicine/10`, the decision is `clinical-medicine/03` |
| How a slide is made and where it loses information | `09-ANATOMIC-PATHOLOGY-TECHNIQUE` | Technique is principle/constraint, never a runnable procedure |
| How a pattern becomes a signed diagnosis and report | `10-DIAGNOSIS-PATTERN-RECOGNITION` | The report is an interface; belief update and action are downstream |
| How the diagnostic laboratory is governed as a system | `11-QUALITY-ERROR-AND-THE-SYSTEM` | `08` owns one result; `11` owns the cross-process program |
| What condition a person actually has, and what to do | `disease/` + `clinical-medicine/` | This module produces the finding; it never diagnoses a person or recommends action |

---

## Common Confusion Points

**"Pathology is just looking at slides."**
Anatomic pathology (slides) is one axis; clinical pathology (laboratory testing of fluids) is
the other, and both are equal members of the discipline. This module owns both substrates,
plus the reasoning that turns either into a diagnosis and the quality system that governs
them.

**General pathology vs systemic pathology.**
General pathology is the *organ-agnostic mechanism* (how any cell is injured, how any tissue
inflames). Systemic pathology is the *organ-specific entity catalog* — and it lives in
`disease/`, not here. When this module names an organ or entity, it is illustrating a
mechanism, not cataloging a disease.

**Lesion vs disease.**
A lesion is a *structural or functional abnormality* — the observable departure from normal.
A disease is a *named entity with a natural history*. This module reasons about lesions and
mechanisms; `disease/` owns the entities. "Granulomatous inflammation" is a lesion/pattern;
"sarcoidosis" is an entity.

**Result vs interpretation.**
A released laboratory result (a number plus its uncertainty and flags) is not the same as an
interpreted result. `08` stops at the released result; `10` stops at the signed diagnosis;
neither updates a clinician's belief or chooses an action. That is `clinical-medicine/03`.

**Grade vs stage (previewed here, owned by `05`/`10`).**
Grade is *how abnormal the cells look* (differentiation); stage is *how far the tumor has
spread* (anatomic extent). They are orthogonal axes measured separately, and the specific
grading/staging systems are attributed, dated, and deferred to `disease/`.

---

## Resource, Geographic, and Bias Caveats

- **Classification systems and reference intervals are population-, era-, and
  jurisdiction-specific.** WHO tumor classifications, AJCC/UICC staging, CAP protocols, and
  ISO/CLSI laboratory standards are revised on cycles; a healthy reference population's
  interval shifts with age, sex, ancestry, and altitude. This module teaches the reasoning
  and dates/attributes every named framework; it never universalizes one edition or one
  population.
- **The diagnostic apparatus assumes a resourced setting where the toolbox is fullest.**
  Broad immunohistochemistry panels, molecular/next-generation sequencing, on-call frozen
  section, mass-spectrometry organism identification, and subspecialty sign-out are
  concentrated in resourced laboratories; district and low-resource settings reason
  morphology- and microscopy-forward, with referral, send-out, and telepathology. The
  *reasoning* transfers; the *toolbox* does not. Each affected guide carries a resource-tier
  section.
- **Morphologic and laboratory judgment carry intrinsic, bounded variability.** Interobserver
  variability is real (e.g., grading reproducibility is measured by kappa); consensus,
  second opinion, and referral exist precisely because judgment is not perfectly
  reproducible. The evidence base skews toward certain populations and platforms.
- **Forensic and autopsy legal determination is out of scope.** Where autopsy or forensic
  material is mentioned, it is conceptual; no cause-of-death, manner-of-death, or legal
  conclusion is offered anywhere in this module.
