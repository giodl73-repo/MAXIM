# The Concept Index Mechanism — Numbers That Are Addresses

A puzzle mechanism that uses the Concept Index (`CONCEPT-INDEX.md`) as a hidden lookup table. The puzzle presents only numbers. The solver must discover that the numbers are section references, and that the Concept Index maps which concepts span which sections.

---

## How It Works

### The puzzle presents rows of numbers:

```
 2   5   8
 1   4   7  13
 3   6   9
 1   5  10  12
 4   8  11
```

No title beyond the compound's molecular weight. No instructions. Just numbers.

### The solver's aha cascade:

1. **"Just numbers."** Small integers. Meaningless.
2. **"They're all between 1 and 13."** Thirteen sections in the library.
3. **"Each row might be a set of section numbers."** Sections 2, 5, 8 — what do those have in common?
4. **"What concept appears in exactly those sections?"** The solver searches — and discovers the Concept Index, the encyclopedia's cross-reference map.
5. **"SYMMETRY appears in sections 2, 5, and 8."** (Or whatever concept matches.) The concept name gives a letter.
6. **Five rows → five concepts → five letters → answer word.**

### The confirmation:

Each row uniquely identifies ONE concept in the Index. If the solver picks the wrong concept, it won't appear in exactly those sections. The section-number pattern IS the fingerprint.

### The "don't be too obvious" principle:

- The puzzle NEVER mentions the Concept Index
- The puzzle NEVER says "look at sections"
- The numbers are just numbers until the solver connects them
- A solver who already knows the Index exists will solve faster — but the puzzle doesn't require prior knowledge, just discovery

---

## Why This Fixes the Black Joker

Snyder's Round 3 critique: "15 of 26 compound puzzles are 'just combine two topics' — no mechanism, no solve path."

The Concept Index mechanism gives every compound puzzle a SPECIFIC, VERIFIABLE mechanism:
- Each compound puzzle presents numbered rows
- Each row points to a real concept in the Index
- The concept names extract to the answer
- The mechanism is identical across compounds (consistent) but the specific concepts are different (varied)
- The solver must UNDERSTAND cross-section connections to identify the concepts

This turns "combine Mechanics and History" from a vague prompt into a concrete puzzle: "find the concept that appears in both Mechanics files AND History files, and only in those."

---

## Variants

### Basic: Section numbers only
```
2  5  8
```
"Which concept spans sections 2, 5, and 8?"

### Advanced: Section + file numbers
```
2/03  5/07  8/01
```
"Which concept appears in section 2 file 3, section 5 file 7, and section 8 file 1?"
This is more precise (fewer false matches) but reveals the mechanism faster.

### Encoded: Just the file numbers, section implied by compound
Since each compound combines specific sections, the solver already knows WHICH sections. The numbers are just file numbers within those sections.

For compound NaCl (Social Sciences + Language):
```
3  7
1  4
6  2
```
Row 1: Social file 3 + Language file 7 → concept that appears in both
Row 2: Social file 1 + Language file 4 → another concept
Etc.

### Steganographic: Numbers hidden in compound puzzle content
The numbers don't appear as a grid — they're woven into the puzzle's narrative or clues. The solver has to extract the numbers first, THEN realize they're Index references.

---

## Integration with Current Compounds

The 15 "shallow" compounds identified by Snyder could each use this mechanism with section-specific variations:

| MW | Compound | Sections | Concept Index rows point to... |
|----|----------|----------|-------------------------------|
| 40 | MgO (Magnesia) | Tech + Earth | Concepts spanning both |
| 41 | AlN | Natural + Language | Concepts spanning both |
| 80 | TiO₂ | Tech + Earth | Concepts spanning both |
| 88 | FeS (Troilite) | Mech + History | Concepts spanning both |
| 96 | CuS (Covellite) | Material + History | Concepts spanning both |
| 97 | ZnS (Sphalerite) | Natural + History | Concepts spanning both |
| 106 | Na₂CO₃ (Soda Ash) | Social + Life + Earth | 3-section concepts |
| 115 | NaOH (Lye) | Social + Earth | Concepts spanning both |
| 120 | FeS₂ (Pyrite) | Mech + History | (Pyrite duplicates Troilite — replace or differentiate) |
| 136 | CaSO₄ (Gypsum) | Earth + History | Concepts spanning both |
| 151 | SnO₂ (Cassiterite) | Material + Earth | Concepts spanning both |
| 160 | Fe₂O₃ (Hematite) | Mech + Earth | Concepts spanning both |
| 198 | As₂O₃ (Arsenic) | History + Earth | Concepts spanning both |
| 239 | PbS (Galena) | Math + History | Concepts spanning both |
| 267 | PbCO₃ (Cerussite) | Math + Life + Earth | 3-section concepts |

The 7 "named" synthesis puzzles (The Debate, The Chain, etc.) keep their richer narrative mechanisms. The 15 simpler compounds get the Index mechanism — consistent, verifiable, deeply tied to the library's own structure.

---

## The Meta Implication

If the solver discovers the Concept Index through this mechanism, they now possess the library's CONNECTION MAP. This changes how they see everything:

- "Wait — 'entropy' appears in physics, information theory, AND chemistry?"
- "Symmetry shows up in 8 different sections?"
- The encyclopedia stops being 13 shelves and becomes one web

That realization — seeing the connections — is the Black Joker's thesis. The Concept Index mechanism doesn't just solve a puzzle. It delivers the hunt's message.

---

## Verification Requirement

Before committing to this mechanism, verify:
- [ ] The Concept Index has enough entries with unique section-number patterns
- [ ] No two concepts share the exact same set of sections (if they do, add file numbers for disambiguation)
- [ ] The concepts identified by each compound's rows produce extractable answer letters
- [ ] The Index is discoverable by a solver who doesn't know it exists (is it in mkdocs navigation? Can it be found by browsing?)
