---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-ACUTE-AND-CHRONIC-CARE.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:clinical-medicine:acute-and-chronic-care
kind: guide
module: clinical-medicine
section: clinical-medicine
title: Acute and Chronic Care - Two Control Logics for Managing Illness Over Time
status: source-custody
source_custody: partial
current_path: clinical-medicine/05-ACUTE-AND-CHRONIC-CARE.md
canonical_path: clinical-medicine/05-ACUTE-AND-CHRONIC-CARE.md
backsource_ids: [proof-backfill:clinical-medicine:05-acute-and-chronic-care]
concepts: [acute-care, chronic-care, illness-trajectory, chronic-care-model, triage-prioritization]
root_concepts: [care-architecture]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Acute and Chronic Care — Two Control Logics for Managing Illness Over Time

**This guide owns** the two fundamentally different **control logics** medicine uses to
manage illness across time: the **acute/undifferentiated** logic (time-critical
prioritization, stabilize-while-diagnosing, disposition) treated **conceptually as an
architecture**, and the **chronic/longitudinal** logic (continuity, trajectory management,
the Chronic Care Model). **It builds on** `02-DIFFERENTIAL-DIAGNOSIS` and `04-EVIDENCE-BASED-MEDICINE`
(the reasoning and evidence these care logics apply) and feeds `06-MULTIMORBIDITY-AND-GERIATRICS`
and `07-CARE-TRANSITIONS` (chronic complexity and the handoffs between the two logics). **It
explicitly defers** the *diseases* and their natural history to `disease/`; *drugs* to
`pharmacology/` (**no dosing**); *population prevention/health-system policy* to
`public-health/`; and — critically — **all emergency, first-aid, resuscitation, and
self-treatment technique** to trained clinical practice: this guide describes the *shape* of
acute prioritization, never how to perform it. This is a guide to *how care is organized over
time*, **not** a source of emergency instructions or self-management directions.

> **This module is an educational reference about *how clinical medicine reasons and
> how care is organized* — the cognitive and system architecture of the discipline.
> It is *not* medical advice. It does not diagnose, does not give treatment, dosing,
> or procedure instructions, does not give emergency or first-aid instructions, and
> is *not a substitute* for evaluation by a licensed clinician. Worked cases are
> illustrative teaching vignettes showing *how a clinician thinks*, not what any
> reader should do. For personal concerns, appropriate care comes from qualified
> local professionals; emergencies are handled through local emergency services.**

*Per-guide banner: educational reference on the architecture of acute and chronic care —
**not** emergency, first-aid, or self-treatment instructions. Acute content describes
prioritization concepts only; the operational execution is trained clinical work and is
deliberately out of scope.*

---

## The Big Picture: An Interrupt Handler and a Control Loop

The novice model is one undifferentiated "treatment." The expert model runs **two different
control systems** with opposite priorities. Acute care is an **interrupt handler**: a
deadline-driven, worst-case-first response that acts *before* a full diagnosis. Chronic care
is a **long-running control loop**: a setpoint-tracking, continuity-driven system that
manages a trajectory over years. Most patients move between the two, and the *handoff between
loops* is where much goes wrong (guide 07).

```
TWO CONTROL LOGICS  (this guide owns the shapes, not the clinical execution)
==========================================================================
  ACUTE / UNDIFFERENTIATED  (interrupt handler)     CHRONIC / LONGITUDINAL (control loop)
  --------------------------------------------      -------------------------------------
  trigger:  a new, time-critical problem            trigger:  an ongoing condition over time
  priority: WORST-CASE first (must-not-miss)        priority: track a SETPOINT / goal
  order:    STABILIZE, then diagnose (inverted)     order:    monitor -> adjust -> monitor
  horizon:  minutes to hours; hard deadlines        horizon:  months to years; continuity
  output:   a DISPOSITION (admit/observe/refer)     output:   a managed TRAJECTORY
  failure:  missing a time-critical threat          failure:  drift, gaps, fragmentation
  --------------------------------------------      -------------------------------------
             \                                              /
              \___ acute-on-chronic: the SAME patient _____/
                   crosses between loops (exacerbations);
                   the CROSSING is a care transition (guide 07)
==========================================================================
  Different objectives, different tempos, different failure modes. Confusing one logic
  for the other -- running chronic deliberation in an acute window, or acute reflexes in
  a chronic condition -- is itself an error.
```

