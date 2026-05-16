---
name: maxim-wave
description: "Manage MAXIM waves in context/waves: find the active quality wave, show status, advance pulses, and close waves."
tags: [maxim, wave, quality, execution, planning]
---

# maxim-wave

Use this skill when the user asks for a wave, quality-control rail, next stage,
roadmap, milestone execution, or to continue from the active MAXIM wave.

## Source Of Truth

- Wave index: `context/waves/PHASES.md`
- Active wave: first row with `status: active`
- Active wave card: `context/waves/{active}/WAVE.md`
- Pulse plans: `context/waves/{active}/pulses/`
- Fork contexts: `context/waves/{active}/forks/`
- Review panels: `context/waves/{active}/panels/`
- Historical phase/flair record: `HISTORY.md` and `cards/CONCEPTS.md`

## Status Procedure

1. Read `context/waves/PHASES.md`.
2. Resolve the first `active` wave directory.
3. Read `context/waves/{active}/WAVE.md`.
4. List pulses in order.
5. Report:
   - active wave
   - completed pulses
   - next `status: todo` pulse
   - validation gates
   - known carry-forwards

## Next Procedure

1. Resolve the next `todo` pulse unless the user names a pulse.
2. Read the pulse completely.
3. Run the pulse's pre-implementation scout commands.
4. Implement the deliverables using existing MAXIM conventions.
5. Update documentation and pulse checkboxes.
6. Update `WAVE.md` pulse status.
7. Run validation commands from the pulse.
8. Report files changed, gates run, and carry-forwards.

## Close Procedure

Close only when every pulse in `WAVE.md` is done or explicitly deferred:

1. Write `CLOSE.md`.
2. Update `context/waves/PHASES.md` status.
3. If the work was significant, run `/honor` to claim a card role and write the
   phase/flair into `HISTORY.md` and `cards/CONCEPTS.md`.
4. Run final validation.
5. Commit with a concise project-style message.

## Rules

- A wave is an execution rail, not a public milestone.
- A pulse is the smallest committable quality improvement unit.
- Do not mark a pulse done unless its validation ran or the blocker is written.
- Do not delete or rewrite historical phases; bridge them from wave close notes.
- Keep old wave directories as history.
