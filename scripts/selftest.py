#!/usr/bin/env python3
"""Contract selftest for the public mafia-framework skill."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / "SKILL.md").read_text()
bot = (ROOT / "GROKBOT.md").read_text()
version = (ROOT / "VERSION").read_text().strip()
bugs: list[str] = []


def check(name: str, cond: bool, detail: object = "") -> None:
    if not cond:
        bugs.append(f"{name}: {detail}")
        print("FAIL", name, detail)
    else:
        print("ok", name)


def main() -> int:
    check("version_file", version == "1.2.0", version)
    check("version_in_skill", "1.2.0" in text)
    check("version_in_bot", "1.2.0" in bot)
    for section in (
        "Key Roles",
        "How the Game Is Going",
        "Townsfolk Interests",
        "Who Is Winning",
        "Next-Best Decisions",
        "Evidence Ledger",
    ):
        check(f"section_{section[:16].lower().replace(' ', '_')}", section in text)
        check(f"bot_{section[:16].lower().replace(' ', '_')}", section in bot)
    check("data_thin", "DATA_THIN" in text)
    check("falsify", "falsify" in text.lower())
    check("no_invent", "No invented" in text)
    check("not_a_desk", "Not a trading desk" in text)
    check("role_mafia", "**Mafia**" in text)
    check("role_sheriffs", "**Sheriffs**" in text)
    check("role_angel", "**Angel**" in text)
    check("role_townsfolk", "**Townsfolk**" in text)
    check("invert", "invert" in text.lower())
    # Public cut must not pin private skill versions or venues.
    # Tokens are split so this file does not itself contain the private names.
    banned = (
        "v3." + "8",
        "hy" + "dra",
        "kra" + "ken",
        "trade-" + "engine",
        "btc-market-" + "snapshot",
    )
    for i, token in enumerate(banned):
        check(f"unpinned_{i}", token not in text.lower(), "private coupling")
    if bugs:
        print(f"\n{len(bugs)} FAIL")
        return 1
    print("\nALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
