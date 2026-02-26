# MongoDB Query Language (MQL) + Aggregation Pipeline

MongoDB is the dominant document database. The query language is not SQL — it's JSON-based MQL for CRUD and the aggregation pipeline for complex transformations. The mental model shift: instead of tables with rows, you have collections with documents (JSON objects). Documents can be nested and variable-schema. The aggregation pipeline is MongoDB's equivalent of SQL `SELECT` with `GROUP BY`, `JOIN`, and window functions — but expressed as a sequence of stages, each transforming the document stream.

---

## 1. Relational → Document Mapping

```
┌──────────────────────────────────────────────────────────────────────────────┐
│               SQL (relational)         MongoDB (document)                    │
│               ────────────────         ──────────────────                    │
│               Database            →   Database                               │
│               Table               →   Collection                             │
│               Row                 →   Document  (BSON/JSON object)           │
│               Column (fixed)      →   Field  (variable, nested, optional)    │
│               NULL                →   Field absent  OR  field: null          │
│               PRIMARY KEY         →   _id  (auto ObjectId if not supplied)   │
│               FOREIGN KEY / JOIN  →   Embedded subdoc  OR  $lookup           │
│               INDEX               →   Index  (same concept, similar types)   │
│               VIEW                →   db.createView() or $lookup-based agg   │
│               Stored procedure    →   Application layer (JS removed in 4.x)  │
│                                                                              │
│               SELECT … WHERE …    →   db.col.find({filter}, {projection})    │
│               GROUP BY + aggs     →   aggregate([$match, $group, …])         │
│               JOIN                →   $lookup  stage in aggregation pipeline │
│               UNNEST / EXPLODE    →   $unwind  stage                         │
│               CASE WHEN           →   $cond / $switch  expression operator   │
│               HAVING              →   $match  after  $group                  │
└──────────────────────────────────────────────────────────────────────────────┘

Bridge: think of a MongoDB document as an ADO.NET DataRow where columns can hold
nested DataTables, arrays, or arbitrary objects — and the schema is not enforced
at the database level. The application is the schema contract.
```

### T-SQL JSON vs MongoDB Document Model

SQL Server has a JSON layer (FOR JSON, OPENJSON, JSON_VALUE, JSON_QUERY) that sits on top of relational storage. The architecture is fundamentally different from MongoDB, but the surface-level operations map directly — which gives you a concrete anchor.

**Storage layer difference:**
- SQL Server: JSON is stored in `NVARCHAR(MAX)` columns. It's text on disk. The JSON structure is parsed at query time on every access. The relational engine has no awareness of JSON internals at storage level.
- MongoDB: BSON (Binary JSON) is the native physical encoding. The storage engine is document-native. Field access does not require string parsing — the engine navigates the binary structure directly.

**Operation mapping:**

| T-SQL JSON | MongoDB equivalent | Notes |
|---|---|---|
| `JSON_VALUE(doc, '$.address.city')` | `{ "address.city": "Seattle" }` in filter, or `"$address.city"` in expression | Dot notation is native in MongoDB — no function call needed |
| `JSON_QUERY(doc, '$.line_items')` | `"$line_items"` | Accessing a nested array or subdoc |
| `OPENJSON(doc) WITH (city VARCHAR(100) '$.address.city')` | `{ $project: { city: "$address.city" } }` | Projecting specific fields from a document |
| `FOR JSON PATH` | `{ $project: { ... } }` or `{ $replaceRoot }` | Constructing a JSON output shape |
| `ISJSON(doc)` | No equivalent — every document is valid BSON by definition | |
| `JSON_MODIFY(doc, '$.status', 'active')` | `{ $set: { status: "active" } }` in `updateOne` | |

**The structural difference in practice:** In SQL Server, you choose whether to use JSON — it's an escape hatch from the relational model. In MongoDB, you are always in the document model — there is no "relational substrate" to fall back on. The discipline that SQL Server enforces at the schema level (column names, data types, NOT NULL constraints) is enforced by the application in MongoDB.

### SQL Server Normalized Schema → Two MongoDB Design Strategies

```
SQL Server (normalized — 3NF):

  orders                           customers
  ┌────────┬─────────────┬──────┐  ┌────────────┬───────────┬────────────┐
  │ id     │ customer_id │ ...  │  │ id         │ name      │ email      │
  ├────────┼─────────────┼──────┤  ├────────────┼───────────┼────────────┤
  │ 1001   │ 42          │ ...  │  │ 42         │ Alice     │ a@b.com    │
  └────────┴─────────────┴──────┘  └────────────┴───────────┴────────────┘
           │                                 ▲
           └─── FK ──────────────────────────┘   (join at query time)

  order_items
  ┌──────────┬──────────┬────────┬───────┐
  │ order_id │ product  │ qty    │ price │
  ├──────────┼──────────┼────────┼───────┤
  │ 1001     │ Widget   │ 2      │ 9.99  │
  │ 1001     │ Gadget   │ 1      │ 14.99 │
  └──────────┴──────────┴────────┴───────┘

MongoDB Strategy A — embed everything (denormalized, read-optimized):

  orders collection:
  {
    _id: 1001,
    customer: { name: "Alice", email: "a@b.com" },   // customer embedded
    line_items: [                                      // items embedded array
      { product: "Widget", qty: 2, price: 9.99  },
      { product: "Gadget", qty: 1, price: 14.99 }
    ]
  }

  Pro: one document read = complete order. No joins.
  Con: customer data duplicated across all orders. Updates require touching
       every order document when customer email changes.

MongoDB Strategy B — reference customers, embed line items:

  customers collection:              orders collection:
  { _id: 42, name: "Alice",   →      { _id: 1001,
    email: "a@b.com" }                 customer_id: 42,           // reference
                                       line_items: [              // still embedded
                                         { product: "Widget", qty: 2, price: 9.99 },
                                         { product: "Gadget", qty: 1, price: 14.99 }
                                       ]
                                     }

  Pro: customer data in one place — update once. Line items always read with
       the order (never queried independently) so embedding is correct there.
  Con: order queries that need customer name require $lookup.
```

