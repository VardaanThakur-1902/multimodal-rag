from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session

from database.database import get_session
from schemas.response import APIResponse
from services.document_service import DocumentService

router = APIRouter()


@router.get("/")
def get_documents(
    session: Session = Depends(get_session),
):

    documents = DocumentService.get_all(
        session
    )

    return APIResponse(
        success=True,
        message="Documents retrieved.",
        data=documents,
    )


@router.delete("/{document_id}")
def delete_document(
    document_id: str,
    session: Session = Depends(get_session),
):

    document = DocumentService.delete(
        document_id,
        session,
    )

    if document is None:
        return APIResponse(
            success=False,
            message="Document not found.",
        )

    return APIResponse(
        success=True,
        message="Document deleted.",
    )