**Bridge (software).** Acute care is an interrupt service routine / incident response: bounded
latency, mitigate-before-root-cause, keep the system alive while you debug. Chronic care is
steady-state SRE: a control loop with a setpoint, telemetry, and slow titration, plus
capacity planning against a predicted load curve (the trajectory). The two require different
skills, and the riskiest moment is the *context switch* between them.

---

## 1. The Acute Logic — Prioritization as Architecture (conceptual only)

> **Scope note.** This section describes the *conceptual structure* of acute prioritization —
> how the problem is framed and ordered — as system architecture. It gives **no** operational
> thresholds, maneuvers, first-aid, or resuscitation instructions. Executing acute care is
> trained clinical and emergency-services work; recognizing and acting on a real emergency is
> not something this reference guides. This is architecture, not a protocol.

Acute care inverts the normal diagnostic pipeline. In the ordinary flow (guides 01→04) a
clinician diagnoses, then acts. Under a time-critical threat, the order flips: a **parallel
stabilization track runs concurrently with diagnosis**, because some problems can cause harm
faster than a diagnosis can be established.

```
  THE ACUTE INVERSION  (conceptual)
  ----------------------------------------------------------------
  NORMAL:   gather -> differential -> test -> act        (guides 01-04)
  ACUTE:    [ stabilize the fastest-killing problem ]  ||  [ diagnose ]   <- concurrent
            worst-case-first, by SYNDROME, before a label exists
  ----------------------------------------------------------------
  The concept: address the problem with the shortest time-to-harm first, in parallel with
  working out what it is. This is a PRIORITIZATION ordering, described here as architecture,
  not a set of actions for any reader to take.
```

Four *conceptual* structures characterize the acute logic:

| Concept | What it means (architecturally) | Systems analog |
|---|---|---|
| **Triage** | order patients by **acuity, not arrival** — a priority queue | scheduling by severity, not FIFO |
| **Worst-case-first framing** | manage by the most dangerous plausible cause until excluded | fail-safe / defensive default |
| **Stabilize-then-diagnose** | keep physiology viable *while* the cause is worked out | mitigate before root-cause; keep the service up |
| **Disposition** | the routing decision: admit / observe / refer / discharge | request routing to the right tier (guide 08) |

**Triage as a priority queue.** The defining architectural feature of acute care is that it
serves a *queue ordered by acuity*. Named triage systems exist as frameworks — for example
the Emergency Severity Index (ESI), the Manchester Triage System, and, in mass-casualty
contexts, START — but this guide names them only as *examples of prioritization schemes*; it
does not reproduce their operational criteria, which are trained tools, not reader
instructions. The transferable idea is that acute systems **reorder work by time-to-harm**,
so the sickest are seen first even though they arrived last.

**Time-critical windows.** Some conditions have a **therapeutic window** in which outcome
degrades with delay ("time is tissue," in the shorthand). Architecturally this means the
acute loop is a *deadline scheduler*: the value of an action decays with time, so the system
is designed to compress the interval from presentation to decision. The *existence* of the
window is the concept this guide owns; *which* conditions have one, and what is done within
it, are clinical content (`disease/`, `medicine/`) and clinical execution — not here.

**Undifferentiated management.** Acute care frequently acts on a *syndrome* before a diagnosis
is established, carrying the must-not-miss list (guide 02) as the working frame and narrowing
as data arrive. The disposition — the acute loop's *output* — routes the patient to the tier
and loop that will carry them next (guide 08), which is itself a care transition (guide 07).

**Bridge (systems).** The acute logic is real-time incident response: a priority queue by
severity, deadline-aware scheduling, "keep it alive while you diagnose," and a routing
decision at the end. None of that tells anyone *how* to perform the mitigation — and neither
does this guide.

---

## 2. The Chronic Logic — Continuity and Control Over Years

Chronic care is the opposite discipline: not a bounded interrupt but an **open-ended control
loop** that tracks a condition over months to years. Its objective is not "resolve and
disposition" but "keep the trajectory acceptable," and its defining property is **continuity**
— the same informed relationship and durable record (the problem list, guide 07) persisting
across many encounters.

