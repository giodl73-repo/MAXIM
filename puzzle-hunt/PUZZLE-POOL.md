# Puzzle Pool — All Candidates for Panel Ranking

Every puzzle idea generated across all brainstorm sessions. Organized by section, then cross-section/visual/physical. The panel will rank them and we'll select the best 13 for Red Joker + best for Black Joker.

Each brief: name, one-line pitch, mechanism, section fit, answer word (if designed).

★ = current V3 selection. Everything else is a challenger.

---

## K — Computing & Software

### K1 ★ Cipher Decryption
**Pitch:** Decrypt a message using an algorithm the encyclopedia teaches you.
**Mechanism:** Joker gives ciphertext. Solver learns a cipher from `cryptography/`, finds the key in `computing/25-SECURITY.md`, decrypts. Plaintext leads to answer.
**Worksheet:** Decryption grid (ciphertext, key, shift, plaintext columns).
**Answer:** ALGORITHM
**V3 score:** 29/30

### K2 — Algorithm Execution
**Pitch:** Execute pseudocode by hand — the output IS the answer.
**Mechanism:** Joker gives a short pseudocode program (loop, conditional, string operations). Solver traces execution step by step using computing concepts. Final output string is the answer word.
**Worksheet:** Execution trace table (step, variable state, output).
**Connection:** computing/ (algorithms, data structures)

### K3 — State Machine Traversal
**Pitch:** Follow a state machine diagram — the path through it spells a word.
**Mechanism:** ASCII state diagram with labeled transitions. Each transition has a condition the solver must evaluate (requires reading computing/ content). Valid path through the machine collects letters.
**Worksheet:** State diagram with path-tracking blanks.

### K4 — Stack Trace / Recursion
**Pitch:** Trace a recursive function — return values at each level encode letters.
**Mechanism:** A recursive function definition that references CS concepts. Solver traces the call stack, computes return values. Values map to letters.
**Worksheet:** Call stack diagram with return value blanks.

### K5 — Binary Decoder
**Pitch:** An ASCII art image contains binary — decode it to read the answer.
**Mechanism:** A visual pattern of 0s and 1s that forms a picture (like ASCII art). The binary values, read in order, decode to ASCII text.
**Worksheet:** Binary grouping brackets + ASCII conversion table.

---

## Q — Arts & Culture

### Q1 — Crossword (V2 design)
**Pitch:** A crossword where every clue comes from the Arts section.
**Mechanism:** Standard crossword, clues reference art-history/, music-theory/, architecture/, etc. Highlighted cells spell answer.
**Answer:** PERSPECTIVE
**V3 score:** 25/30 (current floor — needs upgrade)

### Q2 — Visual Rebus
**Pitch:** A page of visual word puzzles representing arts concepts.
**Mechanism:** Spatial arrangements of words/letters represent terms from the Arts section. Each solved rebus is an arts concept. Extracted letters spell the answer.
**Example:** Letters arranged in vanishing-point perspective → PERSPECTIVE. Musical notes stacked vertically → COUNTERPOINT.
**Worksheet:** Rebus images with identification blanks + extraction row.

### Q3 — Musical Staff Decoder
**Pitch:** Read the notes — they spell a message.
**Mechanism:** A musical staff with specific notes. Note names (CDEFGAB) spell words directly. Solver must read music notation (taught in `music-theory/`). The melody, when notes are named, gives the answer or a cluephrase.
**Worksheet:** Staff with note-naming blanks beneath each note.
**Connection:** music-theory/, directly self-referential

### Q4 — Color Overlay
**Pitch:** Overlay two pages — the intersection reveals a hidden word.
**Mechanism:** Two pages with colored patterns (red and blue). When held up to light or placed atop each other, overlapping areas reveal letters. Requires physical interaction with the book.
**Connection:** colors/, pigments/, optics/
**Physical:** Yes — must manipulate pages

