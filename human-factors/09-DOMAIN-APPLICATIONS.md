---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-factors:domain-applications
kind: guide
module: human-factors
section: human-factors
title: Domain Applications - Applying the Models, Deferring the Systems
status: source-custody
source_custody: partial
current_path: human-factors/09-DOMAIN-APPLICATIONS.md
canonical_path: human-factors/09-DOMAIN-APPLICATIONS.md
backsource_ids: [proof-backfill:human-factors:09-domain-applications]
concepts: [domain-applications, crew-resource-management, patient-safety-hf, control-room-hf, rail-hf, maritime-hf, road-hf, apply-and-defer]
root_concepts: [domain-applications]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Domain Applications — Applying the Models, Deferring the Systems

**This guide owns** the module's **apply-and-defer pattern**: it is the *single deliberately
domain-organized guide*, and it exists to show how the module's models — physical fit (`02`),
workload/SA (`03`), error (`04`), reliability (`05`), interface (`06`), automation (`07`),
hazard (`08`), and culture (`11`) — **recur across domains** (aviation, healthcare, process,
rail, maritime, road), while **the domain systems themselves are deferred to their owners**. Its
thesis is the module's organizing decision made visible: **the operator-and-safety science is
reusable; the domain is where it is applied, not a separate human-factors field**. **It builds
on** every prior guide and applies them. **It explicitly defers** — and this is the whole point:
flight systems/avionics to [`aeronautics/04-AVIONICS`](../aeronautics/04-AVIONICS.md); clinical
practice and clinical patient-safety to
[`clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW`](../clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW.md);
medical-device engineering to
[`biomedical-engineering/07-MEDICAL-DEVICES`](../biomedical-engineering/07-MEDICAL-DEVICES.md);
reactor systems to [`nuclear/05-SAFETY-SYSTEMS`](../nuclear/05-SAFETY-SYSTEMS.md); rail signalling
and road/vehicle autonomy to [`transportation/`](../transportation/00-OVERVIEW.md); and all
legal/regulatory duty to `law/`. This guide **re-teaches no domain system** and **issues no domain
operating advice**.

> **Safety & ethics contract (binds every human-factors guide).** This is an **educational
> systems reference**. Applying a model to a domain here is **not** a procedure for that domain,
> a certification, an accident ruling, or clinical/operational advice. Domain examples are
> **illustrations of transferable human-factors reasoning**, dated and bounded; **acceptance and
> implementation in any domain belong to that domain's accountable organizations and regulators**,
> never to this module.

*Per-guide banner: this guide names domains only to show the **same models** at work. Every
domain-specific system, procedure, and regulation is **out of scope and deferred** — if a
sentence here starts to read like "how to fly / treat / operate," it has crossed the line the
guide exists to hold.*

---

## The Big Picture: One Toolkit, Many Domains

The pivotal architecture call (`00`) was to organize by the **human-factors problem**, not the
domain — because a domain-first cut would re-teach systems the domain modules own. Guide `09` is
where that call pays off: it lines the domains up **against the models** and shows the same rows
recurring.

```
APPLY-AND-DEFER  (the models are the rows; the domains are the columns)
================================================================================
   model \ domain   AVIATION      HEALTHCARE     PROCESS/     RAIL         ROAD
                                                 NUCLEAR
   02 physical      cockpit reach  OR/ward layout console reach  cab layout   cab/seat
   03 workload/SA   crew SA,       alarm fatigue, control-room   driver       driver
                    mode awareness cognitive load  vigilance     vigilance    distraction
   04 error         CRM, checklists med error taxa  slips/violat. SPAD errors  lapses
   05 HRA           flight-crew HEP  care-task HEP   PRA human    driver HEP   -
   06 interface     flight-deck     device alarms,  alarm mgmt    signal       ADAS HMI
                    displays, modes infusion HMI    (06 std)      salience     modes
   07 automation    autopilot,      closed-loop     DCS/advisory  ATP/ATO      ADAS/AV
                    mode confusion  device control  automation    takeover     takeover
   08 hazard        bow-tie, STPA   RCA, bow-tie     HAZOP, PRA    STPA         STPA
   11 culture       CRM, just cult. just culture     HRO          SPAD reporting reporting
   ================================================================================
   DEFER (columns' SYSTEMS): aeronautics/04 | clinical-medicine/11 + bme/07 |
      nuclear/05 | transportation/ (rail) | transportation/07 (road/AV).  law/ owns duty.
   The GRID is the guide: read DOWN a column to apply the toolkit to a domain; read
   ACROSS a row to see one model recur. The guide APPLIES the models and DEFERS the systems.
```

