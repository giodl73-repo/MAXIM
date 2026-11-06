import copy
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import python_custody as custody

ROOT = Path(__file__).resolve().parents[1]


class PythonCustodyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = (ROOT / "python-inputs/inputs.zip").read_bytes()
        cls.sha = (ROOT / "python-inputs/sha256.txt").read_text().split()[0]
        cls.catalog_raw = (ROOT / "python-inputs/releases.json").read_bytes()
        cls.catalog = json.loads(cls.catalog_raw)
        cls.lock = (ROOT / "requirements-build.lock").read_bytes()
        cls.manifest, cls.data = custody.verify(cls.raw, cls.sha, cls.catalog_raw, cls.lock)

    def repack(self, changes=None, mutate=None, catalog=None, modes=None):
        data = dict(self.data)
        data.update(changes or {})
        manifest = copy.deepcopy(self.manifest)
        catalog_raw = json.dumps(catalog, sort_keys=True, indent=2).encode() + b"\n" if catalog is not None else self.catalog_raw.replace(b"\r\n", b"\n")
        manifest["catalog_sha256"] = custody.digest(catalog_raw)
        if mutate:
            mutate(manifest, data)
        manifest["files"] = [dict(path=name, bytes=len(value), sha256=custody.digest(value)) for name, value in data.items() if name != "INPUT-MANIFEST.json"]
        data["INPUT-MANIFEST.json"] = json.dumps(manifest).encode()
        result = io.BytesIO()
        with zipfile.ZipFile(result, "w") as archive:
            for name, value in data.items():
                row = zipfile.ZipInfo(name)
                row.create_system = 3
                row.external_attr = (modes or {}).get(name, 0o100644) << 16
                row.compress_type = zipfile.ZIP_DEFLATED if name in ("INPUT-MANIFEST.json", "DEPENDENCY-NOTICES.txt") else zipfile.ZIP_STORED
                archive.writestr(row, value)
        return result.getvalue(), catalog_raw

    def reject(self, packed, message):
        raw, catalog = packed
        with self.assertRaisesRegex(ValueError, message):
            custody.verify(raw, custody.digest(raw), catalog, self.lock)

    def test_complete_capsule(self):
        self.assertEqual(len(self.manifest["artifacts"]), 62)
        self.assertEqual(sum(len(a["files"]) for a in self.manifest["artifacts"]), 39635)
        self.assertEqual(len(self.catalog["packages"]), 29)

    def test_outer_sha_and_lock(self):
        with self.assertRaisesRegex(ValueError, "capsule SHA"):
            custody.verify(self.raw + b"bad", self.sha, self.catalog_raw, self.lock)
        with self.assertRaisesRegex(ValueError, "catalog/lock"):
            custody.verify(self.raw, self.sha, self.catalog_raw, self.lock + b"#bad\n")

    def test_windows_checkout_line_endings(self):
        manifest, _ = custody.verify(self.raw, self.sha, self.catalog_raw.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n"), self.lock.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n"))
        self.assertEqual(manifest, self.manifest)

    def test_original_artifact_cannot_be_rebound(self):
        artifact = self.manifest["artifacts"][0]
        self.reject(self.repack({artifact["path"]: self.data[artifact["path"]] + b"changed"}), "upstream artifact checksum")

    def test_member_modes_and_notice_inventory(self):
        def mode(manifest, _):
            manifest["artifacts"][0]["files"][0]["mode"] ^= 0o111
        self.reject(self.repack(mutate=mode), "release member/identity")
        def grants(manifest, _):
            manifest["artifacts"][0]["grants"] = []
        self.reject(self.repack(mutate=grants), "notice inventory")

    def test_missing_source_and_role(self):
        def remove(manifest, _):
            manifest["artifacts"].pop()
        self.reject(self.repack(mutate=remove), "artifact closure")
        def role(manifest, _):
            manifest["artifacts"][0]["roles"].pop()
        self.reject(self.repack(mutate=role), "Artifact roles")

    def test_notices_cannot_be_pruned(self):
        self.reject(self.repack({"DEPENDENCY-NOTICES.txt": b"Use original terms\n"}), "notice bytes")

    def test_unsafe_wire_paths_and_modes(self):
        for name in ("../escape", "C:escape", "NUL.txt"):
            with self.subTest(name=name):
                self.reject(self.repack({name: b"bad"}), "Unsafe input path")
        self.reject(self.repack({"dependency-notices.txt": b"case alias"}), "Unsafe Python capsule")
        self.reject(self.repack({"artifacts": b"file parent"}), "Ancestor Python capsule")
        self.reject(self.repack(modes={"DEPENDENCY-NOTICES.txt": 0o120777}), "Unsafe Python capsule")
        raw, catalog = self.repack({"proof/wire_marker_20261105": b"bad"})
        self.assertEqual(raw.count(b"proof/wire_marker_20261105"), 2)
        self.reject((raw.replace(b"proof/wire_marker_20261105", b"proof\\wire_marker_20261105"), catalog), "Unsafe input path")

    def test_unreferenced_file_and_resource_count(self):
        self.reject(self.repack({"unexpected.txt": b"extra"}), "Unreferenced Python capsule")
        self.reject(self.repack({f"extra/{i:03}": b"" for i in range(257)}), "resource limit")

    def test_catalog_package_and_role_closure(self):
        catalog = copy.deepcopy(self.catalog)
        catalog["packages"].pop(next(iter(catalog["packages"])))
        self.reject(self.repack(catalog=catalog), "dependency/role closure")

    def test_corrupt_wheel_record_with_upstream_hash_rebound(self):
        # Simulate a newly catalogued upstream artifact whose internal RECORD
        # no longer describes its actual bytes. Outer hashes alone must not pass.
        artifact = self.manifest["artifacts"][0]
        buffer = io.BytesIO()
        with zipfile.ZipFile(io.BytesIO(self.data[artifact["path"]])) as source, zipfile.ZipFile(buffer, "w") as target:
            changed = False
            for row in source.infolist():
                value = source.read(row)
                if row.filename.endswith(".py") and not changed:
                    value += b"\n#changed\n"
                    changed = True
                target.writestr(row, value)
        self.assertTrue(changed)
        value = buffer.getvalue()
        replacement = custody.digest(value)
        catalog = copy.deepcopy(self.catalog)
        for package in catalog["packages"].values():
            for role in package["roles"].values():
                if role["sha256"] == artifact["sha256"]:
                    role.update(sha256=replacement, bytes=len(value))
        def mutate(manifest, data):
            item = manifest["artifacts"][0]
            data.pop(item["path"])
            item.update(sha256=replacement, bytes=len(value), path="artifacts/" + replacement + "/" + item["filename"])
            data[item["path"]] = value
        self.reject(self.repack(mutate=mutate, catalog=catalog), "Wheel RECORD hash/size")

    def test_restore_all_original_archives(self):
        with tempfile.TemporaryDirectory(prefix="maxim-python-inputs-") as directory:
            root = Path(directory).resolve()
            self.assertIn(Path(tempfile.gettempdir()).resolve(), root.parents)
            output = custody.restore(self.manifest, self.data, root / "cache")
            for artifact in self.manifest["artifacts"]:
                folder = "wheels" if artifact["filename"].endswith(".whl") else "sources"
                self.assertEqual((output / folder / artifact["filename"]).read_bytes(), self.data[artifact["path"]])
            self.assertEqual(len((output / "requirements-hashes.txt").read_text().splitlines()), 29)
            self.assertEqual((output / "DEPENDENCY-NOTICES.txt").read_bytes(), self.data["DEPENDENCY-NOTICES.txt"])

    def test_restore_existing_source_and_target(self):
        with tempfile.TemporaryDirectory(prefix="maxim-python-dest-") as directory:
            root = Path(directory).resolve()
            self.assertIn(Path(tempfile.gettempdir()).resolve(), root.parents)
            existing = root / "existing"
            existing.mkdir()
            (existing / "marker").write_bytes(b"keep")
            with self.assertRaisesRegex(ValueError, "new destination"):
                custody.restore(self.manifest, self.data, existing)
            with self.assertRaisesRegex(ValueError, "outside source/compiled target"):
                custody.restore(self.manifest, self.data, ROOT / "new-python-proof-never-created")
            with patch.dict(os.environ, {"CARGO_TARGET_DIR": str(root / "target")}):
                with self.assertRaisesRegex(ValueError, "outside source/compiled target"):
                    custody.restore(self.manifest, self.data, root / "target/cache")
            self.assertEqual((existing / "marker").read_bytes(), b"keep")
            self.assertFalse((root / "target").exists())

    def test_restore_link_or_junction_before_writes(self):
        with tempfile.TemporaryDirectory(prefix="maxim-python-link-") as directory:
            root = Path(directory).resolve()
            self.assertIn(Path(tempfile.gettempdir()).resolve(), root.parents)
            target = root / "target"
            target.mkdir()
            (target / "marker").write_bytes(b"keep")
            link = root / "link"
            if os.name == "nt":
                subprocess.run([os.environ.get("COMSPEC", "cmd.exe"), "/c", "mklink", "/J", str(link), str(target)], check=True, capture_output=True)
            else:
                link.symlink_to(target, target_is_directory=True)
            try:
                with self.assertRaisesRegex(ValueError, "link/junction"):
                    custody.restore(self.manifest, self.data, link / "cache")
                self.assertFalse((target / "cache").exists())
                self.assertEqual((target / "marker").read_bytes(), b"keep")
            finally:
                self.assertEqual(link.resolve(), target.resolve())
                link.rmdir() if os.name == "nt" else link.unlink()


if __name__ == "__main__":
    unittest.main()
