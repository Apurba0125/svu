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
                "Ph.D. In Electrical Engineering",
            ],
        },
        {
            "label": "Department Of Electronics & Communication",
            "slug": "department-of-electronics-communication-engineering",
            "courses": [
                "Diploma In Electronics and Communication Engineering",
                "B.Tech In Electronics and Communication Engineering",
                "M.Tech In Electronics and Communication Engineering",
                "Ph.D. In Electronics and Communication Engineering",
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
                "B.A. (Hons.) In English",
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
                "Ph.D. In Journalism and Mass Communication",
            ],
        },
        {
            "label": "Department Of Education",
            "slug": "department-of-education",
            "courses": [
                "B.Ed.",
                "M.Ed.",
                "Ph.D. In Education",
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
                "Ph.D. In Agriculture",
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
                "MBA (Master Of Business Administration)",
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
                "Ph.D. In Physiotherapy",
            ],
        },
        {
            "label": "Department Of Optometry",
            "slug": "department-of-optometry",
            "courses": [
                "B.Sc. In Optometry",
                "M.Sc. In Optometry",
                "Ph.D. In Optometry",
            ],
        },
        {
            "label": "Department Of Food & Nutrition",
            "slug": "department-of-food-nutrition",
            "courses": [
                "B.Sc. In Food and Nutrition",
                "M.Sc. In Food and Nutrition",
                "Ph.D. In Food and Nutrition",
            ],
        },
        {
            "label": "Department Of Psychology",
            "slug": "department-of-psychology",
            "courses": [
                "B.Sc. In Psychology",
                "M.Sc. In Psychology",
                "Ph.D. In Psychology",
            ],
        },
        {
            "label": "Department Of Medical Laboratory Technology",
            "slug": "department-of-medical-laboratory-technology",
            "courses": [
                "B.Sc. In Medical Laboratory Technology",
                "M.Sc. In Medical Laboratory Technology",
                "Ph.D. In Medical Laboratory Technology",
            ],
        },
        {
            "label": "Department Of Medical Radiology & Imaging Technology",
            "slug": "department-of-medical-radiology-imaging-technology",
            "courses": [
                "B.Sc. In Medical Radiology and Imaging Technology",
                "M.Sc. In Medical Radiology and Imaging Technology",
                "Ph.D. In Medical Radiology and Imaging Technology",
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
                "B.A. LL.B. (Hons.)",
                "LL.B.",
                "LL.M.",
                "Ph.D. In Law",
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
                "Ph.D. In Computer Application",
            ],
        },
        {
            "label": "Department Of Data Science",
            "slug": "department-of-data-science",
            "courses": [
                "B.Sc. In Data Science",
                "M.Sc. In Data Science",
                "Ph.D. In Data Science",
            ],
        },
        {
            "label": "Department Of Advanced Networking & Cyber Security",
            "slug": "department-of-cyber-security-and-advanced-networking",
            "courses": [
                "B.Sc. In Advanced Networking and Cyber Security",
                "M.Sc. In Advanced Networking and Cyber Security",
                "Ph.D. In Advanced Networking and Cyber Security",
            ],
        },
        {
            "label": "Department Of Multimedia & Animation",
            "slug": "department-of-animation",
            "courses": [
                "B.Sc. In Multimedia and Animation",
                "M.Sc. In Multimedia and Animation",
                "Ph.D. In Multimedia and Animation",
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
                "B.Sc. In Biotechnology",
                "M.Sc. In Biotechnology",
                "Ph.D. In Biotechnology",
            ],
        },
        {
            "label": "Department Of Microbiology",
            "slug": "department-of-microbiology",
            "courses": [
                "B.Sc. In Microbiology",
                "M.Sc. In Microbiology",
                "Ph.D. In Microbiology",
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
                "B.Sc. (Hons.) In Mathematics",
                "M.Sc. In Mathematics",
                "Ph.D. In Mathematics",
            ],
        },
        {
            "label": "Department Of Chemistry",
            "slug": "department-of-chemistry",
            "courses": [
                "B.Sc. (Hons.) In Chemistry",
                "M.Sc. In Chemistry",
                "Ph.D. In Chemistry",
            ],
        },
        {
            "label": "Department Of Physics",
            "slug": "department-of-physics",
            "courses": [
                "B.Sc. (Hons.) In Physics",
                "M.Sc. In Physics",
                "Ph.D. In Physics",
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
        "Know Us", "Our team","Our Mentors", "Vision & Mission", "Leadership", "Core Values",
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
        "enquiry_schools": ENQUIRY_SCHOOLS,
        "enquiry_courses": ENQUIRY_COURSES,
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
