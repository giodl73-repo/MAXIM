---
maxim_schema: maxim.frontmatter.v1
id: maxim:accounting:cost-accounting
kind: guide
module: accounting
section: accounting
title: Cost Accounting - The Cost Measurement Engine
status: source-custody
source_custody: partial
current_path: accounting/06-COST-ACCOUNTING.md
canonical_path: accounting/06-COST-ACCOUNTING.md
backsource_ids: [proof-backfill:accounting:06-cost-accounting, git-history:accounting:06-cost-accounting]
concepts: [cost accounting, fixed cost, variable cost, contribution margin, break-even, activity-based costing, cost allocation]
root_concepts: [cost accounting]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Cost Accounting — The Cost Measurement Engine

## The Big Picture

Cost accounting is the **internal measurement layer** (managerial side, no GAAP/IFRS rules)
that answers: *what does a unit actually cost, and how does total cost behave as volume
changes?* Every pricing, make-or-buy, keep-or-drop, and break-even decision rests on
classifying costs correctly. The master distinction is **cost behavior** (fixed vs variable)
and **cost traceability** (direct vs indirect).

```
+--------------------------------------------------------------------------+
|                    TWO AXES OF COST CLASSIFICATION                      |
|                                                                          |
|              BEHAVIOR (vs volume)        TRACEABILITY (to a unit)        |
|              ------------------          ----------------------         |
|     FIXED  --- constant in total,        DIRECT --- traceable to one     |
|                varies per unit                       product/job        |
|                (rent, salaries)                      (materials, labor)  |
|                                                                          |
|     VARIABLE - varies in total,          INDIRECT (overhead) --- shared, |
|                constant per unit                     must be ALLOCATED   |
|                (materials, commissions)              (factory rent,      |
|                                                       supervisor salary) |
|                                                                          |
|     MIXED ---- both components            +---------------------------+  |
|                (utilities: base + usage)  | Total cost =              |  |
|                                           |   Fixed + (Variable x Q)  |  |
|                                           +---------------------------+  |
+--------------------------------------------------------------------------+
```

**Read it as a 2x2 of independent axes:** a cost is fixed-or-variable *and* direct-or-indirect.
Direct materials are variable+direct; factory rent is fixed+indirect; the two axes don't
collapse into one.

---

## Cost Behavior: The Linear Model

Within a **relevant range** (the volume band where the structure holds), total cost is
linear in quantity:

```
   Total Cost (TC) = Fixed Cost (F) + Variable Cost per unit (v) x Quantity (Q)

   $  TC
   |          ____________ slope = v (variable cost/unit)
   |     ____/
   |____/  <- F (fixed cost, the intercept)
   |
   +-------------------------------> Q
        relevant range
```

The crucial, counterintuitive inversion — **fixed and variable swap behavior depending on
whether you look at totals or per-unit:**

| | Total | Per unit |
|--|-------|----------|
| **Fixed cost** | Constant (flat) | **Decreases** as Q rises (spread over more units) |
| **Variable cost** | **Increases** with Q | Constant (same per unit) |

This inversion is the entire reason scale lowers unit cost: fixed costs amortize over more
units. **Bridge:** identical to fixed startup cost vs marginal cost in `economics/` — the
fixed cost is the up-front capex/overhead; `v` is marginal cost. Economies of scale = falling
average fixed cost.

---

## Contribution Margin — The Decision Workhorse

Contribution margin (CM) is **revenue minus variable costs** — what each sale "contributes"
toward covering fixed costs and then profit. It is the single most useful managerial number
because fixed costs are (in the short run) sunk.

```
   Price per unit            p
   - Variable cost per unit  v
   ----------------------------
   Contribution margin/unit  CM = p - v

   CM ratio = CM / p   (contribution per dollar of revenue)
```

```
   REVENUE
   |--- Variable costs ---|------ Contribution margin ------|
                          |-- covers Fixed --|-- Profit --|

   Once fixed costs are covered, ALL further CM is profit.
```

| Metric | Formula | Meaning |
|--------|---------|---------|
| CM per unit | p − v | $ each unit adds toward fixed + profit |
| CM ratio | (p − v) / p | Fraction of each revenue dollar that contributes |
| Total CM | (p − v) × Q | Total contribution before fixed costs |
| Operating income | Total CM − Fixed costs | What's left after fixed |

