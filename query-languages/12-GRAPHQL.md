# GraphQL — Schema, Query Language, and API Patterns

GraphQL is not a database query language — it's an API query language. The client specifies exactly what data it needs in a hierarchical query; the server resolves it from any backing sources (databases, REST APIs, other services). It solves the over-fetching and under-fetching problems of REST. The query language has a schema (types + fields), queries (reads), mutations (writes), and subscriptions (real-time). It's the transport-layer equivalent of a typed SELECT (query), INSERT/UPDATE (mutation), and a live cursor (subscription) — but the schema lives at the API boundary, not the database.

---

## 1. Big Picture — GraphQL vs REST vs tRPC vs OData

```
┌──────────────────────────────────────────────────────────────────────────┐
│                   API Query Language Landscape                           │
│                                                                          │
│  REST (resource-based, URL-per-resource):                                │
│    GET /users/1           → returns ALL user fields (maybe 30 fields)   │
│    GET /users/1/orders    → second round-trip for orders                │
│    Problem: over-fetching + N round trips for N related resources       │
│                                                                          │
│  GraphQL (field-based, single endpoint):                                 │
│    POST /graphql                                                         │
│    { user(id: 1) { name, orders { id, total } } }                      │
│    → exactly these fields, one request, client drives shape             │
│                                                                          │
│  tRPC (TypeScript-first RPC):                                            │
│    No schema language — TypeScript IS the schema                        │
│    Type-safe without codegen, but TypeScript/Node-only ecosystem        │
│                                                                          │
│  OData (Microsoft's URL-based query):                                    │
│    GET /users?$select=name,email&$expand=orders&$filter=age gt 18      │
│    Query params in URL — REST + filter language                         │
│    Used in: Azure REST APIs, Dynamics 365, Power BI datasets            │
│    T-SQL bridge: if you've used Azure REST APIs or ADO.NET OData        │
│    adapters, you've already used OData                                  │
│                                                                          │
│  Where GraphQL fits architecturally:                                     │
│                                                                          │
│  ┌──────────┐     ┌─────────────────┐     ┌────────────────────────┐   │
│  │  Client  │────►│  GraphQL Layer  │────►│  Backing Data Sources  │   │
│  │ (mobile/ │     │  (schema +      │     │  - PostgreSQL / SQL Srv │   │
│  │  web/IoT)│◄────│   resolvers)    │◄────│  - REST microservices  │   │
│  └──────────┘     └─────────────────┘     │  - Redis / caches      │   │
│                                            │  - gRPC services       │   │
│                                            └────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Snapshot

| Attribute | Value |
|-----------|-------|
| Created | Facebook (2012 internal), open-sourced 2015 |
| Specification | graphql.org — language spec, not an implementation |
| Reference impl | graphql-js (JavaScript) |
| Server libraries | Apollo Server, graphql-js, Hasura, Strawberry (Python), Hot Chocolate (.NET), gqlgen (Go), graphql-ruby |
| Client libraries | Apollo Client, urql, Relay, graphql-request |
| Transport | Usually HTTP POST (single endpoint); WebSocket for subscriptions |
| Schema language | SDL (Schema Definition Language) — the IDL for your API |
| T-SQL bridge | SDL is to GraphQL what a database schema is to SQL — defines the type contract. REST is "stored procedures with URLs"; GraphQL is "dynamic SELECT from a typed schema with the client writing the projection." |

---

## 3. Schema — SDL (Schema Definition Language)

```graphql
# ── Scalar types (built-in primitives) ─────────────────────────────────
# String, Int, Float, Boolean, ID
# ID is a string semantically; signals "unique identifier", not numeric math

# ── Object types — the nouns of your API ───────────────────────────────
type User {
  id:        ID!           # ! = non-null (required, never null)
  name:      String!
  email:     String!
  age:       Int           # nullable (no !) — can be null in response
  orders:    [Order!]!     # non-null list of non-null Orders
  createdAt: String!
}

type Order {
  id:        ID!
  status:    OrderStatus!  # enum
  total:     Float!
  lineItems: [LineItem!]!
  customer:  User!         # back-reference — resolved by a separate resolver
}

type LineItem {
  product:  Product!
  quantity: Int!
  price:    Float!
}

# ── Enum ────────────────────────────────────────────────────────────────
enum OrderStatus {
  PENDING
  PROCESSING
  SHIPPED
  DELIVERED
  CANCELLED
}

