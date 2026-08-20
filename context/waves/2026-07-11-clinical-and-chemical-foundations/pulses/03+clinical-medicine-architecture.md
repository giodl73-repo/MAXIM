---
wave: clinical-and-chemical-foundations
pulse: 03
date: 2026-07-11
status: done
depends_on: [01]
governing_roles: [reference-editor, expert-skeptic, index-weaver, ascii-cartographer]
---

# Pulse 03 - Clinical Medicine Module Architecture (Prototype Boundary Review)

## Mission

Define `clinical-medicine/` as a first-class, non-duplicating MAXIM discipline module
and de-risk its two hardest boundaries by prototyping before full authoring. Establish
the module's scope against `medicine/`, `disease/`, `pharmacology/`, `human-biology/`,
and `public-health/`; ratify the 12-guide reasoning-and-care-architecture manifest;
author the two highest-risk guides (`03` diagnostic decision theory, `08` specialty
interfaces) at full peer-level depth; and record the architecture for the Pulse-04
authoring pass and Pulse-05 pathology coordination. **This is a prototype boundary
review, not the full module** — remaining guides, navigation/section integration, and
source-corpus backfill are deferred to Pulse 04.

> **Final sign-off (reconciliation).** Pulse 03 is **DONE with final sign-off**: prototypes
> `03` and `08` passed the strict boundary gate across two adversarial passes (R1 + R2) with no
> unresolved BLOCK/WARN findings, establishing the ratified quality/safety pattern for the module.
> The `medicine/10 §11` ↔ `clinical-medicine/03` boundary — described as *forward-only* below, per
> the Pulse-03 guardrail against editing `medicine/` — is now **bidirectional**: a **minimal
> reverse** pointer from `medicine/10 §11` → `03` was added in Pulse 04, so the *forward-only /
> not-yet-bidirectional* phrasing in this record is **superseded**. The earlier
> `panels/clinical-prototype-r1/` "sign-off pending" wording is likewise superseded by this final
> sign-off; the remaining full-module review is a Pulse-04 concern (`panels/clinical-full-r1/`).

## Pre-implementation Scout

```powershell
# Read the governing context and exemplars
Get-Content CLAUDE.md, EXPANSION.md
Get-Content context\waves\2026-07-11-clinical-and-chemical-foundations\WAVE.md
Get-Content chemistry\00-OVERVIEW.md, chemistry\STATUS.md          # quality exemplar
Get-Content .claude\skills\maxim-review\SKILL.md, .claude\skills\maxim-pulse\SKILL.md
# Inspect the sharpest overlap surface (do NOT edit medicine/)
Get-Content medicine\10-DIAGNOSTICS-IMAGING.md | Select-Object -Index (455..610)
Get-Content disease\STATUS.md, medicine\STATUS.md, public-health\STATUS.md
```

## Scope Inventory

| Area | Files |
|---|---|
| Prototype guides | `clinical-medicine/03-DIAGNOSTIC-TEST-INTERPRETATION.md`, `clinical-medicine/08-SPECIALTY-INTERFACES.md` |
| Module manifest | `clinical-medicine/STATUS.md` (full 12-guide manifest; 03 + 08 complete, rest planned) |
| Architecture record | `context/waves/.../artifacts/CLINICAL-MEDICINE-ARCHITECTURE.md` (MAXIM-CLIN-01 … 24 + G00 … G11) |
| Wave tracking | `context/waves/.../pulses/03+clinical-medicine-architecture.md`; `WAVE.md` pulses table (Pulse 03 → IN REVIEW) |
| **Deferred to Pulse 04** | `00-OVERVIEW` + guides 01, 02, 04, 05, 06, 07, 09, 10, 11; `sections/life-sciences.md`; `.mkdocs/mkdocs.yml`; `TRACKER.md`; source-corpus (`.proof/backfill/**`, `.mdcrop/**`, `.mdport/**`, `.fletch/**`) |

## Scope Contract (non-duplication)

- **Uniquely owns** the transferable cognitive/system architecture of medicine:
  clinical reasoning, **diagnostic decision theory**, evidence appraisal, and
  care-process design — organized around **reusable reasoning patterns, not per-organ
  specialties** (MAXIM-CLIN-19).
- **Defers** disease catalogs/mechanisms/natural history to `disease/`; anatomy/
  physiology to `human-biology/`; drug classes + the diagnostics/imaging **catalog**
  and reference ranges + imaging physics to `medicine/` (incl. `medicine/10:~460–600`);
  receptor theory/ADME/PK/PD/pharmacogenomics to `pharmacology/`; population epi
  methods, screening **programs**, and health-system typology/financing to
  `public-health/`; and tissue/cell mechanism + lab-medicine result generation to
  `pathology/` (planned).