```
  THE CHRONIC CONTROL LOOP
  ----------------------------------------------------------------
        [ set goals with the patient ]  <-- values-driven setpoint (guide 09/10)
                    |
                    v
        [ monitor ] --> [ assess vs goal ] --> [ adjust the plan ] --+
            ^                                                         |
            +---------------------------------------------------------+
                    (repeat over months/years; the LOOP is the care)
  ----------------------------------------------------------------
  The care IS the loop, not any single visit. Continuity is what makes the loop stable;
  fragmentation (many uncoordinated visits, no owner) is what makes it drift.
```

The failure modes are the mirror image of acute care's: not "missed a fast threat" but
**drift** (silent trend away from goal), **gaps** (missed monitoring, lost follow-up), and
**fragmentation** (many hands, no integrator — guide 08). Because the loop runs for years, its
reliability depends less on any one clinician's brilliance and more on the *system* that keeps
the loop closing — which is exactly what the Chronic Care Model formalizes (Section 4).

**Self-management is part of the loop.** For most chronic conditions the patient performs the
majority of day-to-day management, so the chronic logic explicitly includes **self-management
support** — building the patient's capability and confidence to run their part of the loop.
This guide describes that as an *architectural element* of the model; it is not a set of
self-management instructions for any reader.

---

## 3. Illness Trajectories — The Predicted Load Curve

A **trajectory** is the expected shape of a condition's course over time. Thinking in
trajectories lets a clinician plan proactively — the chronic analogue of capacity planning
against a forecast load curve. A widely cited typology of end-of-life trajectories (Lynn &
Adamson, 2003; Murray et al., *BMJ* 2005) describes several characteristic shapes; the sociology
of "illness trajectories" (Glaser & Strauss) is older still. Presented conceptually:

```
  CHARACTERISTIC TRAJECTORY SHAPES  (function vs time; illustrative, conceptual)
  ----------------------------------------------------------------
  (a) SUDDEN         high, then an abrupt drop        ___________ |
                     (little warning)                            \|

  (b) STEADY-THEN-   preserved, then a short          ___________
      SHORT-DECLINE  steep terminal decline                      \____
                                                                      \

  (c) INTERMITTENT   sawtooth: exacerbations +        \/\  /\  /\
      DECLINE        partial recovery, drifting down      \/  \/  \___

  (d) SLOW           prolonged, gradual decline        ----____
      DWINDLING      from an already-low baseline              ----____
  ----------------------------------------------------------------
  Different shapes imply different care designs: (c) needs exacerbation planning and rescue
  pathways; (d) needs sustained support and anticipatory planning; (a) needs prevention +
  advance decisions. The shape is the FORECAST the chronic loop plans against.
```

The value of the trajectory frame is that it converts reactive care into **anticipatory**
care: knowing the likely shape, a team plans monitoring intervals, pre-commits to exacerbation
responses, and raises goals-of-care conversations (guide 10) *before* a crisis rather than
during one. The specific trajectory of any given condition is disease content (`disease/`);
the *use of trajectory thinking* to design care is what this guide owns.

**Bridge (systems).** A trajectory is a forecast load/reliability curve. Sawtooth decline (c)
is a system with recurring incidents and incomplete recovery each time (accreting damage);
slow dwindling (d) is gradual capacity loss; sudden (a) is a system that needs pre-provisioned
failover because there is no ramp. You plan monitoring and runbooks against the predicted
curve, not against yesterday's state.

---

## 4. The Chronic Care Model — Engineering the Loop for Reliability

The **Chronic Care Model (CCM)** (Wagner and the MacColl Institute, late 1990s; widely
disseminated c. 2001) is the canonical framework for making the chronic loop *reliably* close.
Its thesis: good chronic outcomes come not from heroic individual effort but from **productive
interactions between an informed, activated patient and a prepared, proactive care team**, and
that interaction has to be *engineered* by the system around it.

```
  CHRONIC CARE MODEL  (the system produces the productive interaction)
  ----------------------------------------------------------------
   HEALTH SYSTEM / ORGANIZATION  +  COMMUNITY RESOURCES        <- the context
        |                                    |
        v                                    v
   [ self-management ]  [ delivery-system ]  [ decision ]  [ clinical information ]
   [   support        ]  [   design         ]  [ support  ]  [   systems (registry) ]
        \                     |                   |                   /
         \____________________|___________________|__________________/
                                     v
        INFORMED, ACTIVATED PATIENT  <--productive interaction-->  PREPARED, PROACTIVE TEAM
                                     v
                            IMPROVED OUTCOMES
  ----------------------------------------------------------------
  Six elements; the two that most distinguish it from acute care are PROACTIVE (reach out
  before the crisis) and POPULATION/REGISTRY (manage the whole panel, not just who shows up).
```

