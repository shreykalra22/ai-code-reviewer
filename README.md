# 🤖 AI Code Reviewer API

An AI-powered backend API that analyzes source code and provides structured feedback on code quality, strengths, weaknesses, suggestions, and an overall score.

Built with FastAPI, Google Gemini, SQLAlchemy, SQLite, and Docker.

## ✨ Features

- AI-powered source code review using Google Gemini
- Structured feedback with:
  - Overall review
  - Strengths
  - Weaknesses
  - Improvement suggestions
  - Code quality score out of 10
- Store and manage review history
- Full CRUD operations for saved reviews
- Input validation using Pydantic
- Pagination with validated query parameters
- Newest reviews returned first
- Positive review ID validation
- AI service error handling
- Database transaction rollback protection
- Request and response logging
- Health check endpoint
- Interactive Swagger API documentation
- Dockerized application
- Persistent SQLite database using Docker volumes

## 🛠️ Tech Stack

- Python
- FastAPI
- Google Gemini API
- Google Gen AI SDK
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Docker
- Docker Compose
- Pytest

## 📁 Project Structure

```text
ai-code-reviewer/
├── app/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── config.py
│   ├── database.py
│   ├── logger.py
│   └── prompts.py
├── tests/
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
└── README.md
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API root |
| GET | `/health` | Check API health |
| POST | `/review` | Generate and save an AI code review |
| GET | `/reviews` | Get review history with pagination |
| GET | `/reviews/{review_id}` | Get a review by ID |
| PUT | `/reviews/{review_id}` | Update a saved review |
| DELETE | `/reviews/{review_id}` | Delete a saved review |

## 🧠 Example AI Review

### Request

```json
{
  "language": "Python",
  "code": "def divide(a, b):\n    return a / b"
}
```

### Response

```json
{
  "success": true,
  "id": 1,
  "language": "Python",
  "review": "The function is simple and readable but lacks validation for division by zero.",
  "score": 7,
  "strengths": [
    "Clear and concise implementation"
  ],
  "weaknesses": [
    "No handling for division by zero"
  ],
  "suggestions": [
    "Validate the divisor before performing division"
  ]
}
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/shreykalra22/ai-code-reviewer.git
cd ai-code-reviewer
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the environment file

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

### 5. Start the API

```bash
uvicorn main:app --reload
```

Open the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## 🐳 Run with Docker

Create the `.env` file first, then run:

```bash
docker compose up --build
```

The API will be available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

Stop the containers with:

```bash
docker compose down
```

## 🛡️ Validation and Error Handling

The API includes protection against:

- Empty or whitespace-only programming languages
- Empty or whitespace-only code submissions
- Oversized code submissions
- Invalid pagination values
- Invalid review IDs
- Invalid review scores
- Whitespace-only review updates
- Temporary AI service failures
- Invalid AI-generated JSON responses
- Database transaction failures

## 📌 What I Learned

Through this project, I gained practical experience with:

- Designing REST APIs with FastAPI
- Integrating an LLM into a backend application
- Building structured prompts for reliable JSON output
- Migrating to the Google Gen AI SDK
- Working with SQLAlchemy and SQLite
- Implementing validation and production-style error handling
- Adding application logging
- Containerizing a Python API with Docker
- Persisting application data using Docker volumes
- Testing and debugging APIs using Swagger UI

## 🔮 Future Improvements

- Add automated API tests
- Add authentication and user accounts
- Support multiple AI models
- Add asynchronous AI requests
- Add PostgreSQL support
- Build a frontend dashboard
- Add CI/CD workflows

## API Workflow

The API follows a simple request-to-review workflow:

1. A client submits source code and its programming language to the `POST /review` endpoint.
2. The request is validated using Pydantic.
3. The code is sent to the Gemini API using a structured review prompt.
4. The AI response is parsed and validated.
5. The generated review and score are stored in the SQLite database.
6. The structured review is returned to the client as a JSON response.

This design keeps API routing, validation, AI processing, and database operations separated across dedicated application layers.

## 👨‍💻 Author

**Shrey Kalra**

GitHub: `shreykalra22`

---

If you found this project useful, consider giving it a ⭐.

