---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "07-AUTOMATION-HUMAN-MACHINE.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-factors:automation-human-machine
kind: guide
module: human-factors
section: human-factors
title: Automation & Human-Machine - Levels, the Ironies, and Function Allocation
status: source-custody
source_custody: partial
current_path: human-factors/07-AUTOMATION-HUMAN-MACHINE.md
canonical_path: human-factors/07-AUTOMATION-HUMAN-MACHINE.md
backsource_ids: [mdloom-backfill:human-factors:07-automation-human-machine]
concepts: [levels-of-automation, function-allocation, ironies-of-automation, trust-in-automation, automation-bias, out-of-the-loop, human-autonomy-teaming]
root_concepts: [automation-human-machine]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Automation & Human–Machine — Levels, the Ironies, and Function Allocation

**This guide owns** the *human-factors view of automation*: the **levels and types of
automation** (Sheridan & Verplank; the Parasuraman–Sheridan–Wickens four-stage model), the
**ironies of automation** (Bainbridge) that make higher automation a *trade*, not a free win,
the psychology of **trust, complacency, and automation bias**, the **out-of-the-loop (OOTL)**
performance problem, and **function allocation** — from the 1951 Fitts list to dynamic
human–autonomy teaming. **It builds on**
[`03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS`](03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md)
(automation is a workload/SA intervention) and
[`06-DISPLAY-CONTROL-INTERFACE-DESIGN`](06-DISPLAY-CONTROL-INTERFACE-DESIGN.md) (mode/state
visibility is how automation stays legible), and feeds
[`08-SAFETY-SYSTEMS-AND-HAZARD-ANALYSIS`](08-SAFETY-SYSTEMS-AND-HAZARD-ANALYSIS.md) (automation
introduces new failure modes to analyze). **It explicitly defers**: the **domain automation
systems themselves** — flight automation / FMS / autopilot to
[`aeronautics/04-AVIONICS`](../aeronautics/04-AVIONICS.md), vehicle autonomy and the SAE J3016
driving-automation levels to
[`transportation/07`](../transportation/07-AUTONOMOUS-VEHICLES.md), reactor control systems to
[`nuclear/05`](../nuclear/05-SAFETY-SYSTEMS.md) — to their owners; the **control-theory and AI**
that build automation to `control-theory/`, `robotics/`, and `ai-engineering/`; and the
**cognitive mechanism** of attention/trust to
[`cognitive-science/`](../cognitive-science/00-OVERVIEW.md).

> **Safety & ethics contract (binds every human-factors guide).** This is an **educational
> systems reference**. Nothing here tells anyone how to operate, tune, or certify an automated
> system, rules an automation-related accident, or declares an automation level "safe." Levels
> of automation are a **design vocabulary**, not a safety ladder where "higher is safer";
> **acceptance of any automation design belongs to the accountable domain organization and its
> regulator**, never to this module.

*Per-guide banner: automation is never *pure* workload reduction. Every increase in automation
**changes the operator's task** — usually from doing to monitoring — and **introduces new
failure modes** (mode error, complacency, OOTL, skill decay). Treat each level as a trade with a
named cost, not a free improvement.*

---

## The Big Picture: Automation Is a Trade, Not a Subtraction

The naïve model of automation is *subtraction*: give the machine a task, the human's workload
drops, done. The human-factors model is a **trade**: automation reshapes the human's job into
**monitoring and exception-handling** — the two things humans are *worst* at — and shifts the
hard work to the moments automation fails. Two frameworks organize the field: **what** and **how
much** is automated (levels/types), and **what that does to the human** (the ironies).

```
AUTOMATION AS A TRADE  (the two frameworks this guide owns)
================================================================================
   FRAMEWORK 1 -- LEVELS & TYPES (what/how much)     FRAMEWORK 2 -- THE IRONIES (so what)
   ------------------------------------------        ---------------------------------------
   Sheridan-Verplank: 10 levels, human->full auto    Bainbridge (1983): automating the EASY
   Parasuraman-Sheridan-Wickens (2000): 4 STAGES     parts leaves the human the HARD parts;
      1 information acquisition                       the human must MONITOR (bad at it),
      2 information analysis                          take over in the WORST moments, with
      3 decision selection                           DECAYED skills and lost SA.
      4 action implementation                         => higher automation TRADES routine
   each stage automatable to a DEGREE (a level)          load for rare-event fragility.
================================================================================
   Read together: choose a LEVEL for each STAGE (a design point in a grid), then pay the
   IRONY TAX -- monitoring load, complacency, OOTL, skill decay -- with eyes open. There is
   no level that is "just better"; there is a level appropriate to the failure rate and the
   difficulty of human takeover.
```

