# Language: Haskell

> Pure functional programming — lazy evaluation, Hindley-Milner type inference, typeclasses, and monads. The language where type theory from MIT TCS is the everyday idiom.

---

## Type System Snapshot

| Axis | Haskell |
|------|---------|
| Binding | Early (static) + typeclass dictionary dispatch |
| Typing | Static |
| Strength | Strong — no implicit coercions whatsoever |
| Type system | Nominal; typeclasses for ad-hoc polymorphism |
| Type inference | **Full Hindley-Milner** — annotate only for clarity |
| Memory model | GC (GHC generational) |

---

## Theory Connections (MIT TCS Context)

```
THEORY                         HASKELL
───────────────────────────────────────────────────────────────
Simply-Typed Lambda Calculus → Core language structure
System F                      → forall a. a -> a (rank-1 polymorphism, more with RankNTypes)
Hindley-Milner inference      → let x = ... (no annotation needed)
Curry-Howard correspondence   → types as propositions, programs as proofs
                                  a -> b ≅ A ⊃ B
                                  (a, b) ≅ A ∧ B
                                  Either a b ≅ A ∨ B
Monads (from category theory) → IO, Maybe, State, Either, Reader, Writer
Comonads                      → Store, Env (less common)
Kind theory                   → * (type), * -> * (type constructor), * -> * -> *
Denotational semantics        → ⊥ (bottom) = non-termination; laziness = lifted domain
```

---

## Syntax Reference Card

### Variables & Bindings
```haskell
-- Top-level binding (no mutation — it's a mathematical definition)
x = 5
name = "Alice"
pi = 3.14159

-- Type annotation (optional but idiomatic for top-level)
x :: Int
x = 5

-- Local binding
result = let y = 5
             z = y * 2
         in y + z

-- where clause (same semantics, different layout)
result = y + z
  where
    y = 5
    z = y * 2

-- No variables (in the mutation sense) — all bindings are immutable
-- In IO monad: IORef for mutable cells, STRef for local mutation

-- Numeric types
Int         -- fixed-precision (machine word size)
Integer     -- arbitrary precision (no overflow)
Float       -- 32-bit IEEE
Double      -- 64-bit IEEE
Rational    -- exact fractions (1/3 is exact!)
Natural     -- non-negative integer
```

### Equality & Comparison
```haskell
-- Eq typeclass — (==) :: Eq a => a -> a -> Bool
1 == 1          -- True
"hello" == "hello"  -- True
[1,2,3] == [1,2,3]  -- True
(1,2) == (1,2)  -- True

-- /= is not-equal (NOT != like C-family!)
1 /= 2          -- True

-- Ord typeclass — compare, (<), (>), (<=), (>=)
compare 1 2     -- LT  (returns Ordering: LT | EQ | GT)
1 < 2           -- True
max 3 5         -- 5
min 3 5         -- 3

-- No reference equality concept (pure — no mutable identity)
-- Everything is compared by value (structural)

-- Deriving instances
data Point = Point { x :: Int, y :: Int }
  deriving (Show, Eq, Ord)    -- compiler generates instances
```

### Logical Operators
```haskell
&&      -- AND (short-circuit)
||      -- OR  (short-circuit)
not     -- NOT (function, not symbol)

-- Bitwise (Data.Bits)
import Data.Bits
x .&. y     -- AND
x .|. y     -- OR
xor x y     -- XOR
complement x -- NOT
shiftL x n  -- left shift
shiftR x n  -- right shift
```

