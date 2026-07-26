---
wave: clinical-and-chemical-foundations
pulse: 05
kind: architecture-record
module: pathology
date: 2026-07-11
status: final
governing_roles: [reference-editor, expert-skeptic, index-weaver, ascii-cartographer]
---

# pathology/ — Architecture & Research Record (Pulse 05)

Wave-local architecture record for the `pathology/` module: the module that closes the
`clinical-and-chemical-foundations` wave by supplying the **mechanism-to-diagnosis
bridge**. Condenses the Pulse-05 design work into a durable record: the research
question, the numbered findings (MAXIM-PATH-01 … MAXIM-PATH-25), the ratified 12-guide
manifest with per-guide architecture IDs, the ownership/defer contract, the four-pillar
safety contract, known biases/limitations, quality risks, and adopt/prototype/defer
decisions and the completed module/review state. This is the durable architecture reference
for future pathology maintenance and promotion work.

> **Status: FINAL — module complete; Pulse 05 final PASS recorded 2026-07-12.**
>
> **⇢ RECONCILED 2026-07-12.** This record was first written as a **prototype boundary
> review** covering guides `08`/`10` only. That framing is **superseded**: all **12/12**
> guides are now authored at full peer depth and focused-MDLOOM-clean; the module is
> **integrated** (`sections/life-sciences.md`, `.mkdocs/mkdocs.yml`, `TRACKER.md`),
> **reciprocally wired** with the architecture-approved minimal sibling pointers
> (`disease/00`→`01`–`03`; `disease/04`→`05`/`10`; `medicine/10`→`08` preserving its
> `clinical-medicine/03` pointer; `clinical-medicine/03`→`pathology/`), and
> **source-corpus backfilled** (`pathology/` plus the changed siblings `disease`,
> `medicine`, `clinical-medicine`), custody `partial`. Throughout this record, any sentence
> that calls the remaining guides, integration, reciprocal pointers, or backfill
> *deferred / planned / not-added-this-pulse* is **historical and superseded** — the
> authoritative current state is the **Ratified Guide Manifest** (now **12/12 complete**)
> and the *Reconciliation* note in `pulses/05+pathology-architecture.md`. Provenance note:
> `pathology/` is still untracked, so the backfill records **`mdloom-backfill` backsources
> only**; the module ledger truthfully reports Git provenance recorded for **0** guides and
> pending for **12**. The generator adds `git-history` only when real tracked history exists.
>
> **Review history.** Prototype adversarial panels **R1** (`panels/pathology-prototype-r1/`)
> and strict **R2** (`panels/pathology-prototype-r2/`) gated `08`/`10` — R2 sharpened the
> total-error model to matched-unit formulas, reserved RCV for serial within-person change
> (removing the cross-lab RCV recommendation), split spectrum-dependent Sn/Sp/LR from
> prevalence-dependent PPV/NPV/posterior, corrected the margin claim to examined-inked-margin
> status (not proof of complete excision), and separated unavailable tissue architecture from
> meaningful cytologic group arrangements. The `09`/`11` **scaling gates** both passed
> Stage 2 after repair. The **full-module** adversarial panel is
> recorded under **`panels/pathology-full-r1/`** (`expert-skeptic` + `reference-editor` +
> consolidated); its content findings are repaired in the guides and its custody finding is
> fixed in the backfill generator. `R2-gold-rubric.md` records guide-specific ten-dimension
> scores and reader-task evidence: all twelve guides are **Silver**, with no registry
> insertion because pathology-specific Da Vinci invariants are absent and source custody is
> partial. The final reviewer returned **PASS** with no BLOCK/WARN; **Pulse 05 is DONE**.

## Summary

`pathology/` is designed as the **mechanism-to-diagnosis bridge** of MAXIM's Life
Sciences vertical (molecular → cellular → **tissue/lesion** → laboratory → **diagnosis**),
the layer that connects *why disease happens* (`disease/`, `human-biology/`) to *how a
clinician reasons and acts* (`clinical-medicine/`). Its unique, non-duplicating value is
the **causal chain from injury to observable finding to reported diagnosis**: general/
cellular pathology mechanisms (guides 01–07), how a laboratory result is generated and
bounded (08), anatomic technique (09), the reasoning that turns a morphologic pattern into
a signed report (10), and the diagnostic laboratory as a quality system (11). The pivotal
architecture call mirrors chemistry ("split by problem, not technique") and
clinical-medicine ("reusable reasoning patterns, not per-organ specialties"): **organize
general pathology by mechanism, not by organ system**, and teach diagnosis as a *reusable
method*, not a disease catalog. The sharpest boundary is the **three-way lab-interpretation
split** — `pathology/08` (result generation) vs `medicine/10` (catalog/ranges) vs
`clinical-medicine/03` (belief update) — which `clinical-medicine` Pulse 03 explicitly left
for this module to ratify. Two guides were prototyped to de-risk exactly the two boundaries
most likely to fail: `08` (does the lab-result content stay out of the `medicine/10`
catalog and the `clinical-medicine/03` decision theory?) and `10` (does the diagnostic
content teach a method without becoming a `disease/` catalog?). A strict **four-pillar
non-advice / non-procedure contract** is mandatory throughout.

## Research Question

How should MAXIM add a standalone `pathology/` module that is independently useful as a
peer-level educational reference on disease mechanism, laboratory-result generation, and
diagnostic reasoning, **without** (a) duplicating the disease catalogs (`disease/`), the
diagnostics/reference-range catalog (`medicine/10`), the diagnostic decision theory
(`clinical-medicine/03`), the differential-diagnosis cognition (`clinical-medicine/02`),
normal structure/function (`human-biology/`), immune-cell biology (`immunology/`), organism
biology (`microbiology/`, `virology/`), or the general analytical formalism
(`chemistry/04`); and (b) becoming medical advice, a bench procedure manual, or a forensic/
legal opinion? Sub-questions: the right 12-guide manifest and deep scope; whether general
pathology should be organized by mechanism or by organ system; how to ratify the three-way
lab-interpretation split now that `clinical-medicine` is complete; which boundaries are
risky enough to prototype first; and the four-pillar safety contract that keeps the module
educational yet peer-level.

