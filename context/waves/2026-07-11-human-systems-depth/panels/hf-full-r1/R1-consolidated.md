# Human-Factors Full-Module R1 — Consolidated

> **Disposition (2026-07-13): REPAIRED — wave remains IN REVIEW pending an independent final
> re-review. No Gold, no registry, no unresolved BLOCK/WARN in source after this pass.** This
> record consolidates the two R1 lenses — `R1-expert-skeptic.md` (overclaim, quantitative/model
> rigor, safety floor, boundary accuracy) and `R1-reference-editor.md` (citations, standards,
> structure, cross-references, accessibility reach, trackers, MDLOOM-artifact truth, records) — over
> the **whole** authored `human-factors/` module (all twelve guides `00`–`11`) and its records,
> run after authoring, integration, and source-corpus backfill. This is the conservative
> full-module adversarial pass named by Pulse 04's Definition-of-Done closure gate 12. Every finding
> is **repaired** in the guides or records; `R2-gold-rubric.md` scores every guide **Silver** and
> records **no registry insertion**. Because this panel both **raised and repaired** the findings,
> it cannot self-ratify — the wave stays **IN REVIEW** until an independent reviewer re-derives the
> passes. No `commit`/`push`.

## Decision

**REPAIRED — IN REVIEW pending final re-review; Silver; no registry; no unresolved BLOCK or WARN in
source.** The conservative pass returned a superset of defects concentrated in **quantitative/model
correctness** (`05` HRA error-factor/ceiling/SPAR-H-trigger; `07` automation L1-takeover and model
structure; `10` overlapping coverage strata), an **overclaim/prescription** defect (`09` domain
"same fix"/checklist/handoff/second-check), a **determinate-without-triangulation** defect (`11`
reporting culture), a **barrier-ranking + dust-advice** defect (`08`), plus reference-editor defects
in **cross-reference navigability, the accessibility contract's honest reach (`01`/`03`/`05`/`09`/
`10`), the trackers/totals, the Leveson/RNLE citations and untracked whitespace, the MDLOOM-artifact
truth, and the missing panel/DoD records**. All are repaired in the guides and records; the
full-module MDLOOM/backfill validation is clean. No Da Vinci / Gold work is claimed.

## Repair summary

| Area | Result |
|---|---|
| `05` HRA — EF convention, bounded-probability ceiling, SPAR-H trigger (ES-01) | EF defined as `sqrt(P95/P05)`; `median×EF = 1.45` shown inadmissible for a HEP; **bounded** band `~[0.06, 0.8]` via truncated-lognormal/logit-normal (the 0.8 is the model's, not EF's); SPAR-H adjustment applied **only at ≥3 negative PSFs** (sweep recomputed: ×1 → 0.04, ×0.1 → 0.004, plain product); worked case + tasks 1–3 aligned. |
| `08` shared HEP value (ES-01a) | Bow-tie pass + reader task 2 now carry the corrected bounded `~0.06–0.8`; human-term propagation `~6e-5 to ~8e-4 /yr`. |
| `07` automation — model + L1 (ES-02) | Redesigned `E(L)=(1−p)·W(L)+p·C(L)` with **common** off-normal `p` and **level-specific** conditional `C(L)`; **L1 carries no takeover term**; sweep recomputed (`W=[8,5,3,1]`, `C=[3,12,30,60]`): optimum **slides L4→L3→L2→L1** (p=0.01/0.08/0.15/0.30) — **no winner**; task 2, case, note, cheat aligned. |
| `10` methods — coverage frame (ES-03) | Overlapping 3-way "strata" replaced by **orthogonal crossed factors** E×P×T×C = **16 cells** (+ requirements-coverage-matrix alternative); convenience = **1/16 ≈ 6%**, designed = **16/16**; case + task 2 recomputed. |
| `09` domain — candidate mechanisms only (ES-04) | "The fix is the same," "paper checklist," "structured verbal handoff," and "a second check" reframed to **candidate mechanisms / evidence questions**; **intervention selection & acceptance deferred to the domain owner** under its own review. |
| `08` barriers + dust (ES-05) | Hollnagel taxonomy retitled **types, not a universal strength ranking** (reliability must be assessed, not read off the category); **common-cause decomposition made explicit**; the combustible-dust example reframed to **hypotheses under a domain hazard review / MoC** — no actionable barrier advice. |
| `11` reporting culture — triangulation (RE-01) | Reporting-rate comparison declared **indeterminate without triangulation**; additional evidence listed (exposure/opportunity, definitions, severity, near-miss ratio, reporting climate, audit); §4 box, case, task 1, cheat aligned. |
| Cross-references (RE-03) | Meaningful **clickable Markdown links** added across all twelve guides (intro deferrals + key cheat routes), no link spam. |
| Accessibility ≥2-channel (RE-04) | Concise explicit cross-cutting note added to `01`,`03`,`05`,`09`,`10`, each anchored + pointing to `06` §3 — the module-wide claim is now true. |
| Trackers/totals (RE-05) | Complete stays **239** (HCI counted; HF separate); **final target recomputed to 240 / ~2,410**; `sections/technology.md` marks HF 🔬. |
| Leveson / RNLE / whitespace (RE-06) | Leveson → **MIT Press 2011** (paper *Safety Science* 2004) in `01`,`08`; RNLE load constant → **set by the revised 1993 equation** in `02`; stray `04` diagram trailing whitespace trimmed; whitespace validated over untracked files via **`git add --intent-to-add`**. |
| MDLOOM-artifact truth (RE-07) | Focused **HF-only MDLOOM, 12 files, 0/0** recorded; `.mdloom/last-check.json` refreshed from the stale prototype `3` to `12`; sibling warnings reported separately. |
| Records (RE-02) | This panel + `R2-gold-rubric.md` created; citation-risk items closed against authoritative sources with recorded status; STATUS/Pulse/WAVE + DoD closure evidence updated, **IN REVIEW preserved**. |

