# 2026-07-29 — Module source-corpus backfill (fact-fixed set)

## Scope
Regenerated PROOF / MDCROP / MDPORT / FLETCH source-corpus artifacts for the six
modules touched by the 2026-07-29 fact + K♠ rescore pass:

- biology
- cryptography
- distributed-systems
- genomics
- disease
- cloud-architecture

Source-first rule held: numbered guides are canonical; derived trees were
regenerated, not hand-edited.

## Tooling
- `module_source_backfill.py`: resolve `mdcrop` via portfolio alias `crop`
- scoped `--validate` mdcrop inspect to module views only (same-depth temp under
  `.mdcrop/` so `../../<module>` roots still resolve)
- TRACKER `repo-map.toml`: `[repos.mdcrop]` alias → `repos/tools-infra/crop`

## Results (all `--validate` exit 0)

| module | guides | roundtrip | tables | blocks | pack sections | fletches |
|--------|--------|-----------|--------|--------|---------------|----------|
| disease | 11 | 11/11 | 44 | 121 | 238 | 56 |
| biology | 7 | 7/7 | 11 | 62 | 101 | 36 |
| cryptography | 6 | 6/6 | 8 | 77 | 83 | 31 |
| genomics | 10 | 10/10 | 13 | 89 | 129 | 51 |
| distributed-systems | 11 | 11/11 | 24 | 107 | 211 | 56 |
| cloud-architecture | 10 | 10/10 | 11 | 55 | 135 | 51 |

## Spot checks
Stale bad strings absent from regenerated `.proof` sources:
- biology Okazaki / discontinuous lagging strand wording present; old continuous-both-strands absent
- cryptography RSA-OAEP present
- genomics Sanger generation wording present; stale 1 Gb/day claim absent
- disease 1918 "deadliest influenza pandemic" present; "deadliest pandemic in history" absent

Guide working-tree diffs are frontmatter only (`backsource_ids`: `proof-backfill:` → `proof-backfill:`).

## Non-goals
- No full-library regen
- No Gold factory / score inflation
- No bulk editor-tag stripping
