---
maxim_schema: maxim.frontmatter.v1
id: maxim:pathology:diagnosis-pattern-recognition-and-reporting
kind: guide
module: pathology
section: pathology
title: Diagnosis, Pattern Recognition, and Reporting - Morphology to Signed Report
status: source-custody
source_custody: partial
current_path: pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING.md
canonical_path: pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING.md
backsource_ids: [proof-backfill:pathology:10-diagnosis-pattern-recognition-and-reporting]
concepts: [pattern-recognition, differential-pattern-classes, ancillary-testing, diagnostic-certainty, grading-staging-margins, synoptic-reporting]
root_concepts: [diagnostic-pathology]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Diagnosis, Pattern Recognition, and Reporting — Morphology to Signed Report

**This guide owns** the *reasoning that turns a morphologic pattern into a signed
diagnosis, and the report that carries it*: pattern recognition as constrained
inference, the reusable taxonomy of **differential pattern classes**, the integration
of **ancillary tests** (special stains, immunohistochemistry, flow, cytogenetics,
molecular) as evidence that must first clear analytical validity, the **independent
dimensions of diagnostic certainty** (locally governed lexicons, not a universal ladder),
the *principles* of **grading, staging, and margins**, the **report as an
interface** (synoptic vs narrative), **critical-result communication**, and the
**amended/addended report** correction loop. **It builds on** the mechanism guides
`01`–`07` of this module (which explain *why* a lesion looks the way it does), on
`09-ANATOMIC-PATHOLOGY-TECHNIQUE` (which explains how the slide substrate is made — the
gross-to-glass pipeline), and on `08-LABORATORY-MEDICINE` (an ancillary stain is a
*test with its own analytical performance*). It borrows, by reference, the dual-process
and cognitive-bias framing of `clinical-medicine/02-DIFFERENTIAL-DIAGNOSIS` and the
decision-theory of `clinical-medicine/03`.

**It explicitly defers** four things it must never absorb:

- the **disease catalog** — entity-specific diagnostic criteria, WHO classifications, and
  natural history — to `disease/`; multi-organ examples here teach a *reusable method*,
  not a set of entities to memorize;
- the **Bayesian belief-update math** — pretest/posttest probability, likelihood ratios,
  test/treatment thresholds — to `clinical-medicine/03`;
- the **test/reference-range catalog** to `medicine/10`, and **result generation** (how
  an assay or stain physically produces its signal) to `08-LABORATORY-MEDICINE`;
- **operating procedures** — staining protocols, cutting, fixation steps — to the
  *principles* of `09` and, as runnable SOPs, out of scope entirely.

**Where this sits in the three-way split.** `08-LABORATORY-MEDICINE` produces a bounded
*result*; this guide produces a *diagnosis* from morphology + ancillary results and
packages it as a *report*; `clinical-medicine/03` consumes the report to update belief
and choose action. This guide's product is **a signed report carrying explicit certainty
dimensions** — not a number, and not a treatment decision.

> **This module is an educational reference about *how pathology reasons from morphology
> to a diagnosis and communicates it* — the mechanism-to-diagnosis architecture of the
> discipline. It is *not* medical advice. It does *not* interpret any reader's own slides,
> images, biopsy, or report, does *not* diagnose, does *not* give treatment or procedure
> instructions, and is *not a substitute* for a licensed pathologist or clinician. It
> gives *no specimen-collection, grossing, or laboratory-operating instructions* and *no
> forensic or legal (cause- or manner-of-death) determinations*. All cases are fictional
> teaching vignettes and all figures are illustrative.**

*Per-guide banner: educational reference on diagnostic pattern-reasoning and reporting —
never self-diagnosis, never personal-slide/report interpretation, never a bench or
grossing procedure, never forensic/legal advice. Entity names appear only to illustrate a
reusable method; the disease catalog is `disease/`.*

---

## The Big Picture: Diagnosis Is an Inference Pipeline, Not a Lookup

The novice mental model is "the pathologist looks down the microscope and *recognizes the
disease*." The expert model is a **staged inference pipeline** that starts from a
low-level pattern, prunes a hypothesis space, gathers discriminating evidence, calibrates
a confidence, classifies along orthogonal axes, and emits a *typed, signed artifact* — a
report — into a downstream system. Recognition is only the first stage; everything after
it is disciplined reasoning under uncertainty.

```
SPECIMEN-TO-SIGNED-REPORT  (this guide owns the reasoning + the report)
=======================================================================
  [ 09: GROSS-TO-GLASS ]  substrate: fixed, processed, stained slide
        |   (technique is 09; here we start from the image)
        v
  [ PATTERN ]     low-level morphology: architecture + cytology + context
        |            "what am I looking at?"  (Section 1-2)
        v
  [ DIFFERENTIAL BY PATTERN CLASS ]  pattern -> a FAMILY of hypotheses
        |            prune the space to a short list  (Section 3)
        v
  [ ANCILLARY EVIDENCE ]  IHC / stains / flow / cytogenetics / molecular
        |            each a TEST with its own Sn/Sp -> combine  (Section 4)
        v
  [ CERTAINTY: 4 DIMENSIONS ]  adequacy · assertion strength · negative
        |            scope · residual doubt (local lexicon, not one ladder)
        v            (Section 5)
  [ CLASSIFY ]  grade (how it looks) x stage (how far) + margins (edge)
        |            orthogonal axes, principles only  (Section 6)
        v
  [ REPORT ]  synoptic (structured) + narrative + comment  (Section 7)
        |
        +---> [ CRITICAL? ] active notify + read-back  (Section 8)
        |
        v
  SIGNED REPORT  ---> clinical-medicine/03 (belief + action, NOT here)
        |
        +---< [ AMEND / ADDEND ]  versioned correction loop  (Section 9)
```

Two properties of this pipeline organize the guide. First, **pattern precedes diagnosis**:
the pathologist commits to *what kind of thing* this is (a pattern class) before naming
*which* thing, and that commitment is what makes the search tractable. Second, **the
output is an interface, not a verdict**: the report is consumed by other humans and
systems, so its *structure* and its *explicit certainty language* are as much a part of the
diagnosis as the answer itself.