## Findings

### Repository conventions & the depth bar

- **MAXIM-PATH-01 — Module shape is fixed by convention.** `00-OVERVIEW` (landscape/
  taxonomy) + `01…N` numbered `UPPERCASE-HYPHENATED.md` guides + `STATUS.md` (manifest, not
  counted in the total). Each guide carries `maxim.frontmatter.v1` YAML (`id:
  maxim:pathology:<slug>`, `module: pathology`, `section: pathology`, …), matching the
  chemistry/clinical-medicine precedent. The `status`/`source_custody`/`backsource_ids`
  triple is *lifecycle* metadata: **backfilled** guides read `status: source-custody` with
  `source_custody: partial|verified` and recorded backsource IDs, whereas the pre-backfill
  prototypes carry a truthful pre-backfill state (see MAXIM-PATH-25).
- **MAXIM-PATH-25 — Custody metadata must reflect actual provenance.** Prototype metadata
  began truthfully at `source_custody: needs-source` with no backsources. The completed
  backfill now promotes all twelve guides to `status: source-custody` /
  `source_custody: partial` with MDLOOM backfill records. Because the guides remain untracked,
  no guide may claim git provenance: the module ledger reports MDLOOM backfill for all 12,
  Git provenance recorded for 0, pending for 12. External/authentic factual backsources
  remain incomplete, so custody stays partial.
- **MAXIM-PATH-02 — Style contract & hard limits.** Landscape diagram first → layer
  downward → ASCII boxes → decision-useful tables → universal-CS-first bridges → end with
  **Decision Cheat Sheet** + **Common Confusion Points**. Hard cap ~32,000 tokens/guide.
  Learner is a peer (VP Eng, MIT Math+TCS); bridges route through universal CS/systems
  concepts (pipelines, error budgets, typed values, inference/compilation, delivery
  guarantees), not Azure specifics.
- **MAXIM-PATH-03 — Chemistry and the gate-passed clinical-medicine prototypes govern the
  bar.** The clinical-medicine `03`/`08` prototypes are the nearest, most directly
  applicable exemplars (same wave, same non-advice discipline). Reusable structure to copy:
  bold **"This guide owns / builds on / defers to"** header; an explicit boundary/overlap
  note that *resolves* the sharpest adjacency; a fully worked, clearly labeled illustrative
  case; a resource/geographic-variation section; reader tasks; cheat sheet; confusions.
- **MAXIM-PATH-04 — Review is adversarial and evidence-gated.** 3–5 concrete reader tasks
  answerable without another source; diagrams that do conceptual work; tables that decide/
  compare/compress; a focused numbers/names/frameworks fact-check. Lenses include
  `expert-skeptic` (overclaims/caveats/stale) and `index-weaver`; the `expert-skeptic` pass
  carries an explicit **advice-creep + procedure-creep** checklist; findings are BLOCK/WARN/
  NOTE; the exit gate requires no unresolved BLOCK.

### Placement in the library

- **MAXIM-PATH-05 — Belongs in Life Sciences as the mechanism-to-diagnosis bridge** of the
  molecular→clinical vertical, sitting between `disease/`/`human-biology/` (failure modes /
  normal function) and `clinical-medicine/` (reasoning that selects and acts). The
  clinical-medicine architecture (MAXIM-CLIN-05, MAXIM-CLIN-12) anticipated the owner of
  *why a result is what it is*. Placement is now **wired** in
  `sections/life-sciences.md`, `.mkdocs/mkdocs.yml`, and `TRACKER.md`.

### Overlap inventory (the core boundary problem)

- **MAXIM-PATH-06 — CRITICAL: the three-way lab-interpretation split must be ratified
  here.** `clinical-medicine` Pulse 03 (MAXIM-CLIN-12) *proposed* the split and explicitly
  deferred ratification to pathology authoring. Ratified form: `pathology/08` = *how the
  result is generated and how far to trust it* → `medicine/10` = *the catalog, panels, and
  reference bands* → `clinical-medicine/03` = *how a clinician updates belief and decides to
  act*. Guide `08` was prototyped precisely to prove this holds without leaking either way.
- **MAXIM-PATH-07 — `medicine/10-DIAGNOSTICS-IMAGING` already owns the diagnostics
  catalog** (CBC, metabolic/coagulation panels, cardiac biomarkers, blood gas, imaging, and
  a compact §11 reasoning section). `pathology/08` must own *result manufacture and
  uncertainty* and must **not** re-tabulate reference ranges/panels — it explains what a
  reference interval *is* and how it is derived, then hands off the numbers.
- **MAXIM-PATH-08 — `clinical-medicine/03` owns Bayesian belief updating** (2×2 belief
  engine, LR/odds, thresholds, value of information). `pathology/08` stops at the released
  result + its uncertainty and flags; `pathology/10` stops at a signed, calibrated
  diagnosis. Neither updates a posterior or recommends action — that is a hard boundary and
  a safety requirement.
- **MAXIM-PATH-09 — `clinical-medicine/02` owns the *clinical* differential** and its
  dual-process/cognitive-bias cognition. `pathology/10` owns the *morphologic*
  differential-by-pattern and the report; it inherits the dual-process and bias framing **by
  reference** and localizes it to morphology, rather than re-deriving it.
- **MAXIM-PATH-10 — `disease/` owns disease entities, catalogs, and natural history.**
  `pathology/` uses lesions only as *illustrations of a mechanism or a method*; it does not
  enumerate diseases. Guide `10` was prototyped to prove the diagnostic content teaches a
  *reusable method* with multi-organ examples, not a per-organ entity catalog — the
  pathology analogue of clinical-medicine's "interface catalog, not disease catalog."
