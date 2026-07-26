---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-TRANSPORT.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:networking:transport
kind: guide
module: networking
section: networking
title: The Transport Layer - TCP State Machine, UDP, QUIC, Ports, Sockets
status: source-custody
source_custody: partial
current_path: networking/03-TRANSPORT.md
canonical_path: networking/03-TRANSPORT.md
backsource_ids: [mdloom-backfill:networking:03-transport, git-history:networking:03-transport]
concepts: [tcp, udp, quic, ports, sockets, three-way handshake, flow control, mss]
root_concepts: [transport layer]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# The Transport Layer — TCP State Machine, UDP, QUIC, Ports, Sockets

## The Big Picture

L3 (02) delivers a packet to a *host*. The transport layer (L4) does two more
things that L3 cannot: it picks **which process** on that host (via **ports**),
and — for TCP — it turns the unreliable, unordered, lossy packet service of IP
into a **reliable, ordered byte stream**. That is the whole layer: process
multiplexing plus optional reliability. UDP gives you the first and skips the
second; TCP gives you both; QUIC reinvents TCP+TLS on top of UDP.

```
                       THE TRANSPORT LAYER MENU
   +-----------------------------------------------------------------+
   |  UDP                 TCP                    QUIC                 |
   |  ===                 ===                    ====                 |
   |  message-oriented    byte-stream            byte-streams,       |
   |  no connection       connection             many in parallel    |
   |  no reliability      reliable, ordered      reliable + encrypted|
   |  no congestion ctrl  full congestion ctrl   built-in (BBR/CUBIC)|
   |  8-byte header       20-byte header (min)   on top of UDP       |
   |  "fire and forget"   "phone call"           "TCP+TLS, faster"   |
   |                                                                 |
   |  DNS, VoIP, games    HTTP/1-2, SSH, SMTP     HTTP/3              |
   +-----------------------------------------------------------------+
        |                      |                       |
        +----- both ride on -->+ <-- IP (L3) -->       + (rides on UDP)
                            same SOCKET API (mostly)
```

The unifying abstraction above both is the **socket**: the OS endpoint your code
reads and writes. A connection is fully identified by a **5-tuple** — (protocol,
src IP, src port, dst IP, dst port) — and that tuple is what the kernel uses to
demultiplex an incoming packet to the right open socket.

> **Bridge — the stream abstraction.** TCP is the network's `Stream`: an ordered,
> reliable sequence of bytes with no message boundaries. UDP is the network's
> `Message`/datagram: discrete, possibly-lost, possibly-reordered units. If you've
> ever debugged "why did two of my writes arrive as one read?", you've met TCP's
> defining property — it is a byte stream, not a message queue.

---

## Ports and Sockets

A **port** is a 16-bit number (0–65535) identifying a process endpoint on a host.
It is the L4 address. The kernel demultiplexes incoming segments to sockets by the
full 5-tuple, which is why one server port (say 443) can hold thousands of
simultaneous client connections — they differ in the client side of the tuple.

```
   THE 5-TUPLE uniquely identifies a connection:
   ( protocol , src IP , src port , dst IP , dst port )

   A web server on 203.0.113.5:443 handling two clients:
     ( TCP, 198.51.100.7, 51514, 203.0.113.5, 443 )   <- client A
     ( TCP, 198.51.100.9, 49002, 203.0.113.5, 443 )   <- client B
              ^ different src means different sockets, SAME server port.

   PORT RANGES (IANA):
     0    - 1023   well-known  (need privilege to bind; HTTP 80, HTTPS 443)
     1024 - 49151  registered  (assigned to specific apps)
     49152- 65535  ephemeral   (the OS picks these for outbound client ports)
```

Ports worth memorizing because they appear constantly across this directory:

| Port | Protocol | Service |
|---|---|---|
| 22 | TCP | SSH |
| 25 | TCP | SMTP (mail) |
| 53 | UDP/TCP | DNS (05) |
| 80 | TCP | HTTP |
| 123 | UDP | NTP (time) |
| 443 | TCP/UDP | HTTPS (TCP) and HTTP/3/QUIC (UDP) |
| 853 | TCP | DNS-over-TLS (05) |

---

## The TCP Header

