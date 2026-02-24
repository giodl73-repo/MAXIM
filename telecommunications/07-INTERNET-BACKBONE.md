# Internet Backbone — A Layered Guide

## The Big Picture

The internet is a layered hierarchy of networks. The physical infrastructure
of fiber, IXPs, and submarine cables underpins the logical structure of BGP routing.

```
INTERNET TIER HIERARCHY
════════════════════════════════════════════════════════════════════

TIER 1 ISPs                            Free peering with each other
(AT&T, Lumen, Cogent, NTT,            Own backbone spanning continents
 Telia, Deutsche Telekom, GTT)         No transit payments to anyone
         │ │ │                         Connected to every other network
         │ Peering with all Tier 1s    Examples: 14-15 companies worldwide
         │
    ─────┴─────
    │         │
TIER 2 ISPs     TIER 2 ISPs             Pay Tier 1 for transit
(Regional        (Cloud providers:       Peer with others at IXPs
 ISPs, major      AWS, Azure, GCP        Sell to Tier 3 and end users
 enterprises)     have Tier 1-like       Examples: Comcast, BT, KDDI
                  networks but focus
                  on own cloud)
         │
    ─────┴─────
TIER 3 ISPs / Access Networks           Pay Tier 2/1 for transit
(Local ISPs, mobile operators,          Deliver to end users
 enterprise networks, universities)     Limited or no peering
         │
    ─────┴─────
END USERS / ENTERPRISES
```

---

## Peering vs Transit

```
BUSINESS RELATIONSHIPS IN THE INTERNET

TRANSIT:
  "I'll route your traffic anywhere, and you pay me"
  Tier 3 → pays Tier 2 or Tier 1 for access to full internet routing table
  Tier 2 → may pay Tier 1 for routes it can't reach via peering
  Transit agreement: $X per Mbps of committed capacity

PEERING:
  "We'll route traffic between our networks for free (settlement-free)"
  Both parties benefit approximately equally
  Traffic exchanged: only between the two networks' customers
  Two types: public peering (at IXP) or private peering (direct cable/dark fiber)

SETTLEMENT-FREE PEERING REQUIREMENTS:
  Similar traffic ratios (ratio of outbound:inbound ≈ 1:1 to 1:3 typical)
  Minimum traffic threshold (often several Gbps)
  Geographic presence at peering points
  "Peering dispute": one party claims asymmetric benefit → demands payment or de-peers

CONTENT-CENTRIC CHANGES:
  Google, Netflix, Meta built their own backbone networks
  These "hyperscalers" peer everywhere (300+ IXPs) → become near-Tier 1 in practice
  Netflix: 15+ Tbps peak delivered from own CDN servers, largely bypassing transit
```

---

## Internet Exchange Points (IXPs)

```
IXP STRUCTURE

An IXP is a physical facility where ISPs exchange traffic directly.

Core: Ethernet switching fabric (Layer 2)
  All members connect their routers to the IXP fabric
  Exchange routes via BGP sessions
  Traffic flows directly: no transit charges at IXP

IXP: Route server   ◄──BGP session──► ISP A router
     (optional         peer routes     announces: 192.0.2.0/24, 10.1.0.0/16...
     facilitates
     multilateral
     peering)           ──BGP session──► ISP B router
                                         announces: 203.0.113.0/24...

Physical: usually a data center, or multiple connected DCs
Size: 1 Gbps ports to 100 Gbps+ ports
Traffic: 1 Gbps (small IXP) to 10+ Tbps peak (DE-CIX Frankfurt, AMS-IX)

MAJOR IXPs (by traffic):
  DE-CIX Frankfurt: 16+ Tbps peak, 1000+ members
  AMS-IX (Amsterdam): 10+ Tbps
  LINX (London): 6+ Tbps
  NYIIX, Equinix IX (multiple US cities): 1-5 Tbps each
  JPIX (Tokyo), HKIX (Hong Kong): major Asian IXPs
  PTT Brasil (São Paulo, Rio): dominant South America

WHY IXPs MATTER:
  Without IXPs: A→B traffic might go through expensive Tier 1 transit
  With IXP: direct exchange → latency reduced, cost reduced
  "Peering reduces latency": Frankfurt ↔ Frankfurt via IXP = 1 ms; via New York = 100 ms
```

---

## BGP (Border Gateway Protocol)

BGP is the routing protocol of the internet — the glue that holds it together.

```
BGP FUNDAMENTALS

BGP: Path-vector routing protocol
  Carries: routing information between Autonomous Systems (ASes)
  Each AS: a collection of IP prefixes under one administrative domain

AUTONOMOUS SYSTEM (AS):
  Identified by ASN (Autonomous System Number)
  16-bit ASN (1-65535), now 32-bit (1-4294967295)
  Examples: AS15169 (Google), AS8075 (Microsoft), AS16509 (Amazon AWS)
  ~80,000+ active ASes globally (2024)

BGP PATH ATTRIBUTES:
  AS-PATH: list of ASes this route traversed
    Prevents loops: router discards routes containing its own AS
    Longer AS-PATH generally preferred less (shortest path heuristic)
  NEXT-HOP: IP address of next hop router
  LOCAL-PREF: internal preference (higher = prefer, internal use only)
  MED (Multi-Exit Discriminator): hint to neighbor for multi-homed exits
  COMMUNITY: 32-bit tag for routing policy (e.g., "no export", "learned from peer")

BGP DECISION PROCESS (simplified):
  1. Highest LOCAL-PREF  (set by local policy)
  2. Shortest AS-PATH
  3. Lowest MED
  4. External (eBGP) over internal (iBGP)
  5. Lowest IGP metric to next-hop
  6. Oldest route / lowest router-ID (tiebreaker)

POLICY ROUTING:
  "I prefer to reach AS15169 via my peer at DE-CIX over paying transit to reach it"
  Encoded as LOCAL-PREF manipulation on inbound BGP route
  → BGP is largely driven by business relationships, not just shortest path
```

