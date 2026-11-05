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

import input_custody as custody

ROOT = Path(__file__).resolve().parents[1]


class InputCustodyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = (ROOT / "cargo-inputs/inputs.zip").read_bytes()
        cls.sha = (ROOT / "cargo-inputs/sha256.txt").read_text().split()[0]
        cls.lock = (ROOT / "Cargo.lock").read_bytes()
        cls.manifest, cls.data, cls.modes = custody.verify(cls.raw, cls.sha, cls.lock)

    def repack(self, changes=None, mutate=None, modes=None, duplicate_manifest=False):
        data = dict(self.data)
        data.update(changes or {})
        manifest = copy.deepcopy(self.manifest)
        if mutate:
            mutate(manifest)
        manifest["files"] = [dict(path=name, bytes=len(value), sha256=custody.digest(value)) for name, value in data.items() if name != "INPUT-MANIFEST.json"]
        data["INPUT-MANIFEST.json"] = json.dumps(manifest).encode()
        if duplicate_manifest:
            data["INPUT-MANIFEST.json"] = b'{"schema":"maxim.cargo-inputs.v1",' + data["INPUT-MANIFEST.json"][1:]
        result = io.BytesIO()
        with zipfile.ZipFile(result, "w") as archive:
            for name, value in data.items():
                info = zipfile.ZipInfo(name)
                info.create_system = 3
                info.external_attr = (modes or {}).get(name, self.modes.get(name, 0o100644)) << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, value)
        return result.getvalue()

    def reject(self, raw, message):
        with self.assertRaisesRegex(ValueError, message):
            custody.verify(raw, custody.digest(raw), self.lock)

    def test_complete_original_and_crlf_lock(self):
        self.assertEqual(len(self.manifest["registry"]), 20)
        manifest, _, _ = custody.verify(self.raw, self.sha, self.lock.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n"))
        self.assertEqual(manifest, self.manifest)

    def test_outer_sha_and_lock_identity(self):
        with self.assertRaisesRegex(ValueError, "capsule SHA"):
            custody.verify(self.raw + b"changed", self.sha, self.lock)
        with self.assertRaisesRegex(ValueError, "lock identity"):
            custody.verify(self.raw, self.sha, self.lock + b"#changed\n")

    def test_original_archive_checksum_even_if_inventory_rebound(self):
        package = self.manifest["registry"][0]
        self.reject(self.repack({package["archive"]: self.data[package["archive"]] + b"changed"}), "archive checksum")

    def test_vendor_cannot_be_rebound_away_from_original(self):
        package = self.manifest["registry"][0]
        relative = "README.md"
        name = f"vendor/{package['name']}-{package['version']}/{relative}"
        value = self.data[name] + b"changed"
        checksum_path = name.rsplit("/", 1)[0] + "/.cargo-checksum.json"
        checks = json.loads(self.data[checksum_path])
        checks["files"][relative] = custody.digest(value)
        def mutate(manifest):
            manifest["registry"][0]["files"][relative] = custody.digest(value)
        self.reject(self.repack({name: value, checksum_path: json.dumps(checks).encode()}, mutate), "Vendor bytes/mode")

    def test_source_modes_and_symlinks(self):
        path = "vendor/bumpalo-3.20.3/README.md"
        self.reject(self.repack(modes={path: 0o120777}), "regular source file")
        self.reject(self.repack(modes={path: 0o100755}), "Vendor bytes/mode")

    def test_unsafe_case_and_ancestor_paths(self):
        for name in ("../escape", "C:escape", "vendor/CON.txt", "vendor/space. "):
            with self.subTest(name=name):
                self.reject(self.repack({name: b"bad"}), "Unsafe input path")
        self.reject(self.repack({"vendor": b"ancestor"}), "ancestor input path")
        self.reject(self.repack({"dependency-notices.txt": b"duplicate"}), "case-colliding")
        # ZipInfo normalizes Windows backslashes when constructing a ZIP. Mutate
        # both filename headers to exercise an actually unsafe wire filename.
        raw = self.repack({"vendor/escape": b"bad"})
        self.assertEqual(raw.count(b"vendor/escape"), 2)
        self.reject(raw.replace(b"vendor/escape", b"vendor\\escape"), "Unsafe input path")
        self.reject(raw.replace(b"vendor/escape", b"vendor/\x00scape"), "Unsafe input path")

    def test_unreferenced_files_and_source_configuration(self):
        self.reject(self.repack({"unreferenced.txt": b"not a locked source"}), "Unreferenced")
        self.reject(self.repack({"CARGO-CONFIG.toml": self.data["CARGO-CONFIG.toml"] + b"\n[build]\ntarget-dir='elsewhere'\n"}), "source configuration")

    def test_missing_dependency_and_grants(self):
        self.reject(self.repack(mutate=lambda m: m["registry"].pop()), "dependency closure")
        self.reject(self.repack(mutate=lambda m: m["registry"][0].update(grants=[])), "grants/notices inventory")

    def test_schema_and_source_kind(self):
        for change in (dict(schema="different-project.v1"), dict(git_sources={}), dict(git_sources=[{"source": "git+unknown"}])):
            with self.subTest(change=change):
                self.reject(self.repack(mutate=lambda m: m.update(change)), "Unsupported input schema or source kind")

    def test_notices_cannot_be_pruned_with_new_hashes(self):
        self.reject(self.repack({"DEPENDENCY-NOTICES.txt": b"MIT dependencies\n"}), "grants/notices bytes")

    def test_duplicate_json_keys(self):
        self.reject(self.repack(duplicate_manifest=True), "Duplicate JSON key")

    def test_resource_count(self):
        changes = {f"extra/{i:05}.txt": b"" for i in range(10001)}
        self.reject(self.repack(changes), "resource limit")

    def test_positive_restore_preserves_every_vendor_file(self):
        with tempfile.TemporaryDirectory(prefix="maxim-input-proof-") as directory:
            root = Path(directory).resolve()
            self.assertIn(Path(tempfile.gettempdir()).resolve(), root.parents)
            inputs, home = custody.restore(self.data, self.modes, root / "inputs", root / "home")
            for name, expected in self.data.items():
                if name.startswith("vendor/"):
                    path = inputs / name
                    self.assertEqual(path.read_bytes(), expected)
                    if os.name != "nt":
                        self.assertEqual(path.stat().st_mode & 0o777, self.modes[name] & 0o777)
            config = (home / "config.toml").read_text()
            self.assertIn((inputs / "vendor").as_posix(), config)
            self.assertIn("offline = true", config)
            self.assertFalse((home / "registry").exists())
            self.assertFalse((home / "git").exists())

    def test_existing_and_paired_destination_checks_write_nothing(self):
        with tempfile.TemporaryDirectory(prefix="maxim-input-destination-") as directory:
            root = Path(directory).resolve()
            self.assertIn(Path(tempfile.gettempdir()).resolve(), root.parents)
            existing = root / "existing"
            existing.mkdir()
            (existing / "marker").write_bytes(b"preserve")
            for first, second in [(existing, root / "home"), (root / "inputs", existing)]:
                with self.assertRaisesRegex(ValueError, "new destination"):
                    custody.restore(self.data, self.modes, first, second)
            self.assertEqual((existing / "marker").read_bytes(), b"preserve")
            self.assertFalse((root / "inputs").exists())
            self.assertFalse((root / "home").exists())

    def test_overlapping_source_target_and_input_home(self):
        with tempfile.TemporaryDirectory(prefix="maxim-input-overlap-") as directory:
            root = Path(directory).resolve()
            self.assertIn(Path(tempfile.gettempdir()).resolve(), root.parents)
            with patch.dict(os.environ, {"CARGO_TARGET_DIR": str(root / "target")}):
                for inputs, home, message in [
                    (root / "same", root / "same", "separate"),
                    (root / "inputs", root / "inputs/home", "separate"),
                    (ROOT / "new-input-proof-never-created", root / "home", "source repository"),
                    (root / "target/new", root / "home", "compiled target"),
                    (root / "inputs", ROOT / "target/proof-never-created", "source repository|compiled target"),
                ]:
                    with self.subTest(inputs=str(inputs), home=str(home)):
                        with self.assertRaisesRegex(ValueError, message):
                            custody.restore(self.data, self.modes, inputs, home)
            self.assertFalse((root / "inputs").exists())
            self.assertFalse((root / "home").exists())
            self.assertFalse((root / "target").exists())

    def test_link_or_junction_parent(self):
        with tempfile.TemporaryDirectory(prefix="maxim-input-link-") as directory:
            root = Path(directory).resolve()
            self.assertIn(Path(tempfile.gettempdir()).resolve(), root.parents)
            target = root / "target"
            target.mkdir()
            (target / "marker").write_bytes(b"preserve")
            link = root / "link"
            if os.name == "nt":
                subprocess.run([os.environ.get("COMSPEC", "cmd.exe"), "/c", "mklink", "/J", str(link), str(target)], check=True, capture_output=True)
            else:
                link.symlink_to(target, target_is_directory=True)
            try:
                with self.assertRaisesRegex(ValueError, "link/junction"):
                    custody.restore(self.data, self.modes, link / "inputs", root / "home")
                self.assertFalse((root / "home").exists())
                self.assertEqual((target / "marker").read_bytes(), b"preserve")
            finally:
                self.assertEqual(link.resolve(), target.resolve())
                link.rmdir() if os.name == "nt" else link.unlink()


if __name__ == "__main__":
    unittest.main()
