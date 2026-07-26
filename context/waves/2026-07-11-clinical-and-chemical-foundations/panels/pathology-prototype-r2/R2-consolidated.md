# Pathology Prototype R2 — Consolidated (strict re-review)

> **Historical point-in-time prototype panel.** Pending-sign-off and deferred-work claims
> below are preserved as R2 evidence and superseded by the 2026-07-12 full-module final PASS;
> Pulse 05 is DONE.

> **Prototype-round panel (Pulse 05), round R2 — strict re-review. Status: REPAIRED — held
> IN REVIEW.** This consolidates the `expert-skeptic` (`R2-expert-skeptic.md`) and
> `reference-editor` (`R2-reference-editor.md`) lenses over the two boundary prototypes
> `pathology/08-LABORATORY-MEDICINE` and
> `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING` after the R1 repairs. R1 removed
> the gross boundary/metrology defects; this strict re-review closes the remaining
> finer-grained findings. As with R1, **final sign-off is not granted** — Pulse 05 stays IN
> REVIEW pending a final strict sign-off gate.

## Decision

**REPAIRED — no unresolved BLOCK or WARN after the R2 pass; Pulse 05 remains IN REVIEW.**
The R1 repairs hold, but the strict re-review found residual precision/honesty defects: a
unit-mixed total-error expression, an over-extended within-subject change value recommended
for cross-lab comparison, a spectrum/prevalence conflation in the ancillary-evidence weight,
an over-actionable margin claim (a clear margin implying proof of complete excision), a
cytology example that flattened *tissue* architecture with *cell-group* cytoarchitecture, an
under-specified `09`/`11` scaling gate, and prototype frontmatter asserting backfill/git-history
artifacts that do not exist. Every finding is repaired in `08`, `10`, `PATHOLOGY-
ARCHITECTURE.md`, `STATUS.md`, the pulse record, and this panel. No `medicine/`,
`clinical-medicine/`, `sections/`, `.mkdocs/`, or `TRACKER.md` edits; no source backfill; no
commit/push.

## Repair Summary

| Area | Result |
|---|---|
| Total error (08 §2) | Split into **matched-unit** formulas: absolute `TEcalc_abs = \|bias_abs\| + z·SD_abs` vs `TEa_abs`; percent `TEcalc_% = \|bias_%\| + z·CV_%` vs `TEa_%`. Never combines an absolute bias with a percentage CV. Sigma uses matching percentage terms `σ = (TEa_% − \|bias_%\|)/CV_%`. One-sided `z ≈ 1.65` stated (two-sided `z ≈ 1.96` noted). Table rows + MAXIM-PATH-23 aligned. |
| Reference Change Value (08 §6, Task 2, Confusions) | **Reserved for serial within-person change on the same/analytically comparable method.** Cross-hospital/method RCV recommendation **removed**; cross-lab reconciliation routed to method bias, measurement uncertainty, commutability, calibration traceability, and method-comparison evidence (standardization/harmonization, Deming/Passing–Bablok, Bland–Altman). "RCV does not bridge methods." |
| Diagnostic evidence (10 §4) | **Spectrum-dependent Sn/Sp/LR split from prevalence-dependent PPV/NPV/posterior.** Explicit: **prevalence does not change Sn/Sp/LR**; it drives predictive value/posterior only. Posterior math deferred to `clinical-medicine/03`. Gate-2 bullet, two-gate ASCII, and post-table paragraph aligned. |
| Margins (10 §6, §10, Task 4, Confusions) | Margin status = **tumor presence/absence/distance at the examined inked specimen margins**; **evidence about, not proof of, complete excision** (sampled planes of the inked surface, not the whole resection bed). §6 bullet + axis table, report payload (field/Comment/note), Task 4, and the Confusion Point reworded. |
| Thyroid FNA (10 §3) | Distinguishes **unavailable tissue-level architecture/invasion** (capsule/stroma/invasion/growth pattern) from **diagnostically meaningful cytologic group arrangements** (microfollicular groups, papillary fragments, syncytial sheets). Cytoarchitecture is available; the two must not be conflated. |
| Scaling contracts (architecture, STATUS) | `09`/`11` mini-contracts expanded to a **two-stage gate**: Stage 1 on **representative high-risk draft sections** (`09` grossing/orientation + staining/frozen/cytology; `11` governance/accreditation + the total-testing-process `08`↔`11` seam) before authoring; Stage 2 a **completed-guide whole-procedure/whole-seam review** before sign-off. MAXIM-PATH-19/24, Scaling Mini-Contracts, QR-12, STATUS rows/paragraph updated. |
| Prototype metadata (08/10 frontmatter, architecture) | Generated `proof-backfill`/`git-history` backsource IDs **removed**; frontmatter set to the truthful pre-backfill state `status: prototype` / `source_custody: needs-source` / `backsource_ids: []`. Forward-compatible with the deferred backfill. Recorded as **MAXIM-PATH-25** + **QR-14**; Gaps notes updated. |

## Findings ledger

| ID | Lens | Severity | Subject |
|---|---|---|---|
| ES2-01 | expert-skeptic | BLOCK | Total error still mixed absolute + relative units (08 §2) |
| ES2-02 | expert-skeptic | BLOCK | RCV recommended for cross-hospital/method comparison (08 §6, Task 2) |
| ES2-03 | expert-skeptic | BLOCK | Sn/Sp/LR tied to prevalence — spectrum/prevalence conflation (10 §4) |
| ES2-04 | expert-skeptic | WARN | Clear margin implied proof of complete excision (10 §6/§10) |
| RE2-01 | reference-editor | WARN | FNA "architecture unavailable" flattened cytologic group arrangements (10 §3) |
| RE2-02 | reference-editor | WARN | 09/11 scaling gate under-specified (no representative sections / no whole-guide gate) |
| RE2-03 | reference-editor | BLOCK | Prototype frontmatter claimed nonexistent backfill/git-history artifacts |
| RE2-04 | reference-editor | NOTE | R2 recorded; Pulse 05 kept IN REVIEW |

## Validation

- Focused PROOF (MAXIM `proof.toml`) via the `tools-infra/proof` Cargo manifest, scoped to
  the two prototype guides, re-run after the R2 repairs: **2 files checked, 0 errors, 0
  warnings**.
- `git diff --check`: clean (no whitespace/conflict markers). The pathology module is still
  **untracked** (not integrated), so PROOF was run against the two guides explicitly.
- Structural spot-check: each guide has a single H1, a landscape diagram, a Decision Cheat
  Sheet, balanced code fences, no `@editor` tags, and **0** `you/your`.
- Source backfill (PROOF sources / CROP / PEBBLE / FLETCH) **not** run — this is a prototype
  boundary re-review, and the frontmatter is at the truthful pre-backfill state. `medicine/`,
  `clinical-medicine/`, `sections/`, `.mkdocs/`, and `TRACKER.md` untouched. No commit or push.

## Gate status

The R2 findings — the finer-grained metrology/boundary/taxonomy/metadata defects that survived
R1 — are repaired with no unresolved BLOCK or WARN. Consistent with the pulse scope, **final
strict prototype sign-off is not granted in this round**; the next step is the final strict
sign-off gate and, on sign-off, the deferred full authoring — including the `09`/`11`
two-stage scaling reviews — integration, reciprocal sibling wiring, and source-corpus
regeneration (which will promote the prototype frontmatter to real source-custody). **Pulse 05
is held IN REVIEW.**
