---
maxim_schema: maxim.frontmatter.v1
id: maxim:pathology:environmental-nutritional-and-toxic-injury
kind: guide
module: pathology
section: pathology
title: Environmental, Nutritional, and Toxic Injury
status: source-custody
source_custody: partial
current_path: pathology/07-ENVIRONMENTAL-NUTRITIONAL-AND-TOXIC-INJURY.md
canonical_path: pathology/07-ENVIRONMENTAL-NUTRITIONAL-AND-TOXIC-INJURY.md
backsource_ids: [proof-backfill:pathology:07-environmental-nutritional-and-toxic-injury]
concepts: [physical-injury, chemical-toxic-injury, environmental-exposure, nutritional-deficiency, nutritional-overload, dose-response]
root_concepts: [environmental-pathology]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Environmental, Nutritional, and Toxic Injury

**This guide owns** the *mechanisms by which the external environment injures tissue*: **physical
injury** (mechanical, thermal, electrical, radiation, pressure) as injury mechanisms; **chemical
and toxic injury** and its general toxicology principles (direct-acting vs metabolically
activated agents, the target-organ concept, dose–response); **environmental and occupational
exposure** pathology (inhaled particulates, the exposure–latency–lesion pattern); **nutritional
deficiency** lesions (macronutrient and micronutrient) and **nutritional excess/overload**
lesions; and the unifying **dose–response and host-modifier** model that explains why the same
exposure injures differently. **It builds on** `01-CELL-INJURY-ADAPTATION-AND-DEATH` (oxidative
stress, necrosis, and accumulation are the cellular endpoints here), `02` (chronic exposure
drives inflammation and fibrosis), and `05` (many environmental agents are carcinogens feeding
the multi-hit process).

**It explicitly defers** the *specific drug and toxin catalog and any dosing* to `pharmacology/`
(and **no dose is given anywhere** — pillar 2/4); the *nutritional biochemistry and dietary
science* to `nutrition/` and `biochemistry/`; the *specific environmental and deficiency
diseases* to `disease/`; the *radiation physics* to `physics/` and `nuclear/`; and the
*population exposure epidemiology and screening programs* to `public-health/`. This guide owns
the **injury mechanism** — how an agent reaches, damages, and scars tissue — not a toxicology
manual, a nutrition guide, or a disease catalog.

> **This module is an educational reference about *how pathology reasons about disease
> mechanism* — never medical advice. It does *not* interpret any reader's own results,
> exposures, images, or symptoms, does *not* diagnose, and gives *no* treatment, dosing,
> antidote, dietary, specimen, or bench instructions and *no* forensic/legal (including
> poisoning or cause-of-death) determinations. All cases are fictional teaching vignettes; all
> numbers are illustrative and, where a real standard is named, attributed and dated.**

*Per-guide banner: educational reference on environmental/nutritional/toxic injury mechanism —
never self-diagnosis, never personal-result or personal-exposure interpretation, never a dose,
antidote, or procedure, never forensic/legal (poisoning/cause-of-death) advice. Agents and
diseases are named only to illustrate a mechanism; the catalog is `disease/`/`pharmacology/`.*

---

## The Big Picture: Tissue Is the Interface With a Hostile Environment, and Dose Makes the Poison

The novice mental model is "toxins are poisonous; deficiencies cause weakness." The expert model
is a **dose-at-target problem**: an external agent must be *delivered* to a tissue, reach an
effective *dose at its molecular target*, and act by a *mechanism*, before any lesion appears —
and the same agent can be harmless, therapeutic, or lethal depending on dose, route, duration,
and host. The organizing principle, attributed to Paracelsus (16th century) — *"the dose makes
the poison"* — applies to **everything** in this guide: physical energy, chemicals, and even
nutrients, each of which injures by **deficiency, sufficiency, or excess**.

