# -*- coding: utf-8 -*-
"""
Forth Projects - site content.
Every page on the site is generated from the data in this file by build.py.
Items marked TODO must be confirmed with Forth before launch.
"""

SITE = {
    "name": "Forth Projects",
    "url": "https://forthprojects.com.au",
    "tagline": "Spaces. Built Forward.",
    "phone": "07 3186 4400",            # TODO confirm (taken from brand board mock-up)
    "phone_e164": "+61731864400",       # TODO confirm
    "email": "info@forthprojects.com.au",  # TODO confirm
    "locality": "Brisbane",
    "region": "QLD",
    "country": "AU",
    "qbcc": "QBCC Licence No. TBC",     # TODO required before launch
    "abn": "ABN TBC",                   # TODO
    "form_endpoint": "REPLACE_WITH_FORM_ENDPOINT",  # TODO e.g. https://formspree.io/f/xxxx
    "linkedin": "",                     # TODO add profile URL
    "instagram": "",                    # TODO add profile URL
    "updated": "2026-10-02",
}

AREAS_SERVED = ["Brisbane", "Gold Coast", "Sunshine Coast", "Ipswich", "Logan",
                "Moreton Bay", "Redland City"]

WHY = [
    ("One team, start to finish",
     "A single point of contact from the first site walk to handover, with no gaps between design, pricing and construction."),
    ("Programs built around your business",
     "Staged works, after-hours scheduling and clear access plans so you can keep trading while we build."),
    ("Clear numbers early",
     "Itemised pricing, cost plans at each stage and variations documented before they happen."),
    ("Finished properly",
     "Defects closed out, as-built documentation, manuals and warranties handed over in one place."),
]

PROCESS = [
    ("Brief and site walk",
     "We meet on site, listen to what the space needs to do for your business and identify constraints early: lease conditions, building rules, services and timing."),
    ("Design and pricing",
     "We coordinate or review the design, test it for cost and buildability, and give you an itemised price and a realistic program."),
    ("Approvals and planning",
     "Landlord, certifier and authority approvals are coordinated, long-lead items are ordered and the site plan is set."),
    ("Construction",
     "Our site team manages trades, quality and safety, with regular updates in plain terms and decisions documented as they're made."),
    ("Handover and aftercare",
     "Final inspections, defects closed out, as-builts, manuals and warranties handed over, and support through the defects liability period."),
]

