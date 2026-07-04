from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlmodel import Session

from database.database import get_session
from rag.rag_service import RAGService
from schemas.chat import ChatRequest

router = APIRouter()

rag_service = RAGService()


@router.post("/")
def chat(
    request: ChatRequest,
    session: Session = Depends(get_session),
):

    return rag_service.answer(
        question=request.question,
        session_id=request.session_id,
        session=session,
    )


@router.post("/stream")
async def chat_stream(
    request: ChatRequest,
    session: Session = Depends(get_session),
):

    return StreamingResponse(
        rag_service.answer_stream(
            question=request.question,
            session_id=request.session_id,
            session=session,
        ),
        media_type="text/event-stream",
    )