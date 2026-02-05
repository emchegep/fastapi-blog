# FastAPI Blog Application
A full-stack blog application built with FastAPI, providing both:

- A JSON REST API for programmatic access

- HTML pages rendered with Jinja2 for users browsing in a web browser

The application includes user authentication, database persistence, file uploads, background tasks, and a clean, modular project structure suitable for real-world use.

---

## 🚀Project Overview
This project is a production-style blog application built using FastAPI. It serves two types of clients:

1. Programmatic clients (via a RESTful JSON API)

2. End users (via server-rendered HTML pages using Jinja2 templates)

The backend is powered by SQLAlchemy for database interactions and Pydantic for data validation. The application implements complete CRUD operations, secure user authentication, file uploads, background tasks, and clean routing using FastAPI routers.

The project is designed to be:

- Easy to understand and extend

- Fast and scalable

- Suitable for learning, portfolios, or production foundations

- Runnable locally using uv or inside Docker containers

---

## ✨ Key Features
### Backend & API

- FastAPI-based REST API

- Full CRUD operations for blog posts and users

- Pydantic schemas for request/response validation

- SQLAlchemy ORM for database access

- JWT-based authentication and authorization

- Secure password hashing

- Cleanly organized routers and modules

### Frontend

- Server-side rendered HTML pages using Jinja2

- User-friendly pages for browsing blog posts

- Forms for registration, login, and content creation

- Shared backend logic with the JSON API

### Additional Functionality

- User registration and login

- Profile picture uploads

- Background tasks (e.g. sending emails)

- Environment-based configuration

- Automatic API documentation (Swagger & ReDoc)

### Dev & Deployment

- Dependency management with uv

- Docker & Docker Compose support

- Reproducible builds using uv.lock

---

## 🛠️ Tech Stack

- Python 3.13+

- FastAPI

- Jinja2

- SQLAlchemy

- Pydantic

- Uvicorn

- JWT (JSON Web Tokens)

- uv

- Docker & Docker Compose

---