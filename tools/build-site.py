"""Build the existing MkDocs library and its Rust/WASM search front door."""
import argparse
import gzip
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    subprocess.run(args, cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("site"))
    args = parser.parse_args()
    site = args.site.resolve()
    # Only the dedicated generated tree can be replaced. Resolve symlinks first.
    output_root = ROOT / "site"
    if site != output_root and output_root not in site.parents:
        raise ValueError("Output must be site or a directory inside site")
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
        for name in ("index.html", "style.css", "app.js", "worker.js"):
            shutil.copy2(ROOT / "web" / name, explore / name)
        (build / ".nojekyll").touch()
        size = sum(path.stat().st_size for path in build.rglob("*") if path.is_file())
        print(f"Published site: {size:,} bytes")
        if size >= 1_000_000_000:
            raise ValueError("Generated site exceeds the GitHub Pages 1 GB limit")
        if site.exists():
            shutil.rmtree(site)
        site.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(build, site)
    print(f"Search: {site / 'explore'}")


if __name__ == "__main__":
    main()
