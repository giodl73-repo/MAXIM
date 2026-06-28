---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "04-CONGESTION-CONTROL.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:networking:congestion-control
kind: guide
module: networking
section: networking
title: Congestion Control - Reno, CUBIC, BBR, AIMD, Bufferbloat
status: source-custody
source_custody: partial
current_path: networking/04-CONGESTION-CONTROL.md
canonical_path: networking/04-CONGESTION-CONTROL.md
backsource_ids: [proof-backfill:networking:04-congestion-control, git-history:networking:04-congestion-control]
concepts: [congestion control, aimd, reno, cubic, bbr, slow start, bufferbloat, ecn]
root_concepts: [congestion control]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Congestion Control — Reno, CUBIC, BBR, AIMD, Bufferbloat

## The Big Picture

Congestion control answers one question: **how fast should I send when I cannot
see the network's capacity?** No router tells the sender "the link is full" (with
rare exceptions). The sender must *infer* available bandwidth from indirect
signals — lost packets, rising delay, ACK timing — and continuously adjust its
sending rate. Get it wrong on the low side and you waste capacity; get it wrong
on the high side and you cause **congestion collapse**, where everyone retransmits
into an already-full network and throughput craters. The history of this field is
a sequence of ever-cleverer guesses at that hidden capacity.

```
              THE FUNDAMENTAL PROBLEM: capacity is INVISIBLE
   SENDER                    NETWORK (unknown capacity)            RECEIVER
   +------+    cwnd packets   +----+    +----+    +----+           +------+
   | send |================>  | R1 |===>| R2 |===>| R3 |=========> | recv |
   +------+                   +----+    +----+    +----+           +------+
       ^                        |bottleneck link, finite rate|        |
       |                        | a QUEUE builds if you      |        |
       |   feedback signals:    | send faster than it drains |        |
       +--- loss (drop) --------+                                     |
       +--- delay (RTT rising) -+  <- queue filling shows as latency  |
       +--- ACK pacing ---------+----------------------------- ACKs --+

   GOAL: send at exactly the bottleneck rate. Too slow = waste.
         Too fast = queue grows -> latency rises -> eventually DROPS.
```

The sender maintains a **congestion window** `cwnd` — the number of bytes it may
have in flight before getting an ACK. Congestion control is entirely the
algorithm that grows and shrinks `cwnd`. Recall from 03 that the real send limit
is `min(rwnd, cwnd)`; this guide is about the `cwnd` half.

> **Bridge — control under partial observability.** This is a control-theory
> problem with a hidden plant: you actuate (send rate), observe a noisy proxy
> (loss/delay), and must converge to an unknown setpoint (bottleneck bandwidth)
> while *other* controllers (competing flows) perturb the same plant. AIMD is the
> control law that makes that distributed system stable and fair.

---

## Flow Control vs. Congestion Control (Recap)

Worth restating because it is *the* prerequisite distinction (see 03):

```
   FLOW CONTROL          CONGESTION CONTROL
   ============          ==================
   protects RECEIVER     protects the NETWORK
   window = rwnd         window = cwnd
   set BY receiver       computed BY sender (this guide)
   explicit (header)     INFERRED (no field tells you)

   actual send window = min(rwnd, cwnd)
```

Flow control is easy — the receiver simply states its free buffer. Congestion
control is hard — the network states *nothing*, so the sender must reverse-engineer
capacity from symptoms. Everything below is that reverse-engineering.

---

## AIMD — The Stability Law

The foundational algorithm is **AIMD (Additive Increase, Multiplicative
Decrease)**, from the original work by Van Jacobson (1988) after the Internet
suffered real congestion collapses. The rule:

