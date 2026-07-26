---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-HUMAN-RELIABILITY-ANALYSIS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-factors:human-reliability-analysis
kind: guide
module: human-factors
section: human-factors
title: Human-Reliability Analysis - The Human-Error Probability as a Bounded Estimate
status: source-custody
source_custody: partial
current_path: human-factors/05-HUMAN-RELIABILITY-ANALYSIS.md
canonical_path: human-factors/05-HUMAN-RELIABILITY-ANALYSIS.md
backsource_ids: [mdloom-backfill:human-factors:05-human-reliability-analysis]
concepts: [human-reliability-analysis, human-error-probability, performance-shaping-factors, therp, heart, spar-h, cream, hra-uncertainty]
root_concepts: [human-reliability-analysis]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Human-Reliability Analysis — The Human-Error Probability as a Bounded Estimate

**This guide owns** the *quantification of human error*: how human-reliability analysis (HRA)
turns a task and its conditions into a **human-error probability (HEP)** that can enter a
risk model, and — the load-bearing epistemic point — **why a HEP is a wide, method-bounded
estimate, not a fact**. It owns the **method families** (THERP, HEART, SPAR-H, CREAM; first-
vs second-generation HRA), the machinery of **performance-shaping factors (PSFs)** and
**dependency**, and the honest treatment of **HRA's large uncertainty and weak validation**.
**It builds on** [`04-HUMAN-ERROR-TAXONOMIES`](04-HUMAN-ERROR-TAXONOMIES.md) (the error types HRA
quantifies) and
[`03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS`](03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md)
(workload/SA as PSFs), and feeds
[`08-SAFETY-SYSTEMS-AND-HAZARD-ANALYSIS`](08-SAFETY-SYSTEMS-AND-HAZARD-ANALYSIS.md) (which places
the HEP in a barrier/tree model). **It explicitly borrows** the **fault-tree / event-tree
combination and reliability mathematics** from
[`systems-engineering/06-FMEA-RELIABILITY`](../systems-engineering/06-FMEA-RELIABILITY.md) — the
human is a **basic event** whose probability HRA supplies; the *tree math that combines it* is
sys-eng's, re-derived nowhere here. **It explicitly defers**: **inferential statistics / lognormal
fitting** to [`statistics-applied/`](../statistics-applied/00-OVERVIEW.md); the **cognitive
mechanism** to [`cognitive-science/`](../cognitive-science/00-OVERVIEW.md); and any **clinical
error-rate** practice to
[`clinical-medicine/11`](../clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW.md).

> **Safety & ethics contract (binds every human-factors guide).** This is an **educational
> systems reference**. A HEP here is a **modeled, uncertain estimate for conceptual literacy**,
> **not** a safety certification, a probability that a specific person will fail, an accident
> prediction, or a compliance number. Nothing here declares a task, plant, or operator
> "reliable enough." Screening HEPs are population- and method-relative; **acceptance of any
> risk number belongs to the accountable organization and its regulator**, never to this module.

*Per-guide banner: every HEP below is a **synthetic, reproducible** illustration of the
*method*, framed as a **range**. Real HRA numbers carry error factors of several-fold, disagree
across methods, and rest on sparse data — treat any single HEP as the *center of a wide, dated,
method-bounded interval*, not a point.*

---

## The Big Picture: A HEP Is a Model Output, Not a Measurement

HRA answers a narrow question — *given this task under these conditions, what is the modeled
probability the required human action fails?* — so the answer can enter a risk model beside
hardware failure rates. The universal shape of every method is the same: a **nominal
probability** for a generic kind of task, **multiplied or adjusted by the conditions** (PSFs),
producing a **HEP with wide uncertainty**.

```
THE HRA PIPELINE  (every method is a variation on this shape)
================================================================================
   TASK + CONTEXT
        |  (1) decompose: what human actions must succeed? (task analysis, guide 10)
        v
   NOMINAL HEP  (a base rate for this GENERIC task type)      e.g., "diagnose" ~ 0.01
        |  (2) adjust for CONDITIONS -- performance-shaping factors (PSFs):
        |      time, stress, complexity, experience, procedures, HMI/ergonomics,
        v      fitness, teamwork  -> each a MULTIPLIER or level
   TASK HEP  (nominal x PSFs, with an adjustment so HEP stays <= 1)
        |  (3) DEPENDENCY: correlated actions are not independent -> combine with a
        v      dependency model, not naive multiplication
   HEP as a RANGE  (a distribution with an error factor, NOT a point)
        |  (4) place into the risk model as a BASIC EVENT
        v
   FAULT / EVENT TREE  <-- combination math BORROWED from systems-engineering/06
================================================================================
   The signature honesty of HRA: step (4) hands a NUMBER to a precise-looking tree, but
   that number is the WIDEST-uncertainty input in the whole model. Never launder a HEP's
   uncertainty by quoting only its point value.
```

