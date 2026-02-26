# Message Queues and Streaming: Kafka Architecture, At-Least-Once, Ordering

## The Big Picture

Message systems serve as the nervous system of distributed architectures. They decouple producers from consumers, provide durability, and enable asynchronous processing.

```
MESSAGE SYSTEM TAXONOMY
+-----------------------------------------------------------------------+
|                                                                       |
|  TRADITIONAL QUEUE          STREAMING LOG           EVENT GRID        |
|  +-------------------+     +------------------+     +-------------+  |
|  | RabbitMQ          |     | Apache Kafka     |     | Azure Event |  |
|  | Azure Service Bus |     | Azure Event Hubs |     | Grid        |  |
|  | Amazon SQS        |     | AWS Kinesis      |     |             |  |
|  +-------------------+     +------------------+     +-------------+  |
|  Message is consumed        Message stays in log    Publisher/sub    |
|  once then deleted.         until retention ends.   reactive event   |
|  Consumer acks/nacks.       Multiple consumer       routing          |
|  Point-to-point or pub/sub  groups, each tracks     HTTP push        |
|  with routing.              own offset.             to endpoints.    |
|                                                                       |
|  USE: Task queues           USE: Event sourcing,    USE: Reactive    |
|       work distribution          audit logs,             automation  |
|       retry / DLQ                stream processing       triggers    |
+-----------------------------------------------------------------------+
```

---

## Apache Kafka: Architecture Deep Dive

### Core Concepts

```
KAFKA COMPONENT HIERARCHY

Cluster
  └── Brokers (3–N nodes, each stores data)
        └── Topics (logical names: "user-events", "orders")
              └── Partitions (physical shards, 0 to N-1)
                    └── Segments (files on disk, rolling windows)
                          └── Records (offset, key, value, headers, timestamp)

RECORD:
  offset        → position in partition (monotonically increasing integer)
  key           → optional; controls which partition record goes to
  value         → actual payload (bytes; often Avro/JSON/Protobuf)
  headers       → metadata key-value pairs
  timestamp     → producer time or broker time
```

### Topic Partitioning and Ordering

```
TOPIC: "user-events" with 4 partitions

Producer(s)                            Consumers
  |                                        |
  | key="user123" → hash(key) % 4 = P1    |
  | key="user456" → hash(key) % 4 = P2    |
  | key=null      → round-robin           |
  |                                        |
  |---> Partition 0: [offset 0, 1, 2, ...]|
  |---> Partition 1: [offset 0, 1, 2, ...]| ---> Consumer Group A
  |---> Partition 2: [offset 0, 1, 2, ...]|       Consumer 1 reads P0, P1
  |---> Partition 3: [offset 0, 1, 2, ...]|       Consumer 2 reads P2, P3
                                            ---> Consumer Group B
ORDERING GUARANTEE:                               Consumer 3 reads P0
  Within a partition: strict order by offset      Consumer 4 reads P1
  Across partitions: NO ordering guarantee        Consumer 5 reads P2, P3

  → If you need all events for user123 in order:
    use user123 as key → all go to same partition
```

### Leader, Followers, and In-Sync Replicas (ISR)

```
PARTITION REPLICATION (replication-factor=3)

Broker 1 (Leader P0)    Broker 2 (Follower P0)   Broker 3 (Follower P0)
   |                          |                          |
   | Partition 0 data         | ISR: replicating         | ISR: replicating
   | offset 0..N              | offsets behind leader    | offsets behind leader
   |                          |                          |
Producer writes to LEADER only
Followers pull from leader (not push)
ISR (In-Sync Replicas): followers that are within replica.lag.time.max.ms of leader

HIGH-WATER MARK: the offset up to which all ISR members have replicated
  Consumers can only read up to the high-water mark
  Protects against reading uncommitted data
```

### Producer Acknowledgment Levels

```
acks=0: Producer does not wait for any acknowledgment
        → Fire and forget
        → Fastest, but data loss if broker crashes
        Use: metrics, logs where occasional loss is OK

acks=1: Wait for leader acknowledgment only
        → Leader writes to log, acks
        → Data loss if leader crashes before ISR replication
        Use: moderate throughput, tolerable rare loss

acks=all (acks=-1): Wait for all ISR replicas to acknowledge
        → min.insync.replicas=2 → need 2 ISR acks minimum
        → Highest durability, ~2x latency
        Use: transactional, financial, audit logs
```

---

