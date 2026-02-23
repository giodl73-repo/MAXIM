# Language: Ruby

> Everything is an object, everything is open — dynamic, expressive, optimized for developer happiness. Rails made it famous; its metaprogramming makes it powerful and dangerous.

---

## Type System Snapshot

| Axis | Ruby |
|------|------|
| Binding | Late — method lookup via ancestor chain at runtime |
| Typing | Dynamic |
| Strength | Strong — no implicit coercions (`"1" + 1` raises TypeError) |
| Type system | Duck typing |
| Type inference | None (Sorbet / RBS for static analysis) |
| Memory model | GC (incremental mark-sweep + compaction, MRI) |

---

## Syntax Reference Card

### Variables & Assignment
```ruby
# Local variables — lowercase or underscore
x = 5
name = "Alice"
my_value = true

# Multiple assignment
a, b = 1, 2
a, b = b, a             # swap (idiomatic!)
first, *rest = [1, 2, 3, 4]   # splat — first=1, rest=[2,3,4]
*init, last = [1, 2, 3, 4]    # init=[1,2,3], last=4
a, _, c = [1, 2, 3]          # _ discards middle

# Variable scope sigils
x = 5           # local (lowercase)
$x = 5          # global
@x = 5          # instance variable (in class)
@@x = 5         # class variable
X = 5           # constant (UPPER — reassignment gives warning)

# Ruby has no const keyword — convention only
MAX_SIZE = 100

# Parallel assignment
x, y, z = 1, 2, 3
```

### Equality & Comparison
```ruby
# == value equality (calls == method — overridable)
1 == 1          # true
"hello" == "hello"  # true
[1,2,3] == [1,2,3]  # true

# equal? — object identity (same as Object.ReferenceEquals)
a = "hello"
b = "hello"
a.equal?(b)     # false (different objects)
a.equal?(a)     # true

# eql? — type + value equality (used by Hash for keys)
1.eql?(1)       # true
1.eql?(1.0)     # false (different types! 1 is Integer, 1.0 is Float)
1 == 1.0        # true (different behavior from eql?)

# === case equality (used in case/when, often overridden)
(1..10) === 5   # true (Range#=== checks membership)
String === "hi" # true (Module#=== checks is-a relationship)
/hello/ === "hello world"  # true (Regexp#=== checks match)
:foo === :foo   # true

# Comparison
1 <=> 2         # -1 (spaceship — -1/0/1)
"a" <=> "b"     # -1
1 <=> 1         # 0
1.between?(0, 10)  # true
```

### Logical Operators
```ruby
&&    # short-circuit AND (returns operand)
||    # short-circuit OR  (returns operand)
!     # NOT

and   # lower precedence AND (use for control flow, not assignment)
or    # lower precedence OR
not   # lower precedence NOT

# WARNING: && and and have DIFFERENT precedences
x = true && false   # x = false (&&  binds tighter)
x = true and false  # x = true  (and has lower precedence — x gets true first!)

&     |     ^     ~     <<     >>   # bitwise

# Truthy/Falsy in Ruby
# ONLY false and nil are falsy
# 0 is TRUTHY (unlike many languages!)
# "" is TRUTHY
# [] is TRUTHY
```

### Collections
```ruby
# Array — mutable, ordered, heterogeneous
arr = [1, 2, 3]
arr = Array.new(5) { |i| i * 2 }   # [0,2,4,6,8]
arr = %w[foo bar baz]               # ["foo","bar","baz"] (word array)
arr = %i[foo bar baz]               # [:foo,:bar,:baz] (symbol array)

arr.push(4)  arr << 4               # append (both equivalent)
arr.pop                             # remove last (returns it)
arr.unshift(0)                      # prepend
arr.shift                           # remove first
arr[0]  arr[-1]  arr[1..3]         # access, negative from end, range
arr.first  arr.last
arr.first(3)  arr.last(3)
arr.length  arr.size  arr.count
arr.empty?
arr.include?(2)
arr.flatten                         # flatten nested arrays
arr.compact                         # remove nil elements
arr.uniq                            # unique elements
arr.sort  arr.sort_by { |x| x.to_s }
arr.reverse
arr.map { |x| x * 2 }
arr.select { |x| x > 1 }           # filter
arr.reject { |x| x > 1 }           # inverse filter
arr.reduce(0) { |sum, x| sum + x }
arr.each_with_index { |x, i| }
arr.each_with_object([]) { |x, acc| acc << x * 2 }
arr.zip(other)                      # [[1,'a'],[2,'b'],...]
arr.flatten.map(&:to_s)             # & converts symbol to proc

# Hash — mutable, ordered (Ruby 1.9+)
h = { "key" => value }             # hash rocket syntax
h = { key: value }                 # symbol key syntax (preferred)
h[:key]                            # access (symbol key)
h["key"]                           # access (string key)
h[:missing]                        # nil (no exception)
h.fetch(:key)                      # raises KeyError if missing
h.fetch(:key, "default")           # with default
h[:new] = "val"                    # set
h.delete(:key)                     # delete (returns value)
h.key?(:key)  h.has_key?(:key)     # membership
h.keys  h.values  h.each_pair { |k,v| }
h.merge(other_hash)                # new hash
h.transform_values { |v| v * 2 }
h.select { |k,v| v > 1 }
h.any? { |k,v| v > 5 }

# Range
(1..10)                 # inclusive
(1...10)                # exclusive (three dots)
("a".."z")              # character range
(1..10).to_a            # [1,2,...,10]
(1..10).include?(5)     # true
(1..10).each { |i| }
```

