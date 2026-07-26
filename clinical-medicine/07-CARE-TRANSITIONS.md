---
maxim_schema: maxim.frontmatter.v1
id: maxim:clinical-medicine:care-transitions
kind: guide
module: clinical-medicine
section: clinical-medicine
title: Care Transitions - Handoffs as State Transfer Across Time and Teams
status: source-custody
source_custody: partial
current_path: clinical-medicine/07-CARE-TRANSITIONS.md
canonical_path: clinical-medicine/07-CARE-TRANSITIONS.md
backsource_ids: [proof-backfill:clinical-medicine:07-care-transitions]
concepts: [care-transitions, handoff, medication-reconciliation, problem-list, continuity-of-care]
root_concepts: [care-architecture]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Care Transitions — Handoffs as State Transfer Across Time and Teams

**This guide owns** the care transition treated as **state transfer**: the structured handoff
(**I-PASS**, **SBAR**), **medication reconciliation** as a list diff-and-merge, the
**discharge** as a high-risk serialization, the three types of **continuity**, the **problem
list as shared mutable state**, and the **closed-loop** discipline that keeps pending items from
being dropped. It also defines its own **ownership-field** discipline (Section 5), so it stands
alone. **It builds on** `05-ACUTE-AND-CHRONIC-CARE` (the crossings between care logics
are transitions). `08-SPECIALTY-INTERFACES` **reinforces** the same closed-loop and
ownership-field discipline across *services*; it is a companion, **not a prerequisite** — this
guide applies the discipline across *time and shifts* and defines the fields it needs locally.
**It explicitly defers** the *EHR/health-IT engineering* to `biomedical-engineering/` and
systems texts; the *drugs* to `pharmacology/` (**no dosing**); and the *diseases* to `disease/`.
This is a guide to *how patient state is moved without loss*, **not** instructions for
performing a handoff on a real patient and **not** medication advice.

> **This module is an educational reference about *how clinical medicine reasons and
> how care is organized* — the cognitive and system architecture of the discipline.
> It is *not* medical advice. It does not diagnose, does not give treatment, dosing,
> or procedure instructions, does not give emergency or first-aid instructions, and
> is *not a substitute* for evaluation by a licensed clinician. Worked cases are
> illustrative teaching vignettes showing *how a clinician thinks*, not what any
> reader should do. For personal concerns, appropriate care comes from qualified
> local professionals; emergencies are handled through local emergency services.**

*Per-guide banner: educational reference on how care transitions move patient state — not a
handoff procedure to perform and not medication guidance. Named tools (I-PASS, SBAR) are
described as communication schemas; any figure is illustrative and attributed.*

---

## The Big Picture: A Transition Is State Transfer Across a Boundary

The novice model treats a handoff as "telling the next person about the patient." The expert
model treats it as **serialize → transmit → deserialize → acknowledge** across a process
boundary — shift change, ward transfer, discharge, referral — where any dropped field is a
patient harm. Transitions are the single most error-prone moment in care precisely because they
are where state crosses a boundary and no single owner spans both sides.

```
A CARE TRANSITION IS A STATE TRANSFER  (this guide owns the transfer, not the clinical acts)
==========================================================================
  SENDER (context A)                                RECEIVER (context B)
     shift / ward / hospital / clinic                  next shift / ward / clinic / home
        |                                                        ^
        |  (1) SERIALIZE   compress state to a message           |
        |      structured: I-PASS / SBAR (Section 1)             |
        v                                                        |
     [ MESSAGE ] --(2) TRANSMIT--> [ MESSAGE ]                   |
        |                              |                         |
        |                              v                         |
        |                      (3) DESERIALIZE + read-back ------+  (4) ACKNOWLEDGE
        |                          receiver SYNTHESIZES back         the transfer COMMITS
        |                          (I-PASS "S")                      only on ACK, not on send
        v
   RECONCILE what crosses:  medications (Section 2) + problem list (Section 4)
   CLOSE every loop:        pending results/actions get a NAMED owner (Section 5)
==========================================================================
  Drop any step -> lost update, dropped message, or split-brain state. The transfer is not
  done when the sender speaks; it is done when the receiver acknowledges and owns.
```

**Bridge (software).** A transition is exactly cross-process state transfer with the same
failure modes: partial serialization (a field omitted), a dropped message (a verbal handoff no
one recorded), split-brain (two teams with divergent copies of the plan), and lost updates
(concurrent edits to the problem list). The fixes are the same: a structured schema (I-PASS/SBAR),
an explicit ACK (read-back), a merge protocol for shared state (medication reconciliation), and
no fire-and-forget (closed loops).

