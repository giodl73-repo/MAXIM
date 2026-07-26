---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-factors:human-error-taxonomies
kind: guide
module: human-factors
section: human-factors
title: Human-Error Taxonomies - Classifying Failure as a Systems Property
status: source-custody
source_custody: partial
current_path: human-factors/04-HUMAN-ERROR-TAXONOMIES.md
canonical_path: human-factors/04-HUMAN-ERROR-TAXONOMIES.md
backsource_ids: [proof-backfill:human-factors:04-human-error-taxonomies]
concepts: [human-error, slips-lapses-mistakes, skill-rule-knowledge, violations, latent-conditions, active-failures, systems-view-of-error]
root_concepts: [human-error-taxonomies]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Human-Error Taxonomies — Classifying Failure as a Systems Property

**This guide owns** the *classification of human error* as an analytic starting point, not a
verdict: the **slip / lapse / mistake** taxonomy (Reason's GEMS), the **skill / rule /
knowledge** performance levels (Rasmussen's SRK) and the error forms each produces, the
distinction between **errors and violations** (and the violation sub-types), the split between
**active failures and latent conditions**, and — the load-bearing stance — **error as a
property of the system, not a moral failing of a person**. **It builds on**
`03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS` (workload and lost SA are error-shaping conditions)
and feeds `05-HUMAN-RELIABILITY-ANALYSIS` (which *quantifies* the error types this guide
*names*), `08-SAFETY-SYSTEMS-AND-HAZARD-ANALYSIS` (which *defends* against them), and
`11-ORGANIZATIONAL-SAFETY-CULTURE` (the *just-culture* handling of them). **It explicitly
defers**: the **cognitive mechanisms** of attention/memory/decision that *produce* error to
[`cognitive-science/`](../cognitive-science/00-OVERVIEW.md); the **clinical error taxonomy**
(diagnostic error, medication-error classes, patient-safety event coding) to
[`clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW`](../clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW.md);
**legal culpability and liability** to `law/`; and the **reliability mathematics** to
[`05`](05-HUMAN-RELIABILITY-ANALYSIS.md) and
[`systems-engineering/06`](../systems-engineering/06-FMEA-RELIABILITY.md).

> **Safety & ethics contract (binds every human-factors guide).** This is an **educational
> systems reference**. A taxonomy here is a **lens for analysis, never a blame ledger, a
> disciplinary tool, an accident-cause ruling, or a legal finding**. Classifying an event as a
> "slip" or a "knowledge-based mistake" describes *how the action failed given the conditions*;
> it does **not** assign fault, certify a person unfit, or determine liability. Causation of any
> real event belongs to a full investigation and its accountable owners, not to a label.

*Per-guide banner: "human error" is the **beginning** of an analysis, not its conclusion.
Every category below is a bounded, inter-rater-imperfect classification whose value is the
**different countermeasure** it implies — not a judgment of the person who was at the sharp end.*

---

## The Big Picture: Two Questions Split Every Error

To classify an unsafe act, human factors asks two orthogonal questions: **was the action as
intended?** (execution vs planning) and **at what cognitive level was the operator running?**
(skill / rule / knowledge). Together they generate the whole taxonomy — and each cell implies a
*different* fix.

```
THE ERROR TAXONOMY  (Reason's GEMS x Rasmussen's SRK -- each cell has a DIFFERENT fix)
================================================================================
                    | ACTION AS INTENDED?          | intention itself wrong?
                    | (execution failed)           | (the PLAN was wrong)
   -----------------+------------------------------+-----------------------------
   SKILL-based      | SLIP  (attention capture,    |  --
   (automatic)      |  wrong object/action)        |
                    | LAPSE (memory: step omitted) |
   -----------------+------------------------------+-----------------------------
   RULE-based       |  --                          | RULE-BASED MISTAKE
   (stored if-then) |                              |  (good rule misapplied, or
                    |                              |   a bad rule applied)
   -----------------+------------------------------+-----------------------------
   KNOWLEDGE-based  |  --                          | KNOWLEDGE-BASED MISTAKE
   (novel, effortful|                              |  (reasoning in a novel situation:
    reasoning)      |                              |   bounded rationality, biases)
   ================================================================================
   Plus a SEPARATE axis: VIOLATIONS -- intended deviations from a rule (routine,
   situational, exceptional, optimizing). A violation is not an execution/plan FAILURE;
   it is a chosen departure, usually shaped by the system that made the rule hard to follow.
```

The two families need **opposite countermeasures**: **slips and lapses** (right plan, wrong
execution) are best defended by **constraints, forcing functions, and cues** at the point of
action; **mistakes** (wrong plan) are defended by **better knowledge, feedback, and decision
support**; **violations** are defended by **fixing the system that made compliance costly**,
not by exhortation. Confusing the families — e.g., "re-training" a slip that needs a forcing
function — is the most common analytic error in this guide's domain.

---

## 1. Slips and Lapses — When the Action Betrays the Intention

At the **skill-based** level, behavior is automatic and attention is elsewhere. The plan is
correct; execution goes wrong.

- **Slips** (Norman, "Categorization of action slips," **1981**; Reason, **1990**) are
  **attention/execution** failures: a *capture slip* (a frequent action hijacks a similar
  intended one), a *description slip* (right action, wrong nearby object), a *mode slip* (right
  action, wrong device mode — see `06`). You *meant* the right thing and *did* another.
- **Lapses** are **memory** failures: an intended step is omitted or lost (place-losing after an
  interruption is the archetype). Lapses are often invisible until their consequence appears.

```
SLIP vs LAPSE  (skill-based; the plan was RIGHT)
--------------------------------------------------------------------------------
   SLIP  -> execution deviated (you did the wrong thing)   e.g., typed the practiced
            code, not the intended one; flipped the habitual switch
   LAPSE -> a step vanished (you skipped the right thing)  e.g., after a phone call,
            resumed two steps ahead and never re-armed the guard
   FIX FAMILY: constraints, forcing functions, interlocks, salient cues, checklists,
      interruption-recovery design -- NOT "try harder" or generic re-training.
```

**Why interruptions matter.** Skill-based sequences are fragile to interruption; the
place-keeping failure after a distraction is a canonical lapse. This is why guide `06` treats
mode/state visibility and guide `10` treats task structure as *error-shaping design variables*.

---

## 2. Mistakes — When the Intention Itself Is Wrong

At the **rule-** and **knowledge-based** levels, execution may be flawless but the **plan** is
wrong.

- **Rule-based mistakes:** a stored `if-then` rule is **misapplied** (a normally good rule fired
  in the wrong situation) or a **bad rule** was learned and applied. The operator is
  *pattern-matching* — efficient, but wrong when the pattern is a trap (a "strong-but-wrong"
  rule fires because it usually works).
- **Knowledge-based mistakes:** in a **novel** situation with no rule, the operator reasons from
  first principles under **bounded rationality** — and reasoning is where confirmation bias,
  anchoring, and an incomplete mental model do their damage. Knowledge-based work is slow,
  effortful, and error-prone precisely because it is *unpracticed*.

```
RULE- vs KNOWLEDGE-BASED MISTAKE  (the PLAN was wrong)
--------------------------------------------------------------------------------
   RULE-BASED      -> "I recognized this and applied my rule" -- but the rule did not
                      fit. Strong-but-wrong rules fire under time pressure. (SRK: rule)
   KNOWLEDGE-BASED -> "I had no rule and reasoned it out" -- and the reasoning was wrong
                      (bad mental model, bias, missing data). (SRK: knowledge)
   FIX FAMILY: better mental models & training, decision support, ecological displays
      (06) that show the work's deep structure, time to think, second opinions --
      NOT a forcing function (there is no single "wrong action" to block).
```

The **SRK mapping matters for the fix**: skill-level failures want *constraints*; rule-level
failures want *better rules and disconfirming cues*; knowledge-level failures want *support for
reasoning*. Why the operator's memory/attention/reasoning behave this way is
`cognitive-science/`'s to explain; this guide owns the *classification and its design
consequence*.

---

## 3. Violations — Intended Deviations, Shaped by the System

A **violation** is not an error in the execution/planning sense — it is a **deliberate
departure** from a rule or procedure. Critically, violations are usually **system-shaped**: the
rule was unworkable, slow, or contradicted by production pressure.

```
VIOLATION SUB-TYPES  (Reason 1990; routine/situational/exceptional; Lawton 1998)
--------------------------------------------------------------------------------
   ROUTINE       corner-cutting that has become normal (the rule is habitually skipped
                 because following it is costly and "nothing ever happens") -> normalization
                 of deviance (see 11)
   SITUATIONAL   the situation makes compliance impractical (missing tool, staffing, time)
   EXCEPTIONAL   a one-off departure in an unusual, often emergency, situation
   OPTIMIZING    deviation for personal goals (efficiency, stimulation), not the task
   -----------------------------------------------------------------------------
   KEY: a violation is a SYSTEMS signal. Punishing it without fixing the gap between
   work-as-imagined (the rule) and work-as-done (reality) just drives it underground.
```

The **error/violation distinction is not the culpability distinction.** A violation can be
blameless (a broken rule that made the task impossible) and a slip can, rarely, sit near
recklessness. Sorting *culpability* is `11`'s just-culture job and, at the legal end, `law/`'s —
**not** this taxonomy's.

---

## 4. Active Failures vs Latent Conditions — The Systems View

Reason's decisive move (*Human Error*, **1990**; *Managing the Risks of Organizational
Accidents*, **1997**) was to distinguish the **active failure** at the sharp end from the
**latent conditions** — the "resident pathogens" (understaffing, bad interfaces, poor
procedures, incompatible goals) laid down earlier by designers, managers, and regulators, that
lie dormant until an operator's action completes the path.

```
ACTIVE FAILURE vs LATENT CONDITION  (why "who touched it last?" is the wrong question)
--------------------------------------------------------------------------------
   BLUNT END (designers, managers, regulators)   SHARP END (operator)
      latent conditions laid down here:             active failure occurs here:
        bad control layout, thin staffing,            the slip / lapse / mistake /
        unworkable procedure, goal conflict           violation that completes the path
                 \                                    /
                  \___ align over time, and the ____/
                       accident trajectory passes through
   -----------------------------------------------------------------------------
   PERSON MODEL (old view): blame & retrain the sharp end -> misses the pathogens,
      so the next operator repeats the error.
   SYSTEM MODEL (new view, Reason; Dekker's "new view", 2002/2014): the sharp-end act
      is a SYMPTOM; fix the latent conditions -> the design carries the safety.
```

This is the guide's core claim: **"human error" is the name of a symptom.** The productive
analysis asks *what conditions made this action likely for a normal person*, not *who was to
blame*. Hindsight bias (`cognitive-science/`) makes the sharp-end act look obviously wrong
*after* the outcome is known; the discipline resists that with the systems view.

---

## 5. Detection, Recovery, and Why Multi-Channel Cues Matter

Errors are not just committed; many are **detected and recovered** before harm — and good design
maximizes detection. Detection relies on **feedback that the action's effect does not match the
intent**. Because a single cue can fail (unheard tone, unseen color for a color-vision-deficient
operator on a dim panel), **safety-relevant error cues must ride on ≥2 coding channels** — the
operator-safety twin of accessibility's "never color alone" (`06`, §3). A forcing function that
*prevents* a slip is better than a cue that *reveals* it; a cue that reveals it is better than
nothing.

---

## The Boundaries (ownership in one place)

```
WHO OWNS WHAT AROUND HUMAN ERROR
--------------------------------------------------------------------------------
   this guide (04)     the TAXONOMY: slip/lapse/mistake, SRK, violations, latent vs
                       active, error-as-systems-property, the fix FAMILY per type
   cognitive-science/  the MECHANISM: why attention/memory/reasoning fail (bias, WM limits)
   05 (HRA)            the QUANTIFICATION: turning these types into a bounded HEP + PSFs
   08 (hazard)         the DEFENSE: barriers/bow-tie/STAMP that stop the trajectory
   11 (culture)        the CULPABILITY handling: just culture, reporting, normalization
   clinical-medicine/11 the CLINICAL taxonomy: diagnostic/medication error coding in care
   law/                LEGAL culpability and liability
   -----------------------------------------------------------------------------
   Rule: this guide NAMES and CLASSIFIES error and picks the fix FAMILY; it quantifies
   nothing, defends nothing, and judges no person.
```

---

## A Worked Classification Pass — Five Synthetic Events (reproducible)

*All events are **synthetic** and non-operational. The demonstration is the *classification and
its rationale*, plus a simple tally of the fix-family mix — not a judgment of any person or a
ruling about any event.*

Classify each event on three axes — **SRK level**, **GEMS type**, **active/latent emphasis** —
and read off the **fix family**:

| # | Synthetic event | SRK level | GEMS type | Active/latent | Fix family |
|---|---|---|---|---|---|
| E1 | Operator flips the *habitual* switch, not the intended adjacent one, mid-routine | Skill | Slip (capture) | Active; latent = adjacent identical controls | Constraint / coding (`06`) |
| E2 | After a phone interruption, resumes two steps ahead and omits re-arming a guard | Skill | Lapse (omission) | Active; latent = no interruption-recovery design | Forcing function / checklist |
| E3 | Applies the standard restart rule; today's fault is the atypical case it doesn't fit | Rule | Rule-based mistake (strong-but-wrong) | Active; latent = rule lacks a disconfirming cue | Better rule + disconfirming display |
| E4 | Novel multi-fault upset with no procedure; reasons from a wrong mental model | Knowledge | Knowledge-based mistake | Active; latent = no ecological display, no time to think | Decision support / EID (`06`), time |
| E5 | Skips a slow verification step that "is always fine," under shift-output pressure | Rule | Routine violation | Latent-dominant: production pressure, costly rule | Fix the work/rule gap (`11`), not blame |

```
FIX-FAMILY MIX  (tally of the five synthetic events -- the ANALYTIC payoff)
--------------------------------------------------------------------------------
   constraint / forcing / coding  : E1, E2         -> 2/5  (skill-level: block the slip)
   knowledge / decision support   : E3, E4         -> 2/5  (mistake: support the plan)
   fix the system/rule gap        : E5             -> 1/5  (violation: close work-as-done gap)
   -----------------------------------------------------------------------------
   Reading: 2 of 5 would be UNTOUCHED by "re-training the operator" (E1, E2 need design
   constraints), and E5 would get WORSE under blame. The taxonomy's value is that it
   routes each event to a DIFFERENT, effective countermeasure.
```

**Uncertainty / validity / bias note.** (1) **Classification is not exact.** The slip/lapse and
rule/knowledge boundaries are judgment calls; independent raters disagree, so a serious analysis
records *inter-rater* agreement and reasons, and treats a single label as provisional. (2)
**Hindsight bias inflates "mistake" labels** — knowing the outcome makes the operator's plan look
obviously wrong; the honest analysis reconstructs what was knowable *at the time*. (3) The
**active/latent split is a matter of emphasis, not a clean cut** — every event has both; the
systems view deliberately weights the latent side to avoid the person-model trap. (4) This is a
**classification exercise**, not a probability estimate (that is `05`) and not a cause
determination.

---

## A Fully Worked Case — Analyzing a Near-Miss Without Blame (illustrative, fictional)

*Fictional throughout. It demonstrates the systems view of error — not an investigation, a
cause ruling, or a judgment about any person.*

**Setting.** At *fictional* **Larkfield Chemicals**, a night-shift operator opens the wrong one
of two identical, adjacent transfer valves; a level alarm catches it and no harm occurs. The
plant asks human factors to "explain the operator error."

1. **Reframe from person to system.** The question becomes *what made opening the wrong valve
   likely for a competent, rested-enough operator on nights?* — not *who to blame* (§4).
2. **Classify the active failure.** Right intention (transfer product), wrong object executed →
   a **skill-based slip (description/capture)**, favored by two identical adjacent valves with
   weak labels on a dim panel (§1).
3. **Surface the latent conditions.** Identical hardware, poor labeling, low night lighting,
   single-channel state feedback, and thin staffing that discouraged a second check — each a
   *resident pathogen* laid down by design and staffing decisions, not by the operator (§4).
4. **Pick the fix family.** Because this is a slip, **constraints and coding** dominate: distinct
   valve shapes/positions, redundant state coding (color **+** shape **+** position **+** label,
   §5), and a forcing check — **not** "re-train the operator," which would leave the pathogens in
   place for the next person (§1).
5. **Hand off the rest.** The *probability* this recurs and how much a barrier lowers it →
   `05`; the *barrier model* → `08`; whether the near-miss gets **reported without punishment**
   so the system can learn → `11`. Whether anyone is *culpable* is a **just-culture** question
   (`11`), not a taxonomy output; any *legal* question is `law/`'s.

**Reading.** The event is classified, its latent conditions named, and each routed to an
effective countermeasure — with **no** blame assigned, **no** cause ruled, and **no** judgment
of the operator. That restraint is the point.

---

## Reader Tasks (answerable from this guide)

1. **Classify and prescribe.** For events E1–E4 in the worked pass, give the SRK level, the GEMS
   type, and the *fix family*, and explain why applying E1's fix (a constraint) to E4 (a
   knowledge-based mistake) would fail (§1–2, Worked pass).
