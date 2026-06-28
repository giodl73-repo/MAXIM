---
maxim_schema: maxim.frontmatter.v1
id: maxim:accounting:managerial-accounting
kind: guide
module: accounting
section: accounting
title: Managerial Accounting - Decisions, Budgets, Variances
status: source-custody
source_custody: partial
current_path: accounting/07-MANAGERIAL-ACCOUNTING.md
canonical_path: accounting/07-MANAGERIAL-ACCOUNTING.md
backsource_ids: [proof-backfill:accounting:07-managerial-accounting, git-history:accounting:07-managerial-accounting]
concepts: [managerial accounting, budgeting, variance analysis, transfer pricing, relevant costs, capital budgeting]
root_concepts: [managerial accounting]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Managerial Accounting — Decisions, Budgets, Variances

## The Big Picture

Managerial accounting is the **forward-looking, internal** discipline that turns the cost
data of file 06 into plans (budgets), control (variance analysis), internal pricing
(transfer pricing), and discrete decisions (relevant costs, capital budgeting). It has no
GAAP/IFRS rules — its only standard is *usefulness to the decision*. This is the accounting a
VP with budget responsibility actually operates inside.

```
+--------------------------------------------------------------------------+
|                  THE MANAGERIAL CONTROL LOOP                            |
|                                                                          |
|     PLAN              EXECUTE            MEASURE           CORRECT       |
|     ----              -------            -------           -------       |
|   +--------+        +---------+        +-----------+     +----------+    |
|   | BUDGET |  --->  | actual  |  --->  | VARIANCE  | --> | decision |    |
|   | (the   |        | results |        | analysis  |     | / adjust |    |
|   | plan)  |        |         |        | (plan vs  |     |          |    |
|   +--------+        +---------+        |  actual)  |     +----------+    |
|       ^                                +-----------+          |         |
|       |                                                       |         |
|       +-------------------- feedback ---------------------------+        |
|                                                                          |
|   Plus discrete decisions, run on RELEVANT COSTS:                        |
|     make-or-buy * keep-or-drop * accept-special-order * capital budgeting|
+--------------------------------------------------------------------------+
```

**Read it as a control loop**: plan, execute, measure the gap, correct, re-plan. Variance
analysis is the feedback signal; relevant-cost analysis governs the discrete choices.
**Bridge:** this is a PID controller / OODA loop on the business — the budget is the setpoint,
variance is the error term.

---

## Budgeting — The Setpoint

A **master budget** is an integrated plan that cascades from a sales forecast down to
pro-forma financial statements. Each piece feeds the next.

```
   SALES BUDGET  (forecast units x price)
        |
        +-> PRODUCTION BUDGET (units to make = sales + desired ending - beginning inv)
        |        +-> Direct materials budget
        |        +-> Direct labor budget
        |        +-> Manufacturing overhead budget
        +-> SELLING & ADMIN BUDGET
                 |
                 v
        CASH BUDGET (receipts - disbursements -> financing needs)
                 |
                 v
        PRO-FORMA INCOME STATEMENT, BALANCE SHEET, CASH FLOW
```

### Static vs flexible budget — the key control distinction

```
   STATIC BUDGET  ---- built for ONE planned volume. Comparing actual
                       (at a different volume) to it mixes volume and
                       efficiency effects -> misleading.

   FLEXIBLE BUDGET ---- recomputed at the ACTUAL volume achieved.
                        Isolates: "given the volume we hit, did we
                        control costs per unit?"
```

A flexible budget is the prerequisite for honest variance analysis: you can't tell whether a
cost overrun was "we made more units" (fine) or "we wasted materials" (bad) until you flex
the budget to actual volume.

| Budget type | Built at | Answers |
|-------------|----------|---------|
| Static (master) | Planned volume | Did we hit the plan? (mixes volume + efficiency) |
| Flexible | Actual volume | Given actual volume, did we control costs? |

---

## Variance Analysis — The Feedback Signal

A variance is **actual minus budgeted**, decomposed so you know *which lever* moved. The
total operating-income variance splits cleanly:

```
   TOTAL VARIANCE (actual op income vs static budget)
        |
        +-- SALES-VOLUME variance  (we sold a different # than planned)
        |        = (actual units - budgeted units) x budgeted CM
        |
        +-- FLEXIBLE-BUDGET variance (at actual volume, cost/price control)
                 |
                 +-- PRICE variance     (paid more/less per input unit)
                 +-- EFFICIENCY variance (used more/less input per output)
```

