---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-factors:cognitive-workload-situation-awareness
kind: guide
module: human-factors
section: human-factors
title: Cognitive Workload & Situation Awareness - Measuring the Operator in Context
status: source-custody
source_custody: partial
current_path: human-factors/03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md
canonical_path: human-factors/03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md
backsource_ids: [mdloom-backfill:human-factors:03-cognitive-workload-situation-awareness]
concepts: [cognitive-workload, multiple-resource-theory, nasa-tlx, situation-awareness, sagat, vigilance, attentional-tunneling, distributed-situation-awareness]
root_concepts: [cognitive-workload, situation-awareness]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Cognitive Workload & Situation Awareness — Measuring the Operator in Context

**This guide owns** the *measurement and design of the operator's mental state in an
operational context*: **cognitive workload** as supply-vs-demand of attention (multiple
resource theory), the **workload–performance dissociation**, and the three measurement
families — **subjective (NASA-TLX raw vs weighted, and its limits)**, **performance
(primary/secondary/embedded task)**, and **physiological (cardiac, pupil, ocular, EEG)**;
the **vigilance decrement**; **situation awareness (SA)** as an *applied* three-level
framework and, centrally, **how SA is measured** (SAGAT, SPAM, SART) **and the scientific
critiques of the construct**; the failure modes of **attentional tunneling / change
blindness / out-of-the-loop**; and **team and distributed SA**. **It builds on**
`02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS` (fatigue and environment as load modifiers) and
feeds `06` (displays that hold SA), `07` (automation as a workload/SA problem), and
`10-METHODS-AND-MEASUREMENT` (study design). **It explicitly defers**: the **cognitive
mechanisms** — why attention, working memory, and perception behave as they do, and the
psychophysical "laws" (Fitts, Hick, Miller, cognitive-load theory) and the SA/NDM
cognitive theory — to [`cognitive-science/`](../cognitive-science/09-APPLIED-BRIDGE.md) (especially
`cognitive-science/09-APPLIED-BRIDGE`, which owns Endsley's SA *as a cognitive model* and Klein's
recognition-primed decision making); **general digital-interface usability** to
[`human-computer-interaction/`](../human-computer-interaction/00-OVERVIEW.md);
**inferential statistics** to [`statistics-applied/`](../statistics-applied/00-OVERVIEW.md); and
**safety-critical integration, error taxonomy, and hazard analysis** to `04`, `05`, and `08`.

> **Safety & ethics contract (binds every human-factors guide).** This is an
> **educational systems reference**, not an operations manual. It provides **no
> operational instructions**, **no safety certification** (no method here certifies an
> operator, a workload level, or a control room as "safe"), **no accident or legal
> determination**, and **no individual fitness-for-duty or clinical assessment**. Every
> workload index and SA score below is a **bounded, context-relative measurement**, useful
> mainly for *within-design comparison* — never an absolute verdict about a person or a
> system.
>
> **Cross-cutting accessibility invariant.** SA is built from *perceived* cues, so a
> safety-relevant cue carried on a **single** channel (color or tone alone) simply fails to
> reach any operator who cannot use that channel — degrading their Level-1 SA by design.
> Safety-relevant cues must therefore ride on **≥2 coding channels**, the operator-safety
> twin of accessibility's "never color alone"
> ([`06` §3](06-DISPLAY-CONTROL-INTERFACE-DESIGN.md), where it is owned); measurement must
> sample the operators for whom a one-channel cue fails ([`10`](10-METHODS-AND-MEASUREMENT.md)).

*Per-guide banner: workload and SA are **constructs measured by proxy**. Every instrument
here (TLX, SAGAT, an EEG index, a pupil diameter) is a dated, validated-in-a-context proxy
with known confounds, not a direct readout of the mind. Treat scores as comparative
evidence, attributed and bounded, never as universal constants.*

---

## The Big Picture: Two Constructs — Supply of Attention, and Model of the Situation

Human factors asks two different questions about the operator's head, and they are easy to
conflate. **Cognitive workload** is about *supply vs demand*: how much of a limited
attentional resource the task consumes, and how much reserve is left. **Situation
awareness** is about *content*: how accurate and complete the operator's internal model of
the situation is — what is happening (perception), what it means (comprehension), and what
happens next (projection). They interact — high workload degrades SA, poor SA raises
workload — but they are **distinct constructs measured by different instruments**, and
conflating them is the classic beginner error.