The most important observation: the **cells repeat**. "Alarm fatigue" is guide `06`'s alarm
philosophy in an ICU *and* a control room; "mode confusion" is guide `07`'s ironies in a cockpit
*and* a car; "SPAD" and "wrong-patient" are guide `04`'s error taxonomy with different
consequences. The science is one toolkit; the domain sets the **stakes, the regulator, and the
idiom**.

---

## 1. Aviation — Where the Discipline Grew Up

Aviation is the discipline's birthplace (`01`), so its idioms are the most mature.

- **Crew Resource Management (CRM)** — born from a **1979 NASA workshop** (Cockpit/Crew Resource
  Management; Helmreich and colleagues) after accidents where *coordination*, not stick-and-rudder
  skill, failed. CRM trains communication, assertion, shared SA (`03`), and cross-checking — and it
  is the **canonical portable intervention** that later crossed into healthcare, maritime, and rail.
- **Checklists and the "sterile cockpit"** — structured defenses against lapses (`04`) and
  interruption; the *concept* is HF's, the specific **regulation** (e.g., the sterile-cockpit rule)
  is `law/`'s and the domain's.
- **Flight-deck displays and mode confusion** — apply `06` (mode/state visibility) and `07`
  (automation surprise). The **avionics/FMS systems themselves defer to `aeronautics/04`.**

---

## 2. Healthcare — The Highest-Volume Transfer

Healthcare imported aviation HF wholesale, with a crucial boundary: **the clinical practice and
clinical patient-safety systems are `clinical-medicine/11`'s**; this guide owns the **generic
human-factors science** applied there.

- **Surgical checklists** — the **WHO Surgical Safety Checklist** (introduced **2008**; Haynes et
  al., *NEJM* **2009**) is a checklist/`04`-lapse defense and a CRM-style team intervention. The
  *clinical* content is `clinical-medicine/11`'s; the *human-factors mechanism* (why checklists
  catch lapses, how teams share SA) is this module's.
- **Alarm fatigue** — guide `06`'s alarm philosophy and guide `03`'s attention budget, in an ICU:
  too many non-actionable alarms → desensitization → missed real ones (cry-wolf). The **device HMI**
  defers to `biomedical-engineering/07`; the **clinical response protocol** to `clinical-medicine/11`.
- **Handoffs** — information loss at shift/care transitions is a `04`-lapse + `03`-shared-SA
  problem; *whether* a structured handover helps, and in what form, is a **candidate mechanism the
  domain must select and verify** — the *clinical* handover practice is `clinical-medicine/11`'s,
  not this module's to prescribe.

---

## 3. Process & Nuclear — Control Rooms and Alarm Management

The process industries gave the module its **alarm-management standards** (`06`: EEMUA 191,
ANSI/ISA-18.2, IEC 62682) and much of its **HRA** (`05`: THERP/SPAR-H).

- **Control-room design and alarm management** — guide `06` is largely *about* this domain's
  hard-won lessons (Three Mile Island, `01`); applied here it means rationalized alarms, visible
  modes, and ecological displays. The **reactor protection systems themselves defer to
  `nuclear/05`.**
- **Procedures and HRA** — `05`'s PSFs and `08`'s HAZOP grew up in process plants; applied here
  they screen operator tasks and enumerate hazards. The **plant and its safety systems** are the
  domain's.

---

## 4. Rail, Maritime, Road — Vigilance, Takeover, Distraction

- **Rail** — **signals passed at danger (SPAD)** are a guide `04` error problem (slips, lapses,
  rule-based mistakes under monotony) plus a guide `03` vigilance problem; **ATP/ATO** automation is
  guide `07`'s takeover/OOTL problem. The **signalling and train-control systems defer to
  `transportation/`.**
- **Maritime** — **Bridge Resource Management** is CRM at sea; watchkeeping fatigue is a guide `02`/`03`
  problem; ECDIS mode confusion is guide `06`/`07`. The **navigation systems defer to their owners.**
