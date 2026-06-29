from fastapi import FastAPI

from api.chat import router as chat_router
from api.health import router as health_router

app = FastAPI(
    title="Multimodal RAG",
    version="1.0.0"
)

app.include_router(
    health_router,
    prefix="/health",
    tags=["Health"]
)

app.include_router(
    chat_router,
    prefix="/chat",
    tags=["Chat"]
)