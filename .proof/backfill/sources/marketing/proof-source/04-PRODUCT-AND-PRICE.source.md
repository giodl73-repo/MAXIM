---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "04-PRODUCT-AND-PRICE.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:marketing:product-and-price
kind: guide
module: marketing
section: marketing
title: Product and Price
status: source-custody
source_custody: partial
current_path: marketing/04-PRODUCT-AND-PRICE.md
canonical_path: marketing/04-PRODUCT-AND-PRICE.md
backsource_ids: [proof-backfill:marketing:04-product-and-price, git-history:marketing:04-product-and-price]
concepts: [product life cycle, new product development, pricing, price elasticity, value-based pricing]
root_concepts: [pricing, product life cycle]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Product and Price

## The Big Picture

Two of the four Ps, joined because they are the most *quantitative* and the most
*coupled*: what you build (product) sets what you can charge (price), and price
feeds back into what's worth building. The landscape runs from defining the
offering, through its life cycle, to setting the number on the tag.

```
+-------------------------------------------------------------------------+
|                      PRODUCT + PRICE LANDSCAPE                          |
|                                                                         |
|  PRODUCT SIDE                          PRICE SIDE                       |
|  ------------                          ----------                       |
|  What is the offering?                 What does the buyer pay?         |
|                                                                         |
|  .------------------.                  .------------------------.       |
|  | PRODUCT LEVELS   |                  | PRICING APPROACH       |       |
|  | core->actual->   |                  | cost+ / competition /  |       |
|  |  augmented       |                  | VALUE-BASED            |       |
|  '------------------'                  '------------------------'       |
|         |                                       |                       |
|         v                                       v                       |
|  .------------------.                  .------------------------.       |
|  | LIFE CYCLE       |  --- price ----> | ELASTICITY of demand   |       |
|  | intro->growth->  |    moves with    | how volume responds    |       |
|  |  maturity->decline    the stage     | to a price change      |       |
|  '------------------'                  '------------------------'       |
|         |                                       |                       |
|         v                                       v                       |
|  .------------------.                  .------------------------.       |
|  | NEW-PRODUCT DEV  |                  | PRICE STRUCTURE        |       |
|  | idea->...->launch|                  | tiers, bundles, discr. |       |
|  '------------------'                  '------------------------'       |
|                                                                         |
|  Price is the ONLY P that directly produces revenue; the rest cost.     |
+-------------------------------------------------------------------------+
```

Price is special: **Product, Place, and Promotion are cost centers; Price is the
revenue lever.** A 1% price improvement typically moves profit more than a 1% cost
cut, because it flows straight to the bottom line. This guide draws on
`economics/01-MICROECONOMICS.md` for demand/elasticity theory and applies it.

---

## Product: The Levels of an Offering

A "product" is more than the physical thing. Kotler's **three (or five) levels**
model unpacks what the customer actually buys.

```
+-----------------------------------------------------------------+
|                  LEVELS OF A PRODUCT                            |
|                                                                 |
|   .-------------------------------------------------.           |
|   |  AUGMENTED PRODUCT                              |           |
|   |  warranty, support, delivery, onboarding, docs  |           |
|   |   .--------------------------------------.      |           |
|   |   |  ACTUAL PRODUCT                      |      |           |
|   |   |  features, design, brand, quality,   |      |           |
|   |   |  packaging                           |      |           |
|   |   |    .---------------------------.     |      |           |
|   |   |    |  CORE BENEFIT             |     |      |           |
|   |   |    |  the fundamental need     |     |      |           |
|   |   |    |  being solved             |     |      |           |
|   |   |    '---------------------------'     |      |           |
|   |   '--------------------------------------'      |           |
|   '-------------------------------------------------'           |
|                                                                 |
|  Competition increasingly happens at the AUGMENTED level.       |
|  (For SaaS: support, SLAs, onboarding, docs = the real moat.)   |
+-----------------------------------------------------------------+
```

The strategic point: **buyers buy the core benefit, choose on the actual product,
and stay for the augmented product.** For software, the augmented layer (support,
docs, SLA, ecosystem) is often where differentiation and switching costs live —
the same insight as "the platform is the API plus everything around it."

---

## The Product Life Cycle

The **PLC** models sales and profit over a product's market life. Each stage has a
different competitive situation and a different mix emphasis — including price.

```
+-----------------------------------------------------------------+
|                  PRODUCT LIFE CYCLE                             |
|                                                                 |
|  sales                          .--------.                      |
|   ^                         .---'         '---.                 |
|   |                      .-'                    '-.   decline   |
|   |                   .-'                          '-.__        |
|   |                .-'                                  '--.    |
|   |             .-'                                         '.  |
|   |          .-'                                                |
|   |       .-'                                                   |
|   |    .-'                                                      |
|   |_.-'__________________________________________________ time  |
|     INTRO    |   GROWTH   |   MATURITY      |   DECLINE         |
|   -----------+------------+-----------------+-------------      |
|   low sales  | rising     | peak, flat      | falling           |
|   high cost  | falling    | lowest cost     | low cost          |
|     /unit    |   cost     |   /unit         |   /unit           |
|   losses     | profit up  | profit peak/    | profit falls      |
|              |            |   declines      |                   |
+-----------------------------------------------------------------+
```

