# Round 2 Review: Puzzle Pool Ranking

**Reviewer**: Kenny Young
**Lens**: Infrastructure and Buildability
**Date**: 2026-02-26
**Input**: PUZZLE-POOL.md (89 candidates), TWO-JOKERS.md (freed answer words)

---

## Context Shift Since Round 1

The ENLIGHTENMENT acrostic is dead. Good riddance. That constraint was
the single largest construction headache in my first review — it forced
bad answer words on sections that didn't want them, and it meant every
feeder puzzle was fighting the acrostic before it could fight its own
mechanism.

Now each section picks its own best answer word. The puzzle pool also
moves from "steganographic embedding in live encyclopedia files" to
"standalone Joker book with worksheets." This changes everything. The
fragility concern I hammered in Round 1 (signal elements breaking on
content edits) largely evaporates. These are now book puzzles that
*reference* the encyclopedia rather than puzzles *embedded in* it. That
is a massive buildability upgrade.

The pool has 89 candidates: 72 section puzzles (roughly 5-7 per section)
and 17 cross-section/physical puzzles. We need 13 for Red Joker. This
review scores every candidate on buildability, then recommends the best
13 and a build order.

---

## Scoring Criteria (Buildability 1–5)

| Score | Meaning |
|:-----:|---------|
| **5** | Can prototype in an afternoon. Answer word achievable. Minimal construction risk. |
| **4** | Buildable in a day or two. One constraint to verify, but likely solvable. |
| **3** | Buildable but requires real construction labor. One or two unsolved constraints. |
| **2** | Significant construction risk. Multiple unsolved constraints or fragile mechanism. |
| **1** | May not be possible. Fundamental constraint that could block completion. |

---

## K — Computing & Software

### K1 ★ Cipher Decryption — Buildability: 5/5

The cleanest puzzle in the pool. The Joker gives ciphertext. The solver
learns a cipher from `cryptography/`. The key lives in `computing/25-SECURITY.md`.
Plaintext becomes answer. Answer: ALGORITHM.

Why this works: You control the ciphertext completely. You control the key
placement. The mechanism is self-contained — no constraint-satisfaction
needed, no fragile content dependencies. The worksheet (ciphertext / key /
shift / plaintext grid) is a classic that every puzzle constructor knows
how to build. One file to create (the puzzle page), one file to reference
(the key source). ALGORITHM is 9 letters, which is a comfortable cipher
length — not so short that the cipher is trivial, not so long that the
worksheet sprawls.

Only risk: the cipher must be learnable from the encyclopedia in
reasonable time. A Caesar shift is too easy. A Vigenere is about right.
A substitution cipher with a keyed alphabet (key phrase from SECURITY.md)
is ideal — requires learning the construction, then applying it.

**Verdict: Slot this. First prototype.**

### K2 — Algorithm Execution — Buildability: 4/5

Give the solver pseudocode to trace. Output = answer. This is PuzzleJS
territory — I have built interactive execution-trace puzzles. On paper
it is a worksheet with variable-state columns.

Construction is straightforward: write pseudocode that produces the
desired output string. The constraint is that the pseudocode must look
like a real teaching example (not a Rube Goldberg string factory) while
outputting exactly ALGORITHM or whatever the answer is. Achievable with
a loop that indexes into an array.

Risk: if the pseudocode is too tricky, solvers stall on execution
semantics rather than the puzzle. If too simple, it is busywork. The
sweet spot is a 10-15 step trace with one conditional and one loop.
Prototypable in a couple hours.

**Verdict: Strong backup to K1. Not needed if K1 is selected.**

### K3 — State Machine Traversal — Buildability: 3/5

ASCII state diagram, labeled transitions, path collects letters. Sound
concept. The problem is that state machine diagrams are hard to render
clearly on a printed page. You need enough states (8-10) that the path
is non-trivial, but ASCII state diagrams with 8+ nodes and labeled
transitions get visually messy fast. I have drawn these — they eat a
full page and still feel cramped.

The construction: design a DFA where exactly one valid path exists (given
the transition conditions), and that path visits states labeled with
answer letters. This is a graph-design problem with a unique-path
constraint. Solvable, but you need to prototype the diagram to verify
readability.

**Verdict: Interesting but harder to lay out than it sounds.**

### K4 — Stack Trace / Recursion — Buildability: 3/5

Trace a recursive function, return values encode letters. The concept
maps well to the computing section and produces a natural worksheet (call
stack diagram). But: designing a recursive function whose return values
at each level are exactly the right integers to map to letters is a
tight constraint. You need return values in the 1-26 range at each level
of recursion, and the function must look like a plausible teaching
example.

Also, recursion tracing is genuinely hard for many solvers. The Red
Joker aims for "engaged reader, solo weekend." A 7-level recursive
trace with arithmetic at each level might be difficulty-inappropriate.

**Verdict: Cool mechanism, risky difficulty calibration.**

### K5 — Binary Decoder — Buildability: 4/5

ASCII art made of 0s and 1s, binary decodes to text. This is very
buildable — you are generating ASCII art from a fixed string, which is
a deterministic process. Many tools exist for this. The visual is
striking on a page.

Risk: binary ASCII art requires 7-8 bits per character, so a 9-letter
word needs 63-72 binary digits arranged in a legible image. The image
needs to be large enough to read individual digits. This eats page
space. Also, the "picture" aspect might not add puzzle value — if the
solver just reads the 0s and 1s as binary (ignoring the image), the
picture is decoration.

**Verdict: Buildable but thin. Better as a B-side element than a
standalone.**

### K Section Summary

| ID | Name | Build | Notes |
|----|------|:-----:|-------|
| K1 ★ | Cipher Decryption | **5** | Best in section. Slot it. |
| K2 | Algorithm Execution | **4** | Strong backup |
| K3 | State Machine | **3** | Layout concerns |
| K4 | Stack Trace | **3** | Difficulty risk |
| K5 | Binary Decoder | **4** | Buildable but thin |

---

## Q — Arts & Culture

### Q1 — Crossword — Buildability: 4/5

A crossword with Arts clues and highlighted cells. The most traditional
puzzle type in the pool. Crossword construction is well-understood —
tools exist, the workflow is known, and the result is always solvable if
the grid is valid.

Answer: PERSPECTIVE. 11 letters. That means 11 highlighted cells in the
grid. The grid needs to be large enough to embed 11 thematic entries
with crossing constraints. A 15x15 grid is standard; you could do 11x11
or 13x13 for space reasons. Construction time: a couple hours with
crossword-building software.

The V3 score of 25/30 was noted as "the floor." The mechanism is safe
but unexciting. For the Arts section, you want something with more
visual flair. A crossword does not *feel* like art.

**Verdict: Reliable fallback. Not the first choice for Arts.**

### Q2 — Visual Rebus — Buildability: 4/5

Spatial arrangements of words/letters represent concepts. Each solved
rebus is an Arts term, extracted letters spell the answer. Rebus puzzles
are well-understood, highly buildable, and visually engaging on a page.
You control every pixel of the layout.

Construction: design N rebus images, each with one unambiguous answer.
Extract one letter per rebus (by position). For PERSPECTIVE (11 letters)
you need 11 rebuses. That is a lot — most rebus sets are 6-8. Consider
a shorter answer word, or accept that this takes a full page spread.

Risk: rebus ambiguity. "Letters arranged in vanishing-point perspective"
could be read as PERSPECTIVE or VANISHING POINT or CONVERGENCE. You need
each rebus to have exactly one defensible answer, which means careful
design and probably a confirming crossing or enumeration hint.

**Verdict: High visual appeal, needs careful disambiguation.**

### Q3 — Musical Staff Decoder — Buildability: 4/5

Notes on a staff spell a message. Note names are C-D-E-F-G-A-B, which
limits your alphabet to 7 letters. PERSPECTIVE cannot be spelled (no P,
R, S, T, I, V). You would need an answer word using only {A, B, C, D,
E, F, G}. FACADE (F-A-C-A-D-E) works. CABBAGE. BADGE. DEFACE.