# ── Input types — for mutations ─────────────────────────────────────────
# Cannot reuse regular output types as mutation inputs (SDL rule)
input CreateOrderInput {
  customerId: ID!
  lineItems:  [LineItemInput!]!
}

input LineItemInput {
  productId: ID!
  quantity:  Int!
}

# ── Interface — structural contract ────────────────────────────────────
# T-SQL bridge: like a C# interface or abstract base type
interface Node {
  id: ID!
}

type User implements Node {
  id:   ID!
  name: String!
}

# ── Union — one of several concrete types ──────────────────────────────
union SearchResult = User | Order | Product

# ── Custom scalar (optional) ────────────────────────────────────────────
scalar DateTime   # defined via scalar in SDL; serialization logic in resolver

# ── Root types — the entry points into the graph ───────────────────────
type Query {
  user(id: ID!): User                              # nullable — returns null if not found
  users(limit: Int, offset: Int): [User!]!         # paginated list
  search(query: String!): [SearchResult!]!         # union return
}

type Mutation {
  createOrder(input: CreateOrderInput!): Order!
  updateOrderStatus(id: ID!, status: OrderStatus!): Order!
  deleteOrder(id: ID!): Boolean!
}

type Subscription {
  orderStatusChanged(orderId: ID!): Order!
  newOrderCreated: Order!
}
```

---

## 4. Query Syntax — Client-Side Requests

```graphql
# ── Basic query — ask for exactly what you need ─────────────────────────
query GetUser {
  user(id: "1001") {
    id
    name
    email
    orders {
      id
      status
      total
    }
  }
}

# ── Variables — parameterized queries ────────────────────────────────────
# T-SQL bridge: equivalent to sp_executesql with @param = N'value'
query GetUser($userId: ID!) {
  user(id: $userId) {
    name
    email
  }
}
# Variables sent as separate JSON: { "userId": "1001" }

# ── Aliases — rename fields in response ──────────────────────────────────
query CompareOrders {
  firstOrder: order(id: "1") {
    id
    total
  }
  secondOrder: order(id: "2") {
    id
    total
  }
}
# Response: { "firstOrder": {...}, "secondOrder": {...} }

# ── Fragments — reusable field selections ────────────────────────────────
# T-SQL bridge: like a CTE that defines a reusable column list
fragment UserDetails on User {
  id
  name
  email
}

query GetUsers {
  activeUsers: users(filter: { status: ACTIVE }) {
    ...UserDetails        # spread fragment — replaced with id, name, email
  }
  pendingUsers: users(filter: { status: PENDING }) {
    ...UserDetails
  }
}

# ── Inline fragments — polymorphic queries ────────────────────────────────
# Required when querying union or interface types
query Search($term: String!) {
  search(query: $term) {
    __typename            # returns the concrete type name ("User", "Order", etc.)
    ... on User {
      name
      email
    }
    ... on Order {
      id
      total
      status
    }
    ... on Product {
      name
      price
    }
  }
}

# ── Directives — conditional field inclusion ─────────────────────────────
query GetUser($includeOrders: Boolean!, $skipAge: Boolean!) {
  user(id: "1001") {
    name
    email
    age   @skip(if: $skipAge)            # skip this field if skipAge == true
    orders @include(if: $includeOrders) {
      id
      total
    }
  }
}
# Built-in directives: @include(if: Boolean), @skip(if: Boolean), @deprecated(reason: String)
```

---

## 5. Mutations — Writes

```graphql
# Mutation — CREATE, UPDATE, DELETE
# Mutations are sequential within a single document (unlike queries, which are parallel)

mutation CreateOrder($input: CreateOrderInput!) {
  createOrder(input: $input) {
    id
    status
    total
    lineItems {
      product { name }
      quantity
      price
    }
  }
}
# Variables: { "input": { "customerId": "42", "lineItems": [{ "productId": "7", "quantity": 2 }] } }

mutation UpdateStatus($id: ID!, $status: OrderStatus!) {
  updateOrderStatus(id: $id, status: $status) {
    id
    status
    updatedAt
  }
}

# Multiple mutations in one document — guaranteed sequential (not parallel)
mutation BatchOps {
  createFirst:  createOrder(input: { customerId: "1", lineItems: [] }) { id }
  createSecond: createOrder(input: { customerId: "2", lineItems: [] }) { id }
  # createSecond runs only after createFirst completes
}