The single most important claim: **the relationship between automation level and safety is not
monotonic.** Higher automation reliably improves *routine* performance and *lowers routine
workload*, but reliably *worsens* failure-state performance, situation awareness, and takeover —
so the right level depends on **how often the situation goes off-normal (needing the human to
carry the load) and how hard that takeover is**.

---

## 1. Levels and Types of Automation

- **Sheridan & Verplank (1978)** proposed a **10-level scale** from fully manual (level 1),
  through the computer *suggesting* options and *executing with approval*, to the computer acting
  autonomously and *optionally* informing the human (level 10). It made "automation" a *continuum*
  rather than an on/off choice.
- **Parasuraman, Sheridan & Wickens (2000)** added the decisive refinement: automation applies to
  **four information-processing stages** — *acquisition, analysis, decision, action* — and **each
  stage can sit at a different level**. This turns automation design into choosing a **point in a
  stage × level grid**, and it predicts *where* the ironies bite: automating **decision** and
  **analysis** (stages 2–3) tends to cost the most SA, because the human loses the *reasoning*, not
  just the *doing*.

```
THE STAGE x LEVEL DESIGN SPACE  (Parasuraman-Sheridan-Wickens, 2000)
--------------------------------------------------------------------------------
   stage \ level   LOW automation ................ HIGH automation
   1 ACQUISITION   human scans          -> sensors filter/cue attention
   2 ANALYSIS      human integrates     -> system fuses & predicts (trend, projection)
   3 DECISION      human decides        -> system recommends -> system decides
   4 ACTION        human executes       -> system executes on approval -> fully autonomous
   -----------------------------------------------------------------------------
   KEY: pick a level PER STAGE. Automating stages 2-3 (analysis/decision) buys the most
   routine relief but costs the most SA and OOTL -- the human loses the PICTURE, and is
   worst placed to retake control. Automating stage 1 or 4 is usually cheaper in SA.
```

---

## 2. The Ironies of Automation (Bainbridge, 1983)

Lisanne Bainbridge's four-page paper is the field's most-cited argument and the reason "higher
is safer" is false:

```
THE IRONIES  (Bainbridge 1983 -- why automation creates the problems it is meant to solve)
--------------------------------------------------------------------------------
   IRONY 1  The designer automates what is EASY to automate and leaves the human the
            parts that are HARD -- so the human's residual job is harder, not easier.
   IRONY 2  The human is asked to MONITOR the automation for rare failures -- but humans
            are poor sustained monitors (the vigilance decrement, guide 03).
   IRONY 3  The human must TAKE OVER when the automation fails -- i.e., in exactly the
            abnormal, high-workload, low-time situations that are hardest to handle.
   IRONY 4  Skills DECAY without practice (deskilling), so the human who must take over
            is LESS practiced than before automation existed.
   -----------------------------------------------------------------------------
   Corollary (the "substitution myth", Christoffersen & Woods): automation does not
   simply SUBSTITUTE for the human -- it TRANSFORMS the task, creating new coordination,
   monitoring, and mode-tracking demands.
```

These are not arguments *against* automation; they are the **costs to design against** — through
better feedback (`06`), practice regimes, and keeping the human meaningfully in the loop.

---

## 3. Trust, Complacency, and Automation Bias

Automation only helps if the operator's **reliance is calibrated** to the automation's actual
reliability (Lee & See, "Trust in Automation," **2004**).

```
CALIBRATED RELIANCE  (Lee & See 2004; the two miscalibrations both hurt)
--------------------------------------------------------------------------------
   OVER-TRUST (misuse)     rely when you should not -> COMPLACENCY (under-monitor) and
                           AUTOMATION BIAS: commission (follow a wrong automated cue) and
                           omission (miss an event the automation didn't flag)
   UNDER-TRUST (disuse)    reject good automation -> lose its benefit, add workload,
                           sometimes disable it entirely
   CALIBRATION goal        reliance MATCHES reliability, per situation and per function
   -----------------------------------------------------------------------------
   Trust tracks PERCEIVED reliability; a few salient failures crater it, and a long clean
   run inflates it. Design for calibration: show the automation's CONFIDENCE and LIMITS,
   make its state and MODE continuously visible (guide 06), and avoid "cry wolf" (guide 05/06).
```