**Bridge — this is a compiler/inference pipeline.** Pattern recognition is *lexing +
feature extraction*; the differential-by-pattern is *narrowing to a grammar/hypothesis
class*; ancillary tests are *additional evidence that resolves ambiguity*; certainty
language is a *typed return* (`Result<Diagnosis, Uncertainty>`, never a bare value); the
synoptic report is a *structured, schema-validated payload*; and the amendment loop is a
*versioned correction with an audit trail*. A pathologist who reports a bare entity name
with no explicit certainty dimensions is returning an untyped value that drops its error
state.

---

## 1. Morphology as a Language: Pattern Before Diagnosis

A stained slide is not "a picture of a disease"; it is a field of **features** that the
observer parses at three levels simultaneously, and the diagnosis is an inference over
that parse — never a direct readout.

```
THE PARSE  (three levels, read together)
========================================
  ARCHITECTURE   how tissue is organized: glands, sheets, nests, fascicles,
   (low power)   follicles; infiltrative vs circumscribed; is normal
                 structure preserved or effaced?
  CYTOLOGY       the individual cell: size, nucleus:cytoplasm ratio,
   (high power)  chromatin, nucleoli, pleomorphism, mitoses
  CONTEXT        the company it keeps: stroma, inflammation, necrosis,
                 vessels, borders, the clinical/site frame
```

**Recognition is dual-process, exactly like clinical reasoning.** A fast *gestalt* (System
1) proposes a pattern in seconds; a slower *analytic* pass (System 2) tests it feature by
feature. `clinical-medicine/02` owns this dual-process framing and its cognitive-bias
failure modes (anchoring, premature closure, satisfaction of search); this guide inherits
them and localizes them to morphology: the danger is *committing to the first pattern and
reading every feature as confirmation*. The disciplined move is that the model names the
pattern, then seeks the feature that would *break* it — a falsification pass, not a
confirmation pass.

**A single feature is a weak classifier; the pattern is the ensemble.** No one feature
("has mitoses," "is blue," "invades") is diagnostic on its own — each is a weak signal with
its own false-positive and false-negative behavior. The pattern is the *joint*
configuration, which is why morphology is robust where any single feature is fragile. This
is precisely an ensemble of weak learners: individually noisy, jointly discriminating, and
catastrophically misled if any one feature is allowed to dominate the vote.

| Parse level | Question it answers | Failure if over-weighted |
|---|---|---|
| Architecture | What kind of process / is structure effaced? | Missing high-grade cytology in a bland architecture |
| Cytology | How atypical is the cell? | Calling reactive atypia neoplastic |
| Context | What frame changes the meaning? | Ignoring site/clinical data that flips the differential |

---

## 2. From Pattern to a Short List: The Discipline of the Differential

The move from "I see a pattern" to "here is my differential" is the reasoning core, and it
has the same shape as a clinical differential: generate a *ranked* hypothesis set, then
test discriminators. The morphologic version ranks along two axes at once — **what is most
likely** and **what must not be missed** — because a benign-looking pattern with a
low-probability but high-consequence mimic (a bland pattern that could be a well-
differentiated malignancy) is not "done" just because the common answer fits.

```
RANKING TWO AXES AT ONCE  (borrowed from clinical-medicine/02, localized)
=========================================================================
                 high consequence if missed
                        ^
        must-not-miss   |   top priority
        (rare mimic)    |   (likely AND dangerous)
     -------------------+-------------------> high probability
        low-yield       |   most likely
        (ignore)        |   (common, benign)
```

The engine is: **pattern → a family of hypotheses → the discriminating feature or test
that separates them.** The skill is not memorizing entities (that is `disease/`); it is
knowing, for a given pattern, *which discriminator has the most separating power* and
reaching for it next — the morphologic analogue of choosing the test that most changes the
posterior in `clinical-medicine/03`.

---

## 3. The Diagnostic Parse as a Multidimensional Matrix

The reason a pathologist can work across organs is that a small set of **orthogonal
dimensions** recurs across every specimen, and it is the *joint* profile across those
dimensions — not any single "pattern" axis — that prunes the hypothesis space. A one-axis
list of pattern classes undersells the parse: in practice the material is scored along
**adequacy, compartment, architecture, cytology, stromal/background, hematolymphoid
considerations, and sampling/discordance** at once. Which dimensions carry information
depends on the *specimen type*, which is exactly why the same method behaves differently
on a cytology aspirate and a resection. The examples below span multiple organs and
specimen types on purpose: they demonstrate that the *method* generalizes, not to catalog
diseases (which live in `disease/`).

```
THE PARSE MATRIX  (orthogonal dimensions; the JOINT profile discriminates)
==========================================================================
  DIMENSION            what it scores                     gates / feeds
  ------------------   --------------------------------   --------------------
  ADEQUACY             enough representative material     GATES everything below;
                       to parse at all?                   if not, the output is
                                                          "nondiagnostic", not benign
  COMPARTMENT          where does the process sit?        epithelium / stroma /
                       (which tissue layer or space)      vessel / lumen / node
  ARCHITECTURE         how is tissue organized?           glands / sheets / nests /
   (low power)         circumscribed vs infiltrative;     follicles; effaced or
                       structure preserved or effaced?    preserved?
  CYTOLOGY             the individual cell                atypia degree; separates
   (high power)        size, N:C ratio, chromatin,        reactive from neoplastic
                       nucleoli, pleomorphism, mitoses
  STROMAL/BACKGROUND   the company it keeps               desmoplasia, necrosis,
                       matrix, secretion, inflammation    mucin, colloid, diathesis
  HEMATOLYMPHOID       is this a lymphoid/myeloid          switches the method:
   CONSIDERATIONS      process rather than epithelial?    clonality + flow, not
                                                          gland-counting
  SAMPLING/            does the finding fit the clinical  triggers deeper levels,
   DISCORDANCE         and radiologic context; do         re-cut, correlation, or
                       blocks/levels/priors agree?        deferral
```

Three moves make the matrix operational (the reusable method, not an entity list):

1. **Adequacy and sampling gate everything else.** A confident-looking focus on
   non-representative or scant material is not a diagnosis; the disciplined output is
   "nondiagnostic/insufficient" or a request for deeper levels. Scoring the other five
   dimensions on inadequate material manufactures false confidence.
2. **Architecture and cytology are read together, then the class opens a family.** A
   *pattern class* (e.g., a granulomatous background, a spindle-cell architecture, a
   small-round-blue-cell cytology) is not a diagnosis; it opens a bounded differential
   *family* and, critically, *selects a small ancillary panel* — the pattern chooses the
   test, exactly as a pretest hypothesis chooses the most informative next test in decision
   theory.
