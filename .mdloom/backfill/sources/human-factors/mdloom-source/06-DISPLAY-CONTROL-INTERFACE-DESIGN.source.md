---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "06-DISPLAY-CONTROL-INTERFACE-DESIGN.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-factors:display-control-interface-design
kind: guide
module: human-factors
section: human-factors
title: Display, Control & Control-Room Design - The Safety-Critical Operator Interface
status: source-custody
source_custody: partial
current_path: human-factors/06-DISPLAY-CONTROL-INTERFACE-DESIGN.md
canonical_path: human-factors/06-DISPLAY-CONTROL-INTERFACE-DESIGN.md
backsource_ids: [mdloom-backfill:human-factors:06-display-control-interface-design]
concepts: [display-control-compatibility, population-stereotypes, coding-redundancy, alarm-philosophy, ecological-interface-design, control-room-layout, mode-visibility]
root_concepts: [display-control-interface-design]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Display, Control & Control-Room Design — The Safety-Critical Operator Interface

**This guide owns** the *human-factors design of the safety-critical operator interface*:
**display–control compatibility** (stimulus–response and movement compatibility, Warrick's
principle); **population stereotypes and their cultural limits**; **coding and redundancy**
(the sensory dimensions available for information, and why color alone is unsafe); **alarm
philosophy** (the alarm system as its own hazard — flood, nuisance/standing/chattering
alarms, rationalization, prioritization, and the dated industry standards that bound it);
**salience vs nuisance** (the attention budget and the cry-wolf cost of over-alerting);
**mode and state visibility** (mode error and automation surprise); **ecological interface
design** (Rasmussen's skill/rule/knowledge and the abstraction hierarchy); and
**control-room / workspace layout** (importance, frequency, sequence, and function). **It
builds on** `03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS` (displays support SA and manage
load) and hands automation trade-offs to `07` and safety analysis to `08`. **It explicitly
defers**: *general digital-interface usability, interaction design, information
architecture, and accessibility evaluation* to
[`human-computer-interaction/`](../human-computer-interaction/08-ACCESSIBILITY-INCLUSIVE-DESIGN.md);
the *domain systems themselves* — reactor protection and safety systems to
[`nuclear/05-SAFETY-SYSTEMS`](../nuclear/05-SAFETY-SYSTEMS.md), avionics/flight-deck systems to
[`aeronautics/04-AVIONICS`](../aeronautics/04-AVIONICS.md), medical-device engineering and
regulation to [`biomedical-engineering/07-MEDICAL-DEVICES`](../biomedical-engineering/07-MEDICAL-DEVICES.md),
vehicle autonomy to [`transportation/07`](../transportation/07-AUTONOMOUS-VEHICLES.md);
*perceptual/psychophysical mechanism* (Fitts, Hick, perception) to
[`cognitive-science/`](../cognitive-science/00-OVERVIEW.md); and *product-form control shaping*
(knob form, grip) to [`industrial-design/05-ERGONOMICS`](../industrial-design/05-ERGONOMICS.md).

> **Safety & ethics contract (binds every human-factors guide).** This is an
> **educational systems reference**, not an operations manual. It contains **no runnable
> operating procedures** (nothing here tells anyone how to operate a plant, fly, treat a
> patient, or respond to a specific alarm), **no safety certification** (no design here is
> declared "safe" or "compliant"), **no accident or legal determination**, and **no
> individual assessment**. Named standards and stereotypes are **dated, industry- and
> culture-specific context**, bounded — never a certification, a legal duty, or a universal
> rule.

*Per-guide banner: every design principle below is a **population- and context-dependent**
tendency, attributed and dated where it names a study or standard. A "stereotype," an alarm
rate, and a coding convention are engineering guidance for a specified population and
domain, not a human universal and not a compliance verdict.*

---

## The Big Picture: The Interface Is Where Workload, SA, and Error Meet the World

The operator interface is the **surface** where everything else in human factors becomes
physical: it is where the situation is made perceptible (feeding SA, guide 03), where
attention is spent (workload, guide 03), where an action either matches the operator's
expectation or invites an error (guide 04), and where automation announces — or hides — its
state (guide 07). Safety-critical interface design is therefore not "make it pretty" or even
"make it usable"; it is **shaping perception and action so that the right state is obvious
and the right action is natural, under load, under stress, at 3 a.m.** Two questions drive
every decision: *does the interface make the true state and the required action
**compatible** with the operator's expectations and the work's structure?* and *does it
**spend the operator's limited attention** on what matters, without flooding or crying
wolf?*

```
THE SAFETY-CRITICAL OPERATOR INTERFACE   (this guide owns the HF design layer)
================================================================================
   WORLD / PROCESS                                        OPERATOR
   (plant, aircraft, patient, grid)                       (loaded, stressed, on shift)
        |   sensors                                            ^   actions
        v                                                      |
   +-- DISPLAYS ------------------+          +-- CONTROLS ------------------+
   | make state PERCEPTIBLE (L1)  |          | make the right action        |
   | show MEANING/RELATIONS (L2)  |          | NATURAL and COMPATIBLE        |
   | show TRENDS/PROJECTION (L3)  |          | resist the wrong action       |
   | ALARMS: only what matters    |          | show the active MODE/STATE    |
   +------------------------------+          +------------------------------+
        |                                              |
        +---- CODING + REDUNDANCY (color+shape+position+label) ----+
        +---- LAYOUT (importance / frequency / sequence / function) +
        +---- EID (make the work-domain CONSTRAINTS visible: SRK)  -+
================================================================================
   SEAM: general DIGITAL usability & accessibility -> human-computer-interaction/
         the DOMAIN systems themselves -> nuclear/05, aeronautics/04, bme/07, transport/07
   THIS GUIDE -> the HF principles that make the SAFETY-CRITICAL interface work.
```

The layers below go compatibility → stereotypes → coding → alarms → salience → modes →
EID → layout → the HCI seam, then a worked case and the reader aids.

---

## 1. Compatibility — Making the Right Action Obvious

**Compatibility** is the degree to which the relationship between a display (or a control)
and its effect matches the operator's expectation. High compatibility means faster, more
accurate action and — crucially — **fewer errors under stress**, because the operator falls
back on expectation exactly when deliberation fails.

```
KINDS OF COMPATIBILITY
--------------------------------------------------------------------------------
   STIMULUS-RESPONSE (S-R):  the control that acts on a display is CO-LOCATED / mapped
      to it. (The burner knob nearest the back-left burner controls the back-left burner.)
   MOVEMENT:  moving a control in a direction moves the display / process the EXPECTED way.
      WARRICK'S PRINCIPLE (Warrick, 1947): a pointer should move the SAME direction as
      the nearest point of its control -> the mapping people expect.
   CONCEPTUAL:  the interface's structure matches the operator's mental model of the work.
   MODALITY:  the response modality suits the signal (auditory alert -> vocal ack, etc.).

   WHY IT MATTERS UNDER STRESS: when workload spikes, operators revert to POPULATION
   STEREOTYPES (Sec.2). A control that violates the stereotype is usable when calm and
   DANGEROUS when loaded -- the operator does the "expected" thing, which is now wrong.
```

Compatibility is the cheapest safety intervention available, because it costs design
attention, not operator training — and training does not survive panic the way expectation
does.

---

## 2. Population Stereotypes & Their Cultural Limits

A **population stereotype** is a direction-of-effect expectation held by most of a
population: which way is "on," "more," "open." Alignment with the local stereotype may
reduce wrong-direction error risk; conflict may increase it. The critical human-factors
caveat is that **many stereotypes are cultural, not universal**, so evidence from one
population does not establish acceptability for another.

```
COMMON STEREOTYPES -- and where they REVERSE  (attributed; culture-bound)
--------------------------------------------------------------------------------
   ROTARY: clockwise -> increase / on / right   (strong in many populations)
   LIGHT SWITCH:  UP = on (US/Canada)   vs   DOWN = on (UK, Ireland, much of Europe/AU)
   FAUCET:  hot on the LEFT (widespread Western plumbing convention, not universal)
   COLOR:   red has danger/stop conventions in many industrial systems and festive/
            prosperity symbolism in Chinese culture; symbolism alone does NOT establish
            a reversed safety-control convention
   VERTICAL scale: up = more (widespread); but reading direction (L-to-R vs R-to-L)
            changes horizontal "increase" expectations
   STEREOTYPE STRENGTH VARIES: cross-cultural studies (e.g., Courtney on Hong Kong
      operators; Loveless 1962 review) show both DIFFERENT stereotypes and WEAKER ones
      in some populations -> a weak stereotype gives less error protection.

   DESIGN RULE: identify the ACTUAL population's stereotypes; where a product crosses
      cultures or a stereotype is weak/absent, do NOT rely on it -- add explicit coding,
      labeling, and constraints (Sec.3), and test with the real population (guide 10).
```

This is precisely where human factors is deeper than "follow the convention": the discipline
is knowing that the convention is **local and dated**, verifying it for the population that
will actually operate the system, and hardening the design where the stereotype is weak,
mixed, or reversing across the user base.

---

## 3. Coding & Redundancy — Never One Channel Alone

Information can be carried on several **coding dimensions** at once. Safety-critical design
**codes redundantly**, so that no single failed channel (a color-blind operator, a
monochrome night-vision display, a noisy cockpit) loses the message.

```
CODING DIMENSIONS  (carry the SAME distinction on MORE THAN ONE)
--------------------------------------------------------------------------------
   COLOR     fast, salient   -- red-green deficiency is ~8% among men of Northern-European
                                ancestry and lower in many other populations; meaning is
                                culture-bound; unusable in monochrome/low-light -> NEVER alone
   SHAPE     symbol/geometry -- learnable, language-free, works in monochrome
   POSITION  location/layout -- strong, learned (the alarm is where you expect it)
   SIZE      magnitude cue   -- coarse; limited discriminable steps
   ORIENTATION / MOTION / BLINK -- salient but attention-grabbing (use sparingly, Sec.5)
   TEXT / LABEL   precise    -- but language-bound and slow to read under load
   AUDITORY  tone/speech     -- omnidirectional; good for alerts; collides in noise

   REDUNDANCY PRINCIPLE: a critical distinction (safe vs unsafe, on vs off, this vs that
   tank) rides on >=2 dimensions -> color + shape + position + label. Then a single failed
   channel degrades gracefully instead of losing the message.
   (This is the operator-safety twin of accessibility's "don't rely on color alone" --
    HCI/accessibility owns the digital-a11y version; here it is a SAFETY requirement.)
```

The number of **discriminable steps** per dimension is small (a handful of reliably
distinguishable colors or sizes), so overloading one dimension with many meanings fails;
redundant, few-step coding beats dense single-channel coding.

---

## 4. Alarm Philosophy — The Alarm System Is Its Own Hazard

An alarm system is meant to direct attention to what needs action. Done badly, it becomes
**the** hazard: in real incidents, operators have been buried under an **alarm flood** at
the worst moment, unable to find the alarm that mattered. Human factors treats the alarm
system as a designed object with its own failure modes.

```
ALARM PATHOLOGIES  (why "add an alarm" is often the wrong reflex)
--------------------------------------------------------------------------------
   ALARM FLOOD     a plant upset triggers a cascade -> dozens/hundreds of alarms in
                   minutes, exactly when the operator can least process them.
   MISCLASSIFIED   informational notifications incorrectly carried in the alarm channel.
   CHATTERING      an alarm repeatedly toggling around a threshold (a candidate for a
                   deadband, subject to review).
   STANDING/STALE  alarms left active for hours -> ignored; hide new ones.
   CRY-WOLF        frequent false/low-value alarms erode TRUST -> real alarms ignored or
                   silenced (the trust seam to automation, guide 07).

   ALARM MANAGEMENT (analysis discipline, NOT operating instruction) -- every
     candidate change is a HYPOTHESIS subject to HAZARD REVIEW, management of
     change (MoC), qualified domain validation, and local procedures:
     RATIONALIZE   ask whether each alarm justifies its existence, setpoint, and
                   a required operator ACTION -- an alarm with no action is a
                   CANDIDATE for change, not an instruction to delete.
     PRIORITIZE    propose a few priority levels tied to urgency x consequence.
     SHAPE         deadbands, shelving, state-based suppression are CANDIDATE
                   techniques to EVALUATE, each reviewed under MoC and validated
                   by qualified domain staff before any live change.
     MEASURE       characterize alarm RATE per operator, flood frequency, and
                   standing-alarm count (descriptive analysis of logged data).

   DATED, BOUNDED STANDARDS (primary sources; context, NOT certification):
     EEMUA 191 (4th ed. 2024; 1st ed. 1999) -- alarm design/management guide;
       widely-cited BENCHMARK rates (steady-state ~a few alarms/hr per operator;
       "flood" as >10 alarms per 10 min) -- guideline figures for the PROCESS
       INDUSTRIES, not universal limits.
     ANSI/ISA-18.2-2016 and IEC 62682:2022 -- alarm-mgmt lifecycle standards
       (ISA / IEC), harmonized with EEMUA 191.
   Attributed, dated, INDUSTRY-SPECIFIC process-industry guidance; other sectors
   (aviation, healthcare, rail) have their OWN alarm/alert guidance. The guide
   gives the REASONING only; it certifies nothing and prescribes no change.
```

The counter-intuitive lesson every engineer needs: **more alarms usually means less
safety.** The design goal is *fewer, rationalized, prioritized* alarms — because the
operator's ability to act is the scarce resource, not the number of detectable conditions.

---

## 5. Salience vs Nuisance — The Attention Budget

Salience (blink, motion, loud tones, red) **captures** attention. Attention is finite, so
salience is a **budget**: spend it on the few things that must be seen, and every extra
salient element **devalues the rest**. Over-alerting is not just annoying; it is a safety
regression via two paths.

```
THE SALIENCE BUDGET
--------------------------------------------------------------------------------
   spend salience on ---> the FEW must-see, must-act signals
      too little: a critical change is missed (change blindness, guide 03)
      too much:   (1) DILUTION -- everything is red, so nothing is;
                  (2) CRY-WOLF -- false salience erodes trust -> operators tune it out
   TUNING: reserve the strongest codes (motion/blink/loud) for the highest priority;
      graded, not binary; let low-priority info be AVAILABLE (perceptible on look) but not
      INTRUSIVE (grabbing attention). Attention-DIRECTION must not itself tunnel (guide 03).
```

The design discipline is to rank signals by *urgency x consequence* and grant salience in
that order, keeping most information in the "available but quiet" tier — the opposite of the
instinct to make every important thing loud.

---

## 6. Mode & State Visibility — Designing Out the Mode Error

A **mode** is a state in which the same control or indication *means something different*.
Modes are powerful and dangerous: a **mode error** happens when the operator acts correctly
for the mode they *think* they are in, but the system is in another. When the system is
partly automated, this becomes an **automation surprise** (Sarter & Woods, 1995): "why is it
doing that? what is it doing now? what will it do next?"

```
MODE ERROR AND ITS DESIGN ANTIDOTE
--------------------------------------------------------------------------------
   THE TRAP:  same input, different effect depending on an INVISIBLE mode.
      classic illustration: a vertical-speed vs flight-path-angle mode confusion, where
      the same knob/number means different things by mode (Air Inter, 1992 -- the AVIONICS
      SYSTEM belongs to aeronautics/04; here it is the canonical MODE-VISIBILITY lesson).
   THE ANTIDOTE (design principles, not a procedure):
      - make the ACTIVE mode/state continuously, saliently VISIBLE (not buried).
      - make MODE TRANSITIONS salient (defeat change blindness, guide 03) -- especially
        AUTONOMOUS transitions the operator did not command.
      - minimize the NUMBER of modes and the overlap of controls across modes.
      - show what the automation is doing and WILL do (feed SA levels 1-3, guide 03).
   This is the interface half of the automation problem; the trust/authority/level-of-
   automation trade-offs are guide 07's.
```

Mode visibility is where displays (guide 03's SA), controls (compatibility, §1), and
automation (guide 07) intersect: the interface must answer, always and without being asked,
*what mode am I in and what is the machine about to do?*

---

## 7. Ecological Interface Design — Show the Work's Deep Structure

Most displays show **data** (values, states). **Ecological Interface Design (EID)** —
Vicente & Rasmussen (1992), built on Rasmussen's work — argues that safety-critical
displays should also externalize the **constraints and relationships of the work domain**
itself, so the operator can reason through **unanticipated** situations that no procedure
foresaw.

```
RASMUSSEN'S SRK + THE ABSTRACTION HIERARCHY  (the basis of EID)
--------------------------------------------------------------------------------
   SKILL-RULE-KNOWLEDGE (SRK) -- three levels of operator behavior:
      SKILL      smooth, automatic (reading a familiar gauge)         -> support with
                                                                          direct perception
      RULE       "if this state, do that" (known procedures)          -> support with
                                                                          clear signs/cues
      KNOWLEDGE  reasoning from first principles when nothing fits    -> support by making
                 (the novel fault, the un-proceduralized upset)          the DOMAIN visible

   ABSTRACTION HIERARCHY (what to make visible):
      functional purpose  (why the system exists: keep the core cool)
        v
      abstract function   (mass/energy balances, flows, conservation)
        v
      generalized function(processes: this pump feeds that tank)
        v
      physical function   (equipment: pump P-2, valve V-7 states)
        v
      physical form       (layout, location)
   EID makes the UPPER (functional) layers visible, not just the bottom (equipment), so a
   KNOWLEDGE-level operator can see WHY the numbers matter and reason about a novel fault.
```

EID's payoff is exactly the case procedures cannot cover: when the situation is off-script,
a display that shows the mass/energy structure of the plant lets the operator reason from
constraints, instead of hunting through equipment readouts for a pattern. It is the interface
expression of "support knowledge-based behavior, not just skill and rule."

---

## 8. Control-Room / Workspace Layout

When many displays and controls share a workspace, **where** each goes is a human-factors
decision governed by four classic, sometimes-competing principles.

```
FOUR LAYOUT PRINCIPLES  (arrange displays/controls by...)
--------------------------------------------------------------------------------
   IMPORTANCE       the most safety-critical items get the best (central, reachable,
                    visible) positions -- even if used rarely.
   FREQUENCY-OF-USE the most-used items go in the best remaining positions (reach zone,
                    guide 02; central vision).
   SEQUENCE-OF-USE  items used in a fixed order are arranged in that order (left-to-right
                    or top-to-bottom along the task flow).
   FUNCTION         items serving the same function are grouped and bordered together
                    (all cooling controls together, all electrical together).

   THEY CONFLICT: an IMPORTANT item may be INFREQUENT (emergency stop) -> importance wins
      for placement, and coding (Sec.3) plus guarding resolves the rest. Resolve conflicts
      EXPLICITLY, ranking importance and safety first.
   PLUS: reach/clearance/vision geometry from guide 02; SA-supporting grouping from guide 03.
```

Layout is where guide 02 (the physical reach/vision envelope) and guide 03 (grouping to
support SA and manage scan load) meet this guide's coding and alarm logic: the panel is a
single designed field, not a collection of independently-placed instruments.

---

## 9. The Safety-Critical UI ↔ HCI Usability Seam

The sharpest boundary this guide must hold is with `human-computer-interaction/`. Both
design interfaces; they own different halves, and modern touchscreen consoles put them on
the same glass.

```
WHO OWNS WHAT AT A SHARED SAFETY-CRITICAL INTERFACE
--------------------------------------------------------------------------------
   human-computer-interaction/  the INTERACTION, visualization, accessibility
      METHODS: interaction models, design process, usability EVALUATION, info
      architecture/visualization, interactive ACCESSIBILITY, research methods --
      they apply to EVERY interactive system: a safety-critical console is STILL
      an HCI system, not a lesser or "non-user" one.

   human-factors/06 (this guide)  supplies the SAFETY REQUIREMENTS on that same
      interface: compatibility & stereotypes for error-under-stress, redundant
      coding as a SAFETY need, ALARM philosophy, salience, MODE visibility, EID,
      control-room layout, plus workload/error CONSTRAINTS and the
      performance-UNDER-STRESS VALIDATION.

   MAXIM modules supply METHODS + EVIDENCE; ACCEPTANCE + IMPLEMENTATION belong to
      the ACCOUNTABLE DOMAIN ORGANIZATION and its REGULATOR (the systems defer to
      nuclear/05, aeronautics/04, biomedical-engineering/07, transportation/07)
      -- legal obligation defers to law/.

   ONE system: HCI methods/evidence + HF safety/under-stress evidence feed the
   accountable domain organization's ACCEPTANCE -- NOT an HCI object OR an HF object,
   and no reference module signs off or vetoes a real deployment.
```

```
EVIDENCE + ACCEPTANCE  (one safety-critical interface, who owns what)
--------------------------------------------------------------------------------
   MODULES OWN METHODS + EVIDENCE  (they do NOT sign off a real system):
      HCI  interaction / visualization / accessibility METHODS + EVIDENCE
      HF   workload / error / performance-under-stress EVIDENCE
                         |  both evidence streams feed ->
                         v
   THE ACCOUNTABLE DOMAIN ORGANIZATION + ITS REGULATOR own ACCEPTANCE and
      IMPLEMENTATION: they weigh the evidence, accept or reject, and implement.
      Legal obligation -> law/.

   RULE: a reference module SUPPLIES EVIDENCE; it does not sign off or veto. Weak
      HF evidence may indicate elevated error risk under load; weak HCI evidence
      may indicate usability or accessibility shortfalls. Evidence can be
      insufficient for acceptance, but the decision belongs to the accountable
      organization and regulator, not HCI or HF.
```

The rule: *if the question is "which interaction/visualization/accessibility method fits?"*
it is HCI's; *if it is "does this interface prevent operator error and support safe action
under load, and is it validated under stress?"* it is this guide's; *if it is "how does this
reactor/aircraft/device actually work, who accepts it, and who regulates it?"* it belongs to
the domain module and, in the real world, to the accountable domain organization and its
regulator. The reference modules own **methods and evidence**; **acceptance and
implementation are the accountable organization's and the regulator's**, not any reference
module's — no module signs off or vetoes a real system.

---

## A Worked Quantitative Pass — Before/After Alarm Metrics (synthetic)

*Synthetic figures for a fictional process plant, computed on **logged and replayed** data
in a design-analysis — not a live plant, not a certification, and not an operating change.
The "after" column is a **modeled projection** from a rationalization analysis, not a
measured live result.*

A converging-upset scenario is characterized before, and modeled after, an alarm
**rationalization** analysis. **Every number below is derived** from a stated fictional
event inventory and explicit aggregation rules (so the metrics are traceable, not asserted);
EEMUA-191-style benchmarks (dated, process-industry GUIDELINES, never limits) appear only for
context:

```
EVENT INVENTORY + AGGREGATION RULES  (fictional; how each number is derived)
--------------------------------------------------------------------------------
   RULES (applied to a replayed event log):
     steady-state rate = annunciations in a representative QUIET hour / 1 h
     peak flood        = max annunciations in any rolling 10-min window (upset)
     standing          = alarms continuously active > 24 h (a stock, not a rate)
     % actionable      = share of annunciations with a DOCUMENTED action
     priority mix      = P1/P2/P3 split of the ACTIONABLE alarms only
                         (informational messages are NOT alarms -> no priority)

   BEFORE, one quiet hour = 62 annunciations, by class:
     chattering (3 tags toggling a setpoint) .... 21   no action
     standing/stale re-annunciations ............  8   no action
     informational status msgs (mis-set as alarm)  8   no action -> notify
     actionable process alarms (cascade dups) ... 25   action
     TOTAL 62  ->  25 / 62 = 40% actionable

   AFTER (modeled projection), same hour:
     chattering    -> deadband candidate .........  ~0
     standing      -> shelving / redesign ........  ~0
     informational -> MOVED to a notification channel (not deleted)
     actionable    -> cascade dups consolidated: 25 -> ~9 distinct
     TOTAL 9  ->  100% action-requiring in the modeled alarm channel

   PEAK 10-MIN UPSET WINDOW:
     BEFORE 220 annunciations =
       145 cascade duplicates + 45 chatter + 20 standing repeats + 10 distinct alarms
     AFTER 14 annunciations =
       10 distinct action-requiring alarms + 4 modeled repeats

   STANDING-ALARM STOCK:
     BEFORE 45 continuously active tags
     AFTER   6 retained as unresolved/valid standing conditions pending domain review

   ACTIONABLE PRIORITY COUNTS (quiet-hour alarm channel):
     BEFORE 25 = P1:8, P2:7, P3:10  -> 32% / 28% / 40%
     AFTER   9 = P1:1, P2:2, P3:6   -> 11% / 22% / 67%
```

| Metric (per operator) | Before | After (modeled) | Benchmark (guideline) |
|---|---|---|---|
| Steady-state alarm rate (alarms/hr) | 62 | 9 | order of a few / hr |
| Peak flood (alarms / 10 min) | 220 | 14 | "flood" > 10 / 10 min |
| Standing (stale) alarms (count) | 45 | 6 | as low as practicable |
| Alarms with a defined operator ACTION (%) | 40 | 100 | an alarm should require action |
| Informational msgs mis-carried as alarms (/hr) | 8 | 0 | belong in a notification channel |
| Priority mix of the ACTIONABLE alarms, P1/P2/P3 (%) | 32 / 28 / 40 | 11 / 22 / 67 | few high-priority |

**Alarms vs informational notifications.** Everything that survives in the **alarm** system
requires an operator response; priorities **P1/P2/P3 are three urgency bands of
action-requiring alarms**, not a slot for no-action messages. A signal that needs **no**
action is not a low-priority alarm — it is an **informational notification** and belongs in a
**separate channel**, which is where the rationalization *moves* the ~8/hr mis-carried
messages (it does not delete them). **Prioritization rationale.** Priority is assigned by
**urgency x consequence**, not by how alarming a value looks: of the modeled actionable
alarms, 11% are **P1** (rare, immediate, safety-relevant action), 22% **P2**, and 67% **P3**
(**lowest-urgency but still action-requiring**) — so that when a P1 fires it is rare,
meaningful, and actionable. The modeled flood drop (220 -> 14 per 10 min) comes from
**consolidating cascade duplicates** and **rationalizing** no-action items out of the alarm
stream, plus deadband/suppression *candidates* — not from hiding real conditions.

**Uncertainty / validation.** The "after" figures are a **modeled projection**: they assume
the rationalization holds under real upsets, which a replay cannot fully prove. The key
residual risk is that a suppression or deadband **candidate hides an alarm that turns out to
matter** — so each candidate is a **hypothesis** requiring hazard review, management of
change, and qualified domain validation *before* any live change, and re-measurement
*after*. The EEMUA/ISA/IEC benchmarks are dated, process-industry guidelines; meeting them
is **not** a safety certificate, and this pass sets **no** operating values.

---

## A Fully Worked Case — A Console Redesign (illustrative, fictional)

*Fictional throughout; a demonstration of design reasoning, not an operating procedure, not
a certification, and not a judgment about any real system.*

**Setting.** *Aster Water* (invented) is redesigning the **operator console** for a
treatment plant after operators reported "too many alarms" during upsets. The question to
human factors: *make the true state obvious and the right action natural, under load —
without touching how the plant itself works.*

1. **Fix compatibility and stereotypes first (§1–2).** Valve controls are laid out
   **S-R compatible** with the mimic (the control for tank 2 sits on tank 2's diagram), and
   pointer/valve movement follows **Warrick's principle**. Because operators span two
   regions with **different light-switch/rotary stereotypes**, the team verifies the actual
   population's expectations (guide 10) and, where mixed, does **not** rely on direction
   alone — adding explicit labels and state coding.
2. **Code redundantly (§3).** "Valve open/closed" and "within/over limit" each ride on
   **color + shape + position + label**, so a color-blind operator on a dimmed night panel
   still reads state. No safety distinction rides on color alone.
3. **Attack the alarm flood, don't add alarms (§4–5).** Rather than add a "master alarm,"
   the team runs a **rationalization analysis**: each alarm is examined for a required
   operator action, and no-action alarms become **candidates** for demotion to information;
   a few **priority** levels are proposed by urgency x consequence; deadbands and
   state-based suppression are proposed as **candidates** to evaluate. Crucially, every such
   change is a **hypothesis** — routed through hazard review, management of change, and
   qualified domain validation before any live change, never a direct edit to a running
   alarm system. They characterize alarm rate against the EEMUA-191-style benchmark as a
   *guideline* (dated, industry-specific context, not a pass/fail certificate; see the
   before/after pass above). Salience is **budgeted**: only top-priority alarms get
   motion/loud tones, defeating both dilution and cry-wolf.
4. **Make modes and the future visible (§6).** Any automatic control loop shows its
   **active mode** continuously and makes **autonomous transitions salient**, so an
   operator is never surprised about what the automation is doing or about to do — the
   trust/authority trade-offs themselves route to guide 07.
5. **Add an EID layer for the off-script case (§7).** Alongside equipment readouts, a
   display externalizes the **mass/flow balance** of the plant (abstract function), so a
   **knowledge-level** operator facing a novel fault can reason from constraints instead of
   scanning raw values.
6. **Lay it out by importance, then frequency/sequence/function (§8),** resolving the
   emergency-stop (important but rare) conflict in favor of importance plus guarding.

**Reading.** Compatibility and stereotypes checked against the *real* population, redundant
safety coding, an alarm system treated as a hazard to *reduce*, budgeted salience, visible
modes, an EID layer for the unanticipated — and not one operating instruction or
certification. The plant's own workings stay with the domain module.

---

## Reader Tasks (answerable from this guide)

1. **Diagnose an incompatible control.** Given "the pointer moves left when the knob turns
   right," name the movement-compatibility / Warrick violation, explain why it is *extra*
   dangerous under stress (revert-to-stereotype), and give the fix. (§1–2.)
2. **Catch a cultural-stereotype trap.** Given a design shipping to populations with
   opposite light-switch or color conventions, explain why relying on the stereotype plants
   a latent error and what redundant coding/labeling/testing you'd add. (§2–3.)
3. **Reduce an alarm flood — read the metrics, stay within the safety contract.** Using the
   before/after pass, compute the change in steady-state rate (62 -> 9 /hr) and peak flood
   (220 -> 14 /10 min), say whether each moves toward the EEMUA-style **guideline** (not a
   limit), and explain the priority-mix shift (32/28/40% -> 11/22/67%). Then state why deadbands,
   shelving, and state-based suppression are **candidate hypotheses** — each requiring hazard
   review, management of change, and qualified domain validation — **not** operating
   instructions, and cite ANSI/ISA-18.2-2016 / IEC 62682:2022 / EEMUA 191 (4th ed. 2024) as
   dated guidance, not certification. (§4–5, before/after pass.)
4. **Design out a mode error.** Given "the operator acted right for the wrong mode," specify
   continuous active-mode visibility, salient (especially autonomous) transitions, and fewer
   modes — and route the authority/trust trade-off to guide 07. (§6.)
5. **Place the seam and assign evidence vs acceptance.** Given a clinical-device touchscreen,
   assign the interaction/visualization/accessibility *methods/evidence* to
   `human-computer-interaction/` (it is still an HCI system) and the alarm/salience/mode and
   workload-SA **safety + under-stress evidence** to this guide; then assign **acceptance and
   implementation to the accountable domain organization and its regulator** (with the device
   engineering deferred to `biomedical-engineering/07`) — and state why a reference module
   supplies evidence but does **not** sign off or veto a real system. (§9.)

---

## Decision Cheat Sheet

| Situation | Move | Why (this guide) |
|---|---|---|
| Placing a control that acts on a display | make it **S-R compatible**; Warrick movement | expectation-matching cuts error under stress (§1) |
| Choosing a direction-of-effect | use the **real population's** stereotype; verify it | stereotypes are cultural, dated, variable (§2) |
| Encoding a safety distinction | **redundant** color + shape + position + label | any single channel can fail (color-blind, mono) (§3) |
| Tempted to "add an alarm" | **rationalize** first: no action -> not an alarm | more alarms usually means less safety (§4) |
| Alarms chatter / stand / flood | propose deadbands/shelving/state-suppression as **candidates** (hazard review, MoC, validation); measure | alarm system is its own hazard (§4) |
| Everything is red/loud | **budget salience** by urgency x consequence | dilution + cry-wolf erode response (§5) |
| Same control means different things | make the **active mode** + transitions visible; fewer modes | mode error / automation surprise (§6) |
| Operator faces a novel, off-script fault | add an **EID** layer (abstraction hierarchy) | support knowledge-based reasoning (§7) |
| Arranging a crowded panel | **importance** first, then frequency/sequence/function | resolve placement conflicts safety-first (§8) |
| "Is this interactive system usable?" | route to **`human-computer-interaction/`** | general digital usability is HCI's (§9) |
| "How does the reactor/aircraft/device work?" | route to **nuclear/05, aero/04, bme/07** | domain systems belong to their owners (§9) |
| Certify the console / write the procedure | **out of scope** — principles only | safety contract, banner |

---

## Common Confusion Points

**"Follow the convention and you're safe."** Only if it is *this population's* convention.
Light-switch direction, faucet sides, and color meanings **reverse** across cultures, and
some stereotypes are weak. Human factors verifies the stereotype for the real operators and
hardens the design where it is mixed or absent (§2).

**"Color-code it."** Color is fast but red-green deficiency prevalence varies by
population (~8% among men of Northern-European ancestry), and color also fails in
monochrome/low light and can shift in meaning across cultures. A safety distinction must ride on **at least two** dimensions —
color *and* shape *and* position *and* label (§3).

**"If in doubt, add an alarm."** Usually wrong. Unrationalized alarms cause floods,
nuisance, and cry-wolf, burying the alarm that matters. Fewer, rationalized, prioritized
alarms make the operator *more* able to act (§4). EEMUA 191 (4th ed. 2024),
ANSI/ISA-18.2-2016, and IEC 62682:2022 are dated, process-industry **guidance**, not
certifications.

**"Make everything important stand out."** Salience is a budget; if everything is salient,
nothing is, and false salience trains operators to ignore alerts. Grant salience by urgency
x consequence and keep most info available-but-quiet (§5).

**"The operator should have known which mode it was in."** That is a design failure, not an
operator failure: an invisible mode plus a shared control *causes* mode error. Make the mode
and its (especially autonomous) transitions visible (§6). Naming the *cause* of any real
event is `04`/`08`'s method, not "the operator lost track."

**"This is just UI/UX."** General digital usability and accessibility are
`human-computer-interaction/`'s. This guide owns the **safety-consequence** layer — alarms,
salience, modes, compatibility-under-stress, control-room layout — and defers the domain
systems to their modules (§9).

---

## Global, WEIRD & Resource Caveats

- **Stereotypes and standards are Western-industrial by default.** Warrick's principle, the
  common rotary/switch stereotypes, and EEMUA/ISA alarm guidance were established largely in
  Western industrial settings; strength and even direction differ across populations, and
  the alarm benchmarks are process-industry figures, not universal limits. Verify against the
  actual operator population (guide 10).
- **Color and symbol meaning are cultural.** Red/green semantics, iconography, and
  reading-direction expectations vary; a coding scheme validated in one region can mislead in
  another. Redundant, tested coding is the safeguard.
- **Localization is a safety issue, not a translation task.** Labels, alarm text, and
  procedures render into other languages and literacy levels; text-heavy coding degrades for
  operators reading a second language under load — another argument for shape/position
  redundancy.
- **Resource asymmetry shapes what's buildable.** Alarm-management platforms, EID displays,
  and eye-tracking-backed layout studies are resource-rich-organization tools; low-resource
  control rooms may inherit legacy panels and foreign stereotypes, magnifying the caveats
  above. The correction is explicit verification and redundant coding, not a borrowed
  convention assumed universal.

---

## A Contrasting Example (non-WEIRD, low-resource)

*Fictional, to show how the principles hold while the specifics must be re-verified.*

**Setting.** A *fictional* small hydro control room is staffed by operators from several
regions with **mixed switch/rotary stereotypes** and **multiple first languages**, running a
**legacy panel** with no budget for a new alarm platform.

**What breaks if you copy a Western design wholesale.**
- **Imported stereotypes mislead.** Assuming "up = on" or a single rotary convention plants
  latent errors for the operators who hold the opposite expectation; the fix is to verify the
  actual population and **not rely on direction alone** — add shape/position/label coding.
- **Color/label coding degrades.** A color-plus-English-label scheme fails color-blind and
  second-language operators under load; **shape + position** redundancy carries the safety
  distinction when color and text do not.
- **Alarm discipline beats alarm technology.** Without a management platform, the highest-
  value analysis is still **rationalization** — identifying no-action alarms as candidates
  for demotion, proposing deadbands, and ranking a few priorities by hand — which needs
  judgment, not budget. These are **candidate changes** for hazard review, management of
  change, and qualified validation, not hand edits to a live system; done that way they
  target flood and cry-wolf.

**Reading.** Compatibility, redundant coding, alarm rationalization, salience budgeting, and
mode visibility **transfer as principles**; the stereotypes, colors, labels, and benchmark
numbers must be **re-verified** for the real population and setting, and stated as such.

---

## Prototype Seam Contract (review gate for this guide)

This guide is a **review-gated prototype**, authored before the rest of the module to prove
the module's other hard boundary: the **safety-critical interface ↔ HCI usability** seam,
plus the deferral of **domain systems** to their owners. The gate this guide must pass:

- **The HCI seam holds.** Interaction design, IA/visualization, and accessibility
  *methods/evaluation* are owned by `human-computer-interaction/` (a safety-critical console
  is still an HCI system); this guide owns only the **safety-evidence** layer on that same
  interface and records the **evidence-vs-acceptance** split (HCI methods/evidence + HF
  safety/under-stress evidence; **acceptance and implementation owned by the accountable
  domain organization and its regulator**). *Fails if* it re-teaches usability method,
  caricatures HCI's users as discretionary/casual, claims HCI's method space, or lets a
  reference module sign off/veto a real system.
- **Domain systems stay deferred.** Reactor, avionics, medical-device, and vehicle-autonomy
  systems are cited to `nuclear/05`, `aeronautics/04`, `biomedical-engineering/07`,
  `transportation/07`; this guide gives **HF principles only**. *Fails if* it explains or
  operates a domain system.
- **No procedures, no certification.** Everything is design principle; there is **no runnable
  operating procedure** and **no** declaration that a design is safe/compliant. Standards
  (EEMUA 191, ISA-18.2) and stereotypes are dated, bounded context. *Fails if* a procedure or
  a certification appears.
- **The module-wide pattern is inherited, not restated.** The full guide-family scaling
  contract lives in the scaling-gate prototype `02`; this guide conforms to it.

Passing this gate ratifies that the module can carry the HCI seam and the domain-deferral
boundary on real content before the remaining guides are authored.
