---
wave: clinical-and-chemical-foundations
pulse: 03
kind: architecture-record
module: clinical-medicine
date: 2026-07-11
status: final
governing_roles: [reference-editor, expert-skeptic, index-weaver, ascii-cartographer]
---

# clinical-medicine/ — Architecture & Research Record (Pulse 03)

Wave-local summary of the clinical-medicine architecture research. Condenses the
Pulse-03 design report into a durable record: the research question, the numbered
findings (MAXIM-CLIN-01 … MAXIM-CLIN-24), the ratified 12-guide manifest with
per-guide architecture IDs, the ownership/defer contract, the non-advice contract,
known biases/limitations, quality risks, and adopt/prototype/defer decisions. This is
the reference the Pulse-04 authoring pass and the Pulse-05 pathology coordination
should build against.

> **Status reconciliation (final).** The architecture specified here is **ratified and final**.
> The module it defines is now **fully authored — all 12 guides complete** (Pulse 04) — and the
> `medicine/10 §11` ↔ `clinical-medicine/03` boundary is wired **both ways**: the forward pointer
> from `03` (present since Pulse 03) plus a reciprocal pointer from `medicine/10 §11` → `03` (added
> in Pulse 04). Passages below that describe the link as *forward-only*, or the reverse pointer as
> *deferred* / *not yet bidirectional*, record the Pulse-03 point-in-time plan and are
> **superseded** by that bidirectional wiring. The full-module adversarial review
> and guide-specific rubric evidence are complete under `panels/clinical-full-r1/`;
> they confirm rather than alter this architecture.

## Summary

`clinical-medicine/` is designed as the **reasoning-and-care-architecture apex** of
MAXIM's Life Sciences vertical (molecular → cellular → organismal → population →
**clinical**), a layer the section landscape already anticipates but has no directory
for. Its unique, non-duplicating value is the **transferable cognitive and system
architecture of medicine** — clinical reasoning, diagnostic decision theory, evidence
appraisal, care-process design — **not** disease catalogs (`disease/`), drug lists
(`medicine/`, `pharmacology/`), physiology (`human-biology/`), or population methods
(`public-health/`). The pivotal architecture call is to organize **around reusable
reasoning patterns, not per-organ-system specialties** — the single most important
non-duplication decision, mirroring chemistry's "split by problem, not by technique."
The sharpest overlap is `medicine/10-DIAGNOSTICS-IMAGING` (~lines 460–600), which
already carries a Bayesian diagnostic-reasoning section; it is resolved by having
`clinical-medicine/03` own the **decision theory at depth** while `medicine/10`
remains the **catalog + imaging physics** (plus a short compact reasoning section).
The link is now **bidirectional**: a forward cross-reference from `clinical-medicine/03`
→ `medicine/10` (present since Pulse 03) and a reciprocal pointer from `medicine/10 §11`
→ `clinical-medicine/03` (added in Pulse 04). The two treatments are deliberately layered —
a catalog-side quick reference vs. graduate-depth decision theory — not a duplication to
reconcile. A strict **non-advice contract** is mandatory throughout.

## Research Question

How should MAXIM add a standalone `clinical-medicine/` module that is independently
useful as a peer-level educational reference on clinical reasoning and care
architecture, **without** (a) duplicating the disease catalogs, drug lists,
physiology, and population-health methods MAXIM already owns, and (b) becoming
medical advice? Sub-questions: the right 10–12-guide manifest and deep scope; whether
organ-system specialties should be guides or reasoning patterns; exact boundaries
against `medicine/`, `disease/`, `pharmacology/`, `human-biology/`, `public-health/`,
`psychology/`, `nutrition/`, `immunology/`, and the concurrent `pathology/`; and the
non-advice/safety contract that keeps it educational yet peer-level.

## Findings

### Repository conventions & the depth bar

- **MAXIM-CLIN-01 — Module shape is fixed by convention.** `00-OVERVIEW` (landscape/
  taxonomy) + `01…N` numbered `UPPERCASE-HYPHENATED.md` guides + `STATUS.md`
  (manifest, not counted in the total). Each guide carries `maxim.frontmatter.v1`
  YAML (`id: maxim:<module>:<slug>`, `module`, `section`, `title`, `status:
  source-custody`, …).
