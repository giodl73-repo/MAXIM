# 10 — Methods of Knowing

## The Big Picture

This crosscut is the **Mathematics & Physics companion atlas**. It uses section
number 10 because mathematics and physics make the machinery of knowing most
explicit: proof, measurement, model, experiment, simulation, inference, and
uncertainty.

But every section has its own truth machinery. A botanist, historian, engineer,
doctor, linguist, architect, economist, and compiler writer do not know things
in the same way. This guide maps the recurring methods without flattening those
differences.

```
METHODS OF KNOWING

The question is not "is this true?"
The question is "what kind of warrant makes this claim credible?"

OBSERVE ----------> MEASURE ----------> MODEL
notice              instrument          abstraction
  |                    |                   |
  v                    v                   v
CLASSIFY --------> INFER ------------> TEST
name patterns        estimate causes      confront reality
  |                    |                   |
  v                    v                   v
SIMULATE --------> PROVE ------------> REMEMBER
run possible worlds  derive necessity     archive, replicate, teach

Each method buys one kind of confidence and leaves another kind of doubt.
```

Read this as a **warrant stack**. Observation starts the chain. Measurement
disciplines observation. Classification makes comparisons possible. Models
compress mechanisms. Inference estimates what cannot be seen directly. Testing
confronts claims with the world. Simulation explores regimes that are expensive
or impossible to run. Proof gives necessity inside formal assumptions. Archives
and replication preserve what a field has learned.

---

## Why This Belongs in Crosscuts, Not Just Mathematics & Physics

Mathematics and physics have the cleanest names for method:

```
proof          -> theorem, derivation, invariant
measurement    -> instrument, unit, calibration, uncertainty
model          -> state variables, law, approximation
experiment     -> intervention, control, repeatability
simulation     -> numerical world under explicit rules
inference      -> estimate, likelihood, posterior, confidence
```

The crosscut asks:

```
What counts as evidence when the field changes?
```

| Method | Physics Echo | Life / Earth Echo | Social / Human Echo |
|---|---|---|---|
| Measurement | meter, volt, spectrum | genome read, rainfall gauge | survey, census, price index |
| Experiment | controlled apparatus | clinical trial, field plot | randomized trial, A/B test |
| Model | differential equation | food web, climate model | game model, demographic model |
| Classification | particle taxonomy | species, rock, disease | legal category, genre, language family |
| Archive | lab notebook | specimen collection | court record, oral tradition, corpus |
| Proof | theorem | protocol proof, formal verification | legal proof standard, argument validity |
| Simulation | finite element, N-body | epidemic, hydrology | traffic, market, urban growth |

This is the key bridge:

```
different fields do not merely have different facts
they have different rules for converting evidence into warranted belief
```

---

## Layer 1: Observation, Classification, and Description

Before a field can explain, it must notice and name.

```
raw encounter -> repeated observation -> named category -> comparable cases
```

| Field | What Gets Classified | Why It Matters | Failure Mode |
|---|---|---|---|
| Natural World | species, clades, spices, crops | comparison and identification | folk categories hide evolutionary relation |
| Earth & Space | rocks, clouds, soils, landforms | field diagnosis and mapping | surface similarity hides process difference |
| Medicine | symptoms, syndromes, diseases | treatment and prognosis | label substitutes for mechanism |
| Language | sounds, scripts, families | translation and historical reconstruction | political identity confused with linguistic lineage |
| Arts & Culture | genres, styles, movements | comparison and criticism | style label becomes shallow period costume |
| Materials | phases, fibers, grains, defects | processing and performance | microstructure ignored |

Classification is not "mere naming." It is a compression system. The hard
question is whether the categories track real causal structure or only surface
appearance.

---

## Layer 2: Measurement and Instrumentation

Measurement is disciplined observation. It turns a perception into a quantity,
but only through an instrument, a unit, and a calibration chain.

```
phenomenon -> instrument -> signal -> unit -> uncertainty -> claim
```

| Measurement Question | Start With | Key Caveat |
|---|---|---|
| What is being measured? | Operational definition | The measured proxy may not be the target concept |
| What is the instrument? | Sensor, assay, survey, rubric, scale | Instruments have bias, drift, resolution, and blind spots |
| What is the unit? | Unit system or coding scheme | Units encode assumptions about comparability |
| What is the uncertainty? | Error bars, confidence, calibration | Precision is not accuracy |
| What is the sampling frame? | Who or what could be observed | Missing cases can dominate the conclusion |

