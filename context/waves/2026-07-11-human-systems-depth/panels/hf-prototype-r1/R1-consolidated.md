# HF Prototype Boundary Gate — R1 Consolidated

Consolidated Round-1 boundary-gate review of the three `human-factors/` prototype guides
authored in Pulse 03:

- `human-factors/02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS.md` (scaling-gate prototype)
- `human-factors/03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md` (review-gated)
- `human-factors/06-DISPLAY-CONTROL-INTERFACE-DESIGN.md` (review-gated)

Panel lenses: **expert-skeptic** (`R1-expert-skeptic.md`) and **reference-editor**
(`R1-reference-editor.md`). This record merges their findings, records dispositions, and
sets the gate decision. It is **review-only** and edits no source itself.

## Scope & method

The three guides were chosen as prototypes because they sit on the module's hardest
boundaries: the quantitative-model depth + the `industrial-design/05` overlap (`02`), the
cognitive-mechanism seam with `cognitive-science/09` (`03`), and the safety-critical-UI ↔
HCI-usability seam plus domain deferral (`06`). R1 stress-tested them for advice-creep into
operational instruction, factual/standards accuracy, quantitative reproducibility,
construct/threshold reification, the HCI-seam caricature, scaling-contract completeness, and
record truthfulness. The findings below were **repaired in the same pass**; that is why R1
**conditionally** clears its own findings but does **not** ratify the pattern — an
independent strict re-review is required.

## Consolidated findings & disposition

| ID | Src | Guide/record | Issue | Sev | Disposition |
|---|---|---|---|---|---|
| C-01 | ES-01 | 02 | Worked case reads as operational lifting direction (cut distance / raise origin / remove twist / set work–rest) → recast as hypothetical model comparisons requiring qualified assessment + local validation | BLOCK | repaired |
| C-02 | ES-02 | 03 | Live-operational vigilance/flood prescriptions (watch rotations, injected live signals, live flood-response probes) → offline simulation/replay or descriptive measurement | BLOCK | repaired |
| C-03 | ES-03 | 06 | Operational alarm direction (delete / suppress / set deadband) → candidate hypotheses subject to hazard review, MoC, qualified validation, local procedures | BLOCK | repaired |
| C-04 | RE-01 | 02 | CAESAR "~2,400" stated as total → ~4,431 total (~2,400 North America), verified now | BLOCK | repaired |
| C-05 | RE-02 | 02 | "seven multipliers" → six multipliers + 23 kg load constant, verified now | BLOCK | repaired |
| C-06 | RE-03 | 03 | MRT 4th dimension = response modality → visual channel (focal/ambient); response modality noted separately, verified now | BLOCK | repaired |
| C-07 | RE-04 | 06 | Stale alarm standards → EEMUA 191 4th ed. 2024, ANSI/ISA-18.2-2016, IEC 62682:2022 (primary/authoritative, industry-specific), verified now | BLOCK | repaired |
| C-08 | RE-08 | architecture / pulse | Findings "… 24" (actual 20); gate "ratified/remaining step" → findings 20; gate **proposed, not ratified before R2**; R1 recorded; standards verified now | BLOCK | repaired |
| C-09 | ES-04 | 03 | Performance–workload "redline" as a universal rule → schematic, task/strategy/context-dependent, no universal redline | WARN | repaired |
| C-10 | ES-05 | 03 | Heuristic "WORKLOAD = demand/supply" equation → labelled schematic | WARN | repaired |
| C-11 | ES-06 | 06 | Discretionary/casual-user caricature; safety-critical UI framed as not-HCI → safety-critical systems remain HCI systems; joint acceptance recorded | WARN | repaired |
| C-12 | ES-07 / RE-05 | 02 / 03 | No reproducible quantitative demonstration → synthetic percentile/joint-accommodation math + bounded RNLE sensitivity (`02`) and a discordant raw/weighted-TLX + performance + SA pass (`03`) | WARN | repaired |
| C-13 | RE-06 | 06 | No quantitative alarm demonstration → fictional before/after alarm metrics + prioritization rationale + uncertainty/validation | WARN | repaired |
| C-14 | RE-07 | 02 | Scaling contracts are slogans → testable Definition of Done (8 gates) per remaining guide + common safety/accessibility contract | WARN | repaired |
| C-15 | ES-06 / RE-09 | 02 / 06 / STATUS / architecture | Joint HCI/HF/domain acceptance unrecorded + WARN diagrams missing → joint-acceptance handoff diagram (`06`), joint-distribution diagram (`02`), acceptance recorded in guides/STATUS/architecture | WARN | repaired |
| C-16 | RE-09 | 02 / 03 / 06 / architecture | Recall-oriented tasks; thin citation-risk register → tasks recast to computation/boundary; citation-risk register expanded with verified-now results | WARN | repaired |

BLOCK: 8 · WARN: 8 · all **repaired** in the repair pass; none outstanding in source.

## Validation observed

- Focused PROOF (repo `proof.toml`, the three guides only): **3 files checked, 0 errors, 0
  warnings** after repairs.
- `git diff --check`: clean on the touched files.
- No source-corpus backfill was run (out of scope, by pulse design); no edits to any sibling
  module (`industrial-design/`, `cognitive-science/`, `human-computer-interaction/`,
  `systems-engineering/`, `clinical-medicine/`, `nuclear/`, `aeronautics/`, `transportation/`,
  `biomedical-engineering/`). Metadata stays `status: prototype` / `source_custody:
  needs-source` / `backsource_ids: []`; no Gold/Da Vinci tier or `context/gold` row is claimed.

## Gate decision

**Pulse 03 remains IN REVIEW.** R1 found and drove the repair of 16 conservative-prototype
findings, but every fix was made by the authoring pass itself; R1 cannot both raise and clear
its own findings. Ratification requires an independent **strict re-review (R2)** that:

1. re-derives the `02` synthetic percentile / joint-accommodation math (`0.90^k` and the
   positive-correlation bound) and the bounded RNLE **six-multiplier** sensitivity from the
   stated inputs, and the `03` raw/weighted-TLX arithmetic (RTLX 48.8 vs weighted 60.3);
2. re-checks the corrected facts against primary sources — CAESAR (~4,431 total / ~2,400
   North America), the NIOSH revised equation (23 kg + six multipliers), Wickens MRT
   (focal/ambient visual channel), and the alarm-standard editions (EEMUA 191 4th ed. 2024,
   ANSI/ISA-18.2-2016, IEC 62682:2022);
3. confirms the safety-contract recasts read cleanly end to end — no operational lifting,
   vigilance, or alarm direction survives; each candidate is a hypothesis for hazard
   review / MoC / qualified validation / local procedures, or an offline/descriptive option;
4. confirms the discordant TLX/performance/SA pass, the before/after alarm metrics, the
   testable Definition of Done, and the joint HCI/HF/domain acceptance (safety-critical
   systems remain HCI systems) are load-bearing, not decorative;
5. confirms the records stay truthful — findings **MAXIM-HF-01 … 20**; the gate **proposed,
   not ratified**; standards **verified now**; metadata prototype / needs-source.

Only after R2 signs off may the prototype pattern be marked **ratified** and govern the
Pulse-04 authoring of the remaining nine guides. Until then: no integration, no backfill, no
Pulse-04 authoring.
