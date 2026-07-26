---
wave: clinical-and-chemical-foundations
pulse: 04
date: 2026-07-12
status: done
depends_on: [03]
governing_roles: [reference-editor, expert-skeptic, index-weaver, ascii-cartographer]
---

# Pulse 04 - Clinical Medicine Full Authoring and Integration

## Mission

Author the remaining ten `clinical-medicine/` guides at full peer-level MAXIM depth using
the **ratified prototype pattern** established by guides `03` and `08` (which passed the
strict Pulse-03 boundary gate under `panels/clinical-prototype-r1/`), then integrate the
completed module and regenerate its source-corpus artifacts. The two prototypes define the
quality/safety pattern every new guide follows: descriptive third-person model voice, the
module non-advice banner, an ownership/defer header, a conceptual landscape, layered
formalism with worked *fictional* cases, decision-useful tables, software/systems bridges,
3–5 solved reader tasks, a Decision Cheat Sheet, Common Confusion Points, and
geographic/resource/bias caveats. This pulse completes authoring, integration,
adversarial review, and honest tier assignment.

## Pre-implementation Scout

```powershell
Get-Content CLAUDE.md, clinical-medicine\STATUS.md
Get-Content clinical-medicine\03-DIAGNOSTIC-TEST-INTERPRETATION.md   # passed prototype pattern
Get-Content clinical-medicine\08-SPECIALTY-INTERFACES.md            # passed prototype pattern
Get-Content context\waves\2026-07-11-clinical-and-chemical-foundations\artifacts\CLINICAL-MEDICINE-ARCHITECTURE.md
Get-Content context\waves\2026-07-11-clinical-and-chemical-foundations\panels\clinical-prototype-r1\R1-consolidated.md
Get-Content chemistry\00-OVERVIEW.md, chemistry\STATUS.md          # integration exemplar
# Inspect the reverse-xref target (minimal edit only)
Get-Content medicine\10-DIAGNOSTICS-IMAGING.md | Select-Object -Index (466..561)
```

## Scope Inventory

| Area | Files |
|---|---|
| New guides (10) | `clinical-medicine/00-OVERVIEW.md`, `01-CLINICAL-ENCOUNTER.md`, `02-DIFFERENTIAL-DIAGNOSIS.md`, `04-EVIDENCE-BASED-MEDICINE.md`, `05-ACUTE-AND-CHRONIC-CARE.md`, `06-MULTIMORBIDITY-AND-GERIATRICS.md`, `07-CARE-TRANSITIONS.md`, `09-PREVENTION-AND-SCREENING.md`, `10-ETHICS-CONSENT-CAPACITY.md`, `11-SAFETY-QUALITY-AND-WORKFLOW.md` |
| Prototypes (unchanged) | `03-DIAGNOSTIC-TEST-INTERPRETATION.md`, `08-SPECIALTY-INTERFACES.md` |
| Manifest | `clinical-medicine/STATUS.md` (12/12 complete) |
| Integration | `.mkdocs/mkdocs.yml`, `sections/life-sciences.md`, `TRACKER.md` |
| Minimal reverse xref | `medicine/10-DIAGNOSTICS-IMAGING.md` `§11` → `clinical-medicine/03` (no other `medicine/` change) |
| Source-corpus (regenerated) | `.mdloom/backfill/sources/clinical-medicine/**`, `.mdloom/backfill/modules/clinical-medicine.json`, `.crop/views/maxim-clinical-medicine-*.json`, `.mdport/packs/maxim-clinical-medicine-*.pebble.json`, `.fletch/registries/maxim-clinical-medicine-source-corpus.json` |
| Wave tracking | `WAVE.md` (Pulse 03 → DONE, Pulse 04 → DONE); `pulses/03+...` DONE; this record; `panels/clinical-full-r1/` (full-module review and rubric evidence) |

## Scope Contract (non-duplication)

Unchanged from Pulse 03. `clinical-medicine/` owns the transferable cognitive/system
architecture of medicine, organized around **reusable reasoning patterns, not per-organ
specialties**; it defers disease catalogs to `disease/`, physiology to `human-biology/`,
the diagnostics/imaging catalog + reference ranges + imaging physics to `medicine/`
(incl. `medicine/10`), drug pharmacology to `pharmacology/`, population methods/programs to
`public-health/`, normative ethical theory to `ethics/`, and law to `law/`. The sharpest
overlap (`medicine/10 §11`) is now resolved **both ways**: the forward pointer from `03`
(present since Pulse 03) plus a **minimal reverse** pointer from `medicine/10 §11` → `03`
added in this pulse — decision-theory-at-depth (`03`) vs catalog + physics (`medicine/10`).
The **non-advice contract** is a hard gate on every guide.

## Deliverables

- [x] `00-OVERVIEW.md` — discipline map; ACGME-6 / AAMC-13-EPA spine; ownership/boundary
      table; the module non-advice contract; reading order by background; software bridges.
- [x] `01-CLINICAL-ENCOUNTER.md` — H&P as information architecture; hypothesis-driven
      gathering; problem representation; semantic qualifiers; illness scripts (not exam how-to).
- [x] `02-DIFFERENTIAL-DIAGNOSIS.md` — dual-process; diagnostic schemas; likely vs
      must-not-miss ranking; cognitive bias + debiasing; calibration; NASEM framing.
- [x] `04-EVIDENCE-BASED-MEDICINE.md` — Sackett three-circle; PICO; hierarchy; GRADE;
      ARR/RRR/NNT with baseline-risk dependence; external validity; surrogate endpoints.
- [x] `05-ACUTE-AND-CHRONIC-CARE.md` — acute prioritization as concept only vs chronic
      longitudinal (trajectories, Chronic Care Model); no emergency/self-treatment instructions.