**Old world -> new world bridge:** in older engineering settings this looks like
metrology: gauges, tolerances, calibration, traceability. In software and data
systems it becomes telemetry, logging, benchmark design, dataset lineage, eval
harnesses, and observability. Same discipline: know the instrument before
trusting the number.

---

## Layer 3: Models and Abstractions

A model is a deliberate compression: keep what matters, discard what does not,
then see whether the discard was safe.

```
world too rich
     |
     v
choose variables -> choose relations -> choose scale -> choose error budget
     |
     v
model useful for one purpose, dangerous for another
```

| Model Type | Strong At | Weak At |
|---|---|---|
| Mechanistic model | Explaining causal structure | Requires correct mechanism and parameters |
| Statistical model | Estimating patterns under uncertainty | Can predict without explaining |
| Simulation model | Exploring complex interactions | Can become an opaque artificial world |
| Formal model | Clarifying assumptions and consequences | May prove facts about the model, not the world |
| Narrative model | Connecting events and motives | Vulnerable to hindsight and selective evidence |
| Taxonomic model | Organizing variation | Can freeze transitional or hybrid cases |

The mature move is not "models are wrong." That is too easy. The mature move is:

```
for what decision is this approximation good enough?
```

---

## Layer 4: Experiment, Fieldwork, and Intervention

Experiments ask what changes when the world is pushed. Fieldwork asks what the
world is doing when it is not simplified for you.

```
LAB EXPERIMENT                         FIELDWORK

control variables                      preserve context
repeat conditions                      observe variation
strong internal validity               strong ecological validity
risk: artificial setup                 risk: confounding
```

| Field | Intervention / Field Method | What It Buys | What It Risks |
|---|---|---|---|
| Physics | controlled apparatus | clean causal isolation | apparatus artifact |
| Biology | wet lab, field station | mechanism plus organism context | model organism overreach |
| Medicine | clinical trial | treatment effect estimate | exclusion criteria hide real patients |
| Agriculture | field plot | soil/weather/crop realism | location-specific result |
| Anthropology | participant observation | tacit practice and meaning | observer effect, interpretive bias |
| Software | A/B test, staged rollout | behavior under live traffic | metric gaming, local optimum |

The central tradeoff:

```
control removes noise
context reveals whether the claim survives outside the apparatus
```

---

## Layer 5: Inference, Proof, and Judgment

Inference estimates beyond what was directly observed. Proof derives what must
follow from assumptions. Judgment decides whether the warrant is enough for the
decision at hand.

```
DATA -----------------> INFERENCE -----------------> BELIEF UPDATE
ASSUMPTIONS ----------> PROOF ---------------------> NECESSARY RESULT
CASE EXPERIENCE ------> JUDGMENT ------------------> ACTION
```

| Mode | Core Question | Failure Mode |
|---|---|---|
| Statistical inference | What is likely, given data and assumptions? | Hidden selection, model misspecification |
| Causal inference | What would change under intervention? | Confounding, bad counterfactual |
| Mathematical proof | What follows necessarily? | Assumptions mistaken for reality |
| Legal proof | Has the standard of proof been met? | Procedure confused with truth |
| Historical inference | What best explains surviving evidence? | Archive survival bias |
| Expert judgment | What action is warranted now? | Unexamined tacit bias or stale expertise |

Formal proof is the sharpest warrant, but only inside its frame. Field judgment
is the messiest warrant, but often the only one available in time.

---

## Cross-Library Appearance Map

