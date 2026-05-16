---
wave: gold-certification-reset
pulse: 03
date: 2026-05-15
status: done
depends_on: [01, 02]
governing_roles:
  - reference-editor
  - ascii-cartographer
  - expert-skeptic
  - bridge-builder
  - index-weaver
---

# Pulse 03 - First Reset Panel

## Mission

Run the first stricter Gold panel against a small Gold Factory sample and prove
that reset-era certification is not equivalent to factory hardening.

## Scope Inventory

| Guide | Factory Evidence | Da Vinci Invariant |
|---|---|---|
| `geology/05-PLATE-TECTONICS.md` | `context/waves/2026-05-15-gold-factory-wave-37/WAVE.md` | `global-plate-system` |
| `geotechnical-engineering/02-EFFECTIVE-STRESS.md` | `context/waves/2026-05-15-gold-factory-wave-37/WAVE.md` | `effective-stress-master-concept` |
| `glassmaking/04-FLOAT-GLASS.md` | `context/waves/2026-05-15-gold-factory-wave-37/WAVE.md` | `float-glass-process` |

## Pre-Implementation Scout

```powershell
Get-Content context\waves\2026-05-15-gold-factory-wave-37\WAVE.md
Get-Content geology\05-PLATE-TECTONICS.md
Get-Content geotechnical-engineering\02-EFFECTIVE-STRESS.md
Get-Content glassmaking\04-FLOAT-GLASS.md
Select-String -Path proof.toml -Pattern "global-plate-system|effective-stress-master-concept|float-glass-process"
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml geology\05-PLATE-TECTONICS.md geotechnical-engineering\02-EFFECTIVE-STRESS.md glassmaking\04-FLOAT-GLASS.md
```

Scout result: all three guides are mechanically clean and invariant-protected.
That satisfies the prerequisite gate only.

## Deliverables Checklist

| Deliverable | Status |
|---|---|
| Create reset panel files under `panels/first-reset-panel/` | done |
| Record guide-specific Gold scores and findings | done |
| Decide registry tier for each sampled guide | done |
| Update wave evidence | done |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS; proof output contained no `FAIL` |
| Rubric depth | PASS; consolidated panel records guide-specific notes |
| Adversarial review | PASS; WARN findings recorded |
| Reader tasks | PASS; tasks recorded, but several require stronger decision surfaces before Gold |
| Registry decision | PASS; all three remain Candidate-Hardened, none restored to Certified Gold |

## Non-Goals

- Do not edit guide content in this pulse.
- Do not remove Cross-References or Da Vinci invariants.
- Do not restore Certified Gold until WARN findings are fixed and re-panelled.

## Evidence

| Artifact | Purpose |
|---|---|
| `context/waves/2026-05-15-gold-certification-reset/panels/first-reset-panel/R1-reference-editor.md` | Style, layering, and decision-surface findings |
| `context/waves/2026-05-15-gold-certification-reset/panels/first-reset-panel/R1-ascii-cartographer.md` | Diagram usefulness findings |
| `context/waves/2026-05-15-gold-certification-reset/panels/first-reset-panel/R1-expert-skeptic.md` | Factual-density and adversarial findings |
| `context/waves/2026-05-15-gold-certification-reset/panels/first-reset-panel/R1-bridge-index.md` | Bridge and cross-reference findings |
| `context/waves/2026-05-15-gold-certification-reset/panels/first-reset-panel/R1-consolidated.md` | Scores, reader tasks, and registry decision |
