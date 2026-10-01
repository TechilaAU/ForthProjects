# -*- coding: utf-8 -*-
"""
Forth Projects static site builder.
Run from the repo root:  python3 _src/build.py
Writes clean-URL pages (folder/index.html) to the repo root, plus sitemap.xml and robots.txt.
"""
import json, os, shutil, html
from content import (SITE, AREAS_SERVED, WHY, PROCESS, SERVICES, SECTORS, LOCATIONS,
                     COMBOS, PROJECTS, INSIGHTS)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = SITE["url"]
SITEMAP = []          # (path, priority)
GENERATED = []        # top-level dirs/files we own, for clean rebuilds

SVC = {s["slug"]: s for s in SERVICES}
SEC = {s["slug"]: s for s in SECTORS}
LOC = {l["slug"]: l for l in LOCATIONS}

esc = html.escape

# ------------------------------------------------------------------ shared bits
MARK = ('<svg class="mark" viewBox="0 0 100 100" aria-hidden="true" focusable="false">'
        '<polygon class="mark-top" points="4,6 96,6 82,30 4,30"/>'
        '<polygon class="mark-low" points="4,38 66,38 52,60 30,60 4,96"/></svg>')

LOGO = (f'<a class="brand" href="/" aria-label="Forth Projects home">'
        f'<span class="brand-word">{MARK}<span class="brand-orth">ORTH</span></span>'
        f'<span class="brand-sub">PROJECTS</span></a>')


def org_schema():
    same = [u for u in (SITE["linkedin"], SITE["instagram"]) if u]
    d = {
        "@context": "https://schema.org",
        "@type": "GeneralContractor",
        "@id": URL + "/#org",
        "name": SITE["name"],
        "url": URL + "/",
        "logo": URL + "/assets/img/forth-logo.svg",
        "image": URL + "/assets/img/og-default.png",
        "slogan": SITE["tagline"],
        "telephone": SITE["phone_e164"],
        "email": SITE["email"],
        "address": {"@type": "PostalAddress", "addressLocality": SITE["locality"],
                    "addressRegion": SITE["region"], "addressCountry": SITE["country"]},
        "areaServed": [{"@type": "City", "name": a} for a in AREAS_SERVED],
        "knowsAbout": [s["name"] for s in SERVICES] + [s["name"] for s in SECTORS],
    }
    if same:
        d["sameAs"] = same
    return d


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": URL + "/#website",
            "url": URL + "/", "name": SITE["name"], "publisher": {"@id": URL + "/#org"}}


def crumbs_schema(crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n,
                                 "item": URL + p} for i, (n, p) in enumerate(crumbs)]}


def faq_schema(faqs):
    import re
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs]}


def service_schema(name, desc, path, areas):
    return {"@context": "https://schema.org", "@type": "Service", "name": name,
            "description": desc, "url": URL + path, "provider": {"@id": URL + "/#org"},
            "areaServed": [{"@type": "City", "name": a} for a in areas],
            "serviceType": name}


