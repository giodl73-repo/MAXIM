---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `coral-reefs/03-SYMBIOSIS.md`
- `coral-reefs/04-REEF-ECOLOGY.md`
- `coral-reefs/05-BLEACHING.md`
- `coral-reefs/06-REEF-DIVERSITY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era Q&A
tables. Current Certified Gold requires diagnostic reader-task support with
caveats.

## Changes

| Guide | Repair |
|---|---|
| `coral-reefs/03-SYMBIOSIS.md` | Rebuilt the symbiosis table around zooxanthellae identity, energy budget, symbiont benefit, bleaching trigger, thermotolerant clades, shuffling, nutrient recycling, bleached color, and holobiont framing. |
| `coral-reefs/04-REEF-ECOLOGY.md` | Rebuilt the reef-ecology table around coral cover, CCA, herbivory, Diadema loss, parrotfish sand, phase shifts, Trapezia mutualism, cryptic diversity, night feeding, and mesophotic reefs. |
| `coral-reefs/05-BLEACHING.md` | Rebuilt the bleaching table around DHW, alerts, local thresholds, global events, GBR mortality, recovery windows, sensitive/resistant taxa, refugia, and 2 deg C projections. |
| `coral-reefs/06-REEF-DIVERSITY.md` | Rebuilt the reef-diversity table around Coral Triangle richness, Caribbean richness, province split, depth peak, Center of Origin, Acropora disease, Diadema mortality, SCTLD, endemism, and gradient caveats. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- coral-reefs\03-SYMBIOSIS.md coral-reefs\04-REEF-ECOLOGY.md coral-reefs\05-BLEACHING.md coral-reefs\06-REEF-DIVERSITY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml coral-reefs\03-SYMBIOSIS.md coral-reefs\04-REEF-ECOLOGY.md coral-reefs\05-BLEACHING.md coral-reefs\06-REEF-DIVERSITY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

