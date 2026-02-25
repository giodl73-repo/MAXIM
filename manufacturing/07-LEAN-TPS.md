# Lean Manufacturing and the Toyota Production System

## The Big Picture

The Toyota Production System (TPS) is a production philosophy developed by Taiichi Ohno and Shigeo Shingo at Toyota from the 1950s–1970s. "Lean Manufacturing" is the Western formalization of TPS by Womack and Jones (1990 MIT study, "The Machine That Changed the World"). They are operationally the same framework with different vocabulary.

```
TPS STRUCTURE ("The TPS House")
──────────────────────────────────────────────────────────────────
                    ┌─────────────────────────────┐
                    │     GOAL: Best quality,      │
                    │  lowest cost, shortest lead  │
                    │    time, best safety,        │
                    │     high morale             │
                    └────────────┬────────────────┘
               ┌─────────────────┴────────────────────┐
               │                                       │
    ┌──────────▼──────────┐               ┌───────────▼──────────┐
    │     JUST-IN-TIME     │               │       JIDOKA          │
    │  Right part, right  │               │  "Automation with     │
    │  amount, right time │               │  a human touch"       │
    │                     │               │                       │
    │  Continuous flow    │               │  Stop when abnormal   │
    │  Pull system/kanban │               │  Separate man/machine │
    │  Takt time          │               │  Poka-yoke            │
    └─────────────────────┘               └───────────────────────┘
                         │               │
                         └───────┬───────┘
                                 │
    ┌────────────────────────────▼──────────────────────────────┐
    │                    FOUNDATION                              │
    │   Heijunka (leveling)  ·  Standardized work               │
    │   Kaizen (continuous improvement)                          │
    └────────────────────────────────────────────────────────────┘
```

