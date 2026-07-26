---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "09-PREVENTION-AND-SCREENING.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:clinical-medicine:prevention-and-screening
kind: guide
module: clinical-medicine
section: clinical-medicine
title: Prevention and Screening - Individual Shared Decisions, Biases, and Harms
status: source-custody
source_custody: partial
current_path: clinical-medicine/09-PREVENTION-AND-SCREENING.md
canonical_path: clinical-medicine/09-PREVENTION-AND-SCREENING.md
backsource_ids: [mdloom-backfill:clinical-medicine:09-prevention-and-screening]
concepts: [prevention, screening, overdiagnosis, lead-time-bias, length-time-bias, natural-frequencies, shared-decision-making]
root_concepts: [care-architecture]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Prevention and Screening — Individual Shared Decisions, Biases, and Harms

**This guide owns** the *individual-level* reasoning of prevention and screening: the levels of
prevention, screening as **guide 03's testing logic applied to a low-prevalence, asymptomatic
population**, the specific **harms** (false positives, **overdiagnosis**, overtreatment,
labeling, false reassurance), the two statistical illusions that make screening look better than
it is (**lead-time** and **length-time** bias), **natural-frequency** risk communication, and
the **three-talk** model of shared decision-making. **It builds on** `03-DIAGNOSTIC-TEST-INTERPRETATION`
(the screening paradox, PPV at low prevalence) and `04-EVIDENCE-BASED-MEDICINE` (absolute benefit,
the right endpoint). **It explicitly defers** *population screening programs, policy, and the
epidemiology of program design* to `public-health/`; the *diseases* to `disease/`; and the *tests*
to `medicine/10`. This is a guide to *how an individual screening decision is reasoned as a shared
decision*, **not** a schedule of who should be screened when — it contains **no personal screening
advice**, and every real-world threshold it mentions is attributed, dated, and illustrative.

> **This module is an educational reference about *how clinical medicine reasons and
> how care is organized* — the cognitive and system architecture of the discipline.
> It is *not* medical advice. It does not diagnose, does not give treatment, dosing,
> or procedure instructions, does not give emergency or first-aid instructions, and
> is *not a substitute* for evaluation by a licensed clinician. Worked cases are
> illustrative teaching vignettes showing *how a clinician thinks*, not what any
> reader should do. For personal concerns, appropriate care comes from qualified
> local professionals; emergencies are handled through local emergency services.**

*Per-guide banner: educational reference on how screening decisions are reasoned — **not** a
recommendation to obtain or forgo any screening test, and **not** a screening schedule. Every
age, interval, or threshold is illustrative and attributed to a named body with a date; such
guidance changes over time and differs by country and body.*

---

## The Big Picture: Screening Is Testing the Well — and the Math Is Unforgiving

The novice model is "screening finds disease early, so more is better." The expert model is
sober: screening runs a test on **asymptomatic people at low prevalence**, where guide 03's
arithmetic guarantees a large false-positive share; it can **overdiagnose** disease that would
never have harmed anyone; and its apparent benefits are inflated by two statistical illusions.
So a screening decision is a genuine **weighing of small absolute benefit against common harms**,
best made as a **shared decision** — not a reflex.

```
WHY SCREENING IS HARD  (this guide owns the individual decision, not the program)
==========================================================================
  SCREEN an asymptomatic person (low pretest probability)
        |
        v
  [ guide 03 arithmetic ]  low prevalence -> low PPV -> many FALSE POSITIVES
        |                    -> confirmatory testing, anxiety, cascades
        v
  [ OVERDIAGNOSIS ]  detect real-but-harmless disease that never would have surfaced
        |             -> overtreatment of something that would never have hurt them
        v
  [ TWO ILLUSIONS ]  survival LOOKS better even if nothing changed:
        |             LEAD-TIME bias + LENGTH-TIME bias (Section 4)
        v
  [ WEIGH ]  small absolute benefit (disease-specific mortality) vs common harms
        |     communicate with NATURAL FREQUENCIES (Section 5)
        v
  [ SHARED DECISION ]  three-talk model (Section 6); the "right" answer depends on values
==========================================================================
  Screening is not free early detection; it is a test on the well whose benefits are small,
  harms are real and common, and apparent gains are partly statistical artifact.
```

**Bridge (software / ML).** Screening is deploying a classifier on a rare-event production stream:
precision collapses (guide 03), and you get a flood of false alarms. Overdiagnosis is alerting on
"defects" that would never have caused a failure. Lead-time bias is starting the clock earlier and
calling the longer interval an improvement. Length-time bias is a sampler that oversamples
slow-moving items. And presenting risk as natural frequencies instead of conditional probabilities
is the same fix as showing absolute counts instead of relative percentages.

