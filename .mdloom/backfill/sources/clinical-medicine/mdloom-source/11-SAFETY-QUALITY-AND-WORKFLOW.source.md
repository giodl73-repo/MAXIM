---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "11-SAFETY-QUALITY-AND-WORKFLOW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:clinical-medicine:safety-quality-and-workflow
kind: guide
module: clinical-medicine
section: clinical-medicine
title: Safety, Quality, and Workflow - Systems-Based Practice
status: source-custody
source_custody: partial
current_path: clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW.md
canonical_path: clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW.md
backsource_ids: [mdloom-backfill:clinical-medicine:11-safety-quality-and-workflow]
concepts: [patient-safety, swiss-cheese-model, just-culture, donabedian, pdsa, diagnostic-safety]
root_concepts: [systems-based-practice]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Safety, Quality, and Workflow — Systems-Based Practice

**This guide owns** the **systems-based practice** of medicine: patient **safety** (the
Swiss-cheese model, error taxonomy, **just culture**, **RCA**, **HRO**), **quality** (Donabedian
**structure–process–outcome**, **PDSA** and the Model for Improvement, the Triple/Quadruple Aim),
**diagnostic safety** (guide 02's errors as a system problem), the **EHR order/result closed
loops**, and **team roles**. **It builds on** every prior guide — it is where their failure modes
are engineered against at the system level — and closes the module. **It explicitly defers** the
*engineering of medical devices and health-IT internals* to `biomedical-engineering/` and systems
texts; *population health-system policy/financing* to `public-health/`; and the *drugs/diseases* to
`medicine/`, `pharmacology/`, `disease/`. This is a guide to *how the care system is made safe and
improved*, **not** instructions for patient care and **not** medical advice.

> **This module is an educational reference about *how clinical medicine reasons and
> how care is organized* — the cognitive and system architecture of the discipline.
> It is *not* medical advice. It does not diagnose, does not give treatment, dosing,
> or procedure instructions, does not give emergency or first-aid instructions, and
> is *not a substitute* for evaluation by a licensed clinician. Worked cases are
> illustrative teaching vignettes showing *how a clinician thinks*, not what any
> reader should do. For personal concerns, appropriate care comes from qualified
> local professionals; emergencies are handled through local emergency services.**

*Per-guide banner: educational reference on the systems architecture of patient safety and quality
— not patient-care instructions. Frameworks and any figures are attributed and dated as
illustrations; safety statistics are cited to their source reports.*

---

## The Big Picture: Safety Is a System Property, Not a Character Trait

The novice model blames the person at the sharp end ("who made the mistake?"). The expert model,
established by the IOM report *To Err Is Human* (1999), is that **most harm comes from system
design, not bad individuals**, and that the same competent person will err at predictable rates
unless the system is engineered to catch and absorb those errors. *To Err Is Human* estimated (its
figure, dated 1999, and debated since) that on the order of **44,000–98,000** U.S. deaths per year
were attributable to preventable medical error — the number that launched the field. The response
is not exhortation but **systems engineering**: layered defenses, blameless-but-accountable
learning, measurement, and iterative improvement.

```
SYSTEMS-BASED PRACTICE  (this guide owns the system, not the individual bedside act)
==========================================================================
  SAFETY (prevent + learn from harm)          QUALITY (measure + improve)
  -----------------------------------          ---------------------------
  Swiss-cheese layered defenses (Sec 1)        Donabedian structure/process/outcome (Sec 5)
  error taxonomy (Sec 2)                       PDSA / Model for Improvement (Sec 6)
  just culture (Sec 3)                         Triple / Quadruple Aim (Sec 6)
  RCA (learn) + HRO (stay alert) (Sec 4)
        \                                              /
         \____ the WORKFLOW that carries both ________/
              diagnostic safety (Sec 7) + EHR order/result loops (Sec 8) + teams (Sec 9)
==========================================================================
  Errors are predictable, so the durable fix is a designed system -- defense in depth, blameless
  learning, measurement, and iteration -- not "try harder." Blame is the enemy of learning.
```

**Bridge (software).** This entire guide is SRE and reliability engineering applied to care:
defense-in-depth (Swiss cheese), blameless postmortems with accountability (just culture),
root-cause analysis and threat modeling (RCA/FMEA), a reliability culture (HRO ≈ chaos-engineering
mindset), observability layered as structure/process/outcome (Donabedian), and iterative change
(PDSA ≈ hypothesis-driven deployment). Anyone who has run an incident review will recognize the
shape; medicine adds the constraint that the "service" is a person.

---

## 1. The Swiss-Cheese Model — Defense in Depth

Reason's **Swiss-cheese model** (James Reason, 1990s) is the founding metaphor: a system's defenses
are layers of cheese, each with holes; harm occurs only when the holes in *every* layer momentarily
line up so a hazard passes all the way through. Two failure types create the holes:

```
  THE SWISS-CHEESE MODEL  (harm passes only when holes ALIGN)
  ----------------------------------------------------------------
   hazard --> [ layer 1 ] [ layer 2 ] [ layer 3 ] [ layer 4 ] --> HARM
                 O   O        O            O   O        O
                  \           |            /
                   `---- holes align ------'   (a rare, correlated alignment)
  ----------------------------------------------------------------
   ACTIVE failures:  the sharp-end slip/mistake, immediate, visible (Section 2)
   LATENT conditions: the blunt-end holes -- design, staffing, defaults, culture -- dormant,
                      built in long before, waiting for an active failure to line up with them
  ----------------------------------------------------------------
  Blaming the sharp end (the active failure) leaves every LATENT hole in place, so the next
  person hits the same aligned holes. The fix is closing holes, especially latent ones.
```

The load-bearing distinction is **active vs latent**: the frontline "error" is usually the *last*
hole, not the cause; the causes are the **latent conditions** (understaffing, confusing defaults,
missing forcing functions, production pressure) built into the system upstream at the "blunt end."
This is why safety work targets the *layers*, not the last person to touch the patient.

**Bridge (systems).** This is defense-in-depth with the correlated-failure caveat: independent
controls each catch most faults, and a breach requires simultaneous holes — so the real danger is
*common-mode* failure (one latent condition that punches a hole in several layers at once). Blaming
the on-call engineer for the last click leaves the latent misconfig that will re-fire tomorrow.

---

## 2. Error Taxonomy — Naming the Failure Precisely

> **Boundary — clinical application vs generic science.** This guide owns the **clinical**
> patient-safety practice: applying error taxonomy, just culture, RCA, and HRO to diagnosis,
> treatment, medication, and clinical workflow. The **generic human-factors science** these
> rest on is owned by human factors:
> [`human-factors/04-HUMAN-ERROR-TAXONOMIES`](../human-factors/04-HUMAN-ERROR-TAXONOMIES.md)
> (slips/lapses/mistakes, SRK, violations, latent conditions, error-as-a-systems-property)
> and [`human-factors/11-ORGANIZATIONAL-SAFETY-CULTURE`](../human-factors/11-ORGANIZATIONAL-SAFETY-CULTURE.md)
> (just culture, HRO, Safety-I/II, reporting, normalization of deviance). Both cite Reason
> from different ownership; the clinical *application* is this guide's, the general *model* is
> human factors'.

Improving safety requires classifying failures precisely, because different error types need
different fixes. Reason's taxonomy (from the skill/rule/knowledge performance framework) separates
*execution* failures from *planning* failures:

```
  ERROR TAXONOMY  (execution vs planning -- they need different fixes)
  ----------------------------------------------------------------
  SLIPS + LAPSES  (execution failure: RIGHT plan, WRONG execution)
     slip  = attentional (did the wrong action)   -> fix with forcing functions, design
     lapse = memory (omitted a step)              -> fix with checklists, reminders
  MISTAKES  (planning failure: WRONG plan, executed faithfully)
     rule-based      = applied a wrong/mis-fitting rule  -> fix with training, decision support
     knowledge-based = wrong reasoning in a novel case   -> fix with expertise, consultation
  ----------------------------------------------------------------
  Slips are failures of a good plan; mistakes are failures OF the plan. A checklist fixes a lapse,
  not a knowledge-based mistake -- matching the fix to the type is the whole point of classifying.
```

A second axis names *what reaches the patient* — and cleanly separates **error** from **harm**:

| Term | Meaning | Key point |
|---|---|---|
| **Near-miss / close call** | an error caught before reaching the patient | free lessons; the richest safety data |
| **Adverse event** | harm from care (not necessarily from error) | some harm is non-preventable |
| **Preventable adverse event** | harm from an error | the target of safety work |
| **Error (no harm)** | a mistake that reached the patient without harming | still a system signal |

The critical decouplings: **harm is not the same as error** (some adverse events are unavoidable;
some errors cause no harm), and **near-misses are the most valuable data** because they reveal an
aligned-holes pathway *without* a patient being hurt — the reason a healthy safety system works hard
to *surface* them (which requires the reporting culture of Section 3).

**Bridge (systems).** Slips are typos and fat-finger deploys (fix with linting, guardrails, "are you
sure?" forcing functions); mistakes are wrong designs (fix with review and expertise). A near-miss is
an averted incident — the caught exception you learn from before it pages — which is why mature teams
mine them instead of only counting outages.

---

## 3. Just Culture — Blameless, But Accountable

For a system to learn, people must *report* errors and near-misses — and they will not if reporting
gets them punished. **Just culture** (Reason; operationalized by David Marx) resolves the tension
between "no blame" and "accountability" by distinguishing the *behavior*, not the *outcome*:

```
  JUST CULTURE  (judge the BEHAVIOR, not the outcome)
  ----------------------------------------------------------------
   HUMAN ERROR      inadvertent slip/lapse         -> CONSOLE + fix the system (Section 1-2)
   AT-RISK BEHAVIOR drifted from safe practice,     -> COACH + remove the incentive to drift
                    risk not recognized
   RECKLESS BEHAVIOR conscious disregard of a        -> ACCOUNTABLE (disciplinary)
                    substantial, unjustifiable risk
  ----------------------------------------------------------------
  Same bad outcome can arise from any of the three; the RESPONSE depends on the behavior that
  produced it, NOT on how badly it turned out. Punishing human error just drives it underground.
```

The core move is **outcome-independence**: an identical bad outcome warrants a different response
depending on whether it arose from unavoidable human error (console and fix the system), at-risk
behavior (coach and remove the drift incentive), or reckless disregard (hold accountable). Just
culture is therefore **not** "blame-free" — it is *fair*: it protects honest error reporting while
still holding recklessness to account, and it is the cultural precondition for every learning system
in this guide.

**Bridge (systems).** This is the blameless-postmortem principle with its usual caveat: blameless
does *not* mean consequence-free for reckless action; it means you do not punish the predictable human
error that a bad system invited, because doing so destroys the reporting you depend on to find the
latent holes.

---

## 4. Learning and Staying Alert — RCA and HRO

**Root cause analysis (RCA)** is the structured *retrospective* investigation of a serious event to
find its systemic contributors rather than a scapegoat. Techniques include the **"5 Whys"** (iterate
"why?" past the proximate cause to the latent conditions) and the **fishbone / Ishikawa** diagram
(enumerate contributing-factor categories). Modern practice (the "RCA2" refinement) insists the
analysis end in *specific, assigned, verifiable actions* — a finding with no owned action is an open
loop (guide 07).

```
  RCA: PAST-FACING (learn from an event)   |   FMEA: FUTURE-FACING (find risk first)
  --------------------------------------   |   -----------------------------------
  event -> "5 whys" past the sharp end     |   map a process -> for each step, ask
        -> contributing factors (fishbone) |   how could it fail, how bad, how likely,
        -> SYSTEM causes (latent holes)     |   how detectable -> prioritize + mitigate
        -> assigned, verifiable ACTIONS     |   (a prospective threat model)
  --------------------------------------   |   -----------------------------------
  RCA is the postmortem; FMEA is the pre-mortem. Both target latent conditions (Section 1).
```

**High Reliability Organizations (HRO)** (Weick & Sutcliffe, ~2001/2007) describe how industries with
catastrophic-failure potential (aviation, nuclear, aircraft carriers) stay safe despite complexity —
by cultivating a state of collective mindfulness with five principles:

| HRO principle | What it means | Systems analog |
|---|---|---|
| **Preoccupation with failure** | treat small signals as warnings; chase near-misses | watch weak signals; mine near-misses |
| **Reluctance to simplify** | resist easy explanations; probe deeper | don't paper over anomalies |
| **Sensitivity to operations** | maintain situational awareness at the front line | observe the running system, not the diagram |
| **Commitment to resilience** | build capacity to detect, contain, recover | graceful degradation; practiced recovery |
| **Deference to expertise** | decisions migrate to whoever knows most, not rank | escalate to the expert, not the org chart |

RCA/FMEA are the *tools*; HRO is the *culture* that keeps using them when nothing is currently on
fire — the difference between running one postmortem and being a reliability-minded organization.

---

## 5. Donabedian — Measuring Quality as Structure, Process, Outcome

You cannot improve what you cannot measure, and the canonical model for *what* to measure is
Donabedian's **structure–process–outcome (SPO)** framework (Avedis Donabedian, 1966):

```
  DONABEDIAN SPO  (three layers of quality measurement)
  ----------------------------------------------------------------
  STRUCTURE   the setting + resources: staffing, equipment, systems, training
                -> "do we have what good care requires?"    (necessary, not sufficient)
  PROCESS     what is actually DONE: the care delivered vs what should be
                -> "are we doing the right things right?"    (actionable, but a proxy)
  OUTCOME     what RESULTS for patients: mortality, function, experience, harm
                -> "did patients end up better?"             (what matters; hard to attribute)
  ----------------------------------------------------------------
  Structure enables Process enables Outcome. Outcomes are the goal but are noisy and slow and need
  risk-adjustment; process measures are faster and more actionable but only matter if linked to
  outcomes. Good measurement uses all three deliberately.
```

The reasoning discipline is knowing each layer's trade-off: **outcomes** are what ultimately matter
but are slow, noisy, multi-causal, and demand risk-adjustment (a good outcome can follow bad care and
vice versa); **process** measures are timely and actionable but only count if genuinely linked to
outcomes (a process measure divorced from outcomes is Goodhart bait, guide 04); **structure** is a
necessary enabler but far from sufficient. Balanced measurement spans all three.

**Bridge (systems).** SPO maps onto observability layers: structure is the infrastructure/capacity you
provisioned, process is the traces of what actually ran, outcome is the user-facing SLI. Optimizing a
process metric with no outcome linkage is optimizing a vanity dashboard; watching only outcomes is
slow and hard to attribute — you need all three.

---

## 6. Improving — PDSA and the Aims

Measurement feeds **improvement**. The dominant method is the **Model for Improvement** (Associates in
Process Improvement; disseminated by the IHI), which pairs three questions with **PDSA** cycles
(Plan–Do–Study–Act, descended from Shewhart/Deming):

```
  MODEL FOR IMPROVEMENT + PDSA
  ----------------------------------------------------------------
  Three questions:
     1 what are we trying to accomplish?   (aim)
     2 how will we know a change is an improvement?  (measure -- Section 5)
     3 what change might we test?           (idea)
  then iterate PDSA:
     PLAN  a small test of change + prediction
     DO    run it on a small scale
     STUDY compare results to the prediction (run charts / SPC over time)
     ACT   adopt / adapt / abandon -> next cycle
  ----------------------------------------------------------------
  Small, fast, iterative tests beat big-bang rollouts: you learn from each cycle and limit blast
  radius. Run charts track change over time and separate signal (real shift) from noise.
```

The purpose these serve is captured by the **Triple Aim** (IHI; Berwick, Nolan & Whittington, 2008):
better *care experience*, better *population health*, and lower *per-capita cost* — later extended to
the **Quadruple Aim** (Bodenheimer & Sinsky, 2014) by adding *care-team wellbeing*, on the recognition
that a burned-out workforce cannot deliver the other three (the treatment-burden logic of guide 06
applied to clinicians). PDSA is the engine; the Aims are the objective it optimizes toward.

**Bridge (systems).** PDSA is hypothesis-driven, incremental deployment: small experiment, measure
against a prediction, iterate, keep the blast radius small — canary releases and A/B tests with run
charts instead of dashboards. The Quadruple Aim's fourth element is the SRE lesson that on-call
burnout is a reliability risk, not a soft concern.

---

## 7. Diagnostic Safety — Guide 02's Errors as a System Problem

Historically, safety work focused on *treatment* errors (medications, procedures, surgery) and
under-attended **diagnostic** error. The NASEM report *Improving Diagnosis in Health Care* (2015,
introduced in guide 02) reframed diagnostic error as a **system safety domain**: its contributors are
cognitive **and** system **and** communication, so its fixes belong here as much as in the individual
reasoning of guide 02.

```
  DIAGNOSTIC SAFETY  (guide 02's cognition + this guide's systems)
  ----------------------------------------------------------------
  cognitive contributors (guide 02)   -> debiasing, calibration, forcing functions
  system contributors (this guide)    -> workload/fatigue, teamwork, health-IT (Section 8),
                                          time pressure, follow-up loops (Section 8)
  communication contributors (guide 07) -> handoffs, transmit uncertainty, result loops
  ----------------------------------------------------------------
  A large share of diagnostic error is the aligned-holes pattern (Section 1): a cognitive slip
  meeting a latent system hole (no result follow-up, a rushed handoff). The fix spans all three.
```

The transferable point: diagnostic safety cannot be solved by "think better" alone (guide 02's own
conclusion). It requires the *system* — measuring diagnostic performance, building outcome-feedback
loops so clinicians learn their calibration (guide 02, Section 5), and closing the result loops of
Section 8 — combined with the cognitive guardrails. It is the clearest place where the whole module
converges: guides 01–04 (cognition) meet guide 07 (communication) meet this guide (system).

---

## 8. The EHR and the Order/Result Closed Loops

The electronic health record is both a major safety *tool* and a major safety *hazard*, and it is
where many latent holes now live. The safety-critical loops it mediates:

| Mechanism | What it does | Safety role / hazard |
|---|---|---|
| **CPOE** (computerized order entry) | orders entered directly, legibly, structured | removes handwriting/transcription errors; can introduce new slip patterns |
| **Clinical decision support (CDS)** | alerts, reminders, order sets at the point of care | catches interactions/omissions; **alert fatigue** if over-fired |
| **Closed-loop result management** | ensures every result reaches an owner who acts | prevents the unowned pending result (guides 07/08); the classic latent hole |
| **Interoperability** | records cross settings | informational continuity (guide 07); fragmentation if broken |

```
  THE RESULT LOOP  (the latent hole that safety systems must close)
  ----------------------------------------------------------------
   order placed -> test performed -> result returns -> [ NAMED OWNER acknowledges ] -> ACT / record
                                                              ^
                                                              |
                              if no owner is assigned here, the loop is OPEN -> missed result
  ----------------------------------------------------------------
  Same closed-loop invariant as guides 07 and 08. The EHR can CLOSE this loop (route to an owner,
  track acknowledgment) or LEAVE it open (a result in an unmonitored inbox). Design decides which.
```

Two design lessons: **alert fatigue** is a real hazard — over-firing CDS trains clinicians to
dismiss alerts, so the signal-to-noise of alerting is itself a safety parameter (the pager-fatigue
problem); and **closed-loop result management** is the technical expression of guide 07/08's invariant
— the EHR is where "every pending result has a named owner who acknowledges and acts" is either
enforced or quietly abandoned. The *engineering* of these systems is `biomedical-engineering/`; their
*safety logic* is owned here.

**Bridge (systems).** CDS is policy-as-code / linting at commit time — invaluable until it cries wolf
so often it is muted (alert fatigue = ignored pagers). Closed-loop result management is guaranteed
callback delivery with an ACK; an unmonitored results inbox is a dropped-callback dead-letter queue no
one drains.

**Resource and geographic caveat.** This section describes the safety loops as an EHR mediates them,
but the **EHR is one implementation of the invariants, not the invariants themselves**. The
load-bearing properties survive without an EHR, CPOE, continuous monitoring, or on-site specialists:
**defense in depth** (§1), **just culture** and honest **reporting** (§3, §9), **measurement** as
structure/process/outcome (§5), and above all the **named-owner closed loop** (§8) hold on a paper
chart with a manual result log, on intermittent clinical checks instead of continuous telemetry, and
with a teleconsult or task-shifted generalist rather than an on-site specialist as the named owner.
What changes across settings is the *mechanism* (a written tracking book instead of CDS; a scheduled
check instead of a monitor; a hub-and-spoke escalation instead of a local consult), never the
requirement that every pending result and every defense have an owner. Guide 08's alternate interface
topologies (§7, §10) enumerate those low-resource shapes and confirm the same discipline is required
in each; this guide's system models assume a resourced setting and flag that assumption rather than
universalizing it.

---

## 9. Team Roles and the Culture That Enables Reporting

Care is delivered by **interprofessional teams**, and most latent holes are *coordination* failures.
Structured teamwork frameworks (for example **TeamSTEPPS**, from AHRQ and the U.S. Department of
Defense, adapted from aviation **crew resource management**) train explicit communication, mutual
monitoring, and role clarity — the same crew-resource ideas behind SBAR/I-PASS (guide 07).

The precondition for all of it is **psychological safety** (Amy Edmondson, 1999): a shared belief that
speaking up — reporting an error, questioning a superior, flagging a concern — will not be punished.
Without it, near-misses go unreported (Section 2 loses its richest data), hierarchy suppresses the
"deference to expertise" that HRO requires (Section 4), and just culture (Section 3) is words on a
poster. Checklists (the Pronovost central-line work; Gawande's *Checklist Manifesto*) are the concrete
artifact that encodes team steps and flattens hierarchy at critical moments — but a checklist only
works inside a culture that lets a junior member halt the line.

```
  THE CULTURE STACK  (each layer needs the one below it)
  ----------------------------------------------------------------
   improvement (PDSA) + learning (RCA/HRO)      <- needs data
        ^
   error + near-miss REPORTING                  <- needs people to speak up
        ^
   JUST CULTURE (fair, not blame-free)          <- needs trust
        ^
   PSYCHOLOGICAL SAFETY (speaking up is safe)   <- the foundation
  ----------------------------------------------------------------
  Every safety system above rests on people reporting what went wrong. Blame collapses the stack.
```

**Bridge (systems).** Psychological safety is the blameless-culture foundation that makes incident
reporting honest; TeamSTEPPS/CRM is structured on-call communication; a checklist is a shared runbook
that anyone — regardless of seniority — is empowered to invoke to stop an unsafe action.

---

## Fully Worked Case — Analyzing an Event and Improving the System (illustrative, fictional)

All details are invented to show the *systems reasoning*; nothing here is patient-care guidance.
Specifics are abstract.

**Setup.** A fictional preventable adverse event occurs: a test result returned after a care
transition and was not acted on in time (an open result loop, Section 8).

**Step 1 — Swiss-cheese analysis (Section 1).** The investigation maps the layers whose holes aligned:
an **active** failure (a busy clinician did not see the result) meeting **latent** conditions (no
assigned pending-result owner at the transition, an unmonitored results inbox, and production pressure)
— the harm required all of them, not the last click.

**Step 2 — classify the error (Section 2).** The frontline failure is a **lapse** (a memory/attention
omission under load), not a reckless act — and there were prior **near-misses** on the same pathway
that had gone unreported.

**Step 3 — apply just culture (Section 3).** Because the behavior was human error / at-risk drift, the
response is to **console and fix the system**, not to discipline — and to ask why the near-misses were
never reported (a psychological-safety gap, Section 9), since punishing the lapse would only bury the
next one.

**Step 4 — RCA to assigned actions (Section 4).** A "5 Whys" walks past the sharp end to the latent
holes and ends in **specific, owned, verifiable actions**: assign a pending-result owner at every
transition (guides 07/08) and route results to a monitored, acknowledged queue (Section 8) — not a
finding without an owner.

**Step 5 — measure and improve (Sections 5–6).** A Donabedian **process** measure (percentage of
results with a documented acknowledging owner) and an **outcome** measure (missed-result events) are
defined, and a **PDSA** cycle tests the closed-loop result-management change on a small scale, tracked
on a run chart, before spread.

**Step 6 — sustain via culture (Sections 4, 9).** The organization treats the near-miss data as a
warning (HRO preoccupation with failure) and reinforces psychological safety so the *next* aligned-holes
pathway is reported before it causes harm.

**What the case shows.** An event analyzed as a system (aligned holes, error type, just-culture
response), learned from via RCA with owned actions, measured with SPO, improved via PDSA, and sustained
by an HRO/psychological-safety culture — the systems-based practice this guide owns, converging the
cognition of guide 02, the transitions of guide 07, and the interfaces of guide 08.

---

## Reader Tasks (answerable from this guide)

1. **Analyze an event with Swiss cheese.** Given a fictional adverse event, separate the active
   failure from the latent conditions and explain why blaming the sharp end leaves the system unsafe.
   (Section 1.)
2. **Classify an error and match the fix.** Given a failure, decide whether it is a slip, lapse,
   rule-based, or knowledge-based mistake, and name a fix that matches the type (and why a checklist
   fixes a lapse but not a knowledge-based mistake). (Section 2.)
3. **Apply just culture.** Given the *same* bad outcome from human error, at-risk behavior, and
   recklessness, assign the correct response to each and explain why the response is outcome-independent.
   (Section 3.)
4. **Design a balanced measure set.** For a quality goal, propose a structure, a process, and an
   outcome measure, and state each one's trade-off (Donabedian). (Section 5.)
5. **Close a result loop with PDSA.** Given an open EHR result loop, name the closed-loop fix and design
   a PDSA cycle (with a process and outcome measure) to test it before spread. (Sections 6, 8.)

---

## Decision Cheat Sheet

| Situation | What systems-based practice does | Why (this guide) |
|---|---|---|
| Harm occurs | analyzes **aligned holes** (active + latent), not the last person | safety is a system property (§1) |
| Classifying a failure | separates **slip/lapse** (execution) from **mistake** (planning) | the fix depends on the type (§2) |
| Responding to an error | applies **just culture**: console / coach / hold accountable by *behavior* | blame kills the reporting you need (§3) |
| Learning from an event | runs **RCA** to owned, verifiable actions; stays alert via **HRO** | latent holes recur until closed (§4) |
| Measuring quality | uses **structure + process + outcome** deliberately | each layer has a distinct trade-off (§5) |
| Making a change | tests it with **PDSA**, tracked on a run chart, toward the Aims | small iterative tests beat big-bang (§6) |
| A diagnostic error | treats it as **cognitive + system + communication** | NASEM: fixes span guides 02/07/11 (§7) |
| A result may be unacted-on | closes the **EHR result loop** to a named owner | the unowned pending result is the classic hole (§8) |
| Near-misses go unreported | builds **psychological safety** + just culture | the whole safety stack rests on reporting (§9) |

---

## Common Confusion Points

**"Find who made the mistake."** That is the failure mode the field was founded to escape. Most harm
comes from *system* design (latent conditions), and the sharp-end error is usually the last hole, not
the cause. Blaming the individual leaves every latent hole in place for the next person.

**"Just culture means no one is ever blamed."** No — just culture is *fair*, not blame-free. It consoles
honest human error and coaches at-risk drift (both system problems) but still holds *reckless* disregard
accountable. The response depends on the behavior, not on how badly the outcome turned out.

**"Harm means someone erred, and an error means harm."** Both false. Some adverse events are
non-preventable (harm without error); some errors reach the patient without harming, and near-misses are
errors caught before harm — and they are the *most valuable* safety data precisely because no one was
hurt.

**"Outcome measures are the only quality that matters."** Outcomes are the goal but are slow, noisy, and
multi-causal, needing risk-adjustment. Process measures are timely and actionable but only count if
linked to outcomes; structure is a necessary enabler. Balanced measurement uses all three (Donabedian),
and a process metric divorced from outcomes is Goodhart bait.

**"More alerts and more EHR mean more safety."** Only up to a point. Over-firing decision support causes
**alert fatigue** — clinicians learn to dismiss alerts, muting the real ones — so alert signal-to-noise
is itself a safety parameter. The EHR closes result loops *or* leaves them open depending on design; it
is a tool and a hazard at once.
