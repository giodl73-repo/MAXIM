"""Verify original Python build artifacts and restore an offline archive cache.

No downloaded Python code is executed. Source archives remain unextracted.
Use a capsule SHA and release catalog from a trusted checkout/release receipt.
"""
import argparse
import base64
import csv
from email.parser import BytesParser
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import tarfile
import zipfile

from input_custody import destination, digest, safe_path, strict_json

ROLES = {"original-sdist", "windows-cp312-wheel", "linux-cp312-wheel"}
NOTICE_NAMES = ("LICENSE", "LICENCE", "COPYING", "COPYRIGHT", "NOTICE", "AUTHORS", "CREDITS")


def canonical(name):
    return name.lower().replace("_", "-")


def lock_identity(raw):
    raw = raw.replace(b"\r\n", b"\n")
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    pins = {}
    for line in raw.decode().splitlines():
        if not line or line.startswith(("#", "-r ")):
            continue
        name, separator, version = line.partition("==")
        if not separator or not version or " " in line or canonical(name) in pins:
            raise ValueError("Expected unique exact Python pins")
        pins[canonical(name)] = version
    return digest(raw), blob, pins


def archive_members(raw, filename):
    members, values = [], {}
    if filename.endswith(".whl"):
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            rows = archive.infolist()
            if len(rows) > 100000 or sum(r.file_size for r in rows) > 512 * 1024 * 1024:
                raise ValueError("Nested artifact resource limit")
            folded = set()
            for row in rows:
                if row.is_dir():
                    continue
                safe_path(row.orig_filename)
                if row.orig_filename != row.filename or row.filename.casefold() in folded or row.external_attr >> 16 & 0o170000 == 0o120000:
                    raise ValueError("Unsafe wheel member")
                folded.add(row.filename.casefold())
                value = archive.read(row)
                values[row.filename] = value
                members.append(dict(path=row.filename, bytes=len(value), sha256=digest(value), mode=row.external_attr >> 16, kind="file"))
        records = [p for p in values if p.endswith(".dist-info/RECORD")]
        if len(records) != 1:
            raise ValueError("Wheel RECORD missing or ambiguous")
        seen = set()
        for name, encoded, size in csv.reader(io.StringIO(values[records[0]].decode())):
            if name not in values or name in seen:
                raise ValueError("Wheel RECORD inventory mismatch")
            seen.add(name)
            if encoded:
                algorithm, expected = encoded.split("=", 1)
                if algorithm not in ("sha256", "sha384", "sha512"):
                    raise ValueError("Unsupported wheel RECORD digest")
                actual = base64.urlsafe_b64encode(hashlib.new(algorithm, values[name]).digest()).decode().rstrip("=")
                if actual != expected or len(values[name]) != int(size):
                    raise ValueError("Wheel RECORD hash/size mismatch")
            elif name != records[0]:
                raise ValueError("Unhashed wheel member")
        if seen != set(values):
            raise ValueError("Wheel RECORD omits members")
        metadata = [p for p in values if p.endswith(".dist-info/METADATA")]
        if len(metadata) != 1:
            raise ValueError("Wheel metadata missing or ambiguous")
        identity = BytesParser().parsebytes(values[metadata[0]])
    else:
        total = 0
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:*") as archive:
            for row in archive:
                if row.isdir():
                    continue
                safe_path(row.name)
                if row.name in values or not row.isfile():
                    raise ValueError("Unsupported source archive member")
                total += row.size
                if len(members) >= 100000 or total > 512 * 1024 * 1024:
                    raise ValueError("Nested artifact resource limit")
                value = archive.extractfile(row).read()
                values[row.name] = value
                members.append(dict(path=row.name, bytes=len(value), sha256=digest(value), mode=row.mode, kind="file"))
        metadata = [p for p in values if PurePosixPath(p).name == "PKG-INFO"]
        if not metadata:
            raise ValueError("Source release metadata missing")
        shortest = min(len(PurePosixPath(p).parts) for p in metadata)
        metadata = [p for p in metadata if len(PurePosixPath(p).parts) == shortest]
        if len(metadata) != 1:
            raise ValueError("Ambiguous source release metadata")
        identity = BytesParser().parsebytes(values[metadata[0]])
    if len(members) > 100000 or sum(x["bytes"] for x in members) > 512 * 1024 * 1024:
        raise ValueError("Nested artifact resource limit")
    grants = {}
    for name, value in values.items():
        parts = [p.lower() for p in PurePosixPath(name).parts]
        if PurePosixPath(name).name.upper().startswith(NOTICE_NAMES) or "licenses" in parts or "licences" in parts:
            grants[name] = value
    if not grants:
        raise ValueError("Original grant/attribution files missing")
    if not identity["Name"] or not identity["Version"]:
        raise ValueError("Original release identity missing")
    return members, grants, canonical(identity["Name"]), identity["Version"]


