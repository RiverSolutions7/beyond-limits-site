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
| 1 | "Other ways to support the Foundation" strip: Susetka, Kosovo, three named sub-campaigns | `donate.html`, foot | DONATE-053, DONATE-057 | medium |
| 2 | Stamford Peace shop row inside that strip | `donate.html`, same strip | GETINV-029, GETINV-030 | small |
| 3 | Leadership: Brian Kriftcher and Andy Sklover | `about.html` | LEAD-005 to 008, LEAD-014 to 017 | medium |
| 4 | Staff, phone numbers, office hours | `about.html` or footer | CONTACT-003 to 040 | medium |
| 5 | DEI statement and non-discrimination clause | `about.html` | WWD-013, WWD-014 | small |
| 6 | Wire the partner logo grid, 10 of 14 links | `index.html` | HOME-057 to 096 | small |
| 7 | Two Get Involved paths: Host a Fundraiser, Spread the Word | `start.html` | GETINV-014 to 017, GETINV-023 to 030 | medium |

### Why item 3 is the most urgent thing on this list

`about.html` is headlined **"The people behind Beyond Limits."** There are no people on
it. The two sections are "The Uniqueness of Our Model" and "A Growing List of
Collaborators." The headline promises something the page does not deliver, and we hold
full biographies for both men.

### Notes that change how three of these get built

**Item 1.** We hold real copy for the Susetka fund and Kosovo Heritage. The three Beyond
Limits sub-campaigns in the Kindful menu, End of School Year, Sponsorships 25-26 and the
Hart Elementary Collaboration, appear nowhere in the 725 rows. They exist only inside the
checkout. They can be named and linked, but not described, until Andy says what they fund.

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
| Scholarships for Beyond Limits students | **Dan, then Andy** | We hold the copy, but it names two 13-year-olds and quotes them. Same class as the recipient list already deferred. See decision 3. |
| Three Beyond Limits sub-campaign descriptions | Andy | No source text exists anywhere. |
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

**1. Basketball and Our Impact.** Both nav items currently point at `peaceyouthct.org`.
A visitor clicking them leaves the new site and lands on the old one, mid-journey. Build
the two pages, or accept the handoff and label those links as external?

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
