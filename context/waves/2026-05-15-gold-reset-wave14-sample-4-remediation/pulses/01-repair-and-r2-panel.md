---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `geochemistry/05-CARBON-CYCLE.md`
- `geochemistry/07-WEATHERING-SOILS.md`
- `geochemistry/08-OCEAN-GEOCHEMISTRY.md`
- `geochemistry/09-PLANETARY-GEOCHEMISTRY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era Q&A
tables. Current Certified Gold requires diagnostic reader-task support with
caveats.

## Changes

| Guide | Repair |
|---|---|
| `geochemistry/05-CARBON-CYCLE.md` | Rebuilt the table around the Urey reaction, carbon isotope excursions, CCD, oxygenation, vitrinite reflectance, LIPs/OAEs, and kerogen. |
| `geochemistry/07-WEATHERING-SOILS.md` | Rebuilt the table around hydrolysis, CIA, olivine/quartz stability, saprolite, podzolization, silicate CO2 drawdown, laterites, and climate feedback. |
| `geochemistry/08-OCEAN-GEOCHEMISTRY.md` | Rebuilt the table around residence time, Redfield, biological pump, deep-water age, 230Th normalization, Sr isotopes, HNLC regions, and Cd/Ca. |
| `geochemistry/09-PLANETARY-GEOCHEMISTRY.md` | Rebuilt the table around CAIs, late veneer, delta 17O, lunar volatiles, KREEP, SNC meteorites, CC-NC dichotomy, and Widmanstatten patterns. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- geochemistry\05-CARBON-CYCLE.md geochemistry\07-WEATHERING-SOILS.md geochemistry\08-OCEAN-GEOCHEMISTRY.md geochemistry\09-PLANETARY-GEOCHEMISTRY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml geochemistry\05-CARBON-CYCLE.md geochemistry\07-WEATHERING-SOILS.md geochemistry\08-OCEAN-GEOCHEMISTRY.md geochemistry\09-PLANETARY-GEOCHEMISTRY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

