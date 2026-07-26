---
maxim_schema: maxim.frontmatter.v1
id: maxim:clinical-medicine:overview
kind: guide
module: clinical-medicine
section: clinical-medicine
title: Clinical Medicine - Discipline Map, Competency Spine, and the Non-Advice Contract
status: source-custody
source_custody: partial
current_path: clinical-medicine/00-OVERVIEW.md
canonical_path: clinical-medicine/00-OVERVIEW.md
backsource_ids: [proof-backfill:clinical-medicine:00-overview]
concepts: [clinical-medicine, clinical-reasoning, care-architecture, competency-frameworks, non-advice-contract]
root_concepts: [clinical-medicine]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Clinical Medicine — Discipline Map, Competency Spine, and the Non-Advice Contract

Clinical medicine is the discipline that **turns knowledge about disease into decisions
for one person under uncertainty**. This module is the peer-level reference for the
*transferable cognitive and system architecture* of that discipline — how a clinician
gathers information, forms and ranks hypotheses, updates belief with tests, weighs
evidence, organizes care over time, hands work across interfaces, and keeps the whole
system safe. It is the **reasoning-and-care apex** of MAXIM's Life Sciences vertical
(molecular → cellular → organismal → population → **clinical**): the layer that
*selects, sequences, and governs* everything the modules below it describe.

> **This module is an educational reference about *how clinical medicine reasons and
> how care is organized* — the cognitive and system architecture of the discipline.
> It is *not* medical advice. It does not diagnose, does not give treatment, dosing,
> or procedure instructions, does not give emergency or first-aid instructions, and
> is *not a substitute* for evaluation by a licensed clinician. Worked cases are
> illustrative teaching vignettes showing *how a clinician thinks*, not what any
> reader should do. For personal concerns, appropriate care comes from qualified
> local professionals; emergencies are handled through local emergency services.**

*Per-guide banner: this overview maps the discipline and its module boundaries — not
medical advice and not a self-assessment tool. Competency frameworks and any numeric
examples are attributed and dated as illustrations of how the field is structured.*

---

## The Big Picture: Medicine as a Decision-and-Care Pipeline

The novice model of medicine is a lookup table: symptom → disease → drug. The expert
model is a **pipeline that runs under uncertainty**, with belief updated at each stage
and decisions gated by what would actually change management. This module owns the
*pipeline and its control logic*, not the biological tables it consults.

```
CLINICAL MEDICINE AS A PIPELINE  (this module owns the arrows + the control logic)
==========================================================================
  ENCOUNTER (01)         gather + structure information -> problem representation
        |                 history/physical as information architecture
        v
  DIFFERENTIAL (02)      hypotheses, ranked: likely + must-not-miss (a PRIOR)
        |                 dual-process reasoning; bias + debiasing
        v
  TESTING (03)           update belief; act only if a threshold can be crossed
        |                 2x2 as belief engine; LR/odds Bayes; VOI
        v
  EVIDENCE (04)          is the proposed action supported? for WHOM?
        |                 PICO; hierarchy; GRADE; ARR/NNT; external validity
        v
  CARE OVER TIME (05,06) acute prioritization (concept) vs chronic trajectories;
        |                 multimorbidity, competing risks, deprescribing
        v
  HANDOFFS (07,08)       move state without loss across time + across services
        |                 I-PASS/SBAR; med reconciliation; closed loops; referral
        v
  PREVENTION (09)        shared decisions before disease; screening harms + biases
        |
        v
  ETHICS + SAFETY (10,11)  consent/capacity/justice; Swiss-cheese, RCA, SPO, PDSA
==========================================================================
  Read top-to-bottom as care flows; every stage is a belief update or a state
  transfer, and every stage has a characteristic failure mode this module names.
```

**The load-bearing idea:** medicine's *transferable* content is the organ-agnostic
reasoning move — problem representation, Bayesian updating, threshold decisions,
evidence appraisal, deprescribing logic, closed-loop handoffs — not the per-organ
catalog. This module is therefore organized **around reusable reasoning patterns, not
per-organ specialties** (the single most important non-duplication decision; specialties
appear in guide 08 as an *interface catalog*, not a disease catalog).

