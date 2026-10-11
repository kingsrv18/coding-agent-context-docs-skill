#!/usr/bin/env python3
"""Check a generated project package for missing local document references."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


LINK = re.compile(r"(?<!!)\[[^\]]+\]\((<[^>]+>|[^)]+)\)")
CODE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
DOC_PATH = re.compile(r"(?i)(?:^|/)[\w.-]+\.(?:md|pdf)$")
EXTERNAL = re.compile(r"(?i)^(?:[a-z][a-z0-9+.-]*:|//)")
SKIP_DIRS = {".git", ".next", ".venv", "__pycache__", "dist", "node_modules"}


def project_markdown(root: Path):
    for directory, subdirs, files in os.walk(root):
        subdirs[:] = [name for name in subdirs if name not in SKIP_DIRS]
        for name in files:
            if name.lower().endswith(".md"):
                yield Path(directory) / name


def meaningful_lines(markdown: str):
    fence = None
    for number, line in enumerate(markdown.splitlines(), 1):
        marker = re.match(r"^\s*([`~]{3,})", line)
        if marker:
            character = marker.group(1)[0]
            if fence is None:
                fence = character
            elif fence == character:
                fence = None
            continue
        if fence is None:
            yield number, line


def candidates(raw: str, root: Path, source: Path):
    raw = raw.strip()
    raw = unquote(raw[1:-1] if raw.startswith("<") and raw.endswith(">") else raw.split(" ", 1)[0])
    target = urlsplit(raw).path.replace("\\", "/")
    if not target or target.startswith("#") or EXTERNAL.match(raw):
        return []
    if any(part in target for part in ("...", "<", ">", "*", "{", "}")):
        return []
    if target.startswith("/"):
        return [root / target.lstrip("/")]
    if target.startswith(("docs/", "deliverables/")):
        return [root / target]
    options = [source.parent / target, root / target]
    if "/" not in target:
        docs = root / "docs"
        if docs.is_dir():
            options.extend(docs.rglob(target))
    return options


def inspect(root: Path, pdf: str | None):
    issues = []
    for required in ("README.md", "AGENTS.md", "docs"):
        if not (root / required).exists():
            issues.append(f"missing required package entry: {required}")

    markdown_files = sorted(project_markdown(root))
    if not markdown_files:
        issues.append("no Markdown context documents found")

    for source in markdown_files:
        content = source.read_text(encoding="utf-8-sig")
        if not content.strip():
            issues.append(f"empty document: {source.relative_to(root)}")
        for number, line in meaningful_lines(content):
            raw_targets = [match.group(1) for match in LINK.finditer(line)]
            raw_targets += [
                match.group(1)
                for match in CODE.finditer(line)
                if DOC_PATH.search(match.group(1).replace("\\", "/"))
            ]
            for raw in raw_targets:
                options = candidates(raw, root, source)
                if not options:
                    continue
                inside = [path.resolve() for path in options if path.resolve().is_relative_to(root)]
                if inside and not any(path.exists() for path in inside):
                    issues.append(
                        f"{source.relative_to(root)}:{number}: unresolved local reference {raw}"
                    )

    if pdf:
        target = (root / pdf).resolve()
        if not target.is_relative_to(root):
            issues.append(f"PDF path leaves package root: {pdf}")
        elif not target.is_file():
            issues.append(f"missing PDF: {pdf}")
        else:
            with target.open("rb") as stream:
                if stream.read(5) != b"%PDF-":
                    issues.append(f"file is not a PDF: {pdf}")
    return sorted(set(issues)), len(markdown_files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_folder", type=Path)
    parser.add_argument("--pdf", help="PDF path relative to the project folder")
    args = parser.parse_args()
    root = args.project_folder.resolve()
    if not root.is_dir():
        parser.error(f"project folder does not exist: {root}")
    issues, count = inspect(root, args.pdf)
    if issues:
        for issue in issues:
            print(f"ERROR {issue}")
        print(f"Checked {count} Markdown files; {len(issues)} issue(s).")
        return 1
    print(f"Checked {count} Markdown files; local references and package entries passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
