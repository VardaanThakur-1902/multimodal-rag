from datetime import datetime
from uuid import uuid4

from sqlmodel import Field, SQLModel
from typing import Optional


class ChatSession(SQLModel, table=True):

    id: str = Field(
        default_factory=lambda: str(uuid4()),
        primary_key=True,
    )

    title: str = "New Chat"

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
    )


class ChatMessage(SQLModel, table=True):

    id: str = Field(
        default_factory=lambda: str(uuid4()),
        primary_key=True,
    )

    session_id: str

    role: str

    content: str

    # Store citations as JSON string
    sources: Optional[str] = None

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
    )