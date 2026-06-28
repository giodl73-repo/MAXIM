---
maxim_schema: maxim.frontmatter.v1
id: maxim:networking:load-balancing-cdn
kind: guide
module: networking
section: networking
title: Load Balancing and CDN - L4 vs L7, Anycast, CDNs, Edge
status: source-custody
source_custody: partial
current_path: networking/08-LOAD-BALANCING-CDN.md
canonical_path: networking/08-LOAD-BALANCING-CDN.md
backsource_ids: [proof-backfill:networking:08-load-balancing-cdn, git-history:networking:08-load-balancing-cdn]
concepts: [load balancing, l4, l7, anycast, cdn, edge, reverse proxy, dsr]
root_concepts: [load balancing]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---

# Load Balancing and CDN — L4 vs L7, Anycast, CDNs, Edge

## The Big Picture

Once a service outgrows one machine, you need two things: a way to **spread
traffic** across many backends (load balancing) and a way to **serve content
close to users** (CDNs / edge). Both are about *indirection* — the client talks
to a stable front (a VIP, a hostname, an anycast IP) and the system steers the
request to one of many real servers behind it, ideally the best one. This guide is
where the lower layers (routing, transport, TLS) get composed into the scaling
patterns you actually deploy.

```
        THE SCALING STACK: from one client to many servers, near and far
   CLIENT
     |
     |  (1) DNS / ANYCAST steers you to the nearest EDGE (05, 02)
     v
   +-------------------+   EDGE / CDN POP (close to the user)
   |  CDN edge cache   |   - serves cached static content directly
   |  + TLS terminate  |   - or forwards a cache MISS toward origin
   +---------+---------+
             |  (2) cache miss -> go to origin region
             v
   +-------------------+   LOAD BALANCER in front of the fleet
   |  L4 or L7 LB / VIP|   - L4: fast, by 5-tuple
   |                   |   - L7: smart, by URL / header / cookie
   +----+----+----+----+
        |    |    |
        v    v    v
     +----++----++----+   BACKEND POOL (the actual servers)
     | s1 || s2 || s3 |   - health-checked, added/removed dynamically
     +----++----++----+
```

Two axes organize the whole field. **Where** the steering happens: globally (DNS
and anycast pick a *region/edge*) vs. locally (a load balancer picks a *server*
within one site). And **how deep** it looks: L4 (fast, by connection 5-tuple) vs.
L7 (smart, by application content). Everything below is those two axes.

> **Bridge — the front door indirection.** A load balancer is a reverse proxy
> with a server-selection policy: a stable virtual endpoint hides a changing pool
> of backends, exactly like a service mesh's virtual service or a Kubernetes
> Service hiding its pods. The VIP is the indirection; the algorithm is the
> policy. You've built this — here's the network-layer vocabulary for it.

---

## L4 vs. L7 Load Balancing

The single most important distinction. An **L4** load balancer steers by the
transport **5-tuple** (03) — it doesn't read the payload, it just forwards
packets/connections fast. An **L7** load balancer **terminates** the connection,
reads the HTTP request, and routes on application content.

```
   L4 LOAD BALANCER (transport layer)
   ==================================
     client --TCP--> [ LB picks a backend by 5-tuple ] --TCP--> backend
     - decides ONCE per connection, by (src/dst IP+port)
     - does NOT read HTTP; can't route by URL or cookie
     - very fast, very high throughput, protocol-agnostic
     - the whole TCP/TLS connection pins to one backend

   L7 LOAD BALANCER (application layer / reverse proxy)
   ====================================================
     client --TLS--> [ LB TERMINATES, reads HTTP, routes ] --(new conn)--> backend
     - decides PER REQUEST, by URL path / Host header / cookie / method
     - can do path routing (/api -> svc-a, /img -> svc-b), sticky sessions,
       header rewrites, retries, rate limiting, WAF
     - must terminate TLS (06) to read the request -> more CPU
```

| | L4 LB | L7 LB |
|---|---|---|
| Operates at | transport (TCP/UDP) | application (HTTP/gRPC) |
| Routes by | 5-tuple | URL, headers, cookies, method |
| Reads payload? | no | yes (terminates the connection) |
| TLS | can pass through | usually terminates (06) |
| Granularity | per connection | per request |
| Cost | low (packet forwarding) | higher (full proxy + crypto) |
| Use for | raw throughput, any protocol | path routing, sticky sessions, WAF |

A common production layout uses **both**: an L4 LB spreads raw connections across a
tier of L7 proxies, which then do content-aware routing to microservices. L4 for
volume, L7 for intelligence.

---