def verify(raw, expected_sha, catalog_raw, lock):
    if digest(raw) != expected_sha:
        raise ValueError("Python capsule SHA mismatch")
    catalog_raw = catalog_raw.replace(b"\r\n", b"\n")
    catalog = strict_json(catalog_raw)
    lock_sha, blob, pins = lock_identity(lock)
    if catalog["schema"] != "maxim.python-releases.v1" or catalog["python"] != "3.12.16" or catalog["lock_sha256"] != lock_sha or catalog["lock_git_blob"] != blob:
        raise ValueError("Python catalog/lock identity mismatch")
    packages = catalog["packages"]
    if ({name: p["version"] for name, p in packages.items()} != pins
            or any(canonical(p["name"]) != name or set(p["roles"]) != ROLES for name, p in packages.items())):
        raise ValueError("Python dependency/role closure differs")
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        rows = archive.infolist()
        if len(rows) > 256 or sum(r.file_size for r in rows) > 256 * 1024 * 1024:
            raise ValueError("Python capsule resource limit")
        names = set()
        for row in rows:
            safe_path(row.orig_filename)
            if row.orig_filename != row.filename or row.filename.casefold() in names or row.external_attr >> 16 != 0o100644:
                raise ValueError("Unsafe Python capsule member")
            names.add(row.filename.casefold())
        if any(str(parent).casefold() in names for row in rows for parent in PurePosixPath(row.filename).parents if str(parent) != "."):
            raise ValueError("Ancestor Python capsule member")
        data = {r.filename: archive.read(r) for r in rows}
    manifest = strict_json(data["INPUT-MANIFEST.json"])
    if (manifest["schema"] != "maxim.python-inputs.v1" or manifest["python"] != catalog["python"]
            or manifest["catalog_sha256"] != digest(catalog_raw) or manifest["lock_sha256"] != lock_sha or manifest["lock_git_blob"] != blob):
        raise ValueError("Python manifest identity mismatch")
    inventory = manifest["files"]
    if len({p["path"] for p in inventory}) != len(inventory) or set(data) != {p["path"] for p in inventory} | {"INPUT-MANIFEST.json"}:
        raise ValueError("Python capsule inventory differs")
    for row in inventory:
        value = data[row["path"]]
        if len(value) != row["bytes"] or digest(value) != row["sha256"]:
            raise ValueError("Python capsule file hash mismatch")
    expected = {}
    for package in packages.values():
        for role, row in package["roles"].items():
            expected.setdefault(row["sha256"], []).append((canonical(package["name"]), package["version"], role, row))
    artifacts = manifest["artifacts"]
    if (len({a["sha256"] for a in artifacts}) != len(artifacts)
            or len({a["filename"].casefold() for a in artifacts}) != len(artifacts)
            or {a["sha256"] for a in artifacts} != set(expected)):
        raise ValueError("Python artifact closure differs")
    allowed = {"INPUT-MANIFEST.json", "DEPENDENCY-NOTICES.txt"}
    member_count = 0
    for artifact in artifacts:
        rows = expected[artifact["sha256"]]
        filename = artifact["filename"]
        safe_path(filename)
        if "/" in filename or artifact["path"] != "artifacts/" + artifact["sha256"] + "/" + filename:
            raise ValueError("Unexpected artifact path")
        value = data[artifact["path"]]
        if any(r["filename"] != filename or r["bytes"] != len(value) for _, _, _, r in rows) or digest(value) != artifact["sha256"] or artifact["bytes"] != len(value):
            raise ValueError("Original upstream artifact checksum differs")
        roles = {(canonical(p["package"]), p["version"], p["kind"]) for p in artifact["roles"]}
        if len(roles) != len(artifact["roles"]) or roles != {(name, version, role) for name, version, role, _ in rows}:
            raise ValueError("Artifact roles differ")
        members, grants, name, version = archive_members(value, filename)
        if any(name != n or version != v for n, v, _, _ in rows) or members != artifact["files"]:
            raise ValueError("Original release member/identity differs")
        member_count += len(members)
        if member_count > 100000:
            raise ValueError("Python artifact member count limit")
        recorded = {p["path"]: p for p in artifact["grants"]}
        if len(recorded) != len(artifact["grants"]) or set(recorded) != set(grants):
            raise ValueError("Original Python notice inventory differs")
        for path, content in grants.items():
            row = recorded[path]
            label = f"\n\n===== {filename} / {path} =====\n".encode()
            if row["bytes"] != len(content) or row["sha256"] != digest(content) or label + content not in data["DEPENDENCY-NOTICES.txt"]:
                raise ValueError("Original Python notice bytes differ")
        allowed.add(artifact["path"])
    if set(data) != allowed:
        raise ValueError("Unreferenced Python capsule files")
    return manifest, data


