---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "11-QUALITY-ERROR-AND-THE-DIAGNOSTIC-LABORATORY-AS-SYSTEM.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:pathology:quality-error-and-the-diagnostic-laboratory-as-system
kind: guide
module: pathology
section: pathology
title: Quality, Error, and the Diagnostic Laboratory as a System
status: source-custody
source_custody: partial
current_path: pathology/11-QUALITY-ERROR-AND-THE-DIAGNOSTIC-LABORATORY-AS-SYSTEM.md
canonical_path: pathology/11-QUALITY-ERROR-AND-THE-DIAGNOSTIC-LABORATORY-AS-SYSTEM.md
backsource_ids: [proof-backfill:pathology:11-quality-error-and-the-diagnostic-laboratory-as-system]
concepts: [total-testing-process-governance, quality-control, quality-assurance, external-quality-assessment, accreditation-and-competence, document-and-change-control, validation-verification-governance, error-taxonomy, incident-and-amendment-loops, turnaround-and-traceability, laboratory-resilience]
root_concepts: [diagnostic-laboratory-as-system]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Quality, Error, and the Diagnostic Laboratory as a System

**This guide owns** the *diagnostic service as a system* — the cross-process quality,
error, and governance layer that sits above any single result or diagnosis: quality
control (QC), quality assurance (QA), and external quality assessment (EQA) as a layered
control program across the **total testing process**; accreditation and competence *as
concepts*; document and change control; the **governance** of method validation and
verification (not their statistics); the cross-process **error taxonomy** (pre-analytic,
analytic, post-analytic, and the pre-pre-/post-post- ends of the brain-to-brain loop);
incident, critical-communication, and amendment feedback loops; turnaround time and
end-to-end traceability; the autopsy and audit *boundary*; and the resilience of the
laboratory as a system. **It builds on** `08-LABORATORY-MEDICINE` (which owns how a single
result is generated and bounded), `10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING` (which
owns the diagnosis and the report), and `09-ANATOMIC-PATHOLOGY-TECHNIQUE` (which owns the
substrate) — this guide governs the *processes* those three run inside.

**It explicitly defers** four things it must never absorb:

- the **per-result metrology derivations** — imprecision, bias, calculated vs allowable
  total error, measurement uncertainty, sigma, reference-change value, detection limits — to
  `08-LABORATORY-MEDICINE §2–§6`. This guide uses those metrics; it does **not** re-derive
  them and never contradicts them;
- the **generation of a single result or diagnosis** — how an assay/stain produces a
  signal (`08`), how a slide substrate is made (`09`), and how morphology becomes a signed
  report (`10`). This guide owns the *cross-process system*, not the individual product;
- the **general clinical-system-safety science and the clinical care system** — the
  Swiss-cheese/latent-error model, just culture, root-cause analysis and high-reliability
  theory, Donabedian structure–process–outcome, PDSA/Model for Improvement, and the
  clinical diagnostic-safety loop — to `clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW`.
  This guide applies those frameworks to the *laboratory* by reference, and names them
  dated/attributed rather than re-teaching them;
- **accreditation "how-to," jurisdiction-specific compliance steps, and any forensic/legal
  (cause-/manner-of-death) determination** — governance is described only *as concept*, and
  the autopsy appears only as a quality-audit *boundary*, never as a legal opinion.

**The `08`↔`11` seam (the boundary this guide anchors).** A single laboratory result and the
system that governs thousands of them are two different objects, and keeping them separate is
the point:

```
  08-LABORATORY-MEDICINE                 11 (this guide)
  ----------------------                 ---------------------------------
  ONE result: generation + bounding      the SYSTEM around all results:
  local QC concepts only as needed  ---> QC as a PROGRAM (SPC across runs),
  to bound a single number               QA, EQA, governance, accreditation,
  (a delta check; an autoverify          the cross-process error taxonomy,
  gate; sigma as method headroom)        change control, resilience
        |                                        ^
        +------ points forward to 11 ------------+
        the metrology + result belong to 08; the system belongs to 11
```

`08` introduces QC/error concepts *only* to the extent needed to bound one result; `11` owns
the cross-process quality program, the system-level error taxonomy, and governance. Neither
re-derives the other.

> **This module is an educational reference about *how pathology and the laboratory produce
> and reason about findings, and how the diagnostic service is governed as a system* — the
> mechanism-to-diagnosis architecture of the discipline. It is *not* medical advice, *not* a
> laboratory-operating, accreditation, or compliance manual, and gives *no runnable
> procedures, no jurisdiction-specific compliance steps, and no forensic or legal
> determinations*. It does *not* interpret any reader's own result, slide, or report, and
> does *not* diagnose. Governance and standards are described only as concepts, dated and
> attributed; all cases are fictional teaching vignettes and all figures are illustrative.**

*Per-guide banner: educational reference on the diagnostic laboratory as a quality system —
never an accreditation/compliance how-to, never a bench or collection procedure, never
self-diagnosis or personal-result interpretation, never a forensic/legal determination.
Standards and frameworks are named, dated, and treated as concepts, not authoritative
instructions.*

---

## The Big Picture: The Unit of Quality Is the Process, Not the Result

The novice mental model is "a good laboratory produces correct results." The expert model is
that **a laboratory is a system whose product is a *process* with bounded, monitored, and
continuously improved error** — and the unit that quality acts on is not the single number
(`08` owns that) or the single diagnosis (`10` owns that), but the **total testing process**:
Lundberg's *brain-to-brain loop* (1981), from the clinician's question to the answer back in
the clinician's head. The laboratory owns the middle; this guide owns the **control system
wrapped around the whole loop.**

```
THE QUALITY SYSTEM WRAPS THE TOTAL TESTING PROCESS (this guide owns the wrapper)
===============================================================================
        clinician's question                          answer to clinician
              |                                              ^
              v                                              |
  [ pre-pre ]->[ PRE-ANALYTIC ]->[ ANALYTIC ]->[ POST-ANALYTIC ]->[ post-post ]
      order        collect/         measure /       validate /        interpret
      identity     transport        make slide      release           + act
              \___________________ the process being governed ________________/
              |                                              |
   =========  GOVERNANCE + CONTROL LAYER (11)  ==============================
   QC (statistical process control across runs)   EQA (external comparison)
   QA / quality management system (the wrapper)    accreditation + competence
   document + change control                       error taxonomy across phases
   incident / CAPA / amendment feedback loops      turnaround + traceability
   validation/verification GOVERNANCE              resilience + defense-in-depth
   ================================================================================
```

Three properties organize the guide. First, **quality is a control loop, not an inspection
step**: the system *validates* a process into service, *controls* it statistically while it
runs, *assesses* it against an external comparison (EQA), *detects* error, *corrects and
prevents* (CAPA), *change-controls* any modification, and re-validates — a closed loop, not a
final gate. Second, **error is phase-indexed and mostly outside the analytic middle**: as in
`08`, the pre- and post-analytic phases dominate the error surface, so a quality system that
only watches the instrument is watching the smallest slice. Third, **the individual product
and the system are different objects with different owners**: a delta check bounds *one*
result (`08`); a control chart, an EQA program, and an error taxonomy govern *the process that
makes all of them* (`11`).

