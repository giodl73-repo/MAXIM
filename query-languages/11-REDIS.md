# Redis — Commands, Data Structures, and Modules

Redis is not a query language in the SQL sense — it's a command-based interface to in-memory data structures. It's the standard ephemeral store: cache, session store, rate limiter, pub/sub bus, distributed lock, leaderboard. Redis Stack adds modules: RediSearch (full-text + vector search), RedisJSON, RedisTimeSeries, RedisBloom. The "query language" is the combination of commands + Lua scripting for atomicity.

> **If you've used Azure Cache for Redis** — you've used `GET`/`SET`/`EXPIRE` and probably `INCR` for counters. That's maybe 5% of what Redis exposes. This guide covers the full command surface: typed data structures (Hash, List, Set, Sorted Set, Stream, HyperLogLog, Geospatial), persistence models (RDB/AOF), the single-threaded event loop that makes it fast, and the clustering topologies (Sentinel vs Cluster) that Azure Cache abstracts away from you. Azure Cache for Redis Premium and Enterprise tiers support all of this — most .NET teams just never reach it.

---

## 1. Big Picture — Where Redis Sits

```
┌──────────────────────────────────────────────────────────────────────┐
│                         Where Redis Sits                             │
│                                                                      │
│  App ──► Redis (in-memory) ──────────────────► responses in μs-ms    │
│   │                                                                  │
│   └──► PostgreSQL / SQL Server (on-disk) ────► responses in ms-s     │
│                                                                      │
│  Redis = primary store for ephemeral / hot data                      │
│  RDBMS = primary store for durable / relational data                 │
│                                                                      │
│  Use cases:                                                          │
│  ┌──────────────────────────────────────────────────────────────┐    │
│  │  Cache (aside, write-through, write-behind)                  │   │
│  │  Session storage  (user session → JSON blob by session ID)   │   │
│  │  Rate limiting    (INCR + EXPIRE per user/IP)                │   │
│  │  Distributed lock (SET NX + EX — Redlock algorithm)         │   │
│  │  Leaderboard      (Sorted Set by score)                      │   │
│  │  Pub/Sub          (fan-out messaging — fire-and-forget)      │   │
│  │  Job queue        (List LPUSH/BRPOP — BullMQ, Sidekiq)      │   │
│  │  Streams          (append-only log — Kafka-lite with ACK)    │   │
│  │  Vector search    (RediSearch KNN — RAG embeddings store)    │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                      │
│  Redis Stack modules:                                                │
│  ┌────────────────┬──────────────────────────────────────────────┐  │
│  │ RediSearch     │ Full-text + vector similarity search (KNN)   │  │
│  │ RedisJSON      │ Native JSON storage + JSONPath queries       │  │
│  │ RedisTimeSeries│ Time-series data with downsampling           │  │
│  │ RedisBloom     │ Probabilistic structures (Bloom, Cuckoo,     │  │
│  │                │ Count-Min Sketch, Top-K, HyperLogLog)        │  │
│  └────────────────┴──────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────┘
```

```
┌──────────────────────────────────────────────────────────────────────────┐
│                     Redis Data Structure Taxonomy                        │
│                                                                          │
│  ┌──────────────┬───────────────────────────────────────────────────┐    │
│  │  String      │ Bytes, integers, floats. GET/SET/INCR. O(1).      │   │
│  │              │ Use: cache values, counters, session tokens        │   │
│  ├──────────────┼───────────────────────────────────────────────────┤   │
│  │  Hash        │ Field→value map (flat row). HSET/HGET/HINCRBY.    │   │
│  │              │ O(1) per field. Use: objects, profiles, configs   │   │
│  ├──────────────┼───────────────────────────────────────────────────┤   │
│  │  List        │ Doubly linked list. LPUSH/RPUSH/BRPOP. O(1)       │   │
│  │              │ push/pop. Use: queues, stacks, activity feeds      │   │
│  ├──────────────┼───────────────────────────────────────────────────┤   │
│  │  Set         │ Unordered unique members. SADD/SINTER/SUNION.     │   │
│  │              │ O(1) add/member. Use: tags, unique visitors,      │   │
│  │              │ follow graphs                                       │ │
│  ├──────────────┼───────────────────────────────────────────────────┤   │
│  │  Sorted Set  │ Members + float score, sorted. ZADD/ZRANGE.        │   │
│  │  (ZSET)      │ O(log N). Use: leaderboards, priority queues       │   │
│  ├──────────────┼───────────────────────────────────────────────────┤   │
│  │  HyperLogLog │ Probabilistic cardinality estimator. PFADD.       │   │
│  │              │ O(1), 12KB max. Use: unique visitor counts        │   │
│  ├──────────────┼───────────────────────────────────────────────────┤   │
│  │  Geospatial  │ Lat/lon members via ZSET + geohash encoding.       │   │
│  │              │ GEOADD/GEOSEARCH. O(log N). Use: proximity         │   │
│  ├──────────────┼───────────────────────────────────────────────────┤   │
│  │  Stream      │ Append-only log with consumer groups + ACK.       │   │
│  │              │ XADD/XREADGROUP. O(1) append. Use: event log,     │   │
│  │              │ durable queue                                       │ │
│  └──────────────┴───────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────────┘
```

```
┌──────────────────────────────────────────────────────────────────────────┐
│             Redis Execution Model — Single-Threaded Event Loop           │
│                                                                          │
│  Client A ──┐                                                            │
│  Client B ──┼──► epoll/kqueue ──► Event Loop ──► Command Executor        │
│  Client C ──┘    (I/O mux,        (single         (one command at        │
│                   all sockets)     thread)          a time, in RAM)      │
│                                        │                                 │
│                                        ▼                                 │
│                              Responses queued back                       │
│                              to client sockets                           │
│                                                                          │
│  Key consequence: every command is serialized — no locks, no mutexes,    │
│  no deadlocks. Atomicity is structural, not lock-based.                  │
│                                                                          │
│  Redis 6.0+: network I/O is multithreaded (reading from / writing to     │
│  sockets). Command execution is still single-threaded.                   │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Snapshot

| Attribute | Value |
|-----------|-------|
| Created | Salvatore Sanfilippo (2009), now Redis Ltd |
| License | RSALv2 (changed from BSD in 2024 — check your use case; Valkey fork maintains BSD) |
| Current version | Redis 7.x |
| Persistence | RDB snapshots + AOF (append-only file) + no persistence (cache-only mode) |
| ACID | Single command: atomic. Lua scripts: atomic. MULTI/EXEC: command queue (not SQL ACID — no rollback) |
| Clustering | Redis Cluster (hash slot sharding), Sentinel (HA), standalone |
| Cloud | Azure Cache for Redis, AWS ElastiCache, Upstash (serverless), Redis Cloud |
| T-SQL bridge | No JOIN, no schema, no SQL — closest analogy is a key-indexed in-memory hash table with typed values |

---

## 3. Key Naming Conventions

```
# Keys are arbitrary strings — convention matters for namespacing and SCAN patterns
# Pattern: entity:id:field   or   namespace:entity:id

