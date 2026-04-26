# Incident Response: Detection, Containment, Eradication, Post-Mortem

## The Big Picture

Incident response is the structured process for detecting, analyzing, containing, and recovering from security incidents. The goal is not just to stop the current attack but to learn from it and improve the security posture.

```
NIST SP 800-61 INCIDENT RESPONSE LIFECYCLE
+-----------------------------------------------------------------------+
|                                                                       |
|  PREPARATION → DETECTION & → CONTAINMENT, → POST-INCIDENT          |
|               ANALYSIS      ERADICATION,   ACTIVITY                 |
|                              RECOVERY                                 |
|                                                                       |
|  PREPARATION:        DETECTION &        CONTAINMENT:                  |
|  IR plan             ANALYSIS:          Short-term containment        |
|  CSIRT / SOC         SIEM alerts        Evidence preservation         |
|  Runbooks            EDR telemetry      System isolation              |
|  Communication       User reports       Network block                 |
|  templates           Threat intel                                     |
|  Legal contacts      Triage             ERADICATION:                  |
|  Forensic tools      Severity matrix    Remove malware                |
|  Offline backups                        Reset compromised creds       |
|                                         Patch exploited vuln          |
|                      RECOVERY:                                        |
|                      Restore systems    POST-INCIDENT:                |
|                      Validate integrity Lessons learned               |
|                      Monitor closely    Blameless postmortem          |
|                                         Control improvements          |
+-----------------------------------------------------------------------+
```

---

## Preparation

Preparation is the most important phase — you cannot respond effectively to an incident you are not prepared for.

### IR Plan Components

```
INCIDENT RESPONSE PLAN MUST INCLUDE:
  1. Incident severity classification (P1-P4 definitions)
  2. CSIRT roster: who to call, in what order, contact info (offline copy)
  3. Legal and compliance contacts (General Counsel, compliance officer)
  4. Communication templates (internal exec, external customer, regulator)
  5. Runbooks per incident type:
     - Ransomware / destructive malware
     - Data breach / exfiltration
     - Account compromise / insider threat
     - DDoS
     - Supply chain compromise
  6. Evidence collection procedures (forensic imaging order, chain of custody)
  7. Backup validation schedule
  8. Crisis communication decision tree
```

### CSIRT Structure

```
CSIRT (Computer Security Incident Response Team) ROLES:
  Incident Commander (IC):    Overall coordination and decisions
  Security Analyst(s):        Technical analysis, malware/forensics
  Infrastructure/Ops:         Isolation, containment actions
  Communications Lead:        Internal exec comms, customer notification
  Legal Counsel:              Regulatory requirements, evidence handling
  Executive Sponsor:          Business decisions (take down a system?)

On-call rotation:
  Security engineer with pager rotation
  Escalation path defined: analyst → senior analyst → IC → CISO

MICROSOFT SSIRT / MSRC:
  Microsoft Security Response Center handles external vulnerability reports
  SSIRT (Secure Software Incident Response Team) handles active incidents
  Separate from CSIRT: SSIRT is for software vulnerabilities; CSIRT is for
  operational security incidents
```

---

## Detection and Analysis

### Detection Sources

```
DETECTION INPUT SOURCES (by likelihood of true positive)

HIGH SIGNAL:
  EDR (Endpoint Detection and Response): Defender for Endpoint, CrowdStrike
    → Process injection, credential dumping, LOLBAS (Living off the Land)
    → Behavioral detection, not just signatures
  UEBA (User and Entity Behavior Analytics):
    → "Admin account logged in from foreign country at 3am"
    → "Service account making 50,000 AD queries in 10 minutes"
  Threat intelligence feeds:
    → Known C2 IP in firewall logs, known malware hash in EDR

MEDIUM SIGNAL:
  SIEM correlation rules: multiple auth failures + successful login
  Azure Security Center / Defender alerts
  Deception technology: honeypot credentials used

LOWER SIGNAL (high volume, needs correlation):
  WAF alerts (many false positives from scanners)
  IDS/IPS signatures
  Firewall anomalies (volume, new destination)
  User reports ("my computer is acting weird")
```

### Triage Methodology

