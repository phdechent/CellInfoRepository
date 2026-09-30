#!/usr/bin/env python
"""Verifies that every `> Evidence: "..."` quote in a wiki page appears
verbatim (modulo whitespace/unicode normalization) in the source text.

Usage: verify_quotes.py <wiki-page.md> <paper-text.txt>
Exit code 0 = all quotes verified; 1 = failures listed on stdout.
"""
import re
import sys
import unicodedata


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = re.sub(r"[\s ]+", " ", s)
    return s.lower().strip()


def main():
    md = open(sys.argv[1], encoding="utf-8").read()
    text = norm(open(sys.argv[2], encoding="utf-8", errors="replace").read())
    quotes = re.findall(r'> Evidence: "([^"]+)"', md)
    if not quotes:
        print("no evidence quotes found (all questions 'Not explicitly discussed.'?)")
        return 0
    failures = []
    for q in quotes:
        if norm(q) not in text:
            failures.append(q)
    if failures:
        print(f"{len(failures)}/{len(quotes)} quotes NOT found verbatim in source:")
        for q in failures:
            print(f'  - "{q[:90]}"')
        return 1
    print(f"all {len(quotes)} quotes verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