```
   ADDITIVE INCREASE:        every RTT with no loss, cwnd += 1 (a constant)
   MULTIPLICATIVE DECREASE:  on loss, cwnd *= 0.5 (cut in half)

   cwnd over time = the classic SAWTOOTH:

   cwnd
    |            /|          /|          /|
    |           / |         / |         / |
    |          /  |        /  |        /  |     additive climb (gentle)
    |         /   |       /   |       /   |
    |        /    |______/    |______/    |____ multiplicative drop (sharp)
    |_______/                                    (halve on loss)
    +------------------------------------------------> time
            ^loss      ^loss      ^loss
```

Why this asymmetry — *slow up, fast down*? Because it provably converges to
**fairness and stability**. The classic argument: if two flows share a link and
both add the same constant and multiply by the same factor, their rates converge
toward equality regardless of starting point. Symmetric additive-both or
multiplicative-both does **not** converge to fair shares; AIMD does. Reacting hard
to congestion and probing gently for more is what keeps the whole Internet from
oscillating into collapse.

---

## TCP Reno: Slow Start and the Phases

The classic loss-based algorithm — **TCP Reno** (and its NewReno refinement) —
wraps AIMD in a startup phase and a recovery phase. Four states:

```
   1) SLOW START (despite the name, EXPONENTIAL growth):
        cwnd starts small (a few MSS), DOUBLES every RTT.
        Goal: find the rough scale of capacity fast.
        Continues until cwnd reaches ssthresh OR a loss occurs.

   2) CONGESTION AVOIDANCE (additive increase, the linear climb):
        once past ssthresh, cwnd += 1 MSS per RTT.
        This is the slow probing edge of the sawtooth.

   3) FAST RETRANSMIT / FAST RECOVERY (3 duplicate ACKs = mild loss):
        cut ssthresh = cwnd/2, set cwnd ~= ssthresh, keep going.
        (multiplicative decrease, but stay in avoidance)

   4) TIMEOUT (RTO fires = severe loss):
        ssthresh = cwnd/2, cwnd = 1, back to SLOW START.
        (the harsh reset — the network may be badly congested)

   cwnd
    |          ____ congestion avoidance (linear)
    |         /
    |        /
    |       / <- exit slow start at ssthresh
    |      |
    |     /| slow start
    |    / | (exponential)
    |___/__|________________________________> time
```

The two loss signals from 03 map directly onto recovery aggressiveness: **3
duplicate ACKs** mean "one packet lost, network basically fine" → gentle halving;
an **RTO timeout** means "I heard nothing back, the network may be wedged" → harsh
reset to `cwnd = 1` and slow start. Reno's defining weakness: it treats *any*
loss as congestion, which punishes long-distance, high-bandwidth links and
wireless (where loss can be non-congestive).

---

## TCP CUBIC: The Modern Default

