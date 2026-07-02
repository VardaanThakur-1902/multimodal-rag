from pydantic import BaseModel


class ImageCaption(BaseModel):

    document_name: str

    page_number: int

    image_number: int

    image_path: str

    caption: str
    