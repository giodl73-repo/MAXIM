# Databases — Modern Patterns Guide

## The Big Picture

The database landscape has fragmented — not because SQL is broken, but because different workloads genuinely need different storage models. PostgreSQL still handles 90% of cases well. The ecosystem around it has matured dramatically.

```
+------------------------------------------------------------------+
|                    DATABASE LANDSCAPE                            |
|                                                                  |
|  RELATIONAL (SQL)          DOCUMENT         KEY-VALUE / CACHE    |
|  ----------------          --------         ---------------      |
|  PostgreSQL ← king         MongoDB          Redis                |
|  MySQL / MariaDB           DynamoDB         Memcached            |
|  SQLite (embedded)         Firestore        Upstash (serverless) |
|  SQL Server (you know it)  CouchDB          DynamoDB             |
|                                                                  |
|  SEARCH                    GRAPH            VECTOR               |
|  ------                    -----            ------               |
|  Elasticsearch             Neo4j            pgvector (Postgres)  |
|  Typesense                 Amazon Neptune   Pinecone             |
|  Meilisearch               FalkorDB         Qdrant               |
|                                                                  |
|  ORM / QUERY LAYER                                               |
|  -----------------                                               |
|  Prisma      (type-safe, schema-first, the modern EF Core)       |
|  Drizzle     (SQL-first, lightweight, growing fast)              |
|  Knex        (query builder, no model layer)                     |
|  Kysely      (type-safe query builder, SQL in TS)                |
|  Raw SQL     (pg / mysql2 clients — always an option)            |
+------------------------------------------------------------------+
```

**Bridge from .NET**: You know SQL Server + ADO.NET + Entity Framework. That maps almost directly: SQL Server → PostgreSQL, ADO.NET → `pg` client, Entity Framework Core → Prisma. The concepts (migrations, DbContext, DbSet, LINQ-style queries) all have direct equivalents.

---

## PostgreSQL — The Modern Default

```
  WHY POSTGRES OVER SQL SERVER FOR NEW PROJECTS:

  +-------------------------+---------------------------+
  | SQL Server              | PostgreSQL                |
  +-------------------------+---------------------------+
  | License cost            | Free, open source         |
  | Windows-first           | Cross-platform            |
  | Azure SQL (managed)     | Supabase, Neon, AWS RDS,  |
  |                         | Azure Database for PG     |
  | T-SQL dialect           | Standard SQL + extensions |
  | Tight SSMS tooling      | pgAdmin, TablePlus, psql  |
  | IDENTITY columns        | SERIAL / GENERATED ALWAYS |
  | NVARCHAR                | TEXT (UTF-8 always)       |
  | JSON (good)             | JSONB (excellent)         |
  | No native arrays        | Native array types        |
  | Full-text search (ok)   | Full-text search (good)   |
  |                         | pgvector (AI embeddings)  |
  +-------------------------+---------------------------+

  SQL compatibility: ~90% of T-SQL knowledge transfers.
  Main syntax differences: string functions, date math, window functions.
  CROSS APPLY → LATERAL JOIN. TOP(n) → LIMIT n.

  Standard connection URL:
  postgresql://username:password@hostname:5432/dbname
  DATABASE_URL="postgresql://alice:secret@localhost:5432/myapp"
```

### PostgreSQL Data Types That Matter

```sql
  -- Core types
  INTEGER / BIGINT / SMALLINT    -- whole numbers
  NUMERIC(p,s) / DECIMAL         -- exact decimal (money, not FLOAT)
  REAL / DOUBLE PRECISION        -- floating point (scientific, not money)
  TEXT                           -- variable length, no size limit needed
  VARCHAR(n)                     -- same as TEXT with constraint
  BOOLEAN                        -- true/false (not BIT like SQL Server)
  TIMESTAMP WITH TIME ZONE       -- always store with TZ (UTC best practice)
  DATE / TIME
  UUID                           -- gen_random_uuid() built-in
  JSONB                          -- binary JSON, indexable, queryable
  ARRAY                          -- e.g., TEXT[], INTEGER[]
  SERIAL / BIGSERIAL             -- auto-increment (or use GENERATED ALWAYS)

  -- Useful Postgres-specific
  CITEXT                         -- case-insensitive text
  TSVECTOR                       -- full-text search
  INET / CIDR                    -- IP addresses
  INTERVAL                       -- time spans

  -- Best practices:
  Use TEXT, not VARCHAR(255)     -- no performance difference in PG
  Use BIGINT for IDs             -- INT runs out at 2.1 billion rows
  Use TIMESTAMPTZ                -- always store timezone-aware
  Use NUMERIC for money          -- never FLOAT/REAL for currency
  Use UUID for distributed IDs   -- no coordination needed across shards
```

