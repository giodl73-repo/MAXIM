---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "07-MARKET-RESEARCH.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:marketing:market-research
kind: guide
module: marketing
section: marketing
title: Market Research
status: source-custody
source_custody: partial
current_path: marketing/07-MARKET-RESEARCH.md
canonical_path: marketing/07-MARKET-RESEARCH.md
backsource_ids: [proof-backfill:marketing:07-market-research, git-history:marketing:07-market-research]
concepts: [market research, qualitative, quantitative, surveys, sampling, conjoint, A/B testing]
root_concepts: [market research]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Market Research

## The Big Picture

Market research is how marketing learns what is *true* — about customers, demand,
and what works — instead of guessing. It is applied inference: a research design
maps a business question to data and back to a decision. The landscape runs from
the question, through method choice, to a confident answer.

```
+-------------------------------------------------------------------------+
|                      THE RESEARCH PROCESS                               |
|                                                                         |
|  1 DEFINE        the business question -> a researchable question       |
|     |            ("should we launch X?" -> "what is WTP for X?")        |
|     v                                                                   |
|  2 DESIGN        choose the method:                                     |
|     |            EXPLORATORY (qual) -> DESCRIPTIVE (survey) ->          |
|     |            CAUSAL (experiment / A/B)                              |
|     v                                                                   |
|  3 SAMPLE        who do we ask? probability vs non-probability,         |
|     |            sample size, frame, error                              |
|     v                                                                   |
|  4 COLLECT       instruments: interviews, surveys, observation,         |
|     |            behavioral logs, experiments                           |
|     v                                                                   |
|  5 ANALYZE       statistics / coding -> findings (see statistics-       |
|     |            applied/ for the methods)                              |
|     v                                                                   |
|  6 DECIDE        translate findings into a marketing decision           |
|                                                                         |
|  PRIMARY data = collected for THIS question. SECONDARY = existing.      |
+-------------------------------------------------------------------------+
```

**Read top-down**: the question dictates the design; the design dictates the
sample and instrument; analysis produces findings; findings drive a decision. The
bridge: this is the **scientific method / experiment pipeline** you already run —
hypothesis, design, sample, measure, infer — applied to customers. Statistical
machinery lives in `statistics-applied/`; this guide is the *applied design*.

---

## Qualitative vs Quantitative

The first fork. They answer different questions and are usually *sequenced*, not
chosen between.

```
+-----------------------------------------------------------------+
|         QUALITATIVE  vs  QUANTITATIVE                           |
|                                                                 |
|  QUALITATIVE                    QUANTITATIVE                    |
|  -----------                    ------------                    |
|  Question: WHY / HOW            Question: HOW MANY / HOW MUCH   |
|  Small N, deep                  Large N, shallow                |
|  Words, themes, meaning         Numbers, rates, magnitudes      |
|  Generates hypotheses           Tests hypotheses                |
|  Not projectable to pop.        Projectable (if sampled right)  |
|                                                                 |
|  Methods:                       Methods:                        |
|   focus groups                   surveys                        |
|   depth interviews               experiments / A/B              |
|   ethnography / observation      conjoint                       |
|   projective techniques          behavioral analytics           |
|                                                                 |
|  TYPICAL SEQUENCE: qual to find the questions ->                |
|  quant to measure the answers at scale.                         |
+-----------------------------------------------------------------+
```

| Dimension | Qualitative | Quantitative |
|---|---|---|
| **Answers** | Why, how, what themes | How many, how much, which is bigger |
| **Sample** | Small, purposive | Large, representative |
| **Output** | Hypotheses, language, insight | Estimates, tests, projectable numbers |
| **Risk** | Not generalizable; analyst bias | Misses the "why"; garbage-in if mis-designed |
| **Role** | Explore / generate | Confirm / measure |

The classic mistake is running a quant survey before you understand the problem —
you measure precisely the wrong thing. **Qual scopes the question; quant sizes the
answer.**

---

## Surveys and Questionnaire Design

The workhorse of descriptive research. The design choices that determine validity:

```
+-----------------------------------------------------------------+
|                  SURVEY DESIGN PITFALLS                         |
|                                                                 |
|  LEADING QUESTIONS   "How much do you love our fast service?"   |
|                      -> biases the answer. Ask neutrally.       |
|                                                                 |
|  DOUBLE-BARRELED     "Is it fast AND affordable?" -> two        |
|                      questions; the answer is uninterpretable.  |
|                                                                 |
|  ACQUIESCENCE BIAS   tendency to agree. Balance positive +      |
|                      negative framings.                         |
|                                                                 |
|  SOCIAL DESIRABILITY  people answer how they "should".          |
|                      -> stated != revealed preference.          |
|                                                                 |
|  ORDER / ANCHORING   earlier questions prime later ones.        |
|                                                                 |
|  NON-RESPONSE        who DIDN'T answer may differ               |
|                      systematically -> non-response bias.       |
+-----------------------------------------------------------------+
```