**Bridge — the laboratory is a production service with SRE around it.** QC is *monitoring and
alerting* on a running process (control charts are SLIs/dashboards; a rejection rule is an
alert threshold); QA is the *engineering practice and quality-management system* the service
runs under; EQA is a *third-party synthetic-probe/audit* that internal monitoring cannot
replace; the error taxonomy is an *incident taxonomy*; CAPA is a *blameless postmortem plus
tracked action items*; change control is *staged rollout with gates and rollback*; validation
vs verification is *pre-production acceptance testing vs local smoke testing of vendor
claims*; traceability is *distributed tracing with a request ID*; turnaround is a *latency
SLO*; resilience is *redundancy, graceful degradation, and defense-in-depth*. The general
safety-science behind all of this (Swiss-cheese, just culture, RCA, HRO, PDSA) is owned and
taught by `clinical-medicine/11`; this guide applies it to the laboratory.

| Layer | Question it answers | `08`↔`11` ownership |
|---|---|---|
| Result generation + bounding | Is *this number/slide/diagnosis* right and how far to trust it? | `08`/`09`/`10` |
| QC (statistical process control) | Is the *process* in control across runs, right now? | `11` (metrics from `08`) |
| QA / QMS | Is the whole system designed and run to produce quality? | `11` |
| EQA (⊇ PT) | Does the process agree with an *external comparison*? | `11` (comparison, not ground truth) |
| Governance / accreditation | Is competence for a scope formally demonstrated (distinct from QMS certification)? | `11` (as concept) |
| Error taxonomy + CAPA | What class of failure occurred and how is it prevented? | `11` |

---

## 1. The `08`↔`11` Seam: Local Control vs the Control Program

Because QC vocabulary appears in both `08` and `11`, the sharpest risk in the whole module is
blurring which owns what. The seam is precise: **`08` owns the concepts needed to bound a
single result; `11` owns the cross-process control *program* those concepts are instantiated
in.**

```
WHERE A QC CONCEPT LIVES  (local bound vs system program)
=========================================================
  CONCEPT                     08 (one result)        11 (the system)
  -------------------------   --------------------   ------------------------
  imprecision / bias / TE     DEFINES + derives      USES for QC PLANNING (rules,
                                                     # controls) -- not chart limits
  delta check                 flags ONE patient's    the delta-check RULE SET
                              implausible change      as a monitored program
  autoverification            gate on ONE result      the autoverify POLICY +
                                                      its validation + audit
  a control observation       (not 08's job)          Levey-Jennings chart +
                                                      Westgard rejection PROGRAM
  method validation numbers   the statistics          the GOVERNANCE requiring,
                                                      recording, approving them
  a single critical value     generation + read-back  the SLA, monitoring, and
                                                      loop-closure surveillance
```

The rule of thumb: if the statement is about **one** number, slide, or diagnosis, it is `08`/
`09`/`10`; if it is about **the process that produces many of them over time** — its control,
conformance, error rate, and governance — it is `11`. `08` introduces local QC only as far as
needed to bound one result and *points forward here*; `11` builds the program and *points back
to `08`* for the underlying metrics, re-deriving none of them.

---

## 2. QC, QA, and EQA: A Three-Layer Control System

Laboratory quality is layered, and the three most-confused terms name three *different* layers
with different scopes and different comparators.

```
THREE LAYERS, THREE SCOPES  (inner to outer)
============================================
  QC   statistical control of a process, run by run, against ITS OWN limits
        |    "is the analytic process in control right now?"
        v
  QA / QMS  the whole management system: people, documents, process design,
        |   competence, improvement -- the WRAPPER around QC
        v
  EQA (⊇ PT)  external COMPARISON to peers/reference -- an OUTSIDE CHECK, not
            ground truth: "does the process agree with other labs / a
            reference, not just with itself?"
```

**Quality control (QC) is statistical process control.** The laboratory runs known control
materials through the *same* process as patient samples and plots the results over time on a
**Levey–Jennings control chart**. The chart's centre line and control limits are the **mean and
SD of that control material as measured repeatedly in *this* laboratory** — established
*empirically from the control's own behaviour*, **not computed from the method's published
imprecision**. The `08 §2` figures (imprecision, bias, allowable total error, sigma) are used
here too, but for **QC *planning*** — how many control levels, which rules, how often — **not**
to draw the chart limits: a high-sigma method can be watched with a sparse rule set, a fragile
low-sigma method needs a denser one. A **rejection rule set** — canonically the **Westgard
multirules** (1981) — then interprets the plotted points, and the interpretation is not
"any point outside ±2SD is a failure." A single point beyond **±2SD (`1_2s`) is commonly a
*warning*, not a rejection**; a run is generally rejected only on **`1_3s`** (one point beyond
±3SD — sensitive to a large random excursion but also capable of detecting a large
systematic shift) or on a **multirule combination**. Within a run, `R_4s` is primarily
sensitive to random error (two controls separated by more than 4 SD), while `2_2s`,
`4_1s`, and `10x` are patterns associated with systematic shift/trend. The whole
point is a *monitoring program*, not a one-time measurement: QC watches the process the way an
SLI dashboard with alert thresholds watches a running service — and a warning is not treated as
an outage.

```
CONTROL CHART SIGNALS  (the shape of the out-of-control tells the error type)
============================================================================
  +3SD ----------------------------------------------  1_3s REJECT
  +2SD - - - - - - - - - - - - - - - - - - - - - - - -  1_2s WARNING only
       .   .      .              . . . . .   <- SHIFT (systematic: calibration,
  mean ----.---.-----.---.---.------------------------     reagent lot, bias)
       .        .  .      .
  -2SD - - - - - - - - - - - - - - - - - - - - - - - -  1_2s WARNING only
  -3SD ----------------------------------------------  1_3s REJECT
    ^one point past 3SD = large excursion     ^same-side run / steady climb = SYSTEMATIC
```

**A central trade-off, borrowed straight from detection theory.** Selecting that rule set is
**QC planning**, and it trades **error detection** against **false rejection**: a very sensitive
rule catches more true out-of-control events but also halts good runs (a false alarm wasting time
and material); a lax rule passes bad runs. It is a **ROC-style operating-point decision** driven
by the `08 §2` performance the method actually has — its sigma against the allowable total error —
so `08` frames sigma as *method headroom* and `11` turns that headroom into a *QC strategy* (which
rules, how many controls, how often). This planning is separate from, and prior to, the chart
limits, which come from the control material itself.

**QC is not only quantitative chemistry.** The Levey–Jennings/Westgard picture is the
quantitative-analyte archetype, but the *concept* — run a known control through the same process
and act on a defined out-of-control signal — generalizes across the laboratory, and a quality
system that only charts chemistry is blind to most of its own testing:

- **Qualitative tests** (reactive/non-reactive, present/absent) cannot be charted on a mean/SD;
  they use **positive and negative controls** (often with a weak near-cutoff control) that must
  read correctly each run — the *control result*, not a numeric distance, is the accept/reject
  signal.
- **Microbiology** uses **reference control strains** for media performance, stain reactivity, and
  antimicrobial-susceptibility panels — a known organism whose expected growth/reaction/MIC is the
  control.
- **Molecular** assays run **positive, negative, and no-template controls**, an **internal
  amplification/extraction control** to catch inhibition or failed extraction, and contamination
  monitoring — the controls guard the *process chain*, not a single number.
- **Anatomic pathology / IHC** uses **on-slide or batch control tissue** of known antigen
  expression (and stain controls), so a negative patient stain is trusted only when the positive
  control worked — the substrate-quality controls owned technically by `09`.
- **Pre- and post-analytic controls** exist too: specimen-acceptability criteria act as a
  *pre-analytic* control gate, and consistency/delta and release checks act as *post-analytic*
  controls — QC is a property of the whole process, not just the analyzer.

