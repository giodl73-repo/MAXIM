---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "07-COLLECTION-MANAGEMENT.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:library-information-science:collection-management
kind: guide
module: library-information-science
section: language-communication
title: Collection Management - Acquisition, Deselection, Open Access
status: source-custody
source_custody: partial
current_path: library-information-science/07-COLLECTION-MANAGEMENT.md
canonical_path: library-information-science/07-COLLECTION-MANAGEMENT.md
backsource_ids: [proof-backfill:library-information-science:07-collection, git-history:library-information-science:07-collection]
concepts: [collection management, acquisition, deselection, weeding, scholarly communication, open access, serials crisis, licensing]
root_concepts: [collection management]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Collection Management — The Collection as a Managed Asset

A collection is not a pile that only grows. It is a **portfolio managed under a
budget**: things are acquired against a policy, evaluated for ongoing value, and
deselected when they no longer earn their space. Layered on top is the economics of
**scholarly communication** — who owns research, who pays to read it, and the open-
access movement reshaping both. For a VP, this file is the most familiar of the set:
it is lifecycle management of an asset portfolio with vendor contracts, a budget, and
a build-vs-license decision.

```
+======================================================================================+
|              THE COLLECTION LIFECYCLE  (a managed portfolio, not a hoard)            |
+======================================================================================+
|                                                                                      |
|   .----------.   .-----------.   .------------.   .-----------.   .------------.     |
|   | SELECT   |-->| ACQUIRE   |-->| MAINTAIN / |-->| EVALUATE  |-->| DESELECT   |     |
|   | (policy) |   | (buy /    |   | provide    |   | (usage,   |   | (weed /    |     |
|   |          |   |  license) |   | access)    |   | gaps)     |   | deaccess.) |     |
|   '----------'   '-----------'   '------------'   '-----------'   '------------'     |
|        ^                                                              |              |
|        |                  feedback: gaps & usage drive next cycle      |             |
|        '--------------------------------------------------------------'              |
|                                                                                      |
|   GOVERNED BY:   collection development policy  +  fixed budget                      |
|                                                                                      |
|   THE BIG ECONOMIC CONTEXT (scholarly communication):                                |
|   .-------------------------------------------------------------------.              |
|   | researchers WRITE -> publishers OWN -> libraries BUY BACK access   |             |
|   | the "serials crisis" -> the OPEN ACCESS response                  |              |
|   '-------------------------------------------------------------------'              |
+======================================================================================+
```

---

## Acquisition: Own vs. License

The first strategic split, and one a VP knows cold from software: do you **own** the
asset or **license access** to it? Print is owned (a perpetual, transferable copy);
most digital content is licensed (access governed by a contract, often revocable, not
transferable). The shift from owning to licensing is the same one that moved software
from boxed perpetual licenses to SaaS subscriptions — and it carries the same risks.

```
+----------------------------------------------------------------------------+
|  OWN (purchase)               |  LICENSE (subscription / access)           |
+----------------------------------------------------------------------------+
|  perpetual, you hold the copy |  access for the contract term only         |
|  no ongoing fee after buying  |  recurring fee; stops when you stop paying |
|  you control retention        |  vendor controls the platform & terms      |
|  preservation is YOUR job     |  perpetual-access clauses are negotiated   |
|                               |                                            |
|  = a perpetual software       |  = SaaS / subscription. Cancel and the     |
|    license + the binary       |    access ends; you kept nothing.          |
+----------------------------------------------------------------------------+
```

Acquisition models have themselves been "cloudified": **approval plans** (a vendor
auto-ships titles matching a profile — a standing order / subscription to a category),
**DDA / PDA** (Demand/Patron-Driven Acquisition — buy only when a user actually
triggers use, i.e. pay-per-use / lazy provisioning), and **Big Deals** (bundle
licensing of a publisher's whole journal package — the enterprise volume contract,
with the same lock-in dynamics). Each is a procurement strategy trading cost, control,
and risk in ways that map directly onto cloud/SaaS purchasing.

---

## Deselection (Weeding) — Pruning the Asset

