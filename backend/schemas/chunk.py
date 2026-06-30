from pydantic import BaseModel


class Chunk(BaseModel):

    chunk_id: str

    document_name: str

    page_number: int

    chunk_type: str

    content: str

    metadata: dict = {}