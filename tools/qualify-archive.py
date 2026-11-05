"""Rebuild the complete verified Pages source outside Git with isolated inputs."""
import argparse
import datetime
import json
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import time
import urllib.request

from source_custody import new_destination, restore_source, digest
from site_custody import verify_site, BUILD_MANIFEST


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, required=True)
    parser.add_argument('--manifest-sha256', required=True)
    parser.add_argument('--expected-source-head', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--target-dir', type=Path, help='Explicit optional compiled-cache reuse; default is new/empty')
    args = parser.parse_args(); repo = Path(__file__).resolve().parents[1]
    output = new_destination(args.output, repo)
    original, _, data, modes = verify_site(args.site, args.manifest_sha256, args.expected_source_head)
    output.mkdir(parents=True); restored = output / 'source'; restore_source(data, modes, restored); del data, modes
    assert not (restored / '.git').exists()
    target = args.target_dir.resolve() if args.target_dir else output / 'target'
    if target == restored or target in restored.parents or restored in target.parents:raise ValueError('Compiled target overlaps restored source')
    if not args.target_dir and target.exists():raise ValueError('Use a new compiled target')
    env = {k:v for k,v in os.environ.items() if not k.startswith('PIP_') and k != 'PYTHONPATH'}
    env.update(PYTHONUTF8='1', PYTHONNOUSERSITE='1', PYTHONDONTWRITEBYTECODE='1', PIP_CONFIG_FILE=os.devnull, PIP_DISABLE_PIP_VERSION_CHECK='1', CARGO_TARGET_DIR=str(target), CARGO_INCREMENTAL='0', CARGO_NET_OFFLINE='true', RUSTUP_TOOLCHAIN='1.95.0')
    commands = []
    def run(name, command):
        command = [str(x) for x in command]; process = subprocess.run(command, cwd=restored, env=env, capture_output=True)
        (output / (name + '.stdout')).write_bytes(process.stdout); (output / (name + '.stderr')).write_bytes(process.stderr)
        commands.append(dict(name=name, command=command, exit_code=process.returncode)); (output / 'commands.json').write_text(json.dumps(commands, indent=2)+'\n', encoding='utf-8')
        print(json.dumps(dict(step=name, exit_code=process.returncode)), flush=True)
        if process.returncode:raise RuntimeError(name + ' failed; retained stdout/stderr at ' + str(output))
        return process
    bootstrap = Path(sys._base_executable); venv = output / 'python-env'; cache = output / 'python-inputs'; python = venv / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
    run('restore-python', [bootstrap, 'tools/python_custody.py', '--sha256', (restored / 'python-inputs/sha256.txt').read_text().split()[0], '--output', cache])
    run('new-venv', [bootstrap, '-m', 'venv', venv]); env['PATH'] = str(python.parent) + os.pathsep + env['PATH']
    run('offline-python-install', [python, '-m', 'pip', 'install', '--no-index', '--no-compile', '--find-links', cache / 'wheels', '--require-hashes', '--only-binary=:all:', '--no-deps', '-r', cache / 'requirements-hashes.txt'])
    run('pip-check', [python, '-m', 'pip', 'check']); run('generator-preflight', [python, 'tools/build_inputs.py'])
    pycheck = [python, 'tools/check_python_inputs.py', '--cache', cache, '--venv', venv]
    run('python-before', pycheck + ['--snapshot', output / 'installed-python.json'])
    inputs = output / 'rust-inputs'; home = output / 'cargo-home'
    run('restore-rust', [python, 'tools/input_custody.py', '--sha256', (restored / 'cargo-inputs/sha256.txt').read_text().split()[0], '--inputs', inputs, '--cargo-home', home]); env['CARGO_HOME'] = str(home)
    run('metadata', ['cargo', '+1.95.0', 'metadata', '--locked', '--offline', '--all-features', '--format-version', '1'])
    rustcheck = [python, 'tools/check_input_metadata.py', '--metadata', output / 'metadata.stdout', '--inputs', inputs, '--cargo-home', home]
    run('rust-before', rustcheck)
    for name, command in [('fmt', ['cargo', '+1.95.0', 'fmt', '--check']), ('native', ['cargo', '+1.95.0', 'test', '--locked', '--offline', '--all-targets']), ('clippy', ['cargo', '+1.95.0', 'clippy', '--locked', '--offline', '--all-targets', '--all-features', '--', '-D', 'warnings']), ('corpus', [python, 'tools/test_build_search.py']), ('control', ['cargo', '+1.95.0', 'build', '--locked', '--offline', '--example', 'search-control'])]:run(name, command)
    built = restored / 'site/MAXIM'; run('site', [python, 'tools/build-site.py', '--site', built, '--expected-source-head', args.expected_source_head])
    run('parity', [python, 'tools/check-search.py', '--site', built / 'explore', '--output', output / 'parity', '--expected-source-head', args.expected_source_head])
    rebuilt, _, _, _ = verify_site(built, digest((built / BUILD_MANIFEST).read_bytes()), args.expected_source_head)
    before = {row['path']:row for row in original['files']}; after = {row['path']:row for row in rebuilt['files']}
    differences = [dict(path=path, original=before.get(path), rebuilt=after.get(path)) for path in sorted(before.keys() | after.keys()) if before.get(path) != after.get(path)]
    comparison = dict(all_files_exact=not differences, original_manifest_sha256=args.manifest_sha256, rebuilt_manifest_sha256=digest((built / BUILD_MANIFEST).read_bytes()), differences=differences)
    (output / 'site-comparison.json').write_text(json.dumps(comparison, indent=2)+'\n', encoding='utf-8')
    if differences or comparison['original_manifest_sha256'] != comparison['rebuilt_manifest_sha256']:raise ValueError('Complete archive rebuild differs; retained comparison identifies every file')
    # Node/Playwright and browser are installed test prerequisites, not app inputs.
    package = json.loads((repo / 'node_modules/@playwright/test/package.json').read_bytes()); lock = json.loads((restored / 'package-lock.json').read_bytes())
    if package['version'] != lock['packages']['node_modules/@playwright/test']['version']:raise ValueError('Installed browser-test prerequisite differs from source lock')
    shutil.copytree(repo / 'node_modules', restored / 'node_modules')
    with socket.socket() as probe:probe.bind(('127.0.0.1', 0)); port = probe.getsockname()[1]
    with (output / 'server.stdout').open('wb') as stdout, (output / 'server.stderr').open('wb') as stderr:
        server = subprocess.Popen([str(python), '-m', 'http.server', str(port), '--bind', '127.0.0.1', '--directory', str(built.parent)], cwd=restored, env=env, stdout=stdout, stderr=stderr)
        try:
            for _ in range(100):
                if server.poll() is not None:raise RuntimeError('Owned HTTP server stopped')
                try:
                    with urllib.request.urlopen(f'http://127.0.0.1:{port}/MAXIM/explore/', timeout=1) as response:assert response.status == 200
                    break
                except OSError:time.sleep(.1)
            else:raise RuntimeError('Owned HTTP server not ready')
            config = output / 'playwright.config.mjs'
            config.write_text('import {defineConfig} from '+json.dumps((restored / 'node_modules/@playwright/test/index.mjs').as_uri())+';\nexport default defineConfig('+json.dumps(dict(testDir=str(restored / 'tests/browser'), timeout=120000, workers=2, retries=0, outputDir=str(output / 'browser-results'), reporter=[['json', dict(outputFile=str(output / 'browser-report.json'))]], use=dict(baseURL=f'http://127.0.0.1:{port}', browserName='chromium', trace='retain-on-failure', screenshot='only-on-failure')))+');\n', encoding='utf-8')
            run('browser', ['node', restored / 'node_modules/@playwright/test/cli.js', 'test', '--config', config])
        finally:server.terminate(); server.wait(timeout=15)
    run('rust-after', rustcheck); run('python-after', pycheck + ['--compare', output / 'installed-python.json'])
    assert (output / 'rust-before.stdout').read_bytes() == (output / 'rust-after.stdout').read_bytes()
    assert not (restored / '.git').exists()
    parity = json.loads((output / 'parity/results/receipt.json').read_bytes()); browser = json.loads((output / 'browser-report.json').read_bytes())
    assert parity['all_exact'] and parity['controls'] == 134 and parity['constructor_controls'] == 7 and parity['boundary_controls'] == 10
    assert browser['stats']['expected'] == 16 and all(browser['stats'][key] == 0 for key in ['unexpected', 'skipped', 'flaky'])
    receipt = dict(source_commit=args.expected_source_head, checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(), comparison=comparison, parity=parity, browser_stats=browser['stats'], commands=commands, compiled_target=str(target), compiled_cache_reused=bool(args.target_dir), rust_input_before_after_exact=True, python_after=json.loads((output / 'python-after.stdout').read_bytes()), node_prerequisite_version=package['version'], scope='Complete original source restored outside Git; original Rust/Python inputs and a new Python venv/Cargo home restored offline. Full native/site/WASM/index and every published file/manifest match; archived-source browser suite passes. Installed interpreter/pip/toolchain/bindgen/Node/browser prerequisites reused explicitly; Node test package copied from locked installed prerequisite. No default/live or factual certification.')
    (output / 'receipt.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8'); print(json.dumps(dict(qualified=True, source_commit=args.expected_source_head, browser_cases=16, complete_site_byte_exact=True)))


if __name__ == '__main__':main()
