from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.resume import router as resume_router

app = FastAPI(
    title="TalentOS API",
    version="1.0.0"
)

app.include_router(chat_router)
app.include_router(resume_router)


@app.get("/")
def root():
    return {
        "message": "TalentOS API is running 🚀"
    }