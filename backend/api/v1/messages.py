import json

from fastapi import APIRouter, Depends
from sqlmodel import Session

from database.database import get_session
from services.message_service import MessageService

router = APIRouter()


@router.get("/{session_id}")
def get_messages(
    session_id: str,
    session: Session = Depends(get_session),
):

    messages = MessageService.list(
        session,
        session_id,
    )

    return [
        {
            "id": message.id,
            "session_id": message.session_id,
            "role": message.role,
            "content": message.content,
            "sources": (
                json.loads(message.sources)
                if message.sources
                else []
            ),
            "created_at": message.created_at,
        }
        for message in messages
    ]