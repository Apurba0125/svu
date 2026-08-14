from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.templatetags.static import static


LEGACY_STATS = [
    {"value": "200+", "label": "Industry Collaborations"},
    {"value": "50+", "label": "International MoUs"},
    {"value": "500+", "label": "Patents Filed"},
    {"value": "60+", "label": "Programs Offered"},
    {"value": "3,000+", "label": "Alumni Network"},
]

STAT_HIGHLIGHTS = [
    {"icon": static("img/Icon2.png"), "value": "150+", "label": "PHD Faculties"},
    {"icon": static("img/Icon3.png"), "value": "60+", "label": "Courses"},
    {"icon": static("img/Icon4.png"), "value": "200+", "label": "Industry Collaboration"},
    {"icon": static("img/Icon5.png"), "value": "98%", "label": "Placement"},
]

# "Life at SVU" tiles on the homepage. Each one links to /page/<slug>/, so the
# whole tile — image and caption — opens that page.
#
# The slug IS the filename of the page: build one by dropping
# templates/pages/<slug>.html into place, e.g. templates/pages/library.html.
# Until that file exists the link still works and shows the standard
# "under construction" stub, so nothing 404s while the pages are written.
#
# Slugs are lower case with hyphens to match every other page on the site.
# A tile with no "slug" renders as a plain, unclickable tile.
CAMPUS_GALLERY_ITEMS = [
    {"image": static("img/library.jpg"), "caption": "Library", "slug": "library"},
    {"image": static("img/lab.png"), "caption": "Laboratory", "slug": "laboratory"},
    {"image": static("img/classroom.jpg"), "caption": "Classroom", "slug": "classroom"},
    {"image": static("img/campus.png"), "caption": "Campus Building", "slug": "campus-building"},
    {"image": static("img/garden.png"), "caption": "Gardening", "slug": "gardening"},
    {"image": static("img/sports.png"), "caption": "Sports", "slug": "sports"},
    {"image": static("img/groupstudy.png"), "caption": "Group Study", "slug": "group-study"},
    {"image": static("img/lab-2.jpg"), "caption": "Practical Laboratory", "slug": "practical-laboratory"},
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

# Notice board on the homepage. "Read Details" opens the notice's own PDF in a
# new tab.
#
#   pdf   path to the document under static/, RELATIVE to static/ and WITHOUT a
#         leading slash — the template runs it through {% static %}, which adds
#         the hash and the prefix. Documents live in static/img/notice/.
#
#         Deliberately a bare string rather than static("…") the way
#         CAMPUS_GALLERY_ITEMS does it. static() here would run at import time,
#         and with the manifest storage a filename that has not been collected
#         raises ValueError during import — meaning gunicorn never starts and
#         the whole site is down, not just this panel. Resolved in the template
#         instead, the same mistake costs one page.
#
#         Drop "pdf" (or leave it "") and that notice falls back to the old
#         behaviour: /page/<title-slugified>/, which is the placeholder stub
#         until someone writes the page. So a notice without a document still
#         links somewhere sensible.
#
# AFTER ADDING OR REPLACING A PDF:  python manage.py collectstatic --noinput
# Not optional. A {% static %} path with no manifest entry raises ValueError on
# every request and takes the homepage down.
#
# The three files below are placeholders — real one page PDFs that open and
# say so. Overwrite them with the official notices, keeping the filenames.
NOTICE_ITEMS = [
    {
        "month": "Aug'26", "day": "14",
        "title": "Independence Day Celebration",
        "pdf": "img/notice/independence-day-celebration.pdf",
    },
    {
        "month": "Aug'26", "day": "13",
        "title": "Academic Calendar 2026-27",
        "pdf": "img/notice/Academic Calendar 2026-27.pdf",
    },
    {
        "month": "Aug'26", "day": "13",
        "title": "FDP_IKS_SVU_2026",
        "pdf": "img/notice/FDP_IKS_SVU-1.pdf",
    },
]

PLACEMENT_DRIVES = [
    {
        "name": "Netfotech Solutions",
        "color": "#3dae2b",
        "desc": "Netfotech Solutions for B.Tech / Bca  students of 2026 passing out batch.",
        "note": "Shortlisted Students",
    },
    {
        "name": "METCONNECT INFOTECH",
        "color": "#8dc63f",
        "desc": "METCONNECT INFOTECH PVT. LTD. for  B.Tech / BCA / MCA  of 2026 passing out batch.",
        "note": "",
    },
   
    {
        "name": "ICE MEDIA LAB",
        "color": "#141414",
        "desc": " ICE MEDIA LAB India for  / B.Tech (Computer Science) students of 2026 passing out batch.",
        "note": "Shortlisted Students",
    },
    {
        "name": "ZigZag AI",
        "color": "#0070c0",
        "desc": "ZigZag AI for  B.Tech (All Branches) students of 2026 passing out batch.",
        "note": "",
    },

     {
            "name": "Saasaro Technova Pvt Ltd",
            "color": "#173f8a",
            "desc": "Saasaro Technova Pvt Ltd for B.E / B.Tech  students of 2026 passing out batch.",
            "note": "",
        },
]

PLACED_STUDENTS = [
    {
        "first": "Bikash", "last": "Mondal", "company": "ShipBob",
        "package": "14.6", "image": static("img/logos/student1_com.png"),
    },
    {
        "first": "Anup", "last": "kumar Dey", "company": "GRSE",
        "package": "8.16", "image": static("img/logos/student2_com.png"),
    },
    {
        "first": "Anup", "last": "Maji", "company": "sinume Automation",
        "package": "8", "image": static("img/logos/student3_com.png"),
    },
    {
        "first": "Mounik", "last": "Ghosh", "company": "Varun Baverages",
        "package": "5", "image": static("img/logos/student4_com.png"),
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

# The recruiter marquee under the placement drives. Each entry is one slide.
#
#   logo    the company's logo, RELATIVE to static/ and WITHOUT a leading slash
#           — the template runs it through {% static %}. Files go in
#           static/img/logos/.
#
#           Leave it "" and the slide falls back to the company name set in
#           "color", exactly as this strip looked before. That is why every
#           entry below still carries name and color: the two are not
#           alternatives to be cleaned up later, they are the fallback, and a
#           logo that is ever removed lands back on readable text instead of a
#           gap in the marquee.
#
#           A bare string, not static("…"). static() runs at import time and
#           with the manifest storage an uncollected filename raises ValueError
#           during import, so gunicorn never starts and the whole site is down
#           rather than one strip. Resolved in the template, a typo costs one
#           page. Same rule as NOTICE_ITEMS.
#
#   name    always required. It is the alt text on the logo, so it is what a
#           screen reader and a failed image request both fall back to.
#
#   color   the text colour for the fallback. Ignored once a logo is set.
#
# AFTER ADDING A LOGO:  python manage.py collectstatic --noinput
#
# Use the company's own official logo file — a wordmark on transparent PNG or
# SVG reads best in the strip. They are trademarks, so take them from the
# company's press or brand page rather than redrawing or recolouring them.
# Aim for about 120px tall; the strip renders them at 44px and the extra gives
# a clean result on high-DPI screens.
HIRING_COMPANIES = [
    {"name": "John Deere", "color": "#141414", "logo": "img/logos/johndeere.png"},
    {"name": "TCS", "color": "#f37021", "logo": "img/logos/tcs.png"},
    {"name": "shipbob", "color": "#f37021", "logo": "img/logos/shipbob.png"},
    {"name": "UltraTech", "color": "#1e4b9c", "logo": "img/logos/Ultratech.png"},
    {"name": "Deloitte", "color": "#002d72", "logo": "img/logos/deloitte.png"},
    {"name": "Tech Mahindra", "color": "#00539f", "logo": "img/logos/techmahindra.png"},
    {"name": "Ecart", "color": "#e31837", "logo": "img/logos/ekart.png"},
    {"name": "Adani", "color": "#00a651", "logo": "img/logos/adani.png"},
    {"name": "Accenture", "color": "#5b2c91", "logo": "img/logos/accenture.png"},
    {"name": "GRSE", "color": "#5b2c91", "logo": "img/logos/grse.png"},
    {"name": "cognizant", "color": "#007cc3", "logo": "img/logos/cognizant.png"},
    {"name": "kyb", "color": "#ed1c24", "logo": "img/logos/kyb.png"},
    {"name": "TATA", "color": "#ed1c24", "logo": "img/logos/tata.png"},
    {"name": "wipro", "color": "#141414", "logo": "img/logos/wipro.png"},
    {"name": "Aditya Birla Capital", "color": "#141414", "logo": "img/logos/adityabirlacapital.png"},
]

GLOBAL_EXPERIENCE_ITEMS = [
    "My Campus Life",
    "Degree Programs",
    "Language Certificate",
    "International Faculty",
    "Career Pathways",
]

GLOBAL_ACCORDION_PANELS = [
    {"label": "Central Campus", "image": static("img/globaledu/cc.png"),"active": True},
    {"label": "Global Collaborations", "image": static("img/globaledu/globalcollab.png")},
    {"label": "Degree Opportunities", "image": static("img/globaledu/degreeopportunities.png")},
    {"label": "Language and Culture", "image": static("img/globaledu/language.png"), },
    {"label": "Career Pathways", "image": static("img/globaledu/cp.png")},
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

# Each card opens its YouTube video in a new tab. Paste the real watch URL into
# "url" — the placeholders below deliberately point nowhere so an unreplaced one
# is obvious rather than silently sending visitors to someone else's video.
# ("slug" is still supported as an alternative and opens /page/<slug>/ instead,
# but "url" wins when both are present.)
RESEARCH_MEDIA = [
    {"tag": "Why Study Civil Engineering?", "image": static("img/podcast/civil.jpg"), "url": "https://www.youtube.com/watch?v=q-kk3jtXz9I"},
    {"tag": "Food & Nutrition", "image": static("img/podcast/food.jpg"), "url": "https://www.youtube.com/watch?v=co-O7fs01Ro"},
    {"tag": "Civil Engineering Podcast", "image": static("img/podcast/civil2.jpg"), "url": "https://www.youtube.com/watch?v=2xLu_2pcyP8"},
    {"tag": "Optometry", "image": static("img/podcast/eye.jpg"), "url": "https://www.youtube.com/watch?v=BPn1xnN5fUY"},
    {"tag": "Biotechnology", "image": static("img/podcast/biotech.jpg"), "url": "https://www.youtube.com/watch?v=xJchmgshzAs"},
    {"tag": "Alvito D'Cunha", "image": static("img/podcast/play.jpg"), "url": "https://www.youtube.com/watch?v=MR1wKKw81FE"},
]

# "In the Spotlight" carousel on the homepage. Two kinds of card, both keeping
# every field they already had — nothing was renamed or removed.
#
#   image           EITHER a full external URL as a plain string, OR a local
#                   file via static("img/…") — the FUNCTION CALL, unquoted.
#                   Writing it as the string "static('img/…')" instead puts
#                   those inner quotes straight into the CSS the card is built
#                   from: url('static('img/…')') closes early, the whole
#                   background-image declaration is invalid, and the browser
#                   throws away the gradient with it. The card then renders
#                   white with white text on it — invisible, not merely
#                   missing a picture. Same rule as CAMPUS_GALLERY_ITEMS and
#                   AERIAL_SLIDES above.
#
#   type: "video"   the branded card with the play button.
#       url         WHERE THE PLAY BUTTON GOES. Paste the full YouTube watch or
#                   shorts URL here and the whole card becomes a link that opens
#                   it in a new tab. Leave it "" and the card renders exactly as
#                   before, with a play button that does not navigate — so an
#                   unfilled slide is inert rather than broken.
#       url_text    DISPLAY TEXT ONLY, printed in the strip along the bottom
#                   next to phone_text. It is not a link and never was. Putting
#                   a URL here shows the raw address on the card without making
#                   anything clickable, which is the trap this pair of fields
#                   invites — the address goes in "url", the words go here.
#       image, eyebrow, title, phone_text  unchanged.
#
#   type: "news"    the photo card with the red CTA button.
#       cta_slug    opens /page/<cta_slug>/ as before.
#       url         optional override for an external destination, same rule as
#                   RESEARCH_MEDIA above: "url" wins when both are present.
#       image, title, body, cta_label, tags  unchanged.
#
# Same convention as RESEARCH_MEDIA and TOP_NAV_LINKS, so there is one rule to
# remember across the site: an external "url" beats an internal slug.
SPOTLIGHT_SLIDES = [
    # {
    #     "type": "news",
    #     "image": "https://placehold.co/900x620/1a1a1a/1a1a1a",
    #     "title": "Not a Real Court⚖️... But It Feels Exactly Like One! 😱 | Law Moot Court ",
    #     "body": " Learn. Argue. Advocate. Succeed. …",
    #     "cta_label": "Scholarships",
    #     "cta_slug": "scholarships",
    #     "url": "",
    #     "tags": ["Scholarships", "Admissions"],
    # },
    # {
        
    #     "type": "video",
    #     "image": "https://placehold.co/900x620/141414/141414",
    #     "eyebrow": "Built for",
    #     "title": "Ambitious Bharat",
    #     "url": "",
    #     "url_text": "www.svu.ac.in",
    #     "phone_text": "Call: 7044086270",
    # },
    # {
    #     "type": "news",
    #     "image": "https://placehold.co/900x620/1a1a1a/1a1a1a",
    #     "title": "SVU Signs Landmark MoU for Global Student Exchange with 12 Partner Universities",
    #     "body": "Students across engineering, management and design programs will now be eligible for semester-abroad and dual-degree pathways …",
    #     "cta_label": "International",
    #     "cta_slug": "international",
    #     "url": "",
    #     "tags": ["International", "MoU"],
    # },
    # {
    #     "type": "video",
    #     "image": static("img/Shorts/motivation-1.jpg"),
    #     "eyebrow": "Explore",
    #     "title": "Motivational Video",
    #     "url": "https://www.facebook.com/reel/2225041254931372",
    #     "url_text": "swamivivekanandauniversity.ac.in",
    #     "phone_text": "Call: 7044086270",
    # },
    {
        "type": "video",
        "image": static("img/Shorts/Key To Success.png"),
        "eyebrow": "Explore",
        "title": "Key To Success",
        "url": "https://www.youtube.com/shorts/XjUHOBU1tTc",
        "url_text": "swamivivekanandauniversity.ac.in",
        "phone_text": "Call: 7044086270",
    },
    {
        "type": "video",
        "image": static("img/Shorts/1.png"),
        "eyebrow": "Explore",
        "title": "Virtual Lab",
        "url": "https://www.youtube.com/shorts/QI4D_vYJdRg",
        "url_text": "swamivivekanandauniversity.ac.in",
        "phone_text": "Call: 7044086270",
    },
    {
        "type": "video",
        "image": static("img/Shorts/mootcourt.png"),
        "eyebrow": "Explore",
        "title": "Law Moot Court ",
        "body": " Learn. Argue. Advocate. Succeed. …",
        "url": "https://www.youtube.com/shorts/mWRA03EiuGo",
        "url_text": "swamivivekanandauniversity.ac.in",
        "phone_text": "Call: 7044086270",
    },
    {
        "type": "video",
        "image": static("img/Shorts/neshamukhti.png"),
        "eyebrow": "Explore",
        "title": "Nasha Mukt Yuva for Viksit Bharat",
        "body": " Nasha Mukt Yuva: Building India’s Future",
        "url": "https://www.youtube.com/shorts/-Vk2kn4AYVQ",
        "url_text": "swamivivekanandauniversity.ac.in",
        "phone_text": "Call: 7044086270",
    },
    {
        "type": "video",
        "image": static("img/Shorts/ot.png"),
        "eyebrow": "Explore",
        "title": "OT Zones",
        "body": " Operating Theatre Zones Explained",
        "url": "https://www.youtube.com/shorts/GzY85e3B8l0",
        "url_text": "swamivivekanandauniversity.ac.in",
        "phone_text": "Call: 7044086270",
    },
    # {
    #     "type": "news",
    #     "image": "https://placehold.co/900x620/1a1a1a/1a1a1a",
    #     "title": "SVU Athletes Bring Home Gold and Silver at the 2026 Commonwealth Games",
    #     "body": "The university’s sports scholarship program continues to produce national and international medal-winning athletes …",
    #     "cta_label": "Sports & Adventure",
    #     "cta_slug": "sports-adventure",
    #     "url": "",
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


# Mentors for the Our Mentors page. "image" is a static-relative path resolved by
# {% static %} in the template rather than static() here, so adding a mentor
# never depends on the staticfiles manifest being built at import time.
# Drop a photo into static/img/our_mentors/ and add a row — the hero carousel and
# the scroll-stacked panels below it are both driven off this one list.
#
# "message" is the paragraph shown in the stacked panel. The copy below is
# neutral, third-person placeholder text describing the office, NOT a quotation:
# nobody should publish invented words under a real person's name. Replace each
# one with the mentor's own approved message before this page goes public.
#
# stat_label/stat_value are optional — leave blank and the stat block is hidden.
MENTOR_SLIDES = [
    {
        "image": "img/our_mentors/1707036444prof-dr-suranjan-das.jpeg",
        "name": "Prof. (Dr.) Suranjan Das",
        # "role": "Swami Vivekananda University",
        "role": "Vice-Chancellor, Adamas University",
        "message": (
            "The Vice Chancellor's office sets the academic direction of the "
            "university — curriculum design, research priorities, faculty "
            "development and accreditation. Students meet that work in the form "
            "of syllabi that keep pace with the field, laboratories that are "
            "actually used, and teachers who are still learning themselves."
        ),
        # "stat_label": "123",
        # "stat_value": "123",
    },
    {
        "image": "img/our_mentors/1707036474Dhrubajyoti-Chattopadhyay.jpeg",
        "name": "Prof. (Dr.) Dhrubajyoti Chattopadhyay",
        "role": "Vice Chancellor, Sister Nivedita University Kolkata",
        "message": (
            "The Vice Chancellor's office is where a student's record lives: admission, "
            "enrolment, examinations, results and the certificates that follow "
            "them into their career. Its work is to make sure the administrative "
            "side of a degree is never the thing that slows a student down."
        ),
        # "stat_label": "",
        # "stat_value": "",
    },
    {
        "image": "img/our_mentors/1707201511WhatsApp Image 2024-01-27 at 17.23.39.png",
        "name": "Prof. (Dr.) Shorosimohan Dan",
        "role": "Former Vice Chancellor , The University of Burdwan",
        "message": (
            "The Vice Chancellor's office is where a student's record lives: admission, "
            "enrolment, examinations, results and the certificates that follow "
            "them into their career. Its work is to make sure the administrative "
            "side of a degree is never the thing that slows a student down."
        ),
        # "stat_label": "",
        # "stat_value": "",
    },
    {
        "image": "img/our_mentors/17320970693. Prof. (Dr.)Deb Narayan Bandyopadhyay.png",
        "name": "Prof. (Dr.)Deb Narayan Bandyopadhyay",
        "role": "Founder Vice Chancellor,Bankura University",
        "message": (
            "The Vice Chancellor's office is where a student's record lives: admission, "
            "enrolment, examinations, results and the certificates that follow "
            "them into their career. Its work is to make sure the administrative "
            "side of a degree is never the thing that slows a student down."
        ),
        # "stat_label": "",
        # "stat_value": "",
    },
    {
        "image": "img/our_mentors/17363494544. Dr. Ranjan Chakrabarti.jpg",
        "name": "Prof. (Dr.) Ranjan Chakrabarti",
        "role": "Former Vice-Chancellor Vidyasar University",
        "message": (
            "The Vice Chancellor's office is where a student's record lives: admission, "
            "enrolment, examinations, results and the certificates that follow "
            "them into their career. Its work is to make sure the administrative "
            "side of a degree is never the thing that slows a student down."
        ),
        # "stat_label": "",
        # "stat_value": "",
    },
    {
        "image": "img/our_mentors/17322701125. Prof.(Dr.) Malayendu Saha.jpeg",
        "name": "Prof.(Dr.) Malayendu Saha",
        "role": "Former Vice-Chancellor , Kalyani University",
        "message": (
            "The Vice Chancellor's office is where a student's record lives: admission, "
            "enrolment, examinations, results and the certificates that follow "
            "them into their career. Its work is to make sure the administrative "
            "side of a degree is never the thing that slows a student down."
        ),
        # "stat_label": "",
        # "stat_value": "",
    },
    {
        "image": "img/our_mentors/17322700986. Prof.(Dr.) Mita Banerjee.jpeg",
        "name": "Prof.(Dr.) Mita Banerjee",
        "role": "Former Vice-Chancellor of The West Bengal University of Teachers' Training Education Planning and Administration",
        "message": (
            "The Vice Chancellor's office is where a student's record lives: admission, "
            "enrolment, examinations, results and the certificates that follow "
            "them into their career. Its work is to make sure the administrative "
            "side of a degree is never the thing that slows a student down."
        ),
        # "stat_label": "",
        # "stat_value": "",
    },

     {
            "image": "img/our_mentors/17322700817. Prof.(Dr.) Swapan Kumar Datta.jpeg",
            "name": "Prof.(Dr.) Swapan Kumar Datta",
            "role": "Former Vice-Chancellor Visva-Bharati & Biswa Bangla Biswabidyalay",
            "message": (
                "The Vice Chancellor's office is where a student's record lives: admission, "
                "enrolment, examinations, results and the certificates that follow "
                "them into their career. Its work is to make sure the administrative "
                "side of a degree is never the thing that slows a student down."
            ),
            # "stat_label": "",
            # "stat_value": "",
        },
         {
                "image": "img/our_mentors/1726321589asutosh.jpg",
                "name": "Prof.(Dr.) Ashutosh Ghosh",
                "role": "Former Vice-Chancellor Rani Rashmoni Green University , Former Pro Vice-Chancellor , (Academic Affairs) University of Calcutta",
                "message": (
                    "The Vice Chancellor's office is where a student's record lives: admission, "
                    "enrolment, examinations, results and the certificates that follow "
                    "them into their career. Its work is to make sure the administrative "
                    "side of a degree is never the thing that slows a student down."
                ),
                # "stat_label": "",
                # "stat_value": "",
            },
             {
                    "image": "img/our_mentors/1707201486184896.jpg",
                    "name": "Prof. (Dr.) Nemai Saha",
                    "role": "Former Vice-Chancellor , The University of Burdwan",
                    "message": (
                        "The Vice Chancellor's office is where a student's record lives: admission, "
                        "enrolment, examinations, results and the certificates that follow "
                        "them into their career. Its work is to make sure the administrative "
                        "side of a degree is never the thing that slows a student down."
                    ),
                    # "stat_label": "",
                    # "stat_value": "",
                },
                 {
                        "image": "img/our_mentors/17072853476 (1).jpg",
                        "name": "Dr. Baidyanath Chakrabarty",
                        "role": "Renowned Gynecologist and IVF Specialist",
                        "message": (
                            "The Vice Chancellor's office is where a student's record lives: admission, "
                            "enrolment, examinations, results and the certificates that follow "
                            "them into their career. Its work is to make sure the administrative "
                            "side of a degree is never the thing that slows a student down."
                        ),
                        # "stat_label": "",
                        # "stat_value": "",
                    },
                     
                         {
                                "image": "img/our_mentors/17072853737.jpg",
                                "name": "Padmashri Bikash Sinha",
                                "role": "Former Director of the Saha Institute of Nuclear Physics and Variable Energy Cyclotron Centre and the chairman of the Board of Governors of the National Institute of Technology, Durgapur",
                                "message": (
                                    "The Vice Chancellor's office is where a student's record lives: admission, "
                                    "enrolment, examinations, results and the certificates that follow "
                                    "them into their career. Its work is to make sure the administrative "
                                    "side of a degree is never the thing that slows a student down."
                                ),
                                # "stat_label": "",
                                # "stat_value": "",
                            },
                             {
                                    "image": "img/our_mentors/17072853858.jpg",
                                    "name": "Prof.(Dr.) Bashabi Fraser",
                                    "role": "Professor Emerita of English and Creative Writing Director, Scottish Centre of Tagore Studies (ScoTs) School of Arts & Creative Industries Edinburgh Napier University Honorary Fellow, Centre for South Asian Studies, University of Edinburgh",
                                    "message": (
                                        "The Vice Chancellor's office is where a student's record lives: admission, "
                                        "enrolment, examinations, results and the certificates that follow "
                                        "them into their career. Its work is to make sure the administrative "
                                        "side of a degree is never the thing that slows a student down."
                                    ),
                                    # "stat_label": "",
                                    # "stat_value": "",
                                },
                                 {
                                        "image": "img/our_mentors/17072853989.jpg",
                                        "name": "Prof. (Dr.) Neil Fraser",
                                        "role": "FProfessor, School of Social and Political Studies University of Edinburgh",
                                        "message": (
                                            "The Vice Chancellor's office is where a student's record lives: admission, "
                                            "enrolment, examinations, results and the certificates that follow "
                                            "them into their career. Its work is to make sure the administrative "
                                            "side of a degree is never the thing that slows a student down."
                                        ),
                                        # "stat_label": "",
                                        # "stat_value": "",
                                    },
                                     {
                                            "image": "img/our_mentors/170728540810.jpg",
                                            "name": "Prof.(Dr.) Arun Bandyopadhyay",
                                            "role": "Director, Gujarat Biotechnology University, Gandhinagar. Former Director, CSIR-Indian Institute of Chemical Biology, Kolkata",
                                            "message": (
                                                "The Vice Chancellor's office is where a student's record lives: admission, "
                                                "enrolment, examinations, results and the certificates that follow "
                                                "them into their career. Its work is to make sure the administrative "
                                                "side of a degree is never the thing that slows a student down."
                                            ),
                                            # "stat_label": "",
                                            # "stat_value": "",
                                        },
                                         {
                                                "image": "img/our_mentors/170720123911.png",
                                                "name": "Prof. (Dr.) Amlan Chakrabarti",
                                                "role": "Head IT & Tech. Innovation Cell, Dept. of Higher Education, Govt. of West Bengal, Professor and Director, A.K. Choudhury School of IT, University of Calcutta",
                                                "message": (
                                                    "The Vice Chancellor's office is where a student's record lives: admission, "
                                                    "enrolment, examinations, results and the certificates that follow "
                                                    "them into their career. Its work is to make sure the administrative "
                                                    "side of a degree is never the thing that slows a student down."
                                                ),
                                                # "stat_label": "",
                                                # "stat_value": "",
                                            },
                                             {
                                                    "image": "img/our_mentors/170720120612.jpeg",
                                                    "name": "Prof. (Dr.) Debprasad Chattopadhyay",
                                                    "role": "Founder Director & Scientist G at ICMR-National Institute of Traditional Medicine",
                                                    "message": (
                                                        "The Vice Chancellor's office is where a student's record lives: admission, "
                                                        "enrolment, examinations, results and the certificates that follow "
                                                        "them into their career. Its work is to make sure the administrative "
                                                        "side of a degree is never the thing that slows a student down."
                                                    ),
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
        # Opens the admission enquiry modal by itself a moment after the page
        # loads. The modal partial lives in base.html and is on every page, so
        # this flag is what keeps the pop-up to the homepage. Add it to another
        # view to auto-open there too; "Talk to us" still works everywhere.
        "enquiry_autoshow": True,
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
