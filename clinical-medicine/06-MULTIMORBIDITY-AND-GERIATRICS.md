---
maxim_schema: maxim.frontmatter.v1
id: maxim:clinical-medicine:multimorbidity-and-geriatrics
kind: guide
module: clinical-medicine
section: clinical-medicine
title: Multimorbidity and Geriatrics - Competing Risks, Treatment Burden, and Deprescribing Reasoning
status: source-custody
source_custody: partial
current_path: clinical-medicine/06-MULTIMORBIDITY-AND-GERIATRICS.md
canonical_path: clinical-medicine/06-MULTIMORBIDITY-AND-GERIATRICS.md
backsource_ids: [proof-backfill:clinical-medicine:06-multimorbidity-and-geriatrics]
concepts: [multimorbidity, competing-risks, treatment-burden, prescribing-cascade, deprescribing, time-to-benefit]
root_concepts: [care-architecture]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Multimorbidity and Geriatrics — Competing Risks, Treatment Burden, and Deprescribing Reasoning

**This guide owns** the reasoning that breaks when single-disease logic meets a person with
*many* conditions: **competing risks**, **guideline collision**, **treatment burden**,
**polypharmacy** and **prescribing cascades**, **deprescribing** reasoning, the geriatric
**5Ms**, **frailty**, and **time-to-benefit**. **It builds on** `04-EVIDENCE-BASED-MEDICINE`
(single-disease trials generalize poorly here — an external-validity problem) and
`05-ACUTE-AND-CHRONIC-CARE` (multimorbidity is many chronic loops interacting). **It
explicitly defers** *drug pharmacology* (classes, PK/PD, interactions) to `pharmacology/` and
*specific drugs* to `medicine/` — **no dosing, ever**; the *diseases* to `disease/`; and
*normal aging physiology* to `human-biology/`. This guide owns the **decision reasoning** of
prescribing, deprescribing, and prioritization in complexity — **not** a drug list, **not**
dosing, and **not** instructions to any reader to start, stop, or change a medication (those
are clinician-supervised decisions).

> **This module is an educational reference about *how clinical medicine reasons and
> how care is organized* — the cognitive and system architecture of the discipline.
> It is *not* medical advice. It does not diagnose, does not give treatment, dosing,
> or procedure instructions, does not give emergency or first-aid instructions, and
> is *not a substitute* for evaluation by a licensed clinician. Worked cases are
> illustrative teaching vignettes showing *how a clinician thinks*, not what any
> reader should do. For personal concerns, appropriate care comes from qualified
> local professionals; emergencies are handled through local emergency services.**

*Per-guide banner: educational reference on reasoning about multimorbidity, polypharmacy, and
deprescribing — **not** a prompt to change any medication and **not** dosing guidance. Named
tools (Beers, STOPP/START, 5Ms) are described as frameworks; any threshold is illustrative and
attributed.*

---

## The Big Picture: Single-Disease Logic Does Not Compose

The novice model treats a patient with five conditions as five separate problems, each managed
by its own guideline. The expert model recognizes that **the conditions and their treatments
interact**, that guidelines built on single-disease trials *do not compose*, and that in an
older, frailer patient the right objective is not "optimize each disease" but "align the whole
plan with what matters, the person's reserve, and the time they have."

```
WHY COMPLEXITY BREAKS SINGLE-DISEASE CARE  (this guide owns the reconciliation)
==========================================================================
  N single-disease guidelines applied independently
        |
        v
  [ GUIDELINE COLLISION ]  contradictory / additive recommendations (Section 2)
        |                    -> a huge regimen no one designed as a whole
        v
  [ POLYPHARMACY ]  many drugs -> interactions, adverse events, cascades (Section 4)
        |
        v
  [ TREATMENT BURDEN > CAPACITY ]  the workload of care exceeds the patient's capacity (Sec 3)
        |
        v
  RECONCILE against three constraints the single-disease view ignores:
     COMPETING RISKS (Section 1) + FRAILTY / reserve (Section 6) + TIME-TO-BENEFIT (Section 7)
        |
        v
  [ INDIVIDUALIZED PLAN ]  prioritized to "what matters most" -- 5Ms (Section 5),
                           with DEPRESCRIBING as a first-class move (Section 4)
==========================================================================
  The failure is COMPOSITION: locally-correct single-disease decisions sum to a
  globally-incoherent, over-burdensome plan. The fix is a global objective, not more guidelines.
```

