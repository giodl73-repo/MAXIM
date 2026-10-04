# Rust search and the browser reference desk

Status: native, WASM, fresh-site build, browser checks, and hosted CI passed.
Publication evidence is tracked by the default-branch Pages workflow and the
TRACKER adoption snapshot. GitHub authentication and repository access restored.

## Mission

Let a reader search MAXIM entries through the same efficient Rust query engine
in native tools and GitHub Pages. Keep numbered source guides canonical and
preserve the distinction between relevance and factual certification.

| Pulse | Deliverable | Status |
|---|---|---|
| 01 | Rust inverted index, WASM adapter, accessible search UI, Pages build | locally and hosted-CI validated; see Pages workflow for deployment |

## Scope and scout

Read root CLAUDE.md, README.md, MkDocs configuration, wave phases, the portfolio
operating guidance, and the four repository role lenses. The starting checkout
was clean on `pitfall/use-case-integration-20260829`; its metadata is stored in
TRACKER's `.git/modules/repos/knowledge-systems/maxim`. The default branch is
`master`, not `main`. Existing branch work must not be swept into this change.

No source-guide edits or source-backfill outputs are part of this pulse.
No implementation changes were made to ICELINES, BISECT, or OSW.

## Evidence

See [validation](VALIDATION.md) for commands, environment, baseline measurements,
role review, and the remaining release gates. Do not mark this wave published
until fresh-build checks pass and the default-branch deployment is verified.