### The price/efficiency split (the workhorse decomposition)

For any input (materials, labor), the flexible-budget variance splits into a **price** piece
and a **quantity/efficiency** piece:

```
   PRICE variance      = (Actual price - Std price) x Actual quantity used
   EFFICIENCY variance = (Actual qty - Std qty allowed) x Std price

   where Std qty allowed = std input per unit x actual units produced
```

Labeling convention: a variance is **Favorable (F)** if it raises income (lower cost, higher
revenue) and **Unfavorable (U)** if it cuts income. Favorable is not automatically "good" —
a favorable materials *price* variance from buying cheap, defective stock can cause an
unfavorable *efficiency* variance downstream (scrap, rework). Read variances as a *system*.

### Worked example — direct materials

```
   Standard: 2 lbs/unit at $5/lb.   Produced 1,000 units.
   Actual:   2,200 lbs bought/used at $4.50/lb.

   Std qty allowed = 2 lbs x 1,000 units = 2,000 lbs

   PRICE var.      = ($4.50 - $5.00) x 2,200 = -$1,100  -> $1,100 Favorable
                     (paid 50c/lb less)
   EFFICIENCY var. = (2,200 - 2,000) lbs x $5.00 = +$1,000 -> $1,000 Unfavorable
                     (used 200 extra lbs)

   Net materials variance = 1,100 F - 1,000 U = $100 Favorable
   Story: bought cheap material, then wasted more of it. The two are
   likely LINKED — investigate the purchasing decision.
```

That linkage — favorable price *causing* unfavorable efficiency — is exactly why you
decompose rather than look at the net. The net ($100 F) hides the real story.

---

## Transfer Pricing — Internal Markets

When one division sells to another inside the same firm, the **transfer price** sets each
division's measured profit. It's an internal-market mechanism-design problem
(bridge: `economics/` mechanism design — you're choosing a price rule to align divisional
incentives with firm-wide optimum).

```
   DIVISION A (seller)  --- transfer price P --->  DIVISION B (buyer)
   - higher P helps A's profit                     - lower P helps B's profit
   - the FIRM's total profit is unchanged by P (it nets out internally)
   - but P drives each manager's DECISIONS and bonus
```

### The methods

| Method | Transfer price = | Pros | Cons |
|--------|------------------|------|------|
| **Market-based** | External market price | Objective, optimal when a market exists | Needs a real external market |
| **Cost-based** | Variable or full cost (± markup) | Simple, no market needed | Passes on inefficiency; full-cost distorts |
| **Negotiated** | Whatever divisions agree | Reflects local info | Time-consuming; power imbalances |

**The general rule (decision-correct floor):**

```
   Minimum transfer price = Variable cost + Opportunity cost of the seller

   - If seller has IDLE capacity: opportunity cost = 0 -> floor = variable cost
   - If seller is at CAPACITY: opportunity cost = lost external CM
                               -> floor = market price
```