**Decision rule:** embed when the child data is always read with the parent and is bounded in size. Reference when the child is large, frequently updated, or queried independently. Line items → embed. Customer profile → reference. Order history on a customer document → reference (unbounded growth).

---

## 2. Dialect Snapshot

| Attribute | Value |
|-----------|-------|
| Created by | 10gen (now MongoDB Inc), 2009 |
| License | SSPL (not OSI-approved) / Atlas is commercial SaaS |
| Current version | MongoDB 7.x (2024) |
| Data model | BSON documents in collections — binary-encoded JSON with extra types |
| ACID | Single-document always; multi-document transactions since 4.0 (replica sets/sharded) |
| SQL equivalent | None — MQL for CRUD, aggregation pipeline for analytics |
| Cloud options | MongoDB Atlas (multi-cloud), AWS DocumentDB (partial compat), Azure Cosmos DB (MongoDB API — partial compat) |
| Unique strengths | Flexible schema, embedded documents, horizontal sharding, Atlas Search (Lucene), Atlas Vector Search |
| Indexing | B-tree, compound, text, 2dsphere, TTL, partial, wildcard, hashed (for sharding) |

---

## 3. CRUD — MQL Syntax

```javascript
// find() — the SELECT equivalent
db.orders.find(
    { status: "active", total: { $gt: 100 } },    // filter (WHERE)
    { customer_id: 1, total: 1, _id: 0 }          // projection (SELECT columns)
                                                   // 1 = include, 0 = exclude
)
.sort({ total: -1 })    // ORDER BY total DESC  (-1=DESC, 1=ASC)
.limit(10)              // LIMIT 10
.skip(20);              // OFFSET 20

// findOne() — first matching document
db.users.findOne({ email: "alice@example.com" });

// insertOne / insertMany
db.products.insertOne({ name: "Widget", price: 9.99, tags: ["tool", "hardware"] });
db.products.insertMany([
    { name: "Gadget",     price: 14.99 },
    { name: "Doohickey",  price:  4.99 }
]);

// updateOne / updateMany — PARTIAL update with $set
db.orders.updateOne(
    { _id: ObjectId("...") },                        // filter
    {
        $set:   { status: "shipped", shipped_at: new Date() },
        $unset: { pending_since: "" },               // remove field
        $inc:   { attempt_count: 1 }                 // increment in place
    }
);

// findOneAndUpdate — atomic read + update (returns old or new doc)
// Equivalent to SQL Server OUTPUT clause pattern
db.counters.findOneAndUpdate(
    { _id: "order_seq" },
    { $inc: { value: 1 } },
    { returnDocument: "after", upsert: true }        // upsert = INSERT if not found
);

// deleteOne / deleteMany
db.sessions.deleteMany({ expires_at: { $lt: new Date() } });

// replaceOne — replaces the ENTIRE document (not partial)
// Equivalent to a full UPDATE without $set — overwrites all fields
db.products.replaceOne({ _id: productId }, newProductDocument);

// countDocuments
db.orders.countDocuments({ status: "active" });           // exact count with filter
db.orders.estimatedDocumentCount();                       // fast approximate total count
```

---

## 4. Query Operators — Reference Card

```javascript
// ── Comparison ────────────────────────────────────────────────────────────
{ field: value }                       // exact equality (implicit $eq)
{ field: { $eq:  value } }             // explicit equality
{ field: { $ne:  value } }             // not equal         ≠
{ field: { $gt:  100   } }             // greater than       >
{ field: { $gte: 100   } }             // greater or equal   >=
{ field: { $lt:  100   } }             // less than          <
{ field: { $lte: 100   } }             // less or equal      <=
{ field: { $in:  [1, 2, 3] } }         // IN (1, 2, 3)
{ field: { $nin: [1, 2, 3] } }         // NOT IN (1, 2, 3)

// ── Logical ───────────────────────────────────────────────────────────────
{ a: 1, b: 2 }                         // implicit AND (both conditions must match)
{ $and: [ {cond1}, {cond2} ] }         // explicit AND (required when same field appears twice)
{ $or:  [ {cond1}, {cond2} ] }         // OR
{ $nor: [ {cond1}, {cond2} ] }         // NOR — neither condition is true
{ field: { $not: { $gt: 100 } } }      // NOT (inverts operator result)

// ── Existence and type ────────────────────────────────────────────────────
{ field: { $exists: true  } }          // field present in document (IS NOT NULL analog)
{ field: { $exists: false } }          // field absent
{ field: { $type: "string" } }         // BSON type check
{ field: { $type: ["string", "null"] } }

// ── String / regex ────────────────────────────────────────────────────────
{ name: { $regex: /^alice/i } }        // starts with "alice", case-insensitive
{ name: /alice/i }                     // shorthand — equivalent
{ name: { $regex: "alice", $options: "i" } }  // string form for dynamic regex

// ── Array operators ───────────────────────────────────────────────────────
{ tags: "mongodb" }                    // array contains element "mongodb" (scalar match)
{ tags: { $all: ["mongodb", "db"] } }  // array contains ALL listed elements
{ scores: { $elemMatch: { $gt: 80, $lt: 100 } } }  // at least one element matches ALL conditions
                                                    // { scores: { $gt: 80, $lt: 100 } } is different:
                                                    // checks any element > 80 AND any element < 100
{ tags: { $size: 3 } }                 // array has exactly 3 elements

// ── Nested field access (dot notation) ───────────────────────────────────
{ "address.city": "Seattle" }          // nested document field
{ "address.zip.code": "98101" }        // multi-level nesting
{ "line_items.0.product_id": 42 }      // first element of array
```

