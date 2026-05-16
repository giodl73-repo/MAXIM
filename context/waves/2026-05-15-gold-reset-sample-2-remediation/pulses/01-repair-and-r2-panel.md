---
wave: gold-reset-sample-2-remediation
pulse: 01
date: 2026-05-15
status: done
depends_on: []
governing_roles:
  - reference-editor
  - ascii-cartographer
  - expert-skeptic
  - bridge-builder
  - index-weaver
---

# Pulse 01 - Repair and R2 Panel

## Mission

Repair the second three-guide Wave 37 sample and certify only after proof,
guide-specific scoring, adversarial closure, and reader-task checks agree.

## Scope Inventory

| Guide | Repair Focus |
|---|---|
| `games-history/06-DICE-GAMBLING.md` | Problem-of-Points factual slip and decision-table depth |
| `genomics/00-OVERVIEW.md` | Cloud/tool freshness and task-oriented method selection |
| `geography/04-BIOGEOGRAPHY.md` | Wallace Line framing, climate-debt caveat, decision-table depth, outward cross-links |

## Pre-Implementation Scout

```powershell
Get-Content context\waves\2026-05-15-gold-factory-wave-37\WAVE.md
Get-Content games-history\06-DICE-GAMBLING.md
Get-Content genomics\00-OVERVIEW.md
Get-Content geography\04-BIOGEOGRAPHY.md
Select-String -Path proof.toml -Pattern "gambling-mathematics-origin|genomics-landscape|biogeography-frameworks"
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml games-history\06-DICE-GAMBLING.md genomics\00-OVERVIEW.md geography\04-BIOGEOGRAPHY.md
```

## Deliverables Checklist

| Deliverable | Status |
|---|---|
| Repair `games-history/06-DICE-GAMBLING.md` | done |
| Repair `genomics/00-OVERVIEW.md` | done |
| Repair `geography/04-BIOGEOGRAPHY.md` | done |
| Write R2 panel evidence | done |
| Update Gold registry | done |

## Validation Gates

| Gate | Result |
|---|---|
| Proof with Da Vinci | PASS; output contained no `FAIL` |
| Diff hygiene | PASS |
| R2 panel | PASS |
| Registry decision | PASS; three repaired guides restored to Certified Gold |