- [x] `06-MULTIMORBIDITY-AND-GERIATRICS.md` — competing risks; treatment burden; guideline
      collision; polypharmacy/prescribing cascades; deprescribing reasoning; 5Ms; frailty;
      time-to-benefit; no dosing or personal treatment.
- [x] `07-CARE-TRANSITIONS.md` — I-PASS/SBAR; medication reconciliation; discharge/continuity;
      problem list as shared state; ownership and closed loops.
- [x] `09-PREVENTION-AND-SCREENING.md` — individual shared decisions; screening harms;
      lead/length-time bias; natural frequencies; three-talk model; thresholds attributed,
      dated, and illustrative; no personal screening advice.
- [x] `10-ETHICS-CONSENT-CAPACITY.md` — four principles; consent; Appelbaum capacity vs
      competence; surrogates; advance directives; confidentiality; justice; cultural
      variation; educational process only.
- [x] `11-SAFETY-QUALITY-AND-WORKFLOW.md` — Swiss cheese; error taxonomy; RCA/just
      culture/HRO; Donabedian SPO; PDSA; diagnostic safety; EHR order/result loops; team roles.
- [x] `STATUS.md` — updated to 12/12 complete; non-advice contract + boundary contracts recorded.
- [x] Minimal reverse cross-reference in `medicine/10 §11` → `clinical-medicine/03` (no other
      `medicine/` rewrite).
- [x] Integration: `.mkdocs/mkdocs.yml` (Life Sciences nav), `sections/life-sciences.md`
      (Directories table + count 19→20), `TRACKER.md` (Summary Dashboard row + 236→237
      directories, ~2,362→~2,374 files).
- [x] Source-backfill with `--validate` for `clinical-medicine` (regenerated
      MDLOOM/CROP/MDPORT/FLETCH) and re-validation for `medicine` (because `medicine/10`
      changed); focused MDLOOM clean; `git diff --check` clean.
- [x] **Full-module adversarial panel and rubric review:**
      `expert-skeptic` advice-creep + `reference-editor` across all 12 guides, recorded under
      `panels/clinical-full-r1/` (expert-skeptic, reference-editor, consolidated). No advice-creep
      BLOCK; the conservative WARN/NOTE findings (resource caveats in 05/07/11; ethics
      disclosure/appreciation hedges; guide-11 voice; guide-09 Jamoulle framing; guide-03 stale
      prototype language; guide-07 independent readability; records reconciliation) are all
      repaired. Guide-specific ten-dimension and reader-task evidence is recorded in
      `R2-gold-rubric.md`; all guides are Silver pending optional future Da Vinci work.

## Non-Advice Contract (hard gate, applied to all ten new guides)

Third-person descriptive voice (never second-person imperative); no drug doses/titration/
routes; no step-by-step procedures; acute content (05) as conceptual prioritization schema
only (no first-aid/CPR/self-treatment); screening (09) as reasoning with every threshold
attributed and dated; capacity (10) as how clinicians assess (not a reader self-test) and
educational process, not legal advice; every numeric threshold labeled illustrative/as-of-date;
Decision Cheat Sheets phrased as "what the model/clinician does". An advice-creep breach is a
BLOCK for the pending panel.

## Validation

Repo-config MDLOOM and the source-backfill helper, run from the MAXIM root:

```powershell
# Source-backfill regenerates MDLOOM/CROP/MDPORT/FLETCH and validates
python .claude\skills\maxim-source-backfill\scripts\module_source_backfill.py `
  --module-dir clinical-medicine --module-id clinical-medicine --validate

# medicine/10 changed, so re-validate medicine (focused MDLOOM)
cargo run --manifest-path ..\..\tools-infra\proof\Cargo.toml -- `
  check medicine\10-DIAGNOSTICS-IMAGING.md --config mdloom.toml

git --no-pager diff --check
```

**Outcome (recorded):** all 12 `clinical-medicine` guides MDLOOM-clean; source-backfill
`--validate` passed (MDLOOM check, CROP inspect `--strict`, FLETCH registry validate, shaft
paths present, `git diff --check`); `medicine/10` re-checked — its only new content is the
minimal reverse cross-reference, and its two remaining MDLOOM warnings (`md_missing_section`
for the numbered "12. Decision Cheat Sheet" heading and an `ascii_unclosed_fence`) are
**pre-existing** in the committed file and untouched by this pulse. The full-module review
repairs (`panels/clinical-full-r1/`) were then re-validated: `clinical-medicine` re-backfilled
(**12/12** round-trip, CROP strict valid, FLETCH 61 entries/0 findings), `medicine` re-backfilled
(**11/11** round-trip), focused MDLOOM **12 files / 0 errors / 0 warnings** on the numbered guides,
`git diff --check` clean. No commit/push performed.

## Status

All ten new guides authored at full depth, `00` map written, `STATUS.md` at 12/12, module
integrated into section/nav/`TRACKER`, minimal `medicine/10` reverse cross-reference added,
and source-corpus regenerated and validated. The full-module adversarial panel and
guide-specific rubric review are complete, all findings are repaired, and Pulse 04
is **DONE**. The module's final tier is **Silver**; optional Da Vinci pinning and Gold
promotion are separate future work.

## Non-Goals

- Do not commit or push (snapshot/pointer updates are a separate TRACKER pulse).
- Do not rename, re-scope, or otherwise rewrite `medicine/` beyond the single minimal reverse
  cross-reference in `§11`.
- Do not author `pathology/` (Pulse 05) or ratify the three-way lab split yet.
- Do not lower the depth bar to introductory-textbook prose or template filling.
- Do not introduce medical-advice framing; the non-advice contract is a hard gate.
