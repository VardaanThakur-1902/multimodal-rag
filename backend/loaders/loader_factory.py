from pathlib import Path

from loaders.pdf_loader import PDFLoader
from loaders.docx_loader import DocxLoader
from loaders.txt_loader import TxtLoader
from loaders.csv_loader import CSVLoader
from loaders.excel_loader import ExcelLoader
from loaders.image_loader import ImageLoader


class LoaderFactory:

    LOADERS = {
        ".pdf": PDFLoader,
        ".docx": DocxLoader,
        ".txt": TxtLoader,
        ".csv": CSVLoader,
        ".xlsx": ExcelLoader,
        ".png": ImageLoader,
        ".jpg": ImageLoader,
        ".jpeg": ImageLoader,
    }

    @classmethod
    def get_loader(cls, file_path: str):

        extension = Path(
            file_path
        ).suffix.lower()

        loader = cls.LOADERS.get(
            extension
        )

        if loader is None:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return loader()