# ---------------------------------------------------------------- SERVICES
SERVICES = [
    {
        "slug": "commercial-construction",
        "name": "Commercial construction",
        "short": "New commercial buildings delivered by one team, from early advice to handover.",
        "title": "Commercial Construction Brisbane & SEQ | Forth Projects",
        "meta": "Commercial builders for offices, retail, medical, childcare and industrial projects across Brisbane, the Gold Coast and Sunshine Coast.",
        "lead": "New commercial buildings across South East Queensland and the Sunshine Coast, delivered by one team from early advice to handover.",
        "intro": [
            "A commercial build has more moving parts than most owners expect: consultants, certifiers, authorities, services, long-lead materials and a program that has to hold. Forth Projects manages all of it under one contract, so you deal with one team and get one clear line of accountability.",
            "We build offices, showrooms, medical and allied health centres, childcare centres, hospitality venues and light industrial buildings. Whether you're an owner-occupier, investor or developer, we start by understanding how the building needs to perform for the business inside it, then plan the build around that.",
        ],
        "includes": [
            "Pre-construction advice and buildability reviews",
            "Cost planning and staged pricing",
            "Coordination with architects, engineers and certifiers",
            "Authority and service provider coordination",
            "Site establishment, civil and structural works",
            "Building envelope, services and internal fit-out",
            "Quality inspections at each stage",
            "Handover with as-built documentation, manuals and warranties",
            "Defects liability period support",
        ],
        "faqs": [
            ("Do you build from an existing design?",
             "Yes. If you already have documentation we can price and build it, and we'll flag any buildability or cost issues before work starts. If you're earlier in the process, our <a href=\"/services/design-and-construct/\">design and construct</a> service may suit you better."),
            ("What size projects do you take on?",
             "Every project is different, so the best starting point is a conversation about your site, scope and timing. We'll tell you early if we're the right fit."),
            ("Can you help with development approval?",
             "We coordinate with your town planner, certifier and consultants and can recommend specialists where needed. Applications are lodged by the relevant consultant, and we plan the construction program around expected approval timeframes."),
            ("Which areas do you build in?",
             "Brisbane, the Gold Coast, the Sunshine Coast, Ipswich, Logan, Moreton Bay and Redland City. See <a href=\"/locations/\">where we build</a>."),
        ],
        "sectors": ["office", "retail", "health-medical", "education-childcare", "industrial-warehouse"],
        "image": "New commercial building, exterior at dusk",
    },
    {
        "slug": "commercial-fit-outs",
        "name": "Commercial fit-outs",
        "short": "Tenancy fit-outs planned around your lease, your landlord and your opening date.",
        "title": "Commercial Fit-Outs Brisbane & SEQ | Forth Projects",
        "meta": "Commercial fit-outs for offices, retail, hospitality and medical tenancies across South East Queensland and the Sunshine Coast, planned around your lease.",
        "lead": "Tenancy fit-outs that open on time, meet the landlord's requirements and work for the people using the space every day.",
        "intro": [
            "A fit-out sits between two sets of obligations: what the business needs from the space, and what the lease and building require. We read the landlord's design criteria early, work with your designer (or bring one in), and plan the works so approvals, building management sign-offs and services shutdowns don't hold up opening day.",
            "From a single-floor office to a multi-site retail rollout, we manage the trades, materials and program, and keep you updated in plain terms throughout.",
        ],
        "includes": [
            "Review of lease, landlord design criteria and building rules",
            "Space planning and design coordination",
            "Demolition and strip-out",
            "Partitions, ceilings and acoustic treatments",
            "Custom joinery and shopfitting",
            "Flooring, finishes and lighting",
            "Electrical, data, mechanical and fire services modifications",
            "After-hours and weekend works in occupied buildings",
            "Signage, furniture and equipment coordination",
            "Building management sign-off and handover documentation",
        ],
        "faqs": [
            ("How long does a commercial fit-out take?",
             "It depends on size, complexity and lead times for joinery, equipment and approvals. Once we've seen the space and the scope, we give you a program showing each milestone and what it depends on."),
            ("Can you work with my own designer?",
             "Yes. We can build from your designer's documentation, or bring in a designer so you have a single point of contact through our <a href=\"/services/design-and-construct/\">design and construct</a> service."),
            ("Do you work after hours?",
             "Where the building or your business requires it, we schedule noisy or disruptive works outside trading hours and coordinate access with building management."),
            ("Who handles landlord approvals?",
             "We prepare and coordinate what the landlord and building manager need, including method statements, insurances and services drawings, and track them through to approval."),
        ],
        "sectors": ["office", "retail", "hospitality", "health-medical"],
        "image": "Completed office fit-out, reception and breakout space",
    },
    {
        "slug": "commercial-refurbishment",
        "name": "Commercial refurbishment",
        "short": "Upgrades to existing buildings and tenancies, staged so you can keep operating.",
        "title": "Commercial Refurbishment Brisbane & SEQ | Forth Projects",
        "meta": "Refurbishment of offices, lobbies, amenities and ageing commercial buildings across SEQ and the Sunshine Coast, staged to keep tenants operating.",
        "lead": "Bring an existing building or tenancy up to date without shutting it down.",
        "intro": [
            "Refurbishment is about working with what's already there: existing structure, existing services and, often, people still using the building. We investigate before we price, so hidden conditions are found early instead of halfway through the job.",
            "Typical projects include lobby and foyer upgrades, amenities and end-of-trip facilities, floor refurbishments between tenancies, façade and entry refreshes, and accessibility and compliance upgrades.",
        ],
        "includes": [
            "Site investigation and condition review",
            "Staging plans for occupied buildings",
            "Lobby, foyer and common area upgrades",
            "Amenities and end-of-trip facilities",
            "Floor refurbishments for leasing",
            "Accessibility and compliance upgrades",
            "Façade, entry and external refresh works",
            "Services upgrades coordinated with your consultants",
            "Dust, noise and access management",
        ],
        "faqs": [
            ("Can the building stay open during the works?",
             "In most cases, yes. We stage the works, separate work zones from occupied areas and schedule disruptive tasks out of hours where needed."),
            ("What happens if problems appear once work starts?",
             "We investigate as much as we can before pricing. If something unexpected appears, we stop, show you, and price the options before going further."),
            ("Do you refurbish vacant floors for leasing?",
             "Yes. We can program refurbishments of vacant floors around your leasing agent's timeline so the space is ready when a tenant is."),
        ],
        "sectors": ["office", "retail", "hospitality", "education-childcare"],
        "image": "Refurbished commercial lobby",
    },
    {
        "slug": "design-and-construct",
        "name": "Design + construct",
        "short": "One contract covering design and build, with cost tested at every stage.",
        "title": "Design and Construct Builders Brisbane & SEQ | Forth Projects",
        "meta": "Design and construct for commercial buildings and fit-outs across SEQ and the Sunshine Coast. One contract from concept design to handover.",
        "lead": "One contract, one team and one point of accountability, from the first sketch to the final key.",
        "intro": [
            "With design and construct, Forth Projects takes responsibility for both the design and the build. We bring in the architect, interior designer and engineers, test the design against cost and buildability as it develops, and then build what's been designed. There's no handover between consultants and builder for you to manage, because there isn't one.",
            "It suits clients who want cost certainty earlier, a faster start on site, or simply one relationship to manage. We use it for new commercial buildings as well as larger fit-outs and refurbishments.",
        ],
        "includes": [
            "Brief development and feasibility input",
            "Engagement and management of design consultants",
            "Concept design and design development",
            "Cost planning at each design stage",
            "Value engineering that protects the brief",
            "Approvals coordination",
            "Construction, commissioning and handover",
            "A single contract and a single point of contact",
        ],
        "faqs": [
            ("How is design and construct different from a traditional contract?",
             "In a traditional contract you appoint the designers yourself, then tender the finished design to builders. In design and construct the builder is responsible for both, so design, cost and program are managed together. We explain the trade-offs in <a href=\"/insights/design-and-construct-vs-traditional-contracts/\">this guide</a>."),
            ("Do I still get a say in the design?",
             "Yes. You approve the brief and each design stage. The difference is that every decision is tested against cost and buildability as it's made, rather than after the drawings are finished."),
            ("When do I get a fixed price?",
             "Usually once the design is developed enough to price accurately. Before that, you receive a cost plan at each stage, so there are no surprises when the contract sum is set."),
        ],
        "sectors": ["office", "hospitality", "health-medical", "education-childcare", "industrial-warehouse"],
        "image": "Design team reviewing plans and material samples",
    },
    {
        "slug": "make-good",
        "name": "Make good works",
        "short": "Lease-end strip-out and reinstatement, scoped clearly and finished on time.",
        "title": "Make Good Works Brisbane & SEQ | Forth Projects",
        "meta": "Make good and strip-out works at lease end for offices, retail and industrial tenancies across SEQ and the Sunshine Coast, scoped clearly and finished on time.",
        "lead": "Hand back your tenancy in the condition your lease requires, on time and without drawn-out disputes.",
        "intro": [
            "At the end of a lease, most commercial tenants must return the premises to an agreed condition. That can mean removing partitions, joinery and cabling, reinstating ceilings and floors, and repairing services. We scope the works against your lease and the landlord's schedule of make good, price them clearly and complete them within your exit timeframe.",
            "We can also price make good alongside your next fit-out, so the move between premises is planned as one project. Your lease and your legal advisers remain the authority on what's required; we turn those requirements into a clear scope and program.",
        ],
        "includes": [
            "Review of make good obligations with your advisers",
            "Site inspection and scope of works",
            "Strip-out of partitions, joinery, cabling and fixtures",
            "Reinstatement of ceilings, flooring, lighting and finishes",
            "Services made safe and reinstated",
            "Waste management and recycling of salvageable materials",
            "Completion documentation for the landlord",
        ],
        "faqs": [
            ("When should I start planning make good?",
             "Ideally several months before your lease ends, so there's time to agree the scope with the landlord and finish the works before the handback date. Our guide to <a href=\"/insights/make-good-what-tenants-should-plan-for/\">make good obligations</a> covers the basics."),
            ("Can make good be settled with a payment instead?",
             "Some landlords will accept a payment in place of physical works. We can price the works to help you and your advisers weigh up that option."),
            ("Can you do the make good and our new fit-out?",
             "Yes. Running both together gives you one program for the move and one team coordinating both sites."),
        ],
        "sectors": ["office", "retail", "industrial-warehouse"],
        "image": "Office tenancy stripped back for handover",
    },
]

