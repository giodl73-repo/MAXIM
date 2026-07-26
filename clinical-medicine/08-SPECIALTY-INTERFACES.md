---
maxim_schema: maxim.frontmatter.v1
id: maxim:clinical-medicine:specialty-interfaces
kind: guide
module: clinical-medicine
section: clinical-medicine
title: Specialty Interfaces - The Care System as a Service Catalog
status: source-custody
source_custody: partial
current_path: clinical-medicine/08-SPECIALTY-INTERFACES.md
canonical_path: clinical-medicine/08-SPECIALTY-INTERFACES.md
backsource_ids: [proof-backfill:clinical-medicine:08-specialty-interfaces]
concepts: [specialty-interfaces, care-levels, referral, consultation, comanagement, closed-loop-followup, practice-variation]
root_concepts: [care-architecture]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Specialty Interfaces — The Care System as a Service Catalog

**This guide owns** the specialty map treated as an **interface / service catalog**:
the division of cognitive labor between generalists and specialists, the
primary/secondary/tertiary/quaternary **care levels**, the anatomy of a good
**consultation question**, the ownership semantics of **referral vs consultation vs
comanagement vs transfer**, scope/result-follow-up and the **closed-loop
consultation**, resource/geographic **practice variation**, and **multi-specialty
conflict resolution**. **It builds on** `02-DIFFERENTIAL-DIAGNOSIS` and
`03-DIAGNOSTIC-TEST-INTERPRETATION` (the undifferentiated→differentiated funnel that
generates referrals) and `07-CARE-TRANSITIONS` (handoffs as information transfer).
**It explicitly defers** the *diseases themselves* — mechanisms, catalogs, natural
history — to `disease/`; organ-system anatomy/physiology to `human-biology/`; drug
classes and diagnostic/imaging catalogs to `medicine/`+`pharmacology/`; and
**health-system typology, financing, and workforce policy** (Bismarck/Beveridge,
coverage, macro workforce) to `public-health/08`. This guide is about *how the
specialties interface*, **not a catalog of conditions** and **not a source of
personal referral advice**.

> **This module is an educational reference about *how clinical medicine reasons and
> how care is organized* — the cognitive and system architecture of the discipline.
> It is *not* medical advice. It does not diagnose, does not give treatment, dosing,
> or procedure instructions, does not give emergency or first-aid instructions, and
> is *not a substitute* for evaluation by a licensed clinician. Worked cases are
> illustrative teaching vignettes showing *how a clinician thinks*, not what any
> reader should do. For personal concerns, appropriate care comes from qualified
> local professionals; emergencies are handled through local emergency services.**

*Per-guide banner: educational reference on how medical specialties divide labor and
interface — not medical advice and not a guide to which specialist any individual
should see. Descriptions of specialty scope are architectural, not personal referral
triggers.*

---

## The Big Picture: Medicine Is a Distributed System of Services

A single clinician cannot hold the whole of medicine at expert depth, so the
discipline is **partitioned into services** with defined responsibilities and
**interfaces** between them. The generalist is a broad, always-on front door and
**integrator**; specialists are deep, narrow services reached through a request
protocol. Almost every systemic failure in this architecture is an **interface**
failure — a dropped referral, an ambiguous request, an unowned result, two services
editing the same patient without coordination — not a failure of anyone's expertise.

```
THE CARE SYSTEM AS A SERVICE CATALOG  (this guide owns the arrows, not the boxes' insides)
==========================================================================
  UNDIFFERENTIATED PROBLEM (population)   large volume, low prior per dx (03)
        |
        v
  [ PRIMARY CARE ]  breadth + continuity + coordination = the INTEGRATOR
        |   two independent axes (Section 5):
        |     routing:  refer / e-consult / direct access
        |     contract: advice-only / comanage / transfer
        |   (well-formed question required -- Section 4)
        v
  [ SECONDARY ]   general specialists, community hospital     narrower, deeper
        |
        v
  [ TERTIARY ]    subspecialty, academic centers, advanced procedures
        |
        v
  [ QUATERNARY ]  rare / experimental / highly specialized (transplant, etc.)
   ^    |
   |    v
   +--- RESULT + PLAN must flow BACK (closed loop, Section 6); referral is a
        round trip, not fire-and-forget. A response nobody reads is an outage.
==========================================================================
  The funnel narrows the population and sharpens the question at each hop.
  The return path (up the arrows) is where most real-world defects live.
```

**Bridge (software).** This is a microservice/service-catalog architecture:
primary care is the API gateway and orchestrator; specialties are bounded-context
services with published responsibilities; a referral is an RPC with a request
contract and an expected response; care levels are escalation tiers (L1→L2→L3
support); and the notorious failure mode — a request that fans out to services that
never call back and a result that no owner reads — is a distributed-tracing / dropped-
callback problem, not a competence problem.

---

## 1. Generalist vs Specialist — Division of Cognitive Labor

The split is not "less skilled vs more skilled"; it is **breadth-optimized vs
depth-optimized**, working at different points on the prior-probability curve.