```
THE OPERATOR IN CONTEXT   (this guide owns the MEASUREMENT + DESIGN, not the mechanism)
================================================================================
   task DEMAND ---> [ limited attentional RESOURCES ] ---> PERFORMANCE
        ^                    |  (multiple pools)                ^
        |                    v                                  |
   environment          WORKLOAD: demand-vs-supply         SITUATION AWARENESS
   (heat, noise,        (schematic; how much reserve?)     (how good is the operator's
    time pressure)                                          model of what's going on?)

   WORKLOAD  measured by:  subjective (NASA-TLX) | performance (2nd task) | physiological
   SA        measured by:  freeze-probe (SAGAT)  | real-time probe (SPAM) | self-rate (SART)

   MECHANISM (why attention/memory behave this way) -> cognitive-science/09  (DEFERRED)
   THIS GUIDE -> measure workload & SA in real operational context, and design for them.
================================================================================
```

The layers below take each construct in turn: workload (its theory, its
dissociation from performance, its three measurement families) and SA (its levels, its
measurement, its critiques, its failure modes, and its team/distributed forms), then the
boundaries, a worked case, and the reader aids.

---

## 1. Workload Is Supply vs Demand — Multiple Resource Theory

The naive model treats attention as a **single** pool: one tank that any task drains. It
predicts that two tasks interfere in proportion to their combined difficulty — and it is
wrong in a specific, useful way. Wickens' **Multiple Resource Theory (MRT, 1984/2002)**
says attention is **several partly-separate pools**, so *two tasks interfere more when they
draw on the same pool and less when they draw on different pools.* That is why you can
drive (visual–manual–spatial) while talking (auditory–vocal–verbal) more easily than while
texting (visual–manual–spatial — a direct collision).

```
MULTIPLE RESOURCE THEORY  (Wickens) -- 4 dimensions of separate-ish resource pools
--------------------------------------------------------------------------------
   STAGE (processing):     perception/cognition   vs  responding
   MODALITY (perceptual):  visual                 vs  auditory
   VISUAL CHANNEL:         focal (detail/reading)  vs  ambient (motion/orient)
   CODE (processing):      spatial                vs  verbal

   Response modality (manual vs vocal) is a RELATED but separate OUTPUT distinction
   that maps onto the CODE dimension -- treat it alongside, not as a 5th pool. The
   four Wickens dimensions are STAGE, perceptual MODALITY, VISUAL CHANNEL, and CODE.

   PREDICTION: two concurrent tasks interfere MORE the more dimensions they SHARE.
      drive (visual-spatial) + talk (auditory-verbal)   -> low interference
      drive (visual-spatial) + text (visual-spatial)    -> HIGH interference
      steer by peripheral flow (visual-AMBIENT) + read a gauge (visual-FOCAL)
                                                        -> less than two FOCAL tasks

   DESIGN LEVER: offload a saturated channel onto a free one
      (e.g., an auditory alert when the eyes are saturated) -- but only if the FREE
      channel is truly free; adding audio into an auditory-saturated cockpit backfires.
```

The *why* — the cognitive architecture that makes these pools partly separate — is
`cognitive-science/`'s. This guide owns the **applied consequence**: how to predict and
redistribute load across channels in a real task, and how to measure the result.

---

## 2. Workload ≠ Performance — The Dissociation

The costliest mistake in workload work is reading **performance** as a workload gauge.
They dissociate, because operators **defend performance by spending reserve capacity**.

```
THE PERFORMANCE-RESOURCE FUNCTION  (schematic -- positions are task-dependent)
--------------------------------------------------------------------------------
   performance
      ^     region A: RESERVE      region B: near the "redline"
      |     (adding load does      (reserve exhausted; more load
      |      not hurt output --      -> performance drops steeply)
      |      output is FLAT)                   ______
      | ________________________             /      \  overload
      |/                        \___________/         \____ performance collapses
      |
      | region C: UNDERLOAD (too little demand -> boredom,
      |           mind-wandering, vigilance loss -- ALSO bad)
      +-------------------------------------------------> task demand / load
   SCHEMATIC: the curve shape, and where the "redline" sits, depend on TASK,
   STRATEGY, expertise, and CONTEXT -- there is NO universal redline value.
   Reusable point: in region A performance is FLAT while load CLIMBS, so output
   reads "fine" until the drop-off -- measure the RESERVE, not just output.
```

Two consequences: (1) **overload and underload both hurt** — the relationship is an
inverted-U, so a bored monitor (region C) and a saturated operator (region B) are both
failure states; (2) **primary-task performance is only diagnostic near the redline** — on
the flat part it is blind to rising load, which is exactly why the secondary-task and
physiological families exist (§3). "They completed the task, so workload was fine" is a
non-sequitur.

---

## 3. Measuring Workload — Three Families, Each Bounded

There is no workload thermometer. Three families triangulate it, each with a different
blind spot; a strong design uses more than one.

