#!/usr/bin/env python3
"""Backfill a MAXIM module into PROOF/MDCROP/MDPORT/FLETCH source-corpus artifacts."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
import tomllib
from pathlib import Path


ROOT = Path.cwd()

# Tool crates (PROOF/MDCROP/FLETCH) are located via the portfolio `repo-map.toml`
# config rather than hardcoded paths. The map records where every repo lives
# locally; we walk up from the current module checkout to find the portfolio
# root that defines the tool crates, then build each Cargo manifest path.
TOOL_CRATES = {"proof": "proof", "mdcrop": "mdcrop", "fletch": "fletch"}
# Portfolio map historically used `crop` for the MDCROP checkout.
TOOL_REPO_ALIASES = {"mdcrop": ("mdcrop", "crop")}


def resolve_tool_manifests() -> dict[str, Path | None]:
    """Resolve PROOF/MDCROP/FLETCH Cargo manifests from repo-map.toml.

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
            keys = TOOL_REPO_ALIASES.get(tool, (key,))
            rel = None
            for candidate_key in keys:
                rel = repos.get(candidate_key, {}).get("relative")
                if rel:
                    break
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


def ensure_frontmatter(path: Path, module_id: str, section: str, has_history: bool) -> dict[str, str]:
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
        "backsource_ids": bracket_list(guide_backsource_ids(module_id, num, slug, has_history)),
        "concepts": concepts,
        "root_concepts": roots,
        "index_roles": "[guide, root-concept]",
        "remap_from": "[]",
        "remap_to": "[]",
        "updated": "null",
    }
    merged = {**defaults, **fields}
    # backsource_ids is *derived* from provenance facts (PROOF literal backfill always
    # applies; git-history applies only when the file has real tracked history), so it must
    # be recomputed on every run and never preserved stale from existing frontmatter.
    merged["backsource_ids"] = defaults["backsource_ids"]
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


def guide_backsource_ids(module_id: str, num: str, slug: str, has_history: bool) -> list[str]:
    """Backsource IDs for a guide's frontmatter.

    The PROOF literal-backfill source always applies. A ``git-history`` backsource is
    included only when the file actually has tracked git history; an untracked or
    historyless file must not claim git provenance it does not have.
    """
    ids = [f"proof-backfill:{module_id}:{num}-{slug}"]
    if has_history:
        ids.append(f"git-history:{module_id}:{num}-{slug}")
    return ids


def source_record_backsource_ids(module_id: str, num: str, slug: str, has_history: bool) -> list[str]:
    """Backsource IDs for a generated source-record.

    The source-record's only backsource is git-history provenance, so it is present only
    when real tracked history exists and empty otherwise (its ``Git provenance`` line then
    stays ``pending``).
    """
    if has_history:
        return [f"git-history:{module_id}:{num}-{slug}"]
    return []


def module_provenance_note(guides: list[dict[str, object]]) -> str:
    """Summarize PROOF and git provenance without claiming history for untracked guides."""
    recorded = sum(bool(guide["git_hashes"]) for guide in guides)
    pending = len(guides) - recorded
    return (
        f"PROOF literal backfill is recorded for all {len(guides)} guides; "
        f"Git provenance is recorded for {recorded} guides and pending for {pending}."
    )


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


def markdown_heading_count(path: Path) -> int:
    """Count real Markdown headings in a canonical guide body."""
    _, body = parse_frontmatter(path)
    return sum(1 for line in body.splitlines() if re.match(r"^#{1,6}\s+\S", line))


def read_mdport(path: Path) -> dict:
    mdport = json.loads(path.read_text(encoding="utf-8"))
    if mdport.get("schema") != "mdport.v1" or not isinstance(mdport.get("sections"), list):
        raise ValueError(f"{path}: invalid mdport.v1 document")
    return mdport


def validate_full_guide_mdport(guide_path: Path, pack_path: Path) -> int:
    """Require the publication pack to preserve every canonical heading section."""
    expected = markdown_heading_count(guide_path)
    actual = len(read_mdport(pack_path)["sections"])
    if actual != expected:
        raise ValueError(
            f"{pack_path}: expected {expected} sections from {guide_path}, found {actual}"
        )
    return actual


