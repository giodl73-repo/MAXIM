---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "11-ORGANIZATIONAL-SAFETY-CULTURE.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-factors:organizational-safety-culture
kind: guide
module: human-factors
section: human-factors
title: Organizational & Safety Culture - HRO, Just Culture, and Safety-II
status: source-custody
source_custody: partial
current_path: human-factors/11-ORGANIZATIONAL-SAFETY-CULTURE.md
canonical_path: human-factors/11-ORGANIZATIONAL-SAFETY-CULTURE.md
backsource_ids: [mdloom-backfill:human-factors:11-organizational-safety-culture]
concepts: [safety-culture, high-reliability-organizations, just-culture, safety-i-safety-ii, resilience-engineering, reporting-systems, normalization-of-deviance]
root_concepts: [organizational-safety-culture]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Organizational & Safety Culture — HRO, Just Culture, and Safety-II

**This guide owns** the *organizational layer of safety*: **safety culture and climate** (and why
it is not a number to maximize), **High-Reliability Organizations (HRO)**, **just culture** (the
balance of blameless learning and accountability), **Safety-I vs Safety-II / resilience
engineering** (safety as the presence of success, not only the absence of failure), **reporting
systems** and the reporting paradox, and **normalization of deviance**. It is the guide that keeps
the module's barriers (`08`) and error-handling (`04`) *alive over time* — a design or a HEP
decays if the organization does not sustain it. **It builds on** `04` (just culture is how error
is handled without blame), `08` (culture sustains barriers), and `07`/`06` (the conditions culture
shapes). **It explicitly defers**: **clinical patient-safety culture and practice** to
[`clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW`](../clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW.md)
(this guide owns the *generic* science; the clinical application is theirs); **general
organizational theory** — motivation, leadership, structure beyond safety — to
`organizational-behavior/`; **legal/regulatory duty** to `law/`; and **survey statistics** to
[`statistics-applied/`](../statistics-applied/00-OVERVIEW.md).

> **Safety & ethics contract (binds every human-factors guide).** This is an **educational
> systems reference**. Nothing here rates an organization "safe" or "compliant," ranks a unit,
> settles culpability in a specific case, or serves as an audit checklist. Safety-culture models
> are **lenses and evidence**, not scores or verdicts; **acceptance and accountability belong to
> the accountable organization and its regulator**, never to this module. A just-culture *concept*
> here is not a disciplinary or legal ruling about any person.

*Per-guide banner: **safety culture is not a single number.** Every metric below (a reporting
rate, an injury rate, a survey score) is a **confounded proxy** that becomes a distortion the
moment it is treated as a target. The value is in what the evidence *reveals*, not in a league
table.*

---

## The Big Picture: Culture Is Where Safety Is Sustained or Eroded

A safe design, a low HEP, and a clean bow-tie all **decay** if the organization does not keep them
alive — through reporting, learning, and resisting the slow drift toward "it's fine." Safety
culture is that sustaining layer, and it is studied through four connected ideas.

```
THE ORGANIZATIONAL SAFETY LAYER  (four ideas that sustain -- or erode -- safety)
================================================================================
   HRO -- how some organizations stay safe        JUST CULTURE -- how error is handled
   with hazardous tech (Weick & Sutcliffe):        so people REPORT (Reason; Dekker):
     preoccupation with failure                     blameless LEARNING balanced with
     reluctance to simplify                         genuine ACCOUNTABILITY -- not
     sensitivity to operations                      blame-free, not blame-all
     commitment to resilience                       => the precondition for REPORTING
     deference to expertise
                    \                              /
                     \___ both feed REPORTING & LEARNING ___/
                    /                                        \
   SAFETY-II / RESILIENCE -- study what goes RIGHT   NORMALIZATION OF DEVIANCE -- how
   (Hollnagel): everyday work varies to SUCCEED;      "we got away with it" slowly
   understand normal work, not only failures          becomes the new normal (Vaughan)
================================================================================
   Read it as: HRO + just culture BUILD reporting and learning; Safety-II widens what you
   learn from (successes too); normalization of deviance is the EROSION they must resist.
   None of these is a score -- they are lenses on how an organization stays safe.
```