**Bridge (software).** This is the failure of composing independently-optimized subsystems.
N linters, each locally correct, emit contradictory fixes with no global objective; dependencies
accrete into unmaintainable complexity; and the right move is often *deletion* (deprescribing =
refactoring / removing harmful code) guided by a global goal, not another feature. Competing
risks are a preemptive deadline (one failure mode decommissions the system before another
matters); time-to-benefit is payback period; frailty is a system running with no headroom.

---

## 1. Competing Risks — One Outcome Can Preempt Another

**Competing risks** arise when a person faces several possible outcomes that are not
independent: experiencing one (say, death from condition A) *removes the opportunity* to
experience another (a slow complication of condition B). This has a sharp consequence for
preventive treatment: **an intervention that prevents a distant outcome delivers little benefit
to a patient who is likely to reach a different endpoint first.**

```
  COMPETING RISKS  (outcomes compete for the same patient)
  ----------------------------------------------------------------
   patient --+--> outcome A (near-term, high probability)  --- preempts --->
             |                                                            |
             +--> outcome B (distant; the target of a preventive)  <------+
  ----------------------------------------------------------------
  If A is likely to arrive first, preventing B buys little: the benefit of the preventive
  is CONDITIONAL on surviving long enough (and well enough) to reach B. Competing mortality
  shrinks the absolute benefit (guide 04) of long-horizon interventions toward zero.
```

The link to guide 04 is exact: the *absolute* benefit of a preventive is its relative effect
applied to the patient's baseline risk **of actually reaching that outcome** — and competing
risks lower that reaching-probability. So the same intervention that is clearly worthwhile in a
robust patient can be near-worthless in one whose competing risks make the target outcome
unlikely to occur in their remaining time. This is not nihilism; it is the honest arithmetic of
benefit, and it is why "treat the number" (a lab target) can diverge from "help the patient."

**Bridge (systems).** Optimizing a long-horizon reliability fix on a service already scheduled
for decommission (a different failure mode arriving first) is negative-value work. The
competing deadline dominates the payoff calculation.

---

## 2. Guideline Collision — Why Guidelines Do Not Compose

Clinical guidelines are almost all **single-disease**: built from trials that *excluded*
multimorbid, older, frail patients (the external-validity skew of guide 04). Applying several of
them to one complex patient produces a regimen no clinician would design as a whole. The classic
demonstration is Boyd et al. (*JAMA*, 2005): applying all relevant single-disease guidelines to a
*hypothetical* older woman with several common conditions generated a large daily medication
count, a dense self-care schedule, and internal contradictions — an object lesson, not a
recommendation.

```
  GUIDELINE COLLISION
  ----------------------------------------------------------------
  guideline(condition 1) -> add drugs, targets, monitoring
  guideline(condition 2) -> add drugs, targets, monitoring
     ...                                                     -> SUM:
  guideline(condition N) -> add drugs, targets, monitoring      contradictions
                                                                + huge burden (Section 3)
  ----------------------------------------------------------------
  Each guideline is locally valid and was tested WITHOUT the others present. Composition
  was never tested. The interactions (drug-drug, drug-disease, recommendation-recommendation)
  are exactly what the single-disease evidence base does not cover.
```

Three collision types:

| Collision | What conflicts | Example (abstract) |
|---|---|---|
| **Drug–drug** | two agents interact | one guideline's drug amplifies/blocks another's |
| **Drug–disease** | a drug for A worsens B | an agent helpful for one condition is risky in another |
| **Recommendation–recommendation** | targets or actions contradict | one says "intensify," another's risk profile says "relax" |

