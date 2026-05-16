---
wave: gold-reset-wave24-sample-1-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 24 Sample 1 Remediation

## Mission

Repair and re-panel the first Wave 24 animal-phylogeny sample before restoring
Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `animal-phylogeny/02-EARLY-ANIMALS.md` | `early-animals-non-bilaterian-grade` |
| `animal-phylogeny/03-LOPHOTROCHOZOA-WORMS.md` | `lophotrochozoa-worms-clade` |
| `animal-phylogeny/04-NEMATODA-ECDYSOZOA.md` | `ecdysozoa-molting-tree` |
| `animal-phylogeny/05-MOLLUSCA.md` | `mollusca-tree` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave24-sample-1/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: early animals, lophotrochozoan worms, ecdysozoans, and mollusks cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 24 sample 1 restores four animal-phylogeny guides with reset-era R2
evidence.