| Dimension | Generalist (e.g., primary care, hospitalist) | Specialist / subspecialist |
|---|---|---|
| Problem state | **undifferentiated**, low prior per diagnosis | **differentiated**, enriched prior after triage |
| Core skill | breadth, triage, integration, continuity | depth in a narrow domain, procedures |
| Prevalence they see | high-volume common problems | pre-filtered, higher-prevalence-of-target |
| Failure risk | premature narrowing; missing the rare | over-focus on their organ; "hammer/nail" |
| Bayesian role | **sets** and manages pretest probability (03) | **updates** sharply within a domain |
| Ownership default | owns the whole patient + coordination | owns a defined problem or episode |

**The referral funnel and its Bayesian consequence.** Because specialists often see a
*pre-filtered* stream (the generalist has removed many non-cases), the local prevalence
of the target condition **can be** higher in a specialist's clinic than in the general
population — and higher prevalence raises PPV (the prevalence effect from guide 03). But
this is **conditional, not automatic**: the specialist's PPV rises **only when** the
referred population is **demonstrably enriched** for the target *and* the test's
performance **transports** to that population — i.e., the Sn/Sp measured elsewhere still
hold there. Referral changes the *case mix*, and **spectrum effects** can change Sn/Sp
themselves (a referred stream skewed toward more advanced disease can raise sensitivity;
one crowded with mimics of the target can lower specificity), so PPV need not move as a
naive prevalence-only calculation predicts. When enrichment is real and performance
transports, the **same test behaves differently** at each level — which is why "screen
everyone with the specialist's confirmatory test" is an architecture error — but
assuming enrichment or transport without evidence is itself an error.

**The integrator role.** Someone must own the *whole* patient — reconcile competing
specialty plans, hold the problem list, and prevent the sum of locally-correct
specialty decisions from becoming a globally-incoherent plan. This integrator is
usually primary care (or a hospitalist inpatient). Systems that weaken the integrator
(direct-access subspecialty care with no coordinator) trade access for fragmentation
(Sections 6, 8).

---

## 2. Care Levels — Primary, Secondary, Tertiary, Quaternary

Care levels describe **increasing specialization and decreasing volume**, not
increasing importance. Each level is a service tier with a characteristic catchment,
question type, and resource intensity.

```
                    /\        QUATERNARY  rare / experimental / ultra-specialized
                   /  \       (transplant, complex rare-disease, novel therapeutics)
                  /----\      TERTIARY    subspecialty consult, academic centers,
                 /      \                 advanced imaging/procedures, ICUs
                /--------\    SECONDARY   general specialists, community hospitals,
               /          \              on referral from primary
              /------------\  PRIMARY     first contact, continuity, coordination,
             /______________\             comprehensiveness  (the "4 Cs")
              population base            <- volume high at bottom, narrow at top
```

| Level | Who / where | Access | Owns | Defers up when |
|---|---|---|---|---|
| **Primary** | family/GP, general internal med, general peds | direct (first contact) | breadth, continuity, coordination, prevention | problem exceeds generalist diagnostic/management scope |
| **Secondary** | general specialists, community hospital | usually by referral | domain diagnosis + management | needs subspecialty depth, advanced procedure, or complexity |
| **Tertiary** | subspecialists, academic medical center | referral from secondary | advanced/complex care, procedures, multidisciplinary | needs experimental/ultra-rare capability |
| **Quaternary** | national/reference centers | referral from tertiary | rare, experimental, highest-complexity | — (top of stack) |

