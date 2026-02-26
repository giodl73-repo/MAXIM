# 05 — Corporate Law

## Entity Types, Fiduciary Duties, M&A Mechanics, Securities Basics, Governance

---

## Big Picture: Corporate Law Landscape

```
┌──────────────────────────────────────────────────────────────────────────┐
│                      CORPORATE LAW FRAMEWORK                             │
├──────────────────────────┬──────────────────────────┬────────────────────┤
│   ENTITY FORMATION       │   ONGOING GOVERNANCE     │   M&A / EXIT       │
├──────────────────────────┼──────────────────────────┼────────────────────┤
│  Corp / LLC / LP         │  Board of directors      │  Asset sale        │
│  Incorporation state     │  Fiduciary duties        │  Stock sale        │
│  Capitalization          │  Shareholder rights      │  Merger (fwd/rev)  │
│  Organizational docs     │  Derivative suits        │  Tender offer      │
│  Option pool / cap table │  Disclosure (SEC)        │  Going private     │
└──────────────────────────┴──────────────────────────┴────────────────────┘

Delaware: ~70% of Fortune 500 incorporated here
  Court of Chancery: specialized business court; deep corporate jurisprudence
  DGCL (Delaware General Corporation Law): highly developed, flexible
```

---

## 1. Business Entity Types

```
CORPORATION (C-Corp):
  Separate legal entity; limited liability for shareholders
  Ownership: shares of stock (common + preferred classes)
  Management: board of directors (fiduciary duty); officers (agents)
  Taxation: "double taxation" — corp pays corporate tax; shareholders pay income tax on dividends
  Public benefit corporation: allows consideration of stakeholders beyond shareholders
  IPO vehicle: almost always C-Corp (investors require it)
  VC-backed startups: C-Corp Delaware

S-CORPORATION:
  Corporation that elected pass-through taxation (no entity-level tax)
  Restrictions: ≤100 shareholders; one class of stock; US citizen/resident shareholders only
  Common for small professional businesses; not for VC funding (violates restrictions)

LIMITED LIABILITY COMPANY (LLC):
  Hybrid: limited liability + flow-through taxation (like partnership)
  No corporate formalities requirement (no board, no meetings if not desired)
  Operating Agreement: governs management/economics (can be flexible)
  Member-managed vs manager-managed
  Single-member LLC: Schedule C (disregarded entity); multi-member: Schedule K-1 (partnership)
  Tax election: can elect to be taxed as C-Corp (check-the-box)

PARTNERSHIP:
  General partnership (GP): all partners have unlimited personal liability
    Implied from joint for-profit conduct; no filing required (dangerous)
  Limited partnership (LP): general partner (management + liability) + limited partners (invest only)
    LPs: no management participation → limited liability
    LPs: passive investor vehicle (private equity funds, real estate)
  Limited liability partnership (LLP): all partners have limited liability; professional services

KEY DIFFERENCES:
                Corp          LLC          LP
Liability      Limited       Limited      LP=Limited, GP=Unlimited
Taxation       Double*       Pass-through Pass-through
Formalities    High          Low          Moderate
Raising capital Easiest      Moderate     PE fund standard
* S-Corp or REIT structures can avoid double taxation
```

---

## 2. Corporate Governance

### The Board

```
BOARD STRUCTURE:
  Directors: elected by shareholders; fiduciary duties owed to corporation (not to CEO)
  Officers (CEO, CFO, etc.): appointed by board; agents of corporation; board can fire them
  Committees: Audit, Compensation, Nominating/Governance (required by exchange listing rules)

DIRECTOR TYPES:
  Inside directors: executives who also serve on board (CEO as director)
  Outside/independent directors: no material relationship with company
  Lead independent director: when CEO also chairs board

PUBLIC COMPANY BOARD REQUIREMENTS:
  NYSE/NASDAQ: majority independent directors on board
  Audit committee: all independent; at least one financial expert
  Compensation committee: all independent (NYSE)
  Executive sessions: independent directors meet without management
```

### Fiduciary Duties

