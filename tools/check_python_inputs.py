"""Verify a restored Python cache, package locations and installed environment."""
import argparse
import importlib.metadata
import json
import os
from pathlib import Path
import sys

from build_inputs import verify as verify_generator
from input_custody import destination, digest
from python_custody import verify


def snapshot(prefix):
    files = []
    interpreter = Path(sys._base_executable).resolve()
    for path in sorted(prefix.rglob("*")):
        name = path.relative_to(prefix).as_posix()
        if path.is_symlink():
            resolved = path.resolve()
            if prefix not in resolved.parents and resolved != interpreter:
                raise ValueError("Unexpected external environment symlink")
            files.append(dict(path=name, kind="symlink", target=os.readlink(path)))
        elif getattr(path.lstat(), "st_file_attributes", 0) & 0x400:
            raise ValueError("Unexpected environment junction/reparse point")
        elif path.is_file():
            raw = path.read_bytes()
            files.append(dict(path=name, kind="file", bytes=len(raw), sha256=digest(raw), mode=path.stat().st_mode & 0o777))
    return dict(schema="maxim.python-installed.v1", prefix=str(prefix), files=files)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--venv", type=Path, required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--snapshot", type=Path)
    group.add_argument("--compare", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    prefix = Path(sys.prefix).resolve()
    if prefix != args.venv.resolve() or prefix == Path(sys.base_prefix).resolve():
        raise ValueError("Use the declared independent virtual environment")
    if os.environ.get("PYTHONPATH"):
        raise ValueError("Do not inject owner modules via PYTHONPATH")
    if os.environ.get("PYTHONDONTWRITEBYTECODE") != "1":
        raise ValueError("Set PYTHONDONTWRITEBYTECODE=1 to preserve installed bytes")
    config = dict(line.partition("=")[::2] for line in (prefix / "pyvenv.cfg").read_text().splitlines() if "=" in line)
    if not any(k.strip().lower() == "include-system-site-packages" and v.strip().lower() == "false" for k, v in config.items()):
        raise ValueError("Virtual environment includes system packages")
    generator = verify_generator()
    packages = []
    for dist in importlib.metadata.distributions():
        name = dist.metadata["Name"].lower().replace("_", "-")
        if name == "pip":
            continue
        location = Path(dist.locate_file("")).resolve()
        if name not in generator["distributions"] or prefix not in location.parents:
            raise ValueError("Unexpected distribution or owner site-package location")
        packages.append(dict(name=name, version=dist.version, location=str(location)))
    if len(packages) != len(generator["distributions"]):
        raise ValueError("Installed distribution closure differs")
    capsule_sha = (root / "python-inputs/sha256.txt").read_text().split()[0]
    manifest, data = verify((root / "python-inputs/inputs.zip").read_bytes(), capsule_sha, (root / "python-inputs/releases.json").read_bytes(), (root / "requirements-build.lock").read_bytes())
    cache = args.cache.resolve()
    expected = {"DEPENDENCY-NOTICES.txt", "requirements-hashes.txt"}
    for artifact in manifest["artifacts"]:
        kind = "wheels" if artifact["filename"].endswith(".whl") else "sources"
        path = cache / kind / artifact["filename"]
        if path.is_symlink() or path.read_bytes() != data[artifact["path"]]:
            raise ValueError("Restored Python artifact bytes differ")
        expected.add(kind + "/" + artifact["filename"])
    actual = set()
    for path in cache.rglob("*"):
        if path.is_symlink() or getattr(path.lstat(), "st_file_attributes", 0) & 0x400:
            raise ValueError("Restored Python cache contains a link/junction")
        if path.is_file():
            actual.add(path.relative_to(cache).as_posix())
    if actual != expected or (cache / "DEPENDENCY-NOTICES.txt").read_bytes() != data["DEPENDENCY-NOTICES.txt"]:
        raise ValueError("Restored Python cache inventory/notices differ")
    # Bind the generated offline requirements to only the verified wheel hashes.
    required = {}
    for artifact in manifest["artifacts"]:
        if artifact["filename"].endswith(".whl"):
            for role in artifact["roles"]:
                required.setdefault((role["package"], role["version"]), set()).add(artifact["sha256"])
    lines = [name + "==" + version + " " + " ".join("--hash=sha256:" + h for h in sorted(hashes)) for (name, version), hashes in sorted(required.items())]
    if (cache / "requirements-hashes.txt").read_text().splitlines() != lines:
        raise ValueError("Restored Python hash requirements differ")
    state = snapshot(prefix)
    if args.snapshot:
        output = destination(args.snapshot)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(state, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        snapshot_sha = digest(output.read_bytes())
    else:
        previous = json.loads(args.compare.read_bytes())
        if state != previous:
            raise ValueError("Installed environment changed during build")
        snapshot_sha = digest(args.compare.read_bytes())
    print(json.dumps(dict(packages=len(packages), artifacts=len(manifest["artifacts"]), capsule_sha256=capsule_sha, prefix=str(prefix), all_package_locations_in_venv=True, complete_cache_bytes_verified=True, installed_files=len(state["files"]), installed_snapshot_sha256=snapshot_sha, compared=bool(args.compare), scope="Entire installed venv snapshot includes installed sources/binaries/metadata and prerequisite pip/launcher files. Bytecode writing is disabled. Original archives/notices checked; third-party wheel builds were not reproduced.")))


if __name__ == "__main__":
    main()
