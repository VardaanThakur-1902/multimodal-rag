from pydantic import BaseModel
from typing import Any


class RAGResponse(BaseModel):
    answer: str
    sources: list[dict[str, Any]]