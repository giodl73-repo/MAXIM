# 02 — Pandas

> Pandas is a labeled ndarray with a query engine bolted on.
> Once you see it that way, the API stops being arbitrary.

---

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PANDAS DATA MODEL                                   │
│                                                                             │
│  DataFrame = dict of Series sharing an Index                               │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Index    │  col_A  │  col_B  │  col_C  │  ...                     │   │
│  │  ─────────┼─────────┼─────────┼─────────┼──────────────────────    │   │
│  │  "a"      │  1.0    │  "foo"  │  True   │                          │   │
│  │  "b"      │  2.0    │  "bar"  │  False  │                          │   │
│  │  "c"      │  3.0    │  "baz"  │  True   │                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│       │           │          │         │                                   │
│     Index      Series     Series    Series  ← each column is a Series     │
│   (labels)   (float64) (object_)  (bool_)    with the same Index          │
│                                                                             │
│  EXECUTION LAYERS                                                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                     │
│  │   Pandas     │  │    NumPy     │  │    Arrow     │                     │
│  │  (labeled    │  │  (homogeneous│  │  (columnar   │                     │
│  │   ops, SQL-  │  │   C arrays)  │  │   format,    │                     │
│  │   style API) │  │              │  │   Pandas 2+) │                     │
│  └──────────────┘  └──────────────┘  └──────────────┘                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

Pandas 2.0 (2023) switched the default backend from NumPy to Apache Arrow for
many dtypes. Arrow uses a columnar memory format that is more efficient for
string columns, nullable integers, and large datasets. The API is unchanged.

---

## Series

A Series is a 1-D labeled array. Think of it as a NumPy array with an index.

```python
import pandas as pd
import numpy as np

# Creation
s = pd.Series([10, 20, 30], index=["a", "b", "c"], name="values")
s2 = pd.Series({"a": 10, "b": 20, "c": 30})  # dict → Series

# Access
s["b"]          # 20 — label-based
s[1]            # 20 — positional (deprecated for non-integer index)
s.iloc[1]       # 20 — always positional
s.loc["b"]      # 20 — always label-based

# Operations are automatically aligned by index
s3 = pd.Series([1, 2, 3], index=["b", "c", "d"])
s + s3
# a    NaN   ← "a" only in s
# b    22.0  ← 20 + 2
# c    32.0  ← 30 + 3 (wait: s["c"]=30, s3["c"]=3... s["c"]=30, s3["b"]=2, s3["c"]=3
# d    NaN   ← "d" only in s3

# Index alignment is the killer feature and the surprise behavior
```

---

## DataFrame Construction

```python
# From dict of lists (most common)
df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Carol"],
    "score":  [95.0, 82.0, 88.0],
    "passed": [True, True, True],
})

# From list of dicts
df2 = pd.DataFrame([
    {"name": "Alice", "score": 95.0},
    {"name": "Bob",   "score": 82.0},
])

# From NumPy array
arr = np.random.rand(5, 3)
df3 = pd.DataFrame(arr, columns=["x", "y", "z"])

# From CSV / Parquet / JSON / SQL
df = pd.read_csv("data.csv", dtype={"id": "int32", "score": "float32"})
df = pd.read_parquet("data.parquet")
df = pd.read_sql("SELECT * FROM users", con=engine)  # SQLAlchemy engine

# Inspection
df.shape          # (3, 3)
df.dtypes         # dtype per column
df.info()         # dtypes + null counts + memory usage
df.describe()     # count/mean/std/min/quartiles/max for numeric cols
df.head(5)        # first 5 rows
df.tail(5)        # last 5 rows
df.sample(5)      # 5 random rows
```

---

## Indexing: `.loc`, `.iloc`, `[]`

This is the most confusing part of Pandas. Three indexers with overlapping behavior:

```
┌────────────────────────────────────────────────────────────────────┐
│  INDEXER   │  ROWS           │  COLUMNS        │  RETURNS         │
├────────────┼─────────────────┼─────────────────┼──────────────────┤
│  df[col]   │  —              │  label only     │  Series          │
│  df[cols]  │  —              │  list of labels │  DataFrame       │
│  df[slice] │  integer slice  │  —              │  DataFrame (rows)│
│            │  (DEPRECATED)   │                 │                  │
│  .loc[]    │  label-based    │  label-based    │  Series/DataFrame│
│  .iloc[]   │  integer-based  │  integer-based  │  Series/DataFrame│
│  .at[]     │  single label   │  single label   │  scalar (fast)   │
│  .iat[]    │  single integer │  single integer │  scalar (fast)   │
└────────────┴─────────────────┴─────────────────┴──────────────────┘
```

```python
df = pd.DataFrame({"A": [1,2,3], "B": [4,5,6], "C": [7,8,9]},
                   index=["x", "y", "z"])

# Column access
df["A"]           # Series
df[["A", "C"]]    # DataFrame with two columns

# .loc — label-based, INCLUSIVE on both ends
df.loc["x"]            # row "x" as Series
df.loc["x":"y"]        # rows x and y (inclusive end!)
df.loc["x":"y", "A":"B"]   # rows x-y, cols A-B

# .iloc — integer-based, exclusive end (like Python slicing)
df.iloc[0]             # first row
df.iloc[0:2]           # rows 0 and 1 (not 2)
df.iloc[0:2, 0:2]      # top-left 2×2 subgrid

# Boolean mask with .loc
mask = df["A"] > 1
df.loc[mask]           # rows where A > 1
df.loc[mask, "B"]      # just column B for those rows

# Assignment — always use .loc/.iloc to avoid SettingWithCopyWarning
df.loc[mask, "A"] = 0  # correct
df[mask]["A"] = 0      # WRONG — may write to a copy (chained indexing)
```

The `SettingWithCopyWarning` is Pandas' way of saying: chained indexing
(`df[condition]["col"] = value`) may or may not modify the original, depending
on whether the first selection returned a view or a copy. Always use `.loc`.

---

## Data Types and Casting

```python
df.dtypes             # shows dtype of each column

# Cast
df["score"] = df["score"].astype("float32")
df["id"] = df["id"].astype("int32")
df["category"] = df["category"].astype("category")  # CategoricalDtype → memory savings

# Pandas 2 nullable types (vs NumPy types)
# NumPy int64 cannot represent NaN — NaN forces float64
# Pandas Int64 (capital I) = nullable integer
df["count"] = df["count"].astype("Int64")   # nullable, can hold NA
df["flag"] = df["flag"].astype("boolean")   # nullable bool

# String types
df["name"].dtype      # object_ in Pandas 1; ArrowDtype in Pandas 2
df["name"] = df["name"].astype("string")    # StringDtype — better performance

# Check memory usage
df.memory_usage(deep=True).sum()   # bytes including string content
```

---

## Missing Data

```python
df.isna()              # boolean DataFrame of NaN locations
df.isna().sum()        # count of NaNs per column
df.notna()

# Drop
df.dropna()                      # drop rows with any NaN
df.dropna(subset=["score"])      # only where score is NaN
df.dropna(axis=1)                # drop columns with any NaN

# Fill
df.fillna(0)                     # replace all NaN with 0
df["score"].fillna(df["score"].mean())   # fill with column mean
df.ffill()                       # forward fill (propagate last valid)
df.bfill()                       # backward fill

# Interpolate (numeric columns)
df["score"].interpolate(method="linear")
```

---

## Filtering and Querying

```python
# Boolean indexing
df[df["score"] >= 90]
df[(df["score"] >= 80) & (df["passed"] == True)]   # use & | ~ not and/or/not
df[df["name"].isin(["Alice", "Carol"])]
df[~df["name"].isin(["Bob"])]                       # ~ = NOT

# .query() — string expression (eval'd, slightly faster for large DataFrames)
df.query("score >= 80 and passed == True")
df.query("name in @names_list")   # @ references Python variable

# str accessor — vectorized string operations
df[df["name"].str.startswith("A")]
df[df["name"].str.contains("li", case=False)]
df["name"].str.upper()
df["name"].str.split(" ", expand=True)  # split into multiple columns
df["name"].str.len()
```

---

## Operations and Apply

