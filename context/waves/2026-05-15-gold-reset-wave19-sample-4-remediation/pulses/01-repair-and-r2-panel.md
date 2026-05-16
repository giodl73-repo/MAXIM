---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `journalism/05-INVESTIGATIVE.md`
- `journalism/06-PRESS-FREEDOM.md`
- `journalism/07-PHOTOJOURNALISM.md`
- `journalism/08-BROADCAST.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
situation/standard selector tables. Current Certified Gold requires diagnostic
reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `journalism/05-INVESTIGATIVE.md` | Rebuilt the investigative table around tips, whistleblowers, FOIA denial, legal threats, denials, private individuals, cross-border work, and evidence control. |
| `journalism/06-PRESS-FREEDOM.md` | Rebuilt the press-freedom table around prior restraint, subpoenas, SLAPP suits, authoritarian reporting, Espionage Act risk, protest arrest, defamation, and statistics. |
| `journalism/07-PHOTOJOURNALISM.md` | Rebuilt the photojournalism table around decisive moments, staging, digital edits, captions, archival reuse, war-zone images, AI images, contest integrity, and juveniles. |
| `journalism/08-BROADCAST.md` | Rebuilt the broadcast table around unconfirmed news, live shots, lower thirds, chyrons, sound bites, speculation, re-enactment, podcasts, and ratings pressure. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- journalism\05-INVESTIGATIVE.md journalism\06-PRESS-FREEDOM.md journalism\07-PHOTOJOURNALISM.md journalism\08-BROADCAST.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml journalism\05-INVESTIGATIVE.md journalism\06-PRESS-FREEDOM.md journalism\07-PHOTOJOURNALISM.md journalism\08-BROADCAST.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