The discipline's contribution is not the specific number — it is the **structured,
auditable reasoning** from task and conditions to a *bounded* number, and the *discipline of
carrying the uncertainty forward*.

---

## 1. First-Generation HRA — THERP and HEART

**First-generation** methods decompose a task into steps, assign each a nominal error
probability from a table, and adjust for conditions.

- **THERP** — Technique for Human Error Rate Prediction (Swain & Guttmann, **NUREG/CR-1278,
  1983**). Builds an **HRA event tree** of correct/incorrect branches, reads **nominal HEPs**
  from handbook tables, applies **PSFs**, and — importantly — models **dependency** between
  actions on a five-level scale (zero / low / moderate / high / complete). THERP is the
  granular, effortful ancestor of the field.
- **HEART** — Human Error Assessment and Reduction Technique (Williams, **1988**). Faster:
  classify the task into a **Generic Task Type (GTT)** with a nominal HEP, then multiply by
  selected **Error-Producing Conditions (EPCs)**, each with a published maximum multiplier,
  scaled by an **Assessed Proportion of Affect (APOA)** the analyst judges. HEART's value is
  that its EPCs (unfamiliarity, time shortage, poor feedback, …) *name the conditions worth
  fixing* — it is a reduction technique, not just an assessment one.

```
FIRST-GENERATION SHAPE  (THERP vs HEART -- same skeleton, different granularity)
--------------------------------------------------------------------------------
   THERP  : event tree of steps -> nominal HEP per step (tables) -> PSFs -> dependency
            -> combine up the tree. GRANULAR, data-hungry, slow.
   HEART  : one GTT nominal HEP -> x product of [1 + (EPC_max - 1) x APOA] -> task HEP.
            FAST, transparent about WHICH conditions dominate (the big EPCs).
   Both: the nominal values and multipliers are DATED, largely nuclear/industrial in
   origin, and carry wide uncertainty -- they are calibration conventions, not constants.
```

---

## 2. Second-Generation HRA — SPAR-H and CREAM

**Second-generation** methods answer the critique that first-generation HRA ignored *context
and cognition*. They foreground the situation that drives error.

- **SPAR-H** — Standardized Plant Analysis Risk-HRA (Gertman, Blackman, et al., **NUREG/CR-6883,
  2005**; US NRC, public domain). Splits each task into **diagnosis** and **action**, assigns a
  **nominal HEP** to each, and multiplies by **eight PSFs** (available time, stress/stressors,
  complexity, experience/training, procedures, ergonomics/HMI, fitness for duty, work
  processes), with an explicit **adjustment formula** — applied **only when 3 or more PSFs are
  negative** (worse than nominal) — so a pile-up of negative PSFs cannot push the HEP over 1. Its
  worksheets make it the widely-used screening workhorse.
- **CREAM** — Cognitive Reliability and Error Analysis Method (Hollnagel, **1998**). Ties error
  probability to **control modes** (scrambled → opportunistic → tactical → strategic) set by
  **Common Performance Conditions (CPCs)** — a genuinely context-first model rather than a
  table of acts.

```
SECOND-GENERATION SHAPE  (context and cognition FIRST)
--------------------------------------------------------------------------------
   SPAR-H : HEP = NHEP(diagnosis/action) x (8 PSF multipliers), adjusted to stay <= 1.
            Public-domain worksheets; diagnosis and action scored separately.
   CREAM  : CPCs set a CONTROL MODE; the mode implies a HEP interval. Error is a loss of
            control, not a mis-stepped table row.
   Shift from gen-1: the QUESTION moved from "what is this act's rate?" to "what context
   is the operator in, and what does that context do to reliability?"
```

---

## 3. Performance-Shaping Factors — Where the HEP Actually Comes From

Across all methods, the **PSFs do most of the work**: the nominal HEP is a starting point, and
the *conditions* swing it by orders of magnitude. The recurring PSFs are **time available,
stress, task complexity, experience/training, quality of procedures, HMI/ergonomics (guide
`06`), fitness/fatigue, and teamwork/work processes** — and workload/SA from `03` feed several
of them directly.

