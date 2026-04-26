# Networking — The Modern Stack

> **Audience note**: This guide assumes TCP/IP, DNS, and HTTP/1.1 fundamentals at the level of someone who built them. Sections 1–3 (IP/TCP/DNS) are reference — skim or skip. The high-value sections are 4+ (HTTP/2–3, QUIC, gRPC, modern TLS, WebSockets).
> Jump to: [HTTP version evolution](#4-http11--http2--http3) · [TLS 1.3](#5-tls-13-deep-dive) · [QUIC/HTTP3](#http3--quic) · [gRPC](#7-grpc) · [WebSockets](#6-websockets) · [Network Security / Zero Trust](#11-network-security)

## The Big Picture

```
+--------------------------------------------------------------------------------+
|  APPLICATION LAYER                                                             |
|  DNS   HTTP/1.1   HTTP/2   HTTP/3(QUIC)   WebSocket   gRPC   TLS               |
+--------------------------------------------------------------------------------+
              |                |                 |               |
+--------------------------------------------------------------------------------+
|  TRANSPORT LAYER                                                               |
|  TCP (reliable, ordered, flow-controlled)                                      |
|  UDP (unreliable, unordered, low-overhead)                                     |
|  QUIC (UDP-based, streams, built-in TLS 1.3)                                   |
+--------------------------------------------------------------------------------+
              |                |                 |
+--------------------------------------------------------------------------------+
|  NETWORK LAYER                                                                 |
|  IPv4 / IPv6   ICMP   BGP / OSPF (routing)   NAT   IPsec                       |
+--------------------------------------------------------------------------------+
              |
+--------------------------------------------------------------------------------+
|  DATA LINK LAYER                                                               |
|  Ethernet   MAC addresses   ARP   VLANs (802.1Q)   Spanning Tree (802.1D)      |
+--------------------------------------------------------------------------------+
              |
+--------------------------------------------------------------------------------+
|  PHYSICAL LAYER                                                                |
|  Copper, fiber, radio — not covered here                                       |
+--------------------------------------------------------------------------------+
```

### Real-World: What Happens on a Single HTTPS API Call

```
You call: GET https://api.example.com/users/42
                              |
    1. DNS RESOLUTION (Application layer)
       Stub resolver → OS cache → Recursive resolver (8.8.8.8)
       → Root NS → .com TLD NS → example.com authoritative NS
       Result: 104.18.22.119
                              |
    2. TCP 3-WAY HANDSHAKE (Transport layer)
       SYN → SYN-ACK → ACK  [~1 RTT]
                              |
    3. TLS 1.3 HANDSHAKE (Application layer over TCP)
       ClientHello + key_share → ServerHello + Certificate + Finished
       Client Finished  [~1 RTT, 0-RTT possible on resume]
                              |
    4. HTTP/2 REQUEST (Application layer, binary)
       HEADERS frame: method=GET, path=/users/42, authority=api.example.com
       Server responds: HEADERS (200) + DATA (JSON body)
                              |
    5. TCP TEARDOWN
       FIN → FIN-ACK → FIN → ACK  [or connection reused via keep-alive]
```

On a cold start to a new host with no DNS cache: approximately 2.5–3 RTTs before you see data.
HTTP/2 over TLS 1.3 brings this to 2 RTTs. QUIC/HTTP/3 can reach 1 RTT (0-RTT on resume).

---

## 1. IP & Subnetting

### Subnetting Reference Table

| CIDR | Subnet Mask     | Hosts (usable) | Use Case                              |
|------|-----------------|----------------|---------------------------------------|
| /8   | 255.0.0.0       | 16,777,214     | Large private networks (Class A)      |
| /16  | 255.255.0.0     | 65,534         | Corporate networks, Azure VNets       |
| /24  | 255.255.255.0   | 254            | Typical subnet, home networks         |
| /25  | 255.255.255.128 | 126            | Split a /24 in half                   |
| /26  | 255.255.255.192 | 62             | Medium-sized subnet                   |
| /27  | 255.255.255.224 | 30             | Small subnet                          |
| /28  | 255.255.255.240 | 14             | Azure delegated subnets (min size)    |
| /29  | 255.255.255.248 | 6              | Point-to-point links with spares      |
| /30  | 255.255.255.252 | 2              | Point-to-point links (exactly 2 ends) |
| /31  | 255.255.255.254 | 2 (no bcast)   | RFC 3021 P2P — no network/bcast addr |
| /32  | 255.255.255.255 | 1              | Host route, loopback, specific rule   |

Azure reserves 5 addresses per subnet (0=network, 1=default gateway, 2–3=Azure DNS, 255=broadcast).
A /28 gives 16 - 5 = 11 usable IPs in Azure.

### Private Address Ranges (RFC 1918)

| Range                      | CIDR           | Size     | Common Use                      |
|----------------------------|----------------|----------|---------------------------------|
| 10.0.0.0 – 10.255.255.255  | 10.0.0.0/8     | 16M IPs  | Large enterprises, Azure VNets  |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12  | 1M IPs   | Docker default bridge (172.17.x) |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | 65K IPs | Home/SOHO networks              |

Also: `169.254.0.0/16` (link-local, APIPA — assigned when DHCP fails)
`127.0.0.0/8` (loopback — only `127.0.0.1` used in practice)

### NAT — Network Address Translation

```
PRIVATE NETWORK                         PUBLIC INTERNET
192.168.1.10:54321  ─────────────────►  203.0.113.5:80
                      NAT DEVICE
                   src: 192.168.1.10:54321
                   translated to: 1.2.3.4:49152
                       Connection table:
                       1.2.3.4:49152 ↔ 192.168.1.10:54321
```

**SNAT (Source NAT)**: Rewrites the source address. Used for outbound traffic (private → internet).
**DNAT (Destination NAT)**: Rewrites the destination address. Used for inbound traffic (port forwarding, load balancing).
**PAT / NAPT (Port Address Translation)**: Many private IPs share one public IP via unique port mappings. What home routers do.

Connection tracking maintains the state table. Stateless firewalls cannot do NAT — stateful required.

### IPv6 Transition Mechanisms

IPv6 addresses are 128-bit. Dual-stack and NAT64 are the two main transition paths.

**Dual-stack**: host has both IPv4 and IPv6 addresses. Happy Eyeballs (RFC 8305) races both, uses whichever connects first (prefers IPv6). This is the right default posture for new Azure VNet deployments — enable both address families on subnets and NICs.

**NAT64 / DNS64**: IPv6-only clients communicating with IPv4-only servers. DNS64 synthesizes AAAA records from A records using a well-known prefix (64:ff9b::/96). NAT64 at the network edge translates IPv6 packets to IPv4. Common in mobile networks (iOS requires NAT64 compatibility for App Store approval).

**CGNAT (Carrier-Grade NAT)**: ISPs sharing one public IPv4 across thousands of subscribers. Implications:
- IoT devices behind CGNAT cannot be directly addressed (no inbound connectivity)
- `src_ip` logging is useless for attribution — thousands of customers share one IP
- Ephemeral port starvation hits harder (shared pool)
- Solution: use IPv6 everywhere possible; for IoT, use outbound-initiated connections (MQTT, long-poll) since CGNAT state is maintained for outbound sessions

| Address Type       | Prefix          | Notes                                     |
|--------------------|-----------------|-------------------------------------------|
| Global unicast     | 2000::/3        | Publicly routable (2001:db8::/32 = docs) |
| Link-local         | fe80::/10       | Non-routable, auto-configured per NIC     |
| Unique local       | fc00::/7        | RFC 4193, private (like RFC 1918)         |
| Multicast          | ff00::/8        | No broadcast in IPv6 — multicast instead  |
| Loopback           | ::1/128         |                                           |

---

## 2. TCP Deep Dive

### 3-Way Handshake + 4-Way Teardown

```
CONNECT:                       CLOSE:
Client      Server             Client      Server
  │── SYN ─────►│               │── FIN ─────►│  "done sending"
  │◄── SYN-ACK ─│               │◄── ACK ─────│  (half-close)
  │── ACK ─────►│               │◄── FIN ─────│  "I'm done too"
  [ESTABLISHED]                 │── ACK ─────►│
                                [TIME_WAIT on client: 2×MSL]
```

### TIME_WAIT Exhaustion

After 4-way teardown the connection initiator (usually client) holds TIME_WAIT for `2 × MSL` (~4 minutes). Purpose: ensure final ACK reaches server; prevent stale segments confusing a new same-4-tuple connection.

**At scale — the problem**: a reverse proxy or microservice making many outbound connections to the same upstream can exhaust ephemeral ports (typically 32768–60999, ~28K ports). At 4-minute TIME_WAIT, max outbound connection rate = 28000 / 240 ≈ 116 new connections/sec to the same destination.

**Mitigations**:
- `net.ipv4.tcp_tw_reuse = 1` (Linux): reuse TIME_WAIT sockets for new outbound connections (safe for outbound)
- `SO_REUSEPORT`: multiple sockets bind the same port — enables kernel-level load distribution per-CPU (also helps inbound acceptance throughput)
- Connection pooling: the real fix. Keep connections alive, amortize handshake cost. HTTP/2 multiplexing, database connection pools, gRPC channels all do this.

### BBR vs CUBIC Congestion Control

CUBIC (Linux default since 2006) is loss-based: grows cwnd aggressively, backs off on packet loss. Works well on low-BDP links. Problem: on high-BDP links (satellite, trans-ocean fiber) with shallow buffers, CUBIC doesn't fill the pipe efficiently; it backs off before the bottleneck is actually saturated.

**BBR (Bottleneck Bandwidth and RTT)** — Google, 2016: instead of reacting to loss, BBR estimates bandwidth and RTT directly via probing. It targets the bandwidth-delay product directly.

```
CUBIC behavior on high-BDP link:
  cwnd grows → buffer fills → packet dropped → cwnd halved → repeat
  [shallow buffer + high RTT = terrible utilization]

BBR behavior:
  Probes bandwidth (short bursts), measures RTT baseline
  Keeps inflight ≈ BDP (bandwidth × RTT) — avoids filling buffers
  [better throughput + lower latency on high-BDP links]
```

When it matters for your systems:
- Cross-region Azure calls (eastus → westeurope) — high RTT, BBR wins
- Kubernetes egress over public internet — BBR outperforms CUBIC ~10–30% on trans-ocean paths
- Within a datacenter/region — difference is negligible (low RTT, both work)
- Enable: `sysctl -w net.ipv4.tcp_congestion_control=bbr` (requires Linux 4.9+)

### Useful Socket Options

| Option              | Effect                                                                 |
|---------------------|------------------------------------------------------------------------|
| `TCP_NODELAY`       | Disable Nagle — send immediately, don't buffer small writes            |
| `SO_KEEPALIVE`      | Enable TCP keepalive probes for idle connections                       |
| `TCP_KEEPIDLE`      | Seconds of idle before first keepalive probe (Linux, default 7200)     |
| `TCP_KEEPINTVL`     | Interval between keepalive probes                                      |
| `TCP_KEEPCNT`       | Number of probes before declaring connection dead                      |
| `SO_REUSEADDR`      | Allow binding to an address in TIME_WAIT                               |
| `SO_REUSEPORT`      | Multiple sockets can bind to the same port (Linux load distribution)   |
| `TCP_FASTOPEN`      | Send data in the SYN packet on reconnect (saves 1 RTT on reconnection) |
| `SO_LINGER`         | Control behavior on close() — whether to wait for data to flush        |

**TCP_FASTOPEN**: client caches a Fast Open Cookie from the first connection. On subsequent connections, sends data in the SYN itself — server processes it immediately, saves 1 full RTT. Useful for short-lived connections (CDN origin pulls, DNS over TCP). Kernel support required both ends; Linux 3.7+, enabled with `tcp_fastopen = 3`.

**Receive buffer tuning**: default rmem/wmem (87KB) undersizes high-BDP paths. For 100ms RTT at 1Gbps, BDP = 12.5 MB. Set:
```
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_wmem = 4096 65536 16777216
net.core.rmem_max = 16777216
```

### Nagle's Algorithm

Buffers small writes until an ACK arrives or the buffer reaches MSS (1460 bytes on Ethernet). Reduces tiny-segment flooding on chatty connections. Adds latency on interactive protocols.

```c
socket.setNoDelay(true);   // Node.js — sets TCP_NODELAY
tcpClient.NoDelay = true;  // .NET
```

### TCP vs UDP

| Dimension         | TCP                                    | UDP                                    |
|-------------------|----------------------------------------|----------------------------------------|
| Reliability       | Guaranteed delivery, retransmission    | Best-effort, no retransmission         |
| Ordering          | In-order delivery                      | Out-of-order possible                  |
| Connection        | Stateful (3-way handshake)             | Stateless                              |
| Flow control      | Yes (rwnd)                             | No                                     |
| Congestion control | Yes (cwnd, CUBIC/BBR)                  | No                                     |
| Head-of-line block | Yes — lost packet blocks stream        | No — each packet independent           |
| Overhead          | 20-byte header + state                 | 8-byte header, no state                |
| Use cases         | HTTP, databases, SSH, email            | DNS, gaming, video streams, QUIC       |

---

## 3. DNS

DNS resolution chain (3 lines): stub resolver checks OS cache → forwards to recursive resolver (e.g., 8.8.8.8) → recursive resolver iterates root → TLD → authoritative NS, caches result per TTL, returns to caller.

`dig +trace example.com` shows the full iterative chain. `dig @8.8.8.8 example.com` bypasses OS resolver.

### Record Types

| Type  | Purpose                                         | Example                                           |
|-------|-------------------------------------------------|---------------------------------------------------|
| A     | Hostname → IPv4 address                         | `example.com. → 93.184.216.34`                    |
| AAAA  | Hostname → IPv6 address                         | `example.com. → 2606:2800:220:1:248:1893:25c8:1946` |
| CNAME | Hostname → another hostname (alias)             | `www.example.com. → example.com.`                 |
| MX    | Mail exchange server for domain                 | `example.com. 10 mail.example.com.`               |
| TXT   | Arbitrary text — SPF, DKIM, DMARC, domain verify | `"v=spf1 include:_spf.google.com ~all"`           |
| NS    | Authoritative nameservers for zone              | `example.com. NS ns1.example.com.`                |
| SOA   | Start of Authority — zone metadata              | serial, refresh, retry, expire, minimum TTL       |
| SRV   | Service location (host + port)                  | `_grpc._tcp.example.com. 0 5 50051 api.example.com.` |
| PTR   | Reverse DNS — IP → hostname                     | `34.216.184.93.in-addr.arpa. → example.com.`      |
| CAA   | Authorized certificate authorities for domain   | `example.com. CAA 0 issue "letsencrypt.org"`      |
| TLSA  | DANE — cert pinning in DNS (requires DNSSEC)    |                                                   |

### Negative Caching (NXDOMAIN TTL)

`NXDOMAIN` responses are cached with a TTL taken from the SOA record's `minimum` field (commonly 300–3600 seconds). Implications:
- You deleted the wrong record and re-added it — clients still get NXDOMAIN until the negative TTL expires
- Accidental NXDOMAIN during a migration is sticky for minutes to hours
- Lower the SOA minimum before any DNS surgery; raise it back after
- Pre-lowering TTL 24–48 hours before a change is standard practice

**CNAME at zone apex**: A CNAME cannot coexist with SOA/NS records. Use ALIAS/ANAME extensions (CloudFlare, Route 53 ALIAS) for apex domains — they flatten the CNAME at serve time.

### Split-Horizon DNS

Same name resolves differently depending on who's asking.

```
External query:  api.example.com → 40.112.45.67    (public IP)
Internal query:  api.example.com → 10.0.1.42       (private IP in VNet)
```

Azure Private DNS Zones implement this. A private zone linked to a VNet makes internal services resolvable by private IP. External resolvers never see the private zone. Critical pattern: internal-only services should have their public DNS disabled once Private Endpoints are in place.

For hybrid scenarios: Azure DNS Private Resolver forwards on-premises DNS queries to Azure Private DNS, and vice versa, without requiring DNS forwarder VMs. Replaces the old "DNS forwarder VM in every hub VNet" pattern.

### DNS over HTTPS (DoH) / DNS over TLS (DoT)

Standard DNS is plaintext UDP/TCP. ISP and network operators can see and modify DNS queries.

| Protocol | Port | Transport         | Notes                                    |
|----------|------|-------------------|------------------------------------------|
| DNS      | 53   | UDP/TCP plaintext | Default, observable by network           |
| DoT      | 853  | TCP + TLS         | RFC 7858, easy to block (single port)    |
| DoH      | 443  | HTTP/2 + TLS      | RFC 8484, looks like HTTPS, hard to block |

**Enterprise split-horizon risk with DoH**: browsers (Firefox, Chrome) use DoH by default to their own resolvers (Cloudflare 1.1.1.1, Google 8.8.8.8), bypassing OS resolver configuration entirely. This breaks enterprise split-horizon DNS, DNS-based filtering, and DNS-based traffic steering. Enterprise mitigation: configure canary domains (Firefox checks `use-application-dns.net`; if NXDOMAIN, DoH disabled) or push Managed Browser Policy that forces OS resolver.

### DNSSEC

Chain of trust from root zone down to leaf record.

```
Root Zone  (trust anchor — root KSK baked into resolvers)
    ↓  signs
.com Zone
    ↓  signs
example.com Zone
    ↓  signs
api.example.com A record
```

Each zone has a ZSK (Zone Signing Key) for signing records and a KSK (Key Signing Key) for signing the ZSK. Parent zone publishes the child's KSK fingerprint as a DS (Delegation Signer) record. RRSIG records carry the signatures. NSEC/NSEC3 provides authenticated denial of existence.

**DNSSEC does NOT encrypt DNS** — it only authenticates. DoH/DoT provides privacy; DNSSEC provides integrity.

**DNSSEC deployment reality**: most public zones are signed; enterprise zones usually are not. Key rollover is operationally complex (KSK rollover requires coordination with parent zone). The 2018 ICANN KSK rollover was delayed a year due to widespread misconfigured resolvers. For internal Azure DNS: Azure-managed DNS zones do not support DNSSEC as of 2024 — external providers (Cloudflare, Route 53) support it.

### Common DNS Gotchas

- `TTL` on a CNAME: both the CNAME TTL and the target A record TTL matter. Final IP cached for A record's TTL.
- DNS cache poisoning (Kaminsky attack): forged DNS responses injecting false records. Mitigated by source port randomization, DNSSEC.
- Negative caching of `NXDOMAIN` means "I deleted the wrong record — just add it back" is not instant.
- `dig +trace example.com` shows the full iterative resolution chain. Invaluable for debugging.

---

## HTTP Version Evolution

Before diving into per-version details, the lineage in one table:

| Version | Problem it solves | Key mechanism | Still use? |
|---------|-------------------|---------------|------------|
| HTTP/1.1 | Persistent connections vs HTTP/1.0 | Keep-Alive, pipelining (broken in practice) | Yes — universal fallback |
| HTTP/2 | Application-layer head-of-line blocking | Multiplexed streams, binary framing, HPACK compression — all over a single TLS connection | Yes — current default |
| HTTP/3 / QUIC | TCP-layer HOL blocking + 0-RTT reconnection | UDP-based QUIC with per-stream loss recovery, TLS 1.3 built in | Growing — ~30% of web traffic (2024) |

The distinction matters: HTTP/2 fixes HOL blocking **at the HTTP layer** (multiple requests on one connection without waiting). But HTTP/2 still runs over TCP — one lost TCP segment stalls **all** HTTP/2 streams. HTTP/3 fixes HOL blocking **at the transport layer** by running over QUIC/UDP where each stream is independently loss-recovered.

---

## 4. HTTP/1.1 → HTTP/2 → HTTP/3

### HTTP/1.1

Request format (text-based):
```
GET /users/42 HTTP/1.1\r\n
Host: api.example.com\r\n
Accept: application/json\r\n
Authorization: Bearer eyJ...\r\n
\r\n
```

Response:
```
HTTP/1.1 200 OK\r\n
Content-Type: application/json\r\n
Content-Length: 82\r\n
Cache-Control: max-age=60\r\n
ETag: "abc123"\r\n
\r\n
{"id":42,"name":"Alice",...}
```

**Connection: keep-alive** (default in HTTP/1.1): reuse TCP connection for multiple requests. Avoids repeated handshake cost.

**Head-of-line blocking**: HTTP/1.1 processes requests sequentially on a connection. Request N must complete before request N+1 begins (in practice — pipelining is the supposed fix).

**Pipelining**: Send multiple requests without waiting for responses. Theoretically fixes HOL blocking. In practice: proxy and server implementations buggy, responses still in-order → never widely deployed. Browsers disabled it.

**Workarounds (HTTP/1.1 era)**:
- Domain sharding: open 6 connections per origin (browser limit) to parallelize
- Sprite sheets, concatenated CSS/JS: reduce request count
- These hacks become anti-patterns under HTTP/2

### Key HTTP Headers

| Header                           | Purpose                                                              |
|----------------------------------|----------------------------------------------------------------------|
| `Cache-Control: max-age=3600`    | Cache for 3600 seconds                                               |
| `Cache-Control: no-cache`        | Must revalidate before using (NOT "don't cache")                     |
| `Cache-Control: no-store`        | Do not store anywhere (truly don't cache — e.g., auth pages)        |
| `Cache-Control: private`         | Browser can cache; CDN/shared cache cannot                           |
| `Cache-Control: s-maxage=3600`   | Shared cache (CDN) TTL, overrides max-age for CDN                    |
| `Cache-Control: stale-while-revalidate=60` | Serve stale while revalidating in background               |
| `ETag: "abc123"`                 | Entity tag — opaque version identifier                               |
| `If-None-Match: "abc123"`        | Conditional GET — 304 if unchanged                                   |
| `Last-Modified: Tue, 01 Jan 2025 00:00:00 GMT` | Last modification time                              |
| `If-Modified-Since: ...`         | Conditional GET by time — 304 if unchanged                           |
| `Vary: Accept-Encoding`          | Cache key includes Accept-Encoding — separate cache entries per value |
| `Content-Encoding: gzip`         | Response body is gzip-compressed                                     |
| `Transfer-Encoding: chunked`     | Body sent as chunks, length unknown upfront (streaming)              |

### HTTP/2

RFC 7540 (2015), updated RFC 9113 (2022).

```
HTTP/1.1 (text, one request per connection slot):
──────────────────────────────────────────────────
GET /a    response-a    GET /b    response-b    GET /c    response-c
[blocking each other on single connection]

HTTP/2 (binary, multiplexed streams on single TCP connection):
──────────────────────────────────────────────────────────────────
Stream 1: GET /a ────────────────────────────────► response-a
Stream 3: GET /b ──────────────────────────────────────► response-b
Stream 5: GET /c ─────────────────────────────────────────────► response-c
          [all in-flight simultaneously, no domain sharding needed]
```

**Binary framing**: HTTP/2 wraps everything in frames. Each frame has a 9-byte header: length (24 bits), type (8 bits), flags (8 bits), stream ID (31 bits).

Key frame types:
- `HEADERS`: request/response headers (compressed with HPACK)
- `DATA`: request/response body
- `SETTINGS`: negotiation of parameters
- `WINDOW_UPDATE`: flow control
- `PING`: keepalive / RTT measurement
- `GOAWAY`: graceful shutdown, tells client max processed stream ID

**HPACK header compression** (RFC 7541):
- Static table: 61 predefined header name-value pairs (`:method: GET` = index 2)
- Dynamic table: headers seen in this connection, added as encountered
- Huffman encoding: compress header values
- Result: headers that repeated are sent as a single index byte. Massive reduction vs HTTP/1.1

**Multiplexing**: Stream IDs are odd (client-initiated) or even (server-initiated). Stream 0 is the connection-level control stream.

**HTTP/2 head-of-line blocking**: HTTP/2 solves APPLICATION-level HOL. But it still runs over TCP. A single lost TCP segment blocks all HTTP/2 streams until retransmitted. This is transport-level HOL blocking — not fixed until HTTP/3.

**Server Push**: Server proactively sends resources before client requests them. Turned out to be hard to use correctly (double-push, cache issues). Removed from most browser implementations. HTTP 103 Early Hints is the replacement (hints to preload before main response).

### HTTP/3 / QUIC

QUIC: RFC 9000. HTTP/3: RFC 9114.

```
HTTP/2 over TCP:
┌────────────────────────────────────────────┐
│  HTTP/2 Streams                            │
│  Stream 1  Stream 3  Stream 5  Stream 7    │
├────────────────────────────────────────────┤
│  TLS 1.3 Record Layer                      │
├────────────────────────────────────────────┤
│  TCP (ordered, reliable byte stream)       │  ← single lost packet blocks ALL streams
└────────────────────────────────────────────┘

HTTP/3 over QUIC:
┌──────────────────────────────────────────────────────────┐
│  HTTP/3 Streams                                          │
│  Stream 1  Stream 3  Stream 5  Stream 7                  │
├──────────────────────────────────────────────────────────┤
│  QUIC (stream multiplexing, per-stream loss recovery)    │  ← lost packet only blocks its stream
├──────────────────────────────────────────────────────────┤
│  TLS 1.3 (built into QUIC handshake)                     │
├──────────────────────────────────────────────────────────┤
│  UDP                                                     │
└──────────────────────────────────────────────────────────┘
```

**Why UDP**: QUIC implements reliability at the QUIC layer, not the OS/kernel TCP layer. This means:
1. QUIC can evolve without kernel changes (UDP is universal)
2. Per-stream loss recovery — a lost packet only blocks the stream that contains it
3. Avoids TCP's HOL blocking

**Built-in TLS 1.3**: QUIC doesn't layer TLS on top — TLS is integrated into the QUIC handshake. The packet protection (encryption) is done by QUIC using TLS keys. No separate TLS record layer.

**1-RTT handshake**: QUIC connection + TLS negotiated in 1 RTT. First data can be sent as part of the handshake.

**0-RTT**: On reconnection to a known server, client can send application data in the first UDP datagram (0 RTTs before data). Uses a session ticket (PSK — Pre-Shared Key) from the previous session.

```
0-RTT flow:
Client ──── QUIC Initial + Early Data (0-RTT) ────► Server
            [app data piggybacks on the handshake packet]
Server ──── QUIC Handshake + Response ─────────────► Client
```

**0-RTT replay risk**: Early data can be replayed by an attacker. The server cannot tell a legitimate 0-RTT request from a replayed one (no RTT to verify freshness). Only safe for idempotent operations (GET, not POST). Some deployments disable 0-RTT entirely.

**Connection migration**: QUIC connections are identified by a Connection ID (not the 4-tuple). When a mobile device switches from WiFi to LTE (IP changes), the QUIC connection survives. TCP would require a new handshake.

**Adoption**: ~30% of web traffic as of 2024. Major CDNs (Cloudflare, Akamai, AWS CloudFront) support it. HTTP/3 negotiated via `Alt-Svc` header or HTTPS DNS record.

---

## 5. TLS 1.3 Deep Dive

### TLS 1.3 Handshake (1-RTT)

```
Client                                          Server
  │                                               │
  │── ClientHello ───────────────────────────────►│
  │   supported_versions: [TLS 1.3, TLS 1.2]      │
  │   key_share: ECDH public key (x25519)          │
  │   cipher_suites: [AES-256-GCM, ChaCha20, ...]  │
  │   supported_groups: [x25519, P-256, P-384]     │
  │   server_name: api.example.com (SNI)           │
  │                                               │
  │◄─ ServerHello ────────────────────────────────│
  │   selected_version: TLS 1.3                   │
  │   key_share: ECDH public key (x25519)         │
  │   selected_cipher: TLS_AES_256_GCM_SHA384     │
  │                                               │
  │   [Both sides derive session keys via HKDF    │
  │    from ECDH shared secret + nonces]           │
  │                                               │
  │◄─ {EncryptedExtensions} ──────────────────────│  encrypted from here
  │◄─ {Certificate} ──────────────────────────────│  server's X.509 cert
  │◄─ {CertificateVerify} ────────────────────────│  signature over transcript
  │◄─ {Finished} ─────────────────────────────────│  MAC over transcript
  │                                               │
  │── {Finished} ────────────────────────────────►│
  │                                               │
  │          [Application Data]                   │
```

Total: 1 RTT. Compare TLS 1.2: 2 RTTs (or 1 RTT with False Start, but non-standard).

### TLS 1.2 vs TLS 1.3

| Feature                     | TLS 1.2                              | TLS 1.3                               |
|-----------------------------|--------------------------------------|---------------------------------------|
| Handshake RTTs              | 2 RTT (1 RTT with session resumption) | 1 RTT (0-RTT on resumption)           |
| RSA key exchange            | Supported (no forward secrecy)       | **Removed**                           |
| Key exchange                | RSA, DHE, ECDHE                      | **Only (EC)DHE** — always PFS         |
| Cipher suites               | 300+ (many weak)                     | **5 only** (all AEAD)                 |
| Compression                 | Supported (CRIME attack)             | Removed                               |
| Renegotiation               | Supported (attack surface)           | Removed                               |
| Session tickets             | Supported                            | Supported (PSK)                       |
| Certificate in handshake    | Plaintext                            | **Encrypted** (after key exchange)    |
| Downgrade protection        | SCSV extension                       | Built-in (random sentinel values)     |

### Cipher Suites in TLS 1.3

Only 5 cipher suites:
- `TLS_AES_128_GCM_SHA256`
- `TLS_AES_256_GCM_SHA384`
- `TLS_CHACHA20_POLY1305_SHA256`
- `TLS_AES_128_CCM_SHA256`
- `TLS_AES_128_CCM_8_SHA256`

All are AEAD (Authenticated Encryption with Associated Data). No CBC, no RC4, no MD5, no SHA-1.

### Key Exchange: ECDHE

Elliptic Curve Diffie-Hellman Ephemeral.

```
Client and Server agree on curve (e.g., x25519)
Client generates: private key c, public key C = c × G
Server generates: private key s, public key S = s × G
Client sends C, Server sends S
Shared secret = c × S = s × C = c × s × G
Neither side's long-term private key was used → forward secrecy
```

Forward secrecy: compromise of the server's long-term private key does not decrypt past sessions. Each session uses a fresh ephemeral key pair.

### X.509 Certificate Chain

```
Root CA (self-signed, baked into OS/browser trust stores)
    └── Intermediate CA (signed by Root CA)
            └── Leaf Certificate (signed by Intermediate CA)
                    subject: CN=api.example.com
                    subjectAltName: DNS:api.example.com, DNS:*.example.com
                    publicKey: [server's public key]
                    validity: 2025-01-01 to 2025-04-01 (Let's Encrypt: 90 days)
                    issuer: [Intermediate CA]
                    signature: [Intermediate CA's signature over above]
```

Client verifies: signature chain is valid, root is trusted, cert is not expired, subject matches SNI.

### SNI and ALPN

**SNI (Server Name Indication)**: The `server_name` extension in ClientHello. Tells the server which certificate to present. Required for virtual hosting — multiple HTTPS sites on one IP. SNI is sent in plaintext (encrypted in TLS 1.3's ECH — Encrypted ClientHello, still emerging).

**ALPN (Application-Layer Protocol Negotiation)**: The `application_layer_protocol_negotiation` extension. Client offers list: `["h2", "http/1.1"]`. Server picks one. This is how HTTP/2 is negotiated over TLS. Without ALPN, you'd have to use a different port for HTTP/2.

### mTLS (Mutual TLS)

Standard TLS: client verifies server's cert. Server doesn't verify client.
mTLS: both sides present and verify certificates.

```
Client                          Server
  │── ClientHello ─────────────►│
  │◄─ ServerHello + Cert ────────│
  │◄─ CertificateRequest ────────│  ← server demands client cert
  │── Certificate (client cert) ►│
  │── CertificateVerify ─────────►│
  │── Finished ──────────────────►│
```

Use cases: service mesh (Istio, Linkerd), internal APIs, IoT device auth. Eliminates shared secret / API key management at service level.

### Certificate Pinning

Hardcode expected certificate / public key hash in the client. Client rejects any cert not matching, even if signed by a trusted CA.

| Approach          | Pin What                | Rotation Difficulty | Use Case                         |
|-------------------|-------------------------|---------------------|----------------------------------|
| Cert pinning      | Full cert               | Hard (90-day cycle) | Generally avoid                  |
| SPKI pinning      | Subject Public Key Info | Medium (new key = new pin) | Mobile apps with long-lived installs |
| CA pinning        | Specific CA cert        | Low                 | Better than cert pinning          |

HPKP (HTTP Public Key Pinning) header — deprecated and removed from browsers. Too many sites bricked themselves with bad pins.

### OCSP Stapling

Normally: client contacts OCSP responder to check cert revocation → extra RTT + privacy leak.
OCSP stapling: server fetches its own OCSP response, caches it, includes ("staples") it in the TLS handshake. Client gets revocation status without a separate request.

---

## 6. WebSockets

### Upgrade Handshake

```
Client → Server:
GET /chat HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==   ← random base64 nonce
Sec-WebSocket-Version: 13

Server → Client:
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
                      ← SHA-1(key + magic GUID), base64
```

After `101`, the TCP connection is no longer HTTP. Frames flow in both directions.

### Frame Format

```
  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
 +-+-+-+-+-------+-+-------------+-------------------------------+
 |F|R|R|R| opcode|M| Payload len |    Extended payload length    |
 |I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
 |N|V|V|V|       |S|             |  (if payload len==126/127)    |
 | |1|2|3|       |K|             |                               |
 +-+-+-+-+-------+-+-------------+ - - - - - - - - - - - - - - -+
```

| Opcode | Meaning                        |
|--------|--------------------------------|
| 0x0    | Continuation frame             |
| 0x1    | Text frame (UTF-8)             |
| 0x2    | Binary frame                   |
| 0x8    | Close frame                    |
| 0x9    | Ping                           |
| 0xA    | Pong                           |

**Masking**: Client-to-server frames MUST be masked (XOR with 32-bit masking key). Server-to-client MUST NOT be masked. Mitigates cache poisoning attacks on proxies.

### WebSocket vs SSE vs HTTP/2 Push

| Feature             | WebSocket             | SSE (Server-Sent Events)    | HTTP/2 Push (deprecated)     |
|---------------------|-----------------------|-----------------------------|------------------------------|
| Direction           | Bidirectional         | Server → Client only        | Server → Client only         |
| Protocol            | Custom framing        | HTTP/1.1 chunked / HTTP/2   | HTTP/2                       |
| API (browser)       | `WebSocket`           | `EventSource`               | Preload hint (passive)       |
| Auto-reconnect      | Manual                | Built-in                    | N/A                          |
| Proxy-friendly      | Often not (port 80/443) | Yes (pure HTTP)           | Yes (pure HTTP/2)            |
| Use case            | Chat, games, collab   | Live feeds, notifications   | Asset push (mostly removed)  |
| Firewall issues     | Sometimes             | Rarely                      | Rarely                       |

### Scaling WebSockets

WebSocket connections are long-lived and stateful. Horizontal scaling requires:
1. Sticky sessions (route same client to same server) — fragile
2. Pub/sub backend (Redis, Kafka, NATS) — each server subscribes, message broadcast to correct server
3. Managed services: Azure Web PubSub, Pusher, Ably, Soketi

Load balancers need to be configured for WebSocket: long timeout, no connection reuse to backend, handle Upgrade headers.

---

## 7. gRPC

### Wire Format

```
gRPC Call Flow:
─────────────────────────────────────────────────────────────────────
Client Stub                              Server Stub
  │                                          │
  │  Method: UserService.GetUser(userId=42)  │
  │  Serialized as Protobuf binary:          │
  │  field 1 (user_id, varint): 42           │
  │  → byte sequence: 0x08 0x2A              │
  │                                          │
  │── HTTP/2 HEADERS frame ─────────────────►│
  │   :method = POST                         │
  │   :path = /UserService/GetUser           │
  │   :scheme = https                        │
  │   :authority = api.example.com           │
  │   content-type = application/grpc        │
  │   grpc-timeout = 5S                      │
  │                                          │
  │── HTTP/2 DATA frame ────────────────────►│
  │   [0x00]        ← compression flag       │
  │   [0x00 0x00 0x00 0x02]  ← message length│
  │   [0x08 0x2A]   ← protobuf-encoded body  │
  │                                          │
  │◄─ HTTP/2 DATA frame (response) ──────────│
  │   [0x00][length][protobuf response]      │
  │                                          │
  │◄─ HTTP/2 HEADERS frame (trailers) ───────│
  │   grpc-status = 0                        │
  │   grpc-message = ""                      │
```

Status and error details are in HTTP/2 **trailers** (HEADERS frame with END_STREAM), not the HTTP status line. The HTTP status is always 200 for gRPC responses (as long as the transport worked). Check `grpc-status`, not HTTP status.

### Streaming Modes

| Mode                  | Direction                  | Use Case                                 |
|-----------------------|----------------------------|------------------------------------------|
| Unary                 | 1 request → 1 response     | Standard RPC (like REST)                 |
| Server streaming      | 1 request → N responses    | Live feed, large result set pagination   |
| Client streaming      | N requests → 1 response    | Chunked upload, sensor batching          |
| Bidirectional streaming | N requests ↔ N responses  | Chat, collaborative editing, game state  |

### Protobuf Wire Format

Field encoding: `(field_number << 3) | wire_type`

| Wire Type | Meaning                | Used For                         |
|-----------|------------------------|----------------------------------|
| 0         | Varint                 | int32, int64, bool, enum         |
| 1         | 64-bit                 | fixed64, double                  |
| 2         | Length-delimited       | string, bytes, embedded message  |
| 5         | 32-bit                 | fixed32, float                   |

Varint encoding: use 7 bits per byte, MSB = 1 if more bytes follow.
Value 300 = `0b100101100` → two bytes: `0b10101100 0b00000010` = `0xAC 0x02`

No field names on the wire — only field numbers. Schema (`.proto` file) maps numbers to names. Adding a new optional field with a new number is backward-compatible.

### gRPC Status Codes

| Code | Name              | Meaning                                        |
|------|-------------------|------------------------------------------------|
| 0    | OK                | Success                                        |
| 1    | CANCELLED         | Client cancelled the call                      |
| 2    | UNKNOWN           | Unknown server error                           |
| 3    | INVALID_ARGUMENT  | Bad request data                               |
| 4    | DEADLINE_EXCEEDED | Timeout expired                                |
| 5    | NOT_FOUND         | Resource not found                             |
| 6    | ALREADY_EXISTS    | Resource already exists                        |
| 7    | PERMISSION_DENIED | Auth OK but no permission                      |
| 8    | RESOURCE_EXHAUSTED | Quota exceeded, rate limited                   |
| 9    | FAILED_PRECONDITION | System not in state to execute (e.g., not empty) |
| 10   | ABORTED           | Concurrency conflict (compare-and-set failed)  |
| 11   | OUT_OF_RANGE      | Beyond valid range                             |
| 12   | UNIMPLEMENTED     | Method not implemented                         |
| 13   | INTERNAL          | Internal invariant violated                    |
| 14   | UNAVAILABLE       | Server not available (retry-able)              |
| 15   | DATA_LOSS         | Unrecoverable data loss                        |
| 16   | UNAUTHENTICATED   | No valid auth credentials                      |

### gRPC vs REST

| Dimension          | gRPC                               | REST/JSON                             |
|--------------------|------------------------------------|---------------------------------------|
| Transport          | HTTP/2 only                        | HTTP/1.1, HTTP/2, HTTP/3              |
| Encoding           | Protobuf (binary)                  | JSON (text)                           |
| Schema             | Required (.proto)                  | Optional (OpenAPI)                    |
| Code gen           | First-class, multi-language        | Optional (openapi-generator)          |
| Streaming          | Built-in, 4 modes                  | SSE, WebSocket (different protocol)   |
| Browser support    | Needs gRPC-Web proxy               | Native                                |
| Observability      | Status in trailers (non-standard)  | HTTP status codes (universal)         |
| Versioning         | Proto field numbers (append-only)  | URL versioning / Accept header        |
| Human-readable     | No (binary)                        | Yes (JSON)                            |
| Performance        | ~5–10× smaller payload, lower CPU  | Larger payload, higher CPU (JSON)     |

**Deadlines vs timeouts**: A deadline is an absolute point in time (`context.WithDeadline`). A timeout is a duration (`context.WithTimeout`). gRPC propagates deadlines across service calls — the deadline for the upstream call minus elapsed time is set as the deadline for downstream calls. If the original deadline expires, all in-flight child calls are cancelled.

**gRPC-Web**: Browsers can't use raw HTTP/2 trailers (Fetch API doesn't expose them). gRPC-Web encodes trailers as a special DATA frame. Requires a proxy (Envoy, nginx plugin) on the server side to translate. gRPC-Web-Text uses base64 for environments that can't handle binary.

### Interceptors

Server-side and client-side middleware. Wraps every RPC call.

```
Client interceptor chain:
  AuthInterceptor(add token) → LoggingInterceptor(log request/response) → actual call

Server interceptor chain:
  LoggingInterceptor(log req) → AuthInterceptor(verify token) → RateLimitInterceptor → handler
```

---

## 8. CDN & Caching

### How a CDN Works

```
                    ┌──────────────────────────────────────────────┐
Client (Paris)      │  CDN                                         │
  │                 │  PoP Paris ──────────── PoP NYC              │
  │──► DNS query   │  PoP London             PoP Tokyo            │
  │◄── 104.18.5.1  │       │                                       │
  │    (Anycast)   │  Origin Shield (optional, one per region)     │
  │                │       │                                       │
  │──► HTTPS ──────►  Edge cache at Paris PoP                      │
  │                │  HIT: serve from cache                        │
  │                │  MISS: forward to origin shield → origin      │
  └────────────────└──────────────────────────────────────────────-┘

Anycast: multiple PoPs share the same IP. BGP routes client to nearest PoP.
GeoDNS: different CNAME/A records returned based on client's geographic location.
Anycast is more resilient (routing adapts to failures); GeoDNS is simpler.
```

### Cache-Control Anatomy

```
Cache-Control: public, max-age=86400, s-maxage=3600, stale-while-revalidate=60

public           → any cache (browser, CDN, proxy) may cache
private          → only browser cache; CDN must not cache
no-cache         → cache may store but MUST revalidate before serving (conditional GET)
no-store         → do not store anywhere (PCI/sensitive data)
max-age=86400    → browser cache for 86400 seconds (1 day)
s-maxage=3600    → CDN cache for 3600 seconds (overrides max-age for shared caches)
stale-while-revalidate=60 → serve stale for 60s while refreshing in background
must-revalidate  → don't serve stale even if origin unreachable (bank balances)
immutable        → asset will never change; skip revalidation (use with content-hash URLs)
```

### Conditional Requests (Revalidation)

```
First request:
  GET /api/users → 200 OK
                   ETag: "v3"
                   Last-Modified: Mon, 01 Jan 2025 00:00:00 GMT
                   Cache-Control: max-age=60

After 60s, cache asks origin:
  GET /api/users
  If-None-Match: "v3"
  If-Modified-Since: Mon, 01 Jan 2025 00:00:00 GMT

Origin: unchanged → 304 Not Modified (no body, save bandwidth)
Origin: changed   → 200 OK with new body + new ETag
```

**ETag vs Last-Modified**: ETags are stronger — they detect content changes even within the same second. Last-Modified has 1-second granularity. Use ETags when possible.

### Cache Invalidation Strategies

| Strategy             | How                                              | Latency       | Notes                              |
|----------------------|--------------------------------------------------|---------------|------------------------------------|
| TTL expiry           | Wait for max-age/s-maxage to expire              | Up to TTL     | Simple, delayed                    |
| URL versioning       | `/app.abc123.js` — hash in filename              | Instant       | Forces new URL = new cache entry   |
| Surrogate keys / Cache tags | Tag resources, purge by tag               | Instant (API) | Cloudflare Cache-Tag, Fastly surrogates |
| CDN purge API        | Explicit API call to invalidate URL/path         | Seconds       | After deploy, purge affected paths |
| Vary-based           | `Vary: Accept-Encoding` creates per-variant entries | N/A         | Can fragment cache badly if overused |

**Origin shield**: An intermediate caching layer between edge PoPs and origin. Without it: 200 edge PoPs each miss → 200 requests to origin. With shield: all PoPs route misses through 1 shield → origin sees 1 request.

### CDN Comparison

| Feature                    | Azure Front Door      | AWS CloudFront        | Cloudflare CDN        |
|----------------------------|-----------------------|-----------------------|-----------------------|
| Network                    | Anycast (Azure backbone) | Anycast             | Anycast (world's largest) |
| WAF                        | Built-in              | AWS WAF (add-on)      | Built-in              |
| DDoS                       | Standard included     | Standard included     | Built-in (Unmetered)  |
| Cache purge                | Yes (path + tag)      | Yes (path)            | Yes (path + tag)      |
| Routing rules              | Rules engine          | CloudFront Functions  | Workers               |
| HTTP/3                     | Yes                   | Yes                   | Yes (early support)   |
| Origin protocol            | HTTP/1.1, HTTP/2      | HTTP/1.1, HTTP/2      | HTTP/1.1, HTTP/2, HTTP/3 |
| Azure integration          | Native                | Via Direct Connect    | Via CNAME             |

---

## 9. Load Balancers

```
                    ┌──────────────────────────────────────────────────┐
                    │                                                  │
Client ────────────►│  L4 Load Balancer                               │
                    │  Sees: TCP/UDP (IP, port)                        │──► Backend 1: 10.0.1.4:8080
                    │  Cannot: inspect HTTP path/headers               │──► Backend 2: 10.0.1.5:8080
                    │  Algorithms: hash(src_ip+dst_ip+ports)           │──► Backend 3: 10.0.1.6:8080
                    │                                                  │
                    │  L7 Load Balancer (Application Gateway, ALB)     │
                    │  Sees: HTTP headers, URL, cookies, TLS SNI       │──► /api/* → API backends
                    │  Can: path routing, host routing, rewrite URL    │──► /static/* → CDN
                    │       header insert, WAF, auth, rate limit       │──► gRPC → gRPC backends
                    └──────────────────────────────────────────────────┘
```

### L4 vs L7

| Dimension             | L4 (Transport)                      | L7 (Application)                       |
|-----------------------|-------------------------------------|----------------------------------------|
| OSI layer             | 4 — TCP/UDP                         | 7 — HTTP, gRPC, WebSocket              |
| Visibility            | IP addresses, ports                  | Headers, URLs, cookies, body           |
| TLS                   | Pass-through only                   | Can terminate TLS, inspect plaintext   |
| Routing               | IP/port hash, round-robin            | Path, host, header, content-type       |
| Performance           | Very fast (kernel bypass possible)   | Slower (parse HTTP, stateful)          |
| Azure product         | Azure Load Balancer                 | Azure Application Gateway, Front Door  |
| AWS product           | NLB (Network Load Balancer)         | ALB (Application Load Balancer)        |
| Use case              | Database clusters, raw TCP, UDP      | HTTP/HTTPS APIs, WebSockets, gRPC      |

### Load Balancing Algorithms

| Algorithm             | How                                                             | Best For                            |
|-----------------------|-----------------------------------------------------------------|-------------------------------------|
| Round-robin           | Each request to next backend in order                           | Homogeneous backends, equal request cost |
| Weighted round-robin  | More requests to higher-weight backends                         | Mixed capacity backends             |
| Least connections     | Route to backend with fewest active connections                 | Variable request duration           |
| IP hash               | hash(client_ip) % backends = backend index                      | Soft session affinity               |
| Consistent hashing    | Ring topology, hash both backends and requests                  | Cache sharding, minimize redistribution |
| Random                | Random backend selection                                        | Simple, stateless, works well at scale |
| Resource-based        | Route based on backend CPU/memory (L7 only)                     | Heterogeneous load                  |

### Consistent Hashing

```
Virtual ring (0 to 2^32-1):
     0
   /   \
 3B     1B
  \   /
   2B

Backend A maps to positions: 100, 700, 1500, 2400 (virtual nodes)
Backend B maps to positions: 300, 900, 1800, 2800
Backend C maps to positions: 500, 1100, 2000, 3200

Request hashes to 850 → find next clockwise position → 900 (Backend B)
```

When a backend is added/removed, only the keys between the removed backend and its predecessor migrate. Without consistent hashing, removing 1 of N backends reshuffles ~(N-1)/N keys. With consistent hashing: ~1/N keys move.

Virtual nodes (vnodes): each physical backend gets K positions on the ring. Distributes load more evenly. Without vnodes, unequal spacing → unequal load.

### Health Checks

| Type              | What It Checks                                          | Overhead  |
|-------------------|---------------------------------------------------------|-----------|
| TCP probe         | Port accepts connection                                 | Low       |
| HTTP probe        | GET /health returns 200                                 | Medium    |
| HTTP probe (body) | GET /health returns 200 + specific body                 | Medium    |
| Custom script     | Shell script returns 0                                  | Higher    |
| gRPC health       | Calls `grpc.health.v1.Health/Check` returns SERVING     | Medium    |

Connection draining: when removing a backend from rotation, stop sending new connections but allow in-flight requests to complete. Grace period typically 30–60 seconds. Without draining, in-flight requests return 503.

### Sticky Sessions (Session Affinity)

| Method            | How                                                    | Limitation                             |
|-------------------|--------------------------------------------------------|----------------------------------------|
| Cookie-based      | LB sets cookie (AWSALB, ApplicationGatewayAffinity)   | Requires L7 LB; cookie can be cleared  |
| IP hash           | hash(src_ip) → same backend                            | CGNAT: many clients look like same IP  |
| Application-level | App generates session token, LB reads it               | Requires app cooperation               |

**Prefer stateless over sticky**: Sticky sessions create uneven load and complicate deploys. Better: store session state in Redis/database and let any backend serve any request.

---

## 10. Reverse Proxy Patterns

### nginx Configuration

```nginx
upstream api_backends {
    keepalive 32;           # keep 32 idle connections to each upstream
    server 10.0.1.4:8080;
    server 10.0.1.5:8080;
    server 10.0.1.6:8080;
}

server {
    listen 443 ssl http2;
    server_name api.example.com;

    ssl_certificate /etc/nginx/certs/fullchain.pem;
    ssl_certificate_key /etc/nginx/certs/privkey.pem;

    location /api/ {
        proxy_pass http://api_backends;
        proxy_http_version 1.1;
        proxy_set_header Connection "";       # enable keepalive to upstream
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
        proxy_read_timeout 30s;
        proxy_connect_timeout 5s;
    }
}
```

`X-Forwarded-For`: appends client IP to existing header. Value can be spoofed by client — only trust rightmost IPs added by your own infrastructure. Use `RemoteAddr` (or nginx's `$remote_addr`) for the immediately connecting IP.

### Envoy

Envoy (CNCF) is the data plane of service meshes (Istio uses Envoy sidecars). Configured via xDS APIs (Listener Discovery Service, Cluster Discovery Service, Route Discovery Service, Endpoint Discovery Service). Dynamic configuration — no restart needed.

```
xDS Control Plane (Istio Pilot / Consul / custom)
      │
      │  xDS APIs (gRPC streaming)
      ▼
Envoy sidecar (each pod)
  ├── Listener: :15001 (outbound), :15006 (inbound)
  ├── Routes: /api/users → cluster:user-service
  ├── Clusters: user-service → [10.0.1.4:8080, 10.0.1.5:8080]
  └── Endpoints: health-checked, weighted
```

Envoy handles: retries, circuit breaking, timeouts, TLS origination, mTLS, observability (metrics, tracing), rate limiting. Configuration via Kubernetes CRDs (VirtualService, DestinationRule) in Istio.

### Caddy

```
api.example.com {
    reverse_proxy localhost:8080
    # automatic TLS via ACME (Let's Encrypt) — no cert config needed
}
```

Caddy manages ACME certificate lifecycle automatically. Handles HTTP-01 and TLS-ALPN-01 challenges, auto-renewal, OCSP stapling. Significantly simpler than nginx for TLS.

---

## 11. Network Security

### Firewalls: Stateful vs Stateless

**Stateless**: Filter individual packets based on rules (source IP, destination IP, port, protocol). No memory of connection state. Cannot distinguish a legitimate ACK from a spoofed one.

**Stateful**: Track connection state table. An incoming packet is only allowed if it belongs to an established or related connection initiated from the allowed direction. Azure NSGs are stateful — allowing outbound TCP:443 automatically allows the return traffic.

### Azure NSG Rules

```
Priority  Name              Port    Protocol  Source         Destination  Action
100       Allow-HTTPS-in    443     TCP       Internet       VNet         Allow
200       Allow-HTTP-in     80      TCP       Internet       VNet         Allow  ← for redirect
300       Allow-SSH-in      22      TCP       CorpNetwork    VNet         Allow
65000     AllowVnetInBound  Any     Any       VirtualNetwork VNet         Allow  ← default
65500     DenyAllInBound    Any     Any       Any            Any          Deny   ← default
```

Lower priority number = higher priority. Rules evaluated in priority order. First match wins.
NSG can be applied to subnet (affects all resources in subnet) or NIC (affects individual VM).

### Zero Trust — Network Layer

```
Traditional perimeter model (1990s–2010s):
  ┌──────────────────────────────────┐
  │  VNet / Corporate Network        │
  │  All traffic inside = trusted    │
  │  One firewall at the edge        │
  └──────────────────────────────────┘
  Breach the perimeter → lateral movement free

Zero trust network model:
  Every workload is its own security boundary
  Traffic between workloads is authenticated + encrypted
  No implicit trust based on network location
```

**Microsegmentation with NSGs as micro-perimeters**: Rather than one VNet-wide NSG, each subnet (or NIC) has its own NSG with explicit allow rules. VM A in subnet A cannot reach VM B in subnet B unless there is an explicit rule permitting it. Azure Application Security Groups (ASGs) let you group VMs by role (e.g., "web-tier", "db-tier") and write NSG rules against ASG names rather than IP ranges — rules survive VM IP changes.

```
ASG: web-tier   → NSG rule: web-tier → db-tier on port 5432 ALLOW
ASG: db-tier    → NSG rule: db-tier  → * DENY (no outbound except response)
Rule: * → db-tier on port 5432 DENY (only web-tier can reach DB)
```

**Azure Private Endpoints (Private Link)**: Azure PaaS services (Key Vault, Storage, SQL, Service Bus) get a private NIC inside your VNet with a private IP. Traffic from VMs to these services never leaves the Azure backbone — it never touches the public internet. The public endpoint can be disabled entirely.

```
Without Private Endpoint:
  VM (10.0.1.10) → public IP → storage.blob.core.windows.net
  [traverses internet or at minimum Microsoft's public network edge]

With Private Endpoint:
  VM (10.0.1.10) → 10.0.1.50 (private NIC in VNet) → Azure Storage
  [stays on Azure backbone; public access disabled]
```

Private DNS zone (`privatelink.blob.core.windows.net`) overrides public DNS to return the private IP. Link the private zone to the VNet — resolution is automatic.

**Azure Firewall Premium**: beyond basic NSG rules, Azure Firewall Premium adds:
- IDPS (Intrusion Detection and Prevention System): signature-based detection of known attack patterns
- TLS inspection: decrypt TLS traffic to inspect content (requires deploying a custom CA cert to workloads)
- FQDN filtering: allow/deny by fully qualified domain name (not just IP)
- Web categories: block social media, gambling, etc. by category

Use Azure Firewall in the hub VNet of a hub-and-spoke topology. NSGs for micro-perimeters within spokes; Firewall for egress policy and inspection.

**Just-in-Time (JIT) VM access (PIM for network)**: Azure Defender for Cloud's JIT access locks down management ports (SSH/22, RDP/3389) by default — NSG rules deny all inbound. When access is needed, engineer requests JIT activation for specific port + source IP + time window. Defender for Cloud creates a temporary NSG rule, records the approval, auto-expires after the window.

```
Without JIT:                          With JIT:
NSG: SSH from Internet ALLOW          NSG: SSH from Internet DENY (always)
[exposed 24/7; bots scan within min]  [request JIT → 2hr window → auto-close]
```

**Conditional Access for workloads**: Entra ID Conditional Access policies can now gate access to Azure resources based on device compliance, sign-in risk, and IP location — not just user sign-in. This applies the same identity-aware zero-trust controls to workload access that BeyondCorp applies to user access.

### VPN Types

| Type                  | Protocol           | Use Case                                          |
|-----------------------|--------------------|---------------------------------------------------|
| Site-to-site          | IPsec/IKEv2        | On-prem datacenter ↔ Azure VNet                  |
| Point-to-site         | SSTP, OpenVPN, IKEv2 | Individual developer → Azure VNet               |
| WireGuard             | WireGuard (UDP)    | Modern, fast, simple config, 4096-byte codebase  |
| Azure ExpressRoute    | MPLS/BGP           | Private, dedicated circuit, not over internet    |

WireGuard advantages over OpenVPN: stateless cryptography (ChaCha20-Poly1305 + Curve25519), ~1/50th the codebase, faster handshake, reconnects instantly on IP change.

### Rate Limiting Algorithms

**Token bucket**: Bucket holds capacity C tokens. Tokens added at rate R/second. Each request consumes 1 token. If bucket empty, request rejected. Allows burst up to C.

```
Bucket capacity: 100  Rate: 10/sec
Time 0:   100 tokens, 100 requests arrive → 100 served, 0 left
Time 1s:  10 tokens added, 10 requests → served
Time 2s:  10 tokens, 5 requests → 5 served, 5 tokens left
```

**Leaky bucket**: Queue of fixed size. Requests processed at constant rate. Overfull queue = drop/reject. Smoothes bursts (unlike token bucket which allows bursts).

**Fixed window**: Count requests per time window (per minute). Simple but susceptible to boundary attacks: 100 requests at 12:00:59, 100 more at 12:01:01 = 200 in 2 seconds.

**Sliding window log**: Track exact timestamps of recent requests. Accurate but memory-intensive.

**Sliding window counter**: Weighted average of current and previous window. Approximation of sliding window log, constant memory.

---

## 12. Ports & Protocols Reference

| Port     | Protocol     | Notes                                                         |
|----------|--------------|---------------------------------------------------------------|
| 20/21    | FTP          | 21=control, 20=data. Plain text. Avoid — use SFTP (SSH)      |
| 22       | SSH / SFTP   | Secure shell, secure file transfer                           |
| 25       | SMTP         | Server-to-server email. Often blocked by ISPs                |
| 53       | DNS          | UDP (queries), TCP (zone transfers, responses >512B)         |
| 67/68    | DHCP         | 67=server, 68=client. UDP broadcast                          |
| 80       | HTTP         | Typically redirects to 443                                   |
| 110      | POP3         | Email retrieval (legacy). Prefer IMAP/993                    |
| 123      | NTP          | Network Time Protocol. UDP                                   |
| 143/993  | IMAP         | 143=plaintext, 993=IMAPS (TLS)                               |
| 443      | HTTPS        | HTTP over TLS 1.3. Also HTTP/2, HTTP/3 via ALPN             |
| 465/587  | SMTP (TLS)   | 465=SMTPS, 587=Submission (STARTTLS). For sending email      |
| 853      | DNS over TLS | DoT. RFC 7858                                                |
| 3306     | MySQL        | MySQL / MariaDB                                              |
| 3389     | RDP          | Windows Remote Desktop Protocol                              |
| 5432     | PostgreSQL   | PostgreSQL wire protocol                                     |
| 5671/5672 | AMQP         | RabbitMQ. 5671=TLS, 5672=plain                              |
| 6379     | Redis        | Redis. No TLS by default — use TLS or TLS proxy              |
| 6443     | Kubernetes   | Kubernetes API server                                        |
| 8080     | HTTP alt     | Dev convention, HTTP without TLS                             |
| 8443     | HTTPS alt    | Dev convention, HTTPS on non-standard port                   |
| 9090     | Prometheus   | Prometheus HTTP API                                          |
| 9092     | Kafka        | Kafka broker plaintext                                       |
| 9200     | Elasticsearch | REST API                                                     |
| 10250    | kubelet      | Kubernetes kubelet API (node agent)                          |
| 27017    | MongoDB      | MongoDB wire protocol                                        |
| 50051    | gRPC         | gRPC convention (not standard, just common)                  |

---

## 13. Old World → New World Bridge

| Old World                          | New World                                     | Notes                                              |
|------------------------------------|-----------------------------------------------|----------------------------------------------------|
| WCF BasicHttpBinding               | REST over HTTPS/1.1 or HTTP/2                 | Text/XML → JSON, similar request/response model    |
| WCF NetTcpBinding                  | gRPC over HTTP/2                              | Binary, multiplexed, TLS, Protobuf ≈ WCF BinEnc   |
| WCF WSHttpBinding                  | OpenID Connect / OAuth2 + REST                | WS-Security → JWT Bearer tokens                   |
| ISAPI filters / HTTP Modules       | ASP.NET Core Middleware pipeline              | IMiddleware with RequestDelegate chain             |
| WCF service reference + proxy gen  | `grpc_tools` / openapi-generator             | Same concept: schema → generated client            |
| Hardware LB (F5 BIG-IP, NetScaler) | Azure Application Gateway / Azure Front Door  | F5 iRules → AG routing rules; same L7 concepts    |
| Windows Server NLB                 | Azure Load Balancer (L4)                      | L4 hash-based; Azure LB uses 5-tuple hash         |
| On-prem DNS / Active Directory DNS | Azure Private DNS + Azure DNS                 | Private zones linked to VNets = split-horizon      |
| HOSTS file                         | CoreDNS in Kubernetes                         | ConfigMap-based DNS overrides per namespace        |
| VPN Concentrator                   | Azure VPN Gateway / ExpressRoute              | ExpressRoute = dedicated circuit (no internet)     |
| SSL cert from Verisign (expensive, annual) | Let's Encrypt (free, 90-day auto-renew) | ACME protocol, Caddy/Certbot automates renewal |
| IIS SSL termination                | Azure Application Gateway / nginx             | Same concept: offload TLS, forward HTTP to backend |
| HTTPS via IIS + ARR                | nginx/Caddy/Envoy reverse proxy               | ARR = Application Request Routing, same pattern   |
| Windows Firewall rules             | Azure NSG rules (inbound/outbound)            | Priority-ordered allow/deny with stateful tracking |
| IPsec tunnel to branch office      | Azure VPN Gateway (site-to-site IPsec/IKEv2)  | Same IPsec/IKEv2 under the hood                   |
| SCOM network monitoring            | Azure Monitor + Network Watcher               | Packet capture, connection monitor, NSG flow logs  |
| WCF client-cert auth               | mTLS (mutual TLS)                             | X.509 client certs, same concept                  |

---

## 14. Decision Cheat Sheet

| Scenario                                              | Solution                                             |
|-------------------------------------------------------|------------------------------------------------------|
| Browser ↔ server realtime bidirectional               | WebSocket                                            |
| Browser ↔ server server-push only (notifications)    | SSE (EventSource) — simpler, auto-reconnect          |
| Internal service ↔ service (typed RPC, high perf)    | gRPC + Protobuf over HTTP/2                          |
| Public REST API, browser clients                      | HTTPS/2 (TLS + ALPN negotiates HTTP/2)               |
| Maximum performance, mobile clients                   | HTTP/3 / QUIC (CDN support required)                 |
| Large file download/upload                            | HTTP/1.1 with Range requests or chunked encoding     |
| High-frequency IoT telemetry                          | MQTT (pub/sub, tiny overhead) or UDP + custom        |
| Microservice traffic encryption + identity            | mTLS via service mesh (Istio/Linkerd)                |
| Client auth without shared secrets                    | Client certificates (mTLS)                           |
| Cache static assets at edge globally                  | CDN with `immutable` + content-hash URLs             |
| Global L7 routing + WAF + DDoS protection             | Azure Front Door / AWS CloudFront with WAF           |
| Session-aware load balancing                          | L7 LB with cookie-based session affinity             |
| Stateless microservice load balancing                 | L4 LB or L7 round-robin; design statelessness in    |
| Internal service not publicly exposed                 | Private Endpoint (Azure Private Link)                |
| Connect on-prem to Azure (internet-based)             | Azure VPN Gateway (IPsec/IKEv2)                      |
| Connect on-prem to Azure (dedicated private circuit)  | Azure ExpressRoute                                   |
| Automatic TLS for internal services                   | cert-manager (Kubernetes) + Let's Encrypt            |
| DNS for internal Kubernetes services                  | CoreDNS (built-in to Kubernetes)                     |
| Debugging why a request is slow                       | `curl -w "@curl-format.txt"` timing breakdown; Wireshark |
| Rate limiting at edge                                 | CDN/Front Door rate limiting rules; token bucket     |
| Service-to-service auth without passwords             | Workload identity (Managed Identity in Azure)        |
| NSG microsegmentation by role                         | Azure Application Security Groups (ASGs)             |
| Lock management ports, open on demand                 | JIT VM access (Azure Defender for Cloud)             |
| Outbound internet egress policy + IDPS                | Azure Firewall Premium in hub VNet                   |

---

## 15. Common Confusion Points

**`Cache-Control: no-cache` does NOT mean "don't cache"**
It means "you may cache this, but you MUST revalidate with the origin before serving it." The cached copy is stale until the origin confirms it's still valid (304 Not Modified). `no-store` means "don't cache this at all."

**HTTP/2 vs HTTP/3 head-of-line blocking distinction**
HTTP/2 multiplexing fixes application-level HOL blocking (one slow request no longer blocks others at the HTTP layer). But HTTP/2 still runs over TCP — a single lost packet blocks ALL HTTP/2 streams until TCP retransmits it. HTTP/3/QUIC runs streams independently over UDP, so a lost packet only blocks the stream it belongs to. Two different HOL blocking problems at two different layers.

**TLS 1.3 makes RSA key exchange impossible**
In TLS 1.2, you could use RSA to encrypt the session key with the server's public key. This has no forward secrecy — compromise the private key later, decrypt all past sessions. TLS 1.3 eliminates this. All key exchanges are (EC)DHE — ephemeral, forward-secret.

**gRPC status codes ≠ HTTP status codes**
gRPC always returns HTTP 200 at the transport layer (if the RPC completed). The actual result is in the `grpc-status` trailer. An HTTP 200 response from a gRPC endpoint might carry `grpc-status: 5` (NOT_FOUND). Middleware that reads HTTP status codes will misleadingly report success. Use grpc-status for gRPC, not HTTP status.

**DNS TTL is advisory, not enforced**
Resolvers SHOULD respect TTL. They are not required to. Browsers have their own DNS caches. Operating systems cache. Load balancers might cache. Lowering TTL to 60s before a DNS migration is smart, but expect some traffic to the old address for far longer. Set TTL low (60s) at least 24–48 hours before any change.

**WebSockets bypass HTTP caching entirely**
Once the WebSocket upgrade occurs, the connection is no longer HTTP. There is no `Cache-Control` for WebSocket frames. CDNs typically cannot cache WebSocket traffic and just proxy it. Design accordingly — don't rely on caching for WebSocket payloads.

**0-RTT data in QUIC/TLS 1.3 is replay-unsafe**
The 0-RTT early data is encrypted with a session ticket key from a previous session. There's no freshness guarantee — an attacker who captures the 0-RTT datagram can replay it. The server has no way to distinguish a legitimate from a replayed 0-RTT request. Only use 0-RTT for idempotent, read-only operations. Mutation operations should wait for 1-RTT.

**L4 load balancer cannot do path-based routing**
L4 only sees TCP/IP headers (source IP, destination IP, source port, destination port). It cannot inspect the HTTP path `/api/users` vs `/static/app.js`. Path-based routing requires L7 load balancer, which terminates TLS (or reads plaintext) and inspects the HTTP request.

**mTLS ≠ TLS**
Standard TLS authenticates the server to the client via the server's certificate. The client is anonymous (from TLS perspective — application may do its own auth). mTLS adds client certificate authentication — both parties present certs, both verify. The client proves its identity at the transport layer, not the application layer.

**`X-Forwarded-For` can be spoofed**
A client can set `X-Forwarded-For: 1.1.1.1` in its request. The reverse proxy appends the client's real IP to whatever was in the header. If you naively read `X-Forwarded-For` to get the "client IP," an attacker can make themselves appear to come from any address. Trust only the rightmost IP (added by your own proxy) or use a separate header your own proxy sets from `$remote_addr` (nginx's `X-Real-IP`).

**SNI is sent in plaintext (until ECH)**
The Server Name Indication in the TLS ClientHello reveals the hostname to anyone observing the TLS handshake. Network operators can see which HTTPS sites you're connecting to even without breaking encryption. Encrypted ClientHello (ECH, RFC draft) encrypts SNI, but requires CDN support and is not yet widely deployed.

**gRPC-Web is not gRPC**
Browser fetch/XHR cannot access HTTP/2 trailers, and cannot send cleartext HTTP/2 without ALPN negotiation infrastructure. gRPC-Web is a different protocol that encodes trailers in the body. It requires a proxy (Envoy, nginx gRPC-Web module) to translate to real gRPC. Your server may need explicit gRPC-Web support depending on the framework.

**Consistent hashing with few backends has uneven distribution**
With 3 backends on a ring and no virtual nodes, spacing will be uneven by chance. One backend might cover 50% of the ring, another 30%, another 20%. Virtual nodes (assign each backend K positions on the ring) distribute load evenly. Kubernetes Services use IPVS consistent hashing with configurable virtual nodes.

**BBR is not a silver bullet**
BBR outperforms CUBIC on high-BDP links (high bandwidth, high latency — trans-ocean, satellite). On low-BDP links (LAN, within-datacenter) the difference is negligible. BBR can be unfair to CUBIC flows in mixed environments — CUBIC backs off when it sees loss; BBR does not, so BBR can "steal" bandwidth from CUBIC flows at shared bottlenecks. Google runs BBR on their WAN where they control both ends; in public internet mixed environments, exercise judgment.
