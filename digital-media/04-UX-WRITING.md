# UX Writing: Microcopy, Error Messages, Onboarding, Conversational UI

## The Big Picture

```
UX WRITING SCOPE
=================

+------------------------------------------------------------------+
|                    INTERFACE TEXT DOMAINS                        |
|                                                                  |
|  NAVIGATION          FORMS              ERROR STATES            |
|  Labels, tabs,       Field labels,      Error messages,         |
|  menu items,         placeholder text,  validation messages,    |
|  breadcrumbs         help text          empty states            |
|                                                                  |
|  ONBOARDING          NOTIFICATIONS      ACTIONS                 |
|  Welcome messages,   Push, in-app,      Button labels,          |
|  tooltips, tours,    email subject      CTAs, confirm dialogs   |
|  empty states        lines              destructive actions     |
|                                                                  |
|  TRANSACTIONAL       SYSTEM STATUS      CONVERSATIONAL          |
|  Confirmation,       Loading states,    Chatbot, voice UI,      |
|  receipts,           progress bars,     AI assistant,           |
|  invoices            sync indicators    Siri/Alexa scripts      |
+------------------------------------------------------------------+

UX Writing is NOT:
  - Marketing copy (sells features)
  - Documentation (explains systems)
  - Journalism (informs broadly)

UX Writing IS:
  - Functional text that enables task completion
  - The words users don't notice when they work
  - The words users DO notice when they fail
```

---

## Microcopy: The High-Stakes Small Text

Microcopy is the small words that have outsized impact: button labels, error messages, empty states, form hints.

### Button Labels

```
BUTTON LABEL PRINCIPLES
========================

SPECIFIC BEATS GENERIC:
  WRONG: "Submit" (what does submit do?)
  RIGHT: "Create account" / "Send message" / "Pay $99"
  The label should complete: "I want to ___"
  User clicks "Create account" -- they know what happens

ACTION VERB + OBJECT PATTERN:
  [verb] [object] [context]
  "Download PDF"
  "Schedule meeting"
  "Save changes"
  "Delete account" (not just "Delete" -- object required)

DESTRUCTIVE ACTIONS:
  Must be specific and final-sounding
  "Delete account" not "Remove"
  "Cancel subscription" not "Opt out"
  Confirmation pattern:
    First: "Delete account"
    Confirm dialog: "Delete your account? This cannot be undone."
    Final button: "Yes, delete my account" (echo the severity)
    Cancel button: "Keep my account" (echo what user keeps)

POSITIVE CTA IN ALERTS:
  Keep "positive" action (what user wants) on the right
  Keep "negative" action (dismiss, cancel) on the left
  Exception: Google Material Design inverts this for destructive
  Consistency matters more than "right" answer
```

---

## Error Message Architecture

Error messages are the most important microcopy — they appear when the system and the user are misaligned.

```
ERROR MESSAGE ANATOMY
======================

THREE COMPONENTS (all required):
  1. WHAT HAPPENED:
     Describe the error without blame
     "Your payment wasn't processed"
     NOT: "You entered an invalid credit card number"
           (blame) OR "Payment error" (vague)

  2. WHY IT HAPPENED (when not obvious):
     "Your session expired after 30 minutes of inactivity"
     NOT required if obvious: "Email address is already in use"
           (why is clear: already registered)

  3. WHAT TO DO:
     Specific, actionable next step
     "Try your payment again, or use a different card."
     "Sign in again to continue"
     "Contact support if this keeps happening"

TONE:
  Calm: the user is already frustrated; alarm makes it worse
  Direct: no technical jargon
  Helpful: a path forward always

VALIDATION ERRORS (form fields):
  Inline: show near the field that has the error
  Immediate vs. submit-time: show on blur (leaving field)
    OR on form submit? Research says: on submit is less disruptive
  Specific: "Password must be at least 8 characters"
    NOT: "Invalid password"
  Positive when possible: "3 more characters needed"
    (shows progress toward success, not just failure)
```

### Error Message Anti-patterns

```
COMMON ERROR MESSAGE FAILURES
==============================

TECHNICAL ERROR CODES TO USERS:
  "Error 403: Forbidden" (developer message, not user message)
  INSTEAD: "You don't have permission to view this page.
            Contact your admin if you need access."

BLAME:
  "You have not completed the required fields"
  INSTEAD: "Please add your email address to continue"

VAGUE / UNHELPFUL:
  "Something went wrong"
  INSTEAD: "We couldn't load your profile. Refresh the page
            or contact support."

HUMOROUS WHEN USER IS STRESSED:
  A 404 page with a funny animation is fine
  An error during checkout with a joke: bad
  Match emotional context: comedy for inconvenience;
  clarity for failure of important tasks

AMBIGUOUS CONFIRMATION:
  "Are you sure you want to delete this?"
  Button options: "Yes" / "No" -- yes, what? no, what?
  INSTEAD: "Delete this project?"
  Buttons: "Delete project" / "Cancel"
```

