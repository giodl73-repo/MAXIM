---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-factors:physical-ergonomics-anthropometrics
kind: guide
module: human-factors
section: human-factors
title: Physical Ergonomics & Anthropometrics - Designing Work for the Distribution of Bodies
status: source-custody
source_custody: partial
current_path: human-factors/02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS.md
canonical_path: human-factors/02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS.md
backsource_ids: [proof-backfill:human-factors:02-physical-ergonomics-anthropometrics]
concepts: [physical-ergonomics, anthropometrics, percentile-design, accommodation, occupational-biomechanics, niosh-lifting-equation, musculoskeletal-risk]
root_concepts: [physical-ergonomics]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Physical Ergonomics & Anthropometrics — Designing Work for the Distribution of Bodies

**This guide owns**, at quantitative-systems depth, the *physical* fit between the
human body and a system of work: the human body as a **statistical distribution**
(percentile design, z-scores, and the multivariate-accommodation problem); the
**design-limit logic** of clearance, reach, and strength; anthropometric data as
**dated, sampled estimates**; the **workspace/accommodation envelope**; **posture and
occupational biomechanical load** and its bounded screening indices (RULA, REBA, OWAS,
Snook tables); the **NIOSH lifting equation as a bounded model**; **work–rest, fatigue,
and environmental load** as modifiers; and the **musculoskeletal-disorder (MSD) risk**
model at the population level. **It builds on** `00-OVERVIEW` (the human-factors system
map) and hands physical measurement/instrumentation to `10-METHODS-AND-MEASUREMENT`.
**It explicitly defers**: *compact product-form ergonomics* — consumer handles, seats,
knobs, doorknobs, affordances, the Norman action model, and the seven principles of
universal design — to [`industrial-design/05-ERGONOMICS`](../industrial-design/05-ERGONOMICS.md),
which remains MAXIM's product-form entry point; *tissue/joint/gait biomechanics as an engineering
science* to [`biomedical-engineering/01-BIOMECHANICS`](../biomedical-engineering/01-BIOMECHANICS.md);
*clinical diagnosis, treatment, or rehabilitation of musculoskeletal disorders* to
[`clinical-medicine/`](../clinical-medicine/00-OVERVIEW.md) and `medicine/`; *cognitive workload
and mental load* to
[`03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS`](03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md); and
*population statistics machinery* (fitting distributions, sampling error, regression) to
[`statistics-applied/`](../statistics-applied/00-OVERVIEW.md).

> **Safety & ethics contract (binds every human-factors guide).** This is an
> **educational systems reference**, not an operations manual. It contains **no
> operational instructions** (nothing here tells anyone how to lift, how to set up a
> real workstation, or how to run a task), **no certification or compliance ruling** (it
> cannot say a job "passes OSHA" or "meets an ISO limit"), **no accident or legal
> determination**, and **no individual fitness-for-duty assessment**. Screening models
> and exposure limits below are **population-level engineering estimates**, attributed
> and dated, with a bounded validity domain — never a medical judgment about a specific
> person or a warrant that a specific task is safe.

*Per-guide banner: every number below (a percentile, a load constant, a multiplier, a
score band) is a dated, population-and-context-bounded estimate from a named data set or
model, not a universal human constant. Anthropometric tables age; equations have a
domain of validity outside which they are silent, not conservative.*

---

## The Big Picture: You Are Not Designing for a Person — You Are Designing for a Distribution

Physical ergonomics starts from one uncomfortable fact: **the "average person" does not
exist**, and a system built for that phantom fits almost no one. Every body dimension is
a distribution over a defined population; a job, a cockpit, or a workstation must
**accommodate a specified range of that distribution while a modeled physical load stays
below a limit**. Two orthogonal questions drive every physical-ergonomics decision:
*which dimension constrains this design, and toward which tail?* and *what physical load
does the task impose, and does it exceed a bounded limit for the population you must
accommodate?* The first is the **fit / accommodation** problem; the second is the
**load / injury-risk** problem. Product-form design (`industrial-design/05`) mostly lives
in the first; occupational human factors owns both at systems depth.

```
PHYSICAL ERGONOMICS = FIT  x  LOAD    (this guide owns the quantitative-systems view)
================================================================================
   AXIS 1 -- FIT / ACCOMMODATION            AXIS 2 -- LOAD / INJURY RISK
   which body dimension constrains,         what physical demand does the task
   toward which tail of the distribution?   impose, vs a bounded population limit?

   CLEARANCE -> high percentile (95/99th)   FORCE / LIFT -> NIOSH eqn, Snook tables
   REACH     -> low  percentile (5/1st)     POSTURE      -> RULA / REBA / OWAS bands
   STRENGTH  -> low  percentile of capacity  REPETITION / DURATION -> work-rest, MSD
   ADJUST    -> span the accommodated range  ENVIRONMENT  -> heat / vibration / noise
================================================================================
   Read it as: pick the constraining dimension + tail (FIT), then check the modeled
   load against a dated, bounded limit (LOAD). A body that fits can still be overloaded;
   a light load can still exclude bodies that do not fit. Both must pass.
```

```
       THE ACCOMMODATION FRAME                boundary with product-form design
   ----------------------------------     ------------------------------------------
   population  ->  distribution  ->  design    industrial-design/05  = compact
   (who, when,     (mean, SD,        limit     product-form entry (handle, seat,
    which survey)   percentiles)     + adjust   knob, affordance, universal design)
        |                |              |
        v                v              v        human-factors/02 (this guide) =
   provenance      z = (x - mu)/sigma  who is    quantitative systems depth:
   matters:        5th  z = -1.645     excluded  population modeling, occupational
   dated, sampled  95th z = +1.645     and at    biomechanics, lifting/posture
   estimates       1st  z = -2.326     what cost  models, work-rest, MSD risk
================================================================================
```

The rest of this guide layers down each half — the distribution and its design-limit
logic first, then load, posture, the lifting model, environment, and the product↔work
boundary — and closes with the reader tasks, cheat sheet, confusions, caveats, and the
**scaling contract** that governs how the other eleven guides inherit this discipline.

---

## 1. The Population Is a Distribution, Not a Person

A body dimension — stature, eye height, forearm length, grip strength — is a random
variable over a **defined population** (a place, an era, a sex, an age band, an
occupational group). Model it, within that population and sex, as approximately normal,
and a **percentile** is just a point on that curve:

```
PERCENTILE = mu + z * sigma        (x-th percentile of one dimension, one population)
--------------------------------------------------------------------------------
   z(1st)  = -2.326      z(5th)  = -1.645      z(50th) =  0.000
   z(95th) = +1.645      z(99th) = +2.326      (standard-normal quantiles)

   Example (illustrative): if adult male stature ~ N(mu = 176 cm, sigma = 7 cm),
      5th  percentile = 176 - 1.645*7  ~= 164.5 cm
      95th percentile = 176 + 1.645*7  ~= 187.5 cm
   The MEAN (176) is a summary of the curve, not a target you build for.
```

### 1.1 The "average person" is empty

