# Security Compliance: SOC 2, ISO 27001, FedRAMP, GDPR, PCI DSS

## The Big Picture

Security compliance frameworks define minimum standards that organizations must meet to operate in regulated markets, handle sensitive data, or sell to certain customers. Understanding the difference between compliance (meeting the standard) and security (actually being hard to compromise) is essential.

```
COMPLIANCE LANDSCAPE
+-----------------------------------------------------------------------+
|                                                                       |
|  VOLUNTARY FRAMEWORKS           REGULATORY REQUIREMENTS               |
|  +---------------------------+  +--------------------------------+    |
|  | SOC 2 (AICPA)             |  | GDPR (EU - all personal data)  |   |
|  | ISO 27001 (global ISMS)   |  | CCPA (California consumers)    |   |
|  | CSA STAR (cloud security) |  | HIPAA (US health data)         |   |
|  | CIS Controls              |  | PCI DSS (payment card data)    |   |
|  +---------------------------+  | GLBA (US financial)            |   |
|                                  | SOX (US public companies)      |  |
|  US GOVERNMENT                  +--------------------------------+   |
|  +---------------------------+                                        |
|  | FedRAMP (cloud, federal)  |  COMPLIANCE vs. SECURITY:              |
|  | FISMA (federal agencies)  |  Compliance = meeting audit criteria   |
|  | NIST CSF (guidance)       |  Security = actually hard to attack    |
|  | CMMC (defense contracts)  |  You can be compliant AND insecure     |
|  +---------------------------+                                        |
+-----------------------------------------------------------------------+
```

---

## SOC 2

SOC 2 (System and Organization Controls 2) is an auditing standard by the AICPA for service organizations that store or process customer data.

### Trust Service Criteria (TSC)

SOC 2 is built on 5 Trust Service Criteria:

| Criteria | Abbreviation | Requirement |
|----------|-------------|-------------|
| Security | CC | System protected against unauthorized access (required for all SOC 2) |
| Availability | A | System available for operation as committed |
| Confidentiality | C | Information designated confidential is protected |
| Processing Integrity | PI | Processing is complete, valid, accurate, timely |
| Privacy | P | Personal information collected, used, retained, disclosed as committed |

Most SOC 2 audits cover Security only. Adding Availability and Confidentiality is common for SaaS companies. Privacy is included when handling PII specifically.

### Type I vs. Type II

```
SOC 2 TYPE I:
  Point-in-time assessment
  "On this date, were controls designed appropriately?"
  Auditor reviews design of controls
  Useful for initial market entry (faster to obtain)
  NOT sufficient for most enterprise procurement requirements

SOC 2 TYPE II:
  Period of time assessment (typically 6–12 months)
  "Over this period, were controls operating effectively?"
  Auditor reviews evidence of controls operating: logs, tickets,
    access reviews, security scans, training records
  Industry standard for SaaS enterprise sales
  Renewal: annual re-audit

TIMELINE:
  Prepare (3–6 months): implement controls, collect evidence
  Audit period (6 months minimum): controls operating under observation
  Audit + reporting (2–3 months): auditor reviews evidence, issues report
  Total: 11–15 months from start to first Type II report
```

### Security Criterion (CC) Key Controls

The Security criterion (CC) covers the common criteria shared across all TSC:

```
CC6 LOGICAL ACCESS (most engineering-intensive):
  CC6.1: Logical access security measures
    → Multi-factor authentication for all privileged access
    → Role-based access control, least privilege
    → Access reviews (quarterly for privileged, annual for all)
  CC6.2: Formal access granting/revoking process
    → HR-to-IT provisioning/deprovisioning workflow
    → Leavers: access revoked same day
  CC6.3: Restrict privileged access
    → No shared admin accounts
    → Individual accountability for privileged actions
    → PAM / JIT for production access

CC7 SYSTEM OPERATIONS:
  CC7.1: Monitoring for security events
    → SIEM deployed, alerts configured, reviewed
  CC7.2: Incident response procedures
    → IR plan documented, tested (tabletop)
  CC7.3: Incident identification and analysis

CC8 CHANGE MANAGEMENT:
  → Change management process
  → Approval gates, rollback procedures
  → Security review of significant changes

CC9 RISK MITIGATION:
  → Formal risk assessment process
  → Vendor risk management (third-party assessments)
```

---

## ISO 27001

ISO 27001 is an international standard for Information Security Management Systems (ISMS). It is the most widely recognized global security certification.

### ISMS Structure

```
ISO 27001 ISMS FRAMEWORK

PLAN:
  Context of the organization (scope, interested parties)
  Risk assessment methodology
  Information security risk assessment
  Risk treatment plan (accept, transfer, mitigate, avoid)
  Statement of Applicability (which Annex A controls apply and why)

DO:
  Implement Annex A controls
  Implement risk treatment plan
  Operate security policies and processes
  Manage security incidents

CHECK:
  Internal audits (at least annual)
  Management review
  Performance measurement against controls

ACT:
  Nonconformity and corrective action
  Continual improvement
```

