# Pinned Python generator artifacts

This input capsule preserves 29 original source distributions and 33 unique
wheels selected for CPython 3.12 on Windows/Linux x64. Shared platform-neutral
wheels are stored once. All 62 original archives, 39,635 member records and 119
notice/attribution files are retained; every wheel RECORD was checked. Upstream
source releases accompany the original binaries; their wheel builds were not
reproduced here. Original third-party terms remain unchanged. MAXIM's own license
does not replace them. Interpreter/pip/compiler/browser prerequisites are separate.

The separately tracked `releases.json` fixes all selected release identities and
the unchanged `requirements-build.lock` identity. A trusted capsule SHA and this
catalog are required before restoring an offline cache. No source distribution
is automatically unpacked or executed. The bootstrap verifier uses Python 3.11+;
generator installation/execution requires Python 3.12.16.

```sh
python tools/python_custody.py --sha256 <trusted-capsule-sha> --output <new-external-cache>
python -m venv <new-venv>
# Use <new-venv>/bin/python below, or <new-venv>/Scripts/python.exe on Windows.
<venv-python> -m pip install --no-index --no-compile --find-links <cache>/wheels --require-hashes --only-binary=:all: --no-deps -r <cache>/requirements-hashes.txt
<venv-python> -m pip check
<venv-python> tools/build_inputs.py
```

Use a new isolated venv without system/user packages. Select the SHA from the
trusted checkout's sha256.txt or a separately verified release receipt. The cache
must be new, external to the source/compiled target, and free of links/junctions.
The capsule is committed for durable source-input custody; it stays out of the
runtime MkDocs tree. The complete-source download will include these exact bytes.
Portable receiver/negative controls, both-host offline install and full outside-
Git archive qualification remain required before release.

CI sets `PYTHONDONTWRITEBYTECODE=1` and `PYTHONNOUSERSITE=1`, clears
`PYTHONPATH`, and uses `tools/check_python_inputs.py` to snapshot the whole
installed environment before the build and compare it afterwards. It also
checks every restored archive, notice file and generated hash requirement.
Interpreter, pip, Rust, Node and browser installation remain prerequisites.