The single most consequential idea in this guide: **no one is average on everything at
once.** Someone at the 50th percentile of stature is almost never simultaneously at the
50th percentile of arm length, sitting height, hip breadth, and grip strength — those
dimensions are only partly correlated. If you require ten dimensions to each land in a
narrow band around the median, the fraction of real people who qualify collapses toward
zero. Designing for "the average person" therefore designs for a body that essentially
**does not occur** — the historical *Norma* / "average airman" failure, where cockpits
built to 1940s mean dimensions fit almost no actual pilot.

```
THE MULTIVARIATE-ACCOMMODATION TRAP  (why "5th-95th on each" != "90% of people")
--------------------------------------------------------------------------------
   Univariate view (WRONG as a population claim):
     "5th-95th percentile on EACH dimension" sounds like 90% coverage.

   Multivariate reality:
     A person is accommodated only if they fall inside the box on ALL constraining
     dimensions at once. Because dimensions are imperfectly correlated, the JOINT
     accommodated fraction is LOWER than any single-dimension 90%.

        1 dimension:                       ~90% inside
        2 partly-correlated dimensions:    < 90% inside both
        k dimensions:                      shrinks further as k grows

   Fix: accommodate the JOINT distribution -- boundary manikins / a PCA family of
   representative cases spanning the multivariate hull -- not k independent percentiles.
```

This is exactly the depth that a compact product-form treatment (`industrial-design/05`)
does not carry, and it is the reason human factors owns the *systems* view: real
workstations, cockpits, and PPE constrain **several** dimensions simultaneously, so the
accommodation claim must be **multivariate**, not a stack of univariate percentiles.

### 1.2 Structural vs functional, and why posture changes the number

**Structural (static) anthropometry** measures a still body in a standard pose (stature,
sitting height, breadths). **Functional (dynamic) anthropometry** measures reach and
clearance in the *working* posture, with joints moving and clothing/PPE on. A cockpit
control lives in functional space: a static forearm length overstates real reach once
the shoulder harness, the seated recline, and a gloved hand are included. Design limits
are set in **functional** space; static tables are the raw material, corrected for
posture, motion, clothing, and footwear.

---

## 2. Design-Limit Logic — Clearance, Reach, Strength, Adjust

For each constraining dimension you make one of four calls. The choice of **tail** is not
a preference; it follows from what failure looks like.

```
THE FOUR DESIGN-LIMIT MOVES
--------------------------------------------------------------------------------
   CLEARANCE  (a minimum space/opening: hatch, legroom, aisle, PPE inner size)
      -> design to a HIGH percentile (95th / 99th) of the constraining dimension.
      -> if the largest accommodated body fits, every smaller body fits.

   REACH  (max distance to a control that MUST be operable)
      -> design to a LOW percentile (5th / 1st) of reach.
      -> if the shortest-reach body can reach it, everyone with longer reach can.

   STRENGTH / FORCE  (force an actuator or task demands)
      -> design to a LOW percentile of CAPACITY (the weakest accommodated user).
      -> if the weakest can operate it, the stronger can; do NOT size to the mean.

   ADJUSTABILITY  (one fixed size cannot satisfy both tails)
      -> provide a RANGE spanning, e.g., 5th-percentile-female to 95th-percentile-male
         on the governing dimension; seat height, monitor arm, steering column.

   ONE-SIDED vs TWO-SIDED:
      clearance and reach are usually ONE-SIDED (one tail governs).
      a fixed seat height is TWO-SIDED (too high excludes short legs -> dangling feet;
      too low excludes long legs -> knees up) -> this is where adjustability earns its cost.
```

### 2.1 The accommodation cost curve

Accommodation is not free, and the tails cost the most. Moving from 90% to 99%
accommodation widens every adjustment range, adds mechanism, mass, and cost, and can
compromise other requirements (a cockpit that fits the 1st-to-99th percentile may not
close). The systems decision is **where to truncate the distribution and who that
excludes**, made explicitly — not by defaulting to "the average" and pretending the tails
are not people.

```
ACCOMMODATION vs COST  (schematic -- the tails are expensive)
--------------------------------------------------------------------------------
   cost / complexity
      ^
      |                                             * 99%   <- steep: rare bodies,
      |                                        *              wide adjust range,
      |                              *   95%                  mass/cost/other reqs
      |                    *  90%
      |            *  80%
      |     *  (design decision: choose the truncation KNOWINGLY,
      |  *          name who is excluded and why)
      +------------------------------------------------> % population accommodated
   Rule: state the accommodation target, the governing dimensions, and the excluded
   tail as an explicit design record -- not an accident of building for the mean.
```

---

## 3. Anthropometric Data Is a Dated, Sampled Estimate

Every percentile you use came from a **specific survey of a specific population at a
specific time**. Treating one survey as "the human body" is the most common factual error
in physical ergonomics.

```
MAJOR ANTHROPOMETRIC DATA SETS  (attributed, dated -- context, not a universal table)
--------------------------------------------------------------------------------
   ANSUR II (2012)   US Army, 6,068 personnel, 93 measures. Military, fit,
                     age/selection-biased -- NOT a civilian or global sample.
   CAESAR (~1998-2000) US/Canada + NL + Italy civilians, 3D scans; ~4,431 TOTAL
                     (~2,400 North America, ~1,200 NL, ~775 Italy) -- 3D-shape
                     reference, late-1990s Western civilians, not a global sample.
   NHANES (ongoing)  US civilian health survey; stature/weight/BMI trends over decades.
   DINED (TU Delft)  Curated Dutch + international tables; the Dutch skew TALL.
   Regional surveys  SizeChina, Indian/Japanese/Brazilian national studies -- each
                     differs; no single set transfers to another population unadjusted.

   THREE QUESTIONS TO ASK OF ANY PERCENTILE:
     WHOSE body?  (population, sex, age, occupation, selection)
     WHEN?        (secular trend: historical growth ~1 cm/decade in stature, now
                   plateauing/reversing in some countries -- a 1970 table is stale)
     HOW MEASURED? (posture, clothing, landmarks, instrument -- structural vs functional)
```

Key consequences: (1) **secular trend** — stature and mass have drifted over the 20th
century, so old tables under-size current populations; (2) **cross-population difference**
— a Dutch-derived 95th percentile is not a Japanese 95th percentile; a global product
needs global or region-specific data; (3) **secular trend in mass/BMI** shifts breadth and
clearance more than stature. The honest move is to name the survey and its bounds, not to
launder one nation's soldiers into "the human."

---

## 4. Reach, Clearance & the Workspace Envelope

Putting §2's design-limit logic in space gives the **workspace envelope**: the volume a
seated or standing operator can reach and see in the working posture. Two nested reach
zones organize control placement.

```
WORKSPACE ENVELOPE  (functional reach, seated operator -- schematic plan view)
--------------------------------------------------------------------------------
                       . . . . . . . . . . .
                   .        MAXIMUM REACH       .     full arm extension + torso
                 .     (occasional controls,      .   rotation; sized to LOW
                .        acceptable to lean)        .  percentile of reach (5th/1st)
               .        - - - - - - - - - - -        .
              .      /      NORMAL REACH       \      .   forearm pivot at the elbow;
              .     |   (frequent / critical     |     .  no torso movement; the ZONE
              .     |    controls live here)      |     .  for anything used often or
              .      \    [ operator seat ]      /      .  under time pressure
               .       - - - - - - - - - - - -        .
                .                                     .   PRINCIPLE:
                 .                                   .    frequency + criticality ->
                   .                              .       inner zone; sized so the
                       . . . . . . . . . . . .           SHORTEST-reach user reaches.
   Vision cone and neutral head/eye line constrain DISPLAY placement the same way ->
   see 06-DISPLAY-CONTROL-INTERFACE-DESIGN for the display/control layout half.
```

