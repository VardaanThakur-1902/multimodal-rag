from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class ImageChunk(BaseModel):

    chunk_id: str = Field(
        default_factory=lambda: str(uuid4())
    )

    document_name: str

    page_number: int

    image_path: str

    caption: str

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )