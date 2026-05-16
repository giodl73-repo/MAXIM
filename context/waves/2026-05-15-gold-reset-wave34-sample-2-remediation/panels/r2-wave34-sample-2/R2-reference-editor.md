# R2 Reference Editor Review - Gold Reset Wave 34 Sample 2

## Scope

| Guide | Invariant |
|---|---|
| `energy-systems/09-HYDROPOWER.md` | `hydropower-landscape` |
| `energy-systems/10-GRID-DISPATCH.md` | `grid-dispatch-job-scheduling` |
| `entomology/00-OVERVIEW.md` | `arthropod-tree-of-life` |

## Rubric Findings

### `energy-systems/09-HYDROPOWER.md`

| Dimension | Score | Note |
|---|---:|---|
| Landscape | 4.6 | Reservoir, run-of-river, pumped hydro, turbines, economics, environment, and climate risk are coherently mapped. |
| Diagrams | 4.6 | Hydropower landscape remains proof-clean and useful. |
| Conceptual accuracy | 4.6 | Dispatchability and black-start claims are narrowed to reservoir/many-plant cases; run-of-river wording is corrected. |
| Peer tone | 4.6 | Treats hydro as hydraulic infrastructure plus grid service plus river intervention. |
| Bridges | 4.6 | Storage/buffer, backpressure, and bottleneck bridges remain useful. |
| Decision support | 4.7 | Cheat sheet now diagnoses grid value, turbine choice, economics, pumped storage, methane, fish passage, and climate risk. |

Decision: PASS at 4.6.

### `energy-systems/10-GRID-DISPATCH.md`

| Dimension | Score | Note |
|---|---:|---|
| Landscape | 4.6 | Merit order, unit commitment, BESS dispatch, curtailment, demand response, seasonal storage, and markets are integrated. |
| Diagrams | 4.5 | Dispatch/job-scheduling invariant remains proof-clean. |
| Conceptual accuracy | 4.6 | Optimization and BESS/peaker claims are caveated; data-center DR is tied to workload separability. |
| Peer tone | 4.7 | The guide retains senior scheduling/optimization analogies without oversimplifying ISO practice. |
| Bridges | 4.7 | Constraint-aware scheduling and cache/buffer analogies are strong. |
| Decision support | 4.7 | Cheat sheet now diagnoses dispatch, commitment, clearing price, VRE, BESS, seasonal storage, missing money, curtailment, and dark-doldrum claims. |

Decision: PASS at 4.6.

### `entomology/00-OVERVIEW.md`

| Dimension | Score | Note |
|---|---:|---|
| Landscape | 4.6 | Arthropod relationships, insect definition, orders, abundance, roles, timeline, and library organization are clear. |
| Diagrams | 4.6 | Arthropod tree-of-life invariant remains proof-clean. |
| Conceptual accuracy | 4.6 | Biomass and decline claims are caveated; termite classification is corrected. |
| Peer tone | 4.6 | Maintains the collector-frame style without overclaiming. |
| Bridges | 4.5 | Identification-key to decision-tree bridge remains effective. |
| Decision support | 4.7 | Cheat sheet now diagnoses insect identity, hexapod distinctions, order ID, beetle dominance, metamorphosis, pollination, decline, and termite classification. |

Decision: PASS at 4.6.

## Adversarial Closure

| Concern | Closure |
|---|---|
| All three guides ended with lookup tables rather than diagnostic decision support. | Decision Cheat Sheets were rebuilt as diagnostic tables with caveats. |
| Hydropower guide overclaimed renewables dispatchability and black-start uniqueness. | Reframed around reservoir storage and many-plant black-start capability. |
| Grid-dispatch guide overstated BESS replacement and data-center flexibility. | Added duration, fuel-availability, workload-separability, and service-level caveats. |
| Entomology guide overclaimed biomass/dominance and simplified insect-decline literature. | Reframed dominance around terrestrial diversity/function and decline around metric/region/taxon. |
| Termite classification wording was too specific and potentially wrong. | Reframed termites as infraorder Isoptera within Blattodea. |

No BLOCK or WARN findings remain for the scoped Gold claims.