---

## 1. Structured Handoffs — I-PASS and SBAR

Unstructured handoffs lose information non-randomly: severity gets understated, contingencies go
unmentioned, and the receiver never confirms what they heard. Two schemas dominate.

**I-PASS** (Starmer et al., *NEJM* 2014 — a multi-center study that reported a substantial
reduction in medical errors and preventable adverse events after implementation) is a handoff
*bundle* whose five elements force the high-loss fields to be transmitted, ending with a
receiver **read-back**:

```
  I-PASS  (the receiver's synthesis is the ACK)
  ----------------------------------------------------------------
  I   Illness severity        one-word priority: how sick, how stable
  P   Patient summary         the compressed story + working diagnosis (guides 01-02)
  A   Action list             what to do, by when, by whom (the to-dos)
  S   Situation awareness     what MIGHT happen + contingency ("if X, then Y")
      + contingency planning
  S   Synthesis by receiver   RECEIVER restates it back  <-- the acknowledgment / commit
  ----------------------------------------------------------------
  The final S is the load-bearing step: without a read-back, the sender does not know the
  transfer landed. It is a two-phase commit -- the handoff commits on the receiver's ACK.
```

**SBAR** (originating in aviation/military crew communication, adapted to healthcare by Kaiser
Permanente) structures a single *message* — especially an urgent one — into four parts:

| SBAR | Content | Role |
|---|---|---|
| **S** — Situation | what is happening now, in one line | the headline |
| **B** — Background | the relevant context | the compressed history |
| **A** — Assessment | the sender's interpretation | the working diagnosis / concern |
| **R** — Recommendation | what the sender wants to happen | the explicit ask |

The key contrast: **SBAR structures the *message*** (concise, especially for an escalation call),
while **I-PASS structures the *handoff event*** (a full transfer of responsibility, with a
contingency plan and a read-back). Both exist to make the high-loss fields — severity,
contingencies, the explicit ask, and the acknowledgment — impossible to skip.

**Bridge (systems).** SBAR is a message schema (a well-defined log/alert format so the receiver
can parse it fast); I-PASS is a transfer *protocol* with an ACK and an explicit contingency
("if X then Y" is a runbook branch). The final "Synthesis by receiver" is the ACK that turns a
send into a committed transfer.

---

## 2. Medication Reconciliation — A List Diff-and-Merge

At every transition, the patient's medication list can silently diverge: a home drug is omitted
on admission, a hospital drug is unintentionally continued at discharge, or two sources disagree.
**Medication reconciliation** is the process of building the single most accurate list of what
the patient is *actually* taking and **comparing it against new orders at each transition** to
catch discrepancies. (The Joint Commission named it a National Patient Safety Goal in 2005,
signaling how error-prone transitions are for medications specifically.)

```
  MEDICATION RECONCILIATION = A THREE-WAY MERGE AT EACH TRANSITION
  ----------------------------------------------------------------
   SOURCE A: what the patient was taking (home / prior setting)
   SOURCE B: what is ordered now (this setting)
        |         |
        v         v
     [ DIFF ]  find discrepancies:
        - OMISSION    a needed drug dropped
        - DUPLICATION two entries for the same thing
        - CONFLICT    disagreeing entries (a classic drug-drug interaction, guide 06)
        - UNINTENDED  a temporary drug carried forward by accident
        |
        v
     [ RESOLVE ] each discrepancy explained + corrected, with a reason recorded
        |
        v
   RECONCILED LIST -> becomes SOURCE A for the NEXT transition
  ----------------------------------------------------------------
  The output of one merge is the input to the next; an unreconciled list propagates its
  errors through every downstream transition (diagnosis momentum for the med list).
```

Reconciliation is the medication-list analogue of a version-control merge: two sources, a diff,
a conflict-resolution step, and a committed result that becomes the new base. Its failure mode is
the *silent* discrepancy — an omission or an accidental continuation that no one notices because
no diff was run — which then flows through every subsequent transition. This guide owns
reconciliation as a *reasoning/process pattern*; the drugs and their interactions are
`pharmacology/`, and it is never a reader instruction to change a list.

**Bridge (software).** This is a three-way merge with conflict markers. Skip it and you get the
distributed-state classic: divergent replicas that never re-converge, each confidently wrong. The
reconciled list is the merged main branch; an unreconciled transition is a force-push that drops
commits.

