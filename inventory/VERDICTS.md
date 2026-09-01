# Proposed verdicts: the 206 items not found on the new site

Grouped into fourteen themes so they can be approved as themes, not as 206 rows.

Two verdicts are possible:

- **OMIT** — deliberately left out. Every one carries a reason we could say out loud
  to the client.
- **ADD** — genuinely missing. Needs a home on the new site.

**Status as of 2026-09-01.** Four themes are now decided and carry a dated block
saying so: **6** and **7** stay out and go to Andy as questions, **5** and **8** were
reversed to ADD and get built. The remaining ten are still proposals.

---

## OMIT — platform and UI artifacts

### 1. SportsEngine chrome · ~20 rows · every page
"Sports Relationship Management", "©2026 SportsEngine, LLC.", login and account
widgets.

**Reason:** branding for the old site's hosting platform. The new site does not run on
SportsEngine, so carrying it across would be inaccurate.

### 2. Platform UI labels · ~12 rows
"Click for MORE INFO", "Click on image to view full presentation", "Interested in
Participating?", "Enter or select an amount:", the four `layout_container` tab links.

**Reason:** interface furniture from the old page builder, not content. The equivalent
function exists on the new site with different wording.

### 3. Dated 2025 material · 3 rows
2025 Summer Tutoring Flyer (English), 2025 Summer Tutoring Flyer (Spanish), 2025 MSSSP.

**Reason:** these describe a programme that has finished. Carrying them over would put
stale dates in front of a parent. Should return when the 2026 equivalents exist.

---

## OMIT — out of the Beyond Limits funnel

### 4. Basketball-specific items · ~4 rows
PEACE Basketball & JCC Merger PDF, the Edona basketball testimonial, AAU links.

**Reason:** Peace Basketball is a separate programme. The new site links out to it
rather than reproducing it, which is the scope we agreed.

### 5. SquadLocker merchandise shop · 4 rows
"Rep PEACE swag: shop Squad Locker for cool PEACE t-shirts, hoodies and more. A portion
of sale benefits..."

**Reason:** merchandise for the Foundation as a whole, not a Beyond Limits path.
⚠ **This is a live fundraising channel we would be dropping.** Worth a deliberate yes
or no rather than silence.

> **DECIDED 2026-09-01 (Dan). Reversed to ADD.** Keep it, as one row in the donate
> page's "Other ways to support the Foundation" strip (theme 8).
>
> **Checked before deciding:** the store is live. `curl` returns 403, but that is a
> Cloudflare bot challenge, not a dead link. Loaded in a real browser it resolves to a
> stocked Stamford Peace locker of 59 items across Under Armour, Champion, Badger and
> Carhartt, with an active clearance section. So omitting it would have silenced a
> channel that currently works, which is a different thing from tidying away a dead one.
>
> It goes in the donate strip rather than on the Get Involved router. The router is
> already due two more cards from theme 14, and shopping is a way to give rather than a
> way to participate. The strip costs it one line and no new structure.
>
> Source copy: GETINV-029 and GETINV-030, plus HOME-050 and HOME-051.

---

## OMIT — needs the client's explicit permission, not a default

### 6. Bill Susetka scholarship recipient names · ~40 rows
A published list of roughly forty named scholarship recipients, most of them children.

**Reason:** republishing a list of named minors on a new site is a decision for the
client to make explicitly. Carrying it across by default because it happened to be on
the old page is the wrong instinct. It is also a different fund, not Beyond Limits.

**Recommendation:** leave out, and ask. If he wants it, it is trivial to add back.

> **DECIDED 2026-08-31 (Dan).** Leave it off the new site, and put the question to Andy
> for his sign-off rather than deciding it for him. Added to the client findings
> document as question 17 so it reaches him in writing.
>
> Two things noted while checking the section in context: it is a **Stamford Peace
> Basketball League** award, not a Beyond Limits one, so it sits outside the tutoring
> pages on scope grounds as well. And the fund is a **memorial** to Bill Susetka, so the
> recipient list may be part of the tribute rather than incidental. If Andy wants it, it
> goes back exactly as it reads now.

---

## OMIT — but flag, because we are dropping a function