---

## 5. Aggregation Pipeline — The SQL SELECT Equivalent

The pipeline is an ordered array of stages. Each stage transforms the stream of documents. Conceptually identical to SQL SELECT but expressed as a sequence of operations rather than a single declarative statement.

**Pipeline stage → T-SQL correspondence:**

```
┌─────────────────┬────────────────────────────────────────────────┐
│ Pipeline Stage  │ T-SQL Equivalent                               │
├─────────────────┼────────────────────────────────────────────────┤
│ $match          │ WHERE  (before $group)  /  HAVING (after $group)│
│ $group          │ GROUP BY + aggregate functions                  │
│ $project        │ SELECT (column list, computed columns, aliases) │
│ $sort           │ ORDER BY                                        │
│ $limit          │ TOP N  /  FETCH NEXT N ROWS ONLY               │
│ $skip           │ OFFSET N ROWS                                   │
│ $lookup         │ LEFT JOIN  (nested-loop, no optimizer reorder)  │
│ $unwind         │ CROSS APPLY UNNEST / OPENJSON on array column   │
│ $addFields      │ SELECT *, computed_col AS alias                 │
│ $count          │ SELECT COUNT(*) AS n                            │
│ $facet          │ Multiple CTEs / subqueries in one pass          │
│ $out / $merge   │ SELECT INTO / MERGE (terminal, writes result)   │
└─────────────────┴────────────────────────────────────────────────┘

Pipeline executes LEFT TO RIGHT. Order is explicit. The optimizer cannot
reorder stages (unlike SQL where the optimizer reorders freely). PUT $match
FIRST — it's the single most important performance rule in MongoDB.
```

```javascript
db.orders.aggregate([

    // Stage 1: $match — like WHERE (filter EARLY to reduce data for subsequent stages)
    { $match: {
        status:     { $in: ["completed", "shipped"] },
        order_date: { $gte: new Date("2024-01-01") }
    }},

    // Stage 2: $group — like GROUP BY + aggregates
    { $group: {
        _id:             "$customer_id",            // GROUP BY customer_id
        order_count:     { $sum: 1 },               // COUNT(*)
        total_revenue:   { $sum: "$total" },        // SUM(total)
        avg_order:       { $avg: "$total" },        // AVG(total)
        max_order:       { $max: "$total" },        // MAX(total)
        first_order:     { $min: "$order_date" },   // MIN(order_date)
        all_products:    { $push: "$product_id" },  // array_agg(product_id)
        unique_products: { $addToSet: "$product_id" } // array_agg(DISTINCT product_id)
    }},

    // Stage 3: $match after $group — like HAVING
    { $match: { total_revenue: { $gt: 1000 } }},

    // Stage 4: $sort — ORDER BY
    { $sort: { total_revenue: -1 }},               // DESC

    // Stage 5: $limit
    { $limit: 20 }
]);
```

---

## 6. Aggregation Stages — Full Reference

```javascript
// $project — like SELECT: reshape, include, exclude, compute
{ $project: {
    customer_name:  1,                                     // include
    _id:            0,                                     // exclude _id
    year:           { $year: "$order_date" },              // computed
    total_with_tax: { $multiply: ["$total", 1.08] }
}}

// $addFields — extend documents with computed fields (keeps ALL existing fields)
// Like adding computed columns to a SELECT without dropping others
{ $addFields: {
    total_with_tax: { $multiply: ["$total", 1.08] },
    is_high_value:  { $gt: ["$total", 500] }
}}

// $unwind — flatten array field to one document per array element
// Like CROSS APPLY UNNEST or OPENJSON in T-SQL
{ $unwind: "$line_items" }
{ $unwind: { path: "$tags", preserveNullAndEmpty: true } }  // keep docs with empty/null array

// $lookup — LEFT OUTER JOIN equivalent
{ $lookup: {
    from:         "customers",      // join to this collection
    localField:   "customer_id",    // field in current docs
    foreignField: "_id",            // field in 'customers'
    as:           "customer"        // output field (always an ARRAY of matching docs)
}}
// Result: each order gets a 'customer' field = [{...customer doc...}]
// Follow with $unwind to flatten to a single object:
{ $unwind: { path: "$customer", preserveNullAndEmpty: true } }
```

**$lookup is not a SQL JOIN — performance model is fundamentally different.**

A SQL JOIN is a logical operation the optimizer evaluates at compile time. The optimizer can reorder joins, push predicates inside the join, choose hash join vs nested-loop vs merge join based on statistics, and use indexes on both sides simultaneously. `$lookup` is a pipeline stage executed at a fixed position in the sequence. It cannot be reordered by the optimizer, does not benefit from predicate pushdown from stages that appear after it, and executes as a nested-loop lookup: for each document in the pipeline at that point, MongoDB issues a query against the `from` collection. The `from` field must be indexed for this to perform acceptably.

Rules for `$lookup`:
- Always put `$match` before `$lookup` to reduce the number of documents that trigger lookups.
- The `foreignField` (or the field matched in the pipeline form) must be indexed.
- High cardinality `$lookup` at the primary query pattern level is a schema design signal — if your queries routinely join across collections, your schema needs redesign (embed the data instead).
- `$lookup` is appropriate for occasional enrichment (add customer name to an order summary) not for the core data retrieval pattern.

**If your query workload is primarily JOIN-heavy, MongoDB is the wrong tool. Use PostgreSQL.**

