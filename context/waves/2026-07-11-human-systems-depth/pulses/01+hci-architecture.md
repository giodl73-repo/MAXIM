---
wave: human-systems-depth
pulse: 01
date: 2026-07-12
status: complete
depends_on: []
governing_roles: [reference-editor, expert-skeptic]
---

# Pulse 01 - HCI Module Architecture (Prototype Boundary Review)

## Mission

Define `human-computer-interaction/` as a first-class, non-duplicating MAXIM discipline
module and de-risk its two hardest boundaries by prototyping before full authoring.
Establish the module's scope against `cognitive-science/`, `statistics-applied/`,
`industrial-design/`, `psychology/`, and the concurrent `human-factors/`; ratify the
12-guide lifecycle-plus-cross-cutting manifest; lock the HCI↔HF (three-way with `law/`)
seam and the safety/ethics contract; author the two highest-risk guides
(`05-USABILITY-EVALUATION`, `08-ACCESSIBILITY-INCLUSIVE-DESIGN`) at full peer-level
depth; and record the architecture for the Pulse-02 authoring pass and the Pulse-03
human-factors coordination. **This is a prototype boundary review, not the full
module** — the remaining ten guides, navigation/section integration, and source-corpus
backfill are deferred to Pulse 02.

## Pre-implementation Scout

```powershell
# Read the governing context and exemplars
Get-Content CLAUDE.md, EXPANSION.md
Get-Content context\waves\2026-07-11-human-systems-depth\WAVE.md
# Depth/format exemplars (deeper than computing/01-PACKAGE.md)
Get-Content clinical-medicine\03-DIAGNOSTIC-TEST-INTERPRETATION.md, clinical-medicine\STATUS.md
Get-Content context\waves\2026-07-11-clinical-and-chemical-foundations\artifacts\CLINICAL-MEDICINE-ARCHITECTURE.md
Get-Content .claude\skills\maxim-review\SKILL.md, .claude\skills\maxim-pulse\SKILL.md
# Inspect the sharpest overlap surfaces (do NOT edit these modules)
Get-Content cognitive-science\09-APPLIED-BRIDGE.md      # owns Fitts/Hick/Miller/GOMS "HCI laws"
Get-Content industrial-design\06-INTERACTION-DESIGN.md  # owns Norman action model at product level
Get-Content cognitive-science\STATUS.md, industrial-design\STATUS.md, statistics-applied\STATUS.md
# MDLOOM rule surface for content guides
Get-Content mdloom.toml | Select-Object -First 92
```

## Scope Inventory

| Area | Files |
|---|---|
| Prototype guides | `human-computer-interaction/05-USABILITY-EVALUATION.md`, `human-computer-interaction/08-ACCESSIBILITY-INCLUSIVE-DESIGN.md` |
| Module manifest | `human-computer-interaction/STATUS.md` (full 12-guide manifest; `05` + `08` gate-passed prototypes, rest planned) |
| Architecture record | `context/waves/2026-07-11-human-systems-depth/artifacts/HUMAN-COMPUTER-INTERACTION-ARCHITECTURE.md` (MAXIM-HCI-01 … 24 + G00 … G11) |
| Wave tracking | `context/waves/2026-07-11-human-systems-depth/pulses/01+hci-architecture.md`; `WAVE.md` frontmatter (date_open/status), Guardrails, Pulse Sequence table (Pulse 01 → DONE), Quality/Exit gates |
| **Deferred to Pulse 02** | `00-OVERVIEW` + guides `01`, `02`, `03`, `04`, `06`, `07`, `09`, `10`, `11`; `sections/computing-and-software.md`; `.mkdocs/mkdocs.yml`; `TRACKER.md`; source-corpus (`.mdloom/backfill/**`, `.crop/**`, `.mdport/**`, `.fletch/**`) |

## Scope Contract (non-duplication)

- **Uniquely owns** the **design and evaluation of interactive computing systems for
  human use** — organized **around the design↔evaluate lifecycle and cross-cutting
  concerns, not by platform/technology and not by re-teaching cognitive science**
  (MAXIM-HCI-19), the single most important non-duplication decision.
- **Defers** cognitive **mechanisms and the psychophysical "HCI laws"** (Fitts, Hick,
  Miller, cognitive load, GOMS) to `cognitive-science/09` (+ `01`–`08`); general
  inferential statistics to `statistics-applied/`; Norman's action model & interaction
  design at the **product level** plus physical ergonomics to `industrial-design/06`/`05`;
  experimental-psychology foundations to `psychology/`; statistical-graphics theory &
  rendering internals to `data-science/`/`computer-graphics/`; model internals behind
  conversational/agentic interfaces to `ai-engineering/`/`machine-learning-theory/`;
  operator performance/workload/error/safety to the forthcoming `human-factors/`; and
  legal obligation to `law/`.