```
INCIDENT TRIAGE MATRIX

SEVERITY ASSESSMENT:
  Impact score (data / system / user):
    1 = low (single system, non-sensitive data)
    2 = medium (multiple systems, sensitive data)
    3 = high (production, PII/financial, critical service)
  Urgency score (progression speed):
    1 = slow (opportunistic, no active attacker)
    2 = medium (automated malware, expanding)
    3 = high (active human attacker, lateral movement observed)

  P1: Impact 3 + Urgency 3 → Immediate response (15min SLA)
  P2: Impact 3 + Urgency 2 or Impact 2 + Urgency 3 → 1 hour SLA
  P3: Impact 2 + Urgency 2 → 4 hour SLA
  P4: Impact 1 + Urgency 1 → Business hours SLA

INITIAL TRIAGE QUESTIONS:
  What systems are affected? (scope)
  Is the attacker still present? (active vs. historic)
  What data may have been accessed or exfiltrated? (impact)
  When did the intrusion begin? (timeline)
  How did they get in? (initial access vector)
```

### Incident Categories (NIST)

| Category | Examples |
|----------|---------|
| Denial of Service | DDoS, application-layer DoS, ransomware |
| Malicious Code | Malware, ransomware, worm, rootkit |
| Unauthorized Access | Account compromise, privilege escalation, unauthorized data access |
| Inappropriate Usage | Policy violation, data exfiltration by insider |
| Scans / Probes | Reconnaissance, vulnerability scanning |

---

## Containment Strategy

### Isolate vs. Monitor Decision

```
CONTAINMENT DECISION TREE

Active attacker present?
  |
  YES → Do we want to gather intelligence first?
        |
        YES → MONITOR mode:
               Keep attacker unaware while gathering IOCs
               (Indicators of Compromise: malware hashes, C2 IPs, TTPs)
               Risk: attacker may escalate, exfiltrate, destroy evidence
               Use: when attribution or legal action is desired
               Duration: short (hours, not days)
        |
        NO → ISOLATE immediately:
              Cut network access (firewall rules, VLAN change)
              Prevent lateral movement
              Risk: attacker may have dead-man switches
              May destroy evidence if not carefully done first
  |
  NO (no active attacker) → Isolate and investigate at own pace
```

### Containment Actions

```
SHORT-TERM CONTAINMENT (immediate, preserves evidence):
  Firewall rule: block malicious IP at perimeter
  NSG rule: isolate compromised VNet subnet
  Disable compromised user account (do NOT delete — preserve evidence)
  Revoke session tokens, force re-authentication
  Pull affected system off network but keep it running (memory volatile)
  Note: act carefully to avoid triggering destructive payloads

LONG-TERM CONTAINMENT (can take hours to days):
  Rebuild compromised systems from known-good images
  Apply emergency patches for exploited vulnerability
  Reset all credentials potentially accessible on compromised systems
  Deploy compensating controls (WAF rule, block exploit path)
```

---

## Evidence Preservation

```
FORENSIC EVIDENCE ORDER OF VOLATILITY (most volatile → least):
  1. CPU registers and cache
  2. Memory (RAM) — capture FIRST before powering off
  3. Network connections / ARP cache / routing tables
  4. Running processes
  5. Open files
  6. Disk (persistent, less volatile)
  7. Remote logs (SIEM, external storage)
  8. Backup media

MEMORY ACQUISITION:
  Tool: Volatility framework, WinPmem (Windows), LiME (Linux kernel module)
  Captures: running processes, network connections, encryption keys in memory,
            malware that exists only in memory (fileless)

DISK IMAGING:
  Forensic copy: bit-for-bit image (dd, FTK Imager, DC3DD)
  Hash verification: SHA-256 of image before and after → proves no tampering
  Chain of custody form: who collected, when, where stored, who accessed

AZURE FORENSICS:
  VM snapshot before remediation
  Azure Disk → copy to forensic storage account
  Enable boot diagnostics, serial console before incident
  Azure Activity Log: immutable audit trail of Azure control plane operations
  Defender for Endpoint: 30-day EDR timeline, offline investigation
```

---

## Eradication and Recovery

```
ERADICATION CHECKLIST:
  [ ] Remove all malware (confirmed with EDR + manual review)
  [ ] Close all attacker-created backdoors (scheduled tasks, registry persistence,
      new user accounts, SSH keys, OAuth tokens, service principals)
  [ ] Patch the exploited vulnerability (or implement compensating control)
  [ ] Reset all potentially compromised credentials
      (not just the obviously compromised ones — blast radius analysis)
  [ ] Verify no remaining persistence mechanisms
  [ ] Review and audit all privileged accounts

RECOVERY CHECKLIST:
  [ ] Restore from known-good backup (or rebuild from image)
  [ ] Re-enable systems in monitored environment (not direct re-connection)
  [ ] Validate integrity: known-good hashes, file system audits
  [ ] Monitor closely: EDR enhanced alerting, SIEM tuned rules for recurrence
  [ ] Test functionality before announcing recovery
  [ ] Rotate monitoring credentials used during investigation
```

---