```python
# Column-wise arithmetic (vectorized)
df["adjusted"] = df["score"] * 1.1
df["z_score"] = (df["score"] - df["score"].mean()) / df["score"].std()

# apply — row-wise or column-wise Python function (slow; avoid if possible)
df["grade"] = df["score"].apply(lambda x: "A" if x >= 90 else "B")
df["combined"] = df.apply(lambda row: f"{row['name']}:{row['score']}", axis=1)

# map — element-wise on Series
grade_map = {"A": 4.0, "B": 3.0, "C": 2.0}
df["gpa"] = df["grade"].map(grade_map)

# assign — method-chaining friendly (returns new DataFrame)
df = (df
    .assign(adjusted=df["score"] * 1.1)
    .assign(z_score=lambda x: (x["score"] - x["score"].mean()) / x["score"].std())
    .rename(columns={"name": "student_name"})
)
```

### Method Chaining Pattern

```python
result = (
    pd.read_csv("grades.csv")
    .rename(columns=str.lower)
    .dropna(subset=["score"])
    .query("score >= 60")
    .assign(grade=lambda df: pd.cut(df["score"],
                                     bins=[0, 60, 70, 80, 90, 100],
                                     labels=["F","D","C","B","A"]))
    .groupby("grade")["score"]
    .agg(["count", "mean"])
    .round(2)
)
```

Method chaining reads as a data pipeline — the same mental model as ADF pipelines
or LINQ chains. Each step produces a new DataFrame; nothing mutates in place.

---

## GroupBy

GroupBy is pandas' implementation of the split-apply-combine pattern:

```
split  → partition rows by key(s)
apply  → compute something within each group
combine → collect results back into a DataFrame/Series
```

```python
df = pd.read_csv("sales.csv")

# Single key
by_region = df.groupby("region")

# Aggregation
by_region["revenue"].sum()             # Series: region → total revenue
by_region["revenue"].mean()
by_region.agg({"revenue": "sum", "units": "mean"})  # multiple cols

# Named aggregation (Pandas 0.25+)
by_region.agg(
    total_rev=("revenue", "sum"),
    avg_units=("units", "mean"),
    n_orders=("order_id", "count"),
)

# Multiple keys
df.groupby(["region", "product"])["revenue"].sum()

# Transform — returns same-shape result (for adding group stats back to df)
df["region_mean"] = df.groupby("region")["revenue"].transform("mean")
df["deviation"] = df["revenue"] - df["region_mean"]

# Filter — keep groups satisfying a condition
large_regions = df.groupby("region").filter(lambda g: g["revenue"].sum() > 1_000_000)

# Apply — arbitrary function per group (slowest; last resort)
def top_n(group, n=3):
    return group.nlargest(n, "revenue")

df.groupby("region").apply(top_n, n=3)
```

---

## Merge and Join

Pandas' merge is relational JOIN, not matrix concatenation:

```python
orders = pd.DataFrame({"order_id": [1,2,3], "customer_id": [101,102,101], "amount": [50,30,70]})
customers = pd.DataFrame({"customer_id": [101,102,103], "name": ["Alice","Bob","Carol"]})

# Inner join (default)
pd.merge(orders, customers, on="customer_id")

# All join types
pd.merge(orders, customers, on="customer_id", how="inner")   # matching rows only
pd.merge(orders, customers, on="customer_id", how="left")    # all orders + matched customers
pd.merge(orders, customers, on="customer_id", how="right")   # all customers + matched orders
pd.merge(orders, customers, on="customer_id", how="outer")   # all rows, NaN where no match

# Different key names
pd.merge(orders, customers,
         left_on="customer_id", right_on="id")

# Join on index
orders.join(customers.set_index("customer_id"), on="customer_id")

# Concatenate (stack rows or columns)
pd.concat([df1, df2], axis=0)          # stack vertically (add rows)
pd.concat([df1, df2], axis=1)          # stack horizontally (add columns)
pd.concat([df1, df2], ignore_index=True)  # reset integer index
```

---

## Reshaping

