"""Find places where the client's own site contradicts itself.

Runs over every verified row from all three inventory rounds, 969 of them, and
looks for the same fact asserted with two different values.

Why a script and not a model: the whole point is exactness. A model reading 969
rows produces plausible contradictions. This produces only real ones, each with
the row ids and the literal strings, so every claim in the client document can be
checked in ten seconds against the inventory.

It reports; it changes nothing. Judging which value is right is a human job, and
in most cases only the client can settle it.

Usage:
    python contradiction-sweep.py
"""
import io
import json
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROUNDS = ['old-site-inventory.json', 'old-site-inventory-2.json',
          'old-site-inventory-3.json']

# Each probe is: label, regex, how to normalise the captured value, and a
# REQUIRED subject term that must appear in the same row.
#
# The subject requirement is the whole trick. A first version without it reported
# four contradictions and three were false. It grouped the Foundation's 2008
# founding with Beyond Limits' 2013, with Stamford Achieves' 2004 out of
# Sklover's biography, and with a board member's company founded in 2016. It also
# grouped the tutoring programme's grades 4-10 with the basketball league's 1-8
# and AAU's 3-11, which are three different programmes serving different ages.
#
# A tool that reports false contradictions to a client is worse than no tool.
PROBES = [
    ('Beyond Limits student count',
     r'\b(\d{3})\s*\+?\s*(?:enrolled\s+)?students?\b',
     lambda m: m.group(1),
     r'Beyond Limits'),

    ('Beyond Limits grade range',
     r'\b(\d{1,2})(?:st|nd|rd|th)?\s*(?:through|thru|to|-)\s*'
     r'(\d{1,2})(?:st|nd|rd|th)?\s+grade',
     lambda m: '%s to %s' % (m.group(1), m.group(2)),
     r'Beyond Limits|tutoring and informal mentoring'),

    ('Beyond Limits grade range',
     r'\bgrades?\s+(\d{1,2})\s*(?:through|thru|to|-)\s*(\d{1,2})\b',
     lambda m: '%s to %s' % (m.group(1), m.group(2)),
     r'Beyond Limits|tutoring and informal mentoring'),

    ('Beyond Limits free or reduced lunch rate',
     r'\b(?:over\s+)?(\d{2}(?:\.\d)?)\s*(?:percent|%)\s+of\s+(?:our\s+)?participants',
     lambda m: m.group(1) + '%',
     r'Beyond Limits|subsidiz'),

    ('Beyond Limits founding year',
     r'\b(?:launched|established)\s+in\s+(?:late\s+)?(\d{4})',
     lambda m: m.group(1),
     r'Beyond Limits'),

    ('Beyond Limits founding year',
     r'\bIn (\d{4}),\s+Andy Sklover co-founded',
     lambda m: m.group(1),
     r'Beyond Limits'),

    ('Kriftcher career length',
     r'\b(\d{2})[- ]year\s+(?:Wall Street|career in financial services)',
     lambda m: m.group(1) + ' years',
     r'Kriftcher'),

    ('Stamford Peace founding year',
     r'Stamford Peace was founded in (\d{4})',
     lambda m: m.group(1),
     r'Stamford Peace'),

    ('young people reached',
     r'more than ([\d,]+) young people',
     lambda m: m.group(1).replace(',', ''),
     r'Stamford Peace'),
]

# Facts that should carry exactly one value across the whole site. The email
# probe is scoped to the Foundation's own domain: the stamfordjcc.org addresses
# on the basketball league page belong to JCC staff and are not a contradiction.
SINGLETONS = [
    ('EIN', r'EIN\s*([\d-]{9,12})'),
    ('street address', r'(\d{3}\s+Long Ridge Road)'),
    ('Foundation email', r'\b([A-Za-z0-9._%+-]+@peaceyouthct\.org)\b'),
]

# Deliberately NOT probed: phone numbers. A first version reported six "values"
# and every one was noise. Three were formatting variants of the same number,
# "203-588-9020" and "(203) 588-9020" and a capture artifact. Two were JCC staff
# on the basketball league page. The last was 203-588-9023, which is a second
# real Foundation line rather than a disagreement: 9020 is the Foundation and
# 9023 appears only against Andy Sklover. Two phone numbers is not a
# contradiction, and a probe that cannot tell the difference does not belong
# in a document handed to a client.


def load():
    rows = []
    for fn in ROUNDS:
        p = os.path.join(HERE, fn)
        if not os.path.exists(p):
            print('skipping missing %s' % fn)
            continue
        for r in json.load(io.open(p, encoding='utf-8')):
            rows.append(r)
    return rows


def page_of(rid):
    return str(rid).split('-')[0]


def main():
    rows = load()
    usable = [r for r in rows if r.get('type') not in ('image', 'error')]
    print('rows loaded: %d   usable: %d' % (len(rows), len(usable)))
    print()

    claims = defaultdict(lambda: defaultdict(list))

    for r in usable:
        c = r.get('content') or ''
        for label, pat, norm, subject in PROBES:
            if not re.search(subject, c, re.I):
                continue
            for m in re.finditer(pat, c, re.I):
                snip = re.sub(r'\s+', ' ', c[max(0, m.start() - 58):m.end() + 58]).strip()
                claims[label][norm(m)].append((r['id'], snip))

    for label, pat in SINGLETONS:
        for r in usable:
            c = r.get('content') or ''
            for m in re.finditer(pat, c):
                val = m.group(0) if m.lastindex and m.lastindex > 1 else m.group(1)
                snip = re.sub(r'\s+', ' ', c[max(0, m.start() - 48):m.end() + 48]).strip()
                claims[label][val].append((r['id'], snip))

    conflicts = {k: v for k, v in claims.items() if len(v) > 1}
    agreed = {k: v for k, v in claims.items() if len(v) == 1}

    if conflicts:
        print('=' * 76)
        print('CONTRADICTIONS: the same fact asserted two or more ways')
        print('=' * 76)
        for label in sorted(conflicts):
            vals = conflicts[label]
            print()
            print('## %s  --  %d values' % (label, len(vals)))
            for val in sorted(vals, key=lambda v: -len(vals[v])):
                hits = vals[val]
                pages = sorted({page_of(i) for i, _ in hits})
                print('   %-14s %2d row(s)   on: %s'
                      % ('"%s"' % val, len(hits), ', '.join(pages)))
                for rid, snip in hits[:2]:
                    print('       [%s] ...%s...' % (rid, snip[:100]))

    print()
    print('=' * 76)
    print('CONSISTENT: asserted the same way everywhere it appears')
    print('=' * 76)
    for label in sorted(agreed):
        val = list(agreed[label])[0]
        n = len(agreed[label][val])
        print('   %-38s "%s"  (%d rows)' % (label, val[:30], n))

    print()
    print('%d contradictions, %d facts consistent.' % (len(conflicts), len(agreed)))
    print()
    print('Every value above is a literal string from a verified inventory row.')
    print('Nothing is inferred. A probe that finds nothing is reported nowhere, so')
    print('absence here is not evidence of consistency: it means no probe covers it.')
    return 0


sys.exit(main())