| Section | How It Knows |
|---|---|
| Natural World | Classification, field observation, morphology, phylogeny, cultivation records |
| Earth & Space | Remote sensing, maps, stratigraphy, cores, proxies, planetary comparison |
| Material Culture | Recipes, process control, failure analysis, microscopy, craft transmission |
| Life Sciences | Assays, trials, organisms, populations, mechanisms, clinical judgment |
| History & Ideas | Textual evidence, archaeology, historiography, argument reconstruction |
| Mechanics | Measurement, tolerances, load tests, simulations, standards, prototypes |
| Technology | Verification, benchmarks, reliability tests, monitoring, regulation |
| Social Sciences | Surveys, administrative data, experiments, causal inference, institutional analysis |
| Language & Communication | Corpora, phonetic measurement, translation comparison, semiotic analysis |
| Mathematics & Physics | Proof, derivation, experiment, instrument calibration, model validation |
| Arts & Culture | Criticism, style analysis, performance practice, provenance, reception history |
| Computing & Software | Tests, types, proofs, logs, benchmarks, evals, incident evidence |
| People | Biography, correspondence, decisions under uncertainty, influence traces |

---

## What This Crosscut Is For

Use it when a claim sounds plausible but the warrant is unclear.

```
CLAIM TYPE                         ASK FIRST

"this causes that"              -> what counterfactual or intervention?
"this is measured"              -> what instrument and calibration?
"this model predicts"           -> what data and error regime?
"this is proven"                -> proven from which assumptions?
"this happened historically"    -> what survived in the archive?
"experts agree"                 -> by what practice and incentives?
```

The goal is not skepticism as posture. The goal is **right-sized trust**:
matching the confidence to the method that produced it.

---

## Decision Cheat Sheet

| If you need to diagnose... | Start With | Key Caveat |
|---|---|---|
| Whether a claim is observational or measured | Identify the instrument, unit, calibration, and sampling frame | Numbers inherit the instrument's blind spots |
| Whether a category is useful | Ask what the classification predicts or distinguishes | Names can preserve surface similarity while hiding mechanism |
| Whether a model is trustworthy | Identify purpose, scale, assumptions, and error budget | A model can be valid for one decision and dangerous for another |
| Whether an experiment proves causality | Check intervention, control, randomization, and external validity | Internal validity and real-world validity trade off |
| Whether field evidence is strong | Look at sampling, context, observer effects, and replication | Rich context can bring confounding with it |
| Whether statistical inference is warranted | Inspect data generation, missingness, model fit, and uncertainty | Elegant math cannot rescue biased data |
| Whether proof settles the issue | Separate formal conclusion from real-world interpretation | Proof gives necessity inside assumptions |
| Whether expert judgment is enough | Ask what feedback trained the expert and how current the domain is | Expertise decays when feedback is delayed, sparse, or politicized |

---

## Common Confusion Points

**Evidence is not one thing** — A fossil, theorem, lab result, oral testimony,
compiler error, randomized trial, and satellite image are all evidence, but they
carry different warrants and different failure modes.

**Quantitative does not mean objective** — A number can be precise, reproducible,
and still measure the wrong proxy. Measurement is a social-technical system:
instrument, unit, protocol, calibration, and interpretation.

**Models are not failed realities** — Models are tools built by omission. The
question is not whether a model omits. The question is whether the omissions are
safe for the decision being made.

**Proof is not empiricism with extra rigor** — Proof establishes necessity from
assumptions. Empirical work establishes warranted belief about the world. Both
are rigorous, but their rigor has different targets.

**Fieldwork is not weak experiment** — Field methods preserve context that lab
methods intentionally remove. The resulting evidence is different, not inferior
by default.

---

## Connection Forward

Methods of Knowing should be the standard for every later crosscut's evidence
discipline:

```
01 Scale & Hierarchy             -> what scale was observed?
02 Infrastructure & Logistics    -> what operational data proves flow?
03 Materials & Substrates        -> what instrument sees the substrate?
04 Energy & Flows                -> what conservation or accounting holds?
05 Time, Evolution & Memory      -> what archive or trace survived?
06 Tools & Instruments           -> what tool makes the phenomenon visible?
07 Systems & Failure             -> what incident evidence survives?
08 Institutions & Standards      -> what authority validates the rule?
09 Interfaces & Communication    -> what channel preserves meaning?
10 Methods of Knowing            -> what warrant supports the claim?
11 Practice, Craft & Judgment    -> what feedback trained the practitioner?
12 Design Patterns Across Reality -> what structure recurs?
13 Risk, Uncertainty & Decision  -> what action follows under uncertainty?
```

Every crosscut should name not just its pattern, but the method by which that
pattern is known.