- **Resolves the sharpest overlap** (`cognitive-science/09-APPLIED-BRIDGE`, which already
  owns the "HCI/UX laws") as **mechanism-vs-application**: `cognitive-science/` owns the
  psychology and the law derivations; `human-computer-interaction/` cites & applies them
  and owns the design/evaluation methods. At Pulse-01 time this is **forward-only** (no
  edits to `cognitive-science/` or `industrial-design/` under the wave guardrail — prototype
  review first); a minimal reciprocal cross-reference, if warranted, is a Pulse-02 decision.
- **Locks the HCI↔HF seam** now (three-way with `law/` for accessibility): HCI owns the
  interactive interface + its usability/accessibility design/evaluation; `human-factors/`
  owns operator performance/workload/error/safety; `law/` owns legal obligation.
- **Safety/ethics contract** is a hard gate: no manipulation/dark-pattern playbook; no
  legal/compliance ruling; no safety-certification; research ethics as concept not IRB
  substitute; standards/"laws" attributed, dated, bounded (heuristics ≠ laws; conformance
  ≠ usability).

## Deliverables

- [x] Architecture record with research question, findings MAXIM-HCI-01 … 24, the ratified
      12-guide manifest (G00 … G11), the ownership/defer matrix, the HCI↔HF (three-way with
      `law/`) seam, the safety/ethics contract, bias/limitations, quality risks, the
      prototype rationale, and adopt/prototype/defer decisions.
- [x] `human-computer-interaction/STATUS.md` — full 12-guide manifest; `05` and `08`
      recorded as **gate-passed prototypes**, the other ten **planned**; module explicitly **IN PROGRESS
      / not complete**; boundary contracts + HCI↔HF seam + safety/ethics contract recorded;
      placement explicitly **not yet wired**.
- [x] `05-USABILITY-EVALUATION.md` — formative/summative; heuristic evaluation with the
      **evaluator effect** and limitations; cognitive walkthrough; think-aloud (reactivity/
      veridicality); the ISO-9241 effectiveness/efficiency/satisfaction metric triad with
      task-success/time/error paths; **SUS scoring math and interpretation limits**;
      controlled usability tests; **A/B vs usability** (what each is blind to); qualitative
      coding & **triangulation**; the **sample-size ceiling** (Nielsen–Landauer discovery
      model vs measurement/power) with explicit defer of statistics to `statistics-applied/`;
      the benchmark→iterate loop; **a full fictional mixed-method evaluation plan + results
      synthesis** (*Tessera*); explicit defer of cognitive mechanism to `cognitive-science/`;
      ownership header, banner, landscape, software bridges, 5 reader tasks, Decision Cheat
      Sheet, Common Confusion Points, global/WEIRD/resource caveats. Treats heuristics as
      heuristics, not laws.
- [x] `08-ACCESSIBILITY-INCLUSIVE-DESIGN.md` — disability models (medical/social/ICF/
      interaction); **accessibility vs usability vs inclusive/universal design**; **WCAG 2.2
      principles/levels, dated (2023) and bounded**; assistive-technology interaction via the
      **accessibility tree** (name + role required, value/state when applicable, +
      descriptions/relationships); keyboard/focus/semantics; access by
      **visual/auditory/motor/cognitive** channel; accessible research (testing with disabled
      users); **conformance vs actual usability**; localization/literacy/low-bandwidth;
      procurement/governance; the **three-way HCI↔HF↔law boundary** (opening diagram + worked
      case); a fictional inclusive-design case (*Rivergate*). No compliance/legal advice; no
      exploit/manipulation detail; full style-contract sections + caveats. Treats conformance
      as a floor, not usability.
- [x] `WAVE.md` updated — frontmatter `date_open: 2026-07-12`, `status: active`; stale FONTES
      binding removed from the Exit Gate (MAXIM standalone; source evidence optional
      supporting); Guardrails + a **Pulse Sequence** table with **HCI prototypes first**
      (Pulse 01 → DONE); Quality Gate.
- [x] **Prototype boundary-gate review — R1 + R2 recorded; pattern ratified.** The R1 panel
      (`expert-skeptic` + `reference-editor` + consolidated) over `05` and `08` ran under
      `panels/hci-prototype-r1/` and returned 16 conservative-prototype findings (statistical
      rigor, model honesty, WCAG accuracy, global coverage, metadata truthfulness), **all
      repaired**. Because those fixes were made in the same pass, an independent **strict R2
      re-review** (`panels/hci-prototype-r2/` — `reference-editor` + `expert-skeptic` +
      consolidated) then re-derived the statistics, re-checked the WCAG/recall citations,
      confirmed the models and the full scaling contracts, closed a further seven
      strict-editor findings, and **signed off**. The **prototype pattern is ratified** (the
      12-guide manifest was ratified at authoring); Pulse 01's boundary review is complete.