```
THREE WORKLOAD MEASUREMENT FAMILIES  (triangulate -- none is ground truth)
--------------------------------------------------------------------------------
   SUBJECTIVE       operator RATES experienced load     NASA-TLX, SWAT, Bedford
     + cheap, face-valid, integrates everything         - retrospective, subjective,
                                                           dissociates from performance
   PERFORMANCE      spare capacity via a TASK            primary; secondary/loading;
     + behavioral, continuous                              embedded secondary task
                                                         - primary blind on the flat part;
                                                           secondary can be intrusive
   PHYSIOLOGICAL    body correlates of effort/arousal    HR, HRV, pupil, blink, EEG
     + continuous, non-intrusive-ish, no task stop      - SENSITIVE but NON-SPECIFIC;
                                                           confounded by motion/emotion/light
```

- **Performance family.** *Primary-task* measures the task of interest (diagnostic only
  near the redline). *Secondary-task* adds a low-priority loading task whose decline
  reveals spare capacity — powerful but intrusive. *Embedded secondary task* uses a
  naturally-occurring low-priority duty as the probe, reducing intrusiveness.
- **Physiological family.** Heart rate rises and **heart-rate variability falls** with
  load; **task-evoked pupil dilation** rises with cognitive effort (Beatty); blink rate/
  duration and eye-scan patterns shift; **EEG** engagement indices move (frontal theta up,
  alpha down). All are **sensitive but non-specific** — they track *effort/arousal*, not
  workload uniquely, and are confounded by physical exertion, emotion, lighting, and
  individual differences. They need **baselining** and careful controls.

### 3.1 NASA-TLX — Raw vs Weighted, and the Limits

The **NASA Task Load Index (Hart & Staveland, 1988)** is the most-used subjective
instrument. It is multidimensional: six subscales rated 0–100.

```
NASA-TLX  (Hart & Staveland, 1988)
--------------------------------------------------------------------------------
   SIX SUBSCALES (each rated 0-100, fine gradations):
      Mental Demand | Physical Demand | Temporal Demand
      Performance   | Effort          | Frustration

   WEIGHTED TLX (original):
      15 pairwise comparisons ("which contributed more to YOUR workload?")
      -> per-source weights -> weighted average across the six subscales.
   RAW TLX / RTLX (Byers/Bittner; Hendy):
      DROP the 15 comparisons; just AVERAGE the six subscales.
      Often correlates ~as well or better; the weighting step is frequently omitted.
   WHAT THE NUMBER IS: a within-subject, comparative index of EXPERIENCED load,
      collected AFTER the task. It is NOT an absolute, cross-person, or cross-study
      constant, and combining six sources into one score DISCARDS the profile.
```

**Limits to state whenever a TLX is quoted:** it is (1) **retrospective** — rated after
the task, subject to memory and peak/end effects; (2) **subjective** — anchored
differently by different people, so best for *within-subject / within-design* comparison,
weak for absolute or cross-population claims; (3) **a scalar from a vector** — one number
hides which of the six sources drove it, so report the **subscale profile**, not just the
composite; (4) **dissociable from performance and from physiological load** (§2). Raw vs
weighted rarely changes the conclusion, but the choice, the *n*, and the subscale profile
should always be reported.

---

## 4. Vigilance & the Vigilance Decrement

Sustained monitoring for **rare** signals is a distinct, underload-flavored problem.
Mackworth's **Clock Test (1948)** — modeling WWII radar watch — showed detection of rare
deflections **declines within ~20–35 minutes**: the **vigilance decrement**.

```
THE VIGILANCE DECREMENT  (sustained attention to rare signals degrades over time)
--------------------------------------------------------------------------------
   detection rate
      ^  high  \___
      |            \_____ decrement sets in ~20-35 min (task-dependent)
      |                  \________________
      |                                    \____ misses rise, latency grows
      +----------------------------------------------> time on watch
   PARADOX: low event rate feels like LOW load but is COGNITIVELY DEMANDING to sustain.
   COMPETING ACCOUNTS (mechanism deferred to cognitive-science):
      resource-depletion  (watch drains a finite resource) vs
      mindlessness/underload (too little to do -> disengagement)
   HF STUDYING IT (offline, not live): characterize the decrement OFFLINE, via
      SIMULATION or REPLAY of recorded signals, or DESCRIPTIVE detection-vs-time
      measurement -- NOT by injecting signals into a live watch or altering
      shift rotations. Automation MONITORING is a vigilance task (guide 07:
      humans are poor rare-event monitors of reliable automation); candidate
      mitigations (salience, keeping the human in the loop) are design
      HYPOTHESES to validate, not prescriptions.
```

