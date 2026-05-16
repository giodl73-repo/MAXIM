---
name: maxim-pulse
description: "Execute one MAXIM wave pulse end to end with scout, edits, documentation, and validation."
tags: [maxim, pulse, execute, quality, validation]
---

# maxim-pulse

Execute a pulse from the active MAXIM wave.

## Usage

```text
/maxim-pulse next
/maxim-pulse 02
```

## Procedure

1. Resolve the active wave from `context/waves/PHASES.md`.
2. If `next`, choose the first pulse with `status: todo`.
3. Read the pulse file completely.
4. Run every command in `Pre-implementation Scout`.
5. Implement deliverables using existing MAXIM patterns.
6. Update docs and the pulse checklist.
7. Update `WAVE.md` pulse table.
8. Run validation from the pulse.
9. Run `git diff --check`.

## Default MAXIM Validation

```powershell
git diff --check
python -m proof check
```

If `python -m proof check` is unavailable, record the exact failure and run the
focused validation commands named in the pulse instead.

## Completion Report

Report:

- pulse number and title
- files changed
- gates completed
- validation commands and result
- carry-forwards

## Rules

- Editorial tags are evidence, not embarrassment; do not remove an `@editor`
  tag unless the issue is actually fixed.
- A "clean" claim must name the gate that made it clean.
- ASCII/SVG quality changes must be viewed as rendered or checked by a proof
  rule before being called done.
- History/flair updates happen through `/honor` at wave close, not ad hoc.
