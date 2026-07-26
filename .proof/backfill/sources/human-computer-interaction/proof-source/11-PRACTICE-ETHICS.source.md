---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "11-PRACTICE-ETHICS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-computer-interaction:practice-ethics
kind: guide
module: human-computer-interaction
section: human-computer-interaction
title: Practice and Ethics - The Profession and Its Refusals
status: source-custody
source_custody: partial
current_path: human-computer-interaction/11-PRACTICE-ETHICS.md
canonical_path: human-computer-interaction/11-PRACTICE-ETHICS.md
backsource_ids: [proof-backfill:human-computer-interaction:11-practice-ethics]
concepts: [professional-practice, design-critique, persuasive-design, dark-patterns, value-sensitive-design, sustainability, ethics]
root_concepts: [practice-ethics]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Practice and Ethics — The Profession and Its Refusals

**This guide owns** HCI as a **profession** and its **applied ethics of interaction**: teams and
roles, design critique, the ethics of influence (persuasion vs manipulation), dark/deceptive patterns
**as a recognize-and-refuse taxonomy**, value-sensitive design, sustainability, and the module's
ethics contract and the professional's **duty to avoid and disclose harm** (with the escalate-or-refuse
decision treated honestly as ethical judgment, not a guaranteed legal/professional right). **It builds on** the whole module (it
is where the safety/ethics floor named in `00` and demonstrated in `05`/`08` becomes a practice). **It
explicitly defers**: *moral philosophy and normative ethical theory* to `ethics/` and `philosophy/`;
*legal obligation and liability* to `law/`; *organizational/management theory* to
`organizational-behavior/`; and *the safety analysis* of high-consequence systems to `human-factors/`.

> **This module is an educational reference on *how to recognize and refuse* manipulative and harmful
> interaction design — **never a playbook for building it.** Deceptive/dark patterns and attention-
> engineering are described *only* so a professional can spot and reject them, in their own work and in
> what they are asked to build. **Any actionable manipulation, coercion, deception, or addiction
> recipe is out of scope.** This guide gives no legal ruling (that is `law/`) and no safety
> certification (that is `human-factors/`). Named frameworks are attributed and dated.**

*Per-guide banner: interaction ethics is evaluated against **value and harm**, never against a number
to maximize. "We moved the metric" is **not** a defense of a harmful design — the A/B-metric caveat of
`05` §7 generalized. A recommendation that optimizes a number which is the wrong thing to move fails
this guide's test.*

---

## The Big Picture: Two Faces — The Practice and the Refusal

Being an HCI professional is two things at once: a **practice** (working in teams, giving and taking
critique, shipping through a design process) and a set of **refusals** (the lines you will not cross,
even when a metric or a manager pushes). The organizing idea is that **a metric is an instrument, not
a goal** — the discipline that runs from `05` (a SUS is not usability) and `07` (an accurate chart can
still deceive) reaches its conclusion here: *what you choose to optimize is an ethical act.*

```
  HCI AS A PROFESSION -- practice + refusal
  ==================================================================
   THE PRACTICE                        THE REFUSAL (the ethics floor)
   ------------------------------      ------------------------------
   teams & roles (research, design,    no manipulation / dark-pattern
     content, engineering, PM)           playbook  (recognize & refuse)
   design critique (on the work,       no legal/compliance ruling (-> law/)
     not the person)                   no safety-certification (-> human-factors/)
   the design<->evaluate loop          research ethics is not an IRB substitute
     (guides 04, 05)                   standards/"laws" dated & bounded;
   value-sensitive design                conformance is a floor, not the goal
   sustainable practice                METRIC != GOAL: "we moved the number"
                                         is not a defense of harm
  ==================================================================
   The through-line: influence is unavoidable in design; the ethics is in
   WHOSE interest it serves. Persuasion helps users meet THEIR goals;
   manipulation serves the designer's goals AGAINST the user's.
```