# ---------------------------------------------------------------- SECTORS
SECTORS = [
    {
        "slug": "office",
        "name": "Office and corporate",
        "nav": "Office fit-outs",
        "title": "Office Fit-Outs Brisbane & SEQ | Forth Projects",
        "meta": "Office fit-outs and refurbishments across Brisbane, the Gold Coast and Sunshine Coast. Workplaces planned around how your team actually works.",
        "h1": "Office fit-outs",
        "lead": "Workplaces planned around how your team works, delivered with minimal disruption to the business.",
        "intro": [
            "A good office supports focus, collaboration and the impression you want clients to have when they walk in. We work with your designer or ours to plan workstations, meeting rooms, breakout spaces and reception, then deliver the fit-out around the building's rules and your move date.",
            "We fit out new leases, refurbish existing offices while teams keep working, and deliver everything from small suites to multi-floor tenancies.",
        ],
        "considerations": [
            "Acoustic separation for meeting rooms and focus areas",
            "Data, AV and power planned for hybrid work",
            "Landlord design criteria and after-hours access",
            "Reception and client-facing spaces",
            "Kitchens, breakout areas and end-of-trip facilities",
            "Staged works for occupied offices",
        ],
        "faqs": [
            ("Can we stay in the office during the fit-out?",
             "Often, yes. We stage the works by zone, separate work areas and schedule noisy tasks out of hours so your team can keep working."),
            ("Do you handle IT and AV?",
             "We coordinate cabling, power and AV infrastructure with your IT provider so equipment can be installed and tested before you move in."),
        ],
        "services": ["commercial-fit-outs", "commercial-refurbishment", "design-and-construct", "make-good"],
        "image": "Open-plan office with meeting rooms",
    },
    {
        "slug": "retail",
        "name": "Retail and showrooms",
        "nav": "Retail fit-outs",
        "title": "Retail Fit-Outs & Shopfitting Brisbane & SEQ | Forth Projects",
        "meta": "Retail fit-outs and shopfitting for stores and showrooms in shopping centres and street-front sites across SEQ and the Sunshine Coast.",
        "h1": "Retail fit-outs and showrooms",
        "lead": "Stores and showrooms built to the centre's requirements and ready to trade on the date you've promised.",
        "intro": [
            "Retail fit-outs run on fixed dates: centre handover, trading deadlines and launch campaigns. We plan around the centre's fit-out guide and approvals process, lock in shopfitting and joinery lead times early, and work within centre access hours.",
            "We deliver single stores, flagship showrooms and multi-site rollouts, with consistent standards from site to site.",
        ],
        "considerations": [
            "Shopping centre fit-out guides and approvals",
            "Shopfronts, signage and display joinery",
            "Lighting that shows the product properly",
            "Hoarding and after-hours works",
            "Durable finishes for high-traffic areas",
            "Consistency across multi-site rollouts",
        ],
        "faqs": [
            ("Can you work within shopping centre requirements?",
             "Yes. We work from the centre's fit-out guide, prepare the submissions centre management needs, and schedule works within permitted hours."),
            ("Do you deliver multi-site rollouts?",
             "Yes. We build to a consistent specification across sites and stagger programs so each store opens on schedule."),
        ],
        "services": ["commercial-fit-outs", "commercial-refurbishment", "make-good"],
        "image": "Retail showroom with display joinery",
    },
    {
        "slug": "hospitality",
        "name": "Hospitality",
        "nav": "Hospitality fit-outs",
        "title": "Hospitality Fit-Outs Brisbane & SEQ | Forth Projects",
        "meta": "Restaurant, café, bar and venue fit-outs across SEQ and the Sunshine Coast. Kitchens, bars and dining spaces built for service and atmosphere.",
        "h1": "Hospitality fit-outs",
        "lead": "Restaurants, cafés, bars and venues built for busy service and lasting atmosphere.",
        "intro": [
            "Hospitality spaces work hard. Kitchens need the right exhaust, gas, plumbing and grease management; bars need durable, serviceable joinery; and the dining room has to look right on opening night and years later. We coordinate the technical side with your designer and kitchen consultant so the venue works as well as it looks.",
            "From neighbourhood cafés to multi-level venues, we plan the program around licensing, equipment deliveries and your opening date.",
        ],
        "considerations": [
            "Commercial kitchen exhaust, gas and grease management",
            "Food safety and council requirements",
            "Bar and back-of-house joinery",
            "Acoustic treatment for dining spaces",
            "Lighting and atmosphere",
            "Outdoor and alfresco dining areas",
        ],
        "faqs": [
            ("Do you coordinate kitchen equipment?",
             "Yes. We work with your kitchen consultant and suppliers so services, penetrations and exhaust are in place for equipment delivery and commissioning."),
            ("Can you refurbish a venue between busy periods?",
             "Yes. We can plan intensive works for quieter periods and stage the rest to limit lost trading."),
        ],
        "services": ["commercial-fit-outs", "commercial-refurbishment", "design-and-construct"],
        "image": "Restaurant interior with bar and timber battens",
    },
    {
        "slug": "health-medical",
        "name": "Health and medical",
        "nav": "Medical fit-outs",
        "title": "Medical Fit-Outs Brisbane & SEQ | Forth Projects",
        "meta": "Medical, dental and allied health fit-outs across Brisbane, the Gold Coast and Sunshine Coast. Clinical spaces built to the standards your practice needs.",
        "h1": "Medical and health fit-outs",
        "lead": "Clinics, practices and allied health spaces built to the standards your patients and practitioners rely on.",
        "intro": [
            "Medical fit-outs carry requirements general fit-outs don't: infection control, clinical hand basins, durable cleanable finishes, specialist equipment, and access for patients with limited mobility. We work with your designer and equipment suppliers so the space supports clinical workflow from reception to consult room.",
            "We fit out GP clinics, dental practices, specialist suites, physiotherapy and allied health spaces, and new medical centres.",
        ],
        "considerations": [
            "Infection control and cleanable finishes",
            "Clinical hand basins and plumbing",
            "Services and structural support for equipment",
            "Patient privacy and acoustic separation",
            "Accessible entries, consult rooms and amenities",
            "Coordination with your accreditation requirements",
        ],
        "faqs": [
            ("Do you work with medical equipment suppliers?",
             "Yes. We coordinate services, structural support and installation windows with your suppliers so equipment can be installed and commissioned on time."),
            ("Can you work around an operating practice?",
             "Yes. We stage works, maintain clean separation from clinical areas and schedule noisy work outside consulting hours."),
        ],
        "services": ["commercial-fit-outs", "commercial-construction", "design-and-construct"],
        "image": "Medical clinic reception and consult corridor",
    },
    {
        "slug": "education-childcare",
        "name": "Education and childcare",
        "nav": "Education and childcare",
        "title": "Childcare & Education Builders SEQ | Forth Projects",
        "meta": "Childcare centres, early learning and education fit-outs across SEQ and the Sunshine Coast. Safe, durable spaces built to regulatory requirements.",
        "h1": "Education and childcare",
        "lead": "Safe, durable learning spaces for early learning centres, schools and training providers.",
        "intro": [
            "Early learning and education buildings must meet building codes, the requirements of the National Quality Framework and the expectations of families. We build and fit out childcare centres and learning spaces with durable finishes, child-safe detailing and outdoor play areas, coordinated with your designer and approval requirements.",
            "We work on new purpose-built centres, conversions of existing buildings, and refurbishments of classrooms, libraries and training facilities, including works during school holidays.",
        ],
        "considerations": [
            "Indoor and outdoor space planning",
            "Child-safe detailing and finishes",
            "Nappy change, bathrooms and kitchens",
            "Outdoor play areas and shade",
            "Works scheduled around terms and holidays",
            "Accessible and secure entries",
        ],
        "faqs": [
            ("Can you work during school holidays?",
             "Yes. We plan intensive works for holiday periods and stage anything remaining so classes can continue safely."),
            ("Do you build new childcare centres?",
             "Yes, both new purpose-built centres and conversions of existing buildings, working with your designer and approval consultants."),
        ],
        "services": ["commercial-construction", "commercial-refurbishment", "design-and-construct"],
        "image": "Early learning centre with outdoor play area",
    },
    {
        "slug": "industrial-warehouse",
        "name": "Industrial and warehouse",
        "nav": "Industrial and warehouse",
        "title": "Industrial & Warehouse Builders SEQ | Forth Projects",
        "meta": "Warehouses, workshops, trade showrooms and industrial office fit-outs across Brisbane, Logan, Ipswich, the Gold Coast and Sunshine Coast.",
        "h1": "Industrial and warehouse",
        "lead": "Warehouses, workshops and showrooms built for operations, plus the offices that go with them.",
        "intro": [
            "Industrial projects are judged on how well the building supports the work inside it: clear spans, slab capacity, loading, power and the safe movement of people and vehicles. We build and refit warehouses, workshops, trade showrooms and the offices and amenities attached to them.",
            "Much of the region's industrial activity sits along its freight corridors, from the port and airport precincts to Logan, Ipswich, Yatala and the Sunshine Coast. We plan works to keep your operation running wherever possible.",
        ],
        "considerations": [
            "Slab, loading and racking requirements",
            "Power, three-phase and lighting upgrades",
            "Mezzanines and office pods",
            "Amenities and lunchrooms",
            "Hardstand, access and vehicle movement",
            "Staged works around operations",
        ],
        "faqs": [
            ("Do you fit out offices inside warehouses?",
             "Yes. Office, showroom and amenities fit-outs within industrial buildings are a common part of our industrial work."),
            ("Can you upgrade a warehouse for a new tenant?",
             "Yes. We can scope and deliver tenant-specific upgrades such as power, lighting, mezzanines and amenities to suit the incoming operation."),
        ],
        "services": ["commercial-construction", "commercial-fit-outs", "make-good"],
        "image": "Warehouse interior with office mezzanine",
    },
]

