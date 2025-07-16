<h1 align="center">📝 Django REST Framework Todo API</h1>

<div align="justify">
A simple RESTful API built using Django and Django REST Framework (DRF) for managing a list of Todo items.  
This project demonstrates how to implement basic CRUD (Create, Read, Update, Delete) operations for a Todo application with clean and structured API responses.
</div>

---

## 📚 Table of Contents

- [Features](#features)
- [Tech Stack](#-tech-stack)
- [Setup Instructions](#-setup-instructions)
- [Project Structure](#-project-structure)
- [Model: Todo](#-model-todo)
- [API Endpoints](#-api-endpoints)
- [API Testing with Postman](#-api-testing-with-postman)

---
## 🚀 Features

- **CRUD Functionality**: Create, Read, Update, and Delete Todo items using RESTful endpoints.
- **DRF Serializers for Validation**: Ensures clean and validated input using Django REST Framework's powerful serializers.
- **Exception Handling**: Handles unexpected errors gracefully with clear and consistent error messages.
- **Structured JSON Responses**: All API responses follow a consistent JSON structure with `status`, `message`, and `data` keys.
- **Modular & Extensible Codebase**: Cleanly structured for easy maintenance and future enhancements.

---

## 🧱 Tech Stack
This project leverages the following technologies:

- [![Python](https://img.shields.io/badge/Python-3.10.9%2B-blue?logo=python)](https://www.python.org/)
- [![Django](https://img.shields.io/badge/Django-5.2.4%2B-green?logo=django)](https://www.djangoproject.com/)
- [![DRF](https://img.shields.io/badge/DRF-3.16.0-red?logo=django)](https://www.django-rest-framework.org/)

---

## 🔧 Setup Instructions

Follow these steps to set up the project on your local machine:

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/drf_learning.git
cd drf_learning
```
#### 2. Create and Activate a Virtual Environment

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

#### 3. Install Project Dependencies
```bash
pip install -r requirements.txt
```
<details>
<summary><strong>Or manually</strong></summary>
    
```bash
pip install django djangorestframework
```
</details>  

#### 4. Apply Database Migrations
```bash
python manage.py migrate
```
#### 5. Start the Development Server
```bash
python manage.py runserver
```
Once the server is running, visit http://localhost:8000 to access the API.

---

## 📂 Project Structure

```text
drf_learning/
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

---

## 🧾 Model: `Todo`

| Field             | Type      | Description                       |
|-------------------|-----------|-----------------------------------|
| `uid`             | UUID      | Unique identifier (primary key)   |
| `todo_title`      | CharField | Short title of the task           |
| `todo_description`| TextField | Detailed description              |
| `is_done`         | Boolean   | Completion status (default: False)|
| `created_at`      | Date      | Auto-updated on creation          |
| `updated_at`      | Date      | Auto-updated on each save         |

---

## 📌 API Endpoints

### 🏠 Home Test Endpoint

**URL**: `/home/`  
**Methods**: `GET`, `POST`, `PATCH`

| Method | Description          |
|--------|----------------------|
| GET    | Test endpoint        |
| POST   | Test POST method     |
| PATCH  | Test PATCH method    |

### 📥 Create Todo

**URL**: `/post-todo/`  
**Method**: `POST`  
**Description**: Create a new todo item.

#### ✅ Request Example:

```json
{
  "todo_title": "Finish DRF Guide",
  "todo_description": "Write a README and document all API endpoints.",
  "is_done": false
}
```
#### ✅ Success Response:

```json
{
  "status": true,
  "message": "valid or success data",
  "data": {
    "uid": "uuid-value",
    "todo_title": "Finish DRF Guide",
    "todo_description": "Write a README and document all API endpoints.",
    "is_done": false,
    "created_at": "2025-07-16",
    "updated_at": "2025-07-16"
  }
}
```

### 📥 Get All Todos

**URL**: `/get-todo/`  
**Method**: `GET`  
**Description**: Fetch all todo entries.

#### ✅ Example Response:

```json
{
  "status": true,
  "message": "Todo fetched",
  "data": [
    {
      "uid": "uuid-value",
      "todo_title": "Example Todo",
      "todo_description": "Sample description",
      "is_done": false,
      "created_at": "2025-07-16",
      "updated_at": "2025-07-16"
    },
    ...
  ]
}
```

### ✏️ Update Todo

**URL**: `/patch-todo/<uid>/`  
**Method**: `PATCH`  
**Description**: Partially update a todo item.

#### ✅ Request Example:

```json
{
  "is_done": true
}
```

#### ✅ Success Response:

```json
{
  "status": true,
  "message": "Todo updated successfully",
  "data": {
    "uid": "uuid-value",
    "todo_title": "Example Todo",
    "todo_description": "Sample description",
    "is_done": true,
    "created_at": "2025-07-16",
    "updated_at": "2025-07-16"
  }
}
```

#### ❌ Not Found Response:

```json
{
  "status": false,
  "message": "Todo not found"
}
```
---

## 🧪 API Testing

You can test the API endpoints using:

- **Postman**  
- **cURL**  
- **Django Browsable API** at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 API Testing with Postman

You can test the `/post-todo/` endpoint using **Postman** by following the steps below:

### 🔧 Request Configuration

- **Method:** `POST`  
- **URL:** `http://127.0.0.1:8000/post-todo/`  
- **Headers:**
  ```http
  Content-Type: application/json

### 📦 Request Body

Set the body to raw and choose JSON as the format. Then paste the following payload:

```json
{
  "todo_title": "Learn DRF",
  "todo_description": "Study API views and serializers",
  "is_done": false
}
```

### ▶️ Sending the Request

Once you've configured everything:

- Click Send.

- You should receive a JSON response indicating the todo was successfully created.

---