## Exactly-Once Semantics

Kafka's delivery guarantees have evolved:

```
DELIVERY GUARANTEE LEVELS

AT-MOST-ONCE: Producer sends, does not retry on failure
  → Messages may be lost
  → Fastest producer path
  → Acceptable for: low-value events, approximated metrics

AT-LEAST-ONCE: Producer retries until ack received
  → Messages may be delivered more than once (on retry)
  → Consumer must be idempotent (handle duplicates)
  → Most common production pattern
  → Handle with idempotency key or deduplication

EXACTLY-ONCE: Kafka 0.11+ (2017)
  → Idempotent Producer: each producer gets a PID and sequence number
    → Broker deduplicates retries using PID + sequence
  → Transactions: atomic read-process-write across topics
    → Producer opens transaction
    → Writes to multiple partitions
    → Commits atomically (or aborts)
    → Consumers with isolation.level=read_committed only see committed
  → Cost: ~20% throughput reduction; transactional coordinator per group
```

### Idempotent Producer Internals

```
Producer PID (Producer ID, assigned by broker)
Sequence number (per partition, monotonically increasing)

ON RETRY:
  Producer sends (PID=42, seq=5, partition=P0, msg=X)
  Broker already received seq=5 for PID=42 on P0
  Broker deduplicates → does NOT write again
  Broker returns success

PITFALL: PID is reset on producer restart
  → Idempotency is only within a single producer session
  → Across restarts, use transactional.id for persistent deduplication
```

---

## Consumer Groups and Offset Management

```
CONSUMER GROUP: logical group of consumers sharing the work of a topic

PARTITION ASSIGNMENT (1 consumer per partition max):
  Topic: 4 partitions
  Group A: 4 consumers → each gets 1 partition
  Group A: 2 consumers → each gets 2 partitions
  Group A: 5 consumers → 4 active, 1 idle
  Group A: 1 consumer  → gets all 4 partitions

OFFSET TRACKING:
  Consumer tracks offset per partition
  Commits offset to __consumer_offsets topic (internal Kafka topic)
  Commit frequency:
    auto-commit (default, every 5s) → at-least-once semantics
    manual commit after processing  → at-least-once, controlled
    commit before processing        → at-most-once

CONSUMER LAG:
  lag = latest offset - consumer current offset
  Measure: consumer group lag metric
  Alert if lag exceeds threshold (consumer is falling behind)
  Tool: kafka-consumer-groups.sh --describe, or Burrow (LinkedIn)
```

---

## Log Compaction

Kafka supports two retention modes:

```
TIME/SIZE-BASED RETENTION:
  Delete segments older than retention.ms (default 7 days)
  or larger than retention.bytes
  → Clean tombstone: old events are gone

LOG COMPACTION:
  Keep only the latest value per key
  Tombstone record: key=X, value=null → X is deleted

  BEFORE:  offset 0: key=user1, val=profile_v1
           offset 3: key=user1, val=profile_v2
           offset 7: key=user2, val=profile_v1
  AFTER:   key=user1 → profile_v2 (latest only)
           key=user2 → profile_v1

  USE: Changelog topics for database-like semantics
       Kafka Streams state stores use compacted topics
       Configuration updates (always want latest per key)
```

---

## Kafka vs. Azure Event Hubs, Service Bus, Event Grid

| Dimension | Kafka | Azure Event Hubs | Azure Service Bus | Azure Event Grid |
|-----------|-------|-----------------|-------------------|------------------|
| Protocol | Kafka wire protocol | Kafka-compatible + AMQP/HTTPS | AMQP, HTTP | HTTP push |
| Model | Streaming log (partitions) | Streaming log (partitions) | Message queue/topic | Reactive event routing |
| Message retention | Hours to days to forever | 1–7 days (std), 90 days (premium) | Until consumed + TTL | Not stored (push) |
| Ordering | Per partition | Per partition | Per session (ordered sessions) | Not guaranteed |
| Consumer groups | Yes (parallel reads) | Yes (consumer groups) | Competing consumers | Subscriptions |
| Exactly-once | Yes (0.11+) | No | With deduplication | N/A |
| Scale | Very high (millions/sec) | High (millions/sec) | Moderate | High |
| Schema registry | Confluent Schema Registry | Azure Schema Registry | N/A | N/A |
| Best for | Event sourcing, stream processing | Telemetry ingestion, IoT, Kafka migration | Task queues, workflows, reliable messaging | Reactive automation, Azure resource events |

