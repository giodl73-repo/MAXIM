# Serverless: Azure Functions, Durable Functions, Cold Start, State Management

## The Big Picture

Serverless means you write function code; the platform handles provisioning, scaling, and lifecycle. You pay per execution, not per hour of idle time.

```
AZURE SERVERLESS SPECTRUM

  STATELESS COMPUTE — Azure Functions (code-first):
    Triggers: HTTP, Timer, Queue, Blob, Event Hub, Cosmos, etc.
    Hosting plans: Consumption, Elastic Premium, Dedicated (ASP).

  STATEFUL WORKFLOWS — Durable Functions (orchestrator + activities):
    Patterns: function chaining, fan-out/fan-in, async HTTP API,
              monitor, human interaction.
    Storage: Azure Storage queues + Table (Durable task framework).

  INTEGRATION — Logic Apps (low-code, 200+ connectors):
    Designer: visual flow canvas.

  CONTAINER APPS:
    KEDA-based scale-to-zero containers.
```

---

## Azure Functions: Core Model

### Trigger Types

```
TRIGGER TYPES AND USE CASES
+----------------------------------------------------------+
| HTTP Trigger         | REST API endpoint, webhook        |
|                      | Input: HTTP request               |
|                      | Output: HTTP response             |
+----------------------------------------------------------+
| Timer Trigger        | Scheduled execution (cron)        |
|                      | Input: timer info                 |
|                      | Use: nightly reports, cleanup     |
+----------------------------------------------------------+
| Blob Trigger         | Fire when blob created/updated    |
|                      | Input: blob content               |
|                      | Use: image processing, ETL        |
+----------------------------------------------------------+
| Queue Trigger        | Process Azure Storage Queue msg   |
|                      | At-least-once delivery            |
|                      | Use: background work items        |
+----------------------------------------------------------+
| Service Bus Trigger  | Process Service Bus queue/topic   |
|                      | Sessions supported, DLQ           |
+----------------------------------------------------------+
| Event Hub Trigger    | Process event streams (batched)   |
|                      | Consumer group per function app   |
|                      | Use: telemetry, IoT, streaming    |
+----------------------------------------------------------+
| Cosmos DB Trigger    | Change feed: new/updated docs     |
|                      | Use: real-time sync, projections  |
+----------------------------------------------------------+
| Event Grid Trigger   | React to Azure events             |
+----------------------------------------------------------+
| Durable Trigger      | Orchestrator + activity starters  |
|                      | (see Durable Functions section)   |
+----------------------------------------------------------+
```

### Hosting Plans: The Critical Decision

```
CONSUMPTION PLAN:
  Scale to zero: no cost when idle
  Scale out: automatically, up to 200 instances
  Cold start: first invocation after idle → ~200ms-1s warmup
  Timeout: 5 minutes default, 10 minutes max
  VNet: NOT supported (can outbound via VNet Integration, but limited)
  Cost: per execution + GB-seconds
  Use: variable workloads, event-driven, dev/test

ELASTIC PREMIUM PLAN (Recommended for production):
  Pre-warmed instances: 1+ always-warm instances → no cold start
  Scale out: rapid elastic scale like Consumption
  Timeout: unlimited
  VNet Integration: full inbound and outbound VNet connectivity
  Private endpoints: can restrict inbound to VNet only
  Premium hardware: faster instances
  Cost: per vCPU-second (higher base cost, but warm instances)
  Use: production APIs, VNet-connected functions, no cold start requirement

DEDICATED (APP SERVICE PLAN):
  Runs on VMs you provision (not serverless)
  Always on: no cold start, no scale to zero
  Timeout: unlimited
  VNet: full support
  Cost: fixed per VM hour (pay whether idle or not)
  Use: when you have spare App Service Plan capacity; predictable,
       constant-load functions; running alongside App Service apps
```

### Cold Start Explained

```
COLD START:
  Function app has been idle → no instance running
  First request → trigger instance creation:
    Pull container image (or use cached layer)
    Start host process
    Load .NET / Node / Python runtime
    Load function code
    Handle request
  Time: 200ms (Node.js) to 1s+ (.NET with large dependencies)

COLD START MITIGATIONS:
  Elastic Premium: pre-warmed instances eliminate cold start
  Always Ready Instances (Container Apps): minimum instance count
  Keep-alive: timer trigger pings function every 2-4 min (hacky, costs money)
  Minimize dependencies: smaller packages = faster startup
  .NET NativeAOT: pre-compile to native, faster startup
  Container Functions (Premium): bring your own container image

LANGUAGES RANKED BY COLD START SPEED:
  JavaScript/TypeScript → fastest
  Python               → fast
  Java                 → slower (JVM startup)
  .NET isolated worker → moderate (improved in .NET 8 with NativeAOT)
```

---

## Durable Functions

Durable Functions is a stateful workflow extension on top of Azure Functions. It uses the Task Hub (Azure Storage) to persist orchestration state.

### Core Patterns

#### Function Chaining

```
[Orchestrator] → Activity1 → Activity2 → Activity3 → result

Orchestrator code:
  async function* orchestrator(context) {
    const result1 = yield context.callActivity("Activity1", input);
    const result2 = yield context.callActivity("Activity2", result1);
    const result3 = yield context.callActivity("Activity3", result2);
    return result3;
  }

Key: orchestrator is deterministic (can replay to reconstruct state)
     if it crashes mid-way, it replays from the beginning using stored event history
```

#### Fan-Out / Fan-In

```
[Orchestrator] → [Activity1A] → |
               → [Activity1B] → +→ [Aggregate] → result
               → [Activity1C] → |

// Process 100 items in parallel, wait for all:
const tasks = items.map(item => context.callActivity("Process", item));
const results = yield context.Task.all(tasks);
const aggregate = results.reduce(...);
```

