from fastapi import UploadFile
from sqlmodel import Session

from database.models import Document
from services.storage_service import StorageService
from services.validation_service import ValidationService


class UploadService:

    @staticmethod
    async def upload(
        file: UploadFile,
        session: Session,
    ):

        extension = await ValidationService.validate(file)

        stored_name = StorageService.save(
            file,
            extension,
        )

        document = Document(
            original_name=file.filename,
            stored_name=stored_name,
            file_type=extension,
            mime_type=file.content_type,
            size=file.size or 0,
        )

        session.add(document)
        session.commit()
        session.refresh(document)

        return document