# NOTE: sequential does not mean transactional.
# If createFirst succeeds and createSecond fails, createFirst is NOT rolled back.
# Implement DB-level transactions inside the resolver if atomicity is required.
```

---

## 6. Subscriptions — Real-Time

```graphql
# Subscription — persistent connection, server pushes updates
# Transport: WebSocket (not HTTP) — different infrastructure from query/mutation

subscription OrderUpdates($orderId: ID!) {
  orderStatusChanged(orderId: $orderId) {
    id
    status
    updatedAt
  }
}
# Connection stays open
# Server pushes a new OrderUpdates payload each time the order's status changes

# Client (Apollo Client):
# const { data, loading } = useSubscription(ORDER_UPDATES, { variables: { orderId } });

# Infrastructure note:
# HTTP for query + mutation → stateless, horizontally scalable
# WebSocket for subscription → stateful, requires sticky sessions or a pub/sub broker
# (Redis Pub/Sub or a message bus) behind multiple server instances
```

---

## 7. Introspection — Schema as First-Class Data

```graphql
# The schema itself is queryable — GraphQL is self-documenting
# This is how GraphiQL, Playground, and codegen tools work

{
  __schema {
    types {
      name
      kind          # OBJECT | SCALAR | ENUM | INTERFACE | UNION | INPUT_OBJECT | LIST | NON_NULL
      fields {
        name
        type { name kind }
      }
    }
    queryType   { name }
    mutationType { name }
  }
}

# Inspect a specific type
{
  __type(name: "User") {
    name
    kind
    fields {
      name
      type {
        name
        kind
        ofType { name kind }   # unwraps NON_NULL and LIST wrappers
      }
    }
  }
}

# What introspection enables:
# - Interactive explorers: GraphiQL, Apollo Sandbox
# - Client code generation: graphql-codegen, Apollo Client codegen
# - Schema validation and linting: graphql-inspector
# - Schema registry diffing (breaking change detection)

# SECURITY: Disable introspection in production environments
# It exposes your entire data model to attackers. Use introspection only in dev/staging.
```

---

## 8. The N+1 Problem and DataLoader

```
The N+1 problem is the #1 production pitfall of naive GraphQL implementations.

Query: { orders { customer { name } } }

Without batching:
─────────────────
  SELECT * FROM orders                           -- 1 query → returns 100 orders
  SELECT * FROM users WHERE id = 1              -- 1 query per order
  SELECT * FROM users WHERE id = 2
  SELECT * FROM users WHERE id = 3
  ...                                            -- 100 queries for customer lookups
  Total: 101 queries (N+1)

With DataLoader:
────────────────
  SELECT * FROM orders                           -- 1 query → 100 orders
  SELECT * FROM users WHERE id IN (1,2,3,...)   -- 1 batched query for all customers
  Total: 2 queries

DataLoader mechanics:
─────────────────────
  1. Each order resolver calls userLoader.load(order.customerId)
  2. DataLoader collects all .load() calls made in the same event loop tick
  3. After tick: fires one batch function with all collected IDs
  4. Distributes results back to each individual resolver

DataLoader implementation (JavaScript):

  import DataLoader from 'dataloader';

  const userLoader = new DataLoader(async (ids: readonly string[]) => {
      const users = await db.query(
          'SELECT * FROM users WHERE id = ANY($1)',
          [ids]
      );
      // CRITICAL: must return results in same order as input ids
      // DataLoader maps by position, not by ID
      return ids.map(id => users.find(u => u.id === id) ?? null);
  });

  // In Order resolver:
  const resolvers = {
    Order: {
      customer: (order) => userLoader.load(order.customerId),
      // ^ batched automatically — no code change in the resolver itself
    }
  };

DataLoader also caches within a single request:
  - Two queries for the same user ID in one request → one DB call, both get the result
  - Cache is per-request (new DataLoader instance per request) — not cross-request
```

---

## 9. Resolver Architecture

```
GraphQL execution model:

  Schema defines the type tree
  Each field in each type has a resolver function
  Resolvers execute in parallel (same level), depth-first (parent before children)

  type Query {
    orders: [Order]    ← resolver: fetches list of orders
  }
  type Order {
    id: ID!            ← default resolver: returns order.id (trivial)
    customer: User     ← resolver: fetches customer by order.customerId
    lineItems: [LineItem] ← resolver: fetches line items by order.id
  }