```
TWO CORE DUTIES (Delaware):
  Duty of Care: act with the care of a reasonably prudent person in similar position
    Informed decision: read materials, ask questions, seek expert advice
    Gross negligence = breach; mere negligence typically not enough

  Duty of Loyalty: act in the best interests of the corporation, not personal interests
    Self-dealing: director on both sides of transaction = conflicted
    Corporate opportunity doctrine: cannot take for yourself an opportunity that belongs to corporation
    Usurping corporate opportunities = breach regardless of whether company would have taken it

BUSINESS JUDGMENT RULE (BJR):
  Presumption that directors acted: (1) on an informed basis, (2) in good faith, (3) honestly believed
  in the best interests of the corporation
  Courts defer to board judgment if BJR presumption not rebutted
  To rebut: show fraud, bad faith, self-dealing, waste, or failure to be informed
  Effect: very difficult to win duty of care claim when BJR applies

REVLON DUTIES (change of control):
  When company is being sold for cash (auction or Revlon mode), BJR shifts to enhanced scrutiny
  Board must maximize shareholder value; must act as auctioneer to get best price
  Triggered by: cash merger with acquirer, company initiating active auction
  Not triggered by: all-stock deal where shareholders remain; controlling stockholder transactions

UNOCAL ENHANCED SCRUTINY (defensive measures):
  Board adopting takeover defense must show: (1) reasonable belief threat exists AND
    (2) response proportionate to threat
  Poison pill (rights plan): triggers when acquirer crosses threshold (e.g., 15%)
    → allows existing shareholders to buy shares at 50% discount, diluting acquirer
    → board adopts without shareholder vote; court reviews under Unocal
```

---

## 3. Shareholder Rights and Actions

```
SHAREHOLDER VOTING:
  Annual meeting: elect directors, ratify auditors, vote on proxy advisory proposals
  Extraordinary meeting: mergers, amendments to charter/bylaws, extraordinary transactions
  Record date: determines who votes
  Proxy: written authorization to vote shares; proxy statement = SEC filing (DEF 14A)
  Proxy advisory firms: ISS, Glass Lewis — recommend voting positions; huge institutional influence

DERIVATIVE SUITS:
  Shareholder sues on behalf of corporation (corp is nominal defendant; can't sue its own officers)
  Demand requirement: must first demand that board bring suit OR show demand futile
    Demand futile: majority of directors are conflicted or face substantial likelihood of personal liability
  Special Litigation Committee (SLC): board committee of independent directors can terminate derivative suit
  Business judgment rule protects SLC decision (if truly independent; Zapata test)

DIRECT vs DERIVATIVE:
  Direct: shareholder personally harmed (misrepresentation inducing purchase; denial of vote)
  Derivative: harm is to corporation; shareholder sues indirectly
  Distinction matters: standing, demand requirement, who gets recovery (corp vs shareholder)

APPRAISAL RIGHTS:
  Shareholder who votes against certain mergers can demand judicial valuation
  Court determines "fair value" of shares; shareholder gets that instead of merger consideration
  High-profile: Dell appraisal proceedings; DFC Global
  Delaware: appraisal arbitrage; sophisticated funds buy stock post-announcement to seek appraisal
  Recent Delaware reforms: allow companies to pay out merger price immediately (reduces interest)
```

---

## 4. Mergers and Acquisitions

### Deal Structures

```
ASSET ACQUISITION:
  Buyer purchases specific assets and assumes specific liabilities
  Selective liability assumption: buyer can avoid assuming unwanted liabilities
  Tax: generally step-up in basis for buyer (favorable); double tax for selling C-Corp
  Requires: assignment of every contract, license, permit (burdensome)
  Successor liability: some liabilities follow assets (products liability, environmental,
    union contracts) regardless of asset deal structure

STOCK ACQUISITION:
  Buyer purchases shares directly from shareholders
  All assets and liabilities transfer by operation of law (including unknown liabilities)
  Tax: no step-up; carryover basis; cap gains for seller (often lower rate)
  Simple transfer: stock purchase agreement; no need to assign individual contracts
  Change of control clauses: may still trigger even in stock deal (review material contracts)

STATUTORY MERGER:
  Companies combine pursuant to state merger statute (DGCL §251)
  Board approval + shareholder vote (typically)
  Surviving corporation absorbs target; target ceases to exist as legal entity
  Forward merger: target merges into acquirer (or subsidiary)
  Reverse merger: acquirer merges into target; target is survivor
  Reverse triangular merger: acquirer's subsidiary merges into target; target survives
    as wholly-owned subsidiary; popular because keeps target entity alive
    (contracts, licenses stay in entity)

TENDER OFFER:
  Acquirer makes offer directly to shareholders to purchase their shares
  Bypasses target board (hostile takeover vehicle)
  Securities laws apply: SEC filing, 20 business day open period, best price rule
  Board can respond with poison pill, white knight, pac-man defense

SPECIAL COMMITTEE:
  Required when conflicted transaction: management buyout, acquisition by controlling stockholder
  Independent directors evaluate and approve on behalf of minority shareholders
  MFW structure: controller tender offer + merger with special committee + majority-of-minority vote
    → BJR deference applies (whole foods of judicial deference)
```

