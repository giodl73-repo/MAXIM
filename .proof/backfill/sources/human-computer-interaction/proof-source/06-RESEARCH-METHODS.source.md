---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "06-RESEARCH-METHODS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-computer-interaction:research-methods
kind: guide
module: human-computer-interaction
section: human-computer-interaction
title: HCI Research Methods - Studying People and Contexts
status: source-custody
source_custody: partial
current_path: human-computer-interaction/06-RESEARCH-METHODS.md
canonical_path: human-computer-interaction/06-RESEARCH-METHODS.md
backsource_ids: [proof-backfill:human-computer-interaction:06-research-methods]
concepts: [research-methods, field-studies, interviews, surveys, diary-esm, ethnography, experiment-design, mixed-methods, research-ethics]
root_concepts: [research-methods]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# HCI Research Methods — Studying People and Contexts

**This guide owns** the methods HCI uses to *study people and their contexts* — controlled
experiments for HCI questions, surveys, interviews, field studies/ethnography, diary and
experience-sampling methods, and mixed methods — plus **research ethics as a concept**, and, above
all, the rule that **each method carries its own inferential and validity contract.** **It builds
on** nothing in the module (it feeds `04` with understanding and shares instruments with `05`).
**It explicitly defers**: *usability evaluation of a specific design* to `05` (a usability test is a
`05` object; this guide owns the broader study of people/context); the *general inferential
statistics* — hypothesis tests, power, confidence intervals, regression, mixed models, multiple-
comparison correction — to `statistics-applied/` (this guide names *which* estimate/test a design
needs and *why*, never the machinery); *experimental-psychology theory and the DSM* to `psychology/`;
and *legal obligations* around data/consent to `law/`.

> **This module is an educational reference. Research-ethics guidance here (consent, welfare,
> privacy, compensation, accessible participation) is **principle-level and never an IRB/ethics-
> board substitute** and never legal advice. Methods are described to study people *with* their
> informed consent and benefit, never to deceive or manipulate them (`11`). Named frameworks are
> attributed and dated.**

*Per-guide banner: a method is admitted only with its **validity contract stated** — its sampling
frame, its estimator or its declared qualitative paradigm, its missingness/reactivity risk, and (in
mixed designs) its integration logic. Generalizing a **convenience sample** without a coverage
argument, treating a **diary as passive ground truth**, or bolting **inter-rater κ onto a reflexive
analysis** are the three signature errors this guide exists to prevent.*

---

## The Big Picture: Every Method Trades Among Validities

There is no method that is valid in every way at once; each buys some validities and pays in others.
The map below is the whole guide: pick the method whose **validity profile** fits the question, and
**state the contract** you're accepting.

```
  THE FOUR VALIDITIES (Cook & Campbell 1979; Campbell & Stanley 1963)
  ------------------------------------------------------------------
   INTERNAL ....... did the manipulation CAUSE the effect? (control, randomization)
   EXTERNAL ....... does it GENERALIZE to other people/settings/times? (sampling)
   CONSTRUCT ...... are we measuring the THING WE NAME? (valid operationalization)
   STATISTICAL .... (defer machinery to statistics-applied/) is the inference sound?
   + ECOLOGICAL ... does the study setting resemble the REAL context of use?
  ------------------------------------------------------------------
   No method maximizes all. A lab experiment buys internal validity and pays
   ecological/external; a field ethnography buys ecological and pays internal.
   The METHOD CHOICE is a choice of WHICH validity to protect.
```

```
  METHODS BY WHAT THEY ANSWER (and what they can't)
  ------------------------------------------------------------------
   CONTROLLED EXPERIMENT .. "does A cause more X than B?"   strong internal, weak ecological
   SURVEY ................. "how common / how distributed?" needs a real sampling frame
   INTERVIEW .............. "why / how do people see it?"    rich meaning, no prevalence
   FIELD STUDY / ETHNOGRAPHY "what actually happens in situ?" strong ecological, weak control
   DIARY / ESM ............ "what happens in the moment, over time?" in-situ, compliance risk
   MIXED METHODS .......... combine, IF integration is designed  power + meaning, or a muddle
  ------------------------------------------------------------------
```

