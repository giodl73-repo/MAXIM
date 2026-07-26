---
name: maxim-source-backfill
description: "Backfill a MAXIM module into MDLOOM source sidecars, MDCROP views, MDPORT packs, and FLETCH cachelines."
tags: [maxim, source-corpus, proof, crop, mdport, fletch, backfill]
---

# maxim-source-backfill

Backfill a numbered MAXIM module directory into the shared source-corpus flow:
MDLOOM preserves source fidelity and structured sidecars, MDCROP defines views,
MDPORT emits portable packs, and FLETCH publishes fetchable cachelines.

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

3. Review any MDLOOM errors. Fix real article issues, usually:
   - wide emoji inside ASCII boxes or fenced layout blocks;
   - markdown table column mismatches;
   - malformed frontmatter.
4. Re-run the helper with `--validate` until it passes.
5. Inspect the generated counts:
   - guide count;
   - MDLOOM round-trip pass/fail;
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
| MDCROP guide views | `.mdcrop/views/maxim-{module-id}-{guide-slug}.json` |
| MDCROP module view | `.mdcrop/views/maxim-{module-id}-source-corpus.json` |
| MDPORT guide packs | `.mdport/packs/maxim-{module-id}-{guide-slug}.mdport.json` |
| MDPORT module pack | `.mdport/packs/maxim-{module-id}-source-corpus.mdport.json` |
| MDLOOM literal sources | `.mdloom/backfill/sources/{module-id}/mdloom-source/*.source.md` |
| MDLOOM table sidecars | `.mdloom/backfill/sources/{module-id}/mdloom-source/*.tables.json` |
| MDLOOM block sidecars | `.mdloom/backfill/sources/{module-id}/mdloom-source/*.blocks.json` |
| Source records | `.mdloom/backfill/sources/{module-id}/*.source-record.md` |
| Module ledger | `.mdloom/backfill/modules/{module-id}.json` |
| FLETCH registry | `.fletch/registries/maxim-{module-id}-source-corpus.json` |

## Validation

The helper's `--validate` mode runs:

```powershell
cargo run --manifest-path C:\src\proof\Cargo.toml --quiet -- check <module guides>
cargo run --manifest-path C:\src\MDCROP\Cargo.toml --quiet -- view --inspect --dir .mdcrop\views --strict
cargo run --manifest-path C:\src\FLETCH\Cargo.toml --bin fletch-cli --quiet -- registry validate --file <registry>
git diff --check
```

It also checks every registry shaft path exists.

## Rules

- For content maintenance after backfill, edit the canonical numbered guide in
  the module directory first, then rerun this helper with `--validate`.
- Do not hand-edit generated source-corpus outputs unless the task explicitly
  changes the generator/schema: `.mdloom/backfill/sources/**`,
  `.mdloom/backfill/modules/**`, `.mdcrop/views/**`, `.mdport/packs/**`, and
  `.fletch/registries/**` are regenerated from the guide source.
- Commit source guide edits and regenerated outputs together.
- Do not mark source custody complete in first pass.
- Preserve existing frontmatter values when present.
- Keep MDCROP/MDPORT/MDLOOM interpretation out of FLETCH core; FLETCH only fetches
  and verifies generic cache entries.
- MDLOOM rendered output should omit frontmatter by default; MDPORT carries
  frontmatter metadata.
- If validation reveals real guide defects, fix the guide and regenerate all
  sidecars before committing.