- **Road** — driver **distraction** and **drowsiness** are guide `03`; **ADAS/automated-driving**
  takeover and mode confusion are guide `07`; the **vehicle autonomy and the SAE J3016 levels defer
  to `transportation/07`.**

---

## The Boundaries (ownership in one place)

```
THE APPLY-AND-DEFER LINE  (the guide's reason to exist)
--------------------------------------------------------------------------------
   this guide (09)  APPLIES the models (02-08, 11) to domains; owns the cross-domain
                    PATTERN and the portability of interventions (CRM, checklists, alarm mgmt)
   aeronautics/04   flight/avionics SYSTEMS            nuclear/05   reactor safety SYSTEMS
   clinical-medicine/11  clinical practice & patient-safety SYSTEMS
   biomedical-engineering/07  medical-DEVICE engineering & regulation
   transportation/  rail signalling; road/vehicle autonomy (J3016)
   law/             legal/regulatory duty in every domain
   -----------------------------------------------------------------------------
   Rule: read DOWN a column to APPLY; hand the SYSTEM in that column to its owner.
   The guide issues NO domain procedure and re-teaches NO domain system.
```

---

## A Worked Cross-Domain Pass — One Model, Two Domains (reproducible)

*All numbers are **synthetic**. It demonstrates that the *same* guide-`06` alarm model and guide-
`03` attention reasoning apply across domains, with domain-specific readings — not an assessment,
procedure, or certification for either domain.*

**The model (from `06`).** An alarm system is healthy when **most alarms require an action** and
the **rate is within the attention budget**; the key metric is **actionable fraction** and
**alarms per operator per hour**, read against dated, domain-specific guidance (never a limit).
Apply the *same* metric to two domains with synthetic inventories:

```
SAME MODEL (06/03), TWO DOMAINS  (synthetic alarm inventories)
--------------------------------------------------------------------------------
   metric                          ICU bedside      PROCESS control room
   alarms per operator per hour        90                 62
   actionable fraction (%)             15                 40
   ACTIONABLE alarms / hour        90*0.15 = 13.5     62*0.40 = 24.8
   non-actionable "noise" / hour   90-13.5 = 76.5     62-24.8 = 37.2
   -----------------------------------------------------------------------------
   SAME reading in BOTH: the majority of alarms are NON-ACTIONABLE -> the SAME candidate
   MECHANISM is implicated (cry-wolf -> desensitization, guide 03 attention budget). The
   model raises an evidence QUESTION -- "is the actionable fraction low? what is the
   attention budget? which alarms are non-actionable?" -- it does NOT prescribe the fix.
   WHETHER and HOW to act (e.g., re-rationalizing an alarm set) is the DOMAIN OWNER's
   call, under its own hazard review / change process and informed by local evidence.
   DOMAIN DIFFERENCE is CONSEQUENCE and OWNER, not the model:
      ICU: missed alarm -> patient harm; device HMI -> bme/07; protocol -> clinical-medicine/11
      Process: missed alarm -> release; alarm std -> 06/EEMUA; plant system -> nuclear/05
   ----------------------------------------------------------------------------------------
   The >=2-CHANNEL invariant travels with the model: wherever an alarm or mode cue carries a
   safety-relevant state (ICU, control room, flight deck, cab) it should ride on >=2 coding
   channels, never color or tone alone -- the operator-safety twin of accessibility's "never
   color alone" (06 sec.3). Which channels, and whether to change a real system, is the
   owner's decision.
```

