import os

from fastapi import HTTPException
from fastapi import UploadFile

from config.constants import ALLOWED_EXTENSIONS
from config.settings import MAX_FILE_SIZE


class ValidationService:

    @staticmethod
    async def validate(file: UploadFile):

        extension = os.path.splitext(
            file.filename
        )[1].lower()

        if extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail="Unsupported file type.",
            )

        contents = await file.read()

        if len(contents) == 0:
            raise HTTPException(
                status_code=400,
                detail="Empty file.",
            )

        if len(contents) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=400,
                detail="File exceeds maximum size.",
            )

        await file.seek(0)

        return extension