from django.utils.text import slugify


# Departments grouped by school, rendered as the columns of the PROGRAMS mega
# panel and, on small screens, as collapsible sections in the drawer.
# Slugs are explicit rather than derived with |slugify so a department resolves
# to the same URL here and in the "Our Course" carousel on the homepage.
#
# "courses" drives the dependent Course dropdown in the admission enquiry modal:
# pick a department there and only that department's courses are offered. This
# list is the single source for both, so adding a department to the menu adds it
# to the form automatically — but a department with no "courses" key will show an
# empty Course dropdown, so always fill it in.
#
# !! VERIFY BEFORE LAUNCH: the course names below follow the standard naming for
# each department (the pattern given for Computer Science & Engineering, applied
# outward). They have NOT been checked against the SVU prospectus. Correct any
# programme the university does not actually run, and add the ones it does.
SCHOOL_ENGINEERING = {
    "title": "School of Engineering",
    "departments": [
        {
            "label": "Department Of Computer Science & Engineering",
            "slug": "department-of-computer-science-engineering",
            "courses": [
                "Diploma In Computer Science and Engineering",
                "B.Tech In Computer Science and Engineering",
                "M.Tech In Computer Science and Engineering",
                "Ph.D. In Computer Science and Engineering",
            ],
        },
        {
            "label": "Department Of Civil Engineering",
            "slug": "department-of-civil-engineering",
            "courses": [
                "Diploma In Civil Engineering",
                "B.Tech In Civil Engineering",
                "M.Tech In Civil Engineering",
                "Ph.D. In Civil Engineering",
            ],
        },
        {
            "label": "Department Of Electrical Engineering",
            "slug": "department-of-electrical-engineering",
            "courses": [
                "Diploma In Electrical Engineering",
                "B.Tech In Electrical Engineering",
                "M.Tech In Electrical Engineering",
            ],
        },
        {
            "label": "Department Of Electronics & Communication",
            "slug": "department-of-electronics-communication-engineering",
            "courses": [
               
                "B.Tech In Electronics and Communication Engineering",
                "M.Tech In Electronics and Communication Engineering",
               
            ],
        },
        {
            "label": "Department Of Mechanical Engineering",
            "slug": "department-of-mechanical-engineering",
            "courses": [
                "Diploma In Mechanical Engineering",
                "B.Tech In Mechanical Engineering",
                "M.Tech In Mechanical Engineering",
                "Ph.D. In Mechanical Engineering",
            ],
        },
    ],
}

SCHOOL_HUMANITY = {
    "title": "School of Humanity & Social Science",
    "departments": [
        {
            "label": "Department Of Language, Literature And Cultural Studies",
            "slug": "department-of-language-literature-cultural-studies",
            "courses": [
                "B.A. In English",
                "M.A. In English",
                "Ph.D. In English",
            ],
        },
        {
            "label": "Department Of Journalism & Mass Communication",
            "slug": "department-of-mass-communication",
            "courses": [
                "B.A. In Journalism and Mass Communication",
                "M.A. In Journalism and Mass Communication",
            ],
        },
        {
            "label": "Department Of Education",
            "slug": "department-of-education",
            "courses": [
                "B.A (Hons.) in Education",
                "M.A in Education",
               
            ],
        },
    ],
}

SCHOOL_AGRICULTURE = {
    "title": "School of Agriculture",
    "departments": [
        {
            "label": "Department Of Agriculture",
            "slug": "department-of-agriculture",
            "courses": [
                "B.Sc. (Hons.) In Agriculture",
                "M.Sc. In Agriculture",
                
            ],
        },
    ],
}

SCHOOL_MANAGEMENT = {
    "title": "School of Management",
    "departments": [
        {
            "label": "Department Of Management Studies",
            "slug": "school-of-management",
            "courses": [
                "BBA (Bachelor Of Business Administration)",
                "BBA HM (Bachelor Of Business Administration In Hospital Management)",
                "BBA HHM (Bachelor Of Business Administration In Hotel & Hospital Management)",
                "BBA DM (Bachelor Of Business Administration In Digital Marketing)",
                "MBA (Master Of Business Administration)",
                "MBA FINANCE (Master Of Business Administration In Finance)",
                "MBA ABM (Master Of Business Administration In Agri Business Management)",
                "Ph.D. In Management Studies",
            ],
        },
    ],
}

