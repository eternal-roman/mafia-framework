#!/usr/bin/env python3
"""Fail if the public tree contains private-book or credential markers.

Personal names are not listed here. A local pre-publish scan covers those
and is not part of this tree.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git"}
# Split so this file does not contain the private names.
RAW = (
    "hy" + "dra",
    "kra" + "ken",
    "trade-" + "engine",
    "btc-market-" + "snapshot",
    "cowen-" + "cycle",
)
PATTERNS = [re.compile(re.escape(token), re.I) for token in RAW]
PATTERNS.append(re.compile(r"api[_ -]?key", re.I))
PATTERNS.append(re.compile(r"\bpassword\b", re.I))
PATTERNS.append(re.compile(r"\b\d{3}-\d{2}-\d{4}\b"))


def main() -> int:
    hits: list[str] = []
    files = [
        p
        for p in ROOT.rglob("*")
        if p.is_file() and not any(s in p.parts for s in SKIP_PARTS)
    ]
    for path in files:
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
            continue
        if path.name == "pii_scan.py":
            continue
        text = path.read_text(errors="replace")
        for cre in PATTERNS:
            if cre.search(text):
                hits.append(f"{path.relative_to(ROOT)} :: matched private or credential marker")
    if hits:
        print("PII FAIL")
        for hit in hits:
            print(" -", hit)
        return 1
    print(f"PII PASS ({len(files)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
