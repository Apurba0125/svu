from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.templatetags.static import static


LEGACY_STATS = [
    {"value": "500+", "label": "Industry Collaborations"},
    {"value": "200+", "label": "International MoUs"},
    {"value": "1,350+", "label": "Patents Filed"},
    {"value": "50+", "label": "Programs Offered"},
    {"value": "5,000+", "label": "Alumni Network"},
]

STAT_HIGHLIGHTS = [
    {"icon": static("img/Icon2.png"), "value": "300+", "label": "PHD Faculties"},
    {"icon": static("img/Icon3.png"), "value": "50+", "label": "Courses"},
    {"icon": static("img/Icon4.png"), "value": "500+", "label": "Industry Collaboration"},
    {"icon": static("img/Icon5.png"), "value": "98%", "label": "Placement"},
]

CAMPUS_GALLERY_ITEMS = [
    {"image": static("img/library.jpg"), "caption": "Library"},
    {"image": static("img/lab.png"), "caption": "Laboratory"},
    {"image": static("img/classroom.jpg"), "caption": "Classroom"},
    {"image": static("img/campus.png"), "caption": "Campus Building"},
    {"image": static("img/garden.png"), "caption": "Gardening"},
    {"image": static("img/sports.png"), "caption": "Sports"},
    {"image": static("img/groupstudy.png"), "caption": "Group Study"},
    {"image": static("img/lab-2.jpg"), "caption": "Practical Laboratory"},
]

RANKING_GROUPS = [
    {
        "logo_text": "QS",
        "logo_year": "2027",
        "logo_sub": "World University Rankings",
        "expandable": False,
        "expanded": False,
        "primary_row": [
            {"rank": "1%", "desc": "Top Universities in India by QS World University Rankings 2027", "detail": "Among Top 10 Universities"},
            {"rank": "2%", "desc": "Top Universities Globally by QS World University Rankings 2027", "detail": "Global Rank #526"},
        ],
        "extra_rows": [],
    },
    {
        "logo_text": "QS",
        "logo_year": "2026",
        "logo_sub": "World University Rankings by Subject",
        "expandable": True,
        "expanded": False,
        "primary_row": [
            {"rank": "#251-300", "desc": "Among the World's Top 1% Universities by QS World University Rankings by Subject 2026", "detail": "Mechanical, Aeronautical & Manufacturing"},
            {"rank": "#251-300", "desc": "Among the World's Top 1% Universities by QS World University Rankings by Subject 2026", "detail": "Electrical and Electronics Engineering"},
        ],
        "extra_rows": [
            [
                {"rank": "#301-350", "desc": "Among the World's Top 1% Universities by QS World University Rankings by Subject 2026", "detail": "Computer Science & Information Systems"},
                {"rank": "#351-400", "desc": "Among the World's Top 1% Universities by QS World University Rankings by Subject 2026", "detail": "Civil & Structural Engineering"},
            ],
            [
                {"rank": "#401-450", "desc": "Among the World's Top 1% Universities by QS World University Rankings by Subject 2026", "detail": "Business & Management Studies"},
            ],
        ],
    },
    {
        "logo_text": "NIRF",
        "logo_year": "2025",
        "logo_sub": "National Institutional Ranking Framework",
        "expandable": True,
        "expanded": False,
        "primary_row": [
            {"rank": "19th", "desc": "Among The Best Universities in India by NIRF Rankings 2025"},
            {"rank": "31st", "desc": "Among The Best Institutions For Engineering In India by NIRF Rankings 2025"},
        ],
        "extra_rows": [
            [
                {"rank": "32nd", "desc": "Among The Best Institutions For Management Studies In India by NIRF Rankings 2025"},
                {"rank": "15th", "desc": "Among The Best Institutions For Pharmacy In India by NIRF Rankings 2025"},
            ],
            [
                {"rank": "14th", "desc": "Among The Best Institutions For Architecture & Planning In India by NIRF Rankings 2025"},
            ],
        ],
    },
]

ACCREDITATION_ROWS = [
    {
        "logo_text": "ABET",
        "logo_sub": "Engineering Accreditation Commission",
        "desc": "ABET Accreditation For Globally Recognized Engineering Programs",
        "programs": ["B.E. Chemical Engineering", "B.E. Computer Science and Engineering", "B.E. Electronics and Communication Engineering"],
    },
    {
        "logo_text": "ABET",
        "logo_sub": "Computing & Engineering Accreditation Commission",
        "desc": "ABET Accreditation For Globally Recognized Engineering Programs",
        "programs": ["B.E. Computer Science and Engineering"],
    },
]

