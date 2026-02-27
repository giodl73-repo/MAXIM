# Puzzle Test: 13-Al-ALUMINUM

**Puzzle:** [13] Aluminum -- Dichotomous Key (Natural World)
**Card:** 2 of Clubs -- The Taxonomist
**Testers:** Lucas Pope, Rand Miller, Alex Rosenthal
**Date:** 2026-02-27

---

## Sanitized Puzzle (as presented to testers)

The following was stripped before presenting to testers:
- Line 3: Removed `T1` tier marker and `&#9733;` star
- Line 14: Removed `**References:** animal-phylogeny/, botany/, mycology/, entomology/` line
- Line 112: Changed answer line to `**Your answer:** _______________`
- All `<!-- comments -->` removed (none present in original)
- No "Answer:", letter count, or "Panel votes" lines present in original (clean)

The sanitized puzzle retains:
- The Taxonomist flavor text
- Full dichotomous key (Steps 1-5 with branching paths to NAUTILUS, MUSHROOM, ORCHID, MAPLE, BIRCH)
- Five specimen descriptions (A-E)
- Three-step worksheet: classify, diagonal extraction, read answer
- Hint line: "You may find the Natural World section helpful."

---

## Intended Solution

### Step 1 -- Classifications

| Specimen | Key Path | Common Name |
|---|---|---|
| A | 1a (animal) -> 2a (coiled shell, jet propulsion, open ocean) | NAUTILUS |
| B | 1b (not animal) -> 3b (cellulose, chlorophyll) -> 4b (eudicot, net veins) -> 5b (papery bark, catkins, winged nutlet) | BIRCH |
| C | 1b (not animal) -> 3b (cellulose, chlorophyll) -> 4a (monocot, parallel veins, flower parts in threes) | ORCHID |
| D | 1b (not animal) -> 3a (chitin, no chlorophyll, osmotrophic, spores) | MUSHROOM |
| E | 1b (not animal) -> 3b (cellulose, chlorophyll) -> 4b (eudicot, net veins) -> 5a (palmate lobing, paired samara, opposite leaves) | MAPLE |

### Step 2 -- Diagonal Extraction

| Specimen | Name | Position | Letter |
|---|---|---|---|
| A (1) | NAUTILUS | 1st | **N** |
| B (2) | BIRCH | 2nd | **I** |
| C (3) | ORCHID | 3rd | **C** |
| D (4) | MUSHROOM | 4th | **H** |
| E (5) | MAPLE | 5th | **E** |

### Step 3 -- Answer

**NICHE**

---

# Test: Aluminum -- Lucas Pope

## Solve Attempt

Pope reads the Taxonomist flavor text: "The Taxonomist named six million species and found a place for each one. Five unnamed specimens are on your desk. Classify them."

He immediately notes the structural layout: a dichotomous key with five terminal nodes, five specimens, and a diagonal extraction. "This is a filling-the-matrix puzzle. Five specimens, five names, one-to-one matching. The key is the mechanism -- I need to decide which specimen maps to which name. Let me see how the key constrains this."

### Reading the Key

Pope reads the key first, mapping its structure before touching the specimens:

```
Step 1: Animal vs. Not-animal
  Animal -> Step 2: Shell/jet propulsion? -> NAUTILUS (else: not in set)
  Not-animal -> Step 3: Chitin vs. Cellulose
    Chitin -> MUSHROOM
    Cellulose -> Step 4: Monocot vs. Eudicot
      Monocot -> ORCHID
      Eudicot -> Step 5: Palmate lobes/samaras vs. Papery bark/catkins
        Palmate -> MAPLE
        Papery bark -> BIRCH
```

"Five terminal nodes. Five specimens. Bijection. Every specimen maps to exactly one name. This is clean -- no ambiguity in the key structure itself. The only question is whether each specimen description contains enough information to traverse the key unambiguously."

He notes: "The key has a '[not in set]' dead end at 2b. That means if something is an animal but does not match the shell description, the key fails. This is intentional -- it constrains the solution space. Exactly one specimen is an animal, and it had better be a nautilus."

### Running the Specimens

**Specimen A:** "Cephalopod, phylum Mollusca, external shell divided into gas-filled chambers, jet propulsion, pelagic zone." Step 1a (animal -- it is explicitly called a cephalopod). Step 2a (coiled external shell of calcium carbonate, jet propulsion, open ocean). **NAUTILUS.** "The description is massively overdetermined -- siphuncle, pinhole eyes, ninety tentacles, living fossil. Any one of three details would suffice. The key only needs 'external shell + jet propulsion + open ocean.'"

**Specimen B:** "Deciduous angiosperm tree, papery bark peeling in horizontal strips, ovate to triangular leaves, doubly serrated margins, catkins, winged nutlet, ectomycorrhizal." Step 1b (sessile, cell walls). Step 3b (implicit -- it is an angiosperm tree, therefore cellulose and photosynthetic). Step 4b (eudicot -- though the clue does not use the word 'eudicot' directly, it says 'simple, ovate to triangular' which matches 5b, and the fact that it is not a monocot can be inferred from the bark description and serrated leaves). Step 5b (papery bark peeling in horizontal strips, catkins, winged nutlet). **BIRCH.**

Pope pauses here: "The specimen description does not explicitly say 'eudicot' or 'net veins.' The key at Step 4 distinguishes monocots from eudicots by vein pattern and flower parts. The description says 'catkins' for flowers -- that is neither 'multiples of three' nor 'multiples of four or five.' A solver who is strict about following the key as written might stall at Step 4 because the catkin morphology does not directly match either option's flower description." He flags this but proceeds: "The bark and leaf description at Step 5b are so specific to birch that a reasonable solver will land here. But the key path technically requires identifying the monocot/eudicot split first, and the specimen description relies on botanical inference rather than stating it outright."

**Specimen C:** "Monocot, parallel leaf venation, flower parts in threes, epiphyte, bilateral symmetry, dust-like seeds." Step 1b (sessile, cell walls -- it grows on tree branches). Step 3b (it is a flowering plant, so cellulose + chlorophyll). Step 4a (explicitly says 'monocot,' 'parallel leaf venation,' 'flower parts in threes'). **ORCHID.** "This is the cleanest match. The description practically quotes the key verbatim at Step 4a."

**Specimen D:** "Kingdom Fungi, chitin cell walls, no chlorophyll, osmotrophic (secretes enzymes externally, absorbs nutrients), fruiting body with cap/gills/stipe, basidiospores, saprotroph." Step 1b (sessile, cell walls). Step 3a (chitin cell walls, no chlorophyll, osmotrophic, spores from fruiting body). **MUSHROOM.** "Again massively overdetermined. The chitin + osmotrophic combination alone is diagnostic. The entire paragraph is a biology lecture."

**Specimen E:** "Eudicot, family Sapindaceae, palmately lobed with 3-5 pointed lobes, opposite pairs, palmate veins, paired samaras, sucrose-rich sap." Step 1b (sessile, cell walls). Step 3b (flowering plant, photosynthetic). Step 4b (explicitly says 'eudicot,' net veins implied by palmate venation). Step 5a (palmate lobing 3-5 lobes, paired samara, opposite leaf arrangement). **MAPLE.** "The samara description ('two winged seeds joined at the base, spinning like helicopter rotors') is a direct match to the key's 'paired samara.' The sap/sucrose detail is extra flavor -- a solver would recognize maple from the samaras alone."

### Extraction

Pope fills the diagonal extraction:

| Specimen | Name | Position | Letter |
|---|---|---|---|
| A (1) | NAUTILUS | 1st | N |
| B (2) | BIRCH | 2nd | I |
| C (3) | ORCHID | 3rd | C |
| D (4) | MUSHROOM | 4th | H |
| E (5) | MAPLE | 5th | E |

**N-I-C-H-E.**

"NICHE. The ecological niche -- each specimen's place in the natural world. The Taxonomist's job is literally to define where each organism fits. The puzzle asks you to classify five organisms into their taxonomic identities, and the answer is the word for the concept that classification serves. That is self-referential in exactly the right way."

### Deduction Analysis (Pope's Lens)

Pope now applies his Obra Dinn framework:

**Identification mechanism:** "This is a deduction puzzle, barely. The key provides a deterministic decision tree. Each specimen maps to exactly one terminal node. There are no branching ambiguities -- no specimen could plausibly match two different key paths. The deduction is: read description, match criteria, follow arrows. This is closer to a flowchart than to Obra Dinn's matrix."

**Lateral information:** "None. Each specimen is classified independently. Knowing Specimen A is NAUTILUS gives you zero information about Specimen B. There is no cross-referencing, no elimination logic needed (except trivially: once NAUTILUS is assigned to A, no other specimen can be NAUTILUS -- but the descriptions are so overdetermined that this elimination is never needed). In Obra Dinn terms, this is a puzzle where every crew member wears a name tag."

**Confirmation mechanism:** "The word NICHE confirms the grid. If a solver gets one classification wrong, the diagonal extraction produces garbage. This is adequate but blunt -- it is a single all-or-nothing check. Obra Dinn's Rule of Three is more granular."

**Tiered difficulty:** "There is a minor tier. Specimen C (ORCHID) and D (MUSHROOM) are the easiest -- the descriptions practically recite the key criteria verbatim. Specimen A (NAUTILUS) is medium -- the 'animal' classification is stated explicitly, and the shell/jet propulsion match is direct. Specimens B (BIRCH) and E (MAPLE) are the hardest -- they both go through four key steps, and the Step 4 monocot/eudicot split requires botanical knowledge that is not always stated explicitly in the descriptions. But even the 'hard' specimens are straightforward for anyone willing to read carefully."

**Multiple solution paths:** "No. There is exactly one path through the key for each specimen. No alternative evidence chains. No process of elimination needed. This is a single-path puzzle."

## Answer

**NICHE**

## Scores

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Clarity | 5 | The key is impeccably formatted. Binary choices at every node. Clear arrows ("go to 2," "go to 3"). Terminal nodes named in capitals. Specimen descriptions are detailed and unambiguous. The worksheet structure (classify -> extract -> read) is linear and intuitive. A solver with zero biology background can follow the key if they can match descriptions to criteria. |
| Solvability | 5 | Every specimen maps unambiguously to exactly one key terminal. No specimen could plausibly match two paths. The descriptions are overdetermined -- each contains 3-5 confirmatory details when the key only needs 1-2. A motivated solver will complete this even without encyclopedia access, since the key itself is self-contained. |
| Elegance | 3 | The mechanism is clean: one key, five specimens, one word. The answer NICHE is thematically perfect. But the solving experience is flat -- five independent traversals of the same decision tree with no interaction between specimens. No specimen's classification informs another. No constraint propagation. No moment where the solver says "wait, if D is MUSHROOM, then B must be..." because the identifications are never in doubt. The puzzle is five parallel tracks, not one interconnected system. Compare to a key where some specimens are ambiguous and require elimination logic -- that would add genuine deductive structure. |
| Reading Reward | 4 | The specimen descriptions are genuinely educational. The nautilus paragraph teaches siphuncle buoyancy control, the mushroom paragraph explains osmotrophic nutrition and the carbon cycle, the birch paragraph introduces ectomycorrhizal symbiosis. A solver who reads carefully learns real biology. The key itself teaches the fundamental method of biological classification -- dichotomous keying is how real field biologists work. One notch off because the key's five terminal nodes are all common organisms; a solver already knows what a nautilus and a maple are. The puzzle confirms knowledge rather than generating new understanding. |
| Fun | 3 | The first specimen is satisfying -- you learn the key, trace the path, and land on NAUTILUS. By the third specimen, the mechanism is familiar and the novelty has faded. The diagonal extraction and NICHE reveal provide a payoff. But the middle three specimens are rote: read, match, write. The puzzle lacks a difficulty arc -- there is no specimen that makes you stop and think. Everything resolves on first reading. |
| Confirmation | 4 | NICHE is a real word with strong thematic resonance. If any classification is wrong, the extraction breaks. The five-letter word provides adequate confirmation. The blank lengths in the worksheet (8, 5, 6, 8, 5) match the expected answers, providing per-specimen confirmation before the final extraction. |
| **Total** | **24/30** | |