- **Clearance** dimensions (knee room under a bench, aisle, hatch, helmet inner shell)
  are sized to a **high** percentile so the largest accommodated body fits.
- **Reach** to any control that must be operated — especially emergency controls — is
  sized to a **low** percentile of reach so the shortest-reach operator succeeds.
- The **overlap constraint**: a chair low enough to give a tall operator knee clearance
  can leave a short operator's feet dangling — hence adjustable seat height plus a
  footrest, the canonical two-sided case.

Physical *placement* of displays and controls, coding, and control-room layout is the
subject of `06`; this guide owns the **reach/clearance geometry and its percentile
logic**, `06` owns **what goes where and why** for operator performance.

---

## 5. Posture & Occupational Biomechanical Load

Fit gets the body to the work; **load** decides whether the work injures it over a shift,
a month, a career. The core biomechanical idea is the **moment (torque) about a joint**:
an external load times its horizontal distance from the joint must be balanced by muscle
and ligament forces with a *short* internal moment arm, so tissue forces are far larger
than the external load — the reason a modest weight held at arm's length loads the low
back enormously.

```
WHY POSTURE MULTIPLIES LOAD  (moment balance about the L5/S1 disc -- schematic)
--------------------------------------------------------------------------------
   external load W at horizontal distance D from the spine
      -> external moment  = W * D
   internal muscle force Fm acts at a SHORT moment arm d (a few cm)
      -> Fm ~= (W * D) / d          (d small  =>  Fm large)
   spinal COMPRESSION ~= Fm + upper-body weight component

        held CLOSE (D small)              held FAR (D large)
            |  W                                        W
            | /  small D                    __________/  large D
        [spine]-- d                         [spine]-- d (unchanged, small)
        Fm modest                           Fm LARGE -> high disc compression

   Lesson: the SAME weight is a different load depending on posture and distance.
   This is why the lifting model (Sec.6) is dominated by HORIZONTAL distance.
```

### 5.1 Static vs dynamic load, and the tissue-tolerance model

- **Static (postural) load** — holding a posture (arms overhead, trunk flexed, neck
  down) occludes blood flow and fatigues muscle even with no motion; risk rises with
  **magnitude x duration**.
- **Dynamic load** — repeated exertions (lifting, gripping, keying); risk rises with
  **force x repetition x posture deviation x recovery deficit**.
