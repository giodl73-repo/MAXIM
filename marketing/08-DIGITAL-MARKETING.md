---
maxim_schema: maxim.frontmatter.v1
id: maxim:marketing:digital-marketing
kind: guide
module: marketing
section: marketing
title: Digital Marketing
status: source-custody
source_custody: partial
current_path: marketing/08-DIGITAL-MARKETING.md
canonical_path: marketing/08-DIGITAL-MARKETING.md
backsource_ids: [proof-backfill:marketing:08-digital-marketing, git-history:marketing:08-digital-marketing]
concepts: [SEO, SEM, social media, content marketing, programmatic, attribution, ad tech]
root_concepts: [digital marketing]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Digital Marketing

## The Big Picture

Digital marketing is the promotion mix (`05`) reborn on channels that are
**targetable, measurable, and biddable in real time**. The defining feature: every
touch can (in principle) be tracked to a user and a cost, which makes the funnel
instrumented and the spend optimizable. The landscape, organized by who owns the
audience:

```
+-------------------------------------------------------------------------+
|                     DIGITAL MARKETING LANDSCAPE                         |
|                                                                         |
|  OWNED              EARNED                PAID                          |
|  (you control)      (others give you)     (you buy)                     |
|  -------------      -----------------      -----------                  |
|  website / app      organic search rank    SEM (paid search)            |
|  email list         PR / press / mentions  paid social                  |
|  content / blog     shares / virality      display / programmatic       |
|  SEO (earns rank)   reviews / UGC          video / connected TV         |
|       |             influencer (organic)   retargeting                  |
|       |                  |                      |                       |
|       +------------------+----------------------+                       |
|                          v                                              |
|                  +-----------------+                                    |
|                  |   THE FUNNEL    |  every stage is now TRACKED        |
|                  | (instrumented)  |  -> attribution + analytics (09)   |
|                  +-----------------+                                    |
|                                                                         |
|  Owned = free but you build it. Earned = credible but uncontrolled.     |
|  Paid = instant + scalable but you pay per touch.                       |
+-------------------------------------------------------------------------+
```

**Read by ownership**: owned media you build and control; earned media others
grant (credible, uncontrolled); paid media you buy (instant, scalable). The
bridge: this is **build vs depend-on-community vs buy** — the same trade-off as
in-house vs open-source-with-goodwill vs paid-vendor. Most programs run all three.

This guide covers the channels and the ad-tech plumbing; the *measurement* (CAC,
ROAS, attribution math) lives in `09`.

---

## Search: SEO vs SEM

Search captures *intent* — the buyer is already looking. Two ways to appear:
**SEO** (earn the rank) and **SEM/paid search** (buy the placement).

```
+-----------------------------------------------------------------+
|              SEO  vs  SEM                                       |
|                                                                 |
|  SEO (organic)                  SEM (paid search)               |
|  -------------                  ----------------                |
|  earn ranking via relevance     bid in a real-time auction      |
|  + authority                    for ad slots                    |
|                                                                 |
|  cost: effort + time            cost: per click (CPC)           |
|  (no per-click charge)                                          |
|                                                                 |
|  slow to build, durable,        instant on, stops when you      |
|  compounding asset (OWNED)      stop paying (PAID)              |
|                                                                 |
|  levers:                        levers:                         |
|   - on-page (content, tags)      - keywords + match types       |
|   - technical (speed, crawl)     - bid + Quality Score          |
|   - off-page (backlinks/auth)    - ad copy + landing page       |
+-----------------------------------------------------------------+
```

SEM runs as a **real-time auction** (Google Ads / generalized second-price style):
your effective rank is roughly **bid x Quality Score** (relevance, expected CTR,
landing-page experience). So you don't simply outbid — a more relevant ad wins the
slot for less. The bridge: it's a priority queue where priority = bid weighted by
a relevance score, cleared continuously.

