"""Flat routes for two auxiliary documents with case-colliding directory URLs."""
import os
from pathlib import Path, PurePosixPath
import sys
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from source_custody import validate_paths

FLAT_DOCUMENTS = {'PUZZLE-HUNT.md', 'context/waves/2026-11-05-search-self-service/VALIDATION.md'}


def on_files(files, config):
    for file in files:
        if file.src_uri in FLAT_DOCUMENTS:
            file.use_directory_urls = False
            file.dest_uri = str(PurePosixPath(file.src_uri).with_suffix('.html'))
            file.url = quote(file.dest_uri, safe='/')
            file.abs_dest_path = os.path.join(file.dest_dir, *PurePosixPath(file.dest_uri).parts)
    validate_paths([file.dest_uri for file in files if file.inclusion.is_included()])
    return files