The "4 Cs" of primary care — **first Contact, Continuity, Comprehensiveness,
Coordination** (Starfield's framing; long-standing in primary-care research) — are the
properties the whole stack depends on. Systems with a strong primary-care base and a
clear referral gradient tend to show better coordination and lower duplication;
systems that let every level be a front door tend to fragment. That is a
*systems-design* observation owned here; the *financing and policy* that shape it
belong to `public-health/08`.

---

## 3. The Specialty Interface Table (a Service Catalog, Not a Disease Catalog)

This is the guide's centerpiece: the specialty map as an **API surface**. The catalog
below is **illustrative, not exhaustive** — it samples the major service *families* to
show the shape of the interface, not to enumerate every specialty or subspecialty
(there are many more, and the boundaries differ by country and institution). The
families group coherently as **longitudinal/generalist** (primary care, general
internal medicine, general pediatrics), **acute/hospital** (emergency medicine,
critical care, hospital medicine), **medical specialties** (cardiology, pulmonology,
gastroenterology, nephrology, neurology, endocrinology, rheumatology, hematology,
infectious disease, allergy/immunology, dermatology), **women's & children's health**
(obstetrics & gynecology, pediatric subspecialties), **oncology**, **surgical &
procedural** (general surgery and its subspecialties — orthopedic, urologic, ENT,
ophthalmic, neurosurgical, vascular — plus anesthesiology/perioperative),
**diagnostic/consultative** (radiology, pathology/lab medicine, clinical genetics), and
**mind, function & support** (psychiatry, rehabilitation/PM&R, palliative care). Each
row names *what the service owns* (its bounded context), the *type of question* it
answers, its *typical care level*, and *what it hands back*. It deliberately contains
**no personal referral triggers** — nothing of the form "symptom X → see service Y."
Scope is described as an architectural boundary, and the actual conditions live in
`disease/`.

| Specialty (service) | Bounded context it owns | Typical consult-question *type* | Level | Hands back |
|---|---|---|---|---|
| Primary care / family med | whole-person breadth, continuity, coordination | "integrate and own this patient over time" | 1 | (is the integrator) |
| General internal medicine | complex adult multi-system reasoning | "diagnostic uncertainty across systems" | 1–2 | dx + management plan |
| General pediatrics | whole-child breadth, development, continuity | "integrate and own this child over time" | 1 | (child integrator) |
| Emergency medicine | undifferentiated acute stabilization + disposition | "stabilize and route" (time-critical) | 1–2 | disposition + handoff |
| Critical care / intensive care | failing-physiology support of the sickest inpatients | "support organs while the cause is treated" | 2–4 | ICU course + handoff |
| Cardiology | cardiovascular diagnosis/management | dx clarification / procedure / co-manage | 2–3 | plan + procedure result |
| Pulmonology | respiratory / airway / sleep | dx + management of complex respiratory disease | 2–3 | dx + management |
| Gastroenterology | luminal GI + hepatobiliary | endoscopic dx/therapy / management | 2–3 | scope findings + plan |
| Nephrology | kidney function; **dialysis management and access coordination** | dialysis planning + management of advanced kidney failure | 2–3 | co-management plan |
| Neurology | nervous-system diagnosis/management | localization + dx of complex neuro problems | 2–3 | dx + management |
| Endocrinology | hormonal/metabolic regulation | management of refractory/complex cases | 2–3 | titration/management plan |
| Rheumatology | systemic autoimmune / inflammatory MSK | dx + management of multisystem autoimmune disease | 2–3 | dx + management |
| Hematology | blood, marrow, coagulation | dx + management of cytopenias/clotting (often with oncology) | 2–3 | dx + management |
| Infectious disease | complex/atypical infection & stewardship | regimen selection, source, stewardship | 2–3 | advisory plan |
| Allergy / clinical immunology | hypersensitivity + immune dysregulation | dx + management of allergy/immunodeficiency | 2–3 | dx + management |
| Dermatology | skin/hair/nail dx + ambulatory procedures | "characterize + manage this lesion/rash" | 1–3 | dx + procedure/plan |
| Obstetrics & gynecology | pregnancy + female reproductive care | maternity care; dx/management/operative gyn | 1–3 | plan + delivery/operative result |
| Oncology | cancer diagnosis/therapy/coordination | staging + treatment planning | 3 | treatment plan (often owns episode) |
| General surgery / surgical subspecialties (orthopedic, urologic, ENT, ophthalmic, neuro, vascular) | operative diagnosis and intervention | "is there an operative solution + do it" | 2–4 | operative plan + post-op ownership |
| Anesthesiology / perioperative | peri-procedural physiologic management | peri-op risk + intra-op management | 2–4 | peri-op plan |
| Radiology | image acquisition + interpretation | "characterize this finding" | 2–4 | read + recommendation |
| Pathology / lab medicine | tissue/lab result generation + interpretation | "what is this specimen / result" | 2–4 | diagnostic result |
| Clinical genetics / genomics | heritable-risk evaluation + variant interpretation | "is this heritable; what does this variant mean" | 2–3 | risk assessment + plan |
| Psychiatry | mental-health diagnosis/management | co-management of complex psychiatric illness | 1–3 | dx + management plan |
| Rehabilitation / PM&R | functional restoration | functional assessment + program | 2–3 | rehab plan |
| Palliative care | symptom + goals-of-care across diseases | goals-of-care + symptom co-management | 1–3 | goals + co-management |

**How to read a row (and how not to).** A row says "this service owns this bounded
context and answers this *kind* of question." It does **not** tell any reader to
consult this service — that determination is a licensed clinician's, made with a
specific patient. Radiology and pathology are the two *pure-consultative* services
every other service calls (they rarely own the patient but generate the evidence
others act on — the classic shared dependency); their split with the diagnostic
decision-maker is exactly the three-way lab-interpretation boundary from guide 03
(`pathology/` = why the result is what it is → `medicine/10` = the catalog + ranges →
`clinical-medicine/03` = how a clinician updates belief and decides to act).

---

## 4. Consultation Question Quality — Formatting the Request

A consultation is an RPC, and like any RPC it fails when the request is malformed. The
single highest-leverage skill at this interface is asking a **specific, answerable
question** — not "please see" but "please help me with *this decision*."

```
  MALFORMED REQUEST                 WELL-FORMED REQUEST
  -----------------                 -------------------
  "Consult cardiology.          ->  "Specific question: is this arrhythmia the cause
   Please see and advise."          of the syncope, or incidental? Urgency: today.
   (no question, no urgency,        Background: [pertinent data]. What I've done: [x].
    no context, no owner)           What I'll do with your answer: [decision it feeds]."
```

| Property of a good consult request | Why it matters (interface view) |
|---|---|
| **One focused, answerable question** | undefined scope → the consultant guesses → non-answer or scope creep |
| **Stated urgency** | routes the request into the right queue (emergent vs routine) |
| **The pertinent context, pre-assembled** | avoids a re-work round trip; respects the callee |
| **What decision the answer feeds** | ties the consult to a threshold (guide 03): if no decision hangs on it, VOI ≈ 0 |
| **Named requester + call-back path** | so the response reaches an owner (Section 6) |

**Curbside vs formal consultation** is the informal-vs-contracted call: a *curbside*
("quick question in the hallway") is a low-latency, no-record advisory with **no
transfer of responsibility and no chart review** — fast but unaccountable and prone to
missing context; a *formal consult* creates a record, a reviewer who sees the actual
patient/data, and a documented recommendation. Using a curbside where a formal consult
is warranted is the clinical analogue of relying on an undocumented Slack answer for a
production change. Classic guidance on effective consultation (Goldman et al.,
"Ten Commandments for Effective Consultations," *Arch Intern Med* 1983, and later
updates) codifies exactly these interface norms — a focused question, appropriate
urgency, and clear communication of the response.

---

## 5. Two Independent Axes — Routing Mechanism and Responsibility Contract

The words *referral*, *consultation*, *comanagement*, and *transfer* get used as if
they named one thing, but they mix **two orthogonal axes**, and collapsing them is a
leading cause of "I thought *you* had it." Keep them separate:

- **Axis A — request / routing mechanism:** *how the request travels and how the patient
  reaches the service.* A **referral** (a routed request to a named service), an
  **e-consult** (an asynchronous electronic question; the patient usually does not
  move), or **direct access** (the patient self-routes with no gatekeeper).
- **Axis B — intended responsibility contract:** *what accountability is meant to move.*
  An **advice-only consultation** (requester keeps ownership; the other service
  advises), **shared care / comanagement** (ownership shared under a named duty split),
  or an **explicit transfer** (the whole problem or episode moves).

```
  TWO INDEPENDENT AXES  (name BOTH; neither implies the other)
  ------------------------------------------------------------------
  AXIS A -- ROUTING MECHANISM  (how the request travels)
     REFERRAL       a routed request to a named service
     E-CONSULT      an async electronic question; patient usually stays put
     DIRECT ACCESS  patient self-routes, no gatekeeper
  ------------------------------------------------------------------
  AXIS B -- RESPONSIBILITY CONTRACT  (what accountability is meant to move)
     ADVICE-ONLY CONSULTATION    requester KEEPS ownership; the other ADVISES
     SHARED CARE / COMANAGEMENT  ownership SHARED under a named duty split
     EXPLICIT TRANSFER           the whole problem/episode MOVES
  ------------------------------------------------------------------
  A label or a bare acceptance moves NOTHING. Responsibility moves only on an
  explicit, locally valid AGREEMENT + ACKNOWLEDGMENT of the contract by a named owner.
```

**The axes are independent.** A referral (mechanism) may *intend* advice-only,
comanagement, **or** transfer; an e-consult is usually advice-only, but the intended
contract still has to be stated; direct access changes only who initiates — the
responsibility contract between services still has to be established once the patient
arrives. Naming the mechanism says nothing definite about who is now accountable, and
naming the contract says nothing about how the request was routed. **Both** must be made
explicit:

| Routing mechanism / intended contract | Advice-only consultation | Shared care / comanagement | Explicit transfer |
|---|---|---|---|
| **Referral** | "see and advise; I keep the problem" | "co-manage this with me, split named" | "please take over this problem" |
| **E-consult** | the typical case — async advice | possible — an async shared plan | rare — usually needs an in-person handoff |
| **Direct access** | patient-initiated advice visit | patient-initiated ongoing shared care | patient-initiated episode the service owns |

**A label — or even acceptance — does not transfer responsibility.** This is the
load-bearing rule. Neither the word "referral" nor a receiving service *accepting the
request to see the patient* moves accountability by itself. Responsibility moves only on
an **explicit, locally valid agreement** about the specific contract **and an
acknowledgment** of it by a named owner — "locally valid" meaning it holds under the
local rules, scope-of-practice, and policies that actually govern the two services.
Absent that explicit, acknowledged agreement, the requester still holds the problem, the
pending results, and the follow-up — whatever the routing was called.

**Five ownerships that must each be named (they are not one field).** The intended
contract is applied field-by-field; the frequent failure is collapsing them into a
single "who has the patient":

| Ownership field | What it covers | Default holder (until an explicit, acknowledged agreement reassigns it) |
|---|---|---|
| **Overall-patient** | the whole person, integration, the problem list | the integrator (usually primary care) |
| **Referred-problem** | the specific problem named in the request | the requester **until** an explicit contract for it is agreed and acknowledged |
| **Ordering** | who placed a given test/treatment order | whoever placed it — they own its consequences |
| **Pending-result** | who acknowledges a result that returns later | must be assigned explicitly at every handoff |
| **Follow-up** | who acts on the result and closes the loop | named when the order is placed, never assumed |

These are distinct. A routed request can move *referred-problem* ownership **only when
an explicit transfer or comanagement contract is agreed and acknowledged**, while
*overall-patient* ownership stays with the integrator; a *pending-result* from a test
the requester ordered stays with the requester unless it is explicitly handed off.
Naming each field — and who acknowledged which contract — is what prevents "I thought
you had it."

| Contract (Axis B) | Owner after | Duty split defined by | Classic failure |
|---|---|---|---|
| Advice-only consultation | requester (unchanged) | "advice only" | consultant starts managing (scope creep); or requester ignores advice |
| Shared care / comanagement | shared, per a named split | pre-agreed division (who orders/adjusts what) | **both** or **neither** act on a finding (double/no coverage) |
| Explicit transfer | receiver **on explicit, acknowledged agreement** | handoff content (I-PASS/SBAR, guide 07) | a routing label assumed to have transferred; dropped context at the seam |

**The load-bearing rule: the intended contract must be explicitly *agreed*, *scoped*,
*named*, and *acknowledged* to take effect — never inferred from the routing mechanism
or from a bare acceptance.** Comanagement in particular is a **concurrent-write**
situation — two services editing the same patient — and, exactly like concurrent writes
to shared state, it needs an agreed protocol for *who owns which field* and how
conflicts resolve, or the interaction produces lost updates (a change nobody made
because each assumed the other would) and write conflicts (contradictory orders).
Section 8 handles the conflict case; the prerequisite is that everyone knows which
mechanism routed the request **and** which contract is in force and who acknowledged
it.

**Bridge (systems).** Axis A is the *transport* (how the message is routed — a call, an
async message, a client connecting directly); Axis B is the *ownership protocol* the
message carries. Advice-only consultation = a read-only query; comanagement =
multi-writer shared state needing a coordination protocol (locks / CRDT-like
duty-split); explicit transfer = handing off the on-call pager — and, as with any
two-phase commit, it is committed only on an explicit **ACK**, never by the sender's
*send* alone or by the transport used. "Who is on-call for this problem right now?"
should always have exactly one answer.

---

## 6. Scope, Result Follow-Up, and the Closed-Loop Consultation

The most dangerous interface defect is the **unowned pending result** — a test ordered
at one node whose result returns after the patient has moved to another node, with no
one owning the acknowledgement. It is a dropped callback, and it harms patients
silently.

```
  CLOSED-LOOP CONSULTATION / REFERRAL  (the invariant to preserve)
  --------------------------------------------------------------
  (1) REQUEST  sent, with owner + question (Section 4)
        |
        v
  (2) RECEIVED + accepted   <- acknowledgement, not silence
        |
        v
  (3) RESPONSE produced (recommendation / result)
        |
        v
  (4) RESPONSE delivered TO A NAMED OWNER who ACKNOWLEDGES it
        |
        v
  (5) ACTION taken (or explicitly declined) and recorded
  --------------------------------------------------------------
  Break ANY arrow -> "open loop" -> the classic missed/mismanaged-result event.
  Pending tests at a transition (Section 5) are where the loop most often opens.
```

**Ownership of pending items must be assigned, not assumed.** At every handoff (guide
07), the outstanding tests, the "who will read the biopsy," and the "who acts if it is
abnormal" are explicit handoff fields. "Closed-loop communication" (read-back
confirmation) and closed-loop referral tracking exist precisely because open loops are
common and injurious; result-management systems and explicit follow-up ownership are
the engineering controls. The reasoning owned here: a referral or an order is not
complete when sent — it is complete when a **named owner has acknowledged the result
and acted or documented a decision**. Anything less is fire-and-forget, and
fire-and-forget loses messages.