### Control Flow
```ruby
# If
if cond
  ...
elsif cond2
  ...
else
  ...
end

# One-line (postfix if — very idiomatic)
return if cond
puts "hello" if name
do_thing unless flag     # unless = if not

# Ternary
result = cond ? t : f

# Case/when (=== under the hood)
case x
when 0
  "zero"
when 1, 2
  "one or two"
when 3..10
  "small"
when String
  "it's a string"
when /pattern/
  "matches regex"
else
  "other"
end

# Case without argument
case
when x < 0 then "negative"
when x == 0 then "zero"
else "positive"
end

# Loops
# for..in (uncommon — each is preferred)
for i in 1..5
  puts i
end

# Each (idiomatic)
[1,2,3].each { |x| puts x }
5.times { |i| puts i }
(1..10).each { |i| }
1.upto(10) { |i| }
10.downto(1) { |i| }

# while / until
while cond
  ...
end
do_something until done_condition

# loop (infinite)
loop do
  break if should_stop
end
```

### Strings & Characters
```ruby
# String — MUTABLE by default (unlike most languages!)
s = "hello"
s << " world"           # mutates s in place!
s.concat(" world")      # also mutates

# Interpolation — only in double-quoted strings
name = "Alice"
"Hello, #{name}!"           # interpolation
'Hello, #{name}!'           # NO interpolation (literal #)
"#{2 + 2}"                  # any expression

# Escape sequences — only in double-quoted
"\n \t \\ \""

# Heredoc
s = <<~HEREDOC
  line one
  line two
HEREDOC                     # strips leading whitespace to content

# String operations
s.length  s.size
s.upcase  s.downcase
s.strip  s.lstrip  s.rstrip
s.chomp                     # remove trailing \n
s.chop                      # remove last character
s.split(",")                # array
s.split                     # split on whitespace
s.include?("sub")
s.start_with?("prefix")
s.end_with?("suffix")
s[0]  s[-1]  s[1..3]  s[1,3]  # access (returns String, not char)
s.replace("new")            # mutates in place
s.gsub("old", "new")        # global substitution (returns new string)
s.gsub!("old", "new")       # mutates in place (! = danger)
s.tr("aeiou", "*")          # translate chars
"42".to_i  "3.14".to_f
42.to_s  nil.to_s           # to_s always defined

# No char type — s[0] returns a String of length 1
# ord/chr:
"A".ord   # 65
65.chr    # "A"

# Frozen strings (immutable)
s = "hello".freeze
s << "!"    # FrozenError!

# Symbols — immutable, interned strings (good for hash keys)
:name  :id  :user_id
:name.to_s  # "name"
"name".to_sym  # :name
```

### Nil
```ruby
nil             # the null object (only instance of NilClass)
nil.nil?        # true
nil.to_a        # [] — nil converts to empty array (convenient!)
nil.to_s        # "" — nil converts to empty string
nil.to_i        # 0

# Nil checks
x.nil?
x == nil
x.is_a?(NilClass)

# Safe navigation (Ruby 2.3+)
user&.name      # nil if user is nil
user&.address&.city

# Common patterns
name = user&.name || "Anonymous"
name = user&.name.presence || "Anonymous"  # .presence returns nil for blank
```