- **MAXIM-PATH-11 — Adjacent life-science modules own their biology.** `immunology/` owns
  immune-cell biology (so `pathology/04` owns hypersensitivity *as a tissue-injury
  mechanism*); `microbiology/`/`virology/` own organisms (so `pathology/08` owns *how a
  micro/molecular result is generated*, not the organisms); `genomics/`/`biochemistry/`/
  `human-biology/` own gene/pathway/normal structure (so `pathology/` owns the *lesion*, not
  normal function). Name by reference, never re-derive.
- **MAXIM-PATH-12 — `chemistry/04-ANALYTICAL-QUANTITATIVE` owns the general analytical
  formalism** (calibration, LOD/LOQ, method validation). `pathology/08` *applies* it to
  biological matrices and clinical-laboratory constraints (interference, HIL, harmonization,
  RCV) rather than re-deriving the metrology from scratch — an explicit build-on, not a
  duplication.

### External framework grounding (grounded in standard summaries — verify against primary sources)

> **Citation status (not authoritative as written).** The framework attributions in
> MAXIM-PATH-13 … 17 are grounded in standard secondary summaries and textbook-level
> knowledge, **not** verified against the primary standards/PDFs. They are treated as
> *provisional pointers to verify*, never as authoritative citations. A focused
> re-verification (below and in Gaps) was run for the load-bearing ones during the prototype
> repair; the rest are to be confirmed during full authoring. Every number stays
> illustrative and dated.

- **MAXIM-PATH-13 — The discipline has two orthogonal top-level splits** that give `00` its
  spine: **anatomic vs clinical** pathology (tissue/cell diagnosis vs laboratory testing),
  and **general vs systemic** pathology (mechanisms that recur everywhere vs organ-specific
  disease). The module owns general + the diagnostic/laboratory apparatus; systemic disease
  is deferred to `disease/`.
- **MAXIM-PATH-14 — General pathology has a canonical mechanistic spine** (the Robbins-style
  organization): cell injury/adaptation/death; inflammation & repair; hemodynamic disorders/
  thrombosis/shock; immunopathology; neoplasia; genetic/developmental/metabolic; and
  environmental/nutritional/toxic injury. This maps 1:1 onto guides `01`–`07` and is the
  argument for a mechanism-first (not organ-first) manifest.
- **MAXIM-PATH-15 — Laboratory medicine has a canonical quality/metrology spine** for guide
  `08`: the **total testing process** / Lundberg brain-to-brain loop (1981); analytical
  performance (imprecision/bias/total error; measurement uncertainty per the GUM/ISO
  approach); CLSI evaluation protocols (e.g., EP17 detection-limit concepts; AUTO10
  autoverification); Westgard total-error and sigma metrics; the HIL interference indices;
  and the reference-change-value / delta-check model. (Attribute and date each; keep numbers
  illustrative.)
- **MAXIM-PATH-16 — Diagnostic reporting has canonical frameworks** for guide `10`:
  structured **synoptic reporting** (CAP-protocol style), the **TNM** staging *framework*
  (definitions per site owned by `disease/`), calibrated **certainty-language** conventions,
  **critical-diagnosis** communication with verified delivery, and the **addendum/amendment/
  retraction** correction taxonomy. The reusable method — pattern → differential family →
  ancillary evidence → calibrated certainty → orthogonal classification → report — is the
  organizing spine.
- **MAXIM-PATH-17 — Diagnostic safety/quality has a canonical systems framing** for guide
  `11`: error taxonomy distributed across the total testing process (with the
  pre-/post-analytic phases dominating), external quality assessment / proficiency testing,
  accreditation frameworks *as concepts*, and the brain-to-brain loop as the diagnostic-
  safety backbone that threads through `08` and `10`.
- **MAXIM-PATH-23 — Focused citation verification (prototype-repair pass).** The
  load-bearing framework attributions were re-checked against standard references and
  **qualified** (not left as bare authoritative claims). Findings:
  - **Total testing process / brain-to-brain loop** — originates with Lundberg, *Acting on
    Significant Laboratory Results*, JAMA 1981;245(17):1762–1763; 40-year retrospective in
    Plebani, Laposata & Lundberg, *Am J Clin Pathol* 2011. Year **1981 confirmed**.
  - **Pre-analytic error dominance** — the "~60–70%" figure is **not** a universal constant;
    it derives from stat-laboratory error series (Carraro & Plebani and later work) and
    varies widely by setting/era/definition. Guide `08` was repaired to present it as an
    illustrative, setting-dependent range, not a law.
  - **Measurement uncertainty** — GUM = *Guide to the Expression of Uncertainty in
    Measurement* (JCGM 100 / ISO/IEC Guide 98-3); expanded uncertainty `U = k·u_c`. Framing
    confirmed; keep `k` illustrative.
  - **Total error vs allowable total error** — the Westgard model computes calculated total
    error in **matched units**: absolute `TEcalc_abs = |bias_abs| + z·SD_abs` (judged
    against `TEa_abs`) or relative `TEcalc_% = |bias_%| + z·CV_%` (judged against `TEa_%`),
    with `z ≈ 1.65` the one-sided ~95% quantile; an absolute bias is never added to a
    percentage CV. `TEa` is a *separate specification* (biological variation / regulatory-EQA
    / clinical need); the sigma metric uses matching percentage terms,
    `σ = (TEa_% − |bias_%|)/CV_%`. Guide `08` was repaired (R1: stop conflating
    `TEcalc`/`TEa`; R2: give the two matched-unit formulas, state the one-sided z, and use
    the percentage sigma).
  - **CLSI EP17** (*Evaluation of Detection Capability*, EP17-A2) — LoB is a **percentile of
    blank results** (`mean_blank + 1.645·SD_blank`, the one-sided 95th percentile), **not**
    the highest raw signal; guide `08` LoB definition was corrected accordingly.
  - **CLSI AUTO10-A** (autoverification) — **superseded/expanded by AUTO15**; guide `08` now
    cites AUTO10-A *and* AUTO15.
  - **TNM** — maintained by UICC/AJCC (e.g., AJCC 8th ed., 2017); the pathology report
    supplies **pathologic elements `pT`/`pN`/`pM`**, distinct from the **overall stage
    group**, which integrates T/N/M and, in current systems, selected **non-anatomic
    prognostic factors**, and is often assigned downstream. Guide `10` was repaired to make
    this distinction and to stop implying the report owns the stage group.
  - **Synoptic reporting** — CAP cancer protocols (US, tied to CoC/CAP accreditation) are one
    governing system; ICCR datasets (international) and RCPath datasets (UK) are others.
    Structured-completeness enforcement is **protocol-governed and heterogeneous**, not a
    universal "cannot sign" rule; guide `10` was repaired to scope this.
  - **Certainty language** — reframed in guide `10` from a *universal ladder mapped to
    posteriors* to **independent dimensions** on **locally governed lexicons / named category
    systems** (organ-specific reporting-category frameworks), which are population-, era-,
    and jurisdiction-specific — consistent with MAXIM-PATH-20/22.