Resolver signature (Node.js):
─────────────────────────────
  (parent, args, context, info) => result | Promise<result>

  parent   = resolved value of the parent object (the Order, in Order.customer)
  args     = field arguments from the query ({ id: "1001" })
  context  = shared request context (auth, DataLoaders, DB connections)
  info     = AST info about the current query (field name, selected subfields — for optimization)

  const resolvers = {
    Query: {
      user: (_, { id }, { db }) => db.users.findById(id),
      orders: (_, { limit, offset }, { db }) => db.orders.findAll({ limit, offset }),
    },
    Order: {
      customer: (order, _, { userLoader }) => userLoader.load(order.customerId),
    },
    SearchResult: {
      __resolveType: (obj) => {          // required for union types
        if (obj.email) return 'User';
        if (obj.total) return 'Order';
        return null;
      }
    }
  };

Context pattern: inject DataLoaders and DB connections per request
  const server = new ApolloServer({
    typeDefs, resolvers,
    context: ({ req }) => ({
      db: getDbConnection(),
      userLoader: new DataLoader(batchUsers),  // new instance per request (fresh cache)
      currentUser: getAuthUser(req),
    })
  });
```

---

## 10. Schema-First vs Code-First

```
Schema-First                              Code-First
─────────────────────────────────         ─────────────────────────────────
Write SDL → generate TypeScript types     Write code → generate SDL