**Bridge (software).** This is a request-processing pipeline with a control plane. The
encounter is input parsing and normalization; the differential is a ranked hypothesis
set (a prior); testing is a Bayesian filter that updates state only when the update can
flip a downstream branch; evidence appraisal is the policy layer deciding whether an
action is warranted and for which population; care-over-time is long-running stateful
orchestration; handoffs are state transfer across process and service boundaries; and
safety/quality is the observability-plus-postmortem layer. Most catastrophic failures
are at the seams (dropped state, unowned callbacks), not inside any one stage.

---

## The Competency Spine: What the Discipline Officially Comprises

A module about "how medicine reasons" risks reading as one author's taxonomy. It is
anchored instead to the two frameworks that formally define physician competence, so the
guide map is a *recognizable* map of the discipline rather than an invented one. Both are
attributed and dated; both are Anglo-American in origin (a bias flagged below).

**ACGME six core competencies** (Accreditation Council for Graduate Medical Education,
US; adopted with the ABMS c. 1999, the "Outcome Project"): the domains every US
resident is assessed against.

```
  ACGME-6  (competency domains)              -> where this module develops it
  --------------------------------------------------------------------------
  1 Patient Care (PC)                        -> 01, 02, 03, 05, 06
  2 Medical Knowledge (MK)                   -> assumed floor (disease/, human-biology/)
  3 Practice-Based Learning & Improvement    -> 04 (EBM), 11 (PDSA, QI)
  4 Interpersonal & Communication Skills     -> 07 (handoffs), 09/10 (shared decisions)
  5 Professionalism (PROF)                   -> 10 (ethics, consent, confidentiality)
  6 Systems-Based Practice (SBP)             -> 07, 08, 11 (interfaces, safety, workflow)
  --------------------------------------------------------------------------
  MK is the ONLY domain this module defers wholesale (it is disease + physiology +
  pharmacology). The other five ARE the transferable architecture this module owns.
```

**AAMC Core EPAs** (Association of American Medical Colleges, *Core Entrustable
Professional Activities for Entering Residency*, 2014): thirteen concrete units of work a
graduating student should be trusted to do. EPAs are *observable activities* (unlike the
abstract competencies), so they map almost one-to-one onto the guides.

| EPA | Activity (abbreviated) | Owned/developed by |
|---|---|---|
| 1 | Gather a history and perform a physical exam | 01 |
| 2 | Prioritize a differential diagnosis | 02 |
| 3 | Recommend and interpret common diagnostic/screening tests | 03, 09 |
| 4 | Enter and discuss orders and prescriptions | 06 (reasoning only; **no dosing**) |
| 5 | Document a clinical encounter | 01, 07 (problem list as shared state) |
| 6 | Provide an oral presentation of a clinical encounter | 01, 07 |
| 7 | Form clinical questions and retrieve evidence | 04 |
| 8 | Give or receive a patient handover | 07 |
| 9 | Collaborate as an interprofessional team member | 07, 08, 11 |
| 10 | Recognize a patient needing urgent/emergent care and initiate | 05 (**conceptual prioritization only**) |
| 11 | Obtain informed consent for tests/procedures | 10 |
| 12 | Perform general procedures of a physician | **out of scope** (would invite how-to; see safety contract) |
| 13 | Identify system failures and contribute to a safety culture | 11 |

The AAMC **PCRS** (Physician Competency Reference Set) adds *interprofessional
collaboration* and *personal/professional development* as explicit domains; this module
threads both through guides 07–11 rather than giving them a separate file. EPA 12
(procedures) is deliberately unowned: a procedures guide would pull the module toward
step-by-step how-to and breach the non-advice contract.

---

## What Each Guide Owns (and Where NOT to Look Here)

The module is 12 guides: `00` (this map) plus 11 numbered guides. Each opens with an
ownership header so navigation errors are cheap to catch. The split is **by reasoning
problem, not by organ or by disease**.