2. **Separate error from violation.** Given "the operator skipped the slow check that is always
   fine," classify it as a **routine violation**, name the *system* condition that shaped it, and
   explain why punishing it drives it underground (§3; forward to `11`).
3. **Find the latent conditions.** For the Larkfield near-miss, list three latent conditions and
   explain why "blame and retrain the operator" leaves them intact (§4, Worked case).
4. **Resist hindsight.** Given a knowledge-based mistake in a novel upset, explain how knowing the
   outcome makes the operator's plan look "obviously wrong," and how you would reconstruct what was
   knowable at the time (§4, Worked pass uncertainty note).
5. **Hold the boundary.** State what this guide does (names the error type and fix family) and
   what it refuses to do (assign blame, estimate a probability, rule a cause, decide culpability),
   and name the owner of each refused task (Boundaries).

---

## Decision Cheat Sheet

| The unsafe act looks like... | Classify as | Fix family (not this) |
|---|---|---|
| Right plan, wrong action slipped out | **Slip** (skill) | constraint/coding — *not* "try harder" |
| Right plan, a step was forgotten | **Lapse** (skill) | forcing function/checklist/interruption design |
| Recognized the situation, applied a rule that didn't fit | **Rule-based mistake** | better rule + disconfirming cue — *not* a block |
| No rule, reasoned it out, reasoning was wrong | **Knowledge-based mistake** | decision support/EID/time — *not* a forcing function |
| Deliberately departed from a costly/unworkable rule | **Violation** (routine/situational/…) | fix the work-as-done gap (`11`) — *not* exhortation |
| "The operator caused it" | reframe: **symptom of latent conditions** | find the pathogens (§4) — *not* blame |
| "How likely is this?" / "What barrier stops it?" | **out of scope** | → `05` (HEP), `08` (barriers) |
| "Is anyone culpable / liable?" | **out of scope** | → `11` (just culture), `law/` (legal) |

