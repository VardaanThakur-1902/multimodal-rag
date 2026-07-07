from fastapi import FastAPI

from api.v1.chat import router as chat_router
from api.v1.health import router as health_router

from database.database import create_db

from api.v1.upload import router as upload_router
from api.v1.documents import router as document_router

from fastapi.middleware.cors import CORSMiddleware

from api.v1.sessions import router as sessions_router
from api.v1.messages import router as messages_router
from api.v1 import session_documents

app = FastAPI(
    title="Multimodal RAG",
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

app.include_router(
    sessions_router,
    prefix="/api/v1/sessions",
    tags=["Sessions"],
)

app.include_router(
    messages_router,
    prefix="/api/v1/messages",
    tags=["Messages"],
)

app.include_router(
    session_documents.router,
    prefix="/api/v1/sessions",
    tags=["Session Documents"],
)