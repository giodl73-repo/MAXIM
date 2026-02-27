# Round 2 Review: Puzzle Pool (89 Candidates)

**Reviewer**: Wei-Hwa Huang (simulated)
**Lens**: Deductive rigor and solve-path quality
**Date**: 2026-02-26
**Input**: PUZZLE-POOL.md (89 briefs), TWO-JOKERS.md (two-book structure)

---

## Preamble

My Round 1 review evaluated a steganographic design where 13 puzzles were hidden inside the encyclopedia itself. That design had deep problems: most "puzzles" were encodings (A1Z26, mod arithmetic, date-sort acrostics). The move to an explicit companion book (Red Joker) with worksheets, named puzzles, and section pointers fundamentally changes the design space. Good. An explicit puzzle book can afford richer mechanisms because the solver knows they are solving -- no steganographic camouflage tax.

The pool contains 89 candidates. The task: select the best 13 for the Red Joker (one per section), evaluating each on deductive rigor. I will evaluate every candidate in every section, then name my ideal 13.

My four criteria for each candidate:

| Criterion | Scale | What it measures |
|-----------|-------|------------------|
| **Solution standout** | 1-5 | Does the intended answer emerge uniquely from the mechanism? |
| **Brute-force resistance** | Flag | Can a solver shortcut the intended path? |
| **Deductive path** | 1-5 | Is there a clean chain of reasoning from puzzle to answer? |
| **Confirmation checkpoints** | Yes/No | Can the solver verify progress before finishing? |

---

## K — Computing & Software

### K1 -- Cipher Decryption (current pick)

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | Minor flag -- if the cipher is a simple Caesar, frequency analysis shortcuts it |
| Deductive path | 4 |
| Checkpoints | Yes -- plaintext emerges incrementally |

**Analysis.** This is a massive improvement over the V2 indexed-extraction. The solver learns a cipher from `cryptography/`, finds the key in `computing/25-SECURITY.md`, and decrypts. The two-source structure (learn method from one file, find key in another) creates a genuine two-step deduction: (1) identify the cipher, (2) locate the key. Decryption with the correct key is then mechanical, which is fine -- the deduction IS the cipher identification and key-finding.

**Concern.** "Finds the key in computing/25-SECURITY.md" is vague. If the key is a number embedded in the text, the solver might try all plausible numbers (brute-force). The key needs to be extractable only by understanding the content -- e.g., the key is a specific algorithm's block size, or a protocol's default port, something that requires *reading* to identify. If the key is just "the number 13 appears on page 4," that is a scavenger hunt, not deduction.

**Verdict: Strong pick.** Ensure the key requires domain comprehension, not just text scanning.

---

### K2 -- Algorithm Execution

| Criterion | Score |
|-----------|-------|
| Solution standout | 5 |
| Brute-forceable? | No -- must trace correctly |
| Deductive path | 5 |
| Checkpoints | Yes -- each execution step produces verifiable state |

**Analysis.** This is the puzzle I asked for in Round 1. "Execute pseudocode by hand -- the output IS the answer." The solver traces a program: loops, conditionals, string operations. Each step is deterministic. The output is unique. There is no ambiguity about what the answer is -- you either trace correctly or you don't.

This is a *genuine puzzle* by my definition: artificially created, one intended solution, solvable through legitimate deduction (here: mechanical execution, which is a form of deduction). The execution trace table provides continuous confirmation -- at every step, the solver can verify their variable state is consistent.

**Concern.** The pseudocode must reference computing concepts (the brief says it does), which ties the solve to reading the encyclopedia. If the pseudocode is self-contained, the solver never opens a reference volume, which defeats the Red Joker's purpose.

**Verdict: Excellent.** This is a top-tier candidate. Would unseat K1 if the pseudocode genuinely requires encyclopedia knowledge.

---

### K3 -- State Machine Traversal

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | Minor flag -- small state machines can be exhaustively traced |
| Deductive path | 4 |
| Checkpoints | Yes -- each transition yields a letter |

**Analysis.** Follow a state diagram where transitions have conditions requiring content knowledge. Valid path collects letters. This is clean: the solver must evaluate conditions (deduction), choose transitions (constrained choice), and collect letters (extraction). The path is unique if conditions are deterministic.

**Concern.** If the state machine is small (5-6 states), a solver can trace all paths and check which one spells a word. Anti-guessing requires either a large state machine or conditions that cannot be evaluated without reading. Prefer the latter.

**Verdict: Solid.** Slightly below K2 because the state-machine format is less inherently tied to Computing content.

---

### K4 -- Stack Trace / Recursion

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | No |
| Deductive path | 4 |
| Checkpoints | Yes -- each return value is independently checkable |

**Analysis.** Trace a recursive function; return values at each level encode letters. This is structurally similar to K2 (execute code, get output) but specifically tests recursion understanding. The call stack diagram is a natural worksheet. Return values mapping to letters is a clean extraction if the mapping is given (e.g., "return values are ASCII codes" or "return values are A1Z26").

**Concern.** If the mapping from return values to letters is A1Z26, I flag this -- A1Z26 is puzzle-mechanical, not thematic. If the function itself produces characters (string operations), that is much cleaner.

**Verdict: Good.** Slightly redundant with K2 -- both are "execute code, read output." Pick one.

---

### K5 -- Binary Decoder

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | Yes -- just try ASCII conversion on any binary string |
| Deductive path | 2 |
| Checkpoints | Yes -- each byte decodes independently |

**Analysis.** An ASCII art image made of 0s and 1s. Decode the binary to ASCII text. This is an encoding, not a puzzle. The solver sees binary, tries ASCII conversion, gets the answer. There is no deductive step beyond "this is binary." Any experienced puzzle solver will try binary-to-ASCII within 30 seconds.

**Verdict: Weak.** The mechanism is the first thing anyone tries. No selection for the K slot.

---

### K Section Ranking

1. **K2 -- Algorithm Execution** (if pseudocode requires encyclopedia)
2. **K1 -- Cipher Decryption** (current pick, solid)
3. **K3 -- State Machine Traversal**
4. **K4 -- Stack Trace / Recursion**
5. K5 -- Binary Decoder (reject)

**My pick: K2** if executable; **K1** as safe fallback.

---

## Q — Arts & Culture

### Q1 -- Crossword (V2 design)

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Partially -- crossword grids constrain answers, solvers can guess from crosses |
| Deductive path | 3 |
| Checkpoints | Yes -- crossing letters confirm |

**Analysis.** A standard crossword with arts clues and highlighted cells. Crosswords are well-understood puzzle forms with built-in confirmation (crossing letters). But this is the most generic possible format. It does not do anything specific to the Arts section -- any section could have a crossword.

**Verdict: Acceptable floor, not inspired.**

---

### Q2 -- Visual Rebus

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Moderate -- rebuses can be guessed from partial information |
| Deductive path | 3 |
| Checkpoints | Yes -- each rebus is independently solvable |

**Analysis.** Visual word puzzles representing arts concepts. Each solved rebus is an arts term; extracted letters spell the answer. The rebuses provide individual confirmation checkpoints (each one resolves independently). But rebus interpretation is inherently subjective -- "is this PERSPECTIVE or VANISHING POINT?" Multiple valid readings of a visual arrangement undermine solution standout.

**Concern.** Rebuses are notoriously ambiguous. Without extremely tight visual design, the solver faces multiple plausible interpretations at each step. This violates my core principle: the intended solution must stand out.

**Verdict: Risky.** Execution-dependent. Could be great or could be an ambiguity nightmare.

---

### Q3 -- Musical Staff Decoder

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | No -- must read the notation correctly |
| Deductive path | 4 |
| Checkpoints | Yes -- each note is independently readable |

**Analysis.** A musical staff where note names (CDEFGAB) spell a message. This is clean: the notation is deterministic, the mapping is standard (not invented), and the solver must learn to read music from `music-theory/`. The constraint is that the answer can only use letters A-G, which severely limits answer words. The brief says "the melody gives the answer or a cluephrase."

**Concern.** The CDEFGAB alphabet is brutally restrictive. Only 7 of 26 letters. The answer PERSPECTIVE contains P, R, S, T, I -- none of which are note names. This means the musical staff cannot directly spell the answer word. It must spell a cluephrase using only A-G letters, which will be tortured ("A BAD FACE" = "ABADFACE"?). Cluephrases from 7 letters are ugly.

The deeper problem: if the puzzle produces a cluephrase rather than the answer word, there is an interpretation gap between cluephrase and answer. That gap is a guessing opportunity.

**Verdict: Mechanically clean but alphabet-constrained to the point of impracticality.** Would need a redesigned answer word that lives within {A,B,C,D,E,F,G}.

---

### Q4 -- Color Overlay

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | No -- must physically perform the overlay |
| Deductive path | 2 |
| Checkpoints | No -- the word either appears or it doesn't |

**Analysis.** Hold two pages together against light; overlap reveals letters. This is a *reveal mechanism*, not a deductive puzzle. The solver does one physical action and either sees the word or doesn't. There is no chain of reasoning. The "puzzle" is knowing to hold the pages together, which is told to you (in an explicit puzzle book) or discovered by one insight.

**Concern.** Once you know to overlay the pages, there is zero deduction. The answer is revealed, not derived. This is a magic trick, not a puzzle.

**Verdict: Spectacle, not puzzle.** Might serve the Black Joker as a wow moment, but fails my deductive-path criterion for the Red Joker.

---

### Q5 -- Anamorphic Drawing

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | No |
| Deductive path | 2 |
| Checkpoints | No -- you either see the word or you don't |

