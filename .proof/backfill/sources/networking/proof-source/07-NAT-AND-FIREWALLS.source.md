---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "07-NAT-AND-FIREWALLS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:networking:nat-and-firewalls
kind: guide
module: networking
section: networking
title: NAT and Firewalls - NAT Types, Stateful Firewalls, CGNAT, Port Forwarding
status: source-custody
source_custody: partial
current_path: networking/07-NAT-AND-FIREWALLS.md
canonical_path: networking/07-NAT-AND-FIREWALLS.md
backsource_ids: [proof-backfill:networking:07-nat-and-firewalls, git-history:networking:07-nat-and-firewalls]
concepts: [nat, pat, stateful firewall, cgnat, port forwarding, nat traversal, stun]
root_concepts: [nat and firewalls]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# NAT and Firewalls — NAT Types, Stateful Firewalls, CGNAT, Port Forwarding

## The Big Picture

NAT and firewalls are the **middleboxes** — devices that sit in the path and
rewrite or filter traffic, breaking the original Internet ideal that any host can
directly address any other. NAT exists because IPv4 ran out of addresses (02): it
lets many private hosts share one public IP by rewriting addresses and ports on
the fly. Firewalls exist for security: they decide which connections are allowed.
Both are **stateful** — they remember connections — and that shared mechanism
(a connection-tracking table) is the key to understanding them together.

```
              THE MIDDLEBOX: where private meets public
   PRIVATE SIDE (RFC 1918)                            PUBLIC INTERNET
   +---------------------+                            +----------------+
   | 192.168.1.10  ------|----+                       |                |
   | 192.168.1.11  ------|--+ |                       |                |
   | 192.168.1.12  ------|+ | |    +-------------+    |  server        |
   +---------------------+| | |    |  NAT +      |    |  203.0.113.5   |
                          | | +--->|  FIREWALL   |--->|  :443          |
                          | +----->|             |    |                |
                          +------->| (one public |    |                |
                                   |  IP, a state|    |                |
                                   |  table)     |    |                |
                                   +-------------+    +----------------+
                                    public IP: 198.51.100.7

   NAT:      rewrite (private IP:port) <-> (public IP:port), remember it
   FIREWALL: allow/deny based on rules + connection STATE
   BOTH:     keep a per-connection table; the table is the whole trick.
```

The central consequence: behind NAT, hosts have **no inbound reachability** by
default. A private host can *initiate* outbound connections (creating a table
entry that lets the reply back in), but nobody on the Internet can start a
connection *to* it — there's no public address for it and no table entry to match.
This asymmetry is the source of nearly every NAT headache and the whole field of
NAT traversal.

> **Bridge — a stateful proxy / connection table.** NAT and a stateful firewall
> are exactly a connection-tracking proxy: an outbound request opens a flow entry
> that authorizes the matching return traffic; everything unsolicited is dropped.
> It's the same model as a reverse proxy's connection table or a security group —
> default-deny inbound, allow established-and-related.

---

## Why NAT Exists

```
   IPv4 = 32 bits = ~4.29 billion addresses. The Internet has FAR more
   devices than that. The stopgap (since the mid-1990s):

     MANY private hosts  --share-->  ONE public IPv4 address

   Private ranges (RFC 1918, from 02) never appear on the public Internet:
     10.0.0.0/8      172.16.0.0/12     192.168.0.0/16

   NAT translates between the private world and the one public IP, so a whole
   home/office/carrier looks like a single (or few) public address(es).
```

IPv6 (02), with its effectively unlimited address space, removes the *addressing*
reason for NAT — every device can have a globally unique address. But the
*firewall side effect* of NAT (no unsolicited inbound) is something operators
still want, so IPv6 networks typically achieve it with a stateful firewall
instead of address translation.

---

## How NAT Actually Works (PAT)

The form of NAT everyone actually uses is **PAT (Port Address Translation)**,
also called **NAPT** or "NAT overload" — it multiplexes many internal hosts onto
one public IP by also rewriting the **port** and tracking the mapping.

```
   OUTBOUND: host 192.168.1.10:51000 -> server 203.0.113.5:443

   NAT rewrites the SOURCE and records the mapping in its table:

   +------------------------+------------------------+
   | INSIDE (private)       | OUTSIDE (public)       |
   +------------------------+------------------------+
   | 192.168.1.10 : 51000   | 198.51.100.7 : 62000   |
   | 192.168.1.11 : 51000   | 198.51.100.7 : 62001   |  <- same inside port,
   +------------------------+------------------------+     different public port

   ON THE WIRE the server sees: src 198.51.100.7:62000 -> 203.0.113.5:443

   INBOUND REPLY: server -> 198.51.100.7:62000
     NAT looks up 62000 in the table -> rewrites dst back to 192.168.1.10:51000
     -> delivers to the right private host.

   The PORT is what disambiguates which internal host a reply belongs to.
```

