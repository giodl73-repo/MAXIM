# Network Security: Segmentation, Firewall Rules, TLS Pinning, DNSSEC

## The Big Picture

Network security controls the flow of traffic between systems, enforcing who can talk to what, how, and under what conditions. The evolution: from perimeter-only (firewall at the edge) to zero trust (authenticate and authorize every flow, everywhere).

```
NETWORK SECURITY LAYERS
+-----------------------------------------------------------------------+
|                                                                       |
|  LAYER 7 (Application)                                               |
|  WAF (Web Application Firewall): HTTP/HTTPS inspection               |
|  API Gateway: auth, rate limiting, routing                           |
|                                                                       |
|  LAYER 4-7 (Transport + Application)                                 |
|  NGFW (Next-Gen Firewall): stateful, TLS inspection, IDS/IPS        |
|  Zero Trust Network Access (ZTNA): identity-aware access            |
|                                                                       |
|  LAYER 3-4 (Network + Transport)                                     |
|  Classic Firewall: IP/port-based packet filter                       |
|  Network Segmentation: VLANs, subnets, NSGs                        |
|                                                                       |
|  LAYER 2 (Data Link)                                                 |
|  802.1X port authentication                                          |
|  VLAN tagging                                                        |
|                                                                       |
|  TRANSPORT SECURITY (spans all layers)                               |
|  TLS 1.3: encryption + authentication for all TCP                   |
|  DNSSEC: authenticated DNS responses                                 |
|  mTLS: mutual authentication for service-to-service                 |
+-----------------------------------------------------------------------+
```

---

## Network Segmentation Models

### Flat vs. Segmented vs. Microsegmented

```
FLAT NETWORK (avoid):
  All hosts on 10.0.0.0/8
  Any host can reach any other host
  Compromised workstation → reach production DB directly
  VSTS/TFS era internal networks often looked like this

VLAN SEGMENTATION (basic):
  10.0.1.0/24 - DMZ (public-facing)
  10.0.2.0/24 - Application servers
  10.0.3.0/24 - Database servers
  10.0.4.0/24 - Management

  Firewall rules at zone boundaries
  Compromised web server → cannot directly reach DB (must go through FW)
  But within a zone: still flat

AZURE VNET SEGMENTATION:
  VNet: 10.0.0.0/16
  Subnet: payment-svc  10.0.1.0/24  NSG: allow inbound 443 from appsvc
  Subnet: order-svc    10.0.2.0/24  NSG: allow inbound 443 from payment-svc
  Subnet: db-tier      10.0.3.0/24  NSG: allow inbound 1433 from order-svc only
  Subnet: bastion      10.0.4.0/24  NSG: allow RDP/SSH from Bastion only

  Default deny: NSGs deny all unless explicitly permitted

MICROSEGMENTATION (zero trust):
  Policies at individual workload level (pod, VM, container)
  East-west inspection: even same-subnet traffic is inspected
  Service mesh mTLS: every service-to-service call authenticated
  Azure Firewall Premium: FQDN-based rules, TLS inspection, IDPS
```

### NSG Rule Design (Azure)

```
AZURE NSG RULE STRUCTURE:
  Priority: 100–4096 (lower = higher priority), evaluated in order
  Direction: Inbound or Outbound
  Protocol: TCP, UDP, ICMP, *
  Source: IP range, service tag, application security group
  Destination: IP range, service tag, application security group
  Port range: single port, range, or *
  Action: Allow or Deny

DESIGN PRINCIPLES:
  Start with a DENY ALL inbound rule at high priority (4000)
  Add explicit ALLOW rules at lower priority numbers
  Use service tags instead of IP ranges where possible
    (AzureLoadBalancer, Internet, VirtualNetwork, Storage.WestUS)
  Use Application Security Groups (ASG) to group VMs logically:
    ASG: web-tier, app-tier, db-tier
    Rule: allow from web-tier to app-tier on 443

DEFAULT NSG RULES (cannot delete, only override):
  AllowVnetInBound: VNet to VNet always allowed (65000)
  AllowAzureLoadBalancerInBound: LB health probes (65001)
  DenyAllInBound: default deny all (65500)
  AllowVnetOutBound: VNet to VNet outbound (65000)
  AllowInternetOutBound: VNet to Internet outbound (65001)
  DenyAllOutBound: (65500)
```

---

## Next-Generation Firewall (NGFW)

Classic firewalls are stateful packet filters (L3/L4: IP + port). NGFWs inspect at L7 (application layer) and integrate IDS/IPS.