None of these are great "Arts & Culture" answer words. You could use
sharps/flats to extend the alphabet (C# = 8th letter?), but that is an
invented encoding, not real music notation.

Alternative: the note sequence spells a cluephrase using only those 7
letters, like "A BEAD FACE" → extract somehow? Getting weird.

**Verdict: The 7-letter alphabet kills this for most answer words. Only
viable if the answer is constrained to {A-G}.**

### Q4 — Color Overlay — Buildability: 2/5

Two pages, hold to light, overlap reveals word. Beautiful concept. THE
problem: this requires precise color registration across two pages of a
printed book. If the pages shift by even 1mm when held to light, the
overlay misaligns. Professional puzzle-book printers can do this (Maze
books, transparent-overlay puzzles exist), but it requires:

1. Full-bleed color printing on specific paper stock
2. Registration marks or alignment guides
3. Testing with the actual print run (screen mockups lie)

You cannot prototype this on a home printer. You need a print proof from
the actual production printer. If this is a MkDocs-rendered PDF viewed
on screen, the mechanism does not work at all.

**Verdict: Requires professional print production. Not prototypable in
an afternoon. Park until print format is decided.**

### Q5 — Anamorphic Drawing — Buildability: 2/5

Distorted image resolves when viewed at extreme angle. Anamorphic art is
real (Holbein's skull), but making it work on a printed page requires
precise geometric distortion calculated for a specific viewing angle and
distance. The distortion depends on the viewer's eye position relative to
the page surface.

You can generate anamorphic images computationally, but: (1) it only
works at one specific angle, (2) the page surface must be reflective
enough to read at an extreme angle (matte paper kills contrast), (3) the
"aha" only works if the viewer knows to try it. Without a hint, most
solvers will not hold their book at 80 degrees from horizontal.

**Verdict: Cool concept, engineering-heavy execution. Not a construction
afternoon — this is a multi-day print-R&D project.**

### Q6 — Golden Ratio Composition — Buildability: 3/5

Measure an artwork, find phi, use it as key. Requires a ruler, which
most solvers have. The construction: design an artwork where key
measurements follow phi = 1.618... This is achievable — architectural
drawings naturally incorporate golden ratio proportions. The extraction
(letters at golden-ratio intervals) needs definition: intervals along
what? A baseline? A spiral?

Risk: measurement precision. If the solver's ruler reads 4.1cm instead
of 4.0cm, the ratio becomes 1.64 instead of 1.618. How precise must the
measurement be? For a code extraction, you need integer positions —
"the 5th letter, the 8th letter, the 13th letter" (Fibonacci!). That is
more robust than continuous measurement.

**Verdict: Workable if you use Fibonacci positions rather than
continuous phi measurement.**

### Q7 — Fibonacci Art Sequence — Buildability: 3/5

Element counts follow 1, 1, 2, 3, 5, 8... This is an organizing
principle more than a puzzle mechanism. How do element counts extract
letters? If you map count → A1Z26, you get A, A, B, C, E, H — which is
arbitrary. If counts are indices into a text, you need a text to index
into.

This feels like a structural flourish (cool that the puzzle has
Fibonacci structure) rather than a solvable extraction. It works better
as a meta-level design principle (X5 in the pool) than as a standalone
puzzle.

**Verdict: Not a standalone puzzle. Possible structural overlay for
another mechanism.**

### Q Section Summary

| ID | Name | Build | Notes |
|----|------|:-----:|-------|
| Q1 | Crossword | **4** | Reliable, unexciting |
| Q2 | Visual Rebus | **4** | Best visual appeal; needs disambiguation work |
| Q3 | Musical Staff | **4** | 7-letter alphabet kills most answer words |
| Q4 | Color Overlay | **2** | Print-production dependent |
| Q5 | Anamorphic | **2** | Multi-day print R&D |
| Q6 | Golden Ratio | **3** | Viable with Fibonacci indices |
| Q7 | Fibonacci Seq | **3** | Organizing principle, not standalone |

---

## J — Mathematics & Physics

### J1 ★ Proof Completion — Buildability: 5/5

A proof with blanks. Fill the blanks with math/physics concepts. First
letters spell SYMMETRY (8 blanks). The construction is entirely under
your control: you write the proof, you choose the blanks, you choose the
missing terms. As long as 8 plausible math/physics concepts start with
S-Y-M-M-E-T-R-Y, this is done.

S = Substitution. Y = ? (Yielding? not a math term). Hmm. Y is hard.
Let me think... Y-axis? Not a "concept." Y: this is the one constraint
to verify. But SYMMETRY as the answer word is so thematically perfect
for Math/Physics that it is worth finding a Y-word. "Y-intercept" in a
coordinate geometry proof? Plausible.

Actually, the proof does not need to be an acrostic of SYMMETRY through
first letters alone. The brief says "first letters of the missing terms
spell the answer." So you need 8 missing terms whose first letters are
S, Y, M, M, E, T, R, Y. That is findable:

- S: Substitution / Scalar / Supremum
- Y: "by symmetrY" — wait, first letters. You need a term starting with Y.
  Y... Yield (as in yield strength, from physics). Or the proof references
  a "Young's modulus" step? That works in a physics-flavored proof.
- M: Matrix / Magnitude / Minimum
- M: Mapping / Measure
- E: Eigenvalue / Equivalence
- T: Transpose / Tensor / Theorem
- R: Rotation / Reflection / Rank
- Y: See above — use a different Y-word, or accept "Young's modulus" twice.

Two Y's is the only constraint. Manageable.

**Verdict: Slot this. High confidence build.**

### J2 — Symmetry Operations — Buildability: 3/5

Apply group theory transforms to a letter grid. This is conceptually
wonderful (the Math section's puzzle IS about symmetry operations). But:
grid transformations on paper are error-prone. A solver must mentally
(or on scratch paper) rotate/reflect a letter grid, then overlay multiple
transformed copies. With 3+ operations on an 8x8 grid, the manual labor
is high and mistakes compound.

Construction: you need a starting grid and a sequence of operations such
that the overlay reveals exactly the answer. This is a solvable design
problem (work backward from the answer), but the solver experience of
manually performing matrix operations on paper is tedious, not delightful.

**Verdict: Great theme, labor-intensive solving. Better as an
interactive PuzzleJS puzzle than a paper worksheet.**

### J3 — Geometric Construction — Buildability: 2/5

Compass-and-straightedge constructions that form letters. Each
construction = one letter, 8 constructions = SYMMETRY. The problem: you
need a compass. The Red Joker should not require external tools beyond
a pencil. Some solvers will improvise (string and pin), but the
precision needed for construction→letter legibility is high.

Also: constructing a letter shape via compass and straightedge is not
a standard geometric construction. You cannot construct the letter "S"
with compass and straightedge in any meaningful sense. The claim
"constructions form letter shapes" is aspirational, not verified.

**Verdict: Requires an external tool (compass) and unverified letter
legibility. Pass.**

### J4 — Matrix Multiplication — Buildability: 4/5

Multiply matrices, decode results. Straightforward construction: define
matrices, compute products, verify products decode to target letters.
The worksheet is a natural fit (matrix grid with blank cells for the
result). A1Z26 on individual cells or mod-26 on determinants.

Risk: matrix multiplication is tedious by hand. 3x3 matrix mult is 27
multiply-and-add operations per product. Multiple products = 100+
arithmetic operations. Solvers will make arithmetic errors, get garbage
letters, and blame the puzzle. Keeping matrices 2x2 reduces labor but
limits the encoding space.

**Verdict: Buildable but tedious. Use 2x2 matrices only.**

### J5 — Equation Balancing — Buildability: 4/5

Solve equations for unknowns represented by letters. Unknowns spell the
answer. This is clean: you write the equations, you choose the unknowns,
you label them with letters. The solver does algebra. The worksheet is
equation blanks.

Construction: 8 equations (for SYMMETRY), each with one unknown. The
equations reference physics/chemistry concepts (F=ma, PV=nRT, etc.).
Each solved value is a number — how does a number become a letter? If
the unknowns are directly labeled S, Y, M, etc., the number is
irrelevant and the "solve" is just confirming the equation works. That is
busywork, not a puzzle. If the number maps to a letter (A1Z26), you need
the solved value to be 19 (for S), 25 (for Y), etc. — which constrains
the equation parameters heavily.

**Verdict: Clean mechanism but extraction needs thought. The "unknowns
are already letters" version is trivial; the "solve for a number" version
is constrained.**

### J6 — Topology Puzzle — Buildability: 3/5

Classify shapes by genus, genus → A1Z26. Genus is 0, 1, 2, 3... for
most practical shapes. Genus 0 = A, genus 1 = B, genus 2 = C. You are
limited to letters A through maybe F (genus 5 is exotic). SYMMETRY
needs S (19), which would require a genus-19 surface. That is a
19-holed torus. Drawing a genus-19 surface legibly is not happening.

This mechanism only works for very short answer words using early
alphabet letters. Not viable for SYMMETRY.

**Verdict: Alphabet range too limited. Not viable for any interesting
answer word.**

### J Section Summary

| ID | Name | Build | Notes |
|----|------|:-----:|-------|
| J1 ★ | Proof Completion | **5** | Best in section. Two Y-words needed; findable. |
| J2 | Symmetry Operations | **3** | Great theme, tedious paper execution |
| J3 | Geometric Construction | **2** | Needs compass; letter legibility unverified |
| J4 | Matrix Multiplication | **4** | Buildable with 2x2; tedious with 3x3 |
| J5 | Equation Balancing | **4** | Clean, but extraction path needs definition |
| J6 | Topology / Genus | **3** | Alphabet range kills it for most words |

---

## 10 — Language & Communication

### 10-1 ★ Multi-Cipher Decoder — Buildability: 5/5

Ten messages, ten encoding systems, first letters spell INFLECTION. This
is a constructor's dream. You control every message. Each encoding is
independently verifiable. The worksheet is ten decode boxes. The section
reference (`codes/`) teaches every encoding the solver needs.

Construction: for each encoding, write a short message whose first word
starts with the target letter. Morse message starting with "I"? "INDIA
IS THE FIRST WORD." Braille message starting with "N"? "NEVER FORGET
THE DOTS." You have total freedom. The only constraint is that each
message must be unambiguously decodable and non-trivially short (a
one-word Morse message is too easy).

Ten encodings is a lot — but the pool already names them: Morse, Braille,
semaphore, pigpen, NATO phonetic, signal flags, ASL fingerspelling,
binary, Caesar, telephone keypad. All are well-defined, all are
enumerable, all have standard references. The solver's experience is a
delightful variety pack — each decode feels different.

INFLECTION as the answer word is outstanding for the Language section.
10 letters = 10 systems. Perfect fit.

**Verdict: Slot this. Prototype-ready today.**

### 10-2 — Rosetta Stone — Buildability: 3/5

Same message in three scripts. The concept is elegant but the
construction is tricky: you need the solver to *not* already know one of
the scripts. If they read Cyrillic, Latin, and Arabic, the puzzle is a
translation exercise, not a decryption. The mechanism depends on the
solver's script ignorance, which you cannot control.

Also: "use parallels to decode" is vague. Parallel structure in three
scripts gives you character-level correspondences, but only if the
scripts have similar character-level structure (alphabetic). Chinese,
which is logographic, would not parallel an alphabetic script at the
character level.

**Verdict: Elegant concept, execution depends heavily on script
selection. Needs more mechanism definition.**

### 10-3 — Phonetic Riddle — Buildability: 4/5

IPA symbols that sound like an English phrase. This is a well-known
puzzle type (rebus by sound). Construction: write an English phrase in
IPA. The solver must read IPA (taught in `linguistics/`) and pronounce
it to hear the answer.

Buildable: IPA transcription is deterministic. The answer must be a
phrase that sounds like itself in IPA, which is... every phrase. The
real question is whether the solver can read IPA fluently enough to
pronounce it. Partial IPA knowledge leads to garbled pronunciation and
a failed puzzle.

Risk: this is a "say it aloud" puzzle — works in a group, awkward solo.
The Red Joker targets solo solvers. Silent reading of IPA and mentally
"hearing" it is possible but harder than speaking.

**Verdict: Buildable, fun in groups, awkward solo.**

### 10-4 — Etymological Chain — Buildability: 3/5

Trace a word across 5 languages to its PIE root. The construction
requires historically accurate etymological chains, which means research
(not creativity). You need a word whose PIE root translates to the
answer. PIE roots are often abstract and their "translations" are
debated among linguists.

Also: the solver needs to trace a word through Old French, Latin, and
PIE. Even with `linguistics/` and `world-languages/` as references,
this is specialized knowledge that most solvers lack and a reference
library may not provide at the needed depth.

**Verdict: Interesting but research-heavy construction and niche solver
knowledge.**

### 10-5 — Cipher Wheel Construction — Buildability: 3/5

Cut out two discs, assemble, decode. The construction of the page
template is straightforward (two concentric circles with alphabets). The
problem is physicality: cutting circles from a book is destructive (you
lose the content on the reverse side of the page), and the pin/fastener
is not provided.

This would work better as a tear-out insert (perforated card stock) than
a regular book page. Format-dependent.

**Verdict: Format-dependent. If the book has tear-out inserts, this is
great. If not, destructive.**

### 10-6 — Semaphore / Flag Reading — Buildability: 4/5

Stick figures holding flags, decode via semaphore alphabet. Highly
buildable: draw N stick figures, each in a semaphore position. The
solver looks up the semaphore alphabet in `codes/` and decodes. The
visual is clear and engaging on a page.

But: this is a subset of 10-1 (which already includes semaphore as one
of ten systems). If 10-1 is selected, 10-6 is redundant.

**Verdict: Solid standalone, redundant if 10-1 is selected.**

### 10 Section Summary

| ID | Name | Build | Notes |
|----|------|:-----:|-------|
| 10-1 ★ | Multi-Cipher | **5** | Best in section. Best in pool. Slot it. |
| 10-2 | Rosetta Stone | **3** | Script selection tricky |
| 10-3 | Phonetic Riddle | **4** | Awkward solo |
| 10-4 | Etymological Chain | **3** | Research-heavy |
| 10-5 | Cipher Wheel | **3** | Format-dependent |
| 10-6 | Semaphore | **4** | Redundant with 10-1 |

---

## 9 — Social Sciences

### 9-1 ★ Logic Grid — Buildability: 5/5

Einstein's riddle with social science concepts. Answer: INCENTIVE. This
is the most well-understood puzzle construction in the pool. Logic grid
puzzles have known construction techniques, known difficulty calibration,
and known worksheet formats (the elimination grid). I have built dozens.

Construction: define 5 entities, 5 attributes per entity (governance
type, economic model, legal tradition, etc.), and a set of clues that
uniquely determine the assignment. The solver fills the grid. Extraction:
the ordering of the solution (which nation has which system) produces
letters via some rule — first letters of governance types in alphabetical
order of nations, or similar.

INCENTIVE is 9 letters, which is more than the 5 entities can directly
produce. You either need 9 attributes to extract from, or a cluephrase
mechanism. With 5 entities × 5 attribute categories = 25 cells, there
is plenty of extraction space.

**Verdict: Slot this. Known construction. Prototypable in a few hours.**

### 9-2 — Prisoner's Dilemma Tournament — Buildability: 3/5

Five rounds of game theory, optimal strategy → binary → letters. The
five-round structure is clean. Each round has a payoff matrix; the
solver finds the optimal move (cooperate/defect = 0/1). Five bits of
binary = 5 bits. 5 bits encodes values 0-31, which gives one letter
(via A=1, ..., Z=26). For a multi-letter answer, you need multiple
5-round tournaments (5 tournaments × 5 rounds = 25 decisions for 5
letters). That is a LOT of payoff matrices.

Also: "optimal strategy" is ambiguous. In a single-shot game, defect is
always dominant. In iterated games, tit-for-tat is optimal. The puzzle
must specify single-shot vs. iterated, and the solver must know game
theory well enough to find the Nash equilibrium. That is a steep
knowledge requirement for "engaged reader, solo weekend."

**Verdict: Mechanism is sound but difficulty is high and the volume of
matrices is large.**

### 9-3 — Voting Paradox — Buildability: 3/5

Three elections, three systems, three winners. The construction requires
carefully tuned voter preferences such that plurality, ranked-choice,
and approval voting produce different winners. This is a known result in
social choice theory (Condorcet paradox) and examples exist.

The encoding is unclear: "which candidate wins under which system" gives
you 3 candidate names × 3 systems = 9 data points. How these become
letters of the answer is not specified. The mechanism needs more
definition.

**Verdict: Interesting concept, underspecified extraction.**

### 9-4 — Market Equilibrium — Buildability: 3/5

Supply/demand curves, equilibrium price → letter. You need to draw
curves on the page, have the solver find intersection points, and map
prices to letters. This is buildable (you control the curves), but the
price-to-letter mapping is arbitrary (A1Z26 from a price?) and the
graphical precision required is high. If the equilibrium is at $14.50
instead of $14.00, does the solver get N or O?

**Verdict: Graphical precision risk. Needs integer-valued equilibria,
which constrains the curve shapes to look artificial.**

### 9-5 — Treaty Network — Buildability: 2/5

Graph of nations and treaties, structure encodes answer. The problem:
graph-structural encoding (degree sequence, shortest path, etc.) is not
a natural puzzle extraction for most solvers. The solver must identify
the "right" graph property to read, which is an unsignaled meta-puzzle
on top of the main puzzle.

**Verdict: Extraction mechanism is too ambiguous. Most solvers would not
know what to do with the graph.**

### 9 Section Summary

| ID | Name | Build | Notes |
|----|------|:-----:|-------|
| 9-1 ★ | Logic Grid | **5** | Best in section. Known construction. Slot it. |
| 9-2 | Prisoner's Dilemma | **3** | High difficulty, many matrices |
| 9-3 | Voting Paradox | **3** | Underspecified extraction |
| 9-4 | Market Equilibrium | **3** | Graphical precision risk |
| 9-5 | Treaty Network | **2** | Ambiguous graph extraction |

---

## 8 — Technology

### 8-1 ★ Signal Tracing — Buildability: 4/5

ASCII system diagram, trace a signal through components, output decodes
to answer. Answer: TRANSISTOR. The construction: draw a signal path
through N components. Each component transforms the signal in a known
way (amplify, filter, modulate, invert). The solver must know what each
component does (from the encyclopedia) and apply the transformation.

This is buildable. The diagram is under your control. The transformations
are under your control. The output is deterministic. TRANSISTOR is 10
letters — you need 10 meaningful signal transformations, which is a
long chain. But signal processing chains of 10 stages are plausible
(input → preamp → filter → mixer → IF amp → demodulator → filter →
amplifier → DAC → output).

Risk: the "determine each component's effect" step requires domain
knowledge that the solver might not have even after reading the
encyclopedia. If the solver does not know that a mixer multiplies two
signals, the chain breaks. The puzzle needs the encyclopedia to be
sufficient — which means the technology section must actually teach
these components.

**Verdict: Strong mechanism. Verify that the encyclopedia teaches the
needed components.**

### 8-2 — Logic Gate Circuit — Buildability: 4/5

Circuit diagram with gates, binary output → ASCII → letters. This is a
classic computer science / EE puzzle. Construction: design a circuit
with known inputs, the solver traces gate-by-gate, the binary output
(read MSB to LSB) decodes to ASCII characters.

Highly buildable: logic circuit tracing is deterministic and the
construction is straightforward (work backward from the desired output
bits). The worksheet is the circuit with signal-value blanks at each
wire. For TRANSISTOR (10 letters), you need 10 × 7 = 70 output bits,
which means a large circuit. Better to use a shorter extraction (use the
circuit output as a key to decode something else, not as raw ASCII).

**Verdict: Solid. Keep the circuit small (5-6 output bits) and use the
output as a decryption key rather than raw ASCII.**

### 8-3 — Frequency Spectrum — Buildability: 2/5

Identify frequencies, map to notes/letters. The problem: frequency →
note mapping requires precise Hz values (A4 = 440 Hz, B4 = 493.88 Hz).
Reading precise Hz values from a printed spectrum chart is impractical —
graph resolution on paper is maybe ±50 Hz, which is a semitone at higher
frequencies. And the note-name alphabet is only {A, B, C, D, E, F, G},
the same limitation as Q3.

**Verdict: Graph precision insufficient. 7-letter alphabet. Not viable.**

### 8-4 — Bit Pattern / QR by Hand — Buildability: 4/5

Grid of black/white squares, simplified encoding. This is buildable as
a 5-bit encoding (like Baudot code) or 8-bit ASCII. The grid is visually
striking on a page. Construction: lay out the grid with the right
pattern. The solver counts rows and decodes.

Risk: actual QR codes are complex (error correction, positioning, mode
indicators). The puzzle must clearly NOT be a QR code, or solvers will
try to scan it and get confused. Labeling it "decode this grid" with a
provided encoding table is cleaner than implying QR.

**Verdict: Buildable and visually interesting. Needs clear framing to
avoid QR confusion.**

### 8-5 — PCB Trace Following — Buildability: 4/5

Follow traces on a circuit board, collect letters at components. This is
a path-following puzzle — the PCB is a maze with letters at nodes. Very
buildable: draw the PCB, place letters, define the trace to follow (e.g.,
"follow the power rail from Vcc to GND"). The visual is engaging and
thematically rich for Technology.

Risk: PCB diagrams can be visually dense. If the solver cannot
distinguish traces from each other, the puzzle fails. Use color or line
weight to distinguish the signal trace from ground planes.

**Verdict: Strong visual puzzle. Verify readability at print
resolution.**

### 8 Section Summary

| ID | Name | Build | Notes |
|----|------|:-----:|-------|
| 8-1 ★ | Signal Tracing | **4** | Good mechanism, verify encyclopedia coverage |
| 8-2 | Logic Gate Circuit | **4** | Classic, keep circuit small |
| 8-3 | Frequency Spectrum | **2** | Precision and alphabet problems |
| 8-4 | Bit Pattern | **4** | Clear framing needed |
| 8-5 | PCB Trace | **4** | Strong visual, verify readability |

---

## 7 — Mechanics

### 7-1 ★ Engineering Calculation — Buildability: 5/5

Five simple machines, calculate output force/velocity, numbers → A1Z26
→ TORQUE. This is textbook puzzle construction. You define the machine
parameters (lever arm lengths, pulley counts, gear ratios, incline
angles, piston areas). The solver applies the formulas (which the
encyclopedia teaches). The outputs are specific integers (20, 15, 18,
17, 21, 5 for T-O-R-Q-U-E via A1Z26).

Construction: work backward from the target numbers. Need T=20? Design
a lever where the mechanical advantage is 20 (or the output force is
20N, or the gear ratio is 20:1). Each machine has parameters you
control. The constraint is that the resulting numbers must look natural
(a gear ratio of 20:1 is fine; a gear ratio of 25:1 is unusual but
plausible; a gear ratio of 26:1 is suspicious).

Actually wait — TORQUE is only 6 letters but the brief says 5 simple
machines. T-O-R-Q-U-E is 6 letters. Five machines give 5 numbers.
Mismatch. Either use 6 machines (add screw or wedge) or change the
answer word to 5 letters (FORCE? LEVER?).

This is a fixable constraint. Add a 6th machine or change the word.
Either way, the mechanism is clean.

**Verdict: Excellent. Fix the 5-vs-6 mismatch. Prototype-ready.**

### 7-2 — Gear Train — Buildability: 4/5

Gear train diagram, tooth counts → output RPM → letters. This is a
subset of 7-1 (gear train is one of the simple machines). As a
standalone, the visual is engaging and the math is straightforward
(gear ratio = teeth_driven / teeth_driver, RPM_out = RPM_in / total
ratio).

But if 7-1 already includes a gear train, this is redundant. And a
standalone gear train puzzle producing a 6+ letter word needs 6+ stages,
which is a LOT of gears to draw legibly.

**Verdict: Redundant with 7-1. Only viable if 7-1 is dropped.**

### 7-3 — Rube Goldberg Chain — Buildability: 3/5

Elaborate chain reaction, identify each stage's mechanical principle,
first letters spell answer. The visual is inherently delightful — I love
the concept. But: drawing a Rube Goldberg machine in ASCII/print that
is both legible and visually fun is hard. Real Rube Goldberg drawings
are hand-illustrated with enormous detail. An ASCII approximation will
look cramped.

The extraction (first letter of each principle) constrains the
principles to start with the right letters. TORQUE = T, O, R, Q, U, E.
O for... Oscillation? Okay. Q for... that's hard. Quenching? Not a
mechanical principle. The answer word constrains available principles.

**Verdict: Delightful concept, hard to draw, Q-words are a problem for
TORQUE. Try FULCRUM: F(friction), U(uniform motion), L(lever),
C(compression), R(rotation), U(uplift), M(momentum). More findable.**

### 7-4 — Bridge Structural Analysis — Buildability: 4/5

Truss analysis: tension/compression → binary → letters. This is a
well-defined engineering calculation. For a simple truss with N members,
T/C analysis gives N bits. TORQUE (6 letters) in binary needs 6 × 5 =
30 bits (using 5-bit encoding) or 6 × 8 = 48 bits (ASCII). A truss
with 30-48 members is large but not unreasonable for a Pratt or Warren
truss.

Construction: design a truss, solve it for T/C, verify the binary
encodes correctly. The solver must do method of joints or sections on
paper — this is real engineering analysis, which is educational but
potentially difficult for non-engineers.

**Verdict: Niche audience but mechanically sound. Good for a structural
engineering enthusiast.**

### 7-5 — Fluid Flow Path — Buildability: 3/5

Pipe network, calculate which branch fluid takes, path collects letters.
The physics (Bernoulli/Poiseuille) is real but the calculation requires
diameter, pressure, and length data for every segment. The solver must
do fluid dynamics by hand, which is calculation-heavy.

Also: fluid network analysis can have non-obvious solutions (parallel
paths with flow splitting). You need a network topology where each
junction has a binary choice (one path clearly dominates), not a
realistic network with distributed flow.

**Verdict: Calculation-heavy, needs unrealistic network simplification.**

### 7 Section Summary

| ID | Name | Build | Notes |
|----|------|:-----:|-------|
| 7-1 ★ | Engineering Calc | **5** | Fix 5 vs 6 mismatch. Excellent. |
| 7-2 | Gear Train | **4** | Redundant with 7-1 |
| 7-3 | Rube Goldberg | **3** | Drawing + Q-constraint problems |
| 7-4 | Bridge Analysis | **4** | Sound but niche |
| 7-5 | Fluid Flow | **3** | Calculation-heavy, unrealistic simplification |

---

## 6 — History & Ideas

### 6-1 ★ Primary Source Detective — Buildability: 5/5

Identify 8 documents from opening lines, chronological order + extract.
Answer: PARADIGM. This is a pure research-and-identify puzzle. The
construction: select 8 primary sources with recognizable opening lines,
ordered chronologically with extraction from author names.

You control the source selection entirely. The constraint is that
extraction from author names (in chronological order) must spell
PARADIGM. 8 sources, 8 letters. For each letter, find a primary source
whose author's name contains that letter at a specific position, and
whose date falls in the right chronological slot.

This is a constraint-satisfaction problem but over a HUGE search space
(thousands of primary sources across history). Solvable with research.
The solver experience is satisfying: "I know this quote!" or "Let me
look this up." The educational value is high — the solver reads real
primary sources.

**Verdict: Slot this. Research-intensive construction but guaranteed
solvable.**

### 6-2 — Historical Map Overlay — Buildability: 2/5

Overlay maps from different eras, differences form letters. Same problem
as Q4 (Color Overlay): requires precise page registration when
overlaid. Additionally, historical map differences are complex (boundary
changes are blobs, not letter shapes). The claim that "changed boundaries
form letter shapes" is aspirational.

You could design fictional maps where the differences ARE letters — but
then they are not real historical maps, which undercuts the History
theme.

**Verdict: Registration problem + letter-shape implausibility. Pass.**

### 6-3 — Philosophical Argument Chain — Buildability: 4/5

Follow an argument, classify valid/fallacy, binary → letters. This is
buildable: write an argument with N steps. Some steps are valid, some
contain named fallacies. The solver identifies which is which using
`philosophy/` and `logic/`. Valid=1, fallacy=0. Binary decodes to
letters.

PARADIGM is 7 letters. 7 × 5 bits = 35 steps in the argument. Or 7 × 8
bits = 56 steps. That is a VERY long argument. Better: use 7 arguments,
each with one valid/fallacy judgment. But binary from 7 single bits only
gives 0-127, encoding one character. So you need 7 arguments × 5 bits
each = 35 total judgments across 7 sub-arguments.

This is getting complex. Simpler: each argument has a named fallacy (or
"valid"). First letters of the fallacy names spell PARADIGM. P = Post
hoc. A = Ad hominem. R = Red herring. A = Appeal to authority.
D = Denying the antecedent. I = Ignoratio elenchi. G = Genetic fallacy.
M = Modus ponens (the one valid step!). That is elegant and buildable.

**Verdict: Use the fallacy-names extraction, not binary. Then
buildability jumps to 4/5.**

### 6-4 — Cause-and-Effect Web — Buildability: 3/5

Historical causation web, longest chain encodes answer. The problem:
"longest chain" in a directed graph is a well-defined concept but the
solver must identify it by inspection. In a complex web, this is
non-trivial. Also, there might be ties (multiple longest paths), making
the answer ambiguous.

Construction: design a DAG with a unique longest path, where events on
that path contribute the right letters. Achievable but requires careful
graph design to avoid alternate paths of equal length.

**Verdict: Solvable construction but ambiguity risk.**

### 6-5 — Fairy Tale Logic — Buildability: 3/5

Narrative logic puzzle with mythological constraints. This is a dressed-
up logic grid (like 9-1) in fairy-tale language. The construction is the
same as any logic puzzle, with the flavor text drawn from mythology.
Buildable, but thematically overlapping with 9-1 (both are logic
deduction puzzles).

**Verdict: Builds fine but duplicates 9-1's mechanism. Do not slot both.**

### 6 Section Summary

| ID | Name | Build | Notes |
|----|------|:-----:|-------|
| 6-1 ★ | Primary Source | **5** | Slot this. Research-heavy but guaranteed. |
| 6-2 | Map Overlay | **2** | Registration + letter-shape problems |
| 6-3 | Argument Chain | **4** | Fallacy-names extraction is elegant |
| 6-4 | Cause-Effect Web | **3** | Ambiguity risk |
| 6-5 | Fairy Tale Logic | **3** | Duplicates 9-1 mechanism |

---

## 5 — Life Sciences

### 5-1 ★ Codon Decoding — Buildability: 5/5

DNA → mRNA → codons → amino acids → single-letter codes → GENETIC. I
said in Round 1 that this was the best seed in the hunt (tied with the
Language cipher). Nothing has changed. The mechanism is biologically
real, the encoding is unambiguous, the amino acid single-letter code is
a published standard, and the answer word GENETIC uses only letters that
exist in the amino acid code (G, E, N, E, T, I, C — all valid amino
acid single-letter codes).

Verification: G = Glycine (Gly), E = Glutamic acid (Glu), N =
Asparagine (Asn), E = Glu, T = Threonine (Thr), I = Isoleucine (Ile),
C = Cysteine (Cys). All valid. Seven codons needed: GGN, GAR, AAY, GAR,
ACN, AUH, UGY (using standard wobble notation). Each codon maps to
exactly one amino acid. No ambiguity.

Construction: write a 21-nucleotide DNA sequence (7 codons × 3 bases).
The solver transcribes to mRNA, groups into codons, looks up the genetic
code table (in the encyclopedia), and reads single-letter codes. Worksheet:
DNA strand with transcription/translation blanks. Done.

**Verdict: The single most buildable puzzle in the entire pool. Slot it.
Build it first if you want a confidence boost.**

### 5-2 — Phylogenetic Tree Traversal — Buildability: 3/5

Climb a phylogenetic tree, branch points contribute letters. The
construction: draw a tree with specific species at leaves. The solver
traces a path, identifies common ancestors at each node. The "key trait"
of each ancestor contributes a letter.

The problem: "key trait" is ambiguous. What is the key trait of the
common ancestor of humans and chimps? Bipedalism? Opposable thumbs?
Social behavior? The solver must pick the "right" trait, which means
you need the encyclopedia to unambiguously name one trait per node. This
requires tight content alignment.

**Verdict: Interesting but disambiguation of "key trait" is hard.**

### 5-3 — Metabolic Pathway — Buildability: 4/5

Follow glucose through metabolism, first letters of intermediates spell
answer. The intermediates of glycolysis are: Glucose → Glucose-6-P →
Fructose-6-P → Fructose-1,6-BP → DHAP/G3P → 1,3-BPG → 3-PG → 2-PG →
PEP → Pyruvate. First letters: G, G, F, F, D/G, B, P, P, P, P. Too
many P's and not a useful set.

Krebs cycle: Acetyl-CoA → Citrate → Isocitrate → α-Ketoglutarate →
Succinyl-CoA → Succinate → Fumarate → Malate → Oxaloacetate.
First letters: A, C, I, K, S, S, F, M, O. Better variety but you are
locked to these specific letters (biology does not let you swap
intermediates). Answer must be an anagram subset of {A, C, I, K, S, S,
F, M, O}.

This is extremely constraining. The mechanism works only if the answer
word happens to be spellable from real metabolic intermediates' first
letters. GENETIC cannot be spelled. HELIX cannot. The answer word must
be reverse-engineered from available biochemistry.

**Verdict: Mechanism locks you to specific letters you cannot change.
Answer word must be found by searching, not chosen.**

### 5-4 — Punnett Square Genetics — Buildability: 4/5

Genetic crosses, phenotype ratios → letters. The classic ratios are 3:1
(monohybrid), 9:3:3:1 (dihybrid), 1:2:1 (incomplete dominance). Mapping
ratios to letters: 3:1 gives you numbers 3 and 1 → C and A? Or the
total ratio 4 → D? The mapping is arbitrary unless you define a specific
rule.

Better approach: the number of offspring in a specific phenotype class.
E.g., out of 16 F2 offspring, 9 are wild-type → 9 = I. You control the
cross design, so you control the expected ratio. For simple ratios (3:1,
1:1, etc.), the numbers are small and A1Z26-able.

**Verdict: Buildable with defined number→letter rule. Answer word
constrained to small A1Z26 values (1-16 range).**

### 5-5 — Cell Organelle Labeling — Buildability: 4/5

Label a cell diagram, first letters spell answer. You draw the cell. You
place organelles in clockwise order such that their first letters spell
the answer. GENETIC: G(Golgi), E(Endoplasmic reticulum), N(Nucleus),
E(Endosome), T(? — no T organelle), I(? — no I organelle), C(Centriole).

T: tough. No standard organelle starts with T. "Transport vesicle"? Not
a standard organelle name. I: "Intermediate filament"? That is a
cytoskeletal component, not an organelle.

The available organelle first letters are roughly: C(centriole,
chloroplast, cytoplasm), E(ER, endosome), G(Golgi), L(lysosome),
M(mitochondria, membrane), N(nucleus, nucleolus), P(peroxisome),
R(ribosome), V(vacuole). Missing: A, B, D, F, H, I, J, K, O, Q, S, T,
U, W, X, Y, Z.

This is a severe alphabet limitation. GENETIC needs T and I, neither of
which maps to a standard organelle. The answer word is constrained to
organelle initials.

**Verdict: Alphabet too limited for most answer words. Check word
viability before committing.**

### 5-6 — Epidemic Network — Buildability: 3/5

Trace disease spread, infected initials spell answer. A network-tracing
puzzle where you control the network, transmission rules, and individual
names. Construction: assign names to nodes such that infection order
produces the answer word's letters.

This is buildable but the "transmission rules" need to be deterministic
and teachable. If transmission depends on proximity + immunity + contact
rate, the solver must execute a complex simulation. If it is simpler
(e.g., "infect all direct contacts, highest-degree first"), it is a
graph traversal puzzle — buildable.

**Verdict: Buildable with simplified transmission rules.**

### 5 Section Summary

| ID | Name | Build | Notes |
|----|------|:-----:|-------|
| 5-1 ★ | Codon Decoding | **5** | Best in pool. Verified answer word. |
| 5-2 | Phylogenetic Tree | **3** | Trait disambiguation hard |
| 5-3 | Metabolic Pathway | **4** | Locked to real biochemistry letters |
| 5-4 | Punnett Square | **4** | Small number range |
| 5-5 | Cell Labeling | **4** | Organelle alphabet limited |
| 5-6 | Epidemic Network | **3** | Needs simplified rules |

---

## 4 — Material Culture

### 4-1 ★ Element Identification — Buildability: 5/5

Seven riddle-clues about elements, first letters spell CASTING. C =
Carbon, A = Aluminum, S = Silver (Argentum? — no, Silver starts with S),
T = Tin, I = Iron (wait — Iron starts with I? no, I = Iridium? or
Indium?). Let me re-read: "Carbon, Aluminum, Silver, Tin, Iron, Nickel,
Gold." First letters: C, A, S, T, I, N, G.

Wait — Iron starts with I, not F (that's the symbol Fe). And Gold starts
with G, not A (that's Au). The puzzle uses common English names, not
chemical symbols. C(Carbon), A(Aluminum), S(Silver), T(Tin), I(Iron),
N(Nickel), G(Gold) = CASTING. Verified.

Construction: write 7 riddle-clues. Each riddle describes an element's
properties (density, color, melting point, uses, history). The solver
identifies the element from the Material Culture encyclopedia entries.
You control the riddle text entirely.

This is trivially buildable. The riddles can reference real content from
`periodic-table/`, `metalworking/`, `jewelry/`, etc. The solver's
experience is satisfying (identify the element → aha, first letters
spell CASTING). The worksheet is 7 riddle-and-answer blanks.

**Verdict: Slot this. Prototypable in an hour.**

### 4-2 — Craft Process Ordering — Buildability: 4/5

Steps of a craft out of order, correct sequence + extraction. Buildable:
pick a craft process (e.g., lost-wax casting), list its steps out of
order, have the solver reorder using `metalworking/` or `ceramics/`.
Extract letters from step names at specific positions.

The constraint: step names must be real craft terminology AND the
extracted letters must spell the answer. This is a two-way constraint
(correct order + correct extraction), but you choose which letters to
extract from each step, so the extraction side is flexible.

**Verdict: Solid backup to 4-1.**

### 4-3 — Textile Pattern Binary — Buildability: 3/5

Weaving draft where over/under = 1/0. The visual is beautiful on a page
— a weaving draft grid is inherently attractive. But: reading binary
from a weaving pattern requires the solver to distinguish over from under
in a printed grid. With black/white squares (drawdown notation), this is
just a bitmap — same as 8-4 (Bit Pattern). The "textile" framing adds
theme but the mechanism is identical.

Risk: if the solver does not know weaving notation, they cannot read the
grid. The encyclopedia must teach drawdown notation for this to work.

**Verdict: Visually appealing, mechanically identical to 8-4. Needs
weaving-notation teaching in the encyclopedia.**

### 4-4 — Glaze Chemistry — Buildability: 2/5

Ceramic glaze oxide ratios → letters. The ratios are real chemistry
(unity molecular formula), but simplifying oxide ratios to small integers
is not always possible (glaze chemistry uses irrational numbers like
0.3:0.7:3.5 for Al2O3:RO:SiO2). Forcing integer ratios makes the
chemistry unrealistic.

Also: the number of common glaze oxides is small (SiO2, Al2O3, CaO,
MgO, K2O, Na2O, Fe2O3). You get 7 ratios at most, constraining the
answer word to 7 letters or fewer with values in a small range.

**Verdict: Chemistry constrains the numbers too tightly. Not viable for
arbitrary answer words.**

### 4-5 — Periodic Table Spelling — Buildability: 3/5

Spell answer using element symbols. CASTING: Ca-S-Ti-N-G. Ca = Calcium,
S = Sulfur, Ti = Titanium, N = Nitrogen, G = ? No element has symbol G.
The brief itself catches this failure. For other answer words: you need
every letter or pair of letters to be a valid element symbol. This
constrains the answer word to a subset of the ~118 element symbols.

Running "CRUCIBLE" through element symbols: C-Ru-Ci-B-Le? Ci is not an
element. Cr-U-C-I-B-Le? Le is not an element. Cr-U-Ci... nope. This
approach requires reverse-engineering the answer word from element symbol
constraints, which is the tail wagging the dog.

**Verdict: Answer word must be designed around element symbols, not the
other way around. Constraining.**

### 4-6 — Kiln Temperature Profile — Buildability: 3/5

Temperature-vs-time graph, peak temps → letters. Same graph-precision
concern as 9-4 (Market Equilibrium). The solver reads temperatures from
a graph — if they read 1050°C instead of 1040°C, the extraction breaks.
You need temperatures at round numbers with clear graph markings.

If you use cone numbers instead of temperatures (Cone 06 = ~1000°C,
Cone 6 = ~1220°C), the numbers are small (1-12) and map cleanly to
A1Z26. Cone numbers are native ceramics vocabulary. Better mechanism.

**Verdict: Use cone numbers, not raw temperatures. Then 3/5 → 4/5.**

### 4 Section Summary

| ID | Name | Build | Notes |
|----|------|:-----:|-------|
| 4-1 ★ | Element ID | **5** | Best in section. Trivially buildable. |
| 4-2 | Craft Process | **4** | Solid backup |
| 4-3 | Textile Binary | **3** | Same as 8-4 with theming |
| 4-4 | Glaze Chemistry | **2** | Chemistry constrains numbers |
| 4-5 | PT Spelling | **3** | Answer word constrained by symbols |
| 4-6 | Kiln Temp Profile | **3** | Use cone numbers → 4/5 |

---

## 3 — Earth & Space

### 3-1 ★ Connect-the-Dots Star Chart — Buildability: 5/5

Seven groups of celestial objects, identify and plot, each group traces
a letter, spelling EQUINOX. This is a beautiful puzzle. The construction:
describe 7 groups of celestial objects poetically (without naming them).
Each group, when plotted on a coordinate grid, traces a letter shape.
Seven letters → EQUINOX.

You control the descriptions, the coordinate grid, and which celestial
objects to include. The constraint is that real celestial objects must
exist at positions that trace each letter. For a custom coordinate grid
(not actual RA/Dec), you can place objects wherever you want. For an
actual sky map, you would need to find constellations/stars that happen
to form letter shapes — but the brief says "coordinate grid," not "real
sky map."

The brief says this is "the Chicago Fire moment" — the solver draws on
the page and gets the aha. Physical interaction with the book. Memorable.
Educational (learning to identify celestial objects). Thematic (Earth &
Space section). The worksheet is a pre-printed coordinate grid with
plotting instructions.

EQUINOX is 7 letters, 7 groups. Clean 1:1 mapping.

**Verdict: Slot this. One of the best puzzles in the pool.**

### 3-2 — Geological Cross-Section — Buildability: 4/5

Rock layers with hidden words in strata names. The visual is a classic
geology diagram. Construction: label strata with real geological names
(Ordovician, Silurian, Devonian, etc.). Certain letters at certain
positions spell the answer. You choose the strata and their order (any
real stratigraphic column).

The extraction needs definition: "specific depths" → which letters? If
you take one letter per stratum at a defined position (e.g., the 3rd
letter of each stratum name), the solver needs to know the rule. That
rule must be signaled somehow.

**Verdict: Visually strong, extraction rule needs definition.**

### 3-3 — River Confluence Map — Buildability: 3/5

River confluences on a map, connected by river length, trace letters.
The problem: real river confluences are wherever geography put them. They
do not form letter shapes when connected in length order. You would need
to cherry-pick confluences that happen to form letters, which constrains
your river selection severely.

Also: "connected in order of river length" requires the solver to know
(or look up) the lengths of major rivers. This is data lookup, not
puzzle solving.

**Verdict: Geography constrains the letter shapes. Data-lookup heavy.**

### 3-4 — Mountain Silhouette — Buildability: 2/5

Mountain range profiles as letter shapes. Real mountain range silhouettes
do not look like letters. The Alps do not look like an A. The Rockies do
not look like an R. You would need very creative interpretation — which
means the solver's interpretation might differ from yours. Ambiguity is
fatal for puzzles.

**Verdict: Cute idea but subjective recognition is ambiguous. Pass.**

### 3-5 — Tectonic Plate Jigsaw — Buildability: 2/5

Cut-out plates, assemble like Pangaea, edge letters align. Physical
cut-out from the book — destructive. Also: tectonic plate shapes are
complex curves. Cutting them cleanly from a book page is impractical.
And aligning complex curved edges to reveal letters at edge junctions
requires precise cutting that scissors cannot achieve.

**Verdict: Cutting curves from paper is impractical. Pass.**

### 3-6 — Sundial Construction — Buildability: 1/5

Paper sundial, shadow at specific time points to answer. Requires: (1)
sunlight, (2) knowledge of your latitude (the gnomon angle depends on
latitude), (3) the correct time of day. If it is cloudy, nighttime, or
the solver is at the wrong latitude, the puzzle is unsolvable.

Environmental dependencies make this the least reliable puzzle in the
pool. You cannot control when or where the solver opens the book.

**Verdict: Cannot guarantee solvability. Hard pass.**

### 3 Section Summary

| ID | Name | Build | Notes |
|----|------|:-----:|-------|
| 3-1 ★ | Star Chart | **5** | Outstanding. Slot it. |
| 3-2 | Geological Cross-Section | **4** | Strong visual, needs extraction rule |
| 3-3 | River Confluence | **3** | Geography constrains shapes |
| 3-4 | Mountain Silhouette | **2** | Subjective recognition |
| 3-5 | Tectonic Jigsaw | **2** | Impractical cutting |
| 3-6 | Sundial | **1** | Environmental dependency |

---

## 2 — Natural World

### 2-1 ★ Organism Identification + Diagonal — Buildability: 4/5

Identify 5 organisms from characteristics, diagonal read spells NICHE.
N-I-C-H-E from a 5×5 diagonal means: 1st letter of organism 1 = N, 2nd
letter of organism 2 = I, 3rd letter of organism 3 = C, 4th letter of
organism 4 = H, 5th letter of organism 5 = E.

Organism 1 starts with N: Nightingale? Nautilus? Newt?
Organism 2, 2nd letter is I: BIson? LIchen? FIg?
Organism 3, 3rd letter is C: BuCkthorn? ArCtium? OrChid?
Organism 4, 4th letter is H: something with H in position 4: BusHbaby? MasHroom? Nope — MusHroom!
Organism 5, 5th letter is E: something with E in position 5: SnakE? HorsE? MaplE?

Plausible set: Nautilus, Bison, Orchid, Mushroom, Maple. All identifiable
from the Natural World section. The diagonal is clean.

Construction: write 5 characteristic descriptions (habitat, morphology,
behavior) without naming the organism. The solver identifies each using
the encyclopedia. The diagonal read is signaled by the worksheet layout
(a grid with highlighted diagonal).

**Verdict: Clean, verified, buildable. The V3 score of 26/30 was
conservative.**

### 2-2 — Food Web Traversal — Buildability: 3/5

Trace energy through a food web, path spells word. The visual is a
directed graph (organisms as nodes, arrows for predation). The solver
traces from producer to apex predator. Letters at organisms on the path
spell the answer.

Problem: "multiple valid paths exist — only one spells a real word."
This means the solver must try paths until one spells something. That is
trial and error, not deduction. A solver could get stuck trying paths
that almost-spell words. Better: have exactly one path from producer to
apex predator (a linear food chain hidden in a web).

**Verdict: Trial-and-error risk unless the path is unique. Needs
redesign.**

### 2-3 — Leaf / Mushroom ID Key — Buildability: 4/5

Dichotomous key, classify specimens, classifications encode letters.
This is a well-structured puzzle: binary choices at each node, a
determined path to a classification. The solver follows the key using
visual specimen illustrations. The classification name (or its position
in the key) gives a letter.

Construction: design a dichotomous key with N terminal nodes. Each
terminal = one letter. The solver classifies specimens by following the
key. The specimen order gives the letter order.

Beautiful intersection of puzzle and field guide methodology. The visual
(specimen illustrations + branching key) is rich and page-filling.

**Verdict: Strong puzzle. Well-defined mechanism.**

### 2-4 — Birdsong as Morse — Buildability: 3/5

Spectrograms of birdsong, long/short = dash/dot. Clever concept. But:
spectrogram resolution on a printed page is limited. Real birdsong
spectrograms have complex harmonic structure — distinguishing "short"
from "long" notes requires simplified spectrograms (which are
essentially invented diagrams, not real birdsong).

Also: this is a Morse puzzle, which overlaps with 10-1 (which already
includes Morse as one of ten systems). Mechanism overlap.

**Verdict: Cool concept, spectrogram legibility concerns, overlaps
with 10-1.**

### 2-5 — Spice Route — Buildability: 3/5

Identify spices, plot origins, trace route spells word. Similar to 3-3
(River Confluence) — real geographic positions constrain letter shapes.
The spice origins are fixed by geography (pepper = India, cinnamon = Sri
Lanka, cloves = Maluku). These positions, connected, form an arbitrary
path — not letter shapes.

Unless: you use a grid map where the spice origins happen to fall on
grid positions that trace letters. On a coarse enough grid, you can
place markers anywhere. But then it is a "plot points, connect dots"
puzzle — essentially 3-1 (Star Chart) with a different theme.

**Verdict: Same mechanism as 3-1 with weaker execution. Redundant.**

### 2 Section Summary

| ID | Name | Build | Notes |
|----|------|:-----:|-------|
| 2-1 ★ | Organism ID | **4** | Verified diagonal. Solid. |
| 2-2 | Food Web | **3** | Trial-and-error risk |
| 2-3 | Leaf/Mushroom Key | **4** | Strong mechanism |
| 2-4 | Birdsong Morse | **3** | Spectrogram + overlap concerns |
| 2-5 | Spice Route | **3** | Redundant with 3-1 |

---

## A — People

### A-1 ★ Influence Chains — Buildability: 5/5

Trace intellectual lineage (who taught whom), chain order gives
extraction order, letters from names spell POLYMATH. The construction:
describe N intellectual inheritance relationships. The solver identifies
each figure. The chain order (teacher → student → student's student)
determines the extraction order. A specific letter from each figure's
name (by position in chain) contributes to POLYMATH.

Seven letters in POLYMATH. Seven figures in the chain. Position 1: take
letter 1 from figure 1's name → P. Position 2: take letter 2 from
figure 2's name → O. Etc.

Figure 1: name starts with P → Plato, Pascal, Poincare, Planck
Figure 2: 2nd letter is O → some name with O as 2nd letter: Bohr?
Noether? Fourier? Go with name where 2nd letter = O.

The constraint is solvable: for each chain position, find a historical
figure whose name has the correct letter at the correct position AND who
has a plausible intellectual lineage connection to the adjacent figures.
This requires research but the search space (famous thinkers across all
fields) is enormous.

**Verdict: Slot this. Research-intensive but high-confidence buildable.**

### A-2 — Portrait Gallery — Buildability: 4/5

Identify 8 people from achievements, initials spell answer. Similar to
6-1 (Primary Source Detective) but using achievements instead of quotes.
Clean, buildable, but thematically overlapping with 6-1.

POLYMATH: 8 people whose initials are P, O, L, Y, M, A, T, H.
P = Pythagoras? Pascal? O = Oppenheimer? Ohm? L = Leibniz? Lovelace?
Y = Young (Thomas)? This is findable.

**Verdict: Solid mechanism, overlaps with 6-1.**

### A-3 — Timeline of Overlapping Lives — Buildability: 3/5

Find overlapping lifetimes, connections encode answer. The mechanism is
underspecified: "the connection word encodes the answer" — what
connection? How does a conceptual connection between two thinkers become
a letter? This needs much more definition.

**Verdict: Underspecified. Needs mechanism design.**

### A-4 — Letter Exchange — Buildability: 3/5

Famous correspondences, extract from real letters. Finding real,
attributable correspondence excerpts that contain specific extractable
words is a research task. The construction is doable but every excerpt
must be verified against historical sources.

Risk: real letters are copyrighted until ~70 years after the author's
death (varies by jurisdiction). Using pre-1950 letters is safe.

**Verdict: Research-heavy, copyright considerations.**

### A-5 — Invention Dependency Chain — Buildability: 4/5

Dependency graph of inventions, trace critical path, inventor names
encode answer. Similar to A-1 (Influence Chains) but using inventions
instead of intellectual lineage. The construction is the same: a
directed graph with a unique longest path, names at nodes contribute
letters.

**Verdict: Solid, but overlaps significantly with A-1.**

### A Section Summary

| ID | Name | Build | Notes |
|----|------|:-----:|-------|
| A-1 ★ | Influence Chains | **5** | Best in section. Slot it. |
| A-2 | Portrait Gallery | **4** | Overlaps with 6-1 |
| A-3 | Overlapping Lives | **3** | Underspecified |
| A-4 | Letter Exchange | **3** | Research + copyright |
| A-5 | Invention Dep Chain | **4** | Overlaps with A-1 |

---

## X — Cross-Section, Visual, and Physical Puzzles

These are the wild cards. Some are spectacular concepts that require
engineering miracles to execute. Some are afternoon prototypes. Let me
separate the practical from the aspirational.

### X1 — Paper + Light (Shadows) — Buildability: 2/5

Cut-out polyhedron template, fold, shine flashlight, shadows spell
answer. This is the "legendary moment" candidate. I built the
rhombicosidodecahedron meta for PH 123. I know what 3D paper
construction requires. Here is the honest assessment:

**Will it actually work?** Probably not as described. The problem is
optical: for shadows to form legible letters, you need:

1. Point light source (flashlight qualifies)
2. Holes in the polyhedron that are shaped as letter silhouettes
3. A flat surface at the right distance and angle
4. A dark enough environment

Items 1 and 4 are solvable. Item 3 introduces the distance/angle
variable — the shadow scales and distorts with distance. Item 2 is the
killer: you need holes in a 3D surface that project AS LETTERS when
light passes through them. On a curved surface (polyhedron faces are
flat, but the assembly curves), the projection is non-trivial. A hole
that is a perfect "A" on a face will project as a trapezoid from most
angles.

You could use a simple box (cube or rectangular prism) where one face
has letter-shaped cutouts, and the opposite face is open (or acts as the
screen). That simplifies the optics enormously — it is essentially a
shadow box. But that is much less dramatic than a polyhedron.

**Prototype time:** A simple shadow box → one afternoon. A polyhedron
with optical letter cutouts → multiple days of iteration, and it might
not work at all.

**Verdict: Shadow box version is an afternoon prototype. Polyhedron
version is weeks of engineering with uncertain outcome. Build the
shadow box first. Upgrade to polyhedron only if shadow box succeeds
perfectly.**

### X2 — Color Overlay (pages to light) — Buildability: 2/5

Hold two pages to light, overlap reveals word. Same assessment as Q4.
Registration precision is the blocker. Cannot prototype without actual
print production.

**Verdict: Print-production dependent. Not prototypable at home.**

### X3 — Fold the Page — Buildability: 4/5

Fold page, distant elements meet, form word. This IS prototypable in an
afternoon. Print a page. Put letters at specific positions. Fold. See if
they align. The math is simple: a fold at position X brings position
X-d to meet position X+d. You need letter positions that, when folded
at the crease, bring the right letters together.

Risk: the fold must be along a line that the solver can find (a printed
fold line, a crease mark, or a clue in the content). If the fold line is
not obvious, the solver never tries it.

Also: folding a book page is slightly destructive (creasing). Some
solvers will resist.

**Verdict: Simple and prototypable. Needs clear fold-line signaling.**

### X4 — Golden Ratio Spiral — Buildability: 3/5

Multi-section puzzle where phi is the key. This is a Black Joker puzzle
(cross-section), not a Red Joker puzzle. As a design concept for Black
Joker, it is interesting. Buildability depends on whether four different
manifestations of phi (art, nature, music, math) all converge on a
useful decryption key. The "decryption" step is vague.

**Verdict: Black Joker material. Not for Red Joker ranking.**

### X5 — Fibonacci Structural Sequence — Buildability: N/A

Not a puzzle — an organizing principle for the 13 Red Joker puzzles. If
puzzles have 1, 1, 2, 3, 5, 8, 13 elements respectively, the solver who
notices the pattern can predict structure. This is a meta-structural
flourish, not a buildable puzzle.

**Verdict: Not a puzzle. Assess as a structural overlay if desired.**

### X6 — Musical Score Message — Buildability: 4/5

Note names spell a word. Same mechanism as Q3 but positioned as a cross-
section puzzle. Same 7-letter alphabet limitation. If the answer word
uses only {A, B, C, D, E, F, G}, this is trivially buildable (write
the notes on a staff). If not, it does not work.

**Verdict: Same as Q3 — alphabet-limited but trivially buildable within
that constraint.**

### X7 — Cipher Wheel Construction — Buildability: 3/5

Same as 10-5. Cut-out discs, assemble, decode. Same format dependency.

**Verdict: Same as 10-5.**

### X8 — Punch Card Overlay — Buildability: 3/5

Punch holes, overlay on text page, visible words are the answer. The
construction is straightforward: design a text page with the answer words
at specific positions. Design a mask page with holes at those positions.
The solver punches holes and overlays.

Punching holes in a book page is destructive. The mask page must align
precisely with the text page. If the pages are on the same leaf (front
and back), alignment is automatic but the text page gets punched too.
If they are different pages, alignment is manual and imprecise.

**Verdict: Fun mechanism, alignment + destructiveness concerns. Works
well if the mask is a tear-out card.**

### X9 — Mirror Puzzle — Buildability: 4/5

Mirror-reversed text, readable in reflection. Trivially buildable:
horizontally flip the text in layout. The solver holds the page to a
mirror. Da Vinci wrote this way, so the thematic connection is real.

Risk: the solver must have a mirror. Most bathrooms have one. Not a
serious constraint.

The "aha" is the moment the solver thinks to try a mirror. That moment
needs a trigger (da Vinci reference, "ECNEREFER" appearing as garbled
text that a solver might recognize as reversed).

**Verdict: Buildable in minutes. Needs a trigger clue for the mirror.**

### X10 — Tangram Letter Assembly — Buildability: 3/5

Cut tangram pieces, form letter shapes. Standard tangram sets have 7
pieces. You can form recognizable letter shapes with 7 pieces for many
(not all) letters. The solver needs to figure out which letter each
arrangement forms, which is visual recognition — potentially ambiguous
(is it an "N" or a "Z"?).

Also: cutting 7 tangram pieces from a book page is destructive and
requires careful cutting.

**Verdict: Some letter shapes are ambiguous. Destructive. Mid-tier.**

### X11 — Origami Fold — Buildability: 2/5

Fold following instructions, visible surfaces spell answer. Origami
instructions are hard to convey on paper without extensive diagramming
(10-20 step diagrams for even simple folds). The solver must execute
precise folds; imprecise folds misalign the visible letters.

Also: origami from a book page means the page must be detachable (or
the solver tears it out — destructive). And the paper weight of most
books is wrong for origami (too stiff or too floppy).

**Verdict: High instruction overhead, precision-dependent, paper-stock
issues. Not practical.**

### X12 — Five Senses Quintet — Buildability: N/A

Not a puzzle — an organizing principle. "Five puzzles, each engaging a
different sense." This could organize a subset of Red Joker puzzles
thematically, but it is not itself a buildable puzzle.

**Verdict: Organizing principle, not a puzzle.**

### X13 — River Letters — Buildability: 3/5

Same as 3-3 (River Confluence) — rivers plotted on a map trace letters.
Same geography constraint. Same issue: real rivers do not form letters.

**Verdict: Redundant with 3-3. Same problems.**

### X14 — Mountain Range Frequency — Buildability: 2/5

Elevation profiles as waveforms, frequency → notes → letters. Three
separate encoding steps (elevation → frequency → note → letter). Each
step introduces ambiguity and error. The frequency of a mountain range
profile is not a well-defined concept (Fourier analysis gives multiple
frequency components, not one). And the note-name alphabet is {A-G}.

**Verdict: Three-layer encoding, each layer lossy. Not viable.**

### X15 — Phenakistoscope / Zoetrope — Buildability: 1/5

Cut-out disc, spin, animation reveals word. I love this as a concept.
But: a phenakistoscope requires (1) cutting a precise circle, (2)
cutting thin viewing slits at exact intervals, (3) spinning at the right
speed, (4) viewing through the slits while spinning. The word appears
as a persistence-of-vision effect.

The construction is doable (phenakistoscope templates exist), but the
viewing experience is extremely finicky. Spin too fast → blur. Spin too
slow → flicker with no persistence. Wrong slit width → illegible. Wrong
ambient light → invisible. I have seen phenakistoscope demos fail in
controlled museum settings. In a home with a solver who has never seen
one, this will fail more often than it succeeds.

**Verdict: Beautiful idea. Will not work reliably. Park for a deluxe
edition with professional die-cut components.**

### X16 — Sundial — Buildability: 1/5

Same as 3-6. Requires sunlight. Cannot guarantee solvability.

**Verdict: Hard pass. Same as 3-6.**

### X17 — Stereo Pair — Buildability: 3/5

Cross-eye stereogram reveals hidden word. The construction is well-
defined: generate a stereo pair where the depth map encodes a word. Tools
exist for this (random-dot stereograms, parallel-view stereo pairs).

The problem: not everyone can see stereograms. Approximately 5-10% of
people have stereo vision deficits. Making a puzzle that 5-10% of
solvers physically cannot solve is bad design. Also, cross-eye viewing
gives some people headaches.

For a non-critical puzzle (one of 13, with the answer obtainable by
other means), this is acceptable. As the sole path to an answer, it
excludes solvers.

**Verdict: Buildable but accessibility concern. Only acceptable if
an alternative solve path exists.**

### X Section Summary

| ID | Name | Build | Notes |
|----|------|:-----:|-------|
| X1 | Paper + Light | **2** | Shadow box = afternoon; polyhedron = weeks |
| X2 | Color Overlay | **2** | Print-production dependent |
| X3 | Fold the Page | **4** | Simple and prototypable |
| X4 | Golden Ratio | **3** | Black Joker material |
| X5 | Fibonacci Struct | N/A | Organizing principle |
| X6 | Musical Score | **4** | Alphabet-limited |
| X7 | Cipher Wheel | **3** | Same as 10-5 |
| X8 | Punch Card | **3** | Alignment + destructiveness |
| X9 | Mirror Puzzle | **4** | Trivially buildable |
| X10 | Tangram Letters | **3** | Ambiguous + destructive |
| X11 | Origami Fold | **2** | Precision + paper-stock issues |
| X12 | Five Senses | N/A | Organizing principle |
| X13 | River Letters | **3** | Redundant with 3-3 |
| X14 | Mountain Freq | **2** | Three-layer lossy encoding |
| X15 | Phenakistoscope | **1** | Beautiful but will not work reliably |
| X16 | Sundial | **1** | Environmental dependency |
| X17 | Stereo Pair | **3** | Accessibility concern |

---

## Master Ranking — All 89 Candidates

### Tier 1: Buildability 5/5 — Prototype This Afternoon

| ID | Name | Section | Answer | Notes |
|----|------|---------|--------|-------|
| 5-1 ★ | Codon Decoding | Life Sciences | GENETIC | Best in pool. Biologically real encoding. |
| 10-1 ★ | Multi-Cipher Decoder | Language | INFLECTION | Ten encodings, total control, variety pack. |
| K1 ★ | Cipher Decryption | Computing | ALGORITHM | Clean mechanism, self-contained. |
| 9-1 ★ | Logic Grid | Social Sciences | INCENTIVE | Known construction, known tools. |
| 7-1 ★ | Engineering Calc | Mechanics | TORQUE | Fix 5↔6 mismatch. Otherwise ready. |
| 4-1 ★ | Element ID | Material Culture | CASTING | Seven riddles. One hour to prototype. |
| J1 ★ | Proof Completion | Math & Physics | SYMMETRY | Two Y-words needed; findable. |
| 6-1 ★ | Primary Source | History | PARADIGM | Research-intensive but guaranteed. |
| 3-1 ★ | Star Chart | Earth & Space | EQUINOX | The "draw on the page" moment. |
| A-1 ★ | Influence Chains | People | POLYMATH | Research-intensive but high confidence. |

### Tier 2: Buildability 4/5 — Buildable With Focused Work

| ID | Name | Section | Answer | Notes |
|----|------|---------|--------|-------|
| 8-1 ★ | Signal Tracing | Technology | TRANSISTOR | Verify encyclopedia teaches components. |
| 2-1 ★ | Organism ID | Natural World | NICHE | Verified diagonal. Conservative score. |
| Q1 | Crossword | Arts | PERSPECTIVE | Reliable but unexciting. |
| Q2 | Visual Rebus | Arts | PERSPECTIVE | High visual appeal. Disambiguation needed. |
| Q3 | Musical Staff | Arts | (constrained) | Only for {A-G} answer words. |
| K2 | Algorithm Exec | Computing | (flexible) | Strong backup to K1. |
| K5 | Binary Decoder | Computing | (flexible) | Buildable but thin. |
| J4 | Matrix Mult | Math/Physics | (flexible) | Keep 2x2. |
| J5 | Equation Balance | Math/Physics | (flexible) | Extraction path needs definition. |
| 10-3 | Phonetic Riddle | Language | (flexible) | Awkward solo. |
| 10-6 | Semaphore | Language | (flexible) | Redundant with 10-1. |
| 8-2 | Logic Gate | Technology | (flexible) | Keep circuit small. |
| 8-4 | Bit Pattern | Technology | (flexible) | Clear framing needed. |
| 8-5 | PCB Trace | Technology | (flexible) | Verify print readability. |
| 7-2 | Gear Train | Mechanics | (flexible) | Redundant with 7-1. |
| 7-4 | Bridge Analysis | Mechanics | (flexible) | Sound but niche. |
| 6-3 | Argument Chain | History | (flexible) | Fallacy-names version is elegant. |
| 5-3 | Metabolic Path | Life Sciences | (constrained) | Locked to biochemistry letters. |
| 5-4 | Punnett Square | Life Sciences | (constrained) | Small number range. |
| 5-5 | Cell Labeling | Life Sciences | (constrained) | Organelle alphabet limited. |
| 4-2 | Craft Process | Material Culture | (flexible) | Solid backup to 4-1. |
| 4-6 | Kiln Temp | Material Culture | (flexible) | Use cone numbers. |
| 2-3 | Leaf/Mushroom Key | Natural World | (flexible) | Strong mechanism. |
| A-2 | Portrait Gallery | People | (flexible) | Overlaps with 6-1. |
| A-5 | Invention Chain | People | (flexible) | Overlaps with A-1. |
| X3 | Fold the Page | Physical | (flexible) | Simple and prototypable. |
| X6 | Musical Score | Physical | (constrained) | Same as Q3. |
| X9 | Mirror Puzzle | Physical | (flexible) | Trivially buildable. |

### Tier 3: Buildability 3/5 — Requires Significant Construction Work

| ID | Name | Section | Notes |
|----|------|---------|-------|
| K3 | State Machine | Computing | Layout concerns |
| K4 | Stack Trace | Computing | Difficulty risk |
| Q6 | Golden Ratio | Arts | Use Fibonacci indices |
| Q7 | Fibonacci Seq | Arts | Organizing principle, not standalone |
| J2 | Symmetry Ops | Math/Physics | Tedious paper execution |
| J6 | Topology/Genus | Math/Physics | Alphabet range |
| 10-2 | Rosetta Stone | Language | Script selection tricky |
| 10-4 | Etymological Chain | Language | Research-heavy, niche |
| 10-5 | Cipher Wheel | Language | Format-dependent |
| 9-2 | Prisoner's Dilemma | Social Sci | High difficulty, many matrices |
| 9-3 | Voting Paradox | Social Sci | Underspecified extraction |
| 9-4 | Market Equilibrium | Social Sci | Graphical precision risk |
| 7-3 | Rube Goldberg | Mechanics | Drawing + Q-constraint |
| 7-5 | Fluid Flow | Mechanics | Calculation-heavy |
| 6-4 | Cause-Effect Web | History | Ambiguity risk |
| 6-5 | Fairy Tale Logic | History | Duplicates 9-1 |
| 5-2 | Phylogenetic Tree | Life Sciences | Trait disambiguation |
| 5-6 | Epidemic Network | Life Sciences | Simplified rules needed |
| 4-3 | Textile Binary | Material Culture | Same as 8-4 themed |
| 4-5 | PT Spelling | Material Culture | Constrained by symbols |
| 3-2 | Geo Cross-Section | Earth & Space | Needs extraction rule |
| 3-3 | River Confluence | Earth & Space | Geography constrains shapes |
| 2-2 | Food Web | Natural World | Trial-and-error risk |
| 2-4 | Birdsong Morse | Natural World | Spectrogram + overlap |
| 2-5 | Spice Route | Natural World | Redundant with 3-1 |
| A-3 | Overlapping Lives | People | Underspecified |
| A-4 | Letter Exchange | People | Research + copyright |
| X4 | Golden Ratio Spiral | Physical | Black Joker material |
| X7 | Cipher Wheel | Physical | Same as 10-5 |
| X8 | Punch Card | Physical | Alignment concerns |
| X10 | Tangram Letters | Physical | Ambiguous + destructive |
| X13 | River Letters | Physical | Redundant with 3-3 |
| X17 | Stereo Pair | Physical | Accessibility concern |

### Tier 4: Buildability 2/5 — High Construction Risk

| ID | Name | Section | Notes |
|----|------|---------|-------|
| Q4 | Color Overlay | Arts | Print-production dependent |
| Q5 | Anamorphic | Arts | Multi-day R&D |
| 9-5 | Treaty Network | Social Sci | Ambiguous graph extraction |
| 8-3 | Frequency Spectrum | Technology | Precision + 7-letter alphabet |
| 4-4 | Glaze Chemistry | Material Culture | Chemistry constrains numbers |
| 3-4 | Mountain Silhouette | Earth & Space | Subjective recognition |
| 3-5 | Tectonic Jigsaw | Earth & Space | Impractical cutting |
| 6-2 | Map Overlay | History | Registration + letter shapes |
| J3 | Geometric Construct | Math/Physics | Needs compass; letter legibility unverified |
| X1 | Paper + Light | Physical | Shadow box = afternoon; polyhedron = weeks |
| X2 | Color Overlay | Physical | Print-production dependent |
| X11 | Origami Fold | Physical | Precision + paper stock |
| X14 | Mountain Freq | Physical | Three-layer lossy encoding |

### Tier 5: Buildability 1/5 — Do Not Build

| ID | Name | Section | Notes |
|----|------|---------|-------|
| 3-6 | Sundial | Earth & Space | Requires sunlight. Unsolvable at night. |
| X15 | Phenakistoscope | Physical | Beautiful. Will fail reliably. |
| X16 | Sundial | Physical | Same as 3-6. |

---

## Physical Puzzles — The Honest Assessment

The pool has 17 physical/cross-section puzzles. Here is the prototype-
time reality:

### Afternoon Prototypes (< 4 hours)

| ID | Concept | What You Need |
|----|---------|---------------|
| X3 | Fold the Page | Printer, ruler, pencil. Print test page, fold, verify alignment. |
| X9 | Mirror Puzzle | Printer, mirror. Print reversed text, hold to mirror. 10 minutes. |
| X6 | Musical Score | Staff paper, knowledge of answer word in {A-G}. Write notes. |

### Weekend Prototypes (1-2 days)

| ID | Concept | What You Need |
|----|---------|---------------|
| X8 | Punch Card | Two printed pages, hole punch. Test alignment at multiple registration points. |
| X10 | Tangram | Card stock, scissors, ruler. Cut 7 pieces. Try to form each letter. |
| X1 (shadow box) | Paper + Light | Card stock, box cutter, flashlight. Build a simple box with letter cutouts. |
| X17 | Stereo Pair | Stereogram generator software. Generate, print, test cross-eye viewing. |

### Weeks of Engineering (and maybe failure)

| ID | Concept | Why It Takes Weeks |
|----|---------|-------------------|
| X1 (polyhedron) | Paper + Light 3D | 3D projection math, template iteration, optical testing |
| X2 / Q4 | Color Overlay | Need print production partner, paper stock testing, registration trials |
| Q5 | Anamorphic | Geometric distortion computation, angle testing, paper surface experiments |
| X11 | Origami | Fold sequence design, instruction diagramming, paper stock sourcing |
| X15 | Phenakistoscope | Disc template, slit engineering, speed calibration, persistence testing |

### Will Not Work

| ID | Concept | Why |
|----|---------|-----|
| X16 / 3-6 | Sundial | Weather, time, latitude |
| X14 | Mountain Frequency | Undefined "frequency," lossy encoding chain |
| 3-5 | Tectonic Jigsaw | Impractical curves |

---

## Kenny's Buildable 13

My recommended Red Joker lineup, optimized for constructibility, answer-
word achievability, mechanism variety, and solver experience:

| Slot | Section | Puzzle | Answer | Build | Mechanism Family |
|:----:|---------|--------|--------|:-----:|------------------|
| K | Computing | **K1 — Cipher Decryption** | ALGORITHM | 5 | Cipher |
| Q | Arts & Culture | **Q2 — Visual Rebus** | PERSPECTIVE | 4 | Visual decode |
| J | Math & Physics | **J1 — Proof Completion** | SYMMETRY | 5 | Fill-in-the-blank |
| 10 | Language | **10-1 — Multi-Cipher** | INFLECTION | 5 | Multi-cipher |
| 9 | Social Sciences | **9-1 — Logic Grid** | INCENTIVE | 5 | Logic deduction |
| 8 | Technology | **8-1 — Signal Tracing** | TRANSISTOR | 4 | System tracing |
| 7 | Mechanics | **7-1 — Engineering Calc** | TORQUE* | 5 | Calculation |
| 6 | History | **6-1 — Primary Source** | PARADIGM | 5 | Research + ID |
| 5 | Life Sciences | **5-1 — Codon Decoding** | GENETIC | 5 | Domain encoding |
| 4 | Material Culture | **4-1 — Element ID** | CASTING | 5 | Riddle + ID |
| 3 | Earth & Space | **3-1 — Star Chart** | EQUINOX | 5 | Plot + connect |
| 2 | Natural World | **2-1 — Organism ID** | NICHE | 4 | Diagonal read |
| A | People | **A-1 — Influence Chains** | POLYMATH | 5 | Chain + extract |

*Fix 5-machine vs. 6-letter mismatch (add a 6th machine or use FULCRUM).

**Mechanism variety check:**

| Family | Count | Puzzles |
|--------|:-----:|---------|
| Cipher / decryption | 2 | K1, 10-1 |
| Fill-in / proof | 1 | J1 |
| Visual decode | 1 | Q2 |
| Logic deduction | 1 | 9-1 |
| System tracing | 1 | 8-1 |
| Calculation | 1 | 7-1 |
| Research + identification | 2 | 6-1, 4-1 |
| Domain-native encoding | 1 | 5-1 |
| Plot + connect (physical) | 1 | 3-1 |
| Diagonal / positional read | 1 | 2-1 |
| Chain + extraction | 1 | A-1 |

Eleven mechanism families across 13 puzzles. Two small overlaps (K1/10-1
both use ciphers; 6-1/4-1 both use research+ID). The ciphers feel
completely different in practice (K1 is a single-cipher decryption; 10-1
is a ten-system variety pack). The research puzzles differ too (6-1 is
quotes → sources → dates; 4-1 is properties → elements → first letters).
I am satisfied with this variety.

**Average buildability: 4.77 / 5.** That is a set you can build.

---

## Build Order

The five puzzles to prototype first, in order:

### 1. Codon Decoding (5-1)

**Why first:** Highest confidence in the pool. The mechanism is verified
against the answer word. The encoding is a published biological standard.
You write a 21-nucleotide DNA sequence on a worksheet, provide a codon
table, and the solver translates. Build it, test it with one human, and
you have your first complete puzzle. This gives the team a confidence
boost and a quality benchmark.

**Prototype deliverable:** One worksheet page (DNA sequence + codon table
+ amino acid blanks + answer blank).

### 2. Multi-Cipher Decoder (10-1)

**Why second:** Tests the highest-variety puzzle in the set. Ten encoding
systems means ten mini-puzzles. Prototype two systems first (Morse +
Braille), verify they are fun and decodable, then build the other eight.
This is the longest individual puzzle in the set — prototyping early
catches scope problems.

**Prototype deliverable:** Two of ten encoding panels (Morse message +
Braille message) with decode worksheets.

### 3. Element Identification (4-1)

**Why third:** Tests the riddle format. If 4-1's riddles work, the same
format validates elements of 6-1 (identifying sources from quotes) and
A-1 (identifying thinkers from lineage descriptions). Three puzzles'
formats depend on "identify X from description Y." Prove the format
once.

**Prototype deliverable:** Three of seven riddle-clues with identification
blanks.

### 4. Star Chart Connect-the-Dots (3-1)

**Why fourth:** Tests the physical "draw on the page" experience. This
is the only puzzle where the solver permanently marks the book. Prototype
it to verify: (a) celestial object descriptions are identifiable, (b)
plotted points form legible letters, (c) the coordinate grid is usable.
Print the grid, plot the points yourself, and see if someone else can
read the letters.

**Prototype deliverable:** Coordinate grid + 2 of 7 object-group
descriptions + plotted letter verification.

### 5. Visual Rebus (Q2)

**Why fifth:** Tests the weakest slot in the Buildable 13. Q2 scored 4/5
because of disambiguation risk. Prototype 3-4 rebus images, show them to
5 people, and see if everyone gets the same answer. If disambiguation
fails, swap to Q1 (Crossword) — the reliable backup.

**Prototype deliverable:** Four rebus images with answer verification
testing.

---

## Alternate Slots — If Any Buildable 13 Puzzle Fails

| Primary | Build risk | Backup | Backup Build |
|---------|-----------|--------|:------------:|
| Q2 (Rebus) | Disambiguation | Q1 (Crossword) | 4 |
| 8-1 (Signal) | Encyclopedia gap | 8-5 (PCB Trace) | 4 |
| 2-1 (Organism ID) | Diagonal constraint | 2-3 (Dichotomous Key) | 4 |
| 7-1 (Engineering) | 5↔6 mismatch | 7-4 (Bridge Analysis) | 4 |

All backups are Tier 2, all score 4/5. The lineup is robust.

---

## Final Thoughts

The V3 starred selections are almost exactly what I would pick. That is
a good sign — the brainstorm correctly identified the best seed in each
section on the first pass. The pool's function is to provide backups and
stress-test the starred picks, and it does that well.

The physical puzzles (X-series) are mostly aspirational. X3 (Fold) and
X9 (Mirror) are the only afternoon-prototypable physicals. X1 (Paper +
Light) is worth a shadow-box prototype but should not be load-bearing
until it is proven. X15 (Phenakistoscope) is a museum exhibit, not a
book puzzle. Save it for the deluxe collector's edition that ships with
a spinning disc and a viewing slit.

The 89-puzzle pool is 5x larger than what you need. That is healthy —
it means you can afford to be ruthless about cutting. Cut everything
below 4/5. Build the Buildable 13. Playtest. Iterate. Ship.

My one strategic concern: K1 and 10-1 are both cipher puzzles. In a
13-puzzle set, two ciphers is fine if they FEEL different. K1 is "decrypt
one message with one cipher you learned" — a focused exercise. 10-1 is
"ten messages, ten systems, a variety pack" — a survey. The experiences
are distinct. But watch the ordering: do not place K and 10 adjacent in
the book. Separate them with at least 3-4 puzzles so the solver does not
feel cipher fatigue.

Build order starts tomorrow. Prototype 5-1 first. It will take an hour.
You will feel great. Then tackle the rest.

— Kenny
