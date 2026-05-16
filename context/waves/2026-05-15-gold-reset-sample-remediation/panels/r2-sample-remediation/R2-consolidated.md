# R2 Consolidated - Sample Remediation

## Mechanical Gate

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml geology\05-PLATE-TECTONICS.md geotechnical-engineering\02-EFFECTIVE-STRESS.md glassmaking\04-FLOAT-GLASS.md
```

Result: pass. Output was checked for literal `FAIL`.

## Gold Dimension Scores

| Guide | Landscape | Layering | ASCII | Explanation | Decision | Confusion | Bridge | Cross-ref | Voice | Factual | Average | Decision |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `geology/05-PLATE-TECTONICS.md` | 4.8 | 4.6 | 4.6 | 4.6 | 4.5 | 4.5 | 4.7 | 4.6 | 4.7 | 4.6 | 4.6 | Certified Gold |
| `geotechnical-engineering/02-EFFECTIVE-STRESS.md` | 4.7 | 4.6 | 4.6 | 4.7 | 4.7 | 4.5 | 4.5 | 4.5 | 4.6 | 4.6 | 4.6 | Certified Gold |
| `glassmaking/04-FLOAT-GLASS.md` | 4.6 | 4.6 | 4.5 | 4.6 | 4.7 | 4.5 | 4.6 | 4.5 | 4.6 | 4.5 | 4.6 | Certified Gold |

## Reader-Task Checks

| Guide | Tasks | R2 Result |
|---|---|---|
| `geology/05-PLATE-TECTONICS.md` | Explain why plate tectonics unified geology; infer boundary type from observations; connect seafloor spreading to Wilson cycle; separate boundary volcanism from plume exceptions; follow tectonics into ore systems and planetary comparison | Pass |
| `geotechnical-engineering/02-EFFECTIVE-STRESS.md` | Compute effective stress; diagnose drawdown settlement; choose Ko vs active/passive framing; detect piping risk; decide what field monitoring must close | Pass |
| `glassmaking/04-FLOAT-GLASS.md` | Explain the float revolution; map ribbon to product families; choose hard vs soft coat; choose safety/thermal/acoustic products by use case; identify tin-side relevance | Pass |

## Adversarial Review

| Lens | Result |
|---|---|
| reference-editor | No remaining BLOCK/WARN; decision surfaces now answer real use cases |
| ascii-cartographer | Protected figures remain proof-clean; added maps improve conceptual work without ASCII failures |
| expert-skeptic | Mechanism, field-uncertainty, safety/code, and climate caveats are now explicit |
| bridge-builder | Universal conceptual bridges now carry the old-world/new-world model rather than stack-specific flavor |
| index-weaver | Cross-links now deepen navigation beyond local adjacency |

## Registry Decision

Restore the three scoped guides to Current Certified Gold. This is a reset-era
certification backed by repair, proof, guide-specific scoring, adversarial
review, and reader-task checks; it does not restore any other factory guide.

