# Scripting: Perl

```
SCRIPTING LANGUAGE LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  Unix text tools          Perl                   Modern successors
  ─────────────────        ──────────────────────  ─────────────────────────────
  sed  awk  sh             "Swiss Army chainsaw"   Python    Ruby    Node.js
  ─────────────────        ──────────────────────  ─────────────────────────────
  single-purpose tools     ate the entire left     data science, web, async
  line-at-a-time           column in one language  explicit OOP, readable
  no data structures       regex-native grammar    large ecosystems
  no CPAN                  BioPerl, DBI, Moose     pip/npm vs CPAN
  1970s–1980s              1987–present            1991–present

  Perl's three modes — spatially:
  ┌───────────────────────────────────────────────────────────────────────────┐
  │                                                                           │
  │  ONE-LINER             SCRIPT FILE             MODULE / OOP               │
  │  ─────────────────     ──────────────────────  ───────────────────────    │
  │  perl -e 'code'        #!/usr/bin/perl          package My::Module;        │
  │  perl -n -e '...'      use strict;              use Moose;                 │
  │  perl -p -e '...'      use warnings;            has 'attr' => (...);       │
  │  perl -i -e '...' f    # full program           method dispatch, roles     │
  │                        # file I/O, CPAN         CPAN-deployable            │
  │  ← replaces sed/awk →  ← replaces shell  →     ← replaces Java beans →    │
  │                                                                           │
  │  Language surface:                                                        │
  │    $scalar  @array  %hash                 ← data                         │
  │    =~  s///  tr///  qr//                  ← regex (grammar, not library) │
  │    map grep sort reverse                  ← functional list ops           │
  │    open / close / <$fh> / print           ← I/O                          │
  │    eval / die / $@                        ← error handling               │
  │    use Module / CPAN                      ← ecosystem                    │
  └───────────────────────────────────────────────────────────────────────────┘
```

> "The Swiss Army chainsaw." AWK+sed+sh in one coherent language. The original practical scripting language that built the early internet's infrastructure and still runs in bioinformatics, sysadmin tooling, and legacy codebases everywhere.

---

## Language Snapshot

| Attribute | Value |
|-----------|-------|
| Platform | All Unix/Linux/macOS (built-in on most distros); Windows via Strawberry Perl |
| Extension | `.pl` (scripts), `.pm` (modules) |
| Shebang | `#!/usr/bin/perl` or `#!/usr/bin/env perl` |
| Paradigm | Imperative + OOP + functional; regex-native |
| Typing | Dynamic; context-sensitive (scalar vs list) |
| Execution | Compiled to op-tree, then interpreted (not bytecode files like Java) |
| Version | 5.38 current; 5.10+ for `//`, `say`, `state`; 5.36+ for signatures |

---

## Three Modes of Perl

```
Perl exists in three modes:

  1. AWK/sed replacement — one-liners
     perl -e 'code'              execute code string
     perl -n -e '...'            implicit while(<>) loop (like awk pattern block)
     perl -p -e '...'            loop + auto-print $_ (like sed)
     perl -i -e '...' file       in-place edit (like sed -i, cross-platform)

  2. Shell script replacement — .pl scripts
     #!/usr/bin/perl
     use strict; use warnings;
     # Full program: file I/O, regex, data structures, CPAN modules

  3. Module / OOP system — larger programs
     package My::Module;
     use Moose;                  class hierarchies, method dispatch
     # CPAN-deployable modules, type constraints, roles
```

---

## Bridge: Typed Language → Perl Data Structures

Any developer coming from a typed language (C#, Java, Go, TypeScript) needs this map. Perl's type system is dynamic and context-sensitive — the same container can hold any value at runtime. The sigil (`$`, `@`, `%`) reflects the *shape* you're accessing, not a declared type.

```
TYPED LANGUAGE          PERL EQUIVALENT         NOTES
──────────────────────  ──────────────────────  ────────────────────────────────────────────
string / int / float    $scalar                 No type distinction at runtime. "42" and 42
object                                          are the same thing in different contexts.
null / nil / None       undef                   The absence of a value. Warns under
                                                'use warnings' if used without check.
T?? / null coalescing   // defined-or operator  $x = $val // "default";
                                                // is undef-safe; || fires on 0 and ""
List<T> / ArrayList     @array                  Ordered, resizable, 0-indexed.
                                                push/pop/shift/unshift/splice.
Dictionary<K,V>         %hash                   Unordered key-value. Keys are strings.
HashMap<K,V>            $href = {k => v}        Anonymous hash ref for nesting.
T[]  / new T[]{...}     [1, 2, 3]               Anonymous array ref — a reference (pointer).
string[]  literal       qw(foo bar baz)         Whitespace-delimited string list.
                                                Equivalent to ('foo', 'bar', 'baz').
pointer / reference     \@array  \%hash  \$x    Reference to existing container.
                        $aref = [...]           Anonymous array ref — like new T[]{...}
                        $href = {...}           Anonymous hash ref — like new Map<>()
lambda / delegate       sub { ... }             Anonymous subroutine — a code reference.
                        $cref = \&func_name
caller context          wantarray()             No typed-language equivalent.
                                                Returns true in list context, false in scalar.
                                                Perl functions can change their return shape
                                                based on how the caller receives the value.
```

Sigil-shift rule — the one thing that surprises every typed-language developer:

```perl
# The sigil on ACCESS reflects the return TYPE, not the container type
my @arr   = (1, 2, 3);
$arr[0]               # $ — single scalar element from @arr
@arr[0, 1]            # @ — slice (multiple elements) from @arr

my %hash  = (a => 1, b => 2);
$hash{a}              # $ — single scalar value from %hash
@hash{qw(a b)}        # @ — hash slice (multiple values) from %hash

# This is NOT a type error. It is intentional: the sigil tells you the shape of the result.
```

---

## Syntax Reference Card

### Variables and Sigils

```perl
# Sigil determines TYPE, but changes on access based on what you're extracting

# $ = scalar (single value)
my $str   = "hello";
my $num   = 42;
my $float = 3.14;
my $undef = undef;

# @ = array (ordered list of scalars)
my @array = (1, 2, 3);

# % = hash (unordered key-value pairs)
my %hash = (name => "Alice", age => 42);

# SIGIL SHIFTS ON ACCESS — this is the #1 Perl confusion point
$array[0]              # single element of @array  → uses $
$hash{name}            # single value from %hash   → uses $
@array[0, 1]           # multi-element slice        → uses @ (returns list)
@hash{qw(name age)}    # multi-key hash slice       → uses @ (returns list)
$#array                # last index (not length!)
scalar @array          # length (force scalar context)

# Scoping
my $x    = 5;    # lexical scope — ALWAYS use this
our $x   = 5;    # package global (accessible from other packages)
local $x = 5;    # dynamic scope — temporarily overrides package global in this call stack

# Without my/our/local: implicit package global. use strict; forbids this.

use strict;      # require my/our/local; disallow barewords
use warnings;    # warn on likely mistakes (uninitialized vars, etc.)
# These two lines go at the top of every Perl script. Non-negotiable.
```

---

### String Quoting

```perl
# Single-quoted: fully literal (only \' and \\ are escapes)
my $s = 'no $interpolation, no \n newline';

# Double-quoted: interpolation + escape sequences
my $name = "Alice";
my $msg  = "Hello, $name!\n";
my $expr = "Sum: ${\(2+3)}";           # expression interpolation
my $call = "Len: ${\length($name)}";   # function result interpolation

# Escape sequences in double-quoted strings
"\n"  "\t"  "\r"  "\\"  "\""  "\$"
"\x41"           # hex literal → 'A'
"\x{263A}"       # Unicode code point → ☺

# qq{} — generalized double-quote (any balanced delimiter)
my $s = qq{Hello, $name!};
my $s = qq(parens work);
my $s = qq[brackets work];
my $s = qq/slashes work/;

# q{} — generalized single-quote
my $s = q{no $interpolation here};

# qw{} — quote words: whitespace-delimited list of strings (extremely common)
my @days = qw(Monday Tuesday Wednesday Thursday Friday);
# equivalent: ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
# Used everywhere in Perl — idiomatic for array literals

# Here-doc
my $text = <<END;
Line one with $name interpolated
Line two
END

my $literal = <<'END';
No $interpolation: single-quote sigil on delimiter
END

# qr{} — compiled regex object
my $pat = qr/\d{4}-\d{2}-\d{2}/;
if ($date =~ $pat) { ... }    # precompiled; reused without recompilation
```

---

### Context: Scalar vs List

```perl
# Perl has two primary evaluation contexts: scalar and list.
# The SAME expression can return different things in each.

my @arr = (1, 2, 3);

# Scalar context — gets count
my $n   = @arr;           # → 3 (array in scalar context = element count)
if (@arr) { ... }         # true if non-empty
scalar @arr               # explicit scalar context
$#arr                     # last index = 2

# List context — gets elements
my @copy          = @arr;          # (1, 2, 3)
my ($head, @tail) = @arr;          # head=1, tail=(2,3)
my ($a, $b, $c)   = (10, 20, 30);

# Context changes function return values
my $s = localtime();    # scalar: "Sat Feb 22 12:00:00 2026"
my @t = localtime();    # list:   (sec, min, hour, mday, mon, year, wday, yday, isdst)

# Numeric vs string context
my $s = "42abc";
my $n = $s + 0;          # → 42 (numeric context: stops at first non-digit)
my $b = $s . "!";        # → "42abc!" (string context: concatenation)
```

---

### Arrays

```perl
my @a = (1, 2, 3, 4, 5);

# Access
$a[0]                            # first element (0-indexed)
$a[-1]                           # last element
scalar @a                        # length
$#a                              # last index (= length - 1)

# Slices
@a[1..3]                         # elements at indices 1,2,3 → (2,3,4)
@a[0, 2, 4]                      # elements at 0,2,4 → (1,3,5)

# Mutation
push @a, 6;                      # append (one or more)
push @a, (7, 8, 9);
pop @a;                          # remove and return last
shift @a;                        # remove and return first
unshift @a, 0;                   # prepend
splice(@a, 2, 1);                # delete 1 element at index 2
splice(@a, 2, 0, 10, 11);        # insert at index 2
splice(@a, 2, 3, 10, 11);        # replace 3 elements at index 2 with 10, 11

# Common operations
my @sorted  = sort @a;                       # lexicographic
my @numsort = sort { $a <=> $b } @a;         # numeric ascending
my @rev     = reverse @a;
my @evens   = grep { $_ % 2 == 0 } @a;      # filter (like Where-Object)
my @doubled = map  { $_ * 2 } @a;           # transform (like Select-Object)
my $sum     = 0; $sum += $_ for @a;         # sum
my @uniq    = do { my %s; grep { !$s{$_}++ } @a };  # deduplicate (preserve order)
```

---

### Hashes

```perl
my %h = (name => "Alice", age => 42, city => "Seattle");
# => is the "fat comma" — identical to , but auto-quotes the left side

# Access
$h{name}                         # value by key

# Mutation
$h{email} = 'alice@example.com'; # add / update key
delete $h{city};                 # remove key

# Existence vs definition
exists $h{name}                  # true if key exists (even if value is undef)
defined $h{name}                 # true if value is defined (not undef)

# Keys, values, iteration
my @keys = keys %h;              # unordered list of keys
my @vals = values %h;
while (my ($k, $v) = each %h) { # iterate pairs (each returns (k,v) then () when done)
    print "$k = $v\n";
}
for my $k (sort keys %h) {      # sorted iteration (common idiom)
    print "$k = $h{$k}\n";
}

# Hash slice
my @subset = @h{qw(name age)};  # → ("Alice", 42)
@h{qw(x y)} = (1, 2);          # assign multiple keys

# Hash references (anonymous hash)
my $person = { name => "Bob", age => 30 };   # ref to anonymous hash
$person->{name}                  # dereference with ->
$$person{name}                   # also valid

# Reference to existing hash
my $href = \%h;
$href->{name}
%{$href}                         # whole hash from ref
```

---

### Regex — Perl's Killer Feature

```perl
# Match operator: =~  (not-match: !~)
if ($str =~ /pattern/)  { ... }
if ($str !~ /pattern/)  { ... }

# Flags (suffix after closing delimiter)
/pattern/i      # case-insensitive
/pattern/g      # global (all matches)
/pattern/m      # multiline: ^ and $ match per-line
/pattern/s      # single-line: . matches \n
/pattern/x      # extended: ignore whitespace, allow comments
/pattern/e      # evaluate replacement as Perl code (in s///)

# Capture groups — $1, $2, ... are automatic
if ("2026-02-22" =~ /(\d{4})-(\d{2})-(\d{2})/) {
    my ($year, $month, $day) = ($1, $2, $3);
}

# Named captures
if ($str =~ /(?<year>\d{4})-(?<month>\d{2})/) {
    print $+{year}, "\n";
}

# Global match — collect all occurrences
my @nums = ($str =~ /(\d+)/g);   # all number sequences

# Non-greedy quantifiers
/a.*?b/         # shortest match between a and b
/a.+?b/
/a.{2,5}?b/

# Lookahead / lookbehind
/foo(?=bar)/    # foo followed by bar
/foo(?!bar)/    # foo NOT followed by bar
/(?<=foo)bar/   # bar preceded by foo
/(?<!foo)bar/   # bar NOT preceded by foo

# Substitution operator: s///
$str =~ s/foo/bar/;              # replace first
$str =~ s/foo/bar/g;             # replace all
$str =~ s/foo/bar/i;             # case-insensitive
$str =~ s/(\w+)/ucfirst($1)/ge; # /e: replacement is eval'd as Perl code

# tr/y — transliterate (like sed y///)
$str =~ tr/a-z/A-Z/;            # lowercase to uppercase
my $count = ($str =~ tr/e//);   # count occurrences of 'e'

# split / join
my @parts = split /,/,   $line;         # split on regex
my @parts = split /\s+/, $line;         # split on whitespace
my @parts = split /,/,   $line, 3;      # limit to max 3 parts
my $str   = join(", ", @parts);         # join with separator

# Compiled regex object
my $pat = qr/\d{4}-\d{2}-\d{2}/;       # compiled once
if ($date =~ $pat) { ... }
```

---

## Regex Bridge: PCRE → Perl

Perl regex is the origin. PCRE (Perl Compatible Regular Expressions) is named after Perl — Python `re`, Java `Pattern`, .NET `System.Text.RegularExpressions`, PHP `preg_*` are all implementations of the Perl regex spec. If you know any PCRE-flavored engine, you already know most of Perl regex. The differences are few but worth mapping explicitly.

```
FEATURE                PCRE (common denominator)       Perl-specific behavior
─────────────────────  ──────────────────────────────  ──────────────────────────────────────
Match                  m.match(str) / str.match(pat)   $str =~ /pattern/
Non-match              (negate result)                 $str !~ /pattern/
Substitution           re.sub / str.replaceAll         $str =~ s/pattern/replacement/
Positional captures    $1 $2 (most tools)              $1 $2 — same
Named captures         (?P<name>...) Python            (?<name>...) — same as .NET / JS
                       (?<name>...) .NET, JS, PCRE2
Named cap access       group dict / Groups["name"]     $+{name}
Non-greedy             .*? .+? .{n,m}?                 .*? .+? — same
Flags: case-insensitive /i or RegexOptions.Ignorecase  /i — same position, suffix
Flags: global          re.sub replaces all             /g on s/// or =~ in list context
Flags: multiline       re.MULTILINE / (?m)             /m — ^ and $ match per line, same
Flags: dotall          re.DOTALL / (?s)                /s — . matches \n, same
Flags: verbose         re.VERBOSE / (?x)               /x — same; inline comments
Non-destructive        re.sub returns new string       /r modifier: $new = $str =~ s/a/b/r
                       (original unchanged)            returns modified copy; $str unchanged
Eval replacement       no equivalent                   /e: s/(\d+)/$1*2/e (eval as code)
\K keep / reset-start  not in most PCREs               \K: resets start of match; no lookbehind
                                                        needed for "replace after prefix" patterns
\b word boundary        \b — same                      \b — same
Precompile             re.compile(pat)                 qr/pattern/ — compiled regex object
```

What this means in practice:

```perl
# Named captures — same syntax as .NET / modern PCRE
if ($str =~ /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/) {
    print $+{year};      # $+{name} — different from Python's .group('name')
}                        #            but same as .NET Groups["year"]

# /r — non-destructive (5.14+)
my $new = $str =~ s/foo/bar/r;   # $str is unchanged; $new has the result
# Python equiv: new = re.sub('foo', 'bar', str)  — same semantics

# /e — evaluate replacement as code (no PCRE equivalent)
$str =~ s/(\d+)/$1 * 2/e;              # double every number
$str =~ s/(\w+)/ucfirst(lc $1)/ge;     # title-case every word

# /x — verbose mode (same as Python re.VERBOSE)
$str =~ /
    (\d{4})    # year
    -
    (\d{2})    # month
    -
    (\d{2})    # day
/x;

# \K — avoid lookbehind (Perl-specific, not in standard PCRE)
$str =~ s/PREFIX\K.*/replacement/;     # replace everything AFTER PREFIX
# without \K you'd need: s/(?<=PREFIX).*/ -- but \K is simpler and no length limit

# /s — dot matches newline (needed for multiline content in one string)
perl -0777 -pe 's/START.*?END/REDACTED/s' file   # whole-file mode + /s
```

---

### Control Flow

```perl
# if / elsif / else
if ($x > 0) {
    print "positive\n";
} elsif ($x == 0) {
    print "zero\n";
} else {
    print "negative\n";
}

# unless — negated if (use sparingly; double negatives kill readability)
unless ($error) { do_thing() }

# Postfix form — very idiomatic Perl; reads like English
print "positive\n"  if     $x > 0;
do_thing()          unless $error;
$x++                while  $x < 10;
print "$_\n"        for    @array;

# Ternary
my $msg = $x > 0 ? "positive" : "non-positive";

# Hash dispatch table (preferred over given/when which is experimental)
my %dispatch = (
    add => sub { $_[0] + $_[1] },
    sub => sub { $_[0] - $_[1] },
    mul => sub { $_[0] * $_[1] },
);
my $result = $dispatch{$op}->($a, $b)
    if exists $dispatch{$op};
```

---

### Loops

```perl
# foreach / for — identical keywords
foreach my $item (@array) { print "$item\n"; }
for    my $item (@array)  { print "$item\n"; }

# $_ default variable — often omitted in short loops
for (@array) { print "$_\n"; }
print "$_\n" for @array;

# C-style for
for (my $i = 0; $i < 10; $i++) { print "$i\n"; }

# while — reads lines from filehandle naturally
while (my $line = <$fh>) {
    chomp $line;
    process($line);
}

# Loop control
next;          # continue (skip to next iteration) — like C continue
last;          # break — like C break
redo;          # restart current iteration without re-evaluating condition

# Labeled loops — named break/continue through nested loops
OUTER: for my $i (1..5) {
    for my $j (1..5) {
        last OUTER if $i == $j;    # break out of both loops
        next OUTER if $j == 3;     # continue outer loop
    }
}
```

---

### Subroutines

```perl
# Define
sub greet {
    my ($name, $greeting) = @_;    # unpack from @_ (all args land here)
    return "Hello, $name!";        # explicit return
}

# Call
my $msg = greet("Alice", "Hi");

# Named parameters (hash idiom)
sub connect {
    my (%args) = @_;
    my $host = $args{host} // "localhost";  # // is defined-or (5.10+)
    my $port = $args{port} // 5432;
}
connect(host => "db.example.com", port => 5433);

# Function references and closures
my $double = sub { $_[0] * 2 };
$double->(5);                        # → 10; call via ->

sub make_adder {
    my $n = shift;                   # shift pops first element of @_
    return sub { $n + shift };       # closure — captures $n from outer scope
}
my $add5 = make_adder(5);
$add5->(3);                          # → 8

# wantarray: know your calling context
sub flexible {
    return wantarray ? (1, 2, 3) : 3;
}

# Signatures (5.20+ experimental; stable/default in 5.36)
use feature 'signatures';
sub add($a, $b) { $a + $b }          # no more my ($a,$b) = @_
```

---

### File I/O

```perl
# Three-argument open — ALWAYS use this form (never two-argument)
open(my $fh, '<',  'file.txt')  or die "open failed: $!";   # read
open(my $fh, '>',  'file.txt')  or die "create failed: $!"; # write (truncate)
open(my $fh, '>>', 'file.txt')  or die "append failed: $!"; # append
open(my $fh, '+<', 'file.txt')  or die "r/w failed: $!";    # read+write
open(my $fh, '-|', 'ls -la')   or die "pipe failed: $!";    # read from command
open(my $fh, '|-', 'sort')     or die "pipe failed: $!";    # write to command

# Read
my $line  = <$fh>;              # one line (includes \n)
chomp $line;                    # strip trailing \n
my @lines = <$fh>;              # slurp entire file into array
while (my $line = <$fh>) {     # line-by-line (preferred for large files)
    chomp $line;
    process($line);
}

# Slurp entire file as single string
my $content = do { local $/; <$fh> };   # undef $/ = no record separator

# Diamond operator <> — reads from @ARGV files or stdin (classic Unix filter)
while (<>) {
    chomp;
    print "Line: $_\n";
}

# Write
print $fh "text\n";
printf $fh "%s: %d\n", $key, $val;
say $fh "auto-newline";          # say = print + \n  (use feature 'say')

close $fh;

# File test operators (prefix -X)
-e $path    # exists
-f $path    # regular file (not dir, not symlink)
-d $path    # directory
-r $path    # readable by effective uid
-w $path    # writable
-x $path    # executable
-s $path    # size in bytes (0 = empty, so also boolean for non-empty)
-l $path    # symbolic link
-M $path    # age in days since modification (float)
-z $path    # zero size
```

---

### Error Handling

```perl
# die / warn
open(my $fh, '<', $file) or die "Can't open $file: $!";  # $! = OS errno string
warn "suspicious value: $x\n";   # like die but does not exit

# eval {} — try block
eval {
    risky_operation();
    die "something went wrong";   # die with string
};
if ($@) {                         # $@ = caught exception (empty string if none)
    print "Caught: $@\n";
}

# die with object (structured exceptions)
eval {
    die { code => 404, message => "not found" };
};
if (ref $@) {
    printf "Error %d: %s\n", $@->{code}, $@->{message};
}

# Trailing \n on die suppresses " at file line N" annotation
die "fatal\n";           # just "fatal"
die "fatal";             # "fatal at script.pl line 42."

# use autodie — system calls die automatically on failure
use autodie;
open(my $fh, '<', $file);    # dies on failure; no 'or die' needed

# Carp — report errors from caller's perspective (for module authors)
use Carp;
croak   "error (reported at caller)";    # like die
confess "error (with stack trace)";      # die + full stack trace
carp    "warning (at caller)";           # like warn
cluck   "warning (with stack trace)";
```

---

### One-Liner Mode

```bash
# -e: execute code string
perl -e 'print "hello\n"'

# -n: implicit while(<>){ ... } loop — reads stdin or @ARGV files
perl -ne 'print if /pattern/'            # grep equivalent
perl -ne 'print if $. >= 10 && $. <= 20' # lines 10-20 ($. = line number)

# -p: like -n but also prints $_ after each loop body
perl -pe 's/foo/bar/g'                   # sed s/// replacement — cross-platform!
perl -pe 's/foo/bar/gi'                  # case-insensitive

# -i: in-place edit (like sed -i but portable)
perl -i.bak -pe 's/foo/bar/g' file.txt  # with .bak backup
perl -i     -pe 's/foo/bar/g' file.txt  # no backup (dangerous)

# -a: autosplit each line into @F (like awk's field splitting)
perl -ane 'print $F[1], "\n"'            # print second field (default split on whitespace)
perl -F: -ane 'print "$F[0]\n"'          # split on : (-F sets separator)

# -l: auto-chomp input lines; auto-append \n to print output
perl -lne 'print length($_)'             # print line lengths cleanly

# -0777: slurp entire file as one string (null record separator)
perl -0777 -pe 's/pattern/replace/gs'   # whole-file regex (. matches \n with /s)

# Practical one-liners
perl -ne  'print if /ERROR/'                             # grep
perl -pe  's/\bfoo\b/bar/g'                             # word-boundary replace
perl -ane 'print if $F[2] > 100'                        # filter by column value
perl -ne  'print unless /^#/ || /^\s*$/'                # strip comments + blanks
perl -ne  '!$seen{$_}++ and print'                      # uniq (preserve order)
perl -e   'print join "\n", sort <>'                    # sort all input lines
perl -MList::Util=sum -ane '$t += $F[0]; END{print "$t\n"}' # column sum
perl -pe  's/(\w+)/ucfirst(lc $1)/ge'                   # title-case words
perl -ne  'print if $. == 42'                           # print specific line
```

---

## References and Data Structures

```perl
# References: the mechanism for complex data structures
my $sref = \$scalar;      # scalar ref
my $aref = \@array;       # array ref
my $href = \%hash;        # hash ref
my $cref = \&sub_name;    # code ref

# Anonymous constructors
my $aref = [1, 2, 3];             # anonymous array ref
my $href = { name => "Alice" };   # anonymous hash ref
my $cref = sub { $_[0] * 2 };    # anonymous sub ref

# Dereference
$$sref                     # scalar
@{$aref}  or  @$aref       # array
%{$href}  or  %$href       # hash
$aref->[0]                 # array element via ->
$href->{name}              # hash value via ->
$cref->()                  # call code ref

# Nested structures
my %config = (
    db => {
        host => "localhost",
        port => 5432,
        creds => ["admin", "secret"],
    },
    cache => {
        ttl  => 300,
        keys => [qw(a b c)],
    },
);

$config{db}{host}          # hash of hashes: nested -> optional at top level
$config{db}{creds}[0]      # hash → hash → array
push @{ $config{db}{creds} }, "extra";  # push onto nested array ref

# Array of hashes (very common pattern)
my @users = (
    { name => "Alice", age => 42 },
    { name => "Bob",   age => 30 },
);
for my $user (@users) {
    printf "%s is %d\n", $user->{name}, $user->{age};
}
my @adults = grep { $_->{age} >= 18 } @users;
my @names  = map  { $_->{name} } @users;
```

---

## Modern Perl (5.10 — 5.38)

```perl
use v5.36;     # enables: strict + warnings + say + signatures + etc.

# say — print with automatic \n (5.10+)
say "hello";                     # equivalent to print "hello\n"

# defined-or // (5.10+)
my $x = $val // "default";       # use "default" only if $val is undef
#   vs || which fires on any false value (0, "", "0", undef)

# state variables (5.10+) — initialized once, persist across calls
use feature 'state';
sub counter { state $n = 0; ++$n }
counter();  # → 1
counter();  # → 2

# Subroutine signatures (5.20+ experimental; stable default in 5.36)
use feature 'signatures';
sub add($a, $b)           { $a + $b }
sub greet($name, $msg="Hi") { "$msg, $name" }  # default argument

# Postfix dereference (5.20+) — reads left-to-right
$arrayref->@*              # instead of @{$arrayref}
$hashref->%*               # instead of %{$hashref}
$coderef->&*               # instead of &{$coderef}

# use strict + warnings always (or use v5.36 which includes them)
```

---

## Ecosystem

| Area | Module / Tool |
|------|---------------|
| Package manager | CPAN; `cpanm` (cpanminus); `Carton` (like Bundler — lockfile) |
| HTTP client | `LWP::UserAgent`, `HTTP::Tiny` (core), `Mojo::UserAgent` |
| Database | `DBI` (universal adapter) + `DBD::Pg`, `DBD::mysql`, `DBD::SQLite` |
| JSON | `JSON::XS`, `Cpanel::JSON::XS`, `Mojo::JSON` |
| OOP system | `Moose` (full-featured), `Moo` (lighter), `Mouse` (faster load) |
| Web framework | `Mojolicious` (modern, async), `Dancer2`, `Plack/PSGI` |
| Regex tools | `Regexp::Common`, `Text::CSV` (proper CSV — never hand-parse CSV) |
| File handling | `Path::Tiny` (modern path API), `File::Find`, `File::Temp` |
| Testing | `Test::More`, `Test::Exception`, `Test2::Suite` |
| Template | `Template::Toolkit` (TT2), `Text::Template` |
| Linter / format | `Perl::Critic` (PBP compliance), `perltidy` (formatter) |
| Debugger | `perl -d script.pl`; `Devel::NYTProf` (profiler) |
| Bioinformatics | BioPerl ecosystem — the dominant use of Perl today |

---

## What Makes Perl Distinct

```
TMTOWTDI — "There's More Than One Way To Do It"
  Perl's explicit design philosophy. Contrast with Python's TOOWTDI.
  Consequence: Perl written by different people looks like different languages.

Regex as first-class syntax:
  Most languages:  import re; re.sub(pattern, repl, string)
  Perl:            $str =~ s/pattern/replacement/g;
  Flags are suffix characters. $1 $2 $& are automatic. qr// precompiles.
  This is not a library call — it is grammar-level syntax.

Context-sensitivity — same expression, different results:
  scalar @arr     → count
  my @copy = @arr → elements
  localtime()     → string in scalar context, 9-element list in list context
  This is the single biggest conceptual leap for people coming from typed languages.

Default variable $_ — implicit iteration:
  for (@arr)  { print }          # $_ is each element; print prints $_
  s/foo/bar/                     # operates on $_ if no =~ binding
  Powerful shorthand; makes code terse (sometimes too terse).

Sigil shift on access — the classic confusion source:
  @arr is the array
  $arr[0] accesses ONE element → scalar → uses $
  @arr[0,1] accesses a SLICE  → multiple values → uses @
  The sigil reflects the return TYPE, not the container type.
```

---

## Gotchas & Traps

| Trap | Issue | Fix |
|------|-------|-----|
| `$arr[0]` not `@arr[0]` for single element | Sigil reflects return type, not container | Remember: one element → `$`; multiple → `@` |
| `eq` vs `==` | `==` is numeric, `eq` is string comparison | `"5" == "5.0"` → true; `"5" eq "5.0"` → false |
| Missing `chomp` | `<$fh>` includes trailing `\n` | Always `chomp` after read, unless you want the newline |
| `.` for concatenation | `"a" + "b"` → 0 (numeric!), not `"ab"` | Use `.`: `"a" . "b"` |
| `@_` is aliased | `$_[0] = "new"` modifies the CALLER's variable | Always unpack: `my ($a) = @_` |
| Forgetting `my` / `use strict` | Typo in variable name silently creates new global | `use strict;` makes this a compile error |
| `||` vs `//` for defaults | `$x = $val || "default"` fires on `0` and `""` | Use `//`: `$x = $val // "default"` |
| `die` appends location | `die "msg"` → `"msg at file line N\n"` | `die "msg\n"` — trailing `\n` suppresses the location |
| `$@` cleared by eval | Nested `eval` clobbers `$@` | Save `my $err = $@` immediately after `eval {}` |
| Hash in list context | `%h` flattens to `(k,v,k,v,...)` — order not guaranteed | Use `keys %h` explicitly; never rely on hash order |
| `sort` is lexicographic by default | `sort (10, 9, 100)` → `(10, 100, 9)` | Always provide comparator: `sort { $a <=> $b }` |
| `local` vs `my` | `local` is DYNAMIC scope (affects called functions); `my` is lexical | Use `my` unless you explicitly need dynamic scope |

---

## Perl vs Python Decision Cheat Sheet

| Use Perl when... | Use Python when... |
|-----------------|-------------------|
| Complex regex with substitution (`s///e`) | Data science / ML (numpy, pandas, sklearn) |
| One-liners replacing sed/awk | Web APIs and HTTP client work |
| Legacy Perl codebase maintenance | Team already knows Python |
| Bioinformatics (BioPerl, BLAST scripts) | Structured data (JSON/YAML heavy processing) |
| In-place file edits (`perl -i`) | Long-term maintainability in a team |
| Sysadmin on older Linux where Perl is guaranteed | New greenfield projects |
| Cross-platform `s///` without sed BSD/GNU differences | When readability matters more than terseness |
| Need DBI (best Perl DB interface) | Async / web framework work |
