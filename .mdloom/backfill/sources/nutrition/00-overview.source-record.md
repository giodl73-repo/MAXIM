---
maxim_schema: maxim.frontmatter.v1
id: mdloom-backfill:nutrition:00-overview
kind: source-record
module: nutrition
section: nutrition
title: Nutrition - Overview source record
status: source-custody
source_custody: partial
current_path: .mdloom/backfill/sources/nutrition/00-overview.source-record.md
canonical_path: .mdloom/backfill/sources/nutrition/00-overview.source-record.md
backsource_ids: [git-history:nutrition:00-overview]
concepts: [overview]
root_concepts: [overview]
index_roles: [source-map]
remap_from: []
remap_to: []
updated: null
---

# Nutrition - Overview source record

| Field | Value |
|---|---|
| Current MAXIM file | `nutrition/00-OVERVIEW.md` |
| MDLOOM source artifact | `.mdloom/backfill/sources/nutrition/mdloom-source/00-OVERVIEW.source.md` |
| MDLOOM table sidecar | `.mdloom/backfill/sources/nutrition/mdloom-source/00-OVERVIEW.tables.json` |
| MDLOOM block sidecar | `.mdloom/backfill/sources/nutrition/mdloom-source/00-OVERVIEW.blocks.json` |
| Backfill report | `.mdloom/backfill/sources/nutrition/backfill-report.json` |
| MDLOOM classification | `literal_markdown` |
| MDLOOM confidence | `high` |
| Round trip | `passed` |
| Structured extraction | `4` markdown tables, `4` visual/block candidates |
| Git provenance | `454b1bd6`, `6b9c5b4a` |

## Custody note

This first-pass record proves the current file can be regenerated as a MDLOOM
literal source artifact and round-tripped without loss. It is still marked
`partial` because external/authentic backsources for factual claims have not yet
been attached.
