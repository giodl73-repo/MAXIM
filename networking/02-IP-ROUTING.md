---
maxim_schema: maxim.frontmatter.v1
id: maxim:networking:ip-routing
kind: guide
module: networking
section: networking
title: IP and Routing - IPv4/IPv6, CIDR, Routing Tables, BGP, OSPF
status: source-custody
source_custody: partial
current_path: networking/02-IP-ROUTING.md
canonical_path: networking/02-IP-ROUTING.md
backsource_ids: [proof-backfill:networking:02-ip-routing, git-history:networking:02-ip-routing]
concepts: [ipv4, ipv6, cidr, subnetting, routing table, bgp, ospf, longest prefix match]
root_concepts: [ip routing]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# IP and Routing — IPv4/IPv6, CIDR, Routing Tables, BGP, OSPF

## The Big Picture

The link layer (01) gets a frame across one segment. The network layer (L3)
solves the much harder problem: **deliver a packet across the whole Internet,
hop by hop, through networks owned by strangers.** It does this with two
ingredients — a **global, hierarchical address** (IP) and a **distributed
agreement on the path** (routing). The hierarchy is what makes it scale: instead
of knowing every host, a router knows *prefixes* and forwards toward the
best-matching one.

```
                        THE INTERNET = NETWORK OF NETWORKS
   +----------+        +----------+        +----------+        +----------+
   |   AS 1   |  BGP   |   AS 2   |  BGP   |   AS 3   |  BGP   |   AS 4   |
   | (Comcast)|<------>| (transit)|<------>|(Cloudflr)|<------>| (Azure)  |
   +----------+        +----------+        +----------+        +----------+
        | OSPF              | OSPF              | OSPF              | OSPF
        | (interior)        | (interior)        | (interior)        |
    +---+---+           +---+---+           +---+---+           +---+---+
    |routers|           |routers|           |routers|           |routers|
    +-------+           +-------+           +-------+           +-------+

   TWO ROUTING SCOPES:
     INTRA-AS  (inside one org)   -> IGP: OSPF / IS-IS    "find best path, I trust me"
     INTER-AS  (between orgs)     -> EGP: BGP             "find path, I trust no one"

   Each router does ONE primitive over and over:
     "Look up the dst IP, find the longest-matching prefix, forward to next hop."
```

There are two completely different routing worlds. **Inside** an organization
(an Autonomous System), you run an **IGP** like **OSPF** that optimizes for the
shortest path because you trust your own routers. **Between** organizations you
run **BGP**, which optimizes for *policy and economics* because you trust no one.
Keeping these two scopes separate is the key mental model of the entire layer.

> **Bridge — addressing as a hierarchical key space.** IP addressing is a
> hierarchical key space, exactly like a sharded keyspace or a DNS-style tree:
> the prefix is the shard, and "longest prefix match" is range routing to the
> most specific shard. You already understand consistent-hashing range ownership;
> IP routing is that, with the ranges (prefixes) advertised by a protocol.

---

## IPv4 Addressing

An **IPv4** address is **32 bits**, written as four dotted decimal octets:
`192.168.1.10`. That gives **~4.29 billion** (2^32) addresses — which the
Internet exhausted, driving NAT (07) and IPv6.

```
   32 bits = 4 octets
   192   .   168   .   1   .   10
   11000000.10101000.00000001.00001010
   \____________ network _______/\__host_/   <- the split is set by the MASK

   The split is NOT fixed. A "prefix length" / mask says where it falls:
     /24  = first 24 bits are network, last 8 are host  (256 addresses)
     /16  = first 16 bits network, last 16 host          (65,536 addresses)
```

### Private and Special Ranges (RFC 1918 + friends)

These you should know cold, because every NAT (07) and datacenter (09) uses them:

| Range | CIDR | Purpose | RFC |
|---|---|---|---|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | Private (large) | RFC 1918 |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | Private (medium) | RFC 1918 |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | Private (small/home) | RFC 1918 |
| 127.0.0.0/8 | loopback | localhost (127.0.0.1) | RFC 1122 |
| 169.254.0.0/16 | link-local | auto-config when DHCP fails (APIPA) | RFC 3927 |
| 100.64.0.0/10 | CGNAT shared | carrier-grade NAT (07) | RFC 6598 |