### Collections
```haskell
-- List — LINKED list (not array!)
xs = [1, 2, 3, 4, 5]   -- :: [Int]
xs = [1..5]             -- [1,2,3,4,5]
xs = [1,3..9]           -- [1,3,5,7,9]  (arithmetic sequence)
xs = [1..]              -- INFINITE list (lazy evaluation!)

-- List operations
head [1,2,3]    -- 1
tail [1,2,3]    -- [2,3]
[0] ++ [1,2,3]  -- [0,1,2,3]  (concatenation — O(n))
0 : [1,2,3]     -- [0,1,2,3]  (cons — O(1))
xs !! 2         -- 3           (index — O(n))
length xs       -- 5
reverse xs      -- [5,4,3,2,1]
take 3 xs       -- [1,2,3]
drop 3 xs       -- [4,5]
zip [1,2,3] ["a","b","c"]  -- [(1,"a"),(2,"b"),(3,"c")]
map (*2) xs     -- [2,4,6,8,10]
filter even xs  -- [2,4]
foldr (+) 0 xs  -- 15 (right fold)
foldl' (+) 0 xs -- 15 (strict left fold — use for sums)

-- List comprehensions
[x^2 | x <- [1..10], odd x]   -- [1,9,25,49,81]
[(x,y) | x <- [1..3], y <- [1..3], x /= y]

-- Tuple (fixed size, fixed types)
t = (1, "hello", True)  -- :: (Int, String, Bool)
fst (1, "a")    -- 1
snd (1, "a")    -- "a"
let (a, b, c) = t in a  -- destructuring

-- Data.Map (ordered, immutable)
import qualified Data.Map.Strict as Map
m = Map.fromList [("a",1), ("b",2)]
Map.lookup "a" m    -- Just 1
Map.insert "c" 3 m  -- new map (original unchanged)
Map.toList m        -- [("a",1),("b",2)]

-- Data.Set (ordered, immutable)
import qualified Data.Set as Set
s = Set.fromList [3,1,4,1,5,9]  -- {1,3,4,5,9}
```

### Control Flow
```haskell
-- If (expression, else required, both branches same type)
if x > 0 then "positive" else "non-positive"

-- Guards (alternative to if for function clauses)
classify x
  | x < 0    = "negative"
  | x == 0   = "zero"
  | x < 10   = "small"
  | otherwise = "large"

-- Case (pattern matching)
case xs of
  []     -> "empty"
  [x]    -> "singleton: " ++ show x
  (x:xs) -> "head: " ++ show x

-- Pattern matching on function definition
fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

-- Algebraic data types + pattern matching
data Shape = Circle Double | Rectangle Double Double

area :: Shape -> Double
area (Circle r) = pi * r * r
area (Rectangle w h) = w * h
```

### Strings & Characters
```haskell
-- String = [Char] — a linked list of characters
-- This is historically true and a performance footgun
-- Use Data.Text for real string work

s = "hello"             -- :: String = :: [Char]
s = "hello" ++ " world" -- concatenation (O(n))
length "hello"          -- 5 (chars)
words "hello world"     -- ["hello","world"]
unwords ["hello","world"]  -- "hello world"
lines "a\nb\nc"         -- ["a","b","c"]
unlines ["a","b"]       -- "a\nb\n"

-- Char
c = 'A'                 -- :: Char
ord 'A'                 -- 65  (from Data.Char)
chr 65                  -- 'A'
isAlpha c  isDigit c  isUpper c  isLower c

-- Data.Text (use this for real text)
import qualified Data.Text as T
t = T.pack "hello"      -- :: Text
T.unpack t              -- :: String
T.length t              -- O(n) but at least packed

-- Show and Read (type class based serialization)
show 42         -- "42"
show True       -- "True"
show [1,2,3]    -- "[1,2,3]"
read "42" :: Int   -- 42 (needs type annotation)
```

### Null / Maybe
```haskell
-- No null. Use Maybe.
data Maybe a = Just a | Nothing

-- Creating
x = Just 42     -- :: Maybe Int
y = Nothing     -- :: Maybe a

-- Pattern matching
case mx of
  Just v  -> use v
  Nothing -> defaultValue

-- Functor fmap (map over Maybe)
fmap (+1) (Just 5)  -- Just 6
fmap (+1) Nothing   -- Nothing

-- Maybe is a Functor, Applicative, Monad
-- Monad instance enables chaining (>>=)
do result <- lookupUser id        -- Maybe User
   name <- Just (userName result)  -- Maybe String
   return name
-- If any step returns Nothing, the whole do-block returns Nothing

-- fromMaybe
import Data.Maybe
fromMaybe 0 (Just 5)   -- 5
fromMaybe 0 Nothing    -- 0
catMaybes [Just 1, Nothing, Just 3]  -- [1,3]
mapMaybe f xs   -- apply f, keep Just results
```

