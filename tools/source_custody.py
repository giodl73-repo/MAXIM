"""Complete Git object custody; verification/restoration never executes source."""
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import zipfile

import input_custody as rust_inputs
import python_custody as python_inputs

digest = rust_inputs.digest
safe_path = rust_inputs.safe_path
strict_json = rust_inputs.strict_json
SOURCE_MANIFEST = 'SOURCE-MANIFEST.json'
MAX_FILES = 50_000
MAX_RAW_BYTES = 768 * 1024 * 1024
MAX_ZIP_BYTES = 512 * 1024 * 1024


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode('utf-8')


def git_id(kind, raw):
    return hashlib.sha1(kind.encode() + b' ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def validate_paths(names):
    folded, components = set(), {}
    for name in names:
        safe_path(name)
        if name.casefold() in folded:
            raise ValueError('Duplicate or case-colliding source paths')
        folded.add(name.casefold())
        parts = PurePosixPath(name).parts
        for count in range(1, len(parts) + 1):
            prefix = '/'.join(parts[:count])
            if components.setdefault(prefix.casefold(), prefix) != prefix:
                raise ValueError('Case-colliding source directory components')
    if any(str(p).casefold() in folded for name in names for p in PurePosixPath(name).parents if str(p) != '.'):
        raise ValueError('Source file/directory collision')


def git_tree(rows):
    validate_paths([row['path'] for row in rows])
    tree = {}
    for row in rows:
        if row['mode'] not in ('100644', '100755') or not re.fullmatch('[a-f0-9]{40}', row['git_blob']):
            raise ValueError('Unsupported source mode/blob')
        parent = tree
        parts = PurePosixPath(row['path']).parts
        for part in parts[:-1]:
            parent = parent.setdefault(part, {})
        parent[parts[-1]] = (row['mode'], row['git_blob'])

    def tree_hash(node):
        content = bytearray()
        for name, value in sorted(node.items(), key=lambda item: item[0].encode() + (b'' if isinstance(item[1], tuple) else b'/')):
            mode, blob = value if isinstance(value, tuple) else ('40000', tree_hash(value))
            content.extend(mode.encode() + b' ' + name.encode() + b'\0' + bytes.fromhex(blob))
        return git_id('tree', content)
    return tree_hash(tree)


def read_zip(raw):
    if len(raw) > MAX_ZIP_BYTES:
        raise ValueError('Source ZIP resource limit')
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        rows = archive.infolist()
        if len(rows) > MAX_FILES or sum(row.file_size for row in rows) > MAX_RAW_BYTES:
            raise ValueError('Source member resource limit')
        for row in rows:
            safe_path(row.orig_filename)
            if row.orig_filename != row.filename or row.external_attr >> 16 not in (0o100644, 0o100755):
                raise ValueError('Unsafe source ZIP wire name/mode')
        validate_paths([row.filename for row in rows])
        return {row.filename: archive.read(row) for row in rows}, {row.filename: row.external_attr >> 16 for row in rows}


def verify_tree(data, modes, expected_head):
    manifest = strict_json(data[SOURCE_MANIFEST])
    if manifest['schema'] != 'maxim.source.v1' or manifest['source_commit'] != expected_head or not re.fullmatch('[a-f0-9]{40}', expected_head):
        raise ValueError('Source commit mismatch')
    commit = bytes.fromhex(manifest['commit_object_hex'])
    if git_id('commit', commit) != expected_head:
        raise ValueError('Original source commit object mismatch')
    rows = manifest['git_files']
    if len(rows) >= MAX_FILES or sum(row['bytes'] for row in rows) > MAX_RAW_BYTES:
        raise ValueError('Source manifest resource limit')
    if modes[SOURCE_MANIFEST] != 0o100644 or set(data) != {row['path'] for row in rows} | {SOURCE_MANIFEST} or any(row['path'] == SOURCE_MANIFEST for row in rows):
        raise ValueError('Complete source inventory mismatch')
    tree = git_tree(rows)
    if manifest['source_tree'] != tree or commit.split(b'\n', 1)[0] != b'tree ' + tree.encode():
        raise ValueError('Complete original source tree mismatch')
    for row in rows:
        value = data[row['path']]
        if len(value) != row['bytes'] or digest(value) != row['sha256'] or git_id('blob', value) != row['git_blob'] or modes[row['path']] != int(row['mode'], 8):
            raise ValueError('Original source blob/mode mismatch: ' + row['path'])
    return manifest


def verify_source_data(data, modes, expected_head):
    manifest = verify_tree(data, modes, expected_head)
    rust, rust_data, _ = rust_inputs.verify(data['cargo-inputs/inputs.zip'], data['cargo-inputs/sha256.txt'].decode().split()[0], data['Cargo.lock'])
    if strict_json(data['cargo-inputs/manifest.json']) != rust or data['cargo-inputs/DEPENDENCY-NOTICES.txt'] != rust_data['DEPENDENCY-NOTICES.txt']:
        raise ValueError('Original Rust manifest/notices differ')
    python, python_data = python_inputs.verify(data['python-inputs/inputs.zip'], data['python-inputs/sha256.txt'].decode().split()[0], data['python-inputs/releases.json'], data['requirements-build.lock'])
    if strict_json(data['python-inputs/manifest.json']) != python or data['python-inputs/DEPENDENCY-NOTICES.txt'] != python_data['DEPENDENCY-NOTICES.txt']:
        raise ValueError('Original Python manifest/notices differ')
    return manifest


def verify_source(raw, expected_head):
    data, modes = read_zip(raw)
    return verify_source_data(data, modes, expected_head), data, modes


def check_source_files(repo, names):
    expected = set(names) | {SOURCE_MANIFEST}
    generated = {'.git', 'site', 'target', 'node_modules', 'test-results'}
    for base, directories, files in os.walk(repo, followlinks=False):
        parent = Path(base)
        directories[:] = [name for name in directories if name != '__pycache__' and not (parent == repo and name in generated)]
        for name in [*directories, *files]:
            path = parent / name
            if path.is_symlink() or getattr(path.lstat(), 'st_file_attributes', 0) & 0x400:
                raise ValueError('Source contains a link/junction')
        for name in files:
            path = parent / name
            if not (parent == repo and name == '.git') and path.relative_to(repo).as_posix() not in expected:
                raise ValueError('Unexpected source/config file: ' + str(path))


def git_source(repo, head):
    if subprocess.check_output(['git', 'status', '--porcelain'], cwd=repo):
        raise ValueError('Commit source changes before exporting')
    if subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip() != head:
        raise ValueError('Expected source head differs from checkout')
    rows = []
    for item in subprocess.check_output(['git', 'ls-tree', '-rz', head], cwd=repo).split(b'\0'):
        if not item:
            continue
        header, path = item.split(b'\t', 1)
        mode, kind, blob = header.decode().split()
        if kind != 'blob':
            raise ValueError('Unbundled Gitlink or unsupported source object')
        rows.append(dict(path=path.decode('utf-8'), mode=mode, git_blob=blob))
    if len(rows) >= MAX_FILES:
        raise ValueError('Source file count exceeds budget')
    validate_paths([row['path'] for row in rows])
    check_source_files(repo, [row['path'] for row in rows])
    # Raw objects bypass checkout/export filters; one batch avoids 20k processes.
    transport = io.BytesIO(subprocess.check_output(['git', 'cat-file', '--batch'], cwd=repo, input=''.join(row['git_blob'] + '\n' for row in rows).encode()))
    data = {}
    for row in rows:
        blob, kind, size = transport.readline().decode().split()
        value = transport.read(int(size))
        if blob != row['git_blob'] or kind != 'blob' or len(value) != int(size) or transport.read(1) != b'\n':
            raise ValueError('Git object transport mismatch')
        physical = (repo / row['path']).read_bytes()
        if physical != value and physical.replace(b'\r\n', b'\n') != value:
            raise ValueError('Checkout content differs from original Git bytes: ' + row['path'])
        if os.name != 'nt' and (repo / row['path']).stat().st_mode & 0o777 != int(row['mode'], 8) & 0o777:
            raise ValueError('Checkout source mode mismatch')
        row.update(bytes=len(value), sha256=digest(value)); data[row['path']] = value
    if transport.read():
        raise ValueError('Unexpected Git object transport output')
    commit = subprocess.check_output(['git', 'cat-file', 'commit', head], cwd=repo)
    manifest = dict(schema='maxim.source.v1', source_commit=head, source_tree=git_tree(rows), commit_object_hex=commit.hex(), git_files=rows,
                    scope='Complete original Git tree including both locked dependency capsules and notices. Original software/content/third-party grants apply. Installed interpreter/pip/toolchains/Node/browser are prerequisites, not bundled. Integrity is not authorship or factual certification.')
    data[SOURCE_MANIFEST] = encoded(manifest)
    modes = {row['path']: int(row['mode'], 8) for row in rows}; modes[SOURCE_MANIFEST] = 0o100644
    verify_source_data(data, modes, head)
    return data, modes


def source_data(repo, head):
    if (repo / '.git').exists():
        return git_source(repo, head)
    manifest_raw = (repo / SOURCE_MANIFEST).read_bytes()
    manifest = strict_json(manifest_raw); rows = manifest['git_files']
    if len(rows) >= MAX_FILES or sum(row['bytes'] for row in rows) > MAX_RAW_BYTES:
        raise ValueError('Source manifest resource limit')
    validate_paths([row['path'] for row in rows]); check_source_files(repo, [row['path'] for row in rows])
    if any((repo / row['path']).stat().st_size != row['bytes'] for row in rows):
        raise ValueError('Restored source file size mismatch')
    data = {row['path']: (repo / row['path']).read_bytes() for row in rows}; data[SOURCE_MANIFEST] = manifest_raw
    modes = {row['path']: int(row['mode'], 8) for row in rows}; modes[SOURCE_MANIFEST] = 0o100644
    if os.name != 'nt' and any((repo / row['path']).stat().st_mode & 0o777 != int(row['mode'], 8) & 0o777 for row in rows):
        raise ValueError('Restored source mode mismatch')
    verify_source_data(data, modes, head)
    return data, modes


def source_zip(data, modes):
    result = io.BytesIO()
    with zipfile.ZipFile(result, 'w') as archive:
        for name, value in sorted(data.items()):
            item = zipfile.ZipInfo(name, (2026, 11, 5, 0, 0, 0)); item.create_system = 3
            item.compress_type = zipfile.ZIP_STORED if name.endswith(('.zip', '.gz', '.png', '.woff2')) else zipfile.ZIP_DEFLATED
            item.external_attr = modes[name] << 16; archive.writestr(item, value)
    return result.getvalue()


def new_destination(path, repo=None):
    output = rust_inputs.destination(path)
    if repo is None:
        candidate = Path(__file__).resolve().parents[1]
        repo = candidate if (candidate / 'Cargo.toml').is_file() else None
    repo = repo.resolve() if repo else None
    if repo and (output == repo or repo in output.parents or output in repo.parents):
        raise ValueError('Destination overlaps source repository')
    targets = [repo / 'target'] if repo else []
    if os.environ.get('CARGO_TARGET_DIR'):
        targets.append(Path(os.environ['CARGO_TARGET_DIR']).resolve())
    if any(output == target or output in target.parents or target in output.parents for target in targets):
        raise ValueError('Destination overlaps compiled target')
    return output


def restore_source(data, modes, output):
    output = new_destination(output)
    validate_paths(list(data))
    output.mkdir(parents=True)
    for name, value in data.items():
        path = output / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(value); path.chmod(modes[name] & 0o777)
    return output


def package_source(repo, output, head):
    output = new_destination(output, repo)
    data, modes = source_data(repo, head)
    raw = source_zip(data, modes)
    manifest, _, _ = verify_source(raw, head)
    output.parent.mkdir(parents=True, exist_ok=True); output.write_bytes(raw)
    return dict(source_commit=head, source_tree=manifest['source_tree'], git_blobs=len(manifest['git_files']), bytes=len(raw), sha256=digest(raw))