```
THE EXPOSURE -> LESION CHAIN  (this guide owns the shaded middle)
================================================================
  external agent (physical energy / chemical / nutrient level)
        |  ROUTE + DOSE + DURATION  (how much reaches the body, and how)
        v
  ===== DOSE AT THE TARGET ===== (absorption, distribution, metabolism, excretion)
   some agents act DIRECTLY; some must be METABOLICALLY ACTIVATED to a toxic form;
   nutrients act by being TOO LOW or TOO HIGH
        |
        v
  ===== MECHANISM OF INJURY ===== (owned here; links to 01)
   oxidative damage · membrane/enzyme disruption · DNA damage · covalent binding ·
   physical/thermal destruction · a missing cofactor · overload accumulation
        |
        v
  ===== TISSUE LESION ===== (owned here; links to 01/02/05)
   necrosis · chronic inflammation + fibrosis · deficiency lesion · overload
   deposit · neoplasia (if a carcinogen)
        |
        v
  PHENOTYPE / DISEASE   <-- disease/ owns the entity; public-health/ owns the epi
```

Two facts govern the guide. First, **the mechanism is dose-at-target, not exposure alone**: an
exposure that never reaches an effective dose at a vulnerable target produces no lesion, which is
why route, duration, metabolism, and host handling matter as much as the agent. Second,
**nutrients obey the same dose curve as toxins**: too little and too much both injure, so
deficiency and overload are two ends of one axis, not separate topics. This is the U-shaped
dose–response that unifies the whole guide.

**Bridge — input validation, resource limits, and a supply chain.** Toxic injury is a *malformed
input that corrupts state* — sometimes benign until a transform ("metabolic activation") turns it
into something that overflows a buffer (covalent binding, DNA damage). Nutritional deficiency is
a *starved dependency*: a required input is missing, so the pathway that needs it fails.
Nutritional overload is *unbounded input with no back-pressure*: more arrives than the system can
store or clear, and it accumulates until it degrades the tissue. In every case the lesion is set
by how much reaches the target and whether the system can buffer it.

---

## 1. Physical Injury Mechanisms

Physical agents injure by **transferring energy** to tissue in excess of what the tissue can
absorb without damage. The classes differ by the *form* of energy, and each maps to a mechanism
already developed in `01`.

```
PHYSICAL INJURY  (sorted by the FORM of energy transferred)
===========================================================
  MECHANICAL     force disrupts tissue structure directly
                 (laceration, crush) -> immediate structural damage +/- hemorrhage (03)

  THERMAL        HEAT denatures proteins + destroys membranes (burns) OR
                 COLD causes ice/vascular injury -> ischemic necrosis (01/03)
                 -> severity scales with temperature x duration x area

  ELECTRICAL     current heats tissue along its path + disrupts excitable
                 membranes -> injury follows the current path

  RADIATION      IONIZING: deposits enough energy to ionize -> DNA damage + ROS
                 (01 oxidative; 05 carcinogenesis) -> acute + delayed lesions
                 NON-IONIZING is not one thing:
                   UV -> direct photochemical DNA lesions (dimers) ->
                     mutation + carcinogenesis (05); no ionization needed
                   INFRARED / RADIOFREQUENCY -> primarily thermal (heating)

  PRESSURE       barotrauma / altitude: gas-volume + oxygen-availability changes
                 -> mechanical + hypoxic injury (01)
```

**Mechanical** injury disrupts tissue structure directly, with immediate damage and often
hemorrhage (`03`). **Thermal** injury is a denaturation problem for heat (proteins and membranes
destroyed, scaling with temperature × duration × area) and an ice/vascular problem for cold
(producing ischemic necrosis, `01`/`03`). **Electrical** injury heats tissue along the current
path and disrupts excitable membranes, so the lesion follows the path of current flow.
**Radiation** is the most mechanistically rich: **ionizing** radiation deposits enough energy to
ionize molecules, damaging **DNA directly and via reactive oxygen species** — which is exactly
the `01` oxidative-injury mechanism and the `05` carcinogenesis mechanism, and why ionizing
radiation causes both **acute** (rapidly dividing tissue) and **delayed** (fibrosis, neoplasia)
lesions. **Non-ionizing** radiation is *not one mechanism*: **ultraviolet (UV)** lacks the
energy to ionize yet still causes **direct photochemical DNA injury** (e.g., pyrimidine dimers),
driving mutation and **carcinogenesis** (`05`), whereas **infrared and radiofrequency** are
**primarily thermal** — they mainly heat. Calling non-ionizing radiation "just heat" is
therefore wrong for the UV band, whose lesion is photochemical rather than thermal.
**Pressure** injury (barotrauma, altitude)
combines mechanical gas-volume effects with hypoxia. The *physics* is `physics/`/`nuclear/`; this
guide owns the *tissue-injury mechanism*.

