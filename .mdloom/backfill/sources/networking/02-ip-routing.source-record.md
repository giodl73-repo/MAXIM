---
maxim_schema: maxim.frontmatter.v1
id: mdloom-backfill:networking:02-ip-routing
kind: source-record
module: networking
section: networking
title: IP and Routing - IPv4/IPv6, CIDR, Routing Tables, BGP, OSPF source record
status: source-custody
source_custody: partial
current_path: .mdloom/backfill/sources/networking/02-ip-routing.source-record.md
canonical_path: .mdloom/backfill/sources/networking/02-ip-routing.source-record.md
backsource_ids: [git-history:networking:02-ip-routing]
concepts: [ipv4, ipv6, cidr, subnetting, routing table, bgp, ospf, longest prefix match]
root_concepts: [ip routing]
index_roles: [source-map]
remap_from: []
remap_to: []
updated: null
---

# IP and Routing - IPv4/IPv6, CIDR, Routing Tables, BGP, OSPF source record

| Field | Value |
|---|---|
| Current MAXIM file | `networking/02-IP-ROUTING.md` |
| MDLOOM source artifact | `.mdloom/backfill/sources/networking/mdloom-source/02-IP-ROUTING.source.md` |
| MDLOOM table sidecar | `.mdloom/backfill/sources/networking/mdloom-source/02-IP-ROUTING.tables.json` |
| MDLOOM block sidecar | `.mdloom/backfill/sources/networking/mdloom-source/02-IP-ROUTING.blocks.json` |
| Backfill report | `.mdloom/backfill/sources/networking/backfill-report.json` |
| MDLOOM classification | `literal_markdown` |
| MDLOOM confidence | `high` |
| Round trip | `passed` |
| Structured extraction | `4` markdown tables, `7` visual/block candidates |
| Git provenance | `801707f4`, `d5ad514c` |

## Custody note

This first-pass record proves the current file can be regenerated as a MDLOOM
literal source artifact and round-tripped without loss. It is still marked
`partial` because external/authentic backsources for factual claims have not yet
been attached.