- **MSD risk model** (population level): a musculoskeletal disorder emerges when
  **cumulative load exceeds tissue tolerance**, and tolerance itself falls with fatigue
  and rises with recovery. This is a *dose–response* frame, not a threshold: there is no
  single weight that is universally "safe," only exposures that raise or lower risk for a
  population. (Clinical diagnosis and treatment of any actual disorder is
  `clinical-medicine/`'s and `medicine/`'s, not this guide's.)

### 5.2 Posture screening indices — bounded tools, attributed and dated

Practitioners compress posture/force/repetition into **screening scores**. Treat each as
a *bounded index*, dated and attributed, that flags exposures for further study — never a
diagnosis, a certification, or a guarantee.

```
POSTURE / LOAD SCREENING INDICES  (bounded models -- flag, do not certify)
--------------------------------------------------------------------------------
   RULA  (McAtamney & Corlett, 1993)  upper-limb posture+force+use -> score 1-7
         1-2 acceptable | 3-4 investigate | 5-6 investigate & change soon | 7 now
   REBA  (Hignett & McAtamney, 2000)  whole-body incl. legs/trunk -> score 1-15 bands
   OWAS  (Karhu et al., 1977)         back/arms/legs/load posture categories, sampled
   Snook tables (Liberty Mutual;      psychophysical "acceptable weights/forces" for a
     Snook & Ciriello, 1991)          % of the working population by task geometry
   NIOSH lifting eqn (Sec.6)          a physics+psychophysics+physiology composite model

   HOW TO READ A SCORE: it is an ordinal FLAG for a population, computed from a defined
   input set, valid only inside that input domain. A "2" is not "safe for this person";
   a "7" is not a legal finding. Different indices disagree by design -- they weight
   different hazards. Use them to PRIORITIZE study, not to rule on a job or a worker.
```

---

## 6. The NIOSH Lifting Equation as a Bounded Model

The **revised NIOSH lifting equation** (Waters, Putz-Anderson, Garg & Fine, **1993**;
applications manual **1994**; revising the original **1981** equation) is the canonical
worked example of a *bounded model* in human factors. This guide explains **how the model
reasons** — as a piece of engineering thinking about a distribution of workers — and does
**not** provide operational lifting instruction, workplace certification, or any judgment
that a specific task is safe. It is presented for conceptual literacy only.

```
STRUCTURE OF THE MODEL  (conceptual -- NOT a procedure to follow)
--------------------------------------------------------------------------------
   RWL = LC * HM * VM * DM * AM * FM * CM        RWL = Recommended Weight Limit

   LC  Load Constant     the model's baseline "ideal-condition" weight
                         (23 kg, set by the revised 1993 equation) -- a starting point,
                         then DISCOUNTED by six dimensionless multipliers in [0,1].
   HM  Horizontal        smaller as the load is held FARTHER from the spine (Sec.5:
                         horizontal distance dominates spinal moment).
   VM  Vertical          smaller as the start/end height departs from mid-height.
   DM  Distance          smaller as the vertical travel of the lift grows.
   AM  Asymmetry         smaller as the lift twists away from the sagittal plane.
   FM  Frequency         smaller as lifts/min and duration rise (fatigue/recovery).
   CM  Coupling          smaller for poor hand-object coupling (bad grip/handles).

   LIFTING INDEX:  LI = (weight actually handled) / RWL
      LI  <= 1   modeled demand within the model's recommended limit for ~most workers
      LI  > 1    modeled demand exceeds it; risk rises with LI for the population
   The multipliers ENCODE the biomechanics of Sec.5 (moment arms) plus psychophysical
   and physiological evidence into one composite screening number.
```

### 6.1 The validity domain — where the model is silent, not conservative

A bounded model's most important property is the **domain outside which it does not
apply**. The NIOSH equation was derived for a specific envelope; outside it, the equation
does not become conservative — it simply **does not model the task**:

```
ASSUMPTIONS / VALIDITY DOMAIN (illustrative -- outside these the model is SILENT)
--------------------------------------------------------------------------------
   two-handed, smooth lifts        NOT one-handed, jerking, or carrying/pushing
   moderate thermal environment    NOT extreme heat/cold
   good footing/traction           NOT slippery or constrained stances
   unrestricted posture            NOT seated, kneeling, or space-restricted lifts
   the load is a known, stable mass NOT unstable/live loads (liquids, people, animals)

   => A low LI is NOT proof of safety, and an out-of-domain task has NO valid LI.
      The model is a lens for reasoning about horizontal distance, height, twist,
      frequency, and coupling -- not a certificate and not a how-to.
```

So the equation earns its place here as a **teaching model**: it shows how physical
ergonomics turns the moment-arm physics of §5, plus fatigue and grip evidence, into a
single population-level index with an explicit validity domain and an explicit failure
mode (silence outside the domain). Everything an actual workplace would need — measured
task parameters, a qualified assessor, and a real safety program — is deliberately out of
scope per the safety contract.

---

## 7. Work–Rest, Fatigue & Environmental Load

Load is not just per-exertion; it accumulates and it interacts with the environment.

```
LOAD MODIFIERS OVER TIME AND ENVIRONMENT  (conceptual)
--------------------------------------------------------------------------------
   WORK-REST:  fatigue accumulates with exertion and DISSIPATES with recovery.
      How recovery is DISTRIBUTED over a shift is a design VARIABLE, not a rule:
      whether many short recovery periods or fewer long ones better clear a
      given accumulated load is a hypothesis to MODEL and validate locally, not
      a schedule this guide sets. The Sec.6 FM multiplier discounts RWL for lift
      frequency and duration; it does NOT prescribe a rest schedule.
   STATIC HOLD:  even light postures held long occlude perfusion -> earlier fatigue
      than the raw force suggests; "no motion" is not "no load."
   THERMAL:  heat raises cardiovascular strain and lowers usable strength/endurance;
      cold lowers dexterity and grip -> the SAME task is a heavier load in the heat.
   VIBRATION:  hand-arm vibration (power tools) and whole-body vibration (vehicles)
      are independent MSD/comfort hazards that compound posture/force load.
   NOISE / LIGHTING:  environmental stressors that raise overall strain and error
      (auditory/visual load) -- their PERFORMANCE effects tie to guide 03; their
      role here is as physical-load modifiers.
```

The systems point: a task rated acceptable in a cool, quiet, well-lit lab can be
overloading on a hot line with vibration and time pressure. Physical ergonomics models
the **envelope of conditions**, not a single nominal case — and hands the *cognitive*
consequences of fatigue, heat, and noise (workload, vigilance, error) to guide 03.

---

## 8. The Product ↔ Workplace Boundary (with `industrial-design/05`)

MAXIM deliberately carries physical human fit in **two** places. Keeping them
non-duplicating is the central architecture call for this guide.

```
WHO OWNS WHAT  (product-form vs quantitative-systems depth)
--------------------------------------------------------------------------------
   industrial-design/05-ERGONOMICS  (COMPACT PRODUCT-FORM ENTRY)
      the object in the hand / under the body: handle diameter, grip type, seat
      shape, knob, doorknob; Norman affordances & anti-affordances; the 7 principles
      of universal design; "design for 5th/95th" stated at product scale.
      Audience: a designer shaping a consumer product's FORM.

   human-factors/02  (THIS GUIDE -- QUANTITATIVE SYSTEMS DEPTH)
      the DISTRIBUTION and the SYSTEM OF WORK: z-scores and multivariate
      accommodation; the design-limit + accommodation-cost logic; occupational
      biomechanics (moment arms, spinal load); the lifting model and its validity
      domain; posture indices; work-rest/environment; population MSD-risk dose-response.
      Audience: an engineer accommodating a POPULATION doing a TASK over time.

   SHARED OBJECT (e.g., a workstation with a graspable handle at a bench):
      industrial-design/05 owns the handle's FORM and affordance;
      human-factors/02 owns population ACCOMMODATION and recovery/load evidence;
      the accountable organization owns any implemented work-rest schedule.
   Rule of thumb: if the question is "what does the body touch and how is it shaped?"
      -> industrial-design/05. If it is "what fraction of which population can do this
      task, at what modeled load, over what schedule?" -> human-factors/02.
```

This boundary is the reason `industrial-design/05` stays a compact, correct product-form
guide while human factors carries the statistical and occupational-biomechanics depth
without either guide re-teaching the other.

**Evidence-and-acceptance boundary at an interactive workstation.** Where the system of work includes a
digital/interactive interface (a touchscreen induction terminal, a handheld scanner UI),
the workstation is simultaneously an **HCI system** and a **human-factors** system. These
MAXIM modules own **methods and evidence**, not authority over a real deployment:
`human-computer-interaction/` supplies the interaction, visualization, and accessibility
*methods and evidence*; `human-factors/02` supplies the physical-accommodation and
occupational-load **evidence** (with `03` adding the workload/error and
performance-under-stress evidence). **Acceptance and implementation are owned by the
accountable domain organization and its regulator**, not by any reference module: a usable
screen on an unaccommodated bench, or an accommodated bench with an unusable screen, is
strong on one evidence stream and weak on another, and it is the accountable organization
that weighs the evidence and decides. Safety-critical systems remain HCI systems. Guide `06`
carries the full HCI↔HF seam.

---

## A Worked Quantitative Pass — Percentiles, Joint Accommodation & a Bounded Lifting-Index Sensitivity (synthetic)

*All numbers here are **synthetic**, chosen so the arithmetic is fully reproducible by
hand. This section demonstrates the math of §1–§6; it is **not** an assessment of any real
population, task, worker, or product, and **not** operational instruction.*

### Q1. Percentiles from a synthetic distribution (reproducible)

Take two body dimensions, modeled (within one synthetic population and sex) as normal:

```
SYNTHETIC INPUTS  (illustrative -- not a real survey)
--------------------------------------------------------------------------------
   stature            X ~ N(mu_X = 170 cm, sigma_X = 10 cm)
   functional reach   Y ~ N(mu_Y =  75 cm, sigma_Y =  5 cm)
   correlation        rho(X, Y) = 0.50   (partial, positive -- typical of body dims)

   PERCENTILE = mu + z*sigma        z(5th) = -1.645     z(95th) = +1.645
   -----------------------------------------------------------------------------
   stature  5th = 170 - 1.645*10 = 153.6 cm    95th = 170 + 1.645*10 = 186.5 cm
   reach    5th =  75 - 1.645*5  =  66.8 cm    95th =  75 + 1.645*5  =  83.2 cm
```

Each single-dimension "5th–95th" band captures the central **90%** of *that one*
dimension. The trap of §1.1 is what happens when one design constrains **both** at once.

### Q2. Joint accommodation is not the product of the marginals

Ask: what fraction of people fall inside [5th, 95th] on stature **and** [5th, 95th] on
reach *simultaneously*?

```
JOINT ACCOMMODATION  (why "90% each" is not "90% of people") -- bivariate schematic
--------------------------------------------------------------------------------
   reach Y
   95th ^         . .                    the univariate BOX = [5th,95th] on EACH
        |     . :::::: .                 dim; its CORNERS are nearly empty --
        |   . ::::::::::: .              almost nobody is 95th-stature AND
   50th |    . ::::::@::::: .            5th-reach at once when rho = 0.5.
        |      . ::::::::: .
        |        . :::: .                the real ACCOMMODATION HULL is the
    5th +--------------------------->    TILTED ellipse, not the axis-aligned box.
           5th       50th       95th  stature
   -----------------------------------------------------------------------------
   INDEPENDENT (rho = 0):     P(both central) = 0.90 * 0.90        = 0.8100
   POS. CORRELATED (rho=0.5): standard-bivariate-normal box mass  ~= 0.8245
   -> the JOINT fraction is BELOW 90%; multiplying or averaging the marginals does
      NOT recover it. Accommodate the JOINT hull (boundary manikins / a PCA family).
```

**Reproducible core (method + inputs).** For **independent** dimensions the joint central
fraction is exactly `0.90^k` — **0.8100** for two dimensions, **0.729** for three, **0.656**
for four — so coverage falls fast as constraints stack. For **correlated** dimensions the
fraction is the probability mass of the standard bivariate normal inside the square
`[-1.645, +1.645] x [-1.645, +1.645]`, read from the bivariate-normal CDF `F2(a, b; rho)` by
inclusion–exclusion:
`P = F2(z, z; rho) - F2(-z, z; rho) - F2(z, -z; rho) + F2(-z, -z; rho)`, with `z = 1.645`.
At `rho = 0.5` this evaluates to **~= 0.8245** — above the independent **0.8100** and below
any single dimension's **0.90**. Because `rho` is itself an uncertain, dataset-dependent
estimate and **not** a constant, the honest reading is a **bounded range, not a point**:
across a plausible `rho` from **0.3 to 0.7** for partly-correlated body dimensions the joint
fraction moves only within **~0.815 to ~0.839**, so the conclusion (**~0.82**, below 0.90,
just above 0.81) is robust to the exact `rho`. The fully honest target is the mass inside the
**actual joint distribution** — which is exactly why the fix is boundary manikins / PCA, not
arithmetic on the marginals.

**Uncertainty / validity note.** The means, SDs, and `rho` are assumed, and `rho` in
particular is a **point estimate carrying its own sampling error** (hence the bounded-range
reading above, not a single 0.8245); a real design owes a provenance statement (§3) and,
ideally, a local sample. The normal model is itself an approximation (real dimensions are
mildly skewed), so treat the tail percentiles and the joint fraction as estimates carrying
their own error, not exact cut-points.

### Q3. A bounded NIOSH lifting-index sensitivity (synthetic inputs)

Using the model structure of §6 (RWL = LC * HM * VM * DM * AM * FM * CM; LC = 23 kg) with
the standard multiplier forms, on **one synthetic task** with fully stated geometry, lift
frequency, duration, and coupling:

| Term | Synthetic input | Multiplier form / lookup | Value |
|---|---|---|---|
| LC | ideal-condition baseline | 23 kg | 23.00 |
| HM | H = 30 cm | 25 / H | 0.833 |
| VM | V = 75 cm | 1 - 0.003*abs(V-75) | 1.000 |
| DM | D = 50 cm | 0.82 + 4.5 / D | 0.910 |
| AM | A = 30 deg | 1 - 0.0032*A | 0.904 |
| FM | F = 3 lifts/min, short-duration class: <= 1 h with recovery >= work time, V >= 75 cm | frequency table | 0.88 |
| CM | fair coupling, V >= 75 cm | coupling table | 1.00 |

The two lookup terms are read from named cells of the **public-domain** applications manual
(NIOSH 94-110); the exact cells used are reproduced as a **bounded excerpt** so the numbers
are traceable rather than asserted — and so the coupling term matches the *stated* vertical
height, which is the subtle correctness point:

```
ILLUSTRATIVE LOOKUP EXCERPT  (public-domain NIOSH 94-110; cells used here)
--------------------------------------------------------------------------------
   FREQUENCY MULTIPLIER FM   (short duration <= 1 h, recovery >= work time,
                              V >= 75 cm column)
      F = 1 /min -> 0.94     F = 2 /min -> 0.91     F = 3 /min -> 0.88
   COUPLING MULTIPLIER CM
      GOOD            -> 1.00 (any V)
      FAIR, V >= 75   -> 1.00        FAIR, V < 75 -> 0.95
      POOR            -> 0.90 (any V)
   => at V = 75 cm (which is >= 75) with FAIR coupling, CM = 1.00 -- the V < 75
      value 0.95 would be WRONG for this stated height.
```

`RWL = 23 * 0.833 * 1.000 * 0.910 * 0.904 * 0.88 * 1.00 ~= 13.88 kg`. For a synthetic
handled load of **15 kg**, the **Lifting Index** `LI = 15 / 13.88 ~= 1.08` (> 1: modeled
demand exceeds the model's recommended limit for this synthetic population). Now hold every
other term fixed and **sweep the horizontal distance H** — the term §5 predicts dominates:

```
LI SENSITIVITY TO HORIZONTAL DISTANCE  (synthetic; load held at 15 kg)
--------------------------------------------------------------------------------
   H (cm)   HM = 25/H     RWL (kg)     LI = 15/RWL
   -----------------------------------------------------------------------------
     25       1.000         16.65         0.90     (LI < 1)
     30       0.833         13.88         1.08
     35       0.714         11.89         1.26
     40       0.625         10.41         1.44     (LI ~ 1.5)
   -----------------------------------------------------------------------------
   Reading: a 15 cm increase in HORIZONTAL distance ALONE drives LI from ~0.90 to
   ~1.44 -- the model says horizontal distance dominates, exactly as the moment-arm
   physics of §5 predicts. VM/DM/AM/FM/CM are held constant here to isolate HM.
```

**Uncertainty / validity notes (mandatory whenever an LI is quoted).**
- **Input error propagates.** Because `HM = 25/H`, a ±2 cm measurement error in `H` near
  30 cm shifts HM (and thus LI) by roughly **±7%** — the index is only as good as the
  measured geometry.
- **FM and CM are table lookups**, not formulas; here `FM = 0.88` (F = 3 lifts/min,
  short duration <= 1 h **with recovery time at least equal to the work period**,
  V >= 75 cm) and `CM = 1.00` (fair coupling at V >= 75 cm) are read from
  the bounded corrected electronic edition of the NIOSH 94-110 applications manual.
  Changing the frequency, duration/recovery class, or coupling
  class — or dropping V below 75 cm, which flips fair-coupling CM to 0.95 — moves RWL
  materially; the multipliers are correct only for the *stated* inputs.
- **The model is silent outside its domain (§6.1).** If the synthetic lift became
  one-handed, jerky, or handled an unstable load, **no** valid LI exists — a low LI is not
  proof of safety, and an out-of-domain task has no LI at all.
- **LI is a population index, not a per-person verdict** and not a certification; this pass
  is conceptual literacy, not a lifting assessment and not instruction.

---

## A Fully Worked Case — Accommodating a Task (illustrative, fictional)

*Fictional throughout. It demonstrates the reasoning, and is explicitly **not** an
assessment of any real job, worker, or product, and **not** operational instruction.*

**Setting.** *Meridian Freight* (invented) wants a **new parcel-induction bench** where
operators move totes from a floor cart onto a scanning surface, all shift. The question
posed to human factors: *which bodies can do this, at what modeled load, and where does
it break?* Nothing below tells anyone how to lift; it shows how the models reason.

1. **Frame fit as multivariate.** The governing dimensions are functional forward reach
   (to the cart), knee/thigh clearance under the bench, and standing elbow height (bench
   surface). Sized univariately, "5th–95th each" would *overstate* coverage (§1.1); the
   team instead spans a **boundary-manikin family** (short-reach/short-stature through
   tall/long-limb) and checks all three constraints jointly.
2. **Apply the four moves (§2) as design hypotheses, not directives.** Bench height is a
   **two-sided** constraint, so a *fixed* height necessarily excludes one tail while an
   **adjustable** range (roughly 5th-percentile-female to 95th-percentile-male standing
   elbow height) is the variant that *would* accommodate both — a hypothesis to validate
   locally, not an instruction to build. Reach to the cart is **one-sided**: a variant with
   the cart nearer the operator lets a **5th-percentile** reach succeed without trunk
   flexion, whereas a farther cart excludes it — a modeled comparison, not a placement
   order. Any slide force is compared against a **low-capacity** percentile. Which variant
   is actually adopted is a matter for **qualified assessment and local validation**.
3. **Read the load, not just the fit (§5–6).** The lift starts low (floor cart) and
   ends at bench height, sometimes twisting toward the scanner. Conceptually, the model's
   **horizontal**, **vertical**, and **asymmetry** terms each discount the baseline, and a
   high **frequency** (totes/min, full shift) discounts it further — so the *modeled*
   Lifting Index climbs with distance, twist, and rate. Treated as a **design-variable
   analysis**, the model lets the team *compare hypothetical variants* — a variant with the
   cart nearer vs farther changes HM; a raised-origin variant changes VM; a twist-free
   linear-layout variant changes AM — and read which variable the modeled LI is most
   sensitive to (§Q3 shows horizontal distance). These are **model comparisons, not
   recommendations**: any actual change to cart placement, lift origin, layout, or rate is a
   hypothesis that requires **qualified assessment and local validation** before use.
4. **Name the validity limits (§6.1).** If totes turn out to be **unstable** (shifting
   contents) or the lift becomes **one-handed** while scanning, the equation is **silent**
   — those tasks are outside its domain, and the analysis must switch tools (e.g., a
   psychophysical Snook-table view), not pretend a number applies.
5. **State exclusions and environment explicitly (§2.1, §6.1, §7).** The chosen
   accommodation target names the excluded tail and why. Environment enters as an
   **out-of-model modifier**, not as a term in the lifting equation: extreme heat sits
   **outside the RNLE's validity domain** (§6.1 — the model assumes a moderate thermal
   environment), so the equation does **not** quantify it and **no "hot RWL" is computed**
   from it; heat's cardiovascular effect is treated qualitatively (§7) and, where it
   matters, by tools that actually model thermal strain. The in-model sensitivity the team
   *can* legitimately read is over a variable the equation contains — the horizontal-distance
   sweep of §Q3 — not over temperature. Any change to conditions or pace is, again, a matter
   for **qualified assessment and local validation**; the guide models the envelope, it sets
   no schedule.

**Reading.** Every output is a **modeled, population-level design record with named
exclusions and a stated validity domain** — the fit is multivariate, the load is
dose–response, the lifting index is a lens not a verdict, and nothing here is a
certification, a medical judgment, or a lifting procedure.

---

## Reader Tasks (answerable from this guide)

1. **Compute joint accommodation.** With stature ~ N(170, 10) and reach ~ N(75, 5) (§Q1),
   compute each dimension's 5th/95th percentiles, then — treating them as **independent** —
   compute the joint fraction inside the [5th,95th] x [5th,95th] box (`0.90^2`). Explain why
   the *true* fraction differs once `rho > 0` — for `rho = 0.5` the bivariate-normal box mass
   is `~= 0.8245`, between the independent `0.81` and the marginal `0.90` — and what
   "accommodate the joint hull" means instead of stacking univariate percentiles.
   (§1.1, §Q1–Q2.)
2. **Pick the tail and resolve a conflict.** For "how wide must the escape hatch be?" choose
   a **high** clearance percentile; for "how far can the emergency stop be?" a **low** reach
   percentile; for "how much force may the latch need?" a **low** capacity percentile —
   justify each from its failure mode, then resolve the **two-sided** seat-height conflict
   (tall knee-clearance vs short foot-reach) and say why adjustability wins. (§2.)
3. **Interrogate a percentile and bound its error.** Given "the 95th-percentile stature is
   187 cm from ANSUR II (2012)," state the three provenance questions (whose population, from
   when, measured how), then reason about the **direction and rough size** of the error if
   you applied that figure to a shorter, older civilian population — and how you would widen
   your stated uncertainty. (§3.)