**Bridge (software).** These are the human-side analogs of your measurement stack. A controlled
experiment is a **benchmark on a fixed harness** (clean, causal, artificial); a field study is
**production observation** (real load, no control); a survey is **fleet telemetry** (only as good as
its sampling and instrumentation); interviews/ethnography are **incident deep-dives** (why, not how
often). And the cardinal engineering rule transfers: **a metric is only as trustworthy as the
population it sampled** — convenience data generalizes about as well as benchmarking on your own
laptop.

---

## 1. Controlled Experiments for HCI — Strong Cause, Weak Context

The experiment isolates cause by **manipulating an independent variable** and measuring a
**dependent variable** while controlling the rest.

```
  EXPERIMENT DESIGN CHOICES (and the validity each protects)
  ------------------------------------------------------------------
   BETWEEN-SUBJECTS ... each person sees one condition
                        + no learning/carryover  - needs more participants, individual-diff noise
   WITHIN-SUBJECTS .... each person sees all conditions
                        + controls individual diffs, fewer people
                        - ORDER/LEARNING effects -> COUNTERBALANCE (e.g., Latin square)
   CONFOUNDS .......... anything that varies WITH the condition -> internal-validity threat
   DEMAND / REACTIVITY  participants infer the hypothesis and comply (Orne 1962)
  ------------------------------------------------------------------
   Its contract: strong INTERNAL validity, weak ECOLOGICAL/EXTERNAL. The lab
   task is not the real task, and the sample is usually not the population.
```

The validity contract to state: **which difference estimate** the comparison needs (a *between* vs
*within* design demands a two-sample vs a paired procedure — the same distinction `05` §6 makes),
and that the **statistical machinery and power** are `statistics-applied/`'s. Threats to name up
front: confounds (internal), the artificial task (ecological), the convenience sample (external),
and demand characteristics / experimenter effects (construct + internal).

---

## 2. Surveys — Only as Good as the Sampling Frame

A survey estimates **how common** or **how distributed** something is across a population — but only
if the **sampling frame** supports the claim. The dominant threats (the Total Survey Error framing;
Groves and colleagues) are *not* the sample size:

```
  WHERE A SURVEY GOES WRONG (none of these is fixed by more n)
  ------------------------------------------------------------------
   COVERAGE error ..... the frame excludes part of the population (e.g., web-
                        only survey misses offline users)
   SAMPLING error ..... random variation from sampling (the ONE stats handles)
   NONRESPONSE bias ... who answers differs from who doesn't (usually the big one)
   MEASUREMENT error .. question wording/order/scale bias the answer (Likert, 1932)
  ------------------------------------------------------------------
   The signature error: generalizing a CONVENIENCE sample (whoever clicked)
   to "users" with NO coverage argument. State the frame or don't generalize.
```

The contract: state the **sampling frame and how it maps to the target population**, the
**response/nonresponse profile**, and the **measurement instrument's** provenance (a validated scale
vs ad-hoc questions). A convenience sample is fine for *exploration or discovery*; generalizing its
proportions to a population **without a coverage argument** is the failing test. The confidence-
interval and weighting *machinery* is `statistics-applied/`'s.

---

## 3. Interviews — Meaning, Not Prevalence

Semi-structured interviews yield **rich, situated meaning**: how people understand, value, and narrate
their experience. Their contract is honest about what they *cannot* do:

- **They estimate no prevalence.** N=12 interviews tell you *what perspectives exist and how they
  hang together*, never *what fraction of users* hold them. Reporting interview counts as if they
  were rates is a construct/external-validity error.
