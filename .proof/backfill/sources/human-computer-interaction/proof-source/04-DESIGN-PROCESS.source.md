---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "04-DESIGN-PROCESS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-computer-interaction:design-process
kind: guide
module: human-computer-interaction
section: human-computer-interaction
title: The Design Process - Generating Interactive Systems as Hypotheses
status: source-custody
source_custody: partial
current_path: human-computer-interaction/04-DESIGN-PROCESS.md
canonical_path: human-computer-interaction/04-DESIGN-PROCESS.md
backsource_ids: [proof-backfill:human-computer-interaction:04-design-process]
concepts: [user-centered-design, double-diamond, design-thinking, personas, scenarios, prototyping-fidelity, design-systems]
root_concepts: [design-process]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# The Design Process — Generating Interactive Systems as Hypotheses

**This guide owns** the *generate* half of the design↔evaluate loop: human-centred / user-centred
design, the double diamond, design thinking, and the artifacts they produce — requirements,
personas, scenarios, prototypes at varying fidelity, and design systems. Its single organizing
claim is that **everything this process produces is a hypothesis, not a result.** **It builds on**
`06` (which supplies the user/context understanding a design responds to) and `02`/`03` (the models
and substrate a design is built from). **It explicitly defers**: *whether a design actually works*
— all confirmation — to `05-USABILITY-EVALUATION` (a design claim is unresolved until `05` tests
it); the *statistics* behind any confirming study to `statistics-applied/`; the *physical-product*
design process (industrial design, product form, materials) to `industrial-design/`; and *service/
organizational* fit to `09`.

> **This module is an educational reference on *how interactive systems are designed*. A design
> process that optimizes for a business metric at the user's expense is how dark patterns get built;
> metric selection is an ethical act (`11`), and this guide describes generating designs *for* users,
> never against them. Named frameworks and standards are attributed and dated; a framework is a
> scaffold, not a guarantee.**

*Per-guide banner: every artifact here — a persona, a scenario, a wireframe, a "clearer" flow — is a
**hypothesis about the user or the solution**, and stays **unresolved until an evaluation in `05`
confirms or fails it**. A design "validated" only by its own artifacts (a persona that proves the
persona, a demo that impresses stakeholders) is not validated. And **prototype fidelity must match
the question being asked**, or the prototype answers the wrong question.*

---

## The Big Picture: Design Is Structured Hypothesis Generation

The design process is not a pipeline that outputs a correct interface; it is a **disciplined way of
generating well-grounded hypotheses** and getting them to evaluation cheaply. It alternates
**divergence** (widen the option space) and **convergence** (commit), grounded in real user/context
understanding (`06`) and closed by evaluation (`05`).

```
  THE DESIGN <-> EVALUATE LOOP (this guide owns the GENERATE half)
  ------------------------------------------------------------------
   understand ----> frame ----> generate ----> prototype ----> [ EVALUATE ]
   context (06)     the problem  options        at fidelity      (guide 05)
        ^                                          matched to        |
        |                                          the question      |
        +---------------- iterate: the eval result updates ----------+
                          the hypothesis; then generate again
  ------------------------------------------------------------------
   Design PROPOSES; evaluation DISPOSES. Nothing between "understand" and
   "evaluate" is a fact yet -- it is the current best hypothesis.
```

Three canonical framings of this loop coexist; they are **scaffolds, attributed and dated, not
dogma**:

- **Human-centred design (HCD/UCD).** ISO **9241-210** (2010; rev. **2019**; successor to ISO 13407,
  1999) — an iterative cycle: *understand the context of use → specify requirements → produce design
  solutions → evaluate against requirements → iterate.* This is the formal, standards-grade statement
  of the loop.
- **The Double Diamond.** UK Design Council (**2005**) — *Discover, Define, Develop, Deliver*, two
  diamonds of divergence-then-convergence (explore the problem, then the solution).
- **Design thinking.** IDEO / Stanford d.school (popularized by Tim Brown, *HBR*, **2008**) —
  *empathize, define, ideate, prototype, test.*

They differ in vocabulary and emphasis, not in structure: all three **diverge then converge, ground
in users, and iterate through evaluation.**

**Bridge (software).** This is **hypothesis-driven development** with the human in the loop. A persona
is a **typed assumption about the caller**; a scenario is an **acceptance-test narrative**; a
prototype is a **spike** whose fidelity you choose to answer one question; the design system is a
**shared component library**. And the cardinal rule matches engineering: **a feature isn't "done"
because it compiles and demos** — it's done when it passes the test. Here the test lives in `05`.

---

