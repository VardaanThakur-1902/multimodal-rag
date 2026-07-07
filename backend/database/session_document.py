from sqlmodel import SQLModel
from sqlmodel import Field


class SessionDocument(SQLModel, table=True):

    session_id: str = Field(
        foreign_key="session.id",
        primary_key=True,
    )

    document_id: str = Field(
        foreign_key="document.id",
        primary_key=True,
    )