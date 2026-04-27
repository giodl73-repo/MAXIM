# Storage Patterns: Object, Block, File, Database — Azure Blob, Managed Disk, Files

## The Big Picture

Storage in the cloud is not a single category — the right storage type depends on access pattern, latency requirement, throughput, and data structure.

```
STORAGE TYPE TAXONOMY

  OBJECT / BLOB:
    Azure Blob (S3, GCS equiv).
    Unstructured; HTTP API access; cheap at scale;
    eventual consistency.

  BLOCK:
    Managed Disk (EBS equiv).
    Raw block device; mount to VM; high IOPS/BW;
    consistent.

  FILE:
    Azure Files (EFS equiv).
    NFS / SMB share; mount to VM or pod;
    shared file access; AD auth (SMB).

  DATABASE SERVICES:
    Azure SQL Database:    structured, ACID, SQL Server compatible.
    Azure Cosmos DB:       NoSQL, global, multi-model.
    Redis Cache:           in-memory, K/V cache.
```

---

## Azure Blob Storage

Blob Storage is Azure's object store — the equivalent of Amazon S3. It is the foundation for data lakes, backups, content delivery, and analytical workloads.

### Access Tiers

```
BLOB ACCESS TIERS
+----------------------------------------------------------+
| HOT tier                                                 |
|   Storage cost: highest                                  |
|   Access cost:  lowest (per read/write operation)        |
|   Use: frequently accessed data, active web content      |
|   Latency: single-digit milliseconds                     |
+----------------------------------------------------------+
| COOL tier                                                |
|   Storage cost: ~50% of Hot                             |
|   Access cost: higher than Hot                          |
|   Minimum retention: 30 days                            |
|   Use: infrequently accessed (30 days+), backups,       |
|        monthly reports                                   |
+----------------------------------------------------------+
| COLD tier (preview 2023)                                 |
|   Storage cost: lower than Cool                          |
|   Minimum retention: 90 days                             |
|   Use: rarely accessed, long-term backup                 |
+----------------------------------------------------------+
| ARCHIVE tier                                             |
|   Storage cost: lowest (~90% less than Hot)             |
|   Access cost: very high                                |
|   Rehydration: 1–15 hours to access                    |
|   Minimum retention: 180 days                           |
|   Use: long-term retention, compliance archives,        |
|        rarely accessed data                             |
+----------------------------------------------------------+

LIFECYCLE MANAGEMENT RULES:
  Automatically transition blobs between tiers:
    After 30 days: Hot → Cool
    After 90 days: Cool → Archive
  Delete after 365 days
  Apply to entire container or by blob prefix
```

### Redundancy Options

```
LRS (Locally Redundant Storage):
  3 copies in same datacenter
  Protects: disk failure, rack failure
  Does NOT protect: datacenter failure
  Cost: cheapest
  SLA: 99.999999999% (11 9s) durability

ZRS (Zone Redundant Storage):
  3 copies across 3 AZs in same region
  Protects: datacenter failure within region
  Cost: moderate
  SLA: 12 9s durability

GRS (Geo-Redundant Storage):
  LRS in primary + LRS in secondary (paired) region
  Secondary is read-only normally; readable only after failover
  Protects: entire region failure
  Cost: ~2x LRS
  SLA: 16 9s durability

GZRS (Geo-Zone Redundant Storage):
  ZRS in primary + LRS in secondary
  Best protection + read access
  Cost: highest

RA-GRS / RA-GZRS:
  "Read-Access" variants: secondary is always readable
  (no failover required to read from secondary)
  Use: geo-distributed reads, CDN-like pattern, disaster recovery
```

### Data Lake Gen2 (ADLS Gen2)

Azure Data Lake Storage Gen2 is Blob Storage with a hierarchical namespace enabled. The key difference: it supports real directory semantics (rename is O(1) not O(n) as in flat blob), POSIX permissions, and HDFS-compatible APIs for Spark/Hadoop workloads.