## 1. Human-Centred Design — The Standards-Grade Loop

ISO 9241-210 codifies four iterative activities and six principles. The activities are the loop
above; the principles are the guardrails:

```
  ISO 9241-210 (2019) -- the SIX PRINCIPLES of human-centred design
  ------------------------------------------------------------------
   1. design is based on an explicit understanding of users, tasks, contexts
   2. users are involved throughout design and development
   3. design is driven and refined by USER-CENTRED EVALUATION (guide 05)
   4. the process is ITERATIVE
   5. the design addresses the WHOLE user experience
   6. the team has multidisciplinary skills and perspectives
  ------------------------------------------------------------------
   Principle 3 is the hinge: without user-centred evaluation, "human-centred
   design" is just assertion. That evaluation is guide 05's, not this guide's.
```

The applied consequence: HCD is **not** a warrant to declare a design good because it followed the
steps. The standard itself makes *evaluation* a principle, precisely because generating a design —
however empathetically — proves nothing on its own.

---

## 2. The Double Diamond and the Divergence/Convergence Rhythm

The double diamond's value is naming the **two distinct search problems** and the discipline of
separating them:

```
  THE DOUBLE DIAMOND (Design Council 2005)
  ------------------------------------------------------------------
     PROBLEM SPACE                    SOLUTION SPACE
     <  DISCOVER  >   DEFINE      <  DEVELOP  >   DELIVER
     diverge: explore  converge:   diverge: many   converge: build,
     the real problem  frame ONE   candidate        refine, ship (-> 05)
     (research, 06)    problem     solutions
  ------------------------------------------------------------------
   Failure mode: skipping the first diamond (solving the wrong, unexamined
   problem) or never diverging in the second (shipping the first idea).
   Each converge point is a COMMITMENT to a hypothesis, not a proof of it.
```

The most common process error the double diamond guards against: **jumping to a solution before the
problem is framed** (skipping the first diamond). Framing the wrong problem well still yields the
wrong product — which is why `06` (understanding) precedes generation, and why the first diamond is
explicitly *problem* work.

---

## 3. Design Thinking — Useful Scaffold, Honest Limits

Design thinking (empathize/define/ideate/prototype/test) popularized user empathy and rapid
prototyping in non-design organizations, which is its real contribution. Held honestly, it has
**limits worth stating** (a peer should not present it as a proven method): it is a *heuristic
scaffold*, its "empathize" step can produce shallow or projected understanding if it substitutes for
real research (`06`), and its cheerful framing can under-serve accessibility, ethics, and the users
who are hardest to "empathize with." Use it to *structure divergence and get to prototypes fast*;
do not treat completing its steps as evidence the design works — that is still `05`'s call.

---

## 4. Requirements, Personas, and Scenarios — Hypotheses with Names

The artifacts that carry the process are all **hypotheses**, and labeling them as such is the
discipline:

| Artifact | What it is | The hypothesis it encodes | How it fails |
|----------|-----------|---------------------------|--------------|
| **Requirement** | a stated need/constraint | "users need to do X in context C" | invented from the team's assumptions, not grounded in `06` |
| **Persona** (Cooper, *The Inmates Are Running the Asylum*, **1999**) | an archetype standing for a user segment | "this cluster of goals/abilities/contexts is real and matters" | a made-up persona that launders the team's biases as a "user" |
| **Scenario / user story** (Carroll, *Making Use*, **2000**) | a narrative of a user pursuing a goal | "this is a real path a real user takes" | a happy-path fiction that never meets a real workflow |
| **Job-to-be-done** | the progress a user is trying to make | "users 'hire' the product for this job" | confusing a feature you want to build for a job users have |

The load-bearing rule: **a persona is a hypothesis about *who*, a scenario is a hypothesis about
*what path*, and a requirement is a hypothesis about *what's needed*.** Grounded in `06` data, they
focus a team; **invented** from within, they become a mirror that reflects the team's assumptions
back as if they were users — the most seductive failure in the process, because the artifacts *feel*
like validation. They are not. Confirmation is `05`'s.

**A carried invariant (accessibility of the sample).** Personas and requirements that silently omit
disabled users, non-dominant-language users, and low-bandwidth/low-end-device users are **under-
specified for the population, not simpler** (`08`). Disabled users are a first-class segment in the
persona set, not a late "edge case."

---

## 5. Prototyping — Fidelity Is Chosen to Answer a Question

A prototype is **a question made tangible**, and its **fidelity must match the question** — the
core prototyping discipline (Buxton, *Sketching User Experiences*, **2007**).

