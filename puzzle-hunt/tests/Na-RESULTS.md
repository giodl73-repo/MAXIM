# Puzzle Test: 11-Na-SODIUM

**Puzzle:** [11] Sodium -- Logic Grid (Social Sciences)
**Card:** 9 of Clubs -- The Strategist
**Testers:** Wei-Hwa Huang, Dan Katz, Lucas Pope
**Date:** 2026-02-27

---

## Sanitized Puzzle (as presented to testers)

> The Strategist knows that every system has rules, and every set of rules has a solution. Five nations. Five systems. No one will tell you which is which.

**Type:** Logic Grid -- five nations, five political-economic systems, deduce which is which

Five nations sit around a negotiating table. Each has a distinct form of government, a distinct legal tradition, a distinct economic model, and a distinct trade policy. No two nations share any attribute.

### The Nations

**Aldara** -- **Brevnia** -- **Caledor** -- **Durath** -- **Eskara**

### The Attributes

| Category | Five Possibilities |
|---|---|
| **Government** | Parliamentary, Presidential, Theocratic, Oligarchic, Monarchic |
| **Legal tradition** | Civil law, Common law, Religious law, Customary law, Mixed law |
| **Economic model** | Keynesian, Monetarist, Mercantilist, Supply-side, Laissez-faire |
| **Trade policy** | Interventionist, Free trade, Autarky, Protectionist, Export-led |

### The Clues

**1.** Caledor follows the economic school that prescribes counter-cyclical fiscal spending -- running deficits during recessions and surpluses during expansions -- to stabilize aggregate demand. The school born from the wreckage of the Great Depression.

**2.** The Keynesian nation's courts operate under common law: an adversarial system where judges build law case-by-case, binding future courts through stare decisis. The ratio decidendi of each ruling constrains every court that follows.

**3.** The nation with common law has a presidential system -- executive power vested in a single elected head of state, constitutionally separate from the legislature.

**4.** The presidential nation pursues an export-led growth strategy, channeling domestic production toward foreign markets to drive GDP.

**5.** Aldara's government meets in a parliament. Its legal system follows the continental pattern: comprehensive statutory codes are the primary source of law. Judicial decisions interpret the code but do not create binding precedent. Civil law -- not to be confused with civil litigation.

**6.** Brevnia's economy hoards gold and silver, treating international trade as a zero-sum contest for bullion. The mercantilist doctrine: exports good, imports bad, the treasury must always grow.

**7.** The mercantilist nation has sealed its borders entirely. No imports. No exports. Complete economic self-sufficiency -- autarky in its purest form.

**8.** One nation's legal system rests on customary law -- unwritten norms and traditions transmitted across generations, predating any legislative code or judicial reporter. That nation is governed by an oligarchy, and its economic policy follows the supply-side school: cut marginal tax rates, deregulate, and trust that production incentives will grow the economy from the top.

**9.** Eskara's monarch presides over a mixed legal system -- one that blends elements of multiple traditions, neither purely code-based nor purely precedent-driven. The crown espouses laissez-faire economics: the doctrine that markets self-regulate and the state governs best by governing least.

**10.** The supply-side nation rejects interventionism abroad. Instead it shields its domestic producers behind tariffs and import quotas -- the protectionist stance.

**11.** The monarchy maintains no tariffs and imposes no import quotas. Its borders are open to all foreign goods.

### Extraction

Nine letters are hidden in the solved grid. For each row below, find the cell indicated and extract the letter at the given position within that attribute's name.

| # | Nation | Category | Letter position | Letter |
|---|---|---|---|---|
| 1 | Aldara | Legal tradition | 2nd letter | |
| 2 | Caledor | Economic model | 4th letter | |
| 3 | Durath | Legal tradition | 1st letter | |
| 4 | Caledor | Government | 3rd letter | |
| 5 | Eskara | Government | 3rd letter | |
| 6 | Durath | Trade policy | 4th letter | |
| 7 | Brevnia | Economic model | 8th letter | |
| 8 | Aldara | Trade policy | 6th letter | |
| 9 | Eskara | Trade policy | 3rd letter | |

**Your answer:** _______________

---

## Intended Solution

