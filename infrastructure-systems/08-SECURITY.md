# Infrastructure Security: ICS/SCADA, OT/IT Convergence, Defense in Depth

## The Big Picture

Infrastructure security has two largely separate domains: physical security (fences, guards,
access control) and cybersecurity. Physical security is mature and well-understood. Cyber
is the fast-moving frontier. The defining challenge: operational technology (OT) --
the industrial control systems that run physical infrastructure -- was designed for
reliability and safety, not security. It is now connected to corporate IT networks and
increasingly to the internet, without security architectures commensurate with that exposure.

```
INFRASTRUCTURE ATTACK SURFACE
================================

   PHYSICAL ATTACK SURFACE            CYBER ATTACK SURFACE
   =====================              ====================
   Substations (5,000+ in US)         Internet-exposed ICS (Shodan: 50k+ devices)
   Dams, water treatment plants       IT/OT convergence points (historians)
   Pipeline pump/compressor stations  Remote access VPNs (vendor maintenance)
   Telecom switching centers          Engineering workstations (dual-homed)
   Data centers (cloud providers)     Supply chain (firmware, software updates)
   Underwater cables (96% of traffic) Insider threat (disgruntled operators)

   COMBINED (compound):
   Physical access enables cyber: attacker inside perimeter -> USB/console access
   Cyber enables physical damage: Stuxnet, CRASHOVERRIDE destroyed physical equipment

ATTACK CONSEQUENCE SPECTRUM:
  Level 0: Data theft, no operational impact
  Level 1: Operational disruption (brief outage, controlled recovery)
  Level 2: Extended outage, economic damage ($1M - $1B)
  Level 3: Physical equipment damage, recovery weeks-months (Colonial, Ukraine power)
  Level 4: Catastrophic physical damage with casualties (Stuxnet category; hypothetical US grid attack)

MOST DANGEROUS INFRASTRUCTURE TARGETS (by consequence):
  1. Bulk electric grid (cascading blackout potential)
  2. Natural gas pipeline network (explosion/supply disruption)
  3. Water treatment systems (mass poisoning potential)
  4. Nuclear facilities (radiological release risk)
  5. Financial infrastructure (economic disruption)
  Per CISA: energy + water are highest consequence; most actively targeted
```

---

## ICS/SCADA Architecture

### The Purdue Model

```
PURDUE ENTERPRISE REFERENCE ARCHITECTURE (ISA-95)
===================================================

A layered model for industrial control system architecture.
Original design: isolation by layer; security = no communication between layers.
Current reality: IT/OT convergence eroded layer separation everywhere.

LEVEL 5: ENTERPRISE NETWORK (IT)
+-------------------------------------------------------+
| ERP systems (SAP, Oracle)                             |
| Business intelligence, analytics                      |
| Corporate email, internet access                      |
| Cloud connectivity                                    |
+-------------------------------------------------------+
                         |  ← ENTERPRISE/DMZ FIREWALL
LEVEL 4: SITE BUSINESS PLANNING / LOGISTICS
+-------------------------------------------------------+
| Production scheduling                                 |
| Site-level IT (Active Directory, file shares)         |
| Engineering workstations (often dual-homed to L3)     |
+-------------------------------------------------------+
                         |  ← IT/OT FIREWALL (THE CRITICAL BOUNDARY)
                         |    (often poorly implemented; many exceptions poke holes)
LEVEL 3: MANUFACTURING OPERATIONS MANAGEMENT (IT/OT BOUNDARY)
+-------------------------------------------------------+
| Historian servers (OSIsoft PI, GE Historian)          |  ← HIGHEST-RISK COMPONENT
| MES (Manufacturing Execution System)                  |  aggregates OT data to IT
| Remote access termination (vendor VPN gateway)        |
| Data diode or unidirectional security gateway         |
+-------------------------------------------------------+
                         |  ← OT FIREWALL
LEVEL 2: SUPERVISORY CONTROL
+-------------------------------------------------------+
| SCADA servers                                         |
| HMIs (Human Machine Interfaces)                       |
| Engineering stations (PLC programming tools)          |
| DCS (Distributed Control Systems)                     |
| Historian data collection agents                      |
+-------------------------------------------------------+
LEVEL 1: BASIC CONTROL
+-------------------------------------------------------+
| PLCs (Programmable Logic Controllers)                 |
| RTUs (Remote Terminal Units)                          |
| IEDs (Intelligent Electronic Devices - substations)   |
| Safety Instrumented Systems (SIS)                     |
+-------------------------------------------------------+
LEVEL 0: PHYSICAL PROCESS
+-------------------------------------------------------+
| Sensors (temperature, pressure, flow, vibration)      |
| Actuators (valves, motors, pumps, circuit breakers)   |
| Physical infrastructure being controlled              |
+-------------------------------------------------------+

HISTORIAN SERVER: THE CRITICAL VULNERABILITY POINT
  Function: collects real-time data from Level 2 OT; makes available to Level 3/4 IT
  Problem: sits in both OT and IT network -> by design, bridges the air gap
  Exposure: if historian compromised, attacker has data visibility into OT network
  Lateral movement risk: historian with OT network access = pivot point for attack
  Example: Colonial Pipeline attack used IT network; but IT/OT integration via
           billing/dispatch systems forced OT shutdown
```