**BGP incidents**:
```
NOTABLE BGP INCIDENTS (illustrate brittleness)

2008 Pakistan Telecom / YouTube:
  Pakistan Telecom issued more specific /24 prefix for YouTube's 208.65.153.0/22
  Misconfiguration propagated to Tier 1 ISPs → YouTube traffic blackholed worldwide
  Duration: ~2 hours; affected 2+ billion users

2010 China Telecom (15 min):
  AS23724 advertised ~50,000 prefixes (small subnets) of major networks
  Traffic for parts of US DoD, Congressional websites briefly rerouted through China
  Source still debated: misconfiguration vs intentional

2021 Facebook global outage:
  Internal BGP misconfiguration during maintenance → Facebook withdrew own AS routes
  Facebook, Instagram, WhatsApp unreachable globally for ~6 hours
  Also took down internal systems → no SSH access to fix (had to physically enter DCs)

BGPSEC / RPKI (mitigation):
  RPKI (Resource Public Key Infrastructure): cryptographically sign route origin announcements
  Route Origin Authorization (ROA): "only AS15169 can announce 8.8.8.0/24"
  BGPSEC: sign AS-PATH cryptographically (prevents path manipulation)
  Deployment: ~50% of internet routes covered by RPKI (2024), growing
```

---

## Content Delivery Networks (CDNs)

```
CDN ARCHITECTURE

Problem: User in Tokyo fetching video content from origin server in Virginia = 200 ms latency

CDN Solution:
  1. Cache content at edge servers ("PoPs" - Points of Presence) globally
  2. User requests www.example.com → DNS resolves to nearest edge server
  3. Cache hit: content served from Tokyo PoP (< 5 ms latency)
  4. Cache miss: edge fetches from origin, caches locally

MAJOR CDN PROVIDERS:
  Akamai: 4000+ PoPs, 230+ countries
  CloudFlare: 300+ PoPs, all major internet cities
  Amazon CloudFront: 450+ PoPs (AWS edge locations)
  Fastly, Google Cloud CDN, Azure CDN: similar coverage

CDN TRICKS:
  Anycast: same IP address announced from multiple PoPs, BGP routes to nearest
  TCP connection pre-establishment: anticipate requests, warm up connections
  HTTP/3 (QUIC): latency improvement for mobile users with packet loss
  Smart caching: origin pushes content proactively before requests surge
  Edge compute: run code at CDN edge (Cloudflare Workers, Lambda@Edge)

AZURE CONTEXT:
  Azure CDN: built on Akamai and Verizon/Edgio networks + Microsoft's own Azion
  Azure Front Door: CDN + load balancer + WAF at Microsoft's global edge
  ExpressRoute: dedicated fiber bypassing public internet (transit to Azure guaranteed)
```

---

## Physical Infrastructure

```
UNDERSEA CABLE GEOGRAPHY (key routes)

TRANSATLANTIC (North America ↔ Europe):
  25+ active cable systems
  Total capacity: 200+ Tbps
  Key: AEConnect-1, Dunant (Google), MAREA (Microsoft/FB), TAT-14

TRANSPACIFIC (North America ↔ Asia):
  20+ systems
  Key: FASTER (Google), New Cross Pacific, JUPITER (Facebook)

SOUTHEAST ASIA ↔ EUROPE:
  SEA-ME-WE (3,4,5,6): Marseille → Singapore → Perth/Hong Kong
  AAE-1: Asia-Africa-Europe-1

AFRICA:
  Submarine cables reaching African coasts mostly since 2009-2020
  SEACOM, EASSy, ACE, 2Africa (Meta, 45 Tbps, 2023)

CHOKEPOINTS:
  Suez Canal: cables pass through Red Sea, Egypt border
  Strait of Malacca: all Southeast Asian cables
  South China Sea: contested geopolitically
  British Indian Ocean Territory (BIOT/Diego Garcia): cable landing
  Multiple cables have been cut near chokepoints (Yemen conflict area)
```

---

## Decision Cheat Sheet

| Scenario | Network Engineering Response |
|----------|------------------------------|
| Minimize latency to customers globally | CDN + multiple PoPs + anycast |
| Reduce transit costs | Peer at IXPs, especially DE-CIX/AMS-IX |
| Route traffic via preferred path | BGP LOCAL-PREF policy manipulation |
| Prevent BGP route hijacking | RPKI/ROA validation + BGPSEC (where supported) |
| Bypass public internet for Azure | Azure ExpressRoute (dedicated fiber) |
| Resilient connectivity (no single PoP failure) | Multi-homed BGP with multiple upstreams |

---

## Common Confusion Points

**Tier 1 ISPs are not government entities**: They're private companies with massive fiber networks.
Their "Tier 1" status is an industry designation based on settlement-free peering. There's no official
classification; the list is fluid as networks grow and merge.

**BGP is not designed for security**: BGP operates on trust — it trusts what neighboring routers
announce. RPKI/ROA addresses route origin authentication but not path. Anyone who can peer with
another AS can (accidentally or maliciously) affect global routing. This is a long-known weakness.

**Peering vs transit doesn't affect end users visibly**: From a user perspective, packets arrive
the same way. The difference is economic and latency-based. Direct peering is usually lower latency
than transit because fewer hops, but the impact varies from <1 ms to ~50 ms depending on geography.

**CDN doesn't help with dynamic content**: CDN caches static content (images, JS, CSS, video segments).
API calls, real-time data, and personalized content must still come from origin servers. Modern
CDNs add "edge computing" (Lambda@Edge, Workers) to process dynamic requests at the edge.
