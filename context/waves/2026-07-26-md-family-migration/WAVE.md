---
wave: md-family-migration
date_open: 2026-07-26
status: done
source_request: "Resolve MAXIM local state and migrate generated artifacts."
---

# Wave: MD family migration

MAXIM's active expansion work was first preserved in checkpoint commit
`0a189c79`. The source-corpus generator and derived artifacts then migrated to:

- `.proof/`, `proof.toml`, and `proof.*`,
- `.mdport/`, `*.mdport.json`, and `mdport.v1`,
- existing MDCROP views and FLETCH registries pointing at the renamed artifacts.

Canonical numbered guides were not modified by the naming migration.

Validation:

- `python -m unittest discover -s .claude\skills\maxim-source-backfill\tests -p "test_*.py"`
- `git diff --check`
