---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `biology/03-GENETICS.md`
- `biology/04-EVOLUTION.md`
- `biology/05-ECOLOGY.md`
- `biology/06-PHYSIOLOGY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
goal/question/physiological-goal selector tables. Current Certified Gold
requires diagnostic reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `biology/03-GENETICS.md` | Rebuilt the genetics table around knockout, base editing, CRISPRa/i, GWAS, RNA-seq, scRNA-seq, regulatory maps, inheritance, constraint, and epigenetic state. |
| `biology/04-EVOLUTION.md` | Rebuilt the evolution table around selection, HWE, allele spread, drift, phylogeny, molecular clocks, hybrid failure, evo-devo, coalescent history, and clade support. |
| `biology/05-ECOLOGY.md` | Rebuilt the ecology table around population decline, coexistence, primary-production limits, biodiversity, trophic energy, food-web stability, nutrient cycles, reserve sizing, trophic cascades, and metapopulation viability. |
| `biology/06-PHYSIOLOGY.md` | Rebuilt the physiology table around blood pressure, glucose, temperature, infection, acid-base, fight-or-flight, endocrine axes, kidney water balance, oxygen delivery, and immune memory. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- biology\03-GENETICS.md biology\04-EVOLUTION.md biology\05-ECOLOGY.md biology\06-PHYSIOLOGY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml biology\03-GENETICS.md biology\04-EVOLUTION.md biology\05-ECOLOGY.md biology\06-PHYSIOLOGY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

