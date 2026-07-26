---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-factors:overview
kind: guide
module: human-factors
section: human-factors
title: Human Factors - Overview and Discipline Map
status: source-custody
source_custody: partial
current_path: human-factors/00-OVERVIEW.md
canonical_path: human-factors/00-OVERVIEW.md
backsource_ids: [mdloom-backfill:human-factors:00-overview]
concepts: [human-factors, discipline-map, fit-load-frame, workload-sa-frame, error-safety-spine, ownership-boundaries, safety-ethics-contract, hci-hf-seam]
root_concepts: [human-factors]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Human Factors — Overview and Discipline Map

**This guide is the module's map, not a modeling guide.** It owns the **discipline
frame** (the fit/load and workload/SA views of the operator, and the error/safety
spine), the **ownership/defer matrix** that keeps every concept claimed exactly once,
the **HCI↔human-factors seam**, the **safety/ethics contract** that binds all twelve
guides, and the **reading order**. Every quantitative model, worked case, and standard
lives in a numbered guide; `00` shows *where* each lives and *why the boundaries fall
where they do*. **It builds on** nothing (it is the entry point) and **it hands** all
modeling to guides `01`–`11`. **It explicitly defers** — like every guide here —
product-form ergonomics to [`industrial-design/05-ERGONOMICS`](../industrial-design/05-ERGONOMICS.md),
cognitive mechanism to [`cognitive-science/`](../cognitive-science/00-OVERVIEW.md), interactive
digital usability to [`human-computer-interaction/`](../human-computer-interaction/00-OVERVIEW.md),
reliability mathematics to [`systems-engineering/06-FMEA-RELIABILITY`](../systems-engineering/06-FMEA-RELIABILITY.md),
clinical patient-safety practice to [`clinical-medicine/11`](../clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW.md),
and the domain systems to `nuclear/`, `aeronautics/`, `transportation/`, and
`biomedical-engineering/`.

> **Safety & ethics contract (binds every human-factors guide).** This is an
> **educational systems reference**, not an operations manual. Nothing in this module is
> an **operational instruction**, a **safety certification or compliance ruling**, an
> **accident or legal determination**, or an **individual fitness-for-duty or clinical
> assessment**. The modules supply **methods and evidence**; **acceptance and
> implementation of any real system belong to the accountable domain organization and its
> regulator**, never to a reference module. Every named model, standard, and stereotype is
> **attributed, dated, and bounded**.

*Per-guide banner: human factors is the study of **human performance, error, and safety in
the operation of complex systems**. Its models are bounded lenses with validity domains,
not universal constants — this overview names each lens and the guide that owns it.*

---

## The Big Picture: The Operator-and-Safety Layer of the Engineering Verticals

MAXIM's engineering modules design **systems**; human factors is the layer that asks
what happens when a **human body and mind operate them under real load, over time, and
when things go wrong**. It is organized around the **human-factors problem** (fit, load,
error, reliability, interface, automation, hazard, method, culture), **not** around a
domain — the single most important non-duplication decision in the module, because a
domain-first cut (aviation HF / medical HF / nuclear HF) would collide head-on with the
domain modules and force re-teaching their systems.

```
HUMAN FACTORS = TWO SPINES, JOINED  (this module owns the quantitative-systems view)
================================================================================
   FIT / LOAD SPINE                          ERROR / SAFETY SPINE
   the operator's body & mind vs demand      how work fails, and how systems defend
   ----------------------------------        ----------------------------------------
   02 PHYSICAL ergonomics/anthropometrics    04 human ERROR taxonomies
   03 COGNITIVE workload & SA                 05 human RELIABILITY analysis (HEP)
                                              08 SAFETY systems & HAZARD analysis
                                              11 organizational SAFETY CULTURE

                 \                    JOINED BY                    /
                  06 DISPLAY/CONTROL interface   07 AUTOMATION & function allocation
                 /                                                 \
   GROUNDED BY   10 METHODS & MEASUREMENT (how any of the above is measured)
   APPLIED BY    09 DOMAIN APPLICATIONS (apply the models, defer the systems)
   FRAMED BY     01 HISTORY & FOUNDATIONS      00 OVERVIEW (this map)
================================================================================
   Read it as: FIT/LOAD asks "can this person do this task, at what modeled load?"
   ERROR/SAFETY asks "how does it fail, how likely, and what defends it?" The
   interface (06) and automation (07) are where the two spines meet a real system;
   method (10) grounds them; domains (09) apply them; history (01) explains the idioms.
```

