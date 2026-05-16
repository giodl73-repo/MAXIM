---
wave: maxim-quality-control-spine
pulse: 04
date: 2026-05-14
status: done
depends_on: [02]
governing_roles: [ascii-cartographer, expert-skeptic]
---

# Pulse 04 - ASCII Perfection Spec

## Mission

Define what "ASCII art always perfect" means for MAXIM: not merely aligned
boxes, but diagrams that communicate structure, sequence, scale, and decisions.

## Pre-implementation Scout

```powershell
rg "```" C:\src\maxim\computing C:\src\maxim\distributed-systems C:\src\maxim\periodic-table --glob "*.md"
```

## Deliverables

- [x] Define diagram classes: box, pipeline, layer cake, matrix, timeline, map,
      state machine, and latitude/axis chart.
- [x] Define validation rules for each class.
- [x] Define when SVG is superior to ASCII, using atlas precedent.
- [x] Add Da Vinci invariant candidates for canonical diagrams.
- [x] Produce a checklist agents can apply before calling a diagram polished.

## Evidence

- `artifacts/ASCII-PERFECTION-SPEC.md`

## Validation

```powershell
git diff --check
```

## Non-Goals

- Do not rewrite diagrams in this pulse.
- Do not build a parser before the spec is reviewed.
