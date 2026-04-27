# Cloud Networking: VNet, Peering, Load Balancer, DNS, CDN, ExpressRoute

## The Big Picture

Cloud networking provides the connectivity fabric between all other services. The hierarchy flows from global routing and CDN at the edge down to VNet-internal routing between services.

```
AZURE NETWORKING ARCHITECTURE LAYERS

  GLOBAL / EDGE LAYER:
    Azure Front Door     — Global HTTP/S load balancing + WAF + CDN
    Azure CDN            — Content caching at edge nodes
    Azure Traffic Manager — DNS-based global routing (non-HTTP)

  REGIONAL ENTRY POINTS:
    Application Gateway  — L7 load balancer + WAF (regional)
    Azure Load Balancer  — L4 (TCP/UDP) load balancer (regional)

  VIRTUAL NETWORK LAYER:
    VNet / Subnets / NSGs — Private network space, micro-segment
    VNet Peering          — Connect VNets (same or cross-region)
    VPN Gateway           — Site-to-site VPN to on-premises
    ExpressRoute          — Dedicated private circuit to Azure

  DNS LAYER:
    Azure DNS             — Authoritative DNS hosting
    Private DNS Zones     — Internal DNS for VNet resources
    Azure Private Link    — Private endpoints, no public IP needed
```

---

## Virtual Network (VNet)

A VNet is your private network in Azure — isolated, you define the IP space.

```
VNET STRUCTURE
  VNet: 10.0.0.0/16  (you choose the address space)
    |
    +-- Subnet: 10.0.1.0/24  web-tier
    |     NSG: allow inbound 443 from Internet
    |
    +-- Subnet: 10.0.2.0/24  app-tier
    |     NSG: allow inbound 8080 from web-tier only
    |
    +-- Subnet: 10.0.3.0/24  data-tier
    |     NSG: allow inbound 1433 from app-tier only
    |
    +-- Subnet: 10.0.4.0/24  private-endpoints
    |     Private endpoints for Storage, SQL, Key Vault
    |
    +-- Subnet: 10.0.5.0/24  AzureBastionSubnet
          (required for Azure Bastion, specific naming)

RESERVED ADDRESSES IN EVERY SUBNET:
  .0  - Network address
  .1  - Azure default gateway
  .2  - Azure DNS
  .3  - Azure reserved
  .255 - Broadcast
  → A /29 gives you 3 usable IPs; plan subnet size appropriately

BEST PRACTICE:
  Use /8 or /16 for VNet address space (room for subnets)
  Use /24 or smaller per subnet (avoid waste)
  Reserve separate subnet for GatewaySubnet, AzureBastionSubnet
  Do NOT overlap with on-premises network (VPN/ExpressRoute peering requires non-overlapping)
```

### VNet Peering vs. VPN Gateway vs. ExpressRoute

```
CONNECTIVITY COMPARISON
+----------------------------------------------------------------------+
| Option           | Bandwidth  | Latency  | Cost      | Use Case      |
+------------------+------------+----------+-----------+---------------+
| VNet Peering     | Up to VNet | ~1ms     | Per GB    | Same org,     |
| (same region)    | limits     | (low)    | transferred|connect VNets |
+------------------+------------+----------+-----------+---------------+
| Global VNet      | Up to VNet | ~10-50ms | Per GB    | Multi-region  |
| Peering          | limits     | (varies) | trans/GB  | VNets         |
+------------------+------------+----------+-----------+---------------+
| VPN Gateway      | 1-10 Gbps  | 10-50ms  | Gateway   | Small/medium  |
| (site-to-site)   | (gen SKU)  |          | + per GB  | hybrid (VPN)  |
+------------------+------------+----------+-----------+---------------+
| ExpressRoute     | 50Mbps–    | ~5-10ms  | Circuit   | Large hybrid, |
| Standard         | 10Gbps     | (private)| + port    | latency-sens  |
+------------------+------------+----------+-----------+---------------+
| ExpressRoute     | 10Gbps–    | ~5ms     | High      | Global enter- |
| Global Reach     | 100Gbps    |          | premium   | prise, DC-DC  |
+------------------+------------+----------+-----------+---------------+

VNET PEERING PROPERTIES:
  Non-transitive: VNet A peers with B, B peers with C ≠ A can reach C
  Solution: Hub-Spoke topology (all spokes peer with hub; hub routes)
  Or: Azure Virtual WAN (managed hub-spoke at scale)

EXPRESSROUTE:
  Dedicated private circuit from your datacenter to Azure
  Does NOT traverse public internet
  Partners: AT&T, Equinix, Verizon, etc. (colocation required or via partner)
  BGP routing: you announce your on-premises prefixes; Azure announces its
  Redundant by design: two circuits in different peering locations
```