**Analysis.** Same structural problem as Q4. One physical action (tilt the book) reveals the answer. No deductive chain. The connection to art history (Holbein's skull) is lovely thematically, but the *solve* is "tilt and read." That is perception, not deduction.

**Verdict: Thematically excellent, deductively empty.**

---

### Q6 -- Golden Ratio Composition

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Moderate -- once you know the ratio, measurement is mechanical |
| Deductive path | 3 |
| Checkpoints | Partial -- early measurements can confirm the ratio |

**Analysis.** Measure an artwork, recognize the golden ratio, use it to decode positions. This has more deductive steps than Q4/Q5: (1) measure distances, (2) recognize the ratio, (3) apply it as a key. Step 2 is a genuine aha. But step 3 ("letters at golden-ratio intervals") is underspecified. What intervals? Intervals of what? If the instruction is "take every phi-th character," that is not well-defined for irrational numbers.

**Concern.** Physical measurement introduces error. Ruler measurements on a printed page are imprecise. If the decoding requires distinguishing 1.618 from 1.6 or 1.62, measurement noise will produce wrong answers. Puzzles that require precise physical measurement on a printed page are fundamentally fragile.

**Verdict: Interesting concept, fragile execution.** Measurement precision is an anti-deduction problem.

---

### Q7 -- Fibonacci Art Sequence

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | Yes -- Fibonacci sequence is recognizable on sight |
| Deductive path | 2 |
| Checkpoints | No |

**Analysis.** The number of elements follows 1,1,2,3,5,8. But what does the solver DO with this observation? "Mapped to letters or used as indices" -- the brief doesn't know. When the brief itself can't specify the extraction, that is a sign the mechanism is an observation without a puzzle attached.

**Verdict: An observation, not a puzzle.** Recognizing Fibonacci is one aha; converting it to an answer requires an unspecified second mechanism.

---

### Q Section Ranking

1. **Q3 -- Musical Staff Decoder** (if alphabet constraint can be solved)
2. **Q1 -- Crossword** (safe, well-understood)
3. **Q2 -- Visual Rebus** (if ambiguity is controlled)
4. Q6 -- Golden Ratio (fragile)
5. Q4 -- Color Overlay (spectacle, not puzzle)
6. Q5 -- Anamorphic Drawing (perception, not deduction)
7. Q7 -- Fibonacci (observation without extraction)

**My pick: Q1 (Crossword)** as the safest choice with built-in deductive confirmation. Q3 if the answer word can be redesigned. Neither is championship quality. The Arts slot is the weakest in the pool.

---

## J — Mathematics & Physics

### J1 -- Proof Completion (current pick)

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | Moderate -- if blanks are fill-in-the-term, a math-literate solver may guess |
| Deductive path | 4 |
| Checkpoints | Yes -- each blank is independently verifiable within the proof |

**Analysis.** A proof chain with blanks. Each blank requires a specific mathematical concept. First letters of missing terms spell SYMMETRY. This is a strong format: the proof provides internal consistency checks (each step must follow from the previous), which means the solver can verify each blank against the logical flow. The extraction (first letters) is standard but justified by the worksheet format.

**Concern.** "First letters of missing terms" means the constructor must find 8 mathematical terms starting with S-Y-M-M-E-T-R-Y. Double-M is hard. What mathematical term starts with Y? "Y-axis"? That is weak. The answer word constrains the term selection, which may force unnatural choices. Unnatural terms in a proof break the proof's internal logic, which is the puzzle's primary confirmation mechanism.

**Anti-guessing.** A math-literate solver who recognizes the proof's topic may fill blanks from domain knowledge without reading the encyclopedia. If the proof is about group theory and the blanks are standard group-theory terms, a mathematician solves this without the book. This defeats the Red Joker's pedagogical purpose.

**Verdict: Good structure, constrained by answer word.** The proof must be unusual enough that the terms are not guessable from general mathematical knowledge.

---

### J2 -- Symmetry Operations

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | No -- must apply transformations correctly |
| Deductive path | 4 |
| Checkpoints | Partial -- each transformation can be verified against the group axioms |

**Analysis.** Apply group theory transformations (rotation, reflection, translation) to a letter grid. Transformed grids, overlaid, reveal the answer. This is mathematically rigorous: group operations are deterministic, composable, and verifiable. The solver must understand the operations (from `mathematics/`) and apply them precisely. The overlay step is a clean reveal.

**Concern.** "Overlaid" is physically ambiguous. Do you stack transparencies? Do you AND the letter positions? Do you XOR? The overlay rule must be specified precisely. If it is "letters that appear in the same position across all transformations," that is well-defined. If it is "the visual composite," that is subjective.

**Verdict: Mathematically clean if the overlay rule is specified.** Strong candidate.

---

### J3 -- Geometric Construction

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | No |
| Deductive path | 3 |
| Checkpoints | Partial -- each construction produces a visible shape |

**Analysis.** Compass-and-straightedge constructions that form letter shapes. 8 constructions produce 8 letters. The constructions themselves are deterministic (classical geometry). But the extraction -- "the construction forms a letter shape" -- is perceptual, not deductive. Does this arc look like an S or a 5? Is that a T or a cross? Letter-shape recognition from geometric constructions is inherently ambiguous.

**Physical concern.** Requires compass and straightedge (or improvisation). Physical construction introduces error. A slightly wrong compass radius produces a slightly wrong arc, which may not resemble the intended letter.

**Verdict: Beautiful concept, perceptual ambiguity in extraction.** The constructions-to-letters step is the weak link.

---

### J4 -- Matrix Multiplication

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | No -- must compute correctly |
| Deductive path | 3 |
| Checkpoints | Yes -- each multiplication is independently verifiable |

**Analysis.** Multiply matrices, decode results to letters. Mechanically clean: matrix multiplication is deterministic. But the decoding step ("mod 26, or specific cell positions") is underspecified and arbitrary. If it is mod 26, I flag it for the same reason as in Round 1 -- modular arithmetic is puzzle-mechanical, not mathematically motivated. If it is "read a specific cell," which cell? The choice of cell is an arbitrary convention, not a deduction.

**Verdict: Deterministic computation with arbitrary extraction.** The math is real; the letter-extraction is bolted on.

---

### J5 -- Equation Balancing

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Moderate -- algebraic equations have unique solutions, but the letter-mapping step is guessable |
| Deductive path | 3 |
| Checkpoints | Yes -- each equation is independently solvable |

**Analysis.** Physics/chemistry equations with unknowns as letters. Solve for unknowns; unknowns spell the answer. The concept is elegant: the unknowns ARE the answer letters, and solving the equation IS the deduction. But the equations must be carefully constructed so that each unknown has a unique solution AND that solution maps cleanly to a letter. If the unknown is a physical quantity (e.g., force = 13 Newtons), the mapping to a letter (13 = M via A1Z26) is again arbitrary.

If instead the unknowns are literally letters used as algebraic variables (F, O, R, C, E) and the equations constrain their numerical values such that each letter-variable has exactly one consistent assignment, this becomes a cryptarithmetic puzzle. THAT would be championship quality.

**Verdict: Depends entirely on execution.** Cryptarithmetic variant = excellent. "Solve equation, apply A1Z26" = mediocre.

---

### J6 -- Topology Puzzle

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | Yes -- genus counting is straightforward once you know the concept |
| Deductive path | 2 |
| Checkpoints | Yes -- each shape is independently classifiable |

**Analysis.** Classify shapes by genus, map genus numbers to letters via A1Z26. This is counting + A1Z26 -- the same mechanism I condemned in Round 1 for Technology. Genus is a richer concept than bullet counts, but the extraction is identical: count holes, convert to letter. There is no topological reasoning beyond counting.

**Anti-guessing.** Genus values are small integers (0-3 for most reasonable shapes). A1Z26 maps these to A, B, C, D. The answer word is constrained to letters A-D, which is absurdly restrictive. Either the answer must use only the first few letters of the alphabet (impossible for any natural word), or the genus values must be larger (requiring bizarre high-genus surfaces that strain visualization).

**Verdict: Fundamentally broken.** Genus-to-A1Z26 does not produce usable letters.

---

### J Section Ranking

1. **J2 -- Symmetry Operations** (if overlay rule is specified)
2. **J1 -- Proof Completion** (current pick, solid)
3. **J5 -- Equation Balancing** (if cryptarithmetic variant)
4. **J3 -- Geometric Construction** (perceptual ambiguity)
5. J4 -- Matrix Multiplication (arbitrary extraction)
6. J6 -- Topology (broken)

**My pick: J1 (Proof Completion)** remains the safe choice. J2 is the more interesting puzzle if the overlay mechanism is nailed down.

---

## 10 — Language & Communication

### 10-1 -- Multi-Cipher Decoder (current pick)

| Criterion | Score |
|-----------|-------|
| Solution standout | 5 |
| Brute-forceable? | No -- must correctly identify and decode each cipher |
| Deductive path | 5 |
| Checkpoints | Yes -- each decoded message is independently verifiable |

**Analysis.** Ten messages, each in a different encoding system, all taught in `codes/`. This is outstanding. Each message is an independent sub-puzzle with its own aha ("this is Braille... this is semaphore..."). The solver must identify the encoding, look it up in the encyclopedia, and decode. Each decoded message yields one letter. First letters spell INFLECTION.

This is the exact structure I advocate: skill isolation per sub-puzzle, legitimate deduction at each step, independent confirmation, and the encyclopedia is genuinely necessary (you must look up the encoding systems). The ten different encodings ensure variety within a single puzzle. No two sub-puzzles use the same cognitive skill.

**Anti-guessing.** Each encoding has a distinctive visual signature (dots for Braille, flag positions for semaphore, dashes for Morse). A solver cannot shortcut without recognizing the encoding, which requires either prior knowledge or reading the reference. This is anti-guessing by design.

**Verdict: Championship quality.** The strongest candidate in the entire pool. Keep it.

---

### 10-2 -- Rosetta Stone

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Moderate -- parallel texts are solvable by pattern matching without understanding |
| Deductive path | 3 |
| Checkpoints | Partial -- each script decoded is a checkpoint |

**Analysis.** Same message in three scripts; knowing one lets you decode the others. Thematically perfect (the actual Rosetta Stone). But the solve is pattern-matching between parallel texts, which is a well-known technique that does not require understanding the scripts themselves. A solver can align character frequencies across parallel texts without reading `linguistics/` at all.

**Verdict: Thematic but shortcuttable.** The intended path (learn scripts from the encyclopedia) is not the only path.

---

### 10-3 -- Phonetic Riddle

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Yes -- can be approximated by trying to pronounce IPA symbols without formal training |
| Deductive path | 2 |
| Checkpoints | No -- you either hear it or you don't |

**Analysis.** IPA symbols that sound like an English phrase when pronounced. This is an "aha or not" puzzle: either the solver pronounces correctly and hears the answer, or they don't. There is no intermediate deductive step. The puzzle collapses to perception, not logic.

**Anti-guessing concern.** A solver who roughly knows IPA (or who tries enough pronunciations) can stumble into the answer. The puzzle has no resistance to approximate approaches.

**Verdict: Perceptual, not deductive.**

---

### 10-4 -- Etymological Chain

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Yes -- the PIE root can be looked up directly, bypassing the chain |
| Deductive path | 3 |
| Checkpoints | Yes -- each stage is independently verifiable |

**Analysis.** Trace a word's origin across five languages to find the PIE root. The chain is interesting linguistically, but the solve is a lookup sequence, not a deduction. Each stage asks "what is this word in the previous language?" which is a research task. A solver with an etymological dictionary solves this without the encyclopedia.

**Verdict: Research task, not deductive puzzle.**

---

### 10-5 -- Cipher Wheel Construction

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | No -- must build and align correctly |
| Deductive path | 3 |
| Checkpoints | Yes -- decoded text is incrementally verifiable |

**Analysis.** Build a physical cipher wheel, then decode a message. The construction is a nice physical moment, and the decoding is a legitimate solve step. But the puzzle has two phases: build (which is craft, not deduction) and decode (which is mechanical once the wheel is built). The deductive content is thin -- the solver follows construction instructions and then applies a substitution cipher.

**Concern.** How does the solver know the correct alignment? If the alignment is given, the puzzle is pure mechanical decoding. If the alignment must be deduced, THAT is the puzzle -- and it needs to be specified.

**Verdict: Physical spectacle with thin deductive content.** The alignment deduction is the puzzle; everything else is setup.

---

### 10-6 -- Semaphore / Flag Reading

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | No -- must decode correctly |
| Deductive path | 4 |
| Checkpoints | Yes -- each flag position decodes independently |

**Analysis.** Stick-figure flag positions decoded using the semaphore alphabet. Clean, deterministic, teachable from `codes/`. Each flag is an independent decode step. But this is essentially one of the ten sub-puzzles in 10-1 (Multi-Cipher Decoder), extracted and expanded to fill an entire puzzle slot. As a standalone puzzle, it is too thin -- "decode semaphore" is one aha repeated N times.

**Verdict: Clean but thin.** Already subsumed by 10-1.

---

### 10 Section Ranking

1. **10-1 -- Multi-Cipher Decoder** (championship quality)
2. 10-6 -- Semaphore (clean but thin, subsumed by 10-1)
3. 10-5 -- Cipher Wheel (physical, thin deduction)
4. 10-2 -- Rosetta Stone (shortcuttable)
5. 10-4 -- Etymological Chain (research, not deduction)
6. 10-3 -- Phonetic Riddle (perceptual, not deductive)

**My pick: 10-1.** No contest.

---

## 9 — Social Sciences

### 9-1 -- Logic Grid (current pick)

| Criterion | Score |
|-----------|-------|
| Solution standout | 5 |
| Brute-forceable? | No -- logic grids are NP-hard in general; well-designed ones require deduction |
| Deductive path | 5 |
| Checkpoints | Yes -- each deduced constraint eliminates possibilities, visible on the grid |

**Analysis.** An Einstein's riddle with social science concepts as attributes. This is a gold-standard puzzle format. Logic grids are the purest form of deductive reasoning in puzzle design: every placement follows from constraint elimination. The solver can verify progress at every step (the grid shows what has been eliminated). The answer emerges inevitably from complete deduction.

The social science theming (governance types, economic models, legal traditions) requires reading the encyclopedia to understand the attributes. A solver who doesn't know the difference between "common law" and "civil law" cannot evaluate the clues. This forces genuine engagement with the content.

**Anti-guessing.** A well-designed logic grid cannot be brute-forced by casual guessing because the constraint space is too large (5! = 120 permutations per attribute, multiple attributes). It CAN be brute-forced by systematic enumeration, but the effort is comparable to just solving it logically. This is the sweet spot.

**Concern.** The answer word INCENTIVE has 9 letters. How does a 5-entity logic grid produce a 9-letter answer? The extraction mechanism is unspecified. Standard logic-grid extraction: the arrangement of attributes in the solved grid, read in some order, gives letters. This needs to be specified.

**Verdict: The best puzzle format in the pool alongside 10-1.** The extraction from grid-to-answer-word is the only missing piece.

---

### 9-2 -- Prisoner's Dilemma Tournament

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | Yes -- only 2^5 = 32 possible binary strings for 5 rounds |
| Deductive path | 2 |
| Checkpoints | No |

**Analysis.** Five games, each with a payoff matrix. Optimal move maps to binary, decoded to letters. I flagged this mechanism family in Round 1 and my concerns remain.

**Anti-guessing.** 5 binary choices = 32 possible strings. A solver can enumerate all 32 and check which one decodes to something meaningful. This is trivially brute-forceable.

**Verdict: Brute-forceable. Reject.**

---

### 9-3 -- Voting Paradox

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Moderate -- three elections with known voting systems have deterministic outcomes |
| Deductive path | 3 |
| Checkpoints | Partial -- each election's winner is independently verifiable |

**Analysis.** Same candidates, three voting systems, three different winners. The paradox is genuinely interesting. But the brief says "which candidate wins under which system" -- this is a calculation, not a deduction. Given votes and a voting system, the winner is determined mechanically. The interesting part (the paradox) is an observation, not a puzzle step.

The extraction is unclear: "the paradox itself encodes the answer." How? If the three winners' initials spell something, that is a three-letter extraction from a deterministic calculation. Thin.

**Verdict: Interesting topic, underdeveloped as a puzzle.**

---

### 9-4 -- Market Equilibrium

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | Yes -- equilibrium prices are deterministic from supply/demand curves |
| Deductive path | 2 |
| Checkpoints | Yes -- each equilibrium is independently findable |

**Analysis.** Find equilibrium prices from supply/demand curves, map to letters. This is "read a graph, get a number, apply A1Z26." The graph-reading step is mechanical. The number-to-letter step is arbitrary. There is no deduction beyond "find where the lines cross."

**Verdict: Graph reading + A1Z26. Reject.**

---

### 9-5 -- Treaty Network

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | Moderate -- graph metrics can be computed mechanically |
| Deductive path | 2 |
| Checkpoints | No |

**Analysis.** A graph of nations and treaties; graph structure encodes the answer. The brief lists multiple possible metrics (most connections, shortest path) without committing. When the extraction metric is unspecified, the solver must guess which metric to use. That is the opposite of "the intended solution stands out."

**Verdict: Underspecified. The solver must guess the metric.**

---

### 9 Section Ranking

1. **9-1 -- Logic Grid** (championship quality)
2. 9-3 -- Voting Paradox (interesting, underdeveloped)
3. 9-5 -- Treaty Network (underspecified)
4. 9-2 -- Prisoner's Dilemma (brute-forceable)
5. 9-4 -- Market Equilibrium (A1Z26)

**My pick: 9-1.** Dominant choice.

---

## 8 — Technology

### 8-1 -- Signal Tracing (current pick)

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | No -- must understand each component's effect |
| Deductive path | 4 |
| Checkpoints | Yes -- signal state can be tracked at each component |

**Analysis.** Trace a signal through a system diagram; each component transforms the signal; output decodes to the answer. This is the technology equivalent of K2 (Algorithm Execution): follow a deterministic process, track state at each step, read the output. The solver must understand what each component does (from the encyclopedia), which forces genuine content engagement.

The signal-tracing format provides natural checkpoints: at each component, the solver can verify their current signal state against the expected behavior. If something is wrong, they can localize the error to a specific component.

**Concern.** "Apply transformations sequentially" -- the transformations must be well-defined and deterministic. If a component "amplifies" a signal, what does that mean for a text/number signal? The metaphor of signal transformation must map cleanly to actual operations on the answer data.

**Verdict: Strong.** The Technology equivalent of Algorithm Execution.

---

### 8-2 -- Logic Gate Circuit

| Criterion | Score |
|-----------|-------|
| Solution standout | 5 |
| Brute-forceable? | No -- must trace the circuit correctly |
| Deductive path | 5 |
| Checkpoints | Yes -- each gate output is independently verifiable |

**Analysis.** A logic circuit with AND/OR/NOT/XOR gates. Given inputs, trace through to compute outputs. Binary output decodes to ASCII. This is CLEAN. Logic gate evaluation is completely deterministic. Each gate is an independent verification point. The solver must understand Boolean logic (learnable from the encyclopedia). The binary-to-ASCII decoding is standard and well-motivated (this IS how computers work).

**This is the puzzle I asked for in Round 1** when I said Technology should have "a circuit-logic puzzle." The solver thinks like an engineer. The mechanism IS the subject matter. Perfect thematic integration.

**Anti-guessing.** A logic circuit with 8+ inputs and multiple gate layers has an exponentially large truth table. The solver cannot enumerate -- they must trace. Excellent resistance.

**Verdict: Championship quality for the Technology slot.**

---

### 8-3 -- Frequency Spectrum

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Moderate -- frequency-to-note mappings are well-known |
| Deductive path | 3 |
| Checkpoints | Yes -- each frequency decodes independently |

**Analysis.** Frequency peaks identified and mapped to musical notes, then to letters. This is a cross-section puzzle (Technology + Music Theory) with a two-step encoding: Hz -> note name -> letter. The Hz-to-note mapping is deterministic and well-defined (A4 = 440 Hz, etc.). But the note-to-letter extraction has the same CDEFGAB alphabet constraint as Q3 (Musical Staff).

**Verdict: Same alphabet constraint as Q3. Impractical for most answer words.**

---

### 8-4 -- Bit Pattern / QR by Hand

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Moderate -- visual grids can be decoded by trying standard encodings |
| Deductive path | 3 |
| Checkpoints | Yes -- each byte decodes independently |

**Analysis.** A grid of black and white squares, decoded to letters. Similar to K5 (Binary Decoder) but visual rather than textual. The solver must recognize the encoding system. If it is explicitly given (e.g., "this is a 5-bit encoding"), the puzzle is mechanical. If it must be deduced, the solver tries standard encodings until one works -- guess-and-check.

**Verdict: Guess-and-check on the encoding type. No clean deductive path.**

---

### 8-5 -- PCB Trace Following

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | Moderate -- if the PCB is small, all paths can be enumerated |
| Deductive path | 3 |
| Checkpoints | Yes -- letters at each component are independently readable |

**Analysis.** Follow copper traces on a circuit board; collect letters at components. The path-following is clean (traces are deterministic), but the deductive content is thin: "follow the line, read the letter." This is a maze with letters, which is engaging but not deeply deductive.

**Concern.** If the solver must choose which trace to follow at branch points, what determines the correct choice? If it is "follow the thickest trace" or "follow the trace labeled VCC," the selection rule must be deducible. If it is arbitrary, this is a brute-forceable maze.

**Verdict: Engaging visual puzzle, thin on deduction.**

---

### 8 Section Ranking

1. **8-2 -- Logic Gate Circuit** (championship quality)
2. **8-1 -- Signal Tracing** (current pick, solid)
3. 8-5 -- PCB Trace Following (engaging, thin deduction)
4. 8-3 -- Frequency Spectrum (alphabet-constrained)
5. 8-4 -- Bit Pattern (guess-and-check)

**My pick: 8-2.** It is the cleanest deductive puzzle in the Technology pool and better than the current pick 8-1. Signal Tracing (8-1) is the fallback if 8-2's visual design proves impractical for print.

---

## 7 — Mechanics

### 7-1 -- Engineering Calculation (current pick)

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | No -- must compute each machine correctly |
| Deductive path | 4 |
| Checkpoints | Yes -- each calculation is independently verifiable |

**Analysis.** Five simple machines, calculate output for each, numbers map to letters via A1Z26 to spell TORQUE. Each calculation is deterministic and requires understanding the machine (from `mechanical/`). The worksheet format provides natural structure.

**Concern.** A1Z26 again. The numbers must happen to map to T-O-R-Q-U-E (20-15-18-17-21-5). That means the five machines must produce outputs of exactly 20, 15, 18, 17, 21, and 5 (in some unit). This constrains the machine parameters severely. A lever with mechanical advantage 20? A gear train with ratio 15? These must feel like natural engineering problems, not reverse-engineered arithmetic. If the parameters feel contrived to produce specific numbers, the puzzle loses credibility.

**Anti-guessing.** Five calculations = five numbers. If the solver suspects A1Z26, they can check whether the five numbers fall in the range 1-26 and try decoding. A1Z26 is always the first guess. However, the solver still needs to compute the numbers correctly, which requires understanding the machines. This is acceptable -- the A1Z26 step is guessable, but the calculation step is not.

**Verdict: Solid.** The A1Z26 extraction is the weakest link, but the calculation steps are genuinely deductive.

---

### 7-2 -- Gear Train

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | No -- must count teeth and calculate |
| Deductive path | 3 |
| Checkpoints | Yes -- each stage is independently calculable |

**Analysis.** A gear train with multiple stages; calculate output RPM for each stage; outputs encode letters. This is a subset of 7-1 (Engineering Calculation) restricted to gears. It's narrower in scope (one machine type vs. five) and uses the same A1Z26 extraction. Less variety, same mechanism.

**Verdict: Subsumed by 7-1.** No reason to pick this over the broader Engineering Calculation.

---

### 7-3 -- Rube Goldberg Chain

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Yes -- identifying mechanical principles by name is a lookup, not a deduction |
| Deductive path | 2 |
| Checkpoints | Yes -- each stage is independently identifiable |

**Analysis.** An elaborate chain reaction; each stage uses a different principle; first letters of principle names spell the answer. The visual is delightful (the brief correctly notes high fun factor). But the deductive content is thin: "look at the picture, name the principle, take the first letter." This is identification + acrostic, not deduction.

**Anti-guessing.** A mechanically literate solver can name the principles without the encyclopedia. "That's a lever. That's a spring. That's a pulley." No reference needed. This defeats the Red Joker's pedagogical purpose.

**Verdict: High fun, low deductive rigor.** Better suited for the Black Joker as a warm-up or for a younger audience.

---

### 7-4 -- Bridge Structural Analysis

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | No -- must analyze each member correctly |
| Deductive path | 4 |
| Checkpoints | Yes -- each member can be independently verified via equilibrium |

**Analysis.** A truss bridge with labeled members. Determine tension (T) or compression (C) for each. T/C pattern = binary, decoded to letters. The structural analysis is genuinely deductive: each member's state follows from equilibrium equations at the joints. This is constraint-based reasoning -- the same cognitive mode as logic grids.

**Concern.** T/C binary encoding has the same Morse-ambiguity problem: where are the letter boundaries? If the bridge has 40 members and the encoding is 5-bit ASCII, you get 8 characters. But the solver must know to group in chunks of 5 (or 7 or 8). The grouping convention must be deducible or given.

**Stronger concern.** Structural analysis requires force calculations, not just qualitative T/C classification. A solver can determine T/C for a simple truss by the method of joints without any calculations -- just sign analysis. This is actually a feature: the deduction is purely logical (which way does this force point?), not numerical.

**Verdict: Strong.** The T/C binary encoding needs a specified grouping rule, but the structural analysis itself is excellent deductive content.

---

### 7-5 -- Fluid Flow Path

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Moderate -- simple pipe networks have obvious flow paths |
| Deductive path | 3 |
| Checkpoints | Yes -- flow direction at each junction is determinable |

**Analysis.** Trace fluid through a branching pipe network; at each junction, calculate which branch the fluid takes. This is a path-following puzzle with physics-based branching decisions. The deductive content is at the junctions: which way does the fluid go? If the physics is simplified (fluid takes the wider pipe), the deduction is trivial. If it requires Bernoulli-equation calculations, the deduction is genuine but heavy.

**Verdict: Depends on junction complexity.** Trivial junctions = trivial puzzle. Complex junctions = potentially excellent but may be too calculation-heavy for a general audience.

---

### 7 Section Ranking

1. **7-1 -- Engineering Calculation** (current pick, solid)
2. **7-4 -- Bridge Structural Analysis** (strong deductive content)
3. 7-5 -- Fluid Flow Path (depends on execution)
4. 7-2 -- Gear Train (subsumed by 7-1)
5. 7-3 -- Rube Goldberg (fun, not deductive)

**My pick: 7-1** for breadth (five machine types), or **7-4** for deeper deduction (structural analysis is constraint-based reasoning). 7-1 is safer; 7-4 is more rigorous.

---

## 6 — History & Ideas

### 6-1 -- Primary Source Detective (current pick)

| Criterion | Score |
|-----------|-------|
| Solution standout | 5 |
| Brute-forceable? | No -- must identify sources correctly |
| Deductive path | 4 |
| Checkpoints | Yes -- each source identification is independently verifiable |

**Analysis.** Identify 8 historical documents from their opening lines. Chronological ordering + extraction from author names spells PARADIGM. This is a strong format: source identification is a genuine reasoning task (recognize the rhetoric, the era, the concerns), chronological ordering adds a sort step, and the extraction from author names is clean.

**Concern.** "Extraction from author names" is vague. First letters of author names? Nth letter? The extraction rule must be specified and must feel natural. If it is first-letter acrostic, that is another acrostic (I have counted too many in this pool). If it is positional (letter 1 from author 1, letter 2 from author 2...), that is a diagonal read.

**Anti-guessing.** Identifying historical documents from opening lines is not trivially brute-forceable. A solver needs either historical knowledge or the encyclopedia. The chronological ordering adds a constraint that prevents rearrangement to make a different word. Good.

**Concern about source ambiguity.** Some famous documents have well-known opening lines ("We the People..."). These are identifiable without the encyclopedia, which undermines pedagogical purpose. Others are obscure. The difficulty curve should be managed -- mix recognizable and less-recognizable sources.

**Verdict: Strong.** The extraction rule needs specification, but the identification + ordering format is sound.

---

### 6-2 -- Historical Map Overlay

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | No |
| Deductive path | 2 |
| Checkpoints | No -- the word either appears or it doesn't |

**Analysis.** Overlay maps from different eras; boundary differences form letter shapes or encode letters. This is a physical reveal (like Q4 Color Overlay), not a deductive puzzle. The solver performs one physical action and reads the result.

**Concern.** "Boundaries that changed form letter shapes" is perceptually dubious. Borders are determined by geography, wars, and treaties -- not by aesthetic letter-formation. The letters will be crude at best, ambiguous at worst.

**Verdict: Reveal mechanism, not deductive puzzle.**

---

### 6-3 -- Philosophical Argument Chain

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | Moderate -- formal fallacy identification has a finite set |
| Deductive path | 4 |
| Checkpoints | Yes -- each step is independently evaluable |

**Analysis.** A multi-step argument; some steps are valid, others are fallacies. Valid = 1, fallacy = 0; binary decoded to letters. The fallacy identification requires reading `philosophy/` and `logic/`. This is a genuinely deductive puzzle: evaluating logical validity IS deduction. The solver must reason about each step's logical structure.

**Concern.** Binary encoding has the same grouping problem (where do letter boundaries fall?). But if the argument has a fixed number of steps and the grouping is specified (e.g., "8 steps = 1 byte = 1 letter"), this is clean. Also: fallacy identification can be subjective for informal fallacies. Restrict to formal fallacies (denying the antecedent, affirming the consequent, etc.) where validity is objectively determinable.

**Verdict: Strong if restricted to formal logic.** The binary encoding is not ideal but the fallacy-identification step is genuinely deductive.

---

### 6-4 -- Cause-and-Effect Web

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | Yes -- "longest causal chain" is computable by inspection |
| Deductive path | 2 |
| Checkpoints | No |

**Analysis.** A web of historical events with causal arrows. Trace the longest chain; events contribute letters. The "longest chain" is a well-defined graph problem (longest path in a DAG), but finding it is mechanical, not deductive. The solver follows arrows and counts chain length. No historical reasoning is required beyond reading the labels.

**Verdict: Graph traversal, not historical reasoning.**

---

### 6-5 -- Fairy Tale Logic

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Depends on the logic puzzle embedded in the narrative |
| Deductive path | 3 |
| Checkpoints | Depends on structure |

**Analysis.** A narrative logic puzzle with constraints from mythology and religious studies. This is a wrapper: the puzzle quality depends entirely on the logic puzzle inside the fairy-tale narrative. The narrative is flavor; the puzzle is the constraint structure. Without seeing the actual constraints, I cannot evaluate deductive rigor.

**Verdict: Undefined.** The brief describes a framing device, not a puzzle mechanism.

---

### 6 Section Ranking

1. **6-1 -- Primary Source Detective** (current pick, strong)
2. **6-3 -- Philosophical Argument Chain** (genuinely deductive)
3. 6-5 -- Fairy Tale Logic (undefined mechanism)
4. 6-4 -- Cause-and-Effect Web (graph traversal)
5. 6-2 -- Historical Map Overlay (physical reveal)

**My pick: 6-1.** The current pick is the strongest. 6-3 is a strong alternative if the History slot wants more logical rigor.

---

## 5 — Life Sciences

### 5-1 -- Codon Decoding (current pick)

| Criterion | Score |
|-----------|-------|
| Solution standout | 5 |
| Brute-forceable? | No -- must perform the biological translation correctly |
| Deductive path | 5 |
| Checkpoints | Yes -- each codon translates independently |

**Analysis.** DNA -> mRNA -> codons -> amino acids -> single-letter codes -> answer. This is real biochemistry used as a puzzle mechanism. The translation process has multiple deterministic steps (transcription, codon lookup, amino acid naming). Each step is taught in the encyclopedia. The solver learns the genetic code and applies it.

V3 score of 30/30 is justified. This is a perfectly clean puzzle:
- One intended solution (the genetic code is universal)
- Cannot be brute-forced (64 codons, no shortcuts)
- Clean deductive path (follow the central dogma)
- Strong confirmation (each amino acid is independently derivable)
- Genuinely self-referential (biology section teaches the tool needed to solve the biology puzzle)

**The answer GENETIC uses only valid amino acid single-letter codes: G(Gly), E(Glu), N(Asn), E(Glu), T(Thr), I(Ile), C(Cys). Every letter checks out.**

**Verdict: The best puzzle in the pool, tied with 10-1.** Do not change anything.

---

### 5-2 -- Phylogenetic Tree Traversal

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Moderate -- tree structure constrains the path |
| Deductive path | 3 |
| Checkpoints | Yes -- each branch point is independently evaluable |

**Analysis.** Trace a phylogenetic tree; at each branch point, the common ancestor's key trait contributes a letter. The tree traversal is deterministic (there is one path between any two species). The trait identification requires biology knowledge. Clean concept but the extraction (trait -> letter) is underspecified. First letter of trait name? That is another acrostic.

**Verdict: Solid structure, underspecified extraction.**

---

### 5-3 -- Metabolic Pathway

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Yes -- metabolic pathway intermediates are well-known and googlable |
| Deductive path | 3 |
| Checkpoints | Yes -- each intermediate is independently identifiable |

**Analysis.** Follow glucose through metabolism; first letters of intermediates spell the answer. The pathway is standard biochemistry (glucose -> G6P -> F6P -> FBP -> ... -> pyruvate -> acetyl-CoA -> citrate -> ...). The first letters are determined by biology, not by puzzle construction. This means the answer word is fixed by the pathway, not designed. If the pathway naturally spells a word, that is beautiful. If it doesn't (and it probably doesn't -- G,F,F,D,G,P,...), the constructor must cherry-pick intermediates, which breaks the natural ordering.

