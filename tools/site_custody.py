"""Bind complete Pages files/downloads to their verified original source tree."""
import gzip
import io
import os
from pathlib import Path
import zipfile

from font_custody import verify_fonts
from source_custody import digest, encoded, strict_json, validate_paths, source_zip, verify_source

BUILD_MANIFEST = 'explore/BUILD-MANIFEST.json'
SITE_BUDGET = 1_000_000_000
INDEX_RAW_BUDGET = 256 * 1024 * 1024
RUNTIME_NOTICE = 'notices/rust-1.95.0-COPYRIGHT-library.html'
RUNTIME_NOTICE_SHA = '90567e2718bf7fd65a71a3a43c5596488e80e5f51ed02bfea6fec54458b5f3d1'
HELPERS = ['receive-source.py', 'source_custody.py', 'input_custody.py', 'python_custody.py', 'receive-site.py', 'site_custody.py', 'font_custody.py']
NOTICES = {
    'LICENSE.md': 'LICENSE.md',
    'RUST-DEPENDENCY-NOTICES.txt': 'cargo-inputs/DEPENDENCY-NOTICES.txt',
    'PYTHON-DEPENDENCY-NOTICES.txt': 'python-inputs/DEPENDENCY-NOTICES.txt',
    'FONT-NOTICES.txt': 'assets/fonts/FONT-NOTICES.txt',
    'RUST-RUNTIME-NOTICES.html': RUNTIME_NOTICE,
}


def ui(raw, manifest):
    values = {'__SOURCE_COMMIT__': manifest['source_commit'], '__SOURCE_SHORT__': manifest['source_commit'][:12],
              '__INDEX_SHA256__': manifest['index']['raw_sha256'], '__INDEX_SHORT__': manifest['index']['raw_sha256'][:12]}
    for token, value in values.items():raw = raw.replace(token.encode(), value.encode())
    return raw


def receiver_files(data, manifest):
    files = {name: data['tools/' + name] for name in HELPERS}
    raw = data['docs/receiver.txt']
    for token, value in {'__SOURCE_COMMIT__': manifest['source_commit'], '__SOURCE_SHA256__': manifest['source']['sha256'], '__SOURCE_NAME__': manifest['source']['path'].rsplit('/', 1)[1]}.items():
        raw = raw.replace(token.encode(), value.encode())
    files['README.txt'] = raw
    return files


def receiver_zip(files):
    result = io.BytesIO()
    with zipfile.ZipFile(result, 'w') as archive:
        for name, raw in sorted(files.items()):
            row = zipfile.ZipInfo(name, (2026, 11, 5, 0, 0, 0)); row.create_system = 3; row.external_attr = 0o100644 << 16; row.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(row, raw)
    return result.getvalue()


def descriptor(path, raw):return dict(path=path, bytes=len(raw), sha256=digest(raw))


def source_epoch(data):
    commit = bytes.fromhex(strict_json(data['SOURCE-MANIFEST.json'])['commit_object_hex'])
    rows = [row for row in commit.split(b'\n\n', 1)[0].splitlines() if row.startswith(b'committer ')]
    if len(rows) != 1:raise ValueError('Original source committer missing')
    epoch = int(rows[0].rsplit(b' ', 2)[1])
    if epoch < 0 or epoch >= 2**32:raise ValueError('Source epoch outside gzip range')
    return epoch


def index_digest(raw):
    with gzip.GzipFile(fileobj=io.BytesIO(raw)) as stream:value = stream.read(INDEX_RAW_BUDGET + 1)
    if len(value) > INDEX_RAW_BUDGET:raise ValueError('Expanded index resource budget exceeded')
    return digest(value)


def add_delivery(build, data, modes, head):
    source_manifest = strict_json(data['SOURCE-MANIFEST.json'])
    verify_fonts(data)
    if digest(data[RUNTIME_NOTICE]) != RUNTIME_NOTICE_SHA:
        raise ValueError('Original Rust library runtime notice differs')
    downloads = build / 'explore/downloads'; downloads.mkdir()
    source = source_zip(data, modes)
    source_name = 'explore/downloads/maxim-source-' + head + '.zip'
    (build / source_name).write_bytes(source)
    index_raw = (build / 'explore/index.json.gz').read_bytes()
    manifest = dict(schema='maxim.site.v1', source_commit=head, source_tree=source_manifest['source_tree'], source_date_epoch=source_epoch(data), source=descriptor(source_name, source),
                    index=dict(**descriptor('explore/index.json.gz', index_raw), raw_sha256=index_digest(index_raw), schema=1),
                    wasm=descriptor('explore/pkg/maxim_search_bg.wasm', (build / 'explore/pkg/maxim_search_bg.wasm').read_bytes()),
                    adapter=descriptor('explore/pkg/maxim_search.js', (build / 'explore/pkg/maxim_search.js').read_bytes()),
                    scope='Complete site/source/download integrity, not authorship or factual certification. Original split software/content and third-party terms apply. Installed interpreter/pip/toolchain/Node/browser prerequisites are not bundled.')
    for name in ['index.html', 'style.css', 'app.js', 'worker.js']:
        (build / 'explore' / name).write_bytes(ui(data['web/' + name], manifest))
    for name, original in NOTICES.items():(downloads / name).write_bytes(data[original])
    (downloads / 'SOURCE-MANIFEST.json').write_bytes(data['SOURCE-MANIFEST.json'])
    receiver = receiver_zip(receiver_files(data, manifest)); (downloads / 'receiver.zip').write_bytes(receiver)
    manifest['receiver'] = descriptor('explore/downloads/receiver.zip', receiver)
    rows = []
    for path in sorted(build.rglob('*')):
        if path.is_file():rows.append(descriptor(path.relative_to(build).as_posix(), path.read_bytes()))
    manifest['files'] = rows
    total = sum(row['bytes'] for row in rows)
    manifest['total_bytes'] = total
    for _ in range(8):
        final = total + len(encoded(manifest))
        if manifest['total_bytes'] == final:break
        manifest['total_bytes'] = final
    if manifest['total_bytes'] >= SITE_BUDGET:
        raise ValueError('Complete site and downloads exceed the existing 1 GB budget')
    (build / BUILD_MANIFEST).write_bytes(encoded(manifest))
    return manifest


