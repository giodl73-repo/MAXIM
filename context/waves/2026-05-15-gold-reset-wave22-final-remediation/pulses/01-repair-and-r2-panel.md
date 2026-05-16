---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `ethics/03-DEONTOLOGY.md`
- `ethics/04-VIRTUE-ETHICS.md`
- `ethics/05-RAWLS.md`
- `ethics/06-APPLIED-ETHICS.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
concept and domain selector tables. Current Certified Gold requires diagnostic
reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `ethics/03-DEONTOLOGY.md` | Rebuilt the deontology concept table around Kantian motivation, imperative tests, humanity, duties, side constraints, thresholds, and separateness. |
| `ethics/04-VIRTUE-ETHICS.md` | Rebuilt the virtue ethics concept table around eudaimonia, function, mean, virtue, phronesis, habituation, Stoicism, MacIntyre, and Foot. |
| `ethics/05-RAWLS.md` | Rebuilt the Rawls concept table around original position, veil, primary goods, principles, maximin, reflective equilibrium, consensus, and public reason. |
| `ethics/06-APPLIED-ETHICS.md` | Rebuilt the applied ethics domain table around bioethics, consent, end-of-life, abortion arguments, enhancement, professional ethics, allocation, safety, whistleblowing, and journalism. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- ethics\03-DEONTOLOGY.md ethics\04-VIRTUE-ETHICS.md ethics\05-RAWLS.md ethics\06-APPLIED-ETHICS.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml ethics\03-DEONTOLOGY.md ethics\04-VIRTUE-ETHICS.md ethics\05-RAWLS.md ethics\06-APPLIED-ETHICS.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

