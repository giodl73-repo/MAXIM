---
wave: gold-registry
date_open: 2026-05-14
date_close: 2026-05-14
status: complete
source_wave: maxim-quality-control-spine
---

# Gold Registry

## Mission

Create a durable registry for Gold claims so certification does not live only in
individual wave closeouts.

## Pulse Status

| Pulse | Status | Evidence |
|---|---|---|
| 01 - Certified Gold list | DONE | `context/gold/REGISTRY.md` lists Package and Consensus as certified Gold |
| 02 - Candidate list | DONE | Registry records Atlas, Hydrogen, and Pitch as candidates with next gates |
| 03 - Invariant inventory | DONE | Registry mirrors current Da Vinci IDs and protected URIs |
| 04 - Promotion protocol | DONE | Registry defines evidence required before adding future Gold claims |
| 05 - Review skill hook | DONE | `/reference-review` now names the registry and update rules |

## Validation

```powershell
git diff --check
C:\src\proof\target\debug\proof.exe check -e --no-fail context\gold\REGISTRY.md
```

## Closeout

Gold is now a tracked status, not an adjective. Future waves can add candidates,
promote guides, or record regressions without rewriting the pilot history.