### Q5 — Anamorphic Drawing
**Pitch:** A distorted drawing that only reads correctly from one angle.
**Mechanism:** An image on the page looks like abstract streaks. When the book is held at a severe angle (nearly edge-on), the streaks resolve into a word. Classic anamorphic art technique.
**Connection:** art-history/ (Holbein's skull in "The Ambassadors"), perspective/
**Physical:** Yes — must tilt the book

### Q6 — Golden Ratio Composition
**Pitch:** Measurements in an artwork follow the golden ratio — φ is the key.
**Mechanism:** A detailed architectural drawing or artwork reproduction on the page. Key measurements follow φ (1.618...). The solver measures distances, recognizes the ratio, uses it to decode marked positions. Letters at golden-ratio intervals spell the answer.
**Connection:** art-history/, architecture/, mathematics/ (cross-section!)
**Physical:** Yes — must measure with a ruler

### Q7 — Fibonacci Art Sequence
**Pitch:** The number of elements in each part of the puzzle follows the Fibonacci sequence.
**Mechanism:** A series of artistic vignettes. The first has 1 element, the next 1, then 2, 3, 5, 8... The element counts ARE the signal — mapped to letters or used as indices.
**Connection:** mathematics/, art-history/, botany/ (phyllotaxis)

---

## J — Mathematics & Physics

### J1 ★ Proof Completion
**Pitch:** Complete a mathematical proof — the missing terms spell the answer.
**Mechanism:** A proof chain with blanks. Each blank requires a specific mathematical concept (from different Math/Physics directories). First letters of the missing terms spell the answer.
**Answer:** SYMMETRY (8 blanks)
**V3 score:** 27/30

### J2 — Symmetry Operations
**Pitch:** Apply group theory transformations to a letter arrangement.
**Mechanism:** A grid of letters. The Joker specifies symmetry operations (rotation, reflection, translation) from group theory. Apply each operation to the grid. The transformed grids, overlaid, reveal the answer.
**Connection:** mathematics/ (group theory), physics/ (crystallography)
**Visual:** Yes — grid transformations

### J3 — Geometric Construction
**Pitch:** Follow compass-and-straightedge instructions — the construction yields a letter.
**Mechanism:** Step-by-step classical construction instructions. When drawn on the page, each construction forms a letter shape. 8 constructions → 8 letters → SYMMETRY.
**Worksheet:** Blank circles/lines for construction.
**Physical:** Yes — must draw with compass/straightedge (or improvise)

### J4 — Matrix Multiplication
**Pitch:** Multiply matrices — the results encode a message.
**Mechanism:** Several 2×2 or 3×3 matrices to multiply. Results, when decoded (mod 26, or specific cell positions), give letters.
**Connection:** mathematics/ (linear algebra)

### J5 — Equation Balancing
**Pitch:** Balance equations where the unknowns are letters.
**Mechanism:** Physics/chemistry equations with unknown quantities represented by letters. Solve each equation for its unknown. The unknowns, in order, spell the answer.
**Worksheet:** Equations with solve-for blanks.

### J6 — Topology Puzzle
**Pitch:** Which shapes are equivalent? The classification reveals the answer.
**Mechanism:** A set of shapes. Classify each by genus (number of holes) using topology from the encyclopedia. Genus numbers map to letters via A1Z26.
**Connection:** topology/

---

## 10 — Language & Communication

### 10-1 ★ Multi-Cipher Decoder
**Pitch:** Ten messages, each in a different encoding system, all taught in the same encyclopedia.
**Mechanism:** 10 encoded messages. Solver identifies each encoding (Morse, Braille, semaphore, pigpen, NATO, signal flags, ASL, binary, Caesar, telephone keypad) using `codes/`. Decodes each. First letters spell the answer.
**Answer:** INFLECTION (10 letters = 10 encoding systems)
**V3 score:** 29/30

### 10-2 — Rosetta Stone
**Pitch:** The same message in three scripts — use the parallels to decode.
**Mechanism:** A message written in three writing systems (e.g., Latin, Cyrillic, Arabic). Knowing one lets you decode the others. The decoded message reveals the answer.
**Connection:** linguistics/, world-languages/

### 10-3 — Phonetic Riddle
**Pitch:** Say these symbols aloud — what do they sound like?
**Mechanism:** A sequence of IPA (International Phonetic Alphabet) symbols. When pronounced, they sound like an English phrase that IS the answer.
**Connection:** linguistics/ (phonetics)
**Physical:** Yes — must speak aloud

### 10-4 — Etymological Chain
**Pitch:** Trace a word's origin across 5 languages — the root IS the answer.
**Mechanism:** A word's journey: Modern English ← Middle English ← Old French ← Latin ← Proto-Indo-European. At each stage, identify the word form using `linguistics/`, `world-languages/`. The PIE root, translated, is the answer.

### 10-5 — Cipher Wheel Construction
**Pitch:** Build a cipher wheel from the book — use it to decode a message.
**Mechanism:** A page with two concentric circles to cut out. Assemble into a physical cipher wheel. Use it to decode a message on another page.
**Connection:** codes/, cryptography/
**Physical:** Yes — cut and assemble

### 10-6 — Semaphore / Flag Reading
**Pitch:** Read the flags — they spell a message.
**Mechanism:** A series of stick-figure flag positions (semaphore) drawn on the page. Solver decodes using semaphore alphabet from `codes/`. The message spells the answer.
**Visual:** Yes — flag position diagrams

---

## 9 — Social Sciences

### 9-1 ★ Logic Grid
**Pitch:** Five fictional nations, five political systems — figure out which is which.
**Mechanism:** Einstein's riddle with social science concepts as attributes. Requires understanding governance types, economic models, legal traditions.
**Answer:** INCENTIVE
**V3 score:** 27/30

### 9-2 — Prisoner's Dilemma Tournament
**Pitch:** Play 5 rounds of game theory — optimal strategy yields the answer.
**Mechanism:** Five sequential games with different payoff matrices. The optimal move in each (cooperate/defect) maps to a binary code → decoded to letters.
**Connection:** game-theory/, economics/

### 9-3 — Voting Paradox
**Pitch:** Three elections, three voting systems, three different winners — resolve the paradox.
**Mechanism:** Same set of candidates, same voters, but plurality/ranked-choice/approval voting produces different winners. The paradox itself encodes the answer (which candidate wins under which system).
**Connection:** political-science/, game-theory/

### 9-4 — Market Equilibrium
**Pitch:** Supply meets demand — the equilibrium price IS a letter.
**Mechanism:** Supply and demand curves for several goods. Find equilibrium price/quantity for each. Prices map to letters.
**Connection:** economics/, behavioral-economics/

### 9-5 — Treaty Network
**Pitch:** Map which nations signed which treaties — the network reveals a word.
**Mechanism:** A graph where nations are nodes and treaties are edges. The structure of the graph (which nodes have the most connections, or the shortest path between specific nodes) encodes the answer.
**Connection:** international-relations/, law/

---

## 8 — Technology

### 8-1 ★ Signal Tracing
**Pitch:** Trace a signal through a system — decode what comes out the other end.
**Mechanism:** ASCII system diagram with components. Determine each component's effect on the signal. Apply transformations sequentially. Output decodes to answer.
**Answer:** TRANSISTOR
**V3 score:** 26/30

### 8-2 — Logic Gate Circuit
**Pitch:** Evaluate a logic circuit — the binary output decodes to letters.
**Mechanism:** A circuit diagram with AND/OR/NOT/XOR gates. Given inputs, trace through the circuit to compute outputs. Binary output → ASCII → letters.
**Connection:** semiconductor-manufacturing/, computer-architecture/
**Visual:** Yes — circuit diagram

### 8-3 — Frequency Spectrum
**Pitch:** Identify frequencies — each maps to a musical note or letter.
**Mechanism:** A frequency spectrum chart showing peaks at specific Hz values. Identify what each frequency represents (using `telecommunications/`, `signal-processing/`). Frequencies map to notes → note names spell the answer.
**Connection:** telecommunications/, signal-processing/, music-theory/ (cross-section!)

### 8-4 — Bit Pattern / QR by Hand
**Pitch:** A grid of black and white squares — decode it like a simple QR code.
**Mechanism:** A visual grid pattern. Not an actual QR code but a simpler encoding (like Braille scaled up, or a 5-bit binary grid). Solver decodes the pattern to get letters.
**Visual:** Yes — must read a visual grid

### 8-5 — PCB Trace Following
**Pitch:** Follow copper traces on a circuit board — the path collects letters.
**Mechanism:** A printed circuit board diagram. Follow specific traces from component to component. Letters at each component, collected in trace order, spell the answer.
**Visual:** Yes — must follow paths on a complex diagram

---

## 7 — Mechanics

### 7-1 ★ Engineering Calculation
**Pitch:** Calculate forces in 5 simple machines — the numbers spell a word.
**Mechanism:** Five diagrams (lever, pulley, gear train, inclined plane, hydraulic press). Calculate output for each. Numbers → A1Z26 → letters → TORQUE.
**Answer:** TORQUE
**V3 score:** 28/30

### 7-2 — Gear Train
**Pitch:** Count teeth, calculate ratios — the output RPM encodes a letter.
**Mechanism:** A gear train diagram with multiple meshing gears. Given input RPM and tooth counts, calculate output RPM for each stage. Outputs encode letters.
**Visual:** Yes — gear diagrams
**Connection:** mechanical/, manufacturing/

### 7-3 — Rube Goldberg Chain
**Pitch:** Trace a chain reaction — each stage contributes a letter.
**Mechanism:** An elaborate Rube Goldberg machine drawn across the page. Each stage involves a different mechanical principle (lever, spring, pulley, pendulum). Identifying each principle's name → first letters spell the answer.
**Visual:** Yes — elaborate chain-reaction diagram
**Fun factor:** Very high — Rube Goldberg machines are inherently delightful

### 7-4 — Bridge Structural Analysis
**Pitch:** Which members are in tension? Which in compression? The pattern encodes a message.
**Mechanism:** A truss bridge diagram with labeled members. Analyze each member (tension T or compression C). The T/C pattern across members = binary → decoded to letters.
**Connection:** structural/
**Visual:** Yes — truss diagram

### 7-5 — Fluid Flow Path
**Pitch:** Trace water through a pipe network — the path spells a word.
**Mechanism:** A branching pipe network. At each junction, the solver must calculate which branch the fluid takes (based on pressure/diameter — from `hvac/`, `plumbing/`). The path through the network collects letters at nodes.
**Visual:** Yes — pipe network diagram

---

## 6 — History & Ideas

### 6-1 ★ Primary Source Detective
**Pitch:** Identify 8 historical documents from their opening lines.
**Mechanism:** Real quotes from real primary sources, unattributed. Solver identifies source and date using History section. Chronological ordering + extraction from author names spells the answer.
**Answer:** PARADIGM
**V3 score:** 29/30

### 6-2 — Historical Map Overlay
**Pitch:** Overlay maps from different eras — the differences reveal a message.
**Mechanism:** Two maps of the same region from different centuries. The boundaries that changed between eras, when traced, form letter shapes. Or: territories that appear/disappear encode letters.
**Connection:** historical-geography/, military-history/
**Physical:** Yes — overlay pages

### 6-3 — Philosophical Argument Chain
**Pitch:** Follow a logical argument — identify the valid and invalid steps.
**Mechanism:** A multi-step philosophical argument. Some steps are valid deductions, others are fallacies. Valid steps = 1, fallacies = 0 → binary → decoded to letters. Identifying fallacies requires reading `philosophy/`, `logic/`.
**Connection:** philosophy/, logic/

### 6-4 — Cause-and-Effect Web
**Pitch:** Trace historical causation — the chain reveals a word.
**Mechanism:** A web of historical events with causal arrows. Trace the longest causal chain. Events on the chain, in order, contribute letters to the answer.
**Connection:** history-of-science/, economic-history/

### 6-5 — Fairy Tale Logic
**Pitch:** Classic puzzle wrapped in a fairy-tale narrative from mythology.
**Mechanism:** "The sage must cross 3 rivers. Each bridge demands a tribute of knowledge..." A narrative logic puzzle where the constraints come from mythology/ and religious-studies/. Solving the narrative puzzle reveals the answer.
**Connection:** mythology/, religious-studies/, philosophy/

---

## 5 — Life Sciences

### 5-1 ★ Codon Decoding
**Pitch:** Translate a DNA sequence into a secret message using the genetic code.
**Mechanism:** DNA → mRNA → codons → amino acids → single-letter codes → answer.
**Answer:** GENETIC (G-E-N-E-T-I-C, all valid amino acid codes)
**V3 score:** 30/30

### 5-2 — Phylogenetic Tree Traversal
**Pitch:** Climb the tree of life — each branch point encodes a letter.
**Mechanism:** A phylogenetic tree with species at the leaves. Trace the path between specific species. At each branch point, the common ancestor's key trait (identified from `biology/`, `evolutionary-biology/`) contributes a letter.
**Visual:** Yes — tree diagram

### 5-3 — Metabolic Pathway
**Pitch:** Follow glucose through metabolism — the intermediates spell a word.
**Mechanism:** A simplified metabolic pathway (glycolysis → Krebs cycle). Key intermediates are named. First letters of intermediates in pathway order spell the answer.
**Connection:** natural-sciences/08-METABOLISM.md

### 5-4 — Punnett Square Genetics
**Pitch:** Cross organisms — the phenotype ratios encode letters.
**Mechanism:** Several genetic crosses with given genotypes. Calculate phenotype ratios. Ratios (3:1, 9:3:3:1, etc.) map to specific numbers → letters.
**Connection:** biology/, genomics/

### 5-5 — Cell Organelle Labeling
**Pitch:** Label the cell — first letters of organelles spell a word.
**Mechanism:** An unlabeled cell diagram. Solver identifies each organelle using `natural-sciences/10-CELL-BIOLOGY.md`. First letters of organelle names, reading clockwise, spell the answer.
**Visual:** Yes — cell diagram

### 5-6 — Epidemic Network
**Pitch:** Trace disease spread through a population — the path spells a word.
**Mechanism:** A network of individuals. Given patient zero and transmission rules (from `disease/`, `public-health/`), trace the spread. Infected individuals' initials, in order of infection, spell the answer.
**Visual:** Yes — network diagram

---

## 4 — Material Culture

### 4-1 ★ Element Identification (First Letters)
**Pitch:** Identify 7 mystery elements from material clues — first letters spell CASTING.
**Mechanism:** 7 riddle-clues about elements (Carbon, Aluminum, Silver, Tin, Iron, Nickel, Gold). Solver identifies each from properties. First letters = CASTING.
**Answer:** CASTING
**V3 score:** 29/30

### 4-2 — Craft Process Ordering
**Pitch:** Put the steps of a craft in order — the sequence reveals a word.
**Mechanism:** Steps of a material process (smelting, glazing, weaving, etc.) given out of order. Correct sequence + extraction from step names spells the answer.
**Connection:** metalworking/, ceramics/, textiles/

### 4-3 — Textile Pattern Binary
**Pitch:** A weaving pattern encodes a message — over/under = 1/0.
**Mechanism:** A weaving draft diagram. Warp-over-weft = 1, weft-over-warp = 0. Read the binary pattern → decode to ASCII → letters.
**Connection:** textiles/
**Visual:** Yes — weaving draft grid

### 4-4 — Glaze Chemistry
**Pitch:** Balance ceramic glaze recipes — the oxide ratios encode letters.
**Mechanism:** Ceramic glaze formulas with oxide ratios (SiO₂, Al₂O₃, etc.). The ratios, when simplified, give small integers → A1Z26 → letters.
**Connection:** ceramics/, periodic-table/

### 4-5 — Periodic Table Spelling
**Pitch:** Spell the answer using element symbols from the periodic table.
**Mechanism:** Clues point to specific elements. Their 1-2 letter chemical symbols, concatenated, spell the answer word. E.g., Ca + S + Ti + N + G = CaSTiNG... (verify: Ca=Calcium, S=Sulfur, Ti=Titanium, N=Nitrogen, G=? — G isn't an element symbol. Doesn't work for CASTING specifically but the concept is sound for other words.)

### 4-6 — Kiln Temperature Profile
**Pitch:** A firing schedule graph — the temperature peaks encode letters.
**Mechanism:** A temperature-vs-time graph for a ceramic firing. Peak temperatures at specific hold points → numbers → A1Z26 → letters.
**Connection:** ceramics/
**Visual:** Yes — graph reading

---

## 3 — Earth & Space

### 3-1 ★ Connect-the-Dots Star Chart
**Pitch:** Plot celestial objects on a chart — groups trace letter shapes.
**Mechanism:** 7 groups of celestial objects described poetically. Identify, plot on coordinate grid. Each group traces a letter. 7 letters spell EQUINOX.
**Answer:** EQUINOX
**V3 score:** 29/30
**Physical:** Yes — draw on the page (the "Chicago Fire" moment)

### 3-2 — Geological Cross-Section
**Pitch:** Read the rock layers — hidden words in the strata names.
**Mechanism:** A geological cross-section diagram with labeled strata. Certain letters in the strata names, when read at specific depths, spell the answer.
**Connection:** geology/, paleontology/
**Visual:** Yes — cross-section diagram

### 3-3 — River Confluence Map
**Pitch:** Where rivers meet — the confluence points trace a word.
**Mechanism:** Major river confluences plotted on a map grid. The points, connected in order of river length, trace letter shapes.
**Connection:** geography/, hydrology/
**Physical:** Yes — draw on a map

### 3-4 — Mountain Silhouette
**Pitch:** The mountain range profile IS a letter.
**Mechanism:** Silhouette profiles of famous mountain ranges. Each skyline, when viewed as a letter shape, gives one character. Multiple ranges → multiple letters → answer.
**Connection:** geology/, geography/
**Visual:** Yes — skyline interpretation

### 3-5 — Tectonic Plate Jigsaw
**Pitch:** Fit the plates together — the assembled map reveals a hidden word.
**Mechanism:** Cut-out tectonic plates (simplified shapes). When assembled correctly (like Pangaea), letters on plate edges align to spell the answer.
**Connection:** geology/
**Physical:** Yes — cut and assemble

### 3-6 — Sundial Construction
**Pitch:** Build a sundial from the page — the shadow points to the answer.
**Mechanism:** A page designed as a cut-out sundial. Fold and assemble. At a specific time (encoded in the puzzle), the shadow falls on a letter.
**Connection:** astronomy/
**Physical:** Yes — cut, fold, use sunlight

---

## 2 — Natural World

### 2-1 ★ Organism Identification + Diagonal
**Pitch:** Identify 5 mystery organisms — their names hide a word on the diagonal.
**Mechanism:** 5 organisms described by characteristics only. Identify using Natural World section. Diagonal read across common names spells the answer.
**Answer:** NICHE (5 letters — buildable)
**V3 score:** 26/30

### 2-2 — Food Web Traversal
**Pitch:** Follow energy through a food web — the path spells a word.
**Mechanism:** An ecosystem food web diagram. Trace the energy path from producer to apex predator. Organisms on the path contribute letters. Multiple valid paths exist — only one spells a real word.
**Connection:** ecology/
**Visual:** Yes — food web diagram

### 2-3 — Leaf / Mushroom Identification Key
**Pitch:** Use a dichotomous key to classify specimens — each classification yields a letter.
**Mechanism:** A visual identification key (like a field guide). Several specimens to classify. Each binary choice in the key (smooth/serrated, gilled/pored) leads to a classification. Classifications encode letters.
**Connection:** botany/, mycology/
**Visual:** Yes — specimen illustrations + branching key

### 2-4 — Birdsong as Morse
**Pitch:** Visual birdsong spectrograms — the patterns ARE Morse code.
**Mechanism:** Spectrogram-style representations of birdsong. Long notes = dashes, short notes = dots. Decode as Morse.
**Connection:** ornithology/, acoustics/
**Visual:** Yes — spectrograms

### 2-5 — Spice Route
**Pitch:** Trace spices to their origins — the route spells a word on the map.
**Mechanism:** Clues identify specific spices. Plot their geographic origins on a map. Connected in trade-route order, the path traces letter shapes.
**Connection:** spices/, culinary-history/, historical-geography/
**Physical:** Yes — draw on a map

---

## A — People

### A-1 ★ Influence Chains
**Pitch:** Trace who taught whom — the chain gives the extraction order.
**Mechanism:** Intellectual inheritance descriptions. Identify each figure. Trace the chain. Letters extracted from each figure's name (by position in chain) spell the answer.
**Answer:** POLYMATH
**V3 score:** 29/30

### A-2 — Portrait Gallery
**Pitch:** Identify 8 people from their achievements, not their names.
**Mechanism:** Descriptions of accomplishments without naming the person. Solver identifies each using People section. Initials spell the answer.
**Connection:** All People directories

### A-3 — Timeline of Overlapping Lives
**Pitch:** Whose lifetimes overlapped? The connections reveal a word.
**Mechanism:** Birth and death years of famous figures. Find pairs whose lifetimes overlapped. The overlapping figures share a connection — the connection word encodes the answer.

### A-4 — Letter Exchange
**Pitch:** Famous correspondences — extract from the letters they wrote each other.
**Mechanism:** Excerpts from real historical letters between thinkers (Einstein-Born, Darwin-Hooker, Adams-Jefferson). Key words extracted from each letter spell the answer.
**Connection:** All People directories

### A-5 — Invention Dependency Chain
**Pitch:** A invented X, which enabled B to invent Y — trace the chain.
**Mechanism:** A dependency graph of inventions. Each invention required a prior one. Trace the critical path. Inventor names along the path encode the answer.
**Connection:** engineers-inventors/, computing-pioneers/

---

## Cross-Section, Visual, and Physical Puzzles

### X1 — Paper + Light (Raiders of the Lost Ark)
**Pitch:** Build a 3D shape from the book. Shine a flashlight through it. Shadows spell the answer.
**Mechanism:** A page with a cut-out template. Fold into a 3D polyhedron with holes/windows. When light shines through, shadows on a flat surface form letters.
**Physical:** Maximum physicality. THE legendary moment.
**Where:** Black Joker meta, or Red Joker meta payoff.

### X2 — Color Overlay
**Pitch:** Hold two pages together up to light — the overlap reveals a hidden word.
**Mechanism:** Two pages with partial patterns in different colors. When aligned and backlit, the combined pattern spells a word.
**Physical:** Yes — manipulate pages.
**Where:** Red Joker Arts puzzle, or Black Joker synthesis.

### X3 — Fold the Page
**Pitch:** Fold the page in half — distant elements meet and form a word.
**Mechanism:** Letters scattered across a page. When folded at a specific crease, letters align to spell the answer.
**Physical:** Yes — fold the book page.
**Where:** Any section — mechanism is section-agnostic.

### X4 — Golden Ratio Spiral
**Pitch:** The golden ratio connects art, nature, math, and music — find φ and use it as a key.
**Mechanism:** A multi-section puzzle. Measurements in an artwork, a nautilus shell, a musical rhythm, and a mathematical expression all yield φ = 1.618... The ratio is the decryption key for a final message.
**Where:** Black Joker "Spectrum" puzzle — one phenomenon across 4 sections.

### X5 — Fibonacci Structural Sequence
**Pitch:** The number of elements in each puzzle follows 1, 1, 2, 3, 5, 8, 13.
**Mechanism:** Not a standalone puzzle but a META-structural principle. If the 13 Red Joker puzzles have Fibonacci-number-of-elements, the solver who notices can predict puzzle structures.
**Where:** Red Joker structural layer.

### X6 — Musical Score Message
**Pitch:** A melody on a staff — the note names spell a word.
**Mechanism:** A musical staff with specific notes. Note letters (C,D,E,F,G,A,B) read in sequence spell a word or cluephrase. Solver must read notation from `music-theory/`.
**Where:** Red Joker Arts puzzle or Black Joker synthesis.

### X7 — Cipher Wheel Construction
**Pitch:** Cut out two discs, assemble a cipher wheel, decode a message.
**Mechanism:** A page with two concentric circle templates. Cut, pin together, rotate to alignment. Use the wheel to decode a message elsewhere in the book.
**Physical:** Yes — cut and build a tool.
**Where:** Red Joker Language puzzle (tool-building before decoding).

### X8 — Punch Card Overlay
**Pitch:** Punch holes at marked positions — overlay on another page — visible text is the answer.
**Mechanism:** A page with marked dots to punch out. Place the punched page on top of a text-heavy page. Only specific words show through the holes. Those words spell the answer.
**Physical:** Yes — punch and overlay.
**Where:** Any — the underlying text page could be from any section.

### X9 — Mirror Puzzle
**Pitch:** Hold the page to a mirror — the reflection reveals hidden text.
**Mechanism:** Text or an image printed in mirror-reversed form. Only readable when reflected. Leonardo da Vinci wrote this way.
**Connection:** art-history/ (da Vinci), optics/
**Physical:** Yes — need a mirror.
**Where:** Red Joker Arts or Black Joker.

### X10 — Tangram Letter Assembly
**Pitch:** Rearrange tangram pieces to form letter shapes.
**Mechanism:** A set of tangram pieces (cut from the page). Instructions say "form the following shapes." Each shape is a letter. The letters spell the answer.
**Physical:** Yes — cut and arrange.
**Connection:** games-history/, mathematics/ (geometry)

### X11 — Origami Fold
**Pitch:** Fold the page following instructions — the folded shape reveals a word.
**Mechanism:** Specific fold instructions. When completed, the visible surfaces show only certain letters/images that spell the answer. The rest is hidden in the folds.
**Physical:** Yes — origami.

### X12 — Five Senses Quintet
**Pitch:** Five puzzles, each engaging a different sense.
**Mechanism:** Not a single puzzle but an organizing principle:
- Sight: visual rebus or anamorphic drawing
- Touch: paper construction or origami
- Hearing: musical score or "say it aloud" phonetics
- Taste/Smell: spice identification from flavor descriptions
- Balance/proprioception: something spatial/physical
**Where:** Could organize 5 of 13 Red Joker puzzles.

### X13 — River Letters
**Pitch:** Major rivers, plotted on a map, trace letter shapes.
**Mechanism:** Identify rivers from descriptions. Plot their courses on a provided map. The river paths form letters.
**Physical:** Yes — draw on a map.
**Connection:** geography/, hydrology/

### X14 — Mountain Range Frequency
**Pitch:** Mountain elevation profiles as waveforms — the frequencies encode letters.
**Mechanism:** Elevation profiles of mountain ranges look like waveforms. Measure the "frequency" (peaks per unit distance). Frequencies map to musical notes → note names → letters.
**Connection:** geology/, music-theory/, signal-processing/ (cross-section!)

### X15 — Phenakistoscope / Zoetrope
**Pitch:** Cut out a disc, spin it — the animation reveals a word.
**Mechanism:** A disc with sequential images around the edge. When cut out and spun (with slits to view through), the images animate and reveal a word that's invisible when stationary.
**Physical:** Maximum novelty. Deeply connected to cinema-film/ and optics/.

### X16 — Sundial
**Pitch:** Build a paper sundial — the shadow at a specific time points to the answer.
**Mechanism:** Cut-out sundial template calibrated to a specific latitude. Assemble and place in sunlight. At a specific time (given by the puzzle), the shadow falls on a marked letter.
**Physical:** Yes — requires sunlight.
**Connection:** astronomy/

### X17 — Stereo Pair
**Pitch:** Cross your eyes — the 3D image reveals a hidden word.
**Mechanism:** Two slightly different images side by side (stereogram). When viewed with crossed eyes (or a stereoscope), a 3D effect reveals depth, and a word appears floating above or below the surface.
**Connection:** optics/, photography/
**Physical:** Yes — must cross eyes or use viewer.

---

## Summary — Total Pool

| Category | Count |
|----------|-------|
| K: Computing | 5 |
| Q: Arts | 7 |
| J: Math/Physics | 6 |
| 10: Language | 6 |
| 9: Social Sciences | 5 |
| 8: Technology | 5 |
| 7: Mechanics | 5 |
| 6: History | 5 |
| 5: Life Sciences | 6 |
| 4: Material Culture | 6 |
| 3: Earth & Space | 6 |
| 2: Natural World | 5 |
| A: People | 5 |
| X: Cross-section / Physical | 17 |
| **TOTAL** | **89 puzzle briefs** |
