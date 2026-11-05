"""Check the exact Python generator environment before rendering the library."""
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform

ROOT = Path(__file__).resolve().parents[1]
PYTHON = "3.12.16"


def requirements(path):
    result = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith(("#", "-r ")):
            continue
        name, separator, version = line.partition("==")
        if not separator or not name or not version or " " in line:
            raise ValueError(f"Expected exact distribution pin in {path.name}")
        key = name.lower().replace("_", "-")
        if key in result:
            raise ValueError(f"Duplicate distribution pin: {name}")
        result[key] = version
    return result


def verify():
    lock = ROOT / "requirements-build.lock"
    expected = requirements(lock)
    direct = requirements(ROOT / "requirements.txt")
    for name, version in direct.items():
        if expected.get(name) != version:
            raise ValueError(f"Direct/locked dependency differs: {name}")
    failures = []
    if platform.python_version() != PYTHON:
        failures.append(f"Python {platform.python_version()} (expected {PYTHON})")
    observed = {}
    for name, version in expected.items():
        try:
            actual = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            actual = None
        observed[name] = actual
        if actual != version:
            failures.append(f"{name} {actual or 'missing'} (expected {version})")
    if failures:
        raise ValueError("Generator inputs differ: " + "; ".join(failures) + ". Use Python " + PYTHON + " and pip install -r requirements-build.lock")
    return dict(python=PYTHON, distributions=observed, lock_sha256=hashlib.sha256(lock.read_bytes()).hexdigest(), scope="Exact installed versions; upstream wheel/source hash custody is separate.")


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
