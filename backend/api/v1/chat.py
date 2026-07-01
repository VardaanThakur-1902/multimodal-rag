from fastapi import APIRouter

from rag.rag_service import RAGService
from schemas.chat import ChatRequest

router = APIRouter()

rag_service = RAGService()


@router.post("/")
def chat(request: ChatRequest):
    return rag_service.answer(request.question)