```javascript
// $lookup pipeline form — correlated join with filtering inside the join
{ $lookup: {
    from: "products",
    let:  { productIds: "$line_items.product_id" },    // bind local variables
    pipeline: [
        { $match:   { $expr: { $in: ["$_id", "$$productIds"] }}},
        { $project: { name: 1, price: 1 }}
    ],
    as: "products"
}}

// $facet — run multiple sub-pipelines on the same input simultaneously
// Like running three GROUP BYs in parallel
{ $facet: {
    byStatus:     [{ $group: { _id: "$status",                 count:  { $sum: 1 }}}],
    byMonth:      [{ $group: { _id: { $month: "$order_date" }, total:  { $sum: "$total" }}}],
    topCustomers: [{ $sort:  { total: -1 }}, { $limit: 5 }]
}}

// $bucket — group into ranges (histogram, manual boundaries)
{ $bucket: {
    groupBy:    "$total",
    boundaries: [0, 50, 100, 500, 1000],
    default:    "1000+",
    output:     { count: { $sum: 1 }, avg_total: { $avg: "$total" }}
}}

// $bucketAuto — auto-distribute into N equal-population buckets
// Equivalent to NTILE(N) histogram — MongoDB chooses boundaries automatically
{ $bucketAuto: {
    groupBy:    "$total",
    buckets:    5,                             // create 5 buckets
    output:     { count: { $sum: 1 }, avg_total: { $avg: "$total" }},
    granularity: "POWERSOF2"                   // optional: snap boundaries to powers of 2
}}
// $bucket requires you know the value range; $bucketAuto discovers it from data.

// $unwind + $group — "spreadsheet flatten" pattern
// Use case: orders have embedded line_items array; compute total quantity per product
// T-SQL equivalent: CROSS APPLY OPENJSON(line_items) + GROUP BY product
db.orders.aggregate([
    { $match:  { order_date: { $gte: new Date("2024-01-01") } }},
    { $unwind: "$line_items" },                // flatten: one doc per line item
    { $group:  {
        _id:        "$line_items.product_id",  // GROUP BY product
        total_qty:  { $sum: "$line_items.qty" },
        total_rev:  { $sum: { $multiply: ["$line_items.qty", "$line_items.price"] }},
        order_count: { $addToSet: "$_id" }     // distinct orders per product
    }},
    { $addFields: { order_count: { $size: "$order_count" } }},  // set → count
    { $sort:   { total_rev: -1 }},
    { $limit:  20 }
])
// The $unwind "inflates" the document stream — 1 order with 5 line items → 5 documents.
// $group then re-aggregates the inflated stream. This is the canonical pattern for
// aggregating across embedded arrays.

// $replaceRoot — promote nested document to top level
// SELECT customer.* FROM orders (flatten the embedded customer subdoc)
{ $replaceRoot: { newRoot: "$customer" }}

// $count — count documents at this point in pipeline
{ $count: "total_orders" }

// $out — write pipeline result to a new collection (terminal stage)
{ $out: "customer_revenue_summary" }

// $merge — upsert pipeline result into a collection (terminal stage)
{ $merge: {
    into:         "customer_revenue_summary",
    on:           "_id",
    whenMatched:  "merge",          // merge fields on match
    whenNotMatched: "insert"        // insert new doc if no match
}}
```

---

## 7. Expression Operators — Reference

Used inside `$project`, `$addFields`, `$group`, `$match` with `$expr`, etc.

```javascript
// ── Arithmetic ────────────────────────────────────────────────────────────
{ $add:      [expr1, expr2] }
{ $subtract: [expr1, expr2] }
{ $multiply: [expr1, expr2] }
{ $divide:   [expr1, expr2] }
{ $mod:      [expr1, expr2] }
{ $abs:      expr }
{ $round:    [expr, decimalPlaces] }
{ $ceil:     expr }, { $floor: expr }

// ── Conditional — like CASE WHEN ─────────────────────────────────────────
{ $cond: { if: { $gt: ["$total", 500] }, then: "high", else: "low" } }
{ $cond: [condition, trueVal, falseVal] }            // shorthand form

{ $ifNull: ["$discount", 0] }                        // COALESCE($discount, 0)

{ $switch: {
    branches: [
        { case: { $gte: ["$total", 1000] }, then: "platinum" },
        { case: { $gte: ["$total",  500] }, then: "gold"     },
        { case: { $gte: ["$total",  100] }, then: "silver"   }
    ],
    default: "bronze"
}}

// ── Comparison (expression form — for use inside $expr) ──────────────────
{ $eq:  [expr1, expr2] }
{ $ne:  [expr1, expr2] }
{ $gt:  [expr1, expr2] }
{ $gte: [expr1, expr2] }
{ $lt:  [expr1, expr2] }
{ $lte: [expr1, expr2] }

// ── String ────────────────────────────────────────────────────────────────
{ $concat:   ["$firstName", " ", "$lastName"] }
{ $toLower:  "$name" }
{ $toUpper:  "$name" }
{ $substr:   ["$name", 0, 5] }                       // 0-indexed, length 5
{ $strLenCP: "$name" }                               // character count (code points)
{ $trim:     { input: "$name" } }
{ $regexFind:    { input: "$email", regex: /@(.+)$/, options: "i" } }
{ $regexFindAll: { input: "$body",  regex: /\d+/ } }

// ── Date ──────────────────────────────────────────────────────────────────
{ $year:       "$order_date" }
{ $month:      "$order_date" }
{ $dayOfMonth: "$order_date" }
{ $dayOfWeek:  "$order_date" }                       // 1=Sun, 7=Sat
{ $dateToString: { format: "%Y-%m-%d", date: "$order_date" } }
{ $dateDiff:   { startDate: "$start", endDate: "$end", unit: "day" } }
{ $dateAdd:    { startDate: "$start", unit: "day", amount: 30 } }

// ── Array ─────────────────────────────────────────────────────────────────
{ $size:         "$tags" }                           // array length
{ $slice:        ["$tags", 3] }                      // first 3 elements
{ $arrayElemAt:  ["$items", 0] }                     // element at index (0-based)
{ $first:        "$items" }                          // first element
{ $last:         "$items" }                          // last element
{ $reverseArray: "$items" }
{ $concatArrays: ["$arr1", "$arr2"] }
{ $setUnion:     ["$arr1", "$arr2"] }                // distinct elements union
{ $setIntersection: ["$arr1", "$arr2"] }
{ $in:           [value, "$arrayField"] }            // array contains value

{ $filter: {
    input: "$items",
    cond:  { $gt: ["$$this.price", 50] }             // $$this = current element
}}

{ $map: {
    input: "$items",
    as:    "item",
    in:    { $multiply: ["$$item.qty", "$$item.price"] }
}}

{ $reduce: {
    input:        "$items",
    initialValue: 0,
    in:           { $add: ["$$value", "$$this.price"] }  // $$value = accumulator
}}
```

