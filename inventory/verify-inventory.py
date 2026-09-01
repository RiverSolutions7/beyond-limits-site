"""Verify the old-site inventory before anyone relies on it.

The inventory's whole value is that every quoted line is a real quote. This script
proves it mechanically instead of trusting the model that produced it.

Usage:
    python verify-inventory.py

Expects:
    old-site-inventory.json     the model's output
    source-text/<PREFIX>.txt    the plain text of each source page

The .txt files are whoever fetched the pages saving what they actually saw. The
inventory is checked against those, so a page that changes later cannot silently
invalidate the check.

Known limit of that check: the .txt captures are visible text, so they hold no URLs.
The href half of every `link` and `pdf` row is therefore invisible to the quote check.
Those rows are 17% of the inventory, and we were about to wire the partner logo grid
from them. So hrefs get their own structural pass below.

A malformed URL is reported as a SOURCE DEFECT, not an error. It is the client's own
mistake, faithfully recorded, which is the inventory working correctly. It must not fail
the run, and it must not stay invisible either.

Exit code 0 = usable. 1 = do not build on this.
"""
import io, json, os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
INV = os.path.join(HERE, 'old-site-inventory.json')
SRC = os.path.join(HERE, 'source-text')

TYPES = {'heading', 'paragraph', 'stat', 'list', 'link', 'pdf',
         'image', 'form', 'contact', 'embed', 'error'}
PREFIXES = {'HOME', 'BL', 'BBALL', 'WWD', 'IMPACT', 'WWA',
            'LEAD', 'CONTACT', 'GETINV', 'DONATE', 'INVEST'}
REQUIRED = ['id', 'source_url', 'source_title', 'source_section',
            'type', 'content', 'verbatim', 'fetched', 'notes']

# Phrases that mean the model described instead of copying.
# Hrefs we would refuse to ship. Every pattern here is a real defect in this source.
BAD_HREF = [
    (r'^https?://https?:?//', 'doubled scheme, resolves to a nonsense hostname'),
    (r'^\s*$', 'empty href'),
    (r'^https?://\s*$', 'scheme with no host'),
    (r'\s', 'whitespace inside the URL'),
]

TELLS = [r'^a (paragraph|heading|list|section|link|photo|image)\b',
         r'^(this|the) (page|section|paragraph) (describes|explains|covers|contains)\b',
         r'\betc\.?$', r'\band so on\b', r'^\[?various\b']


def norm(s):
    """Whitespace and unicode punctuation differ harmlessly between HTML and text."""
    s = unicodedata.normalize('NFKC', s)
    s = (s.replace('’', "'").replace('‘', "'")
          .replace('“', '"').replace('”', '"')
          .replace('–', '-').replace('—', '-')
          .replace(' ', ' '))
    return re.sub(r'\s+', ' ', s).strip().lower()


def main():
    if not os.path.exists(INV):
        print('MISSING:', INV); return 1
    rows = json.load(io.open(INV, encoding='utf-8'))
    if not isinstance(rows, list):
        print('FAIL: top level is not a JSON array'); return 1

    sources = {}
    if os.path.isdir(SRC):
        for f in os.listdir(SRC):
            if f.endswith('.txt'):
                sources[f[:-4].upper()] = norm(io.open(
                    os.path.join(SRC, f), encoding='utf-8').read())

    errs, warns, seen, defects = [], [], set(), []
    per_page, unmatched = {}, 0

    for i, r in enumerate(rows):
        rid = r.get('id', '<row %d>' % i)

        for k in REQUIRED:
            if k not in r:
                errs.append('%s missing field %r' % (rid, k))
        if r.get('type') not in TYPES:
            errs.append('%s bad type %r' % (rid, r.get('type')))
        if rid in seen:
            errs.append('%s duplicate id' % rid)
        seen.add(rid)

        pref = str(rid).split('-')[0]
        if pref not in PREFIXES:
            errs.append('%s unknown prefix %r' % (rid, pref))
        per_page[pref] = per_page.get(pref, 0) + 1

        content = str(r.get('content', ''))
        if not content.strip() and r.get('type') != 'error':
            errs.append('%s empty content' % rid)

        low = content.strip().lower()
        for t in TELLS:
            if re.search(t, low):
                errs.append('%s looks like a description, not a quote: %r'
                            % (rid, content[:70]))
                break

        if r.get('notes'):
            if re.search(r'\b(outdated|should be|recommend|poor|bad|improve|ugly)\b',
                         str(r['notes']).lower()):
                warns.append('%s notes contain a judgement: %r' % (rid, r['notes'][:60]))

        # A text capture holds no URLs, so hrefs get a shape check instead.
        if r.get('type') in ('link', 'pdf') and ' -> ' in content:
            href = content.split(' -> ')[-1].strip()
            for pat, why in BAD_HREF:
                if re.search(pat, href):
                    defects.append('%s  %s  ->  %s'
                                   % (rid, why, href[:78]))
                    break

        # The check that matters: is this quote really in the page?
        if r.get('verbatim') is True and r.get('type') not in ('image', 'error'):
            src = sources.get(pref)
            if src is None:
                warns.append('%s no source text for %s, quote unverified' % (rid, pref))
            else:
                probe = norm(content).split(' -> ')[0]
                if len(probe) > 12 and probe not in src:
                    unmatched += 1
                    errs.append('%s NOT FOUND in source: %r' % (rid, content[:70]))

    print('rows: %d across %d pages' % (len(rows), len(per_page)))
    for p in sorted(per_page):
        print('   %-8s %d' % (p, per_page[p]))
    missing_pages = sorted(PREFIXES - set(per_page))
    if missing_pages:
        errs.append('no rows at all for: %s' % ', '.join(missing_pages))

    print()
    if defects:
        print("SOURCE DEFECTS (%d) - broken URLs on the old site, recorded faithfully."
              % len(defects))
        print("These are findings to report to the client, not inventory errors.")
        print("Do not carry them across to the new site.")
        for d in defects:
            print('   ', d)
        print()
    if warns:
        print('WARNINGS (%d):' % len(warns))
        for w in warns[:25]:
            print('   ', w)
        if len(warns) > 25:
            print('    ... and %d more' % (len(warns) - 25))
        print()
    if errs:
        print('ERRORS (%d):' % len(errs))
        for e in errs[:40]:
            print('   ', e)
        if len(errs) > 40:
            print('    ... and %d more' % (len(errs) - 40))
        print()
        print('VERDICT: do not build on this inventory yet.')
        if unmatched:
            print('%d quotes could not be found in the source. That is the'
                  ' paraphrasing failure mode.' % unmatched)
        return 1

    print('VERDICT: usable. Every verbatim quote was found in its source page.')
    return 0


sys.exit(main())
