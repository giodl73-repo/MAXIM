"""Stable Rust diagnostic paths without changing first-party Rust or search policy."""
import os
from pathlib import Path
import tomllib

from input_custody import safe_path


def expected_policy(lock, inherited=()):
    packages = tomllib.loads(lock.decode())['package']
    return dict(source='/maxim-source', dependencies=sorted(p['name']+'-'+p['version'] for p in packages if p.get('source')), inherited_flags=list(inherited))


def reproducible_flags(root, metadata, environment):
    encoded = environment.get('CARGO_ENCODED_RUSTFLAGS')
    inherited = (encoded.split('\x1f') if encoded else []) if encoded is not None else environment.get('RUSTFLAGS', '').split()
    flags = list(inherited)
    flags.append('--remap-path-prefix=' + str(Path(root).resolve()) + '=/maxim-source')
    names = set()
    for package in sorted((p for p in metadata['packages'] if p.get('source')), key=lambda p: (p['name'], p['version'])):
        name = package['name'] + '-' + package['version']; safe_path(name)
        if name in names:raise ValueError('Dependency virtual source path collision')
        names.add(name)
        path = Path(package['manifest_path']).resolve().parent
        flags.append('--remap-path-prefix=' + str(path) + '=/maxim-inputs/' + name)
    return flags, dict(source='/maxim-source', dependencies=sorted(names), inherited_flags=inherited)


def configure(root, metadata):
    flags, policy = reproducible_flags(root, metadata, os.environ)
    os.environ['CARGO_ENCODED_RUSTFLAGS'] = '\x1f'.join(flags)
    os.environ.pop('RUSTFLAGS', None)
    return policy