**Why contribution, not gross margin, drives decisions:** gross margin (file 03) mixes fixed
and variable production costs together. For a *decision* — accept this extra order? drop this
product? — only the costs that *change* matter, and those are the variable ones. Contribution
isolates them.

---

## Break-Even Analysis

Break-even is where total contribution exactly covers fixed costs — operating income = 0.

```
                  Fixed Costs              Fixed Costs
   Break-even Q = -------------   =   ---------------------
                  CM per unit           p - v

   Break-even $ = Fixed Costs / CM ratio
```

```
   $ |                              Total Revenue (slope p)
     |                         ___/
     |                    ___/  ___/ Total Cost (F + vQ)
     |               ___/  ___/
     |          ___/  ___/   <-- BREAK-EVEN (lines cross)
     |     ___/__/            below: LOSS    above: PROFIT
     |  _/_/  <- F
     +-------------------------------> Q
                    Q*
```

### Worked example

```
   Price             p   = $50
   Variable cost     v   = $30   -> CM = $20/unit, CM ratio = 40%
   Fixed costs       F   = $200,000

   Break-even units  = 200,000 / 20      = 10,000 units
   Break-even sales  = 200,000 / 0.40    = $500,000

   Target profit of $80,000:
     Units = (F + target) / CM = (200,000 + 80,000) / 20 = 14,000 units
```

**Operating leverage** falls straight out: the higher the fixed-cost share, the steeper
profit swings with volume. Degree of operating leverage = Total CM / Operating income. A
software firm (mostly fixed cost, near-zero `v`) has huge operating leverage — every extra
sale is almost pure profit past break-even, but below break-even losses mount fast.

---

## Cost Allocation — Spreading Indirect Costs

Direct costs trace to a product trivially. **Indirect (overhead)** costs — factory rent,
machine depreciation, supervisors — are shared and must be **allocated** by some basis. The
choice of basis is where cost accounting gets contentious.

```
   OVERHEAD POOL ($500,000)
        |
        | allocation base (the "driver" you pick)
        v
   +---------+   +---------+   +---------+
   |Product A|   |Product B|   |Product C|
   +---------+   +---------+   +---------+

   Traditional: allocate by a single volume base
                (direct labor hours, machine hours)
                Overhead rate = Pool / Total base units
```

```
   Predetermined overhead rate = Estimated overhead / Estimated base

   Applied overhead = Rate x Actual base used by the product
```

The flaw: a **single volume-based driver** (e.g., labor hours) over-costs high-volume simple
products and under-costs low-volume complex ones, because much overhead is driven by
*complexity and transactions*, not volume. This distortion is what activity-based costing
fixes.

---

## Activity-Based Costing (ABC)

ABC allocates overhead through **activities** and their **cost drivers** rather than one
blunt volume base. You identify what actually *causes* each pool of cost.

```
   TRADITIONAL                    ACTIVITY-BASED COSTING
   -----------                    ----------------------
   Overhead                       Overhead
      |                              |
      | one base                     +-> Activity: Machine setups
      | (labor hrs)                  |     driver: # setups
      v                              +-> Activity: Quality inspections
   Products                          |     driver: # inspections
                                     +-> Activity: Order processing
                                     |     driver: # orders
                                     +-> Activity: Machining
                                           driver: machine hours
                                              |
                                              v
                                          Products
                                     (each charged for the activities
                                      it actually consumes)
```

### ABC vs traditional — worked contrast

```
   Two products. Overhead = $400,000. Setups activity = $100,000 (50 setups).
   Product HIGH-VOL: 9,000 units, 5 setups (long runs)
   Product LOW-VOL:  1,000 units, 45 setups (many short custom runs)

   TRADITIONAL (allocate setups by volume / units):
     HIGH-VOL gets 90% of $100k = $90,000  (9,000/10,000)
     LOW-VOL  gets 10% of $100k = $10,000

   ABC (allocate setups by # setups, the real driver):
     HIGH-VOL gets  5/50 of $100k = $10,000
     LOW-VOL  gets 45/50 of $100k = $90,000   <- the truth: it's expensive!

   Conclusion: the low-volume custom product was being massively
   UNDER-costed. Traditional costing was subsidizing it.
```