NEWS_INTEREST = {
    # "image": "https://placehold.co/560x420/eeeeee/999999?text=Campus+Life",
    "topic": "Topic For News",
    "body": "Welcome to Swami Vivekananda University. We are an institution in West Bengal dedicated to the pursuit of knowledge and excellence and providing quality education to our students. Since our inception, we have been striving to provide our students with an exceptional learning experience.",
}

NOTICE_ITEMS = [
    {"month": "Aug'25", "day": "14", "title": "Independence Day Celebration"},
    {"month": "Aug'25", "day": "13", "title": "Special Supplementary Examination"},
    {"month": "Aug'25", "day": "12", "title": "Eligible Candidates to Appear in RET"},
]

PLACEMENT_DRIVES = [
    {
        "name": "Schneider Electric",
        "color": "#3dae2b",
        "desc": "Schneider Electric India Pvt. Ltd. for B.Tech / M.Tech (Mechanical / Power Systems / EE / EEE) students of 2026 passing out batch.",
        "note": "Shortlisted Students",
    },
    {
        "name": "Sify",
        "color": "#8dc63f",
        "desc": "Sify Technologies Limited for B.E / B.Tech (EEE, Mechanical) of 2026 passing out batch.",
        "note": "",
    },
    {
        "name": "JBM Group",
        "color": "#173f8a",
        "desc": "JBM Group for B.E / B.Tech (Mechanical, Electrical) students of 2026 passing out batch.",
        "note": "",
    },
    {
        "name": "Amazon",
        "color": "#141414",
        "desc": "Amazon India for B.E / B.Tech (Computer Science, Electronics) students of 2026 passing out batch.",
        "note": "Shortlisted Students",
    },
    {
        "name": "TCS",
        "color": "#0070c0",
        "desc": "Tata Consultancy Services for B.E / B.Tech (All Branches) students of 2026 passing out batch.",
        "note": "",
    },
]

PLACED_STUDENTS = [
    {
        "first": "Jaspreet", "last": "Singh", "company": "Amazon",
        "package": "25", "image": "https://placehold.co/460x620/1a2233/1a2233",
    },
    {
        "first": "Vandana", "last": "Chauhan", "company": "TCS",
        "package": "17", "image": "https://placehold.co/460x620/2a3324/2a3324",
    },
    {
        "first": "Rohan", "last": "Mehta", "company": "IBM",
        "package": "10", "image": "https://placehold.co/460x620/241a1a/241a1a",
    },
    {
        "first": "Ananya", "last": "Roy", "company": "Rich Panel",
        "package": "5", "image": "https://placehold.co/460x620/1a2422/1a2422",
    },
]

PLACEMENT_OVERVIEW_STATS = [
    {"value": "100+", "label": "Placement Offers", "tone": "beige"},
    {"value": "500+", "label": "Companies Visited for Recruitment", "tone": "grey"},
    {"value": "25", "suffix": "LPA", "label": "Highest National Package Offered", "tone": "black"},
    # {"value": "1.7", "suffix": "CR", "label": "Highest International Package Offered", "tone": "grey"},
]

PACKAGE_TIERS = [
    {"value": "5", "companies": "5+"},
    {"value": "4.5", "companies": "10+"},
    {"value": "3.5", "companies": "15+"},
    {"value": "2.40", "companies": "8+"},
    # {"value": "1.80", "companies": "25+"},
]

HIRING_COMPANIES = [
    {"name": "Amazon", "color": "#141414"},
    {"name": "TATA AIA", "color": "#1e4b9c"},
    {"name": "Tech Mahindra", "color": "#00539f"},
    {"name": "GoComet", "color": "#002d72"},
    {"name": "Focalyt", "color": "#e31837"},
    {"name": "EXPOSYS DATA LABS", "color": "#f37021"},
    {"name": "Skytel Tele Services", "color": "#ed1c24"},
    {"name": "METCONNECT INFOTECH", "color": "#00a651"},
    {"name": "ZigZag AI", "color": "#5b2c91"},
    {"name": " ICE MEDIA LAB", "color": "#141414"},
    {"name": "Saasaro Technova", "color": "#007cc3"},
    
]

GLOBAL_EXPERIENCE_ITEMS = [
    "My Campus Life",
    "Degree Programs",
    "Language Certificate",
    "International Faculty",
    "Career Pathways",
]

