from fastapi import APIRouter, Depends
from sqlmodel import Session

from database.database import get_session
from schemas.session import SessionCreate
from services.session_service import SessionService

router = APIRouter()


@router.post("/")
def create_session(
    data: SessionCreate,
    db: Session = Depends(get_session),
):
    return SessionService.create(
        data.name,
        db,
    )


@router.get("/")
def get_sessions(
    db: Session = Depends(get_session),
):
    return SessionService.get_all(
        db,
    )


@router.delete("/{session_id}")
def delete_session(
    session_id: str,
    db: Session = Depends(get_session),
):
    return SessionService.delete(
        session_id,
        db,
    )