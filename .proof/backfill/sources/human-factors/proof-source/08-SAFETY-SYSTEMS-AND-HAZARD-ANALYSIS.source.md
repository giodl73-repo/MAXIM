---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "08-SAFETY-SYSTEMS-AND-HAZARD-ANALYSIS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-factors:safety-systems-and-hazard-analysis
kind: guide
module: human-factors
section: human-factors
title: Safety Systems & Hazard Analysis - Barriers, Bow-Ties, and Control-Theoretic Methods
status: source-custody
source_custody: partial
current_path: human-factors/08-SAFETY-SYSTEMS-AND-HAZARD-ANALYSIS.md
canonical_path: human-factors/08-SAFETY-SYSTEMS-AND-HAZARD-ANALYSIS.md
backsource_ids: [proof-backfill:human-factors:08-safety-systems-and-hazard-analysis]
concepts: [defense-in-depth, swiss-cheese-model, barrier-analysis, hazop, bow-tie, human-inclusive-fmea, stamp-stpa]
root_concepts: [safety-systems-hazard-analysis]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Safety Systems & Hazard Analysis — Barriers, Bow-Ties, and Control-Theoretic Methods

**This guide owns** the *structured methods that reason about how a socio-technical system
fails and what defends it*, with the **human included as both a barrier and a source of
hazard**: **barrier / defense-in-depth** models (Reason's Swiss cheese; Hollnagel's barrier
taxonomy), **hazard-identification** methods (HAZOP guide-words, what-if), the **human-inclusive
FMEA**, the **bow-tie** (threats → top event → consequences with preventive and mitigative
barriers), and the **control-theoretic** methods (**STAMP/STPA**) that model accidents as
inadequate control rather than component-failure chains — plus **safety-case reasoning as a
concept**. **It builds on** `04-HUMAN-ERROR-TAXONOMIES` (the failures being defended against) and
`05-HUMAN-RELIABILITY-ANALYSIS` (the HEP that quantifies a human barrier), and hands sustained
defense to `11-ORGANIZATIONAL-SAFETY-CULTURE`. **It explicitly borrows** the **fault-tree /
event-tree combination math, cut sets, and the FMEA/RPN machinery** from
[`systems-engineering/06-FMEA-RELIABILITY`](../systems-engineering/06-FMEA-RELIABILITY.md) — this
guide *extends those tools to the human* and does **not** re-derive them. **It explicitly defers**:
the **domain safety systems themselves** (reactor protection/ECCS to
[`nuclear/05`](../nuclear/05-SAFETY-SYSTEMS.md), avionics safety to
[`aeronautics/04`](../aeronautics/04-AVIONICS.md), vehicle safety to
[`transportation/07`](../transportation/07-AUTONOMOUS-VEHICLES.md), device safety to
[`biomedical-engineering/07`](../biomedical-engineering/07-MEDICAL-DEVICES.md)); the
**legal/regulatory duty** to `law/`; and **inferential statistics** to
[`statistics-applied/`](../statistics-applied/00-OVERVIEW.md).

> **Safety & ethics contract (binds every human-factors guide).** This is an **educational
> systems reference**. A hazard analysis here is a **structured way to reason**, **not** a safety
> certification, a compliance sign-off, an accident-cause ruling, or a licence. Nothing declares a
> system "safe," "adequate," or "compliant." The methods produce **evidence and requirements**;
> **acceptance of any safety case belongs to the accountable organization and its regulator**,
> never to this module.

*Per-guide banner: every barrier is a **fallible hypothesis**, every probability a **bounded
estimate** (guide `05`), and every method a **lens that finds *some* hazards, not all**. A clean
analysis is evidence of diligence, not proof of safety — the absence of a found hazard is not the
presence of safety.*

---

## The Big Picture: Two Views of Failure — Chains and Control

Hazard analysis has two mental models, and mature practice uses both. The **linear/barrier**
view sees an accident as a **trajectory** that pierces successive defenses (Swiss cheese); the
**systemic/control** view sees it as **inadequate control** of a system whose components may each
be "working" (STAMP). The first is excellent for *energy/loss-of-containment* hazards with
identifiable barriers; the second is essential for *software-, automation-, and coordination-rich*
systems where no component "failed."

