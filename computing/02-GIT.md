# Git — Modern Version Control Workflows

## The Big Picture

Git is a **distributed version control system**. Every clone is a full copy of history. There is no "server" from Git's perspective — the server is just another clone that everyone agrees to treat as canonical.

```
                     GIT MENTAL MODEL

  REMOTE (GitHub / Azure DevOps / GitLab):
  +----------------------------------------------------------+
  | origin/main      origin/feat-auth    origin/feat-ui      |
  +----------------------------------------------------------+
        ↑ ↓  push / pull

  LOCAL CLONE (your machine):
  +----------------------------------------------------------+
  |  main         feat-auth       feat-ui                    |
  |                                                          |
  |  WORKING      STAGING         COMMIT                     |
  |  TREE    -->  AREA (index) --> HISTORY (.git/)           |
  +----------------------------------------------------------+

  Each developer has their own full LOCAL copy of history.
  "origin" is a named pointer to the shared remote.
```

**Key insight vs Source Depot / TFS**: There is no check-out lock. Multiple people can edit the same file simultaneously. Merging is the norm, not the exception. The repository lives entirely on your machine — you don't need the server to commit, branch, or view history.

### Source Depot → Git: The Inversion of Ownership

If you came from Source Depot (SD), this is the single most important mental model shift:

```
  SOURCE DEPOT MENTAL MODEL           GIT MENTAL MODEL
  ========================            ================

  Server holds the depot.             Every clone IS the depot.

  +-------------------+               +-------------------+
  |   SD SERVER       |               |   origin (GitHub) |
  |   (the truth)     |               |   (just a clone   |
  |   Full history    |               |    everyone agrees|
  |   All branches    |               |    is canonical)  |
  +-------------------+               +-------------------+
           |                                   |
           | enlistment:                       | git clone:
           | "map these depot                  | "give me the ENTIRE
           |  paths to my local                |  repository — all history,
           |  workspace"                        |  all branches, all objects"
           v                                   v
  +-------------------+               +-------------------+
  |   LOCAL MACHINE   |               |   LOCAL MACHINE   |
  |   Only files in   |               |   .git/ = full    |
  |   your client     |               |   object store    |
  |   spec mappings   |               |   (the whole repo)|
  |   (a view)        |               |   working tree =  |
  +-------------------+               |   checked-out     |
                                      |   snapshot        |
                                      +-------------------+

  SD: "I have a view into the server"
  Git: "I have the server — origin is just a named remote I sync with"
```

**Concrete consequence**: In SD, `sd sync` goes to the server and pulls down changes. In Git, `git fetch` downloads objects to your local `.git/` store — the server is not involved in any subsequent operation. You can commit, branch, merge, and view full history entirely offline. `git fetch` is the SD `sd sync` equivalent, but `git merge` (or `git rebase`) is a separate step that you do locally against the already-downloaded objects.

```
  SD workflow:       sd sync          (get + integrate in one step)
  Git equivalent:    git fetch        (download remote objects)
                   + git merge        (integrate into your working branch)
  Or combined:       git pull         (fetch + merge — the sd sync analog)
```

The three-tree model (working tree / index / HEAD) is described in the next section. The key SD translation: your client workspace maps to the working tree; SD shelvesets map to `git stash`; a changeset maps to a commit (but commits are snapshots, not diffs — see Core Concepts).

---

## The Three Trees

Before any command makes sense, you need this mental model. Git manages three distinct areas:

```
  WORKING TREE          STAGING AREA            COMMIT HISTORY
  (your files)          (the index)             (.git/objects)
  ------------          -----------             --------------
  What you see          What's been             Permanent
  in your editor.       marked for the          snapshots.
                        next commit.            SHA-addressed.

  git add -->           git commit -->

  Untracked files       Staged changes          Committed changes
  Modified files        (diff vs last           (diff vs parent)
  Deleted files          commit)

  git diff              git diff --staged       git log
  (working vs staged)   (staged vs HEAD)        (history)
```

This three-tree model explains 80% of confusing Git behavior. When `git status` shows something, it tells you which tree it's in.

---

## Core Concepts

### Commits Are Snapshots, Not Diffs