```python
df = pd.DataFrame({
    "student": ["Alice","Alice","Bob","Bob"],
    "subject": ["math","english","math","english"],
    "score":   [90, 85, 78, 92]
})

# Pivot — long to wide
wide = df.pivot(index="student", columns="subject", values="score")
#          english  math
# Alice       85    90
# Bob         92    78

# Pivot table — like Excel pivot table; handles duplicates with aggregation
pt = df.pivot_table(index="student", columns="subject",
                     values="score", aggfunc="mean")

# Melt — wide to long (inverse of pivot)
long = wide.reset_index().melt(id_vars="student",
                                var_name="subject",
                                value_name="score")

# Stack / unstack — move index level to columns or back
stacked = wide.stack()     # MultiIndex Series
unstacked = stacked.unstack()  # back to DataFrame

# Explode — expand list-valued cells into rows
df2 = pd.DataFrame({"id": [1, 2], "tags": [["a","b"], ["c"]]})
df2.explode("tags")
# id  tags
# 1   a
# 1   b
# 2   c
```

---

## Time Series

Pandas has first-class support for time-indexed data:

```python
# Parse dates on read
df = pd.read_csv("prices.csv", parse_dates=["date"], index_col="date")

# Date range index
dates = pd.date_range("2024-01-01", periods=365, freq="D")
dates_business = pd.bdate_range("2024-01-01", "2024-12-31")

# Resampling (temporal groupby)
daily = df.resample("D")["price"].mean()     # daily average
weekly = df.resample("W")["price"].ohlc()   # open/high/low/close per week
monthly = df.resample("ME")["price"].last() # month-end

# Rolling windows
df["7d_ma"] = df["price"].rolling(window=7).mean()
df["30d_std"] = df["price"].rolling(window=30).std()
df["expanding_mean"] = df["price"].expanding().mean()  # cumulative

# Shift and diff
df["prev_price"] = df["price"].shift(1)
df["daily_return"] = df["price"].pct_change()    # (t - t-1) / t-1
df["log_return"] = np.log(df["price"]).diff()

# Time zone handling
df.index = df.index.tz_localize("UTC")
df_eastern = df.tz_convert("US/Eastern")

# Period indexing
df.index = df.index.to_period("M")   # monthly periods
```

---

## Performance

Pandas is slow when misused. The hierarchy:

```
┌─────────────────────────────────────────────────────────────────────┐
│  FAST  ← ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ►  SLOW │
│                                                                     │
│  Vectorized   eval()    apply()   itertuples()  iterrows()  loop   │
│  numpy ops    (numexpr)  (Python   (named        (Series     over  │
│                          func)     tuples)        per row)   rows  │
└─────────────────────────────────────────────────────────────────────┘
```

### `iterrows` is the performance anti-pattern

```python
# NEVER do this for computation
for idx, row in df.iterrows():
    df.at[idx, "result"] = row["a"] + row["b"]  # 1000× slower than vectorized

# Do this
df["result"] = df["a"] + df["b"]
```

### Key Patterns

```python
# 1. Use categorical dtype for low-cardinality string columns
df["status"] = df["status"].astype("category")
# Memory: N strings → N ints + small lookup table
# GroupBy on categoricals is dramatically faster

# 2. Use correct numeric dtypes at read time
df = pd.read_csv("data.csv", dtype={"id": "int32", "score": "float32"})
# Halves memory for int and float columns

# 3. pd.eval() for complex column arithmetic (uses numexpr, multithreaded)
result = pd.eval("a**2 + b**2 - 2*a*b")   # module-level
df.eval("c = a**2 + b**2", inplace=True)   # DataFrame method

# 4. Chunked reading for files that don't fit in memory
chunks = pd.read_csv("huge.csv", chunksize=100_000)
result = pd.concat(
    (chunk.groupby("key")["val"].sum() for chunk in chunks)
).groupby(level=0).sum()

# 5. Parquet > CSV for everything except human-readable exchange
df.to_parquet("data.parquet")           # columnar, compressed, typed
df = pd.read_parquet("data.parquet")    # column selection available
df = pd.read_parquet("data.parquet",
                      columns=["id", "score"])  # read only needed columns
```

### When to Move Off Pandas