### Functions
```haskell
-- All functions are curried (single argument, return function for rest)
add :: Int -> Int -> Int    -- really: Int -> (Int -> Int)
add x y = x + y

add 1       -- partially applied: Int -> Int (a function that adds 1)
add 1 2     -- 3

-- Lambda
\x -> x * 2
\x y -> x + y   -- multi-arg (sugar for \x -> \y -> x + y)

-- Function composition
-- (.) :: (b -> c) -> (a -> b) -> (a -> c)
(f . g) x = f (g x)    -- right-to-left
doublePos = filter (>0) . map (*2)

-- Application operator (avoids parentheses)
-- ($) :: (a -> b) -> a -> b
f $ x = f x    -- right-associative
print $ map (*2) [1..5]   -- instead of: print (map (*2) [1..5])

-- Sections (partial application of operators)
(+1)    -- add 1 (left section)
(2^)    -- 2 to the power of (left section)
(^2)    -- square (right section)
map (+1) [1,2,3]    -- [2,3,4]

-- Typeclasses (the ad-hoc polymorphism mechanism)
class Describable a where
    describe :: a -> String

instance Describable Int where
    describe n = "the number " ++ show n

instance Describable Bool where
    describe True = "yes"
    describe False = "no"

-- Functor, Applicative, Monad
fmap :: Functor f => (a -> b) -> f a -> f b
(<*>) :: Applicative f => f (a -> b) -> f a -> f b
(>>=) :: Monad m => m a -> (a -> m b) -> m b
```

### IO and Effects
```haskell
-- IO is the only way to interact with the outside world
-- IO a is a description of an action that produces a value of type a

main :: IO ()
main = do
    putStrLn "What's your name?"
    name <- getLine           -- name :: String
    putStrLn ("Hello, " ++ name)

-- do notation is syntactic sugar for (>>=)
main = putStrLn "What's your name?" >>
       getLine >>= \name ->
       putStrLn ("Hello, " ++ name)
```

### Error Handling
```haskell
-- Pure code
-- Either e a — Right is success, Left is error
data Either e a = Left e | Right a

safeDiv :: Int -> Int -> Either String Int
safeDiv _ 0 = Left "division by zero"
safeDiv a b = Right (a `div` b)

case safeDiv 10 2 of
    Right v -> print v
    Left e  -> putStrLn e

-- do notation for Either (short-circuits on Left)
result = do
    x <- safeDiv 10 2
    y <- safeDiv x  0     -- Left "division by zero" — rest skipped
    return (x + y)

-- IO exceptions (for runtime failures)
import Control.Exception
result <- try (readFile "file.txt") :: IO (Either IOException String)
case result of
    Left e  -> print e
    Right s -> putStr s

throwIO (SomeException (ErrorCall "msg"))
```

---

## What Makes It Distinct

1. **Purity** — functions have no side effects (except in IO monad). Given the same input, always the same output. This enables equational reasoning, easy testing, and fearless refactoring.
2. **Laziness** — expressions evaluated only when needed. Enables infinite data structures (`[1..]`), efficient composition (no intermediate lists), and improved modularity.
3. **Typeclasses = Rust traits + more** — Haskell's typeclass system is the theoretical foundation for Rust traits, Scala implicit/given, and Swift protocols. Functor/Applicative/Monad express patterns that appear everywhere.
4. **Monads = programmable semicolons** — `IO`, `Maybe`, `Either`, `State`, `Reader` are all the same mechanism. `do` notation unifies effectful computation with pure code. You compose effects the same way you compose functions.
5. **Laziness is both a feature and a footgun** — can cause space leaks. Need `seq`, `$!`, `BangPatterns`, and strict variants (`foldl'`) in performance-critical code.

---

## Ecosystem

| Tool | Purpose |
|------|---------|
| GHC | Compiler (Haskell = GHC in practice) |
| Cabal / Stack | Build + package management |
| Hackage / Stackage | Package repositories |
| HLS | Haskell Language Server |
| QuickCheck | Property-based testing (the original) |
| Aeson | JSON serialization |
| Servant | Type-safe HTTP APIs |
| Conduit / Pipes | Streaming |
| STM | Software Transactional Memory (concurrency) |

---

## Gotchas from C#

| C# behavior | Haskell behavior | Consequence |
|-------------|-----------------|-------------|
| `string` is efficient | `String = [Char]` is a linked list | Use `Data.Text` for text |
| `for` loops | Recursion + list operations | Different mental model |
| Mutation is default | Mutation requires IORef/STRef/MVar | Pure first, effect explicitly |
| `null` exists | No null — use `Maybe` | Forces explicit handling everywhere |
| `async Task<T>` | `IO a` (synchronous) or `async` libraries | Different concurrency model |
| Integer overflow | Integer is arbitrary precision (Int can overflow) | Use Integer for big numbers |
| `++` increments | `++` is list concatenation! | Different operator |