**Bridge to software**: Lean thinking directly inspired DevOps and Agile. "The Phoenix Project" (Kim et al.) is explicitly a software adaptation of The Goal (Goldratt's ToC applied to manufacturing). Continuous deployment, one-piece flow, pull-based work queues — all came from TPS to software via Agile and DevOps.

---

## The Seven Wastes (Muda)

Ohno's original seven wastes — TIMWOOD mnemonic:

```
T — Transportation    Moving material that doesn't add value
                      (parts moving between buildings, cross-facility)

I — Inventory         More material than currently needed
                      (raw stock, WIP, finished goods)
                      Hides problems, ties up capital

M — Motion            Unnecessary operator movement
                      (reaching, walking, bending to find parts)

W — Waiting           Idle time for person or machine
                      (batch job queued, machine down, approval needed)

O — Overproduction    Making more than customer needs NOW
                      THE WORST waste — creates all other wastes
                      (push vs pull, make-to-forecast)

O — Overprocessing    More work than required by customer
                      (tight tolerance not needed, extra cleaning)

D — Defects           Making bad parts, inspection, rework, scrap
                      (includes warranty, customer returns)

Some organizations add:
S — Skills            Underutilizing people's knowledge and creativity
                      (the "eighth waste" — Lean practitioners debate inclusion)
```

**Software analogues**:
- Overproduction = features built ahead of need / speculative development
- Inventory = unmerged branches, incomplete features in WIP
- Waiting = PR review queue, blocked deployments, approval gates
- Defects = bugs, rework, technical debt

---

## Just-In-Time (JIT)

### Takt Time

```
TAKT TIME CALCULATION
──────────────────────────────────────────────────────────────────
Takt time = Available production time / Customer demand

Example:
  8-hour shift = 480 min
  Breaks: 30 min total
  Available: 450 min
  Customer demand: 90 units/day

  Takt time = 450 / 90 = 5 min/unit

Meaning: We need to complete one unit every 5 minutes
to exactly match customer demand. Not faster, not slower.

If cycle time < takt: over-producing (or waiting)
If cycle time > takt: behind (overtime, or lose orders)
```

### One-Piece Flow vs Batch

```
BATCH PROCESSING                    ONE-PIECE FLOW
──────────────────────────────      ──────────────────────────────
OP1 all 100 → OP2 all 100           OP1 one → OP2 one → OP3 one
→ OP3 all 100                       → ship one (repeat)

Batch lead time:                    Flow lead time:
  3 operations × 2 hours each       3 operations × 2 min each
  = 6 hours for first part          = 6 min for first part
  = 6 hours for last part           = 6 min for last part (also)

Batch reveals defects late:         Flow reveals defects immediately:
  Defect at OP1 found at OP3        Defect at OP1 found at OP2
  100 defective parts already made  1 defective part

Flow requires balanced stations, tight coupling, immediate feedback.
```

### Pull System and Kanban

```
PUSH vs PULL
──────────────────────────────────────────────────────────────────
PUSH:                              PULL:
Production driven by forecast.     Production triggered by actual
Make to plan.                      consumption downstream.

Plan → OP1 → OP2 → OP3 → Ship     Ship ← OP3 ← OP2 ← OP1 ← Signal
Inventory buffers at each step.    Kanban signals trigger replenishment.

Kanban signal types:
  Kanban card:   physical card authorizes production of one container
  Empty bin:     two-bin system — empty bin is signal to refill
  e-Kanban:      electronic signal in ERP/MES
  Triangle kbn:  reorder point signal

Container = defined quantity (batch size = ideally 1, practically small)
```

---

## Jidoka

Jidoka = "automation with a human touch" — machines detect abnormalities and stop. Separates machine monitoring from human operation. One operator can watch multiple machines because machines stop themselves when abnormal.

### Andon System

```
ANDON CORD / BUTTON
──────────────────────────────────────────────────────────────────
Worker notices problem → pulls andon cord → light/sound signals
Team lead has time window (e.g., takt time = 5 min) to fix problem
If not fixed by end of station → production line stops

Counterintuitive: stopping the line is GOOD
  → forces root cause resolution immediately
  → never passes defect downstream
  → forces problem solving (Kaizen)

Toyota stopped their line many times per day.
Western factories stopped it almost never.
Toyota had fewer defects.
```

### Poka-Yoke (Mistake-Proofing)

```
POKA-YOKE LEVELS
──────────────────────────────────────────────────────────────────
Level 1 — Warning (least strong):
  Light or alarm when error about to occur
  Operator can still proceed with error

Level 2 — Control (medium):
  Machine stops when abnormality detected
  Cannot proceed until corrected

Level 3 — Prevention (strongest):
  Physical design makes error impossible
  Wrong part cannot be inserted (keyed connectors)
  Wrong direction impossible (asymmetric fixture)

Examples:
  Asymmetric USB-A plug (physical prevention of wrong orientation)
  Factory: fixtures with limit switches — part correctly seated before machine cycles
  Assembly: color-coded parts, foolproofed gauges
  Software analog: type systems (wrong type = compile error, not runtime failure)
```

---

## Kaizen (Continuous Improvement)

### Kaizen vs Kaikaku

```
KAIZEN (continuous small improvements)
  Many small changes, every person, every day
  No investment required typically
  Bottom-up: workers propose and implement
  "Better today than yesterday"

KAIKAKU (radical transformation)
  Major process redesign, significant investment
  Top-down: management decision
  Examples: new production line, factory layout change
  Less frequent, bigger impact per event
```

### PDCA (Plan-Do-Check-Act) / PDSA

```
P — Plan:    Identify problem, analyze root cause (5 Why), propose countermeasure
D — Do:      Implement countermeasure (small scale, controlled)
C — Check:   Measure results, compare to prediction
A — Act:     If successful → standardize. If not → return to Plan.

             ┌───────────────────────────────────────────┐
             │               PDCA Cycle                  │
             │                                           │
             │   ┌───────┐         ┌───────┐            │
             │   │  Act  │◄────────│ Check │            │
             │   └───┬───┘         └───┬───┘            │
             │       │                 │                 │
             │   ┌───▼───┐         ┌───▼───┐            │
             │   │ Plan  │────────►│  Do   │            │
             │   └───────┘         └───────┘            │
             └───────────────────────────────────────────┘
```

### 5 Why (Root Cause Analysis)

```
EXAMPLE: Machine stopped
  Why 1? Overload, fuse blown
  Why 2? Insufficient lubrication on bearing
  Why 3? Oil pump not pumping adequately
  Why 4? Pump intake clogged with debris
  Why 5? No filter on intake, and no schedule to clean
  Countermeasure: Add intake filter, schedule cleaning

Not: replace fuse → same failure in 2 weeks
     replace pump → same failure next month
```

---

## Heijunka (Production Leveling)

```
HEIJUNKA: Level the mix and volume of production

Without heijunka:               With heijunka:
Monday:    100 units A          Each day: 20A, 20B, 20C
Tuesday:   0 units              Every day same mix
Wednesday: 100 units B          Level demand on supply chain
Thursday:  0 units              Level demand on labor
Friday:    100 units C          Smaller batches, faster response

Heijunka box:
  Grid of cells = time slots × product types
  Kanban cards fill cells by sequence
  Ensures small batches of each type cycle rapidly
  Customer variation absorbed in final assembly (mixed-model)
```

---

## Value Stream Mapping (VSM)

VSM is a lean tool to visualize entire value flow from customer demand to raw material, and identify waste.

```
TYPICAL VSM SYMBOLS
──────────────────────────────────────────────────────────────────
Factory/Supplier:  ┌─┐        Process box:    ┌────────┐
                   │ │                        │ Stamp  │
                   └─┘                        └────────┘

Inventory:         △           Push arrow:    ───►

Information:       ─ ─ ─►      Pull (kanban): ───○►

Timeline:          ▲  cycle    Total lead time vs value-add time
                   │  time
                   ▼  wait

Typical VSM finding:
  Total lead time:    15 days
  Value-added time:   45 minutes
  → 99.7% waste in time (waiting, transport, inventory)
  → Map shows where to focus improvement
```

---

## 5S Methodology

Workplace organization foundation for lean:

```
5S (JAPANESE → ENGLISH)
──────────────────────────────────────────────────────────────────
Seiri    → Sort:       Remove everything not needed at workstation
Seiton   → Straighten: "A place for everything, everything in its place"
              Shadow boards, floor tape, labeled locations
Seiso    → Shine:      Clean workstation daily (reveals abnormalities)
              "Cleaning is inspection"
Seiketsu → Standardize: Document the standard state, make visible
Shitsuke → Sustain:    Discipline to maintain standards, audit process

6S adds:
Safety:  Hazard identification built into workplace organization
```

---

## Theory of Constraints (TOC) — Goldratt

```
SYSTEM CONSTRAINT (BOTTLENECK)
──────────────────────────────────────────────────────────────────
Every system has exactly one constraint at any time.
Throughput of entire system = throughput of constraint.
Improving non-constraint operations achieves nothing for throughput.

TOC 5 Steps:
  1. Identify the constraint
  2. Exploit the constraint (maximize its output, stop starving it)
  3. Subordinate everything else to the constraint
     (don't over-produce upstream, buffer inventory in front of constraint)
  4. Elevate the constraint (invest to increase capacity if needed)
  5. Return to step 1 (constraint will move after you fix it)

Drum-Buffer-Rope:
  Drum = constraint sets pace (the "drum" of the system)
  Buffer = inventory in front of constraint (protects throughput)
  Rope = signal from constraint to release work upstream (pull signal)

Software connection:
  Deployment pipeline has a constraint (e.g., slow integration tests)
  Adding more devs without fixing constraint = more WIP, same throughput
  Fix the constraint first (parallelize tests, invest in infrastructure)
```

---

## Key Metrics

| Metric | Definition | Target |
|--------|-----------|--------|
| OEE (Overall Equipment Effectiveness) | Availability × Performance × Quality | >85% world class |
| Takt time | Available time / demand | Match cycle time |
| Cycle time | Actual time to complete one unit | ≤ takt time |
| Lead time | Customer order → delivery | As short as possible |
| WIP | Work in process count | Minimize (reveals constraint) |
| First Pass Yield (FPY) | Units passing without rework / total | >99% |
| DPMO | Defects per million opportunities | <3.4 (Six Sigma) |

---

## Decision Cheat Sheet

| Problem | Lean Tool |
|---------|-----------|
| Long lead time, unclear bottleneck | Value Stream Mapping |
| Defects, waste not visible | 5S + Andon + Jidoka |
| Uneven demand causing overproduction | Heijunka |
| Operators wait for machines | Jidoka (separate man/machine) |
| Root cause of recurring defect unknown | 5 Why |
| Production triggered by push/forecast | Implement kanban (pull) |
| Ergonomics bad, things hard to find | 5S |
| Production line too slow | Takt time analysis, constraint ID |

---

## Common Confusion Points

**Lean is not headcount reduction**: TPS was designed to grow Toyota without proportionally growing headcount — by making more value per person. Western companies often use "lean" to justify layoffs. This destroys the trust required for kaizen and worker engagement.

**Kanban is not Agile Kanban**: Agile kanban boards are inspired by Toyota kanban but are not the same. Toyota kanban is a physical replenishment signal. Agile kanban is a workflow visualization tool. They share the pull principle but operate differently.

**Pull vs push ambiguity**: "Push" in lean means production driven by forecast. In software "push" means deploying/sending code upstream. Don't confuse the direction of the metaphors.

**Heijunka vs JIT tension**: Heijunka requires some finished-goods inventory (level production ≠ build-to-order). Pure JIT build-to-order creates demand spikes. Real TPS manages this tension: build to leveled schedule, not to each order.

**Poka-yoke scope**: In manufacturing, poka-yoke is physical. In software, the equivalent is type systems, input validation schemas, API contracts — structural impossibility of wrong inputs. Both enforce correctness at the earliest possible point.
