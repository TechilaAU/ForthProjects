# Forth Projects website

Static site for **Forth Projects** (forthprojects.com.au), a commercial builder covering commercial construction, fit-outs, refurbishment, design + construct and make good works across Brisbane, SEQ and the Sunshine Coast.

Every page is generated from `_src/content.py` by `_src/build.py`. Don't hand-edit the generated HTML. Edit the content file instead, then rebuild.

```bash
python3 _src/build.py      # rebuilds every page, sitemap.xml and robots.txt
python3 -m http.server     # preview at http://localhost:8000
```

## Site map (44 indexable pages)

| Section | Pages |
|---|---|
| Home | `/` |
| Services (6) | `/services/` plus commercial-construction, commercial-fit-outs, commercial-refurbishment, design-and-construct, make-good |
| Sectors (7) | `/sectors/` plus office, retail, hospitality, health-medical, education-childcare, industrial-warehouse |
| Locations (8) | `/locations/` plus brisbane, gold-coast, sunshine-coast, ipswich, logan, moreton-bay, redland-city |
| Location × service (9) | `/locations/{brisbane,gold-coast,sunshine-coast}/{commercial-fit-outs,commercial-construction,commercial-refurbishment}/` |
| Projects | `/projects/` with filterable index and case study template (`/projects/sample-project/` is noindex) |
| Insights (4) | `/insights/` plus 3 starter articles |
| Company (8) | about, our-process, safety-and-quality, careers, subcontractors, capability-statement, contact, privacy |
| Other | `404.html`, `sitemap.xml`, `robots.txt` |

## SEO built in

- A unique title and meta description on every page, checked for length and duplicates.
- Canonical URLs, Open Graph and Twitter tags, `en-AU` language and the `AU-QLD` geo region.
- JSON-LD on every page:
  - GeneralContractor organisation, plus WebSite on the home page
  - BreadcrumbList
  - Service on services, sectors, locations and combo pages, with areaServed and geo coordinates
  - FAQPage
  - Article on insights
  - ContactPage
- One H1 per page, visible breadcrumbs, and clean trailing-slash URLs.
- Dense internal linking: services ↔ sectors ↔ locations ↔ combo pages, plus a full footer index.
- `sitemap.xml` is generated automatically and excludes noindex pages. `robots.txt` points to it.
- Performance:
  - self-hosted Montserrat variable font (52 KB woff2, preloaded)
  - one CSS file and one small JS file
  - no frameworks

### Keyword targeting (avoid cannibalisation)
- **Services** target the service plus region, e.g. "commercial fit-outs Brisbane".
- **Sectors** target sector fit-outs, e.g. "office fit-outs Brisbane" or "medical fit-outs".
- **Locations** target "commercial builders {location}".
- **Combo pages** target "{service} {location}" for the three main regions.

## Adding content

- **Case study:** add an entry to `PROJECTS`. The page, the projects index and its filters, and the sitemap all update automatically. Once there's at least one real project, delete the sample entry.
- **Article:** add an entry to `INSIGHTS`.
- **New combo page:** add a `(location, service)` key to `COMBOS` with two unique paragraphs. Don't reuse text between combo pages.

## Launch checklist (TODO)

- [ ] **Vector logo.** The logo in `/assets/img` and the header mark are recreations from the brand board. Replace them with the supplied artwork.
- [ ] **Contact details and registrations** in `SITE`: confirm phone, email and address (the board values may be mock-ups). Add the QBCC licence number (required) and ABN.
- [ ] **Form endpoint.** Set `form_endpoint` (Formspree, Netlify Forms, etc.). Until then, forms fall back to opening a prefilled email.
- [ ] **Photography.** Every `.ph` placeholder shows its brief as a caption. Swap each for real photography in WebP/AVIF, with `width`/`height` set and descriptive alt text.
- [ ] **Copy confirmation.** Confirm services, sectors and service areas with Forth, and confirm the "Why Forth" differentiators.
- [ ] **Case studies.** Add at least 3–4 real ones, plus testimonials.
- [ ] **Team and documents.** Add team profiles to `/about/`, and the capability statement PDF.
- [ ] **Privacy policy.** Have it reviewed.
- [ ] **Social profiles.** Add LinkedIn and Instagram URLs (they feed `sameAs` in the schema).
- [ ] **Google tools.** Set up a Google Business Profile, Search Console (submit the sitemap) and analytics. The form pushes a `form_submit` event to `dataLayer` if GTM is installed.
- [ ] **OG image.** `/assets/img/og-default.png` is a generated placeholder. Replace it with a branded 1200×630 image.

## Brand tokens

| Token | Hex | Use |
|---|---|---|
| Charcoal | `#1E1E1E` | Primary |
| Bronze | `#A68B6A` | Accent, button fills, rules, large text on dark |
| Bronze deep | `#7A6343` | Small bronze text on light backgrounds (passes WCAG AA) |
| Stone | `#E8E6E1` | Background |
| Olive | `#4A5A3F` | Secondary, used sparingly |

Buttons use charcoal text on bronze, because white on bronze fails contrast.