def verify_site_data(files, expected_manifest_sha, expected_head):
    raw = files[BUILD_MANIFEST]
    if digest(raw) != expected_manifest_sha:
        raise ValueError('Build manifest SHA mismatch')
    manifest = strict_json(raw)
    if manifest['schema'] != 'maxim.site.v1' or manifest['source_commit'] != expected_head:
        raise ValueError('Site source identity mismatch')
    rows = manifest['files']; validate_paths([row['path'] for row in rows])
    if len(rows) > 50_000 or set(files) != {row['path'] for row in rows} | {BUILD_MANIFEST} or any(row['path'] == BUILD_MANIFEST for row in rows):
        raise ValueError('Complete site inventory mismatch')
    if sum(len(value) for value in files.values()) != manifest['total_bytes'] or manifest['total_bytes'] >= SITE_BUDGET:
        raise ValueError('Complete site budget/size differs')
    for row in rows:
        value = files[row['path']]
        if len(value) != row['bytes'] or digest(value) != row['sha256']:
            raise ValueError('Site file hash mismatch: ' + row['path'])
    for key, required in [('source', 'explore/downloads/maxim-source-' + expected_head + '.zip'), ('wasm', 'explore/pkg/maxim_search_bg.wasm'), ('adapter', 'explore/pkg/maxim_search.js'), ('index', 'explore/index.json.gz'), ('receiver', 'explore/downloads/receiver.zip')]:
        row = manifest[key]
        if row != descriptor(required, files[required]) | ({'raw_sha256': row['raw_sha256'], 'schema': row['schema']} if key == 'index' else {}):
            raise ValueError('Artifact descriptor differs: ' + key)
    if files[manifest['wasm']['path']][:8] != b'\0asm\x01\0\0\0':
        raise ValueError('WASM header mismatch')
    if manifest['index']['schema'] != 1 or index_digest(files[manifest['index']['path']]) != manifest['index']['raw_sha256']:
        raise ValueError('Complete index identity mismatch')
    source_manifest, data, modes = verify_source(files[manifest['source']['path']], expected_head)
    if source_manifest['source_tree'] != manifest['source_tree']:
        raise ValueError('Site and original source tree differ')
    if manifest['source_date_epoch'] != source_epoch(data):raise ValueError('Original source epoch differs')
    verify_fonts(data)
    if digest(data[RUNTIME_NOTICE]) != RUNTIME_NOTICE_SHA:
        raise ValueError('Original runtime notice hash mismatch')
    for name in ['index.html', 'style.css', 'app.js', 'worker.js']:
        if files['explore/' + name] != ui(data['web/' + name], manifest):
            raise ValueError('Site UI differs from original source')
    for name, original in NOTICES.items():
        if files['explore/downloads/' + name] != data[original]:
            raise ValueError('Original source/runtime notice differs')
    if files['explore/downloads/SOURCE-MANIFEST.json'] != data['SOURCE-MANIFEST.json']:
        raise ValueError('Download source manifest differs')
    for name in data:
        if name.startswith('assets/fonts/') and files.get(name) != data[name]:
            raise ValueError('Site font bytes/notices differ')
    with zipfile.ZipFile(io.BytesIO(files[manifest['receiver']['path']])) as archive:
        entries = archive.infolist(); validate_paths([row.orig_filename for row in entries])
        if len(entries) != len(HELPERS) + 1 or sum(row.file_size for row in entries) > 2 * 1024 * 1024 or any(row.orig_filename != row.filename or row.external_attr >> 16 != 0o100644 for row in entries):
            raise ValueError('Unsafe receiver bundle')
        if {row.filename: archive.read(row) for row in entries} != receiver_files(data, manifest):
            raise ValueError('Receiver helper differs from original source')
    return manifest, source_manifest, data, modes


def verify_site(root, expected_manifest_sha, expected_head):
    root = Path(root)
    for parent in [root, *root.parents]:
        if parent.is_symlink() or (parent.exists() and getattr(parent.lstat(), 'st_file_attributes', 0) & 0x400):
            raise ValueError('Site root uses a link/junction')
    root = root.resolve(); paths = []
    for path in root.rglob('*'):
        if path.is_symlink() or getattr(path.lstat(), 'st_file_attributes', 0) & 0x400:
            raise ValueError('Site contains a link/junction')
        if path.is_file():paths.append(path)
    if len(paths) > 50_000 or sum(path.stat().st_size for path in paths) >= SITE_BUDGET:
        raise ValueError('Site resource budget exceeded')
    files = {path.relative_to(root).as_posix(): path.read_bytes() for path in paths}
    return verify_site_data(files, expected_manifest_sha, expected_head)