user:1001:profile           # user 1001's profile JSON
user:1001:session           # user 1001's session data
session:abc123def456        # session by session token
rate:limit:user:1001        # rate limit counter for user 1001
rate:limit:ip:192.168.1.1   # rate limit by IP
cache:product:sku:W123      # cached product data
lock:payment:order:9876     # distributed lock for order processing
leaderboard:2024-01         # January 2024 leaderboard (Sorted Set)
queue:email:send            # email job queue (List)
stream:orders               # orders stream (append-only log)
```

---

## 4. String Commands — The Swiss Army Knife

```redis
# Basic get/set
SET   key value
SET   key value EX 3600       # expire in 3600 seconds (TTL)
SET   key value PX 60000      # expire in 60000 milliseconds
SET   key value NX            # set only if NOT exists (distributed lock pattern)
SET   key value XX            # set only if EXISTS
SET   key value GET           # set and return old value (Redis 6.2+)

GET   key                     # returns value (nil if not exists)
MGET  key1 key2 key3          # get multiple keys in one round trip
MSET  key1 val1 key2 val2     # set multiple keys atomically

# Atomic increment — rate limiting, counters
INCR        key               # increment integer by 1 (creates key=1 if absent)
INCRBY      key 5             # increment by 5
INCRBYFLOAT key 1.5           # increment float
DECR        key
DECRBY      key 3

# TTL management
EXPIRE   key 3600             # set/update TTL in seconds
PEXPIRE  key 60000            # set TTL in milliseconds
TTL      key                  # remaining TTL (-1 = no TTL, -2 = key doesn't exist)
PTTL     key                  # remaining TTL in milliseconds
PERSIST  key                  # remove TTL, make persistent

# Key introspection
EXISTS  key                   # 1 if exists, 0 if not (also counts: EXISTS k1 k2 k3)
TYPE    key                   # string | list | set | zset | hash | stream
DEL     key1 key2             # delete synchronously
UNLINK  key1 key2             # delete asynchronously (background — for large values)
RENAME  key newkey

# Scanning — safe vs unsafe
KEYS pattern                  # DANGER: O(N) full scan, blocks single-threaded Redis — never in production
SCAN cursor [MATCH pattern] [COUNT hint]  # iterative cursor-based scan (safe)
# SCAN returns a cursor; iterate until cursor == 0
```

---

## 5. Hash Commands — Flat Object Storage

```redis
# Hash = map of {field: value} — like a flat, schemaless row
# Use for: user profiles, product data, config objects

HSET    user:1001 name "Alice" email "alice@example.com" age 30
HGET    user:1001 name                      # "Alice"
HGETALL user:1001                           # returns all fields + values interleaved
HMGET   user:1001 name email               # fetch multiple fields in one call

HEXISTS   user:1001 email                  # 1 if field exists
HDEL      user:1001 age                    # delete one field
HLEN      user:1001                        # number of fields
HKEYS     user:1001                        # all field names
HVALS     user:1001                        # all field values

HINCRBY      user:1001 login_count 1       # atomic increment on numeric field
HINCRBYFLOAT user:1001 balance 10.50

# TTL note: TTL is per-key (the whole hash), NOT per-field
```

**SQL Server In-Memory OLTP bridge:** If you've used SQL Server in-memory OLTP (Hekaton) tables for hot lookup data — memory-optimized tables with hash or range indexes, sub-millisecond access, durability traded for speed — Hash is the Redis equivalent. It's a flat key-value structure with no schema enforcement, field-level atomic operations (`HINCRBY`), and sub-millisecond access. The difference: Hekaton still gives you SQL semantics (transactions, schema, joins within the engine). Redis Hash is the pure in-memory key-value case with no query engine. Both are the right tool when you need structured hot data that's too slow to round-trip from disk.

---

## 6. List Commands — Queue and Stack

```redis
# List = doubly linked list — O(1) push/pop at head or tail, O(N) by index
# Use for: job queues, activity feeds, bounded recent-items lists

LPUSH  queue:jobs "job1" "job2"     # push to LEFT (head) — stack behavior if paired with LPOP
RPUSH  queue:jobs "job3" "job4"     # push to RIGHT (tail) — FIFO queue if paired with LPOP
LPOP   queue:jobs                   # pop from left (non-blocking)
RPOP   queue:jobs                   # pop from right (non-blocking)
LLEN   queue:jobs                   # length
LRANGE queue:jobs 0 -1              # all elements (0=first, -1=last)
LRANGE queue:jobs 0 9               # first 10
LINDEX queue:jobs 0                 # element at index (O(N) — avoid in hot paths)

# Blocking pop — worker pattern
BRPOP  queue:jobs 0                 # block until element available, no timeout
BRPOP  queue:jobs 30                # block up to 30 seconds then return nil
BLPOP  queue:jobs 5

# Bounded recent-items pattern
LPUSH  recent:events "event-data"
LTRIM  recent:events 0 99           # keep only first 100 elements
# LPUSH + LTRIM together = bounded sliding window (use in pipeline for atomicity)
```

---

## 7. Set Commands — Unique Membership

```redis
# Set = unordered collection of unique strings
# Use for: tags, unique visitors, follow graphs, feature-flag user groups

SADD     user:1001:tags "premium" "beta" "power-user"
SREM     user:1001:tags "beta"
SMEMBERS user:1001:tags                   # all members (unordered — don't rely on order)
SISMEMBER  user:1001:tags "premium"       # 1 if member
SMISMEMBER user:1001:tags "premium" "beta"  # check multiple (Redis 6.2+)
SCARD    user:1001:tags                   # cardinality (count)
SRANDMEMBER user:1001:tags 3              # 3 random members (sampling)
SPOP     user:1001:tags                   # remove and return random member

# Set operations (return results or store in destination)
SUNION       set1 set2          # union
SINTER       set1 set2          # intersection
SDIFF        set1 set2          # difference (in set1 not in set2)
SUNIONSTORE  dest set1 set2     # store union result in dest key
SINTERSTORE  dest set1 set2
SDIFFSTORE   dest set1 set2
```

---

## 8. Sorted Set (ZSET) — Leaderboards and Priority Queues

```redis
# Sorted Set = unique members + a float score + sorted by score
# Use for: leaderboards, priority queues, time-ordered events (score = epoch ms)
# Internals: skip list + hash table — O(log N) add/remove/score-lookup

ZADD leaderboard 1000 "player:alice"       # add/update with score
ZADD leaderboard  850 "player:bob"
ZADD leaderboard NX  900 "player:carol"    # add only if member is new
ZADD leaderboard GT 1100 "player:alice"    # update only if new score > current (6.2+)
ZADD leaderboard LT  800 "player:bob"      # update only if new score < current (6.2+)

ZINCRBY leaderboard 50 "player:alice"      # atomic score increment
ZSCORE  leaderboard "player:alice"         # get score (nil if not member)
ZRANK   leaderboard "player:alice"         # 0-based rank, lowest score = rank 0
ZREVRANK leaderboard "player:alice"        # 0-based rank, highest score = rank 0 (leaderboards)
ZCARD   leaderboard                        # total member count

# Range queries — the power of sorted sets
ZRANGE leaderboard 0 9 WITHSCORES REV      # top 10, highest score first (Redis 6.2+ unified syntax)
ZREVRANGE leaderboard 0 9 WITHSCORES       # equivalent, older syntax
ZRANGEBYSCORE leaderboard 800 1000         # members with scores between 800 and 1000 (inclusive)
ZRANGEBYSCORE leaderboard "(800" "+inf"    # strictly > 800
ZRANGEBYSCORE leaderboard "-inf" "+inf" LIMIT 0 10   # paginated
ZRANGEBYLEX   leaderboard "[a" "[z"        # lexicographic range when scores are equal

# Removal
ZREM             leaderboard "player:bob"
ZREMRANGEBYSCORE leaderboard "-inf" 500    # remove all members with score < 500
ZREMRANGEBYRANK  leaderboard 0 9           # remove bottom 10 (lowest scores)

# Set operations on sorted sets
ZUNIONSTORE  dest 2 zset1 zset2            # union into dest
ZINTERSTORE  dest 2 zset1 zset2            # intersection into dest
ZDIFFSTORE   dest 2 zset1 zset2            # difference into dest (6.2+)
```

---

## 9. HyperLogLog — Probabilistic Cardinality Estimation

HyperLogLog answers: "how many distinct elements have I seen?" — without storing the elements. It uses ~12KB of memory regardless of cardinality and guarantees a standard error of 0.81%.

```redis
PFADD   pageviews:2024-01-15 "user:1001" "user:1002" "user:1001"
# Adds elements — duplicates are silently ignored. Returns 1 if internal state changed.

PFCOUNT pageviews:2024-01-15
# Returns estimated unique count. O(1).

PFMERGE pageviews:2024-01 pageviews:2024-01-14 pageviews:2024-01-15
# Merge multiple HLLs into a single one. Use for: "how many unique visitors this month?"
# The merged key can then be PFCOUNT'd.
```

**When to use:**
- "How many unique users visited this page today?" — you need approximate count, not exact, and storing a SET of every user ID is unacceptable at scale (millions of users = millions of keys per page per day).
- A/B test participation counts, unique impressions, distinct IP counters.

**When NOT to use:**
- Billing and compliance require exact counts — use a SET or a counter.
- Cardinality is small (< a few thousand) — a SET is more precise and still compact.

**SQL Server bridge:** `COUNT(DISTINCT column)` in SQL Server is exact but requires the engine to track all distinct values (hash aggregate or sort). SQL Server 2019+ added `APPROX_COUNT_DISTINCT` which uses a similar sketch-based algorithm internally and trades a small error margin for significantly reduced memory and CPU. HyperLogLog in Redis is the cache-layer version of the same tradeoff: O(1) memory, O(1) update, 0.81% error, no full enumeration.

---

## 10. Geospatial Commands — Proximity Queries

Geospatial in Redis is a thin layer over Sorted Set: coordinates are encoded as a 52-bit geohash and stored as the ZSET score. All the Sorted Set internals apply (skip list, O(log N) operations).

```redis
# GEOADD — store members with coordinates
GEOADD stores -122.4194 37.7749 "sf-store"
GEOADD stores  -73.9857 40.7484 "nyc-store"
GEOADD stores   -0.1278 51.5074 "london-store"

# GEODIST — distance between two members
GEODIST stores "sf-store" "nyc-store" km    # → ~4134 km
GEODIST stores "sf-store" "nyc-store" mi    # → ~2568 mi
# Units: m, km, mi, ft

# GEOPOS — retrieve coordinates of a member
GEOPOS stores "sf-store"                    # → [[-122.4194, 37.7749]]

# GEOSEARCH (Redis 6.2+ — replaces GEORADIUS)
# Find members within a circle from a point:
GEOSEARCH stores FROMLONLAT -122.4 37.7 BYRADIUS 500 km ASC COUNT 5 WITHCOORD WITHDIST
# Find members within a bounding box from an existing member:
GEOSEARCH stores FROMMEMBER "sf-store" BYBOX 1000 1000 km ASC COUNT 10

# Options:
#   ASC/DESC             — sort by distance
#   COUNT N              — limit results
#   WITHCOORD            — include lat/lon in results
#   WITHDIST             — include distance in results
#   STORE dest           — write results to a ZSET key
```

**Precision and limits:** Accuracy is approximately ±0.6m at the equator. Coordinates must be within -180 to +180 longitude, -85.05 to +85.05 latitude (Mercator projection limits). No polygon support — radius and bounding box only.

**Use case:** "Find the 5 nearest stores to a user at (lat, lon)" — a read on every request, fast, requires no schema.

**SQL Server bridge:** SQL Server handles this with `geography` columns + spatial indexes and `STDistance()`. The Redis approach is simpler for point-in-radius queries (one command vs a parameterized query + index seek) but lacks polygon containment, spatial joins, and multi-geometry operations. If you need `STContains`, `STIntersects`, or JOIN with non-spatial tables, SQL Server spatial wins. If you need "nearest N points to this coordinate" at sub-millisecond latency, Redis Geospatial wins.

---

## 11. Transactions — MULTI/EXEC

```redis
# MULTI/EXEC: queue commands, execute as a single atomic block
# No other client's commands interleave during EXEC
# NOT a SQL transaction: errors inside EXEC do not abort the batch — other commands still run
# NOT rollback: if SET fails, INCR that follows still executes