---

## 8. Indexes

```javascript
// Single field
db.orders.createIndex({ customer_id: 1 });          // 1 = ASC
db.orders.createIndex({ order_date: -1 });           // -1 = DESC

// Compound — leftmost prefix rule applies (same as SQL Server composite index)
db.orders.createIndex({ customer_id: 1, order_date: -1 });

// Unique
db.users.createIndex({ email: 1 }, { unique: true });

// Sparse — only indexes documents where the field exists
// Useful for optional fields (avoids indexing thousands of nulls)
db.events.createIndex({ deleted_at: 1 }, { sparse: true });

// TTL — auto-deletes documents at the datetime stored in the indexed field
db.sessions.createIndex({ expires_at: 1 }, { expireAfterSeconds: 0 });
// or: expireAfterSeconds: 3600 → delete 1 hour after the date value

// Partial — only indexes documents matching the filter expression
// Like SQL Server filtered index
db.orders.createIndex(
    { customer_id: 1, total: -1 },
    { partialFilterExpression: { status: "active" } }
);

// Text index — basic full-text search (BM25, not Lucene)
db.articles.createIndex({ title: "text", body: "text" });
db.articles.find({ $text: { $search: "database performance" } });

// 2dsphere — geospatial (WGS84 spherical geometry)
db.stores.createIndex({ location: "2dsphere" });
db.stores.find({
    location: {
        $near: {
            $geometry:   { type: "Point", coordinates: [-122.33, 47.61] },
            $maxDistance: 5000   // meters
        }
    }
});

// Wildcard — indexes all fields or all subfields of a nested document
db.products.createIndex({ "attributes.$**": 1 });   // all fields under 'attributes'
db.catalog.createIndex({ "$**": 1 });               // every field in every document

// Hashed — for hash-based sharding (not for range queries)
db.orders.createIndex({ customer_id: "hashed" });

// Multikey — automatically created when indexing an array field
// MongoDB indexes each element of the array individually
db.orders.createIndex({ tags: 1 });                  // tags is an array field
// The index contains one entry per array element per document.
// A document with tags: ["mongodb", "database", "performance"] contributes 3 index entries.
// You cannot create a compound index where more than one field is a multikey (array) field.
```

### Compound Index Design — ESR Rule

The ESR rule governs compound index field ordering (same concept as SQL Server composite index selectivity ordering, but with a more specific rule for range fields):

```
ESR: Equality → Sort → Range

Fields used in Equality conditions first.
Fields used for Sort order next.
Fields used in Range conditions last.

Example query:
  db.orders.find({ status: "active", total: { $gte: 100 } }).sort({ order_date: -1 })

  status → Equality (exact match)    → first
  order_date → Sort                  → second
  total → Range ($gte)               → third

Correct index: { status: 1, order_date: -1, total: 1 }
Incorrect:     { status: 1, total: 1, order_date: -1 }
               ^^^ Range before Sort — sort can't use index efficiently

SQL Server rule: put most selective column first.
MongoDB ESR rule: put equality columns first regardless of selectivity, then sort, then range.
The rules differ because MongoDB's query planner uses the sort stage differently.
```

### Index Intersection vs Compound Index

MongoDB can combine two single-field indexes (index intersection) to answer a query that filters on both fields. However, index intersection is less reliable than a purpose-built compound index:
- Index intersection requires loading and intersecting two index result sets in memory.
- The optimizer may not choose intersection even when it would help — it depends on query shape and collection statistics.
- A compound index is always preferable when the query pattern is known and stable.

Rule of thumb: **create compound indexes for hot query paths. Let intersection handle ad-hoc queries.**

---

## 9. EXPLAIN

```javascript
db.orders.find({ customer_id: 42, status: "active" }).explain("executionStats");
db.orders.aggregate([...]).explain("executionStats");
```

Key fields to read in the output:

| Field | What it means | Good / Bad |
|-------|---------------|------------|
| `executionStats.executionTimeMillis` | Total execution time in ms | Lower is better |
| `executionStats.totalDocsExamined` | Documents scanned | Should ≈ `totalDocsReturned` |
| `executionStats.totalDocsReturned` | Documents returned to caller | Baseline |
| `executionStats.totalKeysExamined` | Index keys scanned | Should ≈ `totalDocsReturned` |
| `winningPlan.stage` | Execution strategy | `IXSCAN` = good, `COLLSCAN` = full scan = bad |
| `winningPlan.indexName` | Which index was chosen | Verify it's the expected index |

A `totalDocsExamined` >> `totalDocsReturned` ratio means index selectivity is poor — add a more selective compound index.

**Bridge to SQL Server execution plans:**

| SQL Server | MongoDB `explain("executionStats")` |
|---|---|
| Execution plan → graphical/XML plan | `winningPlan` tree (nested JSON stages) |
| Clustered Index Scan / Table Scan | `COLLSCAN` — full collection scan, no index |
| Index Seek | `IXSCAN` — good, using index efficiently |
| Index Scan | `IXSCAN` with low key selectivity — high `totalKeysExamined` vs `totalDocsReturned` |
| Key Lookup (RID lookup) | `FETCH` stage after `IXSCAN` — fetching full document after index lookup |
| Estimated rows / actual rows | `totalDocsReturned` vs `totalDocsExamined` |
| Logical reads | No direct equivalent — `totalKeysExamined` is the closest proxy |
| Missing index hint | No built-in hint — read the ratio and build the index manually |
| SET STATISTICS IO ON | No equivalent — use `explain("executionStats")` |

