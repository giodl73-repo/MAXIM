# Redis — Commands, Data Structures, and Modules

Redis is not a query language in the SQL sense — it's a command-based interface to in-memory data structures. It's the standard ephemeral store: cache, session store, rate limiter, pub/sub bus, distributed lock, leaderboard. Redis Stack adds modules: RediSearch (full-text + vector search), RedisJSON, RedisTimeSeries, RedisBloom. The "query language" is the combination of commands + Lua scripting for atomicity.

---

## 1. Big Picture — Where Redis Sits

```
┌──────────────────────────────────────────────────────────────────────┐
│                         Where Redis Sits                             │
│                                                                      │
│  App ──► Redis (in-memory) ──────────────────► responses in μs-ms  │
│   │                                                                  │
│   └──► PostgreSQL / SQL Server (on-disk) ────► responses in ms-s   │
│                                                                      │
│  Redis = primary store for ephemeral / hot data                     │
│  RDBMS = primary store for durable / relational data                │
│                                                                      │
│  Use cases:                                                          │
│  ┌──────────────────────────────────────────────────────────────┐   │
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
│  │ RedisJSON      │ Native JSON storage + JSONPath queries        │  │
│  │ RedisTimeSeries│ Time-series data with downsampling            │  │
│  │ RedisBloom     │ Probabilistic structures (Bloom, Cuckoo,      │  │
│  │                │ Count-Min Sketch, Top-K, HyperLogLog)        │  │
│  └────────────────┴──────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────┘
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
# T-SQL bridge: a single Hash key is like one row from a key-value table,
#               but without schema enforcement

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

# Preference: use Hash over GET/SET for structured objects
# — avoids serialize/deserialize overhead, enables field-level operations
# — TTL note: TTL is per-key (the whole hash), NOT per-field
```

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

## 9. Transactions — MULTI/EXEC

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

## 10. Pub/Sub — Fire-and-Forget Messaging

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
# For durable messaging → use Streams (section 11) or Azure Service Bus / Kafka
```

---

## 11. Streams — Durable Append-Only Log

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

---

## 12. Lua Scripting — Atomic Compound Operations

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

## 13. Redis Stack Modules

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

## 14. Distributed Lock Pattern (Redlock)

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

## 15. Common Patterns Reference

```
Pattern                  Commands Used                     Notes
─────────────────────────────────────────────────────────────────────────────
Cache-aside              GET → miss → compute → SET EX     App manages cache population
Write-through cache      SET (cache) + INSERT (DB)         Write to both synchronously
Rate limiter             INCR key; EXPIRE key window        One INCR per request; window = TTL
Sliding window rate      ZADD (score=ts) + ZREMRANGEBYSCORE Clean old entries; ZCARD = count
Session store            SET session:<token> <json> EX      Serialize session as JSON
Distributed lock         SET NX EX + Lua release            See section 14
Leaderboard              ZADD + ZREVRANGE + ZREVRANK        Score = points, member = player ID
Job queue (FIFO)         RPUSH + BRPOP                      Producer RPUSH, consumer BRPOP
Job queue (priority)     ZADD (score=priority) + ZPOPMAX    Higher score = higher priority
Bounded recent list      LPUSH + LTRIM 0 N-1                Keep last N items
Unique visitor count     PFADD + PFCOUNT                    HyperLogLog — ~0.81% error
Bloom filter             BF.ADD + BF.EXISTS                 Probabilistic membership (RedisBloom)
Pub/Sub fan-out          PUBLISH + SUBSCRIBE                Fire-and-forget broadcast
Durable message queue    XADD + XREADGROUP + XACK           Streams — persistent with ACK
Vector store (RAG)       HSET embedding + FT.SEARCH KNN     RediSearch VECTOR field
```

---

## 16. Decision Cheat Sheet

| Use Redis For | Do Not Use Redis For |
|---------------|----------------------|
| Cache (sub-ms reads, TTL-managed expiry) | Primary durable store (memory is finite, data loss possible) |
| Session storage (fast read, short TTL) | Complex relational queries (no JOIN, no schema) |
| Rate limiting (INCR + EXPIRE — atomic) | Large datasets that exceed available RAM |
| Distributed locks (SET NX EX) | Long-term analytics (use a data warehouse) |
| Leaderboards (Sorted Set by score) | Multi-table ACID transactions with rollback |
| Job queues (List LPUSH/BRPOP) | Compliance/audit data requiring guaranteed durability |
| Pub/Sub fire-and-forget fan-out | Ordered relational reporting |
| Durable event log (Streams + consumer groups) | |
| Vector search / RAG embeddings (RediSearch KNN) | |
| Full-text search over cached objects (RediSearch) | |

---

## 17. Common Confusion Points

**Redis is single-threaded for command execution.**
Each command is atomic by design — no client-side locking needed per individual command. Multiple connections queue behind the event loop. Long Lua scripts or large KEYS scans block everyone.

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