**Anti-guessing.** Glycolysis and the Krebs cycle are textbook material. A biology student solves this from memory. No encyclopedia needed.

**Verdict: Answer word is constrained by biology, not design. Likely does not naturally spell a useful word.**

---

### 5-4 -- Punnett Square Genetics

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | No -- must compute ratios correctly |
| Deductive path | 3 |
| Checkpoints | Yes -- each cross is independently solvable |

**Analysis.** Genetic crosses; phenotype ratios map to letters. The Punnett square computation is deterministic and teachable. But the ratio-to-letter mapping is arbitrary. 3:1 maps to... what? The number 3? The number 1? The ratio "3:1" itself? Without a natural mapping, this is another "compute a number, apply arbitrary conversion."

**Verdict: Clean computation, arbitrary extraction.**

---

### 5-5 -- Cell Organelle Labeling

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Yes -- cell organelles are standard biology knowledge |
| Deductive path | 2 |
| Checkpoints | Yes -- each organelle is independently identifiable |

**Analysis.** Label a cell diagram; first letters of organelle names, read clockwise, spell the answer. This is identification + acrostic. The identification is a lookup task, not a deduction. A biology student labels a cell without the encyclopedia. The "clockwise" reading order is arbitrary -- why clockwise? The organelles are arranged in a cell by biology, not by alphabet.

