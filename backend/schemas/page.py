from pydantic import BaseModel


class PageData(BaseModel):

    page_number: int

    text: str

    has_text: bool

    has_images: bool

    has_tables: bool

    is_scanned: bool

    word_count: int

    character_count: int