The single most important claim: **you cannot buy safety culture with a metric.** The moment a
reporting rate or an injury rate becomes a target, it is gamed (Goodhart), and the *distortion*
usually makes the organization *less* safe while the number improves.

---

## 1. High-Reliability Organizations (HRO)

Some organizations — aircraft carriers, air-traffic control, some power grids — run hazardous
technology with **far fewer accidents than expected**. The Berkeley HRO researchers (La Porte,
Roberts, Rochlin, **1980s–90s**) and **Weick & Sutcliffe** (*Managing the Unexpected*, **2001**;
later editions) distilled five principles of **collective mindfulness**:

```
THE FIVE HRO PRINCIPLES  (Weick & Sutcliffe -- anticipation + containment)
--------------------------------------------------------------------------------
   ANTICIPATION (see problems coming):
     1 PREOCCUPATION WITH FAILURE   treat small signals/near-misses as information,
                                    not noise; worry when things are quiet
     2 RELUCTANCE TO SIMPLIFY       resist easy explanations; keep the messy detail
     3 SENSITIVITY TO OPERATIONS    keep a live picture of the front line (SA at scale, 03)
   CONTAINMENT (cope when they arrive):
     4 COMMITMENT TO RESILIENCE     build the capacity to absorb and recover, not just prevent
     5 DEFERENCE TO EXPERTISE       in a crisis, authority migrates to the person who KNOWS,
                                    not the person who RANKS
   -----------------------------------------------------------------------------
   HRO is a set of PRACTICES and a mindset, not a certificate. An organization is not
   "an HRO" because it says so; the principles are observable behaviors to cultivate.
```

---

## 2. Just Culture — The Precondition for Reporting

Reason's insight (`04`): an organization learns only from what people **report**, and people
report only if reporting is **safe**. But a *blame-free* culture that excuses recklessness loses
the workforce's trust as much as a blaming one. **Just culture** (Reason, **1997**; Dekker, *Just
Culture*, **2007**; Marx, **2001**) is the *balance*.

```
JUST CULTURE  (the line is BEHAVIOR, not OUTCOME)
--------------------------------------------------------------------------------
   HUMAN ERROR (slip/lapse/mistake, 04)  -> CONSOLE & support; fix the system
   AT-RISK BEHAVIOR (drift, unaware risk) -> COACH; remove the incentive to drift
   RECKLESS BEHAVIOR (conscious disregard  -> ACCOUNTABILITY (a genuinely different case)
     of a substantial, unjustified risk)
   -----------------------------------------------------------------------------
   THE SUBSTITUTION TEST (Reason): would a DIFFERENT competent person, in the same
   situation with the same information, plausibly have done the same? If yes, the design
   /system is on trial, not the individual.
   OUTCOME BIAS TRAP: judge the BEHAVIOR and the situation, not the OUTCOME. The same act
   is called "error" if it ends well and "negligence" if it ends badly -- just culture
   refuses that severity-driven relabeling.
```

