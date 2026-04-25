# Language: Python

> Readability first — dynamic typing, batteries included, and a culture that values clarity over cleverness. The dominant language for data science, scripting, and AI.

---

## Type System Snapshot

| Axis | Python |
|------|--------|
| Binding | Late — everything is a runtime attribute lookup via `__dict__` |
| Typing | Dynamic |
| Strength | Strong — no implicit coercions (`"1" + 1` raises TypeError) |
| Type system | Duck typing (check at runtime by hasattr) |
| Type inference | None at runtime; mypy/pyright for static analysis of hints |
| Memory model | Reference counting + cycle-detecting GC; GIL (CPython) |

---

## Python Execution Model & Ecosystem Landscape

```
SOURCE                 COMPILATION              RUNTIME
─────────────────────────────────────────────────────────────────────────

 your_module.py   ──►  CPython compiler  ──►  .pyc bytecode cache
  (UTF-8 text)          (built into             (__pycache__/)
                         CPython)
                                          ──►  CPython VM (interpreter)
                                               ┌─────────────────────┐
                                               │  Bytecode evaluator │
                                               │  ┌───────────────┐  │
                                               │  │  GIL          │   │
                                               │  │ (one thread   │   │
                                               │  │  runs Python  │   │
                                               │  │  bytecode at  │   │
                                               │  │  a time)      │   │
                                               │  └───────────────┘   │
                                               │  Reference-counted   │
                                               │  heap + cycle GC     │
                                               └─────────────────────┘

ALTERNATIVE RUNTIMES:
  CPython  — default, C implementation, the GIL lives here
  PyPy     — JIT compiler, 5-10x faster for CPU-bound loops, same .py source
  Jython   — runs on JVM, true threads (no GIL), Java interop
  GraalPy  — GraalVM polyglot, experimental

─────────────────────────────────────────────────────────────────────────
C# COMPARISON: IL → CLR JIT → native code (true OS threads, no GIL)
Python:        .py → bytecode → interpreter (GIL limits thread parallelism)

GIL IMPACT ON CONCURRENCY:
  I/O-bound work   → threading or asyncio works fine (GIL released on I/O)
  CPU-bound work   → use multiprocessing (separate processes, each with own GIL)
                     or PyPy, or C extensions that release the GIL (NumPy does)
  Python 3.13+     → experimental "free-threaded" build (--disable-gil) available

─────────────────────────────────────────────────────────────────────────
PACKAGING ECOSYSTEM:

 pyproject.toml          ← project metadata + dependencies (PEP 517/518)
 (or setup.py legacy)
       │
       ▼
   pip / uv / poetry     ← installers / resolvers
       │
       ▼
  PyPI (pypi.org)        ← package registry (like NuGet)
       │
       ▼
  .venv/  (virtualenv)   ← isolated environment per project
  site-packages/         ← installed packages live here

  Wheel (.whl)  — pre-built binary distribution (fast install)
  sdist (.tar.gz) — source distribution (requires build step)
```

## Syntax Reference Card

### Variables & Types
```python
x = 5                       # no declaration keyword
x: int = 5                  # type hint (annotation — NOT enforced at runtime)
x: int                      # annotate without assigning (variable doesn't exist yet)

# Constants: uppercase by convention — Python has no enforcement
MAX_SIZE = 100
PI = 3.14159

# Multiple assignment
a = b = c = 0
a, b = 1, 2                 # tuple unpacking
a, *rest = [1, 2, 3, 4]     # a=1, rest=[2,3,4]
_, b, _ = (1, 2, 3)         # _ discards

# Built-in types
bool: True, False            # subclass of int! True==1, False==0
int: arbitrary precision     # no overflow
float: 64-bit IEEE 754
complex: 3+4j
str: immutable Unicode
bytes: b"raw bytes"
bytearray: mutable bytes
NoneType: None               # the null
```

### Equality & Comparison
```python
# == calls __eq__ — value equality
[1,2,3] == [1,2,3]          # True (different objects, same content)

# is checks identity (same object)
a is None                    # ✅ use is for None/True/False
a is not None

# !! Never use == None
x == None                    # works but wrong style (mypy warns)
x is None                    # correct ✅

# Comparison chaining — Python unique feature!
1 < x < 10                  # True if 1 < x AND x < 10 (short-circuit)
a < b < c < d               # all three comparisons

# Object identity
id(a) == id(b)              # same address (roughly like ReferenceEquals)

# is vs == for small ints — Python caches -5 to 256
a = 256; b = 256; a is b    # True (cached!)
a = 257; b = 257; a is b    # False (NOT cached)
```