| Nation | Government | Legal Tradition | Economic Model | Trade Policy |
|---|---|---|---|---|
| **Aldara** | Parliamentary | Civil law | Monetarist | Interventionist |
| **Brevnia** | Theocratic | Religious law | Mercantilist | Autarky |
| **Caledor** | Presidential | Common law | Keynesian | Export-led |
| **Durath** | Oligarchic | Customary law | Supply-side | Protectionist |
| **Eskara** | Monarchic | Mixed law | Laissez-faire | Free trade |

**Extraction:** I-N-C-E-N-T-I-V-E = **INCENTIVE**

---

# Test: Sodium -- Wei-Hwa Huang

## Solve Attempt

Wei-Hwa approaches this as a standard 5x4 logic grid. He immediately notes the structure: 5 entities, 4 categories of 5 options each, 11 clues, extraction step.

**Pass 1 -- Direct assignments from clues:**

Clue 1: "counter-cyclical fiscal spending... born from the wreckage of the Great Depression" -- that is Keynesian economics. **Caledor = Keynesian.** No ambiguity.

Clue 5: **Aldara = Parliamentary, Civil law.** Two direct assignments in one clue.

Clue 6: **Brevnia = Mercantilist.** "Hoards gold and silver... zero-sum contest for bullion."

Clue 9: **Eskara = Monarchic, Mixed law, Laissez-faire.** Three direct assignments. Very generous.

**Pass 2 -- Chain deductions (Clues 1-2-3-4):**

Clue 2: Keynesian nation has Common law. Since Caledor = Keynesian, **Caledor = Common law.**

Clue 3: Common law nation = Presidential. **Caledor = Presidential.**

Clue 4: Presidential nation = Export-led. **Caledor = Export-led.**

This is a clean four-clue deductive chain: Caledor = Keynesian -> Common law -> Presidential -> Export-led. Caledor is now fully determined.

**Pass 3 -- Clue 8 compound:**

Clue 8 links three attributes: Customary law = Oligarchic = Supply-side. Which nation?

Governments so far: Aldara = Parliamentary, Caledor = Presidential, Eskara = Monarchic. Remaining: Brevnia and Durath get Theocratic and Oligarchic.

Since Clue 8 says the Customary law nation is Oligarchic, and Brevnia is Mercantilist (not Supply-side as Clue 8 requires), the Clue 8 nation cannot be Brevnia. **Durath = Oligarchic, Customary law, Supply-side.**

Therefore **Brevnia = Theocratic.**

**Pass 4 -- Remaining assignments by elimination:**

Legal traditions: Aldara = Civil, Caledor = Common, Durath = Customary, Eskara = Mixed. Remaining: **Brevnia = Religious law.** (Thematically consistent with Theocratic government -- nice.)

Economic models: Caledor = Keynesian, Brevnia = Mercantilist, Durath = Supply-side, Eskara = Laissez-faire. Remaining: **Aldara = Monetarist.**

**Pass 5 -- Trade policies:**

Clue 7: Mercantilist nation = Autarky. **Brevnia = Autarky.**

Clue 10: Supply-side nation = Protectionist. **Durath = Protectionist.**

Clue 11: Monarchy (Eskara) = Free trade. **Eskara = Free trade.**

Caledor = Export-led (from Clue 4). Remaining: **Aldara = Interventionist.**

**Pass 6 -- Consistency check:**

Clue 10 says supply-side nation "rejects interventionism." Durath = Protectionist, not Interventionist. Consistent.

Clue 11 says monarchy has no tariffs. Eskara = Free trade. Consistent.

Everything checks out. Grid is complete.

**Pass 7 -- Extraction:**

1. Aldara, Legal tradition = "Civil law", 2nd letter = **I**
2. Caledor, Economic model = "Keynesian", 4th letter = **N**
3. Durath, Legal tradition = "Customary law", 1st letter = **C**
4. Caledor, Government = "Presidential", 3rd letter = **E**
5. Eskara, Government = "Monarchic", 3rd letter = **N**
6. Durath, Trade policy = "Protectionist", 4th letter = **T**
7. Brevnia, Economic model = "Mercantilist", 8th letter = **I**
8. Aldara, Trade policy = "Interventionist", 6th letter = **V**
9. Eskara, Trade policy = "Free trade", 3rd letter = **E**

Spells: **INCENTIVE**

