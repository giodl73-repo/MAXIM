"""Prove Cargo resolved every locked external manifest in restored inputs."""
import argparse
import json
import os
from pathlib import Path
import tomllib

from input_custody import CONFIG, verify


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--cargo-home", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    sha = (root / "cargo-inputs/sha256.txt").read_text().split()[0]
    manifest, data, modes = verify((root / "cargo-inputs/inputs.zip").read_bytes(), sha, (root / "Cargo.lock").read_bytes())
    metadata = json.loads(args.metadata.read_bytes())
    vendor = (args.inputs / "vendor").resolve()
    home = args.cargo_home.resolve()
    expected = {(p["name"], p["version"], p["source"]) for p in manifest["registry"]}
    external = [p for p in metadata["packages"] if p.get("source")]
    if len(external) != len(expected) or {(p["name"], p["version"], p["source"]) for p in external} != expected:
        raise ValueError("Cargo metadata dependency closure differs")
    for package in external:
        actual = Path(package["manifest_path"]).resolve()
        expected_path = vendor / f"{package['name']}-{package['version']}" / "Cargo.toml"
        if actual != expected_path or not actual.is_file():
            raise ValueError("Locked manifest is outside restored inputs: " + package["name"])
    local = [p for p in metadata["packages"] if not p.get("source")]
    if len(local) != 1 or Path(local[0]["manifest_path"]).resolve() != root / "Cargo.toml" or Path(metadata["workspace_root"]).resolve() != root:
        raise ValueError("Unexpected first-party workspace/manifest")
    node = next(p for p in metadata["resolve"]["nodes"] if p["id"] == local[0]["id"])
    if not set(local[0]["features"]).issubset(node["features"]):
        raise ValueError("Cargo metadata did not enable all first-party features")
    expected_files = {name[len("vendor/"):]: value for name, value in data.items() if name.startswith("vendor/")}
    actual_files = set()
    for path in vendor.rglob("*"):
        if path.is_symlink() or getattr(path.lstat(), "st_file_attributes", 0) & 0x400:
            raise ValueError("Restored vendor contains a link/junction")
        if path.is_file():
            name = path.relative_to(vendor).as_posix()
            actual_files.add(name)
            if name not in expected_files or path.read_bytes() != expected_files[name]:
                raise ValueError("Restored vendor source bytes differ")
            if os.name != "nt" and path.stat().st_mode & 0o777 != modes["vendor/" + name] & 0o777:
                raise ValueError("Restored vendor source mode differs")
    if actual_files != set(expected_files):
        raise ValueError("Restored vendor inventory differs")
    config = tomllib.loads((home / "config.toml").read_text(encoding="utf-8"))
    expected_config = tomllib.loads(CONFIG.decode().replace('directory = "vendor"', 'directory = ' + json.dumps(vendor.as_posix())) + "\n[net]\noffline = true\n")
    if (home / "registry").exists() or (home / "git").exists() or config != expected_config:
        raise ValueError("Cargo home/input configuration differs")
    print(json.dumps(dict(packages=len(external), capsule_sha256=sha, inputs=str(args.inputs.resolve()), cargo_home=str(home), all_manifests_in_restored_vendor=True, restored_vendor_files=len(actual_files), restored_source_bytes_verified=True, posix_modes_verified=os.name != "nt", registry_git_caches_absent=True, scope="Locked all-feature Cargo metadata and full restored byte/inventory/config closure. Rust compilation and actual parity are separate pipeline steps.")))


if __name__ == "__main__":
    main()
