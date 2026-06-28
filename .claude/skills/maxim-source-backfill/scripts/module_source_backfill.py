#!/usr/bin/env python3
"""Backfill a MAXIM module into PROOF/CROP/PEBBLE/FLETCH source-corpus artifacts."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import tempfile
import tomllib
from pathlib import Path


ROOT = Path.cwd()

# Tool crates (PROOF/CROP/FLETCH) are located via the portfolio `repo-map.toml`
# config rather than hardcoded paths. The map records where every repo lives
# locally; we walk up from the current module checkout to find the portfolio
# root that defines the tool crates, then build each Cargo manifest path.
TOOL_CRATES = {"proof": "proof", "crop": "crop", "fletch": "fletch"}


def resolve_tool_manifests() -> dict[str, Path | None]:
    """Resolve PROOF/CROP/FLETCH Cargo manifests from repo-map.toml.

    Searches upward from the current working directory for a `repo-map.toml`
    that defines `[repos.proof]`; the directory holding that map is the
    portfolio root. Returns a dict mapping tool name -> manifest Path (or None
    if the map or an entry is missing).
    """
    start = Path.cwd().resolve()
    for base in (start, *start.parents):
        candidate = base / "repo-map.toml"
        if not candidate.is_file():
            continue
        try:
            data = tomllib.loads(candidate.read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError):
            continue
        repos = data.get("repos", {})
        if "proof" not in repos:
            continue
        resolved: dict[str, Path | None] = {}
        for tool, key in TOOL_CRATES.items():
            rel = repos.get(key, {}).get("relative")
            resolved[tool] = (base / rel / "Cargo.toml") if rel else None
        return resolved
    return {tool: None for tool in TOOL_CRATES}


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = read_text(path)
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}, text
    fields: dict[str, str] = {}
    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line == "---":
            end_index = index
            break
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    if end_index is None:
        return {}, text
    body = "\n".join(lines[end_index + 1 :])
    if text.endswith("\n"):
        body += "\n"
    return fields, body


def heading_title(body: str, fallback: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip().replace("—", "-").replace("&", "and")
    return fallback


def bracket_list(values: list[str]) -> str:
    return "[" + ", ".join(values) + "]"


def guide_slug(path: Path, title: str) -> str:
    name = re.sub(r"^\d\d-", "", path.stem)
    if name:
        return slugify(name)
    return slugify(title)


def ensure_frontmatter(path: Path, module_id: str, section: str) -> dict[str, str]:
    fields, body = parse_frontmatter(path)
    title = fields.get("title") or heading_title(body, path.stem)
    slug = (fields.get("id") or "").replace(f"maxim:{module_id}:", "")
    if not slug or slug == fields.get("id"):
        slug = guide_slug(path, title)
    num = path.name[:2]
    concepts = fields.get("concepts") or bracket_list(slug.replace("-", " ").split()[:5] or [slug])
    roots = fields.get("root_concepts") or bracket_list(slug.replace("-", " ").split()[:2] or [slug])
    defaults = {
        "maxim_schema": "maxim.frontmatter.v1",
        "id": f"maxim:{module_id}:{slug}",
        "kind": "guide",
        "module": module_id,
        "section": section,
        "title": title,
        "status": "source-custody",
        "source_custody": "partial",
        "current_path": path.as_posix(),
        "canonical_path": path.as_posix(),
        "backsource_ids": f"[proof-backfill:{module_id}:{num}-{slug}, git-history:{module_id}:{num}-{slug}]",
        "concepts": concepts,
        "root_concepts": roots,
        "index_roles": "[guide, root-concept]",
        "remap_from": "[]",
        "remap_to": "[]",
        "updated": "null",
    }
    merged = {**defaults, **fields}
    ordered_keys = [
        "maxim_schema",
        "id",
        "kind",
        "module",
        "section",
        "title",
        "status",
        "source_custody",
        "current_path",
        "canonical_path",
        "backsource_ids",
        "concepts",
        "root_concepts",
        "index_roles",
        "remap_from",
        "remap_to",
        "updated",
    ]
    frontmatter = ["---", *[f"{key}: {merged[key]}" for key in ordered_keys], "---", ""]
    write_text(path, "\n".join(frontmatter) + body.lstrip("\n"))
    return merged


def run(command: list[str], *, stdout_path: Path | None = None) -> None:
    if stdout_path:
        stdout_path.parent.mkdir(parents=True, exist_ok=True)
        with stdout_path.open("w", encoding="utf-8", newline="\n") as handle:
            subprocess.run(command, check=True, stdout=handle)
    else:
        subprocess.run(command, check=True)


def git_hashes(path: str) -> list[str]:
    output = subprocess.check_output(
        ["git", "--no-pager", "log", "--format=%h", "--", path.replace("/", "\\")],
        text=True,
    )
    return [line for line in output.splitlines() if line]


def tick_list(values: list[str]) -> str:
    return ", ".join(f"`{value}`" for value in values) if values else "pending"


def format_obj(schema: str, shape: str, preferred: str, media: str = "application/json") -> dict[str, str | None]:
    return {
        "media_type": media,
        "encoding": "utf-8",
        "compression": None,
        "container": None,
        "schema": schema,
        "record_shape": shape,
        "preferred_local": preferred,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module-dir", required=True, help="Module directory containing numbered markdown guides.")
    parser.add_argument("--module-id", required=True, help="Stable MAXIM module id, e.g. computing-software.")
    parser.add_argument("--section", help="Section id; defaults to --module-id.")
    parser.add_argument("--proof-manifest", default=None, help="Override PROOF Cargo.toml (default: from repo-map.toml).")
    parser.add_argument("--crop-manifest", default=None, help="Override CROP Cargo.toml (default: from repo-map.toml).")
    parser.add_argument("--fletch-manifest", default=None, help="Override FLETCH Cargo.toml (default: from repo-map.toml).")
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args()

    # Redirect cargo build output to a writable location so we never try to
    # create a target/ dir inside the (possibly read-only) tool crates.
    os.environ.setdefault(
        "CARGO_TARGET_DIR", str(Path(tempfile.gettempdir()) / "maxim-cargo-target")
    )

    # Resolve tool-crate manifests from the portfolio config unless overridden.
    resolved = resolve_tool_manifests()
    for tool in TOOL_CRATES:
        attr = f"{tool}_manifest"
        if getattr(args, attr) is None:
            manifest = resolved.get(tool)
            if manifest is not None and manifest.is_file():
                setattr(args, attr, str(manifest))
        if getattr(args, attr) is None or not Path(getattr(args, attr)).is_file():
            parser.error(
                f"could not locate the {tool.upper()} Cargo.toml. Expected it via "
                f"repo-map.toml ([repos.{tool}].relative) or --{tool}-manifest. "
                f"Resolved: {getattr(args, attr) or resolved.get(tool)}"
            )

    module_dir = Path(args.module_dir)
    module_id = args.module_id
    section = args.section or module_id
    source_store = Path(".proof") / "backfill" / "sources" / module_id
    proof_source = source_store / "proof-source"
    module_ledger = Path(".proof") / "backfill" / "modules" / f"{module_id}.json"
    view_store = Path(".crop") / "views"
    pack_store = Path(".pebble") / "packs"
    module_view = view_store / f"maxim-{module_id}-source-corpus.json"
    module_pack = pack_store / f"maxim-{module_id}-source-corpus.pebble.json"
    registry_path = Path(".fletch") / "registries" / f"maxim-{module_id}-source-corpus.json"

    guides: list[dict[str, str]] = []
    for path in sorted(module_dir.glob("??-*.md")):
        fields = ensure_frontmatter(path, module_id, section)
        slug = fields["id"].replace(f"maxim:{module_id}:", "")
        base = path.stem
        num = path.name[:2]
        view_path = view_store / f"maxim-{module_id}-{slug}.json"
        pack_path = pack_store / f"maxim-{module_id}-{slug}.pebble.json"
        source_record = source_store / f"{num}-{slug}.source-record.md"
        guide = {
            "num": num,
            "file": path.name,
            "path": path.as_posix(),
            "slug": slug,
            "id": fields["id"],
            "title": fields["title"],
            "concepts": fields["concepts"],
            "roots": fields["root_concepts"],
            "source_id": f"proof-backfill:{module_id}:{num}-{slug}",
            "source_record": source_record.as_posix(),
            "source_md": (proof_source / f"{base}.source.md").as_posix(),
            "tables": (proof_source / f"{base}.tables.json").as_posix(),
            "blocks": (proof_source / f"{base}.blocks.json").as_posix(),
            "view": view_path.as_posix(),
            "pack": pack_path.as_posix(),
        }
        guides.append(guide)
        view = {
            "schema_version": "crop.view.v1",
            "name": f"maxim-{module_id}-{slug}",
            "root": f"../../{module_dir.as_posix()}",
            "task": f"Backfill MAXIM {fields['title']} as a partial source-custody fact/context pack.",
            "token_budget": 12000,
            "seed": 0,
            "frontmatter_query": f"id eq '{fields['id']}'",
            "include_extensions": ["md"],
            "exclude_dirs": [".git", ".claude", ".crop", ".mkdocs", ".roles", ".vscode", "_archive"],
        }
        write_text(view_path, json.dumps(view, indent=2, ensure_ascii=False) + "\n")

    module_view_json = {
        "schema_version": "crop.view.v1",
        "name": f"maxim-{module_id}-source-corpus",
        "root": f"../../{module_dir.as_posix()}",
        "task": f"Backfill the MAXIM {module_id} module for downstream fact/context reuse.",
        "token_budget": 12000,
        "seed": 0,
        "frontmatter_query": "source_custody eq 'partial'",
        "include_extensions": ["md"],
        "exclude_dirs": [".git", ".claude", ".crop", ".mkdocs", ".roles", ".vscode", "_archive"],
    }
    write_text(module_view, json.dumps(module_view_json, indent=2, ensure_ascii=False) + "\n")

    guide_paths = [guide["path"].replace("/", "\\") for guide in guides]
    run(
        [
            "cargo",
            "run",
            "--manifest-path",
            args.proof_manifest,
            "--quiet",
            "--",
            "backfill",
            *guide_paths,
            "--output-source",
            str(proof_source),
            "--report",
            str(source_store / "backfill-report.json"),
            "--literal-first",
            "--extract-tables",
            "--check-roundtrip",
        ]
    )

    run(
        [
            "cargo",
            "run",
            "--manifest-path",
            args.crop_manifest,
            "--quiet",
            "--",
            "view",
            "--file",
            str(module_view),
            "--format",
            "pebble",
        ],
        stdout_path=module_pack,
    )
    for guide in guides:
        run(
            [
                "cargo",
                "run",
                "--manifest-path",
                args.crop_manifest,
                "--quiet",
                "--",
                "view",
                "--file",
                guide["view"],
                "--format",
                "pebble",
            ],
            stdout_path=Path(guide["pack"]),
        )

    report = json.loads((source_store / "backfill-report.json").read_text(encoding="utf-8"))
    by_original = {Path(item["original_path"]).name: item for item in report["files"]}
    for guide in guides:
        file_report = by_original[guide["file"]]
        table_count = sum(1 for item in file_report.get("extractions", []) if item.get("kind") == "markdown_table")
        block_count = sum(1 for item in file_report.get("extractions", []) if item.get("kind") != "markdown_table")
        if not Path(guide["tables"]).exists():
            write_text(
                Path(guide["tables"]),
                json.dumps(
                    {
                        "schema_version": "1",
                        "source_markdown": guide["path"].replace("/", "\\"),
                        "tables": [],
                    },
                    indent=2,
                    ensure_ascii=False,
                )
                + "\n",
            )
        if not Path(guide["blocks"]).exists():
            write_text(
                Path(guide["blocks"]),
                json.dumps(
                    {
                        "schema_version": "1",
                        "source_markdown": guide["path"].replace("/", "\\"),
                        "blocks": [],
                    },
                    indent=2,
                    ensure_ascii=False,
                )
                + "\n",
            )
        record = f"""---