4. **Compute and stress a Lifting Index.** For the §Q3 synthetic inputs, compute the **six
   multipliers**, RWL, and LI; then increase **H** by 10 cm and recompute, explaining (via
   the moment arm, §5) why horizontal distance dominates. Name one validity-domain condition
   (§6.1) that would make the LI **invalid**, and say why a low LI is still not proof of
   safety — without giving any lifting instruction. (§5, §6, §6.1, §Q3.)
5. **Draw the product↔workplace line and the evidence-and-acceptance boundary.** Assign the handle
   *form* to `industrial-design/05` and the population accommodation, load model, and
   work–rest modeling to `human-factors/02`; then, for an induction bench that adds a
   **touchscreen**, allocate the interaction/accessibility *method* to
   `   human-computer-interaction/`, the safety/workload **evidence and validation** to
   human factors, and **acceptance and implementation to the accountable domain
   organization / regulator** (no reference module signs off a real system). (§8.)

---

## Decision Cheat Sheet

| Situation | Move | Why (this guide) |
|---|---|---|
| Sizing a minimum space/opening | design to a **high** percentile (95th/99th) | if the largest fits, all smaller fit — clearance (§2) |
| Placing a control that must be reached | design to a **low** reach percentile (5th/1st) | if the shortest reach succeeds, all longer do (§2) |
| Setting a force/actuation demand | design to a **low** capacity percentile | the weakest accommodated user sets the max force (§2) |
| One size can't fit both tails | **adjustability** spanning the accommodated range | two-sided constraint (seat height + footrest) (§2) |
| Claiming "90% accommodated" | verify **multivariate**, not k univariate percentiles | joint coverage < any single-dimension 90% (§1.1) |
| Handed a percentile table | ask **whose / when / how measured** | dated, sampled estimate; secular trend; provenance (§3) |
| A weight seems "fine" | check **posture & horizontal distance**, not just mass | moment arm multiplies spinal load (§5) |
| Screening posture/repetition | use RULA/REBA/OWAS/Snook as **bounded flags** | ordinal indices to prioritize study, not certify (§5.2) |
| Reasoning about a manual lift | use NIOSH RWL/LI as a **model**, mind its **domain** | LI>1 raises risk; out-of-domain = silent (§6, §6.1) |
| Hot/vibrating/long-shift task | compare recovery-demand hypotheses across the **exposure envelope** | environment and duration modify load; any schedule requires qualified local assessment (§7) |
| "What does the body touch, and how shaped?" | route to **`industrial-design/05`** | product-form ownership (§8) |
| Actual injury / fitness / compliance question | **out of scope** → clinical/medicine; no legal ruling | safety contract, banner |