```
TWO VIEWS OF FAILURE  (use both; each sees what the other misses)
================================================================================
   LINEAR / BARRIER VIEW (Reason, Hollnagel)     SYSTEMIC / CONTROL VIEW (Leveson STAMP)
   -----------------------------------------     ---------------------------------------
   hazard -> a TRAJECTORY passes through holes    accident = inadequate CONTROL of the
   in successive barriers (defense-in-depth):     socio-technical system: unsafe control
                                                   actions + missing feedback, even when
     [barrier][barrier][barrier] -> LOSS          every COMPONENT is "working"
        holes line up  ^                          controller -> (control action) -> process
                                                   process  -> (feedback) -> controller
   Good for: energy/containment, clear barriers   Good for: software/automation/coordination,
   Tools: bow-tie, HAZOP, FMEA, FTA/ETA           where "nothing failed" but the system did
   ================================================================================
   HUMAN ROLE in both: the human is a BARRIER (a fallible one -- its failure prob is the
   HEP of guide 05) AND a CONTROLLER (whose unsafe control actions STPA hunts) AND a source
   of the LATENT CONDITIONS (guide 04) that pre-open the holes.
```

The prospective/retrospective distinction matters too: these methods are mainly **prospective**
(find hazards *before* harm). Using the *same* structures to explain an event after the fact is
legitimate analysis — but naming a cause or apportioning blame is **not** this module's to do
(safety contract).

---

## 1. Barriers and Defense-in-Depth

- **Reason's Swiss-cheese model** (`04`): defenses are layered; each has holes (latent + active);
  an accident needs the holes to **momentarily align**. Its lesson is *defense-in-depth* —
  independent layers so one hole is not a path — and its trap is *false independence* (holes that
  share a common cause line up together).
- **Hollnagel's barrier taxonomy** (*Barriers and Accident Prevention*, **2004**): barriers are
  **physical** (a bund, an interlock), **functional** (a trip needing a condition), **symbolic**
  (a sign, an alarm, a label — requires interpretation), or **incorporeal** (a rule, a norm —
  requires knowing and choosing). Symbolic/incorporeal barriers can be more dependent on
  interpretation, training, context, and organizational conditions; their reliability must be
  assessed in the actual system rather than assumed from a universal hierarchy.

```
BARRIER TYPES  (Hollnagel -- a classification by NATURE, not a universal strength ranking)
--------------------------------------------------------------------------------
   PHYSICAL     interlock, bund, relief valve        acts without a human
   FUNCTIONAL   trip on a condition, lockout          acts if the logic/sensing holds
   SYMBOLIC     alarm, sign, label, warning light     needs perceiving + reading
   INCORPOREAL  rule, procedure, norm                 needs knowing + choosing
   -----------------------------------------------------------------------------
   NOT A UNIVERSAL RANKING: these are categories by TYPE, not a fixed reliability order.
   Human-interpretation-dependent barriers (symbolic/incorporeal) TEND to fail more quietly,
   but a specific barrier's reliability depends on DESIGN, MAINTENANCE, DEMAND RATE, and
   CONTEXT and must be ASSESSED -- a corroded relief valve or a defeated interlock can be
   worse than a well-drilled procedure. Do not read strength off the category.
   DESIGN LESSON: do not rest safety on a SINGLE barrier of any type, and beware barriers
   that SHARE a failure (see dependency/common-cause, Worked pass); if a barrier depends on
   the operator PERCEIVING it, ride the signal on >=2 channels (guide 06) -- a single alarm
   tone or a single color is a single point of failure.
```

---

## 2. Hazard Identification — HAZOP and What-If

Before you can defend, you must **enumerate** hazards. The workhorse is structured imagination.

- **HAZOP** (Hazard and Operability study; origin ICI, **1960s–70s**; codified in **IEC 61882**):
  apply **guide words** — *No, More, Less, Reverse, As-well-as, Part-of, Other-than, Early/Late* —
  to each process parameter (flow, pressure, level, temperature) at each node, and ask what a
  deviation would cause. Its power is **completeness through discipline**; its cost is time and the
  quality of the team.
- **What-if / checklist**: lighter, less exhaustive prompts. Faster, less complete.

The **human-factors extension** is to apply the same guide-word discipline to **human actions and
information** — *action performed No / More / Less / Reverse / Early / Late*, *information Missing /
Wrong / Late* — so operator deviations are enumerated as first-class hazards, not bolted on.

---

## 3. The Human-Inclusive FMEA (machinery borrowed from `systems-engineering/06`)

