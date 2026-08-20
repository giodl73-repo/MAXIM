# Pathology Prototype R1 — Consolidated

> **Historical point-in-time prototype panel.** Pending-sign-off and deferred-work claims
> below are preserved as R1 evidence and superseded by the 2026-07-12 full-module final PASS;
> Pulse 05 is DONE.

> **Prototype-round panel (Pulse 05), status: REPAIRED — held IN REVIEW.** This consolidates
> the `expert-skeptic` (`R1-expert-skeptic.md`) and `reference-editor`
> (`R1-reference-editor.md`) lenses over the two boundary prototypes
> `pathology/08-LABORATORY-MEDICINE` and
> `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING`. Unlike the clinical prototype
> round (which received final sign-off), **this round is deliberately kept IN REVIEW**: the
> R1 findings are repaired, but final prototype sign-off, full authoring, integration,
> reciprocal sibling wiring, and source-corpus backfill remain gated.

## Decision

**REPAIRED — no unresolved BLOCK or WARN after the R1 pass; Pulse 05 remains IN REVIEW.**
The prototypes hit the metrology and diagnostic-method depth bar, but the first pass carried
a conservative superset of boundary defects: metrology-honesty errors (total-error
conflation, a percentage-vs-unit reference-change comparison, a wrong detection-limit
definition, a universal error-share claim), a false universal certainty ladder, an
analytical-vs-diagnostic conflation, an over-actionable margin claim, pervasive
advice-/procedure-creep, a narrated (not rendered) report case, a flat diagnostic taxonomy,
over-scoped staging/synoptic claims, missing resource-constrained case branches, an
"all-remaining-guides-lower-risk" architecture stance with no scaling contract for `09`/`11`,
and citations called authoritative while unverified. Every finding is repaired in `08`,
`10`, `PATHOLOGY-ARCHITECTURE.md`, `STATUS.md`, and the pulse record. No `medicine/`,
`clinical-medicine/`, `sections/`, `.mkdocs/`, or `TRACKER.md` edits; no source backfill; no
commit/push.

## Repair Summary