## Balancing Algorithms

How does the LB pick *which* backend? The policy menu:

```
   ROUND ROBIN        next server in rotation. Simple, ignores load.
   LEAST CONNECTIONS  the backend with the fewest active conns. Adapts to
                      uneven request durations.
   WEIGHTED           bigger servers get proportionally more. Heterogeneous
                      fleets.
   IP HASH /          hash the client (or 5-tuple) -> same client always hits
   CONSISTENT HASH    the same backend. Gives session affinity AND minimal
                      reshuffling when the pool changes.
   LATENCY / EWMA     pick the backend with the lowest observed response time.
```

**Consistent hashing** deserves emphasis because it's the one with deep
properties: when you add or remove a backend, only ~1/N of keys remap instead of
*all* of them — critical for cache locality and avoiding a thundering rehash. It's
the same algorithm behind sharded data stores; here it provides **session
affinity** ("sticky sessions") so a client keeps landing on the backend holding
its session state.

```
   HEALTH CHECKS gate the whole thing:
     LB periodically probes each backend (TCP connect, HTTP 200 on /healthz).
     UNHEALTHY -> removed from the pool. HEALTHY again -> re-added.
     This is what turns "a server died" into "users never noticed."
```

> **Bridge — consistent hashing you already know.** This is the same ring you use
> for partitioning a distributed cache or sharded store (distributed-systems/):
> minimal key movement on membership change. A load balancer applies it to *which
> server gets a session* instead of *which node owns a key* — identical math,
> different payload.

---

## Anycast: Global Load Balancing via Routing

The global-scale steering mechanism is **anycast** (introduced in 05): announce
the *same* IP from many sites via BGP (02), and the Internet's routing naturally
delivers each client to the topologically nearest site.

```
   ONE IP (198.51.100.1) announced from many POPs via BGP:

      user (Tokyo)   --routing--> Tokyo POP
      user (London)  --routing--> London POP
      user (NYC)     --routing--> NYC POP

   - proximity: clients hit the nearest edge automatically (lower latency)
   - failover: a POP dies -> withdraw its BGP announcement -> clients reroute
   - DDoS absorption: attack traffic spreads across ALL POPs, not one target
```

Anycast is "load balancing by routing table." It complements DNS-based global
balancing (returning different IPs by client geography) — many CDNs use both: DNS
gets you to the right anycast prefix, anycast gets you to the nearest POP within
it. The beauty is zero client logic and automatic failover; the limitation is
coarse control (you steer by network topology, not by precise server load).

---

## CDNs — Content Delivery Networks

A **CDN** is a globally distributed fleet of caching servers (POPs — Points of
Presence) that sit between users and your origin. The core idea: **serve content
from the edge, close to the user**, so most requests never traverse the long path
to your origin at all.

```
   WITHOUT CDN:                      WITH CDN:
   user (Tokyo) -----long----->      user (Tokyo) --short--> Tokyo POP
                origin (US)                                    | (cache HIT)
                  ^                                            v
            every request crosses                       served locally,
            the ocean -> high latency                   origin untouched

   CACHE HIT  -> POP serves from local cache (fast, origin idle)
   CACHE MISS -> POP fetches from origin once, caches it, serves it,
                 future requests are hits.
```

What CDNs cache and how:

```
   CACHE KEY:        usually the URL (+ some headers / query params)
   FRESHNESS:        governed by HTTP Cache-Control / Expires headers
                     (max-age, s-maxage, no-cache, no-store, immutable)
   STATIC vs DYNAMIC:
     - static assets (images, JS, CSS, video) -> highly cacheable
     - dynamic/personalized -> cache briefly, or not at all, or at the edge
   INVALIDATION:     purge a URL when content changes (event-based), in
                     addition to TTL expiry (time-based) -> same cache-
                     coherence problem as DNS TTL (05).
```

