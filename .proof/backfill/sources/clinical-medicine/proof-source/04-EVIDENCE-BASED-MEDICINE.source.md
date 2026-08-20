---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "04-EVIDENCE-BASED-MEDICINE.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:clinical-medicine:evidence-based-medicine
kind: guide
module: clinical-medicine
section: clinical-medicine
title: Evidence-Based Medicine - Appraising and Applying Population Evidence to One Patient
status: source-custody
source_custody: partial
current_path: clinical-medicine/04-EVIDENCE-BASED-MEDICINE.md
canonical_path: clinical-medicine/04-EVIDENCE-BASED-MEDICINE.md
backsource_ids: [proof-backfill:clinical-medicine:04-evidence-based-medicine]
concepts: [evidence-based-medicine, pico, grade, number-needed-to-treat, external-validity, surrogate-endpoints]
root_concepts: [evidence-appraisal]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Evidence-Based Medicine — Appraising and Applying Population Evidence to One Patient

**This guide owns** the reasoning that connects *research evidence* to *a decision for one
person*: Sackett's three-circle definition, the **PICO** question, the **evidence
hierarchy** and its limits, **GRADE** (certainty of evidence vs strength of
recommendation), the absolute-vs-relative effect measures (**ARR / RRR / NNT / NNH**), the
transfer of population effects to an individual (**baseline-risk dependence, external
validity**), and the trap of **surrogate endpoints**. **It builds on**
`03-DIAGNOSTIC-TEST-INTERPRETATION` (the same decision-theoretic spine — effects only matter
if they cross a threshold) and feeds `05`, `06`, and `09` (which apply evidence to care,
multimorbidity, and screening). **It explicitly defers** the *mechanics of study design and
biostatistics* (randomization, meta-analysis math, confounding control) to `public-health/`
and `statistics-applied/`; the *drugs* to `pharmacology/`; and the *diseases* to `disease/`.
This is a guide to *how evidence is appraised and applied*, **not** a catalog of trials or a
recommendation to use any intervention.

> **This module is an educational reference about *how clinical medicine reasons and
> how care is organized* — the cognitive and system architecture of the discipline.
> It is *not* medical advice. It does not diagnose, does not give treatment, dosing,
> or procedure instructions, does not give emergency or first-aid instructions, and
> is *not a substitute* for evaluation by a licensed clinician. Worked cases are
> illustrative teaching vignettes showing *how a clinician thinks*, not what any
> reader should do. For personal concerns, appropriate care comes from qualified
> local professionals; emergencies are handled through local emergency services.**

*Per-guide banner: educational reference on appraising and applying evidence — not a
recommendation to use or avoid any intervention. Every numeric effect below is illustrative
and internally consistent; where a real study or framework is named, it is attributed and
dated.*

---

## The Big Picture: Evidence Is an Input to a Decision, Not the Decision

The novice model is "the trial said it works, so use it." The expert model treats a study
as **one input** — a population-average effect, of some certainty, on some outcome, in some
population — that must be *appraised* for trustworthiness and then *transported* to a
specific person whose baseline risk and values differ from the trial's. Evidence-based
medicine is the discipline of doing that transport honestly.

```
FROM STUDY TO DECISION  (this guide owns the whole transport)
==========================================================================
  [ ASK ]   frame an answerable question -- PICO (Section 1)
       |
       v
  [ ACQUIRE + APPRAISE ]  find evidence; rate it -- hierarchy + GRADE (Sections 2-3)
       |    certainty: High / Moderate / Low / Very Low
       v
  [ MEASURE THE EFFECT ]  absolute, not just relative -- ARR / RRR / NNT (Section 4)
       |    a relative effect without a baseline risk is uninterpretable
       v
  [ TRANSPORT TO THIS PATIENT ]  baseline risk + external validity (Section 5)
       |    the average effect is not this person's effect
       v
  [ CHECK THE OUTCOME IS REAL ]  surrogate vs patient-important (Section 6)
       |
       v
  [ INTEGRATE ]  evidence + clinical expertise + patient values (Sackett) -> a decision
==========================================================================
  A study yields a population-average effect of a stated certainty on a stated outcome.
  The decision requires all four qualifiers, plus this patient's risk and values.
```