The two questions a human-factors analysis always asks — *supply vs demand* (can the
operator meet the load?) and *failure vs defense* (how does it break, and what catches
it?) — are the two spines. Everything else is where those questions touch hardware
(`06`/`07`), how they are measured (`10`), and where they are applied (`09`).

---

## 1. The Two Organizing Frames

### 1.1 Fit / load — the operator against the demand

```
FIT / LOAD FRAME  (guides 02, 03)
--------------------------------------------------------------------------------
   PHYSICAL (02)   body as a DISTRIBUTION vs physical demand
                   -> percentile/multivariate accommodation; occupational
                      biomechanics; bounded lifting/posture models; MSD dose-response
   COGNITIVE (03)  attention as SUPPLY vs mental demand
                   -> multiple-resource workload; NASA-TLX; vigilance; situation
                      awareness (SAGAT/SPAM/SART) measured, mechanism deferred
   INVARIANT: a fit that accommodates can still be overloaded; a light load can still
      exclude bodies that do not fit. Both a fit test AND a load test must pass.
```

### 1.2 Error / safety — how work fails and how systems defend

```
ERROR / SAFETY SPINE  (guides 04, 05, 08, 11)
--------------------------------------------------------------------------------
   ERROR (04)       classify the failure: slip/lapse/mistake; skill/rule/knowledge;
                    violation; latent condition -- error as a SYSTEMS property
   RELIABILITY (05) estimate it: human-error probability (HEP) as a wide, bounded
                    range (THERP/HEART/SPAR-H/CREAM); performance-shaping factors
   HAZARD (08)      defend against it: barriers/Swiss cheese; HAZOP/bow-tie;
                    human-inclusive FMEA; STAMP/STPA -- borrow FTA/FMEA from sys-eng
   CULTURE (11)     sustain the defenses: HRO; just culture; Safety-I vs Safety-II;
                    reporting; normalization of deviance
   INVARIANT: error is classified against a model, never moralized; a HEP is an
      estimate, not a fact; a barrier is a hypothesis, not a certificate.
```

---

## 2. The Twelve-Guide Map (what each guide uniquely owns)

| # | Guide | Uniquely owns (at peer depth) | Load-bearing models |
|---|---|---|---|
| 00 | Overview | this map; ownership/defer matrix; seam; safety contract; reading order | discipline map + matrix |
| 01 | History & Foundations | HF lineage and why it constrains today's idioms | dated lineage |
| 02 | Physical Ergonomics & Anthropometrics | body-as-distribution; occupational load | percentiles; NIOSH RNLE; RULA/REBA |
| 03 | Cognitive Workload & Situation Awareness | workload/SA *measurement in context* | MRT; NASA-TLX; SAGAT/SPAM/SART |
| 04 | Human-Error Taxonomies | classifying failure as a systems property | Reason GEMS; Rasmussen SRK |
| 05 | Human-Reliability Analysis | HEP as a bounded estimate; PSFs | THERP; HEART; SPAR-H; CREAM |
| 06 | Display, Control & Control-Room Design | the safety-critical operator interface | compatibility; EID; alarm standards |
| 07 | Automation & Human–Machine | levels of automation; the ironies; trust | Sheridan; PSW LOA; Bainbridge |
| 08 | Safety Systems & Hazard Analysis | barriers and structured hazard methods | Swiss cheese; bow-tie; STAMP/STPA |
| 09 | Domain Applications | apply the models, defer the systems | the apply-and-defer pattern |
| 10 | Methods & Measurement | how HF measures anything | HTA/CTA; observation; instrumentation |
| 11 | Organizational & Safety Culture | culture as a safety variable | HRO; just culture; Safety-II |

The **root concepts** the module owns, mapped one-to-one onto guides, are: *physical
fit/load* (`02`), *cognitive load/SA* (`03`), *error* (`04`), *reliability* (`05`),
*interface* (`06`), *automation* (`07`), *hazard* (`08`), *application* (`09`), *method*
(`10`), *culture* (`11`), plus the *lineage* (`01`) and the *map* (`00`).

