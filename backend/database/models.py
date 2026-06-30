from datetime import datetime
from typing import Optional
from uuid import uuid4

from sqlmodel import Field
from sqlmodel import SQLModel


class Document(SQLModel, table=True):

    id: str = Field(
        default_factory=lambda: str(uuid4()),
        primary_key=True,
    )

    original_name: str

    stored_name: str

    file_type: str

    mime_type: str

    size: int

    collection: str = "Default"

    status: str = "uploaded"

    processed: bool = False

    uploaded_at: datetime = Field(
        default_factory=datetime.utcnow
    )