3. **The hematolymphoid axis can switch the whole method.** When the process is lymphoid or
   myeloid, the operative questions become lineage and clonality (flow cytometry,
   immunoarchitecture, molecular clonality) rather than architecture-versus-invasion —
   a different toolset than an epithelial biopsy.

**Method demonstration — two contrasting specimens (not a disease catalog).** The same
matrix lights up different dimensions depending on the specimen:

- **A thyroid-nodule fine-needle aspiration (a *cytology* specimen).** What is unavailable
  is **tissue-level architecture and invasion** — an aspirate is dissociated cells and cell
  groups, not intact capsule and stroma, so *capsular/vascular invasion* and the overall
  growth pattern cannot be assessed (precisely why an aspirate cannot separate a follicular
  adenoma from a follicular carcinoma). What **is** available and diagnostically meaningful
  is the **cytoarchitecture of the cell groups themselves** — how the aspirated cells are
  arranged: **microfollicular** groups, papillary fragments, syncytial sheets, dispersed
  single cells. So the parse leans on **adequacy** (a minimum follicular-cell threshold
  defines a satisfactory specimen; below it the honest output is "nondiagnostic," not
  "benign"), **cytology** (nuclear features), those **cell-group-architecture** cues, and
  **stromal/background** (colloid vs cyst contents), and it reports through a **named,
  locally governed category system** rather than a free-form phrase. The tissue-architecture
  row of the matrix is dimmed, but its *cytologic* counterpart is not — the two must not be
  conflated. The hematolymphoid dimension is usually dormant — but a lymphoid-rich aspirate
  flips the method toward a lymphoid work-up (flow), illustrating the axis switch.
- **A lymph-node core or excision (a *tissue* specimen with an active hematolymphoid
  axis).** Here **compartment** and **architecture** are available (is nodal architecture
  effaced? follicular vs diffuse? are sinuses patent?), but **hematolymphoid
  considerations dominate**: the discriminating work is lineage and clonality, not
  gland-versus-stroma. **Sampling/discordance** is load-bearing — a reactive-appearing node
  beside a clinically suspicious mass drives correlation and re-sampling rather than a
  reassuring sign-out.

Both specimens run the *same* seven-dimension parse; the *active* dimensions differ. That
portability is the method; the specific entities in each family (which thyroid pattern,
which lymphoid process) live in `disease/`.

| Parse dimension | The reusable question it poses | Where the entity list / system lives |
|---|---|---|
| Adequacy | Is there representative material to parse at all? | method here (gates the parse) |
| Compartment | Which tissue layer or space holds the process? | `human-biology/` (normal), `disease/` (entities) |
| Architecture | How is tissue organized; is structure effaced? | `pathology/05` (mechanism), `disease/` |
| Cytology | Reactive atypia or neoplastic atypia? | `pathology/01`,`05` (mechanism), `disease/` |
| Stromal/background | What does the company it keeps imply? | `pathology/02` (mechanism), `disease/` |
| Hematolymphoid | Lymphoid/myeloid — does the method switch? | `immunology/` (biology), `disease/` (entities) |
| Sampling/discordance | Does it fit context; do blocks/priors agree? | method here; `09` (technique) |

---

## 4. Ancillary Tests: Analytical Validity, Then Diagnostic Evidence

When morphology alone leaves the parse unresolved, the pathologist orders **ancillary
tests** — special stains, **immunohistochemistry (IHC)**, flow cytometry, cytogenetics/
FISH, and molecular assays. The critical literacy point, and the reason `08-LABORATORY-
MEDICINE` is a prerequisite, is that an ancillary result must clear **two separate gates**,
and collapsing them is the central error:

- **Gate 1 — analytical validity (did the assay technically work?).** This is the `08`
  layer: antigen preservation and detectability, fixation/decalcification effects, antibody
  or probe performance, and — decisively — the **controls**. A "negative" with a failed
  internal control is *uninformative*, not negative; a "positive" from edge artifact or
  cross-reactivity is not a real positive. Analytical validity is a property of *this stain
  on this block*, independent of any disease.
- **Gate 2 — diagnostic evidence (given a valid result, how much does it discriminate
  HERE?).** Only once a result is analytically valid does it become *evidence*. Its
  intrinsic discriminating power — **sensitivity, specificity, and the likelihood-ratio
  contribution** — is a **spectrum-dependent** property: it shifts with *which entities sit
  in the differential* and the morphologic spectrum/case mix they present, so the same valid
  marker separates strongly in one differential and weakly in another. It does **not** shift
  with disease prevalence — **prevalence does not change Sn/Sp/LR.** What prevalence (the
  pre-test probability) drives is the **predictive value and posterior** — PPV, NPV, and the
  updated probability of disease — a *separate* quantity assembled downstream. This guide
  stops at the spectrum-dependent evidence weight; combining that weight with prevalence to
  produce a posterior is `clinical-medicine/03`.

```
TWO GATES FOR AN ANCILLARY RESULT
=================================
  raw stain / assay
        |
  [ GATE 1: ANALYTICAL VALIDITY ]   controls, antigen detectability,
        |    fixation, probe/antibody performance
        |    fail -> UNINFORMATIVE (neither "negative" nor "positive")
        v
  [ GATE 2: DIAGNOSTIC EVIDENCE ]   given a VALID result, its Sn/Sp/LR
        |    CONTRIBUTION varies with the DIFFERENTIAL / spectrum
        |    (strong here, weak there); prevalence drives PPV/NPV/
        |    posterior downstream, NOT Sn/Sp/LR
        v
  weighted evidence -> combined in a PANEL (never a single switch)
```

This split forces four disciplines:

1. **Panels, not single markers.** Each *valid* marker is a weak, noisy classifier (a
   likelihood-ratio contribution, not a switch); a *panel* is chosen so that markers vote in
   combination and the *joint* pattern discriminates. An epithelial-marker-positive /
   mesenchymal-marker-negative profile shifts toward an epithelial lineage — an illustration
   of the combining logic, not an entity recipe.
2. **Controls decide what "negative" means (Gate 1).** A negative stain with a failed
   internal control is *uninformative*, not *negative* — the same distinction `08` draws
   between an analytic flag and a real result. Reading a technically failed stain as absence
   conflates the two gates.
