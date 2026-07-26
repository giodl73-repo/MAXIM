---
wave: human-systems-depth
pulse: 04
date: 2026-07-13
status: in-review
depends_on: [03]
governing_roles: [reference-editor, expert-skeptic]
---

# Pulse 04 - Human Factors Authoring, Integration, and Source Backfill

> **Current disposition (2026-07-13): AUTHORING/INTEGRATION/BACKFILL + FULL-MODULE R1/R2 PANEL DONE
> — WAVE IN REVIEW (independent final re-review pending).**
> The remaining nine `human-factors/` guides are authored at full peer depth on the ratified
> (Pulse-03) prototype pattern, the module is wired into navigation/section/`TRACKER`, minimal
> reciprocal pointers were added to the six boundary siblings, and source-corpus backfill ran for
> `human-factors`. The module passes **focused MDLOOM (12 files, 0 errors, 0 warnings)**. The
> **independent full-module adversarial panel** (Definition-of-Done **closure gate 12**,
> `panels/hf-full-r1/`) has now been **conducted**: it surfaced a conservative **6 BLOCK + 6 WARN**
> superset, all **repaired** in the guides and records, closed the citation/edition items (gates
> 4/11) against authoritative sources, and scored every guide **Silver** (`R2-gold-rubric.md`) with
> **no registry row**. Because that panel both raised and repaired the findings, an **independent
> final re-review** is the remaining closure step, so this pulse is **IN REVIEW, not DONE**, and the
> wave is **IN REVIEW**. No Gold/Da Vinci tier and no `context/gold` registry row are claimed.

## Mission

Complete `human-factors/` by authoring the remaining nine guides on the **gate-passed (R1 +
independent R2) prototype pattern** and the **Testable Definition of Done** carried by the
scaling-gate prototype `02`; integrating the finished module into the library's navigation and
trackers; adding minimal reciprocal cross-references into the six sibling boundary surfaces; and
running the source-corpus backfill. This takes the module from **3/12 prototypes** to **12/12
authored** and from **unintegrated** to **wired**. The full-module adversarial panel has
run and its findings are repaired; final independent re-review/sign-off is the remaining
closure gate, so the wave remains **IN REVIEW**.

## Pre-implementation Scout

```powershell
# Governing context and the ratified pattern + Definition of Done
Get-Content CLAUDE.md
Get-Content context\waves\2026-07-11-human-systems-depth\WAVE.md
Get-Content context\waves\2026-07-11-human-systems-depth\artifacts\HUMAN-FACTORS-ARCHITECTURE.md
Get-Content context\waves\2026-07-11-human-systems-depth\pulses\03+human-factors-architecture.md
Get-Content context\waves\2026-07-11-human-systems-depth\panels\hf-prototype-r2\R2-consolidated.md
# The gate-passed prototypes and the scaling contracts + DoD they carry
Get-Content human-factors\02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS.md   # incl. Guide-Family Scaling Contracts + DoD
Get-Content human-factors\03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md, human-factors\06-DISPLAY-CONTROL-INTERFACE-DESIGN.md
Get-Content human-factors\STATUS.md
# Integration + reciprocal-pointer targets (read before editing)
Get-Content sections\technology.md, .mkdocs\mkdocs.yml, TRACKER.md
Get-Content industrial-design\05-ERGONOMICS.md, cognitive-science\09-APPLIED-BRIDGE.md, systems-engineering\06-FMEA-RELIABILITY.md
Get-Content clinical-medicine\11-SAFETY-QUALITY-AND-WORKFLOW.md, biomedical-engineering\07-MEDICAL-DEVICES.md, human-computer-interaction\STATUS.md
# Backfill mechanics + MDLOOM surface
Get-Content .claude\skills\maxim-source-backfill\SKILL.md, .claude\skills\maxim-source-backfill\scripts\module_source_backfill.py
Get-Content mdloom.toml | Select-Object -First 92
```

## Scope Inventory