| # | Guide | Uniquely owns (peer depth) | Explicitly defers to |
|---|-------|----------------------------|----------------------|
| 01 | Clinical Encounter | H&P as information architecture; problem representation, semantic qualifiers, illness scripts | exam technique/how-to → clinical training; anatomy/physiology → `human-biology/` |
| 02 | Differential Diagnosis | dual-process; diagnostic schemas; likely vs must-not-miss; bias + debiasing; NASEM framing | disease catalogs/mechanisms → `disease/` |
| 03 | Diagnostic Test Interpretation | decision theory: 2×2 belief engine, LR/odds Bayes, thresholds, VOI | the test **catalog**, ranges, imaging physics → `medicine/10` |
| 04 | Evidence-Based Medicine | PICO; hierarchy; GRADE; ARR/RRR/NNT; external validity; surrogates | study-design mechanics, meta-analysis stats → `public-health/`, `statistics-applied/` |
| 05 | Acute and Chronic Care | two care logics: acute prioritization (concept) vs chronic longitudinal (trajectories, CCM) | emergency/first-aid technique → out of scope; drugs → `pharmacology/` |
| 06 | Multimorbidity & Geriatrics | competing risks; guideline collision; polypharmacy/cascades/deprescribing; 5Ms; time-to-benefit | drug classes, PK/PD → `pharmacology/`; **no dosing** |
| 07 | Care Transitions | handoffs as information transfer (I-PASS, SBAR); med reconciliation; problem list as shared state | — (module-unique) |
| 08 | Specialty Interfaces | specialty map as service/interface catalog; referral/comanagement ownership; closed loops | the diseases themselves → `disease/`; financing/workforce → `public-health/08` |
| 09 | Prevention & Screening | individual-level SDM; overdiagnosis; lead/length-time bias; three-talk | screening **programs**/policy, population prevention → `public-health/` |
| 10 | Ethics, Consent, Capacity | four principles; consent; Appelbaum capacity; surrogates; confidentiality; justice | normative ethical theory → `ethics/` |
| 11 | Safety, Quality & Workflow | Swiss-cheese, RCA, just culture, HRO; Donabedian SPO; PDSA; diagnostic safety; EHR loops | device engineering → `biomedical-engineering/` |

**The rule this module follows everywhere:** if another MAXIM module already owns the
*content* (a disease, a drug, a physiology, a population method), this module names it by
reference and owns only the *reasoning that selects and governs it*. When two guides touch
the same object, the split is by **question**: `disease/` says *what pneumonia is*;
`clinical-medicine/02` says *how a clinician ranks pneumonia against its mimics*;
`medicine/10` lists *the test*; `clinical-medicine/03` says *how a result updates belief*.

---

## Module Boundary Contract (Non-Duplication)

| Defers to | For |
|---|---|
| `medicine/10-DIAGNOSTICS-IMAGING` | The test **catalog**, reference ranges, analyte time-courses, imaging physics. Its `§11` diagnostic-reasoning section overlaps guide 03; a **forward** pointer runs 03 → `medicine/10`, and a **minimal reverse** pointer runs `medicine/10 §11` → 03. Neither module re-derives the other's depth. |
| `disease/` | Disease mechanisms, catalogs, natural history, epidemiology basics (R₀) |
| `human-biology/` | Organ-system anatomy and physiology, homeostasis |
| `medicine/`, `pharmacology/` | Drug classes, receptor theory, ADME/PK/PD, interactions, pharmacogenomics (**no dosing, ever**) |
| `public-health/` | Population epidemiology methods, surveillance, screening **programs**, health-system typology/financing, DALYs/QALYs |
| `psychology/`, `nutrition/`, `immunology/` | DSM-5/psychotherapy, dietary science, immune mechanisms |
| `pathology/` | Tissue/cell mechanism behind a result; histopathology; lab-medicine result generation |
| `ethics/` | Normative ethical theory (deontology/consequentialism/virtue) |

**Three-way lab/diagnostic-interpretation split (ratified in Pathology Pulse 05):**
`pathology/` = *why the result is what it is* → `medicine/10` = *the catalog & reference
ranges* → `clinical-medicine/03` = *how a clinician updates belief and decides to act*.
The pathology module is authored and reciprocally wired to this boundary.

---

## The Non-Advice Contract (Hard Review Gate)

This module is peer-level *and* safe because the two goals are met by the same discipline:
describe the reasoning in the third person, and never cross into instructions to a reader.
Every guide is authored and reviewed against these rules; an `expert-skeptic` advice-creep
pass treats any breach as a blocking defect.

```
  NON-ADVICE INVARIANTS  (every guide; any breach = BLOCK)
  --------------------------------------------------------------------------
  1  THIRD-PERSON descriptive voice: "a clinician weighs...", never "you should..."
  2  NO drug doses / titration / routes as instructions; drugs named at class level
  3  NO step-by-step procedure or technique instructions
  4  ACUTE content (05) = prioritization SCHEMAS as concept only; no CPR/self-treatment
  5  SCREENING content (09) = how the decision is REASONED, not "get screened at age X";
       every threshold attributed to a named body AND dated
  6  CAPACITY content (10) = how CLINICIANS assess capacity, not a reader self-test
  7  EVERY numeric threshold labeled illustrative / as-of-date and attributed
  8  DECISION CHEAT SHEETS phrased as "what the model/clinician does", not imperatives
  --------------------------------------------------------------------------
  The test: a reader can learn HOW medicine reasons and still have no instruction to
  self-diagnose, self-treat, or act in an emergency. Teaching the architecture is the
  goal; personalized guidance is out of scope and belongs to a licensed clinician.
```