- **Self-report is filtered.** Social desirability, recall error, and post-hoc rationalization mean
  the *stated* reason may post-date the behavior (the same caveat as `05`'s think-aloud) — behavior
  observed (§5) is often the stronger signal.
- **Quality criterion: the declared paradigm.** If the analysis is interpretive (reflexive thematic
  analysis; §7), depth and reflexivity are the quality bar, not inter-rater agreement. "Saturation"
  (from grounded theory; Glaser & Strauss, **1967**) is a *guide* to sufficiency, not a
  measurement — and it is contested, so state how you judged it.

---

## 4. Field Studies, Ethnography, and Contextual Inquiry — Ecology Over Control

To learn **what actually happens in the real context** — not what people say in a lab — you go to the
setting. **Contextual inquiry** (Beyer & Holtzblatt, *Contextual Design*, **1998**) formalizes
watching users work in situ and interviewing about it in the moment; **ethnography** and
**ethnomethodology** (Garfinkel, **1967**) study the practices and orderliness of real work.

The contract: **strong ecological validity, weak control**, plus two threats to name — the **observer
effect** (being watched changes behavior) and the analyst's **positionality** (what you notice is
shaped by who you are). Field work's outputs are **situated accounts bounded to the setting studied**;
transferring them to another organization is a hypothesis (`02` activity theory made this prediction),
not a given.

---

## 5. Diary Studies and Experience Sampling — In-Situ, and Not Ground Truth

To capture experience **as it unfolds over time**, participants self-record: **diary studies**
(entries on events) and the **Experience Sampling Method** (ESM; Larson & Csikszentmihalyi, **1983**),
which pings participants at intervals to report the moment. Their value is reaching the *in-situ*
experience a lab can't.

Their contract is where the scaling rule bites hardest — **a diary/ESM record is *not* passive ground
truth:**

- **Compliance and missingness are structural.** People skip prompts, back-fill entries, and drop
  out; the *missing* moments are usually not missing at random (the busy, stressed, or bored moments
  go unrecorded). Treating the logged entries as a complete, unbiased record is the failing test.
- **Self-report is reactive.** The act of recording changes behavior and attention (people notice
  more, or perform for the diary). ESM reduces recall bias but adds interruption burden.

State the **prompt schedule, compliance rate, and missingness model**, and treat the diary as a
*sampled, reactive self-report*, never a sensor log.

---

## 6. Mixed Methods — Integration Is the Method, Not an Afterthought

Combining methods can buy **both** prevalence and meaning (survey + interview), or **cause and
mechanism** (experiment + field study) — but only if the **integration logic is designed**, not
stapled on (the purposes-of-mixing framing; Greene, Caracelli & Graham, **1989**; Creswell's
sequential/concurrent designs).

```
  MIXED-METHOD INTEGRATION -- name the logic before you collect
  ------------------------------------------------------------------
   SEQUENTIAL explanatory .. quant first, then qual to EXPLAIN the numbers
   SEQUENTIAL exploratory .. qual first, then quant to TEST/generalize themes
   CONCURRENT triangulation quant + qual at once, CONVERGE and read divergence
  ------------------------------------------------------------------
   Divergence between strands is a FINDING (which instrument is blind here?),
   not noise (the same triangulation logic as guide 05 section 8).
   The QUALITATIVE quality criterion depends on the PARADIGM:
     codebook / coding-reliability -> inter-rater agreement (Cohen's kappa, 1960) is apt
     reflexive thematic analysis (Braun & Clarke 2006/2019) -> kappa is NOT the
       criterion; depth, reflexivity, a coherent evidenced account are. Do not
       bolt kappa onto a reflexive analysis (the failing test).
```

The contract: name the **integration design** up front, use the **quality criterion of the declared
qualitative paradigm** (κ only where coding is a *measurement*), and use an **appropriate difference
estimate** for any quantitative comparison (deferring the estimator machinery to
`statistics-applied/`).

---

## 7. Research Ethics — Principle, Not Permission Slip

Studying humans carries obligations. Stated as **principles** (Belmont Report, **1979**: respect for
persons, beneficence, justice) — **not** as an IRB/ethics-board substitute and **not** as legal
advice:

- **Informed consent** — voluntary, comprehending, revocable; materials themselves accessible (`08`).
- **Welfare / beneficence** — minimize burden and harm; no fatigue-marathon sessions; care with
  distressing tasks.
- **Privacy & data** — collect the minimum; protect sensitive data (disability, health, location);
  the *legal* duty (GDPR and kin) is `law/`'s.
- **Justice & compensation** — fair pay for time and expertise (participants, including disabled
  co-designers, are skilled contributors, not favors — `08` §7); fair inclusion of the populations who
  bear the results.
- **Vulnerable populations & power** — extra care where consent is constrained (children, employees,
  patients, marginalized groups).

The load-bearing line: these principles are a **floor for thinking**, and following them is **never a
warrant to skip formal ethics review** where one applies.

---

## The Per-Method Validity Contract (the spine)

| Method | Sampling frame | Estimator / paradigm | Key threat to name | Owns / defers |
|--------|----------------|----------------------|--------------------|---------------|
| Controlled experiment | recruited sample → stated population | difference estimate (paired vs two-sample); power → `statistics-applied/` | confound, demand, artificial task | HCI owns design; stats deferred |
| Survey | **explicit frame** → target population | proportions/CIs → `statistics-applied/` | coverage & **nonresponse** bias | HCI owns instrument; machinery deferred |
| Interview | purposive (not representative) | interpretive; saturation as a guide | social desirability; **no prevalence** | HCI owns; no rate claims |
| Field / ethnography | the setting itself | situated account; positionality | observer effect; bounded transfer | HCI owns; transfer is a hypothesis |
| Diary / ESM | in-situ over time | sampled reactive self-report | **compliance/missingness**; reactivity | HCI owns; not ground truth |
| Mixed methods | per strand + integration | named integration + per-paradigm criterion | un-integrated "muddle"; κ-misuse | HCI owns integration logic |

---

## A Worked Method Choice (illustrative, fictional)

*Fictional, to show each method's contract and the integration logic. No real study.*

**Question.** *Kettle*, a fictional smart-thermostat maker, asks: "why are rural customers returning
the device, and how common are the reasons?"

- **Strand 1 — field study + interviews (mechanism).** Contextual inquiry (`06` §4) in a dozen rural
  homes reveals a mechanism: intermittent connectivity makes the app's cloud-only control fail, and
  the physical dial was removed. Contract stated: **ecological-strong, control-weak**; N=12 gives
  *reasons*, **not** prevalence; analyzed with **reflexive thematic analysis** (so depth/reflexivity,
  **not** κ, is the quality bar).
- **Strand 2 — survey (prevalence).** A survey estimates *how common* the connectivity complaint is —
  **but only** with a real **sampling frame** (all purchasers, not just app-active or web-responsive
  ones, to avoid coverage bias) and a **nonresponse** analysis (returners may not answer). The
  proportion's CI is `statistics-applied/`'s.
- **Integration — sequential exploratory.** Qual first (find the mechanism), then quant to test how
  widespread it is — the integration logic named **before** data collection. Where the strands
  **diverge** (interviews stress connectivity; the survey surfaces a second, price complaint), the
  divergence is a **finding** about which instrument saw what, not noise.
- **A `05` boundary.** "Does a new offline-first control flow reduce the failure?" is a **usability-
  evaluation** question — it goes to `05` (and any summative claim to `statistics-applied/`), not
  here. This guide found the *why* and the *how common*; testing the *fix* is `05`'s.

**Reading.** Every method is admitted **with its contract**: frames named, prevalence claimed only
from the survey (and only with a coverage argument), the diary/self-report never treated as a sensor,
κ never bolted onto the reflexive strand, and the integration logic designed in advance. That is the
discipline the guide exists to enforce.

---

## Reader Tasks (answerable from this guide)

1. **Match method to question and name its cost.** Given "how often does this bug bite?" vs "why do
   people abandon here?", choose survey vs interview/field study and state which validity each
   protects and which it sacrifices.
