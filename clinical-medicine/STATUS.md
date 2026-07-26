# clinical-medicine/ — Status

**12 of 12 guides authored · Module COMPLETE · Pulse 04 DONE**

> All twelve guides are authored at full peer-level depth. Guides `03` and `08` were
> written first as prototypes (Pulse 03) to de-risk the two hardest boundaries (the
> `medicine/10` diagnostic-reasoning overlap, and the "specialty as interface, not
> disease catalog" decision); the passed prototype pattern then governed the remaining
> ten guides, authored in Pulse 04. The module is now **integrated** into
> `sections/life-sciences.md`, `.mkdocs/mkdocs.yml`, and `TRACKER.md`, and regenerated
> into the source-corpus pipeline (PROOF/CROP/PEBBLE/FLETCH). A **minimal reverse
> cross-reference** now runs from `medicine/10 §11` back to `clinical-medicine/03`
> (the forward pointer from `03` was already present), so the overlap is resolved
> **bidirectionally** as decision-theory-vs-catalog. Pulse 04 is **DONE**: the
> full-module adversarial panel and guide-specific rubric review are complete, all
> BLOCK/WARN findings are repaired, and the module's honest final tier is **Silver**
> pending optional future Da Vinci/Gold promotion work. See
> the architecture record at
> `context/waves/2026-07-11-clinical-and-chemical-foundations/artifacts/CLINICAL-MEDICINE-ARCHITECTURE.md`
> (findings MAXIM-CLIN-01 … MAXIM-CLIN-24) and pulses
> `03+clinical-medicine-architecture.md` (DONE) and `04+clinical-medicine-authoring.md`.

## Scope in one line

`clinical-medicine/` is the **reasoning-and-care-architecture apex** of the Life
Sciences vertical (molecular → cellular → organismal → population → **clinical**). It
owns the *transferable cognitive and system architecture of medicine* — clinical
reasoning, diagnostic decision theory, evidence appraisal, and care-process design —
**not** disease catalogs, drug lists, physiology, or population-health methods. It is
an **educational reference, never medical advice**.

## Guide Manifest (12 guides: 00 + 11)

| # | File | Uniquely owns (at peer depth) | Status |
|---|------|-------------------------------|--------|
| 00 | `00-OVERVIEW.md` | Discipline map; ACGME-6 / AAMC-13-EPA spine; ownership/boundary table; the module **non-advice contract**; reading order; software-mental-model bridges | ✅ |
| 01 | `01-CLINICAL-ENCOUNTER.md` | History/physical as information architecture; **problem representation**, semantic qualifiers, illness scripts | ✅ |
| 02 | `02-DIFFERENTIAL-DIAGNOSIS.md` | Dual-process reasoning; diagnostic schemas; ranking (likely vs must-not-miss); cognitive bias + debiasing; calibration; NASEM diagnostic-error framing | ✅ |
| 03 | `03-DIAGNOSTIC-TEST-INTERPRETATION.md` | **Diagnostic decision theory** — 2×2 as belief engine, LR/odds Bayes, PPV/NPV prevalence, ROC/AUC limits, **Pauker–Kassirer test/treatment thresholds**, sequential/correlated tests, overtesting/incidentaloma cascades, value of information | ✅ (prototype, gate-passed) |
| 04 | `04-EVIDENCE-BASED-MEDICINE.md` | Sackett three-circle; PICO; evidence hierarchy; **GRADE**; NNT/ARR/RRR; external validity; surrogate endpoints; applying population evidence to the individual | ✅ |
| 05 | `05-ACUTE-AND-CHRONIC-CARE.md` | Two care logics: acute/undifferentiated prioritization (conceptual only) vs chronic/longitudinal (trajectories, Chronic Care Model) | ✅ |
| 06 | `06-MULTIMORBIDITY-AND-GERIATRICS.md` | Competing risks; treatment burden; guideline collision; **polypharmacy / prescribing cascade / deprescribing reasoning**; geriatric 5Ms; frailty; time-to-benefit | ✅ |
| 07 | `07-CARE-TRANSITIONS.md` | Handoffs as information transfer (I-PASS, SBAR); med reconciliation; discharge; continuity types; the problem list as shared state; closed loops | ✅ |
| 08 | `08-SPECIALTY-INTERFACES.md` | Specialty map **as a service/interface catalog** — generalist/specialist labor split, care levels, consult-question quality, referral/comanagement ownership, closed-loop follow-up, practice variation, multi-specialty conflict resolution | ✅ (prototype, gate-passed) |
| 09 | `09-PREVENTION-AND-SCREENING.md` | **Individual-level** prevention/screening as shared decision; overdiagnosis, lead-time/length-time bias; natural frequencies; Elwyn three-talk SDM | ✅ |
| 10 | `10-ETHICS-CONSENT-CAPACITY.md` | Applied clinical bioethics: four principles; consent elements; **decision-making capacity** (Appelbaum four abilities) vs competence; surrogates/advance directives; confidentiality; justice; cultural variation | ✅ |
| 11 | `11-SAFETY-QUALITY-AND-WORKFLOW.md` | Systems-based practice: patient safety (Swiss-cheese, just culture, RCA, HRO), quality (Donabedian SPO, PDSA, Triple/Quadruple Aim), diagnostic safety, EHR order/result loops, team roles | ✅ |

Architecture IDs for each guide (MAXIM-CLIN-G00 … G11 in the wave architecture record)
and the manifest above were **ratified in Pulse 03**; a 10-guide "lean" variant was
considered and rejected (see the architecture record §Manifest).

## Boundary Contracts (non-duplication)

This module names mechanisms/catalogs by reference and never re-derives them.

| Defers to | For |
|---|---|
| `medicine/10-DIAGNOSTICS-IMAGING` | The test **catalog**, reference ranges, analyte time-courses, and X-ray/CT/MRI/US/PET **physics**. Its `§11` diagnostic-reasoning section overlaps guide 03; the overlap is now bridged **both ways** — a forward pointer from `03` and a **minimal reverse** pointer from `medicine/10 §11` → `clinical-medicine/03` — with `03` owning the decision theory at depth and `medicine/10` owning the catalog/physics. |
| `disease/` | Disease mechanisms, catalogs, natural history by category; epidemiology basics (R₀) |
| `human-biology/` | Organ-system anatomy & physiology, homeostasis |
| `medicine/`, `pharmacology/` | Drug classes, receptor theory, ADME/PK/PD, interactions, pharmacogenomics (no dosing, ever) |
| `public-health/` | Population epidemiology methods, surveillance, screening **programs**, health-system typology/financing, DALYs/QALYs |
| `psychology/`, `nutrition/`, `immunology/` | DSM-5/psychotherapy, dietary science, immune mechanisms |
| `pathology/` | Tissue/cell mechanism behind a result; histopathology; lab-medicine result generation |
| `ethics/` | Normative ethical theory (deontology/consequentialism/virtue) |
| `law/` | Statute/precedent, legal competence adjudication, jurisdictional rules |

**Three-way lab/diagnostic-interpretation split (ratified in Pathology Pulse 05):**
`pathology/` = *why the result is what it is* → `medicine/10` = *the catalog & reference
ranges* → `clinical-medicine/03` = *how a clinician updates belief and decides to act*.
The pathology module is authored and reciprocally wired to this boundary.

## Non-Advice Contract (hard review gate)

1. Third-person descriptive voice ("a clinician weighs…"), never second-person
   imperative ("take…", "you should…").
2. No drug doses/titration/routes as instructions; drugs named at mechanism/class
   level by reference only.
3. No step-by-step procedure/technique instructions.
4. Acute-care content (guide 05) presents prioritization **schemas** as conceptual
   architecture only — no self-treatment/CPR/dosing/first-aid.
5. Screening content (guide 09) presents *how the decision is reasoned*, not "get
   screened at age X"; every threshold attributed to a named body **and dated**.
6. Capacity (guide 10) describes *how clinicians assess capacity*, not a reader tool;
   ethics content is educational process only, not legal advice.
7. Every numeric threshold labeled **illustrative / as-of-date** and attributed.
8. `expert-skeptic` review carries an explicit **advice-creep** checklist; any
   imperative-mood treatment/emergency instruction is a **BLOCK**.

## Placement (wired)

Life Sciences section, as the clinical apex of the molecular→clinical vertical.
Integrated in `sections/life-sciences.md` (Directories table + count), `.mkdocs/mkdocs.yml`
(Life Sciences nav), and `TRACKER.md` (Summary Dashboard row + counts). Source-corpus
artifacts regenerated for module id `clinical-medicine` (PROOF sources/sidecars, CROP
views, PEBBLE packs, FLETCH registry); source custody remains `partial` (first-pass
publication) per the backfill contract.

## Pulse 04 review status

Guides authored and PROOF-clean; module integrated and source-corpus regenerated. The
**full-module adversarial panel** (`expert-skeptic` advice-creep + `reference-editor`
across all 12 guides) has now **run and its conservative findings are repaired**, recorded
under `panels/clinical-full-r1/` (expert-skeptic, reference-editor, consolidated,
guide-specific rubric). Pulse 04 is **DONE** with no unresolved BLOCK/WARN findings.
All guides are classified **Silver**; Da Vinci pinning and any future Gold promotion
are separate optional work. Pulse 03 is **DONE**.
