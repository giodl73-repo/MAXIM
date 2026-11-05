# Complete source custody

The source packager exports every tracked file from raw Git objects, bypassing
checkout/export filters. It includes all authored guides, software, hidden tracked
files, original Git modes, both locked Rust/Python input capsules and their
original notices. The generated manifest binds each file's bytes, SHA-256, Git
blob and mode to the complete tree and original commit object. A source ZIP is
not an authorship or factual certification. Existing software, content and
third-party grants remain unchanged; see `LICENSE.md` and dependency notices.

Use Python 3.11+ for packaging or receiver verification. The actual site generator
requires Python 3.12.16 and its complete pinned environment; compilers, linker,
Rust target/bindgen, interpreter/pip, Node and browser remain prerequisites.

```sh
python tools/package-source.py --expected-source-head <exact-commit> --output <new-external-source.zip>
python tools/receive-source.py --source <source.zip> --sha256 <trusted-sha256> --commit <exact-commit> --restore-source <new-external-folder>
```

The receiver needs `source_custody.py`, `input_custody.py` and `python_custody.py`
beside it. It needs neither Git nor installed third-party Python distributions.
It checks all original source and dependency bytes before restoring, executes no
downloaded code, refuses existing destinations and links/junctions, and protects
the source checkout and configured compiled target. Obtain the expected commit
and archive SHA from an independently trusted checkout or release receipt.

The producer requires a clean checkout and refuses unlisted source/config files.
Raw Git bytes are authoritative; only ordinary checkout CRLF expansion is allowed
when checking physical files. Archive restoration preserves original bytes and
POSIX modes; Windows mode limitations are explicit. Repacking a verified restored
source tree uses its commit-bound manifest without requiring `.git`.

The source ZIP is deterministic for the same source and Python/zlib environment.
Different zlib versions may encode ZIP compression differently without changing
the verified original file bytes. No cross-platform ZIP identity is assumed.
The 50,000-file / 768 MiB uncompressed / 512 MiB ZIP limits cover the complete
current library, rather than selecting a smaller source subset.

The Pages build publishes the complete source ZIP, source manifest, index,
adapter, WASM and original notices in Explore's footer. The source and index
revision are visible without JavaScript. The verifier bundle contains seven
Git-bound stdlib helpers and concrete source-receiving commands. The complete
project site's `explore/BUILD-MANIFEST.json` inventories every rendered guide,
runtime file and download, with one total budget below 1 GB.

`tools/receive-site.py` verifies a downloaded full project folder using its
independently trusted manifest SHA and source commit. It checks every file,
original source, dependency/font/runtime notices, UI templates and receiver
helper identities. This is artifact integrity; execution evidence remains
separate from hash verification.

`tools/qualify-archive.py` restores the complete source without `.git`, creates
new Cargo/Python inputs and a Python venv, then runs native, full site/WASM,
parity and browser checks. It compares every published file and the complete
manifest byte-for-byte. CI uses a new empty compiled target; explicit local
`--target-dir` cache reuse is recorded. Installed interpreter/pip, Rust/target/
bindgen, Node/Playwright/browser are prerequisites. The locked installed Node
test package is copied as a prerequisite, without re-resolving dependencies.

MkDocs receives `SOURCE_DATE_EPOCH` from the original source commit for stable
build/sitemap timestamps. Fonts retain the original families, WOFF2 bytes and
all original CSS subsets, with URLs pointing to same-origin assets and complete
OFL notices. Their builds and editable font source were not reproduced. Default/
live delivery still needs separate qualification.