- **MAXIM-CLIN-02 — Style contract & hard limits.** Landscape diagram first → layer
  downward → ASCII boxes → decision-useful tables → universal-CS-first bridges → end
  with **Decision Cheat Sheet** + **Common Confusion Points**. Hard cap ~32,000
  tokens/guide (split Part 1/Part 2 if long). Learner is a peer (VP Eng, MIT Math+TCS);
  bridges route through universal CS/systems concepts, not Azure specifics.
- **MAXIM-CLIN-03 — Chemistry is the governing exemplar**, deliberately deeper than
  `computing/01-PACKAGE.md`. Reusable structure to copy: opening landscape + one-line
  caption; "Layers Below and Above" stack diagram with an "owns" contract; "What Each
  Guide Owns (and Where NOT to Look Here)" table; software-mental-model bridge table;
  reading-order-by-background; reader tasks; cheat sheet; confusions. Every content
  guide opens with a bold **"This guide owns… / builds on… / defers to…"** header.
- **MAXIM-CLIN-04 — Review is adversarial and evidence-gated.** 3–5 concrete reader
  tasks answerable without another source; diagrams that do conceptual work; tables
  that decide/compare/compress; a focused numbers/names/formulas fact-check. Lenses
  include `expert-skeptic` (overclaims/caveats/stale) and `index-weaver`; findings are
  BLOCK/WARN/NOTE; the module exit gate requires no unresolved BLOCK.

### Placement in the library

- **MAXIM-CLIN-05 — Belongs in Life Sciences as the clinical apex** of the
  molecular→clinical vertical. `disease/` supplies failure modes, `human-biology/`
  normal function, `medicine/`+`pharmacology/` interventions; `clinical-medicine/`
  supplies the reasoning that selects, sequences, and governs them for an individual.
  Pulse 04 created and registered `clinical-medicine/` in the TRACKER row,
  `sections/life-sciences.md`, MkDocs navigation, and the validated source-corpus
  pipeline. `pathology/` remains the next planned module.

### Overlap inventory (the core boundary problem)

- **MAXIM-CLIN-06 — CRITICAL: `medicine/10` already has a full Bayesian diagnostic-
  reasoning section** (Sn/Sp/PPV/NPV with ML equivalents, SnNout/SpPin, ROC/AUC, LRs,
  Fagan/odds updating, a Wells-score DVT worked example, prevalence dependence, NNT/
  NNH, named decision rules, ACR appropriateness, incidentaloma algorithms). Biggest
  duplication risk. **Resolution:** `clinical-medicine/03` owns the decision theory at
  graduate depth (2×2 as belief engine, **test-treatment threshold model**, calibration,
  value-of-information, overtesting cascades); `medicine/10` remains the catalog +
  reference ranges + imaging physics plus a short compact reasoning section. The
  boundary is now wired **both ways**: the forward cross-reference from `03` (Pulse 03)
  plus a **minimal reverse** pointer from `medicine/10 §11` → `03` (added in Pulse 04,
  the only `medicine/` edit). The overlap is resolved as decision-theory-vs-catalog with
  deliberately layered, bidirectionally cross-referenced treatments — no longer a
  deferred, forward-only boundary. *(Pulse-03 note, superseded: the reverse pointer was
  deferred at the time because rescoping `medicine/` was out of scope for that pulse.)*
- **MAXIM-CLIN-07 — `disease/` owns disease catalogs/mechanisms/natural history by
  category** plus epidemiology basics (R₀). `clinical-medicine/` uses diseases only as
  illustrative examples inside a reasoning move; it does not enumerate them.
- **MAXIM-CLIN-08 — `medicine/`+`pharmacology/` own drug knowledge.**
  `clinical-medicine/` owns prescribing/deprescribing *reasoning*, polypharmacy, and
  interaction *decision-making*; names drug mechanisms/classes only by reference; **no
  dosing, ever** (also a safety requirement).
