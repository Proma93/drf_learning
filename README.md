<h1 align="center">📝 Django REST Framework Todo API</h1>

<div align="justify">
A simple RESTful API built using **Django** and **Django REST Framework (DRF)** for managing a list of Todo items.  
This project demonstrates how to implement basic CRUD (Create, Read, Update, Delete) operations for a Todo application with clean and structured API responses.
</div>

## 🚀 Features

- **CRUD Functionality**: Create, Read, Update, and Delete Todo items using RESTful endpoints.
- **DRF Serializers for Validation**: Ensures clean and validated input using Django REST Framework's powerful serializers.
- **Exception Handling**: Handles unexpected errors gracefully with clear and consistent error messages.
- **Structured JSON Responses**: All API responses follow a consistent JSON structure with `status`, `message`, and `data` keys.
- **Modular & Extensible Codebase**: Cleanly structured for easy maintenance and future enhancements.


## 🧱 Tech Stack
This project leverages the following technologies:

- [![Python](https://img.shields.io/badge/Python-3.10.9%2B-blue?logo=python)](https://www.python.org/)
- [![Django](https://img.shields.io/badge/Django-5.2.4%2B-green?logo=django)](https://www.djangoproject.com/)
- [![DRF](https://img.shields.io/badge/DRF-3.16.0-red?logo=django)](https://www.django-rest-framework.org/)


## 📂 Project Structure

```text
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
```
## 🔧 Setup Instructions

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/todo-api.git
cd todo-api
```
### 2. Create and Activate a Virtual Environment

<details>
<summary><strong>macOS / Linux</strong></summary>
    
```bash
python -m venv venv
source venv/bin/activate
```
</details> 

<details> 
<summary><strong>Windows</strong></summary>
    
```bash
python -m venv venv
venv\Scripts\activate
```
</details>

### 3. Install Project Dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply Database Migrations
```bash
python manage.py migrate
```
### 5. Start the Development Server
```bash
python manage.py runserver
```
Once the server is running, visit http://localhost:8000 to access the API.








