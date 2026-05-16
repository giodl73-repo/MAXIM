---
wave: gold-reset-sample-5-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Sample 5 Remediation

## Mission

Run a fifth Wave 37 slice through the reset-era Gold process: repair substantive
editorial defects in the next geology guides, validate proof/Da Vinci coverage,
and restore Certified Gold only with guide-specific R2 evidence.

## Claim Boundary

This wave certifies only:

| Guide | Invariant |
|---|---|
| `geology/07-GEOLOGIC-TIME.md` | `geologic-time-pillars` |
| `geology/08-ECONOMIC-GEOLOGY.md` | `economic-geology-framework` |
| `geology/09-SURFICIAL-GEOLOGY.md` | `surficial-processes-agent-overview` |

It does not restore Gold to the wider factory backlog.

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-sample-5/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <3 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: recall-style decision tables replaced; overbroad extinction/resource claims corrected or caveated |
| R2 panel | PASS: guide-specific scores, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only the three repaired guides restored to Current Certified Gold |

## Closeout

This wave continues the reset pattern: mechanical hardening is candidacy; Gold
requires editorial repair, skeptical review, and specific reader-task evidence.

