<div align="center">

<img src="https://img.shields.io/badge/ResumeForge-Professional%20Resume%20Builder-e94560?style=for-the-badge&logo=django&logoColor=white" alt="ResumeForge Banner"/>

<br/>
<br/>

# ⬡ ResumeForge

### Build Professional Resumes That Get You Hired

A full-featured **Django-powered Resume Builder** with 6 stunning templates, AJAX-driven editor, PDF export, and a secure authentication system.

<br/>

[![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat-square&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![WeasyPrint](https://img.shields.io/badge/WeasyPrint-PDF%20Export-e94560?style=flat-square)](https://weasyprint.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

<br/>

[Features](#-features) • [Templates](#-templates) • [Tech Stack](#-tech-stack) • [Installation](#-installation) • [Project Structure](#-project-structure) • [Usage](#-usage) • [API Reference](#-api-reference) • [Contributing](#-contributing)

<br/>

</div>

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Templates](#-templates)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Environment Setup](#-environment-setup)
- [Usage Guide](#-usage-guide)
- [Database Models](#-database-models)
- [URL Reference](#-url-reference)
- [PDF Export](#-pdf-export)
- [Authentication System](#-authentication-system)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 About the Project

**ResumeForge** is a professional-grade resume builder built with **Django** and **Bootstrap 5**. It allows users to create, manage, and export multiple resumes using beautifully designed templates — all from a clean, intuitive interface.

Users can fill in their details section by section (personal info, work experience, education, skills, projects, certifications, languages, awards, and volunteer work), preview their resume in real-time, and download a pixel-perfect PDF — all without writing a single line of code.

### Why ResumeForge?

- 🔐 **Secure** — each user's resumes are private and protected by Django's auth system
- 🎨 **Beautiful** — 6 professionally designed templates with 8 accent color options
- ⚡ **Fast** — AJAX-powered editor with no full-page reloads
- 📄 **Accurate** — PDF export matches the browser preview exactly
- 🧠 **Smart** — optional sections keep the CV clean and ATS-friendly
- 📱 **Responsive** — works on desktop, tablet, and mobile

---

## ✨ Features

### 🔐 Authentication
- User registration with first name, last name, email, and username
- Secure login and logout
- Session-based authentication
- Each user can only access their own resumes

### 📝 Resume Editor
- **AJAX-powered** — add, edit, and delete items without page reloads
- **Sidebar navigation** — jump between sections instantly
- **Section counts** — see how many items are in each section
- **Optional sections** — skip any section you don't need
- **Profile photo upload** — supported on all templates
- **Auto-save feedback** — toast notifications on every save

### 🎨 Templates & Styling
- **6 unique templates** — Modern, Classic, Minimal, Executive, Creative, Tech
- **8 accent colors** — customize the color scheme of any template
- **Live preview** — see exactly how your resume looks before exporting
- **Print toolbar** — sticky toolbar on every template with Edit, PDF, and Print buttons

### 📄 PDF Export
- Pixel-perfect PDF export via **WeasyPrint**
- Fallback to browser print dialog if WeasyPrint is not installed
- Downloaded file is named `{full_name}_{template}.pdf`

### 📊 Dashboard
- View all your saved resumes at a glance
- See resume details: template type, number of jobs, education, skills
- Quick actions: Edit, Preview, Export PDF, Delete
- Last-updated timestamps

---

## 🖼️ Templates

| Template | Style | Best For | Font |
|----------|-------|----------|------|
| 🎨 **Modern** | Two-column with colored sidebar | Most industries | Raleway + Open Sans |
| 📋 **Classic** | Centered header, elegant layout | Finance, Law, Academia | EB Garamond + Lato |
| ◻️ **Minimal** | Single-column, ultra clean | Design, Startups | Inter |
| 👔 **Executive** | Premium two-column | Senior roles, C-Suite | Cormorant Garamond + Montserrat |
| ✨ **Creative** | Asymmetric dark sidebar | Design, Marketing, Media | Playfair Display + DM Sans |
| 💻 **Tech** | GitHub-dark terminal style | Developers, Engineers | JetBrains Mono + IBM Plex Sans |

---

## 🛠️ Tech Stack

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.10+ | Core language |
| Django | 4.2+ | Web framework |
| SQLite | Built-in | Database (default) |
| WeasyPrint | 60.0+ | PDF generation |
| Pillow | 10.0+ | Image processing for profile photos |
| Whitenoise | 6.5+ | Static file serving |

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| Bootstrap | 5.3 | UI framework |
| Bootstrap Icons | 1.11 | Icon library |
| Google Fonts | — | Typography |
| Vanilla JavaScript | ES6+ | AJAX interactions |

### Development
| Tool | Purpose |
|------|---------|
| Git | Version control |
| GitHub | Remote repository |
| `venv` | Python virtual environment |
| Django Admin | Database management UI |

---

## 📁 Project Structure

```
resumebuilder/                          ← Project root
│
├── manage.py                           ← Django management CLI
├── requirements.txt                    ← Python dependencies
├── db.sqlite3                          ← SQLite database (auto-generated)
├── .gitignore                          ← Git ignore rules
├── README.md                           ← This file
│
├── resumebuilder/                      ← Django project config
│   ├── __init__.py
│   ├── settings.py                     ← Project settings
│   ├── urls.py                         ← Root URL configuration
│   └── wsgi.py                         ← WSGI entry point
│
├── builder/                            ← Main Django application
│   ├── __init__.py
│   ├── apps.py                         ← App configuration
│   ├── models.py                       ← Database models (9 models)
│   ├── views.py                        ← All views + AJAX endpoints
│   ├── forms.py                        ← Django forms with styled widgets
│   ├── urls.py                         ← App URL patterns
│   ├── admin.py                        ← Django admin registration
│   │
│   ├── migrations/                     ← Database migrations
│   │   └── __init__.py
│   │
│   └── templates/
│       ├── builder/
│       │   ├── base.html               ← Base template (dark theme UI)
│       │   ├── landing.html            ← Marketing homepage
│       │   ├── dashboard.html          ← User's resume dashboard
│       │   ├── resume_create.html      ← Template & color picker
│       │   ├── resume_edit.html        ← Full AJAX resume editor
│       │   │
│       │   └── cv_templates/           ← The 6 CV designs
│       │       ├── modern.html
│       │       ├── classic.html
│       │       ├── minimal.html
│       │       ├── executive.html
│       │       ├── creative.html
│       │       └── tech.html
│       │
│       └── registration/
│           ├── login.html              ← Login page
│           └── register.html          ← Registration page
│
├── static/                             ← Static files directory
│   ├── css/
│   ├── js/
│   └── img/
│
└── media/                              ← User-uploaded files (auto-generated)
    └── profile_photos/
```

---

## 🚀 Installation

### Prerequisites

Make sure you have the following installed:

- **Python 3.10+** → [Download](https://www.python.org/downloads/)
- **Git** → [Download](https://git-scm.com/)
- **pip** (comes with Python)

### Step 1 — Clone the Repository

```bash
git clone https://github.com/yourusername/resumeforge.git
cd resumeforge
```

### Step 2 — Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5 — Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

### Step 6 — Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000
```

Admin panel:

```
http://127.0.0.1:8000/admin
```

---

## ⚙️ Environment Setup

### `requirements.txt`

```
Django>=4.2,<5.0
Pillow>=10.0
weasyprint>=60.0
whitenoise>=6.5
```

### Key Settings (`resumebuilder/settings.py`)

```python
# Authentication redirects
LOGIN_URL          = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# Media files (profile photos)
MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

### WeasyPrint System Dependencies

WeasyPrint requires some system libraries. Install them based on your OS:

```bash
# Ubuntu / Debian
sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz0b

# macOS (with Homebrew)
brew install pango

# Windows
# Follow: https://doc.courtbouillon.org/weasyprint/stable/first_steps.html
```

---

## 📖 Usage Guide

### 1. Register an Account
Navigate to `/register/` and create your free account.

### 2. Create a Resume
Click **New Resume** on the dashboard. Choose:
- A **template** (Modern, Classic, Minimal, Executive, Creative, Tech)
- An **accent color** (8 options)
- A **resume title** (e.g., "Software Engineer — Google Application")

### 3. Fill In Your Details
The editor has **10 sections** in the left sidebar:

| Section | Required | Notes |
|---------|----------|-------|
| 👤 Personal Info | Recommended | Name, title, contact, photo, summary |
| 💼 Work Experience | Optional | Multiple entries supported |
| 🎓 Education | Optional | Multiple entries supported |
| ⚡ Skills | Optional | Group by category, set levels |
| 🚀 Projects | Optional | Include tech stack tags |
| 🏆 Certifications | Optional | Include credential IDs |
| 🌐 Languages | Optional | Set proficiency levels |
| 🎖️ Awards | Optional | Honors and recognition |
| 🤝 Volunteer Work | Optional | Community involvement |
| 🎨 Style & Template | — | Change template or color anytime |

### 4. Preview Your Resume
Click the **Preview** button (top right) to open your resume in a new tab — exactly as it will look in the PDF.

### 5. Export as PDF
Click **Export PDF** to download a pixel-perfect PDF of your resume.

---

## 🗄️ Database Models

### `Resume`
Core model holding personal info and template settings.

| Field | Type | Description |
|-------|------|-------------|
| `user` | ForeignKey | Owner of the resume |
| `title` | CharField | Internal title (e.g., "Google Application") |
| `template` | CharField | Template name (modern, classic, etc.) |
| `accent_color` | CharField | Hex color code |
| `full_name` | CharField | Display name on CV |
| `job_title` | CharField | Professional headline |
| `email` | EmailField | Contact email |
| `phone` | CharField | Contact phone |
| `location` | CharField | City, Country |
| `website` | URLField | Personal website |
| `linkedin` | CharField | LinkedIn profile URL |
| `github` | CharField | GitHub profile URL |
| `summary` | TextField | Professional summary paragraph |
| `photo` | ImageField | Profile photo |

### `WorkExperience`

| Field | Type | Description |
|-------|------|-------------|
| `resume` | ForeignKey | Parent resume |
| `company` | CharField | Employer name |
| `position` | CharField | Job title |
| `location` | CharField | Office location |
| `start_date` | CharField | e.g., "Jan 2020" |
| `end_date` | CharField | e.g., "Dec 2022" |
| `is_current` | BooleanField | Hides end date if true |
| `description` | TextField | Bullet points / achievements |

### `Education`

| Field | Type | Description |
|-------|------|-------------|
| `institution` | CharField | University / School name |
| `degree` | CharField | e.g., "Bachelor of Science" |
| `field_of_study` | CharField | e.g., "Computer Science" |
| `gpa` | CharField | e.g., "3.8/4.0" |

### `Skill`

| Field | Type | Description |
|-------|------|-------------|
| `name` | CharField | Skill name |
| `level` | CharField | beginner / intermediate / advanced / expert |
| `category` | CharField | e.g., "Programming Languages" |

### Other Models
`Project`, `Certification`, `Language`, `Award`, `VolunteerWork` — all follow the same pattern with `resume` as a ForeignKey and relevant fields.

---

## 🌐 URL Reference

| URL | View | Description |
|-----|------|-------------|
| `/` | `landing` | Homepage |
| `/register/` | `register_view` | User registration |
| `/login/` | `login_view` | User login |
| `/logout/` | `logout_view` | User logout |
| `/dashboard/` | `dashboard` | Resume dashboard |
| `/resume/create/` | `resume_create` | Create new resume |
| `/resume/<pk>/edit/` | `resume_edit` | Edit resume |
| `/resume/<pk>/preview/` | `resume_preview` | Preview resume |
| `/resume/<pk>/pdf/` | `resume_pdf` | Download PDF |
| `/resume/<pk>/delete/` | `resume_delete` | Delete resume |
| `/resume/<pk>/save-personal/` | `resume_save_personal` | AJAX save personal info |
| `/resume/<pk>/save-meta/` | `resume_save_meta` | AJAX save template/color |
| `/resume/<pk>/section/<section>/add/` | `section_add` | AJAX add section item |
| `/resume/<pk>/section/<section>/<id>/update/` | `section_update` | AJAX update item |
| `/resume/<pk>/section/<section>/<id>/delete/` | `section_delete` | AJAX delete item |
| `/admin/` | Django Admin | Admin panel |

---

## 📄 PDF Export

PDF generation uses **WeasyPrint**, which renders the exact same HTML/CSS as the browser preview.

```python
# In views.py
from weasyprint import HTML

html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
pdf_bytes = html.write_pdf()
```

### Fallback Behavior
If WeasyPrint is not installed, the PDF endpoint renders the template in `print_mode`, allowing the user to use the browser's **Ctrl+P** / **⌘+P** print dialog to save as PDF.

### Adding a New Template
1. Create `builder/templates/builder/cv_templates/yourtemplate.html`
2. Add to `TEMPLATE_CHOICES` in `models.py`:
   ```python
   ('yourtemplate', 'Your Template Name'),
   ```
3. Done — the system auto-discovers it.

---

## 🔐 Authentication System

ResumeForge uses **Django's built-in authentication** system with custom forms and views.

### Registration Flow
```
User fills RegisterForm → Validates → Creates User object → Auto login → Redirect to dashboard
```

### Login Flow
```
User fills LoginForm → Django authenticates → Session created → Redirect to dashboard
```

### Route Protection
All resume-related views are protected with `@login_required`:

```python
@login_required
def dashboard(request):
    resumes = Resume.objects.filter(user=request.user)  # Only their own
    ...
```

### Data Isolation
Every database query filters by `user=request.user`, so users can **never** access another user's resumes — even by guessing URLs.

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### 1. Fork the repository
Click the **Fork** button at the top of this page.

### 2. Clone your fork
```bash
git clone https://github.com/yourusername/resumeforge.git
cd resumeforge
```

### 3. Create a feature branch
```bash
git checkout -b feature/your-feature-name
```

### 4. Make your changes and commit
```bash
git add .
git commit -m "Add: your feature description"
```

### 5. Push and open a Pull Request
```bash
git push origin feature/your-feature-name
```

Then open a Pull Request on GitHub.

### Contribution Ideas
- 🌍 Add more language translations
- 📐 Create additional CV templates
- 🌙 Dark mode for the CV preview
- 📊 Resume analytics / completion score
- 🔗 Share resume via public link
- 📧 Email resume as PDF attachment
- 🖨️ Multiple paper sizes (A4, Letter)

---

## 📜 License

```
MIT License

Copyright (c) 2024 ResumeForge

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🙏 Acknowledgements

- [Django](https://www.djangoproject.com/) — The web framework for perfectionists with deadlines
- [Bootstrap 5](https://getbootstrap.com/) — Powerful, extensible, feature-packed frontend toolkit
- [WeasyPrint](https://weasyprint.org/) — Pixel-perfect PDF generation from HTML/CSS
- [Google Fonts](https://fonts.google.com/) — Beautiful typography for all 6 templates
- [Bootstrap Icons](https://icons.getbootstrap.com/) — Over 1,800 open-source SVG icons

---

<div align="center">

**Built with ❤️ using Django**

⬡ [ResumeForge](https://github.com/yourusername/resumeforge) — Build better careers

<br/>

⭐ If this project helped you, please give it a star on GitHub!

---

## 👨‍💻 Author

<div align="center">

**Zeeshan Haider**

[![GitHub](https://img.shields.io/badge/GitHub-zeeshancodes-py-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/zeeshancodes-py)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-ZeeshanHaider-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/zeeshan-haider-4b307334b)
[![Email](https://img.shields.io/badge/Email-shanisipraa@gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:shanisipraa@gmail.com)

*Built and maintained with  by Your Name*

</div>
</div>
