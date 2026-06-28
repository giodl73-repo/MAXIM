---
maxim_schema: maxim.frontmatter.v1
id: maxim:networking:link-layer
kind: guide
module: networking
section: networking
title: The Link Layer - Ethernet, MAC, Framing, Switching, VLANs, ARP
status: source-custody
source_custody: partial
current_path: networking/01-LINK-LAYER.md
canonical_path: networking/01-LINK-LAYER.md
backsource_ids: [proof-backfill:networking:01-link-layer, git-history:networking:01-link-layer]
concepts: [ethernet, mac address, framing, switching, vlan, arp, spanning tree]
root_concepts: [link layer]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# The Link Layer — Ethernet, MAC, Framing, Switching, VLANs, ARP

## The Big Picture

The link layer (L2) has exactly one job: **move a frame across one physical
segment, from one network interface to the next, on a single local network.** It
knows nothing about the Internet, nothing about routing, nothing about your
application. Its entire universe is "this LAN." Everything bigger than the local
segment is L3's problem (02). What L2 gives you is the foundational primitive:
*addressable delivery between NICs that share a wire (or a switch).*

```
                        ONE BROADCAST DOMAIN (one LAN / one VLAN)
   +-------------------------------------------------------------------+
   |                                                                   |
   |   HOST A          HOST B          HOST C          ROUTER          |
   |  +------+        +------+        +------+        +--------+        |
   |  | NIC  |        | NIC  |        | NIC  |        | NIC    |        |
   |  | MAC  |        | MAC  |        | MAC  |        | (gw)   |        |
   |  | ..a1 |        | ..b2 |        | ..c3 |        | ..ff   |        |
   |  +--+---+        +--+---+        +--+---+        +---+----+        |
   |     |               |               |               |            |
   |     +-------+-------+-------+-------+-------+-------+              |
   |             |       |       |       |       |                     |
   |          +--+-------+-------+-------+-------+--+                   |
   |          |          ETHERNET SWITCH         |                    |
   |          |  (forwards frames by MAC table)  |                    |
   |          +----------------------------------+                    |
   |                                                                   |
   +-------------------------------------------------------------------+
       Frames carry MAC src/dst. The switch reads dst MAC, looks it up,
       and sends the frame out exactly the right port. The ROUTER is the
       only way OUT of this broadcast domain (to other LANs / the Internet).
```

The two characters in this story are the **MAC address** (who) and the **frame**
(the envelope), and the two devices are the **switch** (smart, per-port) and the
older **hub** (dumb, everyone hears everything). Add **VLANs** to slice one
physical switch into many logical LANs, and **ARP** to bridge L3 addresses down
to L2, and you have the whole layer.

> **Bridge — the local bus.** Think of one LAN as a shared bus on a
> motherboard, and the MAC address as a device's hardwired ID on that bus. A
> switch is a crossbar that gives every device a private lane instead of a shared
> medium. The router is the bridge controller to *other* buses. The mental model
> is identical to interconnect fabric; only the scale differs.

---

## The MAC Address

A **MAC address** (Media Access Control address, also called a hardware or
physical address) is a **48-bit** identifier burned into (or assigned to) a
network interface. It is written as six hex octets: `00:1B:44:11:3A:B7`.

```
   48 bits = 6 octets
   +--------+--------+--------+--------+--------+--------+
   |   00   |   1B   |   44   |   11   |   3A   |   B7   |
   +--------+--------+--------+--------+--------+--------+
   \________ OUI ________/ \______ device-specific ______/
    (vendor, assigned       (vendor picks, must be
     by IEEE: 24 bits)       unique within their OUI)

   Special bits in the first octet:
     - bit 0 (I/G): 0 = unicast, 1 = multicast/broadcast
     - bit 1 (U/L): 0 = globally unique (OUI), 1 = locally administered

   BROADCAST MAC: FF:FF:FF:FF:FF:FF  (every NIC on the segment accepts it)
```

The top 24 bits are the **OUI** (Organizationally Unique Identifier), which IEEE
assigns to a vendor; the bottom 24 the vendor assigns per device. Together they
are intended to be globally unique, though virtualization and "locally
administered" addresses mean you can't fully rely on that.

