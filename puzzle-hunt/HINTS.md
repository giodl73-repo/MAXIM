# Hints — Hint System Design

Optional. Some hunts have no hints (MIT Mystery Hunt tradition). Others have structured hint systems. Design yours here.

---

## Hint Philosophy

Choose one:

| Philosophy | Description | Best for |
|-----------|-------------|----------|
| **No hints** | The hunt is fair. Every clue is in the puzzle. | Expert teams, competitive hunts |
| **Timed hints** | Hints unlock after N minutes of puzzle access | Solo solvers, accessibility |
| **Request-based** | Solver requests a hint, loses points or time | Competitive with mercy |
| **Layered** | 3 hint levels per puzzle (nudge → push → shove) | Casual audience, museum-style |
| **Confirmation only** | No hints, but solver can check if answer is correct | Moderate — rewards persistence |
| **Partial confirmation** | Groups of 3 confirmed together (Obra Dinn Rule of Three) | Deduction-heavy hunts |

**Your choice:** ____________

---

## Hint Tiers (if using layered hints)

### Tier 1: Nudge
Points the solver in the right direction without revealing mechanism or answer.
> "Have you looked at the section on [topic]?"
> "The numbers in this puzzle are not arbitrary."

### Tier 2: Push
Reveals the mechanism but not the answer.
> "Each encoding system is taught in the codes/ directory."
> "The first letters of the decoded words matter."

### Tier 3: Shove
Gives the answer pathway but still requires the solver to execute.
> "Decode using Morse code. The answer starts with I."

---

## Per-Puzzle Hints

Fill in as puzzles are authored. Each puzzle gets up to 3 hints.

| Puzzle ID | Nudge | Push | Shove |
|-----------|-------|------|-------|
| | | | |
| | | | |
| | | | |

---

## Confirmation Mechanism

How does a solver know their answer is correct?

| Mechanism | How it works | Pros | Cons |
|-----------|-------------|------|------|
| **Crossword crossings** | Two answers share a letter in the meta grid — if both are right, the crossing matches | Built-in, elegant | Requires meta grid |
| **Answer checker** | Submit answer to a verification system (hash, API, physical) | Instant feedback | Needs infrastructure |
| **Rule of Three** | 3 correct answers confirmed simultaneously (Obra Dinn style) | Anti-brute-force | Delayed gratification |
| **Self-confirming** | The answer word relates to the puzzle in a way that confirms correctness | No infrastructure | Subjective |
| **Word length** | Puzzle page states answer length — wrong length = wrong answer | Simple | Weak confirmation |
| **None** | The solver proceeds on faith until the meta | Maximum tension | May cause frustration |

**Your choice:** ____________

---

## Meta Hints

Should the meta have hints? Usually no — the meta IS the final challenge. But for accessibility:

| Meta | Hint available? | Hint content |
|------|----------------|-------------|
| Round 1 meta | | |
| Round 2 meta | | |
| Super-meta | | |

---

## Hint Delivery

How are hints delivered?

| Method | Description |
|--------|-------------|
| **In-book** | Printed in the back of the book, sealed or encoded |
| **Website** | Unlockable on a companion site |
| **QR code** | Each puzzle has a QR code linking to its hints |
| **Physical** | Sealed envelopes, scratch-off panels |
| **On request** | Email/message the hunt organizer |
| **None** | No delivery mechanism — no hints exist |

**Your choice:** ____________