### Logical Operators
```python
and     # short-circuit AND — returns OPERAND, not bool!
or      # short-circuit OR — returns OPERAND, not bool!
not     # logical NOT — always returns bool

# The operand-returning behavior is a Python idiom
name = input_name or "default"      # "default" if input_name is falsy
value = x if x is not None else 0  # explicit ternary (preferred)

# Falsy values: False, None, 0, 0.0, "", [], {}, set(), ()
# Everything else is truthy

# Bitwise
&   |   ^   ~   <<   >>     # work on ints (and sets!)
{1,2,3} & {2,3,4}           # set intersection (overloaded &)
{1,2,3} | {2,3,4}           # set union (overloaded |)
```

### Collections
```python
# List — mutable, ordered, heterogeneous allowed
lst = [1, 2, 3]
lst.append(4)
lst.extend([5, 6])
lst.insert(0, 0)
lst.pop()                    # remove last
lst[0]  lst[-1]             # first, last
lst[1:3]                    # slice: [2, 3]
lst[::-1]                   # reverse
len(lst)

# Tuple — immutable, ordered
t = (1, 2, 3)
t = 1, 2, 3                  # parens optional
t = (1,)                     # single-element tuple (trailing comma required)
t = ()                       # empty tuple

# Dict — mutable, ordered (Python 3.7+), hash map
d = {"key": "value", "n": 42}
d["key"]                     # get — KeyError if missing
d.get("key")                 # get — None if missing
d.get("key", "default")      # with default
d["new"] = "val"             # set
del d["key"]                 # delete
"key" in d                   # membership
d.keys()  d.values()  d.items()
{**d1, **d2}                 # merge (Python 3.9+: d1 | d2)

# Set — mutable, unordered, unique
s = {1, 2, 3}
s = set()                    # empty set (NOT {} — that's empty dict!)
s.add(4)
s.remove(4)                  # KeyError if missing
s.discard(4)                 # no error if missing
s & t  s | t  s - t  s ^ t  # intersection, union, difference, symmetric diff

# Comprehensions
squares = [x**2 for x in range(10) if x % 2 == 0]
sq_dict = {x: x**2 for x in range(5)}
sq_set  = {x**2 for x in range(5)}
gen = (x**2 for x in range(5))   # generator (lazy)
```

### Control Flow
```python
if cond:                    # no parens, colon, indentation
    ...
elif cond2:
    ...
else:
    ...

# Ternary (conditional expression)
value = t if cond else f

# Match statement (Python 3.10+) — structural pattern matching
match command:
    case "quit":
        quit()
    case ("go", direction):             # sequence pattern
        move(direction)
    case {"action": action, **rest}:    # mapping pattern
        handle(action)
    case Point(x=x, y=y) if x > 0:    # class pattern + guard
        handle_positive(x, y)
    case _:
        print("unknown")

# Loops
for item in iterable:
    ...
for i, item in enumerate(lst):
    ...
for k, v in dict.items():
    ...

while cond:
    ...

# Loop control
break       # exit loop
continue    # next iteration
else:       # runs if loop completed without break (unusual feature)
    ...

# Exception: no do-while in Python
```

### Strings & Characters
```python
# str — immutable, Unicode (UTF-8 in source, internal representation varies)
s = "hello"                 # double quotes
s = 'hello'                 # single quotes (equivalent)
s = """multi
line"""                     # triple-quoted (also triple single)
s = f"Hello, {name}!"       # f-string (Python 3.6+)
s = f"Result: {2 + 2}"      # any expression
s = f"Debug: {val!r}"       # !r calls repr(), !s calls str(), !a calls ascii()
s = r"\no\escape"           # raw string (no escape processing)
s = b"bytes"                # bytes literal (NOT str — different type)

# String operations
len(s)                      # character count (Unicode, not bytes)
s.upper()  s.lower()  s.title()
s.strip()  s.lstrip()  s.rstrip()
s.split(",")                # list of strings
",".join(["a", "b"])        # "a,b"
s.replace("old", "new")
s.startswith("prefix")
s.find("sub")               # -1 if not found
s.count("sub")
s[0]                        # single char (str, not char type)
s[1:4]                      # slice
s[::-1]                     # reverse

# No char type — indexing returns a one-character string
# ord("A") = 65  chr(65) = "A"

# f-string format spec
f"{3.14159:.2f}"            # "3.14"
f"{1000000:,}"              # "1,000,000"
f"{42:08b}"                 # "00101010" (binary, zero-padded)
f"{'left':<10}"             # "left      " (left-aligned)
```

### Null / None
```python
None                        # the null object (NoneType)
x is None                   # correct null check ✅
x is not None

# Optional in type hints (3.9+ style)
from typing import Optional
def f(x: Optional[str]) -> str:    # Optional[str] = str | None
    ...
def f(x: str | None) -> str:      # newer syntax (3.10+)
    ...

# Default argument pattern
def f(x=None):
    if x is None:
        x = []          # CORRECT: don't use mutable default!

# Common pattern: x or default
name = user.name or "Anonymous"    # works but uses truthiness not None-check
name = user.name if user.name is not None else "Anonymous"  # more precise
```

