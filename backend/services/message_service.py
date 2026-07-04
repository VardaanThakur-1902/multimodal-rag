import json

from sqlmodel import Session, select

from database.chat_models import ChatMessage


class MessageService:

    @staticmethod
    def add(
        session: Session,
        session_id: str,
        role: str,
        content: str,
        sources: str | None = None,
    ):

        message = ChatMessage(
            session_id=session_id,
            role=role,
            content=content,
            sources=sources,
        )

        session.add(message)

        session.commit()

        session.refresh(message)

        return message

    @staticmethod
    def list(
        session: Session,
        session_id: str,
    ):

        return session.exec(
            select(ChatMessage)
            .where(
                ChatMessage.session_id == session_id
            )
        ).all()

    @staticmethod
    def delete_all(
        session: Session,
        session_id: str,
    ):

        messages = session.exec(
            select(ChatMessage)
            .where(
                ChatMessage.session_id == session_id
            )
        ).all()

        for message in messages:
            session.delete(message)

        session.commit()

    @staticmethod
    def recent_history(
        session: Session,
        session_id: str,
        limit: int = 10,
    ):

        messages = session.exec(
            select(ChatMessage)
            .where(
                ChatMessage.session_id == session_id
            )
            .order_by(ChatMessage.created_at.desc())
            .limit(limit)
        ).all()

        messages.reverse()

        return [
            {
                "role": message.role,
                "content": message.content,
                "sources": (
                    json.loads(message.sources)
                    if message.sources
                    else []
                ),
            }
            for message in messages
        ]