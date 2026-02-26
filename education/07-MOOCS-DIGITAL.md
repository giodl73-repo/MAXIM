# MOOCs, EdTech, and the Completion Crisis

## The Big Picture

The Massive Open Online Course (MOOC) revolution (2012) promised to democratize higher education: world-class instruction freely accessible to anyone with internet. What actually happened was more complicated: MOOCs revealed a profound completion problem, failed to disrupt higher education as predicted, but succeeded as professional development tools, and the data they generated has informed adaptive learning systems that represent the more durable EdTech transformation.

```
+------------------------------------------------------------------+
|                 MOOCs AND EDTECH LANDSCAPE                       |
+------------------------------------------------------------------+
|                                                                  |
|  MOOC HISTORY                    EDTECH ECOSYSTEM               |
|  ------------                    ---------------                 |
|  2008: First cMOOC (Siemens)     LMS: Canvas, Blackboard, Moodle|
|  2011: AI class (Thrun, Norvig)  Video: YouTube, Panopto         |
|  2012: "Year of the MOOC" (NYT)  MOOC: Coursera, edX, Udacity   |
|  Coursera, edX, Udacity          Adaptive: Khan, ALEKS, Carnegie |
|  2013-15: Hype → Disillusion     AI Tutors: Khanmigo, Socratic   |
|  2020: COVID → massive adoption  Assessment: Turnitin, Proctorio |
|                                  OPM: 2U, Pearson Online         |
|  COMPLETION CRISIS               Analytics: learning analytics   |
|  -----------------               platforms                       |
|  3-15% completion rates                                          |
|  Who completes? Already educated POLICY QUESTIONS                |
|  Dropout reasons: multifactorial Free vs. credentialed MOOCs     |
|  Self-paced = harder to finish   Online vs. in-person outcomes   |
|                                  AI in assessment (integrity)    |
+------------------------------------------------------------------+
```

---

## MOOC History

### The Two MOOC Models

```
  TWO MOOC PARADIGMS
  ===================

  cMOOC (Connectivist MOOC)
  Origin: Siemens & Downes (2008)
  "Connectivism and Connective Knowledge" course

  PHILOSOPHY:
    Learning is network-based.
    Knowledge is distributed across participants.
    Course = catalyst for connections between learners.
    No central content repository.
    Learners create, share, and build on each other's work.

  STRUCTURE:
    Loosely structured.
    Participants blog, tweet, contribute resources.
    Weekly themes, not strict lessons.
    The community IS the curriculum.

  LIMITATIONS:
    Doesn't scale to hundreds of thousands.
    Requires high learner initiative.
    Not suitable for technical/procedural skills.

  xMOOC (Extended MOOC)
  Origin: Sebastian Thrun's AI class (Stanford, 2011)

  PHILOSOPHY:
    Distribute elite university content widely.
    Same course to 160,000 students.
    Lecture videos + quizzes + peer-graded assignments.

  STRUCTURE:
    Recorded lecture videos (10-15 min segments).
    Auto-graded quizzes.
    Forum discussions.
    (Sometimes) peer-graded assignments.
    Optional: proctored exam for certificate.

  The xMOOC model is what "MOOC" typically means today.
  Coursera, edX, Udacity = xMOOC platforms.
```

### The 2012 Explosion

```
  2012: "YEAR OF THE MOOC"
  =========================

  TIMELINE:
    Jan 2012: Coursera founded (Ng, Daphne Koller, Stanford)
    May 2012: edX founded (MIT + Harvard)
    Udacity: Thrun leaves Stanford to found Udacity
    Venture capital: hundreds of millions invested.

  NARRATIVES:
    "This is the tsunami that's going to sweep higher education."
    "The college bubble is about to burst."
    "Every student in the world will have access to
    MIT and Harvard professors."

  ASSUMPTIONS:
    Content = the bottleneck in education.
    Remove content bottleneck = democratize education.
    Technology = neutral delivery mechanism.

  WHAT THE ASSUMPTION MISSED:
    Learning is not consumption of content.
    Success in higher ed requires:
    - Motivation and support structures
    - Feedback and assessment
    - Social connection and accountability
    - Credential value (employer recognition)
    - Prior preparation
    MOOCs addressed content delivery only.
```

---

## The Completion Crisis

### The Numbers

```
  MOOC COMPLETION RATES
  ======================

  Average completion rate: 3-15% of enrolled students.
  (Completion = finishing the course with a grade/certificate)

  Context:
    A course with 100,000 enrollees may complete 3,000-15,000.
    Still large in absolute terms.
    But: suggests 85-97% of enrolled students don't finish.

  COMPARISON:
    Traditional college course: ~90-95% completion.
    Community college course: ~60-70% completion.
    MOOC: 3-15% completion.

  WHO COMPLETES?
    Studies (Ho et al., MIT; Koller et al., Coursera):
    Completers are disproportionately:
    - Already have bachelor's degrees
    - Employed professionals
    - From high-income countries
    - Male (varies by subject)
    - Already motivated and self-directed

    The democratization promise: NOT for the least-advantaged.
    MOOCs serve the already-educated most effectively.
```