### The organ-system decision (pivotal call)

- **MAXIM-PATH-18 — RECOMMENDATION: organize general pathology by mechanism (guides
  01–07) and teach diagnosis as a reusable method (guide 10); do NOT create per-organ
  systemic-pathology guides.** Rationale: (1) per-organ pathology guides would triplicate
  `disease/` + `human-biology/` + `clinical-medicine/`, violating EXPANSION's "avoid
  duplicating 80%+ of an existing module"; (2) the discipline's transferable value is the
  organ-agnostic *mechanism* (how cells are injured, how tissue inflames/repairs, how a
  neoplasm behaves) and the organ-agnostic *diagnostic method* (pattern → family →
  ancillary → certainty → classification → report) — parallel to chemistry's "split by
  problem, not technique" and clinical-medicine's "reusable patterns, not per-organ
  specialties"; (3) systemic/organ pathology still appears — as *illustration of a
  mechanism or method*, with hard defers to `disease/`.
- **MAXIM-PATH-19 — Prototype the two hardest boundaries first.** `08-LABORATORY-MEDICINE`
  (proves the three-way lab split resolves as generation-vs-catalog-vs-decision and hits the
  quantitative metrology depth bar) and `10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING`
  (proves "reusable method, not disease catalog" holds without leaking into `disease/` or
  the `clinical-medicine/03` decision theory). These are the two guides most at risk of
  *catalog/decision-theory boundary* failure and are prototyped first. **Not all remaining
  guides are low-risk, however:** guides `09` (anatomic technique) and `11` (laboratory-as-
  quality-system) each carry their own **scaling/boundary risk** — procedure-creep for `09`,
  and a `08`↔`11` ownership seam plus governance-scope creep for `11` — and are governed by
  explicit scaling mini-contracts and a **two-stage** review gate — a representative
  high-risk partial-draft mini-review *before* bulk authoring and a completed-guide
  whole-seam/whole-procedure review *before* sign-off (MAXIM-PATH-24). Only the mechanism
  guides `01`–`07` are genuinely lower-risk, and even
  they remain bound by the four-pillar contract and the hard defers to `disease/`.
- **MAXIM-PATH-24 — Guides 09 and 11 get scaling mini-contracts + a two-stage review gate.**
  Rather than treat the eight non-prototyped guides as uniformly safe, the two with the
  sharpest scaling risk are pinned now with contract artifacts (see the **Scaling
  Mini-Contracts** section) and a required **two-stage** review gate: `09` is prone to
  **procedure-creep** (becoming a runnable bench SOP, breaching pillar 2), and `11` is prone
  to **duplicating or contradicting `08`** on QC/error and to **over-broad
  governance/accreditation** scope. **Stage 1** is a scoped `expert-skeptic` pass on
  **representative high-risk draft sections** — for `09`, grossing/orientation plus the
  staining/frozen-section/cytology purpose/failure-mode sections; for `11`, the
  governance/accreditation section plus the total-testing-process error-taxonomy/QC section
  that carries the `08`↔`11` seam — which must pass before the full guide (and the remaining
  mechanism guides) is bulk-authored. **Stage 2** is a **completed-guide whole-procedure
  (`09`) / whole-seam (`11`) `expert-skeptic` review** that must pass **before sign-off**. A
  representative partial draft is necessary but not sufficient: the finished guide is
  re-reviewed end to end before it graduates.

## Ratified Guide Manifest (12 guides: 00 + 11)

Per-guide architecture IDs (MAXIM-PATH-G00 … G11) for traceability. **⇢ RECONCILED
2026-07-12: the manifest is now 12/12 complete** — all twelve guides are authored at full
peer depth, focused-MDLOOM-clean, integrated, source-backfilled, and reviewed; the module is
final and Pulse 05 is DONE. (Historically, `08`/`10` were the gate-candidate
prototypes, `09`/`11` the scaling-gate guides, and `00`–`07` the authoring round — the
per-row "planned"/"prototype" labels below are superseded by the "authored, reviewed"
status shown in each row.)