```
NGFW CAPABILITIES VS. CLASSIC FIREWALL

CLASSIC FIREWALL:
  Rule: Allow TCP from 10.0.1.0/24 to 10.0.3.0/24 on port 443
  ✓ IP-based
  ✓ Port-based
  ✗ Cannot inspect TLS payload
  ✗ Cannot identify application (TLS on 443 could be web, gRPC, database)

NGFW ADDITIONS:
  Application identification: "This is Zoom, not generic HTTPS"
  TLS inspection: decrypt, inspect, re-encrypt
  IDS/IPS: signature-based + behavioral detection
  URL filtering: block known-malicious domains
  DNS sinkholing: redirect C2 domains to internal server
  User identity: rule based on username, not just IP
  File inspection: scan downloads for malware
  Sandboxing: detonate suspicious files in isolated VM

AZURE FIREWALL PREMIUM:
  IDPS: intrusion detection and prevention
  TLS inspection: certificate-based decrypt + inspect + re-encrypt
  URL filtering + web categories
  FQDN-based rules: allow by domain name, not just IP
  Threat intelligence: Microsoft threat feed for known-bad IPs/domains
```

### TLS Inspection Trade-offs

```
TLS INSPECTION:
  Firewall terminates TLS from client
  Firewall presents its own certificate (signed by internal CA)
  Firewall sends traffic to server with new TLS session
  Client must trust internal CA → install CA in trust store

RISKS:
  Breaks certificate pinning (client won't trust substituted cert)
  Privacy: firewall sees decrypted traffic → must be handled carefully
  Performance: TLS termination + re-encryption at scale is expensive
  Regulatory: may violate data handling regulations for certain traffic

USE WHEN:
  Inspecting outbound traffic from internal network to internet
  Inspecting east-west traffic in high-security environments
  NOT: for employee personal traffic (legal/privacy concerns)
```

---

## Zero Trust Network Access (ZTNA)

ZTNA replaces the VPN model. VPN grants broad network access; ZTNA grants per-application, per-session access.

```
VPN MODEL:
  Employee → VPN → Access to entire corporate network
  Compromised VPN credential → lateral movement across all systems

ZTNA MODEL:
  Employee → Identity verification + Device health check
           → Per-application access (only app X, not the whole network)
           → Session-limited access
           → Continuous validation (device still compliant? anomalous behavior?)

ZTNA PRODUCTS:
  Azure: Entra Private Access (Microsoft's ZTNA, replacing Azure AD App Proxy)
  Zscaler Private Access (ZPA)
  Cloudflare Access
  Palo Alto Prisma Access
  Cisco Duo / Cisco ZTNA

HOW IT WORKS:
  1. User authenticates to ZTNA control plane (identity + MFA + device check)
  2. Control plane evaluates policy: user X on compliant device can access app Y
  3. Access granted via encrypted tunnel directly to app, not the network
  4. App never exposed to internet (no public IP)
  5. Control plane logs all access, monitors for anomalies
```

---

## TLS Pinning

TLS pinning tells a client to trust a specific certificate or public key, rather than any certificate signed by a trusted CA.

```
CERTIFICATE PINNING:
  App hardcodes: "Only trust this specific certificate (or its hash)"
  If MITM attacker presents a different valid cert: connection rejected

PUBLIC KEY PINNING:
  App hardcodes the public key hash (SPKI hash): "Only trust this key"
  More flexible: key can be on different certificates (renewal OK)

HTTP PUBLIC KEY PINNING (HPKP) — DEPRECATED:
  Was a browser mechanism via response header
  Deprecated in 2018: too many sites misconfigured and bricked their own HTTPS
  "HPKP pin was lost / wrong → site unreachable for all users for months"
  Firefox removed it; Chrome deprecated it

CURRENT RECOMMENDATION:
  Mobile apps: pin to a certificate pinset (e.g., 2 backup pins)
    Handle rotation gracefully with app update
    Use pin + backup pin: both certs kept in infra
  Web browsers: do NOT use HPKP (deprecated)
    Use CAA DNS records to restrict which CAs can issue for your domain
    Use Certificate Transparency (CT) logs + monitoring instead

CERTIFICATE TRANSPARENCY (CT):
  All public certs must be logged in append-only CT logs
  Any cert issued for your domain is publicly logged
  Monitoring: alert when unexpected cert is issued for your domain
  Tool: crt.sh (search CT logs), Google CT viewer
```

---

## DNSSEC

DNS is unsigned by default — responses can be forged (DNS spoofing/cache poisoning). DNSSEC adds cryptographic signatures to DNS records.