A key literacy point owned here: **radiation injury has two timescales**. The *acute* lesion hits
rapidly dividing tissue first (the same reason it can be used against tumors); the *delayed*
lesion — fibrosis and secondary neoplasia — reflects DNA damage that manifests over years. The
same agent, two lesions, separated by the timescale of the mechanism (immediate mitotic failure
vs slow mutation accumulation).

---

## 2. Chemical and Toxic Injury: General Principles

Chemical injury is governed by **toxicology principles** that are general enough to hold across
agents, which is why this guide teaches the principles rather than cataloging chemicals (the
catalog and any dosing are `pharmacology/`). Two principles do most of the work.

```
DIRECT vs METABOLICALLY ACTIVATED  (the "toxication" idea)
=========================================================
  DIRECT-ACTING TOXIN            METABOLICALLY ACTIVATED TOXIN
  ------------------             -----------------------------
  toxic AS-IS -> injures at the  relatively inert as absorbed -> the body's own
  site of contact/entry          metabolism converts it to a REACTIVE toxic form
        |                                |
  lesion at the first tissue     lesion where the ACTIVATING metabolism happens,
  it contacts                    OR where the reactive metabolite concentrates
                                 -> explains counter-intuitive target organs
```

**Principle 1 — direct-acting vs metabolically activated.** Some chemicals are toxic **as
absorbed** and injure at the site of contact or entry. Others are relatively **inert until the
body's own metabolism converts them into a reactive toxic species** ("toxication" or metabolic
activation) — so the lesion appears **where the activating metabolism occurs** or where the
reactive metabolite concentrates, which explains why some toxins injure an organ far from the
route of exposure. The reactive species then injures by familiar `01` mechanisms: **covalent
binding** to proteins/DNA, **oxidative** damage, and membrane/enzyme disruption.

```
THE TARGET-ORGAN CONCEPT  (why a systemic toxin hits SPECIFIC organs)
====================================================================
  a toxin distributes through the body, but injures most where it is:
    - ABSORBED        (the portal of entry: the surface it crosses)
    - METABOLIZED     (organs that activate it bear the reactive product)
    - EXCRETED        (organs that concentrate it while clearing it)
    - ACCUMULATED     (tissues that bind/store it to high local dose)
  -> the lesion location is a DOSE-AT-TARGET story, not a random hit
```

**Principle 2 — the target-organ concept.** A systemically distributed toxin does not injure
uniformly; it injures most where the **local dose at a vulnerable target is highest** — the
organs that **absorb**, **metabolize** (and thus generate the reactive form), **excrete** (and
thus concentrate it during clearance), or **accumulate** it. This is why toxicology speaks of
*target organs*: the lesion's location is a **dose-at-target** consequence, predictable from
where the agent is handled, not a random hit. Combined with dose–response (Section 6), these two
principles let a reader reason about *where* and *whether* a chemical injures without any catalog.
This guide gives **no dose, threshold, antidote, or exposure limit** — those are
`pharmacology/`/`public-health/`, and stating them would breach the contract.

---

## 3. Environmental and Occupational Exposure Pathology

Environmental and occupational exposures injure tissue by the same principles, but with a
characteristic **chronic, low-dose, long-latency** signature that deserves its own treatment. The
paradigm is the **inhaled particulate**, whose pathology is a clean deposition–clearance–retention
mechanism.

```
INHALED-PARTICULATE MECHANISM  (deposition -> clearance -> retention -> reaction)
===============================================================================
  particles are inhaled
        |  DEPOSITION: where a particle lands depends on its SIZE
        |              (only certain sizes reach the deep, vulnerable regions)
        v
  the body tries to CLEAR them (mucociliary escalator; phagocytosis)
        |  RETENTION: particles that resist clearance stay -> cumulative burden
        v
  retained particles provoke a persistent reaction:
        - chronic inflammation (02)  ->  fibrosis (02)
        - some particle types are also carcinogenic (05)
        |
        v
  LONG LATENCY: the lesion appears YEARS after exposure (cumulative burden +
  the multi-hit timescale) -> exposure and disease are far apart in time
```

