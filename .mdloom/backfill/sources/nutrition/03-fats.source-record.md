---
maxim_schema: maxim.frontmatter.v1
id: mdloom-backfill:nutrition:03-fats
kind: source-record
module: nutrition
section: nutrition
title: Fats source record
status: source-custody
source_custody: partial
current_path: .mdloom/backfill/sources/nutrition/03-fats.source-record.md
canonical_path: .mdloom/backfill/sources/nutrition/03-fats.source-record.md
backsource_ids: [git-history:nutrition:03-fats]
concepts: [fats]
root_concepts: [fats]
index_roles: [source-map]
remap_from: []
remap_to: []
updated: null
---

# Fats source record

| Field | Value |
|---|---|
| Current MAXIM file | `nutrition/03-FATS.md` |
| MDLOOM source artifact | `.mdloom/backfill/sources/nutrition/mdloom-source/03-FATS.source.md` |
| MDLOOM table sidecar | `.mdloom/backfill/sources/nutrition/mdloom-source/03-FATS.tables.json` |
| MDLOOM block sidecar | `.mdloom/backfill/sources/nutrition/mdloom-source/03-FATS.blocks.json` |
| Backfill report | `.mdloom/backfill/sources/nutrition/backfill-report.json` |
| MDLOOM classification | `literal_markdown` |
| MDLOOM confidence | `high` |
| Round trip | `passed` |
| Structured extraction | `1` markdown tables, `15` visual/block candidates |
| Git provenance | `454b1bd6`, `578235d5`, `ddd24c0f`, `99d33bb0`, `6b9c5b4a` |

## Custody note

This first-pass record proves the current file can be regenerated as a MDLOOM
literal source artifact and round-tripped without loss. It is still marked
`partial` because external/authentic backsources for factual claims have not yet
been attached.