SCHOOL_ALLIED_HEALTH = {
    "title": "School of Allied Health Services",
    "departments": [
        {
            "label": "Department Of Physiotherapy",
            "slug": "department-of-physiotherapy",
            "courses": [
                "BPT (Bachelor Of Physiotherapy)",
                "MPT (Master Of Physiotherapy)",
               
            ],
        },
        {
            "label": "Department Of Optometry",
            "slug": "department-of-optometry",
            "courses": [
                "B.Sc. In Optometry",
                
              
            ],
        },
        {
            "label": "Department Of Food & Nutrition",
            "slug": "department-of-food-nutrition",
            "courses": [
                "B.Sc (H) in Clinical Nutrition & Dietetics",
                "M.Sc in Food & Nutrition",
                
            ],
        },
        {
            "label": "Department Of Psychology",
            "slug": "department-of-psychology",
            "courses": [
                "M.Sc. / M.A in Applied Psychology (Specialization in Clinical Psychology)",
                
               
            ],
        },
        {
            "label": "Department Of Medical Laboratory Technology",
            "slug": "department-of-medical-laboratory-technology",
            "courses": [
                "Bachelor of Science (Hons.) in Medical Laboratory Technology",
              
            ],
        },
        {
            "label": "Department Of Medical Radiology & Imaging Technology",
            "slug": "department-of-medical-radiology-imaging-technology",
            "courses": [
                "B.Sc. in Medical Radiology & Imaging Technology",
                
            ],
        },
    ],
}

SCHOOL_LEGAL_STUDIES = {
    "title": "School of Legal Studies",
    "departments": [
        {
            "label": "Department Of Legal Studies",
            "slug": "department-of-legal-studies",
            "courses": [
                "BBA LL.B. (Hons.)",
                "LL.B.(Hons.)",
                "B.A. LL.B. (Hons.)",
               
            ],
        },
    ],
}

SCHOOL_COMPUTER_SCIENCE = {
    "title": "School of Computer Science",
    "departments": [
        {
            "label": "Department Of Computer Application",
            "slug": "department-of-computer-application",
            "courses": [
                "BCA (Bachelor Of Computer Application)",
                "MCA (Master Of Computer Application)",
               
            ],
        },
        {
            "label": "Department Of Data Science",
            "slug": "department-of-data-science",
            "courses": [
                "B.Tech in Data Science",
                "Master of Science in Data Science",
                
            ],
        },
        {
            "label": "Department Of Advanced Networking & Cyber Security",
            "slug": "department-of-cyber-security-and-advanced-networking",
            "courses": [
                "B.SC(H) In Advanced Networking And Cyber Security",
                "M.SC(H) In Advanced Networking And Cyber Security",
               
            ],
        },
        {
            "label": "Department Of Multimedia & Animation",
            "slug": "department-of-animation",
            "courses": [
                "Bachelor of Science (Hons.) in Multimedia & Animation",
                "MSc in Multimedia and Animation",
               
            ],
        },
    ],
}

SCHOOL_LIFE_SCIENCE = {
    "title": "School of Life Science",
    "departments": [
        {
            "label": "Department Of Biotechnology",
            "slug": "department-of-biotechnology",
            "courses": [
                "Bachelor of Science (Hons.) in Biotechnology",
                "Master of Science in Biotechnology",
               
            ],
        },
        {
            "label": "Department Of Microbiology",
            "slug": "department-of-microbiology",
            "courses": [
                "Bachelor of Science (Hons.) in Microbiology",
                "Master of Science in Microbiology",
               
            ],
        },
    ],
}

