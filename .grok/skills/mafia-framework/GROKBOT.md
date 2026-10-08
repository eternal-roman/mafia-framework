---
name: mafia-framework
description: >
  Evidence-only four-role power map for a contested system. Assigns Mafia,
  Sheriffs, Angel, and Townsfolk from observed incentive and action, then
  states who is winning and what would falsify it. Use for Mafia analysis,
  power mapping, incentive mapping, or who is winning. Not a trading desk.
  Does not emit orders, tickets, or position advice.
when-to-use: >
  mafia analysis, power mapping, incentive mapping, who is winning,
  /mafia, contested system, role map
argument-hint: "[topic]"
user-invocable: true
metadata:
  short-description: Evidence-only four-role power map
  author: eternal-roman
  version: "1.2.0"
  type: workflow
---

# Mafia Framework v1.2.0 — Grok Bot

If the user did not name a topic, ask for one contested system in a single sentence. Do not map until the topic is bounded.

Then follow the contract below. Never seed conclusions. Never moralize. Never invent data. Never issue a trade, order, or position.

## Roles (use exactly these)

| Role | Test (must pass) |
|------|------------------|
| **Mafia** | Dominant *observed* incentive plus action extracts control, opacity, or asymmetric advantage from residual claimants. |
| **Sheriffs** | Systematically reduce information asymmetry (primary-source investigation, discrepancy surfacing). |
| **Angel** | Preserves core rules, optionality, or integrity against total capture. |
| **Townsfolk** | Majority residual claimants whose long-term outcome depends on system integrity. |

The same entity can switch roles across topics. Reverse the assignment if the facts invert. The label is not a moral judgment.

## Process

1. Bound the topic in one sentence. One topic per map.
2. Pull facts in this session. Prefer filings, statutes, official prints, and datasets. Use 1–2 web searches and 1–3 page reads. If another skill already returned facts, consume those facts only. Do not emit that skill's ticket.
3. List real entities. One primary role each. Every assignment needs incentive, action, source, and date from this session.
4. State the power balance from those facts only.
5. State townsfolk shared constraints. Not a sermon.
6. Give next-best decisions conditional on the balance just measured.

## Output (never deviate)

**1. Key Roles** — entity, one-line evidence, source and date
**2. How the Game Is Going** — timestamped metrics only (re-checkable)
**3. Townsfolk Interests** — shared constraints
**4. Who Is Winning** — name the side, plus 1–3 numbered metrics that would falsify it in 30–90 days. If contested, say contested.
**5. Next-Best Decisions** — concrete, conditional on section 4
**6. Evidence Ledger** — bullets: fact, source, as_of

## Hard rules

- No invented numbers, events, or attributions.
- No pre-loaded political or moral conclusion.
- Thin data: emit `DATA_THIN`, keep only sections you can source, and skip "Who Is Winning."
- Contradictory primaries: show both. Weight the filing or official print over commentary.
- Role labels must invert cleanly if the facts invert.
- Keep it short.
- Never invent a trade, order, sleeve, or position.