- [ ] **Deferred to Pulse 02:** author `00` + the nine remaining guides; wire section/nav/
      `TRACKER`; run source-corpus backfill; run the adversarial panel over the full module;
      decide any reciprocal cross-references into `cognitive-science/`/`industrial-design/`.

## Validation

Focused prototype validation only (per the boundary-review scope; **no full-module source
backfill**). `STATUS.md`, the architecture record, and the pulse/wave records are excluded
from MDLOOM by `mdloom.toml` (`*/STATUS.md`, `context/**`); the two prototype **guides** are
checked explicitly:

```powershell
# Repo-config MDLOOM (MAXIM mdloom.toml) via the tools-infra/proof Cargo manifest,
# scoped to the two prototype guides
cargo run --release --manifest-path C:\src\TRACKER\repos\tools-infra\proof\Cargo.toml -- `
  check human-computer-interaction\05-USABILITY-EVALUATION.md `
        human-computer-interaction\08-ACCESSIBILITY-INCLUSIVE-DESIGN.md --config mdloom.toml
git --no-pager diff --check
```

Result: focused MDLOOM reports **2 files checked, 0 errors, 0 warnings**; `git diff --check`
is clean for the touched files. (The module is untracked, so MDLOOM was run against the two
guides explicitly.) Source backfill was **not** run, and `cognitive-science/` /
`industrial-design/` were **not** edited.

Each prototype guide carries a landscape diagram, a layered model with the actual formalism
(SUS scoring, the Nielsen–Landauer discovery model, and CI-width reasoning in `05`; the
name+role-required (value/state when applicable, + descriptions/relationships)
accessibility-tree contract, POUR, and WCAG levels in `08`),
decision-useful tables, explicit ownership/defer boundaries, 5 reader tasks, a Decision
Cheat Sheet, Common Confusion Points, and global/WEIRD/resource caveats. Named laws,
standards, and figures are attributed and dated (Nielsen heuristics 1994; Nielsen–Landauer
1993; SUS Brooke 1996; ISO 9241-11 1998/2018; WCAG 2.2 2023-10-05; universal design 1997;
ICF 2001; WHO prevalence 2022), and treated as population-and-context-dependent estimates,
not universal constants.

## Status

Architecture ratified and recorded; the two highest-risk guides authored at full depth and
passing focused MDLOOM; STATUS manifest and wave tracking updated. Both boundary-gate rounds
have now run. The R1 panel (`panels/hci-prototype-r1/` — expert-skeptic + reference-editor +
consolidated) raised conservative-prototype findings (advice-creep / overclaim /
heuristic-as-law / conformance-as-usability / statistical rigor / three-way-boundary honesty
/ metadata truthfulness), all **repaired** in `05`, `08`, STATUS, and the architecture
record; the independent **strict R2 re-review** (`panels/hci-prototype-r2/` — reference-editor
+ expert-skeptic + consolidated) verified those repairs, closed a further set of strict-editor
findings (full scaling-contract coverage, the target-rule α equivalence, the automated-recall
attribution, the `ground-truthier` / native-controls wording, and the records reconciliation),
and **signed off**. The **prototype pattern is ratified** and may govern Pulse-02 authoring;
the 12-guide **manifest** was ratified at authoring. **No Da Vinci figure invariants and no
Gold eligibility are claimed** — that is future-tier work, not a Pulse-01 gate. Pulse 02
(author the remaining ten guides, wire section/nav/`TRACKER`, run source-corpus backfill)
is still outstanding. No module integration, no source backfill, and no edits to
`industrial-design/` or `cognitive-science/` were made in this pulse.

## Non-Goals

- Do not author the remaining ten guides or `00-OVERVIEW` in this pulse.
- Do not integrate the incomplete module into `sections/`, `.mkdocs/mkdocs.yml`, or
  `TRACKER.md`.
- Do not run full-module source backfill (MDLOOM/CROP/MDPORT/FLETCH) — this is a prototype
  boundary review.
- Do not edit, rescope, or add reciprocal cross-references into `cognitive-science/` or
  `industrial-design/` (deferred to Pulse 02; prototype review first).
- Do not author or scope `human-factors/` (its own Pulse 03) — only the seam is locked here.
- Do not modify `README.md`, `FOREWORD.md`, `VOLUMES.md`, `PROJECTS.md`, or any unrelated
  module.
- Do not lower the depth bar to introductory-textbook prose or template filling.
- Do not commit or push; do not update TRACKER submodule pointers.
