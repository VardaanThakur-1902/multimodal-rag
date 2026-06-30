from datetime import datetime

from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: str
    original_name: str
    stored_name: str
    file_type: str
    mime_type: str
    size: int
    collection: str
    status: str
    processed: bool
    uploaded_at: datetime

    class Config:
        from_attributes = True