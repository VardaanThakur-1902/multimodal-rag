from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session

from database.database import get_session
from services.session_service import SessionService

router = APIRouter()


@router.post("/")
def create_session(
    session: Session = Depends(get_session),
):

    return SessionService.create(session)


@router.get("/")
def list_sessions(
    session: Session = Depends(get_session),
):

    return SessionService.list(session)


@router.delete("/{session_id}")
def delete_session(
    session_id: str,
    session: Session = Depends(get_session),
):

    SessionService.delete(
        session_id,
        session,
    )

    return {
        "message": "Session deleted."
    }


@router.patch("/{session_id}")
def rename_session(
    session_id: str,
    title: str,
    session: Session = Depends(get_session),
):

    return SessionService.rename(
        session_id,
        title,
        session,
    )