---

## Hub-Spoke Network Topology

The standard enterprise pattern for Azure networking:

```
HUB-SPOKE TOPOLOGY

                    +--------------------+
                    |   HUB VNet         |
                    |   10.0.0.0/16      |
                    |                    |
                    |  Azure Firewall    |
                    |  VPN/ER Gateway    |
                    |  Bastion           |
                    |  Shared Services   |
                    +--------------------+
                    /         |          \
                   /          |           \
  Three spoke VNets connected to the hub:
    Spoke VNet Dev   (10.1.x.x)
    Spoke VNet Prod  (10.2.x.x)
    Spoke VNet Stage (10.3.x.x)

ALL TRAFFIC FLOWS THROUGH HUB:
  East-west: Spoke A → Hub Firewall → Spoke B
    (inspect, log, control all inter-spoke traffic)
  North-south: Spoke → Hub Firewall → Internet
    (single egress point, URL filtering, threat intelligence)
  Hybrid: On-premises → Hub VPN/ER Gateway → Spokes
    (single on-premises-to-cloud connection point)

AZURE VIRTUAL WAN (managed hub-spoke at scale):
  Microsoft manages hub infrastructure
  Automated routing tables, branch connectivity, security
  Use: many spoke VNets, global connectivity, simplified ops
```

---

## Load Balancers

### Azure Load Balancer (L4)

```
AZURE LOAD BALANCER:
  Layer 4: TCP/UDP packet distribution
  Regional: within one Azure region
  Internal LB: private IP frontend (east-west load balancing)
  Public LB: public IP frontend (internet-facing)
  Health probes: TCP, HTTP, HTTPS
  SKUs:
    Basic: free, limited features, no AZ support
    Standard: $18/month base, AZ support, SLA, HTTPS probes
  Distribution: 5-tuple hash (src IP, src port, dst IP, dst port, protocol)
  Session persistence: source IP affinity (optional)

TYPICAL USE:
  Internal LB in front of multiple VMs in same tier
  TCP load balancing for non-HTTP protocols
  First-hop LB before Application Gateway
```

### Application Gateway (L7)

```
APPLICATION GATEWAY:
  Layer 7: HTTP/HTTPS application delivery controller
  Features:
    SSL offload: terminate TLS at gateway, HTTP to backends
    URL-based routing: /api/* → api-pool, /static/* → static-pool
    Multi-site hosting: host multiple domains on single gateway
    WAF (Web Application Firewall): OWASP Core Rule Set
    Autoscaling: v2 SKU scales based on traffic
    Cookie-based session affinity
    Health probes: HTTP(S) endpoint probing
  Use: single-region HTTPS ingress with WAF

WAF MODES:
  Detection: logs threats but allows traffic (test/audit)
  Prevention: blocks malicious requests (production)
  OWASP CRS (Core Rule Set) 3.x protects against:
    SQL injection, XSS, command injection, path traversal,
    CSRF, protocol violations
```

### Azure Front Door (Global L7 + CDN)

```
AZURE FRONT DOOR:
  Global, multi-region HTTP/S load balancer + WAF + CDN
  Anycast: traffic routed to nearest Front Door PoP (150+ globally)
  Health probes: actively probe backends; failover in <1min

  FEATURES:
    Global load balancing: route to closest healthy backend
    WAF at the edge (closer to users, before traffic hits region)
    TLS offload at edge
    URL rewrite and redirect
    CDN caching (Azure CDN is being merged into Front Door)
    Private link origin: connect to backends without public IP

  USE: Multi-region active-active, global latency optimization,
       globally consistent WAF policy

  vs. Application Gateway:
    App Gateway: regional, inside VNet, standard enterprise L7 LB
    Front Door: global, edge-based, CDN + WAF + global routing
```

---

## DNS Architecture

