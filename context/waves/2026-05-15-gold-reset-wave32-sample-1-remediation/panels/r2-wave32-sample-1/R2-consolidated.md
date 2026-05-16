# R2 Consolidated Panel - Gold Reset Wave 32 Sample 1

## Verdict

PASS. The Wave 32 data-science sample satisfies Gold Rubric v2 after targeted
repair, proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `data-science/02-PANDAS.md` | 4.6 | `pandas-data-model` | Certified Gold |
| `data-science/04-PYTORCH.md` | 4.6 | `pytorch-stack` | Certified Gold |
| `data-science/05-MLOPS.md` | 4.6 | `mlops-lifecycle` | Certified Gold |
| `data-science/06-AZURE-ML.md` | 4.6 | `azure-ml-platform` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all four scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: lookup-table and tool-shopping issues repaired |
| Reader-task check | PASS: all four guides support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `data-science/02-PANDAS.md` | Diagnose a Pandas problem by separating selection semantics, grouping output shape, reshape uniqueness, join cardinality, performance, and time handling. | PASS |
| `data-science/04-PYTORCH.md` | Diagnose a PyTorch problem by separating tool fit, shape/device/dtype, autograd, training mode, distributed scaling, and inference format. | PASS |
| `data-science/05-MLOPS.md` | Diagnose an MLOps claim by separating reproducibility, model promotion, data versioning, serving boundary, drift, feature ownership, and retraining gates. | PASS |
| `data-science/06-AZURE-ML.md` | Diagnose an Azure ML platform choice by separating compute, job packaging, AutoML fit, pipeline boundary, endpoint mode, governance, and cost controls. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

