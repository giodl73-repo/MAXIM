---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

Repair and certify the sixth Wave 35 reset sample:

- `finance/02-DERIVATIVES.md`
- `finance/03-FIXED-INCOME.md`
- `finance/04-RISK-MODELS.md`

## Pre-implementation Scout

Command:

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml finance\02-DERIVATIVES.md finance\03-FIXED-INCOME.md finance\04-RISK-MODELS.md
```

Scout result: proof-clean with Da Vinci invariants present. Editorial review
found Gold-blocking issues around lookup-style cheat sheets, fixed-income
bootstrap indexing, stale TIPS examples, VaR convention mixing, and FRTB
currentness.

## Changes

| Guide | Repair |
|---|---|
| `finance/02-DERIVATIVES.md` | Rebuilt the cheat sheet around derivatives diagnostics: pricing, hedging, exercise, exotics, Greeks, skew, and swaps. |
| `finance/03-FIXED-INCOME.md` | Corrected bootstrap maturity example, caveated TIPS ranges, and rebuilt the cheat sheet around curve/risk diagnostics. |
| `finance/04-RISK-MODELS.md` | Corrected VaR horizon/convention wording, historical VaR percentile, FRTB currentness, and rebuilt the cheat sheet diagnostically. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- finance\02-DERIVATIVES.md finance\03-FIXED-INCOME.md finance\04-RISK-MODELS.md
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml finance\02-DERIVATIVES.md finance\03-FIXED-INCOME.md finance\04-RISK-MODELS.md | Tee-Object -Variable proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