| Property | MAC (L2) | IP (L3) |
|---|---|---|
| Size | 48 bits | 32 (v4) / 128 (v6) bits |
| Scope | one link only | global, end-to-end |
| Assigned by | NIC vendor / OS | network operator / DHCP |
| Changes per hop? | **yes**, rewritten every hop | no (modulo NAT) |
| Hierarchical? | no (flat) | yes (prefix-based) |
| Analogy | name written on your hand | postal address |

The flat, non-hierarchical nature of MAC is *why* L2 can't scale to the Internet:
there is no way to aggregate routes. A switch must, in the limit, know every MAC
in its domain. IP's hierarchy (02) is the fix.

---

## The Ethernet Frame

Ethernet (IEEE 802.3) is the dominant L2 framing on wired LANs. A frame wraps the
L3 packet with a header and trailer. The classic Ethernet II frame:

```
 +----------+----------+----------+----------+------------------+---------+
 | Preamble | Dst MAC  | Src MAC  | EtherType|     Payload      |   FCS   |
 |  + SFD   |          |          |          |  (L3 packet)     |  (CRC)  |
 +----------+----------+----------+----------+------------------+---------+
   7+1 bytes   6 bytes   6 bytes    2 bytes    46-1500 bytes     4 bytes
   (sync)                                      (the MTU range)

   EtherType values you will actually see:
     0x0800 = IPv4
     0x0806 = ARP
     0x86DD = IPv6
     0x8100 = 802.1Q VLAN tag (see VLANs below)
```

Key constants worth committing to memory because the rest of networking leans on
them:

- **MTU (Maximum Transmission Unit) = 1500 bytes** of payload for standard
  Ethernet. This is the single most consequential number in networking — it caps
  how much L3 can put in one frame, which cascades into IP fragmentation (02) and
  TCP's MSS (03).
- **Jumbo frames** raise the payload to ~9000 bytes; common inside datacenters
  (09) where every device is under one administrator's control.
- **FCS (Frame Check Sequence)** is a 32-bit CRC trailer. It *detects* corruption
  and the frame is silently dropped if it fails — Ethernet does **not** retransmit.
  Reliability is L4's job (03), not L2's.
- The **preamble + SFD** (8 bytes) is a clock-sync pattern for the physical layer
  and is not part of the addressable frame.

> **Bridge — the MTU as a packet-size budget.** MTU is the L2 equivalent of a
> fixed-size buffer/page. Everything above has to live within it or pay a
> fragmentation cost. When you later see "MSS = MTU − IP header − TCP header" in
> 03, this is the budget it is subtracting from.

---

## Switching: How a Frame Finds Its Port

A **switch** is a multi-port L2 device that learns which MAC lives behind which
port and forwards frames intelligently. It builds a **MAC address table** (also
called a CAM table) by watching source addresses.

```
   LEARNING (populate the table from SOURCE MACs as frames arrive):

     Frame arrives on port 3, src=AA:..:a1
        -> switch records:  AA:..:a1  is reachable via PORT 3

   FORWARDING (use the table on DESTINATION MAC):

     +-------------------+----------+
     | MAC               | Port     |
     +-------------------+----------+
     | AA:..:a1          |    3     |
     | BB:..:b2          |    7     |
     | CC:..:c3          |    1     |
     +-------------------+----------+

     dst known   -> forward out that ONE port        (unicast)
     dst unknown -> flood out ALL ports but ingress   (learn from the reply)
     dst = FF:FF.. -> flood (broadcast, by definition)
```

Three behaviors, total: **forward** (dst known), **flood** (dst unknown or
broadcast), **filter** (dst is on the same port it came in — drop it). Entries
age out after a timeout (often ~300 s) so the table tracks moves.

### Hub vs. Switch vs. Router

```
   HUB (L1, obsolete)        SWITCH (L2)            ROUTER (L3)
   ================          ===========           ============
   repeats bits out          forwards frames        forwards packets
   ALL ports.                to the RIGHT port       BETWEEN networks
   One collision domain.     by MAC table.           by IP prefix.
   Everyone shares           Each port = its own     Stops broadcasts;
   bandwidth + collisions.   collision domain.       separates LANs.
   "dumb amplifier"          "MAC-aware crossbar"    "the way out"
```

