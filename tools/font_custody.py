"""Verify original font bytes/notices and the same-origin stylesheet derivation."""
import re
from input_custody import digest, strict_json, safe_path

FAMILIES = {'dmsans', 'librecaslondisplay', 'ebgaramond', 'jetbrainsmono'}
OVERRIDES = b'\n:root { --md-text-font: "EB Garamond"; --md-code-font: "JetBrains Mono"; }\n'


def stylesheet(originals, fonts):
    css = b'\n'.join(originals)
    for row in fonts:
        css = css.replace(row['url'].encode(), row['path'].rsplit('/', 1)[1].encode())
    if re.search(rb'url\([\s\'"]*https?://', css):
        raise ValueError('External font URL remains in runtime CSS')
    return css + OVERRIDES


def verify_fonts(data):
    manifest = strict_json(data['font-inputs/manifest.json'])
    if manifest['schema'] != 'maxim.fonts.v1' or {row['family'] for row in manifest['families']} != FAMILIES:
        raise ValueError('Font family closure differs')
    rows = manifest['files']
    if len({row['path'] for row in rows}) != len(rows):
        raise ValueError('Duplicate font files')
    expected = {row['path'] for row in rows} | {'font-inputs/manifest.json', 'assets/fonts/fonts.css'}
    actual = {path for path in data if path.startswith(('font-inputs/', 'assets/fonts/'))}
    if actual != expected:
        raise ValueError('Complete font inventory differs')
    for row in rows:
        safe_path(row['path'])
        raw = data[row['path']]
        if digest(raw) != row['sha256'] or len(raw) != row['bytes']:
            raise ValueError('Original font bytes differ')
    original_css = [data[row['path']] for row in manifest['css']]
    urls = {url.decode() for raw in original_css for url in re.findall(rb'url\((https://fonts\.gstatic\.com/[^)]+)\)', raw)}
    fonts = manifest['webfonts']
    if len(fonts) != 30 or len({row['url'] for row in fonts}) != 30 or {row['url'] for row in fonts} != urls:
        raise ValueError('Original CSS/font URL closure differs')
    for row in fonts:
        if not row['path'].startswith('assets/fonts/') or data[row['path']][:4] != b'wOF2':
            raise ValueError('Original WOFF2 font missing')
    notices = []
    for family in manifest['families']:
        raw = data[family['license']]
        if b'SIL OPEN FONT LICENSE Version 1.1' not in raw or data[family['runtime_license']] != raw:
            raise ValueError('Original font copyright/license differs')
        notices.append(b'\n\n===== ' + family['family'].encode() + b' =====\n' + raw)
    if data['assets/fonts/FONT-NOTICES.txt'] != b''.join(notices):
        raise ValueError('Complete font notices differ')
    if data['assets/fonts/fonts.css'] != stylesheet(original_css, fonts):
        raise ValueError('Runtime stylesheet differs from original font CSS')
    return manifest