**Quality assurance (QA) is the wrapper.** QA — the quality-management system — is the whole
apparatus that makes quality systematic rather than accidental: process design, controlled
documents, competence, internal audit, management review, and continuous improvement. QC is a
*component inside* QA; conflating them ("we do QC, so we have QA") mistakes a monitor for the
management system that acts on it.

**External quality assessment (EQA) is an external *comparison*, not an oracle — and it is
broader than proficiency testing.** Guide `08 §6` owns the operational definition and
comparison mechanics, including commutability. This guide starts at the program boundary:
how external-comparison evidence is selected, reviewed longitudinally, investigated, and
connected to corrective response. Two corrections matter at that system level. First, **EQA ⊋
PT**: proficiency testing (scored external samples) is the best-known *form*, but EQA also
includes inter-laboratory sample-exchange and rechecking/re-read programs, split-sample
comparison against a reference laboratory, and educational schemes — several of which are the
*only* option where formal PT does not exist for an analyte or a setting. Second, **EQA is not
ground truth**: many schemes score against a **peer-group consensus** (which can be collectively
biased), the target may be a consensus mean rather than a reference value, peer groups can be
small, and a non-commutable material can fail a correct method — so an EQA result is *evidence
from an external comparison*, weighed, not an infallible verdict.

Correspondingly, the claim that "internal QC can only agree with itself" is **too strong**.
Internal QC *can* detect **some** bias directly — **assayed controls with independent
reference/target values**, **third-party controls independent of the calibrator**, **reference
materials**, **calibration verification**, and **method-comparison** evidence (`08 §6`) all
surface bias from inside the laboratory. What internal QC structurally struggles to see is bias
**shared with its own calibration or target-setting** (a standardization/commutability problem
common across laboratories); that residual, calibration-linked bias is what an *external*
comparison is uniquely placed to reveal. This is why `11` owns EQA as a **program**, not an
event: choosing and understanding the peer group and target model; **longitudinal review across
cycles** (a trend across scored rounds, not a single pass/fail); its **limitations**
(commutability, consensus targets, small groups); the **corrective response** when a scheme flags
discordance (treat it as nonconforming work → investigate → CAPA, `§6`); and the **alternative
arrangements** — split-sample, inter-laboratory exchange, referral rechecking — that stand in
**when PT is unavailable**.

| Layer | Compared against | Detects | Blind spot (needs another layer) |
|---|---|---|---|
| QC | The control material vs its own established limits | Loss of statistical control (shift/trend/random); *some* bias via assayed/independent controls | Bias **shared with its own calibration/target-setting** |
| QA / QMS | The system vs its own design/requirements | Process/competence/document failures | A single analytic drift in real time |
| EQA (⊇ PT) | An *external* peer group / reference (a comparison, not ground truth) | Calibration-linked bias, blind spots, standardization gaps | Fast, real-time run failures; itself limited by commutability/consensus |

---

## 3. The Cross-Process Error Taxonomy

`08` noted that the error surface is weighted toward the pre- and post-analytic ends; `11`
owns the **taxonomy** that classifies error across the *whole* brain-to-brain loop, because a
classification is the precondition for measuring, targeting, and preventing failure.

```
ERROR ACROSS THE BRAIN-TO-BRAIN LOOP  (phase-indexed; detection vs harm axes)
============================================================================
  PHASE            representative failure class        who first bounds it
  --------------   ---------------------------------   -------------------
  pre-pre          wrong test ordered; wrong patient    ordering + identity
  PRE-ANALYTIC     mislabel, wrong tube, hemolysis,     (08 §5 bounds one
                   clotting, cold-ischemia, mix-up       result; 11 the rate)
  ANALYTIC         calibration/bias, interference,      (08 generates; QC/EQA
                   carryover, instrument fault           surface it in 11)
  POST-ANALYTIC    transcription, wrong units, failed   (release gate 08 §8;
                   flag, result to wrong chart           system view 11)
  post-post        misread, not acted on, delayed       (clinical-medicine/03
                   follow-up of a critical result        + clinical-medicine/11)
```

**Three orthogonal axes make the taxonomy operational.** (1) *Phase* — where in the loop the
failure arose (above). (2) *Error vs harm* — most errors are intercepted before reaching a
patient; a quality system counts *both* the intercepted (near-miss) and the reaching events,
because near-misses are the cheapest data about the next harm. (3) *Detection vs prevention* —
a defense either **catches** an error after it happens (a delta check, an EQA failure, an
amendment) or **prevents** it from happening (barcoded identity, a forcing function in
ordering); a mature system shifts weight from detection toward prevention. The **post-post**
phase — a correct result misread or not acted upon — is a real and often dominant failure
class, but its ownership is shared: the laboratory closes the loop it can (critical-result
communication, `§6`), while the *clinical* diagnostic-safety system is owned by
`clinical-medicine/11` and belief/action by `clinical-medicine/03`.

**Defense in depth.** No single control catches every error, so the system layers independent,
imperfect barriers — identity checks, QC, autoverification limits, delta checks, EQA, review —
so that an error must pass through *several* holes at once to cause harm. This is exactly the
**Swiss-cheese / latent-error model**, whose general theory is owned and taught by
`clinical-medicine/11`; `11` here instantiates it as the laboratory's specific layered
controls and points to that framework rather than re-deriving it.

**Bridge — an incident taxonomy plus defense-in-depth.** Phase-indexed error classes are an
*incident taxonomy*; near-miss counting is *tracking caught exceptions, not just outages*; the
detection→prevention shift is *moving from alerting to eliminating a failure class*; layered
barriers are *defense-in-depth*. Naming the class is what lets the system aggregate, trend, and
target — the same reason a good incident system enforces a taxonomy.

---

## 4. Validation and Verification: Governing Fitness Before Service

Before a method, instrument, or assay is used on patients, the system must establish that it is
**fit for its intended use** — and `11` owns the *governance* of that gate, while `08` owns the
*statistics* computed inside it. Both validation and verification are exercises in producing
**objective evidence** that the requirements for a *specific intended use* are met; the
distinction between them is precise and constantly blurred.

```
VALIDATION vs VERIFICATION  (establish vs confirm; a governance gate)
====================================================================
  VALIDATION     establish that a method meets requirements for its
   (establish)   intended use -- broad, for a new/modified/lab-developed method
        |
  VERIFICATION   confirm, locally, that an already-validated method performs
   (confirm)     to its stated claims in THIS laboratory -- narrower
        |
  [ GOVERNANCE GATE ]  documented acceptance criteria met + approved
        |               BEFORE the method goes into service
        v
  in service -- now governed by ongoing QC (§2) and EQA (§2)
```

- **Validation** asks the broad question — *does this method do what is required for its intended
  use?* — the heavier exercise applied to a new, modified, or laboratory-developed method: it
  produces objective evidence across the performance claims from first principles rather than
  assuming any.
- **Verification** asks the narrower question — *does this already-validated method meet its
  stated performance claims here, in this laboratory, on this population?* — confirming vendor or
  literature claims locally with objective evidence.
- **Local method verification is not reference-interval verification.** Confirming a method's
  *analytical* claims (imprecision, bias, linearity, detection limits) is a distinct activity from
  confirming that a quoted **reference interval** is transferable to the local population (or
  establishing one where it is not). A method can verify cleanly while its reference interval is
  wrong for the population served — two separate objective-evidence gates.
