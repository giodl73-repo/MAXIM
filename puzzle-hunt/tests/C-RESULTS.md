# Carbon — Puzzle Test Results

**Puzzle:** [6] Carbon (5 of Hearts — The Healer)
**Section:** Life Sciences
**Type:** Codon Decoding (DNA -> mRNA -> amino acids -> single-letter codes)
**Answer:** GENETIC (7 letters)

---

## Sanitized Puzzle

The following version was given to all three testers (metadata, answer hints, tier info, comments, and specific file references removed):

---

> The Healer reads the body at the molecular level. There is a message written in the language of life itself. The encyclopedia will teach you to read it. The message is here.

---

### The Puzzle

**Type:** Codon Decoding -- translate DNA -> mRNA -> amino acids -> single-letter codes

A short strand of DNA was recovered from a carbon-rich sample. The coding strand reads:

```
    G G T   G A A   A A C   G A G   A C C   A T C   T G C
```

Seven triplets. Seven codons. Seven amino acids. Seven letters.

To decode it, you will need two things from the encyclopedia. The molecular biology guide explains how DNA becomes mRNA -- the base-pairing rules that govern transcription. The biomolecules guide lists the twenty amino acids and their single-letter abbreviations.

Follow the central dogma. The answer is in the sequence.

---

### Worksheet

#### Step 1 -- Write the DNA coding strand

The coding strand is given above. Copy it into the top row.

```
DNA coding strand:

  ___   ___   ___   ___   ___   ___   ___
  G G T G A A A A C G A G A C C A T C T G C
```

#### Step 2 -- Transcribe to mRNA

The coding strand has the same sequence as the mRNA, except DNA uses T where RNA uses U. Replace every T with U.

```
Base-pairing reminder:

    DNA:   A   T   G   C
    RNA:   A   U   G   C

mRNA transcript:

  ___   ___   ___   ___   ___   ___   ___
  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
```

#### Step 3 -- Group into codons

Each codon is three consecutive mRNA bases, read 5' to 3'. Mark the seven codons.

```
Codon:   1st     2nd     3rd     4th     5th     6th     7th

       |_ _ _| |_ _ _| |_ _ _| |_ _ _| |_ _ _| |_ _ _| |_ _ _|
```

#### Step 4 -- Look up each codon

Use the standard genetic code table below to identify the amino acid encoded by each mRNA codon. The single-letter abbreviation for each amino acid is shown in parentheses. Cross-reference with the amino acid list in the biomolecules guide (Side-Chain Classification) for confirmation.

```
                        STANDARD GENETIC CODE
                        ---------------------
              2nd position
              U           C           A           G
       +----------- ----------- ----------- -----------+
       | UUU Phe (F) UCU Ser (S) UAU Tyr (Y) UGU Cys (C) |
   U   | UUC Phe (F) UCC Ser (S) UAC Tyr (Y) UGC Cys (C) |
       | UUA Leu (L) UCA Ser (S) UAA Stop     UGA Stop     |
       | UUG Leu (L) UCG Ser (S) UAG Stop     UGG Trp (W) |
       +----------- ----------- ----------- -----------+
       | CUU Leu (L) CCU Pro (P) CAU His (H) CGU Arg (R) |
   C   | CUC Leu (L) CCC Pro (P) CAC His (H) CGC Arg (R) |
       | CUA Leu (L) CCA Pro (P) CAA Gln (Q) CGA Arg (R) |
 1     | CUG Leu (L) CCG Pro (P) CAG Gln (Q) CGG Arg (R) |
 s     +----------- ----------- ----------- -----------+
 t     | AUU Ile (I) ACU Thr (T) AAU Asn (N) AGU Ser (S) |
       | AUC Ile (I) ACC Thr (T) AAC Asn (N) AGC Ser (S) |
 p  A  | AUA Ile (I) ACA Thr (T) AAA Lys (K) AGA Arg (R) |
 o     | AUG Met (M) ACG Thr (T) AAG Lys (K) AGG Arg (R) |
 s     +----------- ----------- ----------- -----------+
 i     | GUU Val (V) GCU Ala (A) GAU Asp (D) GGU Gly (G) |
 t  G  | GUC Val (V) GCC Ala (A) GAC Asp (D) GGC Gly (G) |
 i     | GUA Val (V) GCA Ala (A) GAA Glu (E) GGA Gly (G) |
 o     | GUG Val (V) GCG Ala (A) GAG Glu (E) GGG Gly (G) |
 n     +----------- ----------- ----------- -----------+

  Read each codon left to right: 1st position -> 2nd position -> 3rd position.
  Start codon: AUG (Met).  Stop codons: UAA, UAG, UGA.
```