The design payoff mirrors `04`: because PSFs are the dominant term, **the way to lower a HEP is
to improve the conditions** (more time, better procedures, a clearer display) — a *reduction*
technique, not a plea for the operator to be more careful.

**Accessibility as a safety-relevant PSF (the ≥2-channel invariant).** Because the *HMI/ergonomics*
PSF swings the HEP, a display that carries a safety-relevant state on a **single** channel (color or
tone alone) inflates the effective HEP for any operator who cannot use that channel — so
safety-relevant cues must ride on **≥2 coding channels**, the operator-safety twin of
accessibility's "never color alone" ([`06` §3](06-DISPLAY-CONTROL-INTERFACE-DESIGN.md)). Sampling
that omits the sensory tails ([`10`](10-METHODS-AND-MEASUREMENT.md)) hides the very operators for
whom a single-channel cue fails.

---

## 4. Dependency and the Uncertainty That Dominates

Two facts keep HRA honest.

- **Dependency.** Human actions are often **correlated** — the same misunderstanding fails a
  check *and* its backup — so multiplying independent HEPs **understates** risk. THERP's
  five-level dependency model (and SPAR-H's dependency step) exist precisely to stop the
  independence fallacy. This is where HRA and the tree math of `systems-engineering/06` must
  agree: a "redundant" human barrier may not be independent.
- **Uncertainty.** A HEP carries an **error factor (EF)** — a lognormal spread often several-fold
  — and, worse, **different methods give different HEPs for the same task**. HRA **benchmark and
  empirical studies** have repeatedly found analyst-to-analyst and method-to-method spreads of
  **an order of magnitude or more**. The only defensible output is a **range with a stated
  method and PSF set**, never a bare point.

---

## The Boundaries (ownership in one place)

```
WHO OWNS WHAT AROUND HRA
--------------------------------------------------------------------------------
   this guide (05)      the HEP: methods (THERP/HEART/SPAR-H/CREAM), PSFs, dependency,
                        and the UNCERTAINTY discipline -- a bounded estimate
   systems-engineering/06  the TREE MATH: fault/event trees, cut sets, reliability
                        combination -- HRA supplies the human basic-event probability only
   04 (error taxonomy)  the CLASSIFICATION the HEP quantifies (slip/mistake/violation)
   03 (workload/SA)     several PSFs (time pressure, load, lost SA)
   statistics-applied/  lognormal fitting, uncertainty propagation, sampling
   clinical-medicine/11 clinical error-rate practice in care settings
   -----------------------------------------------------------------------------
   Rule: HRA ESTIMATES the human basic-event probability as a range; it does NOT build
   the tree, certify the risk, or predict a specific person's failure.
```

---

## A Worked HEP Pass — SPAR-H Structure, Reported as a Range (reproducible)

*The method attributions and dates are real; the **task inputs are synthetic** and the numbers
are a reproducible illustration of SPAR-H's *structure*. This is conceptual literacy, not an HRA
of any real task, and it certifies nothing.*

**The task (synthetic).** An operator must **diagnose** an off-normal condition and take a
**recovery action**, under **barely adequate time** and **high stress**, with **moderately
complex** cues, everything else nominal.

**SPAR-H structure (public-domain NUREG/CR-6883).** `HEP = NHEP × ∏(PSF multipliers)`, with a
mandatory **adjustment** when the product would push HEP toward/over 1:

```
BOUNDED SPAR-H EXCERPT  (public-domain NUREG/CR-6883; cells used here)
--------------------------------------------------------------------------------
   NOMINAL HEP        diagnosis = 0.01     action = 0.001
   AVAILABLE TIME     inadequate -> HEP = 1.0 ; barely adequate x10 ; nominal x1 ;
                      extra time x0.1 ; expansive x0.01
   STRESS/STRESSORS   nominal x1 ; high x2 ; extreme x5
   COMPLEXITY         nominal x1 ; moderately complex x2 ; highly complex x5
   (experience/training, procedures, HMI, fitness, work processes here = nominal x1)
   ADJUSTMENT (>=3 negative PSFs, keeps HEP <= 1):
      HEP_adj = (NHEP x P) / ( NHEP x (P - 1) + 1 ),   P = product of multipliers
```

**Diagnosis HEP (point).** `P = 10 (time) × 2 (stress) × 2 (complexity) = 40`.
Unadjusted `= 0.01 × 40 = 0.40`; adjusted `= 0.01×40 / (0.01×(40−1)+1) = 0.40 / 1.39 ≈ 0.288`.

**Action HEP (point).** Same PSFs on the action nominal: `P = 40`, unadjusted
`= 0.001×40 = 0.04`; adjusted `= 0.04 / (0.001×39 + 1) = 0.04 / 1.039 ≈ 0.0385`.

**Combine diagnosis + action.** If the two were **independent**, task-failure
`≈ 1 − (1−0.288)(1−0.0385) ≈ 0.315`. But diagnosis and action share the same operator, cues,
and stressor, so a **dependency** adjustment applies — treat them as *at least low-to-moderate
dependent*, which **raises** the combined estimate above the independent 0.315. (The exact
dependency combination is a modeling choice; the point is the direction.)

**Now the honest part — report a RANGE, not 0.29.**

```
THE HEP IS A RANGE, NOT A POINT  (why quoting 0.29 alone is malpractice)
--------------------------------------------------------------------------------
   (a) PARAMETER UNCERTAINTY -- and the probability CEILING. HRA HEPs get a lognormal
       band summarized by an ERROR FACTOR, defined (NUREG convention) as
          EF = sqrt(P95 / P05),  so the 90% band is  [ median / EF ,  median x EF ].
       Here median ~0.29, EF ~5:  P05 = 0.29 / 5 ~ 0.06   (a valid lower bound).
       But  P95 = 0.29 x 5 = 1.45  -- NOT a probability. A HEP lives in (0,1], yet this
       lognormal puts ~10% of its mass ABOVE 1 (impossible). So you may NOT just write
       "0.06-0.9": the upper bound needs an explicit BOUNDED-PROBABILITY treatment --
       truncate the lognormal at HEP=1 and renormalize, or fit a logit-normal / Beta on
       (0,1). Truncated + renormalized here, the 90% band is ~[0.06, 0.8]; the 0.8 is a
       property of the BOUNDED MODEL, not read off the error factor. Lesson: the EF
       convention is borrowed from hardware PRA where failure probs are tiny; a symmetric-
       in-log "x5" band is only self-consistent while median < 1/EF (= 0.2 for EF=5). Our
       0.29 > 0.2, so the naive band overflows the ceiling and MUST be bounded -- never
       laundered into a tidy "x5" interval.
   (b) METHOD VARIANCE: a HEART assessment of the "same" task (a GTT nominal times
       time-shortage/unfamiliarity EPCs) could land materially higher or lower;
       benchmark studies show method-to-method spreads of an order of magnitude.
   (c) PSF SENSITIVITY: the single biggest lever is TIME. Sweep the time PSF, all else
       fixed -- and WATCH THE ADJUSTMENT TRIGGER (it applies ONLY at >=3 negative PSFs):
          time = barely adequate (x10) -> 3 neg PSFs (time,stress,complexity): ADJUST
                                          P=40 ; 0.01x40/(0.01x39+1)     ~ 0.288
          time = nominal       (x1)    -> 2 neg PSFs (stress,complexity): NO adjustment
                                          P=4  ; 0.01x4                   = 0.04
          time = extra time    (x0.1)  -> 2 neg PSFs (stress,complexity): NO adjustment
                                          P=0.4; 0.01x0.4                 = 0.004
       -> the adjustment DROPS OUT once fewer than 3 PSFs are negative (so the earlier
          "P-1" formula must not be applied at x1 / x0.1); the HEP still swings
          ~0.288 -> 0.004 (~70x) across two time steps. The CONDITIONS dominate the nominal.
   -----------------------------------------------------------------------------
   HONEST OUTPUT: "diagnosis HEP median ~0.29; 5th ~0.06 (= median/EF, EF~5); 95th bounded
   BELOW 1 by the probability ceiling -- a truncated-lognormal/logit-normal puts it ~0.8
   (model-dependent, NOT median x EF = 1.45); method variance could widen it; most
   sensitive to available time (SPAR-H, stated PSFs)."
```

**Uncertainty / validity / bias note.** (1) The nominal HEPs and multipliers are **dated,
nuclear-industrial-origin** calibration conventions; transferring them to other domains is an
extrapolation. (2) HRA has **weak empirical validation** — real human-error data is sparse, so
the nominals rest heavily on expert judgment; benchmark exercises show wide inter-method and
inter-analyst variance. (3) **Dependency is easy to get wrong** and errs toward *under*-stating
risk when analysts assume independence. (4) The output is a **screening range for conceptual
use**, not a prediction about a person and not a safety certificate.

---

## A Fully Worked Case — A HEP Inside a Barrier Model (illustrative, fictional)

*Fictional. It demonstrates how a bounded HEP feeds a risk model — not an HRA, a certification,
or a risk acceptance for any real system.*

**Setting.** *Fictional* **Kestrel Terminal** models a rare tank-overfill scenario. A hardware
high-level trip exists; the *human backup* is "operator diagnoses the high level and closes the
feed in time." Human factors is asked for the **human backup's failure probability**.

1. **Decompose (guide `10`).** The human action = *diagnose high level from the alarm* + *close
   the feed within the available window* — a diagnosis + action pair (§Worked pass).
2. **Score PSFs honestly.** Time is **barely adequate** (short window), stress **high** during an
   upset, complexity **moderate**; procedures and HMI are nominal. That is **three negative PSFs**,
   so the SPAR-H adjustment applies; it yields the synthetic ~0.29 diagnosis / ~0.04 action of the
   worked pass — reported as a **bounded range** (5th ~0.06; 95th bounded below 1, ~0.8 under a
   truncated-lognormal — *not* median×EF = 1.45), never a point.
3. **Check dependency, don't assume independence (§4).** The hardware trip and the human backup
   share the *same* level instrument; if that instrument is the failure, **both** barriers fail
   together — a common-cause coupling the tree must model. A "redundant" human barrier that reads
   the same broken gauge is **not** independent.
4. **Hand the number to the tree — don't build the tree here.** The HEP range enters the
   **event tree** as the human basic event; the *combination with the hardware trip* and the
   cut-set math are **`systems-engineering/06`**'s, and the barrier picture is **`08`**'s. HRA
   supplies *one uncertain input*, clearly bounded.
5. **State what this is not.** The result is a **wide screening range for a modeled scenario**,
   not a statement that Kestrel is "safe" or "acceptable." **Acceptance of the risk number is
   Kestrel's and its regulator's**, informed by evidence — no module signs off.

**Reading.** One human basic event, estimated as a bounded range, with dependency flagged and
the tree math deferred — the discipline's job is the *honest number and its uncertainty*, not
the verdict.

---

## Reader Tasks (answerable from this guide)

1. **Compute a SPAR-H HEP and its adjustment.** For the diagnosis task with time ×10, stress ×2,
   complexity ×2 (nominal 0.01) — **three negative PSFs, so the adjustment applies** — compute the
   unadjusted and adjusted HEP; state the **≥3-negative-PSF trigger**, and explain why the
   adjustment formula exists and what it prevents (§2, §Worked pass).
2. **Report it as a bounded range.** Given a **median** HEP ~0.29 and an error factor EF ≈ 5,
   compute the 5th percentile (= median/EF) and show that median×EF = 1.45 is **not** a valid
   probability; explain the **bounded-probability treatment** (truncate/renormalize at HEP = 1, or
   a logit-normal/Beta) that yields a 95th below 1 (~0.8), write the one-sentence "honest output" a
   risk model should carry — and say why quoting only 0.29, *or* a bare "0.06–0.9 from EF = 5",
   is misleading (§4, Worked pass).
3. **Find the dominant PSF.** Sweep the available-time PSF (×10 → ×1 → ×0.1) with all else fixed;
   show the HEP swing **and where the SPAR-H adjustment stops applying** (below three negative
   PSFs, use the plain product), and explain why "improve the conditions" beats "be more careful"
   as a reduction strategy (§3, Worked pass).
4. **Catch a dependency error.** Given "we have a hardware trip *and* an operator backup, so
   multiply their independent failure probabilities," explain why that understates risk when both
   read the same instrument, and what a dependency model does instead (§4, Worked case).
5. **Hold the boundary.** State which part of the Kestrel analysis is HRA's (the human
   basic-event range) and which is `systems-engineering/06`'s (the tree combination), and why HRA
   does not certify the risk (Boundaries, Worked case).