The resolution is *not* a bigger guideline; it is a **global objective** — the patient's
priorities (Section 5) — against which the colliding recommendations are pruned. Guidelines
themselves increasingly say this: many now carry an explicit caveat that they may not apply to
patients with significant multimorbidity or limited life expectancy.

---

## 3. Treatment Burden vs Capacity

**Treatment burden** is the *work of being a patient*: appointments, medications, monitoring,
lifestyle demands, coordination, and the cognitive load of managing it all. It is distinct from
*disease burden* (how much the illness itself weighs) and it accumulates as conditions and
guidelines stack. The **minimally disruptive medicine** frame (May, Montori, and colleagues,
c. 2009) models care as an interaction between a patient's *workload* and their *capacity* to do
that work — where capacity is itself reduced by illness, frailty, cognitive limits, and social
circumstance.

```
  BURDEN vs CAPACITY  (care fails when workload exceeds capacity)
  ----------------------------------------------------------------
   WORKLOAD (of care)        CAPACITY (to do the work)
     appointments               physical + cognitive reserve
     medications + schedules    time, money, social support
     monitoring + self-care     health literacy, access (guide 08)
     coordination across N svcs  competing life demands
  ----------------------------------------------------------------
  When WORKLOAD > CAPACITY -> nonadherence, missed care, exhaustion, worse outcomes.
  Adding "one more correct thing" to an over-capacity patient can make outcomes WORSE.
```

The architectural insight is that **adherence failure is often a design failure**: a plan whose
workload exceeds the patient's capacity will fail no matter how evidence-based each element is.
So burden is a first-class constraint in the objective, not an afterthought — and reducing burden
(fewer drugs, simpler schedules, consolidated visits) can improve outcomes even when it removes
"indicated" care.

**Bridge (systems).** This is operational toil and cognitive load on the on-call human. A
runbook that is individually correct at every step but exceeds the operator's capacity produces
errors and burnout; the fix is to *reduce* the load, not to exhort more diligence.

---

## 4. Polypharmacy, Prescribing Cascades, and Deprescribing

**Polypharmacy** — the use of many concurrent medications — is a *risk marker*, not a diagnosis:
as counts rise, so do drug–drug and drug–disease interactions, adverse drug events, adherence
difficulty, and cost. Some patients genuinely need many drugs; the point is that each addition
carries compounding risk that the single-disease view underweights.

A **prescribing cascade** (Rochon & Gurwitz, *BMJ*, 1997) is the characteristic failure loop: a
drug's *adverse effect* is misread as a *new medical condition* and treated with *another drug*,
whose adverse effect may in turn be treated with a third.

```
  THE PRESCRIBING CASCADE  (a feedback loop that accretes drugs)
  ----------------------------------------------------------------
   drug 1 --> adverse effect --> misinterpreted as a NEW condition
                                          |
                                          v
                              drug 2 added to "treat" it
                                          |
                                          v
                        drug 2's adverse effect --> misread again --> drug 3 ...
  ----------------------------------------------------------------
  Each step is locally rational (a symptom, a treatment) but the ROOT is an unrecognized
  drug effect. Breaking the cascade requires asking "is this new problem actually a drug
  effect?" -- a diagnostic move (guide 02) applied to the medication list itself.
```

**Deprescribing** is the deliberate, supervised process of **reducing or stopping** medications
whose harms or burden now outweigh their benefit for *this* patient's goals. It is a first-class
clinical action, not "giving up," and it has its own reasoning:

```
  DEPRESCRIBING REASONING  (a structured refactor of the regimen)
  ----------------------------------------------------------------
  for each medication, a clinician weighs:
     - is there still a valid INDICATION for THIS patient's goals? (Section 5)
     - does the benefit's TIME-TO-BENEFIT fit remaining life expectancy? (Section 7)
     - is it (or its cascade) causing HARM or BURDEN now? (Sections 3-4)
     - what is the risk of STOPPING (withdrawal, rebound), and how is it monitored?
     - does the patient PREFER to continue or simplify? (shared decision, guides 09-10)
  ----------------------------------------------------------------
  Named tools flag candidates: Beers Criteria (AGS), STOPP/START. This guide names them as
  frameworks -- it does not reproduce their lists, which are dated, versioned, and clinical.
```

