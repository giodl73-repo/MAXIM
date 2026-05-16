---
wave: pilot-gold-rescore
date_open: 2026-05-14
date_close: 2026-05-14
status: complete
source_wave: maxim-quality-control-spine
---

# Pilot Gold Rescore

## Mission

Run a second Gold panel on the five pilot guides after remediation and Da Vinci
coverage, and separate true Gold claims from still-useful Gold candidates.

## Mechanical Gate

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail computing\01-PACKAGE.md distributed-systems\03-CONSENSUS.md periodic-table\01-HYDROGEN.md music-theory\01-PITCH-SCALES.md atlas\02-GLOBAL-WINDS.md
```

Result: pass.

## R2 Score Table

| Guide | Tier | Average | Decision |
|---|---:|---:|---|
| `computing/01-PACKAGE.md` | Gold | 4.8 | model guide; now protected by Da Vinci invariant |
| `distributed-systems/03-CONSENSUS.md` | Gold | 4.7 | internals claim now earned by Paxos and Raft traces |
| `atlas/02-GLOBAL-WINDS.md` | Gold-candidate | 4.5 | strong; needs atlas-specific map/SVG invariant pass before hard Gold claim |
| `periodic-table/01-HYDROGEN.md` | Gold-candidate | 4.4 | bridge placement fixed; dense guide still wants one more visual/decision polish pass |
| `music-theory/01-PITCH-SCALES.md` | Silver+ | 4.1 | inversion fixed; cross-reference and notation polish still below Gold |

## Dimension Scores

| Dimension | Package | Consensus | Hydrogen | Pitch | Winds |
|---|---:|---:|---:|---:|---:|
| Landscape power | 5 | 4 | 5 | 4 | 5 |
| Layering integrity | 5 | 5 | 5 | 4 | 5 |
| ASCII precision | 5 | 5 | 4 | 4 | 5 |
| Explanatory compression | 5 | 5 | 4 | 4 | 4 |
| Decision utility | 5 | 5 | 4 | 4 | 5 |
| Confusion handling | 5 | 5 | 5 | 4 | 4 |
| Bridge quality | 5 | 4 | 5 | 4 | 4 |
| Cross-reference value | 4 | 4 | 4 | 3 | 4 |
| Voice | 5 | 5 | 4 | 4 | 5 |
| Factual confidence | 4 | 5 | 4 | 4 | 4 |

## Reader Task Results

| Guide | Reader Tasks Pass? | Notes |
|---|---|---|
| Package | yes | Explains nesting, tool choice, registry/manager/lockfile confusion |
| Consensus | yes | Now answers both "why consensus" and "how safety survives races/divergence" |
| Hydrogen | mostly | Excellent cross-domain utility; one more mechanism diagram would improve decision speed |
| Pitch | mostly | Math and interval tasks pass; guide needs stronger onward paths/cross-links |
| Winds | yes | Practical weather/navigation tasks pass; atlas-specific visual validation remains separate |

## Carry-Forwards

1. Add atlas/SVG invariants before calling `atlas/02-GLOBAL-WINDS.md` hard Gold.
   Closed by `atlas-map-invariants`.
2. Give Hydrogen one more mechanism-level visual polish pass. Closed by
   `gold-candidate-polish`.
3. Add cross-reference/onward-path polish to Pitch before a Gold claim. Closed by
   `gold-candidate-polish`.

## Closeout

The pilot moved from "does the rubric work?" to "which guides can honestly
claim Gold?" Two guides can: Package and Consensus. Three remain high-quality
candidates with explicit next actions.
