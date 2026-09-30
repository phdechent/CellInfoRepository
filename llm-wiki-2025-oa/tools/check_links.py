#!/usr/bin/env python
"""Verify that every [[wikilink]] resolves the way Obsidian resolves a click:
by note basename (or vault-relative path) only. Frontmatter `aliases:` are
used by Obsidian for autocomplete/search, NOT for resolving a clicked link, so
they are deliberately ignored here. Link to a concept by its file stem with a
display name: [[phase-change-material|Phase Change Material]].

Usage: check_links.py [wiki-dir]   (default: wiki-pages)
Exit 0 = all links resolve; 1 = broken links listed.
"""
import os
import re
import sys

W = sys.argv[1] if len(sys.argv) > 1 else "wiki-pages"


def markdown_files():
    for root, dirs, files in os.walk(W):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for name in files:
            if name.endswith(".md"):
                path = os.path.join(root, name)
                yield os.path.relpath(path, W), path


def main():
    resolvable = set()
    empty = []
    for rel, path in markdown_files():
        resolvable.add(os.path.basename(rel)[:-3])
        resolvable.add(rel[:-3].replace(os.sep, "/"))
        if os.path.getsize(path) == 0:
            empty.append(rel)

    broken = {}
    for rel, path in markdown_files():
        text = open(path, encoding="utf-8").read()
        for m in re.finditer(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]+)?\]\]", text):
            target = m.group(1).strip()
            if target not in resolvable:
                broken.setdefault(rel, set()).add(target)

    for rel in empty:
        print(f"EMPTY   [{rel}] (likely created by clicking a dangling link)")
    for rel, targets in sorted(broken.items()):
        for t in sorted(targets):
            print(f"BROKEN  [{rel}] -> [[{t}]]")
    if broken or empty:
        print(f"\n{sum(len(v) for v in broken.values())} broken links, "
              f"{len(empty)} empty notes. Link as [[file-stem|Display Name]].")
        return 1
    print(f"all wikilinks resolve ({len(resolvable)} resolvable names)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