#### Async HTTP API (Long-Running Polling)

```
POST /start-job
  → Creates orchestration instance
  → Returns HTTP 202 with status endpoint URL

GET /status/{instanceId}
  → Returns: Running / Completed / Failed + output
  → Caller polls until done
  → No timeouts: orchestration can run for days/months

USE: Long-running operations that exceed HTTP timeout
     Client polls for status (or use webhooks/Event Grid to notify)
```

#### Human Interaction (Approval Workflow)

```
[Orchestrator]
  → Send approval email (activity)
  → Wait for external event with timeout:
       event = yield context.waitForExternalEvent("Approved", timeout=3days)
  → If event received: continue
  → If timeout: escalate

EXTERNAL EVENT SENT BY:
  Approval API endpoint (someone clicks "Approve" in email link)
  → POST /runtime/webhooks/durabletask/instances/{id}/raiseEvent/Approved
  → Orchestrator resumes

USE: Approval workflows, human-in-the-loop processes
```

### Durable Functions Internals

```
HOW DURABLE FUNCTIONS MAINTAINS STATE:

Task Hub = Azure Storage Account:
  + Orchestration instances table
  + History table (event log per instance)
  + Work item queue (pending activities)
  + Control queue (orchestrator coordination)

REPLAY MECHANISM:
  Orchestrator function is replayed from scratch on each wakeup
  Uses event history to "fast-forward" past completed activities
  → Second invocation "calls" Activity1 → sees it's complete in history
    → returns cached result immediately (no actual call)
  → Continues to next yield

CONSTRAINT: Orchestrator code must be deterministic
  NO: DateTime.Now, Random, Guid.NewGuid() inside orchestrator
      (these give different values on replay)
  YES: context.currentUtcDateTime, context.newGuid()
  → Side effects (calls to external services, I/O) belong in activities
```

---

## State Management in Stateless Functions

By design, function instances are stateless. State must be externalized:

```
STATE MANAGEMENT PATTERNS

SESSION/USER STATE:
  Azure Cache for Redis → per-user session data
  Cosmos DB → user profile, preferences
  → Look up by user ID on each invocation

DISTRIBUTED LOCKS:
  Redis SETNX + TTL → lock acquisition/release
  Azure Blob leases → leader election, distributed lock
  Use: prevent concurrent processing of same item

IDEMPOTENCY:
  Store processed message IDs in Redis / Cosmos DB
  Before processing: check if ID already processed
  After processing: record ID
  → Safe to deliver at-least-once, process exactly-once

AGGREGATION STATE (event sourcing):
  Store events in Cosmos DB / Table Storage
  Compute aggregate on read (or maintain projection)
  Event store is the source of truth

DURABLE ENTITIES (new pattern):
  Stateful "actors" managed by Durable Functions
  Each entity has its own state in Task Hub
  Operations are serialized (no concurrent calls to same entity)
  Use: virtual actor model, counters, aggregates
```

---

## Azure Logic Apps vs. Functions

```
LOGIC APPS:
  Low-code integration platform
  200+ built-in connectors: Office 365, Salesforce, SAP, ServiceNow, etc.
  Visual designer (drag-and-drop)
  Built-in triggers: recurrence, HTTP, Event Grid, Service Bus, etc.
  When to use:
    Integrations with SaaS applications
    Line-of-business workflows
    Non-developer built automations
    Connector ecosystem value exceeds code flexibility need

AZURE FUNCTIONS:
  Code-first (C#, JavaScript, Python, Java, PowerShell, Go, Rust custom handler)
  Full programming model
  When to use:
    Complex business logic
    Custom algorithms
    Libraries not available in Logic Apps connectors
    High performance, sub-second latency

BOTH together:
  Logic Apps for orchestration + connector fan-out
  Functions as custom steps within Logic App ("Call Azure Function" action)
  Common pattern: Logic App handles SAP/Salesforce integration;
                  Function handles custom calculation/transformation
```

---

## Common Confusion Points

**"Consumption plan is always cheapest"**
Consumption is cheapest at low volume (pay per execution). At high sustained volume, Dedicated (App Service) plan may be cheaper (fixed cost, no per-execution charge). Model both before deciding.

**"Durable Functions = Azure Service Bus"**
Durable Functions is a workflow orchestrator with state persistence. Service Bus is a message broker. They solve different problems. Durable Functions uses Storage Queues internally for coordination — it is a higher-level abstraction.

**"Serverless is stateless"**
Serverless functions are stateless (no persistent memory across invocations). But serverless architectures manage state externally (Cosmos DB, Redis, Durable Functions entity). "Stateless execution model" does not mean "no state in the system."

**"Cold starts only happen once"**
Cold starts happen whenever a function has been idle long enough that instances scale to zero (Consumption plan). A function with occasional traffic can cold-start multiple times per day. Elastic Premium eliminates this with pre-warmed instances.

---

## Decision Cheat Sheet

| Scenario | Recommendation |
|----------|---------------|
| Event-driven processing, variable traffic | Functions (Consumption) |
| HTTP API, no cold start tolerance | Functions (Elastic Premium) |
| Long-running workflow (minutes to days) | Durable Functions |
| Fan-out/fan-in over large dataset | Durable Functions (fan-out pattern) |
| Human approval workflow | Durable Functions (human interaction pattern) |
| SaaS integration, connectors needed | Logic Apps |
| Scheduled background job | Functions (Timer trigger) |
| Container workload, scale to zero | Container Apps (KEDA-based) |
| Stateful microservice (actor model) | Durable Entities |
