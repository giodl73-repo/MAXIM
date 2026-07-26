"""Focused unit tests for module_source_backfill git-history custody behavior.

These tests use only the Python standard library plus git (which the generator
already depends on). They cover the two provenance states that mattered for the
custody bug:

* a file with real tracked history -> a ``git-history`` backsource is claimed;
* an untracked / historyless file -> no ``git-history`` backsource is claimed,
  and the source-record's Git provenance stays ``pending``.
* the module ledger reports recorded and pending Git-provenance counts truthfully.
"""

from __future__ import annotations

import os
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))

import module_source_backfill as msb  # noqa: E402


class GuideBacksourceIdTests(unittest.TestCase):
    """The guide frontmatter always keeps mdloom-backfill; git-history is conditional."""

    def test_includes_git_history_when_history_present(self):
        ids = msb.guide_backsource_ids("pathology", "00", "overview", True)
        self.assertEqual(
            ids,
            [
                "mdloom-backfill:pathology:00-overview",
                "git-history:pathology:00-overview",
            ],
        )

    def test_omits_git_history_when_no_history(self):
        ids = msb.guide_backsource_ids("pathology", "00", "overview", False)
        self.assertEqual(ids, ["mdloom-backfill:pathology:00-overview"])
        self.assertNotIn("git-history:pathology:00-overview", ids)


class SourceRecordBacksourceIdTests(unittest.TestCase):
    """The source-record's only backsource is git-history, present iff history exists."""

    def test_git_history_when_history_present(self):
        self.assertEqual(
            msb.source_record_backsource_ids("pathology", "05", "neoplasia", True),
            ["git-history:pathology:05-neoplasia"],
        )

    def test_empty_when_no_history(self):
        self.assertEqual(
            msb.source_record_backsource_ids("pathology", "05", "neoplasia", False),
            [],
        )

    def test_empty_list_renders_as_bracket_pair(self):
        rendered = msb.bracket_list(
            msb.source_record_backsource_ids("pathology", "05", "neoplasia", False)
        )
        self.assertEqual(rendered, "[]")


class ModuleProvenanceNoteTests(unittest.TestCase):
    """The module ledger reports git provenance counts rather than a blanket claim."""

    def test_all_untracked_guides_report_git_provenance_pending(self):
        guides = [{"git_hashes": []} for _ in range(12)]
        self.assertEqual(
            msb.module_provenance_note(guides),
            "MDLOOM literal backfill is recorded for all 12 guides; "
            "Git provenance is recorded for 0 guides and pending for 12.",
        )

    def test_mixed_history_reports_recorded_and_pending_counts(self):
        guides = [
            {"git_hashes": ["abc123"]},
            {"git_hashes": []},
            {"git_hashes": ["def456", "abc123"]},
        ]
        self.assertEqual(
            msb.module_provenance_note(guides),
            "MDLOOM literal backfill is recorded for all 3 guides; "
            "Git provenance is recorded for 2 guides and pending for 1.",
        )


class GitHashesTests(unittest.TestCase):
    """git_hashes must distinguish tracked history from untracked/no-history files."""

    def setUp(self):
        self._cwd = os.getcwd()
        self._tmp = tempfile.TemporaryDirectory()
        os.chdir(self._tmp.name)
        for cmd in (
            ["git", "init", "-q"],
            ["git", "config", "user.email", "test@example.com"],
            ["git", "config", "user.name", "Test"],
            ["git", "config", "commit.gpgsign", "false"],
        ):
            subprocess.run(cmd, check=True)
        # Seed commit so the repo has history while individual files may not.
        Path(".gitkeep").write_text("", encoding="utf-8")
        subprocess.run(["git", "add", ".gitkeep"], check=True)
        subprocess.run(["git", "commit", "-q", "-m", "seed"], check=True)

    def tearDown(self):
        os.chdir(self._cwd)
        self._tmp.cleanup()

    def test_tracked_committed_file_reports_history(self):
        Path("tracked.md").write_text("# tracked\n", encoding="utf-8")
        subprocess.run(["git", "add", "tracked.md"], check=True)
        subprocess.run(["git", "commit", "-q", "-m", "add tracked"], check=True)
        self.assertTrue(msb.git_hashes("tracked.md"))

    def test_untracked_file_reports_no_history(self):
        Path("untracked.md").write_text("# untracked\n", encoding="utf-8")
        self.assertEqual(msb.git_hashes("untracked.md"), [])


class FullMdportTests(unittest.TestCase):
    def test_heading_count_ignores_frontmatter(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "guide.md"
            path.write_text(
                "---\nid: test\n---\n# Guide\n\n## One\n\n### Detail\n\n## Two\n",
                encoding="utf-8",
            )
            self.assertEqual(msb.markdown_heading_count(path), 4)

    def test_validate_full_guide_mdport_rejects_truncation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            guide = root / "guide.md"
            pack = root / "guide.mdport.json"
            guide.write_text("# Guide\n\n## One\n\n## Two\n", encoding="utf-8")
            pack.write_text(
                json.dumps(
                    {
                        "schema": "mdport.v1",
                        "kind": "document",
                        "sections": [{"id": "guide", "text": "# Guide"}],
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "expected 3 sections"):
                msb.validate_full_guide_mdport(guide, pack)

    def test_assemble_module_mdport_prefixes_section_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = root / "first.json"
            second = root / "second.json"
            output = root / "module.json"
            for path, title in ((first, "One"), (second, "Two")):
                path.write_text(
                    json.dumps(
                        {
                            "schema": "mdport.v1",
                            "kind": "document",
                            "sections": [{"id": "overview", "text": title}],
                            "refs": [f"{title}.md"],
                        }
                    ),
                    encoding="utf-8",
                )
            guides = [
                {"slug": "one", "pack": str(first)},
                {"slug": "two", "pack": str(second)},
            ]
            self.assertEqual(
                msb.assemble_module_mdport("test", Path("test"), guides, output),
                2,
            )
            module = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(
                [section["id"] for section in module["sections"]],
                ["one:overview", "two:overview"],
            )
            self.assertEqual(module["refs"], ["One.md", "Two.md"])


if __name__ == "__main__":
    unittest.main()
