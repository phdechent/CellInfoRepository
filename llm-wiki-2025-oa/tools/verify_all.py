#!/usr/bin/env python3
"""Verify all evidence quotations in a portable review set."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def slug(value: str, maxlen: int = 70) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:maxlen].rstrip("-")


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    value = value.replace("’", "'").replace("‘", "'")
    value = value.replace("“", '"').replace("”", '"')
    return re.sub(r"[\s ]+", " ", value).lower().strip()


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/verify_all.py <review-set.json>", file=sys.stderr)
        return 2
    manifest = Path(sys.argv[1])
    if not manifest.is_absolute():
        manifest = ROOT / manifest
    job = json.loads(manifest.read_text(encoding="utf-8"))
    output_dir = ROOT / job.get("output_dir", "wiki-pages")
    checked = quotes_checked = 0
    failures = []
    for paper in job.get("papers", []):
        title = paper.get("title") or paper["doi_key"]
        note = output_dir / f"{slug(title)}.md"
        source = ROOT / paper.get(
            "fulltext_source", f"text/{paper['doi_key']}.txt")
        if not note.is_file() or not source.is_file():
            failures.append(f"missing file(s): {paper['doi_key']}")
            continue
        markdown = note.read_text(encoding="utf-8")
        fulltext = norm(source.read_text(encoding="utf-8", errors="replace"))
        quotes = re.findall(r'> Evidence: "([^"]+)"', markdown)
        missing = [quote for quote in quotes if norm(quote) not in fulltext]
        if missing:
            failures.append(
                f"{paper['doi_key']}: {len(missing)}/{len(quotes)} quotes missing")
        checked += 1
        quotes_checked += len(quotes)
    print(f"checked {checked} notes and {quotes_checked} evidence quotations")
    for failure in failures:
        print(f"FAIL {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
