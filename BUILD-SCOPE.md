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
| ~~6~~ | **DONE.** Partner logo grid wired, all 14, four corrected | `index.html` | HOME-057 to 096 | done |
| ~~7~~ | **DONE.** Two Get Involved paths, as a secondary block not doorcards | `start.html` | GETINV-014 to 017, GETINV-023 to 028 | done |
| ~~8~~ | **DONE.** Our Impact: four student stories, programme list, growth figures | `impact.html`, new | IMPACT-002 to 036 | done |

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
site.

*Swept afterwards: every other `.btn-ghost` on the site sits inside either the navy
`.doorcard` or the footer, whose background computes to `rgb(11, 27, 48)`. Both are dark,
so white-on-white was introduced by this section alone and is now fixed. No other page is
affected.*

**Item 4.** Two open client questions are now sourced rather than guessed:

- **203-588-9020 is the Foundation line.** Kriftcher, Sasser, Curto and General Inquiries
  all carry it. **203-588-9023 is listed only against Andy Sklover**, "Co-founder, BEYOND
  LIMITS ACADEMIC PROGRAM", so it is the Beyond Limits line. Our footer already carries
  9023 with a chip asking which entity owns it.
- **`info@peaceyouthct.org`** is the published address, appearing six times across four
  pages. The Contact page hides its four addresses behind `compose_email` forms, which is
  why it looked like there was no address at all.

Both still want Andy's confirmation, but each now has a citation instead of a chip.

**Item 6, as built.** All fourteen wired, not ten. Four carried a doubled scheme on the
live site, `http://https://`, which resolves to a nonsense hostname: Person to Person,
Community Fund of Darien, Charter Communications and Sacred Heart. Those were the only
four of the fourteen that failed to load, which is what confirmed the defect was real
rather than a transcription slip. The intended targets are unambiguous, so the corrected
URL is wired and the breakage goes to Andy as a finding rather than being patched
silently.

---

### Wave 1 is complete

All eight items built, plus theme 9 ahead of its wave. Nine sections across five pages,
and one new page.

One thing surfaced building Impact that is worth Andy seeing. **IMPACT-010 contradicts
the tutoring page we had already built.** It says "over 200 students in the 3rd through
12th grades" and "over 80 percent" eligible for free or reduced-price lunch. Our tutoring
page says grades 4 to 10 and around 90%. The facts file forbids resolving a disagreement
by aligning one page to the other, so both ship as sourced and the Impact figures carry
chips naming the conflict. All three are already findings questions 1 and 2.

It also gives a third independent source for **2013** as the launch year: "Established in
late 2013". LEAD-014 says Sklover co-founded it in 2013 and the live Beyond Limits page
says 2014. Two sources to one, and "late 2013" reconciles them.

### Round 3: the board and alumni, added 2026-09-01

Dan asked what happened to the board section. Neither `/boardofdirectors` nor `/alumni`
had been inventoried by round 1 or round 2, and neither was on the new site.

**Board, on `about.html`.** Nine members, eight as an accordion plus Kriftcher whose
biography already sits above. Finance, real estate, social work, clergy and economic
development, most of them living in Stamford. This is the section a grant reviewer goes
looking for.

**Alumni, on `basketball.html`.** The colleges, not the roster. The old page lists 99
named alumni across the classes of 2013 to 2020, naming 74 distinct institutions. Naming
the schools keeps the proof and drops three liabilities: a roster six years out of date,
99 names to maintain, and one entry that appears to carry the wrong person's name. The
page says "more than 70", which holds under any way of counting.

**It also caught a live error in our own work.** The Kriftcher bio published that morning
came from `/leadership`, the oldest of three versions on the client's site. It named
coaching roles he had left and a chairmanship he stood down from in 2018. Corrected from
the board page. Recorded as finding 8.

## Wave 2: blocked, and on what

| What | Blocked on | Why it cannot proceed |
|------|-----------|----------------------|
| ~~Scholarships for Beyond Limits students~~ | ~~Dan~~ | **DONE.** Dan reviewed the source and chose to carry all four recipients, reorganised into one accordion. Built on `tutoring.html`. |
| Three Beyond Limits sub-campaign descriptions | Andy | No source text exists anywhere. |
| ~~`basketball.html`~~ | **DONE 2026-09-01.** | Built as durable structure, linking out for dates and prices. See note below. |
| The Español toggle, 14 dead links | Andy | Findings question 16. Whether Spanish is in scope is a budget decision, not ours. |
| Privacy policy, 6 dead links | Andy | The only one is a SportsEngine PDF dated Feb 2020, describing a platform the new site does not run on. |
| Media consent, 6 dead links | **Us** | It appears in **none** of the 725 rows. We added this link. It has no source and no destination. |
| Grades, fees, student count, $20,000 tier | Andy | Findings questions 1, 2, 7, 8. These clear 37 chips. |

---

### basketball.html, and why it carries no prices

Dan chose durable structure over completeness. The page describes the three leagues in
the Foundation's own words, which does not go stale, and links out for season dates and
fees, which change every year and are maintained elsewhere.

That was the right call for a specific reason: the Boys League page currently advertises
the **2025-2026 season, November 22 to March 8**, which ended in March 2026, alongside an
early-bird deadline of **September 12** that reads as current. Reproducing it faithfully
would have published a finished season on work we hand to Andy. Verified: no price or
season date appears anywhere on our page.

The Summer League card does not link to the Summer League page, because that page is a
SportsEngine sign-in wall. It points at our own contact block instead, which is a real
answer rather than a dead end.

Building it also turned up two footer links, on `donate.html` and `sponsorship.html`,
sending "Beyond Limits Academics" back to the **old site**. Our own footer was undoing
the redesign. Fixed. 21 Basketball links and 18 Our Impact links were rewired in total,
and the only two external `peaceyouthct.org` links left on the whole site are the two
deliberate registration links on this page.

## Wave 3: polish, last

Ordered as agreed: nothing here starts until waves 1 and 2 are settled.

1. ~~Assistant coverage.~~ **Measured 2026-09-01, and the framing was wrong.**

   The assistant is **enrollment-only**: ten steps, families with a student in grades 4
   to 10, no tutor, sponsor or donor branch. So "put it on every page" would drop a
   would-be tutor into a student enrollment form. Coverage is not the goal; the right
   audience reaching it is.

   What was actually wrong: `beyond-limits.html`, the main program page, offered two
   hero buttons and **both were in-page scrolls**. A convinced parent had no way to start
   anything from the top of the page. Its primary CTA now reaches the assistant.

   The persuasion pages, `impact.html`, `about.html` and `basketball.html`, correctly
   route to `tutoring.html`, which carries the assistant alongside cost and logistics.
   Sending someone from an impact page straight into a four-minute enrollment form is
   worse, not better. `sponsorship.html` should never reach the assistant at all.

2. **The real hole: tutors had nowhere to go.** Families reach the assistant, sponsors
   reach the sponsorship page, donors reach the donate page. Two links said "apply" and
   both were dead. There is no application form anywhere, so both now point at the
   contact block, which is a working path. A real application form is an Andy question.

3. Dead links: **41 down to 26.** Every content link now resolves; a full crawl of all
   200 internal links found no broken file and no missing anchor. The 26 left are the two
   groups genuinely blocked on him, Espanol (18) and the privacy policy (8). Media consent
   was removed: we invented it, and it had no source and no destination.
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