A critical structural fact: **a switch does not stop a broadcast.** Every device
reachable through switches forms **one broadcast domain**. The only device that
*terminates* a broadcast domain — that you must cross to reach another LAN or the
Internet — is a **router**. This is the L2/L3 boundary, and it is the single most
important architectural line in this whole directory.

---

## Loops and Spanning Tree

Switches flood unknown/broadcast frames. If you wire a physical loop between
switches, a broadcast frame circles forever, multiplying — a **broadcast storm**
that melts the LAN in seconds. L2 has no TTL to save you (that's an L3 feature).

The fix is **STP (Spanning Tree Protocol)**, originally IEEE 802.1D, which
detects loops and logically *blocks* redundant links to leave a loop-free tree —
while keeping them ready as hot standby.

```
   PHYSICAL (has a loop):          LOGICAL after STP (loop broken):

     S1 ---- S2                      S1 ---- S2
      |  \   /  |                     |       |
      |   \ /   |        ===>         |       |  (one link
      |    X    |                     |       |   set to
      |   / \   |                     |       |   BLOCKING)
     S3 ---- S4                      S3       S4
                                        (tree, no cycle)
```

Modern networks use **RSTP** (Rapid Spanning Tree, IEEE 802.1w) for faster
convergence, and datacenters increasingly abandon STP entirely in favor of
L3-routed fabrics or overlays (09) precisely to *use* all those redundant links
instead of blocking them.

> **Bridge — cycle detection.** STP is literally a distributed minimum spanning
> tree computation (the algorithm Radia Perlman designed) running continuously on
> the switch graph. You already know the graph theory; STP is that theory shipped
> as firmware, electing a root bridge and pruning back-edges.

---

## VLANs: One Switch, Many LANs

A **VLAN (Virtual LAN, IEEE 802.1Q)** partitions one physical switch into
multiple isolated broadcast domains. Two ports in different VLANs cannot reach
each other at L2 even though they share the same hardware — they are as separate
as if they were on different switches. Crossing between VLANs requires a router
(or an L3 switch doing routing).

```
   ONE PHYSICAL SWITCH                Logical result:
   +-------------------------+
   | p1 p2  | p3 p4  | p5 p6 |        VLAN 10 ==  isolated LAN
   |  VLAN  |  VLAN  | TRUNK |        VLAN 20 ==  isolated LAN
   |   10   |   20   |       |        (cannot talk without
   +---||---+---||---+---||--+         going through a router)
       eng       fin     to other switch

   802.1Q TAG inserted into the frame (after Src MAC, EtherType 0x8100):
   +--------+--------+----+-------+----------+
   |Dst MAC |Src MAC |TPID| VID.. | EtherType|  ...payload...
   +--------+--------+----+-------+----------+
                      0x8100  12-bit VLAN ID (1..4094)
```

- **Access port**: belongs to one VLAN; frames are untagged on the wire (the
  host is unaware of VLANs).
- **Trunk port**: carries *many* VLANs between switches; frames are **tagged**
  with a 12-bit VLAN ID so the far switch knows which VLAN each frame belongs to.
- The 12-bit VID field allows up to **4094 usable VLANs** (0 and 4095 reserved).
  This ceiling is exactly why datacenter overlays moved to VXLAN's 24-bit segment
  ID (~16 million) — covered in 09.

> **Bridge — tenancy isolation.** A VLAN is L2 multi-tenancy: the same physical
> resource, partitioned into isolated logical segments by a tag. It is the direct
> ancestor of VPC/network-segment isolation in cloud (cloud-architecture/), and
> VXLAN (09) is what you reach for when 4094 segments isn't enough.

---

## ARP: Bridging L3 Down to L2

Here is the layer-crossing glue. Your host wants to send an IP packet (L3) to
`192.168.1.10`, but to actually put it on the wire it needs the *destination
MAC* (L2). **ARP (Address Resolution Protocol, RFC 826)** answers "what MAC owns
this IPv4 address on my local link?"

```
   HOST A wants to send to 192.168.1.10 but doesn't know its MAC.

   1) ARP REQUEST  (broadcast to FF:FF:FF:FF:FF:FF)
      "Who has 192.168.1.10? Tell 192.168.1.5"
              |
              v   every host on the LAN hears it
   2) ARP REPLY  (unicast back to A)
      "192.168.1.10 is at BB:..:b2"
              |
              v
   3) A caches the mapping in its ARP TABLE and sends the frame.

      192.168.1.10  ->  BB:..:b2   (cached, ages out after minutes)
```

Critical scoping rule: **ARP only resolves addresses on the local link.** If the
destination IP is on a *different* network, the host does not ARP for the remote
host at all — it ARPs for its **default gateway** (the router) and hands the
packet there. The router then repeats the process on the next link. This is the
mechanism behind "the MAC changes every hop but the IP doesn't" from 00.

- **IPv6 doesn't use ARP.** It uses **NDP (Neighbor Discovery Protocol, RFC
  4861)** with ICMPv6 Neighbor Solicitation / Advertisement messages over
  multicast — same idea, cleaner design, no broadcast.
