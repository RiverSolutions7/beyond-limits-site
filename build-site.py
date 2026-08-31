"""Export step: turn Claude Design source pages into the delivery folder.

Two jobs:
  1. Strip design-system scaffolding that must never reach the client.
  2. Wire the onboarding assistant into the exported pages.

The wiring lives here rather than in the design sources so it is declarative,
reviewable in one place, and survives a re-export from Claude Design.

Re-runnable. Operates on beyond-limits-site/ in place and self-verifies.
"""
import io, os, re, sys

# The repo root is the site root: this script lives beside the pages it processes.
OUT = os.path.dirname(os.path.abspath(__file__))

PAGES = ['index.html', 'beyond-limits.html', 'tutoring.html',
         'sponsorship.html', 'donate.html', 'about.html', 'start.html']

ASSISTANT = 'https://vastlyresilient.github.io/beyond-limits-enrollment/'

# The canonical-reference banner the design system injects after <body>.
BANNER = re.compile(
    r'<div style="background:#FDF3DA;border-bottom:1px solid #B77F07;[^"]*">'
    r'.*?Canonical rendered reference.*?</div></div>\s*',
    re.S)

HERO_OLD = ('<a class="btn btn-primary btn-lg" href="tutoring.html">Find tutoring for your student</a>',
            '<a class="btn btn-secondary btn-lg" href="sponsorship.html">Sponsor a student</a>')
HERO_NEW = ('<a class="btn btn-primary btn-lg" href="' + ASSISTANT + '">Start enrollment</a>',
            '<a class="btn btn-secondary btn-lg" href="tutoring.html">See how it works</a>')

SLOT_OLD = '<a class="btn btn-primary btn-lg" href="#">Tell us about your student</a>'
SLOT_NEW = '<a class="btn btn-primary btn-lg" href="' + ASSISTANT + '">Tell us about your student</a>'

WIRING = [
    # Home hero: primary enters enrollment directly, secondary explains first.
    ('index.html', HERO_OLD[0], HERO_NEW[0]),
    ('index.html', HERO_OLD[1], HERO_NEW[1]),
    # Dead assistant slots become the real assistant. Note index uses href="#top"
    # and sponsorship omits btn-lg, so these are matched literally, not by pattern.
    ('index.html', '<a class="btn btn-primary btn-lg" href="#top">Tell us about your student</a>', SLOT_NEW),
    ('tutoring.html', SLOT_OLD, SLOT_NEW),
    ('donate.html', SLOT_OLD, SLOT_NEW),
    # Highest-intent button on the site.
    ('tutoring.html', 'href="#enroll">Start a tutoring inquiry</a>',
                      'href="' + ASSISTANT + '">Start a tutoring inquiry</a>'),
    # This slot promised a guided flow the assistant cannot deliver for sponsors.
    ('sponsorship.html', '<a class="btn btn-primary" href="#">Tell us about your business</a>',
                         '<a class="btn btn-primary" href="#sponsorship">Talk to our team</a>'),
]

# The assistant's own welcome screen says "About 4 minutes". Our buttons said two.
# Align the promise with the tool so the first screen does not contradict the button.
TIMING = ('Takes about two minutes. No account needed.',
          'Takes about four minutes. No account needed.')

# Nav and drawer "Get Involved" becomes the router on every page except the router itself.
# Matches any attributes sitting between the href and the tag close (Sponsorship carried
# aria-current="page" there, which is also now wrong: the router is the Get Involved
# destination, so Sponsorship is no longer "the Get Involved page").
GET_INVOLVED = re.compile(r'href="[^"]*"((?:\s+[a-zA-Z-]+="[^"]*")*)\s*>Get Involved</a>')
ARIA_ON_GI = re.compile(r'(href="start\.html")\s+aria-current="page"')

# On the router itself, Get Involved points at its own choices and is the current page.
GI_ON_ROUTER = ('href="#start">Get Involved</a>',
                'href="#choices" aria-current="page">Get Involved</a>')


def main():
    changed, wired = [], []
    for p in PAGES:
        path = os.path.join(OUT, p)
        if not os.path.exists(path):
            print('MISSING', p)
            continue
        s = io.open(path, encoding='utf-8').read()
        new = s

        new, n1 = BANNER.subn('', new)
        new, n2 = re.subn(r'<!--\s*@dsCard[^>]*-->\s*', '', new)
        # Rule 3 of the link convention: no verified destination means a bare '#'.
        # The placeholder must never ship as an href; clicking it shows our scaffolding.
        new, n3 = re.subn(r'href="PARENT-ONBOARDING-ASSISTANT-URL-PENDING"', 'href="#"', new)

        if p != 'start.html':
            new, n4 = GET_INVOLVED.subn(r'href="start.html"\1>Get Involved</a>', new)
            new = ARIA_ON_GI.sub(r'\1', new)
        else:
            n4 = new.count(GI_ON_ROUTER[0])
            new = new.replace(*GI_ON_ROUTER)
            # The router was generated from about.html, so its About link still
            # self-references (#top) and carries the current-page marker. Point it at
            # the real About page and drop the marker: only one nav item may be current.
            new = re.sub(r'href="#top"\s+aria-current="page"(\s*)>About</a>',
                         r'href="about.html"\1>About</a>', new)

        hits = 0
        for pg, find, repl in WIRING:
            if pg == p and find in new:
                new = new.replace(find, repl)
                hits += 1

        # Only correct the timing note on pages that actually enter the assistant.
        if ASSISTANT in new and TIMING[0] in new:
            new = new.replace(TIMING[0], TIMING[1])

        if n1 or n2 or n3:
            changed.append('%s (banner:%d dsCard:%d assistantHref:%d)' % (p, n1, n2, n3))
        if hits or n4:
            wired.append('%s (buttons:%d getInvolved:%d)' % (p, hits, n4))
        if new != s:
            io.open(path, 'w', encoding='utf-8').write(new)

    print('stripped:', changed if changed else 'nothing (already clean)')
    print('wired:   ', wired if wired else 'nothing (already wired)')

    bad = []
    for p in PAGES:
        s = io.open(os.path.join(OUT, p), encoding='utf-8').read()
        for marker in ['Canonical rendered reference', '@dsCard', 'superseded',
                       'pages-home.html', 'Pages file disagrees', 'href="PARENT-ONBOARDING']:
            if marker in s:
                bad.append('%s contains %r' % (p, marker))
    print('leaks:   ', bad if bad else 'none')

    n_assist = sum(io.open(os.path.join(OUT, p), encoding='utf-8').read().count(ASSISTANT)
                   for p in PAGES)
    print('assistant entry points:', n_assist)
    return 1 if bad else 0


sys.exit(main())
