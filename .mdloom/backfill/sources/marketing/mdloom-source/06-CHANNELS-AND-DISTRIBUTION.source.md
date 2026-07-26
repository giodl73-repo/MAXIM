---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "06-CHANNELS-AND-DISTRIBUTION.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:marketing:channels-and-distribution
kind: guide
module: marketing
section: marketing
title: Channels and Distribution
status: source-custody
source_custody: partial
current_path: marketing/06-CHANNELS-AND-DISTRIBUTION.md
canonical_path: marketing/06-CHANNELS-AND-DISTRIBUTION.md
backsource_ids: [mdloom-backfill:marketing:06-channels-and-distribution, git-history:marketing:06-channels-and-distribution]
concepts: [channel design, distribution, retail, omnichannel, channel conflict, place]
root_concepts: [distribution channel]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Channels and Distribution

## The Big Picture

This is the **Place** P: getting the offering to the buyer, when and where they
want it. A **marketing channel** (distribution channel) is the set of
interdependent organizations that move a product from producer to consumer. The
landscape runs from the producer, through intermediaries, to the buyer — across
both physical and digital paths.

```
+-------------------------------------------------------------------------+
|                       DISTRIBUTION CHANNEL                              |
|                                                                         |
|  PRODUCER                                              CONSUMER         |
|     |                                                     ^             |
|     |   DIRECT (0 levels)                                 |             |
|     o-----------------------------------------------------+             |
|     |                                                     |             |
|     |   ONE LEVEL          .----------.                   |             |
|     o--------------------> | RETAILER | ------------------+             |
|     |                      '----------'                   |             |
|     |                                                     |             |
|     |   TWO LEVELS    .-----------.    .----------.        |            |
|     o---------------> | WHOLESALER| -> | RETAILER | ------+             |
|     |                 '-----------'    '----------'        |            |
|     |                                                     |             |
|     |   THREE+    .-------.  .-------.  .--------.         |            |
|     o-----------> | AGENT |->| WHSLR |->| RETLR  | -------+             |
|                   '-------'  '-------'  '--------'                      |
|                                                                         |
|  More levels = more reach, less control + lower margin per unit.        |
+-------------------------------------------------------------------------+
```

**Read left-to-right by levels**: each intermediary you add extends reach but
costs margin and control. The bridge: a distribution channel is a **delivery
pipeline with middleware** — each hop adds reach/caching/locality but also
latency, cost, and a loss of end-to-end control. Direct-to-consumer is removing
the middleware to own the client relationship.

---

## What Channels Actually Do (Channel Functions)

Intermediaries are not just markup — they perform functions someone must do.
Removing an intermediary does not remove its *work*; it transfers the work to you
or the customer.

```
+-----------------------------------------------------------------+
|                  CHANNEL FUNCTIONS                              |
|                                                                 |
|  INFORMATION    market intelligence, demand signals             |
|  PROMOTION      local persuasion, merchandising                 |
|  CONTACT        finding + reaching buyers                       |
|  MATCHING       assortment, fitting offer to buyer needs        |
|  NEGOTIATION    reaching terms, transferring ownership          |
|  ----------     (the above complete the transaction)            |
|  PHYSICAL DIST  transport, storage, logistics                   |
|  FINANCING      credit, carrying inventory                      |
|  RISK TAKING    bearing the risk of carrying stock              |
|  ----------     (the above fulfill the transaction)             |
|                                                                 |
|  KEY LAW: you can eliminate the intermediary, but NOT the       |
|  function. The work shifts to producer or customer.             |
+-----------------------------------------------------------------+
```

This is the single most important channel idea. "Cutting out the middleman" sounds
like pure savings, but the middleman's *functions* (warehousing, last-mile, credit,
returns, local presence) still have to be performed and paid for. The bridge: it's
like removing a caching/CDN layer — you don't remove the need for fast local
delivery, you just have to provide it yourself.

---

## Channel Design Decisions

Designing a channel means three linked choices.

### 1. Channel length (number of levels)

Covered above: direct (0) vs one/two/three-level. **Disintermediation** (removing
levels, e.g. DTC e-commerce) trades reach for control and margin;
**reintermediation** is when new digital intermediaries (marketplaces, aggregators)
insert themselves.

