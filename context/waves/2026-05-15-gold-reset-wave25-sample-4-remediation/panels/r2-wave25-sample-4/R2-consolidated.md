# R2 Consolidated Panel - Gold Reset Wave 25 Sample 4

## Verdict

PASS. The Wave 25 biomedical-engineering sample satisfies Gold Rubric v2 after
targeted repair, proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `biomedical-engineering/05-NEURAL-INTERFACES.md` | 4.6 | `neural-interface-signal-hierarchy` | Certified Gold |
| `biomedical-engineering/06-PROSTHETICS.md` | 4.6 | `prosthetics-landscape` | Certified Gold |
| `biomedical-engineering/07-MEDICAL-DEVICES.md` | 4.6 | `medical-device-regulatory-framework` | Certified Gold |
| `biomedical-engineering/08-TISSUE-ENGINEERING.md` | 4.6 | `tissue-engineering-landscape` | Certified Gold |

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
| `biomedical-engineering/05-NEURAL-INTERFACES.md` | Diagnose neural-interface choices by separating density, invasiveness, stability, clinical maturity, therapy programming, restoration limits, in-vitro simplification, and modality complementarity. | PASS |
| `biomedical-engineering/06-PROSTHETICS.md` | Diagnose prosthetic recommendations by separating activity level, limb level, safety, cost, balance training, control signal availability, sport specificity, rehab use, and osseointegration. | PASS |
| `biomedical-engineering/07-MEDICAL-DEVICES.md` | Diagnose regulatory strategy by separating exemption, predicate, De Novo, PMA, Special 510(k), significant changes, IDE, combination products, SaMD, and international QMS. | PASS |
| `biomedical-engineering/08-TISSUE-ENGINEERING.md` | Diagnose tissue-engineering strategy by separating scaffold mechanics, cell source, immune strategy, organoids, chips, vascularization, bioreactors, and combination-product evidence. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