TCP's reliability machinery lives in its header fields. Minimum size is **20
bytes** (more with options).

```
   0                   1                   2                   3
   +--------+--------+--------+--------+--------+--------+--------+--------+
   |     Source Port (16)     |   Destination Port (16)                   |
   +-----------------------------------------------------------------------+
   |                  Sequence Number (32)                                |
   +-----------------------------------------------------------------------+
   |              Acknowledgment Number (32)                              |
   +-------+-----+-----------------+-------------------------------------+
   | DataOf| rsv | flags (SYN ACK  |        Window Size (16)             |
   | fset  |     |  FIN RST PSH URG)|       <- flow control rwnd          |
   +-----------------------------+-----------------------------------------+
   |     Checksum (16)           |     Urgent Pointer (16)                |
   +-----------------------------+-----------------------------------------+
   |                    Options (0-40 bytes, e.g. MSS, SACK, timestamps)  |
   +-----------------------------------------------------------------------+

   The two numbers that make TCP reliable:
     SEQ = byte offset of THIS segment's first data byte in the stream.
     ACK = "I have received everything up to byte N; send N next."
```

Sequence and acknowledgment numbers count **bytes** in the stream (not packets),
which is how TCP delivers an ordered byte stream and detects exactly what's
missing. The **window** field is flow control (below). The **flags** drive the
state machine.

---

## The TCP State Machine

TCP is a textbook finite state machine. Two ceremonies bracket every connection:
the **three-way handshake** to open and the **four-way teardown** (with the
notorious `TIME_WAIT`) to close.

```
   THREE-WAY HANDSHAKE (open):

     CLIENT                                 SERVER
        |                                      |
        |  ---- SYN, seq=x --------------->    |   "let's talk, my seq starts x"
        |                                      |
        |  <--- SYN-ACK, seq=y, ack=x+1 ---    |   "ok, my seq y, got your x"
        |                                      |
        |  ---- ACK, ack=y+1 ------------->    |   "got yours, we're open"
        |                                      |
        |=========== ESTABLISHED ==============|   (data flows both ways)

   FOUR-WAY TEARDOWN (close) — each side closes independently:

        |  ---- FIN ------------------>        |
        |  <--- ACK ------------------         |
        |  <--- FIN ------------------         |
        |  ---- ACK ------------------>        |
        |                                      |
        |  [TIME_WAIT ~2*MSL on the closer]    |
```

```
   KEY STATES (the ones you see in `netstat`/`ss`):
   CLOSED -> (open) -> SYN_SENT -> ESTABLISHED -> (close) -> FIN_WAIT_1
        -> FIN_WAIT_2 -> TIME_WAIT -> CLOSED
   server side: LISTEN -> SYN_RCVD -> ESTABLISHED -> CLOSE_WAIT -> LAST_ACK
```

`TIME_WAIT` exists on the side that closes first: it lingers (traditionally
2×MSL, the Maximum Segment Lifetime) to absorb any straggler packets from the old
connection before the 5-tuple can be reused. A box with thousands of `TIME_WAIT`
sockets is usually a server doing the active close on many short connections —
a real operational gotcha at scale.

> **Bridge — you know FSMs.** The TCP state machine is a standard FSM with the
> three-way handshake as a distributed agreement on initial sequence numbers
> (defeating old/duplicate segments). It is a tiny consensus protocol: both sides
> must agree they agree before sending data — the same "establish before commit"
> shape as a 2PC prepare phase, but for one bit of liveness.

---

## Reliability: How TCP Recovers Loss

IP loses, duplicates, and reorders packets. TCP rebuilds the original stream
using cumulative ACKs, retransmission, and (with the SACK option) selective
repair.

```
   Sender sends bytes 1..4 in four segments. Segment 2 is lost.

     seg1 (1) -> ACK 2  "got up to 1, want 2"
     seg2 (2) -> LOST
     seg3 (3) -> ACK 2  "still want 2!"  (duplicate ACK)
     seg4 (4) -> ACK 2  "still want 2!"  (duplicate ACK)
                 ^^^^^^ 3 duplicate ACKs trigger FAST RETRANSMIT of seg2
     retransmit seg2 -> ACK 5  "now I have everything through 4"

   TWO LOSS SIGNALS:
     - 3 duplicate ACKs  -> fast retransmit (mild loss; one segment)
     - RTO timer expires -> timeout retransmit (severe; reset, slow start)
```