```
  Source Depot / TFS mindset:          Git reality:
  +----------------------------+        +-----------------------------+
  | Changeset = set of diffs   |        | Commit = full snapshot      |
  | against previous version   |        | of ALL tracked files        |
  | File A: lines 3-7 changed  |        | SHA: a3f1c9d...             |
  | File B: added lines 11-14  |        | Parent: 82be4a1...          |
  +----------------------------+        | Tree: [all files @ this pt] |
                                        +-----------------------------+

  Git stores snapshots. Diffs are computed on-demand from comparing
  two snapshots. This is why git log -p works and why blame is fast.
```

### The SHA — Your Content Address

Every object in Git (commit, tree, blob) gets a **SHA-1 hash** of its contents. This means:

- Same content = same SHA (deduplication is free)
- Any corruption is immediately detectable
- You can reference any point in history by its SHA
- Short SHAs work as long as they're unambiguous: `git show a3f1c9d`

### HEAD — Where You Are

```
  HEAD is a pointer. It usually points to a branch, which points to a commit.

  main -------> a3f1c9d  <--- HEAD
    |
    v
  You're on main. Commits go here.

  After: git checkout feat-auth

  main -------> a3f1c9d
  feat-auth --> 82be4a1  <--- HEAD

  After: git checkout a3f1c9d  (detached HEAD)

  main -------> a3f1c9d  <--- HEAD (directly)
  feat-auth --> 82be4a1

  Detached HEAD = you're looking at a commit, not a branch.
  New commits here go nowhere (no branch tracks them) unless you create one.
```

---

## Branching

Branches in Git are **cheap** — they are just a 41-byte file containing a SHA. Creating a branch is instantaneous regardless of repo size.

```
                    +--[E]--[F]  feat-auth
                   /
  [A]--[B]--[C]--[D]  main
                   \
                    +--[G]--[H]  feat-ui

  Create branch:  git checkout -b feat-auth     (create + switch)
                  git branch feat-auth           (create only)
                  git switch -c feat-auth        (modern syntax)

  Switch branch:  git checkout main
                  git switch main                (modern syntax)

  Delete branch:  git branch -d feat-auth       (safe: merged only)
                  git branch -D feat-auth       (force: unmerged ok)
```

### Branch Naming Conventions

```
  Common patterns:
  main / master          The production-ready trunk
  develop / dev          Integration branch (some workflows)
  feature/<name>         feat/add-user-auth
  fix/<name>             fix/login-null-crash
  release/<version>      release/2.3.0
  hotfix/<name>          hotfix/critical-security-patch
  chore/<name>           chore/update-dependencies

  Short-lived branches are the goal. Weeks, not months.
```

---

## The Everyday Workflow

### Stage → Commit

```
  1. Edit files in working tree

  2. Stage what you want in this commit:
     git add src/auth.js          # stage specific file
     git add src/                 # stage entire directory
     git add -p                   # interactive: choose hunks
     git add .                    # stage everything (careful)

  3. Review what's staged:
     git status                   # overview
     git diff --staged            # exact diff of staged changes

  4. Commit:
     git commit -m "Add JWT validation to auth middleware"

  5. Repeat — small, atomic commits are better than one giant one.
```

### Good Commit Messages

```
  Format:
  <subject line, imperative, ≤72 chars>

  <body: why, not what — the code shows what>

  <footer: issue refs, breaking change notices>

  Example:
  Add JWT expiry validation to auth middleware

  Without this check, expired tokens were still accepted because the
  middleware only validated signature, not the exp claim. This caused
  sessions to persist indefinitely after logout.

  Closes #342

  Subject line rules:
  - Imperative mood: "Add" not "Added" or "Adding"
  - No period at end
  - ≤72 chars
  - Complete the sentence: "This commit will... [subject]"
```

---

## Remote Operations

```
  REMOTE VOCABULARY

  origin           Default name for the remote you cloned from.
                   Just a name — "origin" has no special meaning to git.

  upstream         Convention for the original repo when you have a fork.
                   You cloned YOUR fork (origin), the source is upstream.

  tracking branch  A local branch configured to follow a remote branch.
                   git branch -u origin/main  (sets tracking)
                   git status shows ahead/behind counts.
```