| Arch ID | # | File | Uniquely owns (peer depth) | Authoring status |
|---|---|------|------------------------------|------------------|
| MAXIM-PATH-G00 | 00 | `00-OVERVIEW.md` | Discipline map (anatomic/clinical; general/systemic); the mechanism→result→diagnosis spine; ownership/boundary table; four-pillar **non-advice/non-procedure contract**; reading order; software bridges | complete ✅ (authored, reviewed) |
| MAXIM-PATH-G01 | 01 | `01-CELL-INJURY-ADAPTATION-AND-DEATH.md` | Reversible/irreversible injury; hypoxia/ischemia/oxidative stress; adaptations; necrosis subtypes vs apoptosis; accumulations/calcification/aging | complete ✅ (authored, reviewed) |
| MAXIM-PATH-G02 | 02 | `02-INFLAMMATION-AND-TISSUE-REPAIR.md` | Acute vs chronic inflammation as a program; mediators; granulomatous pattern; resolution/regeneration/scarring/fibrosis; wound healing | complete ✅ (authored, reviewed) |
| MAXIM-PATH-G03 | 03 | `03-HEMODYNAMIC-DISORDERS-THROMBOSIS-AND-SHOCK.md` | Edema/congestion; hemostasis; Virchow's triad; thrombosis/embolism/infarction; shock classes as a cascade | complete ✅ (authored, reviewed) |
| MAXIM-PATH-G04 | 04 | `04-IMMUNOPATHOLOGY-AND-TISSUE-INJURY.md` | Hypersensitivity I–IV **as tissue-injury mechanisms**; autoimmunity; transplant rejection; immunodeficiency-as-lesion (immune-cell biology → `immunology/`) | complete ✅ (authored, reviewed) |
| MAXIM-PATH-G05 | 05 | `05-NEOPLASIA-CARCINOGENESIS-AND-TUMOR-BIOLOGY.md` | Hallmarks of cancer; benign/malignant; differentiation/anaplasia; invasion/metastasis mechanism; carcinogenesis; nomenclature *principles* (not a tumor catalog) | complete ✅ (authored, reviewed) |
| MAXIM-PATH-G06 | 06 | `06-GENETIC-DEVELOPMENTAL-AND-METABOLIC-PATHOLOGY.md` | Inherited-disease *pathology* principles; developmental/malformation mechanisms; inborn errors/storage as tissue lesions (gene mechanism → `genomics/`) | complete ✅ (authored, reviewed) |
| MAXIM-PATH-G07 | 07 | `07-ENVIRONMENTAL-NUTRITIONAL-AND-TOXIC-INJURY.md` | Physical/chemical/toxic injury mechanisms; nutritional-deficiency/overload lesions; environmental exposure pathology | complete ✅ (authored, reviewed) |
| MAXIM-PATH-G08 | 08 | `08-LABORATORY-MEDICINE.md` | How a laboratory result is generated and bounded: total testing process; analytical vs clinical Sn/Sp; imprecision/bias/linearity/uncertainty; interference; method comparison/harmonization; cell counting + smear-morphology interface; validation/flags | complete ✅ (authored, reviewed) |
| MAXIM-PATH-G09 | 09 | `09-ANATOMIC-PATHOLOGY-TECHNIQUE.md` | Gross-to-glass: fixation, processing, sectioning, staining principles, frozen section, cytology prep, IHC/molecular *substrate* — technique as principle/constraint, not SOP | complete ✅ (authored, reviewed) |
| MAXIM-PATH-G10 | 10 | `10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING.md` | Morphology-to-diagnosis reasoning + the report as interface: pattern recognition; differential pattern classes; ancillary-test integration; certainty language; grading/staging/margin *principles*; synoptic vs narrative; critical-result communication; amended reports | complete ✅ (authored, reviewed) |
| MAXIM-PATH-G11 | 11 | `11-QUALITY-ERROR-AND-THE-DIAGNOSTIC-LABORATORY-AS-SYSTEM.md` | The diagnostic service as a system: QC/QA; error taxonomy across the TTP; EQA/proficiency; accreditation *as concepts*; turnaround/flow; diagnostic safety and the brain-to-brain loop. Split Part 1/Part 2 if > ~32k tokens | complete ✅ (authored, reviewed) |

**Alternate manifests considered and rejected.** (a) A *per-organ systemic-pathology*
expansion (cardiac/renal/GI/… guides) — rejected as an 80%+ duplication of `disease/` +
`human-biology/` + `clinical-medicine/` (MAXIM-PATH-18). (b) A *lean 10-guide* variant that
folds laboratory medicine and diagnostic reporting into one guide — rejected because it
collapses the two most distinctive, highest-risk boundary guides (the very ones prototyped
here) into a single overloaded file that would breach the token cap and blur the three-way
split. Primary recommendation is **12**.

## Scaling Mini-Contracts (Guides 09 and 11)

Per MAXIM-PATH-24, the two non-prototyped guides with the sharpest scaling risk are pinned
now with contract artifacts so full authoring does not re-open settled scope. Each carries a
**two-stage review gate**: (1) a scoped `expert-skeptic` pass on **representative high-risk
draft sections** that must pass *before* the guide is bulk-authored and before the
lower-risk mechanism guides `01`–`07` are written, and (2) a **completed-guide whole-seam /
whole-procedure `expert-skeptic` review** that must pass *before* the finished guide is
signed off. The partial pass gates authoring; the whole-guide pass gates sign-off — a
representative partial draft is necessary but not sufficient.

### Guide 09 — Anatomic Pathology Technique (purpose/failure-mode only, no runnable steps)

- **Owns:** the *principle and constraint* behind each substrate-making step — why fixation,
  processing, embedding, sectioning, staining, frozen section, cytology preparation, and
  IHC/molecular substrate exist, what each is *for*, and how each *fails* in a way that
  changes what the slide can support downstream (`10`).
- **Hard exclusion (pillar 2):** **no runnable procedure.** No reagent formulations, times,
  temperatures, dilutions, cutting sequences, or step-by-step "how to perform" content. The
  guide describes technique as *purpose → failure mode → downstream consequence*, never as an
  executable SOP. Any imperative bench step is a **BLOCK**.