---

## Prisma — The Modern ORM

Prisma is the Entity Framework Core equivalent for Node.js. Schema-first, type-safe, generates a typed client from your schema.

```
  EF CORE                          PRISMA
  -------                          ------
  DbContext                        PrismaClient
  DbSet<User>                      prisma.user
  Code-first migrations            prisma migrate
  Scaffold from DB                 prisma db pull
  modelBuilder.Entity<>()          schema.prisma
  LINQ queries                     Prisma query API
  .Include()                       include: { ... }
  .Where()                         where: { ... }
  .Select()                        select: { ... }
  .AsNoTracking()                  No tracking by default
  NuGet EntityFrameworkCore        npm prisma + @prisma/client
```

**ADO.NET connection pool → Prisma connection pool bridge**: In ADO.NET, the connection pool is managed by the runtime automatically — `SqlConnection.Open()` is O(1) because it draws from a pre-established pool, and this is transparent to application code. Developers rarely think about it unless tuning `Min Pool Size` / `Max Pool Size` in the connection string. `PrismaClient` does the same for long-running servers: default pool size is CPU cores × 2, managed automatically, transparent to query code.

The difference surfaces in **serverless deployments** and is the most common production footgun in Prisma:

```
  TRADITIONAL SERVER (long-running process):
  +------------------+
  | Node.js process  |  One PrismaClient instance
  | (Express)        |  Pool: 10 connections
  +------------------+  Reused across all requests

  SERVERLESS (each invocation may be a new instance):
  +------------------+  +------------------+  +------------------+
  | Function inst. 1 |  | Function inst. 2 |  | Function inst. 3 |
  | PrismaClient     |  | PrismaClient     |  | PrismaClient     |
  | Pool: 10 conns   |  | Pool: 10 conns   |  | Pool: 10 conns   |
  +------------------+  +------------------+  +------------------+
  ...up to 100 instances
        10                     10                     10          = 1000 connections
                                                                    Postgres default max: 100
                                                                    → CONNECTION EXHAUSTION

  The failure mode: traffic spike → 100 Lambda/Vercel invocations
  → 100 new PrismaClient pools → 1000 Postgres connections → crash.
  Postgres's default max_connections is 100.

  SOLUTIONS:
  PgBouncer          Self-hosted connection pooler. Multiplexes app
                     connections into fewer Postgres connections.
                     Sits between app and DB.

  Supabase pooler    Built-in PgBouncer mode. Transaction pooling.
                     Enable in Supabase dashboard.

  Neon serverless    HTTP-based Postgres driver — no persistent TCP
  driver             connection, no pool per function.

  Prisma Accelerate  Managed pooler + edge caching. Prisma's SaaS answer.
```

Recognize this pattern: it's the same class of problem as `SqlConnection` pool exhaustion under high concurrency in .NET — except in serverless it happens even at moderate traffic because the pool is not shared across instances.

### schema.prisma — The Central Definition

