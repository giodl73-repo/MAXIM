# MAXIM search

`maxim-search` is a reusable Rust crate and native index builder. The same query
engine runs in a browser worker through `wasm-bindgen`; GitHub Pages serves its
WASM, adapter, and precomputed index. No server or API key is required. The
interface lives at `/MAXIM/explore/`, linked from the MkDocs navigation.

## Reproduce

Install Rust 1.95.0 (including `wasm32-unknown-unknown`), Python 3.12+, Node 22,
and wasm-bindgen-cli 0.2.127 (`cargo install wasm-bindgen-cli --version 0.2.127
--locked`). From this repository's root:

```sh
python -m pip install -r requirements.txt
cargo test --locked
cargo clippy --locked --all-targets --all-features -- -D warnings
cargo fmt --check
python tools/build-site.py --site site
python -m http.server 8000 --directory site
```

Open `http://localhost:8000/explore/`. To run browser checks under the GitHub
project prefix (including WASM execution, result links, empty results, module
filtering, mobile layout, and load failure):

```sh
npm ci
npx playwright install chromium
python tools/build-site.py --site site/MAXIM
npm test
```

The Pages workflow runs the native tests, builds the complete library and search
assets, and runs browser checks before uploading a deployment artifact. Only
the default branch deploys. Repository Pages settings must select GitHub Actions.

## Data and query contract

- `tools/build-search.py` reads the built MkDocs `search/search_index.json`.
  Numbered guide URLs and headings are authoritative; metadata, hidden process
  files, and duplicated generated corpora are excluded from the Rust index.
- The native `maxim-index entries.json index.json` binary builds sorted posting
  lists once, at publication time. Browser startup deserializes and validates
  the index; queries do not tokenize the corpus again.
- Matching is case-insensitive Unicode alphanumeric token intersection. All
  distinct words must occur in the same entry. There is no stemming, typo
  tolerance, phrase syntax, or semantic/vector search in v1.
- Ranking combines document-frequency weighting, saturating term frequency,
  body-length normalization, and a title boost. It is lexical relevance, not
  factual confidence or Gold certification.
- Queries are limited to 512 UTF-8 bytes and 16 distinct words. Empty, unknown,
  or oversized queries return no hits. Results are deterministic, ties sort by
  URL, and the result limit is clamped to 100 while total counts remain exact.
- Queries start with the shortest posting list and binary-search the remaining
  lists. Top-k storage is bounded to 101 hits. Module filtering is exact.
- Index schema v1 rejects unsupported versions and invalid posting IDs, order,
  or weights before use. The UI renders text nodes, confines result URLs to the
  site, ignores stale replies, and displays a usable failure state.

Posting weights use fixed-point thousandths and compact tuple serialization.
The index is delivered as deterministic gzip and decompressed in the worker with
the browser's `DecompressionStream` API. An unsupported browser gets the normal
load-failure message and library navigation.

The initial index retains entry text for excerpts. Size and startup memory are
the main scaling costs; inspect measured corpus/bundle sizes before adding
sharding or binary compression. Do not describe this as a full-text database,
an offline cache, a factual certification engine, or zero-copy loading.

The query interface is the primary entry finder. Material navigation pruning
keeps guide pages from embedding the complete library navigation repeatedly.
The build enforces a total published-site budget below 1 GB for GitHub Pages.

## Reuse and licensing

Use `Index::build(Vec<Entry>)`, `Index::to_json`, `Index::from_json`, and
`Index::search(query, module, limit)` in native Rust. Enable `wasm` to expose
`SearchIndex` to JavaScript. The crate has no TRACKER-relative dependency.

Software is MIT under `LICENSE.md`; guides and generated corpus/index text
remain CC BY-NC 4.0. Source and compiled WASM downloads are available in the UI.
Crate packaging excludes guide content. Do not publish a content-bearing index
under the software license.