**Bridge (software).** This is at-least-once delivery with **required
acknowledgement** and no orphaned async tasks: every request needs a correlation id,
a designated handler, and a completion callback that some owner is accountable for
draining. Distributed tracing exists because "did the downstream call actually come
back and get handled?" is exactly the question the closed loop answers.

---

## 7. Resource and Geographic Variation

The clean funnel of Section 2 assumes services are *available*. In reality, specialist
density, travel distance, and local practice culture vary enormously, and that
variation changes what "the right interface" even is.

| Variation axis | Effect on the interface |
|---|---|
| **Specialist density / access** | scarce specialists → longer queues, higher referral thresholds, generalists holding more scope |
| **Geography / distance** | rural/remote → hub-and-spoke, outreach clinics, or **teleconsultation as the routing topology**, with advice/shared-care/transfer responsibility named separately |
| **Practice-style variation** | referral rates for the *same* problem vary widely between clinicians and regions with similar outcomes |
| **Supply-sensitive care** | in some settings, the *supply* of specialists/beds drives utilization more than need |

**Unwarranted practice variation** — documented at length in small-area-variation
research (Wennberg and the Dartmouth Atlas tradition) — shows that referral and
procedure rates for comparable populations differ far more than underlying illness
explains, implicating *supply and local habit*, not just patient need. The
architectural reading: the referral interface is not a fixed pipe; its threshold is
set partly by local resource supply and culture, so "appropriate referral" is
context-dependent, and low-resource settings run a materially different topology
(broader generalist scope, telehealth interfaces, delayed escalation). Care-architecture
guides in this module assume a resourced system; that assumption must be flagged, not
universalized. (The macro workforce/financing *policy* behind these patterns is owned
by `public-health/08`.)

