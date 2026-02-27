# Problem Solving, Expertise, and Creativity — Cognitive Science

## The Big Picture

Problem solving is search through a space of possible states toward a goal. That's the Newell-Simon computational account. Gestalt psychology adds: solving also involves *restructuring* the representation of the problem itself. Expertise research shows that novices search; experts recognize.

```
+------------------------------------------------------------------+
|  PROBLEM SOLVING: THREE VIEWS                                    |
+------------------------------------------------------------------+
|                                                                  |
|  INFORMATION PROCESSING     GESTALT          EXPERTISE           |
|  (Newell & Simon)           (Duncker, Köhler) (Chase & Simon)    |
|                                                                  |
|  Problem = search through  Problem = find    Problem = pattern  |
|  state space                right             recognition        |
|                             representation    from LTM           |
|  Operators move from                                             |
|  one state to another      Insight =         Expert sees        |
|                             sudden           "this is a         |
|  Strategy =                 restructuring    class-B problem"   |
|  search algorithm           of problem                          |
|                                                                  |
|  Weakness: doesn't          Weakness: hard   Explains speed     |
|  explain insight            to operationalize but not transfer  |
+------------------------------------------------------------------+
```

---

## Problem Space (Newell & Simon 1972)

The **General Problem Solver** (GPS, 1957) established the framework. A problem consists of:

```
  INITIAL STATE         GOAL STATE
  +───────────+         +───────────+
  |  What you |         |  What you |
  |  start    |         |  want to  |
  |  with     |         |  reach    |
  +───────────+         +───────────+
       |                      |
       └──────────────────────┘
            Problem Space:
       All possible intermediate
       states reachable by operators

  OPERATORS: legal moves from state to state
  CONSTRAINTS: what operators are applicable
  PROBLEM = navigate from initial to goal state
```

**The CS connection**: These search strategies are the same ones from algorithms courses — BFS, DFS, hill-climbing, A*. GPS's means-ends analysis is heuristic search where the "difference function" (distance between current state and goal) serves as the heuristic h(n). The cognitive science question is *not* which search algorithm is optimal (you already know that) — it is: **how do humans construct and select the heuristic function?** In A*, h(n) is given by the designer. In human cognition, the heuristic is learned from experience (chunking), shaped by problem representation (Gestalt restructuring), and often wrong (functional fixedness = a bad heuristic that prunes the correct path). This is the gap between algorithmic problem-solving and psychological problem-solving.

**Search strategies**:

| Strategy | Description | Good when | Bad when |
|----------|-------------|-----------|---------|
| **Breadth-first** | Explore all states at depth d before d+1 | Short paths, complete exploration needed | Deep solutions, exponential space |
| **Depth-first** | Follow one path to completion before backtracking | Deep solutions, limited space | Gets lost in dead ends |
| **Hill climbing** | Always move toward states that seem closer to goal | Smooth landscapes | Local optima, plateaus |
| **Means-ends analysis** | Detect biggest difference between current/goal state; find operator that reduces it | Many AI / human problems | Requires measuring "difference" |
| **Working backward** | Start from goal, work toward initial state | Well-defined goals with few states |  |
| **Analogy** | Map structure from solved problem to new one | Novel problems with known analog | Finding the right analog |

**Means-ends analysis** is GPS's core heuristic and is observable in human problem solving:
1. Compare current state to goal state
2. Find the biggest difference
3. Select operator that reduces that difference
4. Apply; repeat

---

## Gestalt Insight — Restructuring

**Duncker's candle problem** (1945):
```
Materials on table: candle, box of thumbtacks, matches
Task: mount candle on wall so it can burn without dripping wax on floor

Failure mode: try to tack candle directly to wall, melt candle on wall, etc.
Solution: empty box of tacks, use box as shelf, tack to wall, place candle in box

Key barrier: FUNCTIONAL FIXEDNESS — the box is seen as a container for tacks,
not as a platform. Its function is fixed by its current role.
```

**Maier's two-string problem** (1931):
```
Two strings hanging from ceiling. Too far apart to grab simultaneously.
Materials: pliers on table.
Solution: tie pliers to one string as pendulum; swing it; catch while holding other.
```
When subjects were stuck, the experimenter would "accidentally" brush one string → hint → most solved it within 10 seconds — but couldn't report what the hint was. The insight felt spontaneous.

**What is insight?**
```
INCREMENTAL PROBLEM SOLVING      INSIGHT PROBLEM SOLVING
  ──────────────────────          ──────────────────────
  Progress is gradual             Impasse → sudden solution
  Subjects track progress         Subjects report no progress until:
  Proportional to time              "Aha!" moment
  Wrong answers spread             Wrong answers cluster, then
  evenly                            correct answer arrives suddenly
  E.g.: anagram of easy words     E.g.: compound remote associates
                                        (pine/crab/sauce → apple)
```

