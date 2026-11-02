# AVERA - Django Academic Project

AVERA is an informational and awareness platform designed to educate, raise awareness and facilitate supporter engagements around child adoption and child support. The system architecture follows a clean, modular Django app layout based on project requirements.

## Features and Included Modules

- Accounts (accounts): User registration, login, profile management and authentication.
- Adoption Hub (adoption): Information and guides on adoption awareness and processes.
- Child Profiles (children): Child information directory with strict privacy protocols.
- FAQ and Support (faq): Frequently asked questions and help desk assistance.
- Feedback System (feedback): Platform reviews and supporter testimonials.
- Notifications (notifications): In-app real-time status alerts for users and supporters.
- Organizations (organizations): Directory and profiles of verified care institutions.
- Success Stories (stories): Impact stories, adoption journeys and growth logs.
- Support and Wishlists (support): Child support, wishlist fulfillment and transparent gift tracking (Sent -> Received -> Delivered -> Used).

## Tech Stack

- Language: Python 3.13+
- Framework: Django 5.2+
- Database: SQLite (Default for local development)
- Frontend Framework: HTML5, CSS3, JS, Bootstrap 5, Bootstrap Icons
- Image Processing: Pillow

## Project Directory Structure

avera_project/
│
├── accounts/               # User Authentication & Profile App
├── adoption/               # Adoption Info & Awareness App
├── Avera/                  # Main Django Settings & Core Routing Directory
├── children/               # Child Profiles & Privacy Management App
├── faq/                    # FAQ & Help Center App
├── feedback/               # Supporter Feedback & Reviews App
├── notifications/          # Alerts & Notification System App
├── organizations/          # Verified Care Institutions App
├── static/                 # Global Static Files (CSS, JS, Assets)
├── stories/                # Success Story Showcase App
├── support/                # Wishlist & Gift Tracking Journey App
├── feedback/                
│
├── templates/              
│   ├── accounts/
│   ├── adoption/
│   ├── children/
│   ├── faq/
│   ├── notifications/
│   ├── organization/
│   ├── story/
│   ├── feedback/
│   ├── support/
│   ├── base.html           # Master Layout
│   └── home.html           # Homepage
│
├── db.sqlite3              # Local Database
├── manage.py               # Project Execution Script
└── README.md               # Documentation

## How to Run the Project (Windows / PyCharm)

1. Open Project:
   Open the root project folder in PyCharm.

2. Install Dependencies:
   Open the PyCharm Terminal and run:
   pip install django pillow

3. Apply Database Migrations:
   python manage.py makemigrations
   python manage.py migrate

4. Create Superuser (Admin Access):
   python manage.py createsuperuser

5. Start Local Development Server:
   python manage.py runserver

6. Access Application:
   - Web App: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Important Note

AVERA is implemented strictly as an informational and awareness platform. It does not process official legal adoption applications, nor does it claim to replace official governmental adoption authorities.