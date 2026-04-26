# Red and Blue Team: Penetration Testing, Purple Team, Tabletop Exercises

## The Big Picture

Red team, blue team, and purple team activities test security controls against real adversarial behavior. They turn "we believe our controls work" into "we have evidence our controls work."

```
OFFENSIVE AND DEFENSIVE SECURITY FUNCTIONS
+-----------------------------------------------------------------------+
|                                                                       |
|  RED TEAM                     BLUE TEAM               PURPLE TEAM     |
|  +-----------------------+   +-------------------+   +------------+   |
|  | Adversary simulation  |   | Detection &       |   | Red + Blue  | |
|  | Goal-oriented         |   | Response          |   | working     | |
|  | Persistent access     |   | SOC operations    |   | together    | |
|  | Lateral movement      |   | Threat hunting    |   | Real-time   | |
|  | Data exfiltration     |   | SIEM tuning       |   | knowledge   | |
|  | months-long           |   | Playbook updates  |   | transfer    | |
|  +-----------------------+   +-------------------+   +------------+ |
|          |                           |                      |       |
|          v                           v                      v       |
|  PEN TEST                   THREAT HUNTING        TABLETOP          |
|  Point-in-time              Hypothesis-driven     Scenario-based    |
|  scoped assessment          proactive search      discussion exercise |
|  weeks                      for undetected        no actual attack  |
|                             threats               hours             |
+-----------------------------------------------------------------------+
```

---

## Red Team: Adversary Simulation

A red team engagement simulates a real adversary — persistent, goal-oriented, using real TTPs (tactics, techniques, and procedures). It is fundamentally different from a penetration test.

```
PENETRATION TEST vs. RED TEAM

PEN TEST:
  Scope: defined set of systems or applications
  Goal: find as many vulnerabilities as possible
  Duration: 2–4 weeks
  Approach: systematic coverage of defined scope
  Output: vulnerability report with findings and remediations
  Value: good for compliance evidence, specific system assessment

RED TEAM:
  Scope: entire organization (the whole castle, not just one door)
  Goal: achieve specific objective (e.g., "exfiltrate customer data")
  Duration: 3–6 months (or continuous)
  Approach: mimic specific threat actor (APT28, Lazarus group)
  Output: attack narrative, detection gaps, response weaknesses
  Value: tests the full kill chain, detects configuration gaps SAST won't find
  Disclosure: typically limited (only CISO and exec know)
```

### Red Team Phases (Kill Chain)

```
RED TEAM ENGAGEMENT PHASES

1. RECONNAISSANCE
   OSINT: LinkedIn, job postings, GitHub, Shodan, Censys
   Passive: no direct interaction with target systems
   Active: DNS enumeration, service discovery (risk: early detection)

2. INITIAL ACCESS
   Phishing: spear-phishing email with payload
   Credential stuffing: breached credentials tested against VPN/SSO
   Supply chain: compromise a vendor that has access
   Physical: tailgating, USB drops
   Exploit: public-facing vulnerability (WebShell, etc.)

3. EXECUTION
   Run payload on compromised host
   Fileless: PowerShell Empire, cobalt strike beacon in memory
   Persistence: registry run key, scheduled task, service, WMI subscription

4. PRIVILEGE ESCALATION
   Local admin → domain admin
   Kerberoasting, AS-REP roasting, DCSync attack
   Token impersonation, process injection

5. LATERAL MOVEMENT
   Pass-the-Hash, Pass-the-Ticket
   WMI, SMB, RDP, WinRM to reach target systems
   Azure AD: consent phishing, token theft from browser memory

6. EXFILTRATION / IMPACT
   Data staging → exfil over DNS, HTTPS to attacker C2
   Achieve stated objective (access customer DB, deploy "ransomware" simulation)

7. REPORTING
   Attack narrative: step-by-step timeline
   Detection opportunities: where defenders could have seen each step
   Dwell time: how long from initial access to objective
```

### PTES: Penetration Testing Execution Standard

PTES (penetration-testing-standard.org) defines the scope, methodology, and deliverables for pen tests. Phases:
1. Pre-engagement interactions (scope, rules of engagement, legal authorization)
2. Intelligence gathering
3. Threat modeling
4. Vulnerability analysis
5. Exploitation
6. Post exploitation
7. Reporting

**Rules of Engagement (ROE)**: critical document. Defines: what is in scope, what is out of scope, what actions require prior approval (production database access, destructive payloads, social engineering), emergency stop procedure, and who to call if the pen test goes wrong.