## Principle Checks

| Principle | Pass/Fail | Notes |
|---|---|---|
| The Riven Standard | PASS | The puzzle IS what a taxonomist does -- classifying organisms through a dichotomous key. This is the actual method used in field biology. The puzzle is diegetic to the Natural World section. |
| Solving = Proving Understanding | PARTIAL | The solver demonstrates they can read a dichotomous key and match descriptions to criteria. But the descriptions are so overdetermined that understanding is barely tested -- matching is closer to pattern recognition than to comprehension. |
| The Dinner Party Test | FAIL | "I classified five organisms using a dichotomous key and the diagonal spelled NICHE" -- pleasant but not remarkable. This would not stop a dinner conversation. |
| The Book Test | PASS | Pencil and book. No tools needed. The key is self-contained. |
| Blame the Player | PASS | Every path through the key is fair and well-clued. If a solver misclassifies, they will blame their own reading, not the puzzle's design. |
| The 80% Rule | N/A | Individual puzzle, not a meta. |
| Reading Reward >= 4 | PASS | Score: 4. The descriptions teach real biology. The key teaches the actual method of taxonomic classification. |
| No Over-Scaffolding | PARTIAL | The key is complete and explicit. The worksheet provides blanks for every step. The solver never has to decide what to do -- only to execute. The key does the thinking; the solver does the matching. |
| Surprise the Answer | PASS | NICHE is not guessable from "classify five organisms." A solver might expect TAXON, GENUS, KINGDOM, or SPECIES. NICHE is thematically right but not predictable. |
| One Aha, Not Three | PASS | One aha: the diagonal extraction spells a word. The classification step is mechanical; the aha is seeing NICHE emerge. Clean single mechanism. |
| The Periodic Table Is Not Decoration | PASS | Aluminum = element 13 in the Natural World section. The Taxonomist card is the mechanism. The element framing connects to the section. |
| No Deliberate Errors | PASS | All biological facts in the descriptions are accurate. The dichotomous key's criteria are taxonomically correct. Chitin vs. cellulose cell walls, monocot vs. eudicot distinctions, samara morphology -- all verified. |
| Interlock, Not Independence | FAIL | Five independent classifications. No cross-referencing. No elimination logic needed. Each specimen is solved in isolation. |
| Snyder's Computer Test | FAIL | A 10-line script with keyword matching could solve this. Read description, match "chitin" -> MUSHROOM, match "cephalopod" -> NAUTILUS, etc. No judgment, ambiguity, or insight required. |

## Issues

1. **No interlock between specimens.** All five classifications are independent. The solver never needs to use elimination logic ("if A is NAUTILUS, then B cannot be...") because each description is so overdetermined that the identity is never in doubt. This makes the puzzle five parallel lookups rather than one interconnected deduction.

2. **Descriptions are overdetermined relative to the key.** The key needs 1-2 criteria per node to distinguish organisms. The descriptions provide 5-10 confirmatory details each. This eliminates any ambiguity or difficulty in the matching step. A harder puzzle would provide sparser descriptions that require the solver to weigh evidence carefully.

3. **Step 4 monocot/eudicot split is implicit for Specimen B.** The birch description does not explicitly state "eudicot" or "net veins." The solver must infer eudicot status from the tree/bark/catkin description. This is the one moment where the key path requires botanical reasoning rather than direct keyword matching -- but it is a small moment in an otherwise frictionless puzzle.

4. **Flat difficulty curve.** All five specimens resolve on first reading. No specimen requires a second pass, encyclopedia consultation, or careful deliberation. The puzzle lacks a difficulty arc.

## Suggested Fixes

1. **Reduce description specificity.** Give sparser descriptions that force the solver to use the key's criteria more carefully. Example: describe Specimen B as "a temperate tree with peeling bark and wind-dispersed fruits" without mentioning catkins, serrated margins, or nutlets. The solver must consult the encyclopedia's botany section to determine whether it is a maple or a birch, using the key's criteria (palmate lobing vs. serrated margin; paired samara vs. winged nutlet) as the decision tool.

2. **Add ambiguity that requires elimination.** Include one specimen whose description matches two key paths superficially, requiring the solver to use the other specimens' classifications to disambiguate via elimination.

3. **Make the key incomplete.** Remove one distinguishing criterion from a key step, requiring the solver to look up the missing criterion in the encyclopedia. This transforms the key from a complete flowchart into a partial guide that the solver must supplement with research.

---

# Test: Aluminum -- Rand Miller

## Solve Attempt

Miller reads the Taxonomist's invitation and the puzzle type description. "Five specimens sit on your desk. Each is described only by what you can observe -- habitat, body plan, nutrition, reproduction. No names. No labels."

He pauses on this framing. "This is a naturalist's desk. I am looking at five organisms and trying to identify them using a reference tool. The tool is a dichotomous key -- a branching decision tree that field biologists actually use. This is not an arbitrary puzzle mechanism; this is the real method. The puzzle IS the discipline."