**Alternate interface topologies.** The gatekept funnel of Section 2 is only one shape.
Real systems run several, each tuned to a resource reality:

```
  ALTERNATE INTERFACE TOPOLOGIES  (the Section 2 funnel is one shape among many)
  --------------------------------------------------------------------------
  GATEKEPT REFERRAL   patient -> primary-care gate -> specialist  (baseline)
  DIRECT ACCESS       patient -> specialist directly (no gate; the integrator weakens)
  DISTRICT HOSPITAL   patient -> district general hospital (most secondary care)
                                 -> distant tertiary only for the rare/complex
  TASK-SHIFTING/CHW   patient -> community health worker / nurse (protocol + escalate)
                                 -> clinician when the protocol's threshold is crossed
  TELECONSULT         local site -> network link -> remote specialist
                                 (routing topology; contract named separately)
```

| Topology | Front door | Where the interface lives | Trade-off |
|---|---|---|---|
| **Gatekept referral** | primary-care generalist | referral request + return report | coordination & filtered priors vs. access latency |
| **Direct access** | any service, self-referred | patient-chosen entry | faster access vs. lost integrator, unfiltered priors, fragmentation |
| **District-hospital** | district general hospital | local secondary care; escalate the rare | reach with fewer specialists vs. a capability ceiling |
| **Task-shifting / CHW** | community health worker / nurse | protocol + a defined escalation threshold | extends coverage where clinicians are scarce vs. narrower protocol scope |
| **Teleconsult (hub-and-spoke)** | local clinician + remote specialist | a network link; the responsibility contract may be advice-only, shared care, or explicit transfer | specialist reach at distance vs. no hands-on exam; contract and ownership must be named separately |