```prisma
  // schema.prisma
  generator client {
    provider = "prisma-client-js"
  }

  datasource db {
    provider = "postgresql"
    url      = env("DATABASE_URL")
  }

  model User {
    id        Int      @id @default(autoincrement())
    email     String   @unique
    name      String?
    role      Role     @default(USER)
    posts     Post[]
    profile   Profile?
    createdAt DateTime @default(now())
    updatedAt DateTime @updatedAt

    @@index([email])
  }

  model Post {
    id        Int      @id @default(autoincrement())
    title     String
    body      String
    published Boolean  @default(false)
    author    User     @relation(fields: [authorId], references: [id])
    authorId  Int
    tags      Tag[]
    createdAt DateTime @default(now())

    @@index([authorId])
    @@index([published, createdAt])
  }

  model Tag {
    id    Int    @id @default(autoincrement())
    name  String @unique
    posts Post[]
  }

  model Profile {
    id     Int    @id @default(autoincrement())
    bio    String
    user   User   @relation(fields: [userId], references: [id])
    userId Int    @unique
  }

  enum Role {
    USER
    ADMIN
    MODERATOR
  }
```

### Prisma Client — The Query API

```typescript
  import { PrismaClient } from '@prisma/client'
  const prisma = new PrismaClient()

  // FIND
  const user = await prisma.user.findUnique({ where: { id: 1 } })
  const user = await prisma.user.findUniqueOrThrow({ where: { id: 1 } })
  const users = await prisma.user.findMany()
  const users = await prisma.user.findMany({
    where: {
      role: 'ADMIN',
      createdAt: { gte: new Date('2024-01-01') }
    },
    orderBy: { name: 'asc' },
    skip: 20,
    take: 10,                    // OFFSET 20 LIMIT 10
    select: {                    // only these fields (like .Select())
      id: true,
      name: true,
      email: true,
    }
  })

  // RELATIONS — include (eager load, like .Include())
  const userWithPosts = await prisma.user.findUnique({
    where: { id: 1 },
    include: {
      posts: {
        where: { published: true },
        orderBy: { createdAt: 'desc' },
        take: 5,
      },
      profile: true,
    }
  })

  // CREATE
  const newUser = await prisma.user.create({
    data: {
      name: 'Alice',
      email: 'alice@example.com',
      profile: {
        create: { bio: 'Software engineer' }  // nested create
      }
    }
  })

  // UPDATE
  const updated = await prisma.user.update({
    where: { id: 1 },
    data: { name: 'Alicia' }
  })

  // UPSERT (INSERT ... ON CONFLICT UPDATE)
  const upserted = await prisma.user.upsert({
    where: { email: 'alice@example.com' },
    create: { email: 'alice@example.com', name: 'Alice' },
    update: { name: 'Alice Updated' },
  })

  // DELETE
  await prisma.user.delete({ where: { id: 1 } })
  await prisma.user.deleteMany({ where: { role: 'GUEST' } })

  // AGGREGATES
  const count = await prisma.user.count({ where: { role: 'ADMIN' } })
  const stats = await prisma.post.aggregate({
    _count: true,
    _avg: { viewCount: true },
    _max: { createdAt: true },
  })

  // GROUP BY
  const byRole = await prisma.user.groupBy({
    by: ['role'],
    _count: true,
  })
```

### Prisma Raw SQL Escape Hatch

```typescript
  // When the ORM can't express it cleanly
  const result = await prisma.$queryRaw<User[]>`
    SELECT u.*, COUNT(p.id) as post_count
    FROM "User" u
    LEFT JOIN "Post" p ON p."authorId" = u.id
    WHERE u."createdAt" > ${new Date('2024-01-01')}
    GROUP BY u.id
    HAVING COUNT(p.id) > 5
  `

  // $queryRaw uses tagged templates — parameters are safely escaped
  // No SQL injection risk with this pattern
```

---

## Migrations — Schema as Code

This is the most important operational practice. Schema changes must be versioned, reproducible, and tracked in git — exactly like code.

```
  THE PROBLEM WITHOUT MIGRATIONS:
  Dev: "I added a column to users"
  Everyone else: Deployment fails, tests fail, nobody knows why.

  WITH MIGRATIONS:
  Every schema change = a migration file = checked into git.

  PRISMA MIGRATION WORKFLOW:

  1. Edit schema.prisma (add field, table, index)

  2. npx prisma migrate dev --name add-user-bio
     → Compares schema to current DB state
     → Generates SQL migration file
     → Applies it to your dev DB
     → Regenerates Prisma Client

  3. Generated file: prisma/migrations/20240222_add_user_bio/migration.sql
     ALTER TABLE "User" ADD COLUMN "bio" TEXT;

  4. Commit migration file to git

  5. In CI/CD:
     npx prisma migrate deploy
     → Applies any unapplied migrations (in order)
     → Never runs dev mode (no generation, just applies SQL)
```

