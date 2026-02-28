# /hunt profile — Full Profile Rebuild from Confirmed Puzzle Data

Rebuild a reviewer profile completely from top to bottom, using confirmed puzzle credits and mechanics — not inference. Every section is rewritten. The output should read like the person, not a description of the person.

## Usage

```
/hunt profile <name>          — full rebuild of one profile
/hunt profile all             — rebuild all profiles in sequence
/hunt profile score           — score all profiles and list by quality
```

---

## What This Skill Produces

A complete profile with five sections. Each section has a specific job:

**What Makes Them Exceptional** — Why this person matters and what they've done that others haven't. Direct, specific, no hedging. 2–4 paragraphs. Makes you want to know what they think.

**Identity** — Role, affiliation, defining achievement, bio quote. One sentence each.

**Puzzle Hunt Credentials** — Every confirmed hunt credit, puzzle, and achievement. Tables where useful. Sourced from evidence only.

**Design Philosophy** — Their core conviction about what puzzles are for, in their voice. No puzzle titles cited by name. No mechanics described. Flowing prose, 3–5 paragraphs. Ends on something non-negotiable.

**Review Lens** — Their expert checklist. 10–12 items. Not a restatement of the philosophy — the things they actually check, including what they hate and would cut immediately.

---

## Process

### Step 1 — Load the profile

Read `toolkit/profiles/<name>.md`. Note everything already in it. The Credentials section stays. Everything else is rebuilt.

### Step 2 — Load all confirmed puzzle data

Check these sources in order:

1. `evidence/ms-hunt-puzzles-detail.md` — PH23 Economics + Placement Test mechanics
2. `evidence/ph23-all-rounds.md` — all PH23 rounds with author credits
3. `evidence/mit-mh-2009-puzzles.md` — MIT Mystery Hunt 2009 data
4. `evidence/ph-scraped/puzzle-university.json` — scraped solution pages

Extract all puzzles credited to this person from the JSON:
```bash
node -e "
const data = JSON.parse(require('fs').readFileSync('evidence/ph-scraped/puzzle-university.json'));
const sols = data.solutions || {};
const keys = Object.keys(sols).filter(k => (sols[k]||'').includes('<FULL NAME>'));
keys.forEach(slug => {
  const text = sols[slug] || '';
  const ansM = text.match(/Answer:\s*([A-Z][A-Z '!?.]+)/);
  const lines = text.split('\n').filter(l => l.trim());
  const idx = lines.findIndex(l => l.match(/^Answer:/));
  const mech = lines.slice(idx+1, idx+4).join(' ').substring(0, 300);
  console.log(slug + ' | ' + (ansM ? ansM[1].trim() : '?'));
  console.log(mech);
  console.log('');
});
"
```

For profiles without puzzle.university data (game designers, academics, community organizers), work from their documented philosophy: talks, essays, interviews, and published works already in the profile's Key Sources.

### Step 3 — Analyze before writing

With the puzzle list or documented philosophy in front of you, answer these before writing a word:

1. **What is their core conviction?** One sentence. Something most designers don't believe or don't act on. This is the opening line of the Design Philosophy.

2. **What is their specific expertise?** Not "puzzle design in general" — the specific thing they've done hundreds of times that nobody else has. Dana: visual puzzle material and world-building. Kenny: multi-constraint system architecture. This shapes the first half of the Review Lens.

3. **What would they cut immediately?** Think about the failure modes they've watched play out over a career. What makes them put a puzzle down? What do they see in the first 30 seconds that tells them the work isn't done? This is the second half of the Review Lens.

4. **What is their non-negotiable?** The thing they hold regardless of context — theme, difficulty, audience. This is the last sentence of the Design Philosophy.

### Step 4 — Write Design Philosophy

**Rules — enforce all of these:**
- One voice, one argument. Flowing prose, no section headers inside it.
- No puzzle titles or mechanics cited by name. Extract the principle.
- No citations. No "she believes that..." Write from inside the conviction.
- 3–5 paragraphs. If it takes more, the argument isn't clear yet.
- Open with the conviction. The first sentence states what they believe that most designers don't.
- End with the non-negotiable. The last sentence should be the thing they won't compromise on.

### Step 5 — Write Review Lens

**Structure:** One framing sentence about *how* they review (not what they believe). Then 10–12 bullet items.

**The items break into three zones:**

**Zone 1 — Expert diagnostics (items 1–5):** The things they check because of their specific expertise. What only someone who has built what they've built would know to look for. These are the architectural checks, the visual-language reads, the system tests that require fluency, not just attention.

**Zone 2 — Failure mode catches (items 6–9):** What they've seen break hundreds of times. Common failure modes that less experienced reviewers miss. Where puzzles fall apart in the last 20%, where themes dissolve, where extractions become tax, where difficulty becomes obscurity.

**Zone 3 — Cut decisions (items 10–12):** What they would remove. Not "this could be better" but "this doesn't belong here," "this is a costume not a mechanic," "this puzzle makes the hunt worse by being in it." The items that end with something going in the trash.

**Rules:**
- Each item is a demand, not a suggestion.
- Each item should be different from the philosophy — it checks something, it doesn't restate a belief.
- The lens should be usable by someone who hasn't read the philosophy. Each item stands alone.
- At least 3 items should be things the person would hate — puzzles they'd reject outright.
- The last item is a gut check: would this person want to have made this puzzle? If no, what do they do about it?

---

## Quality Bar

**Design Philosophy passes** when: reading it to someone who knows this person makes them say "yes, that's exactly how they think."

**Review Lens passes** when: it includes things from all three zones (expertise / failure modes / cut decisions), none of the items restate the philosophy, and at least 3 items would result in a puzzle being sent back or cut entirely.

**Both fail** if:
- The philosophy could describe any thoughtful puzzle designer
- The lens reads like philosophy in disguise
- The lens has nothing the person would hate

---

## What Makes Dana and Kenny the Reference

**Dana Young** (`toolkit/profiles/dana-young.md`):
- Philosophy: world as puzzle (Riven), visual material not illustration, answer names the experience, range as fidelity
- Lens zones: visual grammar / image precision / theme in the corners / layout direction / visual resolution (expertise) → over-scaffolded flavor text / extraction earning its step / honest difficulty / arbitrary vs inevitable answers (failure modes) → meta earned by feeders / puzzle that doesn't belong in the set (cut decisions)

**Kenny Young** (`toolkit/profiles/kenny-young.md`):
- Philosophy: rules not content, interacting constraints, rule IS the subject matter, answers as revealed truths
- Lens zones: constraint force distribution / emergent interactions / necessity test / weakest forcing chain / extraction coupling / interface transparency (expertise) → logical vs obscure difficulty / dead ends / uniqueness gaps / structural gaps in middle (failure modes) → theme as costume not mechanic / would he build this (cut decisions)

---

## Notes

- Do not invent puzzle credits. Only use what's in the evidence files or confirmed sources.
- Do not name specific puzzles in the philosophy or lens sections.
- For game designers (Blow, Pope, Miller, Weisman) and academics (Winkler, Nicholson): their expertise is documented in talks, essays, and published works. Use those instead of puzzle credits.
- The Credentials section is never rewritten by this skill — only Design Philosophy and Review Lens change (plus What Makes Them Exceptional if it's weak).
- Every profile should feel like a different person. If two profiles sound similar in philosophy or lens, one of them is wrong.