```
ADLS GEN2 vs. BLOB:
  Blob:      flat namespace (paths are just key prefixes)
             rename a "directory" = copy all files + delete originals = expensive
  ADLS Gen2: true directory tree; rename = metadata operation = fast
             POSIX ACLs: owner/group/other permissions per file/directory
             Hadoop ABFS driver: native Azure access from Spark/Databricks

  Azure Databricks, Synapse Analytics → use ADLS Gen2 as data lake
```

---

## Azure Managed Disk (Block Storage)

Block storage is raw storage attached to a VM as a device — the cloud equivalent of a physical SAN volume.

```
MANAGED DISK TYPES (Azure)
+----------------------------------------------------------+
| Standard HDD                                             |
|   Max IOPS: 2,000 (per disk)                             |
|   Max throughput: 500 MB/s                               |
|   Use: dev/test, non-critical, archive                   |
|   Cost: cheapest                                         |
+----------------------------------------------------------+
| Standard SSD                                             |
|   Max IOPS: 6,000                                       |
|   Max throughput: 750 MB/s                              |
|   Use: lightly loaded production, web servers           |
|   Better latency than HDD                               |
+----------------------------------------------------------+
| Premium SSD v2                                           |
|   Max IOPS: 80,000 per disk                              |
|   Max throughput: 1,200 MB/s                             |
|   Configurable IOPS/throughput independently             |
|   Use: production databases, SAP, SQL Server             |
|   SLA: 99.9% on single VM                                |
+----------------------------------------------------------+
| Ultra Disk                                               |
|   Max IOPS: 160,000 per disk                           |
|   Max throughput: 4,000 MB/s                           |
|   Sub-millisecond latency                               |
|   Use: mission-critical databases, IO-intensive apps    |
|   Constraint: must be in Availability Zone             |
+----------------------------------------------------------+

VM DISK LIMITS:
  Each VM size has max uncached IOPS and throughput limits
  (VM throttle: e.g., Standard_D4s_v5 = 12,800 uncached IOPS)
  Adding more disks does NOT exceed VM limit
  → IOPS bottleneck may be VM, not disk
  → Stripe multiple disks (RAID 0 in OS) to exceed single disk limits
```

### Disk Snapshot and Backup

```
MANAGED DISK SNAPSHOTS:
  Full or incremental snapshots
  Incremental: only changed blocks since last snapshot (cost-efficient)
  Cross-region copy: copy snapshot to another region for DR

AZURE BACKUP FOR VMs:
  Application-consistent backup (VSS integration for Windows, freeze for Linux)
  Recovery Services Vault stores backups
  Restore: entire VM, individual disk, or individual file
```

---

## Azure Files (File Storage)

Azure Files provides fully managed file shares accessible via SMB 3.0/2.1 and NFS 4.1.

```
USE CASES FOR AZURE FILES:
  Lift-and-shift: apps using file shares, replace on-premises file server
  Home directory shares: Windows AD integration, per-user quotas
  Container volumes: mount shared read/write storage across pods (NFS)
  Configuration files: shared config without deploying to every instance
  Development: common file share for dev team

TIERS:
  Premium (SSD): sub-millisecond latency, high IOPS, provisioned capacity
  Transaction optimized: frequent reads, standard SSD
  Hot: frequently accessed, standard HDD
  Cool: rarely accessed, archive

AD INTEGRATION (SMB):
  Join Azure Files share to on-premises AD or Azure AD DS
  Users authenticate with their domain credentials
  → Map network drive in Windows with AD credentials
  → No local password required; permissions via AD groups

NFS FOR CONTAINERS:
  Mount Azure Files NFS share as Kubernetes persistent volume
  ReadWriteMany access mode: multiple pods read/write same share
  Use: shared upload directory, logging, shared configuration
  Limitation: NFS shares require Premium tier
```

---

## Database Service Selection