```
  FETCH vs PULL

  git fetch origin          Downloads all remote changes.
                            Does NOT touch your working tree.
                            Safe to run anytime.
                              |
                              v
                            origin/main advances in your local repo.
                            Your local main is unchanged.

  git pull                  fetch + merge (or rebase) in one step.
                            Modifies your current branch.
                            = git fetch && git merge origin/main

  git pull --rebase         fetch + rebase.
                            Keeps history linear. Preferred by many teams.
```

```
  PUSH

  git push                  Push current branch to its tracking remote.
  git push origin main      Explicit: push local main to origin/main.
  git push -u origin feat   Push + set tracking branch (first push).
  git push --force-with-lease  Safer force push — fails if remote has
                               commits you haven't seen. Use instead
                               of --force when rewriting history.
```

---

## Merging vs Rebasing

This is the most debated topic in Git workflows. Understand both.

### Merge

```
  Before:
  [A]--[B]--[C]  main
              \
               [D]--[E]  feat-auth

  git checkout main
  git merge feat-auth

  After:
  [A]--[B]--[C]--------[F]  main   (F = merge commit)
              \        /
               [D]--[E]  feat-auth

  + Preserves exact history of what happened and when.
  + Non-destructive — no commits are rewritten.
  - Creates a merge commit. History graph is a DAG, not linear.
  - git log looks "busy" on active repos.
```

### Rebase

```
  Before:
  [A]--[B]--[C]  main
              \
               [D]--[E]  feat-auth

  git checkout feat-auth
  git rebase main

  After:
  [A]--[B]--[C]  main
              \
               [D']--[E']  feat-auth
               (new SHAs — commits were rewritten)

  Then:
  git checkout main
  git merge feat-auth   (fast-forward — no merge commit needed)

  [A]--[B]--[C]--[D']--[E']  main

  + Linear history. Clean git log.
  + Each commit still logically represents one thing.
  - Rewrites history. NEVER rebase commits already pushed to shared branches.
  - Can be complex to resolve conflicts (one per commit vs one total).
```

### The Golden Rule of Rebase

```
  +-----------------------------------------------+
  |  NEVER rebase commits that exist on a         |
  |  remote branch others have pulled from.       |
  |                                               |
  |  Rebase = rewrite history = new SHAs.         |
  |  Others' local branches still point to        |
  |  the OLD SHAs. Chaos follows.                 |
  |                                               |
  |  Safe: rebase your LOCAL feature branch       |
  |        before opening a PR.                   |
  |  Safe: rebase interactively to clean up       |
  |        your own unpushed commits.             |
  +-----------------------------------------------+
```

### Squash Merge

```
  A middle path: take all commits from a branch, squash to ONE,
  merge that onto main.

  git merge --squash feat-auth
  git commit -m "Add auth feature (#123)"

  Result: Linear main. No merge commit. One commit per feature.
  Trade-off: You lose granular history of the feature branch.

  GitHub/Azure DevOps PR merge options:
  +-----------------+-----------------------------------+
  | Merge commit    | Preserves all commits + adds merge|
  | Squash merge    | Squashes all to one commit        |
  | Rebase merge    | Replays commits linearly, no merge|
  +-----------------+-----------------------------------+
```

---

## Undoing Things

```
  UNDO SCENARIOS

  +---------------------------------+------------------------------------+
  | Situation                       | Command                            |
  +---------------------------------+------------------------------------+
  | Unstage a file (keep changes)   | git restore --staged file.txt      |
  |                                 | (old: git reset HEAD file.txt)     |
  +---------------------------------+------------------------------------+
  | Discard working tree changes    | git restore file.txt               |
  | (DESTRUCTIVE — no undo)         | (old: git checkout -- file.txt)    |
  +---------------------------------+------------------------------------+
  | Amend the last commit message   | git commit --amend                 |
  | (ONLY if not yet pushed)        |                                    |
  +---------------------------------+------------------------------------+
  | Undo last commit, keep changes  | git reset --soft HEAD~1            |
  | staged (not yet pushed)         | (moves HEAD back 1, keeps index)   |
  +---------------------------------+------------------------------------+
  | Undo last commit, unstage too   | git reset --mixed HEAD~1           |
  | (default reset behavior)        | (moves HEAD back 1, clears index)  |
  +---------------------------------+------------------------------------+
  | Undo commit, discard changes    | git reset --hard HEAD~1            |
  | (DESTRUCTIVE — loses work)      |                                    |
  +---------------------------------+------------------------------------+
  | Undo a commit safely (already   | git revert <sha>                   |
  | pushed / shared)                | Creates a NEW commit that undoes it|
  +---------------------------------+------------------------------------+
```