### Functions
```python
def f(x):
    return x

# Default arguments
def f(x, y=5, z=None):
    ...

# *args and **kwargs
def f(*args, **kwargs):
    for arg in args: ...
    for k, v in kwargs.items(): ...

# Keyword-only args (after *)
def f(x, *, name, verbose=False):
    ...
f(1, name="foo")            # name must be keyword

# Positional-only (before /)
def f(x, y, /, z):
    ...

# Type hints
def add(a: int, b: int) -> int:
    return a + b

# Lambda
double = lambda x: x * 2
add = lambda x, y: x + y

# Decorators
@property
def name(self): return self._name

@staticmethod
def create(): ...

@classmethod
def from_string(cls, s): ...

# Async
async def fetch(url: str) -> str:
    return await client.get(url)
```

### Error Handling
```python
# EAFP style (Easier to Ask Forgiveness than Permission) — preferred in Python
try:
    value = d["key"]
except KeyError as e:
    value = "default"
except (TypeError, ValueError) as e:
    log(str(e))
    raise                       # re-raise
except Exception as e:
    raise RuntimeError("wrapped") from e  # chain
else:
    use(value)                  # runs if no exception
finally:
    cleanup()                   # always runs

# LBYL style (Look Before You Leap) — less Pythonic
if "key" in d:
    value = d["key"]

# Context managers (like C# using)
with open("file.txt") as f:
    data = f.read()

# Custom exception
class AppError(Exception):
    def __init__(self, msg, code):
        super().__init__(msg)
        self.code = code
```

---

## What Makes It Distinct

1. **Everything is an object** — including `int`, `function`, `class`, `module`. No primitives vs objects duality.
2. **GIL (CPython)** — Global Interpreter Lock means only one thread runs Python bytecode at a time. Use `multiprocessing` or `asyncio` for parallelism. (GIL being removed in Python 3.13+ experimental)
3. **Dynamic attribute lookup** — `obj.method()` looks up `method` in `obj.__dict__`, then `type(obj).__dict__`, then through MRO at runtime. No vtable. Hugely flexible, slow relative to static dispatch.
4. **Duck typing + protocols** — `typing.Protocol` lets you write structural types for type checkers without changing runtime behavior. No inheritance required.
5. **Comprehensions + generators** — list/dict/set comprehensions and generator expressions are core idioms. `yield` generators enable lazy evaluation natively.

---

## Ecosystem

| Tool | Purpose |
|------|---------|
| pip / uv | Package management |
| venv / poetry / uv | Virtual environments |
| mypy / pyright | Static type checking |
| pytest | Testing |
| FastAPI / Django / Flask | Web frameworks |
| NumPy / Pandas | Data science |
| scikit-learn / PyTorch / TensorFlow | ML |
| Ruff | Fast linter + formatter |

---

## Gotchas from C#

| C# behavior | Python behavior | Consequence |
|-------------|----------------|-------------|
| `==` on strings is value equality | Same — `==` is value | Fine here |
| `null` check with `==` | `None` check should use `is` | `x == None` works but style violation |
| No implicit conversions | `True == 1` — bool IS int | `1 + True = 2` (surprising) |
| Integer overflow throws (checked) | Integers are arbitrary precision | No overflow, but boxing overhead |
| `using` / `IDisposable` | `with` / `__enter__`/`__exit__` | Different protocol |
| Mutable default arguments safe | **Mutable default args are shared!** | `def f(x=[])` — `x` is ONE list shared across calls |
| `async Task<T>` | `async def` returns coroutine | Must `await` or use `asyncio.run()` |

---

## When to Choose Python

