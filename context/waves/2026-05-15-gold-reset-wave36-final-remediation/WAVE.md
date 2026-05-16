---
wave: gold-reset-wave36-final-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 36 Final Remediation

## Mission

Complete Wave 36 reset review by repairing the remaining games-history
candidates, validating proof/Da Vinci coverage, and restoring Certified Gold
only with guide-specific R2 evidence.

## Claim Boundary

This wave certifies only:

| Guide | Invariant |
|---|---|
| `games-history/04-POKER.md` | `poker-evolution-timeline` |
| `games-history/05-BILLIARDS-POOL.md` | `billiards-family-tree` |

It closes Wave 36 reset certification. It does not change the wider factory
backlog rule: factory hardening is candidacy, not Gold.

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave36-final/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <2 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: poker solved-language, pot-odds math, CFR+ wording, snooker 147 details, and lookup-style tables corrected |
| R2 panel | PASS: guide-specific scores, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only the two repaired guides restored to Current Certified Gold |

## Closeout

Wave 36 reset is complete: all 24 Wave 36 candidates now have reset-era
repair, proof/Da Vinci validation, R2 evidence, and scoped registry rows.

