---
maxim_schema: maxim.frontmatter.v1
id: mdloom-backfill:compilers:07-register-allocation
kind: source-record
module: compilers
section: compilers
title: Register Allocation - Graph Coloring vs Linear Scan, Spilling source record
status: source-custody
source_custody: partial
current_path: .mdloom/backfill/sources/compilers/07-register-allocation.source-record.md
canonical_path: .mdloom/backfill/sources/compilers/07-register-allocation.source-record.md
backsource_ids: [git-history:compilers:07-register-allocation]
concepts: [register allocation, interference graph, graph coloring, Chaitin, linear scan, spilling, coalescing]
root_concepts: [register allocation]
index_roles: [source-map]
remap_from: []
remap_to: []
updated: null
---

# Register Allocation - Graph Coloring vs Linear Scan, Spilling source record

| Field | Value |
|---|---|
| Current MAXIM file | `compilers/07-REGISTER-ALLOCATION.md` |
| MDLOOM source artifact | `.mdloom/backfill/sources/compilers/mdloom-source/07-REGISTER-ALLOCATION.source.md` |
| MDLOOM table sidecar | `.mdloom/backfill/sources/compilers/mdloom-source/07-REGISTER-ALLOCATION.tables.json` |
| MDLOOM block sidecar | `.mdloom/backfill/sources/compilers/mdloom-source/07-REGISTER-ALLOCATION.blocks.json` |
| Backfill report | `.mdloom/backfill/sources/compilers/backfill-report.json` |
| MDLOOM classification | `literal_markdown` |
| MDLOOM confidence | `high` |
| Round trip | `passed` |
| Structured extraction | `3` markdown tables, `9` visual/block candidates |
| Git provenance | `16cc6a20` |

## Custody note

This first-pass record proves the current file can be regenerated as a MDLOOM
literal source artifact and round-tripped without loss. It is still marked
`partial` because external/authentic backsources for factual claims have not yet
been attached.