GLOBAL_ACCORDION_PANELS = [
    {"label": "Central Campus", "image": static("img/campaus.png"),"active": True},
    {"label": "Global Collaborations", "image": static("img/campaus.png")},
    {"label": "Degree Opportunities", "image": static("img/campaus.png")},
    {"label": "Language and Culture", "image": static("img/campaus.png"), },
    {"label": "International Research Projects", "image": static("img/campaus.png")},
    {"label": "International Faculty", "image": static("img/campaus.png")},
    {"label": "Career Pathways", "image": static("img/campaus.png")},
]

WHY_CHOOSE_CU = [
    {
        "title": "High-Impact Networking Connections",
        "body": "Connect with an extensive network of top CEOs, Nobel Laureates, eminent entrepreneurs, top scientists, industry innovators, and global academicians for collaboration, mentorship, and career advancement opportunities.",
        "image1": static("img/high-impact1.webp"),
        "image2": static("img/high-impact2.webp"),
    },
    {
        "title": "Tech-driven collaborative and fluid learning environments",
        "body": "Smart classrooms, AI-enabled labs and a culture built around applied, hands-on learning.",
        "image1": static("img/tech1.webp"),
        "image2": static("img/tech2.webp"),
    },
    {
        "title": "360-degree support in building a personal brand",
        "body": "Personal branding cells, LinkedIn workshops and mentorship to help every student stand out.",
        "image1": static("img/360-1.webp"),
        "image2": static("img/360-2.webp"),
    },
    {
        "title": "Multi-Disciplinary University",
        "body": "Freedom to combine majors and minors across 45+ disciplines under one roof.",
        "image1": static("img/multi-disciplinary1.webp"),
        "image2": static("img/multi-disciplinary2.webp"),
    },
    {
        "title": "Global Vision",
        "body": "Partnerships with universities across 68+ countries for exchange and dual-degree programs.",
        "image1": static("img/global-1.webp"),
        "image2": static("img/global-2.webp"),
    },
    {
        "title": "Intercontinental research frontiers & innovation ecosystem",
        "body": "Centres of Excellence driving research collaborations across continents.",
        "image1": static("img/interconinental-1.webp"),
        "image2": static("img/interconinental-2.webp"),
    },
    {
        "title": "Career Advancement",
        "body": "Dedicated placement cells, industry mentors and career-readiness programs.",
        "image1": static("img/career-1.webp"),
        "image2": static("img/career-2.webp"),
    },
    {
        "title": "Global Alumni Network",
        "body": "100,000+ alumni working across industries and geographies worldwide.",
        "image1": static("img/global-alumni-1.webp"),
        "image2": static("img/global-alumni-2.webp"),
    },
]

TESTIMONIALS = [


       # {
        #     "name_first": "Rohit", "name_last": "Kumar",
        #     "role": "Software Engineer at Google", "dept": "Computer Science & Engineering",
        #     "heading": 'From <strong>Engineering</strong> Labs to the <span class="alumni-hl">Skies of Duty</span>',
        #     "body": "Every takeoff begins with a strong runway and mine was built at Swami Vivekananda University. Proud to now serve as a Flying Officer in the Indian Air Force.",
        #     # "avatar": "https://placehold.co/120x120/1a2733/1a2733",
        #     "photo": static("img/testmonials/rohitkumar.png"),
        # },

    {
        "name_first": "Uhona", "name_last": "Thiessen",
        "role": "Senior Data Scientist at Meta", 
        "heading": 'From <strong>Engineering</strong> Labs to the <span class="alumni-hl">Data Scientist at Meta</span>',
        "body": "My experience @ SVU has been a very awesome one. The staff have been so accommodating. The students are very interested in our presentation. They asked very intelligent questions. We enjoyed our time very much.",
        "avatar": static("img/testmonials/uohnathiessen.png"),
        "photo": static("img/testmonials/uohnathiessen.png"),
    },


    {
            "name_first": "Dr. Abhay", "name_last": "Jere",
            "role": "Vice-chairman, AICTE", 
            # "heading": 'From <strong>Engineering</strong> Labs to the <span class="alumni-hl">Data Scientist at Meta</span>',
            "body": "Really enjoyed my visit. Wishing SVU all the best for future growth.",
            "avatar": static("img/testmonials/drabhajere.jfif"),
            "photo": static("img/testmonials/drabhajere.jfif"),
    },
 
]

RESEARCH_STATS = [
    {"value": "24000+", "label": "Research Papers Published"},
    {"value": "5900+", "label": "Scopus Indexed Papers"},
    {"value": "200+", "label": "Patents Granted"},
    {"value": "250+", "label": "Funded Research Projects"},
    {"value": "15+", "label": "Centres of Excellence"},
]

