# 03 — Privacy & Data Law

## GDPR, CCPA, HIPAA, Data Breach Notification, Cross-Border Transfers

---

## Big Picture: Privacy Law Landscape

```
┌──────────────────────────────────────────────────────────────────────────┐
│                     PRIVACY REGULATORY MAP                               │
├───────────────────────┬──────────────────────────────────────────────────┤
│  JURISDICTION         │  KEY LAWS                                        │
├───────────────────────┼──────────────────────────────────────────────────┤
│  European Union (EU)  │  GDPR (2018) — comprehensive                    │
│                       │  ePrivacy Directive (cookies/tracking)           │
│                       │  AI Act (2024) — AI-specific                     │
├───────────────────────┼──────────────────────────────────────────────────┤
│  United States        │  Sectoral approach: HIPAA, FERPA, COPPA, GLBA   │
│  (federal)            │  No comprehensive federal privacy law (Feb 2026) │
│                       │  APRA (American Privacy Rights Act): passed House│
│                       │  committee 2024; stalled in Senate as of Feb 2026│
│                       │  FTC Act §5: deceptive/unfair practices          │
│                       │  ECPA: electronic communications interception    │
├───────────────────────┼──────────────────────────────────────────────────┤
│  US States            │  CCPA/CPRA (California), CPA (Colorado),        │
│                       │  VCDPA (Virginia), CTDPA (Connecticut),          │
│                       │  20+ state laws enacted or pending               │
├───────────────────────┼──────────────────────────────────────────────────┤
│  Other major          │  PIPEDA (Canada) → CPPA in progress             │
│                       │  LGPD (Brazil), POPIA (South Africa)             │
│                       │  APPI (Japan), PDPA (Singapore/Thailand)         │
└───────────────────────┴──────────────────────────────────────────────────┘
```

---

**Formal bridge:** Privacy law is a risk management and access control specification
layered on top of data systems. The mental model shift: legal compliance is not
about a compliance checklist — it's about encoding constraints into system design.
GDPR's "privacy by design" principle (Art. 25) is a direct mandate to implement
data minimization, purpose limitation, and access control at the architecture level
rather than as an afterthought. A DPIA (Data Protection Impact Assessment, Art. 35)
is a required risk assessment before deploying high-risk processing — structurally
identical to threat modeling. Lawful basis documentation maps to access control
policy documentation: you must identify and record the authorization basis for
every category of data processing, not just assume permission. SOC 2 / ISO 27001
cover security (confidentiality, integrity, availability); GDPR additionally
mandates lawfulness, purpose limitation, minimization, and data subject rights —
each of which creates engineering requirements (audit logs for access requests,
deletion workflows, portability APIs, consent management platforms).

## 1. GDPR — General Data Protection Regulation

### Scope and Key Definitions

```
TERRITORIAL SCOPE (Art. 3) — extraterritorial reach:
  (1) Establishment principle: processing by controller/processor established in EU
  (2) Targeting principle: offering goods/services to EU data subjects
                           OR monitoring behavior of EU data subjects
  → US company with no EU presence that has EU users = GDPR applies

PERSONAL DATA: any information relating to an identified or identifiable natural person
  Name, email, IP address, cookie ID, device ID, location data
  Special categories (Art. 9): racial/ethnic origin, political opinions, religious beliefs,
    trade union membership, genetic/biometric data, health data, sex life/orientation
    → Requires explicit consent or other specific legal basis; higher penalties

KEY ROLES:
  Controller: determines purposes and means of processing (the company deciding why/how)
  Processor: processes data on behalf of controller (SaaS vendor, cloud provider)
    Processor needs a Data Processing Agreement (DPA) from controller
  Joint controllers: two+ controllers jointly determine purposes and means
  Data Protection Officer (DPO): required for public authorities, large-scale systematic
    monitoring, large-scale special category data
```

### Six Lawful Bases for Processing (Art. 6)

```
1. Consent: freely given, specific, informed, unambiguous, affirmative action required
   Withdrawal must be as easy as giving consent
   Bundled consent (take it or leave it) often invalid
   Pre-ticked boxes: not valid consent
   NOT required for legitimate activities (most B2B processing uses other bases)

2. Contract: processing necessary for performance of contract with data subject
   Or pre-contractual steps at data subject's request

3. Legal obligation: processing required by EU/member state law

4. Vital interests: protect life where data subject incapable of giving consent

5. Public task: official authority; public interest task laid down by law

6. Legitimate interests (Art. 6(1)(f)): THREE-PART TEST:
   (a) Identify legitimate interest
   (b) Necessity: is processing necessary for that interest?
   (c) Balancing: do data subject interests/rights override?
   Most B2B/analytics processing rests here; cannot use for special categories
   Must document this analysis
```