The systems point: automating a task and leaving the human to *monitor* it converts an
active task into a vigilance task — one humans are demonstrably poor at — which is a core
tension of guide 07.

---

## 5. Situation Awareness — The Three-Level Applied Framework

**Endsley's model (1988/1995)** decomposes SA into three levels. `cognitive-science/09`
owns this model **as cognitive theory** (the perception/comprehension/projection mechanism);
**this guide owns it as an applied scaffold for measurement and design in context.**

```
SITUATION AWARENESS -- three levels  (applied scaffold; mechanism -> cognitive-science/09)
--------------------------------------------------------------------------------
   LEVEL 1  PERCEPTION     detect the relevant elements
            "traffic is converging; tank 2 is at 80%; queue is growing"
   LEVEL 2  COMPREHENSION  understand what they MEAN, together, now
            "converging + our speed = conflict in 90s"; "80% + inflow = overfill soon"
   LEVEL 3  PROJECTION     predict the near-future state
            "if unchanged, separation is lost in 90s"; "overflow in ~4 min"

   SA ERRORS map to levels:  L1 = didn't perceive (not displayed / not scanned)
                             L2 = perceived but misunderstood (wrong mental model)
                             L3 = understood but mis-projected (wrong prediction)
   DESIGN MAPPING: displays for L1 (make elements perceptible), integration/decluttering
      for L2 (show relationships, not just data), trend/predictive cues for L3.
```

The three levels are useful precisely because **SA errors localize to a level**, which
tells you *where* to intervene (a missed indicator is a display/scan problem; a
misinterpretation is a comprehension/training problem). But the levels are an applied
scaffold, not a proof that SA is a single thing in the head — which §6 takes head-on.

---

## 6. Measuring SA — SAGAT, SPAM, SART, and the Critiques

Measuring "what the operator knows about the situation" is genuinely hard, and the field
is not settled. Three measurement approaches, then the critiques you must carry.

```
SA MEASUREMENT APPROACHES  (each trades intrusiveness against directness)
--------------------------------------------------------------------------------
   SAGAT (Endsley) -- FREEZE-PROBE:
      freeze the simulation, BLANK the displays, query L1/L2/L3 elements,
      score against SIMULATOR GROUND TRUTH. Objective + level-specific.
      - needs a simulator; intrusive (freezes); samples MEMORY at the freeze instant.
   SPAM (Durso) -- REAL-TIME PROBE:
      ask a query WITHOUT freezing; measure RESPONSE LATENCY (and accuracy).
      assumes good SA = fast answer (know it, or know where to look).
      - less intrusive; but latency CONFOUNDS with workload and with display search.
   SART (Taylor) -- SELF-RATING:
      operator rates own SA (demand/supply/understanding) after the task.
      - cheap; but subjective, retrospective, and CONFOUNDS SA with workload/confidence
        (people can feel aware while being wrong).
```

**The critiques (carry them — they are legitimate science, not dismissals).** Dekker,
Hollnagel, and Flach argue SA risks being a **folk/circular construct**: if "loss of SA"
is *inferred from* a bad outcome and then offered *as the cause of* that outcome, it
explains nothing ("the crash was caused by loss of SA" — but we only "know" SA was lost
because it crashed). Related concerns: **product vs process** — SAGAT measures SA as an
in-the-head *product* (a snapshot at a freeze), while critics argue awareness is an ongoing
*activity* distributed across people and artifacts (§8); and the **ground-truth assumption**
— scoring against "the true situation" presumes a single correct world-model the analyst
has and the operator should match. The defensible position: SA and its measures are
**useful design and evaluation tools** with a clear validity domain, **not** a mystical
inner quantity and **not** a licence to label an outcome and stop investigating. Where an
event must be analyzed, the causal account belongs to the error/hazard methods of `04`,
`05`, and `08`, not to "they lost SA."

---

## 7. Failure Modes — Attentional Tunneling, Change Blindness, Out-of-the-Loop

Workload and SA fail in patterned ways worth naming, because designs cause them.

```
CHARACTERISTIC ATTENTION/SA FAILURES
--------------------------------------------------------------------------------
   ATTENTIONAL TUNNELING   locking onto one channel/hypothesis, dropping the scan of
     (Wickens)             others -- "cognitive tunneling"; worsens under stress and
                           with compelling but narrow displays. (Classic: a crew fixates
                           on one indicator while the real problem sits unwatched.)
   CHANGE BLINDNESS        a change goes unnoticed when it happens off-fixation or across
                           a transient -- a mode switch or a state change with no salient
                           transition cue is easily missed. (Ties to guide 06 salience.)
   OUT-OF-THE-LOOP (OOTL)  after long automation monitoring, the human is slow to detect
                           automation failure and rebuild SA to intervene -- degraded SA
                           + manual skill + a vigilance deficit. (Core to guide 07.)
   DESIGN RESPONSE: salient state/mode cues, integrated (not raw) displays, attention
     direction that does not itself tunnel, and keeping the human meaningfully in the loop.
```

