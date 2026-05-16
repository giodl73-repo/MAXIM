---
wave: proof-scope-hygiene
date_open: 2026-05-14
date_close: 2026-05-14
status: complete
source_wave: maxim-quality-control-spine
---

# Proof Scope Hygiene

## Mission

Keep guide proof focused on guide content after adding wave and skill metadata to
the repository.

## Pulse Status

| Pulse | Status | Evidence |
|---|---|---|
| 01 - Live tag baseline | DONE | Content-guide search found no live `@editor[` tags outside process docs/examples |
| 02 - Exclude process docs | DONE | `proof.toml` excludes `.claude/**` and `context/**` from content-guide proof |

## Validation

```powershell
git diff --check
C:\src\proof\target\debug\proof.exe check -e --no-fail proof.toml
```

## Closeout

This prevents future process artifacts from polluting content proof gates while
preserving targeted proof of individual wave files when needed.