The six elements (as architecture, not a to-do list):

| CCM element | What it provides | Systems analog |
|---|---|---|
| **Self-management support** | patient capability to run their part of the loop | empowering the on-call user; good runbooks |
| **Delivery-system design** | proactive, planned, team-based visits and roles | designing the process, not ad-hoc heroics |
| **Decision support** | evidence + guidelines embedded at the point of care | policy-as-code / linting at commit time |
| **Clinical information systems** | registries, reminders, feedback on the panel | dashboards + alerting over the fleet |
| **Health-system organization** | leadership, incentives aligned to chronic care | org design; SLOs that reward reliability |
| **Community resources** | linkage beyond the clinic walls | external dependencies wired in deliberately |

Two properties make the CCM the antidote to the chronic failure modes of Section 2:
**proactivity** (the team reaches out on a schedule rather than waiting for the patient to
present, closing the "gap" failure) and **population/panel management** (a registry tracks
*everyone* with the condition, not just who happens to book, closing the "drift" and
"fragmentation" failures). The financing and policy that enable or block the CCM are
`public-health/`'s territory; the *care-design logic* is this guide's.

**Bridge (software).** The CCM is the shift from reactive ops (fix what pages you) to
proactive SRE (error budgets, registries, scheduled reviews of the whole fleet, decision
support baked into the pipeline). "Manage the panel, not the visit" is "manage the fleet, not
the ticket."

**Resource and geographic caveat.** Both control logics here — acute worst-case-first
prioritization (§1) and the chronic monitor → adjust loop (§2, §4) — are described in a resourced
setting (continuous monitoring, a full registry, ready specialist access). The **logic is the
invariant; the instrumentation is not**. Where continuous monitoring, an electronic registry, or
on-site specialists are unavailable, the same architecture survives on a different mechanism:
triage by acuity still orders scarce attention, and the chronic loop still runs on **intermittent,
scheduled clinical checks, a paper or community-held register, and teleconsult or task-shifted
escalation** instead of telemetry and same-day referral. What changes is the sampling interval and
the escalation path, not the requirement to prioritize by acuity and to close the monitor-adjust
loop. Guide 08's alternate interface topologies (§7, §10) enumerate those low-resource shapes; this
module's care-architecture guides assume a resourced system and flag that assumption rather than
universalizing it.

---

## Fully Worked Case — Acute-on-Chronic, Crossing Between Loops (illustrative, fictional)

All details are invented to show the *care architecture*; nothing here is emergency, treatment,
or self-management advice. Clinical specifics are abstract (`disease/`, `pharmacology/`).

**Setup.** A fictional patient, **R**, has a chronic condition managed for years in the chronic
loop (Section 2): a values-based setpoint, scheduled monitoring, a registry entry, and
self-management support (Section 4). R's trajectory is the **intermittent-decline** shape (3c):
periodic exacerbations with partial recovery.

**Step 1 — an exacerbation triggers the acute loop (Section 1).** R develops a new,
time-sensitive worsening. This is an *interrupt*: the care logic switches from setpoint-tracking
to worst-case-first prioritization. Conceptually, an acute system would **triage** R by acuity
(not arrival), frame management around the must-not-miss possibilities (guide 02), and run
stabilization *concurrently* with working out the cause — all described here as architecture,
not as actions. (The actual recognition and handling of a real emergency is trained clinical
and emergency-services work, not something this guide directs.)

**Step 2 — disposition is a routing decision (Section 1 → guide 08).** The acute loop's output
is a **disposition**: the decision about which tier and which loop carries R next
(observe / admit / return to community management). That routing is a care-level decision
(guide 08) and a transition (guide 07).

**Step 3 — crossing back is the dangerous seam (guide 07).** As R stabilizes and re-enters the
chronic loop, the **context switch between loops** is where state is most often dropped — a new
plan, changed medications, and pending results must transfer without loss. This crossing is a
care transition, owned by guide 07; the acute-on-chronic pattern is precisely why guides 05 and
07 are read together.