Use `explain("allPlansExecution")` to see rejected plans (analogous to viewing alternative execution plans in SSMS).

---

## 10. SQL → MQL Translation Table

| SQL | MongoDB MQL / Aggregation |
|-----|--------------------------|
| `SELECT * FROM orders WHERE status = 'active'` | `db.orders.find({ status: "active" })` |
| `SELECT id, total FROM orders` | `db.orders.find({}, { _id: 1, total: 1 })` |
| `WHERE total > 100 AND status = 'active'` | `{ total: { $gt: 100 }, status: "active" }` |
| `WHERE status IN ('a', 'b')` | `{ status: { $in: ["a", "b"] } }` |
| `WHERE name LIKE '%alice%'` | `{ name: { $regex: /alice/i } }` |
| `WHERE field IS NULL` | `{ field: null }` (matches null OR absent) |
| `WHERE field IS NOT NULL` | `{ field: { $ne: null, $exists: true } }` |
| `ORDER BY total DESC` | `.sort({ total: -1 })` |
| `LIMIT 10 OFFSET 20` | `.limit(10).skip(20)` |
| `COUNT(*)` | `db.orders.countDocuments({ status: "active" })` |
| `SELECT dept, SUM(total) GROUP BY dept` | `[{ $group: { _id: "$dept", total: { $sum: "$total" }}}]` |
| `HAVING SUM(total) > 1000` | `{ $match: { total: { $gt: 1000 } } }` after `$group` |
| `LEFT JOIN customers ON orders.cust_id = customers.id` | `{ $lookup: { from: "customers", localField: "cust_id", foreignField: "_id", as: "customer" }}` |
| `CROSS APPLY UNNEST(array_col)` | `{ $unwind: "$array_field" }` |
| `CASE WHEN total > 500 THEN 'high' ELSE 'low' END` | `{ $cond: { if: { $gt: ["$total", 500] }, then: "high", else: "low" } }` |
| `COALESCE(discount, 0)` | `{ $ifNull: ["$discount", 0] }` |
| `SELECT col, 'val' AS new_col` | `$addFields` or `$project` with computed expression |
| `INSERT OR REPLACE` (upsert) | `replaceOne({filter}, doc, { upsert: true })` |
| `UPDATE ... SET field = field + 1` | `updateOne({filter}, { $inc: { field: 1 } })` |
| `DELETE WHERE expires < NOW()` | `deleteMany({ expires_at: { $lt: new Date() } })` |

### T-SQL JSON Functions → MongoDB Native Operations

SQL Server's JSON functions operate on NVARCHAR columns containing JSON text. MongoDB's document model is BSON-native — the same operations that T-SQL performs via function calls are first-class syntax in MQL.

| T-SQL JSON | MongoDB equivalent |
|---|---|
| `JSON_VALUE(doc, '$.address.city')` | `"address.city"` in filter / `"$address.city"` in aggregation expression |
| `JSON_QUERY(doc, '$.line_items')` | `"$line_items"` (array/subdoc field reference) |
| `OPENJSON(doc) WITH (city NVARCHAR(100) '$.address.city')` | `{ $project: { city: "$address.city" } }` |
| `FOR JSON PATH` (construct JSON output) | `{ $project: { nested: { field1: "$f1", field2: "$f2" } } }` |
| `JSON_MODIFY(doc, '$.status', 'active')` | `{ $set: { status: "active" } }` in `updateOne` |
| `OPENJSON(doc, '$.tags') WITH ([value] NVARCHAR(50) '$')` | `{ $unwind: "$tags" }` (flatten array to rows) |
| Cross join + `OPENJSON` to explode array rows | `{ $unwind: "$line_items" }` |

**The key architectural difference:** T-SQL JSON functions are string parsing operations that produce relational output. Every `JSON_VALUE` call parses the NVARCHAR text to locate the path. MongoDB dot notation is a direct path into the BSON binary structure — there is no string parsing at access time. The performance model is different at the I/O layer even when the query surface looks similar.

---

## 11. Atlas Search and Atlas Vector Search

Atlas Search is a Lucene-powered full-text search engine integrated into MongoDB Atlas. It is a separate index type — not the same as the basic `text` index type available in self-hosted MongoDB.

```javascript
// Atlas Search: full-text search with Lucene relevance scoring
db.articles.aggregate([
    { $search: {
        index: "articles_search",           // named search index (configured in Atlas UI)
        text: {
            query: "database performance",
            path:  ["title", "body"],       // fields to search
            fuzzy: { maxEdits: 1 }          // typo tolerance (edit distance)
        }
    }},
    { $project: {
        title: 1, body: 1,
        score: { $meta: "searchScore" }     // Lucene relevance score
    }},
    { $sort: { score: { $meta: "searchScore" } }},
    { $limit: 10 }
]);

// Atlas Search: autocomplete (typeahead)
{ $search: {
    index: "articles_search",
    autocomplete: { query: "dat", path: "title" }
}}

// Atlas Search: compound query (must + should + mustNot)
{ $search: {
    compound: {
        must:    [{ text: { query: "mongodb",     path: "body" } }],
        should:  [{ text: { query: "performance", path: "body" } }],
        mustNot: [{ text: { query: "deprecated",  path: "body" } }]
    }
}}

// Atlas Vector Search — nearest-neighbor search on embedding vectors
// Primary use case: RAG (retrieval-augmented generation)
db.documents.aggregate([
    { $vectorSearch: {
        index:         "vector_index",
        path:          "embedding",         // field storing the float[] vector
        queryVector:   [0.1, 0.2, 0.05, ...],  // query embedding (e.g. 1536 dims for OpenAI)
        numCandidates: 100,                 // ANN candidates to consider (higher = more accurate, slower)
        limit:         10                   // return top-10 nearest neighbors
    }},
    { $project: {
        text:  1,
        score: { $meta: "vectorSearchScore" }
    }}
]);
```

