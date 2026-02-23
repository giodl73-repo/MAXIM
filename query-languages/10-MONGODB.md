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

// $bucket — group into ranges (histogram)
{ $bucket: {
    groupBy:    "$total",
    boundaries: [0, 50, 100, 500, 1000],
    default:    "1000+",
    output:     { count: { $sum: 1 }, avg_total: { $avg: "$total" }}
}}

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
```

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

## 14. Decision Cheat Sheet

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

## 15. Common Confusion Points

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