These are the **design-facing** payoff of the constructs: tunneling argues for
attention-guiding but non-capturing displays; change blindness argues for salient
transition cues (guide 06); OOTL argues against "monitor the automation" designs (guide 07).

---

## 8. Team & Distributed SA

Real operations are teams plus machines, and SA scales up in two competing framings.

```
INDIVIDUAL -> TEAM -> DISTRIBUTED SA
--------------------------------------------------------------------------------
   SHARED SA (Endsley & Jones):
      team members OVERLAP on the SA requirements they hold in common; "team SA" =
      the degree each member has the SA they individually need, plus shared elements.
      -> design shared displays, briefs, and callouts to align the overlap.
   DISTRIBUTED SA / DSA (Stanton, Salmon; after Hutchins' distributed cognition):
      SA is a property of the WHOLE SYSTEM -- people AND artifacts (displays, strips,
      logs) -- held in "SA transactions" between agents. Agents need COMPATIBLE (not
      identical) SA suited to their role; a paper strip or a screen literally HOLDS SA.
   IMPLICATION: a display is not just an input to one head's SA -- it is a system MEMORY
      that carries SA between people and shifts. (Seam: guide 06 displays; guide 07
      automation-as-agent; cognitive-science distributed cognition for the theory.)
```

The distributed view is also the cleanest answer to §6's product/process critique: if SA
lives in transactions across people and artifacts, then measuring one operator's freeze
recall is necessarily partial, and the design target is the **system's** awareness, not
just an individual's.

---

## The Boundaries (ownership in one place)

```
WHO OWNS WHAT
--------------------------------------------------------------------------------
   cognitive-science/09     MECHANISM: why attention/memory/perception behave so; the
                            psychophysical laws; Endsley SA as COGNITIVE THEORY; NDM/RPD.
   human-factors/03 (here)  MEASUREMENT + DESIGN in operational context: workload & SA
                            instruments, their limits, failure modes, team/distributed SA.
   human-computer-interaction/  general DIGITAL-interface usability & evaluation methods.
   statistics-applied/      inference behind any workload/SA experiment.
   human-factors/06         the DISPLAYS/CONTROLS that support SA and manage load.
   human-factors/07         AUTOMATION as a workload/SA/OOTL problem.
   human-factors/05, /08    turning a workload/SA finding into error/reliability/hazard
                            analysis -- and NO safety certification lives anywhere here.
```

---

## A Worked Quantitative Pass — Discordant TLX, Performance & SA (synthetic)

*All numbers are **synthetic**, chosen so the arithmetic is reproducible by hand. This
demonstrates how the instruments dissociate; it is **not** a real study, a
certification, or a judgment about any operator or console.*

**Setting.** In a fictional trial, `n = 12` operators each run the same converging-fault
scenario on the **Old (A)** and **New (B)** console. To keep the arithmetic reproducible by
hand, this pass **follows one representative participant (P)** through both consoles and
shows P's full computation; aggregating all twelve (with the *same* weighting) and testing
whether the differences are real is **`statistics-applied/`'s** job, not this guide's. Five
measures are collected, spanning **three measurement families**: one subjective instrument
(NASA-TLX, reported as raw and weighted scoring outputs), performance (primary and
secondary-task measures), and a situation-awareness probe (SAGAT). They are *not* one
homogeneous set, and reading them as if they agreed is the trap.

### Compute the two NASA-TLX composites for participant P (both consoles, in full)

NASA-TLX weights are elicited **once** from P (each subscale's win-count over the 15 pairwise
comparisons, summing to 15) and applied to **both** conditions, so any raw-vs-weighted move
comes from the ratings, not from re-weighting. P's six subscale ratings (0–100) and the
common weights:

| Subscale | Weight (P) | Rating A | Rating B | A x W | B x W |
|---|---|---|---|---|---|
| Mental Demand | 5 | 56 | 65 | 280 | 325 |
| Physical Demand | 0 | 40 | 20 | 0 | 0 |
| Temporal Demand | 3 | 52 | 58 | 156 | 174 |
| Performance | 1 | 42 | 35 | 42 | 35 |
| Effort | 4 | 60 | 70 | 240 | 280 |
| Frustration | 2 | 45 | 45 | 90 | 90 |
| **Sum** | **15** | (295) | (293) | 808 | 904 |

