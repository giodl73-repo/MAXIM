# R2 Consolidated Panel - Gold Reset Wave 25 Sample 3

## Verdict

PASS. The Wave 25 mixed astrobiology/biomedical sample satisfies Gold Rubric v2
after targeted repair, proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `astrobiology/09-FUTURE-MISSIONS.md` | 4.6 | `astrobiology-mission-pipeline` | Certified Gold |
| `biomedical-engineering/02-BIOMATERIALS.md` | 4.6 | `biomaterials-landscape` | Certified Gold |
| `biomedical-engineering/03-MEDICAL-IMAGING.md` | 4.6 | `medical-imaging-modalities` | Certified Gold |
| `biomedical-engineering/04-BIOSENSORS.md` | 4.6 | `biosensor-architecture` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all four scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: selector-table issues repaired |
| Reader-task check | PASS: all four guides support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `astrobiology/09-FUTURE-MISSIONS.md` | Diagnose mission claims by separating target body, mission purpose, life-detection capability, program risk, contamination, and evidence limits. | PASS |
| `biomedical-engineering/02-BIOMATERIALS.md` | Diagnose biomaterial selection by separating application, material, mechanical fit, biological response, degradation, imaging, and failure modes. | PASS |
| `biomedical-engineering/03-MEDICAL-IMAGING.md` | Diagnose imaging modality choice by separating clinical question, speed, contrast, radiation, contraindications, artifacts, and diagnostic limits. | PASS |
| `biomedical-engineering/04-BIOSENSORS.md` | Diagnose biosensor platform choice by separating analyte, transduction, platform, drift, contamination, calibration, artifacts, and interpretation limits. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