**Neural basis of insight** (Bowden & Jung-Beeman 2003):
- fMRI + EEG: ~300ms before subjects report "Aha!"
- Burst of **gamma activity (~40 Hz)** in **right anterior temporal lobe**
- This area integrates distantly related semantic information
- Left hemisphere: focused, local semantic relations
- Right hemisphere: loose, distant semantic associations (metaphor, jokes, "remote associates")
- Insight = right hemisphere contribution "breaks through" to consciousness

**Representational change theory** (Ohlsson 1992): Insight problems share a structure:
1. Initial representation is wrong / overly constrained
2. Impasse arises
3. Representational change occurs — constraints relaxed, new features attended to
4. Solution becomes apparent

---

## Functional Fixedness and Mental Set

**Functional fixedness**: Difficulty using an object in a novel way when its typical function is salient.
- A box seen as "container" → harder to see as "shelf"
- A wrench seen as "tool" → harder to see as "hammer"
- Reduced with priming: if object is presented without its contents (empty box) → solution faster

**Mental set / Einstellung effect** (Luchins 1942):
```
Water jug problems: Given jugs of size A, B, C — measure out target quantity.

Training problems: All solvable with formula B - A - 2C
Critical problem: Solvable with B - A - 2C BUT ALSO simpler A - C

Trained subjects use the complex formula even when the simple one is obvious.
Mental set = prior successful strategy persists, blocking simpler solutions.
```

**Insight in software**: This is exactly what happens in debugging. You've committed to a hypothesis about what's wrong ("it's a caching issue") and the Einstellung effect makes you miss the actual problem (a logic error in a completely different module). The fix: deliberately set aside the hypothesis and start fresh.

---

## Analogical Reasoning

**Gick & Holyoak (1980, 1983) — the radiation problem**:

```
Duncker's radiation problem:
  A patient has a tumor. A radiation beam can destroy it, but
  at sufficient intensity to destroy the tumor, it also destroys
  healthy tissue. Lower intensity is harmless but doesn't work.
  What do you do?

  Solution: converge multiple beams from different directions
  at low intensity — they sum at the tumor.

  Base rate: ~10% solve without hint.
```

Gick & Holyoak gave subjects an analogous story first (General attacking a fortress — separate armies converge from all directions). With one analogous story: ~30% solve. With two analogous stories: ~60%. The two stories allowed subjects to extract an **abstract schema** (converging forces at a center).

**Why analogy is hard**:
```
SURFACE SIMILARITY              STRUCTURAL SIMILARITY
  Same objects, domain            Same relations, causal structure
  (two military stories)          (convergence solves strength problem)

  Easy to notice                  Required for transfer
  Often misleading                Often invisible
  "This is like that"             "This has the same structure as that"
```