SCHOOL_BASIC_SCIENCE = {
    "title": "School of Basic Science",
    "departments": [
        {
            "label": "Department Of Mathematics",
            "slug": "department-of-mathematics",
            "courses": [
                "Master of Science in Mathematics",
               
            ],
        },
        {
            "label": "Department Of Chemistry",
            "slug": "department-of-chemistry",
            "courses": [
               
            ],
        },
        {
            "label": "Department Of Physics",
            "slug": "department-of-physics",
            "courses": [
                "Master of Science in Physics",
                
            ],
        },
    ],
}

# Four columns, balanced by row count (heading + departments) so the panel stays
# short enough to fit a laptop viewport — three columns pushed the tail of the
# longest column below the fold. Rebalance by moving a school between the lists.
# Weights: 8 / 9 / 9 / 9 rows.
PROGRAM_SCHOOL_COLUMNS = [
    [SCHOOL_ENGINEERING, SCHOOL_AGRICULTURE],
    [SCHOOL_MANAGEMENT, SCHOOL_ALLIED_HEALTH],
    [SCHOOL_COMPUTER_SCIENCE, SCHOOL_HUMANITY],
    [SCHOOL_LIFE_SCIENCE, SCHOOL_BASIC_SCIENCE, SCHOOL_LEGAL_STUDIES],
]

# The enquiry form reads the same schools, flattened out of the four-column
# layout — that grouping is a presentation detail of the mega panel and means
# nothing in a dropdown. Each school becomes an <optgroup> so 26 departments
# stay scannable instead of arriving as one long flat list.
ENQUIRY_SCHOOLS = [school for column in PROGRAM_SCHOOL_COLUMNS for school in column]

# slug -> course names, serialised into the page with |json_script and read by
# the dependent Course dropdown. Derived, never hand-maintained: a department
# can't drift out of sync with the menu because there is only one list.
ENQUIRY_COURSES = {
    department["slug"]: department.get("courses", [])
    for school in ENQUIRY_SCHOOLS
    for department in school["departments"]
}

ABOUT_MENU = {
    "who_we_are": [
        "Know Us", "Our team","Our Mentors", 
        "Recognition & Approvals", "Awards & Rankings", 
    ],
    "related_links": [
        "News", "IIC", "Faculty Lecture Series", "Governance",
        "Hostel Facility", "Student Services", "How to Reach Us?", "GATI Charter Institution",
        "ABET Engineering Accreditation",
    ],
}

SIMPLE_MENUS = {
    "placements": [
        "Placement Overview", "Top Recruiters", "Placement Records", "Training & Development",
        "Alumni in Industry",
    ],
}

ACADEMICS_MENU = {
    "links": [
        "Academics Overview", "Institutes", "Program (Courses)", "Academic Calendar",
        "List of Holidays", "Teaching Practices", "System of Evaluation",
        "Professional Bodies", "Professors of Practice",
    ],
    "promo_title": "Delivering",
    "promo_highlight": "Innovation Excellence",
    "promo_suffix": "in education",
    "tiles": [
        {"icon": "fa-layer-group", "label": "Flexible Choice Based Credit System"},
        {"icon": "fa-book-open-reader", "label": "70+ Electives"},
        {"icon": "fa-microchip", "label": "Advanced Technologies & Integration"},
        {"icon": "fa-diagram-project", "label": "Project based & Experiential Learning"},
    ],
}

ADMISSIONS_MENU = {
    "columns": [
        {
            "title": "JOB ORIENTED PROGRAMS",
            "links": [
                "After 12th", "After Graduation", "Leet Programs", "Specialized Programs",
                "Integrated Programs", "After Post Graduation", "SVU Advantages",
                "ABET Engineering Accreditation",
            ],
        },
        {
            "title": "ADMISSION",
            "links": [
                "Overview", "Course Fee", "How to Apply?", "Admission Criteria",
                "SVU Scholarship", "Education Loan", "Hostel Fee", "Orientation Schedule 2026",
            ],
        },
        {
            "title": "",
            "links": [
                "National Admissions", "International Admissions", "Admission Offices",
                "Visit the Campus", "Migration Policy", "Refund Policy",
            ],
        },
    ],
    "banner_title": "Unlock your Career Goals",
    "tiles": [
        {"icon": "fa-graduation-cap", "label": "Scholarships"},
        {"icon": "fa-hand-holding-dollar", "label": "Education Loan"},
        {"icon": "fa-file-signature", "label": "CUCET"},
    ],
}