Now fill in the table:

```
Codon        Amino acid name       Single-letter code
-----        ---------------       ------------------
1st: _ _ _   _______________       ___
2nd: _ _ _   _______________       ___
3rd: _ _ _   _______________       ___
4th: _ _ _   _______________       ___
5th: _ _ _   _______________       ___
6th: _ _ _   _______________       ___
7th: _ _ _   _______________       ___
```

#### Step 5 -- Read the message

Write the seven single-letter codes in order.

```
  ___ ___ ___ ___ ___ ___ ___
```

---

**Your answer:** _______________

*You may find the Life Sciences section helpful -- particularly the biomolecules and molecular biology guides.*

---

---

# Test: Carbon -- Wei-Hwa Huang

## Solve Attempt

Alright. The puzzle tells me up front what it is: codon decoding. DNA to mRNA to amino acids to single-letter codes. It even provides the genetic code table inline. Let me just execute.

**Step 1:** The DNA coding strand is given directly.
```
GGT  GAA  AAC  GAG  ACC  ATC  TGC
```

**Step 2:** Transcribe to mRNA. The rule is: T becomes U, everything else stays. Only two T's appear (in GGT, ATC, TGC). So:
```
GGU  GAA  AAC  GAG  ACC  AUC  UGC
```

**Step 3:** Group into codons -- they are already grouped:
```
1: GGU   2: GAA   3: AAC   4: GAG   5: ACC   6: AUC   7: UGC
```

**Step 4:** Look up each codon in the provided table:
- GGU -> Gly (G)
- GAA -> Glu (E)
- AAC -> Asn (N)
- GAG -> Glu (E)
- ACC -> Thr (T)
- AUC -> Ile (I)
- UGC -> Cys (C)

**Step 5:** Read the letters in order: G-E-N-E-T-I-C

The answer is **GENETIC**.

Total solve time: Under two minutes. There are zero decision points. Every step is deterministic table lookup.

## Answer
GENETIC

## Scores
| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| Clarity | 5 | Crystal clear. Every step is spelled out. No ambiguity at any point. |
| Solvability | 5 | 100% deterministic. The genetic code table is provided inline. No external knowledge needed beyond reading the table. |
| Elegance | 2 | The mechanism is a straightforward cipher substitution via a lookup table. There is no combinatorial depth. No deduction required -- just execution. |
| Reading Reward | 3 | You do learn how codon translation works, and the molecular biology / biomolecules guides are genuinely educational. But the puzzle itself does not force you to understand the material -- you can solve it purely mechanically. |
| Fun | 2 | This is a worksheet, not a puzzle. I filled in blanks. The "aha" is recognizing that the answer spells GENETIC, which is mildly amusing but not earned through effort. |
| Confirmation | 3 | The answer is a real English word, which provides some confirmation. The self-referential nature (genetics puzzle -> GENETIC) is a form of thematic confirmation. But there is no independent confirmation mechanism. |
| **Total** | **20/30** | |

## Issues

**Major: Brute-forceable.** A solver who knows that amino acids have single-letter codes could skip the entire transcription step, go directly to the codon table, and even guess the answer. The word GENETIC is one of the most obvious 7-letter words you could associate with a DNA puzzle. I would estimate that 30-40% of solvers could guess the answer without solving at all, just from reading the puzzle type line.

**Major: No deduction required.** Every step is a direct lookup. The "puzzle" is actually an exercise. There is no point where the solver must reason, eliminate possibilities, or make a non-obvious connection. The intended solution does not "stand out" because there is no competition -- there is only one mechanical path.

**Minor: Self-referential answer undermines itself.** The fact that a DNA-decoding puzzle spells GENETIC is cute but makes the puzzle easier to guess. It would be a stronger puzzle if the answer were a word that is surprising or that connects to a different domain.

## Suggested Fixes

