# Rhetoric and Composition

## The Big Picture

Rhetoric and Composition (Rhet/Comp) is the academic field concerned with the teaching and theory of writing. It emerged as a distinct discipline in the late 19th century when universities began offering composition courses, and developed a theoretical framework in the 20th century through the influence of cognitive science, linguistics, and rhetorical theory. For a VP-level reader, the practical payoffs are in sentence-level style, writing process theory, and genre awareness — understanding not just *what* to write but *how* the writing decisions affect the reader.

```
+------------------------------------------------------------------+
|          RHETORIC AND COMPOSITION — LANDSCAPE                    |
+------------------------------------------------------------------+
|                                                                  |
|  THREE MAJOR PARADIGMS                                           |
|  Current-Traditional (19th c.–1970s): product focus,           |
|    five-paragraph form, correctness as the goal                  |
|  Process (1970s–present): writing as recursive process,         |
|    drafting/revising/editing as separable stages                 |
|  Post-Process (1990s–present): social/contextual turn,          |
|    genre theory, writing-as-participation in discourse           |
|                                                                  |
|  SENTENCE-LEVEL THEORY                                           |
|  Joseph Williams — Style: Toward Clarity and Grace              |
|  Richard Lanham — Revising Prose (the Paramedic Method)         |
|  Francis-Noël Thomas and Mark Turner — Clear and Simple         |
|  as the Truth (the Classic Style)                               |
|                                                                  |
|  PROFESSIONAL CONNECTION                                         |
|  Design documents, RFCs, strategy memos, executive summaries,   |
|  engineering proposals — all are genre instances.               |
|  Knowing genre norms is prerequisite to effective writing.      |
|  Sentence-level style: the difference between a document         |
|  that is read and one that is skim-checked.                     |
+------------------------------------------------------------------+
```

---

## Layer 1: Writing Process Theory

### The Paradigm Shift: From Product to Process

```
THE PROCESS PARADIGM — KEY INSIGHT
--------------------------------------
Before 1970s: composition teaching focused on the product
  (the finished essay). The goal was a well-formed essay
  that followed formal rules (thesis, evidence, conclusion;
  correct grammar and punctuation).

THE PROBLEM: Product-focused teaching doesn't help writers
  who produce bad first drafts (i.e., almost everyone).
  If the only feedback is on the finished product, the
  writer doesn't know how to improve the process.

THE SHIFT: Writing is recursive, not linear.
  Not: brainstorm → draft → proofread
  But: a recursive loop of drafting, revising, rethinking,
  restructuring, with "prewriting" and "revision" not
  as distinct stages but as interleaved activities.

LINDA FLOWER AND JOHN HAYES — COGNITIVE PROCESS THEORY (1981):
  Protocol analysis (writers thinking aloud while writing)
  revealed:
    1. Planning (generating goals, organizing, setting plans)
    2. Translating (producing text from plans)
    3. Reviewing (evaluating and revising)
  These are not sequential stages; they are processes
  that writers move between throughout the session.
  Expert writers plan more; novice writers draft and
  revise serially.

PRACTICAL IMPLICATION:
  The "write a first draft, then revise" advice is
  correct but incomplete. The revision that matters
  is structural (dispositio), not cosmetic (proofreading).
  Most professionals revise at the sentence level
  (cleaning up) when they should be revising at the
  structural level (does this argument work?).

THE MACRO REVISION CHECKLIST:
  Before editing sentences, verify:
  1. What is the single claim? (Is it stated explicitly?)
  2. Does every section support that claim?
     (Delete sections that don't.)
  3. Is the order correct for this audience?
     (BLUF for executives; narrative for persuasion;
      classical arrangement for complex arguments.)
  4. Are the transitions explicit?
     (Transitions should state the logical relationship,
      not just signal a new topic: not "Additionally..." but
      "This matters because...")
  5. Is the rebuttal addressed?
     (Toulmin: the strongest objection should appear
      and be answered.)
```

### The Cognitive Model of Writing — Why Junior Writers Struggle

