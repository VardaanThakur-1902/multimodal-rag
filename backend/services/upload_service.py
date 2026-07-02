from fastapi import UploadFile
from sqlmodel import Session

from database.models import Document
from services.storage_service import StorageService
from services.validation_service import ValidationService

from loaders.pdf_loader import PDFLoader
from processing.pipeline import ProcessingPipeline
from vectordb.chroma_manager import ChromaManager

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

        if extension == ".pdf":

            pdf_path = StorageService.get_path(
                stored_name,
                extension,
            )

            loader = PDFLoader()

            extracted_document = loader.load(
                str(pdf_path)
            )

            chunks = ProcessingPipeline.process(
                extracted_document
            )

            db = ChromaManager()

            db.add_chunks(chunks)

        return document