RESEARCH_MEDIA = [
    {"tag": "Moot Court", "image": static("img/mootcourt.png")},
    {"tag": "SVU Centre of Excellence", "image": static("img/ce.png")},
    {"tag": "Research Symposium", "image": static("img/rs.png")},
    {"tag": "Innovation Lab", "image": static("img/innovation.png")},
]

SPOTLIGHT_SLIDES = [
    {
        "type": "news",
        "image": "https://placehold.co/900x620/1a1a1a/1a1a1a",
        "title": "Swami Vivekananda University Felicitates 500+ Merit Scholars; Offers Scholarships up to 100% at SVU Scholars' Summit 2026",
        "body": "In a major push toward making world-class education accessible and reducing student dropouts, Swami Vivekananda University inaugurated …",
        "cta_label": "Scholarships",
        "cta_slug": "scholarships",
        "tags": ["Scholarships", "Admissions"],
    },
    {
        "type": "video",
        "image": "https://placehold.co/900x620/141414/141414",
        "eyebrow": "Built for",
        "title": "Ambitious Bharat",
        "url_text": "www.svu.ac.in",
        "phone_text": "Call: 7044086270",
    },
    {
        "type": "news",
        "image": "https://placehold.co/900x620/1a1a1a/1a1a1a",
        "title": "SVU Signs Landmark MoU for Global Student Exchange with 12 Partner Universities",
        "body": "Students across engineering, management and design programs will now be eligible for semester-abroad and dual-degree pathways …",
        "cta_label": "International",
        "cta_slug": "international",
        "tags": ["International", "MoU"],
    },
    {
        "type": "video",
        "image": "https://placehold.co/900x620/141414/141414",
        "eyebrow": "Shaping",
        "title": "Tomorrow's Leaders",
        "url_text": "www.svu.ac.in",
        "phone_text": "Call: 7044086270",
    },
    # {
    #     "type": "news",
    #     "image": "https://placehold.co/900x620/1a1a1a/1a1a1a",
    #     "title": "SVU Athletes Bring Home Gold and Silver at the 2026 Commonwealth Games",
    #     "body": "The university’s sports scholarship program continues to produce national and international medal-winning athletes …",
    #     "cta_label": "Sports & Adventure",
    #     "cta_slug": "sports-adventure",
    #     "tags": ["Campus Life", "Sports"],
    # },
]

AERIAL_SLIDES = [
    {"image": static("img/li_1.jpg"), "caption": "Sprawling Campus Infrastructure"},
    {"image": static("img/li_2.jpg"), "caption": "State-of-the-Art Learning Spaces"},
    {"image": static("img/li_3.jpg"), "caption": "Vibrant Student Life"},
]

NEWS_LIST_ITEMS = [
    {
        "date": "Jan 20", "category": "Accolades",
        "title": "Swami Vivekananda University bags 'AI-First Organisation' award at the Republic AI Summit & Awards 2026",
        "source": "Swami Vivekananda University",
        "image": "https://placehold.co/160x140/dddddd/888888?text=SVU",
    },
    {
        "date": "Jan 11", "category": "Extracurricular",
        "title": "Swami Vivekananda University Becomes Five Time AIU Inter University North Zone Youth Overall Champion",
        "source": "Swami Vivekananda University",
        "image": "https://placehold.co/160x140/dddddd/888888?text=SVU",
    },
    {
        "date": "Dec 06", "category": "KIUG 2025 Crown",
        "title": "Swami Vivekananda University Retains KIUG 2025 Crown With 67 Medals — Including 42 Gold, 14 Silver & 11 Bronze!",
        "source": "Swami Vivekananda University",
        "image": "https://placehold.co/160x140/dddddd/888888?text=SVU",
    },
    {
        "date": "Apr 11", "category": "Competition",
        "title": "SVU Campus Ambassadors Secure 1st Runner-Up at LinkedIn Dragon's Den",
        "source": "Swami Vivekananda University",
        "image": "https://placehold.co/160x140/dddddd/888888?text=SVU",
    },
    {
        "date": "Mar 02", "category": "Research",
        "title": "SVU Researchers Publish Breakthrough Study in Nature Communications",
        "source": "Swami Vivekananda University",
        "image": "https://placehold.co/160x140/dddddd/888888?text=SVU",
    },
]