- **Raw TLX (RTLX)** = mean of the six ratings: A = `295 / 6 = 49.2`, B = `293 / 6 = 48.8`.
- **Weighted TLX** = `sum(rating x weight) / 15`: A = `808 / 15 = 53.9`, B = `904 / 15 = 60.3`.

Raw says the two consoles feel **about the same** (49.2 vs 48.8), but weighting — identical
across conditions — **separates** them (53.9 vs 60.3) because B's load concentrates in the
**heavily weighted** sources (Mental Demand, Effort, Temporal Demand) while A carries more of
its raw score in **zero-weighted** Physical Demand. Raw vs weighted is **not** a rounding
difference here: it moves B's number by ~11 points and flips "about equal" into "B clearly
heavier."

### The five measures/outputs, both consoles (participant P)

| Instrument (converging-fault scenario) | Old (A) | New (B) | Naive reading of B alone |
|---|---|---|---|
| RTLX (raw, 0–100; lower = lighter) | 49.2 | 48.8 | "New feels about the same" |
| Weighted TLX (0–100) | 53.9 | 60.3 | "New is clearly heavier" |
| Primary task (faults resolved, %) | 90 | 92 | "New performs fine" |
| Secondary-task decrement (added RT, ms; higher = less reserve) | 120 | 210 | "New leaves far LESS reserve" |
| SAGAT Level-2 comprehension (% correct) | 70 | 55 | "New SA is WORSE" |

### The discordance, and how to read it

The instruments **disagree**: for P the New console *feels* about the same on raw TLX,
scores **clearly heavier** once weighted, performs **equally well on the primary task**, yet
leaves **much less reserve** (secondary-task decrement 120 -> 210 ms) and yields **worse
Level-2 SA** (70% -> 55%). At least three readings are defensible, and the guide's job is to
hold them open, not to pick a winner by one number:

1. **Dissociation reading (§2).** The New console genuinely raises hidden load and degrades
   comprehension; the good primary-task score is **bought with reserve** the operator will
   not have during a real upset. On this reading, "operators coped and felt fine" is exactly
   the trap — do **not** ship on RTLX.
2. **Instrument reading (§3.1, §6).** SAGAT freezes may disrupt the New workflow
   differently; the secondary task may be more intrusive on B; RTLX is retrospective; and P
   is a **single representative participant** of a small, untested twelve-operator sample. On
   this reading the result is **unresolved**, not proven — confirm before concluding.
3. **Profile reading (§3.1).** Report the **six-subscale profile** (Mental/Temporal/Effort
   dominate), the *n*, and raw-vs-weighted — not a single composite — and route any
   safety-consequence claim to `05`/`08`. A scalar cannot rank the consoles.

**Uncertainty / validity notes.** Every figure here is **one representative participant's**
within-scenario comparative reading — not a group result; aggregating the twelve and running
any inferential test is `statistics-applied/`'s, not this guide's. TLX is retrospective and
anchor-dependent; SAGAT samples memory at a freeze against a simulator's ground truth; the
secondary-task and physiological confounds of §3 all apply. Nothing here certifies a console
or judges an operator.

---

## A Fully Worked Case — Measuring Load and SA in a Redesign (illustrative, fictional)

*Fictional throughout; a demonstration of method, not an operational study, not a
certification, and not a judgment about any real operator or system.*

**Setting.** *Kestrel Grid* (invented) is trialing a new **network-operations console**.
The question to human factors: *does the redesign lower operator workload and improve SA
during a converging-fault scenario — and how would we even know?*

1. **Separate the two constructs (Big Picture).** The team writes two hypotheses — a
   *workload* hypothesis (redesign lowers load at the same demand) and an *SA* hypothesis
   (redesign improves comprehension of converging faults) — and refuses to let "operators
   coped" (a performance statement) stand in for either.
2. **Triangulate workload (§3).** They collect **RTLX** after each scenario (reporting the
   **six-subscale profile**, not just the mean), an **embedded secondary task** (a
   low-priority acknowledgement duty) for spare capacity, and **pupil + HRV** with a rest
   baseline. When RTLX drops but the secondary-task and pupil measures say load is
   unchanged, they treat the dissociation (§2) as a finding, not noise — perhaps operators
   *feel* better without more reserve.
3. **Measure SA at levels (§5–6).** In the simulator they run **SAGAT** freezes probing
   L1 (which tanks/links are degraded), L2 (is this a converging fault?), and L3 (what
   fails next) against ground truth, and cross-check with **SPAM** latencies in a
   no-freeze condition. A gain concentrated at **L2** points at the integration/decluttering
   change; an L1 gap points back at display salience (guide 06).