The counterintuitive professional discipline: a good collection is *weeded*. Removing
low-value items (deselection, or "weeding") keeps the collection relevant, navigable,
and within space — the same reason you deprecate dead code, prune stale feature flags,
and archive cold data off the hot tier. A monotonically growing store degrades.

The standard decision framework is **CREW** / the **MUSTIE** criteria — a checklist
for "should this item leave the collection?"

```
+---------------------------------------------------------------------------+
|  MUSTIE  --  weeding criteria (remove if it is...)                        |
+---------------------------------------------------------------------------+
|   M  Misleading   factually outdated / wrong                              |
|   U  Ugly         worn beyond use                                         |
|   S  Superseded   a newer edition or better item exists                   |
|   T  Trivial      no discernible value                                    |
|   I  Irrelevant   no longer fits the community's needs                    |
|   E  Elsewhere    available readily elsewhere (ILL, consortium, online)   |
+---------------------------------------------------------------------------+
|   Driven by data: circulation stats, last-use dates, condition.           |
|   = a deprecation / tiering policy with usage-based eviction.             |
+---------------------------------------------------------------------------+
```

The "E — available Elsewhere" criterion is shared infrastructure thinking:
**resource sharing** via interlibrary loan (ILL) and **consortia** means a library
need not own everything if it can borrow reliably. This is exactly relying on a shared
service or CDN rather than provisioning every asset locally — own the hot set, borrow
the long tail. Deaccessioning from an *archive* (file 06) is far more constrained,
since those records are unique and irreplaceable; weeding a library collection of
re-buyable published copies is routine asset management.

---

## Scholarly Communication and the Serials Crisis

Now the economics. Scholarly publishing has a structure that, examined coldly, is a
striking market failure — and understanding it explains the entire open-access
movement.

```
+======================================================================================+
|                THE SCHOLARLY PUBLISHING CYCLE (and why it broke)                     |
+======================================================================================+
|                                                                                      |
|   .-----------.   .------------.   .-------------.   .------------------.            |
|   | RESEARCHER|-->| PUBLISHER  |-->| THE SAME    |-->| LIBRARY buys     |            |
|   | writes &  |   | takes      |   | researchers |   | back access at   |            |
|   | peer-     |   | copyright, |   | (as readers)|   | high subscription|            |
|   | reviews   |   | adds little|   | NEED it     |   | prices           |            |
|   | (FOR FREE)|   | cost       |   |             |   |                  |            |
|   '-----------'   '------------'   '-------------'   '------------------'            |
|                                                                                      |
|   The institution PAYS for the labor (salaries), GIVES AWAY the copyright,           |
|   then PAYS AGAIN to read its own output. Reviewers work unpaid.                     |
|                                                                                      |
|   RESULT: the "SERIALS CRISIS" -- journal prices rose far faster than                |
|   library budgets for decades; a few publishers captured the market.                 |
+======================================================================================+
```

The serials crisis is the decades-long phenomenon of journal subscription prices
rising far faster than inflation or library budgets, concentrated among a handful of
commercial publishers with effective monopolies on must-have titles (inelastic
demand — researchers *must* have the key journals in their field, so price has little
ceiling). A VP recognizes the shape: a critical dependency controlled by a vendor with
pricing power and high switching costs. The **Big Deal** bundle deepened the lock-in,
and the response was structural.

---

## Open Access — Routing Around the Toll

Open access (OA) makes research literature free to read online. There are two main
roads and a spectrum of colors, and the distinction is a publishing-model distinction,
not a quality one.

```
+----------------------------------------------------------------------------+
|  THE ROADS AND COLORS OF OPEN ACCESS                                       |
+----------------------------------------------------------------------------+
|                                                                            |
|  GREEN OA   self-archiving. Author deposits a version (often the           |
|             accepted manuscript) in a repository (arXiv, an institutional  |
|             repository -- file 08). Free; may have an embargo.             |
|                                                                            |
|  GOLD OA    the journal itself is open. Often funded by an APC (Article    |
|             Processing Charge) -- the AUTHOR/funder pays to publish,       |
|             readers pay nothing. Shifts cost from reader to producer.      |
|                                                                            |
|  DIAMOND OA gold with NO author fee -- funded by institutions/grants.      |
|             Free to read AND free to publish.                              |
|                                                                            |
|  HYBRID     a subscription journal that opens individual articles for an   |
|             APC -- criticized as "double dipping" (paid twice).            |
+----------------------------------------------------------------------------+
```

