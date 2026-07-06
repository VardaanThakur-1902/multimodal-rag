from sqlmodel import Session
from sqlmodel import select

from database.models import Session as DBSession


class SessionService:

    @staticmethod
    def create(
        name: str,
        db: Session,
    ):

        session = DBSession(
            name=name,
        )

        db.add(session)
        db.commit()
        db.refresh(session)

        return session

    @staticmethod
    def get_all(
        db: Session,
    ):

        return db.exec(
            select(DBSession)
        ).all()

    @staticmethod
    def delete(
        session_id: str,
        db: Session,
    ):

        session = db.get(
            DBSession,
            session_id,
        )

        if not session:
            return None

        db.delete(session)
        db.commit()

        return session