Deprescribing is **not** abrupt cessation and is **not** a reader action: some medications
require monitored tapering, and the decision is individualized and clinician-supervised. This
guide owns the *reasoning* — indication, time-to-benefit, harm/burden, stopping risk,
preference — never a directive to any reader to stop a drug.

**Bridge (software).** A prescribing cascade is a workaround stacked on a workaround: a hack to
fix a bug that another hack caused, with the root cause never diagnosed. Deprescribing is
refactoring and dead-code removal, governed by **Chesterton's fence** — understand *why* each
medication was added before removing it, because some are load-bearing.

---

## 5. The Geriatric 5Ms — A Prioritization Frame

The **5Ms** (a framework promoted by the American and Canadian Geriatrics Societies, c. 2017;
Tinetti, Molnar, and colleagues) organize geriatric care around what actually drives outcomes in
older adults, and — crucially — put the patient's priorities at the center as the *global
objective* the earlier sections needed.

| M | Domain | What it anchors |
|---|---|---|
| **Mind** | cognition, mood, delirium risk, capacity | affects every decision and consent (guide 10) |
| **Mobility** | gait, balance, falls, function | function is often the outcome that matters most |
| **Medications** | polypharmacy, appropriateness, deprescribing | Sections 3–4; the regimen as a whole |
| **Multicomplexity** | multimorbidity + social/contextual complexity | Sections 1–2; the composition problem |
| **what Matters most** | the patient's own goals, values, priorities | the **global objective** that prunes collisions |

```
  THE 5Ms PUT "WHAT MATTERS MOST" AT THE CENTER
  ----------------------------------------------------------------
        Mind ----\                    /---- Mobility
                  \                  /
                   > what MATTERS most <     <- the objective function
                  /                  \
     Medications /                    \ Multicomplexity
  ----------------------------------------------------------------
  The other four Ms are managed IN SERVICE of "what matters most" -- which is what turns a
  colliding pile of single-disease guidelines into a coherent, prioritized plan.
```

The 5Ms are the answer to "reconcile against what?" from Section 2: the global objective is not a
lab target but the patient's own priorities, with the other domains (mind, mobility, medications,
multicomplexity) managed to serve it. This is where guide 06 hands off to shared decision-making
(guide 09) and to consent/capacity and goals-of-care (guide 10).

---

## 6. Frailty — Reduced Reserve, No Headroom

**Frailty** is a state of **diminished physiologic reserve** across multiple systems, producing
disproportionate vulnerability to stressors: a minor insult that a robust person shrugs off can
trigger a cascade of decline in a frail one. It is distinct from age, from disability, and from
any single disease. Two complementary models are standard:

| Model | Idea | Attribution |
|---|---|---|
| **Phenotype** | frailty as a syndrome: weight loss, exhaustion, weakness, slow gait, low activity (≥3 defines it) | Fried et al., 2001 |
| **Cumulative deficit** | frailty as the *count/proportion* of accumulated deficits (a frailty index); more deficits = frailer | Rockwood & Mitnitski, 2005; Clinical Frailty Scale |

```
  RESERVE AND STRESSORS  (why frailty changes every decision)
  ----------------------------------------------------------------
   ROBUST:   [ large reserve ]  --stressor-->  dips, recovers to baseline
   FRAIL:    [ little reserve ]  --stressor-->  dips, RECOVERS PARTIALLY, drifts down
  ----------------------------------------------------------------
  Frailty = a system at capacity with no slack. Interventions that a robust patient tolerates
  (a burdensome regimen, an aggressive target, a procedure) can push a frail patient past the
  edge -- so intensity must be matched to reserve, not to the guideline default.
```

Frailty reframes the benefit/harm balance of everything else: it raises the harm side of
aggressive treatment, shortens the horizon over which benefits can accrue (Section 7), and often
makes *function and burden* the outcomes that matter more than a disease number. Assessing frailty
is a clinician's task; this guide owns why it changes the reasoning, not how to score it.

