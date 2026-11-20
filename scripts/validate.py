#!/usr/bin/env python3
"""Validates structural consistency of the DevCheatSheets repo.

Run manually:   python scripts/validate.py
Run in CI:      python scripts/validate.py  (exit 1 on any failure)

Adding a new check:
  1. Write a function named check_<something>() -> list[str]
  2. Add it to the CHECKS list at the bottom of this file.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
README = ROOT / "README.md"
DOCS_DIR = ROOT / "Documents"
IMAGES_DIR = ROOT / "Images"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _local_md_links(file: Path) -> list[tuple[int, str]]:
    """Return (line_number, path) for all local .md links in a Markdown file."""
    link_re = re.compile(r'\[.*?\]\(([^)]+\.md)\)')
    results = []
    for i, line in enumerate(file.read_text(encoding="utf-8").split("\n"), 1):
        for match in link_re.finditer(line):
            href = match.group(1)
            if not href.startswith("http"):
                results.append((i, href))
    return results


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_readme_links() -> list[str]:
    """All local .md links in README.md must point to existing files."""
    if not README.exists():
        return ["README.md not found"]
    errors = []
    for line_num, href in _local_md_links(README):
        target = (README.parent / href).resolve()
        if not target.exists():
            errors.append(f"README.md:{line_num}: broken link → {href}")
    return errors


def check_orphaned_docs() -> list[str]:
    """Every file in Documents/ must be linked from README.md."""
    if not README.exists():
        return ["README.md not found"]
    readme_text = README.read_text(encoding="utf-8")
    errors = []
    for doc in sorted(DOCS_DIR.glob("*.md")):
        rel = _rel(doc)
        if rel not in readme_text:
            errors.append(f"{rel}: exists on disk but is not linked from README.md")
    return errors


def check_unreferenced_images() -> list[str]:
    """Every file in Images/ must be referenced from README.md or a Documents/ file."""
    if not IMAGES_DIR.exists():
        return []
    text = README.read_text(encoding="utf-8") if README.exists() else ""
    for doc in DOCS_DIR.glob("*.md"):
        text += doc.read_text(encoding="utf-8")
    return [
        f"{_rel(img)}: not referenced from README.md or Documents/"
        for img in sorted(IMAGES_DIR.iterdir())
        if img.is_file() and img.name not in text
    ]


def check_unlabeled_fences() -> list[str]:
    """Every opening code fence in Documents/ must carry a language tag."""
    errors = []
    for doc in sorted(DOCS_DIR.glob("*.md")):
        in_fence = False
        for i, line in enumerate(doc.read_text(encoding="utf-8").split("\n"), 1):
            stripped = line.strip()
            if not stripped.startswith("```"):
                continue
            if not in_fence:
                in_fence = True
                if stripped == "```":
                    errors.append(f"{_rel(doc)}:{i}: code fence has no language tag")
            else:
                in_fence = False
    return errors


def check_empty_sections() -> list[str]:
    """Every leaf heading in Documents/ must have body text before the next heading."""
    heading_re = re.compile(r"^(#{1,6})\s+\S")
    errors = []
    for doc in sorted(DOCS_DIR.glob("*.md")):
        # Collect (line_number, level) for headings outside code fences,
        # plus the line numbers of non-blank, non-heading content lines.
        headings: list[tuple[int, int]] = []
        content_lines: list[int] = []
        in_fence = False
        for i, line in enumerate(doc.read_text(encoding="utf-8").split("\n"), 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_fence = not in_fence
                content_lines.append(i)
                continue
            if in_fence:
                content_lines.append(i)
                continue
            match = heading_re.match(line)
            if match:
                headings.append((i, len(match.group(1))))
            elif stripped:
                content_lines.append(i)
        for idx, (line_num, level) in enumerate(headings):
            if idx == 0:
                continue  # the first heading is the page title, not a section
            nxt =headings[idx + 1] if idx + 1 < len(headings) else None
            if nxt is not None and nxt[1] > level:
                continue  # parent heading: its subheadings are its body
            end = nxt[0] if nxt else float("inf")
            if not any(line_num < c < end for c in content_lines):
                errors.append(f"{_rel(doc)}:{line_num}: heading has no content")
    return errors


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

CHECKS = [
    check_readme_links,
    check_orphaned_docs,
    check_unreferenced_images,
    check_unlabeled_fences,
    check_empty_sections,
]


def _label(fn) -> str:
    return fn.__name__.replace("check_", "").replace("_", " ").title()


def main() -> None:
    all_errors: list[str] = []

    for check in CHECKS:
        errors = check()
        if errors:
            print(f"[FAIL] {_label(check)}")
            for err in errors:
                print(f"       {err}")
            all_errors.extend(errors)
        else:
            print(f"[ OK ] {_label(check)}")

    print()
    if all_errors:
        print(f"{len(all_errors)} issue(s) found.")
        sys.exit(1)
    else:
        print("All checks passed.")


if __name__ == "__main__":
    main()
