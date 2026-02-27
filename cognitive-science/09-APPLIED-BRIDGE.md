# Applied Cognitive Science — Bridge to Engineering

## The Big Picture

Cognitive science produces theories; this module applies them. The bridge from lab to practice — particularly for software engineers and technical leaders making decisions about systems, teams, and learning.

```
+------------------------------------------------------------------+
|  APPLIED COGNITIVE SCIENCE: DOMAINS                              |
+------------------------------------------------------------------+
|                                                                  |
|  HCI / UX                   LEARNING SCIENCE                     |
|  ─────────                  ────────────────                     |
|  Fitts' Law                 Spacing effect                       |
|  Hick's Law                 Testing effect (retrieval practice)  |
|  Cognitive Load Theory      Interleaving                         |
|  GOMS                       The learning styles myth             |
|                                                                  |
|  COGNITIVE ERGONOMICS       ENGINEERING BIASES                   |
|  ──────────────────         ──────────────────                   |
|  Situation Awareness        Planning fallacy                     |
|  Naturalistic DM            Confirmation bias in debugging       |
|  Mode confusion             Hindsight bias in post-mortems       |
|                             Automation bias                      |
|                                                                  |
|  NUDGE THEORY               THE REPLICATION CRISIS               |
|  ────────────               ─────────────────────                |
|  Choice architecture        What survived                        |
|  Default effects            What failed                          |
|  Libertarian paternalism    What it means for evidence           |
+------------------------------------------------------------------+
```

---

## HCI and UX — The Psychophysical Laws

### Fitts' Law (1954)

```
  MT = a + b × log₂(2D/W)

  MT = movement time
  D  = distance to target
  W  = width of target
  a, b = empirical constants

  Simplified: index of difficulty = log₂(2D/W)

  Example:
  Tiny button far away:  ID = log₂(2 × 400 / 10) = 6.3 bits
  Large button nearby:   ID = log₂(2 × 50 / 100) = 0.0 bits
```

**Implications for UI design**:
- Make frequently used targets larger and closer
- Corners and edges of screens are "infinite size" targets (cursor stops at screen edge) — excellent for menus
- Pie menus outperform linear menus (all items same distance from center)
- Touchscreen targets need to be larger than cursor targets (motor variability is higher)
- The taskbar in Windows exploiting screen edge: deliberately Fitts-optimal

**Fitts' Law applies to**: Mouse pointing, touchscreen tapping, eye movements, voice command selection latency (distance = phonetic distance).

### Hick's Law (1952)

```
  RT = a + b × log₂(n + 1)

  RT = reaction time to choose between options
  n  = number of choices
  a, b = empirical constants

  Each additional option adds approximately equal RT increment
  (because log is sub-linear — doubling choices adds one bit)
```

**Implications**:
- Menus: flatten the hierarchy (fewer deeply nested choices) vs. widen (more top-level choices) → Hick's Law argues for some nesting to keep n manageable
- Search interfaces reduce n effectively to near-1 → optimal for large choice sets
- Emergency procedures: reduce choices at critical moments (nuclear/aviation checklists)
- Navigation: reducing options at each node vs. one large list → context determines

**Together Fitts + Hick**: Most UI design problems are about trading movement time (Fitts) against choice time (Hick). Quick-launch bars win on Fitts; search boxes win on Hick.

### Miller's Law (1956, somewhat misrepresented)

```
  "The magical number seven, plus or minus two" — working memory chunks

  Original finding: digit span ~7 ± 2 items
  Modern finding: ~3-4 chunks without rehearsal (Cowan 2001)
  The "7" benefit comes from verbal rehearsal (the phonological loop)

  What "chunking" means:
  Raw digits:    7 4 8 3 9 2 1 = 7 chunks
  Phone number:  748-392-1 = 3 chunks (if you know the structure)
  Meaningful seq: 1 9 9 1 9 1 1 = ??? depends on your knowledge
```