```
  FIDELITY MATCHES THE QUESTION
  ------------------------------------------------------------------
   QUESTION                        RIGHT FIDELITY
   -----------------------------   ------------------------------------
   "is the CONCEPT/flow right?"    LOW-fi: paper, sketches, wireframes
                                   (cheap, fast, invites blunt critique)
   "is the LAYOUT/IA clear?"       MID-fi: greyscale wireframes, clickable
   "does the MICRO-INTERACTION     HIGH-fi: interactive, styled, real data
    / timing / feel work?"         (expensive; slow to change; over-commits)
   "does a HARD-to-build feature   WIZARD OF OZ: a human simulates the system
    even help before we build it?" behind the curtain (test value, not tech)
  ------------------------------------------------------------------
   Mismatch traps: HIGH fidelity too early -> people critique colors, not the
   idea, and the team over-commits to a direction it hasn't tested. LOW
   fidelity for a timing/feel question -> can't answer it at all.
```

Two disciplines make prototyping honest:

- **Match fidelity to the question.** High fidelity too early draws feedback about polish instead of
  concept and sinks sunk-cost into an unvalidated direction; low fidelity cannot answer a question
  about feel or timing. Pick the cheapest fidelity that can *fail* the hypothesis you're testing.
- **A prototype's job is to be *tested*, not admired.** A prototype that impresses a stakeholder has
  moved a **stakeholder** metric, not a **user** one. The prototype is the input to `05`, not a
  substitute for it (banner).

---

## 6. Design Systems — Making the Right Path the Default

A **design system** (component library + patterns + guidelines; lineage from Alexander's *A Pattern
Language*, **1977**, through platform Human Interface Guidelines and modern component libraries) is
the process's highest-leverage governance artifact. Its value for this module is specific:

- **Consistency lowers the learning tax.** Shared components mean an idiom learned once transfers
  everywhere (the `01` installed-base argument, used deliberately).
- **It makes accessibility the default (a `08` shift-left).** If the shared `Button`, `Input`, and
  `Dialog` carry correct semantics, focus behavior, contrast, and target sizes, product teams inherit
  the accessible path without re-deriving it — *the single highest-leverage accessibility move*
  (`08` §9). Fix `<button>` once, fix it everywhere.
- **It encodes decisions, not truths.** A design system is a **convergence artifact** — a library of
  committed hypotheses. It still must be evaluated (`05`), and it can calcify bad patterns library-
  wide if it isn't. Consistency is a means; usability and accessibility are the ends.

---

## A Worked Design Process (illustrative, fictional)

*Fictional, to show the artifacts staying explicitly unresolved until evaluation. No real product.*

**Problem.** *Ferry*, a fictional app for booking small-town ferry crossings. The team is told
"people find booking confusing."

- **First diamond (Discover/Define, grounded in `06`).** A field study (`06`) of actual travelers
  reframes the problem: the confusion is not the booking *form* but **not knowing whether a sailing
  will run in bad weather.** The reframed problem statement is a **hypothesis** ("the core job is
  trip-certainty, not form-filling") to be tested, not a conclusion.
- **Personas & scenarios as hypotheses.** Two grounded personas emerge — a daily commuter and an
  occasional tourist — *and* a first-class third: a low-vision traveler using a screen reader on a
  metered connection (accessibility as a segment, not an edge). Each persona is labeled a hypothesis
  about a real segment, sourced to the field data, not invented.
- **Divergent solutions + fidelity-matched prototypes.** For the concept question ("does a
  weather-first booking flow help?"), the team builds **paper prototypes** (low fidelity — cheap to
  reject). For the later question ("does the live-status micro-interaction read clearly?"), they build
  a **high-fidelity** interactive prototype. A hard-to-build "predict cancellations" idea is tested
  **Wizard-of-Oz** (a human posts statuses) to see if it helps *before* any model is built.
- **Design-system commitment.** The chosen components come from an accessible design system (native
  semantics, focus, contrast, 24×24 targets), so the accessible path is the default.

**Reading — and the honest stance.** At the end of this process the team has a **well-grounded
hypothesis**: a weather-first flow, two-plus personas, scenarios, and a tested-in-Oz feature. **None
of it is validated yet.** "The weather-first flow is clearer" is a claim that stays **unresolved
until `05`** runs a usability test (and any summative claim needs `statistics-applied/`). The
prototypes impressed the steering committee — a *stakeholder* signal, explicitly **not** evidence of
user success. The process did its job: it generated the right hypothesis cheaply and handed it to
evaluation. It did not, and cannot, declare victory on its own artifacts.

---

## Reader Tasks (answerable from this guide)

1. **Label the artifacts as hypotheses.** Given a persona, a "clearer" redesigned flow, and a
   requirement, state what each *claims* and that each remains unresolved until a `05` evaluation
   confirms it — then choose the **family** of evaluation you'd route it to: **inspection/analytic**
   (expert review, no users) vs **empirical/user-based** (observing real users), and **formative**
   (find-and-fix) vs **summative** (measure against a target). Choosing the family is answerable
   here; the specific method and its statistics are `05`'s.
2. **Match fidelity to the question.** Given "we need to know if users understand the new concept"
   vs "we need to know if the swipe-to-confirm feels right," choose paper vs high-fidelity prototypes
   and justify from the fidelity-matches-the-question rule.
3. **Catch a self-validating design.** Given "the persona we made proves users want this, and the
   demo wowed the execs," explain why neither is validation (invented artifact; stakeholder ≠ user
   metric) and what would actually validate it.