**Key distinction**: `reset` rewrites history (dangerous if pushed). `revert` adds a new commit (always safe).

---

## Stashing

Stash is a temporary shelf for uncommitted changes when you need to switch context.

```
  You're mid-feature. Urgent fix needed on main.

  git stash                   Save working tree + index to stash stack.
  git stash push -m "wip auth validation"   Named stash.

  git switch main
  # ... do the urgent fix ...
  git switch feat-auth

  git stash pop               Apply most recent stash, remove from stack.
  git stash apply             Apply but KEEP on stack.
  git stash list              See all stashes.
  git stash drop stash@{0}    Delete a specific stash.
  git stash clear             Delete all stashes.

  Stashes are LOCAL. They don't push to remote.
```

---

## Working with History

```
  INSPECT

  git log                     Full history.
  git log --oneline           Compact: SHA + subject per line.
  git log --oneline --graph   ASCII branch graph.
  git log --oneline -20       Last 20 commits.
  git log src/auth.js         History for one file.
  git log main..feat          Commits in feat not in main.

  git show <sha>              Full diff + metadata for one commit.
  git show HEAD~3             Three commits back from HEAD.

  git diff main..feat         All changes between two branches.
  git diff HEAD~1 HEAD        Diff last commit vs the one before.

  BLAME

  git blame src/auth.js       Line-by-line last-touched-by info.
  git blame -L 40,60 file.js  Lines 40-60 only.

  SEARCH

  git log -S "functionName"   Find commits that added/removed a string.
  git log --grep "JWT"        Find commits with "JWT" in message.
  git grep "TODO"             grep across all tracked files.
```

### Reflog — Your Safety Net

```
  git reflog

  Shows every place HEAD has been — including after resets.
  Commits aren't truly gone until garbage collected (~30 days).

  Example recovery:
  git reset --hard HEAD~3     (oops, lost 3 commits)
  git reflog                  (find the SHA of where you were)
  git reset --hard a3f1c9d    (restore to that point)
```

---

## Branching Workflows

### GitHub Flow (simple, modern standard)

```
  main is always deployable.

  main
  |
  +--- feature branch
  |         |
  |    (commits)
  |         |
  |    pull request
  |         |
  |    code review
  |         |
  |    merge to main
  |         |
  +<--------+
  |
  deploy

  Rules:
  1. Branch from main.
  2. Open a PR early (even draft) for visibility.
  3. Review + CI must pass before merge.
  4. Merge to main = ready to deploy.
  5. Delete branch after merge.
```

### Git Flow (release-oriented)

```
  main          Production releases only. Tagged.
  develop       Integration. Next release accumulates here.
  feature/*     Branch from develop, merge back to develop.
  release/*     Branch from develop when ready, merge to main + develop.
  hotfix/*      Branch from main, merge to main + develop.

  Used when:
  - You have scheduled releases (not continuous deployment)
  - Multiple versions in production simultaneously
  - Mobile apps, libraries with versioned releases
```

### Trunk-Based Development

```
  Everyone commits to main (or merges very short-lived branches frequently).
  Feature flags hide incomplete work.

  Used by: Google, Facebook, high-velocity teams.
  Requires: strong CI, feature flags, team discipline.
```

---

## Remotes and Forks

