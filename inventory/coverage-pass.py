"""First pass of the coverage check: what from the old site is already in the new one.

Mechanical only. It answers one question per row: does this exact text appear
anywhere in the new site? That yields `carried_verbatim` with no judgement involved.

Everything it cannot match is left as `unmatched` for a human pass. Unmatched does
NOT mean missing: the content may have been reworded, merged, moved, or deliberately
dropped. Deciding which is the part a script must not do.

Writes coverage.json keyed by inventory id. Never edits the inventory.
"""
import io, json, os, re, sys, unicodedata
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
INV = os.path.join(HERE, 'old-site-inventory.json')
OUT = os.path.join(HERE, 'coverage.json')

PAGES = ['index.html', 'beyond-limits.html', 'tutoring.html', 'sponsorship.html',
         'donate.html', 'about.html', 'start.html']


def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in [('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'),
                 ('–', '-'), ('—', '-'), (' ', ' ')]:
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()


def visible_text(html):
    html = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', ' ', html, flags=re.S | re.I)
    html = re.sub(r'<[^>]+>', ' ', html)
    return norm(html)


def main():
    rows = json.load(io.open(INV, encoding='utf-8'))

    new = {}
    for p in PAGES:
        fp = os.path.join(SITE, p)
        if os.path.exists(fp):
            new[p] = visible_text(io.open(fp, encoding='utf-8').read())
    if not new:
        print('no new-site pages found'); return 1
    allnew = ' || '.join(new.values())

    # Old-site duplicates: identical content across pages counts once for judging
    # coverage, but every row still gets a verdict.
    by_content = {}
    for r in rows:
        by_content.setdefault(norm(r['content']), []).append(r['id'])

    cov, stats = {}, Counter()
    for r in rows:
        rid, c = r['id'], norm(r['content'])
        probe = c.split(' -> ')[0].strip()

        if r.get('type') in ('image', 'error') or r.get('verbatim') is not True:
            cov[rid] = {'status': 'needs_review', 'new_location': '',
                        'reason': 'not a verbatim quote, judge by hand'}
            stats['needs_review'] += 1
            continue
        if len(probe) < 12:
            cov[rid] = {'status': 'needs_review', 'new_location': '',
                        'reason': 'too short to match reliably'}
            stats['needs_review'] += 1
            continue

        where = [p for p, t in new.items() if probe in t]
        if where:
            cov[rid] = {'status': 'carried_verbatim',
                        'new_location': ', '.join(where), 'reason': ''}
            stats['carried_verbatim'] += 1
        else:
            cov[rid] = {'status': 'unmatched', 'new_location': '',
                        'reason': 'no exact match in the new site'}
            stats['unmatched'] += 1

    dupes = {k: v for k, v in by_content.items() if len(v) > 1}
    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(cov, indent=1))

    print('inventory rows: %d' % len(rows))
    print('unique content strings: %d  (%d appear on more than one old page)'
          % (len(by_content), len(dupes)))
    print()
    for k in ('carried_verbatim', 'unmatched', 'needs_review'):
        print('  %-18s %4d  %5.1f%%' % (k, stats[k], 100.0 * stats[k] / len(rows)))
    print()
    print('wrote', os.path.basename(OUT))
    print()
    print('NOTE: "unmatched" is not "missing". It means no exact string match, which')
    print('also covers reworded, merged, moved and deliberately dropped content.')
    print('Those verdicts come next and are not a script\'s call.')
    return 0


sys.exit(main())