---

## Empty States

Empty states appear when there is no content to display (new user, empty search results, filtered-to-zero).

```
EMPTY STATE DESIGN
===================

THREE TYPES:
  1. FIRST-USE EMPTY STATE:
     User just created an account; nothing in their inbox yet
     Best practice:
       Explain what will appear here
       Give the action that creates the first item
       Make the action button the primary CTA
     Example: GitHub empty repo
       "This repository has no content yet."
       "Create a README" [button]
       "Upload files" [button]

  2. NO-RESULTS EMPTY STATE:
     Search or filter returned nothing
     Best practice:
       Confirm what they searched for (echo their query)
       Suggest alternatives (check spelling, broaden search)
       Do NOT say "No results found" alone -- offer a next step
     Example:
       "No results for 'azuure'"
       "Did you mean 'azure'?"
       OR: "Try different keywords, or [browse all products]"

  3. CLEARED EMPTY STATE:
     User completed all tasks (empty inbox, no notifications)
     Best practice:
       Celebrate completion (this is a success state, not failure)
       "You're all caught up!" > "No items to display"

EMOTIONAL REGISTER:
  Empty states are opportunity moments -- the user is receptive
  Use encouraging, forward-looking language
  "Start your first project" > "No projects yet"
```

---

## Onboarding Copy

The most consequential writing in a product: the first few interactions shape whether users return.

```
ONBOARDING COPY PRINCIPLES
============================

REDUCE TIME-TO-VALUE:
  Users care about doing the thing, not learning the product
  "What does this do for me?" not "How does this work?"
  Onboarding copy should point toward the user's goal:
    "Add your first project to get your personalized dashboard"
    NOT: "Welcome to ProjectTool! Here's a tour of our features"

PROGRESSIVE DISCLOSURE:
  Show only what the user needs to complete the current step
  Next step revealed when current step is complete
  Cognitive load principle: don't overwhelm at start

SKIP OPTIONS:
  Users who know what they're doing resent forced tours
  Always offer "Skip" or "I'll explore on my own"
  Track skip rates: high skip = the tour isn't needed for
    competent users, or it's poorly designed for all users

TOOLTIP COPY:
  Show the tooltip for 1 action, not as a tour
  Point to specific UI element
  Text: 1-2 sentences; explain benefit, not mechanic
    WRONG: "This button opens the settings menu"
    RIGHT: "Adjust your notification preferences here"

GOAL-SETTING IN ONBOARDING:
  Ask users their goal early
  Use their answer to personalize the experience
  Duolingo: "Why are you learning Spanish?" -> 5 options
  -> Routes to appropriate lesson difficulty and style
  -> Makes users feel seen; improves retention
```

---

## Voice and Tone in UI

The Mailchimp Voice and Tone guide (mailchimp.com/voice-and-tone) is the canonical public example of applied UX writing voice:

```
MAILCHIMP VOICE AND TONE: THE MODEL
=====================================

FOUR VOICE TRAITS:
  1. Fun but not childish
     Wit and levity when appropriate
     Not jokes in error states or during payment failure
  2. Confident but not bossy
     "You can" > "You must"
     "Here's how" > "You need to"
  3. Smart but not academic
     Plain language for complex topics
     No jargon unless the audience uses it
  4. Expert but not elitist
     Share knowledge without condescension

TONE SPECTRUM:
  The tone changes to match the user's emotional state:
  Marketing context: playful, enthusiastic
  Setup/config: practical, direct
  Sending campaign: encouraging
  Error during send: calm, specific, action-focused
  Account suspended: very direct, no humor, clear path

WRITING TONE AXES (defined per-context):
  Formal 1 2 3 4 5 Casual
  Serious 1 2 3 4 5 Funny

Each content type gets a position on these axes
  Marketing: casual 4, funny 3
  Error messages: casual 2, funny 1
  Legal/privacy: formal 1, funny 1
```

---

## Accessibility in Writing

