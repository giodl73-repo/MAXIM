# Round 2 — Thomas Snyder Ranks the Puzzle Pool

**Reviewer**: Thomas Snyder (Dr. Sudoku / motris)
**Lens**: Individual puzzle craftsmanship
**Date**: 2026-02-26
**Input**: PUZZLE-POOL.md (89 briefs), TWO-JOKERS.md (two-book structure)

---

## Preface

In my first review I said the hunt had 13 encoding schemes where it needed 13 puzzles. Now I have 89 candidates to choose from — the original 13 plus 76 challengers. The pool is dramatically stronger. Several of these briefs describe genuine puzzles: intentional solving paths, thematic integration at the structural level, and cognitive modes that go beyond "find datum, map to letter."

My task: rank by craftsmanship within each section, flag anything that's "not a puzzle" (mere encoding, no deductive step, trivially computer-solvable), then select an ideal Red Joker lineup of 13 plus my top Black Joker picks.

I'm evaluating on five axes:

1. **Intentional solving path** — Does the solver make a series of deductions, or is it one insight followed by rote transcription?
2. **Thematic integration** — Is the mechanism the section's subject, or is the section just flavor text?
3. **Elegance / signal-to-noise** — Does every element serve a purpose?
4. **Anti-computer** — Could a script generate and solve this? If yes, it fails.
5. **Hand-crafted quality** — Does the constructor's hand show? Is the experience choreographed?

---

## Section-by-Section Rankings

---

### K — Computing & Software

| ID | Name | Craftsmanship | Verdict |
|----|------|:---:|---------|
| **K1** | Cipher Decryption | **4** | Strong. The solver learns a cipher from the encyclopedia and applies it. Discovery and solve are intertwined — you must understand the algorithm to use it. The key hidden in `computing/25-SECURITY.md` means the encyclopedia teaches you the tool, then tests you on it. Near-structural thematic integration. Loses a point because "decrypt ciphertext" is still fundamentally a single-mechanism extraction once you have the key — the post-key experience is mechanical. |
| **K3** | State Machine Traversal | **5** | Excellent. The solver walks a state diagram, evaluating transition conditions that require computing knowledge. This IS computation — the puzzle makes you think like a computer. Multiple transitions at each node means real branching deduction, not linear transcription. The path through the machine collects letters, so the solve and extraction are unified. This is what I asked for in round 1: an algorithm in the Algorithm section. |
| **K2** | Algorithm Execution | **4** | Good. Hand-tracing pseudocode is genuine computational thinking. The execution trace table makes the solving path visible. But pseudocode readability is fragile — one ambiguous operation and the solver is stuck without recourse. Needs careful calibration. |
| **K4** | Stack Trace / Recursion | **4** | Recursion is the most beautiful structure in computing, and tracing a call stack is a real deductive process. Each level's return value depends on the next — the solver builds understanding from the base case upward. Lovely structural metaphor: you must go deep before you can come back up. Risk: recursion depth > 5 becomes tedious to track. |
| **K5** | Binary Decoder | **2** | Encoding, not a puzzle. ASCII art made of 0s and 1s is a visual gimmick. The "decode" is looking up a table. No deductive step. A script handles this in milliseconds. |

**Top picks for K:** K3 (State Machine Traversal) is the clear winner. K1 (Cipher Decryption) is the strong backup.

**Flag — not a puzzle:** K5 (Binary Decoder).

---

### Q — Arts & Culture

