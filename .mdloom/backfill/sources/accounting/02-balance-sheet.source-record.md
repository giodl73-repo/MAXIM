---
maxim_schema: maxim.frontmatter.v1
id: mdloom-backfill:accounting:02-balance-sheet
kind: source-record
module: accounting
section: accounting
title: The Balance Sheet - State Snapshot source record
status: source-custody
source_custody: partial
current_path: .mdloom/backfill/sources/accounting/02-balance-sheet.source-record.md
canonical_path: .mdloom/backfill/sources/accounting/02-balance-sheet.source-record.md
backsource_ids: [git-history:accounting:02-balance-sheet]
concepts: [balance sheet, assets, liabilities, equity, working capital, classification]
root_concepts: [balance sheet]
index_roles: [source-map]
remap_from: []
remap_to: []
updated: null
---

# The Balance Sheet - State Snapshot source record

| Field | Value |
|---|---|
| Current MAXIM file | `accounting/02-BALANCE-SHEET.md` |
| MDLOOM source artifact | `.mdloom/backfill/sources/accounting/mdloom-source/02-BALANCE-SHEET.source.md` |
| MDLOOM table sidecar | `.mdloom/backfill/sources/accounting/mdloom-source/02-BALANCE-SHEET.tables.json` |
| MDLOOM block sidecar | `.mdloom/backfill/sources/accounting/mdloom-source/02-BALANCE-SHEET.blocks.json` |
| Backfill report | `.mdloom/backfill/sources/accounting/backfill-report.json` |
| MDLOOM classification | `literal_markdown` |
| MDLOOM confidence | `high` |
| Round trip | `passed` |
| Structured extraction | `5` markdown tables, `4` visual/block candidates |
| Git provenance | `d5ad514c` |

## Custody note

This first-pass record proves the current file can be regenerated as a MDLOOM
literal source artifact and round-tripped without loss. It is still marked
`partial` because external/authentic backsources for factual claims have not yet
been attached.