### Functions / Methods
```ruby
# Methods (all methods return value of last expression)
def add(a, b)
  a + b             # implicit return
end

def add(a, b) = a + b   # one-liner (Ruby 3.0+)

# Default arguments
def greet(name, greeting = "Hello")
  "#{greeting}, #{name}!"
end

# Keyword arguments
def connect(host:, port: 8080)  # host: required, port: has default
end
connect(host: "localhost")
connect(host: "localhost", port: 3000)

# Splat arguments
def sum(*nums)
  nums.sum
end
sum(1, 2, 3, 4)

# Double splat (keyword args)
def f(**opts)
  opts[:verbose]
end

# Blocks — the Ruby closure mechanism
def call_twice
  yield if block_given?
  yield if block_given?
end
call_twice { puts "hello" }   # prints twice

# Explicit block parameter
def transform(arr, &block)
  arr.map(&block)
end
transform([1,2,3]) { |x| x * 2 }

# Proc and Lambda
add = Proc.new { |x, y| x + y }
add = proc { |x, y| x + y }
add = lambda { |x, y| x + y }
add = ->(x, y) { x + y }   # stabby lambda

# Symbol to proc
[1,2,3].map(&:to_s)         # ["1","2","3"]
# equivalent to: [1,2,3].map { |x| x.to_s }
```

### Classes & Open Classes
```ruby
class Animal
  attr_accessor :name, :age   # generates getter + setter
  attr_reader :id             # getter only

  def initialize(name, age)
    @name = name
    @age = age
  end

  def speak
    "..."
  end

  def self.create(name)       # class method
    new(name, 0)
  end

  protected

  def secret
    "..."
  end

  private

  def internal
    "..."
  end
end

class Dog < Animal            # inheritance
  def speak
    "Woof!"
  end

  def super_speak
    super + " WOOF!"          # call parent
  end
end

# Open classes — reopen ANY class (even built-in!)
class String
  def shout
    upcase + "!"
  end
end
"hello".shout   # "HELLO!"   (monkey-patching)

# Modules (mixins — multiple inheritance mechanism)
module Greetable
  def greet
    "Hello, I'm #{name}"
  end
end

class Person
  include Greetable
  attr_reader :name
  def initialize(name) = @name = name
end
```

### Error Handling
```ruby
begin
  risky_operation
rescue ArgumentError => e
  puts e.message
rescue TypeError, RuntimeError => e
  puts "type or runtime error: #{e}"
rescue => e             # catch StandardError and subclasses
  raise e               # re-raise
ensure
  cleanup               # always runs
end

# Postfix rescue (single line)
value = risky_call rescue "default"

# Custom exception
class AppError < StandardError
  def initialize(msg = "app error")
    super
  end
end

raise AppError.new("something failed")
raise AppError, "something failed"   # equivalent
```

---

## What Makes It Distinct

1. **Everything is an object** — `1.class` = `Integer`. `nil.class` = `NilClass`. `true.class` = `TrueClass`. Even classes are objects (instances of `Class`). Method calls on everything.
2. **Open classes** — you can reopen ANY class, including built-ins. `class Integer; def double; self * 2; end; end` adds `double` to all integers. Powerful for DSLs; dangerous in production.
3. **Blocks** — first-class closures via `{}` or `do..end`. Iterators (`each`, `map`, `select`) take blocks. The `yield` mechanism. `Proc` vs `Lambda` distinction (return behavior differs).
4. **Convention over configuration (Rails)** — The Ruby on Rails design principle: if you follow naming conventions, the framework does the wiring. Built the modern web framework template.
5. **Mutable strings by default** — `s << " world"` mutates `s`. Use `.freeze` or `# frozen_string_literal: true` pragma. Different from every other modern language.

---

## Ecosystem

| Tool | Purpose |
|------|---------|
| Bundler / Gemfile | Dependency management |
| RubyGems | Package repository |
| Rails | Web framework (dominant) |
| Sinatra / Hanami | Lightweight web |
| RSpec / Minitest | Testing |
| RuboCop | Linter + formatter |
| Sorbet / Steep | Optional static typing |
| Sidekiq | Background jobs |

---

## Gotchas from C#

| C# behavior | Ruby behavior | Consequence |
|-------------|--------------|-------------|
| `string` is immutable | `String` is **mutable** | `.dup` to copy before mutating |
| `0`, `""` are truthy in C# | `0` and `""` are **truthy** in Ruby! | Only `false` and `nil` are falsy |
| `==` for value equality | `==` for value, `eql?` for strict, `equal?` for reference | Three levels of equality |
| `array[0]` index | `array[0]` — same, but also `array.first` | Ruby is consistent here |
| Integer overflow throws in checked | Ruby integers are arbitrary precision | No overflow, but boxing overhead |
| Methods are not open by default | ALL classes are open — even String, Integer | Powerful but fragile |
