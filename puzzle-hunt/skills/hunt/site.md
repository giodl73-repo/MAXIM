# /hunt site — Hunt Website

Scaffolds and manages the hunt's delivery website. Static HTML/CSS/JS — deployable to GitHub Pages, Netlify, or any static host. No backend required. Answer submission via configurable form service.

## Usage

```
/hunt site init               — scaffold the full site structure
/hunt site theme              — set up visual theme (colors, fonts, logo)
/hunt site puzzle <id>        — generate HTML page for one puzzle
/hunt site puzzles all        — generate all puzzle pages
/hunt site standings          — generate/update standings page
/hunt site submit             — set up answer submission system
/hunt site unlock             — configure puzzle unlocking (linear, parallel, etc.)
/hunt site deploy             — deployment checklist + instructions
/hunt site test               — pre-launch test checklist
```

---

## Site Structure

All site files in `delivery/site/`:

```
delivery/site/
├── index.html              ← hunt home / splash page
├── puzzles.html            ← puzzle list (locked/unlocked per team)
├── standings.html          ← live leaderboard
├── submit.html             ← answer submission (or per-puzzle submit pages)
├── hints.html              ← hint request form
├── puzzles/
│   ├── P01-[name].html
│   ├── P02-[name].html
│   └── ...
├── assets/
│   ├── logo.[svg|png]
│   ├── theme.css           ← all site styling
│   ├── hunt.js             ← standings, unlock logic
│   └── images/
├── data/
│   ├── puzzles.json        ← puzzle metadata (title, round, unlock condition, answer hash)
│   ├── teams.json          ← team registry
│   └── standings.json      ← current standings (updated by admin during hunt)
└── admin/
    ├── admin.html          ← hunt control panel (password-protected)
    └── admin.js
```

---

## /hunt site init

Creates the full directory structure and base files. Asks:

1. Hunt name and tagline
2. Site URL (e.g., `https://teamname.github.io/hunt2025`)
3. Number of teams
4. Puzzle unlock model: **linear** (solve to unlock next) / **parallel** (all open) / **round-gated** (unlock round-by-round) / **custom**
5. Answer submission: **Netlify Forms** / **Google Forms** / **self-hosted** / **email**
6. Standings: **live JSON** (admin updates a file) / **Google Sheets embed** / **static** (no live standings)

Generates all base files with the hunt's theme applied.

---

## Puzzle Pages

Each puzzle page (`puzzles/P01-name.html`) contains:

```html
<!-- Structure -->
[Hunt header + nav]
[Round badge]
[Puzzle title + flavor text]
[Puzzle content — imported from puzzle.md or embedded]
[Answer submission form / link]
[Hint request button]
[Footer]
```

**Unlock states:**
- **Locked:** shows title + "Not yet unlocked" — no content visible
- **Unlocked:** full puzzle content
- **Solved:** shows answer word + congratulations flavor text

Unlock state is driven by `data/puzzles.json` — the admin updates this file during the hunt to unlock puzzles for teams.

---

## Standings Page

The standings page reads `data/standings.json` and renders a live leaderboard.

```json
{
  "updated": "2025-06-14T15:30:00",
  "teams": [
    {
      "name": "Team Rocket",
      "solved": ["P01", "P02", "P05"],
      "hints_used": 2,
      "last_solve": "2025-06-14T15:22:00"
    }
  ]
}
```

The admin updates `standings.json` during the hunt (manually, or via the admin panel). The page auto-refreshes every 60 seconds.

Standings display:
```
IRONFALL SPEEDRUN STANDINGS
Last updated: 3:30 PM

Rank  Team              Solved   Hints   Last solve
────  ────              ──────   ─────   ──────────
  1   Team Rocket       3/10     2       3:22 PM
  2   The Archivists    3/10     0       3:28 PM
  3   Pixel Hunters     2/10     1       3:15 PM
  ...
```

---

## Answer Submission

### Netlify Forms (recommended for static sites)
- Form embedded on each puzzle page
- Submissions appear in Netlify dashboard
- Admin reviews and marks correct/incorrect manually
- Free tier: 100 submissions/month (enough for most hunts)

### Google Forms
- One form per puzzle, or one master form with puzzle ID field
- Responses in Google Sheets — admin monitors during hunt
- Simple to set up, no deployment complexity

### Self-hosted
- Requires a small backend (Node/Python)
- Most control — real-time answer checking, automatic unlock on correct answer
- Recommended only if the team has a developer available

`/hunt site submit` walks through the chosen option and generates the form HTML + configuration.

---

## Admin Panel

`delivery/site/admin/admin.html` — password-protected hunt control panel.

Features:
- View all team progress
- Manually unlock puzzles for specific teams
- Update standings.json
- Send hint responses (if using hint system)
- Monitor answer submissions
- Emergency: unlock all puzzles (if a team is stuck blocking the hunt)

Password: set in `admin/admin.js` (change before deploy — it's client-side, security is light). For sensitive hunts, use HTTP Basic Auth at the hosting level.

---

## /hunt site theme

Sets the visual design language for the site. Writes to `assets/theme.css` and `delivery/THEME.md`.

Asks:
1. Primary color (background or dominant color)
2. Accent color (buttons, links, highlights)
3. Font family (Google Fonts or system fonts)
4. Aesthetic descriptor (e.g., "pixel art retro", "clean minimal", "dark academia")
5. Logo/wordmark (upload or describe for Claude to generate SVG placeholder)

For fictional-world hunts: the site should feel like it exists within the fiction. For IRONFALL, the site would look like the 1993 fan wiki — late-90s web aesthetic, pixel fonts, countdown timer to server shutdown, scan-line overlay.

---

## /hunt site deploy

Deployment checklist and instructions for common hosts.

### GitHub Pages
```bash
# From delivery/site/
git init
git add .
git commit -m "Hunt site"
git remote add origin https://github.com/[user]/[hunt-name]-site
git push -u origin main
# Enable Pages in repo settings → Source: main branch
```

### Netlify (drag-and-drop)
1. Go to netlify.com → "Add new site" → "Deploy manually"
2. Drag `delivery/site/` folder onto the deploy area
3. Site is live at a random URL — set custom domain if needed
4. Netlify Forms work automatically

### Local (for in-person hunts on a local network)
```bash
cd delivery/site/
python -m http.server 8080
# All devices on local WiFi → http://[your-ip]:8080
```

---

## /hunt site test

Pre-launch checklist:

```
SITE TEST CHECKLIST

Navigation
  [ ] Home page loads correctly
  [ ] All puzzle pages load (N pages)
  [ ] Standings page loads and renders
  [ ] Answer submission form works (test with dummy answer)
  [ ] Hint request form works

Unlock logic
  [ ] Locked puzzles show "not yet unlocked" — no content visible
  [ ] Unlocking a puzzle in puzzles.json reflects on site
  [ ] Solved state shows correct flavor text

Mobile
  [ ] Site readable on phone (test at 375px width)
  [ ] Answer submission works on mobile

Admin
  [ ] Admin panel accessible
  [ ] Can update standings.json and see change on standings page
  [ ] Can unlock a puzzle for a specific team

Content
  [ ] All puzzle titles correct
  [ ] No placeholder text remaining
  [ ] All QR codes (on print pages) point to correct URLs
  [ ] All images load
```