**Why this is not a limitation.** The same third-person discipline that keeps the module
safe also keeps it *honest*: a decision described as "the model favors testing when the
pretest sits in the T_test–T_treat band" is more precise than "order the test," because it
exposes the assumptions (the prior, the threshold, the harm/benefit ratio) that a bare
imperative hides.

---

## Bias, Geography, and Resource Caveats (Read Before Any Guide)

The frameworks this module teaches are real and useful, but they carry provenance that a
peer reader must hold explicitly. These caveats recur, attributed, in the relevant guides.

| Caveat | What to hold |
|---|---|
| **Anglo-American framing** | ACGME/AAMC/USPSTF/Beers (US), NICE/GRADE (UK/intl) dominate. Screening ages, thresholds, and drug lists differ by country and body — attribute and date; never universalize one nation's cutoff. |
| **Evidence-base skew** | Trials skew to high-income, adult, historically male/white populations (the "70-kg male" default). Clinical decision rules and effect sizes may not transport; external validity (guide 04) is foregrounded, not a footnote. |
| **Resourced-system assumption** | Care-architecture guides (05, 07, 08, 11) assume EHRs, labs, imaging, and specialist access. Low-resource settings run materially different topologies (guide 08 §7/§10) — flagged, not universalized. |
| **Autonomy-weighted ethics** | The four-principles frame is Western-liberal and autonomy-forward; many cultures weight family/community differently (guide 10) — noted, not treated as the only frame. |
| **Ancestry and drug response** | Metabolism/response varies by ancestry (pharmacogenomics); named and deferred to `pharmacology/`, never turned into dosing. |

---

## Reading Order by Background

```
CLINICIAN-IN-TRAINING / LINEAR         SYSTEMS / SOFTWARE BACKGROUND
  00 -> 01 -> 02 -> 03 -> 04             00 -> 03 -> 08 -> 07 -> 11
     -> 05 -> 06 -> 07 -> 08                (decision theory + interfaces first;
     -> 09 -> 10 -> 11                       everything else is state + policy)

DECISION-THEORY / DATA BACKGROUND      LEADERSHIP / QUALITY BACKGROUND
  00 -> 03 -> 04 -> 02 -> 09             00 -> 11 -> 07 -> 08 -> 06
  (Bayes, evidence, calibration, bias)    (safety, handoffs, interfaces, burden)
```

Hard prerequisite edges inside the module: **02 before 03** (the differential supplies the
pretest probability that testing updates); **03 before 09** (screening is testing at low
prevalence); **02 before 06** (multimorbidity is many differentials colliding); **07 and
08 reinforce** (handoffs are the transitions that referrals create). Guide 04 (evidence)
can be read at any point but is assumed by 05, 06, and 09.

---

## Bridge: Software Mental Models → Clinical Medicine

Load-bearing analogies for a reader with deep CS and light clinical background.

| Software / systems concept | Clinical-medicine analog |
|---|---|
| Prior + Bayesian filter | Pretest probability updated by a test's likelihood ratio (03) |
| Ranked hypothesis set | Differential diagnosis, ordered by likelihood and by cost-of-miss (02) |
| Decision boundary with asymmetric costs | Treatment threshold p* = H/(H+B) (03) |
| Policy layer / feature flag with rollout evidence | Evidence appraisal + GRADE before an action (04) |
| Long-running stateful orchestration | Chronic care over a trajectory; the problem list as durable state (05, 07) |
| Technical debt / accreting config | Polypharmacy and prescribing cascades; deprescribing as refactor (06) |
| State transfer across a process boundary | Handoff (I-PASS/SBAR); a dropped field is a harm (07) |
| Microservice/service catalog + RPC | Specialties as bounded services; a referral is an RPC with a contract (08) |
| Precision collapse on a rare-event stream | Screening paradox: great test, low prevalence, mostly false positives (03, 09) |
| Swiss-cheese defense-in-depth; blameless postmortem | Reason's latent/active failures; RCA + just culture (11) |
| Observability: metrics vs traces vs logs | Donabedian structure/process/outcome measures (11) |