3. **Decisive vs supportive is a Gate-2 judgment.** A *valid* result can be *decisive* (a
   specific alteration that defines a lineage) or merely *supportive* (consistent with, but
   not specific to, a hypothesis) — and which one it is depends on the differential it is
   deployed against, not on the stain alone. Treating a supportive marker as decisive
   manufactures false certainty.
4. **The pre-test pattern gates the panel.** The parse (Section 3) selects a small,
   high-yield panel rather than a scattershot one — the morphologic analogue of
   value-of-information testing in `clinical-medicine/03`. Staining without a pattern-driven
   question generates uninterpretable noise and incidental positives whose diagnostic weight
   (Gate 2) is undefined.

| Ancillary modality | What it adds | Characteristic *analytical* (Gate-1) failure |
|---|---|---|
| Special (histochemical) stains | Highlights substances/organisms/structures | Low specificity; over-reading faint positivity |
| Immunohistochemistry (IHC) | Lineage/antigen expression, in situ | Cross-reactivity, antigen loss, control failure |
| Flow cytometry | Quantitative immunophenotype of cell suspensions | Needs viable cells; misses tissue architecture |
| Cytogenetics / FISH | Structural/numeric chromosomal changes | Targeted; misses what it isn't probing |
| Molecular (PCR/NGS) | Specific alterations, clonality, load | Result-generation caveats live in `08` |

For every modality, the *diagnostic* weight of an analytically valid result (Gate 2) is
**spectrum-dependent** — set by the differential it is deployed against and the morphologic
spectrum of the entities in play, not by the modality alone. Prevalence enters only later,
when that weight is combined into a predictive value / posterior (`clinical-medicine/03`);
it does not alter the result's Sn/Sp/LR.

---

## 5. Diagnostic Certainty: Independent Dimensions, Locally Governed Words

A diagnosis is rarely binary, but the honest way to encode its uncertainty is **not** a
single universal ladder of words mapped to fixed probabilities. Terms like "consistent
with" and "suspicious for" do **not** carry a stable, cross-institutional numeric posterior;
their force is set by **local convention or a named category system**, and the same phrase
can sit at different places on different services and in different eras. What generalizes is
not a probability scale but a small set of **independent dimensions** a report makes
explicit, each governed by a locally defined lexicon rather than a universal one.

```
FOUR INDEPENDENT DIMENSIONS  (not one ladder; each stated on its own axis)
==========================================================================
  MATERIAL ADEQUACY        is the specimen representative enough to
   (gates the rest)        support ANY assertion?  inadequate -> stop
        |
  POSITIVE ASSERTION       how strongly does THIS material assert a
   STRENGTH                positive finding?  descriptive -> committed
        |                  (words governed by a LOCAL lexicon / system)
  NEGATIVE-FINDING SCOPE   what does a "negative" actually cover?
        |                  "not identified in the material examined" --
        |                  never a universal absence
  RESIDUAL UNCERTAINTY     the explicitly stated floor on doubt: what
                           cannot be excluded, and why
```

Four principles keep these dimensions honest — and because they are *orthogonal*, a report
can be adequate yet weakly asserting, or strongly asserting yet with a wide
residual-uncertainty floor:

1. **The lexicon is locally governed, not a universal probability map.** A term's force is
   defined by the reporting service's convention or by a **named, dated category system**
   (organ-specific reporting-category frameworks are the norm in cytology and some tissue
   settings). The reusable skill is that a report *states which dimension a word addresses
   and under which system* — it does not assume "suspicious for" denotes one probability
   everywhere. Miscalibration *within* a system — a stronger assertion term than that
   system's evidence supports — is the reporting analogue of an overconfident classifier.
2. **Positive assertion strength is one axis.** How firmly the material supports a positive
   finding ranges from a purely *descriptive* statement (report the pattern, name no entity)
   through *favor / suspicious* wording to a *committed* diagnosis — but where a given word
   falls is a property of the local lexicon, not a fixed posterior.
3. **Negative-finding scope is a separate axis.** A "negative" is a scoped claim — "not
   identified in the material examined" — bounded by what was sampled and stained, never a
   universal "absent." Stating that scope is the pathologist's version of "absence of
   evidence is not evidence of absence."
4. **Material adequacy gates, and residual uncertainty is named.** A confident-looking
   morphology on a tiny, crushed, or non-representative sample cannot license a strong
   assertion regardless of how typical it looks; adequacy is stated first. Whatever doubt
   remains is given an explicit floor — the entity or category that **cannot be excluded**,
   and why — rather than left implicit.

**Uncertainty has named, legitimate outputs.** When the evidence is genuinely
indeterminate, disciplined outputs include a **descriptive diagnosis** (report the pattern
without forcing an entity), **deferral** for more sampling/levels/stains, **intradepartmental
consensus** or **second opinion**, and **expert referral** — each a documented output, not a
failure. Forcing a specific diagnosis the evidence cannot support is the failure.

**Interobserver variability is real and bounded.** Even expert observers disagree on
borderline morphology, quantified by agreement statistics (e.g., a kappa coefficient).
Local lexicons, category systems, and consensus mechanisms exist precisely because the
underlying judgment is not perfectly reproducible — a property stated, not hidden.

---

## 6. Classification: Grading, Staging, and Margins (Principles)

When a lesion is neoplastic, the diagnosis carries **classification** along axes that are
*orthogonal* and must not be conflated. This guide owns the *principles and their
reproducibility limits*; the entity-specific systems and cutoffs are `disease/`.

```
TWO ORTHOGONAL AXES + A BOUNDARY CONDITION
==========================================
  GRADE  (how it LOOKS)                 STAGE  (how FAR it has spread)
  intrinsic aggressiveness:             anatomic extent at a point in time:
  differentiation, pleomorphism,        size / depth (T), nodes (N),
  mitotic rate, necrosis                distant spread (M)   [pT·pN·pM elements]
        |                                     |
        +----------------+--------------------+
                         v
             MARGINS (the EDGE / boundary condition)
             is the lesion transected at the cut surface?
             "involved" vs "clear" (with a measured distance)
```

- **Grade is an intrinsic-aggressiveness estimate from morphology** — how far the lesion
  has departed from the normal tissue it arose from (differentiation), plus features like
  mitotic rate and necrosis. It answers "how does it look like it will behave?" It is
  *estimated*, hence subject to interobserver variability, and it is graded on
  entity-specific scales owned by `disease/`.
