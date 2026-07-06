from ocr.ocr_service import OCRService
from schemas.image_caption import ImageCaption
from schemas.image_data import ImageData


class ImageCaptioner:

    @staticmethod
    def generate(image: ImageData) -> ImageCaption:

        ocr_text = OCRService.extract_text(
            image.image_path
        )

        if ocr_text:

            caption = f"""
OCR Text:

{ocr_text}
"""

        else:

            caption = (
                f"Image extracted from page "
                f"{image.page_number} "
                f"of document {image.document_name}."
            )

        return ImageCaption(
            document_name=image.document_name,
            page_number=image.page_number,
            image_number=image.image_number,
            image_path=image.image_path,
            caption=caption,
        )