---

## 1. Levels of Prevention — Where Screening Sits

Prevention is classically layered by *when* it acts relative to disease. The **conventional
public-health taxonomy has three levels** — primary, secondary, and tertiary (the Leavell & Clark
framing that `public-health/` owns at population scale); **quaternary prevention is a later
addition proposed by Marc Jamoulle**. The four-level table below is therefore an *extension* of
the standard three-level model, not a universally settled taxonomy:

| Level | Acts… | Example type (abstract) | This module owns |
|---|---|---|---|
| **Primary** | before disease onset | risk-factor reduction, immunization *concept* | the individual decision to pursue it |
| **Secondary** | early, presymptomatic | **screening** — detect before symptoms | the individual screening decision (this guide) |
| **Tertiary** | after disease, limit impact | rehabilitation, complication prevention | reasoning about its value for this patient |
| **Quaternary** | protect from *overmedicalization* | avoiding overdiagnosis/overtreatment | the harms lens of this whole guide |

**Quaternary prevention** — Jamoulle's extension beyond the conventional three levels — is the
framing most relevant here: protecting
patients from the *harms of medicine itself* — the overtesting cascades of guide 03, the
overdiagnosis of Section 3, and the overtreatment they trigger. Screening lives at the secondary
level but is the activity where quaternary concerns bite hardest, because it acts on the well.

The population-scale versions of all four levels — vaccination *programs*, organized screening
*programs*, policy — belong to `public-health/`. This module owns only the **individual decision**:
whether, for *this* person and *their* values, a preventive action's small expected benefit is
worth its harms.

---

## 2. Screening Is Guide 03 at Low Prevalence

Screening is not a special kind of test; it is the **testing logic of guide 03 applied to a
low-prevalence, asymptomatic population**, and everything that follows is a consequence of that
low prior.

```
  THE SCREENING PARADOX (from guide 03) IN SITU
  ----------------------------------------------------------------
   asymptomatic population  -> LOW prevalence  -> LOW pretest probability
        |
        v
   even an EXCELLENT test (high Sn, high Sp) yields LOW PPV:
        most positives are FALSE at low prevalence (guide 03, Section 3)
        |
        v
   a positive screen is a PROMPT for confirmation, not a diagnosis
        confirmatory serial testing (guide 03, Section 6) rescues PPV -- at a cost
  ----------------------------------------------------------------
  The same instrument that is decision-useful in a symptomatic clinic can be mostly false
  positives in a screening population, purely because the prior moved (guide 03's transport limit).
```

Two consequences carry straight over from guide 03:

- **Value of information still governs.** A screen is worth doing only if a result can cross a
  decision threshold *and* the expected benefit exceeds the harms of the cascade it launches. A
  screen whose positive leads to the same action regardless has zero value of information.
- **Targeting by baseline risk matters (guide 04).** Because absolute benefit is the relative
  effect applied to baseline risk, screening tends to be most favorable in *higher-risk*
  subgroups and least favorable (most harm-dominated) in the low-risk worried-well — the reason
  risk-stratified screening is a recurring design theme.

So a screening decision inherits the full apparatus of guides 03 and 04; Sections 3–4 add the
harms and illusions that are *specific* to detecting disease early in the asymptomatic.

---

## 3. The Harms — Especially Overdiagnosis

Screening harms are not hypothetical; they are the *common* outcomes, while the benefit is rare.

| Harm | What it is | Root |
|---|---|---|
| **False positive** | a positive in someone without the disease | low PPV at low prevalence (guide 03) |
| **Cascade** | confirmatory tests, procedures, their complications | the false positive is a branch, not an endpoint (guide 03 §7) |
| **Overdiagnosis** | detecting *real* disease that would never have caused harm | the reservoir of indolent disease (below) |
| **Overtreatment** | treating overdiagnosed disease | you cannot tell which case was harmless |
| **Psychological / labeling** | anxiety, the "patient" identity, insurance effects | being made a patient by a test |
| **False reassurance** | a false negative delays a real presentation | imperfect sensitivity |

**Overdiagnosis is the subtle, central harm, and it is *not* a false positive.** In a false
positive the disease is absent. In overdiagnosis the disease is **truly present by pathology** but
would **never have progressed** to cause symptoms or death in the person's lifetime — because it is
indolent, or because the person dies of something else first (competing risks, guide 06). Since one
cannot tell at detection which case is the harmless one, overdiagnosis leads to overtreatment of
disease that never needed treating.