**Bridge (software).** This is your **engineering code of conduct plus the design-review gate**, made
specific to interaction. Critique is **code review for designs**; value-sensitive design is a
**threat-model for human values** (who is affected, what could go wrong for them); the metric caveat is
**Goodhart's law** — "when a measure becomes a target, it ceases to be a good measure" — which you
already know breaks systems and here breaks users. And the refusal is the same professional line you
hold when asked to ship a known security hole because it "moves a number."

---

## 1. The Profession — Teams, Roles, and the T-Shaped Practitioner

Interactive systems are built by **multidisciplinary teams** (ISO 9241-210's own principle, `04`). The
common roles and their overlaps:

```
  ROLES AROUND AN INTERACTIVE PRODUCT (they overlap; titles vary)
  ------------------------------------------------------------------
   UX / DESIGN RESEARCH .. studies users & context (guide 06); owns evidence
   INTERACTION / UX DESIGN  designs behavior & flow (guides 02, 04)
   VISUAL / UI DESIGN .... form, layout, encoding (guides 03, 07)
   CONTENT / UX WRITING .. language, labels, information (guides 01, 07)
   ACCESSIBILITY SPECIALIST ensures reach across ability (guide 08)
   ENGINEERING ........... builds it; owns feasibility & implementation quality
   PRODUCT MANAGEMENT .... prioritizes; owns the metric choices (this guide!)
  ------------------------------------------------------------------
   "T-shaped": deep in one, literate across the rest. Accessibility and ethics
   are EVERYONE's, not one specialist's to be delegated and forgotten.
```

The professional norm worth stating: **accessibility and ethics are shared responsibilities**, not a
box checked by one specialist at the end. Delegating them to a single role and forgetting them is how
the `08` conformance-vs-usability gap and this guide's refusals get skipped.

---

## 2. Design Critique — A Practice, Not a Verdict

**Critique** is the disciplined review of design work — the design analog of code review. Done well it
is a *skill with rules*:

- **On the work, against goals — not on the person.** A critique evaluates the design against the
  stated user goals and evidence (`04`/`05`), not the designer's taste or identity. "This label lowers
  scent for the first-time-user goal" is critique; "you always over-design" is not.
- **Critique is not approval, and approval is not evidence.** A design surviving critique is a
  *stronger hypothesis*, not a validated one — validation is still `05`'s (the `04` discipline). And a
  stakeholder *liking* it is a stakeholder signal, not user evidence (`04` worked case).
- **Separate divergent and convergent modes.** Early critique widens options (is this the right
  problem/approach?); late critique converges (is this execution right?). Mixing them — nitpicking
  pixels on a concept sketch — is the common failure, the `04`/§5 fidelity mismatch in social form.

---

## 3. The Ethics of Influence — Persuasion vs Manipulation

Design **always** influences behavior (defaults, ordering, friction, salience all steer choices —
`02`, `07`). The ethics is not "avoid influence" (impossible) but **whose interest the influence
serves.** The field that named designed influence is **captology / persuasive technology** (B.J. Fogg,
concept **1998**; *Persuasive Technology*, **2003**).

```
  THE LINE (the single most important judgment in this guide)
  ------------------------------------------------------------------
   PERSUASION (legitimate) .... helps the user reach the user's OWN goal,
                                with informed, revocable choice
                                (e.g., a clear reminder for a goal they set)
   MANIPULATION (out of scope)  serves the DESIGNER's goal AGAINST the user's
                                interest, by deception, coercion, or exploiting
                                bias without the user's informed consent
  ------------------------------------------------------------------
   Test: if the user knew exactly what the design was doing and why, would they
   still consent? If disclosure would defeat it, it is manipulation. (A useful
   heuristic, not a legal test -- legality is law/'s.)
```

This "would they still consent if they knew?" heuristic (a publicity/transparency test) is how a
professional draws the line in practice. It is a *judgment aid*, not a legal standard.

---

## 4. Dark / Deceptive Patterns — A Taxonomy to Recognize and Refuse

**Dark patterns** (term coined by Harry Brignull, **2010**; now often "deceptive patterns"; empirical
taxonomy in Mathur et al., "Dark Patterns at Scale," **2019**) are interface choices that trick or
coerce users into acting against their own interest. This guide lists them **only so you can name,
catch, and refuse them** — in your own work and in what you're asked to build. **These are anti-
patterns to reject, not techniques to apply.**

```
  DECEPTIVE-PATTERN CATEGORIES -- RECOGNIZE AND REFUSE (never a how-to)
  ------------------------------------------------------------------
   SNEAKING ........... hiding/ delaying information the user would act on
                        (surprise costs, pre-checked add-ons)
   OBSTRUCTION ........ making a legitimate action needlessly hard
                        ("roach motel": easy to get in, hard to cancel)
   NAGGING ............ repeated interruption pressuring a choice
   FORCED ACTION ...... requiring an unrelated action to proceed
   INTERFACE INTERFERENCE  visual tricks that steer to the designer's choice
                        (confirm-shaming; a dimmed/ hidden decline option)
   URGENCY / SCARCITY .. false countdowns or "only 2 left" pressure
  ------------------------------------------------------------------
   HOW TO USE THIS LIST: as a CHECKLIST OF THINGS TO REJECT in design review.
   The refusal is the point. If a spec asks for one of these, it fails the
   ethics floor -- escalate/refuse (section 7), don't optimize it.
```

**Attention and "engagement" maximization** is the systemic version: optimizing time-on-app,
notifications, or infinite feeds for the *business's* engagement metric, not the user's wellbeing, is
the industrial-scale form of the persuasion→manipulation slide (the critique from the digital-
wellbeing / humane-technology movement). This is exactly where the **metric caveat** bites: an A/B test
(`05` §7) will happily validate a dark pattern because it *does* move the chosen number — which is why
**metric selection is an ethical act** and a guardrail (does this harm the user?) must gate it. "It
lifted conversion" is not a defense if the lift came from deception (banner).

*The strict boundary (the module's pillar 1):* this guide describes these patterns' **effects and how
to spot them**, never a step-by-step method to build them effectively. The deliverable is refusal, not
capability.

---

## 5. Value-Sensitive Design — Accounting for Human Values Throughout

**Value-Sensitive Design** (VSD; Batya Friedman and colleagues, **1996** onward; Friedman, Kahn &
Borning, 2006; Friedman & Hendry, 2019) is a principled method for building **human values** (privacy,
autonomy, fairness, dignity, inclusion) into design from the start, not auditing for them at the end.
Its practical machinery:

```
  VALUE-SENSITIVE DESIGN -- the tri-partite investigation
  ------------------------------------------------------------------
   CONCEPTUAL .... which values are at stake, and WHOSE? Identify DIRECT
                   stakeholders (users) AND INDIRECT stakeholders (people
                   affected but not using it -- the person being photographed,
                   the community being policed by the data)
   EMPIRICAL ..... how do stakeholders actually experience those values?
                   (guide 06 methods)
   TECHNICAL ..... how do design choices support or undermine the values?
  ------------------------------------------------------------------
   Key move: INDIRECT stakeholders. Bias in computer systems (Friedman &
   Nissenbaum 1996) and harms often land on people who never opted in.
   VALUE TENSIONS (privacy vs safety, autonomy vs simplicity) are named and
   negotiated, not silently resolved in the business's favor.
```

The load-bearing contributions: **indirect stakeholders** (the affected non-users) and **value
tensions** made explicit. A design that serves its users while harming bystanders (a doorbell camera's
neighbors, a data system's surveilled community) has an ethics problem VSD is built to surface.

---

## 6. Sustainability — Environmental and Human

Interaction design has **material and human sustainability** stakes the profession increasingly owns:

- **Environmental (sustainable interaction design; Blevis, **2007**).** Digital products consume energy
  and drive hardware turnover; design choices affect data transfer (energy), device lifetime (e-waste,
  the "upgrade or die" pattern), and default behaviors (auto-playing 4K video by default has a carbon
  cost). Lightweight, durable, low-default-consumption design is a sustainability *and* an inclusion
  win (the low-bandwidth argument of `08` §8).
- **Human sustainability (digital wellbeing).** Designs that respect attention, allow disengagement,
  and don't manufacture compulsion treat the user's time and mental health as values, not resources to
  extract (§4). This is the constructive counterpart to attention maximization.

**A worked microcase (illustrative, fictional).** *Loop*, a fictional video app, defaults to
**auto-play 4K on cellular**. The metric case for it is watch time; the sustainability case against
it is concrete — 4K-on-cellular maximizes **data transfer (energy)** and silently burns the data
budgets of metered/low-bandwidth users (the `08` §8 inclusion argument) for a quality most can't
perceive on a phone. The professional move is not a lecture but a **default**: ship **auto-play off
(or capped resolution) on cellular**, an *unchecked* "HD on Wi-Fi" opt-in, and a visible data
indicator. The environmental win (less transfer, less device strain) and the inclusion win
(metered/older-device users) are the **same** default — and "watch time dropped" is the honest
baseline, not a reason to revert (the metric-is-not-the-goal rule, §4).

Sustainability is included here because it is where "what should we optimize?" extends beyond the
individual user to the planet and to society — the widest form of the metric-is-not-the-goal argument.

---

## 7. The Ethics Contract and Professional Refusal

The module's five pillars (`00`), restated as a **professional's operating contract**, plus the act
that enforces them — **refusal**:

1. **No manipulation / dark-pattern playbook** — recognize and refuse (§3–4).
2. **No legal / compliance ruling** — name the landscape, route obligation to `law/` (`08`).
3. **No safety-certification** — own the interaction method; route operator-safety to `human-factors/`.
4. **Research ethics as principle, not an IRB substitute** (`06`, `08`).
5. **Standards/"laws" dated and bounded; conformance is a floor, not the goal.**

Professional codes formalize the **duties**, not a protection: the **ACM Code of Ethics and
Professional Conduct** (**2018**) obliges computing professionals to **avoid harm**, **be honest and
disclose** (not conceal) risks, **respect privacy**, **be fair**, and — as its General Principles put
it — hold the **public good** as the paramount consideration. What the Code establishes are **ethical
duties**; it does **not** grant an express **legal or professional *right* to refuse** (a protection
from being reassigned, disciplined, or dismissed). Keep three things distinct:

- **The Code's duties** — avoid and *disclose* harm, prioritize the public good — are ethical
  obligations the profession asserts.
- **Whether refusing is *protected*** — declining the work without penalty — is a matter of
  **organizational** policy, your **contract**, and **the law** (whistleblower statutes, labor
  law): that is `law/`'s and `organizational-behavior/`'s domain, not the Code's and not this
  guide's.
- **The decision to refuse** is finally an **individual ethical judgment** the Code *informs* but
  does not license as a guaranteed right. Escalating rather than silently complying is the
  professional norm the duties point to; what that costs you, and what shields you, is the separate
  protection question above.

---

## A Worked Ethics Decision (illustrative, fictional)

*Fictional, to show "we moved the number" refused on value/harm grounds. No real product.*

**Situation.** *Streamly*, a fictional media app. Growth asks design to make **cancellation** flow
through five screens with a confirm-shaming prompt ("Are you sure? You'll lose your memories"), and to
add a **pre-checked** "resubscribe automatically" box. An A/B test shows the change **cuts cancellations
12%** — a clear, tight metric win at scale (`05` §7 says the number is real).

- **Recognize (§4).** This is **obstruction** ("roach motel" — easy to subscribe, hard to cancel),
  **interface interference** (confirm-shaming), and **sneaking** (pre-checked opt-in). It is a
  deceptive-pattern stack, named from the checklist.
- **The metric defense, refused (banner, §4).** "It moved retention 12%" is **not** a defense: the lift
  came from making a legitimate action (canceling) harder and from a pre-checked deception. The A/B test
  validated a **dark pattern** — exactly the failure mode where "we moved the number" is offered as
  cover. Metric selection is an ethical act; retention-at-the-cost-of-deception is the wrong number to
  optimize.
- **Value-sensitive reframe (§5).** Direct stakeholders (users) lose **autonomy**; the **value tension**
  (business retention vs user autonomy) is named, not silently resolved for the business. A legitimate
  redesign persuades within the user's own interest — a clear one-step cancel, an *unchecked* pause
  option honestly offered — and if that lowers retention, that is the honest baseline, not a failure to
  fix by trickery.
- **The refusal (§7).** The professional escalates and declines to build the confirm-shame/pre-check
  stack, citing the ethics floor (pillar 1) and the ACM Code (2018) duty to avoid harm. Whether it is
  also *illegal* (some jurisdictions restrict exactly these patterns) is routed to `law/`; whether it is
  *unethical* is answered here: yes.

**Reading.** The metric was real and refused; the patterns were named from the recognition taxonomy;
the harm was analyzed with VSD; and the outcome was a **refusal and an honest redesign**, not an
optimization. That is the guide's discipline: evaluate against value and harm, never "did the number
move."

---

## Reader Tasks (answerable from this guide)

1. **Draw the persuasion/manipulation line and refuse deceptive patterns.** Contrast a reminder for
   a user-set goal with a pre-checked add-on, then analyze a cancellation flow with confirm-shaming
   and a hidden decline button. Classify the patterns and state the professional response
   (escalation/refusal and honest redesign), never how to tune the deception.
2. **Rebut a metric defense.** Given "our A/B test proved the change is good because retention rose,"
   explain why a moved metric is not a defense when the lift came from deception, invoking metric
   selection as an ethical act (`05` §7).
3. **Run a mini value-sensitive analysis.** For a neighborhood doorbell camera, identify direct and
   **indirect** stakeholders and one value tension (safety vs bystander privacy), and how you'd surface
   it rather than resolve it silently.
4. **Exercise professional judgment without inventing protection.** Rewrite "this design is bad"
   into an evidence-and-goal-based critique and state why surviving critique is not validation
   (`05`). Then correct "the ACM Code says I can refuse, so I'm protected": the Code establishes
   duties to avoid/disclose harm and prioritize public good, while contractual or legal protection
   belongs to `law/` and organizational mechanisms.
5. **Make a sustainability default call.** Given "auto-play 4K on cellular by default lifts watch
   time," name the environmental cost (data transfer/energy, device turnover) and the inclusion cost
   (metered/low-bandwidth users, `08` §8), give the honest default (off/capped on cellular, an
   *unchecked* HD opt-in), and say why "watch time dropped" is a baseline, not a reason to revert
   (§6, §4).

---

## Decision Cheat Sheet

| Situation | Do | Because (this guide) |
|-----------|----|--------------------|
| a design influences behavior | ask **whose interest** it serves | persuasion helps the user's goal; manipulation serves the designer's (§3) |
| deciding if influence is ethical | apply **would-they-consent-if-they-knew** | if disclosure defeats it, it's manipulation (§3) |
| a spec asks for a deceptive pattern | **recognize it, refuse it, redesign honestly** | dark patterns fail the ethics floor (§4, §7) |
| "the A/B test proved it works" | ask **what number, and is it the right one** | a metric can validate a dark pattern (§4, `05`) |
| harms may land on non-users | run **VSD**: name **indirect** stakeholders | harm often lands on people who didn't opt in (§5) |
| choosing defaults / friction / salience | treat the choice as an **ethical** one | defaults steer; metric ≠ goal (§4) |
| choosing a data-heavy default (autoplay, sync, resolution) | pick the **low-consumption default**; make heavy use an *unchecked* opt-in | environmental + inclusion win is the same default; metric ≠ goal (§6) |
| giving feedback on a design | critique **the work vs goals**, not the person | critique is a practice, not a verdict (§2) |
| asked to build a known harm | **escalate**; cite the ACM Code (2018) **duty** to avoid/disclose harm; declining is your ethical judgment | the Code sets a **duty** to avoid harm, not a guaranteed **right** to refuse; protection is `law/`/org (§7) |
| "are we legally allowed?" | route to **`law/`** | this guide answers *unethical*, not *illegal* (§7) |
| a safety-critical failure risk | route to **`human-factors/`** | this guide owns interaction ethics, not certification (§7) |

---

## Common Confusion Points

**"All persuasion is manipulation / all influence is unethical."** No. Design *always* influences
(defaults, order, friction). The ethics is **whose interest** it serves: helping users meet their *own*
goals with informed, revocable choice is legitimate; serving the designer's goal *against* the user's by
deception or coercion is manipulation (§3).

**"The A/B test proved the design is good."** It proved the design **moved the chosen metric** — which a
dark pattern also does. A moved number is not a defense of harm; **what** you chose to optimize is the
ethical question (§4, banner, `05` §7).

**"Dark patterns are just aggressive optimization."** No. They are choices that trick or coerce users
against their own interest, and they fail the ethics floor. This guide lists them to **refuse** them,
not to tune them (§4).

**"Ethics/accessibility is the specialist's job."** No. They are **everyone's** responsibility across
the team; delegating and forgetting them is how harms and the `08` conformance-vs-usability gap ship
(§1).

**"If it's legal, it's ethical."** No. Legality (`law/`) and ethics are different axes: a pattern can be
legal and still be a harm this guide refuses, or unethical in a place where it isn't yet regulated. This
guide answers *unethical*, not *illegal* (§7).

**"The ACM Code gives me the right to refuse."** Not as a protection. The Code (2018) establishes
ethical **duties** — avoid harm, **disclose** rather than conceal, hold the public good paramount — and
the decision to decline a harmful build is your **ethical judgment** informed by them. Whether that
refusal is *protected* from penalty (reassignment, discipline, dismissal) is set by your
**organization, your contract, and the law** (whistleblower statutes), not by the Code — route that
question to `law/` (§7).

**"Value-sensitive design is just a values checklist."** No. Its distinctive moves are **indirect
stakeholders** (affected non-users) and **naming value tensions** to negotiate them openly, rather than
silently resolving them in the business's favor (§5).

---

## Global, WEIRD, and Resource Caveats

- **Values are situated; "whose values?" is the first question.** Autonomy, privacy, dignity, and
  community are weighted differently across cultures and power structures, and VSD has been critiqued
  for whose values it centers. A professional imports values *with* the affected community (`08` §7
  co-design), not from a WEIRD default — and names the tension when values conflict rather than picking
  for people.
- **Harm and manipulation land hardest on the least powerful.** Deceptive patterns, attention
  extraction, and surveillance fall most heavily on low-income, low-literacy, disabled, and gig/precarious
  users who can least contest them; the attention economy is global, but its costs are unevenly
  distributed. The refusal (§7) matters most exactly there.
- **The carried invariants are this guide's whole point, at module scale.** *Accessibility* is an
  ethical baseline, not a feature — excluding disabled users is a harm (`08`). *The safety/ethics floor*
  is the module's spine: no manipulation playbook, no legal ruling (`law/`), no safety certification
  (`human-factors/`), research ethics as principle not permission (`06`), and **metric is never the
  goal**. This guide is where the floor becomes a professional practice — and a refusal.