Common scale types: **Likert** (agree-disagree, ordinal), **semantic differential**
(bipolar adjective pairs), **NPS** (0-10, "would you recommend"). Each has known
quirks — Likert is ordinal (means are dubious), NPS collapses a 0-10 scale into
promoters/passives/detractors and throws away information. Choose the scale to fit
the analysis you'll run.

The deepest survey trap is **stated vs revealed preference**: what people *say*
they'll pay or do diverges systematically from what they *actually* do (social
desirability, hypothetical bias). This is why behavioral/experimental methods (A/B,
conjoint) often beat direct questioning — they observe revealed behavior. (Stated
vs revealed preference theory: `behavioral-economics/01`.)

---

## Sampling

You can't ask everyone; you sample and infer. The critical split is **probability
vs non-probability** sampling — it determines whether you can generalize.

```
+------------------------------------------------------------------+
|                  SAMPLING METHODS                                |
|                                                                  |
|  PROBABILITY (every unit has a known, non-zero chance)           |
|  ----------------------------------------------------            |
|   SIMPLE RANDOM      everyone equally likely                     |
|   STRATIFIED         random within strata (ensures subgroups)    |
|   CLUSTER            sample whole groups (cheaper, less precise) |
|   SYSTEMATIC         every k-th unit                             |
|   -> PROJECTABLE to the population; error is quantifiable.       |
|                                                                  |
|  NON-PROBABILITY (selection not random)                          |
|  --------------------------------------                          |
|   CONVENIENCE        whoever's easy (most online panels)         |
|   QUOTA              fill demographic quotas, non-randomly       |
|   SNOWBALL           referrals (hard-to-reach groups)            |
|   JUDGMENT           expert picks                                |
|   -> NOT projectable; selection bias unknown.                    |
+------------------------------------------------------------------+
```

| Concept | Meaning | Why it matters |
|---|---|---|
| **Sampling frame** | The list you draw from | If the frame omits people, results are biased before you start |
| **Sampling error** | Random variation from sampling | Shrinks with sample size (~1/sqrt(n)); quantifiable |
| **Non-sampling error** | Bias (coverage, non-response, measurement) | *Doesn't* shrink with n — a bigger biased sample is just confidently wrong |
| **Margin of error** | CI half-width at a confidence level | The honest uncertainty band on an estimate |

The crucial, counterintuitive point: **a bigger sample fixes sampling error, not
bias.** A million-respondent convenience sample with selection bias is *more
confidently wrong* than a small random one. This is the 1936 Literary Digest
lesson — 2.4 million responses, wrong call, because the frame was biased. (Full
sampling theory: `statistics-applied/`.)

```
OLD WORLD                          SAMPLING ANALOG
-----------------------------      -------------------------------------
Representative test traffic        Probability sample
Cherry-picked / convenience logs   Non-probability sample (biased)
"n is huge so it's right"          Big-n fallacy: bias survives n
Monte Carlo error ~ 1/sqrt(n)      Sampling error ~ 1/sqrt(n)
Selection bias in your dataset     Coverage / non-response bias
```

---

## Conjoint Analysis

The premier quantitative technique for measuring *how buyers trade off attributes*
— and for deriving WTP and the value of features. It powers pricing (`04`) and
positioning (`02`).

```
+-----------------------------------------------------------------+
|                  CONJOINT ANALYSIS                              |
|                                                                 |
|  IDEA: don't ask "how important is price?" (people lie).        |
|  Instead, show whole PRODUCT PROFILES and ask them to           |
|  choose. Infer the hidden attribute weights from the choices.   |
|                                                                 |
|  Profile A          Profile B          Profile C                |
|  .-------------.     .-------------.    .-------------.         |
|  | 256GB       |     | 512GB       |    | 256GB       |         |
|  | blue        |     | black       |    | black       |         |
|  | $899        |     | $1099       |    | $999        |         |
|  '-------------'     '-------------'    '-------------'         |
|        "Which would you buy?"  (repeat over many sets)          |
|                                                                 |
|  OUTPUT (per attribute level):                                  |
|   PART-WORTH UTILITIES  e.g. 512GB worth +X utils               |
|   IMPORTANCE weights    which attributes drive choice           |
|   IMPLIED WTP           $ value of each feature                 |
|   SIMULATION            predicted share for any config          |
+-----------------------------------------------------------------+
```