| Area | Files |
|---|---|
| New guides (9) | `human-factors/{00-OVERVIEW,01-HISTORY-FOUNDATIONS,04-HUMAN-ERROR-TAXONOMIES,05-HUMAN-RELIABILITY-ANALYSIS,07-AUTOMATION-HUMAN-MACHINE,08-SAFETY-SYSTEMS-AND-HAZARD-ANALYSIS,09-DOMAIN-APPLICATIONS,10-METHODS-AND-MEASUREMENT,11-ORGANIZATIONAL-SAFETY-CULTURE}.md` |
| Module MDLOOM config | `human-factors/mdloom.toml` (added; tolerance = 2, `check_col_separators = false`, matching every other module) |
| Module manifest | `human-factors/STATUS.md` (→ 12/12 authored, module COMPLETE & WIRED, WAVE IN REVIEW) |
| Navigation / section | `.mkdocs/mkdocs.yml` (Technology nav entry); `sections/technology.md` (Directories row, landscape SYSTEMS-ENGINEERING track, count, volume plan, adjacent-section bridges) |
| Library tracker | `TRACKER.md` (Summary Dashboard row 🔬 In review; totals note) |
| Reciprocal pointers (6 siblings) | `industrial-design/05-ERGONOMICS.md` (→ HF `02` quantitative-systems depth; product-form entry preserved); `human-computer-interaction/STATUS.md` (→ HF `03`/`04`/`06`/`08` safety-critical evidence; interaction/a11y methods retained); `cognitive-science/09-APPLIED-BRIDGE.md` (→ HF `03` applied measurement; mechanism/theory retained); `clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW.md` (→ HF `04`/`11` generic science; clinical application retained); `systems-engineering/06-FMEA-RELIABILITY.md` (→ HF `05`/`08` human extension; tree/RPN math retained); `biomedical-engineering/07-MEDICAL-DEVICES.md` (→ HF `06`/`09` use-safety; device engineering/regulation retained) |
| Source corpus (regenerated) | `.mdloom/backfill/**`, `.crop/views/**`, `.mdport/packs/**`, `.fletch/registries/**` for `human-factors` + the 5 changed content-guide siblings |
| Wave tracking | this pulse; `WAVE.md` Pulse Sequence (Pulse 04 → IN REVIEW; final re-review/sign-off pending) |
| **Remaining Pulse-04 gate** | final independent re-review/sign-off only |
| **Out of scope / future work** | any Gold-tier / Da Vinci-invariant work; any legal content in `law/` |

## Authoring Contract (how the nine guides were written)

Each guide follows the gate-passed pattern **and** the **Testable Definition of Done** recorded in
`02` (§"Guide-Family Scaling Contracts" / "Testable Definition of Done"): the **eight content
gates** (1 required formal model(s) named+dated; 2 reproducible synthetic quantitative
demonstration; 3 uncertainty/validity/bias analysis; 4 source-hierarchy/edition attribution; 5
explicit boundary test; 6 conceptual terminal-readable diagram in the MDLOOM-safe open idiom; 7
fully worked fictional case; 8 3–5 calculation/interpretation reader tasks) **and** the **common
safety & accessibility contract** (no operational instruction / certification / accident-or-legal
ruling / individual fitness assessment; accessibility as a ≥2-channel safety requirement; the
evidence-vs-acceptance seam — modules supply methods/evidence, acceptance belongs to the
accountable organization and its regulator).

| Guide | Required formal model(s) | Minimum quantitative demonstration | Boundary test (defers) |
|---|---|---|---|
| `00` Overview | discipline map + ownership/defer matrix | coverage/MECE check: every concept claimed once, no gap/overlap | not a modeling guide; duplicates no guide |
| `01` History | dated lineage (scientific mgmt → WWII → Fitts/Chapanis → resilience) | dated timeline + the "average airman" collapse (Daniels 1952) shown as dated, not universal | mechanism → `cognitive-science/`; imports no exposure math |
| `04` Error taxonomies | Reason GEMS + Rasmussen SRK; latent conditions | worked classification of 5 synthetic events → level + fix family | clinical taxonomy → `clinical-medicine/11`; no blame/legal |
| `05` HRA | THERP/HEART/SPAR-H/CREAM HEP as bounded estimate; PSFs | SPAR-H worked HEP reported as a **range** (EF, method variance, PSF sweep) | tree math → `systems-engineering/06`; no re-derivation |
| `07` Automation | Sheridan; Parasuraman-Sheridan-Wickens LOA; Bainbridge ironies | synthetic stage×level allocation scored on the workload/OOTL trade (common `p`, level-specific `C(L)` sweep) | domain autopilots → `aeronautics/`/`transportation/`; adds failure modes |
| `08` Hazard | barrier/Swiss-cheese; HAZOP/bow-tie/STAMP-STPA | synthetic bow-tie with one quantified branch + common-cause dependency | FTA/FMEA math → `systems-engineering/06`; certifies nothing |
| `09` Domain apps | apply-and-defer across ≥2 domains | synthetic same-model-two-domains alarm read + portability tally | re-teaches no domain system; defers to owners + `law/` |
| `10` Methods | HTA/CTA; observation; simulation; instrumentation | synthetic study design + a **coverage/sampling** argument | inferential statistics → `statistics-applied/` |
| `11` Safety culture | Safety-I/II; HRO; just culture | synthetic reporting/injury-metric read with confounds ("not one score") | clinical → `clinical-medicine/11`; org theory → `organizational-behavior/` |

## Deliverables

- [x] Nine guides authored at full peer depth, each with ownership/defer header, safety/ethics
      banner + per-guide banner, landscape diagram, layered ASCII (dash-rule open idiom),
      decision-useful tables, named+dated formal models, a reproducible synthetic quantitative
      pass, a fully worked fictional case, 3–5 reader tasks, Decision Cheat Sheet, Common Confusion
      Points, global/WEIRD/resource caveats, and a non-WEIRD contrasting example — meeting the
      eight DoD content gates and the common safety/accessibility contract.