**Automation bias** is the specific error of treating an automated cue as a **heuristic
replacement for vigilance** — accepting a wrong recommendation (commission) or failing to act
because the automation stayed silent (omission). It rises when workload is high and when the
automation is usually right — the worst combination for the rare case when it is wrong.

---

## 4. Out-of-the-Loop and the Takeover Problem

When automation handles a process, the human goes **out-of-the-loop (OOTL)**: manual skills
decay, and — critically — **situation awareness degrades**, because SA is partly built by
*actively doing* the task (guide `03`). The result is the **automation conundrum** (Endsley): the
more the automation does, the less the operator understands the situation, yet the more the
operator is needed exactly when the automation reaches its limit. Takeover then demands
*rebuilding SA under time pressure* — the hardest possible cognitive task.

Mitigations are all **partial**: keep the human doing *something* meaningful (avoid pure
monitoring), make the automation's reasoning and mode **legible** (`06`; state/mode on **≥2**
coding channels, never one indicator alone), stage transitions with warning, and design for a
*graceful*, not abrupt, handback.

---

## 5. Function Allocation — From the Fitts List to Human–Autonomy Teaming

*Who does what* is the **function-allocation** problem.

- **MABA-MABA (the Fitts list, 1951; guide `01`).** The classic static split — "Men-Are-Better-At
  / Machines-Are-Better-At." Still the reference point, but critiqued (Dekker & Woods, "MABA-MABA
  or Abracadabra?") as too static: it treats capabilities as fixed and ignores that automation
  *transforms* the joint task rather than slicing it.
- **Dynamic / adaptive automation.** Allocate *by situation* — shift functions to automation under
  high workload, back to the human when spare capacity returns — which helps load but adds its own
  mode-tracking and authority-transition hazards.
- **Human–autonomy teaming (HAT).** Frame the automation as a **team member** requiring
  *observability, directability, and predictability* — the human must be able to see what it is
  doing, tell it what to do, and anticipate it. This is the modern reframing of the allocation
  question from "divide the tasks" to "design the coordination."

---

## The Boundaries (ownership in one place)

```
WHO OWNS WHAT AROUND AUTOMATION
--------------------------------------------------------------------------------
   this guide (07)     the HUMAN-FACTORS trade: levels/types, the ironies, trust/bias,
                       OOTL, function allocation, human-autonomy teaming
   aeronautics/04      the flight-automation SYSTEMS (FMS, autopilot, envelope protection)
   transportation/07   vehicle autonomy and the SAE J3016 DRIVING-AUTOMATION levels
   nuclear/05          reactor control & protection systems
   control-theory/ robotics/ ai-engineering/  how automation is BUILT
   06 (interface)      mode/state VISIBILITY that keeps automation legible
   03 (workload/SA)    the vigilance/SA science the ironies rest on
   08 (hazard)         analyzing the NEW failure modes automation adds
   -----------------------------------------------------------------------------
   Rule: this guide reasons about the human-automation RELATIONSHIP and its trade-offs;
   it does not design, tune, or certify any domain automation system, and it never treats
   "more automation" as automatically "more safe."
```

Note the **two different "levels" vocabularies**: this guide's LOA (Sheridan; PSW) is a
*human-factors* design continuum; the **SAE J3016 driving-automation levels 0–5** are a
*domain* taxonomy owned by `transportation/07`. They are related but not the same scale — do not
conflate them.

---

## A Worked Allocation Pass — Scoring a Stage's Level on the Trade (reproducible)

*All scores are **synthetic**, chosen so the arithmetic is reproducible. It demonstrates the
LOA *trade-off*, not a recommendation for any real system, and it certifies nothing.*

**The task (synthetic).** Automate the **decision** stage (stage 3) of a monitoring job at one of
four levels L1–L4. Assign synthetic 0–10 scores: **routine workload** (lower is better, falls
with automation), and the **conditional cost of an off-normal** (higher is worse, rises with
automation because SA and skill erode). Combine them using a **common off-normal-scenario
probability `p`** — the same for every level:

```
SYNTHETIC ALLOCATION SCORES  (0-10; the TRADE made explicit)
--------------------------------------------------------------------------------
   level                  routine workload   off-normal CONDITIONAL cost   (SA retained)
                              W(L)               C(L)  [given an off-normal]
   L1 human decides            8                   3   (in the loop: NO takeover)   high
   L2 system recommends        5                  12   (mostly in loop)             good
   L3 system decides,          3                  30   (approval bias; weak SA)     weak
      human approves
   L4 fully autonomous         1                  60   (OOTL: rebuild SA, decayed)  poor
   -----------------------------------------------------------------------------
   Expected-cost model:  E(L) = (1 - p) * W(L)  +  p * C(L)
      p    = COMMON off-normal-scenario probability -- a property of the WORLD, the SAME
             for every level. It is how often an abnormal situation ARISES, not how often
             "the automation fails."
      C(L) = LEVEL-SPECIFIC conditional cost GIVEN an off-normal. It rises with automation
             because OOTL + skill decay + SA-rebuild make human takeover worse.
      L1 carries NO takeover-failure term: the human never left the loop, so C(L1) is just
      the modest cost of handling an abnormal while already engaged -- not a takeover penalty.
```

**Sweep the common off-normal-scenario probability `p` (lower E is "better" in this synthetic
model). Watch the optimum SLIDE — the model crowns no winner:**

```
E(L) = (1 - p) * W(L) + p * C(L)      W = [8,5,3,1]   C = [3,12,30,60]
--------------------------------------------------------------------------------
   p = 0.01 (off-normal very rare):
      E(L1)=.99*8 +.01*3  = 7.95   E(L3)=.99*3 +.01*30 = 3.27
      E(L2)=.99*5 +.01*12 = 5.07   E(L4)=.99*1 +.01*60 = 1.59   -> L4 lowest
   p = 0.08 (occasional off-normal):
      E(L1)=.92*8 +.08*3  = 7.60   E(L3)=.92*3 +.08*30 = 5.16
      E(L2)=.92*5 +.08*12 = 5.56   E(L4)=.92*1 +.08*60 = 5.72   -> L3 lowest
   p = 0.15 (frequent off-normal):
      E(L1)=.85*8 +.15*3  = 7.25   E(L3)=.85*3 +.15*30 = 7.05
      E(L2)=.85*5 +.15*12 = 6.05   E(L4)=.85*1 +.15*60 = 9.85   -> L2 lowest
   p = 0.30 (off-normal dominates):
      E(L1)=.70*8 +.30*3  = 6.50   E(L3)=.70*3 +.30*30 = 11.10
      E(L2)=.70*5 +.30*12 = 7.10   E(L4)=.70*1 +.30*60 = 18.70  -> L1 lowest
   -----------------------------------------------------------------------------
   Reading: the optimum SLIDES L4 -> L3 -> L2 -> L1 as off-normals grow more common.
   EVERY level is best for SOME p, so this synthetic crowns NO winner -- it only prices the
   TRADE. This is Bainbridge quantified: high LOA is great UNTIL off-normals (where the
   human must carry the load with decayed skill and lost SA) get frequent enough to matter.
```

**Uncertainty / validity / bias note.** (1) The scores and the cost model are **synthetic and
illustrative** — the *shape* (routine benefit up, off-normal conditional cost up, with a
`p`-dependent optimum that **slides across levels**) is the real, repeatedly-observed pattern
(higher LOA improves routine performance but degrades failure-state performance and SA), but the
specific numbers are not an empirical dataset and the model crowns **no** level. (2) `p` (the
**common** off-normal-scenario rate) and the **level-specific** `C(L)` (how costly an off-normal
is *given* the level) are **the hard unknowns**, usually estimated with wide uncertainty — the
decision is *sensitive* to them. (3) `C(L1)` deliberately carries **no takeover term** (the human
never leaves the loop); the model also omits deskilling *dynamics* (`C(L)` at higher levels worsens
over months as skills decay) and trust miscalibration — real designs must add them. (4) This is a
**conceptual trade analysis**, not an automation-level recommendation, a winner, or a safety case
for any system.

---

## A Fully Worked Case — Choosing an Automation Level (illustrative, fictional)