This is why NAT must be **stateful**: the table mapping public-port → private-host
is the only way a return packet finds its way home. The entry is created on the
first outbound packet and expires after an idle timeout. If the entry is gone, the
reply has nowhere to go — which is why long-idle connections silently die behind
NAT and why protocols send keepalives.

---

## NAT and the End-to-End Principle

NAT *breaks* a foundational assumption of the Internet — that any host can
address any other directly. The damage is real and worth naming:

```
   WHAT NAT BREAKS:
   - inbound reachability: no public address -> servers behind NAT are
     unreachable from outside without explicit port forwarding.
   - peer-to-peer: two hosts BOTH behind NAT can't directly connect
     (neither can initiate inbound to the other).
   - protocols that embed IPs in their payload (old FTP, SIP) break unless
     the NAT has an "ALG" that rewrites the embedded address too.
   - end-to-end integrity: the L4 checksum must be recomputed; IPsec AH
     (which signs the IP header) is incompatible with NAT.
```

NAT is, in effect, a layering violation: an L3 device reaching up to rewrite L4
ports (and sometimes L7 payloads). It worked spectacularly as a stopgap for
address exhaustion, but every "why can't these two peers connect" problem in
modern networking traces back to it.

---

## NAT Types and Traversal

Because two NATed peers can't connect directly, real-time apps (VoIP, video,
games, WebRTC) need **NAT traversal**. How hard it is depends on the NAT's
**mapping behavior** — a classic taxonomy:

```
   NAT MAPPING BEHAVIORS (roughly, easiest -> hardest to traverse):

   FULL CONE          once 192.168.1.10:51000 -> 62000 is mapped, ANY
                      external host can send to 62000 and reach the host.
                      (most permissive)

   RESTRICTED CONE    only external hosts the inside host has ALREADY
                      contacted may send back (filtered by their IP).

   PORT-RESTRICTED    same, but filtered by IP AND port.

   SYMMETRIC          a DIFFERENT public port per destination. The mapping
                      depends on where you're going -> hardest to predict,
                      hardest to traverse. (most restrictive)
```

The traversal toolkit (the **ICE** framework, used by WebRTC):

```
   STUN (RFC 8489): "what's my public IP:port?" A host asks a STUN server,
        which reflects back the address NAT assigned -> the host learns its
        own external mapping so it can share it with a peer (hole punching).

   TURN (RFC 8656): when traversal FAILS (e.g. symmetric NAT on both ends),
        relay ALL traffic through a public TURN server. Always works, but
        adds a hop and cost -> the fallback of last resort.

   ICE  (RFC 8445): the framework that gathers candidate addresses (local,
        STUN-reflexive, TURN-relayed) and tries them in order to find a
        working path between two peers. The orchestration over STUN+TURN.

   HOLE PUNCHING: both peers send outbound simultaneously, each creating a
        NAT mapping that lets the other's packets in. Works for cone NATs;
        fails for symmetric (unpredictable ports) -> fall back to TURN.
```

> **Bridge — rendezvous through a coordinator.** NAT traversal is a rendezvous
> problem: two nodes that can't be addressed directly use a mutually reachable
> coordinator (STUN/TURN) to discover each other and punch a path — the same
> shape as nodes behind firewalls connecting through a relay/broker in a
> distributed system. The coordinator bootstraps a direct path where possible,
> relays where not.

---

## CGNAT — Carrier-Grade NAT

When ISPs ran out of public IPv4 even for their *own* customers, they added a
*second* NAT layer at the carrier: **CGNAT (Carrier-Grade NAT, RFC 6888)**, also
called LSN. Now your traffic is translated twice — once at your home router, once
at the carrier.

```
   DOUBLE NAT under CGNAT:

   home host        home router         CARRIER (CGNAT)        Internet
   192.168.1.10 --> 100.64.x.x      --> a SHARED public IP  --> server
   (RFC 1918)       (RFC 6598            (one IP shared by
                     shared range)        MANY subscribers)

   The 100.64.0.0/10 range (RFC 6598) is reserved precisely for the space
   BETWEEN the customer NAT and the carrier NAT.
```

CGNAT makes things worse for the user: you no longer have *any* public IP, so port
forwarding is impossible, inbound services can't be hosted, and peer-to-peer
traversal often needs TURN relays. It's purely a consequence of IPv4 scarcity —
and the strongest practical argument for IPv6 deployment, which eliminates the
need for it entirely.

---

## Port Forwarding and Stateful Firewalls

To deliberately allow *inbound* to a host behind NAT, you configure **port
forwarding** (a static, manual NAT table entry):