```
  MIGRATION FILES DIRECTORY:
  prisma/
    schema.prisma           Your current schema (source of truth)
    migrations/
      20240101_init/
        migration.sql       CREATE TABLE statements
      20240215_add_profile/
        migration.sql       CREATE TABLE "Profile" ...
      20240222_add_bio/
        migration.sql       ALTER TABLE "User" ADD COLUMN "bio" TEXT;

  Each migration is additive. You never edit a past migration.
  To undo: write a new migration that reverses the change.

  This is exactly how EF Core migrations work.
  Same concept, different tooling.
```

### Dangerous Migration Patterns

```sql
  SAFE (non-breaking):
  ADD COLUMN bio TEXT                    -- nullable, no default needed
  ADD COLUMN count INT DEFAULT 0         -- has default
  ADD INDEX
  ADD TABLE
  CREATE TYPE (enum)

  RISKY (requires care):
  ADD COLUMN NOT NULL (no default)       -- fails if existing rows have no value
  RENAME COLUMN                          -- breaks ORM queries + app code
  CHANGE COLUMN TYPE                     -- may fail if data can't convert
  DROP COLUMN                            -- permanent data loss
  DROP TABLE                             -- permanent data loss

  SAFE RENAME PATTERN (3 deployments):
  1. Add new column, write to both old + new
  2. Migrate data, switch reads to new column
  3. Drop old column

  Always: run migrations against a production backup first.
  Always: have a rollback plan.
```

---

## Drizzle — The SQL-First Alternative

Drizzle is gaining fast on Prisma. Different philosophy: write SQL-like TypeScript, no separate schema file, lighter weight.

```typescript
  // schema.ts — schema defined in TypeScript
  import { pgTable, serial, text, boolean, integer, timestamp } from 'drizzle-orm/pg-core'
  import { relations } from 'drizzle-orm'

  export const users = pgTable('users', {
    id:        serial('id').primaryKey(),
    email:     text('email').notNull().unique(),
    name:      text('name'),
    createdAt: timestamp('created_at').defaultNow(),
  })

  export const posts = pgTable('posts', {
    id:        serial('id').primaryKey(),
    title:     text('title').notNull(),
    published: boolean('published').default(false),
    authorId:  integer('author_id').references(() => users.id),
  })

  export const usersRelations = relations(users, ({ many }) => ({
    posts: many(posts),
  }))
```

```typescript
  // querying
  import { db } from './db'
  import { users, posts } from './schema'
  import { eq, gte, desc } from 'drizzle-orm'

  // Reads like SQL, types flow through
  const result = await db
    .select({ id: users.id, name: users.name })
    .from(users)
    .where(eq(users.id, 1))

  const userWithPosts = await db.query.users.findFirst({
    where: eq(users.id, 1),
    with: { posts: true }
  })

  const recent = await db
    .select()
    .from(posts)
    .where(gte(posts.createdAt, new Date('2024-01-01')))
    .orderBy(desc(posts.createdAt))
    .limit(10)
```

```
  PRISMA vs DRIZZLE:

  +------------------+--------------------+--------------------+
  |                  | Prisma             | Drizzle            |
  +------------------+--------------------+--------------------+
  | Schema           | schema.prisma file | TypeScript file    |
  | Query API        | Object-based       | SQL-like           |
  | Bundle size      | Larger (client)    | Much smaller       |
  | Edge runtime     | Limited (Prisma    | Full support       |
  |                  | Accelerate needed) |                    |
  | Migrations       | prisma migrate     | drizzle-kit        |
  | Type safety      | Excellent          | Excellent          |
  | Raw SQL          | $queryRaw          | sql`` template     |
  | Maturity         | Mature (2019)      | Growing (2022)     |
  | Learning curve   | Lower              | Slightly higher    |
  +------------------+--------------------+--------------------+

  Pick Prisma if: you want EF Core familiarity, mature tooling, Studio UI.
  Pick Drizzle if: you want SQL control, edge runtime, smaller bundle.
```