- **Three-way lab-interpretation split** (ratify with `pathology/` in Pulse 05):
  `pathology/` (why the result is) → `medicine/10` (the catalog/ranges) →
  `clinical-medicine/03` (how a clinician updates belief and decides to act).
- **Resolves the sharpest overlap** (`medicine/10` §11 Bayesian section) by a
  cross-reference from `03` (at Pulse-03 time, **forward-only** — no edits to `medicine/`
  under the wave guardrail; Pulse-01 non-goals). *Superseded by Pulse 04:* a **minimal
  reverse** pointer `medicine/10 §11` → `03` was added, so the boundary is now **bidirectional**,
  decision-theory-vs-catalog with deliberately layered treatments (not a duplication to
  reconcile).
- **Non-advice contract** is a hard gate: educational reference on *how clinicians
  reason and how care is organized*; never diagnosis, treatment/dosing, procedure, or
  emergency instructions.

## Deliverables

- [x] Architecture record with research question, findings MAXIM-CLIN-01 … 24, the
      ratified 12-guide manifest (G00 … G11), ownership/defer contract, non-advice
      contract, bias/limitations, quality risks, and adopt/prototype/defer decisions.
- [x] `clinical-medicine/STATUS.md` — full 12-guide manifest; `03` and `08` marked
      **prototype / in review**, the other ten **planned**; module explicitly **IN
      PROGRESS / not complete**; boundary contracts + non-advice contract recorded.
- [x] `03-DIAGNOSTIC-TEST-INTERPRETATION.md` — 2×2 belief engine; odds/LR Bayes;
      PPV/NPV prevalence dependence (screening paradox); ROC/AUC limitations;
      **Pauker–Kassirer test/treatment thresholds**; sequential/correlated testing;
      overtesting/incidentaloma cascades; value of information; a fully specified
      numerical worked case **with sensitivity analysis**; ownership header, module
      banner, landscape diagram, software bridges, reader tasks, Decision Cheat Sheet,
      Common Confusion Points. Defers catalog/ranges/imaging physics to `medicine/10`.
- [x] `08-SPECIALTY-INTERFACES.md` — specialties as an interface/service catalog;
      generalist vs specialist; primary/secondary/tertiary/quaternary care;
      consultation-question quality; referral/comanagement ownership semantics;
      scope/result follow-up + **closed-loop consultation**; resource/geographic
      variation; multi-specialty conflict resolution; a **specialty interface table**;
      no personalized referral triggers or medical advice; full style-contract sections.
- [x] `WAVE.md` pulses table updated — Pulse 03 → **IN REVIEW**.
- [x] **Prototype re-review (R1)** — single-round `expert-skeptic` + `reference-editor`
      panel over the two prototypes, recorded under `panels/clinical-prototype-r1/`.
      BLOCK/WARN findings repaired: `03` worked-case branch-by-branch threshold math,
      non-imperative/third-person recast, overgeneralization hedges, `medicine/10 §11`
      overlap honesty, and two contrasting transport-limit contexts; `08`
      referral-ownership-by-acceptance (five separated ownership fields), an end-to-end
      closed-loop comanagement case, alternate system topologies, an explicitly
      illustrative specialty table, and tightened nephrology scope. Focused PROOF re-run
      on `03`/`08` is clean; guides marked **prototype / in review** pending re-review
      sign-off.
- [x] **Strict re-review (R2)** — a stricter editorial pass over `03`/`08` (advice-creep
      + honesty re-check) closed five residual findings, recorded in
      `panels/clinical-prototype-r1/R1-consolidated.md`: reader-directed personal/
      emergency imperatives in both banners and the guide-08 cheat sheet recast to a
      descriptive scope statement and third-person model/contract states; the guide-03
      correlated-test **universal-inequality** claim replaced with the conditional-
      independence treatment (positive dependence overstates, negative can change
      direction; no universal inequality; validated joint model / empirical combined
      LR); guide-08 **routing-mechanism vs responsibility-contract** split into two
      independent axes with transfer gated on explicit, locally valid agreement +
      acknowledgment; specialty-PPV qualified to demonstrable enrichment + test
      transport (spectrum can shift Sn/Sp); and a compact **alternate-system**
      (district-hospital / task-shifting / teleconsult) end-to-end case added. Focused
      PROOF re-run on `03`/`08` is clean; guides passed the strict prototype gate with
      **final sign-off** (recorded as prototype-complete in `STATUS.md`).
