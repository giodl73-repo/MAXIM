---
maxim_schema: maxim.frontmatter.v1
id: maxim:networking:datacenter-networking
kind: guide
module: networking
section: networking
title: Datacenter Networking - Clos/Leaf-Spine, Overlays/VXLAN, RDMA, SDN
status: source-custody
source_custody: partial
current_path: networking/09-DATACENTER-NETWORKING.md
canonical_path: networking/09-DATACENTER-NETWORKING.md
backsource_ids: [proof-backfill:networking:09-datacenter-networking, git-history:networking:09-datacenter-networking]
concepts: [clos, leaf-spine, vxlan, overlay, rdma, sdn, ecmp, east-west traffic]
root_concepts: [datacenter networking]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Datacenter Networking — Clos/Leaf-Spine, Overlays/VXLAN, RDMA, SDN

## The Big Picture

A datacenter network has a fundamentally different shape than the Internet. The
Internet optimizes for **north-south** traffic (clients pulling content in from
outside) over links you don't own. A datacenter optimizes for **east-west**
traffic (server-to-server: a single user request fanning out to hundreds of
internal microservices, databases, and caches) over a fabric one organization
controls completely. That control changes everything: you can abandon spanning
tree (01), route on L3 throughout, build any-to-any bandwidth, and layer software
abstractions on top. This guide is where networking meets the distributed systems
that ride on it.

```
            NORTH-SOUTH (Internet)        vs.        EAST-WEST (datacenter)
   +----------------------------+              +----------------------------+
   |     clients (outside)      |              |   one user request fans    |
   |            |               |              |   out to MANY services:    |
   |            v               |              |                            |
   |        [ origin ]          |              |  svc-A <-> svc-B <-> cache  |
   |     a few big flows IN     |              |    ^         |        ^     |
   +----------------------------+              |    +-- DB <--+        |     |
                                               |         <-> queue <---+     |
   Internet routing is about REACHING          |  MILLIONS of small flows    |
   distant hosts. Datacenter fabric is         |  server-to-server, ANY to   |
   about ANY server reaching ANY other         |  ANY, all under one admin   |
   at full speed, predictable latency.         +----------------------------+
```

Two architectural moves define the modern datacenter. **Clos / leaf-spine** gives
the physical fabric uniform, non-blocking, any-to-any bandwidth. **Overlays
(VXLAN)** give software-defined virtual networks on top of it, so tenants and
services get isolated L2/L3 segments decoupled from the physical wiring. Add
**RDMA** for ultra-low-latency transfers and **SDN** for centralized control, and
you have the cloud's substrate.

> **Bridge — the fabric under your distributed systems.** Every consensus round
> (distributed-systems/03), every replication stream, every shuffle in a data
> pipeline rides on this fabric. The leaf-spine design exists precisely because
> distributed systems generate massive, unpredictable east-west traffic — the
> network had to become a uniform, high-bisection-bandwidth substrate so that
> *where* a service lands doesn't change its performance.

---

## Why Not Just Use the Old Tree?

Classic enterprise networks used a three-tier tree (access → aggregation → core)
with spanning tree (01) blocking redundant links. That design fails the datacenter
on two counts:

```
   OLD ACCESS/AGGREGATION/CORE TREE:

              [ CORE ]
             /        \
       [ AGG ]        [ AGG ]
       /     \        /     \
    [acc]  [acc]   [acc]  [acc]
     |||    |||     |||    |||
    servers...

   PROBLEMS for a datacenter:
   1) OVERSUBSCRIPTION: many servers funnel up through few uplinks ->
      the core is a bottleneck for east-west traffic.
   2) SPANNING TREE BLOCKS half the links to break loops -> you PAY for
      redundant links but can't USE them for bandwidth.
   3) east-west traffic between two access switches must climb ALL the way
      to the core and back -> long, congested path.
```

The datacenter's answer is to flatten and L3-route everything, using a topology
where bandwidth scales horizontally and *every* link carries traffic.