---

## Common Confusion Points

**"An error and a violation are the same thing."** No. An error is an *unintended* failure of
execution or planning; a violation is an *intended* departure from a rule, usually shaped by a
system that made compliance costly. They need different countermeasures, and neither maps
directly to blame (§3).

**"A slip means the operator was careless."** A slip is a **skill-based execution** failure that
happens *to* attentive, competent people — capture, description, and mode slips are structural,
not character flaws. The fix is a constraint, not a reprimand (§1).

**"Human error is the cause of the accident."** In this module "human error" is a **symptom** to
be explained by latent conditions and defeated defenses (`04`,`08`), never an endpoint. "The
operator erred" is where the analysis *starts* (§4).

**"Classifying the error is objective."** The labels are **judgment calls** with real inter-rater
disagreement and heavy hindsight bias; a single label is provisional, and serious work records
its reasoning and uncertainty (Worked pass).

**"This taxonomy tells us who to discipline."** It does not. Culpability is a **just-culture**
question (`11`) and, at the legal end, `law/`'s; the taxonomy names *how* the action failed, not
*who is at fault* (safety contract).

---

## Global, WEIRD & Resource Caveats

- **The taxonomy is Western/industrial in origin** (Reason, Rasmussen, Norman, Dekker), and its
  examples come from aviation, nuclear, and process industries. The categories generalize well,
  but the *examples* and the assumption of formal written procedures do not fit every work
  culture — much consequential work runs on oral tradition and apprenticeship, where "the rule"
  is tacit and the error/violation line is drawn differently.