| Stage | Objective | Pricing emphasis | Other mix moves |
|---|---|---|---|
| **Introduction** | Build awareness, trial | Skim *or* penetrate (below) | Heavy promotion, limited channels |
| **Growth** | Maximize share | Hold or reduce as costs fall | Broaden channels, build preference |
| **Maturity** | Defend share, harvest profit | Match competition; price wars | Differentiate, find new uses/segments |
| **Decline** | Harvest or exit | Cut to clear, or hold for loyalists | Phase out, reduce spend |

The PLC is a *useful heuristic, not a law* — shapes vary, "maturity" can be
extended for decades, and the curve is partly self-fulfilling (cut spend in
"decline" and you cause the decline). Use it to *ask* which stage you're in, not
to fatalistically follow a curve.

---

## New-Product Development

The funnel from idea to launch. Each gate kills bad ideas cheaply before they get
expensive — a staged pipeline with go/kill gates.

```
+-----------------------------------------------------------------+
|              NEW-PRODUCT DEVELOPMENT FUNNEL                     |
|                                                                 |
|  1 IDEA GENERATION    many ideas (internal, customers, etc.)    |
|       |  >> kill weak ideas                                     |
|  2 SCREENING          filter against strategy + feasibility     |
|       |                                                         |
|  3 CONCEPT TEST       describe to target buyers; gauge appeal   |
|       |                                                         |
|  4 BUSINESS ANALYSIS  demand forecast, costs, breakeven, ROI    |
|       |                                                         |
|  5 PRODUCT DEV        build it; prototype                       |
|       |                                                         |
|  6 MARKET / BETA TEST limited release; validate the mix         |
|       |                                                         |
|  7 COMMERCIALIZATION  full launch; scale production + promo     |
|                                                                 |
|  Funnel logic: cost rises down the stages; kill EARLY.          |
+-----------------------------------------------------------------+
```

This is a **stage-gate pipeline** — identical in spirit to a CI/CD or a research
funding gate: cheap experiments early, expensive commitments only after the idea
survives the gates. The expensive failure is the one that reaches stage 7 without
being killed at stage 2. Concept testing and conjoint (`07`) supply the customer
data for stages 3-4.

The **diffusion of innovations** curve (Rogers) describes *adoption* over the PLC:
innovators (2.5%) -> early adopters (13.5%) -> early majority (34%) -> late
majority (34%) -> laggards (16%). The "chasm" (Moore) between early adopters and
early majority is where many tech products die — a targeting (`02`) problem dressed
as a product problem.

---

## Price: The Three Approaches

Every price comes from one (ideally all three) of these lenses.

```
+-----------------------------------------------------------------+
|                  THREE PRICING APPROACHES                       |
|                                                                 |
|  COST-BASED        price = cost + markup                        |
|  (the floor)       Simple, defensible, IGNORES the customer.    |
|                    Sets the floor below which you lose money.   |
|                                                                 |
|  COMPETITION-      price relative to rivals (above/at/below).   |
|  BASED             Easy, but a race to the bottom if all do it. |
|                                                                 |
|  VALUE-BASED       price = customer's willingness to pay,       |
|  (the ceiling /    anchored on the value delivered.             |
|   the right one)   Captures the most surplus. HARD: requires    |
|                    knowing WTP (conjoint, research).            |
|                                                                 |
|   COST  <----------- the viable range ----------->  VALUE       |
|  (floor)        (where your price should live)     (ceiling)    |
+-----------------------------------------------------------------+
```

| Approach | Sets | Pro | Con |
|---|---|---|---|
| **Cost-plus** | The floor | Simple, covers cost | Leaves value on the table; ignores demand |
| **Competition-based** | A reference | Market-aware | Reactive; commoditizes |
| **Value-based** | The ceiling | Maximizes captured value | Needs WTP data (conjoint, `07`) |

**Value-based pricing** is the goal: set price by the value the customer perceives,
not your cost. Cost sets the floor; value sets the ceiling; competition locates
you in between. The shift from cost-plus to value-based is the single highest-
leverage pricing move most firms can make.

---

## Price Elasticity of Demand

The quantitative core. **Price elasticity** measures how responsive quantity
demanded is to a price change. (Full derivation in `economics/01-MICROECONOMICS.md`;
here is the operating version.)

```
              % change in quantity demanded
   E_d  =  ---------------------------------------
              % change in price

  E_d is normally NEGATIVE (price up -> quantity down). Convention
  often reports |E_d|.

  |E_d| > 1   ELASTIC      buyers very price-sensitive.
                           A price CUT raises total revenue.
  |E_d| < 1   INELASTIC    buyers insensitive.
                           A price INCREASE raises total revenue.
  |E_d| = 1   UNIT ELASTIC revenue unchanged by price moves.
```