**CUBIC** is the default congestion control on Linux (and thus most of the
Internet's servers). It keeps the loss-based AIMD framework but replaces the
*linear* increase with a **cubic function** of time since the last loss, which
makes it far more efficient on **long fat networks** (high bandwidth × high RTT).

```
   RENO'S LINEAR PROBE vs CUBIC'S CUBIC PROBE after a loss:

   cwnd                                cwnd
    |        /  (slow, RTT-coupled)     |    ___---  plateau near
    |      /                            |  /  Wmax (the last-loss point)
    |    /                              | |
    |  /                                ||  steep again to probe higher
    |/__________> time                  |/__________> time
       RENO                                CUBIC

   CUBIC's window growth depends on REAL TIME since last loss, not RTT.
   -> two flows with very different RTTs grow more fairly (RTT-independence).
   -> it ramps fast toward the prior max (Wmax), eases off near it (caution),
      then probes beyond it (exploration).
```

CUBIC's key wins: (1) growth is a function of *wall-clock time*, not RTT, so it's
fairer between short-RTT and long-RTT flows; (2) it spends most of its time near
the last known good window, gently probing higher. It is still **loss-based** — it
fills the queue until something drops — which is exactly the behavior that causes
bufferbloat.

---

## Bufferbloat: When Big Buffers Backfire

**Bufferbloat** is the pathology where oversized buffers in routers and modems
*hide* loss from loss-based congestion control, so the sender keeps ramping,
filling the buffer, and adding enormous **latency** without ever triggering the
loss signal that would tell it to back off.

```
   THE TRAP (loss-based CC + huge buffer):

   sender keeps increasing cwnd ----> bottleneck queue fills up
                                       (but buffer is HUGE, so no drop yet)
        |                                      |
        | no loss seen -> "must be fine!"      | queue depth = 100s of ms
        v                                      v
   keeps ramping ------------------------> LATENCY balloons, but
                                            throughput is unchanged.

   Result: a saturated link adds SECONDS of delay. Video buffers, a
   download in another tab makes your video call unusable. The buffer
   "helped" by not dropping -> and thereby broke latency for everyone.
```

The mitigations attack it from two directions:

- **Smarter queue management** in the router: **AQM (Active Queue Management)**
  algorithms like **CoDel** (Controlled Delay) and **FQ-CoDel** drop or mark
  packets *based on how long they've been queued*, signaling congestion before
  the buffer is full and isolating flows fairly.
- **Delay-based congestion control** in the sender (next section): use *rising
  latency* as the congestion signal instead of waiting for a drop.

> **Bridge — queue depth as backpressure.** Bufferbloat is the absence of
> backpressure: an unbounded queue lets a producer outrun a consumer with no
> signal until catastrophe. You solve it in distributed systems (07
> message-queues) with bounded queues and explicit backpressure; CoDel is bounded
> queueing by *time* applied to packets.

---

## TCP BBR: Model the Pipe, Don't Wait for Loss

**BBR (Bottleneck Bandwidth and Round-trip propagation time)**, from Google, is a
fundamentally different philosophy. Instead of treating loss as the congestion
signal, BBR builds an explicit **model of the path**: it continuously measures the
two quantities that actually define the pipe and sends at exactly their product.

```
   BBR MEASURES TWO THINGS:
     BtlBw  = bottleneck bandwidth   (max delivery rate observed)
     RTprop = round-trip propagation (min RTT observed, i.e. empty-queue RTT)

   THE OPTIMAL OPERATING POINT (Kleinrock, 1979):
     BDP (bandwidth-delay product) = BtlBw * RTprop
     -> send just enough to keep the pipe FULL but the QUEUE EMPTY.

         throughput                    latency
              |   ____________              |          /
              |  /                          |         /
              | /                           |________/  <- queue starts here
              |/____________> in-flight     |____________> in-flight
                  ^optimal: edge of full pipe, before the queue grows
```

BBR's advantages: it is **loss-tolerant** (a random wireless drop doesn't crater
its rate, fixing Reno's old weakness) and it actively keeps the queue *empty*,
sidestepping bufferbloat instead of merely surviving it. Its trade-off is
**fairness**: early BBR could be aggressive against loss-based flows (CUBIC)
sharing the same link; **BBRv2/BBRv3** add explicit loss and ECN response to
coexist more gracefully. BBR is a model-based controller; CUBIC is a
signal-reactive one.

---

## ECN: Asking the Network to Just Tell You

The cleanest fix is to stop guessing entirely. **ECN (Explicit Congestion
Notification, RFC 3168)** lets a router *mark* a packet ("I'm getting congested")
instead of *dropping* it. The receiver echoes the mark back to the sender, which
backs off — congestion control without paying the cost of an actual loss and
retransmission.

```
   WITHOUT ECN:  router congested -> DROP packet -> sender infers loss
                 (cost: a retransmission + the latency of detecting it)

   WITH ECN:     router congested -> SET a bit in the IP header (CE)
                 -> receiver echoes it -> sender shrinks cwnd, NO packet lost

   ECN uses 2 bits in the IPv4/IPv6 header (the ECN field) plus TCP flags.
   Modern AQM (CoDel) can MARK instead of DROP when both ends support ECN.
```

ECN turns an implicit, lossy signal into an explicit, lossless one. Adoption is
now widespread on servers; combined with AQM it is the most direct attack on both
congestion *and* bufferbloat. Data-center variants (**DCTCP**) lean on ECN heavily
because in a controlled fabric (09) you can guarantee every device supports it.

---

## Comparison

| Algorithm | Signal | Increase | Strength | Weakness |
|---|---|---|---|---|
| **Reno/NewReno** | loss | linear (AIMD) | simple, foundational | poor on long-fat links; loss = congestion |
| **CUBIC** | loss | cubic vs. time | great on LFNs, fair across RTTs | still fills buffers (bufferbloat) |
| **BBR** | bandwidth + RTT model | rate-paced | loss-tolerant, empties queue | fairness vs. CUBIC (improved in v2/v3) |
| **DCTCP** | ECN marks | ECN-proportional | precise in DC fabrics | needs ECN everywhere (controlled net) |

```
   PHILOSOPHIES:
   Reno/CUBIC: "fill the pipe until something drops, then back off." (reactive)
   BBR:        "measure the pipe, sit at its edge, never fill the queue." (model)
   DCTCP/ECN:  "let the network tell me precisely how congested it is." (explicit)
```

---

## Decision Cheat Sheet

| Situation | Reach for / expect |
|---|---|
| General-purpose server default (Linux) | CUBIC |
| Long fat network (high BW × high RTT) | CUBIC or BBR |
| Lossy links (wireless, transcontinental) | BBR (loss-tolerant) |
| Latency matters under load (video, RPC) | BBR + AQM (CoDel) to kill bufferbloat |
| Controlled datacenter fabric (09) | DCTCP with ECN everywhere |
| Router/modem adding seconds of lag | AQM (FQ-CoDel) + enable ECN |
| Want congestion signal without loss | ECN |
| Two flows sharing a link should be fair | AIMD's convergence is why they are |
| Startup: ramp to capacity fast | slow start (exponential, then ssthresh) |
| Why throughput collapses under load | congestion collapse — AIMD prevents it |

---

## Common Confusion Points

### "Slow start is exponential — isn't that a contradiction?"

The name is historical and misleading. Slow start *grows exponentially* (cwnd
doubles per RTT). It's "slow" only relative to the old behavior of blasting a full
window immediately. It's the *fast* discovery phase; congestion avoidance is the
genuinely slow (linear) phase.

### "Why halve the window on loss instead of just nudging down?"

Because **multiplicative** decrease is what makes AIMD provably converge to fair,
stable sharing. Additive-decrease wouldn't react fast enough to relieve
congestion, and the asymmetry (gentle up, sharp down) is exactly the property
that prevents oscillation and collapse. It's a mathematical result, not a tuning
choice.

### "Bigger buffers should help, right? Fewer drops?"

That's the bufferbloat trap. For loss-based control, an oversized buffer *hides*
the loss signal, so the sender keeps ramping and the buffer fills with hundreds of
milliseconds of latency — throughput unchanged, latency ruined. The fix is
*smaller, smarter* queues (AQM/CoDel) that signal congestion by **delay**, not by
overflow.

### "Is BBR strictly better than CUBIC?"

No — different trade-offs. BBR is loss-tolerant and keeps queues empty, which is
great on lossy or bufferbloated paths. But early BBR could grab more than its fair
share against CUBIC flows on a shared link; BBRv2/v3 added ECN and loss response
to fix that. CUBIC remains the safe, fair default; BBR shines on specific path
characteristics.

### "Does congestion control happen for UDP too?"

Not by default — raw UDP (03) has *no* congestion control, which is why
UDP-flooding can be antisocial. But protocols built on UDP add their own: **QUIC**
(03) implements CUBIC or BBR internally, and real-time media uses purpose-built
schemes. The principle (AIMD-style backoff) is mandatory for any protocol that
wants to coexist on the Internet; it just isn't baked into UDP itself.
