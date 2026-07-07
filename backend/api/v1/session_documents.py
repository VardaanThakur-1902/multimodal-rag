from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session

from database.database import get_session
from schemas.response import APIResponse
from schemas.session_documents import SessionDocumentsRequest
from services.session_document_service import (
    SessionDocumentService,
)

router = APIRouter()

@router.post("/{session_id}/documents")
def attach_documents(
    session_id: str,
    request: SessionDocumentsRequest,
    session: Session = Depends(get_session),
):

    SessionDocumentService.attach_documents(
        session=session,
        session_id=session_id,
        document_ids=request.document_ids,
    )

    return APIResponse(
        success=True,
        message="Documents attached successfully.",
    )

@router.get("/{session_id}/documents")
def get_session_documents(
    session_id: str,
    session: Session = Depends(get_session),
):

    documents = (
        SessionDocumentService.get_documents(
            session=session,
            session_id=session_id,
        )
    )

    return APIResponse(
        success=True,
        message="Documents retrieved successfully.",
        data=documents,
    )