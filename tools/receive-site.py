"""Read-only verification of a complete downloaded MAXIM project-site folder."""
import argparse
import json
from pathlib import Path
from site_custody import verify_site

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, required=True, help='Project root containing explore/')
    parser.add_argument('--manifest-sha256', required=True, help='From a separately trusted build/release receipt')
    parser.add_argument('--commit', required=True)
    args = parser.parse_args()
    manifest, source, _, _ = verify_site(args.site, args.manifest_sha256, args.commit)
    print(json.dumps(dict(verified=True, source_commit=manifest['source_commit'], source_tree=manifest['source_tree'], files=len(manifest['files']), git_blobs=len(source['git_files']), total_bytes=manifest['total_bytes'])))