---

## 3. Ownership / Defer Matrix (the coverage check — every concept claimed once)

The module's correctness as a *map* is a **MECE property**: every human-factors concept is
claimed by exactly one guide, and every adjacent discipline is deferred to exactly one
owner with no gap and no double-claim. This is the overview's "quantitative demonstration"
— a coverage check you can run against the manifest.

```
OWNERSHIP: every concept has exactly ONE human-factors owner (no gaps, no overlaps)
--------------------------------------------------------------------------------
   percentile/accommodation ...... 02      display/control compatibility .. 06
   occupational biomechanics ..... 02      alarm philosophy ............... 06
   workload measurement .......... 03      levels of automation ........... 07
   situation-awareness measurement 03      ironies of automation .......... 07
   error taxonomy (slip/mistake) . 04      barriers / defense-in-depth .... 08
   latent conditions ............. 04      HAZOP / bow-tie / STAMP-STPA ... 08
   human-error probability (HEP) . 05      cross-domain application ....... 09
   performance-shaping factors ... 05      task analysis / instrumentation  10
   just culture / HRO / Safety-II  11      the discipline's lineage ....... 01
```

| Adjacent area | Owner (defer to) | Human factors' relationship |
|---|---|---|
| Product-form ergonomics (handles, seats, knobs, universal design) | `industrial-design/05` | Defer; HF owns quantitative-systems depth (`02`) |
| Cognitive mechanism; psychophysical laws; SA/NDM as theory | `cognitive-science/` (esp. `09`) | Defer; HF owns operator-in-context measurement (`03`) |
| Interactive digital usability, IA/visualization, a11y evaluation | `human-computer-interaction/` | Defer (reciprocal seam); HF owns safety-critical interface (`06`) |
| FMEA/FTA and reliability mathematics/hardware | `systems-engineering/06` | Borrow; HF extends to the human (`05`, `08`) |
| Clinical patient-safety practice; diagnosis/treatment | `clinical-medicine/11` | Defer; HF owns generic error/culture/HRA (`04`,`05`,`11`) |
| Engineering biomechanics; medical-device engineering/regulation | `biomedical-engineering/01`,`/07` | Defer; HF owns occupational load & use-safety concepts |
| Domain systems (reactor safety, avionics, vehicle autonomy) | `nuclear/05`, `aeronautics/04`, `transportation/07` | Defer; HF applies principles (`06`,`07`,`09`) |
| Inferential statistics, sampling, power | `statistics-applied/` | Defer; HF owns study/measurement design (`10`) |
| Legal obligation, liability, compliance | `law/` | Defer; HF issues no legal/compliance ruling |
| General organizational theory | `organizational-behavior/` | Defer; HF owns safety culture specifically (`11`) |

**Coverage self-check (how a reviewer proves the map).** Pick any human-factors concept
and confirm exactly one guide claims it; pick any adjacent discipline and confirm exactly
one owner is named. If a concept has *no* owner, the map has a **gap**; if *two* guides
claim it, the map has an **overlap**. The manifest above is constructed so neither occurs —
e.g., "situation awareness" is *measured* only in `03` and *theorized* only in
`cognitive-science/09`; "FMEA" is *machinery* only in `systems-engineering/06` and
*human-extended* only in `08`.

---

## 4. The HCI ↔ Human Factors Seam (reciprocal, ratified)

A safety-critical console is **still an HCI system** — the "non-user operator" caricature
is rejected. The two modules divide **methods**, and neither owns **acceptance**.

```
SHARED SYSTEM (clinical device, avionics display, control-room touchscreen)
--------------------------------------------------------------------------------
   HCI owns ........ interaction design; usability; information architecture &
                     visualization; interactive accessibility; evaluation methods
   HF owns ......... operator workload/SA support; human-error consequence; alarm
                     philosophy; mode/state visibility; performance under stress/fatigue;
                     the safety analysis and the safety requirements it can STATE
   Domain owns ..... the system itself (nuclear/05, aeronautics/04, bme/07, transport/07)
   law/ owns ....... legal obligation and compliance duty
   -----------------------------------------------------------------------------
   EVIDENCE vs ACCEPTANCE: MAXIM modules supply methods & evidence, not sign-off.
   Acceptance and implementation belong to the accountable domain organization and
   its regulator. No reference module certifies or vetoes a real system.
```

