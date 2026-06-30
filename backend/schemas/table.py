from pydantic import BaseModel


class TableData(BaseModel):

    page_number: int

    table_index: int

    markdown: str

    rows: int

    columns: int