# Cognitive Science Applied: Spacing and Retrieval

## The Big Picture

Cognitive science has produced the most robust, well-replicated, and practically actionable findings in education research. Three phenomena in particular -- spacing, retrieval practice, and interleaving -- have large effect sizes, replicate across settings, and are systematically underused in actual educational practice. The central irony: learners prefer strategies that feel productive but don't work well; the strategies that work feel harder and less comfortable.

```
+------------------------------------------------------------------+
|             COGNITIVE SCIENCE IN EDUCATION                       |
+------------------------------------------------------------------+
|                                                                  |
|  HIGH EVIDENCE, UNDERUSED           LOW EVIDENCE, OVERUSED       |
|  -------------------------          -----------------------       |
|  Spacing effect (distributed        Massed practice / cramming   |
|  practice)                          Re-reading                   |
|  Retrieval practice (testing        Highlighting                  |
|  effect)                            Summarizing                   |
|  Interleaving                       Learning styles (debunked)    |
|  Elaborative interrogation                                        |
|  Concrete examples                                                |
|  Dual coding (words + pictures)                                   |
|                                                                  |
|  COGNITIVE ARCHITECTURE             INSTRUCTIONAL DESIGN          |
|  ====================               =================            |
|  Working memory (~4 chunks)         Cognitive load theory        |
|  Long-term memory (schemas)         Worked examples effect        |
|  Forgetting curve                   Expertise reversal effect     |
|  Consolidation and sleep            Split attention effect        |
+------------------------------------------------------------------+
```

---

## The Spacing Effect

### Core Finding

The spacing effect is one of the oldest and most replicated findings in experimental psychology (Ebbinghaus, 1885). Distributed practice is more effective than massed practice for long-term retention, even when total study time is held constant.

```
  SPACING EFFECT
  ==============

  MASSED PRACTICE ("cramming"):
    Study all material in one long session.
    Short-term: high performance (cramming feels productive).
    Long-term: rapid forgetting.

    Day 1: ████████████ (8 hours of study)
    Exam tomorrow: 90%
    One week later: 40%
    One month later: 15%

  SPACED PRACTICE (distributed):
    Study divided into multiple sessions over time.
    Short-term: lower performance (feels less effective).
    Long-term: superior retention.

    Day 1: ████ (2 hours)
    Day 4: ████ (2 hours)
    Day 10: ████ (2 hours)
    Day 20: ████ (2 hours)
    Exam tomorrow: 75% (lower than cramming)
    One week later: 72% (much higher)
    One month later: 65% (dramatically higher)

  Total time: SAME. Retention: MUCH better with spacing.
```

### The Forgetting Curve and Optimal Spacing

```
  EBBINGHAUS FORGETTING CURVE
  ============================

  Memory retention
     |
  100%|*
     | **
     |   **
     |     ***
     |        ***
     |           ****
     |               ****
     |                   ****
     |                       *****
   0%+--+--+--+--+--+--+--+--+----> Time
      1  2  4  7  14 21 30 60 90
      hours/days after learning

  OPTIMAL RETRIEVAL SPACING:
    Retrieve just before you would forget.
    If you retrieve too early: too easy; weak memory trace.
    If you retrieve too late: you've already forgotten.
    Sweet spot: "desirable difficulty" (Bjork).

  PRACTICAL SCHEDULE:
    After initial learning:
    Review at: 1 day, 1 week, 1 month, 3 months, 1 year.
    Exponentially growing intervals.
    This is the algorithm behind Anki, SuperMemo (SM-2, SM-18).
```

### Mechanism: Why Spacing Works

```
  THEORETICAL MECHANISMS
  =======================

  ENCODING VARIABILITY:
    Each study session occurs in slightly different context.
    More retrieval cues associated with the memory.
    More routes to retrieval.

  CONSOLIDATION:
    Sleep-dependent memory consolidation between sessions.
    Hippocampus --> neocortex transfer during sleep.
    More sleep cycles between sessions = more consolidation.

  FORGETTING AND RELEARNING:
    Some forgetting between sessions means:
    Each subsequent retrieval requires more effort.
    Effort during retrieval = stronger memory trace.
    (Desirable difficulty: Bjork, 1994)
```

---

## Retrieval Practice (The Testing Effect)

### Core Finding

Testing yourself on material -- trying to recall it from memory -- produces dramatically better long-term retention than re-reading, even when total time is held constant. This is the "testing effect" or "retrieval practice effect."

```
  RETRIEVAL PRACTICE RESEARCH
  =============================

  Roediger & Karpicke (2006) Science paper:
    Groups studied a passage, then:
    SSSS: Read 4 times (4 study sessions)
    SSST: Read 3 times, test once
    STTT: Read once, test 3 times

    Immediate recall test: SSSS > SSST > STTT
    (More study = better short-term)

    1-week delayed recall: STTT > SSST > SSSS
    (More retrieval = better long-term)

  The group that felt they learned least (STTT)
  ACTUALLY retained most.
  This is why students underuse retrieval practice --
  re-reading feels more productive than it is.
```

