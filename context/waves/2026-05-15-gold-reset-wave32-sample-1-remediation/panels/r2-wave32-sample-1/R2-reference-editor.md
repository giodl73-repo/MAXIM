# R2 Reference Editor Review - Gold Reset Wave 32 Sample 1

## Scope

| Guide | Invariant |
|---|---|
| `data-science/02-PANDAS.md` | `pandas-data-model` |
| `data-science/04-PYTORCH.md` | `pytorch-stack` |
| `data-science/05-MLOPS.md` | `mlops-lifecycle` |
| `data-science/06-AZURE-ML.md` | `azure-ml-platform` |

## Rubric Findings

| Guide | Score | Note |
|---|---:|---|
| `data-science/02-PANDAS.md` | 4.6 | Pandas now ends with diagnostic guidance for indexing, grouping, reshaping, joins, performance, and time-series edge cases. |
| `data-science/04-PYTORCH.md` | 4.6 | PyTorch now separates tool choice, tensor mechanics, gradient behavior, training-loop state, distributed scaling, and deployment format. |
| `data-science/05-MLOPS.md` | 4.6 | MLOps now distinguishes tracking, promotion, data versioning, serving, drift, feature stores, and retraining gates. |
| `data-science/06-AZURE-ML.md` | 4.6 | Azure ML now diagnoses compute, job packaging, AutoML, pipelines, endpoints, identity/network governance, and cost controls. |

## Adversarial Closure

| Concern | Closure |
|---|---|
| Cheat sheets were task lookup tables. | Rebuilt all four as diagnostic tables with caveats. |
| Pandas guidance needed failure-mode diagnosis. | Added assignment, cardinality, dtype/performance, and temporal caveats. |
| PyTorch guidance needed operational boundaries. | Added shape/device/dtype, gradient, mode, scaling, and inference caveats. |
| MLOps/Azure ML guidance risked tool shopping. | Reframed around reproducibility, promotion, platform boundaries, governance, and cost. |

No BLOCK or WARN findings remain for the scoped Gold claims.

