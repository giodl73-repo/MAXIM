"""Receiver corruption controls. Fixture WASM/index are not engine evidence."""
import copy
import gzip
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import site_custody as site
import source_custody as source
from font_custody import verify_fonts


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='maxim-site-custody-'); cls.root = Path(cls.temp.name).resolve()
        assert Path(tempfile.gettempdir()).resolve() in cls.root.parents
        repo = Path(__file__).resolve().parents[1]
        names = ['Cargo.lock', 'requirements-build.lock', 'LICENSE.md', 'docs/receiver.txt', site.RUNTIME_NOTICE]
        names += ['tools/' + name for name in site.HELPERS] + ['web/' + name for name in ['index.html', 'app.js', 'worker.js', 'style.css']]
        for folder in ['cargo-inputs', 'python-inputs', 'font-inputs', 'assets/fonts']:
            names += [p.relative_to(repo).as_posix() for p in (repo / folder).rglob('*') if p.is_file()]
        data = {name: (repo / name).read_bytes() for name in sorted(set(names))}
        rows = [dict(path=name, mode='100644', git_blob=source.git_id('blob', raw), bytes=len(raw), sha256=source.digest(raw)) for name, raw in sorted(data.items())]
        tree = source.git_tree(rows); commit = b'tree ' + tree.encode() + b'\nauthor Test <test@example.invalid> 0 +0000\ncommitter Test <test@example.invalid> 0 +0000\n\nReceiver fixture\n'
        cls.head = source.git_id('commit', commit)
        data[source.SOURCE_MANIFEST] = source.encoded(dict(schema='maxim.source.v1', source_commit=cls.head, source_tree=tree, commit_object_hex=commit.hex(), git_files=rows))
        modes = {name: 0o100644 for name in data}; source.verify_source_data(data, modes, cls.head); verify_fonts(data)
        cls.build = cls.root / 'site'; (cls.build / 'explore/pkg').mkdir(parents=True)
        # Deliberately small custody fixtures. The browser suite runs real WASM.
        (cls.build / 'explore/pkg/maxim_search_bg.wasm').write_bytes(b'\0asm\x01\0\0\0')
        (cls.build / 'explore/pkg/maxim_search.js').write_bytes(b'// custody fixture\n')
        (cls.build / 'explore/index.json.gz').write_bytes(gzip.compress(b'{"version":1,"entries":[],"terms":{}}', mtime=0))
        (cls.build / 'index.html').write_bytes(b'<p>library fixture</p>')
        for name, raw in data.items():
            if name.startswith('assets/fonts/'):
                path = cls.build / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(raw)
        cls.manifest = site.add_delivery(cls.build, data, modes, cls.head)
        cls.files = {p.relative_to(cls.build).as_posix(): p.read_bytes() for p in cls.build.rglob('*') if p.is_file()}
        cls.manifest_sha = source.digest(cls.files[site.BUILD_MANIFEST]); cls.source_data = data

    @classmethod
    def tearDownClass(cls):cls.temp.cleanup()

    def changed(self, name, raw, descriptor_key=None):
        files = dict(self.files); files[name] = raw; manifest = copy.deepcopy(self.manifest)
        for row in manifest['files']:
            if row['path'] == name:row.update(bytes=len(raw), sha256=source.digest(raw))
        if descriptor_key:manifest[descriptor_key] = site.descriptor(name, raw)
        total = sum(len(v) for k,v in files.items() if k != site.BUILD_MANIFEST)
        for _ in range(8):
            final = total + len(source.encoded(manifest))
            if manifest['total_bytes'] == final:break
            manifest['total_bytes'] = final
        files[site.BUILD_MANIFEST] = source.encoded(manifest)
        return files, source.digest(files[site.BUILD_MANIFEST])

    def test_full_fixture_and_read_only_filesystem_receiver(self):
        manifest, _, _, _ = site.verify_site(self.build, self.manifest_sha, self.head)
        self.assertEqual(manifest['source_commit'], self.head)
        self.assertEqual(len(manifest['files']) + 1, len(self.files))

    def test_wrong_external_manifest_and_source_commit(self):
        with self.assertRaisesRegex(ValueError, 'manifest SHA'):site.verify_site_data(self.files, '0'*64, self.head)
        with self.assertRaisesRegex(ValueError, 'source identity'):site.verify_site_data(self.files, self.manifest_sha, '0'*40)

    def test_missing_and_extra_site_files(self):
        files = dict(self.files); files.pop('index.html')
        with self.assertRaisesRegex(ValueError, 'inventory'):site.verify_site_data(files,self.manifest_sha,self.head)
        files = dict(self.files, extra=b'unknown')
        with self.assertRaisesRegex(ValueError, 'inventory'):site.verify_site_data(files,self.manifest_sha,self.head)

    def test_changed_payload_without_rebound_inventory(self):
        files = dict(self.files); files['index.html'] = b'x'*len(files['index.html'])
        with self.assertRaisesRegex(ValueError, 'file hash'):site.verify_site_data(files,self.manifest_sha,self.head)

    def test_rebound_invalid_wasm_header(self):
        files, sha = self.changed('explore/pkg/maxim_search_bg.wasm',b'bad wasm','wasm')
        with self.assertRaisesRegex(ValueError, 'WASM header'):site.verify_site_data(files,sha,self.head)

    def test_expanded_index_hash_and_resource_budget(self):
        files = dict(self.files); manifest = copy.deepcopy(self.manifest); manifest['index']['raw_sha256'] = '0'*64
        files[site.BUILD_MANIFEST] = source.encoded(manifest)
        with self.assertRaisesRegex(ValueError,'index identity'):site.verify_site_data(files,source.digest(files[site.BUILD_MANIFEST]),self.head)
        with patch.object(site,'INDEX_RAW_BUDGET',2),self.assertRaisesRegex(ValueError,'resource budget'):site.index_digest(gzip.compress(b'too long'))

    def test_rebound_changed_ui_is_not_original_source(self):
        files, sha = self.changed('explore/app.js',b'// replacement\n')
        with self.assertRaisesRegex(ValueError,'UI differs'):site.verify_site_data(files,sha,self.head)

    def test_rebound_pruned_notices_are_rejected(self):
        for name in ['LICENSE.md','RUST-DEPENDENCY-NOTICES.txt','PYTHON-DEPENDENCY-NOTICES.txt','RUST-RUNTIME-NOTICES.html','FONT-NOTICES.txt']:
            with self.subTest(name=name):
                files, sha = self.changed('explore/downloads/'+name,b'pruned')
                with self.assertRaisesRegex(ValueError,'notice differs'):site.verify_site_data(files,sha,self.head)

    def test_rebound_font_asset_is_not_original_source(self):
        name = next(p for p in self.files if p.endswith('.woff2'))
        files, sha = self.changed(name,b'wOF2changed')
        with self.assertRaisesRegex(ValueError,'font bytes'):site.verify_site_data(files,sha,self.head)

    def test_rebound_source_archive_still_requires_original_git_objects(self):
        name = self.manifest['source']['path']; data,modes = source.read_zip(self.files[name]); data['LICENSE.md'] = b'changed'
        files, sha = self.changed(name,source.source_zip(data,modes),'source')
        with self.assertRaisesRegex(ValueError,'source blob/mode'):site.verify_site_data(files,sha,self.head)

    def test_rebound_source_manifest_download_is_rejected(self):
        files, sha = self.changed('explore/downloads/SOURCE-MANIFEST.json',b'{}')
        with self.assertRaisesRegex(ValueError,'source manifest differs'):site.verify_site_data(files,sha,self.head)

    def test_rebound_receiver_helper_is_not_original_source(self):
        with zipfile.ZipFile(io.BytesIO(self.files['explore/downloads/receiver.zip'])) as archive:data={name:archive.read(name) for name in archive.namelist()}
        data['receive-source.py'] = b'print("replacement")\n'
        files, sha = self.changed('explore/downloads/receiver.zip',site.receiver_zip(data),'receiver')
        with self.assertRaisesRegex(ValueError,'Receiver helper'):site.verify_site_data(files,sha,self.head)

    def test_site_root_junction_or_symlink_is_rejected(self):
        link=self.root/'link'
        if os.name=='nt':subprocess.run([os.environ.get('COMSPEC','cmd.exe'),'/c','mklink','/J',str(link),str(self.build)],check=True,capture_output=True)
        else:link.symlink_to(self.build,target_is_directory=True)
        try:
            with self.assertRaisesRegex(ValueError,'link/junction'):site.verify_site(link,self.manifest_sha,self.head)
        finally:
            self.assertEqual(link.resolve(),self.build.resolve());link.rmdir() if os.name=='nt' else link.unlink()


class FontTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root=Path(__file__).resolve().parents[1]
        cls.data={p.relative_to(root).as_posix():p.read_bytes() for folder in ['font-inputs','assets/fonts'] for p in (root/folder).rglob('*') if p.is_file()}

    def test_original_fonts_and_css(self):self.assertEqual(len(verify_fonts(self.data)['webfonts']),30)

    def test_changed_original_font_notice_and_css(self):
        for name in ['assets/fonts/FONT-NOTICES.txt','assets/fonts/fonts.css',next(p for p in self.data if p.endswith('.woff2'))]:
            with self.subTest(name=name):
                data=dict(self.data);data[name]=b'changed'
                with self.assertRaises(ValueError):verify_fonts(data)

    def test_missing_original_font_and_unknown_runtime_file(self):
        data=dict(self.data);data.pop(next(p for p in data if p.endswith('.woff2')))
        with self.assertRaisesRegex(ValueError,'inventory'):verify_fonts(data)
        data=dict(self.data);data['assets/fonts/unknown']=b'unknown'
        with self.assertRaisesRegex(ValueError,'inventory'):verify_fonts(data)


if __name__=='__main__':unittest.main()