- **Cumulative ACK**: an ACK of N means "I have *everything* up to N." Simple, but
  one early loss stalls acknowledgment of everything after it.
- **SACK (Selective ACK, RFC 2018)**: an option letting the receiver say "I have
  1, 3, and 4 but not 2," so the sender retransmits only the true gap.
- **RTO (Retransmission Timeout)** is derived from a smoothed RTT estimate plus a
  variance margin (the Jacobson/Karels algorithm); on timeout TCP retransmits and
  treats it as severe congestion (see 04).

The distinction between the *duplicate-ACK* path and the *timeout* path is the
hinge between this guide and congestion control (04): the two loss signals mean
different things and trigger different recovery aggressiveness.

---

## Flow Control vs. Congestion Control

Both throttle the sender; they protect **different** things. This is the most
important conceptual split at L4.

```
   FLOW CONTROL                          CONGESTION CONTROL
   ============                          ==================
   Protects the RECEIVER.                Protects the NETWORK.
   "Your buffer is full."                "The path is saturated."
   Signaled by: rwnd (window field       Inferred from: loss / delay /
     in the TCP header).                   ACK timing (no explicit field).
   Set by: the receiver.                 Computed by: the sender (04).

   SENDER'S ACTUAL SEND LIMIT:
       in-flight bytes  <=  min( rwnd , cwnd )
                                 ^        ^
                          receiver's   sender's congestion
                          advertised   window (see 04)
                          window
```

The sender may transmit only up to `min(rwnd, cwnd)` unacknowledged bytes. `rwnd`
is *told to it* by the receiver (flow control); `cwnd` it *computes itself* by
probing the network (congestion control, the entire subject of 04). Conflating
these two windows is the classic transport mistake; keep them separate.

---

## MSS and the MTU Chain

**MSS (Maximum Segment Size)** is the largest chunk of *application data* TCP puts
in one segment. It is derived from the link MTU (01):

```
   MTU            1500 bytes  (Ethernet payload, from 01)
   - IPv4 header   -20 bytes
   - TCP header    -20 bytes
   ----------------------------
   MSS            1460 bytes   (typical IPv4 TCP MSS)

   (IPv6 base header is 40 bytes, so MSS is typically 1440 on IPv6.)
```

If a segment is too big for some link on the path, it must fragment (costly, and
forbidden mid-path in IPv6) — so hosts run **Path MTU Discovery (PMTUD)** to find
the smallest MTU along the route and size segments to fit. A firewall (07) that
blocks the ICMP "fragmentation needed" message silently breaks PMTUD — a
notorious "works for small pages, hangs on big ones" bug.

---

## UDP — The Minimalist

**UDP (User Datagram Protocol, RFC 768)** is almost nothing, deliberately. An
**8-byte** header, no handshake, no acknowledgment, no ordering, no congestion
control. It gives you exactly what IP gives you plus ports and an optional
checksum.

```
   UDP HEADER (8 bytes total):
   +-------------+-------------+-------------+-------------+
   | Src Port(16)| Dst Port(16)| Length (16) | Checksum(16)|
   +-------------+-------------+-------------+-------------+

   USE UDP WHEN:
     - latency > reliability   (VoIP, video, games — a late packet is useless)
     - request/response is tiny (DNS — one query, one reply; 05)
     - you build your own reliability on top (QUIC does exactly this)
```

UDP's value is precisely what it *omits*: there's no head-of-line blocking, no
handshake latency, no kernel-imposed ordering. For real-time media a dropped
frame should be skipped, not retransmitted late — so UDP is the right primitive,
and the application handles whatever recovery it actually wants.

---

## QUIC — TCP Reinvented on UDP

**QUIC (RFC 9000)** is a modern transport that runs *over UDP* and fuses what used
to be three layers — TCP reliability, TLS 1.3 encryption (06), and HTTP/2-style
multiplexing — into one protocol. It is the transport beneath **HTTP/3**.