Beyond caching, modern CDNs do far more at the edge: **TLS termination** (06)
close to the user (the handshake's round trips are shorter), **DDoS mitigation**
(anycast absorption + scrubbing), **WAF** (L7 filtering, 07), and increasingly
**edge compute** — running your code in the POP itself.

> **Bridge — cache hierarchy.** A CDN is an L7 read-through cache in front of your
> origin, with the same hit/miss/eviction/invalidation semantics as a CPU cache or
> a Redis tier — just geographically distributed. "Cache-Control: max-age" is TTL;
> "purge" is explicit invalidation; the edge POP is L1, your origin is main
> memory. The hard part, as always, is invalidation.

---

## Edge Compute

The newest layer: instead of only caching static bytes at the edge, run
**application logic** there. The motivation is the same as caching — do the work
close to the user — but applied to computation.

```
   THE GRADIENT from origin toward the user:

   ORIGIN (one region)  --->  REGIONAL  --->  EDGE POP  --->  CLIENT
   full app, database          replicas        edge funcs      browser
   heavy, far                  closer          lightweight,    (last mile)
                                               near, fast

   EDGE FUNCTIONS run at the POP: auth checks, redirects, A/B routing,
   personalization, request rewriting, lightweight APIs. Constrained
   runtime (fast cold start, no big stateful deps) -> close to the user.
```

This is the convergence point of this directory with **cloud-architecture/**: the
edge is where networking (anycast, CDN, TLS termination) meets compute
(serverless functions). The constraint is statelessness and tiny cold-start
budgets; the payoff is single-digit-millisecond latency to the user. State that
can't live at the edge stays in regional or origin tiers — the gradient above.

---

## Putting It Together: A Request's Journey

```
   user types https://shop.example.com/product/42
     |
   (1) DNS resolves to an ANYCAST IP (05, 02)
     |
   (2) BGP routes to the NEAREST CDN POP (anycast)
     |
   (3) POP TERMINATES TLS (06) close to the user
     |
   (4) is /product/42 cached & fresh?
        HIT  -> served from the edge, done. (origin never touched)
        MISS -> forward toward origin region:
                 |
   (5)          ORIGIN-side L4 LB spreads the connection
                 |
   (6)          L7 LB routes /product/* to the product service
                 |
   (7)          health-checked backend in the pool handles it
                 |
   (8)          response flows back, POP caches it per Cache-Control
```

Eight steps, and every one of them is a layer or mechanism from earlier in this
directory — anycast (05), BGP (02), TLS (06), the L4/L7 split, health checks,
caching. Load balancing and CDNs are not new layers; they're the *composition* of
the ones you already have.

---

## Decision Cheat Sheet

| Need | Reach for |
|---|---|
| Raw throughput, any protocol, fast | L4 load balancer |
| Route by URL/path/header, sticky sessions, WAF | L7 load balancer |
| Spread evenly, equal servers | round robin |
| Adapt to uneven request durations | least connections |
| Session affinity + minimal reshuffle on changes | consistent hashing |
| Send users to the nearest site, auto-failover | anycast (BGP) |
| Serve static content fast worldwide | CDN edge caching |
| Shorten the TLS handshake for distant users | terminate TLS at the edge |
| Absorb a DDoS | anycast spread + scrubbing |
| Run logic close to the user | edge compute / edge functions |
| Stop sending a dead server traffic | health checks |
| Cache freshness control | HTTP Cache-Control (max-age, s-maxage) |

---

## Common Confusion Points

### "L4 or L7 load balancer — how do I choose?"

If you need to route by application content (URL path, Host header, cookie) or do
TLS termination, retries, rate limiting, or a WAF, you need **L7** — it terminates
and reads the request. If you just need to spread raw connections fast across
identical backends for any protocol, **L4** is cheaper and faster. Big systems use
both: L4 in front of a tier of L7 proxies.

### "Is anycast the same as a load balancer?"

No — anycast is a **routing** technique (BGP, 02) that distributes traffic across
*sites* by topology and provides automatic failover. A load balancer distributes
across *servers within a site* by an explicit algorithm and health checks. Anycast
is coarse and global; an LB is fine-grained and local. They compose: anycast gets
you to the nearest POP, the LB there picks the backend.

### "A CDN is just a cache, right?"

Caching is the core, but a modern CDN is much more: anycast-based global routing,
edge TLS termination (06), DDoS absorption, an L7 WAF (07), and edge compute. The
cache is the foundation; the platform built on it is the product. And like all
caches, its hardest problem is **invalidation** — purging stale content
everywhere.

### "Why does the CDN serve stale content after I update it?"

Same reason DNS lags (05): the edge holds a cached copy until its freshness
lifetime (`Cache-Control: max-age`) expires, unless you explicitly **purge** it.
TTL is time-based invalidation; purge is event-based. Set short TTLs (or use
versioned/`immutable` URLs) for things that change, and purge on deploy.

### "Where should TLS terminate — edge or origin?"

It's a trade-off (see 06). Terminating at the **edge/LB** shortens the handshake
for distant users and lets the L7 LB read the request to route it — but exposes
plaintext inside your perimeter. **Passthrough** keeps end-to-end encryption but
blinds the LB to L7. Zero-trust shops terminate at the edge and **re-encrypt** with
mTLS internally, getting both proximity and end-to-end secrecy.
