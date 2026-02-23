# 04 — Antitrust Law

## Sherman/Clayton Acts, EU Competition Law, Tech Antitrust Live Cases

---

## Big Picture: Antitrust Framework

```
┌──────────────────────────────────────────────────────────────────────────┐
│                      ANTITRUST FRAMEWORK                                 │
├───────────────────────────────────────────┬──────────────────────────────┤
│  US ANTITRUST                             │  EU COMPETITION LAW          │
├───────────────────────────────────────────┼──────────────────────────────┤
│  Sherman Act §1: Restraints of trade       │  TFEU Art. 101: Agreements  │
│  Sherman Act §2: Monopolization            │  TFEU Art. 102: Abuse of    │
│  Clayton Act §2: Price discrimination      │    dominant position         │
│  Clayton Act §7: Mergers                   │  Merger Regulation (EUMR)   │
│  FTC Act §5: Unfair methods               │  DMA (Digital Markets Act)   │
├───────────────────────────────────────────┴──────────────────────────────┤
│                                                                          │
│  TWO CORE CONCERNS:                                                      │
│  1. Coordinated behavior: cartels, horizontal restraints (§1/Art.101)   │
│  2. Unilateral conduct: monopolization, abuse of dominance (§2/Art.102) │
│                                                                          │
│  RULE: protect COMPETITION, not individual competitors                   │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Sherman Act §1 — Restraints of Trade

### Per Se vs Rule of Reason

```
§1 prohibits "every contract, combination...or conspiracy in restraint of trade"
  REQUIRES: agreement between two or more separate entities (can't conspire with yourself)
  Parent-subsidiary: single enterprise doctrine; no §1 violation possible
  Intra-corporate conspiracy: generally not §1

ANALYSIS FRAMEWORK:

  PER SE ILLEGAL: certain conduct presumed anticompetitive without market analysis
    Price fixing: horizontal agreements on price (including price floors/ceilings)
    Bid rigging: coordination on competitive bids
    Market division: horizontal competitors divide markets/customers
    Group boycotts (naked): horizontal competitors agree to refuse to deal
    → Conduct is condemned categorically; no efficiencies defense available

  RULE OF REASON: weighing procompetitive vs anticompetitive effects
    Plaintiff must prove: anticompetitive harm in a relevant market
    Burden shifts to defendant: procompetitive justifications
    Burden shifts back to plaintiff: less restrictive alternative exists
    Most vertical restraints analyzed under rule of reason
    Some horizontal conduct (IP licensing, joint ventures) analyzed under RoR

  QUICK LOOK: abbreviated rule of reason for obviously anticompetitive conduct
    Without elaborate inquiry, anticompetitive effect presumed
    Defendant must provide plausible efficiency justification or lose
```

### Horizontal Restraints

```
PRICE FIXING:
  Classic cartel: competitors agree on price → eliminated competition on key parameter
  Algorithmic pricing coordination: antitrust agencies actively scrutinizing
  Hub-and-spoke conspiracy: vertical actors (hub) facilitate horizontal coordination (spokes)
    American Airlines v Sabre: potential algorithmic hub-and-spoke
    RealPage: DOJ/state AGs sued algorithmic rent price coordination (2023)

MARKET ALLOCATION:
  Customers, territories, or products divided among competitors
  Per se illegal even if competitors agree "not to compete" for efficiency reasons

INFORMATION EXCHANGE:
  Not per se illegal; analyzed under rule of reason
  Competitively sensitive: current pricing, future plans, customer-specific info
  Safer: historical, aggregate, through third party
  Trade association price reporting: antitrust risk if can facilitate coordination
```

### Vertical Restraints

```
RESALE PRICE MAINTENANCE (RPM):
  Manufacturer specifies price at which retailer must resell
  Minimum RPM: rule of reason after Leegin (2007) — overruled Dr Miles (per se)
  Maximum RPM: rule of reason after State Oil v Khan (1997)
  Most RPM procompetitive (prevents free-riding; maintains service quality)

EXCLUSIVE DEALING: customer agrees to buy only from one supplier
  Foreclosure analysis: substantial share of market foreclosed? duration?
  Generally legal if limited duration and market not dominated

TYING: conditioning sale of one product (tying product) on purchase of another (tied product)
  Per se illegal if: (1) two separate products, (2) seller has market power in tying product,
    (3) substantial commerce in tied product
  Rule of reason applied in practice (Jefferson Parish; Illinois Tool Works)
  IP tying: no presumption of market power from patent/copyright alone (Illinois Tool Works)

EXCLUSIVE TERRITORIES: manufacturer grants exclusive territorial rights to distributor
  Rule of reason; generally legal absent other anticompetitive features
  Interbrand vs intrabrand competition: protecting interbrand competition justifies
    restrictions on intrabrand competition (GTE Sylvania)
```

---

## 2. Sherman Act §2 — Monopolization

### Elements and Relevant Market

```
MONOPOLIZATION (§2):
  (1) Possession of monopoly power in a relevant market
  (2) Willful acquisition or maintenance of that power
      (as distinguished from superior product, business acumen, historical accident)

  Monopoly power: ability to control price or exclude competition
    Proxy: market share > 70% (usually sufficient)
    40-60%: depends on structural barriers, elasticity
    < 40%: rarely found to be monopoly power

  Willful acquisition: how did you get/maintain the monopoly?
    Anticompetitive conduct vs competing on the merits
    "Competing on the merits" is lawful even if competitor is harmed

RELEVANT MARKET (two dimensions):
  Product market: what products compete (define by "reasonable interchangeability")
    SSNIP test: hypothetical monopolist raises price 5-10%; do enough customers switch?
    If yes → must expand market definition (substitute available)
    Cellophane fallacy: if firm already at monopoly price, customers already substituting
      to inferior substitutes → market appears broader than competitive market would be
  Geographic market: where competition occurs (local, regional, national, global)

ATTEMPTED MONOPOLIZATION (§2):
  (1) Predatory or anticompetitive conduct
  (2) Specific intent to monopolize
  (3) Dangerous probability of success (near-monopoly territory)
```

### Exclusionary Conduct Types

```
PREDATORY PRICING:
  Prices below cost to drive out competitors; recoup afterward at supra-competitive prices
  Brooke Group test: (1) prices below appropriate measure of cost?
                     (2) dangerous probability of recouping investment?
  Rarely successful challenge (requires showing below-cost pricing + recoupment)
  Limit pricing (pricing just below entry-deterring level): usually legal

REFUSALS TO DEAL:
  Aspen Skiing: duty to deal when prior profitable course of dealing was terminated
    solely to harm competition (narrow exception to freedom to choose trading partners)
  Generally: no antitrust duty to deal with competitors (Trinko — Verizon)
  Essential facilities doctrine: not favored by SCOTUS (Trinko skepticism)

PREDATORY PRODUCT DESIGN:
  Lorain Journal: refused to sell ads to businesses that also advertised on radio
    (systematic refusal to deal to maintain monopoly in newspaper advertising)
  Leveraging monopoly to adjacent market: generally requires showing harm in adjacent market

BUNDLING/LOYALTY DISCOUNTS:
  Competitor discount only available if buyer buys substantial share from defendant
  LePage's v 3M: bundled rebates can be anticompetitive even if each product priced above cost
  Contested area; economic analysis heavily outcome-determinative
```

---

## 3. Clayton Act

```
§2 (Robinson-Patman Act): price discrimination — different prices to different buyers
  Requires competitive injury; mostly applies to commodity goods
  Rarely enforced today; viewed as protecting competitors not competition

§7 MERGERS: prohibits acquisitions where effect "may be substantially to lessen competition"
  Applies to: stock/asset acquisitions; "may be" = forward-looking (no actual harm required)

HSR ACT (Hart-Scott-Rodino Antitrust Improvements Act 1976):
  Pre-merger notification to DOJ + FTC for transactions above size thresholds
  2024 thresholds: >$119.5M (size of transaction) + size of parties tests
  30-day waiting period; Second Request = additional 30 days
  DOJ or FTC reviews (jurisdiction split based on industry history/expertise)
```

---

## 4. Merger Review

```
HORIZONTAL MERGER ANALYSIS (Merger Guidelines 2023):
  Market concentration: HHI (Herfindahl-Hirschman Index) = sum of squared market shares
    Post-merger HHI > 1,800 and delta > 100: presumptively anticompetitive
    Post-merger HHI > 2,500: highly concentrated; scrutiny
  2023 Guidelines: new presumption for mergers creating >30% market share
                   enhanced focus on multi-sided platforms, data, nascent competition

  UNILATERAL EFFECTS: merged firm can raise prices without coordination
    Diversion ratios: what fraction of sales lost by A would go to B and vice versa?
    High diversion + close substitutes = high unilateral effects

  COORDINATED EFFECTS: merger makes market more susceptible to coordination
    Factors: market concentration, transparency, homogeneous products, inelastic demand

  ENTRY ANALYSIS: would new entry constrain merged firm quickly?
    Timely (2 years), Likely, Sufficient to deter/remedy

  EFFICIENCIES DEFENSE: merger creates efficiencies that benefit consumers
    Must be merger-specific; verifiable; passed through to consumers; not from anticompetitive harm
    Courts skeptical; rarely decisively credited

VERTICAL MERGERS:
  Upstream supplier + downstream customer
  Theories: input foreclosure, customer foreclosure, access to competitively sensitive info
  2023 Guidelines: enhanced concern for vertical mergers vs prior lenient guidance

KILLER ACQUISITIONS:
  Large tech company acquires nascent competitor to eliminate potential threat
  Classic: Facebook/Instagram (2012), Facebook/WhatsApp (2014)
  FTC failed to unwind these; argued no market definition narrow enough, competition
    already reduced before it was apparent
  Policy response: 2023 Guidelines emphasize nascent competition; M&A policy shift
```

---

## 5. EU Competition Law

### TFEU Article 101 (Agreements)

```
Prohibits: agreements, decisions of associations of undertakings, concerted practices
  that have the object or effect of preventing/restricting/distorting competition
  AND affect trade between member states

OBJECT RESTRICTIONS (always illegal, no market analysis):
  Price fixing, market sharing, bid rigging, quota setting, customer allocation

EFFECT ANALYSIS: considers actual/potential competitive effects
  Less severe restrictions: assess effects on market

ARTICLE 101(3) EXEMPTION: agreement may be exempted if:
  (1) Contributes to improving production/distribution or promoting technical/economic progress
  (2) Allows consumers a fair share of resulting benefit
  (3) Does not impose restrictions indispensable to attainment of objectives
  (4) Does not afford possibility of eliminating competition for substantial part of products

Block exemptions: specific categories auto-exempted
  VBER (Vertical Block Exemption Regulation 2022): vertical agreements with <30% market share
  TTBER (Technology Transfer): IP licensing; parties below market share thresholds
  Research & Development; Specialization agreements

LENIENCY PROGRAMME: first cartel member to self-report gets immunity;
  subsequent reporters get reduced fines
```

### TFEU Article 102 (Dominance Abuse)

```
DOMINANT POSITION: market power in relevant market
  Presumption >50% market share; rare to find <40%; 25-50% with structural advantages

ABUSE CATEGORIES:
  Exploitative abuse: excessive pricing, unfair trading terms (EU enforces; US rarely does)
  Exclusionary abuse: conduct that forecloses competition
    Exclusivity; predatory pricing; margin squeeze; tying/bundling; refusal to supply
    Essential facility: dominant firm must supply access to facilities
      (distinct from US approach — Art. 102 creates broader duties to deal)

MARGIN SQUEEZE (Art. 102):
  Vertically integrated dominant firm sets wholesale prices so high that downstream
  competitors cannot profitably compete using the dominant firm's inputs
  TeliaSonera: wholesale access price + retail price by incumbent → squeeze competitors
  Not recognized as standalone antitrust theory in US (Pacific Bell v LinkLine)

FINES: up to 10% of worldwide annual turnover
  Google: multiple billion-euro fines (Shopping €2.4B/2017; Android €4.3B/2018; AdSense €1.5B/2019)
  Apple: €1.8B (2024, Spotify complaint — App Store rules)
  Qualcomm: €997M (2019, exclusivity payments to Apple)
```

---

## 6. Digital Markets Act (DMA) — EU Gatekeeper Regulation

```
In force March 2024; enforcement March 2024+

GATEKEEPERS: large tech platforms meeting thresholds:
  EU turnover ≥€7.5B or market cap ≥€75B in last 3 years
  ≥45M monthly active end users in EU; ≥10,000 annual business users
  Designated core platform services: social networks, search, OS, cloud, advertising,
    browsers, video sharing, virtual assistants, online intermediation services

OBLIGATIONS (per se; no market effects analysis needed):
  Interoperability: instant messaging interoperability required (Apple iMessage, WhatsApp)
  Data portability: allow business users to take their data
  No self-preferencing: gatekeepers cannot rank own services above competitors' in results
  No tying consent to other services
  Allow third-party app stores and sideloading (Apple major target)
  Allow business users to communicate with own customers outside platform
  Share data with business users and competitors (under defined conditions)
  No combining personal data across core platform services without consent

ENFORCEMENT:
  Up to 10% global annual turnover; 20% for repeated violations; 5% daily per diem
  Systemic infringer: structural remedies (divestiture) after 3 violations in 8 years

DESIGNATED GATEKEEPERS (2024): Alphabet (Google/YouTube/Android), Apple (iOS/Safari/App Store),
  Meta (Facebook/Instagram/WhatsApp/Messenger), Microsoft (Windows/Edge/LinkedIn/Teams),
  Amazon (Marketplace/Ads), ByteDance (TikTok), Booking.com
```

---

## 7. Key Tech Antitrust Cases (Live as of 2025)

```
US v Google (Search monopolization) — Judge Mehta ruled Google monopolist Aug 2024
  Theory: exclusive default search agreements with Apple, Android OEMs
  Remedy phase 2025: DOJ proposed forced sale of Chrome, ban on exclusivity payments
  Landmark case; first major US tech monopolization verdict in decades

US v Google (Advertising technology) — trial concluded Nov 2024
  Theory: monopolization of publisher ad server and ad exchange markets;
    acquisitions of DoubleClick, AdMeld; Project Jedi Blue coordination with Facebook
  Verdict: Google liable for monopolizing publisher ad servers + ad exchanges (2025)
  Remedy pending

FTC v Meta (Facebook/Instagram/WhatsApp) — ongoing
  FTC seeking to force divestitures of Instagram + WhatsApp
  Initially dismissed 2021; refiled; survive motion to dismiss 2022; trial 2024-2025
  Theory: Facebook monopoly in personal social networking; acquisitions preserved monopoly

DOJ v Apple (iPhone antitrust) — filed March 2024
  Theory: Apple illegally maintains iPhone monopoly by suppressing cross-platform tools,
    blocking super apps, denying cloud streaming gaming, degrading non-Apple smartwatches
  Broad theory of exclusionary conduct; ongoing

EU DMA compliance investigations (ongoing):
  Apple App Store (sideloading, browser choice, interoperability)
  Meta (pay-or-consent advertising model)
  Alphabet (Google Search self-preferencing; Google Maps)
```

---

## Decision Cheat Sheet

| Conduct | US Analysis | EU Analysis |
|---------|------------|------------|
| Price fixing with competitors | Per se illegal (Sherman §1) | Object restriction (Art. 101) |
| Exclusive dealing by dominant firm | Rule of reason; rarely condemned | Art. 102 abuse; examined carefully |
| Predatory pricing | Below cost + recoupment required | Below cost often sufficient + intent |
| Refusal to deal | Almost never antitrust duty (Trinko) | Possible duty if dominant (Art. 102) |
| Margin squeeze | Not standalone theory (US) | Art. 102 violation (EU) |
| Tying by dominant firm | Rule of reason (IP tying: no market power presumption) | Art. 102 abuse per se if dominant |
| Merger creating 40% market share | Second Request likely; efficiencies defense | Phase II investigation; Art. 2 EUMR |

---

## Common Confusion Points

**Antitrust protects competition, not competitors:** A competitor losing business to a more efficient rival is not an antitrust violation — it's competition working. Antitrust intervenes when a firm uses anticompetitive methods (not superior products/lower costs) to harm market structure.

**EU antitrust ≠ US antitrust:** EU Art. 102 is broader and more interventionist than US §2. EU requires firms to deal with competitors on essential facilities; US doesn't (Trinko). EU enforces excessive pricing (exploitative abuse); US doesn't touch pricing above competitive levels. EU has the DMA as a regulatory tool outside traditional antitrust.

**Monopoly power is not illegal per se:** Holding a monopoly because you have the best product or lowest cost is perfectly legal (United States v Grinnell). What's illegal is maintaining monopoly power through anticompetitive conduct. Microsoft's §2 violation was its exclusionary contracts, not its market share.

**Section 1 requires an agreement:** A unilateral decision not to deal with certain customers or to set certain prices is NOT a §1 violation. You need two or more separate entities agreeing. Intra-corporate coordination (parent/subsidiary) = one entity.

**Merger review is probabilistic:** Mergers are reviewed before consummation. The standard ("may substantially lessen competition") is forward-looking. Agencies and courts must predict future competitive effects, which requires economic modeling and market-structure analysis. Companies regularly litigate merger challenges.

**HHI numbers matter for merger screening:** Post-merger HHI >1,800 and delta >100 flags the deal for close scrutiny. Calculate HHI = sum of squared market shares × 10,000. Two firms with 50% each = HHI of 5,000 (highly concentrated). Delta = change from pre to post-merger HHI.
