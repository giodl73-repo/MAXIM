---
maxim_schema: maxim.frontmatter.v1
id: mdloom-backfill:disease:04-cancer
kind: source-record
module: disease
section: disease
title: Cancer source record
status: source-custody
source_custody: partial
current_path: .mdloom/backfill/sources/disease/04-cancer.source-record.md
canonical_path: .mdloom/backfill/sources/disease/04-cancer.source-record.md
backsource_ids: [git-history:disease:04-cancer]
concepts: [cancer]
root_concepts: [cancer]
index_roles: [source-map]
remap_from: []
remap_to: []
updated: null
---

# Cancer source record

| Field | Value |
|---|---|
| Current MAXIM file | `disease/04-CANCER.md` |
| MDLOOM source artifact | `.mdloom/backfill/sources/disease/mdloom-source/04-CANCER.source.md` |
| MDLOOM table sidecar | `.mdloom/backfill/sources/disease/mdloom-source/04-CANCER.tables.json` |
| MDLOOM block sidecar | `.mdloom/backfill/sources/disease/mdloom-source/04-CANCER.blocks.json` |
| Backfill report | `.mdloom/backfill/sources/disease/backfill-report.json` |
| MDLOOM classification | `literal_markdown` |
| MDLOOM confidence | `high` |
| Round trip | `passed` |
| Structured extraction | `1` markdown tables, `8` visual/block candidates |
| Git provenance | `0a189c79`, `8c4d0671`, `578235d5`, `ddd24c0f`, `c6e8db11`, `617a3f37`, `6928deb2` |

## Custody note

This first-pass record proves the current file can be regenerated as a MDLOOM
literal source artifact and round-tripped without loss. It is still marked
`partial` because external/authentic backsources for factual claims have not yet
been attached.
