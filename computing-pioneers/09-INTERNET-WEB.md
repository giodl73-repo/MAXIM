# Internet and Web Pioneers — Cerf, Kahn, Berners-Lee, Andreessen, Page, Brin

## Era Overview

```
FROM ARPANET TO THE MODERN WEB: 1969–2000
===========================================

  1969 ─── ARPANET: first packet-switched network.
           4 nodes: UCLA, Stanford, UCSB, Utah.
           First message: "lo" (trying to send "login", crashed after "lo").

  1972 ─── EMAIL invented (Ray Tomlinson — @ sign). First killer app.
           ARPANET demonstrated publicly at ICCC.

  1973 ─── CERF + KAHN: begin designing TCP/IP (Transmission Control Protocol
           / Internet Protocol). Problem: how to connect heterogeneous networks.

  1974 ─── CERF + KAHN: "A Protocol for Packet Network Intercommunication"
           The TCP/IP paper. Defines the internet architecture.

  1983 ─── ARPANET switches from NCP to TCP/IP. "Flag Day" January 1.
           The internet officially begins.

  1989 ─── BERNERS-LEE: "Information Management: A Proposal" — WWW concept.
  1991 ─── BERNERS-LEE: First web server, HTTP, HTML, browser running at CERN.
  1993 ─── ANDREESSEN: Mosaic browser released (NCSA, University of Illinois).
           First browser with inline images. Web goes mainstream.

  1994 ─── BERNERS-LEE founds W3C.
           ANDREESSEN co-founds Netscape.

  1995 ─── Netscape Navigator. IPO. "Netscape moment" — web era begins.
           Java (Sun), JavaScript (Netscape/Brendan Eich).
           Amazon, eBay, Yahoo founded.

  1998 ─── PAGE + BRIN: Google founded. PageRank algorithm.

  1999 ─── Napster. Peer-to-peer. Wifi 802.11b.
  2000 ─── Dot-com crash.

  2004 ─── Facebook. Web 2.0. User-generated content era.
  2004 ─── Firefox (Mozilla) — open source browser challenge.
```

---

## Vint Cerf (1943–present) and Bob Kahn (1938–present)

### Bio Snapshot

**Cerf**: Stanford (mathematics), UCLA (computer science PhD). ARPA, Stanford, MCI, ICANN, Google. "Father of the Internet." Now VP at Google. Turing Award 2004 (shared with Kahn).

**Kahn**: Princeton (mathematics and electrical engineering), MIT (PhD). Bell Labs. ARPA. Founded CNRI (Corporation for National Research Initiatives). Turing Award 2004 (shared with Cerf).

### The Problem: Internetworking

By 1973, there were multiple packet-switched networks with incompatible protocols:

```
THE INTERNETWORKING PROBLEM (1973)
====================================

  Network A (ARPANET): NCP protocol
  Network B (PRNET): Packet Radio Network
  Network C (SATNET): Satellite network

  Problem: a packet from Network A cannot pass to Network C.
           Each network has its own packet format, addressing, error handling.

  Previous approach: design one perfect network.
  Cerf+Kahn's insight: design a protocol that works ACROSS networks,
                       without requiring any network to change.

  DESIGN PRINCIPLES:
  ──────────────────
  1. No central control. Any network can join.
  2. Each network operates independently (no internal changes required).
  3. Best-effort delivery. Routers don't remember packets.
  4. "Black boxes" (later called routers/gateways) connect networks.
  5. Endpoints handle reliability (not the network).
  6. No global addressing — a single address space.
  7. No assumptions about the underlying network type.
```

### TCP/IP Architecture

