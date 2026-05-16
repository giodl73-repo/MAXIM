# History / Flair Closeout Bridge

## Purpose

MAXIM has two kinds of history:

| Layer | Source | Purpose |
|---|---|---|
| **Narrative / honor** | `HISTORY.md`, `cards/CONCEPTS.md`, `/honor` | card role, phase meaning, poetic flair |
| **Execution / wave** | `context/waves/**` | mission, pulses, gates, panels, carry-forwards |

The wave system should support `/honor`, not replace it.

## When A Wave Should Recommend `/honor`

Recommend an honor claim only when a wave has at least one of these:

| Trigger | Example |
|---|---|
| new durable capability | new proof mode, new review skill, new atlas pipeline |
| major quality transition | large tag burn-down, gold audit rollout, all diagrams validated |
| new project doctrine | Gold Rubric v2, answer protocol, publishing strategy |
| large authored artifact | new guide family, puzzle volume, atlas section |
| recovery / repair story | repo crash recovery, proof pipeline stabilization |

Do **not** recommend `/honor` for routine pulse completion, typo fixes, or small
metadata updates.

## Closeout Section Template

Add this section to `CLOSE.md` when a wave is significant:

```markdown
## Honor Recommendation

| Field | Value |
|---|---|
| Candidate role | The [Role] |
| Card | [card] |
| Why this role | [one sentence] |
| Flair seed | *...[concrete visual detail]* |
| Scale | [files, guides, tags, gates, agents, maps, etc.] |

This is a recommendation only. Run `/honor` separately to claim the card and
update `HISTORY.md` / `cards/CONCEPTS.md`.
```

## Backfilled Waves

Backfilled waves should:

- cite `source: git-history`;
- cite `history_phases` if matching phases exist;
- use "commit-derived pulses";
- avoid retroactive checkboxes;
- avoid claiming new flairs for old work.

## 52-Phase Goal

The wave system can help the library reach 52 phases without forcing it:

| Need | Wave Support |
|---|---|
| know what significant work happened | `WAVE.md`, `CLOSE.md`, pulse evidence |
| know whether it deserves a card | Honor recommendation section |
| avoid duplicate claims | `/honor status` against `HISTORY.md` |
| preserve execution detail without bloating history | wave pulses and panels |

The target remains: **52 eventual honored phases**, one per archetype role. Waves
are the workshop ledger; `HISTORY.md` is the illuminated manuscript.