*Fictional. It demonstrates the LOA trade — not a design, tuning, or certification of any real
automated system.*

**Setting.** *Fictional* **Halden Sorting** wants to automate anomaly-handling on a parcel line.
Two proposals: **L4** "the system diagnoses and diverts autonomously, informing the operator
after," or **L2** "the system flags and recommends; the operator approves." Human factors frames
the choice:

1. **Split by stage (§1).** Acquisition and action can sit high (sensors cue, actuators divert)
   cheaply; the contested stage is **decision** — automating it buys the most relief but costs the
   most SA (§1 grid).
2. **Price the ironies (§2).** Under L4, the operator becomes a **monitor** (irony 2), will be
   asked to intervene only when the system is **confused** (irony 3), and will have **decayed**
   the diagnostic skill (irony 4). The routine-workload win is real; so is the rare-event
   fragility.
3. **Estimate the off-normal rate and the level-specific conditional costs, honestly wide
   (§Worked pass).** How often does the line hit an off-normal the operator must resolve (`p`, the
   **same** for every level), and how costly is that off-normal *given each level's* automation
   (`C(L)` — low if the operator is in the loop, high if OOTL)? If off-normals are *rare*, L4's
   expected cost is lowest; as they grow *more frequent*, the optimum **slides down** the ladder
   (L4 → L3 → L2 → L1) — no level is "the answer," only the trade.
4. **Design for calibration and legibility (§3–4).** Whatever the level, the automation shows its
   **confidence and limits**, its **mode/state stays continuously visible on ≥2 channels** (`06`),
   and transitions are **staged with warning** — to fight complacency, automation bias, and abrupt
   OOTL handback.
5. **Hold the boundaries.** The **sorter/robotics system** is `robotics/`'s and the plant's; the
   **new failure modes** (mode confusion, silent mis-diverts) route to `08`; and **which level is
   adopted** is Halden's and any regulator's decision, informed by this trade — no module picks the
   level or certifies it.

**Reading.** The level is chosen by pricing the trade — routine relief against rare-event
fragility, under uncertain common `p` and level-specific `C(L)` — with legibility and calibration designed in, and the
system, the hazard analysis, and the acceptance all deferred to their owners.

---

## Reader Tasks (answerable from this guide)

1. **Place a design in the stage × level grid.** For "sensors cue attention, the system fuses
   trends and recommends, the operator approves, actuators execute," give the level of each of the
   four PSW stages, and say which stage's automation most threatens SA and why (§1).
2. **Compute the LOA trade.** Using the synthetic model `E(L) = (1−p)·W(L) + p·C(L)` with
   `W = [8,5,3,1]` and `C = [3,12,30,60]`, compute `E(L1)`–`E(L4)` at `p = 0.01` and `p = 0.15`,
   show the optimum moves from **L4 to L2**, and explain — via Bainbridge — why it slides down as
   `p` grows and why **L1 carries no takeover-failure term** (§2, Worked pass).
3. **Diagnose a trust failure.** Given "the operator stopped checking because the aid is usually
   right, then followed a wrong recommendation," name the miscalibration (over-trust) and the bias
   (commission), and give two design moves toward calibrated reliance (§3).
4. **Explain the takeover problem.** Say why the operator asked to retake control from failed
   automation is in the *worst* position (OOTL + decayed skill + high workload + low time), and
   name two partial mitigations (§4).
5. **Hold the boundary and refuse "higher is safer."** Given "just go full autonomy, it removes
   human error," explain why higher automation is a **trade** with new failure modes (not a
   subtraction), which owner gets the domain system and the hazard analysis, and who decides the
   level (§Boundaries, banner).

---

## Decision Cheat Sheet