The APC model is a cost-shift, not a cost-removal: the toll moves from the reader to
the author/funder. It solves the access problem but raises an equity one (who can
afford to publish?) — a familiar tradeoff when you move a cost from one side of a
two-sided market to the other. Mandates like **Plan S** (funders requiring OA),
national **transformative ("read-and-publish") agreements**, and preprint servers
(arXiv since 1991; bioRxiv) are the structural interventions reshaping the market.
The library's role shifts from *buyer of access* toward *funder of publication and
operator of repositories* — a move up the value chain analogous to going from
consuming a vendor's service to running your own platform.

---

## Old World → New World

| Collection concept | Software / business equivalent |
|---|---|
| Own (purchase) vs. license | Perpetual license vs. SaaS subscription |
| Approval plan | Standing order / category subscription |
| DDA / PDA | Pay-per-use / lazy provisioning |
| Big Deal bundle | Enterprise volume contract (with lock-in) |
| Weeding (MUSTIE) | Deprecation + usage-based tiering/eviction |
| Interlibrary loan / consortia | Shared service / CDN / borrow-don't-own |
| Serials crisis | Vendor lock-in with pricing power |
| Green OA (self-archiving) | Public mirror of the artifact |
| Gold OA / APC | Cost-shift from consumer to producer |
| Institutional repository | Self-hosted artifact store (file 08) |

---

## Decision Cheat Sheet

| Situation | Approach |
|---|---|
| Deciding what to add | Collection development policy + usage data |
| Digital content, want permanence | Negotiate perpetual-access clauses (or own) |
| Want to buy only what gets used | DDA / PDA (pay-per-use) |
| Collection is stale and crowded | Weed using MUSTIE / CREW criteria |
| Can't afford to own the long tail | Resource sharing (ILL) / consortia |
| Facing runaway journal prices | Open access strategies; renegotiate the Big Deal |
| Want research free to read, no author fee | Diamond OA |
| Funder mandates open access | Plan S compliance; green or gold OA |
| Library wants to move up the value chain | Run an institutional repository (file 08) |

---

## Common Confusion Points

### "Why would a library remove books — isn't more always better?"

No — an unweeded collection degrades. Outdated, worn, superseded, and irrelevant items
make the good material harder to find, consume space and maintenance, and erode trust
(a patron who finds a 1995 medical text loses confidence). Weeding is curation, the
same discipline as deprecating dead code or tiering cold data off hot storage. A
collection is a managed portfolio, not an accumulation.

### "Open access means free — so who pays?"

Someone always pays; OA changes *who* and *when*. Gold OA typically shifts the cost
from the reader (subscription) to the author/funder (an APC). Diamond OA is funded by
institutions so neither reader nor author pays directly. Green OA is near-free because
the author self-archives an existing version. The literature becomes free to *read*;
the production cost is relocated, not eliminated.

### "Serials crisis — why can't libraries just cancel expensive journals?"

Because demand is inelastic: researchers in a field *must* have its core journals to
do and publish work, so publishers with those titles have real pricing power, and Big
Deal bundles tie must-have and marginal titles together. It is vendor lock-in on a
critical dependency with high switching costs — which is precisely why the response
had to be structural (OA mandates, transformative agreements) rather than mere haggling.

### "Buying vs. licensing — does it matter for a digital file?"

It matters enormously for preservation and continuity. A purchased copy you hold; a
licensed resource can vanish when the contract ends, the vendor changes terms, or the
platform shuts down — and you kept nothing. It is the perpetual-license-vs-SaaS risk:
licensing is cheaper and more flexible up front but leaves you with no asset and a
dependency you do not control.

### "Is deaccessioning the same as weeding?"

Related but weightier. Weeding removes re-acquirable published copies from a library —
routine. Deaccessioning removes items from an *archive* or special collection, where
records are unique and often irreplaceable (file 06) — a far more constrained, heavily
governed decision, because there is no second copy to buy back.
