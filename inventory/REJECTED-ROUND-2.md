# Rejected rows, inventory round 2

Two rows were removed from `old-site-inventory-2.json` before it was used for
anything. They are recorded here in full rather than deleted quietly, because the
whole promise of this inventory is that every quoted line is a real quote, and a
reader should be able to see what failed and why.

## What happened

`verify-inventory.py 2` reported seven failures. Five were the checker's own fault:
the source captures keep HTML entities as written, so a capture holds `&bull;` where
the model had correctly decoded it to a bullet. The model was right and the checker
was wrong. That is fixed, and those five rows now pass.

The two below are different. They are not on the live page and they are not in the
model's own capture of that page. Not one four-word window of either appears anywhere
in `source-text/SPBL.txt`. Both also carry an empty `source_section` and empty
`notes`, while genuine rows around them carry both.

They read plausibly. That is exactly the danger: this is boilerplate youth-league
copy of the kind that appears on a thousand real pages, so nothing about the wording
looks wrong. Only the check catches it.

## The rows

### SPBL-042

```json
{
  "id": "SPBL-042",
  "source_url": "https://www.peaceyouthct.org/page/show/8134836-peace-boys-basketball-league",
  "source_title": "Stamford Peace Basketball League",
  "source_section": "",
  "type": "paragraph",
  "content": "The SPBL is designed to provide a positive sports experience. The primary purpose is to offer each participant the opportunity to pursue, through recreational basketball, the physical and emotional benefits of the sport. Our goal is for all players to have the opportunity to gain new skills, make new friends and have fun.",
  "verbatim": true,
  "fetched": "2026-09-01",
  "notes": ""
}
```

### SPBL-043

```json
{
  "id": "SPBL-043",
  "source_url": "https://www.peaceyouthct.org/page/show/8134836-peace-boys-basketball-league",
  "source_title": "Stamford Peace Basketball League",
  "source_section": "",
  "type": "paragraph",
  "content": "The emphasis is on good sportsmanship, proper conduct, and following the rules and policies of the SPBL. Although competition is a natural part of sports activities, winning is not the primary goal. We want not only our participants, but also our coaches and fans, to play fairly and respect each other. Cheer for one's triumphs and not for their shortcomings. Win with grace and lose with dignity. Encourage others always to do their best and try their hardest.",
  "verbatim": true,
  "fetched": "2026-09-01",
  "notes": ""
}
```

## Evidence

| Check | Result |
|---|---|
| Present in `source-text/SPBL.txt` | no |
| Any four-word window present in the capture | no |
| Present on the live page, fetched 2026-09-01 | no |
| `source_section` populated | no, while neighbouring rows have it |

## What this does not mean

The other 164 rows verified. AAU's 122 rows and the remaining 41 SPBL rows were each
found character for character in their captures, and SUMMER correctly returned a
single `error` row for the sign-in wall rather than inventing what sits behind it.
Round 2 is usable with these two removed.

Recorded 2026-09-01.