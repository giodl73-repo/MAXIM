---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-DNS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:networking:dns
kind: guide
module: networking
section: networking
title: DNS - Resolution, Record Types, Caching/TTL, DoH/DoT, Anycast
status: source-custody
source_custody: partial
current_path: networking/05-DNS.md
canonical_path: networking/05-DNS.md
backsource_ids: [proof-backfill:networking:05-dns, git-history:networking:05-dns]
concepts: [dns, resolution, record types, ttl, caching, doh, dot, anycast, dnssec]
root_concepts: [dns]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# DNS — Resolution, Record Types, Caching/TTL, DoH/DoT, Anycast

## The Big Picture

DNS (Domain Name System, defined originally in RFC 1034 / RFC 1035, 1987) is the
Internet's distributed naming database. Its one job is to translate
human-memorable **names** into the **addresses** and metadata that lower layers
need: `example.com` → `93.184.216.34`. It is a globally distributed,
hierarchically delegated, aggressively cached key-value store that answers tens
of trillions of queries a day — and it does it with a tree of authority where no
single organization holds the whole database.

```
                       THE DNS HIERARCHY (a delegated tree)
                                  . (root)
                                  |  managed by 13 root server "letters"
                                  |  (a..m), each an ANYCAST cluster
            +---------------------+---------------------+
            |                     |                     |
          .com (TLD)            .org                  .uk
          managed by            managed by            managed by
          a registry            a registry            a registry
            |
        example.com (authoritative zone)
          managed by example's own/hosted nameservers
            |
        +---+---------+-----------+
        |             |           |
      www.          api.         mail.    <- records live in the zone

   DELEGATION: each level only knows WHO to ask next, not the final answer.
   "Ask the root who runs .com; ask .com who runs example.com; ask THEM."
```

The defining property is **delegation**: each level of the tree doesn't hold the
answer, it holds a *referral* to the nameserver one level down. Resolution walks
this tree. And because walking it on every lookup would be catastrophically slow,
the second defining property is **caching** governed by TTLs — most queries never
reach the authoritative servers at all.

> **Bridge — naming layer over an address layer.** DNS is service discovery for
> the Internet: a name resolves to an endpoint, with TTL-based cache invalidation.
> You already know this pattern from service registries — DNS is the original,
> planet-scale, eventually-consistent service-discovery system, and a load
> balancer's VIP (08) is just the modern endpoint it now usually returns.

---

## The Resolution Walk