---

## 5. The Safety / Ethics Contract (the module's hard gate)

1. **Educational systems reference** — no operational instructions (no lifting how-to, no
   operating procedures, no runnable operations).
2. **No certification or compliance ruling** — nothing declares a task, operator, or system
   safe/compliant/passing.
3. **No accident or legal determination** — event causation is a job for the module's
   error/hazard methods (`04`/`08`), never a label ("loss of SA," "human error").
4. **No individual fitness-for-duty or clinical assessment** — screening models are
   population-level estimates, never a medical judgment about a person.
5. **Attributed, dated, bounded** — every named model/standard/stereotype carries a date, an
   attribution, and an explicit validity domain.
6. **Accessibility as a safety requirement** — information a safe design depends on rides on
   **≥2 coding channels** (never color or text alone); the operator-safety twin of HCI's
   "don't rely on color alone" (`06`, §3).

This contract is *stricter* than HCI's, because human factors touches operations — lifting,
plant control, clinical work — where advice-creep is materially dangerous.

---

## 6. Reading Order & Paths

```
READING PATHS  (start at 00; then choose a spine)
--------------------------------------------------------------------------------
   FOUNDATIONS FIRST   00 -> 01 -> 02 -> 03        (frame + the fit/load spine)
   THE SAFETY SPINE    04 -> 05 -> 08 -> 11        (error -> reliability -> hazard -> culture)
   THE INTERFACE JOIN  03 -> 06 -> 07              (load/SA -> display -> automation)
   METHOD & APPLY      10 -> 09                    (how to measure -> where it applies)
   SHORTEST USEFUL     00 -> 04 -> 08              (what error is, how systems defend)
```

- **New to the discipline:** `00 → 01 → 02 → 03`, then the safety spine.
- **Here for safety analysis:** `04 → 05 → 08 → 11` (with `10` for how the evidence is
  gathered).
- **Here for an interface or automation decision:** `03 → 06 → 07`.
- **Here for a domain (aviation, healthcare, rail):** `09`, which *routes* you back to the
  model guides and *out* to the domain module.

---

## A Worked Routing Example — Decomposing One Real Question (illustrative, fictional)

*Fictional. It shows how the map routes a real question across guides and defers the parts
this module does not own — it is not an analysis of any real system.*

**The question.** *Beacon Rail* (invented) asks: "our new driver console had two
signals-passed-at-danger near-misses during night shifts — what does human factors say?"
The overview decomposes it; it does **not** answer it:

1. **Is it a fit/load problem?** Night-shift fatigue and workload → `03` (workload/SA
   measurement, vigilance decrement); physical reach/posture at the console → `02`.
2. **Is it an interface problem?** Signal salience, mode visibility, alarm philosophy →
   `06`; whether automation should intervene (and its ironies) → `07`.
3. **How does it fail, how likely, and what defends it?** Classify the near-miss →
   `04`; estimate the human-error contribution as a bounded HEP → `05`; model the barriers
   and where they were defeated → `08`.
4. **Is it a culture problem?** Whether near-misses are reported and learned from → `11`.
5. **How would any of this be measured?** Study/observation/simulation design → `10`.
6. **What does human factors NOT own?** The **signalling system itself** defers to
   `transportation/`; whether the console **is usable as a digital interface** defers to
   `human-computer-interaction/`; **legal duty** defers to `law/`; and **acceptance of any
   change** belongs to Beacon Rail and its regulator — no MAXIM module signs off.

**Reading.** The overview's job is exactly this **decomposition and routing** — turning one
messy question into owned sub-questions and honest deferrals, with no operating instruction
and no verdict about the real system.

---

## Reader Tasks (answerable from this guide)

1. **Run the coverage check.** Take three concepts — "vigilance decrement," "human-error
   probability," and "just culture" — and name the single guide that owns each; then take
   "FMEA" and "situation awareness *as a cognitive theory*" and name the *sibling* owner
   each defers to. Explain what a "gap" and an "overlap" would look like in the matrix (§2–3).
