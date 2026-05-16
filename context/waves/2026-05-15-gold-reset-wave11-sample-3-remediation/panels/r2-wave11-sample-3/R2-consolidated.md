# R2 Consolidated Panel - Gold Reset Wave 11 Sample 3

## Verdict

PASS. The Wave 11 cancer, cardiovascular disease, metabolic/endocrine disease,
and autoimmune/inflammatory disease sample satisfies Gold Rubric v2 after
targeted repair, proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `disease/04-CANCER.md` | 4.6 | `cancer-hallmarks-landscape` | Certified Gold |
| `disease/05-CARDIOVASCULAR-DISEASE.md` | 4.6 | `cardiovascular-disease-atherosclerosis` | Certified Gold |
| `disease/06-METABOLIC-ENDOCRINE.md` | 4.6 | `metabolic-endocrine-feedback-failure` | Certified Gold |
| `disease/07-AUTOIMMUNE-INFLAMMATORY.md` | 4.6 | `autoimmune-tolerance-failure-mechanisms` | Certified Gold |

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
| `disease/04-CANCER.md` | Diagnose cancer mechanisms by separating two-hit logic, PARP/BRCA synthetic lethality, fusion kinase, MSI-H immunotherapy, Warburg metabolism, and translocation risk. | PASS |
| `disease/05-CARDIOVASCULAR-DISEASE.md` | Diagnose cardiovascular mechanisms by separating ACS categories, reperfusion urgency, HFrEF therapy, AF stroke prevention, QT risk, and aldosterone screening. | PASS |
| `disease/06-METABOLIC-ENDOCRINE.md` | Diagnose metabolic/endocrine disease by separating DKA/HHS, thyroid autoimmunity, pheo sequencing, adrenal axis, DKA potassium, and crystal analysis. | PASS |
| `disease/07-AUTOIMMUNE-INFLAMMATORY.md` | Diagnose autoimmune/inflammatory disease by separating RA, SLE, MS, IBD, anti-TNF, and HLA-B27 caveats. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