### ICS Protocols

```
ICS COMMUNICATION PROTOCOLS
==============================

PROTOCOL    DESIGN ERA  SECURITY    USED IN              VULNERABILITY
----------  ----------  ----------  -------------------  ------------------
Modbus      1979        None        HVAC, manufacturing, No auth, no encrypt;
                                    water/wastewater     raw TCP Modbus/TCP
                                                         anyone can send cmds
DNP3        1990s       None        Electric utilities,  No auth on base DNP3;
                                    water utilities,     DNP3 Secure Auth (SA)
                                    oil/gas pipelines    added 2012, slow adopt
IEC 61850   2003-2013   Partial     Substation automation GOOSE messages: pub/sub,
                                    (protection relays)  no auth on local LAN;
                                                         fast (ms-class latency)
PROFINET    2004        None-Low    Factory automation   ARP spoofing, MITM easy
                                    manufacturing OT
OPC-DA      1996        Windows     Historian integration Legacy Windows auth;
                                                         OPC DA = COM/DCOM
                                                         (classic Windows holes)
OPC-UA      2008        Yes         Modern systems       TLS, certs, roles -- but
                                                         complex implementation;
                                                         profile violations common
EtherNet/IP 2001        None        Rockwell PLCs,       No auth; Modbus-like
                                    manufacturing        exposure on TCP/44818

KEY POINTS:
  Modbus: the most-deployed protocol worldwide; zero security by design
  DNP3: electric utilities standard; Secure Authentication (SA) adoption still <50%
  IEC 61850 GOOSE: protection relay tripping messages; sub-1ms required; auth would add latency
    -> security vs. protection function trade-off; unresolved in most deployments
  Modern approach: put all legacy protocols on encrypted VPN tunnels / data diodes

SHODAN EXPOSURE REALITY:
  Shodan.io: internet-connected device search engine
  Searches for: open Modbus (port 502), DNP3 (port 20000), BACnet (port 47808), etc.
  Finds: PLCs, SCADA servers, building automation, water treatment
  US water systems: researchers regularly find exposed ICS with simple Shodan queries
  2021 Oldsmar, FL attack: attacker used TeamViewer remote access; raised NaOH to 111x normal
    (operator noticed mouse movement; reduced manually; no harm but demonstrated ease of access)
  NIST 800-82 Guide to ICS Security: foundational reference; not mandatory for water utilities
  Gap: AWIA 2018 mandates water utility risk assessment; does NOT mandate specific controls
```

---

## Threat Actor Taxonomy

