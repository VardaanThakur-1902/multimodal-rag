from fastapi import APIRouter

from rag.rag_service import RAGService
from schemas.chat import ChatRequest

from fastapi.responses import StreamingResponse

router = APIRouter()

rag_service = RAGService()


@router.post("/")
def chat(request: ChatRequest):
    return rag_service.answer(request.question)

@router.post("/stream")
async def chat_stream(
    request: ChatRequest,
):

    rag = RAGService()

    return StreamingResponse(
        rag.answer_stream(
            request.question
        ),
        media_type="text/plain",
    )