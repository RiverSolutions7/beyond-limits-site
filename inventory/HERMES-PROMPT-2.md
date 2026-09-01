# Instructions for the inventory model, round 2

Paste everything below the line into Hermes. Nothing above the line is part of the prompt.

---

## CONTEXT

You are an archivist producing a complete, verbatim inventory of three pages on an
existing website.

You did this job once already, for eleven pages of the same site, and it passed
verification: 725 rows, every quote found character for character in its source. This is
the same job on three pages that were missed the first time. Hold the same standard.

You copy. You do not describe, improve, shorten, or tidy.

The site is `https://www.peaceyouthct.org/`, the Stamford Peace Youth Foundation, a youth
nonprofit in Stamford, Connecticut.

Round 1 covered the Peace Basketball hub page. That page turned out to be a signpost: its
whole job is to route visitors to three other pages, and those three are where the real
content lives. They hold the season dates, the registration prices, and the sign-up
paths. Round 2 is those three pages.

Your inventory proves to the site's owner that a redesign carried his content across
without inventing anything and without silently dropping anything. If a line of your
inventory is a paraphrase, that proof fails.

You are doing ONE job: recording what is on these pages. You are not evaluating them, not
comparing them to anything, and not suggesting improvements.

## WHAT ROUND 2 ADDS

Two things are different this time. Both exist because of problems found in round 1.

**1. You must capture URLs, not just link text.**

In round 1 the plain-text captures contained no URLs at all, so the href half of every
link could not be verified against anything. That was 121 rows, 17% of the inventory,
invisible to the checker. This time each text capture ends with a LINKS section listing
every href on the page. Format is given below.

**2. Copy broken URLs exactly as they are written.**

Round 1 found four links on the home page written as `http://https://example.com/`, a
doubled scheme that resolves to a nonsense hostname. Those are real defects on the live
site and reporting them is valuable. Had they been "helpfully" corrected, they would have
been carried into the new site as if they worked.

So: if a URL looks wrong, copy it wrong. Add a factual note saying what you observed, for
example `notes: "href has a doubled scheme"`. Do not fix it. Do not comment on whether it
should be fixed.

## INSTRUCTIONS

For each page in the PAGES list below:

1. Fetch the page.
2. Read it top to bottom in the order a visitor meets it.
3. Emit one JSON object per **content block**, in visitor order.

A content block is one of: a heading, a paragraph, a stat or figure, a list, a link, a
PDF or document, an image, a form, a contact detail, a price, a date, or an embed. If you
are unsure whether something is one block or two, make it two.

Include everything a visitor can see or click, including navigation items, footers,
buttons, form field labels, and image alt text. Exclude only the browser chrome that is
not part of the page: cookie banners and the site platform's own login widgets.

**These pages are transactional.** They carry prices, deadlines, season dates, age or
grade brackets, and contact details for registration. Capture every one of those as its
own row. A price with no row is a family arriving at a number they did not expect.

## CONSTRAINTS

These are not style preferences. Each one exists because breaking it makes the inventory
unusable.

1. **`content` must be copied character for character.** Not summarised, not cleaned, not
   re-punctuated.
2. **Reproduce errors exactly.** Round 1 preserved the misspellings "afforable", "succes",
   "Coodinator", "Schlolarship" and "informaiton". Do the same here. If you correct a
   typo, we cannot tell your errors from theirs.
3. **Never write a description in the `content` field.** "A paragraph about registration"
   is a failed row. The actual words, or nothing.
4. **If a page will not load, or shows a login wall instead of content, emit one row**
   with `"type": "error"` and say exactly what you saw in `notes`. Do not skip it silently
   and do not guess what was behind it. See the note on SUMMER below.
5. **Do not judge, rank, or recommend.** No "this is outdated", no "this should be
   updated". `notes` is for factual observations only: "link returns 404", "text is inside
   an image", "page displays a sign-in form", "date given is for the 2025-2026 season".

   Stating which season a page names is a fact. Saying that season is stale is a
   judgement. Record the first, never the second.
6. **Do not merge similar blocks.** The same phone number in three places is three rows.
7. **Do not stop early or write "and so on".** Every block, every page.

## OUTPUT FORMAT

A single JSON array. No prose before or after it. No markdown fences.

```json
[
  {
    "id": "SPBL-001",
    "source_url": "/page/show/8134836-peace-boys-basketball-league",
    "source_title": "Stamford Peace Basketball League",
    "source_section": "2025-2026 SPBL Season",
    "type": "paragraph",
    "content": "One practice one evening a week and one game on the weekend at a local gym.",
    "verbatim": true,
    "fetched": "2026-09-01",
    "notes": ""
  }
]
```