The mechanism is **deposition → clearance → retention → reaction**: whether an inhaled particle
reaches a vulnerable region depends on its **size**; the body attempts to **clear** it; particles
that **resist clearance are retained** and build a cumulative burden; and retained particles
provoke a **persistent reaction** — chronic inflammation and **fibrosis** (`02`), and for some
particle types, **carcinogenesis** (`05`). The defining feature is **long latency**: because the
lesion depends on cumulative burden and the multi-hit timescale, disease often appears **years to
decades after exposure**, so exposure and lesion are far apart in time — a fact central to
recognizing occupational disease as a *mechanism* (the specific occupational entities are
`disease/`; the exposure epidemiology is `public-health/`). Air and water pollutants injure by
the same logic (a delivered dose acting by an `01`/`02` mechanism); the exposure–latency–lesion
pattern is the transferable idea.

---

## 4. Nutritional Deficiency Lesions

A **nutritional deficiency** injures tissue when a **required nutrient is unavailable in
sufficient amount**, so the structure or pathway that depends on it fails. The pathology follows a
clean, generalizable logic that parallels the metabolic-block logic of `06`: **identify what the
nutrient does, and the deficiency lesion appears wherever that function is most needed.**

```
DEFICIENCY LOGIC  (a missing input -> the dependent function fails)
==================================================================
  a required nutrient is insufficient (inadequate intake, absorption,
  or increased demand/loss)
        |
        v
  the biochemical role it supports is impaired
   (a cofactor for an enzyme · a building block for a structure ·
    an antioxidant · a signaling molecule)
        |
        v
  the lesion appears in the tissue that MOST DEPENDS on that role
   -> rapidly dividing tissue, high-turnover structures, and
      metabolically demanding organs show it first
        |
        v
  MACRONUTRIENT (protein-energy) vs MICRONUTRIENT (vitamin/mineral) deficiency
```

The **deficiency logic** is: a nutrient becomes insufficient (through inadequate intake, impaired
absorption, or increased demand/loss); the **biochemical role it supports** — as an enzyme
cofactor, a structural building block, an antioxidant, or a signaling molecule — is impaired; and
the **lesion appears in whichever tissue most depends on that role** (rapidly dividing tissue and
high-turnover structures typically show it first). The split into **macronutrient**
(protein-energy) and **micronutrient** (vitamin/mineral) deficiency is a scale distinction:
protein-energy deficiency impairs *everything* that needs building blocks and fuel (broad,
systemic lesions), while a specific micronutrient deficiency produces a *characteristic* lesion
tied to that nutrient's specific role. The *biochemistry* of each nutrient is `nutrition/`/
`biochemistry/`; the *named deficiency diseases* are `disease/`; this guide owns the **deficiency
mechanism and its location logic**.

A recurring subtlety owned here: **deficiency can be relative, not just absolute** — impaired
absorption, increased demand (growth, healing, `02`), or increased loss can produce a deficiency
lesion despite adequate intake. So a deficiency lesion is evidence of a *broken supply-to-demand
balance*, not necessarily of inadequate diet — the pathology equivalent of a starved dependency
that is present but unreachable.

---

## 5. Nutritional Excess and Overload Lesions

The other end of the dose axis is **nutritional excess**, and it injures by two distinct
mechanisms worth separating.

```
TWO OVERLOAD MECHANISMS  (the other end of the U-shaped dose curve)
==================================================================
  (1) OVER-NUTRITION (energy excess)
      chronic caloric surplus -> expanded/altered adipose tissue that behaves
      as a METABOLICALLY ACTIVE, pro-inflammatory tissue (links to 02)
      -> systemic low-grade inflammation + metabolic derangement
      -> a risk state feeding cardiovascular, metabolic, and neoplastic lesions

  (2) SPECIFIC OVERLOAD (a single substance accumulates)
      intake/absorption/retention of ONE substance exceeds storage + clearance
      -> it accumulates in tissues to a toxic local dose (links to 01 accumulation)
      -> organ deposition + injury where the substance is stored
```

**Over-nutrition** — chronic energy surplus — is best understood *pathologically* not as "excess
fat" but as an **altered tissue and inflammatory state**: expanded adipose tissue behaves as a
**metabolically active, pro-inflammatory** organ, producing a **systemic low-grade inflammation**
(the `02` machinery, chronically low-level) and metabolic derangement that constitutes a **risk
state** feeding cardiovascular, metabolic, and neoplastic lesions elsewhere. The lesion is
*systemic and mechanistic*, not merely cosmetic.

