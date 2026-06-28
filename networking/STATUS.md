# networking/ — Status

## Files

| File | Topic | Status |
|------|-------|--------|
| 00-OVERVIEW.md | The Layered Network Model End-to-End — Landscape | ✅ |
| 01-LINK-LAYER.md | Link Layer: Ethernet, MAC, Framing, Switching, VLANs, ARP | ✅ |
| 02-IP-ROUTING.md | IP and Routing: IPv4/IPv6, CIDR, Routing Tables, BGP, OSPF | ✅ |
| 03-TRANSPORT.md | Transport: TCP State Machine, UDP, QUIC, Ports, Sockets | ✅ |
| 04-CONGESTION-CONTROL.md | Congestion Control: Reno, CUBIC, BBR, AIMD, Bufferbloat | ✅ |
| 05-DNS.md | DNS: Resolution, Record Types, Caching/TTL, DoH/DoT, Anycast | ✅ |
| 06-TLS-AND-SECURITY.md | TLS 1.3, Certificates/PKI, mTLS — Transport Security | ✅ |
| 07-NAT-AND-FIREWALLS.md | NAT Types, Stateful Firewalls, CGNAT, Port Forwarding | ✅ |
| 08-LOAD-BALANCING-CDN.md | Load Balancing (L4/L7), Anycast, CDNs, Edge | ✅ |
| 09-DATACENTER-NETWORKING.md | Datacenter: Clos/Leaf-Spine, Overlays/VXLAN, RDMA, SDN | ✅ |

## Coverage Notes

Networking from the wire up: the layered model, Ethernet framing and switching,
IP addressing and inter-domain routing (BGP/OSPF), the transport layer (TCP/UDP/QUIC),
congestion control theory, DNS, TLS 1.3 and PKI, NAT and firewalls, load balancing
and CDNs, and datacenter fabrics. The thread throughout is *how the layers nest* and
*what mechanism each layer owns* — addressing vs. routing vs. flow vs. congestion vs.
naming vs. trust. The VP bridge: the services you scaled at VSTS/Azure ride every one
of these layers; this directory is the substrate beneath the distributed systems you
already know cold. Deliberately scoped out: physical-layer signal encoding and the EM
spectrum (covered in telecommunications/), and application protocols above L7 like
HTTP semantics and gRPC framing (touched only where they motivate transport/TLS
choices). Connects to distributed-systems/, cloud-architecture/, cryptography/,
telecommunications/, and os/.
