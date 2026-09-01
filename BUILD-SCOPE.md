# Build scope: from here to a finished site

Written 2026-09-01, after the last two content questions closed.

The four content questions are answered. This document turns the leftovers into a
build queue and separates what can be built today from what cannot.

The test for "buildable today" is strict: **we hold the words, from a cited inventory
row, and no one has to answer anything first.** Everything else waits.

---

## Wave 1: buildable today

Seven items. Every one has sourced copy in hand. None needs Andy.

| # | What | Goes on | Source rows | Size |
|---|------|---------|-------------|------|
| ~~1~~ | **DONE.** Other ways to support the Foundation: Susetka, Kosovo, three named sub-campaigns | `donate.html`, foot | DONATE-053, BL-063, DONATE-057 | done |
| ~~2~~ | **DONE.** Stamford Peace shop row inside that strip | `donate.html`, same strip | GETINV-029, GETINV-030 | done |
| ~~3~~ | **DONE.** Leadership: Kriftcher and Sklover, as an accordion | `about.html` | LEAD-005 to 010, LEAD-014 to 017 | done |
| ~~4~~ | **DONE.** Who to talk to: five contacts, two numbers, office hours | `about.html` | CONTACT-003 to 040 | done |
| ~~5~~ | **DONE.** Our commitment, uncollapsed so funders can find it | `about.html` | WWD-013, WWD-014 | done |
| 6 | Wire the partner logo grid, 10 of 14 links | `index.html` | HOME-057 to 096 | small |
| 7 | Two Get Involved paths: Host a Fundraiser, Spread the Word | `start.html` | GETINV-014 to 017, GETINV-023 to 030 | medium |
| 8 | Our Impact page: four student stories, programme list, growth figures | `impact.html`, new | IMPACT-002 to 036 | large |

### Item 3 was the most urgent thing on this list, and is now done

`about.html` was headlined **"The people behind Beyond Limits"** with no people on it.
The headline promised something the page did not deliver. It now carries both
biographies, five named contacts with direct numbers and office hours, and the DEI and
non-discrimination statements.

Also done, ahead of its wave: **theme 9, the scholarships section**, on `tutoring.html`
directly after the cost block. That was blocked on Dan and is now decided and built.

### Notes that change how three of these get built

**Item 1, as built.** The three Beyond Limits sub-campaigns are named and linked but
carry no description, with a "confirm what these fund" chip, because they appear nowhere
in the 725 rows. They exist only inside the checkout menu.

Two things surfaced while building it. The old page told donors to select **"KHBA"** for
Kosovo, but the live menu in Dan's checkout screenshot reads **"2026 Kosovo Heritage
Basketball Academy"**, so the fund looks to have been relabelled for the new fiscal year.
And `.btn-ghost` is a white border with white text, which only works on the navy
doorcard: on the white fund card all four buttons rendered invisible. Added
`.btn-outline` for light surfaces, matching the `.subpill-off` idiom already on the
site. Worth checking wherever else `.btn-ghost` sits on a light background.

**Item 4.** Two open client questions are now sourced rather than guessed:

- **203-588-9020 is the Foundation line.** Kriftcher, Sasser, Curto and General Inquiries
  all carry it. **203-588-9023 is listed only against Andy Sklover**, "Co-founder, BEYOND
  LIMITS ACADEMIC PROGRAM", so it is the Beyond Limits line. Our footer already carries
  9023 with a chip asking which entity owns it.
- **`info@peaceyouthct.org`** is the published address, appearing six times across four
  pages. The Contact page hides its four addresses behind `compose_email` forms, which is
  why it looked like there was no address at all.

Both still want Andy's confirmation, but each now has a citation instead of a chip.

**Item 6.** Only ten of the fourteen partner links can be wired. Four are broken on the
live site: they carry a doubled scheme, `http://https://`, which resolves to a nonsense
hostname. Person to Person, Community Fund of Darien, Charter Communications and Sacred
Heart. The intended targets are obvious, so we can wire the corrected URL, but the
breakage should be reported rather than quietly patched.

---

## Wave 2: blocked, and on what

| What | Blocked on | Why it cannot proceed |
|------|-----------|----------------------|
| ~~Scholarships for Beyond Limits students~~ | ~~Dan~~ | **DONE.** Dan reviewed the source and chose to carry all four recipients, reorganised into one accordion. Built on `tutoring.html`. |
| Three Beyond Limits sub-campaign descriptions | Andy | No source text exists anywhere. |
| `basketball.html` | **Hermes round 2** | The hub page is a signpost. Real content is on three uninventoried pages. Prompt written, not yet run. |
| The Español toggle, 14 dead links | Andy | Findings question 16. Whether Spanish is in scope is a budget decision, not ours. |
| Privacy policy, 6 dead links | Andy | The only one is a SportsEngine PDF dated Feb 2020, describing a platform the new site does not run on. |
| Media consent, 6 dead links | **Us** | It appears in **none** of the 725 rows. We added this link. It has no source and no destination. |
| Grades, fees, student count, $20,000 tier | Andy | Findings questions 1, 2, 7, 8. These clear 37 chips. |

---

## Wave 3: polish, last

Ordered as agreed: nothing here starts until waves 1 and 2 are settled.

1. Assistant coverage. It is on four of seven pages, missing from `beyond-limits.html`,
   `sponsorship.html` and `about.html`. Those are where a family, a donor and a curious
   visitor land.
2. Audience-specific entry points. Every existing call to action says roughly the same
   thing to four different audiences.
3. Scroll animations and UI.
4. The feedback deck for Andy.

---

## Decisions needed from Dan

**1. Basketball and Our Impact.** ~~Both nav items point at `peaceyouthct.org`.~~
**DECIDED 2026-09-01 (Dan): build both.**

- **`impact.html` proceeds now.** 35 content rows: four student stories, the full
  programme list, growth figures. Strong and self-contained. Moved to Wave 1 as item 8.
- **`basketball.html` waits for a second inventory pass.** The hub page holds only 13
  content rows, six of which are "Go to our X page" plus its link. The substance lives on
  three pages nobody inventoried: AAU (12,220 chars), the Boys League (2,161), and the
  2024 Summer League (249). Dan chose to inventory those first rather than build a
  signpost. See `HERMES-PROMPT-2.md`. Sits in Wave 2 until that returns.

**2. Dead links, 34 of them.** Español is blocked on Andy. Privacy policy points at a
stale SportsEngine PDF. Media consent has no source at all. Leave them dead until Andy
answers, hide them until they work, or remove Media consent outright since we invented it?

**3. Named children.** Theme 9 would publish Anthony Lopez and Danna Rivas, both named
scholarship recipients, one stated as 13 years old, with their quotes. You already
deferred the forty-name list on exactly this reasoning. Consistency says defer this too,
which costs us the single strongest parent-facing argument on the site: your child could
earn a scholarship. The scholarship section can be built without the names.

**4. Broken partner links.** Wire the corrected URLs and tell Andy, or leave them out
until he fixes his own site?