```
┌─────────────────────────────────────────────────────────────────────┐
│  SITUATION                    │  ALTERNATIVE                       │
├───────────────────────────────┼────────────────────────────────────┤
│  > 1GB data, single machine   │  Polars (Rust, lazy eval, faster)  │
│  > memory data, distributed   │  Dask, Spark, Modin                │
│  Columnar analytics SQL-style │  DuckDB (in-process, very fast)    │
│  Need true SQL semantics      │  DuckDB or SQLite                  │
│  NumPy operations on arrays   │  NumPy directly (skip Pandas)      │
│  Streaming / incremental      │  Polars streaming mode             │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Polars — The Modern Alternative

Polars deserves mention here rather than a separate file. Drop-in for most Pandas
workflows with dramatically better performance:

```python
import polars as pl

# Lazy evaluation — builds a query plan, optimizes, then executes
result = (
    pl.scan_csv("data.csv")      # lazy (no data read yet)
    .filter(pl.col("score") >= 80)
    .group_by("region")
    .agg([
        pl.col("revenue").sum().alias("total"),
        pl.col("revenue").mean().alias("avg"),
    ])
    .sort("total", descending=True)
    .collect()                   # execute the plan
)

# Polars expressions are composable and type-safe
df.with_columns([
    (pl.col("score") * 1.1).alias("adjusted"),
    pl.col("name").str.to_uppercase().alias("NAME"),
])

# No index concept — Polars DataFrames have no row labels
# No SettingWithCopyWarning — Polars is immutable by design
```

**Key differences from Pandas:**
- Lazy evaluation by default (scan → collect)
- No mutable operations — everything returns a new DataFrame
- No row index — select rows by value, not label
- Expression API rather than method chaining on column subsets
- 5–20× faster than Pandas for most operations; parallelized by default

---

## Common Confusion Points

**`.loc` includes the end, `.iloc` excludes it**: `df.loc["a":"c"]` returns rows
a, b, and c. `df.iloc[0:3]` returns rows 0, 1, 2. Inconsistent by design — labels
have no natural "one past the end."

**Index alignment in arithmetic**: When you add two Series, Pandas aligns on the
index first. If you want NumPy-style positional arithmetic, use `.values` to
extract the underlying array and lose the index.

**`apply` is not vectorized**: Despite accepting a function and running it over
each row/column, `apply` is a Python loop. It is convenient but slow. Use it
only when a vectorized alternative doesn't exist.

**Chained indexing and `SettingWithCopyWarning`**: `df[condition]["col"] = val`
silently may or may not update the original. Pandas 3.0 will make this always
a copy (Copy-on-Write semantics). Use `.loc[condition, "col"] = val` now.

**`groupby` returns a GroupBy object, not data**: `df.groupby("x")` is lazy.
You must chain an aggregation: `.sum()`, `.mean()`, `.agg()`, etc.

**object dtype strings are slow**: A column of strings stored as `object_` has
one Python string object per cell — no vectorization possible. Cast to
`"string"` (StringDtype) or `"category"` for better performance.

---

## Decision Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────────┐
│  TASK                           │  APPROACH                        │
├─────────────────────────────────┼──────────────────────────────────┤
│  Select single column           │  df["col"]                       │
│  Select by label, safe write    │  df.loc[rows, cols]              │
│  Select by position             │  df.iloc[rows, cols]             │
│  Filter rows                    │  df[mask] or df.query("...")     │
│  Grouped aggregation            │  df.groupby("k").agg(...)        │
│  Add group stat to original     │  groupby().transform()           │
│  Long → wide                    │  df.pivot(index, columns, values)│
│  Wide → long                    │  df.melt(id_vars, value_vars)    │
│  Join two DataFrames            │  pd.merge(left, right, on, how)  │
│  Stack rows                     │  pd.concat([df1, df2], axis=0)   │
│  Temporal groupby               │  df.resample("W").mean()         │
│  Rolling window                 │  df["col"].rolling(7).mean()     │
│  String ops                     │  df["col"].str.contains(...)     │
│  Avoid SettingWithCopyWarning   │  df.loc[mask, "col"] = val       │
├─────────────────────────────────┼──────────────────────────────────┤
│  PERFORMANCE                    │                                  │
│  Low-cardinality strings        │  .astype("category")             │
│  Float/int columns              │  dtype=float32/int32 at read     │
│  Complex arithmetic             │  pd.eval() / df.eval()           │
│  File format                    │  Parquet > CSV always            │
│  > 1GB or need speed            │  Switch to Polars                │
└─────────────────────────────────┴──────────────────────────────────┘
```