The Flower/Hayes cognitive model (1981) is the standard research framework for understanding what actually happens when people write. Its diagnostic value is for understanding the failure modes you observe in junior writers — not as character flaws but as cognitive load problems.

```
FLOWER/HAYES MODEL — THE COGNITIVE ARCHITECTURE

Three processes that compete for working memory:
  PLANNING:      goal-setting, idea generation, organizing
  TRANSLATING:   converting plans into linguistic form
  REVIEWING:     evaluating and revising text

THE NOVICE WRITER'S PROBLEM:
  Low-level translation (word choice, sentence formation,
  grammar) is not yet automated. It occupies working memory
  that should be available for planning and reviewing.
  Result: the writer cannot plan and translate simultaneously.
  They write the first thing that comes to mind; they cannot
  hold an argument structure in working memory while also
  finding words for it.

  Observable symptoms in junior writers:
    - Linear drafting that never reaches the actual argument
    - Inability to revise structure (only surface edits)
    - Bloated prose (generation not filtered by planning)
    - Writing that answers the writer's question while writing,
      not the reader's question

THE EXPERT WRITER'S COGNITIVE PROFILE:
  Translation is automated (below conscious threshold).
  Working memory is free for planning and reviewing simultaneously.
  This is practice-induced automaticity, like a chess player
  who doesn't consciously calculate legal moves.

FREEWRITING (Peter Elbow, 1973) — THE MECHANISM:
  The reviewing process fires during drafting and interrupts translation.
  Freewriting (10 minutes continuous writing, no editing) temporarily
  disables the reviewer to let the translator generate raw material.
  This is not a technique for polished output; it is a diagnostic
  and warm-up for writers whose reviewer is too active during generation.
  When coaching a junior writer who is paralyzed by their own editing:
  prescribe freewriting. When coaching an experienced writer:
  the reviewing process is an asset, not a liability.

TWO-PASS STRATEGY — WHY IT WORKS:
  Reviewing requires distance from the translator's local choices
  to evaluate the document's global structure.
  Immediate review = reading what you intended to write.
  Cold review = approximating the reader's experience.
  The 24-hour gap works because working memory does not maintain
  the planning context after sleep — the planner's assumptions
  are no longer priming the reviewer's reading.
```

---

## Layer 2: Genre Theory

Genre theory is the most practically important contribution of post-process composition theory for professional writers.

### What Genre Actually Means

```
GENRE THEORY — THE RHETORICAL ACCOUNT
----------------------------------------
Pre-theoretical genre: classification of text types
  (the memo, the email, the report, the essay).
  These are useful categories but they describe form,
  not function.

**Genre theory names what expert practitioners already know implicitly**
If you have written and reviewed design docs, strategy memos, incident postmortems, and executive briefings, you already have deep genre knowledge — you know what goes where, what signals competence, what produces friction. Genre theory provides the analytical vocabulary for what you do intuitively. Its value: (1) making the implicit explicit so it can be taught; (2) explaining why violations of genre conventions produce friction beyond "that's not how we do things."

CAROLYN MILLER — "GENRE AS SOCIAL ACTION" (1984):
  Genres are typified rhetorical responses to
  recurring situations.
  Not just forms but social actions that have
  developed conventional forms because those
  forms work for those situations.

  The RFC (Request for Comments) is a genre.
  Its conventions (summary, motivation, design section,
  alternatives considered, backwards compatibility)
  are not arbitrary — each element responds to
  what engineers need to decide whether to adopt
  a proposal.
  Violating the genre conventions creates friction
  not because rules are being broken but because
  the audience cannot find what they need.

GENRE KNOWLEDGE:
  Expert writers have internalized genre conventions
  without necessarily being able to articulate them.
  Novice writers in a new professional context often
  produce technically correct text that violates
  genre expectations — the text is grammatically fine
  but it doesn't do what the genre is supposed to do.

  EXAMPLE: A new VP writes an executive summary that
  reads like a journal abstract (correct information,
  wrong genre). The executive doesn't get the BLUF
  they're looking for.

  EXAMPLE: A design document written as a narrative
  instead of a structured problem/solution document.
  The reader has to extract the structure mentally;
  effort is transferred to the reader.

THE PRACTICAL IMPLICATION:
  Before writing any document, identify the genre:
    What is this document supposed to do?
    Who reads it and in what circumstances?
    What are the genre conventions?
    What do readers expect to find, and where?
```