The single most useful bridge: **a clinical decision is a policy that acts on a posterior
belief only when the expected value of acting exceeds the expected value of waiting or
testing.** Every guide is either about forming the belief (01–04), acting on it over time
(05–06), moving it without loss (07–08), or keeping the whole system that produces it safe
(09–11).

---

## Reader Tasks (answerable from this guide)

1. **"Where does clinical medicine end and `disease/` or `medicine/` begin?"** → At the
   *reasoning/content* boundary. The disease, the drug, the imaging physics live in those
   modules; *how a clinician selects, sequences, and governs them for one person* lives
   here. Use the ownership/defer tables above to route any topic.
2. **"Which guide owns a given competency?"** → Map ACGME-6 or an AAMC EPA to a guide with
   the two spine tables. Example: EPA 8 (handover) → guide 07; SBP → guides 07/08/11.
3. **"Is this module telling me what to do about my own health?"** → No, by contract. Name
   the eight non-advice invariants and explain why third-person "the model favors…" framing
   is both safer and more precise than an imperative.
4. **"What reading path fits a systems/leadership reader?"** → `00 → 03 → 08 → 07 → 11`
   (decision theory and interfaces first), and justify the prerequisite edges (02→03,
   03→09, 07↔08).
5. **"Why is there no per-organ (cardiology, nephrology) guide?"** → Because per-organ
   guides would triplicate `disease/` + `human-biology/` + `pharmacology/`; the module's
   unique value is the organ-agnostic reasoning move, and specialties appear in guide 08
   as an interface catalog, not a disease catalog.

---

## Decision Cheat Sheet

| I need to understand… | Go to |
|---|---|
| How a clinician structures an encounter into a problem representation | `01` |
| How hypotheses are generated, ranked, and de-biased | `02` |
| How a test result updates belief and whether it should be ordered at all | `03` |
| Whether an action is supported by evidence, and for which population | `04` |
| The difference between acute prioritization and chronic longitudinal care | `05` |
| How competing guidelines, polypharmacy, and deprescribing are reasoned | `06` |
| How care is handed off without losing state | `07` |
| How specialties interface and who owns a referred problem | `08` |
| How screening decisions are reasoned, with their biases and harms | `09` |
| How consent, capacity, and justice are applied at the bedside | `10` |
| How the system is kept safe and improved (Swiss-cheese, SPO, PDSA) | `11` |
| The competency frameworks the module maps onto | this guide (ACGME-6 / AAMC EPAs) |

---

## Common Confusion Points

**"Isn't this just `medicine/` or `disease/` again?"** No. `disease/` owns disease
biology; `medicine/`+`pharmacology/` own drugs and the diagnostics catalog;
`human-biology/` owns physiology. This module owns the *reasoning and care architecture*
that consumes all of them for one person — problem representation, Bayesian testing,
evidence appraisal, deprescribing logic, closed-loop handoffs, safety systems. It names
their content by reference and never re-derives it.

**"Where are the organ specialties — cardiology, nephrology, neurology?"** Represented in
guide 08 as an **interface/service catalog** (what each service owns and how the interface
works), not as disease chapters. A per-organ guide would duplicate three existing modules;
the transferable skill is the organ-agnostic reasoning move, taught with examples drawn
across systems.

**"This is a soft, hand-wavy topic."** It is not, and the module refuses to read that way.
Every guide is anchored in a concrete formalism — odds-form Bayes and the threshold model
(03), GRADE and NNT (04), the Appelbaum four abilities (10), Donabedian SPO and PDSA (11)
— with worked, fictional cases. Platitudes are treated as a failure mode, not a style.

**"An educational medical reference must eventually give advice to be useful."** The
opposite: the module is useful *because* it stops at architecture. It explains **how**
clinicians reason so a reader understands the machine, while personalized diagnosis and
treatment remain a licensed clinician's job. The value is comprehension of the system, not
instructions for acting inside it.

**"The frameworks are universal."** They are attributed and dated, and mostly
Anglo-American. Screening ages, thresholds, drug lists, and even the weight given to
autonomy vary by country, body, era, and culture. The module teaches the *reasoning* and
tells the reader where current, local guidance lives — it does not hand out a global
cutoff.