**FMEA** (Failure Modes and Effects Analysis; the RPN mechanics and standard form are
`systems-engineering/06`'s, e.g. **MIL-STD-1629A, 1980**) lists each failure mode and scores
**Severity × Occurrence × Detection = RPN**. The human-factors contribution is to include **human
failure modes** (slip/lapse/mistake/violation from `04`) as rows, using the **HEP** (guide `05`)
to inform *Occurrence* and the **detectability of the error** (feedback design, `06`) to inform
*Detection*.

```
HUMAN-INCLUSIVE FMEA ROW  (form + RPN math are sys-eng/06's; the HUMAN rows are 04/05/06)
--------------------------------------------------------------------------------
   failure mode (04)     S (1-10)  O (from HEP, 05)  D (from feedback, 06)  RPN = SxOxD
   omit re-arm guard        8          6                 7                     336
   -----------------------------------------------------------------------------
   CAUTION on RPN: S,O,D are ORDINAL, so multiplying them is not a true risk number --
   equal RPNs can mean very different risks, and RPN hides severity. Use RPN to TRIAGE,
   never as an acceptance threshold. (This critique is inherited with the tool from sys-eng/06.)
```

---

## 4. The Bow-Tie — Threats, Top Event, Consequences

The **bow-tie** (Shell/ICI lineage, **1970s–90s**) is the field's most legible barrier picture:
a **top event** (loss of control) in the centre, **threats** on the left with **preventive
barriers**, and **consequences** on the right with **mitigative barriers**. It is, structurally, a
**fault tree** (left) joined to an **event tree** (right) at the top event — so the *combination
math is `systems-engineering/06`'s*; the bow-tie adds the **barrier semantics and the human's
place in them**.

---

## 5. STAMP / STPA — Accidents as Inadequate Control

For automation- and software-rich systems, component-failure methods miss the accidents where
**nothing failed** but the system was mis-controlled. **STAMP** (Leveson, *Engineering a Safer
World*, MIT Press **2011**; foundational paper, *Safety Science* **2004**) models the system as a
**control structure** and
looks for **Unsafe Control Actions (UCAs)**: a control action **provided when it shouldn't be**,
**not provided when needed**, **wrong timing/order**, or **wrong duration**. **STPA** (the
analysis method; STPA Handbook, Leveson & Thomas, **2018**) walks the control structure to derive
UCAs and their **causal scenarios** — including inadequate feedback, wrong mental models (`04`),
and mode confusion (`06`, `07`).

```
STPA IN ONE PICTURE  (the human is a CONTROLLER, not just a barrier)
--------------------------------------------------------------------------------
   CONTROLLER (human or automation) --- control action ---> CONTROLLED PROCESS
        ^                                                        |
        |------------------ feedback (may be missing/wrong) -----|
   UNSAFE CONTROL ACTIONS (UCA):
      (1) provided when unsafe   (2) NOT provided when needed
      (3) wrong timing/order     (4) applied too long / stopped too soon
   CAUSAL SCENARIOS include: wrong MENTAL MODEL (04), missing/late FEEDBACK, MODE
   confusion (06/07), and coordination gaps between multiple controllers.
   -----------------------------------------------------------------------------
   Why it matters for HF: STPA treats the operator's mental model and the interface's
   feedback as first-class safety-control elements -- exactly the module's concerns.
```

**Safety-case reasoning (as a concept).** A safety case marshals **claim → argument → evidence**
(e.g., Goal Structuring Notation, Kelly, **1998**) to argue a system is acceptably safe. This
guide teaches the *reasoning structure* — how the methods above become evidence in an argument —
and pointedly does **not** construct or endorse a real safety case: **the argument is the
organization's and the acceptance is the regulator's**.

---

## The Boundaries (ownership in one place)

```
WHO OWNS WHAT AROUND HAZARD ANALYSIS
--------------------------------------------------------------------------------
   this guide (08)     the METHODS with the human in them: barriers, HAZOP-for-humans,
                       human-inclusive FMEA, bow-tie semantics, STAMP/STPA, safety-case shape
   systems-engineering/06  the MATH: FTA/ETA gates & cut sets, FMEA/RPN mechanics, reliability
   04 (error)          the human failure MODES enumerated
   05 (HRA)            the HEP that quantifies a human barrier
   06 (interface)      the FEEDBACK/mode design that a barrier's detection depends on
   11 (culture)        sustaining barriers over time; Safety-II/FRAM
   nuclear/05, aeronautics/04, transportation/07, bme/07   the domain safety SYSTEMS
   law/                legal/regulatory duty
   -----------------------------------------------------------------------------
   Rule: this guide STRUCTURES the reasoning and places the human in it; it borrows the
   tree/RPN math, certifies nothing, and rules no accident.
```

---

## A Worked Bow-Tie Pass — One Quantified Branch (reproducible)

*All numbers are **synthetic**; the combination arithmetic is reproducible and the tree math is
`systems-engineering/06`'s. This demonstrates the *structure*, not a risk assessment, and it
certifies nothing.*

**The bow-tie (synthetic).** Top event: **loss of containment from tank T**. One threat on the
left — **overfill** — with two **preventive barriers**: a **hardware high-level trip** and an
**operator response to the level alarm**. On the right, the consequence **environmental release**
is reduced by a **mitigative barrier**: a **bund (containment dike)**.

```
BOW-TIE (synthetic; one threat branch quantified)
--------------------------------------------------------------------------------
   THREAT                PREVENTIVE BARRIERS         TOP EVENT      MITIGATIVE   CONSEQUENCE
   overfill  --> [HW high-level TRIP] [OPERATOR alarm  loss of  --> [BUND]  --> env. release
   demand         PFD = 0.01           response]        contain-      fails
   f = 0.1/yr                          HEP ~ 0.29        ment          0.05
                                       (guide 05, bounded)
```

**Left side — probability of the top event via this threat (per year), if barriers were
independent.** The AND-combination of independent barrier failures is `systems-engineering/06`'s
gate math:

```
TOP-EVENT FREQUENCY VIA OVERFILL  (independent-barrier assumption FIRST)
--------------------------------------------------------------------------------
   f(top | overfill) = f(demand) x PFD(trip) x HEP(operator)
                     = 0.1 /yr    x 0.01      x 0.29
                     = 2.9e-4 /yr   (~1 in 3,450 years, POINT estimate)
--------------------------------------------------------------------------------
   Then propagate the RANGE (never a point): the HEP is a bounded ~0.06 to ~0.8 (guide 05's
   truncated model -- the upper is bounded BELOW 1, not median x EF), so f(top) plausibly
   spans ~6e-5 to ~8e-4 /yr from the human term ALONE.
```

**The dependency correction (the point of the pass).** The trip and the operator **both read the
same level instrument**. If that instrument fails, **both** barriers fail together — a
**common-cause** coupling. Treating them as independent (the calc above) **understates** the top-
event frequency, because the `0.01 × 0.29` term wrongly assumes the two are unrelated. A defensible
analysis **decomposes each barrier into a shared and an independent part**:

```
WITH COMMON-CAUSE  (decompose each barrier: shared-instrument part + independent part)
--------------------------------------------------------------------------------
   Both barriers READ THE SAME LEVEL INSTRUMENT. Decompose each barrier's failure into:
     (i)  a SHARED-instrument failure  -> defeats BOTH barriers together (common-cause)
     (ii) an INDEPENDENT failure       -> the trip's own logic/actuator, or the operator's
                                          own diagnosis/action, GIVEN a working instrument
   f(top) ~= f(demand) x [ P(shared-instrument CCF)                 (defeats BOTH)
                          + PFD_indep(trip) x HEP_indep(operator) ] (both fail on their own)
   e.g. P(shared CCF) = 0.005 ; PFD_indep x HEP_indep ~ 0.01 x 0.29 = 0.0029
        f(top) ~= 0.1 x (0.005 + 0.0029) ~= 0.1 x 0.0079 = 7.9e-4 /yr
   -----------------------------------------------------------------------------
   Reading: the common-cause term (0.005) now DOMINATES the independent term (0.0029) and
   nearly TRIPLES the top-event frequency vs the independent-only 2.9e-4. "Two barriers"
   that share an instrument are closer to ONE. Defense-in-depth requires INDEPENDENCE, which
   this design lacks. (A fuller model uses a beta-factor split; this screening decomposition
   suffices to show the direction and the dominance.)
```

**Right side (consequence).** If the top event occurs, the bund (mitigative barrier, fail
probability 0.05) reduces the fraction reaching the environment: `f(env release) ≈ f(top) ×
0.05`. With `f(top) ≈ 7.9e-4/yr`, `f(env release) ≈ 4.0e-5/yr` — again a **range**, not a point.

**Uncertainty / validity / bias note.** (1) The frequencies and PFDs are **synthetic**; the HEP
range is from guide `05`'s bounded estimate. (2) The headline lesson is **dependency**: the
biggest error in barrier analysis is assuming independence, which *understates* risk — exactly the
Swiss-cheese "holes line up via a common cause" failure. (3) The analysis finds **only the hazards
enumerated** (here, one threat); a real bow-tie has many threats and the method's completeness
depends on the HAZOP/team quality (§2). (4) This is a **structured estimate for reasoning**, not a
risk acceptance — whether `4e-5/yr` is "tolerable" is the **organization's and regulator's**
decision, informed by evidence.

---

## A Fully Worked Case — Hazard Analysis of a Console Change (illustrative, fictional)

*Fictional. It demonstrates the methods — not an analysis, certification, or acceptance of any
real system.*

**Setting.** *Fictional* **Marsh Junction** adds an automated interlock to a water-treatment
console. Human factors runs a hazard analysis of the *change*:

1. **Enumerate with HAZOP-for-humans (§2).** Apply guide words to the operator's actions and to
   the interlock's information: action *Not done / Done late*, information *Missing / Wrong mode*.
   This surfaces a hazard the hardware FMEA missed: the interlock's **mode is ambiguous**, inviting
   a mode-error (`06`, `07`).
2. **Build the bow-tie (§4).** Top event "unsafe valve state." Preventive barriers: the interlock
   (functional), the operator's alarm response (symbolic + human). The analysis flags that the
   interlock and the operator **share the same sensor** — a dependency to model, not to assume away
   (§Worked pass).
3. **Quantify one branch honestly (§Worked pass).** Combine the demand rate, interlock PFD, and the
   operator HEP **as a range**, then add the **common-cause** term for the shared sensor — showing
   the "two barriers" are closer to one, and that the change's benefit is smaller than it looks.
4. **Run STPA on the automation (§5).** Because a new automated controller is involved, derive
   **UCAs**: interlock *acts when it shouldn't* (spurious trip → operator works around it → new
   hazard), or *doesn't act when needed* (silent). Trace causal scenarios to **feedback gaps** and
   **mode confusion** — routing the fixes to `06` (visible mode on ≥2 channels) and `07` (calibrated
   trust).
