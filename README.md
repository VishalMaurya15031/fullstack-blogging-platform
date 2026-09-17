# 🚀 BlogPulse — Full-Stack Django Blogging Application

A modern, feature-rich Full-Stack Blogging Web Application built with **Python 3.12**, **Django**, and a custom **Glassmorphism CSS Design System**.

---

## ✨ Key Features

- 🎨 **Modern Dark Glassmorphism UI**: High-contrast, responsive design with glow effects, custom CSS tokens, and Google Fonts (`Outfit` + `Inter`).
- 🏷️ **Category Management**: Organized posts by topic badges (AI, Web Dev, UI/UX, Architecture, Tutorials).
- 🔍 **Real-Time Search & Filtering**: Instant search across article titles, content, and category tags.
- 📖 **Rich Article Reader**: Converts Markdown syntax to HTML, includes reading progress bar, estimated read time, and view count tracking.
- 💬 **Interactive Comments**: Approved discussion threads with author identification.
- 👤 **User Authentication & Profile Dashboard**: User registration, login/logout, and personal author dashboard for managing published stories vs. drafts.
- ⚙️ **Django Administrative Portal**: Complete back-office control over posts, categories, and comment moderation.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.12, Django 5.x / 6.x
- **Database**: SQLite (Development) / PostgreSQL compatible
- **Frontend**: HTML5, Modern Vanilla CSS (Glassmorphism), JavaScript (ES6)
- **Utilities**: Markdown parser, Pillow for media management

---

## ⚡ Quick Start Guide

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/django-blogpulse.git
cd django-blogpulse
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv .venv
# On Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations & Seed Sample Data
```bash
python manage.py makemigrations
python manage.py migrate
python seed_data.py
```

### 5. Start Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 🔑 Default Credentials (After Seeding)
- **Username**: `admin`
- **Password**: `admin123`
- **Admin URL**: `http://127.0.0.1:8000/admin/`

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
