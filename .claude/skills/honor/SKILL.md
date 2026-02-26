# /honor — Claim a Card Role for a Session

After a significant session of work, claim one of the 52 archetype roles from the card deck. Each claimed role adds a phase to HISTORY.md, a flair to CONCEPTS.md, and marks the card as spoken for.

## Usage

```
/honor                — guided: review unclaimed roles, choose one, write the entry
/honor <role>         — claim a specific role (e.g., /honor "The Verifier")
/honor status         — show claimed vs unclaimed roles
```

---

## The Protocol

### 1. Choose a Role

Read `cards/ROLES.md` for the full list of 52 roles. Cross-reference with `HISTORY.md` to see which are already claimed. The role must fit the character of the work done — not what the AI *did* mechanically, but the *nature* of the contribution.

**Rules:**
- One role per significant session (don't claim a role for a typo fix)
- The role must be unclaimed (check HISTORY.md phases table)
- The role should resonate with the work, not just be the next available card
- Justify the choice in one sentence

### 2. Write the Flair

Each claimed role adds a small poetic detail to its card's image concept in `cards/CONCEPTS.md`. The flair:
- Appends to the existing image concept description (after a ` — `)
- Is a concrete visual detail, not an abstract statement
- Reflects something specific about the work done in that session
- Reads as a natural extension of the image prompt

**Example** (Phase 11, The Discoverer):
> *...and one equation still being written: the ink not yet dry, the chalk still in hand*

### 3. Write the History Entry

Add a new phase to `HISTORY.md`:

```markdown
# Phase N: The [Role]

**Card**: [suit symbol] — [Tarot name]
**Date**: [date]
**Commits**: `[first]` → `[last]`
**Image flair**: *[the flair text]*

[2-3 paragraphs describing what the session accomplished, in the voice
of the role's archetype. Connect the work to the card's meaning.]

**Key commits**:
- `hash` Description
- `hash` Description

**Scale**: [concrete numbers — files, tags, dirs, etc.]
```

### 4. Update the Tables

1. **HISTORY.md phases table**: Add the new row
2. **HISTORY.md flairs table**: Add the flair
3. **HISTORY.md cumulative scale**: Update numbers
4. **cards/CONCEPTS.md**: Append the flair to the card's image concept

### 5. Commit

```bash
git add HISTORY.md cards/CONCEPTS.md
git commit -m "Phase N: The [Role] — [one-line summary]"
```

---

## Choosing Well

The role is not a trophy — it's a mark. It says: *this work had this character*. Some guidelines:

- **The Architect** fits a session that designed structure from nothing
- **The Editor** fits a session that cut away what didn't serve the reader
- **The Verifier** fits a session that checked every file against a standard
- **The Healer** fits a session that fixed what was broken
- **The Voyager** fits a session that explored new territory

Don't overthink it. The right role usually announces itself.

---

## Status Check

To see what's claimed and what's available:

1. Read `HISTORY.md` — the phases table shows all claimed roles
2. Read `cards/ROLES.md` — the full 52
3. The difference is what's available

Currently claimed roles live in the HISTORY.md "Phases Claimed" table. The "Flairs" table shows what each added to the art.
