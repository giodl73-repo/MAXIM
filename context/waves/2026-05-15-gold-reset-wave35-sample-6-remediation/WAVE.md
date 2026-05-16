---
wave: gold-reset-wave35-sample-6-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 35 Sample 6 Remediation

## Mission

Continue Wave 35 reset review with finance candidates: repair substantive
editorial defects, validate proof/Da Vinci coverage, and restore Certified Gold
only with guide-specific R2 evidence.

## Claim Boundary

This wave certifies only:

| Guide | Invariant |
|---|---|
| `finance/02-DERIVATIVES.md` | `derivatives-structural-landscape` |
| `finance/03-FIXED-INCOME.md` | `fixed-income-landscape` |
| `finance/04-RISK-MODELS.md` | `financial-risk-landscape` |

It does not restore Gold to the wider Wave 35 factory backlog.

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave35-sample-6/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <3 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: derivative, fixed-income, and risk-model diagnostic tables rebuilt; bootstrap, TIPS currentness, VaR convention, and FRTB currentness issues corrected |
| R2 panel | PASS: guide-specific scores, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only the three repaired finance guides restored to Current Certified Gold |

## Closeout

This sample continues Wave 35 reset with scoped certification backed by
reset-era repair, skeptical review, and reader-task evidence.