```
AZURE DNS (authoritative):
  Host your public DNS zones in Azure
  Integrated with Azure RBAC
  Anycast: queries resolved at nearest Azure nameserver
  Use: host public DNS for your domains (contoso.com)

PRIVATE DNS ZONES:
  Internal DNS resolution within VNets
  Auto-registration: Azure services automatically register
    e.g., Private endpoint for SQL: sqlserver.privatelink.database.windows.net
         resolves to 10.0.4.10 inside VNet (public IP outside)
  VNet link: must link Private DNS Zone to each VNet that needs to resolve it
  Naming: typically *.privatelink.<service>.azure.com

DNS FORWARDING FOR HYBRID:
  On-premises DNS → Azure DNS Resolver (inbound endpoint)
    → Resolves Azure Private DNS zones from on-premises
  Azure DNS Resolver (outbound endpoint) → On-premises DNS
    → Resolves on-premises hostnames from Azure
  Conditional forwarders: define which zones go to which resolvers
  Azure DNS Private Resolver (GA 2022): managed service for this pattern
```

---

## CDN and Private Endpoints

### Azure CDN / Front Door CDN

```
CDN BENEFIT:
  Cache static content at edge PoPs (~150 globally)
  User hits nearest PoP → cache hit → <10ms response
  Without CDN → request to origin region → 50-200ms
  Cache rules: by URL pattern, headers, query string

CONTENT TO CACHE:
  Static: images, CSS, JS, fonts → high cache-hit ratio
  Dynamic: personalized HTML, API responses → usually don't cache
    (or cache with very short TTL for partial acceleration)

AZURE CDN OPTIONS:
  Azure CDN from Akamai/Verizon (legacy, being deprecated)
  Azure Front Door (Standard/Premium): recommended modern CDN
    + WAF, global LB, private link all in one service
```

### Private Endpoints vs. Service Endpoints

```
SERVICE ENDPOINT:
  Extends VNet identity to Azure service (Storage, SQL, etc.)
  Service sees traffic as coming from VNet
  But: the traffic may still traverse public IP (route to Azure backbone)
  Access control: allow traffic only from specific VNet/subnet
  Simpler: no private IP needed

PRIVATE ENDPOINT:
  Creates a network interface in your VNet with a private IP
  DNS resolution: private endpoint IP returned for service FQDN
  Traffic NEVER leaves the Azure network (no public internet)
  More secure than service endpoint
  Required for: zero-trust, no public access scenarios
  DNS: auto-updates Private DNS Zone (or manual configuration)

EXAMPLE:
  Storage account: storageaccount.blob.core.windows.net
  Without private endpoint: resolves to public IP (52.x.x.x)
  With private endpoint in VNet: resolves to 10.0.4.10 (private IP)
  → From VNet, all traffic stays on Azure network

  NSG on private endpoint subnet: traffic to private endpoint
    is only from authorized subnets/service tags
```

---

## Common Confusion Points

**"VNet Peering is transitive"**
It is NOT. If VNet A is peered to B and B is peered to C, traffic from A cannot reach C via B unless you configure User Defined Routes (UDR) through a hub NVA/firewall, or use Azure Virtual WAN. This surprises many architects.

**"ExpressRoute is always faster than VPN"**
ExpressRoute is a dedicated private circuit — it does not traverse the public internet. The latency improvement depends on the path. For most enterprise use cases, ExpressRoute is not about raw latency but about consistency, bandwidth, and SLA.

**"Application Gateway and Azure Load Balancer do the same thing"**
Azure Load Balancer is L4 (IP+port): it does not look at HTTP content. Application Gateway is L7 (HTTP): it inspects URLs, headers, cookies, and applies WAF rules. They are used at different points in the architecture — often together (LB in front of App Gateways for scale, or behind App Gateway for internal L4 distribution).

**"Private Endpoint solves all security for cloud services"**
Private Endpoint removes the public IP from the access path — connections come through the private IP only. But you still need: NSG rules on the private endpoint subnet, proper DNS resolution (private zone), access policies on the service itself, and authentication for connecting applications.

---

## Decision Cheat Sheet

| Need | Azure Service |
|------|--------------|
| Regional HTTP/S with WAF, URL routing | Application Gateway (v2 WAF tier) |
| Global HTTP/S with CDN, multi-region failover | Azure Front Door Standard/Premium |
| TCP/UDP regional load balancing | Azure Load Balancer Standard |
| DNS-based global routing (non-HTTP) | Azure Traffic Manager |
| Connect two VNets (same region) | VNet Peering |
| Connect two VNets (different regions) | Global VNet Peering |
| Connect on-prem to Azure over VPN | VPN Gateway |
| Connect on-prem to Azure (dedicated, high-bandwidth) | ExpressRoute |
| Public DNS hosting | Azure DNS |
| Internal DNS for private resources | Private DNS Zones |
| Remove public IP from Azure service | Private Endpoint |
| Hub-spoke at scale (many VNets, branches) | Azure Virtual WAN |