```
DATABASE SELECTION BY ACCESS PATTERN

RELATIONAL (SQL)
+----------------------------------------------------------+
| Azure SQL Database                                       |
|   SQL Server compatible (T-SQL, ADO.NET, EF Core)        |
|   vCore: General Purpose (standard), Business Critical   |
|   (in-memory OLTP, local SSD), Hyperscale (100TB)        |
|   Elastic Pool: shared resources for multi-tenant SaaS   |
+----------------------------------------------------------+
| Azure SQL Managed Instance                               |
|   100% SQL Server compatibility                          |
|   Agent, cross-DB queries, CLR, Service Broker          |
|   Use: migrate SQL Server to cloud with minimal changes |
+----------------------------------------------------------+
| Azure DB for PostgreSQL Flexible Server                  |
|   Managed PostgreSQL (up to v16)                         |
|   Zone redundant HA, read replicas, built-in Citus       |
|   Use: open source preference, PostGIS, JSONB workloads  |
+----------------------------------------------------------+

NoSQL
+----------------------------------------------------------+
| Azure Cosmos DB                                          |
|   Multi-model, multi-region, 5 consistency levels        |
|   APIs: SQL, MongoDB, Cassandra, Gremlin, Table          |
|   Use: global distribution, variable consistency needs   |
|   Pricing: RU/s (Request Units per second)               |
|   Pitfall: RU capacity planning requires workload data   |
+----------------------------------------------------------+

CACHE / KEY-VALUE
+----------------------------------------------------------+
| Azure Cache for Redis                                    |
|   In-memory, sub-millisecond latency                     |
|   Clustering (C6/P5 tiers), persistence, geo-replication |
|   Use: session cache, result cache, pub/sub, rate limit  |
+----------------------------------------------------------+

ANALYTICS
+----------------------------------------------------------+
| Azure Synapse Analytics / Azure Databricks               |
|   See 07-DATA-PLATFORMS.md                               |
+----------------------------------------------------------+
```

---

## Storage Selection Decision Table

| Requirement | Storage Type | Azure Service |
|-------------|-------------|---------------|
| Static web content / CDN origin | Object | Blob (Hot tier) |
| Application binary artifacts / backups | Object | Blob (Cool tier) |
| Data lake for analytics (Spark/Databricks) | Object (hierarchical) | ADLS Gen2 |
| Long-term compliance archives | Object | Blob (Archive tier) |
| Database storage (high IOPS) | Block | Premium SSD v2 / Ultra Disk |
| VM OS disk | Block | Standard/Premium SSD |
| Windows file server replacement (SMB, AD auth) | File | Azure Files (Hot, AD join) |
| Shared volume across Kubernetes pods | File (NFS) | Azure Files (Premium NFS) |
| OLTP web application database | Relational | Azure SQL (General Purpose) |
| SQL Server lift-and-shift | Relational | Azure SQL Managed Instance |
| Global multi-region distributed database | NoSQL | Cosmos DB |
| Session cache, leaderboard, rate limiting | KV cache | Azure Cache for Redis |

---

## Common Confusion Points

**"Blob Storage is slow"**
Blob Storage GET requests from within the same Azure region are fast (single-digit ms latency). The latency perception comes from comparing to local disk. For sequential large-file reads (data lake analytics), Blob throughput is excellent. For random small-record reads (OLTP), use a database.

**"LRS is fine for production"**
LRS provides 11 9s durability within one datacenter. A datacenter fire/flood destroys all 3 copies. For production data that cannot tolerate regional failure, use GRS or GZRS. For non-critical or easily reproducible data, LRS is a reasonable cost trade-off.

**"Managed Disk IOPS is the only limit"**
VM size also has IOPS and throughput limits. A D4s_v5 can only sustain ~12,800 uncached IOPS regardless of how many Ultra Disks you attach. Profile the bottleneck before adding more expensive disk.

**"Cosmos DB is just Azure's version of MongoDB"**
Cosmos DB supports the MongoDB wire protocol as one of its APIs, but it is a completely different database engine underneath. The consistency models, partitioning model, RU pricing, and operational characteristics are distinct from MongoDB. The MongoDB API makes migration easier; it does not make them equivalent.