CAMPUS_LIFE_MENU = {
    "banner_title": "A Home away from Home",
    "tiles": [
        {"icon": "fa-people-group", "label": "Youth Festivals & Summits"},
        {"icon": "fa-earth-asia", "label": "Culturally Diverse"},
        {"icon": "fa-heart", "label": "Student-Friendly"},
        {"icon": "fa-laptop", "label": "Technology integration"},
    ],
    "columns": [
        [
            "Overview", "Convocations", "Live-in-Concerts", "Tech Invent & Events",
            "Cultural & Cosmopolitan", "Evoke & Youth Summits", "Glorious Stars at SVU",
            "Sports & Adventure", "Latest News", "AI Fest 2026",
        ],
        [
            "Bollywood Celebrities", "Prominent Visitors",
            "SVU-RHYTHMS International Folklore Festival", "National & International Conferences",
            "International Faculties", "Notable Alumni", "Canadian Alumni Chapter",
            "Clubs, Communities, Department Societies & Student Chapters",
        ],
    ],
}

RESEARCH_MENU = {
    "heading": "Our",
    "heading_highlight": "Intellectual",
    "heading_suffix": "Pursuits",
    "stats": [
        {"value": "24000+", "label": "Research Publications"},
        {"value": "5900+", "label": "Patents Filed"},
        {"value": "30", "label": "Industry Sponsored Advanced Labs"},
        {"value": "200+", "label": "Departmental Research Groups"},
    ],
    "sections": [
        {
            "title": "RESEARCH INTENSIVE UNIVERSITY",
            "links": [
                "Research", "Patents", "Centers Of Research", "Centers of Excellence",
                "Visiting Scholars", "SVU Global Management Review", "SVU Law Review (SVULR)",
            ],
        },
        {
            "title": "ENTREPRENEURSHIP CELLS",
            "links": [
                "Technology Business Incubator (TBI)",
                "Innovation & Entrepreneurship Development Cell (IEDC)",
            ],
        },
        {
            "title": "SUSTAINABLE DEVELOPMENT GOALS (SDG'S)",
            "links": ["Policies & Strategies"],
        },
    ],
}

TOPBAR_ANNOUNCEMENTS = [
    "International Moot Court Competition on Artificial Intelligence & Intellectual Property Rights",
    "Admissions Open 2026 &mdash; Apply Now for Undergraduate & Postgraduate Programs",
    "Swami Vivekananda University Ranked Among India's Most Awarded Institutions",
]

# Utility links in the black bar above the logo. Three ways to write one:
#
#   "CAMPUSES"
#       plain string — the label doubles as the slug, so this opens
#       /page/campuses/. Renaming the label moves the link, which is why
#       anything that must stay put should use the dict form below.
#
#   {"label": "LIBRARY", "slug": "central-library"}
#       internal page whose URL differs from its label: /page/central-library/
#
#   {"label": "LIBRARY", "url": "https://opac.example.edu/"}
#       an external site. Opens in a new tab, gets rel="noopener", and is
#       marked with a small arrow so visitors know they are leaving the site.
#
# "url" wins if both are given. Same convention as RESEARCH_MEDIA in views.py.
TOP_NAV_LINKS = [
    "EVENTS",
    "GALLERY",
    {"label": "LIBRARY", "url": "https://www.swamivivekanandauniversity.ac.in/"},
    "STUDENT SERVICES",
    "CAREER",
    "BLOGS",
    "SVU PODCAST",
    {"label": "PAYMENT", "url": "https://www.swamivivekanandauniversity.ac.in/Pay-online/"},
    "CONTACT US",
]


