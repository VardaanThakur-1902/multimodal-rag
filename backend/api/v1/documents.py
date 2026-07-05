from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session

from database.database import get_session
from schemas.response import APIResponse
from services.document_service import DocumentService

from fastapi.responses import FileResponse
from pathlib import Path

from config.settings import UPLOAD_DIR
from services.storage_service import StorageService
from database.models import Document

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

@router.get("/{document_id}/preview")
def preview_document(
    document_id: str,
    session: Session = Depends(get_session),
):

    document = session.get(
        Document,
        document_id,
    )

    if not document:
        return APIResponse(
            success=False,
            message="Document not found.",
        )

    folder = StorageService.FOLDER_MAP[
        document.file_type
    ]

    file_path = (
        Path(UPLOAD_DIR)
        / folder
        / document.stored_name
    )

    if not file_path.exists():

        return APIResponse(
            success=False,
            message="File not found.",
        )

    return FileResponse(
        path=file_path,
        media_type=document.mime_type,
        filename=document.original_name,
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