| | SEO | SEM |
|---|---|---|
| **Pay model** | Effort (no per-click) | Per click (CPC) |
| **Speed** | Slow (months) | Instant |
| **Durability** | Compounds; durable asset | Stops when budget stops |
| **Type** | Owned | Paid |
| **Key lever** | Relevance + authority (backlinks) | Bid x Quality Score |

---

## Social, Content, and Email

```
+-----------------------------------------------------------------+
|              OWNED + EARNED CHANNELS                            |
|                                                                 |
|  CONTENT MARKETING  create valuable content to attract +        |
|                     convert. Fuels SEO + social + email.        |
|                     The "pull" engine (vs interruptive ads).    |
|                                                                 |
|  SOCIAL MEDIA       organic (earned reach, community) +         |
|                     paid (targeted by interest/lookalike).      |
|                     Algorithmic feeds gate organic reach.       |
|                                                                 |
|  EMAIL / CRM        owned list, direct, highest ROI per $,      |
|                     lifecycle + retention engine. Segment +     |
|                     trigger-based automation.                   |
|                                                                 |
|  INFLUENCER         borrow an audience's trust (earned-ish,     |
|                     often paid). Credibility of a peer voice.   |
+-----------------------------------------------------------------+
```

**Content marketing** is the inbound/"pull" engine — earn attention with value
rather than interrupt for it — and it feeds the other channels (content ranks in
SEO, gets shared on social, populates email). **Email** remains the highest-ROI
owned channel precisely because you own the list (no algorithm or auction between
you and the audience) and can run lifecycle automation (welcome, onboarding,
win-back) keyed to behavior. **Social** organic reach is increasingly gated by
feed algorithms, pushing brands toward paid; **influencer** marketing rents the
trust of a creator's audience.

---

## Programmatic and the Ad-Tech Stack

For display/video, ad inventory is bought **programmatically** — automated,
real-time auctions per impression. Understanding the plumbing matters because it
determines targeting, cost, and where the money leaks.

```
+-----------------------------------------------------------------+
|              PROGRAMMATIC AD-TECH STACK                         |
|                                                                 |
|  ADVERTISER                                  PUBLISHER          |
|     |                                            |              |
|     v                                            v              |
|  .-------.        .----------.            .-------.             |
|  |  DSP  | <----> | AD       | <--------> |  SSP  |             |
|  | demand-        | EXCHANGE |            | supply-             |
|  | side    |      | (RTB     |            | side    |           |
|  | platform|      |  auction)|            | platform|           |
|  '-------'        '----------'            '-------'             |
|     |                  ^                      |                 |
|     v                  |                      v                 |
|  .-------.          per-impression       .---------.            |
|  |  DMP  |          auction, ~100ms      | inventory|           |
|  | data   |                              | (sites,  |           |
|  | mgmt   |                              |  apps)   |           |
|  '-------'                               '---------'            |
|                                                                 |
|  Each page load triggers a REAL-TIME BIDDING (RTB) auction:     |
|  the advertiser's DSP bids for THIS user, THIS impression,      |
|  in ~100 ms, using audience data.                               |
+-----------------------------------------------------------------+
```

| Component | Role | Side |
|---|---|---|
| **DSP** (demand-side platform) | Advertiser bids/targets/buys impressions | Buy |
| **SSP** (supply-side platform) | Publisher offers/yield-manages inventory | Sell |
| **Ad exchange** | The marketplace running the RTB auction | Middle |
| **DMP / CDP** | Audience data to target/segment | Data |

**Real-time bidding (RTB)** is the core: every impression is auctioned in
~100 milliseconds as the page loads — a high-throughput, low-latency auction
system bidding on *this specific user*. The engineering bridge is direct: it's a
distributed real-time auction at web scale, with the same latency budget and
fan-out concerns you'd design for any sub-100ms request path. The targeting fuel is
audience data (first-party from your CRM, plus third-party) — which is exactly what
privacy changes are constraining.

---

## The Privacy Shift

The tracking that made digital "fully measurable" is being dismantled. This
reshapes targeting and attribution (`09`).