**Anti-guessing.** Cell organelles are basic biology. Nucleus, mitochondria, endoplasmic reticulum, Golgi apparatus, lysosome, ribosome, vacuole... these are recognizable without reference material.

**Verdict: Trivial for biology-literate solvers. Not deductive.**

---

### 5-6 -- Epidemic Network

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Moderate -- transmission rules constrain the spread deterministically |
| Deductive path | 3 |
| Checkpoints | Yes -- each transmission step is independently verifiable |

**Analysis.** Trace disease spread through a population; infected individuals' initials spell the answer. The transmission rules make the spread order deterministic. The solver applies rules step by step. This is similar to K2 (Algorithm Execution) but with epidemiological flavor. The constraint-based propagation is a legitimate deductive activity.

**Concern.** "Multiple valid paths exist -- only one spells a real word." This is guess-and-check: try paths until one spells something. That violates my principle that the intended solution must stand out through deduction, not through checking against an English dictionary.

**Verdict: The "try paths until one spells a word" mechanism is anti-deductive.** If there is exactly one valid transmission path (determined by the rules), this improves dramatically.

---

### 5 Section Ranking

1. **5-1 -- Codon Decoding** (current pick, perfect)
2. 5-6 -- Epidemic Network (if single valid path)
3. 5-2 -- Phylogenetic Tree (underspecified extraction)
4. 5-4 -- Punnett Square (arbitrary extraction)
5. 5-3 -- Metabolic Pathway (answer constrained by biology)
6. 5-5 -- Cell Labeling (trivial)