```
  FORK WORKFLOW (open source / cross-team)

  +---------------------+         +----------------------+
  |  upstream (original)|         |  origin (your fork)  |
  |  github.com/org/repo|         |  github.com/you/repo |
  +---------------------+         +----------------------+
            |                               |
            |  fork (GitHub UI)             |  clone
            +-----------------------------> |
                                            v
                                   +----------------+
                                   |  LOCAL CLONE   |
                                   |  origin = fork |
                                   |  upstream = org|
                                   +----------------+

  git remote add upstream https://github.com/org/repo.git

  Sync with upstream:
  git fetch upstream
  git rebase upstream/main    (or: git merge upstream/main)
  git push origin main        (update your fork)
```

---

## Pull Requests

A pull request (PR) is NOT a Git concept — it's a **platform feature** (GitHub, Azure DevOps, GitLab). Git just has branches. PRs are the collaboration layer on top.

```
  PR LIFECYCLE

  1. Push feature branch to remote.
  2. Open PR: base=main, compare=feat-auth.
  3. CI runs automatically (GitHub Actions, Azure Pipelines).
  4. Reviewers comment on specific lines.
  5. Author addresses feedback (more commits or discussion).
  6. Required approvals met + CI green.
  7. Merge (squash / merge commit / rebase — team decides).
  8. Branch auto-deleted (configure in repo settings).
  9. Deploy triggered (if CD is set up).

  Azure DevOps calls these "Pull Requests" too — same concept,
  different UI. Branch policies enforce review requirements.
```

### Azure DevOps Branch Policies → GitHub Branch Protection Rules

You built branch policies in VSTS/ADO. GitHub calls them "branch protection rules" and configures them in repo **Settings → Branches → Add rule** rather than in the pipeline. The concepts map directly:

| ADO Branch Policy | GitHub Branch Protection Rule | Notes |
|---|---|---|
| Build validation | Required status checks | CI job must pass before merge. GitHub checks come from Actions workflow jobs; name the job in the required checks list. |
| Minimum number of reviewers | Required number of approving reviews | Same enforcement; GitHub adds CODEOWNERS for automatic reviewer assignment. |
| Require a merge strategy (squash / rebase / merge) | Require linear history / Allow squash merging | Configured both in protection rules and in repo Settings → General → Pull Requests. |
| Require comment resolution | Require conversation resolution before merging | Direct equivalent; same intent. |
| Work item linking | Not built-in | GitHub has issue references in commit messages (`Closes #123`), but no mandatory work-item gating like ADO. |
| Require up-to-date branches | Require branches to be up to date before merging | GitHub equivalent: "Require branches to be up to date." Prevents merge if base branch advanced. |
| Bypass policies (admins) | "Do not allow bypassing the above settings" | GitHub lets you explicitly exclude admins from bypass — ADO uses the same policy exception model. |

**CI trigger wiring** — the ADO YAML pipeline's `trigger` and `pr` blocks map to GitHub Actions `on:` events:

```yaml
  ADO pipeline (azure-pipelines.yml):     GitHub Actions (.github/workflows/ci.yml):

  trigger:                                 on:
    branches:                               push:
      include: [main]                         branches: [main]
  pr:                                       pull_request:
    branches:                                 branches: [main]
      include: [main]

  # ADO: pool + steps                      jobs:
  pool:                                      build:
    vmImage: ubuntu-latest                     runs-on: ubuntu-latest
  steps:                                       steps:
    - script: npm test                           - run: npm test
```

The required status check name in the GitHub protection rule must match the **job name** in the workflow file (e.g., `build`). This is the equivalent of ADO's "select build pipeline" in the Build validation policy.

---

## Configuration and Setup

```
  FIRST-TIME SETUP

  git config --global user.name  "Your Name"
  git config --global user.email "you@company.com"
  git config --global init.defaultBranch main
  git config --global core.autocrlf true    # Windows: CRLF on checkout
  git config --global pull.rebase true      # pull --rebase by default

  USEFUL ALIASES

  git config --global alias.lg \
    "log --oneline --graph --decorate --all"

  git config --global alias.st  "status -sb"
  git config --global alias.co  "checkout"
  git config --global alias.br  "branch"

  CONFIG HIERARCHY

  System  /etc/gitconfig           All users on machine.
  Global  ~/.gitconfig             Your user. --global flag.
  Local   .git/config              This repo only. Default target.
  Worktree .git/config.worktree    Individual worktree (rare).

  More specific wins. Local overrides global overrides system.
```