### Deal Process

```
1. LETTER OF INTENT (LOI) / TERM SHEET:
   Non-binding (except exclusivity and confidentiality); outlines key terms
   Price, structure, conditions, exclusivity period (no-shop), closing timeline

2. DUE DILIGENCE:
   Legal: material contracts, litigation, IP, corporate records, regulatory compliance
   Financial: audited financials, projections, working capital
   Technical/operational: product, team, technology
   Findings → adjust price, reps/warranties, purchase price adjustments

3. DEFINITIVE AGREEMENT:
   Merger Agreement / Stock Purchase Agreement / Asset Purchase Agreement
   Representations and warranties (reps): statements of fact about the business
   Covenants: obligations between signing and closing (operate in ordinary course)
   Conditions to closing: MAE condition, regulatory approvals, financing (if LBO)
   MAE (Material Adverse Effect): defines what change allows acquirer to walk
     Post-Akorn v Fresenius (2018): very high bar; general market downturns excluded
     COVID-19 cases: most courts found MAC not triggered despite massive disruption

4. REGULATORY APPROVALS:
   HSR filing for mergers above thresholds (30-day initial waiting period)
   CFIUS (Committee on Foreign Investment in US): national security review for foreign acquirers
   SEC proxy statement (if public company shareholder vote required)

5. SHAREHOLDER VOTE / CLOSING

6. POST-CLOSING:
   Integration; earnout payments (if any); indemnification claims for rep breaches
   Escrow: holdback from purchase price for indemnification claims
   Rep & warranty insurance: policy covers rep breach claims; reduced escrow common
```

---

## 5. Securities Law Basics

```
SECURITIES ACT OF 1933 (Securities Act):
  Governs ISSUANCE (primary market) of securities
  Registration statement (S-1 for IPO) + prospectus: full disclosure required
  Section 5: unlawful to offer/sell unregistered security (unless exempt)
  Exemptions:
    Reg D §506(b): private placement to accredited investors (up to 35 non-accredited)
    Reg D §506(c): can advertise; only accredited investors; verify accreditation
    Reg A+: mini-IPO; up to $75M/year; less disclosure than full S-1
    Reg S: offers/sales outside US
    Rule 144: resale of restricted securities after holding period (6-12 months)

SECURITIES EXCHANGE ACT OF 1934 (Exchange Act):
  Governs TRADING (secondary market) and public companies
  Section 10(b) + Rule 10b-5: fraud/misrepresentation in connection with purchase or sale
  Reporting requirements: 10-K (annual), 10-Q (quarterly), 8-K (material events)
  Section 16: insiders must report and disgorge short-swing profits (<6 month round trip)

INSIDER TRADING:
  Trading on material non-public information (MNPI) while under duty
  Classical theory: corporate insider trades on own company's MNPI
  Misappropriation theory: outsider misappropriates information from source with duty
    (SEC v O'Hagan: lawyer used client's deal info to trade in target)
  Tipper/tippee liability: tipper breaches duty + receives personal benefit; tippee who knows
    can be liable

REGULATION FD (Fair Disclosure):
  Public companies cannot selectively disclose material information to analysts/investors
  Must publicly disclose simultaneously; if accidental, must promptly file 8-K

ACCREDITED INVESTOR:
  Individual: income >$200K ($300K joint) last 2 years, OR net worth >$1M (excluding home)
  OR certain professional certifications (Series 7/65/82 licensees added 2020)
  Entity: assets >$5M, or all equity owners are accredited investors
```

---

## 6. Capital Structure and Startup Financing

