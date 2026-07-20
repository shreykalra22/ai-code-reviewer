<div align="center">

# ⚙️ AI Code Reviewer Backend

### AI-Powered REST API for Intelligent Code Analysis

A production-inspired backend built with **FastAPI**, **Google Gemini AI**, **SQLAlchemy**, and **JWT Authentication** to provide secure, scalable, and intelligent code review services.

<br>

![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange?style=for-the-badge)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue?style=for-the-badge)

---

### 🚀 Built using FastAPI • SQLAlchemy • Google Gemini AI • JWT Authentication

</div>

---

# 📖 Overview

AI Code Reviewer Backend is a secure REST API that powers the AI Code Reviewer platform.

It integrates Google's Gemini AI to analyze source code, generate intelligent reviews, detect bugs, suggest improvements, and produce production-ready code.

The backend follows a modular architecture with authentication, database management, AI services, analytics, and review history while exposing clean REST APIs for the frontend.

---

# ✨ Core Features

## 🤖 AI Code Analysis

- Google Gemini AI Integration
- Intelligent Code Review
- Bug Detection
- Code Quality Analysis
- Performance Suggestions
- Security Recommendations
- Best Practice Recommendations
- Production Ready Code Generation
- AI Quality Score

---

## 🔐 Authentication

- User Registration
- Secure Login
- JWT Authentication
- Password Hashing
- Protected Routes
- Token Verification
- Secure API Access

---

## 🗄 Database Management

- SQLAlchemy ORM
- SQLite Database
- User Management
- Review History
- Persistent Storage
- CRUD Operations

---

## 📊 Analytics

- Review Statistics
- Language Analytics
- Average Quality Score
- Dashboard Data APIs
- Recent Reviews
- Performance Insights

---

# 🏛 Backend Architecture

```text
                    Client Request
                           │
                           ▼
                    FastAPI Router
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
 Authentication       Review Service    Dashboard
          │                │                │
          ▼                ▼                ▼
      JWT Security    Gemini AI Engine   Analytics
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    SQLAlchemy ORM
                           │
                           ▼
                     SQLite Database
```

---

# 📂 Project Structure

```text
backend
│
├── app
│   ├── auth
│   ├── database
│   ├── models
│   ├── routers
│   ├── schemas
│   ├── services
│   ├── middleware
│   ├── utils
│   └── core
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.11 |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | SQLite |
| Authentication | JWT |
| Password Security | Passlib + BCrypt |
| Validation | Pydantic |
| AI | Google Gemini API |
| API Testing | Swagger UI |
| ASGI Server | Uvicorn |

---

# ⚙ Installation

## Clone Repository

```bash
git clone <YOUR_BACKEND_REPOSITORY_URL>

cd AI-Code-Reviewer-Backend
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Server

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 🚀 Request Flow

```text
Frontend
    │
    ▼
FastAPI Router
    │
    ▼
Authentication
    │
    ▼
Review Service
    │
    ▼
Google Gemini AI
    │
    ▼
Review Response
    │
    ▼
Database Storage
    │
    ▼
JSON Response
```
---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

SECRET_KEY=YOUR_SECRET_KEY

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

DATABASE_URL=sqlite:///./database.db
```

> **Note:** Never commit your `.env` file or API keys to GitHub.

---

# 🔗 REST API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive JWT access token |

---

## AI Code Review

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/review` | Submit code for AI analysis |

---

## Review Management

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/reviews` | Get all reviews |
| GET | `/reviews/{id}` | Get a specific review |
| PUT | `/reviews/{id}` | Update a review |
| DELETE | `/reviews/{id}` | Delete a review |

---

## Dashboard

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/dashboard` | Retrieve dashboard analytics |

---

# 🔐 Security Features

The backend follows secure development practices including:

- JWT Authentication
- Password Hashing using BCrypt
- Protected Routes
- Token Validation
- Input Validation with Pydantic
- Environment Variable Configuration
- ORM-Based Database Access
- Structured Exception Handling
- Secure API Design

---

# 🗄 Database Schema

## User

| Field | Type |
|------|------|
| id | Integer |
| username | String |
| email | String |
| password | Hashed String |

---

## Review

| Field | Type |
|------|------|
| id | Integer |
| user_id | Integer |
| language | String |
| original_code | Text |
| review | Text |
| improved_code | Text |
| quality_score | Integer |
| created_at | DateTime |

---

# 🤖 Google Gemini AI Integration

Google Gemini AI is responsible for analyzing submitted source code and generating intelligent feedback.

The backend sends the source code to Gemini AI and processes the response to extract:

- Code Quality Score
- Bugs
- Security Issues
- Performance Suggestions
- Best Practices
- Readability Improvements
- Production Readiness
- Improved Version of the Code

---

# 📊 Dashboard Analytics

The backend aggregates review data to provide analytics for the frontend dashboard.

Metrics include:

- Total Reviews
- Average Quality Score
- Programming Language Distribution
- Weekly Review Activity
- Recent Reviews
- Overall Platform Insights

---

# ⚡ Performance Optimizations

The application is designed with scalability in mind.

Implemented optimizations include:

- Modular Architecture
- Dependency Injection
- SQLAlchemy ORM
- Reusable Services
- Clean API Routing
- Efficient CRUD Operations
- Structured Error Handling

---

# 🧪 Testing Checklist

The backend has been verified for:

- User Registration
- User Login
- JWT Authentication
- Protected Endpoints
- AI Review Generation
- CRUD Operations
- Dashboard APIs
- Database Persistence
- Error Handling

---

# 🚀 Future Improvements

Planned enhancements include:

- PostgreSQL Support
- Docker Containerization
- Redis Caching
- Celery Background Tasks
- Rate Limiting
- API Versioning
- Refresh Tokens
- Role-Based Access Control (RBAC)
- OAuth Login
- Email Verification
- Password Reset
- CI/CD Integration
- Unit & Integration Testing
- Cloud Deployment (AWS, Azure, GCP)

---

# 📚 Learning Outcomes

This backend project demonstrates practical experience with:

- FastAPI Development
- REST API Design
- SQLAlchemy ORM
- JWT Authentication
- Password Hashing
- Google Gemini AI Integration
- Environment Configuration
- Dependency Injection
- CRUD Operations
- Modular Backend Architecture
- Clean Code Principles
- Production-Oriented API Development

---

# 👨‍💻 Author

## Shrey Kalra

**B.Sc. Computer Science (AI & ML)**

**VIT Vellore**

### Connect with me

**GitHub**

https://github.com/shreykalra22

**LinkedIn**

https://www.linkedin.com/in/shrey-kalraaaa

---

# 📄 License

This project is licensed under the MIT License.

See the **LICENSE** file for more details.

---

# 🙏 Acknowledgements

This project was built using the following amazing technologies:

- FastAPI
- Python
- SQLAlchemy
- Google Gemini AI
- SQLite
- JWT
- Passlib
- Pydantic
- Uvicorn

Special thanks to the open-source community for providing the tools and libraries that made this project possible.

---

<div align="center">

# ⭐ If you found this project useful, please consider giving it a Star!

### Built with ❤️ using FastAPI, Python & Google Gemini AI

**Happy Coding 🚀**

</div>