4. **Watch for failure modes (§7).** They check whether the new alerting **tunnels**
   attention onto the first fault while a second grows unwatched, and whether a mode change
   in the console is missed (change blindness) — either would offset an SA gain.
5. **State the limits honestly (§6 critique).** The report says SAGAT samples memory at
   the freeze and scores against a simulator's ground truth; it does **not** conclude "the
   old console caused loss of SA," and it routes any safety-consequence question to `05`/
   `08`. Every number is framed as **within-trial comparative evidence**, with *n*,
   baselines, and confounds named.

**Reading.** Two constructs, three instrument families, level-specific SA probes, explicit
attention to dissociation and to the folk-construct trap — and not one sentence that
certifies the console or judges an operator.

---

## Reader Tasks (answerable from this guide)

1. **Predict dual-task interference across all four dimensions.** Using MRT's four
   dimensions (processing stage, perceptual modality, visual channel focal/ambient,
   processing code), say whether two concurrent tasks collide or coexist — include a
   visual-**focal** vs visual-**ambient** pair and explain why it interferes *less* than two
   focal tasks — then propose a channel offload and state when it backfires. (§1.)
2. **Refute "performance was fine, so workload was fine."** Using the §Q table (equal
   primary-task performance but a larger secondary-task decrement and worse SAGAT on the New
   console) and the performance-resource function, explain why primary output stays flat
   until the drop-off, and name the measure that reveals the spent reserve. (§2–3, §Q.)
3. **Compute both TLX composites.** For condition A — ratings MD 60, PD 25, TD 62, PF 32,
   EF 64, FR 52; weights TD 5, EF 4, MD 3, FR 2, PF 1, PD 0 — compute **RTLX** and
   **weighted TLX**, show they differ (`49.2` vs `58.8`), explain *why*, and state what else
   you must report with the composite (subscale profile, *n*, raw-vs-weighted). (§3.1, §Q.)
4. **Resolve the discordance.** Given the §Q result (New console *feels* lighter on RTLX but
   shows less reserve and worse Level-2 SA), give **two** defensible interpretations
   (dissociation vs instrument/underpowered), state the decision rule (don't collapse to one
   number; route safety to `05`/`08`), and name the folk-construct critique that keeps you
   from concluding "loss of SA." (§2, §6, §Q.)
5. **Diagnose a failure mode.** Given "the crew fixated on one alarm while a second fault
   grew," name attentional tunneling, distinguish it from change blindness and
   out-of-the-loop, and give the display/automation design response — routing the *safety*
   consequence to `05`/`08`. (§7.)

---

## Decision Cheat Sheet

| Situation | Move | Why (this guide) |
|---|---|---|
| Two tasks interfere badly | check **shared MRT pools**; offload to a free channel | interference scales with shared resources (§1) |
| "They finished, so load was fine" | reject; **measure reserve** (2nd task / physiology) | performance is flat until the redline (§2) |
| Operator seems bored/underloaded | treat as a **failure state** (vigilance risk) | inverted-U: underload also degrades (§2, §4) |
| Need a cheap workload read | **NASA-TLX (RTLX)** + report the **subscale profile** | subjective, within-subject, comparative (§3.1) |
| Need a continuous workload read | **pupil / HRV / EEG** with a **baseline** | sensitive but non-specific; confounded (§3) |
| Sustained rare-signal monitoring | expect a **vigilance decrement**; study it offline (sim/replay), don't inject live signals | low event rate is still high cognitive load (§4) |
| Need objective SA in a sim | **SAGAT** freeze-probe vs simulator ground truth | level-specific, objective, but intrusive (§6) |
| Need SA without freezing | **SPAM** latency probes | less intrusive; confounds with workload (§6) |
| Someone says "loss of SA caused it" | reject the **circular** explanation; go to `05`/`08` | SA is a design/eval tool, not a cause (§6) |
| Automation left human as monitor | expect **out-of-the-loop**; keep human in the loop | monitoring reliable automation is a vigilance task (§4, §7) |
| Team/multi-agent operation | design for **shared/distributed SA**; displays hold SA | SA is a system property, not one head (§8) |
| Certify a workload level or an operator | **out of scope** — no certification, no fitness call | safety contract, banner |

---

## Common Confusion Points

**"Workload and situation awareness are the same thing."** No. Workload is *supply vs
demand of attention*; SA is *the accuracy of the operator's model of the situation*. They
interact but are measured by different instruments; a lightly-loaded operator can have
terrible SA, and a heavily-loaded one can have excellent SA (§Big Picture, §2, §5).

**"Good task performance proves low workload."** No. Operators defend performance by
spending reserve capacity, so output stays flat while load climbs to the redline;
primary-task performance is diagnostic only near the cliff (§2).

