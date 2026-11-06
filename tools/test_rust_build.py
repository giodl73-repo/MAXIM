"""Path-flag tests include execution by the pinned compiler, not a text-only model."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

from rust_build import reproducible_flags


class RustBuildTests(unittest.TestCase):
    def test_inherited_flags_and_owned_dependency_roots(self):
        root=Path(tempfile.gettempdir())/'maxim root'
        metadata=dict(packages=[dict(name='example',version='1.0.0',source='registry',manifest_path=str(root.parent/'vendor/example/Cargo.toml')),dict(name='maxim-search',version='0.1.0',source=None)])
        flags,policy=reproducible_flags(root,metadata,{'CARGO_ENCODED_RUSTFLAGS':'-C\x1fdebuginfo=0','RUSTFLAGS':'ignored'})
        self.assertEqual(flags[:2],['-C','debuginfo=0']);self.assertTrue(flags[2].endswith('=/maxim-source'));self.assertTrue(flags[3].endswith('=/maxim-inputs/example-1.0.0'));self.assertEqual(policy['dependencies'],['example-1.0.0'])

    def test_duplicate_virtual_dependency_names_reject(self):
        row=dict(name='example',version='1.0.0',source='registry',manifest_path='/tmp/example/Cargo.toml')
        with self.assertRaisesRegex(ValueError,'collision'):reproducible_flags(Path(tempfile.gettempdir()),dict(packages=[row,row]),{})

    def test_empty_encoded_flags_override_other_flags(self):
        flags,policy=reproducible_flags(Path(tempfile.gettempdir()),dict(packages=[]),{'CARGO_ENCODED_RUSTFLAGS':'','RUSTFLAGS':'-C opt-level=1'})
        self.assertEqual(len(flags),1);self.assertEqual(policy['inherited_flags'],[])

    def test_pinned_compiler_actually_remaps_file_macro(self):
        with tempfile.TemporaryDirectory(prefix='maxim rust path ') as directory:
            root=Path(directory).resolve();self.assertIn(Path(tempfile.gettempdir()).resolve(),root.parents)
            path=root/'probe.rs';path.write_bytes(b'fn main(){println!("{}",file!());}\n');binary=root/('probe.exe' if os.name=='nt' else 'probe')
            flags,_=reproducible_flags(root,dict(packages=[]),{})
            subprocess.run(['rustc','+1.95.0',str(path),'--crate-name','maxim_path_probe','-o',str(binary),*flags],check=True,capture_output=True)
            result=subprocess.check_output([str(binary)]).decode().strip();self.assertTrue(result.startswith('/maxim-source'));self.assertNotIn(str(root),result)


if __name__=='__main__':unittest.main()