---

## CIDR and Subnetting

**CIDR (Classless Inter-Domain Routing, RFC 4632)** replaced the old rigid
Class A/B/C scheme. Instead of fixed network sizes, a prefix length `/n` lets the
network/host boundary fall *anywhere*. This is the single idea that lets routing
tables aggregate.

```
   PREFIX NOTATION:  192.168.1.0/24

   /24 means: first 24 bits are the network -> 8 host bits left.
              2^8 = 256 total addresses.
              Usable hosts = 256 - 2 = 254
              (one address is the NETWORK id, one is the BROADCAST)

   COMMON PREFIX SIZES:
   +------+------------------+-----------------+------------------+
   | CIDR | Mask             | Total addresses | Usable hosts     |
   +------+------------------+-----------------+------------------+
   | /8   | 255.0.0.0        | 16,777,216      | 16,777,214       |
   | /16  | 255.255.0.0      | 65,536          | 65,534           |
   | /24  | 255.255.255.0    | 256             | 254              |
   | /30  | 255.255.255.252  | 4               | 2 (point-to-pt)  |
   | /31  | 255.255.255.254  | 2               | 2 (RFC 3021 link)|
   | /32  | 255.255.255.255  | 1               | 1 (a single host)|
   +------+------------------+-----------------+------------------+
```

**Aggregation** is the payoff. If a provider owns `10.1.0.0/16`, it can advertise
*one* route covering 65,536 addresses instead of 256 separate `/24`s. The whole
Internet routing table stays manageable (a few hundred thousand to ~1M prefixes
globally) only because of this hierarchical summarization. Without CIDR, the
table would be billions of entries.

> **Bridge — prefix trees.** A routing table is a prefix trie keyed on IP bits.
> "Longest prefix match" is trie traversal returning the deepest matching node.
> If you've implemented a radix tree, you've implemented the data structure at the
> heart of every router's forwarding plane.

---

## The Routing Table and Longest Prefix Match

Every router (and every host) has a **routing table** (also called the FIB,
Forwarding Information Base, in hardware). Forwarding is one operation: find the
**most specific** prefix that contains the destination IP, and send the packet
to that entry's next hop.

```
   ROUTING TABLE (simplified):
   +--------------------+------------------+-----------+
   | Destination prefix | Next hop         | Interface |
   +--------------------+------------------+-----------+
   | 10.1.5.0/24        | 10.1.5.1 (direct)|   eth1    |
   | 10.1.0.0/16        | 10.0.0.1         |   eth0    |
   | 0.0.0.0/0          | 192.0.2.1 (gw)   |   eth0    |  <- default route
   +--------------------+------------------+-----------+

   Packet to 10.1.5.42:
     matches 10.1.5.0/24  (24 bits)  <-- WINS, most specific
     matches 10.1.0.0/16  (16 bits)
     matches 0.0.0.0/0    (0 bits, the catch-all default)

   LONGEST PREFIX MATCH: the entry with the most bits wins.
```

The `0.0.0.0/0` entry is the **default route** ("gateway of last resort") —
matches everything, lowest priority, used when nothing more specific applies. On
your laptop this points at your home router; that router's default points at the
ISP; and so on up to the Internet's core, which has a *full table* and no default.

---

## IGP vs. EGP: Two Routing Worlds

```
   +---------------------------------------------------------------+
   |                  ONE AUTONOMOUS SYSTEM (AS)                    |
   |   = one administrative domain, has a unique AS number (ASN)   |
   |                                                               |
   |     R1 ---- R2 ---- R3       run an IGP between themselves:   |
   |      \      |      /         OSPF or IS-IS                    |
   |       \     |     /          goal: SHORTEST PATH, full trust  |
   |        \    |    /                                            |
   |         +---R4---+----[ BGP speaker ]----> to OTHER ASes      |
   +---------------------------------------------------------------+
                                  |
                                  | BGP between ASes:
                                  | goal: POLICY + economics, ZERO trust
                                  v
   +---------------------------------------------------------------+
   |                  ANOTHER AS (different org)                   |
   +---------------------------------------------------------------+
```

