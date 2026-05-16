---
wave: crosscut-pilot-design-patterns
date_open: 2026-05-15
status: complete
source_goal: crosscut-atlas-pilot
---

# Crosscut Pilot — 12 Design Patterns Across Reality

## Mission

Create the first crosscut atlas as a publishable pilot: a separate synthesis
layer that keeps the 13-section numbering, ships with its home section, and
connects patterns across the full MAXIM deck without duplicating the volumes.

## Claim Boundary

| Artifact | Claim |
|---|---|
| `crosscuts/12-design-patterns-across-reality/00-OVERVIEW.md` | Pilot crosscut overview for section 12, Computing & Software |
| `.mkdocs/mkdocs.yml` | Adds a minimal Crosscuts navigation entry for the pilot |

## Inputs

| Input | Use |
|---|---|
| `computing/01-PACKAGE.md` | Style anchor: big picture first, layered explanation, ASCII diagrams, tables, cheat sheet |
| `BILL-OF-MATERIALS.md` | Confirms current 13 sections / 52 volumes structure |
| `VOLUMES.md` | Confirms section numbering and publishing frame |
| `context/gold/REGISTRY.md` | Confirms current Gold proof/evidence posture |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Author and measure pilot | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/pilot-r1/R1-consolidated.md` |

## Validation Gates

| Gate | Requirement |
|---|---|
| Style contract | Pilot starts with a Big Picture ASCII diagram, layers downward, uses tables, ends with diagnostic Decision Cheat Sheet and Common Confusion Points |
| Crosscut contract | Every major concept maps back to multiple existing sections rather than becoming a new isolated discipline |
| Numbering contract | Crosscut uses section number 12 because Computing & Software is its publishing home |
| Mechanical proof | `proof.exe check --daVinci -e --no-fail proof.toml <pilot files>` returns OK and output contains no literal `FAIL` |
| Diff hygiene | `git diff --check -- <pilot files>` passes |
| Scale decision | Closeout records whether the pilot is ready to template across the remaining 12 crosscuts |

## Done Criteria

- The pilot guide is good enough to be the template for the other 12 crosscuts.
- The pilot is discoverable through MkDocs navigation.
- The wave records gates and lessons before scaling.

## Non-Goals

- Do not generate all 13 crosscuts in this wave.
- Do not rewrite the 52-volume deck.
- Do not modify `VOLUMES.md`, `PROJECTS.md`, or the Bill of Materials until the pilot shape is accepted.

## Closeout

The pilot crosscut is proof-clean and review-clean. It should be used as the
template for scaling the remaining 12 crosscuts: separate `crosscuts/` layer,
home-section numbering, cross-library appearance map, diagnostic Decision Cheat
Sheet, and explicit caveats against flattening domain knowledge into metaphor.

The first draft used nested ASCII boxes that proof rejected. The durable visual
grammar for crosscuts is simpler: terminal-safe stack diagrams, bracketed nodes,
and flow arrows rather than dense nested box art.

