from fastapi import FastAPI

app=FastAPI(
    title="AI- Code Reviewer API",
    description="Backend API for AI powered code reviews",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to the AI Code Reviewer API!"
    }



@app.get("/health")
def health():
    return {"status": "Ok",
            "version": "1.0.0"
            }
