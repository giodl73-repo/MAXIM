---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-USABILITY-EVALUATION.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-computer-interaction:usability-evaluation
kind: guide
module: human-computer-interaction
section: human-computer-interaction
title: Usability Evaluation - Measuring and Diagnosing Interactive Systems
status: source-custody
source_custody: partial
current_path: human-computer-interaction/05-USABILITY-EVALUATION.md
canonical_path: human-computer-interaction/05-USABILITY-EVALUATION.md
backsource_ids: [mdloom-backfill:human-computer-interaction:05-usability-evaluation]
concepts: [usability-evaluation, heuristic-evaluation, think-aloud, usability-metrics, system-usability-scale, formative-summative, ab-testing]
root_concepts: [usability-evaluation]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Usability Evaluation — Measuring and Diagnosing Interactive Systems

**This guide owns** the *evaluation* half of the design↔evaluate loop: the methods
that measure and diagnose how usable an interactive system is — analytic inspection
(heuristic evaluation, cognitive walkthrough), empirical testing (think-aloud,
moderated benchmarks), the metric triad (effectiveness/efficiency/satisfaction),
standardized instruments (the SUS and its limits), the formative/summative split,
controlled and A/B experiments, qualitative coding and triangulation, the
sample-size ceiling, and the benchmark→iterate loop. **It builds on**
`04-DESIGN-PROCESS` (which produces the artifact being evaluated) and
`02-INTERACTION-MODELS` (the gulfs of execution/evaluation a usability problem lives
in). **It explicitly defers**: the *cognitive mechanisms* behind observed problems —
why attention, memory, and perception behave as they do, and the psychophysical
"laws" (Fitts, Hick, Miller, cognitive load, GOMS timing) — to
`cognitive-science/` (especially `cognitive-science/09-APPLIED-BRIDGE`); the
*general inferential statistics* a summative study needs — hypothesis testing, power
analysis, confidence-interval and regression machinery — to `statistics-applied/`
and, for HCI-specific study design, `06-RESEARCH-METHODS`; the *design methods* that
generate solutions to `04`; and *operator performance in safety-critical work*
(workload, human-error taxonomy) to [`human-factors/`](../human-factors/00-OVERVIEW.md).

> **This module is an educational reference about *how interactive systems are
> designed and evaluated*. Evaluation methods here are described as engineering
> instruments, not as a warrant to skip ethics review of human-subjects research, and
> not as a manipulation playbook. Named "laws" and standards are attributed and
> dated; heuristics are heuristics, not empirical laws; and a passing score is never
> proof of a usable system.**

*Per-guide banner: this guide is about the theory and practice of usability
measurement. Every numeric benchmark below (detection rates, SUS means, sample sizes)
is attributed and dated where it names a published figure, and treated as a
population-and-task-dependent estimate, never a universal constant.*

---

## The Big Picture: Evaluation Is a Measurement Instrument Pointed at a Design

A usability evaluation is not a verdict ("good" / "bad"); it is a **measurement
instrument** with a purpose, a resolution, and an error model. The two questions that
determine every method choice are orthogonal: *do you want to **find problems** or
**measure a level**?* and *does the data come from **experts/models** or from **real
users**?* Where you sit on those two axes picks the method *family*; the exact method,
the sample size, the setting, and what you are entitled to conclude then turn on a
second set of fit factors — risk/stakes, task type, target population, ecological
validity, product maturity, and practical constraints — that the axes do not capture.

```
THE EVALUATION LOOP   (this guide owns the right-hand "evaluate" half)
==========================================================================
   DESIGN (guide 04)                        EVALUATE (this guide)
   generate candidate  ----------------->   measure & diagnose  ----+
       designs                                                      |
         ^                                                          |
         +------------- iterate: fix, then re-measure <-------------+

   AXIS 1 -- what do you want?         AXIS 2 -- where is the data from?
   ------------------------------      ---------------------------------
   FORMATIVE : find & fix problems     ANALYTIC  : experts / models, no users
   SUMMATIVE : measure vs a target     EMPIRICAL : real users doing real tasks
==========================================================================
   Read it as: the (Axis 1 x Axis 2) cell picks the method FAMILY, not more.
   A "positive result" is a data point about a design, not a fact about a user.
```

The two axes give four cells, and each names a family of methods:

| | FORMATIVE — improve it | SUMMATIVE — grade it |
|---|---|---|
| **ANALYTIC** (no users) | heuristic evaluation; cognitive walkthrough; expert review | model-based predictive estimates (GOMS/KLM task times — deferred to `02`/`cognitive-science/09`) |
| **EMPIRICAL** (users) | think-aloud usability test (small-*n*, rich, diagnostic) | benchmark usability test; **A/B test** (field, huge-*n*, one metric) |

**The axes narrow; they do not decide.** A cell names a *family*; which specific method
you run, with how many participants, in what setting, and what you may conclude are
*not* determined by the axes. Six fit factors, developed through the guide, do the rest:

- **Risk / stakes.** A safety- or money-critical flow justifies more method and larger,
  powered samples than a low-stakes copy tweak.
- **Task type.** Walk-up-and-use vs expert-repeated, transactional vs exploratory,
  change the fit (cognitive walkthrough for first-use learnability vs a longitudinal
  study for expert efficiency).
- **Population.** One homogeneous segment vs many; disabled users and their assistive
  technology (guide `08`); non-WEIRD populations for whom think-aloud may not transport.
- **Ecological validity.** Lab realism vs field/in-the-wild — the more the setting
  distorts the real task, the less any clean number actually means.
- **Maturity.** A napkin sketch wants cheap formative inspection; a release candidate
  wants a powered summative benchmark.
- **Constraints.** Time, budget, recruiting reach, and platform/traffic access bound
  what is genuinely runnable.

So the two-axis table is a *starting filter*, not a decision procedure; the same cell
resolves to different studies for a low-stakes prototype and a safety-critical release.

Three consequences drive the rest of the guide:

1. **Finding problems and measuring level are different jobs with different
   mathematics.** The "5 users" rule is a *problem-discovery* result; it says nothing
   about how precisely you can estimate a completion rate or compare two designs
   (Section 6). Using a discovery sample to make a measurement claim is the most
   common methodological error in the field.
2. **Analytic methods are cheap and biased; empirical methods are expensive but
   directly observe behavior** — evidence that is still sample-, task-, and
   context-bounded, never ground truth. Inspection predicts problems from expertise (and
   inherits the *evaluator effect*, Section 2); user testing observes them (and inherits
   *sampling* and *reactivity*). Neither dominates — they triangulate (Section 8).