```
INFRASTRUCTURE THREAT ACTORS
===============================

NATION-STATE:
  Capability: highest; zero-days, custom malware, patient (years-long access)
  Intent: espionage + pre-positioning for wartime disruption
  Notable examples:
    Russia Sandworm (GRU Unit 74455):
      CRASHOVERRIDE/Industroyer 2016: Ukraine power grid; 200,000 customers, 1 hr outage
      Industroyer2 2022: attempted repeat Ukraine attack (April 2022, pre-empted by CERT-UA)
      NotPetya 2017: destructive wiper disguised as ransomware; $10B global damage
    China Volt Typhoon (2023): pre-positioning in US critical infrastructure
      Multiple US utilities, ports, communications: "living off the land" techniques
      No destructive intent detected yet; assumed pre-positioning for Taiwan contingency
    Iran CyberAv3ngers (2023): attacked water utilities using Unitronics PLCs
      (Unitronics PLCs are internet-connected with default credentials)
      CISA emergency advisory; 4+ US water utilities affected
    US/Israel Stuxnet (2010): gold standard ICS attack (see 04-FAILURE-MODES.md)

CRIMINAL (RANSOMWARE):
  Capability: moderate; use leaked tools, off-the-shelf exploit kits
  Intent: financial extortion ($1M-$50M ransom demands for critical infrastructure)
  Approach: encrypt business/IT systems; threaten data leak; demand ransom
  Notable examples:
    Colonial Pipeline 2021: DarkSide; $4.4M paid; 6-day shutdown
    Oldsmar 2021: TeamViewer attack (attribution uncertain)
    Veolia Water North America 2024: ransomware on billing systems
    US hospitals (ongoing): ransomware diverts ambulances; patient harm documented
  Concern: ransomware gangs don't distinguish military from civilian targets

HACKTIVIST:
  Capability: low-moderate; use public exploit tools, DDoS, website defacement
  Intent: political statement, protest; rarely destructive
  Examples: Killnet (pro-Russian DDoS on EU/NATO infrastructure sites 2022)
            Anonymous infrastructure targets (BART 2011, etc.)

INSIDER THREAT:
  Capability: high; knows the systems, has legitimate access, knows vulnerabilities
  Types:
    Malicious: disgruntled employee; sells access; sabotages
    Negligent: clicks phishing email; uses weak passwords; bypasses security policy
    Unwitting: credentials stolen without their knowledge
  Examples:
    San Francisco BART 2011: IT admin installed rogue code (thwarted)
    Maroochy Shire 2000: ex-contractor (Vitek Boden) hacked Queensland sewage SCADA;
      spilled 800,000L raw sewage; first convicted ICS attacker
    2014 South Houston water utility: disgruntled ex-employee modified SCADA
  Mitigation: least privilege, separation of duties, behavior analytics (UEBA)
```

---

## Defense in Depth

### The ICS Security Architecture