Crucially, this guide teaches just culture as a **concept for organizational learning** — it draws
**no** disciplinary or legal conclusion about any real person (that is the organization's, and at
the legal end `law/`'s).

---

## 3. Safety-I vs Safety-II and Resilience

- **Safety-I** (the traditional view): safety is the **absence of failures**; you improve by
  *counting and removing* what goes wrong. Necessary, but it studies only the rare bad cases and
  treats the human mainly as a hazard.
- **Safety-II** (Hollnagel, *Safety-I and Safety-II*, **2014**): safety is the **presence of
  success** — the everyday **variability** by which operators adapt to keep an under-specified,
  resource-constrained system working. You improve by understanding **normal work** (work-as-done),
  not just failures, and by treating the human mainly as a **resource** for flexibility.

```
SAFETY-I vs SAFETY-II  (two lenses; use BOTH)
--------------------------------------------------------------------------------
   SAFETY-I   learn from the FEW that go wrong     human = hazard to constrain
              reactive; count accidents/incidents  work-as-imagined is the reference
   SAFETY-II  learn from the MANY that go right     human = resource for adaptation
              proactive; study everyday variability work-as-DONE is the reference
   -----------------------------------------------------------------------------
   RESILIENCE (Hollnagel's four cornerstones): RESPOND (to disruptions), MONITOR (the
   near term), ANTICIPATE (the longer term), LEARN (from experience). Safety-II is the
   lens; resilience is the capability it builds. Neither replaces Safety-I -- they add to it.
```

The **work-as-imagined vs work-as-done** gap (also `04`, `10`) is the heart of it: procedures
(imagined) never fully match reality (done); the adaptations that close the gap are usually *why
things go right* and occasionally *why they go wrong* — so punishing all deviation destroys the
adaptations safety depends on.

---

## 4. Reporting Systems and the Reporting Paradox

Learning organizations run **voluntary, confidential, non-punitive** reporting — the archetype is
aviation's **ASRS** (NASA, **1976**), which protects reporters to surface near-misses.

```
THE REPORTING PARADOX  (why report counts are not a safety league table)
--------------------------------------------------------------------------------
   HIGH reporting rate  -> HYPOTHESES: accessible reporting, higher exposure,
                           broader definitions, or more events
   LOW  reporting rate  -> HYPOTHESES: low exposure, narrow definitions,
                           fear/underreporting, or fewer events
   -> the rate ALONE is INDETERMINATE -- exposure, opportunity, definitions,
      severity, reporting climate, and audit evidence must be triangulated.
   ACCESSIBILITY of reporting is a safety requirement: the channel must reach ALL workers
   (language, literacy, anonymity, >=2 channels) or you systematically miss the reports of
   the least-empowered -- the operator-safety twin of "never one channel" (06, 04).
```

**Normalization of deviance** (Diane Vaughan, *The Challenger Launch Decision*, **1996**) is the
erosion these systems resist: a deviation that "gets away with it" is quietly re-classified as
acceptable, the boundary moves, and the next deviation starts from there — until the margin is
gone. It is a *cultural* failure mode, invisible to a snapshot audit.

---

## The Boundaries (ownership in one place)

```
WHO OWNS WHAT AROUND SAFETY CULTURE
--------------------------------------------------------------------------------
   this guide (11)      the GENERIC science: HRO, just culture, Safety-I/II, resilience,
                        reporting systems, normalization of deviance -- and the "not one score" rule
   clinical-medicine/11 the CLINICAL application: patient-safety culture & practice in care
   organizational-behavior/  general org theory (motivation, leadership, structure)
   04 (error)           the error handling just culture governs
   08 (hazard)          the barriers culture sustains
   statistics-applied/  survey design, reliability, and inference on culture metrics
   law/                 legal culpability and regulatory duty
   -----------------------------------------------------------------------------
   Rule: this guide supplies culture LENSES and EVIDENCE; it does not score, rank, audit,
   certify, or rule culpability on any real organization or person.
```

---

## A Worked Metric Pass — Reading Reporting & Injury Data Without a League Table (reproducible)

*All numbers are **synthetic**. It demonstrates why safety culture **cannot** be reduced to one
score — the guide's signature discipline — and hands survey inference to `statistics-applied/`. It
ranks nothing and certifies nothing.*

**The data (synthetic).** Two units, one year:

```
TWO UNITS, NAIVE vs CORRECT READING  (synthetic)
--------------------------------------------------------------------------------
   metric                          Unit A        Unit B
   near-miss reports / 100 staff      120            18
   lost-time injuries / 100 staff     1.1            1.0
   process-safety near-misses         rising          "none reported"
   -----------------------------------------------------------------------------
   NAIVE (single-score) READING: "Unit B is safer -- far fewer reports, similar injuries."
   HONEST READING: the report-count gap is INDETERMINATE without triangulation. A=120 vs
   B=18 is CONSISTENT WITH SEVERAL rival stories, and the raw counts cannot separate them:
     - REPORTING CULTURE (the paradox, §4): A's people may feel safer to report -> more
       VISIBILITY, not more danger.                          [a hypothesis, not a verdict]
     - EXPOSURE / OPPORTUNITY: A may simply DO more of the hazardous task (more staff-hours
       at risk); "/100 staff" is a headcount denominator, not an exposure one.
     - DEFINITIONS: A and B may count "reportable near-miss" differently -- a looser
       threshold inflates A's number with no change in real risk.
     - SEVERITY MIX: the counts blend trivial and serious; A's 120 could be mostly minor.
   TRIANGULATE before concluding -- gather: exposure/opportunity denominators; a
   reporting-CLIMATE survey/interviews (do people feel safe to report?); consistent near-miss
   DEFINITIONS; SEVERITY stratification; the NEAR-MISS-to-incident ratio; and independent
   AUDIT/observation of actual conditions. Only THEN can a reading be defended.
   WHAT SURVIVES on these numbers alone: "none reported" is absence of REPORTS, not of
   EVENTS (a reporting-system GAP to probe); and the INJURY rate is a personal-safety
   (lagging) metric, a POOR proxy for MAJOR-ACCIDENT (process-safety) risk.
```

**The leading/lagging trap (the fatal metric error).**

```
PERSONAL SAFETY IS NOT PROCESS SAFETY  (why a low injury rate can hide catastrophe risk)
--------------------------------------------------------------------------------
   Unit B lost-time injury rate:    1.0  1.0  0.9  1.0   (flat, "good", LAGGING personal-safety)
   Unit B process-safety near-miss: rising but UN-reported ...................  (leading, hidden)
   -----------------------------------------------------------------------------
   Reading personal-injury rate as a proxy for major-accident risk is a documented, fatal
   error (a low slips-trips-and-falls rate has coexisted with high process-accident risk in
   real catastrophes). Personal-safety metrics (lagging) and process-safety leading indicators
   measure DIFFERENT hazards. A single "safety score" collapses them and misleads.
```

**Goodhart / "not one score."**

```
WHY A SINGLE SCORE BACKFIRES  (Goodhart's law on safety metrics)
--------------------------------------------------------------------------------
   TARGET "reduce reported incidents" -> people report LESS (fear) -> metric IMPROVES while
      safety WORSENS (learning dries up). The measure, once a target, stops measuring.
   TARGET "raise the culture survey score" -> survey coached/gamed -> score up, culture flat.
   -----------------------------------------------------------------------------
   HONEST PRACTICE: read a BASKET of indicators (reporting rate AS A CULTURE signal, leading
   process-safety indicators, learning cycle-time, survey WITH confounds), each with its
   limits -- and NEVER rank units on one number or use it as a compliance pass/fail.
```

**Uncertainty / validity / bias note.** (1) The numbers are **synthetic**; the *patterns* — the
reporting paradox, the personal-vs-process-safety divergence, and Goodhart gaming — are real,
repeatedly-observed effects. (2) **Reporting rate is a confounded proxy**: it depends on the
denominator, the reporting culture, severity mix, and definitions — it is a *culture signal*, not
an inverse safety measure. (3) **Culture surveys** have real reliability/validity limits and
social-desirability bias; their *inference* (is a difference real?) is `statistics-applied/`'s. (4)
This is a **metric-reading demonstration**, not a rating, ranking, audit, or certification of any
organization.

---

## A Fully Worked Case — Reading a Unit's Safety Signals (illustrative, fictional)

*Fictional. It demonstrates the culture lenses — not an assessment, rating, audit, or culpability
ruling for any real organization or person.*

**Setting.** *Fictional* **Northgate Logistics** wants to "score its depots on safety and reward
the safest." Human factors reframes the request:

1. **Refuse the single score (§Worked pass).** A league table on one number will be **gamed**
   (Goodhart): depots will suppress reports and chase the injury rate, eroding learning. Instead,
   read a **basket** of signals, each with limits.
2. **Treat reporting rate as *indeterminate* — triangulate before concluding (§4, Worked pass).**
   A high near-miss count is *consistent with* a healthy reporting culture (a candidate HRO
   behavior, preoccupation with failure), but *also* with higher exposure, looser definitions, or a
   milder severity mix — so before ranking anything, gather the **exposure denominator, a
   reporting-climate survey, consistent definitions, severity, the near-miss-to-incident ratio, and
   an audit**. What *is* firm: a **silent** depot's "none reported" flags a reporting-system gap to
   probe, not a proven-safe unit.
3. **Separate personal from process safety (§Worked pass).** A low slips-trips injury rate says
   little about the **major-accident** (e.g., loaded-vehicle) risk; track **leading** process-safety
   indicators separately, and never let a good personal-safety number reassure about catastrophe
   risk.
4. **Apply just culture to events (§2).** When an error surfaces, use the **substitution test** —
   would another competent person plausibly have done the same? — to keep the **system** on trial,
   distinguishing *at-risk* behavior (coach, remove the incentive to drift) from genuine
   *recklessness* (a different, accountable case), and drawing **no** legal conclusion (that is
   `law/`'s).
5. **Watch for drift and defer acceptance (§4, Boundaries).** Track **normalization of deviance**
   (are shortcuts becoming normal?); the **clinical-style** patient-safety framing, if any depot
   handles medical returns, defers to `clinical-medicine/11`; and whether the program is **adopted**
   is Northgate's decision — the module supplies lenses and evidence, not a score or a verdict.

**Reading.** "Rank the depots on one number" became "read a basket of signals with their confounds,
protect reporting, separate personal from process safety, apply just culture, and watch for drift"
— culture as evidence to act on, never a league table.

---

## Reader Tasks (answerable from this guide)

1. **Read the reporting rate as indeterminate.** Given Unit A (120 reports) and Unit B (18
   reports) with similar injury rates, explain why the comparison is **indeterminate without
   triangulation**, list the additional evidence you would gather (exposure/opportunity,
   definitions, severity, near-miss-to-incident ratio, reporting climate, audit findings), and
   state what "none reported" for process-safety near-misses *does* firmly signal (§4, Worked pass).
2. **Separate personal from process safety.** Explain why a flat, low lost-time-injury rate can
   coexist with rising major-accident risk, and why a single "safety score" that blends them
   misleads (§Worked pass).
3. **Apply just culture with the substitution test.** For a synthetic slip that ended badly,
   describe how to judge the *behavior and situation* rather than the *outcome*, and distinguish
   human error / at-risk / reckless — without drawing a legal conclusion (§2).
4. **Catch Goodhart.** Explain what happens to safety when "reduce reported incidents" becomes a
   target, and give a basket-of-indicators alternative that resists gaming (§Worked pass).
5. **Hold the boundary.** State what this guide owns (generic culture science) and what it defers
   (clinical patient-safety to `clinical-medicine/11`, general org theory to
   `organizational-behavior/`, culpability to `law/`), and why culture is "not one score"
   (Boundaries, banner).

---

## Decision Cheat Sheet

| Situation | Move | Why (this guide) |
|---|---|---|
| Tempted to score/rank units on safety | read a **basket** of indicators with limits | one score is gamed (Goodhart) (§Worked pass) |
| A unit reports many near-misses | **triangulate** (exposure, definitions, severity, climate, audit) before concluding | rate alone is indeterminate; the paradox is one hypothesis (§4) |
| A unit reports almost nothing | probe a **reporting-system gap**; don't read it as "safe" | absence of reports ≠ absence of events (§4) |
| Low injury rate cited as "safe" | separate **personal vs process** safety | lagging personal metric ≠ major-accident risk (§Worked pass) |
| Handling a specific error | apply **just culture** + substitution test | judge behavior/situation, not outcome (§2) |
| Running hazardous tech reliably | cultivate the **five HRO principles** | mindful anticipation + containment (§1) |
| Improving beyond counting failures | add **Safety-II** (study normal work) | learn from what goes right (§3) |
| Shortcuts becoming normal | watch **normalization of deviance** | the boundary drifts invisibly (§4) |
| Clinical patient-safety culture | route to **[`clinical-medicine/11`](../clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW.md)** | clinical application deferred (Boundaries) |
| "Rate/certify this org as safe" | **out of scope** — org + regulator | safety contract |

---

## Common Confusion Points

**"More incident reports means the unit is less safe."** The rate alone is
indeterminate. It may reflect reporting climate, exposure/opportunity, definitions,
severity mix, or actual event frequency. A quiet unit may have low exposure or suppressed
reporting; a high-rate unit may have healthy visibility or more hazards. Triangulation is
required (§4).

**"A low injury rate means low risk of a major accident."** No. **Personal-safety** (slips, trips)
metrics are a poor proxy for **process-safety / major-accident** risk; the two have diverged in real
catastrophes. Track leading process-safety indicators separately (§Worked pass).

**"Just culture means no-blame."** No — it is a **balance**. Human error and at-risk behavior are
consoled/coached and met with system fixes; genuine **recklessness** is a different, accountable
case. Blame-all and blame-free both destroy learning (§2).

**"Safety-II replaces Safety-I."** It **adds** to it. Keep counting and removing failures
(Safety-I) *and* study how everyday work succeeds (Safety-II); the human is both a hazard to
constrain and a resource for adaptation (§3).

**"Safety culture is a number you can maximize."** It is **not one score**. Every metric is a
confounded proxy that a target turns into a distortion (Goodhart); culture is read from a basket of
evidence with limits, and it is never a compliance checkbox (banner, §Worked pass).

---

## Global, WEIRD & Resource Caveats

- **The models are Western high-hazard-industry in origin.** HRO (US carriers/ATC), just culture
  (aviation/healthcare), and Safety-II (European) assume formal reporting systems, regulators, and
  resources; the *principles* transfer, but the *machinery* (confidential reporting bodies, survey
  programs) may not exist in every setting.
- **Reporting culture is power- and culture-shaped.** Willingness to report bad news up a hierarchy
  varies enormously with power distance, job security, and language; a reporting system validated in
  one culture can produce silence in another. Accessibility of the channel (language, literacy,
  anonymity, ≥2 channels) is a **safety requirement**, or the least-empowered workers' reports are
  systematically lost.
- **"Just culture" can be co-opted.** Where labor protections are weak, a "just culture" label can
  mask a blaming reality; the model's value depends on genuine, trusted protection for reporters —
  which is an organizational and, at the edge, a legal (`law/`) condition, not something the survey
  score guarantees.

---

## A Contrasting Example (non-WEIRD, low-resource)

*Fictional, to show the culture science where the formal machinery is absent.*

**Setting.** A *fictional* artisanal-mining cooperative in a low-income region has **no**
confidential reporting body, **no** culture-survey program, and a strongly hierarchical, oral work
culture.

**How the science adapts.**
- **The principles transfer; the machinery must be improvised.** HRO's *deference to expertise* and
  *preoccupation with failure* can live in **daily verbal safety huddles** and a **trusted elder** who
  collects near-miss stories — a reporting system without a database. The point is protected
  visibility of bad news, achieved with the tools available.
- **Reporting accessibility is the crux.** With mixed literacy and steep hierarchy, a written form
  would collect nothing; an **oral, anonymized** channel that reaches the least-empowered miners is
  the safety requirement — otherwise the reporting paradox bites hardest here.
- **No score, no verdict.** The cooperative should read a **basket** of local signals (are near-misses
  being voiced? are shortcuts normalizing?), apply just culture through its own trusted process, and
  **not** be handed (or hand itself) a single "safety score" or a certification. The module supplies
  the lenses; **acceptance and accountability stay with the cooperative and any local authority**, and
  culpability with `law/`.