## Findings ledger

| ID | Lens | Severity | Subject |
|---|---|---|---|
| ES-01 | expert-skeptic | BLOCK | `05` EF convention mis-stated; bounded-probability ceiling ignored ("0.06–0.9 from EF=5" without method); SPAR-H adjustment applied below the ≥3-negative-PSF trigger |
| ES-02 | expert-skeptic | BLOCK | `07` automation model charged L1 a takeover failure; single-`K` structure, no common-`p`/level-`C(L)` split; sweep read as a winner |
| ES-03 | expert-skeptic | BLOCK | `10` overlapping (non-orthogonal) coverage "strata" — experience and sensory tail merged; 12-cell percentage double-counts |
| ES-04 | expert-skeptic | BLOCK | `09` prescriptive interventions ("same fix"/paper checklist/structured handoff/second check) instead of candidate mechanisms |
| RE-01 | reference-editor | BLOCK | `11` reporting-rate comparison stated as determinate without triangulation; additional-evidence list missing |
| RE-02 | reference-editor | BLOCK | No independent full-module panel record / `R2-gold-rubric`; citation-risk items not closed with recorded status; DoD closure evidence unrecorded |
| ES-05 | expert-skeptic | WARN | `08` barrier taxonomy presented as universal strength ranking; dust example gave actionable barrier advice; common-cause decomposition implicit |
| RE-03 | reference-editor | WARN | Cross-references were code-tick only; no clickable Markdown links across the 12 guides |
| RE-04 | reference-editor | WARN | ≥2-channel accessibility invariant claimed module-wide but absent in `01`,`03`,`05`,`09`,`10` |
| RE-05 | reference-editor | WARN | `TRACKER.md`/section totals didn't separate HCI-complete from HF-in-review or count HF in the final target |
| RE-06 | reference-editor | WARN | Leveson mis-dated (→ 2011); RNLE load-constant provenance (→ revised 1993 equation); untracked-whitespace validation via intent-to-add |
| RE-07 | reference-editor | WARN | `.mdloom/last-check.json` recorded the prototype's 3 files, not the 12-guide HF-only 12/0/0; sibling warnings not separated |

**BLOCK: 6 · WARN: 6 — all repaired in this pass; none outstanding in source or records.**

## Validation observed

- **Focused MDLOOM (HF-only, all twelve `human-factors/[00–11]` guides):** **12 files checked, 0
  errors, 0 warnings**. `.mdloom/last-check.json` refreshed to `files_checked: 12`. Sibling MDLOOM/
  whitespace warnings, if any, are tracked **separately** and are not part of this module number.
- **Source-backfill `--validate` (regenerate + validate) for `human-factors`:** **12/12 round-trip
  PASS** (`roundtrip_passed: 12`, `roundtrip_failed: 0`), tables 20, structured blocks 81, FLETCH
  registry `fletches: 61` (`.fletch/registries/maxim-human-factors-source-corpus.json`). No sibling
  content guide was edited in this pass, so only `human-factors` was regenerated.
- **Backfill-generator unit tests** (`.claude/skills/maxim-source-backfill/tests`): **9 passed**.
- **`git diff --check` (including untracked via `git add --intent-to-add`):** clean — no
  trailing-whitespace or conflict-marker errors across the HF guides and records after the `04`
  diagram trim.
- **Custody outcome:** `human-factors/` is untracked, so all twelve guides carry `mdloom-backfill`
  backsources only (Git provenance `pending`); all remain `status: source-custody` /
  `source_custody: partial`.
- No `commit`/`push`; no submodule pointer update; no edits outside the twelve HF guides, the HF
  source-corpus, the trackers/section page, and the wave records/panels.

## Gate status — IN REVIEW

The R1 full-module findings — a conservative superset of expert-skeptic quantitative/model/overclaim
defects and reference-editor citation/standard/structure/records/artifact defects — are repaired with
**no unresolved BLOCK or WARN** in source. Because this same panel raised and repaired them, it does
**not** self-ratify: an **independent final re-review** is the remaining Definition-of-Done step, so
Pulse 04 and the wave stay **IN REVIEW, not closed**.

## R2 tier evidence and registry decision

`R2-gold-rubric.md` scores every guide on all ten Gold dimensions, records 3–5 guide-specific reader
tasks with pass/fail evidence, and states the mechanical/adversarial/source-custody/Da Vinci status.

- **Tier:** **Silver** for all 12 guides.
- **Why not Gold:** **no HF-specific Da Vinci invariant** exists in `mdloom.toml`, and external/
  authentic source custody is **partial** (`mdloom-backfill` only; Git provenance pending on an
  untracked module) — **no Gold without pins and custody**.
- **Registry:** **no insertion** in `context/gold/REGISTRY.md`; no Candidate-Hardened or Certified
  Gold claim.
- **Wave gate:** **IN REVIEW pending independent final re-review.** Gold/Da Vinci/external-source
  completion is optional future work.
