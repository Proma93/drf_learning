# 📝 Django REST Framework Todo API

A simple RESTful API built using **Django** and **Django REST Framework (DRF)** for managing a list of Todo items.  
This project demonstrates how to implement basic CRUD (Create, Read, Update, Delete) operations for a Todo application with clean and structured API responses.

## 🚀 Features
✅ CRUD Functionality
Create, Read, Update, and Delete Todo items using RESTful endpoints.
✅ DRF Serializers for Validation
Ensures clean and validated input using Django REST Framework's powerful serializers.
✅ Exception Handling
Handles unexpected errors gracefully with clear and consistent error messages.
✅ Structured JSON Responses
All API responses follow a consistent JSON structure with status, message, and data.
✅ Modular & Extensible Codebase
Cleanly structured for easy maintenance and future enhancements.

## 🧱 Tech Stack
This project leverages the following technologies:

- [![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
- [![Django](https://img.shields.io/badge/Django-3.2%2B-green?logo=django)](https://www.djangoproject.com/)
- [![DRF](https://img.shields.io/badge/DRF-3.x-red?logo=django)](https://www.django-rest-framework.org/)


## 📂 Project Structure

todo_project/
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── drfproject/             # Django project configuration
│   ├── __init__.py
│   ├── settings.py         # Main settings file
│   ├── urls.py             # Root URL configuration
│   └── wsgi.py             # WSGI application
└── home/                   # Core application (e.g., Todo API)
    ├── __init__.py
    ├── models.py           # Database models
    ├── serializers.py      # DRF serializers for data validation
    ├── views.py            # API views (function/class-based)
    ├── urls.py             # App-level routing
    └── admin.py            # Admin site configuration