### Entering the World

Miller reads each specimen description before touching the key, treating them as five rooms in a space to explore:

"Specimen A is a deep-ocean creature with a chambered shell and jet propulsion. Specimen B is a boreal tree with peeling bark and symbiotic fungi. Specimen C is a tropical epiphyte with dust-like seeds and a fungal germination partner. Specimen D is a fungal fruiting body -- cap, gills, stipe -- that decomposes dead wood. Specimen E is a temperate tree with lobed leaves and paired helicopter seeds."

"These are vivid. Each description paints a complete picture of an organism -- where it lives, how it feeds, how it reproduces. The mycorrhizal detail in B, the carbon-cycle role of D, the seed strategy in C -- these are real ecological stories, not just identification tags. I am learning about these organisms while I classify them."

### Running the Key

Miller works through the key methodically:

**Specimen A:** "Animal (it is a cephalopod). External shell, jet propulsion, open ocean. The key says NAUTILUS. Done in two steps."

**Specimen D:** Miller jumps to D next, not sequentially: "This one called to me. 'Not a plant and not an animal. Kingdom Fungi.' The key's Step 3a is about chitin cell walls, no chlorophyll, osmotrophic nutrition, spores from fruiting body. Every word matches. MUSHROOM."

He notes: "The connection between B and D is beautiful. Specimen B mentions 'ectomycorrhizal: its roots form a symbiotic sheath with fungal hyphae.' Specimen D is the fungal partner's reproductive structure. These two specimens are ecologically linked -- the birch tree and the mushroom growing at its base. The puzzle doesn't force you to notice this, but it rewards you if you do."

**Specimen C:** "Monocot, parallel veins, flower parts in threes. Step 4a: ORCHID. The labellum and dust-like seed details are fascinating but unnecessary for classification -- the monocot markers are enough."

**Specimen E:** "Eudicot, palmately lobed 3-5 lobes, paired samaras, opposite leaves. Step 5a: MAPLE. The sucrose/sap detail is the giveaway that would let anyone solve this without the key -- but the key's criteria (palmate lobing, paired samara, opposite arrangement) are the proper diagnostic path."

**Specimen B:** "The last one. Eudicot by elimination (or by inference from tree/bark morphology). Step 5b: papery bark, serrated margins, catkins, winged nutlet. BIRCH. The ectomycorrhizal detail does not appear in the key -- it is extra world-building."

### Extraction and Answer

Miller fills the diagonal:

N (Nautilus, 1st) - I (Birch, 2nd) - C (Orchid, 3rd) - H (Mushroom, 4th) - E (Maple, 5th).

**NICHE.**

"Niche. The ecological niche -- an organism's role in its environment. The nautilus occupies the deep-pelagic scavenger niche. The birch is a pioneer-species niche. The orchid is an epiphytic niche. The mushroom is a decomposer niche. The maple is a canopy-tree niche. Each specimen's description emphasizes its ecological role, not just its morphology. The puzzle is about niche classification, and the answer IS niche."

He sits with the connection. "This is the Riven test: does the world exist for a reason beyond the puzzle? Yes. These five organisms are real. Their descriptions are accurate. The dichotomous key is a real biological tool. The ecological roles described are genuine. You could remove the puzzle layer (the extraction) and the content would still be educational. The puzzle adds a reason to engage deeply with the content, but the content does not exist to serve the puzzle."

### World-Integration Assessment

"Where does this puzzle sit on my three-legged stool? The environment (the naturalist's desk, the five specimens) is strong. The story (the Taxonomist's role, the ecological connections between specimens) is present but light. The puzzle (classify and extract) is functional but not deep."

"The weakness: the key makes everything too easy. In Myst, I explore a space and gradually understand how it works. Here, the key is handed to me complete. There is no moment of discovery -- no 'I see the pattern.' The key is a manual, and I follow the manual. The satisfaction comes from the content (learning about organisms) and the payoff (NICHE), not from the solving process."

## Answer

**NICHE**

## Scores

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Clarity | 5 | The key is perfectly structured. Binary choices, clear paths, unambiguous terminals. The specimen descriptions are richly detailed. The worksheet is clean. No parsing ambiguity anywhere. |
| Solvability | 5 | Every specimen maps to exactly one terminal node. No ambiguity. No encyclopedia required -- the key is self-contained and the descriptions match the criteria directly. |
| Elegance | 3 | The mechanism is clean and the answer is thematically perfect. The ecological connections between specimens (birch + mushroom mycorrhiza, orchid + mushroom fungal germination partner) add depth. But the solving process is a flowchart traversal -- follow the arrows, write the name. The puzzle does not ask the solver to construct understanding; it asks them to follow instructions. In Riven, the world IS the puzzle because you must figure out how the world works. Here, the key tells you how the world works and asks you to apply it. |
| Reading Reward | 5 | This is where the puzzle excels. The specimen descriptions are miniature natural-history essays. The nautilus siphuncle, the mycorrhizal symbiosis, the orchid seed strategy, the mushroom's role in the carbon cycle, the maple sap freeze-thaw mechanism -- these are real ecological concepts presented with care and detail. A solver who reads these descriptions will remember them. The key itself teaches the dichotomous method that real biologists use. The puzzle does what the Taxonomist does: it makes you look closely at organisms and understand what makes each one distinct. |
| Fun | 3 | The first classification (learning the key) is engaging. The ecological connections (birch-mushroom, orchid-fungus) reward attentive reading. The NICHE reveal is satisfying. But the middle of the puzzle is rote: read description, match criteria, write name. There is no moment where the solver is stuck, no moment of genuine discovery, no "I figured it out" feeling. The puzzle is satisfying but not thrilling. |
| Confirmation | 4 | NICHE is a strong thematic answer. The five-letter word confirms the grid. Blank lengths in the worksheet provide per-specimen confirmation. If any classification is wrong, the word breaks. Adequate confirmation. |
| **Total** | **25/30** | |