| Situation | Move | Why (this guide) |
|---|---|---|
| Deciding "how much to automate" | choose a **level per stage** (PSW grid), not on/off | automation is a continuum across 4 stages (§1) |
| Tempted by "higher is safer" | price the **irony tax** (monitoring, OOTL, deskilling) | LOA↔safety is non-monotonic (§2, banner) |
| Off-normals rare, in-loop handling cheap | **higher LOA** minimizes expected cost | routine relief dominates; off-normal term is small (Worked pass) |
| Off-normals frequent or takeover costly | **keep the human engaged** (lower/mid LOA) | the optimum slides down the ladder — no winner (Worked pass) |
| Operator ignores or over-follows the aid | design for **calibrated reliance** (show limits/confidence) | over/under-trust both hurt (§3) |
| Long automated runs, rare interventions | fight **complacency/OOTL**: keep human doing something | vigilance + SA decay (§2, §4) |
| Handing control back to the human | **stage** transitions, warn, keep mode visible (≥2 channels) | abrupt OOTL handback is worst-case (§4, `06`) |
| Splitting tasks human/machine | think **teaming** (observable/directable/predictable), not a fixed list | MABA-MABA is too static (§5) |
| The FMS / driving levels / reactor control | route to **aeronautics/04, transportation/07, nuclear/05** | domain systems (Boundaries) |
| "Certify this automation as safe" | **out of scope** — org + regulator decide | safety contract |

---

## Common Confusion Points

**"Automation reduces workload, full stop."** It **redistributes** work — usually into monitoring
and exception-handling, which humans do poorly — and adds mode-tracking and coordination demands.
Net workload can even *rise* in the busy moments ("clumsy automation") (§2, banner).

**"Higher automation is safer."** Non-monotonic. Higher LOA improves *routine* performance and
lowers *routine* workload but degrades *failure-state* performance, SA, and takeover; the right
level depends on the off-normal-scenario rate and the level-specific conditional off-normal cost (§Big Picture,
Worked pass).

**"The Fitts list tells us what to automate."** It is a **1951 static heuristic** (`01`),
criticized as ignoring that automation *transforms* the joint task. Modern practice thinks in
dynamic allocation and **human–autonomy teaming**, not a fixed men/machines split (§5).

**"Trust means the operator likes the automation."** Trust is about **calibrated reliance** — it
should track the automation's *actual* reliability per situation. Both over-trust (complacency,
automation bias) and under-trust (disuse) are failures (§3).

**"The SAE levels and the levels of automation are the same scale."** No. **SAE J3016 (0–5)** is a
*domain* driving-automation taxonomy owned by `transportation/07`; the Sheridan/PSW levels are a
*human-factors* design continuum. Related, not identical — don't conflate them (§Boundaries).

---

## Global, WEIRD & Resource Caveats

- **The evidence base is Western aviation/military/process-control.** The ironies, LOA, and
  trust research grew from cockpits, control rooms, and lab studies with WEIRD, trained-operator
  samples; the *patterns* generalize, but the specific trust dynamics and acceptable levels vary
  with operator population, training, and culture.
- **Automation shifts risk unevenly.** High automation concentrates capability in resource-rich
  organizations and can export **deskilling** to operators who inherit the takeover role without
  the practice or the legible interfaces to succeed — a distributional cost the trade analysis
  should name, not hide.
- **Trust is culturally and organizationally shaped.** Deference to automated authority, and the
  willingness to override it, differ across work cultures and hierarchies; a calibration design
  validated in one setting can produce over-trust or disuse in another. Verify reliance against the
  *actual* operator population (guide `10`), not an imported assumption.

---

## A Contrasting Example (non-WEIRD, low-resource)

*Fictional, to show the trade under different constraints.*

**Setting.** A *fictional* smallholder-irrigation cooperative is offered a donated
"fully automatic" pump-scheduling controller (an L4 proposal) to replace manual scheduling by
experienced farmers who read the canals by eye.

**How the trade reads here.**
- **`p` and higher-level `C(L)` are unfavorable.** The controller was tuned on *other*
  soils and rainfall, so off-normal scenarios may be frequent (`p` high), while their
  conditional cost at higher automation levels may be large because farmers are newly
  **out-of-the-loop** and deskilled. The synthetic
  optimum slides *away* from L4 toward keeping farmers engaged (an L2 "recommend, human approves"
  design).
- **Legibility is the constraint, not compute.** With no maintenance budget, an **opaque** L4 box
  that fails silently is worse than a simple aid whose **state and recommendation are visible** and
  whose limits the farmers can see and override — calibrated reliance on a shoestring.
- **The refusal holds.** Human factors frames the trade and flags the deskilling and takeover
  costs; it does **not** declare the automation "safe," pick the level, or certify the pump system
  (that is the cooperative's and any local authority's). "Fully automatic, removes human error" is
  exactly the substitution myth the guide rejects.
