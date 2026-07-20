from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.middleware import log_requests

# Import Models
from app.models.review import Review
from app.models.user import User

# Import Routers
from app.routers.review import router as review_router
from app.routers.dashboard import router as dashboard_router
from app.routers.auth import router as auth_router


app = FastAPI(
    title="AI Code Reviewer API",
    description="Backend API for AI Powered Code Reviews",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(log_requests)

Base.metadata.create_all(bind=engine)

app.include_router(review_router)
app.include_router(dashboard_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the AI Code Reviewer API!"
    }


@app.get("/health")
def health():
    return {
        "status": "OK",
        "version": "1.0.0"
    }