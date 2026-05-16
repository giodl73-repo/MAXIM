# R1 Consolidated - First Reset Panel

## Panel Scope

This panel tests the reset doctrine against three guides previously promoted by
Gold Factory Wave 37. The question is not "are these useful?" They are useful.
The question is whether factory hardening plus uniform 4.6 scores is enough to
restore Certified Gold. It is not.

## Mechanical Prerequisite

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml geology\05-PLATE-TECTONICS.md geotechnical-engineering\02-EFFECTIVE-STRESS.md glassmaking\04-FLOAT-GLASS.md
```

Result: pass. Output was checked for literal `FAIL`.

## Gold Dimension Scores

| Guide | Landscape | Layering | ASCII | Explanation | Decision | Confusion | Bridge | Cross-ref | Voice | Factual | Average | Decision |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `geology/05-PLATE-TECTONICS.md` | 3.8 | 4.4 | 4.0 | 4.4 | 4.2 | 4.4 | 4.5 | 4.0 | 4.6 | 4.1 | 4.2 | Candidate-Hardened |
| `geotechnical-engineering/02-EFFECTIVE-STRESS.md` | 4.6 | 4.4 | 4.5 | 4.5 | 3.9 | 4.3 | 4.0 | 4.1 | 4.5 | 4.1 | 4.3 | Candidate-Hardened |
| `glassmaking/04-FLOAT-GLASS.md` | 4.0 | 4.3 | 4.0 | 4.5 | 3.8 | 4.3 | 4.2 | 4.0 | 4.4 | 4.1 | 4.2 | Candidate-Hardened |

## Reader-Task Checks

| Guide | Tasks Tested | Result |
|---|---|---|
| `geology/05-PLATE-TECTONICS.md` | Identify boundary type from observations; explain seafloor spreading evidence; distinguish transform fault from fracture zone; place Wilson-cycle stage | Passes candidate level; opening diagram does not yet make the whole system navigable at Gold level |
| `geotechnical-engineering/02-EFFECTIVE-STRESS.md` | Compute effective stress; reason about groundwater drawdown settlement; identify piping risk; choose which stress-path concept matters | Passes candidate level; needs a stronger design/diagnostic cheat sheet |
| `glassmaking/04-FLOAT-GLASS.md` | Explain why float displaced plate glass; choose hard vs soft Low-E; identify tin side relevance; reason about IGU surface numbering | Passes candidate level; needs application-driven product selection and safety/code caveats |

## Consolidated Findings

| Finding | Severity | Affected Guide |
|---|---|---|
| Plate tectonics opening map is useful but underspecified | WARN | `geology/05-PLATE-TECTONICS.md` |
| Plate tectonics figure is a category panel, not a system diagram | WARN | `geology/05-PLATE-TECTONICS.md` |
| Plate tectonics needs tighter caveats around debated mechanisms | WARN | `geology/05-PLATE-TECTONICS.md` |
| Effective Stress needs a stronger decision surface | WARN | `geotechnical-engineering/02-EFFECTIVE-STRESS.md` |
| Effective Stress should distinguish conceptual formula from field uncertainty | WARN | `geotechnical-engineering/02-EFFECTIVE-STRESS.md` |
| Float Glass cheat sheet is fact recall, not enough selection logic | WARN | `glassmaking/04-FLOAT-GLASS.md` |
| Float Glass process map is linear but not layered | WARN | `glassmaking/04-FLOAT-GLASS.md` |
| Float Glass has strong facts but needs product-risk caveats | WARN | `glassmaking/04-FLOAT-GLASS.md` |
| Float Glass bridge quality is implicit | WARN | `glassmaking/04-FLOAT-GLASS.md` |

## Registry Decision

| Guide | Prior Factory Claim | Reset-Era Decision | Next Gate |
|---|---|---|---|
| `geology/05-PLATE-TECTONICS.md` | Certified Gold in Wave 37 | Candidate-Hardened | Repair WARN findings, then re-panel |
| `geotechnical-engineering/02-EFFECTIVE-STRESS.md` | Certified Gold in Wave 37 | Candidate-Hardened | Repair WARN findings, then re-panel |
| `glassmaking/04-FLOAT-GLASS.md` | Certified Gold in Wave 37 | Candidate-Hardened | Repair WARN findings, then re-panel |

## Conclusion

The reset gate is working. These guides are not "lite polish"; they are strong
candidate-hardened guides. But Certified Gold now requires deeper guide-specific
editorial excellence than proof, Cross-References, Da Vinci invariants, and
uniform cohort scores can demonstrate.