- **MAXIM-CLIN-09 — `human-biology/` owns organ-system anatomy & physiology** — the
  strongest argument against per-organ guides here (normal function is already a
  complete module).
- **MAXIM-CLIN-10 — `public-health/` owns the population layer** (levels of prevention
  as programs; study-design methods; surveillance; screening programs; health-system
  typology/financing; DALYs/QALYs). Its overview already contrasts "clinical medicine
  (individual)" vs "public health (population)" — a ready-made seam.
  `clinical-medicine/` owns the **individual encounter**: prevention/screening as a
  *shared decision for one person*, and *clinical* workflow — **not** financing macro-
  typology.
- **MAXIM-CLIN-11 — `psychology/`, `nutrition/`, `immunology/` overlaps are narrow.**
  Reference them for how a clinician integrates a psychiatric/nutritional/immunologic
  problem into a differential/care plan; never re-derive them.
- **MAXIM-CLIN-12 — `pathology/` (concurrent) is the mechanism-to-diagnosis bridge and
  needs a coordinated three-way split now:** `pathology/` = *why a result is what it
  is* (tissue/cell mechanism, histology, lab-medicine method) → `medicine/10` = *the
  catalog + reference ranges* → `clinical-medicine/03` = *how a clinician updates
  belief and decides to act*. Agree this before either module drafts lab content.

### External framework grounding (authoritative)

- **MAXIM-CLIN-13 — Competency frameworks give the module its spine.** ACGME **six
  core competencies** and AAMC **13 Core EPAs** map ~1:1 onto the guide topics; AAMC
  **PCRS** adds interprofessional collaboration and professional development. Cite in
  `00-OVERVIEW` so the module is a recognizable map of the discipline.
- **MAXIM-CLIN-14 — Clinical reasoning has a teachable formalism** (antidote to a
  "soft concepts" module): dual-process theory, illness scripts, problem
  representation, semantic qualifiers, hypothetico-deductive reasoning, diagnostic
  schemas. Anchors guides 01–02.
- **MAXIM-CLIN-15 — Diagnostic safety has a canonical framework** (NASEM,
  *Improving Diagnosis in Health Care*, 2015): error = failure to establish an
  accurate/timely explanation **or to communicate** it; contributors cognitive +
  system + communication; debiasing via diagnostic timeout, forced System-2, bias
  awareness. Backbone of guide 02's back half; thread into guide 11.
- **MAXIM-CLIN-16 — EBM/guideline reasoning is well-specified** (Sackett 1996;
  evidence hierarchy; GRADE; PICO; ARR/RRR/NNT). Makes guide 04 concrete and defers
  study-design mechanics to `public-health/01`.
- **MAXIM-CLIN-17 — Patient-safety/quality have canonical models** for guide 11: IOM
  *To Err Is Human* (1999); Reason's Swiss-cheese (latent/active); Donabedian SPO; IHI
  Triple/Quadruple Aim; HRO principles; PDSA. (Verify the 44,000–98,000 estimate
  against the primary source before printing.)
- **MAXIM-CLIN-18 — Ethics/consent/capacity/SDM/geriatrics have standard tools** for
  guides 09–10 and 06: Beauchamp & Childress four principles; Appelbaum's four
  abilities; informed-consent elements; Elwyn three-talk SDM; geriatric 5Ms; Beers and
  STOPP/START.

### The organ-system decision (pivotal call)

- **MAXIM-CLIN-19 — RECOMMENDATION: organize around reusable reasoning patterns; do
  NOT create per-organ-system specialty guides.** Rationale: (1) per-organ guides
  triplicate `disease/`+`human-biology/`+`medicine/`+`pharmacology/`, violating
  EXPANSION's "avoid duplicating 80%+ of an existing module"; (2) the discipline's
  transferable value is the organ-agnostic reasoning move (problem representation,
  Bayesian updating, threshold decisions, deprescribing logic) — parallel to
  chemistry's "split by problem, not technique"; (3) specialties are still represented
  — **as an interface/service catalog, not a disease catalog** (guide 08), with hard
  defers to `disease/`. Reasoning guides draw worked examples from multiple organ
  systems to show the pattern transfers.

## Ratified Guide Manifest (12 guides: 00 + 11)