Two kinds of query exist, and the difference is the heart of how DNS scales. Your
machine sends a **recursive** query to a resolver ("get me the final answer");
the resolver then makes **iterative** queries down the tree ("just tell me who to
ask next").

```
   You: browser wants example.com

   1) STUB RESOLVER (your OS) --recursive--> RECURSIVE RESOLVER
        "give me the A record for example.com" (e.g. your ISP's, or 8.8.8.8)
                                   |
   2) RESOLVER --iterative--> ROOT server
        "who handles .com?"  <-- "ask the .com TLD servers at X"
                                   |
   3) RESOLVER --iterative--> .com TLD server
        "who handles example.com?"  <-- "ask ns1.example.com at Y"
                                   |
   4) RESOLVER --iterative--> AUTHORITATIVE server (ns1.example.com)
        "A record for example.com?"  <-- "93.184.216.34, TTL 3600"
                                   |
   5) RESOLVER caches it (for TTL seconds) and returns it to your stub.

   The next user asking within TTL gets it straight from the cache (step 1 only).
```

```
   RECURSIVE                          ITERATIVE
   =========                          =========
   "do all the work, give me          "just tell me the next
    the final answer"                  server to ask"
   stub -> resolver                    resolver -> root/TLD/auth
   one question, one final answer      many questions, referrals
```

DNS runs over **UDP port 53** by default (one small query, one small reply — the
ideal UDP use case from 03). It falls back to **TCP port 53** when a response is
too large to fit a single datagram (notably zone transfers and large DNSSEC
responses).

---

## Record Types

A DNS zone holds typed records. The ones you actually need:

| Type | Maps name to... | Example / use |
|---|---|---|
| **A** | IPv4 address | `example.com → 93.184.216.34` |
| **AAAA** | IPv6 address | `example.com → 2606:2800:...` |
| **CNAME** | another name (alias) | `www → example.com` (no IP at this name) |
| **MX** | mail server (+ priority) | routes email for the domain |
| **NS** | the zone's authoritative nameservers | the delegation glue |
| **TXT** | arbitrary text | SPF/DKIM (mail auth), domain verification |
| **SOA** | zone metadata (serial, TTLs) | one per zone; "start of authority" |
| **PTR** | IP back to a name (reverse DNS) | `34.216.184.93.in-addr.arpa → example.com` |
| **SRV** | service location (host + port) | service discovery for protocols |
| **CAA** | which CAs may issue certs | ties into PKI (06) |

```
   CNAME GOTCHA: a CNAME cannot coexist with other records at the SAME name,
   and you cannot CNAME the zone apex (example.com itself) per the spec. That's
   why providers invented "ALIAS"/"ANAME"/flattened-CNAME records for apex
   pointing at a load balancer (08).

   www.example.com.   CNAME   lb.provider.net.
   lb.provider.net.   A       203.0.113.10
        (resolution follows the chain to the A record)
```

---

## Caching and TTL

Every record carries a **TTL (Time To Live)** in seconds — how long any cache may
serve it before re-querying. TTL is the single knob that trades *propagation
speed* against *query load* and *resilience*.

```
   THE TTL TRADE-OFF:

   LOW TTL (e.g. 60s)              HIGH TTL (e.g. 86400s / 1 day)
   ================               ==============================
   + changes propagate fast        + far fewer queries, less load
   + good before a migration       + survives an authoritative outage
   - heavy query load               - changes take up to a day to spread
   - more exposed to auth outage    - stale during/after a failover

   CACHE LAYERS (each honors TTL):
     browser cache -> OS stub cache -> recursive resolver cache -> auth
        (closest)                                          (source of truth)
```

The standard operational pattern: **lower the TTL well in advance** of a planned
IP change (so caches expire quickly when you cut over), make the change, then
**raise it back** once stable. Note that DNS is **eventually consistent** —
"propagation" is just the slowest cached TTL expiring. There is no global flush;
you wait out the longest TTL any resolver cached.

> **Bridge — TTL is cache invalidation.** This is the same cache-coherence
> problem you know from CDNs, CPU caches, and distributed reads: a writer changes
> the source of truth, but readers hold copies with their own expiry. DNS chose
> *time-based* (TTL) invalidation over *event-based* (purge) because it can't
> reach every cache on Earth — the classic "cache invalidation is hard" lesson at
> planetary scale.

---

## Anycast: One Address, Many Servers

The root and big resolvers (and CDNs, 08) use **anycast**: the *same* IP address
is announced via BGP (02) from many physical locations simultaneously. Each
client's packets are routed to the **topologically nearest** instance — no
client-side logic, the routing fabric does the load distribution and proximity
selection for free.

```
   ANYCAST: the address 198.51.100.1 is announced from THREE sites via BGP.

         CLIENT in Tokyo ---routes to---> TOKYO instance of 198.51.100.1
         CLIENT in Berlin --routes to---> FRANKFURT instance
         CLIENT in Texas --routes to----> DALLAS instance

   Same IP. BGP picks the closest origin per the routing table. If one site
   dies, BGP withdraws its announcement and clients reroute to the next
   nearest -> automatic failover + load spreading, no DNS change needed.
```

This is *why* the "13 root servers" are not 13 machines but 13 *identities*, each
a globally anycast cluster of hundreds of physical servers. Anycast is the
reason DNS (and modern CDNs) survive enormous load and regional outages. It
reappears as the core CDN/edge mechanism in 08.

---

## Encrypted DNS: DoT and DoH

Classic DNS is **plaintext over UDP/53** — anyone on the path can see (and tamper
with) your queries. Two protocols encrypt it, both using TLS (06):

```
   PLAINTEXT DNS (UDP/53)
     query "example.com" visible to your ISP, Wi-Fi operator, anyone on path.

   DoT — DNS over TLS (RFC 7858)
     +-------------------------------+
     | DNS query wrapped in TLS      |   dedicated port 853 (TCP)
     +-------------------------------+   network operators CAN see it's DNS
     | TLS                           |   (distinct port) but not the content
     +-------------------------------+

   DoH — DNS over HTTPS (RFC 8484)
     +-------------------------------+
     | DNS query as an HTTPS request |   port 443, looks like normal web
     +-------------------------------+   traffic -> harder to block or even
     | HTTPS / TLS                   |   distinguish from other HTTPS
     +-------------------------------+
```

| | DoT | DoH |
|---|---|---|
| RFC | 7858 | 8484 |
| Port | 853 (dedicated) | 443 (shared with HTTPS) |
| Visibility | identifiable as DNS by port | blends into web traffic |
| Favored by | network operators (manageable) | browsers/privacy (unblockable) |

The trade-off is genuinely contested: DoH's privacy (indistinguishable from web
traffic) is exactly what makes it hard for an enterprise or parent to filter —
the same property is a feature or a problem depending on who you are.

