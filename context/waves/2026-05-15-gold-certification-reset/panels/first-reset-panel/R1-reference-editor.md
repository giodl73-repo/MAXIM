# R1 - reference-editor

## Scope

| Guide | Review Lens |
|---|---|
| `geology/05-PLATE-TECTONICS.md` | Style contract, layering, decision usefulness |
| `geotechnical-engineering/02-EFFECTIVE-STRESS.md` | Style contract, calculation path, decision usefulness |
| `glassmaking/04-FLOAT-GLASS.md` | Style contract, manufacturing-process layering, decision usefulness |

## Findings

### F-01 - WARN: Plate tectonics opening map is useful but underspecified
File: `geology/05-PLATE-TECTONICS.md`
Finding: The guide has strong sections and a real landscape diagram, but the
opening map compresses a large theory into boundary types plus driving forces.
It does not visually connect evidence, boundary processes, products, Wilson
cycle, hotspots, and diagnostic observations.
Consequence: The guide is useful, but the first figure does not yet carry the
"grand unified theory" claim at Certified Gold level.
Fix: Rework the opening diagram into a layered system map: observations ->
plate motions -> boundary regimes -> geologic products -> diagnostic field
signals.

### F-02 - WARN: Effective Stress needs a stronger decision surface
File: `geotechnical-engineering/02-EFFECTIVE-STRESS.md`
Finding: The guide explains the master equation, stress profiles, seepage,
piping, and uplift well, but the decision cheat sheet is mostly a calculation
index. It does not fully separate field diagnosis, lab test interpretation,
construction sequencing, and failure-mode triage.
Consequence: A practicing reader gets formulas but not enough "which model do I
reach for under which field condition?" guidance for Gold.
Fix: Split the cheat sheet into diagnostic, calculation, and design-action rows.

### F-03 - WARN: Float Glass cheat sheet is fact recall, not enough selection logic
File: `glassmaking/04-FLOAT-GLASS.md`
Finding: The process explanation is dense and useful, but the decision cheat
sheet mostly answers single facts. It does not strongly decide among float,
tempered, laminated, coated, IGU, hard-coat, and soft-coat options by use case.
Consequence: The guide is a strong candidate, but the end-state decision surface
falls below Gold's "what do I use when?" bar.
Fix: Add application-driven rows: ordinary glazing, safety location, museum
case, hot climate facade, cold climate residential, acoustic glazing, and
post-temper coating constraints.

## Summary

All three guides remain Candidate-Hardened. They satisfy the style floor and
mechanical prerequisites, but each has at least one WARN-level decision or
landscape issue that blocks Certified Gold.