**Specific overload** is the mirror of deficiency: when intake, absorption, or retention of **one
substance** exceeds the capacity to store and clear it, the substance **accumulates in tissue to a
toxic local dose** — directly the `01` accumulation mechanism — and injures the organs where it is
stored. The unifying point across Sections 4–5 is the **U-shaped dose–response**: both ends of the
curve injure, so nutritional pathology is a *balance* problem, and "more" is not safer than "just
enough." The dietary science and any intake recommendations are `nutrition/`; the named overload
diseases are `disease/`; this guide owns the *overload mechanism*.

---

## 6. The Unifying Dose–Response and Host-Modifier Model

All of the above collapses into **one model**: the lesion is a function of the **dose at the
target** and the **host's ability to buffer it**. Making the model explicit is what lets a reader
reason about a novel exposure without a catalog.

```
THE DOSE-RESPONSE + HOST-MODIFIER MODEL  (the whole guide in one frame)
=====================================================================
  LESION  =  f( AGENT PROPERTIES,  DOSE,  DURATION,  ROUTE,  HOST FACTORS )

  DOSE-RESPONSE SHAPE:
    THRESHOLD agents      no effect below a threshold, then rising injury
    NO-THRESHOLD agents   risk in principle rises from any exposure (e.g., the
                          stochastic DNA-damage/carcinogenesis model, 05)
    U-SHAPED (nutrients)  injury at BOTH deficiency and excess

  HOST MODIFIERS (why the same dose injures people differently):
    - genetic handling (how fast an agent is activated/detoxified — 06)
    - age + developmental stage (perinatal vulnerability, 06; the timing principle)
    - existing organ reserve + disease
    - adaptation (repeated low exposure can up-regulate handling — up to a limit)
```

The model is **LESION = f(agent properties, dose, duration, route, host factors)**. The
**dose–response shape** varies: some agents have a **threshold** (safe below it, injurious above),
some are modeled as **no-threshold** (risk in principle rising from any exposure — the stochastic
carcinogenesis model of `05`), and nutrients are **U-shaped** (injury at both ends). The **host
modifiers** explain why the same dose injures people differently: **genetic handling** (how fast
the host activates or detoxifies an agent — the `06` metabolism theme), **age and developmental
stage** (perinatal vulnerability and the timing principle, `06`), **existing organ reserve**, and
**adaptation** (repeated low-level exposure can up-regulate handling — but only up to a limit).
This is the honest, mechanism-first frame: it explains *variation* and *thresholds* without ever
asserting a specific number, which is exactly what the four-pillar contract requires. Every
threshold, limit, and dose is owned elsewhere (`pharmacology/`, `public-health/`, `nutrition/`)
and is population- and era-specific; this guide teaches only the *shape and the modifiers*.

---

## 7. Worked Fictional Cases: Mechanism, Not Diagnosis

Each case is a fictional teaching vignette tracing the exposure-to-lesion chain. None interprets a
real person's exposure or findings, and none states a dose, threshold, or antidote.

**Case A — Injury in an organ far from the route of exposure (metabolic activation + target
organ).**
A fictional agent is absorbed at one site but produces its main lesion in a distant organ. The
mechanistic reading combines the two toxicology principles: the agent is **metabolically
activated** — relatively inert as absorbed, then converted by the body's own metabolism into a
reactive species — and it injures a **target organ** determined by where that activating
metabolism occurs or where the reactive metabolite concentrates. The lesion location is a
**dose-at-target** story, not a paradox: the organ that *handles* the agent bears the injury. No
agent is identified and no dose is stated; the mechanism is the point.

**Case B — Fibrosis appearing decades after an inhalational exposure (deposition–retention–latency).**
A fictional occupational scenario shows fibrosis appearing long after the exposure ended. The
mechanism is the **inhaled-particulate** pathway: size-dependent **deposition** in a vulnerable
region, incomplete **clearance**, **retention** building a cumulative burden, and a **persistent
reaction** — chronic inflammation (`02`) progressing to fibrosis, with a **long latency** because
the lesion depends on cumulative burden and the multi-hit timescale. The exposure and the lesion
are far apart in time *by mechanism*, which is why occupational disease is recognized by the
exposure–latency–lesion pattern. The entity and the exposure limits are `disease/`/`public-health/`.