```
  OVERDIAGNOSIS  (real disease, but harmless -- distinct from a false positive)
  ----------------------------------------------------------------
   the "reservoir" of indolent disease present in the well population:
      fast, progressive  ---> would surface + harm  (benefits from early detection)
      slow / non-progressive ---> would NEVER surface  (overdiagnosis if detected)
      dies of other cause first ---> would never have mattered (competing risks, guide 06)
  ----------------------------------------------------------------
  Screening samples this reservoir and CANNOT distinguish, at detection, the deadly from the
  harmless -- so it necessarily overdiagnoses some. The harder you look, the more you find,
  and the larger the harmless fraction.
```

**Bridge (systems).** Overdiagnosis is alerting on anomalies that would never have caused an
incident: a monitor tuned so sensitively that it flags benign, self-resolving conditions, generating
work and "fixes" for problems that were never going to page. Turning up detection sensitivity finds
more of everything — including more that never mattered.

---

## 4. Two Illusions — Lead-Time and Length-Time Bias

Screening's apparent benefit is systematically **overstated** by two biases that inflate
*survival-from-diagnosis* without anyone actually living longer. This is why survival statistics are
the wrong endpoint for screening, and why only **disease-specific mortality in a randomized
comparison** answers "does screening help?"

**Lead-time bias.** Screening advances the *date of diagnosis*. If the date of death is unchanged,
the measured "survival from diagnosis" grows purely because the clock started earlier — a
measurement artifact, not a benefit.

```
  LEAD-TIME BIAS  (earlier diagnosis, same death -> longer "survival" by artifact)
  ----------------------------------------------------------------
   NO SCREEN:   onset........[symptoms/dx]============[death]     survival = the ==== part
   SCREEN:      onset..[screen dx]==================[death]       survival = the longer ==== part
                        ^ lead time ^
  ----------------------------------------------------------------
  Death occurs at the SAME time in both rows. "Survival from diagnosis" is longer only because
  the SCREEN started the clock earlier. Nobody lived longer; the metric moved.
```

**Length-time bias.** Screening at intervals preferentially catches *slow-growing* disease, because
slow disease spends more time in the detectable-but-asymptomatic window and is therefore more likely
to be caught by a periodic screen. Fast, aggressive disease often surfaces *between* screens. So the
screened cases are enriched for indolent disease and look more survivable — a *sampling* bias.
Overdiagnosis is the limiting case: disease so slow it never would have surfaced at all.

```
  LENGTH-TIME BIAS  (periodic screening oversamples SLOW disease)
  ----------------------------------------------------------------
   fast disease:  short detectable window  |--|      often surfaces BETWEEN screens (missed)
   slow disease:  long detectable window   |----------|  likely CAUGHT by a periodic screen
   screen times:      X        X        X        X
  ----------------------------------------------------------------
  Screen-detected cases are enriched for SLOW (more survivable) disease -> screened cohort
  looks better even with no change in biology. Overdiagnosis = the extreme (never surfaces).
```

The combined effect: 5-year-survival and case-fatality among *screen-detected* patients look
impressive even when screening changed nothing, because both illusions inflate them. The honest
endpoint is a randomized comparison of **disease-specific mortality** (and, for net effect,
all-cause mortality and harms) between screened and unscreened groups — the guide 04 discipline of
choosing a patient-important outcome and avoiding artifacts.

**Bridge (systems).** Lead-time bias is measuring "time since we started watching" instead of "time
to failure" — detect earlier and the interval looks longer though the failure lands at the same
wall-clock moment. Length-time bias is a periodic sampler that systematically oversamples
long-lived processes; the sample looks healthier than the population.

---

## 5. Natural Frequencies — Communicating the Real Numbers

Even a correctly reasoned screening balance is useless if it cannot be understood, and probabilities
and relative risks are systematically *misunderstood* — by patients and clinicians alike.
**Natural frequencies** (Gigerenzer and colleagues) present risk as **counts out of a fixed
population** rather than conditional probabilities or relative changes, and they measurably improve
comprehension and calibrate expectations.

```
  NATURAL FREQUENCIES  (illustrative counts -- NOT any real program's numbers)
  ----------------------------------------------------------------
   Imagine 1,000 similar people screened over a defined period (invented figures):
      - a small number have their outcome improved by early detection      ~ 1-2
      - many receive a FALSE POSITIVE and further testing               ~ 100
      - some are OVERDIAGNOSED and treated for harmless disease           ~ a few
      - most gain no benefit (they were never going to have the event)   the rest
  ----------------------------------------------------------------
  These numbers are ILLUSTRATIVE placeholders to show the SHAPE (small benefit, common harms),
  not a claim about any specific test or program. Real figures are attributed, dated, and vary
  by test, population, and country -- and live in guide 04 / public-health/, not here.
```