### Key Professional Genres

```
KEY PROFESSIONAL WRITING GENRES
---------------------------------
EXECUTIVE SUMMARY:
  Genre situation: senior decision-maker with 3-5 minutes.
  Genre conventions:
    First paragraph: the recommendation and the bottom line.
    Subsequent paragraphs: the minimum evidence needed
      to act on the recommendation.
    Supporting detail: linked or appended, not inline.
  Common violation: the executive summary that does not
    summarize but instead previews ("This document will
    argue...").

DESIGN DOCUMENT / RFC:
  Genre situation: engineers deciding whether to adopt
    or implement a technical proposal.
  Genre conventions:
    Summary (1 paragraph): what is being proposed.
    Context/motivation: why this is needed.
    Design: how it works.
    Alternatives considered: what else was evaluated
      and why it was rejected.
    Drawbacks/tradeoffs: honest acknowledgment.
    Rollout/migration: how to implement.
  Common violation: design document that presents
    only the chosen approach without alternatives
    (implies the decision has already been made).

THE STRATEGY MEMO (McKinsey-style):
  Genre situation: leadership deciding on direction.
  Genre conventions (Barbara Minto's pyramid principle):
    Hypothesis-first (not narrative-first).
    Top-down structure: situation → complication → question
      → answer.
    Each level: MECE (mutually exclusive, collectively
      exhaustive) — no gaps, no overlaps.
    Supporting evidence: pyramidal, with the most
      important evidence closest to the claim.
  Common violation: the strategy memo that leads with
    background and arrives at the recommendation only
    at the end (narrative structure where pyramid is needed).

INCIDENT POST-MORTEM:
  Genre situation: technical post-incident review.
  Genre conventions (blameless post-mortem):
    Timeline: what happened and when.
    Root cause analysis: not who but what systems
      and processes failed.
    Contributing factors: no single cause.
    Action items: specific, assigned, time-bounded.
  Common violation: post-mortem that assigns blame
    (the blameless norm is itself a genre convention
    that serves the function of honest reporting).
```

---

## Layer 3: Sentence-Level Style

### Williams: Clarity at the Sentence Level

```
JOSEPH WILLIAMS — STYLE: TOWARD CLARITY AND GRACE
---------------------------------------------------
Williams (1981, multiple editions) is the most rigorous
analysis of what makes sentences clear.

THE KEY INSIGHT: Most obscure sentences violate two principles:
  1. Characters (the agents of action) are not subjects.
  2. Actions (what happens) are not verbs.

NOMINALIZATIONS — THE PRIMARY ENEMY:
  A nominalization turns a verb into a noun.
  VERB: "We decided to proceed."
  NOMINALIZED: "Our decision was to proceed."
  NOMINALIZED FURTHER: "A decision was made to proceed."
    (Who decided? The agent has been buried or deleted.)

  Nominalizations:
    → Hide agency (who did this?)
    → Make sentences longer
    → Require weak verbs (is, was, are, have) to hold them
    → Create chains that force the reader to carry mental load

  THE TEST: Read your sentence and ask:
    "What is the real action here?"
    "Who is the real actor?"
    If the action is buried in a noun and the subject
    is abstract, revise.

  EXAMPLES (Williams's own):
    WEAK: "There is growing recognition of the fact that..."
    STRONG: "We are recognizing..."  or "Researchers now recognize..."

    WEAK: "The utilization of resources..."
    STRONG: "Using resources..." or "When we use resources..."

    WEAK: "The implementation of the plan was undertaken."
    STRONG: "We implemented the plan." / "The team implemented..."

THE STRESS POSITION:
  In English sentences, readers expect the most important
  information at the end of the sentence.
  "The dog bit the man." (who bit whom)
  "The man was bitten by the dog." (who was affected)
  Both are correct; they emphasize different information.
  Writers who don't control stress position accidentally
  emphasize the wrong thing.

  RULE: New information + most important information
  → end of sentence.
  Old information / context → beginning of sentence.
```

### Lanham: The Paramedic Method

```
RICHARD LANHAM — THE PARAMEDIC METHOD
----------------------------------------
Lanham (Revising Prose, 1981, multiple editions) provides
a procedural revision technique:

THE PARAMEDIC METHOD (8 steps):
1. Circle the prepositions.
2. Circle the "is/was/are/were" forms of "to be."
3. Ask: "Where's the action?" (The real action is often
   in a nominalization.)
4. Put the action in a simple active verb.
5. Ask: "Who's doing the action?" Make them the subject.
6. Rewrite using a short, clear sentence.
7. Check if the sentence now needs the context sentence
   to make sense. Combine or separate as needed.
8. Count the words.

THE LARD FACTOR:
  The percentage of words that can be cut without losing meaning.
  Professional prose typically has a lard factor of 30-50%.
  The method produces a drastically shorter sentence
  that is also clearer and more authoritative.

EXAMPLE:
  BEFORE (62 words):
  "At this point in time, there is a necessity for the
  development of a more efficient utilization of the
  resources that are available to us in the achievement
  of our organizational objectives."

  APPLYING THE METHOD:
  1. Prepositions: "in," "for," "of," "of," "to," "in," "of"
  2. "is" is present.
  3. Real action: "utilize" (hidden in "utilization")
     "achieve" (hidden in "achievement")
  4. Active verbs: "use," "achieve"
  5. Actors: "we"
  6. AFTER (9 words):
     "We need to use our resources more efficiently."
     (85% reduction; same meaning; more authority)

LARD PHRASES TO ELIMINATE:
  "at this point in time" → "now"
  "due to the fact that" → "because"
  "in the event that" → "if"
  "has the ability to" → "can"
  "is in a position to" → "can"
  "with regard to" → "about"
  "it should be noted that" → (delete entirely)
  "it is important to recognize that" → (delete)
```

### The Classic Style

```
THOMAS AND TURNER — CLEAR AND SIMPLE AS THE TRUTH (1994)
---------------------------------------------------------
The most important book on prose style written in the 20th century
for professional writers of non-fiction.

THE CLASSIC STYLE:
  A way of writing that treats prose as a window onto the world.
  The writer presents truth to the reader as if pointing
  at a scene visible to both.
  The style is confident, clear, and direct.
  It does not hedge, qualify, or call attention to itself.

FOUR DIMENSIONS:
  TRUTH: The classic writer believes they have something
    to say. They don't hedge the claim to protect themselves.
    "The plan will fail" not "The plan may have limitations."

  PRESENTATION: Writing is a window, not a mirror.
    The reader should see the subject, not the writer's
    struggle to describe it. No throat-clearing ("In this
    paper, I will argue..."); no meta-commentary.

  SCENE: Writer and reader are intellectual equals,
    and the writer is sharing a discovery.
    Not lecturing; not entertaining; discovering together.

  CAST: The writer is present but not intrusive.
    First person is fine; the classic style is not
    impersonal. But "I" should point outward (at the
    subject), not inward (at the writer's process).

WHAT CLASSIC STYLE IS NOT:
  Not plain style (which can be bare to the point of dullness).
  Not practical style (which exists only to transfer information).
  Not contemplative style (which turns inward, uses hedges,
    dwells in uncertainty).
  Not reflexive style (which makes the writing itself
    the subject: "As we have argued above...").

THE CONTRAST:
  REFLEXIVE (bureaucratic/academic):
    "This analysis seeks to examine the potential implications
    of the proposed architectural changes with respect to
    the performance characteristics of the system."
  CLASSIC:
    "The proposed changes will slow the system by 20%."
  Both sentences are about the same thing.
  One hides behind process; the other states a fact.
```

---

## Layer 4: Academic Argument

```
ACADEMIC ARGUMENT — THE GRADUATE SCHOOL MODEL
-----------------------------------------------
The academic argument has conventions that differ
from professional writing. These matter for a reader
who encounters academic literature (papers, studies)
and needs to evaluate them.

STRUCTURE OF AN ACADEMIC ARGUMENT:
  1. ENTER THE CONVERSATION (the literature review)
     Academic writing positions itself in a conversation.
     "X argues A; Y argues B; I will argue C."
     The entry point is not "Here is a new truth"
     but "Here is where I stand in relation to existing claims."

  2. STATE THE CLAIM (thesis)
     Academic thesis ≠ statement of topic.
     "This paper is about X" is not a thesis.
     "X is caused by Y, which overturns the assumption
     that it is caused by Z" is a thesis.
     A thesis has an argument that can be contested.

  3. EVIDENCE AND METHOD
     How do you know? (Empirical: data collection and analysis.
     Theoretical: logical derivation from premises.)
     The methodology section is the argument that the
     evidence is trustworthy.

  4. ACKNOWLEDGMENT OF LIMITATIONS
     Academic credibility requires acknowledgment of
     what your argument doesn't prove.
     The limitation section is not a weakness — it is
     a sign of intellectual honesty.

  5. CONTRIBUTION
     How does this change what we know?
     The contribution must be non-trivial.

EVALUATING ACADEMIC CLAIMS (for a practitioner):
  The study that says "our research shows X" is not
  automatically a claim that X is true in your context.
  Questions to ask:
    What was the sample? (N size, representativeness)
    Was the methodology appropriate to the claim?
    Was this peer-reviewed and replicated?
    What is the effect size? (Statistical significance ≠
      practical significance)
    Do the authors have conflicts of interest?
  A VP who cites academic research in strategy documents
  should apply this filter before citing.
```

---

## Decision Cheat Sheet

| I want to... | Tool |
|-------------|------|
| Write a first draft without getting blocked | Freewriting (generator mode): no editing, no rereading, set a timer |
| Revise a draft structurally | Macro revision: claim? structure? order? transitions? rebuttal? |
| Make a document match its genre | Identify genre situation: who reads this, in what circumstances, what do they need? |
| Cut word count by 40% without losing meaning | Lanham's Paramedic Method: find nominalizations, restore actors and verbs |
| Make technical writing clearer | Williams: subject = actor; main verb = main action; new info at end |
| Write with authority and confidence | Classic style: state the fact directly; window not mirror; no throat-clearing |
| Structure a strategy memo | Barbara Minto's Pyramid: situation → complication → question → answer (BLUF) |
| Evaluate an academic study | Sample, methodology, replication, effect size, conflicts of interest |

---

## Common Confusion Points

**Revision is structural, not cosmetic**
The most common professional revision error is spending time on sentence-level polish before the structure is sound. A beautifully written document with a wrong or unclear argument structure will fail. The correct order: macro revision (claim, structure, order, transitions) → paragraph revision (topic sentences, logic) → sentence revision (Williams/Lanham) → proofreading. Most writers do only the last two steps.

**Genre knowledge is invisible until violated**
Experts in a professional genre follow its conventions automatically and cannot always articulate them. The design document that reads like an academic paper, the executive summary that reads like a news article, the strategy memo that reads like a narrative — these create friction without the reader being able to say why. The diagnostic: "This feels off" usually means a genre norm has been violated.

**Classic style is not simple style**
Thomas and Turner are careful to distinguish classic style from plain style. Classic style is confident and clear but not bare. It assumes the writer has something to say and says it directly, as if presenting a visible truth to an intellectual equal. It is compatible with complex ideas. Plain style strips out everything including the ideas. The test: does the writing feel like a window onto a real subject, or does it feel like a cleared surface?

**Nominalizations are not always wrong**
Williams identifies nominalizations as the primary cause of murky professional prose. But nominalizations are not always wrong. "The decision" is a nominalization of "to decide" — and sometimes the decision is what the sentence is about. The issue is when the nominalization hides the actor ("A decision was made" vs. "The committee decided"). The test: is the agent recoverable and visible?