---

## 3. Discharge and the Three Types of Continuity

**Discharge** is the highest-risk routine transition: the patient crosses from a high-monitoring
setting to a low-monitoring one, often with a changed plan, new medications, and *pending
results* (guide 5). The discharge summary is the **serialization** of the whole admission into a
message the next setting will deserialize — and its quality determines whether continuity
survives the boundary.

**Continuity** is not one thing. Haggerty, Reid, and colleagues (*BMJ* 2003) distinguish three
types, each of which a transition can break independently:

| Continuity type | What persists | How a transition breaks it |
|---|---|---|
| **Informational** | the *record* follows the patient (history, results, plan) | summary missing, results not forwarded |
| **Management** | a *coherent, consistent* plan across providers | conflicting plans, no reconciliation |
| **Relational** | an *ongoing personal relationship* with a clinician/team | patient loses their known clinician; no integrator |

```
  THREE CONTINUITIES  (a transition can sever any one)
  ----------------------------------------------------------------
   INFORMATIONAL  = shared source of truth (the record crosses the boundary)
   MANAGEMENT     = consistent policy across services (one coherent plan)
   RELATIONAL     = the same trusted operator (a durable relationship)
  ----------------------------------------------------------------
  Informational without management = accurate records, incoherent care.
  Management without relational = coherent care from strangers each time.
  A robust transition preserves all three; discharge most often severs informational
  (a result not forwarded) and management (an unreconciled, conflicting plan).
```

The discharge transition therefore has to carry *all three*: the record (informational), a single
coherent reconciled plan (management), and a named continuing owner/integrator (relational — often
primary care, guide 08). Pending tests at discharge are the specific, notorious failure: a result
that returns after the patient has left, with no owner to act on it — which is exactly the
closed-loop problem of Section 5.

**Bridge (systems).** Informational continuity is a shared source of truth (a consistent database
across nodes); management continuity is consistent policy applied across services (no contradictory
configs); relational continuity is sticky sessions to the same operator. Distributed systems need
all three too, and lose coherence when any is dropped at a boundary.

---

## 4. The Problem List as Shared Mutable State

The **problem list** is medicine's canonical shared state: the durable, authoritative
representation of a patient's active problems that every clinician reads and edits over time. It
is the single most important artifact for continuity — and, like any shared mutable state, it
degrades without discipline.

```
  THE PROBLEM LIST = A SHARED, LONG-LIVED SOURCE OF TRUTH
  ----------------------------------------------------------------
   properties it must maintain               failure if not
   -----------------------------             ------------------------------
   ACCURACY (reflects current reality)  ->   stale entries drive wrong decisions
   DEDUPLICATION (one entry per problem) ->  duplicates fragment the picture
   RESOLUTION (close inactive problems)  ->  a graveyard of resolved problems buries the active
   SHARED (one list, many editors)       ->  divergent private notes = split-brain
  ----------------------------------------------------------------
  The problem list is the PROBLEM REPRESENTATION (guide 01) made persistent and shared -- the
  compressed key that every downstream clinician reasons from. A corrupt list corrupts reasoning.
```

The problem list is the *persistent, multi-writer* version of guide 01's problem representation:
the compressed abstraction the whole team reasons from, but now shared and long-lived. Its
maintenance is a garbage-collection-and-consistency discipline — resolve inactive problems (free
the dead entries), deduplicate (one canonical entry per problem), and keep it accurate — because a
stale or duplicated list silently poisons every future decision and hardens errors across handoffs
(diagnosis momentum, guide 02).

**Bridge (software).** The problem list is a shared source-of-truth document with many concurrent
writers: it needs the equivalent of deduplication, garbage collection (closing resolved problems),
and consistency, or it rots into a split-brain of contradictory private copies. A well-groomed
problem list is a clean, canonical schema; a neglected one is an append-only log no one trusts.

---

## 5. Closed Loops — No Pending Item Without an Owner

The most dangerous transition defect is the **unowned pending item**: a test ordered in one
context whose result returns after the patient has moved, with no one responsible for
acknowledging and acting on it. Across *time and shifts* this closed-loop discipline is
identical to the one guide 08 applies across *services* and, if anything, more frequent here.