| Scenario | Python | C# | Reason |
|----------|--------|----|--------|
| Data science / ML / AI | **Yes** — numpy, pandas, PyTorch, scikit-learn | No real ecosystem | Python is the lingua franca of ML research and production. No competition. |
| Scripting / automation / glue | **Yes** — batteries-included stdlib, dynamic typing speeds iteration | Possible but verbose | `pathlib`, `subprocess`, `requests`, `json` out of the box. Dynamic typing is an asset for one-off scripts. |
| ML-integrated web backend | **Yes** — FastAPI + PyTorch in one process | Awkward — need ML service boundary | When your API serves model inference, avoiding a cross-process boundary simplifies architecture. |
| CRUD web API | Solid (FastAPI/Django) | Equally solid (.NET) | Coin-flip. C# wins on type safety and performance; Python wins on iteration speed and ML integration. |
| CPU-bound parallelism | **No** — GIL forces multiprocessing (process overhead) | **Yes** — true OS threads, no GIL | C# `Task`/`Parallel` is simpler and more efficient for CPU-bound parallel work. Python `multiprocessing` works but has serialization overhead. |
| I/O-bound concurrency | Yes — `asyncio` is first-class | Yes — `async`/`await` is first-class | Both are excellent. GIL is released during I/O, so Python threading also works for I/O-bound. |
| Large team codebase (long-lived) | Caution — dynamic typing at scale requires mypy/pyright discipline | **Yes** — static typing catches errors at compile time | Python with type hints + strict mypy is manageable but requires team discipline. C# is more forgiving of large teams. |
| DevOps / infrastructure scripts | **Yes** — Ansible, Fabric, cloud SDKs all Python-first | Possible but rare | AWS/GCP/Azure SDKs are Python-first. The ecosystem gravity is Python for ops automation. |
| CLI tools / utilities | Yes (argparse, click, typer) | Yes (.NET) | Python wins on distribution simplicity (`pipx install`); C# wins if already a .NET shop. |

**The short version**: Python owns data science/ML with no competition. It's a strong default for scripting, automation, and rapid-iteration backends. Reach for C# when you need static type guarantees at scale, CPU-bound performance, or are already in a .NET shop.

---

## Decision Cheat Sheet

### Sequence type: `list` vs `tuple` vs generator expression

| Type | Use when | Key property |
|------|----------|-------------|
| `list` | You need to mutate, append, or reorder | Mutable, O(1) append, O(n) insert |
| `tuple` | Fixed structure — record, return value, dict key | Immutable, hashable (if elements are), slightly faster |
| Generator `(x for x in ...)` | Sequence is large or infinite; you only iterate once | Lazy — values computed on demand, O(1) memory |
| `range` | Integer sequences | Lazy, O(1) memory, supports `len()` and indexing |

### Mapping type: `dict` vs `defaultdict` vs `Counter` vs `dataclass`

| Type | Use when |
|------|----------|
| `dict` | General key-value store; keys are known or arbitrary |
| `collections.defaultdict(list)` | Building a dict of lists/sets without `setdefault` noise |
| `collections.Counter` | Frequency counting; supports `.most_common()`, arithmetic |
| `dataclass` | Typed record with named fields; want `__repr__`, `__eq__` for free |
| `NamedTuple` | Immutable typed record; want tuple unpacking + named access |

### Concurrency model: `asyncio` vs `threading` vs `multiprocessing`

| Model | Use when | C# analogy |
|-------|----------|------------|
| `asyncio` (single-threaded event loop) | I/O-bound; many concurrent connections; you control all the code | `async`/`await` with `Task` — same mental model |
| `threading` | I/O-bound; need to integrate blocking libraries (GIL released on I/O) | `Thread` / `ThreadPool` |
| `multiprocessing` | CPU-bound; need true parallelism; accept serialization overhead | `Parallel.For` / `Task.Run` on separate cores |
| `concurrent.futures.ProcessPoolExecutor` | CPU-bound with a cleaner API than raw `multiprocessing` | `Task.Run` with a pool |

**GIL rule of thumb**: If work is CPU-bound and Python code (not C extension), `threading` gives you concurrency (context switching) but not parallelism. Use `multiprocessing`.

### Attribute access: `@property` vs plain attribute vs `__slots__`

| Approach | Use when |
|----------|----------|
| Plain attribute `self.x = v` | Simple data storage; no validation needed |
| `@property` | Computed value, validation on set, lazy initialization, backward-compatible API change |
| `__slots__ = ['x', 'y']` | High-volume objects (millions of instances); want to ban arbitrary attribute addition; memory optimization |

### String formatting: f-string vs `.format()` vs `%`

| Style | Use when |
|-------|----------|
| `f"Hello {name}"` | Default — modern Python 3.6+, readable, fast |
| `"{name}".format(name=n)` | Template strings stored as variables; Python 2 compat |
| `"Hello %s" % name` | Legacy — reading old code only; do not write new |
| `string.Template` | User-supplied templates (safer — no arbitrary expressions) |

### Type checking: `mypy` vs `pyright`

| Tool | Use when |
|------|----------|
| `pyright` (Pylance) | VS Code / integrated in editors; faster, stricter by default; Microsoft-backed |
| `mypy` | CI pipelines; longest track record; more ecosystem plugins |
| Both | Large codebases — run `pyright` in editor + `mypy` in CI |

### Dependency management: `pip` vs `uv` vs `poetry`

| Tool | Use when |
|------|----------|
| `pip` + `venv` | Simplest; works everywhere; no extras |
| `uv` | New projects — Rust-based, 10-100x faster than pip, supports lockfiles |
| `poetry` | Projects requiring publishing to PyPI; integrated build + publish workflow |