def _resolve_nav_link(entry):
    """Normalise one TOP_NAV_LINKS entry into a dict the template can render.

    Doing this here rather than in the template keeps the markup to a single
    if/else, and means the three authoring forms above cost nothing at the
    point of use. slugify() at import time is safe — unlike reverse(), it does
    not need the URLConf to be loaded.
    """
    if isinstance(entry, str):
        return {"label": entry, "slug": slugify(entry), "external": False}

    label = entry["label"]
    url = entry.get("url")
    if url:
        return {"label": label, "url": url, "external": True}
    return {
        "label": label,
        "slug": entry.get("slug") or slugify(label),
        "external": False,
    }


TOP_NAV_LINKS_RESOLVED = [_resolve_nav_link(e) for e in TOP_NAV_LINKS]

MAIN_NAV = [
    {"label": "ABOUT", "slug": "about", "mega": "about"},
    {"label": "PROGRAMS", "slug": "programs", "mega": "programs"},
    {"label": "ACADEMICS", "slug": "academics", "mega": "academics"},
    {"label": "ADMISSIONS", "slug": "admissions", "mega": "admissions"},
    {"label": "CAMPUS LIFE", "slug": "campus-life", "mega": "campus-life"},
    {"label": "PLACEMENTS", "slug": "placements", "mega": "simple"},
    {"label": "RESEARCH & INNOVATION", "slug": "research-innovation", "mega": "research"},
]

SOCIAL_LINKS = [
    {"label": "Facebook", "icon": "facebook"},
    {"label": "LinkedIn", "icon": "linkedin"},
    {"label": "Instagram", "icon": "instagram"},
    {"label": "YouTube", "icon": "youtube"},
    # {"label": "X", "icon": "x"},
    # {"label": "Threads", "icon": "threads"},
]

FOOTER_COLUMNS = [
    # {
    #     "title": "School",
    #     "links": ["Engineering", "Agriculture", "Management", "Alied Health Services", "Computer Science", "Humanities", "Life Sciences", "Basic Sciences", "Legal Studies"],
    # },
    {
        "title": "Contact Us",
        "links": [
            {"label": "info@swamivivekanandauniversity.ac.in",
             "email": "info@swamivivekanandauniversity.ac.in"},
            # "tel" is the number the phone actually dials, so it is stripped of
            # the spaces and dashes the label wears for readability. Browsers
            # are forgiving about this, dialers on older handsets are not.
            {"label": "+91-7044086270", "tel": "+917044086270"},
            {"label": "+91-7980333922", "tel": "+917980333922"},
            {"label": "+91-9830278216", "tel": "+919830278216"},
            {"label": "+91-8961334184", "tel": "+918961334184"},
            {"label": "Telinipara, Barasat - Barrackpore Rd Bara Kanthalia, "
                      "West Bengal - 700121.",
             "text": True, "icon": "fa-solid fa-location-dot"},
        ],
    },
    {
        "title": "Admissions",
        "links": ["Admission Process", "Scholarships",  "Fee Structure", "FAQs"],
    },
    # Every URL below was checked and returns 200. Two worth noting:
    # cec.nic.in redirects to /cec/, and the NCC portal is indiancc.mygov.in —
    # nccindia.nic.in, the address usually given for it, no longer resolves.
    {
        "title": "Our Links",
        "links": [
            {"label": "NPTEL Courses", "url": "https://nptel.ac.in/"},
            {"label": "SWAYAM", "url": "https://swayam.gov.in/"},
            {"label": "NATS", "url": "https://nats.education.gov.in/"},
            {"label": "NDLI", "url": "https://ndl.iitkgp.ac.in/"},
            {"label": "e Sodh Ganga", "url": "https://shodhganga.inflibnet.ac.in/"},
            {"label": "e-PGPathshala", "url": "https://epgp.inflibnet.ac.in/"},
            {"label": "e-Education @ CEC", "url": "https://cec.nic.in/"},
        ],
    },
    {
        "title": "Our Links",
        "links": [
            {"label": "Digilocker", "url": "https://www.digilocker.gov.in/"},
            {"label": "NSS", "url": "https://nss.gov.in/"},
            {"label": "NCC", "url": "https://indiancc.mygov.in/"},
            # IQAC is one of the university's own bodies and BLOG is a section
            # of this site, so both stay internal. They land on the stub until
            # templates/pages/iqac.html and blogs.html are written.
            "IQAC",
            {"label": "BLOG", "slug": "blogs"},
        ],
    },
    {
        "title": "Quick Links",
        "links": ["Library", "Student Services", "Placements", "Research & Innovation", "Blogs", "Contact Us"],
    },
]