```
WRITING FOR ACCESSIBILITY
==========================

ALT TEXT:
  Describe what the image shows and its function
  Decorative images: alt="" (empty; screen reader skips)
  Informative images: describe the content
  Functional images (buttons): describe the action
    Button with magnifier icon: alt="Search" not alt="magnifier icon"
  Complex images (charts): summary + link to data table

READING LEVEL:
  Target: grade 8 for general audience
  Medical, legal: aim for grade 6-8 despite complex subject
  Technical docs for developers: grade 10-12 acceptable
  Readability tools: Hemingway App, built into Word/Docs

PLAIN LANGUAGE RULES:
  Short sentences (15-20 words average)
  Active voice preferred (passive obscures who does what)
  Common words over technical synonyms where possible
  Define technical terms on first use
  Avoid metaphors if audience is non-native English

COGNITIVE ACCESSIBILITY:
  Consistent label naming (don't call it "Save" in one place
    and "Submit" in another for the same action)
  Predictable patterns (confirmation before destructive action)
  Error recovery (clear path back from error states)
  Avoid time pressure in critical interactions
```

---

## The "Just" Problem

A well-known UX writing diagnostic:

```
THE "JUST" PROBLEM (and hedging language)
==========================================

"Just click the button"
"Simply navigate to settings"
"All you have to do is..."
"It's easy to..."

What these say to users who find it hard:
  "You're the problem -- it's supposed to be easy"
  Amplifies failure; makes users feel incompetent

HEDGING WORDS TO AVOID:
  just, simply, easy, basic, obvious, straightforward,
  "of course", "naturally", "as you know"

REPLACE WITH:
  Specific instructions: "Click Save to continue"
  No hedging: remove the word entirely
  "It's easy" is never true for users who find it hard

SIMILAR: AVOIDING "DON'T WORRY"
  "Don't worry -- your data is safe"
  Introduces the possibility of worry
  INSTEAD: "Your data is encrypted and backed up daily"
  (state the fact; don't mention the anxiety it prevents)
```

---

## Conversational UI and Chatbot Writing

```
CONVERSATIONAL UI PRINCIPLES
==============================

CHATBOT PERSONALITY:
  Consistent with brand voice
  But: more conversational register than web copy
  Users expect chat to feel like conversation

EXPECTATION SETTING:
  Users often don't know chatbot limits
  Chatbot must communicate what it can and can't do
  WRONG: Let users ask anything until they hit a wall
  RIGHT: "I can help with order status, returns, and billing.
          For account changes, I'll connect you to a human."

FALLBACK RESPONSES:
  When the bot doesn't understand:
  WRONG: "I don't understand. Please rephrase."
  RIGHT: "I'm not sure I understood that. Did you mean:
           • Check my order status?
           • Return an item?
           • Something else?"
  Offer options; don't dead-end

ESCALATION:
  Clear path to human when bot can't help
  Don't make users fight to find a human
  "Would you like me to connect you with a support agent?"

VOICE UI (Alexa, Siri, Google Assistant):
  No visual reference; audio is the only channel
  Responses must be self-contained and short
  Navigation through voice only: menus must be small
    (can't display 10 options; offer 3 max)
  Confirmation: always confirm destructive actions verbally
```

---

## Decision Cheat Sheet

| UX writing task | Key rule |
|----------------|---------|
| Button label | Verb + object: "Delete account", not "Submit" |
| Error message | What + why + what to do; no blame; calm tone |
| Destructive action confirmation | Echo the specific action; make consequences clear |
| Empty state | Explain what goes here; provide the action to fill it |
| Onboarding | Lead with user's goal/value; progressive disclosure |
| Form validation | Inline, specific, actionable; positive framing when possible |
| Alt text | Describe content AND function; "" for decorative |
| Hedging language | Remove "just", "simply", "easy" — they signal inaccessibility |

---

## Common Confusion Points

**UX writing is not marketing copy.** Marketing copy sells features. UX writing enables tasks. The register is different: marketing emphasizes benefit; UX writing emphasizes how. Writing "Powerful collaboration features" on a share button is marketing copy in the wrong place.

**"Error 403" is not an error message for users.** HTTP status codes are developer-facing. Users get a human-language explanation of what happened and what to do. The status code should be available (for support reference) but should not be the primary message.

**Confirmation dialogs are not optional for destructive actions.** Delete, cancel subscription, remove account — always require explicit confirmation. One-click irreversible actions create support burden and user distrust.

**Accessibility is not a checklist.** Alt text, reading level, plain language, and consistent labeling are not separate accessibility features — they are the same thing: writing that works for the full range of users, including people with cognitive disabilities, non-native speakers, and users under stress.

**"Don't worry" introduces worry.** Any sentence that mentions a potential anxiety activates that anxiety in readers who didn't have it. State the positive fact instead.