---

## Clos / Leaf-Spine Fabric

The dominant datacenter topology is a **folded Clos network**, marketed as
**leaf-spine**. (Clos networks come from Charles Clos's 1953 work on
non-blocking telephone switching fabrics — the same math, repurposed.) Two tiers:
**leaf** switches connect to servers; **spine** switches interconnect the leaves.
*Every leaf connects to every spine.*

```
   LEAF-SPINE (2-tier Clos):

         [ SPINE1 ]   [ SPINE2 ]   [ SPINE3 ]   [ SPINE4 ]
            | \  \      /  | \       / / |       / /  |
            |  \  \    /   |  \     / /  |      / /   |   <- EVERY leaf
            |   \  \  /    |   \   / /   |     / /    |      to EVERY spine
         [ LEAF1 ]   [ LEAF2 ]   [ LEAF3 ]   [ LEAF4 ]
           ||||        ||||        ||||        ||||
         servers      servers     servers     servers

   KEY PROPERTIES:
   - ANY server to ANY server = exactly 2 hops (leaf -> spine -> leaf).
     Predictable, uniform latency regardless of placement.
   - ALL links active (no spanning tree). Routed at L3 with ECMP.
   - SCALE OUT: need more bandwidth? add a spine. More servers? add a leaf.
     Bandwidth grows by adding switches, not by buying a bigger core.
   - NON-BLOCKING: with the right ratios, every server can talk at full
     line rate simultaneously (high bisection bandwidth).
```

The traffic-spreading mechanism is **ECMP (Equal-Cost Multi-Path)**: since every
spine offers an equal-cost path between any two leaves, the fabric hashes each
flow (by 5-tuple) across all spines, using every link. This is *why* spanning tree
is abandoned — leaf-spine is **L3-routed** (often with BGP as the fabric IGP, even
*inside* the datacenter), so loops aren't a problem and all links carry load.

> **Bridge — horizontal scaling, applied to the network.** Leaf-spine is
> scale-out for bandwidth: add identical commodity switches to grow capacity
> linearly, exactly as you add stateless app servers behind a load balancer (08).
> The old core-tree was scale-up (buy a bigger chassis). The cloud's economics
> demanded the network become as horizontally scalable as the compute on it.

---

## Overlays and VXLAN

The physical fabric is L3-routed for scale — but tenants and services often need
L2 adjacency (a flat segment, mobile IPs, broadcast domains for clustering). The
reconciliation is an **overlay**: a virtual network **tunneled** over the physical
**underlay**. The dominant encapsulation is **VXLAN (Virtual Extensible LAN, RFC
7348)**.

```
   TWO PLANES:
     UNDERLAY = the physical leaf-spine fabric, L3-routed (the "real" network)
     OVERLAY  = virtual L2/L3 networks tunneled across the underlay

   VXLAN ENCAPSULATION: wrap the tenant's L2 frame inside UDP/IP and ship it
   across the L3 underlay. The original frame is the PAYLOAD.

   +--------+------+------+-------+--------------------------------+
   | Outer  | UDP  |VXLAN | VNI   |  ORIGINAL ETHERNET FRAME       |
   | IP hdr | hdr  | hdr  |(24bit)|  (the tenant's L2 frame)       |
   +--------+------+------+-------+--------------------------------+
       ^underlay routes this       ^ the overlay's actual content

   VNI = VXLAN Network Identifier, 24 bits -> ~16 MILLION segments.
   (Compare VLAN's 12-bit, 4094-segment ceiling from 01 -> this is the fix.)
```

- The endpoints that wrap/unwrap VXLAN are **VTEPs (VXLAN Tunnel Endpoints)**,
  typically the leaf switches or the hypervisor's virtual switch.
- The **24-bit VNI** gives ~16 million isolated segments, blowing past the
  4094-VLAN limit (01) — which is exactly why overlays exist: cloud multi-tenancy
  needs far more isolated networks than VLANs can express.