| ID | Name | Craftsmanship | Verdict |
|----|------|:---:|---------|
| **Q5** | Anamorphic Drawing | **5** | This IS art. Anamorphosis is a documented art-historical technique (Holbein's skull in "The Ambassadors" is the textbook example). The solver must physically tilt the book to a severe angle — the puzzle mechanism IS the thing the section teaches. The aha is visceral: abstract streaks suddenly resolve into a word. No encoding steps, no letter mapping — the answer is literally invisible until you adopt the correct perspective. For the Arts section, whose answer word is PERSPECTIVE, this is perfection. Every element serves a purpose. |
| **Q2** | Visual Rebus | **4** | Rebuses are a legitimate puzzle form with deep history. Spatial arrangements of words representing arts concepts (vanishing-point layout = PERSPECTIVE, stacked notes = COUNTERPOINT) means the visual form IS the content. Each rebus is a mini-puzzle with its own aha. The extraction step (pull letters from solved rebuses) is clean. Loses a point because rebus puzzles are common — no novelty premium. |
| **Q6** | Golden Ratio Composition | **4** | Measuring an artwork to find phi is a beautiful intersection of art and mathematics. The solver must recognize the ratio from physical measurement — that's real deduction. Using phi as a decryption key is elegant. Risk: measurement precision on a printed page is imperfect, and tolerance issues kill physical puzzles. Must be designed so reasonable measurement error still yields the correct answer. |
| **Q3** | Musical Staff Decoder | **3** | Note names spelling words is well-trodden territory (BACH = B-flat, A, C, B-natural in German notation). Limited to letters C-D-E-F-G-A-B, which severely constrains the answer space. The solver who can read music finds this trivial; the solver who cannot must learn from `music-theory/`, which IS the point — but the actual decoding is mechanical. |
| **Q4** | Color Overlay | **3** | Physical interaction (hold pages to light) is appealing, but the puzzle reduces to "align and read." No deductive step once you realize you need to overlay. The colors connection is thematic at the surface level — you could do this with any two patterns. |
| **Q7** | Fibonacci Art Sequence | **2** | Counting elements and recognizing Fibonacci is an observation, not a deduction. Once you notice the sequence (1, 1, 2, 3, 5, 8...), the extraction is clerical. The Fibonacci connection to art is real (phyllotaxis, golden spiral) but cosmetic here — the mechanism doesn't use WHY Fibonacci appears in art, just that it's a recognizable number sequence. |
| **Q1** | Crossword (V2) | **2** | A crossword where every clue comes from the Arts section is just... a themed crossword. Competent, not distinctive. No structural thematic integration — the arts content is clue flavor, not mechanism. Any section could have a crossword. Crosswords are also the most computer-assistable puzzle form. |

**Top picks for Q:** Q5 (Anamorphic Drawing) is outstanding. Q2 (Visual Rebus) is the backup.

**Flag — not a puzzle:** Q1 (Crossword) is a puzzle, but a generic one. No structural reason it belongs in Arts.

---

### J — Mathematics & Physics

| ID | Name | Craftsmanship | Verdict |
|----|------|:---:|---------|
| **J2** | Symmetry Operations | **5** | Group theory transformations applied to a letter grid — the solver literally performs the mathematics the section teaches. Rotation, reflection, and translation are the fundamental symmetry operations, and applying them to a grid is what a crystallographer does. The overlay of transformed grids revealing the answer is elegant: the answer emerges from the mathematical structure, not from a lookup table. This is what Math/Physics should feel like. Every operation serves a purpose. |
| **J1** | Proof Completion | **4** | Completing a proof chain requires genuine mathematical reasoning — you must understand what logically follows from what. The blanks demand specific terms, and the first-letters extraction is secondary to the deductive work. The solver experiences mathematical thinking. Loses a point because "first letters of missing terms" is still an acrostic extraction at the end, and the proof must be carefully constructed so each blank has exactly one valid completion. |
| **J3** | Geometric Construction | **4** | Compass-and-straightedge is the oldest form of mathematical puzzle, and the constructions forming letter shapes is a clean payoff. The physical act of drawing makes the solving path tangible. Risk: construction instructions must be precise enough that the letter shapes emerge clearly. Imprecise drawing could make letters ambiguous. Best if each construction uses a different classical technique (perpendicular bisector, angle bisection, circle tangent). |
| **J6** | Topology Puzzle | **3** | Classifying shapes by genus is real topology, and the idea is charming. But genus → A1Z26 is a mechanical step that breaks the thematic spell. Topology is about invariants and equivalence classes — the puzzle should force topological reasoning, not just counting holes. If the classification itself were the challenge (deformable vs. not, with tricky examples), the craftsmanship would jump. As stated, it's "count holes, look up letter." |
| **J4** | Matrix Multiplication | **2** | Matrix multiplication is arithmetic, not insight. The solver multiplies numbers and decodes. A computer does this faster and without errors. No intentional solving path — just computation. The mod-26 step at the end is the same encoding crutch I flagged in round 1. |
| **J5** | Equation Balancing | **2** | "Solve for X, X is a letter" is the oldest puzzle trope in mathematics, and it's a trope for a reason — there's nothing deductive about it once you know algebra. This is homework, not a puzzle. |

**Top picks for J:** J2 (Symmetry Operations) is exceptional. J1 (Proof Completion) is the backup.

**Flag — not a puzzle:** J4 (Matrix Multiplication) and J5 (Equation Balancing) are calculation exercises, not puzzles.

---

### 10 — Language & Communication

| ID | Name | Craftsmanship | Verdict |
|----|------|:---:|---------|
| **10-1** | Multi-Cipher Decoder | **5** | Ten messages, ten encoding systems, all taught in the same encyclopedia section. This is the Language puzzle, and it's about languages — specifically, the languages of codes. The solver must identify each encoding (Morse, Braille, semaphore, pigpen, etc.) before decoding it. That identification step is real pattern recognition. The variety across ten different systems means no two decodes feel the same. The self-referential quality is perfect: the section about codes IS a coded message. First letters of decoded messages spelling INFLECTION is clean and thematically resonant. This is the puzzle I rated highest in round 1 (when it was the self-referential cipher concept), and this new version is even better because it SHOWS you ten different code systems rather than hiding one in running text. |
| **10-3** | Phonetic Riddle | **4** | IPA symbols that sound like an English phrase when spoken aloud — this is a genuine linguistic puzzle. The solver must actually pronounce the symbols, engaging with phonetics at the articulatory level. The physical requirement (say it aloud) adds a dimension most puzzles lack. The aha is auditory, not visual. Elegant. Risk: IPA literacy is genuinely rare outside linguistics. The puzzle either teaches you IPA (good — uses the encyclopedia) or assumes it (bad — gatekeeps). |
| **10-4** | Etymological Chain | **3** | Tracing a word across five languages is real historical linguistics. The chain structure (each stage requires the previous) creates a genuine solving path. But the final extraction (PIE root translated to English) is a lookup, not a deduction. The solver who can trace Modern English -> Old French -> Latin is doing interesting work; the PIE-to-answer step is flat. |
| **10-2** | Rosetta Stone | **3** | Parallel texts in three scripts is the classic decipherment challenge. The concept is strong, but in practice, "knowing one script lets you decode the others" means the solver who reads Latin script just does transliteration twice. The deductive step (using known text to crack unknown text) is real, but the difficulty depends entirely on script selection. Cyrillic is too easy (many shared letters); Arabic is too hard (different directionality, connected script). Finding the sweet spot is the construction challenge. |
| **10-5** | Cipher Wheel Construction | **3** | Building a physical tool and using it to decode — the making IS the puzzle. But a cipher wheel is a Caesar cipher with a physical interface. Once built, the decoding is mechanical rotation. The construction adds craft time, not craft thought. This belongs more in Black Joker (tool-building as meta-layer) than in a Red Joker feeder. |
| **10-6** | Semaphore / Flag Reading | **2** | Decoding semaphore is a lookup table operation. There's no deductive step — you match arm positions to letters. A child with a reference chart solves this as fast as an adult. The visual presentation (stick figures with flags) is charming but doesn't add puzzle depth. This is a component of 10-1, not a standalone puzzle. |

**Top picks for 10:** 10-1 (Multi-Cipher Decoder) is the definitive choice. 10-3 (Phonetic Riddle) is the backup.

**Flag — not a puzzle:** 10-6 (Semaphore Reading) is pure table lookup.

---

### 9 — Social Sciences

| ID | Name | Craftsmanship | Verdict |
|----|------|:---:|---------|
| **9-1** | Logic Grid | **5** | The Einstein's riddle format is one of the purest puzzle forms — pure constraint satisfaction through logical deduction. Five nations, five political systems, and the clues require understanding governance types, economic models, and legal traditions. The solver must both comprehend the social science concepts AND apply logical elimination. That dual requirement is precisely what this hunt needs: domain knowledge as puzzle infrastructure, not decoration. The grid format provides its own worksheet. The solving path is long but every step is a deduction. This is a championship-quality puzzle. |
| **9-3** | Voting Paradox | **4** | Same candidates, same voters, three different winners under three different voting systems — this is a genuinely interesting social science puzzle. The paradox itself (Arrow's impossibility theorem made tangible) IS the mechanism. The solver must understand each voting system well enough to compute the winner. The resolution of the paradox encodes the answer. This makes the solver think like a political scientist. Elegant constraint: the voting preferences are designed so the paradox is sharp and surprising. |
| **9-2** | Prisoner's Dilemma Tournament | **3** | Five rounds of game theory with payoff matrices is thematically strong. Finding the optimal strategy (dominant, Nash equilibrium) is real strategic reasoning. But mapping cooperate/defect to binary is a mechanical encoding step that drains the thematic juice. The game-theoretic insight should BE the answer, not be converted through two more encoding layers. If the optimal strategies themselves spelled something (e.g., the name of each game type contributes a letter), the integration would be tighter. |
| **9-4** | Market Equilibrium | **2** | Find where supply meets demand, read the price, map to a letter. This is graphing homework followed by A1Z26. The economic concept (equilibrium) is used as flavor for a coordinate-reading exercise. No strategic or analytical reasoning required — just reading a graph correctly. |
| **9-5** | Treaty Network | **2** | Graph theory applied to international relations is a nice cross-section idea, but "shortest path between specific nodes" or "highest-degree node" is algorithmic, not deductive. The solver is running Dijkstra's algorithm by hand, which is a Computing task wearing a Social Sciences costume. The connection to international relations is cosmetic — any network with the same structure would produce the same answer. |

**Top picks for 9:** 9-1 (Logic Grid) is the clear winner. 9-3 (Voting Paradox) is the backup.

**Flag — not a puzzle:** 9-4 (Market Equilibrium) is graph reading.

---

### 8 — Technology

| ID | Name | Craftsmanship | Verdict |
|----|------|:---:|---------|
| **8-2** | Logic Gate Circuit | **5** | Tracing a logic circuit — AND, OR, NOT, XOR gates with given inputs — is exactly what a semiconductor engineer does. The solver must understand each gate's truth table and propagate signals through the circuit. The binary output decoding to ASCII is the one encoding step, and it's thematically justified (digital circuits ARE binary). The circuit diagram is visual, the solving path is deductive (each gate's output depends on its inputs, which depend on earlier gates), and the difficulty scales naturally with circuit depth. A human evaluates this faster than they could write the code to automate it for a one-off circuit, which passes the anti-computer test for hand-crafted instances. |
| **8-1** | Signal Tracing | **4** | Tracing a signal through a system diagram with sequential transformations is real engineering thinking. Each component modifies the signal — the solver must know what each component does. This is thematically perfect for Technology. The "ASCII system diagram" format keeps it accessible. Loses a point vs. 8-2 because "signal tracing" is more abstract than logic gates — the component effects might feel arbitrary unless carefully tied to real component behavior. |
| **8-5** | PCB Trace Following | **3** | Following copper traces on a circuit board is a charming visual puzzle. The physical layout matters — traces cross, route around components, use vias. But collecting letters at components in trace order is ultimately a maze with letters. The PCB theming is cosmetic unless the trace routing itself requires technical knowledge (impedance matching, ground planes). As described, it's "follow a line, collect letters." |
| **8-3** | Frequency Spectrum | **3** | Identifying frequencies from a spectrum chart requires real signal-processing knowledge. The Hz-to-note mapping is natural (440 Hz = A4 is universal). But reading a frequency spectrum and identifying peaks is not deduction — it's measurement. The cross-section to music-theory/ is nice but doesn't add puzzle depth. |
| **8-4** | Bit Pattern / QR by Hand | **1** | A grid of black and white squares decoded as binary. This is encoding, not puzzling. A camera (or a patient human with a table) handles this with zero insight. "Simpler than QR" means even less interesting than QR. There is nothing here for a solver to deduce. |

**Top picks for 8:** 8-2 (Logic Gate Circuit) is the winner. 8-1 (Signal Tracing) is the backup.

**Flag — not a puzzle:** 8-4 (Bit Pattern / QR by Hand).

---

### 7 — Mechanics

| ID | Name | Craftsmanship | Verdict |
|----|------|:---:|---------|
| **7-1** | Engineering Calculation | **4** | Five simple machines, five calculations. The solver must understand each machine's physics (mechanical advantage, gear ratios, hydraulic pressure). The calculations are genuine mechanical engineering — not arbitrary arithmetic. Numbers mapping to A1Z26 is the weakest link, but the pre-extraction work is real domain reasoning. The five-machine variety keeps the solve from becoming repetitive. Answer word TORQUE is thematically perfect. |
| **7-4** | Bridge Structural Analysis | **4** | Tension/compression analysis of a truss is a core structural engineering skill. The solver looks at each member, identifies the force type (T or C), and the binary pattern decodes to letters. The analysis is real — you must understand free-body diagrams and load paths. The binary encoding (T=1, C=0) is natural to the domain (tension/compression is inherently binary). Clean thematic integration. Risk: a solver unfamiliar with structural analysis has no entry point. Must reference `structural/` effectively. |
| **7-3** | Rube Goldberg Chain | **3** | The visual delight of a Rube Goldberg machine is real, and identifying each mechanical principle (lever, spring, pulley, pendulum) requires domain knowledge. But "first letters of principle names" is yet another acrostic extraction. The machine drawing would be beautiful — the puzzle construction should match that ambition. Better if the solver must determine the ORDER of stages (which comes first? what triggers what?) rather than just labeling each one. |
| **7-2** | Gear Train | **3** | Calculating gear ratios from tooth counts is real mechanical engineering. RPM encoding is thematically fitting (gears ARE about speed ratios). But this is a subset of 7-1 (Engineering Calculation) — it's one of the five machines, stretched into a standalone puzzle. Less varied, more repetitive. Monotonic "calculate, convert, next" solving path. |
| **7-5** | Fluid Flow Path | **3** | Pipe network with pressure/diameter calculations determining flow direction is a genuine engineering challenge. The maze-like quality (which branch does the fluid take?) adds deductive structure. But the calculations at each junction are independent — the solver doesn't build understanding across the network. Good concept, needs deeper interconnection between junctions. |

**Top picks for 7:** 7-1 (Engineering Calculation) for breadth and variety. 7-4 (Bridge Structural Analysis) is the backup — tighter thematic integration, narrower scope.

---

### 6 — History & Ideas

| ID | Name | Craftsmanship | Verdict |
|----|------|:---:|---------|
| **6-1** | Primary Source Detective | **5** | Identifying historical documents from their opening lines is genuine scholarly detective work. The solver must recognize prose style, period vocabulary, and ideological content. Chronological ordering adds a secondary deduction layer. Extraction from author names is clean. This puzzle makes the solver think like a historian — "who wrote this, and when?" is the fundamental question of the discipline. Eight documents means eight aha moments, each testing different historical knowledge. The constructor's hand shows in document selection: each quote must be identifiable but not obvious, and the chronological order must produce a valid extraction. PARADIGM is a perfect answer for this section (Kuhn's "paradigm shift" is the section's own subject). |
| **6-3** | Philosophical Argument Chain | **4** | Identifying valid deductions vs. fallacies in a multi-step argument is genuine philosophical reasoning. The binary encoding (valid=1, fallacy=0) is natural — logic IS binary. The solver must know their fallacies (ad hominem, straw man, affirming the consequent) from `philosophy/` and `logic/`. The argument chain structure creates a solving path: each step builds on the previous, so a misidentification early on doesn't just produce a wrong letter — it changes the entire argument's trajectory. Needs careful construction: each fallacy must be identifiable to a careful reader but not screaming. |
| **6-5** | Fairy Tale Logic | **3** | A narrative logic puzzle wrapped in mythological framing is charming. The "sage crossing rivers with tribute" format has deep roots (river-crossing puzzles date to Alcuin of York, 8th century). Constraints from mythology/ and religious-studies/ add flavor. But the narrative wrapper risks obscuring the logical structure. If the solver has to decode the fairy-tale language to find the logic puzzle underneath, that's a translation step, not a puzzle step. Best if the mythological content IS the constraint (e.g., "the fire god's bridge cannot bear water; the sea god's bridge cannot bear metal" — the tributes must match the mythology). |
| **6-2** | Historical Map Overlay | **3** | Boundary changes forming letter shapes is a nice visual idea, and the physical overlay mechanic is engaging. But the letter formation depends entirely on historical geography cooperating — do the actual boundary changes between, say, 1648 and 1815 form recognizable letters? If you're designing fictional maps, you've lost the historical connection. If you're using real maps, you're at the mercy of cartography. High risk of the concept being unbuildable with real geography. |
| **6-4** | Cause-and-Effect Web | **2** | "Trace the longest causal chain" is a graph traversal problem. The historical content provides the edges, but the solving mechanism (longest path in a DAG) is algorithmic, not historical. A solver who understands graph theory but knows no history could solve this. The extraction (letters from events on the path) is mechanical. |

**Top picks for 6:** 6-1 (Primary Source Detective) is outstanding. 6-3 (Philosophical Argument Chain) is the backup.

---

### 5 — Life Sciences

| ID | Name | Craftsmanship | Verdict |
|----|------|:---:|---------|
| **5-1** | Codon Decoding | **5** | I gave this a 4 in round 1 for the concept. The pool version has tightened: DNA -> mRNA -> codons -> amino acids -> single-letter codes -> GENETIC. The answer word is buildable entirely within the amino acid alphabet (G, E, N, E, T, I, C — all valid single-letter amino acid codes). That solves the constraint I flagged. The mechanism IS molecular biology — the solver performs transcription and translation, the central dogma of the discipline. This is the most thematically integrated puzzle in the entire pool. The encyclopedia teaches you the genetic code; the puzzle is written in it. Every element serves exactly one purpose. Score: 30/30 in the original V3 ranking is earned. |
| **5-2** | Phylogenetic Tree Traversal | **4** | Walking a phylogenetic tree and identifying common ancestors at branch points is real evolutionary biology. The tree structure creates a natural solving path (root to leaf, or leaf to leaf via common ancestor). The visual diagram is the kind of thing a biologist actually works with. Each branch point requiring identification of a key trait means the solver engages with evolutionary concepts at every step. Clean. Risk: the tree must be carefully designed so branch-point identifications are unambiguous. |
| **5-6** | Epidemic Network | **3** | Tracing disease spread through a population network using transmission rules is real epidemiology. The constraint that "only one path spells a real word" adds a deductive layer — the solver must find the biologically valid AND linguistically valid path. Cross-cutting between biology and graph theory. But "infected individuals' initials in order" is still a collect-letters-along-a-path extraction. |
| **5-3** | Metabolic Pathway | **2** | First letters of metabolic intermediates in pathway order. This is a biology-themed acrostic. The solver either knows the pathway or looks it up, then reads first letters. No deductive step. The pathway order is fixed by biochemistry — there's nothing for the solver to figure out. |
| **5-4** | Punnett Square Genetics | **2** | Calculate phenotype ratios, map to numbers, map to letters. Three encoding layers between the biology and the answer. The genetic crosses are real, but the ratio-to-number-to-letter chain is mechanical encoding. The solver isn't thinking genetically after the first step. |
| **5-5** | Cell Organelle Labeling | **2** | Label a cell diagram, read first letters clockwise. This is a fill-in-the-blank biology worksheet, not a puzzle. The "clockwise" reading direction is arbitrary. No deductive structure. |

**Top picks for 5:** 5-1 (Codon Decoding) is the pinnacle. 5-2 (Phylogenetic Tree Traversal) is the backup.

**Flag — not a puzzle:** 5-5 (Cell Organelle Labeling) is a worksheet. 5-3 (Metabolic Pathway) is an acrostic.

---

### 4 — Material Culture

| ID | Name | Craftsmanship | Verdict |
|----|------|:---:|---------|
| **4-1** | Element Identification | **4** | Seven riddle-clues about elements, each requiring the solver to identify from material properties. The riddle format means each element is a mini-puzzle — you must synthesize multiple clues (luster, conductivity, historical use, malleability) to pin down the element. First letters spelling CASTING is clean and thematically resonant. The elements chosen (Carbon, Aluminum, Silver, Tin, Iron, Nickel, Gold) are the foundational materials of material culture. This is what I flagged in round 1: elements that are genuinely the signature elements for their materials, chosen because they're RIGHT, not because their letters cooperate. The craft is in the riddles — each one should have one path to the answer, and the path should teach you something about the material. |
| **4-2** | Craft Process Ordering | **3** | Ordering craft steps correctly requires domain knowledge (you must know that smelting precedes casting, that annealing follows cold-working). The sequence-as-puzzle is clean. But "extraction from step names" is vague — the brief doesn't specify the mechanism. If it's first letters of correctly ordered steps, it's another acrostic. If the ORDER itself encodes (step 1 is the Nth process alphabetically, N = letter), it's more interesting. Needs mechanism commitment. |
| **4-3** | Textile Pattern Binary | **3** | Over/under = 1/0 in a weaving draft is thematically perfect — weaving IS binary. The visual grid is what a weaver actually reads. But binary-to-ASCII is the same encoding used in K5, 8-4, and half the Technology puzzles. The weaving framing is lovely; the actual solving is generic decoding. Better if the weaving pattern also produces a recognizable fabric pattern (twill, satin, plain weave) that IS the answer, rather than encoding letters through binary. |
| **4-5** | Periodic Table Spelling | **2** | Spelling words with element symbols (Ca + S + Ti + N + G) is a well-known recreational chemistry exercise. It's been done thousands of times — periodic table word puzzles are a genre unto themselves. No novelty, no deductive step beyond "look up element symbols." The brief itself admits CASTING doesn't work (there's no element G). Not a puzzle; it's a constraint-satisfaction lookup. |
| **4-4** | Glaze Chemistry | **2** | Balance oxide ratios, simplify to integers, A1Z26. This is stoichiometry homework with a letter conversion at the end. The ceramic connection is cosmetic — any set of ratios would produce the same solving experience. |
| **4-6** | Kiln Temperature Profile | **2** | Read peak temperatures from a graph, A1Z26. This is the same mechanism as 9-4 (Market Equilibrium) and 8-3 (Frequency Spectrum) — read a number from a chart, convert to a letter. Graph reading is not puzzle solving. |

**Top picks for 4:** 4-1 (Element Identification) is the winner. 4-2 (Craft Process Ordering) is the backup if given a committed mechanism.

**Flag — not a puzzle:** 4-5 (Periodic Table Spelling) is a recreational exercise. 4-4 and 4-6 are A1Z26 with flavor text.

---

### 3 — Earth & Space

| ID | Name | Craftsmanship | Verdict |
|----|------|:---:|---------|
| **3-1** | Connect-the-Dots Star Chart | **5** | This is the puzzle I want to champion. Seven groups of celestial objects described poetically. Identify each object, plot it on a coordinate grid, and each group traces a letter. The physical act of drawing on the page — the "Chicago Fire" moment — makes this unforgettable. The identification step requires real astronomical knowledge (from the encyclopedia). The plotting requires spatial reasoning. The letter-tracing payoff is visual and surprising. This is a puzzle with three distinct cognitive phases (identify, plot, perceive), none of which is mechanical. The answer EQUINOX is thematically perfect. The poetic descriptions of celestial objects are where the constructor's hand shows — each must be evocative enough to be solvable, precise enough to be unambiguous, and beautiful enough to feel like the section earned its puzzle. This is hand-crafted in the deepest sense. |
| **3-5** | Tectonic Plate Jigsaw | **4** | A physical jigsaw where the pieces are tectonic plates and the assembled shape is Pangaea. Letters on plate edges that align when assembled correctly — the puzzle is the assembly, the answer is the reward. The continental drift connection is structurally thematic (the section is ABOUT plates fitting together). The physical manipulation is engaging. Risk: simplified plate shapes may make the jigsaw too easy (there's only one way Pangaea goes together), and cutting pieces from a book is destructive. |
| **3-2** | Geological Cross-Section | **3** | Reading rock layers and finding hidden words in strata names is a decent word-search variant with geological theming. The visual diagram is what a geologist actually interprets. But "certain letters at specific depths" needs more mechanism specificity — how does the solver know WHICH letters? If it's "the letter at the depth in meters, mod 26," we're back to numerology. If it's "the strata name hidden within is an answer word," that's a word search, which is a legitimate puzzle form but not a crafted one. |
| **3-4** | Mountain Silhouette | **3** | Skyline profiles as letter shapes is visually clever. The "aha" of recognizing a familiar mountain range's profile as a letter is satisfying. But this depends entirely on real mountain ranges cooperating — does the Himalayas' profile look like any letter? The Alps? If you're designing fictional skylines to look like letters, the mountain connection is cosmetic. If you're using real profiles, you need 7+ ranges that happen to look like letters. Likely unbuildable with real geography. |
| **3-3** | River Confluence Map | **2** | Plot points on a map, connect, read letter shapes. This is connect-the-dots with geographic flavor. The "trade route order" connection adds one deductive step (which river is longest?), but the core mechanism — connecting points to form letters — is the same as 3-1 (Star Chart) without the poetry, the multi-phase solving, or the celestial identification. A lesser version of a better puzzle. |
| **3-6** | Sundial Construction | **2** | Build a paper sundial, read a shadow at a specific time. The physical construction is cool, but "the shadow falls on a letter" is one bit of information. The entire puzzle yields a single letter. That's a component of a puzzle, not a puzzle. Also requires actual sunlight, which is a hard environmental dependency. |

**Top picks for 3:** 3-1 (Connect-the-Dots Star Chart) is the standout. 3-5 (Tectonic Plate Jigsaw) is the backup.

---

### 2 — Natural World

| ID | Name | Craftsmanship | Verdict |
|----|------|:---:|---------|
| **2-3** | Leaf / Mushroom Identification Key | **4** | A dichotomous key is the naturalist's fundamental tool — binary choices leading to classification. The solver must observe specimen illustrations and make identification decisions (smooth vs. serrated, gilled vs. pored). Each binary choice in the key is a micro-deduction. The branching structure means each specimen follows a unique path. Classifications encoding letters is clean. This makes the solver think like a field biologist. The visual component (specimen illustrations) adds craft. This is what naturalism IS. |
| **2-2** | Food Web Traversal | **3** | Tracing energy through a food web with the constraint that "only one path spells a real word" is a nice combination of ecology and word puzzling. The solver must explore multiple paths, which creates real deduction (dead-end paths are informative). The food web diagram is visually engaging. But the word constraint feels imposed rather than emergent — the web is designed backward from the answer word, which means the ecology is subservient to the letter needs. |
| **2-1** | Organism Identification + Diagonal | **3** | Identifying organisms from characteristics is real natural history. The diagonal read across common names is a legitimate extraction. But 5 organisms with a constrained diagonal is highly restrictive — the constructor must choose species primarily for their letter positions, not for their representativeness. Every unnatural species choice is visible to a knowledgeable solver. NICHE (5 letters) is short enough to be buildable. Serviceable, not inspired. |
| **2-4** | Birdsong as Morse | **3** | Spectrogram patterns as Morse code is a creative cross-domain connection. Long notes = dashes, short notes = dots is natural. The visual spectrograms are beautiful. But once you recognize the Morse pattern, decoding is mechanical. The ornithology connection is in the framing (birdsong), not in the solving (Morse lookup). A solver who knows Morse but nothing about birds solves this just as easily. |
| **2-5** | Spice Route | **2** | Identify spices, plot origins, connect points to form letters. This is 3-3 (River Confluence Map) in a different costume. Plot points, connect, read shapes. The spice identification step adds one layer of deduction, but the map-drawing payoff is the same connect-the-dots mechanism used in three other puzzles. Too many puzzles in this pool draw lines on maps to form letters. |

**Top picks for 2:** 2-3 (Dichotomous Key) is the winner — the mechanism IS the discipline. 2-2 (Food Web) is the backup.

---

### A — People

| ID | Name | Craftsmanship | Verdict |
|----|------|:---:|---------|
| **A-1** | Influence Chains | **5** | "Who taught whom" is the fundamental question of intellectual history. Tracing chains of influence — teacher to student, mentor to protege, correspondent to correspondent — requires knowing not just who these people were but how they connected. The chain gives the extraction order, so the solving path IS the section's subject. Letters extracted from names by position-in-chain is clean. POLYMATH as the answer word is perfect for a section that spans mathematicians, physicists, engineers, artists, and writers. The constructor's craft shows in the chain selection: each link must be historically real, intellectually significant, and extractively cooperative. This is a puzzle about connections between minds, which is exactly what the People section is about. |
| **A-5** | Invention Dependency Chain | **4** | A dependency graph of inventions, each requiring a prior one. The critical-path tracing is genuine engineering reasoning (this is how project management works: identify dependencies, find the critical path). Inventor names encoding the answer ties people to their contributions. Similar structure to A-1 but narrower focus (engineers and inventors only). Loses a point for covering only a subset of the People section's scope. |
| **A-4** | Letter Exchange | **3** | Real historical correspondence (Einstein-Born, Darwin-Hooker, Adams-Jefferson) as puzzle material is wonderful source material. But "key words extracted from each letter" is underspecified — what makes a word "key"? If the constructor highlights the words, it's a highlighting exercise. If the solver must identify them, the identification criterion is the real puzzle, and it's undefined here. Needs mechanism commitment. |
| **A-2** | Portrait Gallery | **3** | Identifying people from achievements (not names) is a quiz, not a puzzle. Initials spelling the answer is an acrostic. No deductive structure beyond "who did this?" The quiz format means each identification is independent — no cumulative insight, no building understanding across the solve. |
| **A-3** | Timeline of Overlapping Lives | **2** | Finding overlapping lifetimes is date arithmetic. The "connection word" encoding is vague — what makes two overlapping figures share a "connection word"? If it's subjective ("both were Enlightenment thinkers"), the puzzle is unsolvable. If it's objective ("both studied at the same university"), it's trivia. The mechanism doesn't cohere. |

**Top picks for A:** A-1 (Influence Chains) is the clear winner. A-5 (Invention Dependency Chain) is the backup.

---

## Cross-Section, Visual, and Physical Puzzles (X1-X17)

This is the section you specifically asked me to evaluate for genuine puzzle depth vs. gimmickry. I'll be direct.

### The Genuine Puzzles

| ID | Name | Score | Assessment |
|----|------|:---:|-----------|
| **X8** | Punch Card Overlay | **4** | Real puzzle depth. The solver must decide WHERE to punch — the marked positions on the page create a stencil. When overlaid on a text page, specific words appear. The craft is in the text page: the visible words must form a coherent message while the full text reads naturally. Two layers of intentional construction. The physical act of punching holes is irreversible, which adds stakes. The connection to early computing (actual punch cards) is structurally thematic. |
| **X10** | Tangram Letter Assembly | **4** | Tangrams are a legitimate spatial reasoning puzzle. Forming specific shapes from fixed pieces requires genuine geometric insight — you can't brute-force tangram solutions easily. If each target shape is a letter, and the letters spell an answer, you have multiple spatial puzzles with a unified payoff. The physical manipulation (cut and arrange) is engaging. Historical connection to games-history/ is structurally relevant. Risk: standard tangram letter solutions are well-documented online. Must use custom piece sets to prevent lookup. |
| **X7** | Cipher Wheel Construction | **3** | Building a tool to solve a puzzle is meta-satisfying. The physical construction (cut, pin, rotate) is engaging. But once built, the cipher wheel performs a Caesar shift — the decoding is mechanical rotation. The tool-building is the aha; the tool-using is rote. Better as a component of a larger puzzle (e.g., the Language section's multi-cipher) than as a standalone. |
| **X4** | Golden Ratio Spiral | **3** | Finding phi across four sections (art, nature, music, math) is a beautiful cross-section idea. The solver must recognize the same constant in four different guises — that's genuine pattern recognition. But using phi as a decryption key is the weakest link: what cipher uses an irrational number as its key? The recognition of phi is the puzzle; the decryption should be the payoff, and it needs a mechanism that's as elegant as the recognition. |

### The Gimmicks (Spectacle Without Puzzle Depth)

| ID | Name | Score | Assessment |
|----|------|:---:|-----------|
| **X1** | Paper + Light (Raiders) | **2** | The spectacle is undeniable — folding a 3D shape and reading shadows is theatrical. But where is the PUZZLE? The solver follows cut-and-fold instructions, holds up a flashlight, and reads letters. There is no deductive step. The construction is the experience, but construction from instructions is craft, not puzzling. This is a party trick, not a puzzle. It's the moment everyone remembers — but they remember the spectacle, not the solving. Use it as the meta PAYOFF (the reward for solving, not the puzzle itself) and it's perfect. Use it as a puzzle and you've mistaken spectacle for substance. |
| **X2** | Color Overlay | **2** | Hold pages to light, read the combined pattern. One physical action, one reading. No deduction. The "puzzle" is knowing to overlay the pages, which is an instruction, not an insight. Once you do it, the answer is literally visible. This is a reveal mechanism, not a puzzle mechanism. |
| **X3** | Fold the Page | **2** | Fold at a specific crease, letters align. Same issue as X2: one physical action, one reading. The fold is either obvious (crease mark) or arbitrary (why fold HERE?). No solving path. |
| **X9** | Mirror Puzzle | **2** | Mirror-reversed text is a single-mechanism trick. The solver either has a mirror or doesn't. With a mirror, instant solution. Without, they can read it backward with moderate effort. No deductive depth. The da Vinci connection is charming but cosmetic. |
| **X11** | Origami Fold | **2** | Follow fold instructions, read visible letters. Same structure as X1 without the flashlight drama. The origami is the experience; the puzzle is absent. |
| **X15** | Phenakistoscope / Zoetrope | **2** | Maximum novelty, minimum puzzle depth. Cut, spin, read animated word. The animation is delightful — but it's a reveal, not a solve. The cinema-film/ connection is structurally perfect, which makes it agonizing that there's no puzzle in it. Could be elevated: if the animation shows a CLUE (not the answer directly) that requires interpretation, you add a deductive layer. |
| **X17** | Stereo Pair | **2** | Cross your eyes, see a hidden word. The 3D effect is a perceptual trick. No deduction, no solving path. The word appears or it doesn't. Some people physically cannot do stereograms. Accessibility concern on top of depth concern. |

### The Structural Ideas (Not Standalone Puzzles)

| ID | Name | Score | Assessment |
|----|------|:---:|-----------|
| **X5** | Fibonacci Structural Sequence | **n/a** | This isn't a puzzle — it's a meta-structural principle. If the 13 Red Joker puzzles have Fibonacci-many elements, that's an elegant hidden layer. But the solver who notices it gets... what? Recognition? A warm feeling? If noticing the Fibonacci structure is required for the meta, it's a legitimate meta-layer. If it's purely decorative, it's a constructor vanity. Worth pursuing ONLY if it feeds the meta. |
| **X12** | Five Senses Quintet | **n/a** | An organizing principle, not a puzzle. "Five puzzles, each engaging a different sense" is an excellent design constraint for selecting which 13 puzzles to include. It should inform selection, not BE a selection. |
| **X6** | Musical Score Message | **n/a** | This is Q3 (Musical Staff Decoder) relisted in the cross-section pool. Same puzzle, same limitations (only notes C-G, A-B). Score it once. |
| **X13** | River Letters | **n/a** | This is 3-3 (River Confluence Map) relisted. Same connect-points-on-map mechanism. Score it once. |
| **X14** | Mountain Range Frequency | **n/a** | This is 3-4 (Mountain Silhouette) with a signal-processing layer added. The frequency interpretation doesn't add puzzle depth — it adds an encoding layer. Score 3-4 instead. |
| **X16** | Sundial | **n/a** | This is 3-6 relisted. Same mechanism, same limitations. |

### Summary of Physical/Visual Assessment

**Genuine puzzle depth:** X8 (Punch Card), X10 (Tangrams)
**Genuine cross-section concept:** X4 (Golden Ratio Spiral)
**Useful as tool/component:** X7 (Cipher Wheel)
**Spectacle without puzzle:** X1, X2, X3, X9, X11, X15, X17
**Structural principle, not puzzle:** X5, X12
**Duplicates of section puzzles:** X6, X13, X14, X16

My verdict: most of the X-series confuses physicality with puzzle depth. A physical interaction is not a puzzle. A puzzle is a sequence of deductions. Physical interactions are DELIVERY MECHANISMS for puzzles — they can make a good puzzle great, but they cannot make a non-puzzle into a puzzle. X8 and X10 succeed because they embed real spatial/logical reasoning inside the physical interaction. The others are reveals — one action, one reading, done.

---

## "Not a Puzzle" Flag Summary

These briefs describe encoding schemes, lookup exercises, or reveals with no deductive step. A script could generate and solve them. They should not appear in either Joker book:

| ID | Name | Why It Fails |
|----|------|-------------|
| K5 | Binary Decoder | Table lookup. No deduction. |
| Q1 | Crossword (V2) | Generic themed crossword. No structural thematic connection. |
| J4 | Matrix Multiplication | Arithmetic exercise. Computer-trivial. |
| J5 | Equation Balancing | Homework, not a puzzle. |
| 10-6 | Semaphore / Flag Reading | Pure lookup table. |
| 9-4 | Market Equilibrium | Graph reading + A1Z26. |
| 8-4 | Bit Pattern / QR | Binary decoding. Zero insight. |
| 5-5 | Cell Organelle Labeling | Labeled worksheet. |
| 5-3 | Metabolic Pathway | Acrostic from a fixed sequence. |
| 4-5 | Periodic Table Spelling | Recreational chemistry exercise. Done thousands of times. |
| 4-4 | Glaze Chemistry | Stoichiometry + A1Z26. |
| 4-6 | Kiln Temperature Profile | Graph reading + A1Z26. |
| 3-6 | Sundial Construction | One-letter yield. Environmental dependency. |
| A-3 | Timeline of Overlapping Lives | Date arithmetic. Vague mechanism. |

That's 14 of 89 briefs that I'd remove from consideration entirely. Another 15-20 are functional but undistinguished (scored 2). The remaining ~55 are genuine puzzle candidates at varying levels of craft.

---

## Snyder's Championship 13 — Red Joker Lineup

My ideal Red Joker, selecting one puzzle per section to maximize craft diversity, thematic integration, and solving-path variety:

| Rank | Section | Puzzle | Score | Cognitive Mode | Why |
|------|---------|--------|:---:|----------------|-----|
| **K** | Computing & Software | **K3 — State Machine Traversal** | 5 | Algorithmic execution | The solver IS a computer. Walk the state machine, evaluate conditions. Computing's own subject IS the puzzle mechanism. |
| **Q** | Arts & Culture | **Q5 — Anamorphic Drawing** | 5 | Perceptual / physical | The solver must adopt the correct perspective — literally. Art history's own technique IS the puzzle. The answer (PERSPECTIVE) is built into the mechanism. Visceral aha when the streaks resolve. |
| **J** | Math & Physics | **J2 — Symmetry Operations** | 5 | Spatial / algebraic | Apply group theory transforms to a grid. The mathematics IS the mechanism. The overlay payoff is visual and mathematical simultaneously. |
| **10** | Language & Communication | **10-1 — Multi-Cipher Decoder** | 5 | Pattern recognition / polyglot | Ten encoding systems, ten decodings. The section about codes IS coded. Maximum variety within a single puzzle. INFLECTION is thematically perfect. |
| **9** | Social Sciences | **9-1 — Logic Grid** | 5 | Constraint satisfaction / deduction | Einstein's riddle with governance, economics, and law. Pure logic. The longest intentional solving path in the hunt. Every step is a deduction. |
| **8** | Technology | **8-2 — Logic Gate Circuit** | 5 | Signal propagation / Boolean | Trace a circuit, evaluate gates, decode binary output. The solver thinks like a chip. The section's subject is the mechanism. |
| **7** | Mechanics | **7-1 — Engineering Calculation** | 4 | Applied physics / calculation | Five machines, five genuine engineering calculations. Breadth across mechanical principles. TORQUE is thematically perfect. |
| **6** | History & Ideas | **6-1 — Primary Source Detective** | 5 | Scholarly identification / chronology | Identify documents from opening lines. Think like a historian. The craft is in the quote selection. PARADIGM is structurally resonant. |
| **5** | Life Sciences | **5-1 — Codon Decoding** | 5 | Molecular biology / translation | DNA -> protein using the genetic code. The central dogma IS the mechanism. The most thematically integrated puzzle in the pool. |
| **4** | Material Culture | **4-1 — Element Identification** | 4 | Riddle solving / materials science | Seven riddle-clues, seven elements. Each riddle is a micro-deduction. CASTING is thematically resonant. The elements are RIGHT (not forced). |
| **3** | Earth & Space | **3-1 — Connect-the-Dots Star Chart** | 5 | Astronomical identification / spatial | Three phases: identify, plot, perceive. The physical drawing moment is the hunt's emotional peak. EQUINOX is perfect. |
| **2** | Natural World | **2-3 — Dichotomous Key** | 4 | Observation / classification | Binary branching decisions on specimen illustrations. The naturalist's fundamental tool IS the puzzle. The solver thinks like a field biologist. |
| **A** | People | **A-1 — Influence Chains** | 5 | Intellectual history / chain tracing | Who taught whom? The section about connections between minds IS a connection puzzle. POLYMATH is the perfect answer for a cross-disciplinary section. |

### Lineup Statistics

- **Average craftsmanship: 4.69 / 5**
- **Puzzles scoring 5: 9 of 13**
- **Distinct cognitive modes: 13** (no two puzzles demand the same kind of thinking)
- **Thematic integration: structural in all 13** (every mechanism IS the section's subject)
- **Anti-computer: all 13 pass** (none are trivially scriptable in their hand-crafted form)
- **Physical/visual variety: 1 physical (Q5 anamorphic), 1 draw-on-page (3-1 star chart), 1 visual circuit (8-2), 10 paper-and-pen logic**

### Why This Lineup Works

The 13 puzzles span 13 genuinely different cognitive modes. No two puzzles feel the same. The solver who finishes all 13 has thought like a computer scientist, an artist, a mathematician, a linguist, a political scientist, an engineer, a mechanic, a historian, a molecular biologist, a materials scientist, an astronomer, a naturalist, and an intellectual historian. That's the promise of the encyclopedia delivered through puzzles.

Every puzzle has at minimum two phases: a discovery/identification phase and a deductive/execution phase. None of them are "find signal, apply mapping, concatenate." The solving PATHS are the puzzles, not the encoding schemes.

---

## Top 3 for Black Joker

The Black Joker demands cross-section synthesis. These puzzles must force the solver to connect ideas across multiple sections. From the pool and the TWO-JOKERS.md structure:

### 1. X4 — Golden Ratio Spiral (reimagined as "The Spectrum")

**Sections spanned:** Arts + Mathematics + Natural World + Physics
**Why it's #1:** Phi appears in art (golden rectangles in composition), mathematics (Fibonacci ratios converging to phi), nature (phyllotaxis in sunflowers, nautilus shells), and physics (Penrose tilings, quasicrystals). Finding the SAME constant in four different guises is exactly the kind of cross-section synthesis the Black Joker promises. The solver must recognize phi in four different representations — visual, numerical, biological, physical — and use the recognition to unlock a final message. The "one phenomenon, four manifestations" structure maps perfectly to Black Joker Puzzle 4 ("The Spectrum"). The deductive step I'd add: phi doesn't just decrypt a message — the four manifestations of phi, when understood together, reveal WHY phi appears everywhere (it's the most irrational number, the slowest to converge via continued fractions, the optimal packing ratio). The answer should be a word that captures that insight.

### 2. 6-3 adapted — "The Debate" (Philosophical Argument Chain across History + Philosophy + Social Sciences)

**Sections spanned:** History & Ideas + Social Sciences + Philosophy
**Why it's #2:** Reconstruct both sides of a real intellectual debate — say, the Hobbes-Locke debate on the state of nature, or the Hayek-Keynes debate on economic planning. Each side draws evidence from different sections. The solver must understand both positions well enough to identify which claims belong to which side, and the sorting of claims reveals the answer. This makes the solver think as a genuine intellectual historian: not just "what happened" but "what did people argue about, and why?" The argument chain format (valid steps vs. fallacies) from 6-3 gives it deductive structure. The cross-section requirement (claims come from History, Philosophy, AND Social Sciences) ensures synthesis.

### 3. Black Joker Puzzle 2 — "The Chain" (Material journey from mineral to craft)

**Sections spanned:** Material Culture + Earth & Space + Natural World
**Why it's #3:** A material's journey from mineral deposit (geology) through extraction (mining, chemistry) to finished craft object (metalworking, ceramics, textiles) crosses three sections naturally. The solver traces the journey using knowledge from all three. The chain structure creates a natural solving path where each step requires a different section's knowledge. This is the kind of cross-section puzzle that makes you realize the encyclopedia's sections are artificial boundaries — in reality, a bronze statue is geology + chemistry + metallurgy + art in one object. The answer word should capture transformation itself.

---

## Closing Thoughts

The pool is dramatically better than the round-1 set. Where the original 13 were encoding schemes with thematic paint, the best candidates in this pool are puzzles whose mechanisms ARE their sections' subjects. That's the standard. A puzzle about computing should require computation. A puzzle about art should require seeing. A puzzle about biology should require thinking biologically. When the mechanism and the subject are the same thing, you get the kind of structural elegance that separates championship puzzles from competent ones.

My 13 all pass that test. The 14 briefs I flagged as "not puzzles" all fail it. The difference is not difficulty or cleverness — it's whether the solver engages with the DISCIPLINE or just with an encoding layer draped over it.

One final concern: the X-series physical puzzles. You asked me specifically about these, and I think the temptation is to include too many. Physical interaction is not puzzle depth. A flashlight, a mirror, a fold — these are delivery mechanisms, not puzzles. I've included exactly one physical puzzle in my 13 (Q5, Anamorphic Drawing) and one draw-on-the-page puzzle (3-1, Star Chart). That's the right density. Use physical spectacle for the meta payoff (X1, Paper + Light, is PERFECT for this — the reward for solving all 13, not a feeder itself). Save the theatrics for the moment they've earned.

Build these 13. Build them by hand. Test every solving path. Make every element earn its place. You have the right candidates. Now the craft is in the construction.

*-- Thomas Snyder, February 2026*
