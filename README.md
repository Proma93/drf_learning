<h1 align="center">📝 Task Management API using Django REST Framework </h1>

<div align="justify">
Built a fully-featured RESTful API using Django REST Framework (DRF) with support for CRUD operations on todo tasks and their related timings. Implemented robust features including token-based authentication, user permissions, request throttling, filtering, search, ordering, and custom pagination. Leveraged ModelViewSet, DjangoFilterBackend, and nested serializers to ensure a clean, extensible, and secure API design.
</div>

---

## 📚 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Models](#models)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Permission Classes](#permission-classes)
- [Throttling](#throttling)
- [Filtering, Search, and Ordering](#filtering-search-and-ordering)
- [API Testing](#api-testing)

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

#### 🔑 Authentication Example (Token-Based)
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

## Authentication
This project uses TokenAuthentication and SessionAuthentication methods to secure all API endpoints.
- TokenAuthentication – for API clients and mobile apps
- SessionAuthentication – for browser-based sessions (e.g., admin panel, DRF browsable API)

### Step-by-Step Setup
#### 1️⃣ Install Required Packages
If not already installed, install Django REST Framework and Token Authentication:

```bash
pip install djangorestframework
```
<details>
<summary><strong>Optionally</strong></summary>
    
```bash
pip install djangorestframework-authtoken
```
</details>  

#### 2️⃣ Update INSTALLED_APPS
Add the following apps in drfproject/settings.py:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]
```
#### 3️⃣ Configure DRF Authentication Classes
Update your REST_FRAMEWORK config in drfproject/settings.py:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```
#### 4️⃣ Apply Migrations
Run the following command to create the necessary tables for token authentication:
```bash
python manage.py migrate
```

#### 5️⃣ Create a Superuser (Optional but recommended)

```bash
python manage.py createsuperuser
```
This account can be used to generate tokens and access the browsable API.

#### 6️⃣ Generate Authentication Token for a User
You can generate a token for a specific user using DRF's built.in Auth Endpoint.
Enable the default token endpoint by adding this to your project-level urls.py (usually drfproject/urls.py):
```python
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    ...
    path('api-token-auth/', obtain_auth_token),
]
```

#### 🔑 Example Request:

```http
POST /api-token-auth/
Content-Type: application/json
```
```json
{
  "username": "your_username",
  "password": "your_password"
}

```
#### 🔑 Example Response:

```json
{
  "token": "2a376d4a5b2e..." 
}

```
#### 7️⃣ Use Token in API Requests
Send the token in the Authorization header for all API requests.

```http
Authorization: Token your_token_here
```
#### 🔐 Example with Postman

- Go to Authorization tab
- Type: Token
- Value: your_token_here
- Header will be automatically added as:

```http
Authorization: Token your_token_here
```
---

## Permission Classes
All views use the IsAuthenticated permission class to restrict access to logged-in users only.

#### Configuration in settings.py

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```
You can also apply permissions at the view level using:
```python
from rest_framework.permissions import IsAuthenticated

permission_classes = [IsAuthenticated]
```
--- 

## Throttling
Rate limiting is applied to protect the API from abuse using:
- AnonRateThrottle – for unauthenticated users
- UserRateThrottle – for authenticated users
#### Configuration in settings.py


```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/day',
        'user': '1000/day',
    },
}
```
--- 

## Filtering, Search, and Ordering
This API supports powerful data querying features including:

- Field-based filtering (DjangoFilterBackend)
- Search across fields (SearchFilter)
- Ordering results (OrderingFilter)

#### Configuration in settings.py

```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}
```

#### Usage in Views

```python
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

filter_backends = [
    DjangoFilterBackend,
    filters.SearchFilter,
    filters.OrderingFilter,
]

filterset_fields = ['is_done']
search_fields = ['todo_title', 'todo_description']
ordering_fields = ['created_at', 'todo_title']
ordering = ['created_at']
```

#### Example API Queries
🔹 Filter by completion

```http
GET /todos/?is_done=true
```
🔹 Search in title or description

```http
GET /todos/?search=test
```
🔹 Order by title

```http
GET /todos/?ordering=todo_title
```

## API Testing

You can test the API endpoints using:

- **Postman**  
- **cURL**  
- **Django Browsable API** at [http://127.0.0.1:8000](http://127.0.0.1:8000)

#### API Testing with Postman
POST /todos/

🔹 Headers:

```http
Content-Type: application/json
Authorization: Token your_token_here
```

🔹 Body:

```json
{
  "todo_title": "Learn DRF",
  "todo_description": "Practice ViewSets and Throttling",
  "is_done": false
}

```
🔹 Response:

```json
{
  "status": true,
  "message": "Todo created successfully",
  "data": {
    "uid": "uuid-value",
    "todo_title": "Learn DRF",
    "todo_description": "Practice ViewSets and Throttling",
    "is_done": false,
    ...
  }
}


```


---























