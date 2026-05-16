---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `remote-sensing/04-LIDAR.md`
- `remote-sensing/05-SATELLITE-ORBITS.md`
- `remote-sensing/06-IMAGE-PROCESSING.md`
- `remote-sensing/07-INSAR.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
application, requirement, task, and approach selector tables. Current Certified
Gold requires diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `remote-sensing/04-LIDAR.md` | Rebuilt the LiDAR table around hydrology DEMs, forest structure, bathymetry, buildings, corridors, space LiDAR, cliff change, and archaeology. |
| `remote-sensing/05-SATELLITE-ORBITS.md` | Rebuilt the orbits table around global optical revisit, constellations, Sentinel-2, Landsat, GEO weather, commercial tasking, SAR, NISAR, cryosphere, and ocean/SST coverage. |
| `remote-sensing/06-IMAGE-PROCESSING.md` | Rebuilt the processing table around atmospheric correction, surface reflectance, aquatic algorithms, random forests, CNNs, global products, time-series change, and SAR disaster proxies. |
| `remote-sensing/07-INSAR.md` | Rebuilt the InSAR table around coseismic slip, volcanoes, subsidence, infrastructure, agriculture, DEMs, landslides, and disaster damage proxies. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- remote-sensing\04-LIDAR.md remote-sensing\05-SATELLITE-ORBITS.md remote-sensing\06-IMAGE-PROCESSING.md remote-sensing\07-INSAR.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml remote-sensing\04-LIDAR.md remote-sensing\05-SATELLITE-ORBITS.md remote-sensing\06-IMAGE-PROCESSING.md remote-sensing\07-INSAR.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