```
   THE STACK SHIFT:

   HTTP/2 over TLS over TCP        HTTP/3 over QUIC over UDP
   =======================        =========================
   +------------------+            +------------------------+
   |     HTTP/2       |            |        HTTP/3          |
   +------------------+            +------------------------+
   |     TLS 1.3      |            |   QUIC (streams + TLS  |
   +------------------+            |   1.3 + loss recovery  |
   |       TCP        |            |   + congestion ctrl)   |
   +------------------+            +------------------------+
   |       IP         |            |         UDP            |
   +------------------+            +------------------------+
                                   |         IP             |
                                   +------------------------+

   WHAT QUIC FIXES:
   - Head-of-line blocking: TCP is ONE byte stream; a single lost packet
     stalls ALL multiplexed HTTP/2 streams. QUIC has INDEPENDENT streams,
     so loss on one doesn't block the others.
   - Handshake latency: TCP+TLS = 2-3 RTTs to first byte. QUIC merges them:
     1-RTT, or 0-RTT on resumption.
   - Connection migration: QUIC uses a connection ID, not the 5-tuple, so a
     connection survives a NAT rebinding or Wi-Fi -> cellular switch.
```

Why UDP and not a brand-new IP protocol? Because the Internet's middleboxes
(NATs, firewalls — 07) only reliably pass TCP and UDP; a new L4 protocol number
would be dropped everywhere. Riding UDP is a deployability hack, and the entire
real transport lives *inside* the encrypted UDP payload, invisible to middleboxes.

> **Bridge — head-of-line blocking is a queue property.** You've hit this in
> message queues (distributed-systems/): a strict single ordered log means one
> stuck message blocks the rest, while independent partitions don't. TCP is the
> single log; QUIC's streams are independent partitions. Same trade-off,
> transport edition.

---

## Decision Cheat Sheet

| I need... | Use |
|---|---|
| Reliable, ordered byte stream | TCP |
| Lowest latency, tolerate loss (media, games) | UDP |
| Tiny request/response (a lookup) | UDP (e.g. DNS) |
| Modern web, avoid HoL blocking, mobile roaming | QUIC / HTTP/3 |
| Encryption fused with transport, 0-RTT resume | QUIC |
| To know which app a packet is for | the destination **port** |
| To identify a unique connection | the **5-tuple** |
| Don't overrun the receiver | flow control (rwnd, automatic) |
| Don't overrun the network | congestion control (cwnd, see 04) |
| Largest data per segment | MSS = MTU − IP hdr − TCP hdr |

---

## Common Confusion Points

### "Two writes, one read — is TCP broken?"

No — that's TCP working as designed. TCP is a **byte stream**, not a message
protocol; it has no concept of message boundaries. The OS may coalesce or split
your writes arbitrarily. If you need framing, you build it yourself (length
prefixes, delimiters) — exactly what every application protocol over TCP does.
UDP, by contrast, preserves datagram boundaries.

### "Why does my server have thousands of TIME_WAIT sockets?"

Because it is doing the **active close** on many short-lived connections.
`TIME_WAIT` lingers ~2×MSL on the closer to absorb stragglers before the 5-tuple
is reused. It's usually benign but can exhaust ephemeral ports at high
connection churn — a reason to use connection pooling / keep-alive, or to have the
client close first.

### "Is rwnd the same as cwnd?"

No, and conflating them is the canonical L4 mistake. `rwnd` is **flow control**:
the receiver tells the sender how much buffer it has. `cwnd` is **congestion
control** (04): the sender's own estimate of network capacity. The send limit is
`min(rwnd, cwnd)` — whichever is tighter wins.

### "QUIC is UDP, so it's unreliable like UDP?"

No. QUIC *uses* UDP as a carrier but reimplements reliability, ordering, and
congestion control *inside* the UDP payload — plus mandatory TLS 1.3 encryption.
It is at least as reliable as TCP, with better loss isolation (independent
streams) and faster handshakes. UDP here is just the lowest-overhead vehicle that
survives NATs and firewalls.

### "Why does a big download hang while small pages load fine?"

Classic broken **PMTUD**. A firewall (07) is dropping the ICMP "fragmentation
needed" message, so the sender never learns to shrink its segments below a
path's MTU; full-size segments get silently dropped. Small responses fit; large
transfers stall. The fix is to allow the relevant ICMP, or clamp MSS at the
gateway.