1. **Remove the inline genetic code table.** Force solvers to find the codon table in the encyclopedia (06-BIOMOLECULES or 09-MOLECULAR-BIO). This at least forces engagement with the source material rather than providing everything on a silver platter.
2. **Remove or reduce the worksheet scaffolding.** Steps 1-3 are so explicit they eliminate all challenge. Keep the DNA strand and the flavor text. Let the solver figure out the process.
3. **Change the answer to a non-obvious word.** The answer should be a word that surprises the solver -- something that connects the Life Sciences theme to the broader puzzle hunt in an unexpected way. GENETIC is too on-the-nose.
4. **Add a twist.** For example: provide the template strand instead of the coding strand, so the solver must do the complementary base-pairing step (A<->T, G<->C) before transcription. This adds one real reasoning step. Or use a frameshift -- give the strand without spaces and let the solver figure out the reading frame.

---

# Test: Carbon -- Lucas Pope

## Solve Attempt

So this is a straight decode. DNA strand given, method explained, table provided, worksheet walks me through it. Let me follow the steps.

DNA: GGT GAA AAC GAG ACC ATC TGC

Replace T with U for mRNA: GGU GAA AAC GAG ACC AUC UGC

Look up each codon in the table they gave me:
- GGU -> G (Gly)
- GAA -> E (Glu)
- AAC -> N (Asn)
- GAG -> E (Glu)
- ACC -> T (Thr)
- AUC -> I (Ile)
- UGC -> C (Cys)

Spell it out: GENETIC.

Huh. The answer to the DNA puzzle is the word GENETIC. That is... extremely on the nose.

Let me think about this from a design perspective. In Obra Dinn, every identification requires cross-referencing multiple scenes. Here, there is exactly one path: read strand -> replace T with U -> look up table -> read letters. There is no lateral information. Nothing I learn here helps me solve anything else, and nothing from other puzzles feeds into this one. It is an isolated exercise.

The worksheet structure is the opposite of hands-off design. It holds your hand through every single step. In Obra Dinn, I give the player the tools (the pocket watch, the ledger) and trust them to figure out how to use them. Here, the puzzle gives you the tools and then uses them for you.

The confirmation mechanism: the answer is a real word. That is something. But GENETIC is so expected in this context that it does not feel like confirmation -- it feels like inevitability. There is no surprise. In Obra Dinn terms, this would be like if identifying the captain required only reading his name tag.

## Answer
GENETIC

## Scores
| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| Clarity | 5 | Perfectly clear. No ambiguity. The puzzle tells you exactly what to do at every step. |
| Solvability | 5 | Trivially solvable. Could not be more solvable. |
| Elegance | 2 | The codon-to-letter mapping is a real biological encoding, which has some inherent elegance. But the puzzle does not exploit that elegance -- it just uses it as a cipher. |
| Reading Reward | 3 | The central dogma (DNA -> mRNA -> protein) is genuinely interesting content. But the puzzle does not require understanding it -- just following mechanical steps. A solver learns the procedure but not the meaning. |
| Fun | 2 | No surprise. No lateral connections. No moment where something clicks. The "aha" (it spells GENETIC!) arrives with a shrug rather than a grin. |
| Confirmation | 2 | The answer is a real word, yes. But it is the most predictable possible word for this puzzle type. The confirmation is not earned -- it is obvious. Compare: if the answer were ECLIPSE or FURNACE, arriving at a real word after codon translation would feel magical. GENETIC just feels tautological. |
| **Total** | **19/30** | |

## Issues

**Major: No lateral information.** This puzzle is a closed system. It does not connect to other puzzles, other encyclopedia entries beyond the two referenced, or any broader theme. In a well-designed puzzle suite, solving one puzzle should change how you think about others.

**Major: Hands-on design, not hands-off.** The worksheet eliminates all trust in the solver. Every step is pre-structured. A stronger design would provide the DNA strand, point to the encyclopedia, and let the solver discover the process themselves.

**Major: Tautological answer.** GENETIC as the answer to a genetics puzzle is self-referential in a way that undermines rather than enhances. It is the equivalent of a murder mystery where the butler did it. No surprise, no delight.

**Minor: No confirmation beyond word recognition.** There is no Rule-of-Three equivalent. No way for the solver to independently verify their answer other than "it is a word."

## Suggested Fixes

