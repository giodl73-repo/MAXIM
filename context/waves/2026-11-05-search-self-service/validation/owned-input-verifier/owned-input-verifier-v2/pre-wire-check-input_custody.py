"""Verify MAXIM's complete locked registry inputs before restoring new folders.

Python3.11+. No package acquisition or downloaded-code execution. A trusted
external capsule SHA anchors integrity; it does not establish authorship.
"""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import tarfile
import tomllib
import zipfile

CONFIG = b'[source.crates-io]\nreplace-with = "vendored-sources"\n\n[source.vendored-sources]\ndirectory = "vendor"\n'
NOTICE_NAMES = ("LICENSE", "LICENCE", "COPYING", "COPYRIGHT", "NOTICE")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def safe_path(name):
    path = PurePosixPath(name)
    reserved = {"CON", "PRN", "AUX", "NUL"} | {f"{stem}{i}" for stem in ("COM", "LPT") for i in range(1, 10)}
    if (not name or name == "." or str(path) != name or path.is_absolute() or "\\" in name or ":" in name
            or any(p in (".", "..") or p.rstrip(" .") != p or p.split(".")[0].upper() in reserved for p in path.parts)):
        raise ValueError("Unsafe input path: " + name)


def strict_json(raw):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("Duplicate JSON key")
            result[key] = value
        return result
    return json.loads(raw, object_pairs_hook=unique)


def verify(raw, expected_sha, lock):
    if digest(raw) != expected_sha:
        raise ValueError("Input capsule SHA mismatch")
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        rows = archive.infolist()
        if len(rows) > 10000 or sum(x.file_size for x in rows) > 128 * 1024 * 1024:
            raise ValueError("Input capsule resource limit")
        names = [x.filename for x in rows]
        for name in names:
            safe_path(name)
        folded = {name.casefold() for name in names}
        if len(folded) != len(names) or any(str(parent).casefold() in folded for name in names for parent in PurePosixPath(name).parents if str(parent) != "."):
            raise ValueError("Duplicate, case-colliding or ancestor input path")
        modes = {row.filename: row.external_attr >> 16 for row in rows}
        if any(mode not in (0o100644, 0o100755) for mode in modes.values()):
            raise ValueError("Only regular source file modes are supported")
        data = {name: archive.read(name) for name in names}
    manifest = strict_json(data["INPUT-MANIFEST.json"])
    if manifest["schema"] != "maxim.cargo-inputs.v1" or manifest["git_sources"]:
        raise ValueError("Unsupported input schema or source kind")
    inventory = manifest["files"]
    if len({r["path"] for r in inventory}) != len(inventory) or set(data) != {r["path"] for r in inventory} | {"INPUT-MANIFEST.json"}:
        raise ValueError("Input file inventory mismatch")
    for row in inventory:
        value = data[row["path"]]
        if len(value) != row["bytes"] or digest(value) != row["sha256"]:
            raise ValueError("Input file hash mismatch: " + row["path"])
    canonical = lock.replace(b"\r\n", b"\n")
    blob = hashlib.sha1(b"blob " + str(len(canonical)).encode() + b"\0" + canonical).hexdigest()
    if digest(canonical) != manifest["lock_sha256"] or blob != manifest["lock_git_blob"]:
        raise ValueError("Cargo.lock identity mismatch")
    packages = {(p["name"], p["version"], p["source"]): p for p in tomllib.loads(lock.decode())["package"] if p.get("source")}
    registry = manifest["registry"]
    keys = [(p["name"], p["version"], p["source"]) for p in registry]
    if len(set(keys)) != len(keys) or set(keys) != set(packages) or any(not p[2].startswith("registry+") for p in keys):
        raise ValueError("Locked dependency closure differs")
    if data["CARGO-CONFIG.toml"] != CONFIG:
        raise ValueError("Unexpected Cargo source configuration")
    allowed = {"INPUT-MANIFEST.json", "CARGO-CONFIG.toml", "DEPENDENCY-NOTICES.txt"}
    for package in registry:
        name, version, source = package["name"], package["version"], package["source"]
        checksum = package["checksum"]
        archive_name = f"original-registry/{name}-{version}.crate"
        if package["archive"] != archive_name or packages[(name, version, source)]["checksum"] != checksum or digest(data[archive_name]) != checksum:
            raise ValueError("Original registry archive checksum mismatch")
        allowed.add(archive_name)
        prefix = f"vendor/{name}-{version}/"
        members = {}
        size = 0
        with tarfile.open(fileobj=io.BytesIO(data[archive_name]), mode="r:gz") as archive:
            for member in archive:
                if member.isdir():
                    continue
                if not member.isfile() or not member.name.startswith(f"{name}-{version}/"):
                    raise ValueError("Unsafe registry member")
                relative = member.name[len(f"{name}-{version}/"):]
                safe_path(relative)
                size += member.size
                if relative in members or len(members) >= 10000 or size > 128 * 1024 * 1024:
                    raise ValueError("Registry member inventory/resource limit")
                value = archive.extractfile(member).read()
                destination = prefix + relative
                if data[destination] != value or modes[destination] != 0o100000 | (member.mode & 0o777):
                    raise ValueError("Vendor bytes/mode differ from original registry member")
                members[relative] = digest(value)
                allowed.add(destination)
        if members != package["files"]:
            raise ValueError("Registry member inventory mismatch")
        checksum_path = prefix + ".cargo-checksum.json"
        checks = strict_json(data[checksum_path])
        allowed.add(checksum_path)
        actual = {p[len(prefix):]: digest(v) for p, v in data.items() if p.startswith(prefix) and p != checksum_path}
        if checks["files"] != members or actual != members or checks["package"] != checksum:
            raise ValueError("Cargo vendor checksum mismatch")
        grants = {row["path"]: row for row in package["grants"]}
        expected_grants = {p for p in members if PurePosixPath(p).name.upper().startswith(NOTICE_NAMES)}
        if not expected_grants or len(grants) != len(package["grants"]) or set(grants) != expected_grants:
            raise ValueError("Original grants/notices inventory differs")
        for relative, row in grants.items():
            value = data[prefix + relative]
            label = f"\n\n===== {name} {version} / {relative} =====\n".encode()
            if row["sha256"] != digest(value) or row["bytes"] != len(value) or label + value not in data["DEPENDENCY-NOTICES.txt"]:
                raise ValueError("Original grants/notices bytes differ")
    if set(data) != allowed:
        raise ValueError("Unreferenced capsule files")
    return manifest, data, modes