4. **Repair a skipped-first-diamond process.** Given a team that jumped straight to building a
   booking form, use the double diamond to show they may be solving an unexamined (wrong) problem,
   and route the fix through `06`.
5. **Use the design system as an accessibility lever.** Explain why baking correct semantics/focus/
   contrast/target-size into shared components (a `08` shift-left) beats per-screen accessibility
   fixes, and why the system still must be evaluated.

---

## Decision Cheat Sheet

| Situation | Do | Because (this guide) |
|-----------|----|--------------------|
| "we know the problem already" | run the **first diamond** anyway | you may be framing the wrong problem (§2) |
| starting a design | ground personas/scenarios in **`06`**, label them hypotheses | invented artifacts launder assumptions (§4) |
| testing a **concept** | **low-fi** prototype | cheap to reject; invites blunt critique (§5) |
| testing **feel/timing** | **high-fi** prototype | low-fi can't answer it (§5) |
| testing a **hard-to-build** idea's value | **Wizard of Oz** | test worth before cost (§5) |
| any "this design is better" claim | send it to **`05`** | design proposes; evaluation disposes (banner) |
| a summative "target met" claim | `05` + **`statistics-applied/`** | design/eval never own the statistics |
| accessibility across many screens | fix it in the **design system** | shift-left default beats per-screen patches (§6, `08`) |
| a stakeholder loved the demo | note it as a **stakeholder**, not user, signal | admiration ≠ evidence (worked case) |

---

## Common Confusion Points

**"We did user-centred design, so it's good."** No. HCD's own principles make **user-centred
evaluation** a requirement precisely because following the steps proves nothing. The design is a
hypothesis until `05` tests it (§1, banner).

**"The persona says users want this."** A persona is a **hypothesis about a segment**, valuable when
grounded in `06` and dangerous when invented — an invented persona reflects the team's assumptions
back as if they were a user. It doesn't validate anything (§4).

**"High-fidelity prototypes give better feedback."** Not for concept questions — high fidelity draws
critique about polish and over-commits the team before the idea is tested. Fidelity must match the
question (§5).

**"The stakeholders approved it, so we're aligned and done."** Stakeholder approval is a *stakeholder*
signal, not evidence users succeed. Those are different metrics; conflating them is how unvalidated
designs ship (worked case, `05`).

**"A design system guarantees good UX."** No. It guarantees **consistency** and can make the
accessible path the default (a real win), but it encodes committed *hypotheses* that still need
evaluation and can propagate a bad pattern everywhere. Consistency is a means, not the end (§6).

---

## Global, WEIRD, and Resource Caveats

- **"Empathy" and personas don't transport across cultures unexamined.** A design team's intuition
  about "the user" is shaped by its own (often WEIRD) context; personas and scenarios built without
  research *in the target context* mis-model users elsewhere. Ground generation in `06` data from the
  actual population, and treat cross-context transfer as a hypothesis, not a given.
- **Prototype fidelity interacts with resources and access.** High-fidelity, high-bandwidth
  prototypes can't even be tested by users on low-end devices or metered data, biasing the process
  toward the well-connected. Match fidelity to the **user's** context, not the studio's.
- **The two module invariants ride here.** *Accessibility of the sample:* disabled and non-dominant-
  language users are first-class **personas and segments**, and the accessible path is the design-
  system default (`08`), not a later remediation. *Safety/ethics floor:* the design process generates
  designs *for* users; a process tuned to extract a business metric against the user's interest is
  building a dark pattern (`11`), and where a design's failure could cause physical harm, the
  operator-safety analysis is `human-factors/`'s, not this guide's.