5. **Assemble evidence, not a verdict (§5).** The outputs are **hazards, barriers, a bounded
   frequency range, and requirements** ("make the interlock mode continuously visible";
   "break the sensor common-cause"). Whether Marsh Junction's safety case is **accepted** is the
   utility's and its regulator's call; the **treatment plant system** stays with its domain owner;
   the module **signs off nothing**.

**Reading.** Two complementary views (barrier + control), one honestly-bounded quantified branch
with dependency exposed, human failure modes enumerated as first-class — and evidence handed up,
not a certificate issued.

---

## Reader Tasks (answerable from this guide)

1. **Classify barriers and assess contextual reliability.** Given an interlock, an alarm light,
   and a written rule, classify them using Hollnagel's taxonomy and identify the dependencies,
   failure modes, and local evidence needed before comparing their reliability
   — and why a detection-dependent barrier needs ≥2 channels (§1).
2. **Quantify a bow-tie branch and its range.** With demand `0.1/yr`, trip PFD `0.01`, and operator
   HEP `0.29` (bounded range ~0.06–0.8, guide `05`), compute the independent top-event frequency and
   its range; then add a common-cause term of `0.005` and explain why it dominates (§Worked pass).
3. **Catch the independence error.** Explain why "we have a trip *and* an operator, so multiply
   their failure probabilities" understates risk when both read the same sensor, and how
   defense-in-depth requires independence (§1, §Worked pass).
