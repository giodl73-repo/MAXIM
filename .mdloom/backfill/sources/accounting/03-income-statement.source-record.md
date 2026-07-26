---
maxim_schema: maxim.frontmatter.v1
id: mdloom-backfill:accounting:03-income-statement
kind: source-record
module: accounting
section: accounting
title: The Income Statement - The Period Delta source record
status: source-custody
source_custody: partial
current_path: .mdloom/backfill/sources/accounting/03-income-statement.source-record.md
canonical_path: .mdloom/backfill/sources/accounting/03-income-statement.source-record.md
backsource_ids: [git-history:accounting:03-income-statement]
concepts: [income statement, revenue recognition, COGS, gross margin, operating margin, EPS]
root_concepts: [income statement]
index_roles: [source-map]
remap_from: []
remap_to: []
updated: null
---

# The Income Statement - The Period Delta source record

| Field | Value |
|---|---|
| Current MAXIM file | `accounting/03-INCOME-STATEMENT.md` |
| MDLOOM source artifact | `.mdloom/backfill/sources/accounting/mdloom-source/03-INCOME-STATEMENT.source.md` |
| MDLOOM table sidecar | `.mdloom/backfill/sources/accounting/mdloom-source/03-INCOME-STATEMENT.tables.json` |
| MDLOOM block sidecar | `.mdloom/backfill/sources/accounting/mdloom-source/03-INCOME-STATEMENT.blocks.json` |
| Backfill report | `.mdloom/backfill/sources/accounting/backfill-report.json` |
| MDLOOM classification | `literal_markdown` |
| MDLOOM confidence | `high` |
| Round trip | `passed` |
| Structured extraction | `5` markdown tables, `2` visual/block candidates |
| Git provenance | `d5ad514c` |

## Custody note

This first-pass record proves the current file can be regenerated as a MDLOOM
literal source artifact and round-tripped without loss. It is still marked
`partial` because external/authentic backsources for factual claims have not yet
been attached.