# schema.graphql                          # TypeScript (type-graphql or NestJS)
type User {                               @ObjectType()
  id: ID!                                 class User {
  name: String!                             @Field(() => ID)
}                                           id: string;

# Then codegen:                              @Field()
#   npx graphql-codegen                      name: string;
# → generates:                          }
interface User {
  id: string;                           # Resolver (type-graphql):
  name: string;                         @Resolver(User)
}                                       class UserResolver {
                                          @Query(() => User)
                                          async user(@Arg('id') id: string) {
                                            return this.userService.findById(id);
                                          }
                                        }

Pros: explicit contract visible           Pros: DRY, no code/schema drift,
  to all teams, language-agnostic SDL,      TypeScript-native, IDE autocomplete
  schema is source of truth             Cons: SDL is generated (less readable),
Cons: SDL + code can drift,               harder to share cross-language
  codegen step required

# .NET (Hot Chocolate — code-first):
public class UserType : ObjectType<User>
{
    protected override void Configure(IObjectTypeDescriptor<User> descriptor)
    {
        descriptor.Field(u => u.Id).Type<NonNullType<IdType>>();
        descriptor.Field(u => u.Name).Type<NonNullType<StringType>>();
    }
}
# Hot Chocolate generates SDL from C# classes — familiar pattern for .NET teams
```

---

## 11. Apollo Federation — Distributed Schema (Supergraph)

```
Federation: each microservice owns its slice of the schema.
Apollo Gateway (or Apollo Router) composes them into one unified graph.
Clients query the gateway; the gateway plans and fans out to subgraphs.

T-SQL bridge: like a federated view that spans multiple databases,
              with the gateway acting as a distributed query planner.

┌─────────────────────────────────────────────────────────────────────┐
│                      Apollo Supergraph                              │
│                                                                     │
│  Client ──► Apollo Router/Gateway ──► Users Subgraph               │
│                          │         └──► Orders Subgraph            │
│                          │         └──► Products Subgraph          │
│                          │                                          │
│  Router generates a query plan: which fields from which subgraph   │
└─────────────────────────────────────────────────────────────────────┘

# Orders subgraph schema:
type Order @key(fields: "id") {
  id:         ID!
  customerId: ID!
  total:      Float!
  customer:   User        # cross-subgraph reference
}
extend type User @key(fields: "id") {
  id:     ID! @external   # defined in Users subgraph
  orders: [Order!]!       # Orders subgraph extends User with this field
}

# Users subgraph schema:
type User @key(fields: "id") {
  id:    ID!
  name:  String!
  email: String!
}

# Client query (gateway resolves across both subgraphs transparently):
query {
  order(id: "1") {
    total
    customer {            # → Router fetches from Users subgraph
      name
      email
    }
  }
}

# Federation v2 directives:
# @key(fields)        — entity identifier for cross-subgraph references
# @external           — field owned by another subgraph
# @requires(fields)   — field needed from another subgraph to resolve this one
# @provides(fields)   — this subgraph can provide these fields locally (optimization)
# @shareable          — field can be resolved by multiple subgraphs
```

---

## 12. Persisted Queries and Caching

```
GraphQL caching is harder than REST:
  - All requests go to one endpoint (POST /graphql)
  - POST is not cached by CDNs
  - Query shape varies per client — no static cache keys

Approach 1: Automatic Persisted Queries (APQ — Apollo)
──────────────────────────────────────────────────────
  1. Client sends: POST /graphql  { "extensions": { "persistedQuery": { "sha256Hash": "abc..." } } }
  2. Server: "unknown hash" → responds with PersistedQueryNotFound error
  3. Client resends with full query body
  4. Server stores query by hash + executes
  5. Future requests: client sends hash only → server executes from cache

  Benefit: smaller payloads. With GET + hash → CDN-cacheable for queries.

Approach 2: Trusted Documents (whitelisted queries — production hardening)
──────────────────────────────────────────────────────────────────────────
  - Build pipeline extracts all queries from client code and registers hashes
  - Server only executes known hashes — arbitrary query execution disabled
  - Eliminates introspection risk AND injection-style abuse

Response caching:
  - @cacheControl directive on types/fields in schema
  - maxAge and scope (PUBLIC | PRIVATE) per field
  - Apollo Server computes max-age from the most restrictive field in a response
  - DataLoader: per-request memoization (not cross-request cache)
```

---

## 13. Hasura — Instant GraphQL Over PostgreSQL

```graphql
# Hasura generates a complete GraphQL API from your PostgreSQL schema — no resolver code
# Also supports: MS SQL Server, MySQL, MongoDB, REST endpoints, event triggers

# Auto-generated query (from orders table with FK to users):
query {
  orders(
    where:    { status: { _eq: "active" } }
    order_by: { created_at: desc }
    limit:    10
    offset:   0
  ) {
    id
    total
    customer {         # FK relationship — auto-joined
      name
      email
    }
  }
}

# Hasura filter operators:
# _eq, _neq, _gt, _gte, _lt, _lte
# _in, _nin
# _like, _ilike (case-insensitive), _similar (regex)
# _is_null
# _and, _or, _not (logical combinators)

# Auto-generated mutation:
mutation {
  insert_orders(objects: [{
    customer_id: 42,
    total:       99.99,
    status:      "pending"
  }]) {
    returning { id created_at }  # RETURNING clause equivalent
  }
}

mutation {
  update_orders(
    where:  { id: { _eq: 42 } }
    _set:   { status: "shipped" }
  ) {
    affected_rows
    returning { id status }
  }
}

# Auto-generated subscription (via PostgreSQL logical replication / polling):
subscription {
  orders(where: { status: { _eq: "pending" } }) {
    id
    total
    created_at
  }
}

# Hasura permissions: role-based row-level + column-level security defined in metadata
# T-SQL bridge: like an OData endpoint that Hasura generates automatically, with
#               the filter language as GraphQL instead of URL query params
```

---

## 14. Query Complexity and Depth Limiting

```
The attack surface of "let the client define the query shape":

  # Malicious deep query — exponential resolver cost
  {
    users {
      friends {
        friends {
          friends {       # depth = 4, each level multiplies previous
            friends {
              name
            }
          }
        }
      }
    }
  }

Defenses:
──────────
  1. Depth limiting: reject queries deeper than N levels
     graphql-depth-limit library: depthLimit(5)

  2. Complexity scoring: assign cost to each field; reject if total > threshold
     Each field has a "complexity" value; nested lists multiply
     graphql-query-complexity library

  3. Query timeout: executor time limit (stops runaway resolvers)

  4. Rate limiting: per-IP or per-user query rate via APQ hash tracking

  5. Trusted documents: only whitelisted queries from your own clients execute
     (eliminates arbitrary query attacks entirely for internal APIs)

Production minimum: depth limit + complexity scoring + introspection disabled
```

---

## 15. Error Handling

```graphql
# GraphQL error shape — NOT HTTP 4xx/5xx (always HTTP 200 for GraphQL errors)
# Errors live in the response body

{
  "data": {
    "user": null           # field is null if its resolver threw
  },
  "errors": [
    {
      "message":   "User not found",
      "locations": [{ "line": 2, "column": 3 }],
      "path":      ["user"],
      "extensions": {
        "code":      "NOT_FOUND",    # machine-readable error code
        "userId":    "1001"
      }
    }
  ]
}

# Partial success: data and errors can coexist
# If user resolver throws, user=null in data AND error appears in errors array
# Other fields in the response may still resolve successfully

# T-SQL bridge: unlike SqlException which throws from the query itself,
# GraphQL field errors are inline — a failed field returns null + appends to errors array
# Monitoring implication: you CANNOT monitor GraphQL health via HTTP status alone.
# Check response body for "errors" array. Set up alerts on error rate in body, not HTTP 4xx/5xx.

# Apollo Server error classes:
import { GraphQLError } from 'graphql';

throw new GraphQLError('User not found', {
  extensions: { code: 'NOT_FOUND', userId: id }
});
# Produces structured error with code in extensions
```

---

## 16. Decision Cheat Sheet

| Use GraphQL When | Use REST When |
|------------------|---------------|
| Multiple clients with different data needs (mobile vs web vs IoT) | Simple CRUD with uniform response shapes |
| Complex nested / relational data in one request | File uploads (REST handles multipart naturally) |
| Frontend teams need autonomy over data shape | CDN caching is the primary concern |
| Real-time subscriptions over WebSocket | Simple webhook integrations |
| API evolution without versioning (add fields freely; deprecate instead of remove) | External public API (REST is more universally understood) |
| Rapid backend with Hasura/Postgraphile auto-generation | Team has no GraphQL experience and deadline is tight |
| Schema-enforced contract between frontend and backend | Microservices-to-microservices communication (gRPC is better) |

| Use Apollo Federation When | Use a Monolithic Schema When |
|---------------------------|------------------------------|
| Multiple teams own separate services | Single team, single service |
| Microservices each have GraphQL endpoints | Schema complexity is manageable in one codebase |
| Need to compose a unified graph from services | Operational overhead of Federation isn't justified |

---

## 17. Common Confusion Points

**GraphQL is not a database.**
It's an API layer. The resolvers call whatever backing data source you wire up — SQL, Redis, REST APIs, gRPC services, files. GraphQL knows nothing about your database schema.

**Single endpoint does not mean one query type.**
One URL (`/graphql`) handles all operations — queries, mutations, subscriptions. They're distinguished by the `query`, `mutation`, `subscription` keyword in the operation and by the operation name, not by URL path or HTTP method (for query/mutation, both use POST).

**HTTP 200 does not mean success.**
GraphQL errors live in `response.errors[]`, not in HTTP status. A response with `HTTP 200` and `{ errors: [...] }` represents a failed operation. Wire your monitoring/alerting to check the response body, not just HTTP status codes. This is the #1 observability gap for teams coming from REST.

**N+1 is silent and the default.**
Naive resolvers silently issue N+1 queries. No warning, no error — just slow performance at scale. DataLoader is required infrastructure, not an optimization to add later. Instrument resolver latency from day one.

**Mutations are sequential, not transactional.**
Multiple mutations in one document execute sequentially, but they are not wrapped in a database transaction. Failed mutation N does not roll back mutation N-1. If you need atomicity, implement the DB transaction inside the resolver.

**Subscriptions require WebSocket infrastructure.**
HTTP for query/mutation is stateless and scales horizontally. WebSocket for subscriptions is stateful — requires sticky sessions, or a shared pub/sub backend (Redis Pub/Sub is the standard choice) when running multiple server instances. Don't deploy subscriptions without planning the WebSocket infrastructure.

**Schema validation is build-time.**
`graphql-codegen` generates TypeScript types from your SDL. If a client queries a non-existent field, codegen fails. This is a strength — it's like TypeScript for your API surface. Wire codegen into your CI pipeline.

**Introspection exposes your entire schema.**
Enabled by default in all GraphQL servers. In production, disable it or put it behind authentication. An attacker with introspection access can reconstruct your full data model and craft targeted queries.

**OData comparison for Azure/Microsoft context.**
Microsoft's OData (used in Azure REST Management APIs, Dynamics 365, Power BI XMLA endpoints) solves the same over-fetching problem but with URL query parameters (`$select`, `$expand`, `$filter`, `$orderby`) instead of a query language. OData responses are REST-cacheable. GraphQL has a richer query language and better tooling. If you're building internal APIs for Microsoft-adjacent environments, Hasura over SQL Server or Hot Chocolate (.NET) are natural GraphQL entry points.

**Nullability design matters early.**
SDL defaults: `String` is nullable, `String!` is non-null. Many schemas make everything non-null by default and opt into nullable explicitly — this matches how TypeScript teams think (strictNullChecks). Changing nullability after the schema is public is a breaking change.