- [ ] **Deferred to Pulse 04:** author `00` + the nine remaining guides; wire section/
      nav/TRACKER; run source-corpus backfill; run the adversarial panel over the full
      module.

## Validation

Focused prototype validation only (per the boundary-review scope; **no full-module
source backfill**):

```powershell
# Repo-config PROOF (MAXIM proof.toml) via the tools-infra/proof Cargo manifest,
# scoped to the two prototype guides
cargo run --manifest-path C:\src\TRACKER\repos\tools-infra\proof\Cargo.toml -- `
  check clinical-medicine\03-DIAGNOSTIC-TEST-INTERPRETATION.md `
        clinical-medicine\08-SPECIALTY-INTERFACES.md --config proof.toml
git --no-pager diff --check
```

If the Cargo-manifest PROOF is unavailable in the environment, record the exact failure
and fall back to focused structural validation (single H1; required `## Decision Cheat
Sheet` H2; ≥1 code block; no `@editor` tags; aligned ASCII boxes; consistent tables)
plus `git diff --check`, per `.claude/skills/maxim-pulse/SKILL.md`.

Each prototype guide carries a landscape diagram, a layered model with the actual
formalism (odds/LR math and threshold derivations in `03`; ownership-contract and
closed-loop models in `08`), decision-useful tables, explicit ownership/cross-reference
boundaries, 3–5 reader tasks, a Decision Cheat Sheet, and Common Confusion Points.
Numeric specifics in `03` are internally recomputed and labeled illustrative; the
LR interpretive bands are attributed and dated (Jaeschke *JAMA* 1994; McGee 2002), and
the threshold model is attributed (Pauker & Kassirer *NEJM* 1975/1980).

**Prototype re-review (R1) outcome:** the two guides were re-reviewed (`expert-skeptic`
+ `reference-editor`) and the repair pass recorded under `panels/clinical-prototype-r1/`.
After repairs, the focused PROOF above reports **2 files checked, 0 errors, 0 warnings**
and `git diff --check` is clean; source backfill was **not** run. The guides then went
through the R2 strict pass below and received **final prototype sign-off**.

**Strict re-review (R2) outcome:** a stricter editorial pass closed five residual
findings (banner + guide-08 cheat-sheet imperatives → descriptive scope statement +
third-person model/contract states; guide-03 correlated-test universal-inequality →
conditional-independence treatment with no universal inequality and a validated joint
model / empirical combined LR; guide-08 routing-vs-responsibility split into two
independent axes with transfer gated on explicit, acknowledged, locally valid agreement;
specialty-PPV enrichment/transport qualification with spectrum caveat; and a new
compact alternate-system end-to-end case). The focused PROOF re-run reports **2 files
checked, 0 errors, 0 warnings** and `git diff --check` is clean (the prototype module is
still untracked, so the check was run against the two edited guides explicitly); source
backfill was **not** run and `medicine/` was **not** touched. With R2 closed, the prototypes
received **final strict re-review sign-off** and the prototype gate is **passed** — Pulse 03 is
DONE.

## Status

Architecture ratified and recorded; the two highest-risk guides authored at full depth
and then **re-reviewed and repaired** across two strict passes (R1: `expert-skeptic` +
`reference-editor`; R2: a stricter advice-creep + honesty re-check), both recorded under
`panels/clinical-prototype-r1/`; STATUS manifest and wave tracking updated. Pulse 03 is
**DONE**: the prototype gate passed with no unresolved BLOCK/WARN findings, and guides
`03`/`08` now define the ratified quality/safety pattern for the module. Full authoring of
the remaining ten guides, section/nav/`TRACKER` integration, the reverse `medicine/10 §11`
→ `03` cross-reference, and source-corpus regeneration were carried out in Pulse 04 (see
`pulses/04+clinical-medicine-authoring.md`).

## Non-Goals

- Do not author the remaining ten guides or `00-OVERVIEW` in this pulse.
- Do not integrate the incomplete module into `sections/life-sciences.md`,
  `.mkdocs/mkdocs.yml`, or `TRACKER.md`.
- Do not run full module source backfill (PROOF/MDCROP/MDPORT/FLETCH) — this is a
  prototype boundary review.
- Do not rename, re-scope, or edit `medicine/` (deferred to a later boundary decision).
- Do not modify `README.md`, `FOREWORD.md`, `VOLUMES.md`, `PROJECTS.md`, or any
  unrelated module.
- Do not lower the depth bar to introductory-textbook prose or template filling.