---

## Decision Cheat Sheet

| Situation | Move | Why (this guide) |
|---|---|---|
| Need a human basic-event probability for a risk model | run an HRA method; output a **range** | HEP is a bounded estimate, not a point (§4) |
| Screening many tasks quickly | **HEART** (GTT × EPCs) or **SPAR-H** worksheets | fast, transparent about dominant conditions (§1–2) |
| Fine-grained, step-by-step nuclear-style task | **THERP** event tree with dependency | granular, models step dependency (§1) |
| Context/cognition drives the error | **SPAR-H** PSFs or **CREAM** control modes | second-generation, context-first (§2) |
| Two human checks "back each other up" | model **dependency**, don't multiply independently | correlated failures understated otherwise (§4) |
| Asked for "the HEP" | give **central + error factor + method + PSFs** | single points hide order-of-magnitude spread (§4) |
| Want to lower a HEP | improve **PSFs** (time, procedures, HMI) | conditions dominate the nominal (§3) |
| Combining the HEP with hardware failures | hand to **[`systems-engineering/06`](../systems-engineering/06-FMEA-RELIABILITY.md)** tree math | HRA supplies the input, not the tree (Boundaries) |
| "Is this risk acceptable / certified?" | **out of scope** — org + regulator decide | safety contract |

---