### .gitignore

```
  Tell git which files to never track.

  # .gitignore
  node_modules/         # dependency directories
  .env                  # secrets — NEVER commit
  .env.local
  dist/                 # build output
  *.log                 # log files
  .DS_Store             # macOS metadata
  *.user                # VS user-specific files (familiar from .NET)
  bin/
  obj/

  Patterns:
    /build        only root-level build/
    build/        any build/ anywhere
    *.log         any file ending in .log
    !important.log  exception: track this one

  .gitignore is committed. It applies to everyone.
  .git/info/exclude is local-only (same syntax, not committed).
  Global ignore: git config --global core.excludesfile ~/.gitignore_global
```

---

## Tags

Tags mark specific commits — typically release points.

```
  LIGHTWEIGHT vs ANNOTATED

  git tag v2.3.0                  Lightweight: just a named pointer.
  git tag -a v2.3.0 -m "Release"  Annotated: stores tagger, date, message.

  Use annotated for releases. Lightweight for temporary bookmarks.

  git push origin v2.3.0          Tags don't push by default.
  git push origin --tags          Push all tags.

  git tag                         List all tags.
  git show v2.3.0                 See tag details.
  git checkout v2.3.0             Detached HEAD at that tag.
```

---

## Worktrees

Multiple working trees from one repository. Useful when you need to work on two branches simultaneously without stashing/switching.

```
  C:\src\craftworks\          (main repo, on main branch)
  C:\src\craftworks-feat-x\   (worktree, on feat-x branch)
  C:\src\craftworks-hotfix\   (worktree, on hotfix branch)

  git worktree add ../craftworks-feat-x -b feature/new-ui
  git worktree add ../craftworks-hotfix hotfix/critical-fix

  git worktree list
  git worktree remove ../craftworks-feat-x

  All worktrees share the same .git — one history, multiple checkouts.
  You cannot have the same branch checked out in two worktrees.
```

---

## Common Confusion Points

### "git pull says I'm diverged"

```
  Your local main and origin/main both have commits the other doesn't.

  Happens when:
  - You committed locally without pushing.
  - Someone else pushed while you were working.

  Options:
  git pull --rebase         Replay your commits on top of theirs. Linear.
  git pull --merge          Create a merge commit. Preserves both timelines.
  git pull --ff-only        Fail if not fast-forward. Forces you to decide.

  Set a default:
  git config --global pull.rebase true   (or false, or ff-only)
```

### "I committed to main instead of my feature branch"

```
  git branch feat-auth          Create branch at current position.
  git reset --soft HEAD~1       Move main back 1 commit (keep changes staged).
  git switch feat-auth          Switch to the new branch.
  git commit                    The commit is now on feat-auth.

  Or simpler if you haven't pushed:
  git branch feat-auth          Create branch WHERE YOU ARE.
  git reset --hard origin/main  Reset main to where remote is.
  git switch feat-auth          Your changes are now on feat-auth.
```

### "HEAD is detached"

```
  You checked out a commit SHA or a tag directly.

  git status shows: HEAD detached at a3f1c9d

  If you want to keep changes made here:
  git switch -c new-branch-name    Create a branch to save your work.

  If you just want to go back:
  git switch main
```

### "git rebase vs git merge — just tell me what to use"

```
  For feature branches before PR:     git rebase main
    -> Clean, linear history for reviewers.
    -> Your branch replays on top of latest main.

  For integrating after PR approval:  Let the platform do it.
    -> GitHub/Azure DevOps handles the merge strategy.
    -> Configure "squash merge" for clean main history.

  For long-lived integration branch:  git merge
    -> Preserves the real history of what happened.
    -> Merge commits show integration points.

  Never rebase shared/remote branches.
```

### "What's origin/main vs main?"

```
  main              Your LOCAL branch. Moves when you commit.
  origin/main       A LOCAL reference to the last known state of
                    the remote branch. Updated by fetch/pull.

  They can diverge. git status shows you by how much.
  "Your branch is ahead of origin/main by 2 commits."
  = You have 2 local commits not yet pushed.
```