---

## Common Confusion Points

**"Design for the average user."** The 50th-percentile-on-everything body does not exist;
partial correlation across dimensions makes it vanishingly rare. Design for a **range** of
each constraining dimension, and verify accommodation on the **joint** distribution, not a
stack of univariate percentiles (§1.1).

**"5th–95th on each dimension means 90% of people fit."** No. Because dimensions are only
partly correlated, the fraction inside the box on **all** constraining dimensions at once
is **lower** than 90% and shrinks as you add dimensions. Multivariate accommodation
(boundary manikins / PCA) is the fix (§1.1).

**"Anthropometric tables are the human body."** Every table is a **survey** — a population,
an era, a method. ANSUR II is fit soldiers in 2012; CAESAR is late-1990s Western
civilians; secular trends age all of them. Name the source and its bounds (§3).

**"A low Lifting Index proves the job is safe."** No. LI is a **model output** with a
validity domain; a low LI inside the domain means *modeled* demand is within the model's
recommended limit for most workers — not that a specific worker or task is safe, and
outside the domain there is **no valid LI** at all (§6.1). This guide gives no lifting
instruction.

**"Comfort is the goal of ergonomics."** Function and injury-risk are the goals; comfort
often follows, but a comfortable posture that accumulates static load can still injure
over a career. The target is load within tolerance across the shift, for the population
(§5).