**Sackett's definition (1996).** Evidence-based medicine is *"the conscientious, explicit,
and judicious use of current best evidence"* integrated with **clinical expertise** and
**patient values** — three circles, not one. Evidence alone never dictates a decision;
without expertise it is misapplied, and without the patient's values it is paternalistic.

```
  SACKETT'S THREE CIRCLES  (the decision lives in the overlap)
  ----------------------------------------------------------------
     [ BEST RESEARCH EVIDENCE ]      what the studies show, and how sure
              \                /
               \   DECISION   /       <- the individual choice lives here
                \            /
     [ CLINICAL EXPERTISE ]--[ PATIENT VALUES + CONTEXT ]
        judgment, skill,        what THIS person wants,
        this patient's data     tolerates, and can access
  ----------------------------------------------------------------
  "Evidence-based" never meant "evidence-dictated." Drop any circle and the decision breaks.
```

**Bridge (software).** This is a data-to-decision pipeline with provenance. PICO is a
well-formed query spec; the hierarchy is a trust/provenance rating on the data source; GRADE
separates *how sure we are of the number* from *how strongly we act on it* (test confidence
vs ship decision); absolute vs relative effect is the perennial "percent improvement over
what baseline?" trap; external validity is train/test distribution shift; and a surrogate
endpoint is a proxy metric that can decouple from the true objective (Goodhart's law).

---

## 1. PICO — Framing an Answerable Question

An unstructured clinical question ("what about this drug?") cannot be searched or answered.
**PICO** decomposes it into four slots, turning it into a specification:

| Slot | Meaning | Example (abstract) |
|---|---|---|
| **P** — Population | who: the patient/problem, described specifically | older adults with condition X and risk factor Y |
| **I** — Intervention | the action considered | strategy A |
| **C** — Comparison | the alternative (often "usual care" or "no treatment") | strategy B / placebo |
| **O** — Outcome | the *patient-important* result, and by when | a hard outcome at a stated horizon |

Variants add **T** (time horizon) or **S** (study design). The discipline of PICO is that it
forces the **comparison** and a **patient-important outcome** to be explicit — the two slots
lay questions omit, and the two that most often hide a weak claim (an intervention with no
stated comparator, or a study that measured a surrogate instead of the outcome the patient
cares about). PICO also *chooses the evidence type*: a therapy question wants a randomized
comparison; a prognosis question wants a cohort; a diagnosis question wants a cross-sectional
accuracy study against a reference standard (guide 03).

**Bridge (software).** PICO is a query with an explicit `WHERE` (population), the operation
under test, an explicit *baseline to diff against*, and the metric to compare on. A benchmark
that reports a number with no baseline and no defined workload is exactly the malformed
question PICO prevents.

---

## 2. The Evidence Hierarchy — Useful Heuristic, Not a Law

Evidence is conventionally ranked by how well a design controls bias *for a therapy
question*:

```
  EVIDENCE HIERARCHY  (risk-of-bias order, for THERAPY questions)
  ----------------------------------------------------------------
        systematic review / meta-analysis of RCTs     <- top (synthesizes RCTs)
        randomized controlled trial (RCT)              <- randomization balances confounders
        cohort study                                   <- observational, temporal
        case-control study                             <- observational, retrospective
        case series / case report                      <- no comparator
        mechanistic reasoning / expert opinion         <- bottom (unvalidated)
  ----------------------------------------------------------------
  Higher = better protection against CONFOUNDING for a "does it work?" question.
```

Three caveats keep the hierarchy from being misused:

- **The hierarchy is question-specific.** It ranks *internal validity for therapy*. For a
  **prognosis** question a cohort is the right top; for **harm** (rare, long-latency) a
  case-control or large observational database may be the only ethical/feasible design; for
  **diagnosis**, a cross-sectional accuracy study. "RCT or it doesn't count" is a category
  error for non-therapy questions.
- **A design is a ceiling, not a guarantee.** A biased, underpowered RCT can be worse than a
  large, well-conducted cohort. *Conduct* matters as much as *design* — which is exactly what
  GRADE formalizes (Section 3).
- **Randomization buys internal validity, sometimes at the cost of external validity.** The
  tight inclusion criteria that make an RCT clean also make its population unlike the average
  patient (Section 5).

The hierarchy is therefore a *prior* on trustworthiness, not a verdict — which is why modern
appraisal uses GRADE rather than reading rank off a pyramid.

---

## 3. GRADE — Certainty of Evidence vs Strength of Recommendation

**GRADE** (Grading of Recommendations Assessment, Development and Evaluation; Guyatt et al.,
*BMJ* 2008) is the dominant modern framework. Its central move is to **separate two things**
that the hierarchy conflates:

```
  GRADE SEPARATES TWO JUDGMENTS
  ----------------------------------------------------------------
  (A) CERTAINTY of evidence:  High / Moderate / Low / Very Low
         -> "how sure are we of the effect estimate?"
  (B) STRENGTH of recommendation:  Strong  vs  Weak/Conditional
         -> "how confidently should action follow?" -- depends on certainty PLUS
            the balance of benefits/harms, patient values, and resource use
  ----------------------------------------------------------------
  High certainty can still yield a WEAK recommendation (benefits ~ harms, or values vary);
  Low certainty can occasionally yield a STRONG one (e.g., obvious net benefit in a crisis).
  The two axes are INDEPENDENT -- this is the whole point.
```

**How certainty is rated.** GRADE *starts* RCT evidence at High and observational at Low,
then adjusts:

| Downgrade certainty for… | Upgrade (observational) for… |
|---|---|
| risk of bias (poor conduct) | large magnitude of effect |
| inconsistency (heterogeneous results) | dose–response gradient |
| indirectness (wrong population/comparison/outcome) | plausible confounding would *reduce* the observed effect |
| imprecision (wide confidence intervals) | |
| publication bias (missing negative studies) | |

**Why the separation matters clinically.** A **strong** recommendation is meant to apply to
almost everyone ("just do it" for most patients); a **weak/conditional** one signals that the
right choice *depends on values* and should be an explicit shared decision (guide 09/10).
Confusing "high certainty" with "strong recommendation" — acting forcefully on a
well-measured but marginal effect — is a common misread that GRADE exists to prevent.

**Bridge (software).** This is separating *confidence in a measurement* from *the decision to
ship*. A benchmark can be highly reproducible (tight CI, high certainty) and still not justify
a rollout if the effect is tiny or the cost/risk is high; conversely a noisy signal can
justify action when the downside of inaction is catastrophic. GRADE is that two-factor gate,
written for clinical actions.

---

## 4. Absolute vs Relative Effects — ARR, RRR, NNT

The single most consequential appraisal skill is refusing a **relative** effect without its
**absolute** counterpart. Define the control event rate (**CER**, baseline risk) and the
experimental event rate (**EER**):

```
  EFFECT MEASURES  (for a bad outcome that treatment REDUCES)
  ----------------------------------------------------------------
  Relative Risk         RR   = EER / CER
  Relative Risk Reduc.  RRR  = 1 - RR = (CER - EER)/CER      <- the "big-sounding" number
  Absolute Risk Reduc.  ARR  = CER - EER                     <- what actually changes
  Number Needed to Treat NNT = 1 / ARR                       <- patients treated per event prevented
  (for harms: ARI = increase in risk; NNH = 1/ARI)
  ----------------------------------------------------------------
  RRR hides the baseline; ARR and NNT expose it. The same RRR can be huge or trivial.
```

**Worked demonstration (illustrative).** Fix the treatment's **RRR at 25%** and vary only the
baseline risk:

| Setting | CER (baseline) | EER = CER×0.75 | ARR = CER−EER | NNT = 1/ARR |
|---|---|---|---|---|
| Higher-risk population | 20.0% | 15.0% | 5.0% | 20 |
| Lower-risk population | 2.0% | 1.5% | 0.5% | 200 |

The **relative** effect is identical (25% in both rows), yet one must treat **20** people to
prevent one event in the high-risk group and **200** in the low-risk group — a tenfold
difference driven entirely by baseline risk. Now add a treatment **harm** whose absolute rate
is roughly constant (a side effect, say ARI ≈ 1%, so **NNH ≈ 100**):

```
  NET-BENEFIT READING  (illustrative; benefit NNT vs harm NNH)
  ----------------------------------------------------------------
  High-risk:  NNT 20  vs  NNH 100  -> benefit reached ~5x more often than harm -> net favorable
  Low-risk:   NNT 200 vs  NNH 100  -> harm reached ~2x more often than benefit -> net unfavorable
  ----------------------------------------------------------------
  Same drug, same RRR. Whether the model favors it FLIPS with baseline risk, because the
  absolute benefit scales with baseline risk while the absolute harm does not.
```

This is why "targeting the high-risk" is a recurring theme (guides 03, 06, 09): a fixed
relative benefit becomes a large absolute benefit only where baseline risk is high, while
absolute harms are often risk-independent. A decision-quality appraisal always converts the
relative headline into an absolute ARR/NNT *at this patient's baseline risk*.

**Bridge (systems).** RRR is "50% faster"; ARR/NNT is "50% faster on a path that was 0.1% of
runtime." Optimizing a large relative gain on a tiny absolute base is the classic premature
optimization; the absolute measure is the amortized, workload-weighted number that actually
governs the decision.

---

## 5. Transporting the Effect — Baseline Risk and External Validity

A trial reports an **average treatment effect** in *its* population. Applying it to one person
requires two transports:

1. **Baseline-risk transport (quantitative).** As Section 4 showed, the absolute benefit is
   the RRR applied to *this patient's* baseline risk, which a risk model or the clinician's
   estimate supplies — not the trial's average baseline. A patient far from the trial's
   average risk gets a different NNT.
2. **External validity / generalizability (qualitative).** Does the effect even apply? Trials
   buy internal validity with **inclusion/exclusion criteria** that make their population
   *unrepresentative*: often younger, single-condition, higher-adherence, and historically
   skewed toward male and high-income populations (the "70-kg male" default). Key threats:

| Threat to external validity | Question it forces |
|---|---|
| **Population indirectness** | is this patient like the trial's patients (age, comorbidity, ancestry, sex)? |
| **Efficacy vs effectiveness** | trial conditions (ideal adherence, monitoring) vs real-world use |
| **Comparator indirectness** | was the trial's comparator the alternative this patient actually faces? |
| **Setting/resource indirectness** | does the trial's health system resemble this one (guide 08)? |
| **Effect modification** | is there a subgroup for whom the effect differs (real, pre-specified — not fishing)? |

The **explanatory–pragmatic** distinction (Schwartz & Lellouch, 1967; the PRECIS tool
formalizes it) names this directly: *explanatory* trials ask "*can* it work under ideal
conditions?" and maximize internal validity; *pragmatic* trials ask "*does* it work in usual
practice?" and maximize external validity. A clinician appraising evidence for a specific,
comorbid, real-world patient weights pragmatic evidence and external validity heavily — the
bias flagged in guide 00 that the evidence base under-represents exactly such patients.

**Bridge (ML).** This is distribution shift. A model with excellent held-out performance on a
curated benchmark (internal validity) can fail in production because the deployment
distribution differs (external validity). "It passed the benchmark" is efficacy; "it works on
live traffic" is effectiveness; and a pre-specified subgroup effect is a genuine
interaction, whereas a post-hoc subgroup is overfitting.

---

## 6. Surrogate Endpoints — Proxy Metrics That Can Decouple

A **surrogate endpoint** is an intermediate marker (a lab value, an image finding, a
physiologic measure) used *in place of* a patient-important outcome (survival, symptoms,
function, quality of life) because it is faster or cheaper to measure. Surrogates are
seductive and sometimes dangerous: an intervention can move the surrogate in the "right"
direction while leaving the true outcome unchanged — or worse.

```
  THE SURROGATE ASSUMPTION (and how it fails)
  ----------------------------------------------------------------
  intervention -> [ surrogate marker ] -> [ patient-important outcome ]
                        moves "good"           assumed to follow
  ----------------------------------------------------------------
  FAILS when the surrogate does not lie on the causal path to the outcome, or the
  intervention affects the outcome through OTHER paths (harms) the surrogate can't see.
  A surrogate is valid only if intervention effects on it RELIABLY predict effects on
  the real outcome (Prentice's criterion) -- a high bar most surrogates do not clear.
```

The canonical cautionary example is historical and dated: the **CAST** trial (Cardiac
Arrhythmia Suppression Trial, *NEJM* 1989/1991) tested drugs that successfully *suppressed a
surrogate* (post-infarction ventricular ectopy) on the assumption that fewer arrhythmias meant
fewer deaths — and found the drugs **increased** mortality. The surrogate improved while the
outcome that mattered got worse. The lesson is general: a decision resting on a surrogate is
resting on an *assumption of causal linkage* that must itself be validated, and PICO's
insistence on a *patient-important* outcome (Section 1) is the first line of defense.

**Bridge (systems).** A surrogate endpoint is a proxy metric, and this is **Goodhart's law**:
when a measure becomes a target, it can decouple from the goal it proxied. Optimizing a
green dashboard metric (a surrogate) while the user-facing objective degrades is the same
failure — the metric moved, the mission didn't.

---

## Fully Worked Case — Appraising and Transporting an Effect (illustrative, fictional)

All numbers are invented and internally consistent; nothing here recommends any
intervention. The specifics are abstract (drugs → `pharmacology/`, diseases → `disease/`).

**Step 1 — PICO (Section 1).** *P:* older adults with condition X; *I:* strategy A; *C:* usual
care; *O:* a hard patient-important outcome at a defined horizon (not a surrogate).

**Step 2 — appraise (Sections 2–3).** The best evidence is a well-conducted RCT plus a
systematic review. Under GRADE it starts High; the review is consistent and precise but the
trial population is younger and single-condition than the patient (**indirectness**), so
certainty is rated **Moderate**. Separately, because benefits and harms are close and depend
on patient values, the recommendation is **weak/conditional** — a shared decision, not a
directive.

**Step 3 — absolute effect at this patient's risk (Section 4).** The headline is *RRR 25%*.
The clinician estimates this patient's baseline risk. If the patient is high-risk (CER 20%),
ARR = 5%, **NNT = 20**; if low-risk (CER 2%), ARR = 0.5%, **NNT = 200**. Against a
roughly fixed harm (**NNH ≈ 100**), the model favors the strategy for the high-risk patient
and disfavors it for the low-risk one — the decision flips on baseline risk, not on the trial.

**Step 4 — external validity check (Section 5).** Because the trial excluded the patient's
comorbidities and skewed toward a different demographic, the clinician down-weights the
effect's transportability and foregrounds any pragmatic/effectiveness data — treating the
"70-kg male" trial population as a limit, not a stand-in for this patient.

**Step 5 — outcome check (Section 6).** The clinician confirms the trial's primary endpoint
was a *patient-important* outcome, not a surrogate; had it been a surrogate, the whole chain
would rest on an unvalidated causal assumption (the CAST lesson).

**Step 6 — integrate (Sackett).** Moderate-certainty, weak-recommendation evidence, an
absolute benefit that depends on baseline risk, external-validity caveats, and the patient's
own values combine into a **shared decision** — the three circles in the overlap, not evidence
dictating the choice.

---

## Reader Tasks (answerable from this guide)

1. **Frame a question as PICO.** Turn a vague query into P/I/C/O, and explain why the missing
   comparator and the patient-important outcome are the two slots that most often hide a weak
   claim. (Section 1.)
2. **Convert relative to absolute.** Given an RRR and two baseline risks, compute ARR and NNT
   for each and explain why the *same* relative effect yields very different absolute benefit.
   (Section 4.)
3. **Separate certainty from strength.** Given a scenario, explain how evidence can be
   high-certainty yet warrant only a weak/conditional recommendation, and vice versa, using
   GRADE's two axes. (Section 3.)
4. **Diagnose an external-validity gap.** Given a trial with narrow inclusion criteria and a
   dissimilar patient, name the indirectness threats and describe how they change the weight
   the evidence carries. (Section 5.)
5. **Catch a surrogate.** Given a study reporting improvement in an intermediate marker,
   explain why that does not establish benefit on a patient-important outcome and what
   validation (Prentice's criterion) would be required. (Section 6.)

---

## Decision Cheat Sheet

| Situation | What the appraisal does | Why (this guide) |
|---|---|---|
| A clinical question arises | frames it as **PICO** with an explicit comparator + hard outcome | unstructured questions can't be answered (§1) |
| A study is cited | reads its **design against the question type**, then its conduct | the hierarchy is a heuristic, not a verdict (§2) |
| Rating the evidence | applies **GRADE**: certainty (High…Very Low) *separate from* strength | confidence in the number ≠ how hard to act (§3) |
| Only a relative effect is given | demands **ARR and NNT at this patient's baseline risk** | RRR hides the baseline; absolute effect governs (§4) |
| Applying a trial to a person | transports the effect via **baseline risk + external validity** | the average effect is not this patient's effect (§5) |
| The endpoint is an intermediate marker | treats it as a **surrogate** needing causal validation | surrogates can decouple from real outcomes (§6) |
| Benefits ≈ harms or values vary | routes to a **shared decision** (weak recommendation) | Sackett's third circle; GRADE weak (§0, §3) |

---

## Common Confusion Points

**"Evidence-based means the evidence decides."** No — Sackett's definition is *three circles*:
best evidence, clinical expertise, and patient values. Evidence is an input; dropping expertise
misapplies it and dropping values makes it paternalistic. "Evidence-based" was never
"evidence-dictated."

**"An RCT always beats an observational study."** For a *therapy* question a well-conducted RCT
controls confounding better, but the hierarchy is question-specific (prognosis wants a cohort;
rare harms may need case-control), and a poorly conducted RCT can be worse than a strong cohort.
Design is a ceiling; conduct and applicability decide.

**"High-certainty evidence means a strong recommendation."** GRADE separates them on purpose.
High certainty about a *marginal* effect, or one whose value trade-off varies between patients,
yields a **weak/conditional** recommendation — an explicit shared decision, not a directive.

**"A 30% risk reduction is a big deal."** Only relative to a baseline. A 30% RRR on a 1%
baseline is a 0.3% absolute reduction (NNT ≈ 333); on a 30% baseline it is a 9% reduction (NNT
≈ 11). Always convert to ARR/NNT *at this patient's risk* before judging.

**"If the trial population is different, I can just scale the relative effect."** The *relative*
effect sometimes transports; whether it *applies at all* is the external-validity question, and
efficacy under trial conditions is not effectiveness in usual practice. The evidence base
under-represents older, comorbid, and non-majority populations, so transport is a caveat, not a
formality.

**"An improved marker proves the treatment works."** A surrogate endpoint only counts if effects
on it reliably predict effects on a patient-important outcome — a bar most surrogates fail (the
CAST lesson). Improving the proxy while the real outcome is unchanged, or worse, is Goodhart's
law in clinical form.