1. **Strip the worksheet entirely.** Give the DNA strand and a pointer to the encyclopedia. Trust the solver to figure out that they need to transcribe to mRNA, then translate to amino acids, then read the single-letter codes. The discovery of the process IS the puzzle.
2. **Change the answer.** Pick a 7-letter word that is thematically relevant to the Life Sciences section but not obvious from the puzzle type. Something like HEALING (thematic to The Healer character) or a word that connects to the meta-puzzle.
3. **Add lateral connections.** The codon table has 64 entries mapping to 20 amino acids. Use this redundancy creatively -- perhaps certain codons chosen (not just any synonym) encode additional information visible only when cross-referenced with another puzzle.
4. **Build in a confirmation mechanism.** For example, the amino acid molecular weights could sum to a specific number, or the amino acid categories (polar/nonpolar/charged) could encode a secondary pattern that confirms correctness.

---

# Test: Carbon -- Thomas Snyder

## Solve Attempt

Let me work through this methodically.

The puzzle provides a DNA coding strand pre-grouped into triplets:
```
GGT  GAA  AAC  GAG  ACC  ATC  TGC
```

Step 2 tells me the coding strand matches mRNA with T replaced by U:
```
GGU  GAA  AAC  GAG  ACC  AUC  UGC
```

Step 4 gives me the full codon table. I look up each:

| Codon | Amino Acid | Letter |
|-------|-----------|--------|
| GGU | Glycine | G |
| GAA | Glutamic acid | E |
| AAC | Asparagine | N |
| GAG | Glutamic acid | E |
| ACC | Threonine | T |
| AUC | Isoleucine | I |
| UGC | Cysteine | C |

Reading the letters: **GENETIC**.

Solve time: approximately 90 seconds.

Now, as a puzzle constructor, let me evaluate the craft.

**Is this hand-crafted with an intentional solving path?** There is a path, but it is not "solving" -- it is "following instructions." A worksheet is not a puzzle. The constructor has choreographed the solve, yes, but the choreography is so prescriptive that no solver skill is being tested. I would describe this as a well-constructed tutorial, not a well-constructed puzzle.

**Is the thematic integration structural or cosmetic?** This is where it gets interesting. The mechanism -- codon translation -- is genuinely the central dogma of molecular biology. The theme (Life Sciences, The Healer) is structurally embedded in the solving mechanism. That is good. The problem is that the answer (GENETIC) is cosmetically thematic rather than structurally surprising. The theme drives the mechanism but not the payoff.

**Could a computer generate this puzzle?** Absolutely. Given any 7-letter word composed of amino acid single-letter codes (which is most words, since 20 of 26 letters are covered), a computer could generate the corresponding DNA strand in milliseconds. There is no hand-crafted element. The codon choices are not even constrained -- for several amino acids, there are 2, 4, or 6 synonymous codons, and the puzzle does not exploit this redundancy at all.

**Is there a specific "aha" moment?** The only candidate is the moment the letters spell GENETIC. But as noted, this is the most predictable answer possible and arrives without effort. A real "aha" requires the solver to have struggled, to have been uncertain, and then to suddenly see the pattern. Here there is no struggle and no uncertainty.

**Is every element serving a purpose?** The worksheet steps 1-3 serve no purpose for anyone who reads step 4. The table is provided, the codons are pre-grouped -- there is nothing to figure out. The worksheet is scaffolding for a learner, not structure for a solver.

## Answer
GENETIC

## Scores
| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| Clarity | 5 | Impeccable clarity. Cannot misinterpret any step. |
| Solvability | 5 | Mechanically trivial. Zero ambiguity, zero difficulty. |
| Elegance | 3 | The biological mechanism of codon translation is inherently elegant. Nature's own encoding scheme being used as a cipher has appeal. But the puzzle adds nothing on top of the natural elegance -- it just exposes it. |
| Reading Reward | 3 | A solver who has never seen the central dogma will learn something real. The encyclopedia references are good content. But the puzzle does not require deep reading -- surface-level table lookup suffices. |
| Fun | 2 | The mechanical nature eliminates fun. No decisions, no uncertainty, no surprise. Filling in a worksheet is educational, not entertaining. |
| Confirmation | 3 | GENETIC is a real word, providing basic confirmation. The self-referential quality (DNA puzzle -> GENETIC) provides thematic closure. But it is too predictable to be satisfying. |
| **Total** | **21/30** | |