### 2. Channel intensity (how many outlets)

```
+-----------------------------------------------------------------+
|                  DISTRIBUTION INTENSITY                         |
|                                                                 |
|  INTENSIVE        as many outlets as possible.                  |
|                   For: convenience goods (gum, soda).           |
|                   Goal: ubiquity. Low control.                  |
|                                                                 |
|  SELECTIVE        a chosen subset of qualified outlets.         |
|                   For: shopping goods (appliances, apparel).    |
|                   Balance of coverage + control.                |
|                                                                 |
|  EXCLUSIVE        one (or very few) outlet per area.            |
|                   For: specialty/luxury goods, complex B2B.     |
|                   Max control + brand protection. Low reach.    |
+-----------------------------------------------------------------+
```

| Intensity | Outlets | Product fit | Trade-off |
|---|---|---|---|
| **Intensive** | Maximum | Convenience goods | Ubiquity, but low control / brand dilution |
| **Selective** | Qualified subset | Shopping goods | Coverage + control balance |
| **Exclusive** | One per territory | Specialty / luxury / B2B | High control + premium, low reach |

Intensity must match the buyer's search behavior (`01`): for a *convenience* good
the buyer won't search, so you must be *everywhere* (intensive); for a *specialty*
good the buyer will seek you out, so *exclusive* protects the brand and margin.

### 3. Channel members (who, and on what terms)

Selecting, motivating (margins, training, co-op funds), and evaluating channel
partners. The terms set who bears which function and margin.

---

## Retail Formats

Retailers are the most common end-of-channel intermediary. The formats vary on
assortment breadth/depth, price, and service.

| Format | Assortment | Price | Service | Example role |
|---|---|---|---|---|
| **Specialty store** | Narrow, deep | Higher | High | One category, deep expertise |
| **Department store** | Broad, medium | Medium | Medium | Many categories under one roof |
| **Supermarket / mass** | Broad, shallow | Low | Low | High volume, low margin |
| **Category killer** | One category, very deep | Low | Med | Dominates a category on selection+price |
| **Warehouse club** | Broad, shallow, bulk | Very low | Very low | Membership, bulk, thin margin |
| **Convenience** | Narrow, shallow | Higher | Med | Location + speed premium |
| **Pure e-commerce** | Effectively unlimited | Variable | Self-serve | The long tail, data-rich |

