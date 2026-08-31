# Beyond Limits Academics — website

A website design for **Beyond Limits Academics**, the tutoring program of the
Stamford Peace Youth Foundation (Stamford, CT).

Static HTML. No framework, no build system, no dependencies, no external requests.
Every page is self-contained: CSS in a `<style>` block, small vanilla JS inline,
images as relative filenames in this folder.

**Status: work in progress.** Several things are intentionally unfinished. Read
"Known gaps" below before assuming any part of this is final.

---

## Run it

No server needed. Open `index.html` from disk and the whole site works offline.

To serve it instead:

```bash
python -m http.server 8777
```

Then visit <http://localhost:8777>.

---

## Pages

| File | Page |
|------|------|
| `index.html` | Home |
| `beyond-limits.html` | Beyond Limits hub |
| `tutoring.html` | Tutoring |
| `sponsorship.html` | Sponsorship |
| `donate.html` | Donate |
| `about.html` | About |
| `start.html` | "What brings you here?" router |

---

## `build-site.py` — the export step

Pages are authored in **Claude Design** and exported here. This script is what turns
an export into a shippable page. It does two jobs:

1. **Strips design-system scaffolding** that must never reach the client (a
   "Canonical rendered reference" banner, internal `@dsCard` comments).
2. **Wires the onboarding assistant** into the pages: six entry points, plus the
   nav "Get Involved" pointing at the router.

The wiring lives here rather than in the design sources so it is declarative,
reviewable in one place, and **cannot be silently lost on a re-export**.

Run it after any export:

```bash
python build-site.py
```

It is idempotent and self-verifying. It prints what it stripped, what it wired,
whether any internal marker leaked, and the assistant entry-point count. A count
other than 6 means something regressed.

---

## The one rule that matters

> **export → commit → deploy**

**Commit before every export.** Claude Design has no version history. If you export
over a content edit made here, the only way to see what was lost is `git diff`
against the commit you made first. Skip the commit and the change is simply gone.

This is not theoretical. It has already cost a session's work once.

Broadly: Claude Design is where **design** changes happen. This repo is canonical for
**the published site and content edits**.

---

## Known gaps

Deliberate, not bugs. Anyone reviewing should know these up front.

- **Three CTAs are inert.** "Tell us about your student" on Tutoring and Donate, and
  "Tell us about your business" on Sponsorship, are `href="#"`. They previously
  pointed at an internal placeholder that rendered a browser error.
- **The onboarding assistant has no backend.** It is a separate static site at
  <https://vastlyresilient.github.io/beyond-limits-enrollment/>. Where a completed
  enrollment goes is untested. A parent could finish all ten steps and nothing may
  reach anyone.
- **44 gold "confirm" markers** across the pages are intentional. Where the source
  material was unclear or a figure was still being verified, the page carries a
  marker rather than a guess. **Do not quietly resolve them.** A marker on settled
  data is exactly as wrong as a missing marker on contested data. They come off as
  each figure is confirmed.
- **Fee wording is still being finalised.** The enrollment assistant and these pages
  describe cost differently. Pending confirmation.
- **The Español toggle is `href="#"`** everywhere. Spanish scope is undecided.
- **Basketball and Our Impact link out** to the client's existing site in a new tab.
  Those sections are out of scope, so the visual jump is expected.
- **No custom domain yet.** `robots.txt` disallows all crawlers while this is a work
  in progress, so it will not show up in search results. Remove that file when the
  design is final and live.

---

## Not in this repo, on purpose

Working notes, research files and correspondence live outside this folder and are
deliberately excluded. The repo boundary is the folder boundary, so nothing above it
can be committed by accident.