### 7. Mailing list signup · ~6 rows
"Stay Connected With Peace", "Join Our Mailing List", the language selector, and
"MailChimp is currently unavailable. Please check back later."

**Reason:** the widget is broken on the live site right now, and the new site routes
people to the onboarding assistant instead.

⚠ **Email capture is a real function and we have no replacement for it.** The assistant
collects contact details, but only from people who complete enrolment. Someone who just
wants updates has nowhere to go.

> **DECIDED 2026-08-31 (Dan).** Leave it off for now and flag it to Andy rather than
> building a replacement. Added to the client findings document as question 18.
>
> Reasoning: a working signup needs somewhere for the addresses to go, which means an
> email service and Andy's account. That cannot be finished without him, so asking is
> the honest step rather than half-building it. The funnel stays pointed at the
> assistant in the meantime.

### 8. Other Foundation funds on the donate page · ~8 rows
Bill Susetka Memorial Scholarship Fund description, Kosovo Heritage Basketball Academy,
and their donate instructions.

**Reason:** our Donate page is scoped to Beyond Limits by design, and the campaign menu
at checkout already lets a donor choose another fund.

⚠ The old page was **Foundation-wide**. If Andy expects his donate page to still cover
every fund, this is the item he will notice first.

> **DECIDED 2026-09-01 (Dan). Reversed to ADD.** Keep every fund. None get dropped.
>
> They go in a short "Other ways to support the Foundation" strip at the foot of the
> donate page, one line and a give button each, below the Beyond Limits block. Beyond
> Limits keeps the page; the other funds stop being invisible.
>
> No onboarding-assistant work is involved. The old site's own routing pattern was a
> description plus "select this from the CAMPAIGN drop down box", and our donate page
> already does exactly that for Beyond Limits. The strip repeats that pattern per fund.
>
> **Blocked on Andy for three of them.** We hold sourced copy for the Susetka fund
> (DONATE-053) and Kosovo Heritage (DONATE-057). The three Beyond Limits sub-campaigns
> in the Kindful menu — End of School Year, Sponsorships 25-26, and the Hart Elementary
> Collaboration — appear nowhere in the 725-row inventory. They exist only inside the
> checkout menu. They can be named but not described until he tells us what they fund.

---

## ADD — genuinely missing, and it matters

### 9. Scholarships available to Beyond Limits students · ~8 rows
The Stamford Rotary Trust Scholarship, the Bill Susetka Memorial Scholarship as offered
*to Beyond Limits students*, the 2025-2026 recipients (Anthony Lopez, Danna Rivas), and
Mia's testimonial.

**Why it matters:** this is a direct parent-facing benefit. "Your child could earn a
scholarship" is one of the strongest reasons to enrol, and it is currently nowhere on
the new site.

**Proposed home:** Tutoring page, near the cost section.

> **DECIDED 2026-09-01 (Dan). Carry all four across, reorganised.** Dan reviewed the
> source material in full before deciding.
>
> **What is being republished.** Four recipients, not two as first reported. Annabella
> (10, 5th grade) and Mia (11, 6th grade, names Dolan Middle School) under the Rotary
> award, both writing in the first person. Anthony Lopez (13) and Danna Rivas under the
> Susetka award, also in the first person. Rows BL-053 to BL-069.
>
> **The concern, stated and overruled.** A first name with an age and a named school is
> enough to identify a specific child, and that combination appears in Mia's entry. It is
> already public on Andy's live site, so nothing here is being exposed that was not
> exposed already. Dan's call is that faithfulness to "all of the old website's
> information reorganized" wins, and that reproducing what he already publishes is not
> our decision to override. Recorded here so the reasoning is not lost.
>
> **Reorganised, not copied.** On the old site the four are scattered: Annabella, then
> the Rotary description, then Mia, then the Susetka description, then Anthony and Danna,
> with their quotes separated from their names further down. All four go in one block
> together, under the two scholarship descriptions. UI to be designed.
>
> **Open: photographs.** The old page carries an image beside each recipient (BL-052,
> BL-055, BL-064, BL-066). We hold none of those files and all four lack alt text.
> Defaulting to a text-only treatment. Fetching and republishing photographs of named
> children is a further step and has not been agreed.
>
> **Andy still gets told.** Not as an omission, but as a disclosure: we carried your four
> recipients across, here is where they sit, say the word and they come out.