```
+-----------------------------------------------------------------+
|             ELASTICITY -> REVENUE DIRECTION                     |
|                                                                 |
|                  |  raise price        |  cut price             |
|  ----------------+---------------------+----------------------  |
|  ELASTIC (>1)    |  revenue FALLS      |  revenue RISES         |
|  ----------------+---------------------+----------------------  |
|  INELASTIC (<1)  |  revenue RISES      |  revenue FALLS         |
+-----------------------------------------------------------------+
```

### What moves elasticity

| Factor | More elastic (sensitive) when... |
|---|---|
| **Substitutes** | Many close substitutes exist |
| **Necessity** | It's a luxury, not a necessity |
| **Share of wallet** | It's a big share of the buyer's budget |
| **Brand** | Weak brand (strong brand -> *inelastic*, the equity payoff) |
| **Time horizon** | Long run (buyers find alternatives) |
| **Switching cost** | Low switching cost / lock-in |

This is where **branding (`03`) cashes out**: brand equity *lowers* elasticity, so
you keep more volume at a higher price. The connection — equity bends the demand
curve, pricing harvests the bend.

```
OLD WORLD                          ELASTICITY ANALOG
-----------------------------      -------------------------------------
Load test: latency vs throughput   Demand curve: price vs quantity
Sensitivity / partial derivative   Elasticity = % d(Q) / % d(P)
"Where's the knee in the curve?"   Where demand turns elastic
Lock-in / switching cost reduces   Lock-in lowers elasticity
  churn                              (less price-sensitive)
```

---

## Price Structure: Beyond a Single Number

A single list price leaves money on the table because buyers have different WTP.
Structure extracts more of the surplus.

| Tactic | Mechanism | Behavioral hook (`behavioral-economics/`) |
|---|---|---|
| **Versioning / tiers** | Good-better-best; self-selection by WTP | Compromise effect (middle option) |
| **Bundling** | Sell together below sum of parts | Reduces price salience; mental accounting |
| **Price discrimination** | Different prices to different segments | Captures more consumer surplus |
| **Psychological pricing** | $9.99 vs $10; charm pricing | Left-digit anchoring |
| **Decoy / anchor** | A high option makes others look cheap | Anchoring; context effects |
| **Freemium** | Free base, paid upgrade | Endowment; foot-in-the-door |
| **Dynamic pricing** | Price varies by demand/time | Real-time elasticity capture |

**Price discrimination** (charging segments their respective WTP) is the
economically optimal structure when you can prevent arbitrage and identify
segments — the theory is in `economics/01-MICROECONOMICS.md`. Tiers/versioning are
its practical, self-selecting form: design the tiers so each segment sorts itself
into its WTP. Many pricing tactics are applied behavioral economics (anchoring,
the decoy/compromise effect, charm pricing) — cross-reference
`behavioral-economics/`.

---

## Decision Cheat Sheet

| I want to... | Do this |
|---|---|
| Define what I'm really selling | Map core / actual / augmented levels |
| Know where my product is in its life | Place it on the PLC; set mix emphasis to the stage |
| Cross the gap to the mainstream | Treat the chasm as a targeting problem (`02`) |
| Vet a new product idea cheaply | Run the stage-gate funnel; kill at the cheap early gates |
| Set a floor I can't go below | Cost-plus = the floor (covers cost) |
| Capture the most value | Value-based pricing on measured WTP (conjoint, `07`) |
| Decide raise vs cut | Estimate elasticity: elastic -> cut raises revenue; inelastic -> raise does |
| Lower customers' price sensitivity | Build brand (`03`), add switching costs, reduce substitutes |
| Serve multiple WTP segments | Versioning/tiers + price discrimination (prevent arbitrage) |

---

## Common Confusion Points

### "Cost-plus pricing is the safe default"

It is the *floor*, not the answer. Cost-plus ignores what the customer would pay
and competitors charge — it routinely under-prices strong products (leaving
surplus on the table) and over-prices weak ones (no one buys). Use it to set the
floor, then price to value.

### "Lower price always increases revenue"

Only when demand is *elastic* (|E_d| > 1). For inelastic demand (necessities,
strong brands, locked-in users) a price *cut* lowers revenue and a price *increase*
raises it. Direction depends on elasticity, which you must estimate — not assume.

### "Elasticity is a fixed property of the product"

It varies with substitutes, time horizon, brand strength, switching cost, and
segment. The *same* product is elastic for a price-shopper and inelastic for a
locked-in enterprise. That heterogeneity is exactly what price discrimination and
tiering exploit.

### "The product life cycle is a deterministic law"

It is a heuristic. Maturity can last decades; "decline" is often self-inflicted by
cutting investment. Use the PLC to diagnose stage and adjust the mix — not to
fatalistically manage a product to death.

### "More tiers always means more revenue"

Beyond a few options, choice overload (`behavioral-economics/`) suppresses
conversion, and tiers that don't map to distinct WTP segments just confuse. Design
tiers so each *self-selects* a real segment; stop when added tiers stop adding
captured surplus.

### "Price is just a number we set last"

Price is the only revenue-producing P and the highest-leverage profit lever. It
should be designed alongside the product (value-based), not bolted on at launch.
Setting price last, from cost, is the most common money-losing habit.