def _resolve_footer_link(entry):
    """Normalise one FOOTER_COLUMNS link into a dict the template can render.

    Five authoring forms, resolved to a "kind" the template switches on once,
    so the markup stays a single if/elif rather than sprouting a branch per
    column:

        "Scholarships"
            plain string — internal page at /page/scholarships/.

        {"label": "BLOG", "slug": "blogs"}
            internal page whose URL differs from its label.

        {"label": "SWAYAM", "url": "https://swayam.gov.in/"}
            external site. New tab, rel=noopener, marked with an arrow.

        {"label": "+91-7044086270", "tel": "+917044086270"}
            tel: link. Tapping it opens the dialer on a phone; on a desktop it
            hands off to whatever handles calls, or does nothing, which is the
            correct outcome rather than a 404.

        {"label": "info@…", "email": "info@…"}
            mailto: link, opening the visitor's own mail client already
            addressed. Deliberately NOT a Gmail compose URL: that would break
            for anyone on Outlook, Apple Mail or a work client, whereas mailto
            opens the Gmail app for a Gmail user anyway.

        {"label": "Telinipara, …", "text": True, "icon": "…"}
            not a link at all. Before this existed the postal address was run
            through slugify and turned into a link to
            /page/telinipara-barasat-barrackpore-rd-…/, a stub page that could
            never exist.

    "icon" is resolved here too so the template does not carry a mapping from
    kind to Font Awesome class.
    """
    if isinstance(entry, str):
        return {"label": entry, "kind": "page", "target": slugify(entry)}

    label = entry["label"]

    if entry.get("email"):
        return {"label": label, "kind": "link",
                "href": "mailto:%s" % entry["email"],
                "icon": "fa-regular fa-envelope"}

    if entry.get("tel"):
        return {"label": label, "kind": "link",
                "href": "tel:%s" % entry["tel"],
                "icon": "fa-solid fa-phone"}

    if entry.get("url"):
        return {"label": label, "kind": "link", "href": entry["url"],
                "icon": entry.get("icon", ""), "external": True}

    if entry.get("text"):
        return {"label": label, "kind": "text", "icon": entry.get("icon", "")}

    return {"label": label, "kind": "page",
            "target": entry.get("slug") or slugify(label),
            "icon": entry.get("icon", "")}


FOOTER_COLUMNS_RESOLVED = [
    {"title": col["title"], "links": [_resolve_footer_link(l) for l in col["links"]]}
    for col in FOOTER_COLUMNS
]


def nav_context(request):
    return {
        "topbar_announcements": TOPBAR_ANNOUNCEMENTS,
        "program_school_columns": PROGRAM_SCHOOL_COLUMNS,
        "enquiry_schools": ENQUIRY_SCHOOLS,
        "enquiry_courses": ENQUIRY_COURSES,
        "about_menu": ABOUT_MENU,
        "academics_menu": ACADEMICS_MENU,
        "admissions_menu": ADMISSIONS_MENU,
        "campus_life_menu": CAMPUS_LIFE_MENU,
        "research_menu": RESEARCH_MENU,
        "simple_menus": SIMPLE_MENUS,
        "top_nav_links": TOP_NAV_LINKS_RESOLVED,
        "main_nav": MAIN_NAV,
        "social_links": SOCIAL_LINKS,
        "footer_columns": FOOTER_COLUMNS_RESOLVED,
    }
