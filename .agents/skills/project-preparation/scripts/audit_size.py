#!/usr/bin/env python3
"""Report local file size and Git-eligible size without changing the project."""

from __future__ import annotations

import argparse
from collections import defaultdict
import json
import math
import os
from pathlib import Path
import stat
import subprocess
import tempfile


GENERATED_DIRS = {
    "node_modules", ".next", "target", "dist", ".tools", ".venv", "venv",
    "__pycache__", "tmp", "test-results", "playwright-report",
}


def directory_link(path: Path) -> bool:
    details = path.lstat()
    return path.is_symlink() or getattr(details, "st_reparse_tag", 0) == getattr(
        stat, "IO_REPARSE_TAG_MOUNT_POINT", 0xA0000003
    )


def inventory(root: Path):
    files, skipped, errors = {}, [], []

    def walk_error(error):
        errors.append(str(error))

    for directory, subdirs, names in os.walk(root, onerror=walk_error):
        for name in list(subdirs):
            path = Path(directory) / name
            try:
                if name == ".git" or directory_link(path):
                    subdirs.remove(name)
                    skipped.append(path.relative_to(root).as_posix())
            except OSError as error:
                subdirs.remove(name)
                errors.append(str(error))
        for name in names:
            if name == ".git":  # Worktree metadata can be a file.
                continue
            path = Path(directory) / name
            try:
                # Git stores a file symlink's target text rather than its contents.
                size = len(os.fsencode(os.readlink(path))) if path.is_symlink() else path.stat().st_size
                files[path.relative_to(root).as_posix()] = size
            except OSError as error:
                errors.append(str(error))
    return files, skipped, errors


def git_run(args, **kwargs):
    return subprocess.run(
        ["git", *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        env={k: v for k, v in os.environ.items() if not k.startswith("GIT_")},
        **kwargs,
    )


def git_classification(root: Path, paths):
    # An isolated index avoids writes to the project and applies only its rules.
    with tempfile.TemporaryDirectory(prefix="scaffold-git-audit-") as temporary:
        initialized = git_run(["init", "--quiet", "--template=", temporary])
        if initialized.returncode:
            raise RuntimeError(os.fsdecode(initialized.stderr).strip())
        matched = git_run(
            ["--git-dir=" + str(Path(temporary) / ".git"), "--work-tree=" + str(root),
             "-c", "core.excludesFile=" + os.devnull, "check-ignore", "--no-index", "-z", "--stdin"],
            input=b"".join(os.fsencode(path) + b"\0" for path in paths),
        )
        if matched.returncode not in (0, 1):
            raise RuntimeError(os.fsdecode(matched.stderr).strip())
        ignored = {os.fsdecode(path) for path in matched.stdout.split(b"\0") if path}

    repository = git_run(["-C", str(root), "rev-parse", "--show-toplevel"])
    if repository.returncode:
        if b"not a git repository" in repository.stderr:
            return ignored, set(), "not initialized"
        raise RuntimeError(os.fsdecode(repository.stderr).strip())
    repository_root = Path(os.fsdecode(repository.stdout).strip()).resolve()
    tracked_result = git_run(["-C", str(root), "ls-files", "--cached", "-z"])
    if tracked_result.returncode:
        raise RuntimeError(os.fsdecode(tracked_result.stderr).strip())
    tracked = {os.fsdecode(path) for path in tracked_result.stdout.split(b"\0") if path}
    state = "initialized" if repository_root == root else "inside parent repository"
    return ignored, tracked, state


def audit(root: Path, large_mib: float = 50):
    files, skipped, errors = inventory(root)
    folders = defaultdict(int)
    for path, size in files.items():
        folders[path.split("/")[0]] += size
    report = {
        "project": str(root), "local_files": len(files), "local_bytes": sum(files.values()),
        "largest_top_level": sorted(folders.items(), key=lambda item: item[1], reverse=True)[:10],
        "largest_files": sorted(files.items(), key=lambda item: item[1], reverse=True)[:10],
        "skipped_directories": skipped, "errors": errors, "flags": [],
        "repository": "unknown", "eligible_bytes": None, "eligible_files": None,
    }
    try:
        ignored, tracked, report["repository"] = git_classification(root, files)
    except (OSError, RuntimeError) as error:
        errors.append("Git classification unavailable: " + str(error))
        return report
    eligible = {path: size for path, size in files.items() if path not in ignored or path in tracked}
    report.update(
        eligible_files=len(eligible), eligible_bytes=sum(eligible.values()),
        ignored_files=len(files) - len(eligible), ignored_bytes=sum(files.values()) - sum(eligible.values()),
        large_eligible=[path for path, size in eligible.items() if size >= large_mib * 1024**2],
        generated_eligible=[path for path in eligible if GENERATED_DIRS.intersection(path.split("/")[:-1])],
        tracked_matching_ignore=sorted(ignored & tracked),
        tracked_missing_locally=sorted(tracked - files.keys()),
    )
    for field, label in (
        ("large_eligible", f"Eligible files at least {large_mib:g} MiB"),
        ("generated_eligible", "Generated/tool files eligible for Git"),
        ("tracked_matching_ignore", "Tracked files still eligible despite ignore rules"),
        ("tracked_missing_locally", "Tracked paths absent from measured files; eligible size covers local files only"),
    ):
        if report[field]:
            report["flags"].append(label + f": {len(report[field])}")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_folder", type=Path)
    parser.add_argument("--large-mib", type=float, default=50, help="Large eligible file review threshold (default: 50)")
    parser.add_argument("--json", action="store_true", help="Emit full report as JSON")
    args = parser.parse_args()
    root = args.project_folder.resolve()
    if not root.is_dir():
        parser.error(f"project folder does not exist: {root}")
    if not math.isfinite(args.large_mib) or args.large_mib <= 0:
        parser.error("--large-mib must be positive and finite")
    report = audit(root, args.large_mib)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=True))
    else:
        print(f"Local: {report['local_bytes'] / 1024**2:.3f} MiB in {report['local_files']} files (excludes Git metadata).")
        if report["eligible_bytes"] is not None:
            print(f"Git eligible: {report['eligible_bytes'] / 1024**2:.3f} MiB in {report['eligible_files']} local files.")
        print(f"Repository: {report['repository']}. Rules: project .gitignore files; history/remotes not audited.")
        for field in ("largest_top_level", "largest_files"):
            print(field.replace("_", " ").capitalize() + ":")
            for path, size in report[field]:
                print(f"  {size / 1024**2:10.3f} MiB  {path}")
        for field in ("skipped_directories", "errors", "flags", "large_eligible", "generated_eligible", "tracked_matching_ignore", "tracked_missing_locally"):
            if report.get(field):
                print(field.replace("_", " ").capitalize() + ":")
                for entry in report[field][:20]:
                    print("  " + entry)
                if len(report[field]) > 20:
                    print("  More entries available with --json.")
    return 2 if report["errors"] else 1 if report["flags"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