**Step 4 — the trajectory is updated (Section 3).** The exacerbation is not just an event but
**information about the forecast**: an intermittent-decline trajectory that is exacerbating more
often signals drift, which the chronic loop uses to intensify monitoring, pre-commit an
exacerbation plan, and — proactively — open anticipatory goals-of-care discussion (guide 10)
before the next crisis rather than during it.

**What the case shows.** One patient, two control logics, and a transition between them: the
acute loop prioritized and dispositioned (conceptually), the chronic loop re-planned against an
updated trajectory, and the *crossing* was the point of maximum risk — the architecture this
guide owns, with the clinical execution deliberately left to trained practice.

---

## Reader Tasks (answerable from this guide)

1. **Contrast the two control logics.** Given a scenario, identify whether the acute
   (interrupt) or chronic (control-loop) logic applies, and name each one's objective, tempo,
   and characteristic failure mode. (Big Picture, §1–2.)
2. **Explain the acute inversion — conceptually.** Describe why acute care runs stabilization
   *concurrently with* diagnosis and how triage orders work by acuity rather than arrival,
   without stating any operational threshold or maneuver. (Section 1.)
3. **Match a trajectory shape to a care design.** Given a trajectory (sudden, steady-then-decline,
   intermittent decline, slow dwindling), describe what anticipatory care design it implies.
   (Section 3.)
4. **Map a scenario onto the Chronic Care Model.** Given a chronic-care failure (a missed
   follow-up, silent drift), name which CCM element addresses it and why proactivity and panel
   management are the distinguishing features. (Section 4.)
5. **Locate the risk in acute-on-chronic.** Given a patient crossing from the acute loop back to
   the chronic loop, explain why the *transition* is the point of maximum risk and which guide
   owns it. (Worked case → guide 07.)

---

## Decision Cheat Sheet

| Situation | What the care architecture does | Why (this guide) |
|---|---|---|
| A new time-critical problem | switches to the **acute loop**: worst-case-first, stabilize-while-diagnosing | some harms outpace diagnosis (§1) |
| Many patients, limited capacity | serves a **priority queue by acuity**, not arrival order | triage is severity scheduling (§1) |
| An ongoing condition over years | runs the **chronic control loop**: monitor → adjust → monitor | the loop *is* the care; continuity stabilizes it (§2) |
| Planning proactively | reasons from the **trajectory shape** (the forecast) | anticipatory care plans against the load curve (§3) |
| A chronic loop keeps drifting/gapping | applies **CCM** proactivity + registry/panel management | the system, not heroics, closes the loop (§4) |
| An acute event in a chronic patient | treats the **crossing between loops** as the key risk | acute-on-chronic transitions drop state (§0, guide 07) |
| A real emergency | **out of scope here** — trained clinical + emergency-services work | this guide is architecture, not instructions (banner) |

---

## Common Confusion Points

**"Acute and chronic care are just faster and slower versions of the same thing."** They are
*different control logics* with opposite objectives and failure modes. Acute care is worst-case-first,
stabilize-then-diagnose, disposition-driven; chronic care is setpoint-tracking, continuity-driven,
trajectory-managed. Running one's reflexes inside the other's window is an error.

**"This section will tell me what to do in an emergency."** It will not, by design. It describes
the *conceptual shape* of acute prioritization — triage as a priority queue, stabilize-while-diagnosing,
disposition — as architecture. It gives no thresholds, maneuvers, or first-aid, because executing
acute care is trained clinical and emergency-services work. Real emergencies are handled through local
emergency services.

**"Chronic care is just repeated acute visits."** No — the *loop is the unit of care*, not the visit.
Its reliability comes from continuity, proactivity, and panel management (the CCM), and its failure modes
are drift, gaps, and fragmentation — none of which a series of reactive visits addresses.

**"Trajectory thinking is just prognosis."** Prognosis estimates an outcome; *trajectory thinking* uses
the expected *shape* of decline to design care proactively — set monitoring intervals, pre-commit
exacerbation responses, and time anticipatory conversations. It is capacity planning against a forecast,
not a single prediction.

**"The Chronic Care Model is a checklist for a good visit."** It is a *system-design* framework: its
distinguishing features — proactivity and population/registry management — are about the machinery around
the interaction, not steps within one encounter. The financing that enables it belongs to `public-health/`;
the care-design logic belongs here.
