<h1 align="center">📝 Task Track API using Django REST Framework </h1>

<div align="justify">
Designed and implemented a fully containerized, secure, and scalable task management REST API using Django REST Framework. Leveraged ModelViewSet, nested serializers, and DjangoFilterBackend to create a clean, DRY endpoint architecture. The API supports authenticated CRUD operations on tasks and their schedules, integrates custom permissions and request throttling for security and performance, and features interactive API documentation via Swagger (drf-yasg). Deployed and distributed the app through Docker Hub, enabling anyone to run the project without setup overhead.ces.
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
- [API Documentation (Swagger UI)](#api-documentation-swagger-ui)
- [Run This Project via Docker](#run-this-project-via-docker)

---
## Features

- CRUD operations for Todo and TimingTodo
- Authentication: Token and Session Authentication
- Permissions: Custom permissions enable controlled API access for both authenticated and unauthenticated users.
- Throttling: Configured for both anonymous and authenticated users
- Custom Pagination with limit-offset
- DjangoFilterBackend and DRF's SearchFilter & OrderingFilter
- Nested endpoint for creating and managing TimingTodo for a specific Todo
- Integrated Swagger UI for interactive, developer-friendly API documentation and testing experience.
- Containerized and published the application using Docker and Docker Hub, enabling consistent development, deployment, and one-command execution without local setup overhead.

---

## Tech Stack
This project leverages the following technologies:

| **Layer**            | **Technology**                                                  | **Description**                                  |
| -------------------- | --------------------------------------------------------------- | ------------------------------------------------ |
| 🐍 Language         | [Python 3.10+](https://www.python.org/)                         | Core programming language                        |
| 🌐 Web Framework    | [Django 5.2](https://www.djangoproject.com/)                    | High-level web framework for rapid development   |
| 🔗 API Toolkit      | [Django REST Framework](https://www.django-rest-framework.org/) | Flexible toolkit to build Web APIs               |
| 🔍 Filtering        | [django-filter](https://django-filter.readthedocs.io/)          | Add filtering to DRF views                       |
| 📚 Docs Generator   | [drf-yasg](https://drf-yasg.readthedocs.io/)                    | Auto-generate Swagger/OpenAPI docs               |
| 🧰 Dev Utilities    | [django-extensions](https://django-extensions.readthedocs.io/)  | Useful dev commands like `shell_plus`, etc.      |
| ⚙️ Env Config       | [python-dotenv](https://pypi.org/project/python-dotenv/)        | Loads environment variables from `.env` files    |
| 🐳 Containerization | [Docker](https://www.docker.com/)                               | Containerize the app for any environment         |
| 📦 Image Hosting    | [Docker Hub](https://hub.docker.com/)                           | Store and distribute Docker images               |
| 🧱 Database         | [SQLite](https://www.sqlite.org/index.html) (default)           | Lightweight, file-based database for dev/testing |
| 🔧 Orchestration    | [Docker Compose](https://docs.docker.com/compose/) *(optional)* | Manage multi-container setups (DB, Redis, etc.)  |


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
├── .dockerignore           # Lists files/directories Docker should ignore during image build
├── docker-compose.yml      # Defines multi-container Docker applications
├── Dockerfile              # Contains instructions to build a Docker image
├── Makefile                # (Optional) Defines shell commands for development workflow automation
├── README.md               # Project overview, setup instructions, usage, etc.
├── drfproject/             # Django project configuration
│   ├── __init__.py
│   ├── settings.py         # Main settings file
│   ├── urls.py             # Root URL configuration
│   └── wsgi.py             # WSGI application
└── home/                   # Core application (e.g., Todo API)
    ├── __init__.py
    ├── models.py           # Database models
    ├── serializers.py      # DRF serializers for data validation
    ├── views.py            # API views (ModelViewSet)
    ├── permissions.py      # Custom permission classes for the Task Management API
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

## API Testing with Postman
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

## API Documentation (Swagger UI)
This **Task Track (Todo) API** project is integrated with **Swagger UI** for easy exploration and testing of available endpoints.

📄 **Access the interactive documentation:**  
[http://localhost:8000/swagger/](http://localhost:8000/swagger/) &nbsp;_(only available in development mode)_

✅ Anyone can view and interact with the API directly through the Swagger interface when the server is running locally.

---

## Run This Project via Docker
You can pull and run this API directly from Docker Hub:

🔹 Pull the Image
```bash
docker pull proma93/drf_learning-web:latest
```
🔹 Run the API Server
```bash
docker run -p 8000:8000 proma93/drf_learning-web:latest
```
🔹 Optional: Run Database Migrations
If you're using SQLite and running the image for the first time:

```bash

docker volume create drf_data

docker run --rm \
  -v drf_data:/app/data \
  yourusername/drf-api:latest \
  python manage.py migrate
```
Then:

```bash
docker run -p 8000:8000 -v drf_data:/app/data proma93/drf_learning-web:latest
```
>🌐 Visit: http://localhost:8000

#### 📦 Docker Hub
You can find the published image here:
👉 https://hub.docker.com/r/proma93/drf_learning-web



















