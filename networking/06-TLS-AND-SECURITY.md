---
maxim_schema: maxim.frontmatter.v1
id: maxim:networking:tls-and-security
kind: guide
module: networking
section: networking
title: TLS and Transport Security - TLS 1.3, Certificates, PKI, mTLS
status: source-custody
source_custody: partial
current_path: networking/06-TLS-AND-SECURITY.md
canonical_path: networking/06-TLS-AND-SECURITY.md
backsource_ids: [proof-backfill:networking:06-tls-and-security, git-history:networking:06-tls-and-security]
concepts: [tls, tls 1.3, certificates, pki, mtls, handshake, ecdhe, certificate authority]
root_concepts: [transport security]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---

# TLS and Transport Security — TLS 1.3, Certificates, PKI, mTLS

## The Big Picture

TLS (Transport Layer Security) gives you three guarantees over an otherwise open
transport: **confidentiality** (eavesdroppers see only ciphertext),
**integrity** (tampering is detected), and **authenticity** (you are talking to
the server you think you are, proven by a certificate). It runs as a session
*above* TCP (03) — or fused into QUIC — and it solves the problem that every
lower layer left open: the link (01) can be sniffed, the route (02) can be
hijacked, DNS (05) can be spoofed. TLS is the end-to-end answer: *trust nothing
in the middle; verify the endpoint cryptographically.*

```
                  WHAT TLS ADDS ON TOP OF THE TRANSPORT
   +-------------------------------------------------------------------+
   |  APPLICATION (HTTP)         <- sees plaintext, unaware of TLS      |
   +-------------------------------------------------------------------+
   |  TLS 1.3                                                          |
   |    1) HANDSHAKE: agree on keys + VERIFY the server's certificate  |
   |    2) RECORD:    encrypt + authenticate every byte (AEAD cipher)  |
   +-------------------------------------------------------------------+
   |  TCP (03)                   <- reliable byte stream, but PLAINTEXT|
   +-------------------------------------------------------------------+

   THREE PROPERTIES:
     CONFIDENTIALITY  ->  symmetric AEAD encryption (AES-GCM / ChaCha20)
     INTEGRITY        ->  the same AEAD tag (tampering breaks the tag)
     AUTHENTICITY     ->  X.509 certificate + signature, validated to a CA
```

The architecture is the classic hybrid: an expensive **asymmetric** step
(key exchange + certificate verification) bootstraps a cheap **symmetric**
channel (AEAD encryption of the bulk data). This guide is the *protocol*; the
cryptographic primitives it composes — ECDHE, AES-GCM, signatures — are proven in
**cryptography/**. We use them; that directory derives them.

> **Bridge — authenticated session establishment.** You've built this shape:
> an expensive authentication/authorization step (token issuance, mutual auth)
> followed by a cheap per-request credential. TLS is that pattern at the
> transport boundary — a handshake to establish identity and a session key, then
> fast symmetric crypto for the conversation.

---

## The Hybrid Model: Why Two Kinds of Crypto

```
   ASYMMETRIC (public-key)              SYMMETRIC
   =======================              =========
   - slow, but no shared secret         - fast, but needs a shared secret
     needed in advance                    both sides already have
   - used to: AUTHENTICATE (signatures)  - used to: ENCRYPT the bulk data
     + AGREE on a key (key exchange)
   - ECDHE, RSA, ECDSA, Ed25519          - AES-GCM, ChaCha20-Poly1305

   TLS USES BOTH:
     handshake (asymmetric) ---> derives ---> session key (symmetric)
        "prove who you are, agree           "now encrypt everything
         on a secret over an open wire"      fast with this secret"
```

The deep idea TLS relies on is **Diffie-Hellman key exchange**: two parties can
agree on a shared secret over a *public* channel that an eavesdropper cannot
derive. TLS 1.3 mandates the **ephemeral** elliptic-curve variant (**ECDHE**),
where a fresh key pair is generated per session — which buys **forward secrecy**:
even if the server's long-term private key is later stolen, past recorded sessions
stay secret because their ephemeral keys are already gone.

---

## The TLS 1.3 Handshake

TLS 1.3 (RFC 8446, 2018) is a major simplification over 1.2. The headline: it
reaches an encrypted, authenticated channel in **one round trip (1-RTT)**, and
**0-RTT** on resumption — roughly halving the old handshake latency.

```
   TLS 1.3 — 1-RTT HANDSHAKE
   CLIENT                                            SERVER
     |                                                  |
     | --- ClientHello -------------------------------> |
     |     + supported ciphers                          |
     |     + key_share (client's ephemeral ECDHE pub)   |
     |     + SNI (which hostname I want)                 |
     |                                                  |
     | <-- ServerHello -------------------------------- |
     |     + key_share (server's ephemeral ECDHE pub)   |
     |     + {Certificate}        <- now ENCRYPTED      |
     |     + {CertificateVerify}  <- signs handshake    |
     |     + {Finished}                                 |
     |                                                  |
     |  [both sides now derive the same session keys    |
     |   from the two key_shares -> ECDHE shared secret]|
     |                                                  |
     | --- {Finished} --------------------------------> |
     |                                                  |
     |======== ENCRYPTED APPLICATION DATA ==============|
                         (1 RTT total)
   { } = encrypted under handshake keys.
```

Two things to notice. First, the **certificate is sent encrypted** in TLS 1.3
(unlike 1.2 where it was in the clear) — the server's identity is hidden from
passive observers. Second, the client puts its ECDHE `key_share` in the very
first message, so by the time the server replies, both sides can compute the
shared secret immediately — that's the source of the 1-RTT win.

```
   WHAT TLS 1.3 REMOVED vs 1.2 (all attack-surface reductions):
     - RSA key transport (no forward secrecy)  -> GONE, ECDHE only
     - static/non-ephemeral DH                  -> GONE
     - obsolete ciphers (RC4, 3DES, CBC modes)  -> GONE, AEAD only
     - renegotiation, compression               -> GONE (had exploits)
     - the 2-RTT handshake                      -> now 1-RTT (or 0-RTT)
```

**0-RTT** lets a returning client send application data in its very first flight
using a pre-shared key from a prior session — zero handshake latency. The
trade-off: 0-RTT data is **replayable**, so it must be used only for idempotent
requests (the same caution you'd apply to any at-least-once delivery).

---

## Certificates and X.509

A **certificate** is a signed statement binding a **public key** to an
**identity** (a domain name). The format is **X.509**. It is the answer to "how
do I know this ECDHE public key belongs to the *real* example.com and not an
impostor who hijacked my route?"

```
   AN X.509 CERTIFICATE (the essentials):
   +-----------------------------------------------+
   | Subject:        example.com                   |  who it's for
   | SAN:            example.com, www.example.com  |  Subject Alt Names
   | Public Key:     <the server's public key>     |  the bound key
   | Issuer:         "R3" (an intermediate CA)     |  who vouches
   | Validity:       notBefore .. notAfter         |  expiry window
   | Serial / Ext:   key usage, CT, OCSP info...   |
   |-----------------------------------------------|
   | SIGNATURE by the Issuer's private key         |  <- the trust glue
   +-----------------------------------------------+

   NOTE: modern validation uses the SAN field, NOT the old Subject CN,
   to match the hostname.
```

The certificate is worthless on its own — anyone can generate one claiming to be
example.com. Its value comes entirely from **who signed it**, and that signature
chains up to a **Certificate Authority** your system already trusts.

---

## PKI and the Chain of Trust

**PKI (Public Key Infrastructure)** is the system of CAs, intermediate
certificates, and pre-installed trust anchors that lets a browser decide a
certificate is legitimate. Trust is **transitive up a chain** to a **root CA**
baked into your OS/browser trust store.

```
                THE CHAIN OF TRUST (validated bottom-up)

   ROOT CA  (self-signed; its public key ships IN your OS/browser)
      | signs
      v
   INTERMEDIATE CA  (the root delegates; kept offline for safety)
      | signs
      v
   LEAF CERT  (example.com)  <- the one the server presents

   VALIDATION the client performs:
     1) signature chain valid up to a trusted root?   (math checks out)
     2) not expired? not revoked? (OCSP/CRL)          (still valid)
     3) hostname matches a SAN?                        (right identity)
     4) intended key usage?                            (cert is for TLS)
   ALL must pass, or the connection is refused.
```

Root CAs sign rarely (their keys are kept offline); they delegate to
**intermediate CAs** that issue the day-to-day leaf certs. Your browser ships
~100+ trusted roots; everything else chains to one of them. This is the
foundational trust assumption of the web — and its weakness: **any** trusted CA
can issue a cert for **any** domain, so a single compromised or coerced CA is a
global risk.

Mitigations you should know:
- **Certificate Transparency (CT)**: CAs must log every issued certificate to
  public append-only logs, so a domain owner can detect a rogue cert for their
  name. Browsers require CT proof.
- **Revocation**: **OCSP** (online status check) and **CRLs** (revocation lists)
  let a cert be invalidated before expiry; OCSP stapling lets the server present
  a fresh signed status to avoid a separate client lookup.
- **Let's Encrypt / ACME**: automated, free issuance that made TLS-everywhere
  practical by removing cost and manual steps; short-lived certs (e.g. 90 days)
  reduce the revocation problem by expiring fast.

> **Bridge — a trust hierarchy you've operated.** This is exactly a code-signing
> / certificate hierarchy: a trusted root authority delegates to issuers who sign
> artifacts, and the verifier walks the chain to a pre-trusted anchor. PKI is
> that pattern for *identity on the wire*, and CT is the audit log that makes the
> delegation accountable.

---

## mTLS — Mutual Authentication

Ordinary TLS authenticates only the **server** (the client checks the server's
cert; the server doesn't check the client's). **mTLS (mutual TLS)** adds the
reverse: the *server also* demands and verifies a **client certificate**. Now
both ends prove their identity cryptographically.

```
   ONE-WAY TLS (the web)              mTLS (zero-trust internal)
   ====================              ==========================
   client verifies server cert        BOTH verify each other's cert
   server trusts client later          identity is mutual + cryptographic
   (password, token, cookie)           no shared secret to phish

   server -> presents cert -> client verifies      (same as normal TLS)
   server -> REQUESTS client cert
   client -> presents cert -> server verifies       (the added half)
   -> only then does the channel open
```

mTLS is the backbone of **zero-trust** and **service mesh** architectures
(distributed-systems/, cloud-architecture/): inside a fleet, every service-to-
service call presents a short-lived client cert, so identity is *intrinsic to the
connection* rather than a bearer token that can be replayed or leaked. A sidecar
proxy typically terminates mTLS so application code stays unaware — the same
separation of concerns as TLS termination at a load balancer (08).

> **Bridge — workload identity over bearer tokens.** A bearer token (API key,
> JWT) is "whoever holds it is trusted" — phishable, replayable. An mTLS client
> cert is "prove you hold the matching private key, per connection." It's the
> move from possession-based to proof-based identity, which is exactly why
> zero-trust meshes standardized on it.

---

## TLS Termination: Where Decryption Happens

A practical architecture question: *where* in your stack does the ciphertext
become plaintext? This is **TLS termination**, and it's a recurring design choice
that links straight to load balancing (08).

```
   TERMINATE AT THE EDGE (LB/CDN decrypts, then plaintext inside)
     client --TLS--> [ LB / CDN terminates ] --plaintext--> backends
     + offloads crypto from backends, lets the LB inspect L7 (routing)
     - traffic inside the perimeter is plaintext (or needs re-encryption)

   PASSTHROUGH (LB forwards ciphertext; backend terminates)
     client --TLS--------------(opaque)-------------> [ backend terminates ]
     + true end-to-end encryption; LB can't read it (L4 only)
     - LB can't do L7 routing or inspect content

   RE-ENCRYPT / mTLS MESH (terminate at edge, then mTLS internally)
     client --TLS--> [ edge ] --mTLS--> services    (best of both, more cost)
```

The trade-off is **inspectability vs. end-to-end secrecy**: terminating at the
edge lets an L7 load balancer (08) route on the URL/headers but exposes plaintext
inside the perimeter; passthrough keeps it encrypted end-to-end but blinds the
middle to L4. Zero-trust shops increasingly re-encrypt with mTLS so the middle is
both useful *and* never sees cleartext on the wire.

---

## Decision Cheat Sheet

| Need | Answer |
|---|---|
| Encrypt + authenticate a TCP connection | TLS 1.3 |
| Lowest handshake latency | TLS 1.3 (1-RTT), 0-RTT on resume (idempotent only) |
| Past sessions safe if key later stolen | forward secrecy → ECDHE (mandatory in 1.3) |
| Prove the server's identity | X.509 cert validated to a trusted root CA |
| Prove the *client's* identity too | mTLS (client certificate) |
| Service-to-service auth in a mesh | mTLS with short-lived certs |
| Free, automated certificates | ACME / Let's Encrypt |
| Detect a rogue cert for your domain | Certificate Transparency logs |
| Restrict which CA may issue your cert | CAA DNS record (05) |
| LB needs to route on URL/headers | terminate TLS at the edge (08) |
| Never expose plaintext in the middle | passthrough or re-encrypt/mTLS |

---

## Common Confusion Points

### "TLS or SSL — what's the difference?"

SSL is the obsolete predecessor; SSL 2.0 and 3.0 are both broken and disabled
everywhere. The modern protocol is **TLS**, and you should be on **TLS 1.3** (or
1.2 at minimum). People still say "SSL certificate" out of habit, but the protocol
is TLS. There is no "SSL" worth running today.

### "Does the certificate encrypt my traffic?"

No. The certificate only **authenticates** identity — it binds a public key to a
domain via a CA signature. The actual encryption uses a **symmetric** session key
derived from the **ECDHE** key exchange during the handshake. Cert = identity;
session key = secrecy. Two different jobs.

### "What is forward secrecy and why does it matter?"

With forward secrecy, each session uses a fresh **ephemeral** key (ECDHE) that's
discarded afterward. So if an attacker records your encrypted traffic today and
steals the server's long-term private key *next year*, they still can't decrypt
the old sessions — the ephemeral keys are gone. TLS 1.3 makes this mandatory; old
RSA key-transport (no forward secrecy) was removed.

### "If any CA can sign any domain, isn't PKI fundamentally weak?"

It's a real weakness — a single compromised or coerced CA can mint a valid cert
for any site. The mitigations are **Certificate Transparency** (every cert is
publicly logged, so you can detect a rogue one), revocation (OCSP/CRL), and CAA
records (05) limiting which CA may issue for your domain. It's defense-in-depth
over an admittedly trust-heavy foundation.

### "Is mTLS just TLS twice?"

No — it's one handshake where *both* sides present and verify certificates. Normal
TLS authenticates only the server; mTLS adds client-certificate verification in
the same handshake. The win is replacing phishable bearer tokens with per-
connection cryptographic proof of identity — the foundation of zero-trust meshes.
