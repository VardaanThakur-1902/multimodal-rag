from typing import Any

from pydantic import BaseModel

from schemas.page import PageData
from schemas.table import TableData


class ExtractedDocument(BaseModel):

    text: str = ""

    pages: list[PageData] = []

    tables: list[TableData] = []

    images: list[Any] = []

    metadata: dict[str, Any] = {}