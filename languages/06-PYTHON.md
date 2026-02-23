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