- **Contract shape:** for each step, a triple — *purpose* (what it enables), *failure mode*
  (what goes wrong: e.g., under-fixation, decalcification antigen loss, folds/chatter,
  edge/scan artifact), and *consequence* (how it bounds adequacy/interpretation in `10`,
  e.g., Gate-1 analytical validity of a stain). Cross-references: substrate → `10 §4`
  (analytical validity), `08` (result generation for molecular/IHC signals).
- **Mini-review gate (two stages).** (1) *Partial-draft mini-review* — a scoped
  **procedure-creep** `expert-skeptic` pass on **representative high-risk draft sections**:
  at minimum the **grossing/orientation** section (the step most prone to becoming a cut-up
  SOP) **plus the staining, frozen-section, and cytology-preparation purpose/failure-mode
  sections** — confirming zero runnable steps (no reagents, times, temperatures, dilutions,
  or cutting sequences) and a clean *purpose → failure mode → downstream consequence*
  framing, before the rest of `09` is bulk-authored. (2) *Completed-guide whole-procedure
  review* — once the full guide exists, a final `expert-skeptic` pass over **the entire
  gross-to-glass procedure surface, end to end**, must confirm the no-runnable-steps
  (pillar-2) contract holds across the whole guide **before sign-off**. The partial pass
  gates authoring; the whole-procedure pass gates sign-off.

### Guide 11 — Laboratory as a Quality System (owns cross-process QC/error/governance)

- **Owns:** the diagnostic service *as a system* — QC/QA across the **total testing
  process**, the cross-process **error taxonomy** (pre-/analytic/post-analytic and the
  brain-to-brain loop), EQA/proficiency, accreditation/governance **as concepts**,
  turnaround/flow, and diagnostic safety. `11` owns the *cross-process quality, error, and
  governance* layer.
- **`08`↔`11` ownership seam (the scaling risk):** `08` owns **method/result generation and
  bounding** and introduces *only* the QC/error concepts it needs *locally* to explain a
  single result (e.g., a delta check or an autoverification gate *as they bound one result*).
  `11` owns the **cross-process** system: QC strategy (e.g., Westgard multirules as a
  program), error taxonomy across phases, EQA programs, governance/accreditation, and the
  safety loop as an institutional system. Neither re-derives the other; `08` points forward
  to `11` for the system view, `11` points back to `08` for result-level generation.
- **Hard exclusions:** no duplication of the `08` metrology derivations; no accreditation
  "how-to" or jurisdiction-specific compliance instructions (governance *as concept*, dated
  and attributed); no forensic/legal determinations (pillar 3).
- **Mini-review gate (two stages).** (1) *Partial-draft mini-review* — a scoped
  `expert-skeptic` pass on **representative high-risk draft sections**: at minimum the
  **governance/accreditation** section (the one most prone to over-broad or prescriptive
  scope) **plus the total-testing-process error-taxonomy/QC section that carries the
  `08`↔`11` seam** — confirming (a) no `08` duplication/contradiction, (b) governance kept
  conceptual, dated, and non-prescriptive (no accreditation how-to or jurisdiction-specific
  compliance steps), and (c) a clean forward/back cross-reference with `08`, before the rest
  of `11` is bulk-authored. (2) *Completed-guide whole-seam review* — once the full guide
  exists, a final `expert-skeptic` pass over **the entire `08`↔`11` seam and the whole
  governance/error/QC surface** must confirm the ownership split and non-prescriptive
  governance hold across the finished guide **before sign-off**. The partial pass gates
  authoring; the whole-seam pass gates sign-off. If `11` exceeds ~32k tokens, split
  Part 1/Part 2 per the token cap.

**Guide `08` note (already applied):** the repaired `08` deliberately introduces QC/error
concepts *only* to the extent needed to bound a single result (delta check, autoverification
gate, sigma as method headroom), and defers the cross-process quality-system treatment to
`11` — the seam this contract formalizes.

**Guide `11` Stage-2 repair note (2026-07-12):** the completed-guide whole-seam review returned
seam/accuracy findings, now **repaired in `11`**. The clean review then passed, as did guide
`09`'s whole-procedure review (see `panels/pathology-{09,11}-scaling/`). The corrected seam is
pinned here so it does not re-open:
- `11` does **not** re-derive `08 §6` EQA/PT mechanics — internal QC can detect *some* bias
  (assayed/independent controls, reference materials, calibration verification, method comparison),
  and **EQA is an external comparison, not an oracle, and is broader than PT (EQA ⊋ PT)**; `11` owns
  EQA program governance, longitudinal review, limitations, corrective response, and alternatives
  when PT is unavailable.
- **Levey–Jennings limits come from the control material's own mean/SD** (established locally),
  `1_2s` is a warning vs `1_3s`/multirule rejection, and bias/TEa/sigma inform **QC planning**, not
  chart-limit construction; QC also spans qualitative/micro/molecular/anatomic-IHC and pre-/post-
  analytic controls, not only quantitative chemistry.
- **CAPA** = correction/containment → impact assessment → cause analysis → **corrective action
  (removes/controls the cause; prevents recurrence)** → effectiveness verification, with
  **preventive action / prospective risk control separate**.
- **Accreditation = ISO 15189:2022 scope-specific competence, impartiality, and consistent
  operation — not certification / QMS conformance**; QC/EQA/audit/accreditation are distinguished
  and **none attests an individual result**.
- Validation/verification deepened (objective evidence; reference-interval verification distinct
  from method verification; modified methods may require validation); nonconforming-work/amendment
  handling deepened with amendment metrics **stratified** (addenda ≠ automatic defects); internal
  audit / EQA-PT / M&M / clinicopathologic autopsy distinguished; routine traceability qualified
  against legal chain of custody; a resource-constrained case/task added. Records: `STATUS.md`,
  `pulses/05+pathology-architecture.md`, and `panels/pathology-{09,11}-scaling/`.

