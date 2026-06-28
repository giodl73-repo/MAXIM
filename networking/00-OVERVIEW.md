---
maxim_schema: maxim.frontmatter.v1
id: maxim:networking:overview
kind: guide
module: networking
section: networking
title: Networking - The Layered Model End-to-End
status: source-custody
source_custody: partial
current_path: networking/00-OVERVIEW.md
canonical_path: networking/00-OVERVIEW.md
backsource_ids: [proof-backfill:networking:00-overview, git-history:networking:00-overview]
concepts: [networking, osi model, tcp/ip, encapsulation, layering]
root_concepts: [networking]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---

# Networking — The Layered Model End-to-End

## The Big Picture

A network exists to move a chunk of application data from one process on one
machine to another process on a different machine, possibly on the other side of
the planet, across equipment owned by dozens of organizations that have never
met. The only way humans have ever made that tractable is **layering**: each
layer solves exactly one problem and hands a clean abstraction to the layer
above. The genius of the design is that each layer talks *logically* to its peer
on the far machine, while *physically* the data travels straight down the stack,
across the wire, and back up.

```
   HOST A                          THE PATH                       HOST B
+-----------+                                                  +-----------+
| APP DATA  |  <===== logical peer conversation (HTTP) =====>  | APP DATA  |  L7  Application
+-----------+                                                  +-----------+
| TLS/QUIC  |  <===== logical peer (encryption/session) ====>  | TLS/QUIC  |  L5-6 Session/Presentation
+-----------+                                                  +-----------+
| TCP / UDP |  <===== logical peer (ports, reliability) ====>  | TCP / UDP |  L4  Transport
+-----------+                                                  +-----------+
|    IP     |  <===== logical peer (global addressing) =====>  |    IP     |  L3  Network
+-----------+        |              |              |           +-----------+
| ETHERNET  |        |              |              |           | ETHERNET  |  L2  Link
+-----------+        v              v              v           +-----------+
|   PHY     |   +--------+     +--------+     +--------+        |   PHY     |  L1  Physical
+-----+-----+   | SWITCH |     | ROUTER |     | ROUTER |        +-----+-----+
      |         | (L2)   |     | (L3)   |     | (L3)   |              |
      +========>+========+====>+========+====>+========+=============>+
       copper/    forwards      forwards by    forwards by     fiber/
       fiber      by MAC        IP prefix      IP prefix       copper

   DATA GOES DOWN A's STACK -> ACROSS DEVICES -> UP B's STACK
   Each box on the path only reads UP TO the layer it operates on.
```

**Read this top-down for intent, bottom-up for mechanism.** The application
*thinks* it is talking HTTP directly to the peer. In reality every layer wraps
the data from above in its own header, ships the bytes down, and the layer pops
its header off on the way up. A switch only looks at L2. A router only looks at
L3. Neither understands your TLS session — and that separation is the whole
point.

---

## Two Models: OSI vs. TCP/IP

Theory uses the 7-layer **OSI model** (ISO/IEC 7498-1). Practice uses the
4-layer **TCP/IP model** (the Internet architecture, described in RFC 1122).
They map onto each other loosely; nobody implements OSI literally, but its
vocabulary ("a layer-3 device", "an L7 load balancer") is universal.

```
   OSI (7 layers)              TCP/IP (4 layers)        Example
   ===============             =================        =======
 7 Application      \
 6 Presentation      >----->   Application              HTTP, DNS, TLS payload
 5 Session          /
 4 Transport        ------->   Transport                TCP, UDP, QUIC
 3 Network          ------->   Internet                 IP, ICMP, routing
 2 Data Link        \
                     >----->   Link                     Ethernet, Wi-Fi, ARP
 1 Physical         /
```

| | OSI | TCP/IP |
|---|---|---|
| **Origin** | ISO standards body, ~1984 | DARPA / Internet, codified RFC 1122 (1989) |
| **Layers** | 7 | 4 |
| **Where TLS lives** | "Layer 5-6" (informally) | Inside Application, above Transport |
| **Used for** | teaching, vendor marketing ("L7 firewall") | the actual Internet |
| **Honest take** | a reference vocabulary | the implemented architecture |

> **Bridge — abstraction layers you already know.** This is the same move as a
> language runtime stack: your C# `Stream` doesn't know whether it's backed by a
> file, a socket, or memory; each layer below exposes a uniform contract. OSI
> layering is the network's equivalent of interface segregation — every layer is
> an interface, and devices implement only the interfaces they need.

---

## Encapsulation: The Onion of Headers

Every layer prepends (and sometimes appends) its own header. By the time your
HTTP request hits the wire it is wrapped four deep. This nesting is called
**encapsulation**; the unwrapping on the far side is **decapsulation**.

```
   APPLICATION:  [ HTTP request bytes ............................. ]
                                  |
   TRANSPORT:    [ TCP hdr | HTTP request bytes ................... ]   "segment"
                                  |
   NETWORK:      [ IP hdr | TCP hdr | HTTP request bytes ......... ]    "packet"
                                  |
   LINK:         [ ETH hdr | IP hdr | TCP hdr | HTTP bytes | FCS ]      "frame"
                                  |
   PHYSICAL:     1010110100101110101011010010111010101101001011101...  "bits"
```

The naming matters because the rest of this directory uses it precisely:

| Layer | Unit name | Address it uses | Key header fields |
|-------|-----------|-----------------|-------------------|
| L2 Link | **frame** | MAC (48-bit) | src/dst MAC, EtherType, FCS |
| L3 Network | **packet** | IP (32/128-bit) | src/dst IP, TTL, protocol |
| L4 Transport | **segment** (TCP) / **datagram** (UDP) | port (16-bit) | src/dst port, seq/ack, flags |
| L7 Application | **message** | URL / name | protocol-specific |

A useful discipline: when something breaks, **name the layer**. "Can't reach the
host" (L3 routing? L2 ARP?) is a different bug from "connection refused" (L4 — no
listener on the port) which is different from "TLS handshake failed" (L6/7 trust).

---

## What Each Layer Actually Owns

The hardest part of networking is keeping straight *which concern lives where*.
Five different layers all do something that sounds like "control flow," and
conflating them is the #1 source of confusion. Here is the clean separation.

```
+-------------------------------------------------------------------------+
| CONCERN              | LAYER | MECHANISM           | "ANSWERS THE Q..."  |
|----------------------|-------|---------------------|---------------------|
| Which physical port? | L2    | MAC switching       | next hop on this LAN |
| Which global host?   | L3    | IP routing          | next hop toward dest |
| Which process?       | L4    | port numbers        | which app on the host|
| Reliable delivery?   | L4    | TCP seq/ack/retx    | did it arrive intact |
| Don't overrun PEER?  | L4    | flow control (rwnd) | peer's buffer space  |
| Don't overrun NET?   | L4    | congestion control  | network's capacity   |
| What's the IP for X? | L7    | DNS                 | name -> address      |
| Who am I talking to? | L6/7  | TLS / PKI           | identity + secrecy   |
+-------------------------------------------------------------------------+
```

Two pairs deserve special emphasis because they are constantly confused:

- **Routing vs. switching.** A *switch* (L2) moves a frame to the right port on
  one LAN using MAC addresses; it has no idea the Internet exists. A *router*
  (L3) moves a packet from one network to another using IP prefixes. Switching
  is "find the right door in this building"; routing is "find the right building
  in the city." (01 and 02 respectively.)

- **Flow control vs. congestion control.** Both throttle the sender, but for
  different reasons. *Flow control* protects the **receiver** from being
  overrun (its buffer is full). *Congestion control* protects the **network**
  in between from being overrun (a link is saturated). TCP does both
  simultaneously with two separate windows. (Covered in 03 and 04.)

> **Bridge — addressing vs. routing.** If you have built a distributed system,
> you already know this split: a service *name* (DNS) resolves to an *address*
> (IP), which a *routing fabric* delivers to a *port* where a *process* listens.
> It is the same indirection chain as service discovery → endpoint → load
> balancer → pod. Networking just standardized it 40 years earlier.

---

## The Journey of One Packet

Concrete walkthrough — what happens when your laptop loads `https://example.com`.
Every numbered directory in this folder owns one step.

```
  YOU TYPE: https://example.com
     |
  (1) DNS RESOLUTION                                          --> see 05-DNS
      "example.com" -> 93.184.x.x   (cached? recurse? anycast root?)
     |
  (2) ROUTE LOOKUP                                            --> see 02-IP-ROUTING
      Is dst on my subnet? No -> send to default gateway.
     |
  (3) ARP / LINK                                              --> see 01-LINK-LAYER
      "What MAC owns the gateway IP?" -> build Ethernet frame.
     |
  (4) NAT (home/CGNAT)                                        --> see 07-NAT
      Rewrite private src IP:port -> public IP:port; remember mapping.
     |
  (5) TCP / QUIC HANDSHAKE                                    --> see 03-TRANSPORT
      SYN / SYN-ACK / ACK establishes a connection to port 443.
     |
  (6) CONGESTION CONTROL ramps the send rate                  --> see 04-CONGESTION
      slow start -> probe for bandwidth (CUBIC/BBR).
     |
  (7) TLS 1.3 HANDSHAKE                                       --> see 06-TLS
      verify cert chain, derive keys, 1-RTT to secure channel.
     |
  (8) LOAD BALANCER / CDN may answer instead of origin        --> see 08-LB-CDN
      anycast routes you to the nearest edge POP.
     |
  (9) DATACENTER FABRIC delivers to the actual server         --> see 09-DATACENTER
      leaf-spine + VXLAN overlay inside the provider.
     |
  HTTP RESPONSE flows back up every layer, in reverse.
```

Nine steps, nine guides. The rest of this directory is just each box, opened up.

---

## The Address Hierarchy

Every layer has its own namespace, and they nest. Keeping the scopes straight is
half of understanding networking.