- **Stage is anatomic extent**, conventionally framed with the **TNM** *framework* (tumor
  size/depth, nodal involvement, distant spread). Two scoping points matter for what a
  pathology report actually contributes. First, the report supplies the **pathologic TNM
  elements** it can observe in the specimen — `pT`, `pN`, and `pM` where material is present
  — which are distinct from the **overall stage group** (stage I–IV). The stage group is an
  *integration* step that combines T, N, and M (clinical *and* pathologic) and, in some
  current systems, selected **non-anatomic prognostic factors**; it is often assigned
  downstream (e.g., by a tumor registrar or the treating team), not owned outright by the
  pathology report. Second, TNM is a *framework* whose site-specific definitions and the
  current edition live in `disease/`. Pathologic stage *elements* are largely
  *measured/observed*, which is why they are generally more reproducible than grade.
- **Margins are a boundary condition**: at the **examined, inked specimen margins**, is
  tumor present (*involved*), absent (*clear*), and — when clear — at what measured
  *distance* from the inked surface? That is the whole of what margin status reports —
  tumor presence/absence/distance at the sampled margin planes. It is **evidence about**,
  not **proof of**, complete removal: the pathologist examines *sections* of the inked
  surface of the excised *specimen*, not the entire three-dimensional resection bed left in
  the patient, so a "clear" margin does **not** prove the excision was complete (residual
  tumor can lie between sampled planes or beyond what the specimen captured). Because it
  also depends on grossing/orientation and inking (technique, `09`), a margin claim is only
  as good as the specimen handling behind it.