Wei-Hwa pauses. "Is position 9 counting 'Free trade' as one string or two? If 'Free trade', the 3rd letter is 'e'. If 'Free' alone, still 'e'. If 'Freetrade' concatenated, still 'e'. Unambiguous regardless of interpretation." Good.

He also checks position 8: "Interventionist", 6th letter. I-N-T-E-R-V -- **V**. Correct.

## Answer

**INCENTIVE**

## Scores

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Clarity | 5 | Every clue is unambiguous. The descriptive text is educational flavor, not obfuscation. Attribute names are crisp. |
| Solvability | 5 | Uniquely solvable with a single deductive path. No bifurcation needed. No guessing. Clean chain logic. |
| Elegance | 4 | The 1-2-3-4 chain is elegant. Clue 8 bundling three attributes is efficient. Slight deduction: Clues 10-11 are mostly confirmation/cleanup rather than genuine deductive steps. The grid "solves itself" after about Clue 9. |
| Reading Reward | 4 | The political-science flavor text is genuinely educational (stare decisis, ratio decidendi, counter-cyclical spending). A solver learns real terminology. Slight deduction: some clues over-explain concepts already named in the attribute list. |
| Fun | 4 | Satisfying to complete. The chain deduction from Clues 1-4 is the highlight. The endgame is pure elimination rather than insight. |
| Confirmation | 4 | Extraction works cleanly. The answer "INCENTIVE" is thematically appropriate for a Social Sciences / Strategist puzzle. Minor concern: no intermediate confirmation that the grid is correct before extraction -- you just trust the logic. |
| **Total** | **26/30** | |

## Issues

1. **Overdetermined endgame.** After Clues 1-9 assign most attributes, Clues 10-11 are confirmatory rather than deductive. The puzzle is solvable from Clues 1-9 alone; 10-11 just verify. This isn't a flaw per se (confirmation is nice), but it means the last ~20% of solving is checking, not discovering.

2. **Extraction space ambiguity (minor).** "Free trade" -- does the solver count spaces? The extraction says "3rd letter" which is 'e' in "Free" regardless, so it works out. But "Civil law" at position 1 wants the "2nd letter" which is 'i' -- that also works whether you count "Civil law" or "Civil". No actual problem here, but stating the counting convention explicitly ("count within the first word" or "count across the full string including spaces") would be cleaner.

3. **No wrong-path traps.** A well-designed logic grid sometimes has a clue that *seems* to imply something but doesn't, forcing careful reading. Every clue here is straightforward. This makes it reliable but slightly predictable for experienced grid solvers.

## Suggested Fixes

1. Consider cutting Clue 11 and making solvers derive Eskara's trade policy purely by elimination (it's already forced after Clues 4, 7, 10 assign three trade policies). This raises the difficulty slightly and rewards solvers who track elimination carefully.

2. Add a parenthetical to the extraction table: "Count letters within the full attribute name, ignoring spaces." One sentence eliminates any ambiguity.

3. Optional: restructure one clue to be indirect (e.g., "The nation that trades freely does NOT follow the supply-side school") to add a deductive wrinkle. Currently every clue is a positive assertion, which makes the grid very linear.

---

# Test: Sodium -- Dan Katz

## Solve Attempt

Dan sees a standard logic grid and immediately assesses the constraint structure. Five entities, four categories, eleven clues. His first instinct: "Is this overconstrained? Underconstrained? Or just right?"

**Structural scan:**

- 5 nations x 4 categories = 20 cells to fill.
- Direct assignments: Clue 1 (Caledor=Keynesian), Clue 5 (Aldara=Parliamentary+Civil), Clue 6 (Brevnia=Mercantilist), Clue 9 (Eskara=Monarchic+Mixed+Laissez-faire). That's 8 cells directly assigned.
- Chain deductions from Clue 2-3-4 give Caledor 3 more attributes. Now 11 of 20 are pinned.
- Clue 8 pins 3 attributes to one unknown nation. That's 14 cells determined once you figure out which nation.
- Clues 7, 10, 11 give 3 more trade policies.

Dan notes: "This is a 20-cell grid with 11 clues that effectively give you ~18 cell values directly or via one-step deduction. The remaining 2 are forced by elimination. The puzzle is heavily overconstrained."

**Speed solve (Dan does this in about 3 minutes):**