2. **Catch a convenience-sample overreach.** Given "60% of respondents to our in-app poll love the
   feature, so most users do," state the coverage and nonresponse threats and what sampling frame
   would be needed to make the prevalence claim.
3. **Refuse to treat a diary as ground truth.** Given a diary study with 55% prompt compliance, name
   the missingness and reactivity risks and how you'd report them, rather than reading the logged
   entries as a complete record.
4. **Assign the right qualitative quality criterion.** Given an interview study analyzed with
   reflexive thematic analysis, explain why reporting Cohen's κ would misframe it, and what quality
   criteria apply instead.
5. **Design a mixed-method integration.** For "why and how widely do users distrust our AI
   suggestions?", specify a sequential-exploratory design, what each strand contributes, and how you'd
   read divergence between them.

---

## Decision Cheat Sheet

| I need to know… | Method | Contract to state |
|-----------------|--------|-------------------|
| does A *cause* more X than B | controlled experiment | difference estimate; confounds; artificial-task limit (stats → `statistics-applied/`) |
| how *common* / distributed | survey | **sampling frame** + nonresponse; convenience ≠ population |
| *why* / how people see it | interviews | meaning not prevalence; paradigm's quality criterion |
| what *actually happens* in context | field study / ethnography | ecological-strong, control-weak; bounded transfer |
| in-the-moment, over time | diary / ESM | compliance/missingness; **not** ground truth |
| both prevalence and meaning | mixed methods | named integration logic; per-paradigm criterion |
| whether a *specific design* is usable | **`05`** | that's usability evaluation, not general research |
| the statistics behind any of it | **`statistics-applied/`** | HCI names the test; it doesn't own the machinery |

---

## Common Confusion Points

**"We surveyed users, so this is representative."** Only if the **sampling frame** covers the
population and **nonresponse** isn't biased. A convenience poll generalizes to no one without a
coverage argument; more responses don't fix coverage or nonresponse (§2).

**"The interviews show most users want X."** No. Interviews reveal *what perspectives exist and how
they cohere*, never *how many* hold them. Counting interview themes as prevalence is a category error
(§3).

**"The diary data is what really happened."** No. Diaries and ESM are **sampled, reactive self-
reports** with structural missingness — the unrecorded moments are usually the interesting ones.
Report compliance and treat it as self-report, not a sensor log (§5).

**"We double-coded and got good κ, so the qualitative analysis is rigorous."** Only if your paradigm
treats coding as **measurement** (codebook/coding-reliability). In **reflexive** thematic analysis, κ
is the *wrong* criterion — depth, reflexivity, and a coherent evidenced account are (§6).

**"We did an experiment, so the result generalizes."** An experiment buys **internal** validity
(cause), typically at the cost of **ecological/external** validity (artificial task, convenience
sample). Generalization needs a sampling and setting argument the experiment usually doesn't provide
(§1).

**"Following the ethics principles means we don't need review."** No. The principles are a floor for
thinking and **not** a substitute for formal ethics/IRB review where it applies, nor legal advice on
data (§7, `law/`).

---

## Global, WEIRD, and Resource Caveats

- **The method canon is WEIRD-sampled.** Most HCI methods were developed and validated on Western,
  educated, tech-literate convenience samples (Henrich et al. 2010). Interview and think-aloud norms
  (narrating to a stranger), survey conventions, and "saturation" heuristics do not transport
  unexamined; a method's validity contract must be re-checked for each population and culture.
- **Access shapes who is studied.** Remote studies widen reach but select for people with devices,
  bandwidth, literacy, and the AT to participate; in-person studies select for proximity. Either way,
  **who is in the frame is part of the result**, and disabled participants recruited **per segment on
  their own AT** are a first-class part of it (`08` §7) — a study that silently excludes them is
  under-powered for the population, not done (a carried invariant).
- **Ethics and safety ride every method.** The safety/ethics floor holds regardless of method: no
  deception-as-manipulation, no coercive recruitment, fair compensation, sensitive-data care; the
  *legal* duty is `law/`'s and the *formal review* is the ethics board's — this guide is neither
  (§7).