### 10. Leadership biographies · ~10 rows
Full biographies for Brian Kriftcher ("Coach K") and Andy Sklover.

**Why it matters:** the About page currently has no people on it at all. A parent
deciding whether to trust strangers with their child gets nothing about who runs this.

**Proposed home:** About page, new section.
⚠ **Andy Sklover appears here as leadership.** If your client is Andy Sklover, this is
his own biography, and the founders question can be settled by asking him directly.

### 11. Staff and contact details · ~12 rows
Caroline Sasser (Program Coordinator), Andy Sklover, Martine Curto, General Inquiries,
plus office hours.

*Corrected 2026-09-01: this line previously read "office hours Tuesday to Sunday", which
was wrong. CONTACT-034 to CONTACT-040 say Monday to Thursday 9AM-3PM, with Friday,
Saturday and Sunday closed. That matches what the donate page already says.*

**Why it matters:** a parent with a question currently has one phone number and a
confirm marker. Named humans with roles is a trust signal, and office hours prevent a
wasted call.

**Proposed home:** About page, or a contact block in the footer.

> **The CONTACT page answers two of our open client questions.** Noted 2026-09-01.
>
> **Which phone belongs to which entity (findings q11).** 203-588-**9020** is the
> Foundation line: Kriftcher, Sasser, Curto and General Inquiries all list it.
> 203-588-**9023** is listed only against Andy Sklover, "Co-founder, BEYOND LIMITS
> ACADEMIC PROGRAM". So 9023 is the Beyond Limits line. Our footer carries 9023 with a
> chip reading "confirm which entity owns this number", and this sources it.
>
> **Which email is canonical (findings q12).** `info@peaceyouthct.org`. It is the only
> address published anywhere on the old site, and it appears six times across four
> pages: HOME-049, GETINV-020, GETINV-034, DONATE-019, DONATE-051 and INVEST-019.
> Confirmed present in the raw text captures.
>
> *An earlier version of this note said no address was published anywhere. That was
> wrong. It is true only of the Contact page, where all four addresses sit behind
> `/page_element/compose_email/NNNNNN` forms. The rest of the site prints it plainly.*
>
> Neither should be treated as settled without his confirmation, but both now have a
> source rather than a guess.

### 12. DEI commitment and non-discrimination statement · 3 rows
"We are cognizant of the fact that our society's full promise has eluded too many for
far too long..." and "Stamford Peace does not discriminate on the basis of race, color,
national origin (ancestry), religion..."

**Why it matters:** for a nonprofit these are not decorative. They are frequently cited
in grant applications and expected by funders. Dropping them silently from a redesign
is the kind of omission a board notices.

**Proposed home:** About page.

### 13. Partner website links · ~13 rows
The new site shows the partner logos but none of them link anywhere. The old site had a
"Visit Website" link for each: Boys & Girls Club, PGC Basketball, Stamford JCC, Near &
Far Aid, Laureus, Yerwood Center, New Canaan YMCA, Grace Farms, Person to Person,
Community Fund of Darien, Charter Communications, Stamford Public Schools.

**Why it matters:** small, but we are showing partners' marks without crediting them
with a link. Easy fix and good manners.

**Proposed home:** wire the existing logo grid.

### 14. Two Get Involved paths · ~4 rows
"Host a Fundraiser" and "Help Us Spread the Word".

**Why it matters:** the old Get Involved page offered five ways in. Our router offers
four, and these two are the ones missing.

**Proposed home:** the router, or a decision that they are out of scope.

---

## Summary

| Verdict | Themes | Rows |
|---|---|---|
| OMIT, uncontroversial | 1, 2, 3, 4 | ~39 |
| OMIT, needs permission | 6 | ~40 |
| OMIT, flagged as a dropped function | 7 | ~6 |
| ADD | 5, 8, 9, 10, 11, 12, 13, 14 | ~62 |

Roughly 50 items to place, about 40 that need one yes or no from the client, and the
rest are defensible omissions with reasons attached.
