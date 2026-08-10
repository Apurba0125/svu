# Departments grouped by school, rendered as the columns of the PROGRAMS mega
# panel and, on small screens, as collapsible sections in the drawer.
# Slugs are explicit rather than derived with |slugify so a department resolves
# to the same URL here and in the "Our Course" carousel on the homepage.
SCHOOL_ENGINEERING = {
    "title": "School of Engineering",
    "departments": [
        {"label": "Department Of Computer Science & Engineering", "slug": "department-of-computer-science-engineering"},
        {"label": "Department Of Civil Engineering", "slug": "department-of-civil-engineering"},
        {"label": "Department Of Electrical Engineering", "slug": "department-of-electrical-engineering"},
        {"label": "Department Of Electronics & Communication", "slug": "department-of-electronics-communication-engineering"},
        {"label": "Department Of Mechanical Engineering", "slug": "department-of-mechanical-engineering"},
    ],
}

SCHOOL_HUMANITY = {
    "title": "School of Humanity & Social Science",
    "departments": [
        {"label": "Department Of Language, Literature And Cultural Studies", "slug": "department-of-language-literature-cultural-studies"},
        {"label": "Department Of Journalism & Mass Communication", "slug": "department-of-mass-communication"},
        {"label": "Department Of Education", "slug": "department-of-education"},
    ],
}

SCHOOL_AGRICULTURE = {
    "title": "School of Agriculture",
    "departments": [
        {"label": "Department Of Agriculture", "slug": "department-of-agriculture"},
    ],
}

SCHOOL_MANAGEMENT = {
    "title": "School of Management",
    "departments": [
        {"label": "Department Of Management Studies", "slug": "school-of-management"},
    ],
}

SCHOOL_ALLIED_HEALTH = {
    "title": "School of Allied Health Services",
    "departments": [
        {"label": "Department Of Physiotherapy", "slug": "department-of-physiotherapy"},
        {"label": "Department Of Optometry", "slug": "department-of-optometry"},
        {"label": "Department Of Food & Nutrition", "slug": "department-of-food-nutrition"},
        {"label": "Department Of Psychology", "slug": "department-of-psychology"},
        {"label": "Department Of Medical Laboratory Technology", "slug": "department-of-medical-laboratory-technology"},
        {"label": "Department Of Medical Radiology & Imaging Technology", "slug": "department-of-medical-radiology-imaging-technology"},
    ],
}

SCHOOL_LEGAL_STUDIES = {
    "title": "School of Legal Studies",
    "departments": [
        {"label": "Department Of Legal Studies", "slug": "department-of-legal-studies"},
    ],
}

SCHOOL_COMPUTER_SCIENCE = {
    "title": "School of Computer Science",
    "departments": [
        {"label": "Department Of Computer Application", "slug": "department-of-computer-application"},
        {"label": "Department Of Data Science", "slug": "department-of-data-science"},
        {"label": "Department Of Advanced Networking & Cyber Security", "slug": "department-of-cyber-security-and-advanced-networking"},
        {"label": "Department Of Multimedia & Animation", "slug": "department-of-animation"},
    ],
}

SCHOOL_LIFE_SCIENCE = {
    "title": "School of Life Science",
    "departments": [
        {"label": "Department Of Biotechnology", "slug": "department-of-biotechnology"},
        {"label": "Department Of Microbiology", "slug": "department-of-microbiology"},
    ],
}

SCHOOL_BASIC_SCIENCE = {
    "title": "School of Basic Science",
    "departments": [
        {"label": "Department Of Mathematics", "slug": "department-of-mathematics"},
        {"label": "Department Of Chemistry", "slug": "department-of-chemistry"},
        {"label": "Department Of Physics", "slug": "department-of-physics"},
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

ABOUT_MENU = {
    "who_we_are": [
        "Overview", "Our Identity","Our Mentors", "Vision & Mission", "Leadership", "Core Values",
        "Recognition & Approvals", "Awards & Rankings", "Institutional Social Responsibility",
        "SVU Edge",
    ],
    "related_links": [
        "Institutes & Departments", "Admissions", "Scholarships", "Governance",
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

TOP_NAV_LINKS = [
    "CAMPUSES", "INTERNATIONAL", "LIBRARY", "STUDENT SERVICES", "CAREER", "BLOGS",
    "SVU PODCAST", "CONTACT US",
]

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
    {"label": "X", "icon": "x"},
    {"label": "LinkedIn", "icon": "linkedin"},
    {"label": "Instagram", "icon": "instagram"},
    {"label": "YouTube", "icon": "youtube"},
    {"label": "Threads", "icon": "threads"},
]

FOOTER_COLUMNS = [
    {
        "title": "Programs",
        "links": ["Engineering", "Management", "Computing", "Commerce", "Law", "Design", "Pharmacy", "Architecture"],
    },
    {
        "title": "About",
        "links": ["Overview", "Leadership", "Vision & Mission", "Awards & Rankings", "SVU Edge", "Careers at SVU"],
    },
    {
        "title": "Admissions",
        "links": ["Admission Process", "Scholarships", "International Admissions", "Fee Structure", "FAQs"],
    },
    {
        "title": "Campus Life",
        "links": ["Hostel Facility", "Sports", "Clubs & Societies", "Events & Fests", "Campus Tour"],
    },
    {
        "title": "Quick Links",
        "links": ["Library", "Student Services", "Placements", "Research & Innovation", "Blogs", "Contact Us"],
    },
]


def nav_context(request):
    return {
        "topbar_announcements": TOPBAR_ANNOUNCEMENTS,
        "program_school_columns": PROGRAM_SCHOOL_COLUMNS,
        "about_menu": ABOUT_MENU,
        "academics_menu": ACADEMICS_MENU,
        "admissions_menu": ADMISSIONS_MENU,
        "campus_life_menu": CAMPUS_LIFE_MENU,
        "research_menu": RESEARCH_MENU,
        "simple_menus": SIMPLE_MENUS,
        "top_nav_links": TOP_NAV_LINKS,
        "main_nav": MAIN_NAV,
        "social_links": SOCIAL_LINKS,
        "footer_columns": FOOTER_COLUMNS,
    }