## Common Confusion Points

**"A HEP is a probability that this operator will fail."** No. It is a **population- and
method-relative model output** for a task under stated conditions — a screening estimate with
wide uncertainty, not a prediction about a specific person (safety contract, §4).

**"Quote the HEP as a single number."** The single most common HRA malpractice. HEPs carry
error factors of several-fold and disagree across methods by an order of magnitude; the output
must be a **range with a stated method and PSF set** (§4).

**"Two human checks are independent, so multiply."** They usually are **not** — shared cues,
shared operator, shared instrument create dependency, and independence *understates* risk. This
is exactly what THERP's dependency model and SPAR-H's dependency step exist to catch (§4).

**"HRA is validated like a physics model."** It is **weakly validated** — human-error data is
sparse, nominals rest on expert judgment, and benchmark studies show large spread. HRA's value
is auditable, condition-sensitive *reasoning*, not precision (§4).

**"Lowering the HEP means telling the operator to try harder."** No. Because **PSFs dominate**,
the HEP falls when the *conditions* improve — more time, better procedures, a clearer HMI —
which is why it is a *reduction* technique, not an exhortation (§3).

---

## Global, WEIRD & Resource Caveats

- **The nominal data is nuclear/aerospace/Western-industrial.** THERP, SPAR-H, and much of HEART
  come from Western nuclear and defense work; their nominal HEPs and PSF multipliers are
  calibrated to those operators, procedures, and cultures. Transferring them to other domains,
  languages, or work cultures is an extrapolation that widens the already-wide uncertainty — say
  so explicitly.