| | IGP (interior) | EGP (exterior) |
|---|---|---|
| Examples | OSPF, IS-IS, (RIP, legacy) | BGP (BGP-4 only, today) |
| Scope | within one AS | between ASes |
| Optimizes for | shortest path (a metric) | **policy** + economics |
| Trust model | full (your own routers) | **none** (the open Internet) |
| Convergence | seconds | can be slow; designed for stability |
| Scale | thousands of routers | the whole Internet (~1M routes) |

---

## OSPF — The Interior Workhorse

**OSPF (Open Shortest Path First, current version OSPFv2 for IPv4 in RFC 2328;
OSPFv3 for IPv6)** is a **link-state** IGP. Every router floods a description of
its own links to all others; each then builds an identical map of the whole AS
and runs **Dijkstra's shortest-path algorithm** independently to compute its own
best routes.

```
   LINK-STATE IDEA:
   1) Each router discovers its neighbors and link costs.
   2) Each floods a Link-State Advertisement (LSA) to ALL routers.
   3) Every router now holds the SAME full topology (link-state database).
   4) Each runs Dijkstra over that graph from itself -> shortest paths.

         R1 --2-- R2
          |        |          Costs are link metrics (often inverse
          5        1          of bandwidth). Dijkstra picks lowest
          |        |          total cost end to end.
         R3 --3-- R4
```

OSPF scales via **areas** (a two-level hierarchy with a backbone Area 0) so the
flooding domain stays bounded in large networks. Contrast it with the older
**RIP** (distance-vector, hop-count metric, max 15 hops) — RIP is simple but
converges slowly and can't scale; link-state won for serious networks.

> **Bridge — you know this algorithm.** OSPF is literally distributed Dijkstra.
> The MIT TCS content is the hard part and you have it; OSPF is the engineering
> wrapper that gets every router to agree on the same graph (via reliable LSA
> flooding) before each runs the shortest-path computation locally.

---

## BGP — The Glue of the Internet

**BGP (Border Gateway Protocol, version BGP-4, RFC 4271)** is *the* inter-domain
routing protocol — there is effectively only one, and it holds the Internet
together. It is a **path-vector** protocol: routers advertise reachable prefixes
along with the **AS-PATH** (the list of ASes the route traverses), and selection
is driven by **policy**, not shortest path.

```
   AS 4 originates prefix 203.0.113.0/24 and advertises it outward.
   Each AS that propagates it PREPENDS its own ASN to the AS-PATH:

     received by AS3 as:  203.0.113.0/24  via AS-PATH [4]
     AS3 re-advertises:   203.0.113.0/24  via AS-PATH [3 4]
     AS2 re-advertises:   203.0.113.0/24  via AS-PATH [2 3 4]

   WHY AS-PATH MATTERS:
     - loop prevention: if a router sees its OWN ASN in the path, reject it.
     - policy: a shorter AS-PATH is *preferred*, but LOCAL POLICY wins first.

   BGP DECISION (simplified order): local pref > shortest AS-PATH > ... > MED
   Translation: "money and contracts decide before distance does."
```

The defining feature of BGP is that it routes on **business relationships**, not
geography or speed. An AS prefers routes through a *customer* (who pays it) over
a *peer* (free exchange) over a *transit provider* (whom it pays) — regardless of
which is physically shorter. This is why your packet sometimes takes a
geographically absurd path: the routing reflects contracts, not maps.

BGP's trust-no-one design is also its weakness: a misconfigured or malicious AS
can announce prefixes it doesn't own (a **route hijack**) or leak routes,
redirecting traffic globally. **RPKI (Resource Public Key Infrastructure, RFC
6480)** adds cryptographic origin validation to mitigate this — a direct link to
cryptography/.

---

## IPv6 — The Successor