2. **Place a question on the two spines.** For "the operator is overwhelmed during an upset,"
   say which spine (fit/load vs error/safety) each part belongs to and which guides you would
   open first, and why the interface guide (`06`) is the join (§1, §6).
3. **Apply the seam.** For a control-room touchscreen, assign the interaction/accessibility
   *method* to HCI, the alarm/mode/workload **safety evidence** to human factors, the *system*
   to its domain owner, and **acceptance** to the accountable organization/regulator — and
   state why no module signs off (§4).
4. **Catch an advice-creep violation.** Given a draft sentence "therefore the console is safe
   to deploy," identify which contract clause it breaks and rewrite it as an
   evidence-and-acceptance statement (§5).
5. **Choose a reading path.** For a reader who only needs "what error is and how systems
   defend against it," give the shortest useful path and justify the omissions (§6).

---

## Decision Cheat Sheet

| If your question is about... | Go to guide | Because it owns... |
|---|---|---|
| Whether a population of bodies fits a workstation/task | `02` | percentile/multivariate accommodation; occupational load |
| Whether the operator can meet the mental demand | `03` | workload & SA *measurement in context* |
| What kind of failure just happened | `04` | the error taxonomy (as a systems property) |
| How likely a human error is (as a range) | `05` | human-error-probability estimation; PSFs |
| Whether the display/control makes the right action obvious | `06` | safety-critical interface design |
| Whether to automate, and what that breaks | `07` | levels of automation; the ironies; trust |
| How the system fails and what defends it | `08` | barrier & structured hazard methods |
| How this plays out in aviation/healthcare/rail | `09` | apply-and-defer across domains |
| How any of this would be measured | `10` | task analysis, observation, instrumentation |
| Whether the organization learns and stays safe | `11` | safety culture; HRO; Safety-II |
| The *shape* of a handle/knob/seat | `industrial-design/05` | product-form ergonomics (deferred) |
| *Why* attention/memory behave as they do | `cognitive-science/` | cognitive mechanism (deferred) |
| Whether an interactive UI is *usable/accessible* | `human-computer-interaction/` | digital usability (deferred) |
| "Is this system certified / safe / legal?" | **out of scope** | acceptance is the org's + regulator's |

---

## Common Confusion Points

**"Human factors is just ergonomics (the shape of things)."** Product-form ergonomics is
one entry (`industrial-design/05`). This module owns the *quantitative-systems* view:
distributions, workload/SA measurement, error taxonomy, reliability estimation, hazard
analysis, and safety culture (§1–2).

**"Human error is the cause."** In this module "human error" is a *starting point for
analysis*, classified against a model and traced to latent conditions and defeated barriers
(`04`,`08`) — never an endpoint, a blame verdict, or an accident ruling (§5).

**"The module can tell me if my system is safe."** No. It supplies **methods and evidence**;
**acceptance belongs to the accountable organization and its regulator** (§4–5). A low
lifting index, a low HEP, or a clean bow-tie is evidence, not a certificate.

**"Situation awareness / workload are things you can read off directly."** They are
**constructs measured by proxy** with confounds and validity domains (`03`); the overview's
job is to keep them measured, not reified.

**"Organize human factors by domain (aviation HF, medical HF)."** That collides with the
domain modules and re-teaches their systems. The module organizes by the *human-factors
problem*; guide `09` is the single deliberately domain-organized guide, and it *applies and
defers* (§2, guide `09`).

---

## Global, WEIRD & Resource Caveats

- **The data and instrument canon is WEIRD/Western-industrial/military-skewed** —
  anthropometry (ANSUR/CAESAR), workload/SA validation samples (TLX/SAGAT), alarm-management
  standards, and population stereotypes are all culture- and era-bound. Every numbered guide
  carries the specific caveats and a non-WEIRD contrasting case; the overview's job is to flag
  that the skew is *module-wide*, not incidental.
- **Method availability is resource-dependent** — scanners, EEG, simulators, and alarm
  platforms shape which of the module's methods a given organization can actually use;
  low-resource practice reuses foreign tables/instruments, magnifying error. The correction is
  stated uncertainty, not a borrowed constant (see `10`).
- **The safety contract is not a Western nicety** — "no certification, no accident ruling, no
  fitness verdict" applies everywhere the module is read; acceptance always belongs to the
  local accountable organization and regulator.