def nav():
    svc = "".join(f'<li><a href="/services/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in SERVICES)
    sec = "".join(f'<li><a href="/sectors/{s["slug"]}/">{esc(s["nav"])}</a></li>' for s in SECTORS)
    loc = "".join(f'<li><a href="/locations/{l["slug"]}/">{esc(l["name"])}</a></li>' for l in LOCATIONS)

    def dd(label, key, items, all_href, all_label):
        return (f'<li class="has-dd"><button class="dd-btn" aria-expanded="false" aria-controls="dd-{key}">{label}'
                f'<svg viewBox="0 0 12 8" aria-hidden="true"><path d="M1 1l5 5 5-5"/></svg></button>'
                f'<ul class="dd" id="dd-{key}">{items}<li class="dd-all"><a href="{all_href}">{all_label}</a></li></ul></li>')
    about = ('<li><a href="/about/">About Forth</a></li><li><a href="/our-process/">Our process</a></li>'
             '<li><a href="/safety-and-quality/">Safety and quality</a></li><li><a href="/careers/">Careers</a></li>'
             '<li><a href="/subcontractors/">Subcontractors</a></li>')
    return f'''<header class="site-header">
  <div class="wrap header-in">
    {LOGO}
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav"><span class="sr">Menu</span><span class="bars" aria-hidden="true"></span></button>
    <nav id="site-nav" class="site-nav" aria-label="Main">
      <ul class="nav-list">
        {dd("Services", "svc", svc, "/services/", "All services")}
        {dd("Sectors", "sec", sec, "/sectors/", "All sectors")}
        <li><a href="/projects/">Projects</a></li>
        {dd("Locations", "loc", loc, "/locations/", "All locations")}
        {dd("About", "abt", about, "/capability-statement/", "Capability statement")}
        <li><a href="/insights/">Insights</a></li>
      </ul>
      <a class="btn btn-bronze nav-cta" href="/contact/">Discuss your project</a>
    </nav>
  </div>
</header>'''


def footer():
    svc = "".join(f'<li><a href="/services/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in SERVICES)
    sec = "".join(f'<li><a href="/sectors/{s["slug"]}/">{esc(s["nav"])}</a></li>' for s in SECTORS)
    loc = "".join(f'<li><a href="/locations/{l["slug"]}/">{esc(l["name"])}</a></li>' for l in LOCATIONS)
    social = ""
    if SITE["linkedin"]:
        social += f'<a href="{SITE["linkedin"]}" rel="noopener">LinkedIn</a>'
    if SITE["instagram"]:
        social += f'<a href="{SITE["instagram"]}" rel="noopener">Instagram</a>'
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        {LOGO}
        <p class="foot-tag">Spaces. Built forward.</p>
        <p class="foot-contact"><a href="tel:{SITE["phone_e164"]}">{SITE["phone"]}</a><br><a href="mailto:{SITE["email"]}">{SITE["email"]}</a><br>{SITE["locality"]}, {SITE["region"]}</p>
        <p class="foot-social">{social}</p>
      </div>
      <div class="foot-col"><h2 class="foot-h">Services</h2><ul>{svc}</ul></div>
      <div class="foot-col"><h2 class="foot-h">Sectors</h2><ul>{sec}</ul></div>
      <div class="foot-col"><h2 class="foot-h">Locations</h2><ul>{loc}</ul></div>
      <div class="foot-col"><h2 class="foot-h">Company</h2><ul>
        <li><a href="/about/">About</a></li><li><a href="/projects/">Projects</a></li>
        <li><a href="/our-process/">Our process</a></li><li><a href="/safety-and-quality/">Safety and quality</a></li>
        <li><a href="/insights/">Insights</a></li><li><a href="/careers/">Careers</a></li>
        <li><a href="/subcontractors/">Subcontractors</a></li><li><a href="/capability-statement/">Capability statement</a></li>
        <li><a href="/contact/">Contact</a></li></ul></div>
    </div>
    <div class="foot-base">
      <p>&copy; <span data-year>2026</span> Forth Projects. {SITE["qbcc"]}. {SITE["abn"]}.</p>
      <p><a href="/privacy/">Privacy</a></p>
    </div>
  </div>
</footer>'''


def head(title, desc, path, schemas, noindex=False, og_type="website"):
    canonical = URL + path
    blocks = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
                       for s in schemas)
    robots = '<meta name="robots" content="noindex, follow">' if noindex else \
             '<meta name="robots" content="index, follow, max-image-preview:large">'
    return f'''<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
{robots}
<meta name="theme-color" content="#1E1E1E">
<meta property="og:site_name" content="Forth Projects">
<meta property="og:locale" content="en_AU">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{URL}/assets/img/og-default.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="AU-QLD">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/montserrat-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css">
{blocks}
</head>'''



def relativise(doc, path):
    """Rewrite root-relative href/src to relative paths so the site works from a
    subfolder (GitHub Pages preview) and from the root domain."""
    import re
    if path == "/404/":
        # 404.html is served at any depth, so resolve links from the site root at runtime.
        base = ('<script>(function(){var m=location.pathname.match(/^\\/ForthProjects\\//i);'
                'document.write(\'<base href="\'+(m?m[0]:"/")+\'">\');})();</script>')
        doc = doc.replace("<meta charset=\"utf-8\">", "<meta charset=\"utf-8\">\n" + base, 1)
        return re.sub(r'(href|src)="/(?!/)', r'\1="', doc)
    depth = 0 if path == "/" else len(path.strip("/").split("/"))
    prefix = "../" * depth if depth else "./"
    return re.sub(r'(href|src)="/(?!/)', lambda m: f'{m.group(1)}="{prefix}', doc)

def page(path, title, desc, main, crumbs=None, schemas=None, noindex=False, priority="0.6",
         og_type="website", body_class=""):
    schemas = list(schemas or [])
    schemas = [org_schema()] + ([website_schema()] if path == "/" else []) + \
              ([crumbs_schema(crumbs)] if crumbs else []) + schemas
    doc = (head(title, desc, path, schemas, noindex, og_type) +
           f'\n<body class="{body_class}">\n<a class="skip" href="#main">Skip to content</a>\n' +
           nav() + f'\n<main id="main">\n{main}\n</main>\n' + footer() +
           '\n<script src="/assets/js/site.js" defer></script>\n</body>\n</html>\n')
    doc = relativise(doc, path)
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    if path == "/404/":
        out = os.path.join(ROOT, "404.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    if not noindex and path != "/404/":
        SITEMAP.append((path, priority))


# ------------------------------------------------------------------ components
def breadcrumbs(crumbs):
    items = []
    for i, (n, p) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li aria-current="page">{esc(n)}</li>')
        else:
            items.append(f'<li><a href="{p}">{esc(n)}</a></li>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def nobreak(t):
    import re
    return re.sub(r"(\S+-\S+)", r'<span class="nb">\1</span>', esc(t))


def page_hero(h1, lead, crumbs, cta=True, kicker=None):
    k = f'<p class="hero-kicker">{esc(kicker)}</p>' if kicker else ""
    c = ('<div class="hero-actions"><a class="btn btn-bronze" href="/contact/">Discuss your project</a>'
         f'<a class="btn btn-line" href="tel:{SITE["phone_e164"]}">Call {SITE["phone"]}</a></div>') if cta else ""
    return f'''<section class="phero">
  <div class="phero-slash" aria-hidden="true"></div>
  <div class="wrap">
    {breadcrumbs(crumbs)}
    {k}<h1>{nobreak(h1)}</h1>
    <p class="lead">{esc(lead)}</p>
    {c}
  </div>
</section>'''


def ph(brief, cls=""):
    return f'<figure class="ph {cls}" role="img" aria-label="{esc(brief)}"><figcaption>Image: {esc(brief)}</figcaption></figure>'


def ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>"


def faq_block(faqs, heading="Common questions"):
    qs = "".join(f'<details class="faq"><summary>{esc(q)}</summary><div class="faq-a"><p>{a}</p></div></details>'
                 for q, a in faqs)
    return f'<section class="band"><div class="wrap narrow"><h2>{heading}</h2><div class="faqs">{qs}</div></div></section>'


def why_block(title="Why clients choose Forth"):
    items = "".join(f'<div class="why"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in WHY)
    return f'<section class="band band-dark"><div class="wrap"><h2 class="h-split">{title}</h2><div class="why-grid">{items}</div></div></section>'


def process_block(compact=True):
    steps = "".join(f'<li><span class="step-n">{i+1}</span><h3>{esc(t)}</h3>'
                    f'{"" if compact else f"<p>{esc(d)}</p>"}</li>' for i, (t, d) in enumerate(PROCESS))
    more = '<p class="more"><a class="link" href="/our-process/">See how we work</a></p>' if compact else ""
    return f'''<section class="band band-stone"><div class="wrap">
  <h2>From concept. To completion.</h2>
  <ol class="steps{' steps-full' if not compact else ''}">{steps}</ol>{more}
</div></section>'''


def cta_band(line="This space is moving Forth.", sub="Tell us about your site, your timing and what the space needs to do. We'll come back to you within one business day."):
    return f'''<section class="cta-band">
  <div class="cta-slash" aria-hidden="true"></div>
  <div class="wrap">
    <p class="cta-line">{esc(line)}</p>
    <p class="cta-sub">{esc(sub)}</p>
    <div class="hero-actions"><a class="btn btn-bronze" href="/contact/">Discuss your project</a>
    <a class="btn btn-line" href="tel:{SITE["phone_e164"]}">{SITE["phone"]}</a></div>
  </div>
</section>'''


def index_rows(items):
    """Editorial list of links: name + one-liner."""
    rows = "".join(f'<li><a class="row" href="{href}"><span class="row-name">{esc(n)}</span>'
                   f'<span class="row-desc">{esc(d)}</span><span class="row-arrow" aria-hidden="true">'
                   f'<svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg></span></a></li>'
                   for n, d, href in items)
    return f'<ul class="rows">{rows}</ul>'


def tiles(items):
    t = "".join(f'<li><a class="tile" href="{href}">{ph(img, "ph-tile")}<span class="tile-name">{esc(n)}</span></a></li>'
                for n, img, href in items)
    return f'<ul class="tiles">{t}</ul>'


def chips(items):
    return '<ul class="chips">' + "".join(
        f'<li><a href="{h}">{esc(n)}</a></li>' if h else f'<li><span>{esc(n)}</span></li>' for n, h in items) + "</ul>"


def two_col(left_html, right_html, flip=False):
    return f'<div class="two-col{" flip" if flip else ""}"><div>{left_html}</div><div>{right_html}</div></div>'


# ------------------------------------------------------------------ pages
def build_home():
    svc_rows = index_rows([(s["name"], s["short"], f'/services/{s["slug"]}/') for s in SERVICES])
    sec_tiles = tiles([(s["name"], s["image"], f'/sectors/{s["slug"]}/') for s in SECTORS])
    loc_chips = chips([(l["name"], f'/locations/{l["slug"]}/') for l in LOCATIONS])
    main = f'''<section class="hero">
  <div class="wrap hero-in">
    <div class="hero-copy">
      <h1>Commercial spaces. <span class="br">Built forward.</span></h1>
      <p class="lead">Commercial construction, fit-out, refurbishment and design + construct across Brisbane, the Gold Coast and the Sunshine Coast.</p>
      <div class="hero-actions"><a class="btn btn-bronze" href="/contact/">Discuss your project</a><a class="btn btn-line" href="/projects/">View projects</a></div>
    </div>
  </div>
  <div class="hero-art" aria-hidden="true"><div class="hero-slash"></div><div class="hero-media">{ph("Completed hospitality fit-out, warm evening light")}</div></div>
</section>

<section class="band"><div class="wrap">
  {two_col('<h2>We take spaces, businesses and ideas forward.</h2>',
           '<p class="big">Forth Projects delivers commercial construction and fit-outs with clarity, craftsmanship and purpose. One team plans, prices and builds your project, so you always know where it stands and who is responsible.</p><p><a class="link" href="/about/">About Forth</a></p>')}
</div></section>

<section class="band band-tight"><div class="wrap">
  <h2>What we do</h2>
  {svc_rows}
</div></section>

<section class="band band-stone"><div class="wrap">
  <div class="head-row"><h2>Sectors we build for</h2><a class="link" href="/sectors/">All sectors</a></div>
  {sec_tiles}
</div></section>

{why_block()}

{process_block()}

<section class="band"><div class="wrap">
  {two_col('<h2>Where we build</h2><p>Based in Brisbane and working across South East Queensland and the Sunshine Coast.</p><p><a class="link" href="/locations/">All service areas</a></p>', loc_chips)}
</div></section>

<section class="band band-tight"><div class="wrap">
  <div class="head-row"><h2>Insights</h2><a class="link" href="/insights/">All insights</a></div>
  {insight_cards(INSIGHTS[:3])}
</div></section>

{cta_band()}'''
    page("/", "Forth Projects | Commercial Builders Brisbane & Sunshine Coast",
         "Forth Projects delivers commercial construction, fit-outs, refurbishment and design + construct across Brisbane, South East Queensland and the Sunshine Coast.",
         main, priority="1.0", body_class="home")


def insight_cards(items):
    cards = "".join(f'<li><a class="icard" href="/insights/{i["slug"]}/"><time datetime="{i["date"]}">{fmt_date(i["date"])}</time>'
                    f'<h3>{esc(i["title"])}</h3><p>{esc(i["summary"])}</p></a></li>' for i in items)
    return f'<ul class="icards">{cards}</ul>'


def fmt_date(d):
    import datetime
    return datetime.date.fromisoformat(d).strftime("%-d %B %Y")


def build_services():
    crumbs = [("Home", "/"), ("Services", "/services/")]
    rows = index_rows([(s["name"], s["short"], f'/services/{s["slug"]}/') for s in SERVICES])
    main = page_hero("Commercial building services", "Everything from a single tenancy fit-out to a new commercial building, delivered by one accountable team.", crumbs) + f'''
<section class="band"><div class="wrap">{rows}</div></section>
{process_block()}
{cta_band()}'''
    page("/services/", "Commercial Building Services Brisbane & SEQ | Forth Projects",
         "Commercial construction, fit-outs, refurbishment, design + construct and make good works across Brisbane, the Gold Coast, Sunshine Coast and SEQ.",
         main, crumbs, priority="0.9")

    for s in SERVICES:
        path = f'/services/{s["slug"]}/'
        c = crumbs + [(s["name"], path)]
        sectors = tiles([(SEC[k]["name"], SEC[k]["image"], f'/sectors/{k}/') for k in s["sectors"]])
        locs = chips([(l["name"], f'/locations/{l["slug"]}/{s["slug"]}/' if (l["slug"], s["slug"]) in COMBOS
                       else f'/locations/{l["slug"]}/') for l in LOCATIONS])
        others = index_rows([(o["name"], o["short"], f'/services/{o["slug"]}/') for o in SERVICES if o["slug"] != s["slug"]])
        intro = "".join(f"<p>{p}</p>" for p in s["intro"])
        main = page_hero(s["name"], s["lead"], c) + f'''
<section class="band"><div class="wrap">
  {two_col(intro, ph(s["image"], "ph-tall"))}
</div></section>
<section class="band band-stone"><div class="wrap">
  {two_col(f'<h2>What&rsquo;s included</h2><p>Every project is scoped to suit, but {esc(s["name"].lower())} with Forth typically covers:</p>', ticks(s["includes"]))}
</div></section>
<section class="band"><div class="wrap">
  <div class="head-row"><h2>Sectors</h2><a class="link" href="/sectors/">All sectors</a></div>
  {sectors}
</div></section>
{why_block()}
<section class="band"><div class="wrap">
  {two_col(f'<h2>{esc(s["name"])} across SEQ and the Sunshine Coast</h2><p>Based in Brisbane, we deliver projects across the region.</p>', locs)}
</div></section>
{faq_block(s["faqs"])}
<section class="band band-tight"><div class="wrap"><h2>Other services</h2>{others}</div></section>
{cta_band()}'''
        page(path, s["title"], s["meta"], main, c,
             [service_schema(s["name"], s["meta"], path, AREAS_SERVED), faq_schema(s["faqs"])], priority="0.9")


def build_sectors():
    crumbs = [("Home", "/"), ("Sectors", "/sectors/")]
    t = tiles([(s["name"], s["image"], f'/sectors/{s["slug"]}/') for s in SECTORS])
    main = page_hero("Sectors we build for", "Each sector has its own standards, rules and ways of operating. We plan every project around them.", crumbs) + f'''
<section class="band"><div class="wrap">{t}</div></section>
{why_block()}
{cta_band()}'''
    page("/sectors/", "Sectors | Office, Retail, Hospitality & Medical | Forth",
         "Forth Projects builds and fits out offices, retail stores, hospitality venues, medical clinics, childcare centres and industrial buildings across SEQ.",
         main, crumbs, priority="0.8")

    for s in SECTORS:
        path = f'/sectors/{s["slug"]}/'
        c = crumbs + [(s["name"], path)]
        intro = "".join(f"<p>{p}</p>" for p in s["intro"])
        svcs = index_rows([(SVC[k]["name"], SVC[k]["short"], f'/services/{k}/') for k in s["services"]])
        others = chips([(o["name"], f'/sectors/{o["slug"]}/') for o in SECTORS if o["slug"] != s["slug"]])
        main = page_hero(s["h1"], s["lead"], c) + f'''
<section class="band"><div class="wrap">
  {two_col(intro, ph(s["image"], "ph-tall"))}
</div></section>
<section class="band band-stone"><div class="wrap">
  {two_col("<h2>What we plan for</h2><p>The details that make or break a project in this sector, built into our planning from the first site visit.</p>", ticks(s["considerations"]))}
</div></section>
<section class="band band-tight"><div class="wrap"><h2>Related services</h2>{svcs}</div></section>
{process_block()}
{faq_block(s["faqs"])}
<section class="band band-tight"><div class="wrap">{two_col("<h2>Other sectors</h2>", others)}</div></section>
{cta_band()}'''
        page(path, s["title"], s["meta"], main, c,
             [service_schema(s["h1"], s["meta"], path, AREAS_SERVED), faq_schema(s["faqs"])], priority="0.8")


def build_locations():
    crumbs = [("Home", "/"), ("Locations", "/locations/")]
    rows = index_rows([(l["name"], l["lead"], f'/locations/{l["slug"]}/') for l in LOCATIONS])
    main = page_hero("Where we build", "Based in Brisbane, delivering commercial projects across South East Queensland and the Sunshine Coast.", crumbs) + f'''
<section class="band"><div class="wrap">{rows}</div></section>
{cta_band()}'''
    page("/locations/", "Service Areas | Commercial Builders SEQ & Sunshine Coast",
         "Forth Projects delivers commercial construction and fit-outs across Brisbane, the Gold Coast, Sunshine Coast, Ipswich, Logan, Moreton Bay and Redland City.",
         main, crumbs, priority="0.8")

    for l in LOCATIONS:
        path = f'/locations/{l["slug"]}/'
        c = crumbs + [(l["name"], path)]
        intro = "".join(f"<p>{p}</p>" for p in l["intro"])
        svc_items = []
        for s in SERVICES:
            href = f'/locations/{l["slug"]}/{s["slug"]}/' if (l["slug"], s["slug"]) in COMBOS else f'/services/{s["slug"]}/'
            svc_items.append((s["name"], s["short"], href))
        areas = chips([(a, None) for a in l["areas"]])
        sec = chips([(s["nav"], f'/sectors/{s["slug"]}/') for s in SECTORS])
        others = chips([(o["name"], f'/locations/{o["slug"]}/') for o in LOCATIONS if o["slug"] != l["slug"]])
        faqs = [
            (f'Do you work across all of {l["name"]}?',
             f'Yes. We work across {", ".join(l["areas"][:6])} and surrounding suburbs.'),
            ("How do we get started?",
             'Send us a few details through our <a href="/contact/">contact page</a> or call us. We\'ll arrange a site visit to understand your space, timing and budget.'),
            ("What types of projects do you deliver here?",
             "Commercial construction, fit-outs, refurbishments, design + construct and make good works for offices, retail, hospitality, medical, education and industrial clients."),
        ]
        schema = {"@context": "https://schema.org", "@type": "Service",
                  "name": f'Commercial building services in {l["name"]}', "url": URL + path,
                  "provider": {"@id": URL + "/#org"}, "description": l["meta"],
                  "areaServed": {"@type": "City", "name": l["name"],
                                 "geo": {"@type": "GeoCoordinates", "latitude": l["geo"][0], "longitude": l["geo"][1]}}}
        main = page_hero(f'Commercial builders in {l["name"]}' if l["slug"] not in ("gold-coast", "sunshine-coast")
                         else f'Commercial builders on the {l["name"]}', l["lead"], c) + f'''
<section class="band"><div class="wrap">
  {two_col(intro, ph(l["image"], "ph-tall"))}
</div></section>
<section class="band band-tight"><div class="wrap"><h2>Our services in {esc(l["name"])}</h2>{index_rows(svc_items)}</div></section>
<section class="band band-stone"><div class="wrap">
  {two_col(f'<h2>Areas we cover</h2><p>Projects across {esc(l["name"])} and surrounding suburbs, including:</p>', areas)}
</div></section>
<section class="band"><div class="wrap">{two_col("<h2>Sectors</h2>", sec)}</div></section>
{why_block()}
{faq_block(faqs)}
<section class="band band-tight"><div class="wrap">{two_col("<h2>Other locations</h2>", others)}</div></section>
{cta_band()}'''
        page(path, l["title"], l["meta"], main, c, [schema, faq_schema(faqs)], priority="0.8")

    # location x service combos
    for (lslug, sslug), paras in COMBOS.items():
        l, s = LOC[lslug], SVC[sslug]
        path = f'/locations/{lslug}/{sslug}/'
        c = crumbs + [(l["name"], f'/locations/{lslug}/'), (s["name"], path)]
        place = f'the {l["name"]}' if lslug in ("gold-coast", "sunshine-coast") else l["name"]
        h1 = f'{s["name"]} on {place}' if place.startswith("the") else f'{s["name"]} in {place}'
        title = f'{s["name"].title().replace("Fit-Outs","Fit-Outs")} {l["name"]} | Forth Projects'
        meta = f'{s["name"]} across {place}. {s["lead"]}'
        if len(meta) > 158:
            meta = f'{s["name"]} across {place} by Forth Projects. {s["short"]}'
        intro = "".join(f"<p>{p}</p>" for p in paras)
        siblings = [(SVC[k]["name"], f'/locations/{lslug}/{k}/') for (ls, k) in COMBOS if ls == lslug and k != sslug]
        same_svc = [(LOC[ls]["name"], f'/locations/{ls}/{sslug}/') for (ls, k) in COMBOS if k == sslug and ls != lslug]
        faqs = s["faqs"][:3] + [(f'Do you work across all of {l["name"]}?',
                                 f'Yes. We work across {", ".join(l["areas"][:6])} and surrounding suburbs.')]
        main = page_hero(h1, s["lead"], c) + f'''
<section class="band"><div class="wrap">
  {two_col(intro + f'<p><a class="link" href="/services/{sslug}/">More about {esc(s["name"].lower())}</a></p>', ph(f'{s["name"]}, {l["name"]}', "ph-tall"))}
</div></section>
<section class="band band-stone"><div class="wrap">
  {two_col("<h2>What&rsquo;s included</h2>", ticks(s["includes"]))}
</div></section>
<section class="band"><div class="wrap">
  {two_col(f'<h2>Areas we cover in {esc(l["name"])}</h2>', chips([(a, None) for a in l["areas"]]))}
</div></section>
{process_block()}
{faq_block(faqs)}
<section class="band band-tight"><div class="wrap">
  {two_col(f'<h2>More in {esc(l["name"])}</h2>' + chips(siblings), f'<h2>{esc(s["name"])} elsewhere</h2>' + chips(same_svc))}
</div></section>
{cta_band()}'''
        schema = service_schema(f'{s["name"]} in {l["name"]}', meta, path, [l["name"]])
        page(path, title, meta, main, c, [schema, faq_schema(faqs)], priority="0.8")


def build_projects():
    crumbs = [("Home", "/"), ("Projects", "/projects/")]
    live = [p for p in PROJECTS if not p.get("sample")]
    if live:
        svc_opts = "".join(f'<option value="{s["slug"]}">{esc(s["name"])}</option>' for s in SERVICES)
        sec_opts = "".join(f'<option value="{s["slug"]}">{esc(s["name"])}</option>' for s in SECTORS)
        cards = "".join(f'<li data-service="{p["service"]}" data-sector="{p["sector"]}"><a class="pcard" href="/projects/{p["slug"]}/">'
                        f'{ph(p["images"][0], "ph-tile")}<h3>{esc(p["name"])}</h3><p>{esc(SEC[p["sector"]]["name"])}, {esc(p["location"])}</p></a></li>' for p in live)
        body = f'''<form class="filters" aria-label="Filter projects" onsubmit="return false">
  <label>Service <select data-filter="service"><option value="">All services</option>{svc_opts}</select></label>
  <label>Sector <select data-filter="sector"><option value="">All sectors</option>{sec_opts}</select></label>
</form>
<ul class="pcards" data-projects>{cards}</ul>
<p class="empty" data-empty hidden>No projects match those filters yet. Try another combination.</p>'''
    else:
        body = '''<div class="empty-state"><h2>Case studies are on the way</h2>
<p>We're documenting recent projects now. In the meantime, we're happy to walk you through relevant work and references for your type of project.</p>
<p><a class="btn btn-bronze" href="/contact/">Ask about our work</a></p></div>'''
    main = page_hero("Projects", "Commercial construction, fit-outs and refurbishments across South East Queensland and the Sunshine Coast.", crumbs, cta=False) + \
        f'<section class="band"><div class="wrap">{body}</div></section>{cta_band()}'
    page("/projects/", "Commercial Building Projects | Case Studies | Forth Projects",
         "Commercial construction, fit-out and refurbishment case studies from Forth Projects across Brisbane, the Gold Coast and Sunshine Coast.",
         main, crumbs, priority="0.8")

    for p in PROJECTS:
        path = f'/projects/{p["slug"]}/'
        c = crumbs + [(p["name"], path)]
        s, sec = SVC[p["service"]], SEC[p["sector"]]
        facts = [("Client", p["client"]), ("Location", p["location"]), ("Service", s["name"]),
                 ("Sector", sec["name"]), ("Size", p["size"]), ("Program", p["program"])]
        fb = "".join(f'<div><dt>{k}</dt><dd>{esc(v)}</dd></div>' for k, v in facts)
        gallery = "".join(ph(i) for i in p["images"][1:])
        q, who = p["testimonial"]
        main = page_hero(p["name"], p["summary"], c, cta=False) + f'''
<section class="band band-tight"><div class="wrap">{ph(p["images"][0], "ph-wide")}<dl class="facts">{fb}</dl></div></section>
<section class="band"><div class="wrap narrow prose">
  <h2>The brief</h2><p>{esc(p["brief"])}</p>
  <h2>The challenge</h2><p>{esc(p["challenge"])}</p>
  <h2>The outcome</h2><p>{esc(p["outcome"])}</p>
</div></section>
<section class="band band-tight"><div class="wrap"><div class="gallery">{gallery}</div></div></section>
<section class="band band-dark"><div class="wrap narrow"><blockquote class="quote"><p>{esc(q)}</p><footer>{esc(who)}</footer></blockquote></div></section>
<section class="band band-tight"><div class="wrap">{two_col("<h2>Related</h2>", chips([(s["name"], f'/services/{s["slug"]}/'), (sec["name"], f'/sectors/{sec["slug"]}/')]))}</div></section>
{cta_band()}'''
        page(path, f'{p["name"]} | Forth Projects', p["summary"], main, c, noindex=p.get("sample", False))


def build_insights():
    crumbs = [("Home", "/"), ("Insights", "/insights/")]
    main = page_hero("Insights", "Practical guidance on planning, pricing and delivering commercial projects.", crumbs, cta=False) + \
        f'<section class="band"><div class="wrap">{insight_cards(INSIGHTS)}</div></section>{cta_band()}'
    page("/insights/", "Commercial Construction Insights & Guides | Forth Projects",
         "Guides on commercial fit-out costs, make good obligations and procurement options from the team at Forth Projects.",
         main, crumbs, priority="0.6")
    for a in INSIGHTS:
        path = f'/insights/{a["slug"]}/'
        c = crumbs + [(a["title"], path)]
        rel = index_rows([(SVC[k]["name"], SVC[k]["short"], f'/services/{k}/') for k in a["related"]])
        schema = {"@context": "https://schema.org", "@type": "Article", "headline": a["title"],
                  "description": a["meta"], "datePublished": a["date"], "dateModified": a["date"],
                  "author": {"@id": URL + "/#org"}, "publisher": {"@id": URL + "/#org"},
                  "mainEntityOfPage": URL + path, "image": URL + "/assets/img/og-default.png"}
        main = page_hero(a["title"], a["summary"], c, cta=False,
                         kicker=fmt_date(a["date"])) + f'''
<section class="band"><div class="wrap narrow prose">{a["body"]}</div></section>
<section class="band band-tight"><div class="wrap"><h2>Related services</h2>{rel}</div></section>
{cta_band()}'''
        page(path, a["seo_title"], a["meta"], main, c, [schema], priority="0.6", og_type="article")


def form_html(kind):
    svc = "".join(f'<option>{esc(s["name"])}</option>' for s in SERVICES)
    sec = "".join(f'<option>{esc(s["name"])}</option>' for s in SECTORS)
    loc = "".join(f'<option>{esc(l["name"])}</option>' for l in LOCATIONS)
    common = '''<div class="f-row"><label>Name<input name="name" autocomplete="name" required></label>
<label>Company<input name="company" autocomplete="organization"></label></div>
<div class="f-row"><label>Email<input type="email" name="email" autocomplete="email" required></label>
<label>Phone<input type="tel" name="phone" autocomplete="tel"></label></div>'''
    hp = '<label class="hp" aria-hidden="true">Leave this empty<input name="_gotcha" tabindex="-1" autocomplete="off"></label>'
    if kind == "project":
        fields = common + f'''<div class="f-row"><label>Project type<select name="service" required><option value="">Select</option>{svc}<option>Not sure yet</option></select></label>
<label>Sector<select name="sector"><option value="">Select</option>{sec}<option>Other</option></select></label></div>
<div class="f-row"><label>Location<select name="location"><option value="">Select</option>{loc}<option>Other</option></select></label>
<label>Approximate size (m²)<input name="size" inputmode="numeric"></label></div>
<div class="f-row"><label>Timing<select name="timing"><option value="">Select</option><option>Within 3 months</option><option>3 to 6 months</option><option>6 to 12 months</option><option>12 months or more</option></select></label>
<label>Budget range<select name="budget"><option value="">Select</option><option>Under $250k</option><option>$250k to $1m</option><option>$1m to $5m</option><option>Over $5m</option><option>Not sure yet</option></select></label></div>
<label>About your project<textarea name="message" rows="5" required></textarea></label>'''
        btn, subject = "Send project details", "New project enquiry"
    elif kind == "subbie":
        fields = common + f'''<div class="f-row"><label>Trade<input name="trade" required></label>
<label>Licence number (if applicable)<input name="licence"></label></div>
<label>Areas you work in<select name="areas" multiple size="4">{loc}</select></label>
<label>Insurances and experience<textarea name="message" rows="4"></textarea></label>'''
        btn, subject = "Register interest", "Subcontractor registration"
    elif kind == "capability":
        fields = common + '<label>What are you considering us for?<textarea name="message" rows="3"></textarea></label>'
        btn, subject = "Request capability statement", "Capability statement request"
    else:
        fields = common + '<label>Role you\'re interested in<input name="role"></label><label>Message<textarea name="message" rows="4"></textarea></label>'
        btn, subject = "Send", "Careers enquiry"
    return f'''<form class="form" data-form action="{SITE["form_endpoint"]}" method="POST" data-mailto="{SITE["email"]}">
<input type="hidden" name="_subject" value="{subject}">
{fields}{hp}
<button class="btn btn-bronze" type="submit">{btn}</button>
<p class="form-status" role="status" aria-live="polite"></p>
<p class="form-note">We use your details only to respond to this enquiry. See our <a href="/privacy/">privacy policy</a>.</p>
</form>'''


def build_company():
    # About
    c = [("Home", "/"), ("About", "/about/")]
    vals = [("Built for what's next", "We plan every project around how the space will be used, not just how it will look on handover day."),
            ("Clarity at every stage", "Clear scopes, clear numbers and clear communication, so decisions are made with the full picture."),
            ("Craftsmanship", "Details done properly, by trades who take pride in the finish."),
            ("Purpose", "We measure success by how well the finished space works for the business inside it.")]
    v = "".join(f'<div class="why"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in vals)
    main = page_hero("About Forth Projects", "We take spaces, businesses and ideas forward.", c) + f'''
<section class="band"><div class="wrap">
  {two_col('<p class="big">Forth Projects delivers commercial construction and fit-outs with clarity, craftsmanship and purpose.</p>',
           '<p>We work with business owners, tenants, landlords and developers across South East Queensland and the Sunshine Coast. Our role is simple to describe and demanding to deliver: plan the project properly, price it clearly, build it well and hand over a space that works from day one.</p><p>Every project has one accountable team, from the first site walk to the final defect closed out. That continuity is what lets us move quickly without losing control of cost, quality or safety.</p>')}
</div></section>
<section class="band band-dark"><div class="wrap"><h2>What we stand for</h2><div class="why-grid">{v}</div></div></section>
<section class="band"><div class="wrap">
  <h2>Our team</h2>
  <p class="muted">Team profiles coming soon.</p>
</div></section>
{process_block()}
{cta_band()}'''
    page("/about/", "About Forth Projects | Commercial Builders Brisbane & SEQ",
         "Forth Projects is a Brisbane-based commercial builder delivering construction, fit-outs and refurbishment across SEQ and the Sunshine Coast.",
         main, c, priority="0.7")

    # Process
    c = [("Home", "/"), ("Our process", "/our-process/")]
    main = page_hero("Our process", "From concept. To completion. Here's how a Forth project runs, and what you can expect at each stage.", c) + \
        process_block(compact=False) + why_block() + cta_band()
    page("/our-process/", "Our Process | Commercial Construction | Forth Projects",
         "How Forth Projects delivers commercial construction and fit-outs, from the first site walk and pricing through approvals, construction and handover.",
         main, c, priority="0.6")

    # Safety and quality
    c = [("Home", "/"), ("Safety and quality", "/safety-and-quality/")]
    s_items = ["Site-specific safety plans and inductions", "Safe work method statements for high-risk work",
               "Subcontractor pre-qualification and insurances checked", "Public protection and site separation in occupied buildings",
               "Regular site inspections and toolbox talks", "Incident reporting and continuous improvement"]
    q_items = ["Inspection and test plans at key stages", "Hold points before work is covered up",
               "Documented defects process before handover", "As-built documentation, manuals and warranties"]
    main = page_hero("Safety and quality", "Everyone goes home safe, and every project is finished properly.", c) + f'''
<section class="band"><div class="wrap">{two_col("<h2>Safety</h2><p>Safety planning starts at pricing, not on day one of site works. We manage the risks of working in occupied buildings, public areas and active operations.</p>", ticks(s_items))}</div></section>
<section class="band band-stone"><div class="wrap">{two_col("<h2>Quality</h2><p>Quality is checked as the work is done, not after it's finished.</p>", ticks(q_items))}</div></section>
<section class="band"><div class="wrap">{two_col("<h2>Licensing and insurance</h2>", f'<p>Forth Projects is licensed with the Queensland Building and Construction Commission ({esc(SITE["qbcc"])}). Insurance certificates and safety documentation are available on request and are included in our <a href="/capability-statement/">capability statement</a>.</p>')}</div></section>
{cta_band()}'''
    page("/safety-and-quality/", "Safety and Quality | Forth Projects",
         "How Forth Projects manages work health and safety and quality on commercial construction and fit-out projects across Queensland.",
         main, c, priority="0.5")

    # Careers
    c = [("Home", "/"), ("Careers", "/careers/")]
    main = page_hero("Careers", "Build what's next with us.", c, cta=False) + f'''
<section class="band"><div class="wrap">{two_col("<h2>Work with Forth</h2><p>We're always interested in hearing from site managers, project managers, estimators, contract administrators and skilled trades who take pride in their work.</p><p>There are no advertised roles right now, but send us your details and we'll be in touch when something suits.</p>", form_html("careers"))}</div></section>'''
    page("/careers/", "Careers | Construction Jobs Brisbane | Forth Projects",
         "Careers at Forth Projects for site managers, project managers, estimators and trades across Brisbane, SEQ and the Sunshine Coast.",
         main, c, priority="0.4")

    # Subcontractors
    c = [("Home", "/"), ("Subcontractors", "/subcontractors/")]
    main = page_hero("Subcontractors and suppliers", "Quality trades are the backbone of every Forth project.", c, cta=False) + f'''
<section class="band"><div class="wrap">{two_col("<h2>Register your interest</h2><p>We're building a network of reliable subcontractors and suppliers across South East Queensland and the Sunshine Coast. Tell us about your business and we'll contact you about upcoming work and pre-qualification.</p>", form_html("subbie"))}</div></section>'''
    page("/subcontractors/", "Subcontractor and Supplier Registration | Forth Projects",
         "Subcontractors and suppliers can register interest in working with Forth Projects on commercial projects across SEQ and the Sunshine Coast.",
         main, c, priority="0.4")

    # Capability statement
    c = [("Home", "/"), ("Capability statement", "/capability-statement/")]
    cs = ["Company overview and services", "Sectors and representative projects", "Licensing and insurances",
          "Safety and quality systems", "Key personnel", "Contact details"]
    main = page_hero("Capability statement", "Everything procurement teams, landlords and project managers need to assess Forth Projects.", c, cta=False) + f'''
<section class="band"><div class="wrap">{two_col("<h2>What&rsquo;s inside</h2>" + ticks(cs), "<h2>Request a copy</h2>" + form_html("capability"))}</div></section>'''
    page("/capability-statement/", "Capability Statement | Forth Projects",
         "Request the Forth Projects capability statement covering services, sectors, licensing, insurances, safety and key personnel.",
         main, c, priority="0.5")

    # Contact
    c = [("Home", "/"), ("Contact", "/contact/")]
    contact_side = f'''<div class="contact-card">
<h2>Talk to us</h2>
<p><a class="big-link" href="tel:{SITE["phone_e164"]}">{SITE["phone"]}</a></p>
<p><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></p>
<p>{SITE["locality"]}, {SITE["region"]}<br>Working across South East Queensland and the Sunshine Coast</p>
<h3>What happens next</h3>
<ol class="mini-steps"><li>We review your details and call you within one business day.</li><li>We arrange a site visit to understand the space and your timing.</li><li>We outline the approach, likely program and next steps.</li></ol>
</div>'''
    main = page_hero("Discuss your project", "Tell us about your site, your timing and what the space needs to do.", c, cta=False) + \
        f'<section class="band"><div class="wrap">{two_col(form_html("project"), contact_side, flip=True)}</div></section>'
    schema = {"@context": "https://schema.org", "@type": "ContactPage", "url": URL + "/contact/",
              "about": {"@id": URL + "/#org"}}
    page("/contact/", "Contact Forth Projects | Discuss Your Commercial Project",
         "Talk to Forth Projects about a commercial build, fit-out or refurbishment in Brisbane, the Gold Coast, Sunshine Coast or wider SEQ.",
         main, c, [schema], priority="0.9")

    # Privacy
    c = [("Home", "/"), ("Privacy", "/privacy/")]
    body = f'''<p>Forth Projects respects your privacy and handles personal information in line with the Privacy Act 1988 (Cth) and the Australian Privacy Principles where they apply to us.</p>
<h2>What we collect</h2><p>We collect the details you give us through our website forms, by email or by phone, such as your name, company, contact details and information about your project. Our website may also collect anonymous usage data through analytics tools.</p>
<h2>How we use it</h2><p>We use your information to respond to enquiries, prepare proposals, deliver projects, manage subcontractor and supplier relationships, and consider job applications. We don't sell your information.</p>
<h2>Who we share it with</h2><p>We may share information with consultants, subcontractors and service providers who help us deliver our services, and where required by law.</p>
<h2>Storage and security</h2><p>We take reasonable steps to protect personal information from misuse, loss and unauthorised access.</p>
<h2>Access and correction</h2><p>You can ask to access or correct the personal information we hold about you by contacting <a href="mailto:{SITE["email"]}">{SITE["email"]}</a>.</p>
<h2>Complaints</h2><p>If you have a privacy concern, contact us first. If you're not satisfied with our response, you can contact the Office of the Australian Information Commissioner.</p>
<p class="muted">Last updated {fmt_date(SITE["updated"])}.</p>'''
    main = page_hero("Privacy policy", "How we collect, use and protect your information.", c, cta=False) + \
        f'<section class="band"><div class="wrap narrow prose">{body}</div></section>'
    page("/privacy/", "Privacy Policy | Forth Projects",
         "How Forth Projects collects, uses and protects personal information.", main, c, priority="0.2")

    # 404
    main = f'''<section class="phero phero-404"><div class="phero-slash" aria-hidden="true"></div><div class="wrap">
<h1>This page has moved forward</h1><p class="lead">The page you're looking for doesn't exist or has moved. Try one of these instead.</p>
<div class="hero-actions"><a class="btn btn-bronze" href="/">Go to the homepage</a><a class="btn btn-line" href="/services/">View services</a></div></div></section>'''
    page("/404/", "Page not found | Forth Projects", "The page you're looking for doesn't exist.", main, noindex=True)


def write_sitemap():
    today = SITE["updated"]
    urls = "".join(f"<url><loc>{URL}{p}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>\n"
                   for p, pr in SITEMAP)
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + urls + "</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /_src/\n\nSitemap: {URL}/sitemap.xml\n")


def clean():
    for d in ["services", "sectors", "locations", "projects", "insights", "about", "our-process",
              "safety-and-quality", "careers", "subcontractors", "capability-statement", "contact", "privacy"]:
        shutil.rmtree(os.path.join(ROOT, d), ignore_errors=True)


if __name__ == "__main__":
    clean()
    build_home(); build_services(); build_sectors(); build_locations()
    build_projects(); build_insights(); build_company(); write_sitemap()
    print(f"Built {len(SITEMAP)} indexable pages.")