# ---------------------------------------------------------------- LOCATIONS
LOCATIONS = [
    {
        "slug": "brisbane",
        "name": "Brisbane",
        "title": "Commercial Builders Brisbane | Forth Projects",
        "meta": "Brisbane commercial builders for fit-outs, refurbishments and new construction, from the CBD and Fortitude Valley to Newstead and the northern industrial areas.",
        "lead": "Brisbane-based, delivering fit-outs, refurbishments and commercial construction across the city and its suburbs.",
        "intro": [
            "Brisbane is home base for Forth Projects. We work across the CBD's office towers, the hospitality and creative precincts of Fortitude Valley, Newstead and South Brisbane, and the commercial and industrial areas running north toward the airport and port.",
            "CBD and inner-city projects come with their own rules: building management requirements, loading dock bookings, restricted hours, and occupied floors above and below. We plan for those from day one so the work runs smoothly for you, the building and its neighbours.",
        ],
        "areas": ["Brisbane CBD", "Fortitude Valley", "Newstead", "Bowen Hills", "South Brisbane", "West End",
                  "Milton", "Toowong", "Woolloongabba", "Hamilton", "Eagle Farm", "Northgate", "Coopers Plains", "Rocklea"],
        "geo": (-27.4698, 153.0251),
        "image": "Brisbane CBD commercial interior",
    },
    {
        "slug": "gold-coast",
        "name": "Gold Coast",
        "title": "Commercial Builders Gold Coast | Forth Projects",
        "meta": "Gold Coast commercial builders for fit-outs, refurbishments and construction, from Southport and Broadbeach to Robina, Burleigh and the Yatala corridor.",
        "lead": "Fit-outs, refurbishments and commercial construction from the northern growth corridor to the southern beaches.",
        "intro": [
            "The Gold Coast's commercial activity spans the Southport CBD and the Gold Coast Health and Knowledge Precinct, hospitality and retail in Surfers Paradise, Broadbeach and Burleigh Heads, office hubs at Bundall, Robina and Varsity Lakes, and industrial estates at Yatala, Coomera and Molendinar.",
            "Tourism-driven businesses often need works completed outside peak seasons, and coastal exposure affects material choices. We plan programs and specifications around both.",
        ],
        "areas": ["Southport", "Surfers Paradise", "Broadbeach", "Bundall", "Robina", "Varsity Lakes", "Burleigh Heads",
                  "Palm Beach", "Coolangatta", "Nerang", "Helensvale", "Coomera", "Molendinar", "Yatala"],
        "geo": (-28.0167, 153.4000),
        "image": "Gold Coast hospitality venue",
    },
    {
        "slug": "sunshine-coast",
        "name": "Sunshine Coast",
        "title": "Commercial Builders Sunshine Coast | Forth Projects",
        "meta": "Commercial fit-outs, refurbishments and construction on the Sunshine Coast, from Maroochydore and Kawana to Caloundra, Noosa and Kunda Park.",
        "lead": "Fit-outs, refurbishments and new commercial buildings across one of Queensland's fastest-growing regions.",
        "intro": [
            "The Sunshine Coast's commercial base is growing quickly, led by the Maroochydore city centre, the health precinct around Sunshine Coast University Hospital at Birtinya, and expanding industrial areas around Kunda Park, Caloundra West and Coolum. Hospitality and retail remain strong along the coast from Caloundra to Noosa.",
            "Coastal sites bring their own considerations, including salt exposure, wind and humidity, which affect material and finish selection. We specify and build with those conditions in mind so your project lasts.",
        ],
        "areas": ["Maroochydore", "Mooloolaba", "Alexandra Headland", "Kawana Waters", "Birtinya", "Caloundra",
                  "Caloundra West", "Sippy Downs", "Buderim", "Nambour", "Kunda Park", "Coolum Beach", "Noosa Heads", "Noosaville"],
        "geo": (-26.6500, 153.0667),
        "image": "Sunshine Coast commercial building, coastal light",
    },
    {
        "slug": "ipswich",
        "name": "Ipswich",
        "title": "Commercial Builders Ipswich | Forth Projects",
        "meta": "Commercial fit-outs, refurbishments and construction in Ipswich and Springfield, including industrial and warehouse projects along the western corridor.",
        "lead": "Commercial and industrial projects across Ipswich, Springfield and the western corridor.",
        "intro": [
            "Ipswich combines a historic city centre with fast-growing Springfield Central and some of South East Queensland's largest industrial and logistics areas. Projects range from medical and education facilities to warehouses and trade showrooms.",
            "Older buildings in central Ipswich can carry heritage considerations, while newer estates often involve tenant fit-outs within large industrial buildings. We plan for both.",
        ],
        "areas": ["Ipswich Central", "Springfield Central", "Springfield Lakes", "Redbank", "Redbank Plains", "Bundamba",
                  "Booval", "Brassall", "Yamanto", "Wulkuraka", "Carole Park", "Goodna"],
        "geo": (-27.6144, 152.7581),
        "image": "Industrial showroom and office frontage",
    },
    {
        "slug": "logan",
        "name": "Logan",
        "title": "Commercial Builders Logan | Forth Projects",
        "meta": "Commercial fit-outs, refurbishments and construction across Logan, from Springwood and Loganholme to the Crestmead and Berrinba industrial areas.",
        "lead": "Fit-outs, refurbishments and construction along the Logan and M1 corridors.",
        "intro": [
            "Logan sits between Brisbane and the Gold Coast, with commercial centres at Springwood, Logan Central and Loganholme, a health precinct around Logan Hospital at Meadowbrook, and major industrial areas at Crestmead and Berrinba.",
            "New communities in growth areas such as Yarrabilba and Flagstone are driving demand for childcare, medical and retail space. We build and fit out these facilities on programs that suit developers and operators.",
        ],
        "areas": ["Springwood", "Logan Central", "Loganholme", "Underwood", "Slacks Creek", "Meadowbrook", "Beenleigh",
                  "Crestmead", "Berrinba", "Browns Plains", "Yarrabilba", "Flagstone"],
        "geo": (-27.6392, 153.1094),
        "image": "Medical centre in a suburban growth area",
    },
    {
        "slug": "moreton-bay",
        "name": "Moreton Bay",
        "title": "Commercial Builders Moreton Bay | Forth Projects",
        "meta": "Commercial fit-outs, refurbishments and construction across Moreton Bay, including North Lakes, Strathpine, Caboolture, Redcliffe and Brendale.",
        "lead": "Commercial projects across Brisbane's growing northern region, from Redcliffe to Caboolture.",
        "intro": [
            "Moreton Bay is one of the region's fastest-growing areas, with commercial centres at North Lakes, Strathpine, Caboolture and Redcliffe, the university precinct at Petrie, and established industrial estates at Brendale, Narangba and Burpengary.",
            "Population growth is bringing new medical, childcare, retail and hospitality projects, alongside industrial upgrades for businesses moving north. We plan each project around access, local requirements and your opening date.",
        ],
        "areas": ["North Lakes", "Mango Hill", "Petrie", "Strathpine", "Brendale", "Lawnton", "Narangba", "Burpengary",
                  "Morayfield", "Caboolture", "Redcliffe", "Kippa-Ring"],
        "geo": (-27.2340, 153.0210),
        "image": "Retail and medical precinct, northern Brisbane",
    },
    {
        "slug": "redland-city",
        "name": "Redland City",
        "title": "Commercial Builders Redland City | Forth Projects",
        "meta": "Commercial fit-outs, refurbishments and construction in Redland City, including Cleveland, Capalaba, Victoria Point and Redland Bay.",
        "lead": "Fit-outs and commercial works across the Redlands, from Capalaba to Redland Bay.",
        "intro": [
            "Redland City's commercial activity centres on Capalaba, Cleveland and Victoria Point, with retail, medical, hospitality and service businesses supporting a growing bayside population.",
            "We deliver fit-outs, refurbishments and smaller commercial buildings here with the same planning and attention to detail as every Forth project.",
        ],
        "areas": ["Capalaba", "Cleveland", "Ormiston", "Wellington Point", "Birkdale", "Alexandra Hills", "Thornlands",
                  "Victoria Point", "Redland Bay"],
        "geo": (-27.5280, 153.2660),
        "image": "Bayside café fit-out",
    },
]