- **The systems view has a resource precondition.** Fixing latent conditions (better interfaces,
  staffing, forcing functions) costs money; low-resource settings are pushed toward the cheap,
  ineffective "blame and retrain" response precisely because the systemic fix is unaffordable —
  which the honest analysis should *name* as a latent condition, not hide.
- **Reporting shapes the data.** In cultures (or organizations) where reporting an error invites
  punishment, the observed error mix is censored, biasing any taxonomy built from reports — a
  direct dependency on the just-culture conditions of `11`.

---

## A Contrasting Example (non-WEIRD, low-resource)

*Fictional, to show how the same taxonomy reads differently when procedures are tacit and
resources are thin.*

**Setting.** A *fictional* community-run micro-hydro station in a remote highland is operated by
rotating villagers trained by apprenticeship. There are **no written procedures**; "the rules"
live in an experienced operator's head and in oral custom.

**How the taxonomy adapts.**
- **The error/violation line moves.** With tacit rules, a "violation" is departure from *custom*,
  not a written SOP; classifying it requires first *eliciting* the unwritten work-as-done (guide
  `10`'s task analysis), or the analyst will mislabel skilled adaptation as violation.
- **Latent conditions are resource-shaped.** Identical unlabeled valves and a single dim
  indicator are latent conditions here too — but the *fix family* must respect that redundant
  electronic coding may be unaffordable; a **cheap physical forcing function** (a distinct hand
  wheel, a mechanical interlock) may be the appropriate multi-channel redundancy.
- **The refusal still holds.** The analysis must **not** conclude the villagers are "unsafe
  operators," certify the station, or rule a cause — it names error types and fix families and
  defers acceptance to the community and any local authority. Treating an unwritten practice as
  culpable *because* it is unwritten would be exactly the person-model error the guide rejects.