**Portability tally (which of the module's models transfer to a new domain).** For a *new* domain
(say, a synthetic "remote drone-operations centre"), score whether each model applies:

```
PORTABILITY OF THE TOOLKIT  (synthetic: does each model transfer? Y/partial/N)
--------------------------------------------------------------------------------
   02 physical fit ...... Y (operator console)        06 interface ..... Y (displays/alarms)
   03 workload/SA ....... Y (multi-drone SA)          07 automation .... Y (supervisory control)
   04 error ............. Y (slips/mode errors)       08 hazard ........ Y (STPA on control)
   05 HRA ............... partial (sparse base rates)  11 culture ....... Y (reporting)
   -----------------------------------------------------------------------------
   Reading: 7 of 8 models transfer directly; HRA transfers only PARTIALLY (no domain HEP
   data yet) -> honest output widens the HRA uncertainty (guide 05), it does not invent a
   number. The DOMAIN SYSTEM (the drone/airspace) defers to its owner; this guide APPLIES.
```

**Uncertainty / validity / bias note.** (1) The alarm inventories and the portability scores are
**synthetic**; the *pattern* (mostly-non-actionable alarms across very different domains) is the
real, repeatedly-observed one, but the numbers are illustrative. (2) **Transfer is not automatic**
— a model validated in aviation can mis-fit healthcare's team structure or a low-resource setting;
CRM's own cross-domain transfer has had mixed, context-dependent results. (3) The **HRA "partial"**
cell is the honest one: no domain data means a *wider range*, not a borrowed constant (`05`). (4)
This is a **cross-domain reasoning demonstration**, not an alarm assessment or a procedure for the
ICU or the control room — those, and the systems, are their owners'.

---

## A Fully Worked Case — Porting an Intervention (illustrative, fictional)

*Fictional. It demonstrates the apply-and-defer pattern — not a program, procedure, or
certification for any real domain.*

**Setting.** A *fictional* regional **maritime authority** has heard that "CRM cut aviation
accidents" and asks whether to port **Crew Resource Management** to its ferries' bridges. Human
factors applies the pattern:

1. **Name the model, not the domain move (§1).** CRM is a **team-SA + communication +
   cross-checking** intervention (guides `03`, `04`) — a *portable human-factors mechanism*, not an
   aviation procedure. That is what may transfer; the cockpit specifics do not.
2. **Check portability honestly (§Worked pass).** Bridge teams differ from cockpits (hierarchy,
   watch rotation, pilot-transfer). The team-SA and assertion mechanisms likely transfer (Bridge
   Resource Management already exists); the *evidence* on outcomes is **context-dependent**, so the
   authority should pilot and measure (guide `10`), not assume the aviation effect size.
3. **Apply the neighbouring models (§2–4).** Watchkeeping fatigue → `02`/`03`; ECDIS mode confusion
   → `06`/`07`; near-miss reporting → `11`. Each is the *same toolkit* applied to the bridge.
4. **Defer the systems (§Boundaries).** The **navigation and ship systems** are `transportation/`'s
   (maritime) and the vendors'; the **legal watch regulations** are `law/`'s and the flag state's;
   **acceptance** of any bridge program is the **authority's and its regulator's** — this module
   supplies the human-factors reasoning and evidence, not the program or the sign-off.

**Reading.** "Port CRM" became "port the *mechanism*, verify the transfer, apply the neighbouring
models, defer the systems and the acceptance" — the apply-and-defer discipline that keeps `09` from
becoming a second, domain-shaped copy of the domain modules.

---

## Reader Tasks (answerable from this guide)

1. **Read the grid two ways.** Pick the "healthcare" column and name which model each of "alarm
   fatigue," "surgical checklist," and "infusion-pump mode error" applies; then pick the "mode
   confusion" row and name it in aviation, road, and maritime — and state the *system owner* deferred
   to in each (§Big Picture, §1–4).
2. **Apply one model across two domains.** Using the synthetic alarm inventories, compute the
   actionable alarms/hour for the ICU and the control room, show that both are dominated by
   non-actionable alarms, and explain why the *fix* is the same guide-`06` rationalization while the
   *consequence and owner* differ (§Worked pass).
3. **Score portability honestly.** For the synthetic drone-operations centre, say which models
   transfer directly and why **HRA** is only "partial," and what the honest HRA output is with no
   domain data (§Worked pass; `05`).
4. **Port an intervention without re-teaching the domain.** Explain why "port CRM to ferries" must
   become "port the team-SA mechanism and verify the transfer," and identify what stays with
   `transportation/` and `law/` (§Worked case).
5. **Catch a boundary violation.** Given a draft paragraph that starts explaining *how to configure
   the reactor protection system*, identify the crossed line and rewrite it as an apply-and-defer
   statement pointing to `nuclear/05` (banner, Boundaries).

---

## Decision Cheat Sheet

| In a domain, you're facing... | Apply model | Defer the system to |
|---|---|---|
| Team coordination / shared SA failure | CRM idea via `03`,`04` | the domain (train the domain's teams) |
| Too many non-actionable alarms | `06` alarm philosophy + `03` | device → `bme/07`; plant → `nuclear/05` |
| A lapse/slip under monotony (SPAD, wrong-patient) | `04` error taxonomy | signalling → `transportation/`; care → `clinical-medicine/11` |
| Mode confusion / automation surprise | `07` + `06` mode visibility | FMS → `aeronautics/04`; AV → `transportation/07` |
| Operator-task failure probability | `05` HRA (as a range) | plant/vehicle system → its owner |
| Fatigue / watchkeeping load | `02`/`03` | shift regulation → `law/` + domain |
| "How does the aircraft/reactor/car work?" | — | its domain module (never here) |
| "Certify / write the procedure for this domain" | **out of scope** | domain org + regulator |

---

## Common Confusion Points

**"Aviation HF, medical HF, and nuclear HF are separate fields."** They are the **same toolkit**
applied to different domains. The models (`02`–`08`, `11`) recur; the domains differ in stakes,
regulator, and idiom. Treating them as separate fields is exactly the domain-first organization the
module rejected (`00`, §Big Picture).

**"This guide teaches the domain."** It does **not**. It applies human-factors *models* and defers
every domain system, procedure, and regulation to the domain module and `law/`. If it reads like
"how to fly/treat/operate," it has failed (banner).

**"An intervention that worked in aviation will work here."** Transfer is **context-dependent**.
CRM, checklists, and alarm standards *often* port, but the effect size and fit vary with team
structure, culture, and resources — pilot and measure (guide `10`), don't assume (§Worked pass).

**"Applying a model to a domain certifies that domain."** No. The application produces
**evidence and requirements**; acceptance and implementation are the domain organization's and its
regulator's (safety contract).

**"The alarm/HEP numbers here are the domain's real numbers."** They are **synthetic
illustrations** of the *model*; real domain values are the domain's, measured locally, and carry
their own uncertainty (§Worked pass).

---

## Global, WEIRD & Resource Caveats

- **The domains and interventions are Western-industrial exemplars.** CRM (US aviation), the WHO
  checklist's original trials, and the process-alarm standards come from well-resourced systems;
  their *mechanisms* transfer, but the assumed staffing, devices, and regulation do not.
- **Transfer can carry a resource assumption.** "Just adopt the checklist / the alarm standard"
  presumes the staffing, equipment, and training to run it; in low-resource domains the intervention
  must be adapted (guide `10`), and the honest output names the resource constraint rather than
  assuming compliance.
- **Consequence asymmetry across domains is real.** The *same* error has very different stakes in an
  ICU vs a parcel line; the toolkit is shared, but the module must not flatten that difference — it
  supplies the reasoning and defers the risk-acceptance to the domain that bears the consequence.

---

## A Contrasting Example (non-WEIRD, low-resource)

*Fictional, to show apply-and-defer where the domain and resources are not the Western default.*

**Setting.** A *fictional* rural district hospital in a low-income region wants to reduce
medication errors but has **no** infusion pumps with configurable alarms, **no** electronic records,
and staff trained by apprenticeship.

**How the pattern adapts.**
- **Name the candidate mechanism, don't prescribe the tool.** The *error taxonomy* (`04`) and the
  *lapse-defense mechanism* transfer as **concepts**; *which* affordable form — a paper aid, a
  verbal cross-check, a layout change, or none — is worth trialling is the **hospital's** decision
  under its own review and tested locally (`10`), not a recommendation this module issues.
- **HRA stays a range, not a borrowed number.** With no local error-rate data, guide `05` outputs a
  **wide range** and flags *where* the highest-severity steps sit as **candidate** places to look;
  whether to add a defense there, and which, is the domain owner's call — not a Western HEP and not
  a prescribed "second check."
- **Defer, and refuse the false verdict.** The **clinical practice** stays with
  `clinical-medicine/11`; any **device** question with `biomedical-engineering/07`; **acceptance**
  with the hospital and its authority. The module does **not** certify the hospital "safe," rule on
  a past harm, or import a procedure — it supplies the transferable reasoning and names the resource
  constraints as latent conditions (`04`).
