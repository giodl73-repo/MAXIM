# 02 — IP & Patent Law

## Patent, Copyright, Trademark, Trade Secret, FOSS Licensing

---

## Big Picture: IP Landscape

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    INTELLECTUAL PROPERTY TAXONOMY                        │
├───────────────┬──────────────────┬────────────────┬───────────────────── ┤
│   PATENT      │    COPYRIGHT     │   TRADEMARK    │   TRADE SECRET       │
├───────────────┼──────────────────┼────────────────┼──────────────────────┤
│ Novel process,│ Original         │ Brand          │ Confidential         │
│ machine,      │ expression fixed │ identifiers:   │ business info        │
│ manufacture,  │ in tangible      │ names, logos,  │ with economic value  │
│ composition   │ medium           │ slogans        │ + reasonable steps   │
│               │                  │                │ to maintain secrecy  │
├───────────────┼──────────────────┼────────────────┼──────────────────────┤
│ 20 yr from    │ Life + 70 yr     │ Indefinite     │ Indefinite           │
│ filing        │ (individual)     │ (while used +  │ (while secret)       │
│               │ 95/120 yr (corp) │ enforced)      │                      │
├───────────────┼──────────────────┼────────────────┼──────────────────────┤
│ Must apply    │ Automatic on     │ Registration   │ No filing;           │
│ Registration  │ creation;        │ optional but   │ contractual/NDA      │
│ required      │ registration for │ beneficial     │ protection           │
│               │ lawsuit          │                │                      │
└───────────────┴──────────────────┴────────────────┴──────────────────────┘
```

---

## 1. Patent Law

### Patent Types

```
UTILITY PATENT: most common; protects processes, machines, manufactures, compositions
  Duration: 20 years from filing (not grant); maintenance fees required (3.5/7.5/11.5 yr)
  Exclusivity: make, use, sell, offer for sale, import

DESIGN PATENT: ornamental design of a functional item
  Duration: 15 years from grant (post-2015; formerly 14)
  No functionality component; purely aesthetic
  Examples: Apple's rounded rectangle iPhone design, Crocs shoe design

PLANT PATENT: asexually reproduced distinct and new plant variety
  Duration: 20 years from filing
  Narrow — only the specific plant variety; agricultural relevance

PROVISIONAL APPLICATION:
  Filing date placeholder; establishes priority date
  12 months to file full non-provisional application
  No examination; never granted as a patent itself
  Used to establish early priority while refining invention
```

### Patentability Requirements

```
NOVELTY (35 USC §102):
  Prior art: anything publicly disclosed before effective filing date
  Absolute novelty: any prior public use, sale, publication, patent anywhere in world
  One-year grace period (US only): applicant's own disclosures < 1 year before filing
  First-inventor-to-file system (post-AIA 2013): filing date determines priority
    (Previously: first-to-invent; interference proceedings)

NON-OBVIOUSNESS (35 USC §103):
  Would not have been obvious to a PHOSITA (person having ordinary skill in the art)
  at time of invention
  Graham v John Deere factors:
    (1) Scope and content of prior art
    (2) Differences between claimed invention and prior art
    (3) Level of ordinary skill in the art
    (4) Secondary considerations (commercial success, long-felt need, failure of others)
  KSR v Teleflex (2007): flexible analysis; combining known elements is often obvious
  Software patents particularly scrutinized for obviousness

UTILITY (35 USC §101):
  Must have specific, substantial, credible utility
  Inoperable inventions (perpetual motion machine) fail utility
  Judicial exceptions (Mayo/Alice framework — 35 USC §101):
    Laws of nature (natural phenomena, mathematical formulas): not patentable
    Abstract ideas: not patentable
    Alice Corp v CLS Bank (2014): software patent eligibility two-step:
      Step 1: Is claim directed to abstract idea?
      Step 2: Do additional elements amount to "significantly more"?
    Post-Alice: many software/business method patents invalidated
    Still eligible: specific technical improvements to computer functionality
                    concrete implementations, not just abstract ideas

ENABLEMENT (35 USC §112):
  Specification must enable PHOSITA to make and use the invention
  Written description: must show inventor possessed the invention
  Definiteness: claims must be clear enough to inform public of scope
```

### Patent Claims

```
CLAIM TYPES:
  Independent claim: complete description of invention; no reference to other claims
  Dependent claim: refers back to + narrows an independent claim (all elements of parent +)

  Method/process claim: series of steps
  Apparatus/device claim: structure
  Composition of matter: chemical formulations
  Means-plus-function (112(f)): "means for [function]" — interpreted as disclosed structure +
    equivalents; often narrower than it looks

CLAIM SCOPE:
  Doctrine of equivalents: infringement even without literal element match if
    "substantially same function in substantially same way to achieve substantially same result"
  Prosecution history estoppel: if applicant narrowed claims to get patent granted,
    cannot recapture surrendered scope via doctrine of equivalents

PATENT INFRINGEMENT:
  Direct: making, using, selling, offering for sale, importing patented invention
  Induced: actively encouraging another to infringe
  Contributory: selling material component of patented invention with knowledge of use
  Willful: knowingly infringed → up to 3× damages (enhanced damages)

PATENT DEFENSES:
  Invalidity: prove patent never should have been granted (prior art, obviousness, §101)
  Inequitable conduct: material misrepresentation/omission during prosecution (fraud on USPTO)
  License: express or implied
  Patent exhaustion: first authorized sale exhausts patent rights for that item
  Laches/equitable estoppel (limited post-SCA Hygiene)
```

### Patent Trolls / Non-Practicing Entities (NPEs)

```
NPE (patent assertion entity / "troll"):
  Acquires patents not to make products but to license/litigate
  Business model: demand licensing fees to avoid litigation costs
  Exploits: asymmetric litigation cost (demand < cost of fighting)

Legal changes to address NPEs:
  America Invents Act (AIA) 2013: IPR (Inter Partes Review) — faster, cheaper patent challenge at USPTO
    60% of challenged claims found unpatentable in IPRs
  Alice decision: invalidated many broad software patents
  TC Heartland (2017): patent cases must be filed where defendant is incorporated or
    has regular place of business (closed Eastern District of Texas venue shopping)
  Fee-shifting: 35 USC §285 — exceptional case → attorney fees (now easier post-Octane Fitness)

Software patent considerations for engineers:
  Freedom-to-operate (FTO) search before shipping product
  Patent exhaustion protects downstream purchasers
  Open source + patents: Apache 2.0 has patent grant + retaliation; GPL v3 similar
  Microsoft, Google, Amazon have large defensive patent portfolios
```

---

## 2. Copyright Law

### What Copyright Protects

```
SUBJECT MATTER: original works of authorship fixed in any tangible medium of expression
  Literary works (including software source code and object code)
  Musical works + sound recordings (separate copyrights!)
  Dramatic works, pantomimes, choreographic works
  Pictorial, graphic, sculptural works
  Motion pictures and audiovisual works
  Architectural works

ORIGINALITY: minimal creativity required; not novel (can copyright independently created work)
  "Sweat of the brow" not sufficient — requires creative spark (Feist v Rural Telephone)
  Phone book alphabetical listings: no creativity → not copyrightable
  Database: selection/arrangement may be copyrightable; raw facts are not

WHAT COPYRIGHT DOES NOT PROTECT:
  Ideas, methods, procedures, systems, mathematical principles (idea/expression dichotomy)
  Facts, data (not copyrightable; only original expression about facts)
  Titles, names, short phrases (too short for originality)
  Works in the public domain
  US government works (federal — state may differ)
```

### Copyright Duration and Formalities

```
DURATION:
  Individual author: life + 70 years
  Work for hire (corporate authorship): 95 years from publication OR 120 years from creation
  Pre-1978 works: complex rules depending on publication/registration/renewal
  "Mickey Mouse Protection Act" (CTEA 1998): extended terms; much of 20th century still protected

FORMALITIES (current law):
  Automatic: copyright exists upon creation + fixation; no registration required
  Registration: required to SUE for infringement (US works; must register first)
  Registration within 5 years of publication: presumption of validity
  Registration within 3 months of publication: statutory damages + attorney fees available
  Notice (©): no longer required (Berne Convention alignment); loss of copyright without
    notice only for pre-March-1989 publications

WORK FOR HIRE:
  Category 1: works created by employee within scope of employment → employer owns copyright
  Category 2: specially ordered/commissioned work IF falls within 9 statutory categories
    AND written agreement says "work for hire"
  9 categories: contribution to collective work, part of motion picture/AV, translation,
    supplementary work, compilation, instructional text, test, answer material for test, atlas
  Software: NOT in the 9 categories → must have Category 1 (employee) for WFH
    Contractor-written code: company needs assignment agreement (not just WFH designation)
    IMPORTANT for tech: get code assignments from contractors, not just "work for hire"
```

### Fair Use

```
Section 107 four-factor test (all factors weighed; no single decisive):
  (1) Purpose and character of the use:
      Commercial vs educational; transformative use (adds new meaning/expression)
      Transformativeness most important factor in practice
  (2) Nature of copyrighted work:
      Factual works get less protection than creative works
  (3) Amount and substantiality:
      Quantity taken; "heart of the work" matters even if small portion
  (4) Effect on the market:
      Most important factor historically; does it harm actual or potential markets?

Key fair use cases:
  Google v Oracle (2021): Google's copying of Java API declarations = fair use
    (transformative — new creative platform; only 11,500 of 2.86M lines)
  Campbell v Acuff-Rose (1994): 2 Live Crew's parody of Pretty Woman = fair use
    (commercial use not automatically unfair; parody = transformative)
  Harper & Row v Nation (1985): quoting 300 words of Ford memoir = NOT fair use
    (heart of the work; scooped first-publication market)
  AI training data: actively litigated 2023-2025; no definitive ruling yet
  <!-- @editor[content/P2]: AI training data fair use status marked 2023-2025 — verify current rulings as of 2026; NYT v OpenAI, Doe v GitHub Copilot, and others may have progressed -->
```

### Copyright in Software

```
PROTECTION:
  Source code and object code both protected as literary works
  APIs: Oracle v Google answered: structure/sequence/organization (SSO) can be
    copyrightable, but copying may be fair use
  User interfaces: look and feel sometimes protected; depends on creativity
  Functional elements: not protected (merger doctrine: only one way to express = merged)

DMCA (Digital Millennium Copyright Act, 1998):
  Anti-circumvention (§1201): illegal to circumvent TPMs (technological protection measures)
    even for noninfringing uses (limited exceptions: security research, education, etc.)
  Safe harbor (§512): ISP/platform immunity for user-generated content IF:
    (a) No actual knowledge of infringement
    (b) No financial benefit from infringement where right/ability to control
    (c) Expeditious takedown upon notification (DMCA takedown notices)
  Red flag knowledge: should have known = lose safe harbor
  DMCA takedown: rightsholders can demand removal; counter-notification process exists
```

---

## 3. Trademark Law

```
WHAT TRADEMARK PROTECTS: source identifiers — names, logos, colors, sounds, trade dress
  Functions to: identify source of goods/services and protect consumer from confusion
  (Different from patents/copyright: trademark is about CONFUSION, not copying)

DISTINCTIVENESS SPECTRUM (Abercrombie & Fitch):
  Fanciful: invented words (Kodak, Xerox, Google) — strongest protection
  Arbitrary: real words applied to unrelated goods (Apple computers, Amazon) — strong
  Suggestive: suggest quality/characteristics (Coppertone, Netflix, Microsoft) — moderate
  Descriptive: describes feature (fast, easy, cheap) — NOT registrable without secondary meaning
    Secondary meaning: consumers associate term with single source through long use
  Generic: the product category itself (aspirin, elevator, thermos) — no protection;
    Genericide: trademark becomes generic (Google as verb? contested; Band-Aid, Kleenex borderline)

REGISTRATION: USPTO (Principal Register or Supplemental Register)
  Not required but confers: nationwide constructive notice, incontestability after 5 years,
    basis for foreign registration, Customs border enforcement, right to use ® symbol
  Federal registration based on: use in interstate commerce OR intent to use (ITU)
  Common law trademark: rights from actual use; limited to geographic area of use

INFRINGEMENT: likelihood of confusion standard
  Polaroid factors (2d Cir) / Sleekcraft factors (9th Cir): similar multi-factor tests
    Strength of mark, proximity of products, similarity of marks, actual confusion,
    buyer sophistication, channels of trade, defendant's intent

DILUTION (Lanham Act §43(c)): famous marks only
  Blurring: weakening of mark's distinctiveness (Nissan.com for cars vs Nissan computers)
  Tarnishment: association with unsavory/low-quality goods

DOMAIN NAMES / CYBERSQUATTING:
  ACPA (Anti-Cybersquatting Consumer Protection Act): bad faith registration of domain
    containing distinctive/famous mark → in rem action against the domain; statutory damages
  UDRP (Uniform Domain Name Dispute Resolution Policy): ICANN arbitration process
```

---

## 4. Trade Secret Law

```
DEFINITION (DTSA + Restatement):
  Information with independent economic value from not being generally known/ascertainable
  Subject to reasonable measures to maintain secrecy

DTSA (Defend Trade Secrets Act, 2016): federal civil cause of action for trade secret misappropriation
  Prior law: patchwork of state trade secret statutes (most follow UTSA)
  DTSA: federal court jurisdiction + ex parte seizure orders + whistleblower immunity

PROTECTABLE INFORMATION: formulas, patterns, compilations, programs, devices, methods, techniques
  Customer lists, pricing information, business strategies
  Negative information (failed experiments can be trade secrets)

MISAPPROPRIATION:
  Acquisition by improper means: theft, bribery, espionage, breach of duty
  Disclosure/use with knowledge it was improperly acquired or maintained in breach of duty

REQUIREMENTS FOR PROTECTION:
  Economic value from secrecy (if public, no protection)
  Reasonable measures: NDAs, access controls, physical security, employee training
    Courts look at actual steps taken, not best possible steps

COMPARISON WITH PATENTS:
  Trade secret: indefinite protection (as long as secret); no disclosure; risk of independent discovery
  Patent: 20-year protection; public disclosure required; blocks independent inventors
  Classic choice: Coca-Cola formula (trade secret since 1886) vs patenting (would have expired ~1906)

EMPLOYEE MOBILITY AND TRADE SECRETS:
  Inevitable disclosure doctrine: employee moving to competitor inevitably uses trade secrets
    (recognized in Illinois; rejected in California)
  California's strong employee mobility policy: trade secrets law used instead of non-competes
  Non-disclosure agreements (NDAs): enforceable; no time limit if information stays secret
  Employee ownership of inventions:
    Work-for-hire: company owns inventions created in scope of employment
    Prior inventions: must be listed at hire to avoid company claiming them
    California Labor Code §2870: employee owns invention created entirely on own time
      with own resources, not related to employer's business, not using trade secrets
```

---

## Decision Cheat Sheet

| IP Type | Duration | Registration | What it Protects |
|---------|----------|-------------|-----------------|
| Utility patent | 20 yr from filing | Required (USPTO) | Novel, non-obvious process/machine/composition |
| Design patent | 15 yr from grant | Required | Ornamental appearance |
| Copyright | Life+70 / 95/120 yr | Automatic (registration to sue) | Original expression fixed in medium |
| Trademark | Indefinite (while used) | Optional (recommended) | Source identifiers; likelihood of confusion |
| Trade secret | Indefinite (while secret) | None | Confidential business info with economic value |

| Scenario | Analysis |
|----------|----------|
| Competitor uses your algorithm | Patent (if patented, not abstract idea) or trade secret |
| Competitor copies your code verbatim | Copyright infringement |
| Competitor uses a name similar to yours | Trademark infringement (likelihood of confusion test) |
| Ex-employee joins competitor | Trade secret (DTSA) + NDA; non-compete if enforceable |
| Open source project needs patent protection | Apache 2.0 or GPL v3 (both have patent grants) |
| Using GPL library in proprietary product | Static link = risky; dynamic link + LGPL = generally OK |

---

## Common Confusion Points

**Patent novelty grace period is US-only:** The US has a 1-year grace period for your own disclosures before filing. In Europe/Asia, any public disclosure before filing = prior art. If you plan international patents, file before disclosing publicly.

**Copyright protects expression, not ideas:** Two people can independently write code that does the same thing, and both can have valid copyrights. Copyright doesn't stop competition — it stops copying. The idea/expression dichotomy is fundamental.

**Trademark is about confusion, not copying:** You can have a trademark in a common word (Apple for computers). A competitor can use the word "apple" for food because no confusion about source. Trademark is consumer protection law at its core.

**Work for hire ≠ contractor assignment:** Work made by contractors is NOT automatically work for hire (software is not in the 9 WFH categories). Companies need a written assignment of copyright from contractors. Major source of corporate IP ownership gaps.

**Trade secret vs NDA:** An NDA is a contract (breach → contract damages). Trade secret protection is statutory/common law (misappropriation → DTSA damages including exemplary damages and attorney fees). NDAs and trade secrets work together but are distinct legal theories.

**Alice doesn't kill all software patents:** Alice's two-step only knocks out "abstract ideas" without "something more." Patents on concrete technical improvements to software systems (better compression algorithms with specific implementations, hardware-software interactions) survive. Over 40% of post-Alice §101 challenges still result in valid patents.
