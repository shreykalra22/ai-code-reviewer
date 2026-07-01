from app.database import engine, Base
from app.models.review import Review
from fastapi import FastAPI
from app.routers.review import router as review_router
from app.middleware import log_requests

app=FastAPI(
    title="AI- Code Reviewer API",
    description="Backend API for AI powered code reviews",
    version="1.0.0"
)
app.middleware("http")(log_requests)
print(Base.metadata.tables.keys())
Base.metadata.create_all(bind=engine)
app.include_router(review_router)

@app.get("/")
def root():
    return {"message": "Welcome to the AI Code Reviewer API!"
    }



@app.get("/health")
def health():
    return {"status": "Ok",
            "version": "1.0.0"
            }