None of these is "wrong": each is an interface topology tuned to a different supply of
clinicians, distance, and infrastructure. What must hold in *all* of them are the same
invariants — a well-formed question (Section 4), explicitly agreed, scoped,
**acknowledged**, and **named** ownership (Section 5), and a **closed loop** (Section
6). Only the physical shape of the interface changes; the required contract
*discipline* does not. The local contract type may still be advice-only, shared care,
or explicit transfer.

---

## 8. Multi-Specialty Conflict Resolution

When several services concurrently touch one patient, their locally-correct decisions
can conflict or fragment. This is the distributed-consistency problem of medicine, and
it has recognizable resolution patterns.

```
  FAILURE MODES OF MANY SERVICES ON ONE PATIENT
  ---------------------------------------------------------------
  FRAGMENTATION : each service optimizes its organ; no one owns the whole
  CONTRADICTION : service A's plan undermines service B's (e.g., competing priorities)
  DIFFUSION     : "someone else will handle it" -> nobody does (bystander effect)
  POLYPHARMACY / over-intervention : sum of locally-rational additions (see guide 06)
  ---------------------------------------------------------------
  RESOLUTION PATTERNS
  ---------------------------------------------------------------
  INTEGRATOR    : one accountable owner (primary care / hospitalist) reconciles plans
  FORUM         : multidisciplinary team meeting / tumor board -> joint decision, one plan
  HIERARCHY     : an agreed "most responsible" service for the current dominant problem
  GOALS-ANCHOR  : resolve conflicts by returning to the patient's goals of care
```

| Resolution mechanism | How it works | When it fits |
|---|---|---|
| **Named integrator** | one accountable owner holds the master plan and problem list | chronic multimorbidity; inpatient with many consults |
| **Multidisciplinary team (MDT) / board** | services meet, deliberate, converge on one documented plan | cancer (tumor board), complex cases, transplant |
| **"Most responsible" designation** | one service is explicitly accountable for the episode | inpatient with a dominant active problem |
| **Goals-of-care anchor** | disputes resolved against what the patient values (guide 10) | value-laden or end-of-life conflicts |

**The principle:** conflict is resolved by **restoring single accountable ownership**
for the decision in question — whether by an integrator, a forum that produces one
plan, or an agreed hierarchy — never by leaving parallel, uncoordinated writers. The
MDT/tumor-board pattern is a formal consensus protocol (bring the deciding services
into one room, produce a single committed plan) that also spreads accountability
appropriately. When specialists disagree, the resolution is not "loudest wins" but a
named owner adjudicating against the patient's goals.

**Bridge (systems).** Fragmentation is a partitioned system with no coordinator;
diffusion of responsibility is the "everyone assumes another replica handled it"
bug; the integrator is an **incident commander**; the tumor board is a consensus
round that commits a single value; goals-of-care is the tie-breaking priority
function. One accountable owner per decision is the invariant.

---

## 9. Worked Case — A Closed-Loop Comanagement Consult (illustrative, fictional)

All names, services, and clinical details below are invented to show the *interface
mechanics*; nothing here is advice, and the clinical specifics are deliberately
abstract (the conditions and their management live in `disease/`, `medicine/`,
`pharmacology/`). Follow the ownership fields (Section 5) and the closed loop
(Section 6) as they move.

**Setup.** Dr. A is patient **R**'s primary-care generalist and the **overall-patient
integrator**. R already has a comanagement relationship with **nephrology (Dr. N)** for
dialysis management and access coordination. A new cardiac problem **P** surfaces.

**(1) Question.** Dr. A sends cardiology a well-formed request (Section 4): *"Focused
question: is P the cause of R's new symptom, and is an intervention indicated? Urgency:
this week. Context: [pre-assembled]. What the answer feeds: whether to pursue a
procedure or continue medical management."* Requester and call-back path are named.

**(2) Agreement + acknowledgment (mechanism vs contract).** The **routing** was a
referral; the **contract** is settled separately. **Cardiology (Dr. C)** acknowledges
the request and **explicitly agrees a locally valid comanagement contract** for the
*referred problem* P — its workup and the procedure decision — and explicitly **not**
the whole patient. *Overall-patient* ownership stays with Dr. A. The routing label and a
bare "received" moved nothing; ownership of P shifts only on this acknowledged
agreement.

**(3) Ordering + result owner.** Dr. C orders test **T** and names its owners: the
*pending-result* owner is Dr. C's team; the *follow-up* owner (who acts on T) is Dr. C.
Separately, Dr. A had ordered a baseline lab; that *pending-result* stays with Dr. A.
Each order carries a named result-and-action owner — none is left "to whoever sees it."

