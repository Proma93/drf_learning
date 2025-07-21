<h1 align="center">📝 Todo API with DRF (ModelViewSet + Throttling + Filtering + Token Auth) </h1>

<div align="justify">
This project is a fully featured Django REST Framework based API for managing Todo tasks and their associated timings.
It includes user authentication, permissions, filtering, search, ordering, throttling, and custom pagination.
</div>

---

## 📚 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Models](#models)
- [API Endpoints](#api-endpoints)
- [API Testing with Postman](#api-testing-with-postman)

---
## Features

- CRUD operations for Todo and TimingTodo
- Authentication: Token and Session Authentication
- Permissions: Only authenticated users can access the API
- Throttling: Configured for both anonymous and authenticated users
- Custom Pagination with limit-offset
- DjangoFilterBackend and DRF's SearchFilter & OrderingFilter
- Nested endpoint for creating and managing TimingTodo for a specific Todo

---

## Tech Stack
This project leverages the following technologies:

- [![Python](https://img.shields.io/badge/Python-3.10.9%2B-blue?logo=python)](https://www.python.org/)
- [![Django](https://img.shields.io/badge/Django-5.2.4%2B-green?logo=django)](https://www.djangoproject.com/)
- [![DRF](https://img.shields.io/badge/DRF-3.16.0-red?logo=django)](https://www.django-rest-framework.org/)
- Django PostgreSQL / SQLite
- Django Filter

---

## Setup Instructions

Follow these steps to set up the project on your local machine:

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
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

#### 5. Create a superuser:

```bash
python manage.py createsuperuser
```

#### 6. Start the Development Server
```bash
python manage.py runserver
```
Once the server is running, visit http://localhost:8000 to access the API.

#### 7. Obtain Auth Token (after logging in):
```http
POST /token/
```

## 🔑 Authentication Example (Token-Based)
Include the token in the Authorization header:
```http
Authorization: Token your_token_here
```
---

## Project Structure

```text
drf_learning/
├── manage.py               # Django management script
├── env                     # Python virtual environments
├── requirements.txt        # Python dependencies
├── .gitignore              # Specifies intentionally untracked files to ignore
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

## Models 
#### `Todo`

| Field             | Type      | Description                       |
|-------------------|-----------|-----------------------------------|
| `uid`             | UUID      | Unique identifier (primary key)   |
| `user`            | FK        | Linked authenticated user         |
| `todo_title`      | CharField | Short title of the task           |
| `todo_description`| TextField | Detailed description              |
| `is_done`         | Boolean   | Completion status (default: False)|
| `created_at`      | Date      | Auto-updated on creation          |
| `updated_at`      | Date      | Auto-updated on each save         |

#### `TimingTodo`

| Field           | Type      | Description                |
| --------------- | --------- | -------------------------- |
| `uid`           | UUID      | Unique ID for timing entry |
| `todo`          | FK        | Related `Todo`             |
| `schedule_date` | Date      | Date the task is scheduled |
| `start_time`    | Time      | Optional start time        |
| `end_time`      | Time      | Optional end time          |
| `note`          | TextField | Additional notes           |

---

## API Endpoints

#### 📌 Todo Endpoints

| Method | Endpoint        | Description              |
| ------ | --------------- | ------------------------ |
| GET    | `/todos/`       | List all todos           |
| POST   | `/todos/`       | Create a new todo        |
| GET    | `/todos/{uid}/` | Retrieve a specific todo |
| PATCH  | `/todos/{uid}/` | Partially update a todo  |
| DELETE | `/todos/{uid}/` | Delete a todo            |


#### 🕒 Nested TimingTodo under Todo

| Method | Endpoint                      | Description                        |
| ------ | ----------------------------- | ---------------------------------- |
| GET    | `/todos/{uid}/timings/`       | List timings of a specific todo    |
| POST   | `/todos/{uid}/timings/`       | Add a timing to a specific todo    |
| GET    | `/todos/{uid}/timings/{tid}/` | Retrieve specific timing           |
| PATCH  | `/todos/{uid}/timings/{tid}/` | Partially update a specific timing |
| DELETE | `/todos/{uid}/timings/{tid}/` | Delete a specific timing           |

#### 🔄 All TimingTodo Endpoints

| Method | Endpoint    | Description               |
| ------ | ----------- | ------------------------- |
| GET    | `/timings/` | List all timing entries   |
| POST   | `/timings/` | Create a new timing entry |

---

## API Testing

You can test the API endpoints using:

- **Postman**  
- **cURL**  
- **Django Browsable API** at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## API Testing with Postman

You can test the `/post-todo/` endpoint using **Postman** by following the steps below:

#### 🔧 Request Configuration

- **Method:** `POST`  
- **URL:** `http://127.0.0.1:8000/post-todo/`  
- **Headers:**
  ```http
  Content-Type: application/json

#### 📦 Request Body

Set the body to raw and choose JSON as the format. Then paste the following payload:

```json
{
  "todo_title": "Learn DRF",
  "todo_description": "Study API views and serializers",
  "is_done": false
}
```

#### ▶️ Sending the Request

Once you've configured everything:

- Click Send.

- You should receive a JSON response indicating the todo was successfully created.

---