| Area | Result |
|---|---|
| Total error (08 §2) | `TEcalc = \|bias\| + z·CV` (calculated, in analyte units; `z ≈ 1.65` one-sided ~95%) separated from **allowable** `TEa` (a spec from biological variation / EQA / clinical need); acceptance `TEcalc ≤ TEa`; sigma reframed as the gap. Table split; cheat sheet aligned. |
| Reference Change Value (08 §6, Task 4) | RCV stated as a **percentage** threshold, compared to the **relative** change. Worked case given explicit `CV_a=5%`, `CV_i=12%`, `z≈1.96` (two-sided) → `RCV≈36%` vs observed `31%` → within noise; log-scale refinement noted. No unit mismatch. |
| Limit of Blank (08 §3) | LoB redefined as `mean_blank + 1.645·SD_blank` — the one-sided **95th percentile of blank results**, in concentration units — not the highest raw signal. LoD/LoQ ordering "by construction." |
| Preanalytic error share (08 Big Picture) | Universal "~60–70%" replaced by an **attributed, bounded, illustrative** range ("roughly one-half to two-thirds," Carraro & Plebani) with a setting-dependence caveat and a `*` note. |
| Advice-/procedure-creep (08, 10) | Potassium value labeled fictional; redraw recast to "provisional pending recollection" (institutional model state). All reader-directed second-person/imperative voice recast to descriptive model states; **0** `you/your` remain in either guide. |
| Certainty (10 §5) | Universal ladder mapped to posteriors removed. Replaced by **four independent dimensions** — material adequacy, positive assertion strength, negative-finding scope, residual uncertainty — on **locally governed lexicons / named category systems**, explicitly not a universal probability. Pipeline node, §11, Task 3, cheat sheet, confusions aligned. |
| Analytical vs diagnostic (10 §4) | **Two-gate** model: Gate 1 analytical validity (controls/antigen detectability/fixation), Gate 2 population/context-dependent Sn/Sp/LR **contribution**; belief-update deferred to `clinical-medicine/03`. Table + Task 2 aligned. |
| Report payload (10 §10) | Narrated case replaced by an **actual fictional report**: v1 (diagnosis line, synoptic fields, grade/stage/margin with context limits, comment/limitation, critical-communication record) and a visible **amendment v2** (prior retained, reason, deltas, re-notification), with an addendum contrast. |
| Margin claim (10 §10) | "<1 mm clinically actionable" removed; the 0.8 mm clearance is a **measured boundary condition** whose significance is entity-/protocol-/context-dependent, owned downstream — not a generic actionable threshold. |
| Pattern taxonomy (10 §3) | Single-axis list rebuilt as a **7-dimension parse matrix** (adequacy, compartment, architecture, cytology, stromal/background, hematolymphoid, sampling/discordance) with two contrasting specimen demonstrations (thyroid FNA vs lymph-node), method not catalog. |
| Report scope (10 §6/§7) | Pathologic `pT`/`pN`/`pM` **elements** distinguished from the integrated **overall stage group** (with non-anatomic factors, assigned downstream); synoptic completeness scoped as **protocol-governed and heterogeneous**; **no universal "cannot sign"** rule. |
| Resource branches (08 Task 1, 10 §10) | Each guide adds an alternate resource-constrained branch: unavailable test changes uncertainty/release/report wording/referral **without** changing the framework. |
| Scaling mini-contracts (architecture, STATUS) | MAXIM-PATH-19 amended ("not all remaining guides low-risk"); **MAXIM-PATH-24** + a *Scaling Mini-Contracts* section pin `09` (purpose/failure-mode only, no runnable steps) and `11` (cross-process QC/error/governance vs `08`'s local-only concepts), each with a **focused mini-review before bulk authoring**; QR-12 added; STATUS rows/notes updated. |
| Citations (architecture) | "External framework grounding (authoritative)" de-authoritized; **MAXIM-PATH-23** qualifies GUM/ISO, CLSI EP17/AUTO10-A→AUTO15, UICC/AJCC TNM elements-vs-stage-group, CAP/ICCR/RCPath synoptic, Lundberg 1981; `08` cites AUTO10-A→AUTO15; QR-13 tracks residual verification. |

## Findings ledger

| ID | Lens | Severity | Subject |
|---|---|---|---|
| ES-01 | expert-skeptic | BLOCK | TEcalc vs TEa conflation (08 §2) |
| ES-02 | expert-skeptic | BLOCK | RCV percentage-vs-unit mismatch (08 Task 4) |
| ES-03 | expert-skeptic | BLOCK | LoB = highest raw signal (08 §3) |
| ES-04 | expert-skeptic | WARN | Universal "~60–70%" preanalytic share (08) |
| ES-05 | expert-skeptic | BLOCK | Advice-/procedure-creep + second-person voice (08, 10) |
| ES-06 | expert-skeptic | BLOCK | Universal certainty ladder → posteriors (10 §5) |
| ES-07 | expert-skeptic | BLOCK | Analytical validity vs diagnostic evidence (10 §4) |
| ES-08 | expert-skeptic | WARN | "<1 mm margin clinically actionable" (10 §10) |
| ES-09 | expert-skeptic | WARN | Citations called authoritative, unverified (architecture) |
| RE-01 | reference-editor | BLOCK | Narrated case, no report payload / versioning (10 §10) |
| RE-02 | reference-editor | WARN | Single-axis pattern taxonomy (10 §3) |
| RE-03 | reference-editor | BLOCK | Staging / synoptic / "cannot sign" overreach (10 §6/§7) |
| RE-04 | reference-editor | WARN | No resource-constrained case branch (08, 10) |
| RE-05 | reference-editor | BLOCK | "All remaining guides lower-risk"; no 09/11 scaling contract |
| RE-06 | reference-editor | NOTE | R1 recorded; Pulse 05 kept IN REVIEW |

## Validation

- Focused PROOF (MAXIM `proof.toml`) via the `tools-infra/proof` Cargo manifest, scoped to
  the two prototype guides, re-run after the R1 repairs: **2 files checked, 0 errors, 0
  warnings**.
- `git diff --check`: clean (no whitespace/conflict markers). The pathology module is still
  **untracked** (not integrated), so PROOF was run against the two guides explicitly.
- Structural spot-check: each guide has a single H1, a landscape diagram, a Decision Cheat
  Sheet, balanced code fences, no `@editor` tags, and **0** `you/your`.
- Source backfill (PROOF sources / MDCROP / MDPORT / FLETCH) **not** run — this is a prototype
  boundary review. `medicine/`, `clinical-medicine/`, `sections/`, `.mkdocs/`, and
  `TRACKER.md` untouched. No commit or push.

## Gate status

The R1 findings — a conservative superset of the expected expert-skeptic + reference-editor
prototype defects — are repaired with no unresolved BLOCK or WARN. Consistent with the pulse
scope, **final prototype sign-off is not granted in this round**; the next step is a strict
re-review (R2) and, on sign-off, the deferred full authoring — including the `09`/`11`
scaling mini-reviews — integration, reciprocal sibling wiring, and source-corpus
regeneration. **Pulse 05 is held IN REVIEW.**
