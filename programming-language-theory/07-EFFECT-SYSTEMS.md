# Effect Systems: Monads, Algebraic Effects, Capability Effects

## The Big Picture

Effect systems track what "side effects" a computation can perform — IO, state mutation, exceptions, nondeterminism — in the type system. The goal: functions that look pure but aren't are rejected; effects compose correctly; effect polymorphism enables reuse.

```
+--------------------------------------------------------------------------+
|                    EFFECT SYSTEMS LANDSCAPE                              |
+--------------------------------------------------------------------------+
|                                                                          |
|  THE PROBLEM:                                                            |
|  Pure functions: f : A → B (no hidden effects)                          |
|  Impure functions: same type but read global state, throw exceptions...  |
|  Without effect tracking: can't tell them apart                         |
|                                                                          |
|  APPROACHES:                                                             |
|  ┌──────────────────┬──────────────────────┬────────────────────────┐  |
|  │ MONADS           │ ALGEBRAIC EFFECTS    │ CAPABILITY TYPES       │  |
|  │ Moggi 1991       │ Plotkin/Power 2003   │ Capabilities-as-tokens │  |
|  │                  │                      │                        │  |
|  │ Haskell IO, State│ Eff language, Koka   │ Scala CC, OCaml 5      │  |
|  │ compose via >>=  │ compose via handlers │ capabilities restrict  │  |
|  │ (bind)           │ algebraic operations │ effect use             │  |
|  │                  │                      │                        │  |
|  │ n effects =       │ n effects compose    │ n effects: capability   │|
|  │ 2ⁿ transformer   │ naturally              │ tokens in environment   │  |
|  │ stack options    │ handlers are first-  │                        │  |
|  │                  │ class                  │                        │|
|  └──────────────────┴──────────────────────┴────────────────────────┘  |
|                                                                          |
|  LINEAR TYPES AND EFFECTS:                                              |
|  Rust: ownership tracks the "memory effect"                             |
|  Affine resource = can't alias; mutation safe                           |
|  Borrow = temporary effect-limited access                               |
+--------------------------------------------------------------------------+
```

---

## 1. Moggi's Computational Lambda Calculus

Eugenio Moggi (1991) — the theoretical foundation for monads as effects:

**The problem**: A function `A → B` says nothing about what it might do besides produce a B from an A. Side-effecting computations need a richer type.

```
MOGGI'S COMPUTATIONAL LAMBDA CALCULUS:

  For each notion of computation (effect), a monad T:
    T : Type → Type    (a type constructor)

  A computation that MAY USE EFFECT E and returns A:
    has type T_E(A)     (wrapped in the effect monad)

  Values:    A → T A    (return / pure)
  Sequencing: T A → (A → T B) → T B    (bind / >>=)

  MONAD LAWS:
    return a >>= f = f a               (left identity)
    m >>= return = m                   (right identity)
    (m >>= f) >>= g = m >>= λa. f a >>= g   (associativity)

  EXAMPLES OF MONADS:
    IO monad: T A = IO A (computation that can do I/O and returns A)
    State monad: T A = S → (A, S) (computation that reads/writes state)
    Maybe monad: T A = A | None (computation that may fail)
    List monad: T A = [A] (nondeterministic computation: multiple results)
    Reader monad: T A = E → A (computation that reads an environment E)
    Writer monad: T A = (A, W) (computation that emits a log W)
    Except monad: T A = Either E A (computation that may throw E)
```

**Philip Wadler (1992)** — "Comprehending Monads" + "The Essence of Functional Programming": brought monads into practical Haskell programming.

---

## 2. Haskell's Monad Architecture

```
HASKELL MONAD HIERARCHY:

  class Functor f where
    fmap :: (a → b) → f a → f b

  class Functor f => Applicative f where
    pure :: a → f a
    (<*>) :: f (a → b) → f a → f b    -- apply effectful function

  class Applicative m => Monad m where
    return :: a → m a     -- = pure
    (>>=) :: m a → (a → m b) → m b   -- sequence + bind

KEY MONADS IN HASKELL:

  IO a        -- computations with I/O effects
  State s a   -- computations with mutable state s
  Reader e a  -- computations with read-only environment e
  Writer w a  -- computations producing a log w
  Maybe a     -- computations that may fail (Nothing)
  Either e a  -- computations that may throw error e
  STM a       -- software transactional memory
  ST s a      -- local mutable state (can be run pure via runST)

DO NOTATION (syntactic sugar for >>= chains):

  do
    x <- getLine      -- x :: String,  getLine :: IO String
    y <- readFile x   -- y :: String,  readFile :: String → IO String
    return (length y)
  -- desugars to:
  getLine >>= λx → readFile x >>= λy → return (length y)
  -- type: IO Int
```

---

## 3. The Monad Transformer Problem

**The problem with stacking effects**:
```
MONAD TRANSFORMER STACK:

  I want: IO + State + Exceptions + Logging

  Single effect:
    IO a, State s a, Except e a, Writer w a

  Combine with transformers:
    StateT s IO a    = s → IO (a, s)    (State over IO)
    ExceptT e (StateT s IO) a           (Except over State over IO)
    WriterT w (ExceptT e (StateT s IO)) a   (full stack)

  READING THE TYPE:
    A computation in WriterT w (ExceptT e (StateT s IO)) a:
    Takes initial state s
    May throw exception e OR return a value (Either)
    Produces a log w
    Is an IO action

  THE EXPLOSION PROBLEM:
    n effects → multiple possible orderings
    StateT s (ExceptT e IO) a  ≠  ExceptT e (StateT s IO) a
    (different: does rolling back state on exception affect it?)
    2ⁿ possible stacks for n effects
    Each requires: lift functions for each level
    Code becomes: lift (lift (liftIO action))

  PRACTICAL RESULT:
    Heavy monad transformer code becomes unreadable
    Operational meaning (stack order) is obscure
    Changing effect order requires refactoring all code
```

**mtl class approach** (partially mitigates):
```
MTL TYPECLASSES:

  class MonadState s m where
    get :: m s
    put :: s → m ()

  class MonadError e m where
    throwError :: e → m a
    catchError :: m a → (e → m a) → m a

  class MonadIO m where
    liftIO :: IO a → m a

  Any monad stack that has State s in it is an instance of MonadState s
  → Code doesn't need explicit lift
  → BUT: class inference is complex; large instance resolution overhead
  → AND: doesn't solve the n! ordering problem
```

---

## 4. Algebraic Effects

Plotkin and Power (2003), Bauer and Pretnar (Eff language 2012):