```
ICS DEFENSE-IN-DEPTH ARCHITECTURE
=====================================

CONCEPT: Security at every layer; no single point of failure.
          Attacker must defeat multiple independent security measures.

LAYER 1: PHYSICAL SECURITY
  Fencing, perimeter (NERC CIP-006 for electric critical assets)
  Badged access control for control rooms, equipment rooms
  Video surveillance, motion detection
  NERC CIP-014: physical security for high-impact substations
  Man-trap entry (no tailgating)
  Laptop/USB restrictions at physical entry

LAYER 2: NETWORK SEGMENTATION
  OT network ≠ IT network (must be enforced, not just designed)
  Firewall rules: explicit allow list (not "deny some")
    Rule: only allow specific, necessary protocols/ports between zones
    No default-allow rules; log all traffic
  VLAN segmentation within OT: protect Level 1/2 from Level 3
  Air gap where feasible: truly no electronic connection
    Data diode (one-way gateway): passes data to IT, cannot receive from IT
      e.g., Waterfall Security Solutions, Owl Cyber Defense: hardware-enforced one-way
      Used in: nuclear facilities, high-security substations
  Jump server: required intermediate step for all IT→OT connections
    Single audit point; MFA required; all sessions logged/recorded

LAYER 3: IDENTITY AND ACCESS MANAGEMENT
  NERC CIP-004 / CIP-007: personnel risk assessment; access management
  Multi-factor authentication: mandatory for all remote access to ICS
    (TSA Security Directive for pipelines; NERC CIP for bulk electric)
  Privileged access management (PAM): CyberArk, BeyondTrust for OT
    Vendor accounts: temporary access only; just-in-time provisioning
    No shared accounts; no shared credentials (primary source of incidents)
  Role-based access: operators vs. engineers vs. read-only; least privilege
  Session recording: Privileged session management records ICS sessions for audit
  Account lifecycle: ex-employees terminated within hours (Maroochy Shire failure here)

LAYER 4: PATCH AND VULNERABILITY MANAGEMENT
  Challenge: OT patching is difficult and risky
    Patching windows: must coordinate with operational schedules
    Testing: patches must be tested in non-production environment
    Vendor qualification: some ICS vendors void warranty if patched without testing
    Embedded OS: some PLCs run EOL Windows XP/CE with no available patches
  NERC CIP-007: patch management program required; security patches assessed within 35 days
  Compensating controls: if can't patch, compensate (network isolation, monitoring)
  Asset inventory: can't patch what you don't know about
    OT asset discovery: Claroty, Dragos, Nozomi Networks: passive OT asset discovery
    (active scanning can crash fragile ICS -- passive is the standard approach)

LAYER 5: DETECTION AND MONITORING
  OT-specific SIEM / anomaly detection:
    Dragos: OT threat intelligence + monitoring; tracks nation-state activity groups
    Claroty: network visibility + anomaly detection for OT
    Nozomi Networks: passive OT monitoring; asset inventory + anomaly
    PLC behavioral analytics: detect unexpected changes to PLC logic (Integrity Check)
  Network flow analysis: NetFlow from OT switches; unusual communication patterns
  Honeypot ICS: fake PLCs/HMIs that detect reconnaissance and attack activity
  SIEM integration: OT alerts → SOC (Security Operations Center)
    Problem: IT SOC analysts often lack OT context (false positive hell)
    Solution: dedicated OT SOC or OT-trained tier in SOC

LAYER 6: INCIDENT RESPONSE
  ICS incident response is different from IT IR:
    Shut-down vs. restore: IT restores fast; OT must verify physical system safety before restart
    Safe state: ICS must fail to known safe state; restoration involves field verification
    No-touch zones: some systems cannot be touched without safety risk
  ICS IR teams: CISA ICS-CERT responds to infrastructure incidents (24/7 hotline)
    Private sector: Dragos, Mandiant, Claroty, Honeywell GARD all offer ICS IR
  Playbooks: sector-specific (E-ISAC for electric, WaterISAC for water)
  Exercises: NERC GridEx (biennial; largest grid security exercise in North America)
    2022 GridEx VI: 250+ organizations; ~6,600 participants; simulated physical + cyber
```

### NERC CIP: The Mandatory Framework

```
NERC CIP (CRITICAL INFRASTRUCTURE PROTECTION) STANDARDS
==========================================================

APPLICABILITY: Bulk Electric System (BES) in North America
  Enforced by NERC; overseen by FERC
  Penalties: up to $1M per violation per day
  NOT applicable to: water, gas, distribution-only utilities, private companies

STANDARDS OVERVIEW:
  CIP-002: Asset identification; classify assets by impact (High/Medium/Low)
  CIP-003: Security management controls (policies, procedures)
  CIP-004: Personnel training and access; background checks
  CIP-005: Electronic security perimeters (ESP) definition and protection
  CIP-006: Physical security of BES cyber systems
  CIP-007: Systems security management (ports/services, patch, logging)
  CIP-008: Incident reporting and response planning
  CIP-009: Recovery plans for BES cyber systems
  CIP-010: Configuration change management and vulnerability management
  CIP-011: Information protection
  CIP-012: Communications between control centers (protection)
  CIP-013: Supply chain risk management (hardware/software vendors)
  CIP-014: Physical security (high-impact substations + control centers)

CIP EFFECTIVENESS CRITICISM:
  Compliance ≠ security: meeting CIP checklist doesn't mean secure
  Low-impact asset exemptions: most distribution assets exempted from CIP
  Supply chain gap: CIP-013 (2020) is relatively new; supply chain risk still high
  SolarWinds/SUNBURST (2020): software supply chain attack; CIP-013 wouldn't have caught it
  Defense-in-depth maturity: CIP compliance is floor, not ceiling

WATER SECTOR: NO EQUIVALENT TO NERC CIP
  AWIA 2018 (America's Water Infrastructure Act):
    Community water systems >3,300 connections: must conduct risk and resilience assessment
    Must certify to EPA within required cycle (varies by size)
    Must develop Emergency Response Plan
    Mandatory reporting: EPA notified of incidents affecting public health
  What AWIA does NOT require: specific security controls (unlike NERC CIP's specificity)
  Result: significant variance in water sector security maturity
  Recent legislation: Water Risk and Resilience Organization (WRRO) proposed but not enacted
```