- The overlay **decouples** virtual topology from physical wiring: a VM can keep
  its IP when it migrates to a different rack, because its segment is a tunnel, not
  a physical cable. The underlay just sees routed UDP packets.

> **Bridge — virtual networks like virtual machines.** VXLAN is to the network
> what the hypervisor is to the server: a virtualization layer that lets many
> isolated logical networks share one physical fabric, decoupled from the
> hardware. The VNI is the tenant tag; the underlay is the bare metal. This is the
> network half of cloud's "software-defined everything."

---

## RDMA — Bypassing the Kernel

For the most latency-sensitive datacenter workloads — distributed storage, HPC,
AI training clusters, in-memory databases — even an optimized TCP stack (03) is too
slow, because every byte crosses the kernel and gets copied. **RDMA (Remote Direct
Memory Access)** lets one machine read/write another's memory *directly*, bypassing
the CPU and kernel on both ends.

```
   NORMAL TCP PATH (every transfer):
     app -> kernel socket -> TCP/IP stack -> NIC -> wire -> NIC ->
            TCP/IP stack -> kernel -> COPY -> app    (CPU touches every byte)

   RDMA PATH (zero-copy, kernel-bypass):
     app memory -----------(NIC DMAs directly)----------> remote app memory
            no CPU copy, no kernel on the data path, ultra-low latency

   DEPLOYMENTS:
     InfiniBand   - a purpose-built RDMA fabric (HPC, AI clusters)
     RoCE         - RDMA over Converged Ethernet (RDMA on standard Ethernet)
     iWARP        - RDMA over TCP/IP
```

The catch: RDMA traditionally assumes a **lossless** fabric, because its simple
flow control doesn't tolerate drops well. So RoCE deployments lean heavily on
datacenter congestion control with **ECN** and priority flow control (the **DCTCP**
philosophy from 04) to keep queues short and avoid loss. RDMA is the reason
datacenter congestion control became its own discipline: the controlled
environment lets you guarantee ECN everywhere, which the open Internet never can.

---

## SDN — Software-Defined Networking

The organizing principle behind all of the above is **SDN (Software-Defined
Networking)**: separate the **control plane** (the decisions about where traffic
goes) from the **data plane** (the hardware that forwards it), and drive the
control plane from centralized software.

```
   TRADITIONAL: each switch runs its OWN control plane (distributed protocols).
     control + data plane fused in every box -> config per device, hard to
     reason about globally.

   SDN: centralize the decisions.
     +-------------------------------------+
     |   SDN CONTROLLER (software)         |  control plane
     |   global view, policy, programming  |
     +-------------------------------------+
          | pushes forwarding rules down (e.g. OpenFlow, gNMI, BGP)
          v
     +--------+   +--------+   +--------+
     | switch |   | switch |   | switch |    data plane (just forwards
     +--------+   +--------+   +--------+     per the rules it's given)

   PAYOFF: the network becomes PROGRAMMABLE. A cloud control plane can spin
   up a tenant's virtual network, security policy, and load balancing as an
   API call -> this is how a VPC appears in seconds when you click "create".
```

SDN is what makes the cloud's network an **API**. When you create a VPC, a subnet,
a security group, or a load balancer in a cloud console, an SDN control plane is
programming the underlying fabric — pushing VXLAN tunnels (overlays), ACLs
(distributed firewalls, 07), and routes onto the physical switches and hypervisor
vswitches. The physical leaf-spine is fixed; *everything logical* is software,
provisioned on demand.

> **Bridge — control plane / data plane, which you know.** This separation is the
> same one in any system you've built at scale: a control plane that holds policy
> and global state, and a data plane that executes the hot path fast. SDN applies
> it to the network — the controller is the "scheduler/orchestrator," the switches
> are the "workers." A cloud VPC is that orchestrator exposed as a REST API.

---

## How It All Stacks in a Cloud