---

## 12. Schema Design Patterns

```
Embedding vs Referencing decision:

┌──────────────────────────────────────┬──────────────────────────────────────┐
│ EMBED (denormalize)                  │ REFERENCE (normalize)                │
│ ────────────────────────────────     │ ────────────────────────────────      │
│ {                                    │ orders: { customer_id: ObjectId(42) } │
│   order_id: 1,                       │ customers: { _id: ObjectId(42), ... } │
│   customer: {                        │                                       │
│     name:  "Alice",                  │ Use when:                             │
│     email: "a@b.com"                 │  • Referenced doc is large            │
│   },                                 │  • Referenced doc changes frequently  │
│   line_items: [                      │  • Many-to-many relationship          │
│     { product: "Widget",             │  • Need to query the referenced doc   │
│       qty: 2, price: 9.99 }          │    independently                      │
│   ]                                  │  • Embedding would exceed 16 MB limit │
│ }                                    │    (BSON document size limit)         │
│                                      │                                       │
│ Use when:                            │                                       │
│  • One-to-few (e.g. order→line items)│                                       │
│  • Always read together              │                                       │
│  • Sub-docs updated infrequently     │                                       │
│  • Single-document atomic update     │                                       │
│    is sufficient                     │                                       │
└──────────────────────────────────────┴──────────────────────────────────────┘

The guiding principle: model data the way your application queries it, not the
way normalization theory says it should be organized.

Bridge: in T-SQL/EF you normalize first and JOIN at query time.
In MongoDB you denormalize first and JOIN (embed) at insert time.
The write cost is higher; the read cost is lower.
```

**Schema-on-write vs schema-on-read** — the core mental model shift:

- **SQL Server = schema-on-write.** The storage engine enforces column names, data types, NOT NULL constraints, and referential integrity at write time. Invalid data is rejected at the database boundary. The schema is the contract, and the database is the enforcer.
- **MongoDB default = schema-on-read.** BSON accepts any document in any collection. The storage engine imposes no constraints. The application code is the schema contract — it decides which fields mean what. There is no database-level rejection of invalid structure.

