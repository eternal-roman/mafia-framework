# mafia-framework

Slash command: `/mafia-framework`

Mafia Framework. Evidence-only four-role power map. Assign Mafia, Sheriffs, Angel, and Townsfolk from observed incentive and action. Say who is winning, and name the metric that would falsify it.

**v1.2.0** — public cut. Skill name is `mafia-framework`, same as the local label. No private books, no orders, no personal data.

| File | Who it's for |
|---|---|
| [GROKBOT.md](GROKBOT.md) | Grok Bot upload. Asks for a topic, then maps. |
| [SKILL.md](SKILL.md) | Grok Build / coding agents. |
| [notebooks/dogfood.ipynb](notebooks/dogfood.ipynb) | Contract dogfood. Runs offline. |

Raw upload: https://raw.githubusercontent.com/eternal-roman/mafia-framework/main/GROKBOT.md

## Install

**grok.com / Grok Bot**

1. Open [grok.com/skills](https://grok.com/skills)
2. Upload `GROKBOT.md`
3. Type `/mafia-framework` and name one contested system

**Grok Build / coding agent**

```
mkdir -p ~/.grok/skills/mafia-framework
curl -L -o ~/.grok/skills/mafia-framework/SKILL.md \
  https://raw.githubusercontent.com/eternal-roman/mafia-framework/main/SKILL.md
```

## Contract

Six sections, or `DATA_THIN` with "Who Is Winning" omitted:

1. Key Roles
2. How the Game Is Going
3. Townsfolk Interests
4. Who Is Winning — plus 1–3 falsifiers in 30–90 days
5. Next-Best Decisions
6. Evidence Ledger

Roles reverse if the facts reverse. The label is not a moral verdict.

## Check

```
python3 scripts/selftest.py
python3 scripts/pii_scan.py
```

Not financial, legal, or political advice. A map of incentives, not a ticket.