```
DNS WITHOUT DNSSEC:
  Resolver asks: "What is the IP of api.contoso.com?"
  Attacker intercepts and responds with malicious IP
  Resolver has no way to verify the answer is authentic
  Client connects to attacker's server (MITM)

DNSSEC CHAIN OF TRUST:
  Root zone (.) → is signed by IANA's KSK (Key Signing Key)
  .com zone     → root zone signs .com zone's DNSKEY
  contoso.com   → .com signs contoso.com's DNSKEY
  api.contoso.com → contoso.com signs the A record

  DS (Delegation Signer) record in parent zone proves child zone's key

VALIDATION:
  DNSSEC-validating resolver checks signatures at each step
  Any forged or tampered response → validation fails → SERVFAIL
  Client gets error (cannot connect) rather than connecting to attacker

LIMITS OF DNSSEC:
  Does NOT encrypt DNS traffic (responses are still in plaintext)
  → Use DNS over HTTPS (DoH) or DNS over TLS (DoT) for privacy
  Adoption is incomplete: not all zones are signed
  Azure DNS supports DNSSEC for Azure DNS zones (GA 2024)

RELATED:
  DoH (DNS over HTTPS): DNS queries sent over HTTPS → encrypted + private
    Browsers use directly (Firefox, Chrome configurable)
  DoT (DNS over TLS): DNS over TLS port 853
    Supported by Android, iOS, some resolvers
```

---

## Network Detection and Response (NDR)

NDR monitors network traffic to detect anomalous patterns that indicate compromise:

```
NDR DATA SOURCES:
  NetFlow / IPFIX: metadata (src/dst IP, port, protocol, bytes, packets)
  Full packet capture (PCAP): for forensics (expensive storage)
  DNS logs: queries, responses, anomalous domains
  TLS metadata: certificate details, version, cipher (without decrypting)

NDR DETECTION METHODS:
  Behavioral: "this server normally doesn't beacon out every 60s"
  Signature: "this domain matches a known C2 pattern"
  ML-based: anomaly detection on traffic volume, timing
  Threat intelligence: known-bad IPs, domains, JA3 fingerprints (TLS)

JA3 FINGERPRINTING:
  Hash of TLS ClientHello parameters (version, cipher suites, extensions)
  Identifies TLS client implementation (browser, malware family)
  C2 frameworks have distinctive JA3 hashes
  Tool: Zeek, Suricata, Corelight

AZURE EQUIVALENT:
  Microsoft Sentinel (SIEM): ingests NSG flow logs, Azure Firewall logs
  Defender for Endpoint: EDR + network telemetry from endpoints
  Defender CSPM: cloud posture and network exposure
```

---

## Common Confusion Points

**"A firewall is sufficient for network security"**
A firewall at the perimeter is necessary but not sufficient. An attacker who gets past the perimeter (phishing, VPN compromise, supply chain) faces no resistance in a flat internal network. Defense in depth requires controls at every layer.

**"ZTNA eliminates the need for segmentation"**
ZTNA enforces identity-based access; segmentation limits blast radius when ZTNA is bypassed or a legitimate account is compromised. Both are needed. ZTNA for access policy, segmentation for containment.

**"TLS means the connection is secure"**
TLS encrypts the connection and authenticates the server (certificate). It does not authenticate the client (unless mTLS), does not protect against valid credentials being stolen, and does not protect the application layer (SQL injection can happen over TLS).

**"DNSSEC prevents all DNS attacks"**
DNSSEC prevents cache poisoning and response forgery. It does not prevent: DDoS against DNS servers, DNS rebinding attacks (requires browser mitigations), compromised authoritative servers (signature key compromise), or typosquatting (different domain, valid signature).

---

## Decision Cheat Sheet

| Requirement | Control |
|-------------|---------|
| Isolate web tier from DB tier | Subnet segmentation + NSG deny rules |
| Detect lateral movement inside VNet | NSG flow logs → Sentinel |
| HTTP/HTTPS attack protection | WAF (Azure Application Gateway WAF, Front Door WAF) |
| L7 outbound inspection | Azure Firewall Premium (FQDN rules + IDPS) |
| Replace VPN for remote employee access | ZTNA (Entra Private Access, Zscaler, Cloudflare) |
| Service-to-service authentication | mTLS via service mesh (Istio) |
| Prevent certificate forgery monitoring | Certificate Transparency monitoring |
| DNS response authenticity | DNSSEC + CAA records |
| DNS query privacy | DoH or DoT at resolver level |
| Detect C2 beaconing | NDR / Sentinel + DNS anomaly detection |