3. **Behavioral scale and explanatory depth trade off.** An A/B test measures *how
   much* a change moves a metric across a whole population but is blind to *why*; a
   think-aloud explains *why* on eight people but cannot estimate a population effect
   (Section 7).

**Bridge (software).** This maps cleanly onto engineering practice you already run.
Analytic inspection is **static analysis / linting / code review against a style
guide** — cheap, early, catches known smells, produces false positives, and misses
anything the rules don't encode. Empirical testing is **runtime testing and
profiling** — you execute the system with real load and watch what actually happens.
Formative vs summative is **debugging (find & fix) vs benchmarking (measure against an
SLA)**. And an A/B test is exactly the **online controlled experiment / flighting**
platform you shipped features through — randomized, powered for one metric, causal but
uninformative about mechanism.

---

## 1. Two Purposes: Formative vs Summative

The single most clarifying distinction in evaluation, borrowed from educational
assessment (Scriven 1967): a **formative** evaluation exists to *change the thing being
evaluated* (find problems while there is still time to fix them); a **summative**
evaluation exists to *judge the thing* against a target, a competitor, or a prior
release. The same method run with a different purpose becomes a different study.

```
  FORMATIVE                              SUMMATIVE
  ----------------------------------     ----------------------------------
  goal: discover & diagnose problems     goal: quantify a level / compare
  when: during design, iteratively       when: at a milestone / before ship
  data: mostly qualitative + severity    data: mostly quantitative + CIs
  n   : small (discovery-sized, ~5-8)    n   : larger (estimate-sized, 2 sigma)
  out : ranked problem list -> fixes     out : metrics vs target, decision
  err : "did we miss a problem?"         err : "how wide is our uncertainty?"
```

The costliest confusion in practice is running a formative-sized study (five users)
and then reporting a summative-sounding number ("task success was 80%!"). Five users
with 4 of 5 succeeding give a **95% Wilson score interval** of about **[0.38, 0.96]**
(±29 points; derived in Section 6) — i.e., the true rate could be anywhere from ~38% to
~96%. The number is not wrong; it is *unresolved*, and reporting it as a measurement is
the error (Section 6).

---

## 2. Analytic Inspection I — Heuristic Evaluation

**Heuristic evaluation** (Nielsen & Molich 1990; refined in Nielsen 1994) has a small
set of evaluators independently judge an interface against a short list of recognized
usability principles, then merge and severity-rate the problems they found. The
canonical list is **Nielsen's 10 heuristics** (1994): visibility of system status;
match to the real world; user control and freedom; consistency and standards; error
prevention; recognition over recall; flexibility and efficiency; aesthetic and
minimalist design; help users recognize/diagnose/recover from errors; help and
documentation.

Severity is usually rated on Nielsen's 0–4 scale (0 = not a problem, 4 = usability
catastrophe), combining **frequency × impact × persistence**, to rank the fix queue.

```
  HEURISTIC EVALUATION PIPELINE
  --------------------------------------------------------------
  each evaluator, ALONE:                 then, TOGETHER:
    walk the UI  ->  flag violations       merge duplicate flags
    tag each with a heuristic              rate severity 0-4
    note where and why                     rank the fix queue
  --------------------------------------------------------------
  Independence first (avoid anchoring), aggregation second.
```

**The load-bearing caveat: heuristics are heuristics, not laws.** The ten items are
*experience-distilled rules of thumb*, not empirical constants and not a coverage
guarantee. Three consequences follow:

- **The evaluator effect is large.** A single evaluator finds only about **one-third**
  of the problems present (Nielsen 1994 reports averages near 35%); *which* third
  depends on the person. Different competent evaluators, given the same interface and
  the same heuristics, produce substantially different problem sets (the "evaluator
  effect"; see Hertzum & Jacobsen 2001, who found agreement often below 50%). The
  heuristics do not make the method objective.
- **Aggregation is why it works at all.** Because misses are partly independent across
  evaluators, unioning several evaluators' lists recovers most problems. Nielsen's
  recommendation of **3–5 evaluators** comes from the discovery model in Section 6
  applied to inspection: at an average per-evaluator detection rate around **λ ≈ 0.31**
  (the Nielsen & Landauer 1993 discovery-model figure), five evaluators find roughly
  **75–85%** of problems while one finds **~31%**. Keep two close-but-distinct numbers
  apart: the **0.31** here is the *discovery-model* detection rate, whereas the **~35%**
  single-evaluator figure above is Nielsen's separately reported *heuristic-evaluation*
  average (**1994**) — a different study lineage, not the same constant. This is a
  cost/coverage argument, **not** a guarantee, and the true detection rate varies with
  interface and evaluator expertise.
- **Inspection over-produces false positives.** Predicted "problems" that never trouble
  a real user are common; heuristic evaluation is good at *generating hypotheses to
  check*, weaker at confirming that any given prediction matters. Adequately powered
  empirical testing (Section 3) is the arbiter — but a *discovery-sized* user sample can
  confirm a prediction, not refute one (Section 6): an inspection flag unseen by five
  users is **unresolved, not cleared**.

**Bridge (software).** Heuristic evaluation is a **lint pass against a style guide**:
fast, runs without users/load, flags known anti-patterns, and produces both true and
false positives that a human triages. The evaluator effect is **reviewer variance** —
the reason you send a design to several reviewers, exactly as you send a hard PR to
several engineers.

---

## 3. Analytic Inspection II — Cognitive Walkthrough

Where heuristic evaluation is a broad checklist, the **cognitive walkthrough**
(Wharton, Rieman, Lewis & Polson 1994; roots in Lewis & Polson's CE+ theory) is a
*focused simulation of a first-time user* learning by exploration. Evaluators pick a
concrete task, list the correct action sequence, and at **each step** ask a fixed set
of questions — classically four:

```
  AT EACH STEP OF THE CORRECT ACTION SEQUENCE, ASK:
  --------------------------------------------------------------
  Q1  Will the user be trying to achieve the right effect?
  Q2  Will they notice the correct action is available?
  Q3  Will they connect that action to the effect they want?
  Q4  After acting, will they see progress toward the goal?
  --------------------------------------------------------------
  A "no" (with a story of why) IS the finding. It localizes the
  break to a step and to a gulf (execution vs evaluation, guide 02).
```

The walkthrough's strength is **learnability for walk-up-and-use systems** (kiosks,
one-off flows, onboarding) and its precision: a finding is pinned to a specific step
and a specific reason, which maps directly to a fix. Its weakness is narrowness — it
evaluates the tasks you script and the "correct" path you chose, so it misses problems
off the happy path, and it says little about efficiency for expert users. **Pluralistic
walkthroughs** (Bias 1994) add real users and stakeholders walking the steps together
to reduce evaluator bias.

*Deferral.* *Why* a user fails Q2 or Q3 — the perception/attention/memory mechanism —
is `cognitive-science/`'s to explain; this guide uses the mechanism as an observed
constraint and localizes *where* it bites.

---

## 4. Empirical Method I — The Think-Aloud Usability Test

The workhorse of formative evaluation. A participant attempts realistic tasks on the
system while **verbalizing their thoughts**; a facilitator observes without leading.
The theory is protocol analysis (Ericsson & Simon 1980, 1993): concurrent verbalization
of the contents of working memory is a reasonably faithful window on reasoning — with
caveats.

```
  CONCURRENT vs RETROSPECTIVE THINK-ALOUD
  --------------------------------------------------------------
  CONCURRENT      talk WHILE doing        rich, in-the-moment
                                          BUT can alter behavior (reactivity):
                                          slower, more deliberate, over-rational
  RETROSPECTIVE   talk AFTER, on replay   preserves natural task behavior
                                          BUT memory decay + post-hoc rationalizing
  --------------------------------------------------------------
  Facilitator rule: prompt only "keep talking / what are you thinking?",
  never "have you tried the menu?" -- leading questions manufacture success.
```

Three honesty points a peer should hold:

- **Reactivity.** Talking aloud is not free; it can make people slower and more
  systematic than they would be silently (the "veridicality" and reactivity debate).
  Concurrent think-aloud is a good problem *detector*, a poor time *measurer* — do not
  report task times from a chatty concurrent session as performance data.
- **Verbal ≠ ground truth.** People rationalize; stated reasons can post-date the
  behavior. The *behavior* (where they clicked, where they stalled) is the stronger
  signal; the talk is a hypothesis about why.
- **Facilitator effects.** The moderator is part of the instrument. Leading, rescuing,
  or reacting changes the data. This is why protocols script the prompts.

Think-aloud is *diagnostic*, not *metric*: it tells you **what breaks and plausibly
why**, on a handful of people. It is the method that turns "the funnel drops 20% here"
(from analytics or an A/B test) into "because users read this label as a different verb."

**Bridge (software).** A moderated think-aloud is **interactive tracing of a black
box**: you drive the system through real scenarios and watch the internal state the
user narrates, exactly as you attach a debugger and step through to see *why* a request
stalls — with the same observer-effect risk that instrumentation perturbs timing.

---

## 5. Metrics — Effectiveness, Efficiency, Satisfaction

Once you want numbers, the anchor is **ISO 9241-11** (1998; revised 2018), which
defines usability as **effectiveness, efficiency, and satisfaction in a specified
context of use**. That triad is the metric taxonomy.

| Dimension | Typical metric | Operational definition (must be pre-committed) | Trap |
|---|---|---|---|
| **Effectiveness** | task success rate | fraction of attempts reaching a pre-defined success state | "success" must be defined *before* testing, incl. partial success |
| | error rate / error paths | count/type of deviations from an optimal path; recoverable vs not | counting keystrokes is not counting errors; classify them |
| **Efficiency** | time on task | elapsed time for successful completions (exclude/flag failures) | timing a concurrent think-aloud is measuring the wrong thing |
| | lostness / path length | actual vs optimal navigation steps (Smith's lostness metric) | needs a defensible "optimal" path |
| **Satisfaction** | SUS, SEQ, UMUX-Lite | standardized post-task/post-test questionnaires (Section 5.1) | satisfaction correlates only loosely with performance |

**Defining "task success" is where rigor lives.** A binary success/fail hides most of
the signal; a **graded scale** (complete unaided / complete with difficulty / complete
with assist / failed / gave up) preserves it. And success must be judged against a
*pre-registered success state*, or the analyst's post-hoc leniency becomes the
measurement.

### 5.1 Standardized Satisfaction Instruments — and the SUS Trap

The **System Usability Scale** (SUS; Brooke 1996) is the field's most-used instrument:
ten alternating positive/negative statements on a 5-point agree scale, scored into a
single number **0–100**. Its ubiquity gives it comparability, but it is routinely
misread. Hold these facts:

```
  SUS SCORING (Brooke 1996)  -- ten items, alternating polarity
  --------------------------------------------------------------
  odd items  (positive): contribution = (response - 1)
  even items (negative): contribution = (5 - response)
  SUS = 2.5 x sum(contributions)        -> range 0..100
  --------------------------------------------------------------
  The x2.5 makes it 0-100. That is NOT a percentage and NOT a percent
  of users satisfied. A SUS of 72 is not "72% good."
```

- **It is not a percentage.** 0–100 is a *scaled score*, not "percent satisfied." The
  benchmark mean across many studies is about **68** (Sauro 2011), so a "70" is roughly
  *average*, not a B-minus. Interpretation uses empirical norms — Bangor, Kortum &
  Miller (2008/2009) adjective anchors ("OK/good/excellent") and acceptability ranges,
  or the Sauro–Lewis curved grade scale (~68 ≈ C, ~80+ ≈ A).
- **It is not unidimensional in practice.** Lewis & Sauro (2009) found a two-factor
  structure (**Usable** and **Learnable**); treating one number as "the usability" hides
  which factor moved.
- **It is not diagnostic.** SUS tells you *that* perceived usability is high or low, not
  *what* to fix. It is a tracking/benchmarking instrument, useless on its own for
  improvement — pair it with formative data.
- **It is perceived usability.** A self-report after the fact; it correlates only
  moderately with measured task performance. Users can rate a system they failed on
  surprisingly highly (and vice versa).
- **Report it as a distribution, not a point.** A SUS is only interpretable with its
  **mean, SD, and *n*, plus a CI** — always a *t*-interval on the mean here, since the
  ±2.5 scaling and small samples make the bare number look more precise than it is. "SUS
  77" is not a result; "SUS 77 (SD 16, n=40, 95% CI [72, 82])" is.

Lighter instruments have their place: the **Single Ease Question** (SEQ; Sauro & Dumas
2009), a 7-point post-*task* difficulty rating, is cheap and sensitive; **UMUX-Lite**
(Lewis 2013) approximates SUS in two items. **NASA-TLX** (Hart & Staveland 1988)
measures *workload*, not satisfaction — and workload under load is where this guide
hands off to `human-factors/`. Net Promoter is a loyalty/brand metric, not a usability
metric; do not substitute it for one.

**Bridge (software).** SUS is a **single composite health score** — like rolling
latency, error rate, and saturation into one "service score." Excellent for a dashboard
trend line, hopeless for root-causing an incident. You would never debug an outage from
the composite alone; do not redesign a flow from a SUS number alone.

---

## 6. The Sample-Size Ceiling — Discovery Is Not Measurement

This is the section that separates a rigorous practitioner from a cargo-cult one. There
are **two different sampling questions**, with two different answers.

**(a) Problem discovery (formative).** How many users/evaluators to find *most* of the
problems? Model each distinct problem as detected by a random participant with some
probability *λ*; the chance a problem with detection rate *λ* is seen at least once in
*n* independent sessions is:

```
  P(problem seen at least once) = 1 - (1 - lambda)^n          (Nielsen & Landauer 1993)

  at the widely cited average lambda ~= 0.31:
     n=1 -> 31%      n=3 -> 67%      n=5 -> 85%      n=8 -> 95%
```

That is the origin of "**five users find ~85% of problems**" (Nielsen & Landauer 1993;
Virzi 1992). Read it honestly:

- It is a claim about **problem discovery only**, and only about problems with an
  *average* detection rate near 0.31. **Low-salience problems** (small *λ*) need many
  more sessions; rare-but-severe problems can hide past 15 users.
- *λ* is **not a constant**. It varies by interface, task, and user segment. On large,
  heterogeneous sites the effective *λ* is small and five users is badly insufficient
  (Spool & Schroeder 2001; Faulkner 2003 shows how much the *found* fraction varies
  run-to-run even at n=5). "Five users" is a **default for a single homogeneous segment
  on a focused flow**, not a law — and distinct user segments each need their own ~5.
- It says **nothing** about how *big* any problem is or how *precisely* you know a rate.

**(b) Measurement / comparison (summative).** How many users to estimate a completion
rate to a given width, or to detect a difference between two designs? This is ordinary
statistical estimation and power — and it needs far larger samples. A completion-rate
confidence interval from a small binomial sample is wide and should use a small-sample
method: **this guide reports the Wilson score interval (95%) throughout** (the closely
related adjusted-Wald / Agresti–Coull interval, Sauro & Lewis 2012, gives similar
bounds), never the naive normal (Wald) approximation. A *comparison* of two designs is
not an interval on either rate by itself — it needs a confidence interval or test on the
**difference**, and which one depends on the design: a **two-sample** procedure (e.g.,
two-proportion / N−1 chi-square) for independent, between-subjects groups; a **paired**
procedure (e.g., McNemar for success, paired *t* for a mean) when the same users saw
both. Detecting a small A/B difference can need thousands per arm.

```
  ROUGH 95% CI HALF-WIDTHS ON A COMPLETION RATE (Wilson score, illustrative)
  n = 5    p-hat 0.80  ->  CI approx [0.38, 0.96]   (+/- ~29 pts) -- unresolved
  n = 20   p-hat 0.80  ->  CI approx [0.58, 0.92]   (+/- ~17 pts)
  n = 40   p-hat 0.80  ->  CI approx [0.65, 0.90]   (+/- ~12 pts)
  n = 100  p-hat 0.80  ->  CI approx [0.71, 0.87]   (+/- ~8 pts)
  Halving the interval width roughly QUADRUPLES the sample -- the sqrt(n) wall.
```

*(Reproducibility: every completion-rate CI in this guide is a 95% Wilson score
interval; every mean CI — e.g., the SUS below — is a 95% *t*-interval from the reported
mean, SD, and *n*. Both are recomputable from the numbers stated, which is the point:
the method is named and the inputs are exposed.)*

*Deferral.* The interval and power **machinery** — which formula, exact widths, effect
sizes, corrections for multiple comparisons — belongs to `statistics-applied/` and, for
study design, `06-RESEARCH-METHODS`. This guide owns the *decision rule*: **discovery
samples cannot make measurement claims, and measurement/comparison needs a powered
sample sized in `statistics-applied/`.**

**Bridge (software).** The discovery curve is a **coverage-saturation curve**: each new
fuzzing seed (participant) finds fewer *new* crashes (problems) than the last, and you
stop when marginal discovery falls below cost — but coverage saturation tells you
nothing about how *often* a bug fires in production. For that you need the equivalent of
a powered measurement, not more seeds.

---

## 7. Controlled Usability Tests vs A/B Tests

Both are empirical; they answer different questions and are blind to different things.

A **controlled/comparative usability test** is a moderated (or carefully unmoderated)
study, small-*n*, that compares designs or conditions with **within-** or
**between-subjects** structure, counterbalancing to control order/learning effects. It
yields rich, causal-*for-the-tested-tasks* insight plus *why*.

An **A/B test** (online controlled experiment; the flighting you already know) randomly
assigns live users to variants and compares one or a few **behavioral metrics** at
scale. Randomization buys causal attribution of the *metric change*; scale buys tight
estimates. It is blind to *why*, to low-frequency users, and to anything not
instrumented.

| Question | Controlled usability test | A/B test |
|---|---|---|
| Primary output | *why* a design works or fails; problem diagnosis | *how much* a change moves a metric |
| Sample | small (5–30), recruited, observed | huge (10³–10⁶), live, anonymous |
| Setting | lab / moderated / task-scripted | production / natural / in-the-wild |
| Causal about | the tested tasks, with observation | the population metric, via randomization |
| Blind to | population effect size; long-term/rare behavior | mechanism (*why*); un-instrumented experience; edge users |
| Fails when | tasks unrepresentative; moderator leads | metric is a poor proxy; novelty effects; p-hacking many metrics |
| Software analog | integration test with a human in the loop | canary / flag experiment at scale |

The mature move is **sequencing**: a formative think-aloud (Section 4) to *find and
explain* candidate problems, then an A/B test to *measure* whether the fix moves the
outcome metric at scale. Running only A/B tests yields a system that is locally
optimized and globally unexplained ("we hill-climbed the funnel and have no idea why the
new flow confuses power users"). Running only lab tests yields explanations you never
confirmed move the real needle.

*Caveat — A/B ethics and metric choice.* An A/B test optimizes whatever metric you pick;
optimizing engagement or conversion without a guardrail is how **dark patterns** get
A/B-validated. Metric selection is an ethical act (guide `11-PRACTICE-ETHICS`), and
experiments on people carry consent/welfare obligations this guide flags but does not
adjudicate.

---

## 8. Qualitative Coding and Triangulation

Formative data is mostly qualitative — observations, quotes, stalls, workarounds — and
turning it into a defensible problem list is a method, not a vibe.

- **Coding.** Segment sessions into events; assign each a **code** (a problem type, a
  UI location, a heuristic violated). Codes can be *deductive* (a pre-set scheme, e.g.,
  Nielsen's heuristics) or *inductive* (emergent). Be explicit about the analytic
  *paradigm*, because the paradigm — not a universal rule — decides what "good coding"
  means and whether inter-rater agreement is even the right quality test (next bullet).
- **The quality criterion depends on the paradigm; they are not interchangeable.** In a
  **coding-reliability** or **codebook** approach — a structured scheme applied as a
  *measurement* (e.g., Boyatzis 1998; codebook variants of thematic analysis; most
  usability problem-tallying) — double-coding and **inter-rater reliability** (two
  coders, agreement beyond chance — Cohen's κ) *are* an appropriate check, and a claim
  that leans on the coding should report it. In **reflexive thematic analysis** (Braun &
  Clarke 2006, 2019), coding is an interpretative, situated act; the authors argue
  explicitly that **inter-rater reliability is *not* the quality criterion** and that κ
  misframes interpretation as measurement — quality there comes from reflexivity, depth
  of engagement, and a coherent, well-evidenced account, not from two coders agreeing.
  So report κ *only* when your paradigm treats coding as measurement; do not bolt it onto
  a reflexive analysis. The *statistic itself* is `statistics-applied/`'s; picking the
  paradigm and its matching quality criterion is this guide's.
- **Severity and merging.** Rank merged problems by frequency × impact × persistence
  (Section 2), producing the fix queue.

**Triangulation** is the payoff: no single method is trustworthy alone, so you converge
several and read the agreements and — more informatively — the disagreements.

```
  TRIANGULATION -- converge independent instruments on the same design
  --------------------------------------------------------------
   heuristic eval  --\                     agree  -> high confidence, fix now
   think-aloud     ---\                    inspection-only, unseen by a small user
   benchmark (SUS, ----> merge & compare       sample -> UNRESOLVED: confirm, not refute
   completion CIs) ---/                    users-fail / metric-flat -> a real problem
   A/B / analytics --/                         the metric can't see; instrument it
  --------------------------------------------------------------
   Divergence is a FINDING, not noise: it says which instrument is blind here.
```

A problem flagged by inspection but not seen in a small user sample is **unresolved,
not disproven**: a discovery-sized sample lacks the power to refute a low-*λ* prediction
(Section 6), so the honest move is to confirm it with more or different users, not to
dismiss it as a false positive. A stall every user hits that the analytics funnel
doesn't show means the metric is blind to it; an A/B win with no mechanism from the lab
is a prompt to find the mechanism before generalizing.

---

## 9. The Benchmark → Iterate Loop

Evaluation is only useful if it closes a loop. The mature program runs a **usability
benchmark** — a fixed task set, fixed metrics, fixed protocol — on a **baseline**, sets
**targets**, and re-runs the identical benchmark each iteration so results are
comparable over time (a regression suite for usability).

```
  BENCHMARK -> DIAGNOSE -> FIX -> RE-BENCHMARK   (the usability regression loop)
  --------------------------------------------------------------
   1. baseline benchmark   : fixed tasks + metrics (completion, time, SUS/SEQ)
   2. formative diagnosis  : think-aloud + inspection -> ranked problem list
   3. fix the top severities (guide 04)
   4. re-run the SAME benchmark : is the run-to-run DIFFERENCE significant?
   5. guard against regression : keep prior tasks in the suite
  --------------------------------------------------------------
   Rule: only compare benchmarks that used the same tasks, metrics, and protocol.
   A "win" is a significant run-to-run DIFFERENCE (CI/test on the change), §6.
```

Two disciplines make it honest: (1) **change one thing at a time** across benchmark
runs, or you cannot attribute the movement; (2) an improvement counts only when a
**confidence interval or test on the *difference* between runs** — paired if the same
users ran both, two-sample if the runs used independent groups — excludes zero.
Whether one run's point estimate happens to fall outside the *other* run's interval is
**not** a valid comparison (two overlapping single-sample CIs can still hide a real
difference, and vice versa). An 80%→85% completion bump on n=20 is well inside the noise
of that difference (Section 6).

---

## A Fully Worked Mixed-Method Evaluation (illustrative, fictional)

*All names, numbers, and findings below are invented to show how the methods compose
into one plan and one synthesis. Nothing here is a real product or a real benchmark.*

**System.** *Tessera*, a fictional internal web app for submitting and approving
travel-expense claims at a mid-size company. A redesign of the claim-submission flow is
underway. Two questions: *(formative)* what breaks in the redesign, and *(summative)*
is it good enough to replace the legacy flow before a company-wide rollout?

**Goals & targets (pre-committed).**
- Formative: find and rank the top usability problems in the new submission flow.
- Summative: **submission-task success ≥ 90%**, **median time ≤ 4 min**, **SUS ≥ 75**
  (chosen because the legacy flow benchmarked at SUS 62 and the team wants a clear,
  above-average improvement, not a coin-flip).
- **Pass rule (pre-committed).** A target counts as *met* only if the **entire two-sided
  95% CI** sits at or beyond it — a deliberately conservative rule, statistically
  equivalent to a one-sided test at **α = .025** (a two-sided 95% interval leaves 2.5% in
  the relevant tail). A less strict one-sided **α = .05** decision would instead require
  the **95% one-sided lower confidence bound** — equivalently, the lower limit of a **90%
  two-sided CI** — to sit at or beyond the target; this guide precommits to the stricter
  whole-95%-CI rule. The legacy→redesign SUS gain counts only if a **two-sample**
  difference CI (the two benchmarks are independent samples) excludes zero. Fixed *before*
  data collection so no post-hoc leniency can rescue a near miss.

**Round 1 — analytic inspection.** Three evaluators run an independent heuristic
evaluation, then merge. They surface 23 candidate problems; after merging duplicates and
setting aside 6 as low-confidence predictions (to confirm or drop with users, not
pre-judged false), **17** remain, 4 rated severity 3–4 (e.g.,
"receipt-upload errors are reported below the fold with no status change" — violates
*visibility of system status*). Explicit note in the report: **evaluator effect** — a
single evaluator had found only 8–11 of these; the union of three is why coverage is
acceptable, and the list is *hypotheses to confirm*, not confirmed defects.

**Round 2 — formative think-aloud.** Six participants (one segment: employees who file
claims monthly) attempt four scripted tasks with concurrent think-aloud. Behavior
confirms 9 of the 17 inspection problems as real (users actually stall), leaves 3
**unresolved** (predicted but not hit in this six-person sample — *not* refuted, since a
discovery sample can't clear a low-*λ* prediction), and **surfaces 2 that inspection
missed**: users read "Itemize" as "submit line items now" and abandon; and the currency
selector defaults to the company HQ currency, silently mis-converting for a traveler
abroad. The two new problems are severity 4. Sample-size honesty in the write-up: six
users is a *discovery* sample for one segment; approvers and international filers are
separate segments needing their own sessions, and low-*λ* problems (plus the 3 unresolved
predictions) may remain undiscovered.

**Fixes (guide 04).** Team fixes the top 6 severities: inline upload status, relabel
"Itemize" → "Add expense items," currency defaults to the claim's trip country, etc.

**Round 3 — summative benchmark.** Unmoderated, **n = 40** monthly filers, the same four
tasks, measuring task success, time on successful tasks, SEQ per task, and SUS at the
end. Results (illustrative):

```
  TESSERA SUMMATIVE BENCHMARK (n=40, illustrative)
  --------------------------------------------------------------
  submission success   : 88%   (Wilson 95% CI approx [74%, 95%])
  median time (success):  3.6 min
  SUS (mean)           : 77    (SD 16, n=40; 95% t-interval [72, 82])
  SEQ, "add expense"   :  6.1 / 7   (was the worst task in round 2)
  --------------------------------------------------------------
```

**Reading against targets, honestly.**
- **SUS 77** sits above the ≥75 target at the point estimate, but the 95% CI [72, 82]
  **includes values below 75**, so under the pre-committed pass rule (whole two-sided 95%
  CI at or beyond target — the conservative α = .025 rule) the **target is not
  demonstrated**. Even the less strict one-sided α = .05 check fails here: the 95%
  one-sided lower bound (≈73 — the lower limit of a 90% two-sided CI) still sits below 75.
  The data are consistent with the true value being under 75, and the one-sided test/
  interval that would settle it belongs to `statistics-applied/`. The honest report says
  "**SUS target not demonstrated at n=40** (point estimate above, interval spans it),"
  never "at target."
- **Success 88%** misses the 90% target, and its CI is wide (n=40 is a modest
  measurement sample). The point estimate plus the round-2 diagnosis point at the
  currency/international-filer path, which this monthly-domestic sample under-represents
  — a **segment** gap, not just noise.
- **Median time 3.6 min** is below the 4-minute target at the point estimate, but
  this fictional summary does not include a confidence interval for the median.
  Under the precommitted whole-interval rule, the **time target is therefore not
  demonstrated**. A real study would pre-specify a median/quantile interval method
  (for example, an order-statistic or bootstrap interval) before interpreting it.

**Round 4 — A/B test (post-launch, one contested decision).** The team disagreed on
single-page vs three-step wizard. They ship the wizard to 50% of live users and measure
**submission-completion rate** and **abandonment**, randomized, for two weeks
(hundreds of thousands of sessions). The wizard wins completion by **+2.1 points**
(tight CI, clearly beyond noise at that scale). But the A/B test is **blind to why** and
to the international-filer stall (too rare to move the aggregate) — so the lab finding
about currency still stands and still needs its own fix; the A/B result does not
overrule it.

**Triangulation & decision.** Inspection, think-aloud, benchmark, and A/B **converge**
on "the redesign is an improvement over legacy (SUS 62→77 — an apparent gain a two-sample
difference test on the independent benchmarks would confirm, not the two point estimates
alone; the wizard's completion lift was a randomized within-experiment difference)" and
**diverge** on international filers (a severe lab problem the population metric can't
see). Decision: roll out the wizard; **do not** claim "target met" — the SUS ≥75 target
is **not demonstrated** at n=40 and success missed 90%; report the legacy improvement
separately and open a **segment-specific** formative round for international/approver
flows before re-testing against the summative target. The evaluation's *limits* are
stated as plainly as its results — that is what makes it a measurement, not a marketing
number.

---

## Reader Tasks (answerable from this guide)

1. **Pick the method for a stage and goal.** Given "we're mid-redesign and want to know
   what confuses new users," locate the cell (formative × empirical) and choose a
   think-aloud test; given "we must certify the new flow beats the old before rollout,"
   choose a summative benchmark (and, for one live decision, an A/B test). Justify from
   the two axes. (Big Picture, §1, §7.)
2. **Size and defend a study.** Explain why five users is defensible for discovering
   problems in one segment but indefensible for claiming "task success is 88%," using the
   discovery model and the CI-width table — and say what `statistics-applied/` must
   supply to make the comparison claim. (§6.)
3. **Interpret a SUS score correctly.** Given "our SUS is 72," state that it is a scaled
   0–100 score (not 72% satisfied), that ~68 is average so 72 is roughly average-plus,
   that it is perceived and non-diagnostic, what you must demand alongside it (the SD, the
   *n*, and a CI, since a bare mean hides its precision), and what formative data you'd
   pair with it — and, if 72 is being judged against a target, apply the pre-committed
   pass rule: the whole two-sided 95% CI must sit at or beyond the target (a one-sided
   test at α = .025), not merely the point estimate. (§5.1, worked case.)
4. **Choose A/B vs usability test — and name the blind spot.** Given "does the new
   checkout reduce abandonment?" pick an A/B test and state it won't tell you *why* or
   catch edge-segment failures; given "why do users abandon at step 3?" pick a
   think-aloud and state it can't estimate the population effect. (§7.)
5. **Read a heuristic-evaluation report skeptically.** Given a one-evaluator heuristic
   report of "15 problems," explain the evaluator effect (one evaluator ≈ ⅓ coverage),
   the false-positive rate, and why you'd confirm the severe items with users before
   funding fixes. (§2, §8.)

---

## Decision Cheat Sheet

| Situation | What the evaluation does | Why (this guide) |
|---|---|---|
| Early design, "what's broken?" | **formative**: think-aloud + heuristic eval, small-*n* | discover & diagnose; measurement not yet the point (§1–4) |
| Milestone, "is it good enough?" | **summative** benchmark: success/time/SUS with CIs | quantify vs a pre-set target (§1, §5) |
| No users available yet | **inspection** (heuristic eval, cognitive walkthrough) | cheap early hypotheses; expect false positives + evaluator effect (§2–3) |
| Only one evaluator did the review | treat coverage as ~⅓; **add evaluators** or confirm with users | evaluator effect; heuristics aren't laws (§2) |
| A SUS number is quoted | read as **scaled 0–100, ~68 = average, non-diagnostic** | SUS is perceived, one-number, needs formative pairing (§5.1) |
| "Five users is enough" claimed | ask **enough for what?** discovery yes (one segment), measurement no | discovery ≠ estimation; *λ* varies; segments each need ~5 (§6) |
| Comparing two designs at scale | **A/B test** on a guardrailed metric | randomization gives causal metric attribution — but not *why* (§7) |
| Need to know *why* it fails | **moderated think-aloud** | behavior + narrated reasoning localize the cause (§4) |
| Methods disagree | **triangulate**: divergence names the blind instrument | no single method is ground truth (§8) |
| Claiming an improvement | test the **difference** (paired if same users, two-sample if independent); require its CI to exclude 0 | comparing a point estimate to the *other* run's CI is not a valid test (§6, §9) |
| Claiming a fixed target is met | require the **whole two-sided 95% CI** at or beyond the target (conservative, α = .025); for a one-sided α = .05 call, use the 95% one-sided lower bound (= the 90% two-sided CI limit) | a point estimate past the target is not enough — the interval must clear it (§6, worked case) |
| Workload / safety-critical operator load | hand off to **`human-factors/`** (NASA-TLX and beyond) | this guide owns discretionary usability, not operator safety |

---

## Common Confusion Points

**"SUS is a percentage — 72 means 72% good."** No. SUS is a *scaled* 0–100 score; the
×2.5 in the formula rescales, it does not create a percentage. ~68 is the empirical
average, so 72 is roughly average-plus, interpreted against norms (Bangor/Sauro), never
as "72% of users satisfied" (§5.1).

**"Five users is the magic number, always."** No. Five users find ~85% of problems
*with average detection rate ~0.31, in one homogeneous segment, on a focused flow*
(Nielsen & Landauer 1993) — a **discovery** result. Large/heterogeneous systems, rare
problems, and multiple segments all break it, and it says nothing about measuring a rate
(§6).

**"The heuristics are the rules; a passing review means it's usable."** No. Nielsen's
ten are experience-based **rules of thumb**, not empirical laws, and one evaluator misses
~two-thirds of problems. Inspection generates *hypotheses*; users confirm them (§2, §8).

**"An A/B test tells us why the new design is better."** No. A/B tests measure *how
much* a metric moved and attribute it causally to the change — they are blind to
*mechanism* and to low-frequency users. Pair them with qualitative methods for *why*
(§7).

**"Think-aloud gives us the real task times and the true reasons."** Partly. Concurrent
verbalization can slow and rationalize behavior (reactivity), so don't report its times
as performance, and treat stated reasons as hypotheses over the harder behavioral signal
(§4).

**"Statistically significant, so it's an important usability improvement."** No.
Significance is about *detectability given n*, not *magnitude* or *user impact*; with a
huge A/B sample a trivial change is "significant." Effect size and practical importance —
and the whole inferential apparatus — are `statistics-applied/`'s to quantify; this guide
insists you separate *detected* from *big enough to matter* (§6, §7).

**"We measured usability, so we know the design is good."** A score is one instrument's
reading in one context on one sample. Usability is effectiveness *and* efficiency *and*
satisfaction *for specified users, tasks, and contexts* (ISO 9241-11); a great number on
the wrong tasks or the wrong segment is a false positive (§5, worked case).

---

## Global, WEIRD, and Resource Caveats

- **The method canon is WEIRD-sampled.** Most usability methods were validated on
  Western, educated, tech-literate, English-speaking convenience samples (the "WEIRD"
  critique, Henrich et al. 2010). Think-aloud assumes a cultural comfort with narrating
  thoughts to a stranger that is not universal; the "5 users / λ≈0.31" figure comes from
  a specific research lineage and does not transport unexamined to other populations or
  task cultures.
- **Instruments carry a language and a norm base.** SUS was written and normed in
  English; translated versions exist but need their own validation, and the ~68 mean is a
  norm over particular (largely Western, software) studies, not a human constant.
  Adjective anchors and grade curves inherit the same provenance.
- **Method access is resource-dependent.** Labs, eye-trackers, moderized-testing tools,
  and A/B experimentation platforms with the traffic to power an experiment are
  resource-rich-organization assets. Remote/unmoderated testing widens reach but adds
  selection bias (who has the device/bandwidth/literacy to participate) and removes the
  observation that catches *why*.
- **Segments are not a monolith and defaults hide people.** The *Tessera* international-
  filer stall is the general lesson: a sample drawn from the dominant segment
  systematically under-measures minority and edge users, and an aggregate metric (A/B,
  SUS mean) can look healthy while a definable group fails. Sizing discovery *per
  segment* and reporting *who* was and wasn't in the sample is the correction — and it is
  also the seam to `08-ACCESSIBILITY-INCLUSIVE-DESIGN`, where the excluded segment is
  disabled users and the method extends to accessible, AT-inclusive evaluation.

---

## A Contrasting Evaluation Example (non-WEIRD, low-resource)

*Fictional, to show how the same plan changes when the population and context are not
the WEIRD default. It is the deliberate counter-case to the (Western, office-software)
*Tessera* case above.*

**System.** *Saheli*, a fictional agricultural-advisory service delivered mainly over a
voice/IVR line and a low-end Android app to smallholder farmers in a rural, multilingual
region: intermittent 2G, mostly oral language use, low text literacy in the app's
default language, and little prior exposure to being "usability-tested."

**What breaks if you copy the *Tessera* plan wholesale.**
- **Think-aloud does not transport.** Concurrent narration of one's reasoning to a
  stranger is a WEIRD-lab convention; here it can read as rude, exam-like, or simply
  unanswerable, and it can silence the very users you need. Substitute in-context
  observation with a trusted local facilitator, a retrospective walk-through in the
  participant's own language, and success judged by *observed* completion.
- **Instruments need re-norming, not just translating.** A translated SUS is not a
  validated SUS, and the ~68 mean is Western-software-derived. Prefer observed
  effectiveness/efficiency and an orally-delivered task-ease question; treat any
  satisfaction number as **un-normed** for this population rather than comparing it to
  the Western benchmark.
- **"5 users / λ≈0.31" is even shakier.** Dialect, literacy, device, and connectivity
  define several distinct segments; each needs its own discovery sessions, and
  low-salience problems hide worse under this much between-user variance.
- **The channel *is* the study.** Evaluate on the real device and bandwidth (2G,
  feature-phone/IVR), because a lab tablet on office Wi-Fi measures a system these users
  never touch — an ecological-validity failure, not a detail.

**Reading.** The two *axes* (formative/summative × analytic/empirical) still hold; the
*methods, instruments, sample frame,* and even the notion of a comparable "score" change
with the population and context — Section 1's fit factors (population, ecological
validity, constraints) made concrete. Reporting *who* was in the sample, in which
language and on which device, is part of the result, not a footnote.

---

## Guide-Family Scaling Contracts (how this discipline extends)

This guide is a **prototype**; its evaluation discipline is meant to scale to the rest of
the module without becoming the same guide eleven times. Because what "evaluation" means
shifts with the object, each guide family inherits a *bounded* contract, not a copy of
this one — and each states the object being judged and the **test that would fail it**, so
it is checkable, not a slogan:

- **Overview (`00`).** Not a usability object; checked for **coverage and boundary
  integrity**. *Test:* every concept the module owns appears in exactly one guide, and the
  ownership/defer matrix has no gap and no overlap (each owned area claimed once, each
  defer target named once). *Fails if* a boundary claim in `00` contradicts a guide, or an
  owned concept is unclaimed or double-claimed. Summative task/CI machinery does not apply.
- **History (`01`).** Not evaluated for usability at all: its claims are historical and
  are judged by **sourcing and dating** (attributed, bounded), never by task success or
  CIs. *Test:* every load-bearing historical claim carries an attribution and a date.
  *Fails if* it imports summative machinery (completion rates, CIs) where it does not
  belong.
- **Interaction models (`02`).** Models are **diagnostic instruments**, not ornaments, and the
  **empirical test must match each model's unit of analysis**. *Test:* individual-level models
  (Norman's stages/gulfs, modes, instrumental interaction; GOMS/KLM as applied) localize a real
  breakdown to a **specific step and gulf** (execution vs evaluation) a think-aloud (§4) could
  confirm or leave unresolved; **system-level lenses** (distributed cognition, activity theory)
  instead predict a **coordination/system breakdown** confirmed by a **field study** (`06`) and
  measured with `09`'s group outcomes, and need **not** map to one gulf. *Fails if* a model cannot
  fail a prediction, a system-level claim is "tested" with a single-user think-aloud (or a
  single-user gulf claim is deferred to a field study), or a model re-derives the psychophysical
  mechanism `cognitive-science/` owns instead of applying it.
- **I/O modalities (`03`).** Modality claims are **performance claims**, carried under
  this guide's discovery-vs-measurement discipline. *Test:* every throughput/error/time
  comparison names its estimator and exposes *n* (§6), and Fitts/Hick appear only as
  **cited, device- and population-bounded** applied laws (derivation deferred to
  `cognitive-science/09`). *Fails if* a "law" is undated or universalized, or a benchmark
  is reported without its sample and estimator.
- **Design process (`04`).** Its generative outputs (personas, scenarios, prototypes) are
  **hypotheses, not results**. *Test:* every design claim ("this persona is right," "this
  flow is clearer") stays **unresolved until an evaluation in `05` confirms it**, and
  prototype fidelity matches the question asked. *Fails if* a design is "validated" only by
  its own artifacts, with no evaluation.
- **Research methods (`06`).** Surveys, controlled experiments, diary/experience
  sampling, interviews, ethnography, and mixed methods each carry their own
  inferential and validity contract. *Test:* the method, sampling frame, estimator or
  qualitative paradigm, missingness/reactivity risk, and integration logic are named;
  quantitative comparisons use an appropriate difference estimate, while qualitative
  work uses the quality criteria of its declared paradigm. *Fails if* a convenience
  sample is generalized without a coverage argument, a diary is treated as passive
  ground truth, or κ is bolted onto reflexive analysis.
- **Socio-technical systems / CSCW (`09`).** Groupware claims must measure both the
  individual interaction and the coordination system: awareness, common ground,
  handoff cost, participation distribution, and organizational adaptation. *Test:* at
  least one outcome captures group/system behavior, the unit of analysis matches the
  claim, and field evidence bounds transfer across organizations. *Fails if* an
  individual SUS score is used as proof of team effectiveness, network effects are
  inferred from one group, or social outcomes are reduced to interface clicks.
- **Combined IA / visualization (`07`).** Its object (findability, navigation, visual
  encodings) is evaluated with *this* guide's methods pointed at comprehension and task
  success (tree-testing, first-click, encoding-comprehension tasks) — the closest scaling
  of Section 5's metric triad. *Test:* the same discovery-vs-measurement and
  difference-test discipline holds. *Fails if* a comprehension score is read as a
  measurement off a discovery sample.
- **Emerging tech (`10`).** AR/VR/agentic/BCI prototypes demand the *hype-vs-evidence*
  discipline: novelty effects, tiny self-selected samples, and instruments unvalidated for
  the new modality mean most numbers are **unresolved by construction**. *Test:* such
  numbers are reported as unresolved and the guide stays formative until an instrument is
  validated. *Fails if* a novelty-inflated metric is reported as a settled effect.
- **Ethics (`11`).** Evaluated against value and harm, not a metric to maximize; the A/B
  metric-selection caveat (Section 7) generalizes. *Test:* no recommendation optimizes a
  number that is the wrong thing to move. *Fails if* "we moved the number" is offered as a
  defense of a harmful design.
- **Accessibility & safety invariants (propagated from `08`, riding every family above).**
  Two invariants travel with all of the above, whatever the method. (1) *Accessibility of
  the sample* — disabled users and their assistive technology are a **first-class
  segment**, sized per segment (§6), not a final-audit afterthought (the `08` §7
  discipline); a sample that silently excludes them is **under-powered for the population,
  not "done."** (2) *Safety/ethics floor* — no manipulation/dark-pattern playbook, no
  legal/compliance ruling, no safety-certification; **conformance is a floor, not
  usability** (`08` §6); where failure risks harm, operator-safety analysis defers to
  `human-factors/` and legal obligation to `law/`. *Fails if* a family trades either
  invariant away, whatever its numbers.

The invariant across every family: **name the method, expose the inputs, separate
discovery from measurement, state who and what the sample did and did not cover — and
carry the `08` accessibility and safety/ethics invariants into all of it.** That invariant
— not any single number — is the pattern the prototype is meant to prove.