**"NASA-TLX is an absolute workload score."** No. It is a **within-subject, comparative,
retrospective** index; anchoring differs by person, and one composite number hides the
six-source profile. Report raw-vs-weighted, *n*, and the subscales (§3.1).

**"Physiological measures read workload directly."** No. HRV, pupil, blink, and EEG track
*effort/arousal* and are **non-specific** — confounded by physical load, emotion, and
lighting. They need baselining and corroboration, not solo interpretation (§3).

**"Low event rate means low workload."** No. Sustained vigilance for rare signals is
cognitively demanding and shows a decrement within tens of minutes; automation monitoring
inherits this problem (§4, §7).

**"SAGAT gives the true SA."** No. It samples memory at a freeze and scores against a
simulator's ground truth — an objective, useful, but **partial and intrusive** proxy. And
"loss of SA" is not a causal explanation of an accident; it is a description that needs the
error/hazard methods of `05`/`08` (§6).

---

## Global, WEIRD & Resource Caveats

- **Instruments are validated in narrow populations.** TLX, SAGAT, SART, and most
  physiological indices were developed and validated largely with Western, often military
  or student, samples doing particular tasks. Norms and even subscale interpretations do
  not transport unexamined to other cultures, languages, or operator populations.
- **Self-report carries a language and a display culture.** Rating "temporal demand" or
  "frustration" assumes a shared vocabulary of introspection; translated instruments need
  their own validation, and willingness to report high workload/low SA to an observer
  varies by culture and workplace power dynamics.
- **Physiological and simulator methods are resource-gated.** Eye-trackers, EEG, and
  high-fidelity simulators for SAGAT freezes are resource-rich-organization assets;
  low-resource settings lean on subjective measures alone, which magnifies the confounds
  above. State which measures you could and could not run.
- **Individual differences are large.** Expertise, age, and training shift both workload
  and SA measures substantially; a single cohort's numbers are not a human constant, and
  between-subject comparisons need matching or statistical control (deferred to
  `statistics-applied/`).

---

## A Contrasting Example (non-WEIRD, low-resource)

*Fictional, to show how the method holds while the instruments must change.*

**Setting.** A *fictional* regional dispatch center coordinates flood response by radio
and paper logs, with mixed-language operators, no simulator, no eye-tracking, and strong
hierarchy between senior and junior staff.

**What breaks if you copy a Western workload/SA study wholesale.**
- **SAGAT has no simulator to freeze**, and probing operators *during* a live flood
  response is not an option. Substitute **descriptive, retrospective** measurement —
  reconstruct SA from the existing radio and log records after the incident — and, for
  evaluation, **offline replay** of a recorded incident in a training setting; state that
  both are weaker, indirect evidence and that latency/self-rating confounds remain.
- **Self-report is shaped by hierarchy.** Junior operators may under-report workload and
  over-report SA to senior staff; anonymous or third-party collection, and reporting *who*
  rated what, becomes part of the method.
- **Distributed SA is the natural unit.** With awareness spread across radios, paper logs,
  and several agents (§8), the design target is the **system's** SA — do the logs and
  callouts carry the right SA between shifts? — not one dispatcher's recall.

**Reading.** The **constructs and their traps** (workload/SA distinction, dissociation,
the folk-construct critique) transfer; the **instruments** must be chosen for the setting,
and their weakened evidential value stated plainly.

---

## Prototype Seam Contract (review gate for this guide)

This guide is a **review-gated prototype**, authored before the rest of the module to
prove the module's second-hardest seam: the boundary with `cognitive-science/09`, which
already owns Endsley SA and NDM **as cognitive theory**. The gate this guide must pass:

- **Mechanism stays deferred.** No cognitive mechanism (attention architecture, memory,
  the SA/NDM *theory*, the psychophysical laws) is re-derived here; each is cited to
  `cognitive-science/` and only its **operational measurement/design** consequence is
  owned. *Fails if* the guide explains *why* attention behaves as it does rather than *how
  to measure and design for it*.
- **Constructs are measured, not reified.** Workload and SA are presented as
  proxy-measured constructs with named confounds and validity domains; the folk-construct
  critique of SA is carried, not hidden. *Fails if* a score is treated as a direct mental
  readout or "loss of SA" is offered as a cause.
- **Safety stays out.** No certification, no fitness-for-duty call, no accident ruling;
  safety consequences route to `05`/`08`. *Fails if* any measurement is used to certify.
- **The module-wide pattern is inherited, not restated.** The full guide-family scaling
  contract lives in the scaling-gate prototype `02`; this guide simply conforms to it.

Passing this gate ratifies that the module can carry the cognitive-mechanism boundary on
real content before the remaining guides are authored.