**Bridge (systems).** Frailty is a system running near 100% utilization with no headroom: latency
is fine until the smallest perturbation, then it collapses because there is no slack to absorb the
shock. You provision such a system conservatively and avoid changes that consume its last margin.

---

## 7. Time-to-Benefit — Does the Payoff Arrive in Time?

**Time-to-benefit (TTB)** is the lag between starting an intervention and when its benefit
actually materializes. Many *preventive* interventions have a long TTB: the harm they prevent is
years away, so the survival curves separate only after a delay. The decision rule follows
immediately: **a preventive with a TTB longer than a patient's remaining life expectancy (or
their competing-risk horizon) offers benefit that will never be realized — while its harms and
burden are immediate.**

```
  TIME-TO-BENEFIT vs REMAINING HORIZON
  ----------------------------------------------------------------
   harms + burden:  |###| start immediately (front-loaded)
   benefit:               ............<TTB>............| begins here
  ----------------------------------------------------------------
  If remaining life expectancy (or competing-risk horizon, Section 1) < TTB:
     the patient bears the immediate harm/burden but does not live to collect the benefit.
  If remaining horizon >> TTB and the patient is robust (Section 6):
     the preventive can be strongly net-beneficial.
  ----------------------------------------------------------------
  TTB is a PAYBACK PERIOD. A long-payback investment on a short-remaining-horizon asset is
  negative value -- the same logic as competing risks and absolute benefit (guide 04).
```

TTB ties the guide together: it is competing risks (Section 1) and absolute benefit (guide 04) on
a time axis. It explains why *de-intensifying* certain long-horizon preventive targets in frail,
limited-life-expectancy patients is not under-treatment but *correct* individualization — and why
the same intervention is right for a robust patient with a long horizon. Estimates of TTB for
specific interventions are evidence content (guide 04, `public-health/`); this guide owns the
*reasoning move* of comparing TTB against the patient's horizon and goals.

---

## Fully Worked Case — Reconciling a Colliding, Over-Burdened Plan (illustrative, fictional)

All details are invented to show the *reasoning*; nothing here recommends starting, stopping, or
changing any medication (those are clinician-supervised). Specifics are abstract (`pharmacology/`,
`disease/`).

**Setup.** A fictional frail older adult, **W**, carries several chronic conditions, a long
medication list, and — per the phenotype and cumulative-deficit models (Section 6) — clear
frailty with little reserve. W's stated priority (the 5Ms' "what matters most," Section 5) is
*staying independent at home with minimal daily hassle*, not maximizing any single disease number.

**Step 1 — spot the collision (Section 2).** Applying each condition's single-disease guideline
independently yields contradictory targets and an additive regimen no one designed as a whole —
the Boyd 2005 pattern. This is treated as a *composition failure*, not a set of separate problems.

**Step 2 — measure the burden (Section 3).** The plan's workload (many drugs, several monitoring
tasks, multiple appointments) is weighed against W's capacity. It exceeds capacity — so "adding
one more indicated thing" would likely *reduce* real outcomes through nonadherence and exhaustion.

**Step 3 — find a cascade (Section 4).** A newer symptom on the list is re-examined with a
diagnostic eye (guide 02) and recognized as a *plausible adverse effect of an existing
medication* rather than a new disease — a prescribing cascade. The reasoning move is to treat the
medication list itself as a differential.

**Step 4 — apply competing risks + time-to-benefit (Sections 1, 7).** For a long-horizon
preventive on the list, the clinician compares its time-to-benefit against W's remaining horizon,
shortened by competing risks and frailty. The benefit would arrive after W's likely horizon, while
its burden is immediate — so its net value for W is low.

**Step 5 — reason about deprescribing against goals (Sections 4–5).** For each candidate, the
clinician weighs indication-for-W's-goals, time-to-benefit vs horizon, current harm/burden,
stopping risk (with monitored tapering where needed), and W's preference. Named tools (Beers,
STOPP/START) flag candidates; the *decision* is individualized to "what matters most." The output
is a **simplified, prioritized plan** aligned to independence-with-minimal-hassle — with any
change made under clinical supervision, never as a reader action.