---

## Supply Chain Security

```
ICS SUPPLY CHAIN THREATS
==========================

ATTACK VECTORS:
  Compromised firmware: malicious code in device firmware (networking equipment, PLCs)
    SeaLevelCom 2013: NSA JETPLOW implants in Cisco firewall firmware
    Juniper 2015: unauthorized code in ScreenOS (VPN backdoor inserted)
  Compromised software updates: legitimate update channel used to push malware
    SolarWinds Orion 2020 (SUNBURST): 18,000 organizations received backdoored update
    Not power grid OT but widely used for IT network management; overlap with utilities
    Kaseya VSA 2021: REvil used MSP software update to push ransomware to 1,500 organizations
  Counterfeit hardware: fake components with hidden functionality
    2018 Bloomberg Supermicro story (disputed): alleged hardware implants in server motherboards
    Documented: counterfeit Cisco equipment in government networks
  Insider at vendor: malicious code inserted by employee of hardware/software vendor
  Nation-state SolarWinds type attack tailored to ICS vendors (theoretical but credible)

NERC CIP-013 SUPPLY CHAIN REQUIREMENTS:
  Applicable to: High and Medium Impact BES Cyber Systems
  Requires: supply chain cyber security risk management plan
  Vendor risk factors to assess: software integrity, authenticity, known vulnerabilities
  Limitations: self-attestation acceptable; no third-party audit required
  Does not require: software bill of materials (SBOM) -- though executive order 14028 does

EXECUTIVE ORDER 14028 (2021, Biden): Software Supply Chain Security
  Requires SBOM for software sold to federal government
  SBOM: Software Bill of Materials -- complete inventory of open-source components
    Like a food ingredient list for software; enables vulnerability tracking
  CISA guidance on SBOM: https://www.cisa.gov/sbom
  Relevance to ICS: most ICS software uses open-source components;
    SBOM would enable operators to know when Log4Shell-class vulnerabilities apply to their PLCs
  Adoption: uneven; some ICS vendors beginning to provide SBOMs; not standard yet

HARDWARE SECURITY:
  Trusted Platform Module (TPM): cryptographic root of trust in hardware
    ICS devices increasingly shipping with TPM 2.0; firmware integrity verification
  Secure Boot: verify firmware hash at startup; prevents modified firmware running
  Code signing: software updates signed; device verifies signature before installing
  These are necessary but not sufficient: protect against modification, not hardware implants
```

---

## Incident Response and Sector Coordination

