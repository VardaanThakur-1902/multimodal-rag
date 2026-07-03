from sqlmodel import Session, select

from database.chat_models import ChatSession
from services.message_service import MessageService


class SessionService:

    @staticmethod
    def create(
        session: Session,
    ):

        chat = ChatSession()

        session.add(chat)

        session.commit()

        session.refresh(chat)

        return chat

    @staticmethod
    def list(
        session: Session,
    ):

        return session.exec(
            select(ChatSession)
        ).all()

    @staticmethod
    def delete(
        session_id: str,
        session: Session,
    ):

        MessageService.delete_all(
            session,
            session_id,
        )

        chat = session.get(
            ChatSession,
            session_id,
        )

        if chat:

            session.delete(chat)

            session.commit()

    @staticmethod
    def rename(
        session_id: str,
        title: str,
        session: Session,
    ):

        chat = session.get(
            ChatSession,
            session_id,
        )

        if chat:

            chat.title = title

            session.add(chat)

            session.commit()

            session.refresh(chat)

        return chat
    
