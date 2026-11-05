# Captured MAXIM Rust build inputs

inputs.zip binds every external package in the original unchanged Cargo.lock:
20 registry archives verified against locked checksums, all original source and
dotfiles/modes, Cargo directory-source checksums, and original grants/notices.
manifest.json inventories the complete capsule; sha256.txt anchors its bytes
from this trusted checkout. Third-party terms remain unchanged; MAXIM's software
license does not replace them. Original archives preserve their own source modes.

The MAXIM-owned verifier checks every archive/member/vendor checksum, source mode,
complete dependency/notice inventory and both new external destinations before
restoring. Run from the source root with two new absolute folder paths:

```sh
python tools/test_input_custody.py
python tools/input_custody.py --sha256 <trusted-input-sha> --inputs <new-input-folder> --cargo-home <new-cargo-home>
```

Take the trusted SHA from this checkout's sha256.txt or a separately verified
release receipt. Set CARGO_HOME to the restored home, CARGO_NET_OFFLINE=true and
CARGO_INCREMENTAL=0 before Cargo commands. Keep CARGO_TARGET_DIR explicit if using
a shared compiled target; source inputs must never overlap it. The CI pipeline
checks every actual metadata manifest path in the restored vendor, then compiles
and exercises native/WASM/browser behavior with acquisition offline.

An earlier external proof independently restored all20 Cargo manifests offline.
See the self-service wave's actual run receipts for the current compiled replay
status. Full Python/source/archive custody and live release remain open. This is
not an installed compiler/toolchain or a complete self-service release. The native Cargo
dependency contract and all version pins are unchanged.

Keep this compact complete input capsule in Git for source preservation. MkDocs
excludes it from incidental copying; the qualified source-download builder will
include these exact bytes explicitly. Do not trim notices or source to meet a
runtime budget. Installed Rust1.95.0/target/linker and compiled cache stay separate.
