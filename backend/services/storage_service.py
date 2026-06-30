import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from config.settings import UPLOAD_DIR


class StorageService:

    FOLDER_MAP = {
        ".pdf": "pdf",
        ".docx": "docx",
        ".txt": "text",
        ".csv": "csv",
        ".xlsx": "excel",
        ".png": "images",
        ".jpg": "images",
        ".jpeg": "images",
    }

    @classmethod
    def save(
        cls,
        file: UploadFile,
        extension: str,
    ):

        folder = cls.FOLDER_MAP[extension]

        destination = (
            Path(UPLOAD_DIR)
            / folder
        )

        destination.mkdir(
            parents=True,
            exist_ok=True,
        )

        filename = (
            f"{uuid4()}{extension}"
        )

        file_path = (
            destination
            / filename
        )

        with open(
            file_path,
            "wb",
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer,
            )

        return filename