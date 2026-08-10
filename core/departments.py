"""Department page content, keyed by the slug already used in the PROGRAMS mega
menu and the homepage "Our Course" carousel.

To publish a new department page:

1. Drop its images in ``static/img/departments/<slug>/`` (or reuse anything
   already in ``static/img/``).
2. Copy the block below, change the key to the department's existing slug and
   fill in the content.

That's it — the nav link and the course-carousel card for that slug stop
resolving to the "under construction" stub and start opening the real page,
because ``core.views.placeholder_page`` looks the slug up here first. Nothing
in the templates or the URLconf needs touching.

Slugs currently in use are listed in ``core/context_processors.py`` under
``PROGRAM_SCHOOL_COLUMNS``.

Every section is optional: leave ``courses``, ``faculty`` or ``tabs`` empty and
that section is skipped instead of rendering an empty heading.
"""

DEPARTMENTS = {
    "department-of-computer-science-engineering": {
        "name": "Department Of Computer Science & Engineering",
        # The intro heading is split so the tail can be tinted red.
        "title_lead": "Department Of Computer",
        "title_highlight": "Science & Engineering",
        "banner": "img/li_1.jpg",
        "intro_image": "img/comp1.png",
        "intro_body": (
            "Computer Science serves as the foundation for various technological advancements "
            "that the world sees today. The field has grown by leaps and bounds. The future "
            "innovations that it brings along never seem to slow down. Yet another beauty of "
            "computer science is that it finds a place in many interdisciplinary fields as well. "
            "With these, there also comes a necessity to keep up to the global demand of finding "
            "highly skilled engineers and scientists. Swami Vivekananda University drives on the "
            "purpose of providing quality education and improving competence among students, "
            "thereby living up to its motto, 'Progress Through Knowledge'."
        ),
        "courses": [
            {
                "level": "Diploma",
                "title": "Diploma in Computer Science",
                "excerpt": (
                    "The Diploma in Computer Science and Technology program at Swami Vivekananda "
                    "University builds practical, industry-ready skills from the first semester."
                ),
                "image": "img/comp1.png",
                "slug": "diploma-in-computer-science",
            },
            {
                "level": "B.Tech",
                "title": "B.Tech in Computer Science and Engineering",
                "excerpt": (
                    "A four-year programme covering algorithms, systems, AI and software "
                    "engineering, taught through project-based and experiential learning."
                ),
                "image": "img/cyber-sec.jpg",
                "slug": "b-tech-in-computer-science-and-engineering",
            },
            {
                "level": "M.Tech",
                "title": "M.Tech in Computer Science and Engineering",
                "excerpt": (
                    "A research-oriented postgraduate programme with specialisations spanning "
                    "data science, cyber security and intelligent systems."
                ),
                "image": "img/ba-data.jpg",
                "slug": "m-tech-in-computer-science-and-engineering",
            },
        ],
        # PLACEHOLDER FACULTY — replace with real people before publishing.
        # Leave "image" empty and the card falls back to an icon avatar rather
        # than showing a broken image or a stand-in photo of someone else.
        "faculty": [
            {
                "image": "",
                "name": "Faculty Name",
                "designation": "Professor & Head",
                "qualification": "Ph.D. (Computer Science & Engineering)",
                "publications": "40+ papers",
                "experience": "18 years",
                "research_area": "Distributed Systems, Cloud Computing",
                "slug": "faculty-profile",
            },
            {
                "image": "",
                "name": "Faculty Name",
                "designation": "Associate Professor",
                "qualification": "Ph.D. (Information Technology)",
                "publications": "26 papers",
                "experience": "12 years",
                "research_area": "Machine Learning, Computer Vision",
                "slug": "faculty-profile",
            },
            {
                "image": "",
                "name": "Faculty Name",
                "designation": "Assistant Professor",
                "qualification": "M.Tech, Ph.D. (pursuing)",
                "publications": "14 papers",
                "experience": "8 years",
                "research_area": "Cyber Security, Network Forensics",
                "slug": "faculty-profile",
            },
            {
                "image": "",
                "name": "Faculty Name",
                "designation": "Assistant Professor",
                "qualification": "M.Tech (Computer Science & Engineering)",
                "publications": "9 papers",
                "experience": "6 years",
                "research_area": "Data Mining, Natural Language Processing",
                "slug": "faculty-profile",
            },
            {
                "image": "",
                "name": "Faculty Name",
                "designation": "Assistant Professor",
                "qualification": "M.Tech (Computer Science & Engineering)",
                "publications": "9 papers",
                "experience": "6 years",
                "research_area": "Data Mining, Natural Language Processing",
                "slug": "faculty-profile",
            },
            {
                "image": "",
                "name": "Faculty Name",
                "designation": "Assistant Professor",
                "qualification": "M.Tech (Computer Science & Engineering)",
                "publications": "9 papers",
                "experience": "6 years",
                "research_area": "Data Mining, Natural Language Processing",
                "slug": "faculty-profile",
            },
        ],
        "tabs": [
            {
                "id": "mission-vision",
                "label": "Mission & Vision",
                "heading": "Mission & Vision",
                "intro": (
                    "The primary goal of the Department of Computer Science and Engineering is to "
                    "advance knowledge and education in the fields of computer science and "
                    "engineering. The department serves various objectives, including:"
                ),
                "points": [
                    {
                        "title": "Education",
                        "body": (
                            "The department aims to provide high-quality education to students at "
                            "various levels, including undergraduate, graduate and doctoral "
                            "programmes. The goal is to equip students with a solid foundation in "
                            "computer science and engineering principles, theories and practical skills."
                        ),
                    },
                    {
                        "title": "Research",
                        "body": (
                            "One of the key goals is to advance the state of knowledge in computer "
                            "science and engineering through research. Faculty members and students "
                            "engage in cutting-edge research projects that lead to innovations, "
                            "discoveries and contributions to the field's body of knowledge."
                        ),
                    },
                    {
                        "title": "Innovation",
                        "body": (
                            "The department fosters an environment that encourages innovation and "
                            "entrepreneurship, incubating new ideas, technologies and startups that "
                            "address real-world problems and contribute to societal progress."
                        ),
                    },
                    {
                        "title": "Technology Transfer",
                        "body": (
                            "In collaboration with industry partners, the department works on "
                            "technology transfer initiatives, facilitating the application of "
                            "research findings in practical settings through licensing and "
                            "industry-sponsored projects."
                        ),
                    },
                    {
                        "title": "Professional Development",
                        "body": (
                            "The department focuses on the professional development of its students "
                            "by providing internships, co-op programmes and industry connections, "
                            "preparing them for successful careers in computing."
                        ),
                    },
                ],
            },
            {
                "id": "core-values",
                "label": "Core Values",
                "heading": "Core Values",
                "intro": "The values that shape how the department teaches, researches and collaborates:",
                "points": [
                    {"title": "Academic Integrity", "body": "Honest, transparent and ethical conduct in teaching, assessment and research."},
                    {"title": "Inclusivity", "body": "A learning environment where students of every background are supported and heard."},
                    {"title": "Curiosity", "body": "Encouraging students to question, experiment and build beyond the syllabus."},
                    {"title": "Collaboration", "body": "Working across departments, institutions and industry to solve problems that matter."},
                ],
            },
            {
                "id": "salient-features",
                "label": "Salient Features",
                "heading": "Salient Features",
                "intro": "What distinguishes the department's approach to computing education:",
                "points": [
                    {"title": "Industry-Aligned Curriculum", "body": "Course content reviewed with industry partners so graduates enter the workforce current."},
                    {"title": "Advanced Laboratories", "body": "Dedicated labs for AI, cyber security, networking and high-performance computing."},
                    {"title": "Project-Based Learning", "body": "Every semester carries a build component, from first-year fundamentals to capstone projects."},
                    {"title": "Certification Support", "body": "Preparation and support for globally recognised industry certifications alongside the degree."},
                ],
            },
            {
                "id": "why-this-department",
                "label": "Why This Department",
                "heading": "Why This Department",
                "intro": "Reasons students choose to study computer science and engineering here:",
                "points": [
                    {"title": "Placement Record", "body": "A dedicated placement cell with recruiters spanning product, services and research organisations."},
                    {"title": "Research Exposure", "body": "Undergraduates are welcomed into faculty research groups rather than waiting for postgraduate study."},
                    {"title": "Mentorship", "body": "Every student is assigned a faculty mentor who tracks academic and career progress."},
                    {"title": "Student Chapters", "body": "Active coding clubs, hackathon teams and professional-body chapters running year-round."},
                ],
            },
            {
                "id": "message-desk",
                "label": "Message Desk",
                "heading": "Message Desk",
                "intro": (
                    "Computing is no longer a discipline students enter only to write software. It "
                    "underpins medicine, agriculture, finance and the arts. Our aim is to graduate "
                    "engineers who are fluent in the fundamentals, comfortable with change, and "
                    "grounded in the responsibility that comes with building technology people rely on."
                ),
                "points": [],
            },
        ],
    },
}
