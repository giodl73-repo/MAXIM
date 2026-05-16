---
wave: gold-reset-sample-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Sample Remediation

## Mission

Repair the first reset-panel WARN findings for three Wave 37 samples, then run a
reset-era R2 panel before restoring any Certified Gold claim.

## Claim Boundary

This wave certifies only the three guides explicitly repaired and re-panelled:
`geology/05-PLATE-TECTONICS.md`,
`geotechnical-engineering/02-EFFECTIVE-STRESS.md`, and
`glassmaking/04-FLOAT-GLASS.md`. It does not restore Gold to the broader Gold
Factory backlog.

## Inputs

| Artifact | Use |
|---|---|
| `context/waves/2026-05-15-gold-certification-reset/panels/first-reset-panel/R1-consolidated.md` | WARN findings to close |
| `geology/05-PLATE-TECTONICS.md` | Plate-system remediation |
| `geotechnical-engineering/02-EFFECTIVE-STRESS.md` | Field-decision remediation |
| `glassmaking/04-FLOAT-GLASS.md` | Product-selection remediation |
| `proof.toml` | Da Vinci prerequisite validation |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, ascii-cartographer, expert-skeptic, bridge-builder, index-weaver | `panels/r2-sample-remediation/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <3 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: all R1 WARN findings closed by targeted guide edits |
| R2 panel | PASS: guide-specific scores and reader tasks recorded |
| Registry update | PASS: only the three repaired guides restored to Current Certified Gold |

## Closeout

This wave demonstrates the new Gold model: factory hardening created strong
candidates, the reset panel found real WARN issues, targeted guide edits closed
those issues, and only then did the registry restore Certified Gold.