**UI application**: Don't use "7 items per menu" as a rule — it's too simplistic. What matters is the *semantic chunking* that users can apply. Grouped, labeled items can be much longer than 7.

### Cognitive Load Theory (Sweller 1988)

```
THREE TYPES of cognitive load:

  INTRINSIC          EXTRANEOUS         GERMANE
  ─────────          ──────────         ───────
  Inherent to the    Caused by bad      Used for schema
  material being     design / poor      formation and
  learned            presentation       learning

  Can't reduce it    Should MINIMIZE    Should MAXIMIZE
  (it's the          (it wastes WM      (it builds
  content)           resources)         understanding)

  Example: learning  Example: confusing  Example: comparing
  async/await is     layout requires    two code examples
  inherently complex reading twice      to extract pattern
```

**UI/documentation design**:
- Segment complex material (reduce intrinsic load per unit)
- Eliminate redundancy (split-attention effect: don't make user look at diagram AND separate text simultaneously — integrate them)
- Use worked examples (reduces extraneous; optimizes germane)
- Progress: novice needs more scaffolding; expert needs less (expertise reversal effect)

### Dual-Coding Theory (Paivio 1971)

Visual and verbal systems are separate but can be linked. Information encoded in *both* systems is better retained than information in one system alone.

**Application**: Combine text with relevant diagrams (not decorative images). The diagram creates a visual code; the text creates a verbal code; both activated together = better encoding.

**The deeper point**: Both Fitts' Law and Hick's Law are information-theoretic results, not just empirical regularities. Fitts' Law is Shannon's Theorem 17 applied to the human motor channel — the index of difficulty ID = log2(2D/W) is literally the channel capacity in bits required to hit a target of width W at distance D. Hick's Law is Shannon's channel capacity applied to choice reaction time — each choice is one bit of information, and RT grows linearly with bits. The log2 in both formulas is not a coincidence; it reflects the human motor and decision systems operating near their information-theoretic capacity limits.

**Where these laws break**: Fitts' Law was derived for stylus/mouse pointing. On touchscreens, the "width" W must account for the finger's contact area and the fat-finger problem — effective W is reduced by motor variability that differs from mouse pointing. For gesture interfaces, the distance metric becomes 3D and the "target" may be a pose region, not a spatial target. For voice interfaces, Hick's Law still applies to the *decision* component, but Fitts' motor component drops out entirely — replaced by articulatory complexity.

**The quantitative design tradeoff**: At the system level, you're trading Fitts' cost (movement time to reach controls) against Hick's cost (decision time among options at the current level). Deeply nested menus minimize Hick's cost per level but maximize Fitts' cost (more traversals). Flat layouts minimize Fitts' cost but increase Hick's cost. The KLM (keystroke-level model) lets you compute the total task time quantitatively for both designs and choose the optimum.

### GOMS (Card, Moran, Newell 1983)

A framework for modeling user task performance:
```
  Goals     — what the user wants to accomplish
  Operators — basic actions (keystrokes, mouse clicks, eye fixations)
  Methods   — sequences of operators to accomplish a goal
  Selection rules — which method to use when multiple exist

  Keystroke-Level Model (KLM): predict task completion time
  from a list of low-level operators with known average durations:
    K = keystroke: 0.2s
    P = pointing (mouse): 1.1s
    H = homing (hand to/from keyboard): 0.4s
    M = mental operation: 1.35s
    R(t) = system response time t
```

---

## Learning Science — What Actually Works

These findings have survived the replication crisis and have large effect sizes.

### Spacing Effect (Distributed Practice)

```
MASSED PRACTICE:       Read chapter → read it again → read it again → test
                       Performance at test: modest
                       Retention one week later: poor

DISTRIBUTED PRACTICE:  Read chapter → [wait] → review → [wait] → test
                       Performance at test: modest (same as massed)
                       Retention one week later: SUBSTANTIALLY BETTER
```

**Why it works** (Forget-to-learn theory): Forgetting is not failure — it's a prerequisite for spacing benefits. When you retrieve a memory that has partially faded, you strengthen it more than re-studying immediately. The benefit comes from the *retrieval effort*.

**Effect size**: One of the largest effects in applied memory research. Effect size d ≈ 0.6–1.0. Robust across age groups, material types, and time scales.

**Optimal spacing**: Expands as material is better learned. For new material: review the next day. Then 3 days. Then 1 week. Then 2 weeks. (Anki uses a variant of this with the SM-2 algorithm.)

### Testing Effect / Retrieval Practice (Roediger & Karpicke 2006)

```
STUDY-STUDY group:     Read passage → study again
STUDY-TEST group:      Read passage → try to recall without looking

Final test 1 week later:
  STUDY-STUDY:  ~40% retention
  STUDY-TEST:   ~60% retention

The test group DID WORSE on the immediate test but MUCH BETTER
on the delayed test.
```

**Why it works**: Retrieval *strengthens* the memory trace more than re-exposure. The act of reconstructing a memory makes it more retrievable in the future. This is not just repetition — the reconstruction is the mechanism.

**Application**: Self-testing while learning (flashcards, practice problems, writing summaries from memory) beats re-reading repeatedly. This is why code challenges and projects beat reading documentation over and over.

### Interleaving

```
BLOCKED practice:      Problem type A, A, A, A, B, B, B, B, C, C, C, C
INTERLEAVED practice:  A, B, C, A, C, B, C, A, B, B, C, A

Immediate test:        Blocked > Interleaved (blocked feels easier)
One week later:        Interleaved > Blocked (sometimes 2x better)
```

**Why it works**: Interleaving forces you to *select the right method* as well as apply it. With blocked practice, you already know which method to use. Interleaving trains the discrimination — harder in training, better in transfer.

**Application**: When learning algorithms, don't do 30 sorting problems, then 30 graph problems. Mix problem types. When reviewing code, interleave different system areas rather than doing deep dives into one area exclusively.

### What Doesn't Work — Learning Styles Myth

```
CLAIM: Students have visual/auditory/kinesthetic learning styles (VAK).
       Teaching should match the student's preferred style.

EVIDENCE: Multiple large, well-controlled studies find:
  - Students do have PREFERENCES
  - Teaching to the preference does NOT improve learning outcomes
  - Pairing preference to instruction = no effect
  - Best instruction style depends on CONTENT not learner preference
    (diagrams are better for spatial topics regardless of preference)

Status: No credible evidence learning styles affect outcomes.
        Very large educational market built on this myth.
```

**What does help** (replicated, large effects):
- Spacing and retrieval practice ✅
- Interleaving ✅
- Elaborative interrogation ("why is this true?") ✅
- Concrete examples before abstractions ✅
- Generative activities (create, explain, summarize from memory) ✅

---

## Cognitive Ergonomics

**Historical note**: Hick himself cited Shannon in the original 1952 paper — the law is explicitly derived from information theory. The human choice-reaction system operates as a noisy channel with capacity approximately 2-3 bits/second for simple choices. This is why adding choices increases RT logarithmically: each additional bit of information in the stimulus requires a fixed increment of processing time.

### Endsley's Situation Awareness (SA)

```
  LEVEL 1: PERCEPTION
    Detecting relevant elements in the environment
    "The system is responding slowly"
    "The deployment queue is backing up"

  LEVEL 2: COMPREHENSION
    Understanding the *meaning* of what's perceived
    "This means we're hitting the rate limiter"
    "The backlog indicates upstream failure"

  LEVEL 3: PROJECTION
    Predicting future states based on current understanding
    "If this continues, the SLA will be breached in 15 minutes"
    "The downstream services will start timing out next"

  SA ERRORS:
  Level 1 failures: key indicator not monitored / noticed
  Level 2 failures: data perceived but misinterpreted
  Level 3 failures: current understanding but wrong prediction
```

**Aviation disasters and SA**: CFIT (Controlled Flight Into Terrain) — crew perceived altitude but didn't comprehend the significance relative to terrain. Mode confusion (Air Inter Flight 148, 1992) — crew thought they were flying at 3,300 feet/min vertical speed, actually 3,300 feet/min descent *rate* — a mode difference they didn't perceive.

**Software engineering SA**: Incident response is a SA problem. Dashboards should be designed for Level 1 SA (perception); runbooks for Level 2 (comprehension); predictive alerts for Level 3 (projection).

### Naturalistic Decision Making (Klein)

Laboratory decision research (Kahneman/Tversky) studies *novices* making *choices between presented options* in low-stakes settings.

**NDM** (Klein's Recognition-Primed Decision model): Studies *experts* making decisions *under time pressure with incomplete information* in high-stakes real environments.

```
RPD MODEL:
  Situation → Recognition (experienced professional matches to class of situation)
  → Mental simulation (quickly run through the action mentally)
  → Execute if simulation succeeds
  → Adjust if simulation fails

  No comparison of multiple options.
  One option is generated and checked.
  Works because experts have high-quality recognition from experience.
```

**Application**: Senior engineers don't debug by exhaustive hypothesis testing. They recognize patterns from experience and check the most likely cause. This looks like bias ("jumping to conclusions") but is expertise.

---

## Cognitive Biases in Engineering (Direct Mapping)

| Cognitive Bias | Engineering Context | Mitigation |
|---------------|--------------------|----|
| **Planning fallacy** | "This feature will take 2 weeks" (takes 8) | Reference class forecasting: how long did similar features take? |
| **Confirmation bias** | Debug by testing expected failure modes only | Adversarial testing; have someone else review; pre-commit to what *would* change your mind |
| **Sunk cost fallacy** | Keep maintaining a bad architecture because "we've invested 2 years" | Ask: "If we were starting today, would we build this?" |
| **Hindsight bias** | Post-mortems attribute failure to "obvious" errors | Blameless post-mortems with timeline focus; distinguish what was known at the time |
| **Status quo bias** | "The current system works, don't change it" | Require explicit articulation of switching costs |
| **Automation bias** | Trusting linter/CI output without judgment | Regularly audit automated tool outputs; define failure modes |
| **Overconfidence** | 90% confidence intervals too narrow in estimation | Pre-mortem exercise: "imagine the estimate was wrong; why?" |
| **Dunning-Kruger** | Junior devs estimate confidently; seniors hedge more | Calibration: track estimates vs actuals systematically |
| **Framing effect** | "1 in 1,000 failure rate" vs "99.9% success rate" flip evaluations | Always present both framings for important decisions |

---

## Nudge Theory (Thaler & Sunstein 2008)

**Choice architecture**: The way options are presented affects which option is chosen, independent of the options' content.

**Key principle**: Small, low-cost changes to environment can have large effects on behavior, without restricting freedom (libertarian paternalism).

**Mechanism** | **Example** | **Effect size**
--- | --- | ---
**Default effects** | Organ donation opt-out vs opt-in countries | Opt-out ~90% donation rate; opt-in ~15% |
**Social norms** | "90% of your neighbors have paid their taxes" | 5-15% tax compliance increase |
**Simplification** | Reduce pension enrollment to one question | Enrollment rate 3× increase |
**Salience** | Traffic warning on road → accident rate down | Variable but often 10-30% |
**Commitment devices** | Set a savings rate that increases with raises | Large retirement savings increase |

**Application to software teams**:
- Default CI on → more code is tested (default effect)
- "Most engineers at this company write tests first" → increases TDD adoption (social norm)
- Code review template with checklist → fewer skipped reviews (simplification)
- Sprint velocity displayed in team room → salience effect on productivity

**Limits of nudge theory**:
- Large nudge effects are often on defaults/automatic behaviors
- For deliberate decisions with high stakes, nudge effects are smaller
- "Choice architecture" can be manipulative (dark patterns in UI = hostile nudges)
- Effect sizes often smaller than initial studies suggested (replication issues)

---

### Detailed Mitigations for the Three Most Damaging Engineering Biases

**Planning fallacy — Reference Class Forecasting (Flyvbjerg)**:
```
PROCEDURE:
1. Define the reference class: "projects of type X at this org"
   (not "all projects" — too broad; not "this exact project" — too narrow)
2. Collect the distribution: actual durations for 10-20 past projects in the class
3. Use the distribution's median (not mean — skewed data) as the base estimate
4. Adjust from the base only for specific, articulable reasons why THIS project
   differs from the reference class
5. Cap the adjustment: never adjust by more than 20-30% from the reference class
   unless you can name the specific mechanism

WHY IT WORKS: Forces the outside view. The inside view (imagining your specific
timeline) is optimistic by ~30-70%. The outside view (base rates) is calibrated.
```

**Confirmation bias — Pre-Mortem (Klein)**:
```
PROCEDURE:
1. Before the decision/project launch: "Imagine it is 6 months from now.
   The project has FAILED. Write down why it failed."
2. Each team member writes independently (no groupthink contamination)
3. Collect and cluster the failure modes
4. For each cluster: "What would we do NOW to prevent this?"
5. Add the top 3-5 preventive actions to the project plan

WHY IT WORKS: Legitimizes dissent. In a normal planning meeting, raising
concerns = being negative. In a pre-mortem, raising concerns = being
thorough. Prospective hindsight (imagining the failure as already happened)
increases identification of potential problems by ~30% (Mitchell et al. 1989).
```

**Hindsight bias — Blameless Post-Mortem structure**:
```
PROCEDURE:
1. TIMELINE FIRST: Reconstruct the sequence of events and decisions
   with timestamps. What was known at each decision point?
2. INFORMATION AVAILABLE: For each decision, document ONLY what the
   decision-maker knew at the time — not what was learned afterward
3. REASONABLE ALTERNATIVES: Given what was known, what alternatives
   existed? Were they reasonable given the information available?
4. SYSTEMIC FACTORS: What system/process/tooling gaps made the
   failure mode possible? (Not: who failed to catch it)
5. ACTION ITEMS: Changes to systems/processes, not changes to people

WHY IT WORKS: Hindsight bias makes past failures look "obvious" — but they
weren't obvious with the information available. The timeline reconstruction
forces the team to evaluate decisions against the information set at the
time, not the full-knowledge retrospective view.
```

## The Replication Crisis — What Survived

**The Open Science Collaboration (2015)**: Attempted to replicate 100 psychology studies. ~39% replicated (strict criteria) to ~68% (less strict). Effect sizes on average halved.

### Notable Casualties

| Claim | Status |
|-------|--------|
| **Ego depletion** (Baumeister: willpower depleted by use) | Multiple large pre-registered failures to replicate |
| **Money priming** (thinking about money → selfish behavior) | Large multi-lab replication: p=0.52, no effect |
| **Priming effects generally** (subtle environmental cues → large behavior changes) | Most large social priming effects fail to replicate |
| **Power poses** (Cuddy: standing like Wonder Woman → hormonal changes + confidence) | Hormonal effects failed; behavioral confidence effects mixed |
| **Facial feedback hypothesis** (pencil in mouth → rate cartoons funnier) | Failed in direct replication |
| **Marshmallow test** (see 06-DEVELOPMENT.md) | Effect dramatically shrinks with SES controls |
| **Implicit Association Test predicts bias** | Poor test-retest reliability; weak behavior prediction |

### What Survived

| Finding | Evidence |
|---------|---------|
| **Spacing effect** | Huge, replicated across labs, ages, materials |
| **Testing effect / retrieval practice** | Huge, replicated |
| **Interleaving** | Replicated; included in cognitive psychology consensus |
| **Cognitive dissonance** | Core effects replicated |
| **Dual-process theory (broadly)** | Behavioral evidence robust; mechanistic details debated |
| **Loss aversion** | Replicated in economic decisions; magnitude varies by context |
| **Stroop effect** | ~100 years of robust replication |
| **Priming with brief exposures** (simple perceptual) | Replicated |
| **Availability heuristic** | Core effects robust |
| **Planning fallacy** | Robust in real-world estimates |
| **Müller-Lyer + other classic illusions** | Fully replicated |

### Lessons for Evidence Consumers

```
HIGH TRUST:
  - Pre-registered studies
  - Large samples (N > 200)
  - Multi-lab replications
  - Large effect sizes (d > 0.5)
  - Theoretically predicted, not p-hacked

LOW TRUST:
  - Single lab, small N (< 50)
  - Surprising, counterintuitive effects
  - "Too clean" results (Simmons et al. p-hacking)
  - Results published without pre-registration
  - Social priming studies especially

ZERO TRUST:
  - "Studies show..." without citations
  - Effect sizes not reported
  - Failed replications brushed off
```

---

## Decision Cheat Sheet

| Applied Problem | Cognitive Science Framework | Action |
|----------------|---------------------------|--------|
| Design a more usable button | Fitts' Law | Larger target, closer to current cursor position |
| Simplify a complex menu | Hick's Law | Reduce choices per level; use search for large sets |
| Train someone new on a complex system | Cognitive Load Theory | Segment; worked examples; reduce extraneous load |
| Improve long-term knowledge retention | Spacing + testing effect | Spaced repetition with active recall |
| Improve debugging speed | Expertise + chunking | Build pattern library; deliberate practice on failure modes |
| Run a better post-mortem | Hindsight bias + SA | Timeline reconstruction; "what was known at the time" |
| Make a more realistic project estimate | Planning fallacy | Reference class; outside view; pre-mortem |
| Evaluate a psychology claim | Replication crisis checklist | Pre-registered? Large N? Multi-lab? Large effect? |
| Increase team adoption of a practice | Nudge theory | Default it on; show peer norm; simplify the process |

---

## Common Confusion Points

**Fitts' Law is not a guideline — it's a law**: MT = a + b × log₂(2D/W) makes quantitative predictions you can test. It's not "make buttons bigger is good" — it's a precise model you can use to predict pointing time and compare design alternatives numerically.

**Cognitive Load Theory ≠ "keep it simple"**: It's a precise framework with three distinct load types. Intrinsic load can't be reduced (it's the inherent complexity of the subject). The target is reducing extraneous (design) load, not the intrinsic load of understanding a complex system.

**"Evidence-based" learning ≠ "learning styles"**: Learning styles are not evidence-based. The evidence-based techniques are spacing, retrieval practice, and interleaving — these are often counterintuitive (they feel harder) but produce dramatically better long-term retention.

**Nudge ≠ manipulation**: Thoughtfully designed: choice architecture that promotes welfare while preserving freedom of choice. Maliciously designed: dark patterns (making it hard to cancel subscriptions, hiding costs). Same cognitive mechanisms; opposite ethics.

**Replication crisis ≠ "psychology is useless"**: Core psychophysical findings (Stroop, illusions, spacing, retrieval practice) are extremely robust. Social priming effects are not. Know the difference. The replication crisis has made the field stronger by eliminating false findings.

**Cross-reference**: For the basic science underlying these applications, see `cognitive-science/02-ATTENTION-MEMORY.md` (working memory + spacing), `03-REASONING-JUDGMENT.md` (biases), `05-PROBLEM-SOLVING.md` (expertise + chunking). The Fitts/Hick laws connect to signal detection theory and Bayesian models in `08-COMPUTATIONAL-MODELS.md`. For team/organizational aspects of planning fallacy and biases, see `economics/03-MECHANISM-DESIGN.md`.
