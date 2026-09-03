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
         'sponsorship.html', 'donate.html', 'about.html', 'start.html',
         'impact.html', 'basketball.html']

ASSISTANT = 'https://vastlyresilient.github.io/beyond-limits-enrollment/'

# Photograph patterns.
#
# The nine pages each hand-authored their own <style> block and no two of them
# match, so the seven patterns have exactly one home: patterns.css. This step
# inlines it into every page between the markers below, replacing whatever was
# there before, and the self-check at the bottom fails the build if any page is
# missing it or carrying a stale copy. Edit patterns.css, run this, done.
#
# Inlined rather than <link>ed because this is a static site on GitHub Pages and
# a blocking request for 4KB costs more than the duplication does.
PATTERNS_FILE = 'patterns.css'
PAT_START = '/* PATTERNS:START -- generated from patterns.css, do not edit here */'
PAT_END = '/* PATTERNS:END */'


def patterns_block():
    """The exact text every page must carry, markers included."""
    css = io.open(os.path.join(OUT, PATTERNS_FILE), encoding='utf-8').read().strip()
    return '%s\n%s\n%s' % (PAT_START, css, PAT_END)

# Keep the work-in-progress site out of search results.
#
# A robots.txt does NOT work here. Crawlers only read robots.txt at the root of a
# domain, and this deploys to a project subpath (username.github.io/repo/), so ours
# was never being read. A meta tag travels with each page and works at any path.
#
# REMOVE THIS when the site launches for real.
NOINDEX = '<meta name="robots" content="noindex, nofollow">'
CHARSET = '<meta charset="utf-8">'

# Claude Design injects a runtime into every exported page, tagged with
# data-omelette-injected. It is ~20KB per page (about 43% of this site's HTML) and
# does nothing outside a Claude Design frame: it posts messages to claude.ai parent
# frames, handles preview theming, and exposes a window.claude API.
#
# It also sets html,body{background:transparent}, which is right for a preview frame
# and wrong for a real site.
#
# The pages' own scripts (count-up stats, sticky header, drawer toggle) are separate
# untagged <script> blocks and are NOT touched by this.
OMELETTE = re.compile(
    r'<(script|style)\b[^>]*\bdata-omelette-injected\b[^>]*>.*?</\1>\s*',
    re.S)

# Stat safety net.
#
# The count-up script zeroes every [data-to] figure on load and only restores the
# real number when an IntersectionObserver fires at 50% visibility. That fails
# UNSAFE: if the observer never delivers, the zeros are permanent and the homepage
# reads "0 students". Observers and rAF do not run in a hidden or heavily throttled
# tab, which is exactly what a background tab is.
#
# This net snaps a figure to its real value only when it is BOTH on screen AND still
# zero, so a normal scroll still gets the animation and an off-screen figure is left
# alone. Runs on scroll, on the tab becoming visible, and once after 3s.
STAT_NET = """<script>
/* Stat safety net: never leave a real figure showing 0 on screen. */
(function(){
function f(v,d,s){return (d?v.toFixed(d):Math.round(v).toLocaleString('en-US'))+(s||'')}
function snap(){
  var n=document.querySelectorAll('[data-to]');
  for(var i=0;i<n.length;i++){var e=n[i],t=parseFloat(e.dataset.to);
    if(!t||parseFloat(e.textContent)!==0)continue;
    var r=e.getBoundingClientRect();
    if(r.bottom>0&&r.top<(window.innerHeight||0))
      e.textContent=f(t,parseInt(e.dataset.dec||'0',10),e.dataset.suffix||'');}
}
var q=false;
function later(){if(q)return;q=true;setTimeout(function(){q=false;snap()},250)}
window.addEventListener('scroll',later,{passive:true});
document.addEventListener('visibilitychange',function(){if(!document.hidden)later()});
setTimeout(snap,3000);
})();
</script>
"""

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

# A confirm chip ANNOTATES a stated value. It must never REPLACE one.
#
# Two sentences had the chip standing in for the launch year, which left a hole:
#   "Launched in [confirm launch year] as a program of the Stamford Peace..."
# That is a broken sentence on a live page, and it misapplies the rule. The facts
# file says CONTESTED means publish the value WITH a chip, not omit it.
#
# 2014 is the better-supported figure: it is what the live Beyond Limits page says
# in the very sentence ours is adapted from ("Launched in 2014 as a program of the
# Stamford Peace Youth Foundation..."), and the deck says "since inception in 2014".
# Only one other page says 2013, which is why the chip stays until Andy confirms.
CHIP_FILL = [
    ('beyond-limits.html', 'Launched in <span class="chip"', 'Launched in 2014 <span class="chip"'),
    ('about.html', 'launched in <span class="chip"', 'launched in 2014 <span class="chip"'),
]

# The open questions, and why this file now depends on a document outside the repo.
#
# On 2026-09-03 all 41 gold confirm chips came out of the nine pages. They were the
# loudest thing on a page after a photograph and nothing about the design could be
# judged with them there.
#
# But the chips were also the site's visible marking of its own uncertainty. Without
# them the page states "Launched in 2014" flatly while we remain unsure between 2013
# and 2014, and transparency with Andy was a stated objective of this project. The
# questions did not stop existing; they stopped being visible.
#
# So they moved to beyond-limits-open-questions.md, and this check makes that move
# safe: every question a chip used to carry must still be in that document, or the
# build fails. The only real failure mode is a question going quietly missing, and
# this is what makes that impossible.
#
# The document lives one directory UP, outside this repo, deliberately. This repo
# publishes to GitHub Pages, and a list of everything we are unsure about is not
# something to serve to the public web. The build depending on a file it does not
# publish is the price of that, and it is the right trade.
QUESTIONS = os.path.join(os.path.dirname(OUT), 'beyond-limits-open-questions.md')

# The 20 distinct questions the 41 chips were carrying, by their exact chip label.
# Several labels ask the same thing in different words, which is why the document
# has 16 entries rather than 20: an entry declares every label it answers in an
# HTML comment, and this list is checked against those declarations.
RETIRED_CHIPS = [
    'confirm grades served',
    'confirm one agreed count',
    'confirm count',
    'confirm %',
    'confirm eligibility %',
    'confirm whether this is the same figure as the 90% on the home page',
    'confirm on-site % (88 vs 90)',
    'confirm launch year',
    'confirm standard fee',
    'confirm subsidized fee',
    'confirm background checks and room supervision',
    'confirm online availability',
    'confirm what this level funds',
    'confirm what these fund',
    'confirm founders',
    'confirm these two portraits are matched to the right names',
    'confirm email',
    'confirm the four paths',
    'confirm level list',
    'confirm reassurance line',
]