# Location x service pages (highest-value search combinations)
COMBOS = {
    ("brisbane", "commercial-fit-outs"): [
        "From CBD office floors to Fortitude Valley venues and Newstead showrooms, Forth Projects delivers commercial fit-outs across Brisbane. We plan around building management requirements, loading dock bookings and after-hours works, so your fit-out progresses without friction with the landlord or neighbouring tenants.",
        "Whether it's a new lease, an expansion or a refresh of your existing space, we coordinate design, approvals and trades under one program and keep you informed throughout.",
    ],
    ("brisbane", "commercial-construction"): [
        "New commercial buildings across Brisbane's suburbs and growth areas: medical centres, childcare centres, showrooms, offices and light industrial buildings. Infill sites in established suburbs often bring tight access, close neighbours and council conditions to work through, and we plan logistics and staging to suit.",
        "Our pre-construction work focuses on cost, buildability and program before you commit, so the build starts on solid ground.",
    ],
    ("brisbane", "commercial-refurbishment"): [
        "Brisbane has a large stock of older commercial buildings that need upgrading to attract tenants and meet current standards. We refurbish lobbies, amenities, end-of-trip facilities and whole floors, often while the building stays occupied.",
        "For owners and asset managers, we program works around leasing campaigns and existing tenants, with clear reporting along the way.",
    ],
    ("gold-coast", "commercial-fit-outs"): [
        "Gold Coast fit-outs span Southport offices, Broadbeach and Burleigh hospitality venues, Robina retail, and medical suites near the Gold Coast Health and Knowledge Precinct. We plan works around peak trading periods, centre requirements and building access.",
        "Coastal conditions matter for fit-outs too, particularly for entries, outdoor areas and anything exposed to sea air. We select finishes that hold up.",
    ],
    ("gold-coast", "commercial-construction"): [
        "New commercial buildings along the Gold Coast's growth corridors, from Coomera and Helensvale to Robina and the southern suburbs. We build medical centres, childcare centres, showrooms, hospitality venues and industrial buildings.",
        "Coastal wind and corrosion requirements, flood and stormwater considerations, and busy road frontages all affect how a Gold Coast site is designed and built. We work through these with your consultants early.",
    ],
    ("gold-coast", "commercial-refurbishment"): [
        "Many Gold Coast venues, offices and retail centres date from earlier building booms and need upgrading to compete. We refurbish hospitality venues, office floors, lobbies and shopfronts while keeping businesses trading where possible.",
        "We schedule disruptive works outside holiday peaks and major events so you don't lose your busiest periods.",
    ],
    ("sunshine-coast", "commercial-fit-outs"): [
        "Fit-outs for offices in the Maroochydore city centre, medical and allied health suites around Birtinya and Kawana, and retail and hospitality from Caloundra to Noosa. We coordinate design, approvals and trades so your space opens on time.",
        "As the Coast grows, more businesses are relocating here or opening a second site. We can manage your project end to end, even if your head office is elsewhere.",
    ],
    ("sunshine-coast", "commercial-construction"): [
        "New commercial buildings across the Sunshine Coast's growth areas, including Maroochydore, Caloundra West, Sippy Downs and the industrial estates around Kunda Park and Coolum.",
        "Salt air, humidity and coastal wind influence structure, cladding and services selections on the Coast. We plan specifications and maintenance access so the building performs over the long term.",
    ],
    ("sunshine-coast", "commercial-refurbishment"): [
        "Refurbishment of offices, retail and hospitality premises across the Sunshine Coast, from Mooloolaba's waterfront venues to established centres in Nambour and Caloundra.",
        "Coastal exposure accelerates wear on older buildings, so refurbishments often include façade, roofing and services upgrades alongside the interior. We investigate first and price clearly.",
    ],
}