4. **Derive a UCA with STPA.** For an automated interlock, give one Unsafe Control Action of each
   type (provided-when-unsafe; not-provided-when-needed) and trace one to a feedback/mode-confusion
   causal scenario, routing the fix to `06`/`07` (§5).
5. **Hold the boundary.** State which parts of the console analysis are this guide's (methods,
   human failure modes, barrier semantics), which are `systems-engineering/06`'s (the tree/RPN
   math), and who owns *acceptance* of the safety case (Boundaries, Worked case).

---

## Decision Cheat Sheet

| Situation | Method | Why (this guide) |
|---|---|---|
| Enumerate hazards on a process | **HAZOP** guide-words (incl. human actions) | disciplined completeness (§2) |
| Score/triage many failure modes incl. human | **human-inclusive FMEA** (S×O×D) | RPN triages; *never* an acceptance threshold (§3) |
| Show threats→event→consequences with barriers | **bow-tie** | legible barrier picture; math is sys-eng/06's (§4) |
| Software/automation/coordination-rich system | **STAMP/STPA** (UCAs) | catches "nothing failed" accidents (§5) |
| "We have two barriers, so we're safe" | check **independence / common cause** | shared instrument ≈ one barrier (§1, Worked pass) |
| A barrier depends on the operator noticing | assess redundant cues, dependencies, and local reliability evidence | category alone does not determine strength (§1) |
| Asked for "the risk number" | give a **range** from the HEP + a dependency note | HEP is bounded (§Worked pass, `05`) |
| Combining human and hardware failures | hand the tree math to **`systems-engineering/06`** | HF places the human; sys-eng combines (Boundaries) |
| "Is this system safe / certified / compliant?" | **out of scope** — org + regulator decide | safety contract |

