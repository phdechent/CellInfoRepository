#!/usr/bin/env python3
"""Resolve a portable review manifest without SQLite."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def slug(value: str, maxlen: int = 70) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:maxlen].rstrip("-")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/set_info.py <review-set.json>", file=sys.stderr)
        return 2
    set_path = Path(sys.argv[1])
    if not set_path.is_absolute():
        set_path = ROOT / set_path
    job = json.loads(set_path.read_text(encoding="utf-8"))
    output_dir = ROOT / job.get("output_dir", "wiki-pages")
    print(json.dumps({"set": str(set_path.relative_to(ROOT)),
                      "template": job.get("template"),
                      "n_papers": len(job.get("papers", [])),
                      "output_dir": str(output_dir.relative_to(ROOT))}))
    missing = 0
    for paper in job.get("papers", []):
        title = paper.get("title") or paper["doi_key"]
        source = ROOT / paper.get(
            "fulltext_source", f"text/{paper['doi_key']}.txt")
        output = output_dir / f"{slug(title)}.md"
        row = {**paper, "text_path": str(source.relative_to(ROOT)),
               "text_exists": source.is_file(),
               "out_path": str(output.relative_to(ROOT)),
               "done": output.is_file()}
        missing += not row["text_exists"]
        print(json.dumps(row, ensure_ascii=False))
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