```
SECTOR SECURITY COORDINATION
================================

INFORMATION SHARING ORGANIZATIONS:
  E-ISAC (Electricity ISAC): operated by NERC
    Threat intelligence sharing among electric utilities
    GridEx: biennial large-scale grid security exercise
    24/7 security operations center; incident coordination
    Membership: ~1,900 members (virtually all bulk power utilities)

  WaterISAC: operated by Water Information Sharing and Analysis Center
    Threat intelligence for water/wastewater sector
    Incident reports, vulnerability notifications, training
    Membership: ~3,000 member organizations (water utilities, WWTP)
    Budget: much smaller than E-ISAC; sector has less funding for security

  ONG-ISAC: Oil and Natural Gas
  A-ISAC: Aviation
  MS-ISAC: Multi-State ISAC (state and local government)

GOVERNMENT AGENCIES:
  CISA (Cybersecurity and Infrastructure Security Agency):
    Lead federal agency for infrastructure security (created 2018 from DHS/NPPD)
    ICS-CERT program: technical assistance for ICS incidents (now incorporated into CISA)
    CISA advisories: regular public advisories on ICS vulnerabilities
    Free services: Cyber Hygiene scanning, CISA vulnerability assessment teams
    Binding Operational Directives (BOD): apply to federal civilian agencies
    CISA reporting requirement: 72-hr incident reporting for critical infrastructure owners
      (CIRCIA 2022: Cyber Incident Reporting for Critical Infrastructure Act)

  NSA: signals intelligence; shares threat intelligence with CISA via advisories
  FBI: cybercrime investigation; criminal prosecution; InfraGard partnership program
  FERC: regulates electric transmission; enforces NERC CIP compliance
  EPA: water sector oversight; AWIA enforcement
  TSA: pipeline and aviation cybersecurity (post-Colonial TSA directives)

CIRCIA 2022 (CYBER INCIDENT REPORTING FOR CRITICAL INFRASTRUCTURE ACT):
  Covered entities (critical infrastructure operators): must report
    Substantial cyber incidents: within 72 hours of discovery
    Ransomware payments: within 24 hours of payment
  CISA receives reports; can share with sector-specific agencies
  Rulemaking: final rules expected 2025-2026; specifics of "covered entities" still TBD
  Goal: create visibility into incidents that previously went unreported
```

---

## Decision Cheat Sheet

| Security question | Answer |
|-------------------|--------|
| What is the Purdue Model? | Layered IT/OT architecture (L0 physical to L5 enterprise); security designed around layer separation |
| Why is the historian server dangerous? | Sits at IT/OT boundary; by design bridges air gap; pivot point for OT access from IT side |
| Most deployed ICS protocol | Modbus (1979); zero security by design; plaintext, no authentication |
| What did CRASHOVERRIDE do? | 2016 Ukraine power grid; automated relay manipulation to open breakers; 200k customers blacked out |
| Water sector equivalent of NERC CIP? | None at equivalent depth; AWIA 2018 requires risk assessment but not specific controls |
| Data diode purpose | Hardware-enforced one-way gateway: OT data flows to IT; nothing flows back; prevents IT→OT attacks |
| What is CIRCIA? | 2022 law requiring 72-hr incident reporting and 24-hr ransomware payment disclosure for critical infrastructure |
| Best OT monitoring approach | Passive network monitoring (not active scanning — active scanning can crash fragile PLCs) |
| CIP-013 subject | Supply chain risk management for BES cyber systems |

---

## Common Confusion Points

**"Air-gapped OT networks are secure."** The air gap assumption is largely false in modern
infrastructure. IT/OT convergence for operational efficiency (remote monitoring, historian data
to ERP, vendor remote maintenance) has eroded most air gaps. The question is not whether an
air gap exists on paper but whether there are managed, monitored data paths between OT and
IT. Unmanaged paths (dual-homed engineering workstations, cellular-connected RTUs, USB ports)
create practical connectivity without visibility.

**"NERC CIP compliance means the grid is secure."** CIP is a compliance framework with
specific minimum requirements. It creates a floor, not a ceiling. Compliance-focused
organizations pass audits while remaining operationally vulnerable. Dragos and E-ISAC
regularly find sophisticated adversaries with persistent presence in compliant utilities.
The limitation: CIP measures are known to adversaries who design around them.

**"Ransomware can't affect OT because OT is isolated."** Colonial Pipeline is the
canonical counter-example. The OT (pipeline) was not compromised, but the IT compromise
was sufficient to force an OT shutdown. Billing and dispatch systems ran on IT; without
them, Colonial could not safely manage pipeline operations and billing. The physical
infrastructure is not always separable from the IT systems that manage it commercially.

**"Critical infrastructure attacks are nation-state only."** Oldsmar 2021, Veolia 2024,
and Maroochy Shire 2000 were not nation-state. Criminal ransomware groups increasingly
target critical infrastructure because the operational disruption creates pressure to pay.
Water utilities with minimal security budgets and minimal regulatory requirements are
soft targets. The attack surface is not limited to nation-state capable adversaries.