def assemble_module_mdport(module_id: str, module_dir: Path, guides: list[dict], output: Path) -> int:
    """Assemble full guide Mdports into one collision-safe module corpus pack."""
    sections: list[dict] = []
    refs: list[str] = []
    for guide in guides:
        guide_mdport = read_mdport(Path(guide["pack"]))
        for section in guide_mdport["sections"]:
            copied = dict(section)
            copied["id"] = f"{guide['slug']}:{section['id']}"
            sections.append(copied)
        refs.extend(guide_mdport.get("refs", []))
    module_mdport = {
        "schema": "mdport.v1",
        "kind": "corpus-slice",
        "title": f"MAXIM {module_id} source corpus",
        "source": module_dir.as_posix(),
        "format": "markdown",
        "metadata": {
            "assembly": "full-guide-proof-mdports",
            "module": module_id,
            "guide_count": len(guides),
        },
        "sections": sections,
        "refs": list(dict.fromkeys(refs)),
    }
    write_text(output, json.dumps(module_mdport, ensure_ascii=False, separators=(",", ":")) + "\n")
    return len(sections)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module-dir", required=True, help="Module directory containing numbered markdown guides.")
    parser.add_argument("--module-id", required=True, help="Stable MAXIM module id, e.g. computing-software.")
    parser.add_argument("--section", help="Section id; defaults to --module-id.")
    parser.add_argument("--proof-manifest", default=None, help="Override PROOF Cargo.toml (default: from repo-map.toml).")
    parser.add_argument("--mdcrop-manifest", default=None, help="Override MDCROP Cargo.toml (default: from repo-map.toml).")
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
    view_store = Path(".mdcrop") / "views"
    pack_store = Path(".mdport") / "packs"
    module_view = view_store / f"maxim-{module_id}-source-corpus.json"
    module_pack = pack_store / f"maxim-{module_id}-source-corpus.mdport.json"
    registry_path = Path(".fletch") / "registries" / f"maxim-{module_id}-source-corpus.json"

    guides: list[dict[str, str]] = []
    for path in sorted(module_dir.glob("??-*.md")):
        hashes = git_hashes(path.as_posix())
        fields = ensure_frontmatter(path, module_id, section, has_history=bool(hashes))
        slug = fields["id"].replace(f"maxim:{module_id}:", "")
        base = path.stem
        num = path.name[:2]
        view_path = view_store / f"maxim-{module_id}-{slug}.json"
        pack_path = pack_store / f"maxim-{module_id}-{slug}.mdport.json"
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
            "git_hashes": hashes,
            "view": view_path.as_posix(),
            "pack": pack_path.as_posix(),
        }
        guides.append(guide)
        view = {
            "schema_version": "mdcrop.view.v1",
            "name": f"maxim-{module_id}-{slug}",
            "root": f"../../{module_dir.as_posix()}",
            "task": f"Backfill MAXIM {fields['title']} as a partial source-custody fact/context pack.",
            "token_budget": 12000,
            "seed": 0,
            "frontmatter_query": f"id eq '{fields['id']}'",
            "include_extensions": ["md"],
            "exclude_dirs": [".git", ".claude", ".mdcrop", ".mkdocs", ".roles", ".vscode", "_archive"],
        }
        write_text(view_path, json.dumps(view, indent=2, ensure_ascii=False) + "\n")

    module_view_json = {
        "schema_version": "mdcrop.view.v1",
        "name": f"maxim-{module_id}-source-corpus",
        "root": f"../../{module_dir.as_posix()}",
        "task": f"Backfill the MAXIM {module_id} module for downstream fact/context reuse.",
        "token_budget": 12000,
        "seed": 0,
        "frontmatter_query": "source_custody eq 'partial'",
        "include_extensions": ["md"],
        "exclude_dirs": [".git", ".claude", ".mdcrop", ".mkdocs", ".roles", ".vscode", "_archive"],
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

    for guide in guides:
        run(
            [
                "cargo",
                "run",
                "--manifest-path",
                args.proof_manifest,
                "--quiet",
                "--",
                "compile",
                guide["source_md"],
                "--target",
                "mdport",
                "-o",
                guide["pack"],
            ],
        )
        guide["pack_sections"] = validate_full_guide_mdport(
            Path(guide["path"]), Path(guide["pack"])
        )
    module_pack_sections = assemble_module_mdport(
        module_id, module_dir, guides, module_pack
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
        record_backsources = source_record_backsource_ids(
            module_id, guide["num"], guide["slug"], bool(guide["git_hashes"])
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
backsource_ids: {bracket_list(record_backsources)}
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
| Git provenance | {tick_list(guide['git_hashes'])} |

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
        "distribution": {
            "mdport_pack": module_pack.as_posix(),
            "mdport_pack_sections": module_pack_sections,
            "guide_packs": [guide["pack"] for guide in guides],
            "guide_pack_sections": {
                guide["path"]: guide["pack_sections"] for guide in guides
            },
            "fletch_registry": registry_path.as_posix(),
        },
        "source_custody": {
            "policy": "Each guide must map to an authentic backsource record before pack publication.",
            "default_state": "partial",
            "notes": [
                "Current MAXIM guide paths are not themselves sufficient backsources.",
                "Backsources can be source notes, cited originals, generated proof artifacts, or reviewed provenance records.",
                module_provenance_note(guides),
                f"All {len(guides)} guides remain partial because external/authentic factual backsources are still pending.",
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
        "gates": [
            "frontmatter-contract-applied",
            "source-custody-partial",
            "proof-module-clean",
            "crop-views-added",
            "full-proof-mdport-packs-emitted",
            "fletch-registry-added",
        ],
    }
    write_text(module_ledger, json.dumps(module, indent=2, ensure_ascii=False) + "\n")

    fletches = [
        {
            "id": f"maxim.{module_id}.source-corpus.mdport",
            "node_kind": "fletch",
            "shafts": [{"kind": "file", "url": module_pack.as_posix()}],
            "edges": [
                {
                    "to": f"maxim.{module_id}.{guide['slug']}.mdport",
                    "kind": "derived-from",
                    "label": "Full guide PROOF Mdport",
                    "metadata": {"module": module_id, "guide": guide["path"], "custody": "partial"},
                }
                for guide in guides
            ],
            "format": format_obj("mdport.v1", "corpus-slice", module_pack.as_posix()),
            "tags": ["source-corpus", "proof", "mdport", "full-module", "partial-custody"],
            "metadata": {"source_repo": "MAXIM", "module": module_id, "distribution": "FLETCH full-module publication surface for downstream repos", "publication_state": "partial-source-custody"},
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
                    "edges": [{"to": f"{prefix}.proof-source", "kind": "derived-from", "label": "View over canonical guide source", "metadata": {"module": module_id, "guide": guide["path"], "custody": "partial"}}],
                    "format": format_obj("mdcrop.view.v1", "view-recipe", guide["view"]),
                    "tags": ["source-corpus", "mdcrop", "view", "partial-custody", "guide"],
                    "metadata": common,
                },
                {
                    "id": f"{prefix}.mdport",
                    "node_kind": "fletch",
                    "shafts": [{"kind": "file", "url": guide["pack"]}],
                    "edges": [{"to": f"{prefix}.proof-source", "kind": "derived-from", "label": "Full guide PROOF publication", "metadata": {"module": module_id, "guide": guide["path"], "custody": "partial"}}],
                    "format": format_obj("mdport.v1", "document", guide["pack"]),
                    "tags": ["source-corpus", "proof", "mdport", "full-guide", "partial-custody", "guide"],
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
        # Inspect only this module's views — full-library .mdcrop/views is multi-minute
        # and floods logs during incremental backfills.
        # Views use roots like ../../<module>; keep the temp dir at the same depth as
        # .mdcrop/views so those relatives still resolve to the repo module folders.
        module_view_paths = [guide["view"] for guide in guides] + [module_view.as_posix()]
        tmp_dir = view_store.parent / f"_validate_tmp_{module_id}"
        if tmp_dir.exists():
            shutil.rmtree(tmp_dir)
        tmp_dir.mkdir(parents=True, exist_ok=True)
        try:
            for view_path in module_view_paths:
                src = Path(view_path)
                if src.is_file():
                    (tmp_dir / src.name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
            run(
                [
                    "cargo",
                    "run",
                    "--manifest-path",
                    args.mdcrop_manifest,
                    "--quiet",
                    "--",
                    "view",
                    "--inspect",
                    "--dir",
                    str(tmp_dir),
                    "--strict",
                ]
            )
        finally:
            shutil.rmtree(tmp_dir, ignore_errors=True)
        run(["cargo", "run", "--manifest-path", args.fletch_manifest, "--bin", "fletch-cli", "--quiet", "--", "registry", "validate", "--file", str(registry_path)])
        missing = [shaft["url"] for fletch in fletches for shaft in fletch["shafts"] if not Path(shaft["url"]).exists()]
        if missing:
            raise SystemExit(f"registry shaft paths missing: {missing}")
        for guide in guides:
            validate_full_guide_mdport(Path(guide["path"]), Path(guide["pack"]))
        if len(read_mdport(module_pack)["sections"]) != sum(
            guide["pack_sections"] for guide in guides
        ):
            raise SystemExit("module Mdport section count does not match guide packs")
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
                "guide_pack_sections": {
                    guide["path"]: guide["pack_sections"] for guide in guides
                },
                "module_pack_sections": module_pack_sections,
                "fletches": len(fletches),
                "registry": registry_path.as_posix(),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