- [x] `human-factors/mdloom.toml` added (the module was missing it as a prototype); single-file
      MDLOOM now resolves the module config, and all 12 guides pass focused MDLOOM (0/0).
- [x] `STATUS.md` → **12/12 authored**, module **COMPLETE & WIRED**, **WAVE IN REVIEW**; manifest
      marks updated; Placement → wired; Pulse 04 status recorded.
- [x] Integration: `.mkdocs/mkdocs.yml` Technology nav entry; `sections/technology.md` Directories
      row + landscape SYSTEMS-ENGINEERING track + count + volume plan + adjacent-section bridges;
      `TRACKER.md` Summary Dashboard row (🔬 In review) + note.
- [x] Reciprocal boundary work: minimal pointers into the six siblings above; each preserves the
      sibling's owned scope (product-form; interaction/a11y method; cognitive mechanism/theory;
      clinical application; tree/RPN math; device engineering/regulation) and each carries the
      evidence-vs-acceptance framing. No other sibling edits.
- [x] Source-corpus backfill (`--validate`) for `human-factors` and the five changed
      content-guide siblings; HF guides graduate to `status: source-custody` / `source_custody:
      partial` with `mdloom-backfill` backsources.
- [x] **Full-module R1/R2 adversarial panel** over all 12 guides (DoD closure gate 12) —
      **conducted** (`panels/hf-full-r1/`: expert-skeptic + reference-editor + consolidated +
      `R2-gold-rubric`); a conservative **6 BLOCK + 6 WARN** superset was surfaced and **repaired**
      in the guides and records; every guide scores **Silver**, **no registry row**; citation-risk
      items closed against authoritative sources. **Independent final re-review pending** — the
      remaining step before the pulse and wave close.
- [ ] **Out of scope / future work:** the independent final re-review; any Gold-tier / Da
      Vinci-invariant work; any legal content in `law/`.

## Validation

Focused, module-scoped validation (no commit/push):

```powershell
# Generator tests for the source-backfill helper
python -m pytest .claude\skills\maxim-source-backfill\tests -q

# Source-corpus backfill + validate for HF and the changed content-guide siblings
$env:CARGO_TARGET_DIR = "C:\src\TRACKER\repos\tools-infra\_cargo-target"
foreach ($m in "human-factors","industrial-design","cognitive-science","systems-engineering","clinical-medicine","biomedical-engineering") {
  python .claude\skills\maxim-source-backfill\scripts\module_source_backfill.py --module-dir $m --module-id $m --validate
}

# Focused MDLOOM over the touched content guides (00-OVERVIEW is mdloom.toml-excluded on a full-repo run)
cargo run --manifest-path C:\src\TRACKER\repos\tools-infra\proof\Cargo.toml --quiet -- check `
  human-factors\01-*.md human-factors\04-*.md human-factors\05-*.md human-factors\07-*.md `
  human-factors\08-*.md human-factors\09-*.md human-factors\10-*.md human-factors\11-*.md `
  industrial-design\05-ERGONOMICS.md cognitive-science\09-APPLIED-BRIDGE.md `
  systems-engineering\06-FMEA-RELIABILITY.md clinical-medicine\11-SAFETY-QUALITY-AND-WORKFLOW.md `
  biomedical-engineering\07-MEDICAL-DEVICES.md --config mdloom.toml

git --no-pager diff --check
```

The source-corpus backfill regenerates MDLOOM/CROP/MDPORT/FLETCH from the canonical numbered
guides; the five sibling backfills include the reciprocal pointers. No commit or push; no submodule
pointer update.

## Status

`human-factors/` is **12/12 authored and WIRED**; the nine new guides follow the gate-passed
pattern and the Testable Definition of Done, and keep the safety/ethics contract (no operational
instruction, no certification, no accident/legal ruling, no fitness assessment; models
dated/bounded; acceptance deferred to the accountable organization and its regulator). The module
is wired into `sections/technology.md`, `.mkdocs/mkdocs.yml`, and `TRACKER.md`; reciprocal pointers
were added to the six boundary siblings only; source-corpus backfill ran for HF and the five
changed content-guide siblings; focused MDLOOM is clean (12 files, 0/0). The independent full-module
adversarial panel (`panels/hf-full-r1/`) has been **conducted** — 6 BLOCK + 6 WARN repaired, every
guide **Silver**, no registry — so the remaining Definition-of-Done step is an **independent final
re-review**, which is **pending**; the wave is **IN REVIEW**. **No Da Vinci figure invariants and no
Gold eligibility** are claimed.

## Non-Goals

- Independent final re-review and final sign-off: **pending** (the full-module panel is done; this
  final re-review is what keeps the wave IN REVIEW, not closed).
- Do not claim Gold-tier or Da Vinci-invariant status, or insert a `context/gold` registry row.
- Do not create legal content in `law/`.
- Do not edit sibling modules beyond the six minimal reciprocal boundary surfaces.
- Do not commit, push, or update TRACKER submodule pointers.
