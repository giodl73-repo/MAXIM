---
maxim_schema: maxim.frontmatter.v1
id: mdloom-backfill:accounting:01-double-entry
kind: source-record
module: accounting
section: accounting
title: Double-Entry Bookkeeping - The Ledger Invariant source record
status: source-custody
source_custody: partial
current_path: .mdloom/backfill/sources/accounting/01-double-entry.source-record.md
canonical_path: .mdloom/backfill/sources/accounting/01-double-entry.source-record.md
backsource_ids: [git-history:accounting:01-double-entry]
concepts: [double-entry, accounting equation, debits, credits, journal, ledger, trial balance]
root_concepts: [double-entry bookkeeping]
index_roles: [source-map]
remap_from: []
remap_to: []
updated: null
---

# Double-Entry Bookkeeping - The Ledger Invariant source record

| Field | Value |
|---|---|
| Current MAXIM file | `accounting/01-DOUBLE-ENTRY.md` |
| MDLOOM source artifact | `.mdloom/backfill/sources/accounting/mdloom-source/01-DOUBLE-ENTRY.source.md` |
| MDLOOM table sidecar | `.mdloom/backfill/sources/accounting/mdloom-source/01-DOUBLE-ENTRY.tables.json` |
| MDLOOM block sidecar | `.mdloom/backfill/sources/accounting/mdloom-source/01-DOUBLE-ENTRY.blocks.json` |
| Backfill report | `.mdloom/backfill/sources/accounting/backfill-report.json` |
| MDLOOM classification | `literal_markdown` |
| MDLOOM confidence | `high` |
| Round trip | `passed` |
| Structured extraction | `4` markdown tables, `8` visual/block candidates |
| Git provenance | `d5ad514c` |

## Custody note

This first-pass record proves the current file can be regenerated as a MDLOOM
literal source artifact and round-tripped without loss. It is still marked
`partial` because external/authentic backsources for factual claims have not yet
been attached.
