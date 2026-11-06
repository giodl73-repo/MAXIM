"""Build the existing MkDocs library and its Rust/WASM search front door."""
import argparse
import gzip
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from build_inputs import verify
from input_custody import destination, digest
from source_custody import source_data
from site_custody import add_delivery, verify_site, BUILD_MANIFEST, source_epoch
from rust_build import configure, expected_policy

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    subprocess.run(args, cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("site"))
    parser.add_argument("--expected-source-head", help="Required for a verified source archive outside Git")
    args = parser.parse_args()
    print(json.dumps({"generator_inputs": verify()}))
    site = destination(args.site)
    # New outputs only; inspect lexical parents before following links.
    output_root = ROOT / "site"
    if site != output_root and output_root not in site.parents:
        raise ValueError("Output must be site or a directory inside site")
    targets = [ROOT / 'target']
    if os.environ.get('CARGO_TARGET_DIR'):targets.append(Path(os.environ['CARGO_TARGET_DIR']).resolve())
    if any(site == target or site in target.parents or target in site.parents for target in targets):raise ValueError('Output overlaps compiled target')
    head = args.expected_source_head
    if (ROOT / '.git').exists():
        actual = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
        if head and head != actual:raise ValueError('Expected source head differs')
        head = actual
    elif not head:raise ValueError('Use --expected-source-head with a verified source archive')
    data, modes = source_data(ROOT, head)
    os.environ['SOURCE_DATE_EPOCH'] = str(source_epoch(data))
    rust_metadata = json.loads(subprocess.check_output(['cargo', 'metadata', '--locked', '--offline', '--all-features', '--format-version', '1'], cwd=ROOT))
    rust_policy = configure(ROOT, rust_metadata)
    if rust_policy != expected_policy(data['Cargo.lock'], rust_policy['inherited_flags']):raise ValueError('Compiler path policy differs from complete lock')
    version = subprocess.check_output(["wasm-bindgen", "--version"], text=True).strip()
    if version != "wasm-bindgen 0.2.127":
        raise ValueError(f"Expected wasm-bindgen 0.2.127, found {version}")
    # MkDocs output must be outside docs_dir (the repository root).
    with tempfile.TemporaryDirectory(prefix="maxim-site-") as directory:
        build = Path(directory) / "html"
        run(sys.executable, "-X", "utf8", "-m", "mkdocs", "build", "-f", ".mkdocs/mkdocs.yml", "-d", str(build))
        run(sys.executable, "-X", "utf8", "tools/build-search.py", "--site", str(build))
        explore = build / "explore"
        run("cargo", "run", "--locked", "--release", "--bin", "maxim-index", "--", str(explore / "entries.json"), str(explore / "index.json"))
        run("cargo", "build", "--locked", "--release", "--target", "wasm32-unknown-unknown", "--lib", "--features", "wasm")
        metadata = json.loads(subprocess.check_output(["cargo", "metadata", "--no-deps", "--format-version", "1"], cwd=ROOT))
        wasm = Path(metadata["target_directory"]) / "wasm32-unknown-unknown/release/maxim_search.wasm"
        run("wasm-bindgen", str(wasm), "--target", "web", "--out-dir", str(explore / "pkg"))
        raw = explore / "index.json"
        (explore / "index.json.gz").write_bytes(gzip.compress(raw.read_bytes(), compresslevel=9, mtime=0))
        raw.unlink()
        (explore / "entries.json").unlink()
        (build / ".nojekyll").touch()
        manifest = add_delivery(build, data, modes, head, rust_policy)
        verify_site(build, digest((build / BUILD_MANIFEST).read_bytes()), head)
        size = sum(path.stat().st_size for path in build.rglob("*") if path.is_file())
        print(f"Published site: {size:,} bytes")
        if size >= 1_000_000_000:
            raise ValueError("Generated site exceeds the GitHub Pages 1 GB limit")
        site.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(build, site)
        print(json.dumps(dict(source_commit=head, source_tree=manifest['source_tree'], build_manifest_sha256=digest((site / BUILD_MANIFEST).read_bytes()), source_archive=manifest['source'], total_bytes=manifest['total_bytes'])))
    print(f"Search: {site / 'explore'}")


if __name__ == "__main__":
    main()