---

## Old World → New World Bridge

| Source Depot / TFS concept | Git equivalent | Notes |
|----------------------------|----------------|-------|
| Check out (exclusive lock) | `git add` | No locks. Anyone can edit. |
| Changeset | Commit | Git commit = snapshot; changeset = diff |
| Shelve / shelveset | `git stash` or draft PR | Stash is local; draft PR is shared |
| Label / tag | `git tag` | Annotated tags for releases |
| Branch (expensive copy) | `git branch` (41 bytes) | Instant, weightless |
| Get latest | `git pull` | Also pulls all remote branch info |
| Sync | `git fetch` + `git merge` | Fetch = download; merge = integrate |
| History / timeline | `git log` | Full DAG, not just linear |
| Visual Studio SCM | VS Code Source Control pane, GitHub Desktop, GitLens | Same concepts, modern UX |
| VSTS/ADO Repos | GitHub / Azure DevOps Git Repos | ADO supports Git natively now |
| Build pipeline trigger | PR CI check (GitHub Actions / Azure Pipelines) | Auto-triggers on push/PR |
| ADO branch policy: build validation | GitHub: required status check | CI must pass before merge allowed |
| ADO branch policy: min reviewers | GitHub: required approving reviews | Configured in branch protection rules |
| ADO branch policy: merge strategy | GitHub: require linear history / squash | Same intent, repo Settings → Branches |

### git bisect — Binary Search Over Commit History

`git bisect` finds the exact commit that introduced a bug by performing a binary search over the commit graph. You tell it one "good" commit (bug absent) and one "bad" commit (bug present). It checks out the midpoint, you test, tell it good/bad, and it halves the search space. O(log n) steps to find the culprit in a history of n commits.

```
  Scenario: Bug exists in HEAD. It didn't exist at v2.0.0 (200 commits ago).
  Manual inspection: 200 commits to check. git bisect: ~8 steps (log₂ 200 ≈ 7.6).

  git bisect start          Begin the bisect session.
  git bisect bad            Mark the current commit (HEAD) as bad.
  git bisect good v2.0.0    Mark v2.0.0 as the last known-good commit.

  Git checks out commit at the midpoint (~100 commits ago).
  You test: does the bug exist?

  git bisect good           If bug is absent — search the upper half.
  git bisect bad            If bug is present — search the lower half.

  Git checks out the next midpoint. Repeat.
  After ~8 rounds, Git prints:
  "a3f1c9d is the first bad commit"

  Binary search over the commit DAG:
  [v2.0.0 ... good ... good ... BISECT HERE ... bad ... bad ... HEAD]
                                     ^
                                Git checks out here first (~midpoint).
                                Each answer cuts remaining range in half.
```

**Automating bisect** — if you have a script that exits 0 for good and non-zero for bad, Git runs the whole thing automatically:

```bash
  git bisect start
  git bisect bad HEAD
  git bisect good v2.0.0
  git bisect run npm test   # runs npm test at each midpoint
                            # exits 0 = good, non-zero = bad
  # Git announces the first bad commit and exits.
```

When done: `git bisect reset` — restores your working tree to HEAD and ends the session.

**When to reach for it**: any regression where you know a commit range. "This worked in the last release, it's broken now" is exactly this scenario.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Start a new feature | `git switch -c feature/my-feature` |
| Save my work temporarily | `git stash push -m "description"` |
| Get latest from remote (safe) | `git fetch origin` |
| Get latest + integrate | `git pull --rebase` |
| Share my branch | `git push -u origin feature/my-feature` |
| Clean up commits before PR | `git rebase -i main` |
| Undo last commit (not pushed) | `git reset --soft HEAD~1` |
| Undo a commit already pushed | `git revert <sha>` |
| Find who wrote a line | `git blame <file>` |
| Find when a bug was introduced | `git bisect` |
| Work on two branches at once | `git worktree add` |
| See compact branch graph | `git log --oneline --graph --all` |
| Recover something I reset | `git reflog` |
| Tag a release | `git tag -a v1.2.0 -m "Release 1.2.0"` |