```
  THE CLOSED LOOP  (across time/shift boundaries; guide 08 applies the same shape across services)
  ----------------------------------------------------------------
  (1) an item is created (a pending test, a follow-up action, a contingency)
        |
        v
  (2) an OWNER is NAMED for it at the transition (not "whoever sees it")
        |
        v
  (3) the result/event arrives
        |
        v
  (4) the named owner ACKNOWLEDGES it
        |
        v
  (5) ACTION is taken (or explicitly declined) and RECORDED
  ----------------------------------------------------------------
  Break any arrow -> OPEN LOOP -> the classic missed-result event. Transitions open loops
  because the person who created the item is often not present when the result returns.
```

**Ownership is not one field.** The load-bearing rule is that **ownership of a pending item must
be *assigned*, not assumed** — and "ownership" is really **five distinct fields**, each of which
needs a named holder at every transition. Collapsing them into a single "who has the patient" is
the root of the "I thought *you* had it" failure:

| Ownership field | What it covers | Default holder (until an explicit, acknowledged handoff reassigns it) |
|---|---|---|
| **Overall-patient** | the whole person, integration, the problem list | the continuing integrator (usually primary care) |
| **Referred-problem** | a specific problem handed to another clinician/service for a defined scope | the originating team **until** an explicit contract for it is agreed and acknowledged |
| **Ordering** | who placed a given test/treatment order | whoever placed it — they own its consequences |
| **Pending-result** | who acknowledges a result that returns after the boundary | must be assigned explicitly at every transition |
| **Follow-up** | who acts on the result and closes the loop | named when the order is placed, never assumed |

Each field must have a named holder who **acknowledged** the duty; a send is not a transfer, and a
routing label moves nothing until the receiving owner explicitly accepts a named scope. The I-PASS
"Action list" and "contingency" elements (Section 1) exist to carry exactly these owned items
across the boundary, and the receiver's synthesis (the ACK) is what commits any ownership transfer.
Guide 08 uses the same five fields across service interfaces (referral, comanagement, transfer); a
reader who wants the cross-service version can go there, but this section is self-contained.

**Bridge (systems).** An open loop is a dropped callback / fire-and-forget async call whose response
no handler consumes. The fix is the same everywhere: register an owner before you issue the request,
and require an ACK that the response was consumed — never assume "someone will see it."

**Resource and geographic caveat.** The worked mechanics below assume a resourced setting (an EHR,
electronic result routing, a reachable primary-care integrator). The **invariants are
implementation-independent** and survive when those are absent: structured serialization
(I-PASS/SBAR), an explicit **acknowledgment**, medication reconciliation as a diff-and-merge, the
three continuities, and a **named-owner closed loop** hold just as firmly on a paper chart, over a
radio/phone handoff, or across a district-hospital, task-shifting, or teleconsult topology — only
the *mechanism* changes (a written tracking log instead of an electronic inbox; a community health
worker or on-call generalist instead of an on-site specialist as the named result owner). What
must never lapse regardless of resources is that **every pending item has a named owner who
acknowledged the duty**. Guide 08's alternate interface topologies (§7, §10) enumerate those
low-resource shapes and confirm the same discipline is required in each.

---

## Fully Worked Case — A Discharge Transition, Closed (illustrative, fictional)

All details are invented to show the *state-transfer mechanics*; nothing here is a handoff to
perform or medication guidance. Specifics are abstract (`pharmacology/`, `disease/`).

**Setup.** A fictional patient, **R**, is moving from a high-monitoring inpatient setting back to
community care — the discharge transition (Section 3). Sender: the inpatient team. Receiver: R's
primary-care integrator (guide 08) and R at home.

**Step 1 — serialize with structure (Section 1).** The inpatient team composes the handoff as
I-PASS: **I**llness severity (now stable), **P**atient summary (the compressed story + working
diagnosis, guides 01–02), **A**ction list (the pending items and to-dos), and **S**ituation
awareness/contingency ("if symptom X recurs, then Y"). For the urgent phone call to the receiving
clinician, the same content is delivered as SBAR (concise Situation/Background/Assessment/
Recommendation).

**Step 2 — reconcile the medications (Section 2).** The team runs a three-way merge of R's
pre-admission list against the discharge orders, and the diff surfaces a discrepancy: a medication
started temporarily inpatient would, if left unreviewed, be carried forward unintentionally
(and a home medication risks omission). Each discrepancy is resolved *with a recorded reason*, and
the reconciled list becomes the base for the next transition. (This is process reasoning, not a
directive to change any drug.)