**My pick: 5-1.** Uncontested.

---

## 4 — Material Culture

### 4-1 -- Element Identification (current pick)

| Criterion | Score |
|-----------|-------|
| Solution standout | 5 |
| Brute-forceable? | No -- must correctly identify each element |
| Deductive path | 4 |
| Checkpoints | Yes -- each element identification is independently verifiable |

**Analysis.** 7 riddle-clues about elements. Identify each from properties. First letters spell CASTING (Carbon, Aluminum, Silver, Tin, Iron, Nickel, Gold). This is a clean format: each riddle is a self-contained identification puzzle. The properties must be specific enough to uniquely identify each element (many elements share common properties like "metallic" or "conducts electricity").

**Concern.** Silver's symbol is Ag, Tin is Sn, Iron is Fe, Gold is Au -- but the puzzle uses English names (first letters C,A,S,T,I,N,G). The solver must provide English names, not chemical symbols. This is fine but should be explicit in the puzzle framing.

**Anti-guessing.** With 118 elements, the search space is too large to brute-force. The solver must use the property clues. However, each clue must uniquely identify one element -- if a clue fits multiple elements, the puzzle has multiple solutions. "A yellow metal" fits gold, brass, and others. "A yellow metal with atomic number 79 that doesn't tarnish" uniquely identifies gold.

**Verdict: Strong.** Ensure each riddle-clue uniquely identifies exactly one element.

---

