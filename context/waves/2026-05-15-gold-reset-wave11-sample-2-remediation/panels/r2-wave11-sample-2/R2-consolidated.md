# R2 Consolidated Panel - Gold Reset Wave 11 Sample 2

## Verdict

PASS. The Wave 11 cancer drugs, bacterial disease, viral disease, and
fungal/parasitic/prion disease sample satisfies Gold Rubric v2 after targeted
repair, proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `medicine/06-CANCER-DRUGS.md` | 4.6 | `cancer-drug-mechanisms` | Certified Gold |
| `disease/01-BACTERIAL.md` | 4.6 | `bacterial-disease-gram-classification` | Certified Gold |
| `disease/02-VIRAL.md` | 4.6 | `viral-disease-baltimore` | Certified Gold |
| `disease/03-FUNGAL-PARASITIC-PRION.md` | 4.6 | `fungal-parasitic-prion-classes` | Certified Gold |

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
| `medicine/06-CANCER-DRUGS.md` | Diagnose cancer-drug choices by separating oncogenic driver, biomarker, resistance, pathway dependence, and toxicity caveat. | PASS |
| `disease/01-BACTERIAL.md` | Diagnose bacterial disease logic by separating envelope class, resistance mechanism, toxin mechanism, antibiotic-risk exception, treatment exception, and biofilm persistence. | PASS |
| `disease/02-VIRAL.md` | Diagnose viral disease logic by separating genome polarity, latent reservoir, reassortment, antiviral activation, release inhibition, and SVR cure definition. | PASS |
| `disease/03-FUNGAL-PARASITIC-PRION.md` | Diagnose fungal/parasitic/prion disease by separating drug targets, morphology, parasite latency, CD4 control, cure limits, and PrP templating. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