MULTI
INCR  counter
EXPIRE counter 3600
SET   last_reset "2024-01-15"
EXEC                              # execute all queued commands atomically

# DISCARD — throw away the queued command batch
MULTI
INCR counter
DISCARD                           # nothing executes

# WATCH — optimistic locking (Compare-And-Swap)
WATCH account:1001:balance        # watch this key for modification
# ... read balance in application code ...
# ... compute new balance ...
MULTI
SET account:1001:balance <newBalance>
EXEC
# If account:1001:balance changed between WATCH and EXEC,
# EXEC returns nil (transaction aborted — no commands ran)
# Retry the whole WATCH → compute → MULTI → SET → EXEC sequence on nil

# T-SQL bridge: MULTI/EXEC is closer to a batch than a transaction.
# No BEGIN TRAN / ROLLBACK equivalent. Atomicity ≠ isolation ≠ rollback.
```

---

## 12. Pub/Sub — Fire-and-Forget Messaging

```redis
# Publisher — any client, any time
PUBLISH notifications:user:1001 '{"type":"order_shipped","order_id":42}'
PUBLISH channel message

# Subscriber — connection is dedicated to subscription state while subscribed
SUBSCRIBE   notifications:user:1001
PSUBSCRIBE  notifications:user:*       # pattern subscribe (glob matching)
UNSUBSCRIBE notifications:user:1001
PUNSUBSCRIBE notifications:user:*

# Pub/Sub is fire-and-forget:
# - No persistence: messages not stored anywhere
# - No ACK: publisher has no confirmation of delivery
# - Offline subscribers miss all messages published while offline
# - No consumer groups, no replay

# T-SQL bridge: closer to MSMQ broadcast with no dead-letter queue
# For durable messaging → use Streams (section 13) or Azure Service Bus / Kafka
```

---

## 13. Streams — Durable Append-Only Log

```redis
# Stream: persistent, append-only log with consumer groups and ACK
# Similar to Kafka topics but embedded in Redis
# Unlike Pub/Sub: messages persist, consumers can replay, ACK required

# Produce — append to stream
XADD orders * customer_id 1001 total 99.99 status "pending"
# * = auto-generate ID: "<epoch_ms>-<sequence>" e.g. "1705312800000-0"
# Returns the generated message ID

# Read without consumer groups
XREAD COUNT 10 BLOCK 5000 STREAMS orders 0    # read from start, block up to 5s
XREAD COUNT 10 BLOCK 0    STREAMS orders $    # only new messages (block indefinitely)
XRANGE orders - + COUNT 10                    # range from beginning, first 10
XREVRANGE orders + - COUNT 10                 # reverse range (newest first)
XLEN orders                                   # message count

# Consumer groups — like Kafka consumer groups
XGROUP CREATE orders order-processors 0       # group starting from first message
XGROUP CREATE orders order-processors $       # group starting from new messages only

# Consume as group member
XREADGROUP GROUP order-processors worker-1 COUNT 10 BLOCK 5000 STREAMS orders >
# > = only messages not yet delivered to this group

# Acknowledge processed message
XACK orders order-processors 1705312800000-0

# Inspect and recover pending (unacknowledged) messages
XPENDING orders order-processors - + 10               # list pending messages
XCLAIM   orders order-processors worker-2 60000 1705312800000-0
# Reassign stale message (idle > 60s) from dead worker to worker-2

# Stream metadata
XINFO STREAM  orders
XINFO GROUPS  orders
XINFO CONSUMERS orders order-processors
```

**SQL Server Service Broker bridge:** If you've used SQL Server Service Broker, Streams are the Redis analog. The mapping is direct: durable queues → persistent stream; conversation groups → consumer groups; `BEGIN DIALOG` → `XGROUP CREATE`; poisoned message handling → `XPENDING`/`XCLAIM`; `END CONVERSATION` → `XACK`. One key structural difference: Service Broker is destructive-read (messages are consumed and removed). Streams are non-destructive — `XREADGROUP` marks messages as pending for that group's offset but the log entry persists. Multiple consumer groups can independently consume the same stream from different offsets. To bound stream size: `XADD orders MAXLEN ~ 100000 *` trims the stream to approximately 100K entries.

---

## 14. Lua Scripting — Atomic Compound Operations

```redis
# EVAL: execute Lua script atomically — no other commands interleave
# All Redis calls inside the script are part of one atomic operation
# KEYS[1]...KEYS[n]: key arguments; ARGV[1]...ARGV[n]: value arguments

# Pattern: atomic read-modify-write (impossible with MULTI/EXEC alone when logic is conditional)
EVAL "
    local current = redis.call('GET', KEYS[1])
    if not current then return 0 end
    if tonumber(current) < tonumber(ARGV[1]) then
        redis.call('SET', KEYS[1], ARGV[1])
        return 1
    end
    return 0
" 1 high_score 1500
# Sets high_score to 1500 only if current value < 1500 — atomically

# EVALSHA: run pre-loaded script by SHA1 (avoids resending script body on every call)
SCRIPT LOAD "return redis.call('GET', KEYS[1])"
# → returns SHA1 hash e.g. "e0e1f9fabfa9d353a55c628d0d0e5b6578a97c5b"
EVALSHA e0e1f9fabfa9d353a55c628d0d0e5b6578a97c5b 1 mykey

# SCRIPT FLUSH — clear script cache (after deploys)
SCRIPT FLUSH

# Note: Lua scripts should be fast — they block the single-threaded Redis event loop
# while running. No slow queries, no sleep(), no HTTP calls inside scripts.
```

---

## 15. Redis Stack Modules

### RediSearch — Full-Text and Vector Search

```redis
# Create a search index over Hash keys with a given prefix
FT.CREATE idx:products ON HASH PREFIX 1 product:
    SCHEMA
        name        TEXT        WEIGHT 5.0
        description TEXT
        price       NUMERIC     SORTABLE
        category    TAG         SEPARATOR ","
        embedding   VECTOR FLAT 6 TYPE FLOAT32 DIM 1536 DISTANCE_METRIC COSINE

# Full-text query
FT.SEARCH idx:products "@name:widget @category:{electronics}" LIMIT 0 10