**(4) Communication.** T returns; Dr. C's team acknowledges it (closed-loop read-back),
produces a recommendation, and delivers it **to a named owner** (Dr. A), who
acknowledges receipt. The advice has completed a round trip, not a fire-and-forget.

**(5) Comanagement + an unresolved conflict.** Dr. C's proposed next step needs an
imaging study that **Dr. N flags** as conflicting with R's kidney/access plan. Two
locally-correct plans now **contradict**, and — briefly — each service assumes the
other will adjust (**diffusion**): the conflict is *unresolved*, and no single owner
holds the decision.

**(6) Resolution.** The **integrator (Dr. A)** restores single accountable ownership: a
short multidisciplinary huddle (Section 8) brings cardiology and nephrology to one
decision, **anchored to R's goals of care** (guide 10). The huddle commits **one** plan
with a **most-responsible** owner for the contested step; the alternative is explicitly
**declined and documented**, not silently dropped.

**(7) Closure.** Every pending item is closed: T acknowledged and acted on by Dr. C;
the baseline lab acknowledged by Dr. A; the imaging decision recorded with its owner and
the declined option noted. The loop is closed because each result reached a **named
owner who acknowledged and acted or documented a decision**. Had any acknowledgement
been missing, that arrow would be an **open loop** — the classic missed-result event.

**Ownership trace (who holds what, end to end):**

| Field | Holder through the case |
|---|---|
| Overall-patient | Dr. A (integrator) throughout |
| Referred-problem (P) | Dr. A → **Dr. C on an acknowledged comanagement agreement** (scoped to P) |
| Ordering | whoever placed the order (T: Dr. C; baseline lab: Dr. A) |
| Pending-result | named per order; never "whoever sees it" |
| Follow-up / closure | the named action owner per item; contested step → most-responsible owner after the huddle |

The interface held not because anyone was more expert, but because every arrow had an
acknowledged, named owner and the loop was closed.

---

## 10. Alternate-System Case — District Hospital, Task-Shifting, and Teleconsult (illustrative, fictional)

Section 9 ran on a resourced, gatekept-referral topology. The same invariants must hold
on a very different one. This compact case runs a **district-hospital + task-shifting +
teleconsult** topology (Section 7), where the nearest subspecialist is only a teleconsult
link away. Names and clinical details are invented; nothing here is advice.

**Setup.** At a **district hospital**, a **community health worker (CHW), M** runs a
protocol-driven clinic; **nurse-clinician K** leads the on-site team and holds **local
overall-patient** ownership; **district physician D** covers escalations; and a **remote
specialist S** is reachable only by **teleconsult** (advice, not transfer — the patient
does not move). Patient **W** arrives by **direct access**, with no gatekeeper.

**(1) Protocol + escalation acceptance.** M works W up to the protocol's defined
threshold, then escalates to K. K **explicitly accepts** on-site ownership of W's problem
— an acknowledged, locally valid agreement, not an assumption — and names the team's duty
split. Task-shifting holds only because the escalation was *accepted*, not merely sent.

**(2) Teleconsult (routing = teleconsult; contract = advice-only).** K opens a teleconsult
to S with a well-formed question (Section 4). The two axes stay explicit: the **routing**
is a remote link; the **contract** is **advice-only** — S advises, K keeps ownership.
Nothing moves to S, because a teleconsult transfers responsibility only on an explicit,
acknowledged agreement (which local scope-of-practice here would not permit anyway).

**(3) Pending-result ownership.** S recommends test **T**, run on-site but sent to a
distant regional lab, so the result will return **after** W has gone home. K remains
the **pending-result and follow-up owner** unless D explicitly agrees to a scoped
handoff. In this vignette D acknowledges that agreement before W leaves, so D becomes
the named follow-up owner while K's district team remains the result-tracking backstop.
Neither duty is left "to whoever opens the report."

**(4) Escalation on the result.** T returns abnormal. D — already the acknowledged,
named follow-up owner — receives the escalation; a second teleconsult with S revises
the plan. Had W needed
capability beyond the district hospital, D would arrange an **explicit transfer** to the
referral center, effective only on that center's acknowledged acceptance.

**(5) Closure.** Every item closes: the escalations accepted by K then D; the teleconsult
advice acknowledged and acted on by K; T acknowledged by its named owner and acted on by
D; the transfer either completed on acknowledged acceptance or explicitly judged
unnecessary and documented. The loop closed on a district-hospital / task-shifting /
teleconsult topology for the same reason it did in Section 9: **every arrow had an
acknowledged, named owner**, and routing was kept distinct from responsibility.

**Ownership trace (alternate topology):**

| Field | Holder through the case |
|---|---|
| Overall-patient (local) | nurse-clinician K throughout |
| Escalated problem | M → **K on accepted escalation**; abnormal-result step → **D on accepted escalation** |
| Teleconsult advice | remote specialist S advises; ownership **stays** with K (advice-only) |
| Pending-result | named per order (T: district team via K); never "whoever opens it" |
| Follow-up / closure | D for T; transfer to a referral center only on **acknowledged acceptance** |

The topology is unrecognizable next to Section 9 — different front door, a task-shifted
team, advice arriving over a wire — yet the contract discipline is identical: routing is
not responsibility, and nothing moves without an explicit, acknowledged, locally valid
agreement.