Children solve problems by surface similarity; adults should (but often don't) transfer by structural similarity.

---

## Expertise and Chunking

**Chase & Simon (1973)** — the chess masters study:

```
Task: Show chess position for 5 seconds, recall piece positions.

Chess masters: recall ~25 pieces of 26 correctly
Novices: recall ~6 pieces

BUT: Show random board (pieces placed randomly, not legal positions):
Chess masters: recall ~6 pieces — SAME AS NOVICES

Interpretation: Masters don't have better raw memory.
They have chunked ~50,000 meaningful patterns (chunks)
stored in LTM. A glance retrieves a chunk; the chunk
contains 4-5 piece positions.
```

**Chunking model**:
```
  Novice sees:          Expert sees:
  P at e4               "King's Indian setup"
  p at e5               (chunk containing 8 pieces +
  N at f3               their relations + typical
  n at c6               continuations)
  B at c4
  ...
```

**Long-term working memory** (Ericsson & Kintsch 1995): Experts can hold more in WM *because* they've built elaborate retrieval structures in LTM. WM isn't bigger; the cues in WM point to richer structures in LTM.

**Deliberate practice** (Ericsson et al. 1993):
- "10,000 hours" rule is a misrepresentation
- What matters is **deliberate practice**: specifically designed to address current weaknesses, with immediate feedback, at the edge of current ability
- Regular work experience ("just doing the job") doesn't produce the same gains
- Expert performance ≠ experience alone → requires structured improvement

**Application to software engineering**:
- Code review is practice only if you get and process feedback
- Reading code is lower-quality than writing + debugging
- Deliberately tackling problems just outside current skill > staying in comfort zone
- Senior engineers have large repertoire of patterns (chunks) — not just faster syntax recall

---

## Creativity

### Four-Stage Model (Wallas 1926)
```
1. PREPARATION     Gather information, define problem, identify
                   what is known and unknown
                   (often frustrating)

2. INCUBATION      Set problem aside — mind continues
                   processing unconsciously
                   (sleep, walk, shower)

3. ILLUMINATION    Sudden insight ("Aha!")
                   Often arises from right hemisphere activation
                   Remote associates suddenly connect

4. VERIFICATION    Test and refine the solution
                   Does it actually work?
```

**Convergent vs Divergent Thinking** (Guilford 1950):
- **Convergent**: One correct answer (most IQ tests, most school tasks)
- **Divergent**: Many possible answers (alternative uses test, open-ended problems)
- Creativity measures: fluency (many ideas), flexibility (different categories), originality (unusual ideas), elaboration (detailed ideas)

**Remote Associates Test (RAT)** (Mednick 1962):
```
Find one word connecting: pine / crab / sauce
Answer: apple
```
Measures the ability to find distant semantic associations — empirically linked to insight and creativity.

**Incubation as spreading activation**: During incubation, the brain continues to activate semantic networks. The critical feature: fixation on wrong representations decreases, and correct associations become accessible. This is why "sleeping on it" actually works (Harris et al. showed post-sleep insight gains).

---

## Flow (Csikszentmihalyi)

**Flow** (Csikszentmihalyi 1990): A state of optimal experience characterized by complete absorption in a challenging activity.

```
           HIGH CHALLENGE
                |
                |    FLOW ZONE
    ANXIETY     |  (skill matches challenge;
                |   full absorption)
         ───────┼────────────────────→
                |   BOREDOM
                |
           LOW CHALLENGE
    Low skill ──────────────── High skill
```

**Eight characteristics of flow**:
1. Complete concentration on the task
2. Clarity of goals and immediate feedback
3. Transformation of time (time passes differently)
4. Intrinsically rewarding (autotelic) — activity is its own reward
5. Effortlessness and ease
6. Balance between challenge and skills
7. Actions and awareness are merged; automaticity
8. Loss of self-consciousness

**Conditions to induce flow**:
- Clear goals with immediate feedback
- Challenge level ≈ skill level (+15% is a rough heuristic)
- Elimination of interruptions
- Autotelic framing: "this is interesting" not "I must perform"

**Relation to expertise**: Flow becomes more accessible as expertise grows. The novice is in anxiety or boredom; the expert can find the sweet spot in increasingly difficult challenges.

**The software engineer angle**: Flow states are disrupted by interruptions (meetings, Slack, notifications). Research shows it takes ~15–25 minutes to re-enter flow after interruption. This is why deep-work scheduling (Cal Newport) has empirical backing from the cognitive science of flow.

---

## Decision Cheat Sheet

| Problem Type | Best Approach |
|-------------|--------------|
| Well-defined, solution space small | Systematic search (BFS/DFS) |
| Well-defined, large state space | Means-ends analysis, heuristic search |
| Ill-defined, stuck with functional fixedness | Representational change: list all objects' possible functions |
| Stuck with mental set | Deliberate meta-cognitive break; try completely different approach |
| Novel problem with known analog | Explicit analogical mapping (don't rely on spontaneous transfer) |
| Requires creative leap | Incubation: deliberately step away after preparation phase |
| Skill development | Deliberate practice at the edge of ability, not comfort zone |

---

## Common Confusion Points

**Insight ≠ random lucky thought**: Insight problems require prior preparation. Incubation works only on problems you've already tried and failed. "Sleeping on it" works because the preparation phase loaded the relevant information — the unconscious processing needs something to work with.

**Chunking ≠ memorization of moves**: Chess masters' chunks are not sequences of moves. They are *spatial patterns* with associated strategic meanings. One chunk activates associated strategic plans. This is closer to schema theory than rote memorization.

**Deliberate practice ≠ any kind of practice**: The "10,000 hours" claim in popular press strips out the critical qualifier "deliberate." Playing chess casually for 10,000 hours doesn't produce grandmaster skill. Targeted practice with feedback at the edge of ability does.

**Flow ≠ relaxation**: Flow requires challenge. Relaxation is low-challenge. Flow is high-challenge + high-skill. A low-challenge task produces boredom, not flow, even if it's enjoyable.

**The Gestalt insight phenomenon is real, but small**: Not all problems are insight problems. Most everyday problem-solving is incremental. Insight effects are replicable but confined to specific problem types (compound remote associates, structural problems with misleading representations).

**Cross-reference**: For the neural basis of insight (gamma oscillations, right temporal lobe), see `neuroscience/03-COGNITION-COMPUTATION.md`. For AI problem-solving systems (GPS, SOAR, planning algorithms), see `cognitive-science/08-COMPUTATIONAL-MODELS.md`. For A* and search algorithms in CS, see `computing/26-ALGORITHMS.md`.