- **A "verification" can tip into requiring validation.** The verification shortcut is licensed
  only while the method is used *within its validated intended use*. Modifying the method, or using
  it outside that boundary — a new matrix, specimen type, population, or analyte, or any off-label
  use — **moves the intended-use boundary** and can require full **validation**, not mere
  verification.
- The **governance** `11` owns is the *gate*: predefined acceptance criteria, the record that the
  evidence met them, documented approval, and the rule that a method does **not** enter service
  until the gate is passed. The underlying performance statistics — imprecision, bias, linearity,
  detection limits, method comparison — are `08 §2–§6`; `11` requires, records, and approves them
  without re-deriving them.

**Bridge — acceptance testing vs a smoke test, behind a release gate.** Validation is *full
pre-production acceptance testing of a new component*; verification is *a local smoke test that
a vendor-certified component meets its spec in the target environment*; the governance gate is *the
release gate that blocks promotion until acceptance criteria are signed off*. The reason both
exist is the same reason a platform both certifies a component and re-tests it in the target
environment.

---

## 5. Document Control, Change Control, and Competence

A quality system is only as trustworthy as its ability to know **what process was in force,
when, run by whom, under which version of which document** — which makes controlled documents,
governed change, and demonstrated competence load-bearing rather than clerical.

**Document control** keeps procedures, policies, and forms as **controlled, versioned,
uniquely identified documents**, so that the process actually in force is knowable and
obsolete versions cannot be used by accident. Conceptually it is *configuration management for
the process*: a single source of truth, versioned, with controlled distribution.

**Change control** governs any modification to a validated process — a new reagent lot, a
platform change, a revised procedure — through **assess (with a risk assessment) →
validate/verify → approve → implement → document → monitor**, so a change cannot silently alter
results. The impact assessment is not only analytical: it also asks which **documents, training,
and competence** the change touches (a revised procedure obsoletes a controlled document and may
require re-training), and after cut-over the change is **monitored for effectiveness** rather than
assumed to have worked. An uncontrolled change is the laboratory's version of an unreviewed push
straight to production; the discipline is a staged rollout with a gate, a recorded rationale, and
post-deployment monitoring, so that a later shift on a control chart (`§2`) can be *traced to* the
change that caused it.

```
CHANGE CONTROL  (no silent change to a validated process)
=========================================================
  proposed change (reagent lot / platform / procedure)
        |
  [ ASSESS impact + RISK ]   results? documents? training/competence?
        |
  [ VALIDATE / VERIFY ] -> [ APPROVE ] -> [ IMPLEMENT with a record ]
        |
  [ MONITOR effectiveness ] ----> a later control shift (§2) traces to its cause
        |
  documented, versioned, reversible (re-validate if the change misfires)
```

**Competence** is the people-layer analogue: a governed program that assesses and records that
individuals performing and interpreting each process are qualified to do so, and that this is
reassessed over time. It is distinct from accreditation (`§7`): accreditation formally
demonstrates the *laboratory/system's* competence for a scope, while competence assessment
documents that an *individual* is qualified — and a system needs both. Competence assessment is described here **as a concept and a
governance obligation**, never as a curriculum, credentialing instruction, or jurisdiction-
specific requirement.

---

## 6. Incident, Communication, and Amendment Loops

Detecting an error is worthless unless it feeds a **closed loop** that communicates,
corrects, and prevents. `11` owns three interlocking feedback loops as *system* mechanisms
(the single-event generation of each is owned by `08`/`10`).

**Critical-result communication as a monitored SLA.** `08 §8` and `10 §8` own the *generation*
of a critical value / critical diagnosis and its read-back; `11` owns the **program**: the
policy defining what counts as critical (a service-level agreement between laboratory and
clinicians), and the ongoing surveillance that the loop actually closes — that verified,
acknowledged delivery is happening at the expected rate, not merely specified. The property is
*at-least-once delivery with acknowledgment*, monitored as a system, not assumed per event.

**Nonconforming work: handle the instance before chasing the cause.** When testing does not
conform to its own requirements (a nonconformity — an out-of-control run, an EQA discordance, a
mislabeled specimen, a released wrong result), the first obligations are about the *instance*, not
yet the cause: **assess the affected results** (which patients/reports, over what interval — a
look-back via traceability, `§8`), **contain and correct** them (halt release, correct or retract
reports), **communicate** to the clinicians who may have acted, and judge the **risk /
significance**. Only then does the system move to the cause. Whether the fix touches a validated
process determines whether it re-enters **change control** (`§5`), and any change to **documents,
training, or competence** is part of the same handling — followed by **monitoring the
implementation** and a later **effectiveness review**.

**Incident reporting and CAPA — and why "preventive action" is not one bucket.** A **non-punitive
reporting** culture captures errors *and near-misses* (the cheapest early warning of the next
harm — the *just-culture* principle, owned generally by `clinical-medicine/11`). What follows is a
**precise sequence**, and the common shorthand "corrective fixes the instance, preventive stops
recurrence" gets it wrong:

- **Correction / containment** fixes or contains the *instance* (correct the wrong result,
  quarantine affected output). It addresses the symptom, **not** the cause.
- **Impact assessment** bounds what was affected (the look-back above).
- **Cause analysis** finds the contributing/root cause (the *technique* — RCA — is owned by
  `clinical-medicine/11`; applied here to laboratory processes).
- **Corrective action** is the step that **controls or removes the cause so the nonconformity does
  not *recur*** — this, not the instance-fix, is what "corrective action" means in quality terms.
- **Effectiveness verification** confirms the corrective action actually worked (the failure class
  stopped recurring), or the loop reopens.
- **Preventive action / prospective risk control** is a **separate, proactive** activity: acting on
  *potential* nonconformities that have **not** occurred, driven by risk assessment (in current
  risk-based quality management this is largely folded into ongoing **risk control**, not a
  reactive "preventive" afterthought).

```
THE CORRECTIVE LOOP  (fix the instance, then remove the cause; prevention is separate)
=====================================================================================
  nonconformity OR near-miss detected (QC, EQA, delta, amendment, report)
        |
  [ CONTAIN / CORRECT ] fix this instance  +  [ IMPACT ASSESSMENT ] look-back (§8)
        |
  [ CAUSE ANALYSIS ]  contributing/root cause (RCA: clinical-medicine/11)
        |
  [ CORRECTIVE ACTION ]  control/remove the CAUSE so it cannot recur
        |
  [ VERIFY EFFECTIVENESS ]  did recurrence actually stop? --> reopen if not
        |
  change control (§5) if the fix alters a validated process
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  PREVENTIVE ACTION / RISK CONTROL (separate, proactive): act on POTENTIAL
  nonconformities that have NOT happened, from risk assessment -- not a bucket
  bolted onto the corrective loop
```

**Amendments as a *stratified* defect signal — not every amendment is a defect.** The
amendment/addendum/retraction taxonomy is owned by `10 §9` (what each *is*); `11` owns the
**surveillance**, and the surveillance must be **stratified by type**, because a crude "amendment
rate" conflates different things. A **correction** or **retraction** of a released report (a wrong
result or a changed interpretation) is a genuine **defect signal** and feeds the corrective loop.
An **addendum that merely adds later-arriving information** — a special stain, an ancillary or
molecular result that returns after sign-out, added correlation — is a **normal, expected** part of
the workflow and is **not automatically a defect**; counting it as one both inflates the metric and
penalizes good practice. So `11` monitors the *rate and type* of report changes, separating defect
corrections (which should trend down) from expected addenda (which should not) — the correction log
is an error-surveillance stream only once it is stratified.