The strategic axis is the **margin x turnover trade-off** (the "wheel of
retailing"): low-margin/high-turnover (mass, warehouse) vs high-margin/low-turnover
(specialty, luxury). New formats often enter low-margin and *trade up* over time,
creating room for the next low-margin entrant.

---

## Omnichannel

Buyers no longer move through one channel. **Omnichannel** is the integration of
all channels into one seamless experience — distinct from **multichannel** (many
channels operated in silos).

```
+-----------------------------------------------------------------+
|         MULTICHANNEL  vs  OMNICHANNEL                           |
|                                                                 |
|  MULTICHANNEL (siloed)        OMNICHANNEL (integrated)          |
|  -------------------          ----------------------            |
|   store   web   app           .---------------------------.     |
|     |      |     |            |   ONE customer view        |    |
|   (separate inventory,        |   (shared inventory,       |    |
|    pricing, data,             |    pricing, cart, history) |    |
|    no shared cart)            |                            |    |
|                               | store <-> web <-> app      |    |
|   customer hits walls         |   buy online, pick up in   |    |
|   crossing channels           |   store; return anywhere   |    |
|                               '---------------------------'     |
|                                                                 |
|  Omnichannel = the channels share STATE. The customer           |
|  experiences ONE system, not N systems.                         |
+-----------------------------------------------------------------+
```

The engineering bridge is exact: **multichannel is N microservices with separate
databases; omnichannel is the same services sharing consistent state** (one cart,
one inventory view, one customer record). BOPIS (buy-online-pickup-in-store),
ship-from-store, and return-anywhere are the user-visible features of that shared
state. The hard part — as in distributed systems — is *consistency* of inventory
and price across channels in real time.

```
OLD WORLD                          OMNICHANNEL ANALOG
-----------------------------      -------------------------------------
Microservices, separate DBs        Multichannel (siloed channels)
Shared source of truth / state     Omnichannel (one inventory/customer)
Cache coherence across nodes       Inventory consistency across channels
Single sign-on / unified session   One customer record across channels
```

---

## Channel Power and Conflict

Channels are organizations with their own interests, so they have **power** over
each other and experience **conflict**. This is the political economy of
distribution.

### Sources of channel power (French & Raven, applied)

| Power source | Basis | Example |
|---|---|---|
| **Coercive** | Threat (drop the line, penalize) | A dominant retailer threatening delisting |
| **Reward** | Incentives (margins, co-op funds) | Producer offering bonus margin |
| **Legitimate** | Contractual right | Franchise/licensing terms |
| **Expert** | Knowledge the other needs | Producer's product training |
| **Referent** | Desire to associate with the brand | Stores wanting a prestige brand |

### Types of channel conflict

```
+-----------------------------------------------------------------+
|                  CHANNEL CONFLICT                               |
|                                                                 |
|  VERTICAL      between LEVELS (producer vs retailer over        |
|                margin, terms, who owns the customer).           |
|                                                                 |
|  HORIZONTAL    between members at the SAME level (two           |
|                retailers in overlapping territory).             |
|                                                                 |
|  MULTICHANNEL  the firm's OWN channels competing (the DTC       |
|                site undercutting its retail partners).          |
|                                                                 |
|  Resolution: vertical marketing systems (VMS) -                 |
|   corporate (own the channel), contractual (franchise),         |
|   administered (lead by power). Or price/territory rules.       |
+-----------------------------------------------------------------+
```

The sharpest modern conflict is **multichannel/channel-cannibalization**: launch a
direct site and your retail partners feel undercut. Managing it (differentiated
assortments, price parity, partner margins) is a core channel-strategy problem.
**Vertical marketing systems (VMS)** — corporate (you own the channel),
contractual (franchising), or administered (one powerful member coordinates) —
reduce conflict by aligning incentives.

---

## Decision Cheat Sheet

| I want to... | Do this |
|---|---|
| Decide direct vs intermediaries | Weigh reach (more levels) vs control + margin (fewer) |
| Evaluate "cutting out the middleman" | Remember the *function* survives — who pays for it now? |
| Set how many outlets | Match intensity to good type: convenience -> intensive, luxury -> exclusive |
| Protect a premium brand at retail | Selective or exclusive distribution; control the experience |
| Serve buyers across store/web/app | Build omnichannel (shared state), not multichannel (silos) |
| Reduce inventory chaos across channels | Single source of truth for inventory + price |
| Manage a powerful retail partner | Build reward/referent power; avoid pure dependence |
| Launch DTC without angering partners | Manage channel conflict: differentiated assortment, price parity |
| Align a fragmented channel | Use a VMS (corporate, contractual, or administered) |

---

## Common Confusion Points

### "Cutting out the middleman is pure savings"

The intermediary's *functions* (warehousing, last-mile, credit, returns, local
selling) don't vanish — they transfer to you or the customer. DTC can win on
control and data, but you now run the logistics the wholesaler used to. Count the
transferred cost, not just the removed margin.

### "More distribution is always better"

Not for premium/specialty goods. Intensive distribution of a luxury brand dilutes
its exclusivity and reference price (`03`, `04`). Match intensity to the product and
the buyer's search behavior — sometimes *fewer* outlets is the strategy.

### "Multichannel and omnichannel are synonyms"

Multichannel = many channels run in silos (separate inventory, pricing, data).
Omnichannel = channels integrated into one experience with shared state. The
difference is consistency — the customer hits no walls crossing from app to store.
It's the difference between separate databases and a shared source of truth.

### "Channel conflict means we picked bad partners"

Conflict is structural — partners have genuinely different interests (margin,
customer ownership, territory). The job isn't to eliminate it but to *manage* it
with aligned incentives (VMS), clear rules, and differentiated roles. Some tension
is healthy.

### "Place is the least strategic P"

For many businesses, distribution is the moat. Availability beats persuasion for
convenience goods; an exclusive channel protects a luxury brand; omnichannel
fulfillment is a hard, defensible capability. Place can be where competitors can't
follow.