```
COMMON STOCK: residual claim; voting rights; last to be paid in liquidation

PREFERRED STOCK: various liquidation preferences + special rights
  Participating preferred: get preference THEN participate pro-rata with common (double-dip)
  Non-participating: preference OR common value, whichever greater
  Liquidation preference: 1× (return of investment first), 2× (double, less common post-2009)
  Cumulative dividends: accrue if not paid
  Anti-dilution: protect against down rounds
    Full ratchet: reprices all shares to new round price (brutal for founders)
    Weighted average: partial adjustment based on size of new issuance (common today)

OPTION POOL:
  Reserved shares for employee stock options
  Typically 10-20% of fully-diluted; created pre-financing (shifts dilution to founders)
  ESOP cliff: typically 1-year cliff + 4-year monthly vest

CAP TABLE:
  Records all equity ownership: founders, investors, option pool, warrants
  Fully-diluted: includes all potentially issuable shares (options, warrants, convertibles)
  Pro-forma post-money: after investment closes

VC FINANCING ROUNDS:
  Pre-seed → Seed (SAFEs, convertible notes) → Series A → B → C... → Exit
  SAFE (Simple Agreement for Future Equity): converts at future priced round
    Discount rate (typically 20%) or valuation cap → investor benefit on conversion
    Post-money SAFE (YC standard): simpler math; investors know their ownership
  Convertible note: debt that converts; interest accrues; maturity date triggers payment/conversion

DILUTION MECHANICS:
  Pre-money valuation: $10M
  New investment: $2M
  Post-money valuation: $12M
  Investor ownership: $2M / $12M = 16.7%
  Existing owners: diluted to 83.3% of prior ownership × prior % = adjusted %
```

---

## Decision Cheat Sheet

| Scenario | Analysis |
|----------|----------|
| CEO wants to acquire competitor; CEO is a major shareholder | Interested transaction → board conflict → special committee + independent approval; enhanced scrutiny or entire fairness |
| Company selling itself to private equity | Revlon mode → maximize shareholder value; fairness opinion; market check |
| Director takes business opportunity for personal benefit | Duty of loyalty violation; corporate opportunity doctrine; rescission + disgorgement |
| VC wants convertible note with 20% discount | Converts at 80% of Series A price; favors investor if cap not triggered |
| Founder leaving 2 years in (4yr/1yr vest) | 2 years × 1/48 = 24/48 = 50% vested |
| Asset deal vs stock deal | Asset: selective liability; stock: simpler transfer but all liabilities follow |
| Hostile acquirer threatens 20% stake | Board may adopt poison pill (rights plan) if threat exists and response proportionate |
| Minority shareholder in merger alleges unfair | Demand on board (unless futile); derivative suit OR appraisal if voted against |

---

## Common Confusion Points

**Delaware law ≠ the corporation's home state:** Delaware is the dominant state for incorporation because of its developed courts and statutes, but you can incorporate in any state. A Delaware corporation with all operations in California still has to comply with California employment, environmental, and securities laws — it's just governed by DGCL internally.

**Business judgment rule doesn't protect self-dealing:** BJR creates deference for disinterested decisions by disinterested directors. Conflicted transactions (director on both sides) get no BJR protection — instead reviewed under entire fairness (fair price + fair process). That's much harder to satisfy.

**Revlon mode isn't a rule about price:** Revlon v MacAndrews created a duty to maximize shareholder value in a cash-out merger. It doesn't prohibit blocking a deal — boards can say no to buyouts. It means once you decide to sell, run an adequate process. The trigger (cash deal) matters more than the price itself.

**Preferred stock economics are complex:** "2× participating preferred with a $10M liquidation preference" means investors get $20M before founders see anything, THEN participate in the remainder. In a $15M exit: investors get $15M; founders get nothing. In a $100M exit: investors get $20M + their pro-rata share of $80M. Model your waterfall before accepting terms.

**Insider trading "material" is broader than you think:** Material information = substantial likelihood a reasonable investor would consider it important in making an investment decision. Upcoming merger announcements, earnings surprises, major contract wins/losses, FDA approval/rejections — all material. "No one will know" is not a defense.

**SAFEs are equity, convertible notes are debt:** A SAFE (YC's post-money SAFE) is technically not a security that accrues interest or has a maturity date — it's a right to receive equity at a future round. Convertible notes accrue interest and have a maturity date (creating pressure to close a priced round or pay back). Both convert at priced round; SAFEs are simpler.