Conjoint's power is that it uses **revealed trade-offs in choices** rather than
**stated importance ratings** — sidestepping the stated/revealed gap. From the
choices it estimates **part-worth utilities** (the value of each attribute level),
which yield feature importance, willingness-to-pay for each feature, and a
**market simulator** that predicts share for any product configuration or price.
It is the closest marketing comes to a demand model you can optimize against — the
empirical input to value-based pricing (`04`).

---

## Experiments and A/B Testing

The only method that establishes **causation**. Everything above is correlational;
a controlled experiment is the gold standard for "did *this* change cause *that*
result."

```
+-----------------------------------------------------------------+
|                  A/B TEST = CONTROLLED EXPERIMENT               |
|                                                                 |
|  random         .--------------.                                |
|  assignment     |  CONTROL (A) | ---> baseline metric           |
|   |  --------> |  unchanged    |                                |
|  population     '--------------'                                |
|   |             .--------------.                                |
|   |  --------> | TREATMENT (B)| ---> treatment metric           |
|  randomize      |  one change  |                                |
|                 '--------------'                                |
|                                                                 |
|  RANDOMIZATION makes A and B equivalent on average, so the      |
|  only systematic difference is the treatment -> the metric      |
|  delta is CAUSAL.                                               |
|                                                                 |
|  Watch: statistical power (enough n), the peeking problem       |
|  (don't stop early on noise), novelty effects, SUTVA            |
|  (units shouldn't interfere), and effect on the RIGHT metric.   |
+-----------------------------------------------------------------+
```

You already run A/B tests on features and rollouts — *this is the same machinery
applied to marketing*: a landing page, a price, an email subject, an ad creative.
The discipline is identical: pre-register the hypothesis and the primary metric,
power the test (compute n for a minimum detectable effect), randomize at the right
unit, don't peek/stop early (inflates false positives), and beware interference
between units. Experimental design and inference live in `statistics-applied/`;
here the point is that A/B testing is *causal* market research, and it beats every
survey for "does it work."

| Method | Establishes | Strength | Weakness |
|---|---|---|---|
| Focus group / interview (qual) | Hypotheses | Depth, "why" | Not projectable, biased |
| Survey (descriptive) | Correlation, magnitudes | Scale, projectable | Stated != revealed; bias risk |
| Conjoint | Trade-offs, WTP | Revealed trade-offs, simulatable | Hypothetical context |
| A/B / experiment (causal) | **Causation** | Gold standard for "did it work" | Needs traffic, control of conditions |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Understand *why* customers behave a way | Qualitative (interviews, focus groups, ethnography) |
| Size how many / how much, projectably | Quantitative survey on a probability sample |
| Generalize to the whole market | Probability sampling — non-probability can't project |
| Avoid being confidently wrong | Fix *bias* (frame, non-response), not just grow n |
| Measure what features are worth / WTP | Conjoint analysis |
| Prove a change *caused* a result | A/B test / controlled experiment |
| Set a value-based price empirically | Conjoint -> WTP -> price (`04`) |
| Avoid the stated/revealed gap | Prefer behavioral methods (conjoint, A/B) over direct asking |
| Choose a rating scale | Match the scale to the analysis (Likert ordinal, NPS lossy) |

---

## Common Confusion Points

### "A bigger sample is always more accurate"

Only for *sampling* error (random noise, ~1/sqrt(n)). It does nothing for *bias*
(coverage, non-response, selection) — a huge biased sample is just confidently
wrong (Literary Digest, 1936). Representativeness beats size.

### "Surveys tell us what customers will do"

They tell you what customers *say* — which diverges systematically from behavior
(social desirability, hypothetical bias). For "will they buy / pay," prefer
revealed-preference methods (conjoint, A/B) over stated intentions.

### "Qualitative research is just unscientific anecdote"

Qual is rigorous when used for its job — generating hypotheses, surfacing the "why"
and the customer's language. Its error is *generalizing* small-N findings to the
population. Use qual to scope, quant to size. Misusing either is the failure.

### "Correlation in our survey shows X causes Y"

No observational method establishes causation; only a randomized experiment does.
Survey cross-tabs and regressions show association, confounded by everything you
didn't control. To claim causation, run an A/B test.

### "We can stop the A/B test now — it's significant"

Peeking and stopping at the first significant result inflates false positives
dramatically. Fix the sample size (or use a proper sequential-testing method)
*before* you start, and read out at the planned n. This is the same discipline as
not p-hacking an experiment.

### "Conjoint asks people to rate importance"

The opposite — conjoint *avoids* importance ratings (which people answer
unreliably) by inferring weights from forced *choices* among whole profiles. That
indirection is precisely why it's more valid than asking "how important is price?"
