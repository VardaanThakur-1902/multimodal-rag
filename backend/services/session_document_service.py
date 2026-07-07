from sqlmodel import Session
from sqlmodel import select

from database.models import Document
from database.session_document import SessionDocument


class SessionDocumentService:

    @staticmethod
    def attach_documents(
        session: Session,
        session_id: str,
        document_ids: list[str],
    ):

        for document_id in document_ids:

            mapping = SessionDocument(
                session_id=session_id,
                document_id=document_id,
            )

            session.add(mapping)

        session.commit()

    @staticmethod
    def get_documents(
        session: Session,
        session_id: str,
    ):

        statement = (
            select(Document)
            .join(
                SessionDocument,
                Document.id ==
                SessionDocument.document_id,
            )
            .where(
                SessionDocument.session_id ==
                session_id
            )
        )

        return session.exec(statement).all()