## Issues

**Major: This is a tutorial, not a puzzle.** The worksheet structure eliminates all puzzle-solving. A puzzle requires the solver to make decisions under uncertainty. Here, every decision is made for them.

**Major: The answer is guessable.** GENETIC is the first word any solver would associate with DNA. The puzzle's answer should not be guessable from its premise alone.

**Minor: Codon redundancy is wasted.** Amino acids are encoded by 1-6 synonymous codons. The constructor chose specific codons but this choice carries no information. A craftsman would exploit this redundancy (e.g., the third position of each codon spells something, or specific codon families were chosen for a reason).

**Minor: No exploitation of the biological content.** The puzzle references two encyclopedia entries but only needs one fact from each (the T->U rule and the codon table). The rich content about protein folding, enzyme catalysis, side-chain chemistry -- none of it matters.

## Suggested Fixes

1. **Remove the worksheet and the inline codon table.** The puzzle should be: here is a DNA strand, here is a hint that the answer is in the language of life, go read the encyclopedia. The solver must discover the decoding process through reading.
2. **Exploit codon redundancy.** Use the wobble position (3rd base of each codon) to encode secondary information. For example, the wobble bases could spell a confirmation code, or the specific codon choices could correspond to particular organisms.
3. **Change the answer to something non-obvious.** The answer should reward the decoding effort with a surprise. A word that recontextualizes the puzzle, connects to the meta, or reveals something unexpected.
4. **Add a genuine puzzle layer.** For example: give the strand without grouping (let the solver find the reading frame), or provide two strands and make the solver determine which is sense vs. antisense, or embed the strand in a longer sequence with a start codon (AUG) that the solver must identify.

---

# Carbon -- Test Synthesis

## Scores Summary

| Tester | Clarity | Solvability | Elegance | Reading Reward | Fun | Confirmation | Total |
|--------|---------|-------------|----------|----------------|-----|--------------|-------|
| Huang | 5 | 5 | 2 | 3 | 2 | 3 | 20/30 |
| Pope | 5 | 5 | 2 | 3 | 2 | 2 | 19/30 |
| Snyder | 5 | 5 | 3 | 3 | 2 | 3 | 21/30 |
| **Average** | **5.0** | **5.0** | **2.3** | **3.0** | **2.0** | **2.7** | **20.0/30** |

## Average: 20/30

## Verdict: REVISE

The puzzle has a strong biological mechanism (codon translation is genuinely elegant as a cipher) and perfect clarity. But it is currently a guided worksheet rather than a puzzle. The answer GENETIC is guessable from context alone, and the extensive scaffolding removes all solver agency. The bones are good -- the revision should remove scaffolding, change the answer, and add at least one genuine reasoning step.

## Issues (Prioritized)

1. **[BLOCKING] Worksheet structure eliminates puzzle-solving.** All three testers independently described this as a tutorial or exercise, not a puzzle. The inline codon table + step-by-step worksheet means zero decisions under uncertainty. **Fix: Remove the worksheet. Remove the inline codon table. Provide the DNA strand and a thematic hint. Let the solver discover the process through the encyclopedia.**

2. **[BLOCKING] Answer is guessable from premise.** GENETIC is the most obvious 7-letter word associated with DNA/codons. Solvers can skip the entire puzzle. **Fix: Change the answer to a word that is thematically relevant but not predictable from the puzzle type. The surprise of the answer should reward the decoding effort.**

3. **[MAJOR] No genuine reasoning step.** Every step is a direct table lookup. There is no point where the solver must think, infer, or deduce. **Fix: Add one real puzzle layer -- e.g., give the template strand (requiring complement + transcribe), remove codon grouping (solver finds reading frame via start codon), or embed the target in a longer sequence.**

4. **[MINOR] Codon redundancy is unexploited.** Each amino acid has 1-6 synonymous codons. The specific codons chosen carry no secondary information. **Fix: Use the wobble position (3rd base) to encode a confirmation pattern or secondary clue.**

5. **[MINOR] No lateral connections to other puzzles.** The puzzle is a closed system with no implications for the broader puzzle hunt. **Fix: Ensure the answer feeds into the meta-puzzle in a way that connects to other Life Sciences puzzles.**