```
+-----------------------------------------------------------------+
|              THE TRACKING TEARDOWN                              |
|                                                                 |
|  THIRD-PARTY COOKIE      cross-site tracking -> deprecated /    |
|  DEPRECATION             blocked by browsers                    |
|                                                                 |
|  MOBILE OPT-IN           app tracking transparency -> users     |
|  (ATT-style)             must consent to cross-app tracking     |
|                                                                 |
|  REGULATION              GDPR / CCPA -> consent, data rights    |
|                                                                 |
|  RESULT:                                                        |
|   - shift to FIRST-PARTY data (your own CRM/CDP)                |
|   - server-side + privacy-preserving measurement                |
|   - modeled conversions (estimate the unobservable)             |
|   - attribution gets HARDER -> lean on experiments (09)         |
+-----------------------------------------------------------------+
```

The practical consequence: **first-party data becomes the strategic asset** (your
logged-in users, your CRM), deterministic cross-site tracking gives way to modeled
and aggregated measurement, and the gold standard for "did it work" shifts back
toward *experiments and incrementality* (`09`) rather than click-path attribution.
The bridge: it's a deprecation of a global identifier you depended on — you migrate
to owned identity and accept more estimation where you used to have logs.

```
OLD WORLD                          DIGITAL ANALOG
-----------------------------      -------------------------------------
Interruptive broadcast ads         Paid display / programmatic
Pull-based docs that earn users    Content marketing / SEO
Real-time request auction          RTB / programmatic auction
Deprecating a global identifier    Third-party cookie deprecation
Migrate to owned auth/identity     Shift to first-party data
```

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Capture existing buyer intent now | SEM / paid search (instant, per-click) |
| Build a durable, compounding traffic asset | SEO + content marketing (owned, slow) |
| Reach the highest-ROI owned audience | Email / CRM (you own the list) |
| Scale targeted reach fast | Paid social + programmatic display |
| Re-engage people who didn't convert | Retargeting |
| Borrow a trusted peer voice | Influencer marketing |
| Buy display at scale, per-impression | Programmatic via a DSP (RTB auction) |
| Win paid search without overbidding | Raise Quality Score (relevance + landing page) |
| Survive the privacy shift | Invest in first-party data; lean on experiments for proof |
| Know which channel actually paid | Attribution + incrementality (`09`) |

---

## Common Confusion Points

### "SEO is free"

SEO has no per-click charge, but it costs content production, technical work, and
time (months to compound). It's an *owned asset you build*, not free traffic — and
it can erode if you stop investing. The trade vs SEM is effort/durability vs
money/instancy.

### "In paid search, the highest bid wins"

Effective rank is roughly **bid x Quality Score**. A more relevant ad with a better
landing page can win a higher slot for a *lower* cost-per-click. Relevance is a
bidding lever, not just the bid.

### "Programmatic means I buy ad space directly from sites"

Programmatic is *automated, auction-based* buying through a DSP against an exchange
— you bid on audiences/impressions in real time, not on fixed placements with a
publisher. Direct deals exist (programmatic guaranteed), but the default mental
model is the RTB auction.

### "Digital is fully measurable, so attribution is solved"

It was *more* measurable than offline, never *fully*. With cookie deprecation,
opt-outs, and cross-device gaps, deterministic tracking is shrinking. Attribution
is increasingly modeled; the trustworthy answer to "did it work" comes from
experiments and incrementality (`09`), not click logs alone.

### "More channels = more growth"

Channels have different roles (intent capture vs awareness vs retention) and
diminishing returns. Spreading budget thin across all of them underperforms
concentrating on the few that fit your funnel and economics. Pick by funnel stage
and measured CAC/ROAS (`09`), not by FOMO.

### "First-party and third-party data are interchangeable"

First-party (your own users/CRM) is consented, durable, and increasingly the
*only* reliable targeting/measurement substrate. Third-party (cross-site) data is
being deprecated and regulated away. The strategic shift is to build and leverage
first-party data — treat it as the asset it is.