### Azure Event Grid vs. Event Hubs Distinction

This is a common confusion point:

```
AZURE EVENT GRID
  Publisher emits event → Grid routes to subscribers
  Subscribers are endpoints (Functions, Logic Apps, webhooks)
  At-least-once delivery with retry
  NOT a stream: no consumer group, no offset tracking
  USE: "Something happened, trigger a reaction"
  EXAMPLE: Blob created → trigger processing function

AZURE EVENT HUBS
  Producers send streams → Hub buffers in partitions
  Consumers read at their own pace (offset-based)
  Kafka-compatible API (your Kafka code works with Event Hubs)
  USE: High-throughput telemetry, log ingestion, streaming analytics
  EXAMPLE: IoT devices sending 1M events/sec → Spark reads for analytics

AZURE SERVICE BUS
  Full-featured message broker
  Queues (point-to-point) and Topics+Subscriptions (pub/sub)
  Message sessions (ordered, per-session delivery)
  Dead-letter queue (DLQ) for failed messages
  Long message TTL (days)
  USE: Reliable business process messaging, retry/DLQ requirements
  EXAMPLE: Order placed → payment service, fulfillment service both receive
```

---

## At-Least-Once Processing and Idempotency

At-least-once delivery is the practical default. Your consumer code must be idempotent:

```
IDEMPOTENCY PATTERNS

1. NATURAL IDEMPOTENCY: Operation is safe to repeat
   "Set status=COMPLETE for order 123"
   → Calling twice has same result as calling once

2. IDEMPOTENCY KEY: Deduplicate at target
   Include unique message-id in every write
   Target checks: "have I processed message-id X before?"
   If yes: skip, return success
   If no: process, record message-id
   Storage: Redis SET NX (set-if-not-exists), DB unique constraint

3. CONDITIONAL WRITES:
   "Update order IF status=PENDING" (optimistic concurrency)
   Second attempt: status is already COMPLETE, not PENDING → no-op
```

---

## Consumer Lag Monitoring

```
KAFKA CONSUMER LAG METRIC (per partition)

lag = log_end_offset - committed_offset

Example:
  Partition 0: latest=10000, committed=9995, lag=5    ← healthy
  Partition 1: latest=10000, committed=8000, lag=2000 ← growing lag
  Partition 2: latest=10000, committed=4000, lag=6000 ← critical

ALERT THRESHOLDS:
  Lag increasing → consumer is slower than producer → scale consumers
  Lag stable (small) → healthy
  Lag = 0 always → potentially too many consumers (idle capacity)

TOOLS:
  kafka-consumer-groups.sh --describe --group my-group
  Burrow (LinkedIn): time-series lag tracking with alerting
  Azure Monitor for Event Hubs: consumer lag metrics built-in
```

---

## Common Confusion Points

**"Kafka is a message queue"**
Kafka is an append-only log. Messages are not deleted on consumption. Multiple consumer groups can read the same messages independently. Traditional queues delete messages on consumption.

**"More partitions = more parallelism always"**
More partitions = more parallelism up to the number of consumers in a group. Beyond that, extra partitions are idle. Too many partitions (thousands) increases leader election time and metadata overhead.

**"Exactly-once means no duplicates ever"**
Kafka exactly-once is end-to-end only within Kafka (producer → broker → consumer within the transactional scope). If your consumer writes to an external database outside the transaction, you still need idempotency at that boundary.

**"Azure Event Hubs is Kafka"**
Azure Event Hubs is Kafka-protocol-compatible (you can use Kafka clients), but the managed infrastructure is different. Event Hubs does not support all Kafka features (some admin operations, compacted topics, Kafka Streams state stores differ). Most producer/consumer workloads work transparently.

---

## Decision Cheat Sheet

| Use Case | Recommendation |
|----------|---------------|
| High-throughput event stream, replay needed | Kafka or Event Hubs |
| Reliable task queue with DLQ and retry | Service Bus |
| Reactive automation (Azure resource events) | Event Grid |
| Event sourcing (store all events forever) | Kafka with compacted topics |
| Real-time analytics ingestion | Event Hubs → Stream Analytics / Spark |
| Cross-service async communication | Service Bus (queues) or Event Hubs (fan-out) |
| Ordering across all events | Not possible; use partition key to order within partition |
| Exactly-once across services | Saga pattern; use Kafka transactions within Kafka boundary |