Clue 1: Caledor = Keynesian.
Clue 2: -> Caledor = Common law.
Clue 3: -> Caledor = Presidential.
Clue 4: -> Caledor = Export-led.

Clue 5: Aldara = Parliamentary + Civil law.
Clue 6: Brevnia = Mercantilist.
Clue 7: -> Brevnia = Autarky.
Clue 9: Eskara = Monarchic + Mixed + Laissez-faire.
Clue 8: Some nation = Customary + Oligarchic + Supply-side. Not Aldara (Parliamentary), not Caledor (Presidential), not Eskara (Monarchic). Not Brevnia (Mercantilist, not Supply-side). -> Durath.
-> Brevnia = Theocratic (last government).
Clue 10: -> Durath = Protectionist.
Clue 11: -> Eskara = Free trade.
Elimination: Aldara = Monetarist + Interventionist. Brevnia = Religious law.

**Extraction:**

I-N-C-E-N-T-I-V-E = INCENTIVE.

Dan double-checks the letter counts with mild irritation: "Why is this always the part where puzzle authors make errors?" He counts carefully:

- "Mercantilist" position 8: M-E-R-C-A-N-T-I -- **I**. Correct.
- "Interventionist" position 6: I-N-T-E-R-V -- **V**. Correct.
- "Free trade" position 3: F-R-E -- **E**. Correct. (He notes: "Are we counting the space? F-R-E-E-[space]-T... No, 3rd letter is 'e' either way. Fine.")

## Answer

**INCENTIVE**

## Scores

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Clarity | 5 | Crystal clear. Every clue is a direct positive statement. No parsing ambiguity. The political-science descriptions are accurate and well-written. |
| Solvability | 5 | Uniquely solvable. No branching. A single deductive thread. |
| Elegance | 3 | The 1-2-3-4 chain is the best part -- a cascade where each clue unlocks the next. But 11 clues for a 5x4 grid is too many. The puzzle is heavily overconstrained. At least 2 clues (10, 11) could be cut without losing solvability. The solve feels like filling in a form, not cracking a puzzle. |
| Reading Reward | 4 | The descriptive text teaches real political science. "Ratio decidendi," "stare decisis," autarky as a concept -- these are genuinely interesting. If this is embedded in an encyclopedia-style reference library, the educational payoff is real. |
| Fun | 3 | For an experienced solver, this is about 3 minutes of work. The deductive chain is satisfying but short. The endgame is pure bookkeeping. I'd rate this "pleasant but not memorable." For a less experienced solver, it's probably more fun -- the chain deduction feels like genuine discovery. |
| Confirmation | 4 | Extraction is clean. "INCENTIVE" is a real word that fits the theme. The redundant clues (10, 11) serve as built-in confirmation that the grid is correct, which is actually a nice feature even if it reduces difficulty. |
| **Total** | **24/30** | |

## Issues

1. **Overconstrained / too easy for the format.** 11 clues for a 5x4 grid where 8 cells are directly stated is generous. A standard newspaper logic grid of this size typically has 7-8 clues and requires multi-step elimination. This puzzle could lose 2-3 clues and still be uniquely solvable.

2. **Linear solve path.** There's essentially one order to process the clues: 1->2->3->4, then 5, 6->7, 9, 8, then 10/11 confirm. No branching, no "aha" moment where two separate deduction chains converge. The puzzle lacks the moment where you go "Wait, THAT connects to THIS."