**"Ergonomics = the shape of the handle."** That product-form view is real but partial and
lives in `industrial-design/05`. Human factors owns the **distribution**, the
**occupational load models**, and the **system of work over time** (§8).

---

## Global, WEIRD & Resource Caveats

- **The data canon is Western- and military-skewed.** The most-cited detailed sets
  (ANSUR, CAESAR) over-represent Western and/or military bodies; using them for other
  populations silently mis-sizes the tails. Global or region-specific surveys exist but
  are unevenly available — the honest design record names which population its percentiles
  actually describe.
- **Screening indices were validated on particular workforces.** RULA/REBA/OWAS/Snook and
  the NIOSH equation were developed and validated largely in industrialized settings and
  populations; their bands and constants are **not** guaranteed to transfer to different
  body distributions, tasks, or climates without revalidation.
- **Accommodation targets encode who counts.** Choosing "5th–95th" rather than "1st–99th"
  is a decision about **whom to exclude**; defaulting to a narrow, majority-centered range
  disproportionately excludes the smallest and largest bodies, which correlate with sex,
  age, and region. State the target and the excluded tail explicitly.
- **Resource asymmetry shapes practice.** 3D scanning, digital human models (RAMSIS,
  JACK), and current regional surveys are resource-rich-organization tools; low-resource
  settings often reuse old or foreign tables, magnifying the provenance and secular-trend
  errors above. The correction is to state the uncertainty, not to hide it behind a
  borrowed percentile.

---

## A Contrasting Example (non-WEIRD, low-resource)

*Fictional, to show how the same reasoning changes when population and resources are not
the Western-industrial default.*

**Setting.** A cooperative in a *fictional* highland region equips a small tea-sorting
workshop. There is **no local anthropometric survey**, the workforce is on average
**shorter** than the ANSUR/CAESAR populations, mixed-sex, and older, and there is no
budget for scanning or digital human models.

**What breaks if you copy a Western analysis wholesale.**
- **Borrowed percentiles mis-size the tails.** A 95th-percentile clearance taken from a
  Dutch table over-builds, and a 5th-percentile reach taken from a tall population leaves
  the *actual* shortest workers unable to reach — the population's real distribution is
  shifted and possibly differently shaped. The correction is to treat the foreign table as
  a **rough prior**, gather a small local sample on the governing dimensions, and widen the
  uncertainty explicitly.
- **The lifting model's constants are foreign.** The RWL load constant and the
  psychophysical Snook percentages come from other workforces; here they are, at best, a
  **conceptual lens** for *comparing variants* — whether a nearer vs farther load changes the
  horizontal term, a higher vs lower origin changes the vertical term, or a twist-free vs
  twisting layout changes the asymmetry term — not a numeric verdict and not a directive to
  alter any real task.
- **Adjustability beats precision.** With unknown distributions, **adjustable** benches and
  cart heights (span a generous range) accommodate more of an unmeasured population than a
  single "optimal" fixed size computed from the wrong table.

**Reading.** The **method** — fit as multivariate accommodation, load as dose–response,
models as bounded lenses with named domains — transfers; the **numbers** do not. Stating
which population your percentiles describe, and how much you are extrapolating, is part of
the result.

---

## Guide-Family Scaling Contracts (how this discipline extends)

This guide is the module's **scaling-gate prototype**: it proves, on the hardest
quantitative-and-boundary surface (population modeling + the `industrial-design/05`
overlap + a bounded exposure model), the pattern the other eleven guides inherit. Each
family gets a **bounded** contract — the object it models, the discipline it must keep,
and the **test that would fail it** — so the pattern is checkable, not a slogan.

- **Overview (`00`).** Not a modeling object; checked for **coverage and boundary
  integrity**. *Fails if* any human-factors concept is unclaimed or double-claimed, or the
  ownership/defer matrix contradicts a guide.
- **History & foundations (`01`).** Judged by **attribution and dating**, not by any
  model. *Fails if* it universalizes a dated figure or imports exposure math where a
  historical claim belongs.
- **Cognitive workload & SA (`03`).** Its objects are **workload and situation-awareness
  measures**; the invariant is *measure-in-context, defer the mechanism to
  `cognitive-science/`*. *Fails if* NASA-TLX or SAGAT is read as a universal constant, or
  a cognitive mechanism is re-derived here.