**Uniquely owns** (name by reference elsewhere, re-derive nowhere): general-pathology
mechanisms — cell injury (01), inflammation/repair (02), hemodynamics/thrombosis/shock
(03), immunopathology as tissue injury (04), neoplasia mechanism (05), genetic/
developmental/metabolic pathology (06), environmental/nutritional/toxic injury (07);
**laboratory-result generation and bounding** (08); anatomic technique as principle (09);
**morphology-to-diagnosis reasoning and the report** (10); and the **diagnostic laboratory
as a quality system** (11).

**Defers to** (name by reference, never re-derive):

| Defers to | For |
|---|---|
| `medicine/10-DIAGNOSTICS-IMAGING` | The test **catalog**, reference intervals/ranges, panel membership, analyte time-courses, imaging **physics** |
| `clinical-medicine/03-DIAGNOSTIC-TEST-INTERPRETATION` | **Bayesian belief updating** — pretest/posttest probability, LRs, test/treatment thresholds, action |
| `clinical-medicine/02-DIFFERENTIAL-DIAGNOSIS` | The *clinical* differential + dual-process/cognitive-bias cognition (borrowed by reference in `10`) |
| `disease/` | Disease entities, catalogs, natural history; entity-specific grading/staging systems |
| `immunology/` | Immune-cell biology and signaling (pathology owns hypersensitivity *as lesion*) |
| `microbiology/`, `virology/` | Organism biology/taxonomy (pathology owns *how a micro/molecular result is generated*) |
| `genomics/`, `biochemistry/`, `human-biology/` | Gene/pathway mechanism and normal structure/function |
| `chemistry/04-ANALYTICAL-QUANTITATIVE` | The general analytical formalism (calibration, LOD/LOQ, method validation) |
| `public-health/`, `statistics-applied/` | Population screening **programs**; study-design methods |
| `law/`, `criminology/` | Statute/precedent; forensic/legal (cause-/manner-of-death) determination — **out of scope** |

**Three-way lab-interpretation split (ratified in this pulse, MAXIM-PATH-06):**
`pathology/08` = *how the result is generated and how far to trust it* → `medicine/10` =
*the catalog, panels, and reference bands* → `clinical-medicine/03` = *how a clinician
updates belief and decides to act*.

## Four-Pillar Safety Contract (mandatory review gate)

A module-level disclaimer heads `00-OVERVIEW` and is embedded/referenced by every guide;
each content guide also carries a one-line banner under its title. Four pillars, each a
hard **BLOCK** in `expert-skeptic` review:

1. **No self-diagnosis / no personal-result interpretation.** Content explains *how the
   laboratory and the pathologist produce and reason about findings in general*, never what
   any reader's own result, image, slide, or lesion means. Worked cases are explicitly
   fictional teaching vignettes.
2. **No specimen-collection or laboratory-operating instructions.** No phlebotomy,
   collection, grossing, assay setup, staining, or bench SOPs. Technique is described at the
   level of *principle and constraint* (guide 09), never as a runnable procedure.
3. **No forensic/legal advice.** Autopsy/forensic content, where it appears, is conceptual;
   no cause-of-death, manner-of-death, or legal determinations.
4. **Third-person descriptive voice; illustrative, dated numbers.** No second-person
   imperatives ("interpret your…", "collect…"). Every numeric threshold/metric/coverage
   factor is labeled illustrative and attributed where it names a real standard; every
   classification system named is dated/attributed and deferred to `disease/` for specifics.

`expert-skeptic` carries an explicit **advice-creep + procedure-creep** checklist; any
imperative-mood self-diagnosis, personal-result interpretation, bench/collection procedure,
or forensic/legal determination is a **BLOCK**.

## Bias / Geographic Limitations

- **MAXIM-PATH-20 — Reference intervals and classification systems are population-, era-,
  and jurisdiction-specific.** The healthy reference population (age/sex/ancestry/altitude)
  shifts a reference interval; grading/staging systems are periodically revised by expert
  bodies. Attribute and date; never universalize one population's interval or one edition's
  system. (Actual intervals are `medicine/10`; entity-specific systems are `disease/`.)
- **MAXIM-PATH-21 — The laboratory and diagnostic guides assume a resourced setting.**
  MALDI-TOF, high-sensitivity immunoassays, molecular/NGS, broad IHC panels, on-call frozen
  section, and subspecialty sign-out are concentrated in resourced laboratories; district/
  low-resource settings reason microscopy- and morphology-forward, with send-out/referral
  and telepathology. Standardization coverage is uneven (only some analytes have a reference
  method/material). Each affected guide (08, 09, 10, and 11) carries a
  resource-tier-variation section; the *reasoning* transfers, the *toolbox* does not.
- **MAXIM-PATH-22 — Morphologic and laboratory judgment carry intrinsic variability and
  scope limits.** Interobserver variability is real and bounded (e.g., kappa for grading);
  consensus/second-opinion/referral exist because judgment is not perfectly reproducible.
  The histology/laboratory evidence base skews to certain populations and platforms.
  Forensic/autopsy legal determination is out of scope (pillar 3). State these limits;
  never present a grade, interval, or certainty phrase as a universal constant.

## Quality Risks (with mitigations)