**The key insight**: separate the *operations* (what effects exist) from the *handlers* (how they're interpreted). Effects are algebraic operations with equations; handlers are first-class interpretations.

```
ALGEBRAIC EFFECTS: OPERATIONS + HANDLERS

  EFFECT DECLARATION:
    effect State s :
      operation get : Unit → s
      operation put : s → Unit

  USING THE EFFECT:
    fun counter () : Unit =
      let n = get () in
      put (n + 1)
    (* counter has type Unit → Unit with effect State Int *)

  HANDLER:
    handler runState (init : s) :
      return x  ↦  fun s → (x, s)
      get ()    ↦  fun s → resume s s    (* pass s to continuation; s unchanged *)
      put s'    ↦  fun s → resume () s' (* pass () to continuation; new state s' *)

    (* runState runs a computation with initial state, returns (result, finalState) *)

THE RESUME KEYWORD: resumable exceptions

  Operations can RESUME the interrupted computation:
    effect Nondeterminism :
      operation choose : Unit → Bool

    handler allChoices :
      return x   ↦  [x]
      choose ()  ↦  resume true ++ resume false
                   (* try both branches; collect results *)

  THIS IS WHAT MAKES ALGEBRAIC EFFECTS POWERFUL:
    Handlers can resume the computation multiple times (nondeterminism)
    Or not at all (abort/exception)
    Or wrap it (state, logging)
    The effect operation = "call the handler" = "raise a resumable exception"
```

**Advantages over monads**:
```
ALGEBRAIC EFFECTS vs. MONADS:

  COMPOSITIONALITY:
    Two effects E₁ and E₂ can be combined freely:
    f : A → B with effects {E₁, E₂}   (effect polymorphism)
    No transformer stack ordering; effects compose automatically

  HANDLERS ARE FIRST-CLASS:
    Different interpretations of the same effect:
    runState = standard state interpretation
    logging_state = state + log all transitions
    transactional_state = state with rollback capability
    Same code; different handlers

  EFFECT POLYMORPHISM:
    f : {e} A → {e} B  (f preserves effects)
    g : A → {IO, Nondeterminism} B
    No monad constraints in signatures

  CONCRETELY IN LANGUAGES:
    OCaml 5 (2022): built-in algebraic effects + multi-core
    Koka (Leijen): row-based effect polymorphism throughout
    Eff: reference implementation (Bauer-Pretnar)
    Haskell: effectful, polysemy, fused-effects libraries (user-land)
```

---

## 5. OCaml 5 Effects

OCaml 5 landed algebraic effects (2022) as part of the multi-core release:

```
OCAML 5 EFFECT EXAMPLE:

  (* Effect declaration *)
  type _ Effect.t +=
    | Get : int Effect.t
    | Put : int → unit Effect.t

  (* Using effects *)
  let counter () =
    let n = Effect.perform Get in
    Effect.perform (Put (n + 1))

  (* Handler *)
  let run_state init f =
    let state = ref init in
    match f () with
    | result → result
    | effect Get, k → continue k !state
    | effect Put n, k → state := n; continue k ()

  (* continue k v = resume the continuation k with value v *)

PERFORMANCE:
  OCaml 5 effects are designed to be zero-cost when not used
  Effect handler overhead is comparable to exception handler
  Much cheaper than equivalent monad transformer stacks

LIMITATION:
  OCaml 5 effects are "one-shot" by default (continuation used once)
  Multi-shot continuations (nondeterminism) require deep copying
  → Not all algebraic effect patterns are zero-cost
```

---

## 6. Capability-Based Effects

**Scala's Capture Checking** (in development):

```
CAPTURE CHECKING IDEA:

  In Scala (experimental):
    def readLine(): String^{io}     (* io is a capability *)
    def writeFile(path: String, data: String): Unit^{io}

  A function that uses io must declare it:
    def processLine^{io}() =
      val line = readLine()      (* requires io capability *)
      writeFile("log.txt", line) (* requires io capability *)

  A pure function cannot call io-capable functions:
    def pure() : String = readLine()  (* ERROR: accessing io without capability *)

  CAPABILITY POLYMORPHISM:
    def map^{c}[A, B](f: A → B^{c}, xs: List[A]): List[B]^{c}
    The effect c is passed as a capability variable
    → Effect-polymorphic map

ADVANTAGE OVER MONADS:
  No wrapping/unwrapping of effect types
  Existing pure code works without changes
  Effects are tracked without changing function signatures (ideally)

SCALA CAPTURE CHECKING STATUS:
  Experimental in Scala 3.3+; opt-in
  Full formalization still in progress
```

---

## 7. Linear Types and the Memory Effect

Rust's ownership system as an effect system — tracking the "mutation" and "aliasing" effects:

```
RUST'S EFFECT ENCODING VIA LINEAR TYPES:

  T         (owned value — linear resource)
  &T        (shared reference — can copy; no mutation)
  &mut T    (exclusive reference — can mutate; no copying)

  EFFECT BEING TRACKED:
    Mutation: only via &mut T (exclusive access)
    Sharing: &T can be freely copied, but no mutation allowed
    Drop: owned T will be dropped when it goes out of scope (resource use)

  BORROW RULES = LINEAR TYPE SYSTEM RULES:
    You can have: ONE &mut T  OR  MULTIPLE &T  (but not both simultaneously)
    This IS the rule of linear logic: A ⊗ B means you have both A and B,
    each used once. The "sharing" (&T) is the !A (of course) of linear logic.

  FORMALIZATION:
    RustBelt (Jung, Jourdan, Krebbers, Dreyer — POPL 2018):
    Formal semantics for the Rust type system using Iris separation logic
    Iris is a concurrent separation logic — the formal tool for aliasing + effects
    RustBelt proves: safe Rust programs cannot exhibit undefined behavior
```

---

## Decision Cheat Sheet

| Need | Approach | Language |
|------|----------|----------|
| Effect tracking via types | IO/State monads | Haskell |
| Multiple effects with less boilerplate | mtl typeclasses | Haskell |
| Maximum compositionality for effects | Algebraic effects + handlers | Koka, OCaml 5, Eff |
| Zero-cost effects in production | OCaml 5 effects | OCaml |
| Memory safety as effect | Ownership / affine types | Rust |
| Protocol state machines | Linear types / session types | Idris 2 |
| Capture effects in OO language | Capture checking (experimental) | Scala 3 |

---

## Common Confusion Points

**Monads are not just for IO**: The IO monad in Haskell happens to be the visible effect-tracking monad, but monads model state, failure, nondeterminism, parsers, continuations — any computation pattern with sequential structure and the monad laws.

**Monad transformers compose effects but in a specific order**: StateT s (ExceptT e IO) differs from ExceptT e (StateT s IO) — in the first, throwing an exception does NOT roll back state changes; in the second, it does. Algebraic effects handlers compose without committing to order (you can write either semantics as a handler).

**OCaml 5 effects are not the same as exceptions**: Exceptions abort and unwind the stack (non-resumable). OCaml 5 effects capture the continuation — you can resume the computation after handling. This is what enables effects like state (which needs to resume), nondeterminism (which needs to resume multiple times), and coroutines.

**Rust's borrow checker is not a complete linear type system**: Rust uses affine types (use at most once) not linear types (use exactly once). Additionally, the borrow system is more expressive than simple affine typing — it allows temporary shared borrows (&T, which act as unrestricted during the borrow's lifetime) within a linear discipline. This makes Rust more flexible but harder to formalize completely.