## Principle Checks

| Principle | Pass/Fail | Notes |
|---|---|---|
| The Riven Standard | PASS | The puzzle IS biological classification. Dichotomous keying is the real method. The organisms are real. The ecological relationships are accurate. A field biologist would recognize their own work in this puzzle. |
| Solving = Proving Understanding | PARTIAL | The solver proves they can follow a dichotomous key. But the descriptions are so specific that mere keyword matching suffices -- the solver does not need to genuinely understand the biological distinctions, just to find the matching words. |
| The Dinner Party Test | FAIL | The mechanism is too simple to generate a remarkable story. "I classified five organisms" does not compete with "I drew the answer in the sky" (Oxygen) or "the answer was written in DNA" (Carbon). |
| The Book Test | PASS | Pencil and book only. The key is self-contained. |
| Blame the Player | PASS | Fair throughout. Every path is well-clued. A wrong answer is the solver's misreading, not the puzzle's deception. |
| The 80% Rule | N/A | Individual puzzle. |
| Reading Reward >= 4 | PASS | Score: 5. The descriptions are outstanding natural-history writing. |
| No Over-Scaffolding | PARTIAL | The key is a complete manual. The worksheet provides structure for every step. The solver's only task is to match and follow. The scaffolding does most of the thinking. A version without the key -- where the solver must build the classification from encyclopedia research -- would be a harder, deeper puzzle. |
| Surprise the Answer | PASS | NICHE is not the obvious guess for a classification puzzle. TAXON, GENUS, PHYLUM would be predictable. NICHE shifts the frame from taxonomy to ecology. |
| One Aha, Not Three | PASS | One aha: NICHE emerges from the diagonal. Clean. |
| The Periodic Table Is Not Decoration | PASS | Element 13, Natural World section, The Taxonomist card. Structural alignment. |
| No Deliberate Errors | PASS | All biological facts verified. Chitin/cellulose distinction, monocot/eudicot criteria, samara morphology, mycorrhizal relationships -- all accurate. |
| Interlock, Not Independence | FAIL | Five independent classifications. No cross-referencing needed. The ecological connections (birch-mushroom) are thematic, not mechanical. |
| Snyder's Computer Test | FAIL | Keyword matching solves this trivially. "Chitin" -> MUSHROOM, "cephalopod" -> NAUTILUS, "monocot" -> ORCHID, "samara" -> MAPLE, "catkins" -> BIRCH. |

## Issues

1. **The key removes all discovery.** The dichotomous key is handed to the solver complete. In Riven, the player must DISCOVER how the world's systems work. Here, the system is explained upfront. The puzzle asks the solver to apply a given tool, not to figure out the tool. The world-as-puzzle principle requires that understanding must be earned, not given.

2. **Ecological connections are decorative, not structural.** The birch-mushroom mycorrhizal link and the orchid-fungus germination partnership are beautiful thematic connections. But they do not affect the solving process. A solver who notices them gains appreciation but not advantage. In a stronger design, these connections would be load-bearing -- e.g., "Specimen D's fruiting body grows at the base of one of the other specimens. Which one?" forces the solver to use the ecological context.

3. **No exploration of the encyclopedia required.** The key is entirely self-contained. The solver never needs to open the Natural World section. The "You may find the Natural World section helpful" hint is misleading -- it is not helpful because it is not needed. The puzzle is closed rather than open.

4. **The specimen descriptions are too specific.** Each description contains 5-10 identifying details when the key only needs 1-2. This overdetermination means the solver is never uncertain. In Myst, uncertainty drives exploration. Here, certainty arrives immediately.

## Suggested Fixes

1. **Make the key incomplete at one node.** Omit the monocot/eudicot distinction criteria from Step 4. The solver must consult the botany section of the encyclopedia to learn what distinguishes monocots from eudicots. This creates genuine exploration.

2. **Add an ecological interlock.** Include a sixth specimen that cannot be classified by the key alone -- it requires understanding the ecological relationship described in another specimen's description. Example: "This organism is the symbiotic partner described in Specimen B" forces the solver to connect the mycorrhizal detail to the fungal identity.

3. **Reduce description specificity for 2-3 specimens.** Give sparser descriptions that match multiple key paths superficially, requiring careful evaluation of the key's specific criteria (not just keyword matching) to disambiguate.

---

# Test: Aluminum -- Alex Rosenthal

## Solve Attempt

Rosenthal approaches from the TED-Ed perspective: could he explain this puzzle to a general audience in 5 minutes? Would a non-biologist enjoy it?

He reads the Taxonomist flavor text. "Six million species -- that is a staggering number. Five on your desk. I like the physical framing: specimens on a desk. You are a naturalist. This has the 'dropped into a world' feeling."

The dichotomous key is immediately accessible: "Binary choices. Yes or no. Follow the arrows. This is a choose-your-own-adventure for organisms. I can explain this mechanism to anyone in 30 seconds. That is a strength -- the format is universally intuitive."

### Solving with Encyclopedia Access

Rosenthal is not a biologist. He reads the key carefully.

**Specimen A:** "Lives in the ocean, cephalopod, external shell, jet propulsion, gas-filled chambers. The key says: 'animal -> coiled external shell, jet propulsion, open ocean -> NAUTILUS.' Direct match." He does not need the encyclopedia. **NAUTILUS.**