---

## Connection Pooling

```
  THE PROBLEM:
  PostgreSQL handles ~100 connections well.
  Your app might have 10 serverless function instances,
  each with a PrismaClient holding 10 connections.
  That's 100 connections from one app. You'll hit limits fast.

  +------------------+         +------------------+
  | App instances    |         | PostgreSQL       |
  | (many)           |  -----> | max_connections  |
  |                  |  -----> | = 100 (default)  |
  | instance 1 ×10   |  -----> | Accepts 100      |
  | instance 2 ×10   |  -----> | simultaneous     |
  | instance 3 ×10   |  -----> | connections      |
  | ...              |         |                  |
  +------------------+         +------------------+
  100 instances = 1000 connections = CRASH

  SOLUTION: Connection pooler sits between app and DB

  App instances → PgBouncer / Supabase pooler → PostgreSQL
                  (multiplexes many connections
                   into fewer DB connections)

  PRISMA + SERVERLESS:
  In serverless (many short-lived functions), use:
  - PgBouncer (self-hosted)
  - Supabase built-in pooler (pgBouncer mode)
  - Neon serverless driver (HTTP-based, no persistent connection)
  - Prisma Accelerate (managed pooler + edge caching)

  For traditional long-running servers: PrismaClient manages
  its own pool automatically. Default pool size = CPU cores × 2.
```

---

## Redis — Not Just a Cache

Redis (Remote Dictionary Server) is an in-memory data structure store. "Cache" understates it.

**Bridge from .NET**: Redis has no single equivalent in the pre-cloud .NET world — these capabilities were scattered across multiple systems. The mapping:

```
  .NET EQUIVALENT                 REDIS CAPABILITY
  ---------------                 ----------------
  IMemoryCache                    Redis SET/GET with TTL
  (in-process, single server)     (distributed, survives process restart)

  IDistributedCache               Redis (via StackExchange.Redis)
  + StackExchange.Redis           The actual .NET Redis client library.
  (the standard .NET Redis client) Used with AddStackExchangeRedisCache().

  Azure Cache for Redis           Redis Cloud / Upstash
  (managed Redis on Azure)        (same product, different clouds)

  System.Runtime.Caching          Redis cache (more features, distributed)
  .MemoryCache

  SQL Server Service Broker       Redis Pub/Sub / Redis Streams
  (message queuing)               (lightweight real-time messaging)

  SQL Server in-memory OLTP       Redis sorted sets, hashes
  (fast key-value in SQL Server)  (purpose-built, simpler API)

  No equivalent                   Redis distributed locks (SET NX EX)
  No equivalent                   Redis rate limiting (INCR + EXPIRE)
  No equivalent                   BullMQ job queues (Redis-backed)

  The gap isn't that .NET had nothing — it's that these capabilities
  were scattered across IMemoryCache, Service Broker, SQL Server OLTP,
  and Azure Cache for Redis separately. Redis unifies them in one tool
  with a consistent O(1)-or-O(log n) API.
```

```
  REDIS USE CASES:

  CACHING (most common use)
  -------------------------
  Store expensive query results. TTL auto-expires them.
  GET /api/leaderboard  → check Redis → miss → query DB → store in Redis → return
  Next request          → check Redis → hit  → return (no DB query)

  SESSION STORAGE
  ---------------
  Store user sessions server-side.
  Key: session_abc123
  Value: { userId: 456, role: 'admin', expiresAt: ... }
  Fast O(1) lookup, auto-expire.

  RATE LIMITING
  -------------
  INCR user:123:requests:2024022214   → atomic increment
  EXPIRE user:123:requests:2024022214 3600
  IF count > 100 THEN reject request

  QUEUES / JOB QUEUES
  -------------------
  Push jobs to a list. Workers pop from the list.
  LPUSH jobs:email { to: "...", subject: "..." }
  BRPOP jobs:email 0  (blocking pop — wait for job)
  Libraries: BullMQ (Redis-backed job queue)

  PUB/SUB (real-time messaging)
  -----------------------------
  Publisher: PUBLISH channel:orders { orderId: 123, status: "shipped" }
  Subscriber: SUBSCRIBE channel:orders  → receives the message
  Lightweight real-time events.

  DISTRIBUTED LOCKS
  -----------------
  SET lock:resource:123 "process-abc" NX EX 30
  NX = only set if Not eXists (atomic check-and-set)
  EX = expire in 30s (auto-release if process dies)

  SORTED SETS (leaderboards, time-series)
  ----------------------------------------
  ZADD leaderboard 1500 "alice"
  ZADD leaderboard 2200 "bob"
  ZREVRANGE leaderboard 0 9 WITHSCORES  → top 10 with scores
```

