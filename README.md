# FastAPI Blog

A full-stack blog application built with FastAPI, featuring user authentication, blog post management, templates, static assets, and database integration.

## Features

- User registration and authentication
- Secure password handling
- User profile management
- Blog post creation and management
- Post listing and retrieval
- Database-backed application
- HTML templates
- Static CSS/JavaScript assets
- Email-related utilities
- Image handling

## Tech Stack

- **Backend:** FastAPI
- **Language:** Python
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Authentication:** JWT / password authentication
- **Frontend:** HTML, CSS, JavaScript
- **Templates:** Jinja2

## Project Structure

```text
FastAPI-blog/
│
├── routers/
│   ├── __init__.py
│   ├── posts.py
│   └── users.py
│
├── templates/
├── static/
│
├── auth.py
├── config.py
├── database.py
├── email_utils.py
├── image_utils.py
├── main.py
├── models.py
├── schemas.py
├── blog.db
├── requirements.txt
└── .gitignore