Per-guide architecture IDs (MAXIM-CLIN-G00 … G11) for traceability; the manifest maps
all requested topics onto 12 files and merges patient-safety/quality and workflow
under one Systems-Based Practice guide (11).

| Arch ID | # | File | Uniquely owns (peer depth) | Authoring status |
|---|---|------|------------------------------|------------------|
| MAXIM-CLIN-G00 | 00 | `00-OVERVIEW.md` | Discipline map; ACGME-6 / AAMC-13-EPA spine; ownership/boundary table; **non-advice contract**; reading order; software bridges | complete ✅ |
| MAXIM-CLIN-G01 | 01 | `01-CLINICAL-ENCOUNTER.md` | H&P as information architecture; problem representation, semantic qualifiers, illness scripts | complete ✅ |
| MAXIM-CLIN-G02 | 02 | `02-DIFFERENTIAL-DIAGNOSIS.md` | Dual-process; diagnostic schemas; likely vs must-not-miss; cognitive bias + debiasing; NASEM framing | complete ✅ |
| MAXIM-CLIN-G03 | 03 | `03-DIAGNOSTIC-TEST-INTERPRETATION.md` | Diagnostic decision theory: 2×2 belief engine, LR/odds Bayes, PPV/NPV prevalence, ROC/AUC limits, Pauker–Kassirer test/treatment thresholds, sequential/correlated tests, overtesting/incidentaloma, VOI | complete ✅ (gate-passed prototype) |
| MAXIM-CLIN-G04 | 04 | `04-EVIDENCE-BASED-MEDICINE.md` | Sackett three-circle; PICO; evidence hierarchy; GRADE; NNT/ARR/RRR; population evidence → individual | complete ✅ |
| MAXIM-CLIN-G05 | 05 | `05-ACUTE-AND-CHRONIC-CARE.md` | Acute/undifferentiated prioritization schemas (conceptual only) vs chronic/longitudinal (trajectories, Chronic Care Model) | complete ✅ |
| MAXIM-CLIN-G06 | 06 | `06-MULTIMORBIDITY-AND-GERIATRICS.md` | Competing risks; guideline collision; polypharmacy/prescribing cascade/deprescribing; 5Ms; time-to-benefit | complete ✅ |
| MAXIM-CLIN-G07 | 07 | `07-CARE-TRANSITIONS.md` | Handoffs as information transfer (I-PASS/SBAR); med reconciliation; discharge; continuity; problem list as shared state | complete ✅ |
| MAXIM-CLIN-G08 | 08 | `08-SPECIALTY-INTERFACES.md` | Specialty map as service/interface catalog; generalist/specialist labor; care levels; consult-question quality; referral/comanagement ownership; closed-loop follow-up; practice variation; conflict resolution | complete ✅ (gate-passed prototype) |
| MAXIM-CLIN-G09 | 09 | `09-PREVENTION-AND-SCREENING.md` | Individual-level prevention/screening as shared decision; overdiagnosis, lead-time/length-time bias; risk communication; Elwyn three-talk | complete ✅ |
| MAXIM-CLIN-G10 | 10 | `10-ETHICS-CONSENT-CAPACITY.md` | Four principles; consent elements; capacity (Appelbaum) vs competence; surrogates/advance directives; confidentiality/justice | complete ✅ |
| MAXIM-CLIN-G11 | 11 | `11-SAFETY-QUALITY-AND-WORKFLOW.md` | Patient safety (Swiss-cheese, just culture, RCA), quality (Donabedian SPO, PDSA, Triple/Quadruple Aim), workflow. Split Part 1/Part 2 if > ~32k tokens | complete ✅ |

All twelve guides are authored (Pulse 04); `03` and `08` were the two gate-passed Pulse-03
prototypes that established the pattern. The full-module adversarial review and
guide-specific Silver-tier rubric evidence are complete under
`panels/clinical-full-r1/`.

**Alternate 10-guide "lean" variant** (merge 01+02, fold 06 into 05) was **considered
and rejected** — it dilutes the two highest-value, most-distinctive guides (reasoning
and test interpretation). Primary recommendation is **12**.

