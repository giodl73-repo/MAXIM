---
maxim_schema: maxim.frontmatter.v1
id: mdloom-backfill:disease:01-bacterial
kind: source-record
module: disease
section: disease
title: Bacterial Disease source record
status: source-custody
source_custody: partial
current_path: .mdloom/backfill/sources/disease/01-bacterial.source-record.md
canonical_path: .mdloom/backfill/sources/disease/01-bacterial.source-record.md
backsource_ids: [git-history:disease:01-bacterial]
concepts: [bacterial]
root_concepts: [bacterial]
index_roles: [source-map]
remap_from: []
remap_to: []
updated: null
---

# Bacterial Disease source record

| Field | Value |
|---|---|
| Current MAXIM file | `disease/01-BACTERIAL.md` |
| MDLOOM source artifact | `.mdloom/backfill/sources/disease/mdloom-source/01-BACTERIAL.source.md` |
| MDLOOM table sidecar | `.mdloom/backfill/sources/disease/mdloom-source/01-BACTERIAL.tables.json` |
| MDLOOM block sidecar | `.mdloom/backfill/sources/disease/mdloom-source/01-BACTERIAL.blocks.json` |
| Backfill report | `.mdloom/backfill/sources/disease/backfill-report.json` |
| MDLOOM classification | `literal_markdown` |
| MDLOOM confidence | `high` |
| Round trip | `passed` |
| Structured extraction | `6` markdown tables, `7` visual/block candidates |
| Git provenance | `8c4d0671`, `578235d5`, `ddd24c0f`, `c6e8db11`, `617a3f37`, `6928deb2` |

## Custody note

This first-pass record proves the current file can be regenerated as a MDLOOM
literal source artifact and round-tripped without loss. It is still marked
`partial` because external/authentic backsources for factual claims have not yet
been attached.
