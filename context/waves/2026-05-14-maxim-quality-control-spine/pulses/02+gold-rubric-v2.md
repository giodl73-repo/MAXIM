---
wave: maxim-quality-control-spine
pulse: 02
date: 2026-05-14
status: done
depends_on: [01]
governing_roles: [reference-editor, expert-skeptic, bridge-builder, card-steward]
---

# Pulse 02 - Gold Rubric v2

## Mission

Raise the quality rubric from "style contract present" to "best-internet
reference quality" while preserving the existing `@editor` workflow.

## Pre-implementation Scout

```powershell
rg "Style Contract|Review Rubric|Quality Bar|SCORECARD" C:\src\maxim --glob "*.md"
```

## Deliverables

- [x] Define Gold/Silver/Bronze guide tiers.
- [x] Add scoring dimensions for landscape power, layering integrity, ASCII
      precision, explanatory compression, decision utility, confusion handling,
      bridge quality, cross-reference value, voice, and factual confidence.
- [x] Map new scores to existing `@editor` tag types instead of inventing a
      second issue system.
- [x] Define what a BLOCK/WARN/NOTE means under the raised bar.
- [x] Decide where the rubric lives before editing structural docs.

## Evidence

- `artifacts/GOLD-RUBRIC-V2.md`

## Validation

```powershell
git diff --check
```

## Non-Goals

- Do not rescore all 52 volumes in this pulse.
- Do not modify `SCORECARD.md` until the rubric location is decided.