# ---------------------------------------------------------------- PROJECTS
# Add real case studies here. Pages, the projects index, filters and the sitemap
# all update automatically. Entries with "sample": True are built with noindex
# and kept out of the index and sitemap.
PROJECTS = [
    {
        "slug": "sample-project",
        "sample": True,
        "name": "Sample project name",
        "client": "Client or sector",
        "location": "Brisbane",
        "service": "commercial-fit-outs",
        "sector": "hospitality",
        "size": "000 m²",
        "program": "00 weeks",
        "summary": "One-sentence summary of the project and outcome.",
        "brief": "What the client needed and why.",
        "challenge": "The constraints: site, program, operations, approvals.",
        "outcome": "What was delivered and how it performs for the client.",
        "testimonial": ("A short quote from the client about working with Forth.", "Name, Role, Company"),
        "images": ["Hero image", "Detail one", "Detail two", "Detail three"],
    },
]

# ---------------------------------------------------------------- INSIGHTS
INSIGHTS = [
    {
        "slug": "commercial-fit-out-cost-factors",
        "title": "What affects the cost of a commercial fit-out",
        "seo_title": "What Affects Commercial Fit-Out Costs? | Forth Projects",
        "meta": "The main factors that drive the cost of a commercial fit-out in Queensland, and how to get an accurate budget before you sign a lease.",
        "date": "2026-10-02",
        "summary": "The main drivers of fit-out cost, and how to get a reliable budget before you commit to a lease.",
        "body": """
<p>Fit-out budgets go wrong for predictable reasons. Most of the cost is decided by a handful of factors, and almost all of them can be understood before you sign a lease. Here's what drives the number, and how to get a budget you can rely on.</p>
<h2>The condition of the space you're taking on</h2>
<p>A tenancy handed over as a clean shell with working base-building services costs far less to fit out than one that needs demolition, ceiling replacement or services rectification first. Ask what condition the space will be delivered in, and have your builder inspect it before you commit.</p>
<h2>Scope and level of finish</h2>
<p>Floor area matters, but scope matters more. Enclosed offices, meeting rooms, kitchens and amenities cost more per square metre than open areas. Custom joinery, feature ceilings, stone, timber and specialist lighting all add up quickly. Deciding early where you want to spend, such as reception and client areas, and where standard finishes will do, keeps the budget under control.</p>
<h2>Building services</h2>
<p>Changes to air conditioning, electrical, data, fire services and plumbing are often the least visible and most underestimated costs. Moving a kitchen, adding meeting rooms that need their own air supply, or relocating sprinklers to suit new walls can all carry significant cost. Many buildings also require the landlord's nominated contractors for some services.</p>
<h2>Building rules and working hours</h2>
<p>CBD towers and shopping centres often restrict noisy work, deliveries and access to certain hours. After-hours work costs more and takes longer to schedule. Your builder should read the landlord's fit-out guide before pricing, not after.</p>
<h2>Program</h2>
<p>A compressed program can mean more trades on site at once, overtime and premium freight for materials. Joinery, specialist equipment and some finishes have long lead times, so an early decision on these protects both the opening date and the budget.</p>
<h2>What's in and what's out</h2>
<p>Furniture, IT and AV equipment, signage, security and moving costs are often excluded from a fit-out price but are still part of the total project cost. List them up front so nothing arrives as a surprise.</p>
<h2>Landlord contributions</h2>
<p>Incentives such as a fit-out contribution or rent-free period can offset part of the cost. Knowing your likely fit-out cost before negotiating gives you a stronger position.</p>
<h2>Getting a reliable budget</h2>
<p>The most reliable approach is to involve a builder before you sign. A site inspection, a review of the landlord's requirements and a cost plan based on a test-fit layout will give you a realistic range and a sensible contingency. <a href="/contact/">Talk to us about your space</a> and we can help you understand what it's likely to involve.</p>
""",
        "related": ["commercial-fit-outs", "design-and-construct"],
    },
    {
        "slug": "make-good-what-tenants-should-plan-for",
        "title": "Make good: what tenants should plan for",
        "seo_title": "Make Good Obligations: A Guide for Tenants | Forth Projects",
        "meta": "What make good means at the end of a commercial lease, what's usually involved, and how tenants can plan the works and avoid disputes.",
        "date": "2026-10-02",
        "summary": "What make good usually involves at the end of a commercial lease, and how to plan it without last-minute stress.",
        "body": """
<p>"Make good" is the obligation in most commercial leases for the tenant to return the premises to an agreed condition when the lease ends. It's often left until the last few weeks, which is when it becomes expensive and stressful. A little planning changes that.</p>
<p><em>This guide is general information only. Your lease and your legal advisers are the authority on what your obligations are.</em></p>
<h2>Start with the lease</h2>
<p>Make good clauses vary widely. Some require the premises to be returned to their original condition at the start of the lease; others refer to a base building standard, or give the landlord discretion to decide what must be removed. Have your advisers confirm exactly what your clause requires.</p>
<h2>Find the starting point</h2>
<p>If a condition report or photos were taken when you moved in, they become very important. Without them, there's more room for disagreement about what the original condition was.</p>
<h2>What's commonly involved</h2>
<p>Typical make good works include removing partitions, joinery and signage; removing data and electrical cabling back to the base building; reinstating ceilings, lighting and flooring; patching and painting; and making services safe. In industrial tenancies it can also include removing racking, repairing slabs and reinstating hardstand areas.</p>
<h2>Physical works or a payment</h2>
<p>Some landlords will accept a payment instead of the works, particularly if they plan to refurbish for the next tenant. Pricing the physical works properly gives you a clear basis for that conversation.</p>
<h2>Timing</h2>
<p>Start planning several months before your lease ends. That allows time to agree the scope with the landlord, book trades and finish the works before the handback date, rather than paying holding-over rent while they're completed.</p>
<h2>Plan it with your next move</h2>
<p>If you're relocating, planning make good alongside your new fit-out means one program and one team coordinating both. Read more about our <a href="/services/make-good/">make good works</a>, or <a href="/contact/">get in touch</a> to arrange a site inspection.</p>
""",
        "related": ["make-good", "commercial-fit-outs"],
    },
    {
        "slug": "design-and-construct-vs-traditional-contracts",
        "title": "Design and construct vs traditional contracts",
        "seo_title": "Design and Construct vs Traditional Contracts | Forth Projects",
        "meta": "How design and construct compares with traditional design-bid-build contracts for commercial projects, and how to choose the right approach.",
        "date": "2026-10-02",
        "summary": "How the two main ways of procuring a commercial project compare, and which suits your situation.",
        "body": """
<p>Before a commercial project starts, you have to decide how it will be procured: who designs it, who builds it, and how they're contracted. The two most common approaches are a traditional contract and design and construct. Each has strengths.</p>
<h2>Traditional contracts</h2>
<p>In a traditional arrangement (sometimes called design-bid-build), you appoint an architect and consultants to complete the design, then tender the finished documents to builders for a price.</p>
<p>The advantages are direct control over every design decision, and competitive tendering on a complete set of drawings. The trade-offs are time, because design and construction happen one after the other, and the risk that the design comes back over budget once it's priced. Gaps between the design and what's actually buildable often surface as variations during construction.</p>
<h2>Design and construct</h2>
<p>In design and construct, one contractor is responsible for both design and construction. The builder engages and manages the designers, and design, cost and program are developed together.</p>
<p>The advantages are a single point of accountability, cost tested at each design stage rather than at the end, and the ability to overlap design and early works for a faster start. The trade-offs are that you need a clear brief up front, and you influence design through the brief and stage approvals rather than directing consultants yourself.</p>
<h2>Early contractor involvement</h2>
<p>A middle path is to bring the builder in early to advise on cost and buildability while your own consultants develop the design. This can suit projects where you want design control but also want pricing and program input before documentation is finished.</p>
<h2>Which suits your project?</h2>
<p>Design and construct tends to suit clients who want one relationship to manage, earlier cost certainty and a faster program. A traditional approach can suit clients who have a strong design vision, an established consultant team and the time to complete documentation before tendering.</p>
<p>If you're weighing up the options, <a href="/contact/">talk to us early</a>. We can explain how each approach would work for your project, and whether our <a href="/services/design-and-construct/">design and construct</a> service is a good fit.</p>
""",
        "related": ["design-and-construct", "commercial-construction"],
    },
]
