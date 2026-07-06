import fitz
import pytesseract

from PIL import Image


class PageOCR:

    @staticmethod
    def extract(pdf_path: str, page_number: int):

        document = fitz.open(pdf_path)

        page = document.load_page(page_number - 1)

        pix = page.get_pixmap(dpi=300)

        image = Image.frombytes(
            "RGB",
            [pix.width, pix.height],
            pix.samples,
        )

        text = pytesseract.image_to_string(image)

        document.close()

        return text.strip()