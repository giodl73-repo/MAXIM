# Search validation — 2026-10-04

## Passed

- Native Rust unit tests: ranking, AND intersection, repeated-word semantics,
  exact module filtering, counts/limits, empty and unknown queries, Unicode,
  schema validation, corrupt postings, deterministic ties, and top-100 bounds.
- `cargo +stable clippy --offline --all-targets --all-features -- -D warnings`.
- Release `wasm32-unknown-unknown` library build with the `wasm` feature.
- JavaScript adapter generated with wasm-bindgen 0.2.127; actual Rust/WASM
  execution in Chromium, not a mocked JavaScript search implementation.
- Python corpus-preparation tests for exclusion, deduplication, missing pages,
  and encoded Unicode filenames.
- Three browser tests: project-prefix search and real guide links, module
  filtering, no-match/empty states, mobile overflow, and failed index download.
- Desktop (1440 px) and mobile (390 px) screenshots visually inspected. A
  discovered mobile text overflow was corrected with wrapping.
- JavaScript syntax checks and tracked-file `git diff --check`.
- Full `python tools/build-site.py --site site/MAXIM` completed from local source
  with MkDocs 1.6.1 and Material 9.7.2. Existing guide-link/anchor warnings remain;
  no library-wide link-clean claim. The new Explore navigation resolves correctly.
- All three browser checks reran against that fresh site, including oversized
  query feedback, and passed. Fresh desktop/mobile screenshots were inspected.

## Fresh local source-build measurements

An initial experiment used the existing sibling reference-site (37,088 entries).
The final verification below rebuilt the current local source through MkDocs,
prepared guide entries, built the Rust index and WASM, and served `/MAXIM/`.
These measurements are local; hosted verification is recorded separately below.

| Measurement | Observation |
|---|---|
| Entries / modules | 42,242 / 242 |
| Raw precomputed index | 96,445,532 bytes |
| Deterministic gzip delivery | 34,828,907 bytes |
| Generated WASM | 163,288 bytes |
| Native index construction | 12.24 seconds during the full build |
| Native sample queries | 0.08–0.37 ms, four warm queries |
| Browser example | `rust ownership`: 146 entries, 2.1 ms worker query/serialization |
| Browser initial navigation to results | about 3.1 seconds on localhost |
| MkDocs build | 465.64 seconds |

Environment: Windows x64, Rust/Cargo stable 1.95.0, Node 24.19.0, Python 3.13,
bundled Playwright 1.62.1 and installed Chromium revision 1243. CI deliberately
uses the committed Playwright 1.58.2 lockfile with its matching browser download;
that clean installation passed in the hosted run below. Final local tests served the
freshly built `site/MAXIM` tree, replacing the earlier baseline preview server.
Localhost timings exclude realistic WAN transfer costs. The initial download
and memory footprint remain material; sharding/binary encoding are follow-ups
if measured usage warrants them. Do not call this a small or instant download.

## Role review (single-agent application of repository lenses)

- Reader Path Editor: numbered guide headings retain MkDocs URLs; search is
  linked from README/navigation and exposes module filters and example queries.
- Reference Integrity Auditor: relevance is not certification; the UI preserves
  this boundary and content licensing. No guide facts were edited or promoted.
- Executable Evidence Auditor: core and browser execution have direct evidence.
  Fresh-site build and its browser tests passed. The pinned CI browser install
  passed; deployment evidence belongs to the default-branch Pages workflow.
- Learner Advocate: descriptive labels, keyboard form submission, mobile
  wrapping, excerpts, empty states, and recovery links are present. Matching
  semantics are visible; no unsupported fuzzy-search promise is made.

## Release evidence and boundaries

1. Git metadata access and `giodl73-repo` authentication are restored. Changes
   are isolated on `codex/rust-wasm-search` from the fetched default branch.
2. [Hosted CI run 37235302834](https://github.com/giodl73-repo/MAXIM/actions/runs/37235302834)
   passed source validation, a clean site/WASM build, the committed Playwright
   1.58.2 browser tests, and Pages artifact upload for implementation `43949e0b6`.
   Final built-in Codex review was clean after the size correction below.
3. `python -m proof check` is unavailable: `No module named proof`. Focused
   implementation checks above ran instead; no library-wide proof claim.
4. [PR #3](https://github.com/giodl73-repo/MAXIM/pull/3) releases the implementation
   to `master`. Its default-branch workflow owns deployment receipts; TRACKER's
   `2026-10-04-rust-webassembly-pages` wave records the final child SHA and live
   verification before its portfolio snapshot is merged.

The DLL crash was isolated separately: bundled Git lacks its HTTPS helper;
placing the installed Git executable/helper and matching native DLLs together
in a temporary task runtime successfully read remote MAXIM HEAD. No system Git
installation was modified. Earlier sandbox metadata-write and connector access
failures were bypassed after shell access and authentication were restored.

## Pages size correction

Built-in Codex review found the initial 1,230,175,866-byte site exceeded Pages'
1 GB limit. Material navigation pruning removes repeated full-library navigation
from guide pages while preserving links and all 42,242 search entries. The fresh
build is 403,235,579 bytes (67% smaller); MkDocs completed in 98.01 seconds.
The build now rejects any generated site at or above 1,000,000,000 bytes before
publishing or replacing the previous local output.
All three browser tests passed again against this reduced site (24.3 seconds).
