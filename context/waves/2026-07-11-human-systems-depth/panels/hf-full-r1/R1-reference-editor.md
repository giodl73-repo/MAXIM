# Human-Factors Full-Module R1 — Reference-Editor

> **Disposition: REPAIRED IN THIS PASS — wave remains IN REVIEW pending an independent final
> re-review.** Preserved conservative, whole-module pass over all **twelve** `human-factors/`
> guides (`00`–`11`) and the module records/artifacts, run after authoring, integration, and
> source-corpus backfill. The reference-editor lens owns **citation/edition accuracy, standard
> attribution, structure and cross-reference navigability, the accessibility contract's honest
> reach, the trackers/totals, the MDLOOM artifact truth, and the panel-record/DoD closure
> evidence**. Every finding is **repaired**. This lens does **not** clear the gate — see the
> verdict. No commit/push. Tier decision (**Silver**, no registry) lives in `R2-gold-rubric.md`.

## Scope reviewed

All twelve guides at peer depth; the named-model citations (Leveson STAMP, the revised NIOSH lifting
equation, SPAR-H/NUREG-CR-6883, Bainbridge, Parasuraman-Sheridan-Wickens, Reason, Hollnagel); the
cross-reference surface (intro deferrals, cheat sheets, boundaries); the module-wide safety &
accessibility contract vs its actual per-guide presence; `TRACKER.md` and `sections/technology.md`
totals; `.mdloom/last-check.json`; and the wave/pulse/STATUS records and the (missing) full-module
panel record.

## Findings