**Specimen B:** "Deciduous tree, papery bark, peeling in horizontal strips, catkins, winged nutlet." He traces: "Not an animal (it is a tree). Step 3: cell walls -- the description says 'angiosperm,' so it has cellulose and chlorophyll. Step 4: monocot or eudicot? The description says 'simple, ovate to triangular' leaves and 'doubly serrated margins.' The key's monocot option says 'parallel veins, flower parts in threes.' The key's eudicot option says 'net veins, flower parts in fours or fives.' The description mentions catkins -- I do not know if catkins come in threes or fives."

He pauses. "I am stuck at Step 4. The description does not say 'monocot' or 'eudicot.' It does not mention vein pattern. It does not say how many flower parts the catkins have. Do I need the encyclopedia?"

He opens `botany/05-FLOWERS-REPRODUCTION.md` and searches for "catkin." He finds that catkins are characteristic of many eudicot families (Betulaceae, Fagaceae, Salicaceae). "Trees with catkins are eudicots. That resolves Step 4." He proceeds to Step 5b: "papery bark peeling in horizontal strips, catkins, winged nutlet." **BIRCH.**

"That was the one moment where I needed external knowledge. Without the encyclopedia, a non-botanist would be stuck at Step 4 for Specimen B. Every other specimen either explicitly states its key criteria or can be inferred from the description alone."

**Specimen C:** "It is a monocot. Parallel leaf venation. Flower parts in threes. The key says ORCHID." He does not need the encyclopedia. **ORCHID.** "This specimen uses the exact words from the key. It is almost too easy -- the description says 'monocot' and the key says 'monocot.' There is no interpretive work."

**Specimen D:** "Kingdom Fungi. Chitin cell walls. No chlorophyll. Osmotrophic. Fruiting body with cap and gills. Spores." Step 3a is a perfect match. **MUSHROOM.** "This is beautiful science writing. The carbon-cycle sentence at the end -- 'Without organisms like this, dead wood would accumulate indefinitely and the carbon cycle would stall' -- that is TED-Ed material. I learned something real while solving this clue."

**Specimen E:** "Family Sapindaceae. Palmately lobed with 3-5 pointed lobes. Opposite pairs. Paired samaras." Step 5a: exact match. **MAPLE.** "The samara description is delightful -- 'spinning like helicopter rotors as they fall.' I have seen this. Everyone has seen this. The puzzle connects scientific terminology to lived experience."

### Extraction

N-I-C-H-E.

"NICHE! The ecological niche. Each of these organisms occupies a different niche -- deep ocean, boreal forest, tropical canopy, forest floor, temperate canopy. The puzzle is about finding each organism's niche, and the answer is the concept of niche itself. That is a clean, satisfying reveal."

### The TED-Ed Assessment

"Could I make a 5-minute video about this? Yes, absolutely. The dichotomous key is a visually demonstrable mechanism -- binary choices, branching paths, five organisms sorted into five categories. The specimen descriptions are vivid (nautilus jet propulsion, mushroom carbon cycle, maple helicopter seeds). The reveal of NICHE ties it together."

"The challenge: the solving process is too easy to generate tension in a video. The best TED-Ed riddles have a moment where the audience thinks 'how could you possibly figure that out?' and then the solution clicks. Here, the solver follows a flowchart. There is no tension, no 'impossible' moment, no clever insight. The mechanism is transparent from the start."

"But the wonder is in the content, not the mechanism. The nautilus as a living fossil. The mycorrhizal connection between the birch and the mushroom. The orchid's partnership with fungi for germination. These are genuinely wonderful facts. The puzzle is a delivery vehicle for wonder about the natural world. That works."

### Accessibility Evaluation

"Who could solve this? Almost anyone. The key is self-contained. The binary choices are intuitive. Four of five specimens can be classified without external knowledge. Only Specimen B requires knowing that catkins indicate a eudicot -- and even there, the Step 5b description is so specific to birch that most solvers would land on the right answer through pattern matching rather than botanical reasoning."

"Who would ENJOY this? Nature enthusiasts, science-curious adults, students. The descriptions reward curiosity. The NICHE reveal creates a 'huh, that is clever' moment. It is not a 'wait, REALLY?' moment -- it is gentler than that. More of a nod than an exclamation."

## Answer

**NICHE**