**What the case shows.** The single-disease pile was reconciled against a global objective
(the 5Ms' "what matters most"), constrained by competing risks, frailty, treatment burden, and
time-to-benefit, with deprescribing as a first-class move — the reasoning this guide owns, and
nothing a reader should enact on their own medications.

---

## Reader Tasks (answerable from this guide)

1. **Explain why guidelines don't compose.** Given a multimorbid patient, describe how applying N
   single-disease guidelines produces collision, and why the single-disease evidence base (guide
   04) is the root cause. (Section 2.)
2. **Apply competing risks and time-to-benefit.** Given a long-horizon preventive and a patient
   with high near-term competing risk, explain why the absolute benefit shrinks and how TTB vs
   remaining horizon governs the decision. (Sections 1, 7.)
3. **Trace and break a prescribing cascade.** Given a sequence where a symptom is treated with a
   new drug, identify where an adverse effect was misread as a new condition and the diagnostic
   move that breaks the loop. (Section 4.)
4. **Reason about a deprescribing candidate.** Given a medication, lay out the five factors a
   clinician weighs (indication, TTB, harm/burden, stopping risk, preference) — and state why this
   is not a reader instruction to stop anything. (Section 4.)
5. **Use the 5Ms to prioritize.** Given a colliding plan, show how "what matters most" becomes the
   global objective that prunes the collision, and how frailty and burden reshape the balance.
   (Sections 3, 5, 6.)

---

## Decision Cheat Sheet

| Situation | What the reasoning does | Why (this guide) |
|---|---|---|
| Several single-disease guidelines at once | expects **collision**; reconciles against a global goal | guidelines were tested singly, not composed (§2) |
| A long-horizon preventive in a limited horizon | compares **time-to-benefit** vs remaining/competing-risk horizon | front-loaded harm, deferred benefit (§1, §7) |
| A growing medication list | treats **polypharmacy** as a compounding risk marker | interactions/burden scale with count (§4) |
| A "new condition" appears on treatment | asks whether it is a **prescribing cascade** | drug effects masquerade as new disease (§4) |
| Harms/burden may exceed benefit | reasons about **deprescribing** (supervised, individualized) | removing harmful care can improve outcomes (§4) |
| An over-complex older patient | organizes with the **5Ms**, centered on "what matters most" | a global objective prunes the collision (§5) |
| Low physiologic reserve | matches intensity to **frailty**, not the guideline default | frail systems have no headroom (§6) |
| A plan the patient can't sustain | reduces **treatment burden** toward capacity | adherence failure is often design failure (§3) |

---

## Common Confusion Points

**"More conditions just means more treatments."** No — treatments *interact*, and single-disease
guidelines do not compose. Stacking them produces contradictions and a burden that can make
outcomes worse. Complexity needs a *global objective* (the 5Ms' "what matters most"), not more
independent recommendations.

**"Polypharmacy is always bad."** Polypharmacy is a *risk marker*, not a verdict; some patients
genuinely need many drugs. The concern is compounding interaction/burden risk and unrecognized
*prescribing cascades* — which is why the medication list is periodically re-examined as if it
were a differential.

**"Deprescribing means giving up, or is something a patient can just do."** Neither. Deprescribing
is a deliberate, evidence-informed, **clinician-supervised** optimization — some drugs need
monitored tapering, and some are load-bearing (Chesterton's fence). This guide describes the
*reasoning*; it never instructs a reader to stop a medication.

**"If a preventive is evidence-based, an older patient should get it."** Only if the benefit can
be *realized*. Long time-to-benefit against a short remaining or competing-risk horizon means the
patient bears immediate harm/burden for a benefit they may not live to collect — so
de-intensification can be correct individualization, not under-treatment.

**"Frailty is just old age or disability."** No — frailty is reduced *physiologic reserve* across
systems, a distinct state that changes the harm/benefit of every intervention. A robust
90-year-old and a frail 70-year-old warrant different intensity; the reserve, not the birthday,
drives the reasoning.
