# Original behavior and same-index parity

Original source d6c411e58b02b0901e96353ab884d4acab2fe607 is the current public
master. Canonical MAXIM remains clean at that source; implementation uses an
isolated child worktree. No TRACKER pointer changes in this phase.

The original native baseline passes7 unit tests, fmt, strict all-feature/all-target
Clippy, native CLI, unknown-target WASM and3 Python corpus-preparation tests.
Rust1.95.0/wasm-bindgen0.2.127, Python3.14.10 and Node22.23.4 are installed tools.
The shared compiled target and installed Cargo cache are reused. An initial
offline metadata failure for two absent crates is retained; locked acquisition
and the corrected complete offline baseline are separate. Cargo.lock is unchanged.

The observed anonymous deployed gzip is34,828,907 bytes; expanded index96,445,532,
42,242 entries,242 modules and125,949 terms. The unmodified native maxim-index
rebuilds every original index byte from all extracted entries. Full original
CLI stdout/stderr, including variable timings, are retained unnormalized. This
does not prove original guide/MkDocs-to-entries regeneration or source lineage.

The native example calls the unchanged Index directly. Actual compiled WASM
SearchIndex agrees on134 typed query/module/limit/Unicode/byte/token-boundary
controls and7 constructor/empty/corruption cases. Full result strings, entry
text, scores, ordering, totals, sections and counts match exactly. Four raw JS
limit coercions remain outside typed parity; no native usize or ranking policy
was changed. Full native/WASM streams are retained as lossless gzip files.
The original Rust, manifests/lock, data generator, guides, web UI, MkDocs config
and grants remain unchanged. The additive control/harness is not a new engine.

CI now drives this harness with the complete freshly generated source index,
retaining its actual Git source and compressed/expanded index identity. Pinned
Ubuntu24.04 supports the original Playwright1.58.2. The workflow passes actionlint;
Python/Node syntax and native example fmt/tests/strictClippy pass locally. The
wrapper's full hosted source-build execution is pending and is not inferred
from same-index local parity. Original3 browser cases remain in the pipeline.

All four full repo role lenses were applied by the implementing agent as
simulated perspectives in WAVE.md. This is not guide graduation, factual/Gold
certification or independent human review. Full Python/Cargo input custody,
complete source/artifact receivers, worker lifecycle, hosted default/live proof
and separate portfolio snapshot remain open. Adequate external scratch space is
pending; under1GB laptop free space prevents safe full local site duplication.
