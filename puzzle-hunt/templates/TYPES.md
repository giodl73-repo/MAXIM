# Puzzle Type Reference

Templates and guidance for each puzzle type supported by the toolkit. Use these as starting points — customize to fit your content.

---

## Cipher / Code-Breaking
**The solver decrypts a message using a system the content library teaches.**
- Ciphertext block (monospace)
- Key discovery requires reading the content (not given directly)
- Decryption worksheet: ciphertext | key | plaintext columns
- Best for: computing, language, history sections

## Crossword
**Clues reference content; highlighted cells extract the answer.**
- ASCII grid with numbered cells
- Across/Down clue list — every clue requires reading the content
- Highlighted extraction cells marked
- Best for: any section with rich terminology

## Logic Grid
**Deduce which attributes belong to which entities using constraint clues.**
- Setup paragraph with entities and attribute categories
- 8-12 clues using content-specific terminology
- Grid table for elimination
- Best for: social sciences, classification-heavy sections

## Multi-Encoding Decoder
**Multiple messages, each in a different encoding system.**
- N encoded messages
- System identification blank per message
- Decoded word blank per message
- First-letter extraction row
- Best for: language, codes, communication sections

## Identification / Riddle
**Identify items from oblique descriptions using the content library.**
- N descriptions (no names given)
- Identification blanks
- First-letter or diagonal extraction
- Add INTERLOCK: cross-references between riddles
- Best for: natural science, material culture, people sections

## Engineering Calculation
**Calculate values; numbers map to letters.**
- ASCII diagrams with given values
- Calculation workspace
- A1Z26 conversion
- CRITICAL: remove inline formulas — make solver find them in the content
- CRITICAL: add deduction layer — don't just "apply formula N times"
- Best for: mechanics, physics, technology sections

## Primary Source Detective
**Identify unattributed quotes from real sources.**
- Real quotes (fully accurate — NO fabrication)
- Identification blanks (author, work, date)
- Chronological ordering
- Surname first-letter extraction
- Best for: history, philosophy, literature sections

## Codon / Biological Encoding
**A DNA/RNA sequence encodes a message through the genetic code.**
- DNA sequence (template strand for added deduction)
- Transcription + translation workflow
- Single-letter amino acid code extraction
- CRITICAL: don't include the codon table — make solver find it
- Best for: life sciences, biology sections

## Star Chart / Map Plotting
**Identify objects, plot on a grid, groups trace letter shapes.**
- Blank coordinate grid provided
- Groups of objects described poetically (no names)
- Identification + coordinate blanks
- "What letter does each group form?" blanks
- Physical: the solver DRAWS on the page
- Best for: earth/space, geography sections

## Dichotomous Key / Classification
**Classify specimens through a branching identification key.**
- Specimens described by characteristics only
- Branching yes/no key structure
- Classification blanks
- Diagonal read extraction
- Best for: natural world, biology sections

## Phylogenetic Tree / Genealogy
**Trace paths through a tree; branch points encode letters.**
- Tree diagram with species/people at leaves
- Trait descriptions at branch points (shuffled)
- Path-tracing from specific pairs
- Letters collected at common ancestors
- Best for: biology, people/history sections

## Voting Paradox / Game Theory
**Same data, multiple systems, different outcomes.**
- Voter preference table
- Apply N different systems
- Different winners reveal the paradox
- Winners encode the answer
- Best for: social science, political science sections

## Visual Rebus
**Spatial arrangements of text/symbols represent concepts.**
- ASCII layouts where the ARRANGEMENT is the clue
- Each rebus = one concept from the content
- Identification + extraction
- Add INTERLOCK: rebuses that reference each other visually
- Best for: arts, music, architecture sections

## Musical Staff / Notation
**Notes on a staff spell a message through note names (A-G).**
- ASCII staff with notes on lines/spaces
- Clef changes add deduction
- Answer limited to letters A-G
- Best for: music, arts sections

## Philosophical Argument
**Identify valid vs. fallacious steps in an argument.**
- Multi-step argument using content-specific concepts
- Some steps valid, some contain named fallacies
- V/F identification + fallacy naming
- First letters of fallacy names encode the answer
- Best for: philosophy, logic, history sections

## Textile / Pattern Binary
**A visual pattern encodes binary data.**
- Grid of filled/empty cells (weave, mosaic, pixel art)
- Over=1, under=0 (or similar convention)
- Rows decode as N-bit binary numbers → A1Z26 → letters
- Solver must determine which symbol = 1 (not told directly)
- Best for: material culture, crafts, computing sections

## Rube Goldberg Chain
**Trace a chain reaction; each stage's principle gives a letter.**
- ASCII machine diagram
- Stages are interlocked (output of one feeds input of next)
- Identify the governing principle at each stage
- First letters spell the answer
- Best for: mechanics, physics, engineering sections

## Influence Chain / Letter Exchange
**Trace intellectual relationships between historical figures.**
- Descriptions of who taught/influenced whom (no names)
- Figure identification using content library
- Chain ordering gives extraction sequence
- Best for: people, history, science sections

## Frequency / Signal Analysis
**Identify frequencies in a spectrum; map to notes or letters.**
- Spectrum chart with peaks
- Separate signal from noise (harmonics, interference)
- Map fundamentals to musical notes
- Note names spell the answer
- Best for: technology, signal processing, music sections

## Geological Cross-Section
**Read rock layers; stratigraphic principles determine order.**
- ASCII cross-section with labeled strata
- Solver must apply superposition, cross-cutting, unconformities
- Chronological order → extraction from strata names
- Best for: earth science, geology sections

## Geometric Construction
**Compass-and-straightedge constructions form letter shapes.**
- Step-by-step construction instructions
- Each construction produces a shape that IS a letter
- Physical: solver draws on the page
- Best for: mathematics sections (especially as warm-up)