**The conflation error to avoid:** grade, stage, and margin are independent. A low-grade
lesion can be advanced-stage; a high-grade lesion can be early-stage with clear
(uninvolved) examined margins. Reporting them as if one implies another (or collapsing "how
bad it looks" with "how far it has gone") is a category error that misinforms the
downstream reader.

| Axis | Question | Nature | Reproducibility | Catalog owner |
|---|---|---|---|---|
| Grade | How aggressive does it look? | Estimated from morphology | Lower (interobserver variation) | `disease/` |
| Stage elements | How far has it spread? | Measured `pT`/`pN`/`pM` (report); the overall stage **group** is integrated downstream | Higher | `disease/` |
| Margin | Tumor present/absent + clearance distance at the examined inked margins? | Sampled planes of the inked surface (evidence about, not proof of, complete excision) | Depends on grossing/inking (`09`) | method here |

---

## 7. The Report as an Interface

The diagnosis only creates value when it is *communicated*, and the report is a **contract
with the treating clinician and their systems**. Its structure — not just its content — is
part of the diagnosis.

```
REPORT ANATOMY  (a typed payload + a human-readable log)
========================================================
  DIAGNOSIS LINE      the actionable answer + explicit certainty
   (the API return)   (entity/pattern, grade, stage elements, margins)
        |
  SYNOPTIC BLOCK      structured, checklist/schema (CAP-protocol style):
   (structured        every required data element, name:value, machine-
    schema)           readable, complete-by-construction
        |
  MICROSCOPIC/GROSS   the narrative description (the "log"): what was seen
   DESCRIPTION        (supports and audits the diagnosis line)
        |
  COMMENT             reasoning, limitations, differential, recommendations
   (the rationale)    for further work-up; where uncertainty is explained
```

- **Synoptic vs narrative is structured-vs-free-text.** A **synoptic** report is a
  schema: a fixed set of required data elements (size, grade, margin distance, nodal
  counts, and so on) reported as name–value pairs, which makes it *complete by
  construction* and *machine-consumable* — registries, downstream decision support, and
  audits can parse it. A **narrative** report is prose: flexible and expressive but easy to
  leave incomplete and hard to parse. Modern practice pairs them — the synoptic block
  guarantees completeness, the narrative carries nuance. The bridge is exact: a synoptic
  report is a validated structured payload; a narrative is an unstructured log. The
  disciplined form uses both, and a *required actionable element* is not placed only in the
  prose where a reader or a parser can miss it.
- **The diagnosis line is the API return; the comment is the rationale.** The actionable
  answer belongs on the diagnosis line with its certainty; the *why*, the differential
  considered, the *limitations*, and any recommended further work-up belong in the comment.
  Burying an actionable qualifier ("margin involved") in a paragraph instead of the
  synoptic field is an interface defect regardless of correctness.
- **Completeness is protocol-governed, not universal.** *Where a synoptic protocol applies*
  (for example, a resection reported under a named cancer-reporting protocol such as the
  CAP protocols in the US or an ICCR/RCPath-style dataset elsewhere), the template enforces
  a fixed contract of required elements the way a typed schema enforces required fields, and
  accreditation may make that structured completeness mandatory for those specimens. But
  reporting systems are **heterogeneous**: many specimens fall outside any synoptic protocol,
  small biopsies and cytology are often narrative, and the specific templates and rules
  differ by jurisdiction and institution. There is **no universal "cannot sign" rule** — the
  enforceable-completeness property holds *within a governing protocol/system*, not as a law
  of pathology; outside such a protocol, completeness is a professional norm rather than a
  schema-enforced gate.

---

## 8. Critical and Urgent Diagnosis Communication

Most reports are *published* to the record and read asynchronously. A minority are
**critical/urgent diagnoses** — findings unexpected or serious enough that passive
publication is unsafe — and these are *pushed* with a documented, closed loop, exactly
paralleling the critical-value logic of `08-LABORATORY-MEDICINE §8`.

```
CRITICAL DIAGNOSIS LOOP  (push, don't just publish)
===================================================
  a diagnosis that is unexpected AND/OR urgent to act on
        |
        v
  [ ACTIVE NOTIFY ]  reach the responsible clinician directly
        |
        v
  [ READ-BACK ]  receiver repeats the finding -> confirms transfer
        |
        v
  [ DOCUMENT ]  who / when / what, recorded in the report
        |
        v
  the loop is CLOSED (delivery is verified, not assumed)
```

The defining property is **verified delivery**: a critical diagnosis is not "done" when it
is signed, but when it is *acknowledged*. This is a delivery-guarantee problem — at-least-
once delivery with an acknowledgment, not fire-and-forget publication. What counts as
"critical" is defined by policy (a service-level agreement between the laboratory and its
clinicians), and the *clinical response* to the finding is not owned here — only its
generation and guaranteed communication.

---

## 9. Amended vs Addended Reports — The Correction Loop

A signed report is a released artifact, so changing it requires a **versioned, audited
correction** rather than a silent edit. The taxonomy matters because the three operations
have different meanings to the downstream reader.

```
POST-SIGN-OUT CHANGES  (versioned corrections, never silent edits)
==================================================================
  ADDENDUM   append-only follow-up: adds information that was pending
   (append)  (a later stain, a molecular result) WITHOUT changing the
             original interpretation
  AMENDMENT  a CHANGE to previously reported information: corrects an
   (revise)  error or revises the diagnosis; the change is flagged and
             the reason recorded (the prior version is retained)
  RETRACTION the strongest correction: the prior conclusion is withdrawn;
   (revoke)  active re-notification if it may have driven action
```

Three principles govern the loop:

1. **Corrections are versioned and audited, never overwritten.** The prior content is
   retained and the change is flagged with a reason — an append-only history with a visible
   diff, not a mutation. A silent edit destroys the reader's ability to know what they
   acted on.
2. **The type of change signals its impact.** An **addendum** (new pending information, no
   change to the interpretation) is low-impact; an **amendment** (the interpretation
   changed) may invalidate a downstream decision and often requires *active* re-notification
   with the same closed-loop discipline as a critical diagnosis. Labeling an amendment as a
   mere addendum understates its impact and is itself an error.
3. **Amendments are error-surveillance data.** The rate and type of amendments are how the
   laboratory *measures* diagnostic defects and feeds its quality system (owned at depth by
   this module's guide `11`) — the correction loop is also the monitoring signal.

---

## 10. End-to-End Fictional Case: The Report Payload

*A fully fictional teaching vignette. The patient, specimen, results, and identifiers are
invented to show the report as a structured, versioned artifact end to end; nothing here is
a real case, a diagnostic rule, or advice. Every field value is illustrative and follows no
real patient.*

The pipeline (Sections 1–9) produces an *artifact*. Rendering it as an actual payload —
rather than narrating it — shows how the parse dimensions land in named fields and how a
correction is versioned. Technique (fixation, grossing, sectioning, staining) is `09`;
result generation is `08`; the pipeline here starts at the stained slide.

### Version 1 — initial sign-out

```
========================= SURGICAL PATHOLOGY REPORT =========================
Accession:   S-00-00000 (fictional)              Report status: FINAL v1
Specimen:    "Soft-tissue nodule, [site]", excision (fictional)

--- DIAGNOSIS LINE ---
  Low-grade spindle-cell neoplasm, favoring [mesenchymal family];
  a well-differentiated malignant mimic is not entirely excluded on the
  material examined (see Comment).

--- SYNOPTIC BLOCK (name : value) ---
  Procedure ............. Excision
  Specimen integrity .... Intact, oriented, inked
  Adequacy .............. Adequate; deep edge focally suboptimal (see limit)
  Lesion size ........... 21 mm (gross), confirmed microscopically
  Histologic pattern .... Spindle-cell, focally infiltrative
  Grade (estimate) ...... Low grade (differentiation / low mitoses / no necrosis),
                          under a named entity system owned by disease/
  Pathologic T element .. Not assigned here (site/entity-specific; disease/)
  Overall stage GROUP ... Not assigned by this report (integrated downstream)
  Margins ............... Neoplasm to within 0.8 mm of the inked deep margin; other
                          examined margins uninvolved in the sections sampled (a measured
                          fact at the examined margins, not proof of complete excision)
  Ancillary (IHC) ....... Epithelial marker NEG (internal control valid);
                          neural/melanocytic marker NEG; mesenchymal marker POS
  Molecular ............. PENDING at sign-out
  Assertion strength .... "Favoring" — not committed (lexicon: local)
  Negative-finding scope  Markers negative in the sections examined only

--- MICROSCOPIC / GROSS DESCRIPTION (narrative log) ---
  Circumscribed but focally infiltrative spindle-cell proliferation; mild
  nuclear atypia; occasional mitoses; entrapped normal structures at the edge.
  (Descriptive; supports and audits the diagnosis line.)

--- COMMENT (rationale + limitations) ---
  The joint IHC profile (epithelial-neg / neural-neg / mesenchymal-pos, controls
  valid) favors [mesenchymal family] over an epithelial mimic; one entity-decisive
  marker was equivocal and is treated as supportive only. The deep edge is focally
  suboptimally preserved, bounding certainty (negative-finding scope = sections
  examined). The measured 0.8 mm deep-margin clearance is reported as a FACT at the
  examined inked planes — evidence about, not proof of, complete excision; its clinical
  significance is entity-, protocol-, and context-dependent and is NOT a generic
  actionable threshold — interpretation and management belong to the treating
  team (clinical-medicine/03), not this report. Molecular assay pending; an amendment
  will follow if it changes the interpretation.

--- CRITICAL-COMMUNICATION RECORD ---
  Not applicable at v1: no unexpected/urgent finding requiring active notification.
=============================================================================
```

Note what the payload does *not* claim: the reported margins are a **measured boundary
condition at the examined inked planes** — tumor presence/absence and a clearance distance
where the specimen was sampled and inked — not a proof that the excision was complete, and
not a generically actionable result. Whether 0.8 mm matters is set by the entity, the
governing protocol, and the clinical context — owned downstream, not asserted here.

### Version 2 — amendment (the pending molecular result returns)

The pending molecular assay (result generation owned by `08`) later returns and is
*decisive* for the leading family at entity level. Because this **changes** the
interpretation (assertion strength moves from "favoring" toward committed), it is issued as
an **amendment**, not an addendum — flagged, reason recorded, prior version retained — and,
because a changed interpretation may alter downstream action, with active re-notification.

```
========================= SURGICAL PATHOLOGY REPORT =========================
Accession:   S-00-00000 (fictional)          Report status: AMENDED v2
                                             (v1 retained; change flagged)

--- AMENDMENT NOTICE ---
  Reason:  pending molecular assay returned and is entity-decisive.
  Change:  assertion strength upgraded from "favoring [family]" (v1) to a
           committed lineage-level diagnosis under [named system].
  Prior version (v1) retained and viewable; interpretation changed.

--- DIAGNOSIS LINE (amended) ---
  Low-grade [entity of mesenchymal family], confirmed by molecular result
  (see disease/ for the entity's criteria and current system/edition).

--- SYNOPTIC DELTAS (v1 -> v2) ---
  Molecular ............. PENDING -> POSITIVE, entity-decisive
  Assertion strength .... "Favoring" -> committed (lineage level)
  (All other fields unchanged; margin still reported as 0.8 mm, a measured fact.)

--- CRITICAL-COMMUNICATION RECORD (amendment) ---
  Amended interpretation actively communicated to the responsible clinician;
  read-back obtained; who / when / what documented (verified delivery, per §8/§9).
=============================================================================
```

Contrast an **addendum**: had the molecular result merely *added* non-changing information
(confirming what v1 already committed to), it would have appended as an **addendum** with no
change to the interpretation and no re-notification.

### Alternate branch — resource-constrained (same framework, different artifact)

Where the entity-decisive molecular assay is unavailable on site and referral is slow or
infeasible, the *same* pipeline yields a *different released artifact* without changing the
framework:

- The `Molecular` field reads "not available on site" rather than "PENDING", and the
  assertion strength stays at *favoring / descriptive* — it is never upgraded, because the
  decisive evidence never arrives.
- The Comment carries the resource limitation explicitly and, where possible, records a
  **send-out or telepathology referral** as the path to resolution — a report-wording and
  referral change, not a reasoning change.
- No amendment is issued (nothing changed); the residual-uncertainty floor is stated and
  left open.

The parse dimensions, the report anatomy, and the correction taxonomy are identical across
both branches; only the available tests, the final assertion strength, and the referral
wording differ.

The artifact that leaves this pipeline is a *signed report carrying explicit certainty
dimensions and a versioned correction history* — which `clinical-medicine/03` then consumes
to update belief and choose action. This guide stops at the signed report.

---

## 11. Resource-Tier Variation — Same Reasoning, Different Toolbox

The *reasoning* pipeline above is invariant; the *tools* available to execute it are not.
The method degrades gracefully — the same parse runs, with different tools and different
report wording.

```
SAME PIPELINE, DIFFERENT RESOURCES
==================================
  RESOURCED CENTER        DISTRICT / LOW-RESOURCE        MITIGATION
  ----------------        --------------------          --------------------
  broad IHC panels        few or no IHC markers         morphology-forward Dx;
                                                        send-out for stains
  in-house molecular      no molecular on site          batch/referral send-out
  frozen section on call  limited/no frozen section     defer to permanent
  subspecialty sign-out   generalist sign-out           telepathology consult
  rapid consensus         isolated practice             digital second opinion
```

The consequences for the *output* are explicit and belong in the report, not hidden:

- **Certainty wording absorbs the resource limit.** Where a discriminating stain or
  molecular test is unavailable, the honest output stays at a *descriptive* or
  *favoring, pending referral* assertion strength — the certainty *dimensions* (Section 5)
  are exactly how a toolbox limit is reported without overclaiming.
- **Telepathology and referral change *who* signs, not *how* one reasons.** A digitized slide
  sent for a second opinion runs the same parse; the pipeline is portable even when the
  expertise is remote — with its own pre-analytic caveats (scan quality, sampling) that the
  report should note.
- **Frozen-section availability changes tempo, not logic.** Where rapid intraoperative
  assessment is unavailable, the same diagnostic reasoning simply runs on permanent sections
  later; the reasoning is unchanged, the timing is not.

---

## Reader Tasks (answerable from this guide)

Each task is a *pathologist-reasoning* exercise — how a diagnosis is built and communicated —
not a personal-slide or personal-report interpretation.

**Task 1 — "A slide shows 'granulomatous inflammation.' Why is that not a diagnosis, and
what does naming the pattern buy?" (Sections 1–3)**
"Granulomatous inflammation" is a **pattern class**, not an entity: epithelioid histiocytes
organized into granulomas. Naming it prunes an enormous space to a *bounded differential
family* (infective vs immune-mediated vs foreign-body vs sarcoidal), which then *selects* the
next steps — targeted special stains for organisms, polarization for foreign material, and
clinical correlation. The value is the hypothesis-class commitment that makes the work-up
targeted; the specific entities in the family live in `disease/`, `microbiology/`,
`immunology/`.

**Task 2 — "An immunostain is 'negative.' Why can that be uninformative rather than
reassuring?" (Section 4)**
Because a stain must clear two gates. The **control** decides *analytical validity* (Gate 1):
a negative stain with a failed internal control is *uninformative*, not *negative* — the same
"analytic flag vs real result" distinction `08` draws. Only an analytically valid negative
becomes *diagnostic evidence* (Gate 2), and even then it merely *lowers* probability by a
context-dependent amount (it is not proof of absence) — one weak classifier weighed in a
panel, not a switch.

**Task 3 — "Two reports say 'consistent with X' and 'suspicious for X.' Is that just
wording?" (Section 5)**
No — but the difference is one of **positive assertion strength**, and that strength is
defined by a **local lexicon or named category system**, not a universal probability. Within
a given system "consistent with" typically asserts more firmly than "suspicious for"; *across*
systems the same phrase can sit differently, so neither denotes a fixed posterior. What is
portable is the *dimension* (assertion strength) and the discipline of not using a stronger
term than that system's evidence supports — the reporting analogue of an overconfident
classifier. The actual belief-update and action are `clinical-medicine/03`.

**Task 4 — "A report gives a low grade but says the tumor is advanced. Is that a
contradiction?" (Section 6)**
No. **Grade** (how aggressive the lesion *looks* — differentiation, mitoses) and **stage**
(how *far* it has spread — captured by pathologic TNM elements `pT`/`pN`/`pM`, with the
overall stage *group* integrated downstream) are *orthogonal* axes. A low-grade lesion can be
advanced-stage and a high-grade lesion early-stage; **margin** status (tumor
presence/absence and clearance distance at the examined inked margins — evidence about, not
proof of, complete excision) is a third, independent boundary condition. Treating one as
implying another is a category error. The entity-specific grading/staging systems are
`disease/`.

**Task 5 — "A pending molecular test comes back after sign-out and changes the diagnosis.
Addendum or amendment — and does it matter?" (Section 9)**
It is an **amendment**, and the distinction matters. An **addendum** *adds* information
without changing the interpretation; an **amendment** *changes* previously reported
information. Because the interpretation changed and may have driven downstream action, it is
issued as a flagged amendment with the reason recorded and the prior version retained, and —
like a critical diagnosis — often with *active re-notification* (verified delivery), not a
silent edit. Mislabeling it an addendum understates the impact.

---

## Decision Cheat Sheet

*Which diagnostic-reasoning concept a given situation involves (all descriptive model
states; no personal-slide/report interpretation, no procedures):*

| Situation / signal | The concept is… | Where it lives |
|---|---|---|
| "The pathologist recognized the disease" | Diagnosis is a staged **inference pipeline**, not a lookup | §Big Picture |
| A pattern named before an entity | **Pattern class → differential family** | §1–3 |
| One feature treated as diagnostic | Features are **weak classifiers**; the pattern is the ensemble | §1 |
| "Most likely" vs "must not miss" | Two-axis **differential ranking** | §2 |
| A multidimensional parse (adequacy…discordance) | The **parse matrix** (specimen sets active dimensions) | §3 |
| A small IHC panel chosen deliberately | Pattern **gates** the panel (value of information) | §3–4 |
| A "positive" or "negative" stain | An ancillary **test**: analytical validity (controls) then context-dependent evidence | §4 |
| "Consistent with" vs "suspicious for" | **Positive assertion strength** on a *local* lexicon (no universal ladder) | §5 |
| A confident call on a tiny sample | **Material adequacy** dimension bounds the assertion | §5 |
| "Descriptive diagnosis" / "deferred" | Named legitimate **uncertainty outputs** | §5 |
| Low grade but advanced stage | **Grade ⟂ stage ⟂ margin** (orthogonal axes) | §6 |
| "Margin involved / clear (< N mm)" | **Margin** = tumor presence/absence/distance at examined inked margins (not proof of complete excision; significance context-dependent) | §6, `09` |
| `pT`/`pN` reported but no stage group | Report gives **pathologic elements**; stage **group** integrated downstream | §6 |
| Structured name:value report block | **Synoptic** report = schema/typed payload (protocol-governed) | §7 |
| Actionable element only in the prose | Interface defect (belongs on the **diagnosis line**) | §7 |
| A phoned diagnosis with read-back | **Critical diagnosis** verified-delivery loop | §8 |
| A post-sign-out result appears | **Addendum** (adds) vs **amendment** (changes) | §9 |
| No IHC/molecular available | Resource-tier variation → certainty *wording* absorbs it | §11 |
| What the diagnosis *means* / what to do | Not here — belief update + action | `clinical-medicine/03` |
| The entity's criteria / natural history | Not here — the catalog | `disease/` |

---

## Common Confusion Points

- **Pattern is not diagnosis.** The pathologist commits to a *pattern class* (which prunes
  the hypothesis space) before naming an entity. "Granulomatous," "spindle-cell,"
  "small-round-blue-cell" are classes, not answers.
- **A single feature is a weak classifier.** No lone feature ("has mitoses," "invades") is
  diagnostic; the *joint pattern* discriminates. Letting one feature dominate the vote is a
  classic error (and a cognitive-bias failure inherited from `clinical-medicine/02`).
- **Positive ≠ present; negative ≠ absent.** An ancillary stain is a test with its own
  false positives and negatives; **controls** decide whether a "negative" is real or a failed
  reaction. Panels combine weak markers; single markers rarely switch a diagnosis.
- **Certainty is independent dimensions on a local lexicon, not a universal ladder.**
  Material adequacy, positive assertion strength, negative-finding scope, and residual
  uncertainty are *separate* axes; the *words* that express them are governed by local
  convention or a named category system, not a fixed cross-institutional probability. Using a
  stronger assertion term than the local system's evidence supports is the
  overconfident-classifier error.
- **Sampling bounds certainty.** A confident-looking morphology on a tiny/crushed/non-
  representative sample does not justify a strong assertion; the adequacy limitation is
  stated, not hidden.
- **Grade, stage, and margin are orthogonal.** How aggressive it *looks* (grade), how *far*
  it has spread (stage — pathologic TNM elements, with the stage *group* integrated
  downstream), and what the **examined inked margins** show (margin status — tumor
  presence/absence/distance, evidence about but not proof of complete excision) are
  independent. Collapsing them is a category error.
- **Grade is estimated; stage is measured.** Grade carries interobserver variability
  (kappa); pathologic stage elements, being anatomic extent, are generally more reproducible.
  Neither is a perfectly reproducible oracle.
- **Synoptic ≠ narrative; where a protocol governs, required elements belong in the synoptic
  block.** Structured reporting is complete-by-construction and machine-readable *within a
  governing protocol*; prose is expressive but loss-prone. Outside such a protocol,
  completeness is a professional norm rather than a schema-enforced gate — there is no
  universal "cannot sign" rule — and an actionable element hidden only in prose is an
  interface defect.
- **Addendum adds; amendment changes.** They are different corrections with different
  downstream impact; an amendment that alters the interpretation often needs verified
  re-notification, never a silent edit.
- **A signed report is not an action.** This guide ends at an explicit-certainty,
  communicated diagnosis. What it *means* for a person and what to *do* is a clinician's
  belief update (`clinical-medicine/03`), never this guide and never a reader's
  self-interpretation.

---

## Resource, Geographic, and Bias Caveats

- **Ancillary access varies enormously.** Broad IHC panels, flow cytometry, cytogenetics,
  and molecular/NGS are concentrated in resourced centers; district and low-resource
  laboratories may reason morphology-forward and send out or refer. The *pipeline* transfers;
  the toolbox does not, and the certainty language (Section 5) is how a toolbox limit is
  reported honestly.
- **Classification systems evolve and are governed externally.** Grading/staging systems and
  entity definitions are periodically revised by expert bodies and are attributed and dated
  in `disease/`; a grade or stage is only meaningful under a *named, dated* system, never as
  a universal constant.
- **Interobserver variability is intrinsic.** Reproducibility differs by lesion and observer
  (borderline morphology, grading); consensus, second opinion, and expert referral exist
  because the judgment is not perfectly reproducible — a property to disclose, not conceal.
- **Reporting standards are jurisdictional.** Synoptic templates, critical-diagnosis
  policies, and amendment/retraction rules are set by accrediting/regulatory bodies that
  differ by country; the *concepts* here are general, the *specific templates and rules* are
  local (and their systems framing is owned by this module's guide `11`).
- **Digital/telepathology adds its own caveats.** A remote or AI-assisted read runs the same
  reasoning but inherits scan-quality, sampling, and validation caveats that belong in the
  report; the substrate and its generation are `09` and `08`.
- **These cases and figures are illustrative and fictional.** Entity names appear only to
  demonstrate the *method*; no case, grade, margin distance, or certainty phrase here applies
  to any individual, and none is a diagnostic rule.
