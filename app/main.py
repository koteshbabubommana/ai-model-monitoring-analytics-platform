from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Model Monitoring & Analytics Platform",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
async def root():
    return {
        "message": "AI Model Monitoring Platform Running"
    }