# Numeric range filter
FT.SEARCH idx:products "@price:[10 100]"

# Combined text + numeric
FT.SEARCH idx:products "@name:widget @price:[0 50]" SORTBY price ASC LIMIT 0 10

# Vector similarity search (KNN — for RAG nearest-neighbor lookup)
FT.SEARCH idx:products "*=>[KNN 10 @embedding $query_vec AS score]"
    PARAMS 2 query_vec <binary_float32_array>
    SORTBY score
    RETURN 3 name price score

# Aggregation pipeline (GROUP BY + REDUCE — like SQL GROUP BY + aggregate functions)
FT.AGGREGATE idx:products "*"
    GROUPBY 1 @category
    REDUCE COUNT 0 AS count
    REDUCE AVG   1 @price AS avg_price
    SORTBY 2 @count DESC
```

### RedisJSON — Native Nested JSON

```redis
# Store and query JSON documents — supports JSONPath syntax
JSON.SET  user:1001 $ '{"name":"Alice","email":"a@b.com","preferences":{"theme":"dark"},"tags":[]}'
JSON.GET  user:1001 $.name                  # returns ["Alice"]
JSON.GET  user:1001 $.preferences.theme     # returns ["dark"]
JSON.SET  user:1001 $.preferences.theme '"light"'    # update nested field
JSON.NUMINCRBY user:1001 $.login_count 1    # atomic increment on numeric path
JSON.ARRAPPEND user:1001 $.tags '"power-user"'
JSON.ARRLEN    user:1001 $.tags
JSON.DEL       user:1001 $.preferences.theme

# RediSearch can index RedisJSON documents too:
FT.CREATE idx:users ON JSON PREFIX 1 user:
    SCHEMA $.name AS name TEXT $.email AS email TAG
```

---

## 16. Distributed Lock Pattern (Redlock)

```
# Single-node Redlock (simplified):

SET lock:payment:order:9876 <unique_token> NX EX 30
# NX  = set only if key does not exist (atomic check + set in one command)
# EX 30 = auto-expire after 30 seconds (safety release if worker crashes)
# Returns: OK (lock acquired) | nil (already locked)

# Release: only release if YOU own the lock (prevent releasing another worker's lock)
# Must use Lua for atomic check + delete:

EVAL "
    if redis.call('GET', KEYS[1]) == ARGV[1] then
        return redis.call('DEL', KEYS[1])
    else
        return 0
    end
" 1 lock:payment:order:9876 <unique_token>
# Returns 1 (released) or 0 (not your lock — don't release)

# Multi-node Redlock:
# Acquire on majority (⌊N/2⌋ + 1) of N independent Redis nodes
# within the lock validity time minus acquisition elapsed time
# If majority acquired → lock held; otherwise release all and retry

# T-SQL bridge: equivalent to sp_getapplock / application locks in SQL Server,
# but cross-process and cross-host without a DB connection
```

---

## 17. Persistence Models — RDB, AOF, and Hybrid

Redis is an in-memory database. Persistence is optional and configurable — choose based on your durability requirements.

### RDB — Point-in-Time Snapshots

RDB writes the entire dataset to disk as a compact binary snapshot at configured intervals.

```
# redis.conf
save 900 1      # save if at least 1 key changed in 900 seconds
save 300 10     # save if at least 10 keys changed in 300 seconds
save 60 10000   # save if at least 10000 keys changed in 60 seconds
dbfilename dump.rdb
dir /var/lib/redis
```

```redis
BGSAVE     # trigger a background save immediately — forks, child writes, parent keeps serving
LASTSAVE   # unix timestamp of the last successful save
```

**How BGSAVE works:** Redis forks the process. The child writes the snapshot using copy-on-write (COW) semantics — the parent's memory pages are shared until either process writes them. The fork itself is instantaneous, but the parent's memory footprint can transiently double under high write load during the save window (COW forces copies of modified pages).

**Durability:** You lose all writes since the last snapshot. If the configured interval is 900 seconds and Redis crashes 899 seconds in, that's up to 15 minutes of data loss.

### AOF — Append-Only File

AOF logs every write command to a sequential file. On restart, Redis replays the log to reconstruct the dataset.

```
# redis.conf
appendonly yes
appendfilename "appendonly.aof"