**Case C — The same nutrient causing injury by both too little and too much (the U-shaped
curve).**
A fictional scenario notes that a substance produces a deficiency lesion at low levels and an
overload lesion at high levels. The mechanistic reading is the **U-shaped dose–response** that
unifies Sections 4–5: at the low end, the **dependent function fails** (deficiency logic — the
lesion appears where the function is most needed); at the high end, the substance **accumulates
beyond storage/clearance** to a toxic local dose (overload logic — the `01` accumulation
mechanism). Both ends injure, so the safe state is a *balance*, not a maximum. No intake amount is
given; the mechanism (the shape of the curve) is the lesson.

---

## Reader Tasks (answerable from this guide)

Each task is a *mechanism-reasoning* exercise — how the environment injures tissue — not a
personal-exposure interpretation, and none states a dose, threshold, or antidote.

**Task 1 — "Why does pathology insist that 'the dose makes the poison' even for water and
vitamins?" (Big Picture, Sections 4–6)**
Because injury is a **dose-at-target** phenomenon on a **dose–response curve**, and that curve
applies to *everything*, including nutrients. Too little of a required nutrient starves the
function that depends on it (deficiency lesion); too much exceeds storage and clearance and
accumulates to a toxic local dose (overload lesion). The safe region is a *band*, not a maximum or
a minimum — the U-shaped curve. This is why deficiency and excess are two ends of one axis, and
why "more" is not inherently safer. The principle is Paracelsus's, attributed and general.

**Task 2 — "How can a toxin absorbed in one place injure a completely different organ?" (Section
2)**
Two toxicology principles combine. First, **metabolic activation**: the agent may be inert as
absorbed and become reactive only after the body's metabolism converts it, so the lesion appears
**where the activating metabolism happens**. Second, the **target-organ concept**: a systemic
toxin injures most where its **local dose at a vulnerable target is highest** — the organs that
metabolize, excrete, or accumulate it. Together they make the distant lesion a predictable
dose-at-target consequence, not a paradox. No agent, dose, or antidote is named; the mechanism is
the answer.

**Task 3 — "Why do occupational lung diseases show up decades after the exposure?" (Section 3)**
Because the mechanism is **cumulative and slow**. Inhaled particles deposit by size, resist
**clearance**, are **retained** to build a cumulative burden, and provoke a **persistent
reaction** — chronic inflammation and fibrosis (`02`), sometimes neoplasia (`05`) — that unfolds
over the multi-hit timescale. So the lesion depends on *accumulated burden over time*, and
exposure and disease are far apart by mechanism. Recognizing the **exposure–latency–lesion**
pattern is how occupational disease is understood mechanistically; the entities and limits are
`disease/`/`public-health/`.

**Task 4 — "Two people have the same exposure but only one is injured. What does the mechanism say
without blaming luck?" (Section 6)**
The **host modifiers**. The lesion is `f(agent, dose, duration, route, host factors)`, and the host
factors differ: **genetic handling** (how fast each person activates or detoxifies the agent —
`06`), **age and developmental stage** (`06`), **existing organ reserve**, and **adaptation** from
prior low-level exposure. So the *same external exposure* can reach very different *doses at the
target* and meet very different buffering capacity, producing injury in one host and not the
other. Variation is mechanistic, not random.

**Task 5 — "Radiation is used to treat some tumors but also causes cancer. How is that not a
contradiction?" (Section 1, with `05`)**
Because ionizing radiation has **two lesions on two timescales**, both from the *same* DNA-damage/
reactive-oxygen mechanism. **Acutely**, it damages rapidly dividing cells enough to kill them —
which is why it can be directed against a rapidly dividing tumor. **In the long term**, sublethal
DNA damage in surviving cells can accumulate into the multi-hit process of carcinogenesis (`05`),
producing delayed neoplasia and fibrosis. Same mechanism, opposite uses, separated by dose,
targeting, and timescale — the physics is `physics/`/`nuclear/`, the carcinogenesis is `05`, and
this guide owns the injury mechanism.

