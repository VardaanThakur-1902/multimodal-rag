from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session

from database.database import get_session
from services.message_service import MessageService

router = APIRouter()


@router.get("/{session_id}")
def get_messages(
    session_id: str,
    session: Session = Depends(get_session),
):

    return MessageService.list(
        session,
        session_id,
    )