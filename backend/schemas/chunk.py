from uuid import uuid4

from pydantic import BaseModel
from pydantic import Field


class Chunk(BaseModel):

    chunk_id: str = Field(
        default_factory=lambda: str(uuid4())
    )

    document_name: str

    page_number: int

    chunk_type: str

    content: str

    metadata: dict = Field(
        default_factory=dict
    )