### Individual Rights (Arts. 15–22)

```
Right of access (Art. 15): data subjects can request copy of their data + supplementary info
  Response: within 1 month (extensible to 3); generally free (first copy)

Right to rectification (Art. 16): correct inaccurate or incomplete data
  Response: 1 month

Right to erasure / "right to be forgotten" (Art. 17):
  No longer necessary for purpose; consent withdrawn; data unlawfully processed; legal obligation
  NOT absolute: overrides legitimate interests, legal claims, freedom of expression
  Technical challenge: data in backups, data shared downstream

Right to restriction (Art. 18): limit processing while contesting accuracy or legitimacy

Right to data portability (Art. 20): receive own data in machine-readable format; transmit to another
  Only applies to consent or contract basis; only data "provided by" data subject

Right to object (Art. 21): object to processing based on legitimate interests or public task
  MUST stop unless compelling legitimate grounds overriding data subject interests
  Direct marketing: absolute right to object; must stop

Rights re automated decision-making (Art. 22): right not to be subject to solely automated
  decisions with significant effects (including profiling for credit, employment, etc.)
  Exceptions: contract, law, explicit consent; but human review must be available

Response timeline: 1 month; extensible to 3 months for complex/numerous requests
Denied: must tell why; data subject can complain to DPA or sue
```

### Security, Breach, Enforcement

```
SECURITY (Art. 32):
  Appropriate technical and organizational measures (TOMs)
  Risk-based approach; encryption/pseudonymization, availability/integrity, testing

BREACH NOTIFICATION (Art. 33/34):
  Notify supervisory authority: 72 hours of becoming aware (unless no risk to individuals)
  Notify individuals: without undue delay if HIGH risk to their rights/freedoms
  "Becoming aware": when processor notifies controller (not when breach first occurs)
  What to include: nature of breach, categories/approximate numbers, consequences,
    measures taken or proposed

ENFORCEMENT:
  Fines (Art. 83):
    Tier 1: up to €10M or 2% global annual turnover (whichever higher)
      For: processor violations, certification bodies, monitoring bodies
    Tier 2: up to €20M or 4% global annual turnover
      For: basic principles, consent, data subject rights, international transfers
  Notable fines:
    Meta (Facebook): €1.2B (2023) — unlawful data transfers to US
    Amazon: €746M (2021) — cookie/tracking consent
    WhatsApp: €225M (2021) — transparency violations
    Google: €50M (2019) — first major GDPR fine

SUPERVISORY AUTHORITIES: each EU member state has one (UK: ICO; Germany: multiple Länder-level)
  One-stop-shop: lead DPA for companies with main EU establishment
    → Meta's lead DPA: Ireland DPC (until recent enforcement coordination)
  EDPB (European Data Protection Board): consistency/guidance/dispute resolution
```

### International Data Transfers

```
MECHANISMS (Art. 44-49) — transfers to "third countries" (outside EEA):

ADEQUACY DECISION: EU Commission finds country has equivalent protection
  Current adequate countries: UK (post-Brexit), Japan, Canada (PIPEDA scope), Switzerland,
    Israel, New Zealand, Argentina, South Korea
  US: EU-US Data Privacy Framework (DPF, July 2023 — third attempt after Schrems I, II)
    Companies self-certify to DPF principles; DOC administers; enforceable by FTC
    Schrems III may be filed; legal uncertainty continues

STANDARD CONTRACTUAL CLAUSES (SCCs): pre-approved contract terms
  New 2021 SCCs replaced old ones; must use new ones
  Controller-to-controller, controller-to-processor, processor-to-processor versions
  Transfer Impact Assessment (TIA): required; assess destination country's laws

BINDING CORPORATE RULES (BCRs): intra-group transfers for multinationals
  Approved by lead DPA; lengthy process (1-2 years); covers all group entities

DEROGATIONS (Art. 49): explicit consent, contract performance, vital interests, public interest
  Not for systematic/repetitive transfers; "gateway of last resort"
```

---

## 2. CCPA / CPRA (California)

```
CCPA (2018) + CPRA amendments (2020, effective 2023):
  Applies to for-profit businesses doing business in California that:
    Annual gross revenue > $25M OR
    Buy/sell/receive/share ≥100,000 consumers' or households' personal info OR
    Derive ≥50% revenue from selling personal info

  Not applicable to: nonprofits, some employee/B2B data (though expanded under CPRA)

CONSUMER RIGHTS:
  Right to know: categories and specific pieces of personal info collected
  Right to delete: request deletion (with exceptions)
  Right to opt-out of sale: "Do Not Sell My Personal Information" link required
  Right to non-discrimination: no degraded service for exercising rights
  CPRA additions:
    Right to correct inaccurate personal info
    Right to limit use of sensitive personal info
    Right to know about automated decision-making

SENSITIVE PERSONAL INFORMATION (SPI) — new CPRA category:
  SSN, financial account credentials, precise geolocation, racial/ethnic origin,
  religious beliefs, union membership, health/sex life/sexual orientation data,
  genetic data, private communications
  Consumers can direct businesses to limit SPI use to necessary purposes

SALE vs SHARING:
  "Sale": exchange for monetary or other valuable consideration
  "Sharing" (CPRA): cross-context behavioral advertising; opt-out right extends to sharing

ENFORCEMENT:
  CPPA (California Privacy Protection Agency): regulatory authority
  AG enforcement: civil penalties up to $7,500 per intentional violation
  Private right of action: ONLY for data breaches (§1798.150)
    $100-$750 per consumer per incident or actual damages
```

---

## 3. HIPAA (Health Insurance Portability and Accountability Act)

```
SCOPE: covered entities + business associates handling PHI
  Covered entities: health plans, healthcare clearinghouses, healthcare providers
    (that transmit electronic PHI in HIPAA transactions)
  Business associates: vendors handling PHI on behalf of covered entity
    BAA (Business Associate Agreement) required before sharing PHI
    Cloud providers, SaaS vendors, billing companies, IT support = BAs

PHI (Protected Health Information):
  Individual health information + any of 18 HIPAA identifiers (name, date, zip, phone, etc.)
  De-identified data: 18 identifiers removed (Safe Harbor) OR expert determination
  Limited data set: some identifiers removed; can be used for research/public health
    with DUA (Data Use Agreement)

PRIVACY RULE (Standards for Privacy of PHI):
  Minimum necessary: only PHI needed for specific purpose
  Notice of privacy practices (NPP): must provide to patients
  Permitted uses/disclosures without authorization:
    Treatment, payment, health care operations (TPO)
    Public health activities, legal proceedings, law enforcement
    Research (with IRB waiver or patient authorization)
  Required disclosures: to individuals (upon request) + to HHS (compliance)

SECURITY RULE (Administrative, Physical, Technical Safeguards):
  Administrative: risk analysis, security management, workforce training, access management
  Physical: facility access controls, workstation use policies, device disposal
  Technical: access controls, audit controls, integrity controls, transmission security
  Risk analysis: MANDATORY; must assess current risks to ePHI confidentiality/integrity/availability

BREACH NOTIFICATION RULE:
  Breach: acquisition, access, use, disclosure of unsecured PHI NOT permitted under HIPAA
  Notify: affected individuals (within 60 days); HHS (within 60 days);
    If >500 individuals in a state: also notify prominent media in that state
    < 500: report to HHS log annually
  Unsecured PHI: not encrypted per NIST standards + not destroyed per guidelines

ENFORCEMENT:
  OCR (HHS Office for Civil Rights): primary enforcer
  Civil penalties: $100–$50,000 per violation per year (tiered by culpability)
    Maximum: $1.5M per violation category per year
  Criminal penalties (DOJ): up to 10 years imprisonment for wrongful disclosure
  State AG enforcement also possible
  Notable fines: $16M (Anthem breach 2015 — largest to date), $3.9M (OCR 2024)
```

---

## 4. Data Breach Notification Laws

```
US PATCHWORK: 50 states + DC/territories all have breach notification laws
  Varying triggers: some require "harm" likelihood; others automatic
  Varying timelines: 30, 45, 60, 72 hours, or "expedient"
  Varying covered info: SSN, financial, health, login credentials, biometrics
  New York SHIELD Act (2019): expanded definition of private info; reasonable security
  Colorado (2018): most stringent 30-day notification to AG + consumers

FEDERAL SECTOR-SPECIFIC:
  HIPAA: 60 days to individuals; 60 days to HHS
  GLBA: FTC Safeguards Rule (2023): financial institutions 30 days to FTC for 500+ affected
  SEC (2023): material cybersecurity incident 4 business days after materiality determination
    (public companies; significant controversy over timeline + what's material)

EU GDPR: 72 hours to DPA; "without undue delay" to individuals if high risk

LEGAL CONCEPT OF "SECURITY BREACH":
  Unauthorized acquisition of personal information
  Not just "breach of a network" — must be actual data acquisition
  Encrypted data: many laws exclude if rendered unreadable (GDPR: "encryption without the key")
  Ransomware: creates breach notification obligations even without confirmed exfiltration
    in many jurisdictions (encryption = unauthorized acquisition)
```

---

## 5. FTC Act Section 5 Privacy Enforcement

```
FTC Act §5: prohibits "unfair or deceptive acts or practices in or affecting commerce"
  Deceptive: representation, omission, practice that misleads a reasonable consumer
    Privacy policy promises you break → deceptive
    Saying "we don't share data" then sharing → deceptive
  Unfair: substantial consumer harm that's not outweighed by benefits + not avoidable
    Inadequate security → unfair (FTC v Wyndham)
    Retroactive privacy changes without consent → unfair

FTC CONSENT ORDERS: company agrees to 20-year oversight, audits, compliance
  Facebook (Meta): $5B settlement 2019 (Cambridge Analytica + prior order violations)
  Google: $22.5M (2012), $170M YouTube/COPPA (2019)
  Twitter: $150M (2022) — used 2FA phone numbers for ads despite promising not to

COPPA (Children's Online Privacy Protection Act):
  Applies to online services directed to children under 13 OR with actual knowledge
  Must: get verifiable parental consent before collecting children's PI
  No data collection beyond what needed; data retention limits; security
  YouTube: $170M FTC/NY AG fine (2019) for COPPA violations on child-directed content

GRAMM-LEACH-BLILEY Act (GLBA):
  Financial institutions: privacy notices + opt-out of sharing with non-affiliated third parties
  Safeguards Rule (2023 update): written information security program requirements
    Encryption at rest and in transit; MFA; patch management; pen testing; incident response
    500+ customer records breach: notify FTC within 30 days
```

---

## Decision Cheat Sheet

| Regulation | Applies to | Key Consumer Rights | Penalties |
|-----------|-----------|--------------------|-----------|
| GDPR | Any org processing EU residents' data | Access, erasure, portability, object | 4% global revenue or €20M |
| CCPA/CPRA | CA businesses (revenue/data thresholds) | Know, delete, opt-out of sale | $7,500/intentional violation |
| HIPAA | Covered entities + BAs handling PHI | Access, restrict, amend | $100-$50K per violation |
| COPPA | Services directed to children <13 | Parental consent required | $50,120/violation (FTC) |
| FERPA | Educational institutions receiving federal funds | Access, amendment, disclosure control | Federal funding loss |

| Scenario | What applies |
|----------|-------------|
| SaaS company with EU customers | GDPR applies; need DPA with processor; SCCs for US transfers |
| Hospital using cloud storage for patient records | HIPAA + BAA required with cloud provider |
| App collecting data from California residents | CCPA if revenue/volume thresholds met |
| Company selling user data to advertisers | CCPA opt-out rights; GDPR requires consent/legitimate interests |
| Security incident affecting 600 California residents | State breach notification (AG within 45 days + individual notice) |

---

## Common Confusion Points

**GDPR "consent" is narrower than you think:** Pre-ticked boxes, bundled consent with T&Cs, and "take it or leave it" approaches don't meet GDPR standards. But consent isn't required for everything — legitimate interests and contract performance cover much B2B and analytics processing.

**HIPAA doesn't apply to all health data:** A fitness app collecting your health data is not a HIPAA covered entity and has no HIPAA obligations. HIPAA only covers health plans, healthcare providers, clearinghouses, and their business associates. Apple Health data, gym apps, genetic testing: not HIPAA (though state laws may apply).

**CCPA "sale" includes non-monetary consideration:** Sharing data for valuable consideration (even if not cash) can be a "sale" under CCPA. The ad tech ecosystem's data trading triggered CCPA's opt-out right even without direct money changing hands.

**Encryption as breach safe harbor:** If data was encrypted per NIST standards (AES-256) and the key wasn't also taken, many breach notification laws don't require notification. "Unsecured" PHI under HIPAA = not encrypted by NIST standards. Design your systems with encryption at rest as the baseline.

**GDPR's territorial scope surprises people:** A US company with no EU offices but that operates a website accepting EU users (especially if targeted at them) falls under GDPR. You need either DPF certification, SCCs, or BCRs for any data transfers back to the US. The "targeting" prong is broad.

**Data minimization is a real compliance obligation:** GDPR Article 5(1)(c): collect only what's adequate, relevant, and limited to what's necessary. This creates engineering obligations — don't just collect everything "in case it's useful." Document your retention schedules and actually delete data at end of retention.