def restore(manifest, data, output):
    output = destination(output)
    root = Path(__file__).resolve().parents[1]
    targets = [root / "target"]
    if os.environ.get("CARGO_TARGET_DIR"):
        targets.append(Path(os.environ["CARGO_TARGET_DIR"]).resolve())
    if root == output or root in output.parents or any(output == t or t in output.parents or output in t.parents for t in targets):
        raise ValueError("Keep Python inputs outside source/compiled target")
    # All paths and content have been verified before creating this new folder.
    output.mkdir(parents=True)
    lines = []
    for artifact in manifest["artifacts"]:
        role = "wheels" if artifact["filename"].endswith(".whl") else "sources"
        path = output / role / artifact["filename"]
        path.parent.mkdir(exist_ok=True)
        path.write_bytes(data[artifact["path"]])
    packages = {}
    for artifact in manifest["artifacts"]:
        if artifact["filename"].endswith(".whl"):
            for row in artifact["roles"]:
                packages.setdefault((row["package"], row["version"]), set()).add(artifact["sha256"])
    for (name, version), hashes in sorted(packages.items()):
        lines.append(name + "==" + version + " " + " ".join("--hash=sha256:" + h for h in sorted(hashes)))
    (output / "requirements-hashes.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (output / "DEPENDENCY-NOTICES.txt").write_bytes(data["DEPENDENCY-NOTICES.txt"])
    return output


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capsule", type=Path, default=root / "python-inputs/inputs.zip")
    parser.add_argument("--catalog", type=Path, default=root / "python-inputs/releases.json")
    parser.add_argument("--lock", type=Path, default=root / "requirements-build.lock")
    parser.add_argument("--sha256", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    manifest, data = verify(args.capsule.read_bytes(), args.sha256, args.catalog.read_bytes(), args.lock.read_bytes())
    if args.output:
        restore(manifest, data, args.output)
    print(json.dumps(dict(verified=True, artifacts=len(manifest["artifacts"]), packages=len(lock_identity(args.lock.read_bytes())[2]), members=sum(len(a["files"]) for a in manifest["artifacts"]), restored=bool(args.output))))


if __name__ == "__main__":
    main()