## Ownership / Defer Contract

**Uniquely owns:** clinical reasoning process (01, 02); diagnostic decision theory
(03); evidence appraisal & guideline reasoning (04); care architecture — acute/chronic,
transitions, specialty interfaces, care levels (05, 07, 08); multimorbidity /
deprescribing reasoning (06); individual prevention/screening SDM (09); applied
clinical ethics/consent/capacity (10); patient safety, QI, diagnostic safety, workflow
(11).

**Defers to** (name by reference, never re-derive): `disease/` (mechanisms, catalogs,
natural history, R₀); `human-biology/` (anatomy/physiology, homeostasis); `medicine/`
(drug classes; diagnostics/imaging catalog incl. `medicine/10:~460–600`);
`pharmacology/` (receptor theory, ADME/PK/PD, interactions, pharmacogenomics);
`public-health/` (population epi methods, surveillance, screening *programs*,
health-system typology/financing, policy, DALYs/QALYs, population prevention);
`psychology/` (DSM-5, psychotherapy; HPA/allostatic load); `nutrition/`;
`immunology/`; `pathology/` (planned — tissue/cell mechanism, histopathology,
lab-medicine result generation); `ethics/` (normative theory);
`biomedical-engineering/` (device engineering).

**Three-way lab/diagnostic-interpretation split (ratify with pathology authoring):**
`pathology/` = why the result is what it is → `medicine/10` = the catalog & reference
ranges → `clinical-medicine/03` = how a clinician updates belief and decides to act.

## Non-Advice Contract (mandatory review gate)

Module-level disclaimer at the top of `00-OVERVIEW` and embedded/referenced by every
guide: educational reference on *how clinicians reason and how care is organized*;
**not** medical advice, diagnosis, treatment/dosing/procedure/emergency instructions,
or a substitute for a licensed clinician. Per-guide one-line banner under each title.
Author rules: (1) third-person descriptive, never second-person imperative; (2) no
doses/titration/routes; (3) no step-by-step procedures; (4) acute prioritization as
conceptual schema only (no CPR/self-treatment); (5) screening as *reasoning*, thresholds
attributed and dated; (6) capacity as *how clinicians assess*, not a reader tool; (7)
every numeric threshold labeled illustrative/as-of-date and attributed; (8)
`expert-skeptic` carries an explicit **advice-creep** checklist — any imperative-mood
treatment/emergency instruction is a **BLOCK**.

## Bias / Geographic Limitations

- **MAXIM-CLIN-20** — Authoritative frameworks are Anglo-American-centric (ACGME/AAMC/
  USPSTF/Beers/IHI US; NICE/GRADE UK/intl). Thresholds/screening ages differ by country/
  body — attribute and date; never universalize one nation's cutoff.
- **MAXIM-CLIN-21** — The evidence base skews to high-income, adult, historically male/
  white trial populations (the "70-kg male" default) — external-validity limits guide 04
  must foreground; clinical decision rules may not transfer across populations.
- **MAXIM-CLIN-22** — Care-architecture guides (05, 07, 08, 11) assume a resourced system
  (EHRs, labs, imaging, specialist access); low-resource settings differ materially — flag
  in each.
- **MAXIM-CLIN-23** — Four-principles ethics is Western-liberal and autonomy-weighted; many
  cultures weight family/community differently — guide 10 must note, not universalize.
- **MAXIM-CLIN-24** — Drug metabolism/response varies by ancestry (pharmacogenomics) —
  noted, deferred to `pharmacology/`.

## Quality Risks (with mitigations)

