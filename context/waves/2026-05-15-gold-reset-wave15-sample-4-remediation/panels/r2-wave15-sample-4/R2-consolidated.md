# R2 Consolidated Panel - Gold Reset Wave 15 Sample 4

## Verdict

PASS. The Wave 15 LiDAR/satellite-orbits/image-processing/InSAR sample
satisfies Gold Rubric v2 after targeted repair, proof/Da Vinci validation, and
guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `remote-sensing/04-LIDAR.md` | 4.6 | `lidar-taxonomy` | Certified Gold |
| `remote-sensing/05-SATELLITE-ORBITS.md` | 4.6 | `satellite-orbit-altitude-classes` | Certified Gold |
| `remote-sensing/06-IMAGE-PROCESSING.md` | 4.6 | `remote-image-processing-layers` | Certified Gold |
| `remote-sensing/07-INSAR.md` | 4.6 | `insar-geometry` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all four scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: selector table issues repaired |
| Reader-task check | PASS: all four guides support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `remote-sensing/04-LIDAR.md` | Diagnose LiDAR modality by separating terrain, canopy, bathymetry, buildings, corridors, global sampling, change detection, and archaeology constraints. | PASS |
| `remote-sensing/05-SATELLITE-ORBITS.md` | Diagnose orbit architecture by separating revisit, swath, constellation, archive, GEO, commercial, SAR, polar, and thermal/ocean tradeoffs. | PASS |
| `remote-sensing/06-IMAGE-PROCESSING.md` | Diagnose remote-image workflows by separating correction, classification, product reuse, archive change detection, and SAR disaster mapping. | PASS |
| `remote-sensing/07-INSAR.md` | Diagnose InSAR use by separating deformation type, time baseline, sensor choice, phase, LOS, atmosphere, and coherence caveats. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

