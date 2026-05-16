---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `behavioral-economics/08-MARKET-ANOMALIES.md`
- `statistics-applied/01-EXPERIMENTAL-DESIGN.md`
- `statistics-applied/02-AB-TESTING.md`
- `statistics-applied/04-BAYESIAN-PRACTICE.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
answer-key and implication tables. Current Certified Gold requires diagnostic
reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `behavioral-economics/08-MARKET-ANOMALIES.md` | Rebuilt the anomaly table around behavioral mechanisms, risk-vs-mispricing caveats, publication decay, and institutional variation. |
| `statistics-applied/01-EXPERIMENTAL-DESIGN.md` | Rebuilt the design answer key around power, concealment, ITT, cluster design, factorial aliasing, crossover suitability, and interim monitoring. |
| `statistics-applied/02-AB-TESTING.md` | Rebuilt the A/B testing answer key around SRM, CUPED, novelty/primacy, bandits, multiplicity, mSPRT, and cluster power. |
| `statistics-applied/04-BAYESIAN-PRACTICE.md` | Rebuilt the Bayesian practice answer key around priors, convergence, NUTS, divergences, pooling, Bayesian A/B, and model comparison. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- behavioral-economics\08-MARKET-ANOMALIES.md statistics-applied\01-EXPERIMENTAL-DESIGN.md statistics-applied\02-AB-TESTING.md statistics-applied\04-BAYESIAN-PRACTICE.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml behavioral-economics\08-MARKET-ANOMALIES.md statistics-applied\01-EXPERIMENTAL-DESIGN.md statistics-applied\02-AB-TESTING.md statistics-applied\04-BAYESIAN-PRACTICE.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

