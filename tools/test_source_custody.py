"""Adversarial source/tree tests; actual full input closure is qualified separately."""
import copy
import io
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import source_custody as custody


class SourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # A real Git tree/commit, including an executable, CRLF bytes and a dotfile.
        cls.temporary = tempfile.TemporaryDirectory(prefix='maxim-source-tree-')
        cls.root = Path(cls.temporary.name).resolve()
        assert Path(tempfile.gettempdir()).resolve() in cls.root.parents
        cls.repo = cls.root / 'repo'; cls.repo.mkdir()
        for name, raw in {'a.txt': b'original\r\n', 'dir/source.py': b'print("hello")\n', '.hidden': b'keep\n', 'run.sh': b'#!/bin/sh\ntrue\n', '\u00e9.txt': b'unicode path\n'}.items():
            path = cls.repo / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(raw)
        def git(*args):return subprocess.check_output(['git', *args], cwd=cls.repo)
        git('init', '-q'); git('config', 'core.autocrlf', 'false'); git('add', '.'); git('update-index', '--chmod=+x', 'run.sh')
        git('-c', 'user.name=MAXIM source test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'fixture')
        cls.head = git('rev-parse', 'HEAD').decode().strip(); commit = git('cat-file', 'commit', cls.head)
        cls.data, cls.modes, rows = {}, {}, []
        for item in git('ls-tree', '-rz', cls.head).split(b'\0'):
            if not item:continue
            header, path = item.split(b'\t', 1); mode, kind, blob = header.decode().split(); name = path.decode(); raw = git('cat-file', 'blob', blob)
            cls.data[name] = raw; cls.modes[name] = int(mode, 8); rows.append(dict(path=name, mode=mode, git_blob=blob, bytes=len(raw), sha256=custody.digest(raw)))
        cls.manifest = dict(schema='maxim.source.v1',source_commit=cls.head,source_tree=git('rev-parse', 'HEAD^{tree}').decode().strip(),commit_object_hex=commit.hex(),git_files=rows)
        cls.data[custody.SOURCE_MANIFEST] = custody.encoded(cls.manifest); cls.modes[custody.SOURCE_MANIFEST] = 0o100644

    @classmethod
    def tearDownClass(cls):cls.temporary.cleanup()

    def variant(self, change):
        data = dict(self.data); manifest = copy.deepcopy(self.manifest); change(data, manifest); data[custody.SOURCE_MANIFEST] = custody.encoded(manifest)
        return data

    def test_original_tree_and_zip_roundtrip(self):
        self.assertEqual(self.data['a.txt'], b'original\r\n')
        self.assertEqual(custody.verify_tree(self.data, self.modes, self.head), self.manifest)
        raw = custody.source_zip(self.data, self.modes); data, modes = custody.read_zip(raw)
        self.assertEqual(data, self.data); self.assertEqual(modes, self.modes)
        self.assertEqual(custody.source_zip(data, modes), raw)

    def test_wrong_commit_and_commit_object(self):
        with self.assertRaisesRegex(ValueError, 'commit mismatch'):custody.verify_tree(self.data, self.modes, '0' * 40)
        data = self.variant(lambda d,m: m.update(commit_object_hex=(bytes.fromhex(m['commit_object_hex'])+b'changed').hex()))
        with self.assertRaisesRegex(ValueError, 'commit object'):custody.verify_tree(data, self.modes, self.head)

    def test_changed_blob_even_with_rebound_sha_and_length(self):
        def change(data, manifest):
            row = next(r for r in manifest['git_files'] if r['path']=='a.txt'); data['a.txt'] = b'changed'; row.update(bytes=7,sha256=custody.digest(data['a.txt']))
        with self.assertRaisesRegex(ValueError, 'blob/mode'):custody.verify_tree(self.variant(change), self.modes, self.head)

    def test_rebound_blob_and_tree_cannot_change_original_commit(self):
        def change(data, manifest):
            row = manifest['git_files'][0]; data[row['path']] = b'changed'; row.update(bytes=7,sha256=custody.digest(b'changed'),git_blob=custody.git_id('blob',b'changed')); manifest['source_tree'] = custody.git_tree(manifest['git_files'])
        with self.assertRaisesRegex(ValueError, 'original source tree'):custody.verify_tree(self.variant(change),self.modes,self.head)

    def test_omitted_file_and_unknown_file(self):
        def remove(data, manifest):
            row = manifest['git_files'].pop(); data.pop(row['path'])
        with self.assertRaisesRegex(ValueError, 'original source tree'):custody.verify_tree(self.variant(remove),self.modes,self.head)
        data = dict(self.data, extra=b'unknown')
        with self.assertRaisesRegex(ValueError, 'inventory'):custody.verify_tree(data,self.modes,self.head)

    def test_mode_tamper_and_unsupported_gitlink(self):
        modes = dict(self.modes); modes['run.sh'] = 0o100644
        with self.assertRaisesRegex(ValueError, 'blob/mode'):custody.verify_tree(self.data,modes,self.head)
        rows = copy.deepcopy(self.manifest['git_files']); rows[0]['mode'] = '160000'
        with self.assertRaisesRegex(ValueError, 'Unsupported source mode'):custody.git_tree(rows)

    def test_paths_cases_ancestors_and_reserved_names(self):
        for names in [['x','x'],['x','X'],['a','a/x'],['A/x','a/y'],['../x'],['x\\y'],['NUL.txt'],['a/../x'],['x.'],['a//x']]:
            with self.subTest(names=names),self.assertRaises(ValueError):custody.validate_paths(names)

    def test_original_wire_backslash_and_nul(self):
        for replacement in [b'a\\b',b'a\0b']:
            raw = io.BytesIO()
            with zipfile.ZipFile(raw,'w') as archive:
                row=zipfile.ZipInfo('a/b');row.external_attr=0o100644<<16;archive.writestr(row,b'content')
            # Raw headers, not ZipInfo creation, preserve the actual unsafe name.
            mutated=raw.getvalue().replace(b'a/b',replacement)
            with self.subTest(replacement=replacement),self.assertRaises(ValueError):custody.read_zip(mutated)

    def test_zip_case_collision_symlink_and_resource_limit(self):
        for entries in [[('x',0o100644),('X',0o100644)],[('link',0o120777)]]:
            raw=io.BytesIO()
            with zipfile.ZipFile(raw,'w') as archive:
                for name,mode in entries:
                    row=zipfile.ZipInfo(name);row.external_attr=mode<<16;archive.writestr(row,b'value')
            with self.assertRaises(ValueError):custody.read_zip(raw.getvalue())
        with patch.object(custody,'MAX_FILES',1),self.assertRaisesRegex(ValueError,'resource limit'):custody.read_zip(custody.source_zip(self.data,self.modes))

    def test_existing_source_and_explicit_target_are_preserved(self):
        existing=self.root/'keep';existing.mkdir();(existing/'marker').write_bytes(b'keep')
        with self.assertRaisesRegex(ValueError,'new destination'):custody.new_destination(existing)
        with self.assertRaisesRegex(ValueError,'source repository'):custody.new_destination(self.repo/'new',self.repo)
        with patch.dict(os.environ,{'CARGO_TARGET_DIR':str(self.root/'compiled')}):
            with self.assertRaisesRegex(ValueError,'compiled target'):custody.new_destination(self.root/'compiled/new',self.repo)
        self.assertFalse((self.repo/'new').exists());self.assertFalse((self.root/'compiled').exists());self.assertEqual((existing/'marker').read_bytes(),b'keep')

    def test_actual_junction_or_symlink_is_rejected_before_writes(self):
        target=self.root/'link-target';target.mkdir();link=self.root/'junction'
        if os.name=='nt':subprocess.run([os.environ.get('COMSPEC','cmd.exe'),'/c','mklink','/J',str(link),str(target)],check=True,capture_output=True)
        else:link.symlink_to(target,target_is_directory=True)
        try:
            with self.assertRaisesRegex(ValueError,'link/junction'):custody.new_destination(link/'new',self.repo)
            self.assertFalse((target/'new').exists())
        finally:
            self.assertEqual(link.resolve(),target.resolve());link.rmdir() if os.name=='nt' else link.unlink()

    def test_complete_restore_and_unlisted_file_detection(self):
        restored=custody.restore_source(self.data,self.modes,self.root/'restored')
        custody.check_source_files(restored,[r['path'] for r in self.manifest['git_files']])
        for name,value in self.data.items():self.assertEqual((restored/name).read_bytes(),value)
        if os.name!='nt':self.assertEqual((restored/'run.sh').stat().st_mode&0o777,0o755)
        (restored/'unexpected.cfg').write_bytes(b'extra')
        with self.assertRaisesRegex(ValueError,'Unexpected source/config'):custody.check_source_files(restored,[r['path'] for r in self.manifest['git_files']])

    def test_duplicate_json_keys(self):
        data=dict(self.data);data[custody.SOURCE_MANIFEST]=b'{"schema":"maxim.source.v1","schema":"other"}'
        with self.assertRaisesRegex(ValueError,'Duplicate JSON'):custody.verify_tree(data,self.modes,self.head)


class CompleteInputTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root=Path(__file__).resolve().parents[1]
        names=['Cargo.lock','requirements-build.lock','cargo-inputs/inputs.zip','cargo-inputs/manifest.json','cargo-inputs/sha256.txt','cargo-inputs/DEPENDENCY-NOTICES.txt','python-inputs/inputs.zip','python-inputs/manifest.json','python-inputs/sha256.txt','python-inputs/releases.json','python-inputs/DEPENDENCY-NOTICES.txt']
        cls.original={name:(root/name).read_bytes() for name in names}

    def committed(self, change=None):
        data=dict(self.original)
        if change:change(data)
        rows=[dict(path=name,mode='100644',git_blob=custody.git_id('blob',raw),bytes=len(raw),sha256=custody.digest(raw)) for name,raw in sorted(data.items())]
        tree=custody.git_tree(rows)
        commit=b'tree '+tree.encode()+b'\nauthor MAXIM test <test@example.invalid> 0 +0000\ncommitter MAXIM test <test@example.invalid> 0 +0000\n\nOriginal input integration fixture\n'
        head=custody.git_id('commit',commit)
        manifest=dict(schema='maxim.source.v1',source_commit=head,source_tree=tree,commit_object_hex=commit.hex(),git_files=rows)
        data[custody.SOURCE_MANIFEST]=custody.encoded(manifest)
        return head,data,{name:0o100644 for name in data}

    def test_actual_complete_rust_and_python_capsules(self):
        head,data,modes=self.committed()
        self.assertEqual(custody.verify_source_data(data,modes,head)['source_commit'],head)

    def test_original_rust_notices_required_despite_valid_rebound_commit(self):
        head,data,modes=self.committed(lambda d:d.update({'cargo-inputs/DEPENDENCY-NOTICES.txt':b'pruned notices'}))
        custody.verify_tree(data,modes,head)
        with self.assertRaisesRegex(ValueError,'Rust manifest/notices'):custody.verify_source_data(data,modes,head)

    def test_original_python_notices_required_despite_valid_rebound_commit(self):
        head,data,modes=self.committed(lambda d:d.update({'python-inputs/DEPENDENCY-NOTICES.txt':b'pruned notices'}))
        custody.verify_tree(data,modes,head)
        with self.assertRaisesRegex(ValueError,'Python manifest/notices'):custody.verify_source_data(data,modes,head)


if __name__=='__main__':unittest.main()