- **Data scarcity is universal but unequal.** Everyone lacks good human-error base-rate data;
  low-resource settings lack it *more* and also lack the analyst time SPAR-H/THERP demand, pushing
  practice toward the crudest screening — with correspondingly wider honest ranges, not falsely
  precise points.
- **PSFs encode a work culture.** "Adequate time," "good procedures," and "fitness for duty" are
  judged against a particular staffing and shift model; a PSF set imported wholesale can mis-score
  a differently-organized workforce. The correction is local elicitation (guide `10`), not a
  borrowed multiplier table.

---

## A Contrasting Example (non-WEIRD, low-resource)

*Fictional, to show how HRA reasoning survives when the nominal tables do not transfer.*

**Setting.** A *fictional* regional grid control room in a lower-income country must reason about
the reliability of a manual load-shedding action during instability. It has **no** local
human-error database and **no** budget for a full THERP study; the SPAR-H nominals were derived
from Western nuclear operators.

**How HRA adapts honestly.**
- **Use the structure, distrust the constants.** The *pipeline* (nominal × PSFs × dependency →
  range) still organizes the reasoning; but the imported nominals become a **rough prior**, and
  the honest output widens the range (a larger error factor) to reflect the extrapolation — not a
  borrowed point value dressed as local truth.
- **Score PSFs for the real conditions.** Long single-operator shifts, sparse procedures, and an
  aging HMI are *negative PSFs here*; naming them both raises the estimate **and** identifies the
  cheapest reliability improvements (a second operator at peak, a better procedure) — the
  reduction payoff.
- **Refuse the false verdict.** The analysis yields a **wide screening range**, flags dependency
  between the operator and a single frequency reading, and **defers acceptance** to the utility and
  its regulator. It does **not** declare the action "reliable enough," certify the room, or hide the
  extrapolation behind a precise-looking number.