---

## Reader Tasks (answerable from this guide)

1. **Classify an interaction on both axes.** Given four vignettes (a hallway question,
   a "please take over her diabetes," a shared post-op diabetes plan, a full handoff),
   name the **routing mechanism** and the **responsibility contract** separately, and
   say who owns the problem and the follow-up — and what explicit acknowledgment would
   be required to move it. (Sections 5–6.)
2. **Rewrite a bad consult request.** Turn "Consult neuro, please see" into a
   well-formed request with a focused question, urgency, context, and the decision it
   feeds — and say why the original risks a non-answer. (Section 4.)
3. **Trace and close an open loop.** Given an ordered test whose result returns after
   discharge, mark where the loop is open and assign the acknowledgement/action owner
   that closes it. (Section 6.)
4. **Place services on the care-level stack.** Given several services, assign typical
   care levels and explain how the referral funnel changes a test's PPV between
   primary and subspecialty clinics — but only when the population is **demonstrably
   enriched** and test performance **transports**, and note how spectrum effects can
   shift Sn/Sp (link to guide 03). (Sections 1–3.)
5. **Resolve a multi-specialty conflict.** Given three services with contradictory
   plans, choose and justify a resolution mechanism (integrator, MDT, most-responsible,
   goals anchor) and state the invariant it restores. (Section 8.)

---

## Decision Cheat Sheet

| Situation | What the interface model shows | Why (this guide) |
|---|---|---|
| A problem is sent to a specialist | a well-formed request carries **one focused, answerable question** + urgency + context + the decision it feeds | a consult is an RPC; malformed requests get non-answers (§4) |
| Unclear who owns the patient now | the two axes read separately: **routing mechanism** (refer / e-consult / direct access) and **responsibility contract** (advice-only / comanage / transfer) | mechanism and contract are independent (§5) |
| Two services adjusting the same thing | a **concurrent write** needing an explicit, named duty split | comanagement without a protocol → double/no coverage (§5, §8) |
| A test is pending at a handoff | a **named owner** holds the result + action | open loops are the classic missed-result harm (§6) |
| A referral was "sent" | the routing label and even a bare acceptance move **nothing**; responsibility moves only on an **explicit, locally valid agreement + acknowledgment**, and the loop closes only when a response is acknowledged and acted on | routing is not the contract; ownership needs explicit agreement (§5, §6) |
| A specialist reports a high PPV | it holds **only if** the referred population is **demonstrably enriched** *and* the test's Sn/Sp **transport** to it — and spectrum shifts can change both | enrichment and transport are assumptions, not givens (§1, §3, links §03) |
| Rural / low-specialist setting | a **broader generalist scope + teleconsult** topology, with different thresholds | the interface topology is resource-dependent (§7, §10) |
| Many services, one incoherent plan | **single accountable ownership** restored (integrator / MDT / MRP / goals) | conflict = uncoordinated concurrent writers (§8) |
| Deciding a real patient's referral | **out of scope** — that is a licensed clinician's call | this guide is architecture, not advice (banner) |

---

## Common Confusion Points

**"A specialist is just a better doctor."** No — a specialist is **depth-optimized on
a narrow domain**, working on a pre-filtered, higher-prevalence stream; a generalist
is **breadth-optimized** and manages undifferentiated problems and coordination. Each
outperforms the other on their own stream; neither dominates. The "hammer/nail" risk
(seeing every problem as one's own organ) is the specialist-side failure mode, matched
by premature narrowing on the generalist side.

**"Tertiary/quaternary care is the important care."** The levels describe
**specialization and volume, not value.** Most health is produced at the wide bottom of
the pyramid (primary care's continuity and coordination); the narrow top is rare,
resource-intense capability. A system that is all top and no base fragments.

**"Referral and consultation are the same thing" (or exact opposites).** Neither — they
live on **different axes**. *Referral* is a **routing mechanism** (how the request
travels); *advice-only consultation* is a **responsibility contract** (what
accountability is meant to move). A referral can carry an advice-only, comanagement,
**or** transfer contract, so the routing label alone says nothing definite about who is
now accountable. The failure is reading the mechanism as if it fixed the contract — or
assuming that *sending* a referral, or its bare acceptance, already moved ownership. Only
an explicit, locally valid, acknowledged agreement does that (§5).

**"Once I refer, it's handled."** Only if the loop closes. A referral is a round trip:
request → acknowledged → response → **owner acknowledges and acts**. The dangerous gap
is the return path and the pending result, not the outbound request (§6).

**"A curbside is as good as a real consult."** A curbside is fast but **carries no
chart review and no transferred responsibility** — it answers a general question with
partial context. For a decision that hinges on this patient's specifics, it is the
wrong instrument, like trusting an undocumented hallway "yes" for a production change.

**"More specialists means better care."** Beyond a point, more concurrent services
without an integrator produce **fragmentation, contradiction, and diffusion of
responsibility** (§8), plus supply-sensitive over-intervention (§7). The binding
constraint is usually coordination, not additional expertise.

**"This tells me which specialist to see."** It does not, and must not. Specialty
scope here is an **architectural boundary**, not a personal referral trigger. Whether
a specific person should see a specific service is a clinical judgment made by a
licensed clinician; the actual conditions and their management live in `disease/`,
`medicine/`, and `pharmacology/`.
