"""Verify actual MkDocs routes without moving authored files or numbered URLs."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

from mkdocs.config import load_config
from mkdocs.structure.files import File, Files, get_files

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('maxim_portable_routes',ROOT/'.mkdocs/portable_routes.py');routes=importlib.util.module_from_spec(spec);spec.loader.exec_module(routes)


class RouteTests(unittest.TestCase):
    def test_auxiliary_documents_use_flat_urls(self):
        files=Files([File(name,str(ROOT),str(ROOT/'site-unused'),True) for name in ['PUZZLE-HUNT.md','puzzle-hunt/01-GUIDE.md','context/waves/2026-11-05-search-self-service/VALIDATION.md','context/waves/2026-11-05-search-self-service/validation/receipt.json']])
        # Prime cached properties, as real MkDocs file collection may do.
        for file in files:_=file.dest_uri,file.url,file.abs_dest_path
        routes.on_files(files,None)
        self.assertEqual(files.get_file_from_path('PUZZLE-HUNT.md').url,'PUZZLE-HUNT.html')
        self.assertEqual(files.get_file_from_path('context/waves/2026-11-05-search-self-service/VALIDATION.md').dest_uri,'context/waves/2026-11-05-search-self-service/VALIDATION.html')
        self.assertEqual(files.get_file_from_path('puzzle-hunt/01-GUIDE.md').url,'puzzle-hunt/01-GUIDE/')

    def test_numbered_guide_urls_are_unchanged(self):
        files=Files([File('languages/01-RUST.md',str(ROOT),str(ROOT/'site-unused'),True)])
        original=files[0].dest_uri,files[0].url
        routes.on_files(files,None);self.assertEqual((files[0].dest_uri,files[0].url),original)

    def test_unexpected_collisions_still_fail(self):
        files=Files([File(name,str(ROOT),str(ROOT/'site-unused'),True) for name in ['OTHER.md','other/01-GUIDE.md']])
        with self.assertRaisesRegex(ValueError,'Case-colliding'):routes.on_files(files,None)

    def test_complete_current_file_map_is_portable(self):
        with tempfile.TemporaryDirectory(prefix='maxim-routes-') as directory:
            root=Path(directory).resolve();self.assertIn(Path(tempfile.gettempdir()).resolve(),root.parents)
            config=load_config(config_file=str(ROOT/'.mkdocs/mkdocs.yml'),site_dir=str(root/'not-built'))
            files=get_files(config);routes.on_files(files,config)
            self.assertGreater(len(files),4000)


if __name__=='__main__':unittest.main()