| ID | Risk | Severity | Mitigation |
|---|---|---|---|
| QR-1 | Advice creep (diagnosis/treatment/emergency instructions) | Highest | Non-advice contract; expert-skeptic advice-creep checklist; imperative treatment/ER instruction = BLOCK |
| QR-2 | Duplication of `medicine/10` diagnostic reasoning | High | 03 owns decision theory at depth; **resolved** — the boundary is now **bidirectional** (forward cross-ref from 03 since Pulse 03 + minimal reverse pointer `medicine/10 §11` → 03 added in Pulse 04), decision-theory-vs-catalog with deliberately layered treatments, not a duplication to reconcile |
| QR-3 | Disease-catalog creep in 02/05/08 | High | Examples-as-illustration; hard defer to `disease/`; 08 is an interface catalog |
| QR-4 | Drug-list creep in 06 | Med | Mechanism/class by reference only; no dosing |
| QR-5 | Staleness of screening ages/cutoffs/Beers | Med-High | Teach reasoning + where current guidance lives; numbers as attributed/dated illustrations |
| QR-6 | US-centrism | Med | Comparative framing; attribute every recommendation to body/nation/date |
| QR-7 | False precision in Bayesian worked examples | Med | Label probabilities illustrative; show sensitivity to assumptions |
| QR-8 | `pathology/` boundary churn (concurrent) | Med | Lock the three-way lab split before either module drafts lab content |
| QR-9 | "Soft outline" failure (platitudes not depth) | High | Anchor every guide in a concrete formalism with multi-system worked examples; match chemistry depth bar |
| QR-10 | Guide 11 over-length | Low-Med | Pre-plan Part 1/Part 2 split per 32k convention |

## Adopt / Prototype / Defer

**ADOPT:** the 12-guide reasoning-and-care-architecture manifest; the reusable-patterns
(not per-organ) decision (MAXIM-CLIN-19); the ownership/defer table + three-way lab
split; the non-advice contract as a hard gate; Life Sciences placement; ACGME-6 /
AAMC-13-EPA spine cited in 00.

**PROTOTYPE FIRST (this pulse):** `03-DIAGNOSTIC-TEST-INTERPRETATION` (proves the
`medicine/10` overlap resolves as decision-theory-vs-catalog and hits the quantitative
depth bar) and `08-SPECIALTY-INTERFACES` (proves "interface catalog, not disease
catalog" holds without leaking into `disease/`). Run both through a single-round
`maxim-review` (`expert-skeptic` + `index-weaver`) before authoring 01–02, 04–07, 09–11.

**DEFER / OUT OF SCOPE:** per-organ-system specialty guides (duplication by design);
renaming/rescoping `medicine/` (forbidden this wave — a single **minimal reverse
cross-reference** in `medicine/10 §11` → `03` was the only `medicine/` edit, added in
Pulse 04, and completed the bidirectional boundary; trimming `medicine/10`'s reasoning
section to a bare pointer remains out of scope and unnecessary, since the two treatments
are deliberately layered); a dedicated procedures/skills guide (would invite how-to
instructions — protect the non-advice contract).

## Gaps & Uncertainties (carry-forward)

- **Pathology plan not yet written.** The three-way lab split is *proposed* coordination
  to be ratified when `pathology/` architecture is defined (Pulse 05); no pathology
  directory/STATUS exists yet.
- **Section placement inferred, not decreed.** Life Sciences is strongly implied
  (MAXIM-CLIN-05; chemistry precedent) but not explicitly assigned in wave docs; confirm
  against `.mkdocs/mkdocs.yml` during integration. *(Resolved in Pulse 04: integrated into
  the Life Sciences nav in `.mkdocs/mkdocs.yml`, `sections/life-sciences.md`, and `TRACKER.md`.)*
- **External figures from search summaries, not primary PDFs.** Re-verify specific numbers
  (To Err Is Human 44k–98k estimate; USPSTF ages; exact LR cutoffs) against primary
  sources during authoring, per the wave numbers/names check.
- **Frontmatter/id for a hyphenated module unverified in the pipeline.** By convention
  `id: maxim:clinical-medicine:<slug>`, `module: clinical-medicine`; confirm the
  source-backfill `--module-id clinical-medicine` resolves during Pulse-04 integration.
  *(Resolved in Pulse 04: `--module-id clinical-medicine` resolves and the source-corpus
  regenerated/validated cleanly.)*

**Post-authoring carry-forward:** Pulse 05 should ratify the
pathology/clinical-medicine/medicine lab split before pathology's lab-result content
is authored. The remaining primary-source and guideline-freshness checks are ongoing
maintenance concerns, not blockers to the completed clinical-medicine module.
