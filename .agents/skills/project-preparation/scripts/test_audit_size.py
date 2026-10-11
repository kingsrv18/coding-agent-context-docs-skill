"""Behavioral checks for size accounting and Git eligibility."""

import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from audit_size import audit


class SizeAuditTests(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory(prefix="scaffold-audit-test-")
        self.addCleanup(self.scratch.cleanup)
        self.root = Path(self.scratch.name).resolve()

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def git(self, *args):
        subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True)

    def test_nested_rules_negation_and_no_project_mutation(self):
        self.write(".gitignore", b"node_modules/\n.next/\n.env.*\n!.env.example\n")
        self.write("apps/web/.gitignore", b"scratch/\n")
        self.write("apps/web/.env.example", b"example")
        self.write("apps/web/.env.local", b"private")
        self.write("apps/web/node_modules/native.bin", b"x" * 4096)
        self.write("apps/web/.next/cache.bin", b"x" * 2048)
        self.write("apps/web/scratch/render.png", b"x" * 1024)
        self.write("package-lock.json", b"lock")
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        report = audit(self.root)
        expected = len(before[Path(".gitignore")]) + len(before[Path("apps/web/.gitignore")]) + 7 + 4
        self.assertEqual(report["eligible_bytes"], expected)
        self.assertEqual(report["ignored_files"], 4)
        self.assertEqual(report["repository"], "not initialized")
        self.assertEqual(report["flags"], [])
        self.assertEqual(before, {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()})
        self.assertFalse((self.root / ".git").exists())

    def test_tracked_ignored_file_remains_eligible_without_index_changes(self):
        self.write(".gitignore", b"node_modules/\n")
        self.write("node_modules/previously-added.bin", b"tracked")
        self.git("init", "--quiet", "--template=")
        self.git("add", "-f", "node_modules/previously-added.bin")
        index_before = (self.root / ".git/index").read_bytes()
        report = audit(self.root)
        self.assertEqual(report["tracked_matching_ignore"], ["node_modules/previously-added.bin"])
        self.assertEqual(report["eligible_bytes"], len(b"node_modules/\n") + 7)
        self.assertEqual(report["ignored_files"], 0)
        self.assertEqual(index_before, (self.root / ".git/index").read_bytes())

    def test_large_and_unignored_generated_files_are_flagged(self):
        self.write(".tools/runtime.bin", b"x" * 2048)
        report = audit(self.root, large_mib=1 / 1024)
        self.assertEqual(report["large_eligible"], [".tools/runtime.bin"])
        self.assertEqual(report["generated_eligible"], [".tools/runtime.bin"])
        self.assertEqual(len(report["flags"]), 2)

    def test_missing_git_reports_unknown_eligibility(self):
        self.write("prd.md", b"source")
        with patch("audit_size.git_run", side_effect=FileNotFoundError("git unavailable")):
            report = audit(self.root)
        self.assertEqual(report["local_bytes"], 6)
        self.assertIsNone(report["eligible_bytes"])
        self.assertTrue(report["errors"])

    def test_workspace_directory_link_is_not_counted_twice(self):
        source = self.write("apps/web/source.txt", b"source").parent
        link = self.root / "linked-web"
        if os.name == "nt":
            # Native PowerShell creates a junction without requiring symlink privilege.
            def quote(value):
                return "'" + str(value).replace("'", "''") + "'"
            subprocess.run(
                ["powershell", "-NoProfile", "-Command",
                 f"New-Item -ItemType Junction -Path {quote(link)} -Target {quote(source)} | Out-Null"],
                check=True, capture_output=True,
            )
            self.addCleanup(lambda: os.rmdir(link))
        else:
            link.symlink_to(source, target_is_directory=True)
        report = audit(self.root)
        self.assertEqual(report["local_bytes"], 6)
        self.assertEqual(report["local_files"], 1)
        self.assertIn("linked-web", report["skipped_directories"])


if __name__ == "__main__":
    unittest.main()
