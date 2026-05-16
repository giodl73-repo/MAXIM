---
name: maxim-source-backfill
description: "Backfill a MAXIM module into PROOF source sidecars, CROP views, PEBBLE packs, and FLETCH cachelines."
tags: [maxim, source-corpus, proof, crop, pebble, fletch, backfill]
---

# maxim-source-backfill

Backfill a numbered MAXIM module directory into the shared source-corpus flow:
PROOF preserves source fidelity and structured sidecars, CROP defines views,
PEBBLE emits portable packs, and FLETCH publishes fetchable cachelines.

## Usage

```text
/maxim-source-backfill module computing --module-id computing-software
/maxim-source-backfill module data-science --module-id data-science
```

The skill owns first-pass source-custody publication only. It must keep factual
custody marked `partial` until authentic external backsources are attached.

## Procedure

1. Check the repo is clean or understand existing edits before changing files.
2. Run the helper in this skill:

   ```powershell
   Set-Location C:\src\MAXIM
   python .claude\skills\maxim-source-backfill\scripts\module_source_backfill.py `
     --module-dir computing `
     --module-id computing-software `
     --validate
   ```

3. Review any PROOF errors. Fix real article issues, usually:
   - wide emoji inside ASCII boxes or fenced layout blocks;
   - markdown table column mismatches;
   - malformed frontmatter.
4. Re-run the helper with `--validate` until it passes.
5. Inspect the generated counts:
   - guide count;
   - PROOF round-trip pass/fail;
   - markdown table count;
   - structured block count;
   - FLETCH registry entry count.
6. Commit the module repo.
7. Update TRACKER dependency-system files with the new module counts and commit.

## Generated surfaces

For a module with numbered guides, the helper generates or refreshes:

| Surface | Path pattern |
|---|---|
| Guide frontmatter | `{module-dir}/NN-*.md` |
| CROP guide views | `.crop/views/maxim-{module-id}-{guide-slug}.json` |
| CROP module view | `.crop/views/maxim-{module-id}-source-corpus.json` |
| PEBBLE guide packs | `.pebble/packs/maxim-{module-id}-{guide-slug}.pebble.json` |
| PEBBLE module pack | `.pebble/packs/maxim-{module-id}-source-corpus.pebble.json` |
| PROOF literal sources | `.proof/backfill/sources/{module-id}/proof-source/*.source.md` |
| PROOF table sidecars | `.proof/backfill/sources/{module-id}/proof-source/*.tables.json` |
| PROOF block sidecars | `.proof/backfill/sources/{module-id}/proof-source/*.blocks.json` |
| Source records | `.proof/backfill/sources/{module-id}/*.source-record.md` |
| Module ledger | `.proof/backfill/modules/{module-id}.json` |
| FLETCH registry | `.fletch/registries/maxim-{module-id}-source-corpus.json` |

## Validation

The helper's `--validate` mode runs:

```powershell
cargo run --manifest-path C:\src\proof\Cargo.toml --quiet -- check <module guides>
cargo run --manifest-path C:\src\CROP\Cargo.toml --quiet -- view --inspect --dir .crop\views --strict
cargo run --manifest-path C:\src\FLETCH\Cargo.toml --bin fletch-cli --quiet -- registry validate --file <registry>
git diff --check
```

It also checks every registry shaft path exists.

## Rules

- For content maintenance after backfill, edit the canonical numbered guide in
  the module directory first, then rerun this helper with `--validate`.
- Do not hand-edit generated source-corpus outputs unless the task explicitly
  changes the generator/schema: `.proof/backfill/sources/**`,
  `.proof/backfill/modules/**`, `.crop/views/**`, `.pebble/packs/**`, and
  `.fletch/registries/**` are regenerated from the guide source.
- Commit source guide edits and regenerated outputs together.
- Do not mark source custody complete in first pass.
- Preserve existing frontmatter values when present.
- Keep CROP/PEBBLE/PROOF interpretation out of FLETCH core; FLETCH only fetches
  and verifies generic cache entries.
- PROOF rendered output should omit frontmatter by default; PEBBLE carries
  frontmatter metadata.
- If validation reveals real guide defects, fix the guide and regenerate all
  sidecars before committing.