In practice, this is not "schema-less" — it is "schema enforced at a different layer." Production MongoDB applications use application-level schema validation (Mongoose ODM, MongoDB's built-in JSON Schema validation, or Zod on the application side). The operational difference: schema migrations in SQL Server require `ALTER TABLE` DDL against the storage layer; schema migrations in MongoDB require application-code changes and potentially a backfill script that updates existing documents — the database itself doesn't care.

Data engineering vocabulary alignment: schema-on-read is the same concept used in Hadoop/data lake architectures where Parquet files have no enforced schema at storage time — the schema is inferred or declared at query time (Spark, Hive, Synapse serverless). MongoDB brings that pattern to a transactional document store.

---

## 13. Transactions (MongoDB 4.0+)

Multi-document ACID transactions. Requires replica sets (Atlas always uses replica sets). Sharded cluster transactions are supported but incur more overhead.

```javascript
const session = client.startSession();
try {
    await session.withTransaction(async () => {
        // Both operations succeed or both are rolled back
        await db.accounts.updateOne(
            { _id: fromAccountId },
            { $inc: { balance: -amount } },
            { session }                       // pass session to ALL operations in txn
        );
        await db.accounts.updateOne(
            { _id: toAccountId },
            { $inc: { balance: amount } },
            { session }
        );
    });
} finally {
    await session.endSession();
}
```

**Performance note:** Multi-document transactions use distributed locking and write to the oplog. They are significantly slower than equivalent transactions in PostgreSQL or SQL Server. Single-document operations are atomic by default. Design your schema to minimize the need for multi-document transactions — embed related data that must stay consistent.

---

## 14. Azure Cosmos DB for MongoDB — Bridge for Azure Engineers

Azure Cosmos DB for MongoDB is a wire-protocol-compatible MongoDB API layer hosted on Cosmos DB's native multi-model storage engine. A standard MongoDB driver connects to a Cosmos DB for MongoDB endpoint and runs standard MQL without modification — for most operations, it is transparent.

**What this means in practice:**
- `mongosh`, MongoDB Node.js driver, Mongoose, Motor (Python async) — all connect to Cosmos DB for MongoDB endpoints unchanged.
- Standard CRUD, aggregation pipeline, and index creation operations work as expected.
- The compatibility target is MongoDB 4.x / 5.x wire protocol. Not all 7.x features are supported — check the compatibility matrix before assuming new aggregation stages or index types work.

### Cosmos DB for MongoDB vs Native MongoDB — Key Differences

| Dimension | Native MongoDB (Atlas) | Azure Cosmos DB for MongoDB |
|---|---|---|
| **Billing unit** | vCore / memory / storage | Request Units (RUs) — measured per operation |
| **Capacity model** | Server-based (provisioned vCores or serverless) | RU-based (provisioned or autoscale) |
| **Partitioning** | Manual sharding (shard key choice is critical) | Automatic — partition key maps to physical partition, managed by Cosmos DB |
| **Consistency** | readConcern / writeConcern (eventual, majority, linearizable) | 5 consistency levels: Strong, Bounded Staleness, Session, Consistent Prefix, Eventual |
| **Change tracking** | Change Streams (resumable, oplog-based) | Change Feed (resumable, Cosmos DB native — similar semantics, different guarantees) |
| **Indexing** | Explicit index creation | All fields indexed by default (wildcard index) — turn off fields you don't need to reduce RU cost |
| **Transaction scope** | Multi-document within replica set / shard | Single partition — cross-partition transactions have limitations |
| **Global distribution** | Atlas Global Clusters (manual config) | Built-in multi-region with configurable consistency per read region |
| **SLA** | Atlas SLA (99.995% for multi-region) | Cosmos DB SLA: <10 ms p99 read, <15 ms p99 write at 99th percentile (provisioned) |

### RU Model — The Critical Operational Difference

Cosmos DB charges Request Units per operation. A point read (fetch by `_id`) costs 1 RU. A query that scans documents costs proportionally more based on data read and compute. This has direct schema design implications:

- **Embed data to minimize RUs per request.** A query that touches one document uses fewer RUs than one that requires `$lookup` across collections.
- **All-fields-indexed-by-default increases write RUs.** Every new field written to a document is indexed. For high-write workloads with many distinct fields, selectively excluding fields from indexing (using an indexing policy exclusion) reduces write cost.
- **RU provisioning is per-container.** Monitor RU consumption via Azure Monitor; throughput exceptions (429) mean the container is RU-starved.

### When to Use Cosmos DB for MongoDB vs Native MongoDB

| Scenario | Recommendation |
|---|---|
| Existing MongoDB application, want Azure hosting | Cosmos DB for MongoDB — minimal driver changes, Azure-native SLAs |
| New application, no existing MongoDB code | Cosmos DB Core SQL API (native) or MongoDB Atlas — avoid the compatibility layer |
| Need guaranteed single-digit ms latency SLAs | Cosmos DB — the SLA is contractual; MongoDB Atlas's latency depends on cluster tier |
| Need MongoDB 6.x+ features (latest operators, new index types) | MongoDB Atlas — Cosmos DB lags on compatibility |
| Multi-region active-active with configurable consistency | Cosmos DB — built-in, no extra config |
| Need Atlas Search (Lucene) or Atlas Vector Search | MongoDB Atlas — Cosmos DB has Azure Cognitive Search as a separate service |

### Change Feed vs Change Streams

MongoDB Change Streams: subscribe to a collection's oplog. Resumable via a resume token. Standard MongoDB driver API.

Cosmos DB Change Feed: Cosmos DB's native event log. Exposed to the MongoDB API via Change Streams (compatible surface), but the underlying guarantees differ: Change Feed is append-only and ordered per logical partition, not globally ordered. Multi-region scenarios introduce per-region feeds. If your application depends on global ordering of change events, test this against your consistency level before assuming equivalence.

---

## 15. Decision Cheat Sheet

| Use MongoDB when | Use a relational DB instead when |
|-----------------|----------------------------------|
| Schema is variable or evolving rapidly | Schema is stable, highly normalized |
| Data is naturally hierarchical (orders + line items) | Query patterns are JOIN-heavy reporting |
| Need to embed sub-documents for read performance | Strong multi-table ACID transactions are frequent |
| Horizontal sharding at extreme scale | Many-to-many relationships dominate the model |
| Atlas Search + Vector Search in one platform | Strict referential integrity required |
| Geospatial queries are core to the app | T-SQL ecosystem (SSRS, SSAS, stored procedures) |
| Flexible content models (CMS, product catalog) | Already on Azure → Cosmos DB may be better fit |

---

## 16. Common Confusion Points

**"Schema-less" is a misnomer.** Documents in a collection should have a consistent structure for query efficiency. MongoDB doesn't enforce schema at the DB level — the application code becomes the schema contract. In practice, use a schema validation library (Mongoose, Zod + MongoDB driver) to enforce it at the application layer.

**`$set` is required for partial updates.** `updateOne({filter}, { field: "value" })` without `$set` will REPLACE the entire document with `{ field: "value" }`, destroying all other fields. Always use `$set` for partial updates.

**`{ field: null }` matches two cases.** It matches documents where the field is `null` AND documents where the field does not exist. To distinguish: `{ field: { $exists: true, $eq: null } }` for "field is present but null"; `{ field: { $exists: false } }` for "field is absent."

**`$elemMatch` vs direct array condition.** `{ scores: { $gt: 80, $lt: 90 } }` finds documents where any element > 80 AND (independently) any element < 90 — they can be different elements. `{ scores: { $elemMatch: { $gt: 80, $lt: 90 } } }` requires a single element to satisfy both conditions simultaneously.

**`$lookup` output is always an array.** Even when the join should produce exactly one match, the `as` field is an array. Always follow with `{ $unwind: { path: "$field", preserveNullAndEmpty: true } }` to get a single document — or use `{ $arrayElemAt: ["$field", 0] }`.

**`$unwind` removes documents with empty arrays by default.** A document with `tags: []` or `tags: null` is dropped by `{ $unwind: "$tags" }`. Use `{ $unwind: { path: "$tags", preserveNullAndEmpty: true } }` to preserve them.

**Aggregation pipeline order is not commutative.** Put `$match` before `$group` and `$lookup` to filter early. A `$match` after a `$group` acts as `HAVING`. A `$sort` before `$limit` is the pattern for top-N.

**`_id` is always returned by `find()`.** Include `{ _id: 0 }` in the projection to suppress it. Exception: you cannot simultaneously include some fields and exclude others (except `_id`).

**Transactions are not free.** Architect the data model to avoid them. The fundamental MongoDB performance advantage (single-document atomicity via embedding) disappears when you use multi-document transactions at high frequency.

**DocumentDB is not MongoDB.** AWS DocumentDB implements a MongoDB 3.x-compatible API but has compatibility gaps in aggregation pipeline stages, index types, and transaction semantics. Test your application directly against DocumentDB — don't assume full compatibility.

**ObjectId is not an integer.** The auto-generated `_id` is a 12-byte ObjectId: 4-byte Unix timestamp + 5-byte random + 3-byte counter. It sorts lexicographically by creation time, which makes it a useful de facto timestamp. You can use any unique value as `_id` (string, integer, compound object) — just provide it explicitly on insert.