Two communication rules follow:

- **Absolute, not relative.** "Reduces the chance of dying from the disease from about 5 in 1,000
  to about 4 in 1,000" is honest; "cuts deaths by 20%" hides the base rate (the RRR-vs-ARR trap,
  guide 04). Both describe the *same* effect; only the first supports a real decision.
- **Both arms, same denominator.** Benefits *and* harms are shown per the same 1,000, so the
  small benefit is seen next to the common false positives and overdiagnoses — the whole balance,
  not a benefit headline.

**Bridge (systems).** This is the same lesson as guide 04's absolute-effect rule and dashboard
design: show absolute counts against a fixed denominator, present both wins and costs on one screen,
and avoid relative deltas that hide the base rate. A "20% improvement" with no baseline is a
misleading metric whether it is a benchmark or a screening pamphlet.

---

## 6. The Three-Talk Model of Shared Decision-Making

Because a screening balance is small-benefit-vs-common-harm and depends on how *this* person weighs
those harms, the decision is a **shared decision**, not a clinician directive — and most screening
guidance for close-call situations explicitly calls for one. The **three-talk model** (Elwyn et al.,
2012, updated 2017) structures it:

```
  THREE-TALK MODEL  (a shared-decision workflow)
  ----------------------------------------------------------------
  TEAM TALK      "there is a choice here, and we will make it together"
                  -> establish that a real decision exists, offer support
        |
        v
  OPTION TALK    lay out the reasonable options + their benefits/harms
                  -> natural frequencies (Section 5), decision aids
        |
        v
  DECISION TALK  elicit and integrate the person's informed PREFERENCES
                  -> what matters to THEM (links to guide 06 "what matters most", guide 10)
  ----------------------------------------------------------------
  The output is a preference-congruent decision, not a default action. For a close-call screen,
  "no decision imposed" is the point: the right answer varies with values.
```

Shared decision-making is supported by **decision aids** (structured tools presenting options and
outcomes in natural frequencies) that improve knowledge and calibrate expectations. The three-talk
model is where this module's testing arithmetic (guide 03), evidence appraisal (guide 04), and the
patient's values (guides 06, 10) converge into an individual choice. Crucially, this guide describes
*how that decision is reasoned and structured* — it does not make the decision, and it issues no
schedule.

**On thresholds (the hard non-advice rule).** Real screening recommendations attach ages, intervals,
and cutoffs to specific tests. Those are set by named bodies — for example the USPSTF (US), NICE
(UK), and national screening committees — and they **change over time and differ between bodies and
countries** (the Anglo-American, evidence-shifting caveat of guide 00). This guide therefore names
*that such thresholds exist and who sets them*, but states none as guidance: any specific figure a
reader encounters must be read as attributed to a body, dated, and local — never as a universal or a
personal instruction.

---

## Fully Worked Case — Reasoning an Individual Screening Decision (illustrative, fictional)

All details and numbers are invented to show the *reasoning*; nothing here recommends obtaining or
forgoing any screening. Specifics are abstract (tests → `medicine/10`, diseases → `disease/`).

**Setup.** A fictional asymptomatic person, **P**, is weighing whether a screening test is right for
them. There is genuine uncertainty and it is a values-sensitive close call.

**Step 1 — frame with guide 03 (Section 2).** Because P is asymptomatic, the pretest probability is
low, so even a good test has low PPV: most positives would be false and lead to confirmatory testing.
The screen's value of information depends on whether a result would cross a decision threshold and
whether the benefit beats the cascade risk.

**Step 2 — surface the harms, including overdiagnosis (Section 3).** The clinician reasons through
false positives, the cascade, and — the subtle one — overdiagnosis: some detectable disease in P's
risk group would never have surfaced, and it cannot be distinguished at detection, so some
overtreatment is unavoidable if P screens.

**Step 3 — discount the illusions (Section 4).** Any "screen-detected patients live longer" figures
are recognized as inflated by lead-time and length-time bias; the clinician anchors on
disease-specific mortality from randomized evidence (guide 04), not survival-from-diagnosis.