3. **The extraction is mechanical.** Count to the Nth letter of an attribute name. No insight required. The extraction doesn't reward understanding the content -- it's just indexing into strings. Compare this to an extraction where the answer emerges from the *structure* of the solution (e.g., reading diagonal cells, or using the first letter of each nation's unique attribute).

4. **Calibration question.** If this is meant for the learner profile (VP of Engineering, MIT background), this is warmup-level. If it's meant as a gentle introduction to the puzzle hunt, that's fine -- but it should be flagged as an easy puzzle.

## Suggested Fixes

1. **Cut Clues 10 and 11.** The grid is still uniquely solvable without them. Solvers must derive Eskara's free trade and Durath's protectionism by elimination, which adds one genuine deductive step.

2. **Make one clue indirect.** Instead of "The supply-side nation is protectionist," try something like: "Durath's trade policy is not the one shared by the nation whose courts hear cases under religious law." This forces cross-referencing between categories rather than direct assignment.

3. **Consider a more thematic extraction.** Instead of "Nth letter of attribute name," what if each solved cell maps to a concept from game theory (the listed reference), and the first letters of those concepts spell the answer? That would tie the extraction to the educational content.

---

# Test: Sodium -- Lucas Pope

## Solve Attempt

Lucas approaches this differently from the competitive puzzlers. He's thinking about the *experience* of solving, not the speed. He reads the flavor text first: "every system has rules, and every set of rules has a solution." He appreciates the framing -- this IS a system with rules.

He reads all 11 clues before touching the grid, building a mental model of the constraint graph.

**Mental model construction:**

Lucas notices the chain structure immediately: Clues 1-2-3-4 form a linked sequence. "That's like Obra Dinn -- one identification leads to the next. The 'lateral information' principle."

He maps the constraint graph:

```
Caledor ---[1]---> Keynesian ---[2]---> Common law ---[3]---> Presidential ---[4]---> Export-led
Aldara  ---[5]---> Parliamentary + Civil law
Brevnia ---[6]---> Mercantilist ---[7]---> Autarky
Eskara  ---[9]---> Monarchic + Mixed + Laissez-faire
???     ---[8]---> Customary + Oligarchic + Supply-side ---[10]---> Protectionist
Monarchy---[11]--> Free trade
```

"The chain from Clue 1 to Clue 4 is the spine of the puzzle. Everything else hangs off named nations. The only deductive step is figuring out that Clue 8's mystery nation must be Durath by elimination."

**Solving:**

He fills in the grid methodically, noting that Clue 8's nation must be Durath (process of elimination -- all other nations are either named in Clue 8's incompatible attributes or have conflicting assignments).

Brevnia's legal tradition (Religious law) is the last piece, forced by elimination. He notes: "Theocratic government + Religious law is a satisfying pair. That's lateral confirmation -- the thematic consistency tells me I'm right even before I check the elimination logic."

**Extraction:**

Lucas counts through each extraction step carefully. Gets INCENTIVE.

"The answer is thematically appropriate -- 'incentive' is a core concept in economics and game theory, and the puzzle is filed under Social Sciences. That's a confirmation signal."

## Answer

**INCENTIVE**

## Scores

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Clarity | 5 | The puzzle presents its rules cleanly. The attribute table is clear. Each clue is a self-contained positive statement. No parsing traps. |
| Solvability | 5 | Uniquely solvable. The deductive path is clean. No guessing required. |
| Elegance | 4 | The Clue 1-4 chain is the standout feature -- genuine lateral information where solving one cell cascades into three more. The thematic consistency (Theocratic + Religious law, Monarchic + Mixed + Laissez-faire) provides implicit confirmation signals. Slight deduction for the overconstrained endgame. |
| Reading Reward | 5 | This is where the puzzle shines from my perspective. The clue text isn't just encoding constraints -- it's teaching real political science. "Stare decisis," "ratio decidendi," "counter-cyclical fiscal spending," "autarky" -- a solver who reads carefully learns genuine concepts. The descriptions of each system are accurate and vivid. This is the "ledger" principle from Obra Dinn: the puzzle organizes real information without dumbing it down. |
| Fun | 4 | The chain deduction is satisfying. The thematic consistency is rewarding. The extraction is mechanical but functional. For a solo solver working through an encyclopedia-embedded puzzle, this delivers. |
| Confirmation | 3 | The puzzle's confirmation mechanism is limited. You solve the grid, then extract letters, and get a word. If the word is real, you're probably right. But there's no intermediate confirmation -- no "Rule of Three" equivalent. If you make one error in the grid, the extraction produces gibberish, and you have to re-check everything. A partial confirmation mechanism (e.g., "the first three letters spell a common English word") would help. |
| **Total** | **26/30** | |

## Issues

1. **No intermediate confirmation.** In Obra Dinn, the Rule of Three confirms clusters of correct identifications. Here, you solve the entire grid, then extract, and only at the very end do you know if you're right (by getting a real word). If you make one counting error in extraction, you get nonsense and have to recheck 9 letter-position lookups with no way to isolate the error.