```
TCP/IP PROTOCOL STACK
========================

  APPLICATION LAYER
  ─────────────────
  HTTP, FTP, SMTP, DNS, SSH, TLS
  Application defines message format.
  TCP/IP is transport — it doesn't care what's in the payload.

  TRANSPORT LAYER
  ───────────────
  TCP: Transmission Control Protocol
    - Reliable, ordered byte stream
    - Connection-oriented (3-way handshake: SYN, SYN-ACK, ACK)
    - Error detection + retransmission
    - Flow control (receiver advertises window size)
    - Congestion control (slow start, AIMD)

  UDP: User Datagram Protocol (added later)
    - Unreliable, unordered
    - No handshake, no retransmission
    - Low overhead (games, video streaming, DNS)

  INTERNET LAYER
  ──────────────
  IP: Internet Protocol
    - Best-effort packet delivery
    - 32-bit addresses (IPv4) / 128-bit addresses (IPv6)
    - Fragmentation and reassembly
    - TTL (Time to Live — prevents infinite loops)
    - Routing: each router forwards based on destination IP

  LINK LAYER
  ──────────
  Ethernet, WiFi, fiber, etc.
  IP doesn't care — "any packet network" was the design goal.
  IP packets are carried inside whatever the physical network uses.

  THE KEY INSIGHT: end-to-end principle
  ──────────────────────────────────────
  Put complexity at the endpoints, not in the network.
  The network delivers packets. Period.
  Reliability, ordering, encryption — the application's problem.
  This is why TCP/IP supports VoIP, HTTP, BitTorrent, WebRTC
  without any changes to the network infrastructure.
```