**Step 4 — communicate in natural frequencies (Section 5).** The benefits and harms are laid out per
1,000 similar people, both arms on the same denominator, absolute not relative — so P sees a small
benefit alongside common false positives and some overdiagnosis. (The figures are illustrative; any
real numbers would be attributed and dated.)

**Step 5 — run the three-talk model (Section 6).** *Team talk:* there is a real choice. *Option
talk:* the options and their natural-frequency outcomes, with a decision aid. *Decision talk:* P's
own weighing of "avoid missing a bad outcome" against "avoid false positives, overdiagnosis, and
overtreatment." The output is P's **preference-congruent** decision — which could reasonably go
either way, because it depends on P's values, not on a universal rule.

**What the case shows.** A screening decision reasoned as a shared decision: guide 03's arithmetic,
guide 04's endpoint discipline, the screening-specific harms and illusions, honest natural-frequency
communication, and a values-driven three-talk structure — the reasoning this guide owns, with no
schedule issued and no personal advice given.

---

## Reader Tasks (answerable from this guide)

1. **Explain why a screening positive is usually not a diagnosis.** Use guide 03's low-prevalence
   arithmetic to show why PPV is low in the asymptomatic and why a positive prompts confirmation.
   (Section 2.)
2. **Distinguish overdiagnosis from a false positive.** Given a screen-detected case, explain how
   overdiagnosis involves *real* disease that would never have harmed the person, and why it cannot
   be told apart from harmful disease at detection. (Section 3.)
3. **Spot lead-time and length-time bias.** Given a claim that "screen-detected patients survive
   longer," identify both biases and name the endpoint (randomized disease-specific mortality) that
   would settle whether screening helps. (Section 4.)
4. **Re-express a risk in natural frequencies.** Given a relative-risk headline, convert it to
   absolute counts per 1,000 with both benefit and harm on the same denominator, and explain why
   that supports a real decision. (Section 5.)
5. **Structure a shared decision.** Given a values-sensitive screen, walk the three-talk model and
   explain why a threshold from a named body is attributed/dated guidance, not a personal
   instruction. (Section 6.)

---

## Decision Cheat Sheet

| Situation | What the reasoning does | Why (this guide) |
|---|---|---|
| Screening an asymptomatic person | applies **guide 03 at low prevalence**: expects low PPV, many false positives | screening paradox in situ (§2) |
| A screen detects "disease" | separates **overdiagnosis** (real but harmless) from a false positive | the indolent-disease reservoir (§3) |
| "Screen-detected patients live longer" | discounts **lead-time + length-time bias**; asks for randomized mortality | survival-from-diagnosis is an artifact (§4) |
| Communicating benefit/harm | uses **natural frequencies**, absolute, both arms per 1,000 | relative figures hide the base rate (§5) |
| A close-call, values-sensitive screen | runs the **three-talk model** to a preference-congruent choice | the right answer depends on values (§6) |
| Encountering a screening age/interval | reads it as **attributed, dated, local** guidance, not a rule | thresholds change and differ by body/country (§6, guide 00) |
| Deciding whether to screen at all | checks **value of information** + targeting by baseline risk | small benefit vs common harms (§2, guide 04) |

---

## Common Confusion Points

**"Early detection is always good."** Not for the asymptomatic. Screening runs a test at low
prevalence (many false positives), can overdiagnose harmless disease, and its apparent benefit is
inflated by lead-time and length-time bias. The real balance is small absolute benefit against
common harms — a values-sensitive shared decision, not a reflex.

**"Overdiagnosis just means a false positive."** No — a false positive means the disease is *absent*.
Overdiagnosis means the disease is *truly present* but would never have caused harm (indolent, or the
person dies of something else first). Because it cannot be distinguished at detection, it leads to
overtreatment of something that never needed treating.

**"Screen-detected patients survive longer, so screening works."** That inference is exactly what
lead-time and length-time bias corrupt: earlier diagnosis lengthens *measured* survival without
changing the date of death, and periodic screening oversamples slow disease. Only randomized
disease-specific mortality answers the question.

**"A 20% risk reduction is a strong reason to screen."** Only in absolute terms. Twenty percent off a
tiny base rate is a tiny absolute benefit (guide 04), and it must be shown against the common false
positives and overdiagnoses per the same denominator. Natural frequencies, not relative percentages,
support an honest choice.

**"This guide will tell me whether and when I should be screened."** It will not, by design. It
describes *how* a screening decision is reasoned and structured as a shared decision; it issues no
schedule and no personal advice. Real ages and intervals are set by named bodies, are dated, change
over time, and differ by country — read them as attributed guidance, and make personal decisions with
a qualified clinician.