### 4-2 -- Craft Process Ordering

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Moderate -- process orderings are well-known in craft literature |
| Deductive path | 3 |
| Checkpoints | Partial -- some ordering constraints are obvious (can't glaze before firing) |

**Analysis.** Steps of a material process, given out of order. Correct sequence + extraction spells the answer. The ordering is deterministic if the process is well-defined. But some processes have steps that can occur in either order, creating ambiguity. The extraction mechanism is unspecified.

**Verdict: Underspecified.** The ordering is potentially deductive, but the extraction needs work.

---

### 4-3 -- Textile Pattern Binary

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | No -- must read the weaving draft correctly |
| Deductive path | 3 |
| Checkpoints | Yes -- each byte decodes independently |

**Analysis.** A weaving draft diagram where over/under = 1/0. Read the binary, decode to ASCII. The weaving draft is a real notation system taught in `textiles/`. The solver must learn to read the draft (which thread is on top), convert to binary, and decode. This has the same structural virtue as 5-1 (Codon Decoding): the section teaches a real notation system, and the puzzle uses that system.

**Concern.** Weaving drafts are 2D grids. The reading order (left-to-right, top-to-bottom? or column-first?) must be specified or deducible. Without a specified reading order, the solver faces multiple possible bit-strings from the same grid.

**Verdict: Good thematic integration.** Needs specified reading order.

---

### 4-4 -- Glaze Chemistry

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | Moderate |
| Deductive path | 2 |
| Checkpoints | Yes -- each ratio is independently computable |

**Analysis.** Balance ceramic glaze recipes; oxide ratios simplify to small integers; A1Z26 to letters. This is "compute a number, apply A1Z26." The glaze chemistry is thematic, but the A1Z26 step is arbitrary. Why would oxide ratios correspond to letters?

**Verdict: A1Z26 again. Reject.**

---

### 4-5 -- Periodic Table Spelling

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | Yes -- element-symbol spelling is a well-known recreational puzzle type |
| Deductive path | 2 |
| Checkpoints | Yes -- each symbol is independently verifiable |

**Analysis.** Spell the answer using element symbols. The brief itself notes this does not work for CASTING ("G isn't an element symbol"). When the brief demonstrates that the mechanism fails for the target answer word, the mechanism is broken.

**Verdict: Self-acknowledged failure. Reject.**

---

### 4-6 -- Kiln Temperature Profile

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | Yes -- peak temperatures are readable directly from the graph |
| Deductive path | 2 |
| Checkpoints | Yes -- each peak is independently readable |

**Analysis.** Read peak temperatures from a graph, A1Z26 to letters. This is "read a graph, apply A1Z26." The graph reading is trivial. There is no deduction.

**Verdict: Graph reading + A1Z26. Reject.**

---

### 4 Section Ranking

1. **4-1 -- Element Identification** (current pick, strong)
2. **4-3 -- Textile Pattern Binary** (good thematic integration)
3. 4-2 -- Craft Process Ordering (underspecified)
4. 4-4 -- Glaze Chemistry (A1Z26)
5. 4-6 -- Kiln Temperature (A1Z26)
6. 4-5 -- Periodic Table Spelling (broken)

**My pick: 4-1.** Clear winner.

---

## 3 — Earth & Space

### 3-1 -- Connect-the-Dots Star Chart (current pick)

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | No -- must identify celestial objects and plot correctly |
| Deductive path | 4 |
| Checkpoints | Partial -- each group of objects can be plotted independently |

**Analysis.** 7 groups of celestial objects described poetically. Identify, plot on a coordinate grid. Each group traces a letter. 7 letters spell EQUINOX. This is a multi-step puzzle: (1) identify objects from descriptions, (2) determine coordinates, (3) plot, (4) recognize letter shapes. Steps 1-2 require the encyclopedia. Step 3 is physical (drawing). Step 4 is perceptual.

**Concern.** Step 4 (recognizing letter shapes from plotted points) is perceptual, not deductive. A group of 4-5 points connected in order might look like an E... or a W... or an M, depending on how you connect them. The connect-the-dots order must be unambiguous (e.g., connect in order of brightness, or in order of distance).

**Physical concern.** This requires drawing on the page -- "the Chicago Fire moment." That is a design choice about the physical experience, not the deductive structure. Drawing is engaging but introduces manual error (imprecise plotting).

**Anti-guessing.** 7 letter shapes from 7 groups is hard to brute-force. The solver must plot correctly to see the letters. The coordinate grid constrains the positions. Good.

**Verdict: Strong if the connection order within each group is unambiguous.** The perceptual letter-recognition step is the weak link.

---

### 3-2 -- Geological Cross-Section

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Yes -- hidden words in strata names are findable by scanning |
| Deductive path | 2 |
| Checkpoints | Yes -- each stratum is independently scannable |

**Analysis.** A cross-section diagram with labeled strata. "Certain letters in the strata names, when read at specific depths, spell the answer." This is a steganographic hidden-word puzzle. The solver scans strata names for embedded words. This is pattern recognition (word search), not geological reasoning. The geology provides the setting but not the puzzle mechanism.

**Verdict: Word search in geological labels. No geological deduction required.**

---

### 3-3 -- River Confluence Map

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | No |
| Deductive path | 2 |
| Checkpoints | No -- letters only visible after connecting all points |

**Analysis.** Plot river confluence points on a map; connected in order of river length, they trace letter shapes. This is connect-the-dots on a map. The ordering (by river length) is a sort step. The letter recognition is perceptual. No geographical reasoning beyond "where do these rivers meet?"

**Verdict: Connect-the-dots with geographic trivia.** Similar to 3-1 but weaker because the points are geographic facts, not objects requiring identification.

---

### 3-4 -- Mountain Silhouette

| Criterion | Score |
|-----------|-------|
| Solution standout | 1 |
| Brute-forceable? | N/A |
| Deductive path | 1 |
| Checkpoints | No |

**FUNDAMENTALLY UNSOUND.** Mountain silhouette profiles do not look like letters. The Himalayas do not look like an "H." This is wishful thinking. Real mountain ranges have complex, irregular silhouettes that are perceptually ambiguous. The solver would be staring at a skyline trying to see a letter that was never there. This is a Rorschach test, not a puzzle.

**Verdict: Reject.** No clean solving path. Perceptual ambiguity is maximal.

---

### 3-5 -- Tectonic Plate Jigsaw

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Moderate -- plate shapes are well-known |
| Deductive path | 2 |
| Checkpoints | Partial -- plate shapes provide some confirmation during assembly |

**Analysis.** Cut-out tectonic plates; assemble correctly; letters on plate edges align to spell the answer. The jigsaw assembly is spatial reasoning (good), but the letter alignment is a reveal, not a deduction. Once assembled, the solver reads the answer. The "puzzle" is the jigsaw; the "answer" is revealed by assembly.

**Concern.** Requires cutting pages from the book. This is a high-commitment physical action that many solvers will resist.

**Verdict: Spatial puzzle with reveal-based extraction.** Cutting the book is a significant barrier.

---

### 3-6 -- Sundial Construction

| Criterion | Score |
|-----------|-------|
| Solution standout | 1 |
| Brute-forceable? | N/A |
| Deductive path | 1 |
| Checkpoints | No |

**FUNDAMENTALLY UNSOUND.** A paper sundial that must be used in actual sunlight at a specific time. This requires: (1) being at the correct latitude, (2) having sunlight, (3) correct assembly, (4) being present at the specific time. Four external dependencies, none of which are under the solver's control. A puzzle that requires waiting for specific weather conditions is not a puzzle -- it is a hostage situation.

**Verdict: Reject.** External dependencies make this unsolvable under most conditions.

---

### 3 Section Ranking

1. **3-1 -- Connect-the-Dots Star Chart** (current pick, strong)
2. 3-5 -- Tectonic Plate Jigsaw (spatial, but requires cutting)
3. 3-2 -- Geological Cross-Section (word search, not geology)
4. 3-3 -- River Confluence (connect-the-dots trivia)
5. 3-4 -- Mountain Silhouette (fundamentally unsound)
6. 3-6 -- Sundial (fundamentally unsound)

**My pick: 3-1.** Best option despite the perceptual letter-recognition concern.

---

## 2 — Natural World

### 2-1 -- Organism Identification + Diagonal (current pick)

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | No -- must identify organisms correctly |
| Deductive path | 4 |
| Checkpoints | Yes -- diagonal produces recognizable letter prefixes after 3-4 organisms |

**Analysis.** 5 organisms described by characteristics. Identify using the Natural World section. Diagonal read across common names spells the answer. This is the same mechanism I praised in Round 1 (then as "Puzzle 12"): diagonal reads are self-confirming, the identification requires encyclopedia knowledge, and the extraction is clean.

**Concern.** Only 5 organisms for a 5-letter answer (NICHE). That is a tight constraint: organism 1's 1st letter, organism 2's 2nd letter, organism 3's 3rd letter, organism 4's 4th letter, organism 5's 5th letter. Each organism must have a name at least as long as its position number. Name 5 must have at least 5 letters. This is constructible but constraining.

**Anti-guessing.** 5 descriptions, each must be identified from characteristics. With thousands of species in the Natural World section, brute-force is impractical. The solver must actually read and reason.

**Verdict: Clean and compact.** The 5-letter answer makes it tight but constructible.

---

### 2-2 -- Food Web Traversal

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | Yes -- "try all paths, check which spells a word" is feasible |
| Deductive path | 2 |
| Checkpoints | No |

**Analysis.** "Multiple valid paths exist -- only one spells a real word." I flagged this exact problem in 5-6 (Epidemic Network). When the puzzle mechanism admits multiple valid paths and the solver must try each one against an English dictionary, the puzzle is brute-forceable by enumeration. The deductive path is absent -- the solver is guessing, not reasoning.

**Verdict: Brute-forceable by path enumeration. Reject.**

---

### 2-3 -- Leaf / Mushroom Identification Key

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | No -- must evaluate each binary choice correctly |
| Deductive path | 4 |
| Checkpoints | Yes -- each classification is independently verifiable |

**Analysis.** A dichotomous identification key. Several specimens to classify. Each binary choice leads to a classification. Classifications encode letters. This is genuinely deductive: dichotomous keys are binary decision trees where each choice is based on observable characteristics. The solver evaluates "smooth or serrated?" at each node and follows the tree. Each classification is deterministic given correct observations.

**Strength.** This is naturalist reasoning in its purest form. The solver does what a field biologist does. Thematic integration is deep. The key structure provides natural checkpoints (each specimen classifies independently).

**Concern.** The extraction from classification to letter is unspecified. If classifications map to species names and first letters spell the answer, that is an acrostic. If the path through the key itself encodes binary (left/right = 0/1), that is cleaner but depends on key depth.

**Verdict: Strong.** Best alternative to 2-1 for the Natural World slot.

---

### 2-4 -- Birdsong as Morse

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | No -- must read spectrograms correctly |
| Deductive path | 3 |
| Checkpoints | Yes -- each spectrogram decodes independently |

**Analysis.** Birdsong spectrograms where long notes = dashes, short notes = dots. Decode as Morse. The spectrogram reading is a learnable skill (from `acoustics/`). The Morse decoding is standard. This is a two-encoding chain (spectrogram -> timing pattern -> Morse -> letter), which is one encoding too many. The solver must identify the spectrogram-to-Morse mapping AND decode Morse.

**Verdict: Two encoding layers. One too many.**

---

### 2-5 -- Spice Route

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | No |
| Deductive path | 2 |
| Checkpoints | No -- letters only visible after connecting all points |

**Analysis.** Identify spices, plot origins on a map, connect to trace letter shapes. This is 3-3 (River Confluence) with spices instead of rivers. Same structure: identify -> plot -> connect -> read letters. Same weaknesses: perceptual letter recognition from plotted points.

**Verdict: Connect-the-dots with spice trivia.** Structurally identical to 3-3.

---

### 2 Section Ranking

1. **2-1 -- Organism Identification + Diagonal** (current pick, clean)
2. **2-3 -- Dichotomous Key** (strong naturalist deduction)
3. 2-4 -- Birdsong Morse (one encoding too many)
4. 2-2 -- Food Web (brute-forceable)
5. 2-5 -- Spice Route (connect-the-dots)

**My pick: 2-1** for simplicity and clean extraction, or **2-3** for deeper deductive engagement.

---

## A — People

### A-1 -- Influence Chains (current pick)

| Criterion | Score |
|-----------|-------|
| Solution standout | 4 |
| Brute-forceable? | No -- must identify figures and trace the chain correctly |
| Deductive path | 4 |
| Checkpoints | Yes -- each figure identification is independently verifiable |

**Analysis.** Intellectual inheritance descriptions. Identify each figure. Trace the chain (who taught whom). Letters extracted from each figure's name by position in chain spell POLYMATH. This addresses exactly what I asked for in Round 1: "connections between people." The influence chain is a genuinely relational structure -- the solver reasons about who influenced whom, which requires understanding each figure's contributions.

The extraction (letter N from figure N's name) is a diagonal read, which is clean and self-confirming.

**Concern.** "Intellectual inheritance descriptions" must be specific enough to uniquely identify each figure. "This physicist was influenced by that mathematician" could describe hundreds of pairs. The descriptions must narrow to exactly one figure at each position.

**Anti-guessing.** The chain structure means each figure's identity depends on the previous figure's identity (who did THIS person teach?). This cascading dependency prevents solving figures in isolation -- you must trace the chain. That is strong anti-guessing design.

**Verdict: Strong.** The relational structure (chain of influence) adds deductive depth beyond simple identification.

---

### A-2 -- Portrait Gallery

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Moderate -- achievement descriptions may identify famous figures uniquely or ambiguously |
| Deductive path | 3 |
| Checkpoints | Yes -- each identification is independent |

**Analysis.** Identify 8 people from achievements. Initials spell the answer. This is a standard "who am I?" puzzle with initial-acrostic extraction. Less interesting than A-1 because there is no relational structure -- each identification is independent. The puzzle is 8 isolated trivia questions.

**Verdict: Trivial compared to A-1.** No relational reasoning.

---

### A-3 -- Timeline of Overlapping Lives

| Criterion | Score |
|-----------|-------|
| Solution standout | 2 |
| Brute-forceable? | Moderate -- overlapping lifetimes are computable from dates |
| Deductive path | 2 |
| Checkpoints | No |

**Analysis.** Find pairs whose lifetimes overlapped; the connections reveal a word. The overlap detection is mechanical (compare date ranges). "The connection word encodes the answer" is vague -- what connection? What word? This is underspecified to the point of being unevaluable.

**Verdict: Underspecified. The extraction is unknown.**

---

### A-4 -- Letter Exchange

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | Moderate -- key words in famous letters are identifiable |
| Deductive path | 2 |
| Checkpoints | Partial |

**Analysis.** Excerpts from real letters between thinkers. Key words extracted spell the answer. The extraction rule ("key words") is subjective. Which words are "key"? Without an objective selection criterion, different solvers extract different words. Subjectivity in extraction is anti-deductive.

**Verdict: Subjective extraction. The solver must guess which words are "key."**

---

### A-5 -- Invention Dependency Chain

| Criterion | Score |
|-----------|-------|
| Solution standout | 3 |
| Brute-forceable? | No -- must trace the dependency graph correctly |
| Deductive path | 3 |
| Checkpoints | Yes -- each dependency link is verifiable |

**Analysis.** A dependency graph of inventions. Trace the critical path. Inventor names encode the answer. Similar to A-1 (chain structure) but focused on inventions rather than direct teacher-student relationships. The critical path through a dependency graph is a well-defined concept. The deductive content is in identifying dependencies (does X require Y?), which requires understanding the inventions.

**Concern.** "Critical path" in a dependency graph has a specific meaning (longest path). The solver must identify all dependencies correctly to find the critical path. One wrong dependency link changes the path. There is no local confirmation until the full graph is built.

**Verdict: Structurally sound but all-or-nothing.** The lack of incremental confirmation is a weakness compared to A-1.

---

### A Section Ranking

1. **A-1 -- Influence Chains** (current pick, strong relational structure)
2. A-5 -- Invention Dependency Chain (structural, but all-or-nothing)
3. A-2 -- Portrait Gallery (trivial)
4. A-4 -- Letter Exchange (subjective extraction)
5. A-3 -- Overlapping Lives (underspecified)

**My pick: A-1.** Clear winner.

---

## X — Cross-Section, Visual, and Physical Puzzles

These 17 candidates are not assigned to specific sections. They could augment or replace section-specific puzzles, or serve the Black Joker. I evaluate each for deductive rigor as potential Red Joker inclusions.

### X1 -- Paper + Light (Raiders of the Lost Ark)

| Solution standout: 2 | Brute-forceable: No | Deductive path: 1 | Checkpoints: No |

Build a 3D shape, shine a flashlight through it, shadows form letters. This is pure physical spectacle. Zero deduction. The "puzzle" is following craft instructions. The answer is revealed, not derived. Appropriate as a meta payoff moment, not as a puzzle.

**Flag: No deductive path whatsoever.**

---

### X2 -- Color Overlay

Duplicate of Q4. Same evaluation: reveal mechanism, not puzzle.

---

### X3 -- Fold the Page

| Solution standout: 2 | Brute-forceable: Moderate | Deductive path: 2 | Checkpoints: No |

Fold the page; distant elements align to spell a word. The solver must deduce where to fold, which is one aha. Then the answer is revealed. One aha + reveal = thin.

**Concern.** A solver can try all possible folds (there are few plausible creases on a standard page). Brute-forceable by enumeration.

---

### X4 -- Golden Ratio Spiral

| Solution standout: 3 | Brute-forceable: No | Deductive path: 3 | Checkpoints: Partial |

Multi-section puzzle where phi appears across art, nature, math, and music. The identification of phi is a genuine aha. Using it as a decryption key requires knowing the key value precisely (1.618...), which prevents brute-force. But "phi is the decryption key" -- for what cipher? Unspecified.

**Better as a Black Joker puzzle** (it spans 4 sections).

---

### X5 -- Fibonacci Structural Sequence

Not a puzzle -- a meta-structural observation. The number of elements in each Red Joker puzzle follows Fibonacci. This is a pattern for the constructor to embed, not a puzzle for the solver to solve. Could enhance the meta if solvers who notice it gain an advantage.

**Not evaluable as a puzzle.**

---

### X6 -- Musical Score Message

Duplicate of Q3. Same CDEFGAB alphabet constraint. Same evaluation.

---

### X7 -- Cipher Wheel Construction

Duplicate of 10-5. Same evaluation.

---

### X8 -- Punch Card Overlay

| Solution standout: 3 | Brute-forceable: No | Deductive path: 2 | Checkpoints: No |

Punch holes, overlay on text page, visible text is the answer. This is a physical reveal with one preparatory step (punching). The deductive content is in determining where to punch -- if the positions are marked, there is no deduction. If the positions must be derived, THAT is the puzzle.

**Verdict: The hole-position derivation is the puzzle. Everything else is spectacle.**

---

### X9 -- Mirror Puzzle

| Solution standout: 2 | Brute-forceable: No | Deductive path: 1 | Checkpoints: No |

Hold to mirror, read reversed text. One physical action, answer revealed. Da Vinci connection is thematically nice. Zero deduction.

---

### X10 -- Tangram Letter Assembly

| Solution standout: 3 | Brute-forceable: Moderate | Deductive path: 3 | Checkpoints: Yes -- each letter is independently assembleable |

Rearrange tangram pieces to form letters. Tangram assembly is genuine spatial reasoning. Each letter is a separate sub-puzzle. But tangram solutions are well-documented and googlable. A solver who recognizes "this is a tangram" can look up solutions.

**Verdict: Spatial reasoning, but googlable.**

---

### X11 -- Origami Fold

| Solution standout: 2 | Brute-forceable: No | Deductive path: 2 | Checkpoints: No |

Follow fold instructions; visible surfaces show answer. This is craft (following instructions) + reveal. No deduction.

---

### X12 -- Five Senses Quintet

An organizing principle, not a puzzle. Not evaluable.

---

### X13 -- River Letters

Duplicate of 3-3 conceptually. Connect-the-dots on a map.

---

### X14 -- Mountain Range Frequency

| Solution standout: 1 | Brute-forceable: N/A | Deductive path: 1 | Checkpoints: No |

**FUNDAMENTALLY UNSOUND.** Mountain elevation profiles do not have meaningful "frequencies." Treating them as waveforms and extracting "peaks per unit distance" is numerology applied to geography. The resulting "frequencies" would be noisy, ambiguous, and would not map cleanly to musical notes. This combines the perceptual problems of 3-4 (Mountain Silhouette) with the arbitrary encoding of frequency-to-note.

---

### X15 -- Phenakistoscope / Zoetrope

| Solution standout: 2 | Brute-forceable: No | Deductive path: 1 | Checkpoints: No |

Cut, spin, view through slits. Physical spectacle. The answer is revealed by the animation, not derived by reasoning. Beautiful connection to cinema history. Zero deduction.

**Verdict: Museum exhibit, not puzzle.**

---

### X16 -- Sundial

Duplicate of 3-6. Same weather/time dependency. Fundamentally unsound.

---

### X17 -- Stereo Pair

| Solution standout: 2 | Brute-forceable: No | Deductive path: 1 | Checkpoints: No |

Cross eyes, see 3D word. Perceptual ability test, not deduction. Many people physically cannot do stereograms (10-15% of the population has insufficient stereoscopic vision). A puzzle that excludes 10-15% of humans by physiology is discriminatory, not challenging.

**Flag: Excludes solvers with vision limitations.**

---

### X Section Summary

Most X-category puzzles are physical spectacles or reveal mechanisms, not deductive puzzles. The ones with deductive content:

- **X10 (Tangram)** -- spatial reasoning but googlable
- **X8 (Punch Card)** -- if hole positions must be derived
- **X4 (Golden Ratio)** -- better as Black Joker

**No X-category puzzle is stronger than the best section-specific candidate for any slot.** The X puzzles serve best as Black Joker moments, meta payoffs, or "experience" puzzles alongside deductive ones.

---

## Fundamentally Unsound Puzzles — Reject List

These puzzles have structural flaws that cannot be fixed by better execution. They should be removed from consideration entirely.

| ID | Name | Fatal Flaw |
|----|------|------------|
| **3-4** | Mountain Silhouette | Mountain profiles do not form letter shapes. Perceptual ambiguity is maximal. |
| **3-6** | Sundial Construction | Requires specific latitude, weather, and time of day. External dependencies make it unsolvable in most conditions. |
| **X14** | Mountain Range Frequency | Numerology -- elevation profiles are not waveforms with meaningful frequencies. |
| **X16** | Sundial (duplicate) | Same as 3-6. |
| **X17** | Stereo Pair | Excludes 10-15% of population who cannot see stereograms. Not a deductive challenge. |
| **4-5** | Periodic Table Spelling | Self-acknowledged failure in the brief itself ("G isn't an element symbol"). |
| **J6** | Topology / Genus A1Z26 | Genus values (0-3) map to only A-D. Alphabet coverage is impossibly small. |
| **K5** | Binary Decoder | Binary-to-ASCII is the first thing any solver tries. No deductive content. |
| **2-2** | Food Web Traversal | "Multiple valid paths, try each against a dictionary." Anti-deductive by design. |

---

## Brute-Force Flags — Vulnerable Puzzles

These puzzles can be solved by enumeration rather than deduction. They are not fundamentally unsound but reward guessing over reasoning.

| ID | Name | Vulnerability |
|----|------|---------------|
| **9-2** | Prisoner's Dilemma | 2^5 = 32 possible binary strings. Trivially enumerable. |
| **9-4** | Market Equilibrium | Graph reading + A1Z26. The A1Z26 step is always the first guess. |
| **4-4** | Glaze Chemistry | Same: compute number + A1Z26. |
| **4-6** | Kiln Temperature | Same: read graph + A1Z26. |
| **Q7** | Fibonacci Art | Fibonacci recognition is instant for any math-literate solver; extraction unspecified. |
| **X3** | Fold the Page | Few plausible folds on a page. Enumerable. |

---

## Huang's Deductive 13

My ideal Red Joker lineup. Every puzzle has a provably clean solving path, independent confirmation checkpoints, and resistance to brute-force.

| # | Rank | Section | Puzzle | Why |
|---|------|---------|--------|-----|
| 1 | **K** | Computing | **K1 -- Cipher Decryption** | Two-step deduction (identify cipher + find key). Incremental decryption provides confirmation. K2 is arguably stronger but K1 is more tightly specified. |
| 2 | **Q** | Arts & Culture | **Q1 -- Crossword** | Crosswords have built-in deductive confirmation (crossing letters). Not inspired, but the only Q-slot candidate with a clean deductive path. The Arts pool is weak. |
| 3 | **J** | Math & Physics | **J1 -- Proof Completion** | Proof structure provides internal consistency checks. Each blank is constrained by the logical flow. Mathematical reasoning is the deductive tool. |
| 4 | **10** | Language | **10-1 -- Multi-Cipher Decoder** | Championship quality. Ten isolated sub-puzzles, each with its own aha, each independently confirmable. The encyclopedia is genuinely necessary. Best puzzle in the pool. |
| 5 | **9** | Social Sciences | **9-1 -- Logic Grid** | Pure constraint-based deduction. The gold standard of logical puzzle formats. Every placement follows from elimination. Visible progress on the grid at every step. |
| 6 | **8** | Technology | **8-2 -- Logic Gate Circuit** | Deterministic Boolean evaluation. Each gate is a verification checkpoint. Cannot be brute-forced. The solver thinks like an engineer. Displaces the current pick 8-1. |
| 7 | **7** | Mechanics | **7-1 -- Engineering Calculation** | Five machine types provide variety within one puzzle. Each calculation is independently verifiable. A1Z26 extraction is the weak link but the physics is genuinely deductive. |
| 8 | **6** | History | **6-1 -- Primary Source Detective** | Identification + chronological ordering is a two-step deduction. Each source is independently identifiable. The cascade from identification to ordering to extraction is clean. |
| 9 | **5** | Life Sciences | **5-1 -- Codon Decoding** | Perfect score. Real biochemistry as puzzle mechanism. Completely deterministic. Each codon translates independently. The section teaches the tool; the puzzle uses the tool. Best puzzle in the pool, tied with 10-1. |
| 10 | **4** | Material Culture | **4-1 -- Element Identification** | Riddle-style identification from properties. Each riddle is an independent sub-puzzle. First-letter acrostic is standard but justified by the riddle format. |
| 11 | **3** | Earth & Space | **3-1 -- Star Chart** | Multi-step: identify, plot, read. The plotting step is physical and engaging. Perceptual letter recognition is the weak link, but manageable with careful construction. |
| 12 | **2** | Natural World | **2-1 -- Organism Identification + Diagonal** | Diagonal reads are self-confirming. The identification step requires the encyclopedia. Compact (5 organisms) and elegant. |
| 13 | **A** | People | **A-1 -- Influence Chains** | Chain structure adds relational reasoning beyond simple identification. Cascading dependencies provide natural ordering. Diagonal extraction is clean. |

### Lineup Characteristics

**Mechanism diversity:** No two puzzles use the same primary mechanism.

| Mechanism | Puzzle |
|-----------|--------|
| Cipher decryption | K1 |
| Crossword | Q1 |
| Proof logic | J1 |
| Multi-encoding identification | 10-1 |
| Constraint elimination (logic grid) | 9-1 |
| Boolean circuit evaluation | 8-2 |
| Physics calculation | 7-1 |
| Source identification + chronological sort | 6-1 |
| Biological translation | 5-1 |
| Riddle identification | 4-1 |
| Celestial plotting + connect-the-dots | 3-1 |
| Organism identification + diagonal read | 2-1 |
| Influence chain tracing | A-1 |

**Confirmation checkpoints:** 13/13 puzzles have at least partial incremental confirmation. This was a 3/13 problem in the V2 design. Solved.

**Brute-force resistance:** No puzzle in the lineup is trivially brute-forceable. The strongest resistance is in 9-1 (logic grid), 8-2 (circuit), 5-1 (codons), and 10-1 (multi-cipher). The weakest is Q1 (crossword -- clues can be guessed from crossing letters), but this is inherent to crossword design and is actually a feature (it provides confirmation).

**Encyclopedia engagement:** Every puzzle requires reading the encyclopedia to solve. The strongest encyclopedia engagement is in 5-1 (must learn the genetic code), 10-1 (must learn 10 encoding systems), and 8-2 (must understand Boolean logic). The weakest is Q1 (crossword clues reference arts content, but a knowledgeable solver might answer from prior knowledge).

### Upgrade Candidates

If the Arts pool is expanded with new briefs, I would replace Q1 (Crossword) immediately. The crossword is a placeholder -- it works, but it does not sing. What the Arts slot needs is a puzzle that makes the solver think like an artist, the way 5-1 makes them think like a biologist and 8-2 makes them think like an engineer. A perspective-drawing puzzle (construct a vanishing-point scene; the vanishing point is at specific coordinates that encode the answer) could work, but it is not in the current pool.

Similarly, 7-4 (Bridge Structural Analysis) is a strong alternative to 7-1 (Engineering Calculation). The tension/compression analysis is purer constraint-based reasoning. But the binary encoding (T/C -> bits -> letters) adds a fragile layer. If the binary grouping can be made clean (e.g., exactly 8 members per span, each span = one byte), 7-4 is the stronger puzzle.

---

## Closing Assessment

The V3 pool is a dramatic improvement over V2. Moving from steganographic encodings to explicit puzzle-book format has unlocked real puzzle mechanisms: logic grids, cipher decryption, circuit evaluation, proof completion. The current starred selections (K1, J1, 10-1, 9-1, 8-1, 7-1, 6-1, 5-1, 4-1, 3-1, 2-1, A-1) are almost exactly my picks -- I change only one (8-1 -> 8-2).

The pool's primary weakness is the Arts slot, where no candidate achieves the deductive clarity of the best puzzles in other sections. The pool's primary strength is the trio of 5-1 (Codons), 10-1 (Multi-Cipher), and 9-1 (Logic Grid) -- three puzzles that would not be out of place in a championship puzzle event.

Nine of my 13 are the current starred picks. The pool has converged on the right answers through iteration. What remains is execution: specifying the exact extraction rules, verifying constructibility, and ensuring every riddle/clue/matrix uniquely determines its intended answer.

A puzzle where the intended solution stands out. That is the standard. Eleven of these 13 meet it. The Arts crossword and the Mechanics A1Z26 step are compromises I accept because the alternatives in those pools are worse. When better candidates emerge for those two slots, swap them in.

---

*Wei-Hwa Huang evaluates puzzles the way he designs sudoku variants: every step must follow from logical necessity. A puzzle that can be guessed is not a puzzle. A puzzle that can be brute-forced is not a puzzle. A puzzle where the intended path is the only path -- that is a puzzle worth solving.*
