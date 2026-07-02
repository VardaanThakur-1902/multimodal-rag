from pydantic import BaseModel


class ImageData(BaseModel):

    document_name: str

    page_number: int

    image_number: int

    image_path: str