---

## Decision Cheat Sheet

| Question to reason about | Mechanism to reach for | Key caveat |
|---|---|---|
| Any physical injury | Energy form: mechanical / thermal / electrical / radiation / pressure | Severity scales with dose × duration × area; maps to `01` endpoints |
| Radiation injury | Ionizing → DNA damage + ROS → acute *and* delayed (fibrosis, neoplasia) | Two timescales, one mechanism; physics is `physics/`/`nuclear/` |
| Non-ionizing radiation injury | UV → direct photochemical DNA lesions → mutation/carcinogenesis (`05`); IR/RF → primarily thermal | "Non-ionizing = just heat" is wrong for UV; the UV lesion is photochemical, not thermal |
| A toxin injuring a distant organ | Metabolic activation + target-organ concept (dose-at-target) | The organ that handles the agent bears the lesion |
| Whether a chemical injures at all | Dose–response: threshold vs no-threshold; route/duration/host | No dose or limit stated here; those are `pharmacology/`/`public-health/` |
| Occupational/environmental disease | Deposition → clearance → retention → reaction; long latency | Exposure and lesion are far apart in time by mechanism |
| A deficiency lesion | Deficiency logic: missing role → lesion where that role is most needed | Can be relative (absorption/demand/loss), not just low intake |
| A nutritional overload lesion | Over-nutrition (inflammatory state) vs specific overload (accumulation) | U-shaped curve: both ends injure; balance, not maximum |
| Why one exposure injures unevenly | Host modifiers: genetic handling, age, reserve, adaptation | Same exposure → different dose-at-target and buffering |

---

## Common Confusion Points

**"The dose makes the poison" applies to nutrients too.**
Injury is dose-at-target on a dose–response curve. For nutrients the curve is U-shaped — deficiency
and excess both injure — so the safe state is a band, not a maximum or minimum.

**Exposure is not dose.**
An exposure that never reaches an effective dose at a vulnerable target produces no lesion. Route,
duration, metabolism, and host handling determine the dose-at-target, which is what actually
injures.

**Direct-acting vs metabolically activated toxins.**
Direct-acting toxins injure as-absorbed at the site of contact; metabolically activated toxins are
inert until the body converts them to a reactive form, so they injure where the activating
metabolism or the reactive metabolite concentrates — often a distant target organ.

**Deficiency can be relative.**
Impaired absorption, increased demand (growth, healing), or increased loss can produce a deficiency
lesion despite adequate intake. A deficiency lesion means a broken supply-to-demand balance, not
necessarily an inadequate diet.

**Over-nutrition is a tissue/inflammatory state, not just "extra fat."**
Pathologically, chronic energy surplus produces a metabolically active, pro-inflammatory tissue
state with systemic low-grade inflammation (`02`) — a risk state feeding lesions elsewhere.

**Long latency is a mechanism, not a coincidence.**
Cumulative-burden and multi-hit processes make environmental and radiation lesions appear years
after exposure; the gap in time is expected from the mechanism.

---

## Resource, Geographic, and Bias Caveats

- **No dose, threshold, exposure limit, antidote, or intake amount is given anywhere in this
  guide.** Those numbers are population-, era-, and jurisdiction-specific and are owned by
  `pharmacology/`, `public-health/`, and `nutrition/`. This guide teaches only the *shape* of the
  dose–response and the *mechanism*; stating a cutoff would breach the non-advice/non-procedure
  contract and would be false precision.
- **Environmental and nutritional disease burden varies enormously by geography, occupation,
  socioeconomic setting, and era** — those *entities* and their epidemiology are `disease/` and
  `public-health/`. Deficiency dominates some settings and overload others; the mechanism (the
  dose curve and the exposure–latency–lesion pattern) transfers, the case mix does not.
- **Host susceptibility means the same exposure is not equally injurious to all.** Genetic
  handling, age, organ reserve, and adaptation modify the dose-at-target; this guide teaches the
  modifier set rather than presenting any exposure as uniformly (or never) harmful.
- **Forensic and cause-of-death determinations are out of scope (pillar 3).** Where poisoning or
  environmental death is conceptually relevant, nothing here should be read as a poisoning,
  causation, or cause-/manner-of-death conclusion; those are legal determinations owned outside
  this module.