---

## 7. Accreditation, Competence, and Governance — As Concepts

**This is the highest scope-risk section, so its boundary is drawn explicitly: everything below
is conceptual, dated, and attributed — there is no accreditation "how-to," no compliance
checklist, and no jurisdiction-specific requirement.** The aim is literacy about *what these
governance mechanisms are and why they exist*, not instructions to obtain or satisfy any of
them.

**Accreditation is scope-specific third-party attestation of *competence* — not certification of a
management system.** An external accreditation body assesses whether a laboratory is **technically
competent** to perform a **defined scope** of examinations and can do so **impartially and with
consistent operation**, and if so attests exactly that — for that scope. The medical-laboratory
archetype is **ISO 15189** (*Medical laboratories — Requirements for quality and competence*; first
published 2003, with the current edition **ISO 15189:2022**, which is risk-based and also absorbed
point-of-care testing — editions and their content should be confirmed against the issuing body,
not assumed from this text), operated through regionally recognized accreditation bodies. The
distinction from **certification** is the crux and is routinely blurred: **certification** (e.g.,
ISO 9001) attests that a **management system conforms** to a standard; **accreditation** (ISO
15189) formally demonstrates **competence, impartiality, and consistent operation for a specific scope of
activities**. The two frameworks address different objects and are not a general
stronger/weaker hierarchy. Accreditation is therefore *not* a QMS-conformance stamp,
and — like every layer here — it addresses the *system's*
competence, **never any individual patient result**.

*(Bridge, kept accurate: certification is like attesting "a documented, conformant process
exists"; accreditation is like an independent body judging a team **demonstrably competent** to
produce trustworthy outputs within a **named scope** — the two are not interchangeable, and neither
guarantees any single output is correct.)*

```
LAYERS OF GOVERNED EVIDENCE  (what object each layer evaluates)
==============================================================
  METHOD      validated/verified fit for intended use     (governed in §4)
  INDIVIDUAL  competent to perform/interpret              (competence, §5)
  SYSTEM      competent, impartial, consistent for a       (accreditation, §7;
              DEFINED SCOPE -- not mere QMS conformance     certification addresses
                                                            a different object)
  PROCESS     in-control + externally compared             (QC + EQA, §2)
  ------------------------------------------------------------------------
  a trustworthy report rests on ALL; NONE attests an individual result --
  each contributes evidence about the system/method/person/process behind it
```

**Governance ties the layers together.** The recurring structure is *define a requirement →
demonstrate conformance/competence → audit periodically → correct gaps* — internal audit and management review
inside the laboratory, external accreditation and EQA outside it. The distinction to hold:
**accreditation demonstrates the system's competence for a scope, competence assessment
evaluates the person, validation/verification provides objective evidence for the method,
QC monitors the process, and EQA compares it externally** — different objects and
evidence functions, none substituting for
another, and **not one of them attests any single patient result**; a specific result is only ever
*inferred* to be trustworthy from the governed system behind it.

**What this guide deliberately does not do.** It does not state how to prepare for, apply for, or
pass any accreditation; it does not enumerate any jurisdiction's regulatory requirements; and it
does not present any standard's clauses as instructions. Standards evolve and differ by country and
era; the durable content is the *concept* (scope-specific third-party attestation of competence,
impartiality, and consistent operation — distinct from management-system certification) and the
*reason it exists* (a result is only as trustworthy as the governed system behind it). Specific
editions, clauses, and local requirements are to be confirmed against the issuing bodies, not this
reference.

---

## 8. Turnaround, Traceability, and Flow

A correct result delivered too late, or that cannot be traced end to end, is a *system* failure
even when every measurement was perfect — so the laboratory governs **time** and **provenance**
as first-class quality attributes.

**Turnaround time (TAT) is a latency SLO.** TAT is the interval across the process (commonly
order-to-result, with meaningful sub-intervals), and it is governed as a *service-level
objective* stratified by urgency: a routine result and a critical-path result carry different
targets. TAT is a **distribution, not a single number** — the discipline is to watch the tail
(the delayed minority that drives harm), exactly as an SRE watches p99 latency rather than the
mean, because the worst-served cases, not the average, are where the risk concentrates.

**Traceability is end-to-end provenance — which is *not* the same as a legal chain of custody.**
Every specimen and result carries an identity and a provenance trail — patient → order → specimen
→ aliquot/block → instrument/stain run → result/diagnosis → report — so that any output can be
traced back to the exact inputs, process version, and operators that produced it. This is
*distributed tracing with a correlation ID* for the specimen: it makes a look-back possible (when a
fault is found, which results were affected?), and it turns the identity failures of `§3` and
`09 §1` from silent mix-ups into detectable, bounded events. **Routine traceability is a quality
property, not a forensic one.** A legal **chain of custody** is a distinct, stricter regime — a
formally documented, tamper-evident custody trail with controlled, signed hand-offs, invoked only
for specimens with medicolegal implications and defensible in a legal proceeding. The everyday
laboratory's traceability supports look-back and QA; it is *not* automatically a legal chain of
custody, and the forensic/legal use of the latter is out of scope (pillar 3, `§9`).

```
FLOW + TRACEABILITY  (provenance turns a fault into a bounded look-back)
======================================================================
  order -> specimen -> accession -> process/run -> result -> report
     \_________________ each step stamped with identity + version ______/
        |
  when a fault is found at ANY step:
        |
  [ LOOK-BACK ]  which specimens/results share the faulty step? -> bound + act
```

**Flow is queueing.** The laboratory is a network of queues and workstations; batching,
prioritization, and bottlenecks set TAT and its variance. Governing flow — where work waits,
how urgent work preempts routine — is a throughput/latency trade-off, the same queueing problem
any high-throughput pipeline manages, and it is owned here as a *system* property, distinct
from the generation of any one result.

---

## 9. The Autopsy and Audit Boundary

Audit — systematically comparing what the system *did* against what it *should have done* — is
the feedback mechanism that closes the outer quality loop, and the **autopsy** is one specialized
audit instrument. Its treatment here is strictly bounded.

**Four feedback instruments, four different comparisons.** "Audit" is used loosely to cover several
outer-loop mechanisms that are *not* interchangeable — they differ in who compares *what* against
*what*:

| Instrument | Compares… | …against | Owner / scope note |
|---|---|---|---|
| **Internal audit** | the laboratory's actual activities/records | its own QMS + defined requirements | planned, independent, documented; owned here |
| **EQA / PT** | the laboratory's *testing performance* | an external peer group / reference | the external comparison of `§2`; not ground truth |
| **Morbidity & mortality (M&M) review** | management/outcomes of specific cases | the expected standard of care | case-based clinical learning forum; clinical scope |
| **Clinicopathologic (consented) autopsy** | pre-mortem diagnoses/management | post-mortem findings | diagnostic-discordance audit; conceptual here only |

Internal audit asks "did we follow our own system?"; EQA asks "do our results agree with
others'?"; M&M asks "was this case managed to standard?"; the clinicopathologic autopsy asks "did
we get the diagnosis right, checked against the tissue?" — related in spirit, distinct in
mechanism.

**Autopsy as a clinicopathologic audit (conceptual only).** A hospital/consented autopsy has
historically served as a **quality audit**: comparing pre-mortem diagnoses and management against
post-mortem findings surfaces *diagnostic discordance* the living system never detected — a
correlation-and-feedback function, the ultimate look-back on the diagnostic process. `11` owns
this only as a **conceptual audit boundary**: it is a mechanism by which the diagnostic system
learns about its own missed or discordant diagnoses.