# fsync policy — the key durability/performance tradeoff:
appendfsync always      # fsync after every write: max durability, highest latency (~1 write/ms)
appendfsync everysec    # fsync once per second: default, lose at most 1 second of data
appendfsync no          # let the OS decide (typically 30s): fastest, least durable
```

**AOF rewrite:** The AOF grows unbounded as commands accumulate. `BGREWRITEAOF` compacts it by rewriting the minimal command set to reconstruct the current state. Auto-trigger:

```
auto-aof-rewrite-percentage 100   # rewrite when AOF is 100% larger than at last rewrite
auto-aof-rewrite-min-size 64mb    # minimum AOF size before considering auto-rewrite
```

### RDB + AOF Combined (Hybrid Format, Redis 7.0+)

Redis 7.0 introduced a hybrid AOF format: an RDB snapshot is embedded at the start of the AOF file, followed by incremental AOF records since that snapshot. This gives fast restart (RDB load) with minimal data loss (AOF tail). Enable with:

```
aof-use-rdb-preamble yes   # default in Redis 7.0+
```

### Durability Tradeoff Table

| Mode | Data Loss on Crash | Restart Speed | File Size | Use Case |
|------|-------------------|---------------|-----------|----------|
| No persistence | All data lost | Instant (empty) | None | Pure cache, ephemeral data |
| RDB only | Since last snapshot (minutes) | Fast (binary load) | Compact | Dev, acceptable-loss cache |
| AOF `always` | Zero (single command) | Slow (log replay) | Large | Billing, compliance |
| AOF `everysec` | Up to 1 second | Medium | Medium-large | Standard production |
| RDB + AOF | Up to 1 second | Fast (RDB + short AOF tail) | Medium | Production recommendation |

**SQL Server bridge:** RDB ≈ a database backup (`BACKUP DATABASE`). AOF ≈ the transaction log (`*.ldf`). Running both RDB + AOF is the Redis equivalent of a full backup + log backup chain: the RDB is your full backup baseline, the AOF covers the delta since the last snapshot. Azure Cache for Redis Premium tier exposes data persistence — you configure this directly in the portal.

---

## 18. Single-Threaded Event Loop Model

Understanding why Redis is fast despite single-threading is the key mental model that separates Redis users from Redis architects.

```
┌─────────────────────────────────────────────────────────────────────┐
│                   Redis Event Loop (Single Thread)                  │
│                                                                     │
│  10,000 client connections                                          │
│       │                                                             │
│       ▼                                                             │
│  ┌─────────────┐    all sockets registered with OS                  │
│  │ epoll/kqueue│◄── epoll_wait() returns readable sockets           │
│  └──────┬──────┘                                                    │
│         │  readable events dispatched one at a time                │
│         ▼                                                           │
│  ┌─────────────────────────────────────────────────┐               │
│  │              Command Executor (1 thread)        │               │
│  │                                                 │               │
│  │  GET key  →  hash lookup  →  O(1)  →  done      │               │
│  │  ZADD key →  skip list insert → O(log N) → done │               │
│  │  EVAL ... →  Lua interpreter → atomic → done    │               │
│  └─────────────────────────────────────────────────┘               │
│         │                                                           │
│         ▼                                                           │
│  Responses written back to client socket buffers                   │
│                                                                     │
│  Redis 6.0+: network I/O (read from sockets, serialize responses)  │
│  is handled by a configurable thread pool. Command execution       │
│  is still single-threaded.                                         │
└─────────────────────────────────────────────────────────────────────┘
```

**Why single-threaded is fast:**
- No lock contention. Mutexes, semaphores, and condition variables have measurable overhead. When there's one thread, there's nothing to synchronize.
- CPU cache locality. The working dataset is hot in L1/L2 cache. Context switches between threads thrash the cache.
- All operations are O(1) or O(log N) by design. Performance comes from algorithm choice, not parallelism.
- Everything is in RAM. Disk I/O latency (the bottleneck that multithreading usually hides) is not in the critical path for reads.

**Blocking commands — clarifying the model:**

`BLPOP`, `BRPOP`, `BZPOPMIN` block the *calling client* without blocking the *server*. When a client issues `BRPOP queue 30`, the event loop registers the client as waiting on that key and moves on to serve other clients. No thread is sleeping. When a producer `LPUSH`es to the queue, the event loop wakes the waiting client.

**Commands that actually block everyone (never use in production):**

| Command | Why It Blocks | Alternative |
|---------|--------------|-------------|
| `KEYS *` | O(N) full scan over all keys | `SCAN` with cursor |
| `SMEMBERS` on large sets | O(N) serialize entire set | `SSCAN` |
| `LRANGE key 0 -1` on huge lists | O(N) | `LRANGE` with bounded range |
| `SORT` on large collections | O(N+M*log(M)) | Pre-sort with ZSET |
| Long Lua scripts | Single-threaded, no preemption | Break into smaller scripts |

**SQL Server bridge:** SQL Server runs on SQLOS, which implements cooperative multitasking: a scheduler with a worker pool, yield points, and the SQLOS task abstraction above OS threads. Multiple workers execute queries in parallel; the query optimizer chooses plans to exploit this. Redis's design inverts this entirely — one worker, no cooperation needed, no query optimizer, no parallel plans. The speed comes from eliminating scheduler overhead, not from parallelizing work.

---

## 19. Cluster Architecture — Redis Cluster and Sentinel

### Sentinel — High Availability for Single-Shard Deployments

Sentinel provides automatic failover for a standalone Redis instance (one master + replicas). It does not shard data.

```
┌─────────────────────────────────────────────────────────────────┐
│                      Sentinel Topology                          │
│                                                                 │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐                     │
│  │Sentinel 1│   │Sentinel 2│   │Sentinel 3│  ← quorum = 2     │
│  └────┬─────┘   └────┬─────┘   └────┬─────┘                   │
│       │              │              │                           │
│       └──────────────┼──────────────┘                          │
│                      │ monitors + elects                        │
│                      ▼                                          │
│              ┌───────────────┐                                  │
│              │  Master Redis │◄── clients connect via           │
│              └───────┬───────┘    Sentinel-aware client         │
│                      │ async replication                        │
│              ┌───────┴────────┐                                 │
│         ┌────┴────┐      ┌────┴────┐                           │
│         │Replica 1│      │Replica 2│                           │
│         └─────────┘      └─────────┘                           │
│                                                                 │
│  On master failure: Sentinels reach quorum → elect new master   │
│  → reconfigure replicas → notify clients via Sentinel API       │
└─────────────────────────────────────────────────────────────────┘
```

Use Sentinel when: you need HA for a single Redis instance, data fits on one node, you want automatic failover without manual intervention. Azure Cache for Redis Standard tier is Sentinel-managed (the replica pair with 99.9% SLA is a Sentinel cluster — Azure abstracts it).

### Redis Cluster — Horizontal Sharding + HA

Redis Cluster shards data across multiple master nodes using hash slots, with each master having its own replica(s).

```
┌──────────────────────────────────────────────────────────────────────┐
│                       Redis Cluster Topology                         │
│                                                                      │
│  16384 hash slots distributed across master nodes                    │
│                                                                      │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐       │
│  │  Master A        │  │  Master B        │  │  Master C        │    │
│  │  slots 0–5460    │  │  slots 5461–10922│  │  slots 10923–   │    │
│  │                  │  │                  │  │  16383           │    │
│  │  ┌─────────────┐ │  │  ┌─────────────┐│  │  ┌─────────────┐│    │
│  │  │  Replica A  │ │  │  │  Replica B  ││  │  │  Replica C  ││    │
│  │  └─────────────┘ │  │  └─────────────┘│  │  └─────────────┘│    │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘     │
│                                                                      │
│  Cluster-aware client:                                               │
│  GET user:1001  →  CRC16("user:1001") mod 16384 = slot 4394         │
│                 →  slot 4394 is on Master A  →  route to Master A   │
│                                                                      │
│  MOVED redirect: if client routes to wrong node, Redis returns       │
│  MOVED 4394 <master-a-addr> — client updates its slot map and       │
│  retries on the correct node.                                        │
└──────────────────────────────────────────────────────────────────────┘
```

**Hash slot routing:**

```
CRC16(key) mod 16384 = slot number
```

Every key maps to exactly one slot. Every slot is owned by exactly one master.

**Hash tags — controlling slot assignment:**

Braces in a key name designate the hash tag. Only the content inside `{}` is hashed.

```
{user:1001}.session  → hash "user:1001" → slot X
{user:1001}.cart     → hash "user:1001" → slot X (same slot)
{user:1001}.profile  → hash "user:1001" → slot X (same slot)
```

This guarantees all three keys land on the same node, enabling multi-key operations (`MGET`, `MSET`, `SINTERSTORE`) between them. Without hash tags, multi-key commands fail if keys span slots.

**Client redirect protocol:**

| Response | Meaning | Client action |
|----------|---------|---------------|
| `MOVED slot addr` | Slot permanently lives on this node | Update slot map, retry on new node |
| `ASK slot addr` | Slot is mid-migration (resharding in progress) | Send `ASKING` to new node, retry once; do not update slot map |

A cluster-aware client (StackExchange.Redis, Lettuce, redis-py with cluster mode) handles both redirects transparently.

**Replica reads:**

By default, reads go to masters. To read from replicas:

```redis
READONLY    # sent on a replica connection — enables reads for this connection
READWRITE   # reverts to master-only reads
```

Note: replica reads are eventually consistent — you may read stale data.

**Gossip protocol and failure detection:**

Cluster nodes exchange state with random peers every 100ms. Failure detection uses two stages:

- `PFAIL` (probable failure): a node doesn't respond to PING within `cluster-node-timeout`
- `FAIL` (confirmed failure): a majority of masters agree the node is unreachable → automatic failover begins, promoting the best replica

**Resharding:**

```bash
redis-cli --cluster reshard <any-cluster-node>:6379
# Interactive: specify source node, target node, number of slots to move
# Slots migrate online — no downtime. ASKING redirects handle in-flight requests.
```

**SQL Server bridge:** Redis Cluster is the Redis equivalent of SQL Server distributed partitioned views on linked servers — both shard horizontally by a shard key, both require the application (or client library) to be aware of where a given key lives, and both allow incremental resharding. The key difference: Redis Cluster's gossip-based membership is automatic; SQL Server distributed partitioned views require manual linked server configuration and have no built-in failover. Azure Cache for Redis Premium tier exposes cluster mode directly.

---

## 20. Azure Cache for Redis — Tiers and .NET Integration

### Tier Comparison

| Tier | SLA | Replication | Clustering | Persistence | Modules | Notes |
|------|-----|-------------|-----------|-------------|---------|-------|
| Basic | None | No | No | No | No | Dev/test only — no replica, no SLA |
| Standard | 99.9% | Yes (replica pair) | No | No | No | Sentinel-managed HA |
| Premium | 99.9% | Yes | Yes (up to 10 shards) | RDB + AOF | No | VNet injection, geo-replication (active-passive) |
| Enterprise | 99.9% | Yes | Yes | Yes | Redis Stack (RediSearch, RedisJSON, etc.) | Redis Enterprise OSS license |
| Enterprise Flash | 99.9% | Yes | Yes | Yes | Redis Stack | Hot+warm tiering: RAM + NVMe SSD |

**Geo-replication:**
- **Premium active-passive:** One primary region writes; secondary region(s) replicate asynchronously. Failover is manual. Read from secondary is supported. Replication lag is typically < 60 seconds.
- **Enterprise active-active:** Uses CRDT (conflict-free replicated data types) for multi-region writes. Last-write-wins for simple types; CRDT merge semantics for counters and sets. No manual failover needed — any region accepts writes. Requires Enterprise tier.

**Deployment topology options:**

| Option | When to Use |
|--------|------------|
| Azure Cache for Redis (managed) | Standard case — Microsoft manages patching, failover, monitoring |
| Redis on Azure VMs | Need control over Redis version, config, or custom modules not in managed service |
| Redis on AKS | Existing K8s investment, need Redis co-located with compute, fine with operator complexity |

**Networking — Private Endpoint vs VNet Injection:**

- **VNet Injection (Premium, legacy):** Cache is deployed into your VNet subnet. All traffic stays within the VNet. Requires subnet delegation, cannot move the cache after creation.
- **Private Endpoint (all tiers, modern approach):** Cache stays in Microsoft's network; a private IP in your VNet routes to it via Azure Private Link. No subnet delegation, can be added post-creation, works with DNS private zones. This is the current recommended pattern.

**StackExchange.Redis connection string (C# / .NET):**

```csharp
// NuGet: StackExchange.Redis

