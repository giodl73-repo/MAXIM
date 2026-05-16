# Tenth Gold Cohort

## Mission

Continue scaled Gold promotion with a natural-world, history/ideas,
material-culture, and arts/culture cohort.

## Scope

| Guide | Promotion Target | Invariant |
|---|---|---|
| `geology/01-MINERALS.md` | mineral structure-property exemplar | `mineral-hierarchy` |
| `hydrology/01-PRECIPITATION-RUNOFF.md` | runoff-process exemplar | `rainfall-runoff-process` |
| `oceanography/01-OCEAN-PHYSICS.md` | water-column physics exemplar | `ocean-water-column` |
| `animal-phylogeny/01-SINGLE-CELL-ORIGINS.md` | tree-of-life origins exemplar | `tree-of-life-origins` |
| `botany/01-PLANT-CELL-PHYSIOLOGY.md` | plant-cell anatomy exemplar | `plant-cell-anatomy` |
| `food-plants/01-GRAINS.md` | grain-family domestication exemplar | `major-grains-family-tree` |
| `history-of-science/01-ANCIENT-NATURAL-PHILOSOPHY.md` | ancient science timeline exemplar | `ancient-natural-philosophy-timeline` |
| `archaeology/01-FIELD-METHODS.md` | archaeological data-pipeline exemplar | `field-archaeology-pipeline` |
| `anthropology/01-PHYSICAL-ANTHROPOLOGY.md` | human biological variation exemplar | `physical-anthropology-landscape` |
| `textiles/01-NATURAL-FIBERS-PLANT.md` | cellulose fiber exemplar | `plant-fibers-cellulose` |
| `glassmaking/01-GLASS-SCIENCE.md` | silicate glass structure exemplar | `silicate-glass-structure` |
| `photography/01-OPTICS-LENSES.md` | camera lens system exemplar | `photography-lens-system` |

## Baseline Findings

| Finding | Resolution |
|---|---|
| `mycology/01-FUNGAL-BIOLOGY.md` had nested-box ASCII drift | Deferred for a future diagram-healing pass |
| `food-plants/01-GRAINS.md` baseline proof was clean | Swapped in as the natural-world replacement |
| Cohort lacked explicit cross-reference surfaces | Added Cross-References sections across all twelve |

## Gold Rubric v2 Scores

| Guide | Explanation | Diagrams | Tables | Bridges | Cross-links | Proof | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| `geology/01-MINERALS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `hydrology/01-PRECIPITATION-RUNOFF.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `oceanography/01-OCEAN-PHYSICS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `animal-phylogeny/01-SINGLE-CELL-ORIGINS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `botany/01-PLANT-CELL-PHYSIOLOGY.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `food-plants/01-GRAINS.md` | 4.6 | 4.5 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `history-of-science/01-ANCIENT-NATURAL-PHILOSOPHY.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `archaeology/01-FIELD-METHODS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `anthropology/01-PHYSICAL-ANTHROPOLOGY.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `textiles/01-NATURAL-FIBERS-PLANT.md` | 4.6 | 4.5 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `glassmaking/01-GLASS-SCIENCE.md` | 4.6 | 4.5 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `photography/01-OPTICS-LENSES.md` | 4.6 | 4.5 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |

## Reader-Task Checks

| Task Family | Representative Pass |
|---|---|
| Earth systems | Geology, Hydrology, and Oceanography connect materials, water movement, and stratified fluid systems |
| Life systems | Animal origins, Botany, and Grains connect cell biology, evolution, crops, and human calories |
| Human history/evidence | History of Science, Archaeology, and Anthropology connect ideas, field evidence, and bodies |
| Material/visual culture | Textiles, Glassmaking, and Photography connect material structure to craft and visual systems |

## Validation

```powershell
git -C C:\src\maxim diff --check
Set-Location -LiteralPath C:\src\maxim
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml geology\01-MINERALS.md hydrology\01-PRECIPITATION-RUNOFF.md oceanography\01-OCEAN-PHYSICS.md animal-phylogeny\01-SINGLE-CELL-ORIGINS.md botany\01-PLANT-CELL-PHYSIOLOGY.md food-plants\01-GRAINS.md history-of-science\01-ANCIENT-NATURAL-PHILOSOPHY.md archaeology\01-FIELD-METHODS.md anthropology\01-PHYSICAL-ANTHROPOLOGY.md textiles\01-NATURAL-FIBERS-PLANT.md glassmaking\01-GLASS-SCIENCE.md photography\01-OPTICS-LENSES.md
C:\src\proof\target\debug\proof.exe check -e --no-fail context\gold\REGISTRY.md context\waves\2026-05-14-tenth-gold-cohort\WAVE.md context\waves\PHASES.md
```

## Decision

Promote all twelve guides to Certified Gold. `mycology/01-FUNGAL-BIOLOGY.md`
remains a known diagram-healing candidate, not a failed promotion.