**The hard boundary (pillar 3).** The **forensic/medicolegal autopsy** — determination of
**cause and manner of death** and any legal conclusion — is **out of scope entirely**. This
guide makes no cause-of-death, manner-of-death, or legal determination, describes no autopsy
procedure, and gives no forensic technique; those belong to legal/forensic authorities and are
excluded by the module's four-pillar contract. Only the *conceptual role of the consented
autopsy as a quality-audit feedback mechanism* is in scope.

```
AUDIT AS OUTER-LOOP FEEDBACK  (what was done vs what should have been)
====================================================================
  the diagnostic system's outputs over time
        |
  [ AUDIT ]  internal audit / EQA / M&M-style review / consented autopsy
        |            compare to the intended standard
        v
  discordance + missed-diagnosis signal  ->  CAPA (§6) -> improvement
  --------------------------------------------------------------------
  IN SCOPE: audit as feedback.  OUT OF SCOPE: forensic cause/manner of death.
```

**Bridge — audit is the retrospective the system runs on itself.** Internal audit, EQA, and the
consented autopsy are the laboratory's *scheduled retrospectives*: they compare intended vs
actual, surface latent failures the real-time monitors missed, and feed the corrective loop.
The forensic determination is a different activity with a different (legal) purpose and is not
this module's.

---

## 10. Laboratory-System Resilience

Individual results can be correct while the *system* fails — an instrument goes down, an
information system is unavailable, a reagent supply is interrupted, a disaster strikes. `11`
owns the resilience of the service as a system.

**Redundancy and graceful degradation.** A resilient laboratory has *defined degraded modes*:
backup instruments, downtime pathways for when the information system is unavailable, and
alternate routing (send-out/referral) when a capability is lost — so the service degrades
gracefully rather than failing hard. Conceptually this is *redundancy plus graceful
degradation*: the system keeps delivering the critical subset of its function under partial
failure, at reduced throughput or capability.

**Defense in depth against system failure.** The same layered-barrier logic of `§3` applies at
the system scale: independent checks (identity, QC, EQA, review) and independent capabilities
(backup instruments, downtime procedures) mean a single failure does not cause a systemic bad-
result event. The general latent-error/defense-in-depth theory is `clinical-medicine/11`;
`11` here instantiates it for the diagnostic service.

```
RESILIENCE MODES  (degrade gracefully, not catastrophically)
===========================================================
  NORMAL          full capability, full throughput
     |   instrument down / LIS down / supply gap / disaster
     v
  DEGRADED        backup instrument; downtime pathway; send-out routing
     |            critical function preserved, throughput/capability reduced
     v
  RECOVERY        reconcile the degraded interval; look-back if needed (§8)
  ----------------------------------------------------------------------
  the failure mode is planned FOR in advance, not improvised
```

**Recovery and reconciliation.** After a degraded interval, the system reconciles what happened
during it — which results were produced under the backup pathway, whether any need review — a
look-back enabled by the traceability of `§8`. Resilience is thus not just staying up; it is
*knowing what the system did while impaired* and correcting it afterward.

---

## 11. Worked Fictional Cases: The System View

*Fully fictional teaching vignettes. No laboratory, event, or result is real; each shows a
*system* mechanism, not a single-result generation (which is `08`/`10`) and not any real
compliance action. Nothing here is a procedure, a compliance instruction, or advice.*

**Case A — a systematic shift, and the `08`↔`11` seam in action (`§1`, `§2`, `§3`, `§6`).** In a
fictional laboratory, individual results are each internally plausible, and a per-result **delta
check** (owned by `08`) flags nothing unusual on any single patient. But the **control chart**
(owned by `11`) shows the control material drifting steadily to one side over successive runs —
a **systematic shift**, not random scatter — and the **Westgard** rule set trips. This is the
seam made concrete: the single-result tool saw nothing, because the failure is a property of the
*process over many runs*, which only the QC *program* detects. The system response is a
laboratory one: hold affected reporting, investigate the cause (e.g., a calibration or reagent-lot
change that should have gone through **change control**, `§5`), and — because results may already
have been released — perform a **look-back** using traceability (`§8`) to bound which results were
affected, then close the loop with **CAPA** (`§6`). No number here is interpreted for any patient;
the case shows *which layer owns the detection.*

**Case B — an ungoverned change surfaces at EQA (`§2`, `§4`, `§5`, `§7`).** A fictional laboratory
modifies a validated process without routing it through **change control** and **verification**
(`§4`/`§5`). The change affects patient-like samples, but the laboratory's control material
is **noncommutable** for the altered matrix effect and therefore remains near its established
mean and limits. Internal QC stays in control because the control fails to reproduce the
patient-sample bias — not because limits silently moved. The failure surfaces in an external
comparison using more patient-like material, revealing a matrix-dependent bias that this
particular IQC system was structurally unable to see. The governance
response is conceptual and system-level: treat the EQA discordance as an incident, investigate,
apply CAPA, and re-establish the change under proper validation/verification governance —
illustrating why EQA is a *separate, independent check* from QC and why change control exists.
Nothing here states how to pass EQA or satisfy any accreditation requirement; it shows *why the
layers are independent* (and EQA is a weighed comparison, not ground truth).

**Case C — graceful degradation and reconciliation (`§8`, `§10`).** A fictional information-system
outage removes automated result release. A resilient laboratory has a **defined downtime pathway**
(`§10`) and continues delivering the critical subset of its function at reduced throughput; every
specimen and result produced during the interval retains **traceability** (`§8`). When the system
recovers, a **reconciliation/look-back** bounds what was produced under the degraded pathway and
whether any of it needs review. The case shows resilience as *planned-for degradation plus
after-the-fact reconciliation*, a system property no single correct result captures.

**Case D — a resource-constrained laboratory keeps the *reasoning* without the infrastructure
(`§2`, `§5`, `§8`, `§10`).** A fictional district laboratory has **no** laboratory information
system, **no** enrolled proficiency-testing scheme for several of its analytes, and **no** backup
analyzer. It still runs the quality *reasoning*, on manual footing. Traceability is a **paper
accession register** linking each specimen to patient, operator, and run — provenance without a
digital tracer (`§8`). External comparison, where formal **PT is unavailable**, is approximated by
a **split-sample exchange** with a referral laboratory and periodic **re-read/rechecking** of a
sample of cases — an EQA *arrangement*, not a scheme (`§2`, and recall EQA ⊋ PT). A method change
still goes through a manual **change-control** record and a documented re-check before use (`§5`).
Resilience is a **defined manual downtime pathway** and **referral routing** for tests it cannot
repeat, with reconciliation on recovery (`§10`). Nothing here assumes accreditation, a digital
system, or a backup platform — it shows that *control, external comparison, traceability, and
planned degradation* are **reasoning**, portable to settings the resourced archetype does not
describe, even as the achievable confidence in a result depends on that surrounding system.

---

## Reader Tasks (answerable from this guide)

Each task is a *system-reasoning* exercise — how the diagnostic service is governed, controlled,
and made to fail safely — not a compliance instruction and not a personal-result interpretation.

