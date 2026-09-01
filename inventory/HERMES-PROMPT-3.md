# Instructions for the inventory model, round 3

Paste everything below the line into Hermes. Nothing above the line is part of the prompt.

---

## CONTEXT

You are an archivist producing a complete, verbatim inventory of two pages on an existing
website.

You have done this job twice on this site. Round 1 covered eleven pages and passed. Round
2 covered three and passed with two rows removed: they were plausible youth-league
boilerplate that appeared nowhere on the page or in your own capture. Round 3 is two pages
that both earlier rounds missed. Hold the standard, and do not let a sentence in that you
did not read.

You copy. You do not describe, improve, shorten, or tidy.

The site is `https://www.peaceyouthct.org/`, the Stamford Peace Youth Foundation, a youth
nonprofit in Stamford, Connecticut.

## WHY THESE TWO PAGES MATTER MORE THAN THEY LOOK

The board page has already caused one real error, which is why you are being sent back.

A biography was published on a redesigned site using the version from
`/leadership`. That turned out to be the oldest of three versions on this site. It named
coaching roles the man left years ago, and it stated that he "is the Global Chairman" of
an organization he chaired from July 2012 to December 2018. The board page has the current
version. Nobody had read it, because nobody had inventoried it.

So this round is not a formality. **Where two pages on this site disagree, record both
exactly as written and let a human decide.** Never smooth a difference away, and never
assume the version you saw first is the current one.

For a nonprofit, the board page is also the page funders and grant reviewers look for
specifically. Every name, title, employer and qualification on it needs to be exact.

## INSTRUCTIONS

For each page in the PAGES list below:

1. Fetch the page.
2. Read it top to bottom in the order a visitor meets it.
3. Emit one JSON object per **content block**, in visitor order.

A content block is one of: a heading, a paragraph, a stat or figure, a list, a link, a PDF
or document, an image, a form, a contact detail, or an embed. If you are unsure whether
something is one block or two, make it two.

Include everything a visitor can see or click, including navigation items, footers,
buttons, form field labels, and image alt text. Exclude only the browser chrome that is
not part of the page: cookie banners and the site platform's own login widgets.

**Each board member is several rows, not one.** A name is a row. Every paragraph of their
biography is its own row. Do not compress a person into a summary.

## CONSTRAINTS

1. **`content` must be copied character for character.** Not summarised, not cleaned, not
   re-punctuated.
2. **Reproduce errors exactly.** Earlier rounds preserved "afforable", "succes",
   "Coodinator", "Schlolarship", "informaiton" and "workships". The board page contains at
   least one too: a not-for-profit is written with a stray space, as "not- for-profit".
   Keep it. If you correct a typo we cannot tell your errors from theirs.
3. **Never write a description in the `content` field.** "A paragraph about a board
   member" is a failed row. The actual words, or nothing.
4. **If a page will not load, or shows a login wall instead of content, emit one row** with
   `"type": "error"` and say exactly what you saw in `notes`. Do not guess what was behind
   it.
5. **Do not judge, rank, or recommend.** `notes` is for factual observations only: "link
   returns 404", "text is inside an image", "this bio differs from the one on /leadership".
   Noting that two pages differ is a fact. Saying which is right is not.
6. **Do not merge similar blocks.** The same qualification on two people is two rows.
7. **Do not stop early or write "and so on".** Every block, every page.
8. **Copy broken URLs exactly as written.** Round 1 found four links on the home page
   written `http://https://example.com/`, a doubled scheme resolving to a nonsense
   hostname. Round 2 found a `mailto:` whose visible text and address were different
   people. Both were real defects worth reporting. If a URL looks wrong, copy it wrong and
   note what you observed.

## OUTPUT FORMAT

A single JSON array. No prose before or after it. No markdown fences.

```json
[
  {
    "id": "BOARD-014",
    "source_url": "/boardofdirectors",
    "source_title": "Our Board of Directors",
    "source_section": "Dorothy Brill",
    "type": "paragraph",
    "content": "Dorothy Brill is the Chief People Officer at Grayscale Investments, where she builds talent function at the firm.",
    "verbatim": true,
    "fetched": "2026-09-01",
    "notes": ""
  }
]
```