This rule makes divisional self-interest match the firm-wide optimum — the core
mechanism-design insight. Set it wrong and a division will rationally reject internal trades
that benefit the whole firm (or accept ones that don't). **Tax angle:** multinational transfer
pricing also shifts profit across tax jurisdictions, which is why it's heavily regulated
(arm's-length standard, OECD guidelines — file 09 territory).

---

## Relevant Costs — Decision-Specific Cost

The most important conceptual discipline: for any decision, only **costs that differ between
alternatives** are relevant. Two large categories are *irrelevant* and routinely trip people
up:

```
   RELEVANT          = future costs/revenues that DIFFER between options
   IRRELEVANT (ignore):
     SUNK COST       = already incurred, unrecoverable (the $X we
                       already spent on the prototype) -> NEVER relevant
     COMMON/UNAVOID. = costs identical under both options (allocated HQ
                       overhead that doesn't change) -> irrelevant
   OPPORTUNITY COST  = the foregone benefit of the next-best option
                       -> ALWAYS relevant (even though it's not a cash outlay)
```

### The classic decisions

```
   MAKE OR BUY:
     Compare buy price vs (variable cost + AVOIDABLE fixed + opportunity
     cost of freed capacity). Ignore allocated fixed overhead that
     persists either way.

   KEEP OR DROP a product line:
     Drop only if its contribution margin < its AVOIDABLE fixed costs.
     The allocated corporate overhead that remains after dropping it is
     IRRELEVANT -- dropping a "loss-making" line can make the firm worse
     off if it was covering shared fixed costs.

   ACCEPT A SPECIAL ORDER:
     If idle capacity exists, accept any price above VARIABLE cost --
     fixed costs are sunk for the period. (Watch: don't cannibalize
     full-price sales or set a precedent.)
```

The keep-or-drop trap is the most common executive error: a product showing an accounting
"loss" after fully-allocated overhead may still contribute positively to fixed costs. Drop it
and the unavoidable overhead just reallocates to the survivors, often turning *them* into
"losers." Decide on **avoidable** costs only.

---

## Capital Budgeting — Long-Horizon Decisions

For multi-year investments, managerial accounting uses discounted cash flow (shared with
`finance/`). Brief map, because it's where managerial accounting hands off to valuation:

| Method | Rule | Note |
|--------|------|------|
| **NPV** | Accept if NPV > 0 | The correct, theoretically-sound rule |
| **IRR** | Accept if IRR > hurdle rate | Intuitive %, but breaks on non-conventional flows |
| **Payback** | Years to recoup outlay | Ignores time value & post-payback cash — weak |
| **Profitability index** | PV inflows / outlay | For ranking under capital rationing |

NPV is the right default; payback is a liquidity heuristic, not a value rule. **Behavioral
note:** capital budgeting is where **escalation of commitment** (file `behavioral-economics/`)
strikes — managers throw good money after bad because of sunk cost. The relevant-cost
discipline above is the antidote: sunk cost is *never* relevant.

---

## Old World → New World Bridges

| Prior art | Managerial concept |
|-----------|-------------------|
| PID controller / setpoint + error | Budget (setpoint) + variance (error signal) |
| OODA / observe-orient-decide-act loop | Plan → execute → measure variance → correct |
| Normalizing a benchmark to actual load | Flexible budget (re-flex to actual volume) |
| Decomposing an error into components | Price vs efficiency variance split |
| Internal billing / chargeback model | Transfer pricing between divisions |
| Mechanism design / incentive alignment | Transfer-price rule = variable + opportunity cost |
| Sunk-cost fallacy in project cancellation | Sunk costs irrelevant; escalation of commitment |
| Marginal analysis on a request | Relevant-cost (only differences matter) |

---

## Decision Cheat Sheet

| Decision | Relevant figures | Rule |
|----------|------------------|------|
| Build the budget | Sales forecast → cascade | Master budget; cash budget reveals financing need |
| Judge cost control | Flexible budget at actual volume | Variance = actual − flexible |
| Diagnose a cost overrun | Price + efficiency split | Decompose; look for linked variances |
| Internal transfer price | Variable cost + opportunity cost | = variable cost if idle; = market if at capacity |
| Make or buy | Avoidable cost vs buy price | Ignore unavoidable allocated overhead |
| Keep or drop a line | CM vs avoidable fixed | Drop only if CM < avoidable fixed |
| Special order, idle capacity | Variable cost as floor | Accept above variable cost |
| Multi-year investment | NPV | Accept if NPV > 0; ignore sunk cost |

---

## Common Confusion Points

### "A favorable variance is always good"

No. A favorable *price* variance can come from buying low-quality inputs that blow the
*efficiency* variance, or from skipping maintenance that bites later. Variances are signals to
investigate, not verdicts — and they interact.

### "Drop the product line that shows a loss"

Only if its loss is from *avoidable* costs. If the "loss" is driven by allocated corporate
overhead that won't disappear, dropping the line removes its contribution while the overhead
reallocates to survivors. Decide on contribution margin vs avoidable fixed cost, never on
fully-allocated accounting profit.

### "Sunk costs should factor into the decision"

Never. Money already spent and unrecoverable is irrelevant to any forward decision — that's
the definition of sunk. Including it is the sunk-cost fallacy / escalation of commitment. The
only question is which future cash flows differ between your options.

### "Transfer price doesn't matter — it's all the same company"

It doesn't change *firm-wide* profit, but it absolutely changes divisional managers'
*decisions* and incentives, and (for multinationals) the *tax* paid across jurisdictions. Get
the rule wrong and divisions reject value-creating internal trades. Mechanism design matters.

### "Comparing actual to the original budget tells me if we controlled costs"

Not by itself — the original (static) budget was built for a different volume. You must flex
the budget to actual volume first; otherwise volume effects masquerade as cost-control
effects.