**IPv6** is **128 bits** — 2^128 addresses, an effectively unlimited space that
ends address scarcity and (largely) the need for NAT. Written as eight
hex groups: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`, compressible with `::` for
runs of zeros (`2001:db8:85a3::8a2e:370:7334`).

```
   IPv4 (32 bit):  192.168.1.10
   IPv6 (128 bit): 2001:db8:85a3::8a2e:370:7334

   +----------------------+------------------+
   |  routing prefix (network) | interface ID |
   |       /64 typical         |   /64 host   |
   +----------------------+------------------+

   KEY DIFFERENCES vs IPv4:
   - 128-bit address  -> no scarcity, no NAT needed for addressing
   - NO header checksum -> faster forwarding (rely on L2 FCS + L4)
   - NO router fragmentation -> only the SOURCE fragments (uses Path MTU Discovery)
   - ARP replaced by NDP (Neighbor Discovery, ICMPv6, RFC 4861)
   - SLAAC: hosts can autoconfigure addresses without DHCP (RFC 4862)
   - Built-in support for IPsec (optional, not mandatory in practice)
```

| Feature | IPv4 | IPv6 |
|---|---|---|
| Address size | 32 bits | 128 bits |
| Header | variable, has checksum | fixed 40-byte base, no checksum |
| Fragmentation | routers + source | **source only** (PMTUD) |
| Address resolution | ARP (broadcast) | NDP (multicast) |
| Autoconfig | DHCP | SLAAC or DHCPv6 |
| NAT | ubiquitous (07) | designed to be unnecessary |

Adoption is partial and uneven; the Internet runs **dual-stack** (both protocols
side by side) and will for the foreseeable future. The transition is a coexistence
story, not a flag day.

---

## Decision Cheat Sheet

| Question | Answer / Tool |
|---|---|
| Routing inside my own network/org | OSPF (or IS-IS); link-state, shortest path |
| Routing between organizations / on the Internet | BGP-4, policy-driven |
| How big is a /24? | 256 addresses, 254 usable hosts |
| How to shrink the routing table | CIDR aggregation (advertise a supernet) |
| Private addresses for internal use | 10/8, 172.16/12, 192.168/16 (RFC 1918) |
| Which route wins when several match | longest prefix match (most specific) |
| Out of IPv4 addresses | NAT (07) short-term, IPv6 long-term |
| Why traffic takes a weird path | BGP policy/economics, not geography |
| Protect against route hijacks | RPKI origin validation (crypto) |
| Catch-all "send everything else here" | default route 0.0.0.0/0 |

---

## Common Confusion Points

### "Is routing the same as switching?"

No. Switching (01) is L2, intra-LAN, by MAC, no TTL decrement. Routing is L3,
inter-network, by IP prefix, decrements TTL every hop (which is what prevents L3
loops and what `traceroute` exploits). A packet is *switched* within each LAN and
*routed* between them.

### "Why does BGP sometimes pick a longer path?"

Because BGP optimizes **policy and economics**, not distance or speed. Its
selection prefers local-preference (business relationship) before AS-PATH length.
A route through a customer who pays you beats a shorter route through a provider
you pay. The Internet's paths reflect contracts.

### "If IPv6 has unlimited addresses, why still use NAT?"

For *addressing*, IPv6 removes the need for NAT. But NAT also gets used for
perceived security/boundary reasons, and the world is dual-stack for the long
haul, so NAT (07) remains everywhere on IPv4. The address-scarcity *reason* for
NAT goes away with IPv6; the habit and the firewall side-effect linger.

### "Does the source IP change as a packet crosses routers?"

No (except at a NAT, 07). L3 source/destination IPs are end-to-end. What changes
every hop is the **TTL** (decremented; packet dies at 0) and the L2 MAC framing
(01). Constant IP, decrementing TTL, fresh MAC each hop — that triple is the
signature of L3 forwarding.

### "What's an Autonomous System, concretely?"

An AS is one administrative routing domain — an ISP, a cloud provider, a big
enterprise — identified by a globally unique **ASN**. BGP routes *between* ASes;
an IGP (OSPF) routes *within* one. "AS" is the unit of trust and policy on the
Internet, the same way a tenant or account is the unit of isolation in cloud.
