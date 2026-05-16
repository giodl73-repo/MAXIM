---
wave: crosscut-systems-and-failure
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_goal: crosscut-atlas-scale
---

# Crosscut — 07 Systems & Failure

## Mission

Scale the crosscut atlas template to the Technology home section with a
synthesis guide about incidents, degradation, cascades, verification, safety
cases, and resilience across the full MAXIM deck.

## Claim Boundary

| Artifact | Claim |
|---|---|
| `crosscuts/07-systems-and-failure/00-OVERVIEW.md` | Fourth crosscut overview, numbered to section 7 |
| `.mkdocs/mkdocs.yml` | Adds the crosscut to navigation |

## Inputs

| Input | Use |
|---|---|
| `crosscuts/12-design-patterns-across-reality/00-OVERVIEW.md` | Approved pilot structure |
| `crosscuts/13-risk-uncertainty-decision/00-OVERVIEW.md` | Risk-to-failure bridge |
| `context/waves/2026-05-15-crosscut-risk-uncertainty-decision/panels/risk-r1/R1-consolidated.md` | Next-crosscut recommendation |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Author and R1 panel | DONE | reference-editor, ascii-cartographer, expert-skeptic, bridge-builder, index-weaver | `panels/failure-r1/R1-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Style contract | PASS: Big Picture, layered sections, tables, diagnostic cheat sheet, Common Confusion Points |
| Crosscut contract | PASS: all 13 sections represented in Cross-Library Appearance Map |
| Numbering contract | PASS: section number 7 maps to Technology |
| Mechanical proof | PASS: focused proof/Da Vinci command returned OK and contained no literal `FAIL` |
| Diff hygiene | PASS |

## Done Criteria

- Guide is proof-clean.
- R1 panel records no BLOCK or WARN findings.
- MkDocs navigation includes the crosscut.

## Non-Goals

- Do not generate the remaining 9 crosscuts in this wave.
- Do not regenerate the Bill of Materials.

## Closeout

The Technology mapping works: the crosscut treats failure as an operating-system
property rather than a component morality play. It also establishes the incident
and resilience vocabulary needed by later tools, infrastructure, and standards
crosscuts.