### Redis in Node.js

```typescript
  import { createClient } from 'redis'

  const redis = createClient({ url: process.env.REDIS_URL })
  await redis.connect()

  // Basic cache pattern
  async function getCachedUser(id: number): Promise<User> {
    const cached = await redis.get(`user:${id}`)
    if (cached) return JSON.parse(cached)

    const user = await prisma.user.findUniqueOrThrow({ where: { id } })
    await redis.setEx(`user:${id}`, 300, JSON.stringify(user))  // 5 min TTL
    return user
  }

  // Cache invalidation on update
  async function updateUser(id: number, data: Partial<User>) {
    const user = await prisma.user.update({ where: { id }, data })
    await redis.del(`user:${id}`)   // bust the cache
    return user
  }

  // Rate limiting
  async function checkRateLimit(userId: number): Promise<boolean> {
    const key = `rate:${userId}:${Math.floor(Date.now() / 60000)}`  // per-minute key
    const count = await redis.incr(key)
    if (count === 1) await redis.expire(key, 60)
    return count <= 100
  }
```

---

## Managed Database Services

```
  LOCAL DEV:
  PostgreSQL in Docker (docker-compose.yml)
  SQLite (no server, single file — great for dev/testing)

  CLOUD OPTIONS:

  +------------------+----------------------------------------+
  | Service          | Notes                                  |
  +------------------+----------------------------------------+
  | Supabase         | Postgres + auth + storage + realtime   |
  |                  | Free tier. BaaS (Backend as a Service) |
  |                  | Open source, can self-host             |
  +------------------+----------------------------------------+
  | Neon             | Serverless Postgres. Scale to zero.    |
  |                  | Branch your database like git.         |
  |                  | Great for serverless / edge apps       |
  +------------------+----------------------------------------+
  | PlanetScale      | MySQL-compatible. Branching model.     |
  | (Vitess)         | Horizontal sharding built-in           |
  |                  | Changed pricing — verify current model |
  +------------------+----------------------------------------+
  | Azure Database   | Managed Postgres on Azure. Familiar    |
  | for PostgreSQL   | tooling, Azure integration, SLA        |
  +------------------+----------------------------------------+
  | AWS RDS /        | Managed Postgres/MySQL/SQL Server      |
  | Aurora           | Aurora = MySQL/PG compatible, faster   |
  +------------------+----------------------------------------+
  | Railway          | Simple Postgres + Redis. Good DX.      |
  | Render           | Simple managed services. Easy setup.   |
  +------------------+----------------------------------------+

  REDIS OPTIONS:
  Upstash         Serverless Redis. Per-request pricing. Great for Vercel.
  Redis Cloud     Official Redis managed service.
  Azure Cache     Managed Redis on Azure.
  for Redis
```

---

## NoSQL — When and Why

