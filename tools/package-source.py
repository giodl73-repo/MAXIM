"""Package the complete source tree and original locked Rust/Python inputs."""
import argparse
import json
from pathlib import Path
from source_custody import package_source

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--expected-source-head', required=True)
    args = parser.parse_args()
    print(json.dumps(package_source(Path(__file__).resolve().parents[1], args.output, args.expected_source_head)))