Field rules:

- `id` is a page prefix plus a three digit counter, restarting per page. The two prefixes
  are exactly `BOARD` and `ALUMNI`. No others.
- `source_section` is the nearest heading above this block, copied verbatim. On the board
  page, use the person's name as it appears. Empty string if there is none.
- `type` is exactly one of: `heading`, `paragraph`, `stat`, `list`, `link`, `pdf`, `image`,
  `form`, `contact`, `embed`, `error`.
- `content` for a `link` is the visible link text, then ` -> `, then the href **exactly as
  written in the HTML**. For an `image`, the alt text, or `[no alt text]` if absent.
- `verbatim` is `true` if `content` is copied exactly. `false` only for `image` and `error`
  rows.
- `fetched` is the date you loaded the page, `YYYY-MM-DD`.

## WHAT A FAILED ROW LOOKS LIKE

**Failed, summarised:**

```json
{ "type": "paragraph", "content": "A board member with a finance background and an MBA." }
```

**Failed, invented.** This is the exact failure mode that cost two rows in round 2. Both
read like ordinary, plausible copy. Neither was on the page.

```json
{ "type": "paragraph", "content": "The board is committed to strong governance and to serving the young people of Stamford." }
```

Before emitting any row, ask: **could I paste this string into the page and find it?**

**Failed, tidied:**

```json
{ "type": "paragraph", "content": "...a not-for-profit organization that uses the game of basketball..." }
```

The page writes "not- for-profit", with the space. Keep it.

## PAGES

| Prefix | URL |
|--------|-----|
| BOARD | https://www.peaceyouthct.org/boardofdirectors |
| ALUMNI | https://www.peaceyouthct.org/alumni |

Notes on these pages:

- **BOARD** is roughly 12,100 characters of visible text, around 26 substantial
  paragraphs, and at least eight people. Brian Kriftcher is listed first and has five
  paragraphs to himself. Others seen include Dorothy Brill, Gina Frederick, Rev. Chapin
  Garner, Darrell Johnson, Brian Large, Patrick Powers and Mike Tepedino. That list came
  from a rough scan and may be incomplete: **trust the page, not this list.**
- **ALUMNI** is roughly 5,400 characters, around 22 paragraphs. It includes a News Channel
  12 "Peace Project" interview and quoted material. Capture the quotes verbatim, including
  any hashtags.

## WHERE TO SAVE

Write all three files to disk yourself. Create folders if they do not exist.

**1. The JSON array**, to a NEW file. Do not touch `old-site-inventory.json` or
`old-site-inventory-2.json`; those hold 725 and 164 already-verified rows.

```
C:\Users\river\OneDrive\Documents\SEO Agency\beyond-limits-site\inventory\old-site-inventory-3.json
```

**2. The plain text of every page you read**, exactly as you saw it, one file per page:

```
C:\Users\river\OneDrive\Documents\SEO Agency\beyond-limits-site\inventory\source-text\BOARD.txt
C:\Users\river\OneDrive\Documents\SEO Agency\beyond-limits-site\inventory\source-text\ALUMNI.txt
```

Each `.txt` file must end with a LINKS section so hrefs can be verified too. Format it
exactly like this, one link per line, visible text then a tab character then the href:

```
=== LINKS ===
Meet our Leadership	https://www.peaceyouthct.org/leadership
```

The text files are not optional. Every quote in your JSON gets checked against them
character for character. Without them nothing can be verified.

## WHEN YOU ARE DONE

Confirm all three files were written, then report in plain text:

- rows per page
- the full list of board members you found, with their titles and employers, so a human
  can sanity check the roster without opening the JSON
- any place where a bio on the board page disagrees with the same person's bio on
  `/leadership`, quoting both
- anything you were unsure how to classify

Keep that report out of the JSON file.