---

## Bug Bounty Programs

Bug bounty programs invite external security researchers to find and responsibly report vulnerabilities in exchange for payment.

```
BUG BOUNTY ECONOMICS

RESEARCHER'S INCENTIVE:
  Paid for valid findings (range: $100 to $250,000+)
  HackerOne, Bugcrowd as platforms (escrow, triage, reputation)
  Reputation building (public leaderboard, Hall of Fame)
  Legal protection: good-faith researchers protected

ORGANIZATION'S VALUE:
  Continuous testing by global researcher pool
  Pay per valid finding (vs. flat pen test fee)
  Finds issues pen tests miss (different researchers, different techniques)
  Community relationship: researchers report rather than exploit

SCOPE DEFINITION:
  In scope: web app, mobile app, specific APIs
  Out of scope: social engineering, physical, DDoS, production data access
  Safe harbor: legal protection for good-faith researchers

MICROSOFT BUG BOUNTY:
  MSRC.microsoft.com/en-us/msrc/bounty
  Range: $500 to $250,000+
  Critical areas: Azure, M365, Windows, Hyper-V
  Identity bounty: up to $100,000 for identity/auth bugs
```

---

## Blue Team: SOC and Threat Hunting

The blue team defends by detecting, investigating, and responding to threats.

### SOC Functions

```
SOC TIERS

TIER 1 (Alert monitoring):
  Monitor SIEM dashboard
  Initial triage: is this a true positive or false positive?
  Escalate confirmed or suspected incidents to Tier 2

TIER 2 (Incident handling):
  In-depth investigation of escalated alerts
  Threat intelligence enrichment
  Containment and remediation actions
  Documentation

TIER 3 (Threat hunting + advanced analysis):
  Proactive hunt for undetected threats
  Malware reverse engineering
  Forensic analysis
  Detection engineering (write new SIEM rules)
  Red team liaison

AUTOMATION LAYER (SOAR):
  Auto-enrich alerts with threat intelligence lookups
  Auto-triage: block known-bad IPs, disable accounts matching IOCs
  Auto-notify: Teams/Slack/PagerDuty for high-severity alerts
  Reduces Tier 1 manual work, reduces MTTD/MTTR
```

### Threat Hunting

Threat hunting is hypothesis-driven, proactive search for threats that have evaded automated detection.

```
THREAT HUNTING PROCESS

1. FORM HYPOTHESIS
   Trigger: threat intelligence report ("APT29 using Cobalt Strike with
   specific beacon configuration against Azure tenants")
   OR: anomaly noticed in data ("unusual DNS query volume")

2. COLLECT AND ANALYZE DATA
   EDR telemetry: process trees, network connections, file operations
   Log analytics: SIEM, Azure Activity, sign-in logs
   Memory: volatile forensics on suspect hosts

3. INVESTIGATE
   Hunt for IOCs: file hashes, C2 IPs, registry keys, beacon patterns
   Hunt for TTPs: abnormal process hierarchy, LOLBAS usage, unusual persistence

4. CONCLUDE
   Finding: evidence of compromise → escalate to incident response
   No finding: update detection rules, document hunt (validates environment)

LOLBAS (Living Off the Land Binaries, Scripts and Libraries):
  Attackers use legitimate Windows binaries to avoid AV detection
  powershell.exe, mshta.exe, certutil.exe, regsvr32.exe, wscript.exe
  Detecting LOLBAS requires behavioral detection (parent/child process trees)
  not just file hash matching
```

---

## Purple Team

Purple team is red and blue working together in real-time, sharing knowledge as the exercise runs.

```
PURPLE TEAM EXERCISE STRUCTURE

SETUP:
  Red team plans specific technique: Kerberoasting via Rubeus
  Blue team sets up detection: configure Splunk/Sentinel to capture
    Event 4769 (Kerberos service ticket request) with RC4 encryption

EXECUTE:
  Red team runs the technique
  Blue team: did the detection fire?
    YES: detection works! Document TTP coverage. Try next technique.
    NO: why not? Was the event logged? Was the rule correct?
       Red team and Blue team investigate together, fix the rule.

VALUE:
  Direct feedback loop: detection coverage is validated, not assumed
  Knowledge transfer: blue team understands attacker perspective
  ATT&CK coverage mapping: which techniques are covered, which are gaps

MITRE ATT&CK INTEGRATION:
  ATT&CK provides taxonomy of real adversary TTPs
  After purple team: map each tested technique to ATT&CK ID
  Heat map: green = detected, red = not detected
  Visualize coverage across kill chain
```