**Step 3 — preserve all three continuities (Section 3).** The discharge summary carries the record
(informational); the reconciled single plan carries management continuity; and the named
integrator (relational) is explicitly identified as the continuing owner. No continuity is left to
chance.

**Step 4 — close the loops (Section 5).** A test was pending at discharge. Rather than "whoever
sees it," the transition **names** the pending-result owner and the follow-up owner, and the
receiver **acknowledges** the duty (the I-PASS synthesis). When the result returns after R is home,
a named owner acknowledges and acts — a closed loop, not the classic missed-result event.

**Step 5 — update the shared state (Section 4).** The problem list is groomed: resolved problems
are closed, duplicates merged, the active picture kept accurate — so R's next clinician reasons
from a clean, canonical representation, not a stale one.

**What the case shows.** State crossed the boundary intact because it was serialized with a schema,
acknowledged by the receiver, reconciled for medications, preserved across all three continuities,
and closed on every pending loop — the transfer discipline this guide owns, with the clinical acts
themselves left to trained practice.

---

## Reader Tasks (answerable from this guide)

1. **Choose and apply the right schema.** Given an urgent escalation call vs a full shift handoff,
   say whether SBAR or I-PASS fits and why, and identify the element that serves as the
   acknowledgment. (Section 1.)
2. **Run a reconciliation diff.** Given a pre-transition list and new orders, classify the
   discrepancies (omission, duplication, conflict, unintended continuation) and explain why the
   reconciled list becomes the base for the next transition. (Section 2.)
3. **Diagnose a severed continuity.** Given a discharge where records arrived but the plan was
   incoherent, name which continuity type broke (informational vs management vs relational) and
   how the transition should have carried it. (Section 3.)
4. **Groom a shared-state problem.** Given a problem list with stale and duplicated entries,
   explain how it corrupts downstream reasoning and what maintenance (resolution, deduplication)
   restores it. (Section 4.)
5. **Close an open loop.** Given a test pending at a transition, mark where the loop is open and
   assign — from the **five ownership fields defined in Section 5** (overall-patient,
   referred-problem, ordering, pending-result, follow-up) — the named owner and acknowledgment
   that closes it. (Section 5.)

---

## Decision Cheat Sheet

| Situation | What the transition does | Why (this guide) |
|---|---|---|
| Handing over responsibility at shift change | serializes with **I-PASS**, ending in receiver **read-back** | the ACK commits the transfer (§1) |
| Making an urgent escalation call | structures the message as **SBAR** | a parseable schema for a time-critical ask (§1) |
| Any transition touching medications | runs **reconciliation** (diff → resolve → commit) | silent discrepancies propagate downstream (§2) |
| Discharging to a lower-monitoring setting | carries record + coherent plan + named integrator | discharge severs continuity most often (§3) |
| Maintaining the shared picture | grooms the **problem list** (accurate, dedup, resolved) | it is the persistent representation all reason from (§4) |
| A test/action is pending at the boundary | assigns a **named owner** who acknowledges + acts | unowned pending items are the classic harm (§5) |
| "I told the next team" | treats the transfer as done only on **acknowledgment** | a send is not a commit (§1, §5) |

---

## Common Confusion Points

**"A handoff is just telling the next person about the patient."** It is *state transfer across a
boundary*, with the same failure modes as any cross-process transfer — omitted fields, dropped
messages, split-brain. Structured schemas (I-PASS/SBAR) and a receiver read-back exist because a
send is not a commit; the transfer lands only on acknowledgment.

**"Medication reconciliation is just copying the list."** It is a *diff-and-merge* at every
transition: build the true list, compare it to new orders, and resolve each discrepancy with a
recorded reason. Its dangerous failure is the *silent* omission or accidental continuation that no
diff caught, which then flows through every later transition.

**"Continuity means seeing the same doctor."** That is only *relational* continuity. Transitions can
also break *informational* continuity (the record doesn't follow) and *management* continuity (the
plan becomes incoherent) independently. A robust transition preserves all three.

**"The problem list is just documentation."** It is *shared mutable state* — the persistent problem
representation every clinician reasons from. Without deduplication, resolution of inactive problems,
and accuracy, it rots into a split-brain that silently corrupts downstream decisions.

**"Once the test is ordered, the result will get seen."** Only if the loop is closed. A result that
returns after the patient (or the ordering clinician) has moved, with no named owner to acknowledge
and act, is the classic missed-result harm. Ownership is assigned at the transition, never assumed —
and this guide describes that discipline, it does not instruct any reader to perform a handoff.