**IP addressing** (Cerf's specific contribution): The 32-bit IPv4 address space (4.3 billion addresses) was designed when the internet had ~100 nodes. By the mid-1990s, address exhaustion was visible. IPv6 (128-bit, 2^128 addresses — essentially unlimited) was standardized in 1998. IPv6 adoption is still incomplete in 2025, 25+ years later.

**The end-to-end principle** (Saltzer, Reed, Clark, 1984 — formalizing Cerf+Kahn's design): functions that can be implemented correctly only with application participation should not be implemented in the network. This principle is why the internet is general-purpose: adding a new protocol requires no changes to routers — only to endpoints. It is also why internet "neutrality" debates matter: edge-added features (content inspection, QoS prioritization) violate end-to-end.

---

## Tim Berners-Lee (1955–present)

### Bio Snapshot

British computer scientist. Oxford (physics). CERN from 1980. Invented the World Wide Web at CERN in 1989. Founded W3C in 1994. Now at MIT and Oxford. Knighted 2004. Never patented the Web — gave it away freely, a decision that shaped the open internet. Most recently advocating for the Solid decentralized web project.

### The Web Proposal

In March 1989, Berners-Lee submitted a proposal to his CERN management: "Information Management: A Proposal." His manager Mike Sendall wrote on it: "Vague but exciting."

The problem: CERN employed thousands of researchers who came and went. Each brought their own information systems. When they left, institutional knowledge left with them. Berners-Lee wanted a system where information could be linked and accessed without a central database controller.

```
THE WEB'S THREE COMPONENTS (Berners-Lee, 1989–1991)
=====================================================

  URI / URL — Uniform Resource Identifier / Locator
  ──────────────────────────────────────────────────
  A universal naming scheme for any resource.
  http://info.cern.ch/hypertext/WWW/TheProject.html

  scheme://host[:port]/path?query#fragment
  http://     — protocol
  info.cern.ch — hostname (resolved via DNS)
  /hypertext/WWW/TheProject.html — path to resource

  Critical: the namespace is globally distributed.
  No central registry controls what URLs exist under a domain.

  HTTP — HyperText Transfer Protocol
  ────────────────────────────────────
  Request-response protocol.
  Stateless: each request independent.
  Verbs: GET, POST (originally); later PUT, DELETE, PATCH.

  GET /hypertext/WWW/TheProject.html HTTP/1.0
  Host: info.cern.ch

  HTTP/1.0 200 OK
  Content-Type: text/html
  [body follows]

  Statelessness is a design choice (not a limitation):
  Scales horizontally — any server can handle any request.
  Session state managed by cookies (Netscape, 1994) or tokens.

  HTML — HyperText Markup Language
  ──────────────────────────────────
  Markup language for documents with links.
  Derived from SGML.

  <a href="http://other-site.com/document">link text</a>
  The href attribute is the hypertext — the link to another document.

  HTML was intentionally simple: easy to parse, easy to write,
  graceful degradation (unknown tags ignored).
  This permissiveness led to decades of browser quirks.
```

**What Berners-Lee did NOT invent**:
- The internet (Cerf+Kahn, 1974)
- Hypertext (the concept: Bush 1945, Nelson 1965, Engelbart 1968)
- Packet switching (Baran, Davies, independently 1960s)

**What he did**: Combined URL + HTTP + HTML into a practical, deployed system running at CERN in December 1991. And gave it away without patents.

### The Gift to the World

Berners-Lee convinced CERN not to patent the Web in 1993. The technology entered the public domain. Had it been patented:

```
COUNTERFACTUAL: PATENTED WEB
==============================

  Every web server → license fee
  Every browser → license fee
  Every web page → potentially licensed content

  The web would likely have developed as fragmented
  proprietary systems, similar to CompuServe, AOL, MSN
  — walled gardens with incompatible protocols.

  The open web's economic value:
    Estimated at $1–2 trillion/year globally (Deloitte, 2012).
    All of e-commerce, all of search advertising, all of SaaS.
    Berners-Lee captured essentially none of this.

  Compare: Qualcomm's CDMA patents earn ~$7 billion/year.
           Berners-Lee's HTTP patents: $0.
```

---

## Marc Andreessen (1971–present)

### Bio Snapshot

Iowa native. Illinois (computer science). National Center for Supercomputing Applications (NCSA) at University of Illinois. Co-wrote Mosaic browser with Eric Bina (1993). Co-founded Netscape (1994). Co-founded Andreessen Horowitz (a16z) VC firm (2009). Board member at Meta, HP, others.

### Mosaic and the Web's Popularization

```
MOSAIC (1993) — WHY IT MATTERED
=================================

  Before Mosaic:
    Web browsers: text-only. Lynx.
    Images: separate windows, separate downloads.
    Installation: complex. Unix command line.

  Mosaic innovations:
    Inline images — images embedded in pages alongside text.
    Single-click links (not type-a-URL).
    Simple installation on Mac and Windows (not just Unix).
    Support for multiple protocols: HTTP, FTP, Gopher, NNTP.

  Effect:
    Web usage grew 341,634% in 1993.
    A technical curiosity became a mass medium.

  Andreessen's design decision: allow inline images by default.
  Berners-Lee and others argued images should be separate.
  Andreessen's position won — visual web, not document web.
  This decision determined the consumer internet's character.
```

**Netscape Navigator**: Andreessen and Jim Clark founded Mosaic Communications, renamed Netscape. Navigator was the first commercial web browser. The Netscape IPO in August 1995 — the company had no profits — validated the internet as an investment category and triggered the dot-com boom.

Netscape's other contributions: JavaScript (Brendan Eich, 1995 — designed in 10 days), SSL/TLS (encrypted web connections), cookies (session state management). All still foundational to the web.

**The browser wars**: Microsoft responded by shipping Internet Explorer bundled with Windows 95, then 98. By 1999 IE had ~95% market share. Netscape's core technology was open-sourced as Mozilla in 1998. Firefox (2004) emerged from Mozilla and began taking share back. Eventually: Chrome (Google, 2008) dominated.

---

## Larry Page (1973–present) and Sergey Brin (1973–present)

### Bio Snapshot

**Page**: Michigan (computer engineering). Stanford PhD (withdrew to run Google). Former Google CEO. Now Alphabet CEO/board.

**Brin**: Maryland (math + CS). Stanford PhD (withdrew). Pioneered data mining for thesis work. Now works on special projects at Alphabet.

Met at Stanford in 1995. Google founded 1998. IPO 2004.

### PageRank

**The problem with 1990s web search**: Search engines (AltaVista, Excite, Lycos) ranked results by keyword frequency in the page's text. This was easily gamed and produced low-quality results.

```
THE PAGERANK ALGORITHM
========================

  INSIGHT: A link from page A to page B is a vote for B.
           But not all votes are equal.
           A vote from an authoritative page (one that has many votes)
           counts more than a vote from an obscure page.

  FORMULATION:
    Let PR(A) = PageRank of page A.
    Pages that link to A: p₁, p₂, ..., pₙ.
    Let L(pᵢ) = number of outgoing links from page pᵢ.
    d = damping factor (typically 0.85).

    PR(A) = (1 - d) + d × Σᵢ (PR(pᵢ) / L(pᵢ))

  INTERPRETATION:
    Model a random surfer who:
    - With probability (1-d): jumps to any page at random (teleportation).
    - With probability d: follows a random link from current page.
    PR(A) = fraction of time the random surfer spends on A.

  COMPUTATION:
    Iterative. Start with PR = 1/N for all pages.
    Apply formula repeatedly until convergence.
    The web graph has ~50 billion pages → distributed computation needed.
    This was Google's MapReduce application before MapReduce was named.

  WHY IT WORKS:
    Gaming keyword frequency: easy.
    Gaming the link graph: hard. You need real pages to link to you.
    Authoritative pages (Wikipedia, NYT, .gov) have high PR.
    Their links transfer authority.
    Spam pages have few legitimate inbound links → low PR → buried.
```

**The infrastructure gap**: PageRank required ranking all pages in the web graph before showing any results. AltaVista was already struggling with the scale of the web. Page and Brin built a custom infrastructure:
- Crawlers to download the entire web
- Storage system for the crawled pages and link graph
- Distributed computation to run PageRank across the graph
- Fast index serving for query time

This infrastructure work became the foundation for MapReduce (2004), BigTable (2006), and the Google File System (2003) — papers that drove the "big data" era.

**Google's business model**: PageRank gave relevance. The business model came from AdWords (2000) — text ads shown alongside search results, priced by cost-per-click. This model (relevance + targeted advertising) generated more revenue than anyone anticipated and funded Google's broader infrastructure ambitions.

---

## Comparison Table

| Figure | Key Contribution | Year | Impact |
|--------|-----------------|------|--------|
| Cerf + Kahn | TCP/IP protocol | 1974 | The internet's plumbing |
| Berners-Lee | HTTP + HTML + URL (WWW) | 1989–1991 | The Web as application layer on the internet |
| Andreessen | Mosaic browser | 1993 | Web goes visual, goes mainstream |
| Page + Brin | PageRank, Google | 1998 | Web becomes findable; search as infrastructure |

---

## Who to Cite for What

| Concept | Figure |
|---------|--------|
| TCP/IP design | Cerf + Kahn (1974) |
| End-to-end principle | Saltzer, Reed, Clark (1984) — formalized from Cerf+Kahn |
| HTTP protocol | Berners-Lee (1991) |
| HTML markup | Berners-Lee (1991) |
| URL/URI scheme | Berners-Lee (1991) |
| Web given to public domain | Berners-Lee (CERN, 1993) |
| Inline images in web browser | Andreessen (Mosaic, 1993) |
| JavaScript | Brendan Eich (Netscape, 1995) |
| SSL/TLS (original) | Netscape (1995) |
| PageRank | Page + Brin (1998) |
| MapReduce (concept) | Dean + Ghemawat (Google, 2004 paper) |

---

## Common Confusion Points

**"Berners-Lee invented the internet."**
He invented the Web. The internet (TCP/IP, ARPANET) predates the Web by 15+ years. The Web is an application layer built on top of the internet.

**"TCP and IP are the same thing."**
IP (Internet Protocol) handles addressing and routing — gets packets from A to B, best effort, no guarantee. TCP (Transmission Control Protocol) provides reliable ordered delivery — handles acknowledgment, retransmission, ordering, flow control. They are separate protocols that work together. UDP is the alternative transport: same IP addressing, no TCP reliability overhead.

**"Google found pages faster."**
The initial advantage was relevance, not speed. PageRank returned better results than competitors. Speed caught up later. The long-term advantage became the scale of Google's index (crawling more of the web faster) and the ad-targeting business model.

**"Andreessen invented the web browser."**
Berners-Lee wrote the first browser (WorldWideWeb, 1990 — later renamed Nexus) and the first web server on the same NeXT machine. Several text-mode browsers followed (Lynx, 1992). Mosaic was the first graphical browser with inline images and Windows/Mac support — which is what made the web accessible to a mass audience.