---

## Common Confusion Points

**"Two barriers means twice the safety."** Only if they are **independent**. Barriers that share a
sensor, a power supply, a procedure, or an operator's mental model fail **together** — the
common-cause that makes Swiss-cheese holes line up. Assuming independence **understates** risk
(§1, Worked pass).

**"A clean hazard analysis proves the system is safe."** It proves the **enumerated** hazards were
considered. The method finds *some* hazards, bounded by team and guide-word quality; absence of a
found hazard is not presence of safety (banner, §2).

**"RPN is a risk number."** Its inputs are **ordinal**, so the product is not a true risk and can
rank equal-RPN items that carry very different severity. RPN **triages**; it is never an acceptance
threshold (§3; critique inherited from `systems-engineering/06`).

**"STAMP is just a fancier fault tree."** No — it is a **different paradigm**: accidents as
inadequate **control**, not chains of component failures. It finds accidents where every component
"worked," which fault trees miss (§5).

**"The analysis certifies the system."** It produces **evidence and requirements**. Building the
safety-case *argument* is the organization's job and **accepting** it is the regulator's; the
module constructs neither (safety contract, §5).

---

## Global, WEIRD & Resource Caveats

- **The methods and their data are Western process/nuclear/aerospace in origin.** HAZOP (UK
  chemicals), FMEA (US defense), STAMP (US academia), bow-tie (oil/gas) carry the assumptions of
  well-resourced, heavily-instrumented, procedure-rich industries. The *reasoning* transfers; the
  assumption of abundant sensors and formal teams does not.
- **Barrier choice is resource-constrained.** Physical, functional, symbolic, and
  incorporeal barriers have different dependencies, costs, and failure modes; no category
  is universally strongest. Low-resource settings may rely more heavily on signs, rules,
  or human coordination, so the analysis must expose their local reliability evidence and
  latent dependencies (`04`) rather than assuming effectiveness from category.
- **Completeness depends on who is in the room.** HAZOP/STPA quality tracks the diversity and
  experience of the analysis team; a thin team or a suppressed voice (a reporting culture problem,
  `11`) systematically misses hazards — a bias in the method itself, not just its inputs.

---

## A Contrasting Example (non-WEIRD, low-resource)

*Fictional, to show barrier reasoning where instrumentation is scarce.*

**Setting.** A *fictional* small-scale grain-drying cooperative faces a dust-explosion hazard but
cannot afford the instrumented suppression systems assumed by Western HAZOP templates.

**How the reasoning pattern applies (without issuing barrier advice).**
- **Barrier TYPE vs count is a concept to reason with, not a prescription.** The analysis notes,
  *as a hypothesis*, that a pile of human-interpretation-dependent barriers (signs, a rule, a lone
  alarm) can give **illusory** defense-in-depth (§1) — but **which** barriers actually suit a
  dust-explosion hazard is out of this module's scope. A combustible-dust hazard is governed by its
  own standards and belongs in a **domain hazard review / Management of Change (MoC)** owned by the
  cooperative and the competent authority; the module names candidate *questions*, not answers, and
  issues **no** barrier advice.
- **Human-inclusive HAZOP with tacit procedures.** With no written SOPs, the guide-word pass must
  first **elicit** the actual work-as-done (guide `10`) before it can ask "action *Not done / Late*"
  — otherwise it mislabels skilled adaptation.
- **Honest bounds, no false verdict.** The bow-tie carries **wide** frequency ranges (sparse local
  data), the analysis **names resource constraints as latent conditions** rather than assuming
  absent barriers, and it **defers acceptance — and any barrier selection —** to the cooperative,
  its dust-hazard standards, and the competent authority via MoC. It does **not** certify the dryer
  "safe," rule on a past incident, or recommend a specific barrier — it structures the *evidence and
  questions* the owners take into their own hazard review.
