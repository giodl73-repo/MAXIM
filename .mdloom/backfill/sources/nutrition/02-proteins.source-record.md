---
maxim_schema: maxim.frontmatter.v1
id: mdloom-backfill:nutrition:02-proteins
kind: source-record
module: nutrition
section: nutrition
title: Proteins source record
status: source-custody
source_custody: partial
current_path: .mdloom/backfill/sources/nutrition/02-proteins.source-record.md
canonical_path: .mdloom/backfill/sources/nutrition/02-proteins.source-record.md
backsource_ids: [git-history:nutrition:02-proteins]
concepts: [proteins]
root_concepts: [proteins]
index_roles: [source-map]
remap_from: []
remap_to: []
updated: null
---

# Proteins source record

| Field | Value |
|---|---|
| Current MAXIM file | `nutrition/02-PROTEINS.md` |
| MDLOOM source artifact | `.mdloom/backfill/sources/nutrition/mdloom-source/02-PROTEINS.source.md` |
| MDLOOM table sidecar | `.mdloom/backfill/sources/nutrition/mdloom-source/02-PROTEINS.tables.json` |
| MDLOOM block sidecar | `.mdloom/backfill/sources/nutrition/mdloom-source/02-PROTEINS.blocks.json` |
| Backfill report | `.mdloom/backfill/sources/nutrition/backfill-report.json` |
| MDLOOM classification | `literal_markdown` |
| MDLOOM confidence | `high` |
| Round trip | `passed` |
| Structured extraction | `1` markdown tables, `13` visual/block candidates |
| Git provenance | `454b1bd6`, `578235d5`, `ddd24c0f`, `99d33bb0`, `6b9c5b4a` |

## Custody note

This first-pass record proves the current file can be regenerated as a MDLOOM
literal source artifact and round-tripped without loss. It is still marked
`partial` because external/authentic backsources for factual claims have not yet
been attached.