def destination(path):
    # Inspect lexical parents before resolve() follows a junction or symlink.
    path = Path(path)
    lexical = path if path.is_absolute() else Path.cwd() / path
    for part in [lexical, *lexical.parents]:
        if part.is_symlink() or (part.exists() and getattr(part.lstat(), "st_file_attributes", 0) & 0x400):
            raise ValueError("Destination uses a link/junction")
    resolved = lexical.resolve()
    if resolved.exists():
        raise ValueError("Use a new destination; existing files are preserved")
    return resolved


def restore(data, modes, inputs, cargo_home):
    inputs, cargo_home = destination(inputs), destination(cargo_home)
    repo = Path(__file__).resolve().parents[1]
    targets = [repo / "target"]
    if os.environ.get("CARGO_TARGET_DIR"):
        targets.append(Path(os.environ["CARGO_TARGET_DIR"]).resolve())
    for path in (inputs, cargo_home):
        if path == repo or repo in path.parents:
            raise ValueError("Keep inputs outside the source repository")
        if any(path == t or t in path.parents or path in t.parents for t in targets):
            raise ValueError("Destination overlaps compiled target")
    if inputs == cargo_home or inputs in cargo_home.parents or cargo_home in inputs.parents:
        raise ValueError("Input and Cargo home folders must be separate")
    # All destination checks finish before creating either folder.
    inputs.mkdir(parents=True)
    cargo_home.mkdir(parents=True)
    for name, value in data.items():
        if name.startswith("vendor/"):
            path = inputs / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(value)
            path.chmod(modes[name] & 0o777)
    config = CONFIG.decode().replace('directory = "vendor"', 'directory = ' + json.dumps((inputs / "vendor").as_posix()))
    (cargo_home / "config.toml").write_text(config + "\n[net]\noffline = true\n", encoding="utf-8")
    return inputs, cargo_home


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capsule", type=Path, default=Path(__file__).resolve().parents[1] / "cargo-inputs/inputs.zip")
    parser.add_argument("--sha256", required=True)
    parser.add_argument("--lock", type=Path, default=Path(__file__).resolve().parents[1] / "Cargo.lock")
    parser.add_argument("--inputs", type=Path)
    parser.add_argument("--cargo-home", type=Path)
    args = parser.parse_args()
    manifest, data, modes = verify(args.capsule.read_bytes(), args.sha256, args.lock.read_bytes())
    if bool(args.inputs) != bool(args.cargo_home):
        parser.error("Supply both --inputs and --cargo-home")
    if args.inputs:
        restore(data, modes, args.inputs, args.cargo_home)
    print(json.dumps(dict(verified=True, packages=len(manifest["registry"]), files=len(manifest["files"]), restored=bool(args.inputs))))


if __name__ == "__main__":
    main()
