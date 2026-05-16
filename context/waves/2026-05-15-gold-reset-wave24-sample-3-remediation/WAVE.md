---
wave: gold-reset-wave24-sample-3-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 24 Sample 3 Remediation

## Mission

Repair and re-panel the mixed animal-phylogeny/archaeology Wave 24 sample before
restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `animal-phylogeny/10-AMPHIBIA.md` | `tetrapod-transition-amphibia` |
| `animal-phylogeny/11-REPTILIA-BIRDS.md` | `amniota-reptilia-birds` |
| `animal-phylogeny/12-MAMMALIA.md` | `mammal-phylogeny` |
| `archaeology/02-DATING-METHODS.md` | `archaeological-dating-time-range` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave24-sample-3/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: amphibian, reptile/bird, mammal, and dating-method cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 24 sample 3 restores three animal-phylogeny guides and one archaeology
guide with reset-era R2 evidence.