### Forms of Retrieval Practice

```
  RETRIEVAL PRACTICE METHODS
  ===========================

  LOW STAKES QUIZZING:
    Frequent short quizzes in class.
    Not for grades -- for learning.
    Immediate feedback.

  FLASHCARDS:
    Classic retrieval practice.
    Spaced repetition algorithms (Anki) optimize timing.
    Work for vocabulary, facts, concepts.
    Less effective for complex relationships.

  FREE RECALL:
    Write down everything you remember.
    No prompts.
    Identifies gaps: what did you not write?

  PRACTICE TESTS:
    Full exam simulations.
    Most powerful when similar to final assessment.
    Reduces test anxiety (familiarity with test format).

  BLANK PAGE METHOD:
    After studying: close book, blank page.
    Write everything you know about the topic.
    Check against source.
    Identify gaps.

  WHY IT WORKS:
    Retrieval = active reconstruction.
    Reconstruction strengthens memory trace.
    Identifies what you don't know (metacognitive signal).
    Re-reading creates familiarity without deep processing.
    (Fluency illusion: "I recognize this" ≠ "I know this")
```

---

## Interleaving

### Core Finding

Interleaving (mixing different types of problems or subjects in a practice session) produces better long-term learning and transfer than blocked practice (completing all problems of one type before moving to the next).

```
  INTERLEAVING vs. BLOCKED PRACTICE
  ====================================

  BLOCKED (traditional):
    All addition problems --> All subtraction problems
    --> All multiplication problems

  INTERLEAVED:
    Mix addition / subtraction / multiplication
    within the same practice session.

  RESULTS:
    During practice: Blocked feels easier.
                     Interleaved feels harder.
    Post-test: Interleaved performs BETTER.
    Transfer: Interleaved performs MUCH better.

  MECHANISM:
    Blocked: you know the rule for the next problem
    before reading it (context cues you).
    Interleaved: you must identify WHICH rule to apply.
    Discrimination learning: "When is this type of
    problem used vs. that type?"
    This decision-making is exactly what real
    problems require.

  ROHRER ET AL. (2010, 2015): Mathematics experiments
    Interleaved practice improved test scores by ~25%
    vs. blocked practice on delayed tests.

  SPORTS APPLICATION:
    Variable practice (different shots in different
    order) > blocked practice for skill retention
    in motor learning (contextual interference effect).
```

---

## Cognitive Load Theory (Sweller, 1988)

The dominant instructional design theory grounded in information processing constraints:

```
  THREE TYPES OF COGNITIVE LOAD
  ================================

  INTRINSIC LOAD:
    Inherent complexity of the material.
    Depends on element interactivity (how many elements
    must be processed simultaneously).
    Cannot eliminate intrinsic load; it IS the learning.
    Can SEQUENCE material to manage it.

  EXTRANEOUS LOAD:
    Load imposed by poor instructional design.
    Irrelevant information; split attention; redundancy.
    Should be MINIMIZED.
    Examples: Decorative images in textbooks.
              Narration + identical on-screen text (redundancy).
              Diagram + explanation in different locations.

  GERMANE LOAD:
    Load associated with schema formation.
    "Desirable" cognitive effort.
    Useful elaboration, self-explanation, connection-making.
    Should be OPTIMIZED (not maximized blindly).

  TOTAL: Intrinsic + Extraneous + Germane ≤ WM Capacity.
  If extraneous is high, no room for germane.
  Good design minimizes extraneous to free room for germane.
```

### Instructional Design Effects from CLT

```
  WORKED EXAMPLE EFFECT:
    Novices learn better from worked examples than
    from problem-solving.
    Why: Problem-solving consumes WM with means-ends analysis.
         Worked examples free WM for schema acquisition.
    Application: Use worked examples heavily for novices.
    Fade to problems as expertise develops (scaffolding).

  EXPERTISE REVERSAL EFFECT:
    What helps novices hurts experts.
    Worked examples: helpful for novices; harmful for experts
    (redundant, creates unnecessary processing).
    Application: Differentiate instruction by expertise.

  SPLIT ATTENTION EFFECT:
    When two related materials must be processed together,
    physically integrating them reduces load.
    Diagram with labels IN the diagram vs. legend below.
    Physically integrated > split.
    Application: Integrate text and visuals.

  REDUNDANCY EFFECT:
    Presenting the same information in multiple formats
    hurts novices.
    Narrated animation + identical on-screen text:
    worse than narrated animation alone.
    Application: Don't add captions to narration unless
    for accessibility.

  MODALITY EFFECT:
    Visual + auditory is better than visual + visual.
    Diagram + spoken explanation > Diagram + written explanation.
    (Uses different cognitive subsystems; less competition)
```

---

## Elaborative Interrogation and Self-Explanation