// Connection string format:
// <hostname>:<port>,password=<access-key>,ssl=True,abortConnect=False

string connectionString =
    "my-cache.redis.cache.windows.net:6380," +
    "password=<primary-access-key>," +
    "ssl=True," +
    "abortConnect=False";

// Singleton — ConnectionMultiplexer is thread-safe and expensive to create
private static readonly ConnectionMultiplexer _redis =
    ConnectionMultiplexer.Connect(connectionString);

// Usage
IDatabase db = _redis.GetDatabase();

await db.StringSetAsync("user:1001:name", "Alice", TimeSpan.FromHours(1));
string name = await db.StringGetAsync("user:1001:name");

// Hash
await db.HashSetAsync("user:1001", new HashEntry[]
{
    new HashEntry("name", "Alice"),
    new HashEntry("email", "alice@example.com")
});
HashEntry[] fields = await db.HashGetAllAsync("user:1001");

// Cluster mode: StackExchange.Redis handles MOVED/ASK redirects transparently
// No code change required between standalone and cluster configurations
```

**Port note:** Azure Cache for Redis uses port 6380 (TLS) by default, not the standard 6379. Non-TLS (6379) can be enabled but is disabled by default and not recommended.

---

## 21. Common Patterns Reference

```
Pattern                  Commands Used                     Notes
─────────────────────────────────────────────────────────────────────────────
Cache-aside              GET → miss → compute → SET EX     App manages cache population
Write-through cache      SET (cache) + INSERT (DB)         Write to both synchronously
Rate limiter             INCR key; EXPIRE key window        One INCR per request; window = TTL
Sliding window rate      ZADD (score=ts) + ZREMRANGEBYSCORE Clean old entries; ZCARD = count
Session store            SET session:<token> <json> EX      Serialize session as JSON
Distributed lock         SET NX EX + Lua release            See section 16
Leaderboard              ZADD + ZREVRANGE + ZREVRANK        Score = points, member = player ID
Job queue (FIFO)         RPUSH + BRPOP                      Producer RPUSH, consumer BRPOP
Job queue (priority)     ZADD (score=priority) + ZPOPMAX    Higher score = higher priority
Bounded recent list      LPUSH + LTRIM 0 N-1                Keep last N items
Unique visitor count     PFADD + PFCOUNT                    HyperLogLog — ~0.81% error
Bloom filter             BF.ADD + BF.EXISTS                 Probabilistic membership (RedisBloom)
Pub/Sub fan-out          PUBLISH + SUBSCRIBE                Fire-and-forget broadcast
Durable message queue    XADD + XREADGROUP + XACK           Streams — persistent with ACK
Vector store (RAG)       HSET embedding + FT.SEARCH KNN     RediSearch VECTOR field
Proximity search         GEOADD + GEOSEARCH                 Sorted Set geohash encoding
```

---

## 22. Decision Cheat Sheet

| Use Redis For | Do Not Use Redis For |
|---------------|----------------------|
| Cache (sub-ms reads, TTL-managed expiry) | Primary durable store (memory is finite, data loss possible) |
| Session storage (fast read, short TTL) | Complex relational queries (no JOIN, no schema, no query planner) |
| Rate limiting (INCR + EXPIRE — atomic) | Large datasets that exceed available RAM |
| Distributed locks (SET NX EX) | Multi-key ACID transactions with rollback semantics |
| Leaderboards (Sorted Set by score) | Compliance/audit data requiring guaranteed durability without careful AOF config |
| Job queues (List LPUSH/BRPOP) | Graph traversal or multi-table joins |
| Pub/Sub fire-and-forget fan-out | Ad-hoc queries across arbitrary key patterns (no query planner — SCAN + filter is brute force) |
| Durable event log (Streams + consumer groups) | Strong consistency across multiple keys without Lua scripting workaround |
| Vector search / RAG embeddings (RediSearch KNN) | Rich relationships: hierarchical data, many-to-many, foreign key integrity |
| Full-text search over cached objects (RediSearch) | Ordered relational reporting (aggregations, window functions, GROUP BY across dimensions) |
| Proximity queries (Geospatial GEOSEARCH) | |
| Unique cardinality at scale (HyperLogLog) | |

---

## 23. Common Confusion Points

**Redis is single-threaded for command execution.**
Each command is atomic by design — no client-side locking needed per individual command. Multiple connections queue behind the event loop. Long Lua scripts or large KEYS scans block everyone. Redis 6.0+ added threaded network I/O (reading/writing sockets) but command execution remains single-threaded.

**MULTI/EXEC is not a SQL transaction.**
EXEC always executes all queued commands. If command N fails (wrong type, wrong arg count), commands N+1 onward still run. There is no ROLLBACK. Use Lua scripts when conditional rollback logic is needed.

**SET NX EX is one atomic command — the old two-command pattern was broken.**
The legacy pattern `SETNX key val` followed by `EXPIRE key 30` had a race condition: process could crash between the two commands, leaving the lock permanent. `SET key val NX EX 30` is atomic. Always use the modern form.

**Pub/Sub vs Streams.**
Pub/Sub = fire-and-forget, no persistence, no history, offline subscribers miss everything.
Streams = persistent append-only log, consumer groups, ACK, replay from any offset.
If you need durability, use Streams. If you need at-most-once fan-out to currently-connected subscribers, use Pub/Sub.

**Hash vs RedisJSON.**
Hash is a flat map of string fields to string values — simple, no module required, no nesting.
RedisJSON handles nested structures, arrays, and JSONPath queries but requires the module.
For simple structured objects, Hash is sufficient and more portable.

**TTL is per-key, not per-field.**
You cannot set an expiry on an individual field within a Hash. TTL applies to the whole key. To expire individual fields, use separate keys each with their own TTL.

**KEYS is production-hostile.**
KEYS pattern does a full O(N) scan and blocks the Redis event loop while it runs. Against a 10M-key instance, this is seconds of blocked latency. Use SCAN with a cursor for any production key enumeration.

**Eviction policy must be explicit.**
By default Redis returns OOM errors when maxmemory is hit. For a cache, set `maxmemory-policy allkeys-lru` or `volatile-lru`. Misconfigured eviction means your cache becomes a memory leak.

**AOF vs RDB persistence trade-offs.**
RDB snapshots: compact, fast restore, but loses all writes since the last snapshot on crash.
AOF: logs every write command, configurable fsync (always / everysec / no), more durable, slower restore, larger files.
Production recommendation: use both. `appendfsync everysec` is the standard durability/performance balance.

**RSALv2 license (2024).**
Redis changed from BSD to RSALv2 + SSPL in March 2024. Restrictions apply to offering Redis as a managed service. If you're building a SaaS product that wraps Redis, review the license. Valkey (Linux Foundation fork of Redis 7.2, maintained by AWS/Google/Oracle/Ericsson) preserves the BSD license and is a drop-in replacement.

**Azure Cache for Redis exposes more than most .NET teams use.**
Basic/Standard/Premium tiers support the full Redis command surface: Sorted Sets, Streams, Lua, Pub/Sub, HyperLogLog, Geospatial, MULTI/EXEC — all of it. Enterprise tier adds Redis Stack modules (RediSearch, RedisJSON, RedisTimeSeries). Most .NET teams using Azure Cache treat it as a string key-value store with GET/SET/EXPIRE. The richer data structures are available without any tier upgrade (above Basic) and without deploying additional infrastructure.

**Data structure time complexity — why Redis is fast at scale.**

| Data Structure | Common Operations | Complexity |
|---------------|------------------|-----------|
| String | GET, SET, INCR | O(1) |
| Hash | HGET, HSET, HINCRBY | O(1) per field |
| Hash | HGETALL, HKEYS, HVALS | O(N) — N fields in the hash |
| List | LPUSH, RPUSH, LPOP, RPOP | O(1) |
| List | LINDEX, LINSERT | O(N) |
| Set | SADD, SREM, SISMEMBER | O(1) |
| Set | SMEMBERS, SUNION, SINTER | O(N) |
| Sorted Set | ZADD, ZREM, ZSCORE, ZRANK | O(log N) |
| Sorted Set | ZRANGE, ZRANGEBYSCORE | O(log N + M) — M returned members |
| HyperLogLog | PFADD, PFCOUNT | O(1) |
| Geospatial | GEOADD, GEODIST | O(log N) |
| Geospatial | GEOSEARCH | O(N+log N) |
| Stream | XADD | O(1) |
| Stream | XRANGE, XREAD | O(N) — N messages returned |

The performance argument is not "Redis is parallelized." It's "every operation is O(1) or O(log N), everything is in RAM, and there's no lock overhead." Those three facts together produce sub-millisecond latency at millions of operations per second on a single node.
