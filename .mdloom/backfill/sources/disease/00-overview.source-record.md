---
maxim_schema: maxim.frontmatter.v1
id: mdloom-backfill:disease:00-overview
kind: source-record
module: disease
section: disease
title: Disease - Overview source record
status: source-custody
source_custody: partial
current_path: .mdloom/backfill/sources/disease/00-overview.source-record.md
canonical_path: .mdloom/backfill/sources/disease/00-overview.source-record.md
backsource_ids: [git-history:disease:00-overview]
concepts: [overview]
root_concepts: [overview]
index_roles: [source-map]
remap_from: []
remap_to: []
updated: null
---

# Disease - Overview source record

| Field | Value |
|---|---|
| Current MAXIM file | `disease/00-OVERVIEW.md` |
| MDLOOM source artifact | `.mdloom/backfill/sources/disease/mdloom-source/00-OVERVIEW.source.md` |
| MDLOOM table sidecar | `.mdloom/backfill/sources/disease/mdloom-source/00-OVERVIEW.tables.json` |
| MDLOOM block sidecar | `.mdloom/backfill/sources/disease/mdloom-source/00-OVERVIEW.blocks.json` |
| Backfill report | `.mdloom/backfill/sources/disease/backfill-report.json` |
| MDLOOM classification | `literal_markdown` |
| MDLOOM confidence | `high` |
| Round trip | `passed` |
| Structured extraction | `3` markdown tables, `7` visual/block candidates |
| Git provenance | `0a189c79`, `8c4d0671`, `578235d5`, `fbc40017`, `ddd24c0f`, `c6e8db11`, `617a3f37`, `6928deb2` |

## Custody note

This first-pass record proves the current file can be regenerated as a MDLOOM
literal source artifact and round-tripped without loss. It is still marked
`partial` because external/authentic backsources for factual claims have not yet
been attached.
