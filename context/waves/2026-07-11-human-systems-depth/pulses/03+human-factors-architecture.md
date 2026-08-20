---
wave: human-systems-depth
pulse: 03
date: 2026-07-12
status: done
depends_on: [01, 02]
governing_roles: [reference-editor, expert-skeptic]
---

# Pulse 03 - Human Factors Module Architecture (Prototype Boundary Review)

## Mission

Define `human-factors/` as a first-class, non-duplicating MAXIM discipline module and
de-risk its three hardest boundaries by prototyping before full authoring. Establish the
module's scope against `industrial-design/05-ERGONOMICS`, `cognitive-science/09-APPLIED-
BRIDGE`, the completed `human-computer-interaction/` module (the HCI↔HF seam),
`systems-engineering/06-FMEA-RELIABILITY`, `clinical-medicine/11-SAFETY-QUALITY-AND-
WORKFLOW`, and the domain owners (`nuclear/05`, `aeronautics/04`, `transportation/07`,
`biomedical-engineering/07`); ratify the 12-guide problem-first manifest; lock the
ownership/defer matrix, the reciprocal HCI↔HF seam, and the safety/ethics contract; author
the three highest-risk guides — `02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS` (the two-stage
**scaling gate**), `03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS`, and `06-DISPLAY-CONTROL-
INTERFACE-DESIGN` (both **review-gated** prototypes) — at full peer-level depth; and record
the architecture for the Pulse-04 authoring pass. **This is a prototype boundary review,
not the full module** — the remaining nine guides, navigation/section integration, and
source-corpus backfill are deferred to Pulse 04.

## Pre-implementation Scout

```powershell
# Governing context and exemplars
Get-Content CLAUDE.md
Get-Content context\waves\2026-07-11-human-systems-depth\WAVE.md
# Depth/format exemplars and the in-wave prototype pattern
Get-Content human-computer-interaction\05-USABILITY-EVALUATION.md, human-computer-interaction\STATUS.md
Get-Content context\waves\2026-07-11-human-systems-depth\artifacts\HUMAN-COMPUTER-INTERACTION-ARCHITECTURE.md
Get-Content context\waves\2026-07-11-human-systems-depth\pulses\01+hci-architecture.md
Get-Content .claude\skills\maxim-review\SKILL.md
# Inspect the sharpest overlap surfaces (do NOT edit these modules)
Get-Content industrial-design\05-ERGONOMICS.md      # compact product-form ergonomics entry
Get-Content cognitive-science\09-APPLIED-BRIDGE.md   # owns psychophysical laws + Endsley SA/NDM as theory
Get-Content systems-engineering\06-FMEA-RELIABILITY.md, clinical-medicine\11-SAFETY-QUALITY-AND-WORKFLOW.md
Get-Content nuclear\05-SAFETY-SYSTEMS.md, aeronautics\04-AVIONICS.md, transportation\07-AUTONOMOUS-VEHICLES.md, biomedical-engineering\07-MEDICAL-DEVICES.md
# PROOF rule surface for content guides
Get-Content proof.toml | Select-Object -First 130
```

## Scope Inventory

| Area | Files |
|---|---|
| Prototype guides | `human-factors/02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS.md`, `human-factors/03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md`, `human-factors/06-DISPLAY-CONTROL-INTERFACE-DESIGN.md` |
| Module manifest | `human-factors/STATUS.md` (full 12-guide manifest; `02` scaling-gate + `03`/`06` review-gated prototypes; rest planned) |
| Architecture record | `context/waves/2026-07-11-human-systems-depth/artifacts/HUMAN-FACTORS-ARCHITECTURE.md` (MAXIM-HF-01 … 20 + G00 … G11) |
| Wave tracking | `context/waves/2026-07-11-human-systems-depth/pulses/03+human-factors-architecture.md`; `WAVE.md` Pulse Sequence table (Pulse 03 → DONE) and current-state line |
| **Deferred to Pulse 04** | `00-OVERVIEW` + guides `01`, `04`, `05`, `07`, `08`, `09`, `10`, `11`; `sections/*`; `.mkdocs/mkdocs.yml`; `TRACKER.md`; reciprocal pointers into `industrial-design/05`, `cognitive-science/09`, `human-computer-interaction/`; source-corpus (`.proof/backfill/**`, `.mdcrop/**`, `.mdport/**`, `.fletch/**`) |

## Scope Contract (non-duplication)

- **Uniquely owns** the **quantitative-systems view of the human in a system of work** —
  organized **by the human-factors problem (fit, load, error, reliability, interface,
  automation, hazard, method, culture), not by domain** (MAXIM-HF-14), the single most
  important non-duplication decision.
- **Defers** compact **product-form ergonomics** to `industrial-design/05` (which remains
  the product-form entry); **cognitive mechanism and the SA/NDM theory** to
  `cognitive-science/09`; **interactive digital usability** to `human-computer-interaction/`;
  **reliability mathematics** to `systems-engineering/06` (HF extends it to the human);
  **clinical patient-safety practice** to `clinical-medicine/11`; the **domain systems** to
  `nuclear/05`, `aeronautics/04`, `transportation/07`, `biomedical-engineering/07`;
  **inferential statistics** to `statistics-applied/`; and **legal obligation** to `law/`.
- **Resolves the sharpest overlap** (`industrial-design/05-ERGONOMICS`, which already carries
  a broad "ergonomics and human factors" treatment) as **product-form vs quantitative-systems
  depth**: `industrial-design/05` keeps the compact product-form entry; `human-factors/02`
  owns population-distribution modeling, occupational biomechanics, the bounded lifting model,
  and the system of work. At Pulse-03 time this is **forward-only** (no edits to sibling
  modules under the wave guardrail — prototype review first); reciprocal cross-references are
  a Pulse-04 decision.
- **Adopts the reciprocal HCI↔HF seam** the completed HCI module already locked: HF owns
  operator performance/workload/error/safety-critical integration/performance-under-stress;
  HCI owns interactive usability/accessibility/evaluation; domains own their systems; `law/`
  owns legal obligation.
- **Safety/ethics contract** is a hard gate and stricter than HCI's: educational systems
  reference only; no operational instructions; no certification/compliance ruling; no
  accident/legal determination; no individual fitness assessment; models/standards/stereotypes
  attributed, dated, bounded.

## Deliverables

- [x] Architecture record with research question, findings MAXIM-HF-01 … 20, the ratified
      12-guide manifest (G00 … G11), the ownership/defer matrix, the HCI↔HF seam, the
      safety/ethics contract, the standards/citation-risk register, bias/limitations, quality
      risks, the prototype/scaling rationale (two-stage scaling gate + review gates), and the
      adopt/prototype/defer decisions.
- [x] `human-factors/STATUS.md` — full 12-guide manifest; `02` recorded as the **scaling-gate
      prototype** and `03`/`06` as **review-gated prototypes**, the other nine **planned**;
      module explicitly **IN PROGRESS / not integrated**; boundary contracts + HCI↔HF seam +
      safety/ethics contract recorded; placement explicitly **not yet wired**; Pulse 03 **IN
      REVIEW**.
- [x] `02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS.md` — the population as a distribution
      (percentiles, z-scores, the **multivariate-accommodation trap**, "no average person");
      clearance/reach/strength design-limit logic and the accommodation cost curve;
      anthropometric data as **dated, sampled estimates** (ANSUR/CAESAR/NHANES/DINED, secular
      trend); the workspace/reach envelope; posture & occupational biomechanics (moment arms,
      spinal load) with **bounded** screening indices (RULA/REBA/OWAS/Snook, attributed/dated);
      the **NIOSH lifting equation as a bounded model** (structure, Lifting Index, and its
      **validity domain / silence outside it**, dated 1981/1993/1994, attributed — **no lifting
      instruction, no certification**); work–rest/fatigue/environment; the explicit
      **product↔workplace boundary** with `industrial-design/05`; a fictional worked case;
      reader tasks; Decision Cheat Sheet; Common Confusion Points; global/WEIRD/resource
      caveats; a non-WEIRD contrasting case; and the module-wide **Guide-Family Scaling
      Contracts** (the scaling gate). Treats models as bounded, not universal.
- [x] `03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md` — workload as supply/demand (**multiple
      resource theory**); the **workload–performance dissociation** (performance-resource
      function, redline, underload); the three measurement families with **NASA-TLX raw vs
      weighted and its limits**, physiological (HR/HRV/pupil/EEG, sensitive-but-non-specific),
      and performance (primary/secondary/embedded); the **vigilance decrement**; **SA levels**
      as an applied scaffold and **SA measurement (SAGAT/SPAM/SART)** with the **construct
      critiques** (folk-model/circularity; product-vs-process; ground-truth); **attentional
      tunneling / change blindness / out-of-the-loop**; **team and distributed SA**; explicit
      **defer of mechanism to `cognitive-science/09`**; ownership header, banner, worked case,
      reader tasks, cheat sheet, confusions, caveats, non-WEIRD case, and a **Prototype Seam
      Contract**. No certification.
- [x] `06-DISPLAY-CONTROL-INTERFACE-DESIGN.md` — display/control **compatibility** (S-R,
      movement, Warrick); **population stereotypes with cultural caveats**; **coding &
      redundancy** (never color alone, as a safety need); **alarm philosophy** (flood/nuisance/
      chattering/standing/cry-wolf; rationalization/prioritization/suppression; EEMUA 191 /
      ISA-18.2 as **dated, bounded** guidance, not certification); **salience vs nuisance** (the
      attention budget); **mode/state visibility** (mode error, automation surprise);
      **ecological interface design** (SRK, abstraction hierarchy); **control-room layout**
      (importance/frequency/sequence/function); the **safety-critical-UI↔HCI seam** and the
      **domain-system deferrals**; a fictional worked case; reader tasks; cheat sheet;
      confusions; caveats; non-WEIRD case; and a **Prototype Seam Contract**. **No runnable
      operating procedures, no certification.**
- [x] `WAVE.md` updated — Pulse Sequence table Pulse 03 → **DONE** after independent R2;
      current-wave-state advances to Pulse 04.
- [x] **Boundary-gate panel R1 recorded (`panels/hf-prototype-r1/`).** The two-stage scaling
      gate for `02` (Stage 1 quantitative-model correctness/bounds; Stage 2 the
      `industrial-design/05` boundary + scaling contracts) and the review gates for `03`
      (mechanism-deferral + construct-critique) and `06` (HCI seam + domain deferral +
      no-procedure/no-certification) were **exercised** by the R1 panel (expert-skeptic,
      reference-editor, consolidated), which found and drove repair of the
      conservative-prototype findings (B1 factual/model; B2 quantitative worked cases; B3
      safety contract; B4 HCI↔HF seam; B5 scaling contracts; B6 records). Load-bearing standards
      were **verified now** against primary sources.
- [x] **Independent strict re-review (R2) complete — gate ratified
      (`panels/hf-prototype-r2/`).** An independent R2 panel (expert-skeptic + reference-editor
      + consolidated) that neither authored nor repaired the R1 findings re-derived the
      quantitative passes, re-checked the standards, and closed its own finer-grained findings
      (joint-coverage method + rho-range; RNLE CM/FM correctness + hot-environment removal;
      guide-03 one-representative-participant + common weighting + "four families" fix;
      guide-06 traceable alarm inventory + alarm-vs-notification separation;
      evidence-vs-acceptance seam; Definition-of-Done closure gates) with **no unresolved
      BLOCK/WARN**. The prototype pattern/gate is **ratified**.
- [ ] **Deferred to Pulse 04 (now unblocked):** author `00` + the nine remaining guides; wire
      section/nav/`TRACKER`; run source-corpus backfill; run the full-module adversarial panel;
      decide reciprocal cross-references into `industrial-design/05`, `cognitive-science/09`,
      and `human-computer-interaction/`.

## Validation

Focused prototype validation only (per the boundary-review scope; **no full-module source
backfill**). `STATUS.md`, `00-OVERVIEW`, the architecture record, and the pulse/wave records
are excluded from PROOF by `proof.toml` (`*/STATUS.md`, `*/00-OVERVIEW.md`, `context/**`); the
three prototype **guides** are checked explicitly:

```powershell
cargo run --release --manifest-path C:\src\TRACKER\repos\tools-infra\proof\Cargo.toml -- `
  check human-factors\02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS.md `
        human-factors\03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md `
        human-factors\06-DISPLAY-CONTROL-INTERFACE-DESIGN.md --config proof.toml
# guides are untracked: intent-to-add so git diff --check actually inspects them,
# then undo staging to leave them untracked (still not integrated).
git add -N human-factors\02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS.md `
           human-factors\03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md `
           human-factors\06-DISPLAY-CONTROL-INTERFACE-DESIGN.md
git --no-pager diff --check
git reset -q -- human-factors
```

Result: focused PROOF reports **3 files checked, 0 errors, 0 warnings** after both the R1 and
the R2 repairs (PROOF checks the three prototype guides **explicitly by path**, since the
module is untracked and `*/STATUS.md` / `*/00-OVERVIEW.md` / `context/**` are PROOF-excluded).
`git diff --check` only inspects **tracked/indexed** content by default, so — because these
guides are still untracked — they were staged with **intent-to-add** (`git add -N`) purely so
the whitespace/conflict-marker check actually covers them, then unstaged; with that, `git diff
--check` is clean. Source backfill was **not** run, and no sibling
module (`industrial-design/`, `cognitive-science/`, `human-computer-interaction/`,
`systems-engineering/`, `clinical-medicine/`, `nuclear/`, `aeronautics/`, `transportation/`,
`biomedical-engineering/`) was edited. Each prototype guide carries a landscape diagram, a
layered model with the actual formalism (percentile/z-score + multivariate accommodation with
reproducible joint-accommodation math + the NIOSH RWL/LI model, its **six** multipliers, and a
bounded LI sensitivity in `02`; MRT's four dimensions incl. the focal/ambient visual channel +
the performance-resource **schematic** + a discordant raw/weighted-TLX + performance + SA worked
pass in `03`; compatibility + coding redundancy + alarm rationalization with before/after
metrics + SRK/abstraction-hierarchy in `06`), decision-useful tables, explicit
ownership/defer boundaries, 5 reader tasks, a Decision Cheat Sheet, Common Confusion Points,
global/WEIRD/resource caveats, and a non-WEIRD contrasting case. Named models, standards, and
figures are attributed and dated (NIOSH 1981/1993/1994; RULA 1993; REBA 2000; OWAS 1977; Snook
1991; NASA-TLX 1988; SAGAT 1988/1995; SART 1990; Mackworth 1948; Warrick 1947; EEMUA 191
4th ed. 2024; ANSI/ISA-18.2-2016; IEC 62682:2022; Rasmussen SRK 1983; EID 1992), and treated
as population-and-context-dependent estimates with an explicit validity domain, not universal
constants. The **load-bearing** figures (NIOSH six multipliers + 23 kg; CAESAR ~4,431/~2,400
North America; Wickens MRT focal/ambient; the alarm-standard editions) were **verified now**
(this pulse) against primary sources and the guides corrected; remaining low-risk precision
items are logged in the architecture record's **standards/citation-risk register** for
Pulse-04 spot-checks (metadata truthfully `status: prototype` / `source_custody: needs-source`
/ `backsource_ids: []`).

## Status

Architecture recorded (findings MAXIM-HF-01 … 20); the three highest-risk guides authored at
full depth and passing focused PROOF; STATUS manifest and wave tracking updated. The two-stage
scaling gate (`02`) and the review gates (`03`, `06`) were **exercised by the R1 boundary-gate
panel** (`panels/hf-prototype-r1/`) and then **ratified by an independent strict R2 re-review**
(`panels/hf-prototype-r2/`) that neither authored nor repaired the findings; load-bearing
standards were **verified** and re-checked, and R2 closed the remaining finer-grained findings
with **no unresolved BLOCK/WARN**. The prototype pattern/gate is therefore **ratified** and
**Pulse 03 is DONE**. **No Da Vinci figure invariants and no Gold eligibility are claimed** —
that is future-tier work, not a Pulse-03 gate. Pulse 04 (author the remaining nine guides, wire
section/nav/`TRACKER`, run source-corpus backfill, run the full-module panel) is now unblocked.
No module integration, no source backfill, and no edits to any sibling module were made in this
pulse.

## Non-Goals

- Do not author the remaining nine guides or `00-OVERVIEW` in this pulse.
- Do not integrate the incomplete module into `sections/`, `.mkdocs/mkdocs.yml`, or `TRACKER.md`.
- Do not run full-module source backfill (PROOF/MDCROP/MDPORT/FLETCH) — this is a prototype
  boundary review; no backfill.
- Do not edit, rescope, or add reciprocal cross-references into `industrial-design/05`,
  `cognitive-science/09`, `human-computer-interaction/`, `systems-engineering/06`,
  `clinical-medicine/11`, `nuclear/05`, `aeronautics/04`, `transportation/07`, or
  `biomedical-engineering/07` (deferred to Pulse 04; prototype review first).
- Do not lower the depth bar to introductory-textbook prose or template filling.
- Do not issue operational instructions, safety certification, accident/legal determinations,
  or individual fitness assessments (safety/ethics contract).
- Do not commit or push; do not update TRACKER submodule pointers.