- **Human error taxonomies (`04`).** Errors are **classified against a model** (slip/lapse/
  mistake; Reason's levels), never moralized. *Fails if* a taxonomy becomes a blame ledger
  or a legal finding.
- **Human reliability analysis (`05`).** HEPs are **bounded model outputs**, exactly like
  this guide's LI. *Fails if* a human error probability is stated as a precise fact rather
  than a wide, method- and context-bounded estimate, or the underlying FTA/reliability
  math (owned by `systems-engineering/06`) is re-derived.
- **Display, control & control-room design (`06`).** Its claims are **compatibility/
  salience/alarm** claims for operator performance; it owns *what goes where and why*,
  deferring digital usability to `human-computer-interaction/`. *Fails if* it issues a
  runnable operating procedure or certifies a real control room.
- **Automation & human–machine (`07`).** Level-of-automation and trust/complacency are
  **design trade-offs**, bounded by the ironies-of-automation frame; domain autopilots
  defer to `aeronautics/`/`transportation/`. *Fails if* automation is treated as pure
  workload reduction with no new failure modes.
- **Safety systems & hazard analysis (`08`).** Hazard methods are **structured models**
  (barriers, Swiss cheese, HAZOP-style reasoning) borrowing FTA/FMEA from
  `systems-engineering/06`. *Fails if* it certifies a system or rules on an accident.
- **Domain applications (`09`).** Aviation/healthcare/process/rail cases **apply** the
  models and **defer** domain systems to their owners (`aeronautics/`, `nuclear/05`,
  `clinical-medicine/11`, `biomedical-engineering/07`, `transportation/`). *Fails if* it
  re-teaches a domain system or issues domain operating advice.
- **Methods & measurement (`10`).** Owns **how** physical/cognitive measures are taken
  (instrumentation, study design), deferring inferential statistics to
  `statistics-applied/`. *Fails if* a convenience sample is generalized without a coverage
  argument.
- **Organizational & safety culture (`11`).** Judged against **value and evidence**, not a
  metric to maximize; overlaps `clinical-medicine/11` (just culture) and
  `organizational-behavior/`. *Fails if* culture is reduced to a single score or a
  compliance checkbox.

The invariant across every family: **name the model and its inputs, state its validity
domain and who/what population it covers, keep the safety/ethics contract (no operational
instruction, no certification, no accident/legal ruling, no individual fitness
assessment), and route product-form to `industrial-design/05` and mechanism to
`cognitive-science/`.** That invariant — not any single percentile or multiplier — is what
this scaling-gate prototype exists to prove.

### Testable Definition of Done (the scaling contract for the nine remaining guides)

The per-family invariants above say *what each guide keeps*; this contract says *how a
reviewer proves it*. Every remaining guide — `00`, `01`, `04`, `05`, `07`, `08`, `09`,
`10`, `11` — is **done** only when it passes the **eight gates** below **and** the **common
safety & accessibility contract**. Each gate is written to be marked pass/fail, not admired.

**The eight gates (apply to every guide 00–11).**
1. **Required formal model(s) named** — the guide's load-bearing model(s) appear
   explicitly, attributed and dated.
2. **Minimum quantitative demonstration** — at least one reproducible, synthetic worked
   computation (or, for a non-quantitative guide, a structured worked classification) with
   inputs and outputs shown.
3. **Uncertainty / validity / bias analysis** — the demonstration states its validity
   domain, its error/uncertainty, and the WEIRD/population/resource bias in its data or
   instruments.
4. **Source hierarchy / edition verification** — every standard/dataset cites a
   primary/authoritative source at the correct level of the source hierarchy and a specific
   **edition/year**, *verified against that source*. Citation-risk may be logged while
   authoring, but **no citation-risk item may remain unresolved at sign-off** (see the
   closure gates).
5. **Boundary test** — an explicit ownership/defer statement naming what the guide does
   **not** own (the sibling/domain module) plus a case that exercises the boundary.
6. **Conceptual diagram** — at least one terminal-readable diagram doing real conceptual
   work (not decoration), in the PROOF-safe open idiom.
7. **Worked fictional case** — one fully worked, explicitly fictional, non-operational case
   demonstrating the reasoning end to end.
8. **3–5 reader tasks** — answerable from the guide and requiring **calculation /
   interpretation / uncertainty / boundary resolution**, not recall.

**The closure gates (a guide is signed off only when ALL of these also hold).** Gates 1–8
prove the *content*; these prove the guide is genuinely *done, truthful, and independently
cleared*, not merely drafted:
9. **Ordinary PROOF passes** — the guide passes the repo's **standard** PROOF run (not only a
   focused subset), with **no unresolved BLOCK or WARN** anywhere in the guide.
10. **Truthful metadata & source-custody transition** — frontmatter matches reality at each
    stage: `status: prototype` / `source_custody: needs-source` / `backsource_ids: []` while
    pre-backfill, promoted to real source-custody (status advanced, `backsource_ids`
    populated, custody transitioned) **only after** source-corpus backfill has actually run
    and its artifacts exist. Metadata may never claim a backfill/custody/history artifact
    that does not exist.
11. **Source-hierarchy / edition & citation-risk closure** — every load-bearing figure is
    verified against a primary/authoritative source at the correct hierarchy level and
    edition; **citation risk cannot remain unresolved at sign-off** (a logged risk is an
    open item, not a done one).
12. **Independent adversarial closure** — a strict, **independent** re-review (the R2
    pattern: the reviewer neither authored nor repaired the findings) signs off with no
    unresolved BLOCK/WARN. Findings that were self-raised and self-repaired in one pass do
    **not** ratify.
13. **Records & integration closure** — STATUS, the architecture record, the pulse/wave
    records, `sections/`, `.mkdocs/mkdocs.yml`, `TRACKER.md`, and the reciprocal sibling
    pointers are all updated and mutually consistent, and the source-corpus artifacts
    (PROOF/CROP/MDPORT/FLETCH) are regenerated and agree with the guide.

**Per-guide specifics (the parts that vary).**

| Guide | Required formal model(s) | Minimum quantitative demonstration | Boundary test (must defer) |
|---|---|---|---|
| `00` Overview | discipline map + ownership/defer matrix | coverage check: every concept claimed once, no gaps/overlaps | not a modeling guide; duplicates no guide's content |
| `01` History | dated lineage (scientific management -> WWII -> Fitts/Chapanis -> resilience) | a timeline with attributed dates; one figure shown as dated, not universal | defers mechanism to `cognitive-science/`; imports no exposure math |
| `04` Error taxonomies | Reason slip/lapse/mistake + SRK; latent conditions | worked classification of >=3 synthetic events to levels, with rationale | error is a systems property; defers clinical taxonomy to `clinical-medicine/11`; no blame/legal finding |
| `05` HRA | THERP/HEART/SPAR-H HEP as a bounded estimate; PSFs | a synthetic HEP shown as a wide **range**, not a point | borrows FTA/reliability math from `systems-engineering/06`; no re-derivation |
| `07` Automation | levels of automation (Sheridan; Parasuraman-Sheridan-Wickens); ironies (Bainbridge) | synthetic function-allocation table scored on workload/OOTL trade-offs | domain autopilots defer to `aeronautics/`/`transportation/`; automation adds failure modes |
| `08` Hazard analysis | barrier/Swiss-cheese; HAZOP/bow-tie/STAMP-STPA | synthetic bow-tie or human-inclusive FMEA with >=1 quantified branch | borrows FTA/FMEA from `systems-engineering/06`; certifies nothing |
| `09` Domain applications | the apply-and-defer pattern across >=2 domains | synthetic cross-domain case applying `02`/`03`/`06` models | re-teaches no domain system; defers to `nuclear/`, `aeronautics/`, `clinical-medicine/11`, `transportation/`, `bme/07` |
| `10` Methods | HTA/CTA; observation; simulation; instrumentation | synthetic study design with a coverage/sampling argument | inferential statistics defer to `statistics-applied/` |
| `11` Safety culture | Safety-I vs Safety-II; HRO; just culture | synthetic reporting-metric read with its confounds/limits | overlaps `clinical-medicine/11` and `organizational-behavior/`; not one score |

**Common safety & accessibility contract (every guide 00–11).**
- **Safety/ethics contract** — no operational instruction, no certification/compliance
  ruling, no accident/legal determination, no individual fitness-for-duty assessment; every
  model/standard/stereotype attributed, dated, and bounded.
- **Accessibility as a safety requirement** — information a safe design depends on rides on
  **>=2 coding channels** (never color or text alone); this is the operator-safety twin of
  HCI/accessibility's "don't rely on color alone" (guide `06`, §3).
- **HCI/HF/domain evidence & acceptance** — where a guide's system includes an
  interactive/digital interface, the modules own **methods and evidence, not sign-off**:
  `human-computer-interaction/` supplies interaction/visualization/accessibility
  *methods/evidence*; human factors supplies the safety, workload/error, and
  performance-under-stress **evidence**; and **acceptance and implementation belong to the
  accountable domain organization and its regulator**, not to any reference module.
  Safety-critical systems remain HCI systems.