```
  ELABORATIVE INTERROGATION
  ==========================

  Technique: Ask "why" questions during studying.
  Instead of: "Mammals are warm-blooded."
  Ask: "Why are mammals warm-blooded?" or
       "Why does this make sense given what I know?"

  Effect: Forces integration of new information
  with prior knowledge.
  Creates more retrieval routes.
  Moderate-strong evidence for retention improvement.

  SELF-EXPLANATION (Chi et al.):
    Students who explain material to themselves
    while studying learn more.
    "Chi et al.'s self-explanation effect":
    Students who self-explain physics problems
    outperform those who just read solutions.

    Method:
    Read: "The ball strikes the wall and bounces back."
    Self-explanation: "The wall exerts a force opposing
    the motion of the ball; by Newton's 3rd law..."

    Forces active processing and gap identification.
```

---

## Dual Coding (Paivio)

```
  DUAL CODING THEORY (Paivio, 1971)
  ====================================

  Two separate cognitive subsystems:
    VERBAL: words, text, language
    IMAGISTIC: pictures, diagrams, mental imagery

  Both systems can process information independently.
  Information encoded in both = more retrieval routes.
  Concrete words (dog, house) easier to remember than
  abstract words (justice, democracy):
  Concrete words can be BOTH verbally and imagistically coded.

  EDUCATIONAL APPLICATION:
    Combine text with relevant diagrams/illustrations.
    Draw diagrams while reading text.
    Encourage students to create visual representations.
    NOT: decorative images (irrelevant = extraneous load).
    YES: diagrams that show relationships text describes.

  MAYER'S MULTIMEDIA LEARNING PRINCIPLES:
    Build on dual coding.
    Multimedia principle: pictures + words > words alone.
    Coherence principle: less is more (remove irrelevant).
    Contiguity: integrate related material spatially.
```

---

## What Doesn't Work

```
  DEBUNKED PRACTICES
  ===================

  LEARNING STYLES (Visual/Auditory/Kinesthetic -- VAK):
    Claim: Students have preferred "learning styles"
    and learn best when instruction matches style.
    Evidence: NONE for the matching hypothesis.
    Pashler et al. (2008) systematic review: No credible
    evidence that matching instruction to preferred style
    improves outcomes.
    ~90% of teachers believe learning styles are real.
    About 20 meta-analyses: no evidence.
    This is one of the most studied and most robustly
    refuted claims in educational psychology.

  CRAMMING (for long-term learning):
    Works for short-term (tomorrow's exam).
    Fails for long-term retention.
    Most professional/life knowledge requires long-term.

  RE-READING:
    Students rate it as their most common strategy.
    Modest effect on retention. Creates familiarity
    (fluency illusion) without testing actual recall.
    Far inferior to retrieval practice.

  HIGHLIGHTING:
    Popular; low effectiveness.
    Identifying information ≠ encoding it deeply.
    Can be slightly useful if done analytically
    (deciding WHAT to highlight = processing).

  MYTH OF MULTI-TASKING:
    No one multi-tasks on cognitive tasks.
    Task-switching with switching cost.
    Studying while watching TV: both suffer.
```

---

## Decision Cheat Sheet

| Strategy | Evidence | Effect Size | Effort | Use When |
|----------|----------|-------------|--------|----------|
| Retrieval practice | Very strong | Large | High | Always, for all material |
| Spacing | Very strong | Large | High planning | Always, when time allows |
| Interleaving | Strong | Medium-large | High | After initial learning |
| Elaborative interrogation | Moderate | Medium | Medium | Factual/conceptual learning |
| Dual coding | Moderate | Medium | Medium | Complex/relational material |
| Worked examples | Strong | Large | Low for learner | Novice learners |
| Re-reading | Weak | Small | Low | Never as primary strategy |
| Learning styles matching | None | Zero | Variable | Never |

---

## Common Confusion Points

**Retrieval Practice Is Not Just Testing for Grades**
The testing effect works even when the test is low-stakes, ungraded, and private. The mechanism is the act of retrieval, not the evaluation. A student quizzing themselves with flashcards, writing from memory, or doing practice problems gets the benefit without formal grading.

**Spacing Feels Worse Than Cramming During Study**
This is the fundamental challenge: spacing is harder and produces lower performance during the study session itself. Students (and teachers) interpret this difficulty as ineffectiveness. Bjork's "desirable difficulties": the difficulty IS the mechanism. Feeling harder during study = stronger memory trace.

**Cognitive Load Theory Applies to Instructional Design, Not Just Learner Strategy**
CLT is primarily an instructional design theory. Its implications are for HOW to teach (worked examples, integrated diagrams, modality choices) as much as how to study. A brilliantly motivated student using optimal strategies can still fail if the instruction maximizes extraneous load.

**Interleaving Works Best After Initial Acquisition**
For complete novices, some blocked practice is appropriate during initial acquisition of each skill. Interleaving is most powerful once learners have some competence in each component being interleaved. Don't interleave before any component is learned.