| ID | Risk | Severity | Mitigation |
|---|---|---|---|
| QR-1 | Advice creep (self-diagnosis / personal-result or personal-slide interpretation) | Highest | Four-pillar contract pillar 1; expert-skeptic advice-creep checklist; imperative interpretation = BLOCK; all cases explicitly fictional |
| QR-2 | Procedure creep (specimen collection, grossing, staining, assay setup as runnable SOPs) | Highest | Pillar 2; procedure-creep checklist; technique as principle/constraint only (guide 09); runnable SOP = BLOCK |
| QR-3 | Duplication of the `medicine/10` catalog (reference ranges/tests/panels) | High | 08 owns *result generation and uncertainty* only; explains what a reference interval *is*, defers the numbers; three-way split |
| QR-4 | Duplication of `clinical-medicine/03` decision theory (Bayesian belief updating) | High | 08 stops at the released result; 10 stops at the signed report; belief-update math deferred by reference |
| QR-5 | Disease-catalog creep in 10 (and 01–07) | High | Examples-as-illustration; 10 teaches a *reusable method*; hard defer of entities/criteria to `disease/` |
| QR-6 | Forensic/legal creep (cause-/manner-of-death, legal opinion) | Med | Pillar 3; conceptual only; explicit out-of-scope in ownership table and banner |
| QR-7 | Staleness of classification systems / reference intervals / breakpoints | Med-High | Teach the *reasoning* + where current guidance lives; numbers illustrative/dated/attributed |
| QR-8 | Analytical-vs-clinical Sn/Sp conflation (the central lab confusion) | Med | Dedicated section (08 §4) + a Common Confusion Point; force the reader to name which sense |
| QR-9 | Resourced-setting bias | Med | Resource-tier-variation section in each affected guide; comparative, non-universalizing framing |
| QR-10 | "Soft outline" failure (platitudes, not depth) | High | Anchor every guide in a concrete formalism (metrology math — TEcalc vs TEa, RCV, LoB — in 08; the inference pipeline + the four independent certainty dimensions + orthogonal grade/stage/margin axes + the parse matrix in 10); match the chemistry/clinical depth bar |
| QR-11 | Boundary churn with the now-complete `clinical-medicine` module | Low-Med | The three-way split was pre-proposed by clinical Pulse 03 (MAXIM-CLIN-12); ratified here; reciprocal sibling pointers were prototype-gated and have **since been added** (2026-07-12: `disease/00`→`01`–`03`; `disease/04`→`05`/`10`; `medicine/10`→`08`; `clinical-medicine/03`→`pathology/`) |
| QR-12 | Scaling risk in the non-prototyped boundary guides (09 procedure-creep; the `08`↔`11` QC/error/governance seam) — **not all remaining guides are low-risk** | Med-High | Scaling mini-contracts pinned now (MAXIM-PATH-24) with a **two-stage** gate: a Stage-1 `expert-skeptic` pass on **representative high-risk draft sections** (09 grossing/orientation + staining/frozen/cytology; 11 governance/accreditation + the total-testing-process `08`↔`11` seam) before bulk authoring, **and** a Stage-2 **completed-guide whole-procedure/whole-seam review before sign-off**; 08 introduces QC/error only as needed locally and defers the cross-process system to 11 |
| QR-13 | False-authority citation (summaries presented as verified primary standards) | Med | MAXIM-PATH-23 citation-verification pass; "External framework grounding" heading de-authoritized; load-bearing attributions qualified and to be re-verified against primary sources at full authoring |
| QR-14 | Custody metadata claiming provenance that does not exist | Med | Backfill complete with `source_custody: partial`; MDLOOM backfill recorded for all 12; Git provenance recorded for 0 and pending for 12 while guides are untracked; generator adds `git-history` only with real history; external/authentic factual backsources remain future work |

## Adopt / Prototype / Defer

**ADOPT:** the 12-guide mechanism-to-diagnosis manifest; the mechanism-first (not
per-organ) general-pathology decision and the method-not-catalog diagnostic decision
(MAXIM-PATH-18); the ownership/defer table + the ratified three-way lab split
(MAXIM-PATH-06); the four-pillar non-advice/non-procedure contract as a hard gate; wired Life Sciences placement; the anatomic/clinical +
general/systemic spine cited in `00`.

**PROTOTYPE-FIRST HISTORY (completed):** `08-LABORATORY-MEDICINE` proved the lab-result content
stays out of the `medicine/10` catalog and the `clinical-medicine/03` decision theory while
hitting the quantitative metrology depth bar; `10-DIAGNOSIS-PATTERN-RECOGNITION-AND-
REPORTING` proved the diagnostic content teaches a reusable method with multi-organ
examples without becoming a `disease/` catalog and packages certainty as a calibrated,
communicated report. Both passed strict prototype review before full authoring.

**COMPLETED / OUT OF SCOPE:** the former deferred work is complete: guides `00`–`07`,
`09`, and `11` are authored; reciprocal sibling links, section/navigation/`TRACKER`
integration, and source-corpus backfill are in place. Permanently out of scope are per-organ
systemic-pathology duplication, runnable laboratory procedures, forensic/legal
determinations, and sibling-owned catalogs/decision theory.

## Gaps & Uncertainties (carry-forward)

- **External source custody remains partial.** MDLOOM literal backfill and round-trip evidence
  exist for all twelve guides, but claim-level authentic/primary-source custody is incomplete.
  The standard/framework pointers remain qualified rather than authoritative.
- **Git provenance remains pending for all twelve guides.** The module is untracked in the
  current working tree, so the truthful ledger count is Git provenance recorded for 0 and
  pending for 12. A future post-commit regeneration can record real history.
- **Pathology-specific Da Vinci invariants do not exist.** The R2 rubric therefore assigns
  Silver rather than Gold despite strong guide quality and ordinary focused-MDLOOM
  cleanliness. Pinning load-bearing figures and performing a final Gold promotion review is
  future work.
- **Registry insertion is intentionally absent.** No pathology row belongs in Certified Gold
  or another promotion table until the missing prerequisites are supplied and re-reviewed.
- **Pulse 05 final sign-off: PASS (2026-07-12).** Authoring, integration, reciprocal
  wiring, source backfill, scaling review, full-module adversarial review, and guide-specific
  R2 tier evidence are complete with no unresolved BLOCK/WARN.