2. **Single solution path.** The puzzle has essentially one deductive thread. In Obra Dinn, different players identify crew through different evidence chains. Here, everyone follows the same clue order. There's no "I solved Durath first by noticing the thematic link" alternative path -- you MUST process Clues 1-4 as a chain.

3. **Extraction doesn't leverage the content.** The extraction is "count to the Nth letter" -- a purely mechanical step. It would be more satisfying if the extraction required understanding the content (e.g., "the economic model that would respond to a supply shock by..." requiring the solver to identify which model, then extract from it).

## Suggested Fixes

1. **Add a checksum or partial confirmation.** For example: "The first four extracted letters form a word meaning 'a motivating factor.'" This lets solvers confirm halfway through extraction without giving away the full answer.

2. **Create alternative entry points.** Restructure so that a solver who starts with Clue 9 (Eskara) can build a parallel deduction chain that converges with the Caledor chain at Clue 8. Currently the Eskara clues are mostly independent assignments -- they don't create a cascade.

3. **The thematic consistency (Theocratic + Religious law) is an underused asset.** Consider making one clue implicit rather than explicit -- e.g., remove the explicit assignment of Brevnia's legal tradition and let solvers derive it from elimination AND confirm it via thematic coherence. This rewards domain knowledge.

---

# Synthesis

## Score Summary

| Dimension | Huang | Katz | Pope | Average |
|---|---|---|---|---|
| Clarity | 5 | 5 | 5 | **5.0** |
| Solvability | 5 | 5 | 5 | **5.0** |
| Elegance | 4 | 3 | 4 | **3.7** |
| Reading Reward | 4 | 4 | 5 | **4.3** |
| Fun | 4 | 3 | 4 | **3.7** |
| Confirmation | 4 | 4 | 3 | **3.7** |
| **Total** | **26** | **24** | **26** | **25.3/30** |

## Consensus Issues

1. **Overconstrained (all three).** 11 clues for a 5x4 grid is too many. Clues 10-11 are essentially redundant. All three testers solved this quickly with no branching or backtracking needed. Katz is most critical here ("filling in a form, not cracking a puzzle"), but all three note the endgame is mechanical.

2. **Linear solve path (Katz and Pope).** There's one deductive thread: the Clue 1-4 chain, then direct assignments, then elimination. No convergence point where separate reasoning paths meet. No "aha" moment.

3. **Mechanical extraction (all three).** Counting to the Nth letter is functional but not inspired. It doesn't leverage the educational content or reward domain knowledge. All three suggest thematic alternatives.

4. **No intermediate confirmation (Pope, echoed by Huang).** The solver has no way to verify partial progress. One error cascades silently through the extraction.

## Consensus Strengths

1. **Crystal clarity.** Every clue is unambiguous. The attribute names are standard political-science terminology. The grid structure is clean.

2. **Educational value.** The clue text teaches real concepts (stare decisis, counter-cyclical spending, autarky, ratio decidendi). This is the best dimension of the puzzle.

3. **Thematic coherence.** Brevnia (Theocratic + Religious law + Mercantilist + Autarky) and Eskara (Monarchic + Mixed + Laissez-faire + Free trade) form internally consistent "nation archetypes." The answer INCENTIVE fits the Social Sciences theme.

4. **The 1-2-3-4 chain.** All three testers highlight the cascade from Keynesian -> Common law -> Presidential -> Export-led as the puzzle's best feature.

## Verdict: PASS

**Score: 25.3/30** -- above the passing threshold.

The puzzle is clean, unambiguous, educational, and uniquely solvable. Its weakness is that it's too easy for experienced solvers -- overconstrained with a linear path. But for its context (an encyclopedia-embedded puzzle meant to reward careful reading of political-science content), this is appropriate. The clarity and educational value compensate for the low difficulty ceiling.

### Recommended Revisions (optional, not blocking)

1. **Cut Clues 10 and 11** to tighten the constraint set. The grid remains uniquely solvable, but solvers must work harder on the trade policy assignments.

2. **Add a space-counting note** to the extraction table: "Count letters within the full attribute name, ignoring spaces."

3. **Consider a partial confirmation hint** in the extraction (e.g., "The first four letters spell a common English word").

4. **If difficulty increase is desired:** replace one direct-assignment clue with an indirect/negative clue to force cross-referencing between attribute categories.