```
  THE HONEST ANSWER: most applications don't need NoSQL.
  Postgres with JSONB handles 90% of "schema flexibility" needs.

  GENUINE NoSQL USE CASES:

  DOCUMENT (MongoDB, DynamoDB, Firestore)
  Use when:
  - Schema varies wildly per document (product catalog with different
    attributes per category)
  - Write throughput is extreme (millions/sec — DynamoDB)
  - Data is naturally document-shaped with no joins needed
  - Mobile sync (Firestore's offline-first model)

  Don't use when: you need joins, transactions, or ACID guarantees.
  "Just use Postgres with JSONB" is often correct.

  KEY-VALUE (DynamoDB, Redis)
  Use when:
  - Simple lookups by key, massive scale
  - Session storage, caches, leaderboards
  - DynamoDB: serverless, infinite scale, millisecond latency

  SEARCH (Elasticsearch, Typesense, Meilisearch)
  Use when:
  - Full-text search with relevance ranking
  - Faceted search (filter by multiple attributes)
  - Typo tolerance, multilingual search
  Not a replacement for your main DB — a secondary index on top of it.

  GRAPH (Neo4j)
  Use when:
  - Relationships ARE the data (fraud detection, recommendations,
    social connections, knowledge graphs)
  - Queries that require traversing many hops: "friends of friends
    who bought X and aren't my existing customers"
  - Postgres recursive CTEs cover simple graph queries but struggle
    at depth.

  TIME SERIES (InfluxDB, TimescaleDB)
  Use when:
  - Append-only time-stamped data (metrics, IoT, telemetry)
  - TimescaleDB = Postgres extension (easier adoption)
```

---

## Common Confusion Points

### "ORM vs raw SQL — which is faster?"

```
  Raw SQL is faster. The question is whether the difference matters.

  ORM overhead is usually <5ms per query — irrelevant vs network latency.
  ORM wins on: correctness, type safety, maintainability, N+1 prevention.
  Raw SQL wins on: complex queries, bulk operations, DB-specific features.

  Pragmatic approach:
  - ORM (Prisma) for 80% of CRUD operations
  - Raw SQL ($queryRaw / sql``) for complex analytical queries
  - Never fight the ORM — use its escape hatch freely
```

### "What's the N+1 problem?"

```
  You fetch 10 users, then for each user you fetch their posts.
  That's 1 + 10 = 11 queries. With 1000 users it's 1001 queries.

  // N+1 problem:
  const users = await prisma.user.findMany()          // 1 query
  for (const user of users) {
    const posts = await prisma.post.findMany({         // N queries
      where: { authorId: user.id }
    })
  }

  // Fix: eager load with include
  const users = await prisma.user.findMany({
    include: { posts: true }                          // 2 queries total
  })
  // Prisma does: SELECT * FROM users; SELECT * FROM posts WHERE authorId IN (...)

  ORMs prevent N+1 when you use include/joins.
  GraphQL DataLoader solves N+1 for GraphQL resolvers.
```

### "JSONB vs separate table — when to embed?"

```
  EMBED IN JSONB WHEN:
  - Data is only read/written with its parent
  - Schema varies per row (product attributes, metadata)
  - No need to query/filter/index individual fields
  - Audit history, event payloads, config blobs

  SEPARATE TABLE WHEN:
  - You query/filter on the nested fields
  - Multiple rows share the same nested data (normalization)
  - You need foreign keys or referential integrity
  - You need to aggregate or join on nested data

  Postgres JSONB lets you index specific JSON paths:
  CREATE INDEX ON products ((attributes->>'color'));
  But it gets unwieldy. When querying JSON fields frequently,
  that's a signal to normalize into proper columns.
```

### "Migrations in production — how do teams handle this?"

```
  ZERO-DOWNTIME MIGRATION PRINCIPLES:

  1. Migrations run BEFORE code deploys (in CI/CD pipeline)
  2. New code must be backward-compatible with old schema
     (during rollout, old + new code may run simultaneously)
  3. Dangerous operations are split into multiple deployments:

     Deploy 1: ADD COLUMN bio TEXT (nullable, no default)
     Deploy 2: Backfill data, add NOT NULL constraint
     Deploy 3: Clean up old code paths

  4. Always test migrations on a production data snapshot first
  5. Blue/green deployments: run migrate on blue, swap traffic

  In Next.js with Vercel:
  - package.json: "build": "prisma migrate deploy && next build"
  - Migration runs atomically before new instances start
```

---

## Old World → New World Bridge