NEWS_FEATURED_SLIDES = [
    {
        "image": static("img/news1.jpg"),
        "date": "Jan 23", "category": "AI Fest",
        "headline": "Swami Vivekananda University Launches West Bengal's First 'AI Fest 2026' to Empower Young Innovators and Transform Ideas into Tech-Driven Solutions for a Digital Bharat",
        "cta_label": "AI Fest 2026",
    },
    {
        "image": static("img/news2.jpg"),
        "date": "Feb 14", "category": "Convocation",
        "headline": "Swami Vivekananda University Celebrates Its Largest Convocation Ceremony with 5,000+ Graduating Students",
        "cta_label": "Convocation 2026",
    },
    {
        "image": static("img/news3.jpg"),
        "date": "Mar 10", "category": "Innovation",
        "headline": "SVU Innovation Tank Backs 40 Student Startups with Seed Funding and Mentorship",
        "cta_label": "Innovation Tank",
    },
    {
        "image": static("img/news4.jpg"),
        "date": "Mar 10", "category": "Innovation",
        "headline": "SVU Innovation Tank Backs 40 Student Startups with Seed Funding and Mentorship",
        "cta_label": "Innovation Tank",
    },
]

NEWS_SIDE_CARDS = [
    {
        "image": static("img/event1.jpg"),
        "date": "June 08", "category": "Influencer Visit",
        "headline": "1st counelling meeting at Swami Vivekananda University with 2026 batch students",
        "source": "Campus Life",
        "quote": "",
        "quote_name": "Gaurav Taneja",
    },
    {
        "image": static("img/event2.jpg"),
        "date": "May 13", "category": "SVU Visit",
        "headline": "Swami Vivekananda University Welcomes Renowned AI Researcher Dr. Ananya Gupta for a Seminar on 'AI in Healthcare'",
        "source": "Campus Life",
        "quote": "", "quote_name": "",
    },
]


# Slides for the Our Mentors hero. "image" is a static-relative path resolved by
# {% static %} in the template rather than static() here, so adding a mentor
# never depends on the staticfiles manifest being built at import time.
# Drop a photo into static/img/our_mentors/ and add a row to slide it in.
# stat_label/stat_value are optional — leave blank and the stat block is hidden.
MENTOR_SLIDES = [
    {
        "image": "img/our_mentors/vc.png",
        "name": "Prof. (Dr.) Subrata Dey",
        # "role": "Swami Vivekananda University",
        "role": "Vice Chancellor, Swami Vivekananda University",
        # "stat_label": "123",
        # "stat_value": "123",
    },
    {
        "image": "img/our_mentors/deputy_register.png",
        "name": "Tanmoy Mazumder",
        "role": "Deputy Register, Swami Vivekananda University",
        # "stat_label": "",
        # "stat_value": "",
    },
]


def home(request):
    context = {
        "legacy_stats": LEGACY_STATS,
        "ranking_groups": RANKING_GROUPS,
        "accreditation_rows": ACCREDITATION_ROWS,
        "news_interest": NEWS_INTEREST,
        "notice_items": NOTICE_ITEMS,
        "placement_drives": PLACEMENT_DRIVES,
        "placed_students": PLACED_STUDENTS,
        "placement_overview_stats": PLACEMENT_OVERVIEW_STATS,
        "package_tiers": PACKAGE_TIERS,
        "global_accordion_panels": GLOBAL_ACCORDION_PANELS,
        "testimonials": TESTIMONIALS,
        "aerial_slides": AERIAL_SLIDES,
        "hiring_companies": HIRING_COMPANIES,
        "stat_highlights": STAT_HIGHLIGHTS * 4,
        "campus_gallery_items": CAMPUS_GALLERY_ITEMS,
        "global_experience_items": GLOBAL_EXPERIENCE_ITEMS,
        "why_choose_cu": WHY_CHOOSE_CU,
        "research_stats": RESEARCH_STATS,
        "research_media": RESEARCH_MEDIA,
        "spotlight_slides": SPOTLIGHT_SLIDES,
        "news_list_items": NEWS_LIST_ITEMS,
        "news_featured_slides": NEWS_FEATURED_SLIDES,
        "news_side_cards": NEWS_SIDE_CARDS,
    }
    return render(request, "core/home.html", context)


def mentors(request):
    return render(request, "core/mentors.html", {"mentor_slides": MENTOR_SLIDES})


def placeholder_page(request, slug):
    """Serve templates/pages/<slug>.html when it exists, else the stub.

    Every nav link and course-carousel card already points here, so building a
    department or course page is just dropping a file into templates/pages/
    named after its slug — no Python, no URLconf entry, no registry.

    The slug comes from the <slug:slug> URL converter, which only matches
    [-a-zA-Z0-9_]+. No dots or slashes can reach the template path.
    """
    template = f"pages/{slug}.html"
    try:
        get_template(template)
    except TemplateDoesNotExist:
        title = slug.replace("-", " ").title()
        return render(request, "core/placeholder.html", {"title": title})

    return render(request, template)