---

## DNSSEC: Authenticity, Not Secrecy

A separate concern from DoT/DoH: those encrypt the *transport*; **DNSSEC (DNS
Security Extensions, RFC 4033–4035)** signs the *records* so a resolver can
verify the answer is authentic and unmodified — defending against cache poisoning
and forged responses.

```
   DNSSEC adds a CHAIN OF TRUST down the same delegation tree:

     root signs ".com is delegated, here's .com's key fingerprint (DS)"
        |
     .com signs "example.com delegated, here's its key fingerprint"
        |
     example.com signs each record (RRSIG) with its key (DNSKEY)

   A resolver validates the signatures up to the root's trust anchor.
   -> answers are AUTHENTIC (not forged) but still PLAINTEXT (not secret).
```

Keep the two axes straight: **DoT/DoH = confidentiality** (encrypt the query in
transit); **DNSSEC = authenticity/integrity** (prove the answer is genuine). They
are orthogonal and complementary — and DNSSEC is what makes records like CAA and
DANE trustworthy enough to feed into the PKI story in 06.

> **Bridge — signatures vs. encryption.** This is the same split as in
> cryptography/: a digital signature proves *who* and *unmodified*; encryption
> hides *what*. DNSSEC signs (like code-signing your records); DoH encrypts (like
> TLS your queries). A record can be signed-but-readable, encrypted-but-unsigned,
> both, or neither.

---

## Decision Cheat Sheet

| Need | Answer |
|---|---|
| Name → IPv4 | A record |
| Name → IPv6 | AAAA record |
| Alias one name to another | CNAME (not at the zone apex) |
| Point the apex at a load balancer | ALIAS/ANAME (provider-specific) |
| Route mail | MX records |
| Verify domain / mail auth (SPF, DKIM) | TXT records |
| Restrict which CA can issue certs | CAA record (ties to 06) |
| Fast propagation before a migration | lower the TTL ahead of time |
| Fewer queries, outage resilience | higher TTL |
| Nearest server, auto-failover, one IP | anycast (BGP, 02) |
| Encrypt my DNS queries | DoT (853) or DoH (443) |
| Prove answers aren't forged | DNSSEC (signing, not encryption) |
| One small query/reply | UDP/53; TCP/53 when too big |

---

## Common Confusion Points

### "Recursive vs. iterative — which does my computer do?"

Your computer (the stub resolver) makes a **recursive** request to a resolver:
"do all the work, hand me the final answer." That resolver then makes
**iterative** queries down the tree (root → TLD → authoritative), each returning a
referral to the next server. Your machine almost never walks the tree itself.

### "I changed my DNS record but it's not updating."

You're waiting out the **TTL**. Caches everywhere (browser, OS, every recursive
resolver that asked) hold the old value until its TTL expires — there is no global
flush. This is why you lower the TTL *before* a planned change. DNS is eventually
consistent; "propagation delay" is just the longest cached TTL draining.

### "Does DoH/DoH make DNS secure?"

It makes it **confidential in transit** — your ISP can't read the query. It does
*not* prove the answer is authentic; a malicious resolver can still lie to you.
Authenticity is **DNSSEC's** job (signing records). Encryption and signing are
orthogonal: DoH hides the question, DNSSEC validates the answer.

### "Why can't I put a CNAME on example.com itself?"

The spec forbids a CNAME coexisting with other records at a name, and the zone
apex must carry SOA and NS records — so a literal CNAME there is illegal.
Providers worked around it with synthetic ALIAS/ANAME records that resolve the
target's A/AAAA at query time, letting the apex effectively point at a load
balancer (08).

### "Is anycast a load-balancing trick or a routing trick?"

It's a **routing** trick (BGP, 02) that *produces* load balancing and failover as
side effects. The same IP is announced from many sites; the Internet's routing
naturally sends each client to the nearest one, and withdrawing a sick site's
announcement reroutes traffic automatically. No DNS change, no client logic — the
fabric does it. CDNs (08) lean on this heavily.
