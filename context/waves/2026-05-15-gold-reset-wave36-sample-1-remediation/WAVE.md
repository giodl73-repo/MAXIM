---
wave: gold-reset-wave36-sample-1-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 36 Sample 1 Remediation

## Mission

Begin Wave 36 reset review with the food-plants slice: repair substantive
editorial defects, validate proof/Da Vinci coverage, and restore Certified Gold
only with guide-specific R2 evidence.

## Claim Boundary

This wave certifies only:

| Guide | Invariant |
|---|---|
| `food-plants/07-SUGAR-CROPS.md` | `sugar-systems-architecture` |
| `food-plants/08-STIMULANT-CROPS.md` | `stimulant-crop-comparison` |
| `food-plants/09-MODERN-BREEDING.md` | `breeding-technology-landscape` |

It does not restore Gold to the wider Wave 36 factory backlog.

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave36-sample-1/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <3 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: recall-style cheat sheets replaced and breeding/stimulant-crop overclaims repaired |
| R2 panel | PASS: guide-specific scores, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only the three repaired guides restored to Current Certified Gold |

## Closeout

Wave 36 remains Candidate-Hardened provenance except for this scoped slice.
Certification rests on reset-era repair and R2 evidence, not the factory wave.