## Scores

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Clarity | 5 | The key is universally intuitive -- binary choices, follow arrows, arrive at names. The specimen descriptions are vivid and detailed. The worksheet is clean. A non-biologist can follow this with no external references (except possibly for the monocot/eudicot distinction at Step 4). |
| Solvability | 5 | Five for five. Every specimen maps unambiguously. Four of five are solvable without encyclopedia access. One (Specimen B, the monocot/eudicot split) benefits from the encyclopedia but can be resolved by process of elimination (the only remaining eudicot paths are MAPLE and BIRCH; the description matches BIRCH at Step 5b). |
| Elegance | 3 | The mechanism is clean: one key, five specimens, one word. The answer NICHE ties the solving act (classifying organisms into their places) to the ecological concept (each organism's place in nature). But the mechanism is a flowchart -- there is no puzzle logic beyond following instructions. The elegance is in the framing, not in the solving. |
| Reading Reward | 4 | The specimen descriptions are excellent natural-history writing. The nautilus siphuncle, the birch mycorrhiza, the orchid seed strategy, the mushroom carbon cycle, the maple sap mechanism -- each teaches something real and memorable. The key itself teaches the dichotomous method. One notch off because four of five specimens can be classified without reading the encyclopedia -- the puzzle is mostly self-contained, so the "reward" for reading the encyclopedia is confirmation rather than discovery. |
| Fun | 3 | The mechanism is immediately clear and stays easy throughout. There is no point where a solver is stuck, puzzled, or surprised during the solving process. The fun is in the reading (specimen descriptions are delightful) and the payoff (NICHE is satisfying). The solving itself is not fun -- it is following directions. Compare to the TED-Ed riddles where the fun is in the "impossible" moment that suddenly resolves -- this puzzle has no such moment. |
| Confirmation | 5 | NICHE is a common English word. It is thematically perfect. The five-letter diagonal extraction is clean. Per-specimen confirmation via blank lengths. If any classification is wrong, the word breaks -- and a solver would immediately notice because NICHE is familiar. This is strong confirmation. |
| **Total** | **25/30** | |

## Principle Checks

| Principle | Pass/Fail | Notes |
|---|---|---|
| The Riven Standard | PASS | The puzzle IS biological classification. Real method, real organisms, real ecology. A biologist would recognize this as their own work. |
| Solving = Proving Understanding | PARTIAL | The solver proves they can follow a dichotomous key. But following a given key and building understanding of biological classification are different things. The key does the intellectual work; the solver does the matching. |
| The Dinner Party Test | FAIL | No remarkable story emerges. The mechanism is too transparent and the solving too smooth to generate a "you won't believe what I just did" moment. |
| The Book Test | PASS | Book and pencil only. Self-contained. |
| Blame the Player | PASS | All clues are fair. A misclassification would be the solver's error. |
| The 80% Rule | N/A | Individual puzzle. |
| Reading Reward >= 4 | PASS | Score: 4. The descriptions are excellent science writing. |
| No Over-Scaffolding | PARTIAL | The key is a complete manual. It provides every criterion needed to classify every specimen. A less scaffolded version would give fewer criteria and require the solver to supplement from the encyclopedia. |
| Surprise the Answer | PASS | NICHE is not the obvious guess for a taxonomy puzzle. |
| One Aha, Not Three | PASS | One aha: NICHE from the diagonal. Clean. |
| The Periodic Table Is Not Decoration | PASS | Element 13, Natural World section, Taxonomist card. Aligned. |
| No Deliberate Errors | PASS | All biology is accurate. |
| Interlock, Not Independence | FAIL | Five independent classifications. No cross-referencing. |
| Snyder's Computer Test | FAIL | Keyword matching trivially solves this. |

## Issues

1. **No tension or "impossible" moment.** The best puzzles create a moment where the solver thinks "I cannot do this" -- and then they can. This puzzle never creates that feeling. The key is complete. The descriptions are clear. The path is always obvious. There is no dramatic arc in the solving experience.

2. **Four of five specimens do not require the encyclopedia.** The hint says "You may find the Natural World section helpful," but four specimens can be classified from the key alone. Only Specimen B's monocot/eudicot ambiguity might send a solver to the encyclopedia. This means the puzzle is largely closed -- it does not drive exploration of the reference library.

3. **Specimen C is too easy.** The orchid description literally says "It is a monocot: parallel leaf venation, flower parts in threes" -- quoting the key's Step 4a almost verbatim. This removes all interpretive work. A better description would describe orchid features without using the key's terminology, forcing the solver to make the connection.

4. **Limited audience expansion potential.** The puzzle is pleasant and educational but does not create the "joyful, perplexing" quality that draws non-puzzlers into puzzle culture. It is more of a well-designed science activity than a puzzle that generates wonder.

## Suggested Fixes

1. **Use description language that does NOT mirror key language.** Describe features in observational terms ("the leaves have lines running from base to tip, all parallel to each other") rather than technical terms ("monocot, parallel venation"). This forces the solver to translate observations into the key's taxonomic criteria -- the actual cognitive work a field biologist does.

2. **Add one "trick" specimen.** Include an organism that appears to match one key path but actually matches another -- e.g., a coral (sessile animal, often mistaken for a plant) that tests the solver's understanding of Step 1's criteria. This creates the tension moment the puzzle currently lacks.

3. **Require encyclopedia access for at least 3 of 5 specimens.** Make the descriptions detailed enough to identify the organism but not detailed enough to traverse the key without research. The solver must use the encyclopedia to bridge from observation to classification -- which is what the hint promises.

---

# Synthesis

## Score Summary

| Dimension | Pope | Miller | Rosenthal | Average |
|---|---|---|---|---|
| Clarity | 5 | 5 | 5 | **5.0** |
| Solvability | 5 | 5 | 5 | **5.0** |
| Elegance | 3 | 3 | 3 | **3.0** |
| Reading Reward | 4 | 5 | 4 | **4.3** |
| Fun | 3 | 3 | 3 | **3.0** |
| Confirmation | 4 | 4 | 5 | **4.3** |
| **Total** | **24** | **25** | **25** | **24.7/30** |

## Principle Checks Summary

| Principle | Pope | Miller | Rosenthal | Consensus |
|---|---|---|---|---|
| The Riven Standard | PASS | PASS | PASS | **PASS** -- unanimous. The puzzle IS taxonomic classification. |
| Solving = Proving Understanding | PARTIAL | PARTIAL | PARTIAL | **PARTIAL** -- unanimous. Following a given key is execution, not understanding. |
| The Dinner Party Test | FAIL | FAIL | FAIL | **FAIL** -- unanimous. No remarkable story emerges. |
| The Book Test | PASS | PASS | PASS | **PASS** -- unanimous. Pencil and book only. |
| Blame the Player | PASS | PASS | PASS | **PASS** -- unanimous. All clues are fair. |
| Reading Reward >= 4 | PASS | PASS | PASS | **PASS** -- all score 4 or 5. |
| No Over-Scaffolding | PARTIAL | PARTIAL | PARTIAL | **PARTIAL** -- unanimous. The key does the thinking. |
| Surprise the Answer | PASS | PASS | PASS | **PASS** -- unanimous. NICHE is not predictable. |
| One Aha | PASS | PASS | PASS | **PASS** -- unanimous. Clean single mechanism. |
| Periodic Table Not Decoration | PASS | PASS | PASS | **PASS** -- unanimous. |
| No Deliberate Errors | PASS | PASS | PASS | **PASS** -- unanimous. All biology accurate. |
| Interlock, Not Independence | FAIL | FAIL | FAIL | **FAIL** -- unanimous. Five independent classifications. |
| Snyder's Computer Test | FAIL | FAIL | FAIL | **FAIL** -- unanimous. Keyword matching solves it. |

## Consensus Issues

1. **Five independent classifications with no interlock (all three).** This is the unanimous primary criticism. Every specimen is classified in isolation. No cross-referencing, no elimination logic, no constraint propagation. Pope: "This is closer to a flowchart than to Obra Dinn's matrix." Miller: "The ecological connections are thematic, not mechanical." Rosenthal: "No specimen's classification informs another." The puzzle is five parallel lookups, not one interconnected deduction.

2. **Descriptions are overdetermined relative to the key (all three).** The key needs 1-2 criteria per node. The descriptions provide 5-10 details each. The solver is never uncertain about any classification. Pope: "Every description is massively overdetermined." Miller: "Certainty arrives immediately." Rosenthal: "Four of five specimens do not require the encyclopedia." This eliminates the interpretive work that would make the puzzle genuinely challenging.

3. **No difficulty arc or tension (all three).** All five specimens resolve on first reading. There is no hard specimen, no moment of uncertainty, no "impossible" obstacle that suddenly resolves. Pope: "Everything resolves on first reading." Rosenthal: "No tension or 'impossible' moment." Miller: "There is no moment of genuine discovery."

4. **The key removes all discovery (Miller, Pope).** The dichotomous key is handed to the solver complete. The solver applies a given tool rather than figuring out how the tool works. Miller: "In Myst, I explore a space and gradually understand how it works. Here, the key is handed to me complete." Pope: "The deduction is: read description, match criteria, follow arrows."

5. **Snyder's Computer Test fails (all three).** A trivial keyword-matching script could solve this. "Chitin" -> MUSHROOM, "cephalopod" -> NAUTILUS, "monocot" -> ORCHID. No ambiguity, no judgment, no insight required.

## Consensus Strengths

1. **Thematic perfection of NICHE (all three).** The answer connects the solving act (classifying organisms into their ecological identities) to the ecological concept (each organism's place in nature). Pope: "The puzzle asks you to find each organism's place, and the answer IS the word for 'place.'" Miller: "Each specimen's description emphasizes its ecological role, not just its morphology." Rosenthal: "That is a clean, satisfying reveal."

2. **Outstanding specimen descriptions (all three).** The five descriptions are praised as genuine natural-history writing. The nautilus siphuncle, the birch mycorrhiza, the orchid seed strategy, the mushroom carbon cycle, the maple sap mechanism -- each teaches something real and memorable. Miller scores Reading Reward 5/5. All three testers note that the descriptions would be valuable educational content independent of the puzzle.

3. **The Riven Standard passes (all three).** The puzzle IS what a taxonomist does. The dichotomous key is the real method used in field biology. The organisms are real. The ecological relationships are accurate. A biologist would recognize their own work.

4. **Crystal clarity (all three, unanimous 5/5).** The key is impeccably formatted. Binary choices, clear arrows, unambiguous terminals. No parsing ambiguity. A non-biologist can follow the key without external help. The worksheet is clean and intuitive.

5. **NICHE as surprise answer (all three).** The answer is not guessable from the puzzle's topic. A solver would expect TAXON, GENUS, SPECIES, or KINGDOM from a classification puzzle. NICHE shifts the frame from taxonomy to ecology -- a genuine surprise that rewards the solving effort.

6. **The dichotomous key format is universally accessible (Rosenthal).** Binary choices are intuitive to all audiences. The mechanism can be explained in 30 seconds. This is one of the most accessible puzzle formats in the collection.

## Verdict

### PASS

**Score: 24.7/30 -- solid pass.**

The puzzle has a strong diegetic foundation (the dichotomous key IS real biology), excellent specimen descriptions (natural-history writing that teaches while encoding), and a thematically perfect answer (NICHE). The clarity and solvability are impeccable.

The weakness is structural: five independent classifications with no interlock, overdetermined descriptions that remove uncertainty, and a complete key that removes discovery. The puzzle is closer to a well-designed science activity than to a deep deduction puzzle. It fails the Dinner Party Test, the Interlock principle, and Snyder's Computer Test.

### Required Fixes (before publication)

1. **Reduce description specificity for at least 2 specimens.** Currently, every specimen contains enough keywords to be classified by pattern matching alone. Make 2-3 descriptions more observational and less technical, requiring the solver to interpret observations against the key's criteria. In particular, Specimen C should not say "monocot" directly -- let the solver make that determination from the described features.

2. **Create one moment of genuine difficulty.** Either make one specimen ambiguous between two key paths (requiring careful evaluation of criteria or encyclopedia consultation) or make the key incomplete at one node (requiring the solver to supplement it with research). The puzzle needs at least one moment where the solver stops, thinks, and makes a judgment call.

### Recommended Fixes (polish)

3. **Add one ecological interlock.** Include a detail in one specimen's description that can only be confirmed by reading another specimen's description. Example: "This organism's mycorrhizal partner produces the fruiting body described in another specimen on your desk." This creates a connection between B and D that is load-bearing, not decorative.

4. **Remove Specimen B's explicit species-family cues.** The description mentions "deciduous angiosperm tree" and many technical terms. A more observational description ("you observe thin bark peeling in horizontal strips, papery and white...") would make the key-traversal more engaging.

5. **Add a "working note" to the key.** After the key, add: "The key above covers five organisms. If a specimen does not match any path, consult the Natural World section of the encyclopedia for additional distinguishing criteria." This primes the solver to expect that the key alone may not be sufficient -- even if it currently is -- creating useful tension.