Field rules:

- `id` is a page prefix plus a three digit counter, restarting per page. The three
  prefixes are exactly `AAU`, `SPBL`, and `SUMMER`. No others. A row with any other prefix
  fails the checker.
- `source_section` is the nearest heading above this block, copied verbatim. Empty string
  if there is none.
- `type` is exactly one of: `heading`, `paragraph`, `stat`, `list`, `link`, `pdf`,
  `image`, `form`, `contact`, `embed`, `error`.
- `content` for a `link` is the visible link text, then ` -> `, then the href **exactly as
  written in the HTML**. For an `image`, the alt text, or `[no alt text]` if absent. For a
  `pdf`, the link text then ` -> ` then the URL.
- `verbatim` is `true` if `content` is copied exactly. `false` only for `image` and
  `error` rows, where a description is unavoidable.
- `fetched` is the date you loaded the page, `YYYY-MM-DD`.

## WHAT A FAILED ROW LOOKS LIKE

**Failed, summarised:**

```json
{ "type": "paragraph", "content": "A paragraph about league pricing and the early bird discount." }
```

Useless. We cannot compare wording we do not have.

**Failed, tidied:**

```json
{ "type": "link", "content": "Person to Person -> https://p2phelps.org/" }
```

The site writes `http://https://p2phelps.org/`. Correcting it hides a real defect.

**Failed, judging:**

```json
{ "type": "heading", "content": "2024 Summer League", "notes": "Outdated, should be removed." }
```

Not your call, and not this document's job.

**Correct:**

```json
{ "id": "SPBL-018", "source_url": "/page/show/8134836-peace-boys-basketball-league", "source_title": "Stamford Peace Basketball League", "source_section": "2025-2026 SPBL Season", "type": "stat", "content": "$220", "verbatim": true, "fetched": "2026-09-01", "notes": "Listed above the line 'Early Bird: thru Sept. 12'." }
```

## SELF-CHECK

This is how your work will be verified, so apply it yourself first.

Every `content` value where `verbatim` is `true` will be searched for, character for
character, in the page's own text. Any row that does not match exactly is a failure.

Before emitting a row, ask: **could I paste this string into the page and find it?** If
not, you have paraphrased. Fix it.

## PAGES

Do them in this order.

| Prefix | URL |
|--------|-----|
| AAU | https://www.peaceyouthct.org/aau |
| SPBL | https://www.peaceyouthct.org/page/show/8134836-peace-boys-basketball-league |
| SUMMER | https://www.peaceyouthct.org/page/show/8561799-2024-summer-league |

Notes on these pages:

- **AAU** is the largest of the three, roughly 12,000 characters of visible text. Expect
  the most rows here.
- **SPBL** carries the season dates, three price tiers, a member discount, a scholarship
  contact, and evaluation dates. Every one of those is its own row.
- **SUMMER** returned a SportsEngine sign-in form rather than page content when it was
  checked on 2026-09-01, roughly 250 characters of visible text. If you see the same, emit
  a single `error` row describing exactly what was displayed, and move on. If you can
  reach the real content, inventory it normally. Either outcome is a useful answer. Do not
  guess at content you cannot see.

## WHERE TO SAVE

Write all four files to disk yourself. Create folders if they do not exist.

**1. The JSON array**, to a NEW file. Do not touch `old-site-inventory.json`; it holds 725
already-verified rows from round 1.

```
C:\Users\river\OneDrive\Documents\SEO Agency\beyond-limits-site\inventory\old-site-inventory-2.json
```

**2. The plain text of every page you read**, exactly as you saw it, one file per page:

```
C:\Users\river\OneDrive\Documents\SEO Agency\beyond-limits-site\inventory\source-text\AAU.txt
C:\Users\river\OneDrive\Documents\SEO Agency\beyond-limits-site\inventory\source-text\SPBL.txt
C:\Users\river\OneDrive\Documents\SEO Agency\beyond-limits-site\inventory\source-text\SUMMER.txt
```

Each `.txt` file must end with a LINKS section, so hrefs can be verified too. Format it
exactly like this, one link per line, visible text then a tab character then the href:

```
=== LINKS ===
AAU page.	https://www.peaceyouthct.org/aau
click here for registration	https://example.com/register
```

The text files are not optional. Every quote in your JSON gets checked against them
character for character. Without them nothing can be verified.

## WHEN YOU ARE DONE

Confirm all four files were written, then report in plain text:

- rows per page
- whether SUMMER showed real content or a sign-in form
- every price, date and deadline you captured, as a short list, so a human can sanity
  check them without opening the JSON
- anything you were unsure how to classify

Keep that report out of the JSON file.
