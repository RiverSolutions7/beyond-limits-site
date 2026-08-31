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

        if n0 or nO or n1 or n2 or n3:
            changed.append('%s (noindex:%d omelette:%d banner:%d dsCard:%d assistantHref:%d)' % (p, n0, nO, n1, n2, n3))
        if hits or n4 or nS or nC:
            wired.append('%s (buttons:%d getInvolved:%d statNet:%d chipFill:%d)' % (p, hits, n4, nS, nC))
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

    # Every page must carry the noindex meta while this is a work in progress.
    missing_noindex = [p for p in PAGES
                       if NOINDEX not in io.open(os.path.join(OUT, p), encoding='utf-8').read()]
    if missing_noindex:
        bad.append('noindex meta missing from: %s' % ', '.join(missing_noindex))

    print('leaks:   ', bad if bad else 'none')
    print('noindex: ', 'all %d pages' % len(PAGES) if not missing_noindex else 'MISSING')

    n_assist = sum(io.open(os.path.join(OUT, p), encoding='utf-8').read().count(ASSISTANT)
                   for p in PAGES)
    print('assistant entry points:', n_assist)
    return 1 if bad else 0


sys.exit(main())
