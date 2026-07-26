# MAXIM MDLOOM backfill

MAXIM backfill moves one module at a time. Each module must preserve source
custody before it can become a CROP/MDPORT/FLETCH distribution surface.

## Flow

1. Select one module from `TRACKER.md`.
2. Record its current MAXIM paths in `modules/<module>.json`.
3. Store or reference authentic backsources under `sources/<module>/`.
4. Record remaps from backsource IDs to current MAXIM files.
5. Add frontmatter using [frontmatter-contract.md](frontmatter-contract.md).
6. Run MDLOOM checks for only that module.
7. After the module is source-custody clean, run the matching CROP view.
8. Emit a MDPORT pack and only then add a FLETCH registry/cacheline for
   downstream repos.

## Standard artifact roots

| Root | Commit? | Purpose |
|---|---:|---|
| `.mdloom/backfill/` | yes | Source-custody records, module ledgers, MDLOOM source artifacts, and remap manifests. |
| `.crop/views/` | yes | Stable CROP view recipes that define module and guide pack scopes. |
| `.mdport/packs/` | yes, after validation | Distributable MDPORT packs meant for downstream reuse. |
| `.fletch/registries/` | yes, after pack publication | FLETCH registry/cacheline manifests that point at committed packs. |
| `.crop/work/` | no | Scratch output, experiments, or unvalidated generated artifacts. |

The stable fetch path is `.fletch/registries/<id>.json` pointing at one or more
`.mdport/packs/<id>.mdport.json` cachelines. Downstream repos should FLETCH the
registry or pack path; they should not vendor MAXIM source directories directly.

## Rules

- Do not run a whole-repo backfill first.
- Do not invent backsources; mark missing source custody as `needs-source`.
- Do not bulk-add frontmatter across MAXIM; frontmatter lands one module at a time.
- Do not publish MDPORT packs before remaps and MDLOOM validation are clean.
- Do not require MDLOOM rendered output to include frontmatter; frontmatter is
  source metadata and should be emitted only with an explicit option.
- Keep generated packs separate from source custody records.
