# 01 — Contract Law

## Formation, Breach, Remedies, UCC, Software Licensing

---

## Big Picture: Contract Law Landscape

```
┌──────────────────────────────────────────────────────────────────────────┐
│                       CONTRACT LAW FRAMEWORK                             │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  FORMATION          ENFORCEABILITY       PERFORMANCE       BREACH        │
│  ─────────          ─────────────        ───────────       ──────        │
│  Offer              Consideration        Conditions        Material       │
│  Acceptance         Capacity             Excuse            Minor          │
│  Meeting of minds   Legality             Impossibility     Anticipatory   │
│                     Statute of Frauds    Frustration                     │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  COMMON LAW (services, real estate) vs UCC Article 2 (goods)             │
│  REMEDIES: expectation / reliance / restitution / specific performance   │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Contract Formation

### Offer

```
Offer: manifestation of willingness to enter into a bargain, so made as to
       justify another person in understanding that their assent will conclude it

Requirements:
  Definite terms: parties, subject matter, price, quantity, time
                  (UCC: quantity is the essential term for goods contracts)
  Communication to offeree
  Intent to be bound (objective standard — "reasonable person" not subjective)

What is NOT an offer:
  Advertisements: generally invitations to make an offer
    Exception: specific, limited-quantity ads with clear terms (Lefkowitz)
  Price quotes: usually preliminary negotiations
  Letters of intent: generally non-binding (unless clearly intended to bind)

Termination of offer:
  Lapse of time (stated period or reasonable time)
  Rejection or counter-offer by offeree
  Revocation by offeror (anytime before acceptance, generally revocable)
  Death or incapacity of either party
  Irrevocable offers:
    Option contracts: consideration paid to hold offer open
    Firm offer (UCC §2-205): merchant's signed written offer ≤3 months irrevocable
```

### Acceptance

```
Mirror image rule (common law): acceptance must exactly match terms of offer
  Counter-offer: rejects original offer + creates new offer
  Conditional acceptance: "I accept if you agree to X" → counter-offer

UCC §2-207 (Battle of the Forms): different rule for goods
  Acceptance valid EVEN IF it states different or additional terms
  Additional terms between merchants → become part of contract UNLESS:
    (a) offer expressly limits acceptance to its terms
    (b) material alteration
    (c) offeror objects within reasonable time
  Different terms: "knockout rule" (majority) — conflicting terms cancel out;
                   UCC gap-fillers supply the term
  Conduct alone can establish a contract even if writings don't agree

Mailbox rule: acceptance effective on dispatch (mailing), not receipt
  Revocation: effective on receipt
  Email: generally effective on receipt (not dispatch)
  Offeror can specify acceptance method

Unilateral contract: accepted by performance, not promise
  Start of performance = acceptance; offer cannot be revoked mid-performance
  Bilateral contract (most): promise for promise
```

### Consideration

```
Definition: bargained-for exchange; legal detriment to promisee OR benefit to promisor

Legal detriment: doing something you had no prior obligation to do, OR
                 refraining from something you had a right to do

What does NOT constitute consideration:
  Past consideration: prior acts cannot support a new promise
  Pre-existing duty rule: promise to do what you already owe is no consideration
    Exception UCC §2-209: modification of goods contract needs no new consideration
  Illusory promises: "I'll buy if I feel like it" — no real obligation, no consideration
  Nominal consideration: courts split on $1 for valuable property

Promissory estoppel (§90 Restatement):
  Promise made; promisor should reasonably expect reliance
  Promisee actually and justifiably relies to their detriment
  Injustice can only be avoided by enforcement
  Damages may be limited to reliance interest (not full expectation)
  Substitutes for consideration in appropriate cases
```

---

## 2. Defenses to Enforcement

```
CAPACITY:
  Minors: voidable by minor (not void); can disaffirm; must pay for necessaries
  Mental incapacity: voidable if couldn't understand nature/consequences at formation
  Intoxication: voidable if other party knew or should have known

MUTUAL ASSENT DEFECTS:
  Mutual mistake: both parties mistaken about a material fact at formation
    → voidable by adversely affected party (unless they assumed the risk)
  Unilateral mistake: generally no defense
    Exception: other party knew or should have known of mistake
  Fraud: intentional misrepresentation of material fact → rescission + tort damages
  Innocent misrepresentation: rescission only
  Duress: improper threat that leaves no reasonable alternative
  Undue influence: inappropriate pressure in relationship of trust/confidence

ILLEGALITY: contracts contrary to law or public policy = void ab initio
  Covenant not to compete: valid if (1) ancillary to legitimate transaction,
    (2) reasonable in scope (time/geography/activity), (3) protects legitimate interest
    California exception: broad prohibition on non-competes (Business & Professions Code §16600)
    Post-2024 FTC rule attempted nationwide ban; enjoined by courts (ongoing)

UNCONSCIONABILITY:
  Procedural: oppressive process (fine print, no choice, unequal bargaining power)
  Substantive: oppressive terms
  Courts require both (generally); may refuse enforcement, strike clause, or limit it

STATUTE OF FRAUDS: certain contracts must be in writing
  MY LEGS: Marriage / Year (not performable within 1 year) / Land / Executor /
           Goods (UCC ≥$500) / Surety (promising to pay another's debt)
  Exceptions: part performance, promissory estoppel, merchant confirmation memo (UCC)
```

---

## 3. Contract Interpretation

```
Parol evidence rule: written final integrated agreement cannot be contradicted by
  prior oral/written evidence

Complete integration: no contradicting or adding terms
Partial integration: cannot contradict; may add consistent additional terms
Exceptions (parol evidence allowed):
  Ambiguity, fraud/mistake/illegality defenses, conditions precedent to effectiveness,
  collateral agreements (separate consideration), trade usage/course of dealing (UCC)

Contra proferentem: ambiguity construed against the drafter
  (Contracts of adhesion: insurance, consumer agreements — heavily applied)

Implied duty of good faith and fair dealing (UCC §1-304; Restatement §205):
  Every contract imposes duty to exercise rights in good faith
  Cannot use contract power to deprive other party of benefit of the bargain
  Example: exclusive distribution contract — cannot fail to use reasonable efforts to sell
```

---

## 4. Performance and Discharge

```
CONDITIONS:
  Condition precedent: event that must occur before duty to perform arises
  Condition subsequent: occurrence that extinguishes an already-arisen duty
  Concurrent conditions: duties trigger simultaneously (payment + delivery)
  Satisfaction: waived if party prevents condition from occurring

PERFORMANCE STANDARDS:
  Perfect tender rule (UCC): buyer can reject for ANY defect in goods or delivery
    Seller cure right: can cure within contract time or reasonable additional period
    Installment contracts exception: material nonconformity required for rejection
  Substantial performance (common law services): breach if material;
    minor defects → contract price minus cost to remedy

DISCHARGE:
  Impossibility: supervening event makes performance objectively impossible
    (destruction of specific subject matter, death of personal services person)
  Commercial impracticability (UCC §2-615): unforeseen contingency + not assumed risk
    Price increase alone rarely sufficient; war, embargo, crop failure = classic cases
  Frustration of purpose: purpose frustrated even though performance still possible
    Classic: Krell v Henry (Coronation cancelled → hotel room contract frustrated)
  Mutual rescission: both parties agree to discharge
  Accord and satisfaction: new agreement + performance discharges original obligation
```

---

## 5. Breach and Remedies

### Types of Breach

```
MATERIAL BREACH:
  Substantially defeats the purpose of the contract
  Non-breaching party: suspend own performance + treat contract as discharged + sue
  Factors: benefit received, extent of performance, likelihood of cure, compensation adequacy

MINOR BREACH:
  Non-breaching party must continue performance; may sue for actual damages

ANTICIPATORY REPUDIATION:
  Unequivocal statement that party will not perform before due date
  Non-breaching party may: sue immediately, suspend own performance, or wait
  UCC: may demand adequate assurance; failure to provide = repudiation
```

### Damages

```
EXPECTATION DAMAGES (default; "benefit of the bargain"):
  = Loss in value + incidental/consequential losses − costs avoided − losses avoided
  Puts non-breaching party in position as if contract performed

CONSEQUENTIAL DAMAGES:
  Foreseeable at time of contracting — Hadley v Baxendale test
  "Reasonably contemplated by both parties at time of contracting"
  Routinely disclaimed in commercial contracts

INCIDENTAL DAMAGES:
  Costs of dealing with breach (finding a replacement, storage, inspection)

RELIANCE DAMAGES:
  Expenses incurred in reliance on the contract
  Alternative when expectation unproven (new ventures without profit history)

RESTITUTION:
  Value of benefit conferred on breaching party; prevents unjust enrichment
  Available even to a breaching party up to contract value

LIQUIDATED DAMAGES:
  Enforceable if: (1) damages difficult to estimate at contracting time AND
                  (2) amount is a reasonable pre-estimate (not a penalty)
  Penalty clauses: void in common law jurisdictions

MITIGATION:
  Non-breaching party must take reasonable steps to minimize losses
  Cannot recover losses that reasonable mitigation would have prevented
  Employee wrongfully terminated: must seek comparable employment

SPECIFIC PERFORMANCE:
  Equitable remedy; available when money damages inadequate
  Real property (always — land is unique)
  Unique goods (rare items, custom software, bespoke works)
  Personal services: NEVER (13th Amendment concerns; courts won't force someone to work)
```

---

## 6. UCC Article 2 — Sale of Goods

```
SCOPE: transactions in "goods" (movable tangible personal property)
  Mixed goods/services: predominant purpose test (majority rule)
  Software: split of authority; some courts apply UCC by analogy

KEY UCC MERCHANT RULES (merchant = person dealing in goods of that kind):
  Firm offer: merchant's signed written offer ≤3 months irrevocable without consideration
  Battle of forms §2-207: additional terms between merchants become part of contract
  Confirmatory memo: signed written confirmation binds merchant who doesn't object in 10 days
  Good faith: merchants = honesty in fact + commercially reasonable standards

IMPLIED WARRANTIES:
  Merchantability: goods fit for ordinary purpose for which they're used
    Automatic from merchant seller; cannot easily disclaim
    Disclaimer: "as is" or specific language mentioning merchantability
  Fitness for particular purpose: if seller knows buyer's specific purpose and
    buyer relies on seller's skill/judgment to select goods
    Disclaimer: "as is" or general fitness disclaimer

RISK OF LOSS:
  No breach by seller:
    FOB shipping point: risk to buyer when seller delivers to carrier
    FOB destination: risk to buyer when tender at destination
  Breach by seller: risk remains on seller until cure or acceptance
  Sale on approval / sale or return: risk on seller (approval) or buyer (return)

BUYER'S REMEDIES on seller breach:
  Reject nonconforming goods (must be seasonably done; state defects)
  Revoke acceptance (if defect substantially impairs value; hard to discover initially)
  Cover: buy substitute + recover difference + incidental/consequential
  Damages without cover: market price at time learned of breach − contract price

SELLER'S REMEDIES on buyer breach:
  Withhold delivery; resell + recover difference + incidental
  Sue for price (if resale impractical; if identified goods can't be resold)
  Lost profits (lost volume seller: would have made 2 sales instead of 1)
```

---

## 7. Software Licensing

### SaaS / Cloud Contract Terms

```
SAAS AGREEMENT STRUCTURE:
  Subscription: right to access service for defined term; not a purchase
  Automatic renewal: common; watch for evergreen clauses (auto-renew unless notice)
  Seats vs usage: per-seat pricing (headcount) vs consumption-based (API calls, compute)
  Enterprise vs SMB: different SLAs, support, data handling, customization rights

SLA (Service Level Agreement):
  Uptime commitment: typically 99.9% (8.7 hrs/yr downtime) to 99.99% (52 min/yr)
  Measurement: often monthly, not annual; often excludes scheduled maintenance,
    force majeure, third-party failures (cloud substrate, BGP routing, DNS)
  Remedy: typically service credits (5-25% of monthly fee) — NOT actual damages
  Important: service credits ≠ actual damages; if downtime costs you $1M and SLA
    gives you $5K in credits, the SLA caps your practical remedy unless contract says otherwise
  Carve-out for consequential damages: check whether SLA remedy is your only recourse

DATA PORTABILITY AND LOCK-IN:
  Right to export your data before or after termination
  Export format: CSV/JSON/standard format vs proprietary format (lock-in risk)
  Transition period: vendor access after termination to allow migration
  Data deletion: when does vendor delete your data after termination?
    Key question: does deletion apply to backups? (30/60/90 day backup retention common)
  Data residency: contractual commitments to keep data in specific geography (EU/US/APAC)

VENDOR LOCK-IN PROVISIONS (watch for):
  Termination-for-convenience penalties (exit fees, breakage)
  Minimum commit terms (3-year deals with heavy discounts)
  IP ownership of derived works or configurations
  Source code escrow (if SaaS goes dark — vendor provides source code to escrow agent)

OWNERSHIP AND LICENSING TERMS:
  Customer data: customer retains ownership; vendor gets license to process only
  Derived data/aggregated insights: watch for vendor rights to anonymized usage data
  Customer configurations/IP: customizations, training data, model outputs — who owns?
  Work product in professional services: separate from SaaS license; needs explicit assignment
```

```
LICENSE vs SALE DISTINCTION:
  Vernor v Autodesk: if licensor retains title and significantly restricts use → license, not sale
  First Sale Doctrine: only applies to copies "sold" not licensed → can't resell licensed software
  SaaS/cloud: no copy at user's end; clearly a license/service, not a sale

OPEN SOURCE LICENSE TAXONOMY:

  PERMISSIVE (minimal restrictions):
    MIT: use/modify/distribute; include copyright notice + license text
    BSD 2-clause: same as MIT essentially
    BSD 3-clause: adds no-endorsement clause (cannot use project name to endorse)
    Apache 2.0: permissive + explicit patent grant; includes NOTICE file requirement

  WEAK COPYLEFT (conditional):
    LGPL v2.1 / v3: copyleft if you modify the library itself; dynamic linking permitted
    MPL 2.0 (Mozilla): file-level copyleft; modifications to MPL files must stay MPL

  STRONG COPYLEFT:
    GPL v2: derivative works must be GPL; source disclosure on distribution
    GPL v3: adds patent retaliation clause; anti-tivoization
    AGPL v3: GPL v3 + network use triggers copyleft (closes SaaS loophole)

  COMPATIBILITY MATRIX (key entries):
    MIT → GPL: compatible (MIT code in GPL project OK)
    Apache 2.0 → GPL v3: compatible
    Apache 2.0 → GPL v2: INCOMPATIBLE (patent clause)
    GPL → MIT: NO (GPL cannot be relicensed as MIT)
    GPL v2 → GPL v3: NOT automatically compatible (different versions)

WHAT TRIGGERS GPL COPYLEFT:
  "Distribution" of a binary containing GPL code to outside parties
  Static linking: generally triggers copyleft
  Dynamic linking (shared library): LGPL allows; GPL debated; depends on context
  SaaS: NOT distribution under GPL v2 → no copyleft obligation
  SaaS: IS considered distribution under AGPL v3 → copyleft obligation

PATENT CLAUSES:
  Apache 2.0: explicit patent grant from contributors to users; patent retaliation
  GPL v3: implicit patent peace clause
  MIT/BSD: no patent license; patent holder could still sue despite MIT license

DUAL LICENSING:
  Copyright owner can license same code under multiple licenses
  Used commercially: AGPL (free) + proprietary (paid, no copyleft obligations)
  Examples: MySQL (GPL + commercial), Qt (LGPL + commercial)
```

---

## Decision Cheat Sheet

| Scenario | Rule |
|----------|------|
| Buyer adds terms in goods contract acceptance | UCC §2-207: additional terms between merchants = part of contract unless material alteration |
| Oral contract for $600 of goods | Void under UCC SoF; exceptions: part performance, merchant memo, admission |
| Employee relies on oral promise to their detriment | Promissory estoppel may substitute for consideration |
| Seller fails to deliver; buyer wants lost profits | Consequential damages if foreseeable; likely disclaimed in B2B contracts |
| Specific performance for unique software system | Equity may grant it if damages inadequate and system truly unique |
| GPL vs Apache 2.0 license compatibility | GPL v3 + Apache 2.0 = compatible; GPL v2 + Apache 2.0 = incompatible |
| SaaS product using GPL library | No copyleft triggered (not distributing); AGPL triggers for network use |
| Non-compete enforceability | Generally valid if reasonable scope/time; void in California |

---

## Common Confusion Points

**Mirror image vs UCC §2-207:** Common law requires perfect acceptance match. UCC §2-207 (goods) allows acceptance even if terms differ — additional terms may become part of the contract between merchants. Know which governs (goods = UCC; services = common law).

**Consideration for modifications:** Common law requires new consideration for contract modifications (pre-existing duty rule). UCC §2-209 requires only good faith. Services contracts modified mid-stream need to watch for this.

**Consequential damages disclaimers:** Nearly universal in commercial software/SaaS agreements. "In no event shall either party be liable for indirect, incidental, special, or consequential damages." This is enforceable between sophisticated commercial parties. Read your contracts.

**GPL "viral" nature and what triggers it:** Distribution is the trigger — putting GPL code in a binary and giving it to someone outside your organization. Purely internal use of GPL code does not trigger copyleft. SaaS delivery does not trigger GPL v2 copyleft (no distribution) — but AGPL v3 explicitly treats network use as distribution.

**Promissory estoppel vs contract:** Promissory estoppel is not a contract; it's an equitable substitute for consideration when strict contract formation fails. Damages may be limited to reliance interest (not full expectation). Courts use it to prevent injustice, not to enforce every oral promise.

**Liquidated damages vs penalty:** Courts ask: at time of contracting, was it a genuine attempt to pre-estimate actual damages? If it looks like a punishment (wildly disproportionate to likely harm), it's a void penalty. Modern trend: enforce unless clearly punitive.