## Post-Incident Activity

### Blameless Postmortem

```
BLAMELESS POSTMORTEM STRUCTURE:
  Date and time range of incident
  Summary (executive summary, 2-3 paragraphs)
  Timeline (chronological, timestamped)
  Root cause analysis (5 Whys or fishbone)
  Contributing factors (not just proximate cause)
  What went well (detection, response, comms)
  What could be improved
  Action items (owner, due date, priority)

5 WHYS EXAMPLE:
  Q: Why was data exfiltrated?
  A: Attacker had access to production S3 bucket

  Q: Why did attacker have access?
  A: Service account credential was compromised

  Q: Why was the credential compromised?
  A: It was hardcoded in source code and the repo was leaked

  Q: Why was it hardcoded?
  A: No secret management policy was enforced

  Q: Why was no policy enforced?
  A: No automated scanning for secrets in CI pipeline

  ROOT CAUSE: Missing secrets scanning in CI pipeline
  FIX: Implement GitHub Secret Scanning + pre-commit hooks (see 04-SECURE-SDLC.md)

BLAMELESS PRINCIPLE:
  People make mistakes — especially under pressure, with incomplete information.
  The postmortem goal is to find systemic gaps, not assign blame.
  "If two different people had been in that role, would the same mistake have
  been made?" If yes: it is a systemic issue, not an individual one.
```

---

## Azure Sentinel (Microsoft Sentinel)

Microsoft Sentinel is Azure's cloud-native SIEM and SOAR (Security Orchestration, Automation, and Response) platform.

```
SENTINEL ARCHITECTURE

DATA CONNECTORS:
  Azure Activity Logs, Microsoft 365, Azure AD sign-in logs,
  Defender for Endpoint, Syslog (Linux), Windows Event Logs,
  CEF (Common Event Format) from NGFW/IDPS, custom REST API connectors

ANALYTICS RULES:
  Scheduled: run KQL query on schedule, create alert if threshold met
  NRT (Near-Real-Time): sub-minute latency for high-priority rules
  ML Fusion: correlate low-fidelity alerts into high-confidence incidents
  Threat Intelligence: match IOCs from TI feeds against log data

INCIDENTS:
  Aggregated from alerts + correlated
  Investigation graph: show entities (IPs, users, hosts) and their relationships
  Entity mapping: automatically extract entities from alerts

WORKBOOKS: KQL-powered dashboards (Azure Monitor Workbooks)

AUTOMATION (SOAR):
  Playbooks: Azure Logic Apps triggered by incident/alert
  "When incident P1 created: send Teams message, create ServiceNow ticket,
   isolate VM in Azure"

KQL EXAMPLES:
  SecurityEvent | where EventID == 4625 | summarize count() by Account, Computer
  → Count failed login attempts per account and computer

  AzureActivity | where OperationName == "Delete" | where Caller !in (expected_admins)
  → Alert on unexpected delete operations
```

---

## Common Confusion Points

**"Incident response starts when the attacker is detected"**
Incident response starts long before — during preparation. An unprepared team discovering an active incident will improvise, make mistakes, and likely destroy evidence. Preparation is 80% of effective incident response.

**"Isolate immediately to stop the bleeding"**
Isolation is often correct, but not always. If you isolate a compromised system before capturing volatile memory, you may lose evidence of how the attacker got in and what they accessed. Short-term containment (network isolation at firewall, not VM shutdown) while preserving evidence is the nuanced response.

**"Deleting the compromised account protects us"**
Deleting a compromised account destroys evidence. Disable it (preserve the audit trail), force token revocation, and investigate before deletion.

**"Post-mortem is about finding who made the mistake"**
Blameless post-mortems produce actionable systemic improvements. Blame-focused post-mortems make people hide mistakes, reducing future detection. The SRE / blameless culture is a security asset, not just a morale asset.

---

## Decision Cheat Sheet

| Situation | Action |
|-----------|--------|
| SIEM alert: failed logins then success from new country | Triage P2: verify user, check for lateral movement, force password reset |
| Ransomware detected on one server | P1: Isolate at network level, initiate IR plan, preserve memory image |
| Possible data exfiltration to S3 bucket | P1: Quantify data, check DLP logs, invoke legal, 72-hour breach notification window starts |
| Privileged account compromised | P1: Disable account immediately, audit all actions, reset all systems the account touched |
| Insider threat suspected | P2: Engage HR + Legal first before taking technical action |
| IR complete, writing postmortem | Blameless, 5 Whys to root cause, action items with owners and dates |
| Planning for ransomware scenario | Run tabletop exercise, validate offline backups, pre-approve isolation authority |
