---
wave: maxim-quality-control-spine
pulse: 03
date: 2026-05-14
status: done
depends_on: [02]
governing_roles: [ascii-cartographer, reference-editor]
---

# Pulse 03 - Proof Gate Tightening Plan

## Mission

Turn `proof.toml` from a gross-failure checker into a staged quality gate without
breaking the existing library in one move.

## Pre-implementation Scout

```powershell
Get-Content C:\src\maxim\proof.toml
python -m proof check
```

## Deliverables

- [x] Inventory current leniencies: ASCII tolerance, disabled column separators,
      required sections, table checks, and editor-tag severity.
- [x] Propose staged modes: baseline, silver, gold.
- [x] Define mechanical rules that can become errors safely.
- [x] Define rules that must remain warnings until false positives are measured.
- [x] Identify a gold pilot set of guides for stricter checks.

## Evidence

- `artifacts/PROOF-GATE-TIGHTENING-PLAN.md`
- `python -m proof check` currently blocked: `No module named proof`

## Validation

```powershell
python -m proof check
git diff --check
```

## Non-Goals

- Do not tighten global proof rules until the pilot set is known.
- Do not add broad table/statistics validation unless the pilot proves value.