```
+----------------------------------------------------------------+
| NAME           example.com               human-friendly, global|
|   | resolved by DNS (L7)                                        |
|   v                                                             |
| IP ADDRESS     93.184.216.34            globally routable (L3)  |
|   | mapped by ARP/NDP on the local link                         |
|   v                                                             |
| MAC ADDRESS    00:1b:44:11:3a:b7        link-local only (L2)    |
|   | identifies a NIC on one segment; never crosses a router     |
|   v                                                             |
| PORT           :443                     which process (L4)      |
+----------------------------------------------------------------+

  SCOPE:  MAC = this LAN only.  IP = whole Internet.  Name = human memory.
          The MAC changes at every router hop; the IP (usually) does not.
```

This last point trips everyone up: as a packet crosses routers, the **L3
source/destination IPs stay the same end-to-end** (modulo NAT), but the **L2
source/destination MACs are rewritten at every single hop** — because MAC
addressing is link-local. The router strips the incoming frame, keeps the
packet, and builds a *brand new* frame for the next link.

---

## Where This Directory Sits in the Library

```
            telecommunications/   <-- L1: spectrum, modulation, the wire itself
                    |
                    v
   +-------------------------------------+
   |          networking/                |   L2-L7: this directory
   |   wire -> frames -> packets ->       |
   |   segments -> sessions -> trust     |
   +-------------------------------------+
         |              |            |
         v              v            v
  distributed-      cloud-       cryptography/
  systems/          architecture/  (TLS internals,
  (what rides       (LB, CDN,       cert math)
   on top)           overlays)
                    |
                    v
                  os/  (sockets, the kernel network stack)
```

| Neighbor | Relationship |
|----------|--------------|
| **telecommunications/** | Owns L1 — EM spectrum, modulation, fiber, cellular. This directory starts at L2 and assumes bits arrive. |
| **distributed-systems/** | The consumers. Consensus, replication, and message queues all run *over* these transports. |
| **cloud-architecture/** | Overlaps at L4-L7 — VPCs, cloud load balancers, service mesh. 08 and 09 bridge directly. |
| **cryptography/** | The math under 06-TLS — AEAD ciphers, ECDHE, signature schemes. We use the protocols; cryptography/ proves them. |
| **os/** | The socket API and the kernel TCP/IP stack live here. Where L4 meets the application. |

---

## Decision Cheat Sheet

| I want to reason about... | Layer | Guide |
|---|---|---|
| Why a host on my LAN is unreachable | L2 | 01-LINK-LAYER |
| Why traffic to a remote network is dropping | L3 | 02-IP-ROUTING |
| Whether to use TCP or UDP or QUIC | L4 | 03-TRANSPORT |
| Why throughput is low on a long fat link | L4 | 04-CONGESTION-CONTROL |
| Why a name resolves slowly or wrong | L7 | 05-DNS |
| Why a TLS handshake fails | L6 | 06-TLS-AND-SECURITY |
| Why a connection works one-way only | NAT | 07-NAT-AND-FIREWALLS |
| How to spread traffic across many servers | L4/L7 | 08-LOAD-BALANCING-CDN |
| How traffic moves inside a datacenter | L2/L3 overlay | 09-DATACENTER-NETWORKING |
| "Which layer is this bug in?" | — | name the unit: frame/packet/segment/message |

---

## Common Confusion Points

### "OSI has 7 layers but the Internet doesn't use it?"

Correct. The Internet runs the 4-layer TCP/IP model (RFC 1122). OSI is a
*reference model* — useful vocabulary ("L3 device", "L7 proxy") and a teaching
ladder, but no production stack implements OSI's session and presentation layers
as distinct entities. When a vendor says "Layer 7 load balancer," they mean
"application-aware," mapped loosely onto OSI's top.

### "Is a switch just a faster router?"

No — they operate at different layers and answer different questions. A switch
(L2) forwards frames within one LAN by MAC address and never decrements TTL. A
router (L3) forwards packets between networks by IP prefix and is the *only*
device that crosses the L3 boundary. Many physical boxes ("L3 switches") do both,
which fuels the confusion, but the *functions* are distinct.

### "Does my IP address change as the packet travels?"

Generally no — the L3 IP addresses are end-to-end (the exception is NAT, see 07).
What changes at *every hop* is the L2 MAC addressing, because MAC scope is one
link only. Each router rebuilds the frame from scratch for the next link.

### "TCP handles reliability — so why is there separate congestion control?"

Reliability (retransmission) and congestion control are related but distinct.
Retransmission fixes *loss after it happens*. Congestion control *adjusts the
sending rate to avoid causing loss in the first place* by inferring the
network's capacity. And both are different again from flow control, which
respects the *receiver's* buffer. Three separate mechanisms, all at L4 — see 03
and 04.

### "Where exactly does TLS live?"

Above L4, below the application payload. TLS runs as a session over an
already-established TCP connection (or, in QUIC, fused into the transport
itself). It is "L6-ish" in OSI hand-waving but in the real stack it is just an
application-layer protocol that happens to encrypt everything above it. See 06.