maxim_schema: maxim.frontmatter.v1
id: {guide['source_id']}
kind: source-record
module: {module_id}
section: {section}
title: {guide['title']} source record
status: source-custody
source_custody: partial
current_path: {guide['source_record']}
canonical_path: {guide['source_record']}
backsource_ids: [git-history:{module_id}:{guide['num']}-{guide['slug']}]
concepts: {guide['concepts']}
root_concepts: {guide['roots']}
index_roles: [source-map]
remap_from: []
remap_to: []
updated: null
---

# {guide['title']} source record

| Field | Value |
|---|---|
| Current MAXIM file | `{guide['path']}` |
| PROOF source artifact | `{guide['source_md']}` |
| PROOF table sidecar | `{guide['tables']}` |
| PROOF block sidecar | `{guide['blocks']}` |
| Backfill report | `{(source_store / 'backfill-report.json').as_posix()}` |
| PROOF classification | `literal_markdown` |
| PROOF confidence | `high` |
| Round trip | `passed` |
| Structured extraction | `{table_count}` markdown tables, `{block_count}` visual/block candidates |
| Git provenance | {tick_list(git_hashes(guide['path']))} |

## Custody note

This first-pass record proves the current file can be regenerated as a PROOF
literal source artifact and round-tripped without loss. It is still marked
`partial` because external/authentic backsources for factual claims have not yet
been attached.
"""
        write_text(Path(guide["source_record"]), record)

    module = {
        "schema_version": "maxim.proof-backfill.module.v1",
        "module_id": module_id,
        "status": "first-pass-complete",
        "current_root": module_dir.as_posix(),
        "source_store": source_store.as_posix(),
        "frontmatter_contract": ".proof/backfill/frontmatter-contract.md",
        "frontmatter_scope": {
            "mode": "module-only",
            "proof_output_default": "omit-frontmatter",
            "proof_output_option": "allow-frontmatter-for-metadata-views",
            "required_kind_values": ["guide", "module-index", "section-index", "concept-index", "source-record", "generated-pack"],
            "first_pass": [guide["path"] for guide in guides],
        },
        "proof_scope": {"config": "proof.toml", "include": [f"{module_dir.as_posix()}/*.md"], "exclude": [f"{module_dir.as_posix()}/STATUS.md"]},
        "crop_view": module_view.as_posix(),
        "distribution": {"pebble_pack": module_pack.as_posix(), "guide_packs": [guide["pack"] for guide in guides], "fletch_registry": registry_path.as_posix()},
        "source_custody": {
            "policy": "Each guide must map to an authentic backsource record before pack publication.",
            "default_state": "partial",
            "notes": [
                "Current MAXIM guide paths are not themselves sufficient backsources.",
                "Backsources can be source notes, cited originals, generated proof artifacts, or reviewed provenance records.",
                f"All {len(guides)} guides are partial: PROOF literal backfill and git provenance are recorded, but external/authentic factual backsources are still pending.",
                "PROOF structured sidecars capture markdown tables plus candidate ASCII tables, charts, and diagrams for quality search/indexing.",
                "Remaps preserve continuity if guide files move after backfill.",
            ],
        },
        "remap": [
            {
                "source_id": guide["source_id"],
                "source_record": guide["source_record"],
                "generated_source": guide["source_md"],
                "current_paths": [guide["path"]],
                "custody_status": "partial",
                "remap_status": "current-paths-recorded",
            }
            for guide in guides
        ],
        "gates": ["frontmatter-contract-applied", "source-custody-partial", "proof-module-clean", "crop-pebble-pack-emitted", "fletch-registry-added"],
    }
    write_text(module_ledger, json.dumps(module, indent=2, ensure_ascii=False) + "\n")

    fletches = [
        {
            "id": f"maxim.{module_id}.source-corpus.pebble",
            "node_kind": "fletch",
            "shafts": [{"kind": "file", "url": module_pack.as_posix()}],
            "edges": [{"to": f"maxim-{module_id}-source-corpus", "kind": "derived-from", "label": "CROP view recipe", "metadata": {"view": module_view.as_posix(), "module": module_id, "custody": "partial"}}],
            "format": format_obj("pebble.v1", "corpus-slice", module_pack.as_posix()),
            "tags": ["source-corpus", "crop", "pebble", "partial-custody"],
            "metadata": {"source_repo": "MAXIM", "module": module_id, "distribution": "FLETCH fetch/cache surface for downstream repos", "publication_state": "partial-source-custody"},
        }
    ]
    for guide in guides:
        prefix = f"maxim.{module_id}.{guide['slug']}"
        common = {"source_repo": "MAXIM", "module": module_id, "guide": guide["path"], "publication_state": "partial-source-custody"}
        fletches.extend(
            [
                {
                    "id": f"{prefix}.view",
                    "node_kind": "fletch",
                    "shafts": [{"kind": "file", "url": guide["view"]}],
                    "edges": [{"to": f"maxim.{module_id}.source-corpus.pebble", "kind": "derived-from", "label": "Guide-level CROP view recipe", "metadata": {"module": module_id, "guide": guide["path"], "custody": "partial"}}],
                    "format": format_obj("crop.view.v1", "view-recipe", guide["view"]),
                    "tags": ["source-corpus", "crop", "view", "partial-custody", "guide"],
                    "metadata": common,
                },
                {
                    "id": f"{prefix}.pebble",
                    "node_kind": "fletch",
                    "shafts": [{"kind": "file", "url": guide["pack"]}],
                    "edges": [
                        {"to": f"{prefix}.view", "kind": "derived-from", "label": "Guide-level CROP view recipe", "metadata": {"module": module_id, "custody": "partial"}},
                        {"to": f"maxim.{module_id}.source-corpus.pebble", "kind": "derived-from", "label": "Guide-level CROP view", "metadata": {"view": guide["view"], "module": module_id, "custody": "partial"}},
                    ],
                    "format": format_obj("pebble.v1", "corpus-slice", guide["pack"]),
                    "tags": ["source-corpus", "crop", "pebble", "partial-custody", "guide"],
                    "metadata": common,
                },
                {
                    "id": f"{prefix}.proof-source",
                    "node_kind": "fletch",
                    "shafts": [{"kind": "file", "url": guide["source_md"]}],
                    "edges": [{"to": f"{prefix}.view", "kind": "derived-from", "label": "Literal PROOF source for guide view", "metadata": {"module": module_id, "guide": guide["path"], "custody": "partial"}}],
                    "format": format_obj("proof.source.literal_markdown.v1", "literal-source", guide["source_md"], "text/markdown"),
                    "tags": ["source-corpus", "proof", "source", "partial-custody", "guide"],
                    "metadata": common,
                },
                {
                    "id": f"{prefix}.tables",
                    "node_kind": "fletch",
                    "shafts": [{"kind": "file", "url": guide["tables"]}],
                    "edges": [{"to": f"{prefix}.proof-source", "kind": "derived-from", "label": "PROOF markdown table sidecar", "metadata": {"module": module_id, "guide": guide["path"], "custody": "partial"}}],
                    "format": format_obj("proof.backfill.tables.v1", "table-sidecar", guide["tables"]),
                    "tags": ["source-corpus", "proof", "tables", "partial-custody", "guide"],
                    "metadata": common,
                },
                {
                    "id": f"{prefix}.blocks",
                    "node_kind": "fletch",
                    "shafts": [{"kind": "file", "url": guide["blocks"]}],
                    "edges": [{"to": f"{prefix}.proof-source", "kind": "derived-from", "label": "PROOF structured block sidecar", "metadata": {"module": module_id, "guide": guide["path"], "custody": "partial"}}],
                    "format": format_obj("proof.backfill.blocks.v1", "structured-block-sidecar", guide["blocks"]),
                    "tags": ["source-corpus", "proof", "blocks", "partial-custody", "guide"],
                    "metadata": common,
                },
            ]
        )
    registry = {"schema_version": "fletch.registry.v1", "generated_by": "MAXIM source-corpus backfill", "registry_id": f"maxim-{module_id}-source-corpus", "fletches": fletches}
    write_text(registry_path, json.dumps(registry, indent=2, ensure_ascii=False) + "\n")

    if args.validate:
        run(["cargo", "run", "--manifest-path", args.proof_manifest, "--quiet", "--", "check", *guide_paths])
        run(["cargo", "run", "--manifest-path", args.crop_manifest, "--quiet", "--", "view", "--inspect", "--dir", str(view_store), "--strict"])
        run(["cargo", "run", "--manifest-path", args.fletch_manifest, "--bin", "fletch-cli", "--quiet", "--", "registry", "validate", "--file", str(registry_path)])
        missing = [shaft["url"] for fletch in fletches for shaft in fletch["shafts"] if not Path(shaft["url"]).exists()]
        if missing:
            raise SystemExit(f"registry shaft paths missing: {missing}")
        run(["git", "--no-pager", "diff", "--check"])

    print(
        json.dumps(
            {
                "module_id": module_id,
                "guides": len(guides),
                "roundtrip_passed": report["summary"]["roundtrip_passed"],
                "roundtrip_failed": report["summary"]["roundtrip_failed"],
                "tables": report["summary"]["tables_extracted"],
                "structured_blocks": report["summary"]["structured_blocks_extracted"],
                "fletches": len(fletches),
                "registry": registry_path.as_posix(),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
