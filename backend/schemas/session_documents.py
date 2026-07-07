from pydantic import BaseModel


class SessionDocumentsRequest(BaseModel):

    document_ids: list[str]