### Why People Don't Complete

```
  DROPOUT TAXONOMY
  ==================

  DIVERSE INTENTIONS:
    Not everyone enrolls to complete.
    "Browsing": checking out the content, no commitment.
    "Auditing": watching lectures without doing work.
    "Sampling": few videos from relevant topic.
    Real completion rate = completers / serious starters.
    Still low even on this adjusted basis.

  EXTERNAL FACTORS:
    Work and family competing demands.
    Financial stress.
    Health issues.

  COURSE FACTORS:
    No accountability structure.
    No human interaction or support.
    Difficulty calibration (often too hard or too easy).
    Technology barriers in some regions.

  MOTIVATION FACTORS:
    Intrinsic motivation required for self-directed learning.
    Students accustomed to external accountability structure.
    "I'll do it later" bias (procrastination).

  STRUCTURAL FACTORS:
    No credential value for many employers.
    "Why finish if no one cares?"
```

### Improving Completion: What Works

```
  MOOC COMPLETION INTERVENTIONS
  ================================

  COHORT-BASED (instructor-led):
    Fixed schedule + classmates = accountability.
    Completion rates dramatically higher than self-paced.
    Trade-off: loses flexibility (main MOOC advantage).

  SMALL GROUPS / STUDY CIRCLES:
    Learners grouped with peers; mutual support.
    Weekly check-ins.
    Completion improvement: moderate.

  REMINDERS AND NUDGES:
    Email reminders.
    Progress tracking visible.
    "You're 40% done; others finished in X hours more."
    Small effect but scalable.

  PAID CERTIFICATES:
    Learners who pay for certificate: much higher completion.
    Financial commitment = commitment to completion.
    Coursera Specializations: better completion than free.

  AI COACHING:
    Personalized reminders based on predicted dropout risk.
    Early alert systems.
    Promising but still developing.
```

---

## Adaptive Learning Systems

Beyond MOOCs, the more durable EdTech contribution is adaptive learning -- systems that personalize content and pacing to individual learner trajectories.

```
  ADAPTIVE LEARNING ARCHITECTURE
  ================================

  KNOWLEDGE GRAPH:
    Learning content structured as directed acyclic graph (DAG).
    Nodes: concepts/skills.
    Edges: prerequisites (directed).
    Topological sort gives valid learning sequences.
    Multiple valid topological orderings = multiple valid curricula.

    +--------+     +--------+     +----------+
    |Fractions|---> |Ratios  |---> |Proportions|
    +--------+     +--------+     +----------+
        |
        v
    +--------+
    |Decimals|
    +--------+

    Navigation problem: given current mastery state (subset of
    nodes "known"), find the optimal next node to teach.
    This is a shortest-path problem on the prerequisite DAG,
    weighted by expected learning time per concept.

  MASTERY ESTIMATION:
    Bayesian Knowledge Tracing (BKT) is a Hidden Markov Model:
    - Hidden state: binary knowledge (knows / doesn't know)
    - Observable: correctness of responses (0/1)
    - Transition: P(L0) = prior; P(T) = learning rate
    - Emission: P(G) = guess rate; P(S) = slip rate

    Four parameters:
    P(L0) = prior probability student already knows skill
    P(T)  = probability of learning skill on each opportunity
    P(G)  = probability of correct response despite not knowing
    P(S)  = probability of incorrect response despite knowing

    State update (Bayesian posterior after observing response r):
    P(know | correct) = P(know) × (1 - P(S)) / P(correct)
    where P(correct) = P(know)(1-P(S)) + (1-P(know))P(G)

    This is exactly the forward algorithm for HMM filtering.
    Extensions (Deep Knowledge Tracing, 2015, Piech et al.)
    replace the HMM with an LSTM for richer state representation.

  ITEM SELECTION:
    Given mastery estimates:
    Choose next item from ZPD (not too easy, not too hard).
    Optimize for learning efficiency.

  EXAMPLE SYSTEMS:
    ALEKS: Math; knowledge space theory.
    Carnegie Learning: Cognitive Tutor; AI tutoring.
    Khan Academy exercises: mastery-based progression.
    Duolingo: spaced repetition + adaptive item selection.
    i-Ready: K-8 diagnostic + adaptive practice.
```

---

## Learning Management Systems (LMS)

