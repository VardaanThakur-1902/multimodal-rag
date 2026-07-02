from uuid import uuid4
from typing import Any

from pydantic import BaseModel, Field


class Chunk(BaseModel):

    chunk_id: str = Field(
        default_factory=lambda: str(uuid4())
    )

    document_name: str

    page_number: int

    chunk_type: str

    content: str

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )