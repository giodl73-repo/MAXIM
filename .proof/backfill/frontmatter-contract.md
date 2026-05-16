# MAXIM frontmatter contract

Frontmatter is introduced during PROOF backfill, one module at a time. It exists
to make MAXIM queryable as a source corpus without breaking the human-readable
library layout.

## Required fields

Every backfilled Markdown file gets:

```yaml
---
maxim_schema: maxim.frontmatter.v1
id: maxim:<module>:<slug>
kind: guide
module: computing-software
section: computing-software
title: Package Management Systems
status: source-custody
source_custody: needs-source
current_path: computing/01-PACKAGE.md
canonical_path: computing/01-PACKAGE.md
backsource_ids: []
concepts: []
root_concepts: []
index_roles: []
remap_from: []
remap_to: []
updated: null
---
```

## `kind`

| Kind | Use | Examples |
|---|---|---|
| `guide` | A normal explanatory guide. | `computing/01-PACKAGE.md` |
| `module-index` | A module table of contents or status file. | `computing/STATUS.md` |
| `section-index` | A section landing page that groups modules. | `sections/computing-software.md` |
| `concept-index` | A cross-module concept index. | `CONCEPT-INDEX.md` |
| `source-record` | A backsource/provenance note under `.proof/backfill/sources/`. | `.proof/backfill/sources/computing-software/...` |
| `generated-pack` | Generated CROP/PEBBLE/FLETCH artifact metadata. | `.crop/packs/...` |

## Concept fields

| Field | Meaning |
|---|---|
| `concepts` | Concepts substantively discussed in this file. |
| `root_concepts` | Concepts for which this file is a canonical/root explanation. |
| `index_roles` | Roles this file plays in generated views: `toc`, `status`, `concept-index`, `source-map`, `volume-map`, `bridge-map`. |

Use `root_concepts` sparingly. A concept should have one primary root per module
unless the domain genuinely needs multiple roots.

## Source custody fields

| Field | Meaning |
|---|---|
| `source_custody` | `needs-source`, `partial`, `verified`, or `generated`. |
| `backsource_ids` | Stable IDs from `.proof/backfill/sources/<module>/`. |
| `current_path` | Current file path in MAXIM. |
| `canonical_path` | Preferred durable path for future links. |
| `remap_from` | Historical or source paths that now map here. |
| `remap_to` | Replacement path if this file moves or splits. |

Current MAXIM files are not backsources by themselves. They become distributable
only after their backsource IDs and remaps are recorded.

## View design

The frontmatter supports these first views:

| View | Query idea |
|---|---|
| Module source-custody dashboard | `module = X`, grouped by `source_custody`. |
| Root concept pack | Files where `root_concepts` contains a requested concept. |
| Concept neighborhood pack | Files where `concepts` intersects a requested concept set. |
| Index-only pack | Files where `kind` is `module-index`, `section-index`, or `concept-index`. |
| Downstream fact pack | Verified guides plus source records, emitted as PEBBLE and fetched with FLETCH. |

## Backfill rule

Do not add frontmatter to the whole repo at once. Add it to a module only when
that module is selected for PROOF backfill and source-custody review.
