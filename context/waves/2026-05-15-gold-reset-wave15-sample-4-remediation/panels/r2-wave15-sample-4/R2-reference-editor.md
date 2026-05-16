# R2 Reference Editor Panel - Gold Reset Wave 15 Sample 4

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `remote-sensing/04-LIDAR.md` | `lidar-taxonomy` | 4.6 |
| `remote-sensing/05-SATELLITE-ORBITS.md` | `satellite-orbit-altitude-classes` | 4.6 |
| `remote-sensing/06-IMAGE-PROCESSING.md` | `remote-image-processing-layers` | 4.6 |
| `remote-sensing/07-INSAR.md` | `insar-geometry` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | Factory-era selector tables were too lookup-oriented. | Repaired into diagnostic `If you need to diagnose...` tables. |
| expert-skeptic | Remote-sensing guidance needs caveats about ground filtering, biomass saturation, bathymetric limits, revisit versus repeat, surface-reflectance assumptions, training data, phase unwrapping, atmosphere, and coherence proxies. | Added caveats for each diagnostic claim. |
| bridge-builder | Existing guide bodies already bridge sensor geometry, orbit design, image pipelines, and deformation measurement to applied decisions. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `remote-sensing/04-LIDAR.md` | Reader can diagnose LiDAR use by separating airborne, bathymetric, mobile, terrestrial, and spaceborne choices with density, filtering, calibration, and registration caveats. |
| `remote-sensing/05-SATELLITE-ORBITS.md` | Reader can diagnose orbit choice by separating SSO, LEO constellations, GEO, commercial tasking, SAR repeat, polar coverage, and thermal/ocean limits. |
| `remote-sensing/06-IMAGE-PROCESSING.md` | Reader can diagnose processing pipelines by separating correction, classification, pre-existing products, time-series change, and rapid SAR proxies. |
| `remote-sensing/07-INSAR.md` | Reader can diagnose InSAR applications by separating single-pair, time-series, PS, SBAS, DEM, coherence-change, atmosphere, and LOS limitations. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