### Annex A Controls (2022 — ISO 27001:2022)

ISO 27001:2022 has 93 controls in 4 domains (reduced from 114 in 2013):

| Domain | Number of Controls | Examples |
|--------|-------------------|---------|
| Organizational | 37 | Policies, roles, threat intelligence, security in projects |
| People | 8 | Screening, training, remote work |
| Physical | 14 | Physical security, clear desk, equipment security |
| Technological | 34 | Access control, endpoint security, logging, cryptography, patch management |

**Statement of Applicability (SoA)**: For each of the 93 Annex A controls, you must state: applicable or not applicable, and if not applicable, the justification. This is the most critical SOA document — it forces explicit decisions about every control.

### Certification Process

```
ISO 27001 CERTIFICATION PROCESS:
  Stage 1 audit (documentation review):
    External auditor reviews: ISMS scope, policies, risk assessment,
    SoA, procedures
    Issues: findings (must fix), observations (should fix), opportunities
  Stage 2 audit (operational effectiveness):
    On-site (or virtual) review of implemented controls
    Evidence sampling: logs, tickets, training records, access reviews
    Issues: major/minor nonconformities
  Certification issued if no major nonconformities
  Surveillance audits: annually (abbreviated)
  Recertification: every 3 years (full audit)
```

---

## FedRAMP

FedRAMP (Federal Risk and Authorization Management Program) is the US government's authorization process for cloud service providers (CSPs) serving federal agencies.

```
FEDRAMP IMPACT LEVELS:

LOW: Information with limited adverse effect if disclosed
  72 controls (NIST SP 800-53 Rev 5 subset)
  Example: public-facing informational websites

MODERATE: Most federal systems (85% of federal use cases)
  323 controls
  Example: benefits systems, grant management, HR systems

HIGH: National security, law enforcement, emergency services
  400+ controls
  Example: criminal justice, financial systems, health systems

AUTHORIZATION TO OPERATE (ATO) PROCESS:
  1. CSP selects impact level and boundary
  2. CSP engages a 3PAO (Third Party Assessment Organization)
  3. 3PAO performs security assessment
  4. CSP submits Security Package to FedRAMP PMO
     (System Security Plan, Security Assessment Report, Plan of Action)
  5. Agency issues Provisional ATO or FedRAMP PMO issues P-ATO
  6. Continuous monitoring: monthly vulnerability scans, annual assessment
  7. Significant changes: require re-assessment

AZURE FEDRAMP:
  Azure Government cloud: FedRAMP High authorized
  Azure Commercial: FedRAMP Moderate authorized for most services
  Microsoft maintains the authorization; customers inherit controls
  → Customer responsibility: application-level controls (data handling, access)

TIMELINE: 6–24 months for initial authorization
COST: $2–5M+ for initial authorization; $500K–$1M annual continuous monitoring
```

---

## GDPR: Security Obligations

The General Data Protection Regulation (EU, 2018) imposes security requirements alongside privacy requirements.

### Article 32: Security of Processing

```
GDPR ARTICLE 32 REQUIREMENTS:
  Implement "appropriate technical and organizational measures" to ensure
  a level of security appropriate to the risk, including:

  (a) Pseudonymisation and encryption of personal data
  (b) Ability to ensure ongoing confidentiality, integrity,
      availability and resilience of processing systems
  (c) Ability to restore data in timely manner in event of incident
  (d) Regular testing and evaluation of security measures

RISK-PROPORTIONATE:
  GDPR does not specify exact controls — it requires "appropriate" measures
  relative to: nature of data, scope of processing, state of the art,
  costs of implementation, risks to data subjects

  → Encryption, MFA, and access controls for any PII
  → Stronger controls for special category data (health, biometric, etc.)
```

### Article 33: Breach Notification

```
72-HOUR NOTIFICATION REQUIREMENT:
  When a personal data breach occurs:
  → Notify supervisory authority (e.g., ICO in UK, DPA in EU member state)
    WITHIN 72 HOURS of becoming aware
  → Unless breach is unlikely to result in risk to individuals

  If notification to authority cannot happen in 72h:
  → Notify with explanation of delay; provide info in phases

NOTIFICATION CONTENT:
  Nature of breach, categories and approximate number of individuals
  Contact details of DPO (Data Protection Officer)
  Likely consequences of breach
  Measures taken to address breach

ARTICLE 34: Notification to data subjects:
  When breach likely results in HIGH risk to individuals:
  → Also notify individuals directly (without undue delay)
  → Not required if effective technical measures rendered data unintelligible
    (encrypted data with keys still secure = no individual notification)

IRDA LESSONS (regulatory lens):
  Microsoft itself has been subject to GDPR enforcement via data transfers
  The 72-hour window means IR plan must include legal/DPO from the start
```

