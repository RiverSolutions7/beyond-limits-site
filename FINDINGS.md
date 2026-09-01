# Things we found on the live site

Every item here was verified against `peaceyouthct.org` directly, not inferred from the
inventory. Each says how it was checked, so any of them can be re-tested.

These are free findings for Andy. They are true whether or not he ever works with us.

Kept separate from `inventory/VERDICTS.md`, which is about what we carry across, and from
`BUILD-SCOPE.md`, which is about what we build. This file is only about defects on his
existing site.

---

## 1. The donate page links a sponsorship kit that no longer loads

`/donate` carries "Download our sponsorship kit HERE" pointing at
`cdn1.../ee3c-3414745/BL_Sponsorship_Kit_2025-2026_DIGITAL.pdf`, which returns **403
Access Denied**. Anyone following it today gets nothing.

The current kit is live at a different address,
`cdn3.../0b43-3495706/BL_Sponsorship_Kit_2025-2026_FINAL.pdf`, and loads fine. Attachment
ids are sequential, so 3495706 is the newer document.

**Fix:** repoint the link.

---

## 2. A donor supporting Beyond Limits has to know a step nobody tells them

The Kindful checkout opens with a campaign menu. If a donor does not select **"Beyond
Limits 2025-2026"**, the gift is not attributed to the program. Nothing on `/donate` says
so, although the Susetka and Kosovo pages do tell donors to pick their campaign, so the
pattern already exists.

**The question that removes the step entirely:** can the Kindful administrator generate a
campaign landing URL for Beyond Limits 2025-2026? If so a donate button can point straight
at it and no donor ever has to know.

---

## 3. Four partner links on the home page are broken

Written with a doubled scheme, `http://https://...`, which resolves to a nonsense
hostname. They appear **eight times** between the logos and the "Visit Website" links.

| Partner | As written |
|---|---|
| Person to Person | `http://https://p2phelps.org/` |
| Community Fund of Darien | `http://https://www.communityfunddarien.org/` |
| Charter Communications | `http://https://corporate.charter.com/` |
| Sacred Heart University | `http://https://www.sacredheart.edu/academics/...` |

**How it was checked.** All fourteen partner URLs were requested. Ten returned 200 or 403,
a 403 being bot protection rather than a dead site. The only four that failed were exactly
these four. The doubled scheme was then confirmed in the live page source.

These are funders and partners. Broken links to them are the kind of thing a board member
notices.

---

## 4. The scholarship contact link emails a different person than it names

On the Peace Basketball League page, the scholarship line reads:

> "Scholarships available. Please contact Daniel Ernst at 203.487.0986 or
> jbasketball@stamfordjcc.org."

The link displays `jbasketball@stamfordjcc.org`. Its `mailto:` is
**`alewin@stamfordjcc.org`**.

A family asking about a scholarship therefore emails an address other than the one on
screen. That may be deliberate, if one person now covers that inbox, but it should be
deliberate rather than accidental.

**How it was checked.** Read directly from the live page source. It is the only `mailto:`
on that page, and shown text and href disagree.

---

## 5. A public navigation link leads to a sign-in wall

The Peace Basketball page links to "Summer League page." That page
(`/page/show/8561799-2024-summer-league`) returns a **SportsEngine sign-in form**, roughly
245 characters, rather than any content.

A visitor following a public link from a public page is asked to log in.

**How it was checked.** Fetched 2026-09-01. Confirmed independently by a second pass that
recorded it as an error rather than guessing at what sits behind it.

---

## 6. The Boys League page cannot tell a parent which season they are registering for

The page advertises the **2025-2026 SPBL Season, November 22 to March 8**, a season that
finished in March 2026. Alongside it sits pricing with an **"Early Bird: thru Sept. 12"**
deadline, which reads as current.

Checked on 1 September 2026. A parent arriving today cannot tell whether they are looking
at last season's page or this season's dates.

Either the year label or the deadline is stale. Only Andy can say which.

---

## 7. The mailing list signup is broken

The "Join Our Mailing List" box on the home and Beyond Limits pages displays **"MailChimp
is currently unavailable. Please check back later."**

Someone who is curious but not ready to enrol currently has no way to hear from you.

---

## Something that is ours, not theirs

The footer we built carries a **"Media consent"** link. That phrase appears in **none** of
the 725 inventory rows from the old site. We added it, it has no destination, and it has
no source. It should either be removed or given a real document.

Recorded here so it is not mistaken for one of Andy's problems.

### The website and the enrollment assistant disagree about price

The enrollment assistant we built says **"Free, one-on-one math & science help"** and
**"at little or no cost to your family"**.

The website says **"Tutoring fees are on a sliding scale and are substantially
subsidized"**.

Both are handed to Andy in the same package. A parent reads "subsidized fees" on the
site, clicks through, and is told it is free.

**Decided 2026-09-01 (Dan): the website stays as it is, and the gap goes to Andy.** The
site's wording is sourced from his own marketing materials. The assistant's "free" is not
sourced from any document we hold, and facts file rule 4 says an unestablished value
ships as a chip rather than an assertion. Overstating cost-free access is the worst thing
on this site to get wrong: a parent told "free" who is later billed has been misled by us.

This is already question 18 in the client findings document, which calls it the question
that changes the most. It now has a second reason to be answered.

---

*Findings 1 and 2 were established before 2026-09-01. Findings 3 to 6 came out of the
inventory work on 2026-09-01. Finding 7 was recorded when the mailing list decision was
made on 2026-08-31.*