```
  LMS LANDSCAPE
  ==============

  MAJOR PLATFORMS:
  +----------+---------------+------------------+
  | Canvas   | Instructure   | ~40% US higher ed|
  | (2011)   |               | clean UX; REST API|
  +----------+---------------+------------------+
  | Blackboard| Anthology    | Legacy dominant  |
  | (1997)   |               | complex; declining|
  +----------+---------------+------------------+
  | Moodle   | Open source   | Strong globally  |
  | (2002)   | community     | high customization|
  +----------+---------------+------------------+
  | Google   | Google        | K-12 dominant    |
  | Classroom| Workspace     | free; limited    |
  +----------+---------------+------------------+
  | Schoology| PowerSchool   | K-12 enterprise  |
  +----------+---------------+------------------+

  LMS FUNCTIONS:
    Content hosting (videos, PDFs, readings)
    Assignment submission + grading
    Gradebook
    Discussion forums
    Quizzing + testing
    Communication (announcements, messaging)
    Integration with external tools (via LTI standard)

  LIMITATION:
    LMS = content management, not learning management.
    Stores and delivers; doesn't optimize for learning.
    No adaptive capability in base LMS.
    Data: what happened (submission times, quiz scores)
    but not why or how to improve.
```

---

## COVID-19 and Emergency Remote Teaching

```
  COVID-19 EDUCATION IMPACT (March 2020)
  =========================================

  WHAT HAPPENED:
    ~1.6 billion students worldwide moved to remote learning.
    Timeline: days/weeks for systems that took decades to develop.
    "Emergency Remote Teaching" (ERT) ≠ planned online learning.

  OUTCOMES:
    Learning loss documented globally.
    NWEA, McKinsey research: 1-2 months math learning lost.
    Low-income students: 3-5 months learning loss.
    Students of color: greater loss (digital divide, home instability).
    Special needs students: greatest losses.

  SILVER LINING:
    Forced teacher professional development in technology.
    Accelerated hybrid/online infrastructure adoption.
    Exposed digital divide: federal/state investment in devices.
    Generated massive data on online learning at scale.

  ENROLLMENT IMPACT:
    Community colleges: largest enrollment drops (~10-15%).
    For-profits and online-only: enrollment surge.
    Traditional 4-year: initial drop; partial recovery.
    Graduate/professional: stable or growing.
```

---

## OPM: Online Program Management

```
  ONLINE PROGRAM MANAGEMENT (OPM)
  =================================

  MODEL:
    Universities contract with OPM companies to build
    and operate their online degree programs.
    OPM provides:
    - Technology infrastructure
    - Marketing and student recruitment
    - Instructional design
    - Student support services

    University provides: brand + faculty + accreditation.

    Revenue split: OPM takes 40-60% of tuition revenue.

  MAJOR PLAYERS:
    2U (merged with edX in 2021)
    Pearson Online
    Academic Partnerships
    Noodle Partners

  CONTROVERSY:
    Revenue share model: incentivizes enrollment over quality.
    Who is actually providing the education?
    "Third-party servicers" increasing regulatory scrutiny.
    2023: ED proposed regulations requiring disclosure.
    Consumer protection concern: is the "MIT" online program
    actually MIT, or a vendor?

  OPM MODEL DISRUPTION:
    Many universities reversing OPM relationships.
    Bringing online operations in-house.
    AI tools reducing cost of instructional design.
```

---

## Decision Cheat Sheet

| Question | Answer | Implication |
|----------|--------|-------------|
| Do MOOCs democratize education? | Partially; serve already-educated most | Not a substitute for access; supplement |
| What's the completion rate? | 3-15% for self-paced xMOOCs | Need accountability structures |
| Who completes? | Already-educated professionals | Not reaching most disadvantaged |
| What improves completion? | Cohorts, payment, reminders, coaching | Design accountability in |
| What does adaptive learning actually do? | Personalizes sequence and pacing using mastery estimation | Strong evidence for math especially |
| What is an LMS for? | Content delivery and management | Not sufficient for deep learning support |

---

## Common Confusion Points

**MOOC Completion Rate Doesn't Mean MOOC Is Useless**
The 5-10% completion rate sounds like failure. But 5,000 completers from 100,000 enrollees is more people than most university courses reach. And completers gain real skills. The problem is when MOOCs are positioned as a substitute for college access -- they're not.

**Online Learning ≠ MOOCs ≠ Adaptive Learning**
These are different things. Online learning: synchronous or asynchronous courses delivered over the internet. MOOCs: open-enrollment large-scale online courses (often asynchronous). Adaptive learning: systems that personalize content/pace based on individual mastery. They overlap but are not synonymous.

**COVID Remote Teaching ≠ Online Learning Quality**
The evidence of learning loss during COVID should not be interpreted as evidence that online learning doesn't work. Emergency Remote Teaching (ERT) with unprepared teachers, unsupported students, and inadequate technology is not equivalent to intentionally designed online learning. These are different conditions.

**AI Is Not Replacing Teachers; It Is Replacing Some Teacher Functions**
Khan Academy's Khanmigo, intelligent tutoring systems, AI feedback on writing -- these tools handle specific feedback and adaptive practice functions. They do not replace the relational, motivational, diagnostic, and institutional functions of teachers. The evidence on intelligent tutoring systems is actually quite strong for procedural skills (math, reading); the challenge is generalization to complex thinking.