```
   +-------------------------------------------------------------------+
   |  SDN CONTROL PLANE (software)  -> programs everything below       |
   +-------------------------------------------------------------------+
   |  OVERLAY:  VXLAN virtual networks (per-tenant VPCs, ~16M segments)|
   +-------------------------------------------------------------------+
   |  UNDERLAY: leaf-spine Clos fabric, L3-routed, ECMP, all links live|
   +-------------------------------------------------------------------+
   |  TRANSPORT: TCP / RDMA(RoCE) with DCTCP/ECN congestion control(04)|
   +-------------------------------------------------------------------+
   |  PHYSICAL: commodity switches + servers, often jumbo frames (01)  |
   +-------------------------------------------------------------------+

   A cloud VPC = an SDN-programmed VXLAN overlay on a leaf-spine underlay.
   That single sentence is the whole modern datacenter.
```

---

## Decision Cheat Sheet

| Need | Datacenter mechanism |
|---|---|
| Uniform any-to-any server bandwidth | leaf-spine (folded Clos) |
| Use all links, no blocking | L3 routing + ECMP (drop spanning tree) |
| More fabric bandwidth | add a spine switch (scale out) |
| More server capacity | add a leaf switch (scale out) |
| Millions of isolated tenant networks | VXLAN overlay (24-bit VNI) |
| VM keeps its IP across racks | overlay decouples virtual from physical |
| Lowest-latency, zero-copy transfers | RDMA (InfiniBand / RoCE / iWARP) |
| Lossless fabric for RDMA | ECN + DCTCP, priority flow control (04) |
| Provision a network by API | SDN (centralized control plane) |
| A cloud VPC, concretely | SDN-programmed VXLAN overlay on Clos underlay |
| Reduce per-packet overhead internally | jumbo frames (~9000 MTU, 01) |

---

## Common Confusion Points

### "Why abandon spanning tree in the datacenter?"

Spanning tree (01) prevents L2 loops by *blocking* redundant links — so you pay
for links you can't use, and east-west traffic detours through a core. Datacenters
instead route at **L3 everywhere** (leaf-spine with ECMP), where loops aren't a
problem and **every** link carries traffic. Often BGP runs as the *internal* fabric
protocol. Spanning tree was built for a world that valued L2 simplicity over
bandwidth; the datacenter inverted that.

### "Underlay vs. overlay — what's the difference?"

The **underlay** is the physical, L3-routed leaf-spine fabric — the real wires and
switches. The **overlay** is the set of *virtual* networks (VXLAN tunnels) running
on top of it, giving tenants isolated L2/L3 segments decoupled from the wiring. The
underlay routes packets between racks; the overlay defines who-can-talk-to-whom
logically. A cloud VPC lives in the overlay.

### "VXLAN vs. VLAN — isn't a VLAN enough?"

A VLAN (01) tops out at **4094** segments (12-bit ID) and is tied to physical L2
adjacency. Cloud multi-tenancy needs *millions* of isolated networks that can span
racks and survive VM migration. VXLAN's **24-bit VNI** gives ~16 million segments
and tunnels them over an L3 underlay, so the virtual network is independent of the
physical topology. VXLAN is the answer to VLAN exhaustion.

### "Is RDMA just faster TCP?"

No — it's a different data path. RDMA **bypasses the kernel and CPU**, letting a
NIC write directly into remote memory (zero-copy), which TCP can't do because every
byte crosses the kernel and gets copied. RDMA trades generality and Internet-
friendliness for latency, and it typically needs a *lossless* fabric (ECN/DCTCP,
04) — viable only in a controlled datacenter, never the open Internet.

### "What does SDN actually give me?"

A **programmable** network. By splitting the control plane (decisions, centralized
in software) from the data plane (forwarding, in hardware), SDN lets a cloud
control plane provision virtual networks, security policy, and load balancing as an
**API call**. That's how a VPC, subnet, or security group materializes in seconds
when you click "create" — software pushing VXLAN tunnels and ACLs onto the fabric.