| ADO.NET / Entity Framework / SQL Server | Node.js / Prisma / PostgreSQL | Notes |
|---|---|---|
| `SqlConnection` / `SqlCommand` | `pg` client / Prisma `$queryRaw` | Raw DB access |
| `DbContext` | `PrismaClient` | The connection + query entry point |
| `DbSet<User>` | `prisma.user` | Table access object |
| `.Add()` / `SaveChanges()` | `prisma.user.create()` | Insert |
| `.Where()` | `where: { ... }` | Filter |
| `.Include()` | `include: { ... }` | Eager load related data |
| `.Select()` | `select: { ... }` | Project fields |
| `.FirstOrDefault()` | `findFirst()` | Single record or null |
| `.FindAsync(id)` | `findUnique({ where: { id } })` | By PK |
| `.AsNoTracking()` | Default in Prisma (no tracking) | Prisma has no change tracking |
| Code-first migrations | `prisma migrate dev` | Schema → SQL migration |
| `dotnet ef migrations add` | `prisma migrate dev --name` | Create migration |
| `dotnet ef database update` | `prisma migrate deploy` | Apply migrations |
| Scaffold from existing DB | `prisma db pull` | Generates schema from DB |
| LINQ aggregate `.Sum()` | `prisma.x.aggregate({ _sum: {...} })` | |
| `GROUP BY` / `.GroupBy()` | `prisma.x.groupBy({ by: [...] })` | |
| SQL Server IDENTITY | `@id @default(autoincrement())` | |
| `NEWID()` (SQL Server UUID) | `@default(uuid())` or `gen_random_uuid()` | |
| `GETUTCDATE()` | `@default(now())` | |
| Connection string in config | `DATABASE_URL` env var | |
| SSMS | TablePlus, pgAdmin, Prisma Studio | GUI clients |
| `NVARCHAR(MAX)` | `TEXT` | PG TEXT is unlimited, always UTF-8 |
| `BIT` | `BOOLEAN` | |
| `MONEY` / `DECIMAL` | `NUMERIC(p,s)` / Prisma `Decimal` | Never use FLOAT for currency |
| Stored procedures | Mostly avoided; raw SQL if needed | ORMs prefer application-side logic |
| SQL Server Agent jobs | pg_cron / BullMQ / cron jobs | Scheduled tasks |
| Always On / replication | Managed service handles this | Supabase/Neon/RDS manage HA |
| `IMemoryCache` | Redis (in-process → distributed) | `IMemoryCache` is single-server only |
| `IDistributedCache` + `StackExchange.Redis` | `redis` npm package (`createClient`) | The .NET Redis client; same concept |
| Azure Cache for Redis | Upstash / Redis Cloud | Managed Redis; same product, different cloud |
| `SqlConnection` pool (auto, transparent) | PrismaClient pool (auto for servers, footgun in serverless) | See Connection Pooling section |

---

## Decision Cheat Sheet

| I need... | Use |
|---|---|
| A relational database (new project) | PostgreSQL |
| An ORM with EF Core-like experience | Prisma |
| An ORM with SQL-first, edge support | Drizzle |
| Complex joins and SQL control | Prisma `$queryRaw` or Drizzle |
| Schema version control | Prisma migrate / Drizzle Kit |
| Managed Postgres (Azure) | Azure Database for PostgreSQL |
| Managed Postgres (Vercel/serverless) | Neon or Supabase |
| Serverless-friendly Postgres | Neon (HTTP driver), Supabase |
| Caching API responses | Redis (Upstash for serverless) |
| Session storage | Redis |
| Background job queue | BullMQ (Redis-backed) |
| Rate limiting | Redis INCR + EXPIRE |
| Real-time events / pub-sub | Redis Pub/Sub or Supabase Realtime |
| Flexible schema / embedded documents | Postgres JSONB |
| Full-text search with ranking | Typesense or Meilisearch (+ Postgres as source of truth) |
| Graph traversal queries | Neo4j or Postgres recursive CTEs (simple) |
| Time-series / metrics data | TimescaleDB (Postgres extension) |
| Mobile offline-first sync | Firestore or PocketBase |
| A dev database, zero setup | SQLite (via Prisma or Drizzle) |
| Visualize / edit data in browser | Prisma Studio (`npx prisma studio`) |
| Avoid serverless connection exhaustion | PgBouncer / Neon serverless driver / Prisma Accelerate |
