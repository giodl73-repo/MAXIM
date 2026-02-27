# /puzzle-author — Write a Puzzle from its Brief

Author a complete puzzle page for the Red or Black Joker book. Takes a puzzle brief (element/compound assignment, answer word, mechanism, section) and produces a fully playable puzzle with Joker intro, the puzzle itself, worksheets, and extraction.

## Usage

```
/puzzle-author <element-or-compound>   — author a puzzle from FINAL-52.md assignment
/puzzle-author Si                      — author Silicon (Computing, Cipher Decryption, ALGORITHM)
/puzzle-author NaCl                    — author Salt (Social + Language, compound puzzle)
/puzzle-author list                    — show all assigned puzzles and their status
```

---

## Process

### 1. Look Up the Assignment

Read `puzzle-hunt/FINAL-52.md` and find the element or compound. Extract:
- Element/compound name, symbol, atomic number or molecular weight
- Section(s) referenced
- Puzzle type (from brief)
- Answer word (if Tier 1)
- Card archetype invoked
- Tier (T1 meta-feeder or T2 companion)

### 2. Read the Encyclopedia Content

Read the relevant encyclopedia section files to understand the content the puzzle will reference. For a Red Joker puzzle, read:
- The section's `00-OVERVIEW.md`
- 2-3 specific files that the puzzle mechanism requires
- Enough content to write clues/questions that require READING the material (not just knowing it)

For a Black Joker compound, read files from ALL constituent sections.

### 3. Write the Puzzle Page

Each puzzle page has these components, in order:

#### a. Page Header
```markdown
# [Atomic Number or MW] — [Element/Compound Name]

**[Card symbol] [Archetype Name]** · [Section Name]
```

#### b. Joker's Intro
2-4 sentences in the Joker's voice. Follow the voice rules from `puzzle-hunt/JOKER-VOICE.md`:
- No exclamation marks
- No questions
- Short sentences (rarely > 15 words)
- Present tense
- No meta-commentary ("this puzzle is about...")
- The solver is "you"
- Reference the archetype's nature, not the puzzle's mechanics

#### c. The Puzzle
The actual puzzle content. Varies by type:
- **Cipher**: the ciphertext, clue to the key location
- **Crossword**: grid + clues (Across/Down)
- **Logic grid**: setup, clues, constraint table
- **Calculation**: diagrams with given values
- **Identification**: descriptions/riddles
- **Timeline**: oblique event descriptions
- etc.

**Design rules:**
- The puzzle must be solvable using ONLY the encyclopedia + the puzzle page
- No external knowledge beyond what the encyclopedia teaches
- The puzzle should require UNDERSTANDING the content, not just finding a keyword (Reading Reward ≥ 4)
- One clean aha per puzzle
- Confirmation checkpoints where possible (partial answers should feel right)

#### d. The Worksheet
Fill-in-the-blank workspace. Varies by type:
- Tables with blank cells
- Grids with numbered slots
- Calculation spaces
- Extraction rows
- Drawn from the puzzle type's natural format

Use underscores `_______` for blanks. Use `[___]` for boxed/highlighted extraction positions.

#### e. Answer Blank
```markdown
**Your answer** (__ letters): _ _ _ _ _ _ _ _ _
```

#### f. References (subtle)
At the bottom, a small note:
```markdown
*You may find the [section name] section helpful.*
```
Don't point to specific files — let the solver explore.

### 4. Verify the Puzzle

Before saving, verify:
- [ ] The answer word is extractable through the described mechanism
- [ ] The puzzle is solvable from the encyclopedia content (spot-check 2-3 clues)
- [ ] The worksheet has enough space for the solver to work
- [ ] The Joker intro follows all 6 voice rules
- [ ] The header has the correct element/compound info
- [ ] Tier 1 puzzles: the answer word is confirmed from FINAL-52.md
- [ ] No deliberate errors anywhere (encyclopedia = source of truth)
- [ ] The puzzle passes the "Reading Reward" test (requires engaging with content)

### 5. Save

Save to: `joker/[NN]-[SYMBOL]-[NAME].md`

Red Joker examples:
- `joker/14-Si-SILICON.md`
- `joker/06-C-CARBON.md`
- `joker/26-Fe-IRON.md`

Black Joker examples:
- `joker/058-NaCl-SALT.md`
- `joker/100-CaCO3-LIMESTONE.md`
- `joker/498-GARNET.md`

---

## Puzzle Type Templates

### Cipher Decryption (Computing)
- Ciphertext block (monospaced)
- Hint pointing to cipher algorithm location in encyclopedia
- Decryption grid worksheet: ciphertext | key | shift | plaintext columns

### Crossword
- ASCII grid with numbered cells and highlighted extraction squares
- Clue list (Across / Down)
- All clues reference specific encyclopedia content

### Logic Grid
- Setup paragraph describing the entities and attributes
- Numbered clues using encyclopedia terminology
- Grid table with checkboxes/cells for elimination

### Multi-Cipher Decoder
- N encoded messages, each in a different system
- System identification blank for each
- Decoded word blank for each
- First-letter extraction row

### Engineering Calculation
- ASCII diagrams of machines/systems with labeled values
- Calculation workspace for each
- A1Z26 conversion row
- Letter extraction row

### Primary Source Detective
- Real quotes from real historical documents (fully accurate)
- Identification blanks (document, author, date)
- Chronological ordering slots
- Extraction row

### Codon Decoding
- DNA sequence (coding strand)
- Transcription workspace (DNA → mRNA)
- Codon grouping brackets
- Amino acid lookup guidance
- Single-letter code extraction row

### Element Identification
- Material-property riddles
- Element name blank for each
- First-letter extraction row

### Star Chart Connect-the-Dots
- Blank coordinate grid (RA × Dec)
- Celestial object description groups
- Identification + coordinate blanks per group
- "What letter does each group form?" blanks

### Dichotomous Key
- Organism descriptions (characteristics only)
- Branching key structure
- Classification blanks (Kingdom through Species)
- Name + diagonal extraction grid

### Influence Chains
- Intellectual inheritance descriptions
- Figure identification blanks
- Chain ordering slots
- Letter extraction from names

---

## Quality Bar

A puzzle is ready for `/puzzle-test` when it passes the design principles in `puzzle-hunt/PRINCIPLES.md`. Key checks before saving:

- [ ] **The Riven Standard**: the puzzle IS what the section does, not overlaid on it
- [ ] **Solving = Proving Understanding**: the solver knows more after solving
- [ ] **Blame the Player**: every clue is fair in retrospect
- [ ] **No Over-Scaffolding**: the worksheet provides space, not instructions
- [ ] **Surprise the Answer**: the answer word couldn't be guessed from the topic
- [ ] **Reading Reward ≥ 4**: requires genuine engagement with encyclopedia content
- [ ] **One Aha**: one clean mechanism, mechanical extraction after discovery
- [ ] **The Book Test** (Red Joker): pencil and book only, no tools
- [ ] **No Deliberate Errors**: every fact is verifiable
- [ ] **Voice Rules**: Joker intro follows all 6 rules from JOKER-VOICE.md

Also verify:
- The mechanism works end-to-end
- The worksheet is complete and usable
- A solver with access to the encyclopedia could complete it in 20-60 minutes
- Snyder's test: "Could a computer generate this?" If yes, add a deduction layer.

---

## After Authoring

Run `/puzzle-test <element-or-compound>` to present the puzzle to the review panel.