This is ABC's whole value proposition: it reveals that **low-volume, high-complexity
products are often money-losers hidden by averaging**. The cost is more bookkeeping; the
benefit is decision-grade unit costs.

| | Traditional | ABC |
|--|-------------|-----|
| Allocation bases | One (volume) | Many (activity drivers) |
| Accuracy | Distorts by complexity | Captures complexity |
| Cost to run | Cheap | Expensive (track many drivers) |
| Best when | Overhead small, products similar | Overhead large, products diverse |

**Bridge (TCS):** ABC is *per-request cost attribution* vs *flat amortization*. Traditional
costing is like dividing your whole cloud bill by request count; ABC is profiling each
endpoint's actual CPU, I/O, and storage draw — you discover the rare complex endpoint is
eating the budget.

---

## Costing Systems and Inventory Methods (quick map)

| System | When used | How costs accumulate |
|--------|-----------|---------------------|
| **Job costing** | Custom, distinct jobs (construction, consulting) | Per job/order |
| **Process costing** | Mass, homogeneous output (chemicals, food) | Per process, averaged over units |
| **Absorption costing** | GAAP-required for external reporting | Fixed overhead *in* product cost |
| **Variable (direct) costing** | Internal decisions | Fixed overhead expensed as period cost |

**Absorption vs variable costing** matters because under absorption, fixed overhead gets
buried in inventory and only hits the income statement when sold — so building inventory can
*inflate* reported profit (a manipulation flagged in file 09). Variable costing avoids this
distortion but isn't GAAP-permissible externally.

---

## Old World → New World Bridges

| Prior art | Cost accounting concept |
|-----------|------------------------|
| Fixed startup cost + marginal cost | Fixed cost (F) + variable cost (v×Q) |
| Average cost falling with scale | Per-unit fixed cost declining (operating leverage) |
| Per-request cost attribution | Activity-based costing (driver-based allocation) |
| Flat amortization of shared cost | Traditional single-base overhead allocation |
| Profiling hot endpoints | ABC revealing high-complexity cost sinks |
| Marginal-cost decisions | Contribution-margin decisions (ignore sunk fixed cost) |
| Throughput past a capacity floor | Profit past break-even (all CM drops to profit) |

---

## Decision Cheat Sheet

| Decision | Use | Rule |
|----------|-----|------|
| Price floor on an extra order | Contribution margin | Accept if price > variable cost (covers `v`, adds CM) |
| Drop a product? | Contribution margin | Drop only if it can't cover its *avoidable* fixed costs |
| Break-even volume | F / CM per unit | Units needed to cover fixed costs |
| Hit a profit target | (F + target) / CM | Units needed for target profit |
| Are unit costs trustworthy? | ABC if products diverse | Single-base costing distorts mixed lines |
| Make or buy | Relevant (variable + avoidable) costs | Compare avoidable internal cost to buy price |
| Sensitivity of profit to volume | Operating leverage | High fixed share = high leverage = high risk |

---

## Common Confusion Points

### "Fixed costs are fixed forever"

Only within the **relevant range** and the short run. Add a second shift, lease another plant,
hire a layer of management — fixed costs step up. "Fixed" means *invariant to volume changes
within the current capacity band*, not permanent.

### "Allocate overhead, then use that full cost for pricing decisions"

For *short-run* decisions (accept an order, drop a line), allocated fixed overhead is often
irrelevant — it's sunk and doesn't change with the decision. Use **contribution margin**.
Full absorbed cost is for external reporting and long-run pricing, not marginal decisions.

### "ABC is always more accurate, so always use it"

ABC is more accurate but costs more to operate. If overhead is a small fraction of total cost
or products are similar, a single base is fine and ABC is wasted effort. ABC pays off when
overhead is large *and* products differ in complexity.

### "Per-unit fixed cost is a real cost per unit"

It's an artifact of dividing a total fixed cost by a chosen volume. It changes the instant
volume changes — so it is *not* a marginal cost and must not be used as one. Selling one more
unit does not cost you the per-unit fixed allocation; it costs you `v`.

### "Building inventory can't change profit"

Under **absorption costing** it can — fixed overhead capitalized into unsold inventory stays
off the income statement until sold, so overproducing inflates current profit. This is a real
earnings-management lever (file 09); variable costing removes it.