# An entry declares the labels it covers as: <!-- chips: label one, label two -->
DECLARED = re.compile(r'<!--\s*chips:\s*(.+?)\s*-->')
# Any chip still standing in the markup, whatever class it carries. Nine of the
# original 41 were styled inline rather than with class="chip", so matching on the
# class alone would have missed them.
CHIP_IN_MARKUP = re.compile(r'>(confirm [^<]+)</span>')

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

        # Insert the noindex meta once, immediately after the charset declaration.
        n0 = 0
        if NOINDEX not in new and CHARSET in new:
            new = new.replace(CHARSET, CHARSET + '\n' + NOINDEX, 1)
            n0 = 1

        new, nO = OMELETTE.subn('', new)
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

        # Restore values that a chip was wrongly standing in for.
        nC = 0
        for pg, find, repl in CHIP_FILL:
            if pg == p and find in new:
                new = new.replace(find, repl); nC += 1

        # Stat safety net, only on pages that actually have count-up figures.
        nS = 0
        if 'data-to=' in new and 'Stat safety net' not in new and '</body>' in new:
            new = new.replace('</body>', STAT_NET + '</body>', 1)
            nS = 1

        # Only correct the timing note on pages that actually enter the assistant.
        if ASSISTANT in new and TIMING[0] in new:
            new = new.replace(TIMING[0], TIMING[1])

        # Inline the photograph patterns, replacing any earlier copy.
        nP = 0
        block = patterns_block()
        if PAT_START in new and PAT_END in new:
            a, b = new.index(PAT_START), new.index(PAT_END) + len(PAT_END)
            if new[a:b] != block:
                new = new[:a] + block + new[b:]
                nP = 1
        elif '</style>' in new:
            new = new.replace('</style>', block + '\n</style>', 1)
            nP = 1

        if n0 or nO or n1 or n2 or n3:
            changed.append('%s (noindex:%d omelette:%d banner:%d dsCard:%d assistantHref:%d)' % (p, n0, nO, n1, n2, n3))
        if hits or n4 or nS or nC or nP:
            wired.append('%s (buttons:%d getInvolved:%d statNet:%d chipFill:%d patterns:%d)' % (p, hits, n4, nS, nC, nP))
        if new != s:
            io.open(path, 'w', encoding='utf-8').write(new)

    print('stripped:', changed if changed else 'nothing (already clean)')
    print('wired:   ', wired if wired else 'nothing (already wired)')

    bad = []
    for p in PAGES:
        s = io.open(os.path.join(OUT, p), encoding='utf-8').read()
        for marker in ['Canonical rendered reference', '@dsCard', 'superseded',
                       'pages-home.html', 'Pages file disagrees', 'href="PARENT-ONBOARDING',
                       'data-omelette-injected', 'window.claude', '__om_api']:
            if marker in s:
                bad.append('%s contains %r' % (p, marker))
    # A chip must never replace a value: catch "in <chip>", "is <chip>", etc.
    dangling = []
    for p in PAGES:
        t = io.open(os.path.join(OUT, p), encoding='utf-8').read()
        for mm in re.finditer(r'(in|of|is|are|about|to|at|for)\s+<span class="chip', t):
            dangling.append('%s: "%s <chip>"' % (p, mm.group(1)))
    if dangling:
        bad.append('chip replacing a value: %s' % '; '.join(dangling))

    # No question may be silently lost. See the RETIRED_CHIPS note above.
    #
    # Two directions, and both matter. Every question the chips used to carry must
    # still be answerable from the questions document; and any chip that ever comes
    # back to the markup must be documented there too, so the document cannot fall
    # behind the pages any more than the pages can fall behind the document.
    declared = set()
    if not os.path.exists(QUESTIONS):
        bad.append('open questions file missing: %s (the chips were removed from the '
                   'pages on the promise that it exists)' % QUESTIONS)
    else:
        md = io.open(QUESTIONS, encoding='utf-8').read()
        for mm in DECLARED.finditer(md):
            declared.update(lab.strip() for lab in mm.group(1).split(','))

        undocumented = [c for c in RETIRED_CHIPS if c not in declared]
        if undocumented:
            bad.append('question dropped from %s: %s'
                       % (os.path.basename(QUESTIONS), '; '.join(undocumented)))

    # A chip that returns must bring its question with it.
    for p in PAGES:
        t = io.open(os.path.join(OUT, p), encoding='utf-8').read()
        for mm in CHIP_IN_MARKUP.finditer(t[t.rindex('</style>'):]):
            if mm.group(1) not in declared:
                bad.append('%s carries an undocumented chip: %r' % (p, mm.group(1)))

    # Every page must carry the noindex meta while this is a work in progress.
    missing_noindex = [p for p in PAGES
                       if NOINDEX not in io.open(os.path.join(OUT, p), encoding='utf-8').read()]
    if missing_noindex:
        bad.append('noindex meta missing from: %s' % ', '.join(missing_noindex))

    # Every page must carry the CURRENT patterns, not a stale copy of them. This is
    # the check that makes one source of truth actually true: edit patterns.css and
    # forget to rebuild, and the build fails instead of nine pages quietly drifting.
    block = patterns_block()
    stale = [p for p in PAGES
             if block not in io.open(os.path.join(OUT, p), encoding='utf-8').read()]
    if stale:
        bad.append('patterns.css missing or stale in: %s' % ', '.join(stale))

    print('leaks:   ', bad if bad else 'none')
    print('noindex: ', 'all %d pages' % len(PAGES) if not missing_noindex else 'MISSING')
    print('questions:', '%d of %d retired chips documented'
          % (sum(1 for c in RETIRED_CHIPS if c in declared), len(RETIRED_CHIPS)))

    n_assist = sum(io.open(os.path.join(OUT, p), encoding='utf-8').read().count(ASSISTANT)
                   for p in PAGES)
    print('assistant entry points:', n_assist)
    return 1 if bad else 0


sys.exit(main())