- **ARP spoofing** is a classic L2 attack: a malicious host replies "that IP is
  *me*," poisoning ARP caches to intercept traffic (a local man-in-the-middle).
  This is why L2 trust is weak and why we layer TLS (06) on top — never trust the
  link.

---

## Decision Cheat Sheet

| Situation | What's happening at L2 | Reach for |
|---|---|---|
| Add a device to a LAN | switch learns its MAC on first frame | nothing — automatic |
| Two hosts on same subnet can't talk | ARP failing, or different VLAN | check VLAN membership / ARP cache |
| LAN suddenly saturated / frozen | broadcast storm from a loop | STP / RSTP must be enabled |
| Need to isolate departments on one switch | logical segmentation | 802.1Q VLANs |
| Need >4094 isolated segments | VLAN ID space exhausted | VXLAN overlay (see 09) |
| Want all redundant links active | STP blocks them | L3 fabric / overlay (09) |
| Inside a datacenter, want bigger frames | reduce per-byte overhead | jumbo frames (~9000 MTU) |
| Reaching anything off the local subnet | host ARPs the gateway, not the dest | a router (L3, see 02) |

---

## Common Confusion Points

### "Does a switch separate broadcast domains?"

No. A switch separates **collision** domains (one per port) but **all** switched
ports form a single **broadcast** domain. Only a **router** (or a VLAN boundary,
which a router must cross) separates broadcast domains. This is the cleanest test
of whether you understand the L2/L3 line.

### "Why does ARP broadcast but the reply is unicast?"

The request must reach an unknown party, so it floods the whole segment
(broadcast). But the requester's MAC *is* in the request, so the responder can
answer it directly (unicast). It's the standard "broadcast to discover, unicast
to converse" pattern you'll also see in DHCP.

### "If MAC addresses are globally unique, why not just route on them?"

Because MAC is **flat** — there is no hierarchy to aggregate. Routing the whole
Internet on MAC would require every router to hold a table entry for every NIC on
Earth. IP's hierarchical prefixes (02) let one routing entry cover millions of
hosts. Flat addressing works on a LAN; hierarchy is mandatory at Internet scale.

### "MTU is 1500 — is that the frame size or the payload size?"

MTU (1500) is the **payload** — the L3 packet that fits inside the frame. The
frame on the wire is larger: add 14 bytes of Ethernet header + 4 bytes FCS (+ 4
more if VLAN-tagged), plus the preamble the PHY uses. When you compute TCP's MSS
in 03, you subtract from the 1500 payload, not from the wire size.

### "Is a VLAN a security boundary?"

It's a *segmentation* boundary, not a strong security boundary on its own.
VLAN-hopping attacks exist, and an L3 switch can route between VLANs trivially.
Treat VLANs as isolation-by-default that a firewall (07) enforces, not as a
cryptographic guarantee — that's what TLS/mTLS (06) provides end-to-end.
