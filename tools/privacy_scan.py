#!/usr/bin/env python3
"""Scan a folder for things that identify a company, a person or a vendor.

Run it before you share filled-in templates, prompts or rules outside your company.

    python3 privacy_scan.py PATH [--names names.txt] [--allow allow.txt]

It reports, per file and line:
  - email addresses
  - phone numbers
  - long IDs (20 or more letters and digits, or 13 or more digits in a row)
  - money amounts ($, EUR, GBP signs or codes followed by a number)
  - every word or phrase listed in --names (one per line, case-insensitive,
    whole words): your company and brand names, people's names, vendors.
    Keep that file outside the folder you scan, so it never ships.

--allow takes lines to ignore: exact strings that may appear (for example
"noreply@example.com"). Exit code 1 if anything was found, else 0.
"""
import argparse
import pathlib
import re
import sys

TEXT_SUFFIXES = {".md", ".txt", ".py", ".html", ".css", ".json", ".yml", ".yaml", ""}

PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "phone": re.compile(r"(?<![\w-])(?:\+?\d{1,3}[\s.-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}(?![\w-])"),
    "long id": re.compile(r"\b(?=[A-Za-z0-9_-]*\d)[A-Za-z0-9_-]{20,}\b|\b\d{13,}\b"),
    "money": re.compile(r"(?:[$€£]\s?\d[\d,.]*|\b[A-Z]{3}\s?\d[\d,.]*)"),
}


def load_lines(path):
    if not path:
        return []
    return [ln.strip() for ln in pathlib.Path(path).read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.strip().startswith("#")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--names")
    ap.add_argument("--allow")
    args = ap.parse_args()

    names = load_lines(args.names)
    allow = load_lines(args.allow)
    name_res = [(n, re.compile(r"(?<![\w])" + re.escape(n) + r"(?![\w])", re.I)) for n in names]

    root = pathlib.Path(args.path)
    files = [root] if root.is_file() else sorted(p for p in root.rglob("*") if p.is_file())
    hits = 0
    scanned = 0
    for f in files:
        if ".git" in f.parts or f.suffix.lower() not in TEXT_SUFFIXES:
            continue
        scanned += 1
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for i, line in enumerate(text.splitlines(), 1):
            found = []
            for label, rx in PATTERNS.items():
                for m in rx.finditer(line):
                    if m.group(0) not in allow:
                        found.append((label, m.group(0)))
            for n, rx in name_res:
                for m in rx.finditer(line):
                    found.append(("name", m.group(0)))
            for label, val in found:
                hits += 1
                print(f"{f}:{i}: {label}: {val}")
    print(f"\n{hits} hit(s) in {scanned} file(s) scanned.")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
