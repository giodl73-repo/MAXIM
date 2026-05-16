---
wave: maxim-quality-control-spine
date_open: 2026-05-14
date_close: 2026-05-14
status: complete
source_request: "copy the wave/pulse/skills from route or apportionment; meld history/flair practice; build a plan for highest quality control"
---

# MAXIM Quality Control Spine

## Mission

Give MAXIM a durable execution rail for becoming the best stated reference on
the internet: perfect-enough ASCII, stronger explanations, stricter proof gates,
and an editorial system that can raise the rubric without losing the card/flair
history that gives the library its character.

## Claim Boundary

This wave may add wave/pulse skills, wave documents, proof/rubric plans, review
panels, and quality-dashboard designs. It must not bulk-transform content, rewrite
historical phases, or modify protected structural files unless a pulse names the
exact file and the edit is manually reviewed.

## Inputs

| Input | Source |
|---|---|
| Existing MAXIM review skill | `.claude/skills/reference-review/SKILL.md` |
| Existing atlas review/spec skills | `.claude/skills/atlas-cartography/SKILL.md`, `.claude/skills/atlas-review/SKILL.md` |
| Card/flair history protocol | `.claude/skills/honor/SKILL.md`, `HISTORY.md`, `cards/ROLES.md`, `cards/CONCEPTS.md` |
| Current proof configuration | `proof.toml` |
| Route wave model | `C:\src\route\.claude\skills\route-wave\SKILL.md`, `C:\src\route\docs\wave-execution.md` |
| Apportionment wave model | `C:\src\apportionment\.claude\skills\r-wave\SKILL.md`, `C:\src\apportionment\context\waves\PHASES.md` |

## Pulse Status

| Pulse | Status | Evidence |
|---|---|---|
| 01 - Wave/pulse skill import | DONE | MAXIM-native skills in `.claude/skills/maxim-*`, wave config, `context/waves/PHASES.md` |
| 02 - Gold Rubric v2 | DONE | `artifacts/GOLD-RUBRIC-V2.md` |
| 03 - Proof gate tightening plan | DONE | `artifacts/PROOF-GATE-TIGHTENING-PLAN.md`; proof tool unavailable in current env |
| 04 - ASCII perfection spec | DONE | `artifacts/ASCII-PERFECTION-SPEC.md` |
| 05 - History/flair closeout bridge | DONE | `artifacts/HISTORY-FLAIR-CLOSEOUT-BRIDGE.md` |
| 06 - Pilot gold audit | DONE | `panels/pilot-gold-audit/R1-consolidated.md` |

## Validation Gates

For documentation-only pulses:

```powershell
git diff --check
rg "@editor\[" C:\src\maxim --glob "*.md"
```

For proof/rubric pulses that modify validation behavior:

```powershell
python -m proof check
git diff --check
```

If `python -m proof check` is unavailable, record the exact tool error and run
focused checks against the touched files.

## Done Criteria

- MAXIM has its own wave, pulse, fork, review, and plan skills.
- The active wave has executable pulses for rubric, proof, ASCII, history/flair,
  and pilot audit work.
- The plan distinguishes mechanical proof from editorial judgment and expert
  adversarial review.
- No bulk content edits occur in this bootstrap wave.
- Wave closeout recommends, but does not automatically perform, a card/flair
  honor claim.

## Non-Goals

- No bulk guide rewrites.
- No broad line-removal or regex cleanup scripts.
- No automatic mutation of `HISTORY.md`, `cards/CONCEPTS.md`, or structural
  library files during bootstrap.
- No table/statistics proof platform unless a later pulse proves it is worth the
  complexity.

## Carry-Forwards

- Decide whether MAXIM wants a dedicated `.roles/` directory or whether review
  roles should remain embedded in skills.
- Decide whether `proof` should have separate `silver` and `gold` modes.
- Decide how to surface quality dashboards: root docs, generated artifact, or
  wave-local panel report.

## Closeout

| Metric | Result |
|---|---|
| Pulses completed | 6 / 6 |
| Backfilled waves created | 7 |
| Skills added | 5 |
| Quality artifacts added | 4 |
| Pilot guides audited | 5 |

See `CLOSE.md` for carry-forwards and honor recommendation.