**RE-01 — BLOCK — Guide `11` (safety culture): the reporting-rate comparison was stated as
determinate without triangulation, and the additional-evidence list was missing.** The worked metric
pass read Unit A (120 reports) as "likely a HEALTHY reporting culture" and Unit B (18 reports, "none
reported") as "a RED FLAG for fear/underreporting" — a verdict the raw counts cannot support. A
report-count gap is **indeterminate**: it is equally consistent with a healthier reporting culture,
higher exposure/opportunity, looser reportable-event definitions, or a different severity mix.
*Repaired:* the box now states the comparison is **INDETERMINATE without triangulation**, lists the
rival explanations, and lists the **additional evidence to gather** — exposure/opportunity
denominators, a reporting-**climate** survey, consistent near-miss **definitions**, **severity**
stratification, the **near-miss-to-incident** ratio, and independent **audit** findings — before any
conclusion. Only two firm readings survive on the numbers alone ("none reported" = a reporting-system
**gap**, not proven safety; injury rate ≠ process-safety risk). The §4 reporting-paradox box now
frames high/low rates as **candidates** requiring triangulation, and reader task 1, the fictional
case step, and two cheat-sheet rows are aligned.

**RE-02 — BLOCK — Records: no independent full-module panel record or Gold rubric existed, and
citation-risk items were not closed against authoritative sources with a recorded status.** Pulse
04's closure gate 12 (the independent full-module panel) had no `panels/hf-full-r1/` record, no
`R2-gold-rubric.md`, and the DoD closure evidence was unrecorded; several load-bearing citations were
flagged but not closed. *Repaired:* this panel (`R1-expert-skeptic.md`, `R1-reference-editor.md`,
`R1-consolidated.md`) and `R2-gold-rubric.md` are created; the citation-risk items are closed against
authoritative sources and recorded (see **Citation-risk closure** below); and STATUS/Pulse/WAVE and
the DoD closure evidence are updated to record the panel while keeping the honest **IN REVIEW**
status (the panel raised and repaired the findings, so a final independent re-review is still
pending). No Gold tier and no `context/gold` registry row are claimed — external/authentic source
custody is `partial` and there is no HF-specific Da Vinci invariant, so a Gold claim would need pins
and custody that do not exist.

**RE-03 — WARN — Cross-references were code-tick only; no clickable Markdown links across the 12
guides.** Every cross-reference (`06`, `industrial-design/05`, `systems-engineering/06`, …) was an
un-navigable inline code span. *Repaired:* meaningful **clickable Markdown links** were added across
all twelve guides — the intro "builds-on / borrows / defers" targets and the highest-value cheat-sheet
routes now link to the exact sibling/guide file (e.g.
`[systems-engineering/06](../systems-engineering/06-FMEA-RELIABILITY.md)`), chosen to deepen
understanding without link-spamming every tick. ASCII-diagram references are left as ticks (links do
not render inside fenced blocks).

**RE-04 — WARN — The ≥2-channel accessibility/safety invariant was claimed module-wide but absent in
guides `01`, `03`, `05`, `09`, `10`.** The architecture record and STATUS assert the invariant is
carried by every guide, but it was only actually stated in `00`, `02`, `04`, `06`, `07`, `08`, `11`.
*Repaired:* a **concise, explicit cross-cutting ≥2-channel note** was added to each of the five
missing guides, each anchored to its own subject (history's design-induced-error lineage in `01`;
SA-cue perceivability in `03`; the HMI PSF in `05`; the cross-domain alarm/mode cue in `09`; the
use-error/coverage measurement side in `10`) and each pointing to guide `06` §3 where the invariant is
owned — so the record's module-wide claim is now true.

**RE-05 — WARN — `TRACKER.md`/section totals did not cleanly separate HCI-complete from
HF-in-review, and the final target did not count HF.** The dashboard's "Final target" read 239
directories / ~2,398 files, neither counting the eventual HF module nor stating that 239 is the
complete count with HF tracked separately. *Repaired:* the **complete total stays 239** (HCI counted;
`human-factors/` explicitly separate and in review) and the **final target is recomputed to 240
directories / ~2,410 content files** (239 + `human-factors/`'s 12 guides), closing when the
full-module panel finishes its final re-review; `sections/technology.md` now marks `human-factors/`
as 🔬 in review. Honest statuses preserved.

**RE-06 — WARN — Citation/edition and whitespace-record defects.** (1) **Leveson**, *Engineering a
Safer World*, was dated "2004+/2012" (`01`) and "2012" (`08`) — the authoritative MIT Press edition
is **2011**, with the STAMP foundational paper in *Safety Science* **2004**. (2) The **revised NIOSH
lifting equation** load constant was attributed to "the 1991 metric revision" (`02`), an imprecise
provenance; the 23 kg load constant was **set by the revised 1993 equation** (Waters, Putz-Anderson,
Garg & Fine, *Ergonomics* 1993; applications manual 1994). (3) One untracked-file **trailing-whitespace**
line inside a `04` ASCII diagram would trip `git diff --check`. *Repaired:* Leveson is corrected to
`MIT Press 2011; foundational paper Safety Science 2004` in both `01` and `08`; the RNLE load constant
now reads "23 kg, set by the revised 1993 equation" (the 1993/1994 primary citations were already
correct); the stray trailing whitespace is trimmed; and the whitespace validation is run over the
untracked files via **`git add --intent-to-add`** so `git diff --check` actually inspects them.

**RE-07 — WARN — MDLOOM artifact truth: `.mdloom/last-check.json` recorded the prototype's 3-file run,
not the 12-guide module.** The persisted artifact read `files_checked: 3` (from Pulse 03's three
prototypes), overstating cleanliness relative to the authored 12-guide module and blending sibling
scope. *Repaired:* a **focused, HF-only MDLOOM over all twelve guides** was run and records the exact
**12 files checked, 0 errors, 0 warnings**; the artifact is refreshed to the 12-file result, and any
sibling MDLOOM/whitespace warnings are reported **separately**, not folded into the HF module number.

## Citation-risk closure (recorded exact status)

| Item | Authoritative source | Status |
|---|---|---|
| Leveson STAMP book | *Engineering a Safer World*, MIT Press **2011** (foundational paper, *Safety Science* **2004**) | **Closed** — corrected in `01`, `08` |
| Revised NIOSH lifting equation | Waters, Putz-Anderson, Garg & Fine, *Ergonomics* **1993** 36(7):749–776; applications manual **1994**; LC = 23 kg set by the 1993 revision | **Closed** — `02` wording fixed |
| SPAR-H | Gertman, Blackman et al., **NUREG/CR-6883 (2005)**; US NRC, public domain | **Closed** — already exact in `05` |
| Bainbridge, "Ironies of Automation" | *Automatica* **1983**, 19(6):775–779 | **Closed** — dated in `07` |
| Parasuraman, Sheridan & Wickens | *IEEE Trans. SMC-A* **2000** | **Closed** — dated in `07` |
| EEMUA 191 / ANSI-ISA-18.2 / IEC 62682 | 4th ed. 2024 / 2016 / 2022 | **Closed** — verified in prototype R2, unchanged |

All are **educational, dated, bounded** attributions; MAXIM remains standalone and no external
source is a completion gate. Where a specific external primary could not be pinned, custody stays
`partial` (see the tier decision) — no Gold claim is made on unpinned custody.

## Decision

**REPAIRED — no unresolved BLOCK or WARN after this pass; the lens does not itself ratify.** The
reference/citation/structure/records defects — one determinate-without-triangulation BLOCK (`11`),
one records/panels BLOCK (`RE-02`), and five WARNs (cross-refs, accessibility reach, totals,
Leveson/RNLE/whitespace, MDLOOM truth) — are repaired, and the citation-risk items are closed against
authoritative sources with recorded status. Because the repairs were made in this same pass, an
**independent final re-review is still required**; the wave stays **IN REVIEW**. Tier: **Silver**,
**no registry** — see `R2-gold-rubric.md`.
