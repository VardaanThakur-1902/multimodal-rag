from fastapi import FastAPI

from api.v1.chat import router as chat_router
from api.v1.health import router as health_router

from database.database import create_db

from api.v1.upload import router as upload_router
from api.v1.documents import router as document_router

app = FastAPI(
    title="Multimodal RAG",
    version="1.0.0",
)


@app.on_event("startup")
def startup():

    create_db()


app.include_router(
    health_router,
    prefix="/api/v1/health",
    tags=["Health"],
)

app.include_router(
    chat_router,
    prefix="/api/v1/chat",
    tags=["Chat"],
)

app.include_router(
    upload_router,
    prefix="/api/v1/upload",
    tags=["Upload"],
)

app.include_router(
    document_router,
    prefix="/api/v1/documents",
    tags=["Documents"],
)