**Task 1 — "Every individual result looked fine, yet the laboratory halted reporting. What system
signal fired, and why couldn't a single-result check catch it?" (`§1`, `§2`)**
A **QC control chart** signalled a **systematic shift** across runs (a Westgard rule tripped) —
a property of the *process over many runs*, which is `11`'s program. A per-result **delta check**
(`08`) evaluates *one* patient's plausibility and cannot see a slow, consistent drift that keeps
each individual value internally plausible. That is the `08`↔`11` seam: the local tool bounds one
result; the control program governs the process. The chart limits come from the control material's established mean and SD; the
imprecision/bias/TEa/sigma metrics in `08 §2` inform QC planning and rule selection,
not limit construction.

**Task 2 — "Internal QC was perfectly in control, but EQA flagged a discordance. How is that
possible, and how much should the laboratory trust the EQA result?" (`§2`)**
Internal QC compares the process to its *own* established limits, so a bias **shared with its own
calibration/target-setting** can leave QC in control while the process is consistently offset — QC
is not blind to *all* bias (assayed/independent controls, reference materials, calibration
verification, and method comparison catch some), but it is weakest exactly on calibration-linked
bias, which an **external comparison** is placed to reveal. Trust the EQA signal as **evidence, not
a verdict**: EQA is a comparison against a peer group/reference (`08 §6`), so a non-commutable
material or a biased peer consensus can flag a correct method — the system response is to treat it
as nonconforming work, investigate, and confirm with independent evidence before acting (`§6`), not
to assume the laboratory is wrong. Neither layer replaces the other, and EQA (⊇ PT) is a *program*
reviewed across cycles, not a single pass/fail.

**Task 3 — "The overall 'amendment rate' is climbing. Why can't the quality system act on that
number as-is?" (`§6`, `10 §9`)**
Because the crude rate **conflates two different things and must be stratified by type**. A
**correction/retraction** (a wrong result or a changed interpretation) is a genuine defect signal
and should feed the corrective loop and trend *down*. An **addendum that adds later-arriving
information** (a special stain, a molecular result returning after sign-out) is **normal, expected
practice and not automatically a defect** — counting it inflates the metric and penalizes good
work. `10 §9` owns what each change *is*; `11` owns the surveillance, and the surveillance is only
meaningful once corrections are separated from expected addenda. Where the *defect* stream rises,
the target is the **cause** (a method, step, or interpretation pattern) via corrective action at
the class level (`§6`).

**Task 4 — "What is the difference between validating a method, accrediting the laboratory,
assessing an individual's competence, and *certifying* a QMS?" (`§4`, `§5`, `§7`)**
Different objects, different evidence: **validation/verification** provides objective
evidence that the **method** is fit for its intended use (`§4`); **competence**
assessment evaluates whether the **individual** is competent
(`§5`); **accreditation** (ISO 15189, as a concept) demonstrates the **system's competence,
impartiality, and consistent operation for a defined scope** (`§7`) — which is **not** the same as
**certification** (e.g., ISO 9001), which attests that a **management system conforms**
to its own standard; the two address different objects and are not a general
stronger/weaker hierarchy. **QC/EQA** provide monitoring and external-comparison
evidence about the running process (`§2`); they do not attest it. None
substitutes for another, and — the point that catches people — **none of them attests any single
patient result**; a result's trustworthiness is *inferred* from the governed system, never directly
certified. This guide treats accreditation and competence as concepts, never as a how-to.

**Task 5 — "Why is the pre-analytic phase a bigger quality target than the analyzer, and what does
a system do about it that `08` does not?" (`§3`)**
Because, as `08` notes, the error surface is weighted toward the pre- and post-analytic ends. `08`
bounds *one* pre-analytic error's effect on *one* result (e.g., a hemolysis flag). `11` owns the
**taxonomy and the rate**: classifying pre-analytic failures (mislabel, wrong tube, cold-ischemia,
mix-up), counting near-misses, and shifting weight from **detection** to **prevention** (barcoded
identity, forcing functions) across the whole process — a system intervention on a failure *class*,
not a bound on a single result.

**Task 6 — "A laboratory has no LIS, no proficiency-testing scheme for an analyte, and no backup
analyzer. Can it still run a quality system?" (`§2`, `§8`, `§10`, `§11`)**
Yes — the *infrastructure* is absent but the *reasoning* is portable. Traceability can be a **paper
accession register** (provenance without a digital tracer, `§8`); external comparison, where formal
**PT is unavailable**, can be approximated by **split-sample exchange** with a referral laboratory
or periodic **re-read/rechecking** (an EQA *arrangement* — recall EQA ⊋ PT — not a scheme, `§2`);
resilience is a **defined manual downtime pathway** and **referral routing** with reconciliation on
recovery (`§10`). What changes is the achievable **confidence** in a result, which depends on the
surrounding system; what does not change is that control, external comparison, traceability, and
planned degradation still apply. No accreditation, digital system, or backup platform is assumed
(Case D).

---

## Decision Cheat Sheet

*Which quality-system concept a given situation involves (all descriptive system model states; no
compliance instructions, no personal-result interpretation):*

| Situation / signal | The concept is… | Where it lives |
|---|---|---|
| "This one result is implausible for this patient" | Local **delta check** (bounds one result) | `08 §8` |
| Control material drifting across runs | **QC / SPC** shift-or-trend; limits from the control's own mean/SD | §2 |
| `1_2s` exceedance vs a rejected run | `1_2s` = **warning**; reject on `1_3s` or a **multirule** | §2 |
| Choosing how many controls / which rules | **QC planning** from sigma/TEa/bias (not the chart limits) | §2, `08 §2` |
| QC for a qualitative / micro / molecular / IHC test | **Non-quantitative controls** (pos/neg, control strains, control tissue) | §2, `09` |
| "We do QC, so we have QA" | QC is a component *inside* **QA/QMS** | §2 |
| In control internally but discordant vs peers | **EQA (⊇ PT)** — external *comparison*, not ground truth | §2, `08 §6` |
| Does internal QC see *any* bias? | *Some* — via assayed/independent controls, reference materials, calibration verification, method comparison | §2, `08 §6` |
| Classifying where a failure arose | **Cross-process error taxonomy** (phase-indexed) | §3 |
| Counting near-misses, not just harms | Error-vs-harm + **detection→prevention** axes | §3 |
| Many independent imperfect checks | **Defense in depth** (framework: `clinical-medicine/11`) | §3, §10 |
| "Does this method meet requirements for its intended use?" | **Validation** (establish fitness by objective evidence) | §4 |
| "Does this validated method meet claims here?" | **Verification** (confirm locally by objective evidence) | §4 |
| Is a quoted reference interval right for this population? | **Reference-interval verification** (distinct from method verification) | §4 |
| Method modified / used outside its intended use | May require **validation**, not mere verification | §4 |
| A reagent-lot/platform change | **Change control** (assess+risk → verify → approve → implement → monitor) | §5 |
| "Which document version was in force?" | **Document control** (config management) | §5 |
| Is the person qualified to do this? | **Competence** assessment | §5 |
| Is the *system* competent for a scope (≠ QMS certification)? | **Accreditation** (ISO 15189, as concept) | §7 |
| A critical result must reach a clinician | Critical-communication **SLA + surveillance** | §6, `08 §8`, `10 §8` |
| Testing didn't conform (a wrong result was released) | **Nonconforming work**: affected-result assessment → contain/correct → communicate → cause → corrective action → verify | §6 |
| "Corrective vs preventive action" | Correction fixes the *instance*; **corrective action** removes the *cause* (recurrence); **preventive/risk control** is separate & proactive | §6 |
| Rising amendment rate | **Stratify**: corrections/retractions = defects; expected **addenda ≠ defects** | §6, `10 §9` |
| Result correct but too late | **Turnaround (TAT)** as a latency SLO (watch the tail) | §8 |
| "Which results did a fault affect?" | **Traceability** + **look-back** (a quality property) | §8 |
| Formal custody trail for a medicolegal specimen | **Legal chain of custody** (≠ routine traceability); out of scope | §8, §9 |
| "Did we follow our own system?" | **Internal audit** (vs EQA, M&M, autopsy — different comparisons) | §9 |
| "Did we get the diagnosis right, checked against the tissue?" | **Clinicopathologic autopsy** (conceptual audit only) | §9 |
| Cause / manner of death, legal opinion | **Out of scope** (pillar 3) | §9 |
| Instrument/LIS down; supply gap | **Resilience** / graceful degradation | §10 |
| No LIS / no PT scheme / no backup analyzer | Quality *reasoning* via manual records, split-sample/rechecking, referral, downtime pathway | §2, §8, §10, §11 |
| How the number/slide/diagnosis is made | Not here — generation | `08`/`09`/`10` |
| The clinical care-system safety science | Not here — the clinical system | `clinical-medicine/11` |

---

## Common Confusion Points

- **The unit of quality is the process, not the result.** `08`/`09`/`10` own the individual
  number, slide, and diagnosis; `11` owns the *system* that produces all of them — its control,
  conformance, error rate, and governance. A statement about *one* output is not a statement
  about the system.
- **QC ≠ QA ≠ EQA.** QC is statistical control of a process against its **own** established limits;
  QA/QMS is the whole management system QC sits inside; **EQA (⊇ PT)** is an *external comparison* —
  a peer group or reference, **not ground truth**. "We do QC" is not "we have QA," and internal QC
  does not substitute for external comparison.
- **Internal QC is not blind to all bias — but it is weakest on calibration-linked bias.** Assayed
  or independent controls, reference materials, calibration verification, and method comparison
  (`08 §6`) let internal QC catch *some* bias; what it structurally struggles to see is bias
  **shared with its own calibration/target-setting**, which an external comparison reveals.
  In-control is not the same as correct — but "QC can only agree with itself" overstates it.
- **Control limits come from the control, not the method's imprecision.** Levey–Jennings limits are
  the control material's own mean/SD established in *this* laboratory; the `08 §2` sigma/TEa/bias
  figures drive **QC planning** (rules, number of controls), not the chart lines. And `1_2s` is a
  **warning** — rejection needs `1_3s` or a multirule. QC also extends past quantitative chemistry
  to qualitative, micro, molecular, and IHC controls.
- **`08` owns the metric; `11` owns the program.** Imprecision, bias, total error, sigma, RCV, and
  detection limits are `08 §2–§6`; `11` *uses* them for QC planning and strategy and
  re-derives none of them. The seam is one-result vs the process.
- **Validation ≠ verification — and verification can tip back into validation.** Validation
  *establishes* fitness for a new/modified method **by objective evidence**; verification *confirms*
  an already-validated method's claims locally. Verifying a **reference interval** for the local
  population is a *distinct* gate from verifying method performance, and **modifying** a method or
  using it outside its intended-use boundary can require full **validation**. `11` owns the
  governance gate; `08` owns the statistics inside it.
- **Correction is not corrective action.** Fixing or containing the *instance* is **correction**;
  **corrective action** removes or controls the *cause* so the nonconformity cannot **recur**;
  **preventive action / risk control** is a *separate, proactive* activity on problems that have
  **not** happened. "Corrective fixes it, preventive stops recurrence" mislabels all three.
- **Accreditation formally demonstrates competence for a scope; certification demonstrates QMS conformance.** They are
  different claims: accreditation (ISO 15189) attests **competence, impartiality, and consistent
  operation** for a defined scope; certification (e.g., ISO 9001) demonstrates that a **management system
  conforms**. Competence assessment, validation, QC, and EQA provide different forms of
  evidence about different objects — and **none certifies any single patient result**;
  result trust is *inferred* from the governed system.
  This guide treats them as concepts, not a compliance how-to.
- **A near-miss is data, not a non-event.** A non-punitive culture captures near-misses because
  they are the cheapest early warning of the next harm; a punitive system suppresses exactly the
  reports it most needs (just-culture theory is `clinical-medicine/11`).
- **The amendment log is an error stream only once stratified.** `10 §9` owns what each change
  *is*; `11` owns *rate and type* — but a **correction/retraction** is a defect signal while an
  **addendum** that adds later-arriving information is **expected practice, not a defect**. Counting
  all amendments together inflates the metric and penalizes good work.
- **Turnaround is a distribution.** Governing TAT means watching the delayed tail, not the mean —
  the worst-served cases carry the risk.
- **Routine traceability is not a legal chain of custody.** Everyday specimen/result provenance
  supports look-back and QA; a legal **chain of custody** is a stricter, tamper-evident, signed
  custody regime for medicolegal specimens and is out of scope (pillar 3).
- **"Audit" names several different comparisons.** Internal audit (did we follow our own system?),
  EQA/PT (do our results agree with others'?), M&M review (was this case managed to standard?), and
  the clinicopathologic autopsy (did we get the diagnosis right vs the tissue?) are related in
  spirit but distinct in mechanism; only the consented autopsy's *quality-audit* role is in scope.
- **The autopsy here is an audit concept, not a forensic act.** Only the consented autopsy's role
  as a clinicopathologic *quality audit* is in scope; cause/manner of death and any legal
  determination are out of scope (pillar 3).
- **The clinical care-system safety science is `clinical-medicine/11`.** The Swiss-cheese model,
  just culture, RCA, HRO, Donabedian, and PDSA are owned and taught there; `11` here applies them
  to the laboratory by reference and does not re-derive them.

---

## Resource, Geographic, and Bias Caveats

- **Quality-system infrastructure is not universal.** Formal QC programs, EQA/proficiency-testing
  schemes, accreditation bodies, information systems for traceability, and defined resilience
  pathways are concentrated in resourced settings; district and low-resource laboratories may run
  reduced QC, limited or no EQA, and manual traceability. The *reasoning* — control, external
  comparison, error taxonomy, governance — transfers; the available infrastructure does not, and the
  confidence placeable in "a result" depends on the surrounding system.
- **Accreditation standards and regulations differ by jurisdiction and era.** ISO 15189 and
  regional programs are named as *concepts*; specific editions, clauses, and legal requirements
  vary by country and change over time and must be confirmed against the issuing bodies, never
  taken from this reference as instructions.
- **QC and EQA benchmarks are population- and method-dependent.** Control limits derive from the
  **control material's** characterized behaviour in the laboratory (QC *planning* uses the `08 §2`
  performance figures); EQA peer groups are method-specific and often scored against a **consensus**
  rather than a reference value; and commutability of QC/EQA materials varies — so a QC or EQA
  judgment is evidence within its method and program context, not an absolute verdict.
- **Error-rate figures are setting-specific and definition-dependent.** As in `08`, the share of
  error attributed to each phase varies by setting, era, and how "error" is defined and counted;
  no phase fraction here is a universal constant.
- **Governance and safety judgments carry intrinsic variability.** What counts as "adequate"
  quality, an "acceptable" change, or a "competent" performer is a governed judgment with real
  variability; it is stated, not hidden, and the general safety-science framing behind it is
  `clinical-medicine/11`.
- **These cases and descriptions are illustrative and fictional.** Nothing here is a compliance
  step, an accreditation instruction, a runnable procedure, or a forensic/legal determination;
  every governance mechanism is described only as a concept and its purpose.