---

## MITRE ATT&CK Framework

ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) is a comprehensive framework cataloguing real adversary behaviors.

```
ATT&CK STRUCTURE

TACTICS (14): What the adversary is trying to achieve (the why)
  TA0001: Initial Access       TA0008: Lateral Movement
  TA0002: Execution            TA0009: Collection
  TA0003: Persistence          TA0010: Exfiltration
  TA0004: Privilege Escalation TA0011: Command and Control
  TA0005: Defense Evasion      TA0040: Impact
  TA0006: Credential Access    TA0042: Resource Development
  TA0007: Discovery            TA0043: Reconnaissance

TECHNIQUES (hundreds): Specific method to achieve tactic
  T1566: Phishing (Initial Access)
    T1566.001: Spearphishing Attachment
    T1566.002: Spearphishing Link
  T1059: Command and Scripting Interpreter
    T1059.001: PowerShell
    T1059.003: Windows Command Shell

SUB-TECHNIQUES: Specific variant of a technique

USAGE:
  ATT&CK Navigator: heat map of coverage
  Detection mapping: "which of our SIEM rules covers which techniques?"
  Threat intel: "threat actor group X uses which techniques?"
  Red team planning: "simulate techniques from the most relevant threat actors"
```

---

## Tabletop Exercises

Tabletop exercises are scenario-based discussions where participants walk through their response to a hypothetical incident. No actual attack occurs.

```
TABLETOP EXERCISE STRUCTURE

PARTICIPANTS:
  CISO, VP Engineering, Legal, Communications, key engineers
  Facilitated by security team or external firm

SCENARIO EXAMPLE:
  "At 2am on Black Friday, your monitoring team alerts that database
  query patterns are anomalous. Within 30 minutes, a ransom note appears
  on 40% of your file servers. What do you do?"

DISCUSSION QUESTIONS:
  - Who makes the decision to take down production?
  - Who authorizes paying the ransom (if at all)?
  - Who notifies the board?
  - What is the customer notification timeline?
  - Which regulators do you notify, and when?
  - Who controls the public statement?
  - How do you communicate without compromised systems?

VALUE:
  Surfaces gaps in IR plan (who has authority for what?)
  Tests communication protocols (can the IR plan actually be reached
    if email/Teams is down?)
  Aligns executives: agreed decisions made BEFORE the incident

FREQUENCY: Annually at minimum; quarterly for high-risk organizations
           Rotate scenarios: ransomware, insider threat, data breach,
           supply chain, social media crisis
```

---

## Common Confusion Points

**"Pen test = red team"**
Pen tests assess a scoped surface for vulnerabilities. Red teams simulate a real adversary over months to test the entire organization's detection and response. A clean pen test does not mean a red team would fail — they often succeed through vectors pen tests never test (phishing, physical, supply chain).

**"Bug bounty replaces pen testing"**
They are complementary. Bug bounties provide continuous broad coverage. Pen tests provide systematic, scoped coverage with a guaranteed deliverable. For compliance (SOC 2, PCI DSS), scheduled pen tests are typically required; bug bounties are supplementary.

**"Purple team is red team + blue team combined"**
Purple team is a structured collaboration exercise, not a merger. Red and blue teams maintain separate perspectives; purple team is the periodic exercise where they share knowledge. Merged red-blue is counterproductive — the red team needs to test the blue team's actual detection.

**"ATT&CK coverage of 80% means we detect 80% of attacks"**
ATT&CK coverage means you have detection rules for 80% of catalogued techniques. Attackers use novel techniques not yet in ATT&CK, evade existing rules, and chain techniques in uncovered combinations. ATT&CK coverage is a floor for detection maturity assessment, not a guarantee.

---

## Decision Cheat Sheet

| Scenario | Recommended Approach |
|----------|---------------------|
| New application before launch | Pen test (scoped, find vulns before attackers) |
| Annual security validation | Penetration test (compliance + systematic) |
| Test entire security program (people/process/tech) | Red team engagement |
| Validate specific detection rule works | Purple team exercise |
| Leadership alignment on incident response | Tabletop exercise |
| Continuous external vulnerability discovery | Bug bounty program |
| Identify undetected threats in environment | Threat hunting |
| Measure ATT&CK detection coverage | Purple team + ATT&CK Navigator heat map |
