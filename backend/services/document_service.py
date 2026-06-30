from pathlib import Path

from sqlmodel import Session
from sqlmodel import select

from config.settings import UPLOAD_DIR
from database.models import Document
from services.storage_service import StorageService


class DocumentService:

    @staticmethod
    def get_all(session: Session):

        return session.exec(
            select(Document)
        ).all()

    @staticmethod
    def delete(
        document_id: str,
        session: Session,
    ):

        document = session.get(
            Document,
            document_id,
        )

        if not document:
            return None

        folder = StorageService.FOLDER_MAP[
            document.file_type
        ]

        file_path = (
            Path(UPLOAD_DIR)
            / folder
            / document.stored_name
        )

        if file_path.exists():
            file_path.unlink()

        session.delete(document)
        session.commit()

        return document