---

## PCI DSS v4.0

PCI DSS (Payment Card Industry Data Security Standard) applies to any organization that stores, processes, or transmits cardholder data.

### 12 Requirements

```
PCI DSS 12 REQUIREMENTS

NETWORK SECURITY:
  1. Install and maintain network security controls (firewalls)
  2. Apply secure configurations to all components

PROTECT ACCOUNT DATA:
  3. Protect stored account data (encryption, masking PAN)
  4. Protect cardholder data with strong cryptography during transmission

VULNERABILITY MANAGEMENT:
  5. Protect all systems and networks from malicious software
  6. Develop and maintain secure systems and software

ACCESS CONTROL:
  7. Restrict access to system components by business need
  8. Identify users and authenticate access (MFA for admin access)
  9. Restrict physical access to cardholder data

MONITOR AND TEST:
  10. Log and monitor all access to network and cardholder data
  11. Test security of systems and networks regularly
     (quarterly: internal scan; annual: external pen test + quarterly ASV scan)

SECURITY POLICY:
  12. Support security with organizational policies and programs

v4.0 ADDITIONS (2024):
  MFA required for ALL access to cardholder data environment (not just admin)
  Targeted risk analysis: justify how often each control is performed
  Software security frameworks: align with OWASP, NIST
  Authenticated internal vulnerability scanning
```

### Cardholder Data Environment (CDE) Scoping

Limiting the CDE scope limits the PCI burden:

```
CDE = any system that stores, processes, or transmits PAN (Primary Account Number)
       or is connected to such a system

SCOPE REDUCTION STRATEGIES:
  Tokenization: replace PAN with non-sensitive token at entry point
    → Only the tokenization service is in-scope; rest of system is not
    → Stripe, Braintree, PayPal handle PAN; you never see it
  Network segmentation: isolate CDE from rest of environment
    → Segmentation validated by pen tester
  P2PE (Point-to-Point Encryption): encrypt at payment terminal
    → Encrypted PAN travels through your system; cannot be decrypted

THE GOAL: make the CDE as small as possible
```

---

## Compliance vs. Security

```
COMPLIANCE IS THE FLOOR
  SOC 2, ISO 27001, PCI DSS define MINIMUM requirements
  A system can be fully compliant and still trivially breached:
    → Compliant with MFA policy but phishing attack delivers session token
    → Compliant with patch SLA but zero-day used before patch exists
    → Compliant with access control but insider threat steals data legally

SECURITY IS THE CEILING (you set it)
  Real security is: threat model driven, risk proportionate,
  defense in depth, continuously tested, blameless postmortem culture

GRC TOOLS (Governance, Risk, Compliance):
  ServiceNow GRC: integrated risk management + compliance tracking
  Archer (OpenText): enterprise GRC platform
  Vanta / Drata / Secureframe: automated evidence collection for SOC 2 / ISO 27001
    (pull audit evidence from AWS/Azure/GCP/Okta APIs automatically)
    Reduces audit preparation from months to weeks
  Microsoft Purview Compliance Manager: Microsoft-specific compliance posture
```

---

## Common Confusion Points

**"SOC 2 Type I means we're secure"**
SOC 2 Type I only verifies that controls were properly designed at a point in time. It does not verify they were actually operating. Type II (operating effectiveness over 6+ months) is the relevant certification for enterprise customers, and even Type II compliance does not guarantee security against sophisticated attackers.

**"ISO 27001 tells us exactly what to do"**
ISO 27001 is a management system standard — it defines the framework and process, but not the specific controls. The Annex A controls are guidance; you document in your SoA which apply and why. The standard requires you to think about your risk and context, not just implement a checklist.

**"FedRAMP is just for government agencies"**
FedRAMP authorization is required for cloud services sold to US federal agencies. But many regulated enterprises (financial, healthcare) use FedRAMP-authorized cloud services as evidence of strong security posture, even without government contracts.

**"GDPR breach notification = security breach notification"**
GDPR Art. 33 notification is triggered by personal data exposure, not any security incident. A DDoS attack that causes availability loss is an incident but may not require Art. 33 notification. A misconfigured S3 bucket exposing customer emails does require it, even without an active attacker.

---

## Decision Cheat Sheet

| Situation | Relevant Framework |
|-----------|-------------------|
| SaaS selling to enterprise | SOC 2 Type II (security criterion mandatory) |
| International operations with EU customers | GDPR (mandatory); ISO 27001 (recommended) |
| Selling to US federal agencies | FedRAMP (mandatory) |
| Processing credit/debit card payments | PCI DSS (mandatory based on transaction volume) |
| Evidence of security program for M&A | SOC 2 + ISO 27001 |
| US federal contractor (defense) | CMMC (Cybersecurity Maturity Model Certification) |
| Healthcare data in US | HIPAA Security Rule |
| Measuring your own security maturity | NIST CSF, CIS Controls |