```
   STATIC RULE on the NAT/router:
     public 198.51.100.7 : 8080  ---ALWAYS-FORWARD-TO--->  192.168.1.50 : 80

   Now external clients hitting :8080 reach your internal web server. This
   is the manual override for NAT's default "no inbound" -> how you self-host.
   (UPnP / NAT-PMP let trusted apps create these mappings automatically.)
```

The **firewall** half is about *policy*, and the modern firewall is **stateful**:
it tracks each connection's state (NEW, ESTABLISHED, RELATED) and decides based on
the flow, not just individual packets.

```
   STATELESS (old, packet-by-packet):
     each packet judged alone against rules. To allow replies you must
     explicitly open the high ports -> coarse, leaky.

   STATEFUL (modern):
     +-------------------------------------------------------------+
     | CONNECTION TRACKING TABLE                                   |
     | flow (5-tuple) | state                                     |
     | A:51000->B:443 | ESTABLISHED   <- outbound created it       |
     +-------------------------------------------------------------+
     RULE: "allow ESTABLISHED + RELATED; default-deny everything else."
     -> outbound connection auto-authorizes its OWN return traffic.
     -> nothing unsolicited gets in. The table IS the security.
```

Stateful tracking is *the same table mechanism* as NAT — which is why a single
home router does both at once. The firewall asks "is this packet part of a flow we
already allowed?"; NAT asks "which inside host does this flow's reply belong to?"
Same table, two questions.

```
   FIREWALL LAYERS (where filtering happens):
     L3/L4 packet filter   -> by IP, port, protocol, flow state (fast, classic)
     L7 / application       -> inspects HTTP, blocks by URL/content (WAF, deep)
     stateful inspection    -> the connection-tracking middle ground (standard)
```

> **Bridge — default-deny + allow established.** A stateful firewall rule set is
> a security group / NSG: default-deny inbound, allow outbound, and the
> connection tracker auto-permits return traffic for flows you initiated. If
> you've written cloud security-group rules, you've written exactly this policy —
> the cloud just hides the conntrack table behind a managed control plane.

---

## Decision Cheat Sheet

| Situation | Mechanism |
|---|---|
| Many private hosts, one public IPv4 | PAT (NAT overload) |
| Host a server behind NAT | port forwarding (static NAT entry) |
| App auto-opens a port on the router | UPnP / NAT-PMP |
| Two peers both behind NAT need to connect | STUN + hole punching (ICE) |
| Traversal fails (symmetric NAT both ends) | TURN relay (fallback) |
| ISP gives you no public IP at all | you're behind CGNAT (100.64/10) |
| Why an idle connection drops behind NAT | mapping timed out → send keepalives |
| Allow return traffic without opening ports | stateful firewall (ESTABLISHED/RELATED) |
| Block by URL/content, not just port | L7 firewall / WAF |
| End the need for NAT entirely | IPv6 + stateful firewall (02) |

---

## Common Confusion Points

### "Is NAT a firewall?"

NAT *behaves* like a one-way firewall as a side effect: with no inbound mapping,
unsolicited traffic has nowhere to go, so it's dropped. But that's incidental, not
a security policy. A real firewall makes explicit allow/deny decisions and tracks
state intentionally. They share the connection-tracking table, which is why one
box does both — but NAT's "protection" is a byproduct of address translation, not
a designed control.

### "If IPv6 has enough addresses, is NAT gone?"

The *address-exhaustion* reason for NAT is gone — every IPv6 host can be globally
addressable. But operators still want "no unsolicited inbound," so IPv6 networks
use a **stateful firewall** to get that property without translating addresses.
NAT as address-sharing dies; the default-deny-inbound posture lives on as an
explicit firewall rule.

### "Why can't my two devices behind NAT just connect directly?"

Because neither has a public address and neither can initiate *inbound* to the
other — NAT only lets replies to *outbound* flows back in. They need a mutually
reachable coordinator (STUN) to learn their public mappings and punch holes
simultaneously, or a relay (TURN) when the NATs are too restrictive (symmetric).
This is the entire reason WebRTC ships ICE.

### "What's CGNAT and why does it make things worse?"

Carrier-Grade NAT is a *second* NAT layer your ISP runs because it ran out of
public IPv4 even for its customers. You get translated twice and have no public IP
of your own — so port forwarding and self-hosting become impossible and P2P often
needs TURN. It's pure IPv4-scarcity collateral damage, and the cleanest argument
for IPv6.

### "Stateful vs. stateless firewall — does it matter?"

A lot. A stateless filter judges each packet alone, so to permit replies you must
open wide port ranges — coarse and leaky. A stateful firewall tracks each flow and
auto-permits the return traffic for connections you initiated (ESTABLISHED/
RELATED), so it can default-deny everything else. Stateful inspection is